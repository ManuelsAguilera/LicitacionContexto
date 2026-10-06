---
id: T7-06
tipo: parte
parte: T7-06
titulo: Metodologías
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-015
  - ADJ-016
jira: []
cifras: []
secciones:
  - T7-06-6.1
  - T7-06-6.2
actualizado: 2026-10-06
---
# Subdocumento 6 — Metodologías

> Maestro del subdocumento. Registra la estructura obligatoria del Comunicado 10, el estado y la trazabilidad. El contenido se redacta en `02_Propuesta/latex_final/sd-06.tex`; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 6 de 14 |
| Título oficial (T-7) | Metodologías |
| Carpeta | `02_Propuesta/sd-06_metodologias/` |
| Capítulo en el informe | No cubierto todavía; se redactará en el Informe 2 o 3 |
| Formularios asociados | T-9, T-10 |
| Estado | Sin redactar |

## Ponderación (Formulario T-21)

Ítem en el T-21: 6 a) Metodología de Gestión de Proyectos / b) Metodología de Desarrollo Software

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

| N | Título oficial | Contenido que debe desarrollar | Estado |
| :--- | :--- | :--- | :--- |
| 6.1 | Metodología de Gestión de Proyectos | PMBOK adaptado a la complejidad del proyecto, con enfoques ágiles donde corresponda. Gestión de interesados, comunicaciones, adquisiciones e integración. Mecanismos de decisión y cadencias de gobierno. Anexo: Formulario T-9. | Sin redactar |
| 6.2 | Metodología de Desarrollo Software | Enfoque coherente con la naturaleza del proyecto (requerimientos, arquitectura evolutiva, refactorización, deuda técnica, tiempo de salida al mercado); DevSecOps, integración y entrega continuas, infraestructura como código, automatización de pruebas; ceremonias, artefactos, cadencias y decisión del desarrollo. Anexo: Formulario T-10. | Sin redactar |

Anexos: Formulario T-9 (6.1); Formulario T-10 (6.2).

La redacción vive en `02_Propuesta/latex_final/sd-06.tex` (edición colaborativa en Prism); este maestro solo registra estructura, estado y trazabilidad.

## Adjuntos esperados

- `form-T-9_metodologia-gestion-proyectos.docx`
- `form-T-10_metodologia-desarrollo.docx`

## Checklist de llenado

- [ ] Cada título del Comunicado 10 está desarrollado en `sd-06.tex`, sin omitir ni mover contenido a otro título
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
