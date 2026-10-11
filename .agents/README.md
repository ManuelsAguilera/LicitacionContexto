# Skills compartidas del proyecto

La fuente versionada de las skills de flujo de artefactos vive en `.agents/skills/`. Las integraciones de agente enlazan o referencian estas instrucciones; las skills nativas preexistentes de `.opencode/skills/` se conservan.

## Revisor de calidad

Instrucciones canónicas: [revisor-calidad/SKILL.md](skills/revisor-calidad/SKILL.md). Material docente, investigación y guía de uso: [calidad](../90_Referencia/calidad/README.md). Para Claude existe el wrapper [revisor-calidad](../.claude/agents/revisor-calidad.md).

Invocación sugerida: «Aplica la skill revisor-calidad a `80_Artefactos/sd-09_contexto/`; revisa el diseño de la matriz y entrega hallazgos con fuentes y condiciones de cierre». La revisión no registra aceptación humana ni ejecuta pruebas del producto.

## Citas de la propuesta

Instrucciones canónicas: [citas-proyecto/SKILL.md](skills/citas-proyecto/SKILL.md). Su índice y OCR paginado están en [90_Referencia](../90_Referencia/indice_paginas_caso09.md). Activar al redactar o revisar citas y Referencias de cualquier subdocumento.
