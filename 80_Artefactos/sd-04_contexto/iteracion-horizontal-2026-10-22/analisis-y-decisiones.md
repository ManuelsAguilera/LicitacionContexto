# Análisis y decisiones de la iteración horizontal

Estado: diseño propuesto, no aprobación operativa. Se aplican las decisiones del usuario y el registro D-01–D-56; no se reabren las decisiones ya cerradas de Service Bus, Application Gateway o servicios comunes. No se edita el contenido de SD-03/SD-04.

## 1. Analítica e innovaciones

Se retira Data Lake porque no se identificó una carga que exija esa pieza. La necesidad de BI sí existe: indicadores por categoría, seguimiento comercial y posición financiera. Se cubre con un PostgreSQL Flexible Server analítico dedicado por ámbito, independiente del almacenamiento transaccional y con modelos semánticos y permisos propios. No se presenta una réplica de lectura de la base operacional como sustituto de un modelo analítico: habría acoplamiento de esquema y atraso variable.

Recorrido: servicio propietario → transacción con outbox → publicador → Service Bus del ámbito → procesador de proyecciones → PostgreSQL analítico del ámbito → Power BI. El outbox pertenece a cada servicio, no al área como base compartida. La publicación ocurre después de confirmar la operación; ni el bus ni el almacén analítico son autoridad de inventario, crédito o evidencia.

Cada evento requiere `event_id`, tipo/versión de contrato, ámbito, agregado, versión de agregado, fecha de origen, fecha de confirmación y referencia mínima a la operación. El procesador confirma en una transacción del repositorio analítico el cambio, la clave de deduplicación y el punto aplicado. Confirma el mensaje después del commit. Una caída entre commit y confirmación produce una reentrega sin doble efecto. Versiones viejas se ignoran con registro; saltos se retienen o concilian con el propietario. Orden por agregado, no orden global. Cambios del proyector no vuelven a publicarse como hechos del negocio.

Los hechos y dimensiones conservarán identificadores de origen, versión y tiempos de confirmación/aplicación. El drill-through usa esas referencias y una API autorizada del propietario; no abre consultas SQL desde BI a bases operacionales. La posición financiera pertenece a la Filial: Retail no recibe cartera, mora, saldos ni cupos personales. Cualquier agregado corporativo adicional necesita un contrato aprobado de X-01; no se presupone una unión libre de ambos modelos.

La carga inicial usa una exportación autorizada por el propietario, un manifiesto de conteos e integridad y un punto de corte consistente. Se capturan deltas desde un punto compatible con el snapshot, se carga una versión paralela, se aplican deltas por versión y se concilian totales antes de cambiar lectores. La captura debe durar más que la carga y validación o se repite el corte. Reconstruir no depende de conservar indefinidamente mensajes de Service Bus. Exportaciones, deltas retenidos y manifiestos tienen acceso, caducidad y propietario propios; no equivalen a un respaldo.

| Necesidad | Modelo y alimentación | Autoridad y aceptación |
|---|---|---|
| Venta, devoluciones y comisiones | Hechos de Ventas/Posventa/Comisiones con dimensiones comerciales; outbox propio | Conciliar importes, anulaciones y fecha de negocio; el modelo no emite DTE |
| Exactitud de inventario por categoría | Movimientos y resultados de conteo auditado, agregados diarios | Existencias; muestra de control aleatoria independiente del modelo predictivo |
| Oferta/precios/disponibilidad | Modelos operacionales propios, caché e historial de precios | Los límites de 30 s/5 min no se delegan a una actualización de Power BI |
| Posición financiera antes de 07:00 | Hechos financieros y corte conciliado por Filial | Cartera/Finanzas validan completitud, atrasos y partidas sin conciliar; no mostrar corte completo si falta una fuente |
| Conteo predictivo | Extractos autorizados del modelo Retail → conjuntos versionados en Blob | Existencias; partición temporal entrenamiento/prueba, trazabilidad y evaluación en sombra; no ajusta stock automáticamente |
| Búsqueda multimodal | Oferta → PostgreSQL/pgvector e imágenes autorizadas | Oferta; índice derivado, disponibilidad confirmada con Existencias al mostrar/comprar |
| Retail Media | Oferta + adaptador a plataforma publicitaria externa por definir | Datos Retail autorizados; sin datos personales financieros; retorno orgánico al fallar |
| Lockers | Pedidos + adaptador/controlador externo por precisar | Custodia, entrega y revocación de credenciales requieren contratos y prueba de contraparte |
| Fila virtual | Clientes + canal de atención y eventos propios | Contrato de entrada/salida y proveedor de avisos pendientes; minimización de identidad |

Conteo predictivo mantiene producción prevista en mes 16; las otras cuatro innovaciones, mes 21 según el contexto de SD-13. La selección del modelo, su entrenamiento y sus resultados siguen pendientes de evidencia. El índice vectorial no es un decimocuarto servicio de negocio.

Power BI admite Import y DirectQuery con el [conector PostgreSQL oficial](https://learn.microsoft.com/en-us/power-query/connectors/postgresql). DirectQuery se propone para vistas que necesitan mayor frescura; Import, para históricos y consolidados. DirectQuery no garantiza por sí mismo actualización de pantalla en 30 segundos: la [actualización automática](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-automatic-page-refresh) depende de capacidad, configuración y límites. Se probará la latencia completa de evento, proyección, consulta y visualización.

La conexión privada de datos se resuelve por ámbito mediante una puerta de enlace de datos compatible con el entorno elegido, con credenciales de solo lectura. La alternativa administrada VNet y la estándar [on-premises data gateway](https://learn.microsoft.com/en-us/data-integration/gateway/service-gateway-onprem) se compararán en el diseño físico por región, HA y salida permitida. Esta conexión de BI no es Application Gateway ni APIM. No se declara desplegada ni se elige región por inferencia. [La matriz de Fabric](https://learn.microsoft.com/en-us/fabric/admin/region-availability) identifica Chile Central como Power BI únicamente; Fabric completo no es la alternativa base de esta iteración.

## 2. Procesos e interfaces

La coordinación durable corresponde a Integración. Los estados y reglas de cada operación siguen en el servicio dueño; no se crea un almacén común de transacciones ni se añade un motor de flujos para completar el dibujo. Antes de seleccionar un motor se medirán duración, timers, reintentos, tareas humanas, recuperación de estado, versionado y trazabilidad requerida. Java/trabajadores y PostgreSQL propios pueden ejecutar coordinaciones acotadas; un motor especializado requerirá justificar qué problema concreto resuelve mejor.

| Proceso | Camino y estado durable | Compensaciones y casos ambiguos |
|---|---|---|
| Pedido | Pedidos registra intención; reserva en Existencias; autoriza pago; confirma venta; adapta DTE/ERP y despacho WMS/transportista/locker | Expirar y liberar reserva; anular autorización o devolver pago por contrato; nota de crédito por ERP cuando proceda. Un timeout requiere consultar por idempotency key antes de repetir. Consumir un evento no demuestra entrega física |
| Devolución | Posventa registra recepción e inspección; Ventas/DTE corrigen documento; proveedor devuelve pago; Existencias reincorpora solo lo aceptado | Mantener cuarentena si inspección rechaza; reintentar devolución financiera sin duplicarla; conservar pendientes si pago y documento se completan por separado |
| Formalización de crédito | Originación registra solicitud y evaluación; Evidencia valida firma y consentimiento; Cartera activa solo tras confirmar evidencia y condiciones | Firma incompleta no activa cartera; respuesta perdida se consulta por referencia; rechazos y vencimientos se registran sin borrar evidencia ni repetir desembolso |
| Compra con tarjeta propia | Ventas → X-01 → APIM de Filial → contrato financiero autorizado, con identidad exclusiva y correlación propia | Respuesta mínima autorizada/denegada y referencia; sin abrir cartera a Retail. Timeout no equivale a aprobación. El receptor publica sus hechos en su propio bus |

Pedidos/Existencias, precios/disponibilidad y autorización financiera requieren contratos síncronos acotados. Entrega, firma, DTE, reembolso y conciliación pueden completar asincrónicamente con estados visibles; sus límites y compensaciones deben aprobarlos los responsables del negocio. El inventario de catorce interfaces actuales permanece por verificar; cuatro familias objetivo no demuestran que se hayan identificado esos catorce enlaces.

API Center queda al costado del tráfico. Mantiene el contrato canónico OpenAPI 3.1; el pipeline valida y deriva una versión compatible para APIM, inicialmente 3.0.3 según D-16. Las [restricciones de importación de APIM](https://learn.microsoft.com/en-us/azure/api-management/api-management-api-import-restrictions) impiden asumir equivalencia completa de funcionalidades 3.1. Se probarán contratos y políticas después de importar. No existe una llamada de negocio obligatoria a API Center.

## 3. Datos y continuidad

| Uso | Pieza | Política que falta cerrar |
|---|---|---|
| Evidencia vigente y consentimiento | Blob Filial + metadatos propietarios de C-03 | Integridad, firma, búsqueda autorizada y plazo por instrumento; no plazo universal de seis años |
| Archivo documental | Blob por ámbito; copia autorizada ERP/DTE y exportaciones de auditoría | Clasificación, inmutabilidad cuando proceda, retención y eliminación por clase |
| Datos para entrenamiento | Contenedores Retail versionados y manifiestos | Autorización, linaje, exclusión de datos financieros y expiración de imágenes |
| Respaldo/recuperación | Backup Vault en vista física/operativa, políticas específicas de cada recurso | Cobertura real, RPO/RTO, copia aislada y prueba de restauración; no todo recurso queda protegido por añadir Vault |
| Proyección analítica | PostgreSQL dedicado y exportaciones consistentes | Regenerable, con control de corte; ni bus ni réplica sustituyen respaldo |

Los seis años aplican a ventas históricas del caso, no a todos los datos. Pedidos online tienen horizonte de migración de tres años; la cartera y evidencia financiera necesitan sus plazos propios. Separar ventana de migración, retención legal, archivo consultable y respaldo. Para las duraciones, contrastar Caso 09 §15 y RT-05.07/05.15, RT-11.14 y RT-16.10; no generalizar una cifra del registro a todas las clases.

La continuidad Retail se expresa lógicamente como Operación sin enlace, Diario durable y Sincronización. El diario se confirma localmente antes de responder, conserva ID único/origen/secuencia y se reenvía por las APIs Retail. Ventas confirma el hecho en nube antes de publicar su outbox. Confirmar el bus no equivale a confirmar todo el proceso. Se concilian cobro, venta, documento, stock y aceptación final; los reintentos no duplican operaciones.

El cupo preautorizado es responsabilidad de Filial, con red, clave, almacenamiento y permisos propios en el diseño físico. No permite abrir crédito ni aumentar cupo sin enlace. Hay un problema pendiente de consistencia: vender en dos terminales desconectados contra un límite compartido puede excederlo. Propuesta para resolverlo: tokens/porciones de autorización exclusivos por terminal, monto máximo, consumo durable y caducidad corta que no supere el horizonte validado de 24 h. Sin esa política aprobada y probada, la autorización financiera offline permanece deshabilitada; la venta con medios admitidos puede continuar según reglas Retail. Vigencia exacta, reloj, revocación, pérdidas y conciliación requieren decisión de Riesgo/Finanzas; no se inventa un valor en la figura.

## 4. Plataforma y observabilidad

Se conserva una sola representación visual de cada producto de entrada, con recursos propios por ámbito. Flujo público: Front Door Premium → Private Link del origen → Application Gateway v2 → APIM → servicio. Las entradas privadas de tiendas y mesón llegan a su Application Gateway por conectividad corporativa y omiten Front Door. El mesón financiero no atraviesa el nodo Retail. [Private Link de Front Door a Application Gateway](https://learn.microsoft.com/en-us/azure/frontdoor/how-to-enable-private-link-application-gateway) no reemplaza la conectividad privada de APIM con sus backends. APIM alcanza subredes del ámbito mediante integración de red, DNS y rutas permitidas que deben verificarse físicamente.

TLS se negocia en saltos distintos: cliente–Front Door, Front Door–origen y conexiones internas hacia APIM y servicio. El descifrado en un proxy exige volver a cifrar el siguiente salto. [La política TLS de Front Door](https://learn.microsoft.com/en-us/azure/frontdoor/tls-policy) no acredita la misma versión en todos los saltos. TLS 1.3 sigue como objetivo sujeto a prueba de extremo a extremo por producto/cliente. WAF y límites se implementan en las piezas de entrada existentes, sin añadir otro producto de borde por nombre de protección.

| Herramienta | Uso justificado | Pendiente de evidencia |
|---|---|---|
| AKS, Java/Spring | Alojar APIs, adaptadores y proyectores propios por ámbito | SKU Premium/LTS, versión compatible, región y conmutación; no acreditar ejecución con el icono |
| Managed Redis | Lecturas operacionales de oferta/disponibilidad Retail | Invalidez, consistencia y frescura ≤30 s; región y capacidad |
| Entra P2 / External ID | Identidades internas y clientes por ámbito | Confirmación expresa de tenant Filial; permisos mínimos y flujos de clientes |
| Key Vault / Managed HSM | Claves, secretos y cifrado de campo | HSM/región, blind indexes, rotación y restauración de claves; tokens de pago dependen de proveedor |
| Sentinel / Defender | Seguridad y respuesta | Fuentes, residencia, costo/capacidad e información mínima de incidentes agregados |
| PIM / Bastion / Private Access | Elevación y administración | Ruta física, grabación, copia inmutable y permisos; no paso de tráfico comercial |
| OpenTelemetry → Monitor | Registros, trazas y alertas por ámbito | Exportador OTLP, límites, cola local de 24 h, pérdida/backpressure y datos personales |
| Prometheus / Grafana | Métricas, SLO e indicadores de entrega | Fuentes, métricas del pipeline/DORA y consultas por ámbito; no duplicar almacén de logs |
| Sintéticos / experiencia real | Medir recorrido del usuario y disponibilidad | TLS soportado, SDK móvil y proveedor; consentimiento y muestreo |

No se crea una plataforma NOC con acceso libre a ambos ámbitos. Se permite proponer salud agregada sin datos del negocio; mecanismo e identidad pendientes. La correlación que cruza X-01 usa referencias propias, sin compartir logs entre tenants. Monitor exporta auditoría al archivo de su ámbito; el símbolo agregado no implica permiso entre ellos.

## 5. Decisiones abiertas y responsables propuestos

| ID | Decisión/trabajo | Responsable propuesto y condición de cierre |
|---|---|---|
| P-01 | Tenant propio de Filial | Mandante/Seguridad: confirmación expresa de D-40, no deducida de aprobación general |
| P-02 | Residencia de datos, metadatos y tránsito en borde; DR | Jurídico/Seguridad/Arquitectura: matriz por recurso y aprobación escrita; Brasil no se da por autorizado. Precisar alternativas del segundo sitio de cliente |
| P-03 | Capacidad/HA/región PostgreSQL, AKS, Redis, HSM y conectividad BI | Plataforma: cotas del dimensionamiento + prueba en SKU/región y evidencia de recuperación |
| P-04 | Servicios comunes | Arquitectura y dueños: responsabilidad, ámbito, consumidores y contratos; hasta entonces sin dependencias ficticias |
| P-05 | Lockers y publicidad | Pedidos/Oferta y contrapartes: identificar proveedor, endpoints, seguridad y manejo de fallos |
| P-06 | Catorce interfaces existentes | Integración + seis proveedores: completar inventario y evidencia de cada extremo |
| P-07 | Semántica de eventos y coordinaciones | Dueños de servicios: versiones, cortes, timers y compensaciones; elegir motor solo tras justificarlo |
| P-08 | Cupo offline | Riesgo/Finanzas: partición exclusiva, caducidad, no doble consumo y conciliación |
| P-09 | Indicadores/analítica | Finanzas/Comercial/Datos: diccionario, cortes, fuentes, exactitud y SLA por tablero |
| P-10 | Retenciones y documentos | Jurídico/Datos: clase, propietario, base aplicable, plazo, archivo y eliminación |
| P-11 | Instrumentación | Operación: OTLP, SDK móvil, sintéticos TLS, agregación de salud y permisos |

La aplicabilidad normativa financiera no se certifica aquí. La [NCG 569 publicada por CMF](https://www.cmfchile.cl/portal/normativa/624/w4-article-111273.html) y las instrucciones pertinentes deben evaluarse según el rol real del emisor y de las interfaces de finanzas abiertas; una consulta normativa no equivale a una regla ya aprobada. Ningún dibujo acredita residencia o cumplimiento.
