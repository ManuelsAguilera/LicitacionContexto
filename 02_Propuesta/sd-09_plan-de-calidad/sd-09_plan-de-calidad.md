---
id: T7-09
tipo: parte
parte: T7-09
titulo: Plan de calidad
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos:
  - ADJ-022
  - ADJ-023
jira: []
cifras: []
secciones:
  - T7-09-9.1
  - T7-09-9.2
  - T7-09-9.3
actualizado: 2026-10-06
---
# Subdocumento 9 — Plan de calidad

> Maestro del subdocumento. Registra la estructura obligatoria del Comunicado 10, el estado y la trazabilidad. El contenido se redacta en `02_Propuesta/latex_final/sd-09.tex`; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 9 de 14 |
| Título oficial (T-7) | Plan de calidad |
| Carpeta | `02_Propuesta/sd-09_plan-de-calidad/` |
| Capítulo en el informe | No cubierto todavía; se redactará en el Informe 2 o 3 |
| Formularios asociados | T-13, T-17 |
| Estado | Sin redactar |

## Ponderación (Formulario T-21)

Ítem en el T-21: Plan de calidad

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
| 9.1 | Plan de Calidad | Marco de aseguramiento basado en ISO/IEC 25010 y modelos de madurez. Métricas de calidad del código, cobertura de pruebas, complejidad y acoplamiento, con umbrales bloqueantes. | Sin redactar |
| 9.2 | Estrategia de Aseguramiento de Calidad | Puertas de calidad, revisiones por pares, análisis estático y dinámico; estrategia de pruebas conforme a ISO/IEC/IEEE 29119; verificación, validación y trazabilidad requerimiento-diseño-código-prueba-despliegue. | Sin redactar |
| 9.3 | Alineación con Plan de Trabajo | Dónde quedan las actividades de calidad en la EDT y en el cronograma del Capítulo 7. | Sin redactar |

Anexos: Formulario T-13; Formulario T-17.

La redacción vive en `02_Propuesta/latex_final/sd-09.tex` (edición colaborativa en Prism); este maestro solo registra estructura, estado y trazabilidad.

## Adjuntos esperados

- `form-T-13.docx`
- `form-T-17_protocolo-aceptacion.docx`

## Checklist de llenado

- [ ] Cada título del Comunicado 10 está desarrollado en `sd-09.tex`, sin omitir ni mover contenido a otro título
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
