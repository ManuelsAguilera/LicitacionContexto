# Adjuntos de la propuesta

Material de apoyo que se cita desde `02_Propuesta/` pero que no es texto redactado: exportaciones de
diagramas, inventarios de hardware y tablas de cálculo.

## Carpetas

| Carpeta | Contenido | Origen |
| :--- | :--- | :--- |
| `diagramas/` | Fuente editable (`.py`, `.drawio`, `.dot`) y exportación (`.png`, `.pdf`) de cada diagrama, todo en la misma carpeta, sin subcarpetas | La **fuente** es el `.py`/`.drawio`/`.dot` que está junto a la exportación |
| `hardware/` | Inventario de hardware y software a proveer (4.2 c) | Exigido en Excel por las Bases |
| `tablas/` | Tablas de cálculo de apoyo (dimensionamiento, boxed de caja) | Derivadas de `00_Bases/` |

## Convención de nombres

| Tipo | Patrón | Ejemplo |
| :--- | :--- | :--- |
| Diagrama exportado | `diag-NN-SN_titulo.<ext>` | `diag-04-02_arquitectura-fisica.svg` |
| Inventario | `sd-NN_sN_titulo.<ext>` | `sd-04_s2_inventario-hardware.xlsx` |

## Regla de fuente única

El diagrama se escribe **una sola vez**, como `.py` (librería `diagrams`), `.drawio`, `.dot` o
`.puml`, junto a su exportación en `diagramas/`. No se usa Mermaid (el importador LaTeX lo rechaza). El
archivo exportado es un derivado: si cambia la fuente, hay que regenerarlo. La copia que consume el
`.tex` vive en `02_Propuesta/latex_final/figuras/`.

Ver "Renderizado de diagramas" en `AGENTS.md` para las herramientas de exportación.
