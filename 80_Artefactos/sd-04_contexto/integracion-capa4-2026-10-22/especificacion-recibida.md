# Especificación de los servicios de la capa 4

Documento de contexto, no es entregable. Fecha: 2026-10-22. Estado: borrador para discutir con el equipo. Describe y especifica cada servicio de la capa 4 (servicios de negocio), evalúa si hacen falta servicios nuevos para cumplir las Bases Transversales, y evalúa los cuatro atributos transversales (auditoría, control de acceso, exportación y parámetros) sobre cada servicio. No edita ni reemplaza `02_Propuesta/`: lista en la sección 6 lo que cambiaría. Manda sobre este documento el texto vigente de `sd-03.tex`, `sd-04.tex` y `sd-05.tex`, y la nomenclatura de `80_Artefactos/sd-03_contexto/divisiones_negocio_servicios_sd-03.md`.

## 0. Cómo leer este documento

**Fuentes.** Cada dato lleva su fuente entre paréntesis. Las siglas son: SD-03, SD-04 y SD-05 para los subdocumentos; T-12 para el Formulario T-12 (matriz de cumplimiento técnico); Anexo B para el catálogo de requerimientos (`04_Adjuntos/tablas/sd-03_s2_anexo-b_catalogo-requerimientos.md`); Bases para `00_Bases/Bases_Transversales.md`; Caso para `00_Bases/Caso_09_Cadena_Multitienda.md`.

**Estados.** «Sí» significa que el cumplimiento está declarado y tiene evidencia en un documento vigente. «Parcial» significa que está declarado, pero la evidencia cubre solo una parte. «No» significa que está declarado como pendiente o que no hay evidencia. «Por verificar» significa que falta una confirmación externa. «Sin evidencia» significa que no se encontró el dato en los documentos revisados.

**Códigos RT.** Los códigos RT sin prefijo son los de las Bases Transversales. El Caso (capítulo 15) usa otra numeración para algunos requisitos del capítulo 16: el RT-16.14 del Caso (firma electrónica) corresponde al RT-16.17 de las Bases, el RT-16.21 del Caso (canales de notificación) al RT-16.20 de las Bases, y el RT-16.30 del Caso (portal público) al RT-16.31 de las Bases. Este documento escribe «del Caso» cuando cita un valor de ese capítulo.

**Asignación de RNF.** El catálogo no liga la mayoría de los requerimientos no funcionales a un servicio (solo algunas notas dicen «Mide el servicio de…»). Las asignaciones de RNF a servicios de este documento son una propuesta y se marcan como tal.

## 1. Marco: frentes, áreas y servicios

La descomposición sigue la secuencia frente, área y servicio (SD-03, 3.3.2). Un **frente** reúne lo que responde a un mismo régimen jurídico y de datos. Un **área** es la división del negocio a la que pertenece el servicio. Un **servicio** es la responsabilidad de negocio dueña exclusiva de un conjunto de datos, que los expone solo mediante contratos. La **base tecnológica** (integración, identidad y gestión de accesos, observabilidad) conecta los servicios y no es un servicio de negocio. El esquema de Miro del equipo coincide con esta jerarquía y agrega un servicio candidato, F:C-04.

```
Multitiendas Ancoa S.A.
├── Frente Retail
│   ├── Área Mercadería ........ R:M-01 oferta comercial · R:M-02 abastecimiento · R:M-03 existencias
│   ├── Área Venta ............. R:V-01 pedidos · R:V-02 ventas · R:V-03 comisiones · R:V-04 marketplace
│   └── Área Relación con el cliente ... R:CL-01 posventa · R:CL-02 clientes Retail
├── Frente Frontera ............ X-01 control de cruces (sin área)
└── Frente Filial emisora
    └── Área Crédito ........... F:C-01 originación · F:C-02 cartera · F:C-03 evidencia financiera · F:C-04 control regulatorio (candidato)
Base tecnológica: integración, identidad y gestión de accesos (incluye repositores externos), observabilidad
```

### 1.1 Tabla maestra

Fuentes de la tabla: nomenclatura y etapa (ficha de alcance del SD-03), requerimientos funcionales (Anexo B, B.1), despliegue candidato (SD-04, Tabla 4.3) y registro principal (SD-04, Tabla 4.2).

| Código | Servicio | Frente · área | Etapa | RF | Despliegue candidato | Registro principal |
| :-- | :-- | :-- | :-: | --: | :-- | :-- |
| R:M-01 | Servicio de oferta comercial | Retail · Mercadería | 1 | 20 | Por decidir (uno o dos microservicios) | Artículos, precios, promociones, vigencias y publicación |
| R:M-02 | Servicio de abastecimiento | Retail · Mercadería | 2 | 3 | Microservicio | Órdenes, transferencias y recepción coordinada |
| R:M-03 | Servicio de existencias | Retail · Mercadería | 1 | 48 | Microservicio | Movimientos conciliados, conteos, reservas y disponible comprometible |
| R:V-01 | Servicio de pedidos | Retail · Venta | 2 | 31 | Microservicio | Estado único, promesa, asignación y seguimiento |
| R:V-02 | Servicio de ventas | Retail · Venta | 1 | 14 | Microservicio | Venta, pago, reversa y conciliación de caja |
| R:V-03 | Servicio de comisiones | Retail · Venta | 2 | 3 | Módulo (extraíble) | Regla y base de atribución |
| R:V-04 | Servicio de marketplace | Retail · Venta | 2 | 25 | Módulo (extraíble) | Reglas de vendedores y coordinación |
| R:CL-01 | Servicio de posventa | Retail · Relación con el cliente | 2 | 12 | Microservicio | Caso y destino de devolución |
| R:CL-02 | Servicio de clientes Retail | Retail · Relación con el cliente | 2 | 5 | Microservicio | Identificación, preferencias y gobierno de datos de fidelización |
| F:C-01 | Servicio de originación de crédito | Filial emisora · Crédito | 1 | 14 | Microservicio | Solicitud, evaluación, cupo y autorización |
| F:C-02 | Servicio de cartera de crédito | Filial emisora · Crédito | 1 y 2 | 6 | Microservicio | Cuenta, saldo, pago, mora, cobranza y repactación |
| F:C-03 | Servicio de evidencia financiera | Filial emisora · Crédito | 1 | 15 | Microservicio | Versiones precontractuales, aceptación, firma y expediente |
| X-01 | Servicio de control de cruces | Frontera · sin área | 1 | 12 | Microservicio | Fichas, políticas, decisiones y bitácora del intercambio |
| F:C-04 | Servicio de control regulatorio (candidato) | Filial emisora · Crédito | por decidir | 0 | Por evaluar (sección 5.7) | Por definir |
| — | Base tecnológica | Transversal | 1 | 19 | No aplica | No es un servicio de negocio |

La suma de requerimientos funcionales de los trece servicios y la base tecnológica es 227 (Anexo B, B.1). F:C-04 no tiene requerimientos en el catálogo vigente.

**Observación de nombres.** El diagrama lógico de la capa 4 usa «Evidencia y consentimiento» para F:C-03. El nombre vigente es «Servicio de evidencia financiera» (nomenclatura del SD-03). Conviene alinear el diagrama.

## 2. Estándar de ficha

Cada servicio se describe con los mismos campos.

| Campo | Contenido |
| :-- | :-- |
| Definición | Qué es el servicio, en una frase, con la fuente |
| Ubicación | Frente, área, etapa y despliegue candidato |
| Autoridad del dato | Qué registra y corrige solo este servicio |
| Qué no hace | Límites y quién lo hace |
| Capacidades | Funciones agrupadas, con los RF que las sostienen |
| Requisitos asociados | RNF (propuesta de asignación) y RT de las Bases y del Caso |
| Interfaces | Qué consume y qué entrega (SD-03, 3.3.2; SD-04) |
| Operación sin enlace | Solo si aplica |
| Atributos transversales | Estado de auditoría, acceso, exportación y parámetros: detalle en la sección 4 |
| Por verificar | Vacíos, riesgos y supuestos |

## 3. Fichas de los servicios

### 3.1 Frente Retail · Área Mercadería

#### R:M-01 · Servicio de oferta comercial

- **Definición.** Administra artículos, atributos, precios, promociones, vigencias y el historial de publicación por canal y de actualización de etiquetas (SD-03, 3.3.2). Incorpora la función de precios y promociones que hoy no existe como sistema.
- **Ubicación.** Retail · Mercadería · Etapa 1 · despliegue por decidir entre uno o dos microservicios, por reglas y carga de cambios distintas (SD-04, Tabla 4.3).
- **Autoridad del dato.** Catálogo de artículos, precio vigente y publicado, promociones y su vigencia. Es el dueño único de la entidad Catálogo (T-12, RT-05.09).
- **Qué no hace.** No reserva existencias ni registra ventas (SD-04, Tabla 4.2).
- **Capacidades (20 RF).**
  - Propagación del cambio de precio a las 380 líneas de caja, al canal digital y a los puntos de exhibición (RF-016, RF-017, RF-018) y agrupación de cambios en ventanas parametrizadas fuera del horario de atención (RF-030).
  - Registro de la etiqueta cambiada y de su ejecutor (RF-019, RF-020), indicador diario de exhibiciones desactualizadas (RF-029) y bloqueo de la venta al precio nuevo mientras la exhibición no se actualiza (RF-028).
  - Precio vigente según el último propagado y cobro del menor de los dos precios (RF-022, RF-023); registro de incidente de discrepancia (RF-024).
  - Recuperación del precio publicado de una referencia en una fecha, hora y canal arbitrarios (RF-021).
  - Vigencia, canal y tienda de cada promoción (RF-032, RF-033, RF-034).
  - Completitud de atributos para publicar (RF-142, RF-143) y reportes de incompletos y de publicaciones fallidas (RF-147, RF-148).
  - Consulta pública del precio vigente (RF-064).
- **Requisitos asociados.** RNF-19 (propagación en un máximo de 5 minutos), RNF-44 (trazabilidad del precio por 3 años), RNF-58 (recuperación del precio en un máximo de 1 minuto), RNF-52 (estándar de catálogo e identificación de producto). Caso: RT-05.29 (precio en cajas y canal digital en un máximo de 5 minutos) y RT-05.10 (trazabilidad de precio por 3 años). Las etiquetas electrónicas quedan fuera (EXC-02).
- **Interfaces.** Entrega la oferta vigente a los canales, a existencias, a pedidos, a ventas y a marketplace (SD-03, 3.3.2). Alimenta las innovaciones de búsqueda vectorial multimodal y de Retail Media Network, que dependen del catálogo (SD-13).
- **Operación sin enlace.** Las condiciones vigentes se conservan en el nodo local de la tienda (SD-03, 3.3.2); la ventana de 24 horas rige para venta y consulta (RT-03.10).
- **Por verificar.** Si se separa en dos microservicios (SD-04, Tabla 4.3). RF-025, RF-026 y RF-027 se eliminaron del catálogo por presuponer etiquetas electrónicas (Anexo B, B.2).

#### R:M-02 · Servicio de abastecimiento

- **Definición.** Administra órdenes, transferencias, propuestas de reposición y recepciones para coordinar proveedores, tiendas y centros de distribución (SD-03, 3.3.2).
- **Ubicación.** Retail · Mercadería · Etapa 2 · microservicio, por tener autoridad propia (SD-04, Tabla 4.3).
- **Autoridad del dato.** Órdenes, transferencias y recepción coordinada.
- **Qué no hace.** La ejecución física de ubicaciones, preparación y despacho sigue en el WMS (sistema de almacenes del centro de distribución principal). Las planillas de Concepción no pasan a ser autoridad permanente (SD-03, 3.3.2).
- **Capacidades (3 RF).** Propuesta diaria de reposición con el disponible vigente (RF-144), ajuste por el planificador de logística (RF-145) y registro del ajuste con usuario, valor propuesto y valor confirmado (RF-146).
- **Requisitos asociados.** RNF-53 (estándar de intercambio de órdenes y avisos con los 940 proveedores), RNF-40 (mecanismo de integridad en la conformidad de recepción de mercadería). Caso: la conformidad de recepción exige firma electrónica (RT-16.14 del Caso).
- **Interfaces.** Consulta el disponible de existencias; se integra con ERP/DTE y con el WMS (SD-03, 3.3.2).
- **Por verificar.** El catálogo tiene solo 3 RF para este servicio (Anexo B, B.1 lo declara como vacío de completitud). No hay un servicio ni una capacidad definida para la firma de la conformidad de recepción en Retail (la firma electrónica del T-12 está asignada a F:C-03). Ver sección 5.3.

#### R:M-03 · Servicio de existencias

- **Definición.** Consolida existencias y movimientos por nodo, administra reservas y calcula el disponible comprometible con un margen de confianza por categoría y punto. Registra conteos, ajustes y causas de diferencia (SD-03, 3.3.2). Es la fuente única de la existencia (Caso 16.1, decisión 1).
- **Ubicación.** Retail · Mercadería · Etapa 1 · microservicio, por ser transaccional para preservar la promesa de existencias (SD-04, Tabla 4.3).
- **Autoridad del dato.** Movimientos conciliados, conteos, reservas y disponible comprometible.
- **Qué no hace.** El WMS conserva la autoridad de ejecución física y el ERP/DTE el asiento contable (SD-04, Tabla 4.2).
- **Capacidades (48 RF).**
  - Reservas temporales con vigencia parametrizable y liberación (RF-035 a RF-042, RF-044) e impedimento de doble compromiso de una unidad (RF-038).
  - Cálculo del disponible: existencia registrada menos reservas y colchón de confianza por categoría y punto (RF-127 a RF-130, RF-149 a RF-152), con traza del cálculo (RF-130).
  - Consulta pública y de sala (RF-065, RF-066, RF-087, RF-101) con porcentaje de error probable (RF-158 a RF-161).
  - Conteo cíclico: frecuencia, método y gatillo parametrizables por categoría, programación y resultado (RF-131 a RF-137).
  - Mermas: clasificación obligatoria de la diferencia, cuantificación e informe mensual (RF-138 a RF-141).
  - Probadores: ingreso, reingreso y venta de unidades en probador (RF-153 a RF-156).
  - Control de publicación: ningún canal consume el saldo bruto (RF-157), alerta al rol facultado cuando la exactitud cae (RF-162), suspensión manual (RF-163), sin suspensión automática de una categoría que no tenga regla de degradación declarada y aprobada (RF-164) y suspensión por orden de degradación (RF-179, RF-182, RF-183).
  - Resolución determinista de la existencia comprometida tras una desconexión (RF-098).
- **Requisitos asociados.** RNF-03 (el conteo no degrada la venta), RNF-16 (consulta en ficha en un máximo de 400 ms), RNF-21 (consulta en terminal de sala en un máximo de 2 s), RNF-45 (movimientos y conteos por 6 años). Caso: RT-05.29 (disponibilidad publicada en un máximo de 30 s tras una venta), RT-09.01.
- **Interfaces.** Recibe movimientos del WMS, del punto de venta, de abastecimiento y de posventa; comunica disponibilidad a pedidos, marketplace y los canales (SD-03, 3.3.2). Alberga la innovación de conteo cíclico predictivo y una ayuda de clasificación de causas que la persona confirma antes de cerrar el ajuste (SD-03, 3.3.2; SD-13).
- **Operación sin enlace.** Consulta de la existencia local en modo desconectado (RF-087).
- **Por verificar.** Tamaño del colchón por categoría (decisión de supuesto); el catálogo concentra 48 de 227 RF en este servicio, lo que sugiere evaluar si se divide internamente (reservas y conteos).

### 3.2 Frente Retail · Área Venta

#### R:V-01 · Servicio de pedidos

- **Definición.** Administra el ciclo y el estado único del pedido, la fecha prometida y el nodo de preparación elegido por costo total de servir (SD-03, 3.3.2).
- **Ubicación.** Retail · Venta · Etapa 2 · microservicio (SD-04, Tabla 4.3).
- **Autoridad del dato.** Estado, promesa, asignación y seguimiento del pedido.
- **Qué no hace.** No reemplaza la ejecución física del WMS (SD-04, Tabla 4.2).
- **Capacidades (31 RF).**
  - Preautorización del pago al aceptar el pedido y captura solo con la confirmación de preparación (RF-043, RF-045), aceptación explícita del cliente antes de capturar el cobro (RF-047), anulación (RF-048), cancelación con motivo (RF-049) y conciliación diaria de preautorizaciones vencidas (RF-050).
  - Alternativa de resolución determinada automáticamente por el motor de reglas: cancelar, sustituir, derivar a tercero o entrega diferida (RF-046).
  - Estado único de consulta para todos los actores (RF-052, RF-067, RF-068, RF-072 a RF-074) y notificación del cambio de estado antes de cualquier cobro (RF-051).
  - Costo total de servir y selección del punto de despacho (RF-076 a RF-078), exclusión de Concepción como origen de promesa (RF-075) y exclusión del stock de exhibición no elegible (RF-053).
  - Fecha prometida calculada, sin plazos fijos de catálogo (RF-079, RF-080), y cumplimiento de la promesa por pedido (RF-081).
  - Reasignación acotada (RF-056 a RF-058), alternativas al cliente (RF-059 a RF-061), monitoreo del tiempo restante y priorización (RF-062, RF-063) y límite de unidades por cliente (RF-180).
- **Requisitos asociados.** RNF-04, RNF-05 (consistencia y desfase del estado entre canales), RNF-17 (confirmación en un máximo de 3 s en el evento anual), RNF-54 (estándar con transportistas), RNF-64 (aviso de quiebre en un máximo de 30 minutos), RNF-65 (sin cobro sostenido sobre pedido no cumplible).
- **Interfaces.** Solicita reservas a existencias; coordina canales, tiendas, centros de distribución y transportistas; comparte estado con comisiones, marketplace y posventa (SD-03, 3.3.2). Aloja el adaptador de la innovación de lockers (SD-13).
- **Por verificar.** Criterio de selección cuando el costo total de servir empata; plazo de validación de la innovación de lockers en la marcha blanca de la Etapa 2.

#### R:V-02 · Servicio de ventas

- **Definición.** Registra ventas, pagos, reversas y registros de caja del punto de venta y del canal digital, incluidas las operaciones realizadas sin enlace que se sincronizan después. Concilia esos hechos (SD-03, 3.3.2).
- **Ubicación.** Retail · Venta · Etapa 1 · microservicio (SD-04, Tabla 4.3).
- **Autoridad del dato.** Venta, pago, reversa y conciliación de caja.
- **Qué no hace.** El ERP/DTE es el único emisor tributario (SD-04, Tabla 4.2).
- **Capacidades (14 RF).** Conmutación a modo desconectado y de vuelta (RF-082, RF-088), registro y cobro sin enlace (RF-083, RF-084), promociones y folios de contingencia sin enlace (RF-085, RF-086), marca de la operación desconectada (RF-094), conciliación idempotente de ventas y documentos (RF-095 a RF-097), informe de excepciones (RF-099), emisión de documentos por el ERP/DTE (RF-100), venta física con reserva digital activa (RF-001) y desactivación temporal de medios de pago de mayor fricción (RF-181).
- **Requisitos asociados.** RNF-18 (venta completa en un máximo de 25 s), RNF-24 a RNF-28 (24 horas sin enlace, sincronización en un máximo de 30 minutos, sin pérdida ni duplicados), RNF-41 (documentos por 6 años), RNF-34 (medios de pago tokenizados), RNF-56 (formato vigente de documento tributario electrónico).
- **Interfaces.** Entrega la venta confirmada a comisiones y posventa; mantiene el estado del documento con el ERP/DTE (SD-03, 3.3.2). Para la compra con tarjeta propia consulta a originación a través de la frontera (SD-04, 4.1).
- **Operación sin enlace.** Es el servicio con mayor exigencia: venta, cobro y emisión de documentos con el nodo local por 24 horas (RT-03.10 de las Bases prevalece sobre el 8 h del Caso).
- **Por verificar.** Cupo preaprobado para compras con tarjeta propia sin enlace: decisión pendiente de validación con la Filial (SD-03, SP-03).

#### R:V-03 · Servicio de comisiones

- **Definición.** Aplica reglas auditables para atribuir una venta y su base de comisión al canal, vendedor y tienda que corresponden, incluso cuando una tienda abastece un pedido de otro canal (SD-03, 3.3.2).
- **Ubicación.** Retail · Venta · Etapa 2 · módulo, que se extrae a microservicio si las mediciones lo justifican (SD-04, Tabla 4.3).
- **Autoridad del dato.** Regla y base de atribución.
- **Qué no hace.** No administra remuneraciones: el ERP/DTE las conserva.
- **Capacidades (3 RF).** Base de comisión reconociendo al vendedor y a la tienda de origen (RF-054), transmisión condicionada al movimiento real de inventario (RF-055) y base considerando canal de origen y de cumplimiento (RF-071).
- **Requisitos asociados.** No hay RNF específico en el catálogo (sin evidencia).
- **Interfaces.** Consume pedidos y ventas; entrega la base calculada al proceso de remuneraciones del ERP/DTE.
- **Por verificar.** Solo 3 RF, declarado como pendiente de completitud en el Anexo B. Reglas de atribución: no está definido si son parametrizables.

#### R:V-04 · Servicio de marketplace

- **Definición.** Relaciona la plataforma de marketplace de 2022 con la oferta, disponibilidad, pedidos, devoluciones y liquidaciones que gestiona Ancoa, y administra las reglas de habilitación y desempeño de vendedores externos (SD-03, 3.3.2).
- **Ubicación.** Retail · Venta · Etapa 2 · módulo (SD-04, Tabla 4.3).
- **Autoridad del dato.** Reglas de vendedores y coordinación.
- **Qué no hace.** No sustituye la plataforma de marketplace de 2022 ni opera la logística de cada vendedor (SD-03, 3.3.2; EXC-12).
- **Capacidades (25 RF).** Existencia declarada por el vendedor (RF-102, RF-103, RF-104, RF-109), indicadores de nivel de servicio (RF-105), devoluciones y su costo (RF-106, RF-107, RF-108, RF-111), consultas del vendedor (RF-110, RF-112), visibilidad al cliente de vendedor, despachador y condiciones (RF-113 a RF-116), separación entre inventario propio y de terceros (RF-117, RF-118), reglas de evaluación con acuse previo y matriz de escalamiento (RF-119 a RF-123), despublicación por stock vencido (RF-124) y base de comisión de marketplace al ERP/DTE (RF-125, RF-126).
- **Requisitos asociados.** RNF-02 (interfaz de declaración 24x7 con 99,5 %), RNF-55 (estándar de sincronización con vendedores), RNF-66 (notificación de devolución en un máximo de 15 minutos), RNF-67 (sin mercadería sin aviso a su dueño).
- **Interfaces.** Se apoya en oferta comercial, existencias, pedidos y posventa (SD-03, 3.3.2).
- **Por verificar.** La ejecución de sanciones requiere un rol y un flujo con aprobación (RF-122); hoy ningún componente define el motor de ese flujo (ver sección 5.2).

### 3.3 Frente Retail · Área Relación con el cliente

#### R:CL-01 · Servicio de posventa

- **Definición.** Abre y resuelve los casos de cambio, devolución, retracto y garantía, con registro de recepción, inspección y destino de cada unidad (SD-03, 3.3.2). La atención no se supedita a la conciliación posterior con el vendedor o el fabricante.
- **Ubicación.** Retail · Relación con el cliente · Etapa 2 · microservicio, por tener reglas y autoridad propias del caso (SD-04, Tabla 4.3).
- **Autoridad del dato.** Caso y destino de devolución.
- **Qué no hace.** El reintegro al disponible queda sujeto a inspección (SD-04, Tabla 4.2).
- **Capacidades (12 RF).** Garantía legal íntegra en mesón sin derivar (RF-187, RF-188), motivo y aptitud de la devolución (RF-189, RF-191), bloqueo del reingreso al disponible sin inspección (RF-190), las tres opciones de garantía y su registro (RF-192, RF-193, RF-194), plazo de garantía parametrizable por tipo de producto (RF-195) e hitos de resolución y de recuperación contra el tercero independientes (RF-196, RF-197, RF-198).
- **Requisitos asociados.** RNF-69 (sin derivación como condición de atención), RNF-20 (registro de devolución en un máximo de 60 s), RNF-40 (mecanismo de integridad en la constancia de devolución). Caso: la constancia de devolución exige firma electrónica (RT-16.14 del Caso).
- **Interfaces.** Consulta la venta en ventas; informa a existencias cuándo una unidad vuelve al disponible; coordina marketplace y las notas de crédito con el ERP/DTE.
- **Por verificar.** Mismo vacío que en abastecimiento: la firma de la constancia de devolución en Retail no tiene dueño (sección 5.3).

#### R:CL-02 · Servicio de clientes Retail

- **Definición.** Administra identificación y deduplicación de clientes, puntos, segmentos, campañas y preferencias dentro de Retail. Integra el sistema de fidelización de 2017 bajo separación de datos (SD-03, 3.3.2; EXC-15).
- **Ubicación.** Retail · Relación con el cliente · Etapa 2 · microservicio (SD-04, Tabla 4.3).
- **Autoridad del dato.** Identificación, preferencias y gobierno de los datos de puntos, segmentos y campañas.
- **Qué no hace.** No recibe saldo, mora ni comportamiento de pago. Cualquier solicitud de datos de la Filial pasa por X-01.
- **Capacidades (5 RF).** Consolidar duplicados en un registro Retail (RF-227), movimientos de puntos (RF-228), segmentos solo con atributos comerciales (RF-229), campañas (RF-230) y sincronización con la fidelización conservada (RF-231).
- **Requisitos asociados.** RNF-46 (datos de fidelización por la duración de la relación más 2 años), RNF-74, RNF-75 y RNF-76 (finalidad, base de licitud y registro de tratamiento de datos personales).
- **Interfaces.** Sincroniza con el sistema de fidelización de 2017. Alberga la innovación de Modo Tienda con fila virtual de probadores (SD-13).
- **Por verificar.** Los 5 RF (RF-227 a RF-231) son propuesta del v3.1; el Excel oficial sigue en v3.0.

### 3.4 Frente Filial emisora · Área Crédito

#### F:C-01 · Servicio de originación de crédito

- **Definición.** Administra solicitudes, evaluaciones, cupos, decisiones y autorizaciones de crédito iniciadas en los canales habilitados (SD-03, 3.3.2).
- **Ubicación.** Filial emisora · Crédito · Etapa 1 · microservicio, para preservar el cupo y el plazo de respuesta (SD-04, Tabla 4.3).
- **Autoridad del dato.** Solicitud, evaluación, cupo y autorización.
- **Qué no hace.** Confirma la apertura solo cuando el servicio de evidencia financiera acredita la entrega previa (SD-04, Tabla 4.2). No origina tarjetas nuevas ni amplía cupos durante una pérdida de enlace (EXC-16).
- **Capacidades (14 RF).**
  - Crédito sin enlace solo contra cupo preaprobado, con topes de monto y de número de operaciones parametrizados (RF-089, RF-090, RF-091), sin apertura de tarjeta ni ampliación de cupo (RF-092, RF-093).
  - Simulador de costo total del crédito para el cliente no autenticado (RF-218).
  - Tasa Máxima Convencional vigente cargada y bloqueo de operaciones que la superen (RF-219, RF-220).
  - Cupo determinado solo por las variables de la evaluación, sin el monto de la venta en curso ni la solicitud del vendedor (RF-221, RF-222, RF-223), y vendedor sin capacidad de alterar el resultado (RF-224).
  - Ventana de enfriamiento entre evaluaciones del mismo cliente (RF-225) y registro de cada intento con identidad y resultado (RF-226).
- **Requisitos asociados.** RNF-06 (evaluación en el punto de venta en un máximo de 8 s), RNF-07 (originación en mesón en un máximo de 3 minutos), RNF-37 (segregación de funciones entre originación, aprobación, modificación de condiciones y cobranza), RNF-33 (cifrado a nivel de campo), RNF-50 (lenguaje claro en las comunicaciones del crédito). Caso: RT-09.01 (evaluación en un máximo de 8 s), RT-12.11 (segregación de funciones).
- **Interfaces.** Exige información y evidencia a F:C-03 antes de confirmar una apertura; comunica a ventas el resultado necesario para la venta (SD-03, 3.3.2). La compra con tarjeta propia en caja entra por la frontera (X-01).
- **Operación sin enlace.** Solo cupo preaprobado guardado en el nodo local, dentro de los topes que fija la Filial y sujeto a una prueba de factibilidad. El registro local no guarda saldo, mora ni comportamiento de pago, y si los topes no se fijan o la prueba falla, esa compra se declara no disponible (SD-04, 4.1; SD-03, 3.2.3 SP-03 y 3.4.5).
- **Por verificar.** Alcance de la Ley 21.521 (art. 18) y del Anexo Técnico N.° 3 para finanzas abiertas: por verificar con el texto oficial (SD-03; registro de decisiones D-21).

#### F:C-02 · Servicio de cartera de crédito

- **Definición.** Administra cuentas, saldos, cuotas, pagos, mora, cobranza y modificaciones de condiciones (SD-03, 3.3.2).
- **Ubicación.** Filial emisora · Crédito · Etapas 1 y 2 (por tramos) · microservicio, separado por migración y operación (SD-04, Tabla 4.3).
- **Autoridad del dato.** Cuenta, saldo, pago, mora, cobranza y repactación.
- **Qué no hace.** Sus saldos no se publican en clientes Retail ni en perfiles comerciales (SD-03, 3.3.2).
- **Capacidades (6 RF).** Consulta del estado de cuenta y de documentos por el cliente autenticado (RF-069, RF-070), gestión de cobranza con medio, instante y ejecutor (RF-211, RF-212), bloqueo de la cobranza fuera de los límites normativos (RF-213) y reporte de conciliación diaria de saldos durante la migración (RF-216).
- **Requisitos asociados.** RNF-08, RNF-09 y RNF-10 (migración de 620.000 clientes sin pérdida, sin interrumpir el cobro y sin divergencias), RNF-31 (24x7 en pagos, estado de cuenta y bloqueo de tarjetas), RNF-38 (registro de todo acceso a la cartera, al comportamiento de pago y a los antecedentes de evaluación), RNF-42 (retención del crédito más 6 años), RNF-68 (restauración desde archivo frío en un máximo de 24 horas).
- **Interfaces.** Consulta a F:C-03 antes de confirmar una repactación y conserva la trazabilidad de su expediente (SD-03, 3.3.2). Su migración se hace por olas conciliadas.
- **Por verificar.** Solo 6 RF. Anexo B y la ficha de alcance declaran sin cubrir la imputación de pagos (RN-42), el derecho de retracto y los gastos de cobranza.

#### F:C-03 · Servicio de evidencia financiera

- **Definición.** Custodia la versión de la información precontractual entregada, la aceptación, el consentimiento y la evidencia de firma vinculados a cada operación (SD-03, 3.3.2).
- **Ubicación.** Filial emisora · Crédito · Etapa 1 · microservicio, separado por custodia y retención (SD-04, Tabla 4.3).
- **Autoridad del dato.** Versiones precontractuales, aceptación, firma y expediente.
- **Qué no hace.** No decide crédito ni administra saldos.
- **Capacidades (15 RF).** Exigencia de la entrega completa de información precontractual (RF-199, RF-206), registro de versión, instante, medio y contenido o huella (RF-200 a RF-204, RF-205), consentimiento expreso e informado (RF-207), bloqueo de modificaciones sin evidencia (RF-208), reconstrucción del acto (RF-209), restauración desde archivo frío (RF-210), enlaces del expediente de repactación con la cobranza y el consentimiento (RF-214, RF-215) y consulta pública de la información precontractual (RF-217).
- **Requisitos asociados.** RNF-39 (integridad verificable), RNF-43 (retención del crédito más 6 años, recuperable a 10 años), RNF-57 (recuperación en un máximo de 5 minutos), RNF-68. Caso: RT-05.10 (retención) y firma electrónica en apertura, aceptación y repactación (RT-16.14 del Caso). T-12 declara firma electrónica avanzada con un prestador acreditado, sello criptográfico SHA-256 encadenado y custodia WORM (RT-16.16 a RT-16.18).
- **Interfaces.** Originación y cartera lo consultan para impedir una originación o repactación sin evidencia suficiente (SD-03, 3.3.2).
- **Por verificar.** La firma electrónica está declarada solo para este servicio. Los actos de firma de Retail (conformidad de recepción y constancia de devolución) no tienen dueño (sección 5.3).

#### F:C-04 · Servicio de control regulatorio (candidato)

- **Definición propuesta.** Servicio dueño de los registros que el emisor debe producir o conservar ante la autoridad del mercado financiero y en prevención de lavado de activos. Aparece como «nuevo» en el esquema de Miro del equipo. No existe en SD-03, SD-04, SD-05, T-12 ni en el catálogo.
- **Evidencia de la brecha.** El Caso exige a la filial gobierno, control interno y reporte (Caso, cap. 12, marco normativo, régimen de emisores de tarjetas) y obligaciones de conocimiento del cliente, reporte de operaciones y conservación de antecedentes en prevención de lavado de activos (Caso, cap. 12, «Prevención de lavado de activos»), y los formatos de reporte a la autoridad del mercado financiero (Caso, RT-05.23). Ningún RF del catálogo v3.0 menciona reportes a la autoridad ni prevención de lavado.
- **Piezas regulatorias que hoy sí tienen dueño.** La Tasa Máxima Convencional vive en F:C-01 (RF-219, RF-220). Los límites de cobranza, en F:C-02 (RF-213). El lenguaje claro, en RNF-50. La capacitación normativa del personal financiero, en la base tecnológica (RF-007 a RF-009).
- **Evaluación.** Ver sección 5.7. Este documento no la da por decidida.

### 3.5 Frente Frontera

#### X-01 · Servicio de control de cruces

- **Definición.** Define y versiona las condiciones de cada intercambio entre Retail y la Filial: finalidad, fundamento, solicitante, destinatario y datos mínimos. El ámbito que entrega verifica la política antes de liberar información y el receptor limita su uso a la finalidad aprobada. Ambos extremos registran autorizaciones, denegaciones y versión de política (SD-03, 3.3.2).
- **Ubicación.** Frontera · sin área · Etapa 1 · microservicio con almacén propio (SD-04, Tabla 4.3). Es la única ruta entre Retail y la Filial (SD-03, 3.3.2; SD-04, 4.1). En el diagrama lógico se dibuja en medio de los dos frentes (decisión D-17 y D-28 del registro).
- **Autoridad del dato.** Fichas, políticas, decisiones y bitácora del intercambio.
- **Qué no hace.** No crea un maestro único de clientes ni habilita atributos financieros para Marketing; no almacena perfiles unificados (SD-04, Tabla 4.2).
- **Capacidades (12 RF).** Registro de cada cruce con el dato que cruzó (RF-165), bloqueo de cruces sin interfaz autorizada y registro del intento (RF-166, RF-167), inventario de interfaces de cruce mantenido por el oficial de cumplimiento (RF-168), rechazo de interfaces sin finalidad, base de licitud y evaluación de impacto (RF-169, RF-176), exclusión de atributos financieros del motor de campañas (RF-170, RF-171, RF-172) e identificador distinto por ámbito con correspondencia solo durante un cruce autorizado (RF-173, RF-174, RF-175).
- **Requisitos asociados.** RNF-11 a RNF-14 (separación lógica y física implementada, documentada y verificada por auditoría independiente), RNF-74 a RNF-76 (finalidad, licitud y registro de tratamiento). Caso: RT-16.09 exige el registro de todo cruce, indicando dato, finalidad, base y quién autorizó.
- **Interfaces.** Aplica las políticas en ambos extremos. La compra con tarjeta propia en caja es el único enlace previsto entre los dos frentes (SD-04, 4.1).
- **Por verificar.** El SD-04 contiene una contradicción de ubicación de X-01 (línea 304, al costado, frente a la 586 y al SD-03, en medio): el equipo debe unificarla. Retención de la bitácora: regla propia que el Cliente aprueba (SD-04, 4.1).

### 3.6 Base tecnológica (no es un servicio de negocio)

La base tecnológica reúne 19 RF (Anexo B, B.1): identidad en terminales y acceso de personal externo (RF-002 a RF-015) y el mecanismo de degradación y de congelamiento (RF-177, RF-178, RF-184, RF-185, RF-186). Proporciona identidad, contratos, transporte, adaptadores y observabilidad; su papel es habilitar los flujos, no concentrar reglas de negocio (SD-04, 4.1). Es el lugar natural para los componentes comunes que no son dueños de datos de negocio; ver sección 5.

## 4. Los cuatro atributos transversales en cada servicio

Se evalúa si todo servicio debe presentar auditoría, control de acceso, exportación y parámetros, con dos preguntas: (1) ¿es factible con la especificación que ya le dimos al servicio?, y (2) ¿ya se cumplía? Las Bases exigen estas capacidades a «la solución» (capítulo 16 y vecinos), no servicio por servicio. Pedirlas a cada servicio es una decisión de diseño de este equipo (ver 7.1).

### 4.1 Especificación base contra la que se mide la factibilidad

| Elemento | Qué está definido | Fuente |
| :-- | :-- | :-- |
| Servicio | Microservicio Java 25 y Spring Boot 4.x sobre AKS Premium, un clúster por negocio, sin estado | Registro D-26 y D-28; T-12 RT-02.05 (parcial) |
| Datos | Un PostgreSQL por ámbito; cada microservicio con autoridad propia tiene su repositorio dentro de él. Comisiones y marketplace pueden compartir despliegue | SD-04, 4.1 y Tabla 4.3 |
| Entrada | API Management por ámbito: valida identidad y permisos de entrada, cuotas, esquemas, idempotencia y trazas | Capa 3 del diagrama; SD-04 |
| Identidad | Entra ID con tenants separados por negocio y Entra External ID por negocio (por confirmar el tenant de la Filial) | Registro D-40 y D-41 |
| Comunicación | mTLS entre servicios con Istio (disponibilidad por verificar) y Azure Service Bus Premium por ámbito (modifica el ADR-06 del SD-04) | Registro D-33 y capa 7 |
| Auditoría | Cada servicio escribe un registro de auditoría en su ámbito cuando cambia una entidad; solo admite agregar filas | SD-05, 5.2.4 |
| Exportación | Zona de exportación en el Data Lake de cada ámbito, en CSV, JSON y Parquet con su diccionario | SD-05, 5.2.6; T-12 RT-05.06 |
| Observabilidad | OpenTelemetry con identificador de correlación | RT-14.01 |

La base de este análisis incluye decisiones del diagrama lógico que modifican el SD-04 (bus y tenant de la Filial). El equipo debe unificarlas antes de editar los subdocumentos.

### 4.2 Auditoría

**Requisitos.** RT-05.03 (trazabilidad de toda operación de negocio), RT-16.06 a RT-16.10, RNF-15 (toda acción relevante con usuario, acción e instante), RNF-38 (todo acceso a cartera, comportamiento de pago y antecedentes de evaluación), RT-12.09 (ciclo de vida de la identidad). Caso: RT-16.09 exige además el registro de todo cruce entre ámbitos.

**¿Se cumplía antes?** En la escritura, sí: cada servicio escribe un registro con identidad, operación, fecha y hora, dispositivo, valor anterior y posterior y correlación (SD-05, 5.2.4); T-12 declara RT-05.03 y RT-16.06 en «Sí». La inalterabilidad es parcial: T-12 declara RT-16.07 en «Sí», pero su evidencia es la bitácora de X-01; el SD-05 dice que los registros solo admiten agregar filas, sin precisar cómo se impide que el administrador de la base los modifique. El registro de lecturas de datos sensibles financieros y de cruces está cubierto (T-12, RT-16.09). La consulta y exportación de la auditoría por el Cliente no se cumplía: T-12 declara RT-16.08 como «No — pendiente».

**¿Es factible con lo especificado?** Sí. Es un patrón único (librería común o interceptor) que escribe en el repositorio del propio servicio. Restricciones: la inalterabilidad frente al administrador no la garantiza PostgreSQL por sí solo; requiere sellar o exportar el registro a almacenamiento inmutable (por verificar el mecanismo). En el nodo local de tienda debe escribirse y sincronizarse tras la reconexión. En el despliegue compartido de comisiones y marketplace hay que separar los registros por servicio.

| Servicio | ¿Se cumplía antes? | ¿Factible? | Qué agregar |
| :-- | :-- | :-- | :-- |
| R:M-01 | Parcial: historial de precio y publicación (RF-021, RF-020, RNF-44, RNF-58) | Sí | Auditoría de atributos, promociones y publicaciones con valor anterior y posterior |
| R:M-02 | Parcial: solo el ajuste de la propuesta (RF-146) | Sí | RF de auditoría de órdenes, transferencias y recepciones |
| R:M-03 | Parcial: traza del cálculo del disponible y quién definió el colchón (RF-130, RF-151) | Sí | Auditoría de reservas, movimientos y ajustes (retención de 6 años, RNF-45) |
| R:V-01 | Parcial: valores del costo total de servir y motivo de cancelación (RF-078, RF-049) | Sí | Auditoría de cambios de estado, reasignaciones y capturas de cobro |
| R:V-02 | Parcial: marca de operación desconectada e informe de excepciones (RF-094, RF-099) | Sí, con registro local sincronizado | Auditoría de venta, reversa y conciliación, incluida la del nodo local |
| R:V-03 | Sin evidencia específica | Sí | Registrar qué regla de atribución se aplicó a cada venta |
| R:V-04 | Parcial: fecha y hora de la existencia declarada, acuse y trazabilidad de la sanción (RF-104, RF-119, RF-123) | Sí | Auditoría del resto de las acciones del vendedor y del ejecutivo |
| R:CL-01 | Parcial: opción de garantía ofrecida y elegida, hitos (RF-193, RF-194, RF-196, RF-197) | Sí | Auditoría de inspección y destino de la unidad |
| R:CL-02 | Parcial: movimientos de puntos (RF-228) | Sí | Auditoría de consolidación de duplicados y de armado de segmentos |
| F:C-01 | Sí: cada intento de evaluación con identidad y resultado (RF-226); falta el registro de lecturas | Sí | Registro de todo acceso de lectura con finalidad (RNF-38, RT-16.09 del Caso) |
| F:C-02 | Parcial: gestión de cobranza con medio, instante y ejecutor (RF-212); falta el registro de lecturas | Sí | Registro de lecturas y de cambios de saldo (RNF-38) |
| F:C-03 | Sí: versión, instantes, medio y huella (RF-200 a RF-205); custodia WORM con sello encadenado (T-12) | Sí | Nada nuevo; es la referencia de inalterabilidad |
| X-01 | Sí: es su función (RF-165, RF-167); bitácora de solo anexión (T-12, RT-16.07) | Sí | Nada nuevo |
| F:C-04 | No existe | Sí | Incorporarla desde el diseño |

### 4.3 Control de acceso

**Requisitos.** RT-12.05 (control basado en roles, complementado por atributos donde el proceso lo exija, con matriz de segregación de funciones documentada y verificable), RT-11.01 y RNF-73 (Zero Trust: verificación explícita en cada solicitud), RNF-37 (segregación de funciones financieras), RT-16.15 y RT-16.27 (el acceso a documentos y la búsqueda respetan el control de acceso). Caso: RT-12.11 (terminales compartidas, rotación de 62 %, repositores externos).

**¿Se cumplía antes?** Parcial. La identidad centralizada y federada está declarada en «Sí» (T-12, RT-12.01), y el inicio de sesión único y la autenticación multifactor, como parciales (T-12, RT-12.02 y RT-12.03). T-12 declara RT-12.05 en «Sí», pero su evidencia es la matriz de segregación del dominio financiero (SD-03, 3.3.2); no hay matriz de roles y permisos para los servicios de Retail en SD-03, SD-04 ni SD-05 (búsqueda sin resultados). Quedan en «No»: ciclo de vida de la identidad (RT-12.09), FIDO2 (RT-12.04) y cuenta de emergencia (RT-12.13). La base tecnológica cubre la identidad en terminales y el personal externo (RF-002 a RF-015).

**¿Es factible con lo especificado?** Sí. API Management valida el token y el alcance en la entrada y cada servicio aplica sus reglas de rol y atributo con los claims de Entra; X-01 gobierna cualquier cruce entre ámbitos. Dos condiciones. Primero, el control por atributo (por ejemplo, por tienda) necesita que el directorio conozca la tienda de cada persona, lo que depende del maestro de unidades organizacionales (RT-16.01, sección 5.1). Segundo, en la operación sin enlace por 24 horas hay que definir cómo se valida el acceso en el nodo local sin Entra (por verificar).

| Servicio | ¿Se cumplía antes? | ¿Factible? | Qué agregar |
| :-- | :-- | :-- | :-- |
| R:M-01 | Sin matriz. Roles que aparecen en los RF: analista comercial, reponedor, ejecutivo de cumplimiento (RF-019, RF-021, RF-142) | Sí | Matriz de roles; atributo de tienda y canal |
| R:M-02 | Sin matriz. Rol: planificador de logística (RF-145) | Sí | Matriz de roles |
| R:M-03 | Sin matriz. Roles: vendedor de piso, gerente de logística, rol facultado para suspender publicación (RF-101, RF-149, RF-163) | Sí | Matriz; atributo de tienda; sesión nominativa en terminal compartida (RF-005) |
| R:V-01 | Sin matriz. Roles: ejecutivo de mesón, cliente autenticado (RF-072, RF-067) | Sí | Matriz; acceso del cliente solo a sus pedidos |
| R:V-02 | Sin matriz. Rol: cajero (RF-083) | Sí, con validación local sin enlace por verificar | Matriz; acceso por línea de caja; validación en el nodo local |
| R:V-03 | Sin evidencia | Sí | Matriz de roles |
| R:V-04 | Sin matriz. Usuarios externos: vendedor de marketplace con acceso solo a lo propio (RF-110 a RF-112); rol nominado para sanciones (RF-122) | Sí | Matriz; atributo de vendedor; aprobación de sanciones |
| R:CL-01 | Sin matriz. Rol: ejecutivo de mesón (RF-187) | Sí | Matriz de roles |
| R:CL-02 | Sin matriz. Segmentos solo con atributos comerciales (RF-229) | Sí | Matriz; los atributos financieros los impide X-01 (RF-170) |
| F:C-01 | Parcial: segregación del vendedor (RF-224), capacitación normativa vigente (RF-007, RF-008), matriz financiera (T-12, RT-12.05) | Sí | Matriz verificable entre originación y aprobación (RNF-37) |
| F:C-02 | Parcial: segregación entre modificación y cobranza (RNF-37), capacitación (RF-009) | Sí | Matriz verificable |
| F:C-03 | Parcial: acceso controlado y recuperación (SD-03, 3.3.2) | Sí | Roles de consulta y de reconstrucción del acto |
| X-01 | Parcial: el oficial de cumplimiento mantiene el inventario de interfaces (RF-168); cumplimiento aprueba (SD-03, tabla de gobierno) | Sí | Aprobación dual de interfaces nuevas |
| F:C-04 | No existe | Sí | Acceso del oficial de cumplimiento y de la autoridad fiscalizadora (RT-12.12 del Caso) |

### 4.4 Exportación

**Requisitos.** RT-05.06 (exportar toda la información en formatos abiertos, sin costo y sin intervención del adjudicatario), RT-16.28 (listados ordenables, filtrables, paginados y exportables con el filtro aplicado), RT-16.29 (exportaciones grandes de forma asíncrona), RT-16.30 (exportación sensible registrada en la auditoría), RT-05.05 (lo analítico separado de lo transaccional), RT-14.02.

**¿Se cumplía antes?** La exportación completa sí: zona de exportación por ámbito en el Data Lake (SD-05, 5.2.6; T-12 RT-05.06 en «Sí»). La exportación desde listados no: T-12 declara RT-16.28, RT-16.29 y RT-16.30 como «No — pendiente», y RT-16.27 (búsqueda) como «Parcial».

**¿Es factible con lo especificado?** Sí. Lo masivo sale de la zona analítica de cada ámbito sin cargar la base transaccional. Para los listados de las pantallas se necesita un patrón común: API con filtro y paginación, trabajo asíncrono en el bus, aviso al terminar (depende del componente de notificaciones) y registro de la exportación sensible en la auditoría. La separación por ámbito se mantiene: un conjunto de datos de ambos ámbitos solo se arma tras aprobación de X-01 (SD-03, 3.3.2).

| Servicio | ¿Se cumplía antes? | ¿Factible? | Qué agregar |
| :-- | :-- | :-- | :-- |
| R:M-01 | Parcial: reportes periódicos de incompletos y fallidos (RF-147, RF-148) | Sí | Listado exportable de oferta y precios publicados |
| R:M-02 | Sin evidencia | Sí | Exportación de órdenes y propuestas |
| R:M-03 | Parcial: informe mensual de merma y exactitud por categoría (RF-141, RF-137) | Sí | Exportación de movimientos y conteos (6 años) |
| R:V-01 | Parcial: conciliación diaria de preautorizaciones (RF-050) | Sí | Exportación de pedidos con filtro |
| R:V-02 | Parcial: informe de excepciones (RF-099) | Sí | Exportación de ventas y documentos |
| R:V-03 | Sin evidencia | Sí | Exportación de la base de comisión |
| R:V-04 | Parcial: comisión de marketplace al ERP (RF-125) | Sí | Exportación de liquidaciones y desempeño |
| R:CL-01 | Sin evidencia | Sí | Exportación de casos de posventa |
| R:CL-02 | Sin evidencia; los segmentos son sensibles | Sí | Exportación de segmentos con registro (RT-16.30) |
| F:C-01 | Sin evidencia | Sí | Exportación de evaluaciones con registro (RT-16.30) |
| F:C-02 | Parcial: conciliación diaria de saldos (RF-216); posición consolidada antes de las 07:00 (RT-05.29 del Caso) | Sí | Exportación de cartera con registro (RT-16.30) |
| F:C-03 | Parcial: reconstrucción del acto de consentimiento (RF-209) | Sí | Exportación de la evidencia para fiscalización |
| X-01 | Parcial: la bitácora debe ser verificable por auditoría independiente (RNF-13) | Sí | Exportación de la bitácora |
| F:C-04 | No existe | Sí | Formatos de reporte a la autoridad (Caso, RT-05.23) |

### 4.5 Parámetros

**Requisitos.** RT-16.01 (administración sin intervención del adjudicatario), RT-16.02 (reglas parametrizables desde la interfaz, con versiones y registro de cambios), RT-16.03 (cambio con impacto operacional aprobado por un segundo perfil), RT-16.04 (declarar qué es parametrizable), RT-16.05 (ambiente de simulación), RNF-48 y RT-02.12 del Caso (tienda nueva por parametrización).

**¿Se cumplía antes?** Parcial. T-12 declara RT-16.02 y RT-16.04 en «Sí» (catálogo con los RF parametrizables); RT-16.01, RT-16.03 y RT-16.05 en «No — pendiente».

**¿Es factible con lo especificado?** Sí. Cada servicio guarda sus parámetros en tablas versionadas dentro de su repositorio, con la auditoría de la sección 4.2. Lo que falta son tres piezas comunes: la interfaz de administración, el flujo del segundo aprobador y el ambiente de simulación. Además, RNF-48 y RT-16.01 exigen un maestro de tiendas, centros, líneas de caja y unidades organizacionales que hoy no tiene dueño entre los servicios (sección 5.1).

| Servicio | Parámetros que el catálogo ya exige | ¿Se cumplía antes? | Qué agregar |
| :-- | :-- | :-- | :-- |
| R:M-01 | Ventanas de cambio de precio (RF-030) | Parcial | Declarar atributos obligatorios y reglas de promoción como parámetros |
| R:M-02 | Ninguno definido | Sin evidencia | Reglas de reposición parametrizables (por definir) |
| R:M-03 | Vigencia de reserva y reserva reducida (RF-036, RF-042), colchón por categoría y punto (RF-128, RF-129, RF-149, RF-150), frecuencia, método y gatillo del conteo (RF-131 a RF-133), umbral de exactitud (RF-162) | Parcial | Aprobación por segundo perfil del colchón (RT-16.03) |
| R:V-01 | Ventana de reasignación, compensación, umbral de prioridad y límite de unidades (RF-058, RF-060, RF-063, RF-180) | Parcial | Aprobación por segundo perfil |
| R:V-02 | Medios de pago a desactivar (RF-181), folios de contingencia (RF-086) | Parcial | Declarar qué es parametrizable |
| R:V-03 | Reglas de atribución sin declarar | Sin evidencia | Declarar si son parametrizables (RT-16.04) |
| R:V-04 | Reglas de evaluación, matriz de escalamiento y plazo de despublicación (RF-105, RF-121, RF-124) | Parcial | Aprobación por segundo perfil |
| R:CL-01 | Plazo de garantía por tipo de producto (RF-195) | Parcial | Ninguno adicional |
| R:CL-02 | Segmentos y campañas (RF-229, RF-230) sin declarar | Sin evidencia | Declarar qué es parametrizable |
| F:C-01 | Topes de monto y de operaciones sin enlace, Tasa Máxima Convencional, ventana de enfriamiento (RF-090, RF-091, RF-219, RF-225) | Parcial | Aprobación por segundo perfil (impacto financiero) |
| F:C-02 | Límites normativos de cobranza (RF-213) | Parcial | Aprobación por segundo perfil |
| F:C-03 | Versiones del documento precontractual (RF-200); plantillas de comunicación (RNF-50, RT-16.19) | Parcial | Plantillas administrables por el Cliente |
| X-01 | Inventario de interfaces, finalidades y políticas versionadas (RF-168, RF-169) | Sí: es su función | Ninguno adicional |
| F:C-04 | No existe | No | Formatos y plazos regulatorios como parámetros |

### 4.6 Resumen de la evaluación

| Atributo | ¿Factible con la especificación actual? | ¿Se cumplía antes? | Lo que hay que agregar |
| :-- | :-- | :-- | :-- |
| Auditoría | Sí, como patrón común | Sí en la escritura; parcial en inalterabilidad; no en consulta | Mecanismo de inalterabilidad, registro de lecturas sensibles, interfaz de consulta (RT-16.08) y RF por servicio |
| Control de acceso | Sí | Parcial: solo el dominio financiero tiene matriz | Matriz de roles y atributos por servicio; validación local sin enlace |
| Exportación | Sí | Sí en la exportación completa; no en listados | Patrón de exportación asíncrona con registro (RT-16.28 a RT-16.30) |
| Parámetros | Sí | Parcial | Interfaz de administración, aprobación por segundo perfil, simulación y maestro de ubicaciones |

**Hallazgo sobre el T-12.** Las filas pendientes de RT-16 remiten a «Subdoc.3 §3.2.2» y a un «diseño detallado de la Etapa 1 (administración, flujos, documentos y notificaciones)». El texto del SD-03, 3.2.2 (líneas 165 a 230 del `.tex`) no menciona esas capacidades. La referencia no tiene respaldo hoy. Decidir los componentes comunes de la sección 5 es lo que resuelve esos pendientes.

## 5. Evaluación de componentes con vida propia

La pregunta es si el bloque «Servicios comunes» del diagrama y los pendientes del T-12 exigen levantar servicios o componentes nuevos. Se evalúan siete candidatos con los mismos criterios. Las recomendaciones son propuestas para la discusión; la decisión es del equipo.

### 5.0 Criterios

| Criterio | Pregunta | Fuente |
| :-- | :-- | :-- |
| C1. Datos propios | ¿Tiene un conjunto de datos de un tema de negocio que ningún otro servicio posee? (definición de servicio) | SD-03, 3.3.2; nomenclatura |
| C2. Vida propia | ¿Necesita desplegarse, escalar o recuperarse por separado? | RT-02.02; SD-04, 4.1 |
| C3. Separación por negocio | ¿Debe haber una instancia por ámbito, sin datos compartidos? | Línea roja del Caso; RNF-11 |
| C4. Pendientes que cierra | ¿Qué filas del T-12 hoy «No — pendiente» resuelve? | T-12, RT-16 y RT-12 |

**Opciones por candidato.** A, patrón o librería dentro de cada servicio, sin componente nuevo. B, servicio de negocio nuevo con código propio (como F:C-04). C, componente de la base tecnológica, sin ser dueño de datos de negocio. Un servicio de negocio se reserva para lo que tiene datos de negocio exclusivos (C1); lo que tiene vida propia pero no datos de negocio es componente de la base tecnológica.

### 5.1 Administración y parámetros (RT-16.01 a RT-16.05)

- **Qué cubre.** Gestión de personas usuarias, roles, permisos, unidades organizacionales y jerarquías; parámetros con versiones, segundo aprobador y simulación; alta de una tienda nueva por parametrización (RNF-48; RT-02.12 del Caso).
- **C1.** Los usuarios y roles pertenecen a Entra (base tecnológica). Los parámetros pertenecen a cada servicio. Lo que no tiene dueño es el maestro de tiendas, centros de distribución, líneas de caja y unidades organizacionales, que además alimenta el control por atributo (sección 4.3).
- **C2.** Sí: interfaz propia y API.
- **C3.** Sí, una instancia por ámbito. Una consola única con permisos por ámbito mezclaría la administración de ambos negocios.
- **C4.** RT-16.01, RT-16.03 (con el flujo de 5.2) y RT-16.05.
- **Recomendación.** Opción C: consola de administración como componente de la base tecnológica, con cada servicio exponiendo sus parámetros mediante API versionada (opción A para el almacenamiento). El maestro de ubicaciones requiere dueño explícito: ver decisión 7.4.

### 5.2 Flujos de trabajo y bandeja de tareas (RT-16.11 a RT-16.14)

- **Qué cubre.** Estados, responsables, plazos, escalamiento, delegación, bandeja unificada y motor de reglas.
- **Quién lo necesita.** Aprobación por segundo perfil (RT-16.03), repactación de crédito, sanciones a vendedores de marketplace (RF-122), reasignación de pedidos, inspección de devoluciones y ajustes de inventario (RF-139).
- **C1.** Guarda instancias de flujo y tareas, que son estado de proceso (RT-02.05 manda que viva fuera de los servicios), no datos de negocio.
- **C2.** Sí: componente con estado propio y escala distinta.
- **C3.** Sí, una instancia por ámbito, porque las aprobaciones crediticias no pueden verse desde Retail.
- **C4.** RT-16.11, RT-16.12, RT-16.13, RT-16.14 y RT-16.03.
- **Distinción con la capa 5.** La orquestación de procesos largos entre servicios (D-23) vive en la capa 5 y es automática. El flujo humano, con tareas, plazos y delegación, es otra cosa.
- **Recomendación.** Opción C: motor de flujos de trabajo con tareas humanas, componente de la base tecnológica por ámbito. El producto se elige en la arquitectura física (D-25: Camunda, Temporal o Flowable).

### 5.3 Documentos, plantillas y firma (RT-16.15 a RT-16.19)

- **Qué cubre.** Versionado, metadatos, control de acceso, previsualización, cifrado e integridad, firma electrónica con sello de tiempo, y plantillas administrables.
- **Estado actual.** La evidencia financiera, con firma avanzada, custodia WORM y sello encadenado, está en F:C-03 (T-12, RT-16.16 a RT-16.18 en «Sí»). Faltan RT-16.15 y RT-16.19 (en «No»).
- **Brecha.** El Caso exige firma electrónica también en la conformidad de recepción de mercadería y en la constancia de devolución (RT-16.14 del Caso). Esos actos pertenecen a Retail (abastecimiento y posventa) y F:C-03 es un servicio de la Filial: no puede custodiar documentos de Retail sin romper la separación.
- **C1.** Cada documento tiene un dueño de negocio: la evidencia financiera es de F:C-03, la conformidad de recepción de abastecimiento y la constancia de devolución de posventa. Un almacén documental común no es dueño de esos datos.
- **C2.** Sí: almacenamiento cifrado e inmutable, integración con el prestador de firma.
- **C3.** Sí, por ámbito.
- **C4.** RT-16.15, RT-16.19 y la parte de Retail de RT-16.17 y RT-16.18.
- **Recomendación.** Opción C: capacidad de documentos y firma de la base tecnológica, una por ámbito, reutilizando el prestador de firma ya declarado y el patrón WORM de F:C-03. F:C-03 se mantiene como dueño de la evidencia financiera y los servicios de Retail pasan a usar la capacidad. Hay que fijar si la capacidad de la Filial es la propia F:C-03 o una instancia hermana (decisión 7.5).

### 5.4 Notificaciones (RT-16.20 a RT-16.26)

- **Qué cubre.** Tres canales, plantillas administrables y versionadas, preferencias de la persona, envío asíncrono con reintento y registro de entrega, proveedor y costo por canal, baja.
- **Quién lo necesita.** Aviso de cambio de estado del pedido antes del cobro (RF-051), aviso al vendedor de marketplace por una devolución recibida (RF-106; RNF-66), alerta interna de exactitud (RF-162), comunicaciones de cobranza con registro íntegro (RT-16.21 del Caso; RF-213), comunicaciones del crédito con lenguaje claro (RNF-50), y RNF-51 (100 % de las notificaciones definidas, emitidas y registradas).
- **C1.** Registro de envíos, plantillas y preferencias de canal. Si una persona es cliente de ambos negocios, tiene un identificador distinto en cada uno (RF-173), así que sus preferencias son separadas.
- **C2.** Sí: envío asíncrono, reintentos y proveedores externos.
- **C3.** Sí: cobranza y comunicaciones de crédito son del Emisor.
- **C4.** RT-16.20 a RT-16.25, siete filas hoy en «No — pendiente», y RNF-51.
- **Recomendación.** Opción C: servicio de notificaciones de la base tecnológica, una instancia por ámbito. Es el candidato con mayor número de pendientes del T-12 que cierra.

### 5.5 Búsqueda y exportación (RT-16.27 a RT-16.30)

- **Búsqueda.** El catálogo tiene su búsqueda léxica y, con la innovación multimodal, vectorial en el propio PostgreSQL del servicio de oferta comercial (SD-13). RT-16.27 pide búsqueda global con texto completo, tolerancia a errores de escritura y filtros facetados que respeten el acceso de quien busca; T-12 la declara «Parcial» con producto por definir (SD-04, Tabla 4.6).
- **Exportación.** Ver 4.4: patrón común con trabajo asíncrono, apoyado en notificaciones.
- **C1.** El índice de búsqueda es una proyección de datos de otros servicios, no un dato propio.
- **C2.** El índice se escala aparte, pero no es dueño de nada.
- **C3.** Sí, un índice por ámbito alimentado por eventos y con filtro de permisos.
- **C4.** RT-16.27 a RT-16.30.
- **Recomendación.** Búsqueda como capacidad de la capa de datos, por ámbito, no como servicio de negocio. Exportación como patrón (opción A) más un trabajo común que usa el servicio de notificaciones.

### 5.6 Consulta de auditoría (RT-16.08)

- **Qué cubre.** Consulta y exportación de la auditoría por el Cliente, con filtros por persona, período, entidad y tipo de operación, sin acceso a la base de datos.
- **C1.** No tiene datos propios: lee los registros de cada servicio.
- **Recomendación.** Opción C: módulo de la consola de administración (5.1), con lectura sobre el almacén de auditoría de cada ámbito. Cierra RT-16.08.

### 5.7 F:C-04, servicio de control regulatorio

- **Qué cubriría (propuesta).** Los registros regulatorios del emisor: reportes a la autoridad del mercado financiero (formatos, periodicidad y evidencia de envío), y prevención de lavado de activos (conocimiento del cliente, reporte de operaciones, conservación de antecedentes).
- **Evidencia de la brecha.** Caso, cap. 12: el emisor tiene obligaciones de gobierno, control interno y reporte, y de prevención de lavado en la originación y la cartera. Caso, RT-05.23: formatos de reporte a la autoridad. El catálogo v3.0 no tiene RF sobre reportes a la autoridad ni sobre prevención de lavado (búsqueda sin resultados). El Caso advierte que invocar una norma sin explicar el control concreto que la implementa se evalúa como no acreditada (Caso, cap. 12).
- **C1.** Sí: expediente de reportes, registros de conocimiento del cliente y operaciones reportables son datos propios y exclusivos del emisor.
- **C2.** Sí: cambia con la normativa, con calendario propio de formatos y plazos.
- **C3.** Exclusivo de la Filial.
- **C4.** No cierra filas de RT-16, pero cubre obligaciones del Caso que hoy no tienen control concreto.
- **Riesgos.** Amplía el alcance del frente Filial de tres a cuatro servicios; requiere RF nuevos y definir su etapa (las obligaciones de prevención aplican desde la originación en el punto de venta, que está en la Etapa 1). El alcance exacto depende de la normativa aplicable, por verificar con el texto oficial.
- **Recomendación.** Opción B: crearlo como servicio de la Filial, con alcance mínimo a validar con el equipo y con la contraparte financiera. Alternativa menor: absorber las obligaciones en F:C-02 (cartera), lo que mezcla cobranza con cumplimiento y debilita la separación de funciones.

### 5.8 Cuadro resumen

| Candidato | Recomendación | Tipo | Cierra en el T-12 |
| :-- | :-- | :-- | :-- |
| 5.1 Administración y parámetros | Consola por ámbito; maestro de ubicaciones con dueño por decidir | Base tecnológica | RT-16.01, RT-16.03, RT-16.05 |
| 5.2 Flujos y bandeja | Motor de flujos de trabajo por ámbito | Base tecnológica | RT-16.11 a RT-16.14 |
| 5.3 Documentos, plantillas y firma | Capacidad por ámbito reutilizando el patrón de F:C-03 | Base tecnológica | RT-16.15, RT-16.19, RT-16.17 y RT-16.18 en Retail |
| 5.4 Notificaciones | Servicio por ámbito | Base tecnológica | RT-16.20 a RT-16.25 |
| 5.5 Búsqueda y exportación | Índice por ámbito y patrón de exportación asíncrona | Capa de datos y patrón | RT-16.27 a RT-16.30 |
| 5.6 Consulta de auditoría | Módulo de la consola | Base tecnológica | RT-16.08 |
| 5.7 F:C-04 control regulatorio | Servicio nuevo de la Filial, alcance mínimo a validar | Servicio de negocio | Obligaciones del Caso, no filas de RT-16 |

**Consecuencia para el diagrama lógico.** El bloque «Servicios comunes» de la capa 4 deja de ser un servicio de negocio. Los cinco componentes de la base tecnológica (consola con consulta de auditoría, flujos, documentos y firma, notificaciones, y búsqueda) se dibujan como «Capacidades comunes» de la base tecnológica, una por ámbito, y los cuatro atributos se anotan en cada servicio. Con F:C-04 aprobado, la capa 4 pasa de trece a catorce servicios.

## 6. Integración con la propuesta y con la arquitectura lógica

Este documento no edita nada de `02_Propuesta/`. Lista lo que cambiaría si el equipo aprueba las decisiones de la sección 7.

| Documento | Qué cambiaría | Motivo |
| :-- | :-- | :-- |
| SD-03, 3.3.2 | Agregar F:C-04 si se aprueba (el frente Filial pasa de tres a cuatro servicios; «trece servicios» pasa a catorce en SD-03, línea 98); describir la base tecnológica con sus componentes comunes | Secciones 3.4 y 5 |
| SD-03, 3.2.2 (Tabla 3.1) | Asignar etapa a F:C-04 y a los componentes comunes; respaldar el texto que el T-12 cita como origen de los pendientes | Hallazgo de 4.6 |
| SD-04, Tablas 4.2 y 4.3 y Figura 4.3 | Agregar F:C-04; en la figura, los componentes comunes en la base tecnológica; «los trece códigos» pasa a catorce (SD-04, línea 155) | Secciones 3.4 y 5 |
| SD-04, Tabla 4.6 y ADR | ADR nuevo para los componentes comunes; unificar el bus (ADR-06) y el tenant de la Filial con el diagrama | Sección 4.1 |
| SD-04, línea 304 | Unificar la ubicación de X-01 con las líneas 586 del SD-04 y 298 del SD-03 (en medio) | Registro D-27 |
| SD-05, 5.1.3 y 5.2.4 | Entidades transversales de parámetro, flujo, notificación y documento; mecanismo de inalterabilidad del registro de auditoría | Secciones 4.2 y 5 |
| T-12 | Pasar de «No» a «Sí» o «Parcial» las filas RT-16.01, 16.03, 16.05, 16.08, 16.11 a 16.15, 16.19 a 16.26 y 16.28 a 16.30, con la nueva referencia; RT-16.07: citar el mecanismo general, no solo X-01 | Sección 4 |
| Catálogo y Excel (v3.1) | RF nuevos para cada atributo por servicio, para F:C-04 y para los componentes comunes; un RNF transversal que obligue a los cuatro atributos | Sección 4 y 5.7 |
| SD-07 y SD-09 | Paquetes de trabajo y pruebas para los cinco componentes comunes y, si se aprueba, F:C-04 | Sección 5 |
| Diagrama lógico (`diagramas-arquitectura-logica/`) | Renombrar «Servicios comunes» a «Capacidades comunes» en la base tecnológica; corregir los nombres de las tarjetas a los vigentes («Evidencia financiera»); agregar F:C-04 si se aprueba; corregir códigos RT (parámetros: RT-16.02 a RT-16.05, no RT-16.01; acceso a datos sensibles: RT-16.09, no RT-16.07) | Secciones 1.1 y 5 |

## 7. Decisiones abiertas

| N.° | Decisión | Opciones | Recomendación de este documento |
| :-- | :-- | :-- | :-- |
| 7.1 | ¿Los cuatro atributos son obligación de todo servicio? | Obligación en cada servicio, o solo requisito de la solución (como en las Bases) | Obligación en cada servicio, con un RNF transversal y RF por servicio |
| 7.2 | F:C-04: ¿se crea y con qué alcance? | Servicio nuevo, absorberlo en F:C-02, o dejarlo fuera | Servicio nuevo con alcance mínimo, validado con la contraparte financiera |
| 7.3 | Los cinco componentes comunes: ¿base tecnológica o servicios con código? | Base tecnológica o servicios R/F | Base tecnológica, una instancia por ámbito |
| 7.4 | ¿Quién es dueño del maestro de tiendas, centros, líneas de caja y unidades organizacionales? | Consola de administración, un servicio nuevo de Retail, o un servicio existente | A decidir; sin dueño no se cumplen RT-16.01 ni RNF-48 |
| 7.5 | Documentos y firma de la Filial: ¿F:C-03 o una instancia hermana de la capacidad común? | F:C-03 amplía su alcance, o capacidad común por ámbito | Capacidad común por ámbito; F:C-03 sigue como dueño de la evidencia financiera |
| 7.6 | Inalterabilidad de la auditoría (RT-16.07) frente al administrador de la base | Sellado y exportación a almacenamiento inmutable, u otro mecanismo | Sellado y exportación; por verificar el diseño |
| 7.7 | Acceso sin enlace en el nodo local de tienda | Credenciales en caché con caducidad, u otra | Por definir con el diseño de identidad (RT-12.09, pendiente) |

**Por verificar en general.** Alcance de la normativa aplicable al emisor (Ley 21.521, propuestas de la autoridad del mercado financiero) con el texto oficial; disponibilidad en Azure Chile Central de los servicios nombrados en 4.1; la numeración de RT del Caso frente a la de las Bases cuando se redacte el T-12.
