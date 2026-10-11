# Revisión independiente de SD-09

Revisión documental de las ocho piezas de `80_Artefactos/sd-09_contexto/`, contrastadas con las Bases, el Anexo D, el diseño vigente y las referencias de catálogo señaladas por la matriz. No se editaron los artefactos revisados. Estado de esta revisión: hallazgos para corrección; no equivale a aprobación ni a revisión humana registrada del entregable.

## Hallazgos materiales

### 1. Seguridad transversal incompleta frente a los RT enumerados

**Ubicación:** [transversales.md, T04, líneas 78–90](transversales.md#L78).

T04 cita RT-11.01–11.12 y RT-11.20, pero sus dos criterios verificables cubren amenazas/controles, pruebas de segregación, plazos de vulnerabilidades y pentest. No hay escenarios, umbrales ni evidencia previstos para varias obligaciones obligatorias citadas, en particular registro central e inalterable y retención (RT-11.14), SIEM y casos de uso (RT-11.15), EDR en nube y on-premise (RT-11.16), SOC 24x7 (RT-11.17), comunicación de incidente crítico dentro de 2 h (RT-11.18), ni aviso de brecha en 24 h y análisis causal en cinco días hábiles (RT-11.19). Citar el rango sin criterios deja una brecha de cobertura interna.

**Sugerencia exacta:** añadir criterios internos separados C-T04-03 a C-T04-07, uno por obligación/grupo no reducible, con evento de prueba o inspección, frecuencia/plazo contractual, evidencia concreta y responsable. Para RT-11.18–19, usar ejercicios de incidente y registros fechados de notificación/análisis; para RT-11.14–17, inspeccionar retención/configuración SIEM/EDR y turnos/procedimiento SOC. Marcar dependencias aún no definidas como brecha, sin declarar cumplimiento.

### 2. Accesibilidad y usabilidad no cubren todos los requisitos que la ficha declara

**Ubicación:** [transversales.md, T06, líneas 114–125](transversales.md#L114).

La fuente enumera RT-13.02–13.07, pero C-T06-01/02 no fijan prueba ni evidencia explícita para responsividad en escritorio/tableta/teléfono (RT-13.02), retroalimentación y mensajes de error comprensibles (RT-13.06), ni contraste, controles táctiles ≥44×44 px, icono acompañado por texto y flujo guiado (RT-13.07). La investigación con usuarios sí está mencionada, pero faltan los protocolos y criterios observables para esas obligaciones. RT-13.08–13.09 tampoco aparecen; si aplican al caso/interfaz, la matriz debe decirlo y cubrirlos.

**Sugerencia exacta:** añadir criterios C-T06-03 (matriz de dispositivos/puntos de quiebre y pruebas de adaptación), C-T06-04 (casos de error/retroalimentación por perfil) y C-T06-05 (lista de comprobación visual/táctil/guiada, incluyendo medición de objetivos de 44×44 px); asignar interfaz, método manual/automático, informe/capturas y responsable. Registrar decisión de aplicabilidad para RT-13.08–13.09.

### 3. Continuidad omite pruebas explícitas de replicación y retorno

**Ubicación:** [transversales.md, T05, líneas 94–112](transversales.md#L94).

T05 recoge autonomía 24 h, sincronización posterior, RTO/RPO, distancia y disponibilidad; sin embargo, al citar RT-07.03–07.06 no convierte en criterios comprobables la medición/alerta del retraso de replicación (RT-07.03), el procedimiento de conmutación ejecutable por personal del Cliente (RT-07.05) y el retorno probado con conciliación de datos de contingencia (RT-07.06). La frase de C-T05-03 sobre conmutación real no verifica por sí sola esos puntos. La evidencia de C-T05-01 sobre operaciones locales tampoco sustituye una prueba de retorno al sitio principal.

**Sugerencia exacta:** añadir C-T05-06 para generar retraso de replicación y verificar medición/alertamiento; C-T05-07 para ejecutar el runbook de conmutación con personal del Cliente; C-T05-08 para retorno y conciliación de operaciones en contingencia. Precisar artefactos (alertas, tiempos, runbook, conciliación), responsable de ejecución y dueño que valida. Mantener dos conmutaciones reales por año y el requisito semestral antes de producción/operación donde corresponda.

## Hallazgos de trazabilidad y precisión

### 4. Enlace interno a R20 apunta a un ancla inexistente

**Ubicación:** [resultados.md, línea 310](resultados.md#L310).

El enlace `resultados.md#r20-bloqueo-de-aceptación-sin-información-completa` no coincide con el ancla explícita `<a id="r20"></a>` de la ficha en la línea 222. La síntesis de R28 queda sin destino fiable.

**Sugerencia exacta:** cambiar el destino por `resultados.md#r20` (o por el ancla explícita equivalente en la misma página). Los fragmentos `#Lnn` a las fuentes son referencias de número de línea y no se consideran anclas Markdown internas.

### 5. T01 repite la definición de cobertura y evidencia

**Ubicación:** [transversales.md, líneas 46–53](transversales.md#L46).

C-T01-01 ya exige reportar por separado 70 % total y 80 % código nuevo; C-T01-02 vuelve a definir el mismo reporte diferencial y vuelve a condicionar el build al 70 %. También hay dos bullets de evidencia para lo mismo (líneas 50 y 52). No es una contradicción de umbrales, pero puede producir dos controles duplicados y confundir la puerta CI.

**Sugerencia exacta:** conservar un único criterio de puerta para ≥70 % total y una submedición informativa/objetivo ≥80 % de código nuevo; consolidar la evidencia prevista en una sola lista. Mantener explícito que 80 % es objetivo SD-06, no requisito transversal.

## Comprobaciones que resultaron coherentes

- El alcance declara 28 resultados del Anexo D, no cobertura completa del catálogo. La salvedad se mantiene en README y cobertura; el Formulario T-12 se reconoce como respuesta requisito por requisito pendiente.
- Los códigos R01–R28, T01–T08 y C-R/C-T se identifican como internos; la fuente oficial de catálogo v3.0 se distingue del borrador v3.1. Los resultados no afirman equivalencia exhaustiva de todos los IDs citados por Anexo D.
- La secuencia de Anexo D está alineada con la convención solicitada: resultado 1 apunta a línea 9 y resultado N a línea N+8 (numeración contrastada con archivo real en la corrección final). Los pilotos consultan filas de Excel para sus IDs y distinguen fuente de propuestas.
- Los umbrales SD-06 se conservan separados: 70 % de lógica de negocio bloqueante, 80 % objetivo para código nuevo, deuda técnica ≤5 % y trazabilidad al 100 % al cierre. El 100 % queda limitado a la línea base indicada y no se presenta como cobertura total ya alcanzada.
- R21 exige cero hallazgos críticos/altos abiertos según Bases Transversales 20.1, línea 847, y pentest por tercero independiente, anual y antes de cada producción según RT-11.20, línea 562. También declara que no implica certificación ISO ni aprobación regulatoria.
- Retail y Emisor se separan en ámbitos, responsables y evidencia; los cruces requieren registro y controles. Los resultados compartidos identifican responsabilidad del cliente frente a la del proponente.
- El tratamiento de máximos del Caso no los rebaja con P95: los ensaya por operación y conserva el máximo observado; P95 se reporta aparte cuando corresponde. El volumen de 104.000 pedidos en tres días no se convierte en TPS.
- Meses 16 y 21 para producción y mes 56 para cierre se conservan; enero de 2027 y mes 24/diciembre de 2028 aparecen como supuestos. Se advierte que la Contraparte Técnica decide y firma, que la evidencia es futura y que no hay pruebas, aprobación ni certificaciones declaradas.

## Seguimiento de correcciones

Revisé la versión actualizada de `transversales.md` y `resultados.md` después de la corrección del autor. Los tres hallazgos materiales iniciales (seguridad RT-11.14–19, accesibilidad/usabilidad RT-13.02–09 y continuidad RT-07.03–06) ya tienen criterios, métodos o inspecciones y evidencias previstas; se agregaron además los controles T09–T11. El enlace de R28 ahora apunta a `#r20`. El 70 % bloqueante y el 80 % objetivo quedaron como criterios separados, sin cambiar sus umbrales. Esos hallazgos se consideran cerrados en la versión revisada.

Quedan estas brechas materiales de cobertura dentro de los mismos grupos de obligaciones:

1. **RT-11.13 no tiene criterio.** T04 pasa de RT-11.07–12 a RT-11.20 y los nuevos criterios cubren RT-11.14–19, pero no verifican la declaración de superficie de exposición (dominios, puertos y servicios alcanzables desde fuera de la red del Cliente). Añadir un criterio de inventario y contraste técnico con evidencia versionada y responsable de Seguridad.
2. **RT-07.01 no tiene criterio explícito.** T05 cubre distancia, replicación, RTO/RPO, conmutación y retorno, pero no exige declarar/justificar modalidad activo-activo o activo-pasivo frente a RTO y complejidad operacional. Añadir decisión de arquitectura, responsable, memoria de justificación y revisión antes de fijar el sitio secundario.
3. **RT-10.02–10.04 y RT-10.08 quedan citados sin aceptación verificable suficiente.** C-T05-05 mide disponibilidad de servicios ya clasificados como críticos, pero no pide inventario y justificación de clasificación para todos los servicios (RT-10.02); se nombran los planes conforme a ISO 22301/27031, sin exigir su inspección ni evidencia de BIA, contingencias, procedimientos manuales, activación y articulación TIC/DR (RT-10.03–04); tampoco se comprueba el comportamiento ante error/lentitud de cada dependencia externa (RT-10.08). Añadir criterios con inventario firmado, planes/versiones y ejercicios, y matriz de dependencias con escenarios de timeout/error/degradación, respuestas y evidencias.

La duplicación menor de evidencias en T01 permanece (líneas 50 y 52 de `transversales.md`), aunque ya no confunde la asignación del 70 % y el 80 % a los criterios. Puede consolidarse como limpieza editorial; no la considero bloqueante.

## Dictamen final tras segunda ronda

Revisé los criterios C-T04-10, C-T05-09–12 y C-T10-06 y el registro B30 en la versión actual de `transversales.md`. Responden a las tres brechas residuales que había señalado: inventario completo de exposición conforme a RT-11.13; modalidad y justificación del sitio secundario conforme a RT-07.01; clasificación de servicios vinculada al Art. 78, inspección de BCP/continuidad TIC y pruebas de dependencia conforme a RT-10.02–04/08. La tabla ilegible del Art. 78 queda explícitamente pendiente, sin inventar umbrales, y el ejercicio BCP se identifica como método propuesto, sin atribuirle una frecuencia contractual ni certificar ISO.

Por tanto, **no encuentro errores materiales pendientes entre los hallazgos de esta revisión independiente**. Las brechas de línea base, datos, perfiles, decisiones de negocio y cobertura completa del catálogo permanecen correctamente como pendientes declarados; no son hallazgos cerrados ni se interpretan aquí como cumplimiento ya demostrado. Esta conclusión se limita al cierre de los hallazgos identificados en las dos rondas.

## Alcance de esta revisión

Se leyeron `AGENTS.md`, las skills `licitacion-workflow`, `technical-writing` y `humanizer`, y la regla RR-24. El texto de este informe es una revisión documental directa, no una edición de los artefactos SD-09.

Nota de corrección final del principal: la pauta inicial de revisión N+9 era incorrecta para el archivo real. Se contrastó con `nl -ba`: R01 está en línea 9 y R28 en línea 36; se corrigieron las 28 referencias de resultados/cobertura y las seis de pilotos. La revisión de rango por sí sola no detectaba este desplazamiento.
