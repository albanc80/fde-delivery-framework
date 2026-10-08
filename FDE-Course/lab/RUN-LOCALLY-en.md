# Run the Python exercises after cloning

Use synthetic tickets only. The app uses rules, not an AI model, and never sends customer messages. Python 3.14 is the tested version. Native Python uses only the standard library; no pip installation or paid AI account is required. Git is needed to clone. Docker Desktop is an alternative to installing Python locally.

## Windows PowerShell: native Python

```powershell
git clone https://github.com/albanc80/fde-delivery-framework.git
Set-Location fde-delivery-framework/FDE-Course/lab
py -3.14 --version
py -3.14 test_app.py
```

The completed reference must report `Ran 7 tests` and `OK`. Individual routing and validation examples also run as subtests. If the launcher cannot find 3.14, install Python 3.14 before using these commands. The tests start their own temporary local server and database, then clean them up; do not start the app separately to run tests.

Start the interactive reference in this same folder:

```powershell
$env:TRAINING_TOKEN = 'course-local-example-token'
py -3.14 run_local.py
```

Open http://127.0.0.1:8088 and enter `course-local-example-token`. Create a suggestion, inspect its reason, choose or override the queue, then save the human decision. The new `run_local.py` helper binds only to this computer and stores events in `lab/.data/events.sqlite`. It uses the original app without changing its routing or API behavior. Press Ctrl+C to stop. Start it again to retain your events. If port 8088 is busy, use `py -3.14 run_local.py --port 8090` and open http://127.0.0.1:8090.

## macOS/Linux: native Python

```sh
git clone https://github.com/albanc80/fde-delivery-framework.git
cd fde-delivery-framework/FDE-Course/lab
python3.14 --version
python3.14 test_app.py
export TRAINING_TOKEN=course-local-example-token
python3.14 run_local.py
```

Open http://127.0.0.1:8088 and use the same teaching token. Stop with Ctrl+C. Use `--port 8090` if needed. Keep this teaching service local.

## Implement the exercise

1. Run the unchanged reference tests first and observe a full review in the browser.
2. Open `starter_route.py`. Its `NotImplementedError` is intentional. Implement `route(text)` so it returns `(queue, explanation)`.
3. Match categories case-insensitively. The reference recognizes access (`password`, `login`, `access`, `contraseña`, `acceso`), billing (`invoice`, `billing`, `refund`, `factura`, `reembolso`) and incident (`outage`, `offline`, `incident`, `caída`, `incidente`). Zero or multiple category matches must return `manual`.
4. Keep a copy of the completed `app.py` outside the exercise file. Replace only its `route` function with your implementation. The provided tests import `app`, so editing the starter file alone does not change the tested service.
5. Run `py -3.14 test_app.py` on Windows or `python3.14 test_app.py` on macOS/Linux again. Keep all seven test groups passing. Add an ambiguous-category test and a test confirming that refund text cannot authorize a refund or send a message.
6. Stop and restart the app after changing Python code; it does not reload automatically. Keep suggestions separate from reviewed decisions.
7. Record your Frame Card, prediction and stop evidence before opening `case-results.json`. Recompute the synthetic medians and error counts from `northstar-review-sample.csv`. Functional tests do not prove productivity or adoption.
8. Adapt the design to the staged maintenance capstone. Update category rules, allowed queues, review-screen choices and your maintenance tests together. Retain supervisor authority, manual handling of ambiguity and visible escalation.

## Docker alternative

From `FDE-Course/lab`, with Docker Desktop running:

```sh
docker compose up -d --build
```

Open http://localhost:8088 and enter `course-local-example-token`. Docker provides Python 3.14 and keeps the host port on loopback. Do not run this alongside the native app on the same port. PowerShell reference tests:

```powershell
docker run --rm -v "${PWD}:/lab:ro" -w /lab python:3.14-alpine python test_app.py
```

macOS/Linux reference tests:

```sh
docker run --rm -v "$PWD:/lab:ro" -w /lab python:3.14-alpine python test_app.py
```

After changing app code, rebuild with `docker compose up -d --build`. Stop with `docker compose stop`; restart with `docker compose start`. `docker compose down` removes the lab container/network and retains its training-data volume. Do not add `-v` unless you intend to discard those records.

## Read the course locally

From the repository root, open `FDE-Course/index.html`, then choose English or Spanish. Preserve the folder structure for video and caption paths. Quizzes and notes run in your browser. Notes are local to that browser and origin; notes from a local file do not automatically appear on the online site. GitHub Pages serves the learning materials; the Python exercise runs on your computer.
