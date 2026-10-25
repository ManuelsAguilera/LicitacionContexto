---
name: redactar-seccion
description: Redactar una sección concreta de la propuesta con contexto, trazabilidad y verificación local.
---

# Redactar una sección

1. Lee `AGENTS.md`, `05_Gestion/convenciones/artefactos.md` y las reglas de redacción `05_Gestion/convenciones/reglas-redaccion.md` (RR-NN, basadas en el Comunicado 10). Las reglas de formato están aparte (`reglas-plantilla.md`) y las cumple la plantilla.
2. Lee solo las decisiones pertinentes de `80_Artefactos/contexto-activo/indice.md`. Ejecuta `python 05_Gestion/scripts/brief.py <ID>` y confirma la ruta y el hash de la fuente actual. SD-04 es referencia de arquitectura y SD-07 de planificación, subordinados a las Bases. Si la sección no se identifica inequívocamente, usa el aviso para localizarla en la fuente principal; no copies Markdown anterior.
3. Escribe únicamente esa sección en su fuente vigente; conserva los títulos obligatorios y no inventes datos. Aplica `.agents/skills/citas-proyecto/SKILL.md` a las citas y Referencias.
4. Pasa el texto redactado por la skill `humanizer` con las restricciones de RR-24: solo quita patrones de IA, sin primera persona ni opiniones, registro formal, sin tocar cifras, IDs, nombres de componentes, citas ni títulos. Revisa el diff antes de seguir.
5. Registra procedencia, requisitos y uso de IA real en frontmatter/declaración, sin afirmar revisiones humanas no realizadas. Declara el uso de `humanizer`.
6. Ejecuta `python 05_Gestion/scripts/check.py --parte T7-NN` como control de metadatos y trazabilidad Markdown. Para LaTeX usa además `exportar_latex.py verificar --parte T7-NN`; ninguno acredita consistencia ni revisión humana. Entrega errores y pendientes sin cambiar estado a `revisado`.
