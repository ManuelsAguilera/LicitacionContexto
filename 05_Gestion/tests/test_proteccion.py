"""El importador protege los .tex editables y rechaza entradas fuera de norma."""

import shutil
import unittest

from apoyo import SECCION_1, ex, proyecto_temporal

HAS_PANDOC = bool(shutil.which("pandoc"))


@unittest.skipUnless(HAS_PANDOC, "pandoc no instalado")
class ProteccionTest(unittest.TestCase):
    def test_no_sobrescribe_sin_reemplazar(self):
        with proyecto_temporal() as (_, latex):
            tex = ex.import_part("T7-14")
            tex.write_text(tex.read_text(encoding="utf-8") + "% edición manual\n", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                ex.import_part("T7-14")
            self.assertIn("% edición manual", tex.read_text(encoding="utf-8"))

    def test_reemplazar_respalda_el_anterior(self):
        with proyecto_temporal() as (_, latex):
            tex = ex.import_part("T7-14")
            tex.write_text(tex.read_text(encoding="utf-8").replace("Primera fila", "EDITADO A MANO"), encoding="utf-8")
            ex.import_part("T7-14", replace=True)
            respaldos = list((latex / "respaldo").glob("sd-14.*.tex"))
            self.assertEqual(len(respaldos), 1)
            self.assertIn("EDITADO A MANO", respaldos[0].read_text(encoding="utf-8"))
            self.assertNotIn("EDITADO A MANO", tex.read_text(encoding="utf-8"))

    def test_rechaza_mermaid(self):
        mermaid = SECCION_1 + "\n```mermaid\ngraph TD; A-->B\n```\n"
        with proyecto_temporal({"sd-14_s1_introduccion.md": mermaid}) as (_, latex):
            with self.assertRaisesRegex(ValueError, "Mermaid"):
                ex.import_part("T7-14")
            self.assertFalse((latex / "sd-14.tex").exists())

    def test_rechaza_imagen_remota(self):
        remota = SECCION_1.replace("figura.png", "https://example.com/x.png")
        with proyecto_temporal({"sd-14_s1_introduccion.md": remota}):
            with self.assertRaisesRegex(ValueError, "remota"):
                ex.import_part("T7-14")

    def test_rechaza_imagen_ausente(self):
        ausente = SECCION_1.replace("figura.png", "no-existe.png")
        with proyecto_temporal({"sd-14_s1_introduccion.md": ausente}):
            with self.assertRaisesRegex(ValueError, "ausente"):
                ex.import_part("T7-14")


if __name__ == "__main__":
    unittest.main()
