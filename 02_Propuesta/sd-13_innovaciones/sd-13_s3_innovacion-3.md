---
id: T7-13-13.3
tipo: seccion
parte: T7-13
titulo: Innovación 3
estado: borrador
bases:
  - "Bases Transversales, RT-16.27 y capítulos 18 y 26"
requisitos: []
depende_de:
  - T7-03
  - T7-04
  - T7-05
  - T7-07
adjuntos: []
jira:
  - OSS-103
cifras:
  - produccion_etapa_2_mes
origen: "80_Artefactos/sd-13_contexto/investigacion_cinco_innovaciones.md, sección 4"
actualizado: 2026-10-11
---
## 13.3 Innovación 3

La innovación tecnológica es Búsqueda vectorial multimodal. Permite consultar el catálogo autorizado mediante una fotografía o una intención expresada en español y recuperar productos pertinentes cuya disponibilidad se verifica en el servicio de existencias. Combina recuperación por significado y similitud visual con búsqueda léxica para marcas, códigos y términos exactos.

### Oportunidad y alcance diferencial

El catálogo de Ancoa y su operación omnicanal requieren que el cliente encuentre productos y reciba una promesa compatible con la existencia real (Multitiendas Ancoa S.A., 2026b, caps. 7–9). La búsqueda con tolerancia a errores, filtros y permisos ya es obligatoria por RT-16.27. Esta innovación agrega recuperación visual y comprensión de intención; no presenta esas funciones base como novedad.

La fotografía devuelve artículos semejantes del catálogo y no garantiza identificar el producto exacto. La recomendación de complementos exige reglas de compatibilidad y evaluación propias, por lo que no se incluye como consecuencia automática del índice vectorial. El levantamiento mide consultas sin resultados pertinentes, reformulaciones y éxito de búsqueda; no presupone que el buscador actual solo reconoce nombres exactos.

### Tecnología y madurez

La arquitectura incorpora un codificador multimodal y un índice de similitud. Jina CLIP v2 constituye la referencia para evaluar texto e imagen en varios idiomas, con contraste frente a alternativas OpenCLIP. La descarga del primero tiene licencia CC BY-NC 4.0; su utilización comercial exige la modalidad habilitada por el proveedor. El suministro incluye la licencia correspondiente si resulta seleccionado (Jina AI, s. f.; ML Foundations, s. f.). La versión de pesos, el código y la ubicación de procesamiento quedan fijados en el acta de diseño.

PostgreSQL con pgvector e índice HNSW constituye la referencia de almacenamiento y recuperación. Se ensaya con filtros y carga real, porque la búsqueda aproximada puede recuperar pocos resultados después de filtrar. La configuración evalúa escaneos iterativos y alternativas de partición antes de dimensionar el servicio (Pgvector contributors, s. f.). La dimensión del vector depende del modelo elegido y de su calidad medida.

Los componentes alcanzan el estado comercial o documental de la escala de evidencia. La integración se valida con un conjunto de consultas, fotografías y juicios de relevancia en español. La prueba de carga y el piloto de usuarios permiten pasar a integración probada y operación aceptada. La documentación de un modelo multilingüe no prueba por sí sola su calidad en expresiones chilenas.

### Incorporación a arquitectura y EDT

El componente pertenece a la capa de aplicación retail. Un trabajador asíncrono genera y actualiza representaciones al cambiar catálogo e imágenes del servicio de oferta comercial. El canal digital entrega la consulta; la recuperación produce candidatos, combina ranking léxico y vectorial y aplica permisos y filtros. El servicio de existencias verifica disponibilidad al mostrar resultados y al iniciar la compra. El índice nunca sustituye al dueño del stock.

El paquete «Búsqueda vectorial multimodal» se ubica en la rama 1.10 Innovaciones. Incluye preparación del conjunto de prueba, selección y licencia del modelo, indexación, integración y evaluación. Se desarrolla y prueba en la Etapa 2, con aceptación antes del mes 21 y entrada en operación en ese mes. Su capacidad se calcula en la memoria del capítulo 4 y su gobierno de datos se integra al capítulo 5.

Las fotografías se procesan con retención mínima definida para la finalidad. El componente elimina metadatos innecesarios, valida formato y tamaño y mantiene auditoría con acceso restringido. El proveedor no entrena con datos del cliente sin autorización expresa. Las sugerencias automáticas se identifican en la interfaz y se documentan límites, trazabilidad y respaldo conforme a RT-18.01 a RT-18.09 (Tabassi, 2023; International Organization for Standardization, 2023).

### Impacto económico

La inversión comprende preparación de catálogo, licencia, integración y pruebas de relevancia y capacidad. El costo operacional incluye inferencia, almacenamiento, actualización del índice y evaluación de cambios. El beneficio se estima mediante margen incremental de compras originadas por una mejora demostrada de búsqueda. La Oferta Económica evita sumar conversiones atribuibles a publicidad o disponibilidad como si fueran exclusivas de esta innovación.

### Verificación del beneficio

Se compara el buscador base con el multimodal mediante consultas equivalentes y juicios de usuarios. Se mide relevancia en las primeras posiciones, recuperación de artículos pertinentes, reformulación, éxito de tarea y latencia de extremo a extremo. La prueba distingue tiempo de subida de foto, inferencia y consulta del índice.

La meta es mejorar relevancia y éxito frente a la línea base, conservando permisos, disponibilidad y límites de respuesta del canal. El protocolo fija los umbrales de mejora y la muestra antes de la evaluación. Se exige que los resultados comerciales remitan a artículos del catálogo y que la desactivación del componente conserve la búsqueda base. La marcha blanca de la Etapa 2 verifica relevancia y carga; desde el mes 21 se controla desempeño con consultas reales bajo la política de conservación.

### Riesgo de adopción y contingencia

La recuperación visual poco pertinente y la calidad desigual del catálogo tienen probabilidad inicial media e impacto alto. Se mitigan mediante evaluación por categoría, filtros y revisión de fichas e imágenes. Cuando la similitud no supera el criterio validado, el canal informa que no encontró coincidencias suficientes y ofrece búsqueda textual.

La incompatibilidad de licencia o de tratamiento de datos tiene probabilidad media e impacto alto. La compra valida derechos de uso y condiciones contractuales antes de producción. Si el modelo no cumple, se sustituye por una alternativa que supere el mismo conjunto de prueba. Durante la sustitución funciona el buscador base. El T-16 revisa estos riesgos con las pruebas y el contrato seleccionado.
