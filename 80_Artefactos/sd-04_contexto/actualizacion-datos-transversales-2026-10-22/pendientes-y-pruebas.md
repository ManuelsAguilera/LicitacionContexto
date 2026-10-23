# Decisiones pendientes y verificación propuesta

Estado: borrador de análisis, 22-10-2026. Los productos seleccionados en los registros no se vuelven a abrir como alternativas. Las tareas siguientes se refieren a su configuración, integración, aceptación y capacidad.

| Tema | Qué falta resolver o demostrar | Responsable por asignar / salida esperada |
| :--- | :--- | :--- |
| Residencia y tenant | Aprobar expresamente tenant de Filial, regiones primarias/secundarias, tránsito, metadatos, soportes y destino de respaldo por producto. Ubicación de Data Factory distinta de su integration runtime. No se infiere autorización por seleccionar Azure. | Mandante, seguridad y arquitectura: registro de aprobación y matriz de ubicación. |
| Datos operacionales | Contrato atómico entre autorización/cupo de Originación y cuentas/saldos de Cartera; reservas, expiración, consumo, reversa y conciliación. | Dueños de F:C-01/F:C-02: contrato y pruebas de concurrencia, sin doble autoridad. |
| Evidencia financiera | Estados de carga, verificación de contenido, integridad, metadatos y completitud del acto; expediente en PostgreSQL y archivos en Blob. | F:C-03 y seguridad: estados y prueba de expediente completo/incompleto. |
| Analítica | Indicadores, detalle navegable, dimensiones, SLA de frescura, particionado, volumen y capacidad por ámbito; autorización de exportaciones y conexión privada de BI. | Datos y dueños de negocio: modelos, cargas y criterios de aceptación. |
| Gobierno | Versión y buscador compatible dedicado de OpenMetadata; permisos, conectores, almacenamiento propio y publicación automática de linaje de trabajos. Sin Airflow añadido ni búsqueda de negocio reutilizada. | Plataforma de datos: matriz de compatibilidad y prueba del API de linaje/calidad. |
| Búsqueda | Esquema, facetas, contenido autorizado, revocación de permisos, reconstrucción y API de OpenSearch. Modelo y versión de representaciones multimodales siguen por seleccionar. | Oferta y plataforma: contrato de consulta, evaluación y reconstrucción. |
| Conteo predictivo | Conjuntos/versiones, evaluación temporal, referencia al código, línea base, promoción humana, deriva, fallback y rollback. MLflow no implementa por sí solo estos controles. | Existencias y equipo de datos: protocolo y resultados reproducibles. |
| Continuidad sin enlace | Caducidad de cupo, asignaciones exclusivas, consumo durable y conciliación. No abrir crédito ni aumentar límites sin enlace. Diario Retail y datos mínimos de Filial separados. | Dueños de Ventas/Originación: reglas y pruebas de tienda. |
| Retención y recuperación | Clasificar evidencia, archivo y respaldo; definir políticas por clase y ámbito, claves, restauración y excepciones. PITR/Backup no sustituyen conservación legal; el plazo de un crédito puede superar una política técnica predeterminada. | Seguridad, datos y mandante: tabla de retención y restauraciones verificadas. |
| Dispositivos y acceso | Equipos compatibles con Intune/Defender, sesiones compartidas, MFA de privilegios, licencias, ruta administrativa permitida y alcance de grabación. QR + PIN es un factor. | Seguridad y operación: matriz de equipos/rutas y pruebas de revocación. |
| Bastion y archivo | Asegurar Blob temporal mutable sin versionado, ventana hasta copia, verificación de WORM y restricciones de acceso. No afirmar grabación de toda operación AKS/BD/API. | Seguridad: prueba de carga, pérdida, copia y alteración. |
| Telemetría | Dimensionar colas durables locales 24 h, almacenes por ámbito, persistencia/HA de Prometheus, versiones y receptores OTLP soportados, saneamiento y retención. Evitar series duplicadas y copias masivas de Loki a Log Analytics. | Plataforma/SRE: configuración, cargas, runbooks y aceptación. |
| Supervisión y operación | Ubicación independiente de sondas, observador del propio monitoreo, ruta de alerta que sobreviva a la falla, turnos NOC/SOC y contrato mínimo de salud agregada. | Operación/mandante: escalamiento, turnos y pruebas de incidente. |
| Capacidades comunes | Producto y contratos de tareas humanas, firma, notificaciones y maestro de ubicaciones. Mantener instancias propias por ámbito. | Arquitectura y dueños: especificaciones; los candidatos no se convierten en servicios aprobados por aparecer en el dibujo. |
| F:C-04 | Alcance, RF, etapa, responsables y aprobación. Continúa sin enlaces operacionales. | Equipo de alcance/mandante: decisión registrada antes de incorporar contratos. |
| Interfaces | Verificar el inventario de catorce interfaces, contratos de contrapartes y migración por olas. El agrupamiento gráfico no acredita ni reemplaza ese inventario. | Integración y proveedores: contratos y matriz de conciliación. |
| Conciliación documental | Incorporar, tras revisión, las diferencias con SD-03/SD-04/SD-05, T-11, T-12, requerimientos y costos/operación a 56 meses. | Equipo de propuesta: cambio controlado posterior. Ninguno de esos documentos se editó en esta entrega. |

## Pruebas propuestas

No se ejecutaron estas pruebas sobre una arquitectura desplegada. Sus criterios contractuales deben verificarse contra las Bases y el Caso antes de la aceptación.

| Ensayo | Estímulo y evidencia esperada |
| :--- | :--- |
| Frescura operacional | Venta real hasta disponible publicado ≤30 s; cambio de precio hasta caja/canal ≤5 min. Medición completa, sin deducirla de TTL ni de refresco BI. |
| Analítica y cierre | Lotes con atrasos, mensajes fallidos, duplicados y datos tardíos; trazabilidad desde indicador hasta origen y posición financiera antes de las 07:00 del día siguiente. Exactitud por categoría diaria. |
| Idempotencia y orden | Reentregar, invertir y omitir hechos; comprobar versiones, reintentos, conciliación, DLQ y ausencia de duplicación de saldos/indicadores. |
| Reconstrucción | Restaurar proyecciones e índices desde exportación autorizada, corte, manifiesto y deltas; no depender de conservar indefinidamente mensajes en Service Bus. |
| Permisos y separación | Identidades Retail intentando acceder a datos/metadatos/índices/BI de Filial y viceversa: denegación. Validar cada instancia representada por un símbolo agregado y los extremos propios de X-01. |
| Cupo concurrente | Dos cajas/tiendas consumiendo la misma autorización; expiración, reconexión, reversas, reintentos y duplicados. Probar ausencia de doble gasto y conciliación de cuenta. |
| Operación sin enlace | Ocho horas sin enlace y sincronización dentro del máximo de 30 minutos indicado por el Caso; probar también el objetivo técnico de autonomía 24 h. El segundo ensayo no crea otro plazo contractual de sincronización. |
| Cola local | Reinicio durante 24 h sin enlace, saturación, agotamiento de disco, alertas, orden y drenaje; distinguir tienda no observable de fallo confirmado. |
| Evidencia y recuperación | Documento incompleto/corrupto, copia WORM, alteración, restauración por recurso con claves y permisos; validar por separado auditoría, respaldo y archivo. |
| Modelos y búsqueda | Evaluación temporal contra línea base, deriva, rechazo/promoción humana, fallback y reconstrucción; revocar permisos y comprobar que el índice deja de exponer contenido. |
| Observabilidad | Collector → Loki/Tempo/Prometheus y consultas Grafana; denegar OTLP no autenticado, evitar doble métrica y comprobar que el saneamiento elimina secretos/PII antes de persistir. |
| Supervisión del monitoreo | Caída de Collector, backend, Grafana y conectividad; demostrar una sonda y canal de aviso independientes. Blackbox no sustituye una compra completa ni el cálculo de SLO a partir de operaciones reales. |

Uso de IA: Alto. No constituye revisión humana ni cierre de los pendientes.
