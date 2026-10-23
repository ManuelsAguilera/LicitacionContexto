# Relaciones y evidencia

Las fuentes están fuera del diagrama y no se escriben en las flechas. El registro explica la intención de cada familia; ninguna ruta propuesta acredita configuración desplegada.

| Familia | Relación | Evidencia de diseño | Límite |
|---|---|---|---|
| publico | Canales públicos / FD / Private Link / AppGW | Registro D-11, D-13, D-18; figura 4.30; SD-04 §4.2 red de sitios | Decisiones anteriores; Private Link y AppGW conservados |
| privado | Canales internos / acceso privado / AppGW | SD-04 §4.2 (rutas de tiendas/DC y ExpressRoute propuesto); instrucción del usuario de pasar por Borde | Vista lógica de conectividad privada; no un circuito por canal |
| entrada | Gateway / APIM / contratos de área | Adjunto §4.1; registro D-18; SD-04 §4.1 | APIM valida entrada; permisos de negocio en el servicio |
| x01 | Cruce y bitácora | Adjunto §3.5; nomenclatura SD-03; D-17/D-29 | Solo autorización mínima y contratos aprobados |
| evento | Outbox / bus / adaptadores / proyecciones | Figura 4.30 y análisis horizontal; D-33; adjunto §4.1/5.5 | Service Bus del ámbito; al menos una vez; índice derivado |
| dato | Repositorio propietario y caches | Adjunto §3 fichas y §4.1; SD-04 Tabla 4.2 | Autoridad por servicio; área no equivale a base compartida |
| comun | APIs y capacidades comunes | Adjunto §5.1–5.6 y decisiones 7.1–7.7 | Propuestas, rutas concretas por validar; sin nuevo alcance aprobado |
| documento | Documentos / firma / archivo / contraparte | Adjunto §5.3; RT-16.15–19 de Bases | Cada servicio conserva dueño; prestador pendiente |
| aviso | Bus / notificaciones / contraparte | Adjunto §5.4; RT-16.20–26 de Bases | Instancias, plantillas y preferencias propias |
| busqueda | Proyector / índice global / API | Adjunto §5.5; RT-16.27 de Bases | No confundir consulta API con conexión SQL del gateway |
| exportacion | Modelo analítico / archivo / aviso | Adjunto §4.4/5.5 + decisión explícita previa sin Lake | Patrón asíncrono; autorización/filtro/corte; incluir datos fuera del mart para exportación completa |
| continuidad | Venta sin enlace / diario / sincronización / cupo | Adjunto §3.2 R:V-02 y §3.4 F:C-01; SD-03 SP-03; SD-04 continuidad | No acceso directo desde el canal a la base; cupo condicionado |
| externo | Adaptadores y plataformas conservadas | Adjunto §3 fichas; SD-03 exclusiones; D-30 | Familias de contratos, no inventario verificado de 14 enlaces |
| observabilidad | OTEL / Monitor / métricas | Registro D-47–D-53; adjunto §4.1; figura 4.30 | Política transversal por ámbito; exportadores y compatibilidad pendientes |


## Inventario de conexiones

| N.º | Origen | Destino | Familia | Intención |
|---|---|---|---|---|
| 1 | dns | front_door | entrada | Hosts de Retail y Filial; configuración DNS, sin actuar como proxy |
| 2 | front_door | private_link | publico | HTTPS privado por perfil y host del ámbito; endpoints separados; residencia condicionada |
| 3 | application_gateway | api_management | entrada | HTTPS privado al APIM del mismo ámbito; políticas y contratos separados |
| 4 | api_center | api_management | entrada | Contratos: API Center → pipeline externo → APIM, separados por ámbito; no tráfico de negocio |
| 5 | web | front_door | publico | Retail: host y perfil propios. API pública Retail |
| 6 | portal_f | front_door | publico | Filial: host y perfil propios. API pública Filial; borde sujeto a residencia aprobada |
| 7 | pos | entrada_privada | privado | Red privada tiendas / CD / DC-01 · conectividad privada corporativa; omite Front Door |
| 8 | operacion | entrada_privada | privado | Red privada tiendas / CD / DC-01 · conectividad privada corporativa; omite Front Door |
| 9 | logistica | entrada_privada | privado | Red privada tiendas / CD / DC-01 · conectividad privada corporativa; omite Front Door |
| 10 | movil | entrada_privada | privado | Red privada tiendas / CD / DC-01 · conectividad privada corporativa; omite Front Door |
| 11 | meson_f | entrada_privada | privado | Red privada del mesón financiero; omite Front Door |
| 12 | api_management | area_mercaderia | entrada | APIs Retail del área; operaciones, contratos y permisos propios por servicio |
| 13 | api_management | area_venta | entrada | APIs Retail del área; operaciones, contratos y permisos propios por servicio |
| 14 | api_management | area_clientes | entrada | APIs Retail del área; operaciones, contratos y permisos propios por servicio |
| 15 | api_management | servicios_e | entrada | APIs Filial del área; operaciones, contratos y permisos propios por servicio La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 16 | area_venta | x01 | x01 | Ventas: solicitud de autorización de compra con tarjeta propia vía X-01 |
| 17 | x01 | api_management | x01 | Autorización: X-01 entra SOLO al APIM de Filial con su identidad; correlativo propio |
| 18 | bus_r | comercio | evento | Consumo de hechos propios; traducción y deduplicación |
| 19 | bus_r | canales | evento | Consumo de hechos propios; traducción y deduplicación |
| 20 | bus_r | socios | evento | Consumo de hechos propios; traducción y deduplicación |
| 21 | bus_e | credito | evento | Consumo de hechos propios; traducción y deduplicación |
| 22 | area_mercaderia | bus_r | evento | Hechos confirmados por productores del área; outbox y contratos por servicio |
| 23 | area_venta | bus_r | evento | Hechos confirmados por productores del área; outbox y contratos por servicio |
| 24 | servicios_e | bus_e | evento | Hechos confirmados por productores del área; outbox y contratos por servicio La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 25 | bus_r | area_clientes | evento | Clientes Retail: consumo para fila virtual; contrato por cerrar |
| 26 | local_serv | local_sync | continuidad | Entrega de operaciones para reconciliar |
| 27 | local_sync | entrada_privada | continuidad | Reenvío por red privada hacia APIs Retail; nunca escritura directa en BD |
| 28 | area_mercaderia | datos_merc | dato | Repositorios propios de los servicios del área; agrupación visual, no escritura compartida |
| 29 | area_venta | datos_venta | dato | Repositorios propios de los servicios del área; agrupación visual, no escritura compartida |
| 30 | area_clientes | datos_clientes | dato | Repositorios propios de los servicios del área; agrupación visual, no escritura compartida |
| 31 | x01 | bitacora | x01 | Persistencia directa propia por contexto; no pasa por el bus |
| 32 | servicios_e | datos_orig | dato | originacion: Persistencia directa propia por contexto; no pasa por el bus La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 33 | servicios_e | datos_cartera | dato | cartera: Persistencia directa propia por contexto; no pasa por el bus La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 34 | servicios_e | datos_evid | dato | evidencia: Persistencia directa propia por contexto; no pasa por el bus La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 35 | area_mercaderia | redis | dato | oferta: Publicación/consulta de oferta operacional; frescura por verificar |
| 36 | area_mercaderia | historial | dato | oferta: Registro de precios publicados; solo anexado |
| 37 | local_serv | local_data | continuidad | Diario transaccional local Retail |
| 38 | local_data | local_sync | continuidad | Operaciones pendientes del diario |
| 39 | servicios_e | cupo_local | continuidad | Originación F:C-01: provisión de cupo preautorizado; límites y autorización propios de Filial; política, caducidad y factibilidad pendientes. La familia no incorpora al candidato de Control regulatorio hasta que se aprueben sus contratos. |
| 40 | comercio | ext_comercio | externo | Familia de interfaces bidireccionales; contratos propios y migración por verificar |
| 41 | canales | ext_canales | externo | Familia de interfaces bidireccionales; contratos propios y migración por verificar |
| 42 | socios | ext_socios | externo | Familia de interfaces bidireccionales; contratos propios y migración por verificar |
| 43 | credito | ext_credito | externo | Familia de interfaces bidireccionales; contratos propios y migración por verificar |
| 44 | otel | monitor | observabilidad | OTLP por colector del ámbito; exportador pendiente |
| 45 | monitor | grafana | observabilidad | Consulta de métricas y salud por ámbito; agregación entre tenants pendiente |
| 46 | private_link | application_gateway | publico | Origen Application Gateway propio de cada ámbito; sin rutas cruzadas |
| 47 | bus_r | local_sync | continuidad | Cambios de oferta confirmados hacia caché local; contrato, entrega y conciliación por cerrar |
| 48 | bus_r | proy_r | evento | Hechos confirmados del ámbito; entrega al menos una vez, orden/versiones y mensajes fallidos |
| 49 | proy_r | mart_r | evento | Escritura idempotente de modelos, dimensiones, indicadores y punto de aplicación |
| 50 | mart_r | powerbi | dato | Lectura analítica Retail por conexión privada de datos; modelos y permisos propios |
| 51 | bus_e | proy_e | evento | Hechos confirmados del ámbito; entrega al menos una vez, orden/versiones y mensajes fallidos |
| 52 | proy_e | mart_e | evento | Escritura idempotente de modelos, dimensiones, indicadores y punto de aplicación |
| 53 | mart_e | powerbi | dato | Lectura analítica Filial por conexión privada de datos; modelos y permisos propios |
| 54 | area_mercaderia | vector | dato | Oferta/Búsqueda: actualizar y consultar el índice derivado; Existencias confirma disponible |
| 55 | proy_r | archivo_r | evento | Exportar conjuntos de entrenamiento versionados y manifiestos; contenedor Retail propio |
| 56 | archivo_r | area_mercaderia | dato | Existencias: lectura del conjunto autorizado para conteo predictivo; Oferta: imágenes autorizadas |
| 57 | comercio | archivo_r | dato | Conservar copia autorizada de documentos ERP/DTE; sin asumir emisión tributaria |
| 58 | datos_evid | archivo_e | dato | Evidencia/C-03: copia verificada, integridad y retención; no borrar por confirmación del bus |
| 59 | area_clientes | bus_r | evento | Hechos confirmados de Posventa/Clientes; outbox de cada servicio, sin republicar cambios de proyección |
| 60 | common_admin | api_management | comun | Consola del ámbito → APIM propio → APIs de parámetros y consulta/exportación de auditoría; permisos y filtros del solicitante. No escritura en repositorios ajenos. |
| 61 | common_docs | archivo_r | documento | Solo instancia documental Retail → contenedores propios: documentos/plantillas/evidencia de firma, acceso e integridad por clase; sin almacén compartido. |
| 62 | bus_r | common_notif | aviso | Solo instancia de notificaciones Retail: hechos autorizados y fin de exportación; plantillas/preferencias propias, al menos tres canales, reintentos y evidencia de entrega. |
| 63 | proy_r | search_r | busqueda | Proyector Retail mantiene índice global derivado con permisos por objeto/usuario, texto completo, tolerancia y facetas. No cambia autoridad de datos ni comparte índices. |
| 64 | api_management | search_r | busqueda | API de consulta de búsqueda del propio ámbito; filtros de permiso en la capacidad, sin acceso directo del cliente al índice. |
| 65 | mart_r | archivo_r | exportacion | Trabajo de exportación Retail: lectura autorizada del modelo analítico al corte y archivo abierto con filtro, diccionario, auditoría, caducidad y enlace de acceso propio; no consultas BI en operacional. |
| 66 | common_docs | archivo_e | documento | Solo instancia documental Filial → contenedores propios: documentos/plantillas/evidencia de firma, acceso e integridad por clase; sin almacén compartido. |
| 67 | bus_e | common_notif | aviso | Solo instancia de notificaciones Filial: hechos autorizados y fin de exportación; plantillas/preferencias propias, al menos tres canales, reintentos y evidencia de entrega. |
| 68 | proy_e | search_e | busqueda | Proyector Filial mantiene índice global derivado con permisos por objeto/usuario, texto completo, tolerancia y facetas. No cambia autoridad de datos ni comparte índices. |
| 69 | api_management | search_e | busqueda | API de consulta de búsqueda del propio ámbito; filtros de permiso en la capacidad, sin acceso directo del cliente al índice. |
| 70 | mart_e | archivo_e | exportacion | Trabajo de exportación Filial: lectura autorizada del modelo analítico al corte y archivo abierto con filtro, diccionario, auditoría, caducidad y enlace de acceso propio; no consultas BI en operacional. |
| 71 | area_venta | local_serv | continuidad | Ventas ejecuta operación sin enlace; solo reglas y condiciones previamente sincronizadas. |
| 72 | entrada_privada | application_gateway | privado | Entrada privada del ámbito → Application Gateway propio, sin Front Door público. |
| 73 | common_docs | ext_comunes | documento | Instancia del ámbito → contraparte autorizada propia, contrato y proveedor pendientes; sin mezcla de datos entre ámbitos. |
| 74 | common_notif | ext_comunes | aviso | Instancia del ámbito → contraparte autorizada propia, contrato y proveedor pendientes; sin mezcla de datos entre ámbitos. |
| 75 | api_management | common_flujos | comun | Familia de APIs de tareas humanas y aprobaciones del mismo ámbito; rutas de consumidores a precisar, sin instancias compartidas. |
| 76 | api_management | common_docs | documento | Familia de APIs de documentos, plantillas y firma del mismo ámbito; rutas de consumidores a precisar, sin instancias compartidas. |
