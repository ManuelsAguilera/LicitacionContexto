"""Pruebas del tablero del loop de la EDT."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import ciclo_edt as ce  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402

PROMPT = RAIZ / "80_Artefactos" / "sd-07_contexto" / "prompt_loop_edt.md"
BITACORA = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion" / "23_bitacora_loop_edt.md"


def con_edt(cambio):
    d = tempfile.mkdtemp()
    p = Path(d) / "edt.md"
    p.write_text(cambio(gm.EDT.read_text(encoding="utf-8")), encoding="utf-8")
    return p


class TestCicloEdt(unittest.TestCase):
    def test_el_tablero_trae_las_nueve_metas_duras_y_las_blandas(self):
        t = ce.tablero()
        self.assertEqual(list(t["duras"]), [f"H{i}" for i in range(1, 10)])
        self.assertEqual(sorted(t["blandas"]), ["S1", "S2", "S3"])
        json.dumps(t)  # serializable

    def test_s1_cuenta_127_paquetes_de_software_y_689_actividades(self):
        s1 = ce.tablero()["blandas"]["S1"]
        self.assertEqual(s1["paquetes_software"], 127)
        self.assertEqual(s1["actividades_software_proyectadas"], 689)

    def test_las_metas_de_coherencia_y_de_tamano_pasan_hoy(self):
        d = ce.tablero()["duras"]
        for k in ("H1", "H2", "H3", "H4", "H5", "H7", "H8", "H9"):
            self.assertTrue(d[k]["ok"], f"{k}: {d[k]['detalle']}")

    def test_la_traza_directa_es_la_tarea_pendiente_del_loop(self):
        h6 = ce.tablero()["duras"]["H6"]
        self.assertEqual(h6["ok"], not h6["infractores"])

    def test_quitar_la_cuenta_de_un_compromiso_rompe_h2_y_el_codigo_de_salida(self):
        p = con_edt(lambda s: "\n".join(x for x in s.split("\n") if not x.startswith("- 1.13.5 ")))
        t = ce.tablero(p)
        self.assertFalse(t["duras"]["H2"]["ok"])
        self.assertIn("K8", t["duras"]["H2"]["infractores"])
        self.assertFalse(t["ok"])

    def test_agregar_la_traza_baja_los_infractores_de_h6(self):
        antes = ce.tablero()["duras"]["H6"]["infractores"]
        if not antes:
            self.skipTest("todas las cuentas ya tienen traza")
        cod = antes[0]
        p = con_edt(lambda s: s.replace(f"- {cod} ", f"- {cod} ", 1))
        # agrega un origen a la cuenta indicada
        texto = p.read_text(encoding="utf-8").split("\n")
        for i, linea in enumerate(texto):
            if linea.startswith(f"- {cod} "):
                texto[i] = linea.replace("etapa:", "origen: sd-03, 3.2.2; etapa:", 1) if "origen:" not in linea else linea
        p.write_text("\n".join(texto), encoding="utf-8")
        despues = ce.tablero(p)["duras"]["H6"]["infractores"]
        self.assertNotIn(cod, despues)
        self.assertEqual(len(despues), len(antes) - 1)

    def test_el_prompt_y_la_bitacora_existen_y_citan_el_tablero(self):
        self.assertTrue(PROMPT.exists())
        self.assertIn("ciclo_edt.py", PROMPT.read_text(encoding="utf-8"))
        self.assertTrue(BITACORA.exists())


if __name__ == "__main__":
    unittest.main()
