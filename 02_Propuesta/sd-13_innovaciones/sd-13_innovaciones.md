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
actualizado: 2026-09-29
---
# Subdocumento 13 — Innovaciones

> Maestro del subdocumento. Cada sección se redacta en su propio archivo `sd-13_sN_*.md` dentro de esta carpeta; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

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

## Secciones

| N | Sección | Archivo | Estado |
| :--- | :--- | :--- | :--- |
| 1 | Criterio de selección de la cartera | `sd-13_s1_criterio-de-seleccion-de-la-cartera.md` | Sin redactar |
| 2 | Ficha de innovación | `sd-13_s2_ficha-de-innovacion.md` | Sin redactar |
| 3 | Trazabilidad de la cartera | `sd-13_s3_trazabilidad-de-la-cartera.md` | Sin redactar |
| 4 | Declaración de investigación pendiente | `sd-13_s4_declaracion-de-investigacion-pendiente.md` | Sin redactar |

### Notas por sección

- **2. Ficha de innovación** - El índice del Informe 1 prevé cinco fichas (6.2 a 6.6), una por cada tipo del Art. 28.º: producto, proceso, arquitectura o tecnología, modelo de negocio y UX o sostenibilidad. El cuerpo actual solo tiene el encabezado 6.2.
- **3. Trazabilidad de la cartera** - Cada innovación debe trazarse con la arquitectura, la EDT y el flujo de caja.
- **4. Declaración de investigación pendiente** - Las innovaciones de base tecnológica exigen fuentes citadas en norma APA 7.ª edición (Art. 29.º).

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

- [ ] Cada sección tiene su archivo `sd-13_sN_*.md` con contenido redactado
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Cinco innovaciones, una por cada tipo del Art. 28.º, con los siete elementos del Art. 29.º
- [ ] Cada innovación trazable con la arquitectura, la EDT y el flujo de caja
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
