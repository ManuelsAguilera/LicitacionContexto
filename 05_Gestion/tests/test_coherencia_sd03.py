"""Las pruebas de coherencia de sd-03.tex detectan los defectos que describen.

Se prueban con textos mínimos. Sobre el sd-03.tex real, el verificador solo informa.
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import verificar_coherencia_sd03 as v  # noqa: E402


class NumeracionTest(unittest.TestCase):
    def test_detecta_tabla_repetida(self):
        tex = "Tabla 3.5: Una.\n\ntexto\n\n{Tabla 3.5. Otra.}\nTabla 3.6: Tercera.\n"
        self.assertEqual(len(v.numeracion_duplicada(tex)), 1)
        self.assertIn("Tabla 3.5", v.numeracion_duplicada(tex)[0])

    def test_ignora_menciones_en_el_texto(self):
        tex = "Tabla 3.5: Una.\n\nComo muestra la Tabla 3.5, los datos coinciden.\n"
        self.assertEqual(v.numeracion_duplicada(tex), [])

    def test_ignora_comentarios(self):
        tex = "Figura 3.1. Una.\n% Figura 3.1. Comentada.\n"
        self.assertEqual(v.numeracion_duplicada(tex), [])


class FigurasTest(unittest.TestCase):
    def test_detecta_figura_inexistente(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "figuras").mkdir()
            (Path(tmp) / "figuras" / "ok.png").write_bytes(b"x")
            tex = "\\includegraphics{figuras/ok.png}\n\\includegraphics{figuras/falta.png}\n"
            out = v.figuras_faltantes(tex, tmp)
        self.assertEqual(len(out), 1)
        self.assertIn("falta.png", out[0])


class PlataformasTest(unittest.TestCase):
    def test_detecta_recuentos_distintos(self):
        tex = "Hay nueve plataformas actuales.\nLa tabla identifica ocho sistemas existentes.\n"
        self.assertEqual(len(v.plataformas_inconsistentes(tex)), 1)

    def test_acepta_un_solo_recuento(self):
        self.assertEqual(v.plataformas_inconsistentes("Son nueve plataformas.\nLas nueve plataformas cambian.\n"), [])


class NombresAntiguosTest(unittest.TestCase):
    def test_detecta_nombre_y_codigo(self):
        out = v.nombres_antiguos("La plataforma común conecta.\nEl servicio R-03 y F-01.\n% R-02 comentado\n")
        self.assertEqual(len(out), 2)


class ReferenciasTest(unittest.TestCase):
    TEX = (
        "Rige la Ley N.º 19.628 y la Circular N.º 1 de la CMF.\n"
        "\\section*{Referencias}\nLey 19.628 sobre datos.\n"
        "\\section*{Declaración de uso de IA}\nTexto.\n"
    )

    def test_detecta_norma_ausente(self):
        out = v.normas_sin_referencia(self.TEX)
        self.assertEqual(len(out), 1)
        self.assertIn("Circular", out[0])


class DeclaracionIATest(unittest.TestCase):
    def cuerpo(self, n):
        return " ".join(["palabra"] * n)

    def test_detecta_seccion_no_mencionada(self):
        tex = (
            f"\\section{{3.1 Uno}}\n{self.cuerpo(60)}\n"
            f"\\section{{3.3 Tres}}\n{self.cuerpo(60)}\n"
            "\\section*{Declaración de uso de IA}\nLa sección 3.1 se redactó con asistencia.\n\\end{document}"
        )
        out = v.declaracion_ia_incompleta(tex)
        self.assertEqual(len(out), 1)
        self.assertIn("3.3", out[0])

    def test_ignora_secciones_vacias(self):
        tex = (
            "\\section{3.3 Tres}\n% solo un comentario\n"
            "\\section*{Declaración de uso de IA}\nTexto.\n\\end{document}"
        )
        self.assertEqual(v.declaracion_ia_incompleta(tex), [])


class ConteosTest(unittest.TestCase):
    def test_lee_totales_y_compara(self):
        anexo = "| **Total** | **227** | **72** | **9** |\n"
        with tempfile.TemporaryDirectory() as tmp:
            ruta = Path(tmp) / "b.md"
            ruta.write_text(anexo, encoding="utf-8")
            totales = v.totales_anexo_b(ruta)
        self.assertEqual(totales, {"rf": 227, "rnf": 72, "op": 9, "total": 308})
        self.assertEqual(v.conteos_distintos("308 elementos, 227, 72 y 9", totales), [])
        self.assertEqual(len(v.conteos_distintos("307 elementos, 227, 72 y 9", totales)), 1)


if __name__ == "__main__":
    unittest.main()
