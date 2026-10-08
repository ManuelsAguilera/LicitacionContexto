# Plan de estimación por Puntos de Casos de Uso (estado)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Resume la ruta, las puertas de validación y el estado de cada paso. El detalle del método está en la clase FEP03 (diapositivas 21 a 52).

## Cómo correr las pruebas

```bash
python3 05_Gestion/scripts/verificar_coherencia_sd03.py   # puerta G0, solo informa
python3 05_Gestion/scripts/verificar_actores.py           # puerta G2a, solo informa
python3 05_Gestion/scripts/estimacion_ucp.py ENTRADA.json  # calculadora UAW, UUCW, TCF, EF, UCP y esfuerzo
python3 -m unittest discover -s 05_Gestion/tests -p 'test_estimacion.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_coherencia_sd03.py' -v
python3 -m unittest discover -s 05_Gestion/tests -p 'test_actores.py' -v
```

Los verificadores sobre los documentos reales informan hallazgos y devuelven 1 mientras existan. Las pruebas de `unittest` prueban los verificadores con textos mínimos y la calculadora con los ejemplos de la clase.

## Flujo y estado

| N.º | Paso | Puerta | Estado |
| :-- | :-- | :-- | :-- |
| 1 | Corregir `sd-03.tex` (numeración, figuras, plataformas, nombres, referencias, declaración de IA) | G0 | **Pendiente.** El verificador lista 21 hallazgos. Requiere coordinar con quien integró 3.3 y 3.4 |
| 2 | Relacionar actores del sd-02 y el sd-03 y crear el maestro de actores | G2a | **Borrador hecho** (`80_Artefactos/maestro_actores.md`). Quedan 2 hallazgos y la validación del equipo |
| 3 | Completar y probar la EDT con la guía (12 ramas) | Lista de control de 14 puntos | Pendiente. Probada solo la rama 3 (49 paquetes) |
| 4 | Reglas de conteo y convenciones | G1 | Pendiente (firma del equipo) |
| 5 | UAW con los actores del maestro | G2 | Pendiente. Depende de 2 y 4 |
| 6 | Modelo de casos de uso | G3 | Pendiente |
| 7 | UUCW y UUCP | G4 | Calculadora lista y validada con la clase. Faltan los datos |
| 8 | TCF y EF | G5 | Pendiente. Depende de sd-04, sd-06 y sd-12 |
| 9 | UCP, esfuerzo total y por etapa, sensibilidad | G6 | Calculadora lista |
| 10 | Estimar lo no cubierto y triangular | G7 | Pendiente |
| 11 | Horas por paquete (T-15) y memoria de capacidad de la 3.4.1 | G8 | Pendiente |
| 12 | Cierre y revisión humana | Estado «revisado» solo por una persona | Pendiente |

## Notas de la calculadora
- La clase redondea el UCP a 127,1 antes de multiplicar y publica 2.542 horas. Con los decimales completos da 2.542,6 (la propia diapositiva 63 pide conservarlos). La diferencia es menor que una hora y las pruebas la aceptan con tolerancia.
- Con cinco o más factores de ambiente desfavorables, la calculadora se niega a estimar, como pide la diapositiva 49.

## Umbrales que debe fijar el equipo (propuestas mías, no vienen de la clase)
- Máximo de transacciones por caso de uso: 12.
- Diferencia aceptable entre UCP y el segundo método.
