# Red del SD-07 v3: medida preventiva de la capacitación E2 (2026-11-10)

Documento de trabajo, no entregable. **Insumo vigente** de horas, dotación y calendario. Es la red v2 (`../red-sd04-v2-2026-11-10/`, traspaso completo del SD-04) más una sola decisión del paso D (`../compresion-2026-11-10/`).

## Decisión (usuario, 2026-11-10): opción A con B de respaldo

En la v2, la capacitación E2 (1.13.3) era el punto más frágil: 1.920 HH en 9 días con 36 personas, desde H9 y con holgura cero. Un atraso de 10 días movía H11, H12 y el inicio de la operación en 14 días.

- **A.** Se adelanta el **30 % (576 HH)** que no depende del software E2 terminado: procesos y reglas de E2, cambios de rol, módulos compartidos con E1 y **formación de formadores**. Se hace en **M17** (8 al 27 de mayo de 2028), con 6 personas y después del diseño aprobado en H8. El **70 % (1.344 HH)** queda desde H9 sobre el software con QA, con las mismas 36 personas en 6 días.
- **B.** Los formadores formados en M17 quedan como reserva para duplicar la dotación si hay atraso. No cambia la red.
- **Descartadas:**
  - capacitar sobre una versión sin QA antes de H9 (obliga a recapacitar y contradice el SD-07);
  - alargar la ventana (está limitada por H9 al inicio y por la marcha blanca al final).

## Efecto

| | v2 | v3 |
| :-- | :-- | :-- |
| Holgura de la capacitación sobre el software | 0 | **3 días** (la parte anticipada tiene 7) |
| S7 sin respuesta (atraso de 10 días) | +14 días en H11 y H12 | **+11** |
| S7 con intensificación | +4 | **+1** |
| S7 con intensificación + horas extra | Recupera; +288 HH y unas 192 equivalentes por recargo | **Recupera; +202 HH y unas 134 equivalentes** |
| Total de HH | 239.250,01 | **239.250,01** (solo cambian las fechas; FTE de M17 de 27,1 a 30,3 y de M18 de 13,9 a 10,7) |

Los escenarios S1 a S6b dan los mismos resultados que en la v2 (`escenarios_resultado_v3.json`).

## Validación

Motor CPM y comprobaciones del verificador:
- 0 actividades tardías;
- 0 violaciones de precedencia;
- H1–H12 idénticos al original;
- marchas blancas intactas;
- 22 tiendas el 7 de abril de 2028.

Estabilización con margen de 10 días: 77 actividades movidas.

## Archivos

| Archivo | Contenido |
| :-- | :-- |
| `ajuste_capacitacion_e2.py` | Divide 1.13.3 E2 sobre la red v2. Uso: `python3 -I ajuste_capacitacion_e2.py <v2>/Red_CPM Red_CPM` |
| `Red_CPM/` | Red v3 (978 nodos) |
| `estabilizacion.json` | Inicios preferidos (margen de 10 días) |
| Matrices por rol y por perfil del E-26, `HH_paquete_x_perfil_E26.csv`, `HH_por_paquete_EDT.csv` | Igual formato que la v2; copiadas a `Economica/insumos-sd07/` |
| `escenarios_resultado_v3.json` | Los 8 escenarios del paso D sobre la v3 |

| `estabilizar.py` | Versión de la v3: agrega un piso para que ninguna actividad de la Etapa 2 o de su marcha blanca empiece antes de M13 (7 de enero de 2028, Art. 17) |
| `programacion_v3.csv` | Programación estabilizada por actividad, base de las figuras diag-07-0* |

Los scripts de matrices y equivalencia son los de `../red-sd04-v2-2026-11-10/`, aplicados a esta red. La estabilización usa `estabilizar.py` de esta carpeta.

**Corrección del 2026-11-10 (piso de la Etapa 2).** La primera estabilización adelantó a M12 (7 de diciembre de 2027) la actividad 1.9.12 E2, «Pruebas de comprensión con clientes y titulares · E2», de 22 HH, hasta su inicio temprano. Ese mes es anterior al período contractual de la Etapa 2. Con el piso, la actividad queda el 14 de julio de 2028 (M19), dentro de su holgura. Las otras 76 actividades movidas, los hitos, el total de HH y los 8 escenarios del paso D no cambian. Cambian 22 HH entre meses: M12 baja y M19 sube.
