# Especificación de los diagramas físicos de SD-04 (figuras 4.13 a 4.19)

**Fecha:** 9 de octubre de 2026. **Estado:** estructura acordada; ninguna figura generada. **Propósito:** fijar, antes de dibujar, qué muestra cada figura de 4.2, 4.2.1, 4.3.1 y 4.3.2, con qué nodos, aristas e iconos, y qué supuestos la condicionan. Complementa la [especificación lógica](especificacion_diagramas_sd04.md), cuyos IDs de sitio (`SIT`, `CD`, `DC`, `CLD`, `EXT`) y de componente (`B-`, `I-`, `D-`, `A-`, `S-`, `O-`, `L-`, `R:`, `F:`, `X-01`) se reutilizan sin cambios.

## Decisiones que rigen todas las figuras

- **Nube Azure definitiva** (D-12 en [contexto SD-04](../../80_Artefactos/sd-04_contexto/contexto_sd-04.md); ADR-07 en `sd-04.tex`). CLD-01 = Azure Chile Central (`chilecentral`), CLD-02 = Azure Brazil South (`brazilsouth`). Iconos Azure reales; no se dibuja Google Cloud.
- **Broker decidido** (ADR-06, D-13): Azure Event Hubs Premium, icono `azure.analytics.EventHubs`, redundante entre zonas y con geo-replicación a Brazil South.
- **Gateway**: Azure API Management Premium clásico, con unidades en tres zonas de Chile Central y gateway adicional en Brazil South.
- **Línea roja Retail / Emisor**: en toda figura física, Retail y Filial emisora van en clústeres separados (suscripción, red y claves propias). Solo cruza el contrato X-01.
- **Ubicaciones actuales supuestas**: ERP/DTE, núcleo Retail 2009 y crédito 2011 en DC-01; WMS en CD-01; comercio electrónico, marketplace y fidelización externos (P-01 a P-09 de la [matriz de supuestos](../../80_Artefactos/sd-04_contexto/supuestos_plataformas_y_conexiones.md)). Se dibujan en ese sitio **sin marcas de incertidumbre sobre la caja**; la incertidumbre se explica en el texto y en el pie, según la [nota de ubicación documental](../../80_Artefactos/sd-04_contexto/ubicacion_documental_supuestos_plataformas.md).

## Convenciones gráficas

| Elemento | Representación | Origen de la convención |
| :--- | :--- | :--- |
| Enlace o relación en alcance | Línea sólida | Especificación lógica |
| Enlace, ruta o alojamiento por acreditar | Línea discontinua | Especificación lógica |
| Flujo prohibido o cerrado | Línea roja con cruz o rótulo «bloqueado» | Especificación lógica |
| Doble enlace acreditado por el Caso (8 tiendas de centro comercial, CD-01) | Doble línea azul | Nota de red actual |
| Enlace propuesto DC-01 ↔ DC-02 | Línea ámbar | Nota de red actual |
| Réplica de recuperación CLD-01 → CLD-02 | Línea discontinua verde con rótulo de RPO | Nueva |
| Ámbito Retail / Emisor | Clúster con borde de color distinto, nunca anidado uno dentro del otro | Línea roja del Caso |

Ninguna figura dibuja **tienda → CD → DC → nube** como cadena obligatoria (regla de la especificación lógica). Los rótulos usan los nombres del catálogo (RR-07). Texto legible a ≥ 9 pt impresos (RP-05): si una figura no cabe, se divide en partes (RR-12), nunca se recorta (RR-13).

## Producción y archivos

- **Fuente:** un generador único `04_Adjuntos/diagramas/diag-04-fisica_generar_mcp.py` (acepta números de figura para regenerar solo esas; ejecutar con `PYTHONUTF8=1`) y el DSL de cada figura guardado como `diag-04-NN_<titulo>-mcp.py.txt`. El `.drawio` conserva clústeres, rótulos y aristas, pero no los iconos.
- **Salida del MCP** (`generate_diagram`, `workspace_dir` = `04_Adjuntos/diagramas`): `diag-04-NN_<titulo>.png` y `.drawio` editable.
- **Incorporación:** copiar el PNG a `02_Propuesta/latex_final/figuras/` y citarlo en `sd-04.tex` con «Figura 4.NN: …» y fuente (RR-11, RR-14). Compilar solo con `exportar_latex.py`.
- **Numeración:** el número del archivo es el número de figura. Las figuras 4.1 a 4.12 corresponden a 4.1; 4.2 empieza en 4.13. Si se agrega o quita una figura, se renumeran archivo, maestro y `adjuntos.json` juntos.

## Mapa de figuras

| Figura | Sección | Archivo | Tipo (RR-12) | Requisito que satisface |
| :--- | :--- | :--- | :--- | :--- |
| 4.13 | 4.2 | `diag-04-13_arquitectura-fisica-general` | Vista general | C10 4.2: emplazamiento de cada componente en nube y on-premise (Art. 16) |
| 4.14 | 4.2 | `diag-04-14_red-y-segmentacion` | Parte | C10 4.2: redes; RT-03.17 enlaces redundantes; segmentación Retail/Emisor |
| 4.15 | 4.2 | `diag-04-15_ambientes-y-despliegue` | Parte | C10 4.2: ambientes Desarrollo, QA, Preproducción, Producción y DR |
| 4.16 | 4.2 | `diag-04-16_conexiones-y-contingencia` | Parte | C10 4.2: conexiones y puntos de falla con su contingencia |
| 4.17 | 4.2.1 | `diag-04-17_tienda-tipo` | Parte | C10 4.2.1: implementos a proveer; continuidad local 24 h |
| 4.18 | 4.3.1 | `diag-04-18_data-center-primario` | Parte | C10 4.3.1: proveedor, región, zonas, servicios y sitio on-premise |
| 4.19 | 4.3.2 | `diag-04-19_data-center-secundario` | Parte | C10 4.3.2: región de recuperación, réplica, RPO/RTO y conmutación |

La tabla de mapeo 3.3 → 4.1 → 4.2 que sugiere el maestro es una **tabla**, no una figura: va en el texto de 4.2 junto a la Figura 4.13.

---

## Figura 4.13 · Arquitectura física general (vista híbrida)

**Qué muestra.** Los ocho sitios de emplazamiento y los enlaces agregados entre ellos. Es el índice visual de 4.2: cada figura siguiente amplía uno de sus bloques.

**Nodos.**

| ID | Rótulo | Contenido dibujado | Icono |
| :--- | :--- | :--- | :--- |
| SIT-01 | 22 tiendas | POS nuevo, nodo local redundante (L-01/L-02/L-03); 14 en centro comercial (8 con enlace de respaldo) y 8 a la calle | `generic.place.Datacenter` (clúster) + `onprem.client.Client` |
| CD-01 | CD principal | Operación logística; WMS (P-06) | `generic.place.Datacenter` + `onprem.compute.Server` |
| CD-02 | CD Concepción | Captura estructurada de existencias; enlace único | `generic.place.Datacenter` + `generic.device.Tablet` |
| DC-01 | Centro de datos casa matriz (140 m²) | ERP/DTE (P-08), núcleo Retail 2009 (P-01), crédito 2011 (P-02); adaptadores in situ si se acredita | `generic.place.Datacenter` + `onprem.compute.Server` |
| DC-02 | Sala de respaldo (misma comuna) | Respaldo existente; función real por acreditar | `generic.place.Datacenter` |
| CLD-01 | Azure Chile Central | Bloques resumidos: borde, aplicación Retail, aplicación Emisor, integración, datos, analítica | `azure.network.VirtualNetworks` por bloque |
| CLD-02 | Azure Brazil South | Recuperación de cargas nuevas | `azure.migration.RecoveryServicesVaults` |
| EXT-01 | Contrapartes externas | Comercio electrónico, marketplace, fidelización (P-04/05/07), transportistas, medios de pago, proveedores, autoridades | `onprem.network.Internet` |

**Aristas.** SIT-01 → CLD-01 (sincronización y APIs, sólida; doble azul solo para las 8 tiendas acreditadas); CD-01 → CLD-01 (doble azul, dos proveedores); CD-02 → CLD-01 (sólida, enlace único); DC-01 ↔ CLD-01 (ExpressRoute propuesto, discontinua hasta acreditar); DC-01 ↔ DC-02 (ámbar, C-16); CLD-01 → CLD-02 (réplica, verde discontinua); EXT-01 ↔ CLD-01 (borde público, sólida).

**Supuestos que la condicionan.** P-01, P-02, P-06, P-08 (ubicación de hosts); C-16 (enlace entre centros); SUP-27 (22 tiendas en 11 regiones, ubicaciones supuestas de Illapel, Valparaíso, Talca y Frutillar).

**Falta para cerrarla.** Topología WAN real; si las tiendas salen a internet o a red corporativa; ubicación comprobada de ERP/DTE y WMS.

## Figura 4.14 · Red y segmentación

**Qué muestra.** Topología hub-and-spoke en CLD-01 y la conexión híbrida con los sitios del Cliente.

**Nodos.** Hub (`azure.network.VirtualNetworks`) con Azure Firewall (`azure.network.Firewall`), puerta de enlace ExpressRoute y VPN (`azure.network.VirtualNetworkGateways`), circuito ExpressRoute (`azure.network.ExpressrouteCircuits`) y DNS privado (`azure.network.DNSPrivateZones`). Borde público con Front Door y WAF (`azure.network.FrontDoors`) delante de API Management (`azure.integration.APIManagement`). Tres spokes: **Retail**, **Emisor** y **Plataforma compartida** (integración y operación). Cada spoke con tres subredes (`azure.network.Subnets`): borde/ingreso, aplicación (AKS) y datos (endpoints privados, `azure.network.PrivateEndpoint`).

**Aristas.** Internet → Front Door → APIM → spoke por ámbito; DC-01 → ExpressRoute → hub (con VPN como respaldo, discontinua); tiendas y CD → VPN/SD-WAN → hub; spoke Retail ↔ spoke Emisor **solo** vía firewall y contrato X-01; flujo directo Retail → datos Emisor dibujado como **bloqueado**.

**Supuestos.** RT-03.17 (enlaces redundantes); hoy solo 9 tiendas separan redes de cajas, administración, videovigilancia y clientes (hecho del Caso, nota de red actual), así que la segmentación de tienda es alcance nuevo.

**Falta para cerrarla.** Direccionamiento IP del Cliente; si el Cliente ya tiene circuito o proveedor de ExpressRoute; capacidad de enlaces por tienda.

## Figura 4.15 · Ambientes y despliegue

**Qué muestra.** Los cinco ambientes exigidos y el canal de entrega como código.

**Nodos.** Repositorio y pipeline (`azure.devops.Repos`, `azure.devops.Pipelines`), Terraform como etiqueta del pipeline, registro de imágenes (`azure.compute.ContainerRegistries`). Suscripciones (`azure.general.Subscriptions`) por ambiente: Desarrollo, QA, Preproducción, Producción y Recuperación ante Desastres; Producción y DR separadas además por ámbito Retail / Emisor. Key Vault por ambiente (`azure.security.KeyVaults`).

**Aristas.** Pipeline → Desarrollo → QA → Preproducción → Producción, con aprobación entre Preproducción y Producción; Producción → DR (misma definición de infraestructura, desplegada en Brazil South). Datos de producción del Emisor **no** fluyen a ambientes inferiores (bloqueado).

**Supuestos.** O-02 (entrega e infraestructura como código); reutilizar el canal CI/CD del Cliente si cumple revisión, firma y trazabilidad (Tabla 4.13).

**Falta para cerrarla.** Herramienta CI/CD definitiva (Azure DevOps o GitHub Actions) y política de datos de prueba.

## Figura 4.16 · Conexiones y puntos de falla

**Qué muestra.** Cada punto de falla y su contingencia, sobre la topología de la Figura 4.13 simplificada.

**Nodos y fallas.** Se marca cada punto de falla con un número y su contingencia al lado:

| N.º | Punto de falla | Contingencia que se dibuja |
| :--- | :--- | :--- |
| 1 | Enlace de tienda | Diario local y operación 24 h; reconciliación al volver (F-03, F-04) |
| 2 | Enlace CD-02 (único) | Captura local durable; enlace secundario propuesto |
| 3 | ExpressRoute DC-01 | VPN de respaldo |
| 4 | Zona de disponibilidad | Servicios zonales en otra zona de Chile Central |
| 5 | Región Chile Central | Conmutación activo-pasivo a Brazil South |
| 6 | ERP/DTE | Modalidad fiscal de contingencia aprobada y conciliación |
| 7 | WMS | Procedimiento de degradación por interfaz |
| 8 | Broker | Outbox en productores y relectura |

**Supuestos.** Los mismos de 4.13. La modalidad fiscal de contingencia y la decisión de crédito sin enlace siguen abiertas (pendientes de 4.1).

**Falta para cerrarla.** Prueba de corte por tienda y CD; mapa de las 14 interfaces.

## Figura 4.17 · Tienda tipo

**Qué muestra.** Los implementos de una tienda y su red interna, base del renglón de tienda del T-11.

**Nodos.** Cajas POS (`onprem.client.Client`) con periféricos (impresora fiscal, lector, terminal de pago como contraparte AS-08); terminales compartidas y móviles de sala (`generic.device.Tablet`, `generic.device.Mobile`); mesón Retail y mesón financiero en VLAN del Emisor; nodo local redundante ×2 (`onprem.compute.Server` o `generic.compute.Rack`) con caché L-01, diario L-02 y sincronizador L-03; switch (`generic.network.Switch`) con VLAN de cajas, administración, Emisor, videovigilancia y clientes; router/firewall (`generic.network.Firewall`) con enlace principal y de respaldo.

**Aristas.** POS → nodo local (operación L); nodo local → CLD-01 (sincronización A, al volver el enlace); mesón financiero → spoke Emisor sin pasar por el nodo local Retail.

**Supuestos.** P-03 (no se presume autonomía del POS actual); la autonomía de 24 h es requisito de la solución nueva. Dos variantes: tienda con enlace de respaldo y tienda sin respaldo (6 de centro comercial y Coyhaique, entre otras).

**Falta para cerrarla.** Inventario de hardware y periféricos por tienda; motor del nodo local; ensayo de 24 horas.

## Figura 4.18 · Data center primario

**Qué muestra.** La región Chile Central por dentro y su relación con DC-01 durante la convivencia.

**Nodos.** Región Chile Central como clúster con tres zonas de disponibilidad. En cada zona: nodos AKS (`azure.compute.KubernetesServices`) por ámbito. Servicios regionales o zonales: API Management Premium (3 unidades, una por zona), Event Hubs Premium (`azure.analytics.EventHubs`), PostgreSQL Flexible Server con HA entre zonas (`azure.database.DatabaseForPostgresqlServers`), Azure Cache for Redis (`azure.database.CacheForRedis`), Data Lake Gen2 por ámbito (`azure.storage.DataLakeStorage`), Power BI (`azure.analytics.PowerBiEmbedded`), Entra ID (`azure.identity.ActiveDirectory`), Key Vault, Azure Monitor y Log Analytics (`azure.monitor.Monitor`, `azure.monitor.LogAnalyticsWorkspaces`), copia de seguridad (`azure.migration.RecoveryServicesVaults`). DC-01 al costado con las plataformas conservadas.

**Aristas.** Primario ↔ espera de PostgreSQL entre zonas (sólida); AKS ↔ servicios por endpoint privado; DC-01 ↔ región por ExpressRoute (discontinua hasta acreditar).

**Supuestos.** API Management Premium clásico, porque los niveles v2 no están en Chile Central; Fabric completo no disponible en Chile Central; brecha física de DC-01 según informe 2024 no entregado.

**Falta para cerrarla.** Disponibilidad por servicio y nivel en Chile Central; inventario de DC-01.

## Figura 4.19 · Data center secundario y recuperación

**Qué muestra.** La recuperación activo-pasivo de los componentes nuevos en Brazil South y el papel de DC-02.

**Nodos.** Chile Central (activo) y Brazil South (pasivo) lado a lado; en Brazil South: AKS en espera o desplegable por IaC, réplica de lectura de PostgreSQL entre regiones, secundario de Event Hubs por geo-replicación, gateway secundario de API Management, almacenamiento con réplica, Key Vault y bóveda de respaldo. DC-02 con su enlace ámbar a DC-01. Rótulos de objetivo: **RTO ≤ 4 h, RPO ≤ 15 min** para servicios críticos (RT-07.04) y **conmutación ensayada dos veces al año**.

**Aristas.** Réplica por conjunto de datos CLD-01 → CLD-02 (verde discontinua, rotulada con su RPO); conmutación de tráfico por Front Door; datos del Emisor con réplica **condicionada** a aprobación de residencia (discontinua con rótulo); DC-01 ↔ DC-02 (ámbar, C-16).

**Supuestos.** Chile Central no tiene región emparejada automática, así que la réplica es diseño explícito por componente. Ninguna norma leída exige al Emisor un sitio de contingencia en Chile ([notas DR](../../80_Artefactos/sd-04_contexto/notas_dr_nube.md)), pero falta verificar su norma propia y la Ley 21.719. DC-02 no se supone suficiente como única recuperación por su riesgo común con DC-01.

**Falta para cerrarla.** Aprobación jurídica de residencia por conjunto de datos; procedimiento de promoción de Event Hubs, conmutación y retorno.

---

## Orden de trabajo sugerido

1. Figura 4.13, porque fija sitios y enlaces para el resto.
2. Figuras 4.18 y 4.19, que ya tienen texto en 4.3.1 y 4.3.2.
3. Figuras 4.14 y 4.17, que alimentan el T-11 y el inventario de hardware.
4. Figuras 4.15 y 4.16.

Las figuras finales quedan en la raíz de `04_Adjuntos/diagramas/`; se copian a `figuras/` al insertarlas en `sd-04.tex`. La aprobación del equipo se registra en la revisión humana del subdocumento.
