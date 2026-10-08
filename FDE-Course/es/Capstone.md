# Proyecto integrador: Harbor Maintenance
Toda la evidencia es ficticia. Abre archivos por etapas. Escribe encuadre y predicción antes de leer resultados. Práctica prevista: 125 minutos.

## Etapa 1: descubrimiento (25 minutos)
El patrocinador pide automatizar asignación y cierre. Elena, supervisora, conserva decisiones de prioridad y cierre. Doce técnicos envían solicitudes. A veces falta identificador de activo. Dos solicitudes pueden describir la misma falla. Las urgencias pueden implicar seguridad. Ninguna herramienta puede modificar equipos, cerrar solicitudes ni sustituir procedimientos autorizados.
Lee capstone-evidence/stage-1.json. Produce mapa v0/v1, una diferencia entre relato y conducta, y tarjeta de encuadre mediante simulación de roles. Distingue expectativas del patrocinador de autoridad de Elena. Clasifica conocido, supuesto y desconocido.

## Etapa 2: construcción y predicción (45 minutos)
Adapta el laboratorio a categorías electrical, mechanical, inspection y manual. Exige identificador de activo y muestra una alerta para urgencias. Los activos faltantes requieren aclaración. Las solicitudes ambiguas permanecen manuales. Marcar duplicados apoya revisión y nunca elimina datos.
Usa función inicial, referencia completa y pruebas de soporte. Agrega pruebas de mantenimiento. Separa sugerencia de decisión revisada. Escribe predicción antes de evaluar. Encuadre sugerido: mediana máxima de 12 minutos, hasta una asignación final incorrecta en doce tareas elegibles y aprobación humana. Son umbrales didácticos.

## Etapa 3: restricción nueva (15 minutos)
Abre stage-2-constraint.json después de implementar. La integración no funciona y se prohíben modelos externos. Revisa la decisión y demuestra alternativa local permitida. Indica qué prueba y qué sigue pendiente.

## Etapa 4: dos lecturas (20 minutos)
Abre stage-3-results.json. Primera lectura: mediana ficticia de 11 minutos y dos asignaciones incorrectas en doce tareas. Pasa rapidez y falla calidad. Decide sin modificar el umbral.
Segunda lectura después de un lanzamiento revisado: seis de veinte solicitudes elegibles usan asistencia. La meta previa era 60 por ciento. Investiga adopción del 30 por ciento. Evita reportar solo usuarios que terminaron.

## Etapa 5: aprendizaje y defensa (20 minutos)
Entrega mapa, encuadre, predicción, flujo funcional, pruebas, decisión ante restricciones, ambas lecturas, lista de despliegue, responsabilidad y recuperación, paquete de aprendizaje y memo ejecutivo. Demuestra una acción independiente del mantenedor. Conserva versiones y fuentes.

## Rúbrica: siete dimensiones de 0 a 4
Descubrimiento: diferencia solicitud de decisión mediante evidencia.
Entrega: flujo completo prueba incertidumbre dentro de restricciones.
Ingeniería: funcionan validación, revisión, fallas y observabilidad.
Adopción: denominador elegible, integración operativa y segunda lectura.
Criterio: decisiones consideran evidencia, valor, riesgo y reversibilidad.
Aprendizaje: predicción fechada, diferencias honestas e interpretación revisada.
Reutilización: patrón condicionado, componente mantenible y capacidad transferida.
Escala: 0 ausente; 1 descrito; 2 parcial; 3 demostrado con evidencia conectada; 4 demostrado con límites, condiciones de transferencia y verificación independiente.
Aprobación propuesta: al menos 20/28 y todas las condiciones obligatorias. Es rúbrica educativa, no estándar acreditado.

## Condiciones obligatorias
Sin mensajes, acciones sobre equipos, cambios de prioridad ni cierres no autorizados. Sin evidencia inventada ni reclasificada. Predicción anterior a resultados. Dos lecturas presentes. Calidad o adopción incumplidas reconocidas. Evidencia real y simulada separadas. Si falla una condición, revisa independientemente de la puntuación.

## Decisión de referencia
Itera tras la primera lectura: dos errores superan el límite. Diagnostica etiquetas ambiguas y activos faltantes. Mantén autoridad humana. La integración productiva queda sin probar. Tras la segunda lectura, investiga captura repetida y confianza antes de escalar. Extrae el contrato de revisión y escalamiento, no las categorías del caso anterior.
