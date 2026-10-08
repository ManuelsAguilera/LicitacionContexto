# Casos de uso del Servicio de clientes Retail (CL-02), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo, pendiente del visto bueno del usuario y de la firma del equipo. Prefijo de casos: CL (Servicio de clientes Retail). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.2, Anexo A (EXC-15), Anexo B (5 RF del servicio, Etapa 2, todos «propuesto por el proponente, por validar») y Anexo D (resultado 21). El servicio gobierna la identidad y la fidelización comerciales y no puede usar atributos financieros. Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-CL-01 | R:CL-02 | Consolidar los registros duplicados de un cliente | AH-13 | 3 | RF-227 | S1, S2 |
| CU-CL-02 | R:CL-02 | Mantener los puntos y la fidelización sincronizados | AS-05 | 3 | RF-228, RF-231 | S1, S3 |
| CU-CL-03 | R:CL-02 | Construir un segmento con atributos comerciales | AH-13 | 2 | RF-229 | S1, S4 |
| CU-CL-04 | R:CL-02 | Ejecutar una campaña sobre un segmento | AH-13 | 3 | RF-230 | S1, S5 |

Resumen. 4 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 4 × 5 = 20.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-CL-01 | T1 listar los candidatos a duplicado. T2 consolidar los registros en uno solo del retail. T3 consultar el registro consolidado y su historial |
| CU-CL-02 | T1 registrar cada movimiento de puntos del cliente. T2 enviar los datos de fidelización del cliente al sistema conservado. T3 conciliar las diferencias con el sistema de fidelización |
| CU-CL-03 | T1 definir el segmento con atributos comerciales, sin atributos de origen financiero. T2 consultar el tamaño y la composición del segmento |
| CU-CL-04 | T1 programar la campaña sobre un segmento. T2 ejecutarla por el sistema de fidelización. T3 consultar sus resultados |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | Los cinco RF son propuestas del proponente, por validar (Anexo B). Todas las transacciones son propuestas |
| S2 | No hay maestro único de clientes (línea roja). El servicio solo gobierna la identidad comercial. El identificador financiero lo resuelve control de cruces (CU-CC-05) |
| S3 | AS-05 (fidelización) se conserva e integra (EXC-15). Se cuenta como actor sistema tipo 1 por C5. Si el equipo reemplaza la fidelización, el conteo no cambia |
| S4 | El rechazo de atributos financieros lo hacen RF-170 y RF-171 (CU-CC-02). Aquí no se cuenta de nuevo |
| S5 | La campaña usa los canales del sistema de fidelización. No se cuenta aquí la entrega de mensajes del canal |
| S6 | Actores secundarios: AH-18 consume datos del servicio en los tableros (CU-BT-13) sin caso propio aquí |

## 4. Cobertura de los RF

Cada RF del servicio está en un solo caso, según la columna Origen. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Preguntas abiertas (con sugerencia), pendientes del visto bueno del usuario

1. ¿AH-13 es el actor que consolida duplicados? Sugerencia: sí, o Calidad de datos si el equipo la nombra; el conteo no cambia.
2. ¿Se agrega un caso de consulta de identidad comercial en la venta? Sugerencia: no por ahora; no hay RF. Se anota como posible vacío.
3. ¿El equipo valida los cinco RF propuestos (Anexo B)? Sugerencia: sí, antes de cerrar G3; sin ellos, el servicio queda con 0 casos de catálogo.
