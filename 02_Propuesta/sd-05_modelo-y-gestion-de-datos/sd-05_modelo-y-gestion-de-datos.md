# Subdocumento 5 — Modelo y gestión de datos

> Maestro del subdocumento. Cada sección se redacta en su propio archivo `sd-05_sN_*.md` dentro de esta carpeta; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

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

## Contenido exigido por el T-7

- Dominio de información.
- Selección del motor y del paradigma de persistencia, con justificación: relacional o no relacional, transaccionalidad, consistencia y disponibilidad conforme al teorema CAP.
- Estrategia de migración, saneamiento, validación y conciliación de los datos históricos.
- Estrategia de desempeño: indexación, particionamiento, caché y optimización de consultas.
- Separación entre almacenamiento transaccional y analítico, y modelo de explotación de información.
- Calidad de datos, retención, archivado y eliminación segura.

## Secciones

| N | Sección | Archivo | Estado |
| :--- | :--- | :--- | :--- |
| 1 | Dominio de información | `sd-05_s1_dominio-de-informacion.md` | Sin redactar |
| 2 | Frontera de datos entre retail y filial emisora | `sd-05_s2_frontera-de-datos-entre-retail-y-filial-emisora.md` | Sin redactar |
| 3 | Selección del paradigma de persistencia por dominio, con teorema CAP explícito | `sd-05_s3_seleccion-del-paradigma-de-persistencia-por-dominio-con-te.md` | Sin redactar |
| 4 | Modelo del dato de existencia y del disponible-para-vender | `sd-05_s4_modelo-del-dato-de-existencia-y-del-disponible-para-vender.md` | Sin redactar |
| 5 | Trazabilidad del precio publicado | `sd-05_s5_trazabilidad-del-precio-publicado.md` | Sin redactar |
| 6 | Modelo de evidencia de consentimiento | `sd-05_s6_modelo-de-evidencia-de-consentimiento.md` | Sin redactar |
| 7 | Estrategia general de migración, saneamiento y conciliación de datos históricos | `sd-05_s7_estrategia-general-de-migracion-saneamiento-y-conciliacion.md` | Sin redactar |
| 8 | Retención, archivado y ciclo de vida del dato | `sd-05_s8_retencion-archivado-y-ciclo-de-vida-del-dato.md` | Sin redactar |
| 9 | Estrategia de desempeño | `sd-05_s9_estrategia-de-desempeno.md` | Sin redactar |
| 10 | Separación entre almacenamiento transaccional y analítico | `sd-05_s10_separacion-entre-almacenamiento-transaccional-y-analitico.md` | Sin redactar |

### Notas por sección

- **2. Frontera de datos entre retail y filial emisora** - Es donde se materializa la línea roja: la separación debe quedar definida antes que cualquier vista unificada.
- **4. Modelo del dato de existencia y del disponible-para-vender** - Debe resolver la fuente única de verdad del disponible (referencia OSS-249).
- **5. Trazabilidad del precio publicado** - Es la evidencia contra la fiscalización de precios (11 % de discrepancia).
- **6. Modelo de evidencia de consentimiento** - Responde a las 1.240 repactaciones sin evidencia recuperable.
- **8. Retención, archivado y ciclo de vida del dato** - La evidencia de consentimiento se retiene 10 años y las grabaciones se purgan a 90 días: el plazo de retención es en sí un requisito.

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

- [ ] Cada sección tiene su archivo `sd-05_sN_*.md` con contenido redactado
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] La frontera entre el negocio retail y la filial emisora fiscalizada queda definida antes que cualquier vista unificada
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
