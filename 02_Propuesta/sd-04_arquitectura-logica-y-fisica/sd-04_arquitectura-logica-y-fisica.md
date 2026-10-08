---
id: T7-04
tipo: parte
parte: T7-04
titulo: Arquitectura lógica y física de la solución
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-008
  - ADJ-009
  - ADJ-010
  - ADJ-011
  - ADJ-012
jira:
  - OSS-168
  - OSS-169
  - OSS-170
  - OSS-89
  - OSS-90
  - OSS-91
  - OSS-92
  - OSS-93
  - OSS-94
  - OSS-95
  - OSS-96
cifras: []
secciones:
  - T7-04-4.1
  - T7-04-4.1.1
  - T7-04-4.2
  - T7-04-4.2.1
  - T7-04-4.3
  - T7-04-4.3.1
  - T7-04-4.3.2
actualizado: 2026-10-08
---
# Subdocumento 4 — Arquitectura lógica y física de la solución

> Maestro del subdocumento. Registra la estructura obligatoria del Comunicado 10, el estado y la trazabilidad. El contenido se redacta en `02_Propuesta/latex_final/sd-04.tex`; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 4 de 14 |
| Título oficial (T-7) | Arquitectura lógica y física de la solución |
| Carpeta | `02_Propuesta/sd-04_arquitectura-logica-y-fisica/` |
| Capítulo en el informe | Capítulo IV |
| Formularios asociados | T-11 |
| Estado | 4.1 a 4.3.2 en borrador; dimensionamiento e inventario de plataformas pendientes |

## Ponderación (Formulario T-21)

Ítem en el T-21: 4.1 a) Esquema Solución / b) Arquitectura Lógica, y 4.2 a) Arquitectura Física b) Especificaciones de Tecnologías de Software c) Especificaciones de Implementos d) Data Center Primaria e) Data Center Secundaria

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

En todo el capítulo: la arquitectura es propia de la solución planteada (no se aceptan diagramas genéricos) y cada decisión se registra con las alternativas evaluadas y el criterio de selección.

| N | Título oficial | Contenido que debe desarrollar | Estado |
| :--- | :--- | :--- | :--- |
| 4.1 | Arquitectura lógica | Mapeada al 100 % con el Esquema de Solución (3.3) y la Explicación de la Solución (3.4). Capas, módulos, límites de contexto, responsabilidades e interfaces; arquitectura de integración (servicios, contratos, mensajería, versionado, gobierno); arquitectura de seguridad (Zero Trust, capa expuesta, identidad, cifrado, controles). | Borrador; validar partición y contratos |
| 4.1.1 | Especificaciones Tecnologías de Software a utilizar | Lenguajes, marcos, motores, servicios y productos, con alternativas evaluadas y criterio de decisión. | Selección inicial documentada; faltan versiones y T-11 |
| 4.2 | Arquitectura física | Mapeada al 100 % con la Arquitectura Lógica. Emplazamiento de cada componente en nube y on-premise (Art. 16.º); servicios contratados en nube; arquitectura de despliegue (ambientes Desarrollo, QA, Preproducción, Producción y Recuperación ante Desastres, redes, alta disponibilidad, DR, respaldos); conexiones y puntos de falla con su contingencia; dimensionamiento y plan de capacidad. | Borrador; falta inventario y memoria de capacidad |
| 4.2.1 | Especificaciones Implementos a proveer (Hardware y Software) | Resumen y análisis; el detalle va en el Formulario T-11. | Borrador; falta inventario de tienda y T-11 |
| 4.3 | Data center | Texto que presenta la estrategia de centros de datos antes de los subtítulos. | Borrador; falta informe de brechas 2024 |
| 4.3.1 | Especificaciones Data Center Primaria | Proveedor, región, zonas de disponibilidad, servicios y sitio on-premise, según corresponda. | Borrador; falta emplazamiento de legados |
| 4.3.2 | Especificaciones Data Center Secundario | Región o sitio de recuperación, replicación, RPO y RTO, y procedimiento de conmutación. | Borrador; falta prueba y validación jurídica |

Anexos: Formulario T-11.

Se sugiere incluir en 4.2 una tabla de mapeo que muestre, para cada componente, su correspondencia entre esquema de solución (3.3), arquitectura lógica (4.1) y componente físico (4.2).

La redacción vive en `02_Propuesta/latex_final/sd-04.tex` (edición colaborativa en Prism); este maestro solo registra estructura, estado y trazabilidad.

## Trazabilidad con Jira

Agrupadora: **OSS-168 (lógica) / OSS-169 (física e implementos) / OSS-170 (data center)**.

La estructura de trabajo vive en el proyecto `OSS` y **no es el índice del informe**: los nombres de sección del plan son maestros y no coinciden uno a uno con las secciones de este subdocumento.

| Clave | Sección en el plan de Jira | Subtareas |
| :--- | :--- | :--- |
| OSS-89 | 4. Introducción | 1 |
| OSS-90 | 4.1 Arquitectura lógica | 7 |
| OSS-91 | 4.1.1 Especificaciones de tecnologías de software a utilizar | 1 |
| OSS-92 | 4.2 Arquitectura física | 2 |
| OSS-93 | 4.2.1 Especificaciones de implementos a proveer (hardware y software) | 2 |
| OSS-94 | 4.3 Data center | 2 |
| OSS-95 | 4.3.1 Especificaciones Data Center Primario | 1 |
| OSS-96 | 4.3.2 Especificaciones Data Center Secundario | 1 |

## Adjuntos esperados

- `diag-04-01_arquitectura-logica.svg`
- `diag-04-02_arquitectura-fisica.svg`
- `diag-04-03_data-center.svg`
- `adj-sd-04_s2_inventario-hardware.xlsx : las Bases exigen la lista de hardware en Excel`
- `form-T-11_especificaciones-tecnicas-ofertadas.docx`

## Checklist de llenado

- [ ] Cada título del Comunicado 10 está desarrollado en `sd-04.tex`, sin omitir ni mover contenido a otro título
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Coherente con el despliegue híbrido obligatorio (Art. 16.º) y con el cronograma de 56 meses (Art. 17.º)
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
