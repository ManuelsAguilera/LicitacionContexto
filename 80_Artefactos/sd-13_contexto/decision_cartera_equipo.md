# Cartera de innovaciones del equipo — decisión sobre la innovación 2

Fecha: 2026-10-11. Documento de contexto para el SD-13 y el Formulario T-19.

Investigación de la cartera: [investigacion_cinco_innovaciones.md](investigacion_cinco_innovaciones.md). Contiene alternativas, recomendaciones técnicas, fuentes primarias, indicadores y condiciones pendientes para las cinco candidatas.

## Procedencia y decisión

El resumen aportado por el usuario, `C:/Users/mosta/Downloads/Resumen_innovaciones_equipo.md`, propone lockers, inventario RFID, búsqueda multimodal, retail media y modo tienda con fila virtual. En esta conversación el usuario decidió sustituir la innovación 2 de inventario continuo con RFID por **conteo cíclico predictivo**. Esta decisión actualiza la cartera del resumen del equipo; no implica aprobación técnica final de las otras cuatro candidatas.

| N.º | Tipo obligatorio | Candidata |
| :--- | :--- | :--- |
| 1 | Producto o servicio | Lockers Ancoa 24/7 |
| 2 | Proceso | Conteo cíclico predictivo |
| 3 | Tecnología o arquitectura | Búsqueda vectorial multimodal |
| 4 | Modelo de negocio o contratación | Retail Media Network |
| 5 | Experiencia de usuario | Modo Tienda con fila virtual de probadores |

La cartera completa del informe `informe_candidatas_innovacion.md`, fechado el 2026-10-08, se conserva como antecedente. Su apartado 4.2 aporta contexto para la innovación 2 elegida aquí; las otras candidatas de ese informe no representan la cartera del resumen del equipo.

## Innovación 2 — Conteo cíclico predictivo

**Problema.** El Caso 09 registra discrepancias en el 12,4 % de las referencias auditadas mediante conteo cíclico. Se busca mejorar la selección de referencias y ubicaciones a contar para detectar diferencias relevantes con las horas disponibles.

**Cambio de proceso.** Un modelo de machine learning estima el riesgo y la magnitud esperada de discrepancia por referencia, ubicación y período. Con esa estimación propone una lista priorizada de conteos que el responsable de inventario revisa y aprueba. Los conteos verifican la existencia física y alimentan la evaluación posterior del modelo. La selección de variables depende del perfilado de los datos disponibles.

**Aporte diferencial.** Según el antecedente del 2026-10-08, RF-131 a RF-137 ya cubren parametrización, programación y seguimiento de conteos. La candidata debe demostrar que la priorización predictiva mejora el rendimiento respecto de esa programación. El aporte elegido consiste en decidir dónde y cuándo contar; el cálculo contable de merma y el diagnóstico automático de sus causas requieren un alcance distinto.

**Verificación propuesta.** Comparar la priorización predictiva con la programación vigente usando diferencias relevantes detectadas por hora de conteo, horas invertidas y cobertura. Mantener una muestra aleatoria o estratificada independiente del modelo para estimar el error general sin sesgar la medición hacia los productos de mayor riesgo. Las líneas base operativas, las metas y la definición de diferencia relevante quedan pendientes del perfilado y del protocolo de prueba. El 12,4 % es una cifra del Caso y no demuestra el rendimiento del modelo.

**Incorporación propuesta.** Servicio de existencias, Etapa 1. Preparar y validar datos durante los meses 1 a 12; evaluar en modo sombra durante la marcha blanca, meses 13 a 15; habilitar el uso operativo desde el mes 16, sujeto a resultados de aceptación. Completar ubicación arquitectónica, paquetes EDT y valorización al desarrollar la ficha T-19.

**Gobierno y contingencia.** La persona responsable aprueba la programación. El modelo no modifica saldos ni autoriza ajustes de inventario. Registrar recomendaciones y decisiones, evaluar sesgo y deriva, y permitir desactivar la priorización predictiva para volver a la programación parametrizada. La ficha formal debe responder al capítulo 18 de las Bases Transversales por incorporar IA.

## Pendientes para la ficha formal

- Confirmar los requisitos citados contra el catálogo vigente.
- Perfilar historial de conteos, ubicaciones, diferencias y horas de trabajo disponibles.
- Definir variables, modelo, versión, madurez y fuentes APA; seleccionar la tecnología con evidencia.
- Fijar protocolo, líneas base, metas y criterio de aceptación del piloto.
- Completar trazabilidad con arquitectura, EDT, cronograma y flujo de caja.
- Estimar inversión, costo operacional y beneficio sin atribuir toda la reducción de merma al modelo.

Esta nota registra la selección del equipo. El SD-13 y el Formulario T-19 ya tienen fuentes LaTeX; su consistencia con SD-04 y SD-07 y su validación siguen pendientes. La selección de cartera se conserva como decisión de origen.
