# Convención de artefactos verificables

## Identificadores

- Parte del Formulario T-7: `T7-NN` (dos dígitos; por ejemplo `T7-03`).
- Sección: `T7-NN-x.y` usando la numeración obligatoria del Comunicado 10.
- Secciones finales no numeradas: `T7-NN-REF` (Referencias) y `T7-NN-IA` (Declaración de uso de IA); la declaración se construye desde `05_Gestion/ia/registro.json`.
- Adjunto: `ADJ-NNN`, correlativo y estable; el mismo ID se conserva si cambia el nombre del archivo.
- Requisito: ID oficial existente en el espejo v3.0 (RF, RNF u OP). No se crean equivalencias por inferencia.
- Jira: clave existente `OSS-NNN`; consultar únicamente `05_Gestion/jira/mapeo/` vigente.

## Estados

`vacio` (sin contenido sustantivo), `esqueleto` (estructura/títulos), `borrador` (contenido en elaboración), `revisado` (revisión humana registrada) y `congelado` (aprobación explícita para una entrega). Los scripts pueden asignar `vacio`, `esqueleto` o `borrador`; nunca suben un artefacto a `revisado` o `congelado`.

## Frontmatter

Usar YAML acotado a listas escalares y valores de texto para que los scripts de la librería estándar puedan leerlo sin dependencias:

```yaml
---
id: T7-03-3.1
tipo: seccion
parte: T7-03
titulo: Resumen Ejecutivo de la Solución
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos: []
jira: []
cifras: []
origen: ""
actualizado: 2026-09-29
---
```

En maestros, `tipo: parte`, `id: T7-NN` y `secciones: [T7-NN-x.y, ...]` en orden oficial. `adjuntos` contiene IDs ADJ declarados; el maestro debe mantener también el nombre del archivo para humanos.

La procedencia se expresa como ruta relativa más título/encabezado o rango identificable del origen. No copiar contenido de otro documento sin conservar esa referencia.

## Tablas en el cuerpo de un subdocumento

Qué tablas son aceptables lo deciden las [reglas de redacción](reglas-redaccion.md) (RR-15 a RR-19, del Comunicado 10 §5), que prevalecen: una tabla puede incumplir RR-16 (celdas con más de una frase) o RR-17 (más de cinco columnas) y debe corregirse al redactar, con criterio humano. El formato de las tablas lo define la [plantilla](reglas-plantilla.md). Una tabla se convierte a párrafos solo si es extensa, no compara dimensiones y el texto resultante es más corto y comprensible.

## Declaración de uso de IA

Al final del subdocumento, tras Referencias, insertar `Declaración de uso de IA` con una fila por sección, anexo y formulario asociado. Campos: herramienta, finalidad, nivel de texto, nivel de diagramas y revisión humana (persona y comprobaciones). Escala: Ninguno, Bajo, Medio, Alto conforme al Comunicado 10. No rellenar una revisión humana que no ocurrió. Consolidar las declaraciones en A-6 al preparar ese formulario.

## Fuente de estructura oficial

El Comunicado 10 determina títulos, orden y separación de archivos. Los maestros deben reproducir sus capítulos y títulos tal cual. El contenido se redacta directamente en el `.tex` de `02_Propuesta/latex_final/` (edición colaborativa con Prism); no hay importación desde Google Docs ni DOCX.
