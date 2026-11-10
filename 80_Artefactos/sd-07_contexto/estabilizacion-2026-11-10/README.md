# Estabilización de recursos del SD-07 (2026-11-10)

Documento de trabajo, no entregable. Paso B del plan del SD-07: histograma por rol y mes y análisis de nivelación de los solapamientos M13–M15 y M19–M20. Parte de los datos de `../traspaso-2026-11-10/` y de la conciliación `../conciliacion-hh-2026-11-10.md`.

## Técnica

Se aplica **estabilización de recursos** (PMBOK 6.5.2.3, p. 211): las actividades se mueven solo dentro de su holgura, entre su inicio temprano (ES) y su inicio tardío (LS). No cambian la ruta crítica ni la fecha final.

- **Motor:** el CPM del equipo (`motor_cpm_verificado_20261105.py`, en el traspaso), con su preferencia de inicio (`proposed_start`). El script no altera duraciones, HH, relaciones ni calendarios.
- **Objetivo:** minimizar la suma de cuadrados de las HH mensuales **por grupo de roles** (desarrollo, arquitectura, análisis, calidad, datos, plataforma y otros) en M13–M18. La cobertura de campo de M16 no entra, porque son otras personas.
- **Margen mínimo:** cada actividad desplazada conserva al menos **10 días hábiles** entre su nuevo inicio y su inicio tardío, o el margen que ya tenía si era menor. Así la estabilización no deja actividades sin colchón ante atrasos.
- **Candidatas:** 211 actividades con HH y holgura que tocan M13–M18. Se movieron 72, con 10.489,51 HH.

## Validación

Se aplican sobre la nueva programación las mismas comprobaciones del verificador del traspaso (`verificar_paquete.py`):

- 0 violaciones de precedencia (FS, SS y FF con desfases y calendarios);
- 0 actividades después de su fecha límite y 0 después de su inicio tardío;
- H1–H12, el cierre del contrato (M56) y el fin de las marchas blancas E1 y E2 sin cambios;
- 22 tiendas inician el 7 de abril de 2028 (H7);
- total de HH conservado: 234.493,47.

**No revalidado:** las cuotas por persona (8 HH por día, 40 por semana y 160 por mes). El registro diario por persona del traspaso no se regeneró para las actividades movidas; la matriz reparte sus HH de forma uniforme en sus días hábiles. Como la carga mensual por grupo baja, la presión sobre esas cuotas disminuye, pero no está demostrado persona por persona.

## Resultado (FTE = HH ÷ 160)

| Mes | Total antes | Total después | Desarrolladores antes | Desarrolladores después |
| :-- | --: | --: | --: | --: |
| M13 | 40,3 | 32,7 | 0,0 | 0,0 |
| M14 | 21,7 | 21,8 | 4,4 | 4,4 |
| M15 | **52,1** | **37,2** | **27,0** | **22,1** |
| M16 | 93,4 | 106,7 | 14,6 | 19,3 |
| M17 | 18,8 | 27,1 | 3,3 | 3,6 |
| M18 | 13,1 | 13,9 | 0,0 | 0,0 |

M16 incluye 67 FTE de cobertura de campo (88 implantadores y 88 formadores durante dos semanas), que son otras personas. En M16 el aumento corresponde a desarrolladores de la Etapa 2.

En el trabajo técnico de M13–M18 (incluida la coordinación del líder técnico), el pico baja de 50,7 a 39,0 FTE y la desviación estándar de 13,2 a 9,0.

## Margen conservado

Las 72 actividades movidas conservan al menos 10 días hábiles de margen (mínimo 10, mediana 10). Ninguna queda en su inicio tardío.

**Alternativa descartada:** sin margen mínimo, el pico técnico bajaba a unos 34 FTE, pero 16 actividades (2.483 HH) quedaban en su inicio tardío y la mediana de margen era de 3 días. Se descartó porque convertía en críticas actividades de H9 y H10.

## Archivos

| Archivo | Contenido |
| :-- | :-- |
| `estabilizar.py` | Estabilización con el motor del equipo. Uso: `python3 -I estabilizar.py <Red_CPM> <Datos_base> estabilizacion.json 10` (el último argumento es el margen mínimo) |
| `matriz_estabilizada.py` | Matrices por rol: resta las HH reales de las actividades movidas y suma su nueva distribución |
| `estabilizacion.json` | Inicios preferidos, actividades movidas (antes, después, ES, LS, HH) y totales por mes y grupo |
| `HH_matriz_roles_M1_M56_estabilizada.csv` | HH por rol (37 roles del E-26) y por mes; `;` y coma decimal |
| `FTE_matriz_roles_M1_M56_estabilizada.csv` | Lo mismo en FTE (HH ÷ 160). **Insumo de dotación del modelo financiero** |

Los scripts requieren la carpeta `Red_CPM/verificacion/` del traspaso (el motor), que no está versionada.
