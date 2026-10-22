# Capa de datos: decisiones y precisiones

Fecha: 22-10-2026. Estado documental: borrador de contexto para SD-04. Procedencia: revisión de la arquitectura lógica y decisiones acordadas en esta conversación. Selección de componentes cerrada para este registro; sin acreditación de despliegue, rendimiento, cumplimiento ejecutado ni revisión humana formal del subdocumento.

## 1. Alcance y precedencia de este registro

Este documento consolida los cambios de la capa de datos respecto de la figura 4.31 y sus antecedentes. El usuario decidió mantener Data Lake, cerrar la selección sin productos candidatos y conservar las capacidades exigidas por las Bases aunque se excluya una marca determinada.

La figura 4.31 y sus archivos describen un estado anterior que retiraba Data Lake. Este registro sustituye esa decisión para la siguiente edición de arquitectura. La incorporación efectiva a la oferta exige conciliar el texto LaTeX de SD-04, sus figuras, decisiones de arquitectura, T-11/T-12 y las dependencias con SD-03, SD-08, SD-09 y SD-13. Guardar esta nota no modifica esos entregables ni el catálogo oficial de requisitos.

Antecedentes:

- [Figura 4.31 y contexto](integracion-capa4-2026-10-22/README.md).
- [Integración y decisiones pendientes anteriores](integracion-capa4-2026-10-22/integracion-y-pendientes.md).
- [Análisis de la iteración horizontal](iteracion-horizontal-2026-10-22/analisis-y-decisiones.md).
- [Dimensionamiento preliminar y pruebas propuestas](iteracion-horizontal-2026-10-22/dimensionamiento-y-pruebas.md).

Las Bases y el Caso rigen sobre esta nota. Las decisiones propias se distinguen de las exigencias contractuales. No se asignan estados `revisado` o `congelado` ni se declara cumplimiento en T-12 por seleccionar una herramienta.

## 2. Selección cerrada

| Componente | Decisión | Responsabilidad definida |
|---|---|---|
| Azure Data Lake Storage Gen2 | Incluido; se restituye | Datos de origen autorizados, históricos, conjuntos depurados, reconstrucción analítica y conjuntos de entrenamiento. Almacenamientos independientes para Retail y Filial. |
| Azure Data Factory | Incluido | Coordinar cargas iniciales, extracciones autorizadas, cargas incrementales y dependencias entre trabajos de datos. Identidades y pipelines separados por ámbito. |
| Trabajadores Java/Spring en AKS | Incluidos | Ingestión de eventos, validación, transformación, deduplicación, conciliación y construcción de proyecciones. Estado durable y recuperación por trabajo. |
| PostgreSQL transaccional | Incluido | Datos oficiales de cada servicio y outbox local. Repositorios, roles y autoridades propios. |
| PostgreSQL analítico dedicado por ámbito | Incluido | Hechos, dimensiones y agregados para consultas de gestión, separados del almacenamiento operacional y del otro negocio. |
| Power BI | Incluido | Tableros y autoservicio con modelos semánticos documentados y permisos por ámbito. |
| Azure Managed Redis | Incluido | Caché operacional reconstruible de oferta y disponibilidad Retail. |
| PostgreSQL/pgvector | Incluido | Índice derivado del catálogo multimodal, bajo responsabilidad de Oferta. |
| OpenSearch autogestionado en Azure | Incluido | Búsqueda global por ámbito: texto completo, tolerancia a errores y facetas, con autorización y filtros de seguridad. |
| Blob Storage con políticas WORM | Incluido | Evidencia financiera y archivo de auditoría con custodia y políticas diferenciadas de los conjuntos de transformación. |
| Azure Backup y PITR de PostgreSQL | Incluidos | Copias de recuperación y restauración reciente, con política y ensayo por recurso. No implica cobertura automática del resto de la plataforma. |
| OpenMetadata autogestionado | Incluido; nueva incorporación | Catálogo, glosario, propietarios, clasificación, relaciones de linaje y resultados de calidad. Despliegues separados por ámbito. |
| MLflow autogestionado | Incluido; nueva incorporación | Registro de experimentos, parámetros, métricas, artefactos y versiones de modelos para las innovaciones Retail. |
| Trabajos Python en AKS y scikit-learn | Incluidos | Entrenamiento, evaluación y ejecución del modelo de conteo predictivo; referencias a conjuntos versionados y resultados registrados en MLflow. |
| Microsoft Purview | Excluido | Sus capacidades seleccionadas se cubren con OpenMetadata y la instrumentación de pipelines. |
| Azure Databricks | Excluido | Transformación cubierta por Data Factory, trabajadores y PostgreSQL; gestión de modelos cubierta por Python y MLflow. |
| Azure AI Search | Excluido | Búsqueda global cubierta por OpenSearch. |
| Microsoft Fabric | Excluido | Funciones necesarias repartidas entre Data Lake, Data Factory, trabajadores, PostgreSQL analítico y Power BI. |
| Azure Synapse | Excluido | Se mantiene la misma distribución explícita de almacenamiento, transformación y consulta. |

No se incorpora un catálogo de datos desarrollado desde cero: OpenMetadata sustituye esa propuesta anterior. Los repositorios de metadatos de OpenMetadata y MLflow son propios de esas herramientas, separados de los esquemas de negocio.

La selección de Python/scikit-learn concreta el conteo predictivo. No define por sí sola el modelo de representaciones de la búsqueda multimodal ni afirma que scikit-learn resuelva esa generación de representaciones.

## 3. Correspondencia con las Bases

La revisión de las Bases Administrativas, Transversales y del Caso no encontró una exigencia de usar Purview, Databricks, Azure AI Search, Fabric o Synapse por marca. Se preservan las capacidades requeridas.

| Capacidad | Exigencia identificada | Solución y precisión |
|---|---|---|
| Modelo, diccionario, propietarios y linaje | Art. 23 administrativo y RT-05.01 | OpenMetadata, modelos documentados y contratos versionados. El linaje documental es obligatorio. |
| Catálogo con linaje automatizado | RT-05.10 transversal, deseable | OpenMetadata y publicación automática de relaciones desde pipelines y trabajadores. Se adopta en la solución, diferenciando su carácter contractual. |
| Calidad de datos | Art. 23 y RT-05.04, obligatorio | Validación en captura; controles de completitud, exactitud y consistencia; saneamiento y conciliación; tablero de calidad para el Cliente. |
| Separación operacional y analítica | Art. 23 y RT-05.05, obligatorio | Repositorios analíticos dedicados y consultas de BI aisladas de la operación. |
| Migración verificable | RT-05.11 a RT-05.15 | Perfilado, reglas, ensayos, cortes, conciliación, reversión y acceso al histórico retenido. |
| Analítica y autoservicio | RT-05.25 a RT-05.29 | PostgreSQL analítico y Power BI; modelos semánticos y latencias por indicador. |
| Búsqueda documental y global | RT-16.15 y RT-16.27, obligatorios | OpenSearch e integración documental, con indexación de contenido y metadatos y respeto de permisos. La previsualización documental se mantiene como responsabilidad de Documentos. |
| Exportación completa y masiva | RT-05.06 y RT-16.28 a RT-16.30 | Trabajos asíncronos, formatos abiertos, manifiestos, filtros, auditoría y aviso. Incluye documentos y datos que no estén en el modelo analítico. |
| Gobierno de IA incorporada | RT-18.01 a RT-18.08 | Trabajos de entrenamiento/evaluación, MLflow, registro de decisiones humanas, desactivación y alternativa manual. La incorporación de IA activa estas obligaciones. |
| Innovaciones | Arts. 28 y 29 administrativos | Se preservan las cinco innovaciones y su trazabilidad con arquitectura, EDT y oferta económica. El conteo predictivo es una selección de OSS, no un producto impuesto por las Bases. |

Fuentes contractuales de lectura: [Bases Administrativas](../../00_Bases/Bases_Administrativas.md), [Bases Transversales](../../00_Bases/Bases_Transversales.md) y [Caso 09](../../00_Bases/Caso_09_Cadena_Multitienda.md). Las referencias son de trabajo; al trasladar afirmaciones particulares a la oferta se verificará el folio impreso conforme a `citas-proyecto`.

## 4. Autoridad, separación y consistencia

### 4.1 Autoridades de datos

Cada servicio conserva la autoridad de escritura sobre sus datos. Las cajas agrupadas por área representan una síntesis visual, no una autorización para compartir tablas, credenciales o consultas SQL entre servicios. La arquitectura física debe declarar bases o esquemas, roles y límites de recursos. Un repositorio propio no equivale automáticamente a un servidor físico por servicio.

Existencias confirma reservas y mantiene movimientos, ajustes y disponible comprometible. Oferta posee artículos, precios y publicaciones. Ventas registra la venta y su conciliación. Originación posee solicitudes, evaluaciones, cupos y autorizaciones; Cartera conserva cuentas, saldos, cuotas y cobros. Debe concretarse el contrato que impide que un cupo se comprometa dos veces o que ambos servicios mantengan autoridades incompatibles sobre el mismo valor.

Evidencia financiera conserva metadatos propietarios en PostgreSQL y archivos en Blob. Una carga parcial no permite declarar completo un expediente: se requieren estados de carga, verificación y conciliación de referencias. La etiqueta agrupada «Originación / evidencia» debe aclararse en la siguiente figura para evitar una propiedad compartida implícita.

### 4.2 Retail y Filial

La separación se aplica a datos operacionales, lagos, repositorios analíticos, índices de búsqueda, catálogos, documentos, claves, credenciales y copias de recuperación. Un símbolo de producto agregado no implica compartir recursos entre negocios.

X-01 conserva una bitácora mínima del cruce autorizado, con referencia, política y resultado. No crea un perfil de cliente unificado ni permite copiar cartera, mora o comportamiento de pago a Retail. Los catálogos también respetan la separación: nombres, esquemas, muestras y metadatos financieros pueden revelar información sensible.

MLflow se incorpora para las innovaciones Retail. Esta nota no agrega modelos financieros ni un despliegue MLflow de Filial sin una necesidad definida.

### 4.3 Consistencia y eventos

La operación y su outbox se confirman en una transacción local. La publicación posterior usa Service Bus propio del ámbito. Los consumidores mantienen deduplicación durable, versiones por agregado, tratamiento de huecos, reintentos y errores persistentes. La confirmación de un mensaje ocurre después de confirmar su efecto durable.

Los cambios en proyecciones no se publican como nuevos hechos de negocio. Service Bus no es el archivo histórico ni la única fuente para reconstruir el lago, los índices o los modelos analíticos. La reconstrucción requiere exportación autorizada, corte consistente, deltas, manifiestos y conciliación.

## 5. Recorridos y responsabilidades de procesamiento

| Recorrido | Flujo definido | Control principal |
|---|---|---|
| Histórico y cargas incrementales | Fuente autorizada → Data Factory y trabajadores → recepción en Data Lake → validación/transformación → conjuntos depurados → PostgreSQL analítico → Power BI | Corte, versión, conteos, sumas de control, permisos y linaje. |
| Hechos operacionales | Servicio y outbox → Service Bus del ámbito → trabajadores de ingesta/proyección → destinos autorizados | Idempotencia, versiones, atraso, errores y conciliación. |
| Búsqueda global | Fuentes autorizadas y proyectores → OpenSearch del ámbito → API de búsqueda | Identidad, filtros por documento/campo, actualización y revocación de permisos. |
| Catálogo multimodal | Oferta e imágenes autorizadas → trabajador de representaciones → pgvector → consulta de Oferta | Modelo/versiones, reconstrucción y confirmación de precio/disponible con el propietario. |
| Conteo predictivo | Históricos Retail autorizados → conjunto versionado → trabajo Python/scikit-learn → MLflow → recomendación en Existencias | Evaluación temporal, comparación con línea base, deriva y validación humana; sin ajuste automático de stock. |
| Gobierno | Conectores y ejecuciones de pipelines → API de OpenMetadata → catálogo y linaje del ámbito | Fuente, propietario, transformación, destino, corte y ejecución identificables. |

Data Factory coordina cargas y dependencias. Los trabajadores ejecutan las reglas propias. La ubicación del factory y la de su integration runtime deben declararse por separado: el primero conserva metadatos y el segundo determina dónde se ejecutan movimientos o actividades. Esta nota no acredita disponibilidad en una región ni autoriza tránsito internacional.

PostgreSQL analítico conserva modelos preparados para consulta; Data Lake conserva los conjuntos e históricos definidos por su finalidad. No se duplican todos los datos en ambos por defecto. Se documentará qué hechos, dimensiones, agregados y detalle permiten navegar desde cada indicador hasta su origen mediante una API autorizada.

La operación inmediata no depende de que termine una carga del lago o un refresco de Power BI. Los plazos del Caso se miden en sus recorridos completos: disponible publicado dentro de 30 segundos desde la venta, precios en cajas y canal digital dentro de cinco minutos, exactitud por categoría diaria y posición financiera antes de las 07:00 del día siguiente. Import/DirectQuery y TTL de caché no acreditan esos plazos por sí solos.

## 6. Gobierno, búsqueda y modelos

### 6.1 OpenMetadata y calidad

OpenMetadata sustituye al catálogo propio propuesto en la conversación. Se instrumentarán conectores y trabajos programados, con permisos mínimos y sin muestrear datos sensibles de forma indiscriminada. Los pipelines y trabajadores publicarán automáticamente las relaciones que no extraiga el conector. El conector ADLS consultado no aporta linaje nativo: no se afirmará cobertura automática completa por instalarlo.

El control de calidad se implementa en los puntos de captura y en los trabajos de datos. Los resultados durables alimentan el catálogo y el tablero Power BI. Se declaran reglas, población evaluada, conteos rechazados, causas, responsables y tratamiento de excepciones. El catálogo no sustituye las restricciones del repositorio ni la conciliación financiera.

La instalación debe incluir sus dependencias soportadas de base de metadatos y motor de búsqueda, con versiones compatibles y repositorios dedicados. No se presupone que pueda reutilizar sin aislamiento el índice de búsqueda del negocio. Los trabajos de ingestión se ejecutarán desde la orquestación ya seleccionada; no se añade Airflow como plataforma independiente.

### 6.2 OpenSearch

OpenSearch resuelve la búsqueda global, mientras pgvector conserva el índice comercial multimodal. La API aplica autorización y evita exponer consultas arbitrarias desde el cliente. Los resultados, fragmentos, facetas y conteos respetan permisos; la revocación y eliminación se propagan a los índices.

El control de lectura por documento no equivale a control de escritura: las identidades de consulta y de indexación tendrán permisos distintos. Se incluyen operación, actualizaciones, capacidad, réplicas, recuperación y reconstrucción de los índices dentro del servicio ofertado.

### 6.3 MLflow y entrenamiento

MLflow registra conjuntos referenciados por versión, código, parámetros, métricas, artefactos y modelo promovido. PostgreSQL almacena sus metadatos y Blob los artefactos, con acceso Retail propio. El conjunto de entrenamiento conserva manifiesto, procedencia y reglas de preparación en el lago.

Los trabajos Python/scikit-learn realizan entrenamiento y evaluación temporal del conteo predictivo. Se registran línea base, métricas, variables y resultados. Se implementarán la detección de deriva, el plan de reentrenamiento, la aprobación humana para promover, la reversión y la alternativa manual. MLflow aporta registro y versionado; esos controles requieren implementación e instrumentación propias.

La recomendación de conteo no se convierte automáticamente en ajuste de stock ni en una atribución de hurto. La métrica de exactitud se contrasta con una muestra de control independiente del modelo.

## 7. Evidencia, precios, retención y exportación

El historial de precios registra valor, canal, vigencia, versión y tiempos de publicación y confirmación en destino. Una actualización en Oferta no prueba que el precio ya se exhibía en la etiqueta. La propiedad append-only necesita protección y evidencia frente a alteraciones administrativas.

ADLS Gen2 usa capacidades de Blob; «lago» y «archivo de evidencia» expresan finalidades y políticas diferentes. Las áreas de transformación tienen permisos y ciclos de vida propios. La custodia WORM se configura donde corresponde a evidencia o archivo retenido, sin bloquear indiscriminadamente las tablas y archivos de trabajo.

El Caso 09, capítulo 15, fija retenciones que algunas notas previas dejaban abiertas:

| Clase de información | Retención del Caso | Aplicación |
|---|---|---|
| Documentos tributarios y antecedentes de venta | 6 años | Datos y documentos consultables y trazables. |
| Evaluación, precontrato, aceptación, repactaciones, comunicaciones y cobranza | Plazo completo del crédito y 6 años más | Plazo vinculado al ciclo del crédito. |
| Grabaciones y soportes del consentimiento de originación y repactación | Plazo completo del crédito y 6 años más | Sustituye la práctica actual de 90 días. |
| Precio publicado por canal | 3 años | Historial verificable de publicación. |
| Movimientos, conteos y ajustes de inventario | 6 años | Conservar movimientos y decisiones, no solo la posición actual. |
| Fidelización | Mientras dure la relación y 2 años más | Definir el cierre de relación y la eliminación de copias derivadas. |
| Videovigilancia | 30 días | Política diferenciada de los expedientes de crédito. |
| Prevención de lavado | Normativa aplicable | Requiere análisis específico de aplicabilidad. |

El RT-05.10 del Caso contiene la tabla de retención; el RT-05.10 transversal trata del catálogo deseable. Se identificará documento y materia al usarlos para evitar confundir ambos textos.

Migración, retención, archivo y respaldo son políticas diferentes. El horizonte de migración de pedidos online es de tres años; no determina por sí solo toda su retención posterior. Para eventos de seguridad y auditoría también se contrastan RT-11.14 y RT-16.10; no se aplica una cifra universal de seis años a todo dato.

La exportación íntegra incluye datos operacionales, documentos, expedientes, metadatos necesarios y diccionario, además de agregados analíticos. Los trabajos masivos generan formatos abiertos, filtros, corte, manifiestos y auditoría; notifican su término. El Cliente debe poder iniciarlos sin intervención del adjudicatario, conforme a RT-05.06. Una exportación temporal tiene caducidad y permisos propios.

## 8. Continuidad y recuperación

El diario de tienda confirma de forma durable antes de responder, conserva identificación y secuencia y se sincroniza con idempotencia. La continuidad también necesita promociones, precios, existencia local, identidad y documentos de contingencia. Debe existir una regla determinista para venta local frente a reservas digitales.

El cupo offline permanece bajo autoridad y custodia de Filial. Su uso exige porciones o autorizaciones exclusivas, consumo durable, caducidad y conciliación que impidan doble gasto entre terminales. No se habilita por guardar una copia del cupo, ni permite aperturas o ampliaciones sin enlace. La política de Riesgo/Finanzas y su prueba de factibilidad siguen siendo necesarias.

Para autonomía se conserva el mínimo transversal de 24 horas por la regla de precedencia: las ocho horas de tienda y cuatro del CD en el Caso no rebajan ese mínimo. La sincronización después de ocho horas debe respetar el máximo de 30 minutos fijado por el Caso. El comportamiento tras 24 horas también se dimensiona y prueba, sin inventar un plazo contractual distinto.

Azure Backup y PITR se detallan por recurso. Los respaldos operacionales de PostgreSQL, el respaldo de largo plazo, la retención de evidencia y la reconstrucción analítica tienen objetivos distintos. La documentación consultada describe hasta 35 días de respaldo operacional y hasta diez años mediante la solución de largo plazo; ninguna cifra sustituye una política de custodia de crédito que puede superar ese horizonte.

Los ensayos de recuperación incluyen claves, documentos, estados de procesos, mensajes pendientes, catálogos e índices. No se declara protegido un recurso por dibujar una bóveda. El destino de recuperación, la residencia y los permisos requieren resolución explícita antes de afirmar cumplimiento.

## 9. Cambios que deben reflejarse en la siguiente edición

| Artefacto o contenido | Cambio definido |
|---|---|
| Figura 4.31 y vista de Datos | Restituir Data Lake por ámbito; incorporar OpenMetadata y MLflow en sus responsabilidades técnicas; conservar PostgreSQL analítico y separar búsqueda global de multimodal. |
| SD-04: selección y decisiones | Registrar productos incluidos/excluidos y responsabilidades; eliminar la decisión de retirar Data Lake y la alternativa de catálogo construido desde cero. |
| SD-04: integración | Mantener Service Bus Premium por ámbito, outbox e idempotencia. Conciliar las menciones históricas a Event Hubs sin trasladar sus promesas de replay. |
| SD-04: autoridad de datos | Aclarar propiedad por servicio, metadatos F:C-03, bitácora X-01 y límites de las agrupaciones visuales. |
| SD-04 y T-11 | Incluir dependencias, versiones, soporte y plan de actualización durante los 56 meses; dimensionamiento por recurso y emplazamiento. |
| T-12 | Trazar capacidades y evidencia prevista sin marcar cumplimiento ejecutado por selección de producto. |
| SD-08 y operación | Incluir fallos, copia aislada, residencia, restauración, mantenimiento y soporte de OpenSearch, OpenMetadata y MLflow. |
| SD-09 | Incorporar controles de datos, linaje, carga, reconstrucción, aislamiento y calidad de modelos. |
| SD-13 | Precisar el entrenamiento y gobierno del conteo predictivo y conservar las responsabilidades de las cinco innovaciones. |

La selección de productos está cerrada en esta nota. Siguen pendientes trabajos de ingeniería y decisiones del mandante sobre tenant, residencia y recuperación, además de contratos, modelos de datos, versiones, dimensionamiento y pruebas. Esos pendientes no se presentan como productos candidatos ni como capacidades ya demostradas.

## 10. Fundamento técnico y límites de verificación

Documentación primaria consultada durante la conversación el 22-10-2026:

- [ADLS Gen2](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction): capacidades analíticas sobre Blob.
- [Data Factory: integration runtimes](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime): ubicación del factory, metadatos y ejecución.
- [OpenMetadata: conector ADLS](https://docs.open-metadata.org/v1.11.x/connectors/database/adls-datalake/yaml): extracción de metadatos y límites de linaje del conector.
- [OpenMetadata: API de linaje](https://docs.open-metadata.org/v1.12.x/api-reference/lineage/add): publicación de relaciones desde trabajos propios.
- [MLflow Tracking](https://www.mlflow.org/docs/latest/ml/tracking/): registro de experimentos y uso de PostgreSQL y Azure Blob.
- [scikit-learn: evaluación temporal](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html): herramientas de separación temporal; la evaluación definitiva debe respetar la estructura real de los datos.
- [OpenSearch: seguridad por documento](https://docs.opensearch.org/latest/security/access-control/document-level-security/) y [consultas fuzzy](https://docs.opensearch.org/latest/query-dsl/term/fuzzy/): controles y búsqueda tolerante.
- [Azure AI Search: regiones](https://learn.microsoft.com/en-us/azure/search/search-region-support): Chile Central no figuraba en la lista consultada; se seleccionó OpenSearch autogestionado.
- [Azure Databricks: regiones](https://learn.microsoft.com/en-us/azure/databricks/resources/supported-regions): Chile Central no figuraba en la lista consultada.
- [Blob: inmutabilidad](https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview): políticas de retención y WORM.
- [PostgreSQL: respaldo operacional](https://learn.microsoft.com/en-us/azure/postgresql/backup-restore/concepts-backup-restore) y [Azure Backup para PostgreSQL Flexible Server](https://learn.microsoft.com/en-us/azure/backup/backup-azure-database-postgresql-flex-overview): mecanismos diferenciados de recuperación y largo plazo.

No se ejecutaron pruebas en Azure, benchmarks, migraciones ni restauraciones. Las comprobaciones gráficas históricas no validan esta nueva composición, que aún debe actualizarse y pasar por el flujo `diagramas-ancoa`. Este archivo conserva decisiones de diseño y requisitos de verificación, no una certificación técnica o normativa.

## Declaración de uso de IA

Documento de contexto consolidado con asistencia de Codex a partir de esta conversación y de fuentes locales y técnicas consultadas. Nivel de texto: Alto. No se generaron ni modificaron diagramas en esta entrega. No se registra revisión humana formal ni aceptación del subdocumento por la creación de esta nota.
