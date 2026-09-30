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
  - T7-08-8.4
  - T7-08-8.5
actualizado: 2026-09-29
---
# Subdocumento 8 — Plan de riesgos

> Maestro del subdocumento. Cada sección se redacta en su propio archivo `sd-08_sN_*.md` dentro de esta carpeta; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 8 de 14 |
| Título oficial (T-7) | Plan de riesgos |
| Carpeta | `02_Propuesta/sd-08_plan-de-riesgos/` |
| Capítulo en el informe | No cubierto todavía; se redactará en el Informe 2 o 3 |
| Formularios asociados | T-16 |
| Estado | Sin redactar |

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

## Secciones

| N | Sección | Archivo | Estado |
| :--- | :--- | :--- | :--- |
| 1 | Identificación y cuantificación de riesgos técnicos, organizacionales, de proyecto, de seguridad y de operación | `sd-08_s1_identificacion-y-cuantificacion-de-riesgos-tecnicos-organi.md` | Sin redactar |
| 2 | Análisis cualitativo y cuantitativo, con técnicas de análisis de modos de falla, árbol de fallas o simulación | `sd-08_s2_analisis-cualitativo-y-cuantitativo-con-tecnicas-de-analis.md` | Sin redactar |
| 3 | Estrategias de mitigación basadas en análisis costo-beneficio, con responsable, plazo y disparador | `sd-08_s3_estrategias-de-mitigacion-basadas-en-analisis-costo-benefi.md` | Sin redactar |
| 4 | Riesgos de obsolescencia tecnológica, bloqueo por proveedor, escalabilidad, ciberseguridad y disponibilidad de contrapartes del CLIENTE | `sd-08_s4_riesgos-de-obsolescencia-tecnologica-bloqueo-por-proveedor.md` | Sin redactar |
| 5 | Reservas de contingencia y de gestión, y su reflejo en el cronograma y en el flujo de caja | `sd-08_s5_reservas-de-contingencia-y-de-gestion-y-su-reflejo-en-el-c.md` | Sin redactar |

### Notas por sección

- **4. Riesgos de obsolescencia tecnológica, bloqueo por proveedor, escalabilidad, ciberseguridad y disponibilidad de contrapartes del CLIENTE** - El soporte del proveedor de la plataforma de crédito (en operación desde 2011) termina en 2029, dentro del período de Operación: es riesgo de calendario, no solo técnico.

## Adjuntos esperados

- `form-T-16_plan-de-riesgos.docx`

## Checklist de llenado

- [ ] Cada sección tiene su archivo `sd-08_sN_*.md` con contenido redactado
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
