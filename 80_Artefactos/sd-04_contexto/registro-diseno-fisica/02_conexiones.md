# 02 · Catálogo de conexiones

**Última actualización:** 2026-10-29. **Fuentes:** `inventario-fisico-integral-2026-10-23.md` sec. 14 (C01–C53, P01–P04); `cierre-inventario/02-red-cloud.md` (FL-01 a FL-12); `.tex` 4.2.4. Decisión D-FIS-15 aplicada a la entrada.

## Cómo leer este documento
- **Cada línea del diagrama grande lleva un número `E-NN` que remite a una fila de aquí.** El diagrama no muestra puertos ni protocolos; viven en esta tabla.
- La flecha indica quién inicia la conexión. La respuesta no cuenta como una conexión nueva.
- «ID interno» (C##, FL-##, P##) es solo para trazabilidad con el inventario integral; no se usa en el sd-04.
- «Si falla / contingencia» se completa en `04_continuidad.md` cuando dice «ver 04». Lo que aparece aquí viene de las fichas.
- Los puertos son los previstos por el producto; se confirman por endpoint al implementar. Esta es una matriz de diseño, no reglas de firewall.
- **Una conexión inexistente por diseño** cuenta tanto como una existente: no hay conexión Retail → bases de la Filial, ni peering entre las redes centrales de los tres frentes, ni acceso del cliente a AKS o PostgreSQL, ni de invitados o IoT a administración.

## A · Entrada pública (Internet → clústeres)

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-01 | Cliente → DNS público | DNS por el resolutor del cliente | — | Servicio global | Ver 04 | C01 | propuesto |
| E-02 | Cliente (Internet) → Azure Front Door | HTTPS (TCP 443) | TLS | Servicio global | Sin Front Door no hay entrada por Internet; ver 04 | C02, FL-01 | propuesto |
| E-03 | Azure Front Door → punto privado de Front Door en Brazil South (origen privado 1) | Private Link | Cifrado de la plataforma | Un punto por negocio | Si el clúster regional de Brazil South no responde, el tráfico sigue por E-03b; 06, P-05 | C03, FL-02 (D-FIS-15) | propuesto |
| E-03b | Azure Front Door → punto privado de Front Door en una segunda región admitida de las Américas (origen privado 2, prioridad menor) | Private Link | Cifrado de la plataforma | Un punto por negocio, región por medir | Respaldo del origen privado 1; mayor latencia | D-FIS-15 (A+) | propuesto; East US con prioridad 2 (S-03) |
| E-04 | Punto privado en Brazil South → Application Gateway del negocio (Chile Central) | Red privada entre regiones, HTTPS 443 | TLS | Una puerta por negocio | Conmutación a Brazil South solo por procedimiento y prueba de salud | FL-02 | propuesto |
| E-05 | Application Gateway → API Management del mismo negocio | HTTPS 443 | TLS | 1 por negocio | Ver 04 | C04, FL-03 | propuesto |
| E-06 | Application Gateway → balanceador interno del clúster (interfaz web) | HTTPS 443 | TLS | 1 por frente | No hay desvío hacia las APIs operacionales | C05, FL-04 | propuesto |
| E-07 | API Management → balanceador interno del clúster (APIs) | HTTPS 443, token e identidad | TLS | Multirregión por negocio | Ver 04 | C06, FL-03 | propuesto |
| E-08 | Balanceador interno → pods del servicio | Puerto del servicio | TLS según configuración | 3 réplicas mínimas por servicio, 3 zonas | Reinicio automático de pods | C07 | propuesto |

## B · Sitios propios hacia Chile Central (túneles privados)

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-09 | Firewall de la tienda → VPN Gateway del frente | IPsec/IKE (UDP 500/4500) por acceso fijo A | IPsec | 2 accesos fijos de operadores distintos (≥10 Mbps) | Pasa al acceso B | C08, FL-05 | propuesto |
| E-10 | Router de respaldo 4G/5G → VPN Gateway del frente | IPsec/IKE sobre red móvil (≥5 Mbps) | IPsec | Tercer camino por frente, prioridad a caja, mesón de crédito y Control de cruces | Conmutación automática desde los accesos fijos; retorno ensayado | C53 | propuesto |
| E-11 | Centro de distribución → VPN Gateway del frente | IPsec/IKE por dos accesos | IPsec | 2 operadores por sitio (Concepción hoy tiene uno; RT-03.17 exige segundo) | Diario local 24 h | FL-05 | propuesto |
| E-12 | Centro de datos de casa matriz → VPN Gateway del frente | IPsec/IKE, redes separadas Retail y Filial | IPsec | Dos rutas físicas cuando el sitio sea crítico | Ver 04 | C08–C09, FL-05 | propuesto |
| E-13 | VPN Gateway → Azure Firewall → entrada privada del frente | Tráfico privado autorizado, retorno simétrico | Dentro de la red privada | 1 por red central | Sin acceso libre a bases | C09 | propuesto |
| E-14 | DNS del sitio → DNS Private Resolver del frente | TCP/UDP 53 | — | 1 por frente | Zonas privadas separadas por frente | C10, FL-10 | propuesto |

## C · Datos y mensajería dentro de Chile Central

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-15 | Servicios del clúster → PostgreSQL del mismo frente | Punto privado, PostgreSQL TCP 5432 | TLS | Primario y espera en zonas distintas | Conmutación a la espera; ver 04 | C14, FL-06 | propuesto |
| E-16 | Servicios del clúster → Service Bus del mismo negocio | Punto privado, AMQPS (TCP 5671) | TLS | Premium, zonas | Mensajes esperan en cola | C15, FL-07 | propuesto |
| E-17 | Procesos de carga → Data Lake y Blob del mismo frente | Punto privado, HTTPS 443 | TLS | Redundancia de zona | Ver 04 | C16, FL-07 | propuesto |
| E-18 | Servicio de oferta → memoria rápida (Redis) / PostgreSQL con vectores | TLS del producto / TCP 5432 | TLS | Se reconstruye desde la base | Reconstrucción | C17 | propuesto; puerto de Redis por confirmar |
| E-19 | Aplicaciones → OpenSearch / catálogo de metadatos | API privada del producto | TLS | Instancia por frente | Ver 04 | C18 | propuesto |
| E-20 | Trabajos de conteo → Data Lake y MLflow | HTTPS / API privada | TLS | Sin redundancia (fuera de la ruta de venta) | Se reintenta | C19 | propuesto |
| E-21 | Cargas → Key Vault / Managed HSM del mismo frente | HTTPS 443 | TLS | Servicio zonal | Ver 04 | C31, FL-07 | propuesto |

## D · Cruce autorizado Retail → Control de cruces → Filial

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-22 | Servicio de ventas de Retail → entrada del Control de cruces | HTTPS privado, contrato `compra_autorizable` | TLS | 3 nodos de sistema y 3 de negocio, 3 zonas | Sin cruce no hay compra a crédito; ver 04 | C11, FL-08 | propuesto; entrada por Private Link Service o proxy por decidir (01, bloque 2) |
| E-23 | Control de cruces → entrada de autorización de la Filial | HTTPS privado, identidad propia del Control de cruces | TLS | 3 nodos de sistema y 3 de negocio, 3 zonas | Ver 04 | C12, FL-08 | propuesto |
| E-24 | Control de cruces → su base PostgreSQL | TCP 5432 | TLS | Primario y espera | Bitácora mínima, sin replicar maestros | C13 | propuesto |

## E · Tienda

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-25 | Caja → servidores de Retail de la tienda | API local, VLAN de cajas | Por definir | Par activo-espera | Sigue vendiendo hasta 24 h sin enlace | C22 | propuesto; protocolo por definir |
| E-26 | Servidor activo → servidor de espera (Retail y Filial por separado) | Protocolo cifrado por definir | Sí | Árbitro de la tienda (quórum y fencing) | Copia separada para recuperar de borrado o corrupción | C23 | propuesto |
| E-27 | Sincronizador local → entrada del frente en la nube | HTTPS por el túnel | TLS | Reintentos, idempotencia y conciliación | Diario local | C24 | propuesto |
| E-28 | Mesón de crédito → par de servidores de la Filial | API privada del frente, caducidad y no doble consumo | Sí | Árbitro de la tienda (quórum y fencing) | Sin enlace, el resultado mínimo pasa por la copia local del Control de cruces | C25 | propuesto |
| E-29 | Servicio local de Retail → copia local del Control de cruces | API local cifrada y autenticada | Sí | Dentro de los servidores de la Filial | Contrato mínimo de compra sin conexión | C46 | propuesto |
| E-30 | Copia local del Control de cruces → API local de la Filial | API cifrada del microsegmento propio | Sí | Dentro de los servidores de la Filial | Consume la reserva previa; no comparte el libro de la Filial | C47 | propuesto |
| E-31 | Copia local del Control de cruces → Control de cruces en la nube | HTTPS privado al recuperar el enlace | TLS | Reenvío idempotente | Bitácora separada de los diarios de Retail y Filial | C48 | propuesto |
| E-32 | Controlador de locker → servicio de Pedidos | API autenticada | Sí | — | Sin acceso directo a la base | C26 | propuesto |
| E-64 | Tótem de fila virtual → servicio de clientes de Retail | HTTPS por la entrada privada de Retail | TLS | — | Sin enlace, el personal atiende con registro local; se sincroniza después | H-22 | propuesto |
| E-33 | Cámaras IP → grabador local (NVR) | Protocolo del equipo, VLAN de video | — | 30 días de retención | Sin salida a datos de negocio | C49 | propuesto |
| E-34 | Invitados → Internet | Salida del SSID, firewall | — | — | Denegación de redes internas | C50 | propuesto |
| E-35 | Dispositivo/punto de acceso → autenticación del frente (AAA) | EAP-TLS | Sí | 2 instancias locales por frente | Revocación ensayada sin enlace | C51 | propuesto |
| E-36 | Administración → switches, puntos de acceso y SD-WAN | Canal de gestión por equipo, VLAN de administración | Sí | — | Identidad nominal; sin acceso desde invitados, video o IoT | C52 | propuesto |

## F · Integración y analítica

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-37 | Nodos de integración de Data Factory (casa matriz o Chile) → control de Data Factory y fuentes | Canal saliente soportado | TLS | Par de dos nodos | No hay administración libre de AKS | C27 | propuesto |
| E-38 | Gateway de Power BI → servicio de Power BI | Canal saliente soportado | TLS | Par por frente | Sin consulta entrante pública | C28 | propuesto |
| E-39 | Gateway de Power BI → PostgreSQL analítico del frente | TCP 5432 | TLS | Par por frente | Sin credenciales operacionales | C29 | propuesto |
| E-40 | Adaptadores → sistemas conservados | Contrato específico pendiente | Sí | — | Solo fuentes y operaciones autorizadas | C20 | **pendiente**: las 14 interfaces no están mapeadas (entrega del proyecto) |
| E-41 | Adaptadores → terceros (pagos, firma, proveedores) | HTTPS/API o transferencia pactada (HTTPS, mTLS, SFTP) | Sí | — | Firewall de salida; nunca ruta genérica a la Filial | C21 | propuesto |

## G · Identidad, administración y acceso

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-42 | Personas y cargas → Microsoft Entra ID | HTTPS 443 | TLS | Servicio global | Cuentas de emergencia por frente | C30 | propuesto |
| E-43 | Administrador → Entra y PIM → Azure Bastion → máquina del frente | HTTPS 443; SSH (TCP 22) o RDP (TCP 3389) solo en el último salto | Sí | 1 Bastion por frente | Sin SSH/RDP público | C32, FL-11 | propuesto |
| E-44 | Conector de acceso privado → servicio Entra Private Access | TLS 443 | TLS | Par por frente | No es garantía de acceso de emergencia | C33 | propuesto |
| E-45 | Máquinas y clústeres → Azure Firewall → Azure y terceros autorizados | HTTPS 443 con reglas por nombre | TLS | 1 firewall por frente | Reglas con dueño y caducidad | C45, FL-09 | propuesto |

## H · Observabilidad y seguridad

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-46 | Aplicaciones y agentes → recolector del frente | OpenTelemetry (OTLP), TLS | TLS | Buffer local | Sin datos personales | C34 | propuesto |
| E-47 | Recolectores → almacenes de métricas, logs y trazas | API según versión | TLS | — | Separados por señal | C35 | propuesto |
| E-48 | Grafana → almacenes / Azure Monitor | API autenticada | TLS | — | Solo el frente propio | C36 | propuesto |
| E-49 | Recursos y agentes → Log Analytics del frente en Chile Central | Configuración de diagnóstico y reglas de recolección | TLS | 1 espacio por frente | 12 meses en línea y 24 en archivo | C37 | propuesto |
| E-49b | Recursos y agentes → espacio con Sentinel del frente en Brazil South (solo tablas de seguridad, envío doble) | Configuración de diagnóstico con segundo destino | TLS | 1 espacio por frente | Si cae Brasil, el registro sigue completo en Chile; si cae Chile, Sentinel sigue con lo de Brasil. Transferencia internacional sujeta a aprobación (S-19) | C37 | propuesto; destino entre regiones a probar en la suscripción |
| E-50 | Sondas de vigilancia → Front Door, Application Gateway, API Management y API crítica | Protocolo de cada sonda | Sí | Fuera del clúster que vigilan | Una sonda caída alerta «sin señal», no salud falsa | C38 | propuesto |

## I · Entrega

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-51 | Pipeline o agente → Container Registry, Azure y clúster | HTTPS con acceso privado | TLS | Agentes efímeros, identidad por ambiente | Despliegue DEV → QA → PRE → PROD con aprobaciones | C39 | propuesto |
| E-52 | Nodos del clúster → Container Registry | HTTPS privado | TLS | Registro replicado en Brazil South | Imagen descargada por digest | C40 | propuesto |
| E-53 | Terraform → estado remoto del frente | Protocolo del backend elegido en IaC | Cifrado | Copia en Brazil South | Bloqueo para evitar dos `apply` | C41 | propuesto |
| E-53b | Canal de entrega y API Management de cada negocio → API Center del negocio en East US | HTTPS (API de Azure) | TLS | Servicio regional; contratos también versionados en el repositorio | Si falla, se publica igual desde el repositorio; no afecta a la venta. Solo metadatos de contratos (S-15) | C39 | propuesto |

## J · Recuperación entre Chile Central y Brazil South

| E | Origen → destino | Medio y protocolo | Cifrado | Redundancia | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E-54 | PostgreSQL de Chile → réplica en Brazil South | Réplica asíncrona del producto | Sí | Una por servidor (12, S-06) | Retraso medido; sobre 15 min no se promete el RPO | C42, FL-12 | propuesto |
| E-55 | Registros durables de productores y consumidores (con la réplica de PostgreSQL) → Service Bus de Brazil South, habilitado en la contingencia | Republicación desde un punto de recuperación; sin geo-replicación del namespace | Sí | Una por negocio | Consumidores toleran duplicados y descartan lo ya procesado | C42, FL-12 | propuesto; reformulado 06-11 (K-01) |
| E-56 | Almacenamiento de Chile → almacenamiento de Brazil South | Copia explícita (Chile Central no tiene región emparejada): Data Factory o AzCopy programados para los Data Lake; replicación de objetos para cuentas Blob sin espacio jerárquico (S-21) | Sí | Una por cuenta | Verificación de hash e inmutabilidad | C42, C44 | propuesto |
| E-57 | Claves y secretos de Chile → Brazil South | Key Vault: re-inyección por procedimiento, sin réplica automática. Managed HSM: replicación multirregión nativa (S-20) | Sí | Key Vault propio en Brasil; HSM activo en las dos regiones | Dominio de seguridad y quórum del HSM fuera de Chile | C42 | propuesto |
| E-58 | Front Door y sitios → entradas de Brazil South | HTTPS / túneles privados de recuperación | TLS | Origen de menor prioridad | Cambio solo tras puerta de salud completa | C43 | propuesto |
| E-59 | Respaldos → restauración autorizada | Mecanismo de cada recurso | Sí | Política 3-2-1-1-0 | Restaura también configuración y claves | C44 | propuesto |

## K · Energía (relaciones físicas, no IP)

| E | Origen → destino | Medio | Si falla / contingencia | ID interno | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E-60 | Generador o fuente del edificio → conmutador automático (ATS) | Cableado eléctrico | Capacidad de carga esencial y autonomía por acreditar | P01 | propuesto |
| E-61 | ATS / tableros → UPS rama A y B con bypass | Cableado eléctrico | Transferencia ensayada | P02 | propuesto |
| E-62 | UPS A y B → PDU A y B de cada rack | Cableado eléctrico (6 PDU por tienda, 2 por rack) | Mapa de circuitos | P03 | propuesto |
| E-63 | PDU A y B → fuente de cada servidor y equipo de red | Cableado eléctrico | Pérdida de una rama sin pérdida de servicio | P04 | propuesto |

## Pendientes
1. Mapa de las 14 interfaces con sistemas conservados (E-40 y E-41): entrega del proyecto, no se inventa.
2. Entrada del Control de cruces (E-22): Private Link Service sobre el balanceador interno, verificado en la documentación de AKS (S-11); el proxy queda como alternativa.
3. Puerto y protocolo de Redis (E-18), protocolo caja → servidor (E-25) y réplica activo-espera de tienda (E-26): por definir con el producto elegido.
4. La columna «Si falla» se completa en `04_continuidad.md`.
5. Falta la conexión de recuperación de Brasil con los sitios propios: cada tienda y centro tiene sus túneles a Chile, y en recuperación reconecta al VPN Gateway de Brazil South (E-58 la resume; el detalle por sitio está en 04).
