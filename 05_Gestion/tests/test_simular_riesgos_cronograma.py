"""Pruebas de la simulación de riesgos del cronograma (sd-08): reproducibilidad, orden de percentiles y caso nulo."""

import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import simular_riesgos_cronograma as sim  # noqa: E402

INICIAL = {r: d[0] for r, d in sim.RIESGOS.items()}
RESIDUAL = {r: d[1] for r, d in sim.RIESGOS.items()}


class TestSimulacion(unittest.TestCase):
    def test_misma_semilla_mismo_resultado(self):
        a = sim.simular(INICIAL, 2000, 7)
        b = sim.simular(INICIAL, 2000, 7)
        self.assertEqual(a, b)

    def test_p80_no_menor_que_p50(self):
        for prob in (INICIAL, RESIDUAL):
            res = sim.resumen(sim.simular(prob, 3000, 11))
            for h in sim.HITOS:
                self.assertGreaterEqual(res[h]["p80"], res[h]["p50"])
                self.assertGreaterEqual(res[h]["p90"], res[h]["p80"])

    def test_probabilidad_cero_sin_atraso(self):
        ceros = {r: 0.0 for r in sim.RIESGOS}
        res = sim.resumen(sim.simular(ceros, 1000, 3))
        for h in sim.HITOS:
            self.assertEqual(res[h]["media"], 0.0)
            self.assertEqual(res[h]["p90"], 0.0)
            self.assertEqual(res[h]["p_atraso"], 0.0)

    def test_solapada_no_supera_a_serie(self):
        a = sim.simular(INICIAL, 3000, 9, agregacion="solapada")
        b = sim.simular(INICIAL, 3000, 9, agregacion="serie")
        for h in sim.HITOS:
            for x, y in zip(a[h], b[h]):
                self.assertLessEqual(x, y + 1e-9)

    def test_respuestas_reducen_el_atraso_medio(self):
        a = sim.resumen(sim.simular(INICIAL, 3000, 5))
        b = sim.resumen(sim.simular(RESIDUAL, 3000, 5))
        for h in sim.HITOS:
            self.assertLess(b[h]["media"], a[h]["media"])


if __name__ == "__main__":
    unittest.main()
