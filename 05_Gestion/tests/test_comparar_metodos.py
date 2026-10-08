"""Pruebas del segundo método: media de tres valores, tolerancia y planillas incompletas."""

import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import comparar_metodos as cm  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"
SERVICIOS = ["EX", "OF", "VE", "OR", "EV", "CC", "CA", "BT", "AB", "PE", "CM", "MK", "PV", "CL"]
CAB = "| Código | Alcance | Unidad | Optimista (h) | Probable (h) | Pesimista (h) |\n| :-- | :-- | :-- | --: | --: | --: |\n"


def escribir(d, nombre, filas):
    p = Path(d) / nombre
    p.write_text(CAB + "".join(f"| {c} | x | y | {o} | {pr} | {pe} |\n" for c, o, pr, pe in filas), encoding="utf-8")
    return p


def planilla_proporcional(d, nombre, factor):
    _, ucp = cm.horas_ucp()
    filas = [(c, int(v * factor * 0.8), int(v * factor), int(v * factor * 1.4)) for c, v in ucp.items()]
    return escribir(d, nombre, filas)


class TestCompararMetodos(unittest.TestCase):
    def test_media_pert(self):
        self.assertAlmostEqual(cm.media_pert((100, 200, 400)), 1300 / 6)
        self.assertAlmostEqual(cm.desviacion((100, 200, 400)), 50.0)

    def test_planilla_vacia_no_compara(self):
        with tempfile.TemporaryDirectory() as d:
            r = cm.comparar([DIR / "12_plantilla_tres_valores.md"])
            self.assertNotIn("total_segundo", r)
            self.assertEqual(cm.main([str(DIR / "12_plantilla_tres_valores.md")]), 2)

    def test_la_plantilla_trae_los_14_servicios_y_las_9_ramas(self):
        f, e = cm.leer_planilla(DIR / "12_plantilla_tres_valores.md")
        self.assertEqual(sorted(c for c in f if c.startswith("S-")), sorted("S-" + s for s in SERVICIOS))
        self.assertEqual(len([c for c in f if c.startswith("R-")]), 9)
        self.assertEqual(e, [])

    def test_dentro_de_la_tolerancia(self):
        with tempfile.TemporaryDirectory() as d:
            p = planilla_proporcional(d, "a.md", 1.0)
            r = cm.comparar([p])
        self.assertTrue(r["dentro"])
        self.assertLess(abs(r["diferencia"]), 0.25)

    def test_fuera_de_la_tolerancia(self):
        with tempfile.TemporaryDirectory() as d:
            p = planilla_proporcional(d, "a.md", 2.0)
            r = cm.comparar([p])
            self.assertFalse(r["dentro"])
            self.assertEqual(cm.main([str(p)]), 1)

    def test_orden_invalido_y_valores_faltantes(self):
        with tempfile.TemporaryDirectory() as d:
            p = escribir(d, "a.md", [("S-EX", 500, 100, 900), ("S-OF", 100, 200, "")])
            f, e = cm.leer_planilla(p)
        self.assertEqual(len(e), 2)

    def test_dos_estimadores_se_promedian_y_miden_dispersion(self):
        with tempfile.TemporaryDirectory() as d:
            a = escribir(d, "a.md", [("S-EX", 90, 100, 130)])
            b = escribir(d, "b.md", [("S-EX", 180, 200, 260)])
            r = cm.comparar([a, b])
        fila = r["servicios"]["S-EX"]
        self.assertEqual(fila["n"], 2)
        self.assertGreater(fila["dispersion"], 0.5)


if __name__ == "__main__":
    unittest.main()
