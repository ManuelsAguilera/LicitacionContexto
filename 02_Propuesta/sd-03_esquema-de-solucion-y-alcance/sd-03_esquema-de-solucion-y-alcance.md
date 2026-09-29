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
| 1 | Descripción de la solución propuesta y coherencia con el problema definido | `sd-03_s1_descripcion-de-la-solucion-propuesta-y-coherencia-con-el-p.md` | Parcial en el Informe 1 |
| 2 | Resolución de las decisiones pendientes declaradas por el CLIENTE | `sd-03_s2_resolucion-de-las-decisiones-pendientes-declaradas-por-el-.md` | Desarrollado en el Informe 1 |
| 3 | Módulos funcionales de la solución | `sd-03_s3_modulos-funcionales-de-la-solucion.md` | Desarrollado en el Informe 1 |
| 4 | Diagrama conceptual de solución e interacción de actores | `sd-03_s4_diagrama-conceptual-de-solucion-e-interaccion-de-actores.md` | Sin redactar |
| 5 | Objetivos del proyecto | `sd-03_s5_objetivos-del-proyecto.md` | Desarrollado en el Informe 1 |
| 6 | Alcance de la Etapa 1 y de la Etapa 2, con criterio de asignación | `sd-03_s6_alcance-de-la-etapa-1-y-de-la-etapa-2-con-criterio-de-asig.md` | Desarrollado en el Informe 1 |
| 7 | Exclusiones explícitas, supuestos y restricciones | `sd-03_s7_exclusiones-explicitas-supuestos-y-restricciones.md` | Desarrollado en el Informe 1 |
| 8 | Catálogo de requerimientos funcionales core | `sd-03_s8_catalogo-de-requerimientos-funcionales-core.md` | Desarrollado en el Informe 1 |
| 9 | Catálogo de requerimientos no funcionales core | `sd-03_s9_catalogo-de-requerimientos-no-funcionales-core.md` | Parcial en el Informe 1 |
| 10 | Estrategia para obtener el apoyo de los grupos de interés clave | `sd-03_s10_estrategia-para-obtener-el-apoyo-de-los-grupos-de-interes-.md` | Sin redactar |
| 11 | Criterios de aceptación del alcance comprometido | `sd-03_s11_criterios-de-aceptacion-del-alcance-comprometido.md` | Sin redactar |

### Notas por sección

- **1. Descripción de la solución propuesta y coherencia con el problema definido** - El T-7 exige explícitamente la coherencia con el problema. El cuerpo del informe abre con un enunciado más genérico.
- **2. Resolución de las decisiones pendientes declaradas por el CLIENTE** - Desarrolla SUP-01 a SUP-07 y las decisiones 3.2.6.1 a 3.2.6.6 (existencia, precio, pedido, postventa, crédito e identidad). Es el núcleo argumental del capítulo.
- **3. Módulos funcionales de la solución** - Siete bloques: 3.3.1 a 3.3.7. Los nombres de los componentes deben coincidir al 100 % con los de la arquitectura lógica (subdocumento 4).
- **4. Diagrama conceptual de solución e interacción de actores** - Fuente Mermaid dentro del `.md`; export en `04_Adjuntos/diagramas/`.
- **5. Objetivos del proyecto** - 3.5.1 objetivo general, 3.5.2 objetivos específicos y 3.5.3 responsabilidad e indicadores.
- **6. Alcance de la Etapa 1 y de la Etapa 2, con criterio de asignación** - Debe respetar la separación de etapas del Art. 17 y el solapamiento de los meses 13 a 15 y 19 a 20. Referencia de trazabilidad: OSS-241.
- **8. Catálogo de requerimientos funcionales core** - Secciones 3.8.1 a 3.8.8. Debe trazarse contra el catálogo v3.0 de `01_Requerimientos/`.
- **9. Catálogo de requerimientos no funcionales core** - El título 3.9 aparece duplicado al final del capítulo: hay un encabezado repetido que habrá que resolver al ensamblar.
- **10. Estrategia para obtener el apoyo de los grupos de interés clave** - Referencia de trazabilidad: OSS-245.
- **11. Criterios de aceptación del alcance comprometido** - Referencia de trazabilidad: OSS-244.

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
