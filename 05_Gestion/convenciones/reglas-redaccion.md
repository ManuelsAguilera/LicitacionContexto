# Reglas de redacción (contenido)

Qué se escribe y cómo se estructura el texto de cada subdocumento T-7. **No** definen el aspecto visual (tipografía, márgenes, portada, estilo de tabla): eso son las [reglas de plantilla](reglas-plantilla.md).

**Fuente y precedencia.** Estas reglas condensan el Comunicado 10 (`00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md`, secciones 2 a 7). Si una regla de este archivo y el Comunicado difieren, **manda el Comunicado**. La política de migración de tablas (`artefactos.md`) es un procedimiento de importación y no sustituye estas reglas.

**Quién las aplica.** Quien redacta o edita un `.tex` (en el editor local o en Prism) y quien revisa. Los agentes las aplican al escribir y no las cambian: modificar una regla requiere decisión del equipo y actualizar este archivo.

**Verificación.** `Auto` = la comprueba `python3 05_Gestion/scripts/exportar_latex.py verificar-redaccion [--parte T7-NN]` (solo informa; ERROR = incumplimiento claro, AVISO = heurística que exige criterio humano). `Manual` = la comprueba una persona al revisar. Los ID `RR-NN` son estables: no renumerar; las reglas nuevas toman el siguiente número.

## Estructura y texto

| ID | Regla | Fuente | Verificación |
| :--- | :--- | :--- | :--- |
| RR-01 | Títulos y subtítulos declarados en el índice se respetan al 100 %: numeración, texto y orden. No se omiten, renombran, fusionan ni reordenan. Pueden agregarse subtítulos de menor nivel; no del mismo nivel. | C10 §2.1–2.3 | Manual |
| RR-02 | Un título declarado que no aplica se mantiene y se justifica por escrito; no se acepta vacío ni la sola frase «no aplica». | C10 §2.4 | Manual |
| RR-03 | Cada capítulo abre con una introducción bajo su título: lo resume y lo conecta con otros capítulos, anexos y formularios. | C10 §2.6 | Manual |
| RR-04 | Ningún título, de ningún nivel, va seguido directamente de otro título, de una figura, de una tabla ni de una lista sin frase introductoria. Bajo cada título hay un texto de caída. | C10 §3 | Auto (ERROR) |
| RR-05 | El subdocumento resume y analiza; el anexo y el formulario detallan y listan. Un capítulo principalmente de tablas o listas no cumple. | C10 §3 | Auto (AVISO, > 60 % del capítulo) |
| RR-06 | Toda cifra relevante deriva de las Bases Técnicas del caso o de un cálculo mostrado. | C10 §3 | Manual |
| RR-07 | Nombres de componentes, módulos y servicios idénticos en todos los subdocumentos. | C10 §3 | Manual |
| RR-08 | La Oferta Técnica no contiene precios, tarifas, valores unitarios ni cifras que permitan inferir el monto de la oferta. | C10 §3 (Art. 50.2) | Auto (AVISO, palabras clave) |
| RR-09 | La sola mención de un estándar, sin evidencia de cómo la solución lo satisface, no cuenta. | C10 §3 (Art. 4.3) | Manual |

## Figuras

| ID | Regla | Fuente | Verificación |
| :--- | :--- | :--- | :--- |
| RR-10 | Texto y diagramas se combinan: el texto recorre, interpreta y concluye a partir de cada figura. Un capítulo técnico sin figuras integradas, o con figuras solo en anexos, no cumple. | C10 §4 | Manual |
| RR-11 | Cada figura se numera y titula («Figura N.N: …»), se cita antes de aparecer y se explica después. | C10 §4 | Auto (AVISO, leyenda y título) |
| RR-12 | Diagramas grandes: primero vista general y luego explicación por partes, con un diagrama preparado para cada parte. | C10 §4 | Manual |
| RR-13 | No se acepta recortar ni ampliar una sección de una imagen mayor como figura de detalle. | C10 §4 | Manual |
| RR-14 | Cada figura indica su fuente: elaboración propia o referencia APA 7. La leyenda de fuente acompaña una figura realmente insertada y explicada. | C10 §4 | Auto (AVISO) |

## Tablas (cuándo y qué contienen; el estilo está en la plantilla)

| ID | Regla | Fuente | Verificación |
| :--- | :--- | :--- | :--- |
| RR-15 | La tabla presenta datos que se comparan en varias dimensiones (cifras, dimensionamientos, alternativas, matrices). No explica: lo que se explica va como texto, apoyado en un diagrama. | C10 §5 | Manual |
| RR-16 | No se aceptan tablas «Concepto \| Descripción» ni con párrafos en las celdas. Si una celda necesita más de una frase, ese contenido es texto. | C10 §5 | Auto (AVISO) |
| RR-17 | Cada columna aporta al punto en que aparece; se eliminan las repetidas o vacías. Una tabla del cuerpo no supera cinco columnas. | C10 §5 | Auto (ERROR, > 5 columnas) |
| RR-18 | Una tabla del cuerpo no excede una página. Si el contenido es un listado, el detalle va al anexo o formulario y en el cuerpo una tabla de síntesis que lo cita. | C10 §5 | Auto (AVISO, > 25 filas) |
| RR-19 | Cada tabla se numera y titula («Tabla N.N: …») con su fuente, se cita antes de aparecer y va seguida de texto que dice qué se concluye. Ningún título va seguido directamente de una tabla. | C10 §5 | Auto (AVISO) |

## Referencias, cierre y uso de IA

| ID | Regla | Fuente | Verificación |
| :--- | :--- | :--- | :--- |
| RR-20 | Las referencias se citan en el lugar donde se usan, en APA 7; las citas a las Bases indican documento, capítulo o artículo y página. Toda cita está en la lista y toda referencia de la lista está citada. | C10 §6 | Manual |
| RR-21 | El subdocumento termina con dos secciones sin numerar, en este orden: Referencias y Declaración de uso de IA. | C10 §2.5, §6, §7.2 | Auto |
| RR-22 | El texto no contiene marcadores ni notas de borrador o del asistente (`TODO`, `[VERIFICAR]`, `[INSERTAR…]`, «Anexo ??», «borrador», «pendiente de validar») ni lenguaje de contexto académico (docente, estudiantes, «propuesta académica»). Su detección en el Informe 2 o la Propuesta Final deja el subdocumento como no presentado. | C10 §7.1 d | Auto (ERROR marcadores; AVISO lenguaje académico) |
| RR-23 | Ningún capítulo se entrega generado íntegramente por IA sin elaboración y revisión humana; el uso se declara en el A-6 y en la Declaración de uso de IA. No se declara una revisión humana que no ocurrió. | C10 §7.1–7.2 | Manual |
| RR-24 | Todo texto redactado o editado por un agente pasa por la skill `humanizer` antes de la revisión humana, acotada así: solo elimina patrones de escritura de IA (relleno, lenguaje promocional, vaguedad, muletillas, conectores y listas de tres por reflejo). No añade primera persona, opiniones ni «personalidad»; mantiene el registro formal; no altera cifras, IDs (RT, RF, RNF), nombres de componentes (RR-07), citas ni títulos (RR-01). Su uso se declara en la Declaración de uso de IA (RR-23). | Decisión del equipo | Manual |
| RR-25 | No se usan los dos puntos para introducir una explicación, una aclaración o una consecuencia dentro de una oración. Se reescribe con conectores o con oraciones separadas. Se admiten en las leyendas («Figura N.N: …», «Tabla N.N: …»), en las citas textuales y en las referencias. | Decisión del equipo | Manual |

## Qué hacer cuando una regla se incumple

- **No convertir automáticamente** tablas a párrafos ni al revés. Un `AVISO` se evalúa con criterio: a veces corresponde reescribir como texto, a veces dividir la tabla, a veces mover el listado a un anexo (RR-15, RR-18) y dejar una síntesis en el cuerpo.
- **Una tabla «conservada» por la política de migración puede seguir incumpliendo RR-16 o RR-17.** Esa política decide si se convierte al importar; estas reglas deciden si la tabla es aceptable en el cuerpo.
- Un hallazgo no equivale a una revisión humana: no cambia el estado a `revisado`.
