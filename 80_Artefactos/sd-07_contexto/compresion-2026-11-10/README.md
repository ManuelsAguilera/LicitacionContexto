# Respuestas ante atrasos en la ruta crítica · paso D (2026-11-10)

Documento de trabajo, no entregable. Insumo para redactar el SD-07 §7.3.3 (ruta crítica y holguras) y la hoja de Sensibilidad del modelo financiero. Red analizada: `../red-sd04-v2-2026-11-10/` (estabilizada con margen de 10 días).

## Diagnóstico

- La **ruta crítica del contrato está impuesta por fechas**: las cadenas con holgura cero hacia H7 y H12 son ventanas de duración fija (marcha blanca E1 de 3 meses y E2 de 2 meses, Art. 17.3; capacitación; entrada a tiendas). Hacia H5 y H10 solo hay revisiones del cliente. Esas ventanas no se comprimen.
- El riesgo está en el **trabajo casi crítico que llega a esas ventanas**: 343 actividades con margen de 10 días o menos. Se agruparon en 7 frentes, de los que salen los escenarios.

## Método (PMBOK 6.5.2.4 y 6.5.2.6; supuestos validados por el usuario)

- **«¿Qué pasa si…?»:** la actividad que dispara el escenario se atrasa 10 días hábiles (14 días corridos si es un plazo de proveedor). El motor CPM del equipo recalcula la programación estabilizada.
- **Intensificación:** hasta el doble de personas; **+15 % de HH** sobre lo comprimido por rendimientos decrecientes (PMBOK p. 197).
- **Ejecución rápida:** solo sobre dependencias discrecionales (PMBOK p. 191). Una relación FS pasa a SS con un desfase del 50 % de la predecesora; **+10 % de HH** de retrabajo en la sucesora.
- **Horas extra** (solo en S7): 2 h diarias con el recargo legal del 50 % (Código del Trabajo, art. 32). La duración baja a 0,8 y el costo sube en el equivalente al 10 % de las HH.

## Resultados

| Escenario | Sin respuesta | Respuesta que recupera la fecha | HH extra | Riesgo agregado |
| :-- | :-- | :-- | --: | :-- |
| S1 Levantamiento (1.2.2, 915 HH) | 1.2.2 y 1.2.3 terminan 13 días después de su fecha límite; expediente de H1 incompleto | Intensificación (doble de analistas) | 137 | Coordinación de un equipo nuevo en M1 |
| S2 Nube base (1.4.1, 620 HH) | Ambientes (1.4.4) 10 días tarde; H3 en riesgo | Intensificación (doble de SRE). La ejecución rápida no sirve: la dependencia es obligatoria | 93 | Bajo |
| S3 Construcción E1 (1.5.36.1) | Lo absorbe el margen | — | 0 | — |
| S4 Entrega de UPS del lote 1 (+2 semanas) | Prueba de corte del piloto 9 días después del 7 de julio de 2027 (fuera de M6–M7) | Ejecución rápida: la pila local empieza a mitad de la instalación física. La intensificación no sirve: el atraso es del proveedor | 29 | Retrabajo si la instalación cambia |
| S5 Corte de inventario (1.7.3) | Lo absorbe el margen | — | 0 | — |
| S6 Construcción E2 (1.5.22.1) | Lo absorbe el margen | — | 0 | — |
| S6b Innovación E2 (1.10.4.6) | H10, H11 y H12 se atrasan 6 días | Intensificación | 30 | Bajo |
| S7 Capacitación E2 (1.13.3, 1.920 HH, 36 personas en 9 días) | H11, H12, cierre de la marcha blanca E2 e inicio de la operación se atrasan **14 días** | Intensificación sola: quedan 4 días. **Intensificación + horas extra**: recupera la fecha | 288 + 192 equivalentes por recargo | El doble de formadores (72) y fatiga |

## Conclusiones

1. De 8 escenarios, **3 se absorben con el margen** y **5 tienen una respuesta que recupera la fecha**. La respuesta depende del tipo de atraso: intensificación si el trabajo es propio, ejecución rápida si el atraso es de un proveedor y no hay dependencia obligatoria.
2. **El punto más frágil es la capacitación E2 (S7)**. Ya está comprimida (36 personas en 9 días, frente a 6 personas en 51 días en E1) y su atraso mueve el inicio de la operación (M21). Requiere una medida preventiva (decisión pendiente).
3. **Costo de todas las respuestas:** unas 577 HH, más 192 de costo equivalente por horas extra. Debe cruzarse con los 14 riesgos que respalda la contingencia de 3.688 HH (SD-08).

## Archivos

| Archivo | Contenido |
| :-- | :-- |
| `escenarios.py` | Ejecuta los escenarios con el motor del equipo. Uso: `python3 -I escenarios.py <traspaso> <dir con Red_CPM y estabilizacion.json>` |
| `escenarios_resultado.json` | Resultado por escenario y respuesta: hitos atrasados, actividades tardías y HH extra |

## Decisión sobre S7 y resultado (red v3)

El usuario eligió la **opción A con B de respaldo**: adelantar a M17 el 30 % de la capacitación E2 que no depende del software (procesos, roles, módulos compartidos y formación de formadores), y usar a esos formadores como reserva para duplicar la dotación si hay atraso. Sobre la red v3 (`../red-v3-2026-11-10/`):

- la capacitación sobre el software pasa de 0 a 3 días de holgura;
- S7 sin respuesta baja de +14 a +11 días; con intensificación queda en +1 día;
- con intensificación más horas extra se recupera la fecha con +202 HH y unas 134 equivalentes (antes 288 y 192).

El total de horas no cambia (239.250,01). Los escenarios S1 a S6b dan los mismos resultados.

## Escenarios S8–S12: actividades que llegan a la revisión del cliente (red v3, 2026-11-11)

Agregados tras la revisión del hilo lógico: el criterio de 10 días de margen dejaba fuera las actividades más ajustadas. Mismo método (atraso de 10 días hábiles, intensificación ≤ 2× y +15 % HH, horas extra con duración × 0,8 y recargo equivalente al 10 % de las HH). Script: `escenarios_ajustadas_v3.py` (uso: `python3 -I escenarios_ajustadas_v3.py <traspaso> red-v3-2026-11-10 escenarios.py`, desde `80_Artefactos/sd-07_contexto/`).

| Escenario | Holgura | Sin respuesta | Respuesta | HH | Recargo equiv. |
| :-- | --: | :-- | :-- | --: | --: |
| S8 Capacitación E1 (1.13.3, 1.950 HH) | 2 | H6, H7, H12 +12 | Intensificación | 292,5 | — |
| S9 Aceptación 28 criterios E1 (1.9.6, 121,34 HH) | 2 | H5, H6, H7, H12 +11 | Intensificación | 18,2 | — |
| S10 Pruebas lockers (1.10.1.6, 52 HH) | 2 | H10–H12 +8 | Intensificación | 7,8 | — |
| S11 Pruebas modo tienda (1.10.5.6, 165,33 HH) | 2 | H10–H12 +8 | Intensificación | 24,8 | — |
| S12 Aceptación 28 criterios E2 (1.9.6, 121,33 HH) | 1 | H10–H12 +13 | Intensificación + horas extra (solo intensificación deja +1) | 18,2 | 12,1 |

Total de respuestas S1–S12: 853 HH (491 + 362) y unas 147 HH equivalentes por recargo (134 + 12).
