"""Pruebas del reparto de horas por paquete (paso 9)."""

import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import repartir_horas_paquetes as rh  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"


class TestHorasPaquetes(unittest.TestCase):
    def test_las_horas_del_ucp_suman_el_total(self):
        filas, total = rh.calcular()
        self.assertAlmostEqual(sum(f["horas"] for f in filas if f["fuente"] == "UCP"), total, places=6)
        self.assertEqual(rh.verificar(filas, total), [])
        self.assertAlmostEqual(total, 31850.0, delta=1.0)

    def test_lo_que_no_cubre_el_ucp_queda_por_estimar(self):
        filas, _ = rh.calcular()
        pend = [f for f in filas if f["fuente"] == "por estimar"]
        self.assertEqual(len(pend), 113)
        self.assertTrue(all(f["horas"] is None for f in pend))

    def test_las_horas_de_una_planilla_entran_a_su_paquete(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = Path(d) / "a.md"
            ruta.write_text("| Código | Paquete | Etapa | Unidad | O | P | Pe |\n| :-- | :-- | :-- | :-- | --: | --: | --: |\n"
                            "| 1.1.1 | x | y | z | 100 | 200 | 400 |\n", encoding="utf-8")
            filas, total = rh.calcular([ruta])
        f = next(x for x in filas if x["codigo"] == "1.1.1")
        self.assertEqual(f["fuente"], "tres valores")
        self.assertAlmostEqual(f["horas"], 1300 / 6)

    def test_hay_un_paquete_de_software_por_caso_de_uso_y_suman_el_total(self):
        filas, total = rh.calcular()
        sw = rh.paquetes_software(filas)
        self.assertEqual(len(sw), 127)
        self.assertEqual(len({x["codigo"] for x in sw}), 127)
        self.assertAlmostEqual(sum(x["horas"] for x in sw), total, places=6)
        self.assertEqual(sum(x["trans"] for x in sw), 296)

    def test_el_informe_publicado_esta_actualizado(self):
        filas, total = rh.calcular()
        self.assertEqual(rh.informe(filas, total), (DIR / "16_horas_por_paquete.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
