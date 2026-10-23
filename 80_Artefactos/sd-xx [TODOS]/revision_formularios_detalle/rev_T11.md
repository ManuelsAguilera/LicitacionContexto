> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión Formulario T-11 (Especificaciones técnicas ofertadas)

Archivo: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-11.tex` (650 líneas). Solo lectura. Líneas = líneas del .tex salvo que se indique otra cosa.

Definición oficial (Bases Admin. línea 2278): "Detalle de los componentes de infraestructura, plataforma, licenciamiento y hardware especificado, con su ubicación / lugar y su justificación." Requisitos de apoyo: Bases Transversales cap. 6 (tipología por sitio, RT-06.01 y 6.33) y cap. 8 (RT-08.01 a 08.15, 8.4). Contra sd-04 (`OnlySimpleSolutions-Subdocumento4.tex`, tablas con la numeración real del archivo).

Resumen: el formulario cubre bien nube, plataforma, licenciamiento, ciclo de vida y portabilidad, no contiene precios (revisado: sin montos, UF ni CLP) y mantiene la separación Retail/Emisor. Falla en el reparto proponente/Cliente del hardware, en el DC-01 (no especifica nada), en las cantidades de red de tienda y en varias remisiones a tablas del sd-04 que no existen con ese número.

## Hallazgos

### Graves

**G-01. T-11.4 dice que el proponente provee el nodo local; el sd-04 dice que el Cliente lo adquiere.**
- Ubicación: líneas 272-274 y 292-298 ("El único hardware que provee Only Simple Solutions es el nodo local de tienda"); línea 553 ("Reposición de cargo del proponente"); línea 628 ("Tabla 4.11 ... reparto de responsabilidades").
- Fuente: sd-04 Tabla 4.15 (línea 729): "Tienda: Especificación, configuración y certificación del nodo local ... / Cliente: Adquisición de los servidores". sd-04 línea 707: el proponente "especifica, configura y certifica el equipo ... que el Cliente adquiere, instala y contrata". verdad_proyecto línea 19 dice lo mismo.
- Debería decir: el nodo local (44 + 5 repuestos) se especifica y certifica por el proponente y se adquiere por el Cliente; mover la Tabla T-11.5 a la sección "de cargo del Cliente" o redactar la tabla como "Hardware especificado por el proponente". Corregir también la reposición de la línea 553 (o justificar que el proponente repone como garantía).
- Matiz: T-9 (OSS-Formulario-T-9.tex línea 1533) dice "Only Simple Solutions (Dell Technologies u opción equivalente): provisión, configuración, recepción y pruebas" para componentes on-premise. Es decir, T-9 apoya a T-11 y contradice al sd-04. Hay que decidir cuál manda; el sd-04 y la verdad vigente mandan, por lo que T-9 y T-11 deben alinearse a la Tabla 4.15.
- Confirmado (contradicción interna del proyecto). Qué decisión se toma, por confirmar con el equipo.

**G-02. El DC-01 no tiene hardware ni obras especificadas en el T-11, y T-11.7 contradice la Tabla 4.15.**
- Ubicación: líneas 380-413 (T-11.7), en especial línea 406 ("Equipos del Cliente; el proponente aporta software de adaptadores y la conexión privada"), línea 410 ("Energía, climatización y seguridad física: A cargo del Cliente") y línea 413 ("El proponente no instala servidores nuevos en DC-01 ni en DC-02").
- Fuente: sd-04 Tabla 4.15 (línea 732): el proponente provee en DC-01 la "Habilitación del recinto técnico con su especificación, equipos, conectividad, seguridad y canalizaciones de cableado". sd-04 4.3.1 (líneas 744, 784-786): par de FortiGate activo-pasivo, pila de switches de núcleo, racks de servidores independientes de los de comunicaciones, almacenamiento en red y respaldo local por zona, cinta en custodia, UPS de al menos 30 min a plena carga, generación autónoma de 24 h con combustible, climatización N+1, detección por aspiración y extinción por agente limpio, control de acceso biométrico, videovigilancia con 30 días, sala técnica principal (RT-06.01 a 06.24). Bases Transv. 6.1: declarar la tipología por sitio; RT-06.33 y 14.2 de las Bases Admin. (verdad línea 19: el proponente provee la infraestructura on-premise del DC-01).
- Debería decir: una tabla T-11.7 del DC-01 con cada equipo (FortiGate o equivalente, switches de núcleo, racks, almacenamiento, UPS, generador, climatización, incendio, acceso, video, cinta), cantidades y características mínimas, la tipología declarada (sala técnica principal en DC-01; sala secundaria o de sitio en DC-02 y CD; gabinete en tiendas) y quién adquiere. Hoy la fila "Energía, climatización y seguridad física: a cargo del Cliente" contradice la 4.15 y RT-06.33.
- Confirmado.

**G-03. Cantidades de red de tienda: el T-11 pone 1 conmutador y 1 router/firewall por tienda; el sd-04 diseña una pila de 2 switches y un par de FortiGate activo-pasivo.**
- Ubicación: líneas 328-329 (filas 5.1 y 5.2: "13 como mínimo, uno por tienda"), 331 (UPS para "2 nodos, el conmutador y el router y firewall"), 341.
- Fuente: sd-04 línea 717 ("pila de dos switches ... par de FortiGate ... activo-pasivo"), línea 730 (Tabla 4.15), línea 600 ("el par de FortiGate de la tienda"). Las Bases RT-08.03 exigen alta disponibilidad sin punto único de falla en conmutadores y cortafuegos.
- Debería decir: 2 switches y 2 firewalls por tienda sin segmentación (26 de cada uno en las 13 tiendas; 44 si se consideran las 22) con la diferencia de qué se adquiere en las 9 tiendas ya segmentadas; o el sd-04 debe cambiar. Hoy el T-11 incumple RT-08.03 y descuadra el gabinete y la UPS.
- Confirmado.

**G-04. Alcance de la red de tienda incompleto: faltan puntos de acceso Wi-Fi, red de móviles y mesón financiero, grabador de video y respaldo LTE/5G.**
- Ubicación: línea 328 (VLAN "cajas, administración, Emisor, video y Wi-Fi de clientes" = 5 redes), tabla T-11.6 (líneas 367-374).
- Fuente: sd-04 línea 715: seis redes (cajas, administración, móviles, video, Wi-Fi de clientes, mesón financiero), punto de acceso corporativo con certificado y otro aislado para clientes, cámaras y grabador de 30 días; línea 719: el respaldo en tiendas sin segundo enlace es una conexión LTE/5G de otro operador.
- Debería decir: seis VLAN; filas para los puntos de acceso Wi-Fi (cantidad por tienda por definir con el levantamiento); el grabador de video queda como equipo existente del Cliente o se especifica; los enlaces de respaldo de 6.2 y 6.3 indicar "LTE/5G de otro operador" o un camino distinto (el T-11 dice solo "camino y proveedor distintos").
- Gravedad: grave por cantidad y alcance de hardware. Por confirmar si los puntos de acceso son existentes o se compran.

**G-05. Faltan las estaciones de trabajo de operación y administración (cap. 8.2) y los atributos exigidos de hardware.**
- Ubicación: ausencia en todo el formulario; solo hay una mención indirecta en la línea 265 ("estaciones de operación" en Defender).
- Fuente: Bases Transv. RT-08.07 (estaciones con monitores duales, en la cantidad que determine el dimensionamiento), RT-08.08 (NCh 2527, eficiencia energética), RT-08.09 (gestión central, cifrado, EDR); RT-08.01 (marca, modelo de referencia, procesador, memoria, almacenamiento, interfaces y consumo, con cálculo de dimensionamiento); RT-08.10 a 08.13 (marca, modelo de referencia, cantidad, características mínimas, accesorios, consumibles, grado de protección IP y caídas, ciclo de vida, repuestos y plan de reposición durante los 56 meses); RT-08.05 (margen de crecimiento en %); RT-08.15 (unidad de cada tipo para pruebas, deseable).
- Debería decir: una fila de estaciones de trabajo (o declarar que no aplican y por qué, con remisión a quien opera) y, para cada hardware, marca y modelo de referencia o la decisión expresa de no fijarlos. Las filas 5.5 a 5.9 ("Se conservan") sí son coherentes con el Caso, pero no declaran ciclo de vida, IP ni caídas de los dispositivos que se conservan; el nodo y los equipos nuevos tampoco declaran consumo, margen de crecimiento en % ni accesorios. La propia Tabla T-11.5 (línea 292) da "Dell Technologies u opción técnicamente equivalente" sin modelo ni procesador, memoria o disco.
- Por confirmar el nivel de detalle admisible mientras el modelo se fije en el ensayo de 24 h (el formulario lo declara en línea 301 y en la Tabla T-11.14). Aun así, el RT-08.01 es obligatorio y el formulario debería decir "modelo de referencia por fijar en el mes X" en una celda explícita, y dar un mínimo numérico (p. ej. núcleos, GB de memoria, TB de disco) o justificar su ausencia.

**G-06. Cantidades de nube remitidas a la "memoria de capacidad", que no las contiene.**
- Ubicación: filas 1.2, 1.3, 1.5, 1.6, 1.23 (líneas 159, 160, 162, 163, 180) y línea 188 ("Las demás cantidades de capacidad se obtienen del método de dimensionamiento de esa misma sección"); tabla T-11.14 línea 618 ("Memoria de capacidad ... H2, mes 4").
- Fuente: `04_Adjuntos/tablas/sd-04_s2_memoria-capacidad.md` ("Uso en el diseño": las unidades, particiones, capacidad de PostgreSQL y nodos de AKS "se derivan en el diseño detallado"). Solo entrega 6 de las 17 dimensiones del Caso 14.2.
- Debería decir: un valor numérico o un rango para nodos de AKS por clúster, unidades y particiones de Event Hubs, clase de cómputo de PostgreSQL, tamaño de Managed Redis y de los grupos de nodos del cómputo predictivo; o decir expresamente "por fijar en H2, mes 4" en una columna "estado". El texto actual presenta la memoria como fuente de esas cantidades y la memoria remite al diseño detallado: la remisión es circular.
- Confirmado.

**G-07. Key Vault y HSM del Emisor: el T-11 resuelve lo que el sd-04 deja condicionado.**
- Ubicación: fila 1.11 (línea 168): "Azure Key Vault, nivel Premium, con claves protegidas por módulo de seguridad de hardware ... sin equipo dedicado en sitio".
- Fuente: sd-04 Tabla 4.6 (línea 442) y Tabla 4.9 (línea 536) y 4.3.1 (línea 772): "Key Vault y, para la filial emisora, Managed HSM", "sujeto a su disponibilidad en la región". verdad_proyecto línea 17: HSM "producto por definir". T-10 (línea 465): "HSM para las llaves del Emisor cuando corresponda".
- Debería decir: Key Vault Premium para las bóvedas de Retail y Managed HSM para el Emisor, condicionado a la disponibilidad regional (comprobación de la Tabla T-11.14), o dejar el HSM del Emisor como "producto por definir" con la alternativa. Hoy el T-11 omite Managed HSM, que figura en dos tablas del sd-04.
- Confirmado (omisión) / por confirmar (qué producto).

**G-08. Titular de las suscripciones y licencias: el T-11 dice Cliente; el sd-04 dice que el proponente las contrata y opera.**
- Ubicación: línea 507-509 (Titular Cliente para Azure, Entra, Power BI, Sentinel, Defender, GitHub, SonarQube, Jira, SharePoint, Slack), línea 487.
- Fuente: sd-04 línea 524: "El proponente las contrata y opera"; Tabla 4.15 (línea 731): "Nube: Suscripciones, servicios Azure, configuración y operación" a cargo del proponente.
- Además GitHub, SonarQube, Jira, SharePoint y Slack (T-11 fila 3.7, "ya comprometido") son herramientas de trabajo del proponente, no del Cliente; ponerlas a nombre del Cliente no tiene fundamento en las Bases (por confirmar si algún artículo exige licencias a nombre del Cliente; el T-11 afirma que "se constituyen a nombre del Cliente, son transferibles" sin citar fuente).
- Debería decir: separar licencias que adquiere el proponente para operar (Azure durante el contrato, herramientas de entrega) de las que se transfieren al Cliente, y alinear con la Tabla 4.15.
- Por confirmar.

### Medianas

**M-01. Remisiones a tablas del sd-04 con numeración que no existe en el archivo actual.**
- T-11 cita "Tabla 4.11" como la de hardware y reparto de responsabilidades (líneas 274, 290, 326, 365, 399, 628); en el sd-04 la Tabla 4.11 es "Puntos de falla y contingencia" y la de implementos es la **Tabla 4.15**.
- T-11 cita "Tabla 4.10" para evidencia/diario local/nodo (líneas 166, 225, 256): en el sd-04 la 4.10 es "Subredes".
- Cita "Tablas 4.2, 4.6, 4.7, 4.10 y 4.11" como fuente de la T-11.2 (línea 212) y "Tablas 4.4 y 4.11" en la T-11.8 (línea 434): 4.2 (servicios) y 4.4 (plataformas) coinciden; 4.7 es emplazamiento, no hay software; 4.10 y 4.11 no corresponden.
- Cita "Tablas 4.6 a 4.9" y "Tabla 4.9" (línea 365, 615): 4.9 es servicios Azure; para enlaces corresponde 4.8 y 4.11.
- Corrección: sustituir por 4.15 (hardware y reparto), 4.9 (servicios Azure), 4.10 (subredes), 4.11 (puntos de falla), 4.8 (nodos y códigos de sitio, esta sí correcta).
- Confirmado.

**M-02. Productos del sd-04 que no aparecen en el T-11.**
- Fuente: sd-04 Tabla 4.9 (líneas 532-537) y texto de redes (552-554): Application Gateway (uno por ámbito), FortiGate-VM x2 en el hub (SD-WAN), Route Server, Azure Bastion, protección DDoS, NAT Gateway, Managed HSM, Entra Private Access, Azure Arc, Azure Policy, gestión de costos, Backup Vault (el T-11 sí tiene Azure Backup), DNS público.
- El T-11 no las incluye; tampoco incluye la cinta en custodia de DC-01 (sd-04 línea 644, política 3-2-1-1-0; RT-06.7 de la copia fuera de línea).
- Debería decir: filas para cada producto con su nivel y cantidad, o aclarar que se agrupan. Confirmado.
- Contraparte: el T-11 incluye servicios que no están en la Tabla 4.9: Azure Container Registry Premium (el sd-04 lo lista como "Container Registry", sin nivel, ok), Log Analytics con retención de "12 meses en línea y 24 en archivo" (línea 170, atribuida a "SD-04, 4.3.1": no se encuentra en el sd-04; es posible que provenga del sd-05, que habla de 12 meses para Retail; verificar).

**M-03. Búsqueda: el sd-04 deja "por decidir en la Etapa 1" y el T-11 la omite; además el índice vectorial del sd-13 usa pgvector.**
- Ubicación: ausencia en T-11.1/T-11.2; línea 476 (pgvector sobre el PostgreSQL de Retail).
- Fuente: sd-04 Tabla 4.6 (línea 440), Tabla 4.13 (línea 673) y Tabla 4.9 (línea 540): "La búsqueda se decide en la Etapa 1 ... se aloja en la subred de datos". Alternativas: Elastic Cloud y OpenSearch.
- Debería decir: una fila de búsqueda con estado "por definir en la Etapa 1" y las alternativas, y aclarar si la búsqueda vectorial del sd-13 queda cubierta por pgvector. Confirmado (omisión). Lo mismo para HSM y SIEM (ver M-04).

**M-04. Productos que la verdad vigente marca como "por definir" y el T-11 fija: SIEM (Sentinel), herramientas DevSecOps (GitHub Actions, SonarQube, Trivy, Syft, Cosign, ZAP, Pact, Playwright, k6).**
- Ubicación: filas 3.1 a 3.9 (líneas 257-265).
- Fuente: verdad_proyecto línea 17 ("HSM, SIEM, búsqueda, motor analítico y herramientas DevSecOps: producto por definir"). sd-04 Tabla 4.6 (línea 444) mantiene "Reutilizar el canal del Cliente" y la Tabla 4.9 lista **Azure Pipelines** como herramienta de entrega, mientras T-10 y T-11 usan **GitHub Actions**.
- Debería decir: alinear sd-04, T-10 y T-11 en un solo producto de entrega (GitHub Actions o Azure Pipelines). Decidir si el T-11 declara Sentinel como seleccionado (el sd-04 lo nombra en la Tabla 4.9, por lo que el T-11 sí tiene respaldo) o como pendiente. La fila 3.10 está bien como "por seleccionar".
- Por confirmar con el equipo; la contradicción GitHub Actions / Azure Pipelines es confirmada.

**M-05. Regiones Azure: el T-11 declara dos, pero el sd-04 usa un tercer origen para Front Door y una puerta VPN y un túnel entre hubs en CLD-02 que el T-11 omite.**
- Ubicación: fila 1.14 (línea 171), fila 1.20 (línea 177), tabla T-11.6 fila 6.6 (línea 372), tabla T-11.8 (líneas 401-410).
- Fuente: sd-04 línea 576: Front Door Premium no ofrece Private Link en Chile Central; "la conexión privada hacia el ámbito de Chile Central se crea en otra región compatible, con una latencia adicional que se mide, y se configura al menos un origen con otra región de Private Link". sd-04 línea 800: "Puerta VPN" en el hub de CLD-02; ExpressRoute solo hacia Chile Central; DC-01 llega a CLD-02 por un túnel VPN, más otro túnel entre los dos hubs. Línea 800 también: Application Gateway propio de Brazil South.
- Debería decir: en la fila 1.14 nombrar la región compatible de Private Link (por definir) como ubicación adicional; en 1.20 y 6.6, una puerta de VPN en CLD-02 y 2 túneles adicionales (DC-01 a CLD-02, entre hubs). Hoy 6.6 declara "1 circuito y 1 túnel".
- Confirmado. Por definir cuál es la tercera región.

**M-06. Clúster AKS: "Un clúster por ámbito" no cubre la plataforma compartida (X-01, adaptadores, agentes, registro).**
- Ubicación: fila 1.2 (línea 159), fila 2.9 (línea 222).
- Fuente: sd-04 línea 554: "La base tecnológica aloja X-01 y los adaptadores, los agentes que despliegan las versiones y el registro de imágenes", rama propia (Tabla 4.10 línea 571).
- Debería decir: clúster (o grupo de nodos) también en la rama compartida, o explicar dónde corre X-01. Hoy 2.9 pone todos los servicios "AKS en CLD-01, ámbito Retail, Emisor y frontera" sin cluster para la frontera. Confirmado.

**M-07. Cantidades de repuestos de la red y de terreno ausentes.**
- Ubicación: líneas 341 y tabla T-11.6.
- Fuente: Bases Transv. 8.4: stock de repuestos al menos 10 % del parque por tipo de componente crítico; dispositivos de terreno, reemplazo en sitio equivalente a 10 % con configuración precargada.
- El texto dice "una existencia de reemplazo del 10 % en sitio" pero no da el número para conmutadores, firewalls, UPS ni dispositivos (solo el nodo, 5). Para 26 firewalls o 22 UPS el número no es 0. Debería decir: repuestos por tipo (p. ej. 3 switches, 3 firewalls, 3 UPS) o una fila. Los repuestos del nodo "en bodega en Chile" (línea 296) no cumplen "en sitio" para dispositivos de terreno si el nodo se considera de terreno; verificar con RT-08.4 (el nodo es crítico, por lo que bodega en Chile basta). Por confirmar.

**M-08. Distancia entre CLD-01 y CLD-02: "2.600 km aproximadamente" no está en el sd-04.**
- Ubicación: línea 405.
- Fuente: sd-04 línea 746: "La distancia exacta entre los sitios y el análisis formal de amenazas comunes se declaran con su fuente antes de aprobar el diseño detallado (RT-07.02)". Ninguna otra mención en el sd-04. El dato es verosímil (Santiago a São Paulo), pero el T-11 lo introduce sin fuente y el sd-04 lo difiere.
- Debería decir: citar la fuente o dejarlo como "por declarar con fuente" y alinear con el sd-04. Por confirmar.

**M-09. Nombres de las innovaciones en T-11.9 difieren del sd-13 y de la verdad vigente.**
- Ubicación: tabla T-11.10 (líneas 473-479): "Casilleros de retiro", "Red de medios", "Conteo cíclico predictivo".
- Fuente: verdad_proyecto línea 24 y sd-13: "Lockers Ancoa 24/7", "Retail Media Network", "Modo Tienda con fila virtual de probadores". Los productos de referencia (Cleveron 355, Zebra KC50 22", Epson TM-T20III, Criteo, Jina CLIP v2, scikit-learn HistGradientBoosting, pgvector) coinciden con el sd-13. La licencia de Jina: el sd-13 (línea 187) dice que la descarga es CC BY-NC, el T-11 dice "licencia comercial; el suministro incluye la licencia"; consistente.
- La cantidad "Según el Subdocumento 13" en lockers y tótems traslada la cantidad sin darla; verificar si el sd-13 la da (no la encontré en las líneas revisadas). Debería decir: la cantidad o "por fijar tras el levantamiento" explícito.
- Mediana (nombres) / por confirmar cantidades.

**M-10. Versiones y niveles imprecisos ("la versión vigente al inicio de la construcción").**
- Ubicación: filas 2.2, 2.3, 2.4, 2.5 (líneas 215-218), 1.2 (nivel Standard sin sd-04), 1.5 ("De uso general o Con optimización de memoria" sin elegir), 1.10 (P2) y 1.11/1.14/1.15/1.22 (niveles que el sd-04 no fija).
- Fuente: encargo (cada producto con nivel y versión). Los niveles que el sd-04 deja remitidos al T-11 son los marcados "nivel T-11" (Origen), y sí quedan resueltos salvo PostgreSQL (dos opciones) y Redis (sin tamaño). Spring Boot "línea 4, versión menor con soporte" no da la versión; PostgreSQL "la mayor más reciente" no da el número (el propio formulario cita 17 y 18); Kubernetes "versión admitida"; TypeScript y React "vigentes".
- Debería decir: PostgreSQL 18 (o 17) y Kubernetes 1.x concreta; Spring Boot 4.0 o 4.1 con su fecha de fin; o aceptar la regla con una nota. Baja a mediana: el Formulario no exige versión, pero la T-11.2 la promete ("con la versión ofertada").
- La fila 2.1 dice "distribución OpenJDK con soporte" y la T-11.11 usa fechas de soporte de Oracle (Java SE Support Roadmap) para esa distribución; el soporte depende del distribuidor elegido, no decidido. Por confirmar.

**M-11. Referencias a la EDT y a hitos no verificables en el sd-07.**
- Ubicación: paquetes 1.4.7 (línea 522), 1.4.8 (341, 619), 1.4.9 a 1.4.13 (625), cuenta 1.15.4 (556); hitos H2 mes 4 y H3 mes 6 (618-625).
- Fuente: sd-07 define H2 en el mes 4 y H3 en el mes 6 (líneas 466 y 689-690), lo que coincide. Los números de paquete de la EDT no aparecen en el texto del sd-07 que busqué; pueden estar en el T-14 (no revisado aquí). Por confirmar contra el T-14.
- Además: el hito "Antes de Etapa 1" (línea 623, prueba de permisos y linaje) no es un hito del plan; fijar un mes.

**M-12. Cobertura de las filas de enlaces: DC-01/DC-02 y centros.**
- Ubicación: líneas 372-373.
- Fuente: sd-04 líneas 474 y 800 (DC-02 con enlace propuesto con DC-01, a cargo del Cliente; DC-01 a CLD-02 por VPN). Está bien que 6.7 sea del Cliente, pero T-11.6 da "Provee: Cliente" para el enlace de 6.5 (CD-02 segundo enlace) y el sd-04 línea 733 dice que el Cliente adquiere "equipo, obras y enlaces". Coincide. Observación menor: 6.6 dice que el proponente "provee" el circuito ExpressRoute (línea 372, "Proponente"); en la Tabla 4.15 el enlace de proveedor lo contrata el Cliente ("enlaces de proveedores" son del Cliente en la fila Red de sitio). El circuito ExpressRoute lo contrata el titular de la suscripción (proponente según sd-04) con un proveedor de conectividad; aclarar quién paga y contrata. Por confirmar.

### Bajas

**B-01. Introducción cita "Formulario T-7 y Formulario T-21" (línea 94) como si ambos definieran el T-11.** El T-11 se define en las Bases Admin. línea 2278; el T-7 (línea 2386) lo lista dentro del subdocumento 4 (c) y el T-21 es la ponderación. Referir al T-7 y al texto del T-11 en las Bases; sacar el T-21 o decir "evaluación". Confirmado.

**B-02. Alojamiento "Misma comuna ambos" (línea 402) sin nombrar la comuna.** El Caso no la nombra en lo revisado; ok como está. Sin acción.

**B-03. Variantes de nombre.** "Núcleo Retail de 2009" (línea 441) correcto; "Plataforma de crédito de 2011" correcto; "Filial emisora"/"Emisor" bien usados; "canal digital" no aparece; "plataforma compartida" y "Compartido/compartida" alternan en la columna Ámbito (líneas 158, 171, 174, 175); unificar. El sd-04 usa "base tecnológica" para la rama compartida; el T-11 usa "plataforma compartida" y "radio" (línea 175, 1.18) en lugar de "rama" del sd-04 ("radios", "ramas", "spokes"); unificar con el glosario del sd-04.

**B-04. Las filas 5.5 a 5.9 usan "Se conservan los existentes" en la columna "Referencia de marca".** Es honesto con el Caso, pero con la regla de RT-08.10 (marca y modelo) conviene indicar "marca y modelo existentes por inventariar".

**B-05. RT-08.10 pide "costo unitario estimado".** El T-11 no lo da y declara "sin precios" (línea 131), lo que es correcto con el art. 50 (Sobre 2 sin precios). Añadir una frase: "el costo unitario estimado de RT-08.10 consta en el Sobre 3". Por confirmar que el Sobre 3 lo recoge.

**B-06. Distinción "Caso proyecta hasta 25 tiendas" (línea 301).** Correcto: Caso línea 735 "22 → hasta 25". Cálculo 25 tiendas = 50 nodos, repuestos 5 (10 % de 50 = 5) correcto.

## Verificaciones sin hallazgo

- 22 tiendas, 2 centros, DC-01 140 m², 380/430 líneas de caja, 640 móviles / 3.820 personas, 44 nodos + 5 repuestos (10 % de 44 = 4,4 redondeado a 5): coherentes.
- 13 tiendas sin segmentación = 22 menos 9: coherente con sd-04 línea 578.
- 14 enlaces de respaldo nuevos (6+8), 7 mínimo exigible y SUP-28: coherente con sd-04 línea 480.
- Regiones: Chile Central (`chilecentral`) y Brazil South (`brazilsouth`), tres zonas cada una, activo-pasivo, RTO 4 h, RPO 15 min, ensayo dos veces al año: coherentes con sd-04 4.3 y RT-07.
- Event Hubs Premium con un espacio de nombres por ámbito, APIM Premium clásico con 3 unidades por instancia, PostgreSQL Flexible con HA entre zonas, Managed Redis solo Retail y su retiro del 30-sep-2028, ADLS Gen2, Power BI, motor analítico por decidir (fila 1.8): coherentes con sd-04 Tablas 4.6 y 4.9.
- Producción: etapa 1 mes 16, innovaciones mes 21 salvo conteo (mes 16): coherente con verdad_proyecto. 56 meses de licencias coherente.
- Nueve plataformas, tratamiento (ERP/DTE conservado, WMS conservado, núcleo y crédito reemplazados por olas, POS tienda por tienda, motor de precios capacidad nueva): coherente con sd-04 Tabla 4.4.
- Fortinet y Dell se escriben con "u opción técnicamente equivalente", lo que respeta que no están decididos. Sin embargo el sd-04 línea 448 dice "sin fijar aún fabricantes" y a la vez nombra FortiGate en el texto (líneas 533, 552, 715-717, 784); el T-11 es coherente con la verdad vigente, pero no con la nomenclatura FortiGate del sd-04. Alinear: el sd-04 debería decir "firewall tipo FortiGate".
- Sin precios, tarifas ni montos en el .tex (art. 50).
- Alianza declarada solo con Microsoft Azure: el T-11 no declara alianza con Fortinet ni Dell.
