# Revisión inicial de la migración T7-02 — `Informes(5).md`

Fecha: 2026-10-02  
Estado: importado como borrador; requiere revisión humana.

## Resultado de la migración

- Se reconocieron 25 bloques dentro del capítulo 2.
- Los 25 bloques quedaron asignados a las cinco secciones obligatorias 2.1–2.5 del Comunicado 10.
- Se detectaron cuatro tablas. Tres se conservaron completas porque comparan varias dimensiones. La tabla extensa de requerimientos también conservó sus dimensiones y se dividió en tres bloques con encabezados repetidos.
- Una figura referenciada se extrajo a `04_Adjuntos/migracion/T7-02/`.
- Las referencias se conservaron en `sd-02_referencias.md` como borrador sin validación bibliográfica.
- Los bloques preliminares y finales que no forman parte de 2.1–2.5 permanecen trazados en `migracion_T7-02_Informes5.json`.
- La declaración de IA de la fuente no se incorporó al registro oficial porque está incompleta: declara uso en 2.3, pero no completa los niveles de texto y diagramas ni las comprobaciones realizadas.

## Problemas visibles conservados para revisión

1. El encabezado `2.2.3` se repite para particularidades regulatorias y estacionales; el segundo debería revisarse como posible `2.2.4`.
2. El título de la promesa 4 contiene el texto ajeno al documento `HOLA SAMIRA DONDE ESTASHOLA SAMIRA DONDE ESTAS`.
3. La subsección `2.3.5 Síntesis …………` conserva un marcador incompleto.
4. La sección 2.5 menciona 223 RF y 75 RNF, mientras la fuente oficial vigente del repositorio declara RF-001…RF-226, RNF-01…RNF-76 y OP-01…OP-09. Las cantidades y la sigla `RFN` deben actualizarse contra el Excel oficial, no por inferencia.
5. Varias cifras todavía no están registradas en `02_Propuesta/datos.yml`; el verificador las mantiene como avisos pendientes.
6. Faltan los adjuntos declarados ADJ-004 y ADJ-005 y los registros completos de uso de IA por artefacto.
7. Las referencias migradas requieren comprobar vigencia, correspondencia con las citas y formato APA 7.

## Verificación automática

`check.py --parte T7-02 --dry-run` finalizó sin errores estructurales. Los avisos se mantienen porque el documento es un borrador y no deben resolverse inventando cifras, revisión humana, adjuntos o niveles de uso de IA.
