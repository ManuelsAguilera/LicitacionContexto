# Licitación TFEP-01/2026 — Caso 09 Cadena Multitienda

Propuesta técnico-económica (licitación **ficticia**) para el caso 09 **"Cadena Multitienda"** (Multitiendas Ancoa S.A.). Proyecto de la Escuela de Informática PUCV — Taller de Formulación de Productos Informáticos (ICI-5444). Proponente: **Only Simple Solutions**.

Todo el trabajo es **documentación tipo oferta en español** (arquitectura, servicios, requerimientos, planificación, riesgos), no código.

## Estructura

Pipeline numerado: el prefijo declara la etapa del flujo.

| Carpeta | Contenido |
| :--- | :--- |
| `00_Bases/` | Documentos rectores y fuente de verdad (precedencia en `AGENTS.md`) |
| `01_Requerimientos/` | Catálogos de requerimientos en Excel (oficial: catálogo v3.0 depurado) + espejos `.md` |
| `02_Propuesta/` | **La propuesta**: los 14 subdocumentos del Formulario T-7, una carpeta por subdocumento |
| `03_Formularios/` | Formularios oficiales de los sobres: A-1..A-6, T-6..T-22, E-21..E-26 |
| `04_Adjuntos/` | Diagramas exportados, inventario de hardware, tablas de apoyo |
| `05_Gestion/` | Plan de trabajo en Jira (`OSS`): plan, mapeo, scripts |
| `06_Informes/` | Los 3 informes y las 3 presentaciones preparatorias (Art. 45°) |
| `07_Entregables/` | Salida final: los 3 sobres y el PDF |
| `80_Artefactos/` | Material general: planilla de consultas al mandante, informes internos |
| `90_Referencia/` | Fragmentos de un caso previo (DistriProducto): **solo referencia de forma** |
| `.opencode/` | Skills y plugin de opencode para el flujo de trabajo |

Cada carpeta tiene su `README.md` con el propósito y las reglas específicas.

## Contexto

- **`AGENTS.md`** — reglas de oro del proyecto (única fuente de verdad). Léelo primero.
- **`02_Propuesta/indice.md`** — índice de los 14 subdocumentos, cobertura por informe y reglas de ensamblado.
- **`CLAUDE.md`** — puntero para usuarios de Claude Code + cómo instalar skills equivalentes.

## Convenciones

- **Formato:** todo artefacto de contenido se escribe en `.md` (o `.txt`). Los binarios (`.xlsx`, `.docx`, `.pptx`, `.pdf`) solo existen como documento de lectura/entrega para el usuario o como export final.
- **Nombres:** `sd-NN_sN_titulo.md` para el texto, `adj-`/`diag-`/`form-` para los adjuntos. El orden alfabético coincide con el orden del informe.

## Skills de opencode

Las skills están **versionadas en `.opencode/skills/`** y quedan instaladas al clonar (no dependen de la config global de cada máquina). El skill `licitacion-workflow` orquesta qué skill cargar en cada fase de la propuesta.

## MCP configurados

| Servidor | Estado | Para qué |
| :--- | :--- | :--- |
| `jira` | Activo en esta máquina | Gestionar el plan de trabajo del proyecto `OSS` |
| `ragdocs` | `enabled: false` | Búsqueda por significado sobre `00_Bases/`, espejos de requerimientos y `02_Propuesta/` (Qdrant Cloud) |

Ambos son opcionales: quien clone el repo sin cuentas ni claves sigue pudiendo trabajar con normalidad. Ver la sección correspondiente de `AGENTS.md`.
