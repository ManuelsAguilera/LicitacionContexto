"""Pruebas de verificar_edt.py con EDT mínimas."""

import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "05_Gestion" / "scripts"))
import verificar_edt as v  # noqa: E402


def correr(texto):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "edt.md"
        p.write_text(texto, encoding="utf-8")
        return v.verificar(p)


def edt(*paquetes, titulo="Rama de prueba", declarados=None):
    n = declarados if declarados is not None else len(paquetes)
    cuerpo = "\n".join(f"- 1.1.{i} {x}" for i, x in enumerate(paquetes, 1))
    return f"### 1.1 {titulo} — {n} paquetes\n\n{cuerpo}\n"


def codigos(h):
    return {(x["codigo"], x["tipo"]) for x in h}


class TestVerificarEdt(unittest.TestCase):
    def test_edt_limpia(self):
        h = [x for x in correr(edt("Plan de dirección integrado", "Registro de supuestos")) if x["tipo"] == "falta"]
        self.assertEqual(h, [])

    def test_verbo_al_inicio(self):
        self.assertIn(("C6", "falta"), codigos(correr(edt("Desarrollar el motor de precios", "Registro de supuestos"))))

    def test_fechas_hitos_y_meses(self):
        for nombre in ("Acta de aceptación (H7, mes 16)", "Plan de marcha (13–15)", "Plan inicial en 90 días"):
            self.assertIn(("C2", "falta"), codigos(correr(edt(nombre, "Registro de supuestos"))), nombre)
        self.assertIn(("C2", "falta"), codigos(correr(edt("Plan", "Otro plan", titulo="Operación (meses 21–56)"))))

    def test_codigos_externos_y_umbrales(self):
        h = codigos(correr(edt("Control de cambios (Art. 72)", "Consulta de existencia ≤30 s", "Plan (RT-05.11)")))
        self.assertIn(("C3", "falta"), h)
        self.assertIn(("C4", "falta"), h)

    def test_varios_entregables_y_fases(self):
        h = codigos(correr(edt("Certificación Etapa 1 y Certificación Etapa 2", "Marcha blanca de la primera etapa")))
        self.assertIn(("C8", "posible"), h)
        self.assertIn(("C5", "posible"), h)

    def test_nombres_antiguos(self):
        self.assertIn(("C13", "falta"), codigos(correr(edt("Retail: catálogo, precios y promociones", "Frontera X-01: autorización"))))

    def test_cantidad_de_paquetes_declarada(self):
        self.assertIn(("C12", "falta"), codigos(correr(edt("Plan", "Otro plan", declarados=5))))

    def test_rango_cuenta_cinco_paquetes_y_se_informa_una_vez(self):
        texto = "### 1.10 Innovaciones — 5 paquetes\n\n- 1.10.1 … 1.10.5 Un paquete por innovación (RT-26.02)\n"
        h = correr(texto)
        self.assertEqual(len([x for x in h if x["codigo"] == "C3"]), 1)
        self.assertFalse(any(x["codigo"] == "C12" and x["tipo"] == "falta" for x in h))

    @unittest.skipUnless(v.EDT.exists(), "la EDT de Eliseo no está en esta copia de trabajo")
    def test_la_edt_real_se_puede_leer(self):
        ramas, paquetes = v.leer(v.EDT)
        self.assertEqual(len(ramas), 15)
        self.assertEqual(len(paquetes), 110)


if __name__ == "__main__":
    unittest.main()
