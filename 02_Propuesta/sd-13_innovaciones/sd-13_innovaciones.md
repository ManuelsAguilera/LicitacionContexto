---
id: T7-13
tipo: parte
parte: T7-13
titulo: Innovaciones
estado: borrador
bases:
  - "Bases Administrativas, artículos 28 a 30"
  - "Bases Transversales, capítulos 13, 18 y 26"
  - "Comunicado 10, capítulo 13"
requisitos:
  - RF-131
  - RF-134
  - RF-135
  - RF-136
  - RF-137
depende_de:
  - T7-03
  - T7-04
  - T7-05
  - T7-07
adjuntos:
  - ADJ-025
jira:
  - OSS-102
  - OSS-103
  - OSS-104
  - OSS-172
cifras: []
secciones:
  - T7-13-INTRO
  - T7-13-13.1
  - T7-13-13.2
  - T7-13-13.3
  - T7-13-13.4
  - T7-13-13.5
  - T7-13-REF
  - T7-13-IA
origen: "80_Artefactos/sd-13_contexto/investigacion_cinco_innovaciones.md; decision_cartera_equipo.md"
actualizado: 2026-10-25
---
# Subdocumento 13 — Innovaciones

> Fuente de contenido: [`OnlySimpleSolutions-Subdocumento13.tex`](../latex_final/sd-13/OnlySimpleSolutions-Subdocumento13.tex). Este maestro conserva estructura, estado y trazabilidad; su contenido previo no sustituye el LaTeX. Pendiente de conciliación con SD-04 y SD-07; sin revisión humana.


> Maestro del subdocumento. La fuente inicial está en los archivos de sección enumerados abajo. Tras la primera importación, la fuente final será `02_Propuesta/latex_final/sd-13/OnlySimpleSolutions-Subdocumento13.tex`. No existe todavía esa importación porque faltan las herramientas de exportación en este entorno.

## Identificación

| Campo | Valor |
| :--- | :--- |
| Subdocumento T-7 | 13 de 14 |
| Título oficial (T-7) | Innovaciones |
| Carpeta | `02_Propuesta/sd-13_innovaciones/` |
| Capítulo en el informe | Capítulo VI |
| Formularios asociados | T-19 |
| Estado | Borrador LaTeX disponible; por conciliar contra SD-04 y SD-07; sin revisión humana registrada |

## Ponderación (Formulario T-21)

Ítem en el T-21: Innovaciones

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

Cada innovación desarrolla los siete elementos del Art. 29.º (problema, tecnología, madurez, diseño de incorporación, impacto económico, indicador de verificación y riesgo de adopción) y su trazabilidad con la arquitectura, la EDT y el flujo de caja. Las de base tecnológica citan fuentes en APA 7.ª. El título se mantiene tal cual («13.1 Innovación 1»); el primer párrafo declara el tipo y el nombre (sección 10 del Comunicado 10).

| N | Título oficial | Contenido que debe desarrollar | Estado |
| :--- | :--- | :--- | :--- |
| 13.1 | Innovación 1 | Lockers Ancoa 24/7, producto o servicio. | Borrador |
| 13.2 | Innovación 2 | Conteo cíclico predictivo, proceso. | Borrador |
| 13.3 | Innovación 3 | Búsqueda vectorial multimodal, tecnología. | Borrador |
| 13.4 | Innovación 4 | Retail Media Network, modelo de negocio. | Borrador |
| 13.5 | Innovación 5 | Modo Tienda con fila virtual, experiencia de usuario. | Borrador |

Anexos: Formulario T-19.

## Fuentes para la primera importación

Esta tabla determina el orden de ensamblado del exportador. El número es de ensamblado; los títulos dentro de las fuentes mantienen 13.1 a 13.5 y el cierre sin numeración.

| Orden | Contenido | Archivo | Estado |
| :--- | :--- | :--- | :--- |
| 0 | Introducción | `sd-13_s0_introduccion.md` | Borrador |
| 1 | Innovación 1 | `sd-13_s1_innovacion-1.md` | Borrador |
| 2 | Innovación 2 | `sd-13_s2_innovacion-2.md` | Borrador |
| 3 | Innovación 3 | `sd-13_s3_innovacion-3.md` | Borrador |
| 4 | Innovación 4 | `sd-13_s4_innovacion-4.md` | Borrador |
| 5 | Innovación 5 | `sd-13_s5_innovacion-5.md` | Borrador |
| 6 | Referencias | `sd-13_s7_referencias.md` | Borrador |
| 7 | Declaración de uso de IA | `sd-13_s6_declaracion-ia.md` | Borrador |

La selección de equipos es de referencia. Para cerrar el T-19 deben fijarse configuración, metas numéricas donde no existe línea base, valorización de la Oferta Económica y paquetes detallados del T-14. La escala de madurez distingue componente documentado, integración probada y operación aceptada. Las probabilidades de riesgo son valoraciones iniciales y no frecuencias medidas.

El modo tienda se entrega en el mes 21 para respetar la Etapa 2 del servicio de clientes Retail en el SD-03. Esta asignación precisa la propuesta de piloto temprano del contexto de investigación.

## Trazabilidad con Jira

Agrupadora: **OSS-172**.

La estructura de trabajo vive en el proyecto `OSS` y **no es el índice del informe**: los nombres de sección del plan son maestros y no coinciden uno a uno con las secciones de este subdocumento.

| Clave | Sección en el plan de Jira | Subtareas |
| :--- | :--- | :--- |
| OSS-102 | 13. Introducción | 1 |
| OSS-103 | 13.3 Innovación 3 - Tecnológica o de arquitectura | 3 |
| OSS-104 | 13.4 Innovación 4 - Modelo de negocio o de contratación | 1 |

## Adjuntos esperados

- `form-T-19_cartera-innovaciones.docx`
- Figura 13.1 en `04_Adjuntos/diagramas/diag-13-00_cartera.png`, con fuente editable `.py`.
- Referencias incorporadas al cierre, en `sd-13_referencias.md`.

## Checklist de llenado

- [ ] Cada título del Comunicado 10 está desarrollado en `sd-13.tex`, sin omitir ni mover contenido a otro título
- [ ] Las cifras citadas derivan de `00_Bases/` o de un cálculo mostrado
- [x] Cinco innovaciones redactadas, una por cada tipo del Art. 28.º, con apartados para los siete elementos del Art. 29.º
- [ ] Cada innovación trazable con la arquitectura, la EDT y el flujo de caja
- [ ] Formularios asociados completados y guardados en `03_Formularios/`
- [x] Diagrama citado e interpretado, con fuente editable y export en `04_Adjuntos/diagramas/`

---

Fuentes rectores: `00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md` (estructura), `00_Bases/Bases_Administrativas.md` (Art. 5.º, Formularios T-7 y T-21), `00_Bases/Bases_Transversales.md` (RT-CC.NN) y `00_Bases/Caso_09_Cadena_Multitienda.md`.
