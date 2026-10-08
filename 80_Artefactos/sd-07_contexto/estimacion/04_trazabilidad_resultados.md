# Trazabilidad de los 28 resultados del Anexo D a los casos de uso (prueba P3.3)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo, pendiente de la firma del equipo. Fuente de los resultados: `04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md`. Casos: `03_casos_de_uso_*.md`. Un resultado se considera trazado cuando al menos un caso de uso entrega la funcionalidad que lo mide. La columna final declara lo que el resultado necesita y no es un caso de uso (requisitos no funcionales, operación del cliente, migración o gestión del proyecto), para que no se pierda en la estimación.

| N.º | Resultado | Casos de uso que lo entregan | Parte fuera de los casos |
| :-- | :-- | :-- | :-- |
| 1 | Disponible que incorpora el error del registro | CU-EX-03, CU-EX-08, CU-EX-09 | Prueba del cálculo por categoría (calidad, sd-09) |
| 2 | Cancelaciones por falta de existencia bajo el umbral | CU-EX-04, CU-EX-05, CU-EX-06, CU-EX-07, CU-EX-17 | Operación del cliente (compartida). Medición mensual y en cada evento |
| 3 | Ningún cobro por una unidad no entregable | CU-EX-06, CU-PE-03, CU-PE-04, CU-PE-05, CU-PE-09 | Auditoría de pedidos cobrados y no cumplidos |
| 4 | Exactitud del inventario medida de forma continua | CU-EX-10, CU-EX-11, CU-EX-12, CU-EX-13 | Conteo en sala por el cliente (compartida) |
| 5 | Merma separada en sus causas | CU-EX-13, CU-EX-14, CU-EX-15 | Ninguna |
| 6 | Cambio de precio llega a cajas, canal digital y sala | CU-OF-01, CU-OF-02, CU-OF-03 | Latencia por destino (RNF-19). Etiquetado en sala por el cliente |
| 7 | Puntos de exhibición desactualizados conocidos | CU-OF-04, CU-OF-05 | Ninguna |
| 8 | Precio publicado acreditable en cada instante | CU-OF-06 | Retención de tres años (RNF-58) |
| 9 | Precio cobrado igual al exhibido | CU-OF-07, CU-OF-08, CU-OF-09, CU-VE-01 | Muestreo propio y política del cliente (compartida) |
| 10 | Estado único del pedido | CU-PE-10, CU-PE-11, CU-PE-12 | Auditoría cruzada entre canales (RNF-04) |
| 11 | Punto de despacho por costo total de servir | CU-PE-02, CU-PE-06 | Ninguna |
| 12 | Reconocimiento de la tienda que despacha para otro canal | CU-CM-01, CU-CM-02 | Ninguna |
| 13 | Devolución de marketplace con aviso al vendedor | CU-MK-07, CU-PV-04 | Aviso en 15 minutos (RNF-66) |
| 14 | Evaluación de los 310 vendedores con reglas conocidas | CU-MK-03, CU-MK-04, CU-MK-05, CU-MK-06 | Acuerdos de nivel de servicio con los vendedores (cliente) |
| 15 | Garantía legal resuelta en el mesón sin derivar | CU-PV-01, CU-PV-02, CU-PV-03 | Cliente oculto en las 22 tiendas (RNF-69). Operación del cliente (compartida) |
| 16 | Evaluación crediticia en el punto de venta en 8 segundos | CU-OR-01, CU-OR-02 | Medición de extremo a extremo (RNF-06) |
| 17 | Registro de la información precontractual | CU-EV-01, CU-EV-02, CU-EV-08 | Ninguna |
| 18 | Ninguna repactación sin evidencia del consentimiento | CU-CA-02, CU-EV-03, CU-EV-07 | Auditoría de los actos de la cartera migrada (migración, rama 6 de la EDT) |
| 19 | Evidencia conservada y recuperable por el plazo exigido | CU-EV-04, CU-EV-05, CU-EV-06 | Retención y recuperación a diez años (RNF-57). Archivo y simulacro |
| 20 | La entrega de información no depende de la voluntad del vendedor | CU-OR-01, CU-EV-01, CU-EV-02 | Prueba negativa de aceptación sin información |
| 21 | Separación de datos implementada, documentada y auditada | CU-CC-02, CU-CC-04, CU-CC-05, CU-CC-06, CU-BT-13 | Informe técnico y prueba de penetración (RNF-11, RNF-14). Separación física en infraestructura (sd-04) |
| 22 | Todo cruce registrado con finalidad, base y autorización | CU-CC-01, CU-CC-03 | Muestra trimestral por el encargado de cumplimiento del cliente |
| 23 | Hitos de remediación cumplidos antes de 2029 | CU-EV-06, CU-CA-01, CU-CA-06 | Informe de cumplimiento por hito (gestión del proyecto, sd-06). Plan de remediación de la autoridad |
| 24 | Migración de la cartera de 620.000 clientes sin diferencias | CU-CA-06, CU-CA-07 | Migración de datos por olas (rama 6 de la EDT, fuera del método de casos de uso) |
| 25 | Evento anual con degradación definida y suspensión de publicación | CU-BT-07, CU-EX-16, CU-EX-17, CU-PE-14, CU-VE-08 | Prueba de carga de 104.000 pedidos (calidad, sd-09) |
| 26 | Estado del pedido sin llamar y aviso previo al cobro | CU-PE-04, CU-PE-10, CU-PE-12, CU-EX-06 | Operación del cliente (compartida) |
| 27 | Diferencia de la tienda con causa atribuida | CU-EX-12, CU-EX-13, CU-EX-14 | Revisión con una jefatura de tienda |
| 28 | Apertura de tarjeta más rápida con información completa | CU-OR-01, CU-OR-02, CU-EV-01, CU-EV-02 | Medición comparada del tiempo de apertura |

## Observaciones

1. Los resultados 8, 16, 19, 21, 24 y 25 dependen en parte de requisitos no funcionales y de pruebas que no son casos de uso. Esa parte va a la EDT de calidad y de infraestructura (sd-07, ramas de pruebas y de migración) y se estima fuera del método (paso 7 del plan).
2. Los resultados 2, 4, 9, 15 y 26 son de responsabilidad compartida con el cliente (Anexo D). El caso de uso entrega solo la parte de la solución.
3. El resultado 12 depende de que la Etapa 2 incluya comisiones. Si se adelanta o se pospone ese servicio, hay que revisar la fecha del resultado (mes 21).
4. Los resultados 13 y 14 dependen de la Opción A del portal y de la interfaz del vendedor externo (AH-17). Si cambia la decisión, se revisan CU-MK-03 y CU-MK-05.
