# Matriz de componentes

76 componentes de la vista y 8 decisiones de retiro, traslado o representación. Ninguna fila acredita despliegue ni aprobación humana. Productor/consumidor puede expresar dependencia de datos, tecnología o gobierno: no siempre es emisor/receptor de un mensaje.

Los contratos al contorno de áreas se descomponen por autoridad de cada servicio; no conceden a todos los servicios escritura en todas las bases. Las capacidades de innovación heredan su dueño. Las bandas de Seguridad/Observabilidad declaran dependencias transversales. Servicios comunes es la única caja intencionalmente sin consumidores; el resto tiene una función o relación explícita, agrupada o pendiente identificada.

## Portal y app de la tienda · React / React Native

ID: `web`

| Campo | Definición |
|---|---|
| Responsabilidad | Canal público de comercio Retail; solicita contratos comerciales propios |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | front_door |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | web → front_door: solicitud |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Caja y mesón · React web servido desde tienda

ID: `pos`

| Campo | Definición |
|---|---|
| Responsabilidad | Venta asistida y mesón Retail; inicia venta e ingreso al modo sin enlace |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | application_gateway; local_serv |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | pos → application_gateway: solicitud; pos → local_serv: solicitud |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## App interna de tienda · 4 perfiles · RN / SQLite / DataWedge · QR + PIN en vista previa

ID: `operacion`

| Campo | Definición |
|---|---|
| Responsabilidad | Operación interna móvil por perfiles; inventario y reposición |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | application_gateway |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | operacion → application_gateway: solicitud |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Vista logística · WMS del CD conservado

ID: `logistica`

| Campo | Definición |
|---|---|
| Responsabilidad | Vista operativa del WMS conservado; no se reemplaza su plataforma |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | application_gateway |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | logistica → application_gateway: solicitud |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Consola comercial y de atención

ID: `movil`

| Campo | Definición |
|---|---|
| Responsabilidad | Atención, comercial y planificación Retail con permisos propios |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | application_gateway |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | movil → application_gateway: solicitud |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Portal y app de la tarjeta · Código propio · simulador CAE

ID: `portal_f`

| Campo | Definición |
|---|---|
| Responsabilidad | Canal propio de tarjeta con sesión y datos de Filial |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | front_door |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | portal_f → front_door: solicitud |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Mesón financiero · Sesión y permisos de la Filial

ID: `meson_f`

| Campo | Definición |
|---|---|
| Responsabilidad | Atención financiera por red y permisos de Filial |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | application_gateway; cupo_local |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | meson_f → application_gateway: solicitud; meson_f → cupo_local: condicionado |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure DNS · Zonas y registros por ámbito

ID: `dns`

| Campo | Definición |
|---|---|
| Responsabilidad | Resolución de hosts por ámbito; no proxy ni tráfico de negocio |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | front_door |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | dns → front_door: politica |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure Kubernetes Service · Ejecución aislada por ámbito · Premium / LTS por acreditar

ID: `aks_r`

| Campo | Definición |
|---|---|
| Responsabilidad | Tecnología de ejecución de APIs, adaptadores y proyectores aislados por ámbito |
| Productor | Pipeline de despliegue por ámbito |
| Consumidor | APIs, adaptadores y proyectores propios |
| Datos | Artefactos y configuración; no autoridad de datos |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Oferta comercial

ID: `oferta` · R:M-01

| Campo | Definición |
|---|---|
| Responsabilidad | Autoridad de oferta/precios; aloja búsqueda y Retail Media |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Mercadería; api_management → area_mercaderia; area_mercaderia → bus_r; area_mercaderia → datos_merc; area_mercaderia → redis; area_mercaderia → historial; area_mercaderia → vector; archivo_r → area_mercaderia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Abastecimiento

ID: `abastecimiento` · R:M-02

| Campo | Definición |
|---|---|
| Responsabilidad | Gestiona abastecimiento y contratos de suministro |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Mercadería; api_management → area_mercaderia; area_mercaderia → bus_r; area_mercaderia → datos_merc; area_mercaderia → redis; area_mercaderia → historial; area_mercaderia → vector; archivo_r → area_mercaderia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Existencias · sugerencias de IA

ID: `existencias` · R:M-03

| Campo | Definición |
|---|---|
| Responsabilidad | Autoridad de disponibilidad y movimientos; aloja conteo predictivo |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Mercadería; api_management → area_mercaderia; area_mercaderia → bus_r; area_mercaderia → datos_merc; area_mercaderia → redis; area_mercaderia → historial; area_mercaderia → vector; archivo_r → area_mercaderia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Pedidos

ID: `pedidos` · R:V-01

| Campo | Definición |
|---|---|
| Responsabilidad | Estado y cumplimiento del pedido; aloja integración de lockers |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Venta; api_management → area_venta; area_venta → x01; area_venta → bus_r; area_venta → datos_venta |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Ventas

ID: `ventas` · R:V-02

| Campo | Definición |
|---|---|
| Responsabilidad | Registra venta y su conciliación; solicita autorización vía X-01 |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Venta; api_management → area_venta; area_venta → x01; area_venta → bus_r; area_venta → datos_venta |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Comisiones

ID: `comisiones` · R:V-03

| Campo | Definición |
|---|---|
| Responsabilidad | Calcula y concilia comisiones propias con trazabilidad |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Venta; api_management → area_venta; area_venta → x01; area_venta → bus_r; area_venta → datos_venta |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Marketplace

ID: `market` · R:V-04

| Campo | Definición |
|---|---|
| Responsabilidad | Gobierna relación comercial con marketplace conservado |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Venta; api_management → area_venta; area_venta → x01; area_venta → bus_r; area_venta → datos_venta |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Posventa

ID: `posventa` · R:CL-01

| Campo | Definición |
|---|---|
| Responsabilidad | Recepción, inspección y coordinación de devoluciones |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Relación con el cliente; api_management → area_clientes; bus_r → area_clientes; area_clientes → datos_clientes; area_clientes → bus_r |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Clientes Retail

ID: `clientes` · R:CL-02

| Campo | Definición |
|---|---|
| Responsabilidad | Datos y atención de cliente Retail; aloja Modo Tienda/fila |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Relación con el cliente; api_management → area_clientes; bus_r → area_clientes; area_clientes → datos_clientes; area_clientes → bus_r |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Originación de crédito

ID: `originacion` · F:C-01

| Campo | Definición |
|---|---|
| Responsabilidad | Solicitud, evaluación y formalización del crédito |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Crédito Filial; api_management → servicios_e; servicios_e → bus_e; servicios_e → datos_orig; servicios_e → datos_cartera; servicios_e → datos_evid; servicios_e → cupo_local |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Cartera de crédito

ID: `cartera` · F:C-02

| Campo | Definición |
|---|---|
| Responsabilidad | Autoridad de saldos/estado financiero y proceso de cartera |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Crédito Filial; api_management → servicios_e; servicios_e → bus_e; servicios_e → datos_orig; servicios_e → datos_cartera; servicios_e → datos_evid; servicios_e → cupo_local |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Evidencia y consentimiento

ID: `evidencia` · F:C-03

| Campo | Definición |
|---|---|
| Responsabilidad | Autoridad de consentimiento, firma, metadatos y evidencia |
| Productor | APIM del ámbito y productores autorizados por contrato |
| Consumidor | Contratos del área, limitados al servicio propietario |
| Datos | Estado y repositorio propios; outbox de hechos confirmados; no escritura entre servicios |
| Interfaces | Familia del área Crédito Filial; api_management → servicios_e; servicios_e → bus_e; servicios_e → datos_orig; servicios_e → datos_cartera; servicios_e → datos_evid; servicios_e → cupo_local |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Control de cruces

ID: `x01` · X-01

| Campo | Definición |
|---|---|
| Responsabilidad | Autoriza cruce mínimo por contrato y registra bitácora; no base financiera compartida |
| Productor | area_venta |
| Consumidor | api_management; bitacora |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | area_venta → x01: compra_autorizable; x01 → api_management: compra_autorizable; x01 → bitacora: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Conteo cíclico predictivo · Existencias · proceso

ID: `conteo`

| Campo | Definición |
|---|---|
| Responsabilidad | Prioriza conteos usando conjuntos autorizados; control independiente sin ajuste automático |
| Productor | Existencias y sus datos autorizados |
| Consumidor | Existencias y canales propios |
| Datos | Datos Retail mínimos; conjuntos versionados y control temporal |
| Interfaces | Capacidad interna del servicio responsable, no microservicio añadido; ver análisis de innovaciones |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Lockers Ancoa 24/7 · Pedidos · producto

ID: `lockers`

| Campo | Definición |
|---|---|
| Responsabilidad | Entrega y retiro bajo responsabilidad Pedidos; contraparte por precisar |
| Productor | Pedidos y sus datos autorizados |
| Consumidor | Pedidos y canales propios |
| Datos | Datos Retail mínimos; contrato específico pendiente de validar |
| Interfaces | Capacidad interna del servicio responsable, no microservicio añadido; ver análisis de innovaciones |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Búsqueda vectorial multimodal · Oferta · tecnología

ID: `busqueda`

| Campo | Definición |
|---|---|
| Responsabilidad | Índice derivado multimodal del catálogo; verifica disponibilidad con Existencias |
| Productor | Oferta y sus datos autorizados |
| Consumidor | Oferta y canales propios |
| Datos | Datos Retail mínimos; contrato específico pendiente de validar |
| Interfaces | Capacidad interna del servicio responsable, no microservicio añadido; ver análisis de innovaciones |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Retail Media Network · Oferta · modelo de negocio

ID: `media`

| Campo | Definición |
|---|---|
| Responsabilidad | Oferta publicitaria contextual Retail; plataforma externa por definir |
| Productor | Oferta y sus datos autorizados |
| Consumidor | Oferta y canales propios |
| Datos | Datos Retail mínimos; contrato específico pendiente de validar |
| Interfaces | Capacidad interna del servicio responsable, no microservicio añadido; ver análisis de innovaciones |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Modo Tienda y fila virtual · Clientes · experiencia

ID: `fila`

| Campo | Definición |
|---|---|
| Responsabilidad | Coordinación de atención del cliente; contrato de eventos y avisos pendiente |
| Productor | Clientes Retail y sus datos autorizados |
| Consumidor | Clientes Retail y canales propios |
| Datos | Datos Retail mínimos; contrato específico pendiente de validar |
| Interfaces | Capacidad interna del servicio responsable, no microservicio añadido; ver análisis de innovaciones |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Azure Service Bus Premium · Retail · outbox / reintentos

ID: `bus_r`

| Campo | Definición |
|---|---|
| Responsabilidad | Entrega de hechos confirmados Retail; reintentos y DLQ; no autoridad del negocio |
| Productor | area_mercaderia; area_venta; area_clientes |
| Consumidor | comercio; canales; socios; area_clientes; local_sync; proy_r |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | bus_r → comercio: consumo; bus_r → canales: consumo; bus_r → socios: consumo; area_mercaderia → bus_r: publicacion; area_venta → bus_r: publicacion; bus_r → area_clientes: consumo; bus_r → local_sync: consumo; bus_r → proy_r: consumo; area_clientes → bus_r: publicacion |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure Service Bus Premium · Filial · outbox / reintentos

ID: `bus_e`

| Campo | Definición |
|---|---|
| Responsabilidad | Entrega de hechos confirmados Filial; sin unión con el bus Retail |
| Productor | servicios_e |
| Consumidor | credito; proy_e |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | bus_e → credito: consumo; servicios_e → bus_e: publicacion; bus_e → proy_e: consumo |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Comercio · ERP/DTE y WMS

ID: `comercio`

| Campo | Definición |
|---|---|
| Responsabilidad | Traduce y concilia contratos propios con ERP/DTE y WMS |
| Productor | bus_r |
| Consumidor | ext_comercio; archivo_r |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | bus_r → comercio: consumo; comercio → ext_comercio: adaptacion; comercio → archivo_r: adaptacion |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Canales · e-commerce / marketplace / fidelización

ID: `canales`

| Campo | Definición |
|---|---|
| Responsabilidad | Traduce contratos con e-commerce/marketplace/fidelización conservados |
| Productor | bus_r |
| Consumidor | ext_canales |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | bus_r → canales: consumo; canales → ext_canales: adaptacion |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Socios · pagos / proveedores / transportistas

ID: `socios`

| Campo | Definición |
|---|---|
| Responsabilidad | Traduce contratos con pagos/proveedores/transportistas; precisar lockers y publicidad |
| Productor | bus_r |
| Consumidor | ext_socios |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | bus_r → socios: consumo; socios → ext_socios: adaptacion |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Crédito · legado 2011 / CMF / firma

ID: `credito`

| Campo | Definición |
|---|---|
| Responsabilidad | Adapta convivencia de crédito 2011 y contrapartes de Filial |
| Productor | bus_e |
| Consumidor | ext_credito |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | bus_e → credito: consumo; credito → ext_credito: adaptacion |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Operación sin enlace · Venta y consulta de oferta vigente

ID: `local_serv`

| Campo | Definición |
|---|---|
| Responsabilidad | Responsabilidad lógica de venta y consulta de oferta sin enlace; no equipo físico |
| Productor | pos |
| Consumidor | local_sync; local_data |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | pos → local_serv: solicitud; local_serv → local_sync: publicacion; local_serv → local_data: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Sincronización de operaciones · Reintentos y conciliación

ID: `local_sync` · L-03

| Campo | Definición |
|---|---|
| Responsabilidad | Reenvía diario a APIs Retail y concilia; no escribe directamente en la base central |
| Productor | local_serv; local_data; bus_r |
| Consumidor | application_gateway |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | local_serv → local_sync: publicacion; local_sync → application_gateway: solicitud; local_data → local_sync: flujo; bus_r → local_sync: consumo |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL · Retail · Oferta / Abastecimiento / Existencias

ID: `datos_merc`

| Campo | Definición |
|---|---|
| Responsabilidad | Agrupa repositorios propietarios de Mercadería; no tablas compartidas entre servicios |
| Productor | area_mercaderia |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | area_mercaderia → datos_merc: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL · Retail · Pedidos / Ventas / Comisiones / Marketplace

ID: `datos_venta`

| Campo | Definición |
|---|---|
| Responsabilidad | Agrupa repositorios propietarios de Venta; no acceso lateral libre |
| Productor | area_venta |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | area_venta → datos_venta: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL · Retail · Posventa / Clientes

ID: `datos_clientes`

| Campo | Definición |
|---|---|
| Responsabilidad | Repositorios propios de Posventa y Clientes |
| Productor | area_clientes |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | area_clientes → datos_clientes: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Bitácora · de cruces

ID: `bitacora`

| Campo | Definición |
|---|---|
| Responsabilidad | Persistencia propia de X-01 con correlativos y decisión mínima |
| Productor | x01 |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | x01 → bitacora: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL · Filial · Originación / metadatos de Evidencia · Repositorios por servicio

ID: `datos_orig`

| Campo | Definición |
|---|---|
| Responsabilidad | Repositorios propios de Originación y metadatos de Evidencia; autoridades distintas |
| Productor | servicios_e |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | servicios_e → datos_orig: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL · Filial · Cartera y estado de procesos

ID: `datos_cartera`

| Campo | Definición |
|---|---|
| Responsabilidad | Persistencia financiera y estado durable de procesos del propietario |
| Productor | servicios_e |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | servicios_e → datos_cartera: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure Blob Storage · Filial · Evidencia y consentimiento vigentes

ID: `datos_evid`

| Campo | Definición |
|---|---|
| Responsabilidad | Documentos de evidencia vigentes de C-03; integridad y consulta autorizada |
| Productor | servicios_e |
| Consumidor | archivo_e |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | servicios_e → datos_evid: persistencia; datos_evid → archivo_e: flujo |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure Blob Storage · Retail · Documentos, retención y conjuntos versionados

ID: `archivo_r`

| Campo | Definición |
|---|---|
| Responsabilidad | Documentos ERP/DTE autorizados, auditoría propia y conjuntos versionados separados |
| Productor | proy_r; comercio; monitor |
| Consumidor | area_mercaderia |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | proy_r → archivo_r: flujo; archivo_r → area_mercaderia: flujo; comercio → archivo_r: adaptacion; monitor → archivo_r: politica |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure Blob Storage · Filial · Archivo retenido y consulta autorizada

ID: `archivo_e`

| Campo | Definición |
|---|---|
| Responsabilidad | Archivo de evidencia y auditoría Filial con clasificación y retención propias |
| Productor | datos_evid; monitor |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | datos_evid → archivo_e: flujo; monitor → archivo_e: politica |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure Managed Redis · Retail · Caché de oferta ≤ 30 s

ID: `redis`

| Campo | Definición |
|---|---|
| Responsabilidad | Caché operacional de oferta/disponibilidad; no modelo de BI ni autoridad |
| Productor | area_mercaderia |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | area_mercaderia → redis: persistencia |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL · Retail · Historial de precios append-only

ID: `historial`

| Campo | Definición |
|---|---|
| Responsabilidad | Historial Retail de precios publicados, solo anexado |
| Productor | area_mercaderia |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | area_mercaderia → historial: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Microsoft Power BI · Modelos semánticos y espacios separados por ámbito · DirectQuery / Import sobre repositorios analíticos

ID: `powerbi`

| Campo | Definición |
|---|---|
| Responsabilidad | Lee únicamente modelos analíticos dedicados; permisos y conexiones propios por ámbito |
| Productor | mart_r; mart_e |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | mart_r → powerbi: flujo; mart_e → powerbi: flujo |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Diario de operaciones pendientes · Persistencia durable Retail

ID: `local_data` · L-02

| Campo | Definición |
|---|---|
| Responsabilidad | Diario durable Retail de operaciones pendientes con identidad y estado de entrega |
| Productor | local_serv |
| Consumidor | local_sync |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | local_serv → local_data: persistencia; local_data → local_sync: flujo |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Cupo preautorizado sin enlace · Datos mínimos de Filial · vigencia pendiente

ID: `cupo_local`

| Campo | Definición |
|---|---|
| Responsabilidad | Datos mínimos preautorizados de Filial; política de exclusividad/caducidad pendiente |
| Productor | servicios_e; meson_f |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | servicios_e → cupo_local: condicionado; meson_f → cupo_local: condicionado |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## ERP/DTE y WMS conservados

ID: `ext_comercio`

| Campo | Definición |
|---|---|
| Responsabilidad | ERP/DTE y WMS conservados; autoridades y contratos externos |
| Productor | comercio |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | comercio → ext_comercio: adaptacion |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## E-commerce, marketplace y fidelización

ID: `ext_canales`

| Campo | Definición |
|---|---|
| Responsabilidad | Plataformas de canal conservadas; no servicios nuevos internos |
| Productor | canales |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | canales → ext_canales: adaptacion |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Pagos, proveedores y transportistas · Lockers y publicidad: interfaz por precisar

ID: `ext_socios`

| Campo | Definición |
|---|---|
| Responsabilidad | Contrapartes de pago/proveedores/transporte; proveedores concretos por levantar |
| Productor | socios |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | socios → ext_socios: adaptacion |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Crédito 2011 (convivencia) · Reportes CMF y firma por interfaz

ID: `ext_credito`

| Campo | Definición |
|---|---|
| Responsabilidad | Plataforma financiera 2011 durante convivencia y contrapartes reguladas |
| Productor | credito |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | credito → ext_credito: adaptacion |
| Estado | Conservado durante convivencia; contratos por verificar |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Microsoft Entra ID P2 · Tenant Filial separado: confirmar

ID: `entra`

| Campo | Definición |
|---|---|
| Responsabilidad | Identidades internas y autorización; tenant propio de Filial pendiente de confirmación |
| Productor | Administración de identidad del ámbito |
| Consumidor | APIM, servicios y personal del ámbito |
| Datos | Identidades y roles; sin copia libre entre tenants |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Microsoft Entra External ID · Tenant externo por negocio

ID: `externalid`

| Campo | Definición |
|---|---|
| Responsabilidad | Identidades de clientes separadas por negocio |
| Productor | Registro/autenticación de clientes por negocio |
| Consumidor | Canales propios y APIM autorizado |
| Datos | Identidad externa y claims mínimos |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Azure Key Vault / Managed HSM · Claves y cifrado de campo por ámbito

ID: `kv`

| Campo | Definición |
|---|---|
| Responsabilidad | Secretos, claves y cifrado de campo por ámbito; HSM y rotación por verificar |
| Productor | Custodios de claves y servicios propietarios |
| Consumidor | Servicios/APIM autorizados por ámbito |
| Datos | Secretos, claves y material cifrado |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Microsoft Sentinel y Defender · SOC: solo incidentes agregados

ID: `sentinel`

| Campo | Definición |
|---|---|
| Responsabilidad | Detección y respuesta de seguridad; solo incidentes agregados entre ámbitos |
| Productor | Señales de seguridad del ámbito |
| Consumidor | SOC del ámbito; salud agregada autorizada |
| Datos | Incidentes y evidencias minimizadas |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## PIM / Bastion / Private Access · Administración y acceso remoto

ID: `privado`

| Campo | Definición |
|---|---|
| Responsabilidad | Elevación y acceso administrativo; detalle de rutas y grabaciones en vista física |
| Productor | Administradores con elevación aprobada |
| Consumidor | Recursos administrados del ámbito |
| Datos | Sesiones privilegiadas y registros |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## OpenTelemetry Collector · Por clúster y tienda · cola local 24 h

ID: `otel`

| Campo | Definición |
|---|---|
| Responsabilidad | Recolección local de señales por ámbito y tienda; cola de 24 h |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | monitor |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | otel → monitor: condicionado |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure Monitor / Log Analytics · Registros, trazas y alertas por ámbito

ID: `monitor`

| Campo | Definición |
|---|---|
| Responsabilidad | Almacena registros y trazas, produce alertas y exporta auditoría propia |
| Productor | otel |
| Consumidor | grafana; archivo_r; archivo_e |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | otel → monitor: condicionado; monitor → grafana: condicionado; monitor → archivo_r: politica; monitor → archivo_e: politica |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Prometheus / Azure Managed Grafana · Métricas, SLO e indicadores de entrega

ID: `grafana`

| Campo | Definición |
|---|---|
| Responsabilidad | Consulta métricas, SLO e indicadores de entrega; no reemplaza almacén de trazas |
| Productor | monitor |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | monitor → grafana: condicionado |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Pruebas sintéticas y experiencia real · TLS y herramienta móvil pendientes

ID: `rum`

| Campo | Definición |
|---|---|
| Responsabilidad | Pruebas sintéticas y experiencia real; herramienta móvil y TLS por verificar |
| Productor | Pruebas y clientes instrumentados con política aprobada |
| Consumidor | Operación del ámbito |
| Datos | Disponibilidad, latencia y experiencia muestreada |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Azure Front Door Premium · Retail / Filial: perfiles separados · WAF propio por ámbito · TLS 1.3 objetivo

ID: `front_door`

| Campo | Definición |
|---|---|
| Responsabilidad | Entrada pública con perfiles y WAF por ámbito; TLS y tránsito sujetos a validación |
| Productor | dns; web; portal_f |
| Consumidor | private_link |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | dns → front_door: politica; front_door → private_link: condicionado; web → front_door: solicitud; portal_f → front_door: solicitud |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Application Gateway v2 · Instancias Retail / Filial separadas

ID: `application_gateway`

| Campo | Definición |
|---|---|
| Responsabilidad | Proxy de entrada privada al ámbito; recursos separados; producto único en vista |
| Productor | pos; operacion; logistica; movil; meson_f; local_sync; private_link |
| Consumidor | api_management |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | application_gateway → api_management: solicitud; pos → application_gateway: solicitud; operacion → application_gateway: solicitud; logistica → application_gateway: solicitud; movil → application_gateway: solicitud; meson_f → application_gateway: solicitud; local_sync → application_gateway: solicitud; private_link → application_gateway: condicionado |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure API Management Premium clásico · Instancias, productos y contratos separados por ámbito

ID: `api_management`

| Campo | Definición |
|---|---|
| Responsabilidad | Políticas, identidad, cuotas y contratos por ámbito; backends privados propios |
| Productor | application_gateway; api_center; x01 |
| Consumidor | area_mercaderia; area_venta; area_clientes; servicios_e |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | application_gateway → api_management: solicitud; api_center → api_management: politica; api_management → area_mercaderia: solicitud; api_management → area_venta: solicitud; api_management → area_clientes: solicitud; api_management → servicios_e: solicitud; x01 → api_management: compra_autorizable |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure API Center · Catálogos Retail / Filial separados

ID: `api_center`

| Campo | Definición |
|---|---|
| Responsabilidad | Gobierno de contratos por ámbito; pipeline deriva contratos APIM; no tráfico comercial |
| Productor | Propietario del componente; detalle por verificar |
| Consumidor | api_management |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | api_center → api_management: politica |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Azure Private Link

ID: `private_link`

| Campo | Definición |
|---|---|
| Responsabilidad | Conecta origen Front Door al Application Gateway del ámbito; endpoints propios |
| Productor | front_door |
| Consumidor | application_gateway |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | front_door → private_link: condicionado; private_link → application_gateway: condicionado |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Servicios comunes · definición pendiente · Separados por ámbito · sin consumidores supuestos

ID: `comunes`

| Campo | Definición |
|---|---|
| Responsabilidad | Responsabilidad aún no definida; componente separado por ámbito sin consumidores supuestos |
| Productor | Pendiente |
| Consumidor | Pendiente: no se inventan |
| Datos | Por definir por ámbito |
| Interfaces | Sin contratos; pendiente P-04 explícito |
| Estado | Pendiente de definición |
| Decision | Conservar en L2 |
| Relacion | Pendiente |

## Procesadores de proyecciones · Retail · Deduplicación, versión y conciliación

ID: `proy_r`

| Campo | Definición |
|---|---|
| Responsabilidad | Actualiza modelos Retail con deduplicación, versión y checkpoint transaccionales |
| Productor | bus_r |
| Consumidor | mart_r; archivo_r |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | bus_r → proy_r: consumo; proy_r → mart_r: persistencia; proy_r → archivo_r: flujo |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL Flexible Server · Retail · Repositorio analítico dedicado · Indicadores, agregaciones y linaje

ID: `mart_r`

| Campo | Definición |
|---|---|
| Responsabilidad | PostgreSQL analítico Retail dedicado: indicadores, hechos, agregados y linaje |
| Productor | proy_r |
| Consumidor | powerbi |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | proy_r → mart_r: persistencia; mart_r → powerbi: flujo |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## Procesadores de proyecciones · Filial · Deduplicación, versión y conciliación

ID: `proy_e`

| Campo | Definición |
|---|---|
| Responsabilidad | Actualiza modelos Filial con deduplicación, versión y checkpoint transaccionales |
| Productor | bus_e |
| Consumidor | mart_e |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | bus_e → proy_e: consumo; proy_e → mart_e: persistencia |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL Flexible Server · Filial · Repositorio analítico dedicado · Indicadores, agregaciones y linaje

ID: `mart_e`

| Campo | Definición |
|---|---|
| Responsabilidad | PostgreSQL analítico Filial dedicado: posición financiera y modelos propios |
| Productor | proy_e |
| Consumidor | powerbi |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | proy_e → mart_e: persistencia; mart_e → powerbi: flujo |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## PostgreSQL / pgvector · Retail · Índice de búsqueda del catálogo

ID: `vector`

| Campo | Definición |
|---|---|
| Responsabilidad | Índice PostgreSQL/pgvector del catálogo autorizado; reconstruible por Oferta |
| Productor | area_mercaderia |
| Consumidor | Uso descrito por responsabilidad; contrato por verificar |
| Datos | Referencias mínimas y datos propios según contrato; verificar clasificación y retención |
| Interfaces | area_mercaderia → vector: persistencia |
| Estado | Propuesto; verificación o decisión pendiente |
| Decision | Conservar en L2 |
| Relacion | Explícita |

## React / React Native · TypeScript · canales separados

ID: `tech_ui`

| Campo | Definición |
|---|---|
| Responsabilidad | Tecnología de canales web y móvil; dependencias de construcción, no nuevo servicio |
| Productor | Equipo de canales |
| Consumidor | Presentación |
| Datos | Artefactos React/TypeScript/React Native |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Java 25 LTS · APIs y trabajadores propios

ID: `tech_java`

| Campo | Definición |
|---|---|
| Responsabilidad | Runtime de servicios y trabajadores propios; compatibilidad por comprobar |
| Productor | Equipo de plataforma |
| Consumidor | APIs y trabajadores |
| Datos | Artefactos y runtime |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Spring Boot 4 · Contratos y lógica de servicios

ID: `tech_spring`

| Campo | Definición |
|---|---|
| Responsabilidad | Framework de APIs y lógica propia; no componente de tráfico adicional |
| Productor | Equipo de servicios |
| Consumidor | APIs y lógica propia |
| Datos | Contratos y artefactos |
| Interfaces | Dependencia transversal/de tecnología declarada por banda, no llamada de negocio |
| Estado | Propuesto, no desplegado/acreditado |
| Decision | Conservar en L2 |
| Relacion | Responsabilidad agrupada/transversal |

## Data Lake Retail

ID: `lago_r`

| Campo | Definición |
|---|---|
| Responsabilidad | Usos analíticos cubiertos por PostgreSQL dedicado; documentos/conjuntos en Blob |
| Productor | No aplica a la vista resultante |
| Consumidor | No aplica a la vista resultante |
| Datos | Conservar autoridad/retención aplicables; no se ordena eliminar datos |
| Interfaces | Ver decisión y análisis |
| Estado | Decisión de esta iteración |
| Decision | Retirar |
| Relacion | Fuera de la vista |

## Data Lake Filial

ID: `lago_e`

| Campo | Definición |
|---|---|
| Responsabilidad | Modelo financiero en PostgreSQL dedicado; archivo/evidencia separados |
| Productor | No aplica a la vista resultante |
| Consumidor | No aplica a la vista resultante |
| Datos | Conservar autoridad/retención aplicables; no se ordena eliminar datos |
| Interfaces | Ver decisión y análisis |
| Estado | Decisión de esta iteración |
| Decision | Retirar |
| Relacion | Fuera de la vista |

## Backup Vault

ID: `backup`

| Campo | Definición |
|---|---|
| Responsabilidad | Definir cobertura por recurso, copia aislada y prueba de restauración |
| Productor | No aplica a la vista resultante |
| Consumidor | No aplica a la vista resultante |
| Datos | Conservar autoridad/retención aplicables; no se ordena eliminar datos |
| Interfaces | Ver decisión y análisis |
| Estado | Decisión de esta iteración |
| Decision | Trasladar a físico/operativo |
| Relacion | Fuera de la vista |

## Arc / Monitor Agent

ID: `arc`

| Campo | Definición |
|---|---|
| Responsabilidad | Gestión de servidores/agentes; OTEL y Monitor mantienen responsabilidad lógica |
| Productor | No aplica a la vista resultante |
| Consumidor | No aplica a la vista resultante |
| Datos | Conservar autoridad/retención aplicables; no se ordena eliminar datos |
| Interfaces | Ver decisión y análisis |
| Estado | Decisión de esta iteración |
| Decision | Trasladar a físico/operativo |
| Relacion | Fuera de la vista |

## Coordinador Retail como motor seleccionado

ID: `saga_r`

| Campo | Definición |
|---|---|
| Responsabilidad | Coordinación durable permanece como responsabilidad de Integración; motor por justificar |
| Productor | No aplica a la vista resultante |
| Consumidor | No aplica a la vista resultante |
| Datos | Conservar autoridad/retención aplicables; no se ordena eliminar datos |
| Interfaces | Ver decisión y análisis |
| Estado | Decisión de esta iteración |
| Decision | Retirar caja concreta |
| Relacion | Fuera de la vista |

## Coordinador Filial como motor seleccionado

ID: `saga_e`

| Campo | Definición |
|---|---|
| Responsabilidad | Sin imponer tecnología de flujos ni base compartida |
| Productor | No aplica a la vista resultante |
| Consumidor | No aplica a la vista resultante |
| Datos | Conservar autoridad/retención aplicables; no se ordena eliminar datos |
| Interfaces | Ver decisión y análisis |
| Estado | Decisión de esta iteración |
| Decision | Retirar caja concreta |
| Relacion | Fuera de la vista |

## Duplicación visual de Servicios comunes

ID: `comunes_r/comunes_e`

| Campo | Definición |
|---|---|
| Responsabilidad | Un símbolo pendiente, recursos separados por ámbito |
| Productor | No aplica a la vista resultante |
| Consumidor | No aplica a la vista resultante |
| Datos | Conservar autoridad/retención aplicables; no se ordena eliminar datos |
| Interfaces | Ver decisión y análisis |
| Estado | Decisión de esta iteración |
| Decision | Consolidar representación |
| Relacion | Fuera de la vista |

## Fila de actores

ID: `actores`

| Campo | Definición |
|---|---|
| Responsabilidad | Última instrucción del usuario; no elimina personas ni funciones del alcance |
| Productor | No aplica a la vista resultante |
| Consumidor | No aplica a la vista resultante |
| Datos | Conservar autoridad/retención aplicables; no se ordena eliminar datos |
| Interfaces | Ver decisión y análisis |
| Estado | Decisión de esta iteración |
| Decision | Omitir de esta vista |
| Relacion | Fuera de la vista |
