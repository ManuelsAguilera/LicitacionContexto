"""Prueba de humo: importar y compilar una parte ficticia hasta PDF carta con texto."""

import importlib.util
import shutil
import unittest

from apoyo import ex, proyecto_temporal

LISTO = all(shutil.which(t) for t in ("pandoc", "xelatex", "latexmk")) and importlib.util.find_spec("pypdf")


@unittest.skipUnless(LISTO, "faltan pandoc/xelatex/latexmk/pypdf (ver exportar_latex.py doctor)")
class CompilarHumoTest(unittest.TestCase):
    def test_importar_y_compilar(self):
        with proyecto_temporal():
            ex.import_part("T7-14")
            part, pdf, _, pages = ex.compile_part("T7-14", final=False)
            self.assertTrue(pdf.is_file())
            self.assertGreaterEqual(pages, 3, "portada + contenido + página final")
            from pypdf import PdfReader
            reader = PdfReader(str(pdf))
            texto = "".join(p.extract_text() or "" for p in reader.pages)
            self.assertIn("SOLUTIONS", texto)
            self.assertIn("Primera fila", texto)


if __name__ == "__main__":
    unittest.main()
