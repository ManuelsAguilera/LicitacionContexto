# Relaciones de la vista general

La numeración de este inventario permite revisar extremos; no se imprime en el dibujo.

| Relación | Inicio | Destino | Intención |
| --- | --- | --- | --- |
| 1 | fd | ag_r | Private Link propio / HTTPS |
| 2 | vpn_r | fw_r | Tráfico híbrido |
| 3 | fw_r | ag_r | HTTPS inspeccionado |
| 4 | ag_r | apim_r | Ruta API HTTPS |
| 5 | apim_r | ilb_r | Backend privado |
| 6 | ag_r | ilb_r | Ruta web privada |
| 7 | ilb_r | biz_r | Service → pods |
| 8 | biz_r | data_r | PE / datos propietarios |
| 9 | tech_r | data_r | PE / recursos técnicos |
| 10 | biz_r | tech_r | Contratos / eventos propios |
| 11 | fd | ag_f | Private Link propio / HTTPS |
| 12 | vpn_f | fw_f | Tráfico híbrido |
| 13 | fw_f | ag_f | HTTPS inspeccionado |
| 14 | ag_f | apim_f | Ruta API HTTPS |
| 15 | apim_f | ilb_f | Backend privado |
| 16 | ag_f | ilb_f | Ruta web privada |
| 17 | ilb_f | biz_f | Service → pods |
| 18 | biz_f | data_f | PE / datos propietarios |
| 19 | tech_f | data_f | PE / recursos técnicos |
| 20 | biz_f | tech_f | Contratos / eventos propios |
| 21 | biz_r | x01 | Ventas → compra autorizada |
| 22 | x01 | pgx | PE / bitácora propia |
| 23 | x01 | ag_f | Contrato financiero permitido |
| 24 | data_r | dr | Copia Retail |
| 25 | data_f | dr | Copia Filial |
| 26 | fw_r | soc | Eventos de seguridad |
| 27 | fw_f | soc | Eventos de seguridad |
| 28 | cliente | fd | Internet HTTPS |
| 29 | cliente | entra | Identidad de cliente / titular |
| 30 | personal | vpn_r | LAN / firewall local / VPN R |
| 31 | personal | vpn_f | LAN / firewall local / VPN F |
| 32 | personal | local_r | Contrato local Retail |
| 33 | personal | local_f | Contrato local Filial |
| 34 | conservados | vpn_r | Integración privada Retail |
| 35 | personal | bastion | Solo perfil administrativo autorizado |
