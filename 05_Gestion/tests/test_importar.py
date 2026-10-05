"""La importación Markdown -> LaTeX produce siempre el formato corporativo."""

import re
import shutil
import unittest

from apoyo import ex, proyecto_temporal

HAS_PANDOC = bool(shutil.which("pandoc"))


@unittest.skipUnless(HAS_PANDOC, "pandoc no instalado")
class ImportarTest(unittest.TestCase):
    def setUp(self):
        self.ctx = proyecto_temporal()
        self.tmp, self.latex = self.ctx.__enter__()
        self.tex = ex.import_part("T7-14").read_text(encoding="utf-8")

    def tearDown(self):
        self.ctx.__exit__(None, None, None)

    def test_marcador_y_preambulo_de_plantilla(self):
        self.assertTrue(self.tex.startswith(f"% oss-plantilla: {ex.template_version()}\n"))
        self.assertEqual(self.tex.split("\\begin{document}")[0], ex.template_preamble())
        self.assertIn("\\usepackage{oss}", self.tex)

    def test_portada_indice_y_pagina_final(self):
        body = self.tex.split("\\begin{document}")[1]
        self.assertIn("\\ossCover{Prueba \\& control\\_de 100\\% formato}{Subdocumento 14}", body)
        self.assertIn("\\tableofcontents", body)
        self.assertTrue(body.split("\\end{document}")[0].rstrip().endswith("\\ossFinalPage"))

    def test_verificar_acepta_lo_importado(self):
        self.assertEqual(ex.verify_tex(self.latex / "sd-14.tex"), [])

    def test_tabla_como_longtable(self):
        self.assertIn("\\begin{longtable}", self.tex)
        self.assertIn("R-02", self.tex)

    def test_niveles_de_titulo_sin_saltos(self):
        levels = {"section": 1, "subsection": 2, "subsubsection": 3, "paragraph": 4}
        found = [levels[m] for m in re.findall(r"\\(section|subsection|subsubsection|paragraph)\{", self.tex)]
        self.assertEqual(found[0], 1)
        for previous, current in zip(found, found[1:]):
            self.assertLessEqual(current, previous + 1, found)
        self.assertIn("\\subsection{Subtítulo con salto de nivel}", self.tex)

    def test_html_y_caracteres_especiales(self):
        self.assertNotIn("comentario de migración", self.tex)
        self.assertNotIn("<br>", self.tex)
        self.assertIn("\\& \\% \\_ \\#", self.tex)

    def test_codigo_sin_resaltado(self):
        self.assertNotIn("Shaded", self.tex)
        self.assertIn("\\begin{verbatim}", self.tex)

    def test_figura_copiada_con_hash(self):
        figuras = list((self.latex / "figuras").glob("figura-*.png"))
        self.assertEqual(len(figuras), 1)
        self.assertIn(f"figuras/{figuras[0].name}", self.tex)


if __name__ == "__main__":
    unittest.main()
