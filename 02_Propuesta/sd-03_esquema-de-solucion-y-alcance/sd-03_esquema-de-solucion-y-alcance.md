---
id: T7-03
tipo: parte
parte: T7-03
titulo: Esquema de solución y alcance
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-006
  - ADJ-007
jira:
  - OSS-167
  - OSS-241
  - OSS-244
  - OSS-245
  - OSS-84
  - OSS-85
  - OSS-86
  - OSS-87
  - OSS-88
cifras: []
secciones:
  - T7-03-3.1
  - T7-03-3.2
  - T7-03-3.3
  - T7-03-3.4
actualizado: 2026-09-30
---
# Subdocumento 3 — Esquema de solución y alcance

> Maestro del subdocumento. Cada sección se redacta en su propio archivo `sd-03_sN_*.md` dentro de esta carpeta; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 3 de 14 |
| Título oficial (T-7) | Esquema de solución y alcance |
| Carpeta | `02_Propuesta/sd-03_esquema-de-solucion-y-alcance/` |
| Capítulo en el informe | Capítulo III |
| Formularios asociados | T-12 |
| Estado | Desarrollado en el Informe 1 |

## Ponderación (Formulario T-21)

Ítem en el T-21: Esquema de solución y alcance

| Puntaje | Cumplimiento | Formalidad |
| :--- | :--- | :--- |
| _pendiente_ | _pendiente_ | _pendiente_ |

> **Pendiente de verificación.** La tabla de ponderación del Formulario T-21 en
> `00_Bases/Bases_Administrativas.md` (línea 2366) está incompleta: la lectura no permite
> reconstruir los porcentajes por ítem ni la fila del Plan de Riesgos, y el encabezado de la tabla
> de correspondencia *sección / subdocumento T-7 / ponderación T-21* del Informe 1 es un marcador
> de posición sin contenido. **No hardcodear cifras acá**: dejarlas en blanco hasta que se reparen
> las tablas de las Bases.

## Contenido exigido por el T-7

- Descripción de la solución propuesta y su coherencia con el problema definido.
- Alcance de la Etapa 1 y de la Etapa 2, con separación explícita y criterios de asignación entre ambas.
- Exclusiones explícitas, supuestos y restricciones del alcance.
- Catálogo de requerimientos funcionales y no funcionales, priorizado y trazable.
- Estrategia para obtener el apoyo de los grupos de interés clave.
- Criterios de aceptación del alcance comprometido.

## Secciones

| N | Sección | Archivo | Estado |
| :--- | :--- | :--- | :--- |
| 1 | Resumen Ejecutivo de la Solución | `sd-03_s1_resumen-ejecutivo-de-la-solucion.md` | Borrador migrado; revisar |
| 2 | Alcance | `sd-03_s2_alcance.md` | Borrador migrado; revisar |
| 3 | Esquema de solución | `sd-03_s3_esquema-de-solucion.md` | Borrador migrado; revisar |
| 4 | Explicación de la Solución | `sd-03_s4_explicacion-de-la-solucion.md` | Borrador migrado; revisar |

### Nota de migración

La estructura entregable sigue las cuatro secciones obligatorias del Comunicado 10. El contenido importado conserva su procedencia y permanece en estado borrador hasta revisión humana.

## Trazabilidad con Jira

Agrupadora: **OSS-167**.

La estructura de trabajo vive en el proyecto `OSS` y **no es el índice del informe**: los nombres de sección del plan son maestros y no coinciden uno a uno con las secciones de este subdocumento.

| Clave | Sección en el plan de Jira | Subtareas |
| :--- | :--- | :--- |
| OSS-84 | 3. Introducción | 2 |
| OSS-85 | 3.1 Resumen Ejecutivo de la Solución | 1 |
| OSS-86 | 3.2 Alcance | 14 |
| OSS-87 | 3.3 Esquema de solución | 5 |
| OSS-88 | 3.4 Explicación de la Solución | 1 |

## Adjuntos esperados

- `form-T-12_matriz-cumplimiento-tecnico.xlsx : formulario oficial, se responde cada RT uno a uno`
- `diag-03-01_esquema-conceptual-solucion.svg`

## Checklist de llenado

- [ ] Cada sección tiene su archivo `sd-03_sN_*.md` con contenido redactado
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] La frontera entre el negocio retail y la filial emisora fiscalizada queda definida antes que cualquier vista unificada
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
