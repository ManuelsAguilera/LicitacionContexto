# Instalación MCP en este repositorio

El paquete original procede de `diagramas-ancoa.zip`, SHA-256
`48284c707c071c2a13344fafb475c7d26803ee8709415e32252cfe6ce5f859f0`.
Se instaló en `.agents/skills/diagramas-ancoa/`, la fuente canónica de skills del proyecto.
La adaptación agrega `scripts/mcp_servidor.py`, su prueba y las dependencias fijadas.
No cambia los estilos ni convierte los ejemplos del ZIP en requisitos de la propuesta.

## Uso

El MCP `diagramas-ancoa` está registrado en Codex en esta máquina. Una nueva sesión o un reinicio
de la conexión carga las herramientas. La sesión que hizo la instalación lo probó mediante un cliente
MCP stdio y también en memoria; registrarlo no incorpora herramientas nuevas retroactivamente a ese turno.

- `catalogo_diagramas()` devuelve el catálogo completo.
- `validar_diagrama(especificacion)` comprueba el JSON sin escribir archivos.
- `renderizar_diagrama(especificacion, salida)` valida y genera L → PNG/SVG/leyenda o F → drawio/leyenda.

`salida` es una ruta relativa al repositorio, sin extensión. Se admite
`04_Adjuntos/diagramas/<nombre>` y `tmp/diagramas-ancoa/<nombre>`, con subcarpetas.
La herramienta conserva el JSON, rechaza rutas fuera de esos destinos y no reemplaza archivos existentes.
Si hay avisos, deben evaluarse aunque el archivo se haya generado. El MCP no exporta la propuesta a PDF.

## Reinstalación en Windows

Desde la raíz, con Python 3.12 o compatible, Graphviz y uv disponibles:

```powershell
uv venv --python 3.12 05_Gestion/build/diagramas-ancoa/venv
uv pip install --python 05_Gestion/build/diagramas-ancoa/venv/Scripts/python.exe -r .agents/skills/diagramas-ancoa/scripts/requirements.txt
05_Gestion/build/diagramas-ancoa/venv/Scripts/python.exe .agents/skills/diagramas-ancoa/scripts/probar_harness.py
05_Gestion/build/diagramas-ancoa/venv/Scripts/python.exe .agents/skills/diagramas-ancoa/scripts/probar_mcp.py
```

El entorno de `05_Gestion/build/` está ignorado por Git y se recrea en cada máquina. Registrar después
el MCP con rutas absolutas de esa máquina, siguiendo la [configuración oficial de Codex](https://learn.chatgpt.com/docs/extend/mcp):

```powershell
codex mcp add diagramas-ancoa -- <python-absoluto-del-entorno> <ruta-absoluta-a-scripts/mcp_servidor.py>
codex mcp get diagramas-ancoa
```

La vista previa opcional de draw.io requiere además instalar Chromium de Playwright:
`05_Gestion/build/diagramas-ancoa/venv/Scripts/python.exe -m playwright install chromium`.
La instalación inicial verificó el render físico a `.drawio`; no instaló ni validó esa vista previa opcional.
Para entrega final se conserva el flujo de exportación descrito en la skill y en las reglas del proyecto.

## Verificación

`probar_harness.py` comprueba cinco ejemplos válidos y dieciocho casos que deben rechazarse.
`probar_mcp.py` abre una sesión stdio, genera un ejemplo de cada familia y comprueba el rechazo
de un cruce prohibido, rutas ajenas y sobrescritura. Deja sus muestras en una subcarpeta única de
`tmp/diagramas-ancoa/`. Los ejemplos son pruebas de la herramienta, no propuestas aprobadas.
