# Inventario de relaciones físicas

El número de cada enlace coincide con el de la lámina. La flecha indica el inicio de la conexión; la respuesta pertenece al mismo intercambio. Las relaciones de despliegue, réplica y ejecución no son tráfico de API.

## 4.37 · Arquitectura física general · personas, sitios y Azure

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | ag | frontend | HTTPS · contenido web |
| 02 | clientes | fd | HTTPS 443 |
| 03 | personal | tiendas | Operación local |
| 04 | operador | ops | Acceso privilegiado |
| 05 | tiendas | wan | VPN IPsec |
| 06 | cdprincipal | wan | VPN / respaldo |
| 07 | dc | wan | ER propuesto / VPN |
| 08 | wan | vpn | IPsec por ámbito |
| 09 | vpn | fw | Rutas inspeccionadas |
| 10 | fw | ag | HTTPS privado |
| 11 | fd | afdpl | Origen privado |
| 12 | afdpl | ag | HTTPS + aprobación |
| 13 | ag | apim | HTTPS privado |
| 14 | apim | lb | Backend privado |
| 15 | lb | aksr | VIP Retail |
| 16 | lb | aksf | VIP Filial |
| 17 | aksr | aksx | Compra por X-01 |
| 18 | aksx | apim | Solo contrato Filial |
| 19 | aksr | pe | Permisos Retail |
| 20 | aksf | pe | Permisos Filial |
| 21 | pe | datos | Acceso al PaaS |
| 22 | aksr | plataforma | Proyecciones Retail |
| 23 | aksf | plataforma | Proyecciones Filial |
| 24 | dc | erp | Interfaces privadas |
| 25 | partners | ag | Contratos autorizados |
| 26 | datos | brazil | Réplica Retail |
| 27 | datos | drf | Copia Filial autorizada |

## 4.38 · Tienda tipo · terminales, IoT, continuidad y separación financiera

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | actor_tienda | pos | Uso |
| 02 | actor_cliente | locker_hw | Retiro |
| 03 | scanner | pos | Lectura local |
| 04 | pos | printer | Impresión local |
| 05 | pos | tpv | Pago tokenizado |
| 06 | pos | local_ra | Venta local TLS |
| 07 | local_ra | local_rb | Diario + fencing |
| 08 | movil_sala | ap_staff | Wi-Fi corporativo |
| 09 | ap_staff | sw_a | LAN autorizada |
| 10 | meson | sw_a | LAN Retail |
| 11 | fila_local | local_ra | Cola / config local |
| 12 | locker_control | locker_hw | Comando / sensor |
| 13 | locker_control | sw_a | VLAN IoT |
| 14 | camera | nvr | Video propio |
| 15 | ap_guest | fw_a | Solo salida Internet |
| 16 | meson_f | local_fa | Autorización local limitada |
| 17 | local_fa | local_fb | Consumo durable propio |
| 18 | local_fa | sw_a | VLAN Filial |
| 19 | local_ra | sw_a | Sincronización Retail |
| 20 | sw_a | sw_b | Par de switches |
| 21 | sw_a | fw_a | Tráfico segmentado |
| 22 | sw_b | fw_b | Ruta alternativa |
| 23 | fw_a | fw_b | HA / control |
| 24 | fw_a | isp | WAN |
| 25 | fw_b | lte | Respaldo WAN |
| 26 | isp | azure_r | VPN Retail |
| 27 | isp | azure_f | VPN Filial |

## 4.39 · Red Azure · dominios separados, DNS y rutas de entrada

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | s2s | vpn_r | IPsec / BGP |
| 02 | vpn_r | fw_r | UDR / retorno simétrico |
| 03 | fw_r | ag_r | HTTPS permitido |
| 04 | pl_brazil | ag_r | Origen privado propio |
| 05 | ag_r | apim_r | HTTPS / probe / host |
| 06 | apim_r | lb_r | Backend privado 443 |
| 07 | lb_r | aks_r | TLS / Service |
| 08 | aks_r | pe_r | Permiso mínimo |
| 09 | s2s | vpn_f | IPsec / BGP |
| 10 | vpn_f | fw_f | UDR / retorno simétrico |
| 11 | fw_f | ag_f | HTTPS permitido |
| 12 | pl_brazil | ag_f | Origen privado propio |
| 13 | ag_f | apim_f | HTTPS / probe / host |
| 14 | apim_f | lb_f | Backend privado 443 |
| 15 | lb_f | aks_f | TLS / Service |
| 16 | aks_f | pe_f | Permiso mínimo |
| 17 | web_client | fd_net | HTTPS 443 |
| 18 | fd_net | pl_brazil | Private Link |
| 19 | ag_r | lb_r | Solo backend web UI |
| 20 | ag_f | lb_f | Solo backend web UI |
| 21 | aks_r | x01net | Compra bajo X-01 |
| 22 | x01net | x01pe | Identidad X-01 |
| 23 | x01pe | ag_f | Solo entrada Filial |
| 24 | pe_r | pgcloud | Solo recurso propio |
| 25 | pe_r | sbcloud | Solo recurso propio |
| 26 | pe_f | pgcloud | Solo recurso propio |
| 27 | pe_f | sbcloud | Solo recurso propio |

## 4.40 · Ejecución Retail · servicios, pods y servidores VMSS

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | apim_retail | ilb_retail | HTTPS 443 |
| 02 | ilb_retail | pod_r_0 | TLS · API autorizada |
| 03 | pod_r_0 | pool_biz | Programación de pods |
| 04 | ilb_retail | pod_r_1 | TLS · API autorizada |
| 05 | pod_r_1 | pool_biz | Programación de pods |
| 06 | ilb_retail | pod_r_2 | TLS · API autorizada |
| 07 | pod_r_2 | pool_biz | Programación de pods |
| 08 | ilb_retail | pod_r_3 | TLS · API autorizada |
| 09 | pod_r_3 | pool_biz | Programación de pods |
| 10 | ilb_retail | pod_r_4 | TLS · API autorizada |
| 11 | pod_r_4 | pool_biz | Programación de pods |
| 12 | ilb_retail | pod_r_5 | TLS · API autorizada |
| 13 | pod_r_5 | pool_biz | Programación de pods |
| 14 | ilb_retail | pod_r_6 | TLS · API autorizada |
| 15 | pod_r_6 | pool_biz | Programación de pods |
| 16 | ilb_retail | pod_r_7 | TLS · API autorizada |
| 17 | pod_r_7 | pool_biz | Programación de pods |
| 18 | ilb_retail | pod_r_8 | TLS · API autorizada |
| 19 | pod_r_8 | pool_biz | Programación de pods |
| 20 | web_r | pool_biz | Programación de pods |
| 21 | batch_r | batch_data_r | Lectura de conjunto autorizado |
| 22 | batch_r | pool_state | Registro MLflow privado |

## 4.41 · Ejecución Filial y Frontera · servidores y separación

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | apim_f_runtime | ilb_f_runtime | HTTPS 443 |
| 02 | ilb_f_runtime | pod_f_0 | TLS autorizado |
| 03 | pod_f_0 | fpool_biz | Programación de pods |
| 04 | ilb_f_runtime | pod_f_1 | TLS autorizado |
| 05 | pod_f_1 | fpool_biz | Programación de pods |
| 06 | ilb_f_runtime | pod_f_2 | TLS autorizado |
| 07 | pod_f_2 | fpool_biz | Programación de pods |
| 08 | x_ilb_runtime | x_runtime | Compra autorizable |
| 09 | x_runtime | apim_f_runtime | Por PE y listener Filial |
| 10 | web_f | fpool_biz | Programación de pods |

## 4.42 · Datos Retail · PaaS, procesamiento y conexión BI

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | pe-pg-r-merc | pg-r-merc | 5432 / TLS |
| 02 | apps_r | pe-pg-r-merc | Solo servicio propietario |
| 03 | pe-pg-r-venta | pg-r-venta | 5432 / TLS |
| 04 | apps_r | pe-pg-r-venta | Solo servicio propietario |
| 05 | pe-pg-r-clientes | pg-r-clientes | 5432 / TLS |
| 06 | apps_r | pe-pg-r-clientes | Solo servicio propietario |
| 07 | pe-pg-r-vector | pg-r-vector | 5432 / TLS |
| 08 | apps_r | pe-pg-r-vector | Solo servicio propietario |
| 09 | pe-pg-r-mart | pg-r-mart | 5432 / TLS |
| 10 | pe-pg-r-tech | pg-r-tech | 5432 / TLS |
| 11 | workers_r | pe_redis_r | Caché / invalidación |
| 12 | pe_redis_r | redis_r_data | TLS · puerto por SKU |
| 13 | ir_vm_r1 | adf_r | Canal saliente de control |
| 14 | ir_vm_r1 | workers_r | REST privado autorizado |
| 15 | ir_vm_r2 | adf_r | Canal saliente de control |
| 16 | ir_vm_r2 | workers_r | REST privado autorizado |
| 17 | apps_r | pe_sb_r | Outbox AMQPS |
| 18 | pe_sb_r | sb_r | 5671 / TLS |
| 19 | workers_r | pe_sb_r | Consumo AMQPS durable |
| 20 | workers_r | pe_st_r | Ingesta / reconstrucción |
| 21 | pe_st_r | lake_r | Blob / DFS 443 |
| 22 | workers_r | idx_r | Indexación con permisos |
| 23 | workers_r | om_r | Linaje / calidad |
| 24 | workers_r | pe-pg-r-mart | Proyección idempotente |
| 25 | om_r | pe-pg-r-tech | Metadatos propios |
| 26 | bi_vm_r1 | relay_r | HTTPS saliente |
| 27 | bi_vm_r1 | pe-pg-r-mart | SQL TLS analítico |
| 28 | bi_vm_r2 | relay_r | HTTPS saliente |
| 29 | bi_vm_r2 | pe-pg-r-mart | SQL TLS analítico |
| 30 | pbi_r | relay_r | Solicitud de consulta |
| 31 | pe_st_r | worm_r | Archivo por cuenta / política |

## 4.43 · Datos Filial · PaaS, procesamiento y conexión BI

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | pe-pg-f-originacion | pg-f-originacion | 5432 / TLS |
| 02 | apps_f | pe-pg-f-originacion | Solo servicio propietario |
| 03 | pe-pg-f-cartera | pg-f-cartera | 5432 / TLS |
| 04 | apps_f | pe-pg-f-cartera | Solo servicio propietario |
| 05 | pe-pg-f-evidencia | pg-f-evidencia | 5432 / TLS |
| 06 | apps_f | pe-pg-f-evidencia | Solo servicio propietario |
| 07 | pe-pg-f-mart | pg-f-mart | 5432 / TLS |
| 08 | pe-pg-f-tech | pg-f-tech | 5432 / TLS |
| 09 | x01_data_client | pe_pg_x01 | Credencial propia |
| 10 | pe_pg_x01 | pg-x01 | 5432 / TLS propio |
| 11 | ir_vm_f1 | adf_f | Canal saliente de control |
| 12 | ir_vm_f1 | workers_f | REST privado autorizado |
| 13 | ir_vm_f2 | adf_f | Canal saliente de control |
| 14 | ir_vm_f2 | workers_f | REST privado autorizado |
| 15 | apps_f | pe_sb_f | Outbox AMQPS |
| 16 | pe_sb_f | sb_f | 5671 / TLS |
| 17 | workers_f | pe_sb_f | Consumo AMQPS durable |
| 18 | workers_f | pe_st_f | Ingesta / reconstrucción |
| 19 | pe_st_f | lake_f | Blob / DFS 443 |
| 20 | workers_f | idx_f | Indexación con permisos |
| 21 | workers_f | om_f | Linaje / calidad |
| 22 | workers_f | pe-pg-f-mart | Proyección idempotente |
| 23 | om_f | pe-pg-f-tech | Metadatos propios |
| 24 | bi_vm_f1 | relay_f | HTTPS saliente |
| 25 | bi_vm_f1 | pe-pg-f-mart | SQL TLS analítico |
| 26 | bi_vm_f2 | relay_f | HTTPS saliente |
| 27 | bi_vm_f2 | pe-pg-f-mart | SQL TLS analítico |
| 28 | pbi_f | relay_f | Solicitud de consulta |
| 29 | pe_st_f | worm_f | Archivo por cuenta / política |
| 30 | apps_f | pe_st_f | Documento de F:C-03 |
| 31 | pe_st_f | evidence_blob_f | Blob vigente / TLS |

## 4.44 · Seguridad y observabilidad · patrón físico por ámbito

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | connector_ops1 | access_ops | TLS saliente 443 / CRL 80 |
| 02 | connector_ops1 | bastion_ops | HTTPS 443 · PoC pendiente |
| 03 | connector_ops2 | access_ops | TLS saliente 443 / CRL 80 |
| 04 | connector_ops2 | bastion_ops | HTTPS 443 · PoC pendiente |
| 05 | admin_pc | id_ops | Autenticación |
| 06 | id_ops | pim_ops | Elevación temporal |
| 07 | admin_pc | access_ops | Sesión autorizada |
| 08 | bastion_ops | exec | RDP/SSH 3389/22 |
| 09 | apps_ops | workload_ops | Federación de carga |
| 10 | workload_ops | kv_ops | Permiso limitado |
| 11 | apps_ops | collector_ops | OTLP privado |
| 12 | device | collector_ops | Cola / reenvío |
| 13 | collector_ops | prom_ops | Métricas |
| 14 | collector_ops | loki_ops | Registros |
| 15 | collector_ops | tempo_ops | Trazas |
| 16 | grafana_ops | prom_ops | Consulta |
| 17 | grafana_ops | loki_ops | Consulta |
| 18 | grafana_ops | tempo_ops | Consulta |
| 19 | grafana_ops | monitor_ops | Consulta Azure |
| 20 | blackbox_ops | apps_ops | Prueba segura |
| 21 | monitor_ops | sentinel_ops | Fuentes de seguridad |
| 22 | bastion_ops | stage_ops | Solo recorrido compatible |
| 23 | stage_ops | worm_ops | Copia y verificación |

## 4.45 · Sitios corporativos · servidores conservados y adaptadores

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | staff_dc | erp_host | Uso autorizado |
| 02 | erp_host | ir_r | Extracción permitida |
| 03 | credit_old | ir_f | Extracción Filial |
| 04 | ir_r | adf_dc | Canal saliente TLS |
| 05 | ir_f | adf_dc | Canal propio Filial |
| 06 | dc_router | er_dc | Conexión dedicada |
| 07 | er_dc | azure_dc_r | Enlace principal |
| 08 | dc_router | azure_dc_f | VPN propia |
| 09 | scanner_cd | wms_host | Captura WMS |
| 10 | wms_host | local_cd | Interfaz por verificar |
| 11 | local_cd | router_cd | Sincronización privada |
| 12 | router_cd | azure_dc_r | VPN |
| 13 | terminal_conce | local_conce | Captura local |
| 14 | local_conce | router_conce | Sincronización |
| 15 | router_conce | azure_dc_r | VPN / respaldo pendiente |
| 16 | azure_dc_r | workers_dc | Contratos Retail |
| 17 | azure_dc_f | workers_dc | Contratos Filial propios |
| 18 | dc_router | dc2_backup | Enlace C-16 por acreditar |

## 4.46 · Recuperación · zonas, región secundaria y sitio de Filial

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | cl_pg | br_pg | Asíncrona Retail |
| 02 | cl_bus | br_bus | Datos + estado Retail |
| 03 | cl_store | br_store | Copia por recurso |
| 04 | cl_apps | br_apps | IaC / versiones |
| 05 | cl_pg | f_stack | Solo destino aprobado |
| 06 | operator_dr | fd_dr | Promoción autorizada |
| 07 | fd_dr | br_gate | Origen alternativo Retail |
| 08 | br_gate | br_apps | Ruta DR privada |
| 09 | br_apps | br_pg | Datos promovidos |
| 10 | local_dr | br_gate | Reconexión conciliada |

## 4.47 · Ambientes y entrega · infraestructura, identidad y promoción

| N.º | Origen | Destino | Intención |
| --- | --- | --- | --- |
| 01 | repo_ci | pipe_ci | Revisión y construcción |
| 02 | pipe_ci | acr_ci | Registro firmado |
| 03 | pipe_ci | api_ci | Contrato versionado |
| 04 | ci | dev | Despliegue por dominio |
| 05 | dev | qa | Pruebas |
| 06 | qa | pre | Carga / recuperación |
| 07 | pre | prod | Aprobación expresa |
| 08 | prod | dr | Misma definición / versión |
