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

    def test_la_plantilla_trae_las_153_cuentas(self):
        f, e = cm.leer_planilla(DIR / "12_plantilla_tres_valores.md")
        self.assertEqual(len(f), 153)
        self.assertEqual(len([c for c in f if c.startswith("1.5.")]), 51)
        self.assertEqual(e, [])
        self.assertTrue(all(v is None for v in f.values()))

    def test_la_plantilla_publicada_esta_actualizada(self):
        import generar_mapa_paquetes as gm
        import generar_plantilla_tres_valores as gp
        paquetes, _ = gm.cargar()
        self.assertEqual(gp.texto(paquetes), (DIR / "12_plantilla_tres_valores.md").read_text(encoding="utf-8"))

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

    # ---- planillas por paquete
    def llenar(self, d, nombre, factor, omitir=()):
        ucp_pk, _, paquetes = cm.horas_ucp_por_paquete()
        filas = []
        for p in paquetes:
            if p["codigo"] in omitir:
                continue
            h = ucp_pk.get(p["codigo"], 100.0) * factor
            filas.append(f"| {p['codigo']} | x | y | z | {int(h * 0.8)} | {int(h)} | {int(h * 1.4)} |\n")
        ruta = Path(d) / nombre
        ruta.write_text("| Código | Paquete | Servicio | Unidad | O | P | Pe |\n| :-- | :-- | :-- | :-- | --: | --: | --: |\n" + "".join(filas), encoding="utf-8")
        return ruta

    def test_paquetes_dentro_de_la_tolerancia(self):
        with tempfile.TemporaryDirectory() as d:
            r = cm.comparar([self.llenar(d, "a.md", 1.0)])
        self.assertEqual(r["modo"], "paquetes")
        self.assertTrue(r["dentro"])
        self.assertEqual(r["faltan"], [])
        self.assertEqual(sum(d["n"] for d in r["ramas"].values()), 102)

    def test_paquetes_fuera_de_la_tolerancia_y_codigo_de_salida(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = self.llenar(d, "a.md", 2.0)
            self.assertEqual(cm.main([str(ruta)]), 1)

    def test_paquetes_incompletos_no_comparan_el_total(self):
        with tempfile.TemporaryDirectory() as d:
            ruta = self.llenar(d, "a.md", 1.0, omitir=("1.5.1.1",))
            r = cm.comparar([ruta])
            self.assertNotIn("total_segundo", r)
            self.assertIn("1.5.1.1", r["faltan"])
            self.assertFalse(r["por_servicio"]["Servicio de oferta comercial"]["completo"])
            self.assertEqual(cm.main([str(ruta)]), 2)

    def test_las_horas_por_paquete_suman_el_total_del_ucp(self):
        ucp_pk, total, _ = cm.horas_ucp_por_paquete()
        self.assertAlmostEqual(sum(ucp_pk.values()), total, places=6)


if __name__ == "__main__":
    unittest.main()
