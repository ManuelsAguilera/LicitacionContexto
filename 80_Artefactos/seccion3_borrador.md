# SECCIÓN 3 — Capítulo 4: Descripción Lógica de la Solución

**Licitación N° TFEP-01/2026 — Caso 09: Cadena Multitienda (Multitiendas Ancoa S.A.)**
**Proponente:** Only Simple Solutions
**Fecha:** Septiembre 2026
**Estado:** Borrador para revisión interna (4.1 y 4.2). La sección 4.3 (Arquitectura) la desarrolla el equipo de arquitectura.

> **Nota de edición:** este borrador se apoya en `productos/seccion3_investigacion.md` y ordena el negocio según `Bases/DivisionNegocios.md` (módulos R1–R7 retail, F1–F3 financiero, C1–C4 compartidas). Las innovaciones marcadas como **INN-X** se desarrollan formalmente en `productos/seccion3_innovaciones.md` (Art. 28–29).

---

## 4 Descripción Lógica de la Solución

### 4.1 Descripción de la solución

Para entender la propuesta hay que empezar por cómo funciona Ancoa hoy.

Ancoa no es una tienda a la que se le agrega una tarjeta. Es **dos negocios bajo un mismo techo y con un mismo cliente**:
- el **retail** (módulos R1–R7): comprar, diseñar surtido, logística, tiendas, canal digital, marketplace, devoluciones y prevención de pérdidas; aporta el 90% de los ingresos;
- y la **filial emisora de crédito** (módulos F1–F3), regulada y fiscalizada, que aporta el 10% pero una proporción mayor del resultado.

Y, entre ambos, hay **cuatro áreas compartidas** (ERP, marketing y fidelización, TI y contraloría) que cruzan la frontera jurídica. La de marketing y fidelización (C2) es la de mayor riesgo, porque cruza el comportamiento de compra del retail con el comportamiento de pago de un negocio fiscalizado **sin regla escrita**.

El problema que el mandante nos pide resolver no es un sistema antiguo. Es un **tejido de nueve plataformas de seis proveedores unidas por catorce interfaces punto a punto**, casi todas por archivo y por lote de noche, y cuyo mapa completo nadie tiene. Sobre ese tejido, Ancoa hace **cuatro promesas cada día**:
1. que el producto existe,
2. que el precio está bien exhibido,
3. que la entrega llega,
4. y que el crédito está correctamente informado.

Hoy esas cuatro promesas descansan sobre registros imprecisos. La cifra que lo resume es el **12,4% de discrepancia en el conteo cíclico**: la tienda cree tener una cosa, y el piso tiene otra. De ahí nacen los 2.840 pedidos cancelados en tres días, el 17% de pedidos que vacían el piso de venta, la evaluación de crédito que tarda hasta tres minutos y se lleva la venta, y los 1.240 casos de repactación de los que no queda evidencia.

**Nuestra solución no reemplaza esos sistemas: los articula.** Proponemos una plataforma lógica única —construida en modelo híbrido, con la carga principal en nube pública y componentes on-premise, según el Art. 16 de las Bases— que le ponga una **capa de verdad y de control** al tejido de plataformas. Esa capa se organiza en **seis módulos funcionales**, uno por dolor central del negocio:

| Módulo funcional | Qué promesa restaura | Dolor del caso que resuelve | Módulo del negocio |
| :--- | :--- | :--- | :--- |
| M1. Inventario y Disponibilidad (ATP) | "El producto existe" | 12,4% de discrepancia; 458.000 SKUs; 2 CD | R2, R4, R7 |
| M2. Precio y Exposición (ESL) | "El precio está bien exhibido" | Precio inconsistente entre canales; 310.000 etiquetas | R1, R3 |
| M3. Cumplimiento de Pedidos (OMS) | "La entrega llega" | 2.840 cancelaciones/3 días; 17% vacían el piso | R3, R4, R5 |
| M4. Negocio Financiero | "El crédito está bien informado" | Evaluación de hasta 3 min; 38% de ventas con tarjeta | F1, F2 |
| M5. Marketplace y Terceros | Estado único para el ecosistema | Vendedor externo a ciegas; devoluciones sin aviso | R5 |
| M6. Datos, Analítica y Gobernanza | Operar con datos y cumplir | Frontera retail–financiero sin definir; sin trazabilidad | C1, C2, C3, C4 |

Una condición transversal domina todo el diseño y es la **línea roja del caso**: Ancoa es al mismo tiempo una tienda y un emisor de crédito fiscalizado, y ninguna solución puede tratarlos como uno solo ni mezclar sus datos. Por eso la plataforma mantiene **dos dominios de datos separados** — el del retail y el del negocio financiero — con gobernanza, acceso y trazabilidad independientes. Eso no impide que ambos se hablen: lo que cruza es lo mínimo necesario, previo consentimiento y por canales auditables. La frontera se define **antes** de construir cualquier vista unificada de cliente, tal como exige la contralora.

---

### 4.2 Módulos de la solución lógica

#### 4.2.1 Módulo 1 — Inventario y Disponibilidad (ATP)

**Objetivo.** Construir la única fuente de verdad de stock, corregida y en tiempo real, sobre el tejido de plataformas heredadas. Es el módulo más importante: sin él ninguna otra promesa se sostiene.

**Cómo lo hace.**
- **Capa de visibilidad unificada:** integra las 9 plataformas por APIs, sin tocar el ERP. Publica, por cada referencia, cuánto hay, dónde (piso, bodega, CD) y en qué estado, en tiempo real.
- **Motor ATP (disponible para vender):** calcula cuánto se puede comprometer por nodo y por categoría, sobre la **contabilidad real corregida** y no sobre el registro nominal, y con el error conocido del inventario incorporado con un margen por categoría y punto (decisión de diseño N° 1 del numeral 16.1).
- **Conteo cíclico respaldado:** cierra la brecha del 12,4% con umbrales de tolerancia por categoría, sin cerrar la tienda (RT-17.01), y atribuye la merma a sus causas (pérdida, daño, recepción, devolución mal reintegrada, error de digitación).
- **Pasillo infinito (endless aisle):** permite vender en tienda todo el catálogo, incluso lo que no está físicamente presente, consultando el stock de la red. (Soporta INN-3.)

**Qué entrega.** ATP por nodo y categoría, visibilidad en tiempo real, conciliación de inventario y catálogo ampliado en piso.

---

#### 4.2.2 Módulo 2 — Precio y Exposición (ESL)

**Objetivo.** Que el precio que un cliente ve en el piso sea el mismo que se cobra en caja y el que se publica en línea, y que se pueda acreditar después.

**Cómo lo hace.**
- **Precio maestro único** (canon de precio, promociones y vigencia) que se publica a los canales.
- **Etiquetas electrónicas de precio (ESL):** despliegue priorizado a categorías de alto tráfico y sensibilidad; elimina el error del cambio manual de etiquetas, que hoy deja el precio desactualizado hasta 24 horas.
- **Sincronización canal a canal:** consistencia precio físico vs. online en tiempo real.
- **Trazabilidad de precio publicado:** queda registro de qué precio se publicó en cada canal en cada instante, para responder a un cliente o a una fiscalización, a favor o en contra (hoy no se puede). (RT-16.21.)

**Qué entrega.** Precio consistente multicanal, cumplimiento de la promesa de precio exhibido y evidencia auditable del precio publicado.

---

#### 4.2.3 Módulo 3 — Cumplimiento de Pedidos (OMS)

**Objetivo.** Que un pedido se cumpla desde el punto correcto, sin degradar la operación de la tienda física y con una sola verdad de estado.

**Cómo lo hace.**
- **Orquestación multicriterio del punto de despacho:** elige entre CD y tiendas ponderando **costo total, disponibilidad real y efecto sobre la sala de venta**, con umbrales de stock de seguridad por tienda. Esto evita el error de hoy, que asigna por distancia y hace que el 17% de los pedidos vacíen el piso. (INN-2.)
- **Retiro en tienda (BOPIS) y despacho desde tienda (SFS):** cumplimiento ágil con preparación en bodega de la tienda y coordinación con caja y canal digital.
- **Devolución en tienda (BORIS):** reembolso ágil y recupero rápido de stock. (INN-5.)
- **Estado único de pedido:** consultable por el cliente, la tienda, el mesón, el CD y el vendedor externo (hoy cada canal ve un estado distinto y el mesón no ve los pedidos en línea).

**Qué entrega.** Promesa de entrega cumplida, selección inteligente del punto de despacho, menos cancelaciones y recupero de stock.

---

#### 4.2.4 Módulo 4 — Negocio Financiero

**Objetivo.** Acelerar la originación de crédito en el punto de venta, a segundos y con plena conformidad regulatoria, respetando la separación de datos del giro fiscalizado.

**Cómo lo hace.**
- **Originación en segundos:** evaluación inmediata que recupera la venta que hoy se pierde en la espera de hasta tres minutos.
- **Scoring alternativo:** complementa el informe tradicional con historial de pago de servicios, comportamiento transaccional y facturación electrónica como proxy de ingresos, ampliando el acceso a clientes sin historial (dimensión de inclusión financiera). (INN-1.)
- **Conformidad regulatoria:** consentimiento informado del cliente para las fuentes de datos; divulgación reforzada de la **Carga Anual Equivalente (CAE)**; trazabilidad de cada decisión de crédito; y evidencia estructurada de la información precontractual entregada y, en su caso, del consentimiento recuperable a diez años (firma electrónica, RT-16.14), para cerrar los 1.240 casos sin evidencia y el plan de remediación con hito en 2029.
- **Dominio de datos financiero separado:** gobernanza, acceso y trazabilidad independientes del retail. Lo que fluye del retail hacia el financiero —para identidad y scoring— **rodea pero no mezcla** los datos: se transfiere lo mínimo, con consentimiento y por canales auditables. (Línea roja; RT-11.10, RT-16.09.)

**Qué entrega.** Crédito aprobado en segundos, menos abandono de venta, inclusión financiera, cumplimiento regulatorio y evidencia recuperable.

---

#### 4.2.5 Módulo 5 — Marketplace y Terceros

**Objetivo.** Integrar a los 310 vendedores externos y al ecosistema de terceros sin que el cliente distinga lo intermediado de lo propio, y con una sola verdad de estado.

**Cómo lo hace.**
- **Integración (no desarrollo) de la plataforma de marketplace:** alta de catálogo, sincronización de stock, gestión de pedidos y conciliación con el OMS.
- **Estado único de pedido y aviso de devolución:** el vendedor externo se entera del estado de sus pedidos y de las devoluciones recibidas en tienda (hoy se entera en la liquidación).
- **Evaluación de vendedores con reglas conocidas:** medición de desempeño con consecuencias claras (RT-16.21).
- **APIs de ecosistema:** conexión con proveedores, transporte de última milla y socios.

**Qué entrega.** Surtido ampliado, ecosistema conectado y un socio externo que operan con la misma visibilidad que el negocio propio.

---

#### 4.2.6 Módulo 6 — Datos, Analítica y Gobernanza

**Objetivo.** Operar con datos y sostener la **frontera entre los dos negocios** con trazabilidad, de forma que la propuesta nunca mezcle lo que no debe mezclarse.

**Cómo lo hace.**
- **Gobernanza de la separación retail–financiero:** define, antes que cualquier vista unificada de cliente, qué puede cruzar entre ambos ámbitos, en qué dirección, con qué base y con qué control técnico que lo impida cuando no corresponda. Cada cruce autorizado queda registrado con su finalidad, base y autorización (RT-16.09). (Línea roja; decisión de diseño N° 4.)
- **Identidad y cliente único, sin vulnerar la frontera:** un identificador que relaciona al cliente de los cuatro canales con el titular de la tarjeta, sin unir ambos dominios de datos (decisión de diseño N° 3).
- **Analítica operacional:** cuadros de mando de inventario, cumplimiento, precio y crédito para el día a día.
- **Analítica de negocio (data retail) separada:** la analítica del retail (para lealtad y servicios a terceros) vive en el dominio retail, anonimizada y agregada, sin mezclarse con el giro financiero. Aquí se apoya la innovación de modelo de negocio (INN-4): una **plataforma de datos comerciales con cruce controlado y auditable**, habilitada por la nube y alineada a la ley y al cumplimiento.

**Qué entrega.** Decisión basada en datos, separación auditable de los dos negocios y una base de datos comercial que se puede aprovechar sin tocar los datos regulados.

---

### 4.3 Arquitectura Lógica

*(Pendiente — la desarrolla el equipo de arquitectura: capas cliente, presentación, borde, negocio, datos y transversal, sobre el modelo híbrido nube + on-premise del Art. 16, y con la separación técnica retail–financiero como requisito de diseño.)*

---

## Resumen de trazabilidad

| Requisito transversal (RT-CC) | Módulo(s) que lo cumplen | Candidato de innovación |
| :--- | :--- | :--- |
| RT-03 — Despliegue híbrido (nube + on-premise) | Transversal (4.3) | INN-3, INN-4 |
| RT-11 / RT-16 — Seguridad de datos, separación retail–financiero, registro de cruces | Módulos 4 y 6 | INN-1, INN-4 |
| Visibilidad/ATP de inventario | Módulo 1 | INN-3 (tecnológica) |
| Precio y exhibición (trazabilidad) | Módulo 2 | — |
| Cumplimiento omnicanal (OMS) | Módulo 3 | INN-2 (proceso), INN-5 (UX/social) |
| Negocio financiero / crédito en segundos | Módulo 4 | INN-1 (producto), INN-5 (social) |
| Marketplace / estado único | Módulo 5 | — |
| Datos, analítica y gobernanza (frontera) | Módulo 6 | INN-4 (modelo de negocio) |
