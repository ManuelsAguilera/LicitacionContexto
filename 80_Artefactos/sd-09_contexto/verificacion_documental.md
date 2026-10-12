---
estado: borrador
parte: T7-09
actualizado: 2026-10-11
---
# Verificación documental de la primera matriz

Se verificó la estructura documental y trazabilidad navegable, no el funcionamiento de una solución. La revisión independiente de un agente Luna y las correcciones se registran en [revisión independiente](revision_independiente.md). Ninguna prueba de producto se ejecutó y ninguna aceptación humana se registró.

| Medida | Resultado comprobado | Límite |
| :--- | :--- | :--- |
| Resultados Anexo D | 28 fichas R01–R28 | No acredita catálogo completo ni todos RT. |
| Criterios internos únicos | 115: 58 asociados a resultados y 57 transversales | Repeticiones en vistas/referencias se deduplican; R28 reutiliza R16/R17/R20. |
| Pilotos detallados | 6 temas y 21 criterios | Constituyen diseño de prueba, no ejecución. |
| Grupos transversales | 11 grupos T01–T11 | Selección pertinente; pendiente ampliación T-12 exhaustiva. |
| Brechas centrales | 38: P01–P08 y B01–B30 | Dueños por rol propuestos; sin resolución/aprobación humana. |
| Criterios formulados | 115 con definición de control | Todos condicionados por datos/configuración, decisiones o evidencias futuras; cero cerrados para aceptación. |
| Evidencias ejecutadas/aceptaciones | 0/0 | Todas las evidencias están previstas. |

No se reduce el estado de un criterio a "definido" por tener un ID. R01 carece de tolerancia numérica acordada; T06-02 conserva indicadores de tarea/perfil por fijar; T06-07 requiere decisión de aplicabilidad; T05-06 requiere umbral de alerta; T10-05 requiere estímulos/límites de campaña; T11-01/02/03 conserva marco, madurez e indicadores de datos por completar. Estos ocho criterios identificados tienen parámetros o aplicabilidad abiertos, además de la configuración pendiente de las demás campañas. La lista no afirma que los restantes 107 estén listos para aprobación: cada grupo conserva brechas en el registro central. Las metas del proponente del Anexo D aún requieren validación del cliente.

## Comprobaciones realizadas

Un análisis local de enlaces resolvió 221 referencias locales en los diez archivos de esta carpeta: ningún destino inexistente ni ancla interna ausente. De ellas, 131 referencias `#Lnn` se contrastaron con el número de líneas del archivo origen; ninguna fuera de rango. El chequeo de líneas comprueba existencia, no equivalencia semántica; la revisión documental contrastó las fuentes materiales y los pilotos registran filas Excel exactas. La comparación final de cada fila Anexo D detectó un desplazamiento de una línea: R01 está en L9 y R28 en L36. Se corrigieron las referencias; la comprobación de rango sola no detectaba el error. Los enlaces remotos metodológicos se conservan y no forman parte del chequeo local.

Se contó por expresión de ID completo `C-[RT][0-9]{2}-[0-9]{2}` en resultados, pilotos y transversales, deduplicando referencias. Se comprobó que los 28 encabezados R son únicos, que cada fila de cobertura apunta a su ficha y que los seis pilotos cuentan con ancla explícita. El registro no añade IDs oficiales de requisitos. Las relaciones de resultados no piloto a RF/RNF son las citadas en Anexo D y no se presentan como equivalencias verificadas exhaustivamente en Excel.

La revisión conservó 70 % bloqueante lógica negocio, 80 % objetivo código nuevo, deuda ≤5 % y trazabilidad 100 % cierre de cada etapa. Conservó meses 16/21/56, separación Retail/Emisor/Frontera, responsabilidades compartidas y máximos del Caso separados de P95. Corrigió la atribución del umbral de pentest: sin críticos/altos abiertos es obligatorio cap.20.1, y ejecución por tercero independiente RT-11.20. Se separaron resiliencia autónoma, autonomía de tienda, retorno POS y recuperación DR.

El alcance de escritura fue únicamente esta carpeta nueva de Markdown. Se conservó `80_Artefactos/objetivo_sesion_sd-09.md`. No se editó cuerpo LaTeX, catálogos Excel, Bases, scripts ni otros subdocumentos; no se hizo commit ni push. Los scripts temporales usados para contar y revisar quedaron fuera del repositorio. Se aplicó pasada de RR-24: eliminación de relleno y reparación de frases/espacios, conservando cifras, IDs, componentes y registro formal. Revisión humana pendiente.
