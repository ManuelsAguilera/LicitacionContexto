# Artefactos generales del proyecto

Material que no pertenece a una etapa del pipeline de la propuesta ni a un subdocumento concreto.

| Artefacto | Qué es | Estado |
| :--- | :--- | :--- |
| `CONSULTAS_ONLYSIMPLESOLUTIONS_20260901.xlsx` | Planilla de consultas al mandante con la nomenclatura del Art. 43.3 | Versada |
| `consultas-al-mandante.md` | Espejo de la planilla anterior, para poder buscarla sin abrir Excel | Versado |
| `Objetivos_Proyecto.docx` | Informe de presentación de objetivos del proyecto | Versado |
| `catalogo_servicios_candidatos_11.md` | Análisis preliminar de 10 fronteras C y puente hacia las 12 fronteras R/F consolidadas; incluye criterios para decidir módulos, servicios y microservicios. El nombre del archivo se conserva por estabilidad de enlaces. | En revisión |
| `escenarios_flujos_actores.md` | Candidatos de procesos con interacción entre actores y recomendación para diagramar un flujo simple. | En revisión |
| `analisis_catalogo_capacidades_servicios_y_actores.md` | Análisis preliminar, conservado como antecedente del catálogo consolidado | Supersedido |
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
| Informe interno | `Objetivos_Proyecto.docx` |
