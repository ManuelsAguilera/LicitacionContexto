"""verificar-redaccion detecta incumplimientos de las reglas RR-NN y las convenciones están segmentadas."""

import re
import sys
import tempfile
import unittest
from pathlib import Path

from apoyo import REPO, SCRIPTS, ex, tex_valido

sys.path.insert(0, str(SCRIPTS))
import verificar_redaccion as vr  # noqa: E402

CELDA = r"\begin{minipage}[b]{\linewidth}\raggedright" + "\n@@\n" + r"\end{minipage}"


def tabla(columnas: list[str], filas: list[list[str]]) -> str:
    spec = "".join(r">{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.2}}" + "\n" for _ in columnas)
    cabecera = " & ".join(CELDA.replace("@@", c) for c in columnas) + r" \\"
    cuerpo = "\n".join(" & ".join(fila) + r" \\" for fila in filas)
    return (f"\\begin{{longtable}}[]{{@{{}}\n{spec}@{{}}}}\n\\toprule\\noalign{{}}\n{cabecera}\n\\midrule\\noalign{{}}\n"
            f"\\endhead\n\\bottomrule\\noalign{{}}\n\\endlastfoot\n{cuerpo}\n\\end{{longtable}}")


def tex(cuerpo: str) -> str:
    base = tex_valido().split("\\begin{document}", 1)[0]
    return base + "\\begin{document}\n\\ossCover{T}{Subdocumento 1}\n\\tableofcontents\n\\clearpage\n" + cuerpo + "\n\n\\ossFinalPage\n\\end{document}\n"


def revisar(cuerpo: str) -> list[vr.Finding]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "sd-01.tex"
        path.write_text(tex(cuerpo), encoding="utf-8")
        return vr.check_file(path)


def reglas(findings, nivel=None) -> set[str]:
    return {f.rule for f in findings if nivel is None or f.level == nivel}


CIERRE = "\\section{Referencias}\n\nLista.\n\n\\section{Declaración de uso de IA}\n\nDeclaración.\n"
BUENO = (
    "\\section{1.1 Capítulo}\n\nIntroducción del capítulo.\n\n"
    "Tabla 1.1: Cifras comparadas. Fuente: elaboración propia.\n\n"
    + tabla(["Código", "Valor"], [["A", "10"], ["B", "20"]])
    + "\n\nLa tabla muestra que B duplica a A.\n\n" + CIERRE
)


class ReglasTest(unittest.TestCase):
    def test_documento_correcto_sin_hallazgos(self):
        self.assertEqual(revisar(BUENO), [])

    def test_rr04_titulo_seguido_de_titulo_tabla_figura_lista(self):
        casos = {
            "\\section{A}\n\n\\subsection{B}\n\nTexto.\n": "otro título",
            "\\section{A}\n\n" + tabla(["x", "y"], [["1", "2"]]) + "\n": "una tabla",
            "\\section{A}\n\n\\begin{figure}\n\\includegraphics{x.png}\n\\caption{c}\n\\end{figure}\n": "una figura",
            "\\section{A}\n\n\\begin{itemize}\n\\item uno\n\\end{itemize}\n": "una lista",
        }
        for cuerpo, texto in casos.items():
            with self.subTest(texto=texto):
                hallazgos = [f for f in revisar(cuerpo) if f.rule == "RR-04"]
                self.assertTrue(hallazgos and texto in hallazgos[0].message, hallazgos)
                self.assertEqual(hallazgos[0].level, "ERROR")

    def test_rr04_encabezado_con_hypertarget_y_titulo_multilinea(self):
        cuerpo = "\\hypertarget{a}{%\n\\section{Título\nmuy largo}\\label{a}}\n\nTexto de caída.\n\n" + CIERRE
        self.assertNotIn("RR-04", reglas(revisar(cuerpo)))

    def test_rr17_mas_de_cinco_columnas(self):
        cols = list("abcdef")
        cuerpo = "\\section{A}\n\nIntro.\n\nTabla 1.1: T.\n\n" + tabla(cols, [["1"] * 6]) + "\n\nConcluye.\n"
        self.assertIn("RR-17", reglas(revisar(cuerpo), "ERROR"))

    def test_rr16_concepto_descripcion_y_celdas_con_varias_frases(self):
        cuerpo = ("\\section{A}\n\nIntro.\n\nTabla 1.1: T.\n\n"
                  + tabla(["Concepto", "Descripción"], [["Uno", "Primera frase larga. Segunda frase que explica más."]])
                  + "\n\nConcluye.\n")
        mensajes = " ".join(f.message for f in revisar(cuerpo) if f.rule == "RR-16")
        self.assertIn("Concepto", mensajes)
        self.assertIn("más de una frase", mensajes)

    def test_rr16_celda_de_una_frase_con_punto_y_coma_es_valida(self):
        cuerpo = ("\\section{A}\n\nIntro.\n\nTabla 1.1: T.\n\n"
                  + tabla(["Código", "Detalle"], [["R-01", "Mantener oferta; habilitar la consistencia."]]) + "\n\nConcluye.\n")
        self.assertNotIn("RR-16", reglas(revisar(cuerpo)))

    def test_rr18_tabla_larga(self):
        cuerpo = ("\\section{A}\n\nIntro.\n\nTabla 1.1: T.\n\n" + tabla(["a", "b"], [["1", "2"]] * 30) + "\n\nConcluye.\n")
        self.assertIn("RR-18", reglas(revisar(cuerpo)))

    def test_rr19_tabla_sin_titulo_ni_conclusion(self):
        cuerpo = "\\section{A}\n\nIntro.\n\n" + tabla(["a", "b"], [["1", "2"]]) + "\n\n\\section{B}\n\nTexto.\n"
        mensajes = " ".join(f.message for f in revisar(cuerpo) if f.rule == "RR-19")
        self.assertIn("sin título numerado", mensajes)
        self.assertIn("qué se concluye", mensajes)

    def test_rr11_rr14_figura_sin_titulo_ni_fuente(self):
        cuerpo = "\\section{A}\n\nIntro.\n\n\\begin{figure}\n\\includegraphics{x.png}\n\\end{figure}\n\nTexto.\n"
        self.assertTrue({"RR-11", "RR-14"} <= reglas(revisar(cuerpo)))

    def test_rr14_figura_con_fuente_pasa(self):
        cuerpo = ("\\section{A}\n\nIntro.\n\n\\begin{figure}\n\\includegraphics{x.png}\n\\caption{Diagrama}\n\\end{figure}\n\n"
                  "Figura 1.1: Diagrama. Fuente: elaboración propia.\n\nSe explica.\n\n" + CIERRE)
        self.assertEqual(revisar(cuerpo), [])

    def test_rr22_marcadores_y_palabra_todo_en_minuscula(self):
        cuerpo = "\\section{A}\n\nTODO completar. Todo el sistema funciona. [VERIFICAR] cifra.\n\n" + CIERRE
        hallazgos = [f for f in revisar(cuerpo) if f.rule == "RR-22"]
        self.assertEqual(len(hallazgos), 1)  # TODO y [VERIFICAR] en la misma línea; «Todo» no cuenta
        self.assertEqual(hallazgos[0].level, "ERROR")

    def test_rr22_lenguaje_academico_es_aviso(self):
        cuerpo = "\\section{A}\n\nEl docente evaluará.\n\n" + CIERRE
        self.assertEqual({f.level for f in revisar(cuerpo) if f.rule == "RR-22"}, {"AVISO"})

    def test_rr08_precio(self):
        cuerpo = "\\section{A}\n\nEl valor unitario es 10 UF.\n\n" + CIERRE
        self.assertIn("RR-08", reglas(revisar(cuerpo)))

    def test_rr08_cifras_del_cliente_no_son_precios(self):
        cuerpo = "\\section{A}\n\nIngresos de \\$474.000 millones de pesos.\n\n" + CIERRE
        self.assertNotIn("RR-08", reglas(revisar(cuerpo)))

    def test_rr21_cierre_ausente_o_en_orden_incorrecto(self):
        self.assertIn("RR-21", reglas(revisar("\\section{A}\n\nTexto.\n")))
        invertido = "\\section{A}\n\nTexto.\n\n\\section{Declaración de uso de IA}\n\nX.\n\n\\section{Referencias}\n\nY.\n"
        self.assertIn("RR-21", reglas(revisar(invertido), "ERROR"))

    def test_rr05_capitulo_dominado_por_tablas(self):
        filas = [["dato largo " * 3, "otro dato " * 3]] * 10
        cuerpo = "\\section{A}\n\nBreve.\n\nTabla 1.1: T.\n\n" + tabla(["a", "b"], filas) + "\n\nOk.\n"
        self.assertIn("RR-05", reglas(revisar(cuerpo)))

    def test_no_modifica_el_archivo(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sd-01.tex"
            path.write_text(tex("\\section{A}\n\n\\subsection{B}\n\nX.\n"), encoding="utf-8")
            antes = path.read_bytes()
            vr.check_file(path)
            self.assertEqual(path.read_bytes(), antes)


class SegmentacionTest(unittest.TestCase):
    """Las reglas de redacción y las de plantilla viven separadas y son consistentes con el verificador."""

    def setUp(self):
        self.conv = REPO / "05_Gestion" / "convenciones"
        self.rr = (self.conv / "reglas-redaccion.md").read_text(encoding="utf-8")
        self.rp = (self.conv / "reglas-plantilla.md").read_text(encoding="utf-8")

    def ids(self, text, prefijo):
        return re.findall(rf"^\| ({prefijo}-\d\d) \|", text, re.M)

    def test_ids_unicos_y_sin_mezcla(self):
        rr, rp = self.ids(self.rr, "RR"), self.ids(self.rp, "RP")
        self.assertEqual(len(rr), len(set(rr)))
        self.assertEqual(len(rp), len(set(rp)))
        self.assertTrue(rr and rp)
        self.assertEqual(self.ids(self.rr, "RP"), [])
        self.assertEqual(self.ids(self.rp, "RR"), [])

    def test_ids_consecutivos(self):
        for prefijo, texto in (("RR", self.rr), ("RP", self.rp)):
            numeros = [int(i.split("-")[1]) for i in self.ids(texto, prefijo)]
            self.assertEqual(numeros, list(range(1, len(numeros) + 1)), prefijo)

    def test_cada_regla_cita_su_fuente_y_verificacion(self):
        for linea in self.rr.splitlines():
            if re.match(r"^\| RR-\d\d \|", linea):
                celdas = [c.strip() for c in re.split(r"(?<!\\)\|", linea.strip().strip("|"))]
                self.assertEqual(len(celdas), 4, linea)
                self.assertTrue(celdas[2].startswith("C10"), f"sin fuente del Comunicado 10: {linea}")
                self.assertRegex(celdas[3], r"^(Auto|Manual)", linea)

    def test_reglas_automaticas_existen_en_la_convencion_y_viceversa(self):
        usadas = set(re.findall(r"RR-\d\d", (SCRIPTS / "verificar_redaccion.py").read_text(encoding="utf-8")))
        declaradas = set(self.ids(self.rr, "RR"))
        self.assertTrue(usadas <= declaradas, usadas - declaradas)
        automaticas = {i for i, linea in zip(self.ids(self.rr, "RR"), [l for l in self.rr.splitlines() if re.match(r"^\| RR-\d\d \|", l)])
                       if "| Auto" in linea}
        self.assertEqual(automaticas, usadas)

    def test_las_reglas_de_redaccion_no_contienen_formato(self):
        for palabra in ("oss.sty", "XeLaTeX", "pdfLaTeX", "margen", "longtable"):
            self.assertNotIn(palabra, self.rr.split("## Qué hacer")[0], palabra)

    def test_las_reglas_de_plantilla_no_contienen_contenido(self):
        for palabra in ("Comunicado 10 §2", "Oferta Técnica", "APA"):
            self.assertNotIn(palabra, self.rp, palabra)

    def test_instrucciones_apuntan_a_ambos_archivos(self):
        agents = (REPO / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("reglas-redaccion.md", agents)
        self.assertIn("reglas-plantilla.md", agents)
        self.assertIn("reglas-redaccion.md", (REPO / ".agents/skills/redactar-seccion/SKILL.md").read_text(encoding="utf-8"))
        self.assertIn("reglas-redaccion.md", (REPO / ".agents/skills/revisar-seccion/SKILL.md").read_text(encoding="utf-8"))

    def test_politica_de_migracion_remite_a_las_reglas(self):
        texto = (self.conv / "artefactos.md").read_text(encoding="utf-8")
        self.assertIn("reglas-redaccion.md", texto)


if __name__ == "__main__":
    unittest.main()
