# Arquitectura física derivada de las decisiones lógicas

Fecha: 22-10-2026. Estado: propuesta de diseño para revisión del equipo. Sin recursos aprovisionados ni aceptación humana registrada.

La nueva arquitectura física abre la vista lógica 4.36 hasta sitios, equipos, redes, servicios administrados, clústeres, pools y servidores. Conserva los trece servicios, las cinco innovaciones y la VPN. La comparación se hizo con SD-04 de `main@1dfdbad`, cuya [copia de lectura](sd-04_main-1dfdbad.txt) conserva el texto que se revisó. No se modificaron los subdocumentos LaTeX.

La selección vigente se toma del [registro de Datos](../capa-datos_decisiones-y-precisiones_2026-10-22.md), los [cambios de Seguridad y Observabilidad](../capas-07-08_cambios-y-conexiones_2026-10-22.md) y el [contexto lógico consolidado](../contexto-arquitectura-y-cambios-logicos_2026-10-22.md). El registro de Datos sustituyó la retirada anterior del lago: ADLS Gen2, OpenSearch, OpenMetadata y MLflow Retail forman parte de la base revisada.

La entrega se organiza en una vista general y diez detalles dentro de un mismo [draw.io multipágina](../../../04_Adjuntos/diagramas/diag-04-37_arquitectura-fisica-completa.drawio). Esto permite abrir un sitio o recorrido sin mezclar todos los servidores con la topología general. Los estilos son F1–F5 de la guía Ancoa y mantienen sus límites de nodos.

## 1. Qué cambia respecto del diseño físico escrito

La sección 4.2 actual todavía dimensiona Event Hubs, presenta una plataforma compartida para adaptadores y operación, omite varios componentes nuevos de datos y no asigna servidores a toda la plataforma autogestionada. Sus tablas de capacidad no pueden mantenerse como resultado definitivo de la arquitectura revisada.

| Cambio | Estado previo en SD-04 | Tratamiento en esta propuesta |
| --- | --- | --- |
| Transporte de hechos | Event Hubs Premium, particiones y geo-réplica. | Service Bus Premium por ámbito; redimensionar MUs, colas/tópicos, consumidores, DLQ y recuperación. |
| Dominios de red | Un hub y una rama Base tecnológica compartida. | Proponer conectividad y operación separadas por ámbito; Frontera conserva solo X-01. |
| Entrada pública | Un perfil global Front Door. | Mantener perfiles propios Retail/Filial bajo un símbolo de producto en la general; recursos separados en el detalle. |
| Paso APIM→servicio | AKS sin abrir el balanceo de backend. | APIM interno → Standard Load Balancer interno → Service/VIP autorizado → pods sobre VMSS. |
| Presentación web | Alojamiento poco explícito. | Contenedores web privados por ámbito; App Gateway sirve la ruta web y envía las APIs a APIM. |
| Servidores AKS | Tres conjuntos con capacidad global anterior. | Pools separados de sistema, negocio, integración, plataforma de datos y observabilidad; batch Retail independiente. |
| Adaptadores | X-01 y adaptadores en la Base tecnológica. | Adaptadores Retail en su pool INT; adaptadores financieros en el pool INT de Filial; X-01 aislado. |
| PostgreSQL | Un servidor principal por ámbito y uno para X-01. | Proponer partición física por áreas y autoridad financiera, manteniendo bases lógicas/roles por servicio. |
| Analítica | ADLS y Power BI, sin motor de consulta cerrado. | PostgreSQL analítico dedicado, alimentación por trabajadores y ADLS, BI sin consultas operacionales. |
| Conexión privada de BI | Sin servidores de conexión identificados. | Proponer dos VM Windows con data gateway estándar por ámbito. |
| Acceso remoto administrativo | Private Access sin sus conectores. | Añadir dos VM Windows Private Network Connector por ámbito; su canal al servicio es saliente. |
| Procesamiento de datos | Trabajos y ejecutores no completos. | Data Factory separado de su runtime; pares SHIR en VM Windows y trabajadores Java/Spring sobre AKS. |
| Búsqueda | Producto global por elegir. | OpenSearch propio; pgvector aislado de Oferta; índice de catálogo separado y compatible. |
| Gobierno y modelos | Sin OpenMetadata/MLflow completos. | Alojar aplicaciones, dependencias y almacenamiento técnico; Python/scikit-learn en pool batch Retail. |
| Telemetría | OpenTelemetry y Azure Monitor como camino genérico. | Pools OPS, Collector, Loki, Tempo, Prometheus, Grafana, sondas y almacenamiento por señal. |
| Auditoría y archivo | Inmutabilidad concentrada en Filial. | Archivo propio por ámbito; distinguir evidencia, WORM, temporal Bastion, exportación y respaldo. |
| Conectividad de sitios | FortiGate-VM, Route Server, gateways VPN y ER coexistentes. | Proponer VPN Gateway AZ para IPsec; conservar FortiGate local y ER DC-01 por acreditar, sin duplicar terminadores cloud sin necesidad. |
| Cupo sin enlace | Mención al nodo de tienda y separación del mesón. | Abrir un par/VM aislado Filial con custodia propia; caducidad, doble gasto y fencing siguen pendientes. |
| Innovaciones en tienda | Tienda tipo sin todos sus equipos. | Añadir controlador/casilleros de lockers, tótem de fila, terminales y sus segmentos. |
| Recuperación financiera | Brasil condicionado y DC-02 como salida provisional. | Mantener pendiente un sitio independiente de DC-01; no declarar DC-02 suficiente. |
| Operación y costo técnico | Herramientas nuevas sin capacidad ni soporte. | Incluir servidores, discos/PV, HA, mantenimiento, respaldo y actualización durante 56 meses. |

Las nuevas particiones de PostgreSQL, los pools y los pares de gateway/IR son **propuestas físicas de esta iteración**, no decisiones anteriores ya aprobadas. Están dibujadas para evaluar una solución concreta. No se infieren SKU, presupuesto ni rendimiento por contar iconos.

## 2. Índice del conjunto de diagramas

Cada página identifica su alcance y conserva iconos, direcciones de conexión, puertos de contorno y leyenda.

| Figura | Qué abre | Archivo editable |
| --- | --- | --- |
| 4.37 | Personas, sitios, entrada Azure, ejecución y recuperación. | [General](../../../04_Adjuntos/diagramas/diag-04-37_fisica-general.drawio) |
| 4.38 | POS, periféricos, móviles, lockers, fila, video, nodos, switches y firewalls. | [Tienda](../../../04_Adjuntos/diagramas/diag-04-38_tienda-detallada.drawio) |
| 4.39 | Hubs, VNets, subredes, gateways, DNS, balanceadores y Private Endpoints. | [Red Azure](../../../04_Adjuntos/diagramas/diag-04-39_red-azure.drawio) |
| 4.40 | Nueve servicios Retail, pods y servidores VMSS por pool/zona. | [Ejecución Retail](../../../04_Adjuntos/diagramas/diag-04-40_ejecucion-retail.drawio) |
| 4.41 | Originación, Cartera, Evidencia y X-01, con sus servidores. | [Ejecución Filial/Frontera](../../../04_Adjuntos/diagramas/diag-04-41_ejecucion-filial-frontera.drawio) |
| 4.42 | PostgreSQL Retail, índices, lago, workers, SHIR y conexión BI. | [Datos Retail](../../../04_Adjuntos/diagramas/diag-04-42_datos-retail.drawio) |
| 4.43 | PostgreSQL Filial y bitácora X-01, evidencia y conexión BI. | [Datos Filial](../../../04_Adjuntos/diagramas/diag-04-43_datos-filial.drawio) |
| 4.44 | Identidad, administración, claves, colectores, señales y custodia. | [Seguridad y observabilidad](../../../04_Adjuntos/diagramas/diag-04-44_seguridad-observabilidad.drawio) |
| 4.45 | Servidores conservados de DC/CD y su integración. | [Sitios corporativos](../../../04_Adjuntos/diagramas/diag-04-45_sitios-corporativos.drawio) |
| 4.46 | Falla de enlace/zona/región, réplica y destino financiero pendiente. | [Recuperación](../../../04_Adjuntos/diagramas/diag-04-46_recuperacion.drawio) |
| 4.47 | Repositorio, imágenes, contratos y promoción por ambientes. | [Ambientes y entrega](../../../04_Adjuntos/diagramas/diag-04-47_ambientes-entrega.drawio) |

Los nombres `R-BIZ-01`, `F-INT-02`, `SIT-xx-R-01` y similares son identificadores de diseño. El inventario levantado deberá asignar recursos y cantidades por tienda. Una vista de pools representa la infraestructura que puede ejecutar réplicas; no una asignación permanente de todos los pods a una VM concreta.

## 3. Recorridos de extremo a extremo

Los recorridos siguientes fijan qué debe probarse en cada salto. Las respuestas pertenecen a la misma conexión iniciada; una réplica o relación de despliegue se distingue de una llamada de negocio.

### 3.1 Navegador o app pública

La API sigue cliente/titular → Front Door Premium del ámbito con WAF → conexión Private Link → Application Gateway privado del ámbito → APIM interno → VIP de un Service en el ILB de AKS → pod del servicio → endpoint privado del repositorio propietario. HTTPS se vuelve a negociar en los proxies que lo terminan. El balanceador L4 no sustituye autenticación ni políticas de APIM.

El frontend web tiene una ruta distinta después de Application Gateway, hacia su backend web privado. Sus llamadas de API vuelven al contrato de APIM; servir el HTML no exige pasar todo el contenido estático por una API de negocio. Ese alojamiento es propuesta y no modifica por sí solo el alcance de conservación del comercio electrónico.

El patrón App Gateway/APIM privado y la conexión interna de AKS están documentados por Microsoft. Se verificaron [protección de APIs](https://learn.microsoft.com/en-us/azure/architecture/web-apps/api-management/architectures/protect-apis), [APIM con AKS](https://learn.microsoft.com/en-us/azure/api-management/api-management-kubernetes) y [ILB de AKS](https://learn.microsoft.com/en-us/azure/aks/internal-lb). El número de gateways API del ámbito permanece en uno; el ILB distribuye conexiones a backends.

### 3.2 Caja, móvil o puesto interno

En línea, el terminal usa su VLAN y, si corresponde, AP corporativo → switches → contexto de firewall propio → VPN IPsec → VPN Gateway de Azure → rutas/firewall del ámbito → App Gateway → APIM → servicio. El mesón financiero usa rutas e identidad de Filial; no atraviesa el diario Retail.

Sin enlace, el POS confirma primero la operación durable en el nodo Retail. La réplica y el fencing local deben impedir dos primarios; el retorno usa las APIs autorizadas y concilia antes de confirmar el efecto. El cupo previo se consulta/consume solo bajo política de Filial. No se habilitan apertura o ampliación de cupo offline.

### 3.3 Compra con tarjeta propia

Ventas inicia la compra → entrada privada de X-01 → pod X-01 → endpoint privado del listener financiero permitido → App Gateway/APIM Filial → Originación. X-01 conserva su bitácora en `pg-x01`, sin ser un maestro de clientes. No existe ruta libre Retail→base financiera ni un bus entre negocios. El endpoint y la identidad de X-01 requieren reglas específicas de salida, entrada, nombres y certificados.

### 3.4 Datos y consulta BI

Los productores confirman su outbox con la operación. Productores y consumidores abren conexiones AMQPS hacia el PE de Service Bus de su ámbito. No se dibuja al broker abriendo una conexión nueva hacia pods privados. Los workers construyen proyecciones e índices; la reconstrucción usa corte, histórico autorizado y deltas.

Data Factory coordina y los SHIR ejecutan conexiones privadas hacia fuentes y APIs de trabajos. Los pares SHIR tienen VM Windows propias y canales de control salientes; no se reutilizan las VM del gateway BI. Microsoft documenta el [runtime autohospedado](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime) y la [Web Activity sobre red privada](https://learn.microsoft.com/en-us/azure/data-factory/control-flow-web-activity).

Power BI usa el clúster de data gateway del ámbito. Sus VM abren el canal saliente requerido por el servicio y consultan por PE únicamente PostgreSQL analítico. Este gateway es software de conexión de datos y no otra puerta de APIs. El [gateway estándar admite clústeres de alta disponibilidad y Windows Server](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-install); deben verificarse capacidad, conectores, residencia y salida de red.

### 3.5 Lockers y fila virtual

El controlador de lockers se ubica en un segmento IoT autorizado, aislado del cupo y de las bases. Mantiene el contrato de Pedidos, valida el retiro y registra el resultado; la definición de controlador, credencial, conectividad y contingencia sigue pendiente. Los casilleros/sensores no son servidores de Azure.

La fila virtual tiene tótem/cliente local y estado bajo Clientes Retail. La pérdida de un servicio publicitario, de búsqueda avanzada o entrenamiento no puede detener la venta ni corromper su diario. Debe probarse por separado qué puede hacer cada dispositivo sin enlace.

## 4. Dónde se ejecuta cada pieza

La [matriz de despliegue](matriz-despliegue.md) asigna los trece servicios y las capacidades técnicas. El [inventario de nodos](inventario-nodos.md) identifica los componentes dibujados. El [inventario de conexiones](relaciones-fisicas.md) permite comprobar cada flecha por número sin poner su evidencia en la figura.

La [cobertura lógica a física](cobertura-logica-fisica.md) asigna los 79 elementos de la figura 4.36 a una ubicación o pendiente explícito. La [matriz de rutas, puertos y segmentos](rutas-puertos-y-segmentos.md) precisa qué red y control intervienen en cada recorrido.

Retail y Filial tienen clústeres privados distintos. Esta iteración propone pools VMSS de sistema, negocio, integración, datos autogestionados y observabilidad, cada uno con nodos repartidos entre tres zonas. La separación evita que entrenamientos, índices o registros compitan sin límite con reservas, cobros o crédito. Las cantidades iniciales de tres nodos por pool dan una propuesta de topología; la capacidad, los mínimos de réplicas y los máximos dependen de las pruebas.

Los servicios corren en pods o módulos documentados sobre el pool BIZ, no en servidores dedicados por cada caja lógica. El scheduler decide el nodo respetando solicitudes de recursos, afinidad, dispersión y presupuesto de disrupción. Comisiones y Marketplace pueden continuar como módulos extraíbles. El plano de control AKS lo opera Microsoft; no se inventan tres VM maestras del proponente.

OpenSearch, OpenMetadata y el backend de catálogo tienen almacenamiento y permisos propios; MLflow y los Jobs Python/scikit-learn se limitan a Retail. El índice compatible del catálogo requiere cerrar versiones. Collector/Prometheus/Loki/Tempo/Grafana necesitan discos o Blob, retención, HA y restauración; seleccionar sus nombres no completa la operación.

Private Access es un servicio global y alcanza la red mediante `R-PA-01/02` o `F-PA-01/02`, VM Windows dedicadas propuestas. Los conectores abren los canales salientes; el servicio no inicia una conexión entrante hacia la VNet. Microsoft recomienda al menos dos conectores por grupo y exige excepciones a la terminación TLS en ese canal: [arquitectura de conectores](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-connectors), [puertos y configuración](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-configure-connectors).

La integración concreta de Private Access con Bastion queda sujeta a PoC de cliente, DNS, autenticación y auditoría. Bastion recibe HTTPS en 443 y alcanza los destinos por sus puertos administrativos autorizados. El [modo privado de Bastion](https://learn.microsoft.com/en-us/azure/bastion/private-only-deployment) y su [cliente nativo](https://learn.microsoft.com/en-us/azure/bastion/native-client) tienen restricciones distintas: el cliente nativo no graba sesiones. La copia de grabaciones a WORM solo aplica a recorridos compatibles; no se presenta esa combinación como resuelta. La sonda `R/F-SYN-01` se propone fuera del clúster supervisado, con ubicación y capacidad pendientes.

PostgreSQL Flexible Server es un servidor administrado. Se propone un recurso por área Retail y recursos distintos para Originación, Cartera, Evidencia, analítica y metadatos técnicos, además de `pg-x01` y pgvector aislado. Dentro de un servidor de área siguen existiendo bases/roles por autoridad. La partición física final debe comparar aislamiento de carga y fallo, mantenimiento, HA y recuperación; no se da por decidida porque el diagrama muestre un círculo.

## 5. Correcciones de representación y red exigidas por Azure

La guía de Microsoft pide separar niveles de detalle y representar con precisión la ubicación de PaaS y endpoints. Se aplicaron [las prácticas de diagramación](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams) y [los iconos oficiales](https://learn.microsoft.com/en-us/azure/architecture/icons/), sin cambiar sus colores o proporciones.

- Un Private Endpoint es una interfaz/IP dentro de una subred. PostgreSQL, Storage, Service Bus y otros PaaS no se convierten en VM alojadas allí. Se muestran fuera de la VNet y se conectan al PE correspondiente.
- Para PostgreSQL se propone el modo compatible con Private Link, con acceso público deshabilitado. No se mezcla con VNet Integration en el mismo servidor. Esa [restricción está documentada](https://learn.microsoft.com/en-us/azure/postgresql/network/concepts-networking-private-link).
- DNS privado debe resolver el FQDN correcto del backend, el hostname de APIM y los subrecursos de Storage. Resolver tiene endpoints/subredes propios; no se usa como proxy de datos ni se comparte su ruleset entre tenants. Véase [DNS Private Resolver](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview).
- NSG, UDR y NetworkPolicy son controles asociados a interfaces, subredes y pods. No son tres cajas de tránsito en serie. Las excepciones de plataforma y las rutas de retorno deben validarse, en especial APIM interno, VPN y Azure Firewall.
- Se retira la promesa de que todo tráfico entra por el firewall del hub. Front Door llega a su origen privado por el mecanismo del servicio; el tráfico híbrido y las salidas inspeccionadas tienen rutas propias.
- Los registros nuevos de red deben diseñarse como VNet flow logs. La [retirada de NSG flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-migrate) afecta al texto físico actual.

La documentación de [Private Link de Front Door](https://learn.microsoft.com/en-us/azure/frontdoor/private-link) consultada incluye Brazil South y no Chile Central. Permite alcanzar un origen de otra región por el backbone, con un salto regional adicional. Por eso el dibujo declara el tránsito; no coloca un PE gestionado de Front Door dentro de nuestra subred de aplicación ni promete residencia exclusivamente chilena. El [procedimiento para Application Gateway](https://learn.microsoft.com/en-us/azure/frontdoor/how-to-enable-private-link-application-gateway) distingue esa conexión del PE que un cliente crea en su VNet.

## 6. Cambios concretos al texto físico y a sus tablas

Las ubicaciones siguientes corresponden al contenido de `main@1dfdbad`. Se conservan los títulos obligatorios y se actualiza su contenido, sin copiar las líneas de una versión anterior.

| Ubicación | Modificación necesaria | Salida de revisión |
| --- | --- | --- |
| 4.2, supuestos de emplazamiento | Revisar sitio de Filial, equipos externos, hosts del legado y condiciones de nuevas innovaciones. | Inventario de sitios y supuestos vigentes. |
| 4.2, servicios contratados / Tabla 4.9 | Sustituir Event Hubs y completar Datos, seguridad, telemetría y conexión BI/ADF. | Cada producto con función, responsable, ubicación y recuperación. |
| Árbol de diecisiete suscripciones | Rehacerlo tras tenant, conectividad y custodia de Frontera. | No conservar una plataforma compartida que contradiga aislamiento. |
| 4.2, redes / Figura 4.14 / Tabla 4.10 | Añadir ILB, redes de pools, endpoints concretos, DNS y ruta X-01; revisar CIDR. | Plan IP sin solapes y matriz de rutas/puertos. |
| Túneles cloud FortiGate-VM y Route Server | Comparar su necesidad frente a VPN Gateway AZ por ámbito. | Retirar solo si el inventario y SD-WAN no los requieren. |
| Subred de datos genérica | Diferenciar PE de servicios PaaS, discos/PV y VM autogestionadas. | Ubicación físicamente correcta por recurso. |
| 4.2, ambientes / Figura 4.15 | Incorporar herramientas y dependencias en los cinco ambientes. | Aislamiento, datos de prueba e infraestructura reproducible. |
| HA y Tabla 4.12 | Rehacer fallos de broker, búsquedas, catálogos, telemetría, gateway BI e IR. | Efecto medido de cada fallo, sin garantías copiadas de Event Hubs. |
| Mapeo / Tabla 4.13 | Reemplazar totales globales por inventario y asignación servicio→pool/VM→datos. | SKU, cantidad, disco, IOPS, red, HA y propietario por nodo. |
| Dimensionamiento / Tabla 4.14 y memoria | Recalcular con innovaciones, históricos, índices, señales y replicas. | Una sola volumetría con fórmulas y márgenes. |
| 4.2.1 y Figura 4.17 | Añadir lockers/tótems/controladores, pares locales y separación financiera. | T-11 e inventario por tienda coherentes. |
| 4.3.1 y Figura 4.18 | Mostrar pools, nodos por zona y recursos PaaS reales. | Evidencia de disponibilidad del nivel/región y prueba de falla de zona. |
| 4.3.2 y Figuras 4.19/4.20 | Rediseñar recuperación completa de Retail y cierre del destino Filial. | Runbook, RPO/RTO, claves, conectividad y retorno probados. |
| T-11, T-12 y operación | Incluir herramientas autogestionadas, licencias, discos, soporte y controles. | Selección trazada sin declarar cumplimiento ejecutado. |

La antigua suma de CPU, memoria y discos no sirve para esta topología ampliada. El error aritmético y las diferencias entre primario, espera, DR, archivo y respaldo deben resolverse en una memoria única. No se mantienen máximos de escalado ni porcentajes de utilización como garantías sin incluir estas cargas.

## 7. Recuperación y decisiones que siguen abiertas

Service Bus ofrece una función de Geo-Replication de mensajes/estado distinta de Geo-Disaster Recovery de metadatos. Se verificó esa [distinción oficial](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-geo-replication). Su uso concreto requiere comprobar región, nivel y combinación de funciones; no se hereda la replicación de Event Hubs ni se declara RPO cumplido por elegirla.

La alternativa Retail mantiene Brazil South y propone capacidad preparada para reducir el riesgo de depender de la creación de todo AKS durante la contingencia. Hay que medir promoción de datos, disponibilidad de claves, broker, índices, gateway de datos, DNS y reconstrucciones. Los índices derivados pueden recuperarse de manera degradada, pero no debe perderse la autoridad de ventas/crédito.

Filial requiere un destino independiente aprobado y una pila recuperable completa. Un conjunto de servidores sin broker, claves, evidencia, red o identidad no es una recuperación operable. DC-02 comparte amenaza con DC-01 y no acredita por sí solo ese requisito. Los objetivos críticos siguen sujetos al ensayo integral y a la autorización de datos y metadatos.

| Pendiente | Qué debe producirse antes de cerrar |
| --- | --- |
| Tenant, residencia y tránsito | Aprobación expresa por recurso, incluido Front Door/Private Link, BI, ADF, soporte, metadatos y DR. |
| Topología R/F y X-01 | Custodia y administración, ruta mínima, firewalls/PE, contratos de frontera y denegaciones. |
| Inventario de sitios | Terminales, periféricos, lockers, UPS, enlaces, hosts del legado y responsabilidades de suministro. |
| Dimensionamiento | SKU regionales, nodos/mínimos/máximos, réplicas, PV, IOPS, MUs, retención y anchos de banda. |
| Gateway BI y SHIR | Compatibilidad de conectores, salidas permitidas, alta disponibilidad, credenciales y ubicación de ejecución. |
| Administración remota | Conectores Private Access, aislamiento por ámbito, PoC con Bastion y recorrido compatible con la auditoría/grabación exigida. |
| Estado autogestionado | Versiones, quórum/anti-afinidad, almacenamiento, actualización, copia y restauración de cada herramienta. |
| Continuidad local | Fencing, reloj, identidad, capacidad, cupo exclusivo/caducidad y conciliación sin doble gasto. |
| Recuperación Filial | Sitio y tecnología, copia íntegra autorizada, RTO/RPO y evidencia de independencia. |
| Prueba de extremo a extremo | Actor→terminal→red→API→pod→dato; latencia, falla, reintento, duplicados, permisos y retorno. |

## 8. Verificación y alcance de la entrega

Las especificaciones se validan mediante el MCP antes de generar cada lámina. La comprobación gráfica revisa contornos, rutas ortogonales, tarjetas y títulos; el draw.io multipágina conserva los mismos nodos y conectores que las vistas individuales. La revisión de contenido comprueba los trece servicios, la ausencia de despliegue de F:C-04, las cinco innovaciones y los límites de los dos negocios.

Los resultados y límites de las comprobaciones se conservan en `verificacion.json`. Esta entrega no ejecuta Terraform, despliega Azure, altera SD-03/SD-04 ni acredita capacidad. Las decisiones físicas nuevas se mantienen como propuestas revisables. No se ha realizado aceptación humana de la arquitectura.

El generador es `05_Gestion/scripts/generar_fisica_arquitectura_20261022.py`; el verificador es `05_Gestion/scripts/verificar_fisica_arquitectura_20261022.py`. El MCP validó once especificaciones. La exportación utilizó el motor oficial de draw.io en un navegador local sin acceso de red del proyecto; SVG y PNG proceden del mismo modelo editable. Se comprobaron 278 apariciones de nodos y 234 enlaces, incluidos puertos/rutas y ausencia de intersecciones con tarjetas o cabeceras. Eso no implica ausencia de cruces entre líneas ni sustituye una revisión visual de cada recorrido. El verificador sin argumentos comprueba la entrega y su geometría conservada; no depende de los renders temporales.

Uso de IA Alto en análisis y diagramas. Registrar en la declaración de SD-04 cuando se incorporen las nuevas figuras y tablas. La redacción se revisó para conservar nombres, estados y diferencias entre selección, propuesta y comprobación.
