"""Estado real del repositorio: los .tex existentes y las instrucciones para agentes."""

import re
import unittest

from apoyo import REAL_LATEX, REPO, ex

GOLDEN = REPO / "05_Gestion" / "tests" / "golden" / "preambulo.tex"


class RepoTexTest(unittest.TestCase):
    def test_todos_los_tex_respetan_la_plantilla(self):
        texs = sorted(REAL_LATEX.glob("sd-[0-9][0-9].tex"))
        self.assertTrue(texs, "no hay sd-NN.tex en latex_final/")
        for tex in texs:
            with self.subTest(tex=tex.name):
                self.assertEqual(ex.verify_tex(tex), [], f"{tex.name}: ejecutar exportar_latex.py verificar")

    def test_preambulo_golden(self):
        """Cambiar la plantilla exige actualizar golden/preambulo.tex a conciencia (y subir la versión)."""
        self.assertEqual(ex.template_preamble(), GOLDEN.read_text(encoding="utf-8"))


INSTRUCCIONES = [
    REPO / "AGENTS.md",
    REPO / "CLAUDE.md",
    REPO / ".agents" / "skills" / "exportar" / "SKILL.md",
    REPO / ".opencode" / "skills" / "licitacion-workflow" / "SKILL.md",
    REPO / ".opencode" / "plugins" / "activar-skills.ts",
    REPO / "02_Propuesta" / "latex_final" / "README.md",
]


class InstruccionesTest(unittest.TestCase):
    """Evita que vuelvan las instrucciones contradictorias que desvían a los agentes."""

    def test_mencionan_el_exportador(self):
        for path in INSTRUCCIONES:
            if path.suffix == ".ts" or path.name == "SKILL.md" and "licitacion" in str(path):
                continue
            with self.subTest(path=path.name):
                self.assertIn("exportar_latex.py", path.read_text(encoding="utf-8"))

    def test_no_mandan_la_exportacion_a_pdf_handling(self):
        for path in INSTRUCCIONES:
            text = path.read_text(encoding="utf-8")
            for line in text.splitlines():
                if re.search(r"export|PDF", line, re.I) and "pdf-handling" in line and not re.search(r"no usar|no se usa|nunca|prohib", line, re.I):
                    self.fail(f"{path.name}: dirige la exportación a pdf-handling: {line.strip()}")

    def test_no_recomiendan_mermaid(self):
        for path in INSTRUCCIONES:
            text = path.read_text(encoding="utf-8")
            for line in text.splitlines():
                if "```mermaid" in line and not re.search(r"no |nunca|prohib|rechaza", line, re.I):
                    self.fail(f"{path.name}: recomienda bloques Mermaid: {line.strip()}")


if __name__ == "__main__":
    unittest.main()
