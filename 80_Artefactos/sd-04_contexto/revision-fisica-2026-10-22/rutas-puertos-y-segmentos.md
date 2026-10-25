# Rutas, puertos y segmentos de la propuesta física

Estado de diseño, 22-10-2026. Esta tabla no es una configuración aplicada ni una autorización para abrir puertos entre negocios. La IP final, el FQDN, el certificado y la identidad se registran por recurso antes de implementar.

## Reglas comunes

Se proponen dominios de conectividad propios de Retail y Filial. El tenant financiero y la custodia de Frontera siguen pendientes de confirmación expresa. El peering, cuando se utilice dentro de un ámbito, no concede por sí solo acceso; NSG, UDR, firewall y política Kubernetes limitan las rutas.

APIM se inyecta en su subred y usa la VIP/hostname de un Service interno de AKS. CNI Overlay no convierte las IP de pods en backends accesibles directamente desde cualquier subred. Se mantienen TLS y autorización en el receptor. El ILB es L4; la API continúa gobernada por APIM. El camino de los recursos web se distingue del de APIs.

| Inicio de conexión | Destino | Protocolo previsto | Restricción |
| --- | --- | --- | --- |
| Navegador/app pública | Front Door del ámbito | HTTPS 443 | Host, WAF, límites y autenticación según canal. |
| Front Door | Origen App Gateway | HTTPS privado | Private Link en región soportada; tránsito aprobado y origen restringido. |
| Sitio | VPN Gateway del ámbito | IPsec, UDP 500/4500 según configuración | Peer, identidad, prefijos y rutas propios; probar NAT-T y respaldo. |
| Sitio/DC | DNS privado del ámbito | DNS UDP/TCP 53 por conectividad autorizada | Reenvío condicional; no resolver financiero abierto a Retail. |
| App Gateway | APIM interno propio | HTTPS 443 | Host/SNI, probe y certificado; listener/ruta API. |
| App Gateway | Backend web privado propio | HTTPS 443 | Solo contenido/UI; no bypass hacia APIs operacionales. |
| APIM | VIP interna del servicio | HTTPS 443 | Backend registrado, token/identidad y autorización de negocio. |
| ILB / Service | Pods seleccionados | Puerto TLS del servicio | Reglas administradas AKS y políticas de red; sin endpoint público de los pods. |
| Ventas | Entrada X-01 | HTTPS 443 privado | Únicamente compra autorizable y ficha de cruce aprobada. |
| X-01 | PE/listener financiero | HTTPS 443 privado | Solo identidad X-01, contrato mínimo y retorno limitado. |
| Servicio propietario | PE PostgreSQL propio | PostgreSQL TLS 5432 | Base/rol propio; no permisos de superusuario del servidor. |
| Productor/consumidor | PE Service Bus propio | AMQPS TLS 5671; alternativa soportada por verificar | Cliente inicia; namespace/cola/tópico autorizado, nunca el otro ámbito. |
| Workers/índices | PE Blob/DFS del ámbito | HTTPS 443 | Cuenta y subrecurso propios; corte, manifiesto e idempotencia. |
| SHIR | Control de Data Factory | Canal saliente soportado | Identidad/registro del runtime; FQDN y excepciones de plataforma declarados. |
| SHIR | APIs privadas de trabajos | HTTPS 443 | REST acotado para iniciar/consultar trabajos; sin control libre del clúster. |
| VM de data gateway BI | Servicio/Relay de datos | Canal saliente HTTPS soportado | Listas de salida del producto; no exponer la VM a consultas entrantes de Internet. |
| VM de data gateway BI | PE PostgreSQL analítico | PostgreSQL TLS 5432 | Solo modelo de lectura; no credenciales operacionales. |
| Carga autorizada | Key Vault/HSM | HTTPS 443 | Workload Identity/identidad soportada y operación criptográfica permitida. |
| Agente/aplicación | Collector propio | OTLP TLS sobre puerto fijado en configuración | Receptor privado autenticado; señales filtradas y limitadas. |
| Collector | Loki/Tempo/Prometheus | Endpoints OTLP soportados por versión | Destino por señal y ámbito; no duplicar series por scrape e ingestión. |
| Grafana | Backends propios / Azure Monitor | API HTTPS del backend | Lectura limitada y consultas del ámbito. |
| Equipo administrativo | Private Access / Bastion | Recorrido administrativo soportado | MFA, elevación PIM y acceso mínimo; sin RDP/SSH público de servidores. |
| R/F-PA-01/02 | Entra Private Access global | Canal saliente TLS 443; CRL 80 según lista oficial | Dos conectores Windows por ámbito; sin interceptar/terminar TLS del conector. |
| Conector privado | Bastion del ámbito | HTTPS 443; integración por demostrar | Resolver, cliente y autenticación en PoC; el cliente nativo de Bastion no aporta grabación. |
| Bastion | VM autorizada | SSH 22 / RDP 3389, según destino | Nunca abrir esos puertos al público ni asumir grabación para todo protocolo/cliente. |

Esta lista cubre los recorridos de la solución. Los servicios administrados también tienen dependencias de gestión, actualización, identidad y diagnóstico que deben enumerarse desde sus versiones elegidas. En particular, el modo interno de APIM no elimina todas las conexiones de plataforma; no se aplicará un «deny all» que impida su gestión ni se interpretará una dependencia interna de Microsoft como otro broker de negocio.

## Segmentos propuestos

Las reservas de las figuras orientan la separación y deben validarse contra el direccionamiento real. No se asignan aquí IP que puedan solaparse con la WAN.

| Segmento | Qué contiene | Separación requerida |
| --- | --- | --- |
| GatewaySubnet | VPN Gateway y, si se aprueba, gateway ExpressRoute. | Tamaño y coexistencia según SKU; no ubicar App Gateway allí. |
| AzureFirewallSubnet | Azure Firewall propio. | Rutas y retorno simétrico; restricciones del servicio. |
| DNS inbound / outbound | Endpoints de DNS Resolver. | Subred dedicada por endpoint y dominio. |
| AzureBastionSubnet | Bastion Premium. | Reglas obligatorias del producto y destino de grabación. |
| snet-ingress | Application Gateway v2. | Subred dedicada; listener de web separado del de APIs. |
| snet-apim | APIM Premium interno. | Dependencias, NSG, DNS y UDR probados. |
| snet-aks | NIC de nodos VMSS. | Pools, CNI Overlay, rangos de pods/Services y políticas por dominio. |
| snet-pe | Interfaces de endpoints privados. | PE y DNS de cada servidor/recurso/subrecurso. |
| snet-bi | VM de gateway de datos. | Solo salida de servicio y consulta analítica autorizada. |
| snet-ir | VM SHIR. | Ejecución/canales propios, sin reutilizar VM de BI. |
| VLAN cajas | POS y periféricos. | Solo nodos y servicios necesarios. |
| VLAN sala/administración | Terminales y AP corporativo. | Sesión nominativa, dispositivo compatible y ACL. |
| VLAN Filial | Mesón y equipos financieros aislados. | Túnel, claves, custodia y cupo propios. |
| VLAN IoT | Controladores lockers y dispositivos autorizados. | Sin acceso directo a DB, cupo ni red administrativa. |
| VLAN video | Cámaras y NVR. | Sin acceso a redes de negocio. |
| VLAN invitados | Wi-Fi de clientes. | Salida a Internet y aislamiento de clientes. |

## Capacidad y cantidades que deben recalcularse

La propuesta de pools distribuidos representa 15 nodos base para Retail, 15 para Filial y 6 para X-01. Son 36 VM de AKS en la topología inicial dibujada, sin batch elástico ni recursos administrados. Se proponen además cuatro VM de gateway BI, cuatro de SHIR cloud y cuatro conectores Private Access. **Esos 48 nodos cloud no son capacidad aprobada ni una cotización.** A ellos se añaden las sondas independientes `R-SYN-01` y `F-SYN-01`, cuya ubicación cloud o en sitio queda pendiente y no se suma al emplazamiento Chile. Se evalúan pools combinables dentro de un mismo ámbito cuando las pruebas acrediten aislamiento y recuperación equivalentes; nunca se consolida Retail con Filial por esa razón.

Los pares SHIR de DC-01 son otros equipos de integración locales y no se suman de nuevo como nodos AKS. La duplicación de clases en distintas vistas no multiplica recursos.

El patrón de tienda conserva dos nodos Retail y propone custodia financiera aislada en un par adicional. Si se decide que ese par requiere dos hosts físicos dedicados en cada una de las 22 tiendas, añade 44 equipos a los 44 Retail de referencia. La alternativa de VM financieras sobre hardware autorizado debe demostrar aislamiento de administración, claves, recursos y fencing; el rótulo Host/VM de la figura mantiene abierta esa decisión. T-11, energía, rack, soporte y responsabilidad de suministro deben conciliarse antes de cerrar cantidad y costo.

Los servidores PostgreSQL administrados representan recursos y sus roles primario/espera, no VM maestras a proveer. Para cada uno hay que calcular vCore, memoria, disco, IOPS, WAL, crecimiento, réplica y recuperación. Los índices y la telemetría añaden almacenamiento que la memoria anterior no consideraba.
