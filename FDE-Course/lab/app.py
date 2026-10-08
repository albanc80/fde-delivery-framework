"""Local synthetic teaching service. Never use as a production deployment."""
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from datetime import datetime, timezone, timedelta
import json, os, secrets, sqlite3, threading, uuid

ROOT=Path(__file__).parent
TOKEN=os.environ.get('TRAINING_TOKEN','')
LOCK=threading.Lock()
DB=os.environ.get('EVENT_DB','/data/events.sqlite')
QUEUES={'access','billing','incident','manual'}

def connect():
    c=sqlite3.connect(DB,timeout=10); c.row_factory=sqlite3.Row
    return c
def setup():
    Path(DB).parent.mkdir(parents=True,exist_ok=True)
    with connect() as c:
        c.execute('CREATE TABLE IF NOT EXISTS events (id TEXT PRIMARY KEY, kind TEXT NOT NULL, ticket_id TEXT NOT NULL, suggestion_id TEXT NOT NULL, queue TEXT NOT NULL, created_at TEXT NOT NULL)')
        c.execute("CREATE UNIQUE INDEX IF NOT EXISTS one_decision ON events(suggestion_id) WHERE kind='decision'")
def validate(data,now=None):
    now=now or datetime.now(timezone.utc)
    if not isinstance(data,dict): raise ValueError('Expected an object')
    if not isinstance(data.get('id'),str) or not 1<=len(data['id'])<=80: raise ValueError('Invalid ticket identifier')
    if not isinstance(data.get('text'),str) or not 1<=len(data['text'])<=2000: raise ValueError('Text must contain 1 to 2000 characters')
    if data.get('status')!='open': raise ValueError('Only open tickets are eligible')
    try: created=datetime.fromisoformat(data['created_at'].replace('Z','+00:00'))
    except (KeyError,TypeError,ValueError,AttributeError): raise ValueError('Invalid timestamp')
    if created.tzinfo is None: raise ValueError('Timezone is required')
    age=now-created
    if age<timedelta(0) or age>timedelta(days=7): raise ValueError('Ticket must be within the past seven days')
    return data
def route(text):
    text=text.casefold()
    matches=[]
    for q,words in {'access':['password','login','access','contraseña','acceso'],'billing':['invoice','billing','refund','factura','reembolso'],'incident':['outage','offline','incident','caída','incidente']}.items():
        if any(w in text for w in words): matches.append(q)
    if len(matches)!=1: return 'manual','No single unambiguous category; human review required'
    return matches[0],'Deterministic keyword baseline; human review required'
def event(kind,ticket,suggestion,queue):
    e={'id':str(uuid.uuid4()),'kind':kind,'ticket_id':ticket,'suggestion_id':suggestion,'queue':queue,'created_at':datetime.now(timezone.utc).isoformat()}
    with connect() as c: c.execute('INSERT INTO events VALUES(:id,:kind,:ticket_id,:suggestion_id,:queue,:created_at)',e)
    return e

class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args): pass  # Do not log tokens or ticket bodies.
    def send(self,status,data,ctype='application/json'):
        raw=json.dumps(data,ensure_ascii=False).encode() if ctype=='application/json' else data.encode()
        self.send_response(status);self.send_header('Content-Type',ctype+'; charset=utf-8');self.send_header('Content-Length',str(len(raw)));self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.send_header('Referrer-Policy','no-referrer');self.end_headers();self.wfile.write(raw)
    def allowed(self):
        candidate=self.headers.get('Authorization','')
        return bool(TOKEN) and secrets.compare_digest(candidate.encode(),('Bearer '+TOKEN).encode())
    def do_GET(self):
        if self.path=='/': return self.send(200,(ROOT/'review.html').read_text(encoding='utf-8'),'text/html')
        if self.path=='/health': return self.send(200,{'status':'ok','scope':'synthetic-training-only'})
        if not self.allowed(): return self.send(401,{'error':'Authorized training token required'})
        if self.path=='/api/events':
            with connect() as c: rows=[dict(r) for r in c.execute('SELECT * FROM events ORDER BY created_at')]
            return self.send(200,rows)
        if self.path=='/api/metrics':
            with connect() as c: counts=dict(c.execute('SELECT kind,COUNT(*) FROM events GROUP BY kind'))
            return self.send(200,{'suggestions':counts.get('suggestion',0),'decisions':counts.get('decision',0),'outcome_review_time':'not_measured','adoption':'not_established'})
        return self.send(404,{'error':'Unknown endpoint'})
    def do_POST(self):
        if not self.allowed(): return self.send(401,{'error':'Authorized training token required'})
        try:
            length=int(self.headers.get('Content-Length','0'))
            if not 0<length<=12000: return self.send(413,{'error':'Invalid body size'})
            data=json.loads(self.rfile.read(length))
            if not isinstance(data,dict): raise ValueError('Expected an object')
            if self.path=='/api/triage':
                ticket=validate(data);queue,reason=route(ticket['text']);sid=str(uuid.uuid4())
                event('suggestion',ticket['id'],sid,queue)
                return self.send(200,{'ticket_id':ticket['id'],'suggestion_id':sid,'queue':queue,'reason':reason,'human_review_required':True,'messages_sent':0,'source':'rule-baseline'})
            if self.path=='/api/decision':
                sid=data.get('suggestion_id');queue=data.get('queue')
                if not isinstance(sid,str) or not isinstance(queue,str) or queue not in QUEUES: raise ValueError('Valid suggestion identifier and queue required')
                with LOCK:
                    with connect() as c: row=c.execute("SELECT * FROM events WHERE suggestion_id=? AND kind='suggestion'",(sid,)).fetchone()
                    if row is None: return self.send(404,{'error':'Suggestion not found'})
                    try: saved=event('decision',row['ticket_id'],sid,queue)
                    except sqlite3.IntegrityError: return self.send(409,{'error':'Decision already recorded'})
                return self.send(200,{'decision':saved,'overridden':queue!=row['queue'],'messages_sent':0})
            return self.send(404,{'error':'Unknown endpoint'})
        except (ValueError,TypeError,UnicodeDecodeError) as exc: return self.send(422,{'error':str(exc)})

if __name__=='__main__':
    if not TOKEN: raise SystemExit('Set TRAINING_TOKEN before starting')
    setup();ThreadingHTTPServer(('0.0.0.0',8080),Handler).serve_forever()
