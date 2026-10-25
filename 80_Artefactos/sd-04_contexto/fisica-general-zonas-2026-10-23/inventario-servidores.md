# Componentes y alojamiento de la general

Los símbolos de pool y datos agrupan recursos separados; esta lista no fija tamaños, cantidades ni asignación de pods a una VM.

| ID | Componente | Zona |
| --- | --- | --- |
| cliente | Cliente / titular · Navegador o app | Exterior |
| fd | Front Door Premium · WAF · perfiles R / F | global |
| ag_r | Application Gateway | retail |
| apim_r | API Management | retail |
| ilb_r | Load Balancer interno · VIP / Service por backend | retail |
| biz_r | Pool BIZ · Servicios / frontend | aks_r |
| tech_r | Pools técnicos · SYS · INT · STATE · OPS | aks_r |
| data_r | Datos Retail · PostgreSQL / PaaS propios | paas |
| vpn_r | VPN Gateway | hubr |
| fw_r | Azure Firewall | hubr |
| ag_f | Application Gateway | filial |
| apim_f | API Management | filial |
| ilb_f | Load Balancer interno · VIP / Service por backend | filial |
| biz_f | Pool BIZ · Servicios / frontend | aks_f |
| tech_f | Pools técnicos · SYS · INT · STATE · OPS | aks_f |
| data_f | Datos Filial · PostgreSQL / PaaS propios | paas |
| vpn_f | VPN Gateway | hubf |
| fw_f | Azure Firewall | hubf |
| x01 | X-01 · Control de cruces | frontera |
| pgx | PostgreSQL · Bitácora X-01 | frontera |
| dr | Recuperación Retail y Filial · Recursos y datos separados | brasil |
| entra | Entra ID / External ID · Identidad y privilegios | seg |
| kv | Key Vault · Secretos / certificados | seg |
| hsm | Managed HSM · Custodia de claves | seg |
| bastion | Azure Bastion · Acceso administrativo | seg |
| soc | Log Analytics / Sentinel · Señales de seguridad | seg |
| personal | Personal de la empresa · POS / móvil / PC / mesón | sedes |
| conservados | Sistemas conservados Retail · ERP / DTE / WMS | sedes |
| local_r | Par local Retail · Venta / diario durable | tiendas |
| local_f | Par local Filial · Cupo preautorizado | tiendas |
