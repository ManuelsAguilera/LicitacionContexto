# Plan de hoy: exportador LaTeX

**Fecha objetivo:** 3 de octubre de 2026.  
**Alcance:** terminar el exportador con los textos existentes. No incluye redactar, completar ni acreditar subdocumentos.

## Resultado comprometido para hoy

Al terminar la jornada quedará un flujo que:

1. importa Markdown a LaTeX una sola vez;
2. nunca sobrescribe un archivo `.tex` creado o editado;
3. permite editar cada `.tex` con cualquier editor de texto;
4. compila un subdocumento mediante XeLaTeX y `latexmk`;
5. incrusta figuras existentes en PDF, PNG o JPEG;
6. compila por lote todas las fuentes disponibles;
7. informa qué subdocumentos todavía no tienen fuente;
8. produce los PDF con nombres compatibles con el Comunicado 10;
9. genera el consolidado cuando existan todas las fuentes requeridas.

Pandoc solo participa en la importación inicial. Después, las ediciones finales se hacen directamente en LaTeX.

## Cronograma de hoy

| Bloque | Trabajo | Duración | Criterio de salida |
| :--- | :--- | ---: | :--- |
| 1 | Corregir y compilar localmente el piloto `sd-01.tex` | 1–1,5 h | PDF legible, texto seleccionable y página carta |
| 2 | Ajustar plantilla, portada, índice, folio, tablas e imágenes | 1,5–2 h | Una edición del `.tex` aparece en PDF sin volver a ejecutar Pandoc |
| 3 | Terminar importación y compilación por parte y por lote | 1,5–2 h | El importador impide sobrescrituras y el lote procesa las fuentes disponibles |
| 4 | Validar, medir y documentar | 1–1,5 h | Reporte de errores, duración y archivos generados |
| **Total restante** | | **5–7 h** | Exportador MVP operativo |

## Estructura mínima

    02_Propuesta/latex_final/
      oss.sty                 estilo común
      sd-01.tex ... sd-14.tex fuentes editables cuando existan
      figuras/                imágenes PDF, PNG y JPEG
      manifiesto.json         origen y estado de importaciones
      README.md               instrucciones
    05_Gestion/scripts/
      exportar_latex.py       importación y compilación
    07_Entregables/
      sobre_2_tecnico/        PDF separados
      pdf_final/              PDF consolidado

No se incorporan bloques Mermaid ni generación de diagramas. Las figuras llegan como imágenes terminadas y se insertan con `includegraphics`.

## Comandos

    python3 05_Gestion/scripts/exportar_latex.py estado
    python3 05_Gestion/scripts/exportar_latex.py importar --parte T7-01
    python3 05_Gestion/scripts/exportar_latex.py compilar --parte T7-01
    python3 05_Gestion/scripts/exportar_latex.py compilar --todo --trabajadores 4
    python3 05_Gestion/scripts/exportar_latex.py compilar --todo --final --trabajadores 4

## Rendimiento

El requisito final es exportar los 14 subdocumentos y el consolidado en menos de 60 minutos. Hoy quedarán implementados el cronómetro, el reporte y la compilación paralela. La medición definitiva requiere que existan las 14 fuentes.

Metas del MVP:

- un subdocumento ordinario en menos de 5 minutos;
- recompilación de un `.tex` en menos de 2 minutos;
- el lote compila todo lo disponible e informa las fuentes ausentes;
- con cuatro compilaciones paralelas, el lote completo permanece bajo una hora si cada parte tarda menos de 15 minutos.

## Validaciones incluidas hoy

- compilación sin errores fatales;
- PDF con páginas y texto seleccionable;
- tamaño carta;
- rutas de imágenes válidas;
- protección contra sobrescritura de LaTeX;
- nombres de salida;
- duración por documento y total;
- lista explícita de fuentes faltantes.

La revisión visual exhaustiva de los 14 documentos, los ajustes particulares de sus tablas y la verificación de contenido quedan fuera del exportador.

## Estado inicial

- Pandoc, XeLaTeX y `latexmk` están instalados.
- Ya existen un primer `sd-01.tex` y la estructura inicial de `exportar_latex.py`.
- El compilador integrado del editor falló por su entorno y por no admitir archivos auxiliares. La exportación usará `latexmk` local; los `.tex` seguirán siendo editables.
- Los demás subdocumentos se incorporarán cuando tengan una fuente disponible, sin modificar su redacción.

## Resultado de la ejecución actual

- `T7-01` se importó a `02_Propuesta/latex_final/sd-01.tex` y compiló con `latexmk` local.
- La vista previa generada tiene 9 páginas, texto seleccionable y tamaño carta; la compilación individual tardó aproximadamente 3,6 segundos.
- Una segunda importación de T7-01 fue rechazada porque el `.tex` ya existe, protegiendo las ediciones finales.
- El lote en modo vista previa produjo 1 PDF y un consolidado en aproximadamente 0,3 segundos, e informó T7-02 a T7-14 como fuentes pendientes.
- El lote en modo `--final` se detuvo correctamente por las fuentes faltantes.
- La validación del compilador integrado del editor sigue bloqueada por su error de entorno; el flujo operativo queda basado en `latexmk` local.

**Estado del MVP:** operativo para las fuentes disponibles; pendiente de incorporar las fuentes LaTeX de T7-02 a T7-14 cuando existan.

## Plan de ejecución detallado

### Fase 0 — Preflight y respaldo

Antes de compilar se ejecutará el chequeo del exportador existente para cada parte disponible. El chequeo debe mostrar las secciones encontradas, adjuntos declarados, formularios separados, estado de borrador y ausencia o presencia de Referencias y Declaración de uso de IA. Se guardará el estado inicial del manifiesto y no se eliminarán archivos intermedios del usuario.

**Salida:** reporte de preflight y lista de partes aptas, incompletas o ausentes.

### Fase 1 — Piloto T7-01

Se usará el Subdocumento 1 como caso de prueba porque contiene texto, tablas y figuras. Se corregirán únicamente problemas del exportador: paquetes, rutas, codificación, tamaño de página, portada, índice, encabezados, foliación, tablas e imágenes. No se corregirán afirmaciones, cifras ni pendientes de la rúbrica.

**Salida:** `sd-01.tex` editable y un PDF de vista previa compilado con `latexmk`.

### Fase 2 — Conversión inicial protegida

El comando `importar` se ejecutará solo para partes que aún no tengan `.tex`. Cada importación registrará en `manifiesto.json` la fuente de origen, su hash, fecha, figuras copiadas y nombre del `.tex`. Si el `.tex` ya existe, el comando se detendrá sin modificarlo.

**Salida:** una fuente LaTeX por parte disponible y un registro de procedencia.

### Fase 3 — Compilación individual

Cada fuente se compilará en un directorio de trabajo separado. El PDF se copiará al directorio de vista previa o al directorio oficial según el modo solicitado. Los errores quedarán en el log de LaTeX y se resumirán en el reporte; un error en una parte no ocultará el resultado de las demás.

**Salida:** PDF y tiempo de compilación por parte.

### Fase 4 — Compilación por lote

El modo `--todo` recorrerá las 14 partes en orden lógico, ejecutará compilaciones independientes en paralelo y generará un reporte JSON. Si faltan fuentes, el lote podrá operar en modo vista previa y reportará las faltantes; el modo `--final` se detendrá antes de publicar si no están todas las partes exigidas.

Después de los PDF individuales, se generará el consolidado con marcadores por subdocumento. El consolidado es una copia de lectura; la entrega oficial conserva los PDF separados.

**Salida:** PDF individuales, PDF consolidado y `ultimo-reporte.json`.

### Fase 5 — Validación de salida

El reporte comprobará:

- código de salida de LaTeX;
- existencia y nombre de cada PDF;
- texto seleccionable;
- tamaño carta u oficio configurado;
- presencia de fuentes incrustadas;
- imágenes encontradas y legibles por el compilador;
- ausencia de marcadores `TODO` o `[VERIFICAR]` en modo final;
- índice y enlaces internos generados;
- duración individual, duración total y número de trabajadores;
- partes omitidas y causa de omisión.

La validación automática no certifica la exactitud del contenido ni sustituye la revisión humana.

## Estados del exportador

| Estado | Significado | Puede generar PDF |
| :--- | :--- | :--- |
| `pendiente` | No existe fuente `.tex` | No |
| `importable` | Existe fuente Markdown y no existe `.tex` | Tras importar |
| `editable` | Existe `.tex` protegido contra regeneración | Sí, como vista previa |
| `compilable` | La última compilación terminó sin error | Sí |
| `finalizable` | Cumple referencias, IA, adjuntos y validaciones finales | Sí, modo final |
| `error` | La última compilación falló | No hasta corregir el `.tex` |

## Criterios de aceptación del MVP

El exportador de hoy se considerará terminado cuando cumpla todo lo siguiente con T7-01:

1. `estado` muestra correctamente la parte disponible y las ausentes.
2. `importar --parte T7-01` crea el `.tex` y su manifiesto.
3. Una segunda ejecución de importación no sobrescribe el `.tex`.
4. Una edición manual del `.tex` aparece en el PDF sin importar nuevamente Markdown.
5. Las dos figuras del Subdocumento 1 se insertan como imágenes.
6. `compilar --parte T7-01` valida PDF, texto seleccionable y tamaño de página.
7. `compilar --todo` termina con un reporte aunque falten partes.
8. `compilar --todo --final` rechaza claramente una entrega incompleta.

El objetivo de menos de una hora para los 14 documentos es un criterio de rendimiento posterior, medible cuando existan las 14 fuentes. No se marcará como cumplido por extrapolación desde T7-01.

## Fuera de alcance

- Redacción, corrección técnica o revisión de la rúbrica.
- Creación o sustitución de figuras que no existan como archivos de imagen.
- Conversión automática de DOCX/XLSX a formularios dentro del subdocumento.
- Publicación en Google Docs o en una plataforma externa.
- Firma digital, envío del ZIP o presentación administrativa.
- Corrección de contenido para forzar que un documento pase el modo final.

## Riesgos y respuestas

| Riesgo | Impacto | Respuesta del plan |
| :--- | :--- | :--- |
| El compilador integrado del editor no soporta el proyecto | No hay previsualización nativa | Usar `latexmk` local y mantener los `.tex` abiertos en el editor para edición |
| Falta una figura o tiene un formato no admitido | Compilación detenida | Informar la ruta exacta; aceptar PDF, PNG y JPEG |
| Un `.tex` ya fue editado | Pérdida de trabajo | No permitir importación automática; integrar cambios manualmente |
| Faltan partes del T-7 | No se puede generar el consolidado final | Compilar disponibles en vista previa y enumerar faltantes |
| Una tabla excede el ancho de página | PDF ilegible | Registrar el error para ajuste de plantilla; no cambiar el contenido |
| El lote excede 60 minutos | Incumplimiento de rendimiento | Usar compilación paralela, caché de figuras y recompilación incremental |

## Handoff de uso

Al cerrar el MVP se entregarán:

- [README de LaTeX](/workspace/LicitacionContexto/02_Propuesta/latex_final/README.md);
- [script del exportador](/workspace/LicitacionContexto/05_Gestion/scripts/exportar_latex.py);
- estilo común `oss.sty`;
- manifiesto de procedencia;
- reporte de la última ejecución;
- PDF de vista previa generado y logs de errores, si los hubiera.

La operación normal será: editar el `.tex`, ejecutar la compilación de la parte, revisar el PDF y luego incluir la parte en el lote. No se volverá a ejecutar `importar` sobre una parte que ya tenga un `.tex` editable.
