# Cronograma de la EDT corregida (paso 10)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_cronograma.py` a partir de `14_edt_corregida.md`; no editar a mano. Fecha: 2026-10-08. Estado: **propuesta** de este trabajo, pendiente del visto bueno del equipo. El mes 1 es enero de 2027 (SUP-26). Cada paquete tiene una ventana de meses. La ventana es **fija por contrato** (Bases, sd-03 o Anexo D) o es **propuesta** de este trabajo; la columna Fuente lo dice. No hay horas de los paquetes que el UCP no cubre, ni dotación, ni personas. No es la carta Gantt del Formulario T-14: es el calendario de ventanas que la hace posible.

## 1. Calendario y anclas del contrato

| Mes | Calendario | Hito | Fuente |
| --: | :-- | :-- | :-- |
| 1 | ene 2027 | Inicio del contrato | SUP-26 |
| 1 a 3 | ene 2027 a mar 2027 | Plan de Reversibilidad (primeros noventa días) | Art. 77.2 |
| 1 a 12 | ene 2027 a dic 2027 | Etapa 1: desarrollo, con certificación y ambientes habilitados | Art. 17 |
| 13 a 15 | ene 2028 a mar 2028 | Etapa 1: marcha blanca, en paralelo con el desarrollo de la Etapa 2 | Art. 17, 17.2 |
| 16 | abr 2028 | Etapa 1 pasa a producción y es el registro oficial | Art. 17 |
| 13 a 18 | ene 2028 a jun 2028 | Etapa 2: desarrollo (cierra en el mes 18 inclusive) | Art. 17 |
| 19 a 20 | jul 2028 a ago 2028 | Etapa 2: marcha blanca, con la Etapa 1 en producción | Art. 17, 17.2 |
| 21 | sep 2028 | Etapa 2 pasa a producción, aceptación final e inicio de la operación | Art. 17 |
| 22 | oct 2028 | Retiro de la plataforma de crédito de 2011 (fecha objetivo) | sd-03, operación |
| 24 | dic 2028 | Hitos del plan de remediación de la autoridad, a más tardar | Anexo D, resultado 23 |
| 21 a 56 | sep 2028 a ago 2031 | Operación | Art. 17 |
| 56 | ago 2031 | Cierre del contrato | Art. 17 |

### Congelamientos (Caso, numeral 13.2)

No puede haber un paso a producción dentro de un congelamiento. Meses calendario afectados: ene (1 al 6 de enero y última semana), feb (todo el mes), mar (primera semana), may (segunda semana y evento anual posible), jun (evento anual posible), nov (todo el mes), dic (todo el mes). Los pasos a producción caen en abr 2028 y sep 2028, fuera de todos ellos. Cae en congelamiento la marcha blanca de la Etapa 1 (ene 2028 a mar 2028): es operación supervisada, sin cambios en producción, así que se coordina con el plan de la marcha blanca. Con la Etapa 1 ya en producción, el evento anual de comercio electrónico y el Día de la Madre de 2028 (may 2028 y jun 2028) caen en el desarrollo de la Etapa 2: el ensayo de degradación del evento (paquete 1.9.6) debe estar hecho antes.

## 2. Ventanas por cuenta de control

Las barras tienen 56 columnas, una por mes; `█` es un mes activo. El año 1 son las columnas 1 a 12.

```
mes               1         2         3         4         5      
         12345678901234567890123456789012345678901234567890123456
```

### Rama 1.1

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.1.1 | Plan de dirección integrado (ámbito, cronograma, costos, calidad, riesgos, comunicaciones, interesados y adquisiciones) | 1–3 | propuesta | plan inicial; se actualiza durante el contrato |
| 1.1.2 | EDT y diccionario de paquetes con entregable, criterio de aceptación y responsable | 1–3 | propuesta | base de la planificación |
| 1.1.3 | Registro de solicitudes de cambio y su resolución | 1–56 | contrato | Art. 72: todo el contrato |
| 1.1.4 | Registros de riesgos, lecciones aprendidas, supuestos y consultas | 1–56 | propuesta | continuo |
| 1.1.6 | Calendario de ventanas de congelamiento y de eventos anuales con declaración de impacto por evento | 1–3 | propuesta | se actualiza cada año antes de la campaña de noviembre |
| 1.1.7 | Actas de los comités e informe mensual de avance | 1–56 | contrato | Art. 71: comités durante todo el contrato; RT-19.06: informe mensual |
| 1.1.9 | Reporte mensual de consumo de nube | 4–56 | propuesta | desde el primer entorno de nube |
| 1.1.10 | Actas de aceptación por entrega y habilitación de pagos | 1–56 | contrato | Art. 18: cada entrega sujeta a aceptación |
| 1.1.11 | Registro de garantías, seguros y certificados laborales vigentes | 1–56 | contrato | Art. 75.3 |
| 1.1.12 | Acta de constitución del proyecto | 1–1 | propuesta | mes de inicio |
| 1.1.13 | Línea base de costos y presupuesto | 1–3 | propuesta | base de la planificación |
| 1.1.14 | Planes alternativos de las dos condiciones del adelanto del negocio financiero | 3–5 | propuesta | sd-03, 3.2.3: antes de la prueba del corte de enlace de los meses 6 y 7 |

### Rama 1.2

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.2.1 | Mapa de las 14 interfaces e inventario de las 9 plataformas, 6 proveedores y dependencias | 1–3 | propuesta | entrega temprana, antes del diseño; antes del diseño |
| 1.2.3 | Levantamiento de procesos, reglas de negocio y volumetría declarada | 1–3 | propuesta | antes del diseño |
| 1.2.4 | Catálogo de requerimientos y matriz de trazabilidad | 1–18 | propuesta | mientras dura el desarrollo; tras el levantamiento |
| 1.2.6 | Línea base de alcance por etapa, con exclusiones y supuestos | 3–4 | propuesta | cierra el levantamiento |
| 1.2.7 | Estudio de decisión con costeo sobre etiquetas electrónicas de precio | 2–5 | propuesta | OP-01 a OP-05 |
| 1.2.8 | Estudio de decisión con costeo sobre el sistema de almacenes de Concepción | 2–6 | propuesta | OP-08, OP-09 |
| 1.2.9 | Estudio de decisión con costeo sobre el destino de las plataformas | 2–5 | propuesta | decide el destino de las plataformas |
| 1.2.10 | Propuesta de criterios del cupo preaprobado para la filial emisora | 3–5 | propuesta | sd-03, 3.2.3: la filial emisora fija los criterios antes de la prueba de los meses 6 y 7 |

### Rama 1.3

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.3.1 | Documento de arquitectura con cinco vistas y catálogo de decisiones | 2–4 | propuesta | arquitectura cerrada en el mes 4 (EDT original); idem |
| 1.3.3 | Arquitectura física con emplazamiento por componente justificado | 2–4 | propuesta | idem |
| 1.3.4 | Modelo de datos con dominios segregados Retail y Emisor, frontera documentada y políticas de retención | 2–4 | propuesta | idem |
| 1.3.5 | Contratos de integración versionados y su gobierno | 3–4 | propuesta | idem |
| 1.3.6 | Especificación del modo desconectado de 24 horas y de la sincronización tras la reconexión | 3–4 | propuesta | idem |
| 1.3.7 | Modelo de capacidad y dimensionamiento | 3–4 | propuesta | idem |
| 1.3.8 | Especificación y costeo de las obras de infraestructura del cliente | 3–6 | propuesta | el cliente necesita plazo para ejecutar las obras |

### Rama 1.4

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.4.1 | Entorno de nube con infraestructura como código, subredes privadas y etiquetado de costos | 3–6 | propuesta | plataforma base lista en el mes 6 (EDT original) |
| 1.4.2 | Configuración del borde por sitio y certificación de la red segmentada en las 13 tiendas que no la tienen | 4–12 | propuesta | primero las tres tiendas del piloto del punto de venta (meses 6 y 7) y después el resto, antes de la marcha blanca; antes del piloto de tiendas |
| 1.4.3 | Entorno dedicado del ámbito emisor con segregación física y lógica acreditada | 4–8 | propuesta | ámbito emisor |
| 1.4.4 | Ambientes de desarrollo, calidad, preproducción, producción y recuperación ante desastres | 1–12 | contrato | Art. 17: ambientes habilitados dentro de la Etapa 1 (meses 1 a 12) |
| 1.4.5 | Plataforma de observabilidad unificada con catálogo de alertas | 4–8 | propuesta | antes de las primeras pruebas |
| 1.4.6 | Plataforma de integración y entrega continuas con infraestructura como código | 3–5 | propuesta | antes del desarrollo en curso |
| 1.4.7 | Licenciamiento de terceros a nombre del cliente | 2–6 | propuesta | a nombre del cliente |
| 1.4.8 | Especificación de hardware y dispositivos de terreno para adquisición del cliente | 3–6 | propuesta | el cliente adquiere después |
| 1.4.9 | Plano y especificación del recinto técnico del centro de datos y coordinación de su obra civil de separación | 2–6 | propuesta | RT-06.03; RT-06.06: el cliente ejecuta la obra |
| 1.4.11 | Plan de cierre de la brecha del centro de datos frente al informe interno de 2024 | 2–5 | propuesta | informe de 2024 |
| 1.4.12 | Sistemas de energía y climatización del centro de datos | 6–12 | propuesta | listo antes de la marcha blanca; idem |
| 1.4.14 | Sistemas de seguridad física del centro de datos y espacio de operación del personal | 6–12 | propuesta | idem |
| 1.4.17 | Solución de respaldo en operación con custodia de medios | 6–12 | propuesta | RT-07.09; RT-06.26 |

### Rama 1.5

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.5.1.1 | Precio: cambio, propagación, consulta e historial | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.1.2 | Etiquetas de exhibición y discrepancias de precio | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.1.5 | Promociones y su vigencia | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.1.6 | Maestro de artículos y reportes de calidad | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.2.1 | Propuesta diaria de reposición y su ajuste | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.2.2 | Órdenes de reposición a proveedores | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.2.3 | Transferencias y recepción de mercadería | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.3.1 | Disponible: cálculo, traza y consulta | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.3.2 | Reservas de existencia para el canal digital | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.3.4 | Conteo, exactitud del inventario, merma y probador | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.3.7 | Suspensión y degradación de la publicación por categoría | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.3.8 | Integración de existencias con el sistema de almacenes y con las planillas de Concepción | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.4.1 | Promesa de entrega, punto de despacho y elegibilidad del stock | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.4.2 | Preautorización, cobro y anulación del pago del pedido | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.4.3 | Resolución de pedidos sin existencia, reasignación y alternativas al cliente | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.4.4 | Estado único del pedido y sus consultas | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.4.5 | Seguimiento y cumplimiento de la promesa de entrega | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.5.1 | Punto de venta nuevo: registro y cobro de ventas, reversas, cierre de caja y medios de pago | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.5.2 | Punto de venta con operación sin conexión: reconciliación y validación posterior | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.5.6 | Ventas del canal digital y enrutamiento de los documentos tributarios al sistema de gestión empresarial | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.5.7 | Cobro con la tarjeta de la casa | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.6.1 | Cálculo de la base de comisión | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.6.2 | Entrega de la base de comisión al sistema de remuneraciones | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.6.3 | Revisión de la atribución de comisiones | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.7.1 | Existencia declarada por el vendedor y su publicación | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.7.2 | Evaluación de vendedores y su consulta | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.7.4 | Devoluciones, base de comisión y liquidación de marketplace | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.7.5 | Identificación del vendedor y separación de la existencia propia | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.8.1 | Atención de garantía legal en el mesón, con sus plazos | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.8.2 | Devolución y aptitud de la unidad devuelta | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.8.3 | Resolución al consumidor y recuperación contra el tercero responsable | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.9.1 | Consolidación de los registros de clientes | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.9.2 | Puntos y sincronización con el sistema de fidelización | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.9.3 | Segmentos y campañas con atributos comerciales | 13–18 | contrato | Art. 17: desarrollo de la etapa 2 |
| 1.5.10.1 | Evaluación crediticia, apertura de tarjeta y ampliación de cupo | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.10.2 | Simulación del costo total del crédito con la tasa máxima vigente | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.10.4 | Autorización de compra a cuotas sin enlace y sus topes | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.11.1 | Mora y gestión de cobranza | 1–18 | contrato | Art. 17 y Anexo D 24: cartera migra en las dos etapas |
| 1.5.11.2 | Repactación, pagos y estado de cuenta | 1–18 | contrato | Art. 17 y Anexo D 24: cartera migra en las dos etapas |
| 1.5.11.5 | Conciliación diaria y convivencia con la plataforma de crédito de 2011 | 1–18 | contrato | Art. 17 y Anexo D 24: cartera migra en las dos etapas |
| 1.5.12.1 | Información precontractual entregada, aceptada y consultable | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.12.2 | Consentimiento de modificaciones de condiciones y su enlace con la cobranza | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.12.3 | Reconstrucción y recuperación de la evidencia del consentimiento | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.13.1 | Inventario de flujos de cruce autorizados y registro de los cruces | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.13.2 | Rechazo de cruces no autorizados entre los ámbitos | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.13.3 | Correspondencia de identificadores y evaluación de impacto sobre la frontera | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.14.1 | Identidad individual y administración de identidades, roles y ámbitos | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.14.2 | Habilitación, revocación y conciliación de accesos | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.14.5 | Orden de degradación y ventanas de congelamiento | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.14.6 | Plataforma de integración y convivencia con el sistema central de 2009 | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |
| 1.5.14.7 | Observabilidad y capacidad analítica | 1–12 | contrato | Art. 17: desarrollo de la etapa 1 |

### Rama 1.6

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.6.1 | Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración | 2–5 | propuesta | catálogo de interfaces |
| 1.6.2 | Rediseño de las integraciones de la Etapa 1 (precios y existencia, crédito con el sistema de gestión empresarial, cobranza y prevención de pérdidas) | 5–18 | propuesta | interfaces de la Etapa 1; cartera: Etapa 1 y 2; interfaz de la Etapa 1 |
| 1.6.3 | Rediseño de las integraciones de la Etapa 2 (pedidos, marketplace y fidelización) | 13–18 | propuesta | interfaz de la Etapa 2 |
| 1.6.9 | Canal de intercambio con los proveedores de mercadería | 13–18 | propuesta | abastecimiento es de la Etapa 2 |
| 1.6.10 | Entrega de reportes a las autoridades fiscalizadoras | 8–12 | propuesta | la filial emisora está en la Etapa 1 |
| 1.6.11 | Certificación de las integraciones con evidencia de conciliación | 10–18 | propuesta | certificación de las dos etapas |
| 1.6.12 | Modalidad de contingencia tributaria aprobada y probada con el ERP/DTE | 4–6 | propuesta | sd-03, 3.4.5: aprobada y probada antes de comprometer la operación sin enlace; antes del piloto |

### Rama 1.7

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.7.1 | Plan de migración con estrategia de corte y de retorno e inventario de datos históricos | 2–4 | propuesta | antes de migrar; RT-05.15 |
| 1.7.3 | Maestro de artículos saneado y validado (268.000 referencias) | 4–10 | propuesta | antes de la marcha blanca |
| 1.7.4 | Corte de inventario en las 24 instalaciones que no cierran | 11–15 | propuesta | corte antes del paso a producción |
| 1.7.5 | Migración del histórico comercial (ventas y pedidos) | 8–15 | propuesta | antes del paso a producción |
| 1.7.6 | Migración del padrón de clientes deduplicado, de los vendedores y de las liquidaciones | 14–19 | propuesta | clientes Retail es de la Etapa 2 |
| 1.7.7 | Migración de la cartera viva (620.000 clientes) con sus actas de conciliación | 10–21 | contrato | Anexo D, resultado 24: primera parte en el mes 16 y segunda en el mes 21; acompaña a la migración |
| 1.7.9 | Repositorio de consulta de datos históricos no migrados | 10–16 | propuesta | antes del paso a producción de la Etapa 1 |
| 1.7.10 | Plan de retiro de la plataforma de originación y cobranza de 2011 | 14–18 | propuesta | antes del retiro |
| 1.7.11 | Plataforma de originación y cobranza de 2011 fuera de servicio | 22–22 | contrato | sd-03 (operación): fecha objetivo octubre de 2028 = mes 22 |
| 1.7.12 | Sistema central de retail de 2009 retirado | 21–56 | contrato | sd-03 (operación): se retira durante la operación; fecha por definir |
| 1.7.13 | Sustitución del punto de venta de 2014 tienda por tienda y su retiro | 8–16 | propuesta | sd-03, 3.3.1: tienda por tienda tras acreditar la operación sin conexión (piloto de los meses 6 y 7) y antes del paso a producción |
| 1.7.14 | Actas de compuerta por tramo de la cartera de crédito | 12–21 | propuesta | sd-03, 3.2.3: la compuerta de cada tramo se cierra antes del paso a producción de la etapa (meses 16 y 21) |

### Rama 1.8

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.8.1 | Plan de seguridad, matriz de controles y modelo de amenazas | 1–5 | propuesta | base de la seguridad; tras la arquitectura |
| 1.8.3 | Declaración de superficie de exposición y plan de respuesta a incidentes | 4–8 | propuesta | tras el diseño; antes de la marcha blanca |
| 1.8.5 | Modelo de identidad, matriz de roles y segregación de funciones, incluido el ámbito emisor | 2–5 | propuesta | tras la arquitectura |
| 1.8.6 | Cifrado y tokenización de los medios de pago | 4–10 | propuesta | RNF-33, RNF-34 |
| 1.8.7 | Protección de datos personales y matriz de cumplimiento normativo | 3–8 | propuesta | Ley 21.719; tras el diseño |
| 1.8.9 | Informe de pruebas de intrusión y plan de remediación | 10–18 | propuesta | antes de la certificación de cada etapa |
| 1.8.10 | Informe de diligencia del proveedor de nube | 2–4 | propuesta | antes de elegir el proveedor de nube |
| 1.8.11 | Atestación de la cadena de suministro y revisión de la arquitectura de confianza cero | 4–12 | propuesta | RNF-70, RNF-71; RNF-73 |

### Rama 1.9

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.9.1 | Plan de pruebas con niveles, tipos, ambientes, datos y calendario | 2–4 | propuesta | antes de probar |
| 1.9.2 | Estándares de codificación, revisión por pares y puertas de calidad | 1–6 | propuesta | antes del desarrollo en curso; antes de programar |
| 1.9.3 | Batería de pruebas funcionales y de requisitos no funcionales | 5–18 | propuesta | durante el desarrollo de las dos etapas |
| 1.9.4 | Pruebas de desempeño, resiliencia y recuperación ante desastres | 9–18 | propuesta | antes de la certificación de cada etapa; idem |
| 1.9.6 | Ensayo de la estrategia de degradación del evento anual | 14–21 | contrato | Anexo D, resultado 25: ensayo del orden de degradación en el mes 16 y prueba de carga completa en el mes 21 |
| 1.9.7 | Informes de aceptación por el usuario y de verificación de los 28 criterios de aceptación del caso | 11–21 | propuesta | aceptación por etapa |
| 1.9.8 | Certificación de calidad de la Etapa 1 | 12–12 | contrato | Art. 17: la certificación va dentro del desarrollo de la Etapa 1 (meses 1 a 12) |
| 1.9.9 | Certificación de calidad de la Etapa 2 | 18–18 | contrato | Art. 17: cierre del desarrollo de la Etapa 2 en el mes 18 |
| 1.9.11 | Informe de la prueba del corte de enlace provocado de 24 horas con retorno ensayado en el piloto | 6–7 | contrato | sd-03, 3.2.3: corte de enlace de 24 horas en una tienda del piloto, en los meses 6 y 7 |
| 1.9.12 | Informe de evaluación de comercio electrónico y fidelización con las pruebas de la Etapa 1 | 9–12 | propuesta | sd-03, 3.3.1: con las pruebas de la primera etapa y antes de la ola que dependa de la plataforma |
| 1.9.13 | Informe de pruebas de tareas del punto de venta con cajeros nuevos y experimentados | 5–7 | propuesta | sd-03, 3.4.6: antes del despliegue y del piloto |
| 1.9.14 | Informe de pruebas de comprensión de precios, entrega e información crediticia con clientes y titulares | 12–20 | propuesta | sd-03, 3.4.6: precios, entrega e información crediticia de las dos etapas |

### Rama 1.10

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.10.1 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | — | depende de las innovaciones que se confirmen (sd-13) |
| 1.10.2 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | — | depende de las innovaciones que se confirmen (sd-13) |
| 1.10.3 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | — | depende de las innovaciones que se confirmen (sd-13) |
| 1.10.4 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | — | depende de las innovaciones que se confirmen (sd-13) |
| 1.10.5 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | — | depende de las innovaciones que se confirmen (sd-13) |

### Rama 1.11

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.11.1 | Plan de implantación con procedimiento de despliegue gradual y de reversión probado | 3–12 | propuesta | T-18; se actualiza; antes de la marcha blanca |
| 1.11.3 | Configuración y certificación de los sitios: 22 tiendas, 2 centros de distribución, 380 líneas de caja, 640 terminales y el nodo de borde de cada tienda | 9–18 | propuesta | sitios de la Etapa 1 antes del mes 13 y de la Etapa 2 antes del mes 19 |
| 1.11.4 | Plan de convivencia entre la Etapa 1 y la Etapa 2 con una única fuente de verdad | 15–18 | propuesta | Art. 17.2 fija la convivencia en los meses 19 y 20; el plan va antes |
| 1.11.5 | Piloto del punto de venta en tres tiendas | 6–7 | contrato | sd-03, 3.2.3: el piloto del punto de venta es de los meses 6 y 7 |

### Rama 1.12

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.12.1 | Plan de la marcha blanca de la Etapa 1 | 10–12 | propuesta | antes de la marcha blanca |
| 1.12.2 | Informe de resultados y evidencia de cierre de la marcha blanca de la Etapa 1 | 15–16 | contrato | Art. 17: la marcha blanca de la Etapa 1 termina en el mes 15; Art. 17.3: condiciones de cierre |
| 1.12.4 | Acta de aceptación de la Etapa 1 | 16–16 | contrato | Art. 17: paso a producción en el mes 16 |
| 1.12.5 | Plan de la marcha blanca de la Etapa 2, en convivencia con la Etapa 1 en producción | 16–18 | propuesta | antes de la marcha blanca de la Etapa 2 |
| 1.12.6 | Informe de resultados de la marcha blanca de la Etapa 2 | 20–20 | contrato | Art. 17: la marcha blanca de la Etapa 2 termina en el mes 20 |
| 1.12.7 | Acta de aceptación final y garantía de correcto funcionamiento | 21–21 | contrato | Art. 17: aceptación final en el mes 21; se activa con la aceptación final |
| 1.12.9 | Informe del soporte de estabilización posterior a la puesta en marcha | 16–24 | propuesta | tras cada paso a producción |

### Rama 1.13

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.13.1 | Plan de gestión del cambio con diagnóstico por perfil y medición de adopción | 3–6 | propuesta | antes de capacitar |
| 1.13.2 | Plan de capacitación por rol y materiales editables en español | 5–8 | propuesta | antes de capacitar |
| 1.13.3 | Registro de capacitación ejecutada y certificación de administradores y equipo técnico, condición de cierre de cada marcha blanca | 10–20 | propuesta | Art. 17.3: la capacitación certificada es condición de cierre de cada marcha blanca (meses 15 y 20) |
| 1.13.4 | Informe de acompañamiento en puesto para el personal de tienda, temporero y externo | 13–24 | propuesta | tras el paso a producción de cada etapa |
| 1.13.5 | Plan de comunicación a los clientes de la cartera por tramo | 10–21 | propuesta | sd-03, 3.2.3: antes del primer tramo y de cada compuerta |

### Rama 1.14

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.14.1 | Documentación técnica y funcional con inventario de componentes de software | 1–56 | propuesta | continua, versión final al cierre; desde el primer artefacto desplegado |
| 1.14.3 | Transferencia tecnológica de código fuente, artefactos de construcción, scripts de infraestructura y procedimientos de despliegue | 48–56 | propuesta | Art. 77.1: programa de transferencia hacia el cierre |
| 1.14.4 | Base de conocimiento y manuales de operación | 10–56 | propuesta | desde la marcha blanca; antes de operar |
| 1.14.6 | Plan de Reversibilidad con exportación en formatos abiertos | 1–3 | contrato | Art. 77.2: dentro de los primeros noventa días; se actualiza cada año |
| 1.14.7 | Acta de cierre, traspaso final y acompañamiento de reversibilidad | 56–56 | contrato | Art. 77.2: noventa días después del cierre, fuera de los 56 meses; cierre del contrato |
| 1.14.9 | Informe de lecciones aprendidas del proyecto | 56–56 | propuesta | cierre del contrato |
| 1.14.10 | Protocolo de aceptación de entregas y del producto final | 1–3 | propuesta | antes de la primera aceptación |

### Rama 1.15

| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |
| :-- | :-- | :-- | :-- | :-- |
| 1.15.1 | Mesa de servicio de tres niveles en operación | 21–56 | contrato | Art. 17: operación de los meses 21 a 56 |
| 1.15.2 | Informes periódicos de nivel de servicio y de certificaciones | 21–56 | contrato | Art. 17: operación de los meses 21 a 56 |
| 1.15.3 | Pruebas periódicas de recuperación ante desastres | 21–56 | contrato | sd-03: la recuperación ante desastres se prueba dos veces al año |
| 1.15.4 | Mantención correctiva, preventiva y evolutiva | 21–56 | contrato | Art. 17: operación de los meses 21 a 56 |
| 1.15.6 | Infraestructura en operación con su informe de gestión | 21–56 | contrato | Art. 17: operación de los meses 21 a 56 |
| 1.15.8 | Jornadas anuales de actualización y capacitación de personal nuevo | 21–56 | contrato | Art. 17: operación de los meses 21 a 56 |

## 3. Barras

```
1.1.1    ███·····················································
1.1.2    ███·····················································
1.1.3    ████████████████████████████████████████████████████████
1.1.4    ████████████████████████████████████████████████████████
1.1.6    ███·····················································
1.1.7    ████████████████████████████████████████████████████████
1.1.9    ···█████████████████████████████████████████████████████
1.1.10   ████████████████████████████████████████████████████████
1.1.11   ████████████████████████████████████████████████████████
1.1.12   █·······················································
1.1.13   ███·····················································
1.1.14   ··███···················································
1.2.1    ███·····················································
1.2.3    ███·····················································
1.2.4    ██████████████████······································
1.2.6    ··██····················································
1.2.7    ·████···················································
1.2.8    ·█████··················································
1.2.9    ·████···················································
1.2.10   ··███···················································
1.3.1    ·███····················································
1.3.3    ·███····················································
1.3.4    ·███····················································
1.3.5    ··██····················································
1.3.6    ··██····················································
1.3.7    ··██····················································
1.3.8    ··████··················································
1.4.1    ··████··················································
1.4.2    ···█████████············································
1.4.3    ···█████················································
1.4.4    ████████████············································
1.4.5    ···█████················································
1.4.6    ··███···················································
1.4.7    ·█████··················································
1.4.8    ··████··················································
1.4.9    ·█████··················································
1.4.11   ·████···················································
1.4.12   ·····███████············································
1.4.14   ·····███████············································
1.4.17   ·····███████············································
1.5.1.1  ████████████············································
1.5.1.2  ████████████············································
1.5.1.5  ████████████············································
1.5.1.6  ████████████············································
1.5.2.1  ············██████······································
1.5.2.2  ············██████······································
1.5.2.3  ············██████······································
1.5.3.1  ████████████············································
1.5.3.2  ████████████············································
1.5.3.4  ████████████············································
1.5.3.7  ████████████············································
1.5.3.8  ████████████············································
1.5.4.1  ············██████······································
1.5.4.2  ············██████······································
1.5.4.3  ············██████······································
1.5.4.4  ············██████······································
1.5.4.5  ············██████······································
1.5.5.1  ████████████············································
1.5.5.2  ████████████············································
1.5.5.6  ████████████············································
1.5.5.7  ████████████············································
1.5.6.1  ············██████······································
1.5.6.2  ············██████······································
1.5.6.3  ············██████······································
1.5.7.1  ············██████······································
1.5.7.2  ············██████······································
1.5.7.4  ············██████······································
1.5.7.5  ············██████······································
1.5.8.1  ············██████······································
1.5.8.2  ············██████······································
1.5.8.3  ············██████······································
1.5.9.1  ············██████······································
1.5.9.2  ············██████······································
1.5.9.3  ············██████······································
1.5.10.1 ████████████············································
1.5.10.2 ████████████············································
1.5.10.4 ████████████············································
1.5.11.1 ██████████████████······································
1.5.11.2 ██████████████████······································
1.5.11.5 ██████████████████······································
1.5.12.1 ████████████············································
1.5.12.2 ████████████············································
1.5.12.3 ████████████············································
1.5.13.1 ████████████············································
1.5.13.2 ████████████············································
1.5.13.3 ████████████············································
1.5.14.1 ████████████············································
1.5.14.2 ████████████············································
1.5.14.5 ████████████············································
1.5.14.6 ████████████············································
1.5.14.7 ████████████············································
1.6.1    ·████···················································
1.6.2    ····██████████████······································
1.6.3    ············██████······································
1.6.9    ············██████······································
1.6.10   ·······█████············································
1.6.11   ·········█████████······································
1.6.12   ···███··················································
1.7.1    ·███····················································
1.7.3    ···███████··············································
1.7.4    ··········█████·········································
1.7.5    ·······████████·········································
1.7.6    ·············██████·····································
1.7.7    ·········████████████···································
1.7.9    ·········███████········································
1.7.10   ·············█████······································
1.7.11   ·····················█··································
1.7.12   ····················████████████████████████████████████
1.7.13   ·······█████████········································
1.7.14   ···········██████████···································
1.8.1    █████···················································
1.8.3    ···█████················································
1.8.5    ·████···················································
1.8.6    ···███████··············································
1.8.7    ··██████················································
1.8.9    ·········█████████······································
1.8.10   ·███····················································
1.8.11   ···█████████············································
1.9.1    ·███····················································
1.9.2    ██████··················································
1.9.3    ····██████████████······································
1.9.4    ········██████████······································
1.9.6    ·············████████···································
1.9.7    ··········███████████···································
1.9.8    ···········█············································
1.9.9    ·················█······································
1.9.11   ·····██·················································
1.9.12   ········████············································
1.9.13   ····███·················································
1.9.14   ···········█████████····································
1.10.1   ························································  por definir
1.10.2   ························································  por definir
1.10.3   ························································  por definir
1.10.4   ························································  por definir
1.10.5   ························································  por definir
1.11.1   ··██████████············································
1.11.3   ········██████████······································
1.11.4   ··············████······································
1.11.5   ·····██·················································
1.12.1   ·········███············································
1.12.2   ··············██········································
1.12.4   ···············█········································
1.12.5   ···············███······································
1.12.6   ···················█····································
1.12.7   ····················█···································
1.12.9   ···············█████████································
1.13.1   ··████··················································
1.13.2   ····████················································
1.13.3   ·········███████████····································
1.13.4   ············████████████································
1.13.5   ·········████████████···································
1.14.1   ████████████████████████████████████████████████████████
1.14.3   ···············································█████████
1.14.4   ·········███████████████████████████████████████████████
1.14.6   ███·····················································
1.14.7   ·······················································█
1.14.9   ·······················································█
1.14.10  ███·····················································
1.15.1   ····················████████████████████████████████████
1.15.2   ····················████████████████████████████████████
1.15.3   ····················████████████████████████████████████
1.15.4   ····················████████████████████████████████████
1.15.6   ····················████████████████████████████████████
1.15.8   ····················████████████████████████████████████
```

## 4. Precedencias y ruta crítica

La ruta crítica es la cadena de anclas del contrato, que no tiene holgura:

| Orden | Eslabón | Mes | Holgura |
| --: | :-- | --: | --: |
| 1 | Levantamiento y línea base de alcance (1.2) | 1 a 4 | 0 |
| 2 | Arquitectura y diseño (1.3) | 2 a 4 | 0 |
| 3 | Plataforma base y ambientes (1.4) | 3 a 10 | 0 |
| 4 | Desarrollo de la Etapa 1 (1.5, servicios de la Etapa 1) | 1 a 12 | 0 |
| 5 | Certificación de la Etapa 1 (1.9.8) | 12 | 0 |
| 6 | Marcha blanca de la Etapa 1 y sus condiciones de cierre (1.12.1 a 1.12.3) | 13 a 15 | 0 |
| 7 | Paso a producción de la Etapa 1 (1.12.4) | 16 | 0 |
| 8 | Desarrollo de la Etapa 2, en paralelo con los pasos 6 y 7 | 13 a 18 | 0 |
| 9 | Certificación de la Etapa 2 (1.9.9) | 18 | 0 |
| 10 | Marcha blanca de la Etapa 2 (1.12.5, 1.12.6) | 19 a 20 | 0 |
| 11 | Paso a producción de la Etapa 2, aceptación final e inicio de la operación (1.12.7) | 21 | 0 |

Los demás paquetes tienen holgura **sin calcular**: no hay horas ni duraciones de los paquetes que el UCP no cubre ni dotación, y una holgura inventada sería falsa. Se calcula cuando existan las planillas de tres valores y la dotación. Precedencias que se respetaron: el levantamiento antecede a la arquitectura; la arquitectura antecede a la plataforma base y a los ambientes; los ambientes antecedan a las pruebas de carga, resiliencia y recuperación; el desarrollo de una etapa antecede a su certificación, la certificación a la marcha blanca y esta al paso a producción; la capacitación certificada es condición de cierre de cada marcha blanca (Art. 17.3); los servicios de la Etapa 2 dependen de servicios de la Etapa 1 (sd-03, Tabla 3.1), así que ninguno empieza antes del mes 13.

## 5. Curva de horas del UCP por mes

Las horas del UCP (31.850 h) se reparten así dentro de la ventana de cada cuenta de software: el análisis (10 %, lectura B) en sus tres primeros meses, que es la ola de especificación de `21_ola_1_paquetes_trabajo.md`, y el 90 % restante en partes iguales en los meses siguientes. Es un supuesto de distribución: el UCP da el total, no el perfil dentro de la etapa. Las horas de los demás paquetes no están (esperan las planillas), por lo que esta curva es **parcial** y no es todavía la curva de dotación del T-15.

| Mes | Calendario | Etapa 1 (h) | Etapa 2 (h) | Cartera, etapas 1 y 2 (h) | Total (h) |
| --: | :-- | --: | --: | --: | --: |
| 1 | ene 2027 | 650 | 0 | 58 | 708 |
| 2 | feb 2027 | 650 | 0 | 58 | 708 |
| 3 | mar 2027 | 650 | 0 | 58 | 708 |
| 4 | abr 2027 | 1.951 | 0 | 104 | 2.054 |
| 5 | may 2027 | 1.951 | 0 | 104 | 2.054 |
| 6 | jun 2027 | 1.951 | 0 | 104 | 2.054 |
| 7 | jul 2027 | 1.951 | 0 | 104 | 2.054 |
| 8 | ago 2027 | 1.951 | 0 | 104 | 2.054 |
| 9 | sep 2027 | 1.951 | 0 | 104 | 2.054 |
| 10 | oct 2027 | 1.951 | 0 | 104 | 2.054 |
| 11 | nov 2027 | 1.951 | 0 | 104 | 2.054 |
| 12 | dic 2027 | 1.951 | 0 | 104 | 2.054 |
| 13 | ene 2028 | 0 | 354 | 104 | 458 |
| 14 | feb 2028 | 0 | 354 | 104 | 458 |
| 15 | mar 2028 | 0 | 354 | 104 | 458 |
| 16 | abr 2028 | 0 | 3.185 | 104 | 3.289 |
| 17 | may 2028 | 0 | 3.185 | 104 | 3.289 |
| 18 | jun 2028 | 0 | 3.185 | 104 | 3.289 |
| **Total** | | **19.505** | **10.617** | **1.728** | **31.850** |

Entre los meses 13 y 15 coexisten el análisis de la Etapa 2 (354 h por mes) y la marcha blanca de la Etapa 1 (sin horas del UCP: son del paso 7). El pico del software está en los meses 14 a 16, con 3.289 h por mes, 1.6 veces la carga del mes 8: la Etapa 2 concentra su construcción en los tres últimos meses del desarrollo porque el Art. 17 cierra el desarrollo en el mes 18. Eso, junto con la marcha blanca de la Etapa 1 y su paso a producción en el mes 16, es lo que el T-15 debe demostrar con dotación (Art. 17.2); sin el sd-12 queda como pregunta.

## 6. Pruebas de la puerta

- P8.3 (la curva por etapa cuadra con los meses 1 a 12, 13 a 18 y 21 a 56): las horas de la Etapa 1 están solo en los meses 1 a 12, las de la Etapa 2 solo en 13 a 18, la cartera en 1 a 18, y no hay horas del UCP en la operación. **Cumple** para las horas del UCP.
- Pasos a producción fuera de los congelamientos: **cumple**.
- P8.2 (personas en el pico frente a la dotación): **pendiente**; el sd-12 está fuera de esta entrega.
- Holguras de los paquetes que no están en la ruta crítica: **pendiente**, por falta de duraciones.

## 7. Supuestos y preguntas para el equipo, con sugerencia

| N.º | Pregunta o supuesto | Sugerencia |
| --: | :-- | :-- |
| 1 | Las ventanas de la rama 1.4 (infraestructura) y de los sistemas del centro de datos están en los meses 6 a 12 | Aceptar. El Art. 17 solo exige los ambientes dentro de los meses 1 a 12; la EDT original fijaba la plataforma base en el mes 6 |
| 2 | El software de cada etapa se reparte parejo por mes dentro de su ventana | Aceptar mientras no haya un plan de iteraciones. Cambiarlo solo desplaza la curva dentro de la etapa |
| 3 | La arquitectura se cierra en el mes 4 y la plataforma base en el mes 6, tomados de la EDT original | Aceptar como propuesta; no están en las Bases, porque los hitos del Formulario E-25 no se leen en las tablas |
| 4 | Los hitos de pago del Formulario E-25 no se anclan | Dejarlos así hasta que se repare la tabla de las Bases |
| 5 | La ventana de cada innovación queda por definir | Cerrarla con el sd-13; el Art. 28 exige las cinco y RT-26.02 pide el mes de cada una |
| 6 | El retiro del sistema central de 2009 no tiene fecha en el sd-03 | Fijarla con el escenario B por ola, después del mes 21; mientras tanto, ventana de operación |
| 7 | La marcha blanca de la Etapa 1 cae en congelamiento (enero a marzo de 2028) | Coordinar el plan de la marcha blanca con el calendario de congelamientos del paquete 1.1.6 |
| 8 | Los noventa días de acompañamiento de reversibilidad quedan después del mes 56 | Dejarlos como están: el Art. 77.2 los fija tras el cierre |
