---
name: redactar-seccion
description: Redactar una sección concreta de la propuesta con contexto, trazabilidad y verificación local.
---

# Redactar una sección

1. Lee `AGENTS.md` y `05_Gestion/convenciones/artefactos.md`.
2. Ejecuta `python 05_Gestion/scripts/brief.py <ID>` y confirma que el paquete corresponde a la sección solicitada.
3. Escribe únicamente esa sección en su archivo Markdown; conserva los títulos obligatorios y no inventes datos.
4. Registra procedencia, requisitos y uso de IA real en frontmatter/declaración, sin afirmar revisiones humanas no realizadas.
5. Ejecuta `python 05_Gestion/scripts/check.py --parte T7-NN`; entrega errores y pendientes sin cambiar estado a `revisado`.
