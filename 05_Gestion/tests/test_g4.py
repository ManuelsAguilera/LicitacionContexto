"""Pruebas del paso 4: generador de la entrada y segunda vía independiente de UAW, UUCW y UUCP."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import generar_entrada_ucp as g  # noqa: E402
import recalcular_uucp as r  # noqa: E402

CASOS = """| Código | Servicio | Caso de uso | Actor principal | Trans. | Origen | Supuestos |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-EX-01 | R:M-03 | A | AH-03 | 2 | RF-001 | S1 |
| CU-EX-02 | R:M-03 | B | AH-03 | 4 | RF-002 | S1 |
| CU-PE-01 | R:V-01 | C | AS-14 | 3 | RF-003 | S1 |

| Código | Transacciones |
| :-- | :-- |
| CU-EX-01 | T1 a. T2 b |
| CU-EX-02 | T1 a. T2 b. T3 c. T4 d |
| CU-PE-01 | T1 a. T2 b. T3 c |
"""
ACTORES = "| AH-03 | Vendedor | 3 | x |\n| AS-14 | Temporizador | 1 | x |\n| AS-09 | Antiguo | 2 | x |\n"


def preparar(d):
    d = Path(d)
    (d / "03_casos_de_uso_x.md").write_text(CASOS, encoding="utf-8")
    (d / "act.md").write_text(ACTORES, encoding="utf-8")
    return d


class TestG4(unittest.TestCase):
    def test_generador_y_calculo(self):
        with tempfile.TemporaryDirectory() as t:
            d = preparar(t)
            e = g.generar(d, d / "act.md")
        self.assertEqual(e["resultado"], {"UAW": 6, "UUCW": 20, "UUCP": 26})
        self.assertEqual([c["etapa"] for c in e["casos_detalle"]], [1, 1, 2])

    def test_segunda_via_coincide(self):
        with tempfile.TemporaryDirectory() as t:
            d = preparar(t)
            e = g.generar(d, d / "act.md")
            (d / "e.json").write_text(json.dumps(e), encoding="utf-8")
            por_caso, tipos = r.leer(d, d / "act.md")
            res = r.calcular(por_caso, tipos)
            self.assertEqual({k: res[k] for k in ("UAW", "UUCW", "UUCP")}, e["resultado"])
            self.assertEqual(res["reparto"], {"simple": 2, "medio": 1, "complejo": 0})
            self.assertEqual(r.main(["--json", str(d / "e.json"), "--dir", str(d), "--actores", str(d / "act.md")]), 0)

    def test_detecta_diferencia(self):
        with tempfile.TemporaryDirectory() as t:
            d = preparar(t)
            e = g.generar(d, d / "act.md")
            e["resultado"]["UUCW"] += 5
            (d / "e.json").write_text(json.dumps(e), encoding="utf-8")
            self.assertEqual(r.main(["--json", str(d / "e.json"), "--dir", str(d), "--actores", str(d / "act.md")]), 1)

    def test_la_segunda_via_cuenta_el_detalle_y_no_la_columna(self):
        with tempfile.TemporaryDirectory() as t:
            d = preparar(t)
            (d / "03_casos_de_uso_x.md").write_text(CASOS.replace("| B | AH-03 | 4 |", "| B | AH-03 | 2 |"), encoding="utf-8")
            por_caso, _ = r.leer(d, d / "act.md")
        self.assertEqual(por_caso["CU-EX-02"], 4)


if __name__ == "__main__":
    unittest.main()
