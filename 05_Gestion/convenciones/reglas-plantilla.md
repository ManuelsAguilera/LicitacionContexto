# Reglas de plantilla (formato)

Cómo se ve el documento. **No** definen qué se escribe: eso son las [reglas de redacción](reglas-redaccion.md). Las reglas de plantilla se cumplen mediante `02_Propuesta/latex_final/oss.sty` y `plantilla/oss-pandoc.latex`; quien redacta no las modifica ni las reproduce a mano en un `.tex`.

**Quién las cambia.** Solo quien mantiene la plantilla. Flujo: editar `plantilla/oss-pandoc.latex` u `oss.sty`, subir la versión de la primera línea, actualizar `05_Gestion/tests/golden/preambulo.tex` y ejecutar `exportar_latex.py actualizar-plantilla --todo` (cambia solo el preámbulo; el cuerpo no se toca).

**Verificación.** `exportar_latex.py verificar` (preámbulo idéntico, portada, índice y página final presentes, sin comandos de formato en el cuerpo) y `compilar` (tamaño carta, texto seleccionable).

| ID | Regla de plantilla | Origen | Cómo se cumple |
| :--- | :--- | :--- | :--- |
| RP-01 | Un único preámbulo, portada, marca de agua, encabezado, pie con logo y página final azul iguales en los 14 subdocumentos. | Formato corporativo aprobado | `oss.sty` + `verificar` |
| RP-02 | Página carta vertical, márgenes de 20 mm, letra de cuerpo de 11 pt (nunca menos de 9 pt), idioma español. | C10 §4–5 (Art. 40.4) | `plantilla/oss-pandoc.latex` + `compilar` |
| RP-03 | Todas las tablas comparten un estilo (`longtable` + `booktabs`): encabezado repetido al cambiar de página, sin cortar filas, texto a la izquierda y cifras a la derecha con su unidad. Nunca tablas pegadas como imagen. | C10 §5 «Formato de empresa» | Plantilla; alineación de cifras: autor de la tabla (`:---:`/`---:` en la importación) |
| RP-04 | Las tablas del cuerpo van en orientación vertical; las de anexo pueden ir en horizontal. | C10 §5 | Plantilla |
| RP-05 | Las figuras se escalan al ancho del texto sin deformarse (`\includegraphics`), en PDF, PNG o JPEG, con todo el texto legible sin ampliar (≥ 9 pt impresos). Se admite página horizontal para figuras de gran formato. | C10 §4 | Plantilla + revisión visual |
| RP-06 | Estilo de títulos, enlaces y colores corporativos (azul, azul claro, verde). | Formato corporativo aprobado | `oss.sty` |
| RP-07 | Compila con XeLaTeX (PDF oficial, DejaVu Sans) y con pdfLaTeX (Prism, Helvetica con símbolos Unicode declarados). | Edición colaborativa | `plantilla/oss-pandoc.latex` (`iftex`) |

**Brecha conocida.** El título y la numeración de tablas y figuras («Tabla 3.2: …», «Figura 3.1: …») hoy se escriben como párrafos de texto junto al elemento, no con una leyenda automática de la plantilla. La regla de contenido (RR-11, RR-19) exige que existan; automatizar su formato es una mejora de plantilla pendiente.
