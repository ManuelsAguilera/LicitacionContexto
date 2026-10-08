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
python3 05_Gestion/scripts/comparar_metodos.py A.md B.md       # paso 7: compara el segundo método con el UCP
python3 -m unittest discover -s 05_Gestion/tests -p 'test_estimacion.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_casos_uso.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_g4.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_tcf.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_ef.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_esfuerzo.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_comparar_metodos.py' -v
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
| 7 | Lo que el método no cubre y segundo método | G7 | **Preparado, esperando al equipo.** Falta que el equipo llene la planilla de tres valores (dos estimadores para los servicios y uno por cada rama no cubierta) y que se compare con el UCP | `11_no_cubierto_y_segundo_metodo.md`, `12_plantilla_tres_valores.md` |
| 8 | Horas por paquete (T-15) y memoria de capacidad de la 3.4.1 | G8 | **Pendiente.** Depende de la EDT, que solo existe como guía (`guia_edt.md`, probada con la rama 3), y del sd-12 | |
| 9 | Cierre y revisión humana | Estado «revisado» solo por una persona | **Pendiente** | |

## Decisiones del usuario que condicionan el resultado
- Opción A del portal: AH-01 sale del UAW base y AS-04 es el actor de las consultas del cliente.
- AS-12 (autoridades fiscalizadoras) sale del UAW base (C6) y se retiró CU-EV-06.
- Granularidad: opción A (el objetivo del actor), con sensibilidades por traslapes, crédito sin conexión y pruebas negativas.
- Lectura B de la clase (E = programación; total = E / 0,40) y regla de Karner para el factor de conversión, con el escenario de 28 h como sensibilidad.
- Segundo método para el desarrollo: tres valores por servicio, con dos estimadores independientes.

## Notas de la calculadora
- La clase redondea el UCP a 127,1 antes de multiplicar y publica 2.542 horas. Con los decimales completos da 2.542,6 (la propia diapositiva 63 pide conservarlos). La diferencia es menor que una hora y las pruebas la aceptan con tolerancia.
- Con cinco o más factores de ambiente desfavorables, la calculadora se niega a estimar, como pide la diapositiva 49.
- `10_esfuerzo.md` se genera con `calcular_esfuerzo.py` y una prueba falla si se edita a mano.

## Umbrales fijados por el usuario (2026-10-08)
- Máximo de transacciones por caso de uso: 12 (C8).
- Diferencia aceptable entre el UCP y el segundo método: ±25 %.
