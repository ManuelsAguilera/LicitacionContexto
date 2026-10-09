# Casos de uso del Servicio de pedidos (V-01), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo. Las dudas se resolvieron el 2026-10-08 adoptando la sugerencia de cada pregunta (sección 5), a pedido del usuario. Pendiente de la firma del equipo. Prefijo de casos: PE (Servicio de pedidos). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2, Anexo A, Anexo B (31 RF del servicio, Etapa 2) y Anexo D (resultados 3, 10, 11, 26). Bajo la Opción A del portal, el sitio y la app de comercio electrónico existentes (AS-04) presentan al cliente y la solución entrega los datos. Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-PE-01 | R:V-01 | Calcular la fecha prometida de entrega | AS-04 | 2 | RF-075, RF-079, RF-080 | S2, S3 |
| CU-PE-02 | R:V-01 | Seleccionar el punto de despacho por costo total de servir | AS-04 | 1 | RF-076 a RF-078 | S4 |
| CU-PE-03 | R:V-01 | Aceptar el pedido y preautorizar el medio de pago | AS-04 | 2 | RF-043 | S5 |
| CU-PE-04 | R:V-01 | Capturar el cobro al confirmarse la preparación | AS-02 | 3 | RF-045, RF-047, RF-051 | S5, S6 |
| CU-PE-05 | R:V-01 | Resolver un pedido cuya unidad no existe | AH-07 | 2 | RF-046 | S7 |
| CU-PE-06 | R:V-01 | Reasignar el pedido a otro punto de despacho | AH-07 | 2 | RF-056 a RF-058 | S7 |
| CU-PE-07 | R:V-01 | Ofrecer al cliente las alternativas de resolución | AH-09 | 2 | RF-059 a RF-061, RF-074 | S8 |
| CU-PE-08 | R:V-01 | Cancelar el pedido y anular la preautorización | AH-09 | 2 | RF-048, RF-049 | S5 |
| CU-PE-09 | R:V-01 | Conciliar las preautorizaciones vencidas sin captura | AS-14 | 1 | RF-050 | S5 |
| CU-PE-10 | R:V-01 | Consultar el estado único del pedido | AS-04 | 2 | RF-052 | S9 |
| CU-PE-11 | R:V-01 | Consultar las compras y las devoluciones | AS-04 | 2 | RF-067, RF-068 | S9 |
| CU-PE-12 | R:V-01 | Atender en el mesón la consulta de un pedido | AH-09 | 2 | RF-072, RF-073 | S9 |
| CU-PE-13 | R:V-01 | Priorizar los pedidos próximos a vencer su promesa | AS-14 | 3 | RF-062, RF-063, RF-081 | S10 |
| CU-PE-14 | R:V-01 | Parametrizar la elegibilidad del stock y el límite por cliente | AH-13 | 2 | RF-053, RF-180 | S11 |
| CU-PE-15 | R:V-01 | Seguir el pedido con el transportista hasta la entrega | AS-07 | 3 | 3.3.2; EXC-07 | S1, S12 |

Resumen. 15 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 15 × 5 = 75.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-PE-01 | T1 solicitar la fecha prometida de un pedido candidato, con exclusión de Concepción y sin plazo fijo de catálogo. T2 confirmar la promesa al aceptar el pedido |
| CU-PE-02 | T1 calcular el costo total de servir de cada punto candidato, seleccionar el menor y registrar el valor de cada término que fundamentó la selección |
| CU-PE-03 | T1 aceptar el pedido y preautorizar el medio de pago sin capturar el cobro. T2 devolver el resultado de la preautorización o su rechazo |
| CU-PE-04 | T1 recibir el evento de confirmación de la preparación física. T2 notificar al cliente el cambio de estado y obtener su aceptación explícita cuando corresponde. T3 capturar el cobro |
| CU-PE-05 | T1 informar que la unidad no está disponible al preparar el pedido. T2 determinar la alternativa según el motor de reglas (cancelar, sustituir, derivar a tercero o entrega diferida) |
| CU-PE-06 | T1 reasignar el pedido a un punto con existencia disponible, con rechazo de una segunda reasignación o fuera de la ventana parametrizada. T2 confirmar la nueva promesa |
| CU-PE-07 | T1 ofrecer las alternativas (producto equivalente, espera compensada o liberación del pedido con anulación de la preautorización). T2 registrar la alternativa elegida |
| CU-PE-08 | T1 cancelar el pedido registrando el motivo. T2 anular la preautorización del pago |
| CU-PE-09 | T1 generar la conciliación diaria de preautorizaciones vencidas e informar el resultado a ventas |
| CU-PE-10 | T1 consultar el estado del pedido desde la fuente única. T2 consultar el historial de cambios de estado |
| CU-PE-11 | T1 consultar las compras del cliente autenticado. T2 consultar sus devoluciones |
| CU-PE-12 | T1 consultar el estado real del pedido. T2 consultar el precio aplicado al pedido |
| CU-PE-13 | T1 monitorear el tiempo restante de cada pedido. T2 priorizar la preparación al alcanzar el umbral parametrizado. T3 calcular el cumplimiento de la promesa por pedido individual |
| CU-PE-14 | T1 marcar el stock de exhibición de las categorías declaradas como no elegible para cumplimiento digital. T2 reducir el límite de unidades por cliente al valor declarado |
| CU-PE-15 | T1 recibir el retiro del pedido por el transportista. T2 recibir el avance de la entrega. T3 recibir la confirmación o la falla de entrega |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | CU-PE-15 no tiene RF. Sale de 3.3.2 («coordina canales, tiendas, centros de distribución y transportistas hasta el retiro o la entrega») y de EXC-07 (integrar a los transportistas y trazar el pedido hasta la entrega). Sus transacciones son propuestas |
| S2 | Bajo la Opción A, AS-04 (comercio electrónico existente) consulta la promesa por interfaz de programación. Las consultas del cliente (CU-PE-10 y CU-PE-11) también las hace AS-04. AH-01 sale del UAW base (sensibilidad en `02_actores_uaw.md`) |
| S3 | RF-075 excluye a Concepción como origen de promesa digital (SP-02). Se cuenta dentro de CU-PE-01 y no como caso aparte |
| S4 | CU-PE-02 y CU-PE-01 son llamadas de AS-04 al servicio. La reserva de existencia que el servicio solicita a existencias se cuenta allí, no aquí (resultado 11) |
| S5 | El procesador de pagos (AS-08, tipo 1) es actor secundario de CU-PE-03, CU-PE-04, CU-PE-08 y CU-PE-09. La respuesta del procesador se cuenta en la transacción que la origina, sin caso propio |
| S6 | El evento de confirmación de preparación (RF-045) lo origina el WMS (AS-02), que es el actor principal. RF-047 y RF-051 se cuentan dentro de CU-PE-04 porque ocurren antes del cobro (resultado 3) |
| S7 | El actor de CU-PE-05 y CU-PE-06 es AH-07 (personal de centros de distribución). Si la preparación ocurre en tienda, el actor es AH-06 y el conteo no cambia |
| S8 | CU-PE-07 reúne las tres alternativas de RF-059 a RF-061 y la oferta en el mesón de RF-074 en una sola presentación. Se unifica el criterio con CU-PE-03 y CU-PV-02: presentar opciones es una ida y vuelta, no una por opción. La segunda transacción es registrar la elegida |
| S9 | La consulta del cliente se sirve a AS-04 (Opción A). Las tres consultas (CU-PE-10, 11 y 12) comparten la fuente única (resultado 10) y no se cuentan dos veces |
| S10 | El umbral de tiempo restante (RF-063) es un parámetro del servicio y no genera caso de administración aparte |
| S11 | RF-053 y RF-180 son parámetros de configuración que usa el evento anual. Se reúnen en un caso porque ambos los declara AH-13 antes del evento |
| S12 | Los transportistas (AS-07) no tienen interfaz definida en el sd-03. Se tratan como tipo 1 por C5 (interfaz objetivo) |
| S13 | Revisión independiente de G3 (2026-10-08): no se cuentan como transacciones los pasos internos que no son una ida y vuelta con el actor (el registro de los términos del costo en CU-PE-02 y el informe a ventas en CU-PE-09). El cliente (AH-01) recibe la notificación de CU-PE-04 por el canal de AS-04 y no es actor |

## 4. Cobertura de los RF

Cada RF del servicio está en un solo caso, según la columna Origen. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Decisiones adoptadas por sugerencia (2026-10-08), pendientes de la firma del equipo

1. ¿AS-04 es el actor principal de las consultas y los cálculos de la promesa bajo la Opción A? Decisión adoptada: sí, también en las consultas (CU-PE-10 y CU-PE-11). AH-01 sale del UAW base por la Opción A firmada (revisión independiente de G3).
2. ¿CU-PE-05 y CU-PE-06 usan a AH-07 o a un actor de tienda? Decisión adoptada: AH-07 como principal y AH-06 como secundario; el conteo no cambia.
3. ¿Los 15 casos de pedidos son una granularidad aceptable para 31 RF? Decisión adoptada: sí; agrupar más baja CU y deja casos de más de 12 transacciones (C8).
4. ¿Se quiere un caso de administración de las reglas del motor de resolución (RF-046)? Decisión adoptada: no por ahora; no hay RF y entra con la parametrización de RF-063.
5. ¿El seguimiento con el transportista (CU-PE-15) cuenta como caso del servicio? Decisión adoptada: sí; EXC-07 pide trazar el pedido hasta la entrega.
