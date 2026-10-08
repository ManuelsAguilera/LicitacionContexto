# Casos de uso del Servicio de ventas (R:V-02), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Prefijo de casos: VE (Servicio de ventas). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2, 3.4.4, 3.4.5 y Tabla 3.7, Anexo A y Anexo B (14 RF del servicio, Etapa 1). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-VE-01 | R:V-02 | Registrar y cobrar una venta | AH-04 | 3 | RF-001; 3.3.2 | S1, S3 |
| CU-VE-02 | R:V-02 | Reversar una venta o un pago | AH-04 | 2 | 3.3.2 | S1, S4 |
| CU-VE-03 | R:V-02 | Cerrar la caja del turno | AH-04 | 2 | 3.3.2 | S1, S4 |
| CU-VE-04 | R:V-02 | Operar la tienda sin enlace | AH-04 | 4 | RF-082 a RF-086; 3.4.5 | S1, S2, S6 |
| CU-VE-05 | R:V-02 | Reconciliar las ventas hechas sin enlace | AS-14 | 3 | RF-088, RF-095 a RF-097; 3.4.5 | S6 |
| CU-VE-06 | R:V-02 | Revisar el informe de excepciones de la conciliación | AH-16 | 2 | RF-099 | S4 |
| CU-VE-07 | R:V-02 | Validar las operaciones cursadas sin enlace | AH-10 | 2 | RF-094; EXC-16 | S5 |
| CU-VE-08 | R:V-02 | Desactivar los medios de pago de mayor fricción | AH-13 | 2 | RF-181 | S7 |
| CU-VE-09 | R:V-02 | Registrar las ventas del canal digital | AS-04 | 2 | 3.3.2 | S4 |
| CU-VE-10 | R:V-02 | Enrutar los documentos tributarios al ERP/DTE | AS-01 | 2 | RF-100; 3.3.2 | S4 |
| CU-VE-11 | R:V-02 | Cobrar con la tarjeta de la casa | AH-04 | 2 | 3.4.4; Tabla 3.7 | S5, S8 |

Resumen. 11 casos, 10 simples (1 a 3 transacciones) y 1 medio (CU-VE-04). UUCW provisional del servicio = 10 × 5 + 1 × 10 = 60.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-VE-01 | T1 registrar la venta, aunque la unidad tenga una reserva digital activa. T2 cobrar con el medio de pago elegido. T3 confirmar la venta |
| CU-VE-02 | T1 registrar la reversa de la venta o del pago. T2 confirmar el ajuste del documento en el ERP/DTE |
| CU-VE-03 | T1 consultar el resumen de caja del turno. T2 registrar el cierre y las diferencias |
| CU-VE-04 | T1 consultar el estado del enlace y de la sincronización. T2 registrar la venta en modo desconectado. T3 cobrar en modo desconectado. T4 emitir el documento en contingencia con folios previos |
| CU-VE-05 | T1 detectar el restablecimiento del enlace y volver a modo conectado. T2 reconciliar las ventas hacia los sistemas centrales. T3 reconciliar los documentos emitidos con el ERP/DTE |
| CU-VE-06 | T1 consultar el informe de excepciones. T2 consultar la regla aplicada a un conflicto |
| CU-VE-07 | T1 consultar las operaciones marcadas como cursadas sin enlace. T2 registrar la validación posterior |
| CU-VE-08 | T1 desactivar un medio de pago declarado. T2 reactivarlo |
| CU-VE-09 | T1 registrar la venta confirmada del canal digital. T2 consultar su estado |
| CU-VE-10 | T1 recibir la solicitud de emisión y devolver el documento o su estado. T2 entregar los folios de contingencia al punto de venta |
| CU-VE-11 | T1 solicitar la autorización de la compra al Emisor y recibir la decisión y su vigencia. T2 cerrar la venta con esa autorización |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | Las cajas son parte de la solución (nuevo punto de venta, sd-03 3.3.2), no un actor sistema |
| S2 | RF-085 (promociones en modo desconectado) no tiene transacción propia en CU-VE-04, porque la ida y vuelta ya está contada en CU-OF-09 T2. Se evita contarla dos veces |
| S3 | RF-001 (vender aunque haya una reserva digital) se cuenta aquí. El conflicto que resuelve el Servicio de existencias (RF-098) está en CU-EX-07, con otro objetivo |
| S4 | El sd-03 no describe este flujo en detalle o el caso no tiene RF (reversas, registros de caja y ventas del canal digital salen de 3.3.2). Las transacciones son propuestas |
| S5 | CU-VE-07 y CU-VE-11 dependen del crédito sin conexión (EXC-16, RT-03.13). Si la prueba de factibilidad falla, la función se declara no disponible y ambos casos se retiran. Tabla 3.7: la compra es condicionada |
| S6 | RF-082 y RF-088 (detectar y conmutar) las ejecuta el sistema. Sus idas y vueltas se cuentan como visibilidad del estado para el actor en CU-VE-04 T1 y CU-VE-05 T1 |
| S7 | RF-181 se asigna a AH-13 como «rol facultado» provisional, hasta que el sd-03 lo defina |
| S8 | Intercambios de la Tabla 3.7. «Compra» (dos filas, una sola operación) en CU-VE-11. «Pago/reversa» y «Reversa» siguen cerrados hasta aprobación y no se cuentan. El rechazo de Marketing es del Servicio de control de cruces |

## 4. Cobertura de los 14 RF

RF-001 en CU-VE-01. RF-082 a RF-086 en CU-VE-04. RF-088, RF-095, RF-096 y RF-097 en CU-VE-05. RF-094 en CU-VE-07. RF-099 en CU-VE-06. RF-100 en CU-VE-10. RF-181 en CU-VE-08. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Decisiones del usuario (2026-10-08)

1. CU-VE-11 se cuenta en ventas.
2. AH-10 valida las operaciones sin enlace (CU-VE-07).
3. AH-13 es el rol facultado para desactivar medios de pago (CU-VE-08).
4. RF-085 queda sin transacción propia (S2).
