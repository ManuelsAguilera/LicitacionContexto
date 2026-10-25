# Publicación del contexto y las fuentes — 25 de octubre de 2026

## Alcance de la rama

Preparada desde `origin/main` en `1a1828fb1d373de324293cff76e1996df57481c3`, sin incorporar los 67 commits completos de la rama local de diagramas. Publica el contexto del equipo, herramientas, archivo reversible y las fuentes importadas que ese contexto necesita para ser utilizable por otras personas.

- Diez subdocumentos principales, tres anexos y trece formularios recibidos; conserva además el T-11 local divergente para conciliación.
- Las 147 figuras referenciadas por esas fuentes, con rutas existentes. No incorpora los generadores ni los cambios pendientes de Draw.io del checkout de trabajo.
- Entrada del equipo: `80_Artefactos/contexto-activo/indice.md`; matriz de ajustes de contenido como consulta puntual. SD-04 y SD-07 son referencias de consistencia indicadas por el usuario, subordinadas a Bases y Comunicado 10; el resto sigue por conciliar.
- Los nueve archivos históricos trasladados conservan su contenido y manifiesto. Cachés, temporales de pruebas, ZIP de recepción y PDF compilados de informes no se publican.

## Comprobaciones de esta copia de publicación

- Las 26 fuentes recibidas coinciden byte a byte con las integradas en el checkout de trabajo antes del commit. Los hashes de SD-04 y SD-07 coinciden con el registro técnico de referencias y usan LF.
- `exportar_latex.py verificar`: diez partes disponibles correctas; cero referencias de figuras ausentes.
- `python -m unittest discover -s 05_Gestion/tests -v`: 256 pruebas ejecutadas; tres fallos y un error ya identificados previamente. Las 15 pruebas nuevas de contexto pasan.
- Persisten diferencias del diccionario publicado/generado, hash del escenario de empaquetado Prism y la expectativa C10 de la prueba editorial RR-20. El error corresponde al escenario de compilación de humo T7-14; no se declara suite completa aprobada.
- Se conserva un espacio final preexistente en la fuente recibida SD-07 para no alterar el hash de la referencia. `git diff --check` lo señala; no es una modificación nueva de contenido.

Las instrucciones requieren revisión de otra persona mediante PR antes de incorporar a main. La publicación de la rama no equivale a revisión humana ni cierre de consistencia.
