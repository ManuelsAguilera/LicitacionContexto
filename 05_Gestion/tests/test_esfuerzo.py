"""Pruebas del esfuerzo provisional (paso 6): las dos vías coinciden y las cifras de referencia no se mueven sin aviso."""

import json
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import calcular_esfuerzo as ce  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"


class TestEsfuerzo(unittest.TestCase):
    def setUp(self):
        self.entrada = json.loads((DIR / "07_entrada_calculadora.json").read_text(encoding="utf-8"))
        self.tcf = ce.leer_tcf()

    def test_las_dos_vias_coinciden(self):
        _, fallas = ce.construir(self.entrada, self.tcf)
        self.assertEqual(fallas, [])

    def test_escenario_neutro(self):
        r = ce.via2(self.entrada["actores"], self.entrada["casos"], self.tcf, [3] * 8)
        self.assertAlmostEqual(r["EF"], 0.995, places=6)
        self.assertEqual(r["CF"], 20)
        self.assertAlmostEqual(r["total"], 41975.0, delta=1.0)

    def test_valores_informados_del_equipo(self):
        for e3, ef in ((3, 0.785), (4, 0.755), (5, 0.725)):
            r = ce.via2(self.entrada["actores"], self.entrada["casos"], self.tcf, [5, 4, e3, 4, 5, 2, 0, 3])
            self.assertAlmostEqual(r["EF"], ef, places=6)
            self.assertEqual((r["mal"], r["CF"]), (1, 20))

    def test_cinco_desfavorables_no_estiman(self):
        r = ce.via2(self.entrada["actores"], self.entrada["casos"], self.tcf, [0] * 6 + [5, 5])
        self.assertIsNone(r["CF"])
        self.assertNotIn("total", r)

    def test_el_informe_esta_actualizado(self):
        texto, _ = ce.construir(self.entrada, self.tcf)
        self.assertEqual(texto, (DIR / "10_esfuerzo.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
