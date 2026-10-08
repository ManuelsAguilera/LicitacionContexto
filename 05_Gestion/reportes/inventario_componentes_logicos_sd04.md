# Reevaluación del inventario lógico de SD-04

**Fecha:** 8 de octubre de 2026. **Estado:** matriz de revisión para validar antes de incorporarla a la redacción de SD-04.

La corrección sobre Azure y Google obliga a separar la **función lógica** de su **producto y lugar de despliegue**. El inventario se deriva del alcance de [SD-03](../../02_Propuesta/latex_final/sd-03.tex), del [SD-04 actual](../../02_Propuesta/latex_final/sd-04.tex) y del [Caso 09](../../00_Bases/Caso_09_Cadena_Multitienda.md). «Microservicio candidato» expresa una unidad de despliegue por comprobar; no agrega un servicio de negocio al catálogo de trece. «Existente» tampoco presupone que el software se aloje en el centro de datos del Cliente o en una nube ajena.

## Tabla integral de componentes lógicos

| ID | Ámbito | Componente lógico | Responsabilidad y autoridad | Tratamiento / unidad | Decisión pendiente |
| :--- | :--- | :--- | :--- | :--- | :--- |
| C-01 | Canal | POS nuevo, interfaz Retail | Venta, precio, disponibilidad y estado de sincronización visibles en caja. | Canal nuevo; no microservicio. | Probar periféricos y sustitución tienda por tienda. |
| C-02 | Canal | Sesión financiera en POS | Acceso por rol a originación o autorización, segregado de Retail. | Interfaz del Emisor; no repositorio Retail. | Definir flujo exacto y regla de crédito sin enlace. |
| C-03 | Canal | Comercio electrónico | Presentación, carro y entrada de pedidos del canal propio. | Plataforma vigente integrada inicialmente; decisión condicionada. | Conservar, remediar o sustituir tras pruebas de etapa 1. |
| C-04 | Canal | Atención y posventa | Interfaz para consulta y resolución de casos; consume servicios autorizados. | Interfaz nueva o integrada; no autoridad de casos. | Precisar vistas y usuarios. |
| C-05 | Canal | Acceso financiero del titular y operadores | Consulta y trámites permitidos por el Emisor. | Interfaz segregada del canal Retail. | Precisar vistas, accesibilidad y legado durante migración. |
| B-01 | Borde | Protección y exposición de canales | Protección perimetral, terminación cifrada y publicación controlada. | Capacidad de plataforma, no servicio de negocio. | Seleccionar controles según amenazas y puntos de acceso. |
| B-02 | Borde | API gateway | Entrada gobernada de APIs: identidad, cuotas, contratos, versiones y trazas. | Capacidad de plataforma; no sustituye adaptadores. | Verificar producto, nivel y región elegidos. |
| R:M-01 | Retail · Mercadería | Oferta comercial | Artículos, atributos, precios, promociones, vigencias y publicación por canal. | Unidad lógica propia; uno o dos despliegues solo tras prueba. | Asegurar versión coherente entre precio y promoción; motor nuevo. |
| R:M-02 | Retail · Mercadería | Abastecimiento | Órdenes, transferencias, propuestas de reposición y recepción coordinada. | Servicio propio candidato. | WMS retiene ejecución física; Concepción requiere decisión propia. |
| R:M-03 | Retail · Mercadería | Existencias | Movimientos conciliados, reservas, disponible comprometible, conteos y ajustes. | Un microservicio transaccional candidato. | Mantener juntos los invariantes de stock; resolver venta local concurrente. |
| R:V-01 | Retail · Venta | Pedidos | Estado, promesa, asignación, seguimiento y coordinación de cumplimiento. | Microservicio candidato. | WMS prepara y despacha físicamente. |
| R:V-02 | Retail · Venta | Ventas | Venta, pago, reversa, caja y conciliación de operaciones locales/digitales. | Microservicio candidato. | ERP/DTE mantiene emisión tributaria. |
| R:V-03 | Retail · Venta | Comisiones | Atribución y base calculada por canal, vendedor y tienda. | Módulo propio extraíble. | ERP conserva remuneraciones. |
| R:V-04 | Retail · Venta | Gobierno de marketplace | Reglas y desempeño de vendedores; coordinación de oferta, pedidos y devoluciones. | Módulo propio extraíble. | Precisar escritura de liquidaciones en plataforma vigente. |
| R:CL-01 | Retail · Cliente | Posventa | Caso, devolución, inspección y destino de producto. | Microservicio candidato. | Reingreso al disponible solo tras inspección; DTE sigue en ERP. |
| R:CL-02 | Retail · Cliente | Clientes Retail | Identidad comercial deduplicada y preferencias Retail. | Unidad propia; no identidad financiera. | Fidelización conserva puntos, segmentos y campañas mientras convive. |
| F:C-01 | Emisor · Crédito | Originación y autorización | Solicitud, evaluación, cupo, decisión y autorización de compra. | Una unidad inicial por invariantes y latencia. | Abrir crédito solo con evidencia suficiente; definir contingencia. |
| F:C-02 | Emisor · Crédito | Cartera | Cuentas, saldo, cuotas, pagos, mora, cobranza y repactación. | Microservicio propio separado. | Migrar cartera por olas conciliadas desde 2011. |
| F:C-03 | Emisor · Crédito | Evidencia financiera | Información precontractual, consentimiento, firma y expediente versionado. | Microservicio/repositorio propio separado. | Fijar conservación, integridad, recuperación y acceso. |
| X-01 | Frontera | Gobierno de cruces | Catálogo de fichas, finalidad, campos mínimos, política y bitácora de decisiones. | Servicio de gobierno; controles aplicados en ambos extremos. | Aprobar jurídicamente cada flujo; no crear maestro común. |
| I-01 | Integración | Contratos síncronos | Reservas, autorización de compra y demás respuestas bloqueantes con plazo e idempotencia. | Patrón de interfaces entre autoridades. | Inventariar fallas, reversas y versiones de contrato. |
| I-02 | Integración | Apache Kafka propuesto | Transporte durable de hechos confirmados, segregado por Retail y Emisor. | Preferencia arquitectónica, no requisito de Bases ni autoridad transaccional. | Justificar casos de uso, elegir operación administrada o propia y réplica regional. |
| I-03 | Integración | Publicación transaccional / outbox | Persistir el evento junto a la operación confirmada y publicarlo sin pérdida. | Componente/patrón por productor. | Medir retraso y tratar publicaciones repetidas. |
| I-04 | Integración | Consumidores y tratamiento de errores | Deduplicación, reintento, cola de fallas y reproceso controlado. | Componentes por flujo; no un bus de decisiones. | Definir orden por agregado y efectos idempotentes. |
| I-05 | Integración | Adaptadores ERP/DTE y WMS | Traducción, confirmación y conciliación con las dos plataformas conservadas. | Adaptadores privados por contrato. | Levantar ubicación, interfaz y autoridad de cada registro. |
| I-06 | Integración | Adaptador marketplace | Intercambio con plataforma de terceros sin duplicar sus funciones. | Adaptador privado. | Precisar liquidaciones y fallas de contraparte. |
| I-07 | Integración | Adaptadores de convivencia | Comercio electrónico, fidelización, Retail 2009 y crédito 2011. | Adaptadores temporales o permanentes según decisión de plataforma. | Retirar interfaz antigua solo tras conciliación por ola. |
| I-08 | Integración | Integraciones de actores externos | Contratos con transportistas y vendedores externos donde aplique. | Interfaces; no reconstrucción de su logística. | Confirmar contratos y alcance de datos expuestos. |
| L-01 | Tienda | Caché local de operación | Oferta vigente, promociones y existencia local necesaria para continuidad. | Componente del nodo local; datos de lectura con vigencia. | Definir cuota de venta desconectada frente a reserva digital concurrente. |
| L-02 | Tienda | Diario transaccional local | Registro durable de ventas y estados pendiente, enviado, confirmado y en conflicto. | Componente local con autonomía mínima de 24 horas. | Dimensionar folios, energía, almacenamiento y modalidad fiscal aprobada. |
| L-03 | Tienda | Sincronizador y conciliador | Reenvío idempotente y resolución de conflictos al regresar el enlace. | Componente local y contraparte R:V-02. | Ensayar 24 horas y drenaje sin duplicidad ni pérdida. |
| D-01 | Datos | Repositorios transaccionales Retail | Escritura por autoridad de R:M/R:V/R:CL, con permisos separados por contexto. | Datos propios; sin lecturas directas transversales. | Elegir motor, HA y recuperación por servicio. |
| D-02 | Datos | Repositorios transaccionales Emisor | Escritura de originación y cartera bajo el Emisor. | Datos propios segregados de Retail. | Autorizar ubicación y replicación financiera. |
| D-03 | Datos | Repositorios de evidencia y auditoría | Expedientes F:C-03 y bitácora X-01 con políticas de acceso distintas. | Almacenes propios; no perfil unificado. | Definir retención, inmutabilidad y custodia por conjunto. |
| A-01 | Analítica | Ingesta y proyecciones | Publicar conjuntos de lectura desde hechos o contratos autorizados. | Canal de datos de solo lectura. | Fijar latencia, calidad, reconciliación y linaje. |
| A-02 | Analítica | Lago de datos Retail | Datos y permisos para análisis comercial. | Espacio analítico propio, sin datos financieros por defecto. | Definir datasets, retención y cifrado. |
| A-03 | Analítica | Lago de datos Emisor | Datos y permisos para análisis crediticio autorizado. | Espacio analítico independiente. | Definir residencia y acceso de detalle. |
| A-04 | Analítica | Motor y modelo semántico de consulta | Indicadores reproducibles sobre datos autorizados. | Capacidad analítica, no base transaccional. | Seleccionar producto regional; validar rendimiento y segregación. |
| A-05 | Analítica | Tableros y autoservicio BI | Exploración, detalle, exportación e informes programados por rol. | Interfaz analítica Retail/Emisor separada. | Probar controles también en exportación y programación. |
| A-06 | Analítica | Catálogo, calidad y linaje | Origen, definiciones y transformaciones de cada indicador. | Gobierno de datos transversal con acceso segregado. | Identificar custodios y reglas de publicación. |
| M-01 | ML Retail | Predicción de conteos y margen | Priorizar conteos y estimar descuento de seguridad desde observaciones reales. | Procesador de apoyo; no escribe ATP ni ajustes. | Medir precisión y beneficio frente a regla actual. |
| M-02 | ML Retail | Clasificación de causas de merma | Sugerir causa de diferencia con evidencia para revisión humana. | Procesador de apoyo; no cierra ajustes. | Validar etiquetas, métricas por clase y sesgos. |
| M-03 | ML Retail | Gobierno y operación de modelos | Versiones, entradas/salidas, monitoreo de deriva, reentrenamiento y apagado. | Capacidad transversal de ML sujeta a RT-18. | Aprobar datos, supervisión y etapa de entrega. |
| S-01 | Seguridad | Identidad, federación y autorización | Personas y servicios por rol, entidad, finalidad y recurso. | Capacidad transversal; Retail y Emisor segregados. | Confirmar directorio existente y atributos necesarios. |
| S-02 | Seguridad | Claves, secretos y cifrado | Custodia de credenciales y protección de datos en tránsito y reposo. | Capacidad transversal con separación de ámbitos. | Definir titularidad y rotación de claves. |
| O-01 | Operación | Telemetría, auditoría y alertas | Correlación de solicitud, evento y efecto, sin volcar datos sensibles. | Capacidad transversal. | Establecer SLO, retención y respuesta por responsable. |
| O-02 | Operación | Entrega e infraestructura como código | Construcción, pruebas, firma, configuración y despliegue trazables. | Capacidad de plataforma; no servicio de negocio. | Elegir canal y roles de operación por nube. |
| P-01 | Plataforma existente | ERP/DTE | Contabilidad, remuneraciones y emisión tributaria exclusiva. | **Conservar e integrar**. | Alojamiento y contratos por acreditar. |
| P-02 | Plataforma existente | WMS principal | Ubicaciones, preparación y despacho físicos. | **Conservar e integrar**. | No asumir extensión a Concepción. |
| P-03 | Plataforma existente | Marketplace vigente | Plataforma de terceros, vendedores y liquidaciones. | **Conservar e integrar**. | Confirmar autoridad exacta de liquidación. |
| P-04 | Plataforma existente | Comercio electrónico vigente | Presentación, carro y canal propio durante la convivencia. | **Integrar; destino condicionado**. | Evaluar conservación, remediación o sustitución en etapa 1. |
| P-05 | Plataforma existente | Fidelización vigente | Puntos, segmentos y campañas durante convivencia. | **Integrar; destino condicionado**. | Transferencia atributo a atributo si se sustituye. |
| P-06 | Plataforma existente | Núcleo Retail 2009 | Autoridad temporal de funciones todavía no cortadas. | **Sustituir por olas**. | Conciliación y retorno por registro. |
| P-07 | Plataforma existente | Plataforma financiera 2011 | Crédito y cartera todavía no migrados. | **Sustituir por olas**. | Conciliación de cartera viva. |
| P-08 | Plataforma existente | POS 2014 | Caja de tiendas aún no migradas. | **Sustituir tienda por tienda**. | Distinguir terminal de dependencia central. |
| P-09 | Registro actual | Planillas y listas operativas | Precio/promoción, conteos, reposición u otros registros manuales. | **Retirar como autoridad al implantar los flujos nuevos**. | Concepción y etiquetas físicas requieren procedimiento; etiquetas electrónicas fuera de alcance. |

La fila C-03 representa el **canal** y su interfaz; P-04 identifica la plataforma que hoy lo presta, no un segundo sistema que deba adquirirse. P-01 a P-09 se muestran para hacer visible el límite de la solución, no para contarlas como microservicios propios. El Caso declara nueve plataformas, pero su tabla enumera ocho vigentes y un motor de precios inexistente; no se inventa una novena para cuadrar el texto.

## Revisión Azure–Google aplicada a la tabla

El proveedor se decide **después** de fijar las responsabilidades anteriores. En [SD-01](../../02_Propuesta/latex_final/sd-01.tex) Azure aparece como apoyo posible, todavía sin acreditar la condición de socio que exige el [artículo 34](../../00_Bases/Bases_Administrativas.md). Su prioridad documental no equivale a una selección técnica irrevocable.

| Componente lógico | Azure en Chile Central | Google Cloud en Santiago | Efecto sobre la decisión |
| :--- | :--- | :--- | :--- |
| I-02 Kafka | No se ha acreditado Kafka administrado en Chile Central; AKS implica operación propia; Event Hubs admite protocolo Kafka, pero no es Apache Kafka. | Managed Service for Apache Kafka está documentado. | Comparar carga de operación y compatibilidad real, no cambiar toda la nube por una sola pieza. |
| B-02 Gateway | API Management es candidato, pero debe verificarse el nivel disponible: la lista oficial de niveles v2 no incluye Chile Central. | Apigee documenta Santiago. | No prometer un nivel concreto de gateway en una región sin prueba. |
| D-01/D-02 PostgreSQL | Flexible Server figura en Chile Central; HA y estrategia de recuperación dependen de la configuración y región. | Cloud SQL figura en Santiago. | Probar recuperación y residencia por conjunto de datos. |
| A-02 a A-05 Analítica | Power BI está disponible en Chile Central; Fabric completo no lo está, por lo que el motor sobre el lago queda por elegir. | Cloud Storage, BigQuery y Looker son candidatos regionales. | Comparar funciones de BI, frontera y operación de extremo a extremo. |

Fuentes de disponibilidad: [regiones de Azure](https://learn.microsoft.com/azure/reliability/regions-list), [API Management por región](https://learn.microsoft.com/azure/api-management/api-management-region-availability), [Fabric por región](https://learn.microsoft.com/fabric/admin/region-availability), [PostgreSQL Flexible Server](https://learn.microsoft.com/azure/postgresql/overview), [Confluent Cloud por proveedor](https://docs.confluent.io/cloud/current/get-started/regions.html), [Event Hubs y Kafka](https://learn.microsoft.com/azure/event-hubs/apache-kafka-frequently-asked-questions), [Kafka administrado de Google](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations) y [Apigee por región](https://docs.cloud.google.com/apigee/docs/locations).

## Ajustes necesarios antes de incorporar la matriz a SD-04

1. **Corregir autoridades y etapas.** En SD-03, una frase de 3.2.1 atribuye a Clientes Retail el gobierno de fidelización con demasiada amplitud, aunque 3.3.2 conserva la escritura de puntos y campañas en la plataforma vigente. Clientes Retail aparece en etapa 2, pero la elegibilidad de promociones lo consulta antes: definir un adaptador temporal o adelantar la capacidad mínima. Precisar también quién escribe las liquidaciones del marketplace.
2. **Cerrar continuidad e integración.** Inventariar las catorce interfaces, fijar la cuota/regla de stock de tienda desconectada frente al canal digital y aprobar la modalidad fiscal de contingencia. No habilitar nueva originación ni aumento de cupo sin enlace mediante una suposición técnica.
3. **Completar vistas.** La figura 4.1 actual agrupa Retail y Emisor y omite nodos explícitos de borde, seguridad, observabilidad, lagos separados y ambos procesadores ML. La tabla permite descomponerla en vista general, Retail, Emisor, integración y tienda con la frontera visible, conforme a RT-02.01 y a la [rúbrica de revisión](../../80_Artefactos/revision_informe_1_rubrica_de_cierre.md).
4. **Asignar evidencia y etapa.** BI y los dos modelos ML están descritos como capacidades de apoyo, pero falta asignarles entrega, prueba y operación. La selección Azure/Google debe cerrarse por región, nivel de producto, recuperación, alianza acreditada y personal necesario para operar lo no administrado.
