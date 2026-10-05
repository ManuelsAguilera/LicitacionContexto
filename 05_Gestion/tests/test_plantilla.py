"""Cambio de plantilla: el preámbulo se actualiza sin tocar el cuerpo y compila con ambos motores."""

import shutil
import tempfile
import unittest
from pathlib import Path

from apoyo import REAL_LATEX, ex, proyecto_temporal, tex_valido

VIEJO = "% oss-plantilla: oss-2020.01\n% preámbulo antiguo\n\\documentclass{article}\n"


def tex_antiguo() -> str:
    cuerpo = tex_valido().split("\\begin{document}", 1)[1]
    return VIEJO + "\\begin{document}" + cuerpo.replace("Hola.", "Cuerpo editado a mano.")


class ActualizarPlantillaTest(unittest.TestCase):
    def test_cambia_solo_el_preambulo_y_respalda(self):
        with proyecto_temporal() as (_, latex):
            tex = latex / "sd-14.tex"
            tex.write_text(tex_antiguo(), encoding="utf-8")
            self.assertTrue(ex.verify_tex(tex))
            ex.update_template("T7-14")
            self.assertEqual(ex.verify_tex(tex), [])
            self.assertIn("Cuerpo editado a mano.", tex.read_text(encoding="utf-8"))
            self.assertEqual(len(list((latex / "respaldo").glob("sd-14.*.tex"))), 1)

    def test_idempotente(self):
        with proyecto_temporal() as (_, latex):
            (latex / "sd-14.tex").write_text(tex_valido(), encoding="utf-8")
            self.assertIn("ya está vigente", ex.update_template("T7-14"))
            self.assertFalse((latex / "respaldo").exists())

    def test_no_modifica_si_el_cuerpo_viola_la_plantilla(self):
        with proyecto_temporal() as (_, latex):
            tex = latex / "sd-14.tex"
            mal = tex_antiguo().replace("Cuerpo editado a mano.", "\\usepackage{tikz}")
            tex.write_text(mal, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "no cumple la plantilla"):
                ex.update_template("T7-14")
            self.assertEqual(tex.read_text(encoding="utf-8"), mal)


class MotoresTest(unittest.TestCase):
    """El preámbulo vigente debe compilar con XeLaTeX (oficial) y pdfLaTeX (Prism)."""

    @unittest.skipUnless(shutil.which("latexmk"), "latexmk no instalado")
    def test_compila_con_xelatex_y_pdflatex(self):
        cuerpo = (
            "\\ossCover{Prueba}{Subdocumento 0}\n\\tableofcontents\n\\clearpage\n"
            "\\section{Símbolos}\nCobertura ≥ 99,9\\% y latencia ≤ 200 ms — ● ñandú → ✓.\n\n\\ossFinalPage\n"
        )
        texto = ex.template_preamble() + "\\begin{document}\n" + cuerpo + "\\end{document}\n"
        for flag, motor in (("-xelatex", "xelatex"), ("-pdf", "pdflatex")):
            if not shutil.which(motor):
                continue
            with self.subTest(motor=motor), tempfile.TemporaryDirectory() as tmp:
                work = Path(tmp)
                shutil.copy2(REAL_LATEX / "oss.sty", work / "oss.sty")
                shutil.copytree(REAL_LATEX / "recursos", work / "recursos")
                (work / "prueba.tex").write_text(texto, encoding="utf-8")
                import subprocess
                result = subprocess.run(["latexmk", flag, "-interaction=nonstopmode", "-halt-on-error", "prueba.tex"],
                                        cwd=work, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout[-1500:])
                self.assertTrue((work / "prueba.pdf").is_file())


if __name__ == "__main__":
    unittest.main()
