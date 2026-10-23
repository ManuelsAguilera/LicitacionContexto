# Especificación de los servicios de la capa 4

Documento de contexto, no es entregable. Fecha: 2026-10-22. Estado: borrador para discutir con el equipo. Describe y especifica cada servicio de la capa 4 (servicios de negocio), evalúa si hacen falta servicios nuevos para cumplir las Bases Transversales, y evalúa los cuatro atributos transversales (auditoría, control de acceso, exportación y parámetros) sobre cada servicio. No edita ni reemplaza `02_Propuesta/`: lista en la sección 6 lo que cambiaría. Manda sobre este documento el texto vigente de `sd-03.tex`, `sd-04.tex` y `sd-05.tex`, y la nomenclatura de `80_Artefactos/sd-03_contexto/divisiones_negocio_servicios_sd-03.md`.

## 0. Cómo leer este documento

**Fuentes.** Cada dato lleva su fuente entre paréntesis. Las siglas son: SD-03, SD-04 y SD-05 para los subdocumentos; T-12 para el Formulario T-12 (matriz de cumplimiento técnico); Anexo B para el catálogo de requerimientos (`04_Adjuntos/tablas/sd-03_s2_anexo-b_catalogo-requerimientos.md`); Bases para `00_Bases/Bases_Transversales.md`; Caso para `00_Bases/Caso_09_Cadena_Multitienda.md`.

**Estados.** «Sí» significa que el cumplimiento está declarado y tiene evidencia en un documento vigente. «Propuesto» significa que un requerimiento o una decisión de este documento lo cubriría y aún no está en un documento vigente. «Parcial» significa que está declarado, pero la evidencia cubre solo una parte. «No» significa que está declarado como pendiente o que no hay evidencia. «Por verificar» significa que falta una confirmación externa. «Sin evidencia» significa que no se encontró el dato en los documentos revisados.

**Códigos RT.** Los códigos RT sin sufijo son los de las Bases Transversales; «del Caso» marca el valor del capítulo 15 del Caso, que en RT-03.13, RT-05.10, RT-05.23, RT-05.29 y RT-09.01 trae otro contenido que las Bases. El Caso (capítulo 15) usa además otra numeración para algunos requisitos del capítulo 16: el RT-16.14 del Caso (firma electrónica) corresponde al RT-16.17 de las Bases, el RT-16.21 del Caso (canales de notificación) al RT-16.20 de las Bases, y el RT-16.30 del Caso (portal público) al RT-16.31 de las Bases. Este documento escribe «del Caso» cuando cita un valor de ese capítulo.

**Asignación de RNF.** El catálogo no liga la mayoría de los requerimientos no funcionales a un servicio (solo algunas notas dicen «Mide el servicio de…»). Las asignaciones de RNF a servicios de este documento son una propuesta y se marcan como tal.

**Requerimientos propuestos.** Los que este documento propone siguen la convención del catálogo (hoja «0_Lectura»): estructura «El sistema deberá [verbo] [entidad] [condición]», un solo verbo, un solo caso de prueba Pasa/Falla, el umbral en un RNF aparte y cada RF derivado de una regla de negocio (Anexo C). Los identificadores son correlativos y provisionales: continúan desde RF-231, el último del v3.1, RNF-76 y RN-P05, y se asignan de forma definitiva al incorporarlos al catálogo (art. 72). Las columnas son las del Anexo B. Todos están reunidos en la sección 9.

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
    └── Área Crédito ........... F:C-01 originación · F:C-02 cartera · F:C-03 evidencia financiera · F:C-04 control regulatorio (propuesta aprobada, por validar)
Base tecnológica: integración, identidad y gestión de accesos (incluye repositores externos), observabilidad
```

### 1.1 Tabla maestra

Fuentes de la tabla: nomenclatura y etapa (ficha de alcance del SD-03), requerimientos funcionales (Anexo B, B.1), despliegue candidato (SD-04, Tabla 4.3) y registro principal (SD-04, Tabla 4.2). La columna de despliegue usa cuatro valores. «Microservicio» es una unidad de despliegue independiente, con repositorio de datos propio. «Módulo» es una responsabilidad que comparte despliegue con otras. «Plataforma» es un componente de la base tecnológica, que se despliega pero no es un servicio de negocio. «Por decidir» marca lo que aún no tiene una decisión. Tres precisiones sobre esos valores. Comisiones y marketplace son módulos que se pueden extraer a microservicio si las mediciones lo justifican (SD-04, Tabla 4.3). La oferta comercial se propone como un solo despliegue con dos módulos internos, Catálogo y Precios y promociones, que también se pueden extraer (ADR-OC-01, sección 8). El servicio de control regulatorio es una propuesta: su etapa, su despliegue y sus 13 requerimientos aún no están en el catálogo (secciones 3.4, 5.7 y 9.4). La base tecnológica no es un servicio de negocio y no es dueña de datos de negocio, pero sí se despliega: reúne la puerta de enlace, el bus de eventos, la identidad, los secretos y la observabilidad, con instancias separadas por ámbito en identidad, secretos y observabilidad (SD-04, 4.1). Su «registro principal» es lo que le es propio: identidades y accesos, contratos publicados y telemetría.

| Código | Servicio | Frente · área | Etapa | RF | Despliegue candidato | Registro principal |
| :-- | :-- | :-- | :-: | --: | :-- | :-- |
| R:M-01 | Servicio de oferta comercial | Retail · Mercadería | 1 | 20 | Módulo | Artículos, precios, promociones, vigencias y publicación |
| R:M-02 | Servicio de abastecimiento | Retail · Mercadería | 2 | 3 | Microservicio | Órdenes, transferencias y recepción coordinada |
| R:M-03 | Servicio de existencias | Retail · Mercadería | 1 | 48 | Microservicio | Movimientos conciliados, conteos, reservas y disponible comprometible |
| R:V-01 | Servicio de pedidos | Retail · Venta | 2 | 31 | Microservicio | Estado único, promesa, asignación y seguimiento |
| R:V-02 | Servicio de ventas | Retail · Venta | 1 | 14 | Microservicio | Venta, pago, reversa y conciliación de caja |
| R:V-03 | Servicio de comisiones | Retail · Venta | 2 | 3 | Módulo | Regla y base de atribución |
| R:V-04 | Servicio de marketplace | Retail · Venta | 2 | 25 | Módulo | Reglas de vendedores y coordinación |
| R:CL-01 | Servicio de posventa | Retail · Relación con el cliente | 2 | 12 | Microservicio | Caso y destino de devolución |
| R:CL-02 | Servicio de clientes Retail | Retail · Relación con el cliente | 2 | 5 | Microservicio | Identificación, preferencias y gobierno de datos de fidelización |
| F:C-01 | Servicio de originación de crédito | Filial emisora · Crédito | 1 | 14 | Microservicio | Solicitud, evaluación, cupo y autorización |
| F:C-02 | Servicio de cartera de crédito | Filial emisora · Crédito | 1 y 2 | 6 | Microservicio | Cuenta, saldo, pago, mora, cobranza y repactación |
| F:C-03 | Servicio de evidencia financiera | Filial emisora · Crédito | 1 | 15 | Microservicio | Versiones precontractuales, aceptación, firma y expediente |
| X-01 | Servicio de control de cruces | Frontera · sin área | 1 | 12 | Microservicio | Fichas, políticas, decisiones y bitácora del intercambio |
| F:C-04 | Servicio de control regulatorio (propuesta) | Filial emisora · Crédito | 1 | 13 | Microservicio | Expediente de cumplimiento y de reportes regulatorios |
| — | Base tecnológica | Transversal | 1 | 19 | Plataforma | Identidades y accesos, contratos publicados y telemetría |

La suma de requerimientos funcionales de los trece servicios y la base tecnológica es 227 (Anexo B, B.1). Los requerimientos propuestos no están incluidos en esa suma: 13 de F:C-04, 20 de abastecimiento (de 3 a 23), 9 de existencias (de 48 a 57), 8 de cartera (de 6 a 14), 7 de pedidos (de 31 a 38), 4 de posventa (de 12 a 16), 1 de ventas (de 14 a 15), 1 de comisiones (de 3 a 4), 1 de originación (de 14 a 15) y 2 de la base tecnológica (de 19 a 21). Están en la sección 9 con numeración provisional.

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
- **Ubicación.** Retail · Mercadería · Etapa 1. El SD-04 (Tabla 4.3) lo deja por decidir entre uno o dos microservicios. Este documento propone un despliegue con dos módulos internos, Catálogo y Precios y promociones, con contratos, esquemas y eventos propios y extraíbles a microservicio si fallan las condiciones medidas (ADR-OC-01, sección 8). Sigue siendo un solo servicio con el código R:M-01.
- **Autoridad del dato.** Catálogo de artículos, precio vigente y publicado, promociones y su vigencia. Es el dueño único de la entidad Catálogo (T-12, RT-05.09).
- **Qué no hace.** No reserva existencias ni registra ventas (SD-04, Tabla 4.2).
- **Capacidades (20 RF).**
  - Propagación del cambio de precio a las 380 líneas de caja, al canal digital y a los puntos de exhibición (RF-016, RF-017, RF-018) y agrupación de cambios en ventanas parametrizadas fuera del horario de atención (RF-030).
  - Registro de la etiqueta cambiada y de su ejecutor (RF-019, RF-020), indicador diario de exhibiciones desactualizadas (RF-029) y bloqueo de la venta al precio nuevo mientras la exhibición no se actualiza (RF-028; propuesta de retirarlo o reformularlo, ver 8.4).
  - Precio vigente según el último propagado y cobro del menor de los dos precios (RF-022, RF-023); registro de incidente de discrepancia (RF-024).
  - Recuperación del precio publicado de una referencia en una fecha, hora y canal arbitrarios (RF-021).
  - Vigencia, canal y tienda de cada promoción (RF-032, RF-033, RF-034). Oferta comercial publica la versión aprobada de precio y promoción por canal y vigencia. Ventas, y pedidos en el canal digital, comprueban la elegibilidad del cliente y aplican y registran la versión (SD-03, 3.4.2).
  - Completitud de atributos para publicar (RF-142, RF-143) y reportes de incompletos y de publicaciones fallidas (RF-147, RF-148).
  - Consulta pública del precio vigente (RF-064).
- **Requisitos asociados.** RNF-19 (propagación en un máximo de 5 minutos), RNF-44 (trazabilidad del precio por 3 años), RNF-58 (recuperación del precio en un máximo de 1 minuto), RNF-52 (estándar de catálogo e identificación de producto). Caso: RT-05.29 (precio en cajas y canal digital en un máximo de 5 minutos) y RT-05.10 (trazabilidad de precio por 3 años). Las etiquetas electrónicas quedan fuera (EXC-02).
- **Interfaces.** Entrega la oferta vigente a los canales, a existencias, a pedidos, a ventas y a marketplace (SD-03, 3.3.2). Alimenta las innovaciones de búsqueda vectorial multimodal y de Retail Media Network, que dependen del catálogo (SD-13).
- **Operación sin enlace.** Las condiciones vigentes se conservan en el nodo local de la tienda (SD-03, 3.3.2); la ventana de 24 horas rige para venta y consulta (RT-03.10).
- **Resultado de la pasada (2026-10-22).** Las seis condiciones del ADR-OC-01 se miden en Preproducción, con la prueba de carga que el T-12 ya declara (RT-09.06, «Sí»): **supuesto SP-14**. El tratamiento de RF-028, RF-022 y RF-023 está decidido (opción B); falta la aprobación de Comercial y del Comité (art. 72): **supuesto SP-09**. RF-025 a RF-027 se eliminaron por EXC-02: **ya se cumple**.

#### R:M-02 · Servicio de abastecimiento

- **Definición.** Administra órdenes, transferencias, propuestas de reposición y recepciones para coordinar proveedores, tiendas y centros de distribución (SD-03, 3.3.2).
- **Ubicación.** Retail · Mercadería · Etapa 2 · microservicio, por tener autoridad propia (SD-04, Tabla 4.3).
- **Autoridad del dato.** Órdenes, transferencias y recepción coordinada.
- **Qué no hace.** La ejecución física de ubicaciones, preparación y despacho sigue en el WMS (sistema de almacenes del centro de distribución principal). Las planillas de Concepción no pasan a ser autoridad permanente (SD-03, 3.3.2). El ERP/DTE conserva cuentas por pagar y contabilidad: abastecimiento es dueño de la orden operativa y le entrega lo necesario para cuentas por pagar (decisión aprobada el 2026-10-22; falta agregarlo a la Tabla 4.2 del SD-04).
- **Capacidades (3 RF vigentes y 20 propuestos).** Propuesta diaria de reposición con el disponible vigente (RF-144), ajuste por el planificador de logística (RF-145) y registro del ajuste con usuario, valor propuesto y valor confirmado (RF-146). Los veinte propuestos cubren órdenes (RF-232, RF-233), recepciones (RF-234 a RF-237), movimiento hacia existencias (RF-238), conformidad firmada (RF-239), diferencias entre lo solicitado y lo recibido (RF-240), transferencias (RF-241) y consulta del proveedor (RF-242, RF-243), y los atributos transversales de parámetros (RF-272, RF-279), auditoría (RF-273 a RF-275), acceso (RF-276) y exportación (RF-277, RF-278), derivados de las entidades RE-06 a RE-08, RE-28 y RE-29 del SD-05 y de las reglas RN-P04 y RN-P06 a RN-P11. Los identificadores son provisionales. Detalle en 9.1.
- **Requisitos asociados.** RNF-53 (estándar de intercambio de órdenes y avisos con los 940 proveedores), RNF-40 (mecanismo de integridad en la conformidad de recepción de mercadería). Caso: la conformidad de recepción exige firma electrónica (RT-16.14 del Caso).
- **Interfaces.** Consulta el disponible de existencias; se integra con ERP/DTE y con el WMS (SD-03, 3.3.2).
- **Por resolver.** Los veinte RF y las reglas RN-P06 a RN-P11 y RN-P17 están propuestos en el formato del catálogo y falta incorporarlos. Las decisiones siguientes quedaron aprobadas el 2026-10-22:
  - **Etapa de RNF-40 y RNF-53 (aprobada).** El catálogo los marca como Etapa 1 y abastecimiento es Etapa 2. RNF-40 se mantiene en Etapa 1 porque la capacidad de documentos y firma es parte de la base tecnológica (Etapa 1); su verificación en Retail ocurre cuando abastecimiento y posventa entran en la Etapa 2. RNF-53 queda en Etapa 1, medido sobre la base tecnológica y sus adaptadores.
  - **Dueño de las órdenes de compra (aprobada).** El Caso asigna órdenes de compra y recepción al sistema central de 2009, que se reemplaza, y el ERP/DTE conserva cuentas por pagar y contabilidad. Abastecimiento es dueño de la orden operativa y el ERP/DTE recibe lo necesario para cuentas por pagar. Hay que agregarlo a «qué no hace» en la Tabla 4.2 del SD-04 y verificarlo con Logística y Finanzas.
  - **Proveedor piloto (aprobada).** RNF-53 exige una prueba de intercambio con un proveedor piloto. Los 940 proveedores se clasifican en intercambio electrónico, API y portal (SD-05, 5.2.6) y el piloto se elige al inicio del proyecto, por volumen y capacidad técnica.
  - **Parámetros de reposición (aprobada).** Las reglas de la propuesta de reposición deben ser parametrizables por el Cliente sin desarrollo, con un segundo perfil que apruebe sus cambios (RF-272 y RF-279). El contenido de las reglas se define con la Gerencia de Logística; no hay fuente para proponerlo.
  - **Atributos transversales (aprobada).** Auditoría de órdenes, recepciones y transferencias (RF-273 a RF-275), acceso por rol (RF-276) y exportación de órdenes y de propuestas de reposición (RF-277, RF-278), más RNF-15 y RNF-78 a RNF-80 (9.5).
- **Por verificar (resultado de la pasada del 2026-10-22).**
  - **Contrato con el WMS (planificado).** El SD-07 (EDT 1.2, «Levantamiento y línea base de alcance») exige el mapa de interfaces aprobado por el Cliente; el adaptador se especifica después de ese entregable.
  - **Concepción (aceptada automáticamente).** Queda ligada al informe de evaluación de Concepción (EXC-13, SUP-20, RN-61), ya decidido en existencias.
  - **Línea base de reposición (fuera del mínimo).** El Caso no fija un resultado de aceptación para la reposición (el cap. 18 y el Anexo D no lo incluyen). Se mide como indicador del piloto, sin meta contractual.

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
- **Por resolver.** Propuestas aprobadas el 2026-10-22; la precedencia y el alta de nodo se resolvieron en la pasada de resolución del mismo día. Los identificadores de la sección 9 son provisionales y se numeran al incorporarlos al catálogo (art. 72).
  - **Plazo de 30 segundos sin RNF (aprobada).** Se agregan RNF-77 y RNF-84 (exactitud por categoría actualizada diariamente, RT-05.29 del Caso). Detalle en 9.2 y 9.5.
  - **Ruta de publicación (aprobada).** Aplicar en el SD-04 la decisión D-33: Service Bus Premium por ámbito en lugar de Event Hubs (l.250, l.274, l.314 y ADR-06). Event Hubs solo entra si la prueba de carga de precios (1.333 eventos por segundo) lo exige. Comprobar en Preproducción que los 1.135 mensajes por segundo del pico cumplen los 30 segundos con Service Bus; las unidades de mensajería están sin dimensionar. El SD-04 (ADR-06) descartó Service Bus porque no ofrece historial ya consumido para reconstruir proyecciones; esa razón no aplica a la autoridad, porque las proyecciones se reconstruyen desde el registro de existencias y desde RE-02 (ADR-OC-01, regla 6) y no desde el bus.
  - **Colchón de confianza (aprobada).** Valor inicial: el descuento fijo de 2019 como regla de referencia por categoría. Calibración con el historial depurado de conteos, ventas, movimientos, reservas y quiebres (SD-03, 3.4.1). Despliegue gradual por categorías en el mes 16 (Anexo D, resultado 1). El piloto compara cancelaciones y unidades retenidas contra la regla de referencia. Tolerancia de conteo inicial de 2 %, la meta del Caso, a confirmar en el levantamiento. Todo cambio lleva aprobación de un segundo perfil (RT-16.03) y registro de quién lo hizo (RF-151). Si el modelo no supera la regla, se mantiene la parametrización supervisada.
  - **Regla de precedencia (RF-098) (elaborada y aceptada en la pasada).** Nueva regla RN-P18, basada en el estado físico de la unidad y no en el instante: la venta en sala prevalece sobre todo compromiso digital aún no preparado; una unidad ya preparada para un pedido sale de la venta en sala (RF-286) y prevalece el pedido; entre dos compromisos digitales prevalece el confirmado primero en la secuencia del registro de existencias. Es coherente con RF-001, RF-038, RF-041, RF-044, RN-48 y RT-03.13 (resultado determinista). El compromiso que pierde entra en la resolución de pedido no cumplible (RN-P19).
  - **Alta de un nodo por parametrización (elaborada y aceptada en la pasada).** RF-292, porque el nodo logístico (RE-26) ya es de existencias (decisión 7.4).
  - **Concepción (aprobada).** Informe de evaluación (EXC-13) con alternativas costeadas, su efecto en el error probable del nodo y una recomendación fundada. Las alternativas se definen con Logística. Lo prepara el proponente antes del diseño detallado de existencias; el documento donde vive está por decidir.
  - **Catálogo y Excel (aprobada).** Corregir las referencias antiguas: RF-160 y RF-161 citan «RF-058» y deben citar RF-158 y RF-159. RF-183 ya cita RF-177 en el catálogo v3.0 y en el Anexo B; la numeración antigua solo está en la hoja de equivalencias del Excel, por verificar allí. Merma: se mantienen los seis componentes de RF-138 y del SD-03 (3.4.1), porque la narrativa del Caso (cap. 4, l.219) nombra las unidades mal ubicadas como causa conocida. El criterio de aceptación 5 se mide con los cinco componentes del Caso (decisión 17 y Anexo D, resultado 5) y la sexta se informa aparte; hay que declararlo en el Anexo D.
  - **Atributos transversales (aprobada).** Auditoría de movimientos, reservas y ajustes (RF-244 a RF-246), acceso a la existencia por tienda según el rol (RF-247), exportación de movimientos y de conteos (RF-248, RF-249) y segundo perfil para modificar el colchón (RF-250), más los RNF transversales RNF-78 a RNF-80. La auditoría general ya la cubre RNF-15. Detalle en 9.2 y 9.5.
- **Por verificar (resultado de la pasada del 2026-10-22).**
  - **Modelos de conteo y de merma (planificado).** SD-03 (3.4.1) y SD-04 (l.217) ya definen su validación y la alternativa supervisada.
  - **Cifras de capacidad (planificado).** Prueba de carga a 1,5 veces el peak declarada en el T-12 (RT-09.06, «Sí»).
  - **Despliegue interno (planificado).** ADR-05 del SD-04, condicionado a prueba de carga, fallas aisladas y costo.

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
- **Por resolver (resultado de la pasada del 2026-10-22).**
  - **RNF-05 frente a «tiempo real» (aceptada automáticamente; desviación declarada en SP-15).** El Caso exige el estado del pedido «en tiempo real y consistente en todos los canales» (RT-05.29) y el catálogo, 0 % de discrepancias (RNF-04). Umbral: tiempo real mediante consulta directa al estado único en R:V-01, que es lo que declara el SD-05 (Tabla 5.6) y el T-12 (RT-05.29, «Sí»). Solo las plataformas conservadas que guarden una copia propia (comercio electrónico y marketplace) tendrían un desfase de 30 s o menos, y eso es una desviación que el proponente declara en SP-15, no una reinterpretación del requisito.
  - **Regla de resolución de un pedido no cumplible (elaborada y aceptada).** RN-P19: primero se reasigna dentro de la ventana (RF-056, RF-058); si no es posible, se ofrece al cliente producto equivalente, espera compensada o liberación (RF-059 a RF-061); el cobro no se captura sin aceptación explícita (RF-047) y la liberación anula la preautorización (RF-061). Se propone quitar «derivar a tercero» de RF-046, porque no tiene definición ni RF. Coherente con SD-03 (3.4.1), SUP-11 y RNF-65.
  - **Valores de los parámetros (elaborada y aceptada).** SUP-28: los valores iniciales de la ventana de reasignación, la compensación, el umbral de prioridad y el límite de unidades por cliente se fijan con Comercial y Logística en el levantamiento y se ajustan tras el piloto. La vigencia de la reserva ya está en SUP-12: **ya se cumple**.
  - **Costo total de servir (elaborada y aceptada; los datos, como supuesto SUP-29).** SUP-29: la fórmula y la fuente de cada término de RF-076 se definen al inicio con Logística y Finanzas; la aceptación es el registro de cada término por asignación (RF-078; Anexo D, resultado 11). Los factores de asignación ya están en SUP-13. Desempate: RN-P20, a igual costo total gana el punto con mayor disponible confiable y, si persiste, el centro de distribución antes que una tienda.
  - **Atributos transversales (aceptada automáticamente).** RF-280 a RF-285 y RF-297 (9.7).
- **Por verificar (resultado de la pasada del 2026-10-22).**
  - **Medios de pago (supuesto SP-06).** Matriz de capacidades por medio (preautorización, captura diferida, anulación y vigencia) en el primer semestre. Si un medio no lo soporta, se desactiva en pedidos con riesgo (RF-181) o se avisa antes del cobro (RT-16.21 del Caso).
  - **Transportistas (supuesto SP-07).** Censo y clasificación por capacidad (EPCIS o portal, SD-05 5.2.6) y transportista piloto antes del desarrollo de la Etapa 2.
  - **Concepción (ya se cumple).** RF-075 y RN-15 la excluyen como origen de promesa hasta acreditar un sistema de almacenes.
  - **Lockers (supuesto SP-08).** La interfaz se valida en la selección del proveedor de la innovación y el ensayo se acepta en la marcha blanca de la Etapa 2, con habilitación en el mes 21 (SD-13).
  - **Cifras de carga (planificado).** Prueba de carga a 1,5 veces el peak (T-12, RT-09.06). Observar el evento anual de junio, si se repite en 2027, queda como mejora sujeta al acceso a datos del Cliente.
  - **Ruta de publicación (aceptada automáticamente).** Se resuelve con la unificación a Service Bus ya aprobada en existencias.

#### R:V-02 · Servicio de ventas

- **Definición.** Registra ventas, pagos, reversas y registros de caja del punto de venta y del canal digital, incluidas las operaciones realizadas sin enlace que se sincronizan después. Concilia esos hechos (SD-03, 3.3.2).
- **Ubicación.** Retail · Venta · Etapa 1 · microservicio (SD-04, Tabla 4.3).
- **Autoridad del dato.** Venta, pago, reversa y conciliación de caja.
- **Qué no hace.** El ERP/DTE es el único emisor tributario (SD-04, Tabla 4.2).
- **Capacidades (14 RF).** Conmutación a modo desconectado y de vuelta (RF-082, RF-088), registro y cobro sin enlace (RF-083, RF-084), promociones y folios de contingencia sin enlace (RF-085, RF-086), marca de la operación desconectada (RF-094), conciliación idempotente de ventas y documentos (RF-095 a RF-097), informe de excepciones (RF-099), emisión de documentos por el ERP/DTE (RF-100), venta física con reserva digital activa (RF-001) y desactivación temporal de medios de pago de mayor fricción (RF-181).
- **Requisitos asociados.** RNF-18 (venta completa en un máximo de 25 s), RNF-24 a RNF-28 (24 horas sin enlace, sincronización en un máximo de 30 minutos, sin pérdida ni duplicados), RNF-41 (documentos por 6 años), RNF-34 (medios de pago tokenizados), RNF-56 (formato vigente de documento tributario electrónico).
- **Interfaces.** Entrega la venta confirmada a comisiones y posventa; mantiene el estado del documento con el ERP/DTE (SD-03, 3.3.2). Para la compra con tarjeta propia consulta a originación a través de la frontera (SD-04, 4.1).
- **Operación sin enlace.** Es el servicio con mayor exigencia: venta, cobro y emisión de documentos con el nodo local por 24 horas (RT-03.10 de las Bases prevalece sobre el 8 h del Caso).
- **Resultado de la pasada (2026-10-22).** Cupo preaprobado sin enlace: **ya declarado** con plan alternativo (SD-04, 4.1; RC-11 del Anexo A), con los topes de la Filial como **supuesto SP-05**. Líneas de caja de una tienda: **elaborada y aceptada**, RF-293 (decisión 7.4).

#### R:V-03 · Servicio de comisiones

- **Definición.** Aplica reglas auditables para atribuir una venta y su base de comisión al canal, vendedor y tienda que corresponden, incluso cuando una tienda abastece un pedido de otro canal (SD-03, 3.3.2).
- **Ubicación.** Retail · Venta · Etapa 2 · módulo, que se extrae a microservicio si las mediciones lo justifican (SD-04, Tabla 4.3).
- **Autoridad del dato.** Regla y base de atribución.
- **Qué no hace.** No administra remuneraciones: el ERP/DTE las conserva.
- **Capacidades (3 RF).** Base de comisión reconociendo al vendedor y a la tienda de origen (RF-054), transmisión condicionada al movimiento real de inventario (RF-055) y base considerando canal de origen y de cumplimiento (RF-071).
- **Requisitos asociados.** No hay RNF específico en el catálogo (sin evidencia).
- **Interfaces.** Consume pedidos y ventas; entrega la base calculada al proceso de remuneraciones del ERP/DTE.
- **Resultado de la pasada (2026-10-22).** Completitud (3 RF): **fuera del mínimo**; las Bases no exigen un número de requerimientos y RF-054, RF-055 y RF-071 cubren la decisión 14 del Caso. Reglas de atribución: **elaborada y aceptada**, RF-287 las hace parametrizables (RT-16.02 y RT-16.04).

#### R:V-04 · Servicio de marketplace

- **Definición.** Relaciona la plataforma de marketplace de 2022 con la oferta, disponibilidad, pedidos, devoluciones y liquidaciones que gestiona Ancoa, y administra las reglas de habilitación y desempeño de vendedores externos (SD-03, 3.3.2).
- **Ubicación.** Retail · Venta · Etapa 2 · módulo (SD-04, Tabla 4.3).
- **Autoridad del dato.** Reglas de vendedores y coordinación.
- **Qué no hace.** No sustituye la plataforma de marketplace de 2022 ni opera la logística de cada vendedor (SD-03, 3.3.2; EXC-12).
- **Capacidades (25 RF).** Existencia declarada por el vendedor (RF-102, RF-103, RF-104, RF-109), indicadores de nivel de servicio (RF-105), devoluciones y su costo (RF-106, RF-107, RF-108, RF-111), consultas del vendedor (RF-110, RF-112), visibilidad al cliente de vendedor, despachador y condiciones (RF-113 a RF-116), separación entre inventario propio y de terceros (RF-117, RF-118), reglas de evaluación con acuse previo y matriz de escalamiento (RF-119 a RF-123), despublicación por stock vencido (RF-124) y base de comisión de marketplace al ERP/DTE (RF-125, RF-126).
- **Requisitos asociados.** RNF-02 (interfaz de declaración 24x7 con 99,5 %), RNF-55 (estándar de sincronización con vendedores), RNF-66 (notificación de devolución en un máximo de 15 minutos), RNF-67 (sin mercadería sin aviso a su dueño).
- **Interfaces.** Se apoya en oferta comercial, existencias, pedidos y posventa (SD-03, 3.3.2).
- **Resultado de la pasada (2026-10-22).** El flujo de aprobación de sanciones (RF-122) lo provee el motor de flujos de trabajo de la base tecnológica (decisión 7.3): **aceptada automáticamente**.

### 3.3 Frente Retail · Área Relación con el cliente

#### R:CL-01 · Servicio de posventa

- **Definición.** Abre y resuelve los casos de cambio, devolución, retracto y garantía, con registro de recepción, inspección y destino de cada unidad (SD-03, 3.3.2). La atención no se supedita a la conciliación posterior con el vendedor o el fabricante.
- **Ubicación.** Retail · Relación con el cliente · Etapa 2 · microservicio, por tener reglas y autoridad propias del caso (SD-04, Tabla 4.3).
- **Autoridad del dato.** Caso y destino de devolución.
- **Qué no hace.** El reintegro al disponible queda sujeto a inspección (SD-04, Tabla 4.2).
- **Capacidades (12 RF vigentes y 4 propuestos).** Los cuatro propuestos cubren la constancia de devolución firmada (RF-288) y el derecho a retracto (RF-289 a RF-291; sección 9.7). Garantía legal íntegra en mesón sin derivar (RF-187, RF-188), motivo y aptitud de la devolución (RF-189, RF-191), bloqueo del reingreso al disponible sin inspección (RF-190), las tres opciones de garantía y su registro (RF-192, RF-193, RF-194), plazo de garantía parametrizable por tipo de producto (RF-195) e hitos de resolución y de recuperación contra el tercero independientes (RF-196, RF-197, RF-198).
- **Requisitos asociados.** RNF-69 (sin derivación como condición de atención), RNF-20 (registro de devolución en un máximo de 60 s), RNF-40 (mecanismo de integridad en la constancia de devolución). Caso: la constancia de devolución exige firma electrónica (RT-16.14 del Caso).
- **Interfaces.** Consulta la venta en ventas; informa a existencias cuándo una unidad vuelve al disponible; coordina marketplace y las notas de crédito con el ERP/DTE.
- **Resultado de la pasada (2026-10-22).** Firma de la constancia de devolución: **elaborada y aceptada**, RF-288 con la capacidad de documentos y firma por ámbito (decisión 7.5). Derecho a retracto de las compras a distancia (Caso 16.1, decisión 22; SUP-22), que no tenía regla ni RF: **elaborada y aceptada**, RN-P21 y RF-289 a RF-291; el reingreso de la unidad ya lo cubre RF-190. El plazo legal del retracto queda como **supuesto SP-13**.

#### R:CL-02 · Servicio de clientes Retail

- **Definición.** Administra identificación y deduplicación de clientes, puntos, segmentos, campañas y preferencias dentro de Retail. Integra el sistema de fidelización de 2017 bajo separación de datos (SD-03, 3.3.2; EXC-15).
- **Ubicación.** Retail · Relación con el cliente · Etapa 2 · microservicio (SD-04, Tabla 4.3).
- **Autoridad del dato.** Identificación, preferencias y gobierno de los datos de puntos, segmentos y campañas.
- **Qué no hace.** No recibe saldo, mora ni comportamiento de pago. Cualquier solicitud de datos de la Filial pasa por X-01.
- **Capacidades (5 RF).** Consolidar duplicados en un registro Retail (RF-227), movimientos de puntos (RF-228), segmentos solo con atributos comerciales (RF-229), campañas (RF-230) y sincronización con la fidelización conservada (RF-231).
- **Requisitos asociados.** RNF-46 (datos de fidelización por la duración de la relación más 2 años), RNF-74, RNF-75 y RNF-76 (finalidad, base de licitud y registro de tratamiento de datos personales).
- **Interfaces.** Sincroniza con el sistema de fidelización de 2017. Alberga la innovación de Modo Tienda con fila virtual de probadores (SD-13).
- **Resultado de la pasada (2026-10-22).** RF-227 a RF-231 se incorporan al Excel oficial con la misma solicitud de cambio que el resto (sección 6): **aceptada automáticamente**.

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
- **Resultado de la pasada (2026-10-22).** Alcance de la Ley 21.521 y del Anexo Técnico N.° 3: **supuesto SP-10**. Mesón financiero de una tienda nueva: **elaborada y aceptada**, RF-294 (decisión 7.4).

#### F:C-02 · Servicio de cartera de crédito

- **Definición.** Administra cuentas, saldos, cuotas, pagos, mora, cobranza y modificaciones de condiciones (SD-03, 3.3.2).
- **Ubicación.** Filial emisora · Crédito · Etapas 1 y 2 (por tramos) · microservicio, separado por migración y operación (SD-04, Tabla 4.3).
- **Autoridad del dato.** Cuenta, saldo, pago, mora, cobranza y repactación.
- **Qué no hace.** Sus saldos no se publican en clientes Retail ni en perfiles comerciales (SD-03, 3.3.2).
- **Capacidades (6 RF vigentes y 8 propuestos).** Consulta del estado de cuenta y de documentos por el cliente autenticado (RF-069, RF-070), gestión de cobranza con medio, instante y ejecutor (RF-211, RF-212), bloqueo de la cobranza fuera de los límites normativos (RF-213) y reporte de conciliación diaria de saldos durante la migración (RF-216). Los ocho propuestos cubren reglas del Anexo C que no tenían ningún RF: imputación de pagos (RN-42; RF-251, RF-252), gastos de cobranza extrajudicial (RN-43; RF-253, RF-254) y comunicaciones de cobranza (RN-44; RF-255 a RF-258). Los identificadores son provisionales y se numeran al incorporarlos al catálogo (art. 72). Detalle en 9.3.

- **Requisitos asociados.** RNF-08, RNF-09 y RNF-10 (migración de 620.000 clientes sin pérdida, sin interrumpir el cobro y sin divergencias), RNF-31 (24x7 en pagos, estado de cuenta y bloqueo de tarjetas), RNF-38 (registro de todo acceso a la cartera, al comportamiento de pago y a los antecedentes de evaluación), RNF-42 (retención del crédito más 6 años), RNF-68 (restauración desde archivo frío en un máximo de 24 horas).
- **Interfaces.** Consulta a F:C-03 antes de confirmar una repactación y conserva la trazabilidad de su expediente (SD-03, 3.3.2). Su migración se hace por olas conciliadas.
- **Resultado de la pasada (2026-10-22).** Con los ocho RF propuestos quedan cubiertas la imputación de pagos (RN-42) y los gastos y comunicaciones de cobranza (RN-43, RN-44). El derecho a retracto no es de cartera: es de las compras a distancia y lo atiende posventa (Caso 16.1, decisión 22; SD-03, 3.3.2), donde se resolvió. Los tramos, plazos y horarios de RN-43 y RN-44 quedan como **supuesto SP-12**. Con los propuestos el servicio sumaría 14 RF.

#### F:C-03 · Servicio de evidencia financiera

- **Definición.** Custodia la versión de la información precontractual entregada, la aceptación, el consentimiento y la evidencia de firma vinculados a cada operación (SD-03, 3.3.2).
- **Ubicación.** Filial emisora · Crédito · Etapa 1 · microservicio, separado por custodia y retención (SD-04, Tabla 4.3).
- **Autoridad del dato.** Versiones precontractuales, aceptación, firma y expediente.
- **Qué no hace.** No decide crédito ni administra saldos.
- **Capacidades (15 RF).** Exigencia de la entrega completa de información precontractual (RF-199, RF-206), registro de versión, instante, medio y contenido o huella (RF-200 a RF-204, RF-205), consentimiento expreso e informado (RF-207), bloqueo de modificaciones sin evidencia (RF-208), reconstrucción del acto (RF-209), restauración desde archivo frío (RF-210), enlaces del expediente de repactación con la cobranza y el consentimiento (RF-214, RF-215) y consulta pública de la información precontractual (RF-217).
- **Requisitos asociados.** RNF-39 (integridad verificable), RNF-43 (retención del crédito más 6 años, recuperable a 10 años), RNF-57 (recuperación en un máximo de 5 minutos), RNF-68. Caso: RT-05.10 (retención) y firma electrónica en apertura, aceptación y repactación (RT-16.14 del Caso). T-12 declara firma electrónica avanzada con un prestador acreditado, sello criptográfico SHA-256 encadenado y custodia WORM (RT-16.16 a RT-16.18).
- **Interfaces.** Originación y cartera lo consultan para impedir una originación o repactación sin evidencia suficiente (SD-03, 3.3.2).
- **Resultado de la pasada (2026-10-22).** Firma de los actos de Retail: **elaborada y aceptada** con la capacidad de documentos y firma por ámbito (decisión 7.5), RF-239 (abastecimiento) y RF-288 (posventa). F:C-03 sigue como dueño de la evidencia financiera.

#### F:C-04 · Servicio de control regulatorio (opción 1 aprobada, por validar)

- **Definición propuesta.** Servicio dueño de los registros que el emisor debe producir ante la autoridad del mercado financiero y en prevención de lavado de activos. Aparece como «nuevo» en el esquema de Miro del equipo. No existe como servicio en SD-03, SD-05, T-12 ni en el catálogo; el SD-04 (l.103) nombra el «reporte regulatorio» solo como un destino condicionado a pruebas, sin servicio responsable. El alcance con prevención de lavado y reportes regulatorios (opción 1 de 5.7) quedó aprobado en esta conversación el 2026-10-22; falta validarlo con la contralora y con el texto oficial de la normativa.
- **Ubicación.** Filial emisora · Crédito · Etapa 1 (propuesta, ver razón abajo) · microservicio (propuesta, ver 5.7).
- **Autoridad del dato.** Expediente de debida diligencia por cliente del Emisor, operaciones sospechosas y su reporte, y el expediente de cada reporte regulatorio (catálogo de archivos, calendario, versión, validación y envío).
- **Qué no hace.** No decide crédito (F:C-01), no lleva saldos ni cobranza (F:C-02), no custodia el consentimiento (F:C-03) y no controla el intercambio con Retail (X-01). No define la política de riesgo de la Filial ni el formato de los archivos: los fija la autoridad (SD-05, 5.2.6).
- **Por qué hace falta.** El Caso (cap. 12) exige al emisor gobierno, control interno y reporte, y conocimiento del cliente, reporte de operaciones y conservación de antecedentes en prevención de lavado de activos, y advierte que invocar una norma sin explicar el control concreto se evalúa como no acreditada. El SD-02 (Tabla 2.1) lo declara como brecha: «conocimiento del cliente en la originación» (Ley 19.913). La regla RN-45 (Anexo C) lo exige y ningún RF del catálogo la cubre. El SD-05 compromete la generación de los archivos para la CMF desde las entidades del Emisor, con el primer archivo validado con el Cliente antes del paso a producción de la Etapa 1, y ningún servicio es dueño de esa función.
- **Capacidades y requerimientos propuestos (13).** Prevención de lavado de activos: expediente de debida diligencia, operaciones sospechosas y su reporte, acceso restringido y conservación (RF-259 a RF-264, de la regla RN-45). Reportes regulatorios: catálogo, calendario, generación, costo total del crédito, versión, validación y envío de cada archivo (RF-265 a RF-271, de la regla propuesta RN-P16). Los identificadores son provisionales: no están en el catálogo y se numeran al incorporarlos (art. 72). Detalle en 9.4.

- **Requisitos asociados.** RT-16.06 a RT-16.10 (auditoría; el acceso a estos expedientes se registra), RT-12.05 (matriz de roles con el responsable de cumplimiento), RT-11.10 (cifrado de campo del Emisor), RNF-11 a RNF-14 (los datos permanecen en el ámbito del Emisor). Caso: RT-05.10 (retención de PLA conforme a la normativa).
- **Interfaces.** Lee entidades del Emisor (EM-01 y EM-05 a EM-10) mediante contratos de F:C-01 y F:C-02; no accede a datos de Retail. Entrega los archivos a la autoridad por el canal que esta fije (por verificar). El responsable de cumplimiento es su usuario principal.
- **Etapa 1, por qué.** El servicio de originación va en la Etapa 1 y la prevención aplica desde la originación en el punto de venta (Caso, cap. 12): sin este control el registro oficial desde el mes 16 queda incompleto. El primer archivo para la CMF debe validarse antes del paso a producción de la Etapa 1 (SD-05, 5.2.6). Cumple la tercera prueba del SD-03 (3.2.2): es necesario para que la Etapa 1 sea el registro oficial de la originación.
- **Por verificar (supuesto SP-11).** El alcance exacto depende de la normativa aplicable (Ley 19.913, instrucciones de la autoridad del mercado financiero y su propuesta sobre servicios externalizados): hay que validarlo con el texto oficial y con la contralora, que es también jefa de cumplimiento (Caso, entrevistas). El Caso lista en 16.2 la prevención de lavado como «materia a investigar» (RN-45, Anexo C).
- **Vacíos de cartera detectados al definirlo.** Tres reglas del Anexo C sin RF (RN-42, RN-43 y RN-44) no son de F:C-04 y se agregan a F:C-02 como RF-251 a RF-258 (ficha de F:C-02 y 9.3).

### 3.5 Frente Frontera

#### X-01 · Servicio de control de cruces

- **Definición.** Define y versiona las condiciones de cada intercambio entre Retail y la Filial: finalidad, fundamento, solicitante, destinatario y datos mínimos. El ámbito que entrega verifica la política antes de liberar información y el receptor limita su uso a la finalidad aprobada. Ambos extremos registran autorizaciones, denegaciones y versión de política (SD-03, 3.3.2).
- **Ubicación.** Frontera · sin área · Etapa 1 · microservicio con almacén propio (SD-04, Tabla 4.3). Es la única ruta entre Retail y la Filial (SD-03, 3.3.2; SD-04, 4.1). En el diagrama lógico se dibuja en medio de los dos frentes (decisión D-17 y D-28 del registro).
- **Autoridad del dato.** Fichas, políticas, decisiones y bitácora del intercambio.
- **Qué no hace.** No crea un maestro único de clientes ni habilita atributos financieros para Marketing; no almacena perfiles unificados (SD-04, Tabla 4.2).
- **Capacidades (12 RF).** Registro de cada cruce con el dato que cruzó (RF-165), bloqueo de cruces sin interfaz autorizada y registro del intento (RF-166, RF-167), inventario de interfaces de cruce mantenido por el responsable de cumplimiento (RF-168), rechazo de interfaces sin finalidad, base de licitud y evaluación de impacto (RF-169, RF-176), exclusión de atributos financieros del motor de campañas (RF-170, RF-171, RF-172) e identificador distinto por ámbito con correspondencia solo durante un cruce autorizado (RF-173, RF-174, RF-175).
- **Requisitos asociados.** RNF-11 a RNF-14 (separación lógica y física implementada, documentada y verificada por auditoría independiente), RNF-74 a RNF-76 (finalidad, licitud y registro de tratamiento). Caso: RT-16.09 exige el registro de todo cruce, indicando dato, finalidad, base y quién autorizó.
- **Interfaces.** Aplica las políticas en ambos extremos. La compra con tarjeta propia en caja es el único enlace previsto entre los dos frentes (SD-04, 4.1).
- **Resultado de la pasada (2026-10-22).** Contradicción del SD-04 (l.304 frente a l.586): **aceptada automáticamente**, corrección listada en la sección 6. Retención de la bitácora: **elaborada y aceptada**, RNF-81 con un mínimo de cinco años (RT-16.10) o el plazo mayor que apruebe el Cliente.

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

**¿Se cumplía antes?** En la escritura, sí: cada servicio escribe un registro con identidad, operación, fecha y hora, dispositivo, valor anterior y posterior y correlación (SD-05, 5.2.4); T-12 declara RT-05.03 y RT-16.06 en «Sí». La inalterabilidad es parcial: T-12 declara RT-16.07 en «Sí», pero su evidencia es la bitácora de X-01; el SD-05 dice que los registros solo admiten agregar filas, sin precisar cómo se impide que el administrador de la base los modifique. El registro de lecturas de datos sensibles financieros y de cruces está declarado (SD-05 5.2.4; T-12, RT-16.09), sin requerimiento propio en el catálogo. La retención de la auditoría sigue la del dato (SD-05 5.2.4) y el Caso fija los plazos (RT-05.10), que prevalecen sobre el mínimo de cinco años de RT-16.10. La consulta y exportación de la auditoría por el Cliente no se cumplía: T-12 declara RT-16.08 como «No — pendiente».

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
| F:C-01 | Parcial: cada intento de evaluación con identidad y resultado (RF-226); el registro de lecturas lo declaran SD-05 5.2.4 y T-12 (RT-16.09), sin RF propio | Sí | RF propio de registro de lecturas con finalidad (RNF-38, RT-16.09 del Caso) |
| F:C-02 | Parcial: gestión de cobranza con medio, instante y ejecutor (RF-212); el registro de lecturas lo declaran SD-05 5.2.4 y T-12 (RT-16.09), sin RF propio | Sí | RF propio de registro de lecturas y de cambios de saldo (RNF-38) |
| F:C-03 | Sí: versión, instantes, medio y huella (RF-200 a RF-205); custodia WORM con sello encadenado (T-12) | Sí | Nada nuevo; es la referencia de inalterabilidad |
| X-01 | Sí: es su función (RF-165, RF-167); bitácora de solo anexión (T-12, RT-16.07) | Sí | Nada nuevo |
| F:C-04 | No existe | Sí | Incorporarla desde el diseño |

### 4.3 Control de acceso

**Requisitos.** RT-12.05 (control basado en roles, complementado por atributos donde el proceso lo exija, con matriz de segregación de funciones documentada y verificable), RT-11.01 y RNF-73 (Zero Trust: verificación explícita en cada solicitud), RNF-37 (segregación de funciones financieras), RT-16.15 y RT-16.27 (el acceso a documentos y la búsqueda respetan el control de acceso). Caso: RT-12.11 (terminales compartidas, rotación de 62 %, repositores externos).

**¿Se cumplía antes?** Parcial. La identidad centralizada y federada está declarada en «Sí» (T-12, RT-12.01), y el inicio de sesión único y la autenticación multifactor, como parciales (T-12, RT-12.02 y RT-12.03). T-12 declara RT-12.05 en «Sí» y cita una matriz de segregación del dominio financiero en SD-03 3.3.2, pero ni el SD-03 ni el SD-04 contienen esa matriz (búsqueda sin resultados de «segregación» y «matriz de roles»). En la práctica no hay ninguna matriz de roles y permisos, ni para Retail ni para la Filial. Quedan en «No»: ciclo de vida de la identidad (RT-12.09), FIDO2 (RT-12.04) y cuenta de emergencia (RT-12.13). La base tecnológica cubre la identidad en terminales y el personal externo (RF-002 a RF-015).

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
| F:C-01 | Parcial: segregación del vendedor (RF-224), capacitación normativa vigente (RF-007, RF-008); sin matriz de roles | Sí | Matriz verificable entre originación y aprobación (RNF-37) |
| F:C-02 | Parcial: segregación entre modificación y cobranza (RNF-37), capacitación (RF-009) | Sí | Matriz verificable |
| F:C-03 | Parcial: acceso controlado y recuperación (SD-03, 3.3.2) | Sí | Roles de consulta y de reconstrucción del acto |
| X-01 | Parcial: el responsable de cumplimiento mantiene el inventario de interfaces (RF-168); cumplimiento aprueba (SD-03, tabla de gobierno) | Sí | Aprobación dual de interfaces nuevas |
| F:C-04 | No existe | Sí | Acceso del responsable de cumplimiento y de la autoridad fiscalizadora (RT-12.12 del Caso) |

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

**Resultado de la pasada (2026-10-22).** Las Bases exigen estos atributos a la solución, no servicio por servicio. El mínimo queda cubierto con RNF-15 (auditoría), RNF-78 (acceso), RNF-79 (exportación) y RNF-80 (parámetros), que aplican a todos los servicios, más los RF propios donde el Caso o la evidencia lo pedían (abastecimiento, existencias y pedidos, sección 9). Las filas de las tablas 4.2 a 4.5 sin RF propio se dan por cubiertas con esos RNF. La inalterabilidad (RT-16.07) se resuelve con la decisión 7.6, la consulta de la auditoría (RT-16.08) con la consola de administración (decisión 7.3) y las exportaciones grandes y sensibles (RT-16.29 y RT-16.30) con el componente de búsqueda y exportación (decisión 7.3).

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
- **C1.** Los usuarios y roles pertenecen a Entra (base tecnológica). Los parámetros pertenecen a cada servicio. Lo que no tenía dueño era el maestro de tiendas, centros de distribución, líneas de caja, mesones financieros y unidades organizacionales, que además alimenta el control por atributo (sección 4.3). La decisión 7.4 lo reparte: el nodo en existencias, las líneas de caja en ventas, el mesón financiero en originación y las unidades organizacionales en la consola.
- **C2.** Sí: interfaz propia y API.
- **C3.** Sí, una instancia por ámbito. Una consola única con permisos por ámbito mezclaría la administración de ambos negocios.
- **C4.** RT-16.01 y RT-16.03 (con el flujo de 5.2). RT-16.05 es Deseable y no se aborda.
- **Recomendación.** Opción C: consola de administración como componente de la base tecnológica, con cada servicio exponiendo sus parámetros mediante API versionada (opción A para el almacenamiento). El maestro de ubicaciones se reparte entre los servicios dueños de cada nodo, línea de caja y mesón (decisión 7.4, RN-P22), y la consola administra las unidades organizacionales.

### 5.2 Flujos de trabajo y bandeja de tareas (RT-16.11 a RT-16.14)

- **Qué cubre.** Estados, responsables, plazos, escalamiento, delegación, bandeja unificada y motor de reglas.
- **Quién lo necesita.** Aprobación por segundo perfil (RT-16.03), repactación de crédito, sanciones a vendedores de marketplace (RF-122), reasignación de pedidos, inspección de devoluciones y ajustes de inventario (RF-139).
- **C1.** Guarda instancias de flujo y tareas, que son estado de proceso (RT-02.05 manda que viva fuera de los servicios), no datos de negocio.
- **C2.** Sí: componente con estado propio y escala distinta.
- **C3.** Sí, una instancia por ámbito, porque las aprobaciones crediticias no pueden verse desde Retail.
- **C4.** RT-16.11, RT-16.12, RT-16.13 y RT-16.03. RT-16.14 es Deseable y no se aborda.
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
- **Recomendación.** Opción C: capacidad de documentos y firma de la base tecnológica, una por ámbito, reutilizando el prestador de firma ya declarado y el patrón WORM de F:C-03. F:C-03 se mantiene como dueño de la evidencia financiera y los servicios de Retail pasan a usar la capacidad. La capacidad de la Filial es una instancia propia del ámbito, que F:C-03 usa para su evidencia (decisión 7.5).

### 5.4 Notificaciones (RT-16.20 a RT-16.26)

- **Qué cubre.** Tres canales, plantillas administrables y versionadas, preferencias de la persona, envío asíncrono con reintento y registro de entrega, proveedor y costo por canal, baja.
- **Quién lo necesita.** Aviso de cambio de estado del pedido antes del cobro (RF-051), aviso al vendedor de marketplace por una devolución recibida (RF-106; RNF-66), alerta interna de exactitud (RF-162), comunicaciones de cobranza con registro íntegro (RT-16.21 del Caso; RF-213), comunicaciones del crédito con lenguaje claro (RNF-50), y RNF-51 (100 % de las notificaciones definidas, emitidas y registradas).
- **C1.** Registro de envíos, plantillas y preferencias de canal. Si una persona es cliente de ambos negocios, tiene un identificador distinto en cada uno (RF-173), así que sus preferencias son separadas.
- **C2.** Sí: envío asíncrono, reintentos y proveedores externos.
- **C3.** Sí: cobranza y comunicaciones de crédito son del Emisor.
- **C4.** RT-16.20 a RT-16.25, seis filas hoy en «No — pendiente», y RNF-51.
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

Se parte de qué obligaciones regulatorias del emisor ya tienen dueño y cuáles no. Las de la columna «Dueño» tienen servicio y requerimientos en el catálogo; el resto no.

| Obligación del emisor | Fuente | Dueño actual | RF en el catálogo |
| :-- | :-- | :-- | :-- |
| Información precontractual y costo total del crédito | SD-02, Tabla 2.1 | F:C-03 y F:C-01 | Sí (RF-199 a RF-205, RF-217, RF-218) |
| Tasa Máxima Convencional | SD-02, Tabla 2.1 | F:C-01 | Sí (RF-219, RF-220) |
| Consentimiento de repactación | SD-02, Tabla 2.1 | F:C-03 | Sí (RF-207 a RF-209) |
| Cobranza: límites de gastos y comunicaciones | RN-43, RN-44 | F:C-02 | Solo genérico (RF-213); RN-43 y RN-44 sin RF |
| Imputación de pagos | RN-42 | F:C-02 | No |
| Prevención de lavado de activos: debida diligencia y reporte | RN-45; Caso, cap. 12 | Ninguno | No |
| Reportes a la autoridad del mercado financiero | SD-05, 5.2.6; Caso, RT-05.23 | Ninguno | No |
| Gobierno y control interno | Caso, cap. 12 | Ninguno | No; sin detalle en las fuentes |

Las dos obligaciones sin dueño y con compromiso explícito (prevención de lavado y reportes) son las candidatas. La de gobierno y control interno no tiene detalle en las fuentes y queda fuera. Las tres reglas de cartera sin RF (RN-42 a RN-44) se asignan a F:C-02, no a un servicio nuevo.

**Opciones.**

| Opción | Qué incluye |
| :-- | :-- |
| 1 | F:C-04 como servicio con las dos capacidades: prevención de lavado y reportes regulatorios |
| 2 | F:C-04 solo con prevención de lavado; los reportes se generan como capacidad de la analítica del Emisor |
| 3 | Sin servicio nuevo: la prevención se reparte entre F:C-01 y F:C-02 y los reportes los genera F:C-02 |

**Criterios.**

| Criterio | Evidencia | 1 | 2 | 3 |
| :-- | :-- | :-- | :-- | :-- |
| Datos propios y exclusivos (definición de servicio) | Prevención: expediente, alertas y reporte. Reportes: solo calendario, versión y envío; el contenido viene de otras entidades | Cumple, con una parte delgada | Cumple | No cumple |
| Separación de roles | Prevención lo opera el responsable de cumplimiento, con acceso restringido y sin cruce con cobranza ni originación | Cumple | Cumple | Mezcla funciones de cumplimiento con las de originación o cobranza, en contra de la segregación de funciones (RT-12.05) |
| Ámbito | Todo es del Emisor; nada cruza a Retail | Neutral | Neutral | Neutral |
| Acreditación ante el Caso | El Caso evalúa como no acreditada una norma sin control concreto | Control con dueño y RF | Parcial: los reportes quedan sin dueño propio | Control difuso |
| Plazo (Etapa 1) | Originación y primer archivo CMF en la Etapa 1 | Un servicio más en la Etapa 1 | Un servicio más, menor | Sin servicio nuevo |
| Riesgo de alcance | Normativa por verificar | Mayor | Menor | Menor, pero deja huecos |

**Decisión: opción 1** (decisión del usuario del 2026-10-22; falta validarla con la contralora y con la normativa). Razón, con el alcance mínimo de los 13 requerimientos de la ficha: la prevención y los reportes comparten dueño (el responsable de cumplimiento), ámbito y entidades de origen, y separarlos fragmentaría el control. La parte de reportes es delgada, y si el equipo prefiere no abrir un servicio por ella, la opción 2 es la alternativa. La opción 3 mezcla funciones que deben estar separadas y deja la obligación sin control con dueño. Los tres RF de cartera (RN-42 a RN-44) se agregan a F:C-02 como RF-251 a RF-258, también aprobado.

**Pruebas de aceptación sugeridas.** Existencia de expediente por cliente y de un procedimiento de reporte con responsable designado (criterio de RN-45); validación con el Cliente del primer archivo regulatorio antes del paso a producción de la Etapa 1 (SD-05, 5.2.6); prueba de acceso restringido a los roles de cumplimiento.

### 5.8 Cuadro resumen

| Candidato | Recomendación | Tipo | Cierra en el T-12 |
| :-- | :-- | :-- | :-- |
| 5.1 Administración y parámetros | Consola por ámbito; el maestro de ubicaciones se reparte entre los servicios dueños (decisión 7.4) | Base tecnológica | RT-16.01, RT-16.03 |
| 5.2 Flujos y bandeja | Motor de flujos de trabajo por ámbito | Base tecnológica | RT-16.11 a RT-16.13 |
| 5.3 Documentos, plantillas y firma | Capacidad por ámbito reutilizando el patrón de F:C-03 | Base tecnológica | RT-16.15, RT-16.19, RT-16.17 y RT-16.18 en Retail |
| 5.4 Notificaciones | Servicio por ámbito | Base tecnológica | RT-16.20 a RT-16.25 |
| 5.5 Búsqueda y exportación | Índice por ámbito y patrón de exportación asíncrona | Capa de datos y patrón | RT-16.27 a RT-16.30 |
| 5.6 Consulta de auditoría | Módulo de la consola | Base tecnológica | RT-16.08 |
| 5.7 F:C-04 control regulatorio | Servicio nuevo de la Filial con prevención y reportes (opción 1 aprobada), por validar | Servicio de negocio | Obligaciones del Caso, no filas de RT-16 |

**Etapa de los componentes.** Pertenecen a la base tecnológica, que entra en la Etapa 1 (SD-03, Tabla 3.1: «registro oficial desde el mes 16»). El uso de la capacidad de documentos y firma por abastecimiento y posventa empieza con esos servicios, en la Etapa 2.

\1 El bloque «Servicios comunes» de la capa 4 deja de ser un servicio de negocio. Los cuatro componentes de la base tecnológica (consola con consulta de auditoría, flujos, documentos y firma, y notificaciones) y el índice de búsqueda de la capa de datos se dibujan como «Capacidades comunes» de la base tecnológica, una por ámbito, y los cuatro atributos se anotan en cada servicio. Con F:C-04 aprobado, la capa 4 pasa de trece a catorce servicios.

## 6. Integración con la propuesta y con la arquitectura lógica

Este documento no edita nada de `02_Propuesta/`. Lista lo que cambiaría si el equipo aprueba las decisiones de la sección 7.

| Documento | Qué cambiaría | Motivo |
| :-- | :-- | :-- |
| SD-03, 3.3.2 | Agregar F:C-04 si se aprueba (el frente Filial pasa de tres a cuatro servicios; «trece servicios» pasa a catorce en SD-03, línea 98); describir la base tecnológica con sus componentes comunes | Secciones 3.4 y 5 |
| SD-03, 3.2.2 (Tabla 3.1) | Asignar etapa a F:C-04 (Etapa 1) y declarar que los componentes comunes entran en la Etapa 1 con la base tecnológica; respaldar el texto que el T-12 cita como origen de los pendientes | Hallazgo de 4.6 |
| SD-04, Tabla 4.2 (fila R:M-02) | Agregar a «qué no hace» que el ERP/DTE conserva cuentas por pagar y contabilidad, y que abastecimiento es dueño de la orden operativa | Sección 3.1 (abastecimiento) |
| SD-04, Tablas 4.2 y 4.3 y Figura 4.3 | Agregar F:C-04; en la figura, los componentes comunes en la base tecnológica; «los trece códigos» pasa a catorce (SD-04, l.157) | Secciones 3.4 y 5 |
| SD-04, Tabla 4.3 (fila R:M-01) | Cambiar «Por decidir» por el despliegue propuesto en ADR-OC-01: un despliegue con dos módulos | Sección 8 |
| SD-04, Tabla 4.3 (resto) | Agregar los módulos internos de existencias, el despliegue compartido entre comisiones y marketplace con sus condiciones de extracción, y la fila de F:C-04 | Sección 12 |
| SD-04, Tabla 4.6 y ADR | ADR nuevo para los componentes comunes; unificar el bus (ADR-06) y el tenant de la Filial con el diagrama | Sección 4.1 |
| SD-04, línea 304 | Unificar la ubicación de X-01 con las líneas 586 del SD-04 y 298 del SD-03 (en medio) | Registro D-27 |
| SD-05, 5.1.3 y 5.2.4 | Entidades transversales de parámetro, flujo, notificación y documento; mecanismo de inalterabilidad del registro de auditoría | Secciones 4.2 y 5 |
| T-12 | Pasar de «No» a «Parcial» o «Sí» las filas RT-16.01, 16.03, 16.08, 16.11 a 16.13, 16.15, 16.19 a 16.25, 16.27, 16.28 y 16.29 y 16.30, con la nueva referencia (RT-16.05, 16.14 y 16.26 son Deseables y no se abordan); RT-16.07: citar el mecanismo general, no solo X-01 | Sección 4 |
| T-12, RT-12.05 | La evidencia cita una matriz de segregación que no está en el SD-03 ni en el SD-04: declarar la matriz (RNF-78) o bajar la fila a «Parcial» | Sección 4.3 |
| SD-03, Anexo C | Reformular RN-18 como desviación declarada (SP-09); mantener RN-16; agregar RF-239 y RF-288 a RN-P04 | Secciones 8.4 y 9.7 |
| SD-03, Anexo A (supuestos del alcance) | Agregar SP-05 a SP-15 (topes del crédito sin enlace, medios de pago, transportistas, lockers, cobro sin esperar la etiqueta, finanzas abiertas, prevención de lavado y reportes, cobranza, retracto y condiciones de Preproducción) | Sección 9.12 |
| SD-02, anexos (supuestos) | Agregar SUP-28 (valores iniciales de los parámetros de pedidos) y SUP-29 (fórmula y fuentes del costo total de servir), como supuestos metodológicos adicionales del proponente | Sección 9.11 |
| SD-03, 3.4.1 | Declarar la regla de resolución de un pedido no cumplible (RN-P19) y la regla de precedencia de la existencia comprometida (RN-P18), que el texto deja pendientes «antes de habilitar ese recorrido» | Secciones 3.1 y 3.2 |
| T-12, RT-16.07 y RT-16.08 | RT-16.07: citar el sellado y la exportación a almacenamiento inmutable de la auditoría de todos los servicios, no solo la bitácora de X-01. RT-16.08: citar la consola de administración | Decisiones 7.3 y 7.6 |
| SD-05, Anexo A | Agregar la entidad de transferencia (RF-241) y la de línea de caja (RF-293) | Secciones 9.1 y 9.7 |
| Catálogo y Excel (v3.1) | Incorporar los requerimientos y reglas de la sección 9 con su numeración definitiva: RF-232 a RF-297, RNF-77 a RNF-84 y RN-P06 a RN-P24. Cambiar el umbral de RNF-05 y quitar «derivar a tercero» de RF-046 (9.10). Además, agregar RNF-84 (exactitud diaria), dividir RF-213, retirar o reformular RF-028 y revisar RF-022 y RF-023 (ADR-OC-01, 8.4), y corregir las referencias de RF-160 y RF-161. Los RF de atributos de los demás servicios se redactan al aprobar cada uno. Todo cambio al catálogo se tramita como solicitud formal ante el Comité Ejecutivo del contrato (art. 72) | Secciones 4, 5.7, 8.4 y 9 |
| SD-07 y SD-09 | Paquetes de trabajo y pruebas para los cinco componentes comunes y, si se aprueba, F:C-04 | Sección 5 |
| Diagrama lógico (`diagramas-arquitectura-logica/`) | Renombrar «Servicios comunes» a «Capacidades comunes» en la base tecnológica; corregir los nombres de las tarjetas a los vigentes («Evidencia financiera»); agregar F:C-04 si se aprueba; corregir códigos RT (parámetros: RT-16.02 a RT-16.05, no RT-16.01; acceso a datos sensibles: RT-16.09, no RT-16.07) | Secciones 1.1 y 5 |

## 7. Decisiones abiertas

| N.° | Decisión | Opciones | Recomendación de este documento |
| :-- | :-- | :-- | :-- |
| 7.1 | ¿Los cuatro atributos son obligación de todo servicio? | Obligación en cada servicio, o solo requisito de la solución (como en las Bases) | **Aceptada automáticamente (2026-10-22):** obligación en cada servicio mediante RNF-15 y RNF-78 a RNF-80, más RF propios donde el Caso lo pide |
| 7.2 | F:C-04: ¿se crea y con qué alcance? | Opción 1: prevención de lavado y reportes regulatorios; opción 2: solo prevención; opción 3: sin servicio nuevo (sección 5.7) | **Decidido: opción 1**, en Etapa 1, con los 13 requerimientos de la ficha. Falta validar con la contralora y con el texto oficial de la normativa |
| 7.3 | Los cinco componentes comunes: ¿base tecnológica o servicios con código? | Base tecnológica o servicios R/F | **Aceptada automáticamente (2026-10-22):** base tecnológica, una instancia por ámbito. Coherente con la definición de base tecnológica del SD-03 y con el T-12, que remite estos pendientes al diseño de la Etapa 1 |
| 7.4 | ¿Quién es dueño del maestro de tiendas, centros, líneas de caja y unidades organizacionales? | Consola de administración, un servicio nuevo de Retail, o un servicio existente | **Elaborada y aceptada (2026-10-22):** nodos en existencias (RE-26, RF-292), líneas de caja en ventas (RF-293), mesón financiero en originación (RF-294) y unidades organizacionales en la consola de administración (7.3); regla RN-P22 |
| 7.5 | Documentos y firma de la Filial: ¿F:C-03 o una instancia hermana de la capacidad común? | F:C-03 amplía su alcance, o capacidad común por ámbito | **Aceptada automáticamente (2026-10-22):** capacidad común por ámbito; F:C-03 sigue como dueño de la evidencia financiera |
| 7.6 | Inalterabilidad de la auditoría (RT-16.07) frente al administrador de la base | Sellado y exportación a almacenamiento inmutable, u otro mecanismo | **Aceptada automáticamente (2026-10-22):** sellado y exportación a almacenamiento inmutable, el mismo «Registro inalterable» que la capa 7 ya usa para los eventos de seguridad |
| 7.7 | Acceso sin enlace en el nodo local de tienda | Credenciales en caché con caducidad, u otra | **Elaborada y aceptada (2026-10-22):** RN-P23, RF-295, RF-296 y RNF-82 (credenciales sincronizadas con caducidad de 24 horas) |
| 7.8 | Despliegue de R:M-01 oferta comercial | A, un microservicio; B, un despliegue con dos módulos; C, dos microservicios | **Decidido en esta conversación: B.** Ver sección 8 |
| 7.9 | RF-028 (venta al precio nuevo bloqueada hasta confirmar la etiqueta) | A, mantener; B, cobrar el precio propagado (y el menor ante una discrepancia acreditada con la etiqueta, SUP-08) y usar la confirmación solo para registrar y medir | **Decidido en esta conversación: B.** Ver sección 8.4. Pendiente la aprobación formal del cambio al catálogo y de Comercial |
| 7.10 | Reglas RN-42, RN-43 y RN-44 sin RF: ¿se agregan a F:C-02? | Sí, como RF-251 a RF-258, o no | **Decidido: sí**, agregados a F:C-02 (sección 3.4) |
| 7.11 | Merma de existencias: ¿cinco o seis componentes? | Cinco (como el Caso) o seis (con unidad mal ubicada) | **Decidido: seis**, con el criterio de aceptación medido en los cinco del Caso y la sexta informada aparte |
| 7.12 | Regla de precedencia de la existencia comprometida (RF-098) | Sin propuesta vigente | **Elaborada y aceptada (2026-10-22):** nueva regla RN-P18 por estado físico de la unidad, con RF-286 (sección 3.1, existencias) |
| 7.13 | Abastecimiento: etapa de RNF-40 y RNF-53, dueño de las órdenes de compra, proveedor piloto, parámetros de reposición y atributos | Sin decidir o decidir | **Decidido el 2026-10-22** (sección 3.1, abastecimiento) |
| 7.14 | Despliegue de los demás servicios | Mantener la Tabla 4.3 o cambiarla | **Aceptada automáticamente (2026-10-22):** ADR-DP-01 (sección 12) |

**Por verificar en general.** Alcance de la normativa aplicable al emisor (Ley 21.521, propuestas de la autoridad del mercado financiero) con el texto oficial; disponibilidad en Azure Chile Central de los servicios nombrados en 4.1; la numeración de RT del Caso frente a la de las Bases cuando se redacte el T-12.

## 8. ADR-OC-01: despliegue del Servicio de oferta comercial (R:M-01)

Borrador de registro de decisión de arquitectura (RT-02.04). Fecha: 2026-10-22. Estado: decidida por el usuario en esta conversación (opción B); falta la aprobación del equipo y la validación de las condiciones medidas. No modifica el SD-04: lo que cambiaría está en la sección 6.

### 8.1 Contexto

- El SD-04 (Tabla 4.3) deja R:M-01 «por decidir» entre uno o dos microservicios, «por reglas y carga de cambios distintas».
- El SD-03 (3.2.1) ya asigna a R:M-01 dos tareas distintas: corregir el maestro de artículos (causa C1) y crear el motor de precios que hoy no existe (causa C2). Es un solo servicio, con el código R:M-01, dentro de los trece del catálogo (SD-03, 3.3.2). Todo R:M-01 va en la Etapa 1 por la promesa priorizada de precio (SD-03, Tabla 3.1).
- Criterio rector fijado por el usuario: pesan más los criterios que tienen que ver con las cuatro promesas que Ancoa no puede acreditar hoy (SD-02, 2.3.1 a 2.3.4). R:M-01 toca directamente la de precio.

### 8.2 Decisión

**Opción B: un solo despliegue con dos módulos internos, Catálogo y Precios y promociones.**

| Módulo | Contiene | Datos propios |
| :-- | :-- | :-- |
| Catálogo | Atributos obligatorios y su completitud (RF-142, RF-143), reportes de incompletos y de publicaciones fallidas (RF-147, RF-148) | Entidad RE-01 Artículo y sus atributos (SD-05) |
| Precios y promociones | Propagación a cajas, canal digital y exhibición (RF-016 a RF-018), registro de etiquetas (RF-019, RF-020, RF-029), ventanas de cambio (RF-030), precio vigente e historial (RF-021 a RF-024), consulta pública del precio (RF-064), vigencia, canal y tienda de las promociones (RF-032 a RF-034). RF-028 se reformula como registro de la divergencia (8.4) | Entidad RE-02 Precio publicado, versionada, con historial por canal (SD-05) |

Reglas de diseño que forman parte de la decisión:
1. Cada módulo tiene esquema, contrato y eventos propios. Ninguno lee las tablas del otro.
2. El precio es una entidad versionada de primera clase, no un atributo del artículo (SD-02, 2.1: hoy «vive como atributo replicado sin versión»).
3. Precio y promoción se versionan y se publican juntos, por canal y vigencia (SD-04, l.332). Oferta comercial publica la versión. Ventas y pedidos comprueban la elegibilidad y aplican y registran la versión (SD-03, 3.4.2).
4. «Publicable» (RF-143) llega a Precios y promociones como indicador copiado por eventos, no por consulta síncrona al catálogo, para no poner una dependencia en el camino crítico del precio.
5. Las reglas de promoción son parámetros del Cliente. Oferta comercial no decide política de precios (EXC-17).
6. La historia del precio está separada de las proyecciones que consumen los canales. La entidad RE-02 Precio publicado es la autoridad: guarda cada versión, con canal, tienda, vigencia y quién la aprobó, y solo admite agregar versiones. Lo que leen las cajas, el canal digital y el nodo local de tienda (la copia LO-02 de SD-05, l.367) son proyecciones derivadas de esa autoridad y no se usan para reconstruir el pasado. Con esto el precio de una referencia en un canal, una tienda y un instante cualquiera se reconstruye siempre desde la autoridad. Es lo que pide el criterio S5-05 de la rúbrica de cierre del Informe 1.

### 8.3 Condiciones medidas y disparadores de extracción

Si alguna falla, el módulo de Precios y promociones pasa a microservicio propio (opción C). Los umbrales son propuestas, no valores del Caso.

| N.° | Prueba | Umbral | Fuente del umbral |
| :-- | :-- | :-- | :-- |
| 1 | Propagación a las 380 cajas y al canal digital con el escenario de estrés y con catálogo y búsqueda cargados a la vez | 5 minutos como máximo por cambio | RNF-19; RT-05.29 |
| 2 | Aislamiento: el catálogo falla o se degrada | El precio se sigue publicando y consumiendo | RT-02.08 |
| 3 | Recuperación independiente de precios y consulta del historial | Precio publicado de una referencia en fecha, hora y canal arbitrarios, en 1 minuto como máximo, sobre 3 años | RNF-58; RNF-44 |
| 4 | Carga y latencia con el estado de confirmación de etiquetas incluido | Sin degradar las pruebas 1 y 3 | Condición nueva, ver 8.4 |
| 5 | Operación sin enlace por 24 horas y sincronización | Las cajas usan la última versión y se sincronizan al reconectar sin pérdida | RT-03.10; RNF-24 a RNF-27 |
| 6 | Reproducibilidad: consulta del precio por canal, tienda e instante, contra lo cobrado | El precio reconstruido desde la autoridad coincide con el registrado en la transacción en una muestra aleatoria, y la proyección no se usa en la reconstrucción | Rúbrica S5-05; RNF-58; RF-021 |

El escenario de estrés (400.000 cambios en 5 minutos, 1.333 eventos publicados y 6.667 entregados por segundo, 3,2 Mbps) es una hipótesis de Only Simple Solutions. El Caso informa 400.000 cambios en un día de campaña, 10,4 veces el promedio de 38.356 diarios (SD-05, l.761; SD-04, Tabla 4.14; SD-02, 2.3.2). Se repite la medición cuando la Etapa 2 agregue búsqueda vectorial al catálogo.

### 8.4 Tratamiento de RF-028, RF-022 y RF-023 (decisión 7.9, opción B)

Los RF del catálogo atan el cobro a la etiqueta: RF-028 impide vender al precio nuevo mientras el punto de exhibición no confirme; RF-022 toma el precio vigente del último precio propagado a la etiqueta de esa tienda; RF-023 cobra el menor de ambos precios. El SD-03 (3.4.2) pide resolver las diferencias entre etiqueta y caja «sin retardar la propagación obligatoria».

**Decisión.** La caja aplica el precio propagado y no espera la confirmación de la etiqueta. Ante una discrepancia detectada en caja, cobra el menor y registra el incidente (RN-16; RF-023; RF-024; SUP-08). La discrepancia la detecta el cajero o el cliente al contrastar la etiqueta, y la etiqueta de referencia es la última propagada a la tienda (RF-022). La confirmación física de la etiqueta se usa solo para registrar y medir (RF-019, RF-029 y los reportes), no para decidir el cobro.

**Consecuencias propuestas para el catálogo (requieren solicitud formal, art. 72):**
- RF-028: retirarlo o reformularlo como registro de la divergencia, sin bloquear la venta.
- RF-022 y RF-023: mantenerlos como regla de protección al consumidor (cobrar el menor entre el precio exhibido, determinado por el último propagado a la etiqueta, y el del sistema). No requieren un estado de confirmación por etiqueta; basta la versión propagada por tienda. Esta lectura es mía y la debe confirmar Comercial.
- El SD-03 (3.4.2) queda sin cambios. En el Anexo C, RN-18 (prioridad «S»: no vender al precio nuevo mientras la exhibición no esté actualizada) se reformula como desviación declarada (SP-09); RN-16 (cobrar el precio exhibido y, ante discrepancia, el menor) se mantiene y es la que protege al cliente. RS-04 («precio cobrado igual al exhibido, y acreditable por canal e instante») se cumple con el historial de RE-02 y el registro de incidentes.

**Por validar.** La decisión toca el criterio de Comercial y de las jefaturas de tienda (EXC-17; SD-03, 3.4.2). Mientras no se apruebe, el estado de confirmación por etiqueta (el Caso habla de unas 310.000) sigue sin dimensionar, y por eso existe la condición 4.

### 8.5 Alternativas descartadas

| Opción | Por qué se descartó |
| :-- | :-- |
| A. Un solo microservicio sin módulos separados | No separa el precio versionado del catálogo y repite el patrón «atributo replicado sin versión» que el SD-02 identifica como origen del problema |
| C. Dos microservicios desde la Etapa 1 | La carga documentada no exige por sí sola una unidad separada: el escenario de estrés es de 1.333 eventos por segundo. Agrega un servicio más a la Etapa 1 (producción en el mes 16) con su pipeline y operación. Queda como respuesta si fallan las condiciones medidas |

### 8.6 Consecuencias y riesgos

- El módulo compartido sigue siendo una unidad de fallo común. La condición 2 y la separación por esquema reducen el riesgo, y la extracción es posible porque los contratos ya están separados.
- Hay que fijar desde el inicio que los dos módulos no comparten tablas. Si se relaja, la extracción deja de ser barata.
- Separar la autoridad de las proyecciones agrega un mecanismo de actualización de las copias y un riesgo de desfase entre ambas. Ese desfase está acotado por el compromiso de 5 minutos y se mide en la condición 1. La rúbrica pide además no cambiar ese compromiso para resolver SUP-09 (S5-05).
- La decisión sobre RF-028 queda abierta hasta que Comercial la apruebe.

### 8.7 Fuentes

SD-02, 2.1, 2.3.2 y 2.3.7 y anexos (SUP-08 y SUP-09); rúbrica de cierre del Informe 1 (S3-03 y S5-05); SD-03, 3.2.1, 3.2.2 (Tabla 3.1), 3.3.2 y 3.4.2; SD-04, Tabla 4.3, Tabla 4.14 y l.332; SD-05, l.366, l.367 y l.761; Anexo A (EXC-02 y EXC-17); Anexo B (RF citados); Bases RT-02.04, RT-02.08, RT-03.10, RT-05.29.

## 9. Requerimientos y reglas propuestos

Esta sección reúne, en el formato del Anexo B y del Anexo C, los requerimientos y las reglas de negocio que proponen las secciones 3 a 5. Ninguno está en el catálogo ni en el Excel oficial. Los identificadores son correlativos y provisionales: RF desde RF-232, RNF desde RNF-77 y RN-P desde RN-P06. Los RF de los atributos de abastecimiento (RF-272 a RF-279) se agregaron después de los demás y por eso no siguen el orden de las subsecciones. La prioridad usa la escala del catálogo (Alta corresponde a «Must» y Media a «Should») y es una propuesta. Las notas que dicen «Inferido» marcan los requerimientos sin una fuente directa en los documentos revisados. Todo cambio al catálogo requiere una solicitud formal ante el Comité Ejecutivo del contrato (art. 72).

### 9.1 Servicio de abastecimiento (R:M-02), RF-232 a RF-243 y RF-272 a RF-279

Veinte requerimientos. Los doce primeros cubren lo que el catálogo no tenía para órdenes, recepciones, transferencias ni proveedor, y los ocho últimos los atributos transversales y los parámetros de reposición. Derivan de las entidades RE-06 Orden de abastecimiento, RE-07 Proveedor, RE-08 Recepción de mercadería, RE-28 Línea de abastecimiento y RE-29 Línea de recepción del SD-05, y de las reglas RN-P04 y RN-P06 a RN-P11.

| ID | Requerimiento | Código | Servicio | Etapa | Prioridad | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-- |
| RF-232 | El sistema deberá registrar la orden de abastecimiento con su proveedor, su nodo destino, su fecha de emisión y su estado. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P06 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P06)); verbo único. No procede división. Entidad RE-06 (SD-05). |
| RF-233 | El sistema deberá registrar cada línea de la orden de abastecimiento con su artículo y sus unidades solicitadas. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P06 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P06)); verbo único. No procede división. Entidad RE-28 (SD-05). |
| RF-234 | El sistema deberá registrar la recepción de mercadería con su proveedor, su nodo, su fecha y hora y su estado. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P07 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P07)); verbo único. No procede división. Entidad RE-08 (SD-05). |
| RF-235 | El sistema deberá registrar cada línea de recepción con su artículo y sus unidades recibidas. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P07 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P07)); verbo único. No procede división. Entidad RE-29 (SD-05). |
| RF-236 | El sistema deberá permitir vincular la línea de recepción con la línea de la orden de abastecimiento que cumple. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P07 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P07)); verbo único. No procede división. El vínculo es opcional en RE-29 (SD-05). |
| RF-237 | El sistema deberá actualizar el estado de la orden de abastecimiento al registrarse una recepción parcial o total. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P07 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P07)); verbo único. No procede división. Estados de RE-06: emitida, parcialmente recibida, recibida o anulada (SD-05). |
| RF-238 | El sistema deberá informar a existencias cada recepción confirmada como movimiento de inventario. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P08 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P08)); verbo único. No procede división. SD-03, 3.3.2: existencias recibe movimientos de abastecimiento. |
| RF-239 | El sistema deberá registrar la conformidad firmada de quien recibe la mercadería. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P04 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P04)); verbo único. No procede división. RE-08 exige la conformidad firmada; RNF-40; RT-16.14 del Caso. |
| RF-240 | El sistema deberá registrar las unidades que difieren entre las solicitadas y las recibidas. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-P09 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P09)); verbo único. No procede división. Inferido: «error de recepción» es un componente de merma (Caso, decisión 17). |
| RF-241 | El sistema deberá registrar la transferencia entre el centro de distribución y la tienda con su origen, su destino y su estado. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-P10 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P10)); verbo único. No procede división. SD-03, 3.3.2 la nombra; falta la entidad en el SD-05. |
| RF-242 | El sistema deberá permitir al proveedor consultar el estado de sus órdenes de abastecimiento. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-P11 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P11)); verbo único. No procede división. RT-16.30 del Caso: portal del proveedor. |
| RF-243 | El sistema deberá permitir al proveedor consultar las recepciones de su mercadería. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-P11 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P11)); verbo único. No procede división. RT-16.30 del Caso: portal del proveedor. |
| RF-272 | El sistema deberá permitir parametrizar las reglas de la propuesta de reposición. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P17 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P17)); verbo único. No procede división. RT-16.02; contenido de las reglas por definir con la Gerencia de Logística. |
| RF-273 | El sistema deberá registrar cada cambio de una orden de abastecimiento con su usuario o sistema, su instante con zona horaria, su origen y sus valores anterior y posterior. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RT-05.03. |
| RF-274 | El sistema deberá registrar cada cambio de una recepción de mercadería con su usuario o sistema, su instante con zona horaria, su origen y sus valores anterior y posterior. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RT-05.03. |
| RF-275 | El sistema deberá registrar cada cambio de una transferencia con su usuario o sistema, su instante con zona horaria, su origen y sus valores anterior y posterior. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RT-05.03. |
| RF-276 | El sistema deberá limitar el acceso a las órdenes de abastecimiento de un nodo según el rol del usuario. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P13 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P13)); verbo único. No procede división. RT-12.05; rol de planificador de logística (RF-145). |
| RF-277 | El sistema deberá permitir exportar las órdenes de abastecimiento en formato abierto con el filtro aplicado. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-P14 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P14)); verbo único. No procede división. RT-16.28. |
| RF-278 | El sistema deberá permitir exportar las propuestas de reposición en formato abierto con el filtro aplicado. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-P14 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P14)); verbo único. No procede división. RT-16.28. |
| RF-279 | El sistema deberá exigir la aprobación de un segundo perfil para modificar las reglas de la propuesta de reposición. | R:M-02 | Servicio de abastecimiento | 2 | Alta | RN-P15 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P15)); verbo único. No procede división. RT-16.03. |

### 9.2 Servicio de existencias (R:M-03), RF-244 a RF-250

Siete requerimientos de los atributos transversales de existencias, más el RNF-84 (9.8) para la actualización diaria de la exactitud de inventario (RT-05.29 del Caso). La auditoría general la cubre RNF-15.

| ID | Requerimiento | Código | Servicio | Etapa | Prioridad | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-- |
| RF-244 | El sistema deberá registrar cada movimiento de inventario con su usuario o sistema, su instante con zona horaria, su origen y sus valores anterior y posterior. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RT-05.03. |
| RF-245 | El sistema deberá registrar cada reserva de inventario con su usuario o sistema, su instante con zona horaria, su origen y sus valores anterior y posterior. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RT-05.03. |
| RF-246 | El sistema deberá registrar cada ajuste de inventario con su usuario o sistema, su instante con zona horaria, su origen y sus valores anterior y posterior. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RT-05.03. |
| RF-247 | El sistema deberá limitar el acceso a la existencia de una tienda según el rol del usuario. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P13 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P13)); verbo único. No procede división. RT-12.05. |
| RF-248 | El sistema deberá permitir exportar los movimientos de inventario en formato abierto con el filtro aplicado. | R:M-03 | Servicio de existencias | 1 | Media | RN-P14 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P14)); verbo único. No procede división. RT-16.28; retención de 6 años en RNF-45. |
| RF-249 | El sistema deberá permitir exportar los conteos cíclicos en formato abierto con el filtro aplicado. | R:M-03 | Servicio de existencias | 1 | Media | RN-P14 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P14)); verbo único. No procede división. RT-16.28. |
| RF-250 | El sistema deberá exigir la aprobación de un segundo perfil para modificar el colchón de confianza. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P15, RN-09 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P15, RN-09)); verbo único. No procede división. RT-16.03; el registro del cambio ya lo exige RF-151. |

### 9.3 Servicio de cartera de crédito (F:C-02), RF-251 a RF-258

Ocho requerimientos para las reglas RN-42, RN-43 y RN-44 del Anexo C, que no tenían ningún RF. Los tramos, plazos y horarios están por verificar con el texto de la ley (Anexo C).

| ID | Requerimiento | Código | Servicio | Etapa | Prioridad | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-- |
| RF-251 | El sistema deberá imputar cada pago según el orden único definido. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-42 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-42)); verbo único. No procede división. |
| RF-252 | El sistema deberá mostrar al cliente en su estado de cuenta el orden de imputación aplicado a cada pago. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-42 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-42)); verbo único. No procede división. |
| RF-253 | El sistema deberá impedir el cobro de gastos de cobranza extrajudicial antes del plazo de atraso que fija la ley. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-43 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-43)); verbo único. No procede división. Plazo por verificar (art. 37 de la Ley 19.496). |
| RF-254 | El sistema deberá impedir el cobro de gastos de cobranza extrajudicial por sobre el porcentaje máximo del tramo de atraso. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-43 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-43)); verbo único. No procede división. Tramos por verificar. |
| RF-255 | El sistema deberá impedir la comunicación de cobranza fuera de los horarios permitidos. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-44 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-44)); verbo único. No procede división. Horarios por verificar. |
| RF-256 | El sistema deberá impedir la comunicación de cobranza en el lugar de trabajo del deudor. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-44 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-44)); verbo único. No procede división. |
| RF-257 | El sistema deberá impedir la comunicación de cobranza con terceros. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-44 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-44)); verbo único. No procede división. |
| RF-258 | El sistema deberá registrar cada comunicación de cobranza con su horario y su destinatario. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-44 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-44)); verbo único. No procede división. Criterio de aceptación de RN-44. |

### 9.4 Servicio de control regulatorio (F:C-04), RF-259 a RF-271

Trece requerimientos: seis de prevención de lavado de activos (regla RN-45) y siete de reportes regulatorios (regla propuesta RN-P16). El alcance depende de la normativa, por verificar con el texto oficial y con la contralora.

| ID | Requerimiento | Código | Servicio | Etapa | Prioridad | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-- |
| RF-259 | El sistema deberá registrar el expediente de debida diligencia de cada cliente del Emisor en la originación de su crédito. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-45 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-45)); verbo único. No procede división. SD-02, Tabla 2.1: conocimiento del cliente en la originación; Ley 19.913 por verificar. |
| RF-260 | El sistema deberá actualizar el expediente de debida diligencia durante la relación con el cliente. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-45 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-45)); verbo único. No procede división. RN-45: debida diligencia sobre clientes y operaciones. |
| RF-261 | El sistema deberá permitir registrar una operación sospechosa con su responsable designado. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-45 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-45)); verbo único. No procede división. Criterio de RN-45: responsable designado. |
| RF-262 | El sistema deberá permitir al responsable designado reportar la operación sospechosa por el procedimiento de reporte vigente. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-45 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-45)); verbo único. No procede división. Procedimiento por verificar. |
| RF-263 | El sistema deberá restringir el acceso a las operaciones sospechosas registradas a los roles de cumplimiento. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-45 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-45)); verbo único. No procede división. Inferido; confirmar con la normativa. |
| RF-264 | El sistema deberá conservar los antecedentes de prevención de lavado de activos por el plazo que fija la normativa. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-45 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-45)); verbo único. No procede división. RT-05.10 del Caso; SD-05, retención. |
| RF-265 | El sistema deberá mantener el catálogo vigente de archivos regulatorios entregado por el Cliente. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-P16 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P16)); verbo único. No procede división. SD-05, 5.2.6. |
| RF-266 | El sistema deberá mantener el calendario de envío de cada archivo regulatorio. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-P16 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P16)); verbo único. No procede división. SD-05, 5.2.6. |
| RF-267 | El sistema deberá generar cada archivo regulatorio desde las entidades del Emisor. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-P16 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P16)); verbo único. No procede división. SD-05, 5.2.6. |
| RF-268 | El sistema deberá calcular el costo total del crédito en la forma normalizada en cada archivo regulatorio. | F:C-04 | Servicio de control regulatorio | 1 | Alta | RN-P16 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P16)); verbo único. No procede división. SD-05, 5.2.6; RT-05.23 del Caso. |
| RF-269 | El sistema deberá registrar la versión de cada archivo regulatorio generado. | F:C-04 | Servicio de control regulatorio | 1 | Media | RN-P16 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P16)); verbo único. No procede división. Inferido (evidencia de cumplimiento). |
| RF-270 | El sistema deberá registrar la validación de cada archivo regulatorio con el Cliente. | F:C-04 | Servicio de control regulatorio | 1 | Media | RN-P16 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P16)); verbo único. No procede división. SD-05, 5.2.6: el primer archivo se valida antes del paso a producción de la Etapa 1. |
| RF-271 | El sistema deberá registrar el envío de cada archivo regulatorio a la autoridad. | F:C-04 | Servicio de control regulatorio | 1 | Media | RN-P16 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P16)); verbo único. No procede división. Inferido (evidencia de cumplimiento). |

### 9.5 Requerimientos no funcionales, RNF-77 a RNF-80

Un RNF para el plazo de 30 segundos de la disponibilidad publicada, que el T-12 declara en «Sí» (RT-05.29) y que el catálogo no medía, y tres RNF transversales que separan, por la Regla 5, lo que antes se proponía como un solo requisito. La auditoría de cambios ya la cubre RNF-15.

| ID | Requerimiento | Umbral | Método de verificación | Ámbito | Prioridad | Etapa | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-- |
| RNF-77 | La disponibilidad publicada de una referencia debe actualizarse en todos los canales dentro del plazo máximo definido. | 30 s o menos desde la confirmación de la venta con enlace; sin enlace, contados desde la reconexión. | Medición del retraso entre venta confirmada y disponibilidad publicada, en la prueba de carga a 1,5 veces el peak (RT-09.06). | Retail | Alta | 1 | RN-08, RN-09 | RT-05.29 del Caso; SD-04, l.330 (la excepción sin enlace se valida con el Cliente). |
| RNF-78 | El acceso a la información de cada servicio de negocio debe limitarse según el perfil del usuario. | 100 % de los servicios con una matriz de perfiles (roles y atributos) documentada y verificable. | Auditoría de la matriz sobre una muestra de servicios. | Ambos | Alta | 1 y 2 | RN-P13 | RT-12.05. |
| RNF-79 | Todo listado de información de negocio debe poder exportarse en formato abierto con el filtro aplicado. | 100 % de los listados de los servicios. | Prueba por muestreo de exportaciones contra el listado en pantalla. | Ambos | Alta | 1 y 2 | RN-P14 | RT-16.28. |
| RNF-80 | Todo cambio de un parámetro con impacto operacional debe requerir la aprobación de un segundo perfil. | 100 % de los parámetros con impacto operacional. | Auditoría de los cambios de parámetros sobre una muestra. | Ambos | Alta | 1 y 2 | RN-P15 | RT-16.03. |

### 9.6 Reglas de negocio propuestas, RN-P06 a RN-P17

Formato del Anexo C (reglas propuestas por el proponente, derivadas de los requerimientos que las citan). Se validan con el Cliente al inicio del proyecto.

| ID | Regla | Requerimientos | Origen |
| :-- | :-- | :-- | :-- |
| RN-P06 | Toda orden de abastecimiento debe registrar proveedor, nodo destino y las unidades solicitadas por artículo. | RF-232, RF-233 | SD-05, RE-06 y RE-28 |
| RN-P07 | Toda recepción de mercadería debe registrarse por línea, pudiendo vincularse a la orden que cumple y actualizando su estado. | RF-234 a RF-237 | SD-05, RE-08, RE-29 y RE-06 |
| RN-P08 | La mercadería recibida se informa al registro de existencias como movimiento. | RF-238 | SD-03, 3.3.2 |
| RN-P09 | Toda diferencia entre lo solicitado y lo recibido debe quedar registrada. | RF-240 | Caso, cap. 4 y decisión 17 (inferido) |
| RN-P10 | Toda transferencia entre el centro de distribución y las tiendas debe quedar registrada con origen, destino y estado. | RF-241 | SD-03, 3.3.2 |
| RN-P11 | El proveedor debe poder consultar sus órdenes y recepciones. | RF-242, RF-243 | RT-16.30 del Caso |
| RN-P12 | Toda operación que crea, modifica o elimina información de un servicio de negocio debe quedar registrada con quién la ejecutó, cuándo, su origen y los valores anterior y posterior. | RF-244 a RF-246, RF-273 a RF-275, RF-280 a RF-282, RF-297, RNF-15 | Bases, RT-16.06 y RT-05.03 |
| RN-P13 | El acceso a la información de cada servicio debe limitarse por rol y, cuando el proceso lo exija, por atributo, con una matriz de segregación de funciones verificable. | RF-247, RF-276, RF-283, RNF-78 | Bases, RT-12.05 |
| RN-P14 | Todo listado de información de negocio debe poder exportarse en formato abierto con el filtro aplicado. | RF-248, RF-249, RF-277, RF-278, RF-284, RNF-79 | Bases, RT-16.28 |
| RN-P15 | Todo cambio de un parámetro con impacto operacional debe aprobarse por un segundo perfil y quedar registrado con su justificación. | RF-250, RF-279, RF-285, RNF-80 | Bases, RT-16.03 |
| RN-P16 | Todo archivo que la filial deba enviar a la autoridad del mercado financiero debe generarse desde las entidades del Emisor, con el costo total del crédito en la forma normalizada. | RF-265 a RF-271 | SD-05, 5.2.6; RT-05.23 del Caso |
| RN-P17 | Las reglas de la propuesta de reposición deben ser configurables por el Cliente sin desarrollo. | RF-272 | Bases, RT-16.02 y RT-16.04 |

### 9.7 Requerimientos de la pasada de resolución (2026-10-22), RF-280 a RF-296

Requerimientos que la pasada aceptó (los de pedidos ya estaban formulados) o elaboró porque ningún documento cubría el pendiente. Cada uno cita la regla de negocio de la que deriva.

| ID | Requerimiento | Código | Servicio | Etapa | Prioridad | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-- |
| RF-280 | El sistema deberá registrar cada cambio de estado de un pedido con su usuario o sistema, su instante con zona horaria, su origen y sus valores anterior y posterior. | R:V-01 | Servicio de pedidos | 2 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RT-05.03. |
| RF-281 | El sistema deberá registrar cada reasignación de un pedido con su usuario o sistema, su instante con zona horaria, su origen y sus valores anterior y posterior. | R:V-01 | Servicio de pedidos | 2 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06. |
| RF-282 | El sistema deberá registrar cada captura de cobro de un pedido con su usuario o sistema, su instante con zona horaria y su origen. | R:V-01 | Servicio de pedidos | 2 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RNF-65. |
| RF-283 | El sistema deberá limitar la consulta del cliente autenticado a sus propios pedidos. | R:V-01 | Servicio de pedidos | 2 | Alta | RN-P13 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P13)); verbo único. No procede división. RT-12.05. |
| RF-284 | El sistema deberá permitir exportar los pedidos en formato abierto con el filtro aplicado. | R:V-01 | Servicio de pedidos | 2 | Media | RN-P14 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P14)); verbo único. No procede división. RT-16.28. |
| RF-285 | El sistema deberá exigir la aprobación de un segundo perfil para modificar un parámetro del servicio de pedidos. | R:V-01 | Servicio de pedidos | 2 | Alta | RN-P15 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P15)); verbo único. No procede división. RT-16.03; parámetros de RF-058, RF-060 y RF-063. |
| RF-286 | El sistema deberá excluir del disponible para la venta en sala la unidad preparada para un pedido. | R:M-03 | Servicio de existencias | 2 | Alta | RN-P18 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P18)); verbo único. No procede división. Precedencia por estado físico; coherente con RF-044 y RF-098. Etapa 2: «preparada para un pedido» existe cuando pedidos entra en producción. |
| RF-287 | El sistema deberá permitir parametrizar las reglas de atribución de la base de comisión. | R:V-03 | Servicio de comisiones | 2 | Media | RN-54 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-54)); verbo único. No procede división. RT-16.02 y RT-16.04. |
| RF-288 | El sistema deberá registrar la constancia de devolución firmada entregada al cliente. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-P04 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P04)); verbo único. No procede división. RNF-40; RT-16.14 del Caso; capacidad de documentos y firma (decisión 7.5). |
| RF-289 | El sistema deberá registrar la solicitud de retracto de una compra a distancia. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-P21 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P21)); verbo único. No procede división. Caso 16.1, decisión 22; SUP-22. |
| RF-290 | El sistema deberá rechazar la solicitud de retracto presentada fuera del plazo legal. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-P21 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P21)); verbo único. No procede división. Plazo por verificar con el texto de la ley. |
| RF-291 | El sistema deberá registrar la devolución de fondos asociada a un retracto. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-P21 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P21)); verbo único. No procede división. SUP-22; el reingreso de la unidad ya lo cubre RF-190. |
| RF-292 | El sistema deberá permitir dar de alta un nodo tienda por parametrización. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P22 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P22)); verbo único. No procede división. RE-26 Nodo logístico (SD-05); RNF-48; RT-02.12 del Caso. |
| RF-293 | El sistema deberá permitir registrar las líneas de caja de una tienda por parametrización. | R:V-02 | Servicio de ventas | 1 | Alta | RN-P22 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P22)); verbo único. No procede división. RNF-48; RT-02.12 del Caso; falta la entidad en el SD-05. |
| RF-294 | El sistema deberá permitir habilitar el mesón financiero de una tienda por parametrización. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-P22 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P22)); verbo único. No procede división. RT-02.12 del Caso; ámbito de la Filial. |
| RF-295 | El sistema deberá validar el acceso en el nodo local sin enlace con las credenciales sincronizadas por última vez. | — | Base tecnológica | 1 | Alta | RN-P23 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P23)); verbo único. No procede división. RT-03.10; RF-005; caducidad en RNF-82. |
| RF-296 | El sistema deberá invalidar en el nodo local las credenciales revocadas al restablecerse el enlace. | — | Base tecnológica | 1 | Alta | RN-P23 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P23)); verbo único. No procede división. RT-12.10; RF-013. |
| RF-297 | El sistema deberá registrar cada anulación de cobro de un pedido con su usuario o sistema, su instante con zona horaria y su origen. | R:V-01 | Servicio de pedidos | 2 | Alta | RN-P12 | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-P12)); verbo único. No procede división. RT-16.06; RNF-65. |

### 9.8 Requerimientos no funcionales de la pasada, RNF-81 a RNF-84

| ID | Requerimiento | Umbral | Método de verificación | Ámbito | Prioridad | Etapa | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-- | :-: | :-: | :-- | :-- |
| RNF-81 | La bitácora de cruces entre ámbitos debe conservarse por el plazo definido. | 5 años como mínimo, o el plazo mayor que apruebe el Cliente según el dato cruzado. | Auditoría de retención. | Ambos | Alta | 1 | RN-02 | RT-16.10 (en defecto del Caso, no inferior a cinco años); RT-16.09 del Caso. |
| RNF-82 | Las credenciales usadas por el nodo local sin enlace deben caducar dentro del plazo máximo definido. | 24 horas desde su última sincronización. | Ensayo de corte de enlace con credenciales vencidas. | Ambos | Alta | 1 | RN-P23 | RT-03.10 (24 horas de autonomía). |
| RNF-83 | Toda exportación de información sensible debe quedar registrada en la auditoría. | 100 % de las exportaciones de información sensible, con quién exportó qué y cuándo. | Prueba por muestreo de exportaciones contra el registro de auditoría. | Ambos | Alta | 1 y 2 | RN-P24 | RT-16.30 de las Bases; RT-16.09 del Caso. Detectado en la revisión de coherencia. |
| RNF-84 | La exactitud de inventario por categoría debe actualizarse con la frecuencia definida. | 1 vez al día. | Verificación de la fecha de actualización del indicador por categoría. | Retail | Alta | 1 | RN-13 | RT-05.29 del Caso (indicador de exactitud de inventario por categoría, actualización diaria); RF-137 sin cambios. |

### 9.9 Reglas de negocio de la pasada, RN-P18 a RN-P24

| ID | Regla | Requerimientos | Origen |
| :-- | :-- | :-- | :-- |
| RN-P18 | Ante un conflicto de existencia comprometida, prevalece el estado físico de la unidad: la venta en sala prevalece sobre todo compromiso digital aún no preparado; la unidad ya preparada para un pedido sale de la venta en sala y prevalece el pedido; entre dos compromisos digitales prevalece el confirmado primero en la secuencia del registro de existencias. | RF-098, RF-286 | RF-001, RF-038, RF-041, RF-044, RN-48; RT-03.13 del Caso |
| RN-P19 | Ante un pedido no cumplible, primero se reasigna una sola vez dentro de la ventana (RN-23, RF-057); si no es posible, se ofrece al cliente producto equivalente, espera compensada o liberación; el cobro no se captura sin su aceptación explícita. | RF-046, RF-056 a RF-061 | SD-03, 3.4.1; SUP-11; RNF-65 |
| RN-P20 | A igual costo total de servir, se elige el punto con mayor disponible confiable y, si persiste el empate, el centro de distribución antes que una tienda (desempate propuesto por el proponente; SUP-13 solo fija los factores). | RF-077 | SUP-13 |
| RN-P21 | El retracto de una compra a distancia se acepta dentro del plazo legal y se gestiona con un procedimiento común que registra la solicitud, la devolución de fondos y el tratamiento de la unidad. | RF-289 a RF-291, RF-190 | Caso 16.1, decisión 22; SUP-22 |
| RN-P22 | Una tienda nueva se habilita por parametrización con su nodo, sus líneas de caja y su mesón financiero, cada uno en el servicio dueño de su ámbito. | RF-292 a RF-294, RNF-48 | RT-02.12 del Caso |
| RN-P23 | Sin enlace, el nodo local valida el acceso con las credenciales sincronizadas por última vez, que caducan en el plazo definido y se revocan al reconectar. | RF-295, RF-296, RNF-82 | RT-03.10; RT-12.10 |
| RN-P24 | Toda exportación de información sensible debe quedar registrada con quién la hizo, qué exportó y cuándo. | RNF-83 | RT-16.30 de las Bases; RT-16.09 del Caso |

### 9.10 Cambios a requerimientos existentes

| ID | Cambio | Motivo |
| :-- | :-- | :-- |
| RNF-05 | Umbral: tiempo real mediante consulta directa al estado único en R:V-01 (sin desfase). Las plataformas conservadas con copia propia son una desviación declarada de 30 s o menos (SP-15) | Reemplaza «por definir (propuesta: 30 s)». El estado único cumple RT-05.29 del Caso; la desviación la declara el proponente |
| RF-046 | Aclarar «derivar a tercero» como «adquirir a un tercero» | Es la alternativa de la decisión 11 del Caso 16.1; su definición operativa se completa con Logística |
| RNF-15 | Ampliar el texto a «usuario o sistema, instante con zona horaria, origen y valores anterior y posterior» | RT-16.06 exige más que «usuario individual, acción e instante»; RN-P12 |
| RF-213 | Dividir en RF-255 a RF-257 (horario, lugar de trabajo y terceros) | Regla 1 de atomicidad: la conjunción une controles con casos de prueba distintos; RF-213 queda absorbido |
| RF-028 | Retirar o reformular como registro de la divergencia | ADR-OC-01, 8.4 |
| RF-160, RF-161 | Corregir las referencias a RF-158 y RF-159 | Numeración antigua (decisión aprobada en existencias). RF-183 ya cita RF-177 en el catálogo v3.0 y en el Anexo B; la numeración antigua solo está en la hoja de equivalencias del Excel |

### 9.11 Supuestos propuestos (formato del SD-02)

Supuestos del proponente sobre decisiones que se completan en el levantamiento, con el formato de los SUP del SD-02.

| ID | Supuesto | Justificación |
| :-- | :-- | :-- |
| SUP-28 | Se propone fijar los valores iniciales de la ventana de reasignación, la compensación por espera, el umbral de prioridad de preparación y el límite de unidades por cliente con Comercial y Logística durante el levantamiento, y ajustarlos tras el piloto. | El catálogo exige que sean parámetros (RF-058, RF-060, RF-063, RF-180) y el Caso no fija sus valores. |
| SUP-29 | Se propone definir al inicio, con Logística y Finanzas, la fórmula del costo total de servir y la fuente de cada uno de sus términos. | RF-076 nombra los términos y el Caso no los cuantifica; la aceptación exige registrar cada término por asignación (Anexo D, resultado 11). |

### 9.12 Supuestos del alcance propuestos, SP-05 a SP-15

El período de consultas al mandante ya cerró (art. 43), así que lo que depende de terceros o de textos oficiales se declara como supuesto y se valida al inicio del proyecto (ficha de alcance del SD-03, sección 3). Formato del Anexo A del SD-03: supuesto, fundamento, qué pasa si no se cumple y quién lo valida y cuándo.

| ID | Supuesto | Fundamento | Si no se cumple | Valida |
| :-- | :-- | :-- | :-- | :-- |
| SP-05 | La Filial fija los topes de monto y de número de operaciones del crédito sin enlace antes de la Etapa 1 y se cargan como parámetros (RF-090, RF-091) | RC-11 (Anexo A); SD-04, 4.1; RN-47 | La compra con tarjeta propia sin enlace se declara no disponible | Filial emisora, al inicio del proyecto |
| SP-06 | Los medios de pago externos admiten preautorizar sin capturar, con una vigencia compatible con el tiempo de preparación del pedido | RF-043, RF-045 y RF-050 (conciliación de preautorizaciones vencidas) | Se desactiva el medio en pedidos de riesgo (RF-181) o se avisa la indisponibilidad antes de cobrar (RT-16.21 del Caso) | Comercial y Finanzas con los proveedores de medios de pago, en el primer semestre |
| SP-07 | Una parte de los transportistas de última milla admite intercambio electrónico (EPCIS) y el resto usa el portal; el proponente elige un transportista piloto al inicio | SD-05, 5.2.6; RNF-54 | Se usa el portal con todos los transportistas | Logística, antes del desarrollo de la Etapa 2 |
| SP-08 | El controlador de lockers del fabricante expone una interfaz, por API o eventos, que confirma el bulto cargado y la puerta cerrada | SD-13, innovación de lockers | No se habilita la innovación y se mantiene el retiro en tienda | Ancoa, en la selección del proveedor de la innovación |
| SP-09 | Comercial y las jefaturas de tienda aceptan que la caja aplique el precio propagado sin esperar la confirmación de la etiqueta y cobre el menor ante una discrepancia acreditada | ADR-OC-01, 8.4; SUP-08; SD-03, 3.4.2; EXC-17 | Se mantiene RF-028 y se dimensiona su carga antes de decidir el despliegue (condición 4 del ADR) | Comercial y jefaturas de tienda, y el Comité por el art. 72, al inicio del proyecto |
| SP-10 | Las finanzas abiertas están dentro del alcance de la Filial, porque se supone que el emisor pertenece al primer grupo regulatorio | Registro de decisiones D-20 y D-21 (NCG 514 y 569); la Ley 21.521 (art. 18) y el Anexo Técnico N.° 3 no se consultaron en su texto oficial | El producto de finanzas abiertas sale del alcance por solicitud de cambio | Filial emisora y su asesoría jurídica, al inicio del proyecto |
| SP-11 | La Filial está sujeta a debida diligencia y reporte de operaciones sospechosas (Ley 19.913) y a los archivos regulatorios que fije la autoridad; el Cliente entrega el catálogo vigente de archivos y su calendario al inicio | RN-45; Caso, cap. 12; SD-05, 5.2.6 | Se ajusta el alcance de F:C-04 por solicitud de cambio | Contralora y jefa de cumplimiento, al inicio del proyecto |
| SP-12 | Los tramos, plazos y horarios de la cobranza son los de la ley vigente y el Cliente los entrega al inicio para cargarlos como parámetros (RF-253 a RF-256) | RN-43 y RN-44 (por verificar en el Anexo C); art. 37 de la Ley 19.496 | Se actualiza el parámetro sin desarrollo | Filial emisora y su asesoría jurídica, al inicio del proyecto |
| SP-13 | El plazo legal del retracto es el de la ley vigente y se carga como parámetro (RF-290) | Caso 16.1, decisión 22; SUP-22 | Se actualiza el parámetro sin desarrollo | Asesoría jurídica de Retail, al inicio del proyecto |
| SP-15 | Las plataformas conservadas que guardan una copia del estado del pedido (comercio electrónico y marketplace) lo muestran con un desfase de 30 s o menos respecto del estado único de R:V-01. Es una desviación del «tiempo real» de RT-05.29 del Caso, declarada por el proponente | RT-05.29 del Caso; SD-05, Tabla 5.6 (estado único); RNF-04 (0 % de discrepancias); EXC-15 (esas plataformas se conservan) | Se exige a esas plataformas consultar el estado único, o se reemplaza su copia por solicitud de cambio | Contraparte Técnica del Cliente, al inicio del proyecto |
| SP-14 | Las seis condiciones del ADR-OC-01 se miden en Preproducción con el escenario de estrés de Only Simple Solutions, y si alguna falla, Precios y promociones pasa a microservicio propio | ADR-OC-01, 8.3; T-12, RT-09.06 | Se aplica la extracción a microservicio antes de la producción de la Etapa 1 | Proponente y Contraparte Técnica, antes del mes 16 |

## 10. Resultado de la pasada de resolución (2026-10-22)

Para cada pendiente se comprobó primero si las Bases o el Caso lo exigen, luego si otro documento ya lo cumple, y solo entonces se aceptó la propuesta existente o se elaboró una nueva con el formato del documento destino. «Supuesto» marca lo que depende de información que no está en los documentos (normativa oficial, terceros o datos del Cliente) y que no se puede consultar, porque el período de consultas cerró; se declara en la sección 9.12 y se valida al inicio del proyecto.

| Servicio o sección | Pendiente | Resultado | Dónde |
| :-- | :-- | :-- | :-- |
| R:M-01 | Condiciones del ADR-OC-01 | Supuesto SP-14 | 9.12 |
| R:M-01 | Aprobación de RF-028, RF-022 y RF-023 | Supuesto SP-09 | 9.12 |
| R:M-02 | Contrato con el WMS | Ya se cumple (SD-07, EDT 1.2) | Ficha |
| R:M-02 | Concepción | Aceptada automáticamente | Ficha |
| R:M-02 | Línea base de reposición | Fuera del mínimo | Ficha |
| R:M-03 | Regla de precedencia | Elaborada y aceptada (RN-P18, RF-286) | 9.7, 9.9 |
| R:M-03 | Modelos, cifras y despliegue interno | Planificado | Ficha |
| R:V-01 | RNF-05 frente a «tiempo real» | Aceptada automáticamente; desviación declarada en SP-15 | 9.10, 9.12 |
| R:V-01 | Regla de resolución | Elaborada y aceptada (RN-P19) | 9.9, 9.10 |
| R:V-01 | Valores de parámetros y costo total | Elaborada y aceptada (SUP-28, SUP-29, RN-P20) | 9.9, 9.11 |
| R:V-01 | Atributos transversales | Aceptada automáticamente (RF-280 a RF-285 y RF-297) | 9.7 |
| R:V-01 | Medios de pago, transportistas y lockers | Supuestos SP-06, SP-07 y SP-08 | 9.12 |
| R:V-01 | Concepción y cifras de carga | Ya se cumple | Ficha |
| R:V-01 | Ruta de publicación | Aceptada automáticamente | Ficha |
| R:V-02 | Cupo preaprobado sin enlace | Ya declarado (SD-04, 4.1; RC-11); topes como supuesto SP-05 | 9.12 |
| R:V-03 | Completitud y reglas de atribución | Fuera del mínimo; elaborada RF-287 | 9.7 |
| R:V-04 | Flujo de sanciones | Aceptada automáticamente (decisión 7.3) | Ficha |
| R:CL-01 | Firma de la constancia de devolución | Elaborada y aceptada (RF-288) | 9.7 |
| R:CL-01 | Derecho a retracto | Elaborada y aceptada (RN-P21, RF-289 a RF-291); plazo legal como supuesto SP-13 | 9.7, 9.9, 9.12 |
| R:CL-02 | RF-227 a RF-231 en el Excel | Aceptada automáticamente | Sección 6 |
| F:C-01 | Ley 21.521 y Anexo Técnico N.° 3 | Supuesto SP-10 | 9.12 |
| F:C-02 | Tramos, plazos y horarios de cobranza | Supuesto SP-12 | 9.12 |
| F:C-03 | Firma de los actos de Retail | Elaborada y aceptada (decisión 7.5) | Ficha |
| F:C-04 | Alcance normativo | Supuesto SP-11 | 9.12 |
| X-01 | Contradicción del SD-04 | Aceptada automáticamente | Sección 6 |
| X-01 | Retención de la bitácora | Elaborada y aceptada (RNF-81) | 9.8 |
| Sección 4 | Atributos de los servicios sin RF propio | Ya se cumple con RNF-15 y RNF-78 a RNF-80 | 4.6 |
| 7.1 | Atributos como obligación de cada servicio | Aceptada automáticamente | 7 |
| 7.3 | Componentes comunes | Aceptada automáticamente | 7 |
| 7.4 | Dueño del maestro de ubicaciones | Elaborada y aceptada (RN-P22, RF-292 a RF-294) | 9.7, 9.9 |
| 7.5 | Documentos y firma | Aceptada automáticamente | 7 |
| 7.6 | Inalterabilidad de la auditoría | Aceptada automáticamente | 7 |
| 7.7 | Acceso sin enlace | Elaborada y aceptada (RN-P23, RF-295, RF-296, RNF-82) | 9.7 a 9.9 |

Para revisión del usuario: lo marcado «Elaborada y aceptada», porque es contenido nuevo, y los supuestos SP-05 a SP-15, porque son los que el proyecto deberá validar al inicio.

## 11. Revisión de coherencia (2026-10-22)

### 11.1 Método

Cuatro pasadas: (1) comprobaciones mecánicas sobre el documento (cada requerimiento cita una regla que existe, cada regla lista los requerimientos que la citan, la etapa de cada requerimiento coincide con la de su servicio, las secciones citadas existen y ningún RF, RNF o RN citado falta); (2) búsqueda de textos desactualizados tras las decisiones de la conversación; (3) contraste del mínimo que exigen las Bases Transversales (capítulo 16); y (4) segunda lectura independiente del agente `revisor-hilo-logico`, que contrastó el documento con los subdocumentos, el T-12, los anexos, las Bases y el Caso. Lo que el agente señaló se verificó contra la fuente antes de corregirlo.

### 11.2 Hallazgos corregidos

| N.° | Hallazgo | Corrección |
| :-- | :-- | :-- |
| 1 | Las reglas RN-P12 a RN-P15 no listaban los RF de pedidos y RN-P17 listaba un RF que deriva de RN-P15 | Tabla de 9.6 corregida |
| 2 | Textos de la sección 5 y del árbol de la sección 1 seguían diciendo «por decidir» o «candidato» sobre decisiones ya tomadas | Reescritos |
| 3 | La ficha de posventa no mencionaba sus cuatro requerimientos propuestos | Corregida |
| 4 | Brecha del mínimo: RT-16.30 no tenía cobertura | RN-P24 y RNF-83 |
| 5 | RNF-05 se presentaba como «coherente con» fuentes que dicen «tiempo real», y el 30 s rebajaba el Caso | Umbral en tiempo real con el estado único; el 30 s de las plataformas conservadas es una desviación declarada (SP-15) |
| 6 | La decisión de cobrar el precio propagado no mencionaba RN-16, RN-18 ni RS-04 y afirmaba «el SD-03 queda sin cambios» | 8.4 corregida: RN-16 se mantiene, RN-18 se reformula como desviación (SP-09) y se agrega a la sección 6 |
| 7 | «Sí» se usaba con dos sentidos (evidencia vigente y requerimiento propuesto) | Se separa «Sí» de «Propuesto» (sección 0 y 11.4); RT-16.17 pasa a «Parcial» |
| 8 | La cifra de F:C-04 en la tabla maestra decía 10 y son 13 | Corregida |
| 9 | Contradicciones sobre los RT Deseables en las secciones 5, 6 y 11 | RT-16.05, 16.14 y 16.26 quedan fuera del mínimo en todo el documento; «siete filas» pasa a «seis» |
| 10 | RNF-15 no exige origen, zona horaria ni valores anterior y posterior, que pide RT-16.06 | Ampliación de RNF-15 en 9.10 |
| 11 | La evidencia de T-12 para RT-12.05 cita una matriz de segregación que no está en el SD-03 ni en el SD-04 (búsqueda sin resultados) | Se declara que no existe matriz; fila nueva en la sección 6 |
| 12 | Atomicidad: RF-282 (captura y anulación), RF-285 (dos grupos de parámetros), RNF-80 (dos verbos), RNF-78 (rol y atributo), RF-236 («deberá vincular» frente a un vínculo opcional) y RF-137 (umbral dentro de un RF) | RF-282 y RF-297 separados; RF-285 y RNF-80 con un solo objeto y verbo; RNF-78 por perfil; RF-236 «permitir vincular»; la frecuencia diaria pasa al RNF-84 |
| 13 | RF-255 se solapaba con RF-213, que ya exigía impedir cobranza fuera de horario y medio de contacto | RF-213 se divide en RF-255 a RF-257 (9.10) |
| 14 | RF-290 (rechazo fuera de plazo) no derivaba de RN-P21 | RN-P21 incluye el plazo legal |
| 15 | RF-286 estaba en Etapa 1 y usa «unidad preparada para un pedido», que existe con pedidos (Etapa 2) | Etapa 2 |
| 16 | RN-P18 citaba «RT-03.13» sin aclarar que el contenido es el del Caso | «del Caso»; nota de la sección 0 ampliada a RT-03.13, RT-05.10, RT-05.23, RT-05.29 y RT-09.01 |
| 17 | Los componentes comunes y RNF-40 quedaban sin etapa | Entran en la Etapa 1 con la base tecnológica (SD-03, Tabla 3.1); RNF-40 se mantiene en Etapa 1 y se verifica en Retail en la Etapa 2 |
| 18 | F:C-04: decía que no existe en el SD-04 (el SD-04 l.103 nombra el «reporte regulatorio»); usaba la cuarta prueba de etapa al revés; citaba RNF-37 fuera de su alcance; llamaba «oficial de cumplimiento» a un rol que el Caso llama contralora y jefa de cumplimiento; y escribía «EM-01 a EM-10» | Corregido en la ficha y en 5.7 |
| 19 | La sección 4.2 decía a la vez que el registro de lecturas «está cubierto» y que «falta» | Reconciliado: está declarado (SD-05 5.2.4; T-12) y falta un RF propio; se aclara que el Caso fija los plazos de retención |
| 20 | RF-046 «derivar a tercero» se proponía quitar, pero el Caso 16.1 decisión 11 incluye «adquirir a un tercero» | Se mantiene y se aclara su redacción (9.10) |
| 22 | La tabla de módulos de 8.2 ponía la consulta pública del precio (RF-064) en Catálogo y omitía RF-028 | RF-064 pasa a Precios y promociones y se anota RF-028 |
| 21 | Referencias: RF-183 ya cita RF-177 en el catálogo; el cupo sin enlace se atribuía a SP-03, que trata de otra cosa; SP-05 no citaba RC-11; SUP-28 y SUP-29 se llamaban «metodológicos»; «SD-04, l.155» era l.157; «evento de junio de 2027» era inferido; RN-P19 omitía «una sola vez»; RN-P20 citaba SUP-13 por un desempate que no dice; la búsqueda figuraba como componente de la base y de la capa de datos | Todo corregido |

Las comprobaciones mecánicas no encontraron etapas distintas entre un requerimiento y su servicio (salvo RF-286, ya declarado), ni requerimientos, reglas o secciones inexistentes.

### 11.3 Hallazgos abiertos

| N.° | Hallazgo | Qué falta |
| :-- | :-- | :-- |
| 1 | Los componentes comunes están decididos (decisión 7.3) pero el SD-04 no los describe y no tienen requerimientos propios; el T-12 solo puede pasar a «Parcial» hasta que lo haga | Describirlos en el SD-04 al aplicar los cambios de la sección 6 |
| 2 | RT-16.05, RT-16.14 y RT-16.26 son Deseables y no están cubiertos | Decidir si se abordan; no son parte del mínimo |
| 3 | RT-16.33 (estimar y comprometer la reducción de atención asistida) es una obligación del proponente sobre los canales | Tratarla con la capa 1 |
| 4 | RT-12.09 (auditoría del ciclo de vida de la identidad) sigue «No» en el T-12; es de la base tecnológica | Fuera del alcance de este documento |
| 5 | El SD-04 sigue con Event Hubs (l.250, l.274, l.314 y ADR-06) y «trece servicios»; el ADR-06 descartó Service Bus por el historial de reconstrucción, razón que este documento responde con la autoridad RE-02 | Aplicar la sección 6 y reescribir el ADR-06 |
| 6 | Cinco requerimientos marcados «Inferido» (RF-240, RF-263, RF-269, RF-271 y la regla RN-P09) | Decide el usuario |
| 7 | Las fichas de ventas, comisiones, marketplace, clientes Retail, originación, evidencia financiera y X-01 se revisaron solo en sus pendientes | Pasada de revisión por servicio |
| 8 | Las reglas elaboradas (RN-P18, RN-P19, RN-P21) y los supuestos SP-05 a SP-15 no han sido validados fuera del equipo; RN-P18 extiende RF-001 de la reserva temporal a todo compromiso digital aún no preparado, y depende de RN-P19 para no cobrar al cliente | Validar al inicio del proyecto |
| 9 | RN-P12 a RN-P15 y RN-P24 reformulan RT de las Bases, no reglas del Caso; se escribieron después para dar origen a sus RF | Confirmar al incorporarlas que el Anexo C admite reglas derivadas de las Bases |
| 10 | La matriz de roles no existe (hallazgo 11 de 11.2): RNF-78 la exige, pero nadie la ha redactado | Redactarla en el diseño de la Etapa 1 |

### 11.4 Cobertura del mínimo de las Bases Transversales, capítulo 16

Estados: «Sí» cuando el T-12 ya lo declara con evidencia vigente; «Propuesto» cuando solo lo cubre un requerimiento o decisión de este documento; «Parcial» cuando el componente está decidido pero falta describirlo en el SD-04 o la evidencia es incompleta; «Fuera del mínimo» cuando el requisito es Deseable y no está cubierto; «Pendiente» cuando no es de la capa 4.

| RT | Carácter | T-12 antes | Cubierto por | Estado propuesto |
| :-- | :-- | :-: | :-- | :-: |
| RT-16.01 | Obligatorio | No | Consola de administración (5.1, decisión 7.3) | Parcial |
| RT-16.02 | Obligatorio | Sí | T-12 ya lo declara; RNF-80 para el cambio | Sí |
| RT-16.03 | Obligatorio | No | RNF-80, RN-P15, RF-250, RF-279, RF-285 | Propuesto |
| RT-16.04 | Obligatorio | Sí | T-12 ya lo declara (catálogo atómico) | Sí |
| RT-16.05 | Deseable | No | Sin cobertura; es Deseable | Fuera del mínimo |
| RT-16.06 | Obligatorio | Sí | RNF-15 (con la ampliación de 9.10), RN-P12, RF-244 a RF-246, RF-273 a RF-275, RF-280 a RF-282, RF-297; los servicios sin RF propio quedan por RNF-15 | Propuesto |
| RT-16.07 | Obligatorio | Sí | Sellado y exportación a almacenamiento inmutable (decisión 7.6) | Parcial |
| RT-16.08 | Obligatorio | No | Módulo de consulta de auditoría de la consola (5.6) | Parcial |
| RT-16.09 | Según caso | Sí | T-12 ya lo declara (X-01); RNF-38 para la Filial | Sí |
| RT-16.10 | Según caso | Sí | T-12 ya lo declara; el Caso fija los plazos (RT-05.10); RNF-81 para la bitácora de cruces | Sí |
| RT-16.11 | Obligatorio | No | Motor de flujos y bandeja (5.2, decisión 7.3) | Parcial |
| RT-16.12 | Obligatorio | No | Motor de flujos y bandeja (5.2) | Parcial |
| RT-16.13 | Obligatorio | No | Motor de flujos y bandeja (5.2) | Parcial |
| RT-16.14 | Deseable | No | Motor de reglas: sin cobertura; es Deseable | Fuera del mínimo |
| RT-16.15 | Obligatorio | No | Documentos y firma (5.3, decisión 7.5) | Parcial |
| RT-16.16 | Obligatorio | Sí | T-12 ya lo declara (F:C-03) | Sí |
| RT-16.17 | Según caso | Sí | T-12 ya lo declara para la Filial (F:C-03); la parte de Retail (RF-239, RF-288) depende de 5.3 | Parcial |
| RT-16.18 | Según caso | Sí | T-12 ya lo declara (F:C-03) | Sí |
| RT-16.19 | Obligatorio | No | Documentos y plantillas (5.3) | Parcial |
| RT-16.20 | Obligatorio | No | Notificaciones (5.4, decisión 7.3) | Parcial |
| RT-16.21 | Obligatorio | No | Notificaciones (5.4) | Parcial |
| RT-16.22 | Obligatorio | No | Notificaciones (5.4) | Parcial |
| RT-16.23 | Obligatorio | No | Notificaciones (5.4) | Parcial |
| RT-16.24 | Obligatorio | No | Notificaciones (5.4) | Parcial |
| RT-16.25 | Obligatorio | No | Notificaciones (5.4) | Parcial |
| RT-16.26 | Deseable | No | Sin cobertura; es Deseable | Fuera del mínimo |
| RT-16.27 | Obligatorio | Parcial | Índice de búsqueda de la capa de datos (5.5) | Parcial |
| RT-16.28 | Obligatorio | No | RNF-79, RN-P14, RF-248, RF-249, RF-277, RF-278, RF-284 | Propuesto |
| RT-16.29 | Obligatorio | No | Exportación asíncrona (5.5) | Parcial |
| RT-16.30 | Obligatorio | No | RNF-83, RN-P24 (brecha detectada en esta revisión) | Propuesto |
| RT-16.31 | Según caso | Sí | T-12 ya lo declara (canal digital); fuera de la capa 4 | Sí |
| RT-16.32 | Obligatorio | Sí | T-12 ya lo declara (canal digital); fuera de la capa 4 | Sí |
| RT-16.33 | Obligatorio | No | Obligación del proponente sobre autoatención; fuera de la capa 4, sin cobertura aquí | Pendiente |
| RT-16.34 | Obligatorio | Sí | T-12 ya lo declara (borde); fuera de la capa 4 | Sí |

De los 26 requisitos obligatorios del capítulo, 5 quedan en «Sí», 4 en «Propuesto», 16 en «Parcial» y 1 en «Pendiente» (RT-16.33). Antes de este documento, el T-12 declaraba «No» en 18 de los 26 obligatorios, «Parcial» en uno y «Sí» en siete. Ningún «Propuesto» ni «Parcial» pasa a «Sí» hasta que el SD-04 o un anexo lo describa.

## 12. ADR-DP-01: despliegue de los servicios de la capa 4 (2026-10-22)

Registro de decisión (RT-02.04), aceptado automáticamente por ser coherente con el SD-04 y con las decisiones de este documento. No modifica el SD-04: lo que cambiaría está en la sección 6.

### 12.1 Contexto y criterio

El SD-04 define el criterio: una unidad se separa como microservicio cuando tiene autoridad de datos clara y necesita evolucionar, escalar o recuperarse de forma independiente (l.165). Su Tabla 4.3 asigna un despliegue candidato a cada servicio y su ADR-05 deja la partición condicionada a prueba de carga, fallas aisladas y costo de operación. Todos los servicios de Retail corren en el clúster AKS de Retail (Tabla 4.13, l.666) y los de la Filial en el suyo. Este registro contrasta cada servicio con ese criterio y con las cifras del SD-04 (Tabla 4.14). Como en el ADR-OC-01, pesan más los criterios ligados a las cuatro promesas que Ancoa no puede acreditar hoy (SD-02, 2.3).

### 12.2 Decisión

La tabla usa los mismos valores de despliegue que la tabla maestra. Tres precisiones: la oferta comercial y las existencias son un solo despliegue con módulos internos, cada uno con esquema, contrato y eventos propios; comisiones y marketplace comparten un despliegue entre ellos y con nadie más, para no exponer ventas ni pedidos (el SD-04 aísla ventas, existencias y crédito, l.165); y la condición de revisión dice qué medición obligaría a extraer un módulo.

| Código | SD-04 | Decisión | Razón principal | Condición de revisión |
| :-- | :-- | :-- | :-- | :-- |
| R:M-01 | Por decidir | Módulo | Promesa de precio; ver ADR-OC-01 | Las seis condiciones del ADR-OC-01 (SP-14) |
| R:M-02 | Microservicio | Microservicio | Autoridad propia (RE-06 a RE-08, RE-28, RE-29); su integración con 940 proveedores y el WMS cambia a otro ritmo | Ninguna |
| R:M-03 | Microservicio | Microservicio | Promesa de existencia: la reserva es síncrona y no admite doble compromiso | Módulos internos: núcleo transaccional, publicación de disponibilidad y conteo con merma. La publicación se extrae si RNF-77 (30 s) falla con 693 consultas por segundo |
| R:V-01 | Microservicio | Microservicio | Promesa de entrega; 5,8 pedidos por segundo en la apertura del evento, con escala propia | Ninguna |
| R:V-02 | Microservicio | Microservicio | Registro oficial desde el mes 16 y venta sin enlace; 11,8 documentos por segundo en diciembre | Ninguna |
| R:V-03 | Módulo | Módulo | Sin promesa directa; 3 RF; calcula una base que conserva el ERP/DTE | Se extrae si su cálculo afecta la disponibilidad de marketplace (RNF-02) |
| R:V-04 | Módulo | Módulo | La plataforma de 2022 conserva la operación; el servicio gobierna reglas y coordinación | Se extrae si no cumple RNF-02 (99,5 %, 24x7) o RNF-66 (15 min) en la prueba de carga |
| R:CL-01 | Microservicio | Microservicio | Reglas propias de garantía legal y retracto | Ninguna |
| R:CL-02 | Microservicio | Microservicio | Identidad comercial y frontera con X-01 | Ninguna |
| F:C-01 | Microservicio | Microservicio | Promesa de crédito: evaluación en 8 s y cupo | Ninguna |
| F:C-02 | Microservicio | Microservicio | Migración por olas de 620.000 clientes con saldo | Ninguna |
| F:C-03 | Microservicio | Microservicio | Custodia y retención de la evidencia por el plazo del crédito más 6 años | Ninguna |
| X-01 | Microservicio | Microservicio | Frontera: aplica políticas en ambos extremos con almacén propio | Ninguna |
| F:C-04 | — | Microservicio | Expediente confidencial con roles de cumplimiento; la normativa cambia a su ritmo | Ninguna |

### 12.3 Alternativas descartadas

| Alternativa | Por qué se descartó |
| :-- | :-- |
| Un solo despliegue para todos los servicios | El SD-04 ya la descartó (ADR-05): amplía el radio de falla y obliga a desplegar todo junto |
| Comisiones y marketplace dentro del despliegue de ventas o de pedidos | Expondría la venta y la promesa de entrega a la falla de servicios sin promesa directa |
| Dividir existencias en microservicios | Separar movimientos, reservas y disponible exigiría coordinar transacciones entre servicios y arriesga la promesa de existencia |

### 12.4 Coherencia con los subdocumentos

| Fuente | Qué se contrastó | Resultado |
| :-- | :-- | :-- |
| SD-04, Tabla 4.3 | Despliegue candidato por servicio | Coincide en doce servicios; R:M-01 pasa de «por decidir» a módulo (ADR-OC-01) y F:C-04 es nuevo |
| SD-04, l.165 y ADR-05 | Criterio de separación y partición condicionada | Se aplica el mismo criterio y se fijan las condiciones de revisión |
| SD-04, Tablas 4.13 y 4.14 | Clúster por ámbito y cifras de carga | Las cifras citadas son estimaciones del SD-04; se miden en Preproducción (RT-09.06) |
| SD-03, Tabla 3.1 | Etapa de cada servicio | Comisiones y marketplace comparten despliegue y ambos son Etapa 2 |
