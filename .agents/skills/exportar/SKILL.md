---
name: exportar
description: Exportar una parte aprobada desde Markdown a PDF corporativo y copia de Google Docs.
---

# Exportar

1. Consulta `05_Gestion/README.md` y la muestra visual en `plantillas/muestra.md`.
2. Ejecuta `build.py --parte T7-NN --dry-run`; revisa la lista de secciones, adjuntos y estado de borrador.
3. Ejecuta la exportación PDF. Pandoc mejora la conversión Markdown cuando está disponible; Edge/Chromium es el renderizador PDF documentado para Windows. El conversor Markdown local sirve de respaldo limitado y debe pasar QA visual.
4. Para crear Google Docs, prepara DOCX/HTML compatible e importa como documento nativo con el conector Google Drive autenticado. Verifica contenido y formato después de importar; nunca afirmes que el HTML local es un Doc publicado.
5. Entrega nombres conforme al Comunicado 10; los Docs son copias editables derivadas. Nunca publica los 14 subdocumentos automáticamente.
