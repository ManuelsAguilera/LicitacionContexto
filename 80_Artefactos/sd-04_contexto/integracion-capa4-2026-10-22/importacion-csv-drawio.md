# CSV importable para draw.io

Estado: exportación probada con el importador oficial draw.io 32.6.1 en Chrome local sin conexión. Conserva la VPN, los 84 componentes y las 76 conexiones de la figura 4.31. No cambia alcance, protocolos ni decisiones pendientes; F:C-04 continúa como candidato. Incluye 14 contenedores, título y leyenda: 100 filas gráficas, no 100 componentes de arquitectura.

## Archivos

- [CSV recomendado: conservar capas](../../../04_Adjuntos/diagramas/diag-04-32_importacion-csv_conservar-capas.csv).
- [Draw.io ya importado](../../../04_Adjuntos/diagramas/diag-04-32_importacion-csv_conservar-capas.drawio).
- [SVG del resultado importado](../../../04_Adjuntos/diagramas/diag-04-32_importacion-csv_conservar-capas.svg).
- [CSV alternativo con layout auto](../../../04_Adjuntos/diagramas/diag-04-32_importacion-csv_auto.csv).
- [Verificación de importación](verificacion-csv.json).

## Importación

1. Abrir un diagrama nuevo en draw.io.
2. Abrir el CSV como texto y copiar todo su contenido, incluidas las instrucciones que empiezan con `#`.
3. Ir a **Organizar → Insertar → Avanzado → CSV**, sustituir el ejemplo y pulsar Importar.
4. Guardar como `.drawio`. Se incluye también el resultado ya importado para abrirlo directamente.

Los iconos están embebidos: el archivo pesa aproximadamente 1,2 MB y no necesita descargar logos. No se abre como una tabla de Excel. Una segunda importación con los mismos IDs actualiza formas, pero draw.io no reconstruye automáticamente las conexiones anteriores; para regenerar toda la figura usar un lienzo nuevo.

## Configuración de distribución

La variante recomendada conserva la agrupación de capas, áreas y bandas transversales verticales, con contenedores que se ajustan a su contenido. Sus instrucciones esenciales son:

```text
# identity: id
# namespace: ancoa-csv-
# parent: parent
# layout: libavoid
# nodespacing: 70
# levelspacing: 140
# edgespacing: 20
# connect: {"from":"a_solicitud","to":"id","style":"edgeStyle=orthogonalEdgeStyle;rounded=0;endArrow=block;endFill=1;"}
```

El archivo completo agrega las columnas, estilos/iconos del catálogo, conexiones por semántica y puertos de borde para dos salidas del área Venta que necesitaban evitar tarjetas. Las flechas conservan dirección y color; no llevan referencias documentales en el dibujo.

La variante alternativa usa `# layout: auto`. En este grafo con varias raíces y ciclos, la selección automática dispersa los grupos y empeora la lectura por capas. Se entrega para reproducir la opción solicitada, pero no como resultado recomendado. `orthogonalEdgeStyle` es un estilo de conector; `# layout: orthogonalEdgeStyle` no es una configuración válida. `libavoid` enruta conectores evitando obstáculos y conserva las posiciones; `auto` decide la distribución de las cajas. Ninguno promete eliminar todos los cruces entre líneas de un grafo complejo. La configuración se ejecuta al importar; el enrutamiento continuo al mover formas es una opción adicional del editor.

Fuentes oficiales: [CSV de draw.io](https://www.drawio.com/docs/manual/insert/insert-from-csv/), [distribución y libavoid](https://www.drawio.com/docs/reference/json-layout-specification/), [enrutamiento de conectores](https://www.drawio.com/docs/manual/connectors/connectors-auto-route/). Especificación arquitectónica: figura 4.31 y su registro de integración; la prueba de sintaxis no constituye evidencia de despliegue.

## Comprobaciones

Se comprobó la especificación con una instancia nueva del MCP local, sin errores ni avisos. Ambas importaciones conservaron todos los terminales, sentidos y semánticas. Se verificaron rótulos, estilos e identidades. La prueba real se ejecutó con recursos oficiales previamente descargados usando datos ficticios, origen local ficticio, Chrome offline, service workers bloqueados y solicitudes resueltas desde archivos o abortadas. No se enviaron componentes ni conexiones al servicio externo. SD-03/SD-04/SD-05 permanecen intactos.

Reproducción de la exportación: `python 05_Gestion/scripts/exportar_csv_drawio.py`. El JSON de la figura 4.31 y su `.drawio` siguen siendo la entrada; no se editan por separado las listas de conexiones del CSV. La fuente original queda preservada. Registrar IA Alto en Tabla 4.17 al incorporar la figura a la propuesta; aquí no se modifica esa tabla.
