#!/usr/bin/env python3
"""Calculadora independiente del método de Puntos de Casos de Uso (FEP03, diap. 21 a 52).

Implementa solo las fórmulas de la clase (diap. 24) y sus tablas de pesos. No decide nada
por el equipo: los actores, los casos de uso y los valores de los factores se entregan desde
afuera, y la calculadora los valida y calcula. Sirve para recalcular de forma independiente
(puerta G4 a G6 del plan de estimación) y se prueba con el ejemplo de la clase.

Uso:
    python3 05_Gestion/scripts/estimacion_ucp.py entrada.json
La entrada es un JSON con estas claves:
    actores:  lista de tipos, 1 (sistema por API), 2 (sistema por protocolo) o 3 (persona con interfaz gráfica)
    casos:    lista con la cantidad de transacciones de cada caso de uso
    tcf:      13 valores de 0 a 5 (T1 a T13)
    ef:       8 valores de 0 a 5 (E1 a E8)
    cf:       opcional, horas por punto. Si falta se decide con la regla de la diap. 49
    lectura:  "A" (el resultado es el esfuerzo total) o "B" (programación, total = E / 0,40). Por defecto "B"
"""

import argparse
import json
import sys

# Diap. 26: peso por tipo de actor (1 = sistema por interfaz de programación, 2 = protocolo, 3 = persona con interfaz gráfica).
PESO_ACTOR = {1: 1, 2: 2, 3: 3}
# Diap. 29: peso por cantidad de transacciones.
CORTE_SIMPLE = 3
CORTE_MEDIO = 7
PESO_CASO = {"simple": 5, "medio": 10, "complejo": 15}
# Diap. 38: pesos de los trece factores técnicos (T1 a T13).
PESOS_TCF = [2, 1, 1, 1, 1, 0.5, 0.5, 2, 1, 1, 1, 1, 1]
# Diap. 42: pesos de los ocho factores de ambiente (E1 a E8). E7 y E8 son negativos.
PESOS_EF = [1.5, 0.5, 1, 0.5, 1, 2, -1, -1]
# Diap. 51: distribución del esfuerzo total entre actividades.
DISTRIBUCION = [("Análisis", 0.10), ("Diseño", 0.20), ("Programación", 0.40), ("Pruebas", 0.15), ("Sobrecarga", 0.15)]
CF_KARNER = 20
CF_EXIGENTE = 28


def _valor(v, nombre):
    if not isinstance(v, (int, float)) or isinstance(v, bool) or v < 0 or v > 5:
        raise ValueError(f"{nombre}: el valor debe estar entre 0 y 5 (recibido {v!r})")
    return v


def uaw(tipos):
    """UAW = suma de los pesos de los actores. Cada elemento es el tipo del actor (1, 2 o 3)."""
    total = 0
    for t in tipos:
        if t not in PESO_ACTOR:
            raise ValueError(f"tipo de actor inválido: {t!r} (use 1, 2 o 3)")
        total += PESO_ACTOR[t]
    return total


def clasificar_caso(transacciones):
    """Devuelve (tipo, peso) según la cantidad de transacciones (diap. 29)."""
    if not isinstance(transacciones, int) or transacciones < 1:
        raise ValueError(f"un caso de uso debe tener al menos una transacción (recibido {transacciones!r})")
    if transacciones <= CORTE_SIMPLE:
        tipo = "simple"
    elif transacciones <= CORTE_MEDIO:
        tipo = "medio"
    else:
        tipo = "complejo"
    return tipo, PESO_CASO[tipo]


def uucw(casos):
    """UUCW = suma de los pesos de los casos de uso. Cada elemento es su cantidad de transacciones."""
    return sum(clasificar_caso(c)[1] for c in casos)


def uucp(tipos_actores, casos):
    """UUCP = UAW + UUCW."""
    return uaw(tipos_actores) + uucw(casos)


def tcf(valores):
    """TCF = 0,6 + 0,01 x suma(peso x valor). Rango de 0,60 a 1,30."""
    if len(valores) != len(PESOS_TCF):
        raise ValueError(f"se esperaban {len(PESOS_TCF)} factores técnicos (T1 a T13) y llegaron {len(valores)}")
    suma = sum(p * _valor(v, f"T{i}") for i, (p, v) in enumerate(zip(PESOS_TCF, valores), 1))
    return 0.6 + 0.01 * suma


def ef(valores):
    """EF = 1,4 - 0,03 x suma(peso x valor). Rango de 0,42 a 1,70."""
    if len(valores) != len(PESOS_EF):
        raise ValueError(f"se esperaban {len(PESOS_EF)} factores de ambiente (E1 a E8) y llegaron {len(valores)}")
    suma = sum(p * _valor(v, f"E{i}") for i, (p, v) in enumerate(zip(PESOS_EF, valores), 1))
    return 1.4 - 0.03 * suma


def ucp(tipos_actores, casos, valores_tcf, valores_ef):
    """UCP = UUCP x TCF x EF. Se conservan los decimales y se redondea solo al final (diap. 63)."""
    return uucp(tipos_actores, casos) * tcf(valores_tcf) * ef(valores_ef)


def factores_desfavorables(valores_ef):
    """Diap. 49: E1 a E6 con valor menor que 3 y E7 y E8 con valor mayor que 3."""
    if len(valores_ef) != len(PESOS_EF):
        raise ValueError("se esperaban 8 factores de ambiente")
    primeros = sum(1 for v in valores_ef[:6] if v < 3)
    ultimos = sum(1 for v in valores_ef[6:] if v > 3)
    return primeros + ultimos


def factor_conversion(valores_ef):
    """Devuelve 20 o 28 horas por punto. Con 5 o más factores desfavorables el método no estima (diap. 49)."""
    n = factores_desfavorables(valores_ef)
    if n <= 2:
        return CF_KARNER
    if n <= 4:
        return CF_EXIGENTE
    raise ValueError(
        f"{n} factores desfavorables: el método no estima, se replantea el proyecto (FEP03, diap. 49)"
    )


def esfuerzo(puntos, cf):
    """E = UCP x CF, en horas-hombre."""
    return puntos * cf


def total_proyecto(e, lectura="B"):
    """Lectura B (la del curso): el resultado es solo programación y el total es E / 0,40. Lectura A: el resultado ya es el total."""
    if lectura == "B":
        return e / 0.40
    if lectura == "A":
        return e
    raise ValueError("lectura debe ser 'A' o 'B'")


def reparto(total):
    """Reparte el esfuerzo total entre las cinco actividades (diap. 51). Devuelve (actividad, porcentaje, horas)."""
    return [(nombre, pct, total * pct) for nombre, pct in DISTRIBUCION]


def calcular(entrada):
    tipos = entrada["actores"]
    casos = entrada["casos"]
    v_tcf = entrada["tcf"]
    v_ef = entrada["ef"]
    lectura = entrada.get("lectura", "B")
    cf = entrada.get("cf") or factor_conversion(v_ef)
    resultado = {
        "UAW": uaw(tipos),
        "UUCW": uucw(casos),
        "UUCP": uucp(tipos, casos),
        "TCF": tcf(v_tcf),
        "EF": ef(v_ef),
        "factores_desfavorables": factores_desfavorables(v_ef),
        "CF": cf,
    }
    resultado["UCP"] = resultado["UUCP"] * resultado["TCF"] * resultado["EF"]
    resultado["E"] = esfuerzo(resultado["UCP"], cf)
    resultado["total"] = total_proyecto(resultado["E"], lectura)
    resultado["lectura"] = lectura
    resultado["reparto"] = reparto(resultado["total"])
    # Sensibilidad (diap. 50 y 68): el mismo tamaño con el otro factor de conversión.
    otro = CF_EXIGENTE if cf == CF_KARNER else CF_KARNER
    resultado["sensibilidad"] = {
        "CF_alternativo": otro,
        "total_alternativo": total_proyecto(esfuerzo(resultado["UCP"], otro), lectura),
    }
    return resultado


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entrada", help="archivo JSON con actores, casos, tcf y ef")
    args = ap.parse_args(argv)
    with open(args.entrada, encoding="utf-8") as f:
        entrada = json.load(f)
    try:
        r = calcular(entrada)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print(f"UAW {r['UAW']}  UUCW {r['UUCW']}  UUCP {r['UUCP']}")
    print(f"TCF {r['TCF']:.3f}  EF {r['EF']:.3f}  UCP {r['UCP']:.2f}")
    print(f"CF {r['CF']} h/punto  ({r['factores_desfavorables']} factores desfavorables)")
    print(f"E (lectura {r['lectura']}) {r['E']:.0f} h  total del proyecto {r['total']:.0f} h")
    for nombre, pct, horas in r["reparto"]:
        print(f"  {nombre:<13}{pct:>5.0%}{horas:>9.0f} h")
    s = r["sensibilidad"]
    print(f"Sensibilidad con CF {s['CF_alternativo']}: total {s['total_alternativo']:.0f} h")
    return 0


if __name__ == "__main__":
    sys.exit(main())
