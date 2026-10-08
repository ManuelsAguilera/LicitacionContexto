# UUCW y UUCP (paso 4, puerta G4)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: resultado del modelo aprobado por el usuario, pendiente de la firma del equipo. Entrada: `07_entrada_calculadora.json`, generada con `05_Gestion/scripts/generar_entrada_ucp.py` a partir de `02_actores_uaw.md` y los `03_casos_de_uso_*.md`. Todavía no incluye TCF ni EF (paso 5).

## 1. Resultado

| Concepto | Valor |
| :-- | --: |
| Actores | 29 |
| Casos de uso | 127 |
| Transacciones | 296 |
| UAW | 64 |
| UUCW | 645 |
| **UUCP = UAW + UUCW** | **709** |

## 2. Dos vías que coinciden

- **Primera vía.** La calculadora `estimacion_ucp.py` (fórmulas y tablas de la clase, probada con el ejemplo de la diapositiva 63) recibe el JSON generado y da UAW 64, UUCW 645 y UUCP 709.
- **Segunda vía.** `05_Gestion/scripts/recalcular_uucp.py` no comparte código con la anterior. Relee los archivos de Markdown, cuenta las transacciones `T1`, `T2`… del detalle de cada caso (no la columna declarada) y aplica los pesos por su cuenta. También da 64, 645 y 709. Termina con código 1 si las dos vías difieren.
- Las dos coinciden exactamente. Hay pruebas en `05_Gestion/tests/test_g4.py`.

## 3. Composición

| Actores (UAW 64) | Cantidad | Peso | Subtotal |
| :-- | --: | --: | --: |
| Tipo 3 (persona con interfaz gráfica) | 16 | 3 | 48 |
| Tipo 2 (sistema por protocolo o archivo) | 3 | 2 | 6 |
| Tipo 1 (sistema por interfaz de programación) | 10 | 1 | 10 |

| Casos (UUCW 645) | Cantidad | Peso | Subtotal |
| :-- | --: | --: | --: |
| Simples (1 a 3 transacciones) | 125 | 5 | 625 |
| Medios (4 a 7) | 2 | 10 | 20 |
| Complejos (8 o más) | 0 | 15 | 0 |

Los dos medios son CU-EX-04 y CU-OF-02. La participación de los actores en el UUCP es de 9,0 %, dentro del rango típico de 5 % a 15 % (diapositiva 33). Con la sensibilidad del UAW (62 a 72), queda entre 9,3 % y 10,0 %.

## 4. UUCW por etapa y servicio

| Etapa | Servicio | Casos | UUCW |
| :-- | :-- | --: | --: |
| 1 | Existencias (EX) | 19 | 100 |
| 1 | Oferta comercial (OF) | 12 | 65 |
| 1 | Ventas (VE) | 11 | 55 |
| 1 | Originación de crédito (OR) | 9 | 45 |
| 1 | Evidencia financiera (EV) | 7 | 35 |
| 1 | Control de cruces (CC) | 6 | 30 |
| 1 | Cartera de crédito (CA) | 7 | 35 |
| 1 | Base tecnológica (BT) | 13 | 65 |
| | **Etapa 1** | **84** | **430** |
| 2 | Abastecimiento (AB) | 5 | 25 |
| 2 | Pedidos (PE) | 15 | 75 |
| 2 | Comisiones (CM) | 3 | 15 |
| 2 | Marketplace (MK) | 11 | 55 |
| 2 | Posventa (PV) | 5 | 25 |
| 2 | Clientes Retail (CL) | 4 | 20 |
| | **Etapa 2** | **43** | **215** |

El UAW no se reparte por etapa. En el paso 6 se asignará a la Etapa 1, porque los actores de la base tecnológica nacen allí, salvo que el equipo prefiera repartirlo por UUCW.

## 5. Rango por sensibilidad

El UUCP va de 667 a 717 con las sensibilidades de `06_decision_granularidad.md` y `02_actores_uaw.md`.

| Escenario | UAW | UUCW | UUCP |
| :-- | --: | --: | --: |
| Base | 64 | 645 | 709 |
| UUCW más bajo (todas las sensibilidades) | 64 | 605 | 669 |
| UAW más bajo (se retira AS-13) | 62 | 645 | 707 |
| Ambos | 62 | 605 | 667 |
| UAW más alto (sistemas a tipo 2) | 72 | 645 | 717 |
| Referencia: agrupación B | 64 | 565 | 629 |

## 6. Cómo reproducirlo

```
python3 05_Gestion/scripts/generar_entrada_ucp.py
python3 05_Gestion/scripts/recalcular_uucp.py
python3 -m unittest discover -s 05_Gestion/tests -p test_g4.py -v
```
