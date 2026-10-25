# Inventario físico de diseño

Estado propuesto. Los IDs no acreditan inventario ni recursos desplegados. Cantidades de réplicas y SKU requieren dimensionamiento.

| ID | Nodo | Clase | Vistas |
| --- | --- | --- | --- |
| clientes | Cliente / titular · Navegador y app | componente | 4.37 |
| personal | Personal / ejecutivo · POS, móvil y mesón | componente | 4.37 |
| operador | Operación / auditoría · Equipo administrado | componente | 4.37 |
| tiendas | SIT-01 · Tiendas · Terminales, lockers y nodos · Detalle 4.38 | componente | 4.37 |
| cdprincipal | CD-01 / CD-02 · WMS / captura durable · Detalle 4.45 | componente | 4.37 |
| dc | DC-01 / DC-02 · ERP, convivencia y archivo · Detalle 4.45 | componente | 4.37 |
| wan | Internet / WAN · VPN IPsec por ámbito · Respaldo por sitio | componente | 4.37 |
| fd | Azure Front Door Premium · Perfiles Retail y Filial · WAF · hosts propios | componente | 4.37 |
| afdpl | Private Link de Front Door · Brazil South → Chile · Tránsito por aprobar | componente | 4.37 |
| vpn | VPN Gateway AZ / ER · Terminaciones por ámbito · ER DC-01 propuesto | componente | 4.37 |
| fw | Azure Firewall Premium · Políticas y rutas propias · Retail / Filial separadas | componente | 4.37 |
| ag | Application Gateway v2 · Una instancia por ámbito · Origen privado / TLS | componente | 4.37 |
| apim | API Management Premium · Instancias propias R / F · Contratos y autorización | componente | 4.37 |
| lb | Standard Load Balancer · ILB privado por clúster · VIP / Service por backend | componente | 4.37 |
| aksr | AKS privado Retail · 9 servicios + capacidades · VMSS / pods · vista 4.40 | componente | 4.37 |
| aksf | AKS privado Filial · 3 servicios + capacidades · VMSS / pods · vista 4.41 | componente | 4.37 |
| aksx | AKS / enclave X-01 · Control y bitácora propios · Vista 4.41 | componente | 4.37 |
| pe | Private Endpoints + DNS · Por servicio y ámbito · Sin acceso público de datos | componente | 4.37 |
| datos | PostgreSQL / Storage · SB, Redis y analítica · PaaS fuera de subredes | componente | 4.37 |
| plataforma | Plataforma de datos · OpenSearch / OpenMetadata · MLflow Retail · 4.42/43 | componente | 4.37 |
| ops | Seguridad y observabilidad · Instancias propias por ámbito · Detalle 4.44 | componente | 4.37 |
| erp | ERP/DTE y WMS · Conservados · Host por inventariar | componente | 4.37 |
| partners | Canales, pagos y socios · Firma, lockers y publicidad · Interfaces por verificar | componente | 4.37 |
| bi | Power BI SaaS · Modelos propios R / F · Conexión de datos privada | componente | 4.37 |
| brazil | CLD-02 · Brazil South · Retail activo/pasivo · Filial solo con aprobación | componente | 4.37 |
| drf | Segundo sitio Filial · Independiente de DC-01 · Destino por aprobar | componente | 4.37 |
| frontend | Web React por ámbito · Contenedores privados en AKS · Portal tienda / tarjeta | workload | 4.37 |
| actor_tienda | Personal / ejecutivo · Sesión nominativa | componente | 4.38 |
| actor_cliente | Cliente / titular · Compra / retiro / fila | componente | 4.38 |
| pos | Terminal POS · React servido localmente · TPV externo separado | componente | 4.38 |
| scanner | Lector de código · USB / Bluetooth validado | componente | 4.38 |
| printer | Impresora de venta · Fiscalidad vía ERP/DTE | componente | 4.38 |
| tpv | Terminal de pago · Procesador autorizado · Sin PAN en diario | componente | 4.38 |
| movil_sala | Terminal compartido · React Native / SQLite · Intune + certificado | componente | 4.38 |
| ap_staff | Wi-Fi corporativo · Certificados y ACL | componente | 4.38 |
| meson | PC mesón Retail · Atención / posventa | componente | 4.38 |
| fila_local | Tótem de fila virtual · Clientes Retail · Estado local durable | componente | 4.38 |
| locker_control | Controlador de lockers · API Pedidos / retiro · No custodia de crédito | componente | 4.38 |
| locker_hw | Casilleros / cerraduras · Sensores de puerta · Modelo por inventariar | componente | 4.38 |
| camera | Cámaras IP · VLAN video aislada | componente | 4.38 |
| nvr | NVR de video · Política propia | componente | 4.38 |
| ap_guest | Wi-Fi de clientes · Solo Internet / aislamiento | componente | 4.38 |
| meson_f | Puesto financiero · Portal / sesión Filial · Sin paso por nodo Retail | componente | 4.38 |
| local_fa | SIT-xx-F-01 · Host/VM Filial activo · Cupo, consumo y vigencia | componente | 4.38 |
| local_fb | SIT-xx-F-02 · Host/VM Filial en espera · Custodia y claves Filial | componente | 4.38 |
| local_ra | SIT-xx-R-01 · Servidor local activo · L-01 / L-02 / L-03 | componente | 4.38 |
| local_rb | SIT-xx-R-02 · Servidor local en espera · Diario y caché replicados | componente | 4.38 |
| sw_a | Switch 1 · Troncales VLAN / ACL | componente | 4.38 |
| sw_b | Switch 2 · Redundancia LAN | componente | 4.38 |
| fw_a | Firewall / SD-WAN 1 · Contextos R / F aislados | componente | 4.38 |
| fw_b | Firewall / SD-WAN 2 · HA con fencing probado | componente | 4.38 |
| ups | UPS / energía · Autonomía por medir | componente | 4.38 |
| isp | Enlace principal · Internet corporativo | componente | 4.38 |
| lte | Segundo proveedor / LTE · Existente o por adquirir | componente | 4.38 |
| azure_r | Azure · entrada Retail · VPN Gateway / Firewall · App Gateway → APIM | componente | 4.38 |
| azure_f | Azure · entrada Filial · VPN y permisos propios · App Gateway → APIM | componente | 4.38 |
| web_client | Cliente / titular · HTTPS de APIs | componente | 4.39 |
| s2s | Sitios / DC-01 · Túneles por ámbito | componente | 4.39 |
| fd_net | Front Door Premium · 2 perfiles, WAF propio | componente | 4.39 |
| pl_brazil | Private Link Front Door · Ubicación Brazil South · Aprobación de tránsito | componente | 4.39 |
| vpn_r | Retail · VPN Gateway AZ · GatewaySubnet /26 | componente | 4.39 |
| fw_r | Retail · Azure Firewall Premium · AzureFirewallSubnet /26 | componente | 4.39 |
| dns_r | Retail · DNS Private Resolver · Inbound / outbound separados · Zonas propias del ámbito | componente | 4.39 |
| bastion_r | Retail · Azure Bastion Premium · AzureBastionSubnet /26 | componente | 4.39 |
| ag_r | Retail · Application Gateway v2 · snet-ingress /24 · Listener HTTPS privado | componente | 4.39 |
| apim_r | Retail · APIM Premium interno · snet-apim /24 · VIP / hostname propio | componente | 4.39 |
| lb_r | Retail · Standard ILB · VIP por Service / backend · TLS hasta el pod | componente | 4.39 |
| aks_r | Retail · AKS privado / VMSS · snet-aks /22 propuesto · CNI Overlay / policies | componente | 4.39 |
| pe_r | Retail · Private Endpoints · snet-pe /24 · IP y DNS por recurso | componente | 4.39 |
| vpn_f | Filial · VPN Gateway AZ · GatewaySubnet /26 | componente | 4.39 |
| fw_f | Filial · Azure Firewall Premium · AzureFirewallSubnet /26 | componente | 4.39 |
| dns_f | Filial · DNS Private Resolver · Inbound / outbound separados · Zonas propias del ámbito | componente | 4.39 |
| bastion_f | Filial · Azure Bastion Premium · AzureBastionSubnet /26 | componente | 4.39 |
| ag_f | Filial · Application Gateway v2 · snet-ingress /24 · Listener HTTPS privado | componente | 4.39 |
| apim_f | Filial · APIM Premium interno · snet-apim /24 · VIP / hostname propio | componente | 4.39 |
| lb_f | Filial · Standard ILB · VIP por Service / backend · TLS hasta el pod | componente | 4.39 |
| aks_f | Filial · AKS privado / VMSS · snet-aks /22 propuesto · CNI Overlay / policies | componente | 4.39 |
| pe_f | Filial · Private Endpoints · snet-pe /24 · IP y DNS por recurso | componente | 4.39 |
| x01net | X-01 · AKS privado + ILB · Sin peering libre R-F | componente | 4.39 |
| x01pe | PE de entrada Filial · Solo contrato X-01 · Destino App Gateway Filial | componente | 4.39 |
| pgcloud | PostgreSQL / Redis · Servicios administrados | componente | 4.39 |
| sbcloud | Service Bus / Storage · Key Vault / HSM | componente | 4.39 |
| apim_retail | APIM Retail · Autorización / contrato | componente | 4.40 |
| ilb_retail | Standard ILB privado · VIP / DNS por backend | componente | 4.40 |
| pod_r_0 | R:M-01 · Oferta comercial · E1 · Java / Spring · DB y permisos propios | workload | 4.40 |
| pod_r_1 | R:M-02 · Abastecimiento · E2 · Java / Spring · DB y permisos propios | workload | 4.40 |
| pod_r_2 | R:M-03 · Existencias · E1 · Java / Spring · DB y permisos propios | workload | 4.40 |
| pod_r_3 | R:V-01 · Pedidos · E2 · Java / Spring · DB y permisos propios | workload | 4.40 |
| pod_r_4 | R:V-02 · Ventas · E1 · Java / Spring · DB y permisos propios | workload | 4.40 |
| pod_r_5 | R:V-03 · Comisiones · E2 · Java / Spring · DB y permisos propios | workload | 4.40 |
| pod_r_6 | R:V-04 · Marketplace · E2 · Java / Spring · DB y permisos propios | workload | 4.40 |
| pod_r_7 | R:CL-01 · Posventa · E2 · Java / Spring · DB y permisos propios | workload | 4.40 |
| pod_r_8 | R:CL-02 · Clientes Retail · E2 · Java / Spring · DB y permisos propios | workload | 4.40 |
| r_sys_1 | R-SYS-01 · AZ1 · VMSS Linux · SKU pendiente · kube-system / DNS · Agentes y políticas | servidor_iaas | 4.40 |
| r_sys_2 | R-SYS-02 · AZ2 · VMSS Linux · SKU pendiente · kube-system / DNS · Agentes y políticas | servidor_iaas | 4.40 |
| r_sys_3 | R-SYS-03 · AZ3 · VMSS Linux · SKU pendiente · kube-system / DNS · Agentes y políticas | servidor_iaas | 4.40 |
| r_biz_1 | R-BIZ-01 · AZ1 · VMSS Linux · SKU pendiente · Réplicas de R:M / R:V / R:CL · Capacidades comunes Retail | servidor_iaas | 4.40 |
| r_biz_2 | R-BIZ-02 · AZ2 · VMSS Linux · SKU pendiente · Réplicas de R:M / R:V / R:CL · Capacidades comunes Retail | servidor_iaas | 4.40 |
| r_biz_3 | R-BIZ-03 · AZ3 · VMSS Linux · SKU pendiente · Réplicas de R:M / R:V / R:CL · Capacidades comunes Retail | servidor_iaas | 4.40 |
| r_int_1 | R-INT-01 · AZ1 · VMSS Linux · SKU pendiente · Adaptadores Retail · Outbox / proyecciones / sagas | servidor_iaas | 4.40 |
| r_int_2 | R-INT-02 · AZ2 · VMSS Linux · SKU pendiente · Adaptadores Retail · Outbox / proyecciones / sagas | servidor_iaas | 4.40 |
| r_int_3 | R-INT-03 · AZ3 · VMSS Linux · SKU pendiente · Adaptadores Retail · Outbox / proyecciones / sagas | servidor_iaas | 4.40 |
| r_state_1 | R-STATE-01 · AZ1 · VMSS Linux · SKU pendiente · OpenSearch / índice catálogo · OpenMetadata / MLflow | servidor_iaas | 4.40 |
| r_state_2 | R-STATE-02 · AZ2 · VMSS Linux · SKU pendiente · OpenSearch / índice catálogo · OpenMetadata / MLflow | servidor_iaas | 4.40 |
| r_state_3 | R-STATE-03 · AZ3 · VMSS Linux · SKU pendiente · OpenSearch / índice catálogo · OpenMetadata / MLflow | servidor_iaas | 4.40 |
| r_ops_1 | R-OPS-01 · AZ1 · VMSS Linux · SKU pendiente · Collector / Prometheus · Loki / Tempo / Grafana | servidor_iaas | 4.40 |
| r_ops_2 | R-OPS-02 · AZ2 · VMSS Linux · SKU pendiente · Collector / Prometheus · Loki / Tempo / Grafana | servidor_iaas | 4.40 |
| r_ops_3 | R-OPS-03 · AZ3 · VMSS Linux · SKU pendiente · Collector / Prometheus · Loki / Tempo / Grafana | servidor_iaas | 4.40 |
| control_r | Plano de control AKS · Administrado por Microsoft · No se cotizan maestros | paas | 4.40 |
| web_r | Frontend web Retail · React / contenido estático · Deployment en VMSS BIZ | workload | 4.40 |
| batch_r | R-BATCH-01..N · Python / scikit-learn · MLflow en VMSS STATE | servidor_iaas | 4.40 |
| batch_data_r | PE de Storage Retail · Conjuntos versionados ADLS · Detalle de datos en 4.42 | componente | 4.40 |
| apim_f_runtime | APIM Filial · Canales propios y X-01 | componente | 4.41 |
| ilb_f_runtime | Standard ILB Filial · VIP de servicios financieros | componente | 4.41 |
| pod_f_0 | F:C-01 · Originación · Java / Spring · Estado y permisos propios | workload | 4.41 |
| pod_f_1 | F:C-02 · Cartera · Java / Spring · Estado y permisos propios | workload | 4.41 |
| pod_f_2 | F:C-03 · Evidencia financiera · Java / Spring · Estado y permisos propios | workload | 4.41 |
| f_sys_1 | F-SYS-01 · AZ1 · VMSS Linux · SKU pendiente · Sistema / políticas | servidor_iaas | 4.41 |
| f_sys_2 | F-SYS-02 · AZ2 · VMSS Linux · SKU pendiente · Sistema / políticas | servidor_iaas | 4.41 |
| f_sys_3 | F-SYS-03 · AZ3 · VMSS Linux · SKU pendiente · Sistema / políticas | servidor_iaas | 4.41 |
| f_biz_1 | F-BIZ-01 · AZ1 · VMSS Linux · SKU pendiente · F:C-01 / F:C-02 / F:C-03 | servidor_iaas | 4.41 |
| f_biz_2 | F-BIZ-02 · AZ2 · VMSS Linux · SKU pendiente · F:C-01 / F:C-02 / F:C-03 | servidor_iaas | 4.41 |
| f_biz_3 | F-BIZ-03 · AZ3 · VMSS Linux · SKU pendiente · F:C-01 / F:C-02 / F:C-03 | servidor_iaas | 4.41 |
| f_int_1 | F-INT-01 · AZ1 · VMSS Linux · SKU pendiente · Crédito 2011 / proyecciones · Sagas / outbox Filial | servidor_iaas | 4.41 |
| f_int_2 | F-INT-02 · AZ2 · VMSS Linux · SKU pendiente · Crédito 2011 / proyecciones · Sagas / outbox Filial | servidor_iaas | 4.41 |
| f_int_3 | F-INT-03 · AZ3 · VMSS Linux · SKU pendiente · Crédito 2011 / proyecciones · Sagas / outbox Filial | servidor_iaas | 4.41 |
| f_state_1 | F-STATE-01 · AZ1 · VMSS Linux · SKU pendiente · OpenSearch / OpenMetadata · Sin MLflow financiero | servidor_iaas | 4.41 |
| f_state_2 | F-STATE-02 · AZ2 · VMSS Linux · SKU pendiente · OpenSearch / OpenMetadata · Sin MLflow financiero | servidor_iaas | 4.41 |
| f_state_3 | F-STATE-03 · AZ3 · VMSS Linux · SKU pendiente · OpenSearch / OpenMetadata · Sin MLflow financiero | servidor_iaas | 4.41 |
| f_ops_1 | F-OPS-01 · AZ1 · VMSS Linux · SKU pendiente · Collector / métricas / logs · Trazas y Grafana propios | servidor_iaas | 4.41 |
| f_ops_2 | F-OPS-02 · AZ2 · VMSS Linux · SKU pendiente · Collector / métricas / logs · Trazas y Grafana propios | servidor_iaas | 4.41 |
| f_ops_3 | F-OPS-03 · AZ3 · VMSS Linux · SKU pendiente · Collector / métricas / logs · Trazas y Grafana propios | servidor_iaas | 4.41 |
| x_sys_1 | X-SYS-01 · AZ1 · Sistema | servidor_iaas | 4.41 |
| x_sys_2 | X-SYS-02 · AZ2 · Sistema | servidor_iaas | 4.41 |
| x_sys_3 | X-SYS-03 · AZ3 · Sistema | servidor_iaas | 4.41 |
| x_biz_1 | X-BIZ-01 · AZ1 · X-01 / políticas / bitácora · Identidad propia | servidor_iaas | 4.41 |
| x_biz_2 | X-BIZ-02 · AZ2 · X-01 / políticas / bitácora · Identidad propia | servidor_iaas | 4.41 |
| x_biz_3 | X-BIZ-03 · AZ3 · X-01 / políticas / bitácora · Identidad propia | servidor_iaas | 4.41 |
| x_runtime | X-01 · Deployment · Fichas / control de cruces · Custodia por aprobar | workload | 4.41 |
| x_ilb_runtime | ILB Frontera · Entrada desde Ventas | componente | 4.41 |
| web_f | Frontend web Filial · React / sesión titular · Deployment en VMSS BIZ | workload | 4.41 |
| apps_r | Servicios Retail · VMSS BIZ / APIs privadas | componente | 4.42 |
| workers_r | Trabajadores Java / Spring · VMSS INT · corte / calidad · Outbox / proyecciones | componente | 4.42 |
| adf_r | Azure Data Factory · Factory / IR: región por validar · Cargas autorizadas | paas | 4.42 |
| pe_sb_r | PE Service Bus · Namespace propio | componente | 4.42 |
| pe_st_r | PE Storage por cuenta · Blob + DFS según uso · NIC distinta por subrecurso | componente | 4.42 |
| pg-r-merc | pg-r-merc · PostgreSQL Flexible Server · Mercadería · DB por autoridad M-01/02/03 · Primario + espera entre AZ | servidor_administrado | 4.42 |
| pe-pg-r-merc | PE · pg-r-merc · FQDN privado propio · Acceso público deshabilitado | componente | 4.42 |
| pg-r-venta | pg-r-venta · PostgreSQL Flexible Server · Venta · DB por autoridad V-01..04 · Primario + espera entre AZ | servidor_administrado | 4.42 |
| pe-pg-r-venta | PE · pg-r-venta · FQDN privado propio · Acceso público deshabilitado | componente | 4.42 |
| pg-r-clientes | pg-r-clientes · PostgreSQL Flexible Server · Clientes · DB Posventa / Clientes · Primario + espera entre AZ | servidor_administrado | 4.42 |
| pe-pg-r-clientes | PE · pg-r-clientes · FQDN privado propio · Acceso público deshabilitado | componente | 4.42 |
| pg-r-vector | pg-r-vector · PostgreSQL Flexible Server · Oferta pgvector · Índice derivado aislado · Primario + espera entre AZ | servidor_administrado | 4.42 |
| pe-pg-r-vector | PE · pg-r-vector · FQDN privado propio · Acceso público deshabilitado | componente | 4.42 |
| pg-r-mart | pg-r-mart · PostgreSQL Flexible Server · Modelos analíticos · Solo lectura desde BI · Primario + espera entre AZ | servidor_administrado | 4.42 |
| pe-pg-r-mart | PE · pg-r-mart · FQDN privado propio · Acceso público deshabilitado | componente | 4.42 |
| pg-r-tech | pg-r-tech · PostgreSQL Flexible Server · Metadatos técnicos · OpenMetadata / MLflow · Primario + espera entre AZ | servidor_administrado | 4.42 |
| pe-pg-r-tech | PE · pg-r-tech · FQDN privado propio · Acceso público deshabilitado | componente | 4.42 |
| sb_r | Service Bus Premium Retail · Mensajes / tópicos propios · DLQ y recuperación definida | paas | 4.42 |
| lake_r | ADLS Gen2 Retail · Landing / curados / historia · Conjuntos versionados | paas | 4.42 |
| worm_r | Blob WORM Retail · Retención por clase · Auditoría y archivo | paas | 4.42 |
| idx_r | VMSS STATE · OpenSearch · Búsqueda del negocio · Índice catálogo separado | componente | 4.42 |
| om_r | VMSS STATE · OpenMetadata · Catálogo / calidad / linaje · Dependencias compatibles | componente | 4.42 |
| redis_r_data | Azure Managed Redis · Oferta reconstruible · No autoridad de stock | paas | 4.42 |
| pe_redis_r | PE Managed Redis · FQDN privado propio | componente | 4.42 |
| bi_vm_r1 | R-BI-01 · AZ1 · VM Windows Server 2022 · Data gateway estándar | servidor_iaas | 4.42 |
| bi_vm_r2 | R-BI-02 · AZ2 · VM Windows Server 2022 · Data gateway estándar | servidor_iaas | 4.42 |
| ir_vm_r1 | R-IR-01 · AZ1 · VM Windows · SHIR de ADF · Web/REST privado / cargas | servidor_iaas | 4.42 |
| ir_vm_r2 | R-IR-02 · AZ2 · VM Windows · SHIR de ADF · Web/REST privado / cargas | servidor_iaas | 4.42 |
| pbi_r | Power BI SaaS · Workspace propio / permisos · Import o DirectQuery | saas | 4.42 |
| relay_r | Canal de datos del gateway · HTTPS saliente / Relay · No es gateway de APIs | saas | 4.42 |
| apps_f | Servicios Filial · VMSS BIZ / APIs privadas | componente | 4.43 |
| workers_f | Trabajadores Java / Spring · VMSS INT · corte / calidad · Outbox / proyecciones | componente | 4.43 |
| adf_f | Azure Data Factory · Factory / IR: región por validar · Cargas autorizadas | paas | 4.43 |
| pe_sb_f | PE Service Bus · Namespace propio | componente | 4.43 |
| pe_st_f | PE Storage por cuenta · Blob + DFS según uso · NIC distinta por subrecurso | componente | 4.43 |
| pg-f-originacion | pg-f-originacion · PostgreSQL Flexible Server · Originación · Evaluación / cupo / autorización · Primario + espera entre AZ | servidor_administrado | 4.43 |
| pe-pg-f-originacion | PE · pg-f-originacion · FQDN privado propio · Acceso público deshabilitado | componente | 4.43 |
| pg-f-cartera | pg-f-cartera · PostgreSQL Flexible Server · Cartera · Cuenta / saldo / pagos · Primario + espera entre AZ | servidor_administrado | 4.43 |
| pe-pg-f-cartera | PE · pg-f-cartera · FQDN privado propio · Acceso público deshabilitado | componente | 4.43 |
| pg-f-evidencia | pg-f-evidencia · PostgreSQL Flexible Server · Evidencia · Expediente y metadatos · Primario + espera entre AZ | servidor_administrado | 4.43 |
| pe-pg-f-evidencia | PE · pg-f-evidencia · FQDN privado propio · Acceso público deshabilitado | componente | 4.43 |
| pg-f-mart | pg-f-mart · PostgreSQL Flexible Server · Modelos analíticos · Sin consulta a operacional · Primario + espera entre AZ | servidor_administrado | 4.43 |
| pe-pg-f-mart | PE · pg-f-mart · FQDN privado propio · Acceso público deshabilitado | componente | 4.43 |
| pg-f-tech | pg-f-tech · PostgreSQL Flexible Server · Metadatos técnicos · OpenMetadata propio · Primario + espera entre AZ | servidor_administrado | 4.43 |
| pe-pg-f-tech | PE · pg-f-tech · FQDN privado propio · Acceso público deshabilitado | componente | 4.43 |
| sb_f | Service Bus Premium Filial · Mensajes / tópicos propios · DLQ y recuperación definida | paas | 4.43 |
| lake_f | ADLS Gen2 Filial · Landing / curados / historia · Conjuntos versionados | paas | 4.43 |
| worm_f | Blob WORM Filial · Retención por clase · Auditoría y archivo | paas | 4.43 |
| idx_f | VMSS STATE · OpenSearch · Búsqueda del negocio · Índice catálogo separado | componente | 4.43 |
| om_f | VMSS STATE · OpenMetadata · Catálogo / calidad / linaje · Dependencias compatibles | componente | 4.43 |
| evidence_blob_f | Blob evidencia vigente · F:C-03 propietario · Contenido + integridad | paas | 4.43 |
| pg-x01 | pg-x01 · PostgreSQL propio · Fichas y bitácora mínima | servidor_administrado | 4.43 |
| pe_pg_x01 | PE de Frontera · Solo credencial X-01 | componente | 4.43 |
| x01_data_client | X-01 · VMSS BIZ Frontera · Referencia a vista 4.41 · Sin credenciales Filial | componente | 4.43 |
| bi_vm_f1 | F-BI-01 · AZ1 · VM Windows Server 2022 · Data gateway estándar | servidor_iaas | 4.43 |
| bi_vm_f2 | F-BI-02 · AZ2 · VM Windows Server 2022 · Data gateway estándar | servidor_iaas | 4.43 |
| ir_vm_f1 | F-IR-01 · AZ1 · VM Windows · SHIR de ADF · Web/REST privado / cargas | servidor_iaas | 4.43 |
| ir_vm_f2 | F-IR-02 · AZ2 · VM Windows · SHIR de ADF · Web/REST privado / cargas | servidor_iaas | 4.43 |
| pbi_f | Power BI SaaS · Workspace propio / permisos · Import o DirectQuery | saas | 4.43 |
| relay_f | Canal de datos del gateway · HTTPS saliente / Relay · No es gateway de APIs | saas | 4.43 |
| admin_pc | Administrador · Equipo compatible / Intune | componente | 4.44 |
| apps_ops | Aplicaciones / workers · Experiencia real / auditoría | componente | 4.44 |
| device | Terminales y nodos · Defender / identidad de equipo | componente | 4.44 |
| id_ops | Entra ID P2 / External ID · Ámbitos de identidad propios | componente | 4.44 |
| pim_ops | PIM · elevación · Aprobación / expiración · No proxy de sesiones | componente | 4.44 |
| access_ops | Entra Private Access · Servicio global / acceso remoto · No reemplaza VPN S2S | componente | 4.44 |
| bastion_ops | Bastion Premium · RDP/SSH autorizado · Grabación compatible | componente | 4.44 |
| kv_ops | Key Vault / Managed HSM · Recursos distintos · Claves y secretos propios | componente | 4.44 |
| workload_ops | Workload Identity · Cuenta por carga · Permisos por recurso | componente | 4.44 |
| collector_ops | Collector OpenTelemetry · Agente / gateway por ámbito · Cola persistente en tienda | componente | 4.44 |
| grafana_ops | Grafana + Alerting · VMSS OPS por ámbito · Consulta / aviso | componente | 4.44 |
| blackbox_ops | R/F-SYN-01 · VM Linux · Blackbox Exporter · Ubicación independiente por fijar | componente | 4.44 |
| ops1 | OPS-01 · AZ1 · VMSS Linux | componente | 4.44 |
| ops2 | OPS-02 · AZ2 · VMSS Linux | componente | 4.44 |
| ops3 | OPS-03 · AZ3 · VMSS Linux | componente | 4.44 |
| prom_ops | Prometheus · Métricas / persistencia · HA por validar | componente | 4.44 |
| loki_ops | Loki · Registros saneados · Almacenamiento propio | componente | 4.44 |
| tempo_ops | Tempo · Trazas saneadas · Almacenamiento propio | componente | 4.44 |
| monitor_ops | Azure Monitor / Log Analytics · Diagnóstico Azure · VNet flow logs | componente | 4.44 |
| sentinel_ops | Sentinel / Defender · Fuentes de seguridad · SOC / planes declarados | componente | 4.44 |
| stage_ops | Blob temporal Bastion · Mutable / sin versionado · Ventana protegida | componente | 4.44 |
| worm_ops | Blob WORM del ámbito · Copia verificada / custodia · Política de retención | componente | 4.44 |
| backup_ops | Backup / PITR · Cobertura por recurso · Restauración con claves | componente | 4.44 |
| connector_ops1 | R/F-PA-01 · AZ1 · VM Windows Server 2022 · Private Network Connector | servidor_iaas | 4.44 |
| connector_ops2 | R/F-PA-02 · AZ2 · VM Windows Server 2022 · Private Network Connector | servidor_iaas | 4.44 |
| staff_dc | Personal administrativo · Finanzas / abastecimiento | componente | 4.45 |
| erp_host | HOST-ERP · por inventariar · ERP / DTE / remuneraciones · Conservado | componente | 4.45 |
| retail_old | HOST-RETAIL-2009 · Convivencia por olas · Ubicación supuesta | componente | 4.45 |
| credit_old | HOST-CREDITO-2011 · Convivencia y migración · Custodia Filial | componente | 4.45 |
| ir_r | DC-IR-R-01/02 · Self-hosted IR de ADF · Extracción Retail autorizada | componente | 4.45 |
| ir_f | DC-IR-F-01/02 · Self-hosted IR de ADF · Extracción Filial autorizada | componente | 4.45 |
| dc_router | Routers / firewall DC-01 · Contextos y rutas propias | componente | 4.45 |
| er_dc | ExpressRoute DC-01 · Circuito / gateway por aprobar | componente | 4.45 |
| wms_host | HOST-WMS · por inventariar · WMS conservado · Sin reemplazo decidido | componente | 4.45 |
| scanner_cd | Terminales / lectores CD · Captura y preparación | componente | 4.45 |
| local_cd | CD-LOCAL-01/02 · Captura durable / sincronía · No se duplica el WMS | componente | 4.45 |
| router_cd | Firewall / dos proveedores · VPN por ámbito | componente | 4.45 |
| terminal_conce | Terminales Concepción · Captura estructurada | componente | 4.45 |
| local_conce | CD02-LOCAL-01/02 · Diario de operación · Sustituye registro en planillas | componente | 4.45 |
| router_conce | Enlace actual único · Segundo enlace propuesto | componente | 4.45 |
| dc2_backup | Infraestructura DC-02 · Inventario / uso por acreditar · Riesgo común con DC-01 | componente | 4.45 |
| azure_dc_r | Entrada privada Retail · VPN / Firewall / APIs | componente | 4.45 |
| azure_dc_f | Entrada privada Filial · VPN / Firewall / APIs | componente | 4.45 |
| workers_dc | VMSS INT del ámbito · Adaptadores / proyecciones · No hay base compartida | componente | 4.45 |
| adf_dc | ADF por ámbito · Pipelines / corte / linaje | componente | 4.45 |
| local_dr | Diarios Retail / cupo Filial · Custodias separadas · Venta local bajo política | componente | 4.46 |
| cl_apps | AKS y pools por ámbito · Pods repartidos AZ1/2/3 | componente | 4.46 |
| cl_pg | PostgreSQL primario / espera · Por recurso y autoridad | componente | 4.46 |
| cl_bus | Service Bus Premium · Namespaces R / F distintos | componente | 4.46 |
| cl_store | ADLS / Blob / índices · Claves / configuración | componente | 4.46 |
| br_gate | Borde / App Gateway / APIM · Gateways regionales propios | componente | 4.46 |
| br_apps | AKS / VMSS Retail · Capacidad caliente propuesta · Arranque y carga por ensayar | componente | 4.46 |
| br_pg | Réplicas PostgreSQL Retail · Promoción y HA posterior | componente | 4.46 |
| br_bus | Service Bus Retail · Geo-Replication de datos · Compatibilidad por verificar | componente | 4.46 |
| br_store | Storage / reconstrucción · Catálogo / índices / modelos · Claves recuperables | componente | 4.46 |
| f_site | Sitio Filial independiente · No DC-02 en misma comuna · País / tecnología pendientes | componente | 4.46 |
| f_stack | Pila financiera recuperable · Cómputo, DB, broker, evidencia · Claves, red e identidad | componente | 4.46 |
| fd_dr | Front Door · Health probes / origen DR · Mismo perfil por ámbito | componente | 4.46 |
| operator_dr | Operador / runbook · Declaración / pruebas / retorno | componente | 4.46 |
| repo_ci | Repositorio / IaC · Revisión de cambios | componente | 4.47 |
| pipe_ci | Pipeline de entrega · SAST / SBOM / firma · Pruebas y aprobación | componente | 4.47 |
| acr_ci | ACR Premium por dominio · Imágenes firmadas · Acceso privado | componente | 4.47 |
| api_ci | API Center por ámbito · OpenAPI 3.1 / derivado 3.0.3 · Validación de contrato | componente | 4.47 |
| dev_r | Retail · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| dev_f | Filial · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| dev_x | Frontera · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| qa_r | Retail · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| qa_f | Filial · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| qa_x | Frontera · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| pre_r | Retail · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| pre_f | Filial · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| pre_x | Frontera · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| prod_r | Retail · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| prod_f | Filial · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| prod_x | Frontera · Suscripción / Key Vault propios · AKS / datos / permisos · Sin copias reales inferiores | componente | 4.47 |
| dr_ci_r | Retail DR · IaC / imágenes / claves · Datos recuperables | componente | 4.47 |
| dr_ci_f | Filial DR · Destino aprobado · Pila completa recuperable | componente | 4.47 |
