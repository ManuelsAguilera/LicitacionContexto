# Inventario de cambios para el paso T (2026-11-10)

Documento de trabajo, no entregable. Lista qué entra en cada sección del SD-07, del T-14 y del T-15 cuando llegue la fuente exacta de noviembre (zip de Prism), desde qué borrador o dato, y cómo se comprueba. Sirve para que el traspaso sea mecánico y verificable.

## 0. Condición previa y procedimiento (AGENTS.md y skill `exportar`)

1. Recibir el zip de Prism del SD-07 (y del T-14 y T-15 si se editaron en Prism).
2. `python3 05_Gestion/scripts/exportar_latex.py doctor`, después `estado`.
3. `prism-importar --parte T7-07 --zip <archivo> --dry-run`. Revisar el informe y después importar. Si pide `--forzar`, solo con instrucción explícita del usuario.
4. Editar **solo el cuerpo** del `.tex`; nunca el preámbulo. Copiar las figuras nuevas de `04_Adjuntos/diagramas/diag-07-0*` a `latex_final/figuras/`.
5. Comprobaciones finales (sección 5) y compilación con `compilar --parte T7-07`.

Los formularios T-14 y T-15 están en `latex_final/Formularios/`. Sus versiones de noviembre (234.493 HH) están en el traspaso y no en el repositorio, así que también entran por la vía que indique el usuario.

## 1. Cifras que cambian en todo el SD-07

Buscar y reemplazar cada aparición, comprobando el contexto.

| Dato | Valor en el PDF de noviembre | Valor vigente | Fuente |
| :-- | :-- | :-- | :-- |
| HH base | 234.493,47 | **239.250,01** | `red-v3-2026-11-10/README.md` |
| HH con contingencia | 238.181,47 | **242.938,01** | 239.250,01 + 3.688 |
| Nodos y relaciones de la red | 853 y 1.836 | **978 y 2.127** | `red-v3-2026-11-10/Red_CPM/` |
| Elementos de tercer nivel de la EDT | 164 (56 cuentas y 108 paquetes) | **176 (56 cuentas y 120 paquetes)** | 12 paquetes nuevos: 1.4.14 a 1.4.24 y 1.8.9 |
| Elementos totales de la EDT | 331 | **343** | 176 + 167 paquetes en cuentas |
| Paquetes de la rama 1.4 | 13 | **24** | Red v2 |
| Paquetes de la rama 1.8 | 8 | **9** | Red v2 |
| «13 tiendas» en 1.4.2 | 13 tiendas | **22 tiendas, 2 CD y laboratorio (25 sitios)** | Red v2 |
| Entorno de 1.4.3 | ámbito emisor | **Filial y Control de cruces** | Red v2 |
| Holguras de hitos (Tabla 7.7) | 4, 21, 30, 31, 0, 0, 0, 29, 31, 0, 0, 0 | **Sin cambio** | Verificado en la v3 |
| Personas en solapamientos | personas distintas (por ejemplo, pico de 147) | **Personas equivalentes (FTE)**, decisión del paso B | Matriz FTE v3 |

## 2. SD-07 sección por sección

| Sección | Cambio | Desde | Comprobación |
| :-- | :-- | :-- | :-- |
| Introducción del capítulo | Mencionar la carta Gantt en tres niveles y el detalle en el anexo T-14 | Borrador G | RR-03 |
| 7.1.1 Criterios de descomposición | Cifras de elementos (176 y 343) y paquetes de 1.4 y 1.8 | Sección 1 de este inventario | Sumas cuadran |
| 7.1.2 Estructura de la EDT | **Figura 7.1** con 1.4 = 24 y 1.8 = 9. **Tabla 7.1**: filas 1.4 y 1.8 (elementos, entregable ampliado con instalación física, datos y controles) | Red v2; cruce SD-04 (fase 2) | Tabla cuadra con el T-14 |
| 7.1.3.4 Rama 1.4 | Texto y **Figura 7.5** con los 11 paquetes nuevos: levantamiento, suministro, laboratorio, piloto, instalación, recuperación, datos, DC-01, pila local y replicación | `red-sd04-v2-2026-11-10/README.md` | Nombres idénticos al SD-04 (RR-07) |
| 7.1.3.8 Rama 1.8 | Texto y **Figura 7.9** con 1.8.9 Controles de seguridad desplegados | Ídem | Ídem |
| 7.1.3.13 Rama 1.13 | Capacitación E2 en dos partes (M17 y desde H9) | `red-v3-2026-11-10/README.md` | — |
| 7.2.1 Secuenciamiento y estimación | Método idéntico. Agregar que el traspaso del SD-04 se estimó con unidad × PERT y que las HH suben a 239.250,01. **Tabla 7.2** recalculada por etapa con la red v3 | Red v3; script de HH por mes del traspaso adaptado | Total de la Tabla 7.2 = 239.250,01 |
| 7.2.3 / Tabla 7.5 | Personas en FTE por etapa (no personas distintas) | Matriz FTE v3 | — |
| 7.2.4.1 Capacidad en solapamientos | Párrafos y **Figura 7.17** (histograma) | Borrador G | RR-10/11/14 |
| 7.3.2 Calendario | Agregar el levantamiento físico (M1–M2) y las compras de DC-01, lote 1 y lote 2, con su relación con H1 y H2 | `red-sd04-v2-2026-11-10/README.md` (tabla R4) | Fechas iguales a la red |
| 7.3.3 Ruta crítica y holguras | Reemplazar el párrafo de medidas de recuperación y la curva. Agregar **§7.3.3.2** con la **Tabla 7.9** de escenarios. Regenerar la figura de la curva mensual (239.250,01) | Borrador 7.3.3 | Cifras = `compresion-2026-11-10` |
| 7.3.4 Carta Gantt | Texto de caída, **Figuras 7.18 y 7.19**. Retirar las 22 láminas del cuerpo y la Tabla 7.8 | Borrador G | Cuerpo con 3 figuras de cronograma |
| 7.3.4.1 a 7.3.4.4 | 7.3.4.1–7.3.4.3 se conservan con fechas verificadas. 7.3.4.4 pasa a remitir al anexo T-14 | — | RR-01 (títulos se mantienen) |
| 7.3.5 y 7.3.5.1 | Estrategia nombrada, **Tablas 7.10 y 7.11**, pruebas y criterios medibles | Borrador H | Folios del caso (p. 31, 34 y 44) |
| 7.3.6 | **Tabla 7.12** con las condiciones del Art. 17.3 y su umbral | Borrador H | — |
| Referencias | Caso 09 con los folios usados (cap. 14 p. 31; cap. 15 p. 34; cap. 18 p. 44). Sin cita del PMBOK (decisión pendiente; sugerencia: no citar) | Skill `citas-proyecto` | Cada cita con su folio |
| Declaración de uso de IA | Actualizar con el uso de esta sesión (análisis de red, figuras, borradores) | — | RR-23 (no declarar revisión humana que no ocurrió) |

## 3. Formulario T-14

| Sección | Cambio | Desde |
| :-- | :-- | :-- |
| Método de estimación | Mismo método. Agregar los componentes nuevos y ajustados con unidad, cantidad y O/M/P | `red-sd04-v2-2026-11-10/Red_CPM/componentes_v2.json` |
| Diccionario, rama 1.4 | 1.4.2 y 1.4.3 actualizados. 11 filas nuevas (1.4.14 a 1.4.24) con entregable, criterio de aceptación, responsable, HH y ventana | `HH_por_paquete_EDT.csv` (v3) y `red-sd04-v2-2026-11-10/README.md` |
| Diccionario, rama 1.8 | Fila nueva 1.8.9; 1.8.4 con 3 frentes | Ídem |
| Diccionario, rama 1.13 | 1.13.3 en dos partes | `red-v3-2026-11-10/README.md` |
| Diccionario, ramas 1.10.1 y 1.10.5 | Compra de lockers y tótems (órdenes y entrega) | Ídem |
| Carta Gantt | **18 láminas** `diag-07-04_gantt-rama-*` y tabla índice T14.1 | Borrador G (sección del anexo) |

## 4. Formulario T-15

| Sección | Cambio | Desde |
| :-- | :-- | :-- |
| Base y método | Componentes nuevos (unidad × PERT) | `componentes_v2.json` |
| Conciliación del presupuesto | Total 239.250,01; desglose v2 y v3 | `conciliacion-hh-2026-11-10.md` (§7) |
| HH por tareas y paquetes | Filas de 1.4, 1.8, 1.10 y 1.13 actualizadas y nuevas | `HH_por_paquete_EDT.csv` |
| Curva de horas hombre | Regenerar con la red v3 | Matriz HH v3 |
| Dotación y frentes | FTE por perfil y por mes; solapamientos M13–M15 y M19–M20 estabilizados | Matrices FTE v3 y Figura 7.17 |
| Reservas de capacidad y nivelación | Resultado de la estabilización (margen de 10 días, 77 actividades, pico de M15 de 46,3 a 30,9) | `estabilizacion-2026-11-10/README.md` y v3 |
| Ruta crítica y holguras | Agregar la prueba de corte del piloto (sin holgura) y la capacitación E2 (3 días) | Red v3 |
| Duraciones, fechas y holguras por rama | Regenerar la tabla desde la programación v3 | `programacion_v3.csv` |
| Contingencia de riesgos | Agregar las respuestas de compresión (491 HH más 134 equivalentes) y su cruce con los riesgos del SD-08 | `compresion-2026-11-10/README.md` |

## 5. Comprobaciones después del traspaso

1. `exportar_latex.py verificar` (plantilla intacta) y `verificar-redaccion --parte T7-07` (reglas RR).
2. Buscar en el `.tex` que no queden 234.493, 238.181, 40.946, «853 nodos», «1.836 relaciones», «13 tiendas» ni «ámbito emisor».
3. Cada figura y tabla nueva citada antes de aparecer y explicada después (RR-11, RR-19); sin dos puntos dentro de las oraciones (RR-25).
4. Lector de prueba de la skill `proposito-documento` sobre el PDF compilado; las 10 preguntas de la ficha del SD-07 deben quedar respondidas.
5. Consistencia entre documentos: HH iguales en SD-07, T-14 y T-15; paquetes de 1.4 iguales al SD-04; contingencia coherente con el SD-08.
6. `compilar --parte T7-07` y revisión humana. El estado «revisado» lo asigna solo una persona.

## 6. Pendientes fuera del SD-07

| Documento | Pendiente |
| :-- | :-- |
| SD-08 | Cruzar los 5 escenarios con respuesta contra los 14 riesgos que respaldan la contingencia |
| SD-09 | Confirmar el percentil de medición de RT-09.01 |
| SD-10 y SD-12 | Validar las 26 personas de operación y los perfiles (hoy supuesto declarado) |
| SD-11 y SD-14 | Volumen operacional y resultados de negocio (hoy no existen) |
| Figuras de ramas de la EDT (7.5 y 7.9) | Regenerar con los paquetes nuevos. Son diagramas de árbol fuera del catálogo de `diagramas-ancoa`, así que requieren la misma excepción autorizada para los cronogramas o la herramienta original del equipo |
