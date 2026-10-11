# Coherencia hacia atrás de la EDT con el subdocumento 3

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/verificar_coherencia_edt_sd03.py`; no editar a mano. Fecha: 2026-10-08. Compara la EDT corregida (`14_edt_corregida.md`) con `sd-03.tex` y sus anexos. «Coherencia hacia atrás» significa que lo que la EDT promete debe poder trazarse a lo que el sd-03 ya dice, y lo que el sd-03 ya compromete debe tener un entregable en la EDT. Los compromisos se buscan por palabras clave en el nombre y el origen de las cuentas: es una comprobación mecánica, no sustituye la lectura del equipo.

## 1. Comprobaciones mecánicas

| Comprobación | Resultado | Detalle |
| :-- | :-- | :-- |
| La etapa de cada servicio coincide con la Tabla 3.1 (13 servicios y la base tecnológica) | cumple | 14 nodos revisados |
| La Tabla 3.4 (RF por etapa) coincide con el Anexo B | cumple | Tabla 3.4 {'Etapa 1': 142, 'Etapas 1 y 2 (cartera por tramos)': 4, 'Etapa 2': 81}; Anexo B {'Etapa 1': 142, 'Etapas 1 y 2 (cartera por tramos)': 4, 'Etapa 2': 81} |
| La etapa de cada cuenta de software coincide con la etapa de sus RF en el Anexo B | cumple | todas coinciden |
| Los 227 RF del Anexo B están en alguna cuenta de control | cumple | 227 RF |
| Las 9 obligaciones del proponente (OP-01 a OP-09) están en alguna cuenta | cumple | todas |
| Los 28 resultados del Anexo D se rastrean a una cuenta de control | cumple | todos |
| Ninguna cuenta implementa algo excluido en el Anexo A (verbos de la prueba P3.4) | cumple | ninguna |

## 2. Compromisos del sd-03 frente a la EDT

| N.º | Sección del sd-03 | Compromiso | Gravedad | Estado | Cuenta de la EDT |
| :-- | :-- | :-- | :-- | :-- | :-- |
| K1 | 3.2.2 | Un nuevo punto de venta capaz de operar sin conexión en las 22 tiendas es parte de la Etapa 1 (y componente de la Tabla 3.1) | A | cubierto | 1.5.5.1, 1.5.5.2, 1.7.13, 1.9.13 |
| K2 | 3.3.1 y 3.4.5 | El punto de venta de 2014 se sustituye tienda por tienda tras acreditar la operación sin conexión y el retorno | A | cubierto | 1.7.13 |
| K3 | 3.2.3 | Piloto del punto de venta en tres tiendas | A | cubierto | 1.9.11, 1.11.5 |
| K4 | 3.2.3 y 3.4.5 | Corte de enlace provocado de 24 horas en una tienda del piloto, en los meses 6 y 7, fuera de los congelamientos, con retorno ensayado | A | cubierto | 1.9.11 |
| K5 | 3.4.5 | Modalidad de contingencia tributaria aprobada y probada antes de comprometer la operación sin enlace | M | cubierto | 1.6.12 |
| K6 | 3.2.3 | El proponente propone los criterios del cupo preaprobado y la filial emisora los fija antes de la prueba | M | cubierto | 1.2.10 |
| K7 | 3.2.3 | Compuerta de cada tramo de la cartera, cerrada por la Contraparte Técnica y la filial emisora | A | cubierto | 1.7.14, 1.13.5 |
| K8 | 3.2.3 | Plan de comunicación a los clientes en la migración de la cartera | A | cubierto | 1.13.5 |
| K9 | 3.2.3 | Plan alternativo para cada una de las dos condiciones del adelanto del negocio financiero (crédito con corte de enlace y convivencia con la plataforma de 2011) | A | cubierto | 1.1.14 |
| K10 | 3.3.1 | Evaluación de comercio electrónico y fidelización con las pruebas de la primera etapa, y decisión de conservar, remediar o sustituir cada plataforma antes de su ola | M | cubierto | 1.9.12 |
| K11 | 3.4.6 | Pruebas de tareas del punto de venta con cajeros nuevos y experimentados antes del despliegue | M | cubierto | 1.9.13 |
| K12 | 3.4.6 | Pruebas de comprensión de precios, entrega e información crediticia con clientes y titulares | B | cubierto | 1.9.14 |
| K13 | 3.3.1 | Nueve plataformas: la novena (planillas y listas impresas) deja de ser registro oficial; el levantamiento documenta las catorce interfaces | B | cubierto | 1.2.1 |
| K14 | 3.2.2 | Retiro de la plataforma de crédito de 2011 en octubre de 2028 (mes 22) | B | cubierto | 1.7.11 |
| K15 | 3.2.2 | La recuperación ante desastres se prueba dos veces al año en operación | B | cubierto | 1.4.4, 1.9.4, 1.15.3 |
| K16 | 3.4.1 | Pruebas en preproducción a 1,5 veces el peak declarado y estrés hasta el punto de quiebre | B | cubierto | 1.9.4 |

Compromisos sin cubrir: **0** de 16. Gravedad A es lo que el sd-03 afirma de forma explícita como parte de la Etapa 1 o de sus condiciones; M, lo que el sd-03 pide para una prueba; B, lo que está cubierto de forma implícita.

## 3. Cuentas que se proponen agregar o corregir

Ninguna: la EDT cubre todos los compromisos revisados.

## 4. Qué no revisa

- No lee la prosa del sd-03 buscando promesas nuevas; solo los compromisos de la lista (K1 a K16).
- No valida que el contenido de una cuenta sea suficiente para cumplir el compromiso, solo que exista un entregable con ese tema.
- Las cifras del Anexo D y las ventanas de los hitos obligatorios se comprueban en `04_trazabilidad_resultados.md` y `17_cronograma_edt.md`.
