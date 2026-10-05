# Fuentes LaTeX de edición final

Todos los subdocumentos T-7 deben tener una fuente `.tex` editable y su PDF en el formato corporativo. El exportador `05_Gestion/scripts/exportar_latex.py` importa Markdown **una vez** para crear `sd-NN.tex`. Desde entonces, el `.tex` es la única fuente del subdocumento y del PDF; los `.md` de `02_Propuesta/` quedan solo como contexto. El importador nunca sobrescribe un `.tex` existente salvo con `--reemplazar`, que primero lo respalda en `respaldo/`.

Comandos desde la raíz del repositorio:

```bash
python3 05_Gestion/scripts/exportar_latex.py doctor      # herramientas: pandoc, xelatex, latexmk, fuente, pypdf
python3 05_Gestion/scripts/exportar_latex.py estado      # qué partes tienen .tex y si respetan la plantilla
python3 05_Gestion/scripts/exportar_latex.py importar --parte T7-04
python3 05_Gestion/scripts/exportar_latex.py verificar   # lint de plantilla (también lo hace compilar)
python3 05_Gestion/scripts/exportar_latex.py compilar --parte T7-01
python3 05_Gestion/scripts/exportar_latex.py compilar --todo --final --trabajadores 4
python3 -m unittest discover -s 05_Gestion/tests -v      # pruebas del exportador
```

Dependencias Python: `python3 -m pip install -r 05_Gestion/requirements.txt`.

`compilar` sin `--final` produce PDF de vista previa en `05_Gestion/reportes/vistas_previas/`. `--final` exige las secciones Referencias y Declaración de uso de IA en el `.tex` y produce los PDF oficiales separados y el consolidado. Los formularios y anexos siguen en archivos aparte.

Esta es la única ruta para generar las vistas previas y los PDF oficiales del formato corporativo.

## Edición colaborativa en Prism

`latex_final/` no se sube a Prism tal cual (mezcla los 14 subdocumentos con `plantilla/`, `build/`, `respaldo/`, SVG y figuras de otras partes). Cada subdocumento tiene su paquete autocontenido:

```bash
python3 05_Gestion/scripts/exportar_latex.py prism-empaquetar --parte T7-03   # o --todo
# genera 05_Gestion/build/prism/sd-03.zip (sd-03.tex, oss.sty, recursos/ sin SVG, solo sus figuras, LEEME-PRISM.txt)
```

1. Crear un proyecto en Prism importando el zip y editar el cuerpo (el preámbulo, `oss.sty` y `recursos/` no se tocan).
2. Descargar el proyecto como zip desde Prism.
3. La persona responsable del subdocumento ejecuta `prism-importar --parte T7-03 --zip <archivo> --dry-run` y luego sin `--dry-run`. Se valida con la plantilla, se respalda el `.tex` anterior en `respaldo/` y se copian las figuras nuevas.
4. Compilar el PDF oficial local con `compilar --parte T7-03` y hacer commit.

Una persona por subdocumento empaqueta e importa; el resto edita en Prism. Si el `.tex` del repositorio cambia mientras el equipo edita en Prism, `prism-importar` se niega (`--forzar` para reemplazar). `prism-prueba` genera `prueba-A-xelatex.zip` (plantilla real) y `prueba-B-pdflatex.zip` para comprobar qué motor admite Prism. La vista previa de Prism puede diferir en tipografía del PDF oficial.

## Plantilla

- `plantilla/oss-pandoc.latex`: preámbulo fijo. Su primera línea `% oss-plantilla: <versión>` se copia a cada `sd-NN.tex`. `verificar` exige que el preámbulo de cada `.tex` sea idéntico. Para cambiar el formato, editar la plantilla u `oss.sty`, subir la versión, actualizar `05_Gestion/tests/golden/preambulo.tex` y regenerar los `.tex` con `--reemplazar` (con respaldo).
- `plantilla/oss.lua`: filtro de importación. Normaliza los niveles de título (sin saltos), convierte `<br>` en salto de línea, descarta el resto del HTML y los comentarios, quita el resaltado de código y rechaza Mermaid.
- `oss.sty`: formato visual. En cada página de contenido incorpora la marca de agua tenue y el logo azul en el pie. `\ossCover{título}{subdocumento}`, que el importador añade automáticamente, genera la portada geométrica con fotografía, tarjetas, bordes y sombras. `\ossFinalPage`, también añadido por el importador, crea la página final azul con el logo blanco. Los recursos están en `recursos/`.

Las figuras son imágenes PDF, PNG o JPEG dentro de `figuras/` y se enlazan desde el `.tex` con `\includegraphics`. `respaldo/` guarda las versiones previas de los `.tex` regenerados.

Para un documento individual también se puede abrir `sd-NN.tex` en un editor LaTeX y compilarlo allí, pero el PDF oficial sale de `exportar_latex.py compilar`.
