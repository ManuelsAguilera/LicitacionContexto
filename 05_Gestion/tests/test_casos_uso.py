"""Pruebas de verificar_casos_uso.py con tablas mínimas."""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verificar_casos_uso as v  # noqa: E402

ANEXO_B = """## B.3
| ID | Requerimiento | Código | Servicio | Etapa |
| :-- | :-- | :-- | :-- | :-- |
| RF-001 | El sistema debe a. | R:M-03 | Servicio de existencias | 1 |
| RF-002 | El sistema debe b. | R:M-03 | Servicio de existencias | 1 |
| RF-003 | El sistema debe c. | R:M-03 | Servicio de existencias | 1 |
| RF-004 | El sistema debe d. | R:V-02 | Servicio de ventas | 1 |
"""
ANEXO_A = "| EXC-12 | No se hace | Sí se hace | Caso |\n| RC-10 | Responsabilidad | Caso |\n"
ACTORES = "| AH-03 | Vendedor |\n| AS-14 | Temporizador |\n"
CAB = "| Código | Servicio | Caso de uso | Actor principal | Trans. | Origen | Supuestos |\n| :-- | :-- | :-- | :-- | --: | :-- | :-- |\n"
CAB_T = "\n| Código | Transacciones |\n| :-- | :-- |\n"


def correr(casos, trans, completo=False):
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        (d / "03_casos_de_uso_x.md").write_text(CAB + casos + CAB_T + trans, encoding="utf-8")
        (d / "b.md").write_text(ANEXO_B, encoding="utf-8")
        (d / "a.md").write_text(ANEXO_A, encoding="utf-8")
        (d / "act.md").write_text(ACTORES, encoding="utf-8")
        return v.verificar(d, d / "b.md", d / "a.md", d / "act.md", completo)


class TestCasosUso(unittest.TestCase):
    def test_expande_rangos(self):
        self.assertEqual(v.expandir("RF-001 a RF-003, RF-009; 3.4.1"), {"RF-001", "RF-002", "RF-003", "RF-009"})

    def test_modelo_correcto(self):
        h = correr("| CU-EX-01 | R:M-03 | Consultar | AH-03 | 2 | RF-001 a RF-003 | S1 |\n", "| CU-EX-01 | T1 uno. T2 dos |\n")
        self.assertEqual(h, [])

    def test_rf_huerfano(self):
        h = correr("| CU-EX-01 | R:M-03 | Consultar | AH-03 | 2 | RF-001, RF-002 | S1 |\n", "| CU-EX-01 | T1 uno. T2 dos |\n")
        self.assertTrue(any("RF-003" in x and "ningún caso" in x for x in h))

    def test_caso_sin_fuente(self):
        h = correr("| CU-EX-01 | R:M-03 | Consultar | AH-03 | 2 | sin cita | S1 |\n", "| CU-EX-01 | T1 uno. T2 dos |\n")
        self.assertTrue(any("no cita" in x for x in h))

    def test_exclusion_inexistente_y_rf_ajeno(self):
        h = correr("| CU-EX-01 | R:M-03 | Consultar | AH-03 | 2 | RF-001 a RF-003, EXC-99, RF-777 | S1 |\n", "| CU-EX-01 | T1 uno. T2 dos |\n")
        self.assertTrue(any("EXC-99" in x for x in h))
        self.assertTrue(any("RF-777" in x for x in h))

    def test_exceso_de_transacciones_y_conteo_desigual(self):
        t = " ".join(f"T{i} x." for i in range(1, 14))
        h = correr("| CU-EX-01 | R:M-03 | Consultar | AH-03 | 13 | RF-001 a RF-003 | S1 |\n", f"| CU-EX-01 | {t} |\n")
        self.assertTrue(any("máximo 12" in x for x in h))
        h = correr("| CU-EX-01 | R:M-03 | Consultar | AH-03 | 3 | RF-001 a RF-003 | S1 |\n", "| CU-EX-01 | T1 uno. T2 dos |\n")
        self.assertTrue(any("declara 3" in x for x in h))

    def test_actor_desconocido(self):
        h = correr("| CU-EX-01 | R:M-03 | Consultar | AH-99 | 2 | RF-001 a RF-003 | S1 |\n", "| CU-EX-01 | T1 uno. T2 dos |\n")
        self.assertTrue(any("AH-99" in x for x in h))

    def test_rf_en_dos_casos(self):
        casos = ("| CU-EX-01 | R:M-03 | A | AH-03 | 2 | RF-001 a RF-003 | S1 |\n"
                 "| CU-EX-02 | R:M-03 | B | AS-14 | 2 | RF-003 | S1 |\n")
        h = correr(casos, "| CU-EX-01 | T1 a. T2 b |\n| CU-EX-02 | T1 a. T2 b |\n")
        self.assertTrue(any(x.startswith("P3.6") and "RF-003" in x for x in h))

    def test_casos_de_una_transaccion_en_masa(self):
        casos = ("| CU-EX-01 | R:M-03 | A | AH-03 | 1 | RF-001 | S1 |\n"
                 "| CU-EX-02 | R:M-03 | B | AS-14 | 1 | RF-002 | S1 |\n"
                 "| CU-EX-03 | R:M-03 | C | AS-14 | 3 | RF-003 | S1 |\n")
        h = correr(casos, "| CU-EX-01 | T1 a |\n| CU-EX-02 | T1 a |\n| CU-EX-03 | T1 a. T2 b. T3 c |\n")
        self.assertTrue(any("30 %" in x for x in h))

    def test_caso_excluido(self):
        h = correr("| CU-EX-01 | R:M-03 | Instalar etiquetas electrónicas | AH-03 | 2 | RF-001 a RF-003 | S1 |\n", "| CU-EX-01 | T1 a. T2 b |\n")
        self.assertTrue(any(x.startswith("P3.4") for x in h))

    def test_completo_exige_todos_los_servicios(self):
        casos, trans = "| CU-EX-01 | R:M-03 | A | AH-03 | 2 | RF-001 a RF-003 | S1 |\n", "| CU-EX-01 | T1 a. T2 b |\n"
        self.assertFalse(any("P3.2" in x for x in correr(casos, trans)))
        self.assertTrue(any("P3.2" in x and "ventas" in x for x in correr(casos, trans, completo=True)))

    def test_actor_sin_caso_solo_en_completo(self):
        casos, trans = "| CU-EX-01 | R:M-03 | A | AH-03 | 2 | RF-001 a RF-003 | S1 |\n", "| CU-EX-01 | T1 a. T2 b |\n"
        self.assertFalse(any("P3.7" in x for x in correr(casos, trans)))
        self.assertTrue(any("P3.7" in x and "AS-14" in x for x in correr(casos, trans, completo=True)))

    def test_actor_secundario_declarado_cuenta(self):
        casos, trans = "| CU-EX-01 | R:M-03 | A | AH-03 | 2 | RF-001 a RF-003 | S1 |\n", "| CU-EX-01 | T1 a. T2 b |\n"
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "03_casos_de_uso_x.md").write_text(CAB + casos + CAB_T + trans + "\n| S1 | Actores secundarios: AS-14 en CU-EX-01 |\n", encoding="utf-8")
            self.assertEqual(v.actores_secundarios(d), {"AS-14"})

    def test_trazabilidad_de_resultados(self):
        casos, trans = "| CU-EX-01 | R:M-03 | A | AH-03 | 2 | RF-001 a RF-003 | S1 |\n", "| CU-EX-01 | T1 a. T2 b |\n"
        filas = "".join(f"| {n} | R | CU-EX-01 | x |\n" for n in range(1, 28)) + "| 28 | R | CU-ZZ-09 | x |\n"
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "03_casos_de_uso_x.md").write_text(CAB + casos + CAB_T + trans, encoding="utf-8")
            (d / "04_trazabilidad_resultados.md").write_text("| N.º | Resultado | Casos | Fuera |\n| :-- | :-- | :-- | :-- |\n" + filas, encoding="utf-8")
            for n, a in (("b.md", ANEXO_B), ("a.md", ANEXO_A), ("act.md", ACTORES)):
                (d / n).write_text(a, encoding="utf-8")
            h = v.verificar(d, d / "b.md", d / "a.md", d / "act.md")
        self.assertTrue(any("resultado 28" in x and "CU-ZZ-09" in x for x in h))
        self.assertFalse(any("resultado 5 " in x for x in h))


if __name__ == "__main__":
    unittest.main()
