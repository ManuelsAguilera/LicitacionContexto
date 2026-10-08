# Insumos para redactar 3.3 Esquema de solución y 3.4 Explicación de la Solución (sd-03)

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

> **Aviso (2026-10-08).** Las secciones 3.3 y 3.4 las elabora otro integrante del equipo. Este archivo conserva los códigos antiguos (R-01 a X-01), que se leen con la tabla de `divisiones_negocio_servicios_sd-03.md`. Las fuentes que cita (`descripcion_alcance_producto.md`, `insumos_3.2.md`, `Análisis de actores…`) están ahora en `historico/` con el prefijo `no_usar_` y sus decisiones vigentes están en `ficha_alcance_sd-03.md`. Verificar cada dato contra `sd-03.tex` y los Anexos A a D.

Documento de contexto, no es entregable. Reúne lo necesario para redactar 3.3 y 3.4 en `02_Propuesta/latex_final/sd-03.tex`. Los diagramas se **especifican**: los dibuja el equipo. Todo dato tiene su fuente; lo marcado **(S)** es propuesta del asistente, por confirmar. Fecha: 2026-10-06.

Contenido: 0. Exigencias y reglas · 1. Lista canónica de componentes · 2. Contenido de 3.3 (diagramas E1 a E4) · 3. Contenido de 3.4 · 4. Tabla de mapeo con el sd-04 · 5. Cifras y puntos abiertos.

---

## 0. Exigencias y reglas

### 0.1 Qué pide el Comunicado 10

- **3.3 Esquema de solución:** "Uno o varios esquemas que presenten el modelo conceptual de la solución. Cada diagrama se explica en el texto; si es complejo o grande, se explica por partes".
- **3.4 Explicación de la Solución:** "Descripción de la solución según la operación o el negocio, y su coherencia con el problema definido en el Capítulo 2. Incluye la estrategia para obtener el apoyo de los grupos de interés clave identificados en 2.4. Debe mapear al 100 % con la Arquitectura Lógica (4.1): los componentes tienen el mismo nombre en ambos capítulos".
- **4.1 Arquitectura lógica (sd-04):** "debe estar mapeada al 100 % con el Esquema de Solución (3.3) y la Explicación de la Solución (3.4)". El Comunicado sugiere además incluir en 4.2 "una tabla de mapeo que muestre, para cada componente, su correspondencia entre esquema de solución (3.3), arquitectura lógica (4.1) y componente físico (4.2)".

Consecuencia: los nombres de la sección 1 de este documento son la **fuente de nombres** del sd-04. Si cambian aquí, cambian allá (RR-07).

### 0.2 Reparto entre 3.3, 3.4 y el sd-04

| Sección | Qué responde | Qué no lleva |
| :-- | :-- | :-- |
| 3.3 Esquema de solución | Qué piezas tiene la solución y cómo se relacionan (modelo conceptual) | Tecnologías, productos, protocolos, nube ni sitios |
| 3.4 Explicación de la Solución | Cómo funciona la operación del negocio con esas piezas y por qué resuelve el problema del cap. 2; cómo se gana el apoyo de los interesados | Detalle técnico; repetir 3.2 |
| 4.1 Arquitectura lógica | Capas, límites de contexto, contratos, mensajería, seguridad | El "por qué de negocio" (ya está en 3.4) |
| 4.2 y 4.3 Arquitectura física y centros de datos | Dónde corre cada componente (nube, on-premise, sitio o región secundaria) | — |

**Regla práctica:** si una frase de 3.3 o 3.4 nombra una tecnología (Kafka, un proveedor de nube, una base de datos), va en el sd-04.

### 0.3 Reglas de redacción que más pesan

- **RR-10:** "texto y diagramas se combinan: el texto recorre, interpreta y concluye a partir de cada figura". Un capítulo técnico sin figuras integradas no cumple.
- **RR-11:** "Figura 3.N: …", citada antes de aparecer y explicada después.
- **RR-12:** diagramas grandes con vista general primero y luego explicación por partes, con un diagrama preparado para cada parte.
- **RR-13:** no se recorta una sección de una imagen mayor para usarla como detalle.
- **RR-14:** "Fuente: elaboración propia" en cada figura realmente insertada.
- **RR-07:** los mismos nombres que en la sección 1.
- **RR-09:** mencionar un estándar no basta; hay que mostrar cómo se cumple.
- **RR-22:** sin marcadores ni lenguaje académico.
- **Diagramas genéricos:** el Comunicado no acepta "diagramas genéricos que no correspondan a la solución propuesta". Cada caja debe ser un componente de Ancoa con su nombre.
- **Herramientas y nombres de archivo:** Graphviz (`.dot`) o PlantUML (`.puml`), exportados a PNG en `04_Adjuntos/diagramas/` como `diag-03-03_<tema>.png` (3.3) y `diag-03-04_<tema>.png` (3.4). No usar Mermaid.

### 0.4 Apoyo de clase (para justificar la forma, no el contenido)

- **FEP02, diapositiva 43:** el diagrama de contexto (la solución al centro y los actores y sistemas externos alrededor).
- **FEP01, diapositivas 16 y 17:** las vistas de una arquitectura; lógica frente a física.
- **FEP01, diapositivas 28 a 31:** capas y N capas.
- **FEP01, diapositivas 45 a 47:** arquitectura basada en eventos. Sirve para explicar en 3.4 cómo se propaga un cambio de precio o de existencia; sin nombrar productos.
- **FEP01, diapositivas 62 a 65:** estilos de diagrama: "actores en columnas, capas en filas" (estilo A) y "capas con microservicios y stack lateral" (estilo C).

---

## 1. Lista canónica de componentes (fuente de nombres para 3.3, 3.4 y 4.1)

### 1.1 Servicios de negocio (13)

| Código | Nombre canónico | Dominio | Autoridad de datos (resumen) |
| :-- | :-- | :-- | :-- |
| R-01 | Catálogo, precios y promociones | Retail | Artículos, precios, promociones, estado de etiqueta, historial publicado |
| R-02 | Abastecimiento y reposición | Retail | Órdenes, transferencias, recepciones, propuestas de reposición |
| R-03 | Inventario, reservas y disponibilidad | Retail | Existencias por nodo, reservas, disponible comprometible, margen de confianza |
| R-04 | Pedidos y cumplimiento omnicanal | Retail | Ciclo del pedido, nodo de preparación, promesa y estado de entrega |
| R-05 | Registro y conciliación de ventas | Retail | Venta confirmada, reversa, pago, caja, desconexión, estado del documento |
| R-06 | Atribución de ventas y comisiones | Retail | Regla de atribución, base de comisión |
| R-07 | Integración y gobierno de marketplace | Retail | Vendedor, oferta, nivel de servicio, pedido intermediado, devolución |
| R-08 | Posventa, garantías y devoluciones | Retail | Caso, inspección, resolución, garantía, reintegro |
| R-09 | Clientes y fidelización Retail | Retail | Identificador de cliente Retail, puntos, segmentos, campañas |
| F-01 | Originación y autorización de crédito | Emisor | Solicitud, evaluación, cupo, decisión, autorización |
| F-02 | Cartera, cobranza y repactaciones | Emisor | Cuenta, saldo, cuotas, pagos, mora, cobranza, repactación |
| F-03 | Consentimiento y evidencia financiera | Emisor | Versión precontractual, aceptación, consentimiento, expediente |
| X-01 | Autorización y auditoría de cruces Retail–Emisor | Frontera | Finalidad, base, solicitante, dato mínimo, decisión y evidencia de cada cruce |

Fuente: `descripcion_alcance_producto.md` §5.

### 1.2 Plataforma común (no son servicios de negocio)

| Código | Nombre canónico | Qué hace en el modelo conceptual |
| :-- | :-- | :-- |
| 1.14a | Plataforma de integración | Reemplaza las 14 interfaces punto a punto; transporta eventos y solicitudes entre servicios y sistemas |
| 1.14b | Catálogo de reglas de acuerdo por tipo de dato | Fija para cada dato su servicio autoridad, sus copias y su regla de reconciliación |
| 1.14c | Identidad y gestión de accesos | Identifica a cada persona y sistema; separa Retail y Emisor; acceso individualizado de los repositores |
| 1.14d | Observabilidad | Registra y sigue cada operación entre sistemas (identificador de correlación, Transversales RT-05.19) |

Nota para el sd-04: el análisis de actores menciona además una puerta de entrada (API Gateway) y la gestión de secretos. En el modelo conceptual van dentro de 1.14a y 1.14c; en 4.1 pueden aparecer como subcomponentes, con nombres que muestren su pertenencia.

### 1.3 Componentes en sitio, puntos de contacto y canales

| Nombre canónico | Qué es | Entregable |
| :-- | :-- | :-- |
| Punto de venta (POS) con operación sin conexión | Caja de las 22 tiendas, nueva, con 24 h de autonomía | 1.16 |
| Componente local de tienda | Gabinete con el cómputo que permite operar sin enlace y sincronizar al volver | 1.15.19 |
| Componente local del centro de distribución principal | Lo mismo en el centro de 42.000 m², con 24 h | 1.15.17 |
| Portal público | Catálogo, precio, disponibilidad, información precontractual y simulador; consulta de pedido | 1.31a, 1.31b |
| Portal del cliente | Compras, devoluciones, estado de cuenta y documentos | 1.32 |
| Vista del vendedor de marketplace | Estado de pedidos, devoluciones y evaluación | 1.33 |
| Portal del proveedor | Órdenes y recepciones | 1.34 |
| Aplicaciones móviles | Cliente, vendedor de sala, preparación de pedidos, conteo cíclico, recepción | 1.35 a 1.39 |

### 1.4 Sistemas que se conservan y actores externos

| Nombre canónico | Tipo | Relación con la solución |
| :-- | :-- | :-- |
| Sistema de gestión empresarial y facturación (ERP/DTE) | Sistema conservado | Único emisor tributario; integración crítica |
| Plataforma de marketplace | Sistema conservado | Integrada y gobernada por R-07 |
| Sistema de gestión de almacenes (WMS) del centro de distribución principal | Sistema conservado | Ejecuta lo físico; R-03 es la autoridad del disponible |
| Plataforma de comercio electrónico | Sistema evaluado e integrado | Publica la disponibilidad de R-03 y el precio de R-01 |
| Sistema de fidelización | Sistema evaluado e integrado | Se integra con R-09 tras la prueba de separación |
| Centro de distribución de Concepción (planillas) | Sitio que se mantiene como está | Entrega existencias a R-03 por carga estructurada |
| Clientes y titulares de tarjeta; vendedores de marketplace; proveedores (940); transportistas de última milla; repositores externos; administradores de centros comerciales | Actores externos | Interactúan por los canales o por integración |
| Autoridad del mercado financiero, autoridad de protección del consumidor, autoridad tributaria | Organismos externos | Reciben reportes o evidencia; fiscalizan |

Los sistemas que se retiran (sistema central de 2009, plataforma de crédito de 2011, POS de 2014) aparecen en 3.3 solo si el diagrama muestra la transición. En el modelo objetivo no figuran.

---

## 2. Contenido de 3.3 Esquema de solución

**Mensaje central.** La solución es un conjunto de 13 servicios con autoridad sobre sus datos, separados en dos dominios con una frontera explícita, conectados por una plataforma común que reemplaza las interfaces punto a punto, y prolongados hasta la tienda por un componente local que sigue operando sin enlace.

**Texto de caída sugerido para 3.3:** "El esquema de solución presenta el modelo conceptual: qué componentes tiene la solución, cómo se relacionan y qué los separa. Se muestra primero el contexto, luego la vista general y después cada parte por separado; la tecnología con que se construye cada componente se trata en el Capítulo 4."

### E1. Contexto de la solución (FEP02, diapositiva 43)

- **Muestra:**
  - Al centro, "Solución de Multitiendas Ancoa" como una caja.
  - Alrededor, los actores y sistemas externos de 1.4 con sus flujos principales, rotulados con lo que intercambian.
  - Los rótulos salen del mapa de flujos del Caso (cap. A): precio y catálogo, existencia, pedidos, documentos tributarios, evaluación y aceptación del crédito, devoluciones y reportes a las autoridades.
- **Conclusión del texto:** qué queda dentro y qué fuera de la solución. Esto conecta con las exclusiones de 3.2.3: el ERP, el marketplace y los transportistas quedan fuera, pero integrados.
- **Herramienta:** Graphviz (`neato` o `circo`).

### E2. Modelo conceptual general (vista general)

- **Estilo:** "actores en columnas, capas en filas" (FEP01, diapositiva 62).
- **Filas, de arriba hacia abajo:**
  1. Canales y puntos de contacto: POS, portales, aplicaciones, mesón, comercio electrónico y marketplace.
  2. Servicios Retail (R-01 a R-09).
  3. La frontera X-01, como banda vertical que separa la zona Retail de la zona Emisor.
  4. Servicios del Emisor (F-01 a F-03).
  5. Plataforma común (1.14a a 1.14d).
  6. Sistemas conservados (ERP/DTE, WMS, marketplace) y componentes locales (tienda y centro de distribución).
- **Conclusión del texto:** la frontera es una pieza del modelo y no una política. Ningún servicio Retail toca datos del Emisor sin pasar por X-01, y ningún sistema conserva interfaces directas con otro.
- **Partes (RR-12):** como la vista general es grande, se explica en E2a, E2b y E2c, cada una dibujada aparte.

**E2a. Dominio Retail.**
- **Muestra:** los nueve servicios R y sus relaciones de autoridad. Por ejemplo, R-01 alimenta a R-03, R-04, R-05 y R-07; R-03 es la autoridad del disponible que consumen R-04, R-07 y el comercio electrónico; R-05 recibe las ventas del POS; R-06 consume R-04 y R-05; R-08 reintegra a R-03.
- **Fuente:** las "Interacciones" de cada servicio en `Análisis de actores, alcance y arquitectura de servicios.md`, Parte II §2.
- **Conclusión del texto:** hay una sola fuente de verdad por dato (Caso 16.1 n.º 1) y por eso un pedido tiene un único estado.

**E2b. Dominio Emisor y frontera.**
- **Muestra:** F-01, F-02 y F-03, y X-01 como único punto de paso.
  - Solicitantes autorizados: R-09, F-01 y F-02, con un mandato definido para auditoría y cumplimiento.
  - Cruces prohibidos marcados: maestro único de clientes, atributos financieros hacia Marketing, saldos hacia R-09.
  - F-03 como custodio de la evidencia que F-01 y F-02 consultan antes de confirmar.
- **Conclusión del texto:** la frontera se construye antes de cualquier vista unificada (Caso 13.1 y 13.3.7), y la evidencia del crédito no depende del vendedor (Caso cap. 18, n.º 20).

**E2c. Plataforma común y autoridad por dato.**
- **Muestra:** 1.14a como columna vertebral, conectada a todos los servicios y sistemas; 1.14b como tabla de autoridad (dato → servicio autoridad → copias → regla de reconciliación); 1.14c y 1.14d como capas transversales.
- **Ejemplos de 1.14b:** disponible comprometible → R-03; ciclo del pedido → R-04; precio vigente → R-01; documento tributario → ERP/DTE; saldo → F-02; consentimiento → F-03.
- **Conclusión del texto:** si cae una autoridad, el resto sigue con confianza degradada declarada y se reconcilia al volver, sin pérdida. Es el criterio verificable de "sin punto único de falla" del objetivo 3.

### E3. Operación sin conexión de la tienda

- **Muestra:**
  - La tienda, con el POS y el componente local de tienda.
  - En operación normal: el POS consulta precio (R-01) y disponibilidad (R-03) y registra la venta en R-05 a través de la plataforma.
  - Sin enlace, durante 24 h: el componente local mantiene precio, promociones, documentos, existencia local y el caché de crédito con el dato mínimo.
  - Al reconectar: la sincronización, con reconciliación determinista y bitácora (RT-03.12), en 30 min o menos.
  - Lo que no está disponible sin conexión: la apertura de tarjeta, la ampliación de cupo, la repactación y la consulta de saldo (declaración de RT-03.13).
- **Conclusión del texto:** la tienda sigue vendiendo y cobrando (restricción 5), incluidas las 14 tiendas en centros comerciales, y el crédito sin conexión no rompe la frontera.
- **Fuente de detalle:** `fundamentacion_credito_sin_conexion.md`.

### E4. Flujos por promesa (cuatro diagramas cortos)

Uno por promesa: qué componente participa en orden y dónde queda la evidencia. Sirven de puente a 3.4.

| Diagrama | Recorrido | Evidencia |
| :-- | :-- | :-- |
| E4a Existencia | Conteo (app 1.38) o recepción → R-03 calcula el disponible con su margen → comercio electrónico y marketplace publican → reserva en R-03 → R-04 | Exactitud por categoría y nodo; cancelaciones |
| E4b Precio | Comercial define en R-01 → la plataforma propaga a las cajas, al canal digital y a la etiqueta → la tienda confirma el cambio de etiqueta → R-05 registra el precio cobrado | Historial publicado por canal; estado de cada etiqueta |
| E4c Entrega | Pedido en el canal → R-04 elige el nodo por costo total → R-03 reserva → preparación (app 1.37) → transportista o retiro → estado único | Fecha prometida frente a la real; estado único |
| E4d Crédito | Vendedor o mesón → F-01 evalúa en 8 s o menos → F-03 entrega y registra la información precontractual → firma electrónica → aceptación → F-02 administra la cuenta | Versión, instante y contenido aceptado; expediente |

**Conclusión del texto:** cada promesa tiene un recorrido y una evidencia. Ese es el puente hacia 3.4, que cuenta lo mismo desde la operación del negocio.

---

## 3. Contenido de 3.4 Explicación de la Solución

**Mensaje central.** 3.4 cuenta la operación de Ancoa con la solución puesta: cómo trabaja cada área y por qué ahora sí se cumplen las cuatro promesas. Muestra que cada causa raíz del cap. 2 tiene respuesta, que las tensiones entre áreas quedan arbitradas por reglas y no por voluntad, y cómo se gana el apoyo de cada grupo de interés.

**Texto de caída sugerido para 3.4:** "Esta sección explica la solución desde la operación del negocio: cómo cambia el trabajo de cada área, por qué ese cambio resuelve el problema descrito en el Capítulo 2 y cómo se obtendrá el apoyo de quienes deben adoptarlo."

**Subtítulos sugeridos (S):**
- 3.4.1 La operación con la solución;
- 3.4.2 Coherencia con el problema;
- 3.4.3 Tensiones entre áreas y cómo se resuelven;
- 3.4.4 Estrategia de apoyo de los grupos de interés.

### 3.1 La operación con la solución (los tres ciclos del Caso, cap. 4)

Conviene contarla por ciclo, con un párrafo por tema.

**Ciclo del producto.**
- **Surtido y maestro de artículos (Caso 4.1):** R-01 es el maestro único, con auditoría de completitud de atributos.
- **Precio, promoción y etiqueta (4.2):**
  - El precio se define en R-01, se propaga en 5 min o menos a las cajas y al canal digital, y la etiqueta queda con estado.
  - La compañía sabe en todo momento qué puntos de exhibición están desactualizados (Caso cap. 18, n.º 7).
  - Cómo se cambia la etiqueta depende del informe 1.25 (decisión 9 del Caso 16.1).
- **Abastecimiento y reposición (4.3):** R-02 calcula sobre un inventario con confianza conocida, no sobre uno con 12,4 % de error.
- **Inventario (4.4):** R-03 no "corrige" el dato. Diseña una promesa cumplible sobre un dato imperfecto (Caso 16.1 n.º 1), con margen por categoría y nodo, conteo cíclico sin cerrar la tienda y causas de diferencia separadas.

**Ciclo del cliente.**
- **Venta en sala (4.5):** el POS cobra, aplica promociones y emite documentos aunque se caiga el enlace. El vendedor consulta la existencia con su grado de confianza en 2 s o menos, en terminal compartida (app 1.36).
- **Pedido en línea y cumplimiento (4.6):** se publica lo comprometible; la reserva es de R-03 y el estado del pedido, de R-04. Un pedido sin unidad se avisa antes de cobrar (Caso cap. 18, n.º 3 y 26).
- **Retiro y despacho desde tienda (4.7):** R-04 decide por costo total y R-06 reconoce a la tienda que entrega (Caso 9.5).
- **Marketplace (4.8):** R-07 mide a los 310 vendedores con reglas conocidas y la devolución en tienda tiene procedimiento (Caso 9.6).
- **Devolución y garantía (4.9):** R-08 resuelve en el mesón sin derivar al cliente (restricción 7) y reintegra a R-03 con aptitud registrada.
- **Evento de comercio electrónico (4.12):** degradación declarada de antemano, capacidad de suspender la publicación de una categoría y responsables definidos (Caso cap. 18, n.º 25).

**Ciclo del crédito.**
- **Originación (4.10):** F-01 evalúa en 8 s o menos y F-03 muestra y registra la información precontractual antes de la aceptación. El proceso impide omitirla, y por eso la rapidez y el cumplimiento dejan de competir (Caso cap. 18, n.º 28).
- **Cobranza, repactación y consentimiento (4.11):** F-02 no confirma una repactación sin evidencia en F-03. La evidencia se conserva por el plazo del crédito más 6 años, en lugar de los 90 días actuales.

### 3.2 Coherencia con el problema del cap. 2

**Tabla C1, causa raíz y respuesta (5 columnas como máximo):**

| Causa raíz (sd-02) | Qué la produce | Componentes que la atacan | Cómo se verifica |
| :-- | :-- | :-- | :-- |
| Causa C1 Registro impreciso | Inventario y maestro que no reflejan lo físico (12,4 %) | R-03, R-01, R-02, R-08, app 1.38 | Exactitud por categoría; merma por causa |
| Causa C2 Tejido de integración | 14 interfaces punto a punto, lote nocturno, sin mapa | 1.14a, 1.14b, mapa 1.21, R-04, R-01 | Estado único; precio propagado en 5 min o menos |
| Causa C3 Frontera difusa | Separación parcial y no documentada; cruces sin regla | X-01, F-03, R-09, 1.14c, red separada 1.15.22 | 100 % de los cruces registrados |
| Causa C4 Incentivos y capacidad | Comisión que compite con los pasos obligatorios; rotación de 62 %; 640 terminales | R-06, F-01 y F-03 (bloqueo), apps en terminal compartida, 3.7 | Información entregada en el 100 % de las aperturas; atribución del despacho |
| Causa C5 Territorio y calendario | Enlaces sin respaldo, red no segmentada, 126 días de congelamiento | Componente local con 24 h, enlaces y red (1.15.20, 1.15.21), olas en ventanas libres | Corte de enlace de 24 h; pasos a producción fuera de las ventanas |

Fuente: `descripcion_alcance_producto.md` §1 (trazabilidad por validar) y sd-02 2.2.2 y 2.3.7.

**Tabla C2, promesa, servicios y evidencia:** es la T1 de `insumos_3.2.md`. En 3.4 no se repite la tabla: se cita y se cuenta con texto.

### 3.3 Tensiones entre áreas (sd-02 2.4.3) y cómo las arbitra la solución

| Tensión | Áreas | Cómo la resuelve la solución |
| :-- | :-- | :-- |
| Crédito rápido frente a información precontractual completa | Negocio Financiero, Contraloría | F-01 en 8 s o menos con F-03 bloqueando la aceptación sin información: rapidez y cumplimiento dejan de competir |
| Comisión del vendedor frente a pasos obligatorios | Vendedores, Contraloría | El proceso no depende de la voluntad; el tiempo de evaluación baja de 40 s a 3 min hasta 8 s o menos |
| Publicar más existencia frente a registro impreciso | Canales Digitales, Logística | R-03 publica lo comprometible con margen por categoría y nodo, y lo prueba primero en un subconjunto de categorías |
| Cambios de precio varias veces al día frente a etiquetas que se cambian de noche | Comercial, operación de tienda | R-01 propaga y registra el estado de cada etiqueta; la alternativa de sala se elige con el informe 1.25 |
| Despacho desde tienda frente a venta presencial y comisión | Canal digital, jefaturas y vendedores | R-04 decide por costo total y R-06 atribuye la venta a la tienda que entrega |
| Uso comercial de datos financieros frente a regulación | Marketing, Contraloría | X-01 autoriza solo con finalidad y dato mínimo; prohíbe atributos financieros en perfiles comerciales |
| Orden del comité frente a la urgencia de 2029 | Comité, Negocio Financiero | El financiero va en la Etapa 1 con justificación (3.2.2) |

Fuente: sd-02 §2.4.3 (`subdoc2-enProgreso.md`), con los nombres de los entrevistados del Caso cap. 8. En el texto se puede usar el nombre del cargo en vez del nombre de la persona.

### 3.4 Estrategia de apoyo de los grupos de interés (exigida por el Comunicado 10 en 3.4)

Se parte de los grupos y la matriz de influencia e interés del sd-02 2.4.1 y 2.4.2. La estrategia sigue los cuatro cuadrantes clásicos; el rol en el proyecto sale del análisis de actores (Parte I §3.3). Es una propuesta (S).

| Grupo (sd-02) | Influencia / interés | Estrategia | Rol en el proyecto | Mensaje clave |
| :-- | :-- | :-- | :-- | :-- |
| Dirección y control (Directorio, Gerencia General, Contraloría) | Alta / alta | Gestionar de cerca | Resuelve decisiones mayores en el Comité Ejecutivo; Contraloría custodia X-01 y valida los controles | La frontera y la evidencia se construyen primero y se pueden auditar |
| Propiedad (grupo controlador, fondos) | Alta / media | Mantener satisfecha | Recibe el avance por hitos | Plazo de 2029 protegido; cumplimiento regulatorio |
| Negocios y operación (Comercial, Canales Digitales, Logística, Negocio Financiero) | Alta / alta | Gestionar de cerca | Valida reglas y resultados; participa en las compuertas de las olas | Cada área recupera una promesa que hoy no puede cumplir |
| Soporte tecnológico y control operacional (TI, Prevención de Pérdidas) | Alta / alta | Gestionar de cerca | TI habilita la integración, la seguridad y la operación (RC-09); Prevención verifica la merma por causa | Mapa de integraciones; menos interfaces que mantener |
| Operación de tienda (jefaturas, vendedores, cajeros, reposición, bodega) | Media / alta | Involucrar y mantener informada | Participa en el piloto de 3 tiendas, en las pruebas y en la adopción; capacitación compatible con la rotación | Vender sin enlace; no se mide a la tienda por errores de registro |
| Clientes y terceros (clientes, titulares, vendedores de marketplace, proveedores) | Baja-media / alta | Mantener informados | Usan los portales y las apps; plan de comunicación a 620.000 clientes durante la migración (13.3.5) | Estado único del pedido; reglas conocidas; información clara del crédito |
| Organismos externos (autoridad financiera, de consumo, tributaria) | Alta / media-alta | Mantener satisfechos | Reciben evidencia y reportes; plan de remediación hasta 2029 | Evidencia acreditable de precio, consentimiento y cruces |
| Administradores de centros comerciales; repositores externos | Baja / baja | Monitorear | Coordinación de enlaces y accesos sin imponer herramientas (restricción 12) | La tienda vende aunque falle su enlace |

Esta tabla tiene 5 columnas, pero celdas con frases largas: en el cuerpo conviene dejar solo grupo, estrategia y rol, y explicar los mensajes en el texto (RR-16).

**Diagrama sugerido para 3.4 (E5):**
- **Muestra:** la matriz de influencia e interés con la estrategia de cada cuadrante superpuesta y flechas de cómo se espera mover a los grupos clave. Por ejemplo, la operación de tienda pasa de "informar" a "involucrar" gracias al piloto. Se redibuja con los mismos grupos de la figura del sd-02; no se copia esa figura.
- **Conclusión del texto:** la gestión de interesados no se concentra solo en la dirección; quienes adoptan la solución en la tienda participan desde el piloto.

### 3.5 Qué no hacer en 3.4

- No adelantar la tecnología (va en 4.1.1).
- No repetir 3.2: 3.4 explica el funcionamiento y el porqué, no el reparto ni las exclusiones.
- No hacer un análisis de riesgos.
- No usar nombres distintos a los de la sección 1.

---

## 4. Tabla de mapeo con el sd-04 (sugerida por el Comunicado para 4.2)

Columnas mínimas: componente en 3.3, componente en 4.1 y emplazamiento en 4.2 (lo decide el sd-04). Propuesta inicial (S) para que el sd-04 la complete:

| Componente (3.3 y 3.4) | 4.1 Arquitectura lógica | 4.2 Emplazamiento (a decidir en el sd-04) |
| :-- | :-- | :-- |
| R-01 a R-09, F-01 a F-03, X-01 | Mismo nombre; límite de contexto propio | Nube pública (carga principal, art. 16) |
| Plataforma de integración (1.14a) | Mensajería, contratos, puerta de entrada | Nube, con adaptadores locales |
| Catálogo de reglas de acuerdo (1.14b) | Gobierno de datos y reconciliación | Documento y configuración |
| Identidad y gestión de accesos (1.14c) | Seguridad (Zero Trust) | Nube, con presencia local |
| Observabilidad (1.14d) | Operación | Nube |
| Componente local de tienda / del centro de distribución | Borde con autonomía de 24 h | On-premise (gabinete por tienda; centro de distribución principal) |
| POS con operación sin conexión | Canal de tienda | On-premise |
| Sitio o región secundaria | Continuidad | Preferencia del equipo: región de nube pública (sd-04 4.3.2) |

---

## 5. Cifras con su fuente y puntos abiertos

**Cifras que suelen aparecer en 3.3 y 3.4.**
- 9 plataformas, 6 proveedores y 14 interfaces (Caso cap. 5).
- 22 tiendas, de las cuales 14 están en centros comerciales (Caso cap. 2).
- 24 h sin conexión (Transversales RT-03.10).
- 30 min para sincronizar (Caso RT-03.13, fijado para 8 h).
- 8 s, 5 min, 2 s, 400 ms y 25 s (Caso RT-09.01).
- 620.000 clientes con saldo (Caso cap. 2).
- 310 vendedores y 940 proveedores (Caso cap. 7 y cap. A).
- 38 % de la venta con tarjeta propia (Caso 4.10).
- Rotación de 62 % y 640 terminales para 3.820 personas (Caso cap. 2 y restricción 11).
- Evidencia por el plazo del crédito más 6 años, en lugar de los 90 días actuales (Caso RT-05.10 y cap. 7).

La tabla completa de cifras está en `insumos_3.2.md` §4.

**Puntos abiertos (no van como marcadores en el `.tex`).**
- **Algoritmo de reconciliación y tecnología de la plataforma de integración:** son decisión del sd-04. En 3.3 y 3.4 se habla de "reglas de reconciliación" sin nombrar productos.
- **Sincronización en 30 min tras 24 h:** hay que validar si se mantiene ese valor o se declara otro con su cálculo (ver `insumos_3.2.md` §5).
- **Trazabilidad de causa a componente** (tabla C1): es una propuesta y conviene que el equipo la confirme.
- **Estrategia de interesados:** es una propuesta (S); se apoya en la matriz del sd-02 sin repetirla.
- **Nombres de los entrevistados (Caso cap. 8):** decidir si se usan los nombres o los cargos.
- **Nombre del componente local:** "componente local de tienda" frente a "gabinete on-premise". Elegir uno y usarlo igual en el sd-04.
- **Objetivo general del proyecto:** sin definir.
