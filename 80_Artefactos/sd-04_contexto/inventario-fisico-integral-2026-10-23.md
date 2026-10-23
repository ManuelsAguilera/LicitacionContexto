# Inventario maestro integral de infraestructura y conexiones

**Multitiendas Ancoa — Only Simple Solutions**  
**Fecha:** 23-10-2026 · **Versión:** 4 consolidada · **Estado:** diseño por zonas para revisión; levantamiento y pruebas pendientes · **Uso de IA:** Alto.

**Actualización vigente:** la figura 4.52 ampliada contiene 46 nodos y 51 enlaces, desglosados en CSV con posiciones, zonas, dominios y rutas. La disposición vigente tiene actores públicos y administración arriba, nube central y sitios Ancoa debajo; las iteraciones resumidas quedan como antecedentes. Las 32 partidas de suministro se desarrollan en la [matriz de responsabilidades y costos](cierre-inventario/12-matriz-suministro-costos.md), con [CSV por partida](cierre-inventario/12-matriz-suministro-costos.csv); la [matriz de red](cierre-inventario/13-matriz-red-y-diagrama.md) fija VLAN/VRF, salidas autorizadas y criterios visuales. La sección 14 reúne 52 familias de conexiones de datos/control y cuatro relaciones de alimentación; no equivalen una a una a flechas del dibujo.

**Lectura vigente de cantidades y decisiones:** las [fichas de cierre](cierre-inventario/) desarrollan cada zona. La capacidad inicial de diseño fija los pools BIZ en 5 nodos cada uno: **40 VM AKS**, 12 VM auxiliares y 2 sondas = **54 VM de producción en Chile**, más batch de 0–3 nodos. La modalidad DR es activo-pasivo templado, con **50 VM activas de espera en Brasil y 4 VM BI reproducibles apagadas**; es capacidad de reserva técnica, no despliegue acreditado. Hay 12 PostgreSQL productivos con 4.500 GiB de reserva inicial propuesta, dos namespaces Service Bus y copias propias hacia Brazil South. La decisión final de tienda fija **dos hosts R y dos F por sitio: 88 hosts para las 22 tiendas**; X-01 local aislado se ejecuta dentro del par F y no añade un quinto host. No se identificó en las Bases consultadas un dataset financiero nuevo que deba residir físicamente en el DC: la reserva de nueva custodia financiera en DC es **cero hasta fuente expresa**, y el crédito 2011 queda solo en convivencia transitoria.

La [revisión cruzada](cierre-inventario/08-revision-cruzada.md) completó los ocho encargos y registra 14 hallazgos. El usuario resolvió la arquitectura de H-01/H-02: par redundante por negocio y X-01 local aislado en F. Las fichas de tienda/revisión reflejan conmutación, identidad, bitácora y pruebas de aceptación; no se declara conformidad operativa antes de ensayarlas. La retención de eventos de seguridad se corrigió a 12 meses en línea más 24 adicionales en archivo, conforme RT-11.14.

## 1. Propósito y reglas de lectura

Este documento reúne los elementos que deben aparecer, directamente o mediante una agrupación trazable, en las próximas vistas físicas. Incluye nube de producción, recuperación, ambientes inferiores, tiendas, centros de distribución, instalaciones corporativas y terceros. La general ya se reconstruyó a partir de los CSV; las fichas desarrollan cada zona y las siguientes modificaciones deben conservar la correspondencia entre inventario, datos de edición y figura. La figura general vigente de esta integración es [4.52](cierre-inventario/09-diagrama-general.md).

Es un inventario de diseño, no un descubrimiento de recursos desplegados ni una lista de compra. Las cantidades nuevas son reservas iniciales de diseño con supuestos descritos en las fichas; el parque conservado requiere levantamiento nominal. No acreditan capacidad, disponibilidad regional de cada SKU ni hardware existente. Cuando falta un dato se deja identificado, sin convertirlo en una decisión.

**Decisiones confirmadas por el usuario:** producción Retail y Filial en **Chile Central**; recuperación de ambos en **Brazil South**. Los pendientes antiguos sobre el destino financiero quedan superados. La separación de datos, identidades, administración, mensajería y claves se mantiene en ambas regiones. La ubicación regional de servicios globales/SaaS y sus metadatos se verifica por producto; no se deduce de la región de AKS.

**Corrección posterior del usuario:** cada tienda tendrá **dos hosts Retail y dos Filial** y redes separadas; X-01 local aislado funciona en el par Filial durante la desconexión. Esta decisión reemplaza el patrón intermedio de un host por negocio. La ejecución financiera principal estará en la nube; en el DC permanecerán sistemas externos o conservados que deban convivir y solamente los datos cuya custodia local sea obligatoria. La clase exacta de esos datos exige verificar su fuente.

Se distinguen cinco clases: equipo físico, VM/nodo de cómputo, contenedor/proceso, recurso administrado y configuración de red/seguridad. Una VNet, un namespace, un Service de Kubernetes, una base lógica y una política no se cuentan como servidores. Un pool VMSS contiene nodos VM; esos nodos alojan pods y no vuelven a contarse como VM adicionales por cada contenedor.

Las tablas usan **R** para Retail, **F** para Filial y **X** para Frontera X-01. La expresión «por ámbito» significa instancias y permisos separados; no un recurso compartido. Los IDs son nombres de diseño, no nombres obtenidos de Azure. Los sitios sin inventario nominal se describen mediante patrones repetibles.

## 2. Fuentes y alcance de la consolidación

| Ref. | Fuente | Uso y precedencia |
| --- | --- | --- |
| S1 | [Explicación del diagrama lógico recibido](explicacion-diagrama-columnas-2026-10-23/README.md) | Componentes, propósito, fundamentos y referencias técnicas FI/FT; incluye las piezas añadidas en la imagen del usuario. |
| S2 | [Decisiones del 23 de octubre](fisica-general-zonas-2026-10-23/decisiones-2026-10-23.md) | Emplazamiento confirmado y presentación gráfica. Prevalece sobre los pendientes anteriores de ubicación. |
| S3 | [Matriz de despliegue anterior](revision-fisica-2026-10-22/matriz-despliegue.md) | Antecedente de servicios y alojamiento; las cantidades vigentes son las de las fichas A/G. |
| S4 | [Inventario anterior](revision-fisica-2026-10-22/inventario-nodos.md) | Detalle de nube y sitios; sus símbolos agregados se descomponen aquí sin multiplicarlos. |
| S5 | [Cobertura lógica a física](revision-fisica-2026-10-22/cobertura-logica-fisica.md) | Alojamiento de canales, innovaciones, capacidades comunes y herramientas. |
| S6 | [Rutas, puertos y segmentos](revision-fisica-2026-10-22/rutas-puertos-y-segmentos.md) | Conectividad de diseño y restricciones. Puertos sujetos a versión/configuración. |
| S7 | [General vigente 4.52](cierre-inventario/09-diagrama-general.md) | 46 nodos, 51 conexiones, iconos y disposición por zonas; editable y exportaciones. |
| S8 | [A · cómputo](cierre-inventario/01-computo-aks.md), [B · red](cierre-inventario/02-red-cloud.md), [C · tienda](cierre-inventario/03-tienda.md) | Capacidad inicial, hubs/radios, reservas IP y cuatro hosts por tienda con X-01 local. |
| S9 | [D · datos](cierre-inventario/04-datos-custodia.md), [E · DC/CD](cierre-inventario/05-dc-cd-externos.md), [F · seguridad](cierre-inventario/06-seguridad-operacion.md), [G · DR](cierre-inventario/07-dr-ambientes.md) | Cantidades, reservas, custodia, convivencia, seguridad, recuperación y ambientes vigentes. |
| S10 | [10 · espacio](cierre-inventario/10-espacio-racks.md), [11 · soporte físico](cierre-inventario/11-soporte-fisico.md), [12 · suministro](cierre-inventario/12-matriz-suministro-costos.md), [13 · matriz de red](cierre-inventario/13-matriz-red-y-diagrama.md) | Racks, energía, clima, cableado, responsabilidades, segmentación y datos de la figura. |

Las referencias son antecedentes internos de diseño, no evidencia de implementación. Esta consolidación no añade una certificación de soporte regional ni sustituye la trazabilidad contractual de S1. En esta consolidación, S8–S10 sustituyen las cantidades y reservas preliminares de S3–S6; las decisiones posteriores expresas del usuario prevalecen sobre formulaciones antiguas de esas fichas. Así, un host por negocio y ausencia de bitácora X local quedan superados. Los agentes de entrega efímeros y el estado Terraform segregado forman parte del diseño; sus parámetros de implementación se completan en ingeniería de detalle.

## 3. Sitios y zonas

| Sitio o dominio | Zonas que debe abrir el inventario | Situación |
| --- | --- | --- |
| Servicios globales / SaaS | DNS público, borde, identidad, gobierno, entrega y BI | Productos seleccionados; residencia y configuración específicas por cerrar. |
| CLD-CL-R · Chile Central Retail | Hub, entrada, AKS, datos, operación, administración | Hub y radios R definidos; 17 nodos AKS base, capacidad sujeta a carga/SKU. |
| CLD-CL-F · Chile Central Filial | Hub, entrada, AKS, datos, operación, administración | Hub y radios F definidos; 17 nodos AKS base y recursos aislados de Retail. |
| CLD-CL-X · Frontera | Entrada restringida, AKS X-01, bitácora, administración | Enclave X en Chile, seis nodos AKS y bitácora propios; custodios nominativos y prueba del contrato pendientes. |
| CLD-BR-R / CLD-BR-F · Brazil South | Redes, entrada, cómputo, datos, seguridad y operación de recuperación | Activo-pasivo templado; 17 nodos AKS por negocio y recursos propios; mecanismos por producto sujetos a ensayo. |
| CLD-BR-X · Recuperación X-01 | Servicio de cruce y bitácora necesarios para operar desde DR | Seis nodos AKS y bitácora X dentro del modo templado; sin apertura de rutas generales R-F. |
| DEV / QA / PRE | Recursos propios R, F y X por ambiente | Chile como emplazamiento de diseño, tres ambientes por ámbito; capacidad exacta por suite/cuotas. |
| SIT-xx · Tienda | Caja, sala, atención, Filial, IoT, video, invitados, servidores, gestión y WAN | Patrón por tienda; falta asociarlo a un padrón nominal verificado. |
| CD-01 / CD-02 | Captura logística, WMS cuando corresponda, nodos locales, LAN y WAN | Roles documentados; hosts y cantidades reales por levantar. |
| DC-01 / DC-02 y oficinas | Sistemas conservados, integración, respaldo existente, usuarios y red | Ubicación física exacta y uso de DC-02 por acreditar. |
| EXT-* · Contrapartes | Canales, pagos, firma, mensajería, socios y publicidad | Fuera de la administración de Ancoa; inventariar endpoints y contratos. |

Una zona de seguridad de este documento no equivale a una zona de disponibilidad Azure. AZ1/AZ2/AZ3 son dominios de disponibilidad del diseño anterior; su uso efectivo se confirma para cada producto, región y suscripción.

## 4. Borde global, identidad y servicios SaaS

Fuente: S1, S4 y S5. Estas piezas no agregan VM que Ancoa deba administrar.

| Elemento | Instancias / separación | Función y conexiones |
| --- | --- | --- |
| Azure DNS público | Zonas y registros R/F; cantidad según dominios | Resuelve los nombres de canales hacia Front Door. No transporta la solicitud de negocio. |
| Front Door Premium | Un perfil R y uno F en el diseño | Borde HTTPS, selección de origen de producción/DR y comprobaciones de salud. |
| WAF de borde | Política propia por perfil/ámbito | Filtra solicitudes públicas; reglas, excepciones y logs propios. |
| Orígenes y enlaces privados de Front Door | Origen regional por ámbito y destino de recuperación | Acceso privado a Application Gateway. La ubicación del enlace gestionado debe comprobarse; la decisión sobre Brasil como DR no resuelve por sí sola esta configuración. |
| Entra ID P2 | Directorios y administración por definir, separación de permisos obligatoria | Identidad laboral y acceso de operadores; no se afirma que ambos negocios compartan tenant. |
| Entra External ID | Configuración de clientes/titulares separada | Autenticación de canales externos. |
| Entra PIM | Roles y elevaciones por ámbito | Acceso privilegiado temporal, aprobación y trazabilidad. |
| Entra Private Access | Aplicaciones y grupos de conectores propios | Acceso remoto privado del personal autorizado; no sustituye los túneles entre sitios. |
| Microsoft Intune | Perfiles y grupos de dispositivos por ámbito | Configuración, cumplimiento y administración de terminales. |
| Defender for Endpoint | Agente en equipos compatibles, licencias por cerrar | Protección de terminales y servidores; envía señales al servicio correspondiente. |
| Defender for Cloud | Planes por suscripción/recurso | Postura y protección de cargas; cobertura concreta por definir. |
| Azure Policy | Asignaciones por jerarquía y ambiente | Control de configuración y evaluación de recursos. |
| Azure Pipelines y repositorio | Proyectos, permisos y conexiones de servicio segregados | Orquestación de construcción y despliegue; agentes en sección 10. |
| Power BI | Workspaces y permisos R/F separados | Consulta de modelos analíticos mediante gateways dedicados. Residencia del servicio por verificar. |

## 5. Chile Central: redes, entrada y balanceo

Fuente vigente: S8/B, con S3–S7 como antecedentes. El siguiente patrón se instancia separadamente para R y F. X utiliza su propia frontera restringida; no se le asigna automáticamente toda la pila de publicación pública.

| Elemento | Cantidad de diseño | Ubicación / relación |
| --- | --- | --- |
| Suscripciones, grupos de recursos y RBAC | Separación R/F/X y por ambiente; número final pendiente | Contenedores administrativos, no servidores. |
| VNet hub, aplicación y acceso privado a datos | Tres VNets por ámbito R/F/X y región en la reserva de B | Hub y radios propios; peering solo dentro del ámbito y flujos X mediante listeners contractuales. |
| VPN Gateway con redundancia compatible | Un recurso por ámbito | GatewaySubnet; termina túneles IPsec de sitios. |
| Azure Firewall Premium y políticas | Un recurso por ámbito | AzureFirewallSubnet; inspección y control de salida/tránsito permitido. |
| ExpressRoute | Alternativa adicional para DC-01, sin cantidad aprobada | Circuito, proveedor y gateway independientes por definir; no reemplazar la VPN en el inventario. |
| DNS Private Resolver | Recurso y endpoints por ámbito | Subredes dedicadas de entrada/salida; reenvío desde DNS de sitios. |
| Zonas DNS privadas y vínculos | Según servicios/subrecursos y ámbitos | Resolución de endpoints privados; sin resolución financiera abierta a Retail. |
| Application Gateway v2 | Un recurso R y uno F | Subred dedicada de entrada; listeners web/API, certificados, probes y backend pools propios. WAF regional como diseño; SKU, capacidad y Private Link sujetos a validación regional. |
| API Management Premium clásico interno | Un recurso R y uno F | Subred APIM; políticas, productos y contratos propios. No equivale al ILB. |
| Standard Load Balancer interno | Recurso por clúster según Services expuestos | Frontends/VIP privados y backends de nodos; reglas y probes administrados de forma compatible con AKS. |
| Entrada privada X-01 | Listener/Service y balanceo restringidos | Recibe solamente contratos autorizados; no se incorpora un Front Door público para X. |
| Private Endpoints y sus NIC | Por recurso/subrecurso accesible | Subred PE. Registrar por separado Blob/DFS cuando corresponda. PaaS no se dibuja alojado dentro de esta subred. |
| NSG y reglas | Por subred/NIC según diseño aplicable | Filtrado de red; no son equipos ni saltos de tráfico. |
| Tablas de rutas UDR | Por segmento que lo requiera | Fuerzan recorridos autorizados y retorno simétrico. |
| Peering | Solo relaciones aprobadas dentro de cada ámbito | No habilita una malla R↔F ni vuelve transitivo el acceso por sí solo. |
| IP públicas, NIC, certificados y FQDN | Inventario dependiente del recurso | Registrar propietario y exposición; no asignar IP pública a cada nodo AKS. |
| Salida de AKS | Ruta controlada por firewall del ámbito | UDR, DNS y retorno por ensayar; no añadir NAT Gateway sin justificar su papel. |

Subredes a representar: GatewaySubnet, AzureFirewallSubnet, AzureBastionSubnet, DNS inbound, DNS outbound, entrada, APIM, nodos AKS, PE, gateways BI, SHIR y conectores administrativos. La ficha B reserva `10.64.0.0/12`, con R/F/X de Chile en 10.64/10.65/10.66 y Brasil en 10.68/10.69/10.70; reserva además `100.64.0.0/16` para pods Overlay y `100.65.0.0/19` para Services. Son bloques de diseño, no asignaciones descubiertas. Deben verificarse junto con DNS, LAN/WAN y terceros antes de fijar IP por recurso. Los VLAN del sitio constan en la sección 11 y la ficha 13.

## 6. Chile Central: clústeres, nodos y contenedores

### 6.1 Inventario de cómputo AKS

Fuente vigente: S8/A y S9/F; S3 y S6 son antecedentes. Hay tres clústeres de diseño: Retail, Filial y Frontera. Cada uno tiene un plano de control administrado por Microsoft; ese plano no agrega VM del inventario de Ancoa.

| Clúster / pool | IDs de nodos de referencia | VM base de diseño | Cargas |
| --- | --- | ---: | --- |
| AKS-R / SYS | R-SYS-01, 02, 03 | 3 | Componentes de sistema del clúster. |
| AKS-R / BIZ | R-BIZ-01..05 | 5 | Frontends, servicios Retail y capacidades comunes. |
| AKS-R / INT | R-INT-01, 02, 03 | 3 | Adaptadores, sincronización, proyecciones y trabajos automáticos. |
| AKS-R / STATE | R-STATE-01, 02, 03 | 3 | Búsqueda, catálogo y MLflow, con persistencia propia. |
| AKS-R / OPS | R-OPS-01, 02, 03 | 3 | Observabilidad autogestionada. |
| AKS-R / BATCH | R-BATCH-01..N | Variable, no incluida | Jobs de entrenamiento/conteo. |
| AKS-F / SYS | F-SYS-01, 02, 03 | 3 | Sistema del clúster financiero. |
| AKS-F / BIZ | F-BIZ-01..05 | 5 | Frontend financiero, crédito y capacidades comunes propias. |
| AKS-F / INT | F-INT-01, 02, 03 | 3 | Adaptación financiera, proyecciones y conciliación. |
| AKS-F / STATE | F-STATE-01, 02, 03 | 3 | Búsqueda y catálogo financieros. |
| AKS-F / OPS | F-OPS-01, 02, 03 | 3 | Observabilidad financiera. |
| AKS-X / SYS | X-SYS-01, 02, 03 | 3 | Sistema del enclave. |
| AKS-X / BIZ | X-BIZ-01, 02, 03 | 3 | X-01, con acceso a su bitácora propia. |

**Total base propuesto: 40 VM de nodos**, más batch elástico 0–3. Es capacidad inicial calculada con presupuestos supuestos de requests y pérdida de AZ, no un mínimo medido. Cada pool lógico puede desplegar VMSS alineados por zona; SKU, vCPU, RAM, discos, autoscaling y distribución definitiva se prueban según la [ficha de cómputo](cierre-inventario/01-computo-aks.md). Los IDs son posiciones de diseño.

La cantidad de nodos no fija la cantidad de réplicas. A define para BIZ/INT sin estado tres pods mínimos por Deployment, distribución entre zonas, anti-afinidad y presupuesto para conservar dos réplicas. Los requests iniciales por pod son supuestos de 0,5 vCPU/1 GiB para API normal, 1 vCPU/2 GiB crítica y 0,25 vCPU/0,5 GiB web ligera; cada manifiesto debe ajustarse a su perfil real. StatefulSet/Job, PV, quórum, afinidad y límites definitivos se completan por producto. Tres nodos STATE no demuestran HA del software.

### 6.2 Cargas de aplicación y su persistencia

| Carga / contenedor o módulo | Ejecución | Persistencia / dependencia principal |
| --- | --- | --- |
| Portal y frontend web de tienda | R-BIZ | APIs Retail; la interfaz de navegador se ejecuta en el dispositivo. |
| Portal y frontend de tarjeta | F-BIZ | APIs financieras; identidad de titular. |
| R:M-01 Oferta comercial | R-BIZ | pg-r-merc; caché Redis y representación vectorial derivadas. Partición de despliegue por conciliar. |
| R:M-02 Abastecimiento | R-BIZ | Base/rol propio en pg-r-merc. |
| R:M-03 Existencias | R-BIZ | Base/rol propio en pg-r-merc. |
| R:V-01 Pedidos | R-BIZ | Base/rol propio en pg-r-venta; contrato con lockers. |
| R:V-02 Ventas | R-BIZ | Base/rol propio en pg-r-venta; cruce autorizado por X-01. |
| R:V-03 Comisiones | R-BIZ | pg-r-venta; módulo extraíble, no se cuenta automáticamente como Deployment adicional. |
| R:V-04 Marketplace | R-BIZ | pg-r-venta; módulo extraíble e integración con plataforma externa. |
| R:CL-01 Posventa | R-BIZ | Base/rol propio en pg-r-clientes. |
| R:CL-02 Clientes Retail | R-BIZ | Base/rol propio en pg-r-clientes; fila virtual. |
| F:C-01 Originación | F-BIZ | pg-f-originacion. |
| F:C-02 Cartera | F-BIZ | pg-f-cartera. |
| F:C-03 Evidencia financiera | F-BIZ | pg-f-evidencia y Blob de evidencia vigente. |
| X-01 Control de cruces | X-BIZ | pg-x01; contrato mínimo hacia Filial. |
| Administración y parámetros | BIZ R y F, instancias propias | Datos y propietario por cerrar. |
| Flujos y tareas humanas | BIZ R y F, instancias propias | Estado durable propio; motor pendiente. |
| Documentos y firma | BIZ R y F, instancias propias | Blob y metadatos propios; prestador externo. |
| Notificaciones | BIZ/INT del ámbito, reparto pendiente | Estado de entrega, colas y proveedor propios. |

Java 25 LTS y Spring Boot 4.x pertenecen a las imágenes de ejecución; React/React Native a las aplicaciones y frontends. No generan servidores adicionales. Las versiones exactas y su compatibilidad siguen pendientes. F:C-04 Control regulatorio conserva su condición de candidato: no se incorpora una VM, base ni Deployment aprobado.

### 6.3 Integración, herramientas y observabilidad en contenedores

| Carga | Ubicación | Componentes a registrar |
| --- | --- | --- |
| Adaptador Comercio | R-INT | Conectores ERP/DTE y WMS, credenciales y colas propias. |
| Adaptador Canales | R-INT | E-commerce, marketplace y fidelización conservados. |
| Adaptador Socios | R-INT | Pagos, proveedores, transportistas y contratos de socios. |
| Adaptador Crédito | F-INT | Crédito 2011, firma y reportes autorizados. |
| Sincronizador de operaciones | R-INT y cliente local | Recepción, idempotencia, reintentos y conciliación. |
| Proyectores / exportadores / outbox | INT de cada ámbito | Workers, consumidores, trabajos de corte/calidad y estado durable propio. |
| Coordinación automática | INT de cada ámbito | Producto y partición pendientes; no confundir con tareas humanas. |
| OpenSearch de negocio | STATE R/F separados | Pods, roles, índices, discos y respaldo; número de nodos del producto pendiente. |
| OpenMetadata | STATE R/F separados | Servicio, ingesta, base técnica e índice de catálogo compatible. No dar por compatible cualquier backend por compartir nombre. |
| MLflow | R-STATE | Servicio de seguimiento/registro, base técnica y Blob de artefactos. |
| Python / scikit-learn | R-BATCH | Jobs, imágenes, conjunto versionado y modelos de conteo. |
| OpenTelemetry Collector | OPS y agentes en nodos/locales | Instancias gateway/DaemonSet según diseño, buffers y receptores privados. |
| Prometheus | OPS R/F separados | Scrape, almacenamiento y HA por dimensionar. |
| Grafana Loki | OPS R/F separados | Ingesta, consulta y almacenamiento de logs saneados. |
| Grafana Tempo | OPS R/F separados | Ingesta, consulta y almacenamiento de trazas saneadas. |
| Grafana y Alerting | OPS R/F separados | Consolas, evaluadores, estado y canales de aviso. |
| Blackbox Exporter | R-SYN-01 / F-SYN-01 independientes | Proceso o contenedor en VM fuera del AKS supervisado. |

También deben constar en el detalle del clúster: Services y VIP, endpoints, namespaces, cuentas de servicio, Workload Identity, políticas de red, objetos de configuración y referencias a secretos; complementos de red/DNS/CSI y componentes de entrada efectivamente seleccionados. No se inventa un producto ingress adicional ni se duplica App Gateway sin definir su necesidad. Los discos de nodo, PV/PVC, StorageClass y snapshots se contabilizan como almacenamiento, no como nuevos nodos.

### 6.4 VM auxiliares fuera de AKS

| IDs | Cantidad de diseño | Plataforma / función | Conexiones |
| --- | ---: | --- | --- |
| R-BI-01/02 | 2 | Windows Server 2022, gateway estándar de datos BI | Power BI/Relay saliente y pg-r-mart privado. |
| F-BI-01/02 | 2 | Windows Server 2022, gateway financiero | Power BI/Relay y pg-f-mart. |
| R-IR-01/02 | 2 | Windows, Self-hosted Integration Runtime de ADF | Control de ADF, fuentes y trabajos Retail permitidos. |
| F-IR-01/02 | 2 | Windows, SHIR financiero | Control de ADF y fuentes financieras permitidas. |
| R-PA-01/02 | 2 | Windows Server 2022, Private Network Connector | Entra Private Access saliente y destinos privados autorizados. |
| F-PA-01/02 | 2 | Conectores Windows financieros | Mismo papel, permisos y red propios. |
| R-SYN-01 / F-SYN-01 | 2 | Linux, sonda independiente fuera de AKS | Se emplazan en Chile dentro de la propuesta de cómputo. |

Son **12 VM auxiliares** y **2 sondas** además de las **40 VM AKS**: subtotal de diseño de Chile **54 VM**. No incluye batch, agentes CI/CD, DR, ambientes inferiores ni recursos administrados. Los pares se distribuyen entre dominios de falla cuando el producto lo admita; el mecanismo HA de cada software se configura y prueba por separado.

La reserva por VM auxiliar es 8 vCPU/16 GiB para BI y SHIR, 4 vCPU/16 GiB para Private Access y 2 vCPU/4 GiB para cada sonda. La ficha A fija además los tamaños objetivo por pool y máximos iniciales de autoscaling; su verificación de RAM asignable, cuotas y carga precede a la elección del SKU. Estas reservas no se suman como nodos nuevos.

## 7. Chile Central: datos, mensajería y almacenamiento

Fuente vigente: S9/D; S1 y S3–S5 son antecedentes. Los siguientes PostgreSQL son recursos administrados, no VM a comprar. Primario/espera y réplicas son roles de disponibilidad del servicio; no se duplican en el subtotal IaaS.

| Recurso | Ámbito | Contenido / consumidores |
| --- | --- | --- |
| pg-r-merc | R | Mercadería; bases y roles por autoridad. Incluye el historial de precios publicados, no otro servidor por ese rótulo lógico. |
| pg-r-venta | R | Pedidos, Ventas y módulos comerciales, con autoridades separadas. |
| pg-r-clientes | R | Posventa y Clientes Retail. |
| pg-r-vector | R | PostgreSQL con pgvector; representación derivada de oferta. |
| pg-r-mart | R | Modelos analíticos; consulta BI separada del operacional. |
| pg-r-tech | R | Metadatos técnicos de herramientas, con bases/roles propios. |
| pg-f-originacion | F | Solicitud, evaluación, cupo y autorización. |
| pg-f-cartera | F | Cuenta, saldo, pagos y cartera. |
| pg-f-evidencia | F | Expedientes, metadatos e integridad de evidencia. |
| pg-f-mart | F | Modelos analíticos financieros. |
| pg-f-tech | F | Metadatos técnicos y catálogo propios. |
| pg-x01 | X | Fichas y bitácora mínima de cruces; sin maestro unificado R/F. |

**Total de diseño: 12 recursos PostgreSQL** (6 R, 5 F, 1 X), con reserva inicial de **4.500 GiB (≈4,39 TiB)**: R 2.250 GiB, F 2.150 GiB y X 100 GiB. La ficha D detalla capacidades por recurso, vCore/IOPS, HA y recuperación; son reservas lógicas sujetas a muestras y carga, no almacenamiento físico medido ni VM propias.

| Recurso adicional | Separación y unidades a inventariar | Uso |
| --- | --- | --- |
| Service Bus Premium | Un namespace R y uno F en el diseño; colas/tópicos/suscripciones/DLQ propios | Mensajería de cada negocio; no existe un puente general entre buses. |
| Azure Managed Redis | Un recurso Retail; reserva inicial 16 GiB, HA/SKU por validar | Oferta reconstruible. No autoridad de inventario ni crédito. |
| Azure Data Factory | Factory y runtimes propios R/F | Carga, transformación y coordinación de conjuntos autorizados. Región concreta del servicio por verificar. |
| ADLS Gen2 | Cuentas R/F y contenedores/conjuntos propios; reserva inicial R 3 TiB y F 2 TiB | Landing, curados e historia versionada; PE Blob/DFS y copia propia a Brasil. |
| Blob de evidencia vigente | F, autoridad F:C-03; reserva inicial ampliable 5 TiB | Objetos del expediente financiero, índice/hash en PG y retención por expediente. |
| Blob documental | Por ámbito, cantidad pendiente | Documentos operacionales; conciliar el recurso F con evidencia para evitar duplicarlo. |
| Blob WORM / archivo | Cuentas/contenedores por ámbito y clase; archivo R 25 TiB y F 12 TiB iniciales | Retención según clase: crédito/consentimiento plazo del crédito +6 años, venta/tributario 6, precio 3, inventario/conteo 6; configurar legal hold y vencimiento. |
| Blob de artefactos MLflow | R | Modelos y artefactos versionados; distinto del modelo servido. |
| Almacenamiento de telemetría | R/F/X propios; reserva inicial 1 TiB por ámbito | Objetos/discos según backend; seguridad 12 meses en línea +24 adicionales en archivo; GB/día y resto de clases por medir. |
| Blob temporal Bastion | Por ámbito | Registro temporal con configuración compatible; copia custodiada al archivo cuando corresponda. |
| Discos administrados / PV | Por nodo y carga con estado | Sistema, OpenSearch, catálogo, métricas y buffers según producto. |
| Backup, snapshots y PITR | Por recurso soportado; vaults/políticas por definir | Recuperación operativa. Archivo, réplica y backup tienen funciones diferentes. |

Una fila representa una finalidad de almacenamiento; no fija necesariamente una cuenta adicional. La separación de cuentas se decide por custodia, retención, claves, red y recuperación antes de sumar unidades.

Los tamaños de D son capacidades lógicas iniciales, no sumas de bytes medidos. Réplicas DR, versiones, redundancia y backups consumen capacidad adicional; no aplicar de nuevo factores ya incluidos en cada reserva. La evidencia se conserva durante el plazo de cada crédito más seis años: el horizonte de diez cohortes usado para estimar volumen no fija una retención uniforme de diez años. Las cuentas documentales y de archivo deben conciliarse para no comprar dos veces capacidad para los mismos objetos.

## 8. Seguridad y administración regionales

Fuente vigente: S9/F. R, F y X tienen sus propios recursos, permisos y custodia; falta nominar responsables y acreditar tenants/licencias. El gobierno X se separa de los operadores R/F; no hereda permisos de Retail.

| Elemento | Dónde se representa | Dependencias / detalle pendiente |
| --- | --- | --- |
| Azure Bastion Premium | Tres recursos Chile, uno por R/F/X, con subred dedicada | Acceso autorizado a VM, grabación según protocolo/cliente compatible. |
| Key Vault | Tres recursos Chile, uno por R/F/X, con endpoints propios | Secretos, certificados y claves según política; permisos de identidad y recuperación. |
| Managed HSM | Dos candidatos, F y X, condicionados al caso de uso de clave | Censo criptográfico, SKU regional, dominio de seguridad y restauración; no contar como adquisición confirmada ni confundir con Dedicated HSM. |
| Workload Identity | Asociación por carga AKS | Cuenta de servicio, identidad federada y permisos mínimos sobre recursos. |
| Azure Monitor / Log Analytics | Tres workspaces Chile, uno por R/F/X, con reglas propias | Separación de señales y retenciones por ámbito. |
| Microsoft Sentinel | Tres configuraciones sobre los workspaces R/F/X | Conectores, reglas, incidentes y permisos SOC. No es una VM independiente. |
| Agentes de seguridad / monitorización | VM, nodos y dispositivos compatibles | Inventario de agente, versión, destino y responsabilidad. |
| Controles Kubernetes | Cada clúster/namespace | NetworkPolicy, RBAC, admisión, secretos y permisos; producto/configuración por cerrar. |
| Logs de red y diagnósticos | Firewall, gateways, VNet y servicios aplicables | Destinos autorizados; no mezclar contenidos financieros con analítica Retail. |
| Estación administrativa | Equipo corporativo gestionado, ubicación por registrar | MFA/PIM y acceso privado. Ser dispositivo corporativo no concede privilegios. |

## 9. Brazil South: inventario de recuperación

La [ficha de recuperación](cierre-inventario/07-dr-ambientes.md) establece como capacidad inicial de diseño 40 nodos AKS (R 17, F 17 y X 6), 8 VM IR/PA y 2 sondas: **50 VM activas de espera**. Las 4 VM BI se reconstruyen y permanecen apagadas en espera. RTO objetivo de hasta 4 horas y RPO de hasta 15 minutos para servicios críticos, sujetos a ensayo completo y a compatibilidad/lag de cada producto. La ficha define además DEV, QA y PRE separados por ámbito, y tres ACR de diseño. Las familias de la tabla inferior se leen con esos conteos y con las decisiones detalladas de la ficha.

Fuente vigente: S9/G, en conjunto con S8/B y S9/D/F. **El destino está decidido para R y F.** La tabla enumera lo que debe poder operar o recuperarse allí; no afirma que todo esté ya provisionado o tenga replicación automática.

| Familia | Retail DR | Filial DR | Qué falta concretar |
| --- | --- | --- | --- |
| Redes y DNS | Hub/spoke, subredes, DNS y rutas R-DR | Equivalentes F-DR aislados | CIDR sin solapamiento, conectividad desde sitios y dependencias de resolución. |
| Entrada privada | App Gateway, APIM, ILB y origen de Front Door R | Pila propia F | Unidades activas, probes, certificados y conmutación. Front Door global no se cuenta de nuevo como servidor regional. |
| Conectividad y protección | VPN, Firewall, NSG/UDR R | Equivalentes F | Túneles alternativos, rutas, inspección y retorno. |
| AKS y cómputo auxiliar | Pools R, IR/PA y sonda; BI reproducible apagado | Pools F, IR/PA y sonda; BI reproducible apagado | 50 VM activas de espera entre R/F/X y 4 BI apagadas; SKU/cuotas y arranque por ensayar. |
| X-01 | Servicio de cruce disponible para ambos | Entrada financiera restringida | Enclave y pg-x01 recuperables propuestos en Brasil; gobierno y secuencia por cerrar. |
| PostgreSQL | Contrapartes de los seis recursos R | Contrapartes de los cinco F | Réplica o restauración compatible por recurso, promoción, claves y retorno. |
| Mensajería | Namespace R y estado recuperable | Namespace F propio | Mecanismo compatible que preserve lo necesario; no asumir que replicar configuración replica mensajes. |
| Storage / archivo | Conjuntos, objetos y copias R | Evidencia, conjuntos y archivo F | Copia autorizada Chile→Brasil, inmutabilidad, integridad y recuperación de claves. |
| Herramientas con estado | OpenSearch, catálogo, MLflow y telemetría R | Búsqueda, catálogo y telemetría F | Respaldar estado no reconstruible; ordenar reconstrucción de índices derivados. |
| Caché | Redis Retail recuperable/reconstruible | No se agrega Redis financiero sin necesidad | Tiempo de reconstrucción y dependencia del servicio. |
| Seguridad y operación | Vault/HSM, Bastion, diagnósticos y alertas R | Recursos y permisos F propios | Disponibilidad de claves, identidad y administración durante una caída de Chile. |
| Artefactos | Imágenes, IaC y configuración accesibles | Artefactos propios F | Copias/digests, backend de estado y permisos de despliegue. |

La recuperación debe poder arrancar en orden: identidad y claves, red/DNS, datos y mensajería, cómputo y herramientas, servicios, entrada y validación funcional. Deben fijarse RTO/RPO por servicio y probar también la compra mediante X-01, la conciliación local y el retorno. La existencia de la región de DR no demuestra esos tiempos.

## 10. Desarrollo, pruebas, preproducción y entrega

Fuente vigente: S9/G. Estas piezas son parte del inventario completo aunque no todas aparezcan en la general de producción.

| Elemento | Instanciación de diseño | Pendiente |
| --- | --- | --- |
| DEV-R/F/X, QA-R/F/X, PRE-R/F/X | Chile; tres ambientes por ámbito, aislados de PROD y entre sí; PRE reproduce topología y políticas | Tamaño permanente, cuotas y horarios por suite; PRE escala temporalmente para rendimiento. No se afirma que existan nueve clústeres adicionales. |
| Azure Container Registry Premium | Tres registros, uno por R/F/X; repositorios y RBAC PROD/no PROD separados | PE y copia/replicación a Brasil compatibles con SKU/región, probando pull por digest sin Chile. |
| Azure API Center | Catálogos R/F y contratos X según gobierno | Región, permisos y ciclo de publicación. Fuera del recorrido de solicitudes. |
| Agentes de Azure Pipelines | Agentes efímeros separados por ámbito, identidad federada y acceso autorizado | Implementación VM/pod/servicio y concurrencia por prueba; no VM permanente sumada al subtotal. Si se requiere agente fijo privado, incorporar ID y capacidad explícitos. |
| Terraform | Proceso ejecutado por agente/estación autorizada | Versión y plugins; no es servidor de negocio. |
| Estado Terraform | Cuentas/contenedores remotos separados por ámbito y ambiente, cifrados y versionados | Bloqueo, RBAC, copia recuperable en Brasil y recuperación sin Chile; cuenta/SKU/capacidad concretos en IaC. |
| Artefactos de compilación, SBOM y firmas | Repositorios/almacenamiento de entrega | Custodia, retención, escaneo y promoción por digest. |
| Datos de prueba | Repositorios y datasets segregados | Datos sintéticos/anonimizados; no copiar producción financiera sin control. |
| Red de entrega | Acceso desde agentes a APIs Azure, ACR y destinos privados | Salidas, identidades y ruta administrativa; no exponer API de AKS al público para facilitar el pipeline. |

## 11. On-premise: patrón completo de tienda SIT-xx

**Decisión que gobierna esta sección:** dos hosts Retail y dos Filial por tienda, con redes y administración separadas. Cada par proporciona la base de redundancia exigida por RT-03.14; la conmutación, fencing, diarios y operación de 24 horas sin enlace deben probarse. X-01 local funciona aislado en el par F, con bitácora propia y contrato mínimo hacia Retail.

Fuente vigente: S8/C y S10/10–13. El patrón se replica solo donde corresponda, tras completar el padrón real. «xx» debe reemplazarse por ID de tienda; el documento anterior utiliza 22 tiendas como referencia, cifra que debe conciliarse con el padrón y T-11 antes de compra.

| Zona | Elementos por tienda | Cantidad / alojamiento | Conexiones y función |
| --- | --- | --- | --- |
| Caja | Terminal POS, lector, impresora y TPV de pago | Según cajas y periféricos reales | POS→nodo Retail; TPV→procesador autorizado; no guardar PAN en el diario. |
| Sala | Terminales móviles compartidos, app React Native, SQLite y captura | Según dotación; aplicación en dispositivo | Wi-Fi corporativo→servicios autorizados; Intune y certificado. |
| Atención Retail | PC de mesón / consola comercial | Cantidad pendiente | Portal Retail; sesión nominativa. |
| Clientes | Tótem o cliente de fila virtual | Por necesidad del sitio | Servicio Clientes y estado local de fila por definir. |
| Par Retail | SIT-xx-R-01/02 | 2 hosts decididos por tienda | UI local, oferta vigente, diario durable, sincronización y conmutación con fencing. |
| Filial | PC de mesón financiero y periféricos autorizados | Según puestos reales | Portal financiero por VLAN/túnel F; no pasar por el nodo Retail. |
| Par Filial | SIT-xx-F-01/02 | 2 hosts decididos por tienda | Cupo preautorizado, consumo y vigencia; X-01 local aislado, bitácora propia, claves y custodia F. |
| IoT / lockers | Controlador, casilleros, cerraduras y sensores | Padrón por sitio; nuevos de solución OSS y conservados según SUM-14 | Contrato Pedidos; no acceso directo a base ni cupo. |
| Video | Cámaras IP y NVR | Cantidad/capacidad según cobertura y padrón | VLAN 50; retención 30 días. No inferir analítica de conteo desde cámaras. |
| WLAN corporativa | AP/gestión, AAA y certificados por ámbito | AP por estudio RF; dos instancias AAA locales por ámbito habilitado sobre hosts existentes | EAP-TLS en compatibles, VLAN 12/22, ACL y funcionamiento con WAN caída; reserva CPU/RAM en el par. |
| Invitados | SSID/AP con aislamiento | VLAN 60 y clientes aislados; cantidad AP por estudio RF | Solo Internet mediante borde controlado; sin rutas a negocio, X o administración. |
| LAN | Switches, Cat 6 LSZH nuevo, patch panels, tomas, latiguillos, fibra OS2 y ópticas | Dos switches R +dos F base; acceso/PoE adicional, puntos y metros por plano | VLAN 10/11/12 R, 20/21/22 F, 23 X, 40 IoT, 50 CCTV, 60 invitados, 70 gestión; VRF/ACL/firewall además de VLAN. |
| Perímetro | Firewall/SD-WAN HA propio por negocio | Dos appliances R +dos F; no un único par compartido | Rutas, NAT y túneles propios; sin tránsito R-F libre. No duplicar funciones integradas como equipos nuevos. |
| WAN | Dos accesos/operadores y sus CPE | Dos CPE; handoff a los perímetros R/F | Túneles por ámbito y región; capacidad, recorrido físico y conmutación por comprobar. |
| Energía y alojamiento | Tres racks 24U, UPS A/B, seis PDU 0U, bypass, ATS, generación y clima | 31/72U iniciales; dos UPS 6 kVA/6 kW, 30 min cada rama; grupo inicial 20 kVA o fuente de edificio acreditada | Objetivos sujetos a carga total, batería y plano; clima N+1 inicial dos unidades de 5 kW térmicos; no sumar energía como salto IP. |
| Gestión | Agentes de seguridad, identidad y Collector con buffer | En equipos compatibles | Administración y telemetría a su ámbito; tolerancia a pérdida de enlace. |
| Persistencia local | Discos propios, réplica dentro de cada par, diario, caché y copias definidas | Motor, RAID/capacidad y backup por prueba | Réplica, copia y sincronización cloud tienen funciones distintas. |

La asignación de L-01/L-02/L-03 al par Retail no autoriza a inventar tres hosts adicionales. La ficha de tienda define el empaquetado de UI/servicio local, diario, sincronizador, réplica, fencing y agentes. X-01 local se registra como carga aislada sobre el par F, no como host ni como cuenta/bitácora financiera compartida.

Capacidad inicial por unidad, tomada de C; no sustituye un benchmark ni una BOM de fabricante:

| Unidad | Reserva inicial | Contabilidad y aceptación |
| --- | --- | --- |
| Cada host R | 8 núcleos, 32 GiB RAM, dos SSD empresariales de 960 GB RAID 1, diario ≥100 GB útiles | Dos hosts por tienda; el superviviente debe absorber servicio, agentes y tareas locales autorizadas. |
| Cada host F | 12 núcleos, 48 GiB RAM, dos SSD empresariales de 960 GB RAID 1, diario F ≥100 GB más cuota X | Dos hosts por tienda; capacidad incluye X local y debe resistir caída de un host. |
| Cada instancia X local | 2 vCPU, 4 GiB RAM, bitácora 20 GB; una instancia por host F | Dos instancias activa/espera dentro del par F; cero hosts físicos adicionales y copia/identidad X propias. |
| Testigo de cada par | Un testigo R y uno F, separados de los hosts de aplicación | Dos por tienda; selección y carga de arbitraje por prueba. No es un quinto/sexto servidor de aplicación. |

Se diseña autonomía funcional mínima de 24 horas sin WAN. Además se ensaya el escenario particular de ocho horas y conciliación posterior en 30 minutos. Esa autonomía de aplicación no equivale a 24 horas de batería: las UPS cubren transferencia y operación transitoria, y la generación sostiene la carga esencial. La venta con tarjeta propia sin WAN consume únicamente reserva financiera preemitida, mediante R→X local→API F local; no permite nueva originación, aumento de cupo ni peering entre negocios.

Como cálculo del patrón decidido, dos hosts Retail y dos Filial × 22 tiendas del Caso 09 equivalen a **88 hosts** en tienda. X-01 local y los procesos propios se contabilizan como cargas dentro de esos hosts. La cantidad de VM/contenedores y la capacidad se detallan en la ficha de tienda; 88 hosts no equivalen a 88 VM.

## 12. On-premise: CD, DC y oficinas

**Decisión que gobierna esta sección:** los servicios financieros nuevos y sus bases operacionales se ejecutan en Chile Central y se recuperan en Brazil South. En el DC se inventarían sistemas conservados/externos durante la convivencia y únicamente los datos cuya custodia local se acredite como obligatoria. `HOST-CREDITO-2011` es un marcador de sistema existente para migración, no un destino de producción financiera permanente.

Fuente vigente: S9/E y S10/10–11; S4 y S5 son antecedentes. Los nombres HOST-* son marcadores para levantar servidores reales, no equipos nuevos comprometidos.

| Sitio / zona | Elementos | Estado y relaciones |
| --- | --- | --- |
| CD-01 · Logística | HOST-WMS, terminales de captura, lectores, estaciones y periféricos | WMS conservado; hosts, OS, base y cantidad por inventariar. Adaptador Comercio en R-INT. |
| CD-01 · Continuidad local | CD-LOCAL-01/02 | Par de captura durable y sincronización propuesto; no duplica el WMS. |
| CD-01 · Red y energía | Switching, AP, firewall, enlaces principal/respaldo, UPS/rack | Cantidades y HA por levantar; acceso privado Retail. |
| CD-02 · Concepción | Terminales de captura y CD02-LOCAL-01/02 | Propuesta de registro estructurado/diario local; no inferir otro WMS instalado. |
| CD-02 · Red | Firewall/router, LAN/WLAN y respaldo de enlace | Segundo enlace propuesto; inventario real pendiente. |
| DC-01 · Sistemas conservados Retail | HOST-ERP (ERP/DTE/remuneraciones), HOST-RETAIL-2009 | Convivencia e interfaces autorizadas; ubicación y número real de VM/hosts por acreditar. |
| Dominio financiero corporativo | HOST-CREDITO-2011 | Sistema conservado/migración; custodio F. Emplazamiento exacto no confirmado por el marcador DC. |
| DC-01 · Integración Retail | DC-IR-R-01/02 | Par SHIR local propuesto, distinto de R-IR cloud. Accede a fuentes Retail permitidas. |
| DC-01 · Integración Filial | DC-IR-F-01/02 | Par SHIR local propuesto, red y credenciales F. |
| DC-01 · Infraestructura | Hosts/hipervisores existentes, almacenamiento, backup, DNS, red, energía | Levantar inventario; no se selecciona Proxmox/Ceph desde la imagen de otro caso. |
| DC-01 · Conectividad | Routers/firewalls, túneles por ámbito, enlaces y alternativa ExpressRoute | Contratos y diversidad pendientes. |
| DC-02 | Infraestructura y respaldo existentes por acreditar | No reemplaza la recuperación financiera decidida en Brazil South. |
| Oficinas / casa matriz | PC/portátiles, telefonía/periféricos aplicables, LAN/WLAN y firewall | Acceso nominativo a sistemas del ámbito; cantidad y sitios por levantar. |
| Trabajo remoto autorizado | Equipo corporativo administrado | Private Access y controles de identidad; acceso administrativo solo para perfiles habilitados. |

Cada sede debe tener una ficha: nombre y dirección, responsable, salas/racks, hosts físicos, VM y procesos, IP/VLAN, enlaces, alimentación, soporte, propiedad y relación con T-11. La ausencia de esa ficha impide afirmar un inventario físico nominal completo del parque existente; este documento conserva todas las familias identificadas y hace visible ese faltante.

## 13. Sistemas externos y dispositivos de entrada

| Elemento | Alojamiento | Punto de integración |
| --- | --- | --- |
| Navegador/app de cliente o titular | Dispositivo del usuario | Internet→Front Door del canal; autenticación correspondiente. |
| E-commerce, marketplace y fidelización conservados | Plataforma del proveedor, ubicación pendiente | Adaptador Canales; no alojarlos dentro de AKS por aparecer en el diagrama. |
| Procesadores de pago | Proveedor externo | TPV y/o Adaptador Socios según contrato. |
| Proveedores y transportistas | Sistemas de contraparte | APIs/eventos/archivos acordados; Adaptador Socios. |
| Prestador de firma | Proveedor por cerrar | Capacidad documental del ámbito; evidencia bajo F:C-03 cuando sea financiera. |
| Mensajería correo/SMS/IM/push | Proveedor por cerrar | Notificaciones propias; endpoints, credenciales y callbacks autenticados. |
| Plataforma publicitaria | Proveedor Retail Media por cerrar | Oferta y adaptador Retail; no se inventan servidores publicitarios propios. |
| Reportes regulatorios | Canal externo autorizado por definir | Adaptador financiero; no se deduce una API pública de un organismo. |
| Servicios de plataforma | Identidad, actualización, certificados, hora y repositorios permitidos | Dependencias salientes registradas por producto; no tratarlas como nuevos servicios de negocio. |

Las cinco innovaciones quedan cubiertas por cómputo concreto: conteo predictivo en BATCH/MLflow; búsqueda multimodal en Oferta/pgvector; Retail Media en Oferta/adaptador externo; lockers en controlador local/Pedidos; modo tienda/fila en terminales/Clientes y estado local. No se añade una máquina por cada nombre de innovación.

## 14. Inventario de conexiones

Fuente vigente: S8/B/C, S9/D–G y S10/11–13; S6 es antecedente. La flecha indica quién inicia la conexión; el retorno de respuesta no constituye una integración nueva. Es una matriz de diseño, no reglas de firewall listas para aplicar. Certificados, FQDN, puertos finales e identidades se completan por endpoint.

| ID | Origen → destino | Transporte previsto | Restricción / finalidad |
| --- | --- | --- | --- |
| C01 | Cliente → DNS público | DNS del resolutor utilizado | Resolver canal; camino lateral al tráfico web. |
| C02 | Cliente → Front Door R/F | HTTPS 443 | WAF, host y autenticación del canal. |
| C03 | Front Door → Application Gateway propio | HTTPS por Private Link | Origen privado, certificado y probe válidos. |
| C04 | Application Gateway → APIM propio | HTTPS 443 | Ruta API, listener y contrato del ámbito. |
| C05 | Application Gateway → VIP web AKS | HTTPS 443 | Publicación UI; no bypass a APIs operacionales. |
| C06 | APIM → VIP interna / Service | HTTPS 443 | Backend autorizado, token e identidad. |
| C07 | ILB / Service → pods seleccionados | Puerto del servicio, TLS según configuración | Enrutamiento al backend compatible con CNI; no usar IP de pod como backend universal. |
| C08 | Firewall sitio → VPN Gateway propio | IPsec/IKE; UDP 500/4500 según caso | Túnel y prefijos R/F separados; probar respaldo y NAT-T. |
| C09 | VPN Gateway → Firewall/ruta → entrada propia | Tráfico privado autorizado | NSG/UDR y retorno simétrico; sin acceso libre a bases. |
| C10 | DNS sitio → Resolver privado propio | UDP/TCP 53 | Reenvío condicional y ámbitos aislados. |
| C11 | Ventas → entrada X-01 | HTTPS privado | Compra autorizable, finalidad y datos mínimos. |
| C12 | X-01 → entrada financiera autorizada | HTTPS privado | Identidad X-01 y respuesta limitada; sin credencial de base F. |
| C13 | X-01 → pg-x01 | PostgreSQL TLS 5432 | Bitácora propia; no replica maestros de los negocios. |
| C14 | Carga propietaria → PostgreSQL propio | PostgreSQL TLS 5432 | Endpoint privado y rol/base propios. |
| C15 | Productor/consumidor → Service Bus propio | AMQPS TLS 5671; alternativa a validar | Permisos por cola/tópico; cliente inicia, no puente R/F. |
| C16 | Workers → Blob/ADLS propio | HTTPS 443 | PE Blob/DFS correspondientes; identidad y ruta de objetos. |
| C17 | Oferta → Redis / pgvector | TLS específico del producto / PG 5432 | Datos derivados; puerto Redis pendiente del servicio elegido. |
| C18 | Aplicaciones/herramientas → OpenSearch / catálogo | API privada del producto | Endpoint y credencial propios; separar búsqueda de negocio y catálogo. |
| C19 | Jobs de conteo → ADLS / MLflow | HTTPS/API privada | Dataset/modelo versionados; resultado hacia servicio propietario. |
| C20 | Adaptadores → sistemas conservados | Contrato específico pendiente | Solo fuentes y operaciones autorizadas; evitar lectura directa no documentada. |
| C21 | Adaptadores → terceros | HTTPS/API o transferencia pactada | Firewall de salida, secretos propios y callbacks autenticados cuando existan. |
| C22 | POS → nodo local R | API local cifrada por definir | Venta/consulta y diario durable. |
| C23 | Host activo → host espera del mismo ámbito | Protocolo cifrado por definir | Réplica de diario y fencing; copia separada para recuperación ante borrado/corrupción. |
| C24 | Sincronizador local → entrada cloud propia | HTTPS por acceso autorizado | Reintentos, idempotencia y conciliación. |
| C25 | Puesto F → par local F / entrada F | API privada del ámbito | Caducidad y exclusión de doble consumo; no usa diario R. Durante desconexión, el resultado mínimo para venta pasa por X-01 local aislado, con identidad y bitácora X propias. |
| C26 | Controlador locker → servicio Pedidos | API autenticada según contrato | Eventos/retiro autorizados, sin acceso directo a DB. |
| C27 | SHIR cloud/local → control ADF y fuentes | Canales salientes soportados / protocolo de fuente | Registro propio y extracción autorizada; no administración libre de AKS. |
| C28 | Gateway BI → Power BI/Relay | Canales salientes soportados | Sin consulta entrante pública hacia la VM. |
| C29 | Gateway BI → PostgreSQL analítico propio | TLS 5432 | Modelo de lectura; sin credenciales operacionales. |
| C30 | Usuario/carga → Entra | HTTPS 443 | Autenticación/federación; no proxy de cada consulta de datos. |
| C31 | Carga autorizada → Key Vault/HSM | HTTPS 443 | Identidad y operación criptográfica permitida. |
| C32 | Administrador → acceso privado/Bastion → VM | HTTPS; SSH 22/RDP 3389 al destino | MFA/PIM y permisos; nunca SSH/RDP público. Integración exacta por ensayar. |
| C33 | Conector PA → servicio Private Access | TLS 443; dependencias CRL según producto | Conexión saliente; sin interceptación TLS incompatible. |
| C34 | Aplicación/agente → Collector propio | OTLP TLS, puerto configurado | Datos saneados y buffer local. |
| C35 | Collector / recolectores → backends de señales | API/protocolo según versión | Separación métricas/logs/trazas; evitar duplicación de ingestión. |
| C36 | Grafana → backends / Azure Monitor | API autenticada | Solo ámbito propio. |
| C37 | Recursos Azure/agentes → Log Analytics/Sentinel | Diagnóstico y conectores soportados | Retención, residencia y permisos propios. |
| C38 | Blackbox independiente → endpoints observados | Protocolo de cada sonda | No alojar la única sonda dentro del clúster que supervisa. |
| C39 | Pipeline/agente → ACR / API Center / Azure / AKS | APIs HTTPS y acceso privado necesario | Identidad de entrega limitada por ambiente. |
| C40 | Nodos AKS → ACR | HTTPS privado | Pull de imágenes aprobadas por digest. |
| C41 | Terraform/agente → backend remoto de estado propio | Protocolo de cuenta/backend seleccionado en IaC | Bloqueo, cifrado/versiones, permisos federados y copia/recuperación sin Chile; no acceso común R/F. |
| C42 | Recursos Chile → recuperación Brasil | Mecanismo soportado por cada producto | Copias/replicación propias R/F/X, integridad y claves; no enlace universal entre bases. |
| C43 | Front Door / sitios → entradas DR | HTTPS / túneles privados correspondientes | Conmutación y pruebas funcionales; mismas fronteras de negocio. |
| C44 | Backup/archivo → restauración autorizada | Mecanismo del recurso | Restaurar también configuración y claves; probar retorno y consistencia. |
| C45 | Equipos/servicios → dependencias operativas | DNS, hora, actualización, PKI y endpoints permitidos | Enumeración por producto pendiente; no abrir Internet completo por omisión. |
| C46 | Servicio local R → listener X local | API local cifrada y autenticada | Contrato mínimo de compra offline; identidad R autorizada, sin credencial ni lectura de base F. |
| C47 | X local → API local F autorizada | API cifrada y autenticada del microsegmento X | Consume reserva previa, registra resultado y referencia; X no comparte el libro F ni expone cartera a R. |
| C48 | X local → X cloud | HTTPS privado al recuperar enlace | Replay idempotente de bitácora X; separado de los diarios R y F. |
| C49 | Cámaras IP → NVR local | Protocolo del equipo, por VLAN 50 | Grabación y retención de 30 días; sin salida a datos de negocio. Acceso de mantenimiento por C52. |
| C50 | Invitados → borde controlado → Internet | Acceso del SSID y salida autorizada | VLAN 60, clientes aislados y denegación de redes internas; la flecha resumida no omite firewall en la implementación. |
| C51 | AP/dispositivo gestionado → AAA del ámbito | EAP-TLS y protocolo AAA según solución | Dos instancias locales por ámbito habilitado, identidad/certificados propios; continuidad y revocación ensayadas sin WAN. |
| C52 | Administración autorizada → switches, AP, SD-WAN y equipos de soporte gestionables | Canal de gestión soportado por cada equipo | VLAN 70, identidad nominal, privilegio limitado y auditoría; no acceso administrativo desde invitados, CCTV o IoT. |

La alimentación se inventaría por separado. Estas relaciones son físicas, no protocolos IP ni pasos de la solicitud de negocio:

| ID | Origen → destino | Separación y aceptación |
| --- | --- | --- |
| P01 | Generador/fuente acreditada del edificio → ATS | Capacidad de carga esencial, arranque, autonomía y permisos del emplazamiento. |
| P02 | ATS/tableros → UPS A/B con bypass | Ramas y protecciones calculadas; transferencia y mantenimiento ensayados. |
| P03 | UPS A/B → PDU A/B de cada rack | Seis PDU por tienda, dos por rack; mapa de circuitos y medición por rama. |
| P04 | PDU A/B → PSU de hosts y equipos de red | Cada PSU a su rama, según compatibilidad; ensayo de pérdida de rama sin pérdida de servicio. La general resume este destino en el rótulo de PDU. |

No se admiten conexiones directas de Retail a DB, colas, secretos o índices financieros; tampoco del cliente a AKS/PostgreSQL ni de invitados/IoT a administración. Los cruces de negocio se formalizan por X-01. Las dependencias internas de un servicio administrado no deben confundirse con un broker adicional de negocio.

## 15. Resumen de cantidades y datos que faltan

| Clase | Cantidad de diseño identificada | Límite de la cifra |
| --- | ---: | --- |
| Clústeres AKS de producción | 3 | R/F/X; 17/17/6 nodos base; SKU/cuotas y responsables nominativos por validar. |
| Pools base AKS de producción | 12 | 5 R + 5 F + 2 X; batch adicional variable. |
| VM de nodos AKS base | 40 | Cinco en BIZ R, cinco en BIZ F y tres en cada otro pool; supuestos de carga por probar. |
| VM cloud auxiliares BI/IR/PA | 12 | Cuatro de cada función, separados R/F. |
| Subtotal VM cloud de producción | 54 | Incluye 40 AKS, 12 auxiliares y 2 sondas; excluye batch, agentes, DR y ambientes inferiores. |
| VM de sondas independientes | 2 | Ya incluidas en el subtotal 54; fuera de AKS. |
| Recursos PostgreSQL producción | 12 | 6 R + 5 F + 1 X; no sumar como VM. |
| Namespaces Service Bus producción | 2 | Cantidad de entidades internas pendiente. |
| Perfiles Front Door / APIM / App Gateway | 2 de cada familia | Recursos R/F; unidades internas, escalado y DR no incluidos. |
| Hosts locales Retail | 2 por tienda; 44 para 22 tiendas | Par HA propio, VM/procesos y capacidad por probar. |
| Hosts locales Filial | 2 por tienda; 44 para 22 tiendas | Par HA propio; X-01 local como carga aislada, sin quinto host. |
| Pares locales CD | Un par por CD descrito | No cuenta los hosts WMS conservados. |
| SHIR corporativo local | Dos pares propuestos, R y F | Distinguir VM/host y sitio real; no sumar al cloud. |
| Pods, discos, PE, cuentas Storage, red local y terceros | Sin total cerrado | Desglosar por recurso, sitio y contrato. |
| VM de recuperación Brazil South | 50 activas de espera +4 BI apagadas | 40 AKS +8 IR/PA +2 sondas; batch 0–3 aparte. Modo activo-pasivo templado, sujeto a ensayo. |
| PostgreSQL DR / buses DR | 12 / 2 | Contrapartes propias R/F/X; mecanismo, lag y promoción por validar. No son VM. |
| Key Vault / Bastion / LAW-Sentinel Chile | 3 de cada familia | Uno por R/F/X; HSM F/X son dos candidatos condicionados, no compra cerrada. |
| ACR Premium | 3 | Uno por ámbito; DR y permisos por ensayo, no VM adicionales. |
| Racks tienda / DC-01 / cada CD | 3×24U / 4×42U / 2×24U | Reservas 31/72U tienda y 80/168U DC; geometría, cargas y parque real por levantar. |
| UPS / PDU / CPE / SD-WAN / switches por tienda | 2 / 6 / 2 / 4 / 4 | Equipos y funciones integradas se cuentan una vez; acceso/PoE adicional por estudio. |
| DEV/QA/PRE | Tres ambientes por ámbito | Chile como diseño; instanciación y capacidad permanente por suite y cuotas. |

No se presenta un gran total que mezcle VM, pods, PaaS y dispositivos. Para cerrar el inventario y luego dibujar, cada recurso debe completar: ID estable, sitio/región, ámbito, ambiente, zona/subred, tipo, propietario, cantidad, SKU/OS/versión, vCPU/RAM/disco, réplicas, identidad, DNS/IP, conexiones, backup/DR y fuente/estado de decisión.

Las brechas se agrupan en levantamiento del mandante, ingeniería de detalle y pruebas de aceptación (sección 18). El modo DR templado, las cantidades iniciales 54/50+4, los cuatro hosts por tienda y las regiones están definidos como diseño; no se vuelven a presentar como decisiones abiertas. La validación de SKU, mediciones, rutas, capacidad, HA y RTO/RPO puede exigir ajustar reservas antes de compra, sin declarar esos resultados como ya acreditados.

## 16. Correspondencia con el diagrama vigente

La general 4.52 muestra sitios, zonas, entradas y enlaces, con agrupaciones que remiten a este inventario. Los detalles posteriores abrirán: red/borde, AKS Retail, AKS Filial, Frontera, datos por ámbito, seguridad/operación, tienda, CD/DC, recuperación y entrega/ambientes. Se mantendrán iconos con nombres y marcos solo para zonas; las tablas conservarán IDs y números de conexiones sin obligar a imprimirlos sobre la imagen. El dibujo vigente representa cuatro hosts por tienda y X-01 local como carga aislada dentro del par F. Las pruebas y observaciones restantes conservarán responsable en la ficha H.

Esta versión consolida las familias identificadas y separa recursos de cargas. Su revisión fue documental: coherencia de ámbitos, cantidades de referencia, conexiones y enlaces a fuentes. No representa una revisión humana formal ni una validación de capacidad o despliegue. La decisión arquitectónica de H-01/H-02 está registrada; resta verificar su implementación y pruebas.

## 17. Infraestructura de sitio y encaje — ampliación vigente

Las fichas [espacio y racks](cierre-inventario/10-espacio-racks.md) y [soporte físico](cierre-inventario/11-soporte-fisico.md) completan el inventario con red, energía, ambiente, seguridad física, cantidades, carácter obligatorio/deseable y fuentes. Prevalecen sobre las reservas genéricas anteriores de estos elementos.

Tienda: tres racks 24U (servidores R, servidores F y comunicaciones), 8+8+15U iniciales presupuestadas; cuatro hosts R/F, dos CPE, dos SD-WAN R y dos F, dos switches R y dos F, testigos separados y copias. PDU A/B por rack, dos UPS de 6kW cada una con objetivo de 30min a plena carga, ATS y generación inicial de 20kVA o suministro del edificio acreditado; clima redundante, sensores, cerraduras, cámara y detección dimensionados al sitio. Las cantidades de PoE/puertos/acceso se fijan por levantamiento. No duplicar router, firewall y SD-WAN cuando una misma unidad integra funciones.

La carga nueva estimada es 2,57kW, 3,341kW con 30% de margen, antes de PoE, POS y clima. Autonomía se acredita con curva de baterías y ensayo; generación incluye clima y arranque, sin deducir combustible solo desde kVA. La instalación tienda pide una reserva técnica objetivo de 12m² útiles para fila/maniobra y parte eléctrica, a ampliar si baterías/puertas lo requieren. No es superficie acreditada del local. La envolvente de mantenimiento de tres racks de referencia es 9,81m².

DC-01: superficie del Caso 140m²; propuesta de cuatro racks 42U, reserva 80/168U y distribución de áreas separadas, sujeta a CMDB y plano. Generador, combustible y unidades exteriores requieren espacio exterior autorizado adicional. DC-02 no tiene superficie informada. CD: dos racks 24U por centro y reserva de sala según ficha 10; los 42.000/9.000m² logísticos no equivalen a espacio técnico. Si plano o legado superan la envolvente, se amplía/habilita espacio y no se recortan pasillos, redundancia o separación.

Se ofrecen deseables: alimentación 2N con transferencia, contención fría cuando proceda, enrolamiento externo, medición PDU, monitoreo remoto y mejoras verificables. La ficha 11 diferencia estos compromisos de requisitos obligatorios y decisiones propias; los controles del DC principal no se trasladan sin proporcionalidad a cada gabinete de tienda.

El cableado horizontal nuevo es Cat 6 LSZH por decisión OSS, con tomas, jacks, patch panels, dos latiguillos por punto salvo excepción de diseño, organizadores, canalización, etiquetas y certificación por enlace. Se mide cada recorrido: no se estima metraje por m² comercial. El criterio es canal de hasta 100 m, con reserva de 90 m de enlace permanente y 10 m de latiguillos; los recorridos que lo exceden requieren IDF/troncal de fibra OS2 según el plano, sin alargar el cobre. AP, puntos, PoE, ópticos y puertos adicionales se calculan por RF/carga y por segmento, descontando los cuatro switches base para no duplicarlos.

La matriz SUM-01..SUM-32 asigna especificación, adquisición, instalación y mantenimiento, además de inversión, operación y evidencia. OSS responde por la ingeniería, integración y suministro nuevo allí asignado. Se conservan las excepciones: obra civil de separación a cargo del cliente según RT-06.06, y dispositivos de terreno/POS cuya adquisición corresponda al cliente según Art. 14.2 y padrón contractual. Los CPE de operador se identifican como servicio/equipo contratado; no se cuenta otra vez como compra OSS una función integrada en SD-WAN. Equipos conservados, nuevos y aportes del cliente deben quedar separados en la BOM y oferta económica. Las 32 partidas no contienen precios confirmados; exigen cotización y cantidades por sitio.

La general distingue generador, ATS, UPS y PDU mediante cuatro nodos y tres enlaces de alimentación; routers/SD-WAN y switches R/F son nodos de red. Seguridad cloud permanece agrupada y la bitácora forma parte de X-01. La figura tiene 46 nodos y 51 conexiones: 48 enlaces de datos/control y tres de energía. No sustituye las 52 familias de datos/control y cuatro relaciones eléctricas del inventario. La ampliación sobre 30 nodos F1, la paleta y los iconos Cisco fueron autorizados; la comprobación geométrica no equivale a conformidad estricta con ese catálogo ni a instalación ejecutada.

## 18. Decisiones consolidadas y brechas con responsable

El maestro está sincronizado documentalmente con las fichas vigentes y la topología CSV de la figura 4.52. Esto cierra la consolidación del diseño; no convierte las reservas en mediciones ni declara el parque instalado completo. Las cantidades de compra se emiten después del levantamiento y los ensayos correspondientes.

| Asunto | Decisión vigente | Dato o prueba restante | Responsable de producir evidencia |
| --- | --- | --- | --- |
| Regiones y DR | Chile Central productivo, Brazil South de recuperación; activo-pasivo templado; R/F/X separados | SKU/AZ/cuotas, lag, promoción, retorno y RTO ≤4 h/RPO ≤15 min críticos | Plataforma/operación con responsables R/F/X |
| Cómputo y datos | 54 VM Chile; 50 activas de espera +4 BI apagadas Brasil; 12 PG Chile y contrapartes DR; 4.500 GiB iniciales Chile | Carga real, memoria asignable, IOPS, conexiones, PV/quórum y crecimiento; ajustar reservas antes de compra | Plataforma y datos |
| Tienda y X local | Dos hosts R +dos F, X aislado dentro del par F, bitácora X propia y reserva previa | Cuatro pruebas de caída de host, fencing, 24 h sin WAN, replay y cierre de reservas; política de límites/consentimiento F | Equipo local/plataforma con operación y control financiero |
| Red | Hub/radios por ámbito, VPN/firewall propios, VLAN/VRF y reservas IP de B/13 | IPAM Ancoa/terceros, diversidad WAN, rutas de retorno, puertos y listeners X; validar Private Link Service o proxy contractual | Redes con mandante y operadores |
| Seguridad y custodia | KV/Bastion/LAW-Sentinel por ámbito, identidades separadas; HSM F/X condicionado a clave | Tenants, responsables nominativos, licencias, censo de claves, recuperación, PoC de Private Access/Bastion | Seguridad/SOC con custodios R/F/X |
| Sitios, espacio y energía | Tres racks tienda, cuatro DC-01, dos por CD; capacidades iniciales de la sección 17 | Planos, parque real, peso/profundidad, U, accesos, baterías, PoE/POS, carga eléctrica/térmica, generación del edificio y permisos | Infraestructura y especialistas con acceso habilitado por cliente |
| Cableado y Wi-Fi | Cat 6 LSZH nuevo, fibra donde corresponda, EAP-TLS/AAA local y red invitados aislada | Padrón de puntos, metros, IDF, RF/capacidad, PoE, compatibilidad y certificación | Redes/cableado y equipo de flota |
| Legado, DC/CD y terceros | Finanzas nuevas cloud; ERP/WMS conservados; crédito 2011 en migración, sin nuevo depósito financiero DC acreditado | CMDB, alojamiento real, 14 interfaces, contratos y dataset/mandato expreso si exige custodia DC; producto para captura de CD-02 | Integración con mandante, proveedores y cumplimiento F |
| Ambientes y entrega | DEV/QA/PRE por ámbito en Chile, tres ACR, agentes efímeros y estado Terraform segregado | Cantidades exactas, SKU/backend IaC, suite, horarios, datos sintéticos y recuperación sin Chile | Plataforma/DevOps y QA |
| Suministro y costos | SUM-01..32 con responsabilidades OSS/cliente/operador y excepciones expresas | Cotizaciones, cantidades por sede, licencias, garantías, recurrencias y aceptación | Compras/gestión de oferta con responsables técnicos y cliente |

### Trazabilidad de las agrupaciones gráficas

Los siguientes 46 IDs pertenecen al CSV y al editable, no a una cuenta de servidores. La disposición o el número de iconos no altera las cantidades de recursos de las secciones anteriores.

| IDs de nodos en figura 4.52 | Correspondencia en este inventario |
| --- | --- |
| `cliente`, `fd`, `entra` | Canales, borde e identidad; secciones 4 y 13. Front Door/Entra agrupan configuraciones separadas por ámbito. |
| `vpn_r`, `fw_r`, `ag_r`, `apim_r`, `ilb_r` | Entrada y red R de la sección 5; no un único recurso compartido R/F. |
| `vpn_f`, `fw_f`, `ag_f`, `apim_f`, `ilb_f` | Entrada y red F de la sección 5. |
| `biz_r`, `biz_f`, `x01` | Tres clústeres y cargas de la sección 6; X incluye su bitácora de la sección 7. |
| `data_r`, `data_f` | PostgreSQL, mensajería, objetos y herramientas de datos de la sección 7, agrupados por ámbito. |
| `dr` | Todos los recursos R/F/X de recuperación de la sección 9; no una sola VM de Brasil. |
| `soc`, `admin_pc` | Seguridad, observabilidad y puesto administrativo de la sección 8; instancias y permisos propios. |
| `personal`, `ap_r`, `sw_r`, `sd_r`, `local_r1`, `local_r2` | Dispositivos/red Retail y dos hosts físicos del patrón de tienda, sección 11. |
| `personal_f`, `ap_f`, `sw_f`, `sd_f`, `local_f1`, `local_f2`, `x_local` | Dispositivos/red Filial, dos hosts F y dos instancias X local aisladas; sección 11. |
| `iot`, `sw_aux`, `sd_aux`, `cctv`, `nvr`, `guest`, `internet` | Segmentos auxiliares, borde y salidas autorizadas, sección 11 y C26/C49–52; sin acceso libre a negocio. |
| `conservados` | Sistemas/hosts reales por levantar de DC/CD, sección 12; no un servidor nuevo por cada sistema. |
| `generator`, `ats`, `power`, `pdu` | Infraestructura eléctrica de la sección 17 y P01–04; no nodos IP. |

**Registro de la consolidación v4:** se retiraron las descripciones vigentes de 30/38 elementos gráficos y las reservas de cantidades anteriores; se incorporaron al cuerpo las decisiones A–G y las fichas 10–13. Se explicitaron siete familias de datos/control adicionales y cuatro relaciones de energía. Se conserva la separación entre decisión, reserva de capacidad, dato por levantar y aceptación por prueba. No se modifica el subdocumento LaTeX ni se asigna estado de revisión humana.
