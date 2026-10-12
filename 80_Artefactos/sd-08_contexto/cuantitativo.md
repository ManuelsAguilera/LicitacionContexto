# Análisis cuantitativo del sd-08 (valor esperado, FMEA y simulación)

Documento de contexto, no entregable, fechado el 2026-10-12. Usa la calificación aprobada de `calificacion.md` (Tablas 1 y 2) sin cambiar sus cifras. Todo es estimación del proponente. Fragmento para la propuesta: `fragmentos/8-2b.tex.txt`.

## Cómo reproducir

```bash
python 05_Gestion/scripts/simular_riesgos_cronograma.py --iteraciones 10000 --semilla 20261012 --agregacion solapada
python 05_Gestion/scripts/simular_riesgos_cronograma.py --agregacion serie   # cota superior
python -m unittest discover -s 05_Gestion/tests -p test_simular_riesgos_cronograma.py -v
```

La semilla y las iteraciones son las del valor por defecto. Resultado de la prueba: 5 pruebas, OK.

## Supuestos del modelo

- Los 14 riesgos críticos y altos son eventos discretos e independientes.
- Cada uno ocurre con su P (valor de la Tabla 1; en el escenario con respuestas, la P residual de la Tabla 2 con la misma I) y, si ocurre, aporta un atraso triangular (mínimo 0,5 x semanas, moda = semanas, máximo 1,5 x semanas). Las semanas son las de la Tabla 2.
- Agregación. Cada riesgo se asigna a UN eslabón de la ruta crítica (Tabla 7.6 del sd-07, más un eslabón propio de migración de cartera y retiro de 2011). Cadenas por hito. Mes 16: levantamiento, arquitectura, plataforma base, desarrollo Etapa 1, certificación Etapa 1, marcha blanca Etapa 1. Mes 21: desarrollo Etapa 2 y marcha blanca Etapa 2. Mes 22: la cadena del mes 21 más la migración.
- Modo `solapada` (caso base): dentro de un eslabón los atrasos corren en paralelo y se toma el máximo; entre eslabones se suma. Modo `serie` (cota superior): se suman todos los atrasos de la cadena.
- Asignación a eslabones (datos del script). Levantamiento: R-11. Arquitectura: R-37. Plataforma base: R-20. Desarrollo Etapa 1: R-18, R-23. Certificación Etapa 1: R-16. Marcha blanca Etapa 1: R-02, R-12, R-24, R-34. Desarrollo Etapa 2: R-33. Migración y retiro 2011: R-01, R-13, R-25. Sin riesgos calificados en marcha blanca de la Etapa 2.
- P residual (Tabla 2): R-02 0,40; R-12 0,20; R-13 0,40; R-01 0,20; R-11 0,20; R-16 0,20; R-18 0,40; R-20 0,40; R-23 0,20; R-24 0,40; R-25 0,20; R-33 0,20; R-34 0,40; R-37 0,20.

## Tabla A. Valor esperado antes de la respuesta

| ID | P | Semanas | VE semanas | Horas | VE horas |
| :-- | --: | --: | --: | --: | --: |
| R-02 | 0,60 | 3 | 1,80 | 600 | 360 |
| R-12 | 0,60 | 4 | 2,40 | 1.280 | 768 |
| R-13 | 0,60 | 6 | 3,60 | 1.920 | 1.152 |
| R-01 | 0,40 | 4 | 1,60 | 960 | 384 |
| R-11 | 0,40 | 3 | 1,20 | 360 | 144 |
| R-16 | 0,40 | 4 | 1,60 | 640 | 256 |
| R-18 | 0,60 | 5 | 3,00 | 1.200 | 720 |
| R-20 | 0,60 | 4 | 2,40 | 640 | 384 |
| R-23 | 0,40 | 4 | 1,60 | 480 | 192 |
| R-24 | 0,60 | 3 | 1,80 | 960 | 576 |
| R-25 | 0,40 | 10 | 4,00 | 2.400 | 960 |
| R-33 | 0,40 | 3 | 1,20 | 600 | 240 |
| R-34 | 0,60 | 3 | 1,80 | 360 | 216 |
| R-37 | 0,40 | 3 | 1,20 | 360 | 144 |
| **Total** | | 59 | **29,20** | 12.760 | **6.496** |

## Tabla B. FMEA de la solución en operación

S, O y D de 1 a 10 (10 en D = pasa inadvertida). NPR = S x O x D. Estimaciones del proponente.

| Modo de falla | Efecto | S | O | D | NPR | Justificación |
| :-- | :-- | --: | --: | --: | --: | :-- |
| Emisión tributaria en contingencia (R-16) | La tienda no emite documentos en un corte; incumple restricción 5 o 6 | 9 | 4 | 4 | 144 | S: I = 5 pero acotada a la tienda con corte; O: P = 0,40 mientras la autoridad no apruebe la modalidad; D: se ve al mes 9 solo si se gestiona la aprobación |
| Sincronización del diario local (R-15) | Cobro doble o descuadre con ERP y DTE | 6 | 4 | 5 | 120 | S: I = 4 sin pérdida masiva; O: P = 0,40 con 14 tiendas por dimensionar; D: el descuadre aparece en la conciliación posterior, salvo la prueba de 24 h |
| Saturación en el peak del evento anual (R-09) | Pedidos cancelados en tres días | 7 | 4 | 4 | 112 | S: I = 4, repite el episodio de junio; O: P = 0,40 con memoria de capacidad no calculada; D: la prueba a 225.000 pedidos y el monitoreo la hacen visible |
| Cruce indebido de datos (R-03) | Se quiebra la línea roja entre retail y emisor | 10 | 2 | 3 | 60 | S: I = 5 por regla; O: P = 0,20 porque el control de cruces lo bloquea por diseño; D: cada cruce queda registrado y el umbral es cero |
| Caída del centro de datos DC-01 (R-31) | Se detienen emisión tributaria y crédito | 9 | 2 | 2 | 36 | S: I = 5 (restricciones 5 y 6); O: P = 0,20, evento local poco frecuente; D: la caída es inmediata y visible |

## Tabla C. Simulación del atraso acumulado (semanas)

10.000 iteraciones, semilla 20261012. Salida real del script.

Caso base, agregación solapada.

| Hito | Escenario | Media | P50 | P80 | P90 | P(atraso > 0) |
| :-- | :-- | --: | --: | --: | --: | --: |
| Mes 16 | Sin respuestas | 13,6 | 13,6 | 17,3 | 19,3 | 100 % |
| Mes 16 | Con respuestas | 8,5 | 8,3 | 12,2 | 14,3 | 96 % |
| Mes 21 | Sin respuestas | 1,2 | 0,0 | 3,0 | 3,4 | 39 % |
| Mes 21 | Con respuestas | 0,6 | 0,0 | 1,7 | 3,0 | 20 % |
| Mes 22 | Sin respuestas | 7,7 | 7,8 | 11,3 | 13,0 | 91 % |
| Mes 22 | Con respuestas | 4,8 | 4,8 | 8,5 | 10,6 | 69 % |

Cota superior, agregación en serie.

| Hito | Escenario | Media | P50 | P80 | P90 | P(atraso > 0) |
| :-- | :-- | --: | --: | --: | --: | --: |
| Mes 16 | Sin respuestas | 17,1 | 17,1 | 21,9 | 24,5 | 100 % |
| Mes 16 | Con respuestas | 9,6 | 9,4 | 13,8 | 16,4 | 96 % |
| Mes 21 | Sin respuestas | 1,2 | 0,0 | 3,0 | 3,4 | 39 % |
| Mes 21 | Con respuestas | 0,6 | 0,0 | 1,7 | 3,0 | 20 % |
| Mes 22 | Sin respuestas | 10,4 | 9,7 | 16,5 | 19,6 | 91 % |
| Mes 22 | Con respuestas | 5,7 | 4,9 | 10,0 | 13,3 | 69 % |

Interpretación: los hitos son contractuales. El P80 solapado con respuestas (12,2 / 1,7 / 8,5 semanas) es una estimación indicativa de exposición en plazo, no una reserva disponible ni una nueva fecha de hito. El P80 en serie (13,8 / 1,7 / 10,0) es la cota superior del modelo resumido. La capacidad para absorber el atraso se comprueba por rol y ventana con el T-15.

## Limitaciones

- Independencia. Los riesgos no se correlacionan (R-20 y R-31 comparten causa; R-23 y R-33 comparten equipo), lo que subestima la cola y a la vez la suma serial dentro del hito la sobrestima. El efecto neto no se midió.
- El solape dentro de un eslabón es un supuesto (los atrasos corren en paralelo sobre la misma ventana); la cota en serie lo desactiva. Aun así el P80 del mes 16 (12,2 semanas con respuestas) es alto para una etapa de 15 meses y debe contrastarse con el CPM y la capacidad por rol antes de comprometerlo.
- Todas las P, semanas, horas, puntajes S/O/D y la asignación a hitos son estimaciones del proponente, no datos del Caso.
- Red resumida de nueve eslabones y tres hitos, no las 164 cuentas de control ni los 11 eslabones de la Tabla 7.6 con sus holguras.
- El mes 21 solo recibe R-33 por ser la única amenaza calificada a la rama de la Etapa 2; los riesgos de la Etapa 2 de zona media quedan fuera.
- El FMEA cubre cinco modos de falla, no todo el registro.
- No hay dinero en ningún cálculo.
