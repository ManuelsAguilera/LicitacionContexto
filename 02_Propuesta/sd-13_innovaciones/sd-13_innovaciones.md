---
id: T7-13
tipo: parte
parte: T7-13
titulo: Innovaciones
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-025
  - ADJ-026
jira:
  - OSS-102
  - OSS-103
  - OSS-104
  - OSS-172
cifras: []
secciones:
  - T7-13-13.1
  - T7-13-13.2
  - T7-13-13.3
  - T7-13-13.4
  - T7-13-13.5
actualizado: 2026-10-06
---
# Subdocumento 13 — Innovaciones

> Maestro del subdocumento. Registra la estructura obligatoria del Comunicado 10, el estado y la trazabilidad. El contenido se redacta en `02_Propuesta/latex_final/sd-13.tex`; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 13 de 14 |
| Título oficial (T-7) | Innovaciones |
| Carpeta | `02_Propuesta/sd-13_innovaciones/` |
| Capítulo en el informe | Capítulo VI |
| Formularios asociados | T-19 |
| Estado | Sin redactar |

## Ponderación (Formulario T-21)

Ítem en el T-21: Innovaciones

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

Cada innovación desarrolla los siete elementos del Art. 29.º (problema, tecnología, madurez, diseño de incorporación, impacto económico, indicador de verificación y riesgo de adopción) y su trazabilidad con la arquitectura, la EDT y el flujo de caja. Las de base tecnológica citan fuentes en APA 7.ª. El título se mantiene tal cual («13.1 Innovación 1»); el primer párrafo declara el tipo y el nombre (sección 10 del Comunicado 10).

| N | Título oficial | Contenido que debe desarrollar | Estado |
| :--- | :--- | :--- | :--- |
| 13.1 | Innovación 1 | Tipo: producto o servicio. | Sin redactar |
| 13.2 | Innovación 2 | Tipo: proceso. | Sin redactar |
| 13.3 | Innovación 3 | Tipo: tecnológica o de arquitectura. | Sin redactar |
| 13.4 | Innovación 4 | Tipo: modelo de negocio o de contratación. | Sin redactar |
| 13.5 | Innovación 5 | Tipo: experiencia de usuario, sostenibilidad o impacto social. | Sin redactar |

Anexos: Formulario T-19.

La redacción vive en `02_Propuesta/latex_final/sd-13.tex` (edición colaborativa en Prism); este maestro solo registra estructura, estado y trazabilidad.

## Trazabilidad con Jira

Agrupadora: **OSS-172**.

La estructura de trabajo vive en el proyecto `OSS` y **no es el índice del informe**: los nombres de sección del plan son maestros y no coinciden uno a uno con las secciones de este subdocumento.

| Clave | Sección en el plan de Jira | Subtareas |
| :--- | :--- | :--- |
| OSS-102 | 13. Introducción | 1 |
| OSS-103 | 13.3 Innovación 3 - Tecnológica o de arquitectura | 3 |
| OSS-104 | 13.4 Innovación 4 - Modelo de negocio o de contratación | 1 |

## Adjuntos esperados

- `form-T-19_cartera-innovaciones.docx`
- `adj-sd-13_s2_referencias-APA7.md`

## Checklist de llenado

- [ ] Cada título del Comunicado 10 está desarrollado en `sd-13.tex`, sin omitir ni mover contenido a otro título
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Cinco innovaciones, una por cada tipo del Art. 28.º, con los siete elementos del Art. 29.º
- [ ] Cada innovación trazable con la arquitectura, la EDT y el flujo de caja
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
