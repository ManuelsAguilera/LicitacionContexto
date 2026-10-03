---
id: T7-01
tipo: parte
parte: T7-01
titulo: Presentación de la empresa
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-001
  - ADJ-002
  - ADJ-003
jira:
  - OSS-165
  - OSS-69
  - OSS-72
  - OSS-73
  - OSS-74
  - OSS-75
  - OSS-76
  - OSS-77
cifras: []
secciones:
  - T7-01-1.1
  - T7-01-1.2
  - T7-01-1.3
  - T7-01-1.4
  - T7-01-1.5
  - T7-01-1.6
actualizado: 2026-09-29
---
# Subdocumento 1 — Presentación de la empresa

> Maestro del subdocumento. Cada sección se redacta en su propio archivo `sd-01_sN_*.md` dentro de esta carpeta; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 1 de 14 |
| Título oficial (T-7) | Presentación de la empresa |
| Carpeta | `02_Propuesta/sd-01_presentacion-empresa/` |
| Capítulo en el informe | Capítulo I |
| Formularios asociados | T-6 |
| Estado | Desarrollado en el Informe 1 |

## Ponderación (Formulario T-21)

Ítem en el T-21: Presentación de la empresa

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

- Presentación de la empresa y reseña de la trayectoria, capacidades instaladas, líneas de negocio, productos y servicios ofrecidos.
- Estructura organizacional, dotación, certificaciones institucionales y alianzas tecnológicas vigentes.
- Experiencia relevante en la industria del caso y en proyectos de complejidad equivalente.
- Modelo de gobierno interno de calidad, seguridad y gestión del conocimiento.

## Secciones

| N | Sección | Archivo | Estado |
| :--- | :--- | :--- | :--- |
| 1 | Identificación y perfil corporativo | `sd-01_s1_identificacion-y-perfil-corporativo.md` | Desarrollado en el Informe 1 |
| 2 | Capacidades instaladas | `sd-01_s2_capacidades-instaladas.md` | Desarrollado en el Informe 1 |
| 3 | Misión, visión y valores | `sd-01_s3_mision-vision-y-valores.md` | Desarrollado en el Informe 1 |
| 4 | Experiencia relevante (Formulario T-6) | `sd-01_s4_experiencia-relevante-formulario-t-6.md` | Desarrollado en el Informe 1 |
| 5 | Certificaciones institucionales y alianzas tecnológicas vigentes | `sd-01_s5_certificaciones-institucionales-y-alianzas-tecnologicas-vi.md` | Parcial en el Informe 1 |
| 6 | Frente de jefaturas asignado | `sd-01_s6_frente-de-jefaturas-asignado.md` | Parcial en el Informe 1 |

### Notas por sección

- **1. Identificación y perfil corporativo** - Datos de operación de Ancoa y presentación de la proponente.
- **2. Capacidades instaladas** - Fábrica de software, célula de datos, célula de ciberseguridad y mesa de servicio.
- **4. Experiencia relevante (Formulario T-6)** - Mínimo tres proyectos finalizados y en operación en los últimos cinco años.
- **5. Certificaciones institucionales y alianzas tecnológicas vigentes** - Falta acreditar ISO 9001, ISO/IEC 27001 y PCI-DSS: el texto actual dice literalmente «Copiar del caso, o con claude». Es requisito habilitante (Art. 34).
- **6. Frente de jefaturas asignado** - Solo consta el nombre del jefe de proyecto (Vicente Rosales Miranda). Faltan arquitecto de solución, encargado de seguridad, líder de datos y líder de implantación.

## Trazabilidad con Jira

Agrupadora: **OSS-165**.

La estructura de trabajo vive en el proyecto `OSS` y **no es el índice del informe**: los nombres de sección del plan son maestros y no coinciden uno a uno con las secciones de este subdocumento.

| Clave | Sección en el plan de Jira | Subtareas |
| :--- | :--- | :--- |
| OSS-72 | 1. Introducción | 2 |
| OSS-69 | 1.1 Presentación de la empresa | 2 |
| OSS-73 | 1.2 Estructura Organizacional | 1 |
| OSS-74 | 1.3 Gobierno interno Calidad, Seguridad y Conocimiento | 1 |
| OSS-75 | 1.4 Experiencia y Certificaciones | 3 |
| OSS-76 | 1.5 Estructura para Proyecto | 1 |
| OSS-77 | 1.6 Alianzas | 1 |

## Adjuntos esperados

- `form-T-6_experiencia-relevante.docx : formulario oficial, se entrega en el Sobre 2`
- `adj-sd-01_s5_certificaciones.pdf (evidencia de certificaciones)`
- `adj-sd-01_s6_frente-jefaturas.md (matriz de roles, RAE y dedicación)`

## Checklist de llenado

- [ ] Cada sección tiene su archivo `sd-01_sN_*.md` con contenido redactado
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
