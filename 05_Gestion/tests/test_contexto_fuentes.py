"""Pruebas de selección de contexto: fuente real, ausencia y ambigüedad."""
import json
import io
from contextlib import redirect_stdout
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import contexto_fuentes as cf
import brief
import estado
import desfase_contexto


class ContextoTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def put(self, name, content):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf8")
        return p

    def make_part(self, number=4, tex=True):
        part = f"T7-{number:02d}"
        folder = f"02_Propuesta/sd-{number:02d}_prueba"
        self.put(f"{folder}/sd-{number:02d}_prueba.md", f"---\nid: {part}\nestado: borrador\n---\n# Anterior\nCONTENIDO_ANTERIOR\n")
        if tex:
            p = cf.main_tex(self.root, part)
            self.put(str(p.relative_to(self.root)), r"\begin{document}" + "\n" + r"\section{4.1 Actual}" + "\nCONTENIDO_ACTUAL\n" + r"\subsection{4.1.1 Detalle}" + "\nDETALLE\n" + r"\section{4.2 Siguiente}" + "\nSIGUIENTE\n" + r"\end{document}")
        return part

    def test_latex_prevalece_y_exhibe_procedencia(self):
        part = self.make_part()
        text = brief.render(self.root, part)
        self.assertIn("CONTENIDO_ACTUAL", text)
        self.assertNotIn("CONTENIDO_ANTERIOR", text)
        self.assertIn(cf.sha256(cf.main_tex(self.root, part)), text)
        self.assertIn("sin revisión humana registrada", text)

    def test_seccion_incluye_hijas_no_siguiente(self):
        self.make_part()
        source = cf.resolve(self.root, "T7-04-4.1")
        self.assertIsNone(source.warning)
        self.assertIn("DETALLE", source.text)
        self.assertNotIn("SIGUIENTE", source.text)

    def test_seccion_ambigua_no_recupera_markdown(self):
        self.make_part()
        p = cf.main_tex(self.root, "T7-04")
        p.write_text(p.read_text(encoding="utf8") + "\n" + r"\section{4.1 Otro}" + "\nOTRO", encoding="utf8")
        source = cf.resolve(self.root, "T7-04-4.1")
        self.assertIn("sin correspondencia inequívoca", source.warning)
        self.assertIn("CONTENIDO_ACTUAL", source.text)
        self.assertNotIn("CONTENIDO_ANTERIOR", source.text)

    def test_seccion_ausente_muestra_fuente_principal(self):
        self.make_part()
        source = cf.resolve(self.root, "T7-04-4.9")
        self.assertIsNotNone(source.warning)
        self.assertEqual(source.path.suffix, ".tex")

    def test_parte_sin_latex_usa_markdown(self):
        part = self.make_part(10, tex=False)
        source = cf.resolve(self.root, part)
        self.assertEqual(source.path.suffix, ".md")
        self.assertIn("todavía no existe LaTeX", source.warning)

    def test_referencias_y_declaracion(self):
        text = r"\section*{Referencias}" + "\nBIBLIO\n" + r"\section*{Declaración de uso de IA}" + "\nUSO"
        self.assertEqual(cf.section_text(text, "REF")[0], r"\section*{Referencias}" + "\nBIBLIO\n")
        self.assertIn("USO", cf.section_text(text, "IA")[0])

    def test_formulario_ignora_copia_local_y_recepcion(self):
        p = self.put("02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-11.tex", "ACTUAL")
        self.put("02_Propuesta/latex_final/sd-04/OSS-Formulario-T-11.tex", "LOCAL_DIVERGENTE")
        self.put("80_Artefactos/recepcion-subdocumentos-prueba/OnlySimpleSolutions-Formulario-T-11.tex", "RECIBIDO")
        self.assertEqual(cf.resolve(self.root, "T-11").path, p)
        p.unlink()
        with self.assertRaisesRegex(ValueError, "falta la fuente"):
            cf.resolve(self.root, "T-11")

    def test_adjunto_registrado_resuelve_formulario_actual(self):
        p = self.put("02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-14.tex", "EDT")
        self.put("05_Gestion/adjuntos.json", json.dumps([{"id": "ADJ-014", "nombre": "form-T-14_plan.docx", "ruta": "02_Propuesta/sd-07_antiguo/form-T-14_plan.docx"}]))
        self.assertEqual(cf.resolve(self.root, "ADJ-014").path, p)

    def test_no_busca_id_en_historicos(self):
        self.put("02_Propuesta/historico/nota.md", "---\nid: T7-04\n---\nVIEJO")
        with self.assertRaises(ValueError): cf.resolve(self.root, "T7-04")

    def test_compilacion_sin_hash_no_acredita_vigencia(self):
        part = self.make_part()
        self.put("salida.pdf", "pdf ficticio")
        self.put("02_Propuesta/latex_final/build/ultimo-reporte.json", json.dumps({"partes": [{"id": part, "pdf": "salida.pdf"}]}))
        self.assertIn("no acreditada por hash", cf.compilation(self.root, part))

    def test_compilacion_con_hash_distingue_desfase(self):
        part = self.make_part()
        self.put("salida.pdf", "pdf ficticio")
        self.put("02_Propuesta/latex_final/build/ultimo-reporte.json", json.dumps({"partes": [{"id": part, "pdf": "salida.pdf", "fuente_sha256": cf.sha256(cf.main_tex(self.root, part))}]}))
        self.assertIn("hash coincidente", cf.compilation(self.root, part))
        cf.main_tex(self.root, part).write_text("otra versión", encoding="utf8")
        self.assertIn("fuente anterior", cf.compilation(self.root, part))

    def test_tablero_separa_dimensiones_y_pendientes(self):
        self.make_part()
        self.make_part(10, tex=False)
        table = estado.render(self.root)
        self.assertIn("Fuente disponible | Estado declarado | Compilación disponible | Revisión humana", table)
        self.assertIn("Markdown; pendiente LaTeX", table)
        self.assertIn("no aplica: sin LaTeX", table)

    def test_detector_no_tacha_recuento_oficial_v30(self):
        self.put("contexto/ficha.md", "Catálogo v3.0 oficial: 226 RF, 76 RNF y 9 OP.\n")
        output = io.StringIO()
        with mock.patch.object(desfase_contexto, "CARPETA", self.root / "contexto"), mock.patch.object(sys, "argv", ["desfase_contexto.py"]), redirect_stdout(output):
            result = desfase_contexto.main()
        self.assertEqual(result, 0)

    def test_detector_pide_conciliar_v31_sin_promoverla(self):
        self.put("contexto/ficha.md", "Catálogo v3.1: 308 requerimientos, 227 RF y 72 RNF.\n")
        output = io.StringIO()
        with mock.patch.object(desfase_contexto, "CARPETA", self.root / "contexto"), mock.patch.object(sys, "argv", ["desfase_contexto.py"]), redirect_stdout(output):
            result = desfase_contexto.main()
        self.assertEqual(result, 1)
        self.assertIn("v3.0 sigue oficial", output.getvalue())
        self.assertNotIn("vigente 308", output.getvalue())

    @unittest.skipUnless(shutil.which("rg"), "rg no disponible")
    def test_busqueda_habitual_excluye_historia_y_derivados(self):
        repo = Path(__file__).resolve().parents[2]
        self.put(".ignore", (repo / ".ignore").read_text(encoding="utf8"))
        active = "80_Artefactos/contexto-activo/indice.md"
        self.put(active, "ACTUAL")
        for name in ("80_Artefactos/archivo-contexto/viejo.md", "80_Artefactos/sd-09_contexto/borradores/viejo.md", "80_Artefactos/sd-03_contexto/historico/no_usar_viejo.md", "80_Artefactos/recepcion-subdocumentos-prueba/recibido.tex", "02_Propuesta/latex_final/respaldo/viejo.tex", "graphify-out/corpus/derivado.txt"):
            self.put(name, "HISTORICO")
        result = subprocess.run(["rg", "--files", "--hidden", "--no-ignore-parent", "."], cwd=self.root, capture_output=True, text=True, check=True)
        self.assertIn("indice.md", result.stdout)
        self.assertNotIn("viejo", result.stdout)
        self.assertNotIn("recibido", result.stdout)
        self.assertNotIn("derivado", result.stdout)


if __name__ == "__main__": unittest.main()
