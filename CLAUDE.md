# CLAUDE.md

## Cómo usar este archivo

El contexto completo del proyecto está en **`AGENTS.md`** (única fuente de verdad). Léelo antes de trabajar: identidad del proponente (Only Simple Solutions), fuentes y precedencia de `00_Bases/`, reglas que condicionan el diseño, carpetas y criterios de verificación.

La convención de IDs, estados, metadatos y procedencia está en `05_Gestion/convenciones/artefactos.md`. Los scripts documentales y su uso están descritos en `05_Gestion/README.md`.

Este archivo solo existe para que los usuarios de Claude Code arranquen con el mismo contexto sin duplicar contenido.

## Skills y plugin de opencode

El skill orquestador `licitacion-workflow` y el plugin `activar-skills.ts` que viven en `.opencode/` son **específicos de opencode** (se cargan con la herramienta `skill` y se inyectan en su prompt de sistema). No aplican a Claude Code; ignóralos.

## Skills compartidas

Las skills nuevas del flujo de artefactos se mantienen versionadas en `.agents/skills/`. En Windows, ejecutar `05_Gestion/scripts/link_skills.ps1` para exponerlas a Claude Code (`.claude/skills/`) y OpenCode (`.opencode/skills/`) mediante junctions locales. No editar las copias enlazadas desde una integración: la fuente canónica está en `.agents/skills/`. Las skills preexistentes de OpenCode se conservan sin cambios.

## Diagramas

- **Mermaid**: escribir bloques ```mermaid``` en los `.md`; la UI de Claude Code y GitHub los renderizan nativo (misma convención que en `AGENTS.md` → "Renderizado de diagramas").
- **PlantUML/UML formal**: `.puml` → PNG/SVG vía Kroki (`curl https://kroki.io/plantuml/png -d 'diagram_source=...'`), o kroki-docker/`plantuml.jar` local. GitHub no lo renderiza: importa siempre la imagen a `04_Adjuntos/diagramas/`.
- Los exports van a `04_Adjuntos/diagramas/` para incrustar en `.docx`/PDF, igual que en opencode.

Nota: cualquier duda de contenido, reglas o precedencia se resuelve en `00_Bases/` y en `AGENTS.md`, no en equivalencias de skills.
