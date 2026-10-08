# Respuestas comentadas



Completa los ejercicios antes de consultar estas respuestas.



## M01-L01 La responsabilidad del FDE

Entrega: el revisor autorizado puede cargar un ticket y examinar una sugerencia de asignación. Resultado: los agentes usan la sugerencia en su cola real, reducen el tiempo de revisión y mantienen la calidad. El líder técnico verifica la entrega. Maya, responsable de soporte, verifica la adopción. Una captura respalda la primera afirmación; un período de observación definido y registros de revisión respaldan la segunda.

B. Uso observado y métricas definidas de antemano

La demostración y la revisión de código muestran avances de entrega. La adopción exige conducta observable y métricas operativas.



## M01-L02 Seis principios en una decisión

Entrega un ticket sintético que pase por una regla de asignación, una pantalla de revisión y una decisión observable. Registra una predicción sobre la utilidad. No envíes mensajes. Conserva la validación de datos y el registro de auditoría como componentes reutilizables. Así limitas el alcance y evitas comprometer a la organización con acciones sin revisión. También defines una pregunta medible para el siguiente experimento.

C. Probar una sugerencia revisable con datos permitidos

La rapidez no amplía la autoridad. El experimento permitido puede producir evidencia útil.



## M01-L03 Un portafolio de evidencia

Para la responsabilidad sobre la adopción, la conducta es programar y realizar una lectura del resultado con el responsable operativo. El artefacto es un registro fechado con uso real, excepciones y una decisión. Para amplitud técnica, demuestra el flujo completo y diagnostica una solicitud fallida. La ecuación de capacidades del documento es una herramienta conceptual, no una fórmula numérica de desempeño validada.

B. Una conducta que otra persona puede verificar

La observación independiente es más sólida que la confianza personal.



## M01-L04 El caso y los límites del curso

Una primera entrada útil dice: conocido dentro del caso, veinte agentes manejan tres categorías. Supuesto, las sugerencias reducirán la revisión. Desconocido, si los agentes las usarán consistentemente. Próxima acción, observar una revisión simulada y probar una sugerencia de extremo a extremo. Todavía no existe un resultado real de cliente. Conserva esta entrada cuando la evidencia cambie tu interpretación.

C. Datos ficticios para un ejercicio

El caso es una simulación educativa. Sus valores no constituyen evidencia comercial.



## M02-L01 La decisión detrás de la solicitud

Decisión: ¿debe Northstar probar ayuda para asignar tickets y reducir la revisión manteniendo aprobación humana? Pregunta dónde se acumula tiempo, cómo se eligen categorías, qué causó errores previos, quién autoriza datos y cómo se observará el éxito. La decisión puede cambiar durante la inmersión. Es más concreta y verificable que comprometerse con un asistente de IA.

A. Una decisión provisional y preguntas

El reconocimiento aporta una hipótesis inicial para investigar.



## M02-L02 Un ticket a través del proceso

El mapa incluye recepción, consulta de cuenta, selección de categoría, asignación y registro. La espera de permisos pertenece al gobierno del acceso. La consulta repetida de categorías pertenece a la ayuda de asignación. Conserva ambos problemas y prueba primero una incertidumbre. Una herramienta que reduce consultas no puede afirmar que eliminó la demora de permisos.

B. Para identificar trabajo desplazado y efectos posteriores

El pensamiento sistémico examina la consecuencia en el proceso completo.



## M02-L03 Conocido, supuesto y desconocido

Conocido en el turno observado: tres agentes usaron notas privadas. Reportado: Maya considera universal el uso de la tabla. Desconocido: conducta en otros turnos. Reportado por Luis: falta acceso productivo, pendiente de confirmar con Priya. Próxima prueba: observar otro turno y comparar fuentes de categorías. Evita concluir que nadie utiliza la tabla.

A. La conducta de ese turno

Ajusta el alcance de la afirmación a la evidencia.



## M02-L04 El mapa del entorno verificado

El mapa identifica a Maya como responsable del proceso, Priya como autorizadora y Luis como mantenedor de la API. Registra datos sintéticos como límite del curso, aprobación humana como condición, notas privadas como conducta observada y permisos productivos como asunto pendiente. La próxima acción es revisar el encuadre con operadores antes de integrar producción.

C. Desconocido, responsable y acción de verificación

La incertidumbre visible permite actuar sobre el mapa.



## M03-L01 La declaración de resultado

Para agentes de soporte, reducir la mediana de revisión de 20 a un máximo de 14 minutos en doce tareas simuladas comparables, manteniendo aprobación humana y hasta una cola incorrecta. El tiempo inicia al abrir el ticket y termina al guardar la decisión. Una cola incorrecta implica desacuerdo con la etiqueta de referencia del caso después de resolver ambigüedades.

B. Reducir el tiempo definido bajo restricciones de calidad

Un encuadre de resultado permite comparar intervenciones.



## M03-L02 La apuesta y la evidencia para reconsiderar

Si consultar categorías domina el esfuerzo, una sugerencia revisable debería reducir el tiempo definido. Prueba una categoría con doce tareas simuladas. Cambia el enfoque si aumenta la verificación o supera el límite de errores. Detén la prueba si envía un mensaje sin aprobación. Una hipótesis fallida puede producir aprendizaje útil.

A. Antes del experimento

El compromiso previo reduce el cambio oportunista de criterios.



## M03-L03 Métricas y límites de calidad

El cálculo es veinte menos doce, dividido entre veinte, igual a cuarenta por ciento. Respaldado: disminuyó la mediana en esta comparación sintética. No respaldado: la nómina bajó cuarenta por ciento. Agrega tamaño de muestra y tasa de error. Si mejora el tiempo y falla la calidad, itera antes de desplegar.

B. Capacidad de tiempo en el alcance medido

El beneficio financiero es otra afirmación y necesita evidencia.



## M03-L04 Acuerdo con operadores y alcance

Incluido: asignación de tickets sintéticos de acceso, aprobación del revisor y registro de eventos. Excluido: respuestas a clientes, credenciales productivas, promesas de personal y compra de modelos. Maya revisa utilidad, Priya conserva autoridad sobre acceso y Luis evalúa integración. La próxima revisión ocurre después de doce tareas, con los umbrales originales.

A. Resolverlas o hacerlas visibles antes de ejecutar

Las diferencias de alcance son una dependencia de entrega.



## M04-L01 Un flujo completo que aporta valor

El flujo usa POST /api/triage, devuelve una sugerencia con human_review_required en true y registra un evento. Guardar una decisión aceptada o modificada genera otro evento. Examina ambos. Generar una sugerencia no demuestra adopción. GET /health confirma disponibilidad, pero no demuestra asignación autorizada ni utilidad operativa.

B. Una entrada que llega a una salida revisada

La integridad se refiere al flujo útil; lo mínimo se refiere al alcance.



## M04-L02 Validación y límites de autoridad

La entrada válida recibe una sugerencia revisable. El estado cerrado o la fecha inválida producen error y ninguna sugerencia. Las instrucciones siguen siendo texto. Ningún endpoint envía mensajes ni reembolsos. Describe esto como control local limitado, no garantía para cualquier sistema de IA. Producción requiere su propio análisis de amenazas y autorización.

C. No, sigue siendo una entrada no confiable

El contenido y la autoridad son distintos.



## M04-L03 Sugerencias y decisiones observables

El registro debe contener una sugerencia y una decisión con el mismo identificador. La modificación conserva la cola elegida sin afirmar que la sugerencia inicial era correcta. El duplicado produce conflicto y no aumenta el conteo. Las fechas muestran ejecución, pero el resultado del encuadre aún necesita medición independiente.

B. Decisión guardada

Distingue generación, revisión y resultados operativos.



## M04-L04 Predicción antes de ejecutar

Las pruebas aprobadas verifican API local, validación, reglas, auditoría y aprobación según lo especificado. No demuestran confianza, adopción, latencia del cliente ni mejora causal de productividad. Conserva abierta la predicción hasta medirla. Una comparación opcional con un modelo debe reutilizar las etiquetas y considerar costo, errores, alternativas y esfuerzo de revisión.

C. No, la medición del resultado es independiente

Vincula cada afirmación con la prueba que puede respaldarla.



## M05-L01 La primera lectura

Predicción: mediana máxima de 14 y hasta un error. Observación: mediana 12 y un error en doce tareas elegibles, más dos entradas rechazadas. Actualización: la ayuda parece útil dentro de esas tareas. Decisión: preparar un despliegue controlado después de cerrar pendientes. Evita generalizar el resultado sintético a todo soporte.

C. Informar cantidad y motivo de exclusión

La cobertura y las exclusiones afectan la interpretación.



## M05-L02 Desplegar, iterar, cambiar o detener

Itera sobre errores si puedes probar una corrección específica con seguridad. Cambia hacia consulta de cuentas cuando la evidencia modifica el mecanismo. Detén respuestas sin autorización y restablece aprobación antes de probar. La detención puede ser temporal, pero seguir igual ignoraría la evidencia.

A. Detener la acción y recuperar el límite

Un promedio favorable no compensa una violación de autoridad.



## M05-L03 Factores externos e interpretación honesta

Complejidad, experiencia y definición de tiempo podrían explicar la diferencia. Compara categorías equivalentes, revisores semejantes e idénticos eventos de inicio y fin. Reporta incertidumbre. Un resultado limitado explícitamente sirve más que una cifra precisa basada en denominadores incompatibles.

B. Complejidad diferente entre muestras

La equivalencia de condiciones importa para interpretar.



## M05-L04 La segunda lectura después de adoptar

La adopción observada es cuarenta por ciento de tickets elegibles. Investiga fricción e incentivos antes de escalar. Itera sobre integración operativa y conserva calidad. No elimines el umbral del setenta por ciento ni reportes solo casos exitosos. La segunda lectura evita convertir éxito técnico en una afirmación de resultado sin respaldo.

C. Resultado y adopción después del despliegue

La segunda lectura revisa la consecuencia operativa en el tiempo.



## M06-L01 Las seis verificaciones de despliegue

La validación local respalda el curso. Seguridad productiva sigue sin aprobación, recuperación sin prueba y adopción como hipótesis. Maya atiende usabilidad y adopción, Luis integración y soporte, y Priya acceso productivo. La decisión se limita a la simulación hasta resolver condiciones.

A. No, su alcance es formación local

Los controles requieren evidencia adecuada al entorno.



## M06-L02 El responsable operativo identificado

La guía describe verificación de disponibilidad, solicitudes fallidas, versión de reglas, consulta manual, escalamiento a Luis y condiciones para desactivar asistencia. Maya decide desactivar dentro de su autoridad operativa. Priya controla cambios de acceso. Una rotación cubre ausencias y evita depender del ingeniero original.

B. Autoridad, capacidad, acceso y recuperación

La responsabilidad debe resistir ausencias y fallas normales.



## M06-L03 Adopción como cambio de trabajo

Prueba incluir sugerencias en la revisión existente en lugar de otra cola. Aclara que las modificaciones aportan aprendizaje durante el piloto y observa conducta. Mide tiempo total y adopción sobre tickets elegibles. No infieras confianza solo de encuestas positivas cuando el uso sigue bajo.

C. Uso sostenido en tareas elegibles

La asistencia es una entrada. El uso operativo es conducta.



## M06-L04 Recuperación y lanzamiento limitado

Disparador: solicitudes fallidas repetidas o una acción no autorizada. Acción: desactivar asistencia y revisar manualmente. Maya conserva continuidad y Luis recupera el servicio. Reanuda después de corregir la falla, aprobar pruebas pertinentes y confirmar preparación. Una prueba productiva requiere entorno real y procedimientos autorizados.

A. Condiciones de desactivación y alternativa manual

Diseñar recuperación forma parte de la preparación.



## M07-L01 El patrón detrás de la solución

Cuando clasificar repetidamente consume esfuerzo y el operador conserva autoridad, una sugerencia dentro de la revisión puede reducir consultas. Prueba estabilidad de categorías e incentivos en el nuevo lugar. La evidencia del curso respalda una hipótesis de transferencia, no una regla universal sobre IA.

B. El principio y sus condiciones

Transfiere el mecanismo y verifica nuevamente el contexto.



## M07-L02 Un componente técnico reutilizable

Componente: registro de decisiones. Entrada: identificador existente y cola permitida. Salida: identificador auditable. Fallas: sugerencia desconocida, decisión duplicada o cola inválida. Prueba cada condición. Los nombres de colas quedan como configuración. Identifica mantenedor y registra una nueva versión al cambiar comportamiento contractual.

C. Un contrato probado de registro de decisiones

Los contratos estables se transfieren mejor que supuestos locales.



## M07-L03 Una señal de producto con evidencia

Observado: cuarenta por ciento de tareas elegibles usan asistencia; agentes reportan captura repetida. Hipótesis: integrar revisión aumentará adopción. Validación: observar la tarea y probar la versión integrada en una muestra limitada. Desconocido: repetición en otros clientes. El caso no respalda cifras de mercado.

A. Evidencia del trabajo y sus consecuencias

Las observaciones trazables ayudan a decidir.



## M07-L04 Capacidad después de retirarte

Pide al operador responder a una indisponibilidad sin contactarte. Pide al mantenedor explicar una entrada rechazada. Registra capacidad, vacíos y responsable del método. Actualización: la exactitud necesita integración y modificaciones confiables para producir utilidad. El siguiente ciclo parte de ese encuadre revisado.

C. Los operadores recuperan de forma independiente

La capacidad demostrada importa más que el volumen documental.



## M08-L01 Una restricción cambia durante el proyecto

Usa datos y reglas locales. Prueba usabilidad, categorías, validación y registros. Marca integración productiva y beneficio del modelo como pendientes. Conserva una revisión futura con Luis y Priya. La alternativa permite avanzar sin afirmar uso de sistemas bloqueados.

A. Conducta seleccionada en la simulación

El alcance de la alternativa determina sus afirmaciones.



## M08-L02 Una decisión para tres audiencias

Operador: revisa, modifica y guarda; utiliza clasificación manual ante indisponibilidad. Ingeniero: la API local valida, separa revisión y registra eventos correlacionados; faltan controles productivos. Ejecutivo: la prueba sintética respalda una hipótesis limitada; autoriza revisión de acceso y evita afirmar ahorro de clientes.

B. Hechos, límites y decisión

Resumir cambia énfasis, no evidencia.



## M08-L03 Diagnóstico de modos de falla

Cambio de metas: restaura el umbral fechado y publica el resultado completo. Prototipo frágil: detén despliegue hasta tener responsable y soporte. Dependencia personal: capacita al mantenedor y prueba un cambio independiente. La corrección requiere conducta observable, además de documentos.

C. Cambiar éxito después de ver resultados

Cambiar umbrales después distorsiona el experimento.



## M08-L04 Práctica y progresión

Semana uno: observa un proceso permitido y su decisión. Semana dos: escribe un encuadre pequeño con el responsable. Semana tres: realiza experimento autorizado y predicción previa. Semana cuatro: compara y extrae aprendizaje reutilizable. Si no hay acceso laboral, utiliza otra simulación y descríbela como tal.

A. No, requiere evidencia de campo

Distingue aprendizaje de capacidad profesional verificada.



## M09-L01 Un nuevo encargo ambiguo

Un encuadre defendible reduce revisión del supervisor manteniendo sus decisiones de prioridad y cierre. Identificadores faltantes requieren aclaración. Detectar duplicados ayuda y no elimina solicitudes en silencio. Las urgencias pasan a revisión humana según procedimientos existentes. Documenta límites antes de implementar.

B. El supervisor autorizado

La herramienta apoya sin asumir autoridad operativa.



## M09-L02 Construir, predecir e incorporar una restricción

La alternativa usa datos sintéticos, valida activos, marca urgencias para supervisor y guarda decisiones revisadas. Predicción y evidencia quedan separadas. El registro marca integración real sin probar y conserva seguridad. Una buena entrega explica cómo los controles responden al caso, además de enumerarlos.

C. La diferencia entre probado y pendiente

Las alternativas cambian el alcance de evidencia.



## M09-L03 El portafolio y la rúbrica

Usa cero para ausencia, uno para descripción, dos para demostración parcial, tres para resultado coherente y respaldado, y cuatro para demostración sólida con límites y transferencia. La aprobación propuesta es setenta por ciento más todas las condiciones obligatorias. Es evaluación educativa, no estándar acreditado.

A. No, la integridad es obligatoria

Las condiciones obligatorias son independientes del total.



## M09-L04 Aplicación de campo y siguiente ciclo

Propón observar una revisión autorizada y probar un resumen revisable con datos sintéticos o permitidos. Conserva criterio humano y procedimientos. Identifica responsable y define éxito antes de actuar. La evidencia real es el próximo objetivo de aprendizaje, no algo demostrado por el portafolio simulado.

B. Vocabulario y contexto; los permisos requieren verificación

Un método transferible no implica autoridad transferible.

