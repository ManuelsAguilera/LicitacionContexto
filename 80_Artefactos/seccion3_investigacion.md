# Sección 3 — Investigación de apoyo

**Licitación N° TFEP-01/2026 — Caso 09: Cadena Multitienda (Multitiendas Ancoa S.A.)**
**Proponente:** Only Simple Solutions
**Documento:** Investigación de apoyo para el Capítulo 4 (Descripción Lógica de la Solución)
**Fecha:** Septiembre 2026

---

## 1. Objetivo y método

Este documento reúne la investigación que sustenta la **Sección 3 — Descripción Lógica de la Solución (Capítulo 4)**. Sigue el orden que pedimos para entender el caso de verdad: **primero cómo funciona el negocio hoy, después qué le falla y solo al final qué tecnología proponemos** y qué innovaciones se desprenden de esa solución.

Para describir el negocio usamos como columna vertebral el documento `00_Bases/DivisionNegocios.md`, que ordena a Ancoa en módulos: **R1–R7** para el negocio retail (tienda), **F1–F3** para la filial emisora de crédito (negocio financiero, fiscalizada) y **C1–C4** para las áreas que cruzan la frontera entre ambos (ERP, marketing/fidelización, TI y contraloría). Esas siglas se reutilizan a lo largo de la propuesta para que todo sea trazable (arquitectura → EDT → riesgos → flujo de caja), que es lo que la evaluación premia (Cap. 19, "Consolidación").

Cada tema cierra con una "Implicación para la solución", redactada en lenguaje llano y siempre atada a un dolor de un módulo concreto y a un requisito transversal (RT).

---

## 2. Parte A — Cómo funciona el sistema hoy (el punto de partida)

> Antes de proponer tecnología hay que describir con claridad cómo opera Ancoa y cuál es su tejido. Esta parte fija el lenguaje de toda la Sección 3.

### 2.1 Los tres bloques del negocio

- **Negocio retail (R1–R7):** Comercial y Compras (precio/surtido), Logística y Centros de Distribución, Operación de Tiendas, Canales Digitales, Marketplace, Atención al Cliente y Prevención de Pérdidas. Aporta el **90%** de los ingresos consolidados (87% retail propio + 3% comisiones de marketplace) ≈ **$ 426.600 millones** anuales.
- **Negocio financiero (F1–F3):** Originación de Crédito, Cobranza/Repactación/Servicio y Control Interno de la filial emisora. Aporta el **10%** ≈ **$ 47.400 millones**, con una proporción mayor del resultado. Es un **emisor de crédito fiscalizado** (dos negocios, dos regímenes jurídicos, un mismo cliente).
- **Áreas compartidas (C1–C4):** ERP, Marketing y Fidelización, TI y Cumplimiento/Contraloría. **Cruzan la frontera jurídica** y son justamente donde la separación exigida puede vulnerarse. Marketing y Fidelización (C2) es el punto de mayor riesgo: cruza comportamiento de compra (retail) con comportamiento de pago (financiero fiscalizado) sin regla documentada.

### 2.2 Cómo viaja la información hoy (y por qué está roto)

El problema no es un sistema viejo que haya que reemplazar: son **nueve plataformas de seis proveedores unidas por catorce interfaces punto a punto**, casi todas por archivo y lote nocturno, y cuyo mapa completo nadie posee.

| Cómo trabaja hoy | Ejemplo del caso | Módulo afectado |
| :--- | :--- | :--- |
| Reposición calculada sobre inventario del sistema | La propuesta se hace sobre un registro con **12,4% de error** | R2 / R7 |
| Existencia publicada en el canal digital por lote nocturno | Se publica con un descuento fijo de seguridad definido en **2019** | R4 |
| Pedido asignado al punto de despacho por **distancia** | **17% de los pedidos online vacían el piso de venta** | R3 / R4 |
| Mesón que no ve los pedidos del canal online | El cliente llama cinco veces y nadie sabe decirle qué pasó | R6 |
| Evaluación de crédito en línea, entre 40 s y 3 min | El vendedor deja de ofrecer la tarjeta si el proceso se alarga | F1 |
| Repactación consentida por llamada grabada conservada **90 días** | **1.240 casos de 2025 sin evidencia recuperable** | F2 / C4 |
| Concepción operado con planillas | Su inexactitud entra directo al registro nacional de existencia | R2 |
| Marketing cruza datos retail y financieros sin regla | La contralora exige definir la frontera antes de cualquier vista unificada | C2 |

### 2.3 Las decisiones de diseño pendientes (numeral 16.1 del caso)

El caso cierra con veinticinco decisiones que el proponente debe resolver y declarar como supuestos. Las que condicionan la solución lógica son:

1. **Fuente única de verdad de la existencia y cálculo del "disponible para vender"** sobre un registro con error conocido, con margen por categoría y punto (la decisión de arquitectura más importante).
2. **Qué hacer con el sistema central de 2009 y las 14 integraciones**, cuyo mapa hay que levantar como parte del trabajo.
3. **Qué es un cliente único** cuando la misma persona es compradora y deudora, sin vulnerar la frontera.
4. **Qué datos pueden cruzar entre retail y filial**, en qué dirección, con qué base y con qué control técnico (la contralora lo exige antes de construir cualquier vista unificada).
5–25. Las demás (consentimiento de repactación, precio válido, reserva de existencia, punto de despacho, merma, evento anual, migración de la cartera, etc.) se recogen en el registro de supuestos.

### 2.4 Lo que la investigación debe aportar (numeral 16.2)

El caso pide estudiar materias que no explica. La Parte B las cubre: inventario omnicanal, modelos de cumplimiento, maestro de artículos, gestión de precios, ley del consumidor, régimen de emisores de tarjeta, obligaciones de información al consumidor financiero, repactación, cobranza y prevención de lavado, protección de datos, norma de medios de pago, marketplace, prevención de pérdidas, eventos de alta concurrencia y lenguaje claro financiero.

---

## 3. Parte B — La investigación técnica, en orden del sistema

### 3.1 Inventario: la disponibilidad comprometible (ATP) es la base de todo

**Qué investigamos.** Cuál es la base técnica de la omnicanalidad y por qué la precisión de inventario es su condición de posibilidad.

**Qué encontramos.**
- La omnicanalidad ya es el negocio en Chile: Falabella alcanzó ~47% de ventas por e-commerce, Paris ~40,6% y Ripley ~30,5% (Q2 2026). Un canal que ya era accesorio es hoy un negocio de igual peso que la tienda.
- La base técnica del cumplimiento omnicanal es el **inventario unificado a nivel red** (WMS + OMS + visibilidad en tiempo real). Sin ATP creíble, las promesas de retiro en tienda, despacho desde tienda o pasillo infinito se derrumban.

**Qué significa para la solución.**
- El problema de Ancoa no se resuelve reemplazando el ERP: se resuelve construyendo una **capa de visibilidad/inventario unificado** que teja las 9 plataformas. Esto confirma el enfoque del caso: "no es un sistema legado, es un tejido de plataformas".
- El ATP se modela por nodo (piso, bodega, CD) y por categoría, sobre contabilidad real corregida. Sin esto no hay ninguna de las cuatro promesas diarias. (Módulo 1; RT-03 despliegue híbrido.)

### 3.2 Cumplimiento de pedidos: SFS, BOPIS y no vaciar el piso

**Qué investigamos.** Cómo decidir desde dónde se despacha un pedido sin degradar la operación de la tienda.

**Qué encontramos.**
- El despacho desde tienda (SFS) y el retiro en tienda (BOPIS) son estándar probado y rentables: marcas con OMS moderno aumentan ~25% sus ventas online al enviar desde tiendas y reducen transporte.
- Pero el caso Ancoa introduce una restricción que el retail genérico no enfatiza: **el 17% de los pedidos vacían el piso de venta**, que sigue siendo la mayor parte del negocio. Por eso la regla de selección del punto de despacho no puede ser solo "la tienda más cercana": debe ponderar **costo total, disponibilidad real y efecto sobre la sala**.

**Qué significa para la solución.**
- El módulo de cumplimiento (OMS) implementa orquestación multicriterio (proximidad + margen + capacidad de piso + umbrales de stock de seguridad por tienda), no un simple enrutamiento por distancia. (Módulo 3; INN-2.)
- La devolución en tienda (BORIS) mitiga el síntoma de las 2.840 cancelaciones y recupera stock más rápido. (INN-5.)

### 3.3 Precio y promociones: propagación a 310.000 puntos y trazabilidad

**Qué investigamos.** Cómo se propaga un precio a las cajas, al canal digital y a la sala, y cómo se acredita el precio publicado.

**Qué encontramos.**
- Los cambios de precio en campaña llegan a **400.000** eventos en un solo día, a 380 líneas de caja, al canal digital y a 310.000 puntos de exhibición física.
- Las etiquetas electrónicas de precio (ESL) eliminan el eslabón manual (y erróneo) entre el precio maestro y el exhibido: cuestan US$8–40 por unidad según tecnología y se amortizan contra la mano de obra de reposición y el incumplimiento de la promesa de precio.

**Qué significa para la solución.**
- El módulo de Precio garantiza el "precio exhibido = precio cobrado" y deja **trazabilidad de qué precio se publicó en cada canal en cada instante** (necesario para responderle a un cliente o a un fiscalizador a favor o en contra, hoy imposible). (Módulo 2; conflicto de precio del numeral 16.1; RT-16.21.)

### 3.4 Crédito en el punto de venta: rapidez sin sacrificar cumplimiento (la línea roja)

**Qué investigamos.** Cómo acelerar la evaluación de crédito retail a segundos manteniendo la separación de datos del negocio fiscalizado.

**Qué encontramos.**
- La CMF actualizó en jun-2026 las reglas del crédito digital no bancario: nuevos requisitos de capital por volumen, un sandbox regulatorio de 24 meses, divulgación reforzada de la **Carga Anual Equivalente (CAE)** e interoperabilidad de datos financieros (open finance) con consentimiento, con implementación gradual hasta 2027.
- El **scoring alternativo** es práctica de mercado chileno: complementa el informe tradicional con historial de pago de servicios, comportamiento en billeteras digitales y facturación electrónica como proxy de ingresos, ampliando el acceso a clientes sin historial.
- La separación de datos entre el giro de tienda y el giro crediticio es un principio de las entidades fiscalizadas. La "línea roja" del caso coincide exactamente con ese principio.

**Qué significa para la solución.**
- El módulo financiero habilita la originación en segundos, pero sobre una **plataforma de datos que respete la separación retail–financiero**: tenants de datos, gobernanza, acceso y trazabilidad independientes, y cruce mínimo solo previo consentimiento y con registro auditado. (Módulo 4; INN-1; RT-11.10, RT-16.09.)

### 3.5 Marketplace y ecosistema de terceros

**Qué investigamos.** Cómo integrar a los 310 vendedores externos sin que el cliente distinga lo intermediado de lo propio.

**Qué encontramos.**
- Hoy el vendedor externo opera a ciegas: no conoce el estado de sus pedidos, no se entera de las devoluciones y no sabe con qué regla se le mide.
- La base es el **estado único de pedido** consultable por el cliente, la tienda, el mesón, el CD y el vendedor externo, y la medición de desempeño con reglas conocidas.

**Qué significa para la solución.**
- El módulo de Marketplace **integra, no desarrolla**: única fuente de estado de pedido, notificación de devolución y evaluación de vendedores con reglas conocidas. (Módulo 5; RT-12.12, RT-16.21, RT-17.01.)

### 3.6 Frontera retail–financiero y gobernanza de datos (C2 y el punto de mayor riesgo)

**Qué investigamos.** Cómo implementar técnicamente la separación entre el ámbito del retail y el de la filial emisora, y cómo registrar cada cruce autorizado.

**Qué encontramos.**
- La protección de datos personales (Ley 21.719, en plena vigencia desde el 1 de diciembre de 2026) alcanza el uso del comportamiento de pago con fines comerciales y el perfilamiento: exige registro de tratamiento, derechos del titular, notificación de brechas y control técnico del cruce de datos.
- Altos estándares de seguridad de datos son exigibles para la cartera y el comportamiento de pago (cifrado a nivel de campo, tokenización de medios de pago).

**Qué significa para la solución.**
- La arquitectura define, **antes de cualquier vista unificada de cliente**, qué puede cruzar entre retail y filial, en qué dirección, con qué base y con qué control técnico que lo impida cuando no corresponda. La contralora lo exige textualmente. (Módulo 6 / dominios de datos; RT-11.10, RT-16.09, RT-12.11_segregación financiera.)

### 3.7 Evento anual y capacidad: degradación controlada

**Qué investigamos.** Cómo soportar el evento anual de e-commerce (equivale a 22 días de venta en línea en 3 días) y qué se degrada cuando la capacidad no alcanza.

**Qué encontramos.**
- La fecha la fija la asociación gremial con unas seis semanas de aviso; el plan debe absorberla sin desplazar hitos contractuales.
- El diseño debe definir de antemano el **orden de degradación** y quién puede suspender la publicación de una categoría, en vez de improvisar durante el evento, que es lo que ocurrió.

**Qué significa para la solución.**
- El diseño prevé capacidad (nube elástica, híbrido on-premise) y una estrategia de degradación declarada, con holgura calculada para la fecha del evento. (Transversal; RT-03 nube elástica; numeral 13.2 y 16.1.)

---

## 4. Síntesis: de la investigación a la solución (tres tesis de diseño)

1. **El inventario creíble en tiempo real es la piedra angular.** La omnicanalidad que el mercado ya exige solo es posible con una capa de inventario unificado sobre el tejido de plataformas heredadas. Corregir el 12,4% de discrepancia es la condición de las cuatro promesas diarias.
2. **El cumplimiento y la tarjeta son multifactoriales y regulados.** El OMS debe orquestar por costo total y sin vaciar el piso; el crédito debe operar en segundos dentro del marco regulatorio y con separación de datos retail–financiero.
3. **La data del retail es un activo monetizable solo si se mantiene separada de la del giro fiscalizado.** El modelo de negocio de la propuesta no es un "retail media" libre sobre datos regulados, sino una plataforma de datos con cruce controlado y auditable, alineada a la nube, a la ley y a la línea roja.

---

## 5. Candidatos de innovación (uno por tipo obligatorio, Art. 28)

Estas se desarrollan a fondo en `80_Artefactos/seccion3_innovaciones.md`. Se derivan de la solución tecnológica (no de la moda): resuelven un dolor concreto de un módulo del negocio.

| Tipo (Art. 28) | Innovación | Dolor del caso que resuelve | Módulo |
| :--- | :--- | :--- | :--- |
| 1. Producto/Servicio | Crédito en segundos con scoring alternativo y open finance consentido | Evaluación de hasta 3 min pierde la venta; crédito = 38% de ventas | M4 (financiero) |
| 2. Proceso | SFS + BOPIS con orquestación que no vacíe el piso | 17% de pedidos vacían el piso; 2.840 cancelaciones/3 días | M3 (OMS) |
| 3. Tecnológica/Arquitectura | Capa de inventario unificado en tiempo real + ESL + endless aisle | 12,4% de discrepancia; 458.000 SKUs; 4 promesas imprecisas | M1, M2, M6 |
| 4. Modelo de Negocio | Plataforma de datos con cruce retail–financiero controlado y auditable, habilitada por la nube y el cumplimiento | Data del retail sin aprovechar; frontera regulada que definida habilita servicios | M6 / C2 |
| 5. UX/Sostenibilidad/Impacto Social | BORIS + experiencia omnicanal fluida + inclusión financiera | Devoluciones/cancelaciones y fricción físico-digital | M3, M4 |

> **Nota de trazabilidad:** las innovaciones 1 y 4 dependen de la **separación de datos retail–financiero** (línea roja). Se diseñan sobre dominios/tenants de datos independientes, con gobernanza, acceso y trazabilidad separados. Cada ficha (Art. 29) detalla los 7 elementos.

---

## 6. Fuentes primarias (APA)

1. Supermercado al Día — "E-commerce se acerca al 50% de ventas en grandes tiendas por departamento" (ago-2026).
2. Perú Retail — "Falabella, Cencosud y Ripley: ventas online de sus multitiendas se acercan al 50%" (sep-2026).
3. ADERS-Perú — "Chilean Retail in 2026: A Landscape of Divergent Fortunes and Structural Transformation" (jun-2026).
4. IBM — "¿Qué es BOPIS (comprar en línea, recoger en tienda) en el comercio minorista?" (nov-2025).
5. Solution Logistics — "Logística omnicanal en retail: integra tu inventario online y en tienda" (oct-2025).
6. Mecalux — "Ship from store: convierte tu tienda en un pequeño centro de distribución" (nov-2023).
7. OneStock — "Estrategias de Ship from Store y recogida en tienda en omnicanal" (mar-2026).
8. CréditoLab — "CMF actualiza reglas para crédito fintech en Chile (jun-2026)".
9. CréditoLab — "Fintechs chilenas adoptan scoring alternativo (jun-2026)".
10. CMF Chile — Portal institucional. https://www.cmfchile.cl
11. Asociación Retail Financiero. https://retailfinanciero.org
12. REM Media & Consulting — "Retail Media Networks Chile 2026" (mar-2026).
13. Grupo Falabella — "Plan de inversiones 2026 (US$900M)" (ene-2026).
14. Emol — "Ripley potencia su estrategia de Retail Media" (sep-2025).
15. ResearchAndMarkets — "Chile B2C E-commerce Market Databook Q4 2025" (jul-2026).
