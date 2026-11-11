# Costos (interno, no pasa al sd-04)

**Regla (decidida 2026-10-28):** aquí van las **partidas** y quién paga cada una, **sin precios**. Sirve para vigilar la coherencia entre arquitectura y costos (las Bases califican de «grave» la incoherencia). Los precios van en la oferta económica (Sobre 3). Al sd-04 pasa solo el **argumento de costo en palabras**, columna de `01_nodos.md`.
**Criterio rector (AGENTS.md):** presupuesto efectivamente ilimitado; el costo nunca decide una pieza ni baja la calidad. Se declara el costo aceptado para cumplir lo exigido.
**Siglas de quién paga:** O = Only Simple Solutions · C = Cliente · Op = operador de telecomunicaciones (contrato gestionado por O). Compra = pago único (CAPEX). Recurrente = pago periódico (OPEX), 36 meses de operación.

## Parte 1 · Sitios del Cliente (tiendas, centros, casa matriz)

Fuente: `cierre-inventario/12-matriz-suministro-costos.md`, partidas SUM-01 a SUM-33 (resumidas por grupo). Las cantidades son por tienda salvo que se indique.

| Grupo | Partidas | Qué se compra | Qué es recurrente | Quién paga | Nodo de `01_nodos.md` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Cableado y canalización | SUM-01 a 04 | Cable, tomas, paneles, fibra, ductos, etiquetas | Reparación y recertificación | O | Red de la tienda |
| Racks y gabinetes | SUM-05, 06 | 3 racks de 24U; gabinetes de acceso según estudio | Revisión y reposición | O | rack |
| Servidores de tienda | SUM-07 | 2 de Retail + 2 de Filial; 2 árbitros | Garantía, soporte, repuestos, energía | O | Servidores de Retail y de la Filial, árbitro |
| Enlaces de operador | SUM-08 | Alta e instalación | Renta de los enlaces y del equipo del operador | Op y C contratan; O gestiona | Acceso fijo A y B |
| Firewall y Wi-Fi | SUM-09 a 12 | 2 firewalls Retail + 2 Filial; puntos de Wi-Fi | Licencias, suscripciones, soporte | O | Firewall y red de la tienda |
| Energía y clima | SUM-15 a 22 | 2 UPS de 6 kVA, tableros, bypass, ATS y generador si la fuente del edificio no basta | Mantención, pruebas, combustible | O (equipos); C (obra civil y edificio) | Batería de respaldo (UPS) |
| Seguridad y operación | SUM-23 a 27 | Configuración de políticas, EDR, MDM, cofre de claves | Suscripciones, respuesta, auditoría | O | Firewall; copia local |
| Software y licencias | SUM-28, 29 | Implantación; licencias a nombre del Cliente | Suscripción y renovación durante todo el período | O paga; titular C | Servidores; copia local del Control de cruces |
| Operación y formación | SUM-30 | Transición y repuestos iniciales | 36 meses de operación, atención y reposición | O | Todos |
| Obra civil de separación | SUM-31, 32 | Particiones, puertas, permisos del inmueble | Conservación estructural | **C** | rack; sala técnica |
| Respaldo móvil 4G/5G | SUM-33 | Router, antena, alta (24 sitios: 22 tiendas + 2 centros) | Planes de datos del Cliente; soporte y reposición | O (equipo); C (planes) | Router de respaldo móvil |
| Copias locales | SUM-27 | Almacenamiento local separado por negocio | Verificación, custodia | O | Copia local cifrada |

**No hay precios, y no se estiman** desde metros cuadrados ni desde iconos (ficha 12). Brechas que bloquean la cotización: plano y permisos de cada tienda, padrón de dispositivos, estudio de Wi-Fi y de energía, generación disponible en el edificio, precios y vigencias de proveedores (ver `06_supuestos-pendientes.md`).

## Parte 2 · Nube (agregado 2026-10-28)

La ficha 12 no cubre Azure. Esta lista dice **por qué se cobra cada servicio**, no cuánto. La unidad de cobro es la forma general de facturación de cada servicio; se confirma con la calculadora de precios de Azure al cotizar. Cantidades de Tabla 4.20 del `.tex`.

| Servicio | Cantidad (Chile Central) | Se cobra por | Recurrente | Quién paga | Espera en Brazil South |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Nodos de AKS (máquinas virtuales) | 40 + 0 a 3 elásticos | Hora de máquina virtual; el clúster Standard suma una tarifa por hora | Sí | O (por el Cliente en la suscripción) | 40 nodos encendidos |
| Máquinas auxiliares y sondas | 12 + 2 | Hora de máquina virtual | Sí | O | 8 + 2 encendidas; 4 de Power BI apagadas |
| PostgreSQL Flexible Server | 12 servidores, 4.500 GiB | Hora de proceso, GiB de disco y de respaldo | Sí | O | Réplicas entre regiones |
| Service Bus Premium | 2 espacios | Hora por unidad de mensajería | Sí | O | Habilitado al conmutar; registro durable replicado |
| Azure Managed Redis | 16 GiB | Hora según tamaño | Sí | O | No |
| Almacenamiento (lago, evidencia, archivo) | Lago 5 TiB; evidencia 5 TiB; archivo 37 TiB | GiB al mes, operaciones y copia entre regiones | Sí | O | Copia explícita |
| Front Door Premium | 1 | Tarifa base por hora, datos transferidos y solicitudes | Sí | O | Segundo origen |
| Application Gateway | 1 por negocio | Hora y unidades de capacidad | Sí | O | 1 por negocio |
| API Management Premium | 1 instancia multirregión por negocio | Hora por unidad, por región | Sí | O | Gateway regional |
| Azure Firewall Premium | 3 | Hora por despliegue y GB procesados | Sí | O | Sí |
| VPN Gateway | 2 (Retail y Filial) | Hora según el nivel | Sí | O | No |
| Bastion y DNS Private Resolver | Por frente | Hora | Sí | O | Sí |
| Key Vault y Managed HSM | 1 por frente; HSM candidato | Operaciones por 10.000; Managed HSM por hora | Sí | O | Propio por frente |
| Registro y observabilidad | Log Analytics, Sentinel, Monitor | GB ingeridos y GB retenidos | Sí | O | Sí |
| Respaldo (Backup) | 1 bóveda por frente y región | GiB protegido | Sí | O | 2.ª bóveda |
| Entra ID P2 | Según usuarios | Usuario al mes | Sí | O | No aplica |
| **Tráfico entre Chile y Brasil** | Copia de PostgreSQL y almacenamiento | GB transferidos entre regiones | Sí | O | — |

**Dos costos que pesan por decisión de diseño, ambos aceptados:**
1. **Brazil South templado:** 50 máquinas de espera encendidas todo el contrato para cumplir el RTO de 4 h. Una pila apagada saldría más barata y no cumpliría.
2. **Servicios en tres zonas y copia entre regiones:** triplica algunos costos y agrega tráfico interregional. Se acepta por RT-03 y RT-07.

## Verificación contra la lista de precios oficial de Azure (2026-10-28)

Microsoft publica una interfaz pública y gratuita, la **API de precios minoristas** (`prices.azure.com/api/retail/prices`), que es la fuente de la calculadora. Se consultó para Chile Central (10.154 líneas, 60 servicios). Sirve para dos cosas: confirmar la **unidad de cobro** de cada servicio y comprobar que **existe en la región**. Los precios no se copian a este registro.

| Servicio | ¿Se vende en Chile Central? | Unidad de cobro confirmada |
| :--- | :--- | :--- |
| AKS, máquinas virtuales | Sí | Hora |
| PostgreSQL Flexible Server | Sí (series General Purpose y Memory Optimized) | Hora de proceso; disco y respaldo aparte |
| Service Bus Premium | Sí | Hora |
| API Management (Premium) | Sí | Hora |
| Azure Firewall (Premium) | Sí | Hora de despliegue y GB procesado |
| Application Gateway WAF v2 | Sí | Hora y unidades de capacidad |
| Azure Managed Redis | Sí (Balanced, Compute y Memory Optimized) | Hora |
| Container Registry Premium | Sí | Día; GB al mes |
| Backup | Sí | GB al mes; instancia protegida al mes |
| Key Vault y HSM | Sí (HSM Pool) | Por operación; HSM por hora |
| Azure Bastion, VPN Gateway | Sí | Hora |
| Log Analytics | Sí | GB ingerido; GB retenido al mes |
| Data Lake Storage Gen2 | Sí | GB al mes; operaciones por 10.000 |

**No aparecen en esa lista y se verifican aparte:** Front Door (servicio global, no se vende por región), Microsoft Sentinel, DNS Private Resolver y Entra ID. Que un servicio tenga precio en una región es evidencia fuerte de que se vende ahí, pero no reemplaza la comprobación en la suscripción del proyecto (Art. 16.3, disponibilidad regional).
**Brazil South:** ver sección final.

**Verificación ampliada (29-10, catálogo completo de ambas regiones):** en Chile Central también tienen precio Azure Managed Redis, Managed HSM («Key Vault HSM Pool»), Service Bus Premium, Azure Firewall Premium, API Management Premium, Container Registry Premium, VPN Gateway con zonas (VpnGw1AZ a 5AZ), DDoS Protection y Data Factory. **Microsoft Sentinel no tiene precio en Chile Central** y la documentación confirma que no lo admite (06, S-19): su costo va a Brazil South. **API Center no tiene precio en ninguna de las dos regiones** (06, S-15): su costo va a East US. DNS Private Resolver sigue sin aparecer por región (S-22).

## Pendientes
1. Precios, vigencias, garantías y unidades de licencia: la oferta económica los obtiene con cotizaciones (ficha 12, brechas).
2. Confirmar cada unidad de cobro de la Parte 2 con la calculadora de precios de Azure.
3. Reservas o compromisos de uso en Azure (ahorro por compromiso): decisión de la oferta económica, no del diseño.


## Brazil South (verificado 2026-10-28, lista de precios oficial)
Tienen precio en Brazil South: AKS, PostgreSQL, Service Bus, API Management, Azure Firewall, Application Gateway, Container Registry, Backup, Key Vault, Azure Bastion, VPN Gateway, Log Analytics, Sentinel y Azure Managed Redis (este último aparece bajo el servicio «Redis Cache»). No confirmados por este medio: Azure Front Door (servicio global), DNS Private Resolver y Private Link. Es evidencia fuerte de que se venden ahí, pero no reemplaza comprobarlo en la suscripción del proyecto.


## Tienda de laboratorio (D-FIS-17, 2026-10-29)
Suma una tienda tipo completa fuera de las 22 de Producción: 4 servidores, 2 árbitros, 3 racks, UPS y 2 accesos fijos más router 4G/5G (compra y operación). Sin precios aquí; se cotiza en la oferta económica. Por definir dónde se instala. Pagan Ancoa o el contratista según el reparto de suministro, como el resto de la tienda tipo (ver Parte 1).
