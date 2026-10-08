"""Guarda los factores de ambiente documentados en `09_ef_preguntas.md` frente a las pruebas de la puerta G5."""

import re
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import estimacion_ucp as calc  # noqa: E402

ARCHIVO = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion" / "09_ef_preguntas.md"


def filas():
    out = []
    for linea in ARCHIVO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*E(\d) [^|]*\|\s*(−?[\d,]+)\s*\|\s*(\d)\s*\|\s*([^|]+)\|", linea)
        if m:
            out.append((int(m.group(1)), float(m.group(2).replace(",", ".").replace("−", "-")), int(m.group(3)), m.group(4).strip()))
    return out


class TestEF(unittest.TestCase):
    def test_ocho_factores_con_los_pesos_de_la_clase(self):
        f = filas()
        self.assertEqual([e for e, _, _, _ in f], list(range(1, 9)))
        self.assertEqual([p for _, p, _, _ in f], calc.PESOS_EF)

    def test_pruebas_de_la_puerta(self):
        v = [x for _, _, x, _ in filas()]
        self.assertTrue(all(0 <= x <= 5 for x in v))
        self.assertFalse(all(x == 3 for x in v))
        self.assertFalse(all(x == 5 for x in v))
        self.assertTrue(0.42 <= calc.ef(v) <= 1.70)

    def test_cada_extremo_tiene_justificacion(self):
        for e, _, x, just in filas():
            if x in (0, 5):
                self.assertGreater(len(just), 30, f"E{e} vale {x} y necesita justificación")

    def test_ef_y_factor_de_conversion_documentados(self):
        v = [x for _, _, x, _ in filas()]
        self.assertAlmostEqual(calc.ef(v), 0.785, places=6)
        self.assertEqual(calc.factores_desfavorables(v), 1)
        self.assertEqual(calc.factor_conversion(v), 20)


if __name__ == "__main__":
    unittest.main()
