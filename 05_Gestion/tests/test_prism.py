"""Paquetes para Prism: empaquetar desde latex_final e importar los cambios validados."""

import json
import shutil
import sys
import unittest
import zipfile
from pathlib import Path

from apoyo import PNG, SCRIPTS, ex, proyecto_temporal

sys.path.insert(0, str(SCRIPTS))
import prism_paquetes as prism  # noqa: E402

HAS_PANDOC = bool(shutil.which("pandoc"))


def leer_zip(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as archive:
        return {i.filename: archive.read(i.filename) for i in archive.infolist()}


def escribir_zip(path: Path, files: dict[str, bytes]) -> Path:
    with zipfile.ZipFile(path, "w") as archive:
        for name, data in files.items():
            archive.writestr(name, data)
    return path


@unittest.skipUnless(HAS_PANDOC, "pandoc no instalado")
class PrismTest(unittest.TestCase):
    def setUp(self):
        self.ctx = proyecto_temporal()
        self.tmp, self.latex = self.ctx.__enter__()
        self.addCleanup(self.ctx.__exit__, None, None, None)
        ex.import_part("T7-14")
        self.tex = self.latex / "sd-14.tex"
        self.zip = prism.package_part("T7-14")
        self.work = self.tmp / "trabajo"
        self.work.mkdir()

    def modificado(self, cambio, nombre="recibido.zip") -> Path:
        files = leer_zip(self.zip)
        cambio(files)
        return escribir_zip(self.work / nombre, files)

    def test_contenido_del_paquete(self):
        names = set(leer_zip(self.zip))
        self.assertIn("sd-14.tex", names)
        self.assertIn("oss.sty", names)
        self.assertIn("LEEME-PRISM.txt", names)
        self.assertTrue(any(n.startswith("figuras/figura-") for n in names))
        self.assertTrue(any(n.startswith("recursos/") and n.endswith(".pdf") for n in names))
        self.assertFalse([n for n in names if n.endswith(".svg") or n.startswith(("plantilla/", "respaldo/", "build/"))])
        self.assertNotIn("manifiesto.json", names)

    def test_paquete_solo_con_figuras_referenciadas(self):
        (self.latex / "figuras" / "otra-parte.png").write_bytes(PNG)
        self.assertNotIn("figuras/otra-parte.png", leer_zip(prism.package_part("T7-14")))

    def test_zip_determinista(self):
        primero = self.zip.read_bytes()
        self.assertEqual(prism.package_part("T7-14").read_bytes(), primero)

    def test_manifiesto_registra_el_empaquetado(self):
        entry = json.loads(ex.MANIFEST.read_text(encoding="utf-8"))["partes"]["T7-14"]["prism"]
        self.assertEqual(entry["empaquetado_sha256"], prism.sha256(self.tex.read_bytes()))

    def test_no_empaqueta_tex_fuera_de_plantilla(self):
        self.tex.write_text("\\documentclass{article}\n\\begin{document}\nx\n\\end{document}\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "fuera de la plantilla"):
            prism.package_part("T7-14")

    def test_ida_y_vuelta_sin_cambios(self):
        antes = self.tex.read_bytes()
        mensajes = prism.import_part("T7-14", self.zip)
        self.assertIn("sin cambios", " ".join(mensajes))
        self.assertEqual(self.tex.read_bytes(), antes)

    def test_importa_edicion_del_cuerpo_con_respaldo(self):
        nuevo = self.modificado(lambda f: f.update({"sd-14.tex": f["sd-14.tex"].replace(b"Primera fila", b"Fila editada en Prism")}))
        prism.import_part("T7-14", nuevo)
        self.assertIn("Fila editada en Prism", self.tex.read_text(encoding="utf-8"))
        respaldos = list((self.latex / "respaldo").glob("sd-14.*.tex"))
        self.assertEqual(len(respaldos), 1)
        self.assertIn("Primera fila", respaldos[0].read_text(encoding="utf-8"))
        entry = json.loads(ex.MANIFEST.read_text(encoding="utf-8"))["partes"]["T7-14"]["prism"]
        self.assertEqual(entry["empaquetado_sha256"], prism.sha256(self.tex.read_bytes()))
        self.assertIn("importado_utc", entry)

    def test_acepta_main_tex_y_carpeta_raiz(self):
        def cambio(files):
            tex = files.pop("sd-14.tex").replace(b"Primera fila", b"Desde main")
            for name in list(files):
                files[f"proyecto/{name}"] = files.pop(name)
            files["proyecto/main.tex"] = tex
        prism.import_part("T7-14", self.modificado(cambio))
        self.assertIn("Desde main", self.tex.read_text(encoding="utf-8"))

    def test_normaliza_saltos_de_linea_windows(self):
        nuevo = self.modificado(lambda f: f.update({"sd-14.tex": f["sd-14.tex"].replace(b"\n", b"\r\n")}))
        self.assertIn("sin cambios", " ".join(prism.import_part("T7-14", nuevo)))

    def test_rechaza_preambulo_alterado(self):
        nuevo = self.modificado(lambda f: f.update({"sd-14.tex": f["sd-14.tex"].replace(b"\\usepackage{oss}", b"\\usepackage{oss}\n\\usepackage{geometry}")}))
        antes = self.tex.read_bytes()
        with self.assertRaisesRegex(ValueError, "fuera de la plantilla"):
            prism.import_part("T7-14", nuevo)
        self.assertEqual(self.tex.read_bytes(), antes)

    def test_rechaza_rutas_peligrosas(self):
        for ruta in ("../escape.tex", "/abs.tex", "figuras/../../x.png"):
            with self.subTest(ruta=ruta):
                with self.assertRaisesRegex(ValueError, "Ruta no admitida"):
                    prism.import_part("T7-14", self.modificado(lambda f, r=ruta: f.update({r: b"x"})))

    def test_rechaza_tipos_no_admitidos(self):
        with self.assertRaisesRegex(ValueError, "no admitido"):
            prism.import_part("T7-14", self.modificado(lambda f: f.update({"figuras/virus.exe": b"x"})))

    def test_rechaza_zip_sin_tex(self):
        with self.assertRaisesRegex(ValueError, "no contiene"):
            prism.import_part("T7-14", self.modificado(lambda f: f.pop("sd-14.tex")))

    def test_rechaza_si_el_repo_cambio_desde_el_empaquetado(self):
        self.tex.write_text(self.tex.read_text(encoding="utf-8").replace("Primera fila", "Cambio local"), encoding="utf-8")
        nuevo = self.modificado(lambda f: f.update({"sd-14.tex": f["sd-14.tex"].replace(b"Segunda fila", b"Cambio Prism")}))
        with self.assertRaisesRegex(ValueError, "cambió en el repositorio"):
            prism.import_part("T7-14", nuevo)
        prism.import_part("T7-14", nuevo, force=True)
        self.assertIn("Cambio Prism", self.tex.read_text(encoding="utf-8"))

    def test_sin_registro_de_empaquetado_exige_forzar(self):
        manifest = json.loads(ex.MANIFEST.read_text(encoding="utf-8"))
        del manifest["partes"]["T7-14"]["prism"]
        ex.MANIFEST.write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "registro de empaquetado"):
            prism.import_part("T7-14", self.zip)

    def test_dry_run_no_escribe(self):
        nuevo = self.modificado(lambda f: f.update({"sd-14.tex": f["sd-14.tex"].replace(b"Primera fila", b"Solo simulado")}))
        antes = self.tex.read_bytes()
        mensajes = prism.import_part("T7-14", nuevo, dry_run=True)
        self.assertIn("+1 -1", " ".join(mensajes))
        self.assertEqual(self.tex.read_bytes(), antes)
        self.assertFalse((self.latex / "respaldo").exists())

    def test_figuras_nuevas_si_existentes_no(self):
        existente = next(n for n in leer_zip(self.zip) if n.startswith("figuras/figura-"))
        def cambio(files):
            files["figuras/nueva.png"] = PNG
            files[existente] = PNG + b"distinta"
        mensajes = prism.import_part("T7-14", self.modificado(cambio))
        self.assertTrue((self.latex / "figuras" / "nueva.png").is_file())
        self.assertNotEqual((self.latex / existente).read_bytes(), PNG + b"distinta")
        self.assertIn("no se sobrescribe", " ".join(mensajes))

    def test_ignora_oss_sty_modificado(self):
        original = (self.latex / "oss.sty").read_bytes()
        mensajes = prism.import_part("T7-14", self.modificado(lambda f: f.update({"oss.sty": b"% manipulado\n"})))
        self.assertEqual((self.latex / "oss.sty").read_bytes(), original)
        self.assertIn("se ignora", " ".join(mensajes))

    def test_zips_de_prueba_del_motor(self):
        a, b = prism.package_probe("T7-14")
        self.assertEqual(set(leer_zip(a)) & {"sd-14.tex", "oss.sty", "LEEME.txt"}, {"sd-14.tex", "oss.sty", "LEEME.txt"})
        archivos_b = leer_zip(b)
        self.assertIn("main.tex", archivos_b)
        self.assertNotIn(b"fontspec", archivos_b["main.tex"])


class NombresTest(unittest.TestCase):
    def test_quita_carpeta_raiz_unica(self):
        self.assertEqual(set(prism.normalize_names(["p/a.tex", "p/figuras/b.png", "p/"]).values()), {"a.tex", "figuras/b.png"})

    def test_conserva_si_hay_archivos_en_la_raiz(self):
        self.assertEqual(set(prism.normalize_names(["a.tex", "figuras/b.png"]).values()), {"a.tex", "figuras/b.png"})


if __name__ == "__main__":
    unittest.main()
