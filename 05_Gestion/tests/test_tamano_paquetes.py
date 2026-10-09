"""Pruebas de la evaluación de tamaño (reglas 8/80 y del período de reporte)."""

import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import evaluar_tamano_paquetes as et  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"


class TestTamanoPaquetes(unittest.TestCase):
    def test_numeros_del_diagnostico(self):
        _, total = et.medir()
        n = et.numeros_base(total)
        self.assertAlmostEqual(n["simple"], 31850 * 5 / 645, delta=1)
        self.assertAlmostEqual(n["por_transaccion"], 31850 / 296, delta=1)
        self.assertGreater(n["simple"], et.MAX_H)
        self.assertGreater(n["por_transaccion"], et.MAX_H)

    def test_ningun_elemento_de_software_cabe_en_80_horas(self):
        items, _ = et.medir()
        sw = [x for x in items if x["fuente"] == "UCP"]
        self.assertTrue(sw)
        self.assertTrue(all(x["mas_80"] for x in sw))

    def test_las_reglas_se_exigen_solo_a_paquetes_de_trabajo(self):
        base = {"mas_80": True, "menos_8": False, "excede_periodo": True, "sin_horas": False}
        cuenta = dict(base, nivel="cuenta de control", codigo="1.1.1")
        trabajo = dict(base, nivel=et.TRABAJO, codigo="1.1.1.1")
        bueno = dict(nivel=et.TRABAJO, codigo="1.1.1.2", mas_80=False, menos_8=False, excede_periodo=False, sin_horas=False)
        self.assertEqual([x["codigo"] for x in et.incumplen([cuenta, trabajo, bueno])], ["1.1.1.1"])

    def test_el_informe_publicado_esta_actualizado(self):
        items, total = et.medir()
        self.assertEqual(et.texto(items, total), (DIR / "20_evaluacion_8_80.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
