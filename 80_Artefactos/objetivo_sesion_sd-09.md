# Objetivo de sesión — Subdocumento 9

Fecha de preparación: 2026-10-11. Objetivo solicitado por el usuario: completar el Plan de calidad con consistencia respecto de los demás subdocumentos y los requisitos del profesor.

## Estado inicial

Se actualizó `origin/main` y se integró en `work` mediante `git merge --ff-only origin/main`, desde `342b218` hasta `6052a3b`, sin conflictos. La rama local `main` apunta a la misma base. No se publicó ningún cambio remoto.

La fuente editable es `02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex`. Existe y contiene únicamente la estructura. No reimportar el Markdown ni modificar el preámbulo corporativo. El maestro Markdown registra estado y trazabilidad.

## Trabajo y criterios de cierre

1. Desarrollar la introducción y conservar los títulos exactos del Comunicado 10, apartado del subdocumento 9, líneas 879–910. La sección 9.1 «Plan de Calidad» desarrolla ISO/IEC 25010, madurez y métricas con umbrales bloqueantes. La 9.2 «Estrategia de Aseguramiento de Calidad» desarrolla puertas de calidad, revisión por pares, análisis estático/dinámico, pruebas ISO/IEC/IEEE 29119 y trazabilidad. La 9.3 «Alineación con Plan de Trabajo» ubica las actividades en la EDT y el cronograma del capítulo 7.
2. Contrastar cada compromiso con Bases Administrativas, Art. 24 y Formularios T-13/T-17, y Bases Transversales, capítulos 4 y 20. Definir responsables, condiciones de entrada/salida, evidencias y tratamiento de incumplimientos. No estimar porcentajes incompletos del T-21.
3. Conservar los compromisos vigentes del T-10 del subdoc 6, líneas 751–755. La cobertura de lógica de negocio es al menos 70 % y bloqueante; el 80 % para código nuevo es un objetivo; la razón de deuda técnica es como máximo 5 %; la cobertura de trazabilidad llega al 100 % al cerrar cada etapa. Son categorías diferentes y deben medirse por separado.
4. Vincular pruebas con los servicios y los 28 resultados del Anexo D del subdoc 3. Distinguir aceptación de entregable, marcha blanca y resultado. El proveedor controla la calidad; la Contraparte Técnica valida y firma. Mantener separados retail y filial emisora, incluyendo datos y pruebas negativas de autorización y consentimiento.
5. Detallar en T-13 niveles, tipos, ambientes, datos, automatización y calendario. Incluir cobertura continua; integración en QA; regresión antes de preproducción; UAT; carga a 1,5 veces el peak; resiliencia y DR antes de producción y semestralmente; pentest antes de producción y anual; accesibilidad WCAG 2.2 AA; dos ensayos de migración con conciliación. Confirmar los umbrales más exigentes del caso antes de fijar RTO/RPO.
6. Desarrollar T-17 por hito con entregables, criterios objetivos, evidencia, plazos de revisión, observaciones y acta. Respetar las salidas a producción en los meses 16 y 21 y operación hasta el mes 56, incluyendo actividades de calidad en ambas etapas solapadas.
7. Aplicar las reglas RR-NN, la skill `humanizer` acotada por RR-24, figuras integradas y explicadas, referencias y declaración real de uso de IA. Usar las clases como criterio metodológico y las Bases como fuente del caso. FEP01, diapositivas 13–15, exige escenario con estímulo, condición, respuesta y métrica; diapositiva 173 distingue percentiles, throughput y concurrencia. Contrastar también la rúbrica de retroalimentación del Informe 1. No declarar revisión humana inexistente.
8. Actualizar el maestro; ejecutar `verificar`, `verificar-redaccion --parte T7-09` y `compilar --parte T7-09` mediante `05_Gestion/scripts/exportar_latex.py`. Inspeccionar el PDF y entregar fuente y vista previa. El cierre técnico queda en estado borrador hasta revisión humana; no presentarlo como aprobado.

## Entorno preparado

Dos agentes `gpt-6-luna` trabajaron en paralelo, uno en recopilación de información y otro en entorno. Pandoc, XeLaTeX, latexmk, Inkscape, DejaVu Sans y pypdf están disponibles. Se crearon enlaces locales de skills con `link_skills.py` y el doctor terminó correctamente. La plantilla de T7-09 pasó `verificar`.

Se instaló Graphify 0.9.85 con `uv tool install 'graphifyy[mcp,office,pdf]'` y se comprobó su CLI. La instalación no acredita una conexión MCP activa. No se generó un índice semántico ni se enviaron documentos a un proveedor externo.

`ragdocs` permanece deshabilitado; faltan bindings de Qdrant y embeddings en el entorno. Jira es opcional y requiere autenticación; OpenCode no está disponible en PATH. La lectura de archivos y las herramientas locales permiten avanzar sin esos servidores. No se añadieron credenciales al repositorio.

El subdoc 9 todavía no está redactado. Este archivo registra el objetivo y los criterios para continuar la sesión, no una declaración de cumplimiento.

## Estado actual — 2026-10-11

El estado inicial descrito arriba ya fue superado. Las secciones 9.1, 9.2 y 9.3 están redactadas como borrador en `02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex`, con tres figuras, matriz interna de cobertura y Preview sincronizado. La skill `citas-proyecto` y el índice de folios del Caso 09 están integrados; el Markdown anterior del Caso permanece intacto. `verificar` pasa, `verificar-redaccion` informa cero errores y dos avisos RR-19 sobre títulos de tablas, y la compilación genera una vista previa de 22 páginas. Siguen pendientes la revisión humana y el cierre de los formularios T-13 y T-17; no se registra aceptación contractual ni pruebas ejecutadas.
