# Adjuntos de la propuesta

Material de apoyo que se cita desde `02_Propuesta/` pero que no es texto redactado: exportaciones de
diagramas, inventarios de hardware y tablas de cálculo.

## Carpetas

| Carpeta | Contenido | Origen |
| :--- | :--- | :--- |
| `diagramas/` | Exportaciones PNG/SVG/PDF de los diagramas | La **fuente** de cada diagrama vive en el `.md` de la sección que lo usa |
| `hardware/` | Inventario de hardware y software a proveer (4.2 c) | Exigido en Excel por las Bases |
| `tablas/` | Tablas de cálculo de apoyo (dimensionamiento, boxed de caja) | Derivadas de `00_Bases/` |

## Convención de nombres

| Tipo | Patrón | Ejemplo |
| :--- | :--- | :--- |
| Diagrama exportado | `diag-NN-SN_titulo.<ext>` | `diag-04-02_arquitectura-fisica.svg` |
| Inventario | `sd-NN_sN_titulo.<ext>` | `sd-04_s2_inventario-hardware.xlsx` |

## Regla de fuente única

El diagrama se escribe **una sola vez**, como bloque Mermaid o como `.puml` dentro del `.md` de la
sección. El archivo exportado es un derivado: si cambia el texto, hay que regenerar el export.
GitHub renderiza los bloques Mermaid de forma nativa, así que la vista de revisión no necesita el PNG.

Ver "Renderizado de diagramas" en `AGENTS.md` para las herramientas de exportación.
