# Informe de propuesta: arquitectura lógica por etapas

**Estado:** propuesta de arquitectura y fundamento de las vistas lógicas; pendiente de incorporar a SD-04 y validar contratos de terceros.

**Alcance:** vista lógica de la Etapa 1 y de la Etapa 2 de la solución Ancoa.

**Criterio visual acordado:** lectura vertical desde actores y vistas hacia conexiones propuestas, middleware, datos propios y servicios de negocio; límites verticales entre Retail y Filial emisora. Las capas exigidas se explican en el texto, sin dividir la figura en bandas horizontales. Los componentes se identifican por nombre e icono.

## 1. Base comprobada y decisiones de diseño

| Asunto | Hecho o decisión vigente | Implicación para la vista |
| --- | --- | --- |
| Integración actual | Existen 14 interfaces punto a punto, en su mayoría mediante archivos y lotes nocturnos. No se dispone del mapa completo. | Mostrar el conjunto de interfaces antiguas como **haz de convivencia**, sin atribuir falsamente las 14 conexiones a pares concretos. El levantamiento es una entrega temprana. |
| Integración objetivo | SD-03 propone una plataforma de integración que sustituye las conexiones directas y mantiene la coherencia entre plataformas. | Todas las integraciones **entre sistemas o dominios** se publican y gobiernan desde una capa lógica común de middleware. Sus capacidades se distribuyen y redundan; no se presupone una sola instancia física. |
| Frontera jurídica | Retail y la Filial emisora conservan autoridades de datos separadas; X-01 gobierna finalidad, autorización, minimización y evidencia de los cruces. | Separar los dos ámbitos y sus almacenes. El middleware transporta, pero la autorización se aplica también en los extremos; X-01 no es una base maestra compartida. |
| Etapas | La Etapa 1 entra en producción en el mes 16 y la Etapa 2 en el mes 21. | Construir las capacidades base de middleware, identidad, seguridad y observabilidad en Etapa 1; incorporar conectores y flujos adicionales en Etapa 2. |
| Continuidad | Prevalece la autonomía local mínima de 24 horas exigida por las Bases Transversales. | El POS y el almacenamiento local operan durante la pérdida de enlace y envían sus hechos pendientes al reconectar. No dependen del middleware central durante el corte. |
| Tiempos del caso | Disponibilidad publicada ≤30 s tras una venta; precio en cajas y canal digital ≤5 min; estado de pedido en tiempo real. | No usar el lote nocturno como mecanismo de estas promesas. Reservar lotes para las contrapartes o consolidaciones que toleran esa latencia. |

**Fuentes:** [Caso 09, integraciones actuales](../../00_Bases/Caso_09_Cadena_Multitienda.md#L318), [Caso 09, objetivos operativos](../../00_Bases/Caso_09_Cadena_Multitienda.md#L797), [Bases Transversales, capas y resiliencia](../../00_Bases/Bases_Transversales.md#L115), [Bases Transversales, autonomía](../../00_Bases/Bases_Transversales.md#L185), [SD-03, solución y transición](../../02_Propuesta/latex_final/sd-03.tex#L408), [Bases Administrativas, calendario](../../00_Bases/Bases_Administrativas.md#L455).

Las ubicaciones y contratos aún desconocidos de cada plataforma se tratan en la [matriz de hipótesis físicas y de interacción](supuestos_plataformas_y_conexiones.md); no se convierten en hechos del estado actual por aparecer en un producto comparable.

## 2. Arquitectura final propuesta

Se propone un **middleware lógico común y modular**, implantado en la plataforma híbrida, con estas capacidades diferenciadas:

1. **Puerta de enlace y exposición:** autenticación, autorización, control de tasa, versionado y contratos para canales y terceros. El borde público se mantiene como capa distinta de la integración interna.
2. **Mediación síncrona:** llamadas con respuesta inmediata cuando el proceso la necesita, con tiempo de espera, control de falla e idempotencia. La autorización financiera y los pagos son ejemplos; no se transforman artificialmente en lotes.
3. **Intermediario persistente de eventos:** publicación de hechos de venta, existencia, precio, pedido y posventa; entrega al menos una vez, consumidores idempotentes, reintentos y cola de mensajes fallidos.
4. **Adaptadores de sistemas conservados y legados:** traducción de contrato y formato, recepción/emisión de archivos, intercambio programado, validación, acuse y conciliación. Cada adaptador encapsula una contraparte; la solución no requiere que el tercero adquiera una API que no posee.
5. **Programación y conciliación:** tareas periódicas, comparación de totales, reproceso controlado, observabilidad de atraso y resultado de cada lote.
6. **Gobierno:** catálogo de interfaces y eventos, propietarios, versiones, trazas correlacionadas y control de cruces Retail–Emisor mediante X-01 y controles en ambos extremos.

«Todo conectado al middleware» se entiende como **toda integración entre sistemas y dominios gestionada por esta plataforma**. Cada servicio mantiene acceso a su propio almacenamiento y responsabilidad sobre sus datos. La operación local desconectada usa el almacenamiento del nodo de tienda y sincroniza al recuperar conectividad. Esta interpretación evita convertir el middleware en base de datos común, motor de decisiones comerciales o punto único de falla.

Las ocho capas obligatorias quedan explícitas: presentación; borde y exposición; puerta de enlace; servicios de negocio; integración y eventos; datos; seguridad transversal; observabilidad transversal. El diseño lógico no fija proveedor, motor ni topología física. [Bases Transversales, RT-02.01–02.11](../../00_Bases/Bases_Transversales.md#L115).

**Decisión de arquitectura propuesta para registrar como ADR:** escoger middleware modular sobre un bus empresarial único y rígido. El bus único simplifica el dibujo y ofrece un lugar común para transformar mensajes, pero concentra fallas, cambios y capacidad en una ruta obligatoria. La opción modular mantiene gobierno y catálogo comunes con gateway, broker y adaptadores independientes, permite escalar por carga y conserva una ruta local de tienda cuando falta enlace. También exige más disciplina de contratos, operación y trazabilidad; esos costos deben constar en el ADR. Las conexiones punto a punto sin gobierno se descartan porque reproducen el problema actual. Esta comparación responde a la exigencia de justificar el estilo elegido frente a alternativas. [Bases Transversales, RT-02.04 y 2.3](../../00_Bases/Bases_Transversales.md#L136).

## 3. Vista prevista para Etapa 1: convivencia controlada

**Contenido de la vista:**

| Conjunto lógico | Componentes que deben aparecer |
| --- | --- |
| Personas y canales | Cliente, personal de tienda, POS nuevo en tiendas migradas, POS 2014 en tiendas pendientes, comercio electrónico existente, personal bajo rol financiero y carga estructurada de Concepción. |
| Borde y acceso | Protección de entrada y puerta de enlace con rutas y permisos separados para Retail y Filial emisora. |
| Servicios Retail nuevos | R:M-01 Oferta comercial, R:M-03 Existencias y R:V-02 Ventas. |
| Frontera y servicios financieros nuevos | X-01 Control de cruces; F:C-01 Originación de crédito y F:C-03 Evidencia financiera; F:C-02 Cartera de crédito **en migración por olas**, claramente marcado como parcial. |
| Middleware | Mediación API, eventos persistentes, adaptadores de archivo/lote, programador, deduplicación, conciliación y catálogo de contratos. Estas capacidades son base definitiva de la Etapa 2. |
| Sistemas coexistentes | Núcleo Retail 2009 y plataforma de crédito 2011 en transferencia; ERP/DTE, WMS principal, marketplace, comercio electrónico y fidelización conservados o bajo evaluación. |
| Datos | Autoridades nuevas por servicio y almacenes legados durante la migración, sin doble autoridad indefinida; almacenamiento local POS para 24 horas; analítica separada por ámbito. |

En esta etapa **R:V-01 Pedidos todavía no existe**: pedidos, recepción y reposición que aún dependan de plataformas antiguas se muestran como rutas transitorias por adaptador. El sistema de ventas nuevo recibe el registro oficial de las ventas de su alcance y concilia operaciones; no se dibuja una escritura indistinta en dos autoridades. La migración de cartera comienza sin presentar F:C-02 como totalmente sustituido. [SD-03, reparto](../../02_Propuesta/latex_final/sd-03.tex#L469), [SD-03, convivencia](../../02_Propuesta/latex_final/sd-03.tex#L412).

## 4. Vista prevista para Etapa 2: arquitectura objetivo

La segunda vista mantiene el mismo orden visual, colores, posiciones de dominio y leyenda. Se añaden R:M-02 Abastecimiento; R:V-01 Pedidos; R:V-03 Comisiones; R:V-04 Marketplace; R:CL-01 Posventa; R:CL-02 Clientes Retail, y se completa F:C-02 Cartera de crédito. Aparecen así los **trece servicios**: nueve de Retail, tres de la Filial emisora y X-01. Los núcleos Retail 2009, crédito 2011 y POS 2014 solo se retiran una vez completadas las olas, conciliaciones y pruebas de retorno; la figura objetivo puede mostrarlos fuera del contorno operativo con la leyenda «retirados tras aceptación».

ERP/DTE, WMS principal y marketplace se conservan y se integran mediante adaptadores. Comercio electrónico y fidelización permanecen inicialmente integrados; su sustitución o remediación depende de la evaluación de Etapa 1. Concepción aporta registros estructurados por personal: no se inventa un WMS o nodo local nuevo. El portal financiero recibe contenido del ámbito Emisor aunque comparta punto de entrada visual con el portal público; la sesión y las rutas conservan separación por rol. [SD-03, catálogo](../../02_Propuesta/latex_final/sd-03.tex#L418), [SD-03, plataformas conservadas](../../02_Propuesta/latex_final/sd-03.tex#L408), [Contexto SD-04, D-07 a D-09](contexto_sd-04.md#L15).

## 5. Mapa óptimo propuesto de intercambios

Esta tabla define **familias de conexión de la solución propuesta**, no afirma que sean las 14 interfaces actuales. El modo definitivo por contraparte se registra tras el levantamiento exigido y las pruebas de contrato. «Middleware» designa las capacidades del punto 2; el acceso de un servicio a sus datos propios queda fuera de esta matriz.

| Origen → destino | Etapa | Modo propuesto en middleware | Dato o finalidad | Precaución |
| --- | --- | --- | --- | --- |
| R:M-01 Oferta → POS y canal digital | 1–2 | Publicación de cambio + consulta versionada | Precio y promoción vigente | Propagación ≤5 min, comprobación de versión y conciliación de etiquetas. |
| R:V-02 Ventas → R:M-03 Existencias | 1–2 | Evento persistente de venta; relectura puntual si hace falta | Movimiento que modifica disponibilidad | Publicación de disponible ≤30 s; clave idempotente. |
| POS local → R:V-02 Ventas | 1–2 | En línea normalmente; cola local y sincronización al volver el enlace | Venta, cobro y folio de operación | 24 h de autonomía; no duplicar ventas durante el drenaje. |
| Comercio electrónico existente ↔ servicios Retail disponibles | 1 | API de exposición y adaptador; eventos de cambio | Oferta y disponibilidad; venta/pedido según capacidad habilitada | En Etapa 1 el pedido sigue en la ruta heredada mientras R:V-01 no existe. |
| R:V-01 Pedidos ↔ R:M-03 Existencias | 2 | Solicitud/respuesta versionada para reserva; evento de estado | Reserva y promesa de entrega | Evitar confirmar pedido sin resultado de reserva. |
| R:V-01 Pedidos ↔ WMS principal/transportistas | 2 | Adaptador API, archivo o lote según contraparte; eventos internos de estado | Preparación, despacho y entrega | WMS conserva ejecución física; estado del pedido debe ser oportuno. |
| R:M-02 Abastecimiento ↔ WMS principal y proveedores | 2 | Adaptadores por contraparte; archivo/lote si es el canal disponible | Órdenes, recepción y movimientos | Canal de proveedores por decidir; no afirmar portal nuevo. |
| R:V-04 Marketplace ↔ plataforma conservada | 2 | Adaptador API o archivo según contrato comprobado | Catálogo, disponibilidad, pedido, devolución y liquidación | El servicio nuevo gobierna la relación; no reemplaza la plataforma. |
| R:CL-01 Posventa ↔ R:V-02/R:M-03/R:V-04 | 2 | Consulta de venta y eventos de resolución | Devolución, reversa comercial, reingreso | La devolución no incrementa existencia vendible hasta la decisión de inspección. |
| R:V-03 Comisiones → remuneraciones/ERP | 2 | Evento o archivo/lote conciliado | Base de comisión aprobada | ERP conserva remuneraciones. |
| R:V-02 Ventas ↔ ERP/DTE | 1–2 | Adaptador según interfaz real, con acuse y conciliación | Estado del documento tributario | ERP/DTE es emisor único; contingencia sin enlace requiere aprobación. |
| R:V-02 Ventas ↔ F:C-01 Originación | 1–2 | Solicitud/respuesta por operación, bajo política X-01 | Importe/referencia → decisión mínima | Sin saldo o mora para Retail; denegación por defecto y auditoría en ambos extremos. |
| F:C-01/F:C-02 ↔ F:C-03 Evidencia | 1–2 | Contrato interno financiero de consulta/registro | Información precontractual y aceptación | Apertura o repactación no avanza sin evidencia suficiente. |
| F:C-02 Cartera ↔ plataforma crédito 2011 | 1–2 | Adaptador de convivencia y migración por olas | Cartera y conciliación | Retiro solo tras cuadratura aprobada. |
| F:C-02 Cartera → ERP | 1–2 | Lote conciliado cuando la contraparte lo permita | Devengo, provisiones y contabilidad | El caso ya describe este flujo por lote en el estado actual. |
| Servicios responsables → analítica de su ámbito | 1–2 | Publicación gobernada de datos/eventos | Indicadores y autoservicio | Retail y Emisor separados; cruce sujeto a X-01. |

**Criterio de selección:** solicitud/respuesta para decisiones que bloquean la operación; eventos persistentes para propagar hechos sin acoplar a todos los consumidores; lote validado para contrapartes o procesos que toleran demora. El middleware no altera quién decide ni quién conserva el dato. Los contratos deben indicar modo, volumen, ventana y respuesta ante falla, además de versionado, correlación y seguridad. [Bases Transversales, RT-05.16–05.21](../../00_Bases/Bases_Transversales.md#L268).

## 6. Crítica y controles obligatorios

| Riesgo de la arquitectura | Control propuesto |
| --- | --- |
| Convertir «middleware común» en un bus único y bloqueante | Separar gateway, mediación, broker y adaptadores como capacidades escalables y redundantes; probar caída de componentes y declarar puntos únicos de falla. |
| Dibujar todas las interfaces conservadas como API | El Caso confirma mayoría de archivos/lotes actuales. D-01 en el contexto SD-04 es una **hipótesis de interfaz objetivo para estimación**, no un inventario real. Adaptadores y estimación deben ajustarse al mapa levantado. |
| Extender lote nocturno a las cuatro promesas | Precio, disponibilidad y estado de pedido usan contratos/eventos oportunos, medidos contra las metas del Caso. |
| Usar X-01 como único control de red o juntar datos Retail y Emisor | Aplicar política, minimización y auditoría en emisor y receptor; almacenes y espacios analíticos separados. |
| Depender del middleware central para vender sin enlace | POS y nodo local registran ventas y condiciones vigentes; salida diferida con idempotencia y conciliación tras recuperar red. |
| Prometer compra con tarjeta propia sin conexión de forma incondicional | El Emisor fija topes y exclusiones, se ensaya el cupo previo en piloto y, si falla, la compra con esa tarjeta queda no disponible durante el corte. No se abren tarjetas ni amplían cupos sin enlace. |
| Prometer tributación offline sin contrato | ERP/DTE mantiene la autoridad; la modalidad de contingencia se aprueba y prueba antes de comprometerla. |

## 7. Decisiones que faltan antes de cerrar SD-04

1. **Inventario real de las 14 interfaces:** pares, dueño, formato, transporte, frecuencia, volumen, fallas y posibilidad de sustitución. Se levanta en Etapa 1; no bloquea este mapa objetivo, pero sí su especificación final y la estimación por adaptador.
2. **Canales concretos de terceros:** proveedor de mercadería (archivo o portal mínimo), procesadores y terminales de pago, contratos de transportistas, y federación con el directorio del cliente. Mantener las alternativas explícitas hasta validar la contraparte.
3. **Reglas de continuidad:** topes de tarjeta propia fijados por el Emisor, prueba de 24 h, ventana de reconciliación y procedimiento tributario aprobado por ERP/DTE. La reversa financiera requiere contrato y aprobación de finalidad antes de habilitar su cruce.
4. **Evaluación de comercio electrónico y fidelización:** conservar, remediar o sustituir con evidencia en la Etapa 1; actualizar la vista de Etapa 2 solo después de la decisión.
5. **Catálogo de contratos objetivo:** por cada flecha de la sección 5, propietario, campos mínimos, versión, seguridad, latencia, volumen, acuse, reintento, deduplicación, monitoreo y ruta de falla. Registrar las elecciones relevantes como ADR.

## 8. Figuras lógicas y uso en SD-04

Las nuevas vistas de [Etapa 1](../../04_Adjuntos/diagramas/borradores/generated-diagrams/diag-04-04a_arquitectura-logica-etapa-1-mcp.png) y [Etapa 2](../../04_Adjuntos/diagramas/borradores/generated-diagrams/diag-04-04b_arquitectura-logica-etapa-2-mcp.png) se generaron con `generate_diagram` del [MCP de andrewmoshu](https://github.com/andrewmoshu/diagram-mcp-server), mediante una sesión MCP de protocolo real en memoria. Sus fuentes son [generador MCP](../../04_Adjuntos/diagramas/borradores/diag-04-04_generar_mcp.py), [draw.io Etapa 1](../../04_Adjuntos/diagramas/borradores/generated-diagrams/diag-04-04a_arquitectura-logica-etapa-1-mcp.drawio) y [draw.io Etapa 2](../../04_Adjuntos/diagramas/borradores/generated-diagrams/diag-04-04b_arquitectura-logica-etapa-2-mcp.drawio). Las vistas anteriores [04-03a](../../04_Adjuntos/diagramas/borradores/diag-04-03a_arquitectura-logica-etapa-1.svg) y [04-03b](../../04_Adjuntos/diagramas/borradores/diag-04-03b_arquitectura-logica-etapa-2.svg) permanecen como guías de contenido, no como figuras finales. La [vista de flujos críticos](../../04_Adjuntos/diagramas/borradores/diag-04-02c_flujos-logicos-criticos.svg) conserva los intercambios sin presentar las 14 interfaces antiguas como pares conocidos.

Los iconos representan **tipos de tecnología** —clientes, nube/conectividad, API, eventos, archivo/lote, datos y servicios—, no marcas seleccionadas. Los productos y motores se deciden en 4.1.1. En Etapa 2, tres iconos Retail agrupan visualmente nueve servicios: Mercadería = Oferta comercial, Abastecimiento y Existencias; Venta = Pedidos, Ventas, Comisiones y Marketplace; Relación = Posventa y Clientes Retail. Cada servicio conserva su propio almacén; el único icono de «BD por servicio» representa ese conjunto de almacenes separados. ERP/DTE, WMS principal, marketplace conservado y fidelización se muestran como plataformas diferenciadas; su conexión dibujada por archivos y lotes expresa una **ruta propuesta que se verifica por contrato**, no un protocolo ya conocido para cada una. Las ubicaciones de plataformas y «Casa matriz» siguen siendo supuestos por validar en 4.2.

La revisión de canales y actores detectó omisiones en la primera versión de estas figuras. Se incorporaron el mesón financiero y su terminal de pago en el ámbito de la Filial emisora, el mesón de atención Retail, las terminales compartidas de sala, la carga de Concepción y los medios de pago externos como contraparte lógica. En Etapa 1, el mesón de atención convive con los procesos antiguos. La línea azul entre ámbitos representa exclusivamente la solicitud de autorización de compra con tarjeta propia; X-01 expresa la política que limita ese intercambio, no una ruta física adicional. El [registro de cobertura y pendientes](auditoria_canales_arquitectura_logica.md) distingue los componentes ya visibles de los canales y flujos que requieren detalle en SD-04.

Las figuras generales representan los ámbitos Retail y Filial emisora, la frontera X-01, el middleware modular y el nodo local POS. Las ocho capas requeridas se explican en las secciones 1–2 y se mapean en el texto de SD-04; no se emplean como divisiones visuales. Los rótulos breves identifican componentes; las decisiones de integración, supuestos y controles permanecen en las secciones 1–7 de este informe. En la vista de flujos, el trazo discontinuo significa **modo de conexión objetivo por validar** con la contraparte, no que el intercambio por archivo o lote esté confirmado. La continuidad de tienda web y fidelización en la vista de Etapa 2 está sujeta a la evaluación de Etapa 1, según la decisión 4 de la sección 7.

El diagrama debe citarse y explicarse en el capítulo 4.1, mapearse por completo con 3.3 y 3.4 y conservar los nombres del catálogo. La tecnología concreta corresponde a 4.1.1 y el despliegue físico a 4.2. [Comunicado 10, sección 4.1](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L660), [Rúbrica de cierre, S4-01](../revision_informe_1_rubrica_de_cierre.md#L132).

**Estado del artefacto:** figuras elaboradas como propuesta visual; faltan el levantamiento de interfaces, la validación de contratos y la incorporación editorial en SD-04.

## 9. Vistas de detalle por bloque

Las vistas generales anteriores se amplían mediante [doce diagramas por bloque y etapa](mapa_bloques_y_tecnologias.md): Tiendas Físicas, Mercadería, Venta y cumplimiento, Relación con clientes, Crédito y frontera, e Integración transversal. Cada bloque repite solo los componentes compartidos necesarios para entender sus flujos. El mismo documento registra los iconos tecnológicos obtenidos del MCP y distingue las tecnologías **candidatas** de las plataformas existentes cuyo fabricante no consta en el Caso. Estos productos se justifican o sustituyen al redactar SD-04 4.1.1.
