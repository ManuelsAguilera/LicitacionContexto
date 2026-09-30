---
id: T7-02
tipo: parte
parte: T7-02
titulo: "Resumen Ejecutivo, comprensión del problema y de la necesidad"
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-004
  - ADJ-005
jira:
  - OSS-166
  - OSS-78
  - OSS-79
  - OSS-80
  - OSS-81
  - OSS-82
  - OSS-83
cifras: []
secciones:
  - T7-02-2.1
  - T7-02-2.2
  - T7-02-2.3
  - T7-02-2.4
  - T7-02-2.5
  - T7-02-2.6
  - T7-02-2.7
actualizado: 2026-09-29
---
# Subdocumento 2 — Resumen Ejecutivo, comprensión del problema y de la necesidad

> Maestro del subdocumento. Cada sección se redacta en su propio archivo `sd-02_sN_*.md` dentro de esta carpeta; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 2 de 14 |
| Título oficial (T-7) | Resumen Ejecutivo, comprensión del problema y de la necesidad |
| Carpeta | `02_Propuesta/sd-02_problema-y-necesidad/` |
| Capítulo en el informe | Capítulo II |
| Formularios asociados | ninguno |
| Estado | Desarrollado en el Informe 1 |

## Ponderación (Formulario T-21)

Ítem en el T-21: Resumen Ejecutivo, comprensión del problema y de la necesidad

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

- Dimensionamiento realista de la magnitud del problema o desafío, con foco cualitativo y con datos cuantitativos que lo sustenten.
- Comprensión del contexto de la industria, de sus particularidades operacionales, regulatorias y estacionales.
- Identificación de los actores afectados y de los grupos de interés, con su nivel de influencia e interés.
- Supuestos declarados y su fundamento. No mezclar el problema con la solución.
- Información de apoyo referenciada en norma APA 7.ª edición.

## Secciones

| N | Sección | Archivo | Estado |
| :--- | :--- | :--- | :--- |
| 1 | Resumen ejecutivo | `sd-02_s1_resumen-ejecutivo.md` | Desarrollado en el Informe 1 |
| 2 | Contexto de la industria y de la compañía | `sd-02_s2_contexto-de-la-industria-y-de-la-compania.md` | Desarrollado en el Informe 1 |
| 3 | La particularidad estructural: dos negocios, un mostrador | `sd-02_s3_la-particularidad-estructural-dos-negocios-un-mostrador.md` | Desarrollado en el Informe 1 |
| 4 | Dimensionamiento del problema por dominio | `sd-02_s4_dimensionamiento-del-problema-por-dominio.md` | Desarrollado en el Informe 1 |
| 5 | Mapa de actores y grupos de interés | `sd-02_s5_mapa-de-actores-y-grupos-de-interes.md` | Sin redactar |
| 6 | Supuestos declarados del análisis | `sd-02_s6_supuestos-declarados-del-analisis.md` | Sin redactar |
| 7 | Síntesis del problema central | `sd-02_s7_sintesis-del-problema-central.md` | Desarrollado en el Informe 1 |

### Notas por sección

- **1. Resumen ejecutivo** - Con 2.1.1 por qué licita, 2.1.2 las cuatro promesas diarias, 2.1.3 doble naturaleza jurídica, 2.1.4 el encargo y sus límites y 2.1.5 lo que se evalúa.
- **3. La particularidad estructural: dos negocios, un mostrador** - La línea roja del directorio: la frontera retail / filial emisora debe quedar resuelta antes que cualquier vista unificada de cliente.
- **4. Dimensionamiento del problema por dominio** - Siete dominios (2.4.1 a 2.4.7), cada uno con su dato y el capítulo fuente de las Bases Técnicas. Cada cifra debe derivar de las Bases o de un cálculo mostrado.
- **6. Supuestos declarados del análisis** - Debe consolidar los supuestos SUP-01 a SUP-25 que el caso deja sin resolver (numeral 16.1).

## Trazabilidad con Jira

Agrupadora: **OSS-166**.

La estructura de trabajo vive en el proyecto `OSS` y **no es el índice del informe**: los nombres de sección del plan son maestros y no coinciden uno a uno con las secciones de este subdocumento.

| Clave | Sección en el plan de Jira | Subtareas |
| :--- | :--- | :--- |
| OSS-78 | 2. Introducción | 1 |
| OSS-79 | 2.1 Resumen Ejecutivo del problema | 1 |
| OSS-80 | 2.2 Comprensión del problema y de la necesidad | 1 |
| OSS-81 | 2.3 Dimensionamiento del problema | 1 |
| OSS-82 | 2.4 Actores y Grupos de Interés | 1 |
| OSS-83 | 2.5 Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones | 2 |

## Adjuntos esperados

- `adj-sd-02_s4_dimensionamiento.xlsx : memoria de cálculo (anexo A.2 del Informe 1)`
- `adj-sd-02_s4_referencias-APA7.md : referencias bibliográficas del subdocumento`

## Checklist de llenado

- [ ] Cada sección tiene su archivo `sd-02_sN_*.md` con contenido redactado
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] No se mezclan el problema y la solución (T-7, subdocumento 2)
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
