# L2 con columnas e iconos

El usuario pidió expresamente reemplazar la vista de cajas de texto por la composición de una imagen de referencia. La variante usa `estilo: L2` y `composicion: columnas_referencia`. No sustituye L2 clásico ni relaja sus reglas.

Por instrucción expresa del usuario del 21-10-2026, la plantilla elimina la columna Cliente y la franja amarilla de frontera. Conserva cinco columnas: Presentación, Negocios, Servicios, Integración y Eventos, Datos. Las ocho capas RT se identifican con sus números; Borde y Puerta de enlace están en Negocios, mientras Seguridad y Observabilidad son transversales.

Los códigos se conservan en JSON y se validan, pero no se imprimen en tarjetas ni en draw.io. Los conectores se anclan explícitamente al contorno. Usan segmentos ortogonales y codos cuando una recta tapa tarjetas o rótulos; los carriles agrupan recorridos por familia sin fusionar las autoridades de datos. Sus colores y significados están en `catalogo.json`: solicitud, persistencia, publicación, consumo y adaptación. Los controles de cruce permanecen en Seguridad y la bitácora en Datos, sin una banda amarilla.

Los carriles superiores de Integración quedan libres para el acceso directo de cada servicio a su repositorio. El bus no media las lecturas/escrituras. Los canales de eventos se dibujan debajo, separados por ámbito, con productores y consumidores explícitos. Outbox pertenece a cada productor; no se modela como caja central compartida. Las autoridades de persistencia de Búsqueda y POS/Fila se rotulan en Datos para evitar aristas que parezcan terminar en el bus. Las cajas de contratos se consolidan en la puerta de enlace. El cruce de compra Ventas–Originación se declara en el control transversal; no se dibujan líneas largas de política.

El ejemplo completo es `ejemplos/L2_capas_referencia.json`. Los grupos requeridos y los tipos de nodo admitidos se encuentran en `catalogo.json`, `estilos.L2.referencia`. Las coordenadas y la tipografía pertenecen a `scripts/render_capas_referencia.py`; la especificación no admite estilos libres. Cada componente conserva un icono, incluso cuando su selección está por acreditar. No se acepta un nodo `caja` sin icono en esta composición.

Los repositorios agrupados por área siguen bajo autoridad de cada servicio. Las cajas de contratos agrupan rutas de API y no son nuevos servicios o instancias. Retail y Emisor mantienen sus datos, contratos y credenciales separados. El catálogo sigue rechazando enlaces directos no permitidos entre ambos frentes.

El MCP conserva JSON, SVG, PNG, leyenda y draw.io. El SVG incluye los iconos como datos y no necesita acceso externo. El draw.io conserva tarjetas, textos, imágenes y conexiones como objetos editables; incluye anclajes de entrada/salida y puntos intermedios que conservan los recorridos revisados. La composición de entrega comprobada visualmente es la del SVG/PNG.

Para el PNG se requiere Inkscape. La salida de esta plantilla es un diagrama; no constituye un segundo renderizador de los subdocumentos T-7 ni compila la propuesta.


## Organización por productos de plataforma (figura 4.25)

La nueva referencia del usuario autoriza `composicion: columnas_organizadas`: seis columnas de capas 1–6, actores fuera de las ocho capas, bandas de ámbito Retail y Emisor y controles transversales 7–8. Borde y Puerta de enlace son columnas distintas. El control de cruces conserva una tarjeta gris, sin reintroducir la franja amarilla ni códigos visibles.

Cada producto se muestra con icono y nombre: Front Door Premium, Application Gateway v2, API Management Premium, AKS, Event Hubs Premium, PostgreSQL, Data Lake Storage Gen2, Power BI, Entra ID P2, Key Vault Premium, Managed HSM, Firewall Premium, DDoS Protection, OpenTelemetry, Azure Monitor y Network Watcher. Las selecciones por acreditar conservan asterisco. Front Door se muestra dos veces como rutas del mismo perfil, no como dos despliegues. Los repositorios agrupados conservan autoridad por servicio. La API del vendedor sigue la tabla 4.1 de SD-04.

El icono OpenTelemetry procede de `https://raw.githubusercontent.com/cncf/artwork/main/projects/opentelemetry/icon/color/opentelemetry-icon-color.png`; aplica la política de marcas del repositorio CNCF artwork. Managed HSM usa el icono de familia Key Vault y se identifica por nombre; no se confunde su recurso con una bóveda Key Vault.

El ejemplo es `ejemplos/L2_capas_organizadas.json` y la plantilla `scripts/render_capas_organizadas.py`. Conserva anclajes explícitos y codos iguales en SVG/draw.io. Las familias de integración externa se enumeran en Adaptadores y en la banda de sistemas, evitando aristas largas que atraviesen otro ámbito. No constituye un inventario de contratos aprobado ni acredita disponibilidad regional.


### Franjas de capas y declaración de redes (22-10-2026)

Por solicitud del usuario, la composición organizada delimita con fondos tenues las seis columnas y las dos bandas transversales. Esos fondos indican alcance lógico, no perímetros de VNet. Las bandas de ámbito identifican las VNets de Producción y subredes de SD-04; un recuadro inferior de identificación de despliegue declara Hub, Retail, Emisor y Base tecnológica, con CIDR, suscripción propia, ausencia de peering directo Retail–Emisor y tránsito autorizado por el hub/control de cruces. No dibuja topología física adicional ni crea una novena capa. Front Door global, accesos privados PaaS y componentes locales no se atribuyen a una VNet por su posición en una columna. Se conserva la política de denegación y las validaciones pendientes del diagnóstico.


Revisión posterior del usuario (22-10-2026): retirar el bloque final de segmentación y el detalle de CIDR/subredes visibles. Conservar las franjas de capas y los ámbitos Retail/Emisor con red y suscripción propias. Esta presentación sustituye el recuadro inferior; no altera el diseño de red de SD-04.


Revisión posterior del usuario (22-10-2026): mostrar un solo símbolo de Front Door, Application Gateway y API Management, con las columnas de borde y gateway continuas; los ámbitos se distinguen por franjas de color. Es agrupación gráfica por producto, no una instancia física común ni modificación de la segmentación o de SD-03/04. Se mantienen contratos, destinos y permisos propios de cada ámbito.


Revisión del usuario (22-10-2026): sustituir Application Gateway por la conexión directa Front Door Premium → Azure Private Link/Private Endpoint administrado → API Management. El endpoint usa un icono pequeño sobre el enlace, sin tarjeta de gateway. APIM se rotula con nivel y modo de red por validar: no se hereda la compatibilidad del Premium clásico interno anterior ni se elige v2 sin validar región, salida privada a AKS y recuperación. Se preservan franjas de ámbito y anclajes de borde; no se modifica SD-03 ni se declara despliegue.


## Revisión del registro D-01–D-56 (22-10-2026)

Nueva composición L2 `columnas_decisiones`, autorizada por la imagen y registro aportados por el usuario. Mantiene máximo 85 nodos, ocho capas y validación de autoridad Retail–Emisor. Dos perfiles Front Door, dos Application Gateway en capa 3, dos APIM Premium clásico y API Center por ámbito; buses Service Bus separados. Capacidades de innovación dentro de sus servicios y continuidad local en capas 4/5/6. Capas con seis fondos tenues y puntos de ámbito; nodos sin contrato se mantienen para inventario, sin inventar aristas. Conserva fuentes anteriores. Plantilla `scripts/render_decisiones_20261022.py`; ejemplo en la figura 4.27 generada. No actualiza subdocumentos ni declara decisiones pendientes como aprobadas.

Revisión final del usuario: agrupar Mercadería, Venta, Relación con el cliente y Crédito dentro de capa 4, dejando las plataformas externas en esa misma capa y los traductores en capa 5. Mostrar un único símbolo Front Door que representa los perfiles separados de D-11, con rutas por host/ámbito. No incorporar F:C-04 solo porque aparezca en la referencia organizativa. Ejemplo: `ejemplos/L2_decisiones_20261022.json`.


## Revisión de legibilidad (figura 4.28)

Composición `columnas_legibles`, solicitada el 22-10-2026: un símbolo por producto de entrada y conectores agrupados al borde de las áreas. Los grupos area_mercaderia, area_venta, area_clientes y servicios_e pueden ser extremos de enlaces solo en esta composición; no representan nuevos servicios. Sus contratos individuales se conservan en el inventario de la figura 4.27. Cada producto agregado mantiene las instancias por ámbito del registro, sin afirmar una instancia compartida. Los elementos de operación sin enlace son funciones de software y repositorios; hardware, VM y emplazamiento se reservan a la vista física. Plantilla: scripts/render_capas_legibles.py. Ejemplo: ejemplos/L2_flechas_legibles.json.

Revisión del usuario, figura 4.29: más conectores al contorno de las áreas y puertos en cualquier borde, incluidos inferiores. El selector prueba rectas y un codo antes del enrutado por obstáculos; las cinco innovaciones identifican su servicio responsable en la tarjeta, sin flechas decorativas de pertenencia. Plantilla columnas_legibles; router_puertos_libres.py con selector router_bordes.py. Conserva contratos, trece servicios, separación de ámbitos y un símbolo por producto.


## Iteración horizontal aprobada (figura 4.30)

El usuario aprobó el plan de franjas horizontales el 22-10-2026. Composición L2 `bandas_horizontales`: conserva las ocho capas y el máximo de 85 componentes; sin fila de actores (corrección expresa del usuario), tecnologías/gobierno al lado izquierdo y sistemas externos en panel derecho. Servicios por áreas, un símbolo por producto de entrada y separación por ámbito. Retira Data Lake y añade PostgreSQL analítico dedicado por ámbito, alimentado por Service Bus y procesadores de proyecciones; BI no consulta bases operacionales. Commons queda pendiente como componente separado, sin contratos inventados. Backup Vault/Arc se trasladan al detalle físico/operativo; coordinación es responsabilidad de Integración. Plantilla render_bandas_horizontales.py; ejemplo L2_bandas_horizontales.json. Las validaciones de región, capacidad y residencia no se acreditan por el dibujo.


## Integración de capa 4 y flujo de entrada (figura 4.31)

La revisión solicitada el 22-10-2026 integra capacidades comunes de base tecnológica, los patrones A/C/E/P por servicio como propuesta y F:C-04 como candidato explícito. Usa la variante `bandas_horizontales`, plantilla `render_horizontal_capa4.py`, sin actores. Las capas 1–6 se conservan horizontales y 7 Seguridad/8 Observabilidad pasan a franjas verticales. Canales públicos → Front Door → origen Private Link → Application Gateway → APIM; internos → acceso privado corporativo en Borde → Application Gateway → APIM. Un símbolo por producto conserva instancias separadas por ámbito. El acceso privado no crea un gateway API nuevo. Fuentes y evidencia quedan en un registro separado, fuera de los rótulos del dibujo, por instrucción del usuario. Las capacidades pendientes no acreditan cumplimiento ni aprueban alcance. Ejemplo `L2_capacidades_comunes.json`. La figura anterior mantiene su plantilla para reproducibilidad.


## Revisión de Datos y capas transversales (figuras 4.33–4.35)

El usuario pide aplicar los dos registros del 22-10-2026 y reunir las capas 7 y 8 en una sola banda Capas transversales. La vista principal conserva ocho responsabilidades lógicas, sin actores. El detalle se divide en otras dos vistas L2 dentro del mismo draw.io para respetar el máximo de 85 nodos. La nueva selección reincorpora ADLS Gen2 y separa analítica, gobierno, modelos y archivo. Los productos de Seguridad/Observabilidad se desglosan con sus conexiones en el detalle, sin convertir el resumen en una instancia compartida. Plantilla `scripts/render_revision_registros.py`; las figuras anteriores conservan sus plantillas.

Iconos añadidos: bibliotecas diagrams y logos oficiales de OpenMetadata (`openmetadata-ui/src/main/resources/ui/public/logo192.png`) y OpenSearch (`project-website/assets/brand/SVG/Mark/opensearch_mark_default.svg`). Conversión de formato con Inkscape sin modificar la marca. Managed HSM conserva el icono de familia Key Vault; Blackbox usa el icono de Prometheus. Disponibilidad regional, residencia, capacidad y pruebas quedan pendientes.


## Corrección de composición compacta (figura 4.36)

Solicitud expresa del usuario: una banda vertical izquierda Capas transversales, resumida y sin carriles visuales Retail/Filial. Datos se representa con círculos, iconos y etiquetas inferiores agrupados por áreas de microservicios, siguiendo la imagen adjunta. La agrupación es visual: se conserva el mapeo a repositorios e instancias propios y a sus contratos. El catálogo incorpora la presentación datos_circulares y el resumen de productos transversal; no se permiten formas libres desde JSON. Plantilla render_compacto_20261022.py. Las figuras anteriores siguen reproducibles.
