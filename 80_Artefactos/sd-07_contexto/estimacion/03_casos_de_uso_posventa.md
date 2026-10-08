# Casos de uso del Servicio de posventa (CL-01), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo, pendiente del visto bueno del usuario y de la firma del equipo. Prefijo de casos: PV (Servicio de posventa). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2, Anexo B (12 RF del servicio, Etapa 2) y Anexo D (resultado 15). La garantía legal se resuelve en el mesón sin derivar al cliente. Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-PV-01 | R:CL-01 | Atender un caso de garantía legal íntegramente en el mesón | AH-09 | 2 | RF-187, RF-188 | S1 |
| CU-PV-02 | R:CL-01 | Ofrecer y registrar la opción de garantía legal | AH-09 | 3 | RF-192 a RF-194 | S2 |
| CU-PV-03 | R:CL-01 | Parametrizar el plazo de garantía legal por tipo de producto | AH-11 | 2 | RF-195 | S3 |
| CU-PV-04 | R:CL-01 | Reingresar una unidad devuelta según su aptitud | AH-09 | 3 | RF-189 a RF-191 | S4 |
| CU-PV-05 | R:CL-01 | Seguir la resolución al consumidor y la recuperación contra el tercero | AH-09 | 3 | RF-196 a RF-198 | S5 |

Resumen. 5 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 5 × 5 = 25.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-PV-01 | T1 abrir el caso de garantía legal sin exigir derivación al fabricante, al servicio técnico ni al vendedor de marketplace. T2 resolver y cerrar el caso en el mesón |
| CU-PV-02 | T1 presentar las tres opciones (reparación, reposición y devolución del precio). T2 registrar la opción ofrecida. T3 registrar la opción elegida por el consumidor |
| CU-PV-03 | T1 definir el plazo de garantía por tipo de producto sin modificar código. T2 consultar los plazos vigentes y su historial |
| CU-PV-04 | T1 registrar la devolución con su motivo. T2 intentar el reingreso sin decisión de aptitud y recibir el rechazo. T3 registrar la decisión de aptitud, con responsable e instante, y reingresar la unidad |
| CU-PV-05 | T1 registrar el hito de resolución al consumidor con su fecha. T2 registrar el hito de recuperación contra el tercero con fecha independiente. T3 cerrar la resolución sin condicionarla al estado de la recuperación |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | Los 12 RF salen del Anexo B y todos tienen caso. El actor AH-09 atiende en el mesón. Un cliente que reclama por el portal (Opción A) no tiene RF y no se cuenta |
| S2 | Las tres opciones se presentan en una transacción y se registran dos (ofrecida y elegida), porque RF-193 y RF-194 son registros distintos con distinto instante |
| S3 | AH-11 (Comercial y compras) parametriza el plazo. El actor exacto está por validar |
| S4 | El reingreso al inventario disponible se informa a existencias. Ese movimiento se cuenta en el caso de recepción de movimientos de existencias y no se repite |
| S5 | La recuperación contra el tercero es un registro paralelo. La gestión con el fabricante o el vendedor externo queda fuera (RF-198) |
| S6 | El resultado 15 del Anexo D (cero derivaciones) se rastrea en CU-PV-01 |
| S7 | Actores secundarios: AS-03 y AS-04 solo como origen de la compra en canal digital, sin caso propio |

## 4. Cobertura de los RF

Cada RF del servicio está en un solo caso, según la columna Origen. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Preguntas abiertas (con sugerencia), pendientes del visto bueno del usuario

1. ¿AH-11 parametriza el plazo de garantía? Sugerencia: sí, mientras el catálogo no nombre otro rol; el conteo no cambia.
2. ¿Se agrega un caso de solicitud de devolución por el cliente en el portal? Sugerencia: no por ahora; no hay RF y depende de la Opción A del portal.
3. ¿La garantía de un producto de marketplace se atiende aquí (RF-188)? Sugerencia: sí, en el mesón, con la devolución al vendedor registrada en marketplace (CU-MK-07).
