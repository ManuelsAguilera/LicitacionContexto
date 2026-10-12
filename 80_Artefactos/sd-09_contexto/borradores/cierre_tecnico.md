---
tipo: registro-tecnico
parte: T7-09
estado: comprobado-por-agentes
actualizado: 2026-10-11
---
# Cierre técnico de la reescritura SD09

Este registro corresponde a la versión intermedia de 15 páginas. La ampliación posterior de 23 páginas y su verificación constan en [`cierre_ampliacion_2026-10-11.md`](../cierre_ampliacion_2026-10-11.md).

La fuente consolidada es `02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex`. La vista auxiliar `preview_consolidado.md` se deriva del cuerpo y no constituye una segunda fuente. Se conservó el preámbulo corporativo y la portada. La vista previa compilada es `05_Gestion/reportes/vistas_previas/T7-09_latex_preview.pdf`, de 15 páginas carta y texto seleccionable.

## Cambios materiales

Se desarrollaron introducción y secciones 9.1–9.3, con ocho títulos contractuales y relación con las nueve características ISO/IEC 25010:2023, QA/QC, marco CMMI v3.0 sin rating, responsables, métricas, COQ, pruebas 29119, trazabilidad y calendario. Se mantienen ≥70% cobertura bloqueante de lógica de negocio, ≥80% objetivo separado de código nuevo, deuda≤5% y duplicación≤3%. Complejidad≤15 por función nueva/modificada y cero ciclos entre servicios son políticas iniciales propuestas con medición, justificación y calibración, sin atribución a Bases/ISO.

H03 se resuelve en duplicación con unidad/población/exclusiones y decisión de bloqueo; H04 en configuración y ensayo de rotación automática, consumidores, revocación y auditoría; H05 en umbrales de desempeño bajo 1,5× peak, separados del estrés hasta quiebre. H01/H02 conservan resultados y procedencia correcta, sin debate editorial en la oferta.

Durante la revisión se corrigieron RT-13.05 tres interacciones, objetivos iniciales propuestos de error/aprendizaje, RT-05.04 captura/tablero/fórmulas y exclusión de excepciones ADR para ciclos/cruces no autorizados. La segunda pasada desarrolló el gobierno de calidad de datos (dueños de Retail y Emisor, Datos, QA y Contraparte), el uso de horas y defectos del costo de calidad por EDT, y el procedimiento de ensayos de migración. Añadió perfilado, saneamiento e informe de decisiones por defecto conforme a RT-05.12. Se preservan producciones M16/M21, operación M21–56, seis condiciones de Art. 17.3 y 10+10 días hábiles de Art. 18. Las figuras 9.1 (gobernanza), 9.2 (puertas) y 9.3 (hitos) incluyen cita previa, fuente y explicación; Acta se acota a hito/paso de etapa.

## Comprobaciones

- `exportar_latex.py doctor` y `estado` correctos. La compilación detectó `ulem.sty` ausente; la coordinación restauró el paquete en TEXMFHOME sin alterar plantilla.
- `verificar --parte T7-09` correcto.
- `verificar-redaccion --parte T7-09` informa 0 errores y 2 avisos RR-19. Son avisos heurísticos sobre títulos de tablas; las dos tablas poseen título numerado, cita previa, fuente y análisis posterior, y caben en una página.
- `compilar --parte T7-09` produjo 15 páginas. No hay Overfull; queda un aviso hyperref de Unicode sin efecto visual observado.
- Revisión visual de portada y páginas con tablas/figuras a resolución de lectura. Las tres figuras están presentes, legibles y sin cortes. La figura 9.1 se simplificó tras detectar una tipografía inicial de alrededor de 5,5 pt; en la versión final su fuente mínima mide 11,77 pt al ancho de inclusión. La figura nueva y su explicación caben en la página física 6.
- `git diff --check` sin errores. No se modificó exportador/plantilla ni se justificó ejecutar sus pruebas unitarias.

## Dictamen del revisor independiente Luna

El revisor aplicó la skill canónica y leyó 38 páginas/anclas docentes e investigación, SD09 completo, pasajes pertinentes de Bases/C10, SD06/07,28 resultados de Anexo D y cuatro criterios materiales de la matriz (C-T02-01,C-T07-01/02,C-T09-07). Tras relectura de las correcciones no identificó hallazgos materiales de diseño abiertos en ese alcance. No revisó individualmente los 115 criterios ni Excel; no inspeccionó visualmente PDFs. ISO web devolvió 403 y la edición se contrastó con investigación local, sin consulta web independiente exitosa. La inspección visual y compilación las efectuó el orquestador, con cotejo visual adicional de la coordinación.

En la segunda pasada, un revisor Luna examinó gobierno, costo de calidad y migración. Detectó la omisión de RT-05.12 en el cuerpo de la oferta, que se corrigió con perfilado, saneamiento, informe de defectos y decisión por defecto. No identificó otra brecha material en esos focos. La revisión visual de la nueva figura la realizaron el orquestador y la coordinación.

## Límites y decisiones de ejecución

El diseño no demuestra ejecución de pruebas ni aceptación humana/contractual. T-13 deberá concretar herramientas/versiones, carga/concurrencia/TPS y perfiles por peak, datos, muestras y protocolos. Arquitectura/Calidad formalizarán antes del primer pipeline la calibración de complejidad y grafo; UX/Calidad y Ancoa revisarán objetivos de error/aprendizaje antes de construir; los responsables de negocio y Contraparte acordarán metas propuestas/tolerancias del Anexo D antes de sus campañas. La línea base oficial v3.0 y su conciliación con trabajo posterior se resolverán por control de cambios. No se reconstruyeron tablas ilegibles, porcentajes económicos ni páginas fuente inexistentes en los Markdown de Bases. Se requerirán elaboración/revisión humana registrada y declaración A-6 antes de presentar la oferta.

La coordinación sincronizó el texto y las tres figuras en la pestaña Preview de Google Docs y comprobó mediante exportación PDF que el texto de la pestaña Matriz permaneció idéntico. No hubo commit/push ni consulta a TrabajosAnteriores.
