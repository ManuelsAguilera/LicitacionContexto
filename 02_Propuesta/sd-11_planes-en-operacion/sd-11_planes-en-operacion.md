---
id: T7-11
tipo: parte
parte: T7-11
titulo: Planes en operación
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos: []
jira: []
cifras: []
secciones:
  - T7-11-11.1
  - T7-11-11.2
actualizado: 2026-10-06
---
# Subdocumento 11 — Planes en operación

> Maestro del subdocumento. Registra la estructura obligatoria del Comunicado 10, el estado y la trazabilidad. El contenido se redacta en `02_Propuesta/latex_final/sd-11.tex`; los adjuntos van como archivos hermanos con prefijo `adj-`, `diag-` o `form-`.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 11 de 14 |
| Título oficial (T-7) | Planes en operación |
| Carpeta | `02_Propuesta/sd-11_planes-en-operacion/` |
| Capítulo en el informe | No cubierto todavía; se redactará en el Informe 2 o 3 |
| Formularios asociados | ninguno |
| Estado | Sin redactar |

## Ponderación (Formulario T-21)

Ítem en el T-21: Planes en operación

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
| 11.1 | Plan Mantención Preventiva / Evolutiva | Mantención preventiva, correctiva y evolutiva con criterios de priorización y presupuesto de capacidad; actualización de dependencias, deuda técnica y ventana de obsolescencia. | Sin redactar |
| 11.2 | Plan Servicios de Operación | Operación conforme a ingeniería de confiabilidad (presupuesto de error, reducción del trabajo manual, análisis retrospectivo sin culpa); gestión de la capacidad y FinOps; pruebas periódicas de recuperación ante desastres y de resiliencia. | Sin redactar |

La redacción vive en `02_Propuesta/latex_final/sd-11.tex` (edición colaborativa en Prism); este maestro solo registra estructura, estado y trazabilidad.

## Adjuntos esperados

- _sin adjuntos previstos_

## Checklist de llenado

- [ ] Cada título del Comunicado 10 está desarrollado en `sd-11.tex`, sin omitir ni mover contenido a otro título
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [ ] Coherente con el despliegue híbrido obligatorio (Art. 16.º) y con el cronograma de 56 meses (Art. 17.º)
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [ ] Diagramas con la fuente en el `.md` y el export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
