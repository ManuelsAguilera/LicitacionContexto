# Integración y decisiones pendientes

## Contenido incorporado

Las tarjetas de los doce servicios de Retail/Filial muestran su responsabilidad, etapa y despliegue candidato; X-01 sigue entre los ámbitos con fichas, políticas y bitácora. F:C-03 se llama Evidencia financiera. Oferta mantiene su despliegue por decidir; Comisiones y Marketplace se identifican como módulos extraíbles: servicio de negocio no equivale automáticamente a microservicio.

A/C/E/P en las trece tarjetas significa auditoría, control de acceso, exportación y parámetros como responsabilidad propuesta, no cuatro verificaciones aprobadas. Los cuatro patrones conservan autoridad en cada servicio: registros propios y lecturas sensibles auditadas; token y controles de rol/atributo; exportación filtrada/autorizada; parámetros versionados con aprobación cuando corresponda. El acceso de APIM no sustituye el control dentro del servicio. Un registro append-only no acredita inalterabilidad frente al administrador.

Se reemplaza la caja indefinida Servicios comunes por capacidades de base tecnológica: administración/parámetros con consulta de auditoría; flujos y tareas humanas; documentos/plantillas/firma; notificaciones. La quinta capacidad, búsqueda global, está en Datos con API de consulta e índice por ámbito. Cada una exige instancias separadas; los símbolos agregados no comparten claves, preferencias, datos ni permisos. Los estados durables son propios de cada componente, fuera de la memoria del proceso; no se crea una base de procesos común a los dos negocios.

Las tareas humanas, segundo aprobador, delegación y bandeja se distinguen de la coordinación automática de larga duración en Integración. Se representa la capacidad, sin elegir Camunda, Temporal o Flowable. Documentos Retail pertenecen a Abastecimiento/Posventa; C-03 conserva la autoridad financiera y no custodia documentos Retail. La instancia común de Filial frente a una ampliación de C-03 continúa por decidir.

Notificaciones consume el bus de su ámbito y se integra con una contraparte de mensajería pendiente, con correo/app/SMS o mensajería instantánea, preferencias, plantillas, reintentos y registro. Firma y mensajería se agrupan solo como contrapartes externas en el panel, sin elegir una marca ni compartir credenciales entre ámbitos. Las APIs comunes se muestran como familias; sus rutas concretas y consumidores se detallan por contrato, no se declaran como tráfico existente.

El índice global respeta permisos y sirve texto completo/facetas/tolerancia. No se da por cubierto mediante el índice vectorial de Oferta: este último se conserva para el catálogo multimodal. Los proyectores propios mantienen índices derivados y modelos analíticos; ninguna proyección cambia la autoridad de negocio.

## Recorrido de entrada corregido

Los dos canales públicos —comercio y tarjeta— entran a Front Door, de allí al origen mediante Private Link, a Application Gateway del ámbito, APIM propio y servicios autorizados. Los cinco canales internos entran a Borde por el acceso privado corporativo, después a Application Gateway y APIM propios. El acceso privado agrupa SD-WAN/VPN de sitios y ExpressRoute propuesto para DC-01: no afirma que cada tienda posea ExpressRoute ni que un canal interno se publique en Internet. No es otro gateway API.

Se retiraron los atajos del mesón hacia el cupo local y de Presentación hacia la función de venta sin enlace. La continuidad es una responsabilidad interna de Ventas/Originación con identidad y persistencia propias. El cupo preautorizado depende de Originación F:C-01, no de una lectura directa del canal a Cartera. Su disponibilidad sigue condicionada a topes/caducidad/viabilidad. Las rutas locales de contingencia se desarrollan en la vista de continuidad; la vista L2 no representa una llamada al borde de nube cuando no hay enlace.

No se agregan enlaces entre servicios por simple proximidad. Las flechas del contorno agrupan contratos por área, limitados al propietario. El único cruce entre negocios sigue mediado por X-01; el símbolo único APIM representa instancias distintas. La bitácora registra el mínimo autorizado y no un perfil de cliente unificado.

## Datos y exportación

Prevalece la decisión del usuario de retirar Data Lake sobre las menciones históricas de la especificación §4.1/4.4. La exportación masiva parte del PostgreSQL analítico dedicado del ámbito, genera archivos abiertos y manifiesto en Blob con filtros/corte/permisos, registra el acceso sensible y avisa mediante bus/notificaciones. Se representa como patrón de trabajo asíncrono, sin inventar producto de ejecución. La exportación íntegra de la información debe incluir documentos y expedientes no replicados en el mart mediante mecanismos del propietario; exportar solo agregados no cumple ese objetivo. Los listados conservan el filtro solicitado y el ámbito del usuario.

Power BI solo lee los dos repositorios analíticos. Los servicios conservan persistencia directa propia y outbox; los eventos alimentan proyecciones. Los registros de auditoría y su exportación al archivo inmutable son políticas transversales propias por ámbito; se eliminaron sus largas flechas repetidas para que la vista no se convierta en un mapa de todos los agentes. Seguridad y Observabilidad permanecen explícitas como franjas verticales que alcanzan las capas 1–6.

## Pendientes preservados

| Decisión de la especificación | Tratamiento gráfico | Condición de cierre |
|---|---|---|
| 7.1 Atributos por servicio | A/C/E/P como propuesta | RNF transversal y RF/matriz verificable aprobados; no marcar T-12 en Sí por dibujar |
| 7.2 Control regulatorio F:C-04 | Tarjeta candidata sin enlaces operacionales | Alcance, RF, autoridad, etapa y contraparte financiera; validación normativa y aprobación expresa |
| 7.3 Capacidades comunes | Base tecnológica por ámbito | Contratos, estado, operación y responsabilidades; sin nuevos códigos R/F |
| 7.4 Maestro de ubicaciones/unidades | Dueño pendiente en Administración | Asignar autoridad; consumidores de tienda/caja/rol y gobierno de cambios |
| 7.5 Documentos de Filial/C-03 | Autoridad financiera conservada | Decidir ampliación o instancia hermana; no duplicar expediente de negocio |
| 7.6 Auditoría inalterable | Patrón propuesto; no acreditación | Sellado y exportación inmutable, resistencia al administrador, prueba de alteración y recuperación |
| 7.7 Identidad offline | Sin habilitación nueva | Credenciales con vigencia, revocación, reloj, sesión nominativa y prueba de 24 h |

Siguen pendientes tenant propio de Filial, residencia/tránsito y DR, capacidades/regiones de productos, proveedor de firma y avisos, catorce interfaces actuales y contratos de búsqueda/exportación. RF-227 a RF-231 de Clientes son propuesta v3.1 en el adjunto, no requisitos aprobados del Excel v3.0. No se cambia el conteo oficial del catálogo ni se reparten RNF a servicios como decisión ya ratificada.

F:C-04 es la única nueva tarjeta intencionalmente sin conexiones: no tiene contratos ni datos aprobados. Las bandas técnicas/transversales expresan dependencias de ejecución, identidad o supervisión sin flechas individuales a cada caja; no son componentes sin función.
