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
actualizado: 2026-10-08
---
# Subdocumento 3 — Esquema de solución y alcance

> Maestro del subdocumento. Registra la estructura obligatoria del Comunicado 10, el estado y la trazabilidad. El contenido se redacta en `02_Propuesta/latex_final/sd-03.tex`; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

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

## Estructura obligatoria (Comunicado 10)

Fuente: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md`. Los títulos se reproducen tal cual. Cada título se desarrolla en el apartado indicado y no en otro.

Cada capítulo abre con un texto de introducción: resumen del capítulo y su conexión con los demás capítulos, anexos y formularios.

| N | Título oficial | Contenido que debe desarrollar | Estado |
| :--- | :--- | :--- | :--- |
| 3.1 | Resumen Ejecutivo de la Solución | Todo el alcance del proyecto: implementación (Etapa 1 y Etapa 2), implantación (marchas blancas y pasos a producción) y operación (36 meses). | Redactada (versión compacta en `sd-03.tex`, 2026-10-07; faltan las dos figuras marcadas y la revisión humana) |
| 3.2 | Alcance | Alcance de la solución descompuesto en componentes manejables: alcance de la Etapa 1 y de la Etapa 2 con criterios de asignación; exclusiones, supuestos y restricciones; catálogo de requerimientos funcionales y no funcionales priorizado y trazable (resumen aquí, trazabilidad completa en el Formulario T-12); criterios de aceptación. | En redacción (2026-10-08). 3.2.1 a 3.2.4 reescritas y evaluadas con los agentes; 3.2.5 reescrita y evaluada en dos rondas con los agentes (2026-10-08), con el Anexo D. Faltan las figuras, los Anexos A a D como documento aparte y la revisión humana. Pendientes del catálogo: ver `80_Artefactos/sd-03_contexto/conciliacion_catalogo.md` (RN-07, RNF-05, SUP-08 y SUP-09, ubicación de RF-180 y RF-181, pocos RF en abastecimiento, comisiones y cartera, trasladar las decisiones al Excel) |
| 3.3 | Esquema de solución | Uno o varios esquemas del modelo conceptual de la solución. Cada diagrama se explica en el texto, por partes si es complejo (sección 6 del Comunicado 10). | Sin redactar |
| 3.4 | Explicación de la Solución | Descripción de la solución según la operación o el negocio y su coherencia con el problema del Capítulo 2. Incluye la estrategia para obtener el apoyo de los grupos de interés clave identificados en 2.4. Mapea al 100 % con la Arquitectura Lógica (4.1): mismos nombres de componentes. | Sin redactar |

Anexos: Formulario T-12.

La redacción vive en `02_Propuesta/latex_final/sd-03.tex` (edición colaborativa en Prism); este maestro solo registra estructura, estado y trazabilidad.

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
- `OnlySimpleSolutions-Subdocumento3-Anexos`: Anexo A (exclusiones, supuestos, responsabilidades del cliente y restricciones), Anexo B (catálogo de requerimientos clasificado), Anexo C (registro de reglas de negocio) y Anexo D (criterios de aceptación de los 28 resultados de negocio). Fuentes en `04_Adjuntos/tablas/sd-03_s2_anexo-*.md`

## Checklist de llenado

- [ ] Cada título del Comunicado 10 está desarrollado en `sd-03.tex`, sin omitir ni mover contenido a otro título
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] La frontera entre el negocio retail y la filial emisora fiscalizada queda definida antes que cualquier vista unificada
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
