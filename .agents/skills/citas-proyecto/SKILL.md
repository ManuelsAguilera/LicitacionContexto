---
name: citas-proyecto
description: Aplicar la política de citas de la oferta TFEP-01/2026. Citar solo exigencias particulares y contexto o datos del Caso 09 con documento, capítulo o numeral y folio impreso verificado; depurar Referencias.
---

# Citas de la propuesta

## Alcance

Aplicar al texto, las tablas, las figuras y las Referencias de todos los subdocumentos de la oferta. El `.tex` de `02_Propuesta/latex_final/` es la fuente vigente de cada subdocumento ya importado. Conservar `00_Bases/Caso_09_Cadena_Multitienda.md` como espejo de búsqueda; no sustituirlo ni borrarlo al usar el PDF paginado.

## Selección de citas

1. **Citar** exigencias, restricciones, umbrales y condiciones **particulares del Caso 09** que configuren este proyecto. Si el Caso precisa o endurece una regla transversal, citar el apartado del Caso que fija la condición particular.
2. **Citar** contexto y datos **propios de Ancoa** necesarios para entender el problema o justificar la solución: cifras, sistemas existentes, dos negocios, entrevistas, indicadores, volumetría y proyecciones del Caso.
3. **No añadir citas bibliográficas** a exigencias generales de las Bases Administrativas o Transversales ni a instrucciones del profesor o del Comunicado 10. Conservar su contenido obligatorio y los IDs de trazabilidad necesarios. El nombre de una norma o de un requisito puede mantenerse como identificador técnico sin crear una entrada bibliográfica por esa sola mención.
4. **No citar como fuente externa** las decisiones, metas, métodos, resultados previstos o cálculos propios de Only Simple Solutions. Exponer sus supuestos y procedimiento. Remitir por nombre y sección a otro subdocumento, anexo o formulario propio cuando sirva para navegar la oferta; esa remisión interna no genera una referencia bibliográfica.
5. No incorporar texto, cifras, imágenes ni diagramas de terceros como elaboración propia. Si son indispensables, resolver su atribución antes de usarlos; nunca atribuirlos ficticiamente al Caso.

## Localizar la página correcta

1. Buscar el término en [`90_Referencia/caso09_ocr_paginado.txt`](../../../90_Referencia/caso09_ocr_paginado.txt) con `rg -n -i`. Cada línea lleva `pNN`, el **folio impreso**. Consultar el [índice de capítulos](../../../90_Referencia/indice_paginas_caso09.md) para orientar la búsqueda.
2. Abrir la página correspondiente del [PDF original del Caso 09](https://drive.google.com/file/d/1cVj84Af4bNYeXu8R1FHi8BoYtOLfcGs1/view), o de su [copia OCR buscable](https://drive.google.com/file/d/1BrPLM6_b5pcIiXiqeMNqRKUZ7NVZyJwW/view), y comprobar visualmente afirmación, capítulo/numeral y folio. En ambos PDF: página del visor = folio impreso + 1; la portada carece de folio.
3. Citar **la página que contiene el dato**, no la primera página del capítulo. Si la afirmación se extiende efectivamente por varias páginas, usar `pp. NN–NN` tras verificar ambos extremos. No usar el número de línea del Markdown ni la página del visor como `p.`. Si el OCR falla, leer la página visible; no inventar folios.

## Forma y consistencia

- La cita en el lugar de uso incluye autor institucional, año/sufijo de la entrada bibliográfica, nombre del documento y capítulo o numeral con folio: `(Multitiendas Ancoa S.A., 2026, Caso 09, cap. 14, núm. 14.1, p. 31)`. Ajustar año/sufijo al listado real antes de insertar. Este ejemplo corresponde a la proyección de hasta 25 tiendas, comprobada en el folio 31.
- Agrupar afirmaciones contiguas del mismo apartado bajo una cita clara, sin repetirla en cada oración. Repetir si cambia el apartado o se vuelve ambigua la procedencia. No atribuir al Caso un valor propuesto por OSS.
- En una tabla o figura propia, conservar `Fuente: Elaboración propia`. Si incorpora cifras o condiciones particulares del Caso, precisar `a partir de Caso 09, cap. X, p. NN` con localización comprobada.
- Mantener `Referencias` y luego `Declaración de uso de IA` al final. En Referencias, incluir únicamente las obras citadas bibliográficamente en el texto o en fuentes de tablas y figuras. Comprobar en ambos sentidos: cita → entrada y entrada → cita. Las remisiones internas SD/T/Anexo se comprueban por existencia y sección, no con bibliografía.

## Procedimiento de edición

1. Leer `AGENTS.md`, las fuentes vigentes y el archivo a revisar. Inventariar citas actuales y afirmaciones particulares sin cita. Clasificar cada una como exigencia particular, contexto/dato del Caso, regla general o decisión propia.
2. Verificar cada cita nueva o conservada en el OCR paginado **y** en el PDF visible. Registrar internamente el término buscado, folio y apartado. El Markdown original permanece intacto para contrastar texto, nunca para inferir páginas.
3. Editar citas, fuentes de tablas/figuras y la redacción mínima necesaria para separar orígenes. No retirar requisitos, cifras, umbrales ni trazabilidad al quitar citas bibliográficas.
4. Depurar Referencias y verificar autor, año, título y correspondencia bidireccional. Comprobar las remisiones a anexos, formularios y otros subdocumentos.
5. Para un `.tex`, usar solo `.agents/skills/exportar/SKILL.md` al verificar y compilar. Si hay un Preview de Google Docs derivado del `.tex`, sincronizarlo sin alterar las otras pestañas.

## Ejemplos rápidos

| Afirmación | Tratamiento |
| :--- | :--- |
| «Ancoa opera 22 tiendas en 11 regiones» | Citar Caso 09, cap. 2, núm. 2.1, p. 5. |
| «Se proyectan hasta 25 tiendas» | Citar Caso 09, cap. 14, núm. 14.1, p. 31. |
| «Aplicaremos una puerta de calidad antes de producción» | Decisión de OSS; explicar control y evidencia, sin cita bibliográfica. |
| «La cobertura mínima general es 70 %» | Conservar valor e ID RT si aporta trazabilidad; sin cita bibliográfica a Bases Transversales. |
| «El detalle está en SD06, sección 6.2» | Remisión interna; sin entrada bibliográfica por esa sola mención. |
