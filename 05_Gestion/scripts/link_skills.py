#!/usr/bin/env python3
"""Expone las skills compartidas de .agents/skills/ a Claude Code (.claude/skills/).

Codex y OpenCode leen .agents/skills/ directamente; Claude Code solo lee .claude/skills/.
En Linux/macOS crea symlinks relativos; en Windows crea junctions (mklink /J, sin administrador).
Es idempotente y nunca reemplaza una carpeta con contenido.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / ".agents" / "skills"
TARGET = ROOT / ".claude" / "skills"
LEGACY = ROOT / ".opencode" / "skills"


def is_link(path: Path) -> bool:
    if path.is_symlink():
        return True
    if os.name == "nt" and path.exists():
        import stat
        return bool(path.lstat().st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT)
    return False


def link_one(source: Path, link: Path, dry_run: bool) -> str:
    if is_link(link):
        if link.resolve() == source.resolve():
            return "ok"
        raise RuntimeError(f"{link} apunta a otro destino: {link.resolve()}")
    if link.exists():
        if link.is_dir() and not any(link.iterdir()):
            if not dry_run:
                link.rmdir()
        else:
            raise RuntimeError(f"No se reemplaza una carpeta no vacía: {link}")
    if dry_run:
        return "crearía"
    link.parent.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        result = subprocess.run(["cmd.exe", "/c", "mklink", "/J", str(link), str(source)], capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(f"No se pudo crear la junction {link}: {result.stderr or result.stdout}")
    else:
        link.symlink_to(os.path.relpath(source, link.parent), target_is_directory=True)
    return "creado"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="muestra qué haría sin modificar nada")
    args = parser.parse_args()
    skills = sorted(p for p in SOURCE.iterdir() if (p / "SKILL.md").is_file()) if SOURCE.is_dir() else []
    if not skills:
        print(f"No hay skills en {SOURCE}", file=sys.stderr)
        return 1
    failed = 0
    for skill in skills:
        link = TARGET / skill.name
        try:
            print(f"{link.relative_to(ROOT)}: {link_one(skill, link, args.dry_run)}")
        except RuntimeError as exc:
            failed += 1
            print(f"Error: {exc}", file=sys.stderr)
    for skill in skills:
        old = LEGACY / skill.name
        if is_link(old):
            print(f"Aviso: {old.relative_to(ROOT)} es un enlace antiguo; OpenCode ya lee .agents/skills/. "
                  "Se puede borrar (solo el enlace) para evitar skills duplicadas.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
