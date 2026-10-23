# Contexto de la arquitectura y cambios necesarios en el subdocumento lógico

Fecha de corte: 22-10-2026. Proponente: Only Simple Solutions. Estado: borrador de trabajo para el equipo, sin revisión humana formal.

Este documento reúne el criterio de diseño de la arquitectura vigente, explica qué decisiones sustituyen a las anteriores y establece los cambios necesarios para que su explicación escrita sea coherente. La referencia visual principal es la figura 4.36. Los detalles de Datos y de Seguridad/Observabilidad se conservan en las figuras 4.34 y 4.35.

El destino principal de las correcciones es **SD-04, sección 4.1 Arquitectura lógica y sección 4.1.1 Especificaciones Tecnologías de Software a utilizar**. SD-03 desarrolla el esquema de solución y el alcance que esa arquitectura debe respetar. En esta entrega se documentan diferencias y acciones; no se modifican SD-03, SD-04, los otros subdocumentos ni el catálogo oficial de requisitos.

## 1. Fuentes, precedencia y lectura de las decisiones

Las Bases Administrativas, las Bases Transversales y el Caso 09 siguen gobernando el contenido. El Comunicado 10 determina la estructura de la propuesta. Una selección de producto, una imagen de referencia o una recomendación de un adjunto no adquiere por sí sola carácter de requisito ni de aprobación del mandante.

La recopilación se apoya en los siguientes archivos locales. Las referencias a líneas del texto son localizadores de la copia revisada, no folios de las Bases.

**Nota de integración en main.** El contraste y los 25 cambios se prepararon sobre la copia de `work` del commit `768a1ca`, cuyos archivos tenían prefijo `OSS-`. Se conservan las copias exactas de [SD-03](fuentes-contraste-2026-10-22/sd-03-contraste.txt) y [SD-04](fuentes-contraste-2026-10-22/sd-04-contraste.txt), con [procedencia y hashes](fuentes-contraste-2026-10-22/procedencia.json). Los enlaces de la tabla siguiente apuntan a los editables de `main`, renombrados a `OnlySimpleSolutions-`. Sus textos y líneas pueden haber cambiado; la futura edición debe localizar cada hallazgo por título y contenido y comprobarlo de nuevo. La integración conserva íntegros esos editables y no presenta la revisión de `work` como una revisión completa de la versión posterior de `main`.

| Fuente de trabajo | Uso en esta recopilación |
| --- | --- |
| [SD-03 editable](../../02_Propuesta/latex_final/sd-03/OnlySimpleSolutions-Subdocumento3.tex) | Alcance, trece servicios, etapas, plataformas conservadas y restricciones de operación sin enlace. |
| [SD-04 editable](../../02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex) | Texto vigente contrastado y localización de cambios de 4.1, 4.1.1 y sus consecuencias físicas. |
| [Registro recibido D-01–D-56](decisiones-2026-10-22/registro-recibido.md) | Antecedente de selección por capas, confirmaciones y pendientes históricos. |
| [Especificación recibida de capa 4](integracion-capa4-2026-10-22/especificacion-recibida.md) | Autoridades de los servicios, atributos A/C/E/P y propuestas de capacidades comunes. |
| [Registro de Datos](capa-datos_decisiones-y-precisiones_2026-10-22.md) | Selección posterior de almacenamiento, procesamiento, búsqueda, gobierno y modelos. |
| [Registro de capas 7 y 8](capas-07-08_cambios-y-conexiones_2026-10-22.md) | Selección posterior de seguridad, telemetría y conexiones transversales. |
| [JSON de la figura 4.36](../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.json) | Componentes y asociaciones de la vista principal vigente. |
| [Asociaciones y contratos](composicion-compacta-2026-10-22/asociaciones-y-contratos.json) | Correspondencia entre relaciones detalladas y agrupaciones de la figura compacta. |
| [Pendientes y pruebas](actualizacion-datos-transversales-2026-10-22/pendientes-y-pruebas.md) | Trabajo de ingeniería y aceptación que la figura no resuelve. |

Tras la reorganización de `main`, la fuente editable de SD-04 es `02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex`. El maestro Markdown todavía menciona una ruta anterior `latex_final/sd-04.tex`; esa remisión también necesita corregirse cuando se actualice el estado del subdocumento. Editar su Markdown de contexto no cambia la oferta compilada.

### 1.1 Qué prevalece cuando los antecedentes discrepan

Las instrucciones posteriores y los registros específicos de Datos y capas 7–8 precisan el registro inicial. Deben leerse en secuencia.

| Tema | Antecedente superado | Estado que debe utilizarse |
| --- | --- | --- |
| Composición | Columnas verticales, actores y bandas inferiores separadas. | Capas 1–6 horizontales, sin fila de actores; una banda vertical izquierda resume 7 y 8. |
| Transporte | Event Hubs del SD-04 original. | Service Bus Premium por ámbito, aprobado en D-33. Event Hubs solo se reconsidera si una prueba de capacidad lo justifica. |
| Data Lake | Retirada en las figuras 4.30/4.31 por falta de uso demostrado. | ADLS Gen2 restituido por el registro posterior de Datos, con alimentación y usos definidos. |
| Gobierno de datos | Catálogo propio por desarrollar. | OpenMetadata seleccionado, con dependencias propias y linaje publicado desde los trabajos. |
| Telemetría de aplicaciones | Collector hacia Azure Monitor como recorrido base. | Collector hacia Loki, Tempo y Prometheus; Azure Monitor se mantiene para diagnóstico Azure y fuentes de seguridad. |
| Grafana | Azure Managed Grafana. | Grafana autogestionado, con Alerting. |
| Servicios comunes | Caja genérica sin consumidores. | Capacidades de base tecnológica diferenciadas; contratos y algunos productos siguen pendientes. |
| Productos de entrada | Cajas repetidas por negocio. | Un símbolo por producto; recursos, permisos y rutas siguen separados por ámbito según el diseño registrado. |

D-22–D-27 y D-29–D-34 aparecen duplicadas en el registro recibido. Se interpretan una sola vez. D-28 ya confirma las selecciones de servicios comunes y AKS Premium; las listas antiguas que vuelven a pedir esas confirmaciones no las reabren. D-40 conserva una confirmación pendiente del tenant de Filial. Una aprobación general de recomendaciones no sustituye esa confirmación específica ni la autorización escrita de residencia o tránsito.

## 2. Problema que la arquitectura debe resolver

La solución busca coordinar las plataformas y conservar una autoridad reconocible para existencias, precios, pedidos, ventas y crédito. La separación del negocio comercial y del financiero condiciona los contratos, la identidad, las redes y los datos. Un perfil de cliente comercial no puede transformarse en una copia de la cartera financiera.

El diseño conserva las cuatro promesas descritas en SD-03, 3.1. El disponible debe sostener la promesa de existencia; la versión de oferta debe permitir acreditar el precio aplicado; Pedidos mantiene la promesa y el seguimiento; Originación y Evidencia deben probar las condiciones del crédito y su aceptación. La analítica, la búsqueda y las innovaciones apoyan esos procesos sin asumir su autoridad de escritura.

Se mantiene el despliegue híbrido y el calendario de 56 meses. La producción de Etapa 1 corresponde al mes 16; la de Etapa 2, al mes 21. La operación se extiende hasta el mes 56. La vista objetivo no implica apagar todas las plataformas de convivencia simultáneamente ni adelantar sus olas de aceptación.

La solución se elige por correctitud, disponibilidad, seguridad y capacidad de operación. El costo debe estimarse para sostenerla; no justifica recortar la separación de datos, las pruebas ni el soporte de las herramientas autogestionadas.

## 3. Cómo debe interpretarse la figura vigente

La figura 4.36 es una vista lógica L2 de relaciones principales. Contiene 79 componentes representados y 53 conexiones, frente a las 88 relaciones de la vista anterior. La reducción se obtiene agrupando familias de contratos, no eliminando sus obligaciones. El archivo de asociaciones conserva el detalle.

Las capas 1 a 6 ocupan franjas horizontales que se leen de arriba hacia abajo. Seguridad y Observabilidad conservan sus números y responsabilidades dentro de **Capas transversales**, a la izquierda. Esa banda resumida no es una instancia común de seguridad o monitoreo. Las tecnologías se alinean lateralmente con la responsabilidad que soportan; las contrapartes externas se ubican a la derecha, próximas a Servicios e Integración.

Los círculos de Datos agrupan repositorios bajo Mercadería, Venta, Clientes y Crédito. La agrupación no decide cuántos servidores, bases o esquemas físicos existirán, ni permite que varios servicios escriban tablas ajenas. Por ejemplo, el símbolo PostgreSQL Crédito resume repositorios distintos de Originación, Cartera y metadatos de Evidencia.

Una representación de Front Door, Application Gateway, APIM o API Center identifica un producto. Según los rótulos y decisiones vigentes, representa recursos propios de Retail y Filial. La petición de evitar duplicación visual no se interpreta como permiso para compartir perfiles, claves, catálogos o rutas entre los negocios. Si se quisiera cambiar también el número real de recursos, haría falta una decisión de arquitectura diferente.

Las líneas con punta expresan solicitudes, publicaciones, consumo o persistencia según su leyenda. La línea gris sin punta expresa una asociación o dependencia y exige consultar el contrato detallado para conocer dirección y operación. Una relación desde el contorno de un área no significa que todos sus servicios llamen a todos los destinos. Los puertos auxiliares del CSV son puntos gráficos, sin responsabilidad de negocio.

La eliminación de actores de esta lámina mejora su lectura; los actores y permisos deben seguir en la matriz de cobertura o en otra vista. No se elimina la necesidad de atender a Contraloría, TI, analistas, vendedores ni titulares por dejar de dibujar personas.

## 4. Responsabilidad de las ocho capas

El texto debe describir qué controla cada capa y cómo se relaciona con las otras, sin convertirlas en una secuencia obligatoria de toda operación.

| Capa | Contenido de la arquitectura | Límite que debe quedar escrito |
| --- | --- | --- |
| 1. Presentación | Portales y apps de tienda y tarjeta; caja/POS; app interna; logística; atención comercial; mesón financiero. | Los canales invocan contratos autorizados y no escriben bases de negocio. |
| 2. Borde y exposición | DNS, Front Door Premium con WAF, Private Link y entrada privada corporativa. | DNS resuelve nombres; las entradas internas omiten el borde público. |
| 3. Puerta de enlace | Application Gateway v2 y APIM Premium clásico; API Center como gobierno lateral. | App Gateway y APIM tienen funciones distintas; API Center queda fuera del tráfico de peticiones. |
| 4. Servicios de negocio | Mercadería, Venta, Relación con el cliente, Crédito y X-01. | Cada servicio mantiene reglas, autorización y autoridad sobre sus datos. |
| 5. Integración y eventos | Service Bus propio por ámbito; adaptadores; sincronización; trabajadores y coordinación durable. | No sustituye la persistencia directa del propietario ni confirma por sí sola un proceso completo. |
| 6. Datos | PostgreSQL operacional y analítico; ADLS; Blob; Redis; índices; diarios locales y repositorios técnicos. | Separar autoridad, proyección, archivo, evidencia y respaldo. |
| 7. Seguridad | Identidad, dispositivos, cargas, secretos, claves, privilegios, acceso y detección. | Los controles se aplican en cada recurso y ámbito, aunque se resuman en una banda. |
| 8. Observabilidad | Instrumentación, colectores, almacenes por señal, consulta, sondas y alertas. | Telemetría saneada y separada; salud agregada sujeta a contrato mínimo autorizado. |

### 4.1 Entrada pública, entrada privada y TLS

El recorrido público de APIs es **canal → Front Door Premium → Private Link del origen → Application Gateway del ámbito → APIM del ámbito → servicio autorizado**. El contenido estático de los portales necesita un alojamiento y un recorrido propios; esta secuencia no demuestra dónde se sirve toda la presentación.

Los canales internos usan **canal → conectividad privada corporativa → Application Gateway → APIM → servicio**. Se conserva VPN/SD-WAN para los sitios y ExpressRoute propuesto para DC-01. No se atribuye un circuito ExpressRoute a cada tienda. La VPN permanece por decisión del usuario; Private Access se limita al acceso remoto administrativo definido, con permisos por recurso.

APIM alcanza un backend privado mediante la conectividad, resolución DNS y reglas de red de su ámbito. Que el servicio esté en otra subred no obliga a crear un segundo gateway API. Private Link del origen de Front Door y el acceso de APIM a sus backends resuelven conexiones distintas y deben detallarse en la vista física.

TLS se especifica por salto. El cliente establece una conexión con el borde; los proxies establecen conexiones posteriores hacia el origen, APIM y los servicios. La terminación en un proxy exige cifrar de nuevo el salto siguiente. TLS 1.3 exclusivo sigue como objetivo sujeto a compatibilidad y prueba en cada tramo; configurarlo en el borde no demuestra que todos los tramos lo soporten. WAF, restricciones de origen, validación, cuotas y límites deben asignarse a las piezas seleccionadas, sin crear otra caja por cada protección.

### 4.2 Gobierno de APIs y cruce X-01

API Center conserva contratos por ámbito. El diseño registrado genera OpenAPI 3.1 y deriva una versión 3.0.3 para APIM mediante el pipeline. Hay que verificar que la transformación conserve validaciones y semántica. API Center no recibe una petición de negocio después de APIM.

El recorrido de compra con tarjeta propia es **Ventas → X-01 → APIM de Filial → contrato de autorización de Originación**, con respuesta limitada a la operación. La puerta financiera solo acepta desde Retail la identidad y contrato autorizados de X-01. Las políticas también se aplican en el extremo receptor.

X-01 conserva ficha de finalidad, campos, versión de política, decisión y bitácora mínima. No mantiene una tabla general de equivalencia cliente–titular ni un perfil unificado. Cada cruce usa una referencia propia; los registros y trazas permanecen en su ámbito. Reversas, conciliaciones o finalidades adicionales no quedan autorizadas por la flecha de compra y requieren su propia ficha aprobada.

## 5. Servicios, capacidades comunes e innovaciones

Se mantienen nueve servicios Retail, tres de Filial y X-01. Las etapas y autoridades siguientes proceden de SD-03/SD-04 y de la integración de la especificación de capa 4.

| Área | Código y servicio | Autoridad y límite | Etapa |
| --- | --- | --- | --- |
| Mercadería | R:M-01 Oferta comercial | Artículos, precio, promoción y publicación; no decide reservas. | E1 |
| Mercadería | R:M-02 Abastecimiento | Órdenes, transferencias y recepción; WMS conserva ejecución física. | E2 |
| Mercadería | R:M-03 Existencias | Movimientos, reservas, disponible, conteos y ajustes aprobados. | E1 |
| Venta | R:V-01 Pedidos | Promesa, asignación y estado; coordina cumplimiento. | E2 |
| Venta | R:V-02 Ventas | Venta, pago, reversa y conciliación; ERP/DTE conserva emisión tributaria. | E1 |
| Venta | R:V-03 Comisiones | Reglas y base de atribución; no reemplaza remuneraciones. | E2 |
| Venta | R:V-04 Marketplace | Gobierno de vendedores e intercambio con la plataforma conservada. | E2 |
| Relación con el cliente | R:CL-01 Posventa | Caso, inspección y destino de devolución. | E2 |
| Relación con el cliente | R:CL-02 Clientes Retail | Identidad y preferencias comerciales; sin datos de cartera. | E2 |
| Crédito | F:C-01 Originación de crédito | Solicitud, evaluación, cupo y autorización. | E1 |
| Crédito | F:C-02 Cartera de crédito | Cuenta, saldo, pagos, mora, cobranza y repactación. | E1/E2 |
| Crédito | F:C-03 Evidencia financiera | Precontrato, aceptación, firma, expediente y metadatos propios. | E1 |
| Frontera | X-01 Control de cruces | Políticas y bitácora del intercambio mínimo autorizado. | E1 |

Los trece servicios no equivalen a trece ejecutables ni trece servidores. Oferta mantiene su partición por decidir; Comisiones y Marketplace pueden ser módulos extraíbles. El detalle de despliegue se justifica mediante cargas, autoridad, fallos y operación. Los rótulos de área tampoco autorizan una transacción distribuida entre sus repositorios.

**F:C-04 Control regulatorio continúa como candidato**, sin etapa, requisitos ni contratos aprobados y sin conexiones operacionales. No eleva el catálogo a catorce servicios. La necesidad de cumplir obligaciones regulatorias debe resolverse, pero el dibujo no aprueba crear ese servicio ni determina la aplicabilidad de una norma financiera.

### 5.1 Atributos y capacidades comunes

A/C/E/P significa auditoría, control de acceso, exportación y parámetros. Son patrones de diseño propuestos por servicio, con evidencia y brechas por cerrar. APIM no sustituye la autorización de negocio; una tabla append-only no demuestra inalterabilidad frente al administrador; un botón de exportar no demuestra exportación íntegra ni conservación de filtros.

La caja genérica Servicios comunes se desarrolla como base tecnológica con Administración/parámetros y consulta de auditoría, Flujos/tareas humanas, Documentos/plantillas/firma y Notificaciones. Búsqueda global queda en Datos; exportación masiva es un patrón de trabajo asíncrono. Cada ámbito conserva sus datos, credenciales y contratos. Se mantienen pendientes el dueño del maestro de ubicaciones, productos de tareas/firma/mensajería y el límite de la capacidad documental de Filial frente a F:C-03.

Las tareas humanas tienen bandeja, plazo, delegación y estado durable. La coordinación automática de pedidos, devoluciones o formalización financiera pertenece a Integración; las compensaciones pertenecen al servicio que puede ejecutarlas. No se selecciona Camunda, Temporal, Flowable ni otro motor para completar el dibujo.

### 5.2 Cinco innovaciones y aislamiento de la operación

Las innovaciones siguen dentro de sus servicios responsables. Añaden capacidades y cargas, no nuevos servicios funcionales por defecto.

| Innovación | Tipo y propietario | Integración que debe explicarse |
| --- | --- | --- |
| Conteo cíclico predictivo | Proceso; Existencias. | Historia autorizada, conjunto versionado, Python/scikit-learn, registro MLflow y recomendación revisada por una persona. |
| Lockers Ancoa 24/7 | Producto; Pedidos. | Estado del pedido, credencial de retiro, controlador externo y confirmación; contrato de contraparte pendiente. |
| Búsqueda vectorial multimodal | Tecnología; Oferta. | Catálogo e imágenes autorizadas, modelo de representaciones, pgvector y confirmación de precio/disponible con sus propietarios. |
| Retail Media Network | Modelo de negocio; Oferta. | Campañas contextuales y plataforma publicitaria; sin usar datos financieros ni bloquear la compra por una falla publicitaria. |
| Modo Tienda y fila virtual | Experiencia; Clientes Retail. | Estado local y sincronización de configuración e indicadores; atención asistida en contingencia. |

El conteo propone prioridades y no cambia stock automáticamente. La ayuda para explicar merma se mantiene basada en evidencia y confirmación humana, sin inventar otro predictor de hurto. Python/scikit-learn concreta el conteo; el modelo multimodal y sus versiones siguen por seleccionar. La autonomía de la tienda no se extiende automáticamente al controlador de lockers ni a todas las apps móviles.

## 6. Integración, datos y continuidad

La persistencia del servicio y la propagación de hechos son recorridos distintos. El propietario confirma su operación y outbox en una transacción local; publica después en Service Bus de su ámbito. El consumidor confirma el mensaje cuando su efecto durable está aplicado. Debe deduplicar, controlar versiones y huecos, reintentar y tratar errores persistentes. La confirmación del broker no confirma una reserva, un cobro ni toda una saga.

Service Bus no sustituye el histórico ni garantiza por sí solo reconstrucción o recuperación regional. Las propiedades de retención, relectura Kafka y geo-replicación que SD-04 atribuye a Event Hubs deben retirarse o rediseñarse, sin copiarlas al nuevo producto. La eventual reintroducción de Event Hubs exige una prueba y una nueva decisión registrada.

Se conservan cuatro familias de adaptadores, Comercio, Canales, Socios y Crédito. Las flechas agrupadas no sustituyen el inventario de catorce interfaces. Cada contrato necesita origen, destino, autoridad, dirección, protocolo, versión, sincronía, confirmación, plazo y conciliación. Pagos, reservas y verificación de evidencia pueden exigir respuesta síncrona aunque el área también consuma eventos.

### 6.1 Cadena analítica, gobierno y búsquedas

La alimentación prevista tiene dos entradas complementarias, siempre separadas por ámbito.

1. **Operación incremental:** servicio/outbox → Service Bus → trabajadores Java/Spring de ingesta y proyección → destinos autorizados, incluidos modelos PostgreSQL analíticos e índices derivados.
2. **Carga inicial y reconstrucción:** exportación autorizada con corte → Data Factory y trabajadores → recepción y conjuntos depurados en ADLS → modelos PostgreSQL analíticos → Power BI.

ADLS tiene usos concretos de recepción, historia autorizada, conjuntos depurados, reconstrucción y entrenamiento. No se vuelcan todos los datos a todos los destinos. Data Factory coordina cargas y dependencias; los trabajadores implementan validación, transformación, deduplicación, proyección y conciliación. Deben declararse por separado la ubicación del factory, sus metadatos y su integration runtime.

Power BI consulta **únicamente PostgreSQL analítico dedicado del ámbito**. La modalidad Import o DirectQuery se decide por informe y frescura requerida. La conectividad privada de BI se documenta como conexión de datos, diferenciada de las puertas de APIs. La selección de modalidad no acredita la frescura del indicador ni la posición financiera antes del corte diario.

OpenSearch autogestionado sirve búsqueda global por APIs con permisos, facetas y tolerancia. PostgreSQL/pgvector sirve el índice comercial multimodal de Oferta. Ambos son proyecciones reconstruibles, con revocación y permisos propagados; no son autoridades de precio, saldo o disponible.

OpenMetadata conserva catálogo, glosario, propietarios, clasificación, calidad y linaje. Necesita almacenamiento de metadatos e índice compatibles y dedicados. Su índice técnico no se confunde con el OpenSearch de búsqueda del negocio. Conectores y trabajadores publicarán el linaje que no se extraiga automáticamente; instalar el catálogo no acredita cobertura completa.

MLflow se limita a las innovaciones Retail definidas, con PostgreSQL para metadatos y Blob para artefactos. Los conjuntos se referencian por versión y procedencia. Evaluación temporal, comparación con una línea base, deriva, promoción humana, reversión y alternativa manual requieren trabajo explícito. No se agrega entrenamiento financiero por simetría visual.

Las selecciones actuales excluyen Purview, Databricks, Azure AI Search, Fabric y Synapse como productos de base. Sus capacidades necesarias se asignan a las piezas anteriores. La exclusión de una marca no elimina una obligación contractual. Las versiones, compatibilidad y disponibilidad regional siguen requiriendo acreditación.

### 6.2 Autoridad, evidencia, archivo y respaldo

Originación conserva evaluación/cupo/autorización; Cartera conserva cuentas/saldos; Evidencia conserva expediente y metadatos financieros propios, con archivos en Blob. Hace falta cerrar el contrato atómico entre cupo y cuenta, sus estados, reversas y conciliación. Agrupar Crédito en un círculo no resuelve esa consistencia.

El historial de precios conserva versión, canal, vigencia y confirmación en destino. Cambiar Oferta no demuestra que caja, web o etiqueta ya muestren ese precio. Redis conserva datos reconstruibles de oferta; su TTL no prueba un plazo de propagación.

ADLS de transformación, evidencia vigente, archivo WORM, exportaciones temporales y respaldos tienen permisos, políticas y ciclos de vida distintos. Las retenciones por clase están recopiladas en el registro de Datos, sección 7; al llevarlas a la oferta se verifican en el Caso visible y se citan con folio impreso. No se aplica un plazo universal de seis años ni se equipara horizonte de migración con conservación legal.

Azure Backup y PITR se especifican por recurso con restauración probada, claves, permisos y destino aprobado. La figura conserva una referencia resumida de recuperación; el detalle de bóvedas, copias y Arc/Monitor Agent corresponde a arquitectura física u operación. Ningún símbolo de respaldo acredita cobertura de bases, mensajes, índices y archivos a la vez.

La exportación íntegra incluye datos operacionales, documentos, expedientes y metadatos necesarios, además de agregados. Los trabajos masivos mantienen filtros, permisos, corte, formatos abiertos, manifiesto, auditoría y aviso. Exportar solamente un tablero analítico no satisface ese alcance.

### 6.3 Operación sin enlace y crédito local

La continuidad lógica se divide en Operación sin enlace, Diario durable L-02 y Sincronizador L-03; L-01 sigue identificando la caché de oferta. El POS confirma primero la escritura local. Al volver el enlace, el sincronizador llama las APIs Retail por la entrada privada; no escribe directamente en PostgreSQL ni considera conciliada una venta solo porque fue enviada.

Se conserva la autonomía de 24 horas y deben probarse identidad local, vigencia de oferta/promociones, secuencia, reinicios, espacio disponible, conflictos de reservas y retorno sin dobles cobros. Las pruebas del corte de ocho horas y sincronización máxima de treinta minutos registradas en los antecedentes se contrastan con el Caso; el ensayo de 24 horas no inventa otro plazo contractual de drenaje.

El cupo preautorizado pertenece a Filial, con almacenamiento, red y clave propios aunque resida en una instalación de tienda. No habilita originación ni ampliación de cupo sin enlace. La política requiere asignaciones exclusivas o mecanismo equivalente contra doble gasto, consumo durable, caducidad, reloj confiable y conciliación. Guardar una copia del cupo no resuelve dos terminales desconectados consumiendo el mismo límite.

SD-03 ya compromete compra offline con cupo previo; su factibilidad pendiente es un riesgo de cumplimiento de ese compromiso, no una autorización para eliminarlo de alcance. Debe cerrarse con Riesgo/Finanzas y una prueba antes de habilitarlo. Si no es viable, cualquier cambio al compromiso exige decisión expresa y conciliación posterior de SD-03.

## 7. Seguridad y observabilidad transversales

La banda izquierda resume productos; el detalle de instancias y conexiones se conserva en los registros y la figura 4.35.

Seguridad diferencia **Entra ID P2, External ID, Intune, Workload Identity/identidades administradas, Key Vault, Managed HSM, PIM, Bastion Premium, Private Access, Defender for Endpoint, Defender for Cloud y Sentinel**. Personal, clientes, dispositivos y cargas tienen identidades y permisos distintos. Los servicios mantienen autorización por rol, entidad, finalidad y recurso.

PIM concede elevación temporal, no transporta sesiones. Private Access ofrece el recorrido administrativo autorizado y no reemplaza la VPN de sitios. Bastion cubre sesiones de máquina compatibles; no demuestra grabación de toda consulta SQL, llamada API o administración de Kubernetes. Key Vault conserva secretos/certificados; HSM protege las claves seleccionadas para el cifrado adicional. El diseño debe probar que acceder a SQL no basta para leer campos financieros protegidos.

La grabación de Bastion escribe primero en un contenedor temporal mutable sin versionado; un trabajador copia y verifica su custodia en WORM. Hay que proteger y medir esa ventana. QR + PIN no se presenta como MFA general; los privilegios y accesos que exijan MFA necesitan un mecanismo válido. Los terminales compartidos requieren sesión nominativa, cierre y limpieza al relevo, con límites claros de revocación offline.

Observabilidad conserva **OpenTelemetry Collector, Prometheus, Loki, Tempo, Grafana/Alerting, Blackbox Exporter y Azure Monitor/Log Analytics**. Aplicaciones y trabajadores publican señales saneadas al Collector de su ámbito. Este dirige registros a Loki, trazas a Tempo y métricas a Prometheus. Grafana consulta esos almacenes y Azure Monitor mediante accesos propios. Azure Monitor recoge el diagnóstico de recursos Azure y las fuentes requeridas por seguridad; no se vuelcan todos los registros Loki en Log Analytics por defecto.

Las sondas Blackbox comprueban endpoints, conectividad, certificados y TLS. La experiencia real se instrumenta en los canales y mide operaciones efectivas. Una sonda HTTP no demuestra una compra completa ni sustituye el SLO de negocio. Los colectores de tienda necesitan cola persistente dimensionada y probada para 24 horas, con reinicio, saturación y drenaje. La auditoría obligatoria utiliza una ruta durable propia y no depende del muestreo de trazas.

Los almacenes, tableros, credenciales y eventos de seguridad son propios por ámbito. Una vista NOC/SOC agregada se limita al contrato de salud autorizado y a referencias mínimas de incidentes; no consulta libremente los almacenes de registros de ambos negocios. El observador del monitoreo y su canal de aviso deben sobrevivir a la falla que detectan. SOC/NOC, turnos y respuesta requieren una operación definida durante los 56 meses.

## 8. Cambios concretos que necesita SD-04

Los localizadores siguientes se comprobaron en `OSS-Subdocumento4.tex` de `work` el 22-10-2026, conservado en la copia de contraste indicada en la sección 1. Los títulos y frases permiten reencontrarlos si cambian las líneas. El trabajo debe realizarse sobre el `.tex` vigente mediante el flujo de exportación del proyecto.

### 8.1 Cambios en 4.1 Arquitectura lógica

Esta matriz separa las correcciones de coherencia de las decisiones de alcance todavía abiertas.

| ID | Localizador actual | Cambio necesario | Condición de cierre |
| --- | --- | --- | --- |
| CL-01 | Apertura 4.1 y explicación de Figuras 4.1–4.3; líneas 95–149. | Introducir la figura compacta, su leyenda, agrupaciones y vista de detalle; mantener ocho responsabilidades sin fila de actores. | Texto anterior y posterior interpreta la misma versión de figura. |
| CL-02 | Tabla 4.1; líneas 121–141. | Conservar cobertura de actores fuera de la vista principal y revisar AH-17/API vendedor externo retirado del dibujo. | Resolver su canal/contrato sin suprimir por inferencia un actor de alcance. |
| CL-03 | Estilo y límites; líneas 153–157. | Precisar que la base tecnológica y los símbolos agregados no comparten datos, tenants ni permisos entre negocios. | Matriz de instancias/autoridades consistente con figuras y física. |
| CL-04 | Tablas 4.2 y 4.3; líneas 165–209. | Mantener trece servicios, autoridades F:C-01/02/03 y despliegues candidatos; excluir F:C-04 del catálogo vigente. | Aprobación expresa antes de alterar catálogo, etapa o alcance. |
| CL-05 | Capas e interfaces; línea 213. | Describir los recorridos público y privado, App Gateway/APIM, gobierno lateral y capacidades comunes. | Ningún atajo Presentación→servicio/BD en modo conectado. |
| CL-06 | Integración; líneas 234–236. | Reescribir Event Hubs como Service Bus Premium con outbox, contratos síncronos, deduplicación, orden, errores y reconstrucción. | No conservar promesas heredadas de Kafka/replay/geo-replicación. |
| CL-07 | Vistas de bloques; líneas 248, 258, 268, 278, 288 y 298. | Regenerar o conciliar diagramas y párrafos de Tiendas, Mercadería, Venta, Clientes, Crédito e Integración. | Todos usan el mismo transporte, entrada y autoridad; no basta sustituir Fig. 4.3. |
| CL-08 | Crédito y frontera; líneas 268, 288 y 318. | Hacer explícita la mediación Ventas→X-01→APIM Filial y la respuesta mínima. | Contrato aprobado, identidad, timeout e idempotencia; otras finalidades cerradas. |
| CL-09 | Recorridos y consistencia; líneas 310–318. | Mantener venta/reserva/devolución; añadir coordinación durable, estados y compensaciones por propietario. | Pedido, devolución y formalización financiera descritos con fallo/reintento. |
| CL-10 | Apoyo predictivo; líneas 209, 344 y selección posterior. | Incorporar las cinco innovaciones con dueño, dependencias y contingencia; aclarar ayuda humana para merma. | Coincidencia con SD-13, EDT y pruebas; ningún ajuste autónomo de stock. |
| CL-11 | Despliegue lógico; líneas 330–332. | Actualizar recuperación de Filial y distinguir conectividad de servicios, sitios y residencia. | Segundo sitio y tránsito aprobados; Brasil no se convierte en autorización implícita. |
| CL-12 | Datos y seguridad; líneas 334–344. | Explicar ADLS restituido, ADF/trabajadores, PostgreSQL analítico y BI solo sobre esos modelos. | Alimentación, corte, trazabilidad, reconstrucción y frescura por indicador. |
| CL-13 | Datos y autoridad; líneas 209 y 344. | Separar búsqueda global OpenSearch, pgvector de Oferta y almacenes técnicos OpenMetadata/MLflow. | Propietario, permisos, entradas y recuperación de cada proyección. |
| CL-14 | Seguridad; líneas 348–350. | Desglosar identidad, cargas, equipos, HSM, privilegios, detección y archivo; TLS por salto. | Pruebas negativas de acceso y protección de campos/claves. |
| CL-15 | Continuidad; línea 352 y Figura 4.10. | Mantener diario/identidad local; precisar cupo Filial, caducidad, asignación exclusiva y conciliación. | Factibilidad demostrada sin abrir ni ampliar crédito offline. |
| CL-16 | Observabilidad; línea 354. | Sustituir la ruta genérica por Collector→Loki/Tempo/Prometheus y consultas Grafana; conservar Monitor acotado. | Separación de ámbitos, instrumentación real, sondas y cola local verificadas. |
| CL-17 | Tabla 4.5 y párrafo de ADR; líneas 366–375. | Revisar ADR-06 y sus alternativas; añadir decisiones de entrada privada, analítica, gobierno y telemetría. | Cada decisión conserva motivo, alternativa y prueba, sin atribuir selección a las Bases. |

### 8.2 Cambios en 4.1.1 y efectos sobre el resto de SD-04

La selección tecnológica necesita recoger las decisiones posteriores y sus costos de operación técnica, sin incluir precios en la oferta técnica.

| ID | Localizador actual | Cambio necesario | Condición de cierre |
| --- | --- | --- | --- |
| CL-18 | Introducción de 4.1.1 y Tabla 4.6; líneas 379–405. | Reemplazar la justificación de Event Hubs; actualizar Managed Redis, React Native, AKS, ADF, analítica, búsqueda, catálogo, MLflow y seguridad/telemetría. | Versión, soporte, compatibilidad, región y responsable por producto. |
| CL-19 | Tabla 4.6, fila Analítica; línea 396. | Cerrar la antigua elección pendiente de motor con PostgreSQL analítico dedicado, conservando ADLS y Power BI. | Modelos e indicadores definidos; DirectQuery/Import y conexión de datos documentados. |
| CL-20 | 4.2 Servicios contratados y redes; líneas 462–474. | Alinear productos, ruta de entrada y redes separadas con la lógica; revisar la noción de plataforma compartida. | Tenant y planos de gestión resueltos; rutas/DNS/firewall probados por ámbito. |
| CL-21 | HA, respaldos, mapeo y capacidad; líneas 490–550. | Rediseñar recuperación de mensajería y herramientas; completar tabla lógico→físico y cargas de datos/innovaciones. | RPO/RTO y capacidad acreditados mediante cálculo y ensayo por recurso. |
| CL-22 | Tienda tipo; línea 562. | Conciliar el cupo Filial alojado en tienda con el mesón que no atraviesa el nodo Retail. | Aislamiento físico/lógico propio, sin cupo en el diario comercial. |
| CL-23 | Centros de datos; líneas 595–609. | Reescribir continuidad y runbook sin asumir promoción Event Hubs ni réplica financiera a Brasil aprobada. | Destino independiente y secuencia de recuperación integral aprobados. |
| CL-24 | Referencias y declaración IA; líneas 611–646 y siguientes. | Depurar fuentes de productos retirados y registrar figuras/texto con IA Alto y revisión humana real. | Correspondencia de fuentes y revisión registrada, sin inventar aceptación. |
| CL-25 | Maestro SD-04 y adjuntos. | Corregir ruta del `.tex`, figura vigente, inventario de adjuntos, estado y remisiones a T-11/T-12. | Fuentes editables y PDF corresponden a la misma versión tras exportación. |

Las líneas del registro recibido pertenecen en parte a otra versión. Por ejemplo, las referencias al árbol de 17 suscripciones o a un único perfil global no se demuestran por sus números de línea en esta copia. Se conserva la decisión nueva, pero no se presenta esa referencia histórica como una contradicción textual ya comprobada.

### 8.3 Orden de explicación propuesto dentro de los títulos existentes

La estructura del Comunicado 10 se mantiene. Dentro de 4.1, primero debe explicarse la vista general y cómo leer las agrupaciones; después la autoridad de los trece servicios y las capacidades comunes. Siguen los recorridos de entrada/X-01, integración y procesos; luego datos/analítica/innovaciones y continuidad local. Seguridad y Observabilidad cierran la explicación transversal antes de las decisiones y condiciones de aceptación.

En 4.1.1 se presentan las tecnologías elegidas con su motivo, alternativas y verificación pendiente. Las cantidades, subredes, zonas, hardware, bóvedas, agentes y procedimientos de DR se desarrollan en 4.2/4.3 y T-11. Los detalles de Figuras 4.34/4.35 deben tener introducción e interpretación propias, no ser recortes ampliados de la figura general.

Un párrafo de entrada propuesto para la futura edición es el siguiente, sujeto a revisión del equipo.

> La arquitectura organiza la solución en ocho responsabilidades. Presentación, Borde y exposición, Puerta de enlace, Servicios de negocio, Integración y eventos y Datos muestran los recorridos principales. Seguridad y Observabilidad se aplican a todas ellas y se resumen en una banda lateral. Los servicios se agrupan en Mercadería, Venta, Relación con el cliente y Crédito, con X-01 como mediador del intercambio autorizado entre Retail y Filial. Los símbolos de producto y repositorio agrupan la lectura de la figura; cada ámbito y cada propietario conservan sus datos, permisos y contratos. La persistencia confirma la operación en el servicio responsable, mientras los hechos confirmados alimentan integraciones y proyecciones por el Service Bus de su ámbito.

## 9. Conciliación con alcance y otros entregables

SD-03 permanece intacto. Su catálogo, las plataformas que conserva y la compra offline con cupo previo son compromisos de referencia. La especificación recibida de capa 4 contiene recomendaciones de ampliar el catálogo, los RF y T-12; no deben ejecutarse automáticamente al incorporar su contenido al dibujo.

| Artefacto | Conciliación necesaria | Límite actual |
| --- | --- | --- |
| SD-03, 3.1–3.4 | Cobertura de canales/actores, plataformas conservadas, autoridad y compromisos offline. | Sin sustitución automática de e-commerce/fidelización ni alta de F:C-04. |
| Catálogo oficial v3.0 | Trazar atributos y brechas de servicios/capacidades. | RF-227–RF-231 del adjunto son propuesta, no requisitos oficiales aprobados. |
| SD-05 | Modelos por autoridad, contratos, calidad, corte, histórico, retención e índices. | No aceptar base común por el agrupamiento visual. |
| SD-07 y EDT | Desarrollo, implantación y operación de datos, capacidades comunes y herramientas. | Mantener hitos de meses 16/21 y horizonte de 56 meses. |
| SD-08 | Residencia/DR, cupo offline, dependencia de proveedores y operación autogestionada. | Selección gráfica no cierra un riesgo ni acredita normativa. |
| SD-09 | Pruebas de consistencia, seguridad, calidad de datos, recuperación y modelos. | Los ensayos aquí descritos son propuestos, sin resultado de plataforma. |
| SD-10/SD-11 | NOC/SOC, runbooks, retención de señales, soporte y actualizaciones. | Grafana/Sentinel no proporcionan por sí solos dotación ni operación 24×7. |
| SD-13 | Cinco innovaciones, modelos, datos autorizados y contingencias. | Conservar pgvector y revisión humana; no extender MLflow a Filial sin necesidad. |
| T-11 y oferta económica | Inventario, niveles, versiones, licencias, dependencias y operación a 56 meses. | Sin cobertura genérica de Backup ni productos autogestionados sin soporte previsto. |
| T-12 | Relacionar capacidades, controles y evidencia con requisitos vigentes. | No cambiar a «Sí» por seleccionar una herramienta o dibujar un enlace. |

## 10. Pendientes que condicionan el cierre

Los productos ya seleccionados no se vuelven a abrir por aparecer aquí. Los pendientes distinguen decisiones humanas de contratos y verificaciones técnicas.

| Prioridad | Trabajo | Responsable propuesto | Evidencia de cierre |
| --- | --- | --- | --- |
| P0 | Confirmar tenant Filial, residencia, metadatos, tránsito de borde y destinos de recuperación. | Mandante, jurídico y seguridad. | Aprobación específica y matriz por producto/región/plano. |
| P0 | Definir segundo sitio de Filial y recuperación integral; Brasil condicionado. | Arquitectura y continuidad. | Sitio independiente, dependencias y ensayo RPO/RTO. |
| P0 | Cerrar compra por X-01, autoridad cupo/cuenta y política offline. | Ventas, Originación, Cartera y Riesgo. | Contratos, estados, pruebas concurrentes, expiración y conciliación. |
| P0 | Resolver aplicabilidad de finanzas abiertas y propuesta F:C-04. | Contraparte financiera y equipo de alcance. | Decisión normativa y de alcance explícita, sin calendario inferido de notas. |
| P1 | Completar catorce interfaces, sagas y contratos síncronos. | Integración y proveedores. | Matriz con confirmaciones, fallos, compensaciones y autoridad. |
| P1 | Definir capacidades comunes y maestro de ubicaciones. | Arquitectura y dueños de procesos. | Propietarios, datos, consumidores, producto y permisos. |
| P1 | Diseñar modelos analíticos, alimentación y reconstrucción. | Datos, Comercial y Finanzas. | Diccionario de indicadores, corte, detalle navegable y SLA de frescura. |
| P1 | Verificar regiones, TLS por salto, niveles y dependencias de herramientas. | Plataforma y seguridad. | Matriz de compatibilidad y prueba en la suscripción prevista. |
| P1 | Definir retenciones, copia temporal Bastion y recuperación por recurso. | Datos, jurídico y seguridad. | Política por clase y restauración con claves/permisos. |
| P1 | Completar telemetría, supervisión independiente y operación. | SRE/NOC/SOC. | Configuración, capacidad, rutas de aviso, turnos y runbooks. |
| P2 | Cerrar contratos lockers/publicidad y modelo multimodal/conteo. | Pedidos, Oferta, Existencias y datos. | Contraparte, evaluación, fallback y promoción humana. |
| P2 | Comprobar visualmente la última importación del CSV. | Equipo de diagramación. | Importación revisada frente al JSON y draw.io de referencia. |

F:C-04 es la tarjeta intencionalmente sin contratos operacionales. Las bandas transversales y la columna tecnológica resumen dependencias que no se dibujan individualmente. En cambio, tareas humanas, firma/mensajería, maestro de ubicaciones y ciertas interfaces externas sí conservan definiciones pendientes; una asociación de área no las convierte en contratos cerrados.

### 10.1 Pruebas que deben acompañar la nueva explicación

La futura aceptación requiere medir recorridos completos, con umbral y fuente contractual comprobados.

- Venta a disponible publicado dentro de 30 segundos y cambio de precio a cajas/canal dentro de cinco minutos, sin deducirlos del TTL o del broker.
- Posición financiera antes de las 07:00 del día siguiente, con atrasos, datos tardíos, conciliación y trazabilidad hasta origen.
- Duplicados, desorden, omisiones, reintentos y DLQ, sin doble cobro, doble consumo de cupo ni doble agregado analítico.
- Reconstrucción de modelos e índices desde corte autorizado, manifiesto y deltas; restauración de estados, claves y documentos.
- Denegación de accesos cruzados entre ámbitos, incluida búsqueda, metadatos, BI, telemetría y archivos; compra mínima válida y finalidad no autorizada rechazada en X-01.
- Operación local, reinicio y cola durable durante el horizonte previsto; reconexión, expiración, reservas concurrentes y conciliación financiera.
- Integridad de evidencia, copia WORM, resistencia a alteración y pérdida de la ventana temporal de grabación.
- Caída de colectores, backends y canal de alertas; aviso desde una posición independiente y distinción entre sitio no observable y falla confirmada.
- Evaluación temporal de modelos, revocación de permisos en índices, promoción humana, reversión y alternativa manual.

## 11. Entrega, verificación y secuencia de implementación documental

La entrega vigente comprende el [draw.io editable](../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.drawio), [PNG](../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.png), [SVG](../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.svg), [JSON](../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.json) y [CSV](../../04_Adjuntos/diagramas/diag-04-36_csv_conservar-capas.csv). Los detalles complementarios son [Datos 4.34](../../04_Adjuntos/diagramas/diag-04-34_detalle-datos.drawio) y [Transversales 4.35](../../04_Adjuntos/diagramas/diag-04-35_detalle-transversales.drawio). Las figuras anteriores se conservan como antecedentes, sin sustituir esta precedencia.

La [verificación de la composición](composicion-compacta-2026-10-22/verificacion.json) registra 79 componentes, 53 relaciones, 205 filas CSV y 26 puertos gráficos de asociación. El JSON y el draw.io del renderizador pasaron los controles de la guía/MCP. La última versión CSV tiene referencias estructurales comprobadas, pero su prueba visual final no se ejecutó porque la revisión automática quedó bloqueada por límite de uso. El draw.io entregado procede del MCP, no de esa última importación CSV.

La validación gráfica no acredita despliegue, capacidad, residencia, cumplimiento normativo ni aceptación del mandante. No se ejecutaron las pruebas de plataforma propuestas en este documento.

Al preparar esta recopilación se comprobaron sus enlaces locales, los 25 identificadores de cambio y la coincidencia de los conteos con el JSON. Se repitieron la validación L2, el linter del draw.io y el harness de la guía, sin fallos. La comprobación mecánica de redacción de T7-04 informó cero errores y cero avisos; ese resultado no detecta ni resuelve las diferencias semánticas descritas aquí. Las 21 fuentes protegidas de la línea base conservaron sus huellas SHA-256.

La implementación documental debe avanzar en el siguiente orden.

1. Resolver o mantener explícitas las decisiones P0 y cerrar contratos que determinen autoridad, rutas y consistencia.
2. Actualizar 4.1 y ADR, con la figura general y detalles coherentes; conservar las etapas y el alcance vigente.
3. Actualizar 4.1.1, el mapeo de 4.2/4.3 y T-11; alinear modelos, pruebas, riesgos y operación en sus subdocumentos.
4. Revisar T-12 y trazabilidad contra el catálogo oficial, sin asignar cumplimiento por inferencia.
5. Ejecutar el flujo corporativo de verificación/compilación y revisar fuentes, remisiones, figuras e IA. El estado «revisado» requiere registro humano.

## Declaración de uso de IA

Recopilación, contraste documental y propuesta de cambios elaborados con asistencia de Codex. Nivel de texto Alto. Se aplicó revisión de claridad conforme a las reglas de redacción y humanizer del proyecto, sin alterar autoridades, IDs ni compromisos. Este documento no incorpora una revisión humana formal, no modifica la oferta compilada y no asigna estado «revisado» a sus fuentes.
