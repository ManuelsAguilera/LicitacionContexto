# Integridad documental de SD-04

Comprobación de referencias locales sobre el árbol Git de `main@1e097c2`. No equivale a compilación ni a inspección visual de las figuras.

| Referencia | Línea SD-04 | Archivo en main |
|---|---|---|
| `figuras/diag-04-01_arquitectura-logica-objetivo.png` | 106 | Presente |
| `figuras/diag-04-02_arquitectura-logica-etapa-1.png` | 116 | Presente |
| `figuras/diag-04-03_capas-y-actores.pdf` | 150 | Presente |
| `figuras/diag-04-04_bloque-tiendas.png` | 259 | Presente |
| `figuras/diag-04-05_bloque-mercaderia.png` | 269 | Presente |
| `figuras/diag-04-06_bloque-venta-y-cumplimiento.png` | 279 | Presente |
| `figuras/diag-04-07_bloque-relacion-clientes.png` | 289 | Presente |
| `figuras/diag-04-08_bloque-credito-y-frontera.png` | 299 | Presente |
| `figuras/diag-04-09_bloque-integracion.png` | 309 | Presente |
| `figuras/diag-04-10_flujo-hibrido-tienda.pdf` | 321 | Presente |
| `figuras/diag-04-11_emplazamientos-logicos.pdf` | 349 | Presente |
| `figuras/diag-04-12_datos-y-frontera.pdf` | 367 | Presente |
| `figuras/diag-04-13_arquitectura-fisica-general.png` | 467 | Presente |
| `figuras/diag-04-14_red-y-segmentacion.png` | 553 | Presente |
| `figuras/diag-04-15_ambientes-y-despliegue.png` | 593 | Presente |
| `figuras/diag-04-16_conexiones-y-contingencia.png` | 611 | Presente |
| `figuras/diag-04-17_tienda-tipo.png` | 730 | Presente |
| `figuras/diag-04-18_data-center-primario.png` | 787 | Presente |
| `figuras/diag-04-19_dc01-casa-matriz.png` | 799 | Presente |
| `figuras/diag-04-20_data-center-secundario.png` | 813 | Presente |

Se comprobaron 20 referencias de figuras. Las veinte están presentes en main. La observación histórica de figuras ausentes no se traslada al estado vigente.

## Evidencia auxiliar

| Referencia citada | Estado en main |
|---|---|
| `sd-04_s2_memoria-capacidad.md` | 04_Adjuntos/tablas/sd-04_s2_memoria-capacidad.md |
| `sd-04_s2_dimensionamiento-nodos.md` | 04_Adjuntos/tablas/sd-04_s2_dimensionamiento-nodos.md |
| `sd-04_s2_inventario-hardware.xlsx` | No localizado por nombre exacto |

## Límites de esta recopilación

- El inventario de 14 interfaces actuales no se reconstruye a partir de flechas lógicas. SD-04 lo mantiene como levantamiento previo al diseño detallado.
- No se ha ejecutado una compilación de main ni certificado la legibilidad de sus veinte figuras.
- La comprobación por requisito atómico contra el Excel oficial, los anexos de SD-03 y la matriz T-12 queda en el plan de evaluación. Los IDs contenidos en las tablas son declaraciones documentales.
- En la consulta inicial al MCP de Graphify no existía `graphify-out/graph.json`. Tras agregar el adaptador MCP se ejecutó `graphify update .`, que generó el grafo estructural de scripts. Ese grafo no incorpora la revisión semántica de las Bases ni de los subdocumentos; los hallazgos proceden de los archivos originales.
