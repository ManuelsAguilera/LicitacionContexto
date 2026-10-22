# Diferencias para conciliación posterior

SD-03 y SD-04 permanecen intactos, comprobados con SHA-256. Las líneas son orientativas de la copia local; los textos no se sincronizan automáticamente con la nueva figura.

| Fuente actual | Nueva figura/análisis | Trabajo de conciliación |
|---|---|---|
| SD-04, Event Hubs en ADR-06, integración y continuidad (aprox. 105, 236, 371, 390, 609) | Service Bus Premium propio por ámbito, D-33 | Cambiar justificación, semántica, retención y recuperación; no trasladar promesas de replay de Event Hubs |
| SD-04, Data Lake y analítica (aprox. 344, 397) | PostgreSQL analítico dedicado por ámbito y Blob con usos separados | Reescribir selección, dimensionamiento, flujos, conexión BI y políticas; BI no consulta transaccional |
| SD-04, Ventas→APIM Filial y X-01 (aprox. 268, 288) | Mediación explícita Ventas→X-01→APIM Filial | Precisar identidad, estado, respuesta mínima y bitácora; impedir acceso directo fuera del contrato |
| SD-04, tablas físicas y promesas de continuidad/respaldo (aprox. 490, 562, 599–609) | Separación de permisos/recursos mantenida; Backup/Arc fuera de L2 | Validar cada respaldo, región, ruta y aislamiento; no afirmar cobertura genérica |
| SD-04, Brasil/DR y residencia | Pendiente de autorización escrita | Conciliar sitio secundario del cliente y alternativa Brasil; no asumir aprobado el tránsito de borde |
| SD-03, plataformas conservadas y crédito offline (aprox. 110, 132) | Conservadas; sin apertura ni incremento de crédito offline | Sin cambio de alcance decidido; documentar política de cupo preautorizado antes de habilitarla |
| SD-13, búsqueda | PostgreSQL/pgvector e imágenes autorizadas | Mantener referencia tecnológica y verificar índice/reconstrucción; no introducir buscador distinto |
| Figura 4.29 | Figura 4.30 horizontal, sin actores, ocho capas | Sustitución gráfica posterior y registro IA Alto en Tabla 4.17 sujetos a edición autorizada |

El registro D-01–D-56 contiene pendientes anteriores resueltos por decisiones posteriores. No reabrir D-22/D-26/D-33 por leer una línea histórica fuera de secuencia. Las aprobaciones generales no sustituyen la confirmación específica del tenant ni la residencia.
