#!/usr/bin/env python3
"""Compara el segundo método (tres valores por servicio) con el UCP (paso 7, puerta G7).

Lee una o más planillas de tres valores (optimista, probable, pesimista, en horas) llenadas por estimadores
independientes, con el formato de `12_plantilla_tres_valores.md`. Calcula la media de tres valores
(O + 4P + Pe) / 6 por fila, promedia entre estimadores y compara el desarrollo de software con el total del
UCP del escenario del equipo (`calcular_esfuerzo.py`), en total y por servicio. Las ramas que el método no cubre
no se comparan: solo se suman.

    python3 05_Gestion/scripts/comparar_metodos.py PLANILLA.md [PLANILLA2.md ...] [--tolerancia 0.25] [--salida RUTA.md]

Código de salida: 0 si el total está dentro de la tolerancia, 1 si no, 2 si la planilla está vacía o incompleta.
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calcular_esfuerzo as ce  # noqa: E402
import estimacion_ucp as calc  # noqa: E402

DIR = ce.DIR
TOLERANCIA = 0.25  # umbral firmado por el usuario el 2026-10-08


def numero(txt):
    txt = txt.strip().replace(".", "").replace(",", ".")
    return float(txt) if txt else None


def leer_planilla(ruta):
    """{código: (O, P, Pe) | None} desde las filas `| S-EX | alcance | unidad | O | P | Pe |`. None si la fila está en blanco."""
    filas, errores = {}, []
    for linea in Path(ruta).read_text(encoding="utf-8").splitlines():
        if not linea.startswith("|"):
            continue
        c = [x.strip() for x in linea.strip().strip("|").split("|")]
        if len(c) < 6 or not re.fullmatch(r"(S-[A-Z]{2}|R-\d{2}[a-z]?)", c[0]):
            continue
        vals = [numero(x) for x in c[3:6]]
        if all(v is None for v in vals):
            filas[c[0]] = None
        elif any(v is None for v in vals):
            errores.append(f"{c[0]}: faltan valores (hay {sum(v is not None for v in vals)} de 3)")
        elif not (0 <= vals[0] <= vals[1] <= vals[2]):
            errores.append(f"{c[0]}: debe cumplirse optimista <= probable <= pesimista (recibido {vals})")
        else:
            filas[c[0]] = tuple(vals)
    return filas, errores


def media_pert(t):
    o, p, pe = t
    return (o + 4 * p + pe) / 6


def desviacion(t):
    return (t[2] - t[0]) / 6


def horas_ucp(entrada=None):
    """Total del UCP del escenario del equipo y su reparto por servicio (el UAW se reparte en proporción al UUCW)."""
    entrada = entrada or json.loads((DIR / "07_entrada_calculadora.json").read_text(encoding="utf-8"))
    ef_v = dict(ce.ESCENARIOS)[ce.REFERENCIA]
    total = ce.via2(entrada["actores"], entrada["casos"], ce.leer_tcf(), ef_v)["total"]
    uucw = calc.uucw(entrada["casos"])
    serv = {}
    for d in entrada["casos_detalle"]:
        serv[d["servicio"]] = serv.get(d["servicio"], 0) + calc.clasificar_caso(d["transacciones"])[1]
    return total, {"S-" + k: total * v / uucw for k, v in serv.items()}


def comparar(planillas, tolerancia=TOLERANCIA, entrada=None):
    total_ucp, por_servicio = horas_ucp(entrada)
    estimadores, errores = [], []
    for p in planillas:
        f, e = leer_planilla(p)
        estimadores.append(f)
        errores += [f"{Path(p).name}: {x}" for x in e]
    codigos = sorted({c for f in estimadores for c in f})
    filas, vacias = {}, []
    for c in codigos:
        medias = [media_pert(f[c]) for f in estimadores if f.get(c)]
        if not medias:
            vacias.append(c)
            continue
        sds = [desviacion(f[c]) for f in estimadores if f.get(c)]
        filas[c] = {"media": sum(medias) / len(medias), "sd": sum(sds) / len(sds), "n": len(medias),
                    "dispersion": (max(medias) - min(medias)) / (sum(medias) / len(medias)) if len(medias) > 1 else None}
    servicios = {c: v for c, v in filas.items() if c.startswith("S-")}
    ramas = {c: v for c, v in filas.items() if c.startswith("R-")}
    faltan_servicios = sorted(set(por_servicio) - set(servicios))
    r = {"total_ucp": total_ucp, "ucp_por_servicio": por_servicio, "servicios": servicios, "ramas": ramas, "vacias": vacias,
         "errores": errores, "faltan_servicios": faltan_servicios, "tolerancia": tolerancia}
    if servicios and not faltan_servicios:
        r["total_segundo"] = sum(v["media"] for v in servicios.values())
        r["diferencia"] = r["total_segundo"] / total_ucp - 1
        r["dentro"] = abs(r["diferencia"]) <= tolerancia
        r["por_servicio"] = {c: servicios[c]["media"] / por_servicio[c] - 1 for c in por_servicio}
    return r


def h(x):
    return f"{x:,.0f}".replace(",", ".")


def informe(r):
    L = ["# Comparación del UCP con el segundo método (paso 7, puerta G7)", "",
         f"Total del UCP (escenario del equipo): {h(r['total_ucp'])} h. Tolerancia: ±{r['tolerancia']:.0%}.", ""]
    if r["errores"]:
        L += ["## Errores de la planilla", ""] + [f"- {e}" for e in r["errores"]] + [""]
    if "total_segundo" not in r:
        L += ["No hay datos suficientes para comparar."]
        if r["faltan_servicios"]:
            L += ["Faltan los servicios: " + ", ".join(r["faltan_servicios"]) + "."]
        return "\n".join(L) + "\n"
    L += ["## Total del desarrollo", "", "| Método | Horas |", "| :-- | --: |", f"| UCP | {h(r['total_ucp'])} |",
          f"| Tres valores por servicio | {h(r['total_segundo'])} |",
          f"| Diferencia | {r['diferencia']:+.1%} ({'dentro' if r['dentro'] else 'FUERA'} de ±{r['tolerancia']:.0%}) |", "",
          "## Por servicio", "", "| Servicio | UCP (h) | Tres valores (h) | Diferencia | Dispersión entre estimadores |",
          "| :-- | --: | --: | --: | --: |"]
    for c in sorted(r["ucp_por_servicio"]):
        s = r["servicios"][c]
        disp = f"{s['dispersion']:.0%}" if s["dispersion"] is not None else "—"
        L.append(f"| {c} | {h(r['ucp_por_servicio'][c])} | {h(s['media'])} | {r['por_servicio'][c]:+.1%} | {disp} |")
    if r["ramas"]:
        L += ["", "## Ramas que el UCP no cubre (solo suma, sin comparación)", "", "| Código | Horas (media de tres valores) | Desviación |", "| :-- | --: | --: |"]
        for c, v in sorted(r["ramas"].items()):
            L.append(f"| {c} | {h(v['media'])} | {h(v['sd'])} |")
        L.append(f"| **Total** | **{h(sum(v['media'] for v in r['ramas'].values()))}** | |")
    if r["vacias"]:
        L += ["", "Filas sin valores: " + ", ".join(r["vacias"]) + "."]
    if not r["dentro"]:
        L += ["", "La diferencia supera la tolerancia: hay que explicar la causa antes de continuar al paso 8."]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("planillas", nargs="+")
    ap.add_argument("--tolerancia", type=float, default=TOLERANCIA)
    ap.add_argument("--salida")
    a = ap.parse_args(argv)
    r = comparar(a.planillas, a.tolerancia)
    texto = informe(r)
    if a.salida:
        Path(a.salida).write_text(texto, encoding="utf-8")
    print(texto)
    if r["errores"] or "total_segundo" not in r:
        return 2
    return 0 if r["dentro"] else 1


if __name__ == "__main__":
    sys.exit(main())
