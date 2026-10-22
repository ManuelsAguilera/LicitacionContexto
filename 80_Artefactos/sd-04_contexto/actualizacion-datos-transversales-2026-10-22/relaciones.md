# Contratos y sentido de los enlaces

Fuentes: registros de Datos y capas 7–8 del 22-10-2026 y figura 4.31. Las fuentes se conservan fuera del diagrama. Los rótulos son intención técnica, no certificación de ejecución.

## 4.33 · Arquitectura lógica por capas · datos y capacidades transversales

| N.º | Origen → destino | Semántica | Intención |
| :--- | :--- | :--- | :--- |
| 1 | `dns` → `front_door` | politica | Hosts de Retail y Filial; configuración DNS, sin actuar como proxy |
| 2 | `front_door` → `private_link` | condicionado | HTTPS privado por perfil y host del ámbito; endpoints separados; residencia condicionada |
| 3 | `application_gateway` → `api_management` | solicitud | HTTPS privado al APIM del mismo ámbito; políticas y contratos separados |
| 4 | `api_center` → `api_management` | politica | Contratos: API Center → pipeline externo → APIM, separados por ámbito; no tráfico de negocio |
| 5 | `web` → `front_door` | solicitud | Retail: host y perfil propios. API pública Retail |
| 6 | `portal_f` → `front_door` | solicitud | Filial: host y perfil propios. API pública Filial; borde sujeto a residencia aprobada |
| 7 | `pos` → `entrada_privada` | solicitud | Red privada tiendas / CD / DC-01 · conectividad privada corporativa; omite Front Door |
| 8 | `operacion` → `entrada_privada` | solicitud | Red privada tiendas / CD / DC-01 · conectividad privada corporativa; omite Front Door |
| 9 | `logistica` → `entrada_privada` | solicitud | Red privada tiendas / CD / DC-01 · conectividad privada corporativa; omite Front Door |
| 10 | `movil` → `entrada_privada` | solicitud | Red privada tiendas / CD / DC-01 · conectividad privada corporativa; omite Front Door |
| 11 | `meson_f` → `entrada_privada` | solicitud | Red privada del mesón financiero; omite Front Door |
| 12 | `api_management` → `area_mercaderia` | solicitud | APIs Retail del área; operaciones, contratos y permisos propios por servicio |
| 13 | `api_management` → `area_venta` | solicitud | APIs Retail del área; operaciones, contratos y permisos propios por servicio |
| 14 | `api_management` → `area_clientes` | solicitud | APIs Retail del área; operaciones, contratos y permisos propios por servicio |
| 15 | `api_management` → `servicios_e` | solicitud | APIs Filial del área; operaciones, contratos y permisos propios por servicio La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 16 | `area_venta` → `x01` | compra_autorizable | Ventas: solicitud de autorización de compra con tarjeta propia vía X-01 |
| 17 | `x01` → `api_management` | compra_autorizable | Autorización: X-01 entra SOLO al APIM de Filial con su identidad; correlativo propio |
| 18 | `bus_r` → `comercio` | consumo | Consumo de hechos propios; traducción y deduplicación |
| 19 | `bus_r` → `canales` | consumo | Consumo de hechos propios; traducción y deduplicación |
| 20 | `bus_r` → `socios` | consumo | Consumo de hechos propios; traducción y deduplicación |
| 21 | `bus_e` → `credito` | consumo | Consumo de hechos propios; traducción y deduplicación |
| 22 | `area_mercaderia` → `bus_r` | publicacion | Hechos confirmados por productores del área; outbox y contratos por servicio |
| 23 | `area_venta` → `bus_r` | publicacion | Hechos confirmados por productores del área; outbox y contratos por servicio |
| 24 | `servicios_e` → `bus_e` | publicacion | Hechos confirmados por productores del área; outbox y contratos por servicio La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 25 | `bus_r` → `area_clientes` | consumo | Clientes Retail: consumo para fila virtual; contrato por cerrar |
| 26 | `local_serv` → `local_sync` | publicacion | Entrega de operaciones para reconciliar |
| 27 | `local_sync` → `entrada_privada` | solicitud | Reenvío por red privada hacia APIs Retail; nunca escritura directa en BD |
| 28 | `area_mercaderia` → `datos_merc` | persistencia | Repositorios propios de los servicios del área; agrupación visual, no escritura compartida |
| 29 | `area_venta` → `datos_venta` | persistencia | Repositorios propios de los servicios del área; agrupación visual, no escritura compartida |
| 30 | `area_clientes` → `datos_clientes` | persistencia | Repositorios propios de los servicios del área; agrupación visual, no escritura compartida |
| 31 | `x01` → `bitacora` | persistencia | Persistencia directa propia por contexto; no pasa por el bus |
| 32 | `servicios_e` → `datos_orig` | persistencia | Solo Originación F:C-01: repositorio propio de evaluación, cupo y autorización; sin metadatos de C-03. |
| 33 | `servicios_e` → `datos_cartera` | persistencia | cartera: Persistencia directa propia por contexto; no pasa por el bus La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 34 | `servicios_e` → `datos_evid` | persistencia | evidencia: Persistencia directa propia por contexto; no pasa por el bus La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 35 | `area_mercaderia` → `redis` | persistencia | oferta: Publicación/consulta de oferta operacional; frescura por verificar |
| 36 | `area_mercaderia` → `historial` | persistencia | oferta: Registro de precios publicados; solo anexado |
| 37 | `local_serv` → `local_data` | persistencia | Diario transaccional local Retail |
| 38 | `local_data` → `local_sync` | flujo | Operaciones pendientes del diario |
| 39 | `servicios_e` → `cupo_local` | condicionado | Originación F:C-01: provisión de cupo preautorizado; límites y autorización propios de Filial; política, caducidad y factibilidad pendientes. La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 40 | `comercio` → `ext_comercio` | adaptacion | Familia de interfaces bidireccionales; contratos propios y migración por verificar |
| 41 | `canales` → `ext_canales` | adaptacion | Familia de interfaces bidireccionales; contratos propios y migración por verificar |
| 42 | `socios` → `ext_socios` | adaptacion | Familia de interfaces bidireccionales; contratos propios y migración por verificar |
| 43 | `credito` → `ext_credito` | adaptacion | Familia de interfaces bidireccionales; contratos propios y migración por verificar |
| 44 | `private_link` → `application_gateway` | condicionado | Origen Application Gateway propio de cada ámbito; sin rutas cruzadas |
| 45 | `bus_r` → `local_sync` | consumo | Cambios de oferta confirmados hacia caché local; contrato, entrega y conciliación por cerrar |
| 46 | `bus_r` → `proy_r` | consumo | Hechos confirmados del ámbito; entrega al menos una vez, orden/versiones y mensajes fallidos |
| 47 | `proy_r` → `mart_r` | persistencia | Escritura idempotente de modelos, dimensiones, indicadores y punto de aplicación |
| 48 | `bus_e` → `proy_e` | consumo | Hechos confirmados del ámbito; entrega al menos una vez, orden/versiones y mensajes fallidos |
| 49 | `proy_e` → `mart_e` | persistencia | Escritura idempotente de modelos, dimensiones, indicadores y punto de aplicación |
| 50 | `comercio` → `archivo_r` | adaptacion | Conservar copia autorizada de documentos ERP/DTE; sin asumir emisión tributaria |
| 51 | `datos_evid` → `archivo_e` | flujo | Evidencia/C-03: copia verificada, integridad y retención; no borrar por confirmación del bus |
| 52 | `area_clientes` → `bus_r` | publicacion | Hechos confirmados de Posventa/Clientes; outbox de cada servicio, sin republicar cambios de proyección |
| 53 | `common_admin` → `api_management` | solicitud | Consola del ámbito → APIM propio → APIs de parámetros y consulta/exportación de auditoría; permisos y filtros del solicitante. No escritura en repositorios ajenos. |
| 54 | `common_docs` → `archivo_r` | persistencia | Solo instancia documental Retail → contenedores propios: documentos/plantillas/evidencia de firma, acceso e integridad por clase; sin almacén compartido. |
| 55 | `bus_r` → `common_notif` | consumo | Solo instancia de notificaciones Retail: hechos autorizados y fin de exportación; plantillas/preferencias propias, al menos tres canales, reintentos y evidencia de entrega. |
| 56 | `proy_r` → `search_r` | persistencia | Proyector Retail mantiene índice global derivado con permisos por objeto/usuario, texto completo, tolerancia y facetas. No cambia autoridad de datos ni comparte índices. |
| 57 | `mart_r` → `archivo_r` | flujo | Trabajo de exportación Retail: lectura autorizada del modelo analítico al corte y archivo abierto con filtro, diccionario, auditoría, caducidad y enlace de acceso propio; no consultas BI en operacional. |
| 58 | `common_docs` → `archivo_e` | persistencia | Solo instancia documental Filial → contenedores propios: documentos/plantillas/evidencia de firma, acceso e integridad por clase; sin almacén compartido. |
| 59 | `bus_e` → `common_notif` | consumo | Solo instancia de notificaciones Filial: hechos autorizados y fin de exportación; plantillas/preferencias propias, al menos tres canales, reintentos y evidencia de entrega. |
| 60 | `proy_e` → `search_e` | persistencia | Proyector Filial mantiene índice global derivado con permisos por objeto/usuario, texto completo, tolerancia y facetas. No cambia autoridad de datos ni comparte índices. |
| 61 | `mart_e` → `archivo_e` | flujo | Trabajo de exportación Filial: lectura autorizada del modelo analítico al corte y archivo abierto con filtro, diccionario, auditoría, caducidad y enlace de acceso propio; no consultas BI en operacional. |
| 62 | `area_venta` → `local_serv` | condicionado | Ventas ejecuta operación sin enlace; solo reglas y condiciones previamente sincronizadas. |
| 63 | `entrada_privada` → `application_gateway` | solicitud | Entrada privada del ámbito → Application Gateway propio, sin Front Door público. |
| 64 | `common_docs` → `ext_comunes` | adaptacion | Instancia del ámbito → contraparte autorizada propia, contrato y proveedor pendientes; sin mezcla de datos entre ámbitos. |
| 65 | `common_notif` → `ext_comunes` | adaptacion | Instancia del ámbito → contraparte autorizada propia, contrato y proveedor pendientes; sin mezcla de datos entre ámbitos. |
| 66 | `api_management` → `common_flujos` | condicionado | Familia de APIs de tareas humanas y aprobaciones del mismo ámbito; rutas de consumidores a precisar, sin instancias compartidas. |
| 67 | `api_management` → `common_docs` | condicionado | Familia de APIs de documentos, plantillas y firma del mismo ámbito; rutas de consumidores a precisar, sin instancias compartidas. |
| 68 | `servicios_e` → `evid_meta` | persistencia | Solo C-03: expediente y metadatos propios; no datos de Originación. |
| 69 | `adf` → `lake_r` | politica | Solo factory del ámbito: coordina cargas iniciales e incrementales autorizadas, punto de corte y manifiestos; no movimiento entre negocios. |
| 70 | `proy_r` → `lake_r` | persistencia | Trabajadores propios escriben únicamente conjuntos autorizados; no duplicar todos los hechos por defecto. |
| 71 | `lake_r` → `proy_r` | flujo | Lectura y validación de conjuntos para transformar y reconstruir modelos; no dependencia del recorrido operacional inmediato. |
| 72 | `proy_r` → `metadata` | politica | Solo catálogo del ámbito: publicar ejecuciones, propietarios, calidad y linaje por API; ADLS no ofrece linaje nativo por el conector. |
| 73 | `powerbi` → `mart_r` | solicitud | Solo modelo semántico del ámbito consulta su PostgreSQL analítico mediante conexión privada de datos; DirectQuery / Import. |
| 74 | `api_management` → `search_r` | solicitud | Solo API de búsqueda del ámbito consulta OpenSearch con filtros de permisos; APIM no abre conexión directa al índice. |
| 75 | `adf` → `lake_e` | politica | Solo factory del ámbito: coordina cargas iniciales e incrementales autorizadas, punto de corte y manifiestos; no movimiento entre negocios. |
| 76 | `proy_e` → `lake_e` | persistencia | Trabajadores propios escriben únicamente conjuntos autorizados; no duplicar todos los hechos por defecto. |
| 77 | `lake_e` → `proy_e` | flujo | Lectura y validación de conjuntos para transformar y reconstruir modelos; no dependencia del recorrido operacional inmediato. |
| 78 | `proy_e` → `metadata` | politica | Solo catálogo del ámbito: publicar ejecuciones, propietarios, calidad y linaje por API; ADLS no ofrece linaje nativo por el conector. |
| 79 | `powerbi` → `mart_e` | solicitud | Solo modelo semántico del ámbito consulta su PostgreSQL analítico mediante conexión privada de datos; DirectQuery / Import. |
| 80 | `api_management` → `search_e` | solicitud | Solo API de búsqueda del ámbito consulta OpenSearch con filtros de permisos; APIM no abre conexión directa al índice. |
| 81 | `proy_r` → `vector` | persistencia | Trabajador de representaciones de Oferta: índice reconstruible; modelo de embeddings por seleccionar, no scikit-learn por defecto. |
| 82 | `area_mercaderia` → `vector` | solicitud | Solo Oferta consulta su índice multimodal y confirma precio/disponible con los propietarios. |
| 83 | `lake_r` → `training` | flujo | Conjunto Retail autorizado, versionado y con manifiesto; validación temporal y línea base. |
| 84 | `training` → `mlflow` | persistencia | Registrar experimento, parámetros, métricas y modelo con referencias a código y conjunto de datos. |
| 85 | `mlflow` → `training` | flujo | Obtener versión de modelo promovida por una persona; fallback y deriva implementados por trabajadores. |
| 86 | `training` → `area_mercaderia` | flujo | Recomendaciones de conteo a Existencias; sin ajuste automático de stock. |
| 87 | `backup` → `mart_r` | politica | Cobertura por recurso; PITR no sustituye archivo, retención legal ni pruebas de restauración. |
| 88 | `backup` → `mart_e` | politica | Cobertura y destino propios de Filial; no respaldo común. |

## 4.34 · Detalle lógico de Datos · alimentación, gobierno y modelos

| N.º | Origen → destino | Semántica | Intención |
| :--- | :--- | :--- | :--- |
| 1 | `x01` → `bitacora_x` | persistencia | Repositorio propio de X-01; no alimenta lago ni modelo analítico conjunto. |
| 2 | `services_r` → `oper_r` | persistencia | Cada servicio escribe únicamente su contexto; únicamente Retail |
| 3 | `services_r` → `bus_r` | publicacion | Publicar desde outbox durable, no desde una escritura no confirmada; únicamente Retail |
| 4 | `bus_r` → `workers_r` | consumo | Deduplicar y aplicar versiones; manejar mensajes fallidos y desorden; únicamente Retail |
| 5 | `oper_r` → `workers_r` | flujo | Exportación autorizada con corte; cargas históricas, no consultas BI; únicamente Retail |
| 6 | `adf_r` → `workers_r` | politica | Coordinar cargas y dependencias; factory y runtime con ubicación propia; únicamente Retail |
| 7 | `workers_r` → `lake_r` | persistencia | Escribir landing, validar y producir curados definidos por finalidad; únicamente Retail |
| 8 | `lake_r` → `workers_r` | flujo | Reconstrucción desde conjuntos y manifiestos; sin retención infinita de mensajes; únicamente Retail |
| 9 | `workers_r` → `mart_r` | persistencia | Mantener modelos de lectura, indicadores, punto aplicado y trazabilidad; únicamente Retail |
| 10 | `bi_r` → `mart_r` | solicitud | Consultar solo modelo analítico: DirectQuery o Import; únicamente Retail |
| 11 | `workers_r` → `search_r` | persistencia | Actualizar índice y revocar permisos con la fuente; únicamente Retail |
| 12 | `search_api_r` → `search_r` | solicitud | Consulta con autorización por documento y campo; únicamente Retail |
| 13 | `workers_r` → `metadata_r` | politica | Publicar linaje de ejecuciones y resultados durables de calidad por API; únicamente Retail |
| 14 | `metadata_r` → `metadata_pg_r` | persistencia | Persistir catálogo y configuración propia; únicamente Retail |
| 15 | `metadata_r` → `metadata_idx_r` | solicitud | Índice dedicado soportado por la versión; sin reutilizar búsqueda de negocio; únicamente Retail |
| 16 | `services_r` → `blob_r` | persistencia | Documentos bajo autoridad del servicio; C-03 verifica completitud; únicamente Retail |
| 17 | `workers_r` → `archive_r` | persistencia | Copiar, verificar y registrar evidencia/archivo por clase de retención; únicamente Retail |
| 18 | `backup_r` → `oper_r` | politica | Cobertura de respaldo por recurso y restauración probada con claves; únicamente Retail |
| 19 | `backup_r` → `mart_r` | politica | Política por recurso; respaldo no equivale a archivo legal; únicamente Retail |
| 20 | `services_e` → `oper_e` | persistencia | Cada servicio escribe únicamente su contexto; únicamente Filial |
| 21 | `services_e` → `bus_e` | publicacion | Publicar desde outbox durable, no desde una escritura no confirmada; únicamente Filial |
| 22 | `bus_e` → `workers_e` | consumo | Deduplicar y aplicar versiones; manejar mensajes fallidos y desorden; únicamente Filial |
| 23 | `oper_e` → `workers_e` | flujo | Exportación autorizada con corte; cargas históricas, no consultas BI; únicamente Filial |
| 24 | `adf_e` → `workers_e` | politica | Coordinar cargas y dependencias; factory y runtime con ubicación propia; únicamente Filial |
| 25 | `workers_e` → `lake_e` | persistencia | Escribir landing, validar y producir curados definidos por finalidad; únicamente Filial |
| 26 | `lake_e` → `workers_e` | flujo | Reconstrucción desde conjuntos y manifiestos; sin retención infinita de mensajes; únicamente Filial |
| 27 | `workers_e` → `mart_e` | persistencia | Mantener modelos de lectura, indicadores, punto aplicado y trazabilidad; únicamente Filial |
| 28 | `bi_e` → `mart_e` | solicitud | Consultar solo modelo analítico: DirectQuery o Import; únicamente Filial |
| 29 | `workers_e` → `search_e` | persistencia | Actualizar índice y revocar permisos con la fuente; únicamente Filial |
| 30 | `search_api_e` → `search_e` | solicitud | Consulta con autorización por documento y campo; únicamente Filial |
| 31 | `workers_e` → `metadata_e` | politica | Publicar linaje de ejecuciones y resultados durables de calidad por API; únicamente Filial |
| 32 | `metadata_e` → `metadata_pg_e` | persistencia | Persistir catálogo y configuración propia; únicamente Filial |
| 33 | `metadata_e` → `metadata_idx_e` | solicitud | Índice dedicado soportado por la versión; sin reutilizar búsqueda de negocio; únicamente Filial |
| 34 | `services_e` → `blob_e` | persistencia | Documentos bajo autoridad del servicio; C-03 verifica completitud; únicamente Filial |
| 35 | `workers_e` → `archive_e` | persistencia | Copiar, verificar y registrar evidencia/archivo por clase de retención; únicamente Filial |
| 36 | `backup_e` → `oper_e` | politica | Cobertura de respaldo por recurso y restauración probada con claves; únicamente Filial |
| 37 | `backup_e` → `mart_e` | politica | Política por recurso; respaldo no equivale a archivo legal; únicamente Filial |
| 38 | `services_r` → `embeddings` | flujo | Solo Oferta e imágenes autorizadas |
| 39 | `embeddings` → `vector` | persistencia | Representaciones y versión del modelo; reconstrucción |
| 40 | `services_r` → `vector` | solicitud | Solo Oferta consulta; confirma precio y disponible con su autoridad |
| 41 | `lake_r` → `training` | flujo | Conjunto autorizado versionado y manifiesto de Retail |
| 42 | `training` → `mlflow` | persistencia | Registrar código, parámetros, métricas, modelo y referencia al conjunto |
| 43 | `mlflow` → `mlflow_pg` | persistencia | Metadatos propios de MLflow |
| 44 | `mlflow` → `mlflow_blob` | persistencia | Artefactos versionados; distintos de conjuntos de entrenamiento |
| 45 | `mlflow` → `training` | flujo | Modelo promovido con aprobación humana; deriva y fallback en trabajadores |
| 46 | `training` → `recommendations` | flujo | Inferencia controlada; sin ajuste automático de stock |

## 4.35 · Capas transversales · Seguridad y Observabilidad por ámbito

| N.º | Origen → destino | Semántica | Intención |
| :--- | :--- | :--- | :--- |
| 1 | `source_r` → `entra_r` | politica | Autenticación interna; JWT se valida localmente, no consulta por cada solicitud; solo Retail |
| 2 | `source_r` → `external_r` | politica | Autenticación de clientes o titulares con emisor propio; solo Retail |
| 3 | `intune_r` → `admin_r` | politica | Administrar solo equipos compatibles; revocación sin enlace no inmediata; solo Retail |
| 4 | `source_r` → `workload_r` | politica | Tokens de cargas/pods/pipelines con permisos por recurso; solo Retail |
| 5 | `source_r` → `kv_r` | solicitud | Lectura autorizada de secretos y certificados; solo Retail |
| 6 | `source_r` → `hsm_r` | solicitud | Operaciones criptográficas / envoltura DEK por propietario; solo Retail |
| 7 | `admin_r` → `entra_r` | politica | Identidad y MFA de administradores; solo Retail |
| 8 | `pim_r` → `admin_r` | politica | Autorizar elevación temporal; PIM no transporta sesiones; solo Retail |
| 9 | `admin_r` → `private_r` | solicitud | Acceso remoto autorizado por identidad, aplicación y recurso; solo Retail |
| 10 | `private_r` → `resources_r` | solicitud | Ruta autorizada a recursos privados; no sustituye VPN corporativa; solo Retail |
| 11 | `admin_r` → `bastion_r` | solicitud | Sesión administrativa autorizada para máquinas compatibles; solo Retail |
| 12 | `bastion_r` → `resources_r` | solicitud | Salto administrativo a máquinas compatibles; no todas las APIs; solo Retail |
| 13 | `endpoint_r` → `admin_r` | politica | Protección y detección de equipos con agente soportado; solo Retail |
| 14 | `cloud_r` → `platform_r` | politica | Planes y cobertura de cargas declarados; solo Retail |
| 15 | `entra_r` → `sentinel_r` | publicacion | Eventos de identidad por conectores soportados; solo Retail |
| 16 | `endpoint_r` → `sentinel_r` | publicacion | Detecciones seleccionadas; solo Retail |
| 17 | `cloud_r` → `sentinel_r` | publicacion | Detecciones de cargas seleccionadas; solo Retail |
| 18 | `kv_r` → `sentinel_r` | publicacion | Diagnóstico de acceso y operación de claves/secretos; solo Retail |
| 19 | `hsm_r` → `sentinel_r` | publicacion | Auditoría criptográfica soportada; solo Retail |
| 20 | `sentinel_r` → `soc_r` | flujo | Incidentes y correlación con permisos del equipo; solo Retail |
| 21 | `bastion_r` → `stage_r` | persistencia | Destino inicial de grabación mutable, sin política WORM ni versionado; solo Retail |
| 22 | `stage_r` → `audit_r` | flujo | Procesar grabación y verificar copia antes de cerrar retención; solo Retail |
| 23 | `source_r` → `audit_r` | publicacion | Auditoría de negocio durable, distinta de logs muestreados; solo Retail |
| 24 | `audit_r` → `worm_r` | persistencia | Copia verificada, manifiesto e integridad bajo retención propia; solo Retail |
| 25 | `source_r` → `otel_r` | publicacion | Telemetría saneada; RUM público mediante ingreso de borde/gateway autorizado; solo Retail |
| 26 | `local_r` → `otel_r` | publicacion | Drenar cola local tras reconexión por red privada autorizada; solo Retail |
| 27 | `platform_r` → `local_r` | publicacion | Solo componentes locales y heartbeat; diferenciar no observable de fallo confirmado; solo Retail |
| 28 | `otel_r` → `loki_r` | publicacion | Registros mediante OTLP HTTP autenticado; solo Retail |
| 29 | `otel_r` → `tempo_r` | publicacion | Trazas mediante OTLP soportado; solo Retail |
| 30 | `otel_r` → `prom_r` | publicacion | Métricas mediante receptor OTLP HTTP habilitado y protegido; solo Retail |
| 31 | `prom_r` → `platform_r` | solicitud | Scrape de métricas/endpoints/exportadores y registro DORA; evitar doble serie; solo Retail |
| 32 | `platform_r` → `monitor_r` | publicacion | Diagnósticos Azure soportados y fuentes necesarias para seguridad; solo Retail |
| 33 | `grafana_r` → `prom_r` | solicitud | Consultar métricas y SLO con credenciales de lectura; solo Retail |
| 34 | `grafana_r` → `loki_r` | solicitud | Consultar registros operacionales autorizados; solo Retail |
| 35 | `grafana_r` → `tempo_r` | solicitud | Consultar trazas autorizadas; solo Retail |
| 36 | `grafana_r` → `monitor_r` | solicitud | Consultar diagnóstico Azure con autenticación soportada; solo Retail |
| 37 | `grafana_r` → `noc_r` | flujo | Alerting integrado: avisos, agrupación y escalamiento sin payloads sensibles; solo Retail |
| 38 | `blackbox_r` → `platform_r` | solicitud | Probar DNS/TLS/URL segura pública y salud privada desde ubicaciones independientes; solo Retail |
| 39 | `prom_r` → `blackbox_r` | solicitud | Recoger resultados de sondas de endpoints; solo Retail |
| 40 | `blackbox_r` → `noc_r` | flujo | Observador independiente y ruta de aviso sobreviven a la falla monitorizada; solo Retail |
| 41 | `source_e` → `entra_e` | politica | Autenticación interna; JWT se valida localmente, no consulta por cada solicitud; solo Filial |
| 42 | `source_e` → `external_e` | politica | Autenticación de clientes o titulares con emisor propio; solo Filial |
| 43 | `intune_e` → `admin_e` | politica | Administrar solo equipos compatibles; revocación sin enlace no inmediata; solo Filial |
| 44 | `source_e` → `workload_e` | politica | Tokens de cargas/pods/pipelines con permisos por recurso; solo Filial |
| 45 | `source_e` → `kv_e` | solicitud | Lectura autorizada de secretos y certificados; solo Filial |
| 46 | `source_e` → `hsm_e` | solicitud | Operaciones criptográficas / envoltura DEK por propietario; solo Filial |
| 47 | `admin_e` → `entra_e` | politica | Identidad y MFA de administradores; solo Filial |
| 48 | `pim_e` → `admin_e` | politica | Autorizar elevación temporal; PIM no transporta sesiones; solo Filial |
| 49 | `admin_e` → `private_e` | solicitud | Acceso remoto autorizado por identidad, aplicación y recurso; solo Filial |
| 50 | `private_e` → `resources_e` | solicitud | Ruta autorizada a recursos privados; no sustituye VPN corporativa; solo Filial |
| 51 | `admin_e` → `bastion_e` | solicitud | Sesión administrativa autorizada para máquinas compatibles; solo Filial |
| 52 | `bastion_e` → `resources_e` | solicitud | Salto administrativo a máquinas compatibles; no todas las APIs; solo Filial |
| 53 | `endpoint_e` → `admin_e` | politica | Protección y detección de equipos con agente soportado; solo Filial |
| 54 | `cloud_e` → `platform_e` | politica | Planes y cobertura de cargas declarados; solo Filial |
| 55 | `entra_e` → `sentinel_e` | publicacion | Eventos de identidad por conectores soportados; solo Filial |
| 56 | `endpoint_e` → `sentinel_e` | publicacion | Detecciones seleccionadas; solo Filial |
| 57 | `cloud_e` → `sentinel_e` | publicacion | Detecciones de cargas seleccionadas; solo Filial |
| 58 | `kv_e` → `sentinel_e` | publicacion | Diagnóstico de acceso y operación de claves/secretos; solo Filial |
| 59 | `hsm_e` → `sentinel_e` | publicacion | Auditoría criptográfica soportada; solo Filial |
| 60 | `sentinel_e` → `soc_e` | flujo | Incidentes y correlación con permisos del equipo; solo Filial |
| 61 | `bastion_e` → `stage_e` | persistencia | Destino inicial de grabación mutable, sin política WORM ni versionado; solo Filial |
| 62 | `stage_e` → `audit_e` | flujo | Procesar grabación y verificar copia antes de cerrar retención; solo Filial |
| 63 | `source_e` → `audit_e` | publicacion | Auditoría de negocio durable, distinta de logs muestreados; solo Filial |
| 64 | `audit_e` → `worm_e` | persistencia | Copia verificada, manifiesto e integridad bajo retención propia; solo Filial |
| 65 | `source_e` → `otel_e` | publicacion | Telemetría saneada; RUM público mediante ingreso de borde/gateway autorizado; solo Filial |
| 66 | `local_e` → `otel_e` | publicacion | Drenar cola local tras reconexión por red privada autorizada; solo Filial |
| 67 | `platform_e` → `local_e` | publicacion | Solo componentes locales y heartbeat; diferenciar no observable de fallo confirmado; solo Filial |
| 68 | `otel_e` → `loki_e` | publicacion | Registros mediante OTLP HTTP autenticado; solo Filial |
| 69 | `otel_e` → `tempo_e` | publicacion | Trazas mediante OTLP soportado; solo Filial |
| 70 | `otel_e` → `prom_e` | publicacion | Métricas mediante receptor OTLP HTTP habilitado y protegido; solo Filial |
| 71 | `prom_e` → `platform_e` | solicitud | Scrape de métricas/endpoints/exportadores y registro DORA; evitar doble serie; solo Filial |
| 72 | `platform_e` → `monitor_e` | publicacion | Diagnósticos Azure soportados y fuentes necesarias para seguridad; solo Filial |
| 73 | `grafana_e` → `prom_e` | solicitud | Consultar métricas y SLO con credenciales de lectura; solo Filial |
| 74 | `grafana_e` → `loki_e` | solicitud | Consultar registros operacionales autorizados; solo Filial |
| 75 | `grafana_e` → `tempo_e` | solicitud | Consultar trazas autorizadas; solo Filial |
| 76 | `grafana_e` → `monitor_e` | solicitud | Consultar diagnóstico Azure con autenticación soportada; solo Filial |
| 77 | `grafana_e` → `noc_e` | flujo | Alerting integrado: avisos, agrupación y escalamiento sin payloads sensibles; solo Filial |
| 78 | `blackbox_e` → `platform_e` | solicitud | Probar DNS/TLS/URL segura pública y salud privada desde ubicaciones independientes; solo Filial |
| 79 | `prom_e` → `blackbox_e` | solicitud | Recoger resultados de sondas de endpoints; solo Filial |
| 80 | `blackbox_e` → `noc_e` | flujo | Observador independiente y ruta de aviso sobreviven a la falla monitorizada; solo Filial |
| 81 | `x01` → `audit_r` | publicacion | Solo extremo Retail del contrato X-01: auditoría/telemetría propia y correlación mínima autorizada, sin payload ajeno ni colector común. |
| 82 | `x01` → `otel_r` | publicacion | Solo extremo Retail del contrato X-01: auditoría/telemetría propia y correlación mínima autorizada, sin payload ajeno ni colector común. |
| 83 | `x01` → `audit_e` | publicacion | Solo extremo Filial del contrato X-01: auditoría/telemetría propia y correlación mínima autorizada, sin payload ajeno ni colector común. |
| 84 | `x01` → `otel_e` | publicacion | Solo extremo Filial del contrato X-01: auditoría/telemetría propia y correlación mínima autorizada, sin payload ajeno ni colector común. |

## Identidad de cargas · relaciones adicionales de 4.35

| Origen → destino | Semántica | Intención |
| :--- | :--- | :--- |
| `workload_r` → `platform_r` | politica | Tokens para recursos Azure compatibles Retail; permisos mínimos por recurso. |
| `workload_e` → `platform_e` | politica | Tokens para recursos Azure compatibles Filial; permisos mínimos por recurso. |

Uso de IA: Alto.
