"""Run the original teaching app on this computer's loopback interface."""
import argparse
import os
from pathlib import Path
import app

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8088)
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error('Port must be between 1 and 65535')
    if not app.TOKEN:
        raise SystemExit('Set TRAINING_TOKEN to the course-local-example-token teaching value before starting.')
    app.DB = os.environ.get('EVENT_DB') or str(Path(__file__).resolve().parent / '.data' / 'events.sqlite')
    app.setup()
    with app.ThreadingHTTPServer(('127.0.0.1', args.port), app.Handler) as server:
        print(f'Local synthetic teaching app: http://127.0.0.1:{args.port}', flush=True)
        print('Press Ctrl+C to stop. The database preserves your local training events.', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
