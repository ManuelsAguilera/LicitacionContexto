# Casos de uso del Servicio de originación de crédito (F:C-01), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Prefijo de casos: OR (Servicio de originación de crédito). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2 y 3.4.4, Anexo A y Anexo B (14 RF del servicio, Etapa 1). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-OR-01 | F:C-01 | Evaluar la solicitud y abrir una tarjeta en el mostrador | AH-10 | 3 | RF-220 a RF-223, RF-225; 3.4.4 | S1, S2, S7 |
| CU-OR-02 | F:C-01 | Ofrecer la tarjeta y consultar el resultado | AH-03 | 2 | RF-224; 3.4.4 | S7 |
| CU-OR-03 | F:C-01 | Simular el costo total del crédito | AH-01 | 1 | RF-218 | S1 |
| CU-OR-04 | F:C-01 | Mantener la tasa máxima convencional vigente | AH-10 | 2 | RF-219 | S7 |
| CU-OR-05 | F:C-01 | Controlar los intentos de evaluación | AH-15 | 2 | RF-226 | S7 |
| CU-OR-06 | F:C-01 | Parametrizar los topes y la ventana de enfriamiento | AH-10 | 3 | RC-11; EXC-16 | S5 |
| CU-OR-07 | F:C-01 | Otorgar crédito sin enlace contra el cupo preaprobado | AH-04 | 3 | RF-090 a RF-093; EXC-16 | S3, S4 |
| CU-OR-08 | F:C-01 | Mantener el cupo preaprobado en la tienda | AS-14 | 2 | RF-089; EXC-16 | S3 |
| CU-OR-09 | F:C-01 | Solicitar la ampliación de un cupo con enlace | AH-10 | 2 | 3.3.2 | S6 |

Resumen. 9 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 9 × 5 = 45.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-OR-01 | T1 ingresar la solicitud del cliente. T2 evaluar y obtener la decisión y el cupo en 8 segundos o menos. T3 confirmar la apertura una vez acreditada la evidencia |
| CU-OR-02 | T1 iniciar la oferta de la tarjeta al cliente. T2 consultar el resultado de la evaluación, sin poder alterarlo |
| CU-OR-03 | T1 simular el costo total y la carga anual equivalente |
| CU-OR-04 | T1 cargar la tasa por tipo y tramo con su fecha de vigencia. T2 consultar la tasa vigente |
| CU-OR-05 | T1 consultar los intentos de evaluación por solicitante. T2 consultar el resultado de un intento |
| CU-OR-06 | T1 definir el tope de monto por operación. T2 definir el tope de número de operaciones. T3 definir la ventana de enfriamiento |
| CU-OR-07 | T1 consultar el cupo preaprobado en la caché local. T2 otorgar el crédito aplicando los topes de monto y de número. T3 recibir el rechazo de una apertura o de una ampliación sin enlace |
| CU-OR-08 | T1 enviar los cupos preaprobados y los topes vigentes a la tienda. T2 retirar los cupos con registro local vencido |
| CU-OR-09 | T1 ingresar la solicitud de ampliación. T2 evaluar y decidir |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | Portal público en la Opción A (D-08 y D-09 de `contexto_sd-04.md`). El contenido financiero se sirve desde la filial emisora. El cliente se conserva como actor por prudencia |
| S2 | CU-OR-01 T3 depende del Servicio de evidencia financiera. Los casos de la evidencia se cuentan en ese servicio, no aquí |
| S3 | CU-OR-07 y CU-OR-08 dependen de la factibilidad del crédito sin conexión (EXC-16, RT-03.13). Si la prueba falla, ambos se retiran. Se suman a CU-VE-07 y CU-VE-11 en la sensibilidad |
| S4 | CU-OR-07 es la vía desconectada. CU-VE-11 es la vía con enlace. Son casos distintos con objetivos distintos |
| S5 | CU-OR-06 cita RC-11 (el cliente fija el apetito de riesgo) y no un RF, porque RF-090 y RF-091 describen la aplicación de los topes y no su parametrización |
| S6 | CU-OR-09 no tiene RF. Sale de «administra solicitudes, evaluaciones, cupos» en 3.3.2 |
| S7 | El sd-03 no describe este flujo en detalle. Las transacciones son propuestas |
| S8 | No hay buró de crédito ni otra fuente externa de evaluación en el Caso. Si existe, faltaría un actor. Se pregunta al cliente al inicio del proyecto |
| S9 | Los resultados 16, 17, 20 y 28 del Anexo D se rastrean aquí y en el Servicio de evidencia financiera |

## 4. Cobertura de los 14 RF

RF-089 en CU-OR-08. RF-090 a RF-093 en CU-OR-07. RF-218 en CU-OR-03. RF-219 en CU-OR-04. RF-220 a RF-223 y RF-225 en CU-OR-01. RF-224 en CU-OR-02. RF-226 en CU-OR-05. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Decisiones del usuario (2026-10-08)

1. AH-10 ejecuta la evaluación en el mostrador (CU-OR-01).
2. CU-OR-09 se incluye como propuesta, aunque no tenga RF.
3. No se incluye un actor de buró de crédito mientras no se confirme su existencia (S8).
4. CU-OR-03 queda con una sola transacción.
