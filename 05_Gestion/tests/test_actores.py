"""Las pruebas del maestro de actores detectan los defectos que describen (puerta G2a)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import verificar_actores as v  # noqa: E402

SD02 = r"""
\textbf{Tabla 2.5: Grupos de interés según influencia e interés.}

\begin{longtable}[]{@{}ll@{}}
\toprule\noalign{}
\begin{minipage}[b]{\linewidth}\raggedright
Grupo
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Influencia
\end{minipage} \\
\midrule\noalign{}
\endhead
Dirección y control & Alta \\
Operación de tienda & Media \\
\end{longtable}
"""

MAESTRO = """## 2. Grupos de interés (Tabla 2.5 del sd-02)

| Código | Grupo | Actores |
| :-- | :-- | :-- |
| G-01 | Dirección y control | Directorio |
| G-05 | Operación de tienda | Cajeros |

### 3.1 Personas (tipo 3)

| Código | Actor | Grupo |
| :-- | :-- | :-- |
| AH-04 | Cajero | G-05 |
| AH-07 | Personal de centros | Sin grupo |
"""


class GruposTest(unittest.TestCase):
    def test_lee_los_grupos_del_sd02(self):
        self.assertEqual(v.grupos_sd02(SD02), ["Dirección y control", "Operación de tienda"])

    def test_detecta_grupo_ausente(self):
        self.assertEqual(v.grupos_cubiertos(MAESTRO, ["Dirección y control", "Propiedad"]),
                         ["P2a.1 el grupo «Propiedad» del sd-02 no está en el maestro"])

    def test_acepta_todos_los_grupos(self):
        self.assertEqual(v.grupos_cubiertos(MAESTRO, v.grupos_sd02(SD02)), [])


class VocabularioTest(unittest.TestCase):
    def test_detecta_sistema_no_nombrado(self):
        out = v.vocabulario_ausente("El ERP/DTE y los transportistas.", "Solo el ERP/DTE.")
        self.assertEqual(len(out), 1)
        self.assertIn("Transportistas", out[0])

    def test_no_exige_lo_que_el_sd03_no_menciona(self):
        self.assertEqual(v.vocabulario_ausente("Texto sin actores.", "Maestro."), [])


class SinonimosTest(unittest.TestCase):
    def test_detecta_nombres_distintos(self):
        out = v.sinonimos_en_uso("La Contraloría exige.", "El Emisor y Cumplimiento evalúan.")
        self.assertEqual(len(out), 1)

    def test_ignora_la_palabra_comun(self):
        self.assertEqual(v.sinonimos_en_uso("La Contraloría exige.", "El cumplimiento de la meta."), [])

    def test_sin_conflicto_si_ambos_usan_el_mismo(self):
        self.assertEqual(v.sinonimos_en_uso("La Contraloría.", "La Contraloría."), [])


class GrupoDeActorTest(unittest.TestCase):
    def test_detecta_actor_sin_grupo(self):
        out = v.actores_sin_grupo(MAESTRO)
        self.assertEqual(len(out), 1)
        self.assertIn("AH-07", out[0])


if __name__ == "__main__":
    unittest.main()
