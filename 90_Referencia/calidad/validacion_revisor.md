# Validación inicial del agente revisor de calidad

**Fecha:** 2026-10-11. **Agente examinado:** `/root/revisor_calidad`, modelo `gpt-6.1-sol`. **Coordinación y evaluación:** agente raíz. Conversión, investigación y preparación se delegaron a Luna y Sol según la preferencia de la sesión. Este registro resume el informe emitido por el revisor; no certifica competencia universal ni conformidad de un producto.

## Preparación y alcance real

El revisor aplicó la [skill canónica](../../.agents/skills/revisor-calidad/SKILL.md), leyó las **38 páginas** de [contextoCalidad.md](contextoCalidad.md) y la [investigación](investigacion_calidad.md). Inventarió las 38 anclas sin faltantes. No afirmó inspección visual propia del PDF.

Examinó los diez archivos de `80_Artefactos/sd-09_contexto/`: README, resultados, pilotos, transversales, cobertura, verificación, aceptación, brechas, revisión independiente y verificación documental. Contó y revisó **115 criterios únicos: 58 de resultados y 57 transversales**, correspondientes a 28 resultados, 11 grupos y seis pilotos. Los 21 criterios de pilotos ya están incluidos en los 115. Separó las 38 brechas existentes (P01–P08 y B01–B30) de sus hallazgos nuevos.

Contrastó pasajes materiales de las Bases Administrativas, Transversales, Caso 09, Anexo D y SD06. No abrió los catálogos Excel, ni revisó íntegramente SD03–SD08 o los formularios económicos. No pudo revisar la vista preliminar de Google Docs: la copia temporal indicada no existía en este entorno. La cobertura documental no equivale a cumplimiento técnico ni a cobertura completa del catálogo.

La coordinación abrió fuentes públicas de ISO (25010:2023, principios y publicación de 9001:2026) y NIST (muestreo/curva OC). El revisor distinguió esa comprobación delegada de una consulta propia. La investigación conserva enlaces, fecha y límites de acceso; no se atribuyeron cláusulas de normas de pago no leídas.

## Prueba sin acceso a la clave

El agente recibió los [casos de revisión](pruebas/casos_revision.md), sin consultar la [clave del evaluador](pruebas/clave_evaluador.json). El evaluador comparó sus clasificaciones con la clave después de recibir el informe.

| Caso | Concepto comprobado | Resultado observado |
| :--- | :--- | :--- |
| A01 | Calidad y grado | Detectó el error. |
| A02 | Ocho categorías contractuales, nueve características de 2023 y certificación indebida | Detectó los errores. |
| A03 | Cinco principios docentes frente a siete ISO; escala pedagógica frente a CMMI | Detectó los errores. |
| A04 | QA preventivo, QC y aceptación por Contraparte | Detectó los errores. |
| A05 | Pareto e Ishikawa: proporción y causalidad no demostradas | Detectó los errores. |
| A06 | Muestreo por conveniencia y sustitución indebida de conciliación | Detectó los errores. |
| A07 | Cobertura 70/80 %, ausencia de defectos y deuda medida aparte | Detectó los errores. |
| A08 | Máximo frente a P95 y volumen frente a tasa peak | Detectó los errores. |
| A09 | Heurística 15–25 % frente a obligación; calidad y presupuesto | Detectó los errores. |
| A10 | Boehm histórico y estimaciones CISQ | Detectó los errores. |
| A11 | Acta, plazos 10+10 hábiles y pagos con fuente contractual | Detectó los errores. |
| A12 | Multas y garantías sin regla legal universal | Detectó los errores; remitió a las Bases del caso. |
| A13 | Diseño válido con perfil pendiente | Conservó el diseño condicionado; no exigió registros de producción inexistentes. |
| A14 | Mapeo y controles adecuados, estados separados | Conservó el diseño sin hallazgo material. |

**Resultado del conjunto: 14/14 clasificaciones coincidentes con la clave; 12/12 fragmentos defectuosos detectados y dos controles conservados con sus límites.** No se infiere precisión futura a partir de este conjunto pequeño.

## Hallazgos nuevos sobre la matriz SD09

Los identificadores H01–H05 son hallazgos internos de revisión, no requisitos oficiales. La coordinación cotejó los cinco contra los pasajes locales indicados. Las correcciones siguen pendientes y no se modificaron los criterios ni sus estados durante esta revisión.

| ID y prioridad | Ubicación evaluada y fuente | Brecha | Remedio y condición de cierre | Responsable propuesto por rol |
| :--- | :--- | :--- | :--- | :--- |
| H01 · Alta | [C-R19-01](../../80_Artefactos/sd-09_contexto/resultados.md#r19); Caso RT-05.10, línea 794 | La retención por plazo del crédito más seis años aparece como propuesta, aunque el Caso la exige. | Separar retención obligatoria de recuperación ≤5 min y simulacro de diez años propuestos; conservar atribución uniforme entre ficha, fuente y campaña. | Cumplimiento Emisor y dueño de Evidencia Financiera, con QA. |
| H02 · Media | [T07](../../80_Artefactos/sd-09_contexto/transversales.md#t07), calendario; RT-09.09, línea 510, y Art. 25, línea 675 | La proyección trimestral de capacidad se rotula como frecuencia propuesta. | Identificar obligación y prever informe trimestral, alertas anticipadas y propuesta de ajuste; cerrar con calendario y modelo de informe. | Arquitectura de rendimiento y Operaciones. |
| H03 · Media | [C-T02-01](../../80_Artefactos/sd-09_contexto/transversales.md#t02); SD06, líneas 3174–3179 | Se menciona duplicación, pero falta el límite ≤3 % comprometido en SD06 y su decisión de control. | Incorporar umbral, unidad, población y exclusiones; separar duplicación de deuda y cobertura; cerrar con criterio trazado y reporte/decisión previstos. | Calidad y líderes de Desarrollo. |
| H04 · Media | [C-T09-07](../../80_Artefactos/sd-09_contexto/transversales.md#t09); RT-04.09, línea 230 | Se verifica rotación de secretos sin exigir explícitamente que sea automática. | Verificar configuración y ensayo de rotación automática, renovación de consumidores y auditoría; distinguir evidencia automática de manual. | DevOps y Seguridad. |
| H05 · Alta antes de aceptación de desempeño | [C-T07-01/02](../../80_Artefactos/sd-09_contexto/transversales.md#t07); Transversales 20.1, línea 844 | Se separan carga a 1,5× peak y medición de umbrales bajo peak, sin unir expresamente ambas condiciones. | Comprobar umbrales del Capítulo 9 bajo 1,5× peak por escenario; documentar protocolo y decisión. Separar esa aprobación del estrés hasta quiebre. | Arquitectura de rendimiento y QA. |

## Aplicación al futuro SD09

Conservar los controles ya adecuados: separación Retail/Emisor, máximos separados de P95, cobertura 70/80 %, conciliación exhaustiva, autonomía y retorno, pentest independiente y aceptación humana. Completar el Plan de Calidad con gobierno preventivo, revisiones/auditorías, responsables y calendario, muestreo justificado, costos por las cuatro categorías y cadena requisito → métrica → prueba → hito/EDT → pago con fuentes verificables. Estos elementos corresponden al plan futuro; una matriz parcial no demuestra ni promete por sí sola todo el aseguramiento.

**Dictamen documental de la matriz: diseño con brechas. Ejecución: verificación pendiente. Aceptación humana: pendiente.** La prueba del agente no ejecutó campañas ni aprobó entregables. El cierre exige corregir las formulaciones y resolver las decisiones pendientes; el cumplimiento posterior exige evidencia real y actas de quienes tengan facultad de aceptación.

## Verificación de los archivos de preparación

La coordinación comprobó 38/38 anclas, la existencia de los enlaces locales de la carpeta y el SHA-256 del PDF preservado: `4c613e060757fea773ea32ea6f1a83d6ce6375bbdcbdc0aa83cf5d0e5e5d04c0`. El agente de conversión cotejó visualmente diez páginas y recuperó 17 tablas Markdown; la extracción íntegra conserva navegación y pies para auditoría. Se corrigieron las referencias cruzadas de NASA/29119 y el mapeo de folios 99–104 en la investigación.
