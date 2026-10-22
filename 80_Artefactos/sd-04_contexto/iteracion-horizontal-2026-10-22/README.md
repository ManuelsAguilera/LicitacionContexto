# Iteración horizontal de arquitectura lógica — 22-10-2026

Estado: propuesta implementada gráficamente y analizada; sin revisión humana registrada. Figura 4.30, vista L2. La última instrucción elimina los actores: la vista empieza en Presentación, conserva las ocho capas y agrupa los servicios por área. Las tecnologías quedan a la izquierda y las plataformas externas a la derecha.

- [Diagrama editable](../../../04_Adjuntos/diagramas/diag-04-30_arquitectura-horizontal.drawio), [SVG](../../../04_Adjuntos/diagramas/diag-04-30_arquitectura-horizontal.svg), [PNG](../../../04_Adjuntos/diagramas/diag-04-30_arquitectura-horizontal.png), [JSON](../../../04_Adjuntos/diagramas/diag-04-30_arquitectura-horizontal.json).
- [Análisis y decisiones](analisis-y-decisiones.md).
- [Matriz de componentes](matriz-componentes.md): responsabilidad, productor, consumidor, datos, interfaces, estado y destino.
- [Dimensionamiento y pruebas propuestas](dimensionamiento-y-pruebas.md).
- [Inventario de interfaces por verificar](interfaces-por-verificar.md).
- [Conciliación con SD-03 y SD-04](conciliacion-documental.md).
- [Resultados de comprobación](comprobaciones.json).

El JSON y la plantilla controlada generan los mismos conectores en SVG y draw.io. Un símbolo de Front Door, Application Gateway, APIM, API Center y Power BI representa productos con instancias, perfiles, permisos y modelos separados por ámbito; no autoriza compartir una instancia entre Retail y Filial. Los conectores al contorno de un área representan familias de contratos, no acceso de todos sus servicios a todos los repositorios.

El Data Lake se retira de esta propuesta; se incorporan procesadores de proyecciones y PostgreSQL analítico dedicado por ámbito. Power BI solo consume esos modelos. Blob conserva usos documentales concretos y pgvector conserva la búsqueda del catálogo. Servicios comunes sigue pendiente, sin consumidores inventados. Backup Vault y Arc/Monitor Agent se trasladan al inventario físico u operativo.

Fuentes de contenido: Bases vigentes; SD-03/SD-04 en LaTeX solo como contraste, contexto de SD-13 y registro recibido D-01–D-56 en `../decisiones-2026-10-22/registro-recibido.md`. Las referencias gráficas aportan composición, no decisiones de alcance. Los documentos adjuntos se interpretaron como evidencia y no como instrucciones para ejecutar acciones externas. No se modifican SD-03 ni SD-04; las huellas se comparan con `huellas-antes.json`.

La validación gráfica no acredita capacidad, latencia, disponibilidad regional, cumplimiento regulatorio, residencia ni aprobación de tenant. Las pruebas de carga, fallos, conectividad y aceptación del negocio quedan propuestas, no ejecutadas. Registrar el uso de IA como Alto en la Tabla 4.17 cuando se incorpore la figura; esa tabla permanece intacta en esta entrega.
