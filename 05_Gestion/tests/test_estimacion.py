"""La calculadora de Puntos de Casos de Uso reproduce los ejemplos de la clase FEP03.

Puerta de entrada del plan de estimación: antes de usar la calculadora con datos del
proyecto, debe dar los mismos números que las diapositivas 32 y 59 a 66.
"""

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import estimacion_ucp as u  # noqa: E402

# Diap. 59 a 66: actores, casos de uso y factores del ejemplo completo.
ACTORES_EJEMPLO = [3, 3, 3, 2, 1, 1, 1, 1]
CASOS_EJEMPLO = [3, 2, 2, 3, 3, 3, 6, 5, 6, 5, 7, 4, 11, 9]
# Valores que dan los totales de la clase (49,5 y 18). T6 = 2, T7 = 5 y T11 = 5 como dice la diap. 62.
TCF_EJEMPLO = [3, 4, 4, 2, 2, 2, 5, 5, 5, 2, 5, 4, 2]
EF_EJEMPLO = [4, 2, 3, 4, 4, 2, 1, 1]


class ValoresDeLaClaseTest(unittest.TestCase):
    def test_ejemplo_minimo_diapositiva_32(self):
        self.assertEqual(u.uaw([3]), 3)
        self.assertEqual(u.uucw([2, 2, 2, 2]), 20)
        self.assertEqual(u.uucp([3], [2, 2, 2, 2]), 23)

    def test_ejemplo_completo_pasos_1_a_3(self):
        self.assertEqual(u.uaw(ACTORES_EJEMPLO), 15)
        self.assertEqual(u.uucw(CASOS_EJEMPLO), 120)
        self.assertEqual(u.uucp(ACTORES_EJEMPLO, CASOS_EJEMPLO), 135)

    def test_ejemplo_completo_factores_y_ucp(self):
        self.assertAlmostEqual(u.tcf(TCF_EJEMPLO), 1.095, places=6)
        self.assertAlmostEqual(u.ef(EF_EJEMPLO), 0.86, places=6)
        self.assertAlmostEqual(u.ucp(ACTORES_EJEMPLO, CASOS_EJEMPLO, TCF_EJEMPLO, EF_EJEMPLO), 127.13, places=1)

    def test_ejemplo_completo_esfuerzo_y_reparto(self):
        r = u.calcular({"actores": ACTORES_EJEMPLO, "casos": CASOS_EJEMPLO, "tcf": TCF_EJEMPLO, "ef": EF_EJEMPLO})
        self.assertEqual(r["CF"], 20)
        # La clase redondea el UCP a 127,1 antes de multiplicar y publica 2.542 horas. Con los decimales
        # completos da 2.542,6 (diap. 63 pide conservar los decimales hasta el final). La diferencia es
        # menor que una hora y la prueba la acepta, pero queda documentada.
        self.assertAlmostEqual(r["E"], 2542, delta=1)
        self.assertAlmostEqual(r["total"], 6355, delta=2)
        esperado = {"Análisis": 636, "Diseño": 1271, "Programación": 2542, "Pruebas": 953, "Sobrecarga": 953}
        for nombre, _, h in r["reparto"]:
            self.assertAlmostEqual(h, esperado[nombre], delta=1.5, msg=nombre)

    def test_lectura_a_no_divide(self):
        self.assertAlmostEqual(u.total_proyecto(2542, "A"), 2542)
        self.assertAlmostEqual(u.total_proyecto(2542, "B"), 6355)


class ReglasTest(unittest.TestCase):
    def test_cortes_de_transacciones(self):
        self.assertEqual(u.clasificar_caso(1), ("simple", 5))
        self.assertEqual(u.clasificar_caso(3), ("simple", 5))
        self.assertEqual(u.clasificar_caso(4), ("medio", 10))
        self.assertEqual(u.clasificar_caso(7), ("medio", 10))
        self.assertEqual(u.clasificar_caso(8), ("complejo", 15))

    def test_rango_de_los_coeficientes(self):
        self.assertAlmostEqual(u.tcf([0] * 13), 0.60)
        self.assertAlmostEqual(u.tcf([5] * 13), 1.30)
        self.assertAlmostEqual(u.tcf([3] * 13), 1.02)
        # El peor equipo: factores positivos en 0 y E7 y E8 en 5. El mejor: al revés.
        self.assertAlmostEqual(u.ef([0, 0, 0, 0, 0, 0, 5, 5]), 1.70)
        self.assertAlmostEqual(u.ef([5, 5, 5, 5, 5, 5, 0, 0]), 0.425, places=3)

    def test_factor_de_conversion_segun_factores_desfavorables(self):
        self.assertEqual(u.factor_conversion([3, 3, 3, 3, 3, 3, 3, 3]), 20)
        self.assertEqual(u.factor_conversion([2, 2, 2, 3, 3, 3, 3, 3]), 28)
        self.assertEqual(u.factor_conversion([2, 2, 2, 2, 3, 3, 3, 3]), 28)
        with self.assertRaises(ValueError):
            u.factor_conversion([2, 2, 2, 2, 2, 3, 3, 3])

    def test_e7_y_e8_son_desfavorables_cuando_superan_3(self):
        self.assertEqual(u.factores_desfavorables([3, 3, 3, 3, 3, 3, 4, 5]), 2)
        self.assertEqual(u.factores_desfavorables([3, 3, 3, 3, 3, 3, 3, 3]), 0)

    def test_rechaza_valores_invalidos(self):
        with self.assertRaises(ValueError):
            u.tcf([6] + [3] * 12)
        with self.assertRaises(ValueError):
            u.ef([3] * 7)
        with self.assertRaises(ValueError):
            u.uaw([4])
        with self.assertRaises(ValueError):
            u.clasificar_caso(0)

    def test_sensibilidad_usa_el_otro_factor_de_conversion(self):
        r = u.calcular({"actores": [3], "casos": [2, 2, 2, 2], "tcf": [3] * 13, "ef": [3] * 8})
        self.assertEqual(r["CF"], 20)
        self.assertEqual(r["sensibilidad"]["CF_alternativo"], 28)
        self.assertAlmostEqual(r["sensibilidad"]["total_alternativo"] / r["total"], 1.4)


class LineaDeComandosTest(unittest.TestCase):
    def test_ejecuta_con_un_json(self):
        entrada = {"actores": ACTORES_EJEMPLO, "casos": CASOS_EJEMPLO, "tcf": TCF_EJEMPLO, "ef": EF_EJEMPLO}
        with tempfile.TemporaryDirectory() as tmp:
            ruta = Path(tmp) / "entrada.json"
            ruta.write_text(json.dumps(entrada), encoding="utf-8")
            salida = io.StringIO()
            with redirect_stdout(salida):
                codigo = u.main([str(ruta)])
        self.assertEqual(codigo, 0)
        self.assertIn("UUCP 135", salida.getvalue())
        self.assertIn("UCP 127.13", salida.getvalue())


if __name__ == "__main__":
    unittest.main()
