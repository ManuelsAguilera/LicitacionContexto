"""Pruebas del mapa de paquetes: cada caso de uso en un solo paquete y coherencia con la EDT corregida."""

import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import generar_mapa_paquetes as gm  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"


def con_edt(texto):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "edt.md"
        p.write_text(texto, encoding="utf-8")
        return gm.cargar(p)


class TestMapaPaquetes(unittest.TestCase):
    def test_la_edt_corregida_cubre_todo_el_modelo(self):
        paquetes, h = gm.cargar()
        self.assertEqual(h, [])
        ucp = [p for p in paquetes if p["metodo"] == "UCP"]
        self.assertEqual(sum(len(p["casos"]) for p in ucp), 127)
        self.assertEqual(sum(p["uucw"] for p in ucp), 645)
        self.assertEqual(len(paquetes), 164)

    def test_el_mapa_publicado_esta_actualizado(self):
        paquetes, _ = gm.cargar()
        self.assertEqual(gm.informe(paquetes), (DIR / "15_mapa_paquetes_ucp.md").read_text(encoding="utf-8"))

    def test_caso_repetido_y_caso_inexistente(self):
        texto = ("### 1.5 Desarrollo — 3 paquetes\n\n#### 1.5.1 Servicio de existencias — 3 paquetes\n\n"
                 "- 1.5.1.1 Primer plan {casos: CU-EX-01, CU-EX-02; etapa: 1}\n"
                 "- 1.5.1.2 Segundo plan {casos: CU-EX-02, CU-EX-99; etapa: 1}\n- 1.5.1.3 Tercer plan {casos: CU-EX-03; etapa: 1}\n")
        _, h = con_edt(texto)
        self.assertTrue(any("CU-EX-02" in x and "y en" in x for x in h))
        self.assertTrue(any("CU-EX-99" in x for x in h))

    def test_servicio_y_etapa_incoherentes(self):
        texto = ("### 1.5 Desarrollo — 3 paquetes\n\n#### 1.5.1 Servicio de pedidos — 3 paquetes\n\n"
                 "- 1.5.1.1 Primer plan {casos: CU-EX-01; etapa: 2}\n- 1.5.1.2 Segundo plan {casos: CU-EX-02; etapa: 1}\n"
                 "- 1.5.1.3 Tercer plan {casos: CU-PE-01; etapa: 2}\n")
        _, h = con_edt(texto)
        self.assertTrue(any("mezcla" in x or "pero sus casos son" in x for x in h))
        self.assertTrue(any("no coincide con la del servicio" in x for x in h))

    def test_rango_de_rf(self):
        self.assertEqual(gm.rango_rf({"RF-001", "RF-002", "RF-003", "RF-009"}), "RF-001 a RF-003, RF-009")
        self.assertEqual(gm.rango_rf({"RF-001", "RF-002"}), "RF-001, RF-002")


if __name__ == "__main__":
    unittest.main()
