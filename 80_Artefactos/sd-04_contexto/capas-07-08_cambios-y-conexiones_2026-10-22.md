# Capas 7 y 8: componentes conservados, cambios y conexiones

Fecha: 22-10-2026. Estado documental: borrador de contexto de SD-04. Procedencia: análisis y selección de servicios de esta conversación. Alcance: especificación para actualizar la arquitectura lógica; no modifica el diagrama ni los entregables LaTeX.

## 1. Referencias y alcance

La línea base es la [figura 4.31](../../04_Adjuntos/diagramas/diag-04-31_arquitectura-servicios-y-flujos.json), su [contexto](integracion-capa4-2026-10-22/README.md), el [inventario de relaciones](integracion-capa4-2026-10-22/relaciones-y-evidencia.md) y el [registro D-40–D-53](decisiones-2026-10-22/registro-recibido.md).

Se integra la actualización de la [capa de datos](capa-datos_decisiones-y-precisiones_2026-10-22.md): Data Lake, Data Factory, OpenSearch, OpenMetadata, MLflow y los trabajos de datos también deben recibir identidad, seguridad y observabilidad. No son componentes ya presentes en su totalidad en la figura 4.31.

La selección de productos registrada aquí está cerrada para la siguiente edición. Siguen requiriéndose dimensionamiento, versiones compatibles, emplazamiento, configuración, pruebas y las aprobaciones del mandante que correspondan. La selección no acredita disponibilidad regional, despliegue, cumplimiento normativo ni aceptación humana del subdocumento.

## 2. Qué se conserva y qué cambia

### 2.1 Capa 7 — Seguridad

| Elemento | Decisión | Cambio respecto de la figura 4.31 |
|---|---|---|
| Microsoft Entra ID P2 | Conservar | Identidad del personal y privilegios; tenant propio de Filial como selección de diseño. Separar administración y cuentas de emergencia. |
| Microsoft Entra External ID | Conservar | Identidad externa de compradores y titulares, separada por negocio. Los terceros operacionales tienen ciclo de acceso propio. |
| Microsoft Intune | Añadir explícitamente | Administración de terminales compartidas, aplicaciones, cumplimiento, bloqueo y borrado remoto de equipos compatibles. |
| Identidades administradas y Entra Workload Identity | Añadir explícitamente | Identidad de servicios, pods, trabajadores y pipelines; permisos propios, sin secretos permanentes repartidos en imágenes o código. |
| Azure Key Vault | Conservar y separar visualmente | Secretos y certificados; dejar de agrupar su función con la de Managed HSM mediante una barra ambigua. |
| Azure Managed HSM | Conservar y separar visualmente | Claves criptográficas seleccionadas para cifrado de campo y protección de claves de datos. |
| Microsoft Sentinel | Conservar y separar de Defender | SIEM, correlación e investigación de seguridad; instancia/espacio propio por ámbito. |
| Defender for Endpoint | Nombrar explícitamente | Protección de equipos compatibles; sustituye parte del rótulo genérico «Defender». |
| Defender for Cloud | Nombrar explícitamente | Postura y protección de servidores y contenedores mediante planes declarados y compatibles. |
| PIM | Conservar y separar visualmente | Elevación temporal, aprobación y registro; no transporta las sesiones administrativas. |
| Bastion Premium | Conservar y precisar nivel | Acceso administrativo a máquinas y grabación en los recorridos compatibles. |
| Entra Private Access | Conservar y separar visualmente | Acceso remoto a recursos privados autorizados; no sustituye el transporte entre tiendas y nube. |
| Archivo WORM del ámbito | Conservar en Datos, referenciar desde Seguridad | Custodia de auditoría y evidencia; distinguir archivo final de almacenamiento temporal de grabaciones. |
| QR + PIN como MFA general | Retirar esa interpretación | Puede usarse en el ingreso interno autorizado, pero es un solo factor y no satisface accesos que exigen MFA. |
| SOC 24×7 | Conservar como servicio operativo | Dotación, turnos, investigación y respuesta; no es una capacidad proporcionada automáticamente por Sentinel. |

### 2.2 Capa 8 — Observabilidad

| Elemento | Decisión | Cambio respecto de la figura 4.31 |
|---|---|---|
| OpenTelemetry e instrumentación | Conservar | Incluir aplicaciones, trabajadores, adaptadores, operación local y nuevos componentes de datos. |
| OpenTelemetry Collector | Conservar | Colectores por ámbito, clúster y tienda; colas persistentes y destinos por señal. |
| Prometheus | Conservar y separar de Grafana | Recolección y almacenamiento de métricas; identificar su persistencia, alta disponibilidad y retención. |
| Grafana Loki | Añadir | Almacenamiento y consulta de registros operacionales. |
| Grafana Tempo | Añadir | Almacenamiento y consulta de trazas distribuidas. |
| Azure Managed Grafana | Sustituir | Se reemplaza por Grafana autogestionado en Azure. |
| Grafana autogestionado | Incluir como sustitución | Visualización y alertas sobre Prometheus, Loki, Tempo y Azure Monitor. Instancias y credenciales separadas por ámbito. |
| Grafana Alerting | Hacer explícito dentro de Grafana | Reglas, agrupación, rutas de notificación y comprobación de entrega. No se añade un Alertmanager independiente. |
| Prometheus Blackbox Exporter | Añadir | Sondas de disponibilidad, conectividad y TLS desde posiciones internas y externas. |
| Azure Monitor / Log Analytics | Conservar con función acotada | Diagnóstico de recursos Azure y fuentes necesarias para seguridad/Sentinel. |
| Collector → Azure Monitor mediante ingestión OTLP en vista previa | Retirar como recorrido productivo base | Registros de aplicaciones a Loki, trazas a Tempo y métricas a Prometheus. |
| Experiencia real web/móvil | Conservar y concretar como instrumentación | Duración, resultado y errores de recorridos reales; no se añade otro producto RUM. |
| NOC con salud agregada | Conservar como vista operativa | Solo información de salud autorizada; sin consultas compartidas a registros o datos de negocio. |

Loki, Tempo, Prometheus y Grafana autogestionados requieren operación, mantenimiento, soporte, alta disponibilidad y recuperación incluidos en la oferta. La excepción a la preferencia por servicios administrados de RT-03.05 se justifica por la integración OTLP documentada y el control del emplazamiento, no por ahorro de costos. No se afirman capacidades acreditadas por seleccionar estos componentes.

## 3. Convención de conexiones

Las flechas siguientes describen la dirección de la solicitud o publicación iniciada, salvo que la fila indique «consulta». Las respuestas pertenecen al mismo intercambio. No representan puertos ya habilitados ni una configuración de red ejecutada.

| Tipo | Significado | Tratamiento gráfico |
|---|---|---|
| Identidad | Inicio de sesión, emisión/validación de credenciales o federación de cargas | Relación de identidad; no dibujar Entra en serie con cada llamada de negocio. |
| Administración | Elevación, acceso remoto o gestión de equipos | Vista de administración; no mezclar con venta, pedido o crédito. |
| Criptografía | Obtención de secretos/certificados o uso autorizado de claves | Dependencia técnica; no trasladar datos completos del negocio al custodio. |
| Telemetría | Publicación de métricas, registros o trazas | Colector y destino por ámbito y tipo de señal. |
| Consulta | Un consumidor consulta un repositorio de telemetría | Grafana → backend; la respuesta devuelve el resultado. |
| Seguridad | Ingestión lógica de eventos y alertas en el SIEM | Conector específico por origen; la dirección de red depende del mecanismo soportado. |
| Archivo | Escritura de evidencia verificada en custodia | Destino WORM del ámbito y confirmación de integridad. |

Las relaciones transversales pueden representarse mediante bandas y familias de dependencias. No se dibuja una flecha a cada caja si ello impide leer la vista general; el inventario de este documento conserva el detalle. Los estilos y semánticas finales se validan mediante `diagramas-ancoa`.

## 4. Identificación de nodos para la siguiente edición

Los nombres de esta tabla son identificadores técnicos de figura, no nuevos códigos de servicios de negocio ni requisitos RF/RNF. Los sufijos `r` y `e` identifican recursos propios de Retail y Filial.

| Nodo actual | Tratamiento | Identificadores de destino de esta especificación |
|---|---|---|
| `entra` | Conservar; distinguir ámbitos | `entra_r`, `entra_e` |
| `externalid` | Conservar; distinguir ámbitos | `externalid_r`, `externalid_e` |
| `kv` | Desagrupar funciones | `keyvault_r`, `keyvault_e`, `hsm_r`, `hsm_e` |
| `sentinel` | Desagrupar SIEM y protección | `sentinel_r`, `sentinel_e`, `defender_endpoint_r/e`, `defender_cloud_r/e` |
| `privado` | Desagrupar administración | `pim_r/e`, `bastion_r/e`, `private_access_r/e` |
| Sin nodo explícito | Añadir gestión e identidad técnica | `intune_r/e`, `workload_identity_r/e` |
| `otel` | Conservar por ámbito y sitio | `otel_r`, `otel_e`, `otel_tienda_r/e` |
| `monitor` | Conservar con función acotada | `monitor_r/e` para Azure Monitor/Log Analytics del ámbito |
| `grafana` | Separar y sustituir visualizador | `prometheus_r/e`, `grafana_r/e` autogestionado |
| Sin nodos explícitos | Añadir destinos y sondas | `loki_r/e`, `tempo_r/e`, `blackbox_r/e` |
| `rum` | Reetiquetar | Instrumentación de experiencia real en canales; sondas en `blackbox_r/e`. |

La notación `r/e` abrevia dos instancias o responsabilidades separadas; no debe usarse como ID literal en el JSON. En la vista general puede conservarse un símbolo de producto con la separación declarada, pero las relaciones deben identificar inequívocamente el ámbito. Una capa no se convierte en una instancia compartida por tener una sola banda visual.

## 5. Conexiones de capa 7 con el resto del diagrama

### 5.1 Identidad y autorización

| Origen | Destino | Relación y alcance | Control |
|---|---|---|---|
| Canales internos `pos`, `operacion`, `logistica`, `movil` y consola Retail de `common_admin` | `entra_r` | Inicio de sesión del personal Retail; integración con directorio corporativo acordado. | Sesión nominativa, roles/atributos y cierre al relevo. |
| `meson_f` y consola Filial de `common_admin` | `entra_e` | Identidad del personal de Filial. | Segregación de originación, aprobación, modificación y cobranza. |
| `web` | `externalid_r` | Registro, autenticación y recuperación de acceso del comprador. | Credenciales y finalidades Retail. |
| `portal_f` | `externalid_e` | Identidad del titular de tarjeta. | Datos e identidad financiera propios; verificación de identidad de negocio separada del simple login. |
| Aplicaciones de proveedores, marketplace, transportistas y repositores | Directorio del ámbito y aplicaciones autorizadas | Acceso de terceros con patrocinador, permisos, vigencia y baja. | No equiparar automáticamente una persona externa a un comprador ni crear cuentas compartidas. |
| `api_management` del ámbito y servicios receptores | Metadatos públicos y claves de validación del emisor de identidad autorizado | Validación local de tokens, audiencia, emisor y permisos; actualización de claves según política. | No hay consulta obligatoria a Entra en cada petición. El servicio mantiene su autorización de negocio. |
| `aks_r` —representación actual de clústeres por ámbito— y cuentas de servicio de pods | `workload_identity_r/e` y Entra propio | Federación de la identidad de la carga. | Identidad y permisos por servicio; ningún pod hereda acceso global a ambos ámbitos. |
| `workload_identity_r/e` y cargas autorizadas | Service Bus, almacenamiento, Key Vault y recursos que admitan el mecanismo | Autenticación de cargas mediante tokens de vida limitada. | El soporte se verifica por recurso; identidad de carga no equivale a habilitar permisos ni a cifrar todos los saltos. |
| Data Factory, proyectores y trabajos de datos | Identidades propias del ámbito | Lectura y escritura en los orígenes y destinos de sus contratos. | Acceso mínimo; no credenciales de propietario de base ni acceso general al histórico financiero. |

OpenMetadata, MLflow, OpenSearch, Grafana y las herramientas de operación también integran identidad y autorización propias del ámbito. Ninguna herramienta obtiene acceso a datos por el solo hecho de aparecer en una banda transversal.

El navegador contacta los endpoints de identidad por su recorrido soportado. No se obliga a insertar APIM como proxy de esos endpoints. Dominios, salidas, residencia y tratamiento de metadatos de identidad se declaran en el inventario de exposición y comunicaciones.

### 5.2 Equipos y acceso administrativo

| Origen | Destino | Relación y alcance | Control |
|---|---|---|---|
| `intune_r/e` | Equipos compatibles que alojan `pos`, `operacion`, `meson_f` y consolas administradas | Inventario, políticas, aplicaciones, cumplimiento, bloqueo y borrado. | Identidad de dispositivo; tratamiento declarado de equipos no compatibles. El borrado remoto no es inmediato sin enlace. |
| Aplicaciones de terminal compartida | Entra/MSAL y modo compartido compatibles | Inicio y cierre de sesión coordinado. | Limpiar datos y credenciales de la persona saliente; probar integración React Native y almacenamiento local. |
| Administrador autorizado | `entra_r/e` → autorización de elevación en `pim_r/e` | Autenticación reforzada y solicitud de privilegios temporales. | Aprobación previa, duración y auditoría. PIM no es un proxy de tráfico. |
| Equipo administrativo autorizado | `private_access_r/e` → recurso privado permitido | Acceso remoto acotado a recursos privados. | Permisos por recurso; no puente general entre redes ni sustitución de la VPN/SD-WAN de las tiendas. |
| Administrador con privilegio vigente | `bastion_r/e` → máquinas de administración y servidores permitidos | Sesión administrativa de máquina mediante recorrido compatible con grabación. | Bastion Premium; sin RDP/SSH públicos ni atajos que eludan el control. |
| Herramienta administrativa autorizada | API de Kubernetes, PostgreSQL, OpenSearch y demás planos de administración propios | Administración técnica específica. | Auditoría del plano correspondiente. No afirmar que Bastion graba automáticamente estas acciones o todas las consolas web. |

La capa de Borde conserva `entrada_privada`, Front Door, Private Link y Application Gateway. Entra Private Access se representa en el acceso administrativo; no se añade en serie a toda venta o consulta interna.

### 5.3 Criptografía, detección y archivo

| Origen | Destino | Relación y alcance | Control |
|---|---|---|---|
| Servicios de negocio, adaptadores, trabajadores y herramientas autorizadas | `keyvault_r/e` | Obtención/rotación de secretos y certificados que cada componente necesite. | Identidad propia, privilegio mínimo y caché segura cuando proceda. Nunca poner secretos en logs. |
| Aplicaciones responsables del cifrado de campo | `hsm_r/e` | Operaciones autorizadas de protección/uso de claves y envoltura de claves de datos. | Diseño criptográfico por dominio. No enviar la base completa al HSM ni suponer una llamada remota por cada campo de cada fila. |
| Servicios financieros `originacion`, `cartera`, `evidencia` y repositorios propietarios | Claves y políticas de Filial | Cifrado adicional de campos sensibles y acceso autorizado. | La posesión de credenciales SQL no debe revelar esos campos. Índices ciegos con riesgo de correlación documentado. |
| `socios` y contrato del procesador de pagos | Contraparte de pagos de `ext_socios` | Tokenización y autorización de medios de pago conforme al contrato. | No añadir un almacén propio de datos originales de tarjeta como alternativa al token. |
| `defender_endpoint_r/e` | Equipos y servidores compatibles | Prevención, detección y respuesta del endpoint. | Identificar cobertura, excepciones y capacidad sin conexión. |
| `defender_cloud_r/e` | Recursos Azure, servidores y clústeres propios | Postura y protección mediante planes de servidores/contenedores declarados. | No asumir protección universal por habilitar el producto. |
| Entra, Key Vault, HSM, Defender, borde, APIM y planos administrativos | `sentinel_r/e` mediante conectores propios | Ingestión de eventos de seguridad y hallazgos. | Describir conectores, permisos, tablas, latencia y residencia. Es una relación lógica, no una promesa de exportador único. |
| Aplicaciones y `x01` | Fuente de auditoría/seguridad propia → `sentinel_r/e` | Eventos mínimos de acceso sensible, exportación, cambio de cupo, elevación y denegación de cruce. | Casos de uso del negocio, sin volcar cartera, contenido de documentos o payloads completos. |
| `sentinel_r/e` | SOC del ámbito | Incidentes y evidencia autorizada para investigación. | Cobertura 24×7, escalamiento, respuesta y comunicaciones al Cliente. |
| Fuente durable de auditoría y exportador autorizado | `archivo_r` o `archivo_e` | Custodia WORM, manifiestos e integridad. | Retención por clase; no sustituir auditoría obligatoria por logs operacionales muestreados. |
| `bastion_r/e` | Contenedor temporal de grabaciones propio | Escritura de la grabación mediante mecanismo soportado. | El destino inicial de grabación de Bastion debe carecer de políticas de inmutabilidad y de versionado según la documentación consultada. |
| Trabajo de archivo del ámbito | Grabación temporal → archivo WORM propio | Copia, comprobación de integridad y confirmación de custodia. | Proteger la ventana previa; detectar copia incompleta, demora y borrado indebido. La tarea usa los trabajadores existentes, sin nuevo servicio de negocio. |

La bitácora `bitacora` permanece bajo X-01 y registra el cruce mínimo autorizado. No se conecta Sentinel de Retail al repositorio de Cartera ni un Collector Retail al workspace financiero para facilitar la investigación.

## 6. Conexiones de capa 8 con el resto del diagrama

### 6.1 Productores de telemetría

| Elementos del diagrama | Destino | Señales y responsabilidad |
|---|---|---|
| `web`, `portal_f` | Ingestión de telemetría del ámbito por su borde/gateway → Collector propio | Experiencia real: tiempo, resultado, errores y referencias técnicas mínimas. Tráfico autenticado o controlado según sesión, validado y limitado. |
| `pos`, `operacion`, `logistica`, `movil`, `meson_f` | Colector local o entrada privada autorizada → Collector propio | Experiencia de terminal, latencia y fallos; cola durable cuando no hay enlace. |
| Servicios `oferta`, `abastecimiento`, `existencias`, `pedidos`, `ventas`, `comisiones`, `market`, `posventa`, `clientes` | `otel_r` | Trazas y métricas de negocio Retail, errores y registros saneados. |
| `originacion`, `cartera`, `evidencia` | `otel_e` | Trazas y métricas financieras sin saldos, mora, identidad sensible ni documentos en el payload de telemetría. |
| `x01` | Colector del contexto de frontera, con destino propio autorizado | Resultado técnico del cruce y referencias mínimas; mapeo autorizado entre correlativos. No exportación común de logs de los dos negocios. |
| `comercio`, `canales`, `socios`, `credito` | Collector del ámbito | Disponibilidad de contraparte, tiempos, reintentos y conciliación. No suponer control sobre los agentes internos de plataformas externas. |
| `proy_r`, `proy_e`, trabajadores, Data Factory y trabajos Python | Collector/exportadores o diagnóstico soportado del componente, por ámbito | Duración, corte, atraso, errores, registros procesados/rechazados y resultados de conciliación. |
| `common_admin`, `common_flujos`, `common_docs`, `common_notif`, APIs de búsqueda | Collector del ámbito | Errores, duración, tareas vencidas y estado de trabajos/notificaciones; auditoría obligatoria por su canal durable propio. |
| `local_serv`, `local_sync`, `local_data`, `cupo_local` | `otel_tienda_r/e` correspondiente | Salud local, pendiente de sincronizar, errores y conciliación. `cupo_local` solo usa observabilidad de Filial. |
| PostgreSQL, Redis, OpenSearch, OpenMetadata, MLflow y nodos de cómputo | Prometheus/exportadores y colectores compatibles del ámbito | Métricas de salud y capacidad, registros y trazas cuando estén disponibles. No se presume soporte idéntico de las tres señales en cada producto. |
| `front_door`, `application_gateway`, `api_management`, Service Bus y almacenamiento Azure | `monitor_r/e` mediante diagnóstico soportado | Métricas y registros de plataforma. La correlación con la aplicación usa referencias permitidas, no cuerpos de petición completos. |

La ruta de telemetría pública es una ruta técnica específica: canal → borde del ámbito → Application Gateway → APIM → receptor autorizado del Collector. No se expone el puerto interno del Collector directamente en Internet. Se aplican límites de tamaño/tasa, validación, saneamiento y protección contra falsificación de señales. El ID enviado por un cliente no se considera identidad confiable.

La instrumentación de experiencia real se implementa en la aplicación. En React Native debe probarse el puente y las bibliotecas de instrumentación compatibles; no se afirma que instalar un Collector instrumente automáticamente el móvil. Se registran inicio, fin, resultado y reloj adecuado, incluyendo operaciones offline y su posterior conciliación.

### 6.2 Destinos, consultas y alertas

| Origen | Destino | Tipo | Intención |
|---|---|---|---|
| Aplicaciones/trabajadores instrumentados | `otel_r/e` | Telemetría | OTLP autenticado en el ámbito y red permitidos; filtrado y control de atributos. |
| `otel_tienda_r/e` | Gateway/colector del ámbito | Telemetría | Reenvío al restablecer enlace, con persistencia, reintentos y control del drenaje. |
| `otel_r/e` | `loki_r/e` | Telemetría | Publicar registros operacionales mediante endpoint OTLP HTTP de Loki. |
| `otel_r/e` | `tempo_r/e` | Telemetría | Publicar trazas mediante OTLP compatible. |
| `otel_r/e` | `prometheus_r/e` | Telemetría | Publicar métricas por receptor OTLP HTTP habilitado y protegido. |
| `prometheus_r/e` | Endpoints de métricas y exportadores propios | Consulta/recolección | Scrape para componentes que expongan métricas Prometheus. Evitar recoger la misma serie por dos recorridos. |
| `grafana_r/e` | `prometheus_r/e` | Consulta | Métricas, indicadores y SLO; credenciales de lectura limitadas. |
| `grafana_r/e` | `loki_r/e` | Consulta | Investigación de registros operacionales autorizados. |
| `grafana_r/e` | `tempo_r/e` | Consulta | Investigación de trazas y enlaces de correlación permitidos. |
| `grafana_r/e` | `monitor_r/e` | Consulta | Diagnóstico de plataforma Azure mediante fuente de datos y autenticación soportadas. |
| Grafana Alerting del ámbito | Canales operativos de notificación | Alertamiento | Reglas, agrupación, escalamiento y confirmación de entrega. Sin incluir payloads sensibles en avisos. |
| Métricas/eventos mínimos de seguridad seleccionados | Conector propio de `sentinel_r/e` | Seguridad | Detecciones de seguridad. No se requiere duplicar todos los registros de Loki en Log Analytics. |
| Pipeline CI/CD y gestión de incidentes | Registro de indicadores → métricas/tableros del ámbito | Telemetría | Frecuencia de despliegue, tiempo hasta producción, cambios fallidos y restauración. |
| Datos históricos de métricas del ámbito | Reglas de análisis/alertas existentes | Alertamiento | Detección de desviaciones y anomalías con baseline, sin añadir otro producto de IA. |

Grafana consulta los almacenes; no los reemplaza. Loki almacena registros operacionales; Tempo trazas; Prometheus métricas. Azure Monitor/Log Analytics conserva el diagnóstico Azure y las fuentes requeridas por Sentinel. Blob WORM conserva evidencia bajo su política. Cada uno tiene retención y capacidad propias.

Grafana Alerting agrupa y enruta avisos. El turno de disponibilidad, el responsable del incidente y la escalada forman parte de NOC/SOC y de sus procedimientos; no se consideran resueltos por configurar una dirección de notificación.

### 6.3 Sondas y supervisión de la supervisión

| Origen | Destino | Qué se mide |
|---|---|---|
| Blackbox Exporter externo del ámbito | DNS y host público de `front_door` | Resolución, accesibilidad pública, HTTPS, certificado, protocolo y respuesta de una URL de prueba segura. |
| Blackbox Exporter interno del ámbito | `application_gateway`, `api_management` y endpoints técnicos privados | Disponibilidad desde la red corporativa y respuesta de componentes internos autorizados. |
| Blackbox Exporter en una posición de fallo independiente | Endpoints de salud de Collectors, Prometheus, Loki, Tempo y Grafana | Disponibilidad del propio sistema de observabilidad. |
| Prometheus del ámbito | Blackbox Exporter propio | Obtener resultados de las sondas y alimentar reglas. |
| Latido de nodo/colector de tienda | Observabilidad del ámbito | Distinguir «sitio no observable» de diagnóstico confirmado de caída de enlace, energía o aplicación. |

Las sondas externas se ejecutan desde una ubicación independiente de la ruta que inspeccionan y con tránsito declarado. Las internas no sustituyen la prueba pública. Blackbox Exporter comprueba endpoints y protocolos; no ejecuta por sí solo una compra completa ni prueba la consistencia funcional del negocio.

El nivel de servicio se calcula desde operaciones reales conforme a RT-14.03. Las sondas son complemento. La supervisión de la plataforma de monitoreo y su ruta de aviso deben sobrevivir a la falla que se pretende detectar; no concentrar todos los observadores y la única alerta en el mismo clúster.

## 7. Frontera entre ámbitos y vistas NOC/SOC

Cada negocio conserva colectores, almacenes, credenciales, tableros y eventos de seguridad propios. Una instancia de Grafana no obtiene credenciales amplias de ambos ámbitos para simplificar la vista.

La vista operativa agregada recibe únicamente un contrato de salud autorizado: componente técnico, estado, severidad, instante y referencia de incidente. Los trabajadores existentes pueden publicar ese resumen; no se crea un servicio de negocio nuevo ni una réplica central de telemetría detallada. Debe aprobarse qué metadatos pueden divulgarse entre equipos y cómo se investiga cada incidente con identidad del ámbito correspondiente.

El intercambio comercial entre negocios continúa por X-01. La administración y la salud agregada se documentan como planos técnicos controlados, sin habilitar acceso directo a cartera ni nuevos contratos de negocio. Se conserva una correspondencia mínima y autorizada entre referencias de cruce para poder reconstruir la transacción sin compartir sus registros completos.

## 8. Aristas de la figura 4.31 que cambian

| Relación o agrupación actual | Tratamiento en la siguiente figura |
|---|---|
| Relación 44: `otel` → `monitor`, exportador pendiente | Retirar como ruta OTLP productiva base. Reemplazar por Collector → Loki, Collector → Tempo y Collector → Prometheus del ámbito. |
| Relación 45: `monitor` → `grafana` | Expresar como dependencia de consulta Grafana → Azure Monitor. Grafana es autogestionado y también consulta Prometheus, Loki y Tempo. |
| Tarjeta «Prometheus / Azure Managed Grafana» | Separar almacén de métricas y visualizador; sustituir Azure Managed Grafana por Grafana autogestionado. |
| Tarjeta «Sentinel y Defender» | Separar SIEM, protección de endpoints y protección de cargas. |
| Tarjeta «PIM / Bastion / Private Access» | Separar elevación, salto administrativo y acceso remoto. No dibujar PIM como elemento de tránsito. |
| Tarjeta «Key Vault / Managed HSM» | Separar secretos/certificados y claves criptográficas. |
| Tarjeta «Pruebas sintéticas y experiencia real» | Separar sondas Blackbox de la instrumentación de canales. No utilizar sintéticos como sustituto de RT-14.03. |
| Bandas sin Intune ni identidad de cargas explícita | Añadir ambos componentes y sus relaciones de administración/identidad. |
| Exportación de auditoría omitida por simplificación visual | Conservar política transversal y detallar destino WORM, integridad y copia de grabaciones en la vista de evidencia/administración. |

Las aristas de negocio y datos de la figura 4.31 se conservan salvo los cambios de capa 6 ya definidos en su nota. Ninguna de estas conexiones permite a APIM escribir directamente en un repositorio de negocio ni incorpora F:C-04 como servicio vigente.

## 9. Controles que no deben perderse al dibujar

- TLS y autenticación por salto; identidad de carga no sustituye autorización, políticas de red ni cifrado.
- MFA para administradores, privilegios y acceso externo. QR + PIN no se presenta como segundo factor.
- Cierre de sesión, limpieza y permisos nominativos en dispositivos compartidos; límites explícitos de revocación y administración sin enlace.
- Cola persistente local dimensionada para 24 horas, con reinicio, saturación, pérdida, drenaje y alerta probados. Auditoría obligatoria por ruta durable propia.
- Registros y trazas sin secretos ni datos personales sensibles; saneamiento antes de emisión y en ingestión. La auditoría de negocio conserva su tratamiento y acceso específicos.
- Retención de eventos de seguridad: mínimo 12 meses en línea y 24 adicionales en archivo, sin confundirla con retenciones de diagnóstico o de auditoría del Caso.
- Evidencia WORM y prueba de resistencia a alteración; no afirmar que el destino temporal de Bastion es inmutable.
- Acceso del Cliente a tableros, exportación, reglas de síntomas de negocio, runbooks, turnos y seguimiento de incidentes.
- Soporte, licencias, versiones y actualizaciones para los 56 meses; Intune, Private Access, planes Defender y demás capacidades se identifican expresamente en T-11 y oferta económica.
- Residencia de datos y metadatos, regiones y destinos de respaldo declarados por producto; ninguna selección equivale a autorización de transferencia internacional.

## 10. Fundamento y verificación

Fuentes contractuales de lectura: [Bases Administrativas](../../00_Bases/Bases_Administrativas.md), Arts. 21–23; [Bases Transversales](../../00_Bases/Bases_Transversales.md), RT-03.05, RT-03.10/16/18, RT-04.12, capítulos 11, 12 y 14 y RT-16.06–10; [Caso 09](../../00_Bases/Caso_09_Cadena_Multitienda.md), separación de negocios y precisiones del capítulo 15 sobre cifrado, terminales y perfiles. Este documento no crea nuevos requisitos ni modifica el catálogo oficial.

Documentación técnica consultada durante la conversación el 22-10-2026:

- [QR en Entra](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-qr-code): método de un factor.
- [Modo compartido](https://learn.microsoft.com/en-us/entra/identity-platform/msal-shared-devices): integración de aplicaciones y administración de equipos.
- [Workload Identity en AKS](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview): identidad federada de cargas.
- [Gestión de claves Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/key-management-choose): funciones distintas de Key Vault y Managed HSM.
- [Grabación de Bastion](https://learn.microsoft.com/en-us/azure/bastion/session-recording): Premium, limitaciones y restricciones del destino inicial.
- [Ingestión del Collector en Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/collect-use-observability-data): recorrido documentado en vista previa, retirado como base de esta selección.
- [Collector y Loki](https://grafana.com/docs/loki/latest/send-data/otel/): ingestión de registros por OTLP.
- [Collector y Tempo](https://grafana.com/docs/tempo/latest/set-up-for-tracing/instrument-send/set-up-collector/otel-collector/): ingestión de trazas por OTLP.
- [Prometheus y OpenTelemetry](https://prometheus.io/docs/guides/opentelemetry/): receptor OTLP HTTP y configuración.
- [Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/fundamentals/notifications/): agrupación y notificaciones.
- [Blackbox Exporter](https://github.com/prometheus/blackbox_exporter): sondas de endpoints y protocolos.
- [Persistencia del Collector](https://github.com/open-telemetry/opentelemetry.io/blob/main/content/en/docs/collector/resiliency.md): colas y recuperación ante fallas.

No se ejecutaron configuraciones, pruebas de integración, autenticación, carga, residencia o recuperación. No se modificaron el JSON, draw.io, imágenes, SD-04 ni formularios. La siguiente figura debe aplicar el catálogo y validación `diagramas-ancoa`; la validez de su trazado no acredita las garantías descritas.

## Declaración de uso de IA

Consolidación de contexto y especificación de conexiones con asistencia de Codex. Nivel de texto: Alto. No se generaron diagramas ni se registra revisión humana formal en esta entrega.
