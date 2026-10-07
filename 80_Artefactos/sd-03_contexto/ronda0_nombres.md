# Ronda 0: nombres de los entregables

Documento de trabajo. No es entregable. Propuesta pendiente de aprobación; no modifica `entregables_alcance.md` hasta que se apruebe.

Origen: revisión de cuatro ejemplos reales de documentos de alcance (hospital HE-1, AvePoint, Cashnet, CIS). En esos documentos cada entregable se entiende solo con leer su nombre.

## Regla de nombres

1. Sustantivo de un objeto o resultado, nunca una actividad (nada de "Migración de…" ni "Reemplazo de…").
2. El tipo de entregable aparece en el nombre: servicio, plataforma, conector, informe, plan, matriz, manual, acta.
3. Un nombre, un entregable. Si una "y" une dos cosas distintas, se separan.
4. Se entiende sin el código (R-01, F-02).
5. Incluye el ámbito cuando importa: "en las 22 tiendas", "de 620.000 clientes".

Excepción justificada: el plan para la dirección del proyecto (2.3) es un solo entregable que el PMBOK define como integración de planes subsidiarios; sus componentes se verifican uno a uno en el criterio de aceptación.

## 1. Entregables de producto

| Cód. anterior | Nombre propuesto | Cambio |
| :-- | :-- | :-- |
| 1.1 | Servicio de catálogo, precios y promociones (R-01) en producción | Se agrega "en producción" y se escribe el nombre completo |
| 1.2 | Servicio de abastecimiento y reposición (R-02) en producción | Ídem |
| 1.3 | Servicio de inventario, reservas y disponibilidad (R-03) en producción | Ídem |
| 1.4 | Servicio de pedidos y cumplimiento omnicanal (R-04) en producción | Ídem |
| 1.5 | Servicio de registro y conciliación de ventas (R-05) en producción | Ídem |
| 1.6 | Servicio de atribución de ventas y comisiones (R-06) en producción | Ídem |
| 1.7 | Servicio de integración y gobierno de marketplace (R-07) en producción | Ídem |
| 1.8 | Servicio de posventa, garantías y devoluciones (R-08) en producción | Ídem |
| 1.9 | Servicio de clientes y fidelización Retail (R-09) en producción | Ídem |
| 1.10 | Servicio de originación y autorización de crédito (F-01) en producción | Ídem |
| 1.11 | Servicio de cartera, cobranza y repactaciones (F-02) en producción | Ídem |
| 1.12 | Servicio de consentimiento y evidencia financiera (F-03) en producción | Ídem |
| 1.13 | Servicio de autorización y auditoría de cruces Retail–Emisor (X-01) en producción | Ídem |
| 1.14 | 1.14a Plataforma de integración en producción | Se separa de las reglas, la identidad y la observabilidad |
|  | 1.14b Catálogo de reglas de acuerdo por tipo de dato (autoridad, copias y reconciliación) | Nuevo entregable documental; hoy estaba escondido en 1.14 |
|  | 1.14c Servicio de identidad y gestión de accesos en producción | Separado (Bases, art. 15: seguridad aparece aparte) |
|  | 1.14d Plataforma de observabilidad en producción | Separado (Bases, art. 15: observabilidad aparece aparte) |
| 1.15 | Se reemplaza por el bloque 1.15.1 a 1.15.22 (más abajo) | "Plataforma híbrida" abarcaba demasiado: nube, centro de datos, sitio de recuperación, centros de distribución y tiendas |
| 1.16 | POS con operación sin conexión de 24 h instalado en las 22 tiendas | Se agrega ámbito y autonomía. Etapa pendiente (opción a o b) |
| 1.17 | 1.17a Cartera de 620.000 clientes migrada y conciliada | "Reemplazo" era una actividad: se parte en dos resultados |
|  | 1.17b Plataforma de originación y cobranza de 2011 retirada | Ídem |
| 1.18 | 1.18a Conector con el ERP/DTE operando | Eran tres conectores en una fila |
|  | 1.18b Conector con el marketplace operando | |
|  | 1.18c Conector con el WMS principal operando | |
| 1.19 | Sistema central de retail de 2009 retirado | Ya no es condicional (SP-01) y pasa de actividad a resultado |
| 1.20 | 1.20a Informe de evaluación del comercio electrónico | Eran tres informes en una fila |
|  | 1.20b Informe de evaluación de fidelización (prueba de separación de datos) | |
|  | 1.20c Informe de evaluación y costeo del WMS en el centro de distribución de Concepción | |

### Entregables nuevos que salen de aplicar la regla del 100 %

Estaban exigidos por el Caso (cap. 11, cap. 13 y RT) o por nuestras exclusiones, y no figuraban en la lista:

| Código provisorio | Nombre propuesto | Origen |
| :-- | :-- | :-- |
| 1.21 | Mapa documentado de las 14 integraciones existentes | Caso cap. 10 n.º 15 y cap. 13: entrega temprana |
| 1.22 | Conector con la plataforma de comercio electrónico operando | EXC-15 (se integra) |
| 1.23 | Conectores con empresas de transporte de última milla operando | EXC-07 (integrarlas y trazar el pedido) |
| 1.24 | Conector con el sistema de remuneraciones operando (base de comisión) | EXC-05 (R-06 entrega la base de comisión) |
| 1.25 | Informe de evaluación, especificación y costeo de etiquetas electrónicas | EXC-02 |
| 1.26 | Especificación de dispositivos móviles para el personal de venta (cantidad y características) | EXC-03 |
| 1.27 | Especificación, costeo y calendario de compra del hardware y equipamiento físico que adquiere e instala el cliente (centro de datos, tiendas y centros de distribución) | EXC-10, EXC-19, SP-04 |
| 1.28 | Especificación, costeo y calendario de obras de infraestructura y enlaces que ejecuta y contrata el cliente | EXC-08, EXC-19, SP-04 |
| 1.29 | Estrategia de corte de inventario | Caso cap. 13 y RT-05.15 |
| 1.30 | Repositorio de consulta de datos históricos no migrados | RT-05.15 de las Bases Transversales |

### Bloque 1.15.x: infraestructura y sitios (reemplaza al antiguo 1.15)

Fuentes: Bases Administrativas art. 16 y 20; Bases Transversales caps. 6, 7 y 8; Caso 09 cap. 5, RT-03.24 y RT-06.01.

Reparto entre subdocumentos (Comunicado 10): el sd-03 declara qué se entrega (alcance). El sd-04 decide y especifica cómo y dónde: 4.2 arquitectura física (emplazamiento, ambientes, DR, respaldos), 4.2.1 implementos (T-11), 4.3.1 data center primaria y 4.3.2 data center secundario (región o sitio, replicación, RPO, RTO y conmutación). Por eso la tipología de cada sitio (sala principal, sala de sitio o gabinete) y la elección de región o sitio físico para el secundario se declaran en el sd-04, no aquí. En el sd-03 los nombres de estos entregables deben coincidir con los componentes del sd-04.

**Nube pública**

| Código provisorio | Nombre propuesto | Fuente |
| :-- | :-- | :-- |
| 1.15.1 | Entorno en nube pública multi-zona en producción, con región primaria y secundaria declaradas | Bases Admin. 16.3 |
| 1.15.2 | Repositorio de infraestructura como código del entorno completo | Bases Admin. 16.3 |

**Centro de datos principal (140 m², casa matriz, sala técnica principal)**

| Código provisorio | Nombre propuesto | Fuente |
| :-- | :-- | :-- |
| 1.15.3 | Plano y especificación del recinto técnico del centro de datos (distribución interna, obra civil y blindaje) | RT-06.01 a 06.06 |
| 1.15.4 | Plan de cierre de brecha del centro de datos frente al capítulo 6 (parte de la brecha del informe interno de 2024 que entrega el cliente) | Caso RT-06.01 |
| 1.15.5 | Sistema de energía ininterrumpida y generación autónoma de 24 h del centro de datos | RT-06.07 a 06.12 |
| 1.15.6 | Sistema de climatización de precisión N+1 con monitoreo ambiental del centro de datos | RT-06.13 a 06.15 |
| 1.15.7 | Sistema de detección temprana y extinción automática de incendios del centro de datos | RT-06.16 a 06.19 |
| 1.15.8 | Sistema de control de acceso físico biométrico y videovigilancia del centro de datos | RT-06.20 a 06.25 |
| 1.15.9 | Cómputo, almacenamiento y red del centro de datos operando | RT-08.01 a 08.06 |
| 1.15.10 | Rutas de comunicaciones redundantes del centro de datos | RT-06.32 y 06.33 |
| 1.15.11 | Espacio de operación del personal habilitado, separado de la sala de equipos | RT-06.29 a 06.31 |
| 1.15.12 | Servicio de custodia de medios de respaldo del centro de datos | RT-06.26 a 06.28 |

**Sitio secundario y recuperación ante desastres**

| Código provisorio | Nombre propuesto | Fuente |
| :-- | :-- | :-- |
| 1.15.13 | Sitio o región secundaria de recuperación ante desastres operando, con replicación continua | Bases Admin. art. 20 ("sitio o región"); RT-07.01 a 07.03. Dónde y cómo se decide en el sd-04 (4.3.2); preferencia del equipo: región de nube pública |
| 1.15.14 | Plan de recuperación ante desastres (RTO ≤ 4 h, RPO ≤ 15 min) | RT-07.04 a 07.06 |
| 1.15.15 | Solución de respaldo 3-2-1-1-0 operando | RT-07.09 a 07.14 |
| 1.15.16 | Informe de prueba de conmutación al sitio secundario (con RTO y RPO medidos) | RT-07.07 |

**Centros de distribución (2)**

| Código provisorio | Nombre propuesto | Fuente |
| :-- | :-- | :-- |
| 1.15.17 | Componentes on-premise operando en el centro de distribución principal, con 24 h de autonomía | RT-03.10 (24 h), Caso |
| 1.15.18 | (Retirado el 2026-10-06) Componentes on-premise y enlace redundante en el centro de Concepción | El centro se mantiene como está (EXC-13, SP-02); ID conservado para no renumerar |

**Tiendas (22)**

| Código provisorio | Nombre propuesto | Fuente |
| :-- | :-- | :-- |
| 1.15.19 | Gabinete on-premise operando en las 22 tiendas, con 24 h de autonomía | Caso RT-06.01 y RT-03.10 |
| 1.15.20 | Red segmentada (cajas, administración, videovigilancia y wifi de clientes) en las 13 tiendas que no la tienen | Caso RT-03.24 |
| 1.15.21 | Enlace de respaldo operando en las 7 tiendas que no lo tienen (6 en centro comercial y Coyhaique) | Caso RT-03.24; sd-02 (7 de 15) |
| 1.15.22 | Separación acreditada de la red y del ámbito de sistemas de la filial emisora respecto del retail | Caso RT-03.24 y RT-06.01 |

Responsabilidad de obras, equipos y enlaces (resuelto el 2026-10-06, ver SP-04 y EXC-19 en `enunciado_alcance.md`): el CLIENTE provee, instala y contrata todo lo físico; el proponente especifica (cómo y dónde), costea (cuánto), coordina, certifica la conformidad y configura y endurece el software y el firmware. La tensión con las Transversales (RT-06.33, RT-08.06) y con las Bases Administrativas (art. 14.1 y 14.2) queda declarada en SP-04 como interpretación, con su "Si no se cumple". Cada entregable 1.15.x que sea físico se acepta cuando el CLIENTE lo instaló conforme a la especificación y el proponente emitió el certificado de conformidad (1.15.23).

### Portales y aplicación móvil (nuevos, decisión del usuario: se separan)

| Código provisorio | Nombre propuesto | Fuente |
| :-- | :-- | :-- |
| 1.31a | Portal público (catálogo con precio y disponibilidad e información precontractual con simulador de costo), integrado con la plataforma de comercio electrónico, en producción | RT-16.30 |
| 1.31b | Consulta pública del estado de un pedido con su número, integrada con la plataforma de comercio electrónico, en producción (separada el 2026-10-06: depende de R-04) | RT-16.30 |
| 1.32 | Portal del cliente autenticado (compras, devoluciones, estado de cuenta y documentos), integrado con la plataforma de comercio electrónico, en producción | RT-16.30 |
| 1.33 | Vista del vendedor de marketplace (estado de cada pedido, devoluciones y evaluación) sobre el servicio R-07, sin administrar vendedores (EXC-04), en producción | RT-16.30 |
| 1.34 | Portal del proveedor (órdenes y recepciones) sobre el servicio R-02 en producción | RT-16.30 |
| 1.35 | Aplicación móvil del cliente (compra, seguimiento, devolución y estado de cuenta) en producción | RT-17.01 |
| 1.36 | Aplicación móvil del vendedor de sala (consulta de existencia con grado de confianza, en 2 s o menos) en producción en las 22 tiendas | RT-17.01 |
| 1.37 | Aplicación móvil de preparación de pedidos en tienda en producción | RT-17.01 |
| 1.38 | Aplicación móvil de conteo cíclico y prevención de pérdidas en producción en las 22 tiendas | RT-17.01 |
| 1.39 | Aplicación móvil de recepción de mercadería en tienda y centro de distribución en producción | RT-17.01 |

## 2. Entregables de gestión del proyecto

| Cód. anterior | Nombre propuesto | Cambio |
| :-- | :-- | :-- |
| 2.1 | Acta de constitución del proyecto | Sin cambio |
| 2.2 | 2.2a Registro de interesados | Se separa en dos |
|  | 2.2b Estrategia de involucramiento de interesados | El Comunicado 10 (3.4, Explicación de la Solución) exige la estrategia para obtener el apoyo de los grupos de interés clave de 2.4; se nombra aparte para poder verificarla |
| 2.3 | Plan para la dirección del proyecto | Excepción de la regla 3 (ver arriba) |
| 2.4 | Enunciado del alcance del proyecto | Sin cambio |
| 2.5 | 2.5a Documento de requisitos | Se separa en dos |
|  | 2.5b Matriz de trazabilidad de requisitos | |
| 2.6 | 2.6a EDT | Se separa en dos (el PMBOK las lista como salidas distintas) |
|  | 2.6b Diccionario de la EDT | |
| 2.7 | Línea base del alcance | Sin cambio |
| 2.8 | Cronograma del proyecto con hitos (línea base) | Se escribe como un solo documento |
| 2.9 | Línea base de costos | Se quita "y presupuesto" (es derivado) |
| 2.10 | Registro de riesgos con plan de respuesta | El registro incluye la respuesta (PMBOK) |
| 2.11 | Plan de gestión de la calidad | Las métricas son parte del plan |
| 2.12 | Informes de desempeño del trabajo | Sin cambio |
| 2.13 | Registro de solicitudes de cambio | Se simplifica |
| 2.14 | Actas de aceptación de entregables | Se simplifica |
| 2.15 | Registro de lecciones aprendidas | Sin cambio |
| 2.16 | 2.16a Informe de cierre del proyecto | Se separa en dos |
|  | 2.16b Acta de cierre del proyecto | |

## 3. Entregables de documentación técnica, transición y operación

Se separa cada paquete en sus documentos. Opción de agrupación en la redacción de 3.2 (decisión del usuario): presentar los documentos en "paquetes documentales" con la lista de sus componentes, sin perder la trazabilidad de cada uno.

| Cód. anterior | Nombre propuesto |
| :-- | :-- |
| 3.1 | 3.1a Documento de arquitectura de la solución |
|  | 3.1b Registro de decisiones de arquitectura |
| 3.2 | 3.2a Estándares de codificación |
|  | 3.2b Documentación de interfaces |
|  | 3.2c Diccionario de datos |
|  | 3.2d Inventario de componentes |
| 3.3 | 3.3a Plan de pruebas |
|  | 3.3b Casos de prueba |
|  | 3.3c Informe de pruebas de carga |
|  | 3.3d Informe de pruebas de resiliencia |
|  | 3.3e Informe de pruebas de seguridad |
| 3.4 | 3.4a Política de seguridad |
|  | 3.4b Modelo de amenazas |
|  | 3.4c Matriz de controles de seguridad |
|  | 3.4d Plan de remediación de seguridad |
| 3.5 | 3.5a Manual de operación |
|  | 3.5b Libros de operación |
|  | 3.5c Guías de resolución de incidentes |
|  | 3.5d Matriz de escalamiento |
|  | 3.5e Plan de continuidad y recuperación |
| 3.6 | 3.6a Plan de migración de datos |
|  | 3.6b Plan de convivencia entre sistemas antiguos y nuevos |
| 3.7 | 3.7a Plan de capacitación del personal del cliente |
|  | 3.7b Programa de certificación del personal del cliente |
| 3.8 | 3.8a Manuales de usuario por perfil |
|  | 3.8b Guía de gestión del cambio |
| 3.9 | Protocolo de aceptación de hitos y de producto final |
| 3.10 | Informe de cierre de marcha blanca (uno por etapa) |
| 3.11 | Plan de retiro de la plataforma de originación y cobranza de 2011 |
| nuevo | 3.12 Plan de salida del proveedor de nube (término anticipado y retorno de la operación por cuenta propia o con otro proveedor) |
|  | 3.13 Informe de diligencia reforzada del proveedor de nube |
|  | 3.14 Registro de proveedores externos y servicios externalizados, en el formato del archivo I28 (condicional) |

|  | 3.15 Política de retención y custodia de datos (RT-05.10 y RT-16.10; agregada el 2026-10-06 tras detectar que ningún documento cubría los plazos de retención) |

Origen de 3.12 a 3.14 (PDF de `90_Referencia/CMF/`, ver `sd-04_contexto/notas_dr_nube.md`): 3.12 y 3.13 salen del capítulo 20-7 de la RAN (planes de salida, num. III.3; diligencia reforzada en nube para actividades críticas, título V, letras a a g). 3.14 sale del informe normativo de abril de 2026, que extiende a los emisores no bancarios el archivo I28 con periodicidad semestral. Reparo: el capítulo 20-7 se dirige a bancos y el informe es una propuesta en consulta pública, no una norma vigente. Se incluyen como buena práctica verificable; 3.14 queda condicionado a que la propuesta se apruebe. Por aprobar por el usuario.

## Cuenta

- Producto: 13 servicios + 4 (1.14) + 1 (POS) + 2 (1.17) + 3 (1.18) + 1 (1.19) + 3 (1.20) + 10 nuevos (1.21 a 1.30) + 22 (bloque 1.15.x; 21 desde el retiro de 1.15.18) + 9 (portales y aplicación móvil) = 68 (67 tras el retiro de 1.15.18; 68 con 1.15.23).
- Gestión: 20.
- Documentación: 29 (3.1a a 3.11) más 3 propuestos (3.12 a 3.14, por aprobar) = 32.
- Total vigente (2026-10-06): 122 entregables (69 de producto, tras retirar 1.15.18, sumar 1.15.23 y separar 1.31 en a y b; 20 de gestión; 33 de documentación incluidos 3.12 a 3.15). Total vigente: 122 con 3.15. Original: 117 (antes 47). El aumento viene de separar paquetes, de los entregables que el Caso exigía y faltaban, y del bloque de infraestructura.

La redacción de 3.2 presenta familias de entregables (servicios, infraestructura, portales y aplicaciones, gestión, documentación); esta lista queda como contexto con el detalle completo.

## Pendientes de esta ronda

1. Nombres aprobados por el usuario, incluido el bloque 1.15.x.
2. Responsabilidad de obras, hardware y conectividad: resuelto el 2026-10-06 (SP-04, EXC-19). El acta por sitio es 1.15.23, "Acta de recepción y certificado de conformidad".
3. Diferido al sd-04: tipología de cada sitio y sitio o región secundaria (preferencia del equipo: región de nube pública; las Bases Admin. art. 20 admiten "sitio o región").
4. Alinear las referencias de `entregables_alcance.md` (1.10, 1.16, 1.19, 1.20) con estos nombres.
