# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Cómo usar este archivo

El contexto completo del proyecto está en **`AGENTS.md`** (única fuente de verdad). Léelo antes de trabajar: identidad del proponente (Only Simple Solutions), fuentes y precedencia de `00_Bases/`, reglas que condicionan el diseño, carpetas y criterios de verificación.

La convención de IDs, estados, metadatos y procedencia está en `05_Gestion/convenciones/artefactos.md`. Los scripts documentales y su uso están descritos en `05_Gestion/README.md`.

Este archivo solo existe para que los usuarios de Claude Code arranquen con el mismo contexto sin duplicar contenido.

## Comandos

No hay build ni lint: el repo es documentación (`.md`, Excel, LaTeX). Las herramientas son los scripts de `05_Gestion/scripts/` (todos aceptan `--help`); el exportador LaTeX tiene pruebas en `05_Gestion/tests/`:

```bash
python3 05_Gestion/scripts/check.py        # verifica trazabilidad/convenciones de artefactos
python3 05_Gestion/scripts/estado.py       # estado de secciones por subdocumento
python3 05_Gestion/scripts/brief.py        # contexto resumido para trabajar una sección
python3 05_Gestion/scripts/agregar_frontmatter.py --dry-run
python3 05_Gestion/scripts/migrar.py --fuente <archivo> --parte T7-NN --dry-run --reporte <json>
python3 05_Gestion/scripts/exportar_latex.py doctor|estado|verificar|importar|compilar   # único camino a PDF
python3 -m unittest discover -s 05_Gestion/tests -v                                    # pruebas del exportador
python3 -m unittest discover -s 05_Gestion/tests -p test_verificar.py                 # un solo archivo de pruebas
```

- Migración: siempre `--dry-run` primero; aplicar solo con `--mapa-aprobado` revisado por humano. Nunca sobrescribe secciones existentes.
- PDF de la propuesta: cumplir la "Regla de exportación" de `AGENTS.md` y `.agents/skills/exportar/SKILL.md`. `sd-NN.tex` manda tras importar; los `.md` son solo contexto. Nunca escribir preámbulos ni llamar a `pandoc`/`xelatex` directamente.
- Estado `revisado` solo lo asigna un humano, nunca un script o agente.

## Notas para Claude Code en Linux

- `link_skills.ps1` es de Windows (junctions). En Linux, enlazar a mano con symlinks: `.agents/skills/<skill>` a `.claude/skills/<skill>`. Editar siempre `.agents/skills/`.
- Existe `.claude/settings.local.json`; `.env` (copia de `.env.example`) no se versiona.

## Skills y plugin de opencode

El skill orquestador `licitacion-workflow` y el plugin `activar-skills.ts` que viven en `.opencode/` son **específicos de opencode** (se cargan con la herramienta `skill` y se inyectan en su prompt de sistema). No aplican a Claude Code; ignóralos.

## Skills compartidas

Las skills nuevas del flujo de artefactos se mantienen versionadas en `.agents/skills/`. En Windows, ejecutar `05_Gestion/scripts/link_skills.ps1` para exponerlas a Claude Code (`.claude/skills/`) y OpenCode (`.opencode/skills/`) mediante junctions locales. No editar las copias enlazadas desde una integración: la fuente canónica está en `.agents/skills/`. Las skills preexistentes de OpenCode se conservan sin cambios.

## Diagramas

- Los diagramas de la propuesta se incrustan como imágenes PNG/PDF exportadas en `04_Adjuntos/diagramas/`. **No usar bloques Mermaid**: el importador los rechaza.
- PlantUML/UML formal: `.puml` → PNG/SVG vía Kroki (`curl https://kroki.io/plantuml/png -d 'diagram_source=...'`) o `plantuml.jar` local; importar siempre la imagen a `04_Adjuntos/diagramas/`.

Nota: cualquier duda de contenido, reglas o precedencia se resuelve en `00_Bases/` y en `AGENTS.md`, no en equivalencias de skills.
