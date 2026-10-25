# Matriz servicio → ejecución → persistencia

Trece servicios vigentes. Los pools son VMSS con nodos en AZ1, AZ2 y AZ3; el scheduler distribuye réplicas, sin fijar todas a una VM.

| Servicio | Ejecución y pool | Datos propios | Etapa |
| --- | --- | --- | --- |
| R:M-01 · Oferta comercial | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-merc; base lógica y rol propios | E1 |
| R:M-02 · Abastecimiento | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-merc; base lógica y rol propios | E2 |
| R:M-03 · Existencias | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-merc; base lógica y rol propios | E1 |
| R:V-01 · Pedidos | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-venta; base lógica y rol propios | E2 |
| R:V-02 · Ventas | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-venta; base lógica y rol propios | E1 |
| R:V-03 · Comisiones | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-venta; base lógica y rol propios | E2 |
| R:V-04 · Marketplace | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-venta; base lógica y rol propios | E2 |
| R:CL-01 · Posventa | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-clientes; base lógica y rol propios | E2 |
| R:CL-02 · Clientes Retail | AKS retail / VMSS BIZ / Deployment o módulo documentado | pg-r-clientes; base lógica y rol propios | E2 |
| F:C-01 · Originación | AKS filial / VMSS BIZ / Deployment o módulo documentado | pg-f-originacion; base lógica y rol propios | E1 |
| F:C-02 · Cartera | AKS filial / VMSS BIZ / Deployment o módulo documentado | pg-f-cartera; base lógica y rol propios | E1/E2 |
| F:C-03 · Evidencia financiera | AKS filial / VMSS BIZ / Deployment o módulo documentado | pg-f-evidencia; base lógica y rol propios | E1 |
| X-01 · Control de cruces | AKS frontera / VMSS BIZ / Deployment o módulo documentado | pg-x01; base lógica y rol propios | E1 |

Comisiones y Marketplace pueden ser módulos extraíbles. Oferta mantiene su partición por decidir. F:C-04 no tiene despliegue aprobado.

# Capacidades y trabajadores

| Capacidad | Ejecución | Estado |
| --- | --- | --- |
| Adaptadores Comercio / Canales / Socios | AKS Retail / VMSS INT, réplicas distribuidas | Propuesto |
| Adaptador Crédito 2011 / firma / reportes | AKS Filial / VMSS INT | Contratos pendientes |
| Proyectores, exportación y coordinación automática | VMSS INT de su ámbito, estado durable PostgreSQL | Motor de coordinación por justificar |
| Administración, tareas humanas, documentos y notificaciones | VMSS BIZ de cada ámbito; permisos y datos propios | Productos / contratos pendientes |
| OpenSearch / OpenMetadata y backend de catálogo | VMSS STATE de cada ámbito, discos/PV propios y anti-afinidad | Versiones y tamaños pendientes |
| MLflow | VMSS STATE Retail, PostgreSQL técnico + Blob artefactos | Seleccionado, por dimensionar |
| Python / scikit-learn | VMSS R-BATCH-01..N, Jobs en AKS Retail | Pool elástico propuesto |
| Collector / Prometheus / Loki / Tempo / Grafana | VMSS OPS propio de cada ámbito, agentes locales; Blackbox en R/F-SYN-01 independiente | Configuración / persistencia / HA pendientes |
| Gateway de datos BI | R-BI-01/02 y F-BI-01/02, Windows Server 2022 | Propuesta de conexión privada HA |
| Frontend web React | Contenedores web privados por ámbito, publicados por listener de App Gateway | Alojamiento propuesto; no sustituye e-commerce sin decisión |
| Caja React y estado sin enlace | SIT-xx-R-01/02 | Mantener autoridad / diario local |
| Cupo local Filial | SIT-xx-F-01/02 o VM/hardware aislado aprobado | Factibilidad y fencing pendientes |
| Private Network Connector de Entra Private Access | R-PA-01/02 y F-PA-01/02, VM Windows Server 2022, subred administrativa propia | HA propuesta; PoC de acceso/Bastion y exclusión de terminación TLS |
| Sonda independiente Blackbox | R-SYN-01 y F-SYN-01, VM Linux fuera del AKS supervisado | Ubicación, salida, alertas y capacidad pendientes |
