# Reconocimiento del sistema de artefactos

Fecha: 2026-09-29  
Rama: `feat/artefactos`

## Convenciones reales en `02_Propuesta/`

El índice y los maestros describen un maestro por subdocumento con patrón `sd-NN_titulo.md` y secciones esperadas con patrón `sd-NN_sN_titulo.md`. Los adjuntos esperados usan prefijos `adj-`, `diag-` o `form-`; sus nombres y declaraciones aparecen en cada maestro. El reconocimiento encontró los catorce maestros, pero no encontró archivos de sección `sd-*_s*.md`. Por eso el estado declarado en las tablas de los maestros no demuestra que las secciones estén materializadas como artefactos.

## Espejo de requerimientos

Existe un espejo: `01_Requerimientos/md/catalogo-de-requerimientos-depurado-v30.md`. Su encabezado indica que fue generado desde el Excel oficial v3.0 y que el Excel prevalece si difieren. Las tablas del espejo incluyen IDs estables (RF, RNF y OP). En la muestra revisada no se identificó una columna general que vincule cada requerimiento con un subdocumento T-7; la cobertura tendrá que validarse contra el propio contenido, las notas de los maestros y los mapeos existentes, sin inventar asignaciones.

## Jira

La fuente del plan está en `05_Gestion/jira/plan/restructuracion_2026-09-29_plan.json`; los mapeos y payloads están en `05_Gestion/jira/mapeo/`; los scripts operativos están en `05_Gestion/jira/scripts/`. El README de Gestión registra 8 agrupadoras, 34 historias y 77 subtareas. Los archivos muestran claves `OSS-*`; el mapeo vigente de subtareas está en `restructuracion_2026-09-29_mapeo_subtareas.csv`. Los archivos de `historico/` son referencias de la estructura anterior y no deben tratarse como mapa operativo.

## Agentes y skills

Existen `AGENTS.md` y `CLAUDE.md` en la raíz. `CLAUDE.md` remite a `AGENTS.md`. `.opencode/` contiene configuración, plugin local y skills; la skill `licitacion-workflow` remite a las skills de arquitectura, estimación, riesgos, escritura, formularios y PDF. No se encontraron carpetas `.agents/skills/` ni `.claude/skills/` en el inventario inicial.

## Estado por subdocumento

Conteo sobre archivos Markdown presentes directamente en cada carpeta `sd-NN_*`, incluyendo maestro, no secciones. La clasificación se refiere a la presencia de archivos, no a calidad ni aprobación editorial.

| Parte | Archivos Markdown | Palabras aprox. | Estado material |
|---|---:|---:|---|
| T7-01 | 1 | 734 | Maestro presente; secciones no materializadas |
| T7-02 | 1 | 800 | Maestro presente; secciones no materializadas |
| T7-03 | 1 | 992 | Maestro presente; secciones no materializadas |
| T7-04 | 1 | 746 | Maestro presente; secciones no materializadas |
| T7-05 | 1 | 791 | Maestro presente; secciones no materializadas |
| T7-06 | 1 | 421 | Maestro presente; secciones no materializadas |
| T7-07 | 1 | 566 | Maestro presente; secciones no materializadas |
| T7-08 | 1 | 476 | Maestro presente; secciones no materializadas |
| T7-09 | 1 | 417 | Maestro presente; secciones no materializadas |
| T7-10 | 1 | 501 | Maestro presente; secciones no materializadas |
| T7-11 | 1 | 447 | Maestro presente; secciones no materializadas |
| T7-12 | 1 | 442 | Maestro presente; secciones no materializadas |
| T7-13 | 1 | 570 | Maestro presente; secciones no materializadas |
| T7-14 | 1 | 422 | Maestro presente; secciones no materializadas |

Existe `06_Informes/informes/informe-1_oferta-tecnica.docx` como fuente documental consolidada. La aceptación de cualquier migración requiere cotejar el texto extraído con el DOCX y revisar los bloques sin mapeo seguro.

## Decisiones pendientes

- El mapeo entre encabezados del Informe 1 y el índice obligatorio del Comunicado 10 necesita aprobación humana cuando haya ambigüedad.
- Los archivos de sección se crearán desde contenido fuente aprobado; no se inferirá que las tablas actuales de los maestros equivalen al índice del Comunicado 10.
- No se encontró en esta fase una conexión a Google Docs necesaria para publicar la copia nativa; esa salida requiere autenticación y verificación durante su fase.
