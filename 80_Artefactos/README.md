# Artefactos generales del proyecto

Material que no pertenece a una etapa del pipeline de la propuesta ni a un subdocumento concreto.

| Artefacto | Qué es | Estado |
| :--- | :--- | :--- |
| `CONSULTAS_ONLYSIMPLESOLUTIONS_20260901.xlsx` | Planilla de consultas al mandante con la nomenclatura del Art. 43.3 | Versada |
| `consultas-al-mandante.md` | Espejo de la planilla anterior, para poder buscarla sin abrir Excel | Versado |
| `seccion3_innovaciones.md` | Material de apoyo sobre innovaciones (conservado para el capítulo 13) | Antecedente |
| `sd-01_contexto/` | Notas para el sd-01: hechos sobre la empresa que salieron de otros trabajos y deben reflejarse en la presentación | Borrador |
| `sd-03_contexto/` | Contexto de trabajo del sd-03: plan de 3.2, análisis de actores y servicios, descripción del alcance del producto y entregables (borradores) | Borrador |
| `revision_informe_1_transcripcion.md` | Transcripción por página del PDF de retroalimentación del Informe 1; conserva la procedencia y el hash del origen | Fuente de revisión |
| `revision_informe_1_rubrica_de_cierre.md` | Informe que transforma esa retroalimentación en criterios de cierre por subsección del Comunicado 10 | Contexto prioritario para el siguiente ciclo |

## Reglas

- Son documentos de **lectura para el equipo**, no fuentes de la propuesta: por eso conservan su
  formato original. Cuando su contenido deba alimentar un subdocumento, se trascribe a `.md` en
  `02_Propuesta/` con la referencia al artefacto de origen.
- El espejo en `.md` de la planilla de consultas se genera desde el `.xlsx`: si el `.md` y el Excel
  difieren, **manda el Excel**.
- La rúbrica de revisión es una lista interna de comprobación: sus observaciones se contrastan
  con las Bases y con la versión actual de cada subdocumento antes de dar una sección por cerrada.

## Nomenclatura

| Tipo | Patrón |
| :--- | :--- |
| Consulta al mandante | `CONSULTAS_ONLYSIMPLESOLUTIONS_AAAAMMDD.xlsx` |
