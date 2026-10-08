# Casos de uso del Servicio de marketplace (V-04), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo, pendiente del visto bueno del usuario y de la firma del equipo. Prefijo de casos: MK (Servicio de marketplace). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2, Anexo A (EXC-04, EXC-12), Anexo B (25 RF del servicio, Etapa 2) y Anexo D (resultados 13 y 14). El servicio gobierna la relación con la plataforma vigente (AS-03) y no la reemplaza. Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-MK-01 | R:V-04 | Declarar y actualizar la existencia del vendedor | AH-17 | 3 | RF-102 a RF-104 | S2 |
| CU-MK-02 | R:V-04 | Publicar la existencia vigente y despublicar la vencida | AS-14 | 2 | RF-109, RF-124 | S3 |
| CU-MK-03 | R:V-04 | Consultar los pedidos, las devoluciones y la evaluación | AH-17 | 3 | RF-110 a RF-112 | S2 |
| CU-MK-04 | R:V-04 | Calcular los indicadores de nivel de servicio por vendedor | AS-14 | 2 | RF-105 | S4 |
| CU-MK-05 | R:V-04 | Dar a conocer las reglas de evaluación al vendedor | AH-17 | 2 | RF-119, RF-120 | S2 |
| CU-MK-06 | R:V-04 | Aplicar la consecuencia escalonada de un incumplimiento | AH-13 | 3 | RF-121 a RF-123 | S5 |
| CU-MK-07 | R:V-04 | Gestionar una devolución de producto de marketplace | AH-09 | 3 | RF-106 a RF-108 | S6 |
| CU-MK-08 | R:V-04 | Identificar al vendedor y las condiciones en la compra | AS-04 | 3 | RF-113 a RF-116 | S7 |
| CU-MK-09 | R:V-04 | Impedir que un pedido intermediado use existencia propia | AS-03 | 2 | RF-117, RF-118 | S8 |
| CU-MK-10 | R:V-04 | Informar la base de comisión de marketplace al ERP | AS-01 | 2 | RF-125, RF-126 | S9 |
| CU-MK-11 | R:V-04 | Conciliar la liquidación de un vendedor | AH-13 | 2 | 3.3.2; EXC-04 | S1, S10 |

Resumen. 11 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 11 × 5 = 55.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-MK-01 | T1 declarar la existencia de sus referencias. T2 actualizar la existencia previamente declarada. T3 consultar el registro de actualizaciones con su fecha y hora |
| CU-MK-02 | T1 publicar solo la existencia de la última actualización vigente. T2 despublicar la oferta cuyo stock declarado superó el plazo sin actualización |
| CU-MK-03 | T1 consultar el estado de cada pedido intermediado. T2 consultar las devoluciones de sus pedidos. T3 consultar su evaluación de desempeño vigente |
| CU-MK-04 | T1 calcular los indicadores según las reglas publicadas. T2 publicar los indicadores al vendedor y a los canales |
| CU-MK-05 | T1 registrar el acuse de conocimiento de las reglas. T2 intentar aplicar una regla sin acuse previo y recibir el rechazo |
| CU-MK-06 | T1 determinar la consecuencia según la matriz de escalamiento. T2 ejecutar la sanción con el rol nominado. T3 consultar la trazabilidad de la sanción |
| CU-MK-07 | T1 registrar la recepción de la devolución y notificar al vendedor en ese momento. T2 registrar qué parte asume el costo. T3 registrar la prestación entregada al cliente |
| CU-MK-08 | T1 consultar el vendedor y quien despacha la unidad, en catálogo, ficha y compra. T2 consultar las condiciones de devolución. T3 consultar las condiciones de garantía legal |
| CU-MK-09 | T1 recibir el pedido intermediado y rechazarlo si compromete existencia propia. T2 rechazar la asignación de una unidad propia a su cumplimiento |
| CU-MK-10 | T1 calcular e informar la base de comisión de la venta efectivamente cumplida. T2 notificar la anulación de la base por devolución o cancelación |
| CU-MK-11 | T1 consultar la liquidación del período con sus pedidos y devoluciones. T2 registrar una diferencia con el vendedor |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | CU-MK-11 no tiene RF. Sale de 3.3.2 («oferta, disponibilidad, pedidos, devoluciones y liquidaciones que gestiona Ancoa») y de EXC-04 (integrar y medir la plataforma). Sus transacciones son propuestas |
| S2 | El vendedor (AH-17) es actor tipo 1 por decisión del usuario del 2026-10-08: usa la interfaz de programación de la plataforma vigente (AS-03) |
| S3 | CU-MK-02 lo dispara el temporizador (AS-14). El plazo de vigencia del stock declarado es parámetro y no genera caso de administración |
| S4 | Los indicadores se calculan para los 310 vendedores (resultado 14). Es una sola ejecución por ciclo y se cuenta una vez |
| S5 | El rol nominado de RF-122 se mapea a AH-13 (Canales digitales y Marketing). El rol exacto está por validar |
| S6 | La devolución se recibe en el mesón (AH-09) y la posventa la gestiona. El servicio solo registra costo y prestación (RF-107 y RF-108), sin repetir la garantía legal de posventa |
| S7 | Bajo la Opción A, AS-04 consulta los datos por interfaz de programación. La presentación al cliente es del sitio existente |
| S8 | AS-03 es la plataforma vigente que se mantiene (EXC-12). La integración se cuenta en CU-MK-02 (oferta), CU-MK-09 (pedidos) y CU-MK-01 (existencia declarada) |
| S9 | AS-01 (ERP/DTE) recibe la base de comisión de marketplace. La comisión de venta propia está en el servicio de comisiones y no se repite |
| S10 | La liquidación la calcula la plataforma de marketplace (EXC-04). Aquí solo se concilia con lo que Ancoa registra. Si el equipo la considera fuera del servicio, se retira CU-MK-11 (−5 UUCW) |

## 4. Cobertura de los RF

Cada RF del servicio está en un solo caso, según la columna Origen. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Preguntas abiertas (con sugerencia), pendientes del visto bueno del usuario

1. ¿Se conserva CU-MK-11 (conciliar liquidaciones)? Sugerencia: sí como propuesta, con la nota del supuesto 10; se retira si el equipo confirma que la liquidación es solo de la plataforma.
2. ¿AH-13 es el rol nominado de la matriz de escalamiento (RF-122)? Sugerencia: sí, mientras la matriz no nombre otro rol.
3. ¿El vendedor externo usa una interfaz de programación o un portal? Sugerencia: interfaz de programación (tipo 1), según la decisión ya firmada de AH-17; si es portal, el caso se mantiene y cambia el peso del actor.
4. ¿RF-106 a RF-108 van en marketplace o en posventa? Sugerencia: marketplace, tal como lo clasifica el Anexo B; posventa solo cubre la garantía de la unidad propia.
