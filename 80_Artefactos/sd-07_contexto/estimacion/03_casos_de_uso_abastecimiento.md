# Casos de uso del Servicio de abastecimiento (M-02), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo. Las dudas se resolvieron el 2026-10-08 adoptando la sugerencia de cada pregunta (sección 5), a pedido del usuario. Pendiente de la firma del equipo. Prefijo de casos: AB (Servicio de abastecimiento). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2, Anexo A y Anexo B (3 RF del servicio, Etapa 2). El sd-03 describe el servicio como administrador de órdenes, transferencias, propuestas de reposición y recepciones. Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-AB-01 | R:M-02 | Generar la propuesta diaria de reposición | AS-14 | 2 | RF-144 | S2 |
| CU-AB-02 | R:M-02 | Ajustar y confirmar la propuesta de reposición | AH-12 | 3 | RF-145, RF-146 | S2 |
| CU-AB-03 | R:M-02 | Colocar y seguir las órdenes a proveedores | AH-12 | 3 | 3.3.2 | S1, S3, S4 |
| CU-AB-04 | R:M-02 | Gestionar las transferencias entre tiendas y centros de distribución | AH-12 | 3 | 3.3.2 | S1, S5 |
| CU-AB-05 | R:M-02 | Registrar la recepción de mercadería en la tienda | AH-06 | 2 | 3.3.2 | S1, S6 |

Resumen. 5 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 5 × 5 = 25.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-AB-01 | T1 calcular la propuesta de reposición con el disponible para vender de existencias. T2 publicar la propuesta a los planificadores |
| CU-AB-02 | T1 consultar la propuesta del día. T2 ajustar las cantidades, con registro de usuario, valor propuesto, valor confirmado e instante. T3 confirmar el envío |
| CU-AB-03 | T1 generar la orden desde la propuesta confirmada y enviarla al ERP/DTE. T2 consultar el estado de la orden. T3 registrar la respuesta del proveedor |
| CU-AB-04 | T1 proponer la transferencia entre nodos. T2 confirmarla y enviarla al WMS principal. T3 seguirla hasta su recepción |
| CU-AB-05 | T1 registrar la recepción contra la orden o la transferencia. T2 registrar las diferencias de recepción y cerrar la recepción |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | CU-AB-03 a CU-AB-05 no tienen RF. Salen de 3.3.2 («órdenes, transferencias, propuestas de reposición y recepciones»). Sus transacciones son propuestas |
| S2 | El disponible para vender (RF-127) se calcula en existencias y aquí solo se consume. No se cuenta dos veces |
| S3 | Las órdenes pasan por el ERP/DTE, que mantiene el registro contable (EXC-01). El servicio no emite documentos tributarios |
| S4 | El canal con los proveedores (AS-13, tipo 2) sigue por validar en el sd-04. La respuesta del proveedor se cuenta una vez, en CU-AB-03 |
| S5 | La ejecución física (ubicación, preparación, despacho) sigue en el WMS principal (EXC-12). Aquí solo se cuenta la decisión y el seguimiento |
| S6 | La recepción en el centro de distribución principal ocurre en el WMS y llega a existencias como movimiento (CU-EX-18). CU-AB-05 cubre la recepción en tienda. Concepción entrega sus existencias por CU-EX-19 y no se cuenta aquí (SP-02) |
| S7 | Actores secundarios: AS-01 (órdenes) y AS-02 (transferencias) en CU-AB-03 y CU-AB-04; AS-13 en CU-AB-03 |

## 4. Cobertura de los RF

Cada RF del servicio está en un solo caso, según la columna Origen. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Decisiones adoptadas por sugerencia (2026-10-08), pendientes de la firma del equipo

1. ¿La recepción en tienda la registra AH-06? Decisión adoptada: sí, es el personal de reposición y bodega de tienda; si la tienda recibe por WMS, el caso baja a 1 transacción y se funde con CU-AB-04.
2. ¿Las transferencias entre tiendas y centros entran como caso propio (CU-AB-04)? Decisión adoptada: sí, 3.3.2 las nombra como parte del servicio.
3. ¿El sistema genera la orden al proveedor o solo la propone al ERP? Decisión adoptada: que la genere el servicio y la entregue al ERP/DTE, que sigue siendo el registro contable.
