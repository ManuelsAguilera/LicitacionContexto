---
name: revisar-seccion
description: Revisar una sección frente a requisitos, bases, cifras y consistencia documental sin editarla.
---

# Revisar una sección

1. Contrasta la sección con `05_Gestion/convenciones/reglas-redaccion.md` (cada regla RR-NN con su fuente en el Comunicado 10); si el subdocumento ya es `.tex`, ejecuta `exportar_latex.py verificar-redaccion --parte T7-NN` y suma lo que solo se revisa a mano.
2. Obtén el contexto con `brief.py <ID>` y contrasta cada requisito citado contra el espejo oficial y las Bases originales.
3. Comprueba cifras y términos con sus fuentes, referencias, anexos y componentes relacionados.
4. Devuelve una tabla por requisito con cumple/no cumple/no verificable y evidencia localizable.
5. No edites contenido ni asignes `revisado`; el integrante responsable registra su propia revisión.
