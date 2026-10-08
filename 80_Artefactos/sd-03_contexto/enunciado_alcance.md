# Enunciado del alcance (borrador de trabajo del sd-03)

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

Documento de contexto, no es entregable. Alimenta 3.2 de `sd-03.tex`. Se completa por elementos del enunciado PMBOK 6 (descripción del producto, entregables, criterios de aceptación, exclusiones, restricciones, supuestos). Cada exclusión, restricción y supuesto lleva un ID estable para citarlo desde 3.2, 3.3, 3.4 y el resto de los subdocumentos.

Estado de elementos: objetivos (aprobados, falta el general), exclusiones (borrador), descripción del producto (cerrada en `descripcion_alcance_producto.md`), supuestos (parcial), restricciones (lista fuente, sin redactar), entregables y etapas (asignados en `entregables_alcance.md` y `asignacion_etapas.md`; criterios con umbrales por completar).

## 0. Objetivos

Versión aprobada por el equipo. Falta el objetivo general. El (4) incorpora los marcos normativos (cap. 12 del Caso y sd-02, 2.1).

1. Reemplazar por etapas y con convivencia las tres plataformas que originan el problema, es decir el sistema central de retail (2009), la plataforma de originación y cobranza de crédito (2011) y el POS (2014), asumiendo sus responsabilidades en trece servicios (nueve de Retail, tres del Emisor y uno de frontera entre ambos).
2. Conservar e integrar el ERP/DTE, el marketplace y el WMS principal, y evaluar comercio electrónico y fidelización antes de decidir si se mantienen.
3. Implementar una capa de integración que mantenga las plataformas coherentes entre sí, con reglas explícitas de acuerdo sobre el estado de la información y sin depender de un único sistema que concentre el riesgo de falla.
4. Separar el negocio comercial del financiero y auditar cada cruce de datos en la frontera entre ambos, conforme a los marcos que rigen a cada uno (la Ley 19.496 de protección del consumidor para el retail y la normativa de la Comisión para el Mercado Financiero para el emisor) y a la Ley 21.719 de protección de datos personales, que alcanza a ambos.
5. Retirar la plataforma de crédito actual antes del fin de su soporte en 2029.

Observación: la capa de integración del objetivo 3 incluye el diseño de autoridad por dato y reconciliación (ver `descripcion_alcance_producto.md`, sección 7); el algoritmo concreto es decisión de diseño.

## 1. Exclusiones (EXC)

Regla del Caso, cap. 11: "que algo esté excluido no significa que pueda ignorarse en el diseño". Cada exclusión declara también qué sí se hace y qué dependencia genera.

### 1.1 Declaradas por el mandante (Caso 09, cap. 11 y cap. 10)

| ID | No se hace | Sí se hace (dependencia) | Fuente |
| :--- | :--- | :--- | :--- |
| EXC-01 | Reemplazar el sistema de gestión empresarial (ERP/DTE) ni la emisión de documentos tributarios | Integrarlo como único emisor tributario | Caso cap. 11 (1); cap. 10 n.º 6 |
| EXC-02 | Instalar etiquetas electrónicas en las 22 tiendas | Evaluar, especificar y costear la alternativa frente a otras opciones | Caso cap. 11 (2) |
| EXC-03 | Adquirir dispositivos móviles para el personal de venta | Especificar cuántos y con qué características | Caso cap. 11 (3); cap. 10 n.º 11 |
| EXC-04 | Desarrollar la plataforma de vendedores de marketplace ni operar su logística | Integrarla, medirla y resolver la devolución en tienda | Caso cap. 11 (4) |
| EXC-05 | Gestionar remuneraciones | Calcular la base de comisión cuando la venta nace en un canal y se cumple en otro | Caso cap. 11 (5) |
| EXC-06 | Operar la cobranza judicial | Mantener el expediente trazable de cada cobranza y repactación | Caso cap. 11 (6) |
| EXC-07 | Sustituir a las empresas de transporte de última milla | Integrarlas y trazar el estado del pedido hasta la entrega | Caso cap. 11 (7) |
| EXC-08 | Construir infraestructura (canalizaciones, obras eléctricas, cableado) | Especificarla y costearla; la ejecuta el CLIENTE | Caso cap. 11 (8) |
| EXC-09 | Resolver la relación con los administradores de centros comerciales | Diseñar para que su indisponibilidad no detenga la venta | Caso cap. 11 (9); cap. 10 n.º 5 |
| EXC-10 | Adquirir hardware (cajas, dispositivos de sala, lectores, impresoras de etiqueta, red, equipamiento del CD) | Especificar qué comprar, cuánto y con qué características (Cap. 8 de las Bases Transversales) | Caso cap. 11 (10) |

### 1.2 Derivadas de las Bases Técnicas Transversales

Las Transversales casi no declaran exclusiones; la única explícita:

| ID | No se hace | Sí se hace (dependencia) | Fuente |
| :--- | :--- | :--- | :--- |
| EXC-11 | Atender en la mesa de ayuda los incidentes de aplicaciones del CLIENTE no provistas por el adjudicatario ni los procedimientos propios de su operación | Derivarlos al CLIENTE; la mesa cubre la plataforma y las aplicaciones provistas | Bases Transversales, RT-21 §21.3, nivel 2 |

### 1.3 Derivadas del análisis de actores y plataformas

| ID | No se hace | Sí se hace (dependencia) | Fuente |
| :--- | :--- | :--- | :--- |
| EXC-12 | Reemplazar el marketplace vigente ni el WMS principal | Integrarlos y gobernarlos (R-07, R-04, R-08, R-03) | Análisis de actores; Caso cap. 5 ("se mantiene") |
| EXC-13 | Incorporar el centro de distribución de Concepción al WMS ni instalar componentes en él; se mantiene como está (tercera opción del Caso 16.1 n.º 20) | Evaluar y costear la extensión (1.20c); R-03 lo modela como nodo con confianza declarada y recibe sus existencias. Dependencias en SP-02 | Caso cap. 5, cap. 10 n.º 14 y cap. 16.1 n.º 20 |
| EXC-14 | (Retirada el 2026-10-06; ID conservado para no renumerar) | La novena plataforma son las planillas y listas impresas (Caso cap. 5), que deben desaparecer como sistema de registro; su cobertura está en `descripcion_alcance_producto.md` §4.2 | Decisión del equipo; Caso cap. 5 |
| EXC-15 | Reemplazar el e-commerce 2019 ni la fidelización 2017 | Evaluarlos e integrarlos con pruebas definidas; el reemplazo solo entra por control de cambios si fallan las pruebas | Decisión del equipo; análisis de actores |
| EXC-16 | Abrir tarjetas ni ampliar cupos sin conectividad | La apertura y la ampliación se retoman al reconectar. R-05 recibe y concilia las ventas del POS registradas offline. La compra con cupo ya aprobado se autoriza contra un caché con topes que fija el Emisor (RC-11), sujeta a la prueba de factibilidad; si no pasa, no está disponible. Fundamento: restricciones 2 y 3, RT-16.14, prevención de lavado de activos y restricción 1; detalle en `fundamentacion_credito_sin_conexion.md` | Caso 16.1 n.º 7, RT-03.10 y RT-03.13; restricciones 1 a 3 y 5 |

Resuelto en EXC-16: la fundamentación está en `fundamentacion_credito_sin_conexion.md`, que además contiene la declaración de RT-03.13.

### 1.4 Decididas por el proponente

| ID | No se hace | Sí se hace (dependencia) | Fuente |
| :--- | :--- | :--- | :--- |
| EXC-19 | Proveer ni instalar el equipamiento físico ni ejecutar obras ni contratar enlaces en el centro de datos, las tiendas y los centros de distribución (UPS, generador, climatización, extinción, control de acceso, cámaras, cómputo, almacenamiento y red del centro de datos, gabinetes de tienda, redes de tienda, enlaces de respaldo) | El proponente especifica (cómo y dónde), costea (cuánto), coordina, certifica la conformidad y configura y endurece el software y el firmware; el CLIENTE provee, instala y contrata (RC-02, RC-04). Dependencias en SP-04 | Decisión del equipo; Caso cap. 11; Bases Admin. 14.2; RT-06.06 |
| EXC-17 | Decidir el surtido ni la política de precios de Ancoa (son decisiones comerciales del cliente) | Se rediseñan los procesos operativos que los servicios requieren, por ejemplo el despacho por costo total (Caso 9.5), la frecuencia de cambio de precio en sala y el conteo cíclico | Decisión del equipo; Caso 9.5 y cap. 16 (decisiones 9 y 18) |
| EXC-18 | Migrar ni depurar datos históricos distintos de los exigidos en RT-05.15 | Migrar maestro de artículos, inventario al corte, venta 6 años, cartera completa, pedidos 3 años, padrón deduplicado, vendedores | Decisión del equipo; RT-05.15 |

Nota de EXC-18: la versión sugerida antes era más amplia; RT-05.15 ya exige migrar una lista cerrada de datos, por lo que la exclusión se limita a lo que esa lista no cubre. La estrategia de corte de inventario sigue obligatoria (Caso cap. 13 y RT-05.15).

Fusionada: la exclusión "no cambiar hardware de tiendas salvo el POS" queda cubierta por EXC-10.

## 2. Supuestos (SP)

### SP-01 Brecha del sistema central de retail 2009

Se asume que el sistema central de retail de 2009 no puede sostener la exactitud de inventario y la propagación de precios que exigen los objetivos, por lo que se reemplaza por etapas con convivencia. Se adopta como supuesto del proponente, no como condición pendiente.

Fundamento:
- El Caso lo identifica como "el corazón del problema de inventario" (cap. 5) y deja la decisión al proponente.
- Opera con lote nocturno, descuento de seguridad fijo de 2019 y réplica de precio en minutos; el registro discrepa en 12,4 % y la discrepancia de precio fiscalizada fue 11 %.
- Sus 14 integraciones no tienen documentación completa; nadie conoce el mapa.
- El Caso no entrega un informe técnico de brecha del sistema (el único informe de brecha que menciona es el del centro de datos, de 2024, y aún no se entrega).

Consecuencia: el reemplazo es compromiso firme del alcance. Si el mandante aporta evidencia de que el sistema sostiene los objetivos, el cambio entra por control de cambios.

Verificar antes de cerrar: que el sd-02 documente estas cifras con la misma redacción. Las consultas al mandante no se citan: no tratan este tema y no tuvieron respuesta.

### SP-02 Centro de distribución de Concepción se mantiene como está

Se asume que el centro de Concepción conserva su operación con planillas durante el contrato y que su eventual incorporación al WMS se decide después de la evaluación (entregable 1.20c). Se adopta como decisión del proponente, no como condición pendiente.

Fundamento:
- El Caso admite explícitamente esta opción: "se incorpora al sistema de gestión de almacenes, se le da una solución propia, **o se mantiene como está**" (cap. 16.1 n.º 20).
- La restricción 14 y el cap. 5 piden evaluar y costear la extensión, y dicen que no puede darse por supuesta. Implantarla antes de concluir la evaluación sería decidir sin evaluar.
- Una implantación exige obras, hardware y capacitación de 100 personas con rotación de 62 %. Obras y hardware los ejecuta el CLIENTE (EXC-08, EXC-10), cuyo equipo de TI son 46 personas para nueve plataformas.

Dependencias que genera (regla del cap. 11: lo excluido no se ignora en el diseño):

| Punto débil | Dependencia y tratamiento |
| :-- | :-- |
| La inexactitud de Concepción "entra directamente en el registro nacional de existencia" (Caso 16.1 n.º 20) | R-03 modela Concepción como nodo con margen de confianza declarado; el disponible comprometible que depende de ese nodo se calcula de forma conservadora; el conteo cíclico de Concepción entra en la estrategia de corte (1.29) |
| Las planillas "deben desaparecer como sistema de registro" (Caso cap. 5) | R-03 es el registro nacional de existencias, incluidas las de Concepción. La planilla queda solo como herramienta de ubicación física dentro del centro y deja de ser autoridad del registro de existencias |
| Las existencias de Concepción llegan a R-03 | Carga estructurada con origen identificado; formato y periodicidad `[por definir en el diseño]`; la entrega periódica es responsabilidad del CLIENTE (RC-10) |
| Enlace único de Concepción (Caso cap. 6) | No se interviene. Si cae, el centro sigue con sus planillas y R-03 degrada la confianza del nodo; no afecta la venta en tienda (la restricción 5 se refiere a las tiendas) |
| Concepción no es menor: 9.000 m² y 100 de las 620 personas de los centros (16 %) | No se presenta como marginal. El argumento es la secuencia (evaluar y luego decidir) y la capacidad del cliente |

Si no se cumple:
- Si el CLIENTE no entrega las existencias de Concepción con la periodicidad acordada, R-03 trata el nodo con confianza mínima y la disponibilidad de los pedidos que dependen de él se declara con ese grado.
- Si la evaluación (1.20c) recomienda incorporarlo y el CLIENTE lo aprueba, la implantación entra por solicitud de cambio aprobada por el Comité Ejecutivo (art. 72, límite acumulado de 20 % del valor del contrato), con impacto en alcance, plazo y costo. El contrato base no la cubre.

### SP-03 Información precontractual de la compra a cuotas con cupo vigente

Se asume que la compra a cuotas con un cupo ya aprobado no exige una nueva entrega de información precontractual distinta de la entregada en la apertura, o que, si la exige, puede mostrarse en pantalla y registrarse localmente con su versión sin conexión. El Caso no lo define (cap. 12, protección del consumidor financiero).

Fundamento: la restricción 3 se refiere a la información precontractual antes de la aceptación del crédito; el Caso describe esa entrega en la apertura (4.10), no en cada compra.

Si no se cumple:
- Si la normativa exige acreditar información adicional que no se puede registrar sin conexión, la compra con tarjeta propia sin conexión se limita a las operaciones que no la exijan o queda no disponible (declarado en RT-03.13).
- Si el Emisor decide ampliar la contingencia a nuevas aperturas, entra por solicitud de cambio (art. 72) con evaluación de normativa y de impacto.

### SP-04 Provisión e instalación física a cargo del CLIENTE

Se asume que el CLIENTE provee, instala y contrata todo lo físico de la infraestructura on-premise (obras, equipos y enlaces), y que el proponente es responsable de especificar, costear, coordinar, certificar la conformidad y configurar y endurecer el software y el firmware. Se adopta como decisión del equipo.

Fundamento:
- El Caso (cap. 11) dice que el CLIENTE ejecuta las canalizaciones, las obras eléctricas y el cableado, y que adquiere el hardware; el proponente debe especificar exactamente qué comprar, cuánto y con qué característica.
- RT-06.06 asigna al CLIENTE la obra civil de separación del recinto, y al proponente su especificación y su coordinación.
- Las Bases Administrativas (art. 14.2) admiten que el hardware de terreno lo adquiera el CLIENTE, con especificación del proponente.

Dependencias y puntos débiles:

| Punto | Tratamiento |
| :-- | :-- |
| Bases Admin. 14.1 ("llave en mano") y 14.2 ("provisión... de los componentes on-premise") prevalecen sobre el Caso (art. 5) | Lectura adoptada: el art. 14.2 ya admite que el CLIENTE adquiera hardware; se extiende, por la declaración expresa del Caso, a los equipos del recinto y a los gabinetes. Es una interpretación y se declara como tal |
| RT-06.33: el proponente "proveerá toda la conectividad, la seguridad y las canalizaciones" para cumplir los niveles de servicio | Se cumple en cuanto a responsabilidad por el resultado: el proponente especifica, coordina y certifica que los niveles de servicio se alcanzan; la ejecución de canalizaciones y enlaces es del CLIENTE (Caso cap. 11) |
| RT-08.06: garantía de fábrica "desde la recepción conforme" | Se verifica en el acta de recepción y certificado de conformidad (1.15.23); el proponente gestiona el soporte del fabricante (Transversales 21.3, nivel 4) |
| Disponibilidad de infraestructura del recinto de 99,95 % (Transversales 6.1) | Depende de que el CLIENTE ejecute conforme a la especificación; toda desviación queda en el acta de observaciones |
| El plan de obras y compras del CLIENTE debe calzar con las ventanas libres y con el calendario de las olas del POS | Calendario de obras y compras coordinado por el proponente en el plan de trabajo (sd-07) |

Si no se cumple:
- Si el CLIENTE no entrega obras o equipos en los plazos acordados, los entregables que dependen de ellos se registran como impedimento imputable al CLIENTE y se deja constancia en el acta, sin que ello desplace por sí solo las fechas contractuales del art. 17.
- Si el mandante o la evaluación exigen que el proponente provea e instale, pasa a ejecución del proponente por solicitud de cambio aprobada por el Comité Ejecutivo (art. 72), con impacto en alcance, plazo y costo.

### Otros supuestos (por decidir)
Disponibilidad de datos y accesos de Ancoa, volumetrías marcadas "a estimar" en el Caso (cap. 15), vigencia del soporte del proveedor hasta 2029.

## 2b. Responsabilidades del CLIENTE (RC)

Salen de las exclusiones y de las Bases (patrón de los ejemplos reales de alcance revisados: el hospital, AvePoint y Cashnet separan lo que hace cada parte).

| ID | Responsabilidad del CLIENTE | Fuente |
| :-- | :-- | :-- |
| RC-01 | Entregar el informe interno de 2024 sobre la brecha del centro de datos | Caso cap. 5 y RT-06.01 |
| RC-02 | Adquirir, instalar y poner en servicio el hardware y el equipamiento físico que el proponente especifica: cajas, dispositivos de sala, lectores, impresoras, red, equipamiento de los centros de distribución, y los equipos del centro de datos y de los gabinetes de tienda (EXC-10, EXC-19, SP-04) | Caso cap. 11; Bases Admin. 14.2; RT-06.06 |
| RC-03 | Adquirir los dispositivos móviles para el personal de venta (EXC-03) | Caso cap. 11 y cap. 10 n.º 11 |
| RC-04 | Ejecutar las obras (civil, eléctrica, canalizaciones y cableado) y contratar los enlaces de comunicaciones que el proponente especifica y costea (EXC-08, EXC-19, SP-04) | Caso cap. 11; RT-06.06 |
| RC-05 | Operar la cobranza judicial (EXC-06) y gestionar las remuneraciones (EXC-05) | Caso cap. 11 |
| RC-06 | Resolver la relación con los administradores de centros comerciales y con las empresas de transporte (EXC-07, EXC-09) | Caso cap. 11 |
| RC-07 | Aprobar los cambios al catálogo de 13 servicios mediante el Comité Ejecutivo | Bases Administrativas, art. 72 |
| RC-08 | Validar y firmar las actas de aceptación mediante la Contraparte Técnica | Entregable 2.14; Bases Administrativas |
| RC-09 | Aportar el personal de TI (46 personas) para coordinar, validar y acompañar | Caso, volumetría (cap. 14): el CLIENTE aporta 46 personas para nueve plataformas |
| RC-10 | Operar el centro de distribución de Concepción con sus planillas y entregar sus existencias a R-03 con la periodicidad acordada | SP-02; Caso cap. 16.1 n.º 20 |
| RC-11 | Fijar el apetito de riesgo del crédito sin conexión: tope por transacción, tope acumulado por cliente, antigüedad máxima del caché y criterios de exclusión | `fundamentacion_credito_sin_conexion.md` §6; Caso 16.1 n.º 7 |

Pendiente: contrastar con el Anexo A.4.2 y con SUP-01..27 del sd-02 cuando el usuario los anexe.

Formato de todo supuesto (SP) desde ahora: texto, fundamento y **"Si no se cumple"** (consecuencia sobre alcance, plazo o costo). SP-01 ya lo cumple.

## 3. Restricciones (RS), lista fuente sin redactar

Caso cap. 10: 15 restricciones no negociables (separación de datos, consentimiento acreditable, información precontractual, precio exhibido igual al cobrado, tienda vende sin enlace, ERP único emisor, garantía legal ante la compañía, migración sin pérdida de 620.000 clientes, ventanas de congelamiento, evento anual de fecha incierta, dispositivos compartidos, repositores externos, rotación del personal, Concepción, mapa de 14 integraciones).
Bases Administrativas: despliegue híbrido (art. 16), cronograma de 56 meses (art. 17), cambios sujetos a aprobación (catálogo de 13 servicios).
Bases Transversales: RT obligatorios del T-12 (se responden en T-12, no se copian aquí).
Fin de soporte de la plataforma de crédito y último hito de remediación: 2029.

Pendiente: asignar RS-01..RS-NN, decidir cuáles pasan a 3.2.3 y cuáles solo se citan.

## 4. Ciclo de vida y asignación por etapas

**Ciclo de vida: híbrido** (FEP02, diapositiva 8). Marco predictivo: contrato de suma alzada, dos etapas con marcha blanca, hitos contractuales, catálogo de 13 servicios, cambios por solicitud formal aprobada por el Comité Ejecutivo (Bases Admin. art. 72). Desarrollo adaptativo en iteraciones dentro de cada etapa.

**Criterios de asignación a etapa, en este orden:** (1) Bases, (2) dependencias técnicas, (3) riesgo e hitos externos, (4) capacidad de absorción del cliente, (5) prioridad del comité.

**Resultado:** matriz en `entregables_alcance.md` (columna Etapa) y justificación por ronda en `asignacion_etapas.md`. Resumen: Etapa 1 = plataforma híbrida completa, integraciones críticas, R-01, R-03, R-05, F-01, F-02 (ola 1), F-03, X-01 y el POS en 22 tiendas (piloto de 3 y luego 19); Etapa 2 = R-02, R-04, R-06, R-07, R-08, R-09 y F-02 (ola 2); retiro de la plataforma de 2011 en Operación (objetivo octubre de 2028).
