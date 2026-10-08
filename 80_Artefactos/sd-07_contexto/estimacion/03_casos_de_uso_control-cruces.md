# Casos de uso del Servicio de control de cruces (X-01), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Prefijo de casos: CC (Servicio de control de cruces). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2, Tablas 3.6 y 3.7, Anexo A y Anexo B (12 RF del servicio, Etapa 1). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-CC-01 | X-01 | Mantener el inventario de flujos de cruce autorizados | AH-15 | 3 | RF-168, RF-169; 3.3.2 | S2, S7 |
| CU-CC-02 | X-01 | Intentar una campaña con atributos de origen financiero | AH-13 | 2 | RF-170, RF-171; Tabla 3.7 | S3, S7 |
| CU-CC-03 | X-01 | Revisar los cruces ejecutados y los intentos bloqueados | AH-15 | 3 | RF-165 a RF-167 | S5, S7 |
| CU-CC-04 | X-01 | Intentar un proceso crediticio con atributos de origen Retail | AH-10 | 2 | RF-172 | S4, S7 |
| CU-CC-05 | X-01 | Resolver la correspondencia de identificadores entre ámbitos | AH-15 | 3 | RF-173 a RF-175 | S6, S7 |
| CU-CC-06 | X-01 | Evaluar el impacto de una iniciativa sobre la frontera de datos | AH-15 | 2 | RF-176 | S7 |

Resumen. 6 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 6 × 5 = 30.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-CC-01 | T1 declarar la interfaz con finalidad, base de licitud y autorización nominada, con rechazo si falta alguna. T2 aprobarla y versionarla. T3 consultar o retirar la interfaz del inventario |
| CU-CC-02 | T1 consultar el catálogo de atributos disponibles, sin atributos de origen financiero. T2 ejecutar la facilidad comercial con un atributo financiero y recibir el rechazo |
| CU-CC-03 | T1 consultar los cruces ejecutados. T2 consultar los intentos bloqueados, con el componente de origen, el dato solicitado y el instante. T3 tomar la muestra trimestral para auditoría |
| CU-CC-04 | T1 invocar un proceso crediticio con un atributo de Retail y recibir el rechazo. T2 consultar el motivo y la vía de autorización |
| CU-CC-05 | T1 solicitar una correspondencia de identificadores con acceso nominado. T2 consultar el registro de accesos a la tabla de correspondencia. T3 verificar que ninguna entidad de Retail persista la clave financiera |
| CU-CC-06 | T1 registrar la evaluación de impacto de la iniciativa. T2 aprobar la iniciativa, con rechazo si falta la evaluación |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | Los servicios que piden un cruce (Ventas a Crédito, Crédito a Ventas, Cartera a Posventa) son internos, no actores. Esas autorizaciones se cuentan una sola vez, en CU-VE-11 y en los casos de cartera de crédito |
| S2 | El «oficial de cumplimiento» de RF-168 se mapea a AH-15 (Contraloría y Cumplimiento) |
| S3 | El rechazo de Marketing de la Tabla 3.7 es CU-CC-02, con AH-13 como actor |
| S4 | CU-CC-04 es la contraparte de CU-CC-02. Su segunda transacción (consultar el motivo y la vía de autorización) es propuesta, porque RF-172 solo describe el rechazo |
| S5 | La muestra trimestral de CU-CC-03 T3 sale del resultado 22 del Anexo D, donde la hace el encargado de cumplimiento del cliente |
| S6 | RF-173 y RF-175 son reglas que el sistema aplica al crear identificadores. Se cuentan dentro de CU-CC-05 y no como casos propios |
| S7 | El sd-03 no describe este flujo en detalle. Las transacciones son propuestas |
| S8 | Los resultados 21 y 22 del Anexo D se rastrean aquí. El resultado 21 se prueba con el informe técnico y la prueba de penetración (RNF-11, RNF-14), que van a la EDT de seguridad y calidad |
| S9 | La política de retención de la bitácora de cruces es un requisito no funcional (Tabla 3.6). No hay RF que la administre, así que no se crea un caso. Queda como posible vacío del catálogo |

## 4. Cobertura de los 12 RF

RF-165, RF-166 y RF-167 en CU-CC-03. RF-168 y RF-169 en CU-CC-01. RF-170 y RF-171 en CU-CC-02. RF-172 en CU-CC-04. RF-173, RF-174 y RF-175 en CU-CC-05. RF-176 en CU-CC-06. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Decisiones del usuario (2026-10-08)

1. AH-15 es el oficial de cumplimiento de RF-168.
2. CU-CC-04 entra como contraparte de CU-CC-02, con la segunda transacción propuesta.
3. Los servicios internos que piden cruces no son actores.
4. La retención de la bitácora no genera un caso (S9).
