# Casos de uso del Servicio de cartera de crédito (C-02), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Prefijo de casos: CA (Servicio de cartera de crédito). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.1, 3.3.2 y 3.4.4, Anexo A y Anexo B (6 RF del servicio, etapas 1 y 2). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-CA-01 | C-02 | Iniciar y registrar una gestión de cobranza | AH-10 | 2 | RF-211 a RF-213 | S8 |
| CU-CA-02 | C-02 | Repactar las condiciones de una deuda | AH-10 | 2 | 3.3.2; 3.4.4 | S1, S2 |
| CU-CA-03 | C-02 | Consultar el estado de cuenta y los documentos | AH-02 | 2 | RF-069, RF-070 | S3 |
| CU-CA-04 | C-02 | Registrar el pago de una cuota | AH-10 | 2 | 3.3.2 | S1, S4, S5 |
| CU-CA-05 | C-02 | Calcular la mora y actualizar las cuentas | AS-14 | 2 | 3.3.2 | S1 |
| CU-CA-06 | C-02 | Revisar la conciliación diaria de la migración | AH-10 | 3 | RF-216; 3.4.4 | S6, S7 |
| CU-CA-07 | C-02 | Convivir con la plataforma de crédito de 2011 | AS-10 | 3 | 3.3.1; 3.4.4 | S1, S6 |

Resumen. 7 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 7 × 5 = 35.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-CA-01 | T1 iniciar la gestión de cobranza sobre una cuenta, con rechazo fuera de los límites normativos de horario y medio. T2 registrar la gestión ejecutada con medio, instante y ejecutor |
| CU-CA-02 | T1 proponer las nuevas condiciones sobre la cuenta. T2 registrar la repactación una vez acreditado el consentimiento (la compuerta es la segunda transacción de CU-EV-03) |
| CU-CA-03 | T1 consultar el estado de cuenta. T2 consultar los documentos de la cuenta |
| CU-CA-04 | T1 registrar el pago. T2 aplicarlo a las cuotas e informar el saldo |
| CU-CA-05 | T1 calcular la mora y actualizar saldos y cuotas. T2 marcar las cuentas que requieren gestión de cobranza |
| CU-CA-06 | T1 consultar el reporte de conciliación por tramo. T2 registrar la explicación de una diferencia. T3 autorizar o detener el avance del tramo |
| CU-CA-07 | T1 recibir los saldos y movimientos del tramo. T2 enviar las operaciones nuevas durante la convivencia. T3 ejecutar el retorno ensayado |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | CU-CA-02, CU-CA-04, CU-CA-05 y CU-CA-07 no tienen RF. Salen de 3.3.2 («cuentas, saldos, cuotas, pagos, mora, cobranza y modificaciones») y de 3.4.4 (olas conciliadas y retorno ensayado). Las transacciones son propuestas |
| S2 | CU-CA-02 usa la compuerta de CU-EV-03 T2. No cuenta dos veces la consulta de evidencia (resultado 18) |
| S3 | CU-CA-03 es de la Etapa 2 (portal del cliente) y depende de la Opción A del portal y del contenido financiero servido desde el Emisor (D-08 y D-09 de `contexto_sd-04.md`). AH-02 se conserva como actor por prudencia |
| S4 | Los pagos los registra AH-10 en el mesón financiero. «Pago/reversa» de la Tabla 3.7 sigue cerrado hasta su aprobación, así que el pago en caja con cruce a Retail no se cuenta |
| S5 | La imputación de pagos (RN-42) es un vacío conocido del catálogo y queda fuera |
| S6 | La migración de datos de 620.000 clientes va fuera del método (rama 6 de la EDT). Aquí solo cuenta lo funcional: la conciliación y la convivencia |
| S7 | Los resultados 18, 23 y 24 del Anexo D se rastrean aquí y en evidencia financiera. Los hitos de remediación (resultado 23) se rastrean en `04_trazabilidad_resultados.md` |
| S8 | EXC-06: no se opera la cobranza judicial. Sí se registra el expediente trazable, dentro de CU-CA-01 |

## 4. Cobertura de los 6 RF

RF-069 y RF-070 en CU-CA-03. RF-211, RF-212 y RF-213 en CU-CA-01. RF-216 en CU-CA-06. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Decisiones del usuario (2026-10-08)

1. AH-10 registra los pagos en el mesón financiero (CU-CA-04).
2. El cálculo de mora (CU-CA-05) entra como propuesta.
3. El caso de convivencia con AS-09 va en la base tecnológica, no repartido entre servicios.
4. Se agrega al verificador la comprobación de actores de la lista sin ningún caso.
