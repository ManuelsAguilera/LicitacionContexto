> **ARCHIVADO (2026-10-08). No usar como fuente.** Material de trabajo superado por `sd-03.tex`, los Anexos A a D y `ficha_alcance_sd-03.md`. Usa códigos y decisiones antiguas. Se conserva solo por trazabilidad.

**OnlySimpleSolutions**

# **Análisis de actores, alcance y arquitectura de servicios**

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

# 

## **Resumen ejecutivo**

Este documento responde tres preguntas. Primero, quién interactúa con la solución y qué rol cumple. Segundo, qué parte del negocio queda dentro o fuera del alcance. Tercero, qué servicios se desplegarán para cumplir ese alcance.

La regla más importante es separar la persona de la función. El actor es quién participa; el rol explica qué hace en una interacción concreta. Por ejemplo, una misma persona puede ser comprador en Retail y titular de crédito en el Emisor, pero los permisos y datos de cada negocio siguen separados.

La propuesta se puede leer como un edificio: las promesas son el resultado que debe recibir el cliente; las responsabilidades son las habitaciones necesarias para lograrlo; los servicios son las unidades que se construirán; y la plataforma —Gateway, eventos, identidad y observabilidad— son las instalaciones que permiten que todo funcione. El resultado comprometido es de 13 servicios de aplicación: 9 Retail, 3 del Emisor y 1 de frontera.

## **Objetivos del documento**

Este documento complementa la definición de alcance mediante los siguientes objetivos:

* Identificar y normalizar actores, grupos, roles, sistemas externos y stakeholders.  
* Relacionar actores y roles con los procesos e interacciones en los que participan.  
* Identificar capacidades exclusivamente de negocio, sin comprometer tecnología.  
* Agrupar capacidades relacionadas en fronteras funcionales coherentes.  
* Separar negocio, canales, sistemas externos, controles transversales y plataforma técnica.  
* Mantener trazabilidad desde los requisitos y las decisiones documentadas en esta propuesta.  
* Establecer criterios para decidir módulos, servicios desplegables y microservicios.  
* Registrar dudas que requieren validación antes de fijar la arquitectura objetivo.

No se fija todavía el número final de microservicios ni sus APIs o infraestructura. Esas decisiones dependen de requisitos no funcionales, datos, operación, equipos y arquitectura física.

## **GLOSARIO DE TÉRMINOS CLAVE**

# 

Actor: persona, grupo, unidad organizacional, organización o sistema que participa directamente en una interacción relevante con el proceso o la solución.

Rol: función que un actor desempeña en una interacción concreta. El rol puede cambiar sin crear un actor nuevo.

Grupo de interés: parte que influye, decide, fiscaliza o resulta afectada por el proyecto, aunque no opere directamente la solución.

Capacidad de negocio: habilidad que Ancoa necesita para producir un resultado, sin describir todavía una tecnología.

Responsabilidad A/B/C: clasificación de trabajo usada en este documento. A corresponde a Retail; B corresponde al Emisor financiero; C corresponde a separación, evidencia y controles transversales.

Servicio de aplicación: unidad desplegable que ofrece una responsabilidad mediante contratos de entrada y salida. En este documento, R, F y X identifican familias de servicios.

Módulo: forma de organizar el código dentro de un servicio. No es una unidad adicional del catálogo ni necesariamente un despliegue separado.

Microservicio: servicio operado con autonomía de despliegue, datos, escalamiento y fallas. Es una decisión de implementación posterior y no aumenta la lista de 13 servicios comprometidos.

Frontera: límite que define qué datos, reglas, operaciones y responsabilidades pertenecen a un servicio o negocio.

Plataforma: componentes técnicos compartidos, como identidad, API Gateway, bus de eventos, adaptadores y observabilidad. La plataforma habilita los servicios, pero no es dueña de sus reglas de negocio.

Integración: intercambio controlado de información entre servicios, canales o sistemas existentes. Una integración no convierte automáticamente al sistema conectado en un servicio del catálogo.

Retail: negocio comercial de Ancoa: catálogo, precios, inventario, ventas, pedidos, marketplace, posventa y fidelización.

Emisor financiero: negocio de crédito fiscalizado de Ancoa: originación, autorización, cartera, cobranza, repactaciones, consentimiento y evidencia financiera.

R / F / X: R identifica servicios Retail; F identifica servicios del Emisor financiero; X identifica el servicio de frontera que autoriza y audita cruces entre ambos.

# 

# **PARTE I — ACTORES, ROLES Y DELIMITACIÓN**

## **1\. Definiciones de actor, rol y grupo de interés**

Un actor es una persona, grupo, unidad organizacional, organización o sistema externo que participa directamente en una interacción relevante para lograr un resultado. Un grupo de interés puede influir, decidir, fiscalizar o verse afectado sin operar directamente la solución; por eso no todo grupo de interés debe aparecer como actor en un diagrama.

Un rol es la función, responsabilidad o posición que un actor asume dentro de una interacción concreta. El actor responde a «quién participa» y el rol a «en calidad de qué participa». Un mismo actor puede asumir varios roles sin transformarse en actores distintos. Por ejemplo, un Cliente puede actuar como comprador, receptor de un pedido o titular de tarjeta; vendedores y cajeros pertenecen a Operación de tienda, pero se distinguen por el rol que cumplen en cada flujo.

Regla de uso: en vistas generales y diagramas se emplea el nombre del actor. El rol se agrega únicamente cuando sea necesario precisar permisos, responsabilidades, decisiones o diferencias de comportamiento. No se crearán sinónimos nuevos para un actor ya definido.

### **1.1 Definición formal de tipo, relación y contexto**

Tipo o naturaleza responde únicamente a qué clase de entidad estable es el actor. Los valores permitidos son: Persona, cuando se modela a un individuo; Colectivo humano, cuando se agrupan personas con el mismo vínculo y comportamiento sin afirmar que constituyen una unidad formal; Unidad organizacional, cuando existe una agrupación interna con responsabilidad reconocible; y Organización, cuando se modela una entidad autónoma, normalmente externa y con responsabilidad legal o contractual.

Relación indica si el actor es interno o externo a Ancoa. Contexto indica dónde participa: Retail, Emisor o transversal controlado. Participación funcional indica qué inicia, ejecuta, aprueba, provee, recibe o fiscaliza en un flujo concreto.

Regla de decisión: si el nombre describe una acción, permiso o función cajero, preparador, deudor, auditor se registra como rol, no como tipo. Si describe software, dispositivo o infraestructura, se registra como sistema o componente, fuera de esta matriz. Si solo resulta afectado o interesado pero no interactúa con el proceso o la solución, se registra como stakeholder, no como actor del flujo.

Esta taxonomía es un perfil de modelado del proyecto: adopta de UML/IIBA que el actor desempeña un rol al interactuar con la solución y usa la distinción de arquitectura empresarial entre persona, grupo/unidad y organización. Los cuatro valores cerrados son una convención documentada del proyecto, no categorías literales impuestas por un único estándar.

### **1.2 Qué implica cada clasificación**

La clasificación de un actor no es una etiqueta única. Se construye combinando dimensiones independientes: naturaleza \+ relación con Ancoa \+ plano de participación \+ contexto de dominio \+ rol en el flujo. Por ejemplo, TI y soporte es una unidad organizacional interna, técnica y transversal de plataforma; un vendedor marketplace es una organización externa, de negocio y del contexto Retail.

#### ***Relación con Ancoa***

##### Actor interno

Es una persona, colectivo o unidad sometida a la autoridad organizacional de Ancoa. Implica identidad corporativa, responsabilidades asignadas, acceso por rol, segregación de funciones, capacitación y trazabilidad individual. Ser interno no concede acceso general: Retail y Emisor mantienen permisos y datos separados.

##### Actor externo

Está fuera de la autoridad organizacional de Ancoa y participa por una relación comercial, contractual, legal o de servicio. Implica patrocinador o contraparte interna, identidad acotada, mínimo privilegio, minimización de datos, vigencia y revocación del acceso, aislamiento entre organizaciones y trazabilidad contractual. “Externo” no significa “fuera de alcance”: puede ser esencial para un flujo.

#### ***Plano de participación***

##### Actor de negocio

Persigue o entrega un resultado del negocio: compra, vende, abastece, transporta, atiende, aprueba o administra una operación. Puede ser interno o externo. Sus permisos corresponden a responsabilidades del proceso; no obtiene privilegios técnicos por participar en él.

##### Actor técnico

Opera, integra, soporta, protege u observa la plataforma, sin asumir por ello decisiones del negocio. Puede ser TI interno o un proveedor externo. Implica cuentas privilegiadas separadas, mínimo privilegio, elevación temporal, registro de sesiones y cambios, acceso excepcional controlado y prohibición de alterar precios, saldos, crédito o autorizaciones por mera capacidad administrativa.

##### Actor de control o fiscalización

Comprueba cumplimiento, evidencia, riesgos o aplicación de reglas, sin ejecutar rutinariamente el proceso controlado. Puede ser interno auditoría, cumplimiento o prevención o externo regulador o auditor. Implica independencia, acceso preferentemente de lectura, evidencia inmutable, trazabilidad y ausencia de facultades operativas salvo mandato explícito.

#### ***Contexto de actuación***

##### Retail

El actor participa en venta, catálogo, inventario, pedidos, logística, marketplace, posventa o conciliación comercial. Sus datos y reglas pertenecen al negocio retail.

##### Emisor

El actor participa en originación, riesgo, consentimiento, administración de cartera, cobranza o cumplimiento financiero. Implica una frontera jurídica y de datos separada de Retail, incluso cuando la misma persona desempeña más de un rol.

##### Transversal controlado

El actor cruza Retail y Emisor solo por un mandato definido —por ejemplo auditoría o cumplimiento—. El cruce debe estar justificado, limitado y registrado; no fusiona ambos dominios.

##### Transversal de plataforma

El actor presta capacidades técnicas comunes, como identidad, seguridad, observabilidad o soporte. La transversalidad técnica no autoriza a usar datos de negocio sin una necesidad operativa aprobada.

#### ***Conceptos que no deben confundirse con el tipo de actor***

##### Sistema actor

Es un sistema, dispositivo o servicio que intercambia información con la solución desde fuera de la frontera que se está modelando. “Externo” aquí es relativo a esa frontera: un ERP propiedad de Ancoa puede ser actor externo de la solución, aunque sea un activo interno de la empresa. API Gateway y bus de eventos son componentes internos de la arquitectura, no actores, mientras permanezcan dentro de la frontera.

##### Stakeholder

Es una parte interesada o afectada. Solo se modela además como actor cuando interactúa directamente con el proceso o sistema analizado. Un directivo informado por reportes puede ser stakeholder sin intervenir en el flujo operativo.

#### ***Regla de uso***

En diagramas se usa el actor. Cuando sea necesario precisar su conducta se agrega el rol y el contexto, por ejemplo: “Cliente \[titular, Emisor\]”, “Personal de venta y caja \[cajero, Retail\]” o “TI y soporte \[administrador IAM, transversal de plataforma\]”. Esta notación evita crear actores nuevos para cada cargo o permiso

## **2\. Actores y grupos de interés identificados**

| Grupo de interés | Actores | Tipo y contexto | Aplicación documental |
| :---- | :---- | :---- | :---- |
| **Dirección y control** | Directorio; Gerencia General; Contraloría. | **Vinculación interna; decisión o control; contexto Retail, Emisor o transversal según el mandato.** | 2.4: influencia e interés. 3.2: decisiones, controles y aprobaciones. 3.4: gobernanza y apoyo. |
| **Propiedad** | Grupo familiar controlador; fondos de inversión. | **Parte interesada vinculada a la propiedad; estratégica y no operativa.** | 2.4: influencia e interés. 3.2: restricciones y decisiones mayores. 3.4: estrategia de involucramiento. |
| **Negocios y operación** | Comercial; Canales Digitales; Logística; Negocio Financiero. | **Interno; negocio; contexto Retail o Emisor según el actor y el flujo.** | 2.4: intereses y tensiones. 3.2: alcance funcional. 3.4: participación directa y validación. |
| **Soporte tecnológico y control operacional** | TI; Prevención de Pérdidas. | **Interno; técnico o control operacional; contexto transversal o Retail.** | 2.4: necesidades y riesgos. 3.2: soporte y controles. 3.4: habilitación técnica y seguimiento. |
| **Operación de tienda** | Jefaturas; vendedores; cajeros; reposición y bodega. | **Interno; negocio operacional; contexto Retail.** | 2.4: problemas operativos. 3.2: interacciones en alcance. 3.4: adopción, pruebas y capacitación. |
| **Clientes y terceros operacionales** | Clientes; titulares de tarjeta; vendedores de marketplace; proveedores tecnológicos y logísticos; administradores de centros comerciales; repositores externos. | **Externo; negocio o apoyo; contexto Retail o Emisor según la interacción.** | 2.4: expectativas e impacto. 3.2: canales e intercambios en alcance. 3.4: participación por flujo. |
| **Organismos externos** | Autoridad financiera; autoridad de protección al consumidor; autoridad tributaria. | Externo; regulador o fiscalizador; contexto definido por su competencia. | 2.4: exigencias. 3.2: reportes y evidencias exigibles. 3.4: validación de cumplimiento cuando corresponda. |

### **Sistemas y plataformas que interactúan con los servicios**

En este análisis, “sistema actor” significa una plataforma externa al límite de los servicios de aplicación; no implica que su proveedor sea necesariamente externo a Ancoa. Las etiquetas indican qué decisión está fija y cuál requiere prueba. Los sistemas listados se integran o conviven con los servicios; no se cuentan entre los trece servicios R/F/X.

**SE CONSERVAN —** ERP/DTE: permanece como único emisor tributario. R-01 y R-05 se integran con ERP/DTE; R-08 coordina los documentos asociados a devoluciones.

**SE CONSERVAN —** Marketplace vigente: no se reemplaza. R-07 integra y gobierna la relación con vendedores; R-04 coordina los pedidos y R-08 la posventa; R-06 recibe información para comisiones y liquidaciones cuando corresponde.

**SE CONSERVA —** WMS principal: continúa como autoridad de ejecución física donde opera. R-02, R-03 y R-04 se integran con él. La extensión a Concepción queda sujeta a evaluación.

**REEMPLAZO OBLIGATORIO —** Plataforma financiera de 2011: F-01, F-02 y F-03 asumirán sus responsabilidades mediante olas de migración antes del fin de soporte anunciado. El ERP/DTE mantiene la emisión tributaria.

**REEMPLAZO PROPUESTO —** POS de tienda de 2014: como no está acreditada la operación offline actual, se asume que falta y se plantea adquirir o desarrollar un POS que sí la demuestre. R-01 entrega precios; R-03 recibe movimientos; R-05 registra y concilia ventas; F-01 requiere conectividad para originar crédito nuevo.

**DECISIÓN CONDICIONAL —** Sistema central de retail de 2009: en el Escenario A se mantiene e integra durante la transición; en el Escenario B se reemplaza por etapas si se demuestra una brecha y existe una transición viable. R-01, R-02 y R-03 se coordinan con sus datos y funciones durante la coexistencia.

**DECISIÓN CONDICIONAL —** Comercio electrónico de 2019: se mantiene e integra si supera pruebas de latencia, disponibilidad, picos de demanda y consistencia de pedidos; si falla la plataforma, se reemplaza. Si falla la fuente de inventario o su interfaz, se corrige esa dependencia. Interactúa con R-01, R-03, R-04 y R-05.

**DECISIÓN CONDICIONAL —** Fidelización de 2017: R-09 integra la plataforma solo si supera la prueba de separación de datos Retail–Emisor; si no, se reemplaza.

**SIN ASIGNAR —** Novena plataforma: no se le adjudican servicios ni conexiones hasta identificarla.

**NO SON PLATAFORMAS EXTERNAS —** Precios y promociones se incorporan como capacidad nueva de R-01. El middleware, el bus de eventos y los adaptadores forman parte de la plataforma técnica C3; Kafka es una alternativa por evaluar. No son actores humanos ni sistemas externos del inventario.

### **Actores humanos y terceros con interacción directa**

| Actor | Relación y contexto | Rol en la interacción | Interacción directa con el sistema | Servicios involucrados |
| :---- | :---- | :---- | :---- | :---- |
| Cliente / consumidor | Externo · Retail o Emisor | Comprador; receptor; solicitante; titular o deudor según el flujo. | Consulta oferta y disponibilidad; crea o recibe pedidos; solicita posventa; solicita crédito; consulta estado y evidencia que le corresponda. | R-01, R-03, R-04, R-08, R-09; F-01, F-02, F-03. |
| Personal de venta y caja | Interno · Retail | Vendedor; cajero; vendedor habilitado para iniciar una gestión de crédito. | Registra ventas; consulta precios e inventario; prepara pedidos; inicia crédito solo con autorización; opera en contingencia definida. | R-01, R-03, R-04, R-05, R-06; F-01 bajo autorización. |
| Jefaturas de tienda o departamento | Interno · Retail | Supervisión; aprobación; seguimiento de metas y excepciones. | Aprueba ajustes y excepciones; consulta indicadores; valida cumplimiento y atribución de operaciones. | R-01 a R-06 y R-08, según permisos. |
| Operación de sala y bodega de tienda | Interno · Retail | Reposición; recepción; custodia; preparación; inspección de devoluciones. | Confirma recepción, movimiento, preparación, entrega a retiro y recepción de devoluciones. | R-02, R-03, R-04 y R-08. |
| Operación de centros de distribución | Interno · Retail | Recepción; almacenamiento; picking; despacho; control de almacén. | Publica movimientos, preparación y despacho; recibe instrucciones y confirma hitos operativos. | R-02, R-03 y R-04. |
| Prevención de Pérdidas | Interno · Retail · control operacional | Conteo cíclico; investigación de merma; validación de ajustes. | Consulta diferencias; registra hallazgos; valida ajustes de inventario con evidencia. | R-03. |
| Comercial y compras | Interno · Retail | Categorías; surtido; gestión de precios y promociones; compras. | Administra artículos, oferta, vigencias, precios y promociones; consulta abastecimiento. | R-01 y R-02. |
| Logística y planificación | Interno · Retail | Planificación de abastecimiento; reposición; asignación y coordinación logística. | Planifica reposición; consulta existencias; asigna nodos y coordina cumplimiento. | R-02, R-03 y R-04. |
| Marketing y canales digitales | Interno · Retail | Administración de sitio/app; campañas; fidelización; operación de canal. | Publica oferta; configura campañas; consulta perfiles Retail; no accede a datos financieros. | R-01, R-04, R-07 y R-09. |
| Administración y finanzas | Interno · Retail | Conciliación; documentos tributarios; comisiones; liquidaciones marketplace. | Consulta ventas asentadas; recibe documentos; revisa comisiones y liquidaciones; gestiona conciliaciones. | R-05, R-06 y R-07. |
| Atención al cliente Retail | Interno · Retail | Agente de mesón; reclamos; cambios; devoluciones; garantía legal. | Busca ventas; abre y actualiza casos; comunica resolución; registra recepción e inspección. | R-04, R-07 y R-08. |
| Negocio financiero / Emisor | Interno · Emisor | Originación; riesgo; operación financiera; cartera; cobranza; repactación. | Evalúa y autoriza crédito; administra cartera; confirma condiciones y repactaciones; consulta evidencia. | F-01, F-02 y F-03. |
| Control interno, cumplimiento y auditoría | Interno · transversal controlado | Revisión de cumplimiento; custodio y aprobador de cruces; revisión probatoria. | Consulta evidencia; aprueba finalidades; revisa cruces Retail–Emisor y decisiones permitidas o denegadas. | F-03 y X-01; controles de R-01, R-05 y R-09. |
| TI y soporte | Interno · transversal de plataforma | Administración técnica; soporte; seguridad; IAM; observabilidad. | Opera configuración, integraciones, identidad y monitoreo; no modifica reglas de negocio por privilegio técnico. | Todos los servicios como soporte; no es servicio de negocio. |
| Vendedor marketplace | Externo · Retail | Publicador de oferta; responsable de cumplimiento; contraparte de posventa y liquidación. | Publica oferta; recibe pedidos pertinentes; informa estados; gestiona devoluciones y liquidaciones. | R-04, R-07 y R-08. |
| Repositor externo de proveedor | Externo · Retail | Reposición y exhibición de productos de su marca. | Registra o confirma reposición y recepción con acceso acotado por organización y contrato. | R-01 y R-02, cuando corresponda. |
| Transportista | Externo · Retail | Retiro; traslado; entrega; actualización de hitos e incidencias. | Recibe instrucción; informa retiro, tránsito, entrega o incidencia; no administra el pedido completo. | R-04. |

Regla de nomenclatura: usar siempre el nombre de la primera columna. En una vista general, escribir solo el actor. Cuando una regla, permiso, caso de uso o responsabilidad dependa de una función particular, escribir Actor \[rol: nombre del rol\]. Ejemplos: Cliente / consumidor \[rol: deudor\] y Personal de venta y caja \[rol: cajero\]. POS, WMS, ERP/DTE y marketplace se registran en el inventario de sistemas integrados, no en la matriz de actores humanos. Si quedan fuera del límite del sistema modelado, se representan como sistemas actor. API Gateway, bus de eventos y adaptadores son componentes internos, no actores.

## **3\. Distribución del contenido entre 2.4, 3.2 y 3.4 preliminar**

(Esto es para entender donde se usara la info de cada cosa.)

### **3.1 Contenido para 2.4  Actores y grupos de interés**

Este apartado debe identificar quiénes tienen interés, influencia o afectación relevante respecto del proyecto. Debe conservar los grupos y nombres utilizados en el subdocumento 2, describir sus intereses, preocupaciones, poder de decisión y tensiones. Aquí corresponden, entre otras, las tensiones entre Negocio Financiero y Contraloría, Canales Digitales y Logística, Comercial y Operación de tienda, Marketing y Contraloría, y la presión de plazos regulatorios. No corresponde definir todavía servicios ni componentes técnicos.

## 

### **3.2 Contenido para 3.2  Delimitación del alcance por actor**

Este apartado debe explicar qué interacciones de cada actor quedan dentro del alcance funcional y cuáles quedan fuera o condicionadas. Los actores directamente operativos participan en procesos, consultas, decisiones o intercambios de información; Dirección y control participa mediante aprobación, supervisión y evidencia; Propiedad se considera como grupo de interés estratégico, no como usuario operativo; los organismos externos intervienen mediante obligaciones, fiscalización o recepción de evidencia cuando corresponda. Un actor no equivale a un servicio y su presencia no obliga a crear un servicio independiente.

## 

### **3.3 Contenido preliminar para 3.4  Participación y gestión de involucrados**

Este apartado debe anticipar cómo participará cada grupo en definición, validación, pruebas, adopción y control de la solución. Negocios y operación valida reglas y resultados; Operación de tienda participa en pruebas y adopción; TI habilita integración, seguridad y operación; Prevención de Pérdidas y Contraloría verifican controles y evidencia; Clientes y terceros operacionales participan por los flujos que les corresponden; Dirección y control resuelve decisiones mayores. Esta vista es preliminar y debe ajustarse cuando se aprueben alcance, plan de trabajo y responsables.

## 

# **PARTE II — SERVICIOS QUE SE DESPLEGARÁN**

Esta parte convierte las responsabilidades de negocio ya validadas en servicios de aplicación que la propuesta implementará. El orden de lectura es: cuatro promesas de Ancoa, responsabilidades A/B/C, servicios desplegables, integraciones y componentes técnicos. R y F identifican servicios: R corresponde a Retail y F al Emisor financiero. X identifica el servicio de frontera entre ambos negocios.

## **1\. Las cuatro promesas y las responsabilidades de negocio**

## 

El caso no solicita simplemente módulos de software. Ancoa debe poder cumplir y demostrar cuatro promesas diarias:

1\. Existencia: el producto existe y la disponibilidad publicada considera la calidad real del registro.

2\. Precio: el precio exhibido, publicado y cobrado coincide y puede acreditarse después.

3\. Entrega: el pedido tiene un estado único y llega en la fecha comprometida.

4\. Crédito: las condiciones informadas al cliente son las que este acepta y pueden demostrarse ante una autoridad.

Las responsabilidades A/B/C son el mapa de resultados que descompone esas promesas:

• A — Retail: responsabilidades del negocio minorista. A1 catálogo y oferta; A2 precios y promociones; A3 abastecimiento y reposición; A4 inventario, reservas y disponibilidad; A5 venta y conciliación; A6 canales digitales; A7 pedidos y cumplimiento; A8 marketplace; A9 posventa, cambios y garantías; A10 clientes y fidelización. A11 es el escenario de alta demanda que pone a prueba varias responsabilidades Retail.

• B — Emisor: responsabilidades del negocio financiero. B1 originación y autorización; B2 administración de cartera y cobranza; B3 repactaciones y modificaciones contractuales.

• C — Frontera y controles: C1 separación y gobierno de datos entre Retail y Emisor; C2 evidencia y trazabilidad probatoria; C3 integración, plataforma y operación técnica. C1 y C2 requieren servicios y controles; C3 se implementa como plataforma técnica.

| Promesa | Responsabilidades | Servicios desplegados | Evidencia verificable | Interacciones principales |
| :---- | :---- | :---- | :---- | :---- |
| Existencia: el producto existe y la disponibilidad publicada considera el registro real. | A3, A4 y A11 | R-02, R-03, R-04 y R-07 | Exactitud por categoría y nodo; disponibilidad comprometible; reservas; cancelaciones por falta de existencia. | R-02/WMS → R-03 → R-04/R-07; R-08 actualiza reintegro. |
| Precio: el precio exhibido, publicado y cobrado coincide. | A1, A2 y C2 | R-01, R-05 y R-06 | Historial de precio publicado; estado de etiqueta; venta conciliada; atribución auditable. | R-01 → canales/POS; R-05 → R-06; ERP/DTE recibe documentos. |
| Entrega: el pedido tiene un estado único y llega en la fecha comprometida. | A3, A6, A7 y A11 | R-02, R-03, R-04, R-07 y R-08 | Fecha prometida; estado único; nodo; despacho/retiro; tasa de cumplimiento. | R-04 coordina R-03, WMS, transportista, comercio electrónico y marketplace. |
| Crédito: las condiciones informadas son las aceptadas y pueden demostrarse. | B1, B2, B3, C1 y C2 | F-01, F-02, F-03 y X-01 | Versión precontractual; consentimiento; expediente recuperable; auditoría de cruces. | F-01/F-02 consultan F-03; X-01 autoriza y audita Retail–Emisor. |

La tabla anterior no introduce capacidades nuevas. Relaciona el mapa de responsabilidades validado con servicios concretos y con evidencia que permitirá verificar cada promesa.

## **2\. Catálogo definitivo de servicios desplegables**

## 

### **2.1 Criterio de implementación**

## 

### **La propuesta desplegará trece servicios de aplicación: nueve Retail, tres del Emisor y uno de frontera. Cada servicio tendrá una responsabilidad propia, contrato de entrada y salida, datos bajo autoridad definida, actores consumidores, interacciones identificadas y unidad de despliegue. Esta lista es el alcance técnico de servicios de aplicación.**

Un servicio puede apoyarse en módulos internos de código. Un microservicio es una forma de operar un servicio con autonomía de despliegue, datos, escalamiento y fallas. La decisión de usar microservicios describe la forma de operación; no cambia la lista de responsabilidades que se implementará.

Durante la actividad de inception de cada servicio se confirmarán: propietario de negocio, propietario técnico, datos de autoridad, contratos, eventos, errores, seguridad, métricas, dependencia de sistemas existentes, estrategia de pruebas y criterio de aceptación. La ficha siguiente define lo que hace y lo que no hace cada servicio.

### **2.2 R-01 · Catálogo, precios y promociones**

### **Promesa y responsabilidades: respalda precio y parte de existencia; cubre A1 y A2, y produce evidencia para C2.**

Actores y roles: Comercial \[rol: gestión de categorías y precios\]; Canales Digitales \[rol: publicación\]; Operación de tienda \[rol: reposición de etiquetas\]; Administración y finanzas \[rol: consulta de evidencia\].

Datos y operaciones: artículos, atributos, categorías, precios, promociones, vigencias, canales, estado de etiqueta e historial de publicación. Expone consulta de oferta y precio vigente, publicación por canal y recuperación histórica.

Interacciones: alimenta R-03, R-04, R-05 y R-07; recibe resultados de venta de R-05; integra el sistema central de Retail y el motor de precios que hoy debe construirse.

Dentro y fuera: incluye maestro comercial, reglas de precio, distribución y trazabilidad de publicación. No calcula reservas, no registra ventas, no administra remuneraciones y no contiene fideli 	zación.

Fundamento: Caso 09, numerales 4.1, 4.2, 9.1 y 9.3; el motor de precios y promociones figura como una función que debe existir.

### **2.3 R-02 · Abastecimiento y reposición**

### **Promesa y responsabilidades: sostiene la promesa de existencia y entrega; cubre A3 y participa en A4 y A7.**

Actores y roles: Comercial \[rol: surtido\]; Logística y planificación \[rol: planificación de abastecimiento\]; Operación de centros de distribución \[roles: recepción y despacho\]; Operación de tienda \[rol: reposición\]; Proveedor de mercadería \[rol: abastecimiento\].

Datos y operaciones: órdenes, transferencias, propuestas de reposición, recepciones, nodos, restricciones y necesidades de abastecimiento. Coordina órdenes y transferencias y entrega información a R-03.

Interacciones: consulta R-03; coordina con WMS y ERP/DTE; entrega disponibilidad de abastecimiento a R-04 y estados a R-07 cuando corresponda.

Dentro y fuera: incluye planificación y coordinación de reposición. No reemplaza automáticamente la ejecución física del WMS principal ni convierte las planillas de Concepción en autoridad permanente sin evaluación.

Fundamento: Caso 09, numerales 4.3, 5.1, 9.1 y 14.1; el centro de Concepción opera con planillas y su incorporación a WMS debe evaluarse.

### **2.4 R-03 · Inventario, reservas y disponibilidad**

### 

### **Promesa y responsabilidades: es la autoridad de la disponibilidad comprometible; cubre A4 y sostiene A11.**

Actores y roles: Operación de tienda \[roles: conteo, recepción y custodia\]; Operación de centros de distribución \[roles: ubicación, picking y despacho\]; Prevención de Pérdidas \[rol: investigación de diferencias\]; Logística y planificación \[rol: disponibilidad\]; Cliente \[rol: consultante de disponibilidad\].

Datos y operaciones: existencias por nodo, conteos, ajustes autorizados, causas de diferencia, reservas, disponible para vender, margen de confianza y estado de inventario. Expone disponibilidad y registra la decisión de comprometer unidades.

Interacciones: recibe movimientos de R-02, WMS, POS y devoluciones de R-08; entrega disponibilidad a R-01, R-04 y R-07; publica indicadores de exactitud.

Dentro y fuera: incluye normalización, reservas y cálculo de disponibilidad comprometible. WMS principal sigue siendo autoridad de ejecución física donde existe; ERP/DTE mantiene sus responsabilidades contables y tributarias. El registro no se considera perfecto: el servicio incorpora la incertidumbre conocida por categoría y nodo.

Fundamento: Caso 09, numerales 4.4, 5.1, 9.1, 9.2 y 18; RT-05.20 y RT-05.21. El 12,4 % de discrepancia de conteo es una condición del problema, no una cifra que el servicio pueda ignorar.

### **2.5 R-04 · Pedidos y cumplimiento omnicanal**

### **Promesa y responsabilidades: entrega un estado único y una fecha comprometida; cubre A6 y A7, y participa en A11.**

Actores y roles: Cliente \[rol: comprador o receptor\]; Personal de venta y caja \[rol: vendedor\]; Operación de tienda \[rol: preparación y retiro\]; Operación de centros de distribución \[rol: despacho\]; Logística \[rol: planificación\]; Atención al cliente retail \[rol: consulta\]; Transportista \[rol: entrega\]; Vendedor marketplace \[rol: seguimiento cuando corresponda\].

Datos y operaciones: pedido, líneas, estado, nodo de preparación, reserva, promesa de entrega, despacho, retiro, entrega, quiebre y compensación. Es la autoridad del ciclo del pedido.

Interacciones: solicita reservas a R-03; consulta R-01; coordina POS, comercio electrónico, WMS, marketplace y transportistas; entrega estado a R-06, R-07 y R-08.

Dentro y fuera: incluye orquestación del ciclo del pedido y selección de nodo por costo total de servir. No es API Gateway, no reemplaza WMS ni administra la relación contractual completa con el transportista.

Fundamento: Caso 09, numerales 4.6, 4.7, 9.4, 9.5 y 18; A11 se prueba durante el evento anual.

### **2.6 R-05 · Registro y conciliación de ventas**

### **Promesa y responsabilidades: acredita la venta y sus reversas; cubre A5 y aporta evidencia a C2.**

Actores y roles: Personal de venta y caja \[roles: vendedor y cajero\]; Jefaturas de tienda \[rol: supervisión\]; Cliente \[rol: comprador\]; Administración y finanzas \[rol: conciliación\].

Datos y operaciones: venta confirmada, reversa, pago, caja, desconexión, conciliación y estado de documento tributario. El POS es canal de borde; el servicio registra y concilia el hecho de venta.

Interacciones: recibe operaciones de POS y comercio electrónico; entrega hechos a R-06 y R-08; integra ERP/DTE, que mantiene la emisión tributaria.

Dentro y fuera: incluye registro y conciliación. No abre crédito nuevo sin conectividad, no emite documentos tributarios por cuenta propia y no calcula la comisión final de R-06.

Fundamento: Caso 09, numerales 4.5, 5.1, 9.3 y 18; ERP/DTE permanece como único emisor de documentos tributarios.

### **2.7 R-06 · Atribución de ventas y comisiones**

### **Promesa y responsabilidades: corrige el incentivo que afecta el despacho desde tienda; cubre la responsabilidad de atribuir ventas dentro de A5 y A7.**

Actores y roles: Personal de venta y caja \[rol: vendedor\]; Jefaturas de tienda \[rol: validación\]; Administración y finanzas \[rol: política y recepción de base de comisión\].

Datos y operaciones: venta, pedido, canal, tienda que prepara, vendedor atribuible, regla de atribución, comisión, reversa y auditoría. Expone la base calculada al sistema empresarial que mantiene remuneraciones.

Interacciones: consume hechos de R-04 y R-05; consulta reglas de R-01; entrega resultados a Administración y finanzas.

Dentro y fuera: incluye atribución multicanal y cálculo de la base de comisión. No administra remuneraciones ni decide políticas comerciales por sí mismo.

Fundamento: Caso 09, numerales 4.7, 9.5 y 18; el despacho desde tienda no debe castigar a la tienda que entrega la unidad.

### **2.8 R-07 · Integración y gobierno de marketplace**

### 

### **Promesa y responsabilidades: permite cumplir existencia, entrega y posventa cuando participa un vendedor externo; cubre A8.**

Actores y roles: Vendedor marketplace \[roles: publicación, cumplimiento y posventa\]; Canales Digitales \[rol: administración\]; Administración y finanzas \[rol: liquidación\]; Atención al cliente retail \[rol: consulta y atención\].

Datos y operaciones: vendedor, oferta, estado de habilitación, nivel de servicio, pedido intermediado, devolución, liquidación y recobro B2B. Expone estados comprensibles para el vendedor y para Ancoa.

Interacciones: integra la plataforma marketplace de 2022; consulta R-01, R-03 y R-04; recibe casos de R-08; entrega información a R-06 y Administración y finanzas.

Dentro y fuera: incluye integración, reglas de gobierno, medición y coordinación de vendedores. No reemplaza la plataforma marketplace vigente ni opera la logística interna del vendedor.

Fundamento: Caso 09, numerales 4.8, 5.1, 9.6, 9.7 y 18; la plataforma marketplace se mantiene e integra.

### **2.9 R-08 · Posventa, garantías y devoluciones**

### 

### **Promesa y responsabilidades: resuelve la relación posterior a la venta; cubre A9 y corrige una causa de diferencias de inventario.**

Actores y roles: Cliente \[rol: solicitante de cambio, devolución o garantía\]; Atención al cliente retail \[rol: agente de mesón\]; Operación de tienda \[rol: recepción e inspección\]; Vendedor marketplace \[rol: contraparte cuando corresponda\].

Datos y operaciones: caso, venta, motivo, recepción, inspección, elegibilidad, cambio, nota de crédito, garantía, destino de unidad y comunicación de resolución.

Interacciones: consulta R-05; publica aptitud de reintegro a R-03; entrega evidencia de devolución a R-07; coordina ERP/DTE y sistemas de vendedores.

Dentro y fuera: incluye recepción y resolución frente al cliente. No posterga la respuesta al consumidor hasta resolver la conciliación B2B y no delega automáticamente la garantía legal al fabricante.

Fundamento: Caso 09, numerales 4.8, 4.9, 9.6, 9.7 y 18\.

### **2.10 R-09 · Clientes y fidelización Retail**

### **Promesa y responsabilidades: permite reconocer al cliente y gestionar fidelización dentro de Retail; cubre A10 y respeta C1.**

Actores y roles: Cliente \[roles: comprador y participante de fidelización\]; Marketing y canales digitales \[roles: segmentación y campañas\]; Atención al cliente retail \[rol: consulta\]; Control interno, cumplimiento y auditoría \[rol: revisión de uso\].

Datos y operaciones: identificador Retail, deduplicación, puntos, segmentos, campañas y preferencias. Expone perfiles comerciales y operaciones de fidelización con finalidad declarada.

Interacciones: consulta R-01, R-04 y R-05; se relaciona con X-01 solo mediante cruces autorizados; integra o reemplaza el sistema de fidelización de 2017\.

Dentro y fuera: incluye fidelización Retail. No incorpora saldos, mora, cupo ni comportamiento de pago del Emisor a un perfil comercial.

Fundamento: Caso 09, numerales 5.1, 9.10 y 18; el sistema de fidelización actual se reemplaza o integra y la separación financiera es obligatoria.

### **2.11 F-01 · Originación y autorización de crédito**

### 

### **Promesa y responsabilidades: cumple la promesa sobre condiciones de crédito; cubre B1.**

Actores y roles: Cliente \[rol: solicitante o titular\]; Negocio Financiero \[roles: originación y riesgo\]; Personal de venta y caja \[rol: vendedor habilitado\], solo con autorización del Emisor.

Datos y operaciones: solicitud, identificación financiera, evaluación, cupo, decisión, condiciones precontractuales y autorización.

Interacciones: opera desde POS y mesón financiero; consulta F-03 antes de confirmar; integra la plataforma financiera reemplazada y comunica el resultado a R-05.

Dentro y fuera: incluye evaluación, originación y autorización. No abre crédito nuevo offline; una contingencia con cupo previamente aprobado queda condicionada a la prueba de factibilidad definida en el caso.

Fundamento: Caso 09, numerales 4.5, 4.10, 9.8 y 18; la plataforma financiera de 2011 se reemplaza por obsolescencia y plan de remediación.

### **2.12 F-02 · Cartera, cobranza y repactaciones**

### 

### **Promesa y responsabilidades: administra la relación financiera posterior a la originación; cubre B2 y B3.**

Actores y roles: Cliente \[rol: deudor\]; Negocio Financiero \[roles: cartera, cobranza y repactación\]; Control interno, cumplimiento y auditoría \[rol: revisión\].

Datos y operaciones: cuenta, saldo, cuotas, pagos, mora, comunicaciones, cobranza, nueva condición y estado de repactación.

Interacciones: consulta F-03 antes de confirmar repactaciones; integra la nueva plataforma financiera; expone estados financieros al actor autorizado.

Dentro y fuera: incluye cartera viva, cobranza y repactación. No comparte saldos con R-09 ni convierte la migración de cartera en una funcionalidad permanente del servicio.

Fundamento: Caso 09, numerales 4.11, 5.1, 9.9 y 17.5; la migración es un programa de transición con conciliación, retorno y comunicación.

### **2.13 F-03 · Consentimiento y evidencia financiera**

### 

### **Promesa y responsabilidades: demuestra qué información se entregó y qué aceptó el cliente; cubre B1, B3 y C2.**

Actores y roles: Cliente \[rol: titular o solicitante\]; Negocio Financiero \[rol: contraparte contractual\]; Control interno, cumplimiento y auditoría \[rol: revisión probatoria\].

Datos y operaciones: versión de información precontractual, aceptación, consentimiento, fecha, relación con operación y expediente recuperable.

Interacciones: recibe solicitudes de F-01 y F-02; responde si existe evidencia suficiente; entrega evidencia a auditoría y autoridades cuando corresponda.

Dentro y fuera: incluye custodia, recuperación, integridad, retención y control de acceso. No administra el saldo ni reemplaza F-01/F-02.

Fundamento: Caso 09, numerales 4.10, 4.11, 9.8, 9.9, 9.10 y 18; los consentimientos deben ser recuperables durante el plazo exigido.

### **2.14 X-01 · Autorización y auditoría de cruces Retail–Emisor**

### 

### **Promesa y responsabilidades: implementa C1 y la parte de C2 relativa a cada cruce entre negocios.**

Actores y roles: Control interno, cumplimiento y auditoría \[rol: custodio y aprobador\]; dueños de datos Retail y Emisor \[rol: autorización\]; servicio solicitante \[rol: finalidad declarada\].

Datos y operaciones: finalidad, base de autorización, solicitante, atributos mínimos, respuesta, fecha y evidencia del cruce. Devuelve solo el dato mínimo necesario o una respuesta puntual.

Interacciones: recibe solicitudes de R-09, F-01, F-02 u otros servicios autorizados; no consulta directamente las bases de otro negocio; registra cada decisión.

Dentro y fuera: incluye autorización, minimización, auditoría y denegación por omisión. No crea un maestro único de clientes, no expone atributos financieros a Marketing y no reemplaza IAM.

Fundamento: Caso 09, numerales 2, 9.10 y 18; la separación de datos debe ser técnica, documentada y auditable.

## **3\. Componentes de plataforma e integración**

## **C3 se implementará mediante despliegues técnicos que soportan los trece servicios:**

• API Gateway: entrada, ruteo, autenticación técnica y políticas de exposición. No es un servicio de negocio.

• Bus de eventos y adaptadores: transporte de eventos y conexión con POS, comercio electrónico, WMS, ERP/DTE, marketplace y plataforma financiera. Kafka puede evaluarse como tecnología para el bus, pero no está fijado como producto; el componente no posee reglas de dominio.

• IAM y gestión de secretos: identidad, autorización técnica, segregación de Retail y Emisor y mínimo privilegio.

• Observabilidad: logs, métricas, trazas, alertas y evidencia operacional.

• Plataforma híbrida: componentes de nube pública y componentes locales en tiendas, centros de distribución y sistemas que deban permanecer allí, conforme al despliegue híbrido obligatorio.

• Migración y convivencia, alineada con los escenarios del análisis de plataformas: en el Escenario A se mantiene e integra el sistema central de retail durante la transición; en el Escenario B se reemplaza por etapas solo con brecha documentada y transición viable. El POS actual no tiene operación offline acreditada en la información disponible, por lo que se asume que esa capacidad falta y se adquiere o desarrolla un POS que la demuestre. R-05 recibe y concilia las ventas del POS, incluso las registradas durante una desconexión; ello no autoriza originar nuevos créditos offline: F-01 requiere conectividad y cualquier contingencia con cupo ya aprobado debe superar su prueba de factibilidad. El comercio electrónico se mantiene e integra si supera pruebas de latencia, disponibilidad, picos de demanda y consistencia de pedidos; si falla la plataforma, se reemplaza; si falla la fuente de inventario o su interfaz, se corrige esa dependencia. Se reemplaza la plataforma financiera de 2011 mediante olas F-01/F-02/F-03; se mantienen ERP/DTE como único emisor tributario, marketplace y WMS principal, integrados con sus servicios; la extensión de WMS a Concepción se evalúa. R-09 integra fidelización si supera la prueba de segregación; si no, se reemplaza. R-01 incorpora la capacidad de precios y promociones. La plataforma novena queda sin servicio ni integración asignados hasta identificarla. Los incrementos pueden ejecutarse iterativamente con la operación en marcha; las prioridades se revisan por riesgo, pero los cambios al catálogo de trece servicios requieren aprobación.

## **4\. Servicios, módulos y microservicios**

Servicio de aplicación: unidad desplegable que ofrece una responsabilidad mediante contratos explícitos. El catálogo comprometido está formado por nueve servicios Retail (R), tres servicios del Emisor financiero (F) y un servicio de frontera entre ambos (X). La nomenclatura se detalla en el Anexo A.

Módulo: unidad interna de organización de código dentro de un servicio. Puede contener varias funciones y compartir despliegue, datos y operación con otros módulos del mismo servicio. No es una caja adicional del catálogo.

Microservicio: servicio de aplicación operado con autonomía de despliegue, datos, escalamiento y fallas, contratos explícitos y capacidad de evolución independiente. La lista de servicios se mantiene en trece; la decisión de empaquetar cada servicio como uno o más procesos se documentará en el diseño técnico, sin alterar su responsabilidad ni duplicar servicios.

## **5\. Trazabilidad y decisiones abiertas**

## 

La trazabilidad vigente se expresa directamente desde las responsabilidades A/B/C hacia los servicios R, F y X. No se utilizan catálogos históricos ni identificadores alternativos para definir el alcance.

Correspondencia principal: A1/A2 → R-01; A3 → R-02; A4 → R-03; A5 → R-05/R-06; A6/A7 → R-04; A8 → R-07; A9 → R-08; A10 → R-09; A11 → escenario de R-01/R-03/R-04/R-07; B1 → F-01/F-03; B2/B3 → F-02/F-03; C1 → X-01; C2 → R-01/F-03/X-01; C3 → plataforma e integración.

Antes de trasladar este catálogo a T7-03 quedan abiertas únicamente estas verificaciones: confirmar la asignación individual de cada RF/SUP; validar la fuente autoritativa de artículo, precio, inventario, DTE, comisión y saldo; confirmar los contratos de integración; probar la contingencia de F-01; y ratificar la custodia de X-01. Estas verificaciones no cambian el catálogo de trece servicios, pero pueden ajustar contratos, etapas o sistemas integrados.

## **6\. Guía de trabajo para IA**

Usar R/F/X para referirse a servicios y A/B/C para referirse a responsabilidades y controles. No llamar capacidades a los servicios ni llamar módulos a los servicios. Para cada servicio comprobar siempre: promesa, responsabilidad, actores y roles, autoridad de datos, operaciones, interacciones, inclusión, exclusión, fundamento y evidencia.

No contar API Gateway, bus de eventos, IAM, observabilidad, WMS, ERP/DTE ni marketplace como servicios de negocio. Mantener Retail y Emisor separados. No inventar requisitos, cifras ni autoridades. Si una decisión está abierta, registrarla como verificación pendiente sin crear un servicio provisional. No modificar los subdocumentos T7 hasta completar el remapeo RF/SUP y la aprobación humana.

# 

# **ANEXO A — NOMENCLATURA DEL CATÁLOGO DE SERVICIOS**

## **Este anexo define cómo leer los códigos del catálogo. El código no representa una capacidad, un actor ni un módulo: identifica un servicio de aplicación que la propuesta desplegará.**

## 

## **R — Servicios Retail**

R significa Retail. Estos servicios atienden el negocio comercial de Ancoa: productos, precios, abastecimiento, inventario, pedidos, ventas, marketplace, posventa y fidelización.

R-01 · Catálogo, precios y promociones

R-02 · Abastecimiento y reposición

R-03 · Inventario, reservas y disponibilidad

R-04 · Pedidos y cumplimiento omnicanal

R-05 · Registro y conciliación de ventas

R-06 · Atribución de ventas y comisiones

R-07 · Integración y gobierno de marketplace

R-08 · Posventa, garantías y devoluciones

## **R-09 · Clientes y fidelización Retail**

## 

## **F — Servicios del Emisor financiero**

F significa Emisor financiero. Estos servicios atienden el negocio de crédito fiscalizado y mantienen sus datos, reglas y evidencias separados de Retail.

F-01 · Originación y autorización de crédito

F-02 · Cartera, cobranza y repactaciones

F-03 · Consentimiento y evidencia financiera

## 

## **X — Servicio de frontera Retail–Emisor**

X identifica un servicio que controla cruces autorizados entre Retail y Emisor. No crea un maestro común de clientes ni mezcla sus datos.

### **X-01 · Autorización y auditoría de cruces Retail–Emisor**

### 

### **Regla de lectura**

Cuando el documento menciona R, F o X, se refiere a la familia del servicio. Cuando menciona un código completo, como R-03 o F-02, se refiere a un servicio específico. Las plataformas existentes —POS, comercio electrónico, sistema central de retail, plataforma financiera, fidelización, WMS, ERP/DTE y marketplace— no reciben códigos R/F/X: son sistemas integrados durante la coexistencia o sujetos al destino definido para cada escenario, no servicios de negocio del catálogo. El middleware, API Gateway, bus de eventos, adaptadores, IAM y observabilidad son componentes técnicos de C3, no servicios separados. La capacidad nueva de precios y promociones corresponde a R-01.

Los servicios son unidades desplegables comprometidas. La decisión posterior de implementarlos como uno o más microservicios no agrega códigos ni modifica la lista.

