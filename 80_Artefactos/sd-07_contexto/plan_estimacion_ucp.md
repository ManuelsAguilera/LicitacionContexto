# Plan de estimación por Puntos de Casos de Uso (estado)

Documento de contexto, no es entregable. Fecha de la última actualización: 2026-10-08. Resume la ruta, las puertas de validación y el estado de cada paso. El detalle del método está en la clase FEP03 (diapositivas 21 a 52). Los artefactos de cada paso están en `estimacion/`. La numeración de los pasos es la de `prompt_estimacion_ucp.md`.

## Cómo correr las pruebas

```bash
python3 05_Gestion/scripts/verificar_coherencia_sd03.py        # puerta G0, solo informa
python3 05_Gestion/scripts/verificar_actores.py                # puerta G2a, solo informa
python3 05_Gestion/scripts/verificar_casos_uso.py --completo   # puerta G3 (P3.1 a P3.7)
python3 05_Gestion/scripts/generar_entrada_ucp.py              # paso 4, primera vía: escribe 07_entrada_calculadora.json
python3 05_Gestion/scripts/recalcular_uucp.py                  # paso 4, segunda vía independiente
python3 05_Gestion/scripts/calcular_esfuerzo.py                # paso 6: regenera 10_esfuerzo.md con dos vías
python3 05_Gestion/scripts/comparar_metodos.py A.md B.md       # paso 7: compara el segundo método (por paquete) con el UCP
python3 05_Gestion/scripts/verificar_edt.py [EDT.md]           # paso 8a: controles mecánicos de la EDT (por defecto la de Eliseo)
python3 05_Gestion/scripts/verificar_edt.py 80_Artefactos/sd-07_contexto/estimacion/14_edt_corregida.md
python3 05_Gestion/scripts/generar_mapa_paquetes.py            # paso 8c: regenera 15_mapa_paquetes_ucp.md
python3 05_Gestion/scripts/generar_plantilla_tres_valores.py   # paso 8d: regenera 12_plantilla_tres_valores.md
python3 05_Gestion/scripts/repartir_horas_paquetes.py [A.md B.md]  # paso 9: regenera 16_horas_por_paquete.md
python3 05_Gestion/scripts/generar_cronograma.py               # paso 10: regenera 17_cronograma_edt.md
python3 05_Gestion/scripts/generar_diccionario.py [A.md B.md]  # paso 10b: regenera 18_diccionario_edt.md (aplica 19_diccionario_campos_manuales.md)
python3 05_Gestion/scripts/evaluar_tamano_paquetes.py [A.md]   # paso 10c: regenera 20_evaluacion_8_80.md
python3 05_Gestion/scripts/verificar_coherencia_edt_sd03.py     # paso 10d: coherencia con el sd-03; regenera 22_coherencia_edt_sd03.md
python3 -m unittest discover -s 05_Gestion/tests -p 'test_estimacion.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_casos_uso.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_g4.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_tcf.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_ef.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_esfuerzo.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_comparar_metodos.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_verificar_edt.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_mapa_paquetes.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_horas_paquetes.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_cronograma.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_diccionario.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_tamano_paquetes.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_coherencia_edt_sd03.py' -v
```

Los verificadores sobre los documentos reales informan hallazgos y devuelven 1 mientras existan. Las pruebas de `unittest` prueban los verificadores con textos mínimos y la calculadora con los ejemplos de la clase.

## Flujo y estado

| Paso | Qué es | Puerta | Estado | Artefacto |
| :-- | :-- | :-- | :-- | :-- |
| 0 | Corregir `sd-03.tex` (numeración, figuras, plataformas, nombres, referencias, declaración de IA) | G0 | **Pendiente.** Quedan unos 20 hallazgos; requiere coordinar con quien integró 3.3 y 3.4. `sd-02.tex` y `sd-03.tex` tienen cambios sin commit | `verificar_coherencia_sd03.py` |
| 1 | Reglas de conteo y convenciones | G1 | **Hecho.** C5, C8 y el umbral de ±25 % firmados por el usuario. Falta la firma del equipo | `01_reglas_de_conteo.md` |
| 2 | Actores y UAW | G2a y G2 | **Hecho.** UAW = 64 (29 actores). Falta la firma del equipo | `02_actores_uaw.md` |
| 3 | Modelo de casos de uso | G3 | **Hecho y revisado por un agente independiente.** 127 casos, 296 transacciones, UUCW 645. `verificar_casos_uso.py --completo` da 0 hallazgos. Pendiente: validar los 5 RF de clientes Retail (Anexo B) y los roles propuestos (AH-11, AH-13, AH-15) | `03_casos_de_uso_*.md`, `04_trazabilidad_resultados.md`, `05_traslapes_entre_servicios.md`, `06_decision_granularidad.md` |
| 4 | UUCW y UUCP | G4 | **Hecho.** UUCP = 709 por dos vías que coinciden | `07_uucw_uucp.md`, `07_entrada_calculadora.json` |
| 5 | TCF y EF | G5 | **Hecho con reservas.** TCF = 1,19. EF = 0,755 con los ocho valores informados por el usuario. Reservas: E7 en 0 es un supuesto sin respaldo (sd-12); E1 en 5 depende del sd-06; E5 en 5 es una autoevaluación; falta la firma del equipo y revisar E6 contra el sd-08 | `08_tcf.md`, `09_ef_preguntas.md` |
| 6 | Esfuerzo y sensibilidad | G6 | **Hecho, provisional hasta la firma del equipo.** UCP = 637, factor de conversión 20 h/punto, programación 12.740 h, total del proyecto 31.850 h (lectura B). Con 28 h/punto serían 44.590 h | `10_esfuerzo.md` |
| 7 | Lo que el método no cubre y segundo método | G7 | **Preparado, esperando al equipo.** El segundo método es de tres valores **por paquete**. Falta que el equipo llene la planilla (dos estimadores para las 51 cuentas de software, uno por cada una de las 102 restantes) y que se compare con el UCP | `11_no_cubierto_y_segundo_metodo.md`, `12_plantilla_tres_valores.md` |
| 8a | Evaluar la EDT del equipo | Lista de control de 14 puntos de la guía | **Hecho.** 21 hallazgos; el verificador da 93 (51 firmes) sobre la EDT de Eliseo, que no se modifica | `13_evaluacion_edt.md` |
| 8b | Copia corregida de la EDT | Lista de control | **Propuesta hecha, pendiente del visto bueno del equipo.** 15 ramas y **153 cuentas de control** tras las fusiones del 2026-10-08 (antes 207 paquetes), con un nodo por servicio; sin portales ni app (Opción A), sin fechas ni hitos. El verificador da 0 hallazgos firmes | `14_edt_corregida.md` |
| 8c | Mapa de paquetes a servicios, casos de uso, RF y etapa | P3.6 (un caso en un solo paquete) | **Hecho.** Los 127 casos y los 227 RF quedan en una cuenta; 51 cuentas del UCP y 102 para tres valores | `15_mapa_paquetes_ucp.md` |
| 8d | Planilla de tres valores por paquete | G7 | **Hecho, vacía.** Una fila por paquete | `12_plantilla_tres_valores.md` |
| 9 | Horas por paquete y por etapa (T-15), sin calendario ni personas | P8.1 y P8.4 | **Parcial.** Las 51 cuentas del UCP tienen horas (31.850 h); las 102 restantes esperan al paso 7. P8.4 pendiente porque la memoria de capacidad de la 3.4.1 no existe | `16_horas_por_paquete.md` |
| 10 | Cronograma, ruta crítica y curva de horas por mes | P8.3 | **Propuesta hecha, pendiente del visto bueno del equipo.** Ventanas de meses para 148 de las 153 cuentas (las cinco innovaciones quedan por definir); la ventana de una cuenta fusionada es la unión de las originales, con las anclas del Art. 17 y los congelamientos. La ruta crítica es la cadena de anclas; las holguras de los demás paquetes no se calculan sin duraciones. La curva de horas cubre solo el UCP (31.850 h) | `17_cronograma_edt.md` |
| 10b | Diccionario de la EDT por paquete (estructura) | Comunicado 10, 7.1: entregable, criterio y responsable | **Estructura hecha.** 153 fichas con los doce campos de la clase; cada valor lleva su estado (derivado, propuesta, manual o por definir). Llenado actual: 536 valores derivados, 148 propuestos y 999 por definir. Los valores de las personas van en `19_diccionario_campos_manuales.md` | `18_diccionario_edt.md`, `19_diccionario_campos_manuales.md` |
| 10c | Evaluación de las reglas 8/80 y del período de reporte | FEP02, diap. 56 | **Hecho.** Ningún elemento de la EDT cumple 8/80: un caso de uso simple ya pesa 247 h y una transacción 108 h. Se resuelve con la planificación gradual de PMBOK 6: el último nivel son 153 cuentas de control y la regla se exige a los paquetes de trabajo de cada ola (período de reporte mensual) | `20_evaluacion_8_80.md` |
| 10d | Coherencia hacia atrás de la EDT con el sd-03 | Tablas 3.1 y 3.4, Anexos A a D y compromisos de 3.2 a 3.4 | **Hecha.** Pasan las 7 comprobaciones mecánicas (etapas, RF, obligaciones, 28 resultados y exclusiones). **12 de los 16 compromisos del sd-03 no tienen entregable en la EDT** (punto de venta nuevo y su sustitución, piloto y corte de enlace de 24 h en los meses 6 y 7, compuertas por tramo, plan de comunicación, planes alternativos, entre otros). Pendiente de tu decisión | `22_coherencia_edt_sd03.md` |
| 11 | Personas en el pico frente a la dotación | P8.2 | **Diferido.** La dotación es del sd-12, que no forma parte de esta entrega; E7 sigue como supuesto sin respaldo | |
| 12 | Cierre y revisión humana | Estado «revisado» solo por una persona | **Pendiente** | |

## Decisiones del usuario que condicionan el resultado
- Opción A del portal: AH-01 sale del UAW base y AS-04 es el actor de las consultas del cliente.
- AS-12 (autoridades fiscalizadoras) sale del UAW base (C6) y se retiró CU-EV-06.
- Granularidad: opción A (el objetivo del actor), con sensibilidades por traslapes, crédito sin conexión y pruebas negativas.
- Lectura B de la clase (E = programación; total = E / 0,40) y regla de Karner para el factor de conversión, con el escenario de 28 h como sensibilidad.
- Segundo método para el desarrollo: tres valores por paquete de la EDT corregida, con dos estimadores independientes.
- EDT: el último nivel son cuentas de control (planificación gradual de PMBOK 6) y la regla 8/80 se exige a los paquetes de trabajo de cada ola, con período de reporte mensual. La versión corregida va en una copia aparte (el archivo de Eliseo no se toca); el desarrollo de software tiene un nodo por servicio con 3 a 8 paquetes; el paquete de portales y app sale por la Opción A.
- Cronograma: ventanas por paquete, con el mes 1 en enero de 2027; la dotación queda fuera por ahora.

## Notas de la calculadora
- La clase redondea el UCP a 127,1 antes de multiplicar y publica 2.542 horas. Con los decimales completos da 2.542,6 (la propia diapositiva 63 pide conservarlos). La diferencia es menor que una hora y las pruebas la aceptan con tolerancia.
- Con cinco o más factores de ambiente desfavorables, la calculadora se niega a estimar, como pide la diapositiva 49.
- `10_esfuerzo.md` se genera con `calcular_esfuerzo.py` y una prueba falla si se edita a mano.

## Umbrales fijados por el usuario (2026-10-08)
- Máximo de transacciones por caso de uso: 12 (C8).
- Diferencia aceptable entre el UCP y el segundo método: ±25 %.
