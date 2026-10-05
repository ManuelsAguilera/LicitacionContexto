"""Apoyo común: carga exportar_latex y arma una parte ficticia en un directorio temporal."""

from __future__ import annotations

import base64
import shutil
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import exportar_latex as ex  # noqa: E402

REPO = ex.ROOT
REAL_LATEX = REPO / "02_Propuesta" / "latex_final"
# PNG de 1x1 píxel.
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
)

MAESTRO = """---
titulo: Prueba & control_de 100% formato
---
# Subdocumento de prueba

| N | Sección | Archivo |
| :--- | :--- | :--- |
| 1 | Introducción | `sd-99_s1_introduccion.md` |
| 2 | Detalle | `sd-99_s2_detalle.md` |
"""

SECCION_1 = """---
id: T7-99-1
---
# 9.1 Introducción

Texto con símbolos & % _ # y <br> salto.

<!-- comentario de migración -->

#### Subtítulo con salto de nivel

![Figura de prueba](figura.png)
"""

SECCION_2 = """---
id: T7-99-2
---
# 9.2 Detalle

| Código | Descripción |
| :--- | :--- |
| R-01 | Primera fila |
| R-02 | Segunda fila |

```python
print("hola")
```
"""


@contextmanager
def proyecto_temporal(secciones: dict[str, str] | None = None):
    """Crea ROOT/02_Propuesta/sd-99_prueba/ y redirige las rutas del módulo a ese directorio.

    Usa la parte T7-14 internamente (el script solo admite T7-01..T7-14) con carpeta sd-14.
    """
    tmp = Path(tempfile.mkdtemp(prefix="oss-test-"))
    try:
        folder = tmp / "02_Propuesta" / "sd-14_prueba"
        folder.mkdir(parents=True)
        textos = {
            "sd-14_prueba.md": MAESTRO.replace("sd-99", "sd-14"),
            "sd-14_s1_introduccion.md": SECCION_1,
            "sd-14_s2_detalle.md": SECCION_2,
        }
        textos.update(secciones or {})
        for name, text in textos.items():
            (folder / name).write_text(text, encoding="utf-8")
        (folder / "figura.png").write_bytes(PNG)
        latex = tmp / "02_Propuesta" / "latex_final"
        latex.mkdir(parents=True)
        shutil.copy2(REAL_LATEX / "oss.sty", latex / "oss.sty")
        shutil.copytree(REAL_LATEX / "recursos", latex / "recursos")
        patches = {
            "ROOT": tmp,
            "LATEX": latex,
            "FIGURES": latex / "figuras",
            "MANIFEST": latex / "manifiesto.json",
            "BUILD": latex / "build",
            "BACKUPS": latex / "respaldo",
            "PREVIEWS": tmp / "vistas_previas",
            "OFFICIAL": tmp / "sobre_2",
            "CONSOLIDATED": tmp / "pdf_final",
        }
        with mock.patch.multiple(ex, **patches):
            yield tmp, latex
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def tex_valido() -> str:
    """Un .tex mínimo que respeta la plantilla, construido desde la plantilla real."""
    return ex.template_preamble() + "\\begin{document}\n\\ossCover{T}{Subdocumento 1}\n\\tableofcontents\n\\clearpage\nHola.\n\n\\ossFinalPage\n\\end{document}\n"
