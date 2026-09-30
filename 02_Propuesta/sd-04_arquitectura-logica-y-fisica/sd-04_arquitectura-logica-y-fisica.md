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
  - T7-04-4.2
actualizado: 2026-09-29
---
# Subdocumento 4 — Arquitectura lógica y física de la solución

> Maestro del subdocumento. Cada sección se redacta en su propio archivo `sd-04_sN_*.md` dentro de esta carpeta; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 4 de 14 |
| Título oficial (T-7) | Arquitectura lógica y física de la solución |
| Carpeta | `02_Propuesta/sd-04_arquitectura-logica-y-fisica/` |
| Capítulo en el informe | Capítulo IV |
| Formularios asociados | T-11 |
| Estado | Sin redactar |

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

## Contenido exigido por el T-7

- Arquitectura lógica: capas, módulos, límites de contexto, responsabilidades e interfaces.
- Arquitectura física: emplazamiento de cada componente en nube y on-premise, con justificación por componente conforme al Artículo 16.º.
- Arquitectura de integración: servicios, contratos, mensajería, versionado y gobierno.
- Arquitectura de seguridad: modelo Zero Trust, capa expuesta, identidad, cifrado y controles.
- Arquitectura de despliegue: ambientes, redes, alta disponibilidad, recuperación ante desastres y respaldos.
- Dimensionamiento y plan de capacidad, con supuestos de volumen, concurrencia y crecimiento.
- Decisiones de arquitectura registradas, con alternativas evaluadas y criterio de selección.
- La arquitectura debe ser propia de la solución planteada. No se aceptarán diagramas genéricos.

## Secciones

| N | Sección | Archivo | Estado |
| :--- | :--- | :--- | :--- |
| 1 | Arquitectura lógica | `sd-04_s1_arquitectura-logica.md` | Sin redactar |
| 2 | Arquitectura física | `sd-04_s2_arquitectura-fisica.md` | Sin redactar |

### Notas por sección

- **1. Arquitectura lógica** - El Informe 1 marca el encabezado como «(Trabajar)». Subsecciones previstas 4.1.1 a 4.1.6: estilo arquitectónico, límites de contexto, estructura por capas, arquitectura de integración, arquitectura de seguridad y registro de decisiones (ADR).
- **2. Arquitectura física** - El Informe 1 marca el encabezado como «(Trabajar)». Subsecciones previstas 4.2.1 a 4.2.10: diagrama de infraestructura, emplazamiento componente por componente, nodo de tienda, data centers, topología de red, alta disponibilidad y RPO/RTO, dimensionamiento, stack de software, implementos y ambientes.

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

- [ ] Cada sección tiene su archivo `sd-04_sN_*.md` con contenido redactado
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Coherente con el despliegue híbrido obligatorio (Art. 16.º) y con el cronograma de 56 meses (Art. 17.º)
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
