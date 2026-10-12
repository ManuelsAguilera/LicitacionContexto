> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión Formulario T-12, tramo líneas 741-1480 (RT-02.08 a RT-26.08)

Archivo: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-12.tex`. Definición oficial: `Bases_Administrativas.md:2282-2288`. Requisitos: `Bases_Transversales.md` (cap. 2-26) y `Caso_09_Cadena_Multitienda.md:784-816` (cap. 15). Contraste: sd-01 a sd-04 en `02_Propuesta/latex_final/`. Solo lectura; nada fue editado.

## 0. Resultado general

- Completitud: los 367 RT del tramo (RT-02.08 a RT-26.08) están presentes, sin faltantes ni duplicados, y cada código existe en las Bases Transversales. Las descripciones copian el texto del RT. Las únicas diferencias textuales son signos de puntuación, "developers" por "desarrolladores" (l.877) y una corrupción en RT-24.01 (l.1429, ver H-31).
- Columnas: la tabla tiene las cinco que pide el T-12 de las Bases Administrativas (ID, Descripción, Cumple, Componente que lo satisface, Sección de la propuesta). Las Bases Transversales 1.5 (l.89-95) piden además "cumple / cumple parcialmente / no cumple", componente "individualizado por nombre y versión", "sección y página" y "evidencia con que se verificará". El formulario solo usa Sí/No (nunca Parcial), no tiene columna de evidencia, no da versiones ni páginas.
- Problema estructural (grave): 135 requisitos Obligatorios y 8 "Según caso" figuran "No" con "-" en componente y sección (143 de 367). Las Bases Transversales 1.4 (l.79-86) dicen que un obligatorio incumplido u omitido da puntaje cero y, si es de seguridad, continuidad o arquitectura, habilita la exclusión (art. 58). Muchos de esos "No" son campos sin completar y no incumplimientos reales (varios sí están cubiertos en sd-04 o sd-05, ver sección 3). Además 28 Deseables dicen "No" (no penaliza, pero pierde puntaje).
- Problema estructural (grave): gran parte de los "Sí" apunta a una arquitectura anterior a los sd-01 a sd-04 reconciliados. Usa códigos M-xx, "Z1/Z2/Z3", "Site Principal/Secundario", Kong, Keycloak, Wazuh, OpenTofu, Argo CD, Patroni, Elastic Cloud, Prometheus/Loki/Grafana, PWA, APC/Schneider, Dell/HPE, y remite a tablas del sd-04 que hoy son otras. Ningún término de ese grupo aparece en sd-01 a sd-04 (verificado con grep: Kong, Keycloak, Wazuh, OpenTofu, Ansible, Argo, Patroni, Semgrep, ZAP, Trivy, Cosign, Syft, Prometheus, Loki, Grafana, PWA, APC, Dell, HPE, DSCP, ZTNA = 0 apariciones; "Elastic" solo como alternativa pendiente, sd-04 l.440).
- Remisiones a otros subdocumentos: el formulario cita "Subdocumento 5" con secciones 5.5, 5.6, 5.7, 5.8.x, 5.10, 5.11.x y "Subdocumento 13, Anexos A.1 a A.5". El sd-05 vigente tiene 5.1 a 5.4 (5.1.1-5.1.9, 5.2.1-5.2.6, 5.3.1-5.3.5, 5.4.1-5.4.5), por lo que la mayoría no existe. No verifiqué el sd-13.

## 1. Conteo Cumple (Sí) / No cumple (No) / Parcial por capítulo RT (solo tramo)

Parcial = 0 en todo el tramo (el formulario no lo usa).

| Capítulo | Tramo | Sí | No | Parcial | Obligatorios/Según caso en "No" |
| :-- | :-- | --: | --: | --: | --: |
| RT-02 | 02.08 a 02.14 | 7 | 0 | 0 | 0 |
| RT-03 | 03.01 a 03.24 | 17 | 7 | 0 | 4 (03.01, 03.06, 03.15, 03.23) |
| RT-04 | 04.01 a 04.14 | 14 | 0 | 0 | 0 |
| RT-05 | 05.01 a 05.30 | 17 | 13 | 0 | 11 |
| RT-06 | 06.01 a 06.34 | 33 | 1 | 0 | 0 (06.34 Deseable) |
| RT-07 | 07.01 a 07.14 | 13 | 1 | 0 | 1 (07.02) |
| RT-08 | 08.01 a 08.19 | 19 | 0 | 0 | 0 |
| RT-09 | 09.01 a 09.10 | 7 | 3 | 0 | 2 (09.03, 09.07) |
| RT-10 | 10.01 a 10.09 | 8 | 1 | 0 | 1 (10.05 Según caso) |
| RT-11 | 11.01 a 11.28 | 24 | 4 | 0 | 2 (11.12, 11.26) |
| RT-12 | 12.01 a 12.13 | 5 | 8 | 0 | 7 |
| RT-13 | 13.01 a 13.12 | 2 | 10 | 0 | 9 |
| RT-14 | 14.01 a 14.09 | 1 | 8 | 0 | 7 |
| RT-15 | 15.01 a 15.09 | 3 | 6 | 0 | 4 |
| RT-16 | 16.01 a 16.34 | 13 | 21 | 0 | 18 |
| RT-17 | 17.01 a 17.08 | 3 | 5 | 0 | 4 |
| RT-18 | 18.01 a 18.10 | 0 | 10 | 0 | 9 |
| RT-19 | 19.01 a 19.10 | 1 | 9 | 0 | 9 |
| RT-20 | 20.01 a 20.08 | 1 | 7 | 0 | 7 |
| RT-21 | 21.01 a 21.22 | 2 | 20 | 0 | 19 |
| RT-22 | 22.01 a 22.09 | 0 | 9 | 0 | 8 |
| RT-23 | 23.01 a 23.10 | 4 | 6 | 0 | 2 |
| RT-24 | 24.01 a 24.06 | 0 | 6 | 0 | 5 |
| RT-25 | 25.01 a 25.10 | 0 | 10 | 0 | 9 |
| RT-26 | 26.01 a 26.08 | 2 | 6 | 0 | 5 |
| Total | | 196 | 171 | 0 | 143 |

(RT-02 en este tramo parte de RT-02.08, l.741. El total del tramo es 367; los 143 son Obligatorio o Según caso con "No".)

## 2. Hallazgos

Convención: gravedad (G grave, M mediana, B baja). Estado: C confirmado, X por confirmar. Las líneas son del T-12 salvo que se indique.

### 2.1 Valores que rebajan umbrales o contradicen el RT / el Caso

H-01 (G, C) l.773 RT-03.10. Dice "Sí" con "autonomía de 8 h (valor del caso, RT-03.10-C) y CD 4 h", y cita sd-04 4.1 y 4.2 (Tabla 4.9). El RT transversal exige 24 h o el mayor que fije el caso; el Caso dice mínimo 8 h (Caso l.790) y prevalece el más exigente (Caso l.786, Transversales 1.3). sd-04 l.384, 470 y 626 declara 24 h para la tienda (4 h para CD-01); sd-02 RES-05 y SUP-07 también 24 h. Debe decir: "nodo local de tienda, 24 horas sin enlace (el Caso pide 8 h; rige la mayor); CD-01, 4 h". La Tabla 4.9 de sd-04 son servicios Azure; las remisiones correctas son Tabla 4.11 (puntos de falla) y 4.2 "Alta disponibilidad...".

H-02 (G, C) l.1275 RT-17.01. Declara "PWA de Punto de Venta ... replicada en el nodo de tienda para operar 8 horas sin conexión". Rebaja 24 h (Caso l.788: los perfiles internos operan sin conexión conforme a RT-03.10). Además el Caso exige cinco perfiles (cliente, vendedor de sala, preparación de pedidos, conteo cíclico/prevención de pérdidas, recepción), y solo se declara el POS. sd-04 no usa "PWA" ni "service workers" (solo "TypeScript y React para portales y vistas POS", Tabla 4.6, estado "Por probar"). Debe ser Parcial hasta declarar los cinco perfiles y las 24 h.

H-03 (G, C) l.1033 y l.1035. RT-09.05 y RT-09.06. RT-09.06 (1,5 veces el peak) está bien (verdad_proyecto, sd-03 3.4.1 l.657). RT-09.05 remite a "Supuestos del emplazamiento, Tabla 4.8" y nombra "enlace de respaldo de las 14 tiendas" como cuello de botella. sd-04 solo supone que las ocho tiendas a la calle (más Coyhaique) no tienen respaldo (l.480) y la Tabla 4.8 es de nodos, no de cuello de botella. Sugerencia: Parcial y reescribir citando la Tabla 4.14 (carga) o dejar el cuello de botella a la memoria de capacidad. Estado X.

H-04 (G, C) l.1213 RT-16.04. "Catálogo atómico de 223 requerimientos funcionales y 75 no funcionales". Verdad vigente: catálogo 3.1 con 308 elementos (227 RF, 72 RNF, 9 OP). El sd-03 l.306 aún dice 307 (223/75/9): hay inconsistencia entre sd-03 y verdad_proyecto. Corregir a 227/72/9 (308) en cuanto el sd-03 se concilie. Estado C para el formulario, X para la cifra del sd-03.

H-05 (G, C) l.1057 RT-10.07. Declara "ingeniería del caos dirigida sobre los cinco tipos de falla exigidos" y cita sd-04 Tabla 4.9. Tabla 4.9 es "Servicios contratados en Azure" y sd-04 no menciona ingeniería del caos ni inyección de fallas (grep "caos" = 0); solo tiene "falla de zona simulada" y ensayo de conmutación (Tabla 4.11). Parcial; remitir a Tabla 4.11 y al ensayo bianual (4.3.2), y reconocer que falta el plan de pruebas de resiliencia (sd-09).

H-06 (G, C) l.797 y l.1121 y siguientes sobre identidad. RT-12.01 declara "Keycloak, dos instancias sin confianza transitiva (Z1 y Z3), OIDC y OAuth 2.0". sd-04 Tabla 4.6 (l.442): Microsoft Entra ID federado con el directorio del Cliente, Key Vault, Managed HSM (filial), estado "Por probar". Además el RT exige OAuth 2.1; el formulario declara 2.0, que rebaja el umbral. Corregir a Entra ID y a OAuth 2.1 (o justificar). RT-12.08 repite "IAM Keycloak" (l.1135).

H-07 (G, C) l.1083 RT-11.11 "API Gateway (Kong Gateway)". sd-04 usa Azure API Management Premium (ADR-06, Tabla 4.6 l.436). Producto no decidido o equivocado. Corregir.

H-08 (G, C) l.1091 y l.1093 RT-11.15 y RT-11.16. "SIEM (Wazuh)", "Wazuh como detección en puntos finales", cita sd-04 Tabla 4.6 (donde no hay SIEM). La verdad vigente dice SIEM "producto por definir". sd-04 Tabla 4.9 (l.536) lista Defender for Cloud y Sentinel. No declarar Wazuh. Decir "SIEM por definir en la Etapa 1" y marcar Parcial, con Sentinel solo si sd-04 lo fija.

H-09 (G, C) l.759 RT-03.03 "OpenTofu ... y Ansible". sd-04 (l.444 y 590) usa Terraform. Ansible no existe en sd-04. Corregir a Terraform.

H-10 (G, C) l.811, l.813, l.1105, l.1107, l.1109 RT-04.05, 04.06, 11.22, 11.23, 11.24. Nombran Semgrep, ZAP, Trivy, OWASP Dependency-Check, Syft, Cosign, Argo CD. La verdad vigente: "herramientas DevSecOps: producto por definir". sd-04 solo tiene "Terraform y canal CI/CD ... Por probar / Reutilizar el canal del Cliente" y Azure Pipelines (Tabla 4.9). Corregir a "cadena DevSecOps con las categorías exigidas; herramientas por definir". Además RT-04.06 (l.813) declara "punto de aprobación manual adicional solo en Z3" mientras RT-04.06 exige "sin intervención manual en el paso a producción"; sd-04 l.592 dice "Producción exige una aprobación explícita" para ambos ámbitos. Es contradicción real: Parcial o declarar la excepción.

H-11 (G, C) l.987 RT-08.01 "Servidor Dell PowerEdge R660 / HPE ProLiant DL380 Gen11 o equivalente". Marcas no decididas (verdad: "Fortinet y Dell no están decididos"; sd-04 l.448: "sin fijar aún fabricantes"). sd-04 l.738 deriva el detalle al Formulario T-11 y al inventario xlsx. Quitar marcas o dejar solo la categoría. La remisión "Tabla 4.11" (puntos de falla) es errónea; el equipamiento está en 4.2.1 y Tabla 4.15.

H-12 (G, C) l.903 RT-06.07 "UPS APC/Schneider Electric (línea Galaxy)" y l.911 RT-06.11 "carga de 18 kW, PUE objetivo 1,6". Marca no decidida y cifras que sd-04 no contiene: sd-04 l.786 dice que la carga eléctrica y la ocupación de rack se declaran después, con el inventario y el informe de 2024. Debe decir "UPS de al menos 30 min" (sin marca) y RT-06.11 y RT-15.04 (l.1195, "PUE objetivo 1,6") Parcial, con cifras pendientes. Lo mismo con 40 % de margen en RT-06.05 y RT-08.05 (l.899, 995): no aparece en sd-04.

H-13 (G, C) l.965 RT-07.04 "RTO ≤ 4 h y RPO ≤ 15 min comprometidos por componente, con segundo HSM en Site Secundario". sd-04 l.628 y l.800: el RPO de 15 min no queda garantizado solo por el producto, se mide y se demuestra en ensayo; Managed HSM de la filial está "sujeto a su disponibilidad en la región" y la réplica del Emisor depende de que el Cliente apruebe la residencia (l.474, 802). Debe ser Sí condicionado o Parcial para el Emisor. "Site Secundario" no es nombre vigente (usar CLD-02, glosario).

H-14 (G, C) l.1061 RT-10.09 y similares con compromisos cuantitativos sin respaldo: "Presupuesto de error mensual de 0,1 %", "detiene el despliegue" (l.1061); "Notificación de brecha 24 h", "2 horas" (l.1097, 1099); "SLA de revocación ≤ 4 horas" (l.1139, de sd-02 RNF-59, que sí existe pero es un criterio, no un componente); "ventana 08:00 a 20:00" (l.827, 1191); "retención 12 + 24 meses" (l.1089); "7/15/30 días" (l.1069); "pruebas de intrusión anuales" (l.1101); "cobertura 70 %" (l.823). Coinciden con los RT, pero sd-04 no los desarrolla; todos citan "sd-04 4.1 Seguridad, continuidad y observabilidad", que no menciona ninguno (grep de cobertura, DORA, STRIDE, 7/15/30 = 0 en sd-04). "Cumple" afirma algo que la propuesta no escribe. Remitir al sd-09 o al sd-08 si allí se declaran; si no, Parcial.

H-15 (G, C) l.1347 RT-21.01. "Sí" con "Soporte y operación de misión crítica 24x7x365 para el canal digital ... " y cita sd-03 3.1. sd-03 3.1 no declara centro de operaciones de red 24x7x365, ubicación ni dotación (grep "24x7" en sd-03 = 0). "Canal digital" es nombre provisional (glosario, Pendientes). RT-21.01 exige declarar ubicación, dotación por turno y procedimientos. Cambiar a No/Parcial hasta que el sd-10 lo cubra; no citar sd-03 3.1.

H-16 (G, C) l.1095 RT-11.17 "SOC con cobertura 24x7" citando sd-04 4.1. sd-04 4.1 no describe un SOC, su ubicación ni dotación; solo Sentinel/Defender (l.536). Parcial.

H-17 (G, C) l.1203 RT-15.08 y l.1313 RT-19.02. Afirman "Equipo de jefaturas nominado con dedicación exclusiva ... certificaciones individuales (PMP, Azure Solutions Architect Expert, CISSP/CCSP, CDMP, CTAL-TM, DevOps Engineer Expert, Prosci)" y "Jefe de Proyecto (Vicente Rosales Miranda, PMP)", citando "sd-01 sección 1.6 'Frente de jefaturas asignado' y Tabla 1". sd-01: la 1.6 se llama "Alianzas" (l.343); no existe esa sección ni "Tabla 1"; la estructura del proyecto está en 1.5 (l.303-340); sd-01 no menciona PMP, CISSP, Prosci ni "dedicación exclusiva" (grep = 0). Afirmación sin sustento: cambiar a lo que diga sd-01 1.5 y quitar las certificaciones personales y el apellido "Miranda" si no constan.

H-18 (G, C) l.1415 RT-23.04. "alianzas tecnológicas con AWS y Microsoft Azure". sd-01 1.6 (l.345-347) declara solo Microsoft Azure; Fortinet y otros no se declaran (l.349). Quitar AWS.

H-19 (G, C) l.1265-1271. RT-16.31/16.32/16.34 Sí con "Portal del Cliente (M-11)". El código M-11 no se usa ("no se usan los códigos M-xx", glosario) y el portal público es un objeto distinto del portal de proveedor y del de vendedor (glosario). Además RT-16.30 en el Caso (l.812) es el "portal público" obligatorio, pero en la numeración transversal el portal es RT-16.31 y RT-16.30 es "exportación de información sensible" (No en el formulario). Ver también H-27.

### 2.2 "Cumple" que afirma algo que la propuesta no hace, o que contradice sd-04

H-20 (G, C) l.711 (RT-02.11). Declara "seis puntos únicos de falla (ERP, enlace Coyhaique, Site Principal, firma electrónica, enlace de 14 tiendas, M-21)". sd-04 Figura 4.16 y Tabla 4.11 declaran ocho puntos: enlace de tienda, enlace único de CD-02, ExpressRoute a DC-01, zona de Chile Central, región Chile Central, ERP/DTE, WMS, broker de eventos. Cambiar la lista y la remisión ("Tabla 4.9" por Tabla 4.11).

H-21 (G, C) l.967 RT-07.05 "Procedimiento de conmutación en 8 pasos". sd-04 l.804: seis pasos. Corregir. RT-07.06 (l.969) "retorno al Site Principal": usar CLD-01. RT-07.08 (l.973): "protección contra split-brain" no aparece en sd-04; la promoción la inicia el equipo de operación (l.628), coherente con "semiautomática". Parcial y quitar split-brain o respaldarlo.

H-22 (G, C) l.763 RT-03.05, l.757 RT-03.02, l.761 RT-03.04. Usan "Z1/Z2/Z3" y "criterio de selección N°2" (esquema antiguo). sd-04: tres zonas de disponibilidad de Chile Central (4.3.1), ámbito Retail y ámbito Emisor, hub y ramas; AKS como servicio administrado (Tabla 4.6, RT-03.05). Z1/Z2/Z3 están vetados fuera de la cita de las Bases (glosario). Reescribir con las zonas de Azure y los ámbitos.

H-23 (G, C) l.775 y l.777 RT-03.11/03.12. "outbox transaccional sobre PostgreSQL local del nodo de tienda". sd-04 Tabla 4.6 l.445: motor local "Valkey u otro motor local, por decidir". Producto no decidido. Sugerencia: "diario local L-02 con estados pendiente / enviado / confirmado / en conflicto (sd-04 4.1)". El ya mencionado requisito del Caso (Caso l.790-792: RT-03.13 sincronización ≤30 min tras 8 h, sin pérdida de venta) no aparece en la fila RT-03.12: agregar "conciliación en 30 minutos o menos (sd-04 l.388, ADR-04)".

H-24 (G, C) l.779 RT-03.13 "Tabla de funciones no disponibles offline y procedimiento manual por función". sd-04 no contiene tal tabla; solo dice que sin enlace no se originan tarjetas y que la compra con tarjeta propia puede declararse no disponible (l.386), y sd-03 3.4.5 deja la modalidad fiscal y la decisión de riesgo pendientes. La ausencia se evalúa como "observación grave". Parcial y señalar el sd donde se completará.

H-25 (G, C) l.781 RT-03.14 y l.989 RT-08.02: "RAID 10 (o erasure coding), NVMe". sd-04 l.717 dice discos "espejados" (equivale a RAID 1) en el nodo local y no declara RAID/NVMe en DC-01. RT-03.14 exige declarar y justificar el nivel RAID. Declarar "espejado (RAID 1)" para el nodo de tienda, y dejar DC-01 pendiente. Remisión "Tabla 4.11" incorrecta.

H-26 (G, C) l.1141 RT-12.11, l.1161 RT-13.08, l.1005-1023 RT-08.10-08.19, l.999 RT-08.07, l.1009 RT-08.12. Cifras y normas ("IP54", "caída desde 1,2 m", "ciclo de vida 4-5 / 5-7 años, renovación mes 40", "NIST SP 800-88", "Ley N° 20.920", "ENERGY STAR", "46 puestos", "NCh 2527") se atribuyen a "sd-04 4.2.1 (Figura 4.17, Tabla 4.11)". La Figura 4.17 es la tienda tipo y la Tabla 4.11 es de puntos de falla; esos datos no están en sd-04 (grep ENERGY STAR, 800-88, 20.920 = 0). sd-04 l.738 los deriva a T-11 y al inventario. Cambiar la remisión a T-11/inventario o marcar Parcial. "46 puestos" es dato del Cliente (personas de tecnología), no un dimensionamiento de estaciones de operación: no sirve de base.

H-27 (M, C) Capítulos 16-17: l.1267 RT-16.31 y l.1269 RT-16.32 citan "sd-04 Tabla 4.1, AH-01" y "sd-03 3.3.2, 3.4.3". Verificar que AH-01 sea el cliente: Tabla 4.1 existe (l.131), pero el portal público se llama en sd-03/sd-04 por servicio, no "Portal del Cliente". Mediana. Estado X.

H-28 (G, C) l.1259 RT-16.27 "Elastic Cloud (Elasticsearch/OpenSearch)". sd-04 l.440: búsqueda "Por decidir en la Etapa 1", Pendiente. Declarar producto no decidido es incorrecto: poner "por decidir (Elastic Cloud u OpenSearch, sd-04 Tabla 4.6)" y Parcial.

H-29 (G, C) l.1171 RT-14.01 "M-24 ... OpenTelemetry, Prometheus, Loki y Grafana, con Azure Monitor/Application Insights". sd-04 (l.443): OpenTelemetry y Azure Monitor, "Por probar". Prometheus/Loki/Grafana no están. M-24 no se usa (glosario). Corregir. Lo mismo RT-03.16 (l.785) y RT-06.14 (l.917), RT-02.09 (l.745), RT-09.08 (l.1039): "M-24". RT-06.14 además afirma monitoreo en línea de temperatura/humedad/agua que sd-04 no menciona.

H-30 (M, C) Códigos M-xx vigentes en el tramo (todos deben reemplazarse por servicios R:/F:/X-01 o ámbito): M-24 (l.745, 785, 917, 1039, 1171), M-21 (l.1063, 1219, 1223), M-23 (l.1121, 1139), M-16 (l.1237, 1239, 1241), M-11 (l.1267, 1269), M-03 (l.847). Glosario: "No se usan los códigos M-xx del sd-02 antiguo".

H-31 (M, C) l.1429 RT-24.01. La descripción termina en "una duración mínima de aparición de cros por persona". Las Bases (Transversales RT-24.01) dicen "10 segundos"; el texto quedó corrupto en el formulario. Corregir.

### 2.3 "No" que sd-01 a sd-05 sí cubren (probable omisión de llenado)

Todos Obligatorios salvo indicación. Estado X para los que dependen de sd-05 (no revisé a fondo).

H-32 (G, X) l.755 RT-03.01 "No". El proveedor y las regiones están declaradas en sd-04 4.1.1 (Tabla 4.6, l.431; ADR-07: Azure, Chile Central primaria, Brazil South secundaria, ambas con tres zonas; estado "Condicionada"). Debe ser Sí (condicionado a la carta del socio y a la residencia de datos).

H-33 (G, X) l.865 y l.867 RT-05.18, 05.19 y otros RT-05. sd-05 5.2.x existe (trazabilidad 5.2.4, exportación 5.2.6, migración 5.3.4 ensayos, 5.3.5 datos no migrados), pero el formulario dice "No" en RT-05.03 (trazabilidad), 05.06 (exportación), 05.13 (dos ensayos de migración), 05.15 (datos no migrados), 05.22 (carga masiva), 05.23 (estándares sectoriales, Según caso). Revisar contra sd-05; el Caso cap. 15 (l.800-806) fija valores de RT-05.15 y RT-05.23 que no están reflejados.

H-34 (G, C) l.887 RT-05.29 (Según caso) "No". El Caso fija 30 s (disponibilidad), 5 min (precio) y la posición financiera antes de las 07:00; sd-04 los usa (ADR-03, Tabla 4.5; l.328, 390). Debe ser Sí con esos valores. Otros Según caso en "No" con Caso aplicable: RT-10.05 (l.1053; ventana protegida, sd-03 3.2.2 y sd-04 l.596 declaran las cinco ventanas de congelamiento); RT-12.12 (l.1143; usuarios externos); RT-21.16 (l.1377; sitios alejados, Caso l.810); RT-22.04 (l.1397); RT-03.23 (l.799; red inalámbrica: sd-04 l.715 declara punto de acceso corporativo con certificado y Wi-Fi de clientes aislado, debería ser Sí); RT-05.15 y RT-05.23 (arriba).

H-35 (M, C) l.1085 RT-11.12 "No". sd-04 l.576 describe Front Door con firewall de aplicaciones web "y los bots". Cambiar a Sí/Parcial.

H-36 (M, C) l.961 RT-07.02 "No" (distancia entre sitios). sd-04 l.746 argumenta que Chile y Brasil no comparten amenazas locales y declara que la distancia exacta y el análisis formal se entregan antes de aprobar el diseño detallado. Debe ser Parcial, no "No".

H-37 (M, C) l.783 RT-03.15 (CIS Benchmarks), l.765 RT-03.06 (FinOps), l.1029 RT-09.03 (3x crecimiento): "No". sd-04 solo menciona "gestión de costos" (Tabla 4.9, l.537) para FinOps; CIS Benchmarks no aparece. Mantener "No" solo si se acepta la penalización; los tres son Obligatorios.

H-38 (M, C) l.1123-1137 RT-12.02/12.03/12.06/12.07/12.09 "No". Son Obligatorios. sd-04 usa Entra ID con Private Access y Bastion para administradores (l.552), lo que respalda al menos 12.03 y 12.06 en parte. Reconsiderar.

### 2.4 Remisiones inexistentes o equivocadas (sd-01 a sd-04)

- sd-04 Tabla 4.9 se cita como "continuidad/degradación/clasificación/ingeniería del caos/dependencias" (l.741, 745, 773, 871, 1039, 1047, 1049, 1057, 1059). Tabla 4.9 = servicios contratados en Azure. Correcta para esos temas: Tabla 4.11 (puntos de falla) y Tabla 4.12 (pérdida y recuperación).
- sd-04 Tabla 4.11 se cita como tabla de hardware (l.901, 953, 955, 987-995, 1013-1023, 1161). Hardware: 4.2.1 y Tabla 4.15.
- sd-04 Tabla 4.8 se cita como enlaces (l.787, 1033). Tabla 4.8 = nodos y comprobaciones. Enlaces: Figura 4.13 y 4.14.
- sd-04 "sección 4.3.1" como evidencia de multi-AZ y disponibilidad (l.757, 1045). 4.3.1 existe y describe tres zonas, pero RT-10.01 no se cumple solo con eso (sd-04 l.646 admite que no se apoya en los SLA sino en el diseño y que 99,94 % queda cerca del límite).
- sd-04 "sección 4.3.2 ... 8 pasos" (l.967): son seis.
- sd-04 4.2 "Redes y segmentación, Figura 4.14" (l.761, 795, 797): existe. "Ambientes, Figura 4.15" existe. "Figura 4.17" existe. "Figura 4.16 y Tabla 4.9" (l.711): Figura 4.16 existe, Tabla 4.9 no corresponde.
- sd-03 3.4.5, 3.4.6, 3.2.3, 3.2.4, 3.2.5, 3.3.2, 3.4.1, 3.4.3: existen. sd-03 3.1 como evidencia de operación 24x7 (l.1347): no la contiene. sd-03 3.2.2 (ventanas): existe.
- sd-02 "Anexo A.5.1 (SUP-25)" (l.1335): no existe A.5.1; los supuestos están en A.4.1 (SUP-25 es migración de cartera por convivencia, correcto en contenido). "Anexo A.2 Tabla A.2.10 (RNF-37 / RNF-59)" (l.1129, 1139): A.2.10 existe y RNF-37 y RNF-59 están allí (sd-02 anexos l.1296, 1298). "Tabla A.2.7 (RNF-15 / RNF-38)" (l.1209, 1217, 1223): existe (A.2.7, l.1165, 1167). "Tabla A.2.14 RNF-49" (l.1153): existe (l.1476). "Tabla A.2.1 (RNF-29 a RNF-31)" (l.1359): RNF-29 está en A.2.1 (l.899); RNF-30 y 31 no verificados. "Anexo A.1 RF-131 a RF-134, RF-184, RF-195" (l.1209): no los verifiqué uno a uno. Estado X.
- sd-01 "sección 1.6 'Frente de jefaturas asignado' y Tabla 1" (l.1203, 1313, 1413), "sección 1.4 'Experiencia relevante en la industria del caso'" (l.1411): los títulos vigentes son 1.5 "Estructura para Proyecto", 1.6 "Alianzas", 1.4 "Experiencia y Certificaciones"; no hay "Tabla 1". "Anexo A.1 'Presencia digital y web corporativa'" existe. "secciones 1.1, 1.3, 1.5 y 1.2" (l.1409, 1415): existen con otros contenidos (1.2 es estructura organizacional, 1.5 estructura de proyecto; "10 años de historia" no consta en sd-01: grep = 0).
- sd-05 5.5, 5.6, 5.7, 5.8.x, 5.10, 5.11.x, "Tabla 5.X" (l.831, 833, 837, 839, 843, 849, 851, 853, 857, 879, 883, 1219, 1225, 1237, 1241): el sd-05 vigente solo llega a 5.4 (5.1.x a 5.4.x). Tampoco "sección 5.1.3 Entidades transversales" (l.1219: 5.1.3 es "Dominio Mercadería"). "Tabla 5.X" (l.1225) es un marcador sin resolver. Estado X para el contenido, C para la numeración.
- sd-13 "Anexos A.1 a A.5" (l.1461, 1465): no verificado.

### 2.5 Contraste con la matriz de supuestos, exclusiones y restricciones (sd-02 Anexo A.4)

- RES-05 y SUP-07 (24 h continuas) contradicen H-01/H-02. RES-20 (8 s, 5 min, 30 s) coincide con sd-04 pero el formulario no lo recoge en RT-05.29 ni RT-09.01.
- RT-20.03 (l.1335): "Sí" con "Condiciones de cierre de marcha blanca y estrategia de migración de cartera con conciliación diaria" y cita sd-03 3.2.3, 3.2.5 y SUP-25. Sustento correcto en sd-03 l.228 y l.302 (conciliación diaria hasta el mes 21 / fin de mes). Remisión "A.5.1" errónea (es A.4.1). El resto de RT-20 queda en "No" aunque sd-03 3.2.2 cubre olas, compuertas y reversión (RT-20.01, 20.02, 20.04 probablemente cubiertos por sd-06/07/03): ver H-39.
- RT-16.10 (l.1225) retención: "documentos tributarios y de venta 6 años; antecedentes de crédito plazo del crédito + 6 años; precio 3 años" coincide con el Caso (l.797, RT-05.10 del Caso) y RES-02. Pero se asocia al RT-16.10 transversal (auditoría) y el valor por dominio del precio (3 años) queda por debajo del piso de 5 años del RT-16.10 si se lee como retención de auditoría; es válido solo porque el Caso lo fija. Aclarar. Remisión sd-05 5.8.2 no existe (sd-05 5.2.5).
- RT-12.05 (l.1129): Según Caso (segregación de funciones, Caso l.807) coincide con RNF-37 (sd-02). Sustento correcto. RT-12.10 (l.1139) y 24 h vs 4 h: el RNF-59 declara 4 h (más exigente), correcto.
- SUP-28 (enlaces) y SP-04 (reparto físico): RT-06.06 y RT-06.33 (l.901, 955) coinciden con SP-04 y sd-04 l.744. Sí correcto.

H-39 (M, X) RT-19.x y RT-20.x (l.1311-1345): 16 de 18 "No". Son Obligatorios y varios se cubren en otros subdocumentos (sd-01 1.5 describe comités y gobierno; sd-06/07/09 el resto). Completar cuando se concilien esos sd. Idem RT-21.02 a 21.22 y RT-22.01 a 22.09 (sd-10, sd-11).

### 2.6 Marcas y productos no decididos

Marcas o productos nombrados que la verdad vigente o sd-04 declaran no decididos: Dell PowerEdge / HPE ProLiant (l.987), APC/Schneider Galaxy (l.903), Kong (l.1083), Keycloak (l.1121, 1135), Wazuh (l.1091, 1093), OpenTofu/Ansible (l.759), Argo CD (l.813), Semgrep, ZAP, Trivy, OWASP Dependency-Check, Syft, Cosign (l.811, 1105, 1107, 1109), Elastic Cloud (l.1259), Prometheus/Loki/Grafana (l.1171), Acepta/E-Sign/TOC Biometrics (l.1239; prestador de firma no decidido), AnaLASER/FM-200 (l.921, 923: aparecen solo porque el RT los cita como referencia "o equivalente"; la fila de componente dice solo "Detección temprana por aspiración de aire" y "agente limpio", lo que está bien). Fortinet/FortiGate no aparece en el tramo (sí en sd-04, que lo nombra como "fabricante Fortinet" y FortiGate-VM; la verdad_proyecto dice que no está decidido, por lo que sd-04 y no este formulario es lo que hay que conciliar).

### 2.7 Otras observaciones menores

H-40 (B, C) l.1119: fila vacía (`&  &  &  &  \\`) tras RT-11.28; sobra.
H-41 (B, C) Columna "Sección de la propuesta" usa formas distintas ("Subdoc.3 §3.3.2", "Subdocumento 4, sección 4.1"); además los textos entre comillas ("Capas e interfaces", etc.) son subsubsecciones sin número en sd-04, no ubicables por número. Transversales 1.5 pide página.
H-42 (B, C) Se usan "Sí/No" con "-" en 143 filas obligatorias. Aun si se prefiere dejarlas en "No", conviene escribir la razón o el subdocumento donde se completará ("Pendiente de sd-0X") para no parecer omisión.
H-43 (M, C) RT-02.12 (l.753 tramo previo) y RT-26.01 (l.1461): RT-26.01 dice que la ficha T-19 declara "capa, zona y módulo"; "zona" y "módulo" son términos antiguos (usar capa, ámbito y servicio). El sd-13 mismo debe revisarse.
H-44 (M, C) RT-23.01 (l.1409) "historia de 10 años" no consta en sd-01 (grep = 0) y la fila se acredita con un sitio web (Vercel), no con el contenido pedido ("giro, historia, misión, visión, valores"); RT-23.02 y RT-23.03 apoyan en "portafolio disponible en la plataforma oficial". Sin evidencia verificable en el propio sd-01: Parcial.

## 3. Resumen de acciones sugeridas (orden de prioridad)

1. Rehacer todas las columnas "Componente" y "Sección" con la arquitectura vigente (Azure, ámbitos Retail y Emisor, X-01, servicios R:/F:, AKS, Event Hubs, API Management, Entra ID, Terraform) y eliminar códigos M-xx, Z1/Z2/Z3, Site Principal/Secundario.
2. Corregir H-01/H-02 (24 h), H-04 (308 elementos), H-20/H-21 (ocho puntos de falla, seis pasos).
3. Quitar marcas y productos no decididos (sección 2.6) o dejarlos como "por definir".
4. Cambiar Sí por Parcial donde sd-04 no desarrolla el compromiso (H-14, H-16, H-24, H-26) y agregar "Parcial" y "Evidencia" al formulario.
5. Resolver los "No" que están cubiertos (H-32, H-34, H-35, H-36) y completar los pendientes con "Pendiente de sd-0X".
6. Rehacer las remisiones de tablas y secciones (sección 2.4).

Fin del informe.
