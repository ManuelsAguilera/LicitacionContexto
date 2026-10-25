# Explicación de la arquitectura lógica por capas y columnas
Actualización de emplazamiento del 23-10-2026. El usuario confirmó producción Retail y Filial en Chile Central y recuperación de ambos en Brazil South. Las menciones posteriores a Brasil condicionado o destino financiero pendiente conservan el estado histórico del corte anterior. Para las próximas modificaciones rige el [registro de decisiones físicas](../fisica-general-zonas-2026-10-23/decisiones-2026-10-23.md).


Fecha de corte: 23-10-2026. Versión documental: 1.0. Estado: borrador de contexto para modificaciones posteriores de SD-04. Proponente: Only Simple Solutions. Sin revisión humana formal ni acreditación de despliegue.

Este documento explica la imagen que el usuario identificó como nuevo diagrama lógico. Conserva el propósito de sus elementos, sus relaciones, el alojamiento propuesto, las razones de selección y los asuntos que deben resolverse antes de modificar la oferta. La imagen recibida gobierna la identificación y disposición de las tarjetas; los registros anteriores aportan el detalle que la imagen resume. Cuando discrepan, se registra la diferencia en la sección 15 y se conserva abierta su resolución.

La explicación es un artefacto de trabajo. Las Bases mantienen su precedencia y los `.tex` siguen siendo la fuente de los subdocumentos importados. Este archivo no cambia SD-03, SD-04, T-11, T-12 ni el catálogo oficial de requisitos. Tampoco convierte los pendientes en decisiones aprobadas.

## 1. Imagen, procedencia y uso de esta referencia

La copia siguiente permite reconocer la versión que se está explicando, aunque desaparezca el adjunto temporal de la conversación.

![Arquitectura lógica por capas, vista por columnas recibida el 23-10-2026](diagrama-recibido.png)

Fuente de la imagen: archivo aportado por el usuario en esta conversación, titulado «Arquitectura lógica por capas · vista por columnas». La autoría gráfica y la herramienta de origen no se acreditan mediante el PNG. El usuario lo identificó como el nuevo diagrama; ello no constituye revisión humana formal de todos sus contratos o de su arquitectura física.

El original recibido tiene 8192 × 4598 píxeles. Su SHA-256 es `590f6debf2bb0fe3a5ef4d58b08ddb3b4a49c043709f2016e63a85b4ee980c2c`. Se conserva sin edición en [diagrama-recibido.png](diagrama-recibido.png). No se recibió el draw.io, JSON o modelo editable correspondiente. Esta referencia no le asigna un número oficial de figura ni sobrescribe la figura 4.36.

La consulta se realizó sobre la copia `work@768a1cae35ba07a437f32509e4d21e5b308f05fb`, con `main` y `origin/main` en `1dfdbad4ce8e1bfbd10c4a3c0177db05cef35681`. La propuesta física de [FI04]–[FI08] estaba presente como trabajo local sin seguimiento Git al comenzar esta documentación. Por eso se identifica como propuesta física previa y no como contenido ya publicado en `main`. Las huellas de las fuentes locales quedan en [huellas-fuentes.txt](huellas-fuentes.txt).

### 1.1 Cómo distinguir los fundamentos

Las referencias `[FIxx]` remiten a fuentes internas y `[FTxx]` a documentación técnica oficial. Las fuentes se identifican en la sección 17. Los IDs de esta explicación, como `B05` o `D14`, son localizadores internos; no reemplazan códigos RF, RNF, RT, ADJ ni los códigos de servicios.

Se utiliza «registrado» para una selección presente en las notas de arquitectura, «visible» para lo que muestra la imagen y «propuesto» para un desarrollo físico o contractual aún revisable. «Pendiente» significa que la fuente no resuelve el detalle o que el nuevo dibujo requiere conciliación. Ninguna de esas expresiones equivale a un recurso aprovisionado o una prueba aprobada.

Los requisitos generales se mantienen como trazabilidad por ID. Una herramienta puede cubrir parte de una capacidad sin estar exigida por marca. Las remisiones a las notas del Caso son antecedentes internos; este documento no crea citas del Caso con folios sin comprobación visual. Antes de trasladar una afirmación particular a la oferta se aplicará `citas-proyecto` y se verificará su folio impreso.

## 2. Qué problema resuelve la organización del diagrama

El diseño organiza canales, autoridades de negocio e integración para coordinar plataformas conservadas y servicios nuevos. La justificación del registro lógico es sostener una oferta publicada reconocible, un disponible de existencias confiable, una promesa de pedido y una operación financiera con evidencia. La separación de Retail y Filial emisora condiciona datos, identidad, interfaces y operación. Estas son las razones de arquitectura recogidas en [FI01], secciones 2, 4 y 5; no se derivan de contar cajas en la imagen.

El despliegue híbrido responde al Art. 16 y a RT-03. La nube concentra servicios centrales y los sitios conservan ejecución local para las funciones que necesitan continuidad. El horizonte contractual se mantiene en 56 meses, con producción E1 en mes 16 y E2 en mes 21. Las etiquetas E1/E2 indican implantación funcional; no significan dos nubes ni dos versiones simultáneas de cada componente.

La solución se evalúa por correctitud, aislamiento, disponibilidad, operación y capacidad. La selección de productos y su dimensionamiento deben sostener esos objetivos. La documentación de selección no autoriza reducir calidad para cumplir una cifra de costo ni demuestra que una marca sea obligatoria.

## 3. Cómo leer columnas, puntos y flechas

Las seis columnas numeradas ordenan Presentación, Borde, Puerta de enlace, Servicios de negocio, Integración y Datos. Las bandas inferiores representan Seguridad y Observabilidad aplicadas a las columnas. La troncal tecnológica reúne tecnologías y herramientas de construcción o gobierno; sus tarjetas no son etapas sucesivas del procesamiento de una venta.

El punto azul identifica Retail y el morado identifica Filial emisora. Dos puntos indican que existe una responsabilidad aplicable a ambos ámbitos. La interpretación registrada exige recursos, permisos, datos y credenciales separados cuando corresponda. Un símbolo de producto no demuestra una instancia común. En particular, «una instancia por ámbito» para capacidades comunes expresa separación de negocio, pero todavía necesita definir producto, réplicas y almacenamiento.

La leyenda de la imagen distingue API/solicitud en azul, persistencia propia en verde, publicación y consumo en naranja, consumo en morado, contrato externo en turquesa discontinuo, cruce por X-01 en rojo, gobierno/catálogo en ocre y flujo analítico en gris. Cada familia se explica en la sección 13. El color describe intención lógica; los puertos y el iniciador de una conexión física se determinan en [FI08]. Una línea que resume varias relaciones no prueba que todas compartan protocolo, credencial o frecuencia.

Los asteriscos aparecen en múltiples tarjetas sin una nota que los defina en la imagen. Se conserva esa observación y no se les atribuye automáticamente el significado de compra, aprobación, dependencia o requisito. Su leyenda queda como pendiente `P01`.

## 4. Troncal tecnológica y capacidades comunes

Estas piezas permiten construir, entregar y administrar la solución. El bloque reúne lenguajes, entornos de ejecución, servicios de plataforma y funciones transversales. Por ello su alojamiento depende de la función concreta y no de una ubicación común para toda la columna.

### 4.1 Tecnologías y cadena de entrega

**T01 · Marco de interfaz.** La imagen identifica una tecnología de interfaz; el registro anterior selecciona React/React Native y TypeScript. Su propósito es implementar portales y aplicaciones con componentes de presentación coherentes. La interfaz usa APIs y telemetría del ámbito. El código web se ejecuta en el navegador y el móvil en el dispositivo; los archivos web necesitan un backend de publicación, propuesto en [FI04] como contenedores privados. El nombre y las versiones definitivas deben coincidir con los siete canales. Fundamento de diseño en [FI01], sección 4, y alojamiento en [FI05].

**T02 · Azure DNS.** Resuelve los nombres públicos de acceso a los canales y se relaciona con sus entradas de borde. La resolución privada exige zonas y resolución corporativa propias, detalladas en la propuesta física. DNS justifica que el cliente encuentre el endpoint correcto; la petición de negocio no atraviesa DNS como si fuera un proxy. Se propone el servicio administrado Azure DNS y los mecanismos privados de cada ámbito. Fuente [FI01], 4.1, y [FI08], reglas de DNS.

**T03 · Azure API Center.** Conserva inventario, versiones y definiciones de APIs para evitar contratos dispersos. El pipeline utiliza esos contratos al publicar en APIM y verificar compatibilidad. Es gobierno lateral y no un salto entre APIM y los servicios. Se selecciona como servicio administrado, con catálogos separados por ámbito; región y permisos requieren cierre. La responsabilidad de inventario está documentada por Microsoft [FT01]; la selección y la transformación de OpenAPI están en [FI01], 4.2.

**T04 · Java 25 LTS.** Es la versión de ejecución declarada para APIs y trabajadores propios. Se integra con Spring Boot y bibliotecas de datos, identidad y telemetría dentro de sus procesos. Se ejecutaría en imágenes de contenedores sobre AKS. El rótulo es una selección de versión del proyecto; no acredita todavía compatibilidad de dependencias, distribución de JDK ni plazo de soporte. Fuente [FI01] y [FI05].

**T05 · Spring Boot 4.x.** Implementa contratos HTTP, lógica de aplicación y trabajadores Java. Su presencia busca mantener una base técnica común para piezas propias. Usa repositorios autorizados, bus e instrumentación según cada servicio y se ejecuta dentro de sus contenedores. Deben fijarse la versión exacta y las pruebas con el JDK, clientes Azure y componentes de seguridad. Fuente [FI01], tecnologías de servicios, y [FI05].

**T06 · Azure Kubernetes Service.** Aloja contenedores de negocio, integración y herramientas autogestionadas. El fundamento registrado es organizar réplicas, despliegues y aislamiento de cargas; AKS es una plataforma de ejecución, no un servicio funcional adicional. [FI04] propone clústeres privados Retail y Filial, más Frontera para X-01, con pools sobre VMSS. Microsoft administra el plano de control y los nodos ejecutan los pods [FT02]. SKU, LTS, versiones y capacidades quedan por demostrar para las regiones elegidas. Fuente [FI06].

**T07 · Terraform.** Aparece explícitamente en la nueva troncal. Su finalidad es describir infraestructura reproducible y revisar cambios de recursos mediante código. El recorrido propuesto es repositorio → agente de entrega → APIs de Azure, con estado y permisos segregados. Terraform se ejecuta en un agente o estación autorizada; no es un servidor que atienda ventas. Su función IaC está documentada en [FT03]. La elección de backend de estado, bloqueo, agentes, revisiones y recuperación se propone aquí para completar el dibujo y queda pendiente en `P04`.

**T08 · CI/CD, Azure Pipelines.** Automatiza compilación, pruebas y promoción de contratos y artefactos. Se conecta con el repositorio, API Center, registro de imágenes y destinos autorizados. Azure Pipelines aporta el servicio de orquestación [FT04]; los trabajos se ejecutan en agentes cuya ubicación y acceso a redes privadas deben definirse. [FI01], 4.2, y [FI09], D-46, ya reconocían una cadena de entrega. La imagen ahora la muestra en la vista lógica. Su configuración concreta no se deduce del rótulo.

**T09 · Container Registry Premium.** Guarda imágenes y artefactos de contenedores para que la construcción y la ejecución utilicen versiones identificables. El pipeline publica y AKS obtiene las imágenes aprobadas; el registro no ejecuta aplicaciones. Azure Container Registry es un servicio administrado [FT05]. El nivel Premium está visible en la imagen, pero faltan región, política de acceso, topología por ámbito, replicación, análisis y promoción por digest. Esas son decisiones de diseño por completar, no recursos ya creados.

**T10 · Azure Policy.** Gobierna la configuración permitida de los recursos Azure mediante políticas y evaluación [FT06]. Se relaciona con las suscripciones y despliegues de Terraform/pipeline; no recibe cada petición comercial ni reemplaza permisos de aplicación. Se propone utilizarlo para controles como ubicación o exposición, previa definición de iniciativas, efectos y excepciones. Es gobierno administrado de Azure y su alcance por ámbito queda abierto en `P04`.

### 4.2 Capacidades comunes por ámbito

El dibujo indica «Base tecnológica · Etapa 1 · una instancia por ámbito». [FI01], 5.1, especifica responsabilidades y [FI06] reserva ejecución en pools de negocio de cada ámbito, pero los productos y contratos no están cerrados. La explicación siguiente preserva la capacidad exigida sin seleccionar un motor o proveedor nuevo.

**C01 · Administración y parámetros.** Permite administrar usuarios, roles, unidades y reglas configurables, con versiones y aprobación. Las consolas llaman a APIs de administración y cada servicio aplica su configuración autorizada. Se propone ejecución en AKS BIZ y persistencia propia por ámbito. Evita cambios directos e informales en bases; su fundamento es RT-16.01–04. La simulación de RT-16.05 conserva su carácter deseable. Fuente [FI10], capítulo 16, y [FI01], 5.1.

**C02 · Flujos y tareas humanas.** Mantiene bandejas, estados, responsables, plazos y delegación para las intervenciones humanas. Los servicios solicitan o consultan tareas y ejecutan las decisiones de negocio bajo su propia autoridad. Se propone AKS BIZ con estado durable propio. La necesidad procede de RT-16.11–13; el motor de reglas de RT-16.14 es deseable. No se selecciona un producto de workflow ni se identifica esta bandeja con el coordinador automático de procesos. Fuentes [FI10], 16.3, y [FI01], 5.1.

**C03 · Documentos y firma.** Gestiona plantillas, versiones, metadatos, generación, acceso y relación con un prestador de firma cuando corresponda. Se conecta con servicios propietarios, almacenamiento documental, búsqueda y contraparte externa. Se propone backend por ámbito sobre AKS y Blob para objetos; F:C-03 mantiene la autoridad del expediente financiero. RT-16.15–19 justifica la capacidad; aplicabilidad y modalidad de firma deben validarse para cada acto. Producto, proveedor y límites frente a Evidencia siguen pendientes. Fuentes [FI02], [FI10] y [FI06].

**C04 · Notificaciones.** Procesa solicitudes de aviso con plantillas, preferencias, reintentos y control de entrega. Los servicios publican hechos o solicitudes autorizadas; la capacidad consume y contacta al proveedor correspondiente. Se propone ejecución por ámbito en AKS, con estado de entrega propio y conectividad externa restringida. Su fundamento es RT-16.20–25; los canales conversacionales de RT-16.26 son deseables. Proveedores, contratos, datos enviados y licencias siguen abiertos. Fuentes [FI01], 5.1, [FI10] y [FI06].

## 5. Capa 1, presentación

Los canales separan experiencias y perfiles, mientras las reglas y autoridades permanecen en servicios. Su justificación y cobertura de actores se recogen en [FI01], secciones 2 y 4. La correspondencia de alojamiento procede de [FI05]; esos alojamientos son propuestas físicas.

**PR01 · Portal y app de la tienda.** Permite consultar la oferta y utilizar funciones comerciales autorizadas. La ruta pública llega al borde Retail y continúa hacia las APIs; la app no accede a PostgreSQL. El navegador o teléfono ejecuta la interfaz y el frontend web privado sirve sus recursos. Debe conciliarse este canal propio con el e-commerce conservado, para que el dibujo no apruebe su sustitución.

**PR02 · Portal y app de la tarjeta.** Atiende al titular con identidad y permisos de Filial. Consume contratos financieros por el borde y gateway de Filial, sin utilizar el perfil comercial como autorización financiera. La app corre en el dispositivo y el frontend web se propone en el entorno Filial. Su separación evita que el canal Retail acceda a cartera o evidencia.

**PR03 · Caja y mesón.** Ejecuta la atención de venta y usa la entrada privada Retail durante la operación en línea. En pérdida de enlace utiliza las funciones locales descritas en B20 y D12. Se propone interfaz web servida en tienda sobre terminales POS y nodos locales. El mesón financiero de PR07 conserva otra sesión y custodia.

**PR04 · App móvil de tienda.** Atiende los perfiles internos de operación en terminales gestionadas. Usa servicios Retail mediante la red corporativa y conserva solo el estado local autorizado. El antecedente selecciona React Native, SQLite y DataWedge, sujeto a compatibilidad del equipo. Se ejecuta en dispositivos de tienda; Intune y la identidad del usuario gobiernan acceso y administración. La autonomía completa de cualquier función móvil requiere definición específica.

**PR05 · Vista logística.** Permite trabajar con las funciones del WMS conservado y con los contratos nuevos de abastecimiento/existencias. Se ejecuta en terminales del CD o puesto autorizado; los hosts del WMS permanecen en la infraestructura conservada por inventariar. El adaptador Comercio traduce su intercambio. El propósito es integrar la ejecución física con el estado central sin trasladar las tablas del WMS al núcleo.

**PR06 · Consola comercial y de atención.** Ofrece a perfiles comerciales funciones de oferta, clientes y posventa según permisos. Usa la ruta privada Retail y APIs de sus servicios. Se propone navegador en PC/terminal y backend web privado Retail. Cada consulta sensible y cada cambio debe mantener su propia trazabilidad; la consola no obtiene privilegios por agrupar funciones.

**PR07 · Mesón financiero.** Atiende solicitudes y consultas de la Filial con sesión financiera y rutas propias. Invoca Originación, Cartera o Evidencia mediante el gateway financiero y no utiliza el diario de venta Retail. Se ejecuta en un puesto de la red Filial; su frontend se propone en el entorno Filial. La atención en una misma tienda no fusiona las autoridades de los dos negocios.

## 6. Capas 2 y 3, acceso a servicios

La separación entre borde, enrutamiento y gobierno de API permite asignar controles a cada salto. Los recorridos de [FI01], 4.1–4.2, y [FI04], 3.1–3.3, explican las decisiones; [FT07] documenta el uso conjunto de Application Gateway y APIM, sin certificar esta topología particular.

**E01 · Azure Front Door Premium.** Es la entrada pública seleccionada, con WAF y perfiles/hosts propios por negocio en el registro anterior. Se conecta al origen privado mediante Private Link. Es un servicio de borde global, no una VM de Chile Central. La región del origen y el tránsito de su conexión privada deben declararse por separado. [FT08] documenta Private Link de Front Door; la residencia y la configuración concreta siguen abiertas.

**E02 · Private Link.** Representa conectividad privada al origen y, en la física, endpoints de recursos. Se justifica para limitar exposición de backends. No constituye un túnel entre Retail y Filial ni un servicio que interprete el contrato de compra. Su ubicación y DNS dependen del recurso y del tipo de enlace. La propuesta anterior registra tránsito Front Door por Brazil South hacia Chile como asunto por aprobar; no se incorpora aquí como garantía de residencia. Fuentes [FI04], sección 5, [FI08] y [FT08].

**E03 · Acceso privado corporativo.** Agrupa VPN/SD-WAN y la propuesta ExpressRoute para los sitios que lo requieran. Conecta terminales y redes autorizadas con los gateways del ámbito. Se distribuye entre equipos locales, enlaces y gateways Azure. Justifica el acceso interno y la operación híbrida; no significa un ExpressRoute por tienda ni reemplaza el aislamiento financiero. Fuentes [FI01], 4.1, y [FI08].

**G01 · Application Gateway v2.** Recibe el tráfico de su ámbito, distingue rutas web y API y lo dirige al backend autorizado. La ruta API continúa a APIM; el contenido web puede ir al frontend privado. Se propone en una subred dedicada de cada VNet. Su función de enrutamiento de entrada evita publicar directamente los pods. El TLS, listener, prueba de salud y restricciones del origen se verifican por salto. Fuentes [FI04], 3.1, [FI08] y [FT07].

**G02 · API Management Premium.** Publica contratos de API y aplica políticas de entrada como validación, autenticación y límites definidos. Invoca backends privados del ámbito; el servicio conserva la autorización de negocio. Se propone APIM interno propio por ámbito, con acceso al Service/VIP interno de AKS mediante un balanceador interno. El catálogo API Center administra contratos fuera de esta ruta. Nivel exacto, compatibilidad OpenAPI y dependencias de red requieren prueba. Fuentes [FI01], 4.2, [FI04] y [FI08].

## 7. Capa 4, servicios y capacidades de negocio

El catálogo de referencia conserva nueve servicios Retail, tres de Filial y X-01. La imagen añade una tarjeta regulatoria sujeta a validación, cinco innovaciones y la operación sin enlace. Sus fuentes principales son [FI01], 5–5.2, [FI09], D-19–D-34, y [FI06]. Los párrafos siguientes explican autoridad y conexiones; una dependencia funcional no se presenta como una flecha individual ya comprobada en el PNG.

### 7.1 Mercadería

**B01 · R:M-01, Oferta comercial, E1.** Posee artículos, precios, promociones y publicaciones. Los canales consultan su contrato y sus hechos alimentan integración, precios publicados, caché y búsqueda de catálogo. Se propone ejecución en AKS BIZ Retail con repositorio lógico/rol propio en el servidor de área `pg-r-merc`. La razón es mantener una versión de oferta atribuible al propietario; Existencias conserva la autoridad sobre reservas y disponible. La partición final como microservicio o módulo requiere conciliación con el rótulo del nuevo diagrama.

**B02 · R:M-02, Abastecimiento, E2.** Gestiona órdenes, transferencias y recepción. Intercambia contratos con Existencias y con ERP/WMS a través de Comercio. Se propone AKS BIZ Retail, con datos propios en el área Mercadería. Existe para coordinar aprovisionamiento y recepción sin reemplazar por una tarjeta la ejecución física del WMS. Deben precisarse confirmaciones, discrepancias y compensaciones de cada interfaz.

**B03 · R:M-03, Existencias, E1.** Es autoridad de movimientos, reservas, disponible, conteos y ajustes aprobados. Recibe operaciones autorizadas de venta/pedido y hechos de recepción; publica resultados confirmados para proyecciones. Se propone AKS BIZ Retail y persistencia propia en Mercadería. Su razón es impedir que cachés, canales o analítica decidan stock por su cuenta. Las recomendaciones de conteo requieren decisión humana antes de modificar existencias.

**B04 · Conteo cíclico predictivo.** Es la innovación de proceso bajo Existencias. Usa históricos autorizados y conjuntos versionados, ejecuta entrenamiento/evaluación en Python/scikit-learn y registra resultados en MLflow. Se propone un pool batch Retail y una integración de recomendaciones con Existencias. Su justificación es priorizar el conteo con evidencia; no modifica inventario automáticamente. RT-18 fija obligaciones de gobierno de IA, pero no impone esta herramienta ni un algoritmo. Fuentes [FI02], secciones 3 y 5, y [FI06].

**B05 · Búsqueda vectorial multimodal.** Es la innovación tecnológica de Oferta. Un trabajador produce representaciones de catálogo/imágenes y guarda un índice derivado en pgvector; la consulta devuelve candidatos y confirma información comercial con sus propietarios. Se propone procesamiento Retail y un PostgreSQL vectorial aislado. La razón es habilitar búsqueda por similitud sin convertir el índice en la autoridad de precio o stock. Modelo, versiones y ubicación del procesamiento de representaciones siguen pendientes. Fuente [FI02], 5.

**B06 · Retail Media Network.** Es la innovación de modelo de negocio bajo Oferta. Integra campañas y publicidad contextual mediante adaptadores y una plataforma externa por precisar. Se propone lógica propia en Retail y conectividad de integración en su pool INT; la contraparte conserva su hosting. Su incorporación no permite usar datos financieros para segmentación ni condicionar la venta a la disponibilidad publicitaria. Fuente [FI01], 5.2.

### 7.2 Venta

**B07 · R:V-01, Pedidos, E2.** Posee promesa, asignación y estado del pedido. Coordina contratos con Existencias y plataformas de cumplimiento a través de integración; recibe confirmaciones de retiro o entrega. Se propone AKS BIZ Retail y repositorio propio del área Venta. Se incorpora para mantener un estado reconocible del cumplimiento. El cierre requiere detallar los procesos largos, fallos y compensaciones; el bus no sustituye su autoridad.

**B08 · R:V-02, Ventas, E1.** Posee la venta, pago, reversa y conciliación. Invoca capacidades autorizadas de oferta/existencias, conecta con medios de pago mediante Socios y utiliza X-01 para la compra con tarjeta propia. Se propone AKS BIZ Retail y repositorio propio de Venta, con operación local de contingencia. ERP/DTE conserva la emisión tributaria según [FI01]; el servicio de Ventas no se convierte por omisión en un reemplazo de ese sistema.

**B09 · R:V-03, Comisiones, E2.** Define reglas y base de atribución comercial utilizando operaciones confirmadas y parámetros versionados. Se propone módulo extraíble en el entorno BIZ Retail con datos de su autoridad en Venta. Su propósito es calcular atribuciones sin atribuirle la gestión de remuneraciones. Debe cerrarse el contrato de datos y la política de recálculo o reversa antes de fijar su independencia de despliegue.

**B10 · R:V-04, Marketplace, E2.** Coordina reglas de vendedores e intercambio con la plataforma marketplace conservada mediante el adaptador Canales. Se propone módulo extraíble en AKS Retail con datos propios de Venta. Existe para gobernar ese intercambio y conservar autoridades, sin asumir que el software externo se reemplaza o se aloja en nuestro clúster.

**B11 · Lockers Ancoa 24/7.** Es la innovación de producto bajo Pedidos. El contrato de retiro relaciona pedido, credencial, controlador y confirmación. La lógica central se propone en Retail y el controlador, cerraduras y sensores en la tienda o instalación autorizada, dentro del segmento IoT. El proveedor, la interfaz, la contingencia y el suministro requieren definición. Un rótulo 24/7 no demuestra disponibilidad ni autonomía durante un corte. Fuentes [FI01], 5.2, y [FI04], 3.5.

**B20 · Operación sin enlace.** Apoya la venta y consulta de oferta autorizada durante el horizonte de continuidad de RT-03.10. El terminal registra de forma durable en el nodo local y la sincronización reconcilia al retornar la conectividad. Se propone el par local Retail `SIT-xx-R-01/02`; la selección de líder, fencing y almacenamiento requieren prueba. La aplicación del cupo financiero sigue otra custodia y no permite originar o ampliar crédito sin enlace. Fuentes [FI01], continuidad, y [FI04], 3.2.

### 7.3 Relación con el cliente

**B12 · R:CL-01, Posventa, E2.** Posee el caso, inspección y destino de una devolución. Coordina con Venta/Existencias los efectos que cada propietario debe ejecutar. Se propone AKS BIZ Retail y datos propios en el área Clientes. Su presencia evita resolver una devolución como una modificación informal del stock o del cobro; el contrato de reversa debe conservar el vínculo con la operación original.

**B13 · R:CL-02, Clientes Retail, E2.** Mantiene identificación, preferencias y relación comercial. Usa el proveedor de identidad como soporte de acceso y contratos con la fidelización conservada cuando corresponda. Se propone AKS BIZ Retail y repositorio comercial propio. No incorpora cartera, mora o comportamiento de pago de Filial; esa separación es una condición del diseño registrado en [FI01] y [FI02].

**B14 · Modo Tienda y fila virtual.** Es la innovación de experiencia bajo Clientes Retail. Relaciona al cliente con atención en tienda, estado de fila y notificaciones autorizadas. Se propone backend Retail y clientes/tótem locales. El estado mínimo de contingencia y la atención asistida deben definirse por dispositivo y función. La autonomía de venta no demuestra por sí sola autonomía completa de la fila. Fuentes [FI01], 5.2, y [FI04], 3.5.

### 7.4 Crédito y frontera

**B15 · F:C-01, Originación de crédito, E1.** Posee solicitud, evaluación, cupo y autorización según el reparto registrado. Recibe solicitudes de los canales financieros y la compra mínima mediada por X-01; coordina con Cartera y Evidencia bajo contratos de Filial. Se propone AKS BIZ Filial y `pg-f-originacion`. La asignación exacta de reserva/consumo de cupo respecto de Cartera debe cerrarse para evitar autoridades incompatibles. Fuente [FI02], 4.1.

**B16 · F:C-02, Cartera de crédito, E1/E2.** Posee cuenta, saldo, pagos, mora, cobranza y repactación. Se integra con Originación, evidencia y el sistema financiero de convivencia mediante contratos de Filial. Se propone AKS BIZ Filial y `pg-f-cartera`. Sus datos no se exponen al bus ni al repositorio de Retail; las conciliaciones y la migración por etapas requieren detalle. Fuentes [FI01], 5, y [FI06].

**B17 · F:C-03, Evidencia financiera, E1.** Conserva precontrato, aceptación, firma y expediente. Coordina la generación/firma con C03 y verifica archivos en Blob, manteniendo metadatos e integridad bajo su autoridad. Se propone AKS BIZ Filial, `pg-f-evidencia` y Blob propio. Su razón es poder reconstruir y comprobar la operación aceptada. Un objeto subido no acredita por sí solo expediente completo ni firma válida. Fuente [FI02], 4.1.

**B18 · F:C-04, Control regulatorio.** La tarjeta nueva sigue indicando propuesta por validar. Agrupa una posible responsabilidad de reportes y prevención, cuya necesidad funcional debe conciliarse con las autoridades existentes. No tiene contratos operacionales, etapa ni despliegue aprobado en los registros. Su futura ubicación sería del ámbito Filial si se aprueba, pero esta nota no asigna pod, base ni servidor. Su presencia no eleva automáticamente el catálogo a catorce servicios. Fuentes [FI01], 5, y [FI06].

**B19 · X-01, Control de cruces, E1.** Media las finalidades autorizadas entre Retail y Filial, verifica el conjunto mínimo de campos y registra decisión y política. El recorrido de compra documentado es Ventas → X-01 → entrada financiera/APIM → Originación. Se propone ejecución aislada de Frontera y `pg-x01`. Evita una ruta libre de Retail a datos financieros. Una nueva finalidad, reversa o conciliación necesita su ficha de cruce; no queda autorizada por la existencia de la flecha. Fuentes [FI01], 4.2, [FI02], 4.2, y [FI04], 3.3.

### 7.5 Atributos presentes en todos los servicios

El subtítulo de la imagen indica auditoría, control de acceso, exportación y parámetros para los servicios de capa 4. Son responsabilidades A/C/E/P, no cuatro ejecutables adicionales por cada tarjeta. Cada servicio aplica permisos sobre sus operaciones y datos; registra acciones y consultas sensibles cuando corresponde; exporta con autorización, filtros y corte; y consume parámetros versionados bajo aprobación. APIM, C01 y el archivo WORM apoyan esas responsabilidades, pero no las completan automáticamente.

La trazabilidad general comprende RT-16.01–10 y RT-16.28–30. Sus pruebas y brechas están recogidas en [FI11]. Esta declaración no marca cumplimiento en T-12 ni determina que todo parámetro sea configurable sin desarrollo.

## 8. Capa 5, integración y eventos

Los componentes de esta columna desacoplan contratos externos y procesamiento diferido. La separación por ámbito responde a [FI09], D-29–D-34. Los detalles de persistencia, idempotencia y reconstrucción están en [FI02], 4.3 y 5. El servicio Azure Service Bus proporciona mensajería con colas y temas/suscripciones [FT09]; los consumidores siguen siendo responsables de sus efectos de negocio.

**I01 · Service Bus Premium, Retail.** Transporta mensajes autorizados de Retail hacia sus consumidores. El productor confirma operación y outbox, publica posteriormente y el consumidor confirma el mensaje después de persistir su efecto. Se propone namespace y acceso privado Retail administrado por Azure. Justifica reintentos y desacoplamiento sin utilizarlo como base de datos histórica ni como puente hacia Filial.

**I02 · Adaptador Comercio.** Traduce contratos con ERP/DTE y WMS conservados. Consume o solicita operaciones según el modo que se acuerde para cada interfaz; valida y reconcilia sus resultados. Se propone AKS INT Retail. Su razón es aislar modelos y fallas externos conforme a RT-05.20; todavía se deben registrar ventanas, volúmenes y comportamiento de cada contrato.

**I03 · Adaptador Canales.** Aísla e-commerce, marketplace y fidelización conservados. Se conecta con sus APIs o intercambio acordado y con los contratos/eventos Retail. Se propone AKS INT Retail. Evita que formatos o cambios del proveedor se propaguen a todos los servicios; la plataforma conservada continúa fuera de este despliegue.

**I04 · Adaptador Socios.** Integra medios de pago, proveedores y transportistas mediante contratos autorizados. Su alojamiento propuesto es AKS INT Retail y utiliza identidad, reintentos y trazabilidad por contraparte. El agrupamiento visual no acredita una única interfaz común para todos los socios ni define el proveedor de lockers o publicidad.

**I05 · Java/Spring en AKS, Retail.** Representa trabajadores de ingesta, validación, proyección, conciliación y exportación. Consumen mensajes o trabajos de su ámbito y escriben destinos derivados autorizados. Se propone pool INT Retail con estado durable. Existen para que los servicios propietarios no asuman todos los procesos de fondo y para recuperar trabajos tras una falla.

**I06 · Sincronizador de operaciones.** Reconcilia el diario local con los servicios centrales después de la pérdida de enlace. Los agentes locales conservan estado y reintentos en tienda; el receptor central se propone en integración Retail. Debe tratar duplicados, orden, confirmaciones y conflictos antes de dar una operación por conciliada. La tarjeta no decide por sí sola qué parte reside en el nodo local y cuál en Azure. Fuentes [FI04], 3.2, y [FI05].

**I07 · Service Bus Premium, Filial.** Transporta hechos y solicitudes financieras dentro de su ámbito. Usa namespace, identidades, colas/temas y almacenamiento operativo separados del Retail. Se propone servicio administrado Azure con acceso privado financiero. Los cruces ingresan por X-01 y contratos de aplicación autorizados; no se establece un enlace entre buses.

**I08 · Java/Spring en AKS, Filial.** Ejecuta ingesta, proyecciones y conciliación financiera utilizando contratos y destinos autorizados. Se propone pool INT Filial con permisos propios. Mantiene el procesamiento financiero independiente de los workers comerciales y conserva su trazabilidad y recuperación.

**I09 · Adaptador Crédito.** Aísla el sistema Crédito 2011, reportes y firma financiera según los contratos finalmente definidos. Se propone AKS INT Filial; los sistemas externos conservan sus hosts. Deben resolverse confirmaciones, corte/migración y custodia de cada intercambio. Una familia de adaptador no acredita las catorce interfaces completas del proyecto. Fuentes [FI09], D-30, y [FI11].

## 9. Capa 6, datos

Los grupos separan datos operacionales, recursos derivados/locales y procesamiento analítico. El fundamento registrado está en [FI02] y el alojamiento propuesto en [FI05] y [FI06]. RT-05.01–10 exige definir modelos, autoridad, persistencia, calidad y separación operacional/analítica. El dibujo por áreas no asigna escritura compartida entre servicios ni una transacción distribuida.

### 9.1 Datos operacionales por área

**D01 · PostgreSQL Mercadería.** Agrupa repositorios de Oferta, Abastecimiento y Existencias. Cada propietario conserva bases/esquemas y roles delimitados. Se propone PostgreSQL administrado `pg-r-merc` con acceso privado; la partición física final requiere carga, aislamiento y recuperación. Su justificación es persistencia transaccional bajo autoridad reconocible.

**D02 · PostgreSQL Venta.** Aloja los datos propios de Pedidos, Ventas, Comisiones y Marketplace en la propuesta `pg-r-venta`. Los servicios escriben mediante sus credenciales; otros consumen contratos autorizados. Se propone recurso administrado Retail. Agruparlos por área mejora la lectura de la figura, pero no permite consultar o actualizar tablas ajenas.

**D03 · PostgreSQL Clientes.** Representa datos comerciales de Clientes y Posventa. Se propone `pg-r-clientes`, administrado y con roles por autoridad. La separación respecto de Crédito preserva las finalidades comerciales y evita formar un perfil financiero compartido.

**D04 · PostgreSQL, bitácora de X-01.** Conserva finalidad, referencia, política y resultado mínimo del intercambio. Se propone `pg-x01`, recurso propio de Frontera con acceso acotado a X-01 y administración por definir. Existe para acreditar el cruce autorizado y no para resolver una equivalencia general cliente–titular.

**D05 · PostgreSQL Crédito.** Es la agrupación visual de las autoridades financieras. [FI06] propone recursos separados para Originación, Cartera y metadatos de Evidencia. Se trata de servidores administrados, no VM de bases instaladas dentro de AKS. El dimensionamiento y la partición final siguen abiertos; el círculo único del antecedente y la tarjeta nueva no fusionan tablas ni custodios.

**D06 · Blob Storage, evidencia vigente.** Guarda objetos del expediente financiero con metadatos/integridad bajo F:C-03. Se propone almacenamiento Azure propio de Filial mediante endpoint privado. Justifica conservar documentos verificables sin cargar sus binarios en la base transaccional. Debe existir conciliación entre registro y objeto, y distinguirse evidencia vigente de archivo inmutable y respaldo.

### 9.2 Caché, búsqueda, archivo y nodo local

**D07 · Azure Managed Redis, oferta.** Conserva una caché reconstruible para acelerar lecturas Retail. La actualizan componentes autorizados y el contrato debe definir frescura e invalidación. Se propone Redis administrado Retail con acceso privado, nivel/región por verificar. No confirma reservas ni constituye el stock oficial. Fuente [FI02], selección y autoridades.

**D08 · PostgreSQL, precios publicados.** Conserva el historial/versiones de publicación bajo Oferta para reconstruir qué oferta se aplicó. La propuesta física lo sitúa bajo Mercadería con permisos propios; no decide un servidor adicional por tarjeta. Consumidores autorizados consultan el contrato correspondiente, sin modificar el historial. Fuente [FI09], D-38, precisada por [FI02].

**D09 · PostgreSQL y pgvector, oferta multimodal.** Guarda representaciones e índice derivado del catálogo. Los workers de representaciones escriben y Oferta consulta candidatos. Se propone `pg-r-vector` aislado de la carga transaccional. Su propósito es búsqueda por similitud; reconstrucción, modelo y consistencia con catálogo requieren definición. Fuente [FI02], 5.

**D10 · OpenSearch, búsqueda global.** Indexa texto y metadatos autorizados para búsqueda global con filtros y permisos. Lo alimentan proyectores propios y lo consulta una API de búsqueda autorizada. Se propone autogestionado en AKS STATE por ámbito, con persistencia y recuperación. Se selecciona por la capacidad de RT-16.27 y la búsqueda documental de RT-16.15; se debe justificar su operación autogestionada bajo RT-03.05. Es distinto de pgvector y del backend de catálogo. Fuente [FI02].

**D11 · Blob WORM, archivo y evidencia inalterable.** Recibe copias verificadas de auditoría y evidencia conforme a políticas por clase. Se propone almacenamiento propio por ámbito, separado de la evidencia en curso y de temporales. Su razón es custodia e inalterabilidad; la protección depende de políticas, bloqueo, claves y pruebas, no del texto WORM en la tarjeta. Fuente [FI03], auditoría/archivo, y RT-16.07.

**D12 · Diario local.** Conserva de forma durable las operaciones de venta en tienda para confirmar y reconciliar durante cortes. Se propone almacenamiento en el par Retail local, con réplica y exclusión de doble primario por probar. Se relaciona con Caja, B20 e I06. Su ubicación es on-premise; moverlo únicamente a Azure anularía su finalidad de continuidad. Fuentes [FI04] y [FI05].

**D13 · Cupo preautorizado.** Conserva la referencia y el consumo mínimo autorizado por Filial para el escenario sin enlace. Se propone custodia financiera local aislada en hardware o VM aprobada, con red y claves propias. Se relaciona con contratos de Filial y el cruce autorizado, sin dar acceso a la cartera completa. Caducidad, doble gasto, exclusividad y conciliación son pendientes críticos. Fuentes [FI09], D-44, [FI02] y [FI05].

### 9.3 Analítica, modelos y respaldo

**D14 · Azure Data Factory.** Coordina cargas, cortes y dependencias. Sus pipelines llaman fuentes/trabajos autorizados y los runtimes ejecutan actividades de movimiento/procesamiento. Se propone factory por ámbito y SHIR dedicados en VM Windows para conectividad privada. La región del servicio y la ejecución del runtime se documentan por separado. Su razón es orquestar cargas verificables, no reemplazar las reglas de todos los workers. Fuentes [FI02], 5, y [FI04], 3.4.

**D15 · ADLS Gen2.** Conserva datos de origen autorizados, históricos y conjuntos depurados/versionados para reconstrucción y entrenamiento. Se conecta con cargas, workers y destinos analíticos. Se proponen cuentas y permisos por ámbito. La decisión posterior de Datos restituye el lago que un dibujo anterior retiraba. La selección no habilita mezclar ambos negocios ni conservar todo indefinidamente. Fuente [FI02], 2 y 5.

**D16 · PostgreSQL analítico.** Mantiene hechos, dimensiones y agregados para consulta. Workers y procesos de carga lo alimentan con corte y linaje; Power BI lo consulta con permisos de lectura. Se proponen `pg-r-mart` y `pg-f-mart`, separados de operación. La razón es cumplir RT-05.05 y sostener los indicadores sin degradar reservas, cobros o crédito. Fuente [FI02], 3 y 5.

**D17 · Microsoft Power BI.** Presenta tableros, filtros y autoservicio sobre modelos semánticos. Se propone SaaS con gateway de datos en VM propias por ámbito para consultar el PostgreSQL analítico privado. El gateway no es otro gateway de APIs. Licencias, residencia, conectores y permisos requieren verificación. Su justificación funcional es RT-05.25–29; el producto es elección de OSS. Fuentes [FI02] y [FI04], 3.4.

**D18 · MLflow.** Registra experimentos, métricas, artefactos y versiones del conteo predictivo. Los Jobs de entrenamiento publican resultados y la promoción necesita revisión humana. Se propone autogestionado en AKS STATE Retail con base técnica y Blob de artefactos propios. No se incorpora un MLflow financiero sin necesidad definida. La función de gestión del ciclo de modelos está documentada en [FT10]; su adopción aquí procede de [FI02].

**D19 · Python y scikit-learn.** Ejecutan preparación, entrenamiento, evaluación y predicción del conteo bajo Existencias. Usan conjuntos autorizados/versionados y registran resultados en MLflow. Se proponen Jobs en un pool batch elástico Retail. Su presencia concreta esa innovación, pero no selecciona el modelo multimodal ni demuestra calidad predictiva. Variables, métrica, línea base, deriva y alternativa manual deben cumplir RT-18. Fuente [FI02], 5.

**D20 · OpenMetadata.** Reúne propietarios, diccionario, clasificación, calidad y linaje. Pipelines, conectores y trabajadores publican metadatos mediante sus mecanismos autorizados; los usuarios consultan el catálogo del ámbito. Se propone autogestionado en AKS STATE, con repositorio e índice técnico compatibles separados de negocio. El fundamento incluye RT-05.01 y la adopción del deseable RT-05.10. [FT11] documenta el modelo de metadatos; la selección y las dependencias del proyecto están en [FI02].

**D21 · Azure Backup y PITR.** Representa recuperación por recurso. PostgreSQL, volúmenes, Blob, claves y aplicaciones necesitan políticas y mecanismos compatibles propios. Se proponen copias y destinos autorizados, con pruebas de restauración integral. No es una garantía de cobertura automática de todos los iconos, ni sustituye alta disponibilidad, réplica o archivo WORM. Fuente [FI02], respaldo, y [FI04], recuperación.

## 10. Sistemas externos

Las tarjetas externas identifican plataformas conservadas o contrapartes; no son recursos que se desplieguen automáticamente en AKS. La familia de conexión turquesa remite al adaptador autorizado. [FI01], 9, [FI05] y [FI09], D-30, mantienen abiertos inventario, ubicación real y contratos particulares.

**X01 · ERP/DTE y WMS conservados.** Intercambian operaciones con Comercio. El ERP/DTE conserva responsabilidades contables/tributarias y el WMS la ejecución logística definida. La propuesta física los ubica en hosts corporativos DC/CD por inventariar. Preservarlos obliga a especificar conectividad, ventanas y conciliación en lugar de asumir una migración completa.

**X02 · E-commerce, marketplace y fidelización.** Intercambian catálogo, estados o funciones autorizadas con Canales. Permanecen en plataformas de terceros o infraestructura conservada cuya ubicación exacta no se acredita. Los nuevos servicios gobiernan sus propios datos y contratos sin adjudicarse el hosting o la sustitución de esas plataformas.

**X03 · Pagos, proveedores y transportistas.** Se relacionan con Socios y con los propietarios de la operación. Se conservan como contrapartes externas con ventanas, formatos y tratamiento de indisponibilidad propios. Deben agregarse las fichas de lockers y publicidad cuando se cierren; la tarjeta no identifica proveedores ni contratos de esos dos casos.

**X04 · Prestador de firma y mensajería.** Proporciona servicios externos utilizados por Documentos/firma y Notificaciones según ámbito. Su hosting es del proveedor aún por seleccionar y debe declarar procesamiento, residencia y subcontrataciones. Se requieren credenciales y contratos separados; un proveedor común no permite mezclar contenido o identidad de los dos negocios.

**X05 · Crédito 2011 conservado.** Mantiene convivencia con los servicios financieros nuevos mediante el adaptador Crédito. Sus hosts, OS, alcance de custodia y plan de transición deben inventariarse. La documentación anterior no permite fijar un alojamiento definitivo de ese sistema ni inferir que Cartera lo apaga en el primer despliegue.

## 11. Capa 7, seguridad transversal

Las doce tarjetas representan controles diferentes y conservan recursos/permisos separados por ámbito. El registro de referencia es [FI03], especialmente secciones 2, 5 y 7–10; [FI04] y [FI06] proponen la infraestructura que algunas necesitan. Los capítulos 11 y 12 de [FI10] justifican capacidades de seguridad e identidad. Seleccionar una herramienta no constituye evidencia de cumplimiento.

**S01 · Microsoft Entra ID P2.** Atiende identidad del personal, emisión de credenciales y políticas de acceso. Los canales y servicios integran su autenticación y validan permisos en el receptor. Es un servicio de identidad Microsoft; el tenant propio de Filial está seleccionado en las notas, pero la confirmación específica D-40 sigue abierta. La separación no puede deducirse solo de los puntos de color.

**S02 · Entra External ID.** Resuelve identidad externa de compradores y titulares. Se conecta con los canales respectivos y las aplicaciones registradas de cada negocio. Es un servicio de identidad externo al clúster; se propone separación por negocio. No constituye el maestro de clientes comerciales ni de cuentas de crédito.

**S03 · Entra PIM.** Controla elevación temporal, aprobaciones y registro de privilegios administrativos. Se relaciona con identidades y roles de recursos/operación. Su alojamiento es el servicio Microsoft de gestión de identidad. Justifica limitar privilegios permanentes; la sesión administrativa sigue otro recorrido.

**S04 · Azure Bastion Premium.** Proporciona acceso administrativo a VM autorizadas mediante la red de administración. Se propone recurso por ámbito en su subred dedicada. La grabación solo aplica a recorridos/clientes compatibles y necesita almacenamiento temporal y copia posterior cuando corresponda. No se promete grabación universal por mostrar el nivel Premium.

**S05 · Entra Private Access.** Permite acceso remoto a recursos privados autorizados. Sus conectores propuestos `R/F-PA-01/02` son VM Windows propias, con canales salientes al servicio. No sustituye VPN/SD-WAN entre tiendas y nube. La integración concreta con Bastion, DNS y cliente sigue sujeta a prueba de concepto.

**S06 · Microsoft Intune.** Administra dispositivos y aplicaciones compatibles, incluyendo configuración, cumplimiento, bloqueo y borrado. Es un servicio SaaS con gestión aplicada a equipos de tienda y otros endpoints autorizados. Su razón es gobernar terminales compartidas y remotas; cada modelo/OS necesita comprobar funciones soportadas.

**S07 · Workload Identity.** Proporciona identidad federada a cargas AKS para solicitar acceso autorizado a servicios Azure, evitando distribuir secretos permanentes. Se relaciona con cuentas de servicio, federación y recursos receptores; no añade una VM. [FT12] documenta ese mecanismo; la segregación por carga y ámbito deriva de [FI03]. Identidades de pipelines y de equipos requieren su configuración correspondiente.

**S08 · Azure Key Vault.** Custodia secretos y certificados utilizados por cargas y procesos autorizados. Se propone servicio Azure y acceso privado/roles propios por ámbito. Su función es reducir exposición y permitir rotación; el acceso a un secreto no concede permisos generales sobre los datos del servicio.

**S09 · Azure Managed HSM.** Custodia las claves criptográficas seleccionadas para proteger claves de datos y cifrado de campo. Se propone recurso de claves propio por ámbito, con responsables y recuperación definidos. Su razón es separar la custodia criptográfica de la aplicación; el cifrado de campo se implementa en el lugar declarado y no por dibujar el HSM junto a PostgreSQL.

**S10 · Defender for Endpoint.** Protege equipos compatibles y genera señales de seguridad. Los agentes y controles se aplican a endpoints autorizados y se integran con la operación de seguridad. Combina servicio Microsoft y componentes en el equipo. Cobertura, exclusiones y licencias deben declararse por tipo de dispositivo.

**S11 · Defender for Cloud.** Evalúa postura y ofrece protecciones según los planes habilitados para recursos, servidores y contenedores. Es un servicio Azure relacionado con inventario y señales de los entornos. La justificación es detectar configuraciones y amenazas de plataforma; su nombre no acredita que todos los planes estén contratados o configurados.

**S12 · Microsoft Sentinel.** Correlaciona e investiga señales de seguridad mediante conectores y espacios propios por ámbito. Se propone servicio Azure con custodia financiera separada y una eventual vista agregada autorizada para el SOC. No debe confundirse con el repositorio de logs operacionales de Loki ni con la dotación humana de atención 24×7.

La auditoría de negocio conserva quién, qué, cuándo y resultado, con datos anteriores/posteriores cuando corresponda y consultas sensibles registradas. Su custodia WORM se trata en D11. Las trazas operacionales deben sanear datos sensibles y no sustituyen ese registro. QR+PIN del antecedente no se utiliza como prueba general de MFA; [FI03] exige distinguir métodos y operaciones que necesitan otro nivel de autenticación.

## 12. Capa 8, observabilidad transversal

El diseño separa transporte de señales, almacenamiento, consulta y prueba activa. La selección posterior de [FI03] reemplaza el recorrido genérico de aplicaciones hacia Azure Monitor por destinos específicos. RT-03.16 y el capítulo 14 de [FI10] sustentan integración de nube/sitios y observabilidad. La operación y almacenamiento autogestionados requieren justificación conforme a RT-03.05.

**O01 · OpenTelemetry Collector.** Recibe, procesa y exporta señales de aplicaciones, workers y agentes [FT13]. Se proponen colectores por ámbito/clúster y agentes locales con cola durable en tienda. Registros van a Loki, trazas a Tempo y métricas a Prometheus por interfaces/versiones compatibles. Su propósito es uniformar instrumentación y saneamiento; requiere capacidad, persistencia y comportamiento ante caída del destino.

**O02 · Prometheus.** Almacena y consulta métricas [FT14]. Se relaciona con endpoints de métricas, colectores y sondas conforme a una configuración que evite duplicación de series. Se propone autogestionado en AKS OPS por ámbito con persistencia propia. Sus datos alimentan paneles y alertas; retención y alta disponibilidad deben dimensionarse.

**O03 · Grafana Loki.** Recibe y permite consultar registros operacionales [FT15]. Lo alimentan agentes/colectores autorizados y Grafana consulta sus resultados. Se propone autogestionado en AKS OPS con almacenamiento y permisos propios por ámbito. Su función es investigar eventos operacionales, preservando saneamiento, límites de etiquetas y retención; no es el archivo inalterable de auditoría.

**O04 · Grafana Tempo.** Conserva trazas distribuidas [FT16] emitidas por instrumentación y enviadas mediante colectores. Se propone AKS OPS y almacenamiento propio por ámbito. Permite seguir recorridos y dependencias; la correlación de un cruce usa una referencia controlada en X-01 sin unir libremente trazas financieras y comerciales.

**O05 · Grafana Alerting.** En la imagen representa consulta/alertamiento mediante Grafana y sus reglas. El registro selecciona Grafana autogestionado, con lectura de Prometheus, Loki, Tempo y Azure Monitor, agrupación y rutas de notificación. Se propone AKS OPS por ámbito. No se añade un Alertmanager independiente ni se atribuyen funciones de NOC a una herramienta sin turnos y runbooks. Fuente [FI03], 2.2.

**O06 · Blackbox Exporter.** Ejecuta sondas de disponibilidad y conectividad contra endpoints autorizados. Prometheus recoge los resultados; el verificador debe situarse fuera del mismo fallo que necesita detectar. Se proponen `R-SYN-01` y `F-SYN-01` independientes del AKS supervisado, con ubicación final aún abierta. La ausencia de latido no identifica por sí sola si falló la tienda, su enlace o el observador. Fuente [FI03] y [FI06].

**O07 · Azure Monitor y Log Analytics.** Conserva diagnóstico de recursos Azure y fuentes requeridas por seguridad/Sentinel según configuración. Es servicio administrado con espacios y accesos propios. Grafana puede consultar datos autorizados; la ruta base de logs y trazas de aplicaciones sigue Loki/Tempo. Su presencia evita perder las señales de plataforma, sin duplicar indiscriminadamente toda la telemetría. Fuente [FI03], 2.2.

## 13. Conexiones y recorridos que explican las flechas

Las relaciones se conservan como familias identificables `R01`–`R12`. Cada una tiene una fuente y un límite, de modo que una modificación posterior pueda comprobar si altera un contrato o solo su dibujo. Los inventarios [FI07] y [FI11] detallan relaciones anteriores; sus cantidades no se trasladan a este PNG porque no se recibió su modelo editable.

### R01. Solicitud pública y publicación web

Para una API, el recorrido documentado es canal público del ámbito → DNS para resolución → Front Door → conexión privada al origen → Application Gateway → APIM → Service/VIP interno de AKS → pod autorizado → repositorio propio. DNS interviene antes de establecer la conexión, no como salto de datos HTTP. En la física, APIM llega al Service mediante un balanceador interno; la respuesta utiliza la conexión correspondiente. El frontend web tiene su ruta desde Application Gateway al backend web, y sus llamadas funcionales usan las APIs. Fuentes [FI01], 4.1, y [FI04], 3.1.

La propuesta prevé HTTPS/TLS por salto. No se infiere que todos los tramos soporten una política idéntica o TLS 1.3 exclusivo sin verificar proxies, clientes y versiones. El enlace privado no reemplaza autenticación, autorización o validación del receptor.

### R02. Solicitud privada desde tienda o CD

El recorrido propuesto es terminal → VLAN/WLAN corporativa → firewall/contexto del ámbito → VPN/SD-WAN y gateway autorizado → red privada → Application Gateway → APIM → servicio. ExpressRoute se mantiene como propuesta específica para DC-01; no es el medio declarado para todas las tiendas. La red Filial tiene rutas e identidad propias. Fuente [FI04], 3.2, y [FI08].

### R03. Persistencia bajo autoridad

Cada servicio inicia una conexión TLS al endpoint de su repositorio con su rol autorizado. Una llamada a otro servicio utiliza su contrato; no consulta su base por conveniencia. Las líneas verdes de la vista reúnen persistencia propia por área, pero no habilitan a todas las tarjetas del área para escribir todas sus tablas. La propuesta de puertos identifica PostgreSQL TLS 5432 y HTTPS 443 para almacenamiento, sujetos a configuración y recurso. Fuentes [FI02], 4.1, y [FI08].

### R04. Publicación, consumo y recuperación

El servicio confirma su operación y outbox en una transacción local. Un publicador envía el hecho al Service Bus del ámbito. Adaptadores, workers y otras capacidades consumen solo contratos autorizados, deduplican y confirman después de persistir su efecto. En la red los clientes abren la conexión al broker; una flecha lógica bus→consumidor no implica una conexión entrante iniciada por el bus a un pod privado. Se propone AMQPS 5671 en [FI08], con alternativas soportadas por verificar.

La entrega repetida exige idempotencia, versiones por agregado, tratamiento de huecos y una cola de errores persistentes. El outbox resuelve la separación entre confirmar y publicar, pero no garantiza por sí solo entrega exactamente una vez a todos los terceros. La reconstrucción de índices y modelos requiere corte, deltas y conciliación. Fuentes [FI02], 4.3 y 5, [FI08] y [FT09].

### R05. Contrato externo

La relación turquesa identifica el intercambio entre un adaptador y su contraparte. Debe descomponerse en modo síncrono/asíncrono, autenticación, protocolo, volumen, ventana, timeout, reintento, deduplicación y reconciliación. La dirección de una flecha de información puede diferir del iniciador de la conexión de red. RT-05.16–23 y [FI11] justifican esas fichas. La vista no acredita por sí sola el inventario completo de interfaces.

### R06. Compra con tarjeta propia y cruce X-01

Ventas solicita el contrato mínimo de compra a X-01; X-01 valida finalidad/política, registra referencia y llega a la entrada financiera autorizada; APIM Filial dirige al contrato de Originación. La respuesta devuelve solo lo permitido para resolver esa operación. X-01 conserva su bitácora y los servicios financieros sus registros. No se habilitan consultas de cartera desde Retail ni conexiones entre sus buses.

El nuevo PNG sitúa conexiones rojas verticales entre la zona Clientes Retail, X-01 y la zona Crédito, sin identificar en texto cada contrato. Esa posición no basta para cambiar el origen registrado Ventas→X-01 ni para aprobar una relación cliente–titular. La conciliación de extremos y finalidad queda en `P03`. Fuentes [FI01], 4.2, [FI02], 4.2, y [FI04], 3.3.

### R07. Sin enlace y reconexión

Caja consulta oferta local autorizada y registra la operación durable en Retail. La custodia Filial aplica únicamente el cupo previo permitido y su control de consumo, sin abrir/ampliar crédito offline. Cuando retorna el enlace, el sincronizador reenvía operaciones identificadas y concilia con sus propietarios, detectando duplicados y conflictos antes de cerrar el lote. Reintentos y réplica local necesitan exclusión de doble primario y recuperación tras reinicio. Fuentes [FI04], 3.2, [FI05] y [FI08].

### R08. Analítica y consulta de gestión

Las fuentes autorizadas, el corte y los deltas alimentan conjuntos de recepción/depuración en ADLS mediante cargas y workers. PostgreSQL analítico mantiene modelos de consulta y Power BI consume su modelo semántico con permisos del ámbito. Data Factory coordina dependencias; los runtimes ejecutan las actividades configuradas. El gateway BI mantiene su canal de servicio saliente y consulta solo el repositorio analítico privado. La consulta no se dirige por defecto a bases operacionales. Fuentes [FI02], 5, y [FI04], 3.4.

Las flechas grises del dibujo son una síntesis de este procesamiento; no significan que todo dato atraviese obligatoriamente cada herramienta ni fijan la periodicidad. Deben especificarse latencia, corte, origen y conciliación por indicador antes de afirmar cumplimiento de RT-05.29.

### R09. Búsqueda, catálogo y modelos

Los proyectores mantienen OpenSearch con contenido/metadatos y permisos derivados de las fuentes. Un trabajador de representaciones alimenta pgvector; Oferta consulta candidatos y confirma los datos oficiales. Los pipelines publican propietario, transformación, destino y ejecución en OpenMetadata. El conteo utiliza ADLS, Jobs Python y MLflow para producir una recomendación dirigida a Existencias. No hay escritura automática de stock ni un modelo financiero implícito. Fuente [FI02], 4–5.

### R10. Documentos, avisos y exportación

El servicio propietario solicita generación/firma o aviso con identidad y datos mínimos. Documentos conserva la relación autorizada entre metadatos, objeto y prestador; Notificaciones mantiene preferencias, plantillas y resultado de entrega. Las exportaciones masivas se proponen como trabajos asíncronos con autorización, corte, manifiesto, archivo temporal y aviso. Exportar todo el Cliente requiere cubrir también datos/documentos fuera del mart analítico. Fuentes [FI01], 5.1, [FI02], 3, y RT-05.06/RT-16.28–30.

### R11. Seguridad, telemetría y administración

La identidad se valida en los receptores y las cargas obtienen acceso a secretos/claves según su permiso. Aplicaciones y agentes emiten señales saneadas al Collector propio; los backends almacenan por señal y Grafana consulta. Defender, Entra y las fuentes de plataforma aportan eventos por conectores a Sentinel. Las sesiones privilegiadas requieren elevación, acceso remoto compatible, Bastion y destino autorizado. Esas dependencias se aplican aunque no aparezca una línea desde cada banda a cada tarjeta. Fuente [FI03], conexiones de capas 7–8, y [FI08].

### R12. Construcción, gobierno y promoción

El recorrido que se propone para completar la nueva troncal es cambio revisado en repositorio → pipeline → construcción y pruebas → imagen identificada en ACR → promoción autorizada a AKS. Los contratos publicados alimentan API Center y APIM mediante el paso de entrega correspondiente. Terraform planifica/aplica infraestructura con identidad acotada y Azure Policy evalúa las reglas del alcance. La aplicación en producción utiliza artefactos aprobados y mantiene reversión.

Este recorrido explica por qué están T07–T10, pero no acredita un pipeline implementado ni resuelve la ubicación de los agentes, el estado Terraform, el registro por ámbito o sus credenciales. Es una propuesta explícita apoyada en las funciones de [FT03]–[FT06] y el gobierno de contratos de [FI01], 4.2. Debe consolidarse con SD-09 y T-11 antes de tratarlo como configuración definitiva.

## 14. Alojamiento, regiones y límites físicos

La propuesta física [FI04] abre la figura anterior hasta recursos, pools y sitios. Se utiliza como correspondencia provisional para la nueva imagen. En particular, un servicio administrado conectado mediante Private Endpoint no se transforma en una VM dentro de la subred; el endpoint aporta una interfaz/IP privada hacia el recurso.

### 14.1 Ejecución central en Azure

El emplazamiento principal propuesto es Chile Central. Los clústeres privados Retail y Filial separan sus cargas y Frontera aísla X-01. Los pools SYS atienden necesidades de sistema, BIZ servicios y capacidades, INT adaptadores/workers, STATE herramientas con estado y OPS observabilidad. Un pool batch Retail ejecuta trabajos de datos/modelos. Los nodos son VMSS y el scheduler distribuye pods conforme a recursos, dispersión y políticas; ninguna tarjeta exige por sí sola un servidor dedicado.

PostgreSQL, Service Bus, Blob/ADLS, Redis y otros recursos administrados tienen ubicación y configuración propias. Su disponibilidad regional, niveles, endpoints y recuperación deben verificarse recurso por recurso. Las VM propuestas para gateway BI, SHIR y conectores Private Access se separan porque ejecutan funciones y canales distintos. Las cantidades dibujadas en [FI08] son topología inicial por dimensionar, no capacidad aprobada.

### 14.2 Ejecución en tiendas y sitios corporativos

Los POS, móviles, puestos, tótems, controladores y diarios locales están en instalaciones físicas. El par Retail y la custodia financiera aislada sostienen continuidad bajo las condiciones definidas, con redes y administración segregadas. Los hosts conservados ERP/WMS y Crédito 2011 requieren inventario que confirme emplazamiento, soporte y conectividad. Una tarjeta de sistema externo no identifica un contrato de hosting nuevo.

### 14.3 Servicios globales, SaaS y terceros

Front Door es borde global y Entra, Intune, Power BI, Azure DevOps y otros servicios conservan planos de servicio/gestión cuyos datos y metadatos pueden tener ubicación distinta de los nodos de aplicación. Declarar Chile para AKS no acredita residencia exclusivamente chilena de toda la arquitectura. Deben documentarse tenants, espacios, región de almacenamiento, runtime, telemetría, agentes y procesamiento del proveedor.

El antecedente físico registra Private Link de Front Door con tránsito por Brazil South sujeto a aprobación y recuperación Retail activo/pasivo en Brazil South. La recuperación de Filial exige resolver un sitio independiente autorizado; Brasil queda condicionado a aprobación escrita. [FI09], D-35/D-45, y [FI04], secciones 5–7, conservan estos pendientes. Esta explicación no verifica una obligación legal ni autoriza transferencia internacional.

### 14.4 Por qué hay componentes autogestionados

OpenSearch, OpenMetadata, MLflow y la plataforma Prometheus/Loki/Tempo/Grafana tienen responsables de versiones, disponibilidad, almacenamiento, actualizaciones y restauración. [FI02] y [FI03] registran su elección para cubrir búsqueda, gobierno, modelos e instrumentación y controlar su emplazamiento. RT-03.05 exige justificar las excepciones a servicios administrados. La justificación debe completarse con carga operativa, soporte y pruebas; la mera capacidad funcional de una herramienta no demuestra que la excepción esté cerrada.

## 15. Diferencias y decisiones pendientes de la nueva imagen

La imagen es la referencia visual más reciente aportada en esta conversación. Las diferencias siguientes se conservan para que una modificación posterior no convierta silenciosamente una síntesis gráfica en una aprobación de diseño.

| ID de pendiente | Punto a resolver | Criterio para cerrarlo |
| --- | --- | --- |
| P01 | Asteriscos sin definición visible | Incorporar leyenda explícita desde el editable o confirmación del autor. |
| P02 | Nuevo PNG sin editable ni número de figura | Identificar draw.io/JSON, versión, fuente y export correspondiente. |
| P03 | Extremos de los cruces rojos de X-01 | Conciliar con Ventas→X-01→Originación y aprobar cada finalidad/campo. |
| P04 | Terraform, Pipelines, ACR y Policy ahora visibles | Registrar agentes, estado, permisos, regiones, separación y promoción. |
| P05 | Capacidades comunes con «una instancia por ámbito» | Definir producto, réplica, datos, propietario y consumidores. |
| P06 | Oferta aparece como microservicio | Resolver la partición que los registros anteriores dejaban abierta. |
| P07 | F:C-04 y sus dependencias | Confirmar alcance, requisitos, etapa y autoridad antes de desplegar. |
| P08 | Agrupación de PostgreSQL y tecnologías con dos puntos | Fijar recursos/bases/roles sin fusionar ámbitos ni autoridades. |
| P09 | Canales propios y plataformas conservadas | Cerrar responsabilidad funcional, alojamiento y convivencia. |
| P10 | Datos y metadatos fuera del emplazamiento principal | Aprobar matriz por producto, runtime, borde, respaldo y proveedor. |
| P11 | Recuperación financiera y custodia Frontera | Definir segundo sitio, administración, claves y restauración completa. |
| P12 | Cupo local y venta sin enlace | Probar caducidad, doble gasto, fencing y conciliación. |
| P13 | Interfaces externas y sagas | Completar fichas, compensaciones, ventanas y observabilidad. |
| P14 | Herramientas autogestionadas | Cerrar versión, soporte, HA, almacenamiento y recuperación. |
| P15 | Reglas y política de archivo | Definir retención por clase, WORM, borrado y restauración. |
| P16 | API y TLS por salto | Probar contratos, transformación OpenAPI, DNS, identidad y compatibilidad. |
| P17 | Instrumentación, sondas y atención operativa | Cerrar límites, retención, ubicación independiente y respuesta humana. |
| P18 | Innovaciones y modelos | Cerrar proveedores, representaciones, métricas y alternativa manual. |

Los trece servicios de referencia se preservan hasta una decisión de alcance expresa. Las cinco innovaciones tienen propietarios; no generan por defecto cinco microservicios. Las capacidades comunes tienen funciones propias y tampoco modifican automáticamente ese conteo. La lista no registra aceptación humana.

## 16. Cómo usar esta explicación al modificar la arquitectura

Cada cambio debe conservar el vínculo entre necesidad, decisión y ejecución. Se propone mantener los IDs internos de componentes y recorridos para localizar impactos, aun cuando cambie el orden gráfico. No se reutilizará el ID de un componente eliminado para otro distinto.

1. Identificar la imagen/modelo de partida y registrar su hash, fecha y fuente editable.
2. Anotar los IDs de elementos, recorridos y pendientes afectados, junto con la necesidad o requisito que motiva el cambio.
3. Separar la nueva decisión de las opciones evaluadas y conservar el motivo de descarte cuando explique una consecuencia técnica.
4. Revisar autoridad del dato, contratos, identidad, alojamiento, residencia, continuidad y efectos de fallo.
5. Actualizar imagen, explicación, inventario de relaciones y matriz de despliegue como una misma versión.
6. Conciliar SD-04 4.1/4.1.1 y 4.2/4.3, SD-03, SD-05, T-11/T-12 y los planes de trabajo, riesgos, calidad y operación afectados.
7. Validar la especificación y el render con `diagramas-ancoa` cuando se edite la figura. Para editar/compilar la oferta se seguirá exclusivamente `exportar_latex.py` y su skill.
8. Registrar resultados de pruebas y revisión humana con su evidencia. El estado del documento seguirá como borrador hasta que corresponda el registro humano.

Las pruebas de integración deben cubrir rutas completas, no solo la presencia de un icono. Los casos mínimos incluyen solicitud pública y privada, acceso cruzado denegado, compra válida por X-01, duplicados/desorden de mensajes, reconstrucción de proyecciones, pérdida/retorno de enlace, restauración de repositorios y claves, falla de telemetría y despliegue/reversión. Los umbrales se tomarán de las fuentes contractuales vigentes y de los contratos aprobados; no se deducen de nombres comerciales o tamaños de VM.

### 16.1 Registro inicial de cambios

La versión 1.0 conserva la imagen aportada, explica 100 tarjetas mediante IDs documentales y desarrolla doce familias de relaciones. Los localizadores permiten discutir una tarjeta sin depender de su posición en una captura. No se han agregado contratos operacionales a F:C-04 ni se ha modificado la oferta.

Las huellas y la [comprobación documental](comprobacion-documental.txt) de esta entrega se conservan junto al documento. La comprobación de enlaces e inventario valida la integridad documental, no una plataforma Azure ni el trazado exacto de cada flecha del PNG.

## 17. Fuentes y localizadores

Las fuentes internas siguientes permiten reconstruir de dónde procede cada explicación. Son referencias de trabajo; no constituyen una bibliografía adicional de la oferta ni sustituyen las Bases.

### 17.1 Registros internos y trazabilidad contractual

**[FI01] [Contexto de arquitectura y cambios lógicos, 22-10-2026](../contexto-arquitectura-y-cambios-logicos_2026-10-22.md).** Secciones 2–5 para problema, capas, contratos y autoridades; 6–7 para Datos y transversales; 8–11 para conciliación y pendientes. Identifica la figura anterior 4.36 y registra los límites de aceptación.

**[FI02] [Capa de datos, decisiones y precisiones](../capa-datos_decisiones-y-precisiones_2026-10-22.md).** Secciones 2–5 para selección, trazabilidad, autoridad, eventos y recorridos; secciones posteriores para respaldo y pendientes. Restituye ADLS y selecciona OpenSearch, OpenMetadata, MLflow y Python.

**[FI03] [Capas 7 y 8, cambios y conexiones](../capas-07-08_cambios-y-conexiones_2026-10-22.md).** Sección 2 para productos seleccionados; secciones de conexiones para identidad, administración, señales y consulta; cierre para condiciones y fuentes técnicas del registro.

**[FI04] [Arquitectura física derivada, README](../revision-fisica-2026-10-22/README.md).** Secciones 3–5 para recorridos, ejecución, endpoints y red; secciones 6–8 para correcciones y límites. Es propuesta local derivada de 4.36, no validación automática de la nueva imagen.

**[FI05] [Cobertura lógica a física](../revision-fisica-2026-10-22/cobertura-logica-fisica.md).** Correspondencia de elementos de la figura anterior con ubicación y pendientes. Se reutiliza por identidad funcional, sin trasladar su número de nodos al PNG nuevo.

**[FI06] [Matriz servicio, ejecución y persistencia](../revision-fisica-2026-10-22/matriz-despliegue.md).** Trece servicios, autoridades y etapas; ejecución propuesta de herramientas, capacidades y trabajadores.

**[FI07] [Relaciones físicas](../revision-fisica-2026-10-22/relaciones-fisicas.md).** Inventario de conexiones de la propuesta física anterior, con identificadores de nodos y relaciones. No es inventario extraído del nuevo PNG.

**[FI08] [Rutas, puertos y segmentos](../revision-fisica-2026-10-22/rutas-puertos-y-segmentos.md).** Reglas, iniciadores, protocolos y topología propuesta. Las cantidades requieren dimensionamiento y no son capacidad aprobada.

**[FI09] [Registro recibido de decisiones D-01–D-56](../decisiones-2026-10-22/registro-recibido.md).** D-11–D-18 para entradas; D-19–D-34 para servicios e integración; D-35–D-45 para datos, custodia y residencia; D-46 para cadena de entrega. Sus antecedentes se interpretan con las precisiones posteriores S02/S03, sin reactivar productos retirados.

**[FI10] [Bases Transversales](../../../00_Bases/Bases_Transversales.md).** Capítulo 3 para hibridación y autonomía; capítulo 5 para datos, interfaces y analítica; capítulos 11, 12 y 14 para seguridad/identidad/observabilidad; capítulo 16 para capacidades transversales; capítulo 18 para IA. Las selecciones de marca siguen siendo decisiones de diseño.

**[FI11] [Relaciones y evidencia de capa 4](../integracion-capa4-2026-10-22/relaciones-y-evidencia.md) y [servicios y atributos](../integracion-capa4-2026-10-22/servicios-y-atributos.md).** Conservan familias de contratos, autoridades y brechas A/C/E/P. La [especificación recibida](../integracion-capa4-2026-10-22/especificacion-recibida.md) es antecedente; sus recomendaciones de alcance no se adoptan por inferencia.

El marco rector se conserva en [Bases Administrativas](../../../00_Bases/Bases_Administrativas.md), Arts. 16, 17 y 23; [Caso 09](../../../00_Bases/Caso_09_Cadena_Multitienda.md); y [Comunicado 10](../../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md). Esta documentación interna evita trasladar sus hechos particulares como citas finales sin verificar folio. Para la futura oferta rigen la [política de citas](../../../.agents/skills/citas-proyecto/SKILL.md) y la [ruta de exportación](../../../.agents/skills/exportar/SKILL.md).

### 17.2 Documentación técnica oficial consultada el 23-10-2026

Las páginas siguientes respaldan funciones de los productos y patrones descritos. No certifican su disponibilidad en Chile, la configuración concreta del proyecto ni cumplimiento normativo. Las URLs de versión `latest` deben fijarse a una versión al cerrar la plataforma.

**[FT01] [Microsoft, Azure API Center overview](https://learn.microsoft.com/en-us/azure/api-center/overview).** Inventario y gobierno de APIs; apoyo a T03.

**[FT02] [Microsoft, AKS core concepts](https://learn.microsoft.com/en-us/azure/aks/core-aks-concepts).** Distinción de plano de control, nodos y cargas; apoyo a T06 y al alojamiento central.

**[FT03] [Microsoft, Terraform on Azure overview](https://learn.microsoft.com/en-us/azure/developer/terraform/overview).** Infraestructura declarada como código y proveedores; apoyo a T07.

**[FT04] [Microsoft, What is Azure Pipelines?](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops).** Construcción, pruebas y entrega; apoyo a T08.

**[FT05] [Microsoft, Azure Container Registry introduction](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro).** Almacenamiento de imágenes y artefactos; apoyo a T09.

**[FT06] [Microsoft, Azure Policy overview](https://learn.microsoft.com/en-us/azure/governance/policy/overview).** Evaluación y aplicación de políticas de recursos; apoyo a T10.

**[FT07] [Microsoft, Protect APIs with Application Gateway and API Management](https://learn.microsoft.com/en-us/azure/architecture/web-apps/api-management/architectures/protect-apis).** Responsabilidades complementarias de entrada y API; apoyo a G01/G02.

**[FT08] [Microsoft, Front Door Premium with Private Link](https://learn.microsoft.com/en-us/azure/frontdoor/private-link).** Conectividad privada del borde hacia orígenes; apoyo a E01/E02. Regiones, origen y tránsito concretos requieren comprobación de diseño.

**[FT09] [Microsoft, Azure Service Bus overview](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview).** Mensajería mediante colas y temas/suscripciones; apoyo a I01/I07. El outbox y la idempotencia del proyecto proceden de S02.

**[FT10] [MLflow, documentación de machine learning](https://mlflow.org/docs/latest/ml/).** Gestión del ciclo y seguimiento de modelos; apoyo a D18.

**[FT11] [OpenMetadata, Metadata Standard](https://docs.open-metadata.org/v2.0.x/main-concepts/metadata-standard).** Entidades y relaciones del modelo de metadatos; apoyo a D20. La versión del despliegue del proyecto no se fija por esta consulta.

**[FT12] [Microsoft, Workload Identity in AKS](https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview).** Federación de identidades de cargas; apoyo a S07.

**[FT13] [OpenTelemetry, Collector](https://opentelemetry.io/docs/collector/).** Recepción, procesamiento y exportación de señales; apoyo a O01.

**[FT14] [Prometheus, overview](https://prometheus.io/docs/introduction/overview/).** Métricas y consulta; apoyo a O02.

**[FT15] [Grafana, Loki overview](https://grafana.com/docs/loki/latest/get-started/overview/).** Almacenamiento y consulta de registros; apoyo a O03.

**[FT16] [Grafana, Tempo documentation](https://grafana.com/docs/tempo/latest/).** Trazas distribuidas; apoyo a O04.

[FI01]: ../contexto-arquitectura-y-cambios-logicos_2026-10-22.md
[FI02]: ../capa-datos_decisiones-y-precisiones_2026-10-22.md
[FI03]: ../capas-07-08_cambios-y-conexiones_2026-10-22.md
[FI04]: ../revision-fisica-2026-10-22/README.md
[FI05]: ../revision-fisica-2026-10-22/cobertura-logica-fisica.md
[FI06]: ../revision-fisica-2026-10-22/matriz-despliegue.md
[FI07]: ../revision-fisica-2026-10-22/relaciones-fisicas.md
[FI08]: ../revision-fisica-2026-10-22/rutas-puertos-y-segmentos.md
[FI09]: ../decisiones-2026-10-22/registro-recibido.md
[FI10]: ../../../00_Bases/Bases_Transversales.md
[FI11]: ../integracion-capa4-2026-10-22/relaciones-y-evidencia.md
[FT01]: https://learn.microsoft.com/en-us/azure/api-center/overview
[FT02]: https://learn.microsoft.com/en-us/azure/aks/core-aks-concepts
[FT03]: https://learn.microsoft.com/en-us/azure/developer/terraform/overview
[FT04]: https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops
[FT05]: https://learn.microsoft.com/en-us/azure/container-registry/container-registry-intro
[FT06]: https://learn.microsoft.com/en-us/azure/governance/policy/overview
[FT07]: https://learn.microsoft.com/en-us/azure/architecture/web-apps/api-management/architectures/protect-apis
[FT08]: https://learn.microsoft.com/en-us/azure/frontdoor/private-link
[FT09]: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview
[FT10]: https://mlflow.org/docs/latest/ml/
[FT11]: https://docs.open-metadata.org/v2.0.x/main-concepts/metadata-standard
[FT12]: https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview
[FT13]: https://opentelemetry.io/docs/collector/
[FT14]: https://prometheus.io/docs/introduction/overview/
[FT15]: https://grafana.com/docs/loki/latest/get-started/overview/
[FT16]: https://grafana.com/docs/tempo/latest/

## Declaración de uso de IA

Documento elaborado con asistencia de Codex para explicar la imagen aportada, contrastarla con registros locales, consultar documentación técnica oficial y conservar trazabilidad para cambios futuros. Nivel de texto Alto. Se aplicaron `technical-writing` y `humanizer` con el registro formal y las restricciones de redacción del proyecto. No se dispone de evidencia suficiente para atribuir la generación de la imagen recibida; esta entrega solo conserva una copia sin editar. No se modificaron diagramas, código de plataforma, requisitos ni fuentes LaTeX. No se registra revisión humana formal ni pruebas de despliegue, capacidad, seguridad o recuperación ejecutadas.
