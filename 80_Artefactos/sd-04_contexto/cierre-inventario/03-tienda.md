# Cierre C · tienda tipo con dos pares de hosts

**Fecha:** 23-10-2026. **Estado:** decisión técnica para integrar, actualizada con la decisión posterior del usuario de dos hosts por negocio y X-01 local. **Ámbito:** una tienda `SIT-xx`; multiplicación referencial por 22 tiendas sujetas al padrón. Este archivo es contexto de diseño, no declara recursos instalados ni revisión humana.

## Decisiones y límites

Cada tienda tiene **cuatro hosts físicos: dos Retail (`SIT-xx-R-01/02`) y dos Filial (`SIT-xx-F-01/02`)**. Cada pareja opera en su red, almacenamiento, cuentas de servicio y administración. R-02 es espera de R-01; F-02 es espera de F-01. El par F aloja además un **X-01 local aislado** con identidad, claves, almacenamiento y bitácora propios, para el contrato mínimo `compra_autorizable` cuando no hay WAN. X-01 no comparte la tabla de cupos F ni entrega datos de cartera a R. La operación financiera nueva tiene autoridad en la nube; F local solo consume autorizaciones **preemitidas y acotadas**. X-01 local es un proceso/VM aislado dentro del par F, no un quinto host.

El [Caso 09, capítulo 15](../../../00_Bases/Caso_09_Cadena_Multitienda.md) fija una prueba de ocho horas de tienda sin enlace y sincronización posterior en 30 minutos; [Bases Transversales, RT-03.10–18](../../../00_Bases/Bases_Transversales.md) exigen autonomía mínima general de **24 horas**, diario íntegro, conciliación determinista, funciones excluidas, redundancia local y enlaces redundantes. Se diseña para 24 horas; se ensaya también el escenario de ocho horas y la meta de conciliación de 30 minutos. La cifra de ocho horas no rebaja la de 24.

## Sitio y recursos

Cantidades por tienda. `D` = decidido por usuario; `T` = decisión técnica para el diseño; `V` = sujeto a prueba/capacidad; `M` = dato del mandante. Las capacidades siguientes son **reserva inicial de diseño**, no una medición de la tienda.

| ID | Zona / ámbito / ambiente | Clase y función | Cantidad y capacidad inicial | HA y recuperación | Entradas → salidas / datos | Fuente y estado |
| --- | --- | --- | --- | --- | --- | --- |
| SIT-xx-R-01/02 | Sala técnica, VLAN R-SRV / Retail / PROD | **2 hosts físicos**, activo/espera; `r-api-local`, `r-diario`, `r-sync`, caché firmada y agentes R en cada uno. | Cada uno: reserva inicial 8 núcleos, 32 GiB RAM, 2 SSD empresariales de 960 GB en RAID 1; diario ≥100 GB útiles. | Réplica síncrona del diario confirmado hacia espera, con quorum/fencing independiente; VIP R cambia solo al dueño de epoch. Discos toleran falla de uno; copia externa cifrada R. | POS→VIP R→diario R→nube R. Sin PAN ni cupo F. | Usuario D; RT-03.10–16 T/V |
| SIT-xx-F-01/02 | Sala técnica, VLAN F-SRV / Filial / PROD | **2 hosts físicos**, activo/espera; `f-autorizador`, libro de consumos, `f-sync` y depósito firmado de reservas. No originación ni evaluación nueva. | Cada uno: reserva inicial 12 núcleos, 48 GiB RAM, 2 SSD empresariales de 960 GB RAID 1; diario F ≥100 GB más cuota X. | Réplica síncrona de consumo y reservas al espera; fencing F independiente, VIP F. Copia externa F. | Terminal F→VIP F→nube F; datos F mínimos. | Usuario D; caso cap. 4/15 T/V |
| SIT-xx-X-LOCAL-01/02 | Segmento X-SRV y microsegmento de ejecución **dentro de F-01/02** / X / PROD | Instancia aislada por host F (VM ligera o sandbox con aislamiento equivalente), una activa y otra espera; servicio `compra_autorizable`, identidad X, bitácora append-only propia. **0 hosts físicos adicionales.** | Reserva por instancia: 2 vCPU, 4 GiB RAM, 20 GB de bitácora; capacidad F anterior incluye esta reserva. | Replicación síncrona y fencing X ligados a la epoch del par F; copia cifrada X distinta de F. No queda activo X en F-02 si F-01 conserva escritura. | R→listener X local→API F local contractual; X→X cloud al reconectar. Ni R→F directa ni lectura de base F por X. | Usuario D; T/V |
| SIT-xx-R-POS | VLAN R-POS / Retail / PROD | Terminales de caja, impresoras y lectores. Cliente local con cola de último recurso solo si el proceso de caja admite recuperación transaccional. | Cantidad real por padrón; caso informa 380 líneas en 22 tiendas, sin distribución por tienda. | Energía propia según dispositivo; no sustituye el diario central local. | API R local; medio de pago externo por red autorizada. | Caso cap. 2 y 8 M |
| SIT-xx-F-TERM | VLAN F-TERM / Filial / PROD | Puesto financiero o componente F aislado de la caja. | Según mesones y cajas con tarjeta propia; padrón pendiente. | Sin caché de cartera amplia. | F local o endpoint F cloud; no conexión directa a R-SRV. | Caso cap. 2/4 M |
| SIT-xx-NET-R / SIT-xx-NET-F / SIT-xx-NET-X | Segmentos R, F y X / PROD | VLAN/ACL o redes físicas separadas, firewall interno con allowlist estricta y gestión independiente. X queda microsegmentado en infraestructura F. | Caminos WAN de operadores distintos; switches/firewalls HA a dimensionar. Testigo de quorum separado por ámbito sin acceso a datos: dispositivo de red gestionado o servicio de arbitraje independiente que **no es host de aplicación**. | R↔hub R; F↔hub F; R→X local solo contrato; X→F local solo contrato. | Usuario D; RT-03.17/23 T/V |
| SIT-xx-UPS | Sala técnica / común físico | Alimentación protegida para **cuatro hosts** y red, circuitos separados. | Autonomía de conmutación y apagado seguro a dimensionar con potencia medida; no se afirma 24 h eléctrica por UPS. | Monitoreo de batería. | Telemetría → operación. | RT-06 T/V |
| SIT-xx-BKP-R / SIT-xx-BKP-F / SIT-xx-BKP-X | Destinos de copia separados por ámbito | Copia protegida fuera del par y replicación cifrada a repositorios propios al reconectar; medio cifrado administrado, **sin añadir host de aplicación**. | Retención según política; RAID y réplica de HA no son backup. | R, F y X tienen restauración y claves separadas. | RT-03.11/14 T/V |

Las redes de invitados, cámaras y sensores quedan en segmentos distintos sin ruta hacia `R-SRV`, `F-SRV` ni `X-SRV`. El agente de red fijará VLAN/CIDR, NAT, QoS, puertos y redundancia de switching/firewall. **El contrato X local no es un peering R↔F**: el firewall permite solo origen POS/R-API autenticado→listener X y X→API F de autorización, con TLS mutuo, esquema y rate limit. No se presume que un terminal de pago pueda cobrar sin conexión: el modo del adquirente requiere contrato.

## Procesos y autoridad

```text
POS R ── VIP R ── R-01 activo ── diario R ── réplica síncrona ── R-02 espera
                        │                                    │
                        └──────── R-sync ────────────── Retail cloud

POS R ── listener X local (F-01 activo, microsegmento X)
                 │ contrato mínimo y bitácora X
                 ▼
           API F local (F-01 activo) ── libro F ── réplica ── F-02 espera
                    │                               │
                    └──────── F-sync ───────── Filial cloud

Con enlace: contrato equivalente R→X-01 cloud→F cloud.
Sin enlace: R→X local→F local; R recibe decisión y referencia, nunca cupo.
```

El precio, la promoción y su vigencia proceden de versiones firmadas recibidas antes de la caída. Una venta obtiene ID global `tienda:caja:secuencia` reservado persistentemente, versión de precio y marca temporal local. El diario se confirma con escritura durable antes de imprimir o confirmar el documento; un reintento del POS con el mismo ID devuelve el resultado anterior. La existencia local se rebaja una sola vez por ese ID. La nube marca como **provisional** la disponibilidad de esa tienda mientras está aislada; otros canales no prometen sus unidades sin reserva confirmada. Al volver el enlace, la nube ingiere por secuencia e idempotencia; conflicto entre venta local y promesa remota se registra y deriva a resolución operacional, sin descartar la venta ni sobrescribir silenciosamente el stock. La política comercial de compensación debe quedar aprobada.

El par F recibe de la autoridad cloud un conjunto pequeño de autorizaciones firmadas, por tarjeta/token, tienda, ventana temporal, importe máximo y saldo reservado. **La reserva reduce el cupo disponible en cloud antes de viajar a tienda**; así el mismo importe no se autoriza además en otra tienda o canal. Cada autorización tiene ID y remanente en libro F, replicado con confirmación durable en F-02 **antes** de responder a X local. X registra ID de cruce, hash/referencia, decisión, epoch y tiempo en bitácora propia replicada, sin tabla de cupos ni datos completos F. X devuelve a R solo autorización/denegación, monto autorizado e ID; R persiste venta por ID idempotente. El mismo segmento de cupo no se asigna simultáneamente a otras tiendas/canales. F no autoriza sobre el remanente ni renueva desconectado. Tras reconectar, F concilia por ID y libera sobrantes solo tras cierre confirmado. Originación, aumento de cupo, repactación y evaluación nueva quedan cloud. Si token vence, identidad no satisface la política o F/X pierde quorum, **no se concede crédito**.

Cada par usa un **testigo de quorum independiente y fencing** del activo: el nodo que pierde quorum pierde VIP y escritura; el sobreviviente asume solo con epoch nueva y diario R/F/X íntegro. El testigo no aloja aplicación ni dato financiero. Se requiere latencia de réplica compatible con caja, se prueba corte de red entre pares y se rechaza split-brain. La bitácora X usa claves y cuenta X propias, aun si su VM/sandbox se ejecuta en un host físico F. La caída de ambos hosts F elimina X local y crédito offline; nunca se monta F ni X en R.

La cantidad de autorizaciones, su vigencia, monto máximo por operación, captura de consentimiento e información precontractual y aceptación de riesgo pertenecen a política F; esta propuesta define el mecanismo, no esos límites de negocio. La separación debe verificarse con cuentas, ACL, claves y registro de cruce X-01 en pruebas.

## Estados de operación y falla

| Estado | Venta Retail y documento | Crédito F | Sincronización y actuación |
| --- | --- | --- | --- |
| Normal, ambos enlaces | Venta por servicio cloud con diario local de respaldo operacional y precio versionado; medio de pago según adquirente. | Autorización cloud vía X-01. | Diario local se vacía tras confirmación remota duradera, conservando retención de auditoría. |
| Cae enlace principal, secundario disponible | Igual que normal tras conmutación automática. | Igual que normal. | Medir tiempo de conmutación y transacciones en vuelo. |
| Caen ambos enlaces hasta 24 h | Venta, promociones vigentes, emisión documental y existencia local con diario R replicado; terceros solo si contrato permite modo offline. | R→X local→F local; consumo de reserva previa válida. Sin cupo/quorum, otro medio de pago o procedimiento manual sin promesa de crédito. | Colas y bitácoras R/F/X separadas; ningún acceso directo R→F. |
| Vuelve enlace | Continúa venta; se conserva secuencia original e idempotencia. | F concilia consumos y cierra reservas; anomalías se bloquean para nueva autorización. | Replay automático y bitácora; prueba contractual: tras 8 h de aislamiento, conciliación ≤30 min. |
| Falla un disco de R o F | Sigue el host afectado en modo degradado RAID 1; sustitución controlada. | Igual si falla un disco F. | Alerta urgente; verificar integridad antes de reconstrucción. |
| Falla R-01 o R-02 | El superviviente con quorum y diario confirmado toma VIP R; venta local continúa incluso sin WAN. | F/X no cambian de dueño. | Medir RTO del par; restaurar el host caído sin promover escritura doble. |
| Falla F-01 o F-02 | Retail continúa. X local y F local asumen **juntos** en el host F superviviente tras quorum/epoch; crédito offline reanuda solo si reservas, libro y bitácora X están íntegros. | No se usa host R para F/X. | Medir RTO y pérdida cero de autorizaciones confirmadas; bloquear mientras cambia epoch. |
| Caen ambos hosts de un ámbito o falla testigo/quorum | R sin par no confirma venta local; F sin par no autoriza cupo local. Con WAN puede usarse servicio cloud del ámbito sano bajo política. | Se bloquean autorizaciones sin quorum. | Continuidad manual controlada y restauración desde copia; esta falla doble excede HA de host simple. |

La venta manual cuando falla el **par R completo** no equivale a prometer continuidad electrónica ni a emitir documentos fiscales sin procedimiento validado. Tampoco se considera venta confirmada una operación que no haya llegado al diario durable o a un comprobante manual controlado. Esos límites deben figurar en el plan de continuidad.

## Cálculo inicial y prueba

Sea `p` el máximo observado de ventas/documentos por hora en la tienda más exigente, `b` bytes medidos por evento completo y `k` factor de eventos auxiliares por venta. Para 24 h, el diario requiere `24 × p × b × k` bytes, multiplicados por margen de crecimiento `g` y de operación `m`. Reserva inicial por host: 100 GB R, 100 GB F y 20 GB X dentro de cada F; el par replica **dos copias** por ámbito, que no se cuentan como capacidad útil doble. Alertas al 60 %, reducción de funciones no críticas al 80 % y nunca pérdida silenciosa de venta. Son valores provisionales; se reemplazan por `p`, `b`, `k`, `g` y margen medidos. La tasa de vaciado tras ocho horas es al menos `8p/0,5 = 16p` eventos/hora, más tráfico normal y reintentos; se miden diarios R, F y X por separado. El cuello probable es el enlace de réplica, la sincronización o el almacenamiento local.

Pruebas de aceptación por tienda tipo: desconectar ambos enlaces durante 24 h; emitir venta y documento, llamar R→X local→F local, consumir reserva, y cortar **cada uno de los cuatro hosts** antes y después del commit. Verificar failover del par, cero venta/autorización confirmada perdida o duplicada y ninguna respuesta X sin bitácora persistida. Cortar enlace de réplica para probar fencing, ausencia de dos VIP activos y bloqueo cuando no hay quorum. Intentar desde R leer cupo o bitácora F/X y desde X abrir otra API F: denegación auditable. Simular vencimiento, doble uso en otra tienda/canal y dos cortes de WAN; comprobar cupo no duplicado. Al reconectar tras 8 h, conciliar ≤30 min por IDs R/F/X, incluyendo conflicto de inventario. Retirar disco de cada RAID, restaurar de copias **separadas** y medir RTO/RPO. Probar terminal de pago y documento conforme contrato del tercero.

## Matriz de decisiones y asuntos de integración

| Tema / alternativas | Elección y razón | Estado / comprobación |
| --- | --- | --- |
| Cuatro hosts (pares por ámbito) frente a dos | **Cuatro físicos por tienda**, R-01/02 y F-01/02; decisión posterior del usuario que reemplaza el conteo de dos. | D; a 22 tiendas actuales: **88 hosts** de patrón, sujeto a padrón y crecimiento. X local añade **dos instancias aisladas**, cero hosts. |
| VM por función frente a procesos/containers en cada host | Contenedores de aplicación separados, persistencia y agentes del ámbito en el mismo host. Evita contar cada proceso como VM/host; el sistema operativo y runtime se fijan en implementación. | T/V; prueba de reinicio, parche y soporte. |
| RAID 1 frente a disco único | RAID 1 de SSD, porque tolera una falla de disco. Copia separada para borrado/corrupción/pérdida de host. | T/V; medir IOPS y recuperación de copia. |
| Crédito offline ilimitado frente a reserva previa | Reservas F preemitidas, firmadas, acotadas y de uso único; reducen disponibilidad cloud antes de distribuirse. Evita doble consumo. | T/V; política de riesgo F, consentimiento y validación contractual. |
| Sincronización por sobrescritura frente a diario e idempotencia | Diario durable, secuencia, replay y bitácora de conflictos. Conserva venta y permite conciliación determinista. | T; pruebas de caos y reconciliación. |
| Un host por ámbito frente a par redundante | Par activo/espera por negocio, réplica síncrona, quorum y fencing; X aislado dentro del par F. Tolera una falla de host por ámbito y un disco por host. | D/T/V; **RT-03.14 cubierto a nivel de diseño**, sujeto a prueba de falla, testigo, red y energía. No confundir réplica/RAID con backup. |
| VLAN lógica frente a equipos de red dedicados | Segregación lógica con políticas distintas como mínimo; firewalls/switches separados si el análisis de amenaza y falla común lo exige. | T/V; agente de red dimensiona puertos, rutas, ACL y hardware. |

**Datos por levantar del mandante:** padrón y plano de las 22 tiendas; distribución real de 380 cajas y mesones; peak por tienda, tamaño real de eventos, terminales/periféricos y aceptación offline del adquirente/facturación; enlaces/energía/sala técnica; política de riesgo financiero para reservas y plazo; RTO/RPO por negocio; reglas de emisión documental de contingencia; política de copias/retención. Dimensionar además testigos de quorum, espacio y potencia para cuatro hosts por tienda y política de aislamiento/clave X local. La solución del par cumple la redundancia del host crítico **en diseño**; la prueba con WAN caída, host caído y split-brain decide su aceptación.
