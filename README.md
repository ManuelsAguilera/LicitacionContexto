# Licitación TFEP-01/2026 — Caso 09 Cadena Multitienda

Propuesta técnico-económica (licitación **ficticia**) para el caso 09 **"Cadena Multitienda"** (Multitiendas Ancoa S.A.). Proyecto de la Escuela de Informática PUCV — Taller de Formulación de Proyectos Informáticos (ICI-5444). Proponente: **Only Simple Solutions**.

Todo el trabajo es **documentación tipo oferta en español** (arquitectura, servicios, requerimientos, planificación, riesgos), no código.

## Estructura

| Carpeta | Contenido |
| :--- | :--- |
| `Bases/` | Documentos rectores y fuente de verdad (precedencia en `AGENTS.md`) |
| `Requerimientos/` | Planillas Excel de requerimientos (fuente oficial: catálogo depurado `RequerimientosAtomizados_Depuracion_Alcance.xlsx`) |
| `productos/` | Salidas: consultas al mandante, planilla de consultas, registro de decisiones |
| `TrabajosAnteriores/` | Subdocumentos de un caso previo (DistriProducto): referencia de **forma**, no de contenido |
| `.opencode/` | Skills y plugin de opencode para el flujo de trabajo |

## Contexto

- **`AGENTS.md`** — reglas de oro del proyecto (única fuente de verdad). Léelo primero.
- **`CLAUDE.md`** — puntero para usuarios de Claude Code + cómo instalar skills equivalentes.

## Skills de opencode

Las skills están **versionadas en `.opencode/skills/`** y quedan instaladas al clonar (no dependen de la config global de cada máquina). El skill `licitacion-workflow` orquesta qué skill cargar en cada fase de la propuesta.