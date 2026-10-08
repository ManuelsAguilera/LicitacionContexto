"""Guarda el TCF documentado en `08_tcf.md`: tabla coherente con la calculadora y con las pruebas de la puerta G5."""

import re
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import estimacion_ucp as calc  # noqa: E402

ARCHIVO = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion" / "08_tcf.md"


def valores():
    out = []
    for linea in ARCHIVO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*T(\d+) [^|]*\|\s*([\d,]+)\s*\|\s*(\d)\s*\|", linea)
        if m:
            out.append((int(m.group(1)), float(m.group(2).replace(",", ".")), int(m.group(3))))
    return out


class TestTCF(unittest.TestCase):
    def test_trece_factores_con_los_pesos_de_la_clase(self):
        v = valores()
        self.assertEqual([t for t, _, _ in v], list(range(1, 14)))
        self.assertEqual([p for _, p, _ in v], calc.PESOS_TCF)

    def test_pruebas_de_la_puerta(self):
        vals = [x for _, _, x in valores()]
        self.assertTrue(all(0 <= x <= 5 for x in vals))
        self.assertFalse(all(x == 3 for x in vals))
        self.assertFalse(all(x == 5 for x in vals))
        self.assertNotIn(0, vals)
        self.assertTrue(0.60 <= calc.tcf(vals) <= 1.30)

    def test_tcf_documentado(self):
        self.assertAlmostEqual(calc.tcf([x for _, _, x in valores()]), 1.19, places=6)


if __name__ == "__main__":
    unittest.main()
