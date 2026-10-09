"""Pruebas de la primera ola de paquetes de trabajo."""

import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import generar_cronograma as gc  # noqa: E402
import generar_ola as go  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"
CAB = "| Código | Paquete | Mes | Unidad | O | P | Pe |\n| :-- | :-- | :-- | :-- | --: | --: | --: |\n"


class TestOla(unittest.TestCase):
    def test_grupos_y_cantidades(self):
        paquetes, cuentas, _ = go.construir()
        self.assertEqual(len(cuentas), 76)
        por = {g: len([x for x in paquetes if x["grupo"] == g]) for g in "ABCD"}
        self.assertEqual(por, {"A": 84, "B": 21, "C": 25, "D": 38})
        self.assertEqual(len({x["codigo"] for x in paquetes}), len(paquetes))

    def test_todo_paquete_de_la_ola_cae_en_un_solo_mes_dentro_de_la_ola(self):
        paquetes, _, _ = go.construir()
        self.assertTrue(all(go.OLA[0] <= x["mes"] <= go.OLA[1] for x in paquetes))

    def test_los_paquetes_de_software_cumplen_8_80(self):
        paquetes, _, _ = go.construir()
        a = [x for x in paquetes if x["grupo"] == "A"]
        self.assertTrue(all(go.MIN_H <= x["horas"] <= go.MAX_H for x in a))
        self.assertEqual([x for x in paquetes if go.incumple(x)], [])

    def test_las_horas_del_analisis_son_el_10_por_ciento_de_los_casos(self):
        paquetes, _, casos = go.construir()
        ids = {x["nombre"].rsplit("(", 1)[1].rstrip(")") for x in paquetes if x["grupo"] == "A"}
        self.assertEqual(sum(x["horas"] for x in paquetes if x["grupo"] == "A"), sum(casos[i]["horas"] for i in ids) * 0.10)

    def test_el_trabajo_continuo_tiene_un_paquete_por_mes(self):
        paquetes, _, _ = go.construir()
        b = [x for x in paquetes if x["cuenta"] == "1.1.3"]
        self.assertEqual([x["mes"] for x in b], [1, 2, 3])
        self.assertIn("ene 2027", b[0]["nombre"])

    def test_el_plan_de_direccion_se_separa_en_ocho_planes(self):
        paquetes, _, _ = go.construir()
        self.assertEqual(len([x for x in paquetes if x["cuenta"] == "1.1.1"]), 8)

    def test_horas_sin_fuente_quedan_por_estimar_y_las_de_planilla_se_verifican(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "a.md"
            p.write_text(CAB + "| 1.1.12.1 | x | 1 | 1 mes | 10 | 20 | 30 |\n| 1.1.3.1 | x | 1 | 1 mes | 100 | 200 | 300 |\n", encoding="utf-8")
            paquetes, _, _ = go.construir([p])
        acta = next(x for x in paquetes if x["codigo"] == "1.1.12.1")
        cambios = next(x for x in paquetes if x["codigo"] == "1.1.3.1")
        self.assertAlmostEqual(acta["horas"], 20.0)
        self.assertFalse(go.incumple(acta))
        self.assertTrue(go.incumple(cambios))
        self.assertTrue(any(x["fuente"] == "por estimar" for x in paquetes))

    def test_el_paquete_de_software_es_el_caso_de_uso_y_el_analisis_es_una_actividad(self):
        paquetes, _, casos = go.construir()
        sw = go.paquetes_software(casos)
        self.assertEqual(len(sw), 127)
        self.assertAlmostEqual(sum(x["horas"] for x in sw), 31850.0, delta=1.0)
        self.assertTrue(all(x["horas"] > go.MAX_H for x in sw))  # excepción declarada a 8/80
        a = [x for x in paquetes if x["grupo"] == "A"]
        self.assertTrue(all(x["codigo"].endswith("-A") and x["nombre"].startswith("Análisis del caso de uso") for x in a))

    def test_proyeccion_cubre_los_127_casos(self):
        _, _, casos = go.construir()
        pr = go.proyeccion(casos)
        self.assertEqual(pr[0][1], 127)
        self.assertTrue(all(mayor <= go.MAX_H for _, _, mayor in pr))

    def test_la_ola_coincide_con_la_curva_del_cronograma(self):
        paquetes, _, _ = go.construir()
        paq, _ = gm.cargar()
        por_mes, _ = gc.curva(gc.asignar(paq))
        curva = sum(v["1"] + v["1 y 2"] for m, v in por_mes.items() if 1 <= m <= 3)
        self.assertAlmostEqual(sum(x["horas"] for x in paquetes if x["grupo"] == "A"), curva, delta=2)

    def test_los_documentos_publicados_estan_actualizados(self):
        paquetes, cuentas, casos = go.construir()
        self.assertEqual(go.texto(paquetes, cuentas, casos), (DIR / "21_ola_1_paquetes_trabajo.md").read_text(encoding="utf-8"))
        self.assertEqual(go.plantilla(paquetes), (DIR / "21_planilla_ola_1.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
