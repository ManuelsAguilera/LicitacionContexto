#!/usr/bin/env python3
"""Compara el segundo método (tres valores por servicio) con el UCP (paso 7, puerta G7).

Lee una o más planillas de tres valores (optimista, probable, pesimista, en horas) llenadas por estimadores
independientes, con el formato de `12_plantilla_tres_valores.md`. Calcula la media de tres valores
(O + 4P + Pe) / 6 por fila, promedia entre estimadores y compara el desarrollo de software con el total del
UCP del escenario del equipo (`calcular_esfuerzo.py`), en total, por servicio y por paquete. Los paquetes que el
método no cubre no se comparan: solo se suman por rama.

Hay dos formatos de fila: por paquete de la EDT corregida (`1.5.1.1`, el vigente) y el anterior por servicio (`S-EX`) y por
rama (`R-06`), que se conserva para planillas ya llenadas.

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
        if len(c) < 6 or not re.fullmatch(r"(S-[A-Z]{2}|R-\d{2}[a-z]?|\d+(\.\d+){2,3})", c[0]):
            continue
        vals = [numero(x) for x in c[-3:]]
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


def horas_ucp_por_paquete():
    """{código de paquete: horas del UCP}, en proporción al UUCW de sus casos, y el total del UCP."""
    import generar_mapa_paquetes as gm  # noqa: E402
    paquetes, _ = gm.cargar()
    total, _ = horas_ucp()
    uucw = sum(p["uucw"] for p in paquetes)
    return {p["codigo"]: total * p["uucw"] / uucw for p in paquetes if p["metodo"] == "UCP"}, total, paquetes


def comparar_paquetes(planillas, tolerancia=TOLERANCIA):
    ucp_pk, total_ucp, paquetes = horas_ucp_por_paquete()
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
    r = {"modo": "paquetes", "total_ucp": total_ucp, "ucp_por_paquete": ucp_pk, "filas": filas, "vacias": vacias, "errores": errores,
         "tolerancia": tolerancia, "paquetes": {p["codigo"]: p for p in paquetes}}
    faltan = sorted(set(ucp_pk) - set(filas))
    r["faltan"] = faltan
    por_nodo = {}
    for c, horas in ucp_pk.items():
        nodo = r["paquetes"][c]["nodo"]
        d = por_nodo.setdefault(nodo, {"ucp": 0.0, "segundo": 0.0, "completo": True})
        d["ucp"] += horas
        if c in filas:
            d["segundo"] += filas[c]["media"]
        else:
            d["completo"] = False
    r["por_servicio"] = por_nodo
    if not faltan:
        r["total_segundo"] = sum(filas[c]["media"] for c in ucp_pk)
        r["diferencia"] = r["total_segundo"] / total_ucp - 1
        r["dentro"] = abs(r["diferencia"]) <= tolerancia
    r["ramas"] = {}
    for c, v in filas.items():
        if c not in ucp_pk:
            rama = ".".join(c.split(".")[:2])
            d = r["ramas"].setdefault(rama, {"media": 0.0, "n": 0})
            d["media"] += v["media"]
            d["n"] += 1
    return r


def comparar(planillas, tolerancia=TOLERANCIA, entrada=None):
    for p in planillas:
        if re.search(r"^\|\s*1\.\d+\.\d+", Path(p).read_text(encoding="utf-8"), re.M):
            return comparar_paquetes(planillas, tolerancia)
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


def informe_paquetes(r):
    L = ["# Comparación del UCP con el segundo método por paquete (paso 7, puerta G7)", "",
         f"Total del UCP (escenario del equipo): {h(r['total_ucp'])} h. Tolerancia: ±{r['tolerancia']:.0%}. "
         f"Paquetes del UCP con valores: {len(r['ucp_por_paquete']) - len(r['faltan'])} de {len(r['ucp_por_paquete'])}.", ""]
    if r["errores"]:
        L += ["## Errores de la planilla", ""] + [f"- {e}" for e in r["errores"]] + [""]
    if "total_segundo" in r:
        L += ["## Total del desarrollo", "", "| Método | Horas |", "| :-- | --: |", f"| UCP | {h(r['total_ucp'])} |",
              f"| Tres valores por paquete | {h(r['total_segundo'])} |",
              f"| Diferencia | {r['diferencia']:+.1%} ({'dentro' if r['dentro'] else 'FUERA'} de ±{r['tolerancia']:.0%}) |", ""]
    else:
        L += ["No hay valores para todos los paquetes del UCP: no se compara el total.", ""]
    L += ["## Por servicio", "", "| Servicio | UCP (h) | Tres valores (h) | Diferencia |", "| :-- | --: | --: | --: |"]
    for nodo, d in r["por_servicio"].items():
        if d["completo"]:
            L.append(f"| {nodo} | {h(d['ucp'])} | {h(d['segundo'])} | {d['segundo'] / d['ucp'] - 1:+.1%} |")
        else:
            L.append(f"| {nodo} | {h(d['ucp'])} | incompleto | — |")
    L += ["", "## Por paquete del UCP", "", "| Paquete | UCP (h) | Tres valores (h) | Diferencia | Dispersión entre estimadores |", "| :-- | --: | --: | --: | --: |"]
    for c, horas in r["ucp_por_paquete"].items():
        f = r["filas"].get(c)
        if f:
            disp = f"{f['dispersion']:.0%}" if f["dispersion"] is not None else "—"
            L.append(f"| {c} {r['paquetes'][c]['nombre']} | {h(horas)} | {h(f['media'])} | {f['media'] / horas - 1:+.1%} | {disp} |")
        else:
            L.append(f"| {c} {r['paquetes'][c]['nombre']} | {h(horas)} | — | — | — |")
    if r["ramas"]:
        L += ["", "## Paquetes que el UCP no cubre (solo suma, sin comparación)", "", "| Rama | Paquetes con valores | Horas (media de tres valores) |", "| :-- | --: | --: |"]
        for rama, d in sorted(r["ramas"].items(), key=lambda kv: [int(x) for x in kv[0].split(".")]):
            L.append(f"| {rama} | {d['n']} | {h(d['media'])} |")
        L.append(f"| **Total** | **{sum(d['n'] for d in r['ramas'].values())}** | **{h(sum(d['media'] for d in r['ramas'].values()))}** |")
    if "total_segundo" in r and not r["dentro"]:
        L += ["", "La diferencia supera la tolerancia: hay que explicar la causa antes de continuar al paso 9."]
    return "\n".join(L) + "\n"


def informe(r):
    if r.get("modo") == "paquetes":
        return informe_paquetes(r)
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
