# Integración de servicios de capa 4 y limpieza de flujos

Estado: diseño propuesto; validación gráfica local, sin revisión humana registrada.

Figura 4.31: [draw.io editable](../../../04_Adjuntos/diagramas/diag-04-31_arquitectura-servicios-y-flujos.drawio), [SVG](../../../04_Adjuntos/diagramas/diag-04-31_arquitectura-servicios-y-flujos.svg), [PNG](../../../04_Adjuntos/diagramas/diag-04-31_arquitectura-servicios-y-flujos.png), [JSON](../../../04_Adjuntos/diagramas/diag-04-31_arquitectura-servicios-y-flujos.json).

Se conserva la figura 4.30 como antecedente. La nueva figura integra la especificación adjunta y la instrucción posterior: Presentación → Borde → Puerta de enlace; Seguridad y Observabilidad verticales. No hay actores ni Data Lake. Cada producto de entrada conserva un símbolo, con instancias y permisos propios por ámbito.

- [Cambios y decisiones pendientes](integracion-y-pendientes.md).
- [Relaciones y evidencia](relaciones-y-evidencia.md): las fuentes se mantienen fuera de la imagen y de las flechas.
- [Atributos y responsabilidades por servicio](servicios-y-atributos.md).
- [Especificación recibida](especificacion-recibida.md), conservada sin editar.
- [Comprobaciones](comprobaciones.json).

SD-03, SD-04, SD-05, T-12 y Excel no se modifican. La especificación es contexto de diseño; sus recomendaciones no son aprobaciones de alcance ni evidencia automática de cumplimiento. F:C-04 se dibuja como candidato, separado de los trece servicios vigentes. Registrar asistencia IA de nivel Alto en Tabla 4.17 cuando se incorpore la figura a la propuesta; la tabla no se edita aquí.

## Importación CSV posterior

[CSV y distribución automática en draw.io](importacion-csv-drawio.md): VPN conservada, variante recomendada por capas y variante `auto`, con prueba local offline.
