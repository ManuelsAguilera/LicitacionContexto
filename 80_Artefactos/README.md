# Artefactos generales del proyecto

Material de trabajo del equipo que no pertenece a una etapa del pipeline de la propuesta: planilla de
consultas, auditorías, rúbricas de revisión y el contexto de trabajo de cada subdocumento
(`sd-NN_contexto/`). Nada de aquí es texto entregable.

**Entrada habitual:** [contexto activo](contexto-activo/indice.md) y [matriz de ajustes](contexto-activo/matriz-ajustes.md). SD-04 es referencia de arquitectura y SD-07 de planificación. Las notas por fecha son antecedentes o pendientes hasta cotejarlas con esas fuentes; no cargar recursivamente todos los artefactos. La trazabilidad de traslados y validaciones se conserva en el [registro técnico de limpieza](../05_Gestion/reportes/limpieza-contexto-2026-10-25.md), de consulta puntual.

| Artefacto | Qué es | Estado |
| :--- | :--- | :--- |
| `CONSULTAS_ONLYSIMPLESOLUTIONS_20260901.xlsx` | Planilla de consultas al mandante con la nomenclatura del Art. 43.3 | Versada |
| `consultas-al-mandante.md` | Espejo de la planilla anterior, para poder buscarla sin abrir Excel | Versado |
| `archivo-contexto/2026-10-25/seccion3_innovaciones.md` | Material de apoyo sobre innovaciones (conservado para el capítulo 13) | Antecedente |
| `sd-01_contexto/` | Notas para el sd-01: hechos sobre la empresa que salieron de otros trabajos y deben reflejarse en la presentación | Borrador |
| `sd-03_contexto/` | Contexto de trabajo del sd-03: plan de 3.2, análisis de actores y servicios, descripción del alcance del producto y entregables (borradores) | Borrador |
| `sd-xx [TODOS]/` | Auditorías que cruzan varios subdocumentos. Hoy: `auditoria_inconsistencias_sd01-04.md` (inconsistencias internas y externas de los sd-01 a sd-04, por gravedad) `auditoria_inconsistencias_sd05-13.md` (lo mismo para los sd-05 a sd-13) y `revision_formularios.md` (revisión de los formularios T-6 a T-22 contra las Bases y los subdocumentos) y `glosario_nombres_comunes.md` (nombres idénticos entre subdocumentos) | Borrador |
| `sd-04_contexto/`, `sd-07_contexto/`, `sd-08_contexto/`, `sd-13_contexto/` | Contexto de trabajo por subdocumento: informes de revisión, estimación y EDT (sd-07), trazabilidad de riesgos (sd-08), candidatas de innovación (sd-13) | Borrador |
| `recursos/` | Imágenes de apoyo (esquema de solución) | Antecedente |
| `revision_informe_1_transcripcion.md` | Transcripción por página del PDF de retroalimentación del Informe 1; conserva la procedencia y el hash del origen | Fuente de revisión |
| `revision_informe_1_rubrica_de_cierre.pdf` | PDF de la rúbrica anterior, para lectura | Antecedente |
| `revision_informe_1_rubrica_de_cierre.md` | Informe que transforma esa retroalimentación en criterios de cierre por subsección del Comunicado 10 | Contexto prioritario para el siguiente ciclo |
| [`sd-04_contexto/explicacion-diagrama-columnas-2026-10-23/README.md`](sd-04_contexto/explicacion-diagrama-columnas-2026-10-23/README.md) | Explicación del nuevo diagrama lógico aportado el 23-10-2026; conserva imagen, propósito, conexiones, alojamiento, fundamentos y pendientes por componente | Borrador de contexto |
| [`sd-04_contexto/fisica-general-zonas-2026-10-23/README.md`](sd-04_contexto/fisica-general-zonas-2026-10-23/README.md) | Vista física general por zonas, con iconos sin tarjetas, AKS, balanceadores y seguridad; registra Chile Central en producción y Brazil South en recuperación de ambos ámbitos | Borrador de contexto |
| [`sd-04_contexto/inventario-fisico-integral-2026-10-23.md`](sd-04_contexto/inventario-fisico-integral-2026-10-23.md) | Inventario previo al rediseño: sitios, zonas, nodos, VM, contenedores, PaaS, equipos locales, recuperación y 45 conexiones; separa decisiones de cantidades pendientes | Borrador de diseño |
| [`sd-04_contexto/plan-cierre-inventario-fisico-2026-10-23.md`](sd-04_contexto/plan-cierre-inventario-fisico-2026-10-23.md) | Plan de ocho encargos por agentes para cerrar dimensionamiento, tienda con pares por negocio, custodia en DC, recuperación y rediseño del diagrama | Plan de ejecución |

| [`sd-04_contexto/cierre-inventario/README.md`](sd-04_contexto/cierre-inventario/README.md) | Ocho fichas ejecutadas, revisión cruzada y figura 4.52; cuatro hosts por tienda y X-01 local aislado | Diseño para revisión |

## Reglas

- Son documentos de **lectura para el equipo**, no fuentes de la propuesta: por eso conservan su
  formato original. Cuando su contenido deba alimentar un subdocumento ya importado, se propone el cambio en su `.tex` vigente con referencia al origen. Para partes sin LaTeX, el borrador se conserva en Markdown. No sustituir una fuente importada por una copia histórica.
- El espejo en `.md` de la planilla de consultas se genera desde el `.xlsx`: si el `.md` y el Excel
  difieren, **manda el Excel**.
- La rúbrica de revisión es una lista interna de comprobación: sus observaciones se contrastan
  con las Bases y con la versión actual de cada subdocumento antes de dar una sección por cerrada.

## Nomenclatura

| Tipo | Patrón |
| :--- | :--- |
| Consulta al mandante | `CONSULTAS_ONLYSIMPLESOLUTIONS_AAAAMMDD.xlsx` |
