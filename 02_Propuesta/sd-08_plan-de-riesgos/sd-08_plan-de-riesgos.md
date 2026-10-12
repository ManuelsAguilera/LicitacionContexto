---
id: T7-08
tipo: parte
parte: T7-08
titulo: Plan de riesgos
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-021
jira: []
cifras: []
secciones:
  - T7-08-8.1
  - T7-08-8.2
  - T7-08-8.3
actualizado: 2026-10-12
---
# Subdocumento 8 — Plan de riesgos

> Maestro del subdocumento. Registra la estructura obligatoria del Comunicado 10, el estado y la trazabilidad. Las fuentes editables son `02_Propuesta/latex_final/sd-08/OSS-Subdocumento8.tex` y `02_Propuesta/latex_final/sd-08/OSS-Formulario-T-16.tex`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 8 de 14 |
| Título oficial (T-7) | Plan de riesgos |
| Carpeta | `02_Propuesta/sd-08_plan-de-riesgos/` |
| Capítulo en el informe | Informe 2 |
| Formularios asociados | T-16 |
| Estado | Borrador redactado con asistencia de IA, sin revisión humana (2026-10-12) |

## Ponderación (Formulario T-21)

Ítem en el T-21: Plan de riesgos

| Puntaje | Cumplimiento | Formalidad |
| :--- | :--- | :--- |
| _pendiente_ | _pendiente_ | _pendiente_ |

> **Pendiente de verificación.** La tabla de ponderación del Formulario T-21 en
> `00_Bases/Bases_Administrativas.md` (línea 2366) está incompleta: la lectura no permite
> reconstruir los porcentajes por ítem ni la fila del Plan de Riesgos, y el encabezado de la tabla
> de correspondencia *sección / subdocumento T-7 / ponderación T-21* del Informe 1 es un marcador
> de posición sin contenido. **No hardcodear cifras acá**: dejarlas en blanco hasta que se reparen
> las tablas de las Bases.

## Estructura obligatoria (Comunicado 10)

Fuente: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md`. Los títulos se reproducen tal cual. Cada título se desarrolla en el apartado indicado y no en otro.

Cada capítulo abre con un texto de introducción: resumen del capítulo y su conexión con los demás capítulos, anexos y formularios.

En todo el capítulo: los riesgos corresponden a la solución efectivamente propuesta, no a un catálogo genérico.

| N | Título oficial | Contenido que debe desarrollar | Estado |
| :--- | :--- | :--- | :--- |
| 8.1 | Plan de riesgos | Enfoque de gestión, roles, escalas de probabilidad e impacto y ciclo de revisión. | Borrador, sin revisión humana |
| 8.2 | Identificación y Análisis de Riesgos | RBS y cuantificación de riesgos técnicos, organizacionales, de proyecto, de seguridad y de operación; en particular obsolescencia tecnológica, bloqueo por proveedor, escalabilidad, ciberseguridad y disponibilidad de contrapartes del CLIENTE; análisis cualitativo y cuantitativo (modos de falla, árbol de fallas o simulación). | Borrador, sin revisión humana |
| 8.3 | Plan de Acción a Riesgos | Mitigación basada en análisis costo-beneficio, con responsable, plazo y disparador; reservas de contingencia y de gestión y su reflejo en el cronograma (valorización en la Oferta Económica, Art. 50.2). | Borrador, sin revisión humana |

Formulario asociado: T-16, en una fuente LaTeX separada del subdocumento.

La redacción vive en `02_Propuesta/latex_final/sd-08/OSS-Subdocumento8.tex` (edición colaborativa en Prism); este maestro solo registra estructura, estado y trazabilidad.

## Adjuntos esperados

- `02_Propuesta/latex_final/sd-08/OSS-Formulario-T-16.tex` (ADJ-021; fuente editable, pendiente de revisión humana y PDF de entrega)

## Checklist de llenado

- [x] Cada título del Comunicado 10 está desarrollado en `sd-08/OSS-Subdocumento8.tex`, pendiente de revisión humana
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [x] El registro del Formulario T-16 tiene fuente editable separada en `latex_final/sd-08/`; pendiente de revisión humana y PDF de entrega
- [x] Las figuras del capítulo tienen fuente editable y exportaciones en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
