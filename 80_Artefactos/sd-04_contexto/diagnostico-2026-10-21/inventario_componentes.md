# Inventario extraído de SD-04

Extracción literal de tablas en `main@1e097c2`. Los nombres se conservan para detectar diferencias; no son decisiones nuevas. Véase [procedencia](fuentes.md).

## Servicios y autoridades — Tabla 4.2

| Línea SD-04 | Fila original (celdas separadas por /) |
|---|---|
| 177 | R:M-01 / Servicio de oferta comercial / Artículos, precios, promociones, vigencias y publicación. / No reserva existencias. |
| 178 | R:M-02 / Servicio de abastecimiento / Órdenes, transferencias y recepción coordinada. / El WMS conserva la ejecución física. |
| 179 | R:M-03 / Servicio de existencias / Movimientos conciliados, conteos, reservas y disponible comprometible. / El ERP/DTE conserva el asiento contable. |
| 180 | R:V-01 / Servicio de pedidos / Estado único, promesa, asignación y seguimiento. / No ejecuta la preparación del almacén. |
| 181 | R:V-02 / Servicio de ventas / Venta, pago, reversa y conciliación de caja. / El ERP/DTE es el único emisor tributario. |
| 182 | R:V-03 / Servicio de comisiones / Regla y base de atribución. / El ERP/DTE conserva las remuneraciones. |
| 183 | R:V-04 / Servicio de marketplace / Reglas de vendedores y coordinación. / Se integra con la plataforma de marketplace de 2022, que se conserva. |
| 184 | R:CL-01 / Servicio de posventa / Caso y destino de devolución. / El reintegro al disponible queda sujeto a inspección. |
| 185 | R:CL-02 / Servicio de clientes Retail / Identificación, preferencias y gobierno de los datos de puntos, segmentos y campañas. / El sistema de fidelización de 2017 los opera mientras se mantiene e integra. |
| 186 | F:C-01 / Servicio de originación de crédito / Solicitud, evaluación, cupo y autorización. / Confirma la apertura solo cuando el servicio de evidencia financiera acredita la entrega previa. |
| 187 | F:C-02 / Servicio de cartera de crédito / Cuenta, saldo, pago, mora, cobranza y repactación. / Su migración se realiza por olas. |
| 188 | F:C-03 / Servicio de evidencia financiera / Versiones precontractuales, aceptación, firma y expediente. / No decide crédito. |
| 189 | X-01 / Servicio de control de cruces / Fichas, políticas, decisiones y bitácora del intercambio. / No almacena perfiles unificados. |

## Unidades técnicas candidatas — Tabla 4.3

| Línea SD-04 | Fila original (celdas separadas por /) |
|---|---|
| 202 | R:M-01 / Catálogo de artículos, precios, promociones y publicación. / Por decidir / Se evalúan dos microservicios por reglas y carga de cambios distintas. |
| 203 | R:M-02 / Órdenes y coordinación de reposición. / Microservicio / Tiene autoridad propia y el WMS conserva la ejecución física. |
| 204 | R:M-03 / Movimientos, reservas, disponible, conteos y ajustes. / Microservicio / Es transaccional para preservar la promesa de existencias. |
| 205 | R:V-01 / Estado, promesa y coordinación de pedidos. / Microservicio / Conserva el estado del pedido y el WMS ejecuta la preparación y el despacho. |
| 206 | R:V-02 / Venta, pago, reversa y conciliación. / Microservicio / El POS es canal y el ERP/DTE emite los documentos. |
| 207 | R:V-03 / Reglas y base de comisiones. / Módulo / Puede extraerse si las mediciones lo justifican y el ERP/DTE conserva las remuneraciones. |
| 208 | R:V-04 / Gobierno e intercambio con marketplace. / Módulo / Puede extraerse si las mediciones lo justifican y la plataforma de marketplace de 2022 permanece. |
| 209 | R:CL-01 / Expediente de posventa e inspección. / Microservicio / Tiene reglas y autoridad propias del caso. |
| 210 | R:CL-02 / Identidad, preferencias y gobierno de los datos de fidelización. / Microservicio / Tiene autoridad propia y el sistema de fidelización de 2017 opera los datos mientras se mantiene. |
| 211 | F:C-01 / Originación, decisión y autorización. / Microservicio / Preserva el cupo y el plazo de respuesta. |
| 212 | F:C-02 / Cartera, pagos, cobranza y repactación. / Microservicio / Se separa por migración y operación. |
| 213 | F:C-03 / Evidencia y consentimiento financiero. / Microservicio / Se separa por custodia y retención. |
| 214 | X-01 / Gobierno de políticas y bitácora de cruces. / Microservicio / Aplica las políticas en ambos extremos y tiene su propio almacén de datos. |

## Destino de plataformas — Tabla 4.4

| Línea SD-04 | Fila original (celdas separadas por /) |
|---|---|
| 233 | ERP/DTE / Se conserva. / Contabilidad, remuneraciones y única emisión tributaria. / DC-01. |
| 234 | WMS / Se conserva. / Ubicaciones, preparación y despacho, con extensión a Concepción por evaluar. / CD-01. |
| 235 | Marketplace / Se conserva. / Plataforma de terceros y liquidaciones. / Externo. |
| 236 | Comercio electrónico / Se integra inicialmente. / Conservación, remediación o sustitución tras pruebas. / Externo. |
| 237 | Fidelización / Se integra inicialmente. / Destino posterior sujeto a pruebas. / Externo. |
| 238 | Núcleo Retail / Se reemplaza. / Por olas conciliadas. / DC-01. |
| 239 | Crédito de 2011 / Se reemplaza. / Por olas de cartera y funciones. / DC-01. |
| 240 | POS 2014 / Se sustituye. / Tienda por tienda. / Terminales en tienda. |
| 241 | Motor de precios y promociones / Se construye. / Capacidad nueva dentro del Servicio de oferta comercial. / No aplica. |

## Tecnologías y estado — Tabla 4.6

| Línea SD-04 | Fila original (celdas separadas por /) |
|---|---|
| 433 | Nube / Microsoft Azure, con Chile Central primaria y Brazil South secundaria. / Condicionada. / Google Cloud en Santiago y São Paulo, descartada por ADR-07. / Servicios por región, residencia y alianza acreditable. |
| 434 | Servicios de aplicación / Java 25 LTS (Oracle, 2026) y Spring Boot 4 (Spring, 2025) para APIs y lógica transaccional. / Por probar. / Ninguna otra evaluada todavía. / Comparar con otro marco soportado y medir desempeño, competencias y ciclo de actualización. |
| 435 | Interfaces nuevas / TypeScript y React para portales y vistas POS. / Por probar. / Ninguna otra evaluada todavía. / Prototipo del modo local y los periféricos del POS antes de fijar su empaquetado. |
| 436 | Microservicios propios / Contenedores en Azure Kubernetes Service (AKS). / Por probar. / Ninguna otra evaluada todavía, y AKS es un servicio administrado conforme a RT-03.05. / Validar zonas, aislamiento por entidad, escalado y recuperación en Brazil South. |
| 437 | Eventos / Azure Event Hubs Premium, un espacio de nombres por ámbito, redundante entre zonas, con geo-replicación a Brazil South y clientes Kafka. / Condicionada. / Kafka en AKS exige operación propia y Service Bus no conserva historial para relectura. / Probar orden por partición, duplicados y promoción. |
| 438 | Entrada API / Azure API Management Premium clásico, una instancia por ámbito, con unidades en tres zonas y gateway adicional en Brazil South. / Condicionada. / Los niveles v2 no están en Chile Central ni admiten multirregión. / Validar políticas, cuotas, identidad y versionado. |
| 439 | Adaptadores / Componentes propios en contenedores o cómputo administrado. / Por probar. / Ninguna otra evaluada todavía. / Probar compatibilidad, error y conciliación con cada plataforma conservada. |
| 440 | Datos transaccionales / Azure Database for PostgreSQL Flexible Server, con aislamiento por contexto. / Condicionada. / Ninguna otra evaluada todavía. / Probar alta disponibilidad entre zonas, réplica a Brazil South y capacidad del nivel escogido. |
| 441 | Caché / Azure Managed Redis, solo para datos reconstruibles de Retail. / Por probar. / Azure Cache for Redis se retira el 30 de septiembre de 2028 (Microsoft, 2026q), y Valkey queda como alternativa por evaluar. / Verificar su disponibilidad en Chile Central y el nivel antes de fijarlo. |
| 442 | Búsqueda / Por decidir en la Etapa 1. / Pendiente. / Elastic Cloud y OpenSearch. / Decidir tras probar permisos, linaje y disponibilidad regional. |
| 443 | Analítica / Azure Data Lake Storage Gen2 y Power BI, con entornos Retail y Emisor separados. / Por probar. / Fabric completo no está disponible en Chile Central (Microsoft, 2026e). / Seleccionar el motor analítico de Azure tras probar permisos y linaje. |
| 444 | Identidad y secretos / Microsoft Entra ID federado con el directorio del Cliente, Azure Key Vault y, para la filial emisora, Managed HSM. / Por probar. / Ninguna otra evaluada todavía. / Confirmar la identidad existente y sus protocolos antes de fijar la federación, y la disponibilidad de Managed HSM en la región. |
| 445 | Telemetría / OpenTelemetry y Azure Monitor. / Por probar. / Ninguna otra evaluada todavía. / Verificar observabilidad conjunta de nube, centro de datos y tiendas. |
| 446 | Infraestructura y entrega / Terraform y canal CI/CD con registro de artefactos y despliegue auditado. / Por probar. / Reutilizar el canal del Cliente. / Reutilizarlo si satisface revisión, firma y trazabilidad. |
| 447 | Tienda desconectada / Nodo local redundante con diario transaccional y sincronizador. / Por probar. / Valkey u otro motor local, por decidir. / Fijar motor y empaquetado tras inventario de hardware, periféricos y ensayo de 24 horas. |

## Sitios — Tabla 4.8

| Línea SD-04 | Fila original (celdas separadas por /) |
|---|---|
| 512 | SIT-01 / 22 tiendas, POS, impresoras y lectores, diario y sincronización local. / Inventario por tienda, enlaces y 24 horas de continuidad con retorno. |
| 513 | CD-01 / Distribución principal, con operación física y WMS conservado. / Equipos, red y ubicación real del WMS. |
| 514 | CD-02 / Distribución Concepción, con operación logística y enlace actual único. / Segundo enlace, funcionalidad requerida y eventual conexión al WMS. |
| 515 | DC-01 / Centro de datos de casa matriz, 140 m², compartido por Retail y la filial emisora. / Inventario de plataformas, diferencias respecto del estándar y enlaces a la nube. |
| 516 | DC-02 / Sala de respaldo del Cliente en la misma comuna que DC-01. / Capacidad, dependencias comunes con DC-01 y función real en recuperación. |
| 517 | CLD-01 / Azure Chile Central, región primaria con aplicación, datos y analítica separados por ámbito. / Zonas, producto disponible, redes privadas, residencia y capacidad. |
| 518 | CLD-02 / Azure Brazil South, región secundaria para recuperar las cargas nuevas. / Réplica por dato, aprobación de residencia, RTO y RPO, y cambio de región ensayado. |
| 519 | EXT-01 / Transportistas, medios de pago, marketplace y proveedores. / Contrato, protocolo, ubicación y límite de responsabilidad de cada contraparte. |

## Componentes físicos — Tabla 4.13

| Línea SD-04 | Fila original (celdas separadas por /) |
|---|---|
| 666 | Servicios Retail: R:M-01 a R:M-03, R:V-01 a R:V-04, R:CL-01, R:CL-02 y portales / RT-09.02, RT-03.02 / AKS Retail, subred de aplicación de CLD-01 / Usuario: 6 × D8ds_v5 (8 vCPU / 32 GiB), hasta 12. Sistema: 3 × D4ds_v5 (4 vCPU / 16 GiB) / Activo-activo en 3 zonas, 3 réplicas por servicio; uso de 62 \% en el peak y 93 \% con una zona caída |
| 667 | Modelos predictivos de conteo y merma / RT-18.03 / AKS Retail, grupo de nodos propio / 0 a 2 × D8ds_v5, escala a cero / Sin redundancia: no está en la ruta de la venta |
| 668 | Servicios del Emisor: F:C-01 a F:C-03 y su portal / RT-09.02, RT-03.02 / AKS Emisor, subred de aplicación / Usuario: 3 × D4ds_v5, hasta 6. Sistema: 3 × D4ds_v5 / Activo-activo en 3 zonas; 54 \% en el peak y 81 \% con una zona caída |
| 669 | X-01 y adaptadores / RT-11.01, RT-03.05 / AKS de la base tecnológica / Usuario: 3 × D8ds_v5, hasta 6. Sistema: 3 × D4ds_v5 / Activo-activo en 3 zonas; 44 \% en el peak y 66 \% con una zona caída |
| 670 | Bitácora de cruces de X-01 (FR-02) / RT-05.03 / PostgreSQL Flexible Server, subred de datos de la base tecnológica / D2ds_v5 (2 vCore / 8 GiB); disco Premium SSD de 128 GiB y 500 IOPS / Activo-pasivo: primario en Z1 y espera en Z2 con copia síncrona |
| 671 | Datos transaccionales de Retail / RT-05.02, RT-07.04 / PostgreSQL Flexible Server, nivel De uso general / D8ds_v5 (8 vCore / 32 GiB); disco Premium SSD de 2 TiB y 7.500 IOPS / Activo-pasivo entre Z1 y Z2; réplica asíncrona en CLD-02 |
| 672 | Datos transaccionales del Emisor / RT-05.02, RT-07.04 / PostgreSQL Flexible Server, nivel De uso general / D4ds_v5 (4 vCore / 16 GiB); disco Premium SSD de 512 GiB y 2.300 IOPS / Activo-pasivo entre Z1 y Z2; réplica en CLD-02 si se aprueba la residencia |
| 673 | Caché de oferta y disponibilidad / RT-09.02 / Azure Managed Redis, ámbito Retail / Balanced B5, 6 GB / Primario y réplica en zonas distintas |
| 674 | Registro de eventos / RT-07.03 / Event Hubs Premium, un espacio por ámbito / Retail 2 unidades de procesamiento; Emisor 1 / Tres copias entre zonas; geo-réplica a CLD-02 con retraso menor a 15 min |
| 675 | Entrada de API / RT-11.11 / API Management Premium clásico / 3 unidades por instancia, 2 instancias; 1 unidad de gateway en CLD-02 / Activo-activo en 3 zonas |
| 676 | Entrada privada de cada ámbito / RT-11.07 / Application Gateway v2, subred de entrada / 2 a 10 instancias con escalamiento automático por ámbito / Activo-activo entre zonas |
| 677 | Borde público / RT-11.07, RT-11.12 / Front Door Premium con firewall de aplicaciones web / Un perfil global / Puntos de presencia múltiples; origen secundario en CLD-02 |
| 678 | Control de tráfico entre ramas / RT-03.04 / Azure Firewall Premium en el hub / Escalamiento automático del servicio / Activo-activo en 3 zonas |
| 679 | Túneles de tiendas y centros / RT-03.21, RT-03.24 / FortiGate-VM en la subred SD-WAN / 2 × Standard_F4s_v2 (4 vCPU / 8 GiB), licencia VM04, para 240 Mbps cifrados / Activo-pasivo en Z1 y Z2 |
| 680 | Conexión con DC-01 / RT-03.17, RT-03.21 / Puertas ErGw1AZ y VpnGw2AZ en GatewaySubnet / Circuito ExpressRoute de 200 Mbps y VPN de respaldo / Activo-pasivo: ExpressRoute principal y VPN de respaldo |
| 681 | Analítica Retail y del Emisor / RT-05.05 / Data Lake Storage Gen2 y Power BI / Retail 1 TB a tres años; Emisor 0,1 TB / Redundancia de zona (ZRS) |
| 682 | Evidencia financiera (F:C-03) / RT-07.11 / Blob Storage con inmutabilidad, ámbito Emisor / 9 TB al cierre del contrato / Redundancia de zona; copia en CLD-02 si se aprueba la residencia |
| 683 | Caché, diario y sincronizador de tienda (L-01 a L-03) / RT-03.10, RT-03.14 / Nodo local de cada tienda de SIT-01 / 2 × (4 núcleos / 16 GB / 2 SSD de 480 GB en RAID 1) por tienda, 44 en total / Activo-pasivo entre los dos nodos; cada uno tolera la falla de un disco |
| 684 | Identidad, claves y secretos / RT-12.01, RT-11.09 / Entra ID P2, Key Vault Premium y Managed HSM del Emisor / Una bóveda por ambiente y ámbito / Servicios zonales administrados; bóveda propia en CLD-02 |
| 685 | Observabilidad y seguridad / RT-03.16, RT-11.14 / Azure Monitor, Log Analytics y Sentinel / Un área de trabajo por ámbito, retención de 12 meses / Servicio administrado |
| 686 | Entrega continua / RT-04.05 / Agentes administrados y Container Registry Premium / 2 agentes D4ds_v5; un registro / Registro replicado a CLD-02 |
| 687 | Respaldo / RT-07.09 / Backup Vault en CLD-01 y en CLD-02 / Una bóveda por ámbito y región / Copia inmutable y política 3-2-1-1-0 |

## Responsabilidad de suministro — Tabla 4.15

| Línea SD-04 | Fila original (celdas separadas por /) |
|---|---|
| 749 | Tienda / Especificación, configuración y certificación del nodo local con dos servidores, más el software del POS nuevo, el diario y el sincronizador. / Adquisición de los servidores, y terminales, impresoras, lectores y redes existentes. |
| 750 | Red de sitio / Especificación, configuración y certificación de la pila de switches y el par de FortiGate, incluida la segmentación de las trece tiendas que hoy no la tienen. / Adquisición e instalación de ese equipo, enlaces de proveedores y obras civiles. |
| 751 | Nube / Suscripciones, servicios Azure, configuración y operación. / Directorio de usuarios del Cliente, con el que se conecta el acceso a la solución. |
| 752 | Centro de datos de casa matriz (DC-01) / Habilitación del recinto técnico con su especificación, equipos, conectividad, seguridad y canalizaciones de cableado, más su configuración y certificación. / Espacio físico del recinto, la instalación del recinto y la obra civil de separación. |
| 753 | Centros de distribución (CD-01 y CD-02) / Especificación, configuración y certificación del equipo de red de ambos centros. / Adquisición de ese equipo, obras y enlaces. |
| 754 | Sala de respaldo (DC-02) / Software de adaptadores y configuración de la conexión privada. / Sala, sus equipos y la contratación del enlace. |
| 755 | Plataformas conservadas e integradas / Adaptadores, que son traductores entre los sistemas nuevos y los actuales, e integración. / Licencias y hardware de ERP/DTE, WMS, marketplace y fidelización. |

## Innovaciones presentes en T-11 y T-14

SD-04 debe incorporar estas capacidades sin contarlas automáticamente como nuevos servicios funcionales.

| Paquete EDT | Innovación | Producción | Evidencia |
|---|---|---|---|
| 1.10.1 | Lockers Ancoa 24/7 | M21 | SD-13 97–131; T-11 554; T-14 447 |
| 1.10.2 | Conteo cíclico predictivo | M16 | SD-13 135–173; T-11 555; T-14 448 |
| 1.10.3 | Búsqueda vectorial multimodal | M21 | SD-13 177–215; T-11 556–557; T-14 449 |
| 1.10.4 | Retail Media Network | M21 técnico, activación comercial condicionada | SD-13 219–257; T-11 558; T-14 450 |
| 1.10.5 | Modo Tienda con fila virtual de probadores | M21 | SD-13 261–299; T-11 559–564; T-14 451 |
