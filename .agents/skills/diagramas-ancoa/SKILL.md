---
name: diagramas-ancoa
description: Úsala siempre que haya que crear, editar o revisar un diagrama de arquitectura para la propuesta de Only Simple Solutions a Multitiendas Ancoa (licitación TFEP-01/2026). Limita los diagramas a 11 estilos (L1–L6 lógicos y F1–F5 físicos) basados en el Subdocumento 4 y el Modelo C4, y los valida antes de dibujarlos.
---

# Diagramas de arquitectura Ancoa: catálogo cerrado

Esta skill es un **harness**: la IA solo puede producir diagramas de los 11 estilos del catálogo, con la
paleta, los trazos, los íconos y los códigos del Subdocumento 4. Todo diagrama pasa por una especificación
JSON, un validador y un renderizador. No se dibuja nada a mano.

## Reglas que no se negocian

1. **Solo estos estilos:** L1 vista lógica general, L2 capas, L3 bloque funcional, L4 recorrido de proceso,
   L5 autoridad de datos, L6 emplazamiento lógico, F1 topología de sitios, F2 red y segmentación,
   F3 ambientes y despliegue, F4 puntos de falla y conmutación, F5 detalle de sitio.
   Para una referencia con columnas Cliente–Presentación–Negocios–Servicios–Datos e iconos, usar
   **L2 con `composicion: columnas_referencia`**. El usuario autorizó esta variante el 21-10-2026.
   Revisión autorizada: sin Cliente, Integración entre Servicios y Datos, códigos solo en JSON
   y conectores de colores con puertos de borde y codos para evitar obstáculos. Conserva las ocho capas RT mediante Borde/Puerta de enlace,
   Integración y bandas transversales de Seguridad y Observabilidad. La referencia posterior con
   Borde y Gateway separados y productos por nombre/icono usa `composicion: columnas_organizadas`. Leer [la variante L2](references/capas-referencia.md). La revisión del registro D-01–D-56 y las referencias del 22-10-2026 usa `composicion: columnas_decisiones`: servicios por área, plataformas externas en capa 4 y un único símbolo Front Door para perfiles separados.
   La iteración aprobada del 22-10-2026 usa L2 `bandas_horizontales`: ocho franjas, tecnologías/gobierno a la izquierda, externos a la derecha y servicios por área. La corrección posterior del usuario elimina la fila de actores; comienza en Presentación. Véase el ejemplo `L2_bandas_horizontales.json`.
2. **Prohibido:** Mermaid, PlantUML, DOT escrito a mano, D2, Excalidraw, ASCII, SVG o imágenes generadas
   libremente; UML de clases, secuencia o casos de uso; BPMN; entidad-relación; mapas mentales; Gantt;
   isométricos o 3D; C4 nivel 4 (código); íconos de AWS, GCP u otros proveedores. Si el pedido es uno de estos,
   explica en una frase que está fuera del catálogo y ofrece el estilo más cercano (por ejemplo, una secuencia → L4)
   o una tabla. Una excepción solo vale si el usuario la pide expresamente sabiendo que rompe el catálogo.
3. **Nunca** se escriben colores, formas, fuentes ni estilos de línea. Se declaran `frente`, `estado` y
   `semantica`, y el catálogo decide el aspecto. El validador rechaza cualquier atributo libre.
4. **Línea roja Retail–Emisor:** el único enlace directo entre ambos frentes es `compra_autorizable`
   (y `denegado` en L5 para mostrar lo que no cruza). Todo lo demás pasa por X-01. El validador lo impone.
5. **Mismos nombres en todas las figuras:** servicios con código del Subdocumento 3 (R:M-01, R:V-02, R:CL-01,
   F:C-01, X-01), elementos locales L-01..L-03, actores AH/AS, sitios SIT/CD/DC/CLD/EXT.
6. Cada figura lleva **título** con tipo y alcance, **leyenda** generada a partir de lo que usa (no se edita a
   mano) y **fuente** («Fuente: elaboración propia a partir de …»).

## Flujo de trabajo

1. **Clasificar.** Elige el estilo con el árbol de decisión de `references/estilos.md`. Si el contenido no cabe
   en el máximo de nodos, divídelo en varios diagramas del mismo estilo; no mezcles estilos en una figura.
2. **Mirar la referencia.** Abre `references/figuras/fig_4_N.png` de la figura de referencia del estilo con la
   herramienta de lectura de imágenes, para copiar disposición y densidad.
3. **Escribir la especificación** en JSON siguiendo la plantilla del estilo en `references/estilos.md` y los
   ejemplos de `ejemplos/`. Los valores permitidos (tipos de nodo, íconos, semánticas, estados, frentes)
   están en `catalogo.json`.
4. **Validar:** `python3 scripts/validar.py espec.json`. Corrige todos los errores. Los avisos se corrigen o se
   justifican al usuario.
5. **Renderizar:**
   - Estilos L: `python3 scripts/render_logico.py espec.json salida/nombre` → `.png`, `.svg`, `.leyenda.txt`
   - Estilos F: `python3 scripts/render_fisico.py espec.json salida/nombre` → `.drawio`, `.leyenda.txt`;
     vista previa opcional con `python3 scripts/previsualizar_drawio.py salida/nombre.drawio salida/nombre.png`.
6. **Revisar la imagen** (ábrela y mírala) con la lista de C4 de abajo. Si hay cruces o rótulos tapados,
   reordena nodos o grupos en el JSON y vuelve a renderizar. En draw.io se puede ajustar el trazado a mano
   después, pero sin cambiar íconos, colores ni trazos.
7. **Entregar** la imagen o el `.drawio`, el pie de figura de `.leyenda.txt` y el JSON (para versionarlo). Recuerda
   al usuario registrar el diagrama como nivel «Alto» de uso de IA en la Tabla 4.17 si la IA lo generó.

Si se edita a mano un archivo generado (`.py` de diagrams, `.drawio`, un `.md` con diagramas), pásalo por
`python3 scripts/lint.py archivo` antes de entregarlo.

## Lista de revisión (Modelo C4, adaptada)

- ¿El título dice el tipo y el alcance? ¿Hay leyenda y explica cada color, trazo e ícono usado?
- ¿Cada elemento tiene nombre, se entiende su tipo y lo que hace, y lleva código cuando es servicio?
- ¿Cada flecha que cruza de un contenedor a otro dice su intención y su dirección es correcta?
- ¿Se entienden todas las siglas (si no, explicarlas en el texto que acompaña)?
- ¿Retail y Emisor aparecen separados, con X-01 entre ellos cuando corresponde?
- ¿Lo propuesto, lo condicionado y lo por acreditar se distingue de lo existente?

## Instalación (una vez por entorno)

En este repositorio está instalado el MCP local `diagramas-ancoa`. Consultar
[instalación y pruebas](references/instalacion-mcp.md) para usarlo o reinstalarlo.
Expone `catalogo_diagramas`, `validar_diagrama` y `renderizar_diagrama`. Esta última herramienta
recibe JSON, aplica el validador y llama al renderizador de la familia correspondiente.
No acepta código Python del cliente. La instalación local conserva los scripts originales del ZIP.

```bash
pip install diagrams playwright   # Graphviz (dot) debe estar instalado en el sistema
```

La vista previa de draw.io usa Chromium y descarga el visor e íconos desde github.com/jgraph/drawio.
Para la versión final, abre el `.drawio` en draw.io y exporta a PNG o PDF.

## Mantenimiento

- `catalogo.json` es la única fuente de verdad. Para agregar un ícono o una semántica, edita el catálogo y
  ejecuta `python3 scripts/probar_harness.py`; debe terminar en «TODO EN ORDEN».
- Un estilo nuevo solo se agrega cuando el equipo lo aprueba y existe una figura de referencia en la propuesta.
