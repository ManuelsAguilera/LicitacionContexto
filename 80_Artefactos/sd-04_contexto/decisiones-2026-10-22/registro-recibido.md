# Registro de decisiones: diagrama de arquitectura lógica

| ID | Fecha | Tema | Decisión | Fuente |
|---|---|---|---|---|
| D-01 | 2026-10-22 | Solapes entre capas | Las capas 7 y 8 proveen; la 2, la 3 y la 4 aplican. Marco del usuario por capa adoptado como base, a verificar | Bases Transv. §2.1, RT-11.11 |
| D-02 | 2026-10-22 | Método visual | M2: llave de servicio sobre iconos de función, con etiqueta de negocio y RT en pequeño | FEP01 diap. 61 |
| D-03 | 2026-10-22 | Capas 7 y 8 | Bandas horizontales bajo las columnas 1 a 6 | FEP01 diap. 66 |
| D-04 | 2026-10-22 | Emplazamiento de la Filial | El sd-04 queda como base; los riesgos se evalúan en las capas 6 y 7 | Caso Cap. 15 RT-06.01, RT-03.24 |
| D-05 | 2026-10-22 | Capa 1, nodo local | Sale de la capa 1. Se dibuja como «Continuidad de tienda» on-premise sobre las capas 4 (ventas y oferta en modo tienda), 5 (sincronizador) y 6 (diario local) | §2.1; SD4:155, 264 |
| D-06 | 2026-10-22 | Capa 1, canales del cliente | Dos canales: tienda (Retail) y tarjeta (Filial), con portal y app propios cada uno | Línea roja; práctica de Falabella, Ripley y Cencosud |
| D-07 | 2026-10-22 | Capa 1, apps internas | Una app interna con cuatro perfiles: sala, preparación, conteo y prevención, recepción | Caso RT-17.01, restricción 11 |
| D-08 | 2026-10-22 | Capa 1, alcance | Se descartan las cajas de autoservicio y el portal del fiscalizador | Fuera de lo que pide el caso; RT-16.28 cubre los reportes |
| D-09 | 2026-10-22 | Capa 1, RT-17.02 | Apps internas y de cliente híbridas en React Native (interna con SQLite y DataWedge; app de la tarjeta con base de código separada). Caja web en React servida por el nodo local | Ver capa 1 |
| D-10 | 2026-10-22 | Capa 1, simulador de CAE | Va en el portal de la tarjeta, enlazado desde el portal público | Caso «RT-16.30» |
| — | 2026-10-22 | Capa 1 | **Cerrada:** 12 elementos en 6 bloques | — |
| D-11 | 2026-10-22 | Capa 2, perfiles | Dos perfiles de Azure Front Door Premium (Retail y Filial), cada uno con su política de WAF y en su suscripción. Cambia el sd-04 (un perfil global, SD4:677) | Caso RT-03.24, D-06 |
| D-12 | 2026-10-22 | Capa 2, TLS | Solo TLS 1.3 (`minimum-tls-version TLS13`) | §2.1, RT-11.08 |
| D-13 | 2026-10-22 | Capa 2, Application Gateway | Sale de la capa 2 y se conserva en la capa 3 | SD4:560, 676 |
| D-14 | 2026-10-22 | Capa 2, entrada privada | Se dibuja una flecha «red privada» directa de tiendas, CD y DC-01 a la capa 3, sin pasar por Front Door (SD-WAN y ExpressRoute) | RT-02.01, RT-03.21 |
| — | 2026-10-22 | Capa 2 | **Cerrada:** dos llaves de Front Door (Retail y Filial), Azure DNS, conexión privada por Brazil South y flecha «red privada» | — |
| D-15 | 2026-10-22 | Capa 2, DNSSEC | Queda fuera | Disponibilidad general no verificada |
| D-16 | 2026-10-22 | Capa 3, OpenAPI 3.1 | 3.1 generado desde el código y publicado en API Center; 3.0.3 derivado e importado a APIM en el pipeline. El riesgo se declara en el T-12 | RT-05.16; restricciones de importación de APIM |
| D-17 | 2026-10-22 | Capa 3, ruta de X-01 | Retail llega a la Filial solo por X-01, que entra por la puerta de la Filial; esa puerta solo acepta la identidad de X-01 desde Retail | SD3:298, SD4:586 |
| D-18 | 2026-10-22 | Capa 3, catálogo | Un Azure API Center por ámbito (Retail y Filial) | Línea roja |
| D-19 | 2026-10-22 | Capa 3, BFF | Fuera del diagrama; cada canal es un producto de APIM con cuota propia | — |
| D-20 | 2026-10-22 | Capa 3, finanzas abiertas | Investigado: el primer grupo de la NCG 514/569 incluye a «emisores de tarjetas de crédito», con plazos de 5 a 18 meses desde julio de 2027. Alcance por decidir | Cuatrecasas, Carey; texto oficial por verificar |
| D-21 | 2026-10-22 | Capa 3, finanzas abiertas | **Dentro del alcance:** producto «Finanzas abiertas» en la puerta de la Filial (capa 3), consentimiento en la capa 4 de la Filial y certificación en la capa 7. Confirmar Art. 18 de la Ley 21.521 y el Anexo Técnico N° 3 | NCG 514/569 |
| — | 2026-10-22 | Capa 3 | **Cerrada:** App Gateway ×2, APIM Premium clásico ×2, API Center ×2 | — |
| D-22 | 2026-10-22 | Capa 4, servicios comunes | Bloque «Servicios comunes» (parámetros, auditoría, flujos y reglas, documentos y firma, avisos, búsqueda y exportación) con una instancia por frente. Pendiente: confirmar con el usuario tras la explicación | RT-16.01 a 16.34 |
| D-23 | 2026-10-22 | Capa 4, orquestación | La orquestación de procesos largos va en la capa 5; la compensación queda en cada servicio de la capa 4 | §2.1 |
| D-24 | 2026-10-22 | Capa 4, IA y consentimiento | «Sugerencias automáticas» (IA) como sub-elemento de Existencias; consentimiento de finanzas abiertas dentro de Evidencia y consentimiento (C-03) | RT-18.07, D-21 |
| D-25 | 2026-10-22 | Capa 4, motor de flujos | Se evalúa en la arquitectura física (Camunda, Temporal, Flowable) | Respuesta del usuario |
| D-26 | 2026-10-22 | Capa 4, AKS | Premium con soporte a largo plazo propuesto; pendiente confirmación y disponibilidad en Chile Central | [AKS LTS](https://learn.microsoft.com/en-us/azure/aks/long-term-support) |
| D-27 | 2026-10-22 | Contradicción en el sd-04 | SD4:304 (X-01 al costado) frente a SD4:586 y SD3:298 (X-01 en medio). Se dibuja X-01 en medio (D-17); el sd-04 se deja sin editar y el equipo debe unificarlo | — |
| D-22 | 2026-10-22 | Capa 4, servicios comunes | Bloque «Servicios comunes» (parámetros, auditoría, flujos y reglas, documentos y firma, avisos, búsqueda y exportación) con una instancia por frente. Pendiente: confirmar con el usuario tras la explicación | RT-16.01 a 16.34 |
| D-23 | 2026-10-22 | Capa 4, orquestación | La orquestación de procesos largos va en la capa 5; la compensación queda en cada servicio de la capa 4 | §2.1 |
| D-24 | 2026-10-22 | Capa 4, IA y consentimiento | «Sugerencias automáticas» (IA) como sub-elemento de Existencias; consentimiento de finanzas abiertas dentro de Evidencia y consentimiento (C-03) | RT-18.07, D-21 |
| D-25 | 2026-10-22 | Capa 4, motor de flujos | Se evalúa en la arquitectura física (Camunda, Temporal, Flowable) | Respuesta del usuario |
| D-26 | 2026-10-22 | Capa 4, AKS | Premium con soporte a largo plazo propuesto; pendiente confirmación y disponibilidad en Chile Central | [AKS LTS](https://learn.microsoft.com/en-us/azure/aks/long-term-support) |
| D-27 | 2026-10-22 | Contradicción en el sd-04 | SD4:304 (X-01 al costado) frente a SD4:586 y SD3:298 (X-01 en medio). Se dibuja X-01 en medio (D-17); el sd-04 se deja sin editar y el equipo debe unificarlo | — |
| D-28 | 2026-10-22 | Capa 4, confirmaciones | D-22 confirmado (servicios comunes, una instancia por frente). D-26 AKS Premium confirmado, sujeto a verificar que exista en Chile Central. D-27 se anota para el equipo. X-01 en medio de la ruta, no al costado | Respuesta del usuario |
| — | 2026-10-22 | Capa 4 | **Cerrada** | — |
| D-29 | 2026-10-22 | Capa 5, un bus por ámbito | Un bus por ámbito (Retail y Filial). Ningún bus cruza la frontera; lo único que cruza es la llamada por X-01, que publica en el bus del lado receptor | SD4:384, D-17 |
| D-30 | 2026-10-22 | Capa 5, traductores | 4 cajas: Comercio (ERP/DTE, WMS), Canales (comercio electrónico, marketplace, fidelización), Socios (transportistas, proveedores, medios de pago), Crédito (plataforma de 2011, reportes CMF, firma). Las 14 interfaces van en la tabla de detalle | RT-05.20 |
| D-31 | 2026-10-22 | Capa 5, cargas masivas | **No** se dibuja «Cargas masivas» como elemento. RT-05.22 sigue siendo obligatorio: se cubre como función de los traductores | RT-05.22 |
| D-32 | 2026-10-22 | Capa 5, coordinación | La coordinación de procesos largos se dibuja en esta capa; el motor se elige en la física | D-23, D-25 |
| D-33 | 2026-10-22 | Capa 5, Event Hubs | **Aprobado:** se quita Event Hubs; solo Azure Service Bus Premium por ámbito. Regla: agregar Event Hubs solo para el pico de precios (1.333 publicados y 6.667 entregados por segundo, 5 min) si la prueba en Preproducción lo exige. Modifica ADR-06 del sd-04 | ADR-06; §2.1 |
| D-34 | 2026-10-22 | Capa 5, RT-05.22 | Las cargas y descargas masivas se cubren como función de las cajas de traductores, sin elemento propio | RT-05.22 |
| — | 2026-10-22 | Capa 5 | **Cerrada** | — |
| D-29 | 2026-10-22 | Capa 5, un bus por ámbito | Un bus por ámbito (Retail y Filial). Ningún bus cruza la frontera; lo único que cruza es la llamada por X-01, que publica en el bus del lado receptor | SD4:384, D-17 |
| D-30 | 2026-10-22 | Capa 5, traductores | 4 cajas: Comercio (ERP/DTE, WMS), Canales (comercio electrónico, marketplace, fidelización), Socios (transportistas, proveedores, medios de pago), Crédito (plataforma de 2011, reportes CMF, firma). Las 14 interfaces van en la tabla de detalle | RT-05.20 |
| D-31 | 2026-10-22 | Capa 5, cargas masivas | **No** se dibuja «Cargas masivas» como elemento. RT-05.22 sigue siendo obligatorio: se cubre como función de los traductores | RT-05.22 |
| D-32 | 2026-10-22 | Capa 5, coordinación | La coordinación de procesos largos se dibuja en esta capa; el motor se elige en la física | D-23, D-25 |
| D-33 | 2026-10-22 | Capa 5, Event Hubs | **Aprobado:** se quita Event Hubs; solo Azure Service Bus Premium por ámbito. Regla: agregar Event Hubs solo para el pico de precios (1.333 publicados y 6.667 entregados por segundo, 5 min) si la prueba en Preproducción lo exige. Modifica ADR-06 del sd-04 | ADR-06; §2.1 |
| D-34 | 2026-10-22 | Capa 5, RT-05.22 | Las cargas y descargas masivas se cubren como función de las cajas de traductores, sin elemento propio | RT-05.22 |
| — | 2026-10-22 | Capa 5 | **Cerrada** | — |
| D-35 | 2026-10-22 | Capa 6, recuperación de la Filial | Producción en Chile Central y un segundo sitio propio del Cliente, distinto de DC-01, para la copia de la Filial. Brazil South solo con aprobación escrita del Cliente (Art. 23). Presentar las tres opciones en el sd-08. Verificar el texto del Cap. 20-7 de la RAN | RT-07.02, Art. 23; CMF 7-04-2026 |
| D-36 | 2026-10-22 | Capa 6, retención | Un elemento «Archivo de retención e histórico consultable» por ámbito: Blob/Data Lake inmutable con ciclo de vida. Dimensionar a 6 años o más en la física | RT-05.07, RT-05.15, caso Cap. 15 |
| D-37 | 2026-10-22 | Capa 6, cifrado y pagos | Cifrado de campo en la aplicación con claves del Managed HSM de cada ámbito e índice ciego para búsquedas. Tokens de pago emitidos por el procesador; sin nombrar proveedor; ficha PCI en la física | RT-11.10, caso |
| D-38 | 2026-10-22 | Capa 6, estado e historial de precios | Sin almacén de sesión en la Filial (credenciales firmadas); estado de procesos en el PostgreSQL de cada ámbito. «Historial de precios publicados» como elemento de Retail, solo de escritura, con particiones por fecha | RT-02.05, RT-12.08, caso 16.1 #10 |
| D-39 | 2026-10-22 | Capa 6, lectura | Se dibujan dos caminos de lectura: operacional (caché de oferta, ≤ 30 s) y analítico (Data Lake, posición financiera antes de las 07:00) | Caso RT-05.29 |
| — | 2026-10-22 | Capa 6 | **Decisiones aprobadas** (falta que el usuario diga que se pasa a la capa 7) | — |
| D-40 | 2026-10-22 | Capa 7, tenant de la Filial | **Opción B** (interpretación del «si» del usuario, a confirmar): tenant de Entra propio para la Filial, con su grupo raíz, su conectividad y su espacio de Sentinel; SOC con vista agregada de incidentes sin datos. Modifica el sd-04 (árbol único de 17 suscripciones, SD4:528; hub y Gestión compartidos) | Caso Cap. 10 #1, RT-03.24 |
| D-41 | 2026-10-22 | Capa 7, identidad de clientes | Entra External ID con un tenant externo por negocio (cliente de la tienda y titular de la tarjeta). Costo tras los 50.000 usuarios activos gratis: por verificar | RT-12.12, D-06 |
| D-42 | 2026-10-22 | Capa 7, terminales | QR + PIN (vista previa) y modo de dispositivo compartido en las 640 terminales. Repositores externos quedan como pendiente de proceso con el Cliente | RT-12.11, caso 16.1 #19 |
| D-43 | 2026-10-22 | Capa 7, registro inalterable | Exportación de las tablas de seguridad y auditoría a Blob inmutable bloqueado en la misma región. La grabación de Bastion va en un contenedor sin inmutabilidad y se copia después al inmutable | RT-11.14, RT-16.07 |
| D-44 | 2026-10-22 | Capa 7, cupo en tienda | Almacén propio de la Filial dentro del nodo de tienda: máquina virtual separada, red del mesón, clave de la Filial; solo referencia seudonimizada, cupo y vigencia | SD4:388 |
| D-45 | 2026-10-22 | Capa 7, residencia | Declarar en RT-11.13 y Art. 23 el tránsito por el borde de Front Door y por Brazil South; pedir aprobación escrita del Cliente antes de comprometer la arquitectura de la Filial | Art. 23 |
| D-46 | 2026-10-22 | Capa 7, cadena de entrega | Fuera del diagrama lógico; va en la física y en el sd de calidad | RT-11.22 a 11.26 |
| — | 2026-10-22 | Capa 7 | **Decisiones aprobadas** (falta que el usuario diga que se pasa a la capa 8) | — |
| D-47 | 2026-10-22 | Capa 8, medición | Aplicaciones emiten OTLP a un recolector de OpenTelemetry por clúster y por tienda, que exporta a Azure Monitor (no el agente de Application Insights directo). Exportador de Azure Monitor: por verificar | RT-14.01, RT-03.07, RT-02.14 |
| D-48 | 2026-10-22 | Capa 8, correlación | X-01 crea un identificador nuevo por cruce; cada lado conserva sus trazas en su espacio; ningún espacio de monitoreo compartido entre tenants | SD4:374, D-40 |
| D-49 | 2026-10-22 | Capa 8, pruebas sintéticas | Se incluyen. Verificar antes si las pruebas Estándar soportan TLS 1.3 exclusivo; si no, medir desde dentro del borde | D-12 |
| D-50 | 2026-10-22 | Capa 8, experiencia real | Elemento «Experiencia real» (web y móvil); herramienta móvil por decidir en la física | RT-14.03 |
| D-51 | 2026-10-22 | Capa 8, tienda | Recolector local con cola de 24 h en el nodo de tienda; alerta «tienda sin enlace» por ausencia de latido | RT-03.10, RT-03.16 |
| D-52 | 2026-10-22 | Capa 8, NOC | Vista de salud agregada, solo estado y sin datos de negocio; mecanismo entre tenants por evaluar en la física | RT-21.01, D-40 |
| D-53 | 2026-10-22 | Capa 8, anomalías y entrega | Detección de anomalías como elemento «por verificar»; indicadores de entrega (RT-04.12, RT-10.09) en Grafana | RT-14.09 |
| — | 2026-10-22 | Capa 8 | **Cerrada.** El usuario delegó: «haz lo que convenga, si conviene entonces sí»; se adoptaron las siete recomendaciones | — |

## Miro (2026-10-22)
- Paso 1 hecho: lectura del tablero. El marco C4 («Contexto agrupado por función», x=4067, y=9315) tiene 14 personas y 11 sistemas externos (verificado por conteo). Convención de color del tablero: Retail azul, Filial morado, transversal gris, sistemas externos blanco con borde oscuro, sistemas en retiro naranja.
- Paso 2 hecho: marco de prueba M2 creado en x=0, y=114000 (id 3458764688056140484), 71 elementos. No se tocó nada existente. Espacio libre confirmado: x −4000 a 12000, y 106800 a 120800.
- El marco «iconos» (x=10731, y=14303) está vacío.
- Método elegido: M4 (tarjeta por servicio) para las láminas de detalle; la general solo lleva nombres de servicios (D-54). Colores: columnas 1 a 6 en amarillo, naranja, verde, rojo, azul y morado; bandas 7 y 8 en gris; ámbito con punto azul (Retail) y morado (Filial) (D-55). Agrupación de personas (5) y sistemas (4) aprobada (D-56).
- Muestras M1, M3 y M4 creadas en y=116000 (x=0, 2000, 4000). Marco M2 en y=114000.
- Lámina general creada: marco «Arquitectura lógica · lámina general», x=0, y=118000, id 3458764688057442762, 145 elementos, 5328×2140. Verificada en una imagen: sin solapes; la flecha de sistemas externos a la capa 5 va por arriba.
- Lámina general v2 (textos 33 y 22, sin tocar la v1): «Arquitectura lógica · lámina general (textos grandes)», x=0, y=121000, id 3458764688057992777, 6448×2360.
- Nueve láminas de detalle (método M4), x=0, desde y=124000: capa 1 (3458764688058018364), capa 2 (…018928), capa 3 (…108430), capa 4 Retail (…210881), capa 4 Filial (…238751), capa 5 (…345152), capa 6 (…345730), capa 7 (…439596), capa 8 (…564029).
- Verificado en imagen: sin solapes. Pendiente: el usuario decide si se borran la general v1 (3458764688057442762) y las muestras M1, M2, M3, M4 (3458764688056619901, …140484, …619902, …619903). No se borró nada.
- Método elegido: M4 (tarjeta por servicio) para las láminas de detalle; la general solo lleva nombres de servicios (D-54). Colores: columnas 1 a 6 en amarillo, naranja, verde, rojo, azul y morado; bandas 7 y 8 en gris; ámbito con punto azul (Retail) y morado (Filial) (D-55). Agrupación de personas (5) y sistemas (4) aprobada (D-56).
- Muestras M1, M3 y M4 creadas en y=116000 (x=0, 2000, 4000). Marco M2 en y=114000.
- Lámina general creada: marco «Arquitectura lógica · lámina general», x=0, y=118000, id 3458764688057442762, 145 elementos, 5328×2140. Verificada en una imagen: sin solapes; la flecha de sistemas externos a la capa 5 va por arriba.
- Lámina general v2 (textos 33 y 22, sin tocar la v1): «Arquitectura lógica · lámina general (textos grandes)», x=0, y=121000, id 3458764688057992777, 6448×2360.
- Nueve láminas de detalle (método M4), x=0, desde y=124000: capa 1 (3458764688058018364), capa 2 (…018928), capa 3 (…108430), capa 4 Retail (…210881), capa 4 Filial (…238751), capa 5 (…345152), capa 6 (…345730), capa 7 (…439596), capa 8 (…564029).
- Verificado en imagen: sin solapes. Pendiente: el usuario decide si se borran la general v1 (3458764688057442762) y las muestras M1, M2, M3, M4 (3458764688056619901, …140484, …619902, …619903). No se borró nada.

## Pendientes abiertos
- Miro: aprobación del método M2, paleta de columnas, y verificar que los emojis se vean en el tablero.
- Capa 8: exportador de Azure Monitor para OpenTelemetry; Spring Boot 4 y Java 25 con el agente; pruebas Estándar con TLS 1.3; mecanismo de vista agregada entre tenants; costo de la telemetría.
- Capa 7: confirmar que el «si» de la decisión 1 era la opción B; Managed HSM, Istio (GA) y Private Access con Intune en Chile Central/sd-04; costo de External ID; NFC no confirmado.
- Capa 4: verificar AKS Premium en Chile Central.
- Capa 6: disponibilidad en Chile Central de Managed Redis, Managed HSM, Power BI (región del servicio), configuraciones D*ds_v5 de PostgreSQL; TLS 1.3 exclusivo en PostgreSQL; réplica Chile Central → Brazil South; texto del Cap. 20-7 de la RAN.
- Capa 7: cupo preaprobado en el nodo de tienda (D-9 de la capa 6); tenant de Entra ID y piezas compartidas (D-04); tránsito por Brazil South; trabajo remoto (RT-03.22).
- Capa 5: confirmar D-33; cómo cubrir RT-05.22 dentro de los traductores.
- Capa 4: confirmar D-22 (instancia por frente) y D-26 (AKS Premium); si se ratifican, cerrar.
- Capa 2: certificados con alerta anticipada (D-8), reto progresivo con accesibilidad (D-6), tránsito por Brazil South (pasa a la capa 7).
- Capa 4/5: dónde van los coordinadores de saga.
- Capa 2/3: Application Gateway v2 y BFF.
- Capa 6/7: cupo preaprobado de la Filial guardado en el nodo de tienda de Retail.


## Miro: borrado de muestras (2026-10-22)
Borradas las 5 láminas de prueba: general v1 (...057442762), M1 (...056619901), M3 (...056619902), M4 (...056619903), M2 (...056140484). Quedan general v2 (...057992777) y las 9 láminas de detalle.


## Pendiente 2026-10-22: innovaciones en capa 4 + iconos Azure
Pedido del usuario: (a) faltan las innovaciones en la capa 4; (b) iconos tipo Azure como su imagen de referencia.
Innovaciones (sd-13, una por tipo, art. 28): Lockers Ancoa 24/7 (producto, servicio Pedidos, adaptador en capa 5); Conteo cíclico predictivo (proceso, Existencias); Búsqueda vectorial multimodal (tecnológica, Oferta comercial, pgvector en capa 6); Retail Media Network (modelo de negocio, Oferta comercial, adaptador a plataforma publicitaria); Modo Tienda con fila virtual (UX, Clientes Retail, nodo local de tienda).
Iconos: URLs jsdelivr funcionan en <image href>: https://cdn.jsdelivr.net/gh/benc-uk/icon-collection@master/azure-icons/<Nombre>.svg (Kubernetes-Services, Azure-Database-PostgreSQL-Server, API-Management-Services, Front-Doors, DNS-Zones, Application-Gateways, Service-Bus, Event-Hubs, Storage-Accounts, Key-Vaults, Firewalls, DDoS-Protection-Plans, Azure-Sentinel, Security-Center, Monitor, Network-Watcher, Log-Analytics-Workspaces, Azure-Arc, Azure-Active-Directory, Private-Link, Users, Mobile, Web-Environment). data: URI rechazado.
Subidos a Miro (widgets de prueba en y=114000, x 0-1000): API Center id 3458764688059748861 (resource 3458764518287239229); Managed Redis 3458764688059953677; Power BI ...953688; Bastion ...953692; Backup Vault ...953702; HSM (Dedicated HSM como proxy) ...953715; Managed Grafana ...953732; External Identities ...953750; Entra Private Access ...953754. Falta leerlos para sacar el resource id de cada uno y usar href="resource://ID" en las láminas. Probar si resource:// funciona con imágenes subidas.
Límite: Miro MCP free plan = 100 llamadas/día; se agotó 2026-10-22. Retomar al reset.
Plan: gen_general2.py -> PH 1500, icono 56px por ítem, bloque "Innovaciones" en capa 4 (5 filas); gen_all.py/content.py -> tarjetas de innovaciones en capa 4 Retail + icono por tarjeta; actualizar láminas existentes con update (no recrear); borrar widgets de prueba y1=114000 al final.


## Estado local 2026-10-22 (listo para subir al resetear el límite de Miro)
Usuario confirmó: iconos en lámina general Y en las 9 de detalle.
Generadores actualizados en scratchpad: icons_map.py (mapa título->icono; iconos subidos se activan creando icons_res.json con claves apicenter, redis, powerbi, bastion, backup, hsm, grafana, extid, privacc -> resource id), gen_all.py (icono 64px por tarjeta, chip Innovación), content.py (5 tarjetas de innovaciones en capa 4 Retail), gen_general2.py (iconos, bloque Innovaciones en capa 4, PH 1760, FH 2880, posición x=7000,y=121000).
Salidas: out/s1..s9.svg a partir de y=144000 (x=0); out/general2.svg a (7000,121000). Las láminas viejas (y=124000.. y general v2 en 0,121000) se borran después de verificar las nuevas.
Pasos mañana: 1) leer widgets subidos (y=114000) y sacar resource ids -> icons_res.json; 2) regenerar; 3) crear nuevas con canvas_create_from_svg (10 llamadas); 4) verificar con board_preview_read; 5) borrar viejas y widgets de prueba.
