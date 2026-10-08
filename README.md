# Forward Deployed Delivery — free bilingual course

Learn an industry-agnostic delivery methodology and mindset through framing, a guided Python prototype, human review, evidence, adoption and a staged capstone. Intended for technical professionals entering FDE roles. Cases are fictional; the local prototype is a deterministic rule baseline.

- [Open the course online](https://albanc80.github.io/fde-delivery-framework/)
- [Download the complete offline learner ZIP](https://github.com/albanc80/fde-delivery-framework/releases/latest)
- [English: clone and run the Python exercises](FDE-Course/lab/RUN-LOCALLY-en.md)
- [Español: clonar y ejecutar los ejercicios Python](FDE-Course/lab/RUN-LOCALLY-es.md)
- [Start here](FDE-Course/START-HERE.md) · [License scope](FDE-Course/LICENSING.md) · [Source attribution](FDE-Course/sources/PROVENANCE.md)

## Clone and read locally

```sh
git clone https://github.com/albanc80/fde-delivery-framework.git
```

Open FDE-Course/index.html in your browser and choose English or Spanish. Clone/download the whole repository, not an individual HTML file. Keep all relative paths intact for media, captions and downloads. Each language has nine modules, 36 lessons, 38 videos, quizzes, notes, transcripts, workbooks, worked answers and editable slides. Browser notes remain local to their browser/origin and do not automatically move between offline and online readers.

## Python exercises — Windows PowerShell

Install Git and Python 3.14. No pip dependencies or paid AI account are needed. After cloning:

```powershell
Set-Location fde-delivery-framework/FDE-Course/lab
py -3.14 test_app.py
$env:TRAINING_TOKEN = 'course-local-example-token'
py -3.14 run_local.py
```

Expect seven test groups and OK. Open http://127.0.0.1:8088 and enter the example token. Press Ctrl+C to stop. The native helper binds to this computer and preserves records in lab/.data/events.sqlite. If the port is busy, add --port 8090. See the linked guides for the starter exercise, tests, rebuilding and troubleshooting.

## Python exercises — macOS/Linux

Install Git and Python 3.14, then:

```sh
cd fde-delivery-framework/FDE-Course/lab
python3.14 test_app.py
export TRAINING_TOKEN=course-local-example-token
python3.14 run_local.py
```

## Docker alternative

With Docker Desktop running, from FDE-Course/lab:

```sh
docker compose up -d --build
```

Open http://localhost:8088 and use the same teaching token. Docker supplies Python 3.14. Do not run the native helper and Docker on the same port. GitHub Pages serves the static readers; the Python exercise runs on your computer.

## Free edition and license

Sales pages, marketing kits, publisher setup guides, launch checklist, upload manifest and private production-source files were removed. All learner lessons, media, workbooks, answers, templates, lab and attribution remain. The introduction videos and cover art remain because they are used by the readers.

**Course content: CC BY 4.0 for original contributions. Code: MIT.** See [the explicit scope and third-party exclusions](FDE-Course/LICENSING.md), [complete CC BY terms](LICENSE-CONTENT.txt) and [rights register](FDE-Course/sources/RIGHTS-REGISTER.md). Both licenses permit commercial reuse of covered material. CC BY requires attribution, a license link and identification of changes. Rights for named source frameworks have not been established; their protected expression and any source-derived protected expression are excluded from the grant. Combining researched sources does not establish those permissions.

This is educational material, not a hiring guarantee, accredited certification or production system. Functional exercise tests do not establish real customer productivity, adoption or operational readiness.
