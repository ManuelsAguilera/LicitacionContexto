---
estado: propuesta de diseño
parte: T7-09
actualizado: 2026-10-11
---
# Figuras para el Plan de Calidad (SD09)

## Conclusión de la revisión

El capítulo 9 necesita figuras integradas. El Comunicado 10, apartado «Figuras, diagramas y esquemas», exige que texto y diagramas construyan juntos la explicación; una figura solo en anexo no basta. Cada una debe citarse antes de aparecer, llevar número, título y fuente, y explicarse después. Su texto debe poder leerse impreso sin ampliar, con al menos 9 puntos. Bajo cada título de sección debe haber primero texto de caída, no una figura.

El archivo LaTeX actual de SD09 contiene solo la introducción y los tres títulos obligatorios: 9.1 Plan de Calidad, 9.2 Estrategia de Aseguramiento de Calidad y 9.3 Alineación con Plan de Trabajo. Las ubicaciones de abajo son para incorporar al redactar el capítulo; la matriz interna de 115 criterios aporta contenido, pero no es todavía el cuerpo de SD09. Se conserva la estructura del Comunicado 10 y se remiten los detalles de pruebas a T-13 y el protocolo de recepción a T-17.

## Selección revisada: dos figuras

La primera versión tendrá **una figura en 9.2 y otra en 9.3**. La numeración final será consecutiva dentro del capítulo (por ejemplo, Figuras 9.1 y 9.2), aunque las figuras aparezcan en las secciones 9.2 y 9.3. La sección 9.1 se explica con texto y una tabla compacta de categorías, indicadores y umbrales; no necesita una figura decorativa. La trazabilidad bidireccional se desarrolla con un ejemplo breve en prosa y referencias a la matriz y T-13/T-17; un diagrama adicional repetiría en gran parte el flujo de puertas.

### Figura en 9.2 — Puertas de calidad de una versión

**Pregunta que resuelve:** ¿cómo se detiene una versión defectuosa y quién puede autorizar que avance?

**Versión A, recomendada: recorrido horizontal con retorno.** Cinco estaciones con rótulos de una o dos palabras: «Cambio» → «CI» → «QA» → «Preprod» → «Acta». Una franja «equipo» sostiene las primeras cuatro; «Contraparte» está bajo el acta. La producción aparece después del acta, no como una estación que se aprueba sola. Un retorno rojo desde cualquier puerta fallida lleva a «corregir y repetir». Cada estación tiene un símbolo pequeño de comprobación; el texto exterior o una leyenda corta agrupa las pruebas que ocurren ahí.

**Versión B: carriles de responsabilidad.** Dos carriles, «Proponente» y «Contraparte», con fichas que pasan de revisión/pruebas/evidencia al acta. Hace más visible la autoridad de firma, pero puede sugerir demasiados traspasos. Usarla solo si el texto de 9.2 necesita explicar roles más que secuencia técnica.

**Lo que queda en el texto:** umbrales por puerta (≥70 % lógica de negocio como bloqueo, ≥80 % de código nuevo como objetivo separado, deuda ≤5 % y duplicación ≤3 % según política SD06), tipos y calendario de pruebas, ambiente/datos, tratamiento de defectos y criterios de repetición. El diagrama comunica el orden y el retorno; el texto y T-13 fijan el procedimiento medible. Ubicación: tras el párrafo sobre revisiones por pares y análisis estático/dinámico, antes del desglose de niveles de prueba. Fuentes: Bases Transversales 20.1, Bases Administrativas Art. 18, SD06 y matriz T01/T02/T09/T10.

### Figura en 9.3 — Calidad sobre los hitos del proyecto

**Pregunta que resuelve:** ¿en qué momento deben terminar las pruebas y aceptaciones para permitir las dos producciones?

**Versión A, recomendada: dos carriles de etapa y una franja de operación.** Carril Etapa 1: certificación **M12** → marcha blanca **M13–15** → producción **M16**. Carril Etapa 2: certificación **M18** → marcha blanca **M19–20** → producción **M21**. Una banda inferior «calidad continua» atraviesa desarrollo y marcha blanca; desde M21 a M56 aparece «operación», con símbolos de ensayos semestrales de resiliencia/DR y revisión anual de seguridad. La Etapa 2 se dibuja comenzando mientras termina la Etapa 1: así se ve el solapamiento.

**Versión B: barra de 56 meses con cuatro puertas ampliadas.** Una línea larga ubica M12, M16, M18, M21 y M56; dos recuadros de aumento muestran las marchas blancas. Reduce el número de carriles, pero la escala completa dificulta leer los meses 12–21, donde están las dependencias decisivas.

**Lo que queda en el texto:** paquetes EDT 1.9 y 1.12, dependencias con seguridad 1.8 y migración 1.7, campañas previas a cada producción, expediente, ventanas de revisión/subsanación y responsables. El diagrama no reemplaza el Gantt del T-14. Ubicación: después del párrafo que enlaza estas ramas con SD07. Fuentes: SD07, Bases Arts. 17–18, Transversales 20.1 y vista de aceptación de la matriz.

### Regla visual común

Máximo cinco estaciones o hitos principales por figura; texto de una a tres palabras dentro de cada forma, más cifras de mes donde aporten. Usar color para separar proceso, decisión y corrección, pero añadir formas o líneas para que funcione impreso en escala de grises. Mantener los colores y códigos del resto de la propuesta. La leyenda identifica símbolos; el párrafo posterior interpreta el recorrido y sus excepciones. La figura nunca tiene que contener todas las reglas que el lector necesita aplicar.

Los 115 criterios, las 38 brechas y el mapeo completo de ocho categorías contractuales a nueve características ISO se leen mejor como tablas o fichas enlazadas. Tampoco conviene repetir la arquitectura de SD03/04 ni toda la carta Gantt de SD07.

## Material reutilizable y producción

Existen fuentes Graphviz preliminares [`escalera_calidad.dot`](../../04_Adjuntos/diagramas/escalera_calidad.dot) y [`d5_niveles_aceptacion.dot`](../../04_Adjuntos/diagramas/d5_niveles_aceptacion.dot). Representan niveles de aceptación, pero contienen demasiado texto y consecuencias contractuales por cotejar; no sirven como figura final. Pueden orientar jerarquía y paleta de la puerta de calidad, con rediseño propio.

Guardar fuente editable y exportación PNG/PDF legible en `04_Adjuntos/diagramas/`; incorporar la imagen exportada al cuerpo LaTeX mediante el flujo del proyecto. Antes de dar por cerrada cada figura, verificar en el PDF compilado: referencia anterior, leyenda/fuente junto a imagen, explicación posterior, tipografía impresa ≥9 puntos y concordancia de IDs/umbrales con la matriz y las Bases. Para una figura extensa, crear una vista general y una de detalle diseñada aparte; el Comunicado 10 prohíbe recortar una imagen grande como detalle.
