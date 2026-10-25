# Cierre E · centros de distribución, centro de datos y sistemas conservados

**Fecha:** 23-10-2026 · **Estado:** diseño para integrar, con ubicaciones y contratos del mandante por acreditar. **Uso de IA:** Alto. Se distinguen *sitio físico*, *sistema externo a la solución nueva* y *host*: el primero no prueba los otros dos. Los identificadores `SYS-*` no son servidores adicionales.

## Decisiones que gobiernan la ficha

La operación financiera nueva, sus bases y su recuperación residen en Azure Chile Central y Brazil South, respectivamente. El DC propio sirve durante la convivencia para sistemas conservados y, solo cuando se acredite la obligación concreta, para custodia de conjuntos locales. No se coloca allí una réplica operativa de la nueva cartera por inercia. Retail, Filial y X-01 conservan redes, identidades, claves y permisos distintos; el crédito de 2011 debe quedar segregado durante la migración aunque hoy comparta instalaciones ([Caso 09, capítulos 5–6](../../../00_Bases/Caso_09_Cadena_Multitienda.md)).

El centro de datos principal es un recinto propio de **140 m² en casa matriz**, con sala de respaldo en la misma comuna y brecha de infraestructura de informe interno 2024 que aún debe entregarse. El CD principal está en Región Metropolitana, mide **42.000 m²** y usa WMS desde 2016; el CD de Concepción mide **9.000 m²** y opera con planillas, sin WMS. Son hechos del Caso 09, capítulos 2, 5 y 6. `DC-02` designa aquí la sala de respaldo descrita; no se presume capacidad de DR ni de host financiero nuevo en ella.

## Inventario de sitios y recursos

`D` = decidido por usuario; `B` = derivado de Bases; `T` = decisión técnica; `V` = validación de producto/capacidad; `M` = dato del mandante. Cantidad **1 sistema** no equivale a 1 VM. Los CIDR cloud y flujos `FL-*` remiten a [B, red cloud](02-red-cloud.md); los hosts de tienda se detallan en [C](03-tienda.md).

| ID | Sitio / zona / ámbito / ambiente | Clase, función y cantidad | Capacidad y HA | Entradas → salidas; datos, copia/DR | Fuente / estado |
| --- | --- | --- | --- | --- | --- |
| DC-01 | Casa matriz, recinto propio / ámbitos R y F segregados / PROD de convivencia | Sitio físico, 1, 140 m². Aloja solo hosts conservados cuya ubicación se pruebe y pasarelas necesarias. | Inventario real de racks, potencia, climatización, incendio, red y capacidad pendiente. No se deriva número de servidores de los m². | Túneles R/F propios hacia hubs; copias de cada sistema según dueño. | Caso cap. 6 B/M |
| DC-02 | Sala de respaldo en misma comuna / R/F segregados | Sitio físico existente, 1; función y equipamiento exactos por levantar. | **No es DR regional**. Riesgo de evento común con DC-01; capacidad real pendiente. | Copia/restauración solo si servicio y datos identificados lo requieren. | Caso cap. 6 B/M |
| DC-NET-R / DC-NET-F | DC-01 y DC-02, redes separadas | Segmentos, firewall y DNS por ámbito, cantidad física según levantamiento. No hay ruta R→F. | Dos operadores/rutas físicas cuando el sitio sea crítico; conmutación automática y pruebas. | `FL-05`, `FL-10` hacia hubs propios; administración por identidad/PIM. | RT-03.04/17 T/V |
| DC-IR-R-01/02 | DC-01, red integración R | **Par propuesto** de runtimes autohospedados para fuentes R conservadas, si el conector de datos lo requiere. Son 2 VM o appliances, no dos sistemas ERP. | Activo/activo según producto; tamaño/ubicación tras medir throughput. No abren base F. | Fuentes R locales → integración R cloud; salida controlada, claves R. | T/V; puede omitirse si API del proveedor reemplaza la necesidad |
| DC-IR-F-01/02 | DC-01, red integración F | **Par transitorio propuesto**, 2 VM/appliances, solo para extracción del sistema de crédito 2011 mientras migra. | Se retira al cerrar reconciliación y aprobación del apagado. Sin dependencia de producción nueva. | Sistema 2011 → integración F cloud, auditado y cifrado. | T/V/M |
| CD-01 | Región Metropolitana, 42.000 m² / R | Centro principal existente con WMS conservado y equipos de captura. | Dos enlaces de distintos proveedores ya descritos; capacidad y redundancia LAN por levantar. | Lectores/terminales ↔ WMS 2016 ↔ adaptador Comercio R; DR del WMS por contrato. | Caso caps. 2, 5–6 B/M |
| CD01-LOCAL-01/02 | CD-01, segmento R-LOCAL / PROD | **Par propuesto de nodos locales**, 2 hosts o VM del sitio para diario durable de recepción, preparación y despacho durante pérdida WAN. No duplica el WMS ni inventa otro. | Configuración activo/espera con fencing y almacenamiento tolerante a falla de disco; SO, memoria y CPU a dimensionar. | Captura local → diario → WMS/adaptador al reconectar; copia cifrada; conflicto auditable. | RT-03.10–16 T/V |
| CD-02 | Concepción, 9.000 m² / R | Centro existente con terminales y planillas actuales, **sin WMS acreditado**. | Enlace único actual; segundo proveedor y ruta física requeridos por RT-03.17 para la solución. | Captura estructurada → servicio logístico R; retirar planilla como registro. | Caso caps. 2, 5–6 B/T |
| CD02-LOCAL-01/02 | CD-02, segmento R-LOCAL / PROD | Par propuesto, 2 nodos de captura y diario durable; mismo patrón de continuidad del principal. | Activo/espera, fencing, RAID y copia separada; tamaño tras pico y prueba. | Terminales → diario local → servicio R cloud; integración con WMS solo si se elige extenderlo. | RT-03.10–16 T/V |
| EXT-ERP-DTE | Ubicación **desconocida**; ámbito R / PROD conservada | Sistema empresarial/facturación, 1 producto, **hosts/VM desconocidos**. Es único emisor tributario actual. | SLA, API, dependencia offline, copia y DR por contrato. | Adaptador Comercio R ↔ ERP/DTE; documento y asiento según contrato. | Caso cap. 5 B/M |
| EXT-WMS-2016 | CD-01 en operación; **alojamiento de servidores desconocido** / R | WMS conservado, 1 producto; no se presume VM dentro de CD ni DC. | HA/backup/DR del proveedor y capacidad de extensión pendientes. | CD-01 y adaptador Comercio R; ubicaciones, preparación y despacho. | Caso cap. 5 B/M |
| EXT-RETAIL-2009 | Ubicación desconocida / R / convivencia | Sistema central de retail, 1 producto; maestro e inventario actuales. | Extraer y conciliar antes de cortar autoridad. | Adaptador Comercio R; auditoría de maestros, precios, existencia. | Caso cap. 5 B/T/M |
| EXT-CREDITO-2011 | Ubicación desconocida / F / convivencia | Plataforma de originación y cobranza a sustituir, 1 producto, **no host permanente del DC ni pila cloud nueva**. | Controles F, copias y recuperación durante migración; 620.000 clientes con saldo. | Adaptador Crédito F/IR-F → migración F cloud; conciliación de saldo y evidencia. | Caso caps. 5/13/15 B/T/M |
| EXT-COMERCIO-2019 / EXT-MARKETPLACE-2022 / EXT-FIDELIZACION-2017 | Ubicaciones desconocidas; ámbitos R y datos sujetos a contrato | Tres productos existentes; infraestructura de proveedor o cliente por acreditar, sin inventar hosts locales. | Contratos, endpoints, retención y DR por levantar. | Adaptador Canales R; fidelización sin acceso a datos de pago F por defecto. | Caso cap. 5 B/M |
| EXT-PAGOS / EXT-FIRMA / EXT-PROVEEDORES | Contrapartes externas, ubicación no atribuida al DC | Grupos de terceros por inventariar individualmente, **no un servidor común**. | Disponibilidad, ventanas, método alterno y responsabilidad por contrato. | Salida desde ámbito permitido, HTTPS/mTLS/SFTP según contrato; nunca ruta genérica a F. | Caso mapa anexo A y diagrama lógico M |

**No agregar** `EXT-*` al conteo de hosts, VM ni recursos propios. Los pares `DC-IR-*` y `CD*-LOCAL-*` son propuestas nuevas y requieren especificación de hardware/VM, no se deducen de la existencia de un sitio. El hardware local se costea con la capacidad que entregue el levantamiento y la prueba.

## Convivencia y migración

| Sistema | Decisión de destino | Corte y condición de apagado |
| --- | --- | --- |
| Crédito 2011 | **Sustituir** por pila F cloud; acceso transitorio segregado. | Migrar cartera completa, 620.000 clientes con saldo, conciliación de cuotas, saldos, repactaciones, garantías, cobranzas y juicios. Cierre según hitos de remediación y fin de soporte 2029. Retener evidencias según obligación acreditada; apagar escritura cuando la autoridad F nueva esté aprobada. |
| ERP/facturación | **Mantener** como sistema de registro empresarial y único emisor tributario actual. | No apagar. Contrato de interfaz, secuencia de emisión, numeración y modo offline deben acordarse y probarse. |
| WMS 2016 CD-01 | **Mantener** en principal. | No apagar. Integrar eventos con servicio logístico R y reconciliar inventario. |
| CD-02 con planillas | **Eliminar planilla como registro**; seleccionar captura estructurada desde el inicio. Preferencia de diseño: evaluar extensión del WMS conservado para operación completa, frente a servicio propio cloud con diario local. | Decisión de producto y costo tras PoC con proveedor WMS; no afirmar que el WMS ya esté en Concepción. |
| Central retail 2009 | Convivencia de solo lectura/operación transitoria; proponer sustitución gradual de autoridades de catálogo, precio e inventario por servicios R. | Cortar por dominio con conteo/conciliación y reversión probados; no apagar hasta que ERP, WMS y canales reciban la autoridad nueva sin divergencia. |
| Comercio electrónico 2019 | Mantener temporalmente y decidir conservar frente a reemplazar con análisis de interfaces, SLO y costo total. | Evitar doble motor de pedido; al final un solo estado autorizado. |
| Marketplace 2022 | Mantener. | Integración de pedidos, devoluciones y liquidaciones; no apagar. |
| Fidelización 2017 | Proponer integración con saneamiento de datos y reglas de finalidad; sustitución solo si el proveedor no admite separación. | Acreditar que atributos F no alimentan segmentación comercial R sin base/autorización. |
| Catorce interfaces actuales | Descubrir inventario completo, dueño y fichero/API; migrar por interfaz con doble lectura/conciliación y control de duplicados. | Apagar cada interfaz antigua solo tras prueba de paridad y aceptación, nunca todas por una flecha única. |

La coexistencia de crédito 2011 no significa que el nuevo negocio F opere en DC. Durante la migración, se restringe el acceso antiguo por perímetro F y se audita cada transferencia; la ubicación exacta del producto la certifica el mandante. El dato financiero cuya custodia física en DC fuese obligatoria se anotará en la ficha D con **dataset, norma/contrato, custodio y retención**; si no existe mandato comprobado, la copia en DC es una opción de diseño que necesita evaluación, no un requisito atribuido al caso.

## Interfaces y redes por comprobar

| ID | Origen → destino | Protocolo y condición mínima | Evidencia faltante |
| --- | --- | --- | --- |
| E-01 | CD-01 terminales → WMS 2016 | Red R de operación, autenticación y cola/diario; puerto del fabricante. | Hosting, HA, versión y API WMS. |
| E-02 | CD-02 terminales → diario local → R cloud | Red R, TLS y secuencia idempotente. | Selección WMS/servicio, ancho de banda y picos. |
| E-03 | WMS/central/ERP → adaptador Comercio R | Listener privado o salida cifrada por hub R; contrato por producto, sin conexión directa F. | Esquema, sentido, puerto, frecuencia, responsable. |
| E-04 | Crédito 2011 → IR-F/adaptador Crédito → F cloud | Conector F aislado, cifrado, extracción con control de saldos y custodia de claves F. | Ubicación, API, ventana y límite de extracción. |
| E-05 | E-commerce/marketplace/fidelización → adaptador Canales R | Contratos individuales; finalidad autorizada y deduplicación. | Hosting, endpoint, proveedor, SLA. |
| E-06 | DC/CD R o F → hub cloud respectivo | VPN cifrada, prefijos y DNS propios según `FL-05/10`; rutas de retorno ensayadas. | IPAM existente, operadores y diversidad física. |
| E-07 | Proveedores/pagos/firma → adaptador autorizado | Cada tercero con contrato, sentido y allowlist; el DC no funciona como concentrador implícito. | Inventario de las 14 interfaces y contratos externos. |

El caso reconoce que nadie tiene el mapa completo de las 14 interfaces; su levantamiento es una **entrega del proyecto**, no información que pueda inventarse en este inventario. Antes de llamar a una conexión «decidida», se exige extremo real, responsable, dato, sentido, protocolo, frecuencia, SLA, seguridad, prueba y plan de retirada del enlace anterior.

## Dimensionamiento inicial y verificaciones

El CD-01 necesita al menos cuatro horas de operación sin exterior según Caso 09 cap. 15; RT-03.10 exige 24 horas como mínimo transversal, por lo que los diarios de ambos CD se prueban a **24 horas**, con el ensayo particular de cuatro horas. Para cada CD, `p` es el máximo de eventos logísticos por hora, `b` el tamaño medido de evento y `k` los eventos auxiliares por operación. Capacidad mínima del diario: `24 × p × b × k × (1 + crecimiento) × margen de seguridad`. Se parte de **100 GB útiles por CD** en el par local como reserva preliminar, revisable tras medición. Los nodos requieren dos dominios de fallo, copia independiente, fencing y replay; la selección de discos y CPU se hace con IOPS y pico de recuperación medidos. Para vaciar ocho horas de cola en 30 minutos, tasa de sincronización adicional mínima `16p`, si la meta de 30 minutos se extiende al CD por diseño; el caso la fija explícitamente para tienda, así que esta tasa CD es **objetivo técnico propuesto**, no obligación textual del caso.

En DC, no se dimensionan hosts de ERP/WMS/crédito como si fueran nuestros. El volumen de extracción se calcula con filas históricas, tamaño real, cambios diarios y ventanas autorizadas. Para crédito, reconciliación exige 100 % de registros esperados y saldos financieros dentro del umbral aprobado por control F; el umbral numérico se fija con la filial, no se improvisa. Para red, comparar `datos a transferir / ventana` más 30 % de margen inicial y medir retransmisiones, latencia y QoS, separando R y F.

**Pruebas:** desconectar ambos enlaces de cada CD, registrar operaciones locales, repetir ID, reiniciar nodo y simular falla de disco; restaurar de copia y conciliar contra WMS/servicio cloud sin perder evento. En DC, comprobar segmentación R/F, cierre de interfaz antigua por etapas, extracción F auditada y restauración de sistemas conservados según contrato. La brecha de sala 2024 y controles de energía/incendio se auditan antes de usar DC-01 para una función crítica nueva.

## Decisiones y faltantes del mandante

| Tema | Elección para integrar | Verificación pendiente |
| --- | --- | --- |
| DC nuevo núcleo financiero frente a F cloud | F cloud decidido; DC solo convivencia y eventual custodia acreditada. | Ubicación real de crédito 2011 y dataset local obligatorio, si existe. |
| CD-02 con planilla frente a captura estructurada | Captura estructurada con diario local; evaluar extensión WMS principal y costear ambas opciones. | Licencia, API, capacidad del WMS y operación Concepción. |
| Pares locales CD frente a un nodo | Par propuesto por continuidad; no confundir con WMS conservado. | Tipo host/VM, falla compartida, potencia, almacenamiento y RTO/RPO. |
| Sitio DC-02 frente a DR Brasil | DC-02 es sala existente de respaldo local; Brasil recupera pila cloud R/F. | Uso y capacidad reales de DC-02; riesgos por misma comuna. |

**Solicitar al mandante:** CMDB y diagramas de DC-01/DC-02, inventario real de hosts/VM, IPAM, informe de brecha 2024, contratos y API de los nueve productos, lista de las catorce interfaces con flujos observados, contratos de proveedores y pagos, software/licencia WMS, volumetría por CD, ubicación de crédito 2011, registros de custodia local obligatoria, topología WAN y padrón de equipos de captura. Su ausencia impide declarar host, interfaz y custodia como hechos actuales; no impide la separación R/F, el destino cloud F ni el patrón local propuesto.
