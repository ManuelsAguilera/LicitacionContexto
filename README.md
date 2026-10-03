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

## Exportación LaTeX editable

La fuente de redacción continúa en Markdown. Para la edición final existe una copia LaTeX editable en `02_Propuesta/latex_final/`, generada por `05_Gestion/scripts/exportar_latex.py`. El formato común de `oss.sty` se aplica a todos los subdocumentos importados: portada geométrica con la foto de alianza, tarjetas con borde y sombra, marca de agua, logo azul en el pie y página final azul con logo blanco.

Desde la raíz:

```bash
python3 05_Gestion/scripts/exportar_latex.py importar --parte T7-01
python3 05_Gestion/scripts/exportar_latex.py compilar --parte T7-01
python3 05_Gestion/scripts/exportar_latex.py compilar --todo --final --trabajadores 4
```

La importación se realiza una sola vez por subdocumento y no sobrescribe un `.tex` existente. Después de importar, las ediciones finales se hacen en el `.tex`; las figuras se incrustan como imágenes y no se usan bloques Mermaid.

Para la vista previa con el formato oficial corporativo se debe usar `exportar_latex.py`. El script `05_Gestion/scripts/build.py` corresponde al flujo Markdown anterior y produce una maqueta académica; no debe usarse para validar la portada ni el formato final LaTeX.

## Skills de opencode

Las skills están **versionadas en `.opencode/skills/`** y quedan instaladas al clonar (no dependen de la config global de cada máquina). El skill `licitacion-workflow` orquesta qué skill cargar en cada fase de la propuesta.

## MCP configurados

| Servidor | Estado | Para qué |
| :--- | :--- | :--- |
| `jira` | Activo en esta máquina | Gestionar el plan de trabajo del proyecto `OSS` |
| `ragdocs` | `enabled: false` | Búsqueda por significado sobre `00_Bases/`, espejos de requerimientos y `02_Propuesta/` (Qdrant Cloud) |

## Graphify MCP local (Claude Code y Codex)

El archivo `.mcp.json` registra Graphify como servidor MCP local para Claude Code. Requiere `uv` y un grafo generado en `graphify-out/graph.json`:

```bash
uv tool install "graphifyy[mcp,office,pdf]"
```

Después, desde Claude Code en la raíz del repositorio, instala la skill del proyecto y genera el grafo:

```bash
graphify install --project --platform claude
```

Luego ejecuta `/graphify .` en Claude Code y acepta el permiso de conexión a Graphify cuando lo solicite. La configuración usa `uvx` para iniciar el servidor MCP, así que cada máquina debe tener `uv`; el primer inicio descarga el paquete `graphifyy[mcp]`. Graphify mantiene el grafo local en `graphify-out/`, carpeta ignorada por Git.

**Privacidad:** Graphify procesa código localmente, pero la extracción semántica de Markdown, Word, Excel y PDF puede usar el modelo disponible en Claude Code. Revisa la configuración de extracción y excluye los archivos que no deban enviarse antes de generar el grafo. El MCP solo tendrá un grafo útil después de completar esa generación.

### Codex

En esta máquina se instaló Graphify con `uv`, la skill se instaló para el usuario y el MCP se registró en la configuración de Codex. `.mcp.json` configura Claude Code; Codex necesita su propio registro.

Para preparar otra máquina, desde la raíz del repositorio:

```bash
uv tool install "graphifyy[mcp,office,pdf]"
graphify install --platform codex
codex mcp add graphify -- graphify-mcp "$(pwd)/graphify-out/graph.json"
```

Reinicia Codex para cargar la skill y el servidor. Luego pide `$graphify .` para generar el grafo o `$graphify . --update` para actualizar los documentos modificados. El registro MCP apunta a una ruta absoluta: si mueves el repositorio o cambias de worktree, actualiza el registro para que consulte el grafo de la nueva carpeta. La configuración de usuario y el grafo se mantienen por máquina.

Ambos son opcionales: quien clone el repo sin cuentas ni claves sigue pudiendo trabajar con normalidad. Ver la sección correspondiente de `AGENTS.md`.
