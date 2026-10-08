# Anexo A del Subdocumento 3. Exclusiones, supuestos, responsabilidades del cliente y restricciones

Fuente del anexo que acompaña al Subdocumento 3 (Esquema de solución y alcance). Se entrega como documento aparte, `OnlySimpleSolutions-Subdocumento3-Anexos`, según el Comunicado 10. El cuerpo del subdocumento (subsección 3.2.3) resume estas listas y remite a este anexo. Los nombres de los servicios son los vigentes en el cuerpo (ver `80_Artefactos/sd-03_contexto/divisiones_negocio_servicios_sd-03.md`). Fecha: 2026-10-07. Estado: borrador por revisar.

Este anexo reúne el detalle de las 18 exclusiones vigentes (diez del cliente, una deducida de las Bases Técnicas Transversales y siete del proponente), los seis supuestos del alcance, las once responsabilidades del cliente y las veinte restricciones. El identificador EXC-14 se conserva sin uso para no renumerar: se retiró al comprobar que la novena plataforma del Caso corresponde a las planillas y listas impresas, que se cubren con servicios.

## A.1 Exclusiones

| ID | No se hace | Sí se hace | Fuente |
| :-- | :-- | :-- | :-- |
| EXC-01 | Reemplazar el sistema de gestión empresarial ni la emisión de documentos tributarios | Integrarlo como único emisor tributario | Caso cap. 11; restricción 6 |
| EXC-02 | Instalar etiquetas electrónicas en las 22 tiendas | Evaluar, especificar y costear la alternativa frente a otras opciones, en un informe de evaluación | Caso cap. 11 |
| EXC-03 | Adquirir dispositivos móviles para el personal de venta | Especificar cuántos y con qué características | Caso cap. 11; restricción 11 |
| EXC-04 | Desarrollar la plataforma de vendedores del marketplace ni operar su logística | Integrarla, medirla y resolver la devolución en tienda, con los servicios de marketplace y de posventa | Caso cap. 11 |
| EXC-05 | Gestionar remuneraciones | Calcular la base de comisión entre canales, con el servicio de comisiones y un conector con el sistema de remuneraciones | Caso cap. 11 |
| EXC-06 | Operar la cobranza judicial | Mantener el expediente trazable de cobranza y repactación, con los servicios de cartera de crédito y de evidencia financiera | Caso cap. 11 |
| EXC-07 | Sustituir a los transportistas de última milla | Integrarlos y trazar el pedido hasta la entrega, con el servicio de pedidos | Caso cap. 11 |
| EXC-08 | Construir obras civiles, eléctricas y de cableado en tiendas y centros de distribución | Especificarlas y costearlas. Las ejecuta el cliente. El proponente provee las canalizaciones y la conectividad del centro de datos on-premise | Caso cap. 11; RT-06.33 |
| EXC-09 | Resolver la relación con los administradores de centros comerciales | Diseñar para que su indisponibilidad no detenga la venta, con 24 horas de operación sin conexión | Caso cap. 11; restricción 5 |
| EXC-10 | Adquirir hardware de tiendas y centros de distribución | Especificar qué comprar, cuánto y con qué características | Caso cap. 11 |
| EXC-11 | Atender en la mesa de ayuda las aplicaciones del cliente no provistas por el proponente | Derivarlas al cliente. La mesa cubre lo provisto | Bases Técnicas Transversales, 21.3, nivel 2 (inferencia del proponente) |
| EXC-12 | Reemplazar el marketplace ni el sistema de almacenes del centro de distribución principal | Integrarlos y gobernarlos, con los servicios de marketplace, existencias y pedidos | Caso cap. 5 («se mantiene») |
| EXC-13 | Incorporar el centro de distribución de Concepción a un sistema de almacenes ni instalar componentes allí | Evaluar y costear la extensión. El servicio de existencias modela a Concepción como un nodo con confianza declarada (SP-02) | Caso cap. 5, restricción 14, núm. 16.1 n.º 20 |
| EXC-15 | Reemplazar el comercio electrónico ni la fidelización | Evaluarlos e integrarlos con pruebas con umbral. El reemplazo solo entra por solicitud de cambio si fallan las pruebas | Caso cap. 5 («se mantiene o se reemplaza, con justificación») |
| EXC-16 | Abrir tarjetas ni ampliar cupos sin conexión | Autorizar la compra con cupo vigente contra un registro local con topes de la filial emisora, sujeta a una prueba de factibilidad | Caso núm. 16.1 n.º 7; RT-03.10 y RT-03.13; restricciones 1 a 3 y 5 |
| EXC-17 | Decidir el surtido ni la política de precios | Rediseñar los procesos operativos que los servicios requieren | Caso 9.5 y cap. 16 (decisiones 9 y 18) |
| EXC-18 | Migrar datos históricos fuera de la lista de RT-05.15 | Migrar la lista exigida y dejar un repositorio de consulta de los datos no migrados | Caso RT-05.15; Bases Técnicas Transversales RT-05.15 |
| EXC-19 | Proveer o instalar equipamiento físico de tiendas y centros de distribución, ejecutar sus obras ni contratar sus enlaces | Especificar, costear, coordinar, certificar y configurar (SP-04) | Caso cap. 11; Bases Administrativas 14.2; RT-06.06 |

## A.2 Supuestos

El Caso pide declarar como supuesto toda decisión que el proponente tomó por el cliente, con su fundamento, su impacto y la instancia que la valida (Caso, núm. 16.1 y 17.1). SP-02 corresponde a la decisión 20 del numeral 16.1. SP-03 se relaciona con las decisiones 6 y 7. SP-01 es una decisión del proponente que el Caso reconoce en su numeral 13.1. SP-04 reparte lo físico entre el proponente y el cliente según las Bases (art. 14.2, RT-06.06 y RT-06.33) y el Caso (cap. 11). SUP-26 y SUP-27 vienen del Subdocumento 2.

| ID | Supuesto | Fundamento | Si no se cumple | Se valida con |
| :-- | :-- | :-- | :-- | :-- |
| SP-01 | El sistema central de 2009 no sostiene los objetivos y se reemplaza por etapas | «Corazón del problema de inventario» (Caso cap. 5), lote nocturno, discrepancia de inventario y de precio, 14 integraciones sin documentar | Si el cliente aporta evidencia en contra, el cambio entra por solicitud de cambio | Comité Ejecutivo, al inicio del proyecto |
| SP-02 | El centro de Concepción se mantiene como está durante el contrato y no es origen de la promesa de entrega digital mientras opere con planillas (equivale al SUP-20 del Subdocumento 2) | Caso núm. 16.1 n.º 20 (tercera opción), restricción 14 | Sin entrega de existencias, el nodo queda con confianza mínima. Si se decide incorporarlo, el cambio entra por el art. 72 de las Bases Administrativas | Contraparte Técnica, al inicio del proyecto |
| SP-03 | La compra a cuotas con cupo vigente no exige nueva información precontractual, o esta se registra sin conexión | La restricción 3 aplica a la apertura (Caso 4.10) | Se limita o queda no disponible, y se declara en RT-03.13 | Filial emisora y su asesoría jurídica, al inicio del proyecto |
| SP-04 | El cliente adquiere, ejecuta y contrata, antes de cada instalación en tienda y centro de distribución, lo físico que el proponente especifica. El proponente provee el centro de datos on-premise con su conectividad, su seguridad y sus canalizaciones | Caso cap. 11; Bases Administrativas 14.2; RT-06.06 y RT-06.33 (Obligatorios), que el proponente cumple para el centro de datos | Si el cliente se retrasa, impedimento registrado. Si el mandante exige que lo haga el proponente en tiendas y centros, cambio por el art. 72 | Contraparte Técnica y Comité Ejecutivo, al inicio del proyecto |
| SUP-26 | El proyecto comienza en enero de 2027 (del Subdocumento 2) | Supuesto de calendario. Los resultados de la licitación se entregan el 01-12-2026 (T-20), el contrato se firma dentro de 10 días hábiles (art. 68) y el Caso congela los sistemas hasta el 6 de enero (13.2). Con inicio en diciembre de 2026 el mes 16 cae en marzo y con inicio en febrero de 2027 cae en mayo, ambos en congelamiento | Se recalculan los meses 16, 21 y 22 y las ventanas de congelamiento, sin cambiar los 56 meses | Contraparte Técnica, en el acta de inicio |
| SUP-27 | Once tiendas se ubican en el entorno de Santiago (del Subdocumento 2) | Supuesto de distribución | Se rehace la selección de las tiendas piloto con la ficha de sitios | Contraparte Técnica, con la ficha de sitios |

## A.3 Responsabilidades del cliente

| ID | Responsabilidad | Fuente |
| :-- | :-- | :-- |
| RC-01 | Entregar el informe interno de 2024 sobre la brecha del centro de datos | Caso cap. 5 y RT-06.01 |
| RC-02 | Adquirir, instalar y poner en servicio el hardware de terreno y los dispositivos operacionales de tiendas y centros de distribución, según lo especificado | Caso cap. 11; SP-04 |
| RC-03 | Adquirir los dispositivos móviles para el personal de venta | Caso cap. 11; restricción 11 |
| RC-04 | Ejecutar la obra civil de separación del centro de datos y las obras y enlaces de tiendas y centros de distribución, especificados y costeados | Caso cap. 11; RT-06.06; SP-04 |
| RC-05 | Operar la cobranza judicial y gestionar las remuneraciones | Caso cap. 11 |
| RC-06 | Mantener la relación con los administradores de centros comerciales y con los transportistas | Caso cap. 11 |
| RC-07 | Aprobar los cambios mediante el Comité Ejecutivo | Bases Administrativas art. 72 |
| RC-08 | Validar y firmar las actas mediante la Contraparte Técnica | Gestión del proyecto |
| RC-09 | Aportar el personal de tecnología (46 personas) para coordinar, validar y acompañar | Caso cap. 2 y cap. 14 |
| RC-10 | Operar Concepción con sus planillas y entregar sus existencias al servicio de existencias | SP-02 |
| RC-11 | Fijar el apetito de riesgo del crédito sin conexión (topes, antigüedad del registro local y exclusiones) | Caso núm. 16.1 n.º 7 |

## A.4 Restricciones

| ID | Restricción | Fuente | Cómo la atiende la solución |
| :-- | :-- | :-- | :-- |
| RS-01 | Separación de datos entre retail y filial emisora definida, implementada, documentada y auditable | Caso restricción 1 | Servicio de control de cruces y segregación de red |
| RS-02 | Ninguna modificación de crédito sin evidencia recuperable del consentimiento | Caso restricción 2 | Servicio de evidencia financiera, con retención por el plazo del crédito más seis años |
| RS-03 | Información precontractual entregada antes de la aceptación y acreditada de forma estructurada | Caso restricción 3 | Servicios de originación de crédito y de evidencia financiera, con un proceso que impide omitirla |
| RS-04 | Precio cobrado igual al exhibido, y acreditable por canal e instante | Caso restricción 4 | Servicios de oferta comercial y de ventas |
| RS-05 | La tienda sigue vendiendo y cobrando sin enlace | Caso restricción 5 | Punto de venta y componente local con 24 horas de autonomía |
| RS-06 | El sistema de gestión empresarial sigue siendo el único emisor tributario | Caso restricción 6 | EXC-01 e integración crítica con el sistema |
| RS-07 | La garantía legal se ejerce ante la compañía | Caso restricción 7 | Servicio de posventa, sin derivaciones |
| RS-08 | La migración de 620.000 clientes sin pérdida, sin interrupción ni divergencia | Caso restricción 8 | Servicio de cartera de crédito, por tramos y con compuerta |
| RS-09 | Prohibido intervenir sistemas en las ventanas de congelamiento | Caso restricción 9; núm. 13.2; RT-10.05 | Pasos a producción en los meses 16 y 21 y despliegues en ventanas libres |
| RS-10 | La fecha del evento anual la fija un tercero, con unas seis semanas de aviso | Caso restricción 10 | Degradación definida en los criterios de aceptación y holgura en el plan de trabajo |
| RS-11 | Sin dispositivo por vendedor (640 terminales para 3.820 personas) | Caso restricción 11 | Aplicaciones en terminal compartida (EXC-03) |
| RS-12 | No se pueden imponer herramientas a los 1.100 repositores externos | Caso restricción 12 | Solo acceso individualizado, con la identidad y gestión de accesos |
| RS-13 | Rotación del 62 % y 1.900 incorporaciones de temporada durante el congelamiento | Caso restricción 13 | Capacitación y certificación |
| RS-14 | Concepción: evaluar y costear, sin dar por supuesta su incorporación | Caso restricción 14 | EXC-13, SP-02 e informe de evaluación |
| RS-15 | El mapa de las 14 integraciones lo levanta el proponente | Caso restricción 15 | Mapa de las catorce integraciones como primera entrega |
| RS-16 | Despliegue híbrido obligatorio | Bases Administrativas art. 16 | Arquitectura del capítulo 4 |
| RS-17 | Cronograma de 56 meses, sin plazos alternativos | Bases Administrativas art. 17 | Reparto de la subsección 3.2.2 |
| RS-18 | Cambios solo por solicitud formal aprobada por el Comité Ejecutivo, con límite de 20 % | Bases Administrativas art. 72 | RC-07 y registro de cambios |
| RS-19 | Fin de soporte de la plataforma de crédito y último hito de remediación en 2029 | Caso núm. 13.2 | Negocio financiero en la Etapa 1 y retiro con fecha objetivo en octubre de 2028 |
| RS-20 | Requisitos técnicos obligatorios de las Bases Técnicas Transversales | Bases Técnicas Transversales | Respuesta uno a uno en el Formulario T-12 |
