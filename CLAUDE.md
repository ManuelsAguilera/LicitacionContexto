# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Cómo usar este archivo

El contexto completo del proyecto está en **`AGENTS.md`** (única fuente de verdad), importado aquí para que Claude Code lo cargue al iniciar (Claude Code no lee `AGENTS.md` si existe un `CLAUDE.md`): identidad del proponente (Only Simple Solutions), fuentes y precedencia de `00_Bases/`, regla de exportación, reglas que condicionan el diseño, carpetas y criterios de verificación.

@AGENTS.md

La convención de IDs, estados, metadatos y procedencia está en `05_Gestion/convenciones/artefactos.md`. Los scripts documentales y su uso están descritos en `05_Gestion/README.md`.

Este archivo solo existe para que los usuarios de Claude Code arranquen con el mismo contexto sin duplicar contenido.

## Comandos

No hay build ni lint: el repo es documentación (`.md`, Excel, LaTeX). Las herramientas son los scripts de `05_Gestion/scripts/` (todos aceptan `--help`); el exportador LaTeX tiene pruebas en `05_Gestion/tests/`:

```bash
python3 05_Gestion/scripts/check.py        # verifica trazabilidad/convenciones de artefactos
python3 05_Gestion/scripts/estado.py       # estado de secciones por subdocumento
python3 05_Gestion/scripts/brief.py        # contexto resumido para trabajar una sección
python3 05_Gestion/scripts/agregar_frontmatter.py --dry-run
python3 05_Gestion/scripts/exportar_latex.py doctor|estado|verificar|importar|compilar   # único camino a PDF
python3 05_Gestion/scripts/exportar_latex.py verificar-redaccion [--parte T7-NN]        # reglas de redacción RR-NN (solo informa)
python3 -m unittest discover -s 05_Gestion/tests -v                                    # pruebas del exportador
python3 -m unittest discover -s 05_Gestion/tests -p test_verificar.py                 # un solo archivo de pruebas
```

- Edición: el contenido se redacta en los `.tex` con Prism; no hay importación desde Google Docs ni DOCX.
- PDF de la propuesta: cumplir la "Regla de exportación" de `AGENTS.md` y `.agents/skills/exportar/SKILL.md`. `sd-NN.tex` manda tras importar; los `.md` son solo contexto. Nunca escribir preámbulos ni llamar a `pandoc`/`xelatex` directamente.
- Estado `revisado` solo lo asigna un humano, nunca un script o agente.

## Notas para Claude Code en Linux

- Claude Code solo lee skills de `.claude/skills/`. Tras clonar, ejecutar `python3 05_Gestion/scripts/link_skills.py` (symlinks en Linux/macOS, junctions en Windows; `python` en Windows). Editar siempre `.agents/skills/`.
- Existe `.claude/settings.local.json`; `.env` (copia de `.env.example`) no se versiona.

## Skills y plugin de opencode

El skill orquestador `licitacion-workflow` y el plugin `activar-skills.ts` que viven en `.opencode/` son **específicos de opencode**. No aplican a Claude Code; ignóralos. La exportación a PDF no depende de ellos: la regla está en `AGENTS.md` y la skill `exportar`.

## Skills compartidas

Las skills del flujo de artefactos (`redactar-seccion`, `revisar-seccion`, `cerrar-parte`, `exportar`) viven en `.agents/skills/`, que es la fuente canónica y la que leen Codex y OpenCode. Claude Code las ve solo a través de los enlaces de `.claude/skills/` (`link_skills.py`). No editar las copias enlazadas. Las skills preexistentes de OpenCode (`.opencode/skills/`) se conservan sin cambios.
