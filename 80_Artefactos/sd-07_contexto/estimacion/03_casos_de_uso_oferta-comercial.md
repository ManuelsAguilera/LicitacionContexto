# Casos de uso del Servicio de oferta comercial (R:M-01), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Prefijo de casos: OF (Servicio de oferta comercial). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2 y 3.4.2, Anexo A y Anexo B (20 RF del servicio, Etapa 1). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-OF-01 | R:M-01 | Cambiar y propagar un precio | AH-11 | 3 | RF-016, RF-018, RF-030; 3.4.2 | S2, S3, S4 |
| CU-OF-02 | R:M-01 | Entregar la oferta vigente a los canales | AS-04 | 4 | RF-017; 3.3.2 | S4 |
| CU-OF-03 | R:M-01 | Consultar el precio vigente en línea | AH-01 | 1 | RF-064 | S1 |
| CU-OF-04 | R:M-01 | Registrar el cambio de etiqueta | AH-06 | 2 | RF-019, RF-020 | S6 |
| CU-OF-05 | R:M-01 | Consultar el estado de exhibición de la tienda | AH-05 | 2 | RF-029 | S4 |
| CU-OF-06 | R:M-01 | Recuperar el precio publicado en un instante | AH-15 | 2 | RF-021 | S6 |
| CU-OF-07 | R:M-01 | Resolver el precio a cobrar ante diferencia con la etiqueta | AH-04 | 3 | RF-022, RF-023, RF-028 | S5 |
| CU-OF-08 | R:M-01 | Revisar los incidentes de discrepancia de precio | AH-05 | 2 | RF-024 | S5, S8 |
| CU-OF-09 | R:M-01 | Aplicar las promociones vigentes en la venta | AH-04 | 2 | RF-032 a RF-034 | S2, S4 |
| CU-OF-10 | R:M-01 | Administrar las promociones y su vigencia | AH-11 | 3 | 3.3.2; 3.4.2 | S3, S4 |
| CU-OF-11 | R:M-01 | Mantener el maestro de artículos | AH-11 | 3 | RF-142, RF-143 | S3 |
| CU-OF-12 | R:M-01 | Revisar los reportes de calidad del maestro y de publicación | AH-11 | 2 | RF-147, RF-148 | S3 |

Resumen. 12 casos, 11 simples (1 a 3 transacciones) y 1 medio (CU-OF-02). UUCW provisional del servicio = 11 × 5 + 1 × 10 = 65.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-OF-01 | T1 registrar el cambio de precio aprobado con su vigencia. T2 consultar la propagación por destino (cajas, canal digital y puntos de exhibición). T3 definir las ventanas de cambio de sala fuera del horario de atención |
| CU-OF-02 | T1 publicar el cambio de precio al canal. T2 publicar el catálogo y sus atributos. T3 responder la consulta de oferta vigente de un canal. T4 republicar tras reconectarse el canal |
| CU-OF-03 | T1 consultar el precio vigente de una referencia |
| CU-OF-04 | T1 registrar la etiqueta cambiada con su referencia, tienda e instante. T2 obtener las etiquetas pendientes del turno |
| CU-OF-05 | T1 consultar el indicador diario de puntos desactualizados. T2 consultar el detalle de cada punto |
| CU-OF-06 | T1 consultar el precio publicado por referencia, fecha, hora y canal. T2 exportar la evidencia de la consulta |
| CU-OF-07 | T1 obtener el precio aplicable, el menor de los dos. T2 registrar el incidente de discrepancia. T3 permitir o bloquear la venta según la confirmación de exhibición |
| CU-OF-08 | T1 consultar los incidentes por tienda. T2 marcar la resolución de un incidente |
| CU-OF-09 | T1 evaluar la promoción por vigencia, canal y tienda en la venta. T2 aplicar las condiciones vigentes en modo desconectado |
| CU-OF-10 | T1 crear o modificar la promoción con su vigencia, canal y tienda. T2 aprobarla y activarla. T3 desactivarla o consultar las vigentes |
| CU-OF-11 | T1 crear el artículo con sus atributos obligatorios, con rechazo si faltan. T2 marcarlo apto para uso operativo. T3 publicarlo al canal digital o impedir su publicación |
| CU-OF-12 | T1 consultar el reporte de referencias con atributos incompletos. T2 consultar el reporte de publicaciones fallidas con su causa |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | Portal público en la Opción A (D-08 de `contexto_sd-04.md`). El cliente llega por el sitio y la aplicación de AS-04 y se conserva a AH-01 como actor por prudencia |
| S2 | Las cajas son parte de la solución (nuevo punto de venta, sd-03 3.3.2), no un actor sistema |
| S3 | El «analista comercial» y el comprador se mapean a AH-11 (comercial y compras) |
| S4 | El sd-03 no describe este flujo en detalle. Las transacciones son propuestas |
| S5 | SUP-08 y SUP-09 (qué precio vale cuando difieren la etiqueta de sala y la propagación) siguen sin resolver. RF-023, «cobrar el menor», puede cambiar |
| S6 | «Obtener las etiquetas pendientes» (CU-OF-04) y «exportar la evidencia» (CU-OF-06) son propuestas mías, por el proceso de etiquetas del Caso (lista de cambios nocturna) y por RT-16.28. RF-021 nombra al «ejecutivo de cumplimiento», que se mapea a AH-15 |
| S7 | Ningún RF cubre registrar un cambio de precio ni administrar promociones, aunque el sd-03 3.3.2 dice que el servicio los administra. CU-OF-01 y CU-OF-10 son propuestas basadas en esa descripción y en 3.4.2 |
| S8 | El responsable de resolver los incidentes (CU-OF-08) se asigna a AH-05 mientras SUP-08 y SUP-09 sigan abiertos |

## 4. Cobertura de los 20 RF

RF-016, RF-018 y RF-030 en CU-OF-01. RF-017 en CU-OF-02. RF-064 en CU-OF-03. RF-019 y RF-020 en CU-OF-04. RF-029 en CU-OF-05. RF-021 en CU-OF-06. RF-022, RF-023 y RF-028 en CU-OF-07. RF-024 en CU-OF-08. RF-032 a RF-034 en CU-OF-09. RF-142 y RF-143 en CU-OF-11. RF-147 y RF-148 en CU-OF-12. CU-OF-01 y CU-OF-10 también se apoyan en el recorrido 3.4.2 (S7). La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Fuera de los casos de uso

OP-01 a OP-05 y EXC-02 (especificar, costear y presentar por separado la alternativa de etiquetas electrónicas) son un informe de evaluación y van a la EDT, no al modelo.

## 6. Decisiones del usuario (2026-10-08)

1. CU-OF-01 y CU-OF-10 entran como propuesta, aunque ningún RF los cubra.
2. El «ejecutivo de cumplimiento» de RF-021 es AH-15.
3. Los incidentes de discrepancia los resuelve AH-05 (S8).
4. CU-OF-03 queda con una sola transacción.
