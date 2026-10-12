#!/usr/bin/env python3
"""Esfuerzo provisional de la estimación por UCP (paso 6, puerta G6), por dos vías independientes.

Lee `07_entrada_calculadora.json` (actores y casos), los 13 valores técnicos de `08_tcf.md` y cinco
valores del factor de ambiente informados por el usuario y cuatro escenarios ilustrativos (los asigna el equipo;
ver `09_ef_preguntas.md`). Calcula con la calculadora `estimacion_ucp.py` y recalcula con fórmulas propias,
sin importar la calculadora. Escribe `10_esfuerzo.md`. Termina con código 1 si las dos vías difieren.

    python3 05_Gestion/scripts/calcular_esfuerzo.py [--salida RUTA.md]
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import estimacion_ucp as calc  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"
REFERENCIA = "Equipo"
ESCENARIOS = [  # E1 a E8. «Equipo» son los valores informados por el usuario el 2026-10-08; el resto es ilustrativo
    ("Equipo", [5, 4, 4, 4, 5, 2, 0, 3]),
    ("Mejor posible", [5, 5, 5, 5, 5, 5, 0, 0]),
    ("Favorable", [4, 4, 4, 4, 4, 4, 1, 2]),
    ("Neutro", [3, 3, 3, 3, 3, 3, 3, 3]),
    ("Algo exigente", [2, 3, 3, 3, 3, 2, 4, 3]),
    ("Peor posible", [0, 0, 0, 0, 0, 0, 5, 5]),
]
NOMBRES_SERVICIO = {"EX": "Existencias", "OF": "Oferta comercial", "VE": "Ventas", "OR": "Originación de crédito",
                    "EV": "Evidencia financiera", "CC": "Control de cruces", "CA": "Cartera de crédito",
                    "BT": "Base tecnológica", "AB": "Abastecimiento", "PE": "Pedidos", "CM": "Comisiones",
                    "MK": "Marketplace", "PV": "Posventa", "CL": "Clientes Retail"}


def leer_tcf(ruta=DIR / "08_tcf.md"):
    v = []
    for linea in Path(ruta).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*T(\d+) [^|]*\|\s*[\d,]+\s*\|\s*(\d)\s*\|", linea)
        if m:
            v.append(int(m.group(2)))
    return v


def via2(tipos, casos, tcf_v, ef_v, cf_forzado=None):
    """Fórmulas de la clase escritas de nuevo, sin la calculadora."""
    pesos_t = (2, 1, 1, 1, 1, .5, .5, 2, 1, 1, 1, 1, 1)
    pesos_e = (1.5, .5, 1, .5, 1, 2, -1, -1)
    uucw = sum(5 if n <= 3 else 10 if n <= 7 else 15 for n in casos)
    uucp = sum(tipos) + uucw
    t = .6 + .01 * sum(p * x for p, x in zip(pesos_t, tcf_v))
    e = 1.4 - .03 * sum(p * x for p, x in zip(pesos_e, ef_v))
    mal = sum(x < 3 for x in ef_v[:6]) + sum(x > 3 for x in ef_v[6:])
    cf = cf_forzado or (20 if mal <= 2 else 28 if mal <= 4 else None)
    if cf is None:
        return {"UCP": uucp * t * e, "TCF": t, "EF": e, "mal": mal, "CF": None}
    ucp = uucp * t * e
    return {"UCP": ucp, "TCF": t, "EF": e, "mal": mal, "CF": cf, "E": ucp * cf, "total": ucp * cf / .40}


def via1(entrada, tcf_v, ef_v, cf=None):
    try:
        r = calc.calcular({"actores": entrada["actores"], "casos": entrada["casos"], "tcf": tcf_v, "ef": ef_v,
                           "cf": cf, "lectura": "B"})
    except ValueError:
        return None
    return r


def h(x):
    return f"{x:,.0f}".replace(",", ".")


def dec(x, spec):
    """Número con coma decimal, como en el resto de los documentos."""
    return format(x, spec).replace(".", ",")


def construir(entrada, tcf_v):
    L = []
    uaw, uucw = calc.uaw(entrada["actores"]), calc.uucw(entrada["casos"])
    T = calc.tcf(tcf_v)
    fallas = []
    L += ["# Esfuerzo provisional por UCP (paso 6, puerta G6)", "",
          "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/calcular_esfuerzo.py`; no editar a mano. "
          "Fecha: 2026-10-08. Estado: **todos los datos informados; pendiente de la firma del equipo**. Los factores de ambiente los informó el usuario "
          "(`09_ef_preguntas.md`, sección 3) y están pendientes de la firma del equipo. Los demás escenarios del cuadro 2 son ilustrativos y no son una propuesta.", "",
          "## 1. Entradas", "",
          f"UAW {uaw} + UUCW {uucw} = UUCP {uaw + uucw} (`07_uucw_uucp.md`). TCF {dec(T, '.2f')} (`08_tcf.md`). Lectura B: la fórmula "
          "E = UCP × CF da solo la programación y el total del proyecto es E / 0,40; se usa porque es la lectura que desarrolla la "
          "clase (convención C1). Reparto del total: análisis 10 %, diseño 20 %, programación 40 %, pruebas 15 %, sobrecarga 15 % (diapositiva 51). "
          "El CF se decide con la regla de Karner (diapositiva 49): 20 h por punto con 2 o menos factores desfavorables, 28 con 3 o 4, y no se estima con 5 o más.", "",
          "## 2. Escenarios del factor de ambiente", "",
          "| Escenario | EF | Desfavorables | CF | UCP | Programación E (h) | Total del proyecto (h) | Total con el otro CF (h) |",
          "| :-- | --: | --: | --: | --: | --: | --: | --: |"]
    res = {}
    for nombre, ef_v in ESCENARIOS:
        r1, r2 = via1(entrada, tcf_v, ef_v), via2(entrada["actores"], entrada["casos"], tcf_v, ef_v)
        res[nombre] = (r1, r2)
        if r1 is None:
            assert r2["CF"] is None
            L.append(f"| {nombre} | {dec(r2['EF'], '.3f')} | {r2['mal']} | no estima | {h(r2['UCP'])} | | | |")
            continue
        for k, k2 in (("UCP", "UCP"), ("E", "E"), ("total", "total"), ("EF", "EF"), ("TCF", "TCF")):
            if abs(r1[k] - r2[k2]) > 1e-9:
                fallas.append(f"{nombre}: {k} {r1[k]} != {r2[k2]}")
        alt = r1["sensibilidad"]["total_alternativo"]
        L.append(f"| {nombre} | {dec(r1['EF'], '.3f')} | {r1['factores_desfavorables']} | {r1['CF']} | {h(r1['UCP'])} | {h(r1['E'])} | {h(r1['total'])} | {h(alt)} |")
    ref = res[REFERENCIA][0]
    L += ["", f"Referencia: «{REFERENCIA}», con los valores informados. Hay un solo factor desfavorable (E6 en 2), así que el CF es 20 horas por punto.", "",
          f"## 3. Reparto por actividad ({REFERENCIA})", "",
          "| Actividad | % | Horas (CF 20) | Horas (CF 28) |", "| :-- | --: | --: | --: |"]
    tot20 = ref["total"]
    tot28 = ref["sensibilidad"]["total_alternativo"]
    for nombre, pct in calc.DISTRIBUCION:
        L.append(f"| {nombre} | {pct:.0%} | {h(tot20 * pct)} | {h(tot28 * pct)} |")
    L.append(f"| **Total** | 100 % | **{h(tot20)}** | **{h(tot28)}** |")
    # por servicio y etapa: el UAW va a la Etapa 1 (07_uucw_uucp.md), los casos reparten por su UUCW
    serv = {}
    for d in entrada["casos_detalle"]:
        serv[d["servicio"]] = serv.get(d["servicio"], 0) + calc.clasificar_caso(d["transacciones"])[1]
    etapas = {1: uaw, 2: 0}
    for d in entrada["casos_detalle"]:
        etapas[d["etapa"]] += calc.clasificar_caso(d["transacciones"])[1]
    uucp = uaw + uucw
    L += ["", f"## 4. Reparto por etapa y servicio ({REFERENCIA}, CF 20)", "",
          "El tamaño de cada servicio es su UUCW. El UAW (64) se asigna a la Etapa 1, porque los actores de la base tecnológica nacen allí; "
          "si el equipo prefiere repartirlo por UUCW, las etapas pasan a 66,7 % y 33,3 %.", "",
          "| Etapa | Servicio | Puntos (UUCP) | % | Horas totales |", "| :-- | :-- | --: | --: | --: |"]
    etapa_de = {d["servicio"]: d["etapa"] for d in entrada["casos_detalle"]}
    for e in (1, 2):
        if e == 1:
            L.append(f"| 1 | Actores (UAW) | {uaw} | {dec(uaw / uucp, '.1%')} | {h(tot20 * uaw / uucp)} |")
        for s in sorted((s for s in serv if etapa_de[s] == e), key=lambda s: -serv[s]):
            L.append(f"| {e} | {NOMBRES_SERVICIO[s]} | {serv[s]} | {dec(serv[s] / uucp, '.1%')} | {h(tot20 * serv[s] / uucp)} |")
        L.append(f"| **{e}** | **Subtotal** | **{etapas[e]}** | **{dec(etapas[e] / uucp, '.1%')}** | **{h(tot20 * etapas[e] / uucp)}** |")
    # sensibilidad
    base_ef = dict(ESCENARIOS)[REFERENCIA]
    L += ["", f"## 5. Sensibilidad ({REFERENCIA})", "", "| Variación | UCP | Total del proyecto (h) | Diferencia |", "| :-- | --: | --: | --: |"]

    def fila(nombre, uucp_, t, e_, cf):
        ucp = uucp_ * t * e_
        tot = ucp * cf / 0.40
        L.append(f"| {nombre} | {h(ucp)} | {h(tot)} | {dec(tot / tot20 - 1, '+.1%')} |")
        return tot
    e_n = calc.ef(base_ef)
    fila("Base (UUCP 709, TCF 1,19, CF 20)", uucp, T, e_n, 20)
    for etiqueta, idx, nuevo in (("E6 en 3 (requisitos más estables)", 5, 3), ("E6 en 1 (requisitos más inestables)", 5, 1),
                                 ("E7 en 3 (la mitad del equipo a tiempo parcial)", 6, 3), ("E8 en 4 (más dificultad de herramientas)", 7, 4),
                                 ("E1 en 3 (menos dominio del modelo)", 0, 3)):
        v = list(base_ef)
        v[idx] = nuevo
        fila(etiqueta, uucp, T, calc.ef(v), 28 if calc.factores_desfavorables(v) >= 3 else 20)
    fila("CF 28 (si el equipo llegara a 3 o 4 factores desfavorables)", uucp, T, e_n, 28)
    fila("TCF bajo (1,11)", uucp, 1.11, e_n, 20)
    fila("TCF alto (1,27)", uucp, 1.27, e_n, 20)
    fila("UUCP bajo (667, `07_uucw_uucp.md`)", 667, T, e_n, 20)
    fila("UUCP alto (717)", 717, T, e_n, 20)
    fila("Combinación baja (UUCP 667, TCF 1,11, CF 20)", 667, 1.11, e_n, 20)
    fila("Combinación alta (UUCP 717, TCF 1,27, CF 28)", 717, 1.27, e_n, 28)
    L += ["", "## 6. Dos vías", "",
          "La primera vía es la calculadora `estimacion_ucp.py`. La segunda repite las fórmulas de la clase dentro de este script sin importarla. "
          + ("**Coinciden** en UCP, E, total, EF y TCF de todos los escenarios (tolerancia 1e-9)." if not fallas else "**NO coinciden**: " + "; ".join(fallas)),
          "", "## 7. Lo que estas cifras no incluyen", "",
          "- La firma del equipo sobre los ocho valores. E7 en 0 es un supuesto sin respaldo (el sd-12 no existe), E1 en 5 depende del sd-06 y E5 en 5 es una autoevaluación del equipo.",
          "- Lo que el método no cubre: migración de datos, infraestructura y licencias, capacitación, marcha blanca y operación. Se estiman aparte (paso 7) y se compara con un segundo método para el desarrollo.",
          "- La sobrecarga del 15 % de la diapositiva 51 ya está en el total (lectura B).",
          "- Las horas por paquete de la EDT (formulario T-15) se reparten en el paso 8."]
    return "\n".join(L) + "\n", fallas


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salida", default=str(DIR / "10_esfuerzo.md"))
    a = ap.parse_args(argv)
    entrada = json.loads((DIR / "07_entrada_calculadora.json").read_text(encoding="utf-8"))
    texto, fallas = construir(entrada, leer_tcf())
    Path(a.salida).write_text(texto, encoding="utf-8")
    print("escrito en", a.salida)
    print("COINCIDEN" if not fallas else "NO COINCIDEN: " + "; ".join(fallas))
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(main())
