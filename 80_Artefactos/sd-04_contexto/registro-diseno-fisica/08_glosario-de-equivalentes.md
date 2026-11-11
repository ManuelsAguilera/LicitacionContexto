# Glosario de equivalentes

Para qué sirve: los IDs y siglas del inventario integral son solo para uso interno de Claude. En el texto y en los diagramas se usa el **nombre legible**, que se explica solo para alguien que no es informático. Aquí se registra cada equivalente para mantener la consistencia. Se consulta antes de nombrar cualquier elemento y se actualiza al crear uno nuevo.

Columnas: **ID interno** (solo Claude) · **Nombre legible** (lo que se escribe o dibuja) · **Qué es, en una frase** · **Dónde se usa** (T = texto, D = diagrama) · **Estado**.

## Reglas de nombres (aprobadas por el usuario el 2026-10-28)

1. **Siglas del inventario:** nunca en texto ni en diagramas. Se reemplazan por el nombre legible de este glosario.
2. **Productos de Azure y de terceros:** en los **diagramas** se rotula solo con el **nombre del producto** (por ejemplo «Azure Firewall»). Su función se explica en la **redacción**, la primera vez que aparece, con la forma «función (producto)», por ejemplo «el guardia de la red (Azure Firewall)».
3. **Términos que las Bases exigen** (RPO, RTO): se escribe el término de las Bases seguido de su explicación, por ejemplo «RPO (pérdida de datos aceptable)».
4. **Frentes:** el espacio propio de Retail, de la Filial emisora y de Control de cruces se llama **«frente»**, como define el SD-03. «Área» queda reservada para lo que el SD-03 llama área (mercadería, venta, relación con el cliente y crédito). El `.tex` del SD-04 usa «ámbito» (160 veces); cambiarlo en el texto final se decide más adelante.
5. **Los nombres de sitios** siguen el vocabulario del propio Caso 09 cuando existe (por ejemplo «centro de distribución principal»).

Estado `propuesto` = lo propuse yo, falta que el usuario lo acepte o lo cambie. `aprobado` = el usuario lo aceptó expresamente.

## Sitios y regiones

| ID interno | Nombre legible | Qué es, en una frase | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| SIT-xx (SIT-01 = tienda 1, SIT-02 = tienda 2, …) | Las 22 tiendas | Las tiendas de Ancoa; se dibuja una como modelo y se indica que se repite 22 veces | T, D | **aprobado** |
| CD-01 | Centro de distribución principal | El centro de distribución mayor de Ancoa, en la Región Metropolitana, con enlace redundante (nombre tomado del Caso 09) | T, D | **aprobado** |
| CD-02 | Centro de distribución de Concepción | El segundo centro de distribución, hoy con un solo enlace (nombre tomado del Caso 09) | T, D | **aprobado** |
| DC-01 | Centro de datos de casa matriz | La sala de servidores de la casa matriz de Ancoa | T, D | **aprobado** |
| DC-02 | Sala de respaldo de casa matriz | Sala del Cliente en la misma comuna que el centro de datos; no sirve como sitio de recuperación porque cae junto con él | T, D | **aprobado** |
| CLD-01 | Azure Chile Central | La región de Azure en Santiago donde corre la operación diaria | T, D | **aprobado** |
| CLD-02 | Azure Brazil South | La región de Azure en São Paulo que guarda una copia y toma el relevo si Chile falla | T, D | **aprobado** |
| EXT-01 | Contrapartes externas de Ancoa | Transportistas, medios de pago, marketplace y proveedores | T, D | **aprobado** |

## Áreas y conceptos

| ID interno | Nombre legible | Qué es, en una frase | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| R | Retail | El negocio de tienda | T, D | **aprobado** |
| F | Filial emisora | El negocio de crédito, con régimen jurídico distinto al de la tienda | T, D | **aprobado** |
| X-01 | Control de cruces | El servicio que autoriza la única conexión permitida entre Retail y Filial: una compra con la tarjeta de crédito | T, D | **aprobado** |
| ámbito | Frente | Cada uno de los tres espacios propios, con sus datos, identidades, redes y claves: Retail, Filial emisora y Control de cruces. Término definido en el SD-03 («tres frentes, según el régimen jurídico y de datos de cada uno») | T | **aprobado** (2026-10-28; reemplaza «área», que en el SD-03 designa una sección dentro de un negocio) |
| RPO | RPO (pérdida de datos aceptable) | Cuánto tiempo de operaciones se acepta perder tras una falla (hasta 15 minutos) | T | **aprobado** |
| RTO | RTO (tiempo máximo detenido) | Cuánto puede estar detenido un servicio (hasta 4 horas) | T | **aprobado** |

## Productos de Azure que ya aparecen en el texto vigente

En diagramas va solo el producto. En la redacción va «función (producto)». Las funciones están tomadas de las definiciones que ya tiene el `.tex`.

| ID interno | Nombre en diagrama | Función para el texto | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| hub y ramas | Red central (hub) y redes por función (spokes) | La red central por donde pasa todo lo que entra a Azure y las redes de aplicación y de datos que cuelgan de ella | T, D | pendiente de nombre |
| Azure Firewall | Azure Firewall | El guardia de la red: revisa lo que sale del área y lo que llega de los sitios | T, D | aprobado el criterio |
| VPN Gateway | VPN Gateway | El extremo de los túneles: punto de Azure donde terminan las conexiones cifradas de tiendas, centros y casa matriz | T, D | aprobado el criterio |
| Front Door | Azure Front Door | La recepción pública: entrada de los clientes por Internet, con filtro contra ataques | T, D | aprobado el criterio |
| AKS | Azure Kubernetes Service (AKS) | La plataforma donde corren los programas nuevos | T, D | aprobado el criterio |
| PostgreSQL | PostgreSQL | La base de datos de cada negocio | T, D | aprobado el criterio |

Los 79 componentes lógicos y los nodos del inventario integral se agregarán aquí al volcarlos en la sección 9 del registro y en `01_nodos.md`.

## Tienda tipo (agregado 2026-10-28)

| ID interno | Nombre legible | Qué es, en una frase | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| SIT-xx-R-01/02 | Servidores de Retail de la tienda | Dos computadores en la tienda: uno trabaja y el otro lo reemplaza si falla; guardan las ventas aunque no haya internet | T, D | **aprobado** |
| SIT-xx-F-01/02 | Servidores de la Filial de la tienda | Igual, para el negocio de crédito; solo usan permisos de compra emitidos antes de la caída | T, D | **aprobado** |
| SIT-xx-X-LOCAL | Copia local del Control de cruces de la tienda | Copia del Control de cruces que vive dentro de los servidores de la Filial y autoriza compras a crédito sin internet | T, D | **aprobado** |
| testigo / quorum | Árbitro de los servidores de la tienda | Equipo liviano que desempata: decide cuál de los dos servidores del par manda, para que no manden ambos a la vez | T, D | **aprobado** (reemplaza «testigo») |
| R-POS | Cajas | Terminales de caja, impresoras y lectores | T, D | **aprobado** |
| F-TERM | Mesón de crédito | Terminales del negocio de crédito en la tienda | T, D | **aprobado** |
| SD-WAN | Firewall de la tienda | Equipo que separa los negocios y elige por qué enlace sale el tráfico | T, D | **aprobado** |
| SUM-33 | Respaldo móvil 4G/5G | Router celular de doble SIM, tercer camino si caen los dos accesos fijos | T, D | **aprobado** |
| UPS | Batería de respaldo (UPS) | Batería que mantiene los equipos encendidos en cortes breves | T, D | **aprobado** |
| rack | rack | Armario metálico donde se montan los equipos | T, D | **aprobado** |
| BKP | Copia local cifrada | Respaldo guardado fuera de los servidores, por negocio | T, D | **aprobado** |

## Red de Chile Central (agregado 2026-10-28)

| ID interno | Nombre legible | Qué es, en una frase | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| hub (NET-xx-H) | Red central | La red por donde pasa todo lo que entra y sale de un frente; como la plaza de la que salen las calles | T, D | **aprobado** |
| radio de aplicación (NET-xx-A) | Red de aplicaciones | La red donde viven los clústeres de un frente | T, D | **aprobado** |
| radio de datos (NET-xx-D) | Red de datos | La red donde llegan las bases de datos y la mensajería de un frente | T, D | **aprobado** |
| APIM | API Management | Control de las interfaces: quién las usa y cuánto | T (función), D (producto) | **aprobado** |
| AppGw | Azure Application Gateway | La puerta de cada negocio, con filtro contra ataques | T (función), D (producto) | **aprobado** |
| ILB | Balanceador interno de AKS | La puerta interna de cada clúster, sin IP pública | T, D | **aprobado** |
| DNS Private Resolver | DNS Private Resolver | Resuelve los nombres internos de cada frente | T (función), D (producto) | **aprobado** |
| Bastion | Azure Bastion | Acceso administrativo seguro, sin abrir puertos al público | T (función), D (producto) | **aprobado** |

## Cómputo y datos de Chile Central (agregado 2026-10-28)

| ID interno | Nombre legible | Qué es, en una frase | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| R-SYS/BIZ/INT/STATE/OPS, F-…, X-… | Clúster de AKS | El taller donde corren los programas de un frente; cada máquina es un nodo | T (función), D (producto) | **aprobado** |
| R-BI, F-BI, R-IR, F-IR, R-PA, F-PA | Máquinas virtuales de apoyo | Máquinas fuera del clúster que conectan Power BI, Data Factory y el acceso privado | T, D | **aprobado** |
| R-SYN, F-SYN | Sondas de vigilancia | Máquinas fuera del clúster que lo vigilan y avisan si falla | T, D | **aprobado** |
| REDIS-R | Memoria rápida (Redis) | Memoria que acelera las consultas de oferta; se reconstruye desde la base | T (función), D (producto) | **aprobado** |
| ADLS-R, ADLS-F | Data Lake | Almacén de datos para analítica, uno por negocio | T, D | **aprobado** (el usuario prefiere «Data Lake» a «lago de datos») |

## Entrega y ambientes (agregado 2026-10-28)

| ID interno | Nombre legible | Qué es, en una frase | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| ENV-DEV | Ambiente de Desarrollo | Entorno aislado donde el equipo construye y prueba cambios, con datos sintéticos | T, D | **aprobado** |
| ENV-QA | Ambiente de QA | Entorno de pruebas de calidad que reproduce los contratos entre frentes | T, D | **aprobado** |
| ENV-PRE | Ambiente de Preproducción | Entorno que reproduce la topología de Producción y donde se hace la prueba de carga | T, D | **aprobado** |
| ACR | Azure Container Registry | Registro privado de imágenes de contenedor, firmadas | T (función), D (producto) | **aprobado** |
| TF-STATE | Estado de Terraform | Archivo remoto y versionado que registra qué infraestructura existe | T, D | **aprobado** |

## Integración de datos en sitios propios (agregado 2026-10-29)

| ID interno | Nombre legible | Qué es, en una frase | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| DC-IR-R-01/02 | Nodos de integración de Data Factory de Retail en casa matriz | Dos máquinas con el Self-hosted Integration Runtime de Azure Data Factory, que leen las fuentes locales de Retail y envían a Chile Central | T, D | **aprobado** |
| DC-IR-F-01/02 | Nodos de integración de Data Factory de la Filial en casa matriz | Igual, transitorios, solo mientras se extrae el crédito de 2011 | T, D | **aprobado** |

## Nombres aprobados de los bloques 4 y 5 (2026-10-29)

| ID interno | Nombre legible | Qué es, en una frase | Dónde | Estado |
| :--- | :--- | :--- | :--- | :--- |
| BR-R/F/X-AKS | Clúster de AKS de cada frente en Brazil South | Clúster equivalente al de Chile, encendido y sin tráfico hasta la conmutación | T, D | **aprobado** |
| BR-R/F-IR, BR-R/F-PA | Máquinas virtuales de apoyo templadas | Las 8 máquinas de apoyo de Brasil, encendidas y sin tráfico | T, D | **aprobado** |
| BR-R/F-BI | Máquinas virtuales de BI apagadas | Las 4 máquinas de Power BI de Brasil, reservadas y apagadas hasta recuperar lo transaccional | T, D | **aprobado** |
| (D-FIS-15) | Punto privado de Azure Front Door | Punto de Private Link en Brazil South por el que Front Door llega al Application Gateway de Chile Central | T, D | **aprobado** |
| DC-01 | Centro de datos de casa matriz | Recinto propio de 140 m² con los sistemas conservados | T, D | **aprobado** |
| DC-02 | Sala de respaldo de casa matriz | Sala en la misma comuna; no es recuperación regional | T, D | **aprobado** |
| CD01-LOCAL, CD02-LOCAL | Nodos locales del centro de distribución | Par de servidores que guarda el diario durable de cada centro durante un corte de enlace | T, D | **aprobado** |
| CD-01, CD-02 | Centro de distribución principal / de Concepción | Los dos centros de distribución de Ancoa | T, D | **aprobado** |

## Nodos agregados por el mapeo (aprobados 2026-10-29)

| ID interno | Nombre legible | Qué es | Uso | Estado |
| :--- | :--- | :--- | :--- | :--- |
| SIT-xx-R-LCK | Controlador de lockers | Equipo del fabricante que abre los casilleros de retiro | T, D | **aprobado** |
| SIT-xx-R-TOT | Tótem de fila virtual | Equipo de autoatención del Modo Tienda | T, D | **aprobado** |
| EXT-ADS | Plataforma publicitaria | Tercero que sirve los resultados patrocinados de Retail Media | T, D | **aprobado** |
| DNS-PUB | Azure DNS público | Zonas públicas de cada negocio | T (función), D (producto) | **aprobado** |
| ADF | Azure Data Factory | Servicio que orquesta cargas y copias de datos | T (función), D (producto) | **aprobado** |
| BKP | Bóveda de respaldo | Almacén de copias de seguridad de cada frente | T, D | **aprobado** |
| PBI-CAP | Capacidad de Power BI | Capacidad Fabric de cada negocio en Chile Central | T, D | **aprobado** |
| IDX | Microsoft Entra External ID | Identidad de los clientes en los canales | T (función), D (producto) | **aprobado** |
| MDM | Microsoft Intune | Administración de dispositivos y terminales | T (función), D (producto) | **aprobado** |
