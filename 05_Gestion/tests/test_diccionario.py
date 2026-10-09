"""Pruebas de la estructura del diccionario de la EDT."""

import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import generar_diccionario as gd  # noqa: E402

DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"


def manual(filas):
    d = tempfile.mkdtemp()
    p = Path(d) / "m.md"
    p.write_text(gd.PLANTILLA_MANUAL + "".join(f"| {c} | {k} | {v} | prueba |\n" for c, k, v in filas), encoding="utf-8")
    return p


class TestDiccionario(unittest.TestCase):
    def test_una_ficha_por_paquete_con_todos_los_campos(self):
        fichas, hall = gd.construir()
        self.assertEqual(hall, [])
        self.assertEqual(len(fichas), 164)
        for f in fichas:
            self.assertEqual(set(f["vals"]), gd.CLAVES, f["paquete"]["codigo"])
            self.assertTrue(all(e in ("derivado", "propuesta", "manual", "por definir") for _, e in f["vals"].values()))

    def test_los_paquetes_del_ucp_traen_esfuerzo_referencias_y_criterio(self):
        fichas, _ = gd.construir()
        ucp = [f for f in fichas if f["paquete"]["metodo"] == "UCP"]
        self.assertEqual(len(ucp), 51)
        for f in ucp:
            self.assertEqual(f["vals"]["esfuerzo"][1], "derivado")
            self.assertTrue(f["vals"]["referencias"][0].startswith("RF-") or "casos de uso" in f["vals"]["referencias"][0])
        total = sum(float(f["paquete"]["uucw"]) for f in ucp)
        self.assertEqual(total, 645)

    def test_lo_que_no_tiene_fuente_queda_por_definir(self):
        fichas, _ = gd.construir()
        # una cuenta sin casos de uso ni origen: el diccionario no puede derivar nada de ella
        f = next(x for x in fichas if not x["paquete"]["casos"] and not x["paquete"]["origen"] and x["paquete"]["rama"] != "1.10")
        for clave in ("descripcion", "criterio", "costo", "recursos", "referencias"):
            self.assertEqual(f["vals"][clave][1], "por definir", clave)
        self.assertEqual(f["vals"]["responsable"][1], "propuesta")
        self.assertIn("Jefe de Proyecto", f["vals"]["responsable"][0])

    def test_los_costos_nunca_se_derivan(self):
        fichas, _ = gd.construir()
        self.assertTrue(all(f["vals"]["costo"][1] == "por definir" for f in fichas))

    def test_el_ajuste_manual_gana_y_se_marca(self):
        m = manual([("1.12.4", "Criterio de aceptación", "Acta firmada por la Contraparte Técnica"), ("1.1.1", "responsable", "Jefe de Proyecto")])
        fichas, hall = gd.construir(manual=m)
        self.assertEqual(hall, [])
        f = next(x for x in fichas if x["paquete"]["codigo"] == "1.12.4")
        self.assertEqual(f["vals"]["criterio"], ("Acta firmada por la Contraparte Técnica", "manual"))
        g = next(x for x in fichas if x["paquete"]["codigo"] == "1.1.1")
        self.assertEqual(g["vals"]["responsable"][1], "manual")

    def test_ajuste_con_codigo_o_campo_invalido(self):
        m = manual([("9.9.9", "Entregable", "x"), ("1.1.1", "Color", "rojo")])
        _, hall = gd.construir(manual=m)
        self.assertEqual(len(hall), 2)

    def test_el_diccionario_publicado_esta_actualizado(self):
        fichas, hall = gd.construir()
        self.assertEqual(gd.texto(fichas, hall), (DIR / "18_diccionario_edt.md").read_text(encoding="utf-8"))

    def test_la_plantilla_manual_publicada_se_puede_leer_y_esta_vacia_de_datos(self):
        valores, hall = gd.leer_manual(DIR / "19_diccionario_campos_manuales.md")
        self.assertEqual(hall, [])
        self.assertEqual(valores, {})


if __name__ == "__main__":
    unittest.main()
