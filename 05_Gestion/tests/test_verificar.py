"""verificar detecta cualquier .tex que se aparte de la plantilla corporativa."""

import tempfile
import unittest
from pathlib import Path

from apoyo import ex, tex_valido

TEX_A_MANO = r"""\documentclass{article}
\usepackage{xcolor}
\begin{document}
\section{Hecho a mano}
Texto.
\end{document}
"""


class VerificarTest(unittest.TestCase):
    def check(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sd-99.tex"
            path.write_text(text, encoding="utf-8")
            return ex.verify_tex(path)

    def test_tex_valido_pasa(self):
        self.assertEqual(self.check(tex_valido()), [])

    def test_sin_marcador(self):
        text = tex_valido().split("\n", 1)[1]
        self.assertTrue(any("marcador" in p for p in self.check(text)))

    def test_preambulo_alterado(self):
        text = tex_valido().replace("\\usepackage{oss}", "\\usepackage{oss}\n\\usepackage{geometry}")
        self.assertTrue(any("preámbulo" in p for p in self.check(text)))

    def test_sin_pagina_final(self):
        text = tex_valido().replace("\\ossFinalPage\n", "")
        problems = self.check(text)
        self.assertTrue(any("ossFinalPage" in p for p in problems))

    def test_pagina_final_no_al_final(self):
        text = tex_valido().replace("\\ossFinalPage\n", "\\ossFinalPage\nTexto extra.\n")
        self.assertTrue(any("lo último" in p for p in self.check(text)))

    def test_sin_portada(self):
        text = tex_valido().replace("\\ossCover{T}{Subdocumento 1}\n", "")
        self.assertTrue(any("ossCover" in p for p in self.check(text)))

    def test_tex_hecho_a_mano(self):
        problems = self.check(TEX_A_MANO)
        self.assertGreaterEqual(len(problems), 3, problems)

    def test_paquetes_y_formato_en_el_cuerpo(self):
        for intruso in ("\\usepackage{tikz}", "\\pagecolor{blue}", "\\newgeometry{margin=1cm}",
                        "\\renewcommand{\\ossCover}[2]{}", "\\setmainfont{Arial}"):
            with self.subTest(intruso=intruso):
                text = tex_valido().replace("Hola.", intruso)
                self.assertTrue(any("no se permite" in p for p in self.check(text)), intruso)

    def test_compilar_rechaza_tex_fuera_de_plantilla(self):
        from apoyo import proyecto_temporal
        with proyecto_temporal() as (_, latex):
            (latex / "sd-14.tex").write_text(TEX_A_MANO, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "fuera de la plantilla"):
                ex.compile_part("T7-14", final=False)


if __name__ == "__main__":
    unittest.main()
