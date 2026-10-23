# Guía: agregar cuatro cuentas de control a la EDT del sd-07 (PENDIENTE)

> **OBSOLETA desde el 2026-10-12.** La decisión D10 se revirtió: no se agregan cuentas a la EDT. Se conserva solo como registro. Ver `integracion_sd-07.md`.

Documento de contexto, no entregable. Creado el 2026-10-11. **Estado: falta hacerlo.** Nace de la decisión D10 del sd-08: R-06, R-27, R-28 y R-36 tienen una respuesta sin cuenta de la EDT donde ejecutarla. Hasta que las cuentas existan en el sd-07, el 8.3 no puede nombrarlas. Si esta guía difiere de los archivos que cita, mandan los archivos.

**Quién:** el responsable del sd-07 (el sd-08 no edita otro subdocumento). Avisar antes de tocar.

## 1. Las cuatro cuentas propuestas

Códigos tentativos: son el siguiente número libre de cada rama a 2026-10-11 (máximos actuales: 1.2.10, 1.6.12, 1.7.14). Confirmar contra `14_edt_corregida.md` antes de asignar, porque los números saltan por las divisiones previas.

| Riesgo | Código tentativo | Nombre sugerido | Etapa | Responsable (rol) | Ventana |
| :-- | :-- | :-- | :-- | :-- | :-- |
| R-06 | 1.2.11 | Acuerdo con la filial emisora sobre la regla de comisión del vendedor | 1 | Jefe de Proyecto (acepta la filial emisora) | Antes del mes 13; el riesgo golpea desde el mes 16 |
| R-27 | 1.2.12 | Acuerdos de cooperación y salida con los proveedores de las plataformas que se reemplazan | desde el inicio del contrato | Jefe de Proyecto (el cliente firma, es su contrato) | Meses 1 a 4, antes de la línea base de alcance |
| R-28 | 1.7.15 | Medida transitoria de retención de grabaciones de repactación | desde el inicio del contrato | Arquitecto o responsable de datos; decide el cliente | Antes del mes 16 (cuanto antes, el pasivo crece) |
| R-36 | 1.6.13 | Plan de incorporación de transportistas y vendedores de marketplace a los contratos de estado | 2 | Por definir con el sd-12 | Antes del desarrollo de pedidos y marketplace |

Lo que cada una entrega y acepta (dejarlo en el diccionario, no en esta tabla):
- **1.2.11:** acta firmada con la regla de comisión acordada. Aceptación: firma de la filial emisora antes del mes 13. Análoga a 1.2.10 (criterios del cupo preaprobado), que ya está en el mismo bloque.
- **1.2.12:** cartas o contratos de cooperación con los seis proveedores actuales, con documentación de interfaces y extracción de datos. Aceptación: documentación entregada por proveedor.
- **1.7.15:** especificación de retención y acta de decisión del cliente para cambiar su política de 90 días. Barata; solo especifica y acompaña.
- **1.6.13:** plan de incorporación con calendario por transportista y por vendedor de marketplace, y medición del 97 % de trazabilidad de entrega.

## 2. Qué archivos tocar, en orden

Todos en `80_Artefactos/sd-07_contexto/estimacion/` salvo el `.tex`. Leer antes `guia_edt.md` §1 y §2: «Ante un vacío se escribe “por definir”; nunca se inventa una cifra».

1. **`14_edt_corregida.md`** (fuente de la EDT). Agregar cada cuenta con el mismo formato que las vecinas:
   `- 1.2.11 <nombre> {ucp: no; nivel: cuenta de control; etapa: 1; origen: <fuente>}`
   Actualizar el encabezado de la rama («12 cuentas de control» pasa a 13, etc.) y la fila de resumen de la rama (por ejemplo `1.2 | 8 → 10`). Total de cuentas: 164 → 168.
2. **`15_mapa_paquetes_ucp.md`:** las cuatro llevan `ucp: no`, así que no entran en el mapa de casos. Comprobar con `python3 05_Gestion/scripts/generar_mapa_paquetes.py --help` y regenerar solo si el script lo exige.
3. **`12_plantilla_tres_valores.md` y `16_horas_por_paquete.md`:** como `ucp: no`, se estiman con los tres valores (optimista, más probable, pesimista) y la técnica PERT. Agregar las cuatro filas y estimarlas. **No inventar horas**: si el equipo no las ha estimado, dejar «por estimar». Regenerar con `generar_plantilla_tres_valores.py` y `repartir_horas_paquetes.py`.
4. **`19_diccionario_campos_manuales.md`:** escribir entregable, criterio de aceptación y responsable de cada cuenta (los tres que exige el Comunicado 10). Luego regenerar `18_diccionario_edt.md` con `generar_diccionario.py`; no se edita a mano.
5. **`17_cronograma_edt.md`:** regenerar con `generar_cronograma.py` con las ventanas de la tabla 1. Revisar que ninguna cuenta caiga en un congelamiento ni empuje la ruta crítica.
6. **`22_coherencia_edt_sd03.md`:** correr `verificar_coherencia_edt_sd03.py`. Las cuentas con origen en el sd-03 deben remitir al texto correspondiente (SP-01 para R-27; 3.4.3 y 3.4.6 para R-36).
7. **`02_Propuesta/latex_final/sd-07/OSS-Subdocumento7.tex`:** es lo único que entrega el informe. Cambiar:
   - l. 157: «las quince ramas suman 164 cuentas de control» pasa a 168 (las ramas siguen siendo quince).
   - Tabla 7.1 (l. 130 y siguientes): cuentas por rama 1.2, 1.6 y 1.7.
   - l. 188: las 31.850 horas son solo las del UCP. Si se estiman horas para las cuatro cuentas, agregarlas al reparto de la Tabla 7.2; si no, aclarar que no están incluidas.
   - Tabla 7.4 (frentes): ubicar las cuentas en su frente.
   - Si la ventana de 1.2.12 o 1.2.11 está antes del mes 4 o 13, mencionarla en 7.3 (línea base de alcance, mes 4).
   - Formulario T-14 (despliegue completo): agregar las cuatro filas si el formulario se exporta del diccionario.
8. **Verificar:** `python3 05_Gestion/scripts/verificar_edt.py`, luego `exportar_latex.py verificar --parte T7-07` y `verificar-redaccion --parte T7-07`. Las pruebas del exportador no cambian: `python3 -m unittest discover -s 05_Gestion/tests -v`.

Las opciones exactas de cada script no se revisaron al escribir esta guía: correr cada uno con `--help` antes de usarlo.

## 3. Efectos en el resto

- **sd-08:** el 8.3 nombra las cuatro cuentas por código y nombre. Si el sd-07 cambia los códigos, actualizar el 8.3 y el T-16.
- **Reserva de contingencia (F4):** sus horas entran en la tabla de valor esperado.
- **Ruta crítica del sd-07 (Tabla 7.6):** ninguna de las cuatro debería entrar en la ruta crítica; si 1.2.12 retrasa la línea base del mes 4, sí. Comprobar.
- **Avisos:** registrar en `avisos_otros_subdocumentos.md` como pendiente del sd-07 junto a I-03 (marcha blanca) y D9 (holgura del evento anual).
- **Alternativa si no hay tiempo antes del 12-10:** nombrar cada respuesta en el 8.3 como «cuenta nueva propuesta al sd-07» y dejarlo declarado. Es honesto, pero el evaluador puede objetarlo como acción sin dueño.

## 4. Lo que no cubre esta guía

- Las horas de las cuatro cuentas. Dependen de la estimación del sd-07 y del sd-12.
- Los responsables nominales (la EDT usa roles, no nombres).
- Si R-06 se reformula (las dos caras del conflicto del vendedor; ver `trazabilidad_riesgos.md` §4.1), el nombre de 1.2.11 puede cambiar.

## 5. Pendiente adicional del sd-07 (D9, grado 1)

Agregar **una frase** en el apartado 7.3 (cerca de l. 277 y 305 del `.tex`, donde dice que la ruta crítica «no admite holgura») que remita al 8.3: las anclas contractuales no se mueven, la reserva de contingencia en semanas del sd-08 se obtiene tomando fechas internas más tempranas dentro de las ventanas existentes, y ese margen no está en la EDT ni en la Tabla 7.6. No se agregan fechas internas, hitos ni cuentas. Si F4 muestra que hace falta, se sube al grado 2 (fechas internas en Tabla 7.6, Gantt y `17_cronograma_edt.md`); eso sería una decisión nueva.
