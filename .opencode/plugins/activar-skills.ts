import type { Plugin } from "@opencode-ai/plugin"

const SKILL_ACTIVATION_GUIDE = `
## Activación proactiva de skills (proyecto licitación TFEP-01/2026)

Este proyecto produce una propuesta técnico-económica documental (no código). Para cada fase, carga la skill indicada con la herramienta \`skill\` ANTES de ejecutar la tarea, sin esperar a que el usuario lo pida:

- Arquitectura (vistas lógica/física/datos/seguridad/despliegue): \`architecture-diagrams\`, \`cloud-architecture\`, \`sre-practices\`
- Requerimientos / volumetría / oferta económica (Excel): \`xlsx\`
- Estimación de esfuerzo y roles: \`project-estimation\` (+ \`xlsx\`)
- Riesgos contractuales y técnicos: \`legal-risk-assessment\`, \`risk-assessment\`
- Oferta económica y flujo de caja: \`project-estimation\`, \`xlsx\`
- Formularios/plantillas oficiales (.docx): \`docx\`
- Presentaciones preparatorias (Sobres): \`pptx\`
- Investigación (lo que el caso no explica): \`deep-research\`
- Redacción de documentos técnicos: \`technical-writing\`
- Entrega final / exportación (md a LaTeX corporativo y PDF): skill \`exportar\` y solo \`05_Gestion/scripts/exportar_latex.py\` (ver "Regla de exportación" en AGENTS.md)

Nota: las skills se cargan por decisión del modelo vía la herramienta \`skill\`; este bloque refuerza cuándo hacerlo. Carga también el skill \`licitacion-workflow\` al iniciar cualquier avance de la propuesta.
`.trim()

export const ActivarSkillsPlugin: Plugin = async () => {
  return {
    "experimental.chat.system.transform": async (_input, output) => {
      output.system.push(SKILL_ACTIVATION_GUIDE)
    },
  }
}
