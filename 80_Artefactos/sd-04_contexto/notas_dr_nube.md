# Notas para el sd-04: sitio secundario en nube y marco de continuidad

Documento de trabajo. No es entregable. Resultado de una búsqueda hecha con otra IA (2026-10-06). Ningún dato de aquí se cita en la propuesta sin abrir antes la fuente primaria: la búsqueda no entregó enlaces directos, solo etiquetas.

## Decisión del equipo
Sitio secundario de recuperación ante desastres en una región de nube pública (Bases Administrativas, art. 20: "sitio o región secundaria"). Se decide y justifica en el sd-04, sección 4.3.2.

## Afirmaciones recibidas y su estado

| Afirmación | Estado | Qué falta |
| :-- | :-- | :-- |
| La CMF exige continuidad del negocio con RTO y RPO y pruebas periódicas (RAN 20-9) | Plausible; sin enlace ni número de norma verificado | Abrir el texto oficial en cmfchile.cl |
| El capítulo 20-7 (externalización) aplica a emisores de tarjetas no bancarios y exigía sitio de contingencia en Chile | Sin verificar. Los capítulos 20-x de la RAN se dirigen a bancos; si aplican a emisores no bancarios depende de la norma que los remita | Confirmar el ámbito de aplicación y qué norma rige a la filial emisora |
| 20-8 (incidentes) y 20-10 (ciberseguridad) obligan al emisor | Sin verificar, mismo reparo | Ídem. Verificar también la numeración (la búsqueda y mi memoria difieren) |
| Ley 21.719 permite alojamiento en el extranjero con garantías adecuadas; vigencia progresiva hasta diciembre de 2026 | Plausible; no verificado | Leer el texto en bcn.cl, en especial transferencias internacionales |
| Sitios secundarios a más de 30 a 50 km, o en otro país, "práctica estándar" | Sin fuente. No citar | Buscar una fuente o declararlo como criterio propio |
| Google Cloud tiene región en Santiago (southamerica-west1) y São Paulo | Coincide con lo que se conoce; verificar zonas | Página oficial de regiones |
| AWS sin región completa en Chile; Azure con Brazil South y "Chile Central" anunciada | Sin verificar; estos datos cambian rápido | Páginas oficiales de cada proveedor, con fecha |
| Brechas típicas de una sala de 2011 (N o N+1, sin contención de pasillos, extinción antigua, respaldo en la misma comuna) | Generalidades razonables; sin fuente citable. La brecha real es la del informe interno de 2024, que no se entregó | Declarar como supuesto, con "Si no se cumple" |

## Pendiente
- Qué norma rige a la filial emisora en continuidad y externalización, y si exige sitio de contingencia en Chile (condiciona la región secundaria).
- Dónde pueden residir los datos del Emisor (RT-16 y Ley 21.719).
- Región primaria y secundaria concretas, con distancia y análisis de amenazas comunes (RT-07.02).

## Resultado de leer las fuentes primarias (PDF en `90_Referencia/CMF/`)

- `articles-28982_doc_pdf.pdf`: capítulo 20-7 de la RAN (Circular 3.570/2014; texto con la Circular 2.244/2019). Ámbito: "instituciones bancarias" (num. I.1). El centro de contingencia en Chile se exige solo cuando un banco externaliza procesamiento en el exterior (num. IV.1.b.i), con excepción por informe independiente. Para el centro de contingencia en el país pide "ubicación y distancia" que garanticen continuidad, sin cifra. No existe el "30 a 50 km" como regla.
- `2026040763_1.pdf`: informe normativo CMF de abril de 2026, propuesta en consulta pública. Solo extiende a emisores de tarjetas no bancarios el archivo I28 (registro de proveedores, actividades e incidentes), semestral (IV.3, tabla 9). No impone sitio de contingencia al emisor. Cita las NCG 502, 507, 508, 509, 510 y 514 como normas de otros fiscalizados con estrategias de término de servicio; no se leyeron.
- Conclusión: ninguna de las dos obliga a la filial emisora a tener el secundario en Chile. Una región de nube fuera del país es defendible con el art. 20 de las Bases Administrativas, pero queda por verificar la norma propia del emisor (Circular N° 1 de emisores, NCG aplicables) y la Ley 21.719.
- Entregables derivados (propuestos en `sd-03_contexto/ronda0_nombres.md`): 3.12 plan de salida del proveedor de nube, 3.13 informe de diligencia reforzada, 3.14 registro en formato I28 (condicional).
