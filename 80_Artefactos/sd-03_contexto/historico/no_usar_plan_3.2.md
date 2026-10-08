> **ARCHIVADO (2026-10-08). No usar como fuente.** Material de trabajo superado por `sd-03.tex`, los Anexos A a D y `ficha_alcance_sd-03.md`. Usa códigos y decisiones antiguas. Se conserva solo por trazabilidad.

# Plan de redacción — 3.2 Alcance (sd-03)

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

Documento de trabajo. No es entregable.

## Decisiones tomadas (2026-10-05)

| Tema | Decisión |
| :--- | :--- |
| Dónde se redacta | Directo en `02_Propuesta/latex_final/sd-03.tex`; luego `prism-empaquetar --parte T7-03`. |
| Plataformas condicionales | Postura firme: **Escenario B** (renovación ampliada del núcleo: reemplazo por etapas del sistema central de Retail, además de crédito y POS). |
| Nomenclatura | Servicios R/F/X se conservan. Exclusiones del catálogo (hoja 7) pasan de X-NN a **EXC-NN**. |
| Reparto Etapa 1 / Etapa 2 | Cerrado (2026-10-06): ver `asignacion_etapas.md` (rondas A a F) y `entregables_alcance.md` (columna Etapa; D decidido, S sugerido por confirmar). |
| Ciclo de vida | Híbrido: marco predictivo (contrato, dos etapas, hitos, 13 servicios, cambios por solicitud formal) y desarrollo adaptativo dentro de cada etapa. Ver `enunciado_alcance.md`, sección 4. |

## Estructura de 3.2

1. Introducción (texto de caída).
2. 3.2.1 Descomposición del alcance: promesas → A/B/C → 13 servicios R/F/X; tratamiento de plataformas (Escenario B); C3 no es servicio.
3. 3.2.2 Alcance de la Etapa 1 y de la Etapa 2: asignación, criterios, respuesta a Caso 13.1 y a las dos objeciones, hitos y congelamientos de 13.2, figura de línea de tiempo.
4. 3.2.3 Exclusiones, supuestos y restricciones: resumen y análisis; detalle en anexo sd-02 (SUP-NN, RES-NN, EXC-NN).
5. 3.2.4 Catálogo de requerimientos: MoSCoW, síntesis por servicio × etapa × prioridad, criterio de casos limítrofes (Caso 17.2), detalle en T-12.
6. 3.2.5 Criterios de aceptación: entregable, marcha blanca, resultado de negocio.

## Datos fijos

- Bases Admin. Art. 17: Etapa 1 desarrollo meses 1–12, marcha blanca 13–15, producción mes 16. Etapa 2 desarrollo 13–18, marcha blanca 19–20, producción mes 21. Operación 21–56.
- Caso 13.1: preferencia del comité (inventario → precio → financiero/marketplace/analítica) y dos objeciones (migración 620.000 clientes antes de 2029; frontera de datos antes de toda vista unificada).
- Caso 13.2: cinco ventanas de congelamiento; hito 2029.
- Caso, Gerente General: «Si alguien viene a decirme que va a reemplazar todo en dos etapas, no le voy a creer.» El Escenario B debe presentarse como reemplazo progresivo con convivencia, no como sustitución total.

## Pendientes detectados

- Catálogo v3.0 sin columnas de etapa ni de servicio: construir cruce RF/RNF → R/F/X → etapa → prioridad.
- Unificar M-01..M-24 (texto viejo y sd-02) con R/F/X; 3.4 y 4.1 deben usar los mismos nombres.
- Renombrar X-NN → EXC-NN en la hoja 7 del Excel (fuente oficial) y regenerar el espejo.
