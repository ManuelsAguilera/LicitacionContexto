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
actualizado: 2026-10-03
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
| Estado | Borrador alineado con rúbrica; acreditaciones pendientes |

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
| 0 | Introducción | `sd-01_s0_introduccion.md` | Redactado |
| 1 | 1.1 Presentación de la empresa | `sd-01_s1_presentacion-de-la-empresa.md` | Borrador; cifras institucionales por conciliar |
| 2 | 1.2 Estructura Organizacional | `sd-01_s2_estructura-organizacional.md` | Borrador; desglose permanente pendiente |
| 3 | 1.3 Gobierno interno Calidad, Seguridad y Conocimiento | `sd-01_s3_gobierno-interno.md` | Borrador; políticas y registros pendientes |
| 4 | 1.4 Experiencia y Certificaciones | `sd-01_s4_experiencia-y-certificaciones.md` | Borrador; T-6 y certificados pendientes |
| 5 | 1.5 Estructura para Proyecto | `sd-01_s5_estructura-para-proyecto.md` | Borrador; dedicaciones y T-8 pendientes |
| 6 | 1.6 Alianzas | `sd-01_s6_alianzas.md` | Borrador; acuerdos pendientes |

### Notas de revisión

El [diagnóstico por criterio](revision-rubrica-y-anexo.md) contrasta los borradores «Informes(7).md» y «Informes(8).md» con las Bases, el Comunicado 10 y la rúbrica S1-01 a S1-09. El anexo A.2 aporta datos preliminares para T-6, pero incluye valores estimados, referencias sin contacto nominal y una atribución a una empresa real. No se consideran acreditados los habilitantes hasta recibir los soportes. El artículo 34 exige ISO/IEC 27001 vigente **o** un plan formal firmado con hitos en los primeros doce meses; el texto de las Bases disponible no establece aquí PCI DSS como certificación institucional habilitante.

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

- Formulario T-6 en archivo separado del subdocumento: falta consolidar estimaciones y referencias verificables.
- Certificados institucionales vigentes o plan formal ISO/IEC 27001 firmado, según corresponda.
- Matriz de roles y dedicación, currículos, cartas y credenciales individuales en Capítulo 12 / Formulario T-8.
- Certificado de socio del proveedor de nube o carta de compromiso de socio certificado participante.

## Checklist de llenado

- [x] La introducción y cada sección oficial 1.1 a 1.6 tienen su archivo `sd-01_sN_*.md` con contenido redactado
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [x] Figuras 1 y 2 incrustadas como imágenes; fuentes `.dot` y exportaciones PNG/PDF en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
