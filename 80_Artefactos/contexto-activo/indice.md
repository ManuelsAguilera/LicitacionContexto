# Contexto activo para el equipo

Actualizado: 25 de octubre de 2026. Leer este archivo al comenzar; abrir de la [matriz de ajustes](matriz-ajustes.md) solo las filas del documento que se trabajará.

## Referencias actuales

- **Arquitectura:** [SD-04](../../02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex): tecnologías, infraestructura, separación Retail/Filial y suministro.
- **Planificación:** [SD-07](../../02_Propuesta/latex_final/sd-07/OnlySimpleSolutions-Subdocumento7.tex): EDT, esfuerzo, recursos, cronograma e implantación.
- Las Bases, el Caso y el Comunicado 10 mantienen su precedencia. SD-04 y SD-07 son las referencias más actualizadas indicadas por el usuario; no implican revisión humana ni aprobación de cada supuesto.
- El resto de los documentos debe conciliarse contra esas referencias. Que un archivo haya sido importado del ZIP o compile no acredita su consistencia.

## Trabajo por documento

| Frente | Ajustar o comprobar | Dependencias |
|---|---|---|
| SD-01 y SD-02, con anexos | Resúmenes, cifras, alcance descrito y remisiones. | SD-04 y SD-07; T-6 y T-22. |
| SD-03 y SD-05 | Servicios, propietarios de datos, interfaces, almacenamiento y cobertura. | SD-04; T-11 y T-12. |
| SD-06 | Metodologías, cadencias, roles y forma de coordinar el proyecto. | SD-07; T-9 y T-10. |
| SD-08 | Riesgos, respuestas y reservas correspondientes al diseño y al plan actuales. | SD-04 y SD-07; T-16. |
| SD-09 | Pruebas, recuperación, aceptación y evidencia prevista. | SD-04 y SD-07; T-13, T-17 y T-18. |
| SD-13 | Innovaciones, componentes, paquetes EDT, calendario y madurez sustentada. | SD-04 y SD-07; T-19. |
| SD-10, SD-11, SD-12 y SD-14 | Desarrollar operación, planes, equipo y consolidación. Aún no tienen fuente LaTeX. | SD-04 y SD-07; T-8, T-11 y T-15. |
| Formularios técnicos | Conciliar cada formulario con su subdocumento; priorizar T-11, T-14, T-15 y T-18. | Inventario, EDT, horas, recursos e implantación. |

## Pendientes compartidos

1. **T-11:** existen dos fuentes divergentes. Conservar ambas y cotejarlas con SD-04 antes de escoger la versión de entrega.
2. **Mensajería:** SD-04 selecciona Service Bus Premium. SD-08 conserva menciones a Event Hubs/Kafka que deben conciliarse; Event Hubs es una alternativa condicionada, no la selección base.
3. **EDT y esfuerzo:** cotejar paquetes, totales y distribución mensual entre SD-07, T-14, T-15 y las innovaciones de SD-13/T-19.
4. **Catálogo:** v3.0 sigue siendo oficial; v3.1 es un borrador conciliado y requiere decisión del equipo antes de reemplazarlo.
5. **Condiciones abiertas:** disponibilidad regional, residencia/recuperación, responsabilidades y pruebas requieren el sustento señalado en la matriz. No convertir una propuesta en una capacidad demostrada.

## Cómo trabajar

- Acordar responsable y alcance por archivo para evitar ediciones simultáneas sobre la misma fuente. Comunicar al equipo los cambios que afecten otros documentos.
- Editar el `.tex` canónico de `02_Propuesta/latex_final/` cuando exista; usar Markdown para partes aún no importadas. Los maestros Markdown conservan estructura y estado.
- `python 05_Gestion/scripts/brief.py T7-NN` localiza la fuente actual; también admite secciones y formularios como `T-11`. Cargar únicamente las Bases, decisiones y anexos pertinentes a esa tarea.
- Usar la matriz como lista de trabajo: **confirmado** identifica un hallazgo sustentado, **por verificar** un cotejo pendiente y **requiere decisión** una definición del equipo. Confirmado no significa corregido.
- Conservar IDs y procedencia. Registrar qué se cambió, dependencias y comprobaciones; solo una persona asigna revisión humana. La edición y compilación LaTeX sigue la skill `exportar`.

Los borradores anteriores, recepciones, auditorías de limpieza, hashes y registros de pruebas son soporte de consulta puntual; no forman parte de la lectura inicial. No cargar directorios completos ni tomar un grafo como sustituto de las fuentes.
