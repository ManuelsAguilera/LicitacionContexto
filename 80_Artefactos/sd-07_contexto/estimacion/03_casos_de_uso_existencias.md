# Casos de uso del Servicio de existencias (R:M-03), muestra de la puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: muestra aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Prefijo de casos: EX (Servicio de existencias). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2 y 3.4.1, Anexo A y Anexo B (48 RF del servicio, Etapa 1). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-EX-01 | R:M-03 | Consultar la disponibilidad para vender en sala | AH-03 | 2 | RF-087, RF-101, RF-161 | S2, S7 |
| CU-EX-02 | R:M-03 | Consultar la disponibilidad en línea | AH-01 | 2 | RF-065, RF-066, RF-160 | S1, S7 |
| CU-EX-03 | R:M-03 | Publicar el disponible a los canales | AS-04 | 3 | RF-127 a RF-129, RF-157; 3.4.1 | S3, S7 |
| CU-EX-04 | R:M-03 | Reservar una unidad para el canal digital | AS-04 | 4 | RF-035, RF-037, RF-038, RF-041; 3.4.1 | S3 |
| CU-EX-05 | R:M-03 | Expirar las reservas vencidas | AS-14 | 2 | RF-039, RF-040, RF-042 | S4 |
| CU-EX-06 | R:M-03 | Verificar la existencia física antes del cobro | AH-06 | 3 | RF-044; 3.4.1 | S5 |
| CU-EX-07 | R:M-03 | Resolver el conflicto de existencia comprometida | AH-04 | 2 | RF-098 | S6 |
| CU-EX-08 | R:M-03 | Parametrizar el colchón de confianza y la vigencia de la reserva | AH-12 | 4 | RF-036, RF-149 a RF-152 | S8, S9 |
| CU-EX-09 | R:M-03 | Consultar la traza del cálculo del disponible | AH-15 | 2 | RF-130 | S9 |
| CU-EX-10 | R:M-03 | Parametrizar el conteo cíclico | AH-12 | 3 | RF-131 a RF-133 | S8, S9 |
| CU-EX-11 | R:M-03 | Ejecutar el conteo cíclico | AH-06 | 3 | RF-134 a RF-136 | S9 |
| CU-EX-12 | R:M-03 | Consultar la exactitud del inventario y recibir alertas | AH-05 | 3 | RF-137, RF-158, RF-159, RF-162 | S9 |
| CU-EX-13 | R:M-03 | Clasificar las diferencias y cerrar el ajuste | AH-14 | 3 | RF-138, RF-139 | S9 |
| CU-EX-14 | R:M-03 | Emitir el informe mensual de merma | AH-14 | 2 | RF-140, RF-141 | S9 |
| CU-EX-15 | R:M-03 | Gestionar las unidades en el probador | AH-03 | 3 | RF-153 a RF-156 | S9 |
| CU-EX-16 | R:M-03 | Suspender la publicación de una categoría | AH-12 | 2 | RF-163, RF-164 | S8, S9 |
| CU-EX-17 | R:M-03 | Degradar por cancelaciones | AS-14 | 2 | RF-179, RF-182, RF-183 | S4, S9, S10 |
| CU-EX-18 | R:M-03 | Recibir los movimientos del sistema de almacenes | AS-02 | 3 | EXC-12; 3.3.2 | S9 |
| CU-EX-19 | R:M-03 | Cargar las existencias de Concepción | AH-07 | 3 | EXC-13, SP-02, RC-10 | S9, S11 |

Resumen. 19 casos, 17 simples (1 a 3 transacciones) y 2 medios (CU-EX-04 y CU-EX-08). UUCW provisional del servicio = 17 × 5 + 2 × 10 = 105.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-EX-01 | T1 consultar la disponibilidad de la referencia en la tienda y recibir cantidad y error probable. T2 consultar contra la existencia local en modo desconectado |
| CU-EX-02 | T1 consultar la disponibilidad por tienda. T2 consultar la disponibilidad para despacho |
| CU-EX-03 | T1 recalcular y publicar tras un movimiento. T2 responder la consulta de disponible de un canal. T3 republicar tras reconectarse un canal |
| CU-EX-04 | T1 crear la reserva o recibir su rechazo por doble compromiso. T2 renovar por actividad. T3 confirmar al comprometerse el pedido. T4 liberar de inmediato |
| CU-EX-05 | T1 liberar la reserva expirada y devolver la unidad al disponible. T2 aplicar la vigencia reducida del evento anual |
| CU-EX-06 | T1 solicitar la verificación y confirmar la presencia de la unidad. T2 informar la unidad no encontrada. T3 registrar la diferencia detectada |
| CU-EX-07 | T1 registrar la venta física de una unidad con reserva digital y aplicar la precedencia. T2 consultar el resultado de la resolución |
| CU-EX-08 | T1 definir el colchón por categoría. T2 definir el colchón por punto. T3 definir la vigencia de la reserva. T4 consultar la sugerencia de referencia y el historial de cambios |
| CU-EX-09 | T1 consultar la traza por referencia y punto. T2 consultar la versión de parámetros aplicada |
| CU-EX-10 | T1 definir la frecuencia por categoría. T2 definir el método. T3 definir el criterio de gatillo |
| CU-EX-11 | T1 obtener la programación asignada. T2 registrar el resultado del conteo. T3 recibir la señal de recuento extraordinario |
| CU-EX-12 | T1 consultar la exactitud por categoría. T2 consultar el error probable por referencia y punto. T3 recibir la alerta bajo el umbral |
| CU-EX-13 | T1 registrar la diferencia detectada. T2 clasificarla en un componente de merma. T3 cerrar el ajuste, con rechazo si falta el componente |
| CU-EX-14 | T1 consultar monto y proporción por componente. T2 emitir el informe mensual |
| CU-EX-15 | T1 registrar el ingreso al probador. T2 confirmar el reingreso a sala. T3 registrar la venta de la unidad |
| CU-EX-16 | T1 suspender manualmente la categoría. T2 consultar la regla de degradación declarada |
| CU-EX-17 | T1 monitorear la tasa y activar la acción de degradación declarada. T2 suspender la categoría según el orden declarado |
| CU-EX-18 | T1 recibir el movimiento de recepción o ubicación. T2 recibir el de preparación o despacho. T3 recibir el de ajuste |
| CU-EX-19 | T1 cargar el registro estructurado. T2 recibir los rechazos de validación. T3 publicar el nodo con su confianza declarada |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | RF-065 y RF-066 nombran al cliente no autenticado, por eso es actor directo. La consulta puede pasar por la plataforma de comercio electrónico y eso cambiaría el actor a AS-04 |
| S2 | RF-087 es un flujo alternativo que agrega una ida y vuelta contra la existencia local, por eso se cuenta como T2 |
| S3 | La reserva y la publicación las pide la plataforma de comercio electrónico (AS-04), no el cliente directo, porque el canal digital es una plataforma conservada |
| S4 | El actor es el temporizador (AS-14). La vigencia reducida del evento anual (RF-042) es un ciclo distinto del normal |
| S5 | RF-044 no nombra a quién verifica. Se asigna a AH-06 hasta que el sd-03 4.x lo defina |
| S6 | La precedencia de RF-098 se dispara por la venta física del cajero (RN-10, RN-48) |
| S7 | El error probable se muestra junto a la disponibilidad. RF-160 y RF-161 citan RF-058, referencia obsoleta del catálogo |
| S8 | El «gerente de logística» de los RF de parámetros se mapea a AH-12 (planificación de abastecimiento) |
| S9 | El sd-03 no describe este flujo. Las transacciones son propuestas |
| S10 | RF-183 cita RF-026.1, referencia obsoleta del catálogo |
| S11 | El personal de Concepción (100 personas) es parte de AH-07. No se instalan componentes allí (EXC-13) y la carga es un registro estructurado |

## 4. Cobertura de los 48 RF

Cada RF del servicio aparece en un solo caso: RF-035 a RF-042 (excepto RF-036) en CU-EX-04 y CU-EX-05, RF-036 en CU-EX-08, RF-044 en CU-EX-06, RF-065 y RF-066 en CU-EX-02, RF-087 y RF-101 en CU-EX-01, RF-098 en CU-EX-07, RF-127 a RF-129 y RF-157 en CU-EX-03, RF-130 en CU-EX-09, RF-131 a RF-136 en CU-EX-10 y CU-EX-11, RF-137, RF-158, RF-159 y RF-162 en CU-EX-12, RF-138 a RF-141 en CU-EX-13 y CU-EX-14, RF-149 a RF-152 en CU-EX-08, RF-153 a RF-156 en CU-EX-15, RF-160 y RF-161 en CU-EX-02 y CU-EX-01, RF-163 y RF-164 en CU-EX-16, RF-179, RF-182 y RF-183 en CU-EX-17. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Fuera de los casos de uso

OP-08 y OP-09 (análisis de Concepción y su impacto sobre RN-15) son entregables de análisis y van a la EDT, no al modelo. La conciliación del inventario contable con el sistema de gestión empresarial no tiene RF. Queda como supuesto: no se cuenta ahora y se pregunta al equipo.

## 6. Decisiones del usuario (2026-10-08)

1. CU-EX-08 y CU-EX-10 quedan como casos separados.
2. AH-06 verifica la existencia física (S5) hasta que el sd-03 lo defina.

## 7. Preguntas para el equipo

1. ¿El cliente es actor directo (S1) o siempre llega por la plataforma del canal? Actor directo es el que se comunica con la solución sin pasar por otro sistema que sea actor. Sugerencia: mantenerlo directo mientras los RF-065 y RF-066 nombren al cliente. El UAW no cambia con ninguna de las dos opciones.
2. ¿Se cuenta la conciliación contable? Es la comprobación periódica de que la cantidad de unidades del Servicio de existencias coincide con el inventario valorizado del ERP/DTE. Ningún RF la pide, y el sd-03 3.3.2 dice que el ERP/DTE es el registro contable. Sugerencia: dejarla fuera de la muestra, y si el equipo la incluye sería un caso con AS-01, de 2 o 3 transacciones y peso 5.
