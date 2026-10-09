# Factores técnicos y TCF (paso 5, puerta G5, parte técnica)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Método: FEP03, diapositivas 38 a 41. Los factores de ambiente (EF) no están aquí: los asigna el equipo por consenso (`09_ef.md`, pendiente). Escala: 0 irrelevante, 1 incidental, 2 moderado, 3 medio, 4 significativo, 5 muy importante.

## 1. Valores propuestos

| Factor | Peso | Valor | Respuesta en una frase | Evidencia |
| :-- | --: | --: | :-- | :-- |
| T1 Sistema distribuido | 2 | 5 | Casi todo el procesamiento está repartido: nube pública, on-premise, 13 servicios más la base y 22 tiendas que operan 24 h sin enlace | Despliegue híbrido obligatorio (Art. 16); RNF-24 a RNF-28; RNF-32 (RTO ≤ 4 h) |
| T2 Objetivos de desempeño | 1 | 5 | El desempeño es exigible por umbrales numéricos con prueba de carga | RNF-06 (8 s), RNF-16 (400 ms), RNF-17 (3 s), RNF-18 (25 s), RNF-21 (2 s), RNF-19 (5 min) |
| T3 Eficiencia del usuario final | 1 | 4 | La productividad del cajero y del vendedor es un objetivo, pero no el principal | RNF-18, RNF-20 (60 s), RNF-07 (3 min), RNF-60 (5 s) |
| T4 Procesamiento interno complejo | 1 | 4 | Hay reglas no triviales (disponible con colchón, costo total de servir, atribución de comisión, conciliaciones), sin algoritmos científicos | RF-127 a RF-130, RF-076 a RF-078, RF-054 y RF-071 |
| T5 Código reutilizable | 1 | 3 | La plataforma común la reusan los 13 servicios, pero no se pide diseñar componentes para otros sistemas | RNF-52 a RNF-55; RT-03.07 |
| T6 Facilidad de instalación | 0,5 | 4 | Instalar es un proyecto: piloto de 3 tiendas, despliegue gradual, convivencia y reversión | sd-03 3.2.4; RNF-48 |
| T7 Facilidad de uso | 0,5 | 4 | Lo usa personal recién incorporado, con rotación de 62 % | RNF-49, RNF-50; RT-12.11 |
| T8 Portabilidad | 2 | 3 | Varios entornos (sitio, app móvil sin conexión, terminal compartida, caja, mesón), sin exigencia multiplataforma por componente | RT-17.01; RT-03.07 solo pide declarar la reversibilidad |
| T9 Facilidad de cambio | 1 | 4 | Muchas reglas se cambian sin programar | RNF-48, RF-184, RF-195, RF-121 y RF-178 (parametrizables) |
| T10 Concurrencia | 1 | 5 | Hay choque real de datos: reservas contra venta física, 104.000 pedidos en 3 días, 380 cajas | RF-098; RNF-22, RNF-23; Caso (volumetría) |
| T11 Objetivos de seguridad | 1 | 5 | Una filtración de datos de crédito fiscalizado tiene daño legal y reputacional máximo | RNF-33, RNF-34, RNF-37, RNF-71 a RNF-73; Ley 21.719 |
| T12 Acceso de terceras partes | 1 | 5 | Entran y salen muchos sistemas y organizaciones ajenas | 14 interfaces; 310 vendedores; unos 1.100 repositores externos; transportistas, procesadores de pago y proveedores |
| T13 Entrenamiento a usuarios | 1 | 4 | Hay que capacitar a mucha gente, con rotación alta y capacitación normativa obligatoria | RNF-49; RF-007 a RF-009; 1.900 incorporaciones de temporada |

## 2. Cálculo

Suma ponderada de peso × valor = 59. **TCF = 0,6 + 0,01 × 59 = 1,19**. El tamaño funcional sube un 19 %. Se calculó con `estimacion_ucp.tcf()` y se repitió a mano.

Pruebas de la puerta (paso 5): todos los valores están entre 0 y 5; no están todos en 3 ni todos en 5; los cinco extremos en 5 (T1, T2, T10, T11 y T12) tienen justificación propia con cifras; ningún factor está en 0; el TCF está entre 0,60 y 1,30.

## 3. Rango

| Escenario | Suma | TCF |
| :-- | --: | --: |
| Base | 59 | 1,19 |
| T3, T4, T5, T6, T7, T8, T9 y T13 bajan 1 punto | 51 | 1,11 |
| Esos mismos factores suben 1 punto | 67 | 1,27 |
| T8 en 4 (si el sd-04 exige portar componentes) | 61 | 1,21 |
| T5 en 2 (si no se pide reutilizar) | 58 | 1,18 |
| T10 o T12 bajan a 4 | 58 | 1,18 |

El UCP varía entre −7 % y +7 % respecto de la base por el TCF.

## 4. Decisiones del usuario (2026-10-08)

1. T8 queda en 3. Sube a 4 solo si el sd-04 exige portar componentes.
2. T5 queda en 3. Baja a 2 si no se pide reutilizar fuera del proyecto.
3. La capacitación (T13) se estima aparte (paso 7), porque la clase no la cubre. El factor queda en 4.
4. T10 y T12 se mantienen en 5, por su evidencia cuantitativa.
5. T11 queda en 5, porque la mayor parte del trabajo de seguridad va dentro del desarrollo.
