# Investigación de las cinco innovaciones del equipo

Fecha de consulta: 2026-10-11. Estado: investigación y recomendaciones para revisión del equipo. No constituye el SD-13 final ni el Formulario T-19.

## 1. Conclusión y reglas de lectura

La cartera elegida es técnicamente plausible: lockers 24/7, conteo cíclico predictivo, búsqueda multimodal, retail media y modo tienda con fila virtual. Su aceptación como innovación depende de demostrar un aporte específico al Caso 09 sobre las funciones obligatorias. La existencia comercial de una tecnología demuestra disponibilidad, pero no prueba beneficios en Ancoa ni garantiza la evaluación del profesor.

Se distinguen tres clases de afirmaciones: **hecho documentado** en Bases o fuente primaria; **recomendación de diseño** de este informe; y **dato pendiente** que requiere levantamiento, cotización o prueba. Las recomendaciones no son compromisos aprobados. No se asignan precios, porcentajes de mejora o niveles TRL sin evidencia suficiente.

Fuentes locales rectoras: `00_Bases/Bases_Administrativas.md`, artículos 28 a 30; `00_Bases/Bases_Transversales.md`, capítulos 13, 18 y 26; `00_Bases/Caso_09_Cadena_Multitienda.md`. El resumen externo del equipo es antecedente, actualizado por `decision_cartera_equipo.md`. Los RF se contrastaron con el espejo v3.0 de `01_Requerimientos/md/catalogo-de-requerimientos-depurado-v30.md`; el Excel oficial prevalece ante diferencias, y la conciliación v3.1 debe verificarse antes del T-19.

| Tipo | Qué se propone demostrar | Confusión que debe resolverse al redactar |
| :--- | :--- | :--- |
| Producto o servicio | Retiro autónomo disponible fuera del horario de tienda | Click & Collect existente no equivale a retiro autónomo 24/7 |
| Proceso | Más discrepancias relevantes detectadas por hora mediante priorización predictiva | Contar sin cerrar tienda y programar conteos ya son parte del alcance base |
| Tecnología o arquitectura | Recuperación multimodal y semántica de productos pertinentes y disponibles | Tolerancia a errores y filtros ya son obligatorios |
| Modelo de negocio | Venta de un servicio publicitario medible a proveedores del retail | Instalar banners por sí solo no define un nuevo negocio |
| Experiencia de usuario | Espera de probadores gestionada con acceso equivalente desde móvil y tótem | Un mapa o una app por sí solos no demuestran mejora de experiencia |

## 2. Innovación 1: Lockers Ancoa 24/7

### Problema, alcance y alternativas

**Hecho local:** el caso tiene problemas de cumplimiento y de operación del retiro; no se ha confirmado una línea base de tiempo de entrega en mesón ni demanda nocturna. El resumen del equipo presenta la congestión como hipótesis que debe dimensionarse. No atribuir a lockers la solución de los 2.840 pedidos fallidos por existencia incorrecta.

**Recomendación:** retiro de pedidos ya preparados, verificados y pagados, en compartimentos compatibles con su volumen y peso. El exterior debe ser accesible 24/7, iluminado y con ruta accesible. Tiendas dentro de recintos que cierran requieren otra ubicación o una promesa horaria distinta. Definir responsable del paquete, retiro por tercero, vencimiento, devolución al mesón, reclamación y evidencia de entrega.

**Opciones documentadas:** Cleveron 302 es interior; por ello no sirve como selección directa para la promesa de exterior del resumen [S1]. Cleveron 355 es exterior y está orientado a mercancía voluminosa [S2]. La recomendación es usar el 355 como referencia técnica para esa categoría y comparar una alternativa exterior para paquetería pequeña, cuya densidad puede ser mejor. La selección de toda la red requiere distribución real de tamaños y cotización. Bloq.it publica una API REST sobre HTTPS para gestionar lockers [S3]; esto verifica una vía de integración alternativa, no certifica por sí solo un modelo de gabinete exterior ni disponibilidad chilena.

### Integración y excepciones

Crear un adaptador al software del fabricante conectado al servicio de pedidos y cumplimiento. Estados propuestos: reservado, en carga, disponible para retiro, retirado, vencido y bloqueado. Registrar escaneo de paquete, asignación de puerta, confirmación de cierre y retiro; usar identificadores idempotentes para impedir duplicación de entregas.

No dar por existente MQTT ni control directo de cerraduras: el protocolo final depende del fabricante. Un PIN numérico no demuestra operación sin internet. Para retiro desconectado se deben verificar credenciales precargadas, vigencia, consumo único, reloj y protección del controlador, además de la reconciliación posterior. La ficha del 355 distingue conexión requerida en sitio, pero esa indicación no explica todo el mecanismo de autorización. Contingencia: conectividad de respaldo y asistencia operativa, con suspensión del retiro automático cuando no se pueda verificar autorización. Las 48 horas del resumen son una política propuesta, no una cifra de las Bases.

### Medición, economía y pendientes

Medir tiempo total de retiro p50/p95, retiros completados sin asistencia, ocupación por tamaño, vencimientos, fallos y minutos de personal por entrega. Levantar la línea base del mesón y comprobar demanda fuera de horario. Dimensionar compartimentos por llegadas, permanencia y percentiles de ocupación por tamaño; el promedio de paquetes diarios no basta.

CAPEX: gabinete, obra civil, energía, comunicaciones y puesta en marcha. OPEX: licencias, soporte, repuestos, conectividad y atención. Beneficio: minutos de entrega evitados y pedidos adicionales atribuibles al servicio. No contar dos veces ventas recuperadas por mejoras de inventario.

**Pendientes críticos:** dimensiones interiores y carga admisible por puerta; disponibilidad y mantenimiento en Chile; API y eventos; seguridad y procedimiento sin red; ubicación accesible; volumen por tienda. Piloto recomendado en Etapa 2, coordinado con el servicio de pedidos, con disponibilidad inicial propuesta en el mes 21. Esta fecha debe incorporarse a EDT y compras antes de comprometerla.

## 3. Innovación 2: Conteo cíclico predictivo

### Diferencial y modelo

**Hecho local:** discrepancias en 12,4 % de referencias auditadas y meta del Caso bajo 2 %. RF-131 a RF-137 ya cubren frecuencia, método, programación, registro y recuentos. El diferencial elegido es ordenar el trabajo según riesgo y valor esperado de la discrepancia con capacidad limitada. El 12,4 % no es una tasa de robo ni una tasa representativa de todo el inventario sin conocer el muestreo.

**Recomendación:** comenzar comparando programación vigente, reglas ABC/riesgo y un modelo supervisado de árboles con boosting. Scikit-learn documenta clasificadores y regresores adecuados para datos tabulares [S4]. No cargar cientos de miles de identificadores SKU como categorías nativas sin tratamiento: las limitaciones de cardinalidad deben considerarse. Un modelo más complejo se justifica solo si mejora las pruebas.

Variables candidatas disponibles antes de decidir: tiempo desde último conteo, ventas, recepciones, devoluciones, ajustes previos, movimientos entre ubicaciones, discrepancias anteriores y duración prevista del conteo. Confirmar existencia y calidad de cada variable. Etiqueta de entrenamiento: diferencia física validada a fecha de conteo, normalizada por movimientos ocurridos mientras se cuenta. No usar el resultado del mismo conteo como variable predictora.

Puntuación propuesta: probabilidad de discrepancia × magnitud o valor esperado / minutos de conteo. Añadir restricciones de cobertura, frecuencias obligatorias y disponibilidad del personal. Mantener muestreo independiente del modelo para detectar áreas poco exploradas y medir exactitud general. Los porcentajes de exploración se fijan mediante protocolo, no arbitrariamente.

### Validación y operación

Separar entrenamiento y evaluación por tiempo y comprobar transferencia entre tiendas; `TimeSeriesSplit` documenta por qué entrenar con futuro produce una evaluación inválida [S5]. Evitar contaminación entre observaciones del mismo ciclo. Evaluar detección por hora, precision/recall en la capacidad de trabajo disponible y calibración de probabilidades; accuracy global puede ocultar fallos cuando hay pocas discrepancias.

Diseño recomendado: comparación controlada de ventanas o grupos equivalentes, misma cantidad de horas y cobertura; cálculo previo de tamaño muestral. El supervisor aprueba la lista, la app registra conteos y el procedimiento establecido valida ajustes. El modelo no autoriza saldos ni acusa hurto. Si faltan datos, se usa programación por reglas mientras se genera historia verificada.

Calendario recomendado: datos y desarrollo meses 1 a 12, modo sombra meses 13 a 15 y uso desde mes 16 sujeto a aceptación. Permite medir antes de producción conforme a RT-26.08. Procesamiento y entrenamiento dentro del ámbito retail, versionado, registro de recomendaciones, detección de deriva y respaldo manual conforme a RT-18.01 a RT-18.09.

Economía: datos, desarrollo, cómputo, validación y mantenimiento. Beneficio directo por horas mejor aprovechadas; ahorro de pérdidas solo con evidencia causal. Las metas de reducción general de merma no se asignan íntegramente al predictor.

**Pendientes:** historial y tamaño de muestra, tiempos de conteo, reglas base, umbral de discrepancia relevante, meta comparativa y recursos de entrenamiento. No se ha encontrado en las fuentes consultadas un resultado empírico transferible que garantice una mejora porcentual en Ancoa.

## 4. Innovación 3: Búsqueda vectorial multimodal

### Qué ofrece y qué no puede prometer

**Hecho local:** RT-16.27 ya exige búsqueda con texto completo, tolerancia a errores, filtros y permisos. No presentar esas funciones como innovación. Tampoco está demostrada en el Caso una tasa de consultas sin resultados ni que el buscador solo entienda el nombre exacto: esa afirmación del resumen requiere evidencia.

**Recomendación:** búsqueda por imagen y por intención en español sobre el catálogo autorizado, combinada con búsqueda léxica para SKU, marcas y términos exactos. La foto permite recuperar productos visualmente semejantes; no garantiza identificar el artículo exacto. Los complementos de un conjunto requieren un módulo de recomendación y reglas adicionales, por lo que deben declararse como alcance separado si se incorporan.

### Tecnología y licencia

Comparar un modelo multimodal multilingüe con CLIP/OpenCLIP y una alternativa de texto en español más recuperación visual. OpenCLIP es un ecosistema de modelos, no una garantía de calidad en modismos chilenos [S6]. Jina CLIP v2 es candidato documentado para texto e imagen multilingües; su licencia descargable es CC BY-NC 4.0, y el proveedor ofrece vías comerciales [S7]. Recomendación: evaluación con este candidato y licencia comercial para despliegue si resulta elegido; verificar contrato, pesos, código, ubicación y prohibición de entrenamiento con datos del cliente. No declararlo gratuito para el negocio.

PostgreSQL con pgvector/HNSW es una opción razonable para prototipo y carga medida [S8]. Comparar frente a un motor de búsqueda especializado si los filtros o la carga lo requieren. La documentación de pgvector explica que los filtros posteriores a un índice aproximado pueden devolver pocos resultados; se deben evaluar escaneos iterativos, partición y configuración con el catálogo real. La dimensión depende del modelo y la calidad obtenida; los 512 componentes del resumen no son una obligación técnica.

### Flujo, prueba y operación

Indexar imágenes y texto al cambiar el catálogo, con versión de modelo e índice. Consultar por texto o imagen, recuperar candidatos, combinar ranking, aplicar filtros de talla, categoría, precio y permisos y validar disponibilidad antes de mostrar y nuevamente antes de comprar. El índice vectorial no es fuente autoritativa de stock.

Construir consultas españolas y chilenas, fotografías representativas y juicios de relevancia de usuarios. Medir nDCG@10/recall@10, resultados pertinentes disponibles, tasa de reformulación y latencia p95 de extremo a extremo. Separar tiempo del índice de subida de foto e inferencia. Evitar prometer milisegundos para todo el proceso sin prueba. Meta comparativa propuesta: mejora estadísticamente sustentada frente al buscador base; el umbral se acuerda tras la línea base.

No guardar fotos personales por defecto: definir retención mínima, eliminación de metadatos, límites de archivo y trazabilidad proporcional. La auditoría de IA debe conservar evidencia suficiente conforme a RT-18.05 con acceso y plazo definidos. Respaldo: búsqueda léxica; si se desactiva imagen, comunicarlo. Calendario propuesto: desarrollo e integración en Etapa 2 y disponibilidad mes 21, a confirmar con alcance del canal digital.

Costos: licencia comercial, inferencia, indexación, almacenamiento, pruebas de relevancia y mantenimiento. Beneficio: margen incremental de conversiones demostrado mediante comparación, no multiplicar visitas por una mejora inventada.

**Pendientes:** calidad de fotos y fichas, licencia elegida, benchmark en español, volumen/concurrencia, dimensión y capacidad, política de fotos y relación con búsquedas patrocinadas.

## 5. Innovación 4: Retail Media Network

### Modelo de negocio y alternativas

**Recomendación:** Ancoa vende a proveedores del retail exposición medible de productos disponibles mediante campañas patrocinadas. Marketing/Comercial recluta anunciantes y aprueba campañas; el sistema gestiona presupuesto, publicaciones, registro y reportes. No dar por comprometidas a las marcas nombradas en el resumen.

Comparar servicio especializado con desarrollo propio. Criteo documenta campañas de productos patrocinados con CPC, pujas y atribución, lo que demuestra una alternativa comercial operativa [S9, S10]. Integrar un servicio especializado es la opción inicial recomendada para evaluar, condicionada a contrato y tratamiento de datos. Desarrollo propio exige además conciliación de presupuesto, fraude, facturación y operación de campañas. La oferta debe elegir una alternativa después de comparar control, privacidad, capacidad y soporte.

Alcance inicial recomendado: web, productos patrocinados y campañas contextuales por consulta o categoría. Extensión a app o tótems solo con inventario publicitario y flujo de usuario validados. Definir etiquetado visible, umbral de relevancia y límites de densidad como políticas del equipo. Una puja alta no habilita publicar un producto agotado ni desplazar todos los resultados pertinentes.

### Datos y medición

Separar ventas retail y publicidad de toda la información de crédito. No usar comportamiento de pago, mora, cupos ni puntajes de la filial. Empezar con selección contextual para reducir dependencia de perfiles personales. Datos seudonimizados siguen pudiendo ser personales; llamar «anonimizados» a un identificador reemplazado no resuelve el tratamiento. La Ley 21.719 tiene vigencia diferida al 1 de diciembre de 2026; diseñar para su aplicación durante operación [S11]. Documentar base jurídica, finalidades, encargados, transferencias, conservación y derechos antes de incorporar perfiles. Esto requiere revisión legal del diseño concreto.

Medir ingresos publicitarios netos, anunciantes activos, retención, clics válidos, cumplimiento de presupuesto y efecto sobre conversión/latencia. Un reporte de ventas atribuidas usa una ventana y regla de atribución; no demuestra causalidad. Usar grupo de control para estimar ventas incrementales y evitar sumar como beneficio todas las ventas posteriores a un anuncio.

### Economía y responsabilidades

Ingresos CPC = clics válidos facturables × precio efectivo; ingresos CPM = impresiones facturables / 1.000 × tarifa. Separar tarifas, descuentos, comisión del proveedor, devoluciones, fraude y costo comercial. No sumar CPC y CPM sobre la misma unidad sin explicar el contrato. Preparar escenarios sin anunciantes, conservador, central y alto; todas las cantidades quedan como supuestos hasta validar demanda.

No modificar la cuota del contrato de licitación mediante revenue share sin comprobar artículos 18 y 72 y E-25. El negocio publicitario de Ancoa puede formularse independientemente del pago al adjudicatario. Calendario propuesto: diseño comercial durante Etapa 2; piloto desde mes 21, condicionado a anunciantes y canal disponibles.

**Pendientes:** demanda de marcas, responsable comercial, plataforma, tarifas, costos, flujo de facturación, tratamiento de datos y control experimental. Sin esas evidencias, el nuevo ingreso es una hipótesis y debe figurar como tal.

## 6. Innovación 5: Modo Tienda con fila virtual

### Alcance recomendado

Priorizar turno de probadores desde móvil y tótem, estado visible de espera y avisos de llamado. Añadir mapa por zonas usando planos y ubicación de catálogo validados. La fila no prueba dónde está físicamente cada prenda ni permite resolver automáticamente las pérdidas del probador.

Entrada recomendada mediante selección de tienda o QR, con acceso a fila sin exigir cuenta, smartphone ni ubicación. Geovallas y BLE son ayudas opcionales: Android documenta demoras en segundo plano [S12], y Apple exige considerar sus condiciones de monitoreo [S13]. No prometer activación inmediata ni posicionamiento preciso por el simple hecho de instalar balizas. Si se ofrece navegación interior detallada, levantar y calibrar cada tienda y medir error de ubicación; el número de balizas depende de esa prueba.

### Equipo recomendado e integración

**Referencia concreta:** Zebra KC50 de 22 pulgadas, montaje de piso accesible, Ethernet y administración empresarial. La ficha oficial documenta opciones de tamaño, conectividad y accesorios [S14]. La impresora de turnos es opcional; como referencia comparar Epson TM-T20III Ethernet, que documenta impresión desde dispositivos móviles [S15]. Compatibilidad física, SDK y variante exacta deben probarse: no se presume que cualquier impresora encaje en el pedestal del KC50. Mantener entrega de número por pantalla y atención asistida si falta papel.

Servidor local de tienda como autoridad de la fila durante cortes WAN; nube para supervisión y consolidación. Estados de turno: espera, llamado, presentación, uso, finalizado, cancelado y ausente. Separar el estado del turno del cubículo: libre, reservado, ocupado, limpieza o fuera de servicio. Liberación por personal; sensores de puerta serían una ampliación específica, no una capacidad asumida del tótem.

Evitar dobles asignaciones mediante transacciones e identificadores únicos. Tras caída y reinicio, recuperar la fila persistida. El móvil requiere conexión al servidor para información en vivo: durante corte WAN, el tótem local puede seguir funcionando mientras que móviles externos no necesariamente podrán hacerlo. Ofrecer acceso asistido y avisos de pantalla como respaldo.

### Reglas y prueba

Definir gracia del llamado, reingreso, prioridades accesibles, acompañantes y cupo de prendas con Operación. La gracia no será una cifra arbitraria. Notificaciones sujetas a permiso y recepción; vibración o sonido no garantizan que el cliente vea el aviso. Mostrar estado y alternativas visibles. WCAG 2.2 AA conforme a RT-13.01, objetivos táctiles y pruebas con usuarios reales conforme a RT-13.03 y RT-13.07; validar accesibilidad física del conjunto instalado.

Medir tiempo físico en fila, tiempo total desde solicitud hasta acceso, abandono, ausencias, asignaciones duplicadas y éxito de solicitud por móvil/tótem. La fila virtual puede reducir espera de pie sin reducir el tiempo hasta que quede libre un cubículo; medir ambos resultados. Economía: tótem, instalación, aplicación, soporte y mantenimiento; el beneficio por conversión requiere evidencia y no se duplica con búsqueda.

Calendario propuesto: piloto en Etapa 1, meses 13 a 15, disponibilidad inicial mes 16 si la app y el entorno local están listos. El despliegue completo necesita plan propio y no se presume incluido en el piloto.

**Pendientes:** demanda por franja, cantidad de cubículos/tótems, planos, conectividad móvil local, reglas de prioridad, integración de impresora y línea base de experiencia.

## 7. Integración de cartera y condiciones de cierre

| Innovación | Dependencias principales | Primer hito propuesto | Evidencia para cerrar diseño |
| :--- | :--- | :--- | :--- |
| Lockers | Pedidos preparados, inventario fiable, emplazamiento y fabricante | Mes 21 | Cotización, contrato API, tamaños/cargas y piloto de entrega |
| Conteo predictivo | Historia verificada y app de conteo | Evaluación 13–15; uso mes 16 | Benchmark contra reglas y protocolo independiente |
| Multimodal | Catálogo, permisos, disponibilidad y canal digital | Mes 21 | Licencia, conjunto de relevancia y carga de extremo a extremo |
| Retail media | Canal digital, plataforma, Marketing y anunciantes | Piloto mes 21 | Demanda comercial, economía, privacidad y medición |
| Fila virtual | Operación de probadores, tótem, app y servidor local | Piloto 13–15; uso mes 16 | Reglas, accesibilidad, continuidad y prueba con usuarios |

Los meses anteriores son recomendaciones que respetan las salidas contractuales de los meses 16 y 21; no son fechas ya incorporadas a la EDT. Asignar paquetes a cada innovación sin inventar códigos y completar su costo en el flujo de caja de 56 meses. La operación abarca los meses 21 a 56.

Para T-19, completar por innovación: problema documentado, tecnología concreta, madurez con escala y evidencia, arquitectura/EDT/mes, inversión/OPEX/beneficio, indicador con línea base/meta/momento y riesgo con probabilidad/impacto/mitigación/contingencia. Las fuentes comerciales demuestran componentes maduros, pero la integración completa en Ancoa sigue sin piloto: no declarar TRL 9 para toda la solución. Si se adopta TRL, justificar por qué la evidencia satisface el nivel asignado.

Prioridades de cierre: (1) levantar datos operativos; (2) probar API y hardware; (3) evaluar modelo de conteo y búsqueda; (4) validar demanda publicitaria; (5) fijar metas y costos; (6) revisar alcance con responsables del cliente y trasladar decisiones a arquitectura, EDT y T-19. No se ha solicitado ni realizado contacto con proveedores o terceros.

## 8. Fuentes primarias consultadas

Las fuentes web fueron consultadas el 11 de octubre de 2026. Cuando no figura fecha editorial se consigna s. f.; la fecha de rastreo del buscador no se usa como fecha de publicación. Las afirmaciones de rendimiento del proveedor no se transfieren a Ancoa.

- **S1.** Cleveron. (s. f.). *Cleveron 302*. https://cleveron.com/products/cleveron-302/
- **S2.** Cleveron. (s. f.). *Cleveron 355*. https://cleveron.com/products/cleveron-355/
- **S3.** Bloq.it. (s. f.). *Partner API*. https://docs.api.bloq.it/
- **S4.** Scikit-learn developers. (s. f.). *HistGradientBoostingClassifier*. https://scikit-learn.org/1.6/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html
- **S5.** Scikit-learn developers. (s. f.). *TimeSeriesSplit*. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
- **S6.** ML Foundations. (s. f.). *OpenCLIP*. https://github.com/mlfoundations/open_clip
- **S7.** Jina AI. (s. f.). *Jina CLIP v2: Model card and license*. https://huggingface.co/jinaai/jina-clip-v2
- **S8.** Pgvector contributors. (s. f.). *pgvector*. https://github.com/pgvector/pgvector
- **S9.** Criteo. (s. f.). *Getting started with onsite sponsored products*. https://help.retailmedia.criteo.com/kb/guide/en/getting-started-with-onsite-sponsored-products-sWZEhIFFWh/Steps/2786463
- **S10.** Criteo. (s. f.). *Create an onsite sponsored products campaign*. https://help.retailmedia.criteo.com/kb/guide/en/create-an-onsite-sponsored-products-campaign-f6bd9kseBQ/Steps/1017658
- **S11.** Biblioteca del Congreso Nacional de Chile. (2024). *Ley 21.719*. https://www.bcn.cl/leychile/navegar?f=2026-12-01&i=1209272
- **S12.** Google. (s. f.). *Create and monitor geofences*. https://developer.android.com/develop/sensors-and-location/location/geofencing
- **S13.** Apple. (s. f.). *Monitoring the user's proximity to geographic regions*. https://developer.apple.com/documentation/corelocation/monitoring-the-user-s-proximity-to-geographic-regions
- **S14.** Zebra Technologies. (s. f.). *KC50 Android kiosk computer: Specification sheet*. https://www.zebra.com/gb/en/products/spec-sheets/interactive-kiosks/kc50.html
- **S15.** Epson. (s. f.). *TM-T20III thermal receipt printer*. https://epson.com/For-Work/Printers/POS/TM-T20III-Thermal-Receipt-Printer/p/C31CH51A9972
- **S16.** Tabassi, E. (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*. NIST. https://doi.org/10.6028/NIST.AI.100-1
- **S17.** International Organization for Standardization. (2023). *ISO/IEC 42001:2023*. https://www.iso.org/standard/42001

S16 y S17 sustentan el marco de gobierno de IA exigido por las Bases. La consulta pública de ISO identifica el alcance de la norma; no equivale a una auditoría contra su texto completo ni a certificación.
