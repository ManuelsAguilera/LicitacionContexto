---
id: SD09-TRANSVERSALES
tipo: contexto
parte: SD-09
titulo: Obligaciones transversales de QA, seguridad, continuidad, accesibilidad y migración
estado: borrador
bases:
  - 00_Bases/Bases_Transversales.md
  - 00_Bases/Bases_Administrativas.md
  - 00_Bases/Caso_09_Cadena_Multitienda.md
requisitos: []
depende_de:
  - 02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex
  - 02_Propuesta/latex_final/sd-04/OSS-Subdocumento4.tex
adjuntos: []
jira: []
cifras:
  - "70 % cobertura bloqueante en lógica de negocio"
  - "80 % objetivo para código nuevo de lógica de negocio"
  - "deuda técnica ≤ 5 %"
  - "trazabilidad al 100 % al cierre"
origen: "Bases Transversales vigentes, Bases Administrativas y Caso 09; contraste con SD-06 T-10 y SD-04"
actualizado: 2026-10-11
---

# Obligaciones transversales para SD-09

Inventario de obligaciones verificables que condicionan la solución y su aceptación. Los criterios de abajo son internos de este artefacto (`C-Tnn-01`); no crean ni reemplazan códigos oficiales RT. La evidencia se planifica para la ejecución futura: no se declara ninguna prueba ejecutada ni cumplimiento ya demostrado.

## Base de lectura y límites

La fuente rectora para los requisitos comunes es [Bases Técnicas Transversales, capítulos y RT citados por ficha](../../00_Bases/Bases_Transversales.md). Para el alcance y los volúmenes rige [Caso 09](../../00_Bases/Caso_09_Cadena_Multitienda.md); SD-04 y SD-06 son compromisos de la oferta que deben conservarse coherentes con esas Bases. El Formulario T-12 exige contestar requisito por requisito con componente, ubicación en la oferta y evidencia prevista (Bases Transversales, líneas 89–96). Las citas enlazan al archivo y línea de la fuente.

La volumetría de 104.000 pedidos en tres días (Caso 09, línea 743) es volumen de evento; no equivale a TPS ni define una tasa uniforme. El cálculo de capacidad y los picos deben derivarse de perfiles temporales, concurrencia y mezcla de operaciones levantados con Ancoa. Las Bases Transversales disponen medición P95 bajo carga peak declarada; no se reinterpretan percentiles ni máximos como promedios (líneas 100–103, 483–510, [RT-09.01 a RT-09.10](../../00_Bases/Bases_Transversales.md#L502)).

El modelo híbrido del Artículo 16, los controles de seguridad del Artículo 21 y los criterios de evaluación del Artículo 56 de Bases Administrativas mantienen su fuerza; ninguna ficha los sustituye ([Art. 16](../../00_Bases/Bases_Administrativas.md#L407), [Art. 21](../../00_Bases/Bases_Administrativas.md#L549), [Art. 56](../../00_Bases/Bases_Administrativas.md#L1226)). El cronograma contractual es de 56 meses: Etapa 1, meses 1–15 con producción en mes 16; Etapa 2, meses 13–20 con producción en mes 21; operación, meses 21–56 (Bases Administrativas, Art. 17 y Bases Transversales, línea 75). Los ensayos y puertas propuestos se ubican en ese marco y respetan las ventanas protegidas del caso.

La referencia de catálogo funcional vigente es v3.0. El Anexo B v3.1 es borrador de trabajo y no se usa para declarar requisitos oficiales ni equivalencias. Se preservan los IDs oficiales RT tal como aparecen en las Bases. Los cuatro umbrales de SD-06 se registran con su condición exacta: 70 % bloqueante para lógica de negocio total; 80 % objetivo separado para código nuevo; razón de deuda técnica no superior a 5 %; y trazabilidad completa, con meta de cierre de 100 %. No se permutan, combinan ni convierten en un percentil.

## Fichas de obligación y aceptación

<a id="t01"></a>

### T01 — Calidad del software y cobertura

- **Obligación y fuente:** cobertura automatizada de al menos 70 % en el código de lógica de negocio, con bloqueo en CI, RT-04.11 ([Bases Transversales, línea 232](../../00_Bases/Bases_Transversales.md#L232)). SD-06 añade como objetivo de calidad al menos 80 % para código nuevo, medido aparte; el objetivo no sustituye ni oculta el mínimo contractual ([SD-06, líneas 3135–3143](../../02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex#L3135)).
- **Ámbito/servicio:** común a Retail y Emisor; aplicar a cada repositorio/servicio nuevo de lógica de negocio y reportar la población evaluada. Mantener segregación de dominios en informes.
- **Criterio:** **C-T01-01.** En cada puerta CI, el total medido de lógica de negocio alcanza ≥70 %. La unidad (líneas o ramas), exclusiones y reglas permanecen documentadas; el 80 % no compensa un total menor al 70 %.
- **Escenario, método y umbral:** cálculo automatizado versionado sobre revisión candidata y reporte desglosado por dominio; umbral contractual 70 % bloqueante, objetivo interno 80 % de código nuevo. No se fija herramienta como requisito de las Bases.
- **Criterio:** **C-T01-02.** Para el código nuevo de lógica de negocio, el reporte identifica el subconjunto y su cobertura, con meta ≥80 % separada del total. Si el objetivo interno no se alcanza, se documenta como brecha; nunca habilita un build que incumple el 70 % bloqueante.
- **Escenario, método y umbral:** evaluar diferencial de código nuevo por versión con la misma definición de cobertura; ≥80 % es objetivo de SD-06, no obligación transversal.
- **Evidencia prevista, no ejecutada:** reporte incremental comparado con base anterior y decisión registrada sobre brechas al cierre del sprint.
- **Estado/fuente del umbral:** 70 % exigido por RT-04.11; 80 % objetivo de SD-06, no umbral transversal adicional.
- **Evidencia prevista, no ejecutada:** configuración CI; reporte de cobertura por commit/versión; configuración de exclusiones aprobada; registro de bloqueo cuando no alcance el 70 %.
- **Responsable/calendario/dependencias/brechas:** líder de Calidad y Pruebas, con líderes de desarrollo; definir métrica y exclusiones antes del primer pipeline de producto y sostener en meses 1–56. Depende de repositorios, estrategia de pruebas y ambientes. Pendiente identificar herramienta y línea base inicial.

<a id="t02"></a>

### T02 — Deuda técnica y hallazgos de liberación

- **Obligación y fuente:** SD-06 establece registro de deuda con origen, impacto y fecha de pago; razón de deuda técnica no superior a 5 %, y ausencia de hallazgos críticos y altos abiertos como condición de aceptación ([SD-06, líneas 3145–3189](../../02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex#L3145)). Las Bases exigen escaneo y remediación de vulnerabilidades conforme a RT-11.04 ([línea 536](../../00_Bases/Bases_Transversales.md#L536)).
- **Ámbito/servicio:** común a servicios nuevos Retail, Emisor y componentes compartidos; deuda y hallazgos se registran por producto y dominio, sin mezclar métricas entre ámbitos.
- **Criterio:** **C-T02-01.** Antes de liberar, la razón de deuda técnica calculada con método documentado es ≤5 %. La convivencia planificada con plataformas conservadas se registra como transición y no se contabiliza automáticamente como deuda.
- **Escenario, método y umbral:** inspección estática y registro de remediación por versión; deuda = esfuerzo estimado de remediación / esfuerzo de desarrollo del código evaluado, según SD-06. Umbral ≤5 % es política de SD-06.
- **Evidencia prevista, no ejecutada:** inventario priorizado de deuda; método y población de cálculo; reporte por versión con deuda, duplicación y excepciones justificadas.
- **Criterio:** **C-T02-02.** No se autoriza liberación con hallazgos críticos o altos abiertos. Se ejecuta escaneo continuo y se mide remediación desde publicación o detección: crítico ≤7 días corridos, alto ≤15 días, medio ≤30 días.
- **Escenario, método y umbral:** análisis de seguridad previo al despliegue, control de severidad y antigüedad de cada hallazgo, y comprobación del cierre. Umbrales RT-11.04 y puerta de salida de SD-06.
- **Evidencia prevista, no ejecutada:** reporte continuo de análisis con hallazgo, severidad, fecha de detección/publicación, fecha de corrección y comprobación posterior.
- **Estado/fuente del umbral:** el 5 % es política propuesta en SD-06; los plazos de severidad son obligatorios en Bases.
- **Responsable/calendario/dependencias/brechas:** líder de Calidad y Seguridad con responsables de servicio; en cada candidato a producción y durante Operación meses 21–56. Depende de herramienta/método acordado y backlog. Pendiente fijar herramienta y tratamiento de falsos positivos.

<a id="t03"></a>

### T03 — Trazabilidad integral de requisito a despliegue

- **Obligación y fuente:** RT-04.04 requiere vínculo completo entre requerimiento, incidencia, cambio de código, prueba y despliegue ([Bases Transversales, línea 225](../../00_Bases/Bases_Transversales.md#L225)). SD-06 fija una cadena bidireccional requisito-trabajo-evidencia (sección 6.2.2; [líneas 2957–2995](../../02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex#L2957)). La meta de cierre de 100 % se aplica aquí a la línea base de requisitos, no al indicador separado de trazabilidad de acuerdos.
- **Ámbito/servicio:** toda obligación y cambio que afecte Retail, Emisor o Frontera X-01; los registros permiten filtrar por entidad y finalidad.
- **Criterio:** **C-T03-01.** Al cierre de cada etapa, el 100 % de los requisitos de su línea base tiene vínculo navegable a historia/incidencia, prueba y evidencia de aceptación/despliegue; un elemento no implementado solo queda trazado con decisión formal de cambio aprobada y actualización de la línea base. No se interpreta 100 % como cobertura de código ni como percentil.
- **Escenario, método y umbral:** consulta de trazabilidad hacia adelante y hacia atrás en la herramienta de gestión; muestreo por Calidad en cada hito y conciliación total de la línea base al cierre. Umbral de cierre 100 % (meta SD-06); RT-04.04 exige trazabilidad completa durante el flujo.
- **Estado/fuente del umbral:** obligación de trazabilidad en Bases; 100 % como meta explícita de SD-06.
- **Evidencia prevista, no ejecutada:** matriz exportable de relaciones; historial de cambios; resultados de pruebas identificados por versión; registros de despliegue y acta de cierre.
- **Responsable/calendario/dependencias/brechas:** jefe de proyecto y líder de Calidad, con responsables funcionales y técnicos; registrar desde levantamiento (meses 1–4), verificar por hito y cerrar al 100 % al cierre de cada etapa, antes de producción meses 16 y 21; mantener hasta mes 56. Depende de IDs estables y herramienta integrada. Pendiente formalizar el vínculo requisito RT ↔ elemento SD-03/catálogo v3.0 ↔ historia/incidencia ↔ prueba.

<a id="t04"></a>

### T04 — Seguridad, segregación y vulnerabilidades

- **Obligación y fuente:** Zero Trust y modelado de amenazas por componente/integración, RT-11.01–11.02 ([líneas 533–535](../../00_Bases/Bases_Transversales.md#L533)); clasificación y matriz de controles RT-11.03–11.06; plazos de remediación de vulnerabilidades RT-11.04 ([línea 536](../../00_Bases/Bases_Transversales.md#L536)); controles de borde, cifrado y gateway RT-11.07–11.12 ([líneas 544–550](../../00_Bases/Bases_Transversales.md#L544)); RT-11.20 exige intrusión por tercero independiente, anual y antes de cada producción ([línea 562](../../00_Bases/Bases_Transversales.md#L562)); la estrategia de pruebas exige cero hallazgos críticos y altos abiertos y aplica antes de cada paso a producción y anualmente ([líneas 836–849](../../00_Bases/Bases_Transversales.md#L847)). SD-04 separa identidades, permisos, claves, canales de eventos y espacios analíticos de Retail y Emisor y define pruebas negativas para X-01 ([SD-04, líneas 346–350](../../02_Propuesta/latex_final/sd-04/OSS-Subdocumento4.tex#L346)).
- **Ámbito/servicio:** ambas entidades y servicios compartidos; cualquier cruce de datos pasa por X-01 con finalidad, campos mínimos y controles en ambos extremos. No habilitar repositorio común ni acceso lateral de Retail a datos del Emisor.
- **Criterio:** **C-T04-01.** Cada servicio e integración tiene amenaza, controles, responsable y evidencia; las pruebas cubren solicitud autorizada mínima, ruta no inventariada y uso secundario denegado. Los plazos de vulnerabilidades se verifican mediante C-T02-02.
- **Escenario, método y umbral:** revisión de amenazas y matriz; pruebas de autorización y segregación; escaneo continuo y verificación de remediación. No se inventa un porcentaje de cobertura de seguridad.
- **Estado/fuente del umbral:** obligaciones y plazos de Bases; pruebas específicas de separación y condición de hallazgos en SD-04/SD-06.
- **Evidencia prevista, no ejecutada:** modelos STRIDE u otra metodología declarada; matriz ISO/IEC 27001/27002; resultados de pruebas de permisos y X-01; reportes de escaneo y tickets con fechas de detección/cierre; registros de auditoría sin exposición de datos sensibles.
- **Criterio:** **C-T04-02.** Un tercero independiente del adjudicatario ejecuta prueba de intrusión antes de cada paso a producción y anualmente; se entrega el informe íntegro al Cliente y un plan de remediación con plazos. No quedan hallazgos críticos ni altos abiertos como criterio de paso a producción.
- **Escenario, método y umbral:** prueba ofensiva independiente, revisión del informe y verificación de correcciones; anual y previa a cada producción según RT-11.20 y capítulo 20.1. Umbral de salida: cero críticos y altos abiertos.
- **Evidencia prevista, no ejecutada:** contrato/independencia del tercero, informe íntegro, plan de remediación y revalidación de hallazgos.
- **Responsable/calendario/dependencias/brechas:** líder de Seguridad contrata y coordina al tercero; previo a producción de meses 16 y 21 y anualmente durante operación meses 21–56. Depende de ambientes representativos y alcance autorizado. Pendiente calendario anual, independencia verificable y circuito de entrega íntegra al Cliente.
- **Responsable/calendario/dependencias/brechas:** líder de Seguridad y dueños de Retail/Emisor; modelo base para H2, mes 4 (programación a confirmar, no compuerta contractual nueva); actualizar ante cambios y revisar antes de cada liberación y durante operación. Depende del catálogo X-01 y clasificación de datos. Pendiente aprobación jurídica de finalidades/retención y de cada cruce.

<a id="t05"></a>

### T05 — Continuidad local de tienda y recuperación

- **Obligación y fuente:** RT-03.10 fija mínimo de 24 horas de autonomía degradada on-premise ([Bases Transversales, línea 185](../../00_Bases/Bases_Transversales.md#L185)); RT-10.01 fija disponibilidad mensual ≥99,9 % extremo a extremo para servicios críticos y RT-10.03/04 planes de continuidad y continuidad TIC ([líneas 517–524](../../00_Bases/Bases_Transversales.md#L517)). RT-07.02 exige distancia suficiente entre sitios para no compartir amenaza de fuerza mayor y declarar distancia y amenazas comunes; RT-07.04 fija RTO ≤4 h y RPO ≤15 min, y RT-07.07 exige dos conmutaciones reales anuales ([líneas 390–395](../../00_Bases/Bases_Transversales.md#L390)). SD-04 define operación local, diario durable, deduplicación, retorno y piloto ([líneas 352 y 369](../../02_Propuesta/latex_final/sd-04/OSS-Subdocumento4.tex#L352)); SD-06 incluye autonomía de 24 h y retorno tras 8 h sin pérdida como escenarios de aceptación ([líneas 3061–3071](../../02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex#L3061)).
- **Ámbito/servicio:** continuidad de venta Retail en tienda; Emisor mantiene identidad, datos y decisión propios. La caída de enlace no habilita originar tarjetas ni ampliar cupos; compras con crédito previamente autorizado quedan sujetas a controles y decisión aún pendiente.
- **Criterio:** **C-T05-01.** Ante pérdida total del enlace, el piloto sostiene al menos 24 horas de operación degradada de tienda; el mínimo de 8 horas del Caso 09 no rebaja este piso.
- **Escenario, método y umbral:** corte controlado con operación de ventas y consulta local; cronometraje continuo de autonomía. Umbral ≥24 h conforme a RT-03.10. Al volver el enlace tras este ensayo de 24 h, SD04 exige cero operaciones perdidas o duplicadas; comparar diario durable y registros centrales. El máximo de 30 minutos del Caso se ensaya por separado tras 8 h, sin extrapolarlo automáticamente a 24 h.
- **Evidencia prevista, no ejecutada:** bitácora del corte, operaciones aceptadas durante la ventana y comprobación de autonomía al completar 24 h.
- **Criterio:** **C-T05-02.** Tras ocho horas desconectada, la tienda sincroniza en ≤30 minutos, sin perder ninguna venta ni documento y resolviendo determinísticamente existencias comprometidas por otros canales.
- **Escenario, método y umbral:** generar ventas/documentos y conflictos de inventario durante 8 h sin enlace, reconectar y medir sincronización completa. Umbral ≤30 min y cero ventas/documentos perdidos, según RT-03.13 del Caso 09.
- **Evidencia prevista, no ejecutada:** conteo de operaciones antes/después, reporte de diferencias y conflictos, marcas de tiempo de reconexión y conciliación final.
- **Criterio:** **C-T05-03.** En conmutación real de recuperación ante desastre, cada servicio crítico cumple RTO ≤4 h y RPO ≤15 min; ambos se miden y se registran por servicio. Esto es una prueba distinta del ensayo de tienda desconectada de 24 h.
- **Escenario, método y umbral:** conmutación de sitio/región primario a recuperación; medir tiempo hasta restituir servicio y antigüedad del último dato recuperado. Umbral máximo RTO 4 h / RPO 15 min (RT-07.04); dos pruebas anuales como mínimo (RT-07.07).
- **Evidencia prevista, no ejecutada:** bitácora de conmutación real, marcas de tiempo, validación de datos, resultados de RTO/RPO y plan de corrección.
- **Criterio:** **C-T05-04.** El sitio secundario declara distancia y analiza amenazas comunes para demostrar que no queda afectado por el mismo evento de fuerza mayor que el sitio principal (RT-07.02).
- **Escenario, método y umbral:** comparar emplazamientos frente a amenazas naturales, infraestructura y dependencias compartidas; la distancia suficiente se justifica por análisis, sin inventar una equivalencia por kilómetros.
- **Evidencia prevista, no ejecutada:** memoria de emplazamiento, distancia y análisis de amenazas comunes con mitigaciones.
- **Criterio:** **C-T05-05.** Cada servicio crítico alcanza disponibilidad mensual ≥99,9 % extremo a extremo (RT-10.01).
- **Escenario, método y umbral:** monitorear transacciones sintéticas y fallas reales por servicio durante el mes; documentar tiempo medido, indisponibilidad y exclusiones contractuales aplicables.
- **Evidencia prevista, no ejecutada:** serie de disponibilidad, incidentes y cálculo mensual por servicio con denominador y exclusiones. Responsable Operaciones/SRE, desde puesta en producción y durante meses 21–56; pendiente acordar sondas y reglas de medición.
- **Estado/fuente del umbral:** 24 h de autonomía, ≤30 min/cero pérdidas al sincronizar, RTO/RPO y pruebas semestrales/anuales son umbrales de las Bases; distancia y amenazas se documentan para acreditar RT-07.02.
- **Responsable/calendario/dependencias/brechas:** líderes de Operación/SRE, Retail y Datos; autonomía y retorno antes de producción de Etapa 1 (mes 16); DR antes de producción y semestral durante operación meses 21–56. Depende de inventario de tiendas, infraestructura de recuperación y conectividad. Pendientes: modo tributario aprobado para contingencia, topes de crédito offline y ubicación/distancia del sitio secundario.

<a id="t06"></a>

### T06 — Accesibilidad y usabilidad

- **Obligación y fuente:** RT-13.01 obliga WCAG 2.2 AA en todas las interfaces con verificación automática y manual e informe; RT-13.02–13.07 establecen diseño responsivo, pruebas con usuarios, indicadores medibles, máximo de tres interacciones para funcionalidad principal, errores comprensibles y objetivos táctiles ≥44×44 px ([líneas 614–620](../../00_Bases/Bases_Transversales.md#L614)). La tabla de pruebas prescribe accesibilidad antes de cada producción ([línea 848](../../00_Bases/Bases_Transversales.md#L848)).
- **Ámbito/servicio:** cliente, vendedor, caja/POS, mesón financiero, bodega y centro de distribución; interfaces de Retail y Emisor, incluidas terminales compartidas.
- **Criterio:** **C-T06-01.** Cada interfaz destinada a personas usuarias cumple WCAG 2.2 AA en comprobaciones automatizadas y manuales y entrega informe de conformidad antes de cada paso a producción.
- **Escenario, método y umbral:** evaluar criterios WCAG por interfaz, teclado y tecnología asistiva; umbral WCAG 2.2 AA y evidencia preproducción.
- **Evidencia prevista, no ejecutada:** matriz de criterios, informes de revisión automática/manual y defectos corregidos con revalidación.
- **Criterio:** **C-T06-02.** Se investigan perfiles reales y se realizan prototipos y pruebas de usabilidad antes de construir definitivamente; se registran hallazgos y cambios. Cada funcionalidad principal queda a ≤3 interacciones desde el inicio del perfil y satisface los indicadores comprometidos para la operación.
- **Escenario, método y umbral:** pruebas de tarea por perfil de cliente, vendedor, caja, mesón y operación; contar interacciones desde pantalla inicial y medir tiempo, pasos, errores y aprendizaje con metas aprobadas. El máximo de tres interacciones es RT-13.05; los otros indicadores deben declararse en la oferta.
- **Evidencia prevista, no ejecutada:** protocolo, perfiles y resultados de pruebas, métricas por tarea, decisiones de diseño y re-prueba.
- **Estado/fuente del umbral:** WCAG 2.2 AA, pruebas automatizadas/manuales, investigación con usuarios, máximo de tres interacciones y entrega de informe son exigencias de Bases; herramientas y muestra se definen en el plan.
- **Responsable/calendario/dependencias/brechas:** líder UX/Accesibilidad y Calidad con dueños de canal; investigación y prototipo antes de construcción definitiva, control en cada incremento y cierre preproducción meses 1–21; repetir antes de toda liberación posterior. Depende de inventario de interfaces y perfiles. Pendiente calendarizar participantes reales y declarar indicadores por operación.

<a id="t07"></a>

### T07 — Perfil de carga, capacidad y desempeño

- **Obligación y fuente:** RT-09.01 requiere cálculo con concurrencia, TPS, volumen y crecimiento desde la volumetría del caso; RT-09.02 aplica carga del caso; RT-09.03 exige crecimiento 3× a tres años; RT-09.06 exige carga a 1,5× peak y estrés hasta quiebre, con informe de curva, saturación y recuperación ([líneas 502–510](../../00_Bases/Bases_Transversales.md#L502)). Caso 09 registra 104.000 pedidos en los tres días del evento (línea 743), no TPS. La tabla consigna además una cifra de proyección ≈150.000, pero ninguna de ellas determina una tasa uniforme por segundo. SD-04 condiciona memoria de capacidad a tasas normales y de evento levantadas antes de fijar cuotas ([línea 354](../../02_Propuesta/latex_final/sd-04/OSS-Subdocumento4.tex#L354)); SD-06 define P95 bajo peak para criterios concretos ([líneas 3037–3059](../../02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex#L3037)).
- **Ámbito/servicio:** Retail digital y presencial; Emisor para evaluación crediticia y evidencia financiera; APIs/eventos compartidos con límites de dominio.
- **Criterio:** **C-T07-01.** La campaña de carga de Preproducción alcanza al menos 1,5× el peak declarado por escenario, y el estrés continúa hasta identificar el punto de quiebre.
- **Escenario, método y umbral:** campañas separadas para evento digital y peak presencial navideño; usar perfil temporal, concurrencia y mezcla de operaciones. Umbral RT-09.06: ≥1,5× peak declarado; documentar curva y punto de saturación según RT-09.07.
- **Criterio:** **C-T07-02.** Cada transacción crítica cumple su máximo del RT-09.01 del Caso 09: disponibilidad digital ≤400 ms; confirmación de pedido durante evento ≤3 s; venta completa en caja con medio externo ≤25 s; evaluación crediticia ≤8 s; propagación de precio a 380 cajas y canal digital ≤5 min; consulta de existencia en terminal de sala ≤2 s e indica confianza; devolución en mesón ≤60 s. Estos máximos se verifican por operación y no se sustituyen por una meta agregada P95.
- **Escenario, método y umbral:** medir el tiempo extremo a extremo bajo peak declarado, con límites de inicio/fin definidos por operación; reportar P95 de Bases y máximo observado por separado, y contrastar el máximo del Caso con su umbral. Ambos aplican; el máximo del Caso no se convierte en promedio ni se reemplaza por el P95.
- **Evidencia prevista, no ejecutada:** informe por operación con distribución de tiempos, máximos observados, carga, ambiente y versión; incluir resultados P95 por separado cuando corresponda.
- **Criterio:** **C-T07-03.** El diseño soporta crecimiento de al menos 3× la volumetría inicial en tres años sin rediseño, conforme a RT-09.03.
- **Escenario, método y umbral:** proyectar componentes y dependencias con carga equivalente a 3×; revisar escalamiento y cuellos de botella por los dos peaks.
- **Evidencia prevista, no ejecutada:** modelo de escalamiento, informe de capacidad al multiplicador 3× y registro de saturación/mitigación.
- **Estado/fuente del umbral:** exigencias RT-09.01–09.07; tasa TPS real y distribución intraevento pendientes de medición/estimación documentada.
- **Evidencia prevista, no ejecutada:** memoria de capacidad con supuestos y fuente; scripts/datos sintéticos; resultados versionados; curvas P95 vs carga, saturación, consumo y recuperación; plan de escalamiento y degradación controlada.
- **Responsable/calendario/dependencias/brechas:** arquitecto de rendimiento y líderes de canales/datos; perfil inicial antes de cerrar arquitectura (propuesta de preparación mes 4, sujeta a validación), ensayo antes de producción mes 16 y ajuste antes de producción mes 21; proyección trimestral en operación (frecuencia propuesta). Depende de telemetría existente, calendario de campañas y reglas de negocio. Pendiente instrumentación y TPS peak aprobado por Ancoa.

<a id="t08"></a>

### T08 — Migración, calidad y conciliación de datos

- **Obligación y fuente:** RT-05.11 exige plan con alcance, origen, volumen, transformación, calidad, ejecución y reversión; RT-05.12 perfilado y saneamiento con decisión por defecto; RT-05.13 al menos dos ensayos completos en Preproducción; RT-05.14 conciliación con recuentos, sumas de control y muestreo dirigido, diferencias explicadas ([líneas 258–261](../../00_Bases/Bases_Transversales.md#L258)). SD-06 exige pruebas de equivalencia, integridad, conciliación, continuidad y retorno por sustitución y tratamiento individual de las catorce interfaces ([líneas 3106–3112](../../02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex#L3106)).
- **Ámbito/servicio:** olas de Retail y Emisor separadas por autoridad y finalidad; no combinar cartera financiera y datos comerciales en una única migración ni usar un solo criterio de conciliación para ambos.
- **Criterio:** **C-T08-01.** Antes del corte definitivo se ejecutan al menos dos ensayos completos de migración en Preproducción y se mide el tiempo total de cada uno.
- **Escenario, método y umbral:** repetir en ambiente representativo el procedimiento previsto para producción; mínimo dos ejecuciones completas conforme a RT-05.13.
- **Evidencia prevista, no ejecutada:** bitácora fechada de cada ensayo, duración, versión del proceso, datos de entrada y defectos encontrados.
- **Criterio:** **C-T08-02.** Antes de migrar se perfila y sanea cada fuente; el informe registra cada defecto y la decisión adoptada. El plan declara alcance, origen, volúmenes, transformaciones, criterios de calidad, ejecución y reversión.
- **Escenario, método y umbral:** perfilado de muestras y fuentes completas disponibles, aprobación de reglas y plan por ámbito Retail/Emisor; no se inicia corte con fuentes o transformaciones sin responsable.
- **Evidencia prevista, no ejecutada:** plan de migración aprobado, perfilado de datos y registro de defectos/decisiones.
- **Criterio:** **C-T08-03.** Tras cada ensayo/corte, la conciliación cubre recuentos, sumas de control y muestreo dirigido; toda diferencia tiene explicación verificable. La reversión de la ola queda preparada y comprobada.
- **Escenario, método y umbral:** comparar origen y destino por dominio y ola, con muestreo dirigido acordado; no se acepta ninguna diferencia inexplicada.
- **Evidencia prevista, no ejecutada:** conciliación reproducible, discrepancias resueltas, resultado de reversión y aprobación de negocio por entidad.
- **Estado/fuente del umbral:** exigencia RT-05.11–05.14. Volúmenes, criterios de conciliación por entidad y orden de olas se fijan tras inventario; no se declara cero diferencias sin respaldo de la fuente.
- **Evidencia prevista, no ejecutada:** mapa de fuentes y transformaciones; reporte de perfilado y decisión por defecto; bitácora de dos ensayos; conciliación; discrepancias con resolución; evidencia de reversión; acta de aprobación de cada ola.
- **Responsable/calendario/dependencias/brechas:** líder de Datos y responsables de negocio Retail/Emisor; perfilado durante meses 1–4; ensayos completos antes de cortes de Etapa 1 y Etapa 2, manteniendo producción en meses 16 y 21; operación y salida contractual hasta mes 56. Depende de accesos y extractos de origen, reglas de conservación y ventanas protegidas. Pendiente inventario detallado, calidad inicial y dueños que aceptarán las diferencias.

## Brechas que deben cerrarse para comprometer aceptación

1. Levantar TPS/concurrencia por intervalo del evento y de Navidad con Ancoa; 104.000 pedidos/3 días no determina esa tasa.
2. Acordar instrumentos, exclusiones y población de cobertura y deuda antes de activar bloqueos CI; mantener 70 %, 80 % y 5 % en métricas separadas.
3. Completar mapa bidireccional RT ↔ requisito/catálogo oficial v3.0 ↔ servicio/entregable ↔ prueba; llevarlo a 100 % al cierre.
4. Aprobar la modalidad fiscal y condiciones de crédito previamente autorizado durante desconexión; probar por separado el requisito mínimo de tienda 24 h.
5. Declarar sitio secundario, distancia y amenazas comunes para RT-07.02; no presumir que dos regiones o sitios son independientes sin análisis.
6. Cerrar la muestra de usuarios, las interfaces y el protocolo de evaluación WCAG 2.2 AA por perfil.
7. Inventariar fuentes, volúmenes, reglas y responsables de conciliación Retail/Emisor y calendarizar los dos ensayos completos por ola.

## Controles añadidos tras revisión independiente

Los controles siguientes completan obligaciones citadas sin prueba explícita en la primera lectura. Todos son diseño de verificación pendiente; se aplican separadamente a Retail, Emisor y recursos comunes con permisos segregados. El líder indicado prepara evidencia; QA revisa y la Contraparte Técnica acepta antes de meses 16/21 y en operación hasta mes 56.

<a id="t04"></a>

### T04 · Detección, respuesta y evidencia

Fuente exacta: [RT-11.14–19](../../00_Bases/Bases_Transversales.md#L556).

| Criterio interno | Escenario, método y umbral contractual | Evidencia prevista / responsable |
| :--- | :--- | :--- |
| C-T04-03 | Inyectar eventos e intentar alterarlos; inspeccionar retención y recuperar archivo. Registro central inalterable; ≥12 meses en línea y 24 adicionales en archivo. | Configuración, eventos íntegros y recuperación; Seguridad/Datos. |
| C-T04-04 | Simular abuso de cruce Retail/Emisor y verificar correlación SIEM por caso de negocio, además de infraestructura. | Casos de uso, alertas correlacionadas y traza incidente; Seguridad/SOC. |
| C-T04-05 | Introducir estímulo controlado en endpoint y workload nube/on-premise y verificar detección/respuesta. | Inventario cubierto, políticas y alertas/acción EDR; Seguridad. |
| C-T04-06 | Inspeccionar SOC declarado, ubicación, dotación, turnos y procedimientos; simular recepción fuera de horario. Cobertura 24x7. | Turnos, procedimientos y ticket atendido; responsable SOC. |
| C-T04-07 | Simular incidente crítico y escalar al Cliente dentro de 2 h desde detección. | Tiempos detección/comunicación, clasificación y cadena; líder incidentes. |
| C-T04-08 | Simular brecha de seguridad/datos personales; notificar Cliente con informe preliminar dentro de 24 h. | Notificación e informe con tiempos; líder incidentes/Cumplimiento. |
| C-T04-09 | Continuar simulación hasta entregar causa raíz dentro de 5 días hábiles siguientes. | RCA y fecha entrega contrastada calendario hábil; líder incidentes. |

Brecha B24: Seguridad/SOC y Cumplimiento deben fijar inventario de eventos/superficies, casos de uso, turnos, canales y calendario hábil, antes de campañas. La inspección de retención configurada y datos sintéticos de antigüedad permite verificar diseño; no demuestra haber operado ya 36 meses.

<a id="t05"></a>

### T05 · Replicación, conmutación y retorno

Fuente exacta: [RT-07.03–06](../../00_Bases/Bases_Transversales.md#L391).

| Criterio interno | Escenario, método y umbral contractual | Evidencia prevista / responsable |
| :--- | :--- | :--- |
| C-T05-06 | Generar retraso de replicación y verificar medición continua/alertamiento. El umbral de disparo debe declararse sin rebajar RPO 15 min. | Telemetría, alerta y configuración; SRE/Datos. |
| C-T05-07 | Personal del Cliente ejecuta procedimiento documentado de conmutación tras transferencia, automatizado en mayor medida posible. | Runbook, transferencia y ejecución observada; SRE y Operaciones Cliente. |
| C-T05-08 | Volver al sitio principal después de operar en contingencia y conciliar datos generados; retorno documentado y probado. | Bitácora, conciliación por ámbito y defectos; SRE/Datos y dueños de negocio. |

Brecha B25: SRE/Operaciones Cliente acuerdan umbral alertamiento, runbooks, operadores y datos de contingencia antes de cada producción. Estas pruebas no sustituyen el retorno POS ni las dos conmutaciones reales anuales.

<a id="t06"></a>

### T06 · Interfaces, errores y alfabetización digital

Fuente exacta: [RT-13.02–09](../../00_Bases/Bases_Transversales.md#L615).

| Criterio interno | Escenario, método y umbral contractual | Evidencia prevista / responsable |
| :--- | :--- | :--- |
| C-T06-03 | Ejecutar tareas en escritorio/tableta/teléfono; verificar adaptación del contenido y quiebres coherentes. | Matriz dispositivos, tareas y capturas; UX/QA. |
| C-T06-04 | Provocar errores/éxitos por tarea; verificar retroalimentación visual y mensajes indicando qué ocurrió/qué hacer, sin texto técnico final. | Casos, mensajes y prueba con usuarios; UX/QA. |
| C-T06-05 | Inspeccionar alto contraste, objetivos táctiles ≥44×44 px, icono con texto y flujos guiados paso a paso. | Mediciones y lista comprobación por interfaz; Accesibilidad/UX. |
| C-T06-06 | Inspeccionar sistema de diseño documentado: paleta acotada, ≤2 familias tipográficas, iconos coherentes, retícula y componentes reutilizables (RT-13.09). | Sistema diseño y contraste con interfaces; UX. |
| C-T06-07 | Determinar interfaces de terreno donde aplica RT-13.08 y ensayar guantes, intemperie, luminosidad variable y desconexión cuando corresponda. | Decisión aplicabilidad y protocolo/resultados; UX/Operaciones. |

Brecha B26: UX/Operaciones deben aprobar matriz de dispositivos y criterio de tareas, sistema de diseño y aplicabilidad por interfaz de terreno. RT-13.08 es según caso; esta ficha mantiene esa decisión pendiente en vez de exigirla indiscriminadamente.

<a id="t09"></a>

### T09 · Ambientes y puertas de entrega

Fuentes: [Bases Administrativas, artículo 24](../../00_Bases/Bases_Administrativas.md#L641) y [Transversales RT-04.01–10](../../00_Bases/Bases_Transversales.md#L222). Ámbito: repositorios y ambientes Retail/Emisor/compartidos, con controles separados. Responsable DevOps/Desarrollo y QA; ambientes operativos al H3, ensayos antes de producción 16/21 y cada liberación posterior. Evidencia prevista, no ejecutada.

| Criterio interno | Escenario/método/umbral | Evidencia prevista |
| :--- | :--- | :--- |
| C-T09-01 | Inspeccionar DEV, QA, Preprod, Prod y DR operativos/aislados; datos sintéticos/anonimizados en DEV, controlados/versionados QA, Prod restringida/auditada sin acceso interactivo directo desarrolladores. | Inventario, permisos, datos y prueba negativa entre ambientes. |
| C-T09-02 | Comparar Preprod y Prod topología/configuración/versiones y volumen representativo; declarar diferencias justificadas. | Inventario comparado y memoria de equivalencia. |
| C-T09-03 | Intentar escribir directamente a principal y promover cambio sin revisión por pares; ambos bloqueados por ramas protegidas. | Configuración repositorio y rechazos. |
| C-T09-04 | Ejecutar pipeline con fallo unitario, estático, composición, secretos y contenedor; comprobar controles de bloqueo definidos. | Pipeline versionado, resultados de cada fase y bloqueo de promoción. |
| C-T09-05 | Desplegar y provocar reversión; automatizados/reproducibles, sin intervención manual del paso a producción; mismo artefacto promovido sin recompilar, configuración externalizada. | Hash artefacto, bitácora despliegue/rollback y configuración por ambiente. |
| C-T09-06 | Demostrar estrategia declarada de liberación sin interrupción en Preprod antes de cada producción. | Sondas de servicio, errores y tiempos durante despliegue/retorno. |
| C-T09-07 | Inspeccionar secretos en gestor, rotación y auditoría; intentar usar credenciales embebidas y observar bloqueo. | Inventario gestor, rotaciones, logs y escaneo secretos. |
| C-T09-08 | Cambiar/revertir esquema versionado automáticamente con dos versiones aplicación coexistentes. | Migración esquema, rollback y prueba de compatibilidad. |

Brecha B27: DevOps/QA deben fijar inventario, controles de acceso, estrategia concreta de despliegue y protocolos equivalencia/rollback antes H3/campañas; no presume que la herramienta elegida demuestra el comportamiento.

<a id="t10"></a>

### T10 · Niveles de prueba y resiliencia

Fuente: [Bases Transversales cap.20.1](../../00_Bases/Bases_Transversales.md#L840). Responsable líder QA con Desarrollo, Integración y Operaciones; Retail y Emisor tienen campañas e informes separados. Evidencias previstas.

| Criterio interno | Escenario/método/umbral contractual | Evidencia prevista |
| :--- | :--- | :--- |
| C-T10-01 | Ejecutar unitarias/componentes continuamente; ninguna prueba fallida, cobertura bloqueante C-T01-01. | Resultados por versión y gate. |
| C-T10-02 | Tras cada despliegue QA ejecutar todos flujos integración del caso; ninguno con error. | Catálogo de flujos/interfaces y resultados, incluidos contratos y mensajes negativos. |
| C-T10-03 | Antes de promover Preprod ejecutar batería regresión automatizada completa, sin regresiones. | Línea base batería, resultados y diferencias. |
| C-T10-04 | Antes certificación cada etapa ejecutar aceptación usuario; casos aprobados/firmados por Contraparte Técnica. | Casos, observaciones/correcciones y acta futura. |
| C-T10-05 | Inyectar fallos de componentes/enlace y verificar degradación controlada y recuperación sin intervención; antes cada producción y semestral en operación. | Protocolo fallos, estados y recuperación autónoma; no sustituye DR. |

Brecha B28: QA/Integración/Operaciones y Contraparte deben cerrar catálogo de flujos/regresión/UAT, actores y estímulos/límites de recuperación, antes campañas 16/21; calendario semestral durante 21–56.

<a id="t11"></a>

### T11 · Marco de calidad y madurez

Fuentes: [Bases Administrativas, criterios ISO/IEC 25010](../../00_Bases/Bases_Administrativas.md#L657) y [contenido SD09](../../00_Bases/Bases_Administrativas.md#L2168); [calidad datos RT-05.04](../../00_Bases/Bases_Transversales.md#L246). Responsables QA/Arquitectura y Datos; aplica por servicio/ámbito antes línea base/campañas, con seguimiento en operación.

| Criterio interno | Escenario/método/umbral | Evidencia prevista |
| :--- | :--- | :--- |
| C-T11-01 | Inspeccionar marco ISO/IEC 25010 y umbrales numéricos declarados para funcionalidad, desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad. | Mapeo ocho categorías a criterios/fuentes; brecha explícita para métrica aún no declarada. |
| C-T11-02 | Inspeccionar modelo de madurez elegido, escala, evaluación inicial y mejora; elección/objetivo pendientes, no inventar nivel alcanzado. | Modelo/escala, diagnóstico futuro y plan mejora. |
| C-T11-03 | Capturar datos inválidos y comprobar validación; medir completitud/exactitud/consistencia ISO/IEC 25012 y tablero Cliente. | Reglas captura, defectos/rechazos y métricas por dominio con denominador. |

Brecha B29: QA/Arquitectura deben completar modelo/umbrales faltantes de las ocho categorías y madurez, sin sustituir máximos contractuales; Datos y dueños de negocio aprueban reglas y umbrales calidad ISO 25012. No se declara certificación de estas normas.

### Complemento de seguridad y continuidad tras segunda revisión

Fuentes: [RT-11.13](../../00_Bases/Bases_Transversales.md#L550), [RT-07.01](../../00_Bases/Bases_Transversales.md#L389) y [RT-10.02–04/08](../../00_Bases/Bases_Transversales.md#L518). Evidencia prevista. Seguridad/Arquitectura y Operaciones mantienen estos controles por ámbito, antes de producción 16/21 y ante cambios durante operación.

| Criterio interno | Escenario/método/umbral | Evidencia prevista / dueño |
| :--- | :--- | :--- |
| C-T04-10 | Inspeccionar cada dominio, puerto y servicio expuesto desde fuera de red Cliente y comparar escaneo autorizado con declaración completa. | Inventario exposición y divergencias resueltas; Seguridad/Arquitectura. |
| C-T05-09 | Inspeccionar modalidad activo-activo o activo-pasivo declarada y justificada frente costo, RTO y complejidad operacional. | Decisión arquitectura y pruebas acordes modalidad; Arquitectura/SRE. |
| C-T05-10 | Clasificar todos servicios crítico/alto/medio/bajo, justificar impacto y vincular nivel Art.78 correspondiente; comprobar inventario completo. | Clasificación, impacto y niveles fuente; Operaciones y dueños negocio. |
| C-T05-11 | Inspeccionar BCP conforme ISO 22301 con BIA, contingencias, respaldo manual y criterios activación; ejercitar escenario propuesto para comprobar procedimientos. | Plan/BIA y simulación prevista con actores; Operaciones y Cliente. |
| C-T05-12 | Inspeccionar continuidad TIC conforme ISO/IEC 27031 y su articulación con DR; recorrer escenario de activación/retorno y responsables. | Plan TIC, enlaces a DR y bitácora de recorrido previsto; SRE/Operaciones. |
| C-T10-06 | Para cada dependencia externa probar ausencia de respuesta, error y lentitud; contrastar comportamiento documentado. | Inventario dependencias, contratos de degradación y resultados; Integración/QA. |

Brecha B30: Seguridad y Arquitectura completan inventario exposición antes campaña; Arquitectura/SRE documentan modalidad de sitios; Operaciones/Cliente aprueban clasificación/Art.78 y planes BCP/TIC; Integración/QA definen comportamiento por dependencia. No inventar SLA de categorías cuya tabla oficial sea ilegible: mantener valor pendiente con fuente Art.78. El ejercicio de BCP es propuesta de verificación del plan, no nueva frecuencia contractual ni certificación ISO.
