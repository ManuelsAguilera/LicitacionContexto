# Arquitectura actualizada con Datos y capas transversales

Estado: borrador para revisión humana. Fecha: 22-10-2026. No se acredita despliegue, capacidad, cumplimiento ni aprobación de residencia.

El archivo [draw.io con tres páginas](../../../04_Adjuntos/diagramas/diag-04-33_arquitectura-actualizada.drawio) contiene la vista principal y dos ampliaciones. Las capas 7 y 8 comparten una banda **Capas transversales**, conservando Seguridad y Observabilidad como responsabilidades distintas. Se elimina su doble columna lateral. Se mantienen la VPN, las ocho capas, trece servicios vigentes, cinco innovaciones y F:C-04 como candidato sin contratos operacionales.

| Página | Contenido | Vista previa | Fuente validada |
| :--- | :--- | :--- | :--- |
| 1 | Arquitectura por capas, con Datos actualizado y banda transversal común | [PNG](../../../04_Adjuntos/diagramas/diag-04-33_arquitectura-datos-transversales.png) · [SVG](../../../04_Adjuntos/diagramas/diag-04-33_arquitectura-datos-transversales.svg) | [JSON](../../../04_Adjuntos/diagramas/diag-04-33_arquitectura-datos-transversales.json) |
| 2 | Alimentación de datos, gobierno, modelos y dependencias | [PNG](../../../04_Adjuntos/diagramas/diag-04-34_detalle-datos.png) · [SVG](../../../04_Adjuntos/diagramas/diag-04-34_detalle-datos.svg) | [JSON](../../../04_Adjuntos/diagramas/diag-04-34_detalle-datos.json) |
| 3 | Productos de Seguridad y Observabilidad, separados por ámbito | [PNG](../../../04_Adjuntos/diagramas/diag-04-35_detalle-transversales.png) · [SVG](../../../04_Adjuntos/diagramas/diag-04-35_detalle-transversales.svg) | [JSON](../../../04_Adjuntos/diagramas/diag-04-35_detalle-transversales.json) |

La división en vistas L2 respeta el máximo de 85 componentes de la guía: 85 en la principal, 41 en Datos y 59 en Transversales. Las tarjetas de resumen de 7 y 8 remiten a los productos de la tercera página; no son nuevos servicios ni despliegues compartidos. El editor conserva tarjetas, iconos, textos y conectores como objetos editables.

## Cambios aplicados

Se aplican [el registro de Datos](../capa-datos_decisiones-y-precisiones_2026-10-22.md) y [el de capas 7–8](../capas-07-08_cambios-y-conexiones_2026-10-22.md). Son decisiones de contexto solicitadas por el usuario; no sustituyen las Bases ni modifican la oferta por sí solas.

- ADLS Gen2 se reincorpora para landing, curados e históricos autorizados, con recursos separados por ámbito. Esta decisión sustituye su retirada de la iteración anterior. El archivo WORM conserva otra responsabilidad y otra política.
- Data Factory coordina las cargas; trabajadores Java/Spring en AKS ejecutan ingesta, calidad, transformación y proyecciones. Los hechos operacionales conservan outbox y Service Bus propios.
- Power BI consulta únicamente PostgreSQL analítico dedicado del ámbito. No consulta bases operacionales, lago, OpenSearch ni catálogos.
- OpenSearch autogestionado cubre búsqueda global con API y filtros propios. PostgreSQL/pgvector conserva el índice multimodal de Oferta. OpenMetadata tiene metadatos e índice de catálogo dedicados; el buscador compatible y su versión siguen por precisar.
- Python/scikit-learn y MLflow se limitan al conteo predictivo Retail, con conjuntos versionados, PostgreSQL de metadatos y Blob para artefactos. El modelo multimodal no se atribuye a scikit-learn.
- Originación conserva evaluación, cupo y autorización; Cartera conserva cuentas y saldos. Los metadatos de Evidencia financiera se separan de Originación y de sus archivos Blob.
- Seguridad separa Entra ID P2, External ID, Intune, identidades de cargas, Key Vault, Managed HSM, PIM, Bastion, Private Access y los dos productos Defender, además de Sentinel. PIM representa elevación, no transporte de sesiones. Private Access complementa el acceso administrativo; la VPN corporativa permanece.
- Bastion escribe primero en Blob temporal mutable y sin versionado; un trabajador copia y verifica las grabaciones en WORM. La protección de esa ventana temporal requiere pruebas.
- Collector envía registros a Loki, trazas a Tempo y métricas a Prometheus. Grafana autogestionado consulta esas fuentes y Azure Monitor. Se retiran la ruta productiva Collector → Azure Monitor y Azure Managed Grafana. Blackbox y Alerting cubren responsabilidades diferentes de la experiencia real y los SLO operacionales.
- Cada extremo de X-01 emite únicamente auditoría y telemetría de su ámbito. Las referencias mínimas de correlación no permiten compartir payloads, almacenes de registros ni credenciales. NOC/SOC conservan acceso propio; una eventual salud agregada requiere aprobar su contrato mínimo.

Los productos de entrada conservan un símbolo por producto en la vista principal: Front Door, Application Gateway, APIM y API Center. Los símbolos agregados representan instancias, permisos y contratos propios de cada ámbito, según sus rótulos; no habilitan recursos compartidos ni tráfico entre negocios.

## Verificaciones y límites

Las tres especificaciones se validaron y renderizaron mediante el MCP local `diagramas-ancoa`, sin errores ni avisos. El harness de la guía terminó en «TODO EN ORDEN» y los archivos draw.io de entrega pasaron el linter. Se comprobó el XML multipágina, la ausencia de solapamientos de tarjetas, 220 conexiones ortogonales sin atravesarlas y la igualdad de puntos entre SVG y draw.io. Esto no significa que no exista ningún cruce entre líneas.

El [resultado de comprobación](verificacion.json) conserva conteos y controles semánticos. Se verificaron por SHA-256 21 fuentes protegidas: todos los `.tex` presentes y los dos registros de entrada permanecen iguales. SD-03, SD-04 y los demás subdocumentos no se editaron. Tampoco se actualizaron T-12 ni el catálogo oficial de requerimientos.

Las verificaciones son documentales y gráficas. Quedan pendientes ensayos de capacidad, conectividad, recuperación, identidad y operación sobre una plataforma desplegada. No se registra revisión humana formal ni estado «revisado».

## Importación mediante CSV

Abrir **Organizar → Insertar → Avanzado → CSV** y pegar completo [el CSV que conserva las capas](../../../04_Adjuntos/diagramas/diag-04-33_importacion-csv_conservar-capas.csv). Usa `layout: libavoid` para ordenar las aristas conservando posiciones y contenedores. El CSV es una alternativa para la vista principal; el draw.io multipágina conserva los recorridos de la revisión gráfica.

El importador oficial draw.io 32.6.1 se probó localmente, con Chrome sin conexión, origen ficticio, service workers bloqueados y recursos del editor servidos desde archivos locales. Se conservaron 100 objetos, 88 enlaces, sus sentidos y semánticas; cero enlaces atraviesan tarjetas. No se enviaron datos de arquitectura a un servicio externo. La variante `auto` se conserva como alternativa generada, pero no se recomienda para conservar esta composición ni se presenta como validada visualmente en esta revisión.

## Análisis y siguientes decisiones

La [matriz de componentes](matriz-componentes.md) registra responsabilidad, ámbito, entradas, salidas y estado por vista. Los [pendientes](pendientes-y-pruebas.md) separan decisiones humanas, configuración técnica y pruebas propuestas. La [lista de relaciones](relaciones.md) conserva la intención de cada enlace fuera del dibujo.

El generador de especificaciones está en `05_Gestion/scripts/generar_revision_datos_transversales.py`; las plantillas controladas en `.agents/skills/diagramas-ancoa/scripts/render_revision_registros.py`. No se dibujan gráficos libres ni se modifica la paleta desde JSON. El generador conserva como antecedente la figura 4.31. Para una nueva revisión, usar un nombre nuevo de salida en el MCP y conservar esta entrega.

Los iconos proceden del catálogo diagrams, [OpenSearch](https://github.com/opensearch-project/project-website/tree/main/assets/brand) y [OpenMetadata](https://github.com/open-metadata/OpenMetadata/tree/main/openmetadata-ui/src/main/resources/ui/public). Managed HSM usa icono de familia Key Vault y Blackbox el de Prometheus; los nombres distinguen los productos. La conversión SVG → PNG de la marca OpenSearch no altera su diseño.

Uso de IA: Alto en texto y figuras. Registrar en la Tabla 4.17 al incorporar la figura a la propuesta.
