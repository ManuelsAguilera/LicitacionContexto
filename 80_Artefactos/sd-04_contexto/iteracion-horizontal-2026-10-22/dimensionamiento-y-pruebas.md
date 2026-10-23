# Dimensionamiento preliminar y pruebas propuestas

Estado: cálculo de ingeniería y diseño de pruebas. No se ejecutaron benchmarks ni pruebas de servicios Azure; ninguna cifra constituye capacidad acreditada, tamaño de SKU seleccionado o cumplimiento de un SLA.

## Entradas y supuestos

Las entradas provienen del Caso 09 §14.1, con crecimiento a tres años. El §14.2 exige derivar TPS, almacenamiento y concurrencia como ingeniería, no los entrega como hechos. Los horizontes de migración corresponden al §15. Los multiplicadores y tamaños de fila siguientes son hipótesis explícitas que se reemplazarán con muestras representativas.

| Variable | Actual / proyección del caso | Uso en el cálculo |
|---|---|---|
| Documentos de venta/año | 31 M / 36 M | Escenario de seis años a tasa constante, no historial real medido |
| Líneas de venta/año | 71 M / 83 M | Escenario de seis años; 192 bytes lógicos por hecho como hipótesis |
| Pedidos online/año | 1,9 M / 3,1 M | Tres años de migración; tamaño de modelo pendiente |
| Cambios de precio/año | 14 M / 17 M | Historial separado; 160 bytes/evento como hipótesis |
| Máximo de campaña | 400.000 cambios en un día | Concentración en cinco minutos y fanout 5: escenario D-33, no TPS factual |
| SKU totales / tiendas | 458.000 / 22 → 650.000 / 25 | Demuestra costo de snapshots cartesianos; no todos los SKU están en todas las tiendas |
| Tarjetas con saldo | 620.000 → 760.000 | Dimensión financiera; retención independiente |
| Transacciones de tarjeta/año | 11,8 M → 14 M | Trabajo financiero a muestrear y conciliar |
| Gestiones de cobranza/año | 2,9 M → 3,4 M | Volumen distinto de transacciones, no sumarlas sin modelo |
| Repactaciones/año | 46.000 → 52.000 | Eventos de negocio propios |
| Estados de cuenta/mes | 620.000 → 760.000 | 7,44 M → 9,12 M/año; documentos excluidos del cálculo relacional |

## Cotas calculadas

Seis años a tasa actual producen un escenario de 426 M líneas y 186 M documentos; a tasa proyectada, 498 M y 216 M. No se afirma que el historial real tenga esos conteos. Con 192 bytes/línea y 128 bytes/documento:

- Actual: `(426 M × 192 + 186 M × 128)` = 105,600 GB decimales = **98.35 GiB lógicos**.
- Proyectado: `(498 M × 192 + 216 M × 128)` = 123,264 GB decimales = **114.80 GiB lógicos**.
- Multiplicador físico hipotético 2,5 para tuplas e índices: **245.87 / 287.00 GiB**. No representa la base analítica completa.
- Si la reconstrucción coexistiera con la versión vigente y fuera del mismo tamaño, solo esas tablas necesitarían **491.74 / 573.99 GiB**, antes de temporales y margen operativo. Es una condición de prueba, no recomendación de un disco final.

Se excluyen movimientos de stock, dimensiones, índices vectoriales/embeddings, imágenes, documentos, duplicados retenidos, staging, WAL, temporales, auditoría, respaldos, exportaciones y crecimiento durante reconstrucción. La suma no permite seleccionar una SKU de 256 GiB. Se medirán bytes reales por tabla/índice y amplificación de escritura con un mes representativo y las campañas de mayor cardinalidad.

Tres años online: escenarios de 5,7 M / 9,3 M pedidos, sin sumar documentos o líneas que ya estuvieran representados en los hechos de venta. Historial de precios: 14 M × 160 B = 2,24 GB lógicos/año actual, 2,72 GB proyectado; su horizonte de conservación debe decidirse y no se hereda del de ventas.

Un snapshot denso SKU×tienda×día produciría **3,677,740,000 / 5,931,250,000 filas/año**. Se descarta como diseño base: usar movimientos, posiciones activas y agregados diarios por categoría, con snapshots de corte donde ayuden a reconstruir. La exactitud se calcula sobre conteos auditados y muestra de control, sin fingir que se contó toda la población.

Promedio anual de documentos: 31 M / 365 / 86.400 = **0.983 ventas/s**. Sirve para contrastar volumen acumulado; no dimensiona Navidad ni Cyber. El caso distingue campañas presenciales y online; no sumar máximos no coincidentes ni extrapolar solo el promedio. Cyber de tres días: 104.000 pedidos actuales / 150.000 proyectados; se requiere perfil horario y simultaneidad reales antes de fijar el pico.

Escenario de precios D-33: 400.000 / 300 s = **1333.33 publicaciones/s**, fanout 5 = **6666.67 entregas/s**. La hipótesis concentra el máximo diario del caso en cinco minutos. Se prueba con tamaños reales de mensaje, escrituras outbox, deduplicación, versiones, tiempo de recuperación y consumidores lentos; no acredita que una unidad de Service Bus soporte esa carga. Event Hubs no se reincorpora sin demostrar una limitación y justificar la alternativa.

## Pruebas de aceptación propuestas

En todas las pruebas: datos sintéticos/anonimizados autorizados, reloj sincronizado, origen identificable, configuración/SKU/región registrada, carga y versión reproducibles. Ejecutar por ámbito y luego comprobar aislamiento; no sumar eventos de ambos ámbitos en un bus. Los dueños aprueban umbrales de proceso donde el caso no los fija.

| ID | Estímulo y fallo | Medición y criterio | Estado |
|---|---|---|---|
| T-01 | Venta por cada canal y caída de invalidación de caché | Disponibilidad publicada ≤30 s desde confirmación, incluidos tienda y digital; registrar máximo y p95/p99; sin descartar fallos de entrega | Propuesta; Caso §15 RT-05.29 |
| T-02 | Campaña de 400.000 precios/300 s, fanout 5, consumidor lento | Precios recibidos/publicados en 380 POS y canales digitales ≤5 min según origen; medir backlog/DLQ y reconciliar 400.000 versiones. Repetir con 430 POS proyectados | Propuesta; escenario de carga, umbral del caso |
| T-03 | Duplicar mensajes y caer tras commit del proyector antes de ack | Hechos, importes y conteos finales idénticos a una entrega; ninguna operación financiera duplicada | Propuesta; RT-02.06/07 |
| T-04 | Invertir eventos por agregado y omitir una versión | Estado no retrocede; gap queda visible y se concilia; no publicar modelo completo con huecos sin resolver | Propuesta; RT-02.07 |
| T-05 | Mensaje inválido/contrato incompatible | DLQ y alerta con referencia, sin PII expuesta; reenvío autorizado idempotente; ausencia no se oculta en totales | Propuesta |
| T-06 | Reconstruir mart desde exportación+corte mientras entran operaciones | Igualdad de sumas, saldos, conteos y versiones al corte; deltas aplicados sin pérdidas/duplicados; ensayo excediendo ventana de captura debe abortar o repetir el corte | Propuesta |
| T-07 | Carga representativa + corte financiero con fuente atrasada | Posición financiera conciliada disponible antes de 07:00 del día siguiente; incompleto visible si hay fuente ausente. Validación de Finanzas y trazas hasta origen | Propuesta; Caso §15 RT-05.29 |
| T-08 | BI Import/DirectQuery bajo concurrencia acordada | Solo conexiones a marts; denegar credenciales BI en transaccionales; medir latencia evento→pantalla y no declarar 30 s con caché/refresh superior | Propuesta; RT-05.05 |
| T-09 | Corte de enlace de tienda por 24 h y reintentos al restablecer | Diario durable, no pérdida/duplicado; venta aceptada por API antes de outbox; conciliación de cobro/documento/stock; carga de recuperación no bloquea tráfico actual | Propuesta; política de conflictos pendiente |
| T-10 | Dos terminales financieros desconectados intentan gastar el mismo cupo | Ninguna apertura ni incremento offline; no doble consumo del monto preautorizado. Sin partición/caducidad aprobada, función financiera offline deshabilitada | Propuesta; aprobación Riesgo/Finanzas pendiente |
| T-11 | Consumidor y credenciales del ámbito equivocado | Denegar red, SQL, bus, BI y claves cruzadas; única solicitud autorizada por X-01 y respuesta mínima; sin copia de cartera a Retail | Propuesta |
| T-12 | Perdida de nodo/servicio, restore y pérdida regional | Verificar RTO≤4 h/RPO≤15 min en cargas críticas, salvo requisito más duro aplicable; evidencia de restauración, claves, archivos y reproyección. DR solo en sitios/regiones autorizados | Propuesta; RT-07.04 |
| T-13 | Modelo predictivo en sombra + control aleatorio estratificado | Comparación contra control independiente, cobertura de categorías y sesgo; ningún ajuste automático ni clasificación de hurto. Umbral de mejora sujeto a validación del dueño | Propuesta |
| T-14 | Búsqueda con precio/stock cambiados y reindexación | Resultado no habilita compra sobre stock ficticio; comprobación con propietario; reconstrucción conserva referencias y política de imágenes | Propuesta |
| T-15 | Timeout de pago/firma/locker durante pedido y devolución | Recuperar por clave idempotente antes de repetir; estado pendiente visible; compensaciones y evidencia auditables | Propuesta |
| T-16 | Fallo de exportador OTLP y cola local durante 24 h | Backpressure/pérdida medidos, alerta y recuperación; no mezclar datos de ámbitos; SLO y métricas de entrega visibles | Propuesta |
| T-17 | Clientes públicos/privados, cadena TLS y consulta BI privada | Registrar protocolos por salto, certificados, DNS/rutas y denegación de acceso público a datos; conexión de BI distinguida de API Gateway | Propuesta |

El harness del diagrama solo ejecuta validaciones de esquema, separación declarada, conectores, formato y preservación de archivos. T-01 a T-17 son diseño de pruebas, ninguna está aprobada ni ejecutada en esta entrega.
