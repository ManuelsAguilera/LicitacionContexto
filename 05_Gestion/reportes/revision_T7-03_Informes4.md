# Revisión del piloto de importación T7-03

**Fecha:** 2026-09-30  
**Fuente conservada:** `05_Gestion/migraciones/fuentes/T7-03_Informes4_source.md`  
**Vista previa:** `05_Gestion/reportes/vistas_previas/T7-03_Informes4_preview.pdf`  
**Estado de los artefactos:** borrador; requiere revisión humana.

## Resultado

- Se importó el documento completo como cuatro secciones con el índice obligatorio del Comunicado 10: resumen ejecutivo, alcance, esquema de solución y explicación de la solución.
- El mapeo cubrió los 54 bloques del capítulo; no quedaron bloques del capítulo sin destino. Se excluyeron los índices y materiales ajenos al capítulo, incluidas las referencias y la declaración de IA de la fuente.
- Las 25 tablas del capítulo se transformaron en párrafos con etiquetas descriptivas. El original se conserva intacto para cotejo y trazabilidad.
- La figura se extrajo del Markdown y quedó como PNG local en `04_Adjuntos/migracion/T7-03/`.
- El generador creó un PDF de 42 páginas con portada corporativa, encabezado y pie, texto seleccionable y marca de agua **BORRADOR**. El índice de esta vista previa no muestra números de página estimados; no es un PDF de entrega.

## Correcciones editoriales aplicadas

- Se reemplazó la organización provisional del capítulo por las cuatro secciones exigidas oficialmente, conservando el contenido y la procedencia de cada bloque.
- Se eliminaron numeraciones antiguas de subsecciones donde interferían con la nueva jerarquía.
- Se reformuló el tratamiento del sistema central de retail de 2009: queda como una plataforma dentro de un ecosistema de nueve plataformas y catorce interfaces, no como el problema completo ni como objeto de reemplazo integral.
- Se hizo explícito que la compatibilidad del sistema central con un API Gateway y la observabilidad/sustitución individual de interfaces deben comprobarse; ya no se presentan como hechos garantizados.
- No se asignó estado `revisado` ni se inventaron validaciones humanas, fuentes o valores faltantes.

## Hallazgos visuales y pendientes

1. **Figura 3.1:** el recurso sí se incrusta en el PDF, pero la imagen fuente tiene fondo negro y textos pequeños; su contraste y legibilidad son bajos en página. Conviene reemplazarla por una exportación de mayor resolución y fondo claro, tras validación del contenido del diagrama.
2. **Extensión:** el subdocumento ocupa 42 páginas; el alcance concentra la mayor parte del contenido. La conversión a párrafos se hizo como se solicitó, pero el resultado queda denso. Recomiendo revisar agrupación, redundancias y longitud antes del cierre, sin volver a tablas.
3. **Pendientes fuente:** permanecen 12 páginas con marcadores `TODO` o `[VERIFICAR]` en el PDF. Se conservan visibles bajo la marca BORRADOR; deben resolverse antes de la exportación final.
4. **Cierre formal:** todavía faltan el artefacto final de referencias y el registro verificable de uso de IA. Por eso el modo de entrega final sigue bloqueado correctamente; la vista previa omite ambos apartados y no los simula.
5. **Verificación documental:** `check.py --parte T7-03` no reporta errores estructurales, pero genera avisos por referencias/cifras aún no registradas y pendientes de revisión. Estos avisos requieren cotejo con las bases y con el registro de cifras; no equivalen automáticamente a errores confirmados.

## Comando de generación de prueba

```powershell
python 05_Gestion/scripts/build.py --parte T7-03 --vista-previa
```

La vista previa se guarda en `05_Gestion/reportes/vistas_previas/`, nunca en `07_Entregables/`.
