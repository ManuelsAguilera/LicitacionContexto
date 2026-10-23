# Revisión visual de arquitectura: Presentación e Integración

Estado: borrador para revisión humana. Figura 4.24. Esta revisión sustituye visualmente la figura 4.23; no modifica el texto de SD-03 ni incorpora todavía figuras en LaTeX.

## Decisiones aplicadas

- Se elimina la capa Cliente y sus actores. La entrada visible es Presentación.
- Integración y Eventos pasa a ser una columna entre Servicios y Datos.
- Se elimina la franja amarilla. El control de cruces permanece en Seguridad y su bitácora en Datos; no se habilitan cruces nuevos.
- Los códigos de los 13 servicios permanecen en JSON para trazabilidad, sin imprimirse en tarjetas.
- Los conectores usan puertos explícitos en los bordes y segmentos ortogonales. Los codos evitan tarjetas y rótulos; los carriles agrupan recorridos de una misma familia sin fusionar destinos. Azul: API; verde: persistencia; naranja: publicación; violeta: consumo; celeste: sistemas externos.
- Cada servicio conserva autoridad sobre su repositorio lógico. Las cajas no representan necesariamente instancias físicas distintas. El bus no intermedia las consultas ni escrituras.
- Los canales Retail y Emisor identifican productores y consumidores. Outbox pertenece a cada productor; no hay una caja central compartida.
- La puerta de enlace consolida visualmente los grupos de contratos. Los responsables de las cinco innovaciones aparecen en sus tarjetas.
- La compra autorizable Ventas–Originación se declara en el control transversal. Se omiten líneas largas de política. Las autoridades de Búsqueda y POS/Fila se indican en Datos para evitar líneas que parezcan acceder mediante el bus.

Los nombres de eventos son rótulos de diseño; los contratos detallados, esquemas, suscripciones y retención siguen pendientes. Los asteriscos conservan las selecciones por verificar.

## Entrega

- [Imagen PNG](../../../04_Adjuntos/diagramas/diag-04-24_arquitectura-conectores-ortogonales.png)
- [SVG autocontenido](../../../04_Adjuntos/diagramas/diag-04-24_arquitectura-conectores-ortogonales.svg)
- [Fuente draw.io](../../../04_Adjuntos/diagramas/diag-04-24_arquitectura-conectores-ortogonales.drawio)
- [Especificación JSON](../../../04_Adjuntos/diagramas/diag-04-24_arquitectura-conectores-ortogonales.json)

La revisión de conectores sustituye la versión anterior de líneas directas. Se verificaron los 51 conectores: anclajes normalizados sobre el contorno, ausencia de segmentos diagonales, ninguna tarjeta atravesada y los mismos puntos intermedios en la imagen y en draw.io. El archivo `.rutas.json` conserva la evidencia geométrica; la verificación reproducible está en `tmp/ancoa-capas-referencia/verificar_conectores.py`.

Generado mediante el MCP local `diagramas-ancoa`, tras validación sin errores ni avisos. Se revisó el PNG y se comprobó draw.io con el lint de la guía. Las seis especificaciones válidas y los 18 casos negativos del harness pasan. Los dos hashes de SD-03 coinciden con el registro previo. Mantener el registro de uso de IA de nivel Alto al incorporar la figura en la propuesta; no se asigna estado revisado automáticamente.
