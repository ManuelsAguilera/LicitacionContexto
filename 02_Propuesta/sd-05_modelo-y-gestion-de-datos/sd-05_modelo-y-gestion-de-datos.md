---
id: T7-05
tipo: parte
parte: T7-05
titulo: Modelo y gestión de datos
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-013
  - ADJ-014
jira:
  - OSS-100
  - OSS-101
  - OSS-171
  - OSS-249
  - OSS-97
  - OSS-98
  - OSS-99
cifras: []
secciones:
  - T7-05-5.1
  - T7-05-5.2
  - T7-05-5.3
  - T7-05-5.4
actualizado: 2026-10-06
---
# Subdocumento 5 — Modelo y gestión de datos

> Maestro del subdocumento. Registra la estructura obligatoria del Comunicado 10, el estado y la trazabilidad. El contenido se redacta en `02_Propuesta/latex_final/sd-05.tex`; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 5 de 14 |
| Título oficial (T-7) | Modelo y gestión de datos |
| Carpeta | `02_Propuesta/sd-05_modelo-y-gestion-de-datos/` |
| Capítulo en el informe | Capítulo V |
| Formularios asociados | ninguno |
| Estado | Sin redactar |

## Ponderación (Formulario T-21)

Ítem en el T-21: Modelo y gestión de datos

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
| 5.1 | Modelo | Dominios de información y modelo de datos por dominio, en figuras legibles. El diccionario de datos va en anexos. | Sin redactar |
| 5.2 | Gestión de datos | Selección del motor y del paradigma de persistencia con justificación (relacional o no relacional, transaccionalidad, consistencia y disponibilidad según el teorema CAP); separación transaccional y analítico y modelo de explotación; calidad de datos, retención, archivado y eliminación segura. | Sin redactar |
| 5.3 | Estrategia de migración | Migración, saneamiento, validación y conciliación de los datos históricos, con volumen y ventanas de corte compatibles con el cronograma. | Sin redactar |
| 5.4 | Estrategia de desempeño | Indexación, particionamiento, caché y optimización de consultas, fundados en la volumetría del caso. | Sin redactar |

La redacción vive en `02_Propuesta/latex_final/sd-05.tex` (edición colaborativa en Prism); este maestro solo registra estructura, estado y trazabilidad.

## Trazabilidad con Jira

Agrupadora: **OSS-171**.

La estructura de trabajo vive en el proyecto `OSS` y **no es el índice del informe**: los nombres de sección del plan son maestros y no coinciden uno a uno con las secciones de este subdocumento.

| Clave | Sección en el plan de Jira | Subtareas |
| :--- | :--- | :--- |
| OSS-97 | 5. Introducción | 1 |
| OSS-98 | 5.1 Modelo | 3 |
| OSS-99 | 5.2 Gestión de datos | 3 |
| OSS-100 | 5.3 Estrategia de migración | 5 |
| OSS-101 | 5.4 Estrategia de desempeño | 2 |

## Adjuntos esperados

- `diag-05-01_modelo-datos.svg`
- `diag-05-02_frontera-datos-retail-financiero.svg`

## Checklist de llenado

- [ ] Cada título del Comunicado 10 está desarrollado en `sd-05.tex`, sin omitir ni mover contenido a otro título
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] La frontera entre el negocio retail y la filial emisora fiscalizada queda definida antes que cualquier vista unificada
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
