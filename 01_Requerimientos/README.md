# Requerimientos

Catálogos de requerimientos del caso 09, en Excel como fuente de verdad y con un espejo en Markdown
para poder buscarlos sin abrir Excel.

## Fuente oficial

| Archivo | Qué es |
| :--- | :--- |
| `RequerimientosAtomizados_Depuracion_Alcance.xlsx` | **Catálogo v3.0 depurado y renumerado**: `RF-001`..`RF-226`, `RNF-01`..`RNF-76`, `OP-01`..`OP-09`. Hojas `6_Equivalencia_IDs` (mapeo de IDs viejos a nuevos) y `7_Depuracion_Alcance` (decisiones ELIMINAR / TRASLADAR / CONSOLIDAR / RECLASIFICAR / CONDICIONAR / REVISAR) |
| `RequerimientosAtomizados_Depuracion_Alcance_v3.1.xlsx` | **Catálogo v3.1 conciliado con el alcance del sd-03** (2026-10-08, borrador por revisar): 308 requerimientos vigentes (227 RF, 72 RNF, 9 OP) con servicio, etapa, prioridad y ámbito; decisiones de depuración, reasignaciones, resumen por fórmula, registro de reglas de negocio y pendientes. Es la fuente del Anexo B del Subdocumento 3. No reemplaza a la v3.0, que se conserva sin cambios hasta que el equipo decida |

## Histórico

| Archivo | Qué es |
| :--- | :--- |
| `RequerimientosAtomizados.xlsx` | Catálogo v2.1 previo a la depuración. Sus IDs se mapean con la hoja `6_Equivalencia_IDs` del v3.0 |
| `RequerimientosHumanos.xlsx` | Análisis original de personas: el insumo del catálogo, no el catálogo |

## Espejos en Markdown

Generados desde los `.xlsx` para lectura por agentes, por búsqueda y por el MCP `ragdocs`.

| Espejo | Origen |
| :--- | :--- |
| `md/catalogo-de-requerimientos-depurado-v30.md` | Catálogo v3.0 (7 hojas) |
| `historico/md/catalogo-de-requerimientos-atomizados-v21-historico.md` | v2.1 (5 hojas) |
| `historico/md/analisis-de-requerimientos-humanos-origen.md` | Análisis humano (7 hojas) |

**Regla:** si el `.md` y el Excel difieren, **manda el Excel**. Los espejos se regeneran; no se
editan a mano. Están truncados a 400 filas por hoja: para el juego completo, abrir el `.xlsx`.

## Uso

- Los **RT-CC.NN** de `00_Bases/Bases_Transversales.md` se responden uno a uno en el **Formulario T-12**
  (`03_Formularios/B/`), no en este catálogo.
- El catálogo v3.0 alimenta la sección 3.8 y 3.9 del subdocumento 3
  (`02_Propuesta/sd-03_esquema-de-solucion-y-alcance/`).
- El caso puede **endurecer** un requisito transversal, nunca rebajarlo. Un "Según caso" se completa
  con la volumetría del documento del caso; si el caso no lo define, rige el valor por defecto del
  transversal.
