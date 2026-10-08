# Contexto de trabajo del sd-03

Material de apoyo para redactar y revisar el sd-03 (Esquema de solución y alcance). No es entregable. Manda siempre `02_Propuesta/latex_final/sd-03.tex`.

**Para cargar en un agente, empezar por `ficha_alcance_sd-03.md`** (resumen vigente, 2.000 palabras aprox.). Los demás archivos se abren solo cuando la tarea los necesita.

| Archivo | Estado | Para qué sirve |
| :-- | :-- | :-- |
| `ficha_alcance_sd-03.md` | Vigente | Resumen del alcance, decisiones, cifras y pendientes. Punto de entrada |
| `divisiones_negocio_servicios_sd-03.md` | Vigente | Nomenclatura de frentes, áreas y servicios, y tabla de equivalencias con los códigos antiguos |
| `conciliacion_catalogo.md` | Vigente | Decisiones sobre el catálogo de requerimientos y cambios que el equipo debe trasladar al Excel oficial |
| `condiciones_caso_13_3.md` | Vigente | Las diez condiciones del Caso 13.3 y su cobertura |
| `fundamentacion_credito_sin_conexion.md` | Vigente | Fundamento del crédito sin conexión (EXC-16, SP-03, RC-11) |
| `auditoria_decisiones.md` | Consulta puntual | Historial de decisiones con su puntaje. Parte está superada |
| `insumos_3.3_3.4.md` | Para el integrante a cargo de 3.3 y 3.4 | Usa códigos antiguos. Verificar contra el `.tex` y los anexos |
| `historico/no_usar_*.md` | Archivado | Planes y borradores ejecutados o superados. No usar como fuente |

## Mantenimiento

- Si cambia una decisión, se actualiza primero el `.tex` o el anexo y después la ficha.
- Antes de cada sesión del equipo, correr `python3 05_Gestion/scripts/desfase_contexto.py` para detectar códigos y términos descartados en los archivos vigentes.
