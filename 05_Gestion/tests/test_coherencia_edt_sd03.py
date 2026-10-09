"""Pruebas de la coherencia de la EDT con el sd-03."""

import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import generar_cronograma as gc  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402
import verificar_coherencia_edt_sd03 as vc  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"


class TestCoherenciaEdtSd03(unittest.TestCase):
    def test_tabla_31_y_34_se_leen_del_sd03(self):
        t31 = vc.tabla_31()
        self.assertEqual(t31["Servicio de cartera de crédito"], "1 y 2")
        self.assertEqual(t31["Servicio de pedidos"], "2")
        self.assertIn("Punto de venta con operación sin conexión", t31)
        self.assertEqual(vc.tabla_34()["Etapa 1"][0], 142)

    def test_las_comprobaciones_mecanicas_pasan_en_la_edt_corregida(self):
        res = vc.comprobar()
        malas = [m for m in res["mecanicas"] if not m[1]]
        self.assertEqual(malas, [])
        self.assertEqual(len(res["mecanicas"]), 7)

    def test_hay_16_compromisos_y_los_implicitos_estan_cubiertos(self):
        res = vc.comprobar()
        self.assertEqual(len(res["compromisos"]), 16)
        por_id = {c["id"]: c for c in res["compromisos"]}
        for k in ("K13", "K14", "K15", "K16"):
            self.assertTrue(por_id[k]["ok"], k)

    def test_la_edt_corregida_cubre_los_16_compromisos_del_sd03(self):
        res = vc.comprobar()
        self.assertEqual([c["id"] for c in res["compromisos"] if not c["ok"]], [])
        self.assertEqual(vc.hallazgos(res), [])

    def test_un_compromiso_con_ventana_incoherente_se_detecta(self):
        with tempfile.TemporaryDirectory() as d:
            edt = Path(d) / "edt.md"
            texto = (gm.EDT.read_text(encoding="utf-8").replace("1.9.4 Pruebas de desempeño, resiliencia y recuperación ante desastres",
                                                                  "1.9.4 Piloto del punto de venta en tres tiendas"))
            edt.write_text(texto, encoding="utf-8")
            res = vc.comprobar(edt)
        k3 = next(c for c in res["compromisos"] if c["id"] == "K3")
        self.assertFalse(k3["ok"])
        self.assertIn("1.9.4", k3["cuentas"])
        self.assertIn("ventana", k3["nota"])

    def test_un_compromiso_cubierto_con_su_ventana_pasa(self):
        original, fus = gc.V.get("1.9.4"), gc.FUSIONES.get("1.9.4")
        try:
            gc.V["1.9.4"] = (6, 7, "contrato", "prueba")
            gc.FUSIONES["1.9.4"] = []
            with tempfile.TemporaryDirectory() as d:
                edt = Path(d) / "edt.md"
                edt.write_text(gm.EDT.read_text(encoding="utf-8").replace("1.9.4 Pruebas de desempeño, resiliencia y recuperación ante desastres",
                                                                           "1.9.4 Piloto del punto de venta en tres tiendas"), encoding="utf-8")
                res = vc.comprobar(edt)
        finally:
            gc.V["1.9.4"] = original
            gc.FUSIONES["1.9.4"] = fus
        self.assertTrue(next(c for c in res["compromisos"] if c["id"] == "K3")["ok"])

    def test_el_informe_publicado_esta_actualizado(self):
        self.assertEqual(vc.texto(vc.comprobar()), (DIR / "22_coherencia_edt_sd03.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
