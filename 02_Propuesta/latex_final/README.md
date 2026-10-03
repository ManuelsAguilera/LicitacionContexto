# Fuentes LaTeX de edición final

El exportador `05_Gestion/scripts/exportar_latex.py` importa Markdown **una vez** para crear `sd-NN.tex`. Desde entonces, el `.tex` se edita directamente. El importador nunca sobrescribe un `.tex` existente.

Comandos desde la raíz del repositorio:

```bash
python3 05_Gestion/scripts/exportar_latex.py estado
python3 05_Gestion/scripts/exportar_latex.py importar --parte T7-01
python3 05_Gestion/scripts/exportar_latex.py compilar --parte T7-01
python3 05_Gestion/scripts/exportar_latex.py compilar --todo --final --trabajadores 4
```

`compilar` sin `--final` produce PDF de vista previa en `05_Gestion/reportes/vistas_previas/`. `--final` exige las secciones Referencias y Declaración de uso de IA en el `.tex` y produce los PDF oficiales separados y el consolidado. Los formularios y anexos siguen en archivos aparte.

Las figuras son imágenes PDF, PNG o JPEG dentro de `figuras/`. Se pueden sustituir y enlazar desde el `.tex` con `\includegraphics`.

El formato común está en `oss.sty`. En cada página de contenido incorpora la marca de agua tenue y el logo azul en el pie. El comando `\ossCover{título}{subdocumento}`, que el importador añade automáticamente, genera la portada geométrica con fotografía, tarjetas, bordes y sombras. El comando `\ossFinalPage`, también añadido por el importador, crea la página final azul con el logo blanco. Los recursos vectoriales, la fotografía de portada y sus PDF compatibles con LaTeX están en `recursos/`.

Para un documento individual también se puede abrir `sd-NN.tex` en el editor LaTeX y compilarlo allí.
