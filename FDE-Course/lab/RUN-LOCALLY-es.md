# Ejecutar los ejercicios Python después de clonar

Utiliza solamente tickets sintéticos. La aplicación usa reglas, no un modelo de IA, y nunca envía mensajes a clientes. La versión probada es Python 3.14. Solo usa la biblioteca estándar: no necesitas instalar paquetes con pip ni una cuenta pagada de IA. Necesitas Git para clonar. Docker Desktop permite ejecutar el laboratorio sin instalar Python directamente.

## Windows PowerShell

```powershell
git clone https://github.com/albanc80/fde-delivery-framework.git
Set-Location fde-delivery-framework/FDE-Course/lab
py -3.14 --version
py -3.14 test_app.py
$env:TRAINING_TOKEN = 'course-local-example-token'
py -3.14 run_local.py
```

Primero las pruebas de referencia deben mostrar `Ran 7 tests` y `OK`. Inician su propio servidor temporal; no necesitas iniciar la aplicación por separado para probar. Si falta Python 3.14, instálalo antes de usar esos comandos.

Abre http://127.0.0.1:8088 e introduce `course-local-example-token`. Genera una sugerencia, revisa la razón, elige o modifica la cola y guarda la decisión humana. El nuevo iniciador `run_local.py` escucha solo en tu computadora y conserva eventos en `lab/.data/events.sqlite`. No cambia las reglas ni la API originales. Detén con Ctrl+C. Reinicia para conservar los eventos. Si el puerto está ocupado, utiliza `py -3.14 run_local.py --port 8090` y abre http://127.0.0.1:8090.

## macOS/Linux

```sh
git clone https://github.com/albanc80/fde-delivery-framework.git
cd fde-delivery-framework/FDE-Course/lab
python3.14 --version
python3.14 test_app.py
export TRAINING_TOKEN=course-local-example-token
python3.14 run_local.py
```

Abre http://127.0.0.1:8088 y usa el mismo token didáctico. Detén con Ctrl+C. Puedes usar `--port 8090`. Mantén local este servicio educativo.

## Resolver el ejercicio

1. Ejecuta las pruebas de referencia y observa una revisión completa en el navegador.
2. Implementa `route(text)` en `starter_route.py`. La excepción inicial es intencional. Devuelve `(cola, explicación)`.
3. Ignora diferencias entre mayúsculas y minúsculas. La referencia reconoce acceso (`password`, `login`, `access`, `contraseña`, `acceso`), facturación (`invoice`, `billing`, `refund`, `factura`, `reembolso`) e incidentes (`outage`, `offline`, `incident`, `caída`, `incidente`). Devuelve las colas técnicas `access`, `billing`, `incident` o `manual`. Cero o varias categorías deben permanecer manuales.
4. Conserva una copia de `app.py` como referencia. Sustituye únicamente su función `route` por tu implementación. Las pruebas importan `app`: editar solo el archivo inicial no modifica el servicio evaluado.
5. Repite `py -3.14 test_app.py` o `python3.14 test_app.py`. Mantén las siete pruebas y añade casos de ambigüedad y ausencia de autoridad para ejecutar un reembolso.
6. Reinicia la aplicación tras editar Python. No existe recarga automática. Conserva separadas sugerencias y decisiones revisadas.
7. Registra encuadre, predicción y criterios de detención antes de leer `case-results.json`. Recalcula medianas y errores en `northstar-review-sample.csv`. Las pruebas funcionales no demuestran productividad ni adopción.
8. Para el proyecto de mantenimiento, adapta reglas, colas permitidas, opciones de revisión y pruebas conjuntamente. Conserva autoridad del supervisor, revisión manual y escalamiento.

## Alternativa Docker

Desde `FDE-Course/lab`, con Docker Desktop funcionando:

```sh
docker compose up -d --build
```

Abre http://localhost:8088 e introduce el token didáctico. Docker proporciona Python 3.14. No ejecutes al mismo tiempo la versión nativa en ese puerto. Pruebas en PowerShell:

```powershell
docker run --rm -v "${PWD}:/lab:ro" -w /lab python:3.14-alpine python test_app.py
```

En macOS/Linux:

```sh
docker run --rm -v "$PWD:/lab:ro" -w /lab python:3.14-alpine python test_app.py
```

Después de editar, reconstruye con `docker compose up -d --build`. Detén con `docker compose stop`; reinicia con `docker compose start`. `docker compose down` conserva el volumen de eventos. No añadas `-v` si quieres conservarlos.

## Leer el curso localmente

Abre `FDE-Course/index.html` desde la carpeta raíz del repositorio y elige idioma. Conserva las carpetas para videos y subtítulos. Las notas pertenecen al navegador y al origen; no se transfieren automáticamente del archivo local al sitio web. GitHub Pages presenta el curso; Python se ejecuta en tu computadora.
