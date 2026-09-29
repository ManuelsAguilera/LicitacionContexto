# CLAUDE.md

## Cómo usar este archivo

El contexto completo del proyecto está en **`AGENTS.md`** (única fuente de verdad). Léelo antes de trabajar: identidad del proponente (Only Simple Solutions), fuentes y precedencia de `00_Bases/`, reglas que condicionan el diseño, carpetas y criterios de verificación.

Este archivo solo existe para que los usuarios de Claude Code arranquen con el mismo contexto sin duplicar contenido.

## Skills y plugin de opencode

El skill orquestador `licitacion-workflow` y el plugin `activar-skills.ts` que viven en `.opencode/` son **específicos de opencode** (se cargan con la herramienta `skill` y se inyectan en su prompt de sistema). No aplican a Claude Code; ignóralos.

## Cómo instalar skills equivalentes en Claude Code

Si necesitas helpers similares (Excel, Word, PowerPoint, PDF, diagramas, riesgos, estimación), Claude Code ofrece **Agent Skills** del mismo formato (`SKILL.md` con frontmatter `name`/`description`), que se buscan e instalan por repositorio en `.claude/skills/`.

1. En el config de Claude Code: busca skills/repos de skills (marketplace) o agrega `.claude/skills/<nombre>/SKILL.md` al proyecto local.
2. Instala solo los que uses; no se versionan aquí para evitar duplicación y confusión entre herramientas.
3. Ejemplos útiles para esta propuesta: manejo de `.xlsx`, `.docx`, `.pptx`, manejo de PDF, evaluación de riesgos y redacción técnica.

## Diagramas

- **Mermaid**: escribir bloques ```mermaid``` en los `.md`; la UI de Claude Code y GitHub los renderizan nativo (misma convención que en `AGENTS.md` → "Renderizado de diagramas").
- **PlantUML/UML formal**: `.puml` → PNG/SVG vía Kroki (`curl https://kroki.io/plantuml/png -d 'diagram_source=...'`), o kroki-docker/`plantuml.jar` local. GitHub no lo renderiza: importa siempre la imagen a `04_Adjuntos/diagramas/`.
- Los exports van a `04_Adjuntos/diagramas/` para incrustar en `.docx`/PDF, igual que en opencode.

Nota: cualquier duda de contenido, reglas o precedencia se resuelve en `00_Bases/` y en `AGENTS.md`, no en equivalencias de skills.