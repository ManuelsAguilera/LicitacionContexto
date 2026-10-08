# Casos de uso del Servicio de comisiones (V-03), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo, pendiente del visto bueno del usuario y de la firma del equipo. Prefijo de casos: CM (Servicio de comisiones). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2, Anexo A (EXC-05) y Anexo B (3 RF del servicio, Etapa 2). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-CM-01 | R:V-03 | Calcular la base de comisión por vendedor, tienda y canal | AS-14 | 2 | RF-054, RF-071 | S2 |
| CU-CM-02 | R:V-03 | Transmitir la base de comisión al sistema de remuneraciones | AS-11 | 2 | RF-055 | S3 |
| CU-CM-03 | R:V-03 | Revisar la atribución de una comisión | AH-15 | 2 | 3.3.2 | S1, S4 |

Resumen. 3 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 3 × 5 = 15.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-CM-01 | T1 calcular la base reconociendo al vendedor y a la tienda de origen de la unidad. T2 recalcular la base considerando el canal de origen y el de cumplimiento cuando difieren |
| CU-CM-02 | T1 verificar el movimiento real de inventario en bodega. T2 transmitir la base de comisión al conector del sistema de remuneraciones |
| CU-CM-03 | T1 consultar la atribución de una venta y la regla aplicada. T2 registrar una observación o corrección con su motivo |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | CU-CM-03 no tiene RF. Sale de 3.3.2 («reglas auditables para atribuir una venta y su base de comisión»). Sus transacciones son propuestas |
| S2 | El servicio consume pedidos y ventas de los servicios correspondientes. No los captura de nuevo |
| S3 | EXC-05: el servicio no gestiona remuneraciones. Solo entrega la base al conector del sistema empresarial (AS-11, módulo del ERP, tipo 1) |
| S4 | AH-15 audita las reglas. La administración de las reglas de atribución (altas y cambios) no tiene RF y no se cuenta; queda como posible vacío del catálogo |
| S5 | Actores secundarios: ventas y pedidos como proveedores de datos, sin ser actores del servicio |

## 4. Cobertura de los RF

Cada RF del servicio está en un solo caso, según la columna Origen. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Preguntas abiertas (con sugerencia), pendientes del visto bueno del usuario

1. ¿AH-15 es el actor que revisa la atribución? Sugerencia: sí, es quien audita los registros; si el equipo prefiere a Comercial, solo cambia el actor.
2. ¿Se agrega un caso para administrar las reglas de atribución? Sugerencia: no por ahora; el catálogo no lo pide. Se anota como vacío para el equipo.
3. ¿El conector hacia AS-11 se cuenta como una transacción de CU-CM-02? Sugerencia: sí, mientras el conector sea la interfaz objetivo de EXC-05.
