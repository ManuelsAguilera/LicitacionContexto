"""Que Codex, OpenCode y Claude Code carguen las mismas instrucciones y la skill exportar."""

import importlib
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from apoyo import REPO, SCRIPTS

sys.path.insert(0, str(SCRIPTS))
link_skills = importlib.import_module("link_skills")

SKILL = REPO / ".agents" / "skills" / "exportar" / "SKILL.md"


class IntegracionTest(unittest.TestCase):
    def test_claude_md_importa_agents_md(self):
        # Claude Code ignora AGENTS.md si existe CLAUDE.md, salvo que lo importe.
        text = (REPO / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^@AGENTS\.md\s*$")

    def test_skill_exportar_activable_por_descripcion(self):
        # Codex y OpenCode eligen la skill por su description.
        text = SKILL.read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^name: exportar$")
        description = re.search(r"(?m)^description: (.+)$", text).group(1).lower()
        for palabra in ("latex", "plantilla", "markdown", "pdf"):
            self.assertIn(palabra, description)

    def test_claude_code_ve_la_skill(self):
        enlace = REPO / ".claude" / "skills" / "exportar" / "SKILL.md"
        self.assertTrue(enlace.is_file(), "ejecutar: python3 05_Gestion/scripts/link_skills.py")
        self.assertEqual(enlace.resolve(), SKILL.resolve())

    def test_regla_de_exportacion_en_agents_md(self):
        text = (REPO / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("## Regla de exportación", text)
        self.assertIn("exportar_latex.py", text)


class LinkSkillsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        for name in ("uno", "dos"):
            (root / ".agents" / "skills" / name).mkdir(parents=True)
            (root / ".agents" / "skills" / name / "SKILL.md").write_text(f"---\nname: {name}\n---\n", encoding="utf-8")
        self.root = root
        patcher = mock.patch.multiple(
            link_skills, ROOT=root, SOURCE=root / ".agents" / "skills",
            TARGET=root / ".claude" / "skills", LEGACY=root / ".opencode" / "skills",
        )
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.tmp.cleanup)

    def run_main(self, *args):
        with mock.patch.object(sys, "argv", ["link_skills.py", *args]):
            return link_skills.main()

    def test_crea_enlaces_y_es_idempotente(self):
        self.assertEqual(self.run_main(), 0)
        for name in ("uno", "dos"):
            self.assertTrue((self.root / ".claude" / "skills" / name / "SKILL.md").is_file())
        self.assertEqual(self.run_main(), 0)

    def test_dry_run_no_crea_nada(self):
        self.assertEqual(self.run_main("--dry-run"), 0)
        self.assertFalse((self.root / ".claude").exists())

    def test_no_pisa_carpeta_con_contenido(self):
        destino = self.root / ".claude" / "skills" / "uno"
        destino.mkdir(parents=True)
        (destino / "propio.md").write_text("no borrar", encoding="utf-8")
        self.assertEqual(self.run_main(), 1)
        self.assertEqual((destino / "propio.md").read_text(encoding="utf-8"), "no borrar")


if __name__ == "__main__":
    unittest.main()
