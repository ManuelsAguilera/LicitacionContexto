# Entregables del alcance (borrador)

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

Documento de trabajo. No es entregable.

Fundamento metodológico: PMBOK 6.ª edición, proceso "Definir el alcance" (salida: enunciado del alcance, con entregables y criterios de aceptación) y "Crear la EDT" (descomposición orientada a entregables, regla del 100 %, diccionario). Apoyo de clase: FEP02, diapositivas 37, 38, 52, 55, 56 y 57.

Fuentes de contenido: `descripcion_alcance_producto.md` (producto, servicios, sistemas) y `Análisis de actores, alcance y arquitectura de servicios.md`. Documentación contractual mínima: Bases Administrativas (documentación como entregable contractual, Art. 18). Valores numéricos: solo los ya documentados en el sd-02 (Tabla 2.2), marcados como tales; el resto queda como `[umbral por definir]`.

## Reglas aplicadas

1. **Definición (FEP02·38).** Entregable es un producto, resultado o capacidad única y verificable. Cada uno lleva su criterio de aceptación; sin criterio no está definido.
2. **Criterio bien escrito (FEP02·38).** Hecho observable, medible y con umbral. Un criterio sin umbral no se puede recibir ni rechazar.
3. **Orientación a entregables (FEP02·EDT).** El primer nivel de la EDT son los entregables, no las fases ni las disciplinas.
4. **Regla del 100 % (FEP02·52).** Los componentes de cada nivel suman todo el trabajo del superior, sin faltante ni duplicado.
5. **Paquete de trabajo (FEP02·56-57).** Cada entregable de último nivel tiene código, descripción, criterio, responsable, hitos, esfuerzo, costo, recursos, supuestos y referencias. Aquí se completan código, descripción, criterio y referencias; el resto lo aporta el plan de trabajo.
6. **Validar vs controlar (FEP02).** Controlar la calidad lo hace el equipo (el entregable es correcto); validar el alcance lo hace el cliente (el entregable es aceptado y firmado).
7. **No es cronograma (FEP02·53).** La lista no ordena en el tiempo. La etapa se asigna aparte.

Convención de código: `1.x` entregables de producto, `2.x` de gestión del proyecto, `3.x` de transición y cierre. Es provisoria hasta alinearla con la EDT del sd-07.

Versión 2 (2026-10-06): nombres aprobados en `ronda0_nombres.md`; etapas de `asignacion_etapas.md`. La columna Etapa indica el origen: **D** = decidido con el usuario, **C** = derivado de los criterios P1 a P4 (2026-10-06, `asignacion_etapas.md`, Ronda G), por confirmar, **S** = sugerido por el asistente sin derivación. La columna "Requiere a" sale de la Ronda B (capas 0 a 4). Versión anterior (47 entregables) respaldada fuera del repositorio.

---

## 1. Entregables de producto

Etapa 1: desarrollo meses 1 a 12, marcha blanca 13 a 15, producción mes 16. Etapa 2: desarrollo 13 a 18, marcha blanca 19 y 20, producción mes 21. Operación: meses 21 a 56. Umbrales marcados `(sd-02)` o con RT salen de los documentos; `[umbral por definir]` queda abierto.

### 1.A Servicios de negocio (13)

| Cód. | Entregable | Criterio de aceptación | Etapa | Requiere a |
| :-- | :-- | :-- | :-- | :-- |
| 1.1 | Servicio de catálogo, precios y promociones (R-01) en producción | Discrepancia entre precio exhibido y cobrado ≤ 3 % en muestra auditada (sd-02); propagación a cajas y canal digital ≤ 5 min; historial por canal y fecha recuperable 5 años | 1 (D) | Capa 0 |
| 1.2 | Servicio de abastecimiento y reposición (R-02) en producción | Órdenes y transferencias coordinadas con WMS y ERP/DTE sin intervención manual `[umbral por definir]` | 2 (D) | R-01, R-03 |
| 1.3 | Servicio de inventario, reservas y disponibilidad (R-03) en producción | Discrepancia en conteo cíclico < 2 % y cancelaciones por falta de existencia < 0,3 % (sd-02); consulta de disponibilidad ≤ 400 ms; actualización ≤ 30 s tras una venta; nodo Concepción con margen de confianza declarado (SP-02) | 1 (D) | R-01 |
| 1.4 | Servicio de pedidos y cumplimiento omnicanal (R-04) en producción | Pedidos entregados en la fecha ofrecida ≥ 97 % (sd-02); estado único en todos los puntos de contacto; confirmación ≤ 3 s en el evento anual | 2 (D) | R-01, R-03, R-05 |
| 1.5 | Servicio de registro y conciliación de ventas (R-05) en producción | 100 % de las ventas del POS conciliadas, incluidas las de desconexión; sincronización ≤ 30 min tras la reconexión `[umbral de diferencia por definir]` | 1 (D) | R-01 |
| 1.6 | Servicio de atribución de ventas y comisiones (R-06) en producción | Base de comisión entregada al sistema de remuneraciones con atribución auditable `[umbral por definir]` | 2 (D) | R-04, R-05 |
| 1.7 | Servicio de integración y gobierno de marketplace (R-07) en producción | Estados comprensibles para vendedor y Ancoa; nivel de servicio medido por vendedor `[umbral por definir]` | 2 (D) | R-03 |
| 1.8 | Servicio de posventa, garantías y devoluciones (R-08) en producción | Reingreso a inventario con aptitud registrada; garantía atendida sin derivar al fabricante como condición `[umbral por definir]` | 2 (D) | R-03, R-05 |
| 1.9 | Servicio de clientes y fidelización Retail (R-09) en producción | Cero atributos del Emisor en perfiles comerciales, verificado en revisión de segregación | 2 (D) | R-01 y X-01 |
| 1.10 | Servicio de originación y autorización de crédito (F-01) en producción | Evaluación en el punto de venta ≤ 8 s (RT-09.01, rige sobre los 10 s del sd-02); versión precontractual registrada en cada solicitud; prueba de factibilidad del crédito sin conexión aprobada (compras dentro de los topes del Emisor, aceptación recuperable en F-03, conciliación en 30 min o menos sin diferencias no explicadas) o, si no pasa, función declarada no disponible | 1 (D) | F-03, X-01 |
| 1.11 | Servicio de cartera, cobranza y repactaciones (F-02) en producción | Cada repactación consulta evidencia en F-03 antes de confirmarse; ola 1 con los clientes con saldo al día y ola 2 con los que tienen repactaciones, cobranza o juicios en curso | 1 ola 1 y 2 ola 2 (D) | F-03 |
| 1.12 | Servicio de consentimiento y evidencia financiera (F-03) en producción | 0 repactaciones sin evidencia recuperable (sd-02); retención por plazo del crédito + 6 años (sd-02) | 1 (D) | Capa 0 |
| 1.13 | Servicio de autorización y auditoría de cruces Retail–Emisor (X-01) en producción | 100 % de los cruces con finalidad, autorización y registro; 0 consultas directas a bases del otro negocio | 1 (D) | Capa 0 |

### 1.B Plataforma común

| Cód. | Entregable | Criterio de aceptación | Etapa | Requiere a |
| :-- | :-- | :-- | :-- | :-- |
| 1.14a | Plataforma de integración en producción | Operación sin punto único de falla; prueba de falla de un componente sin pérdida de coherencia `[umbral por definir]` | 1 (D, Bases art. 15) | — |
| 1.14b | Catálogo de reglas de acuerdo por tipo de dato (autoridad, copias y reconciliación) | Una regla escrita por cada dato bajo autoridad de los 13 servicios; reconciliación sin pérdida de transacciones | 1 (D) | 1.14a |
| 1.14c | Servicio de identidad y gestión de accesos en producción | Acceso por rol verificado en revisión de segregación `[umbral por definir]` | 1 (D, Bases art. 15) | — |
| 1.14d | Plataforma de observabilidad en producción | Trazas con identificador de correlación entre todas las integraciones (RT-05.19) | 1 (D, Bases art. 15) | 1.14a |

### 1.C Aplicaciones, conectores y sistemas

| Cód. | Entregable | Criterio de aceptación | Etapa | Requiere a |
| :-- | :-- | :-- | :-- | :-- |
| 1.16 | POS con operación sin conexión de 24 h instalado en las 22 tiendas | Compuerta de la ola 1 a la 2 (9 condiciones, incluidos el retorno probado y la prueba del crédito sin conexión, ver `asignacion_etapas.md`, D2); 22 tiendas operando; ola 1 en los meses 6 y 7 y ola 2 en los meses 8 a 10, con respaldo hasta el mes 16 (ventanas libres del Caso 13.2) | 1: ola 1 piloto de 3 tiendas, ola 2 las otras 19 antes del mes 16 (D) | R-01, R-05, 1.15.19 |
| 1.17a | Cartera de 620.000 clientes migrada y conciliada | Cuadre de totales sin diferencias; ola 1 clientes con saldo al día, ola 2 clientes con repactaciones, cobranza o juicios en curso; cada tramo con las condiciones del Caso 13.3.5 (conciliación diaria, retorno probado, comunicación) | 1 ola 1 y 2 ola 2 (D) | F-02, F-03 |
| 1.17b | Plataforma de originación y cobranza de 2011 retirada | Retiro con conciliación final sin diferencias no explicadas, antes de enero de 2029 | Operación; fecha objetivo octubre de 2028 (D) | 1.17a ola 2 |
| 1.18a | Conector con el ERP/DTE operando | Intercambio por contrato publicado; ERP/DTE sigue como único emisor tributario | 1 (D, integración crítica) | Capa 0 |
| 1.18b | Conector con el marketplace operando | Intercambio por contrato publicado | 2 (D) | R-03 |
| 1.18c | Conector con el WMS principal operando | Intercambio por contrato publicado | 1 (D, integración crítica) | Capa 0, R-03 |
| 1.19 | Sistema central de retail de 2009 retirado | Maestro de artículos, precios e inventario migrados en la Etapa 1; órdenes, recepción y reposición en la Etapa 2; conciliación sin diferencias no explicadas | Migración en 1 y 2; retiro al cierre de la marcha blanca de la Etapa 2 (D) | R-01, R-03, R-02 |
| 1.20a | Informe de evaluación del comercio electrónico | Piloto por categorías con cancelación por falta de existencia menor que la previa y bajo 0,3 % al cierre; disponibilidad actualizada en 30 s o menos; consulta en 400 ms o menos; decisión aprobada (Caso 13.3.6) | 1 (D) | R-03 |
| 1.20b | Informe de evaluación de fidelización (prueba de separación de datos) | Prueba de separación de datos aprobada antes de cualquier cruce: cero atributos del Emisor en perfiles comerciales; 100 % de los cruces con finalidad, autorización y registro | 1 (D) | X-01 |
| 1.20c | Informe de evaluación y costeo del WMS en el centro de distribución de Concepción | Alternativas costeadas (incorporar al WMS, solución propia o mantener como está) con recomendación; base de la solicitud de cambio si el CLIENTE decide incorporarlo (SP-02) | 1 (D) | — |
| 1.21 | Mapa documentado de las 14 integraciones existentes | 14 integraciones documentadas con origen, destino, datos y dueño | 1, primera entrega (D) | — |
| 1.22 | Conector con la plataforma de comercio electrónico operando | Disponibilidad publicada desde R-03 en ≤ 30 s | 1 (D, integración crítica) | R-03 |
| 1.23 | Conectores con empresas de transporte de última milla operando | Estado del pedido trazado hasta la entrega | 2 (C) | R-04 |
| 1.24 | Conector con el sistema de remuneraciones operando (base de comisión) | Base de comisión entregada y auditada | 2 (C) | R-06 |

### 1.D Informes y especificaciones para el cliente

| Cód. | Entregable | Criterio de aceptación | Etapa | Requiere a |
| :-- | :-- | :-- | :-- | :-- |
| 1.25 | Informe de evaluación, especificación y costeo de etiquetas electrónicas | Alternativas comparadas y costeadas (EXC-02) | 1 (C) | — |
| 1.26 | Especificación de dispositivos móviles para el personal de venta (cantidad y características) | Cantidad y características por tienda (EXC-03) | 1 (C) | — |
| 1.27 | Especificación, costeo y calendario de compra del hardware y equipamiento físico que adquiere e instala el cliente (centro de datos, tiendas y centros de distribución) | Qué comprar, cuánto, con qué características y cuánto cuesta (EXC-10, EXC-19, SP-04) | 1 (C) | — |
| 1.28 | Especificación, costeo y calendario de obras de infraestructura y enlaces que ejecuta y contrata el cliente | Obras y enlaces por sitio, especificados, costeados y calendarizados (EXC-08, EXC-19, SP-04) | 1 (C) | — |
| 1.29 | Estrategia de corte de inventario | Estrategia declarada para 22 tiendas y 2 centros de distribución que no cierran (RT-05.15) | 1 (D) | — |
| 1.30 | Repositorio de consulta de datos históricos no migrados | Consulta de los datos fuera de la lista migrada (EXC-18) | 2 (C) | 1.19 |

### 1.E Infraestructura y sitios (bloque 1.15.x)

Toda la infraestructura va en la Etapa 1 (Bases art. 15: implementación híbrida completa; criterio 1). Tipología de sitios y ubicación del sitio o región secundaria se declaran en el sd-04.

**Responsabilidades (SP-04, EXC-19):** el CLIENTE provee, instala y contrata lo físico (obras, equipos y enlaces). El proponente especifica (cómo y dónde), costea (cuánto), coordina, certifica la conformidad y configura y endurece el software y el firmware. Un entregable físico de esta tabla se acepta cuando está instalado por el CLIENTE conforme a la especificación, con el certificado de conformidad del proponente (por ejemplo, certificación de cada enlace de cableado, RT-06.04) y las pruebas de funcionamiento satisfactorias.

| Cód. | Entregable | Etapa | Provisión e instalación |
| :-- | :-- | :-- | :-- |
| 1.15.1 | Entorno en nube pública multi-zona en producción, con región primaria y secundaria declaradas | 1 (D) | Proponente |
| 1.15.2 | Repositorio de infraestructura como código del entorno completo | 1 (D) | Proponente |
| 1.15.3 | Plano y especificación del recinto técnico del centro de datos | 1 (D) | Proponente (documento) |
| 1.15.4 | Plan de cierre de brecha del centro de datos frente al capítulo 6 | 1 (D) | Proponente (plan); el cliente ejecuta el cierre |
| 1.15.5 | Sistema de energía ininterrumpida y generación autónoma de 24 h del centro de datos | 1 (D) | Cliente |
| 1.15.6 | Sistema de climatización de precisión N+1 con monitoreo ambiental del centro de datos | 1 (D) | Cliente |
| 1.15.7 | Sistema de detección temprana y extinción automática de incendios del centro de datos | 1 (D) | Cliente |
| 1.15.8 | Sistema de control de acceso físico biométrico y videovigilancia del centro de datos | 1 (D) | Cliente |
| 1.15.9 | Cómputo, almacenamiento y red del centro de datos operando | 1 (D) | Cliente (equipos); proponente configura y endurece |
| 1.15.10 | Rutas de comunicaciones redundantes del centro de datos | 1 (D) | Cliente |
| 1.15.11 | Espacio de operación del personal habilitado, separado de la sala de equipos | 1 (D) | Cliente |
| 1.15.12 | Servicio de custodia de medios de respaldo del centro de datos | 1 (D) | Cliente (contrata el servicio) |
| 1.15.13 | Sitio o región secundaria de recuperación ante desastres operando, con replicación continua | 1 (D) | Proponente |
| 1.15.14 | Plan de recuperación ante desastres (RTO ≤ 4 h, RPO ≤ 15 min) | 1 (D) | Proponente |
| 1.15.15 | Solución de respaldo 3-2-1-1-0 operando | 1 (D) | Proponente configura; medios físicos del cliente |
| 1.15.16 | Informe de prueba de conmutación al sitio secundario (con RTO y RPO medidos) | 1 (D); se repite semestralmente en Operación | Proponente |
| 1.15.17 | Componentes on-premise operando en el centro de distribución principal, con 24 h de autonomía | 1 (D) | Cliente (equipos); proponente configura |
| 1.15.18 | (Retirado el 2026-10-06; ID conservado) El centro de Concepción se mantiene como está (EXC-13, SP-02) | — | — |
| 1.15.19 | Gabinete on-premise operando en las 22 tiendas, con 24 h de autonomía | 1 (D); antes de la ola correspondiente del POS | Cliente (equipos); proponente configura |
| 1.15.20 | Red segmentada (cajas, administración, videovigilancia y wifi de clientes) en las 13 tiendas que no la tienen | 1 (D) | Cliente (equipos); proponente configura |
| 1.15.21 | Enlace de respaldo operando en las 7 tiendas que no lo tienen (6 en centro comercial y Coyhaique) | 1 (D) | Cliente (contrata) |
| 1.15.22 | Separación acreditada de la red y del ámbito de sistemas de la filial emisora respecto del retail | 1 (D) | Proponente configura y acredita |
| 1.15.23 | Acta de recepción y certificado de conformidad de obras y equipamiento del cliente (una por sitio) | 1 (C) | Proponente certifica; cliente firma la recepción |

### 1.F Portales y aplicaciones móviles

Etapas por dependencia con los servicios (Ronda B). 1.31a/1.31b y las dos olas de 1.36 y 1.38 se decidieron con el usuario el 2026-10-06; las demás se derivaron de los criterios P1 a P4 (C). Las apps de sala usan las mismas 3 tiendas piloto del POS; su ola 2 llega al resto en la Etapa 2, porque el Caso no obliga a tenerlas en las 22 tiendas el mes 16.

| Cód. | Entregable | Etapa | Requiere a |
| :-- | :-- | :-- | :-- |
| 1.31a | Portal público (catálogo con precio y disponibilidad e información precontractual con simulador de costo), integrado con la plataforma de comercio electrónico, en producción | 1 (D) | R-01, R-03, F-03 |
| 1.31b | Consulta pública del estado de un pedido con su número, integrada con la plataforma de comercio electrónico, en producción | 2 (D) | R-04 |
| 1.32 | Portal del cliente autenticado (compras, devoluciones, estado de cuenta y documentos), integrado con la plataforma de comercio electrónico, en producción | 2 (C) | R-04, R-08, F-02 |
| 1.33 | Vista del vendedor de marketplace (estado de cada pedido, devoluciones y evaluación) sobre el servicio R-07, sin administrar vendedores (EXC-04), en producción | 2 (C) | R-07 |
| 1.34 | Portal del proveedor (órdenes y recepciones) sobre el servicio R-02 en producción | 2 (C) | R-02 |
| 1.35 | Aplicación móvil del cliente (compra, seguimiento, devolución y estado de cuenta) en producción | 2 (C) | R-04, F-02 |
| 1.36 | Aplicación móvil del vendedor de sala (consulta de existencia con grado de confianza, en 2 s o menos) en producción en las 22 tiendas | 1 ola 1 (piloto de 3 tiendas) y 2 ola 2 (resto) (D) | R-03 |
| 1.37 | Aplicación móvil de preparación de pedidos en tienda en producción | 2 (C) | R-04 |
| 1.38 | Aplicación móvil de conteo cíclico y prevención de pérdidas en producción en las 22 tiendas | 1 ola 1 (piloto de 3 tiendas) y 2 ola 2 (resto) (D) | R-03 |
| 1.39 | Aplicación móvil de recepción de mercadería en tienda y centro de distribución en producción | 2 (C) | R-02 |

---

## 2. Entregables de gestión del proyecto (PMBOK 6)

Asignación por proceso (Ronda F, F4). Las etapas de repetición se indican donde corresponde.

| Cód. | Entregable | Criterio de aceptación | Etapa |
| :-- | :-- | :-- | :-- |
| 2.1 | Acta de constitución del proyecto | Firmada por el patrocinador; objetivos, interesados clave y restricciones iniciales | Inicio (D) |
| 2.2a | Registro de interesados | Cobertura de los grupos identificados en sd-02 §2.4 | Inicio (D) |
| 2.2b | Estrategia de involucramiento de interesados | Estrategia por grupo | Inicio (D) |
| 2.3 | Plan para la dirección del proyecto | Aprobado; cada plan subsidiario con responsable y método de control | Inicio (D) |
| 2.4 | Enunciado del alcance del proyecto | Seis contenidos presentes; aprobado | Inicio (D) |
| 2.5a | Documento de requisitos | Cada requisito con origen y prioridad | Inicio (D) |
| 2.5b | Matriz de trazabilidad de requisitos | Cada requisito vinculado a diseño, prueba y entregable | Inicio (D) |
| 2.6a | EDT | Regla del 100 % verificada | Inicio (D) |
| 2.6b | Diccionario de la EDT | Paquetes con responsable único y criterio | Inicio (D) |
| 2.7 | Línea base del alcance | Versionada y aprobada | Inicio (D) |
| 2.8 | Cronograma del proyecto con hitos (línea base) | Alineado con el cronograma contractual; hitos de pago identificados | Inicio (D) |
| 2.9 | Línea base de costos | Consistente con la oferta económica `[detalle por definir]` | Inicio (D) |
| 2.10 | Registro de riesgos con plan de respuesta | Riesgos con probabilidad, impacto, responsable y respuesta | Inicio (D) |
| 2.11 | Plan de gestión de la calidad | Métricas con umbral por entregable | Inicio (D) |
| 2.12 | Informes de desempeño del trabajo | Con la periodicidad del plan de comunicaciones | Continuo (D) |
| 2.13 | Registro de solicitudes de cambio | Todo cambio al catálogo de trece servicios con aprobación del Comité Ejecutivo | Continuo (D) |
| 2.14 | Actas de aceptación de entregables | Acta firmada por la Contraparte Técnica por entregable | Continuo (D) |
| 2.15 | Registro de lecciones aprendidas | Actualizado al cierre de cada etapa | Continuo (D) |
| 2.16a | Informe de cierre del proyecto | Entregables recibidos y pendientes listados | Cierre (D) |
| 2.16b | Acta de cierre del proyecto | Firmada; liquidación y reversibilidad según contrato | Cierre (D) |

---

## 3. Entregables de documentación técnica, transición y operación

3.5, 3.6, 3.7, 3.9 y 3.10 se repiten en cada etapa (D). 3.11 va en la Etapa 1 (D). Los demás tienen emisión en la Etapa 1 y actualización en la Etapa 2, derivados de los criterios P1 a P4 (C).

| Cód. | Entregable | Criterio de aceptación | Etapa |
| :-- | :-- | :-- | :-- |
| 3.1a | Documento de arquitectura de la solución | Lógica, física, datos, integración y seguridad; diagramas propios | 1, actualiza 2 (C) |
| 3.1b | Registro de decisiones de arquitectura | Cada decisión con alternativas y criterio | 1, actualiza 2 (C) |
| 3.2a | Estándares de codificación | Aprobados antes del desarrollo | 1 (C) |
| 3.2b | Documentación de interfaces | Una por servicio e integración | 1, actualiza 2 (C) |
| 3.2c | Diccionario de datos | Propietario por dominio | 1, actualiza 2 (C) |
| 3.2d | Inventario de componentes | Un inventario único | 1, actualiza 2 (C) |
| 3.3a | Plan de pruebas | Cubre los niveles de prueba de las Bases | 1, actualiza 2 (C) |
| 3.3b | Casos de prueba | Por servicio | 1, actualiza 2 (C) |
| 3.3c | Informe de pruebas de carga | Contra los umbrales de RT-09.01 | 1 y 2 (C) |
| 3.3d | Informe de pruebas de resiliencia | Incluye operación sin conexión y falla de componentes | 1 y 2 (C) |
| 3.3e | Informe de pruebas de seguridad | Sin hallazgos críticos abiertos | 1 y 2 (C) |
| 3.4a | Política de seguridad | Aprobada | 1 (C) |
| 3.4b | Modelo de amenazas | Cubre la frontera Retail–Emisor | 1, actualiza 2 (C) |
| 3.4c | Matriz de controles de seguridad | Controles trazables a entregables | 1, actualiza 2 (C) |
| 3.4d | Plan de remediación de seguridad | Con plazos | 1, actualiza 2 (C) |
| 3.5a a 3.5e | Manual de operación; libros de operación; guías de resolución de incidentes; matriz de escalamiento; plan de continuidad y recuperación | Revisados por operación antes de cada paso a producción | 1 y 2 (D) |
| 3.6a | Plan de migración de datos | Cubre sistemas conservados, reemplazados y condicionados | 1 y 2 (D) |
| 3.6b | Plan de convivencia entre sistemas antiguos y nuevos | Por etapa | 1 y 2 (D) |
| 3.7a | Plan de capacitación del personal del cliente | Personal certificado conforme al plan (condición del art. 17.3) | 1 y 2 (D) |
| 3.7b | Programa de certificación del personal del cliente | Idem | 1 y 2 (D) |
| 3.8a | Manuales de usuario por perfil | Un manual por actor principal | 1 y 2 (C) |
| 3.8b | Guía de gestión del cambio | Aprobada | 1 y 2 (C) |
| 3.9 | Protocolo de aceptación de hitos y de producto final | Entregables, criterios, evidencia, plazos y observaciones definidos | 1 y 2 (D) |
| 3.10 | Informe de cierre de marcha blanca (uno por etapa) | Condiciones del art. 17.3 | 1 y 2 (D) |
| 3.11 | Plan de retiro de la plataforma de originación y cobranza de 2011 | Fecha objetivo octubre de 2028 | 1 (D) |
| 3.12 | Plan de salida del proveedor de nube | Por aprobar | 1 (C) |
| 3.13 | Informe de diligencia reforzada del proveedor de nube | Por aprobar | 1 (C) |
| 3.14 | Registro de proveedores externos y servicios externalizados, en el formato del archivo I28 (condicional) | Por aprobar; depende de la norma de la CMF | 2, condicional: antes de la primera entrega semestral que exija la norma (C) |
| 3.15 | Política de retención y custodia de datos | Cada categoría de dato con plazo, custodio, mecanismo de recuperación y destrucción, según RT-05.10 del Caso (documentos tributarios y ventas 6 años; antecedentes del crédito plazo + 6 años; movimientos de inventario 6 años; fidelización relación + 2 años; videovigilancia 30 días; trazabilidad del precio 5 años, ver `descripcion_alcance_producto.md` §2) y RT-16.10 (auditoría, mínimo 5 años) | 1 (D) |

---

## Verificación de la regla del 100 %

- Cada servicio del catálogo de trece tiene entregable propio (1.1 a 1.13) y todos tienen etapa.
- Excepción deliberada a "ningún entregable en dos etapas": F-02 (1.11), la cartera migrada (1.17a) y las apps de sala 1.36 y 1.38 se entregan por olas, cada ola con su propia aceptación (decisiones C2 y D2).
- Etapa 1 contiene la plataforma completa, las seis integraciones críticas y la funcionalidad de primera prioridad (Bases art. 15). Etapa 2 no obliga a rehacer arquitectura.
- Quedan por revisar al construir la EDT: que 1.14 a 1.18 no dupliquen trabajo, y que 3.1 a 3.5 no dupliquen 2.3 y 2.11.

## Pendientes

1. Confirmar las etapas marcadas (C), derivadas de los criterios P1 a P4.
2. Aprobar 3.12 a 3.14 y 1.15.23.
3. Hito y porcentaje de pago (Formulario E-25) de cada entregable.
4. Umbrales marcados `[umbral por definir]`, entre ellos las pruebas de e-commerce y fidelización y la prueba de factibilidad de F-01 offline.
5. Responsable por paquete y esfuerzo, que salen del plan de trabajo (sd-07).
6. Alinear la numeración con la EDT del sd-07.
7. Planillas (novena plataforma): cubiertas por R-01, R-08, identidad (1.14c) y R-03; Concepción se mantiene como está (SP-02). Definir formato y periodicidad de la carga de existencias de Concepción.
