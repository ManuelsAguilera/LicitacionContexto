# Evaluación del middleware de eventos híbrido para SD-04

**Fecha:** 8 de octubre de 2026. **Estado:** conclusión de revisión; selección de producto condicionada al inventario de interfaces y a pruebas de corte.

## Pregunta evaluada

Los eventos de Ancoa pueden originarse en las 22 tiendas, los centros de distribución o plataformas actuales cuya ubicación física aún debe acreditarse. ¿Impide esto usar un servicio de mensajería alojado en Azure como Event Hubs o Service Bus?

**Conclusión compartida por los dos frentes de revisión:** no lo impide mientras exista enlace; sí impide que el servicio en Azure reciba mensajes durante una desconexión del origen. Ninguno de los brokers evaluados sustituye por sí mismo el registro atómico de la venta y del hecho pendiente en el POS. El [diario local y sincronizador ya definidos en SD-04](../../02_Propuesta/latex_final/sd-04.tex) deben conservarse con independencia del bus central.

La ruta propuesta es: **operación local y hecho pendiente en una unidad durable → relay con confirmación y reintento → servicio central de eventos → consumidores idempotentes**. El POS no marca el hecho como entregado antes de recibir confirmación; una confirmación perdida puede causar reenvío, por lo que el consumidor deduplica por identificador de operación. La conciliación decide conflictos de negocio, incluidos stock y documentos. Para plataformas conservadas fuera de Azure se requiere un adaptador/outbox equivalente cuando no puedan publicar de forma fiable; su ubicación y contrato deben levantarse antes de diseñarlo.

## Crítica de las alternativas

| Opción | Qué resuelve | Efecto del evento nacido fuera de Azure | Límite y juicio |
| :--- | :--- | :--- | :--- |
| Azure Event Hubs | Registro de hechos con grupos de consumidores, relectura y captura hacia Data Lake. | Puede recibir desde fuera de Azure cuando existe conectividad; durante el corte el origen debe persistir y reenviar. | No trae cola de errores por consumidor; orden por partición. **Candidato preferente** si predominan hechos confirmados consumidos por varios servicios y BI. |
| Azure Service Bus Topics | Entrega a suscripciones con filtros, sesiones, detección de duplicados y cola de errores. | También requiere enlace antes de aceptar el mensaje; su almacenamiento comienza al recibirlo. | No funciona como historial general ya consumido para reconstruir proyecciones. **Preferible** si predominan trabajos/comandos dirigidos con tratamiento individual de fallas. |
| RabbitMQ Streams / clústeres locales | Mensajería y flujos locales; Federation/Shovel pueden enlazar instalaciones por WAN variable. | Permite comunicación local mientras Azure es inaccesible, si se despliega donde están los consumidores. | Aumenta operación, seguridad y recuperación; no conviene extender un único clúster por WAN. **Condicionado** a necesidad real de intercambio local. |
| NATS JetStream local | Almacenamiento y consumidores locales, con topología de leaf nodes y flujos entre dominios. | Puede mantener actividad local durante corte, con configuración explícita de almacenamiento y posterior intercambio. | Agrega nodos y supervisión; tampoco asegura atomicidad entre venta y evento por sí solo. **Condicionado** a varios consumidores locales autónomos. |
| Apache Kafka | Flujo persistente y relectura en nube o instalación propia. | Kafka alojado en Azure presenta la misma dependencia del enlace; Kafka local requiere operación propia. | No se justifica solo por la ubicación del productor; sigue como preferencia técnica evaluable. |

**No se proponen dos buses centrales por defecto.** La elección entre Event Hubs y Service Bus deriva de la semántica dominante de los contratos, no de la ubicación de los productores. En el alcance hoy descrito predominan hechos confirmados que alimentan varios servicios y BI; por ello Event Hubs es el candidato Azure para evaluar primero, sujeto a comprobar nivel disponible en Chile Central, contratos, residencia, DR y resultados de prueba. Las decisiones bloqueantes —reserva, autorización de compra, evidencia— conservan APIs síncronas con plazo y reglas de falla.

## Cuándo sí agregar un broker local

- **Tienda:** solo si se identifican dos o más aplicaciones locales independientes que deban consumir los mismos eventos y continuar coordinadas durante 24 horas sin enlace. El diario transaccional del POS ya cubre el registro y posterior envío de sus ventas; no justifica por sí mismo un broker por tienda.
- **Centro de datos:** solo si el inventario comprueba que varias plataformas conservadas residen allí y deben intercambiar mensajes entre sí durante una pérdida de conectividad con Azure. En ese caso se comparan broker local y relay de adaptadores, y se diseña la sincronización como puente entre instalaciones, sin un clúster único extendido por WAN.
- **Frontera Retail–Emisor:** el almacenamiento local, el relay y el bus central deben mantener separados permisos, credenciales y contratos. Un corte de enlace no habilita nuevos cruces ni decisiones financieras sin autorización.

## Pruebas que cierran la decisión

1. Cortar tienda–Azure y tienda–centro de datos según rutas reales; mantener 24 horas de operaciones permitidas, con diario íntegro y capacidad medida.
2. Cortar centro de datos–Azure durante el intercambio de una plataforma conservada; comprobar persistencia local, reintento y conciliación.
3. Restaurar cada enlace; medir tiempo de vaciado, orden por agregado, duplicados, errores, atraso de BI y cumplimiento de RPO/RTO.
4. Repetir con eventos Retail y del Emisor; probar denegación de un flujo no aprobado y ausencia de datos financieros en consumidores Retail.
5. Comparar en una prueba de concepto los mismos flujos en Event Hubs y Service Bus antes de elegir servicio, nivel y región; validar la capacidad operativa si se propone broker local.

## Fuentes oficiales

- Microsoft, [patrón transactional outbox](https://learn.microsoft.com/azure/architecture/databases/guide/transactional-out-box-cosmos), [Event Hubs](https://learn.microsoft.com/azure/event-hubs/event-hubs-about), [Service Bus Topics](https://learn.microsoft.com/azure/service-bus-messaging/service-bus-queues-topics-subscriptions) y [comparación de mensajería](https://learn.microsoft.com/azure/event-grid/compare-messaging-services).
- RabbitMQ, [confiabilidad](https://www.rabbitmq.com/docs/reliability), [Federation](https://www.rabbitmq.com/docs/federation) y [Streams](https://www.rabbitmq.com/docs/streams).
- NATS, [JetStream](https://docs.nats.io/concepts/jetstream) y [leaf nodes](https://docs.nats.io/learn/topologies/leaf-nodes).
