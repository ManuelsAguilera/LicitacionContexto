> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión Formulario T-19 (cartera de innovaciones)

Archivo: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-19.tex` (T19). Contraste: sd-13 (`sd-13/OnlySimpleSolutions-Subdocumento13.tex`, S13), sd-07, T-14, T-16, sd-03/sd-04, Bases Admin. arts. 28-30 (líneas 707-785) y T-19 (2328-2352), RT-26.01 a 26.08 (Bases_Transversales 1106-1117), Caso 09.

Resultado global: los 17 campos del formulario están en las cinco fichas, una por tipo del art. 28; tipos, nombres, etapas y meses (Lockers, Búsqueda, Retail Media y Fila en E2 con aceptación 19-20 y habilitación mes 21; Conteo en sombra 13-15 y uso mes 16) coinciden con sd-13, sd-07 y T-14. No hay precios ni montos (art. 50 respetado). La escala de madurez (componente documentado / integración probada / operación aceptada) es la misma en T19 y S13. Los problemas están en lo siguiente.

## Graves

**G1. Metas cuantitativas en T19 que S13 dice que se fijan después (contradicción y compromiso exigible).**
- T19 líneas 186, 294, 402, 503 y 616 fijan umbrales: -20 % minutos de personal por entrega (Lockers), +20 % detección por hora (Conteo), -10 % tasa de fallo (Búsqueda), 3 anunciantes con campaña conciliada en los meses 21-23 (Retail Media), -30 % espera física (Fila).
- S13 dice lo contrario: línea 125 "El acta de diseño fija el umbral de mejora temporal después del levantamiento"; línea 167 "El umbral contractual de mejora se fija con el levantamiento y se registra en el T-19 antes de ensayar"; línea 209 "El protocolo fija los umbrales"; línea 251 "El plan comercial fija la meta de captación e ingreso antes del piloto"; línea 293 "El acta de diseño fija el umbral".
- Dentro de T19, línea 497 (Retail Media) dice que las metas de captación "pertenecen al plan comercial" y la línea 503 fija tres anunciantes. Línea 190 admite que el 20 % "requiere revisión humana previa al compromiso".
- Art. 30.3: las innovaciones comprometidas son exigibles. Art. 29 exige "meta" en el T-19, así que T19 está bien en fijarla, pero S13 debe alinearse y el equipo debe decidir las cifras.
- Sugerencia: decidir si las metas son compromiso. Si lo son, corregir S13 (líneas 125, 167, 209, 251, 293) para citar las metas del T-19 y retirar de T19 las notas "requiere revisión humana" (190, 503 "Marketing debe revisar viabilidad"). Si no lo son, rotularlas "umbral de diseño no contractual" en ambos. Confirmado como inconsistencia; la cifra elegida es por confirmar.

**G2. Las innovaciones no figuran en la arquitectura (sd-03/sd-04), pese a RT-26.01 y art. 28.2.**
- T19 campo 7 de cada ficha las ubica en "capa de integración Retail", "adaptador", "procesador de apoyo", "índice vectorial/pgvector", "componente local de fila en SIT-01". Una búsqueda de `innovaci|locker|vectorial|fila virtual|probador|Retail Media|pgvector` en sd-03 y sd-04 da cero resultados.
- La Ficha 5 (línea 590) y la Ficha 1 (línea 160) remiten a "conciliar con SD-04/T-14". Ese componente local nuevo no existe en el nodo local L-01 a L-03 de la verdad vigente. pgvector no aparece en la lista tecnológica de ADR (solo PostgreSQL Flexible).
- Sugerencia: agregar en sd-04 (capa de integración / nodo local / PostgreSQL con extensión) una referencia a los cinco componentes, o rebajar en T19 las afirmaciones de ubicación a "se propone, pendiente de reflejar en SD-04". Confirmado el vacío; la solución es por confirmar.

**G3. Campo 8 sin los códigos de paquetes de la EDT (RT-26.02, art. 29).**
- T19 líneas 160, 268, 376, 477 y 590 dicen "Rama 1.10 ... El código detallado debe conciliarse con el T-14". El T-14 ya los tiene (`Formularios/...T-14.tex` líneas 422-426): 1.10.1 Lockers (1.864 HH; meses 13-18, 19-20, 21-56; H10 y H12); 1.10.2 Conteo (2.336 HH; 5-12, 13-15, 16-20, 21-56; H5 y H7); 1.10.3 Búsqueda (2.120 HH); 1.10.4 Retail Media (1.784 HH); 1.10.5 Modo Tienda (1.784 HH; ambos 13-18, 19-20, 21-56; H10 y H12), con subpaquetes 1.10.x.y (S07 líneas 830-874).
- Sugerencia: reemplazar la remisión pendiente por los códigos 1.10.1 a 1.10.5, los subpaquetes y los hitos (H5/H7 y H10/H12). Eliminar "debe conciliarse con el T-14" de un documento final. Confirmado.

## Medianas

**M1. Listas de referencias de T19 y S13 no coinciden.**
- T19 incluye fuentes que S13 no tiene en "Referencias": Cleveron 402 (s. f.-c) (T19 líneas 151 y 186), Vaccari et al. (2026) (259, 294), Zhu et al. (2024) (364, 402), Criteo 2024 David Jones (469, 503) y las tres de Qmatic (576-582, 616). S13 no menciona nada de esto en su texto.
- S13 cita la Biblioteca del Congreso (Ley 21.719) y T19 no.
- Sugerencia: unificar. Incorporar esas fuentes a las Referencias de S13 (y citarlas en su texto) o retirarlas de T19. Confirmado.

**M2. Ficha 4: campo 14 y 13 introducen "meses 21-23" y "cierre del mes 23" (líneas 503 y 507), que no están en S13 ni en T-14.**
- T-14 1.10.4: habilitación mes 21 y seguimiento hasta M56. S13 dice "la medición comienza en el mes 21 y continúa" (línea 251).
- Sugerencia: justificar en S13 y T-14 la ventana de piloto de 3 meses o retirarla. Por confirmar.

**M3. Ficha 1: el problema no usa el dato más fuerte del Caso.**
- T19 línea 130: "La operación actual no aporta tiempos de retiro". El Caso 4.7 y 7.2 dan 41 % de los pedidos en línea con retiro en tienda, que comparte mesón y personal con la sala. Art. 29.1 pide "el dato o la evidencia que dimensiona el problema". Las remisiones "capítulos 7 a 9" son imprecisas.
- Sugerencia: citar Caso 4.7 y 7.2 (41 %) y quitar "capítulos 7 a 9". Idem S13 línea 101. Confirmado.

**M4. Remisiones de capítulos del Caso incorrectas o débiles.**
- Ficha 5 (línea 552): "caps. 6-7" para probadores. En el Caso los probadores están en cap. 3 (tabla de zonas, línea 166), 4.4 (línea 219) y en el cap. 8 (entrevista, línea 446). El cap. 6 es conectividad.
- Ficha 3 (línea 343): "caps. 7-9". El Caso no menciona búsqueda del catálogo. El dato de apoyo sería 7.1/7.2 (cancelaciones por falta de existencia, 19 %), pero esos datos no son de búsqueda.
- Ficha 2 (línea 235): "bajar de 2 %"; el Caso (7.1, línea 350) dice "bajo 2 %". Corregir a "bajo 2 %".
- Sugerencia: citar capítulos y números exactos. Confirmado. Para la Ficha 3 se puede reconocer expresamente que el Caso no aporta dato de búsquedas (ya lo hace) y apoyarse en 9.1/9.4; art. 30.2 premia la pertinencia, por lo que conviene reforzarla (por confirmar).

**M5. T19 usa "AH-01" como nombre de componente de comercio electrónico (líneas 372 y 473).**
- En sd-04 (línea 135 y 147) AH-01, AH-03 y AH-04 son códigos de grupos de actores ("Comercio electrónico, terminal compartida y POS"), no un sistema o canal.
- Sugerencia: sustituir por "plataforma de comercio electrónico" (glosario) y, si se quiere, "actor AH-01". Confirmado como uso inexacto del código.

**M6. Riesgos de adopción: remisión circular a T-16.**
- T19 (194, 302, 410, 511, 624) dice que T-16 "consolida/contrasta" las valoraciones; S13 igual (131, 173, 215, 257); sd-08 (líneas 99, 343) dice que no los repite y los trata en el cap. 13. El T-16 no contiene ningún riesgo de innovación (solo O-03 de conteo cíclico, línea 347, y R-18).
- Además T19 y S13 usan escala cualitativa (media/alta) y T-16 una numérica (por ejemplo 0,40).
- Sugerencia: incluir en el T-16 los diez riesgos de adopción con IDs y escala numérica y referenciarlos desde T19, o declarar que T19 es la fuente única de esos riesgos y quitar "T-16 consolida". Confirmado el vacío.

**M7. RT-26.07 (modelado de amenazas) sin tratamiento.**
- Lockers (acceso físico, credenciales de retiro, apertura exterior) y Retail Media/Búsqueda (datos, terceros) tocan la arquitectura de seguridad. T19 y S13 no mencionan "modelo de amenazas" (búsqueda de "amenaza": cero).
- Sugerencia: indicar en el campo 16 de las fichas 1, 3 y 4 que habrá un modelado de amenazas propio (o declarar que no modifican la arquitectura de seguridad, con motivo). Por confirmar.

**M8. Impacto económico (art. 29.5 / RT-26.05): campo 10 y 11 sin ninguna magnitud ni vínculo.**
- T19 (168, 276, 384, 485, 598) dice solo "sustenta la valorización de la Oferta Económica". No hay referencia al Entregable 2 / flujo de caja ni a las HH del T-14 (9.888 HH en total, que no son precio).
- Sugerencia: añadir las HH por paquete del T-14 y remitir al ítem correspondiente del Entregable 2 (art. 30.1), sin montos. Por confirmar si se desea mostrar HH en el campo "Inversión".

**M9. RT-26.03 / madurez: escala propia sin respaldo ni nivel declarado en todas las fichas.**
- La escala de tres estados es del equipo y no cita fuente ni equivale a TRL (T19 línea 138 dice que "no se asigna un TRL"). RT-26.03 y art. 29.3 piden "la escala utilizada" y las fuentes; el evaluador puede esperar una escala reconocida. Ficha 5 y Ficha 3 no declaran explícitamente el nivel alcanzado ("el hardware tiene evidencia del primer estado"; solo Ficha 1 y Ficha 2 lo hacen).
- Sugerencia: definir la escala en una nota inicial del T19 (una vez), declarar el nivel actual por ficha y, si se quiere, mapearla a una escala reconocida con fuente. Por confirmar.

## Bajas

- B1. Líneas 96-104: la "Ficha 1 - Innovación 1" y su frase aparecen duplicadas (mismo label LaTeX repetido, doble entrada en el índice). Borrar el bloque 101-104.
- B2. Nombres del glosario: T19 escribe "SD-13", "SD-07", "SD-04" y "T-14" en vez de "subdocumento 13" (como hace su propia introducción, línea 94). Unificar. La línea 459 usa "repositorio" (término interno) en un texto de la oferta; reformular.
- B3. APA 7: dentro de cada ficha las fuentes no están en orden alfabético (Ficha 1: Cleveron a, b, Bloq.it, Cleveron c; Ficha 2: Scikit, Tabassi, International..., Vaccari; Ficha 3: ... Zhu antes de Tabassi; Ficha 5: Zebra, Epson, Google, Apple, Qmatic). Ordenar: Bloq.it, Cleveron a-c; International..., Scikit, Tabassi, Vaccari; etc. Además varias fuentes (Bloq.it, Zebra, Epson, Google, Apple, Jina, pgvector) están listadas pero no citadas en el texto de la ficha (campos 4 o 5). "(s. f.-a)" con "(2024, ...)" del mismo autor es correcto.
- B4. Ficha 2 campo 9: omite la construcción (T-14: meses 5-12) y la "candidata de M10" (S07 línea 541). Añadir para completar "mes del cronograma".
- B5. Ficha 5: el nombre "Modo Tienda" incluye información de zonas y productos (S13 línea 267), que T19 no recoge; solo describe la fila. Alinear.
- B6. Campo 1 de la ficha 5: "5. Experiencia de usuario, sostenibilidad o impacto social; la dimensión desarrollada es..." sobrecargado; basta "5. Experiencia de usuario".
- B7. Ficha 2 campo 14 y otros usan "cuatro semanas iniciales de medición" que S13 no menciona (S13 solo dice "antes del piloto"). Mantener solo en un lado o en ambos.

## Verificado sin hallazgo
- Precios (art. 50): no hay UF, CLP, USD ni montos. Las menciones a Oferta Económica y flujo de caja son solo remisiones.
- RT-26.06: Fichas 2 y 3 citan RT-18; RT-16.27, RT-13.01/03/07 existen y coinciden con el texto de las Bases.
- RT-26.08: la Ficha 2 cita medición en sombra en los meses 13-15 antes del mes 16, consistente con S13 línea 167, sd-07 línea 541 y T-14.
- Servicios R:M-01, R:M-03, R:V-01, R:CL-02, CLD-01, SIT-01 y L-01 a L-03 con los nombres de la verdad vigente.
