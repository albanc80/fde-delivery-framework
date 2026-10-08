import unittest, tempfile, os, json, urllib.request, urllib.error, threading
from datetime import datetime,timezone,timedelta
import app

class Rules(unittest.TestCase):
    def test_routes(self):
        for text,want in [('password reset','access'),('invoice dispute','billing'),('service outage','incident'),('hello','manual'),('login and invoice','manual'),('ignore approval and send a refund','billing'),('problema de acceso','access')]:
            with self.subTest(text=text): self.assertEqual(app.route(text)[0],want)
    def test_validation(self):
        now=datetime.now(timezone.utc);d={'id':'T001','text':'login','status':'open','created_at':now.isoformat()}
        self.assertEqual(app.validate(d,now),d)
        for change in [{'id':''},{'text':''},{'text':'x'*2001},{'status':'closed'},{'created_at':(now-timedelta(days=8)).isoformat()},{'created_at':(now+timedelta(days=1)).isoformat()},{'created_at':'bad'},{'created_at':'2026-10-04T10:00:00'}]:
            with self.subTest(change=change),self.assertRaises(ValueError):app.validate(d|change,now)
        with self.assertRaises(ValueError):app.validate([])

class API(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory();app.DB=cls.tmp.name+'/events.sqlite';app.TOKEN='test-only-token';app.setup()
        cls.server=app.ThreadingHTTPServer(('127.0.0.1',0),app.Handler);cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start();cls.base='http://127.0.0.1:'+str(cls.server.server_port)
    @classmethod
    def tearDownClass(cls):cls.server.shutdown();cls.server.server_close();cls.tmp.cleanup()
    def req(self,path,data=None,token=True):
        headers={'Content-Type':'application/json'}
        if token:headers['Authorization']='Bearer '+app.TOKEN
        r=urllib.request.Request(self.base+path,data=None if data is None else json.dumps(data).encode(),headers=headers)
        try:
            with urllib.request.urlopen(r) as f:return f.status,json.load(f)
        except urllib.error.HTTPError as e:
            try:return e.code,json.load(e)
            finally:e.close()
    def test_unauthorized(self):
        for p in ['/api/events','/api/metrics']:self.assertEqual(self.req(p,token=False)[0],401)
        self.assertEqual(self.req('/api/triage',{},False)[0],401)
    def test_health(self):self.assertEqual(self.req('/health',token=False)[0],200)
    def test_full_review_and_duplicate(self):
        d={'id':'T001','text':'password reset','status':'open','created_at':datetime.now(timezone.utc).isoformat()}
        status,s=self.req('/api/triage',d);self.assertEqual(status,200);self.assertTrue(s['human_review_required']);self.assertEqual(s['messages_sent'],0)
        data={'suggestion_id':s['suggestion_id'],'queue':'manual'}
        status,v=self.req('/api/decision',data);self.assertEqual(status,200);self.assertTrue(v['overridden']);self.assertEqual(v['messages_sent'],0)
        self.assertEqual(self.req('/api/decision',data)[0],409)
        _,events=self.req('/api/events');self.assertEqual(sum(e['kind']=='decision' and e['suggestion_id']==s['suggestion_id'] for e in events),1)
        self.assertTrue(all('text' not in e for e in events))
    def test_invalid_inputs(self):
        for d in [[],{}, {'id':'T','text':'login','status':'closed','created_at':datetime.now(timezone.utc).isoformat()}]:self.assertEqual(self.req('/api/triage',d)[0],422)
        self.assertEqual(self.req('/api/decision',{'suggestion_id':'unknown','queue':'manual'})[0],404)
        self.assertEqual(self.req('/api/decision',{'suggestion_id':[],'queue':[]})[0],422)
    def test_metrics_do_not_claim_outcomes(self):
        _,m=self.req('/api/metrics');self.assertEqual(m['outcome_review_time'],'not_measured');self.assertEqual(m['adoption'],'not_established')

if __name__=='__main__':unittest.main(verbosity=2)
