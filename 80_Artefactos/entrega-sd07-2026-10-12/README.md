# Subdocumento 7 y formularios T-14, T-15 y T-18

Paquete de revisión preparado el 12 de octubre de 2026 para la rama `codex/subdoc7-formularios-entrega`. Reúne los textos aportados por el equipo y sus imágenes. No acredita aprobación técnica ni cierre de los pendientes.

## Documentos

| Documento | LaTeX | Markdown |
| --- | --- | --- |
| Subdocumento 7 — Plan de trabajo, EDT, cronograma e implantación | [sd-07.tex](sd-07.tex) | [sd-07.md](sd-07.md) |
| T-14 — EDT, cronograma y secuenciamiento | [form-T-14.tex](form-T-14.tex) | [form-T-14.md](form-T-14.md) |
| T-15 — Nivelación de recursos, ruta crítica y holguras | [form-T-15.tex](form-T-15.tex) | [form-T-15.md](form-T-15.md) |
| T-18 — Implantación y puesta en marcha | [form-T-18.tex](form-T-18.tex) | [form-T-18.md](form-T-18.md) |

Los archivos LaTeX conservan el contenido de los adjuntos. El T-15 procede de la versión v2 preparada previamente, porque no se adjuntó una versión nueva. Los Markdown son copias de lectura del contenido de estos LaTeX, con tablas e imágenes enlazadas mediante rutas relativas.

## Pendiente: personas peak del T-15

**Falta calcular la cantidad máxima de personas simultáneas por cada tramo exigido en el formulario.**

1. Etapa 1 — Desarrollo, M1–12.
2. Etapa 1 — Marcha blanca, M13–15.
3. Etapa 2 — Desarrollo, M13–18.
4. Etapa 2 — Marcha blanca, M19–20.
5. Operación, M21–56.

Para completar esas cinco filas deben distribuirse las HH por rol y período, establecerse dedicaciones y capacidad efectiva, y comprobarse la concurrencia de tareas. En M13–15 y M19–20 no se debe asignar dos veces la misma capacidad a equipos compartidos. En operación deben considerarse turnos, guardias, reemplazos y cobertura de los servicios, conciliándolos con los subdocumentos 10 y 12.

La división HH/160 incluida en el T-15 expresa capacidad equivalente bajo una hipótesis de 160 HH mensuales; **no constituye el cálculo de personas reales ni demuestra dotación suficiente**. Las reservas del Capítulo 6 deben aplicarse sin contar dos veces las mismas tareas. La columna de personas peak se mantiene pendiente, sin inventar valores.

## Imágenes y procedencia

- [figuras/sd07-figuras/](figuras/sd07-figuras/) contiene las 21 imágenes utilizadas: EDT general, quince ramas, curva HH, Gantt completa y cronogramas de las dos etapas y de operación.
- Las ramas que solo tenían fuente draw.io local se exportaron nuevamente como PNG, conservando nodos, textos y conexiones. Sus fuentes están en [fuentes-diagramas/](fuentes-diagramas/). Se ajustó su número de figura a la numeración del documento adjunto.
- Se corrigió el enlace de la figura de Operación del subdocumento 7, que repetía la imagen de la Etapa 2.
- La imagen del T-14 denominada `prism-uploads/download.png` se vinculó a la Gantt completa disponible. No se usa la Gantt resumida en este paquete: el texto adjunto describe la vista por cuentas.
- Las portadas de T-14 y T-18 identifican ahora su formulario en lugar de «Subdocumento 1». No se modificaron los preámbulos aportados.
- `oss.sty` y `recursos/` son copias de los recursos corporativos existentes, incluidas para acompañar las fuentes completas.

## Uso y límites de verificación

Las rutas de las figuras se resuelven desde esta carpeta. El T-15 es un fragmento para insertar en el documento principal mediante `\input{form-T-15.tex}`; no tiene preámbulo propio. Los otros tres archivos conservan el preámbulo de sus respectivos adjuntos.

Se comprobaron las referencias de imágenes, la existencia de los recursos y la conversión de tablas a Markdown. No se generaron PDF nuevos: el diagnóstico del exportador indica que faltan Pandoc, XeLaTeX y latexmk. La lectura visual de los documentos compilados queda pendiente.

Este paquete conserva la versión recibida para revisión en una rama separada. No reemplaza automáticamente los maestros de `02_Propuesta/latex_final/` ni supone una importación desde Prism. La integración posterior al maestro debe seguir el procedimiento de exportación/importación del proyecto.
