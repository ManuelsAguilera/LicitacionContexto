# Soporte físico · red, energía, ambiente y seguridad del emplazamiento

**Fecha:** 23-10-2026. **Estado:** diseño inicial para integrar. **Uso de IA:** Alto. Cantidades nuevas propuestas; no representan equipos encontrados, comprados ni instalados. Complementa las fichas [tienda](03-tienda.md) y [DC/CD](05-dc-cd-externos.md). Los espacios y recursos conservados deben comprobarse en visita; las decisiones financieras cloud siguen vigentes.

## Fuentes y aplicación proporcional

El [Caso 09](../../../00_Bases/Caso_09_Cadena_Multitienda.md), capítulos 2 y 6 y particularización RT-06.01, describe **22 tiendas**, **DC de 140 m² en casa matriz**, **sala de respaldo en la misma comuna**, **CD principal de 42.000 m²** y **CD Concepción de 9.000 m²**. La superficie comercial o de bodega no es superficie de sala técnica. No informa dimensiones de gabinetes de tienda ni superficie de la sala de respaldo. El informe de brechas del DC de 2024 se entrega al adjudicatario: no se presume conocido.

Las [Bases Transversales](../../../00_Bases/Bases_Transversales.md), capítulo 6.1, obligan a declarar tipología y proporcionalidad. Se adopta DC-01 como sala principal (RT-06.01–24 íntegros, además de custodia/operación/rutas que correspondan); DC-02 y ambos CD como salas secundarias; tienda como borde operacional protegido. Para tienda se adopta voluntariamente continuidad energética reforzada de 30 minutos de UPS y generación de 24 h para la carga esencial. La obligación de 24 h de operación sin WAN no se interpreta por sí sola como 24 h de batería. No se traslada biometría con esclusa ni climatización de precisión del DC completo a cada pequeño gabinete.

RT-08.03 exige HA de núcleo, cortafuegos y balanceadores; RT-08.04 exige fuentes redundantes y circuitos distintos. Los símbolos Cisco de la figura no fuerzan fabricante ni licencia: cada equipo final debe cumplir fuentes duales y el contrato de soporte, incluidos equipos de operador que se usen como parte crítica. Un adaptador o ATS no convierte una fuente única en fuente redundante conforme.

## Lista de equipos por tienda

Patrón por cada SIT-xx; 22 multiplicadores actuales. Toda cifra de capacidad es reserva inicial de diseño. Se exige margen de crecimiento **30 % sobre carga proyectada**, sin contarlo otra vez en cada subsistema.

| ID / equipo | Cantidad por tienda (total 22) | Especificación y ubicación inicial | Justificación / carácter |
| --- | --- | --- | --- |
| WAN-CPE-A/B · routers de operador | 2 (44) | Dos operadores y entradas físicas distintas, handoff Ethernet; suministro A/B y fuentes duales. No contar el SD-WAN otra vez como router si la función la integra. | RT-03.17/RT-06.32; obligatorio de diversidad, selección técnica de equipos. |
| SDW-R-A/B | 2 (44) | Appliances HA Retail, 1U cada uno, IPsec, selección dinámica de ruta, QoS, firewall y gestión segregada. Ambos acceden a ambos operadores. | HA RT-08.03; elección SD-WAN propia. |
| SDW-F-A/B | 2 (44) | Par independiente Filial; rutas F y X locales explícitas, ninguna LAN R→F libre. Fuentes A/B, mismas dos WAN con aislamiento contractual. | Separación caso RT-03.24 y HA. |
| SW-R-A/B | 2 (44) | Switches de acceso/servidor R, 24 puertos mínimo inicial, VLAN, 802.1X, uplinks 10 Gb/s, doble PSU. Equipo final según puertos y PoE medidos. | Red R y HA, cantidad propia. |
| SW-F-A/B | 2 (44) | Par F independiente; host F y X en segmentos propios, uplinks redundantes, doble PSU. Mínimo 24 puertos inicial; evitar redes de invitados y CCTV. | Separación física de red elegida para sostener la decisión del usuario. |
| SW-ACC-* · acceso periférico | Según padrón, sin cifra ficticia | Cámaras, invitados, administración y móviles en VLAN/VRF independientes; no usar la reserva de 24 puertos como inventario completo del local. | Caso 380 cajas, 640 móviles y 1.840 cámaras agregadas sin distribución local. |
| Q-R/Q-F | 2 dispositivos (44) | Testigos independientes por par, sin datos; arbitraje/fencing accesible con WAN caída, alimentación A/B. Reserva física 1U conjunta para appliances compactos de doble PSU certificados. | Completa requisito de quorum; no es quinto host de aplicación. |
| RACK-R / RACK-F | 2 × 24U (44) | Uno para cada par de hosts, puertas y llaves distintas, 600 × 1.070 mm de referencia, rieles ajustables, tierra y fijación sísmica calculada. | Cuatro hosts existentes en diseño; 2U máximos reservados por host. |
| RACK-NET | 1 × 24U (22) | Rack de comunicaciones separado, 600 × 1.070 mm envolvente de diseño; paneles F/R separados, gestión y acceso F restringidos. | Adopción voluntaria en tienda de separación RT-06.05; en principal es obligatoria. |
| UPS-A/UPS-B | 2 unidades (44) | Online doble conversión, **6 kVA/6 kW por rama**, bypass de mantenimiento individual, tarjeta SNMP; baterías propias para **30 min a 6 kW por unidad**, incluso con rama compañera caída. Instalación de piso en zona eléctrica separada, no dentro de rack servidor. | Meta propia tienda basada en RT-06.07; autonomía depende de curva de fabricante. |
| PDU-A/PDU-B | 6 (132) | Dos PDU verticales 0U medidas por rack, enchufes bloqueables; cada PSU a rama diferente. | RT-08.04 y deseable RT-06.12. |
| GEN-SIT / ATS | 1 + 1 por tienda | Generación del edificio acreditada o grupo propio de reserva **20 kVA** inicial, ATS y bypass; suministro dedicado a carga esencial. Estanque externo dimensionado para 24 h con curva real y reabastecimiento. No atribuir equipo existente al mall sin contrato. | Adopción propia de RT-06.08 al borde; kVA se ajustan por motores/clima/arranque. |
| HVAC-SIT-A/B | 2 | Dos unidades aptas operación continua, cada una capaz de evacuar carga esencial completa; reserva **5 kW térmicos por unidad** para equipos nuevos del patrón, a recalcular por PoE y ambiente. | N+1 ofrecido en tienda; ambiente del equipo obligatorio por tipología. |
| ENV-SIT | 1 controlador + 6 sondas T/HR + 1 cable agua + 3 contactos puerta | Una pareja de sondas entrada/salida por rack; agua bajo zona de riesgo, alertas BMS/NOC. Alimentación protegida y supervisión de pérdida de señal. | RT-06.14 proporcional; distribución técnica inicial. |
| FIRE-SIT | 1 sistema de detección integrado + 1 extintor local habilitado | Detección local integrada a la existente; selección y número de detectores por cobertura real. No instalar agente limpio por defecto en gabinete abierto a sala comercial. | Protección del sitio y ambiente; sistema del edificio debe acreditarse. |
| PHY-SIT | 3 cerraduras registrables + 1 cámara de acceso | Tres racks cerrados, acceso nominativo, alarmas de apertura, cámara integrada a retención de 30 días. No añadir cámaras al total actual como si se conociera cobertura. | Control de acceso físico proporcional. |
| CAB-SIT | 1 lote por tienda | Paneles fibra/cobre, organizadores, latiguillos, fibra dual por ruta, etiquetas, puesta a tierra y prueba de cada enlace. Separar datos, energía y R/F. | RT-06.04 y RT-03.24; suministro medido por planos. |

### Ocupación y potencia inicial de tienda

RACK-R y RACK-F: 4U para dos hosts (2U de envolvente por host), 2U para panel y organización, 1U para testigo/copia compacta si aplica, 1U para accesorios: **8U ocupadas/24U**, 16U libres. No se compra capacidad de cómputo adicional por tener U libres. RACK-NET: CPE 2U, SD-WAN 4U, switches 4U, paneles/organizadores 4U y control 1U: **15U/24U**, 9U libres. Son reservas de montaje; modelo que exceda estas cotas obliga a recalcular. PDU vertical 0U, UPS/baterías y generador fuera de esos racks.

Carga nueva de cálculo: cuatro hosts × 0,35 kW = 1,40 kW; cuatro SD-WAN × 0,08 = 0,32; cuatro switches × 0,15 = 0,60; dos CPE × 0,05 = 0,10; sensores/testigos/copias 0,15: **2,57 kW**. Con 30 %: **3,341 kW**, menor que la capacidad de una rama UPS de 6 kW. No son potencias de producto: deberán sustituirse por mediciones y fichas. PoE periférico, POS, iluminación esencial y climatización se suman expresamente; si el total protegido supera 6 kW se aumenta UPS y batería antes de aceptar el diseño. Un generador de 20 kVA con FP de referencia 0,8 ofrece 16 kW nominales, sujeto a altitud/temperatura y transitorios; no representa 16 kW útiles garantizados ni compra cerrada.

La energía de batería ideal `P × 0,5 h` es solo un límite inferior: 6 kW requieren 3 kWh ideales por rama. La capacidad nominal se obtiene con pérdidas, envejecimiento, temperatura y descarga del fabricante. Combustible mínimo de diseño: `24 × consumo_litros/h(carga efectiva) × 1,20` más volumen no utilizable; no inventar litros a partir de kVA. Demostrar autonomía con ensayo de carga. El generador alimenta climatización esencial además del TI y permite recargar baterías; no arrancar ambos compresores simultáneamente sin cálculo.

## DC principal y sala de respaldo

| Elemento | DC-01 · propuesta inicial | DC-02 · criterio |
| --- | --- | --- |
| Red y operadores | 2 CPE, 2 SD-WAN R + 2 F, 2 switches R + 2 F, uplinks por rutas distintas; firewall integrado o par dedicado sin doble conteo. | Igual patrón HA solo para servicios efectivamente alojados; 2 CPE y par SD-WAN del ámbito presente como base. |
| Racks | Servidores R, servidores F de convivencia/custodia y comunicaciones **independientes**; número y ocupación se fijan contra CMDB, no de 140 m². No nuevo núcleo financiero. | No clonar racks DC-01 sin conocer dimensiones; racks según función local efectiva. |
| Energía | UPS A/B 2N, cada una para 100 % de carga proyectada +30 %, 30 min a plena carga; bypasses, tableros separados y medición kW/FP. Generador y ATS para 24 h con reabastecimiento, sin presuponer potencia existente. | Igual autonomía para carga local crítica que se declare; no considerar respaldo comunal como DR regional. |
| Climatización | Precisión N+1, temperatura/HR por fabricantes, sensores T/HR entrada/salida de cada rack, cable fuga, medición térmica; contención de pasillo frío ofrecida. | Climatización proporcional de uso continuo con redundancia elegida según carga. |
| Incendio | Detección aspirada láser supervisada, panel, agente limpio aprobado UL diseñado conforme NFPA aplicable, extintores vigentes; integración NOC y cliente. Cantidad de boquillas/cilindros/tubería por cálculo del recinto y estanqueidad. | Detección y extinción según riesgo y función; no declarar volumen de agente sin geometría. |
| Seguridad | Control facial con AFIS respaldo, bitácora, estación de enrolamiento externa deseable, pasillo de control y acceso unipersonal, CCTV 30 días + copia anterior auditable. | Acceso físico, CCTV y monitoreo dimensionados a función; sin inventar superficie. |
| Custodia y operación | Zona de medios transportables cifrados, inventario, legibilidad y movimientos; operación del personal fuera de sala equipos, estaciones duales y telefonía. | Custodia solo de conjuntos identificados; no recepción indiscriminada de cartera F cloud. |

El diseño de planta debe reservar zonas de baterías, servidores, comunicaciones, trabajo, respaldo y generación sin ubicar combustible dentro de la sala TI. El generador exterior necesita autorización y superficie propia; los 140 m² del recinto no prueban patio, ducto de escape ni resistencia estructural. Especificación civil y coordinación del proponente; ejecución de separación del cliente (RT-06.06). Recibir plano, cargas de piso, vías de evacuación e informe 2024 antes de afirmar que la instalación cabe.

## Centros de distribución y oficinas

Por **cada CD**: 2 CPE, 2 SD-WAN/firewall R, 2 switches R con fuentes duales, par local logístico de 2 hosts; 1 rack servidor 24U y 1 comunicaciones 24U como reserva inicial; 2 UPS A/B de 6 kW con autonomía 30 min certificada; 1 ATS y generación propia o acreditada del edificio para 24 h esenciales; clima continuo N+1, sensor T/HR por frente y fondo de rack, agua, puerta y detección de incendio integrada. La conectividad RF/cámaras/terminales requiere switches de acceso y AP calculados por cobertura y puertos: el área de bodega no se llena de racks TI por regla de tres. El CD principal conserva WMS sin deducir su alojamiento. Concepción tiene planillas, no un WMS acreditado.

Oficinas: dos accesos WAN cuando soporten función crítica, par de borde y switching HA, UPS A/B de red y puestos esenciales según carga. No agregar generador propio si el del edificio ya acredita potencia, transferencia, mantenimiento y prioridad contractual. No duplicar sanitarios ni áreas exteriores existentes (RT-06.31). Mantener el acceso remoto seguro para que la indisponibilidad del puesto administrativo no bloquee la nube.

## Deseables que se incorporan al diseño

| Exigencia deseable de Bases | Adopción concreta | Comprobación |
| --- | --- | --- |
| RT-06.12 · alimentación 2N o N+1 | UPS A/B 2N y circuitos distintos; acometidas duales donde sean físicamente independientes y factibles. | Retirar cada rama con carga total; verificar fuentes, bypass y alarmas. No declarar doble acometida si ambas siguen mismo punto de falla. |
| RT-06.15 · contención | Pasillo frío contenido en DC-01 si la planta y aire lo admiten; paneles ciegos y sellado de pasos en todos los racks. | Temperatura de entrada de cada rack y energía comparadas antes/después. |
| RT-06.22 · enrolamiento externo mejor evaluado | Puesto de enrolamiento fuera de sala TI del DC. | Recorrido de visitante, bloqueo y bitácora. |
| RT-06.34 · mejoras justificadas | PDU medidas, sensores de fuga, bypass mantenible, revisión de autonomía y batería, repuestos de ópticos/PSU. | Alarmas trazables, prueba de mantenimiento sin pérdida de servicio. |
| RT-08.15 · muestra de cada dispositivo | Una unidad de cada tipo de terminal/appliance para piloto previo a compra masiva. | Compatibilidad, ambiente, puertos, doble fuente y consumo en banco. |
| RT-08.19 · extensión de vida útil | Reutilización de racks/cableado existente solo si certificación y estado admiten; equipos nuevos de suministro cumplen RT-08.06. | Inventario, ensayo y ahorro material cuantificado; no vender equipo usado como nuevo. |
| RT-15.06 · reducción consumo | Medición mensual kWh, FP y PUE del DC con meta inicial de reducción de 5 % tras línea base anual y sin degradar redundancia. | Objetivo propio, no PUE contractual inventado; reporte anual y corrección de carga/clima. |

## Flujos que debe distinguir la figura

Datos: operador A/B → CPE → SD-WAN del ámbito → switches del ámbito → hosts/periféricos; túneles del ámbito al hub cloud correspondiente. R→X local→F es excepción contractual controlada, no unión de switches R/F.

Energía: red pública/generador → ATS/tablero → UPS A/B → PDU A/B → PSU de equipos. Climatización esencial se protege con generación y su circuito apropiado; no usar la misma flecha de datos para electricidad. Telemetría de UPS, ATS, generación, clima, puerta, agua e incendio → red de gestión → observabilidad. Los sistemas de seguridad de vida mantienen actuación local ante pérdida WAN.

La general debe agregar solo agrupaciones reconocibles de CPE/router, SD-WAN, switching, UPS y generación por tipo de sitio; cantidades, PDU, baterías y sensores se conservan aquí y en detalles posteriores. Los racks son envolventes físicas, no routers ni saltos de red.

## Fuentes técnicas primarias abiertas y límites

Consulta 23-10-2026. [Schneider, selector UPS](https://www.se.com/us/en/work/products/tools/ups-selector/) explica que autonomía depende de carga y características del UPS: justifica exigir curva y ensayo, no prometer minutos por kVA. [Manual oficial NetShelter 24U](https://iportal.se.com/Contents/docs/UPS-AR3104.PDF) sirve de referencia de instalación y envolvente de gabinete; debe comprobarse profundidad útil, peso y rieles del equipo final. [Cisco, especificaciones Catalyst 9300](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/technical-specs.html) aporta dimensiones y ambiente por modelo; la marca del icono no acredita que todo modelo soporte las fuentes requeridas. No se ha ejecutado visita, estudio de selectividad, certificación normativa eléctrica, cálculo estructural, hidráulico/incendio ni medición RF.

**Cierre verificable:** plano por sitio con dimensiones y accesos; ocupación U/peso por rack; carga real y protegida de POS/red/PoE/clima; curva UPS 30 min y ensayo de cada rama; cálculo del generador, combustible y emplazamiento; diversidad WAN probada; pérdida de host/switch/borde y quorum sin WAN; registro NOC de todas las alarmas. Ingeniería de detalle convierte las envolventes en lista de compra exacta; ningún dato ausente del caso se presenta como espacio ya disponible.
