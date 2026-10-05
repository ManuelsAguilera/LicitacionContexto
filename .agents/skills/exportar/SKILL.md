---
name: exportar
description: Única ruta para convertir, formatear o pasar Markdown (.md) a LaTeX con la plantilla corporativa de Only Simple Solutions y compilar a PDF. Usar siempre que se pida leer un subdocumento y pasarlo a LaTeX, aplicar el formato o la plantilla, generar vista previa o PDF final, compilar un subdocumento (sd-NN, T7-NN), editar un .tex de latex_final o incorporar figuras. Nunca escribir LaTeX ni preámbulos a mano ni llamar a pandoc/xelatex directamente.
---

# Exportar la propuesta corporativa

## Regla principal

Todos los subdocumentos T-7 de la propuesta técnica se entregan en el formato corporativo LaTeX: cada uno debe tener una fuente `.tex` editable y un PDF compilado desde esa fuente con `05_Gestion/scripts/exportar_latex.py`. La portada, el estilo interior y la página final son comunes y deben coincidir con la vista previa aprobada. Esta es la única ruta de conversión admitida. No usar build.py, Pandoc a PDF, Chromium/Edge, CSS ni otra plantilla de Markdown: esas rutas producían una segunda composición y fueron retiradas.

Todo subdocumento T-7 sin `.tex` se importa una vez. Desde ese momento `02_Propuesta/latex_final/sd-NN.tex` es la **única fuente** del subdocumento; los `.md` de `02_Propuesta/` quedan **solo como contexto** (si el `.md` y el `.tex` difieren, manda el `.tex` y no se reimporta). Los cambios de contenido pedidos por el usuario se escriben directamente en el cuerpo del `.tex`. Entregar ambos archivos (fuente `.tex` y PDF) cuando se solicite generar o actualizar un subdocumento.

## Qué NO hacer (causas de PDF fuera de plantilla)

- No escribir, copiar ni editar el preámbulo (todo lo anterior a `\begin{document}`). Es la plantilla fija `plantilla/oss-pandoc.latex`; `verificar` lo compara byte a byte.
- No crear `sd-NN.tex` a mano ni con `pandoc` directo; no llamar a `xelatex`/`latexmk` por fuera del script.
- No borrar un `.tex` para forzar una reimportación. `importar --reemplazar` existe, pero solo se usa si el usuario lo pide explícitamente; respalda el anterior en `respaldo/`.
- No poner en el cuerpo `\usepackage`, `\documentclass`, `\pagecolor`, `\newgeometry`, `\setmainfont`, `\hypersetup` ni redefinir macros `\oss…`: el formato lo da `oss.sty`.
- No usar `pdf-handling`, WeasyPrint, Chromium, `docx` ni Mermaid para la propuesta.
- Si una herramienta falta, ejecutar `doctor`, informar al usuario y detenerse; no improvisar otra ruta.

## Antes de exportar

1. Leer AGENTS.md ("Regla de exportación"), 02_Propuesta/latex_final/README.md y esta skill. Verificar herramientas:

   ~~~bash
   python3 05_Gestion/scripts/exportar_latex.py doctor
   ~~~

2. Identificar la parte solicitada (T7-01 a T7-14). Si el usuario pide generar o actualizar todos los documentos de la propuesta, tratarlo como todos los subdocumentos T-7; no incluir formularios ni informes internos, que tienen sus propios formatos.
3. Consultar las fuentes editables:

   ~~~bash
   python3 05_Gestion/scripts/exportar_latex.py estado
   ~~~

4. Si la parte no tiene .tex, importarla una vez:

   ~~~bash
   python3 05_Gestion/scripts/exportar_latex.py importar --parte T7-01
   ~~~

   Sustituir T7-01 por la parte seleccionada. Para importar partes disponibles en lote:

   ~~~bash
   python3 05_Gestion/scripts/exportar_latex.py importar --todo
   ~~~

   La importación sigue la tabla de secciones del maestro 02_Propuesta/sd-NN_*/sd-NN_*.md, preserva el orden numérico y transforma Markdown a LaTeX con la plantilla `plantilla/oss-pandoc.latex` y el filtro `plantilla/oss.lua` (normaliza niveles de título, descarta HTML, rechaza Mermaid). Si el archivo .tex ya existe, no reimportar: editar el `.tex` y compilarlo. Solo con instrucción explícita del usuario:

   ~~~bash
   python3 05_Gestion/scripts/exportar_latex.py importar --parte T7-01 --reemplazar
   ~~~

5. Antes de compilar o entregar:

   ~~~bash
   python3 05_Gestion/scripts/exportar_latex.py verificar
   ~~~

   Si informa "FUERA DE PLANTILLA", corregir el `.tex` según el mensaje (normalmente restaurar el preámbulo o quitar comandos de formato del cuerpo). `compilar` se niega a compilar un `.tex` fuera de plantilla.

## Compilar

Vista previa de una parte:

~~~bash
python3 05_Gestion/scripts/exportar_latex.py compilar --parte T7-01
~~~

Vista previa consolidada de todas las partes LaTeX disponibles:

~~~bash
python3 05_Gestion/scripts/exportar_latex.py compilar --todo
~~~

PDF oficial de una parte o compilación oficial consolidada:

~~~bash
python3 05_Gestion/scripts/exportar_latex.py compilar --parte T7-01 --final
python3 05_Gestion/scripts/exportar_latex.py compilar --todo --final --trabajadores 4
~~~

--final exige referencias y declaración de uso de IA y escribe en 07_Entregables/. No afirmar que la propuesta completa está compilada si faltan partes. --todo sin --final compila solo las fuentes presentes e informa cuáles faltan.

## Formato común que debe conservarse

El paquete compartido 02_Propuesta/latex_final/oss.sty aplica automáticamente:

- portada de una página mediante \ossCover{título}{Subdocumento N}, con planos diagonales azul institucional, azul claro, blanco y verde;
- fotografía de alianza en la cuña derecha, tarjeta blanca más pequeña con ONLY / SIMPLE / SOLUTIONS y logo azul/verde; bordes y sombras;
- marca de agua azul tenue en las páginas interiores, nunca en portada ni página final;
- encabezado y logo minimalista azul en el pie de las páginas interiores;
- página final azul completa y logo blanco mediante \ossFinalPage.

No recrear estos elementos manualmente en cada sd-NN.tex. La macro común y los recursos en recursos/ son la fuente visual. Títulos largos van en la caja de título del subdocumento y deben caber; ajustar la macro compartida solo cuando una prueba revele un fallo, no cambiar el diseño de una sola parte para acomodar el mismo caso.

## Incrustar figuras e imágenes

### Durante la importación desde Markdown

- Usar imágenes locales con sintaxis Markdown: ![Descripción de la figura](ruta/relativa/figura.png).
- Resolver la ruta desde el archivo .md de sección, no desde la raíz.
- Formatos admitidos: PDF, PNG, JPG/JPEG y SVG.
- El importador copia cada imagen a 02_Propuesta/latex_final/figuras/ con un hash en el nombre para evitar colisiones y preservar procedencia. Convierte SVG a PDF con Inkscape para XeLaTeX.
- Mantener los diagramas como imágenes exportadas en 04_Adjuntos/diagramas/; no usar bloques Mermaid. Si falta la imagen referenciada, corregir o reportar el recurso antes de declarar la importación terminada.

### Edición directa en LaTeX

- Para una figura propia del subdocumento, guardar o copiar el recurso en figuras/ y usar \includegraphics:

  ~~~latex
  \begin{figure}[htbp]
    \centering
    \includegraphics[width=0.82\linewidth]{figuras/diagrama-sistema.pdf}
    \caption{Descripción concreta de la figura.}
    \label{fig:diagrama-sistema}
  \end{figure}
  ~~~

- Para imágenes anchas usar width=\linewidth; para imágenes pequeñas o logos indicar un ancho explícito. No estirar sin conservar proporción.
- Para imágenes en línea, como marcas de agua, portada y logos, usar recursos del directorio recursos/; están gestionados por oss.sty.
- Preferir SVG como fuente editable más PDF vectorial para inclusión en XeLaTeX. PNG/JPEG son adecuados para fotografías. No enlazar rutas absolutas fuera del repositorio.
- Verificar que la imagen aparece en el PDF, que no queda cortada y que su texto/leyenda se lee.

## Verificación y entrega

1. Revisar el mensaje del exportador: debe indicar ruta, páginas y duración. Si se modificó el exportador o la plantilla, correr `python3 -m unittest discover -s 05_Gestion/tests -v`.
2. Abrir o renderizar al menos la portada y una página interior; en una compilación consolidada, revisar también límites entre subdocumentos y hoja final.
3. Confirmar tamaño carta, texto seleccionable, recursos visibles y ausencia de error de XeLaTeX.
4. Para PDF oficial, confirmar nombres de archivos en las carpetas de entregables y el consolidado.
5. Entregar la ruta del PDF al usuario e indicar si fue vista previa o versión oficial.

### Rutas de salida

- Fuente final editable: 02_Propuesta/latex_final/sd-NN.tex
- Auxiliares ignorados por Git: 02_Propuesta/latex_final/build/
- Vista previa individual y consolidada: 05_Gestion/reportes/vistas_previas/
- PDF oficial por subdocumento: 07_Entregables/sobre_2_tecnico/
- PDF oficial consolidado: 07_Entregables/pdf_final/

## Prompt corto para usuarios

Si el usuario dice “compila con el formato corporativo LaTeX”, usar esta skill y el script indicado arriba. Para una parte nueva, importar solo si no existe su .tex; luego compilar. No pedirle al usuario que recuerde rutas ni comandos.
