# Propuesta técnica — índice de subdocumentos

La Propuesta Técnica se estructura en **catorce subdocumentos** (Formulario T-7, `00_Bases/Bases_Administrativas.md:2066`). Cada subdocumento tiene su carpeta `sd-NN_*/` con un `.md` maestro y un archivo por sección; los adjuntos son archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Orden de los subdocumentos

| N | Subdocumento | Formularios | Capítulo del informe | Estado |
| :--- | :--- | :--- | :--- | :--- |
| 01 | [Presentación de la empresa](sd-01_presentacion-empresa/) | T-6 | Capítulo I | Desarrollado en el Informe 1 |
| 02 | [Resumen Ejecutivo, comprensión del problema y de la necesidad](sd-02_problema-y-necesidad/) | - | Capítulo II | Desarrollado en el Informe 1 |
| 03 | [Esquema de solución y alcance](sd-03_esquema-de-solucion-y-alcance/) | T-12 | Capítulo III | En redacción (rehecho desde cero) |
| 04 | [Arquitectura lógica y física de la solución](sd-04_arquitectura-logica-y-fisica/) | T-11 | Capítulo IV | Sin redactar |
| 05 | [Modelo y gestión de datos](sd-05_modelo-y-gestion-de-datos/) | - | Capítulo V | Sin redactar |
| 06 | [Metodologías](sd-06_metodologias/) | T-9, T-10 | Informe 2/3 | Sin redactar |
| 07 | [Plan de trabajo, EDT, cronograma e implantación](sd-07_plan-de-trabajo-EDT-e-implantacion/) | T-14, T-15, T-18 | Informe 2/3 | Sin redactar |
| 08 | [Plan de riesgos](sd-08_plan-de-riesgos/) | T-16 | Informe 2/3 | Sin redactar |
| 09 | [Plan de calidad](sd-09_plan-de-calidad/) | T-13, T-17 | Informe 2/3 | Sin redactar |
| 10 | [Servicios de operación y niveles de servicio](sd-10_servicios-de-operacion-y-niveles-de-servicio/) | - | Informe 2/3 | Sin redactar |
| 11 | [Planes en operación](sd-11_planes-en-operacion/) | - | Informe 2/3 | Sin redactar |
| 12 | [Equipo de trabajo, subcontrataciones y alianzas](sd-12_equipo-subcontrataciones-y-alianzas/) | T-8 | Informe 2/3 | Sin redactar |
| 13 | [Innovaciones](sd-13_innovaciones/) | T-19 | Capítulo VI | Sin redactar |
| 14 | [Ventajas, beneficios y consolidación](sd-14_ventajas-beneficios-y-consolidacion/) | - | Informe 2/3 | Sin redactar |

## Ponderación (Formulario T-21)

Ningún subdocumento tiene ponderación registrada. La tabla del T-21 en `00_Bases/Bases_Administrativas.md:2366` está incompleta en la extracción y el encabezado de la tabla de correspondencia *sección / subdocumento T-7 / ponderación T-21* del Informe 1 es un marcador de posición sin contenido. Se dejará constancia cuando se reparen las tablas; **no se estiman porcentajes**.

## Cobertura de los informes preparatorios

El Art. 45.º obliga a tres informes y tres presentaciones preparatorias. El `Informe 1` cubre los subdocumentos 1 a 5 y el 13 (se arma desde los `.tex` de `latex_final/`). Los subdocumentos 6 a 12 y el 14 se redactarán en los informes 2 y 3.

## Artefactos de trabajo heredados

Los documentos de `80_Artefactos/` se conservan como fuentes de trabajo y no se ensamblan automáticamente. Su relación con los subdocumentos oficiales es:

| Artefacto | Destino de consolidación | Uso actual |
| :--- | :--- | :--- |
| `seccion3_innovaciones.md` | Subdocumento 13 | Fichas candidatas INN-1 a INN-5 y trazabilidad; consolidar en las secciones 13.1–13.3 y Formulario T-19. |

La consolidación queda pendiente porque el Informe 1 ya cubre estos capítulos y debe evitarse duplicar o reemplazar contenido sin cotejarlo. Los artefactos mantienen enlaces relativos a las rutas vigentes.

## Ensamblado del documento final

El documento final se arma concatenando, en orden, los archivos `sd-NN_sN_*.md` de las 14 carpetas:

1. Se recorren las carpetas `sd-01_` a `sd-14_` en orden numérico.
2. Dentro de cada carpeta, se recorren los `sd-NN_sN_*.md` en orden de sección.
3. Cada adjunto referenciado se inserta en su lugar, no al final.
4. Los diagramas se insertan desde el export en `04_Adjuntos/diagramas/`.
5. La salida oficial va a `07_Entregables/sobre_2_tecnico/` y `07_Entregables/pdf_final/`.

## Convención de nombres

| Tipo | Patrón | Ejemplo |
| :--- | :--- | :--- |
| Maestro del subdocumento | `sd-NN_titulo.md` | `sd-04_arquitectura-logica-y-fisica.md` |
| Texto de sección | `sd-NN_sN_titulo.md` | `sd-04_s2_arquitectura-fisica.md` |
| Adjunto | `sd-NN_sN_titulo.<ext>` | `sd-04_s2_inventario-hardware.xlsx` |
| Diagrama exportado | `diag-NN-SN_titulo.<ext>` | `diag-04-02_arquitectura-fisica.svg` |
| Formulario oficial | `form-<ID>_titulo.<ext>` | `form-T-12_matriz-cumplimiento.docx` |

## Observaciones sobre el estado actual

Detectadas al comparar el índice del Informe 1 con su cuerpo. **No se corrigen acá**: las tablas del informe quedan tal cual hasta que se reparen las de las Bases.

1. El capítulo I del Informe 1 no tiene la sección *Modelo de gobierno interno de calidad, seguridad y gestión del conocimiento*, que su índice anuncia como 1.6 y el T-7 exige. En el cuerpo, 1.6 es *Frente de jefaturas asignado*.
2. El índice del capítulo III anuncia una sección 3.12 *Muestra de matriz de trazabilidad (T-12)* que no aparece en el cuerpo.
3. El índice del capítulo VI anuncia las secciones 6.1 a 6.8, con una ficha por tipo de innovación; el cuerpo solo tiene los encabezados 6.1 a 6.4.
4. El título 3.9 *Catálogo de requerimientos no funcionales core* aparece dos veces en el cuerpo del capítulo III.
5. La estructura de secciones del plan de Jira (`05_Gestion/jira/plan/`) no coincide uno a uno con el índice del Informe 1: conviven dos taxonomías de secciones.
6. Las tablas de las Bases están incompletas en la extracción (ponderaciones del T-21 entre otras). Decidido no intentar reconstruirlas por ahora.

---

Ver `AGENTS.md` para las reglas de precedencia y la convención de formato del repositorio.
