# Pontificia Universidad Católica de Valparaíso - Escuela de Informática
## Licitación N° TFEP-01/2026: Bases Técnicas Transversales

**Requisitos técnicos comunes a las trece industrias del llamado**

| | |
| :--- | :--- |
| **Asignatura** | Taller de Formulación de Proyectos Informáticos - ICI-5444 |
| **Unidad académica** | Escuela de Informática, Pontificia Universidad Católica de Valparaíso |
| **Profesor** | Antonio Moya Villegas <br> antonio.moya@pucv.cl |
| **Objeto** | Requisitos de arquitectura, infraestructura, calidad, operación y presentación exigibles a toda solución ofertada |
| **Ámbito** | Las trece industrias del llamado, sin excepción |
| **Documento base** | Bases Administrativas TFEP-01/2026 (FEP01.26) |
| **Documento complementario** | Bases Técnicas del caso asignado a cada empresa proponente |
| **Fecha / Versión** | agosto de 2026 / 1.0 |

Este documento fija el piso técnico común del llamado. Todo lo que aquí se exige es exigible en las trece industrias; lo que cada industria tiene de propio —su proceso de negocio, sus volúmenes, sus integraciones y su regulación sectorial— se establece en las Bases Técnicas de cada caso.

Los requisitos están codificados como **RT-CC.NN** y deben responderse uno a uno en el Formulario T-12 de las Bases Administrativas.

---

### CONTENIDO

| Título | Contenido | Capítulos |
| :--- | :--- | :--- |
| **I. Disposiciones del documento** | Objeto, ámbito, relación con los demás documentos, régimen de cumplimiento y forma de responder. | 1 |
| **II. Arquitectura de la solución** | Modelo multicapa de referencia, modelo híbrido de nube y on-premise, ambientes y entrega continua, datos, integración y analítica. | 2 - 5 |
| **III. Infraestructura** | Site principal on-premise, site secundario y recuperación ante desastres, hardware, puestos de trabajo y equipamiento de terreno. | 6 - 8 |
| **IV. Requisitos no funcionales** | Desempeño y capacidad, disponibilidad y resiliencia, seguridad, identidad, usabilidad y accesibilidad, observabilidad, sostenibilidad y certificaciones. | 9 - 15 |
| **V. Capacidades transversales** | Módulos obligatorios en toda industria, canales digitales y movilidad, inteligencia artificial y automatización. | 16 - 18 |
| **VI. Proyecto, implantación y operación** | Gobierno del proyecto, pruebas y criterios de aceptación, modelo de operación, mesa de ayuda, mantención y capacitación. | 19 - 22 |
| **VII. Exigencias de presentación** | Presencia digital del proponente, video de presentación, prototipo interactivo de interfaz e innovaciones. | 23 - 26 |
| **VIII. Anexos** | Índice de requisitos, plantilla de volumetría, checklist de entregables y glosario. | A - D |

> **Cómo se articula este documento con los demás**
>
> Las Bases Administrativas gobiernan el proceso y el contrato: quién participa, qué garantías rinde, cómo se evalúa, qué plazos rigen y qué se penaliza. Su Capítulo 4 enuncia los requisitos transversales en el nivel de exigencia contractual.
>
> Este documento desarrolla técnicamente ese Capítulo 4 y lo lleva al nivel de requisito verificable. Donde las Bases Administrativas dicen «la solución deberá tener alta disponibilidad», aquí se dice cuál, medida cómo, probada cuándo y acreditada con qué evidencia.
>
> Las Bases Técnicas de cada caso, que se publican por separado, aportan el contexto de la industria, el proceso de negocio, los requerimientos funcionales, la volumetría real y los valores concretos de todo requisito marcado «Según caso» en este documento.
>
> **Sobre el nivel de exigencia:** Este pliego describe una plataforma de misión crítica, no un sistema de gestión convencional. Los umbrales, los estándares y los controles que contiene son los que hoy se exigen en el mercado a un proveedor que opera la infraestructura digital de una empresa. Una propuesta que los trate como formalidades a declarar, en lugar de como decisiones de ingeniería a resolver, quedará en evidencia en la matriz de cumplimiento y en la defensa técnica.

---

## TÍTULO I: DISPOSICIONES DEL DOCUMENTO

### CAPÍTULO 1: OBJETO, ÁMBITO Y RÉGIMEN DE CUMPLIMIENTO

#### 1.1 Objeto
Las presentes Bases Técnicas Transversales establecen los requisitos técnicos, de infraestructura, de calidad, de operación y de presentación que toda solución ofertada en la Licitación N° TFEP-01/2026 debe satisfacer, con independencia de la industria y del caso asignado a cada empresa proponente.

El propósito de este documento es doble. Primero, fijar un piso técnico común y exigente que impida que la comparación entre ofertas se distorsione por diferencias de interpretación sobre qué es una plataforma de misión crítica. Segundo, liberar a las Bases Técnicas de cada caso de repetir aquello que es común, permitiéndoles concentrarse en lo que efectivamente distingue a una industria de otra: su proceso de negocio, sus volúmenes, sus integraciones, sus regulaciones sectoriales y sus criterios de aceptación propios.

#### 1.2 Ámbito de aplicación
Este documento aplica íntegramente a los trece casos del llamado:

| N° | Industria | N° | Industria |
| :--- | :--- | :--- | :--- |
| 1 | Minería - extracción de recursos | 8 | Sala de cine - entretenimiento |
| 2 | Logística - empresa distribuidora | 9 | Cadena multitienda - retail |
| 3 | Servicios de agua potable - utilities | 10 | Transporte de carga |
| 4 | Consultas médicas - salud y bienestar | 11 | Servicios financieros - banca, seguros y cambio |
| 5 | Cadena de hoteles - turismo y hospitalidad | 12 | Agroindustria |
| 6 | Portuaria - operación marítima comercial | 13 | Telecomunicaciones |
| 7 | Servicio de puerto deportivo - recreación marítima | | |

#### 1.3 Relación con los demás documentos del proceso
Este documento se lee conjuntamente con las Bases Administrativas y con las Bases Técnicas del caso, conforme al orden de precedencia del Artículo 5° de las Bases Administrativas.

| Documento | Qué define | Relación |
| :--- | :--- | :--- |
| **Bases Administrativas TFEP-01/2026** | Reglas del proceso, participación, garantías, evaluación, adjudicación, contrato, niveles de servicio contractuales, penalidades y exigencia de innovación. Incluye el cronograma obligatorio de 56 meses (Art. 17°) y los requisitos transversales de nivel contractual (Capítulo 4). | Prevalecen sobre este documento en materias administrativas y contractuales. |
| **Bases Técnicas Transversales (este documento)** | Cómo debe estar construida, desplegada, protegida, operada y presentada la solución, en términos técnicos verificables y comunes a las trece industrias. | Desarrolla técnicamente el Capítulo 4 de las Bases Administrativas. No lo contradice ni lo rebaja. |
| **Bases Técnicas del caso** | Contexto de la industria, proceso de negocio, requerimientos funcionales, volúmenes reales, integraciones, normativa sectorial, ventana operacional y criterios de aceptación propios del caso. | Puede endurecer cualquier requisito de este documento; nunca rebajarlo. Aporta los valores de los requisitos marcados «Según caso». |

#### 1.4 Régimen de cumplimiento
Los requisitos de este documento se identifican con un código de la forma RT-CC.NN, donde CC es el número del capítulo y NN el correlativo dentro de él. Cada requisito tiene un carácter:

| Carácter | Significado | Efecto en la evaluación |
| :--- | :--- | :--- |
| **Obligatorio** | Requisito de cumplimiento forzoso. La solución no es admisible sin él. | Su incumplimiento o su omisión producen puntaje cero en el ítem afectado. El incumplimiento de un requisito obligatorio de seguridad, continuidad o arquitectura habilita la exclusión conforme al Artículo 58° de las Bases Administrativas. |
| **Deseable** | Requisito que el CLIENTE valora pero no exige. Diferencia una oferta buena de una oferta destacada. | Su cumplimiento acreditado otorga puntaje adicional dentro del ítem. Su ausencia no penaliza. |
| **Según caso** | Requisito obligatorio cuyo valor numérico, umbral o alcance concreto lo fijan las Bases Técnicas del caso. | Se evalúa contra el valor del caso. Si el caso no lo fija, rige el valor por defecto que este documento indique y, en su defecto, el criterio de la Comisión Evaluadora. |

#### 1.5 Cómo debe responderse este documento
El PROPONENTE deberá acreditar el cumplimiento de la totalidad de los requisitos en el Formulario T-12, Matriz de Cumplimiento Técnico y Trazabilidad, indicando por cada código RT:
1. Si cumple, cumple parcialmente o no cumple.
2. El componente, servicio, producto o práctica concreta con que lo satisface, individualizado por nombre y versión.
3. La sección y página de la Oferta Técnica donde se desarrolla.
4. La evidencia con que se verificará durante la ejecución: entregable, prueba, informe o certificado.

> Declarar «cumple» sin individualizar el componente ni indicar dónde se desarrolla equivale a no declarar. La Comisión Evaluadora no buscará en la propuesta la respuesta que el PROPONENTE no señaló, y calificará el requisito como no acreditado.

#### 1.6 Neutralidad tecnológica y criterio de vigencia
Este documento no impone marcas, productos ni proveedores determinados. Cuando menciona un producto lo hace a título de referencia y admite equivalentes de prestaciones iguales o superiores, lo que el PROPONENTE deberá acreditar.

Sí impone, en cambio, un criterio de vigencia. Todo componente ofertado —lenguaje, marco de trabajo, motor de base de datos, sistema operativo, biblioteca, dispositivo— deberá contar con soporte vigente del fabricante o de su comunidad al momento de la oferta, y con hoja de ruta de soporte que cubra, como mínimo, la totalidad del período contractual de 56 meses. El PROPONENTE deberá declarar, por cada componente principal, su versión, su fecha de fin de soporte y su plan de actualización.

La obsolescencia programada de un componente durante la vigencia del Contrato no es un riesgo del CLIENTE. Si un componente alcanza su fin de soporte antes del mes 56, la actualización o la sustitución es de cargo del ADJUDICATARIO y debe estar prevista y costeada en la oferta.

#### 1.7 Interpretación de los umbrales
Todo umbral expresado en este documento es un mínimo exigido, salvo que se indique expresamente que constituye un máximo. Los tiempos de respuesta se entienden medidos en el percentil 95 sobre la experiencia real del usuario final, y no como promedio ni como medición sintética de laboratorio, salvo indicación expresa.

Las mediciones de disponibilidad se calculan sobre la transacción de negocio completa de extremo a extremo. La disponibilidad de la infraestructura subyacente no es un sustituto válido: un componente activo que devuelve errores no cuenta como disponible.

---

## TÍTULO II: ARQUITECTURA DE LA SOLUCIÓN

### CAPÍTULO 2: MODELO DE ARQUITECTURA DE REFERENCIA

#### 2.1 Modelo multicapa exigido
La solución deberá organizarse en las capas que se describen a continuación. Las capas son de existencia obligatoria; la tecnología con que se materializa cada una es decisión del PROPONENTE, que deberá justificarla.

| Capa | Responsabilidad | Exigencias mínimas |
| :--- | :--- | :--- |
| **Presentación** | Interfaces de las personas usuarias: portal web, aplicación móvil, terminales operacionales y pantallas de terreno. | Diseño adaptativo, accesible y sin lógica de negocio. Ninguna interfaz podrá acceder directamente a la base de datos. |
| **Borde y exposición** | Único punto de entrada público: distribución de contenidos, balanceo, protección perimetral y terminación de cifrado. | CDN, WAF gestionado, protección contra denegación de servicio en capas 3, 4 y 7, y terminación TLS 1.3. |
| **Puerta de enlace de servicios** | Publicación, autenticación, autorización, cuotas, límites de tasa, versionado y observabilidad de las interfaces de programación. | Validación de esquema, inspección de carga útil, trazabilidad por transacción y catálogo de servicios. |
| **Servicios de negocio** | Lógica del proceso de negocio del caso, organizada en módulos con límites de contexto explícitos. | Sin estado, desplegables de forma independiente, con contratos versionados y compatibilidad hacia atrás. |
| **Integración y eventos** | Comunicación asíncrona, desacoplamiento, orquestación y coreografía de procesos entre módulos y con sistemas externos. | Bus o intermediario de mensajería con persistencia, cola de mensajes fallidos, reintento y deduplicación. |
| **Datos** | Persistencia transaccional, analítica, documental, de series de tiempo y de archivos, según lo requiera el caso. | Separación entre lo transaccional y lo analítico. Cifrado en reposo. Respaldo y retención declarados. |
| **Seguridad transversal** | Identidad, autorización, gestión de secretos, cifrado, registro de auditoría y detección. | Aplicada a todas las capas, no como capa perimetral única. |
| **Observabilidad transversal** | Métricas, registros y trazas distribuidas correlacionadas. | Instrumentación conforme a OpenTelemetry, cobertura de nube y on-premise sin puntos ciegos. |

#### 2.2 Requisitos de arquitectura

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-02.01** | La solución se organizará en las ocho capas del numeral 2.1. El PROPONENTE presentará el diagrama de la arquitectura lógica identificando cada capa, sus componentes y las interfaces entre ellas. | Obligatorio |
| **RT-02.02** | La arquitectura será modular, con límites de contexto explícitos y acoplamiento débil. Se rechazará toda arquitectura monolítica que no permita desplegar de forma independiente sus componentes críticos. | Obligatorio |
| **RT-02.03** | La descripción de la arquitectura se ajustará a ISO/IEC/IEEE 42010, con vistas lógica, de procesos, de despliegue, de datos y de seguridad. | Obligatorio |
| **RT-02.04** | El PROPONENTE mantendrá un registro de decisiones de arquitectura (ADR) fechado, con la alternativa escogida, las alternativas descartadas y el criterio de decisión. El registro es entregable contractual y se actualizará durante toda la ejecución. | Obligatorio |
| **RT-02.05** | La capa de servicios de negocio será sin estado. El estado de sesión y el estado de proceso residirán en almacenes externos con alta disponibilidad. | Obligatorio |
| **RT-02.06** | Toda operación de escritura expuesta a reintentos será idempotente, con clave de idempotencia declarada por el cliente y ventana de deduplicación documentada. | Obligatorio |
| **RT-02.07** | Los flujos de eventos garantizarán entrega al menos una vez, con deduplicación en el consumidor y orden garantizado dentro de la partición o del agregado cuando el proceso lo exija. | Obligatorio |
| **RT-02.08** | La solución implementará patrones de resiliencia demostrables: reintento con retroceso exponencial y variación aleatoria, cortacircuitos, mamparos de aislamiento, límites de tasa y tiempo de espera explícito en toda llamada remota. No se admiten llamadas remotas sin tiempo de espera. | Obligatorio |
| **RT-02.09** | La solución degradará de forma elegante: ante la indisponibilidad de un componente no crítico deberá continuar operando en modo reducido, informando la degradación a la persona usuaria, y nunca fallar de forma total. | Obligatorio |
| **RT-02.10** | Las capas de aplicación e integración escalarán horizontalmente de forma automática, con umbrales, límites superiores y costo asociado declarados en la oferta. | Obligatorio |
| **RT-02.11** | El PROPONENTE declarará explícitamente los puntos únicos de falla que subsistan en su arquitectura y justificará por qué son aceptables. Omitir esta declaración cuando existan puntos únicos de falla se evaluará como observación grave. | Obligatorio |
| **RT-02.12** | La solución admitirá su replicación a nuevas unidades, sitios, sucursales o filiales del CLIENTE sin rediseño arquitectónico, mediante parametrización o multi-tenencia. | Según caso |
| **RT-02.13** | El PROPONENTE presentará un modelo de dominio del negocio del caso, con las entidades principales, sus relaciones y los eventos de negocio que las modifican. | Obligatorio |
| **RT-02.14** | Se valorará la aplicación documentada de patrones de arquitectura evolutiva que permitan sustituir un componente sin reescribir la solución: capa anticorrupción frente a sistemas heredados, estrangulamiento progresivo y abstracción de proveedores. | Deseable |

#### 2.3 Estilo arquitectónico y su justificación
El CLIENTE no impone un estilo arquitectónico. Sí exige que el escogido sea explícito, coherente con la escala del caso y justificado. El PROPONENTE deberá comparar al menos dos alternativas y explicar por qué descarta la no elegida, considerando la complejidad operacional que introduce, el tamaño y las competencias del equipo, el costo de infraestructura y la capacidad del CLIENTE de operarla al término del Contrato.

> Adoptar una arquitectura de microservicios para un caso cuyo volumen no la justifica es un error de ingeniería y se evaluará como tal. La sofisticación no reemplaza a la pertinencia.

### CAPÍTULO 3: MODELO HÍBRIDO: NUBE Y ON-PREMISE

#### 3.1 Distribución de cargas
Conforme al Artículo 16° de las Bases Administrativas, la solución será obligatoriamente híbrida. El PROPONENTE deberá presentar una tabla de emplazamiento que asigne cada componente a nube o a on-premise y justifique la decisión.

| Criterio de emplazamiento | Tiende a nube | Tiende a on-premise |
| :--- | :--- | :--- |
| **Latencia tolerada por el proceso** | Superior a 100 ms | Inferior a 50 ms o determinista |
| **Consecuencia de la pérdida de conectividad** | El proceso puede esperar | El proceso debe continuar sin excepción |
| **Volumen y costo de transferencia de datos** | Volumen moderado | Alto volumen generado localmente (video, telemetría, sensores) |
| **Acoplamiento con equipamiento físico** | Nulo o mediado por servicios | Directo: balanzas, PLC, lectores, barreras, cámaras, básculas |
| **Elasticidad de la demanda** | Muy variable o estacional | Constante y predecible |
| **Restricción regulatoria de residencia o custodia** | Sin restricción | Con restricción sectorial declarada en el caso |

#### 3.2 Requisitos del componente en nube

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-03.01** | El PROPONENTE declarará el proveedor de nube pública, la región primaria y la región secundaria utilizadas. El proveedor deberá contar con presencia de región o zona en Chile o en Sudamérica. | Obligatorio |
| **RT-03.02** | Todos los componentes con requisito de alta disponibilidad se desplegarán en al menos dos zonas de disponibilidad. No se aceptará un diseño en una sola zona. | Obligatorio |
| **RT-03.03** | La totalidad de la infraestructura se definirá como código, versionada en el repositorio del CLIENTE, revisable y reproducible. No se admite infraestructura creada manualmente por consola, salvo la cuenta raíz inicial, cuya creación deberá documentarse. | Obligatorio |
| **RT-03.04** | La red se segmentará por capas, con subredes privadas para aplicación y datos, y exposición pública restringida a la capa de borde. Ningún componente de datos será alcanzable desde Internet. | Obligatorio |
| **RT-03.05** | El PROPONENTE privilegiará servicios administrados por sobre servicios autoadministrados cuando ello reduzca el riesgo operacional, y justificará cada excepción. | Obligatorio |
| **RT-03.06** | Se aplicarán prácticas FinOps: etiquetado obligatorio de todos los recursos por ambiente, módulo y centro de costo; presupuestos con alertas de desviación; y reporte mensual de consumo desglosado entregado al CLIENTE. | Obligatorio |
| **RT-03.07** | El PROPONENTE declarará su estrategia de reversibilidad y de mitigación del bloqueo por proveedor, identificando qué componentes son portables, cuáles no lo son y cuál sería el esfuerzo estimado de una migración. | Obligatorio |
| **RT-03.08** | La solución empleará instancias reservadas, planes de ahorro o capacidad comprometida cuando el perfil de carga lo justifique, y lo reflejará en la estructura de costos. | Deseable |
| **RT-03.09** | Se valorará el uso de cómputo sin servidor o de contenedores administrados para las cargas de perfil variable, con el análisis comparativo de costo frente a instancias permanentes. | Deseable |

#### 3.3 Requisitos del componente on-premise y del borde operacional

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-03.10** | El componente on-premise operará de forma autónoma y degradada ante la pérdida total del enlace con la nube, durante un período mínimo de 24 horas continuas o el mayor que fije el caso. | Obligatorio |
| **RT-03.11** | Durante la operación desconectada, la solución continuará registrando las transacciones operacionales críticas de forma local, con integridad garantizada y sin pérdida de datos. | Obligatorio |
| **RT-03.12** | Restablecido el enlace, la sincronización será automática, con reconciliación determinista de conflictos, regla de resolución documentada y bitácora auditable de las decisiones aplicadas. | Obligatorio |
| **RT-03.13** | El PROPONENTE declarará qué funciones NO estarán disponibles en modo desconectado y qué procedimiento manual las suple. La ausencia de esta declaración se evaluará como observación grave. | Obligatorio |
| **RT-03.14** | Los equipos on-premise críticos serán redundantes. El almacenamiento local tolerará la falla de al menos un disco; el PROPONENTE declarará el nivel RAID escogido y lo justificará frente a las alternativas. | Obligatorio |
| **RT-03.15** | Los sistemas on-premise se endurecerán conforme a los CIS Benchmarks aplicables, con gestión centralizada de parches y ventana de aplicación acordada con el CLIENTE. | Obligatorio |
| **RT-03.16** | El monitoreo del componente on-premise se integrará a la misma plataforma de observabilidad que la nube, con alertamiento unificado. | Obligatorio |
| **RT-03.17** | El enlace entre el sitio on-premise y la nube será redundante, con caminos físicos y proveedores distintos, y conmutación automática con tiempo de conmutación declarado. | Obligatorio |
| **RT-03.18** | Los dispositivos de borde y de terreno se administrarán de forma remota y centralizada: inventario, configuración, actualización de firmware y de aplicación, bloqueo y borrado remoto. | Obligatorio |
| **RT-03.19** | Se valorará el procesamiento en el borde de las cargas que lo admitan —filtrado, agregación previa, inferencia local— reduciendo el volumen transferido y la dependencia del enlace. | Deseable |

#### 3.4 Conectividad y redes

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-03.20** | El PROPONENTE dimensionará el ancho de banda requerido por sitio, en régimen normal y en peak, y lo justificará con el cálculo de volumen de transacciones y de datos. | Obligatorio |
| **RT-03.21** | La conexión entre la red del CLIENTE y la nube se establecerá mediante enlace privado dedicado o red privada virtual con cifrado, según lo que el volumen y la criticidad justifiquen. | Obligatorio |
| **RT-03.22** | El acceso remoto de las personas trabajadoras del CLIENTE, incluido el trabajo desde el hogar, se resolverá con acceso a la red de confianza cero, con verificación de postura del dispositivo. No se admite exponer servicios internos directamente a Internet. | Obligatorio |
| **RT-03.23** | La red inalámbrica de los sitios operacionales, cuando el caso la requiera, contará con segmentación por tipo de dispositivo, autenticación por certificado o credencial de empresa y cobertura verificada mediante estudio de sitio. | Según caso |
| **RT-03.24** | El PROPONENTE declarará la calidad de servicio y la priorización de tráfico aplicada a las transacciones operacionales críticas frente al tráfico administrativo. | Deseable |

### CAPÍTULO 4: AMBIENTES, ENTREGA CONTINUA Y GESTIÓN DE LA CONFIGURACIÓN

#### 4.1 Ambientes obligatorios

| Ambiente | Propósito | Exigencias |
| :--- | :--- | :--- |
| **Desarrollo** | Construcción y prueba unitaria por parte del equipo de desarrollo. | Aislado. Datos sintéticos o anonimizados. Reconstruible desde código. |
| **QA** | Pruebas funcionales, de integración, de regresión y automatizadas. | Aislado. Datos de prueba controlados y versionados. Reinicio a estado conocido. |
| **Preproducción** | Pruebas de aceptación, de carga, de resiliencia y ensayo del paso a producción. | Equivalente a producción en topología, configuración y versiones. Volumen de datos representativo. |
| **Producción** | Operación real. | Acceso restringido y auditado. Sin acceso interactivo directo de desarrolladores. |
| **Recuperación ante desastres** | Continuidad ante indisponibilidad de la región o del sitio primario. | Replicación continua. Conmutación probada semestralmente. |

#### 4.2 Requisitos de entrega continua

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-04.01** | Los cinco ambientes del numeral 4.1 estarán habilitados y operativos como condición del hito H3 del Formulario E-25. | Obligatorio |
| **RT-04.02** | Preproducción será equivalente a producción en topología, versiones de componentes y configuración. Las diferencias que subsistan por costo se declararán expresamente y se justificarán. | Obligatorio |
| **RT-04.03** | El código residirá en un sistema de control de versiones con ramas protegidas, revisión obligatoria por pares y prohibición de escritura directa sobre la rama principal. | Obligatorio |
| **RT-04.04** | Existirá trazabilidad completa entre requerimiento, incidencia, cambio de código, prueba ejecutada y despliegue realizado. | Obligatorio |
| **RT-04.05** | El flujo de integración continua ejecutará, como mínimo: compilación, pruebas unitarias, análisis estático de código, análisis de composición de software, escaneo de secretos y escaneo de imágenes de contenedor, con criterios de bloqueo automático del despliegue. | Obligatorio |
| **RT-04.06** | Los despliegues serán automatizados y reproducibles, con reversión automatizada y sin intervención manual en el paso a producción. | Obligatorio |
| **RT-04.07** | La estrategia de despliegue permitirá liberar sin interrupción del servicio: azul-verde, canario o despliegue progresivo. Se declarará cuál se emplea y se demostrará en Preproducción antes de cada paso a producción. | Obligatorio |
| **RT-04.08** | Toda configuración estará externalizada del artefacto y gestionada por ambiente. Un mismo artefacto deberá poder promoverse de QA a Preproducción y a Producción sin recompilación. | Obligatorio |
| **RT-04.09** | Los secretos residirán en un gestor de secretos con rotación automática y auditoría de acceso. Queda prohibida toda credencial embebida en código, imágenes o archivos de configuración. | Obligatorio |
| **RT-04.10** | Las migraciones de esquema de base de datos serán versionadas, reversibles y ejecutadas de forma automatizada, con estrategia de compatibilidad que permita convivir dos versiones de la aplicación durante el despliegue. | Obligatorio |
| **RT-04.11** | La cobertura de pruebas automatizadas del código de lógica de negocio será de al menos 70%, con umbral bloqueante en el flujo de integración continua. | Obligatorio |
| **RT-04.12** | El PROPONENTE declarará su frecuencia de despliegue objetivo, su tiempo desde el compromiso de código hasta producción, su tasa de cambios fallidos y su tiempo de restauración, y los medirá durante la Operación. | Obligatorio |
| **RT-04.13** | Los ambientes no productivos se apagarán o reducirán fuera del horario de uso, con el ahorro reflejado en la estructura de costos. | Deseable |
| **RT-04.14** | Se valorará la existencia de ambientes efímeros por rama o por incidencia, creados y destruidos automáticamente. | Deseable |

### CAPÍTULO 5: DATOS, INTEGRACIÓN E INTEROPERABILIDAD

#### 5.1 Modelo y gestión de datos

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-05.01** | El PROPONENTE entregará el modelo de datos documentado y un diccionario de datos con el nombre, el tipo, el dominio de valores, la obligatoriedad, el propietario y la sensibilidad de cada atributo. | Obligatorio |
| **RT-05.02** | El PROPONENTE justificará la selección del paradigma y del motor de persistencia: relacional o no relacional, garantías transaccionales, y la posición escogida entre consistencia y disponibilidad conforme al teorema CAP, para cada dominio de datos. | Obligatorio |
| **RT-05.03** | Toda operación de negocio será trazable: la solución permitirá reconstruir quién, qué, cuándo, desde qué dispositivo y con qué valores anteriores y posteriores, para cualquier registro y en cualquier momento del período de retención. | Obligatorio |
| **RT-05.04** | La calidad de datos se gestionará conforme a ISO/IEC 25012, con validación en el punto de captura, indicadores de completitud, exactitud y consistencia, y tablero de calidad disponible para el CLIENTE. | Obligatorio |
| **RT-05.05** | El almacenamiento transaccional y el analítico estarán separados. Ninguna consulta analítica podrá degradar el desempeño de la operación. | Obligatorio |
| **RT-05.06** | La solución permitirá exportar la totalidad de la información del CLIENTE en formatos abiertos y documentados, en cualquier momento del Contrato, sin costo adicional y sin intervención del ADJUDICATARIO. | Obligatorio |
| **RT-05.07** | El PROPONENTE declarará la política de retención, archivado y eliminación por cada dominio de datos, coherente con la normativa aplicable al caso, e implementará un procedimiento verificable de eliminación segura. | Obligatorio |
| **RT-05.08** | Los datos personales se tratarán conforme al Artículo 85° de las Bases Administrativas, con seudonimización o cifrado a nivel de campo para las categorías sensibles que el caso identifique. | Obligatorio |
| **RT-05.09** | El PROPONENTE presentará una estrategia de gestión de datos maestros que evite la duplicación de entidades compartidas entre módulos y con sistemas externos. | Obligatorio |
| **RT-05.10** | Se valorará la implementación de un catálogo de datos con linaje automatizado, que permita rastrear el origen de cada indicador de negocio hasta su fuente. | Deseable |

#### 5.2 Migración de datos

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-05.11** | El PROPONENTE presentará un plan de migración con alcance, origen, volumen, reglas de transformación, criterios de calidad, estrategia de ejecución y plan de reversión. | Obligatorio |
| **RT-05.12** | La migración incluirá una etapa de perfilado y saneamiento previo, con informe de los defectos detectados en los datos de origen y la decisión adoptada sobre cada uno. | Obligatorio |
| **RT-05.13** | Se ejecutarán al menos dos ensayos completos de migración sobre Preproducción antes de la migración definitiva, con medición del tiempo total y del resultado de la conciliación. | Obligatorio |
| **RT-05.14** | La conciliación posterior a la migración será cuantitativa y verificable: recuentos, sumas de control y muestreo dirigido. Toda diferencia deberá quedar explicada. | Obligatorio |
| **RT-05.15** | Los datos históricos que no se migren quedarán accesibles en un repositorio de consulta durante el período de retención que fije el caso. | Según caso |

#### 5.3 Integración e interoperabilidad

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-05.16** | Los servicios síncronos se documentarán en OpenAPI 3.1 y los flujos dirigidos por eventos en AsyncAPI 2.6 o superior. La documentación se generará desde el código y se mantendrá actualizada automáticamente. | Obligatorio |
| **RT-05.17** | Los contratos de interfaz se versionarán semánticamente, con compatibilidad hacia atrás y política de obsolescencia con preaviso mínimo de seis meses. | Obligatorio |
| **RT-05.18** | La autenticación entre sistemas empleará OAuth 2.1 con credenciales de cliente o autenticación mutua TLS. Queda prohibida la autenticación por clave estática en la ruta de la dirección web. | Obligatorio |
| **RT-05.19** | Toda integración registrará la transacción de entrada y de salida, con identificador de correlación común que permita seguir una operación de negocio a través de todos los sistemas involucrados. | Obligatorio |
| **RT-05.20** | Las integraciones con sistemas heredados o de terceros se aislarán mediante una capa anticorrupción, de modo que un cambio en el sistema externo no propague su modelo al núcleo de la solución. | Obligatorio |
| **RT-05.21** | El PROPONENTE declarará, por cada integración, el modo (síncrono o asíncrono), el volumen esperado, la ventana de disponibilidad del sistema contraparte y el comportamiento de la solución cuando ese sistema no responde. | Obligatorio |
| **RT-05.22** | La solución soportará la carga y descarga masiva de información en formatos abiertos, con validación previa, informe de errores por registro y procesamiento parcial. | Obligatorio |
| **RT-05.23** | Se emplearán los estándares sectoriales de intercambio que las Bases Técnicas del caso identifiquen. | Según caso |
| **RT-05.24** | Se valorará la publicación de un portal de servicios para desarrolladores con documentación navegable, ambiente de pruebas y credenciales de prueba autoservidas. | Deseable |

#### 5.4 Analítica e inteligencia de negocio

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-05.25** | La solución proveerá una capa analítica con tableros operacionales y de gestión, construidos sobre los indicadores que las Bases Técnicas del caso definan. | Obligatorio |
| **RT-05.26** | Los tableros permitirán filtrar por período, unidad organizacional y dimensiones propias del caso, y profundizar desde el indicador agregado hasta la transacción de origen. | Obligatorio |
| **RT-05.27** | El CLIENTE podrá construir sus propios informes sin intervención del ADJUDICATARIO, mediante una herramienta de autoservicio con modelo semántico documentado. | Obligatorio |
| **RT-05.28** | Todo informe será exportable en formatos abiertos y programable para envío automático por calendario. | Obligatorio |
| **RT-05.29** | La latencia máxima entre la ocurrencia de una transacción y su disponibilidad en la capa analítica será la que fije el caso y, en su defecto, no superará las 4 horas. | Según caso |
| **RT-05.30** | Se valorará la incorporación de analítica predictiva pertinente al proceso del caso, con el modelo, sus variables, su métrica de desempeño y su plan de reentrenamiento documentados. | Deseable |

---

## TÍTULO III: INFRAESTRUCTURA

### CAPÍTULO 6: SITE PRINCIPAL ON-PREMISE

#### 6.1 Alcance y dimensionamiento proporcional
El PROPONENTE deberá habilitar un recinto técnico para el alojamiento de los servidores, el almacenamiento y los equipos de telecomunicaciones que soportan la operación on-premise del CLIENTE, con un nivel de disponibilidad de infraestructura de 99,95%. El recinto se emplazará en el espacio físico que proporcione el CLIENTE, cuya ubicación y superficie se establecen en las Bases Técnicas del caso.

Las exigencias de este capítulo se aplican de manera proporcional a la escala del componente on-premise que el caso requiera:

| Tipología | Cuándo aplica | Exigencia |
| :--- | :--- | :--- |
| **Sala técnica principal** | El caso requiere cómputo, almacenamiento y procesamiento sustantivos en las instalaciones del CLIENTE. | Se aplican íntegramente los requisitos RT-06.01 a RT-06.24. |
| **Sala técnica secundaria o de sitio** | Sitios operacionales que requieren cómputo local para continuidad, pero no albergan el núcleo. | Se aplican los requisitos de energía, climatización, control de acceso, detección de incendio y monitoreo, dimensionados al sitio. |
| **Gabinete o borde operacional** | Puntos de operación con equipamiento mínimo: pórtico, muelle, sala de máquinas, sucursal, faena. | Se aplican los requisitos de protección eléctrica, control de acceso físico, monitoreo remoto y condiciones ambientales del equipo. |

El PROPONENTE deberá declarar expresamente qué tipología adopta en cada sitio del caso y justificar el dimensionamiento. Sobredimensionar el recinto es tan penalizado como subdimensionarlo: ambos revelan que el cálculo de capacidad no se hizo.

#### 6.2 Requisitos de obra y habilitación

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-06.01** | El espacio asignado será de uso exclusivo de la solución y estará aislado de otras dependencias del CLIENTE, con acceso independiente. | Obligatorio |
| **RT-06.02** | Los muros no estructurales del recinto contarán con blindaje perimetral; el PROPONENTE especificará el material y la resistencia. | Obligatorio |
| **RT-06.03** | El PROPONENTE entregará el plano de distribución interna del recinto, con la separación de las zonas de generadores, baterías, climatización, servidores, comunicaciones, trabajo y respaldo. | Obligatorio |
| **RT-06.04** | El piso técnico, la canalización, el cableado estructurado y el etiquetado se ejecutarán conforme a norma, con documentación de la certificación de cada enlace. | Obligatorio |
| **RT-06.05** | Los racks de servidores serán independientes de los racks de equipos de comunicación. Se declarará la ocupación proyectada de cada rack y su margen de crecimiento. | Obligatorio |
| **RT-06.06** | La obra civil de separación de las instalaciones es de cargo del CLIENTE; su especificación técnica y su coordinación son de cargo del PROPONENTE. | Obligatorio |

#### 6.3 Energía

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-06.07** | El suministro eléctrico de los equipos será ininterrumpido, con sistema de alimentación ininterrumpida dimensionado para una autonomía mínima de 30 minutos a plena carga. | Obligatorio |
| **RT-06.08** | La capacidad de generación autónoma asegurará un rango mínimo de 24 horas continuas de operación, con estanque de combustible dimensionado y contrato de reabastecimiento declarado. | Obligatorio |
| **RT-06.09** | La instalación eléctrica del recinto será independiente de la del resto del edificio y cumplirá la normativa eléctrica chilena vigente, incluida la NCh Elec. 2777 sobre sistemas de puesta a tierra. | Obligatorio |
| **RT-06.10** | Se efectuará revisión y medición semestral de las instalaciones eléctricas del recinto, con informe entregable al CLIENTE. | Obligatorio |
| **RT-06.11** | El PROPONENTE declarará la carga eléctrica proyectada en kW, el factor de potencia y la eficiencia en el uso de la energía (PUE) estimada del recinto. | Obligatorio |
| **RT-06.12** | Se valorará la redundancia de alimentación en configuración 2N o N+1 con doble acometida y transferencia automática. | Deseable |

#### 6.4 Climatización y condiciones ambientales

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-06.13** | El recinto contará con climatización de precisión para operación continua, redundante en configuración N+1, con control de temperatura y de humedad relativa dentro de los rangos que recomienda el fabricante del equipamiento. | Obligatorio |
| **RT-06.14** | Se monitorearán en línea la temperatura, la humedad y la presencia de agua, con alertamiento integrado a la plataforma de observabilidad. | Obligatorio |
| **RT-06.15** | El PROPONENTE declarará la estrategia de contención de pasillo frío o caliente y su efecto en la eficiencia energética. | Deseable |

#### 6.5 Detección y extinción de incendios

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-06.16** | El recinto contará con detección temprana por aspiración de aire con tecnología láser, tipo AnaLASER o equivalente de prestaciones iguales o superiores. | Obligatorio |
| **RT-06.17** | La extinción será automática mediante agente limpio tipo FM-200 o equivalente, con aprobación UL e instalación conforme a norma NFPA. | Obligatorio |
| **RT-06.18** | Se proveerá un sistema secundario de extintores portátiles habilitados, con mantención y certificación vigentes. | Obligatorio |
| **RT-06.19** | El sistema de detección y extinción se integrará al monitoreo en línea y notificará al NOC y a la contraparte del CLIENTE. | Obligatorio |

#### 6.6 Seguridad física y control de acceso

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-06.20** | El ingreso al recinto se controlará mediante seguridad física y control de acceso biométrico basado principalmente en biometría facial, con AFIS como respaldo. Se admite proponer sistemas de mayor seguridad. | Obligatorio |
| **RT-06.21** | Todo ingreso y egreso quedará registrado en una bitácora auditable, con identificación de la persona, fecha, hora y motivo, conservada por el período de retención declarado. | Obligatorio |
| **RT-06.22** | Entre el acceso principal y el término del pasillo de la zona de control se dispondrá un espacio para la atención de personas en proceso de enrolamiento. Se evaluará mejor la existencia de una estación de enrolamiento fuera de las instalaciones del recinto técnico. | Obligatorio |
| **RT-06.23** | Al término del pasillo se instalará un acceso que impida el paso de más de una persona a la vez, con nueva verificación de identidad previa al ingreso. | Obligatorio |
| **RT-06.24** | El recinto contará con videovigilancia y monitoreo IP, con imágenes en línea y disponibles para visualización de al menos los últimos 30 días. Las grabaciones anteriores se respaldarán en un medio secundario recuperable y auditable. | Obligatorio |
| **RT-06.25** | El PROPONENTE declarará el procedimiento de acceso de terceros —fabricantes, mantenedores, auditores— con acompañamiento obligatorio y registro. | Obligatorio |

#### 6.7 Respaldo y custodia de medios

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-06.26** | Se habilitará un servicio de custodia de medios de respaldo para el sitio primario, en un medio físico transportable a otro lugar cuando el CLIENTE lo determine. Se admite proponer una solución más segura y eficiente, debidamente justificada. | Obligatorio |
| **RT-06.27** | El recinto de custodia cumplirá exigencias de luminosidad, humedad, ventilación y cualquier otro factor que pueda afectar la calidad y la disponibilidad de los medios. | Obligatorio |
| **RT-06.28** | Se llevará un inventario de medios con rotación, verificación periódica de legibilidad y registro de todo movimiento de entrada y de salida. | Obligatorio |

#### 6.8 Espacio de operación del personal

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-06.29** | El PROPONENTE habilitará el espacio físico necesario para el personal encargado de la operación y administración de la plataforma, con estaciones de trabajo, telefonía, conexión a Internet y todo elemento que permita realizar la labor en condiciones adecuadas. | Obligatorio |
| **RT-06.30** | El espacio de operación estará separado de la sala de equipos y no requerirá el ingreso al recinto técnico para las labores habituales de operación. | Obligatorio |
| **RT-06.31** | Las instalaciones sanitarias, las zonas de seguridad ante emergencia y las áreas exteriores existentes en el edificio del CLIENTE podrán utilizarse y no deben implementarse nuevamente. El PROPONENTE declarará de cuáles hará uso. | Obligatorio |

#### 6.9 Rutas de comunicaciones

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-06.32** | El acceso a las redes de comunicaciones estará provisto a través de rutas físicas distintas, con ingreso al edificio por puntos separados. | Obligatorio |
| **RT-06.33** | El PROPONENTE proveerá toda la conectividad, la seguridad y las canalizaciones, cañerías o ductos requeridos para cumplir los niveles de servicio comprometidos. | Obligatorio |
| **RT-06.34** | Se privilegiará al PROPONENTE que ofrezca o provea especificaciones nuevas o mejores que las aquí establecidas, debidamente fundamentadas. | Deseable |

### CAPÍTULO 7: SITE SECUNDARIO Y RECUPERACIÓN ANTE DESASTRES

#### 7.1 Configuración exigida
Complementariamente al sitio principal, el PROPONENTE deberá habilitar un sitio secundario en dependencias distintas, en modalidad activo-activo o activo-pasivo, con replicación de datos en línea para el ambiente de producción y características tecnológicas equivalentes a las del sitio principal en lo que respecta a los servicios críticos.

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-07.01** | El PROPONENTE declarará la modalidad escogida —activo-activo o activo-pasivo— y la justificará frente al costo, al RTO comprometido y a la complejidad operacional que introduce. | Obligatorio |
| **RT-07.02** | El sitio secundario estará emplazado a una distancia suficiente del principal para no verse afectado por el mismo evento de fuerza mayor. El PROPONENTE declarará la distancia y el análisis de amenazas comunes considerado. | Obligatorio |
| **RT-07.03** | La replicación de datos será continua, con medición y alertamiento del retraso de replicación. | Obligatorio |
| **RT-07.04** | El objetivo de tiempo de recuperación (RTO) no superará 4 horas y el objetivo de punto de recuperación (RPO) no superará 15 minutos para los servicios críticos, salvo exigencia superior del caso. | Obligatorio |
| **RT-07.05** | El procedimiento de conmutación estará documentado, automatizado en la mayor medida posible y ejecutable por el personal del CLIENTE tras la transferencia de conocimiento. | Obligatorio |
| **RT-07.06** | Existirá un procedimiento de retorno al sitio principal igualmente documentado y probado, con reconciliación de los datos generados durante la contingencia. | Obligatorio |
| **RT-07.07** | El plan de recuperación ante desastres se probará al menos dos veces al año mediante conmutación real, con informe de resultados, medición del RTO y del RPO efectivamente alcanzados y plan de corrección de las brechas detectadas. | Obligatorio |
| **RT-07.08** | Se valorará que la conmutación sea automática ante la detección de indisponibilidad, con criterio de disparo declarado y protección contra conmutación innecesaria. | Deseable |

#### 7.2 Niveles de servicio de infraestructura

| Componente | Disponibilidad mensual mínima |
| :--- | :--- |
| Energía del recinto | 99,95% |
| Climatización | 99,95% |
| Red y comunicaciones | 99,95% |
| Servidores y cómputo | 99,95% |
| Motor de base de datos | 99,95% |
| Portal y canales de atención | 99,95% |
| Transacción de negocio crítica de extremo a extremo | 99,9% (Artículo 78° de las Bases Administrativas) |

> Los niveles de disponibilidad de infraestructura son un medio, no un fin. El compromiso contractual que se mide y se penaliza es el del Artículo 78º de las Bases Administrativas, sobre la transacción de negocio de extremo a extremo.

#### 7.3 Respaldos

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-07.09** | La política de respaldo seguirá el esquema 3-2-1-1-0: tres copias, en dos medios distintos, una fuera de sitio, una inmutable o fuera de línea y cero errores de verificación de restauración. | Obligatorio |
| **RT-07.10** | Los respaldos estarán cifrados en reposo y en tránsito, con clave gestionada de forma independiente de la infraestructura respaldada. | Obligatorio |
| **RT-07.11** | Las copias inmutables estarán protegidas contra borrado y contra modificación durante su período de retención, incluso frente a credenciales administrativas comprometidas. | Obligatorio |
| **RT-07.12** | Se ejecutará y documentará una prueba de restauración al menos mensual, sobre una muestra representativa, con medición del tiempo efectivo de restauración. | Obligatorio |
| **RT-07.13** | El PROPONENTE declarará, por cada dominio de datos, la frecuencia de respaldo, el período de retención y el tiempo estimado de restauración completa. | Obligatorio |
| **RT-07.14** | Los respaldos permitirán la restauración granular: un registro, una tabla, un módulo o el sistema completo. | Deseable |

### CAPÍTULO 8: HARDWARE, PUESTOS DE TRABAJO Y EQUIPAMIENTO DE TERRENO

#### 8.1 Infraestructura de cómputo, almacenamiento y red

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-08.01** | El PROPONENTE especificará el equipamiento de cómputo con su marca, modelo de referencia, procesador, memoria, almacenamiento local, interfaces y consumo, junto con el cálculo de dimensionamiento que lo sustenta. | Obligatorio |
| **RT-08.02** | El almacenamiento será redundante, con tolerancia declarada a la falla de discos, control de errores y monitoreo predictivo de salud de los medios. | Obligatorio |
| **RT-08.03** | Los conmutadores de núcleo, los cortafuegos y los balanceadores de carga estarán en configuración de alta disponibilidad, sin punto único de falla. | Obligatorio |
| **RT-08.04** | Todo el equipamiento contará con fuentes de poder redundantes y conexión a circuitos eléctricos distintos. | Obligatorio |
| **RT-08.05** | El PROPONENTE declarará el margen de crecimiento del dimensionamiento propuesto, expresado como porcentaje sobre la carga proyectada del caso, y el procedimiento de ampliación. | Obligatorio |
| **RT-08.06** | El equipamiento será nuevo, sin uso previo, con garantía de fábrica vigente desde la recepción conforme. | Obligatorio |

#### 8.2 Puestos de trabajo de operación y de back office

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-08.07** | El PROPONENTE especificará las estaciones de trabajo requeridas para la operación y la administración de la plataforma, en la cantidad que determine el dimensionamiento del caso, con monitores duales. | Obligatorio |
| **RT-08.08** | Los puestos de trabajo cumplirán las condiciones ergonómicas de la NCh 2527 y los equipos contarán con certificación de eficiencia energética. | Obligatorio |
| **RT-08.09** | Las estaciones estarán gestionadas de forma centralizada, con cifrado de disco, control de dispositivos extraíbles, antivirus con detección y respuesta y actualización automatizada. | Obligatorio |

#### 8.3 Equipamiento de terreno y dispositivos operacionales
Conforme al Artículo 14.2 de las Bases Administrativas, la especificación técnica del hardware de terreno es de cargo del PROPONENTE aunque su adquisición corresponda al CLIENTE.

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-08.10** | El PROPONENTE especificará cada dispositivo de terreno con marca, modelo de referencia, cantidad, características mínimas, accesorios, consumibles y costo unitario estimado, aun cuando su compra sea de cargo del CLIENTE. | Obligatorio |
| **RT-08.11** | La especificación considerará las condiciones reales de uso del caso: intemperie, humedad, polvo, vibración, temperatura, uso con guantes, luminosidad y autonomía de batería requerida por turno. | Obligatorio |
| **RT-08.12** | Los dispositivos declararán su grado de protección contra polvo y agua y su resistencia a caídas, coherentes con el entorno de operación. | Obligatorio |
| **RT-08.13** | El PROPONENTE indicará el ciclo de vida esperado de cada dispositivo, la disponibilidad de repuestos y el plan de reposición durante los 56 meses del Contrato. | Obligatorio |
| **RT-08.14** | Los dispositivos se integrarán a la gestión centralizada de flota exigida en RT-03.18. | Obligatorio |
| **RT-08.15** | El PROPONENTE proveerá una unidad de cada tipo de dispositivo especificado para pruebas de aceptación por parte del CLIENTE, antes de la compra masiva. | Deseable |

#### 8.4 Garantías, repuestos y niveles de reemplazo

| Elemento | Exigencia mínima |
| :--- | :--- |
| **Hardware crítico** | Soporte 24x7 con atención en sitio y compromiso de resolución en 4 horas. |
| **Hardware no crítico** | Soporte en horario hábil con compromiso de resolución en 24 horas. |
| **Software de base y de plataforma** | Soporte continuo del fabricante durante todo el período contractual. |
| **Stock de repuestos** | Al menos 10% del parque instalado por tipo de componente crítico, disponible en Chile. |
| **Reemplazo de componente crítico en falla** | Máximo 4 horas desde la confirmación del diagnóstico. |
| **Dispositivos de terreno** | Stock de reemplazo en sitio equivalente al 10% del parque, con configuración precargada. |

#### 8.5 Ciclo de vida y disposición final

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-08.16** | El PROPONENTE presentará el plan de ciclo de vida del equipamiento: recepción, puesta en servicio, mantención, actualización, retiro y disposición final. | Obligatorio |
| **RT-08.17** | Todo medio de almacenamiento que salga de servicio será borrado de forma segura y verificable, con certificado de destrucción o de sanitización entregado al CLIENTE. | Obligatorio |
| **RT-08.18** | La disposición final de equipamiento electrónico se realizará con gestor autorizado, conforme a la normativa de residuos aplicable, con certificado de disposición. | Obligatorio |
| **RT-08.19** | Se valorará una estrategia de reacondicionamiento o de extensión de vida útil que reduzca el impacto ambiental, cuantificada en la propuesta. | Deseable |

---

## TÍTULO IV: REQUISITOS NO FUNCIONALES

### CAPÍTULO 9: DESEMPEÑO, CAPACIDAD Y ESCALABILIDAD

#### 9.1 Umbrales de desempeño
Los siguientes umbrales son exigibles en producción, medidos en el percentil 95 sobre la experiencia real de la persona usuaria y bajo la carga de peak declarada en las Bases Técnicas del caso.

| Indicador | Umbral máximo |
| :--- | :--- |
| Carga inicial de una página del portal | 2 segundos |
| Navegación entre vistas ya cargadas | 1 segundo |
| Respuesta de una interfaz de programación de consulta simple | 500 ms |
| Respuesta de una interfaz de programación de escritura transaccional | 800 ms |
| Transacción operacional crítica de terreno, de extremo a extremo | Definido por el caso; en su defecto, 3 segundos |
| Búsqueda con criterios compuestos | 3 segundos |
| Generación de un informe estándar en línea | 30 segundos |
| Procesamiento por lotes | 10.000 registros por minuto |
| Carga de un archivo de 100 MB | 60 segundos |
| Tiempo de arranque en frío de un servicio | 60 segundos |

#### 9.2 Requisitos de capacidad y escalabilidad

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-09.01** | El PROPONENTE presentará el cálculo de capacidad que sustenta su dimensionamiento, con los supuestos de usuarios concurrentes, transacciones por segundo, volumen de datos y crecimiento anual, tomados de la volumetría del caso. | Obligatorio |
| **RT-09.02** | La solución soportará la concurrencia y el volumen de transacciones que fije el caso, y mantendrá los umbrales del numeral 9.1 bajo esa carga. | Según caso |
| **RT-09.03** | La solución soportará, sin rediseño, un crecimiento de al menos tres veces la volumetría inicial del caso en un horizonte de tres años. | Obligatorio |
| **RT-09.04** | El escalamiento de las capas de aplicación e integración será horizontal y automático, con tiempo de reacción declarado y sin pérdida de transacciones en curso. | Obligatorio |
| **RT-09.05** | EL PROPONENTE identificará el componente que primero se convertirá en cuello de botella al crecer la carga y explicará cómo lo detectará y cómo lo resolverá. | Obligatorio |
| **RT-09.06** | Se ejecutarán pruebas de carga sobre Preproducción con un volumen equivalente a 1,5 veces el peak declarado, y pruebas de estrés hasta identificar el punto de quiebre de la solución. | Obligatorio |
| **RT-09.07** | El informe de pruebas de carga incluirá la curva de tiempo de respuesta frente a carga, el punto de saturación, el consumo de recursos y el comportamiento durante y después del peak. | Obligatorio |
| **RT-09.08** | La solución degradará de forma controlada al superarse la capacidad: encolamiento, limitación de tasa y mensaje explícito a la persona usuaria, nunca error genérico ni pérdida silenciosa de transacciones. | Obligatorio |
| **RT-09.09** | Se gestionará la capacidad durante la Operación con proyección trimestral de crecimiento, alertas anticipadas de agotamiento y propuesta de ajuste de dimensionamiento y de costo. | Obligatorio |
| **RT-09.10** | Se valorará la existencia de pruebas de carga automatizadas ejecutadas de forma periódica en el flujo de integración continua, con detección de regresiones de desempeño. | Deseable |

### CAPÍTULO 10: DISPONIBILIDAD, CONTINUIDAD Y RESILIENCIA

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-10.01** | La solución alcanzará una disponibilidad mensual mínima de 99,9% para los servicios clasificados como críticos, medida sobre la transacción de negocio de extremo a extremo. | Obligatorio |
| **RT-10.02** | El PROPONENTE clasificará cada servicio de la solución en crítico, alto, medio o bajo, justificando la clasificación con el impacto operacional de su indisponibilidad, y aplicará a cada uno el nivel de servicio correspondiente del Artículo 78° de las Bases Administrativas. | Obligatorio |
| **RT-10.03** | El plan de continuidad del negocio se elaborará conforme a ISO 22301, con análisis de impacto en el negocio, escenarios de contingencia, procedimientos manuales de respaldo y criterios de activación. | Obligatorio |
| **RT-10.04** | La continuidad TIC se estructurará conforme a ISO/IEC 27031, articulada con el plan de recuperación ante desastres del Capítulo 7. | Obligatorio |
| **RT-10.05** | Los mantenimientos programados se ejecutarán fuera de la ventana operacional crítica que defina el caso, con aviso previo mínimo de diez días hábiles. | Según caso |
| **RT-10.06** | La solución permitirá desplegar cambios sin interrupción del servicio. Las ventanas de indisponibilidad programada serán excepcionales y deberán justificarse caso a caso. | Obligatorio |
| **RT-10.07** | Se ejecutarán pruebas de resiliencia mediante inyección controlada de fallas —caída de instancia, de zona, de dependencia externa, latencia elevada, saturación de disco— antes de cada paso a producción y al menos una vez por semestre durante la Operación. | Obligatorio |
| **RT-10.08** | El PROPONENTE documentará, por cada dependencia externa, el comportamiento de la solución cuando esa dependencia no responde, responde con error o responde con lentitud. | Obligatorio |
| **RT-10.09** | Se declarará un presupuesto de error por servicio crítico y su vinculación con el ritmo de despliegue de cambios. | Deseable |

### CAPÍTULO 11: SEGURIDAD DE LA INFORMACIÓN

#### 11.1 Gobierno y modelo de seguridad

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-11.01** | La arquitectura de seguridad se basará en el modelo Zero Trust conforme a NIST SP 800-207: verificación explícita de cada solicitud, privilegio mínimo y presunción de compromiso. | Obligatorio |
| **RT-11.02** | El PROPONENTE entregará un modelado de amenazas documentado por cada componente y por cada integración externa, con metodología declarada (STRIDE u otra), y lo actualizará ante cada cambio arquitectónico relevante. | Obligatorio |
| **RT-11.03** | La información del CLIENTE se clasificará por nivel de sensibilidad, con controles diferenciados por nivel documentados en una matriz. | Obligatorio |
| **RT-11.04** | Existirá un programa de gestión de vulnerabilidades con escaneo continuo y plazos máximos de remediación de 7 días corridos para vulnerabilidades críticas, 15 días para altas y 30 días para medias, contados desde su publicación o detección. | Obligatorio |
| **RT-11.05** | El PROPONENTE mantendrá una matriz de controles de seguridad trazable a ISO/IEC 27001 e ISO/IEC 27002, indicando el control, su implementación concreta en la solución y la evidencia que lo acredita. | Obligatorio |
| **RT-11.06** | Se aplicarán los controles de ISO/IEC 27017 para los servicios en nube y de ISO/IEC 27018 para el tratamiento de datos personales en nube. | Obligatorio |

#### 11.2 Protección de la capa expuesta

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-11.07** | La publicación de servicios se realizará exclusivamente a través de la capa de borde, con red de distribución de contenidos, cortafuegos de aplicaciones web con reglas gestionadas y personalizadas, y protección contra denegación de servicio distribuida en capas 3, 4 y 7. | Obligatorio |
| **RT-11.08** | El cifrado en tránsito empleará TLS 1.3, con prohibición expresa de TLS 1.0 y 1.1, conjuntos de cifrado modernos, HSTS con precarga y gestión automatizada de certificados con rotación y alerta anticipada de vencimiento. | Obligatorio |
| **RT-11.09** | La totalidad de los datos en reposo estará cifrada, con claves gestionadas en un servicio de gestión de claves o en un módulo de seguridad de hardware, política de rotación declarada y separación de funciones en la custodia de claves. | Obligatorio |
| **RT-11.10** | Los datos de categoría sensible que el caso identifique se cifrarán adicionalmente a nivel de campo, de modo que el acceso a la base de datos no revele su contenido. | Según caso |
| **RT-11.11** | La puerta de enlace de servicios aplicará autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil. | Obligatorio |
| **RT-11.12** | Los puntos de entrada públicos contarán con protección contra bots y abuso automatizado, con reto progresivo que no degrade la accesibilidad ni bloquee a personas usuarias legítimas. | Obligatorio |
| **RT-11.13** | El PROPONENTE declarará la superficie de exposición completa de la solución: cada nombre de dominio, puerto y servicio alcanzable desde fuera de la red del CLIENTE. | Obligatorio |

#### 11.3 Detección, respuesta y evidencia

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-11.14** | Los eventos de seguridad se registrarán de forma centralizada e inalterable, con retención mínima de doce meses en línea y veinticuatro meses adicionales en archivo recuperable. | Obligatorio |
| **RT-11.15** | Los eventos se correlacionarán en una plataforma SIEM, con casos de uso de detección definidos específicamente para el proceso de negocio del caso, y no sólo genéricos de infraestructura. | Obligatorio |
| **RT-11.16** | Se implementará detección y respuesta en puntos finales y en cargas de trabajo, tanto en nube como on-premise. | Obligatorio |
| **RT-11.17** | El PROPONENTE dispondrá de un centro de operaciones de seguridad con cobertura 24x7, propio o subcontratado, y declarará su ubicación, dotación y procedimientos. | Obligatorio |
| **RT-11.18** | El plan de respuesta a incidentes de seguridad definirá clasificación, cadena de escalamiento, plazos, responsables y protocolo de comunicación al CLIENTE dentro de las dos horas de detectado un incidente de severidad crítica. | Obligatorio |
| **RT-11.19** | Toda brecha de seguridad o de datos personales se notificará al CLIENTE dentro de las 24 horas de su detección, con informe preliminar, y el análisis de causa raíz se entregará dentro de los cinco días hábiles siguientes. | Obligatorio |
| **RT-11.20** | Se ejecutarán pruebas de intrusión por un tercero independiente del ADJUDICATARIO, anualmente y antes de cada paso a producción, con entrega íntegra del informe al CLIENTE y plan de remediación con plazos. | Obligatorio |
| **RT-11.21** | Se realizarán ejercicios de simulación de incidente con participación del CLIENTE al menos una vez al año durante la Operación. | Deseable |

#### 11.4 Seguridad del ciclo de desarrollo y de la cadena de suministro

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-11.22** | El flujo de integración continua incorporará análisis estático de código, análisis de composición de software, análisis dinámico y escaneo de imágenes de contenedor, con criterios de bloqueo automático del despliegue ante hallazgos críticos. | Obligatorio |
| **RT-11.23** | Cada versión liberada se acompañará de su inventario de componentes de software en formato CycloneDX o SPDX, entregado al CLIENTE. | Obligatorio |
| **RT-11.24** | Los artefactos se firmarán y su procedencia se verificará conforme a SLSA nivel 3 o superior. | Obligatorio |
| **RT-11.25** | Queda prohibido el uso de datos productivos reales en ambientes no productivos sin anonimización o seudonimización verificable. | Obligatorio |
| **RT-11.26** | El PROPONENTE declarará el proceso de aprobación de nuevas dependencias de terceros, incluyendo criterios de licencia, mantención activa y ausencia de vulnerabilidades conocidas. | Obligatorio |
| **RT-11.27** | Las personas desarrolladoras no tendrán acceso interactivo directo al ambiente de producción. Todo acceso excepcional será temporal, aprobado, registrado y con sesión grabada. | Obligatorio |
| **RT-11.28** | Se aplicará el marco OWASP SAMM o equivalente para medir y mejorar la madurez del proceso de desarrollo seguro, con evaluación inicial y reevaluación anual. | Deseable |

#### 11.5 Certificaciones y estándares de seguridad exigidos

| Ámbito | Estándar |
| :--- | :--- |
| **Sistema de gestión de seguridad** | ISO/IEC 27001 e ISO/IEC 27002 |
| **Servicios en nube** | ISO/IEC 27017 |
| **Datos personales en nube** | ISO/IEC 27018 |
| **Marco de ciberseguridad** | NIST Cybersecurity Framework 2.0 |
| **Arquitectura de confianza cero** | NIST SP 800-207 |
| **Seguridad de aplicaciones** | OWASP ASVS 4.0 nivel 2 como mínimo; OWASP Top 10 y OWASP API Security Top 10 |
| **Endurecimiento de sistemas** | CIS Benchmarks del producto correspondiente |
| **Cadena de suministro de software** | SLSA nivel 3 o superior |
| **Continuidad** | ISO 22301 e ISO/IEC 27031 |
| **Normativa nacional** | Leyes N° 21.719, N° 21.663, N° 21.459 y N° 19.799, según aplicabilidad al caso |

### CAPÍTULO 12: IDENTIDAD, ACCESO Y GESTIÓN DE SESIONES

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-12.01** | La gestión de identidad será centralizada, con federación mediante OpenID Connect y OAuth 2.1, o SAML 2.0 cuando la integración con el CLIENTE lo requiera, e integración con el directorio corporativo del CLIENTE por LDAP o su equivalente en la nube. | Obligatorio |
| **RT-12.02** | Existirá inicio de sesión único para todos los módulos de la solución, con cierre de sesión propagado a todos ellos. | Obligatorio |
| **RT-12.03** | La autenticación multifactor será obligatoria para personas usuarias administradoras, para todo acceso privilegiado y para todo acceso originado fuera de la red corporativa. | Obligatorio |
| **RT-12.04** | Se soportarán factores resistentes a la suplantación de identidad, tipo FIDO2 o claves de acceso, al menos para los perfiles administradores. | Deseable |
| **RT-12.05** | El control de acceso será basado en roles, complementado con control basado en atributos donde el proceso lo exija, con matriz de segregación de funciones documentada y verificable. | Obligatorio |
| **RT-12.06** | Los accesos privilegiados se gestionarán con elevación temporal a demanda, aprobación previa y grabación de sesión para las operaciones de mayor riesgo. | Obligatorio |
| **RT-12.07** | La política de sesión declarará duración máxima, caducidad por inactividad, renovación de la credencial de sesión tras la autenticación, revocación inmediata y control de sesiones concurrentes. | Obligatorio |
| **RT-12.08** | Las credenciales de sesión serán firmadas y de vida breve, con credencial de refresco rotatoria. Queda prohibido transportar identificadores de sesión en la ruta de la dirección web. | Obligatorio |
| **RT-12.09** | Se registrará auditoría completa del ciclo de vida de la identidad: creación, modificación, elevación, bloqueo y baja de cuentas, con no repudio y retención declarada. | Obligatorio |
| **RT-12.10** | El aprovisionamiento y el desaprovisionamiento estarán automatizados y ligados al ciclo de vida laboral, con baja efectiva en un plazo no superior a 24 horas desde la desvinculación. | Obligatorio |
| **RT-12.11** | El mecanismo de autenticación se adecuará al perfil operacional real descrito en el caso: entornos de terreno, uso con guantes, baja alfabetización digital, dispositivos compartidos por turno y ausencia de correo electrónico personal. | Según caso |
| **RT-12.12** | Las personas usuarias externas del CLIENTE —clientes, proveedores, pacientes, productores, según el caso— dispondrán de un mecanismo de registro, verificación de identidad y recuperación de acceso autoservido y seguro. | Según caso |
| **RT-12.13** | El PROPONENTE declarará el procedimiento de acceso de emergencia (cuenta de último recurso), su custodia, su control y su auditoría. | Obligatorio |

### CAPÍTULO 13: USABILIDAD, ACCESIBILIDAD Y EXPERIENCIA DE USUARIO

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-13.01** | Todas las interfaces destinadas a personas usuarias cumplirán WCAG 2.2 nivel AA, verificado con herramientas automatizadas y con pruebas manuales, con informe de conformidad entregable. | Obligatorio |
| **RT-13.02** | El diseño será responsivo y funcionará correctamente en escritorio, tableta y teléfono, con puntos de quiebre coherentes y adaptación inteligente del contenido, no simple reducción. | Obligatorio |
| **RT-13.03** | El PROPONENTE ejecutará investigación con personas usuarias reales del CLIENTE, prototipado y pruebas de usabilidad antes de la construcción definitiva, y documentará los hallazgos y los cambios de diseño que produjeron. | Obligatorio |
| **RT-13.04** | Se comprometerán indicadores de usabilidad medibles: tiempo máximo de la transacción operacional crítica, número máximo de pasos, tasa de error tolerada y tiempo de aprendizaje esperado por perfil. | Obligatorio |
| **RT-13.05** | Ninguna funcionalidad principal requerirá más de tres interacciones desde la pantalla de inicio del perfil correspondiente. | Obligatorio |
| **RT-13.06** | La solución entregará retroalimentación visual clara ante cada acción, manejará los errores de forma comprensible —indicando qué ocurrió y qué hacer— y evitará mensajes técnicos dirigidos a la persona usuaria final. | Obligatorio |
| **RT-13.07** | La solución soportará a personas usuarias con baja alfabetización digital: alto contraste, objetivos táctiles de al menos 44x44 píxeles, iconografía acompañada de texto, y flujos guiados paso a paso. | Obligatorio |
| **RT-13.08** | Cuando el caso lo requiera, las interfaces de terreno operarán con guantes, a la intemperie, con luminosidad variable y sin conexión. | Según caso |
| **RT-13.09** | Existirá un sistema de diseño documentado con paleta de colores acotada, jerarquía tipográfica de a lo más dos familias, iconografía coherente, retícula y componentes reutilizables. | Obligatorio |
| **RT-13.10** | El PROPONENTE declarará la matriz de navegadores y de versiones soportadas y su política de actualización. | Obligatorio |
| **RT-13.11** | La solución será navegable íntegramente por teclado, con orden de foco lógico y atajos para las operaciones frecuentes. | Obligatorio |
| **RT-13.12** | Se valorará el soporte de modo oscuro, de personalización de la interfaz por persona usuaria y de múltiples idiomas cuando el caso lo justifique. | Deseable |

### CAPÍTULO 14: OBSERVABILIDAD Y GESTIÓN DEL SERVICIO

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-14.01** | La observabilidad será unificada para nube y on-premise, con métricas, registros y trazas distribuidas correlacionadas por un identificador único de transacción, instrumentadas conforme a OpenTelemetry. | Obligatorio |
| **RT-14.02** | El CLIENTE dispondrá de acceso propio y permanente a los tableros operacionales y de negocio, con datos en tiempo real y capacidad de exportación. | Obligatorio |
| **RT-14.03** | Los indicadores de nivel de servicio se medirán sobre la experiencia real de la persona usuaria y no sobre pruebas sintéticas, sin perjuicio de que estas se empleen como complemento. | Obligatorio |
| **RT-14.04** | El alertamiento se basará en síntomas de negocio y no sólo en umbrales de infraestructura, con supresión de ruido, agrupación, escalamiento automático y turnos de disponibilidad declarados. | Obligatorio |
| **RT-14.05** | Existirá un libro de operación y una guía de resolución documentados para cada escenario de falla previsible, con automatización progresiva de las tareas repetitivas. | Obligatorio |
| **RT-14.06** | Todo incidente crítico dará lugar a un análisis de causa raíz obligatorio, con informe entregable dentro de cinco días hábiles y seguimiento de las acciones correctivas hasta su cierre. | Obligatorio |
| **RT-14.07** | Los registros de la solución no contendrán datos personales sensibles ni credenciales, y su acceso estará controlado y auditado. | Obligatorio |
| **RT-14.08** | El PROPONENTE declarará la retención de métricas, registros y trazas, y su costo asociado, distinguiendo el almacenamiento en línea del archivado. | Obligatorio |
| **RT-14.09** | Se valorará la detección proactiva de anomalías mediante análisis del comportamiento histórico, con alerta antes de que el incidente afecte a la operación. | Deseable |

### CAPÍTULO 15: SOSTENIBILIDAD, EFICIENCIA Y CERTIFICACIONES

#### 15.1 Sostenibilidad y eficiencia energética

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-15.01** | El PROPONENTE dimensionará la infraestructura ajustada a la demanda real, evitando capacidad ociosa permanente, y declarará el factor de utilización proyectado. | Obligatorio |
| **RT-15.02** | Los ambientes no productivos se apagarán o reducirán fuera del horario de uso. | Obligatorio |
| **RT-15.03** | El PROPONENTE estimará la huella de carbono anual de la operación de la solución y declarará la metodología empleada. | Obligatorio |
| **RT-15.04** | Se declarará la eficiencia en el uso de la energía (PUE) del recinto on-premise y la intensidad de carbono de la región de nube escogida. | Obligatorio |
| **RT-15.05** | Se valorará la elección de regiones de nube con menor intensidad de carbono cuando la latencia y la regulación lo permitan, con el análisis comparativo correspondiente. | Deseable |
| **RT-15.06** | Se valorará la definición de metas de reducción del consumo durante la Operación, con medición y reporte anual. | Deseable |

#### 15.2 Certificaciones institucionales exigidas

| Certificación | Carácter | Plazo |
| :--- | :--- | :--- |
| **ISO/IEC 27001 - Seguridad de la información** | Obligatoria | Vigente a la fecha de la oferta o plan de certificación con hitos verificables dentro de los primeros 12 meses del Contrato. |
| **ISO 9001 - Gestión de la calidad** | Obligatoria | Vigente a la fecha de la oferta. |
| **ISO/IEC 20000-1 - Gestión de servicios de TI** | Deseable | Vigente o plan declarado. |
| **ISO 22301 - Continuidad del negocio** | Deseable | Vigente o plan declarado. |
| **ISO/IEC 42001 - Gestión de inteligencia artificial** | Deseable | Exigible sólo si la solución incorpora componentes de IA. |
| **Certificación sectorial específica** | Según caso | La que identifiquen las Bases Técnicas del caso. |

#### 15.3 Certificaciones del personal
El equipo propuesto acreditará, como mínimo, las siguientes certificaciones individuales vigentes. Una misma persona puede acreditar más de una, pero no puede contarse dos veces para el mismo requisito.

| Certificación o competencia | Cantidad mínima |
| :--- | :--- |
| **Gestión de proyectos (PMP, PRINCE2 o equivalente)** | 2 personas |
| **Gestión de servicios (ITIL 4 Foundation o superior)** | 5 personas |
| **Gobierno de TI (COBIT o equivalente)** | 2 personas |
| **Arquitectura de nube del proveedor ofertado, nivel profesional o de arquitecto** | 3 personas |
| **Seguridad de la información (CISSP, CISM, CEH, OSCP o equivalente)** | 2 personas |
| **Bases de datos del motor ofertado** | 2 personas |
| **Calidad y pruebas de software (ISTQB o equivalente)** | 2 personas |

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-15.07** | Las certificaciones se acreditarán con copia del certificado vigente y con el código de verificación del organismo emisor cuando exista. | Obligatorio |
| **RT-15.08** | Las personas certificadas formarán parte del equipo efectivamente asignado al PROYECTO, con dedicación declarada. No se aceptará acreditar personal que no participe. | Obligatorio |
| **RT-15.09** | El ADJUDICATARIO mantendrá vigentes estas certificaciones durante todo el período contractual y las repondrá ante la salida de una persona certificada, conforme al Artículo 76° de las Bases Administrativas. | Obligatorio |

---

## TÍTULO V: CAPACIDADES TRANSVERSALES DE LA SOLUCIÓN
Los módulos y capacidades de este Título son exigibles en las trece industrias. No son el negocio del caso —eso lo definen las Bases Técnicas respectivas— sino la infraestructura funcional sin la cual ninguna plataforma de misión crítica es operable, auditable ni administrable.

### CAPÍTULO 16: MÓDULOS TRANSVERSALES OBLIGATORIOS

#### 16.1 Administración y parametrización

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-16.01** | La solución dispondrá de un módulo de administración que permita al CLIENTE, sin intervención del ADJUDICATARIO, gestionar personas usuarias, roles, permisos, unidades organizacionales y sus jerarquías. | Obligatorio |
| **RT-16.02** | Las reglas de negocio parametrizables —umbrales, plazos, montos, tolerancias, catálogos, listas de valores, textos de notificación— serán configurables desde la interfaz de administración, con control de versiones y registro de quién cambió qué y cuándo. | Obligatorio |
| **RT-16.03** | Todo cambio de parámetro con impacto operacional requerirá aprobación de un segundo perfil y quedará registrado con su justificación. | Obligatorio |
| **RT-16.04** | El PROPONENTE declarará expresamente qué elementos son parametrizables y cuáles requieren desarrollo. Presentar como parametrizable lo que exige desarrollo se evaluará como observación grave. | Obligatorio |
| **RT-16.05** | Existirá un ambiente de simulación que permita probar el efecto de un cambio de parámetro antes de aplicarlo a producción. | Deseable |

#### 16.2 Auditoría y trazabilidad

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-16.06** | Toda operación que cree, modifique o elimine información quedará registrada con identificación de la persona o del sistema que la ejecutó, fecha y hora con zona horaria, origen, valores anteriores y valores posteriores. | Obligatorio |
| **RT-16.07** | El registro de auditoría será inalterable y no podrá ser modificado ni eliminado por ningún perfil, incluido el administrador de la plataforma. | Obligatorio |
| **RT-16.08** | El CLIENTE podrá consultar y exportar la auditoría desde la interfaz, con filtros por persona, período, entidad y tipo de operación, sin requerir acceso a la base de datos. | Obligatorio |
| **RT-16.09** | Las consultas a información sensible quedarán registradas, no sólo las modificaciones. | Según caso |
| **RT-16.10** | El período de retención de la auditoría será el que fije el caso y, en su defecto, no inferior a cinco años. | Según caso |

#### 16.3 Flujos de trabajo y motor de reglas

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-16.11** | La solución soportará flujos de trabajo con estados, transiciones, responsables, plazos, escalamiento automático por vencimiento y delegación por ausencia. | Obligatorio |
| **RT-16.12** | Los flujos serán configurables por el CLIENTE sin desarrollo, al menos en lo relativo a responsables, plazos y niveles de aprobación. | Obligatorio |
| **RT-16.13** | Toda solicitud pendiente será visible para su responsable en una bandeja de tareas unificada, con priorización y alerta de vencimiento. | Obligatorio |
| **RT-16.14** | El motor de reglas permitirá definir condiciones de negocio evaluables sin recompilación, con trazabilidad de qué regla se aplicó a cada transacción. | Deseable |

#### 16.4 Gestión documental y firma electrónica

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-16.15** | La solución gestionará documentos con versionado, metadatos, control de acceso, búsqueda por contenido y por metadato, y previsualización sin descarga. | Obligatorio |
| **RT-16.16** | Los documentos se almacenarán cifrados, con verificación de integridad y retención conforme a la política del caso. | Obligatorio |
| **RT-16.17** | La solución soportará firma electrónica conforme a la Ley N° 19.799, con firma avanzada para los actos que el caso lo requiera, y verificación de validez del certificado al momento de la firma. | Según caso |
| **RT-16.18** | Se generará el sello de tiempo y se conservará la evidencia de firma que permita verificar el documento con posterioridad al vencimiento del certificado. | Según caso |
| **RT-16.19** | La solución generará documentos a partir de plantillas administrables por el CLIENTE, con datos de la transacción y salida en formato abierto. | Obligatorio |

#### 16.5 Notificaciones y mensajería multicanal

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-16.20** | La solución enviará notificaciones por al menos tres canales: correo electrónico, notificación en la aplicación y mensajería instantánea o SMS, según lo que el caso requiera. | Obligatorio |
| **RT-16.21** | Las plantillas de notificación serán administrables por el CLIENTE, con variables de la transacción, y versionadas. | Obligatorio |
| **RT-16.22** | Cada persona usuaria podrá configurar sus preferencias de canal y de frecuencia, respetando las notificaciones que el CLIENTE defina como obligatorias. | Obligatorio |
| **RT-16.23** | El envío será asíncrono, con reintento ante falla, control de duplicados y registro de entrega, apertura y error por cada mensaje. | Obligatorio |
| **RT-16.24** | El PROPONENTE declarará el proveedor de cada canal, su costo unitario, su volumen proyectado y el tratamiento del costo variable en la Oferta Económica. | Obligatorio |
| **RT-16.25** | Las notificaciones respetarán la normativa de comunicaciones comerciales y permitirán la baja cuando corresponda. | Obligatorio |
| **RT-16.26** | Se valorará la integración con canales conversacionales que permitan a la persona usuaria responder y ejecutar acciones desde el propio canal. | Deseable |

#### 16.6 Búsqueda, reportería y exportación

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-16.27** | La solución dispondrá de búsqueda global con indexación de texto completo, tolerancia a errores de escritura, filtros facetados y respeto del control de acceso de la persona que busca. | Obligatorio |
| **RT-16.28** | Los listados serán ordenables, filtrables, paginados y exportables en formatos abiertos, con el filtro aplicado reflejado en la exportación. | Obligatorio |
| **RT-16.29** | Las exportaciones de gran volumen se procesarán de forma asíncrona, con notificación al completarse y sin bloquear la sesión. | Obligatorio |
| **RT-16.30** | Toda exportación de información sensible quedará registrada en la auditoría, con identificación de quién exportó qué y cuándo. | Obligatorio |

#### 16.7 Portal público y canales de autoatención

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-16.31** | La solución dispondrá de un portal público con la información que el caso determine, accesible sin autenticación, con los mismos estándares de accesibilidad y desempeño que el resto de la plataforma. | Según caso |
| **RT-16.32** | Las personas usuarias externas dispondrán de autoatención para las consultas de mayor frecuencia, evitando el contacto telefónico para operaciones simples. | Obligatorio |
| **RT-16.33** | El PROPONENTE estimará la reducción esperada del volumen de atención asistida por efecto de la autoatención y comprometerá el indicador. | Obligatorio |
| **RT-16.34** | El portal público resistirá picos de tráfico sin degradar los servicios transaccionales internos, mediante aislamiento de recursos y caché. | Obligatorio |

### CAPÍTULO 17: CANALES DIGITALES Y MOVILIDAD

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-17.01** | La solución proveerá una aplicación móvil para los perfiles operacionales que el caso identifique, con funcionamiento sin conexión y sincronización diferida cuando la operación en terreno lo requiera. | Según caso |
| **RT-17.02** | El PROPONENTE declarará si la aplicación es nativa, híbrida o web progresiva, y justificará la decisión frente al requisito de operación desconectada, al acceso a periféricos y al costo de mantención. | Obligatorio |
| **RT-17.03** | La aplicación soportará las versiones de sistema operativo móvil vigentes y las dos anteriores, con política de actualización declarada. | Obligatorio |
| **RT-17.04** | La aplicación se distribuirá por las tiendas oficiales o mediante gestión de flota corporativa, con firma de la aplicación y verificación de integridad. | Obligatorio |
| **RT-17.05** | La información almacenada en el dispositivo estará cifrada, con borrado remoto y bloqueo ante pérdida o desvinculación de la persona usuaria. | Obligatorio |
| **RT-17.06** | La aplicación integrará los periféricos que el caso requiera: cámara, lector de códigos, NFC, GPS, impresora de etiquetas, balanza o báscula. | Según caso |
| **RT-17.07** | El consumo de datos móviles y de batería se optimizará y se declarará el consumo estimado por turno de trabajo. | Obligatorio |
| **RT-17.08** | Se valorará la disponibilidad de una versión de la interfaz para dispositivos de bajo costo o de generaciones anteriores, ampliando la cobertura de personas usuarias. | Deseable |

### CAPÍTULO 18: INTELIGENCIA ARTIFICIAL Y AUTOMATIZACIÓN
La incorporación de inteligencia artificial no es obligatoria. Sí lo es, cuando el PROPONENTE la incorpore, cumplir íntegramente los requisitos de este capítulo. Una capacidad de inteligencia artificial mal gobernada es un riesgo, no una ventaja competitiva.

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-18.01** | El PROPONENTE declarará cada componente de inteligencia artificial: propósito, modelo o servicio empleado, proveedor, versión y ubicación de procesamiento de los datos. | Obligatorio |
| **RT-18.02** | Se garantizará contractualmente que los datos del CLIENTE no serán utilizados para entrenar modelos de terceros, salvo autorización expresa y escrita. | Obligatorio |
| **RT-18.03** | Se documentarán los límites de uso, los casos en que el resultado requiere validación humana previa y el procedimiento de supervisión. | Obligatorio |
| **RT-18.04** | Los riesgos de sesgo, alucinación, fuga de información y uso indebido se evaluarán y mitigarán conforme al NIST AI Risk Management Framework 1.0 y a la norma ISO/IEC 42001. | Obligatorio |
| **RT-18.05** | Toda interacción relevante con un componente de inteligencia artificial quedará registrada para efectos de auditoría y trazabilidad, incluyendo la entrada, la salida y la decisión humana posterior. | Obligatorio |
| **RT-18.06** | El componente podrá desactivarse sin comprometer la operación del resto de la solución, y existirá un procedimiento manual de respaldo para la función que automatiza. | Obligatorio |
| **RT-18.07** | Cuando el resultado se presente a una persona usuaria, se indicará expresamente que fue generado o sugerido de forma automática, y su nivel de confianza cuando el modelo lo provea. | Obligatorio |
| **RT-18.08** | Los modelos predictivos declararán sus variables de entrada, su métrica de desempeño, su línea base y su plan de reentrenamiento y de detección de deriva. | Obligatorio |
| **RT-18.09** | La responsabilidad por los resultados de los componentes de inteligencia artificial recae íntegramente en el ADJUDICATARIO, conforme al Artículo 86° de las Bases Administrativas. | Obligatorio |
| **RT-18.10** | Se valorará el uso de automatización robótica de procesos o de agentes para tareas repetitivas de back office, con el ahorro de horas cuantificado y reflejado en la Oferta Económica. | Deseable |

> Incorporar un modelo de lenguaje a la solución sin declarar dónde se procesan los datos, sin control de acceso a la información que consulta y sin validación humana de sus resultados será evaluado como incumplimiento de los requisitos de seguridad, no como innovación.

---

## TÍTULO VI: PROYECTO, IMPLANTACIÓN Y OPERACIÓN

### CAPÍTULO 19: ESTRUCTURA Y GOBIERNO DEL PROYECTO

#### 19.1 Oficina de gestión y metodología

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-19.01** | El ADJUDICATARIO constituirá una oficina de gestión del proyecto con metodología declarada, basada en el PMBOK del Project Management Institute e integrando prácticas ágiles donde el PROPONENTE lo justifique. | Obligatorio |
| **RT-19.02** | El Jefe de Proyecto tendrá dedicación exclusiva durante toda la fase de implementación y facultades para comprometer al ADJUDICATARIO en materias de ejecución. | Obligatorio |
| **RT-19.03** | Existirá un procedimiento formal de control de cambios conforme al Artículo 72° de las Bases Administrativas, con registro de cambios, análisis de impacto y aprobación previa a la ejecución. | Obligatorio |
| **RT-19.04** | La gestión del riesgo seguirá la norma ISO 31000, con registro de riesgos vivo, revisión en cada Comité de Proyecto y planes de mitigación con responsable, plazo y disparador. | Obligatorio |
| **RT-19.05** | El ADJUDICATARIO habilitará un espacio colaborativo accesible al CLIENTE, con la documentación del proyecto, los entregables, las actas, el registro de riesgos y el registro de cambios siempre actualizados. | Obligatorio |

#### 19.2 Roles mínimos del equipo

| Rol | Dedicación mínima | Requisito |
| :--- | :--- | :--- |
| **Jefe de Proyecto** | 100% en implementación | Certificación en gestión de proyectos y experiencia comprobable en proyectos de escala equivalente. |
| **Arquitecto de Solución** | Alta en diseño, permanente en el Comité de Arquitectura | Certificación de arquitectura del proveedor de nube ofertado. |
| **Encargado de Seguridad de la Información** | Permanente | Certificación en seguridad vigente. |
| **Líder de Datos** | Permanente en implementación | Experiencia en modelado y migración de datos. |
| **Líder de Desarrollo** | 100% en implementación | Experiencia en la tecnología ofertada. |
| **Líder Funcional** | 100% en implementación | Experiencia en la industria del caso. |
| **Líder de Calidad y Pruebas** | Permanente | Certificación en pruebas de software. |
| **Líder de Integración** | Permanente en implementación | Experiencia en integración de sistemas heredados. |
| **Líder de Operación / SRE** | Desde el mes 6, permanente en Operación | Certificación en gestión de servicios. |
| **Líder de Implantación y Gestión del Cambio** | Desde el mes 8 | Experiencia en implantación con usuarios operacionales. |

El PROPONENTE podrá agregar los roles que su propuesta requiera. La dotación total del equipo deberá ser coherente con las horas hombre del Formulario T-15 y con la curva de recursos de la Oferta Económica.

#### 19.3 Control y reporte del proyecto

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-19.06** | EL ADJUDICATARIO entregará un informe mensual de avance con estado del cronograma, avance físico y financiero, entregables del período, desviaciones, riesgos, incidencias y compromisos del período siguiente. | Obligatorio |
| **RT-19.07** | El avance se medirá con valor ganado, reportando el índice de desempeño del cronograma y del costo, y no mediante declaración cualitativa de porcentaje de avance. | Obligatorio |
| **RT-19.08** | El CLIENTE dispondrá de un tablero de estado del proyecto actualizado, accesible en cualquier momento. | Obligatorio |
| **RT-19.09** | Las actas de todos los comités del Artículo 71 de las Bases Administrativas se levantarán dentro de los dos días hábiles siguientes y registrarán acuerdos, responsables y plazos. | Obligatorio |
| **RT-19.10** | Toda desviación superior al 10% en un hito se comunicará dentro de los cinco días hábiles de detectada, con plan de recuperación. | Obligatorio |

### CAPÍTULO 20: IMPLANTACIÓN, PRUEBAS Y CRITERIOS DE ACEPTACIÓN

#### 20.1 Estrategia de pruebas

| Tipo de prueba | Cuándo | Criterio de salida |
| :--- | :--- | :--- |
| **Unitarias y de componente** | Continuo, en el flujo de integración | Cobertura mínima de 70% en lógica de negocio; sin pruebas en falla. |
| **Integración** | Continuo, tras cada despliegue a QA | Todos los flujos de integración del caso ejecutados sin error. |
| **Sistema y regresión** | Antes de cada promoción a Preproducción | Batería de regresión automatizada completa sin regresiones. |
| **Aceptación de usuario** | Antes de cada certificación de etapa | Casos de aceptación del caso aprobados y firmados por la Contraparte Técnica. |
| **Carga y estrés** | Antes de cada paso a producción | Umbrales del Capítulo 9 cumplidos a 1,5 veces el peak declarado. |
| **Resiliencia** | Antes de cada paso a producción y semestral en Operación | La solución degrada de forma controlada y se recupera sin intervención. |
| **Recuperación ante desastres** | Antes del paso a producción y semestral | RTO y RPO comprometidos alcanzados en conmutación real. |
| **Seguridad ofensiva** | Antes de cada paso a producción y anual | Sin hallazgos críticos ni altos abiertos. |
| **Accesibilidad** | Antes de cada paso a producción | Conformidad WCAG 2.2 AA verificada y documentada. |
| **Migración de datos** | Dos ensayos previos a la migración definitiva | Conciliación sin diferencias no explicadas. |

#### 20.2 Requisitos de implantación

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-20.01** | El PROPONENTE presentará un plan de implantación por sitio y por perfil, coherente con el cronograma obligatorio del Artículo 17° de las Bases Administrativas. | Obligatorio |
| **RT-20.02** | La estrategia de paso a producción será gradual y reversible. Se declarará el criterio de avance entre olas y el procedimiento de reversión, con su tiempo de ejecución. | Obligatorio |
| **RT-20.03** | Durante la marcha blanca, la solución convivirá con la operación vigente del CLIENTE, con conciliación diaria y sin doble digitación no declarada. | Obligatorio |
| **RT-20.04** | El PROPONENTE definirá los indicadores diarios que se medirán durante la marcha blanca y sus umbrales de avance, conforme al Artículo 17.3 de las Bases Administrativas. | Obligatorio |
| **RT-20.05** | Se dispondrá de acompañamiento en terreno durante las primeras semanas de cada ola, con dotación declarada y decreciente según la curva de adopción. | Obligatorio |
| **RT-20.06** | Se establecerá un período de estabilización con atención reforzada tras cada paso a producción, con dotación y duración declaradas y sin costo adicional. | Obligatorio |
| **RT-20.07** | Existirá una definición de terminado acordada con el CLIENTE, aplicable a cada entregable, que incluya código, pruebas, documentación, seguridad y despliegue. | Obligatorio |
| **RT-20.08** | El protocolo de aceptación de cada hito se formalizará conforme al Formulario T-17, con criterios objetivos y verificables. | Obligatorio |

### CAPÍTULO 21: MODELO DE OPERACIÓN, MANTENCIÓN Y SOPORTE

#### 21.1 Estructura operativa

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-21.01** | El ADJUDICATARIO dispondrá de un centro de operaciones de red con cobertura 24x7x365, propio o subcontratado, y declarará su ubicación, dotación por turno y procedimientos. | Obligatorio |
| **RT-21.02** | Se designará un gerente de servicio dedicado como contraparte permanente del CLIENTE durante la fase de Operación. | Obligatorio |
| **RT-21.03** | El equipo de operación contará con especialistas por tecnología, nominados y con dedicación declarada. | Obligatorio |
| **RT-21.04** | Los procedimientos de operación estarán documentados y serán ejecutables por el personal del CLIENTE tras la transferencia de conocimiento. | Obligatorio |

#### 21.2 Centro de atención telefónica
Este ámbito es central para dar continuidad y seguimiento al esfuerzo de incorporación y adopción de la solución.

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-21.05** | El PROPONENTE dispondrá de un centro de atención adecuado para soportar integralmente las consultas, propio o subcontratado con un operador de nivel acreditado. | Obligatorio |
| **RT-21.06** | El centro de atención cumplirá un tiempo de atención al usuario final de 80% antes de 20 segundos y una resolución al primer contacto de al menos 70%. La tasa de abandono no superará el 5%. | Obligatorio |
| **RT-21.07** | El horario mínimo de atención será de 8:00 a 20:00 en días hábiles, ampliado a 24x7 para los incidentes de severidad crítica y para la ventana operacional que defina el caso. | Según caso |
| **RT-21.08** | La atención cubrirá orientación funcional de distintos grados de complejidad, desde preguntas simples hasta situaciones complejas, y las preguntas técnicas más frecuentes sobre la aplicación y su entorno de uso. | Obligatorio |
| **RT-21.09** | Se mantendrá un registro histórico de las actividades de soporte que permita monitorear y gestionar los principales requerimientos, con análisis de tendencia mensual. | Obligatorio |
| **RT-21.10** | Existirá un proceso de aprendizaje del centro de soporte que acumule conocimiento sobre las complejidades de la operación y las necesidades de las personas usuarias, reflejado en la base de conocimiento. | Obligatorio |
| **RT-21.11** | Se proveerán servicios de capacitación en línea en modalidad de autoformación, con registro de avance para efectos de monitoreo. | Obligatorio |
| **RT-21.12** | Se habilitarán espacios de interacción entre las entidades y personas usuarias del sistema, que permitan compartir experiencias de uso. | Deseable |
| **RT-21.13** | Los indicadores clave del proceso de soporte estarán abiertos al CLIENTE, y los indicadores específicos serán accesibles según nivel de autorización. | Obligatorio |
| **RT-21.14** | El PROPONENTE dimensionará la dotación del centro de atención con fundamento cuantitativo, empleando teoría de colas o el modelo Erlang C, a partir del volumen de contactos proyectado del caso. | Obligatorio |

#### 21.3 Mesa de ayuda por niveles

| Nivel | Alcance | Responsabilidad |
| :--- | :--- | :--- |
| **Nivel 1** | Recibe los contactos de las personas usuarias internas y externas sobre cualquier requerimiento de la plataforma. | Recepción, registro del ticket, clasificación, soluciones básicas y derivación. |
| **Nivel 2** | Agentes con mayores conocimientos o especialistas en el sistema y en las aplicaciones provistas por el ADJUDICATARIO. Resuelven los incidentes derivados del nivel 1 apoyándose en manuales y guías. | Soporte especializado, configuraciones y diagnóstico. Los incidentes relativos a procedimientos propios de la operación o a aplicaciones del CLIENTE no provistas por el ADJUDICATARIO son de responsabilidad del CLIENTE y no se derivan a la mesa. |
| **Nivel 3** | Métodos de solución a nivel experto y análisis avanzado de la solución y de las aplicaciones provistas. | Resolución de problemas nuevos o desconocidos, apoyo a los niveles 1 y 2, e investigación y desarrollo de soluciones. Incluye el traslado a sitio cuando el problema lo requiera. |
| **Nivel 4** | Soporte del fabricante de los componentes de software o hardware utilizados. | Es responsabilidad del ADJUDICATARIO gestionar y obtener este soporte cuando se requiera, sin que ello lo exima de responsabilidad frente al CLIENTE. |

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-21.15** | Existirá un canal único de registro de incidentes y solicitudes, con número de ticket, clasificación por severidad y seguimiento del ciclo de vida completo hasta el cierre conforme. | Obligatorio |
| **RT-21.16** | Cuando el caso comprenda sitios alejados, los especialistas de niveles 2 y 3 deberán trasladarse cuando la resolución lo requiera, por el medio más rápido disponible y con disponibilidad de tiempo suficiente, sin alterar la atención normal del resto de los sitios. El costo del traslado está incluido en la oferta. | Según caso |
| **RT-21.17** | El cierre de un ticket requerirá confirmación de la persona usuaria o transcurso del plazo de confirmación automática declarado. | Obligatorio |
| **RT-21.18** | El ADJUDICATARIO reportará mensualmente el cumplimiento de los niveles de servicio de atención, con el detalle por severidad y el análisis de los incumplimientos. | Obligatorio |

#### 21.4 Mantención

| Tipo | Alcance | Exigencia |
| :--- | :--- | :--- |
| **Preventiva** | Revisiones programadas, actualizaciones planificadas, optimización continua y auditorías técnicas. | Calendario anual acordado con el CLIENTE. Auditorías al menos trimestrales, con informe. |
| **Correctiva** | Corrección de defectos de la solución. | Sin costo adicional. Sujeta a los tiempos de resolución del Artículo 78° de las Bases Administrativas. |
| **Evolutiva** | Mejoras funcionales, nuevas características y optimización del desempeño solicitadas por el CLIENTE. | Bolsa anual de horas comprometida en la oferta, con tarifa declarada para el excedente. La bolsa no utilizada en un año no se pierde y se acumula al siguiente. |
| **Normativa** | Adecuación de la solución ante cambios legales o regulatorios aplicables al caso. | Incluida en el valor de la Operación, sin costo adicional. Plazo de adecuación coherente con la entrada en vigencia de la norma. |

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-21.19** | El PROPONENTE declarará el tamaño de la bolsa anual de horas de mantención evolutiva, su composición por perfil y el procedimiento de solicitud, estimación, aprobación y liquidación. | Obligatorio |
| **RT-21.20** | La mantención evolutiva se someterá al mismo estándar de calidad, pruebas y seguridad que el desarrollo original. | Obligatorio |
| **RT-21.21** | El PROPONENTE mantendrá un registro de deuda técnica cuantificado y destinará una fracción declarada de la capacidad de la Operación a reducirla. | Obligatorio |
| **RT-21.22** | Las actualizaciones de versión de los componentes de base se planificarán anualmente, con ventana acordada y plan de reversión. | Obligatorio |

### CAPÍTULO 22: CAPACITACIÓN Y TRANSFERENCIA DE CONOCIMIENTO

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-22.01** | El plan de capacitación se estructurará por perfil: personas usuarias finales, usuarias avanzadas, administradoras, equipo técnico y soporte de niveles 1 y 2. | Obligatorio |
| **RT-22.02** | Las modalidades incluirán capacitación presencial en cada sitio de operación, sesiones en línea sincrónicas, autoformación y acompañamiento en puesto de trabajo durante la marcha blanca. | Obligatorio |
| **RT-22.03** | Todo el material de capacitación se entregará en español, en formato editable y de propiedad del CLIENTE: manuales por perfil, guías rápidas, preguntas frecuentes, videos tutoriales y base de conocimiento consultable. | Obligatorio |
| **RT-22.04** | La capacitación no podrá afectar la operación del CLIENTE: se programará por turnos y en horarios acordados, considerando la estacionalidad y la ventana operacional del caso. | Según caso |
| **RT-22.05** | Las personas usuarias administradoras y el equipo técnico del CLIENTE serán evaluados y certificados como condición para el cierre de cada marcha blanca. | Obligatorio |
| **RT-22.06** | Durante la Operación se ejecutarán al menos dos jornadas anuales de actualización y se capacitará al personal nuevo del CLIENTE sin costo adicional. | Obligatorio |
| **RT-22.07** | El ADJUDICATARIO proveerá acompañamiento y mentoría al equipo técnico del CLIENTE durante al menos seis meses posteriores al paso a producción de la Etapa 2. | Obligatorio |
| **RT-22.08** | La base de conocimiento será mantenida y actualizada durante todo el Contrato, con métricas de uso y de utilidad percibida. | Obligatorio |
| **RT-22.09** | Se valorará la existencia de un ambiente permanente de entrenamiento, con datos ficticios, disponible para la práctica sin riesgo. | Deseable |

---

## TÍTULO VII: EXIGENCIAS DE PRESENTACIÓN DE LA PROPUESTA
Este Título establece entregables de la propuesta que no son documentos escritos: la presencia digital del proponente, un video de presentación y un prototipo interactivo. Los tres se evalúan y los tres tienen causales de descalificación propias.

### CAPÍTULO 23: INFORMACIÓN CORPORATIVA Y PRESENCIA DIGITAL

#### 23.1 Página web corporativa
El PROPONENTE deberá disponer de una página web corporativa activa y actualizada que contenga, como mínimo, la siguiente información claramente identificable y de fácil acceso.

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-23.01** | Información institucional: descripción detallada del giro principal, historia y trayectoria de la empresa con al menos tres años de antigüedad comprobable, misión, visión y valores, certificaciones y acreditaciones vigentes, y presencia geográfica y oficinas. | Obligatorio |
| **RT-23.02** | Experiencia y casos de éxito: portafolio de proyectos similares de los últimos cinco años, casos documentados con métricas verificables, testimonios de clientes con autorización de publicación, industrias atendidas con énfasis en la del caso asignado, y volumen de transacciones o de personas usuarias gestionadas. | Obligatorio |
| **RT-23.03** | Equipo profesional: organigrama del equipo directivo, perfiles de socios y directores, currículos resumidos del equipo técnico clave y certificaciones profesionales del personal. | Obligatorio |
| **RT-23.04** | Capacidades técnicas: servicios y soluciones ofrecidas, conjunto tecnológico dominado, alianzas tecnológicas con proveedores de nube y de plataforma, metodologías de trabajo certificadas, e infraestructura y capacidad instalada. | Obligatorio |
| **RT-23.05** | El sitio será accesible conforme a WCAG 2.2 nivel AA, responsivo y con certificado TLS válido y vigente. | Obligatorio |
| **RT-23.06** | El sitio se mantendrá activo y disponible durante todo el proceso de licitación, desde el registro del participante hasta la adjudicación. | Obligatorio |
| **RT-23.07** | Material educativo digital: seminarios en línea, artículos técnicos o centro de recursos y documentación. | Deseable |
| **RT-23.08** | Demostración en línea, recorrido virtual de la solución o portal de soporte para clientes. | Deseable |
| **RT-23.09** | Métricas de disponibilidad y desempeño de los servicios del proponente publicadas en tiempo real. | Deseable |
| **RT-23.10** | Calculadora de retorno de la inversión o herramienta de estimación pertinente a la industria del caso. | Deseable |

#### 23.2 Verificación y validación
El CLIENTE verificará el sitio durante el proceso de evaluación. Constituyen causal de descalificación:
* Sitio web no disponible o con caídas recurrentes durante el período de evaluación.
* Información falsa o engañosa comprobada.
* Ausencia de la información crítica exigida en el numeral 23.1.
* Casos de éxito no verificables o cuyas contrapartes desmientan lo declarado.
* Plagio de contenido de otros sitios.

#### 23.3 Declaración de veracidad
El PROPONENTE deberá incluir en el Sobre N° 1 una declaración jurada simple que indique:
1. La dirección oficial del sitio web de la empresa.
2. Que toda la información publicada en el sitio es verídica y se encuentra actualizada.
3. La autorización para que la Comisión Evaluadora contacte a las referencias declaradas.
4. El compromiso de mantener el sitio activo durante todo el proceso.
5. La aceptación de la descalificación en caso de información falsa.

### CAPÍTULO 24: VIDEO DE PRESENTACIÓN DE LA PROPUESTA

#### 24.1 Especificaciones técnicas

| Aspecto | Exigencia |
| :--- | :--- |
| **Duración** | Máximo 5 minutos (300 segundos). Excederlo produce descalificación automática. |
| **Resolución** | Full HD, 1920x1080 píxeles como mínimo. |
| **Formato de archivo** | MP4 con códec H.264. |
| **Cuadros por segundo** | 30 fps como mínimo. |
| **Tasa de bits de video** | 5 Mbps como mínimo. |
| **Tamaño máximo del archivo** | 500 MB. |
| **Audio** | 44,1 kHz y 16 bits como mínimo, en AAC o MP3, con niveles normalizados, sin distorsión ni ruido de fondo excesivo. |
| **Música** | Opcional, con licencia acreditable. |
| **Orientación** | Horizontal (apaisada). |
| **Aspectos visuales** | Iluminación profesional adecuada, fondo neutro o corporativo, sin efectos que distraigan del mensaje y con transiciones suaves. |

#### 24.2 Estructura y contenido
El video deberá contener los siguientes segmentos, en este orden:
1. Introducción corporativa: logotipo animado, nombre del proyecto y del caso, fecha de la propuesta y nombre del proponente.
2. Comprensión del problema: análisis de la problemática actual, impacto en las personas afectadas, riesgos de no implementar la solución, métricas del problema identificado y demostración de comprensión del sector.
3. Solución propuesta: visión general, beneficios para cada grupo de interés, diferenciadores clave, innovaciones incluidas y resultados esperados con métricas.
4. Propuesta tecnológica: conjunto tecnológico completo, arquitectura de alto nivel, servicios de nube utilizados, y seguridad y cumplimiento normativo.
5. Ventajas competitivas: por qué el proponente es la mejor opción, experiencia específica, casos de éxito relevantes, garantías y compromisos, y valor agregado único.
6. Cierre y compromiso: compromiso con el proyecto, datos de contacto e identidad corporativa final.

#### 24.3 Participación del equipo

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-24.01** | Todos los integrantes clave del equipo deberán aparecer individualmente presentándose, en toma de medio cuerpo, mirando directamente a la cámara, con vestimenta formal o de negocio informal, y con una duración mínima de aparición de 10 segundos por persona. | Obligatorio |
| **RT-24.02** | Cada vez que aparezca un integrante deberá mostrarse en pantalla su nombre completo, su cargo en el proyecto, sus años de experiencia y su especialización relevante. | Obligatorio |
| **RT-24.03** | Las certificaciones principales de cada integrante podrán mostrarse en pantalla. | Deseable |
| **RT-24.04** | El fondo será el mismo para todas las tomas de personas, con iluminación consistente y encuadre similar para todos los participantes. | Obligatorio |
| **RT-24.05** | La paleta de colores corporativa, la tipografía y el uso de la marca serán consistentes en todo el video, con logotipo visible en todas las escenas y datos de contacto en el encabezado o pie. | Obligatorio |
| **RT-24.06** | Los niveles de volumen estarán normalizados, con la misma calidad de grabación y sin variaciones bruscas de sonido. | Obligatorio |

#### 24.4 Evaluación, penalizaciones y descalificación

| Situación | Efecto |
| :--- | :--- |
| Audio con problemas menores | -5 puntos |
| Iluminación deficiente | -5 puntos |
| Transiciones bruscas | -5 puntos |
| Información poco clara | -5 puntos |
| Falta de un rol no crítico del equipo | -5 puntos |
| Duración superior a 5 minutos | Descalificación automática |
| No aparición del equipo clave completo | Descalificación automática |
| Calidad técnica inferior a la especificada en el numeral 24.1 | Descalificación automática |
| Información falsa o engañosa | Descalificación automática |
| Uso de material con derechos de autor sin licencia | Descalificación automática |
| No entrega del video junto con la propuesta | Descalificación automática |

#### 24.5 Entrega, derechos y autorizaciones
* Entrega física: unidad de almacenamiento USB junto con la propuesta, etiquetada con el nombre de la empresa y del proyecto, incluyendo archivo de respaldo.
* Entrega digital: enlace de descarga con vigencia mínima de 60 días, sin restricciones de descarga y con la contraseña de acceso en documento separado.
* El PROPONENTE autoriza el uso del video para fines de evaluación y su proyección en las sesiones de evaluación.
* El PROPONENTE garantiza que posee todos los derechos necesarios sobre el material utilizado.
* La Comisión Evaluadora mantendrá la confidencialidad del contenido, no lo distribuirá sin autorización y eliminará las copias posteriores a la evaluación de las propuestas no seleccionadas.

### CAPÍTULO 25: PROTOTIPO INTERACTIVO DE INTERFAZ Y DISEÑO UX/UI

#### 25.1 Objetivo y momento de entrega
El PROPONENTE deberá presentar, junto con el Informe 3, un prototipo interactivo de alta fidelidad que demuestre de manera clara y tangible la visión de diseño de interfaz propuesta para la solución del caso. El prototipo permite evaluar la comprensión del proponente sobre las necesidades reales de las personas usuarias y su capacidad de traducirlas en una experiencia de uso adecuada.

El prototipo no requiere conexión con servicios de fondo ni con base de datos, pero debe simular de manera realista la navegación y los flujos de trabajo principales, permitiendo a los evaluadores experimentar la solución desde la perspectiva de los distintos perfiles de personas usuarias.

#### 25.2 Alcance mínimo
El prototipo deberá incluir, como mínimo, las siguientes vistas y funcionalidades navegables:

| Bloque | Contenido mínimo |
| :--- | :--- |
| **Portal principal** | Página de inicio pública; página de inicio con sesión iniciada y personalizada por perfil; tablero principal con componentes configurables; menú de navegación completo y funcional; rastro de navegación y navegación contextual. |
| **Autenticación e incorporación** | Pantalla de inicio de sesión unificada; registro de una nueva persona usuaria externa en al menos cinco pasos; recuperación de acceso; segundo factor de autenticación; y tablero de primer ingreso con recorrido guiado. |
| **Proceso operacional principal del caso** | El flujo de negocio central de la industria asignada, de extremo a extremo, en al menos seis pasos, desde su inicio hasta su cierre, incluyendo los estados intermedios y el manejo de la excepción más frecuente. |
| **Proceso operacional secundario del caso** | Un segundo flujo relevante, con su listado, su vista de detalle, su creación y su flujo de aprobación visual. |
| **Perfil de terreno o de operación** | La vista que utilizará la persona usuaria operacional en su puesto real, incluida su versión móvil y su comportamiento sin conexión, cuando el caso lo requiera. |
| **Gestión de terceros** | Directorio de la contraparte externa del caso —clientes, proveedores, productores, pacientes, pasajeros—, su ficha completa, su evaluación y su historial. |
| **Tablero analítico** | Indicadores principales con visualizaciones; al menos seis tipos de gráfico distintos; filtros por período y categoría; profundización desde el indicador hasta el detalle; y exportación de informes. |
| **Administración** | Gestión de personas usuarias, roles y permisos; parametrización; y consulta de auditoría. |
| **Dos módulos adicionales** | A elección del PROPONENTE, pertinentes al caso. |

#### 25.3 Principios de diseño exigidos

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-25.01** | Navegación intuitiva sin necesidad de manual, con un máximo de tres interacciones para alcanzar cualquier funcionalidad principal. | Obligatorio |
| **RT-25.02** | Retroalimentación visual clara ante cada acción, estados de carga y transición fluidos, y manejo elegante de los errores. | Obligatorio |
| **RT-25.03** | Cumplimiento de WCAG 2.2 nivel AA: contraste adecuado, tamaños de fuente legibles, objetivos táctiles de al menos 44x44 píxeles, navegación completa por teclado, y textos alternativos y etiquetas de accesibilidad. | Obligatorio |
| **RT-25.04** | Diseño responsivo demostrado en escritorio (1920x1080 y 1366x768), tableta (768 x 1024 en vertical y horizontal) y teléfono (375x812), con puntos de quiebre coherentes. | Obligatorio |
| **RT-25.05** | Sistema de diseño documentado: paleta de a lo más cinco colores principales, a lo más dos familias tipográficas jerarquizadas, iconografía coherente, retícula y espaciado consistentes, y componentes reutilizables. | Obligatorio |

#### 25.4 Componentes de interfaz obligatorios

| Categoría | Componentes que el prototipo debe demostrar |
| :--- | :--- |
| **Navegación** | Menú principal, menú secundario contextual, rastro de navegación, paginación, pestañas y acordeones, navegación por pasos y menú de acciones rápidas. |
| **Formularios** | Campos de texto con validación en tiempo real, selectores y desplegables, casillas y botones de opción, selectores de fecha y hora, carga de archivos con arrastrar y soltar, autocompletado y formularios de múltiples pasos. |
| **Visualización de datos** | Tablas con ordenamiento y filtrado, gráficos de barras, de líneas y circulares, tarjetas de información, líneas de tiempo, indicadores de progreso, distintivos y etiquetas, e información contextual emergente. |
| **Retroalimentación** | Mensajes de éxito, error, advertencia e información; ventanas modales y diálogos; notificaciones emergentes; esqueletos de carga; indicadores de progreso; y estados vacíos ilustrados. |
| **Acción** | Botones primarios, secundarios y terciarios; botón de acción flotante; acciones en línea; menús contextuales; acciones masivas; y confirmación de acciones críticas. |

#### 25.5 Entrega y nivel de interactividad

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-25.06** | El prototipo se entregará como enlace navegable en línea, sin instalación ni complementos, compatible con los navegadores modernos vigentes. | Obligatorio |
| **RT-25.07** | El acceso al prototipo estará garantizado por un mínimo de seis meses desde su entrega. | Obligatorio |
| **RT-25.08** | El prototipo permitirá navegación completa entre pantallas, simulación de ingreso de datos, transiciones y animaciones básicas, estados de posado y activo, simulación de carga de archivos, elementos desplegables funcionales y simulación de validaciones. | Obligatorio |
| **RT-25.09** | Se entregará la arquitectura de información del prototipo: mapa del sitio completo, diagrama de navegación, taxonomía y nomenclatura, estructura de menús y jerarquía de la información. | Obligatorio |
| **RT-25.10** | Se valorará la posibilidad de exportar el prototipo a un documento interactivo para revisión sin conexión. | Deseable |

#### 25.6 Restricciones y penalizaciones

| No se requiere | Se penalizará |
| :--- | :--- |
| Funcionalidad real de servicios de fondo. | Prototipos estáticos, no navegables. |
| Conexión a base de datos. | Diseños genéricos sin personalización al caso. |
| Procesamiento real de datos. | Incumplimiento de los estándares de accesibilidad. |
| Integración con servicios externos. | Navegación confusa o enlaces rotos. |
| Autenticación real. | Inconsistencias visuales evidentes. |
| Persistencia de la información ingresada. | Falta de responsividad en los tamaños exigidos. |

#### 25.7 Propiedad intelectual del diseño
* El diseño propuesto será de propiedad del CLIENTE si la propuesta resulta adjudicada, conforme al Artículo 84° de las Bases Administrativas.
* El PROPONENTE mantiene los derechos sobre sus componentes genéricos y sobre su sistema de diseño preexistente.
* Se autoriza el uso del prototipo para fines de evaluación y para su proyección en las sesiones de evaluación.
* El CLIENTE mantendrá la confidencialidad de los diseños no seleccionados.

### CAPÍTULO 26: INNOVACIONES
La exigencia de innovación se establece en el Capítulo 5 de las Bases Administrativas: cinco innovaciones obligatorias, una por cada tipo, con los siete elementos del Artículo 29° documentados en el Formulario T-19. Este capítulo agrega las exigencias técnicas de su formulación.

| Código | Requisito | Carácter |
| :--- | :--- | :--- |
| **RT-26.01** | Cada innovación se ubicará explícitamente en la arquitectura: qué capa la contiene, qué componentes la implementan y qué interfaces consume o expone. | Obligatorio |
| **RT-26.02** | Cada innovación identificará los paquetes de la estructura de descomposición del trabajo que la ejecutan y el mes del cronograma en que se materializa. | Obligatorio |
| **RT-26.03** | Las innovaciones de base tecnológica declararán el nivel de madurez de la tecnología con la escala utilizada y citarán las fuentes en norma APA 7.ª edición. | Obligatorio |
| **RT-26.04** | Cada innovación declarará su riesgo de adopción, su probabilidad, su impacto, la estrategia de mitigación y el plan de contingencia si no rinde lo esperado. | Obligatorio |
| **RT-26.05** | Cada innovación declarará su indicador de verificación con línea base, meta y momento de medición, y su impacto en inversión, costo operacional y beneficio esperado. | Obligatorio |
| **RT-26.06** | Las innovaciones que incorporen inteligencia artificial cumplirán íntegramente el Capítulo 18 de este documento. | Obligatorio |
| **RT-26.07** | Las innovaciones que modifiquen la arquitectura de seguridad requerirán su propio modelado de amenazas. | Obligatorio |
| **RT-26.08** | Se valorará que al menos una innovación sea verificable durante la marcha blanca de la Etapa 1, es decir, que su beneficio pueda medirse antes del mes 16. | Deseable |

> No se aceptará como innovación la sola adopción de una tecnología que ya constituye estándar de la industria, la mención de una tendencia sin diseño de incorporación, ni una funcionalidad exigida por las Bases Técnicas presentada como innovación. La pertinencia al caso pesa más que la novedad tecnológica en abstracto.

---

## TÍTULO VIII: ANEXOS

### CAPÍTULO A: ÍNDICE DE REQUISITOS TRANSVERSALES
Resumen de los requisitos codificados de este documento. El PROPONENTE deberá pronunciarse sobre la totalidad de ellos en el Formulario T-12.
A estos requisitos se suman los del Capítulo 4 de las Bases Administrativas y la totalidad de los requerimientos funcionales, volúmenes y criterios de aceptación de las Bases Técnicas del caso asignado.

| Cap. | Materia | Rango de códigos | N° |
| :--- | :--- | :--- | :--- |
| **02** | Modelo de arquitectura de referencia | RT-02.01 - RT-02.14 | 14 |
| **03** | Modelo híbrido: nube y on-premise | RT-03.01 - RT-03.24 | 24 |
| **04** | Ambientes, entrega continua y configuración | RT-04.01 - RT-04.14 | 14 |
| **05** | Datos, integración e interoperabilidad | RT-05.01 - RT-05.30 | 30 |
| **06** | Site principal on-premise | RT-06.01 - RT-06.34 | 34 |
| **07** | Site secundario y recuperación ante desastres | RT-07.01 - RT-07.14 | 14 |
| **08** | Hardware, puestos de trabajo y terreno | RT-08.01 - RT-08.19 | 19 |
| **09** | Desempeño, capacidad y escalabilidad | RT-09.01 - RT-09.10 | 10 |
| **10** | Disponibilidad, continuidad y resiliencia | RT-10.01 - RT-10.09 | 9 |
| **11** | Seguridad de la información | RT-11.01 - RT-11.28 | 28 |
| **12** | Identidad, acceso y sesiones | RT-12.01 - RT-12.13 | 13 |
| **13** | Usabilidad, accesibilidad y experiencia de usuario | RT-13.01 - RT-13.12 | 12 |
| **14** | Observabilidad y gestión del servicio | RT-14.01 - RT-14.09 | 9 |
| **15** | Sostenibilidad, eficiencia y certificaciones | RT-15.01 - RT-15.09 | 9 |
| **16** | Módulos transversales obligatorios | RT-16.01 - RT-16.34 | 34 |
| **17** | Canales digitales y movilidad | RT-17.01 - RT-17.08 | 8 |
| **18** | Inteligencia artificial y automatización | RT-18.01 - RT-18.10 | 10 |
| **19** | Estructura y gobierno del proyecto | RT-19.01 - RT-19.10 | 10 |
| **20** | Implantación, pruebas y aceptación | RT-20.01 - RT-20.08 | 8 |
| **21** | Operación, mantención y soporte | RT-21.01 - RT-21.22 | 22 |
| **22** | Capacitación y transferencia de conocimiento | RT-22.01 - RT-22.09 | 9 |
| **23** | Información corporativa y presencia digital | RT-23.01 - RT-23.10 | 10 |
| **24** | Video de presentación de la propuesta | RT-24.01 - RT-24.06 | 6 |
| **25** | Prototipo interactivo y diseño UX/UI | RT-25.01 - RT-25.10 | 10 |
| **26** | Innovaciones | RT-26.01 - RT-26.08 | 8 |
| | **TOTAL DE REQUISITOS CODIFICADOS** | | **374** |

### CAPÍTULO B: PLANTILLA DE VOLUMETRÍA
Las Bases Técnicas de cada caso entregan la volumetría real de la industria correspondiente, completando la siguiente plantilla. El PROPONENTE deberá dimensionar su solución sobre esos valores y declarar el margen de crecimiento considerado.

| Dimensión | Actual | Proyectada a 3 años | Peak |
| :--- | :--- | :--- | :--- |
| **Transacciones de negocio anuales** | | | |
| **Transacciones por segundo en régimen normal** | | | |
| **Transacciones por segundo en peak** | | | |
| **Personas usuarias registradas** | | | |
| **Personas usuarias concurrentes** | | | |
| **Contrapartes externas activas** | | | |
| **Documentos procesados al año** | | | |
| **Volumen de almacenamiento transaccional** | | | |
| **Volumen de almacenamiento documental y multimedia** | | | |
| **Volumen de datos históricos a migrar** | | | |
| **Dispositivos de terreno en operación** | | | |
| **Sitios u operaciones a cubrir** | | | |
| **Integraciones con sistemas internos** | | | |
| **Integraciones con sistemas externos** | | | |
| **Contactos mensuales al centro de atención** | | | |
| **Ventana operacional crítica (horario y estacionalidad)** | | | |

### CAPÍTULO C: CHECKLIST DE ENTREGABLES DE LA OFERTA TÉCNICA
Lista de verificación para el PROPONENTE. No reemplaza a los formularios del Anexo B de las Bases Administrativas ni altera sus exigencias.

| N° | Entregable | Dónde se exige | Sobre / instancia |
| :--- | :--- | :--- | :--- |
| **1** | Documento de arquitectura conforme a ISO/IEC/IEEE 42010, con las cinco vistas | RT-02.03 | Sobre N° 2 |
| **2** | Registro de decisiones de arquitectura (ADR) | RT-02.04 | Sobre N° 2 |
| **3** | Tabla de emplazamiento de componentes en nube y on-premise, justificada | Cap. 3 | Sobre N° 2 |
| **4** | Declaración de funciones no disponibles en modo desconectado | RT-03.13 | Sobre N° 2 |
| **5** | Modelo de datos y diccionario de datos | RT-05.01 | Sobre N° 2 |
| **6** | Plan de migración de datos | RT-05.11 | Sobre N° 2 |
| **7** | Documentación de interfaces en OpenAPI y AsyncAPI | RT-05.16 | Sobre N° 2 |
| **8** | Especificación del site principal y del site secundario, con planos | Caps. 6 y 7 | Sobre N° 2 |
| **9** | Plan de recuperación ante desastres y política de respaldo | Cap. 7 | Sobre N° 2 |
| **10** | Especificación del hardware y de los dispositivos de terreno | Cap. 8 | Sobre N° 2 |
| **11** | Cálculo de capacidad y dimensionamiento | RT-09.01 | Sobre N° 2 |
| **12** | Plan de continuidad del negocio conforme a ISO 22301 | RT-10.03 | Sobre N° 2 |
| **13** | Modelado de amenazas y matriz de controles de seguridad | RT-11.02 y RT-11.05 | Sobre N° 2 |
| **14** | Declaración de la superficie de exposición de la solución | RT-11.13 | Sobre N° 2 |
| **15** | Plan de respuesta a incidentes de seguridad | RT-11.18 | Sobre N° 2 |
| **16** | Modelo de identidad, matriz de roles y segregación de funciones | Cap. 12 | Sobre N° 2 |
| **17** | Sistema de diseño e informe de conformidad de accesibilidad | Cap. 13 | Sobre N° 2 |
| **18** | Estrategia de observabilidad y catálogo de alertas | Cap. 14 | Sobre N° 2 |
| **19** | Certificados institucionales y del personal | Cap. 15 | Sobre N° 1 y N° 2 |
| **20** | Estrategia de pruebas y plan de pruebas (Formulario T-13) | Cap. 20 | Sobre N° 2 |
| **21** | Plan de implantación y de marcha blanca (Formulario T-18) | RT-20.01 | Sobre N° 2 |
| **22** | Modelo de operación, soporte y dimensionamiento del centro de atención | Cap. 21 | Sobre N° 2 |
| **23** | Plan de capacitación y de transferencia de conocimiento | Cap. 22 | Sobre N° 2 |
| **24** | Matriz de cumplimiento técnico (Formulario T-12) sobre todos los códigos RT | Numeral 1.5 | Sobre N° 2 |
| **25** | Sitio web corporativo activo y declaración jurada de veracidad | Cap. 23 | Sobre N° 1 |
| **26** | Video de presentación de la propuesta | Cap. 24 | Con la propuesta final |
| **27** | Prototipo interactivo y arquitectura de información | Cap. 25 | Con el Informe 3 |
| **28** | Fichas de las cinco innovaciones (Formulario T-19) | Cap. 26 | Sobre N° 2 |

### CAPÍTULO D: GLOSARIO Y DEFINICIONES
Complementa el Artículo 3º de las Bases Administrativas. Ante discrepancia, prevalece la definición de dicho artículo.

| Término | Definición |
| :--- | :--- |
| **ADR** | Architecture Decision Record. Registro fechado de una decisión de arquitectura, sus alternativas y su fundamento. |
| **AFIS** | Automated Fingerprint Identification System. Sistema automatizado de identificación por huella dactilar. |
| **API** | Application Programming Interface. Interfaz de programación que expone capacidades de un sistema a otro. |
| **ASVS** | Application Security Verification Standard, de OWASP. Estándar de verificación de seguridad de aplicaciones. |
| **Capa anticorrupción** | Componente que traduce el modelo de un sistema externo al modelo propio, impidiendo que aquel contamine este. |
| **CDN** | Content Delivery Network. Red de distribución de contenidos. |
| **CIS Benchmarks** | Guías de configuración segura publicadas por el Center for Internet Security. |
| **Cortacircuitos** | Patrón que interrumpe las llamadas a una dependencia en falla para evitar la propagación del error. |
| **Despliegue azul-verde** | Estrategia que mantiene dos entornos productivos y conmuta el tráfico entre ellos. |
| **Despliegue canario** | Estrategia que expone la nueva versión a una fracción creciente del tráfico. |
| **DevSecOps** | Integración de las prácticas de seguridad en el ciclo de desarrollo y operación. |
| **Erlang C** | Modelo de teoría de colas empleado para dimensionar centros de atención. |
| **FCR** | First Call Resolution. Resolución en el primer contacto. |
| **FM-200** | Agente limpio de extinción de incendios, apto para recintos con equipamiento electrónico. |
| **IaC** | Infrastructure as Code. Infraestructura definida como código versionado. |
| **Idempotencia** | Propiedad de una operación que produce el mismo resultado aunque se ejecute varias veces. |
| **ITIL** | Marco de buenas prácticas para la gestión de servicios de tecnologías de información. |
| **Mamparo de aislamiento** | Patrón que separa recursos por grupo de consumo para que la falla de uno no agote los del resto. |
| **MTTR** | Mean Time To Restore. Tiempo medio de restauración del servicio. |
| **NOC** | Network Operations Center. Centro de operaciones de red. |
| **NCh** | Norma Chilena Oficial, emitida por el Instituto Nacional de Normalización. |
| **OpenTelemetry** | Estándar abierto de instrumentación para métricas, registros y trazas. |
| **OWASP** | Open Worldwide Application Security Project. |
| **Percentil 95** | Valor bajo el cual se encuentra el 95% de las mediciones. Refleja la experiencia de la cola lenta, no el promedio. |
| **PMBOK** | Guía de fundamentos para la dirección de proyectos, del Project Management Institute. |
| **PMO** | Project Management Office. Oficina de gestión de proyectos. |
| **Presupuesto de error** | Fracción de indisponibilidad admitida por el objetivo de nivel de servicio, empleada para regular el ritmo de cambios. |
| **PUE** | Power Usage Effectiveness. Relación entre la energía total consumida por un recinto y la consumida por el equipamiento de TI. |
| **RAID** | Redundant Array of Independent Disks. Arreglo redundante de discos. |
| **RPO** | Recovery Point Objective. Máxima pérdida de datos tolerada, expresada en tiempo. |
| **RTO** | Recovery Time Objective. Máximo tiempo tolerado para restituir el servicio. |
| **SBOM** | Software Bill of Materials. Inventario de los componentes de un artefacto de software. |
| **SIEM** | Security Information and Event Management. Plataforma de correlación de eventos de seguridad. |
| **SLA/SLO/SLI** | Acuerdo, objetivo e indicador de nivel de servicio. |
| **SLSA** | Supply-chain Levels for Software Artifacts. Marco de niveles de seguridad de la cadena de suministro de software. |
| **SOC** | Security Operations Center. Centro de operaciones de seguridad. |
| **SRE** | Site Reliability Engineering. Disciplina de operación de sistemas basada en ingeniería. |
| **STRIDE** | Metodología de modelado de amenazas: suplantación, manipulación, repudio, divulgación, denegación y elevación de privilegios. |
| **TPS** | Transactions Per Second. Transacciones por segundo. |
| **UAT** | User Acceptance Testing. Pruebas de aceptación de usuario. |
| **WAF** | Web Application Firewall. Cortafuegos de aplicaciones web. |
| **WCAG** | Web Content Accessibility Guidelines. Pautas de accesibilidad para el contenido web. |
| **Zero Trust** | Modelo de seguridad en que ninguna red, dispositivo, identidad o carga de trabajo es confiable por defecto. |
