# Matriz de componentes y relaciones

Estado: borrador. Los ámbitos y relaciones se obtienen de los JSON validados. Las direcciones expresan la intención del contrato, que puede ser consulta, política, escritura o evento; no se infiere que toda entrada sea una fuente de datos. El detalle de cada contrato está en `relaciones.md`.

## 4.33 · Arquitectura lógica por capas · datos y capacidades transversales

| Componente | Ámbito | Responsabilidad / datos | Relaciones | Estado y decisión |
| :--- | :--- | :--- | :--- | :--- |
| `web` | retail | Portal y app de la tienda · React / React Native | Salidas: front_door | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `pos` | retail | Caja y mesón · React web servido desde tienda | Salidas: entrada_privada | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `operacion` | retail | App interna de tienda · 4 perfiles · RN / SQLite / DataWedge · QR + PIN: un factor | Salidas: entrada_privada | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `logistica` | retail | Vista logística · WMS del CD conservado | Salidas: entrada_privada | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `movil` | retail | Consola comercial y de atención | Salidas: entrada_privada | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `portal_f` | emisor | Portal y app de la tarjeta · Código propio · simulador CAE | Salidas: front_door | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `meson_f` | emisor | Mesón financiero · Sesión y permisos de la Filial | Salidas: entrada_privada | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `dns` | transversal | Azure DNS · Zonas y registros por ámbito | Salidas: front_door | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `aks_r` | transversal | Azure Kubernetes Service · Ejecución aislada por ámbito · Premium / LTS por acreditar | Soporte tecnológico de la franja alineada; no es una dependencia en serie del tráfico. | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `oferta` | retail | Oferta comercial · Artículos, precios y promociones · E1 · despliegue por decidir | Contratos agrupados al contorno de `area_mercaderia`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `abastecimiento` | retail | Abastecimiento · Órdenes, transferencias y recepción · E2 · microservicio | Contratos agrupados al contorno de `area_mercaderia`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `existencias` | retail | Existencias · Movimientos, reservas y disponible · E1 · microservicio | Contratos agrupados al contorno de `area_mercaderia`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `pedidos` | retail | Pedidos · Promesa, asignación y estado único · E2 · microservicio | Contratos agrupados al contorno de `area_venta`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `ventas` | retail | Ventas · Venta, pago, reversa y conciliación · E1 · microservicio | Contratos agrupados al contorno de `area_venta`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `comisiones` | retail | Comisiones · Regla y base de atribución · E2 · módulo extraíble | Contratos agrupados al contorno de `area_venta`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `market` | retail | Marketplace · Reglas de vendedores y coordinación · E2 · módulo extraíble | Contratos agrupados al contorno de `area_venta`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `posventa` | retail | Posventa · Caso, inspección y destino de devolución · E2 · microservicio | Contratos agrupados al contorno de `area_clientes`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `clientes` | retail | Clientes Retail · Identificación, preferencias y fidelización · E2 · microservicio | Contratos agrupados al contorno de `area_clientes`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `originacion` | emisor | Originación de crédito · Solicitud, evaluación, cupo y autorización · E1 · microservicio | Contratos agrupados al contorno de `servicios_e`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `cartera` | emisor | Cartera de crédito · Cuenta, saldo, pago, mora y cobranza · E1/E2 · microservicio | Contratos agrupados al contorno de `servicios_e`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `evidencia` | emisor | Evidencia financiera · Precontrato, aceptación, firma y expediente · E1 · microservicio | Contratos agrupados al contorno de `servicios_e`; cada servicio conserva su autoridad, transacción y outbox. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `x01` | frontera | Control de cruces | Entradas: area_venta; Salidas: api_management, bitacora | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `conteo` | retail | Conteo cíclico predictivo · Existencias · proceso | Pertenencia visual y responsabilidad: Existencias. No necesita arista decorativa. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `lockers` | retail | Lockers Ancoa 24/7 · Pedidos · producto | Pertenencia visual y responsabilidad: Pedidos. No necesita arista decorativa. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `busqueda` | retail | Búsqueda vectorial multimodal · Oferta · tecnología | Pertenencia visual y responsabilidad: Oferta. No necesita arista decorativa. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `media` | retail | Retail Media Network · Oferta · modelo de negocio | Pertenencia visual y responsabilidad: Oferta. No necesita arista decorativa. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `fila` | retail | Modo Tienda y fila virtual · Clientes · experiencia | Pertenencia visual y responsabilidad: Clientes Retail. No necesita arista decorativa. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bus_r` | retail | Azure Service Bus Premium · Retail · outbox / reintentos | Entradas: area_mercaderia, area_venta, area_clientes; Salidas: comercio, canales, socios, area_clientes, local_sync, proy_r, common_notif | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bus_e` | emisor | Azure Service Bus Premium · Filial · outbox / reintentos | Entradas: servicios_e; Salidas: credito, proy_e, common_notif | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `comercio` | retail | Comercio · ERP/DTE y WMS | Entradas: bus_r; Salidas: ext_comercio, archivo_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `canales` | retail | Canales · e-commerce / marketplace / fidelización | Entradas: bus_r; Salidas: ext_canales | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `socios` | retail | Socios · pagos / proveedores / transportistas | Entradas: bus_r; Salidas: ext_socios | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `credito` | emisor | Crédito · legado 2011 / CMF / firma | Entradas: bus_e; Salidas: ext_credito | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `local_serv` | retail | Operación sin enlace · Venta y consulta de oferta vigente | Entradas: area_venta; Salidas: local_sync, local_data | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `local_sync` | retail | Sincronización de operaciones · Reintentos y conciliación | Entradas: local_serv, local_data, bus_r; Salidas: entrada_privada | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `datos_merc` | retail | PostgreSQL · Retail · Oferta / Abastecimiento / Existencias | Entradas: area_mercaderia;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `datos_venta` | retail | PostgreSQL · Retail · Pedidos / Ventas / Comisiones / Marketplace | Entradas: area_venta;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `datos_clientes` | retail | PostgreSQL · Retail · Posventa / Clientes | Entradas: area_clientes;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bitacora` | frontera | Bitácora · de cruces | Entradas: x01;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `datos_orig` | emisor | PostgreSQL · Filial · Originación: evaluación, cupo y autorización | Entradas: servicios_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `datos_cartera` | emisor | PostgreSQL · Filial · Cartera: cuentas y saldos | Entradas: servicios_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `datos_evid` | emisor | Azure Blob Storage · Filial · Documentos de evidencia vigentes | Entradas: servicios_e; Salidas: archivo_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `archivo_r` | retail | Azure Blob Storage WORM · Retail · Archivo y evidencia retenida | Entradas: comercio, common_docs, mart_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `archivo_e` | emisor | Azure Blob Storage WORM · Filial · Archivo y evidencia retenida | Entradas: datos_evid, common_docs, mart_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `redis` | retail | Azure Managed Redis · Retail · Caché de oferta ≤ 30 s | Entradas: area_mercaderia;  | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `historial` | retail | PostgreSQL · Retail · Historial de precios append-only | Entradas: area_mercaderia;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `powerbi` | transversal | Microsoft Power BI · Modelos y permisos separados por ámbito · Consulta exclusiva de PostgreSQL analítico | Salidas: mart_r, mart_e | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `local_data` | retail | Diario de operaciones pendientes · Persistencia durable Retail | Entradas: local_serv; Salidas: local_sync | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `cupo_local` | emisor | Cupo preautorizado sin enlace · Asignación exclusiva · caducidad pendiente | Entradas: servicios_e;  | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `ext_comercio` | retail | ERP/DTE y WMS conservados | Entradas: comercio;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `ext_canales` | retail | E-commerce, marketplace y fidelización | Entradas: canales;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `ext_socios` | retail | Pagos, proveedores y transportistas · Lockers y publicidad: interfaz por precisar | Entradas: socios;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `ext_credito` | emisor | Crédito 2011 (convivencia) · Reportes CMF y firma por interfaz | Entradas: credito;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `front_door` | transversal | Azure Front Door Premium · Retail / Filial: perfiles separados · WAF propio por ámbito · TLS 1.3 objetivo | Entradas: dns, web, portal_f; Salidas: private_link | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `application_gateway` | transversal | Application Gateway v2 · Instancias Retail / Filial separadas | Entradas: private_link, entrada_privada; Salidas: api_management | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `api_management` | transversal | Azure API Management Premium clásico · Instancias, productos y contratos separados por ámbito | Entradas: application_gateway, api_center, x01, common_admin; Salidas: area_mercaderia, area_venta, area_clientes, servicios_e, common_flujos, common_docs, search_r, search_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `api_center` | transversal | Azure API Center · Catálogos Retail / Filial separados | Salidas: api_management | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `private_link` | transversal | Azure Private Link | Entradas: front_door; Salidas: application_gateway | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `proy_r` | retail | Java / Spring en AKS · Retail · Ingesta, proyecciones y representaciones | Entradas: bus_r, lake_r; Salidas: mart_r, search_r, lake_r, metadata, vector | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `mart_r` | retail | PostgreSQL Flexible Server · Retail · Repositorio analítico dedicado · Indicadores, agregaciones y linaje | Entradas: proy_r, powerbi, backup; Salidas: archivo_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `proy_e` | emisor | Java / Spring en AKS · Filial · Ingesta, proyecciones y conciliación | Entradas: bus_e, lake_e; Salidas: mart_e, search_e, lake_e, metadata | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `mart_e` | emisor | PostgreSQL Flexible Server · Filial · Repositorio analítico dedicado · Indicadores, agregaciones y linaje | Entradas: proy_e, powerbi, backup; Salidas: archivo_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `vector` | retail | PostgreSQL / pgvector · Oferta · Índice multimodal reconstruible | Entradas: proy_r, area_mercaderia;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `tech_ui` | transversal | React / React Native · TypeScript · canales separados | Soporte tecnológico de la franja alineada; no es una dependencia en serie del tráfico. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `tech_java` | transversal | Java 25 LTS · APIs y trabajadores propios | Soporte tecnológico de la franja alineada; no es una dependencia en serie del tráfico. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `tech_spring` | transversal | Spring Boot 4 · Contratos y lógica de servicios | Soporte tecnológico de la franja alineada; no es una dependencia en serie del tráfico. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `common_admin` | transversal | Administración y parámetros · Consolas por ámbito · Auditoría · versiones · Aprobación · simulación · Maestro: dueño pendiente | Salidas: api_management | Conservar capacidad separada por ámbito; producto/contrato por precisar. |
| `common_flujos` | transversal | Flujos y tareas humanas · Bandeja por ámbito · Plazos y delegación · Estado durable propio · Producto pendiente | Entradas: api_management;  | Conservar capacidad separada por ámbito; producto/contrato por precisar. |
| `common_docs` | transversal | Documentos y firma · Capacidad por ámbito · Recepción / devolución · Evidencia propia Filial · Prestador pendiente | Entradas: api_management; Salidas: archivo_r, archivo_e, ext_comunes | Conservar capacidad separada por ámbito; producto/contrato por precisar. |
| `common_notif` | transversal | Notificaciones · Correo · app · SMS/IM · Plantillas y preferencias · Reintentos y entrega · Proveedor pendiente | Entradas: bus_r, bus_e; Salidas: ext_comunes | Conservar capacidad separada por ámbito; producto/contrato por precisar. |
| `search_r` | retail | OpenSearch · Retail · Búsqueda global · API propia y filtros | Entradas: proy_r, api_management;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `search_e` | emisor | OpenSearch · Filial · Búsqueda global · API propia y filtros | Entradas: proy_e, api_management;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `regulatorio` | emisor | Control regulatorio · CANDIDATO · Reportes y prevención de lavado · Alcance, RF y etapa por aprobar | Sin contratos operacionales por ser candidato. | Candidato F:C-04. Alcance/RF/etapa/aprobación pendientes; sin operación. |
| `entrada_privada` | transversal | Acceso privado corporativo · SD-WAN / VPN · ExpressRoute propuesto · Rutas y permisos propios por ámbito | Entradas: pos, operacion, logistica, movil, meson_f, local_sync; Salidas: application_gateway | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `ext_comunes` | externo | Prestadores de firma y de mensajería · Contrapartes y contratos por precisar · Credenciales separadas por ámbito | Entradas: common_docs, common_notif;  | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `evid_meta` | emisor | PostgreSQL · Filial · C-03: metadatos de evidencia | Entradas: servicios_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `lake_r` | retail | ADLS Gen2 · Retail · Landing, curados y conjuntos versionados | Entradas: adf, proy_r; Salidas: proy_r, training | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `lake_e` | emisor | ADLS Gen2 · Filial · Landing y curados autorizados | Entradas: adf, proy_e; Salidas: proy_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `adf` | transversal | Azure Data Factory · Cargas y dependencias por ámbito | Salidas: lake_r, lake_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `metadata` | transversal | OpenMetadata · Catálogo, linaje y calidad · Instancias propias por ámbito | Entradas: proy_r, proy_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `mlflow` | retail | MLflow · Retail · Experimentos y versiones de modelos | Entradas: training; Salidas: training | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `training` | retail | Python / scikit-learn en AKS · Conteo: entrenamiento e inferencia | Entradas: lake_r, mlflow; Salidas: mlflow, area_mercaderia | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `backup` | transversal | Azure Backup / PostgreSQL PITR · Cobertura y restauración por recurso | Salidas: mart_r, mart_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `security_summary` | transversal | 7 · Seguridad · Entra ID P2 · External ID · Intune · Workload Identity · Key Vault · Managed HSM · PIM · Bastion · Private Access · Defender for Endpoint / Cloud · Sentinel · Instancias y permisos por ámbito · detalle: página 3 | Política transversal, desarrollada en página 3; no es un producto adicional. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `observability_summary` | transversal | 8 · Observabilidad · OpenTelemetry Collector · Prometheus · Loki · Tempo · Grafana autogestionado / Alerting · Blackbox Exporter · Azure Monitor / Log Analytics · colas locales 24 h · Instancias y permisos por ámbito · detalle: página 3 | Política transversal, desarrollada en página 3; no es un producto adicional. | Conservar como diseño objetivo; capacidad y configuración por comprobar. |

## 4.34 · Detalle lógico de Datos · alimentación, gobierno y modelos

| Componente | Ámbito | Responsabilidad / datos | Relaciones | Estado y decisión |
| :--- | :--- | :--- | :--- | :--- |
| `x01` | frontera | X-01 · control de cruces · Bitácora mínima propia | Salidas: bitacora_x | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bitacora_x` | frontera | PostgreSQL de X-01 · Bitácora mínima de cruces · sin perfil unificado | Entradas: x01;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `services_r` | retail | Servicios y APIs propietarias · Transacción y outbox por contexto · Retail | Salidas: oper_r, bus_r, blob_r, embeddings, vector | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `oper_r` | retail | Azure PostgreSQL Flexible Server · Repositorios operacionales propios · Retail | Entradas: services_r, backup_r; Salidas: workers_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bus_r` | retail | Azure Service Bus Premium · Hechos confirmados · reintentos · Retail | Entradas: services_r; Salidas: workers_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `adf_r` | retail | Azure Data Factory · Orquestación · corte · manifiestos · Retail | Salidas: workers_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `workers_r` | retail | Java / Spring en AKS · Ingesta, calidad y proyecciones · Retail | Entradas: bus_r, oper_r, adf_r, lake_r; Salidas: lake_r, mart_r, search_r, metadata_r, archive_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `lake_r` | retail | ADLS Gen2 · Landing / curados · versionado · Retail | Entradas: workers_r; Salidas: workers_r, training | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `mart_r` | retail | Azure PostgreSQL Flexible Server · Modelos analíticos dedicados · Retail | Entradas: workers_r, bi_r, backup_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bi_r` | retail | Microsoft Power BI · Modelos, permisos y conexión privada · Retail | Salidas: mart_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `search_r` | retail | OpenSearch autogestionado · Búsqueda global · índice derivado · Retail | Entradas: workers_r, search_api_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `search_api_r` | retail | API de búsqueda global · Identidad y filtros por documento · Retail | Salidas: search_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `metadata_r` | retail | OpenMetadata autogestionado · Catálogo, calidad y linaje por API · Retail | Entradas: workers_r; Salidas: metadata_pg_r, metadata_idx_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `metadata_pg_r` | retail | PostgreSQL de OpenMetadata · Metadatos propios, sin muestreo libre · Retail | Entradas: metadata_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `metadata_idx_r` | retail | Buscador compatible de OpenMetadata · Dependencia dedicada · versión por validar · Retail | Entradas: metadata_r;  | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `blob_r` | retail | Azure Blob Storage · Documentos y evidencia vigente · Retail | Entradas: services_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `archive_r` | retail | Azure Blob Storage WORM · Archivo y evidencia retenida · Retail | Entradas: workers_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `backup_r` | retail | Azure Backup / PostgreSQL PITR · Cobertura y recuperación por recurso · Retail | Salidas: oper_r, mart_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `services_e` | emisor | Servicios y APIs propietarias · Transacción y outbox por contexto · Filial | Salidas: oper_e, bus_e, blob_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `oper_e` | emisor | Azure PostgreSQL Flexible Server · Repositorios operacionales propios · Filial | Entradas: services_e, backup_e; Salidas: workers_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bus_e` | emisor | Azure Service Bus Premium · Hechos confirmados · reintentos · Filial | Entradas: services_e; Salidas: workers_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `adf_e` | emisor | Azure Data Factory · Orquestación · corte · manifiestos · Filial | Salidas: workers_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `workers_e` | emisor | Java / Spring en AKS · Ingesta, calidad y proyecciones · Filial | Entradas: bus_e, oper_e, adf_e, lake_e; Salidas: lake_e, mart_e, search_e, metadata_e, archive_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `lake_e` | emisor | ADLS Gen2 · Landing / curados · versionado · Filial | Entradas: workers_e; Salidas: workers_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `mart_e` | emisor | Azure PostgreSQL Flexible Server · Modelos analíticos dedicados · Filial | Entradas: workers_e, bi_e, backup_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bi_e` | emisor | Microsoft Power BI · Modelos, permisos y conexión privada · Filial | Salidas: mart_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `search_e` | emisor | OpenSearch autogestionado · Búsqueda global · índice derivado · Filial | Entradas: workers_e, search_api_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `search_api_e` | emisor | API de búsqueda global · Identidad y filtros por documento · Filial | Salidas: search_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `metadata_e` | emisor | OpenMetadata autogestionado · Catálogo, calidad y linaje por API · Filial | Entradas: workers_e; Salidas: metadata_pg_e, metadata_idx_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `metadata_pg_e` | emisor | PostgreSQL de OpenMetadata · Metadatos propios, sin muestreo libre · Filial | Entradas: metadata_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `metadata_idx_e` | emisor | Buscador compatible de OpenMetadata · Dependencia dedicada · versión por validar · Filial | Entradas: metadata_e;  | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `blob_e` | emisor | Azure Blob Storage · Documentos y evidencia vigente · Filial | Entradas: services_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `archive_e` | emisor | Azure Blob Storage WORM · Archivo y evidencia retenida · Filial | Entradas: workers_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `backup_e` | emisor | Azure Backup / PostgreSQL PITR · Cobertura y recuperación por recurso · Filial | Salidas: oper_e, mart_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `vector` | retail | PostgreSQL / pgvector · Oferta: índice multimodal derivado | Entradas: embeddings, services_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `embeddings` | retail | Trabajador de representaciones · AKS · Modelo multimodal por seleccionar | Entradas: services_r; Salidas: vector | Conservar; configuración/compatibilidad por acreditar. No acredita aceptación. |
| `training` | retail | Python / scikit-learn · AKS · Conteo: evaluación temporal e inferencia | Entradas: lake_r, mlflow; Salidas: mlflow, recommendations | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `mlflow` | retail | MLflow autogestionado · Retail · Experimentos y versiones de modelos | Entradas: training; Salidas: mlflow_pg, mlflow_blob, training | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `mlflow_pg` | retail | PostgreSQL de MLflow · Retail · Metadatos de experimentos y modelos | Entradas: mlflow;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `mlflow_blob` | retail | Azure Blob Storage · Retail · Artefactos de modelos de MLflow | Entradas: mlflow;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `recommendations` | retail | Existencias · recomendaciones de conteo · Promoción humana · fallback · sin ajuste de stock | Entradas: training;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |

## 4.35 · Capas transversales · Seguridad y Observabilidad por ámbito

| Componente | Ámbito | Responsabilidad / datos | Relaciones | Estado y decisión |
| :--- | :--- | :--- | :--- | :--- |
| `x01` | frontera | X-01 · bitácora propia · Correlación mínima autorizada | Salidas: audit_r, otel_r, audit_e, otel_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `source_r` | retail | Canales, servicios, datos y trabajadores · RUM público entra por borde / APIM propio · Retail | Salidas: entra_r, external_r, workload_r, kv_r, hsm_r, audit_r, otel_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `admin_r` | retail | Administradores y equipos compatibles · Identidad, cumplimiento y privilegios · Retail | Entradas: intune_r, pim_r, endpoint_r; Salidas: entra_r, private_r, bastion_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `resources_r` | retail | Recursos privados autorizados · Máquinas / APIs de administración propias · Retail | Entradas: private_r, bastion_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `platform_r` | retail | Recursos Azure y endpoints propios · Plataforma, tiendas, CI/CD e incidentes · Retail | Entradas: cloud_r, prom_r, blackbox_r; Salidas: local_r, monitor_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `entra_r` | retail | Microsoft Entra ID P2 · Personal, MFA y acceso condicional · Retail | Entradas: source_r, admin_r; Salidas: sentinel_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `external_r` | retail | Microsoft Entra External ID · Clientes / titulares del ámbito · Retail | Entradas: source_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `intune_r` | retail | Microsoft Intune · Dispositivos compatibles y modo compartido · Retail | Salidas: admin_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `workload_r` | retail | Managed / Workload Identity · Identidades de cargas y permisos mínimos · Retail | Entradas: source_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `kv_r` | retail | Azure Key Vault · Secretos y certificados · Retail | Entradas: source_r; Salidas: sentinel_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `hsm_r` | retail | Azure Managed HSM · Claves y envoltura de claves de datos · Retail | Entradas: source_r; Salidas: sentinel_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `pim_r` | retail | Microsoft Entra PIM · Elevación temporal y aprobación · Retail | Salidas: admin_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bastion_r` | retail | Azure Bastion Premium · Salto y grabación de máquinas compatibles · Retail | Entradas: admin_r; Salidas: resources_r, stage_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `private_r` | retail | Microsoft Entra Private Access · Acceso administrativo a recursos privados · Retail | Entradas: admin_r; Salidas: resources_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `endpoint_r` | retail | Microsoft Defender for Endpoint · Protección de equipos compatibles · Retail | Salidas: admin_r, sentinel_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `cloud_r` | retail | Microsoft Defender for Cloud · Planes de cargas expresamente cubiertas · Retail | Salidas: platform_r, sentinel_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `sentinel_r` | retail | Microsoft Sentinel · SIEM · conectores y eventos seleccionados · Retail | Entradas: entra_r, endpoint_r, cloud_r, kv_r, hsm_r; Salidas: soc_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `otel_r` | retail | OpenTelemetry Collector · Instrumentación / RUM · colas durables · Retail | Entradas: source_r, local_r, x01; Salidas: loki_r, tempo_r, prom_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `prom_r` | retail | Prometheus · Métricas · OTLP HTTP / scrape · Retail | Entradas: otel_r, grafana_r; Salidas: platform_r, blackbox_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `loki_r` | retail | Grafana Loki · Registros operacionales saneados · Retail | Entradas: otel_r, grafana_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `tempo_r` | retail | Grafana Tempo · Trazas saneadas · Retail | Entradas: otel_r, grafana_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `monitor_r` | retail | Azure Monitor / Log Analytics · Diagnóstico Azure y seguridad necesaria · Retail | Entradas: platform_r, grafana_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `grafana_r` | retail | Grafana autogestionado · Consultas y Grafana Alerting integrado · Retail | Salidas: prom_r, loki_r, tempo_r, monitor_r, noc_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `blackbox_r` | retail | Prometheus Blackbox Exporter · Sondas externas e internas independientes · Retail | Entradas: prom_r; Salidas: platform_r, noc_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `stage_r` | retail | Azure Blob Storage temporal · Grabaciones: mutable, sin versionado · Retail | Entradas: bastion_r; Salidas: audit_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `audit_r` | retail | Trabajador durable de auditoría · Copiar, verificar y registrar integridad · Retail | Entradas: stage_r, source_r, x01; Salidas: worm_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `worm_r` | retail | Azure Blob Storage WORM · Archivo y evidencia propia del ámbito · Retail | Entradas: audit_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `soc_r` | retail | SOC del ámbito · operación 24×7 · Analistas, escalamiento y respuesta · Retail | Entradas: sentinel_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `local_r` | retail | OpenTelemetry Collector local · Cola persistente de al menos 24 horas · Retail | Entradas: platform_r; Salidas: otel_r | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `noc_r` | retail | NOC y avisos propios del ámbito · Salud mínima autorizada; sin payload sensible · Retail | Entradas: grafana_r, blackbox_r;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `source_e` | emisor | Canales, servicios, datos y trabajadores · RUM público entra por borde / APIM propio · Filial | Salidas: entra_e, external_e, workload_e, kv_e, hsm_e, audit_e, otel_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `admin_e` | emisor | Administradores y equipos compatibles · Identidad, cumplimiento y privilegios · Filial | Entradas: intune_e, pim_e, endpoint_e; Salidas: entra_e, private_e, bastion_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `resources_e` | emisor | Recursos privados autorizados · Máquinas / APIs de administración propias · Filial | Entradas: private_e, bastion_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `platform_e` | emisor | Recursos Azure y endpoints propios · Plataforma, tiendas, CI/CD e incidentes · Filial | Entradas: cloud_e, prom_e, blackbox_e; Salidas: local_e, monitor_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `entra_e` | emisor | Microsoft Entra ID P2 · Personal, MFA y acceso condicional · Filial | Entradas: source_e, admin_e; Salidas: sentinel_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `external_e` | emisor | Microsoft Entra External ID · Clientes / titulares del ámbito · Filial | Entradas: source_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `intune_e` | emisor | Microsoft Intune · Dispositivos compatibles y modo compartido · Filial | Salidas: admin_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `workload_e` | emisor | Managed / Workload Identity · Identidades de cargas y permisos mínimos · Filial | Entradas: source_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `kv_e` | emisor | Azure Key Vault · Secretos y certificados · Filial | Entradas: source_e; Salidas: sentinel_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `hsm_e` | emisor | Azure Managed HSM · Claves y envoltura de claves de datos · Filial | Entradas: source_e; Salidas: sentinel_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `pim_e` | emisor | Microsoft Entra PIM · Elevación temporal y aprobación · Filial | Salidas: admin_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `bastion_e` | emisor | Azure Bastion Premium · Salto y grabación de máquinas compatibles · Filial | Entradas: admin_e; Salidas: resources_e, stage_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `private_e` | emisor | Microsoft Entra Private Access · Acceso administrativo a recursos privados · Filial | Entradas: admin_e; Salidas: resources_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `endpoint_e` | emisor | Microsoft Defender for Endpoint · Protección de equipos compatibles · Filial | Salidas: admin_e, sentinel_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `cloud_e` | emisor | Microsoft Defender for Cloud · Planes de cargas expresamente cubiertas · Filial | Salidas: platform_e, sentinel_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `sentinel_e` | emisor | Microsoft Sentinel · SIEM · conectores y eventos seleccionados · Filial | Entradas: entra_e, endpoint_e, cloud_e, kv_e, hsm_e; Salidas: soc_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `otel_e` | emisor | OpenTelemetry Collector · Instrumentación / RUM · colas durables · Filial | Entradas: source_e, local_e, x01; Salidas: loki_e, tempo_e, prom_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `prom_e` | emisor | Prometheus · Métricas · OTLP HTTP / scrape · Filial | Entradas: otel_e, grafana_e; Salidas: platform_e, blackbox_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `loki_e` | emisor | Grafana Loki · Registros operacionales saneados · Filial | Entradas: otel_e, grafana_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `tempo_e` | emisor | Grafana Tempo · Trazas saneadas · Filial | Entradas: otel_e, grafana_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `monitor_e` | emisor | Azure Monitor / Log Analytics · Diagnóstico Azure y seguridad necesaria · Filial | Entradas: platform_e, grafana_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `grafana_e` | emisor | Grafana autogestionado · Consultas y Grafana Alerting integrado · Filial | Salidas: prom_e, loki_e, tempo_e, monitor_e, noc_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `blackbox_e` | emisor | Prometheus Blackbox Exporter · Sondas externas e internas independientes · Filial | Entradas: prom_e; Salidas: platform_e, noc_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `stage_e` | emisor | Azure Blob Storage temporal · Grabaciones: mutable, sin versionado · Filial | Entradas: bastion_e; Salidas: audit_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `audit_e` | emisor | Trabajador durable de auditoría · Copiar, verificar y registrar integridad · Filial | Entradas: stage_e, source_e, x01; Salidas: worm_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `worm_e` | emisor | Azure Blob Storage WORM · Archivo y evidencia propia del ámbito · Filial | Entradas: audit_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `soc_e` | emisor | SOC del ámbito · operación 24×7 · Analistas, escalamiento y respuesta · Filial | Entradas: sentinel_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `local_e` | emisor | OpenTelemetry Collector local · Cola persistente de al menos 24 horas · Filial | Entradas: platform_e; Salidas: otel_e | Conservar como diseño objetivo; capacidad y configuración por comprobar. |
| `noc_e` | emisor | NOC y avisos propios del ámbito · Salud mínima autorizada; sin payload sensible · Filial | Entradas: grafana_e, blackbox_e;  | Conservar como diseño objetivo; capacidad y configuración por comprobar. |

## Elementos sin aristas explícitas

No equivalen automáticamente a componentes sin uso: se distingue pertenencia, soporte de tecnología, política transversal y candidato.

| Vista | Elemento | Motivo / tratamiento |
| :--- | :--- | :--- |
| 4.33 | `aks_r` | Soporte tecnológico de la franja alineada; no es una dependencia en serie del tráfico. |
| 4.33 | `conteo` | Pertenencia visual y responsabilidad: Existencias. No necesita arista decorativa. |
| 4.33 | `lockers` | Pertenencia visual y responsabilidad: Pedidos. No necesita arista decorativa. |
| 4.33 | `busqueda` | Pertenencia visual y responsabilidad: Oferta. No necesita arista decorativa. |
| 4.33 | `media` | Pertenencia visual y responsabilidad: Oferta. No necesita arista decorativa. |
| 4.33 | `fila` | Pertenencia visual y responsabilidad: Clientes Retail. No necesita arista decorativa. |
| 4.33 | `tech_ui` | Soporte tecnológico de la franja alineada; no es una dependencia en serie del tráfico. |
| 4.33 | `tech_java` | Soporte tecnológico de la franja alineada; no es una dependencia en serie del tráfico. |
| 4.33 | `tech_spring` | Soporte tecnológico de la franja alineada; no es una dependencia en serie del tráfico. |
| 4.33 | `regulatorio` | Sin contratos operacionales por ser candidato. |
| 4.33 | `security_summary` | Política transversal, desarrollada en página 3; no es un producto adicional. |
| 4.33 | `observability_summary` | Política transversal, desarrollada en página 3; no es un producto adicional. |

Los servicios conservan los contratos agrupados en el contorno del área. Las innovaciones conservan su dueño por pertenencia al área. F:C-04 es el único candidato de servicio de negocio aislado. No se inventaron consumidores para cerrarlo.

Uso de IA: Alto. Sin revisión humana formal.
