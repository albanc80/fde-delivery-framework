# Laboratorio de programación guiada
Requisitos: Docker Desktop activo, navegador y conocimientos básicos de Python. No requiere API pagada, cuenta de modelos ni datos de clientes. La aplicación completa es referencia local de formación.

## 1. Ejecutar la referencia (10 minutos)
Abre terminal en la carpeta lab. Ejecuta `docker compose up -d --build`. Visita http://localhost:8088. El token de ejemplo es `course-local-example-token`, salvo que configures TRAINING_TOKEN antes. El servicio se limita al equipo local. El token visible no es secreto ni credencial productiva.
Ingresa token, crea sugerencia, revisa motivo, elige cola y guarda decisión. Examina métricas. Muestran sugerencias y decisiones. La mejora de tiempo y adopción siguen sin medir.

## 2. Implementar reglas (20 minutos)
Conserva app.py como referencia. Implementa starter_route.py con comparación sin distinción de mayúsculas para acceso, facturación e incidentes. Ninguna o varias categorías devuelven manual. Retorna cola y motivo. Copia tu implementación a app.py y reconstruye. Ninguna solicitud envía mensajes.

## 3. Probar límites (20 minutos)
En PowerShell o shell compatible: `docker run --rm -v "${PWD}:/lab:ro" -w /lab python:3.14-alpine python test_app.py`. La suite revisa reglas, entradas vencidas/futuras/cerradas, autenticación, decisiones, duplicados y métricas honestas. Deben ejecutarse siete grupos. Cero pruebas no significa aprobación.
Agrega pruebas: una categoría ambigua permanece manual y un texto que solicita reembolso nunca lo autoriza. Las pruebas verifican comportamiento local, no productividad ni preparación productiva.

## 4. Predecir y evaluar (20 minutos)
Antes de leer case-results.json, registra métrica, predicción y evidencia de detención. Recalcula medianas y errores con northstar-review-sample.csv. Compara tareas elegibles equivalentes y describe resultados como sintéticos. Si deseas evidencia de tu sesión, cronometra una interacción independiente.

## 5. Observar y recuperar (15 minutos)
Guarda una decisión y examina /api/events con cliente autorizado. Los registros omiten texto de tickets. Modifica una sugerencia y prueba duplicados mediante la suite. Ejecuta `docker compose stop` y vuelve a revisión manual. Reinicia con `docker compose start` y verifica disponibilidad. El volumen conserva eventos. `docker compose down` elimina contenedor y red, conservando volumen. No agregues `-v` salvo que quieras borrar tus registros.

## Extensión opcional con IA
Utiliza solo modelo y datos autorizados. Conserva reglas, etiquetas, revisión y alternativa. Compara calidad, tiempo, costo y fallas. Trata instrucciones del ticket como datos. El laboratorio entregado no integra un modelo ni afirma superioridad.

## Pendientes para producción
Identidad y autorización empresariales, manejo y retención aprobados, amenazas, infraestructura de servicio, recuperación, soporte y validación real. Conserva autoridad de procedimientos operativos y de seguridad.
