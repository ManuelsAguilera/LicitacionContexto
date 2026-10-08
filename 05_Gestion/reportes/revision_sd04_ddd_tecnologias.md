# Revisión de SD-04: alcance, DDD y tecnologías

**Fecha:** 8 de octubre de 2026
**Estado:** arquitectura funcional propuesta; proveedor de nube, emplazamiento de legados y dimensionamiento sujetos a comparación y levantamiento.

## 1. Límite de la solución

Los trece servicios de [SD-03](../../02_Propuesta/latex_final/sd-03.tex) son responsabilidades de negocio. Una responsabilidad puede implementarse como módulo, proceso independiente o varios componentes técnicos cuando sus invariantes, carga y operación lo justifiquen. El mapa de microservicios no reemplaza a las plataformas que el Caso 09 ordena conservar.

| Plataforma actual | Decisión de alcance | Responsabilidad que conserva | Emplazamiento actual acreditado |
| :--- | :--- | :--- | :--- |
| ERP/DTE | Conservar e integrar | Contabilidad, remuneraciones y emisión tributaria exclusiva | No identificado por plataforma |
| WMS del centro de distribución principal | Conservar e integrar | Ubicaciones, preparación y despacho físico; extensión a Concepción por evaluar | Centro operativo conocido; alojamiento del software no identificado |
| Marketplace vigente | Conservar e integrar | Plataforma de terceros, vendedores y liquidaciones | No identificado |
| Comercio electrónico | Integrar inicialmente; conservar, remediar o sustituir según pruebas | Presentación, carro y canal propio durante la evaluación | No identificado |
| Fidelización | Integrar inicialmente; conservar, remediar o sustituir según pruebas | Puntos, segmentos y campañas durante la convivencia | No identificado |
| Núcleo Retail de 2009 | Reemplazar por olas | Autoridad temporal hasta conciliación y corte de cada función | No identificado |
| Plataforma financiera de 2011 | Reemplazar por olas | Operación de cartera y crédito hasta cada corte conciliado | No identificado |
| POS de 2014 | Sustituir tienda por tienda | Funciones de caja hasta cada corte; el nuevo POS conserva operación local sin enlace | Terminales en tiendas; alojamiento de sus dependencias no identificado |
| Motor de precios y promociones | Construir capacidad nueva | Hoy se opera con planillas y cargas | No tiene emplazamiento previo |

El [Caso 09](../../00_Bases/Caso_09_Cadena_Multitienda.md#capítulo-5-los-sistemas-que-existen-hoy) confirma un centro de datos propio en casa matriz, una sala de respaldo y uso compartido de red y centro por Retail y Emisor. No atribuye una ubicación física individual a ERP/DTE, WMS, marketplace ni al resto de los sistemas. «Externo a los nuevos servicios» describirá el límite funcional; «nube externa» solo podrá indicarse tras comprobar el alojamiento.

## 2. Candidatos DDD para capacidades nuevas

| Responsabilidad de SD-03 | Primera unidad desplegable candidata | Separación a evaluar | Plataforma que permanece |
| :--- | :--- | :--- | :--- |
| R:M-01 Oferta comercial | Catálogo y publicación de oferta | Motor de precios y promociones si su carga y ciclo de cambios justifican autonomía | Motor actual no existe |
| R:M-02 Abastecimiento | Órdenes, transferencias y coordinación de reposición | Mantener recepción física en WMS; adaptar confirmaciones | WMS, ERP/DTE |
| R:M-03 Existencias | Movimientos conciliados, reservas, ATP, conteos y ajustes en una unidad transaccional | Predicción de conteos y clasificación de merma como procesadores de apoyo sin autoridad de ajuste | WMS y POS como fuentes |
| R:V-01 Pedidos | Estado, promesa y coordinación de cumplimiento | Separar asignación solo si el volumen y las reglas lo requieren | WMS y comercio electrónico |
| R:V-02 Ventas | Venta, pago, reversa y conciliación | POS local es canal con diario propio, no el servicio central | POS nuevo, ERP/DTE |
| R:V-03 Comisiones | Módulo de cálculo y atribución | Extraer ante ciclo y operación independientes | ERP conserva remuneraciones |
| R:V-04 Gobierno de marketplace | Módulo de reglas y coordinación | Extraer si requiere despliegue independiente | Marketplace vigente |
| R:CL-01 Posventa | Casos, inspección y destino de devolución | Contexto propio por expediente y reglas | ERP/DTE y marketplace |
| R:CL-02 Clientes Retail | Identidad y preferencias comerciales | Fidelización conserva la escritura de puntos y campañas durante la convivencia; transferir autoridad solo si se sustituye y se concilian esos registros | Fidelización en evaluación |
| F:C-01 Originación | Solicitud, decisión y autorización en una unidad inicial | Separar autorización solo si se preservan invariantes de cupo y plazo en caja | Plataforma financiera durante migración |
| F:C-02 Cartera | Cuentas, pagos, cobranza y repactación | Contexto propio por migración y ciclo de operación | Plataforma financiera durante migración |
| F:C-03 Evidencia financiera | Expedientes y consentimiento | Contexto propio por integridad y retención | Plataforma financiera durante migración |
| X-01 Control de cruces | Gobierno de políticas y bitácora | Aplicación de la política en los extremos; evitar dependencia central por transacción | Ninguna plataforma sustituida por X-01 |

Estas son **candidatas técnicas**, no nuevos servicios comerciales ni un número final de microservicios. La separación se aprobará por autoridad de datos, invariante transaccional, latencia, carga, frecuencia de cambio y capacidad de operación. Las [Bases Transversales, RT-02](../../00_Bases/Bases_Transversales.md#22-requisitos-de-arquitectura) exigen módulos críticos desplegables de forma independiente y comparar el estilo elegido con una alternativa menos fragmentada.

## 3. Integración: gateway, Kafka y adaptadores

**Decisión de diseño:** las Bases no exigen Apache Kafka; el equipo propone utilizarlo para desacoplar y distribuir hechos de negocio entre servicios, adaptadores y proyecciones analíticas. Su valor debe comprobarse en esos flujos. La capa middleware completa incluye además contratos síncronos, API gateway y adaptadores; Kafka no enruta todas las llamadas ni autoriza por sí mismo operaciones bloqueantes.

- **API gateway:** entrada de canales y APIs expuestas, con identidad, autorización, cuotas, validación de contrato, versionado y trazabilidad. No convierte un legado conservado en microservicio nuevo.
- **Adaptadores privados y capa anticorrupción:** comunicación de los servicios nuevos con ERP/DTE, WMS, marketplace, comercio electrónico y fidelización; cada adaptador registra autoridad, sentido, confirmación y conciliación. El gateway puede publicar una API aprobada, mientras la traducción hacia el sistema conservado corresponde al adaptador.
- **Kafka:** propagación durable de hechos confirmados, como venta registrada, movimiento conciliado y cambio de estado de pedido. El patrón outbox evita perder un hecho tras confirmar una transacción; los consumidores deduplican, reintentan y envían fallas persistentes a una cola de tratamiento.
- **Contratos síncronos:** reserva antes del cobro, autorización financiera, comprobación de evidencia y otras decisiones bloqueantes requieren respuesta con plazo máximo e idempotencia.
- **POS local:** diario durable durante 24 horas sin enlace y sincronización posterior con clave de operación, secuencia y conciliación. La emisión fiscal en contingencia necesita modalidad aprobada; no se originan tarjetas ni se amplían cupos sin enlace.
- **Frontera de datos:** identidades, permisos y flujos separados para Retail y Emisor. X-01 gobierna las fichas aprobadas y la evidencia del cruce; no es un repositorio de datos ni un paso físico obligatorio para toda llamada.

## 4. Tecnologías propuestas para evaluación

| Capa o capacidad | Selección inicial | Alternativa y prueba que decide |
| :--- | :--- | :--- |
| Nube primaria y recuperación | Azure Chile Central (`chilecentral`) y Brazil South (`brazilsouth`) como referencia preferente, coherente con SD-01 | Comparar con Google Cloud Santiago (`southamerica-west1`) y São Paulo (`southamerica-east1`); acreditar socio de nube, residencia, servicios por región y continuidad. |
| Servicios de aplicación | Java 25 LTS y Spring Boot 4 para APIs y lógica transaccional | Comparar con otro marco vigente según soporte, competencias y desempeño; actualizar versiones durante el contrato. |
| Interfaces nuevas | TypeScript y React para portales y vistas POS | Probar periféricos y persistencia local antes de cerrar el empaquetado del POS. |
| Microservicios propios | Contenedores en AKS como referencia | Comparar GKE; prueba de latencia, carga, aislamiento y operación. |
| Eventos | Apache Kafka en AKS u oferta administrada acreditada en la región elegida | Google Cloud ofrece Kafka administrado en Santiago. Confluent Cloud en Azure documenta Brazil South, pero no Chile Central. Event Hubs ofrece protocolo Kafka, no el mismo broker; validar funciones antes de considerarlo alternativa. |
| Puerta de enlace | Azure API Management como candidato | Comparar Apigee por políticas, cuotas, autorización, versionado y trazabilidad; prueba con APIs del caso. |
| Persistencia transaccional | Azure Database for PostgreSQL Flexible Server, repositorios y permisos por contexto | Comparar Cloud SQL y disponibilidad de alta disponibilidad/replicación en cada región. |
| Caché | Redis administrado, condicionado a disponibilidad regional | Caché local por componente; nunca autoridad de venta, cupo o inventario. |
| Analítica Retail/Emisor | Azure Data Lake Storage Gen2 y Power BI; entornos y modelos separados | El motor analítico queda por seleccionar. Fabric completo no está disponible en Chile Central, solo Power BI; comparar BigQuery y Looker por permisos, residencia y linaje. |
| Identidad, secretos y telemetría | Federación con identidad corporativa; Entra ID, Key Vault, OpenTelemetry y Azure Monitor como candidatos | Confirmar proveedor de identidad y cobertura regional. |
| Infraestructura y entrega | Terraform y canal CI/CD auditado | Reutilizar canal del Cliente si satisface revisión, firma y trazabilidad. |
| Tienda sin enlace | Nodo local redundante, diario transaccional y sincronizador | Seleccionar motor y forma de instalación tras inventario de hardware, periféricos y prueba de corte de 24 horas. |
| Apoyo predictivo de inventario | Procesadores de modelo aislados del servicio transaccional, ejecutables en contenedores | Elegir entrenamiento e inferencia tras perfilar datos y comprobar disponibilidad regional y requisitos RT-18. |

La tabla es una **referencia técnica para evaluación**, no la especificación cerrada del Formulario T-11. Las versiones deben actualizarse durante los 56 meses del contrato. Azure se mantiene preferente por coherencia con la alianza propuesta en [SD-01](../../02_Propuesta/latex_final/sd-01.tex), pero el [artículo 34 de las Bases Administrativas](../../00_Bases/Bases_Administrativas.md#artículo-34-requisitos-habilitantes-de-idoneidad-técnica-y-financiera) exige acreditar al socio del proveedor de nube ofertado o un acuerdo formal con uno certificado. Esa evidencia está pendiente.

### Corrección de la decisión de nube

La elección anterior de Google Cloud se basó en disponibilidad documentada de servicios en Santiago y São Paulo, especialmente Kafka administrado. Ese criterio es relevante, pero insuficiente para desplazar Azure, ya mencionado en SD-01. No se había comparado el cumplimiento de alianza, residencia, recuperación, servicios de analítica ni responsabilidad operativa de Kafka. Por ello Azure vuelve a ser **referencia preferente**, Google Cloud queda como **alternativa de evaluación**, y la adjudicación técnica permanece abierta hasta una matriz y prueba de concepto verificables.

| Criterio | Azure | Google Cloud | Consecuencia |
| :--- | :--- | :--- | :--- |
| Región primaria y secundaria | Chile Central y Brazil South con tres zonas cada una; Chile Central no tiene par de región automático | Santiago y São Paulo | Ambas opciones requieren diseño explícito de recuperación y aprobación de transferencia de datos. |
| Kafka real en Santiago | No se ha acreditado una oferta administrada de Apache Kafka en Azure Chile Central; AKS es opción con operación propia | Managed Service for Apache Kafka documenta Santiago | Ventaja concreta de Google; Event Hubs no es Apache Kafka aunque exponga su protocolo. |
| Analítica en Santiago | Fabric completo no está disponible en Chile Central; Power BI sí. ADLS Gen2 más motor analítico por seleccionar | Cloud Storage, BigQuery y Looker Core son candidatos documentados | El diseño Azure no debe prometer Fabric completo en Chile. |
| Alianza habilitante | SD-01 nombra Azure, pero falta acreditación del socio o acuerdo | Requeriría actualizar SD-01 y acreditar una alianza de Google | Preferencia documental por Azure, condicionada a prueba. |

**Criterio de cierre:** comparar por requisito la cobertura regional, los contratos de Kafka, la separación Retail/Emisor, la conectividad con sistemas conservados, RTO/RPO, capacidad operativa y evidencia del socio. Ningún producto se fijará por familiaridad o por una sola ventaja regional.

### Fuentes oficiales de disponibilidad

- [Regiones de Azure](https://learn.microsoft.com/azure/reliability/regions-list), [regiones de Confluent Cloud](https://docs.confluent.io/cloud/current/get-started/regions.html) y [aclaración de Event Hubs frente a Apache Kafka](https://learn.microsoft.com/azure/event-hubs/apache-kafka-frequently-asked-questions).
- [Disponibilidad regional de Fabric y Power BI](https://learn.microsoft.com/fabric/admin/region-availability) y [características por región de Azure Database for PostgreSQL](https://learn.microsoft.com/azure/postgresql/flexible-server/service-overview).
- [Regiones de Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations), [Apigee](https://docs.cloud.google.com/apigee/docs/locations) y [BigQuery](https://docs.cloud.google.com/bigquery/docs/locations).
- [Compatibilidad de Spring Boot 4 con Java 25](https://spring.io/blog/2025/11/20/spring-boot-4-0-0-available-now/) y [calendario de soporte de Java LTS](https://www.oracle.com/java/technologies/java-se-support-roadmap.html).

## 5. Pendientes antes de cerrar el diseño físico

1. Levantar las catorce interfaces reales y los contratos disponibles de cada plataforma conservada.
2. Acreditar dónde se aloja cada sistema actual y qué conectividad privada admite.
3. Verificar los contratos y la conciliación de puntos, segmentos y campañas durante la convivencia con fidelización; si se sustituye, probar la transferencia de autoridad por atributo.
4. Medir transacciones, concurrencia, tamaños de eventos, crecimiento y ventanas de corte para dimensionar cómputo, Kafka, base de datos y red.
5. Validar la réplica a São Paulo con responsables legales y del Emisor; fijar RPO, RTO y prueba de conmutación.
6. Levantar hardware y periféricos del POS para especificar el motor local y la modalidad fiscal desconectada.
