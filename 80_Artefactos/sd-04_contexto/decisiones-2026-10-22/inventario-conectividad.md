# Inventario de conectividad

Figura 4.27: 84 tarjetas y 87 relaciones explícitas. Cero aristas no equivale automáticamente a componente prescindible.

Hay 15 tarjetas sin aristas: 7 funcionales con contrato pendiente y 8 de alojamiento/control transversal. Los dos lagos solo tienen salida a BI.

Los nombres agrupados de PostgreSQL, BI, respaldo y controles no implican instancias, redes, bases ni credenciales compartidas entre negocios.

| ID de tarjeta | Componente | Rol | Entradas | Salidas | Estado |
| :--- | :--- | :--- | ---: | ---: | :--- |
| `a_cliente` | Cliente de la tienda | actor | 0 | 1 | objetivo |
| `a_tienda` | Vendedor, cajero y operación de tienda | actor | 0 | 2 | objetivo |
| `a_cd` | Personal del centro de distribución | actor | 0 | 1 | objetivo |
| `a_comercial` | Atención, comercial y planificación | actor | 0 | 1 | objetivo |
| `a_emisor` | Titular de tarjeta y ejecutivo financiero | actor | 0 | 2 | objetivo |
| `web` | Portal y app de la tienda / React / React Native | operacion | 1 | 1 | objetivo |
| `pos` | Caja y mesón / React web servido desde tienda | operacion | 1 | 2 | objetivo |
| `operacion` | App interna de tienda / 4 perfiles · RN / SQLite / DataWedge / QR + PIN en vista previa | operacion | 1 | 1 | por_acreditar |
| `logistica` | Vista logística / WMS del CD conservado | operacion | 1 | 1 | objetivo |
| `movil` | Consola comercial y de atención | operacion | 1 | 1 | objetivo |
| `portal_f` | Portal y app de la tarjeta / Código propio · simulador CAE | operacion | 1 | 1 | objetivo |
| `meson_f` | Mesón financiero / Sesión y permisos de la Filial | operacion | 1 | 2 | objetivo |
| `dns` | Azure DNS / Zonas y registros por ámbito | configuracion | 0 | 2 | objetivo |
| `appgw_r` | Application Gateway v2 / Retail · entrada privada | operacion | 6 | 1 | objetivo |
| `apim_r` | Azure API Management / Premium clásico · Retail / Productos y cuotas por canal | operacion | 2 | 9 | objetivo |
| `apic_r` | Azure API Center / Retail · catálogo OpenAPI 3.1 | configuracion | 0 | 1 | objetivo |
| `appgw_e` | Application Gateway v2 / Filial · entrada privada | operacion | 2 | 1 | objetivo |
| `apim_e` | Azure API Management / Premium clásico · Filial / Producto: Finanzas abiertas | operacion | 3 | 3 | objetivo |
| `apic_e` | Azure API Center / Filial · catálogo OpenAPI 3.1 | configuracion | 0 | 1 | objetivo |
| `aks_r` | Azure Kubernetes Service / Premium / LTS · un clúster por ámbito | contenedor | 0 | 0 | por_acreditar |
| `oferta` | Oferta comercial | operacion | 1 | 6 | objetivo |
| `abastecimiento` | Abastecimiento | operacion | 1 | 1 | objetivo |
| `existencias` | Existencias · sugerencias de IA | operacion | 1 | 3 | objetivo |
| `pedidos` | Pedidos | operacion | 1 | 3 | objetivo |
| `ventas` | Ventas | operacion | 1 | 3 | objetivo |
| `comisiones` | Comisiones | operacion | 1 | 1 | objetivo |
| `market` | Marketplace | operacion | 1 | 2 | objetivo |
| `posventa` | Posventa | operacion | 1 | 1 | objetivo |
| `clientes` | Clientes Retail | operacion | 2 | 2 | objetivo |
| `originacion` | Originación de crédito | operacion | 1 | 2 | objetivo |
| `cartera` | Cartera de crédito | operacion | 1 | 3 | objetivo |
| `evidencia` | Evidencia y consentimiento | operacion | 1 | 2 | objetivo |
| `x01` | Control de cruces | operacion | 1 | 2 | objetivo |
| `comunes_r` | Servicios comunes · Retail / Parámetros, documentos, firma, avisos… | pendiente_conexion | 0 | 0 | por_acreditar |
| `comunes_e` | Servicios comunes · Filial / Parámetros, documentos, firma, avisos… | pendiente_conexion | 0 | 0 | por_acreditar |
| `conteo` | Conteo cíclico predictivo · proceso | capacidad | 1 | 0 | objetivo |
| `lockers` | Lockers Ancoa 24/7 · producto | capacidad | 1 | 0 | objetivo |
| `busqueda` | Búsqueda vectorial multimodal · tecnología | capacidad | 1 | 0 | objetivo |
| `media` | Retail Media Network · modelo de negocio | capacidad | 1 | 0 | objetivo |
| `fila` | Modo Tienda y fila virtual · experiencia | capacidad | 1 | 0 | objetivo |
| `bus_r` | Azure Service Bus Premium / Retail · outbox / reintentos | operacion | 5 | 5 | objetivo |
| `saga_r` | Coordinación de procesos · Retail / Motor y sagas pendientes | pendiente_conexion | 0 | 0 | por_acreditar |
| `bus_e` | Azure Service Bus Premium / Filial · outbox / reintentos | operacion | 3 | 1 | objetivo |
| `saga_e` | Coordinación de procesos · Filial / Motor y sagas pendientes | pendiente_conexion | 0 | 0 | por_acreditar |
| `comercio` | Comercio · ERP/DTE y WMS | operacion | 1 | 1 | objetivo |
| `canales` | Canales · e-commerce / marketplace / fidelización | operacion | 1 | 1 | objetivo |
| `socios` | Socios · pagos / proveedores / transportistas | operacion | 1 | 1 | objetivo |
| `credito` | Crédito · legado 2011 / CMF / firma | operacion | 1 | 1 | objetivo |
| `local_serv` | Continuidad de tienda / Ventas y oferta en modo local | operacion | 1 | 2 | objetivo |
| `local_sync` | Sincronizador de tienda / Reintentos y conciliación | operacion | 3 | 1 | objetivo |
| `datos_merc` | PostgreSQL · Retail / Oferta / Abastecimiento / Existencias | operacion | 3 | 0 | objetivo |
| `datos_venta` | PostgreSQL · Retail / Pedidos / Ventas / Comisiones / Marketplace | operacion | 4 | 0 | objetivo |
| `datos_clientes` | PostgreSQL · Retail / Posventa / Clientes | operacion | 2 | 0 | objetivo |
| `bitacora` | PostgreSQL · Control de cruces / Bitácora y política propias | operacion | 1 | 0 | objetivo |
| `datos_orig` | PostgreSQL · Filial / Originación y estado de procesos | operacion | 1 | 0 | objetivo |
| `datos_cartera` | PostgreSQL · Filial / Cartera y estado de procesos | operacion | 1 | 0 | objetivo |
| `datos_evid` | Azure Blob Storage · Filial / Evidencia y consentimiento | operacion | 1 | 0 | objetivo |
| `archivo_r` | Blob / Data Lake · Retail / Retención inmutable e histórico | operacion | 0 | 0 | objetivo |
| `archivo_e` | Blob / Data Lake · Filial / Retención inmutable e histórico | operacion | 0 | 0 | objetivo |
| `lago_r` | Data Lake Storage Gen2 · Retail / Modelos analíticos propios | operacion | 0 | 1 | objetivo |
| `lago_e` | Data Lake Storage Gen2 · Filial / Posición financiera y modelos propios | operacion | 0 | 1 | objetivo |
| `redis` | Azure Managed Redis · Retail / Caché de oferta ≤ 30 s | operacion | 1 | 0 | por_acreditar |
| `historial` | PostgreSQL · Retail / Historial de precios append-only | operacion | 1 | 0 | objetivo |
| `powerbi` | Microsoft Power BI / Espacios y modelos por ámbito | operacion | 2 | 0 | por_acreditar |
| `backup` | Azure Backup Vault / Cobertura y destino por definir | pendiente_conexion | 0 | 0 | por_acreditar |
| `local_data` | Diario local de tienda / Persistencia durable de ventas Retail | operacion | 1 | 1 | objetivo |
| `cupo_local` | Cupo local de la Filial / VM y clave propias · datos mínimos | operacion | 2 | 0 | por_acreditar |
| `ext_comercio` | ERP/DTE y WMS conservados | externo | 1 | 0 | objetivo |
| `ext_canales` | E-commerce, marketplace y fidelización | externo | 1 | 0 | objetivo |
| `ext_socios` | Pagos, proveedores y transportistas / Lockers y publicidad: interfaz por precisar | externo | 1 | 0 | objetivo |
| `ext_credito` | Crédito 2011 (convivencia) / Reportes CMF y firma por interfaz | externo | 1 | 0 | convivencia |
| `entra` | Microsoft Entra ID P2 / Tenant Filial separado: confirmar | transversal | 0 | 0 | por_acreditar |
| `externalid` | Microsoft Entra External ID / Tenant externo por negocio | transversal | 0 | 0 | objetivo |
| `kv` | Azure Key Vault / Managed HSM / Claves y cifrado de campo por ámbito | transversal | 0 | 0 | por_acreditar |
| `sentinel` | Microsoft Sentinel y Defender / SOC: solo incidentes agregados | transversal | 0 | 0 | por_acreditar |
| `privado` | PIM / Bastion / Private Access / Administración y acceso remoto | transversal | 0 | 0 | por_acreditar |
| `otel` | OpenTelemetry Collector / Por clúster y tienda · cola local 24 h | transversal | 0 | 1 | por_acreditar |
| `monitor` | Azure Monitor / Log Analytics / Espacios por ámbito; exportador a probar | transversal | 1 | 1 | por_acreditar |
| `grafana` | Prometheus / Azure Managed Grafana / Indicadores, anomalías y vista NOC | transversal | 1 | 0 | por_acreditar |
| `arc` | Azure Arc / Azure Monitor Agent / Operación de servidores locales | transversal | 0 | 0 | objetivo |
| `rum` | Pruebas sintéticas y experiencia real / TLS y herramienta móvil pendientes | transversal | 0 | 0 | por_acreditar |
| `pl_r` | Azure Private Link | operacion | 1 | 1 | por_acreditar |
| `pl_e` | Azure Private Link | operacion | 1 | 1 | por_acreditar |
| `front_door` | Azure Front Door Premium / Retail / Filial: perfiles separados / WAF propio por ámbito · TLS 1.3 objetivo | producto_agrupado | 4 | 2 | por_acreditar |

## Relaciones explícitas

El texto aparece como información de cada conector en SVG/draw.io; se conserva completo aquí para revisar su intención.

| Origen | Destino | Relación | Intención |
| :--- | :--- | :--- | :--- |
| `a_cliente` | `web` | solicitud | Canal del perfil autorizado |
| `a_tienda` | `pos` | solicitud | Canal del perfil autorizado |
| `a_tienda` | `operacion` | solicitud | Canal del perfil autorizado |
| `a_cd` | `logistica` | solicitud | Canal del perfil autorizado |
| `a_comercial` | `movil` | solicitud | Canal del perfil autorizado |
| `a_emisor` | `portal_f` | solicitud | Canal del perfil autorizado |
| `a_emisor` | `meson_f` | solicitud | Canal del perfil autorizado |
| `dns` | `front_door` | politica | Retail: host y perfil propios. Resolución de nombres / configuración; no es proxy |
| `dns` | `front_door` | politica | Filial: host y perfil propios. Resolución de nombres / configuración; no es proxy |
| `front_door` | `pl_r` | condicionado | Retail: perfil y origen exclusivos del ámbito. HTTPS por Azure Private Link · tránsito Brazil South condicionado a D-45 |
| `appgw_r` | `apim_r` | solicitud | HTTPS privado al gateway del mismo ámbito |
| `apic_r` | `apim_r` | politica | Contratos 3.0.3 derivados por pipeline; NO tráfico de aplicación |
| `front_door` | `pl_e` | condicionado | Filial: perfil y origen exclusivos del ámbito. HTTPS por Azure Private Link · tránsito Brazil South condicionado a D-45 |
| `appgw_e` | `apim_e` | solicitud | HTTPS privado al gateway del mismo ámbito |
| `apic_e` | `apim_e` | politica | Contratos 3.0.3 derivados por pipeline; NO tráfico de aplicación |
| `web` | `front_door` | solicitud | Retail: host y perfil propios. API pública Retail |
| `portal_f` | `front_door` | solicitud | Filial: host y perfil propios. API pública Filial; borde sujeto a residencia aprobada |
| `pos` | `appgw_r` | solicitud | Red privada tiendas / CD / DC-01 · SD-WAN y ExpressRoute; omite Front Door |
| `operacion` | `appgw_r` | solicitud | Red privada tiendas / CD / DC-01 · SD-WAN y ExpressRoute; omite Front Door |
| `logistica` | `appgw_r` | solicitud | Red privada tiendas / CD / DC-01 · SD-WAN y ExpressRoute; omite Front Door |
| `movil` | `appgw_r` | solicitud | Red privada tiendas / CD / DC-01 · SD-WAN y ExpressRoute; omite Front Door |
| `meson_f` | `appgw_e` | solicitud | Red privada del mesón financiero; omite Front Door |
| `apim_r` | `oferta` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_r` | `abastecimiento` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_r` | `existencias` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_r` | `pedidos` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_r` | `ventas` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_r` | `comisiones` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_r` | `market` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_r` | `posventa` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_r` | `clientes` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_e` | `originacion` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_e` | `cartera` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `apim_e` | `evidencia` | solicitud | Operaciones publicadas del servicio; autorización propia |
| `ventas` | `x01` | compra_autorizable | Compra con tarjeta propia: solicitud mínima de autorización |
| `x01` | `apim_e` | compra_autorizable | Única identidad de Retail admitida por la puerta de la Filial; nuevo correlativo |
| `existencias` | `conteo` | politica | Capacidad de innovación del servicio, no nuevo microservicio |
| `pedidos` | `lockers` | politica | Capacidad de innovación del servicio, no nuevo microservicio |
| `oferta` | `busqueda` | politica | Capacidad de innovación del servicio, no nuevo microservicio |
| `oferta` | `media` | politica | Capacidad de innovación del servicio, no nuevo microservicio |
| `clientes` | `fila` | politica | Capacidad de innovación del servicio, no nuevo microservicio |
| `bus_r` | `comercio` | consumo | Consumo de hechos propios; traducción y deduplicación |
| `bus_r` | `canales` | consumo | Consumo de hechos propios; traducción y deduplicación |
| `bus_r` | `socios` | consumo | Consumo de hechos propios; traducción y deduplicación |
| `bus_e` | `credito` | consumo | Consumo de hechos propios; traducción y deduplicación |
| `oferta` | `bus_r` | publicacion | Hechos del productor vía outbox transaccional |
| `existencias` | `bus_r` | publicacion | Hechos del productor vía outbox transaccional |
| `pedidos` | `bus_r` | publicacion | Hechos del productor vía outbox transaccional |
| `ventas` | `bus_r` | publicacion | Hechos del productor vía outbox transaccional |
| `market` | `bus_r` | publicacion | Hechos del productor vía outbox transaccional |
| `originacion` | `bus_e` | publicacion | Hechos del lado receptor, sin bus compartido |
| `cartera` | `bus_e` | publicacion | Hechos del lado receptor, sin bus compartido |
| `evidencia` | `bus_e` | publicacion | Hechos del lado receptor, sin bus compartido |
| `bus_r` | `clientes` | consumo | Consumo para la fila virtual; contrato por detallar |
| `pos` | `local_serv` | solicitud | Operación local cuando no hay enlace |
| `local_serv` | `local_sync` | publicacion | Entrega de operaciones para reconciliar |
| `local_sync` | `appgw_r` | solicitud | Reenvío por red privada hacia APIs Retail; nunca escritura directa en BD |
| `oferta` | `datos_merc` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `abastecimiento` | `datos_merc` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `existencias` | `datos_merc` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `pedidos` | `datos_venta` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `ventas` | `datos_venta` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `comisiones` | `datos_venta` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `market` | `datos_venta` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `posventa` | `datos_clientes` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `clientes` | `datos_clientes` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `x01` | `bitacora` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `originacion` | `datos_orig` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `cartera` | `datos_cartera` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `evidencia` | `datos_evid` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| `oferta` | `redis` | persistencia | Publicación/consulta de oferta operacional; frescura por verificar |
| `oferta` | `historial` | persistencia | Registro de precios publicados; solo anexado |
| `lago_r` | `powerbi` | flujo | Consulta analítica Retail; sin mezcla de modelos |
| `lago_e` | `powerbi` | flujo | Consulta analítica Filial; espacios separados |
| `local_serv` | `local_data` | persistencia | Diario transaccional local Retail |
| `local_data` | `local_sync` | flujo | Operaciones pendientes del diario |
| `cartera` | `cupo_local` | condicionado | Provisionar referencia seudonimizada, cupo y vigencia; ruta y caducidad pendientes |
| `meson_f` | `cupo_local` | condicionado | Consulta local en red del mesón; política offline pendiente |
| `comercio` | `ext_comercio` | adaptacion | Familia de interfaces bidireccionales; contratos y olas en inventario E1 |
| `canales` | `ext_canales` | adaptacion | Familia de interfaces bidireccionales; contratos y olas en inventario E1 |
| `socios` | `ext_socios` | adaptacion | Familia de interfaces bidireccionales; contratos y olas en inventario E1 |
| `credito` | `ext_credito` | adaptacion | Familia de interfaces bidireccionales; contratos y olas en inventario E1 |
| `otel` | `monitor` | condicionado | OTLP por colector del ámbito; exportador pendiente |
| `monitor` | `grafana` | condicionado | Consulta de métricas y salud por ámbito; agregación entre tenants pendiente |
| `pl_r` | `appgw_r` | condicionado | Origen privado Application Gateway del ámbito; región y residencia por verificar |
| `pl_e` | `appgw_e` | condicionado | Origen privado Application Gateway del ámbito; región y residencia por verificar |
| `bus_r` | `local_sync` | consumo | Cambios de oferta confirmados hacia caché local; contrato, entrega y conciliación por cerrar |
