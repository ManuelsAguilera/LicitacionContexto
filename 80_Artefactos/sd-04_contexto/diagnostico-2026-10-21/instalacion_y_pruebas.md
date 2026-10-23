# Instalación de la guía y verificaciones

Fecha local 2026-10-21. Paquete de origen `C:\Users\manu\Downloads\diagramas-ancoa.zip`.
SHA-256 `48284c707c071c2a13344fafb475c7d26803ee8709415e32252cfe6ce5f859f0`.

Se instalaron los 63 archivos del ZIP en `.agents/skills/diagramas-ancoa/`, después de comprobar que sus rutas no escapaban del destino ni incluían enlaces simbólicos. La adaptación local agrega un servidor MCP, una prueba de integración, las versiones de dependencias y una referencia de instalación. El contenido del catálogo se conserva.

El servidor `diagramas-ancoa` quedó registrado y habilitado en la configuración de Codex de esta máquina. El ejecutable es `05_Gestion/build/diagramas-ancoa/venv/Scripts/python.exe` y ejecuta `.agents/skills/diagramas-ancoa/scripts/mcp_servidor.py`, con rutas absolutas. El entorno es local y está ignorado por Git. La guía de reinstalación está en `.agents/skills/diagramas-ancoa/references/instalacion-mcp.md`. Una nueva sesión o reinicio de la conexión permite cargar el registro en la interfaz del cliente.

El servidor expone catálogo, validación y renderizado. Acepta JSON y llama a los renderizadores del paquete después de validar. No necesita que el cliente le envíe Python libre. La salida queda dentro de `04_Adjuntos/diagramas/` o `tmp/diagramas-ancoa/`, y se rechazan sobrescrituras.

| Verificación | Resultado |
|---|---|
| Autoprueba del paquete | 5 ejemplos válidos y 18 casos de rechazo correctos; `TODO EN ORDEN`. |
| Validación de skill | `Skill is valid!`. |
| Sesión MCP stdio | Inicialización y descubrimiento de las tres herramientas correctos. |
| Render lógico por MCP | PNG, SVG, leyenda y JSON generados; imagen de prueba inspeccionada. |
| Render físico por MCP | `.drawio`, leyenda y JSON generados. |
| Cruce Retail–Emisor inválido | Rechazado antes de escribir archivos. |
| Ruta fuera del destino | Rechazada. |
| Sobrescritura | Rechazada. |
| Registro en Codex | `codex mcp get diagramas-ancoa` confirma `enabled: true`, transporte stdio y las rutas esperadas. |
| Actualización de Graphify | `graphify update .` completado para los scripts. No se utilizó como prueba del contenido documental. |

La versión inicial del adaptador invocaba el renderizador mediante un subproceso adicional y falló en la prueba stdio de Windows. La versión final llama a las funciones de renderizado directamente; la prueba stdio completa pasó después de ese cambio. Las pruebas finales pueden repetirse con `scripts/probar_harness.py` y `scripts/probar_mcp.py` usando el Python del entorno.

Playwright está instalado. La vista previa física opcional requiere Chromium y no se verificó en esta tarea; el resultado físico comprobado es el archivo editable `.drawio`. No se compilaron subdocumentos, no se reemplazaron diagramas de la oferta y no se hicieron cambios al contenido de los `.tex`.

La guía y los artefactos se agregaron al árbol de `work`. `main` permanece en `1e097c2` y no se hizo commit, merge ni push. Los cambios locales anteriores se conservaron.
