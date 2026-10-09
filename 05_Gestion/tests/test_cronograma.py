"""Pruebas del cronograma: anclas del contrato, congelamientos y curva de horas."""

import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import generar_cronograma as gc  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"


def cargar():
    paquetes, _ = gm.cargar()
    items = gc.asignar(paquetes)
    por_mes, total = gc.curva(items)
    return items, por_mes, total


class TestCronograma(unittest.TestCase):
    def test_calendario(self):
        self.assertEqual(gc.calendario(1), "ene 2027")
        self.assertEqual(gc.calendario(16), "abr 2028")
        self.assertEqual(gc.calendario(21), "sep 2028")
        self.assertEqual(gc.calendario(22), "oct 2028")
        self.assertEqual(gc.calendario(56), "ago 2031")

    def test_pasos_a_produccion_fuera_de_congelamientos(self):
        self.assertNotIn(gc.mes_calendario(16), gc.CONGELADOS)
        self.assertNotIn(gc.mes_calendario(21), gc.CONGELADOS)

    def test_el_cronograma_pasa_las_comprobaciones(self):
        items, por_mes, total = cargar()
        self.assertEqual(gc.verificar(items, por_mes, total), [])

    def test_todos_los_paquetes_tienen_ventana_salvo_innovaciones(self):
        items, _, _ = cargar()
        sin = [p["codigo"] for p in items if p["ventana"] is None]
        self.assertEqual(sorted(sin), [f"1.10.{i}" for i in range(1, 6)])

    def test_la_curva_suma_el_total_del_ucp_y_respeta_las_etapas(self):
        _, por_mes, total = cargar()
        self.assertAlmostEqual(sum(sum(v.values()) for v in por_mes.values()), total, places=6)
        self.assertAlmostEqual(sum(v["1"] for m, v in por_mes.items() if 1 <= m <= 12), sum(v["1"] for v in por_mes.values()), places=6)
        self.assertEqual(sum(sum(v.values()) for m, v in por_mes.items() if m > 18), 0)

    def test_anclas_del_contrato(self):
        items, _, _ = cargar()
        v = {p["codigo"]: p["ventana"] for p in items}
        self.assertEqual(v["1.12.4"][:2], (16, 16))
        self.assertEqual(v["1.12.7"][:2], (21, 21))
        self.assertEqual(v["1.7.11"][:2], (22, 22))
        self.assertEqual(v["1.9.8"][:2], (12, 12))
        self.assertEqual(v["1.9.9"][:2], (18, 18))
        self.assertTrue(all(p["ventana"][0] >= 21 for p in items if p["rama"] == "1.15"))

    def test_la_ventana_de_una_cuenta_fusionada_es_la_union(self):
        items, _, _ = cargar()
        v = {p["codigo"]: p["ventana"] for p in items}
        self.assertEqual(v["1.6.2"][:2], (5, 18))
        self.assertEqual(v["1.12.2"][:2], (15, 16))
        self.assertNotIn("1.6.4", v)

    def test_detecta_software_fuera_de_su_etapa(self):
        items, por_mes, total = cargar()
        malo = dict(next(p for p in items if p["metodo"] == "UCP" and p["etapa"] == "1"))
        malo["ventana"] = (13, 18, "propuesta", "x")
        h = gc.verificar([malo], por_mes, total)
        self.assertTrue(any("debe caer en los meses" in x for x in h))

    def test_el_cronograma_publicado_esta_actualizado(self):
        items, por_mes, total = cargar()
        self.assertEqual(gc.texto(items, por_mes, total), (DIR / "17_cronograma_edt.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
