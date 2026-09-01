# CLAUDE.md

## Cómo usar este archivo

El contexto completo del proyecto está en **`AGENTS.md`** (única fuente de verdad). Léelo antes de trabajar: identidad del proponente (Only Simple Solutions), fuentes y precedencia de `Bases/`, reglas que condicionan el diseño, carpetas y criterios de verificación.

Este archivo solo existe para que los usuarios de Claude Code arranquen con el mismo contexto sin duplicar contenido.

## Skills y plugin de opencode

El skill orquestador `licitacion-workflow` y el plugin `activar-skills.ts` que viven en `.opencode/` son **específicos de opencode** (se cargan con la herramienta `skill` y se inyectan en su prompt de sistema). No aplican a Claude Code; ignóralos.

## Cómo instalar skills equivalentes en Claude Code

Si necesitas helpers similares (Excel, Word, PowerPoint, PDF, diagramas, riesgos, estimación), Claude Code ofrece **Agent Skills** del mismo formato (`SKILL.md` con frontmatter `name`/`description`), que se buscan e instalan por repositorio en `.claude/skills/`.

1. En el config de Claude Code: busca skills/repos de skills (marketplace) o agrega `.claude/skills/<nombre>/SKILL.md` al proyecto local.
2. Instala solo los que uses; no se versionan aquí para evitar duplicación y confusión entre herramientas.
3. Ejemplos útiles para esta propuesta: manejo de `.xlsx`, `.docx`, `.pptx`, manejo de PDF, evaluación de riesgos y redacción técnica.

Nota: cualquier duda de contenido, reglas o precedencia se resuelve en `Bases/` y en `AGENTS.md`, no en equivalencias de skills.