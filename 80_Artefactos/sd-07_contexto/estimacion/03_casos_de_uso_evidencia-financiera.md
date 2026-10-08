# Casos de uso del Servicio de evidencia financiera (F:C-03), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Prefijo de casos: EV (Servicio de evidencia financiera). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.1, 3.3.2 y 3.4.4, Anexo A y Anexo B (15 RF del servicio, Etapa 1). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-EV-01 | F:C-03 | Entregar la información precontractual del crédito | AH-10 | 2 | RF-199, RF-200, RF-201, RF-203; 3.4.4 | S4, S8 |
| CU-EV-02 | F:C-03 | Aceptar la información precontractual con firma electrónica | AH-02 | 2 | RF-202, RF-204 a RF-206; 3.4.4 | S1, S4, S8 |
| CU-EV-03 | F:C-03 | Registrar el consentimiento de una modificación de condiciones | AH-10 | 2 | RF-207, RF-208; 3.4.4 | S5, S8 |
| CU-EV-04 | F:C-03 | Reconstruir el acto de consentimiento | AH-15 | 2 | RF-209 | S8 |
| CU-EV-05 | F:C-03 | Recuperar los antecedentes de una operación desde el archivo | AH-15 | 2 | RF-210 | S8 |
| CU-EV-07 | F:C-03 | Enlazar la repactación con su cobranza y su consentimiento | AH-10 | 2 | RF-214, RF-215 | S5, S8 |
| CU-EV-08 | F:C-03 | Consultar la información precontractual del crédito | AS-04 | 1 | RF-217 | S2 |

Resumen. 7 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 7 × 5 = 35. El código CU-EV-06 queda sin uso, porque el caso se retiró.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-EV-01 | T1 entregar la información y registrar su versión, instante y medio. T2 acreditar la entrega y habilitar la evaluación de la solicitud |
| CU-EV-02 | T1 revisar el contenido de la información precontractual. T2 aceptar con firma electrónica y registrar el instante, el contenido o su huella y la constancia, con rechazo si no hay entrega previa acreditada |
| CU-EV-03 | T1 presentar la modificación y registrar el consentimiento con integridad verificable. T2 confirmar la modificación, con rechazo si falta la evidencia |
| CU-EV-04 | T1 consultar el acto de consentimiento por operación. T2 verificar la integridad del registro |
| CU-EV-05 | T1 solicitar la recuperación de una operación. T2 recibir los antecedentes dentro de 5 minutos |
| CU-EV-07 | T1 enlazar el expediente de la repactación con la gestión de cobranza. T2 enlazarlo con la evidencia de consentimiento |
| CU-EV-08 | T1 consultar la información precontractual del crédito |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | El titular de tarjeta (AH-02) es el actor de la aceptación, porque firma en pantalla. La firma electrónica es exigible en la apertura (RT-16.14, cita del Caso) |
| S2 | Portal público en la Opción A (D-08 y D-09 de `contexto_sd-04.md`). El contenido financiero se sirve desde la filial emisora. El cliente se conserva como actor por prudencia |
| S3 | CU-EV-06 (responder el requerimiento de la autoridad) se retiró el 2026-10-08 por la revisión independiente de G3. La autoridad solo recibe reportes (C6), EXC-06 no respalda el caso y el informe de cumplimiento por hito es un entregable de gestión del proyecto (sd-06). El resultado 23 se traza a otros casos (`04_trazabilidad_resultados.md`) |
| S4 | CU-EV-01 T2 y CU-EV-02 T2 son las compuertas que usa CU-OR-01 T3 para confirmar la apertura. No se cuentan dos veces |
| S5 | CU-EV-03 T2 es la compuerta que usan los casos de cartera de crédito en las repactaciones (resultado 18) |
| S6 | La retención de la evidencia (plazo del crédito más seis años) es un requisito no funcional. Ningún RF administra la retención, así que no se crea un caso. Queda como posible vacío del catálogo y se consulta al cliente |
| S7 | Los resultados 17, 18, 19, 20 y 28 del Anexo D se rastrean aquí y en originación de crédito o cartera de crédito |
| S8 | El sd-03 no describe este flujo en detalle. Las transacciones son propuestas |

## 4. Cobertura de los 15 RF

RF-199, RF-200, RF-201 y RF-203 en CU-EV-01. RF-202, RF-204, RF-205 y RF-206 en CU-EV-02. RF-207 y RF-208 en CU-EV-03. RF-209 en CU-EV-04. RF-210 en CU-EV-05. RF-214 y RF-215 en CU-EV-07. RF-217 en CU-EV-08. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Decisiones del usuario (2026-10-08)

1. El titular de tarjeta (AH-02) es el actor de CU-EV-02.
2. CU-EV-06 se retiró el 2026-10-08 (revisión independiente de G3, aprobada por el usuario).
3. La retención de la evidencia queda como vacío del catálogo y no se crea un caso (S6).
4. CU-EV-05 lo hace AH-15.
