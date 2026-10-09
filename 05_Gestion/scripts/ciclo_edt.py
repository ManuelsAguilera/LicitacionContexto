#!/usr/bin/env python3
"""Tablero del loop de mejora de la EDT: reúne en una sola pantalla todas las comprobaciones.

Metas duras (H1 a H9) y blandas (S1 a S3). Código de salida 0 solo si pasan todas las duras. El loop (`prompt_loop_edt.md`) corre este
tablero antes y después de cada cambio y acepta el cambio solo si ninguna meta dura que pasaba deja de pasar.

    python3 05_Gestion/scripts/ciclo_edt.py [--edt RUTA] [--json] [--detalle]

Con --json imprime un objeto JSON (metas, valores y listas de infractores) pensado para compararse entre iteraciones.
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import evaluar_tamano_paquetes as et  # noqa: E402
import generar_cronograma as gc  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402
import generar_ola as go  # noqa: E402
import repartir_horas_paquetes as rh  # noqa: E402
import verificar_coherencia_edt_sd03 as vc  # noqa: E402
import verificar_edt as ve  # noqa: E402

TOTAL_UCP = 31850.0
# Lo que cuenta como traza a un elemento del sd-03: casos de uso del modelo (que traen RF y resultados) o una cita en el origen.
TRAZA = re.compile(r"sd-03|\bRF-\d|\bRNF-\d|\bOP-\d|\bEXC-\d|\bSP-\d|\bRC-\d|\bSUP-\d|Anexo [A-D]|Tabla 3\.\d|[Rr]esultado \d|\bArt\. ?\d|\bArts\. ?\d|\bRT-\d|Formulario T-|\bCaso\b|Caso,")


def tablero(edt=gm.EDT):
    paquetes, h_mapa = gm.cargar(edt)
    items = gc.asignar(paquetes)
    res = {}

    def meta(clave, nombre, ok, detalle, infractores=()):
        res[clave] = {"nombre": nombre, "ok": bool(ok), "detalle": detalle, "infractores": list(infractores)}

    coh = vc.comprobar(edt)
    mec = coh["mecanicas"]
    meta("H1", "Coherencia mecánica con el sd-03 (etapas, Tabla 3.4, RF, obligaciones, resultados, exclusiones)", all(m[1] for m in mec),
         f"{sum(m[1] for m in mec)} de {len(mec)}", [m[0] for m in mec if not m[1]])
    comp = coh["compromisos"]
    meta("H2", "Compromisos del sd-03 con entregable y ventana", all(c["ok"] for c in comp), f"{sum(c['ok'] for c in comp)} de {len(comp)}",
         [c["id"] for c in comp if not c["ok"]])
    firmes = [x for x in ve.verificar(edt) if x["tipo"] == "falta"]
    meta("H3", "Verificador de la EDT sin hallazgos firmes", not firmes, f"{len(firmes)} firmes", [f"{x['codigo']} {x['donde']}" for x in firmes][:15])
    meta("H4", "Mapa: cada caso y cada RF en una sola cuenta", not h_mapa, f"{len(h_mapa)} hallazgos", h_mapa[:10])
    por_mes, total = gc.curva(items)
    cron = gc.verificar(items, por_mes, total)
    meta("H5", "Cronograma: anclas, congelamientos y curva", not cron, f"{len(cron)} hallazgos", cron[:10])
    sin_traza = [p["codigo"] for p in paquetes if not p["casos"] and not TRAZA.search(p["origen"])]
    meta("H6", "Traza directa: toda cuenta cita un elemento del sd-03", not sin_traza, f"{len(sin_traza)} sin traza de {len(paquetes)}", sin_traza)
    inversa = [m[0] for m in mec if not m[1] and ("RF" in m[0] or "obligaciones" in m[0] or "resultados" in m[0])] + [c["id"] for c in comp if not c["ok"]]
    meta("H7", "Traza inversa: todo RF, obligación, resultado y compromiso tiene cuenta", not inversa, f"{len(inversa)} sin cuenta", inversa)
    ola, _, casos = go.construir()
    fuera = [x["codigo"] for x in ola if go.incumple(x)]
    pr = go.proyeccion(casos)
    horas_min = min(c["horas"] * pct / (1 if c["horas"] * pct <= go.MAX_H else max(c["trans"], -(-int(c["horas"] * pct) // go.MAX_H)))
                    for c in casos.values() for _, pct in go.FASES)
    proy_ok = all(m <= go.MAX_H for _, _, m in pr) and horas_min >= go.MIN_H
    meta("H8", "8/80 y un mes: paquetes de trabajo con horas (ola 1 y proyección del software)", not fuera and proy_ok,
         f"{len(fuera)} fuera de rango en la ola; proyección {sum(n for _, n, _ in pr)} paquetes, máximo {max(m for _, _, m in pr):.0f} h y mínimo {horas_min:.0f} h", fuera)
    filas, tot = rh.calcular()
    ucp = sum(f["horas"] for f in filas if f["fuente"] == "UCP")
    meta("H9", "Las horas del UCP se conservan", abs(ucp - TOTAL_UCP) <= 1 and abs(tot - TOTAL_UCP) <= 1, f"{ucp:,.0f} h de {TOTAL_UCP:,.0f} h")
    blandas = {
        "S1": {"cuentas": len(paquetes), "cuentas_software": sum(p["metodo"] == "UCP" for p in paquetes),
               "paquetes_software_proyectados": sum(n for _, n, _ in pr), "paquetes_ola_1": len(ola)},
        "S2": {"cuentas_sin_horas": sum(f["fuente"] == "por estimar" for f in filas), "paquetes_ola_sin_horas": sum(x["horas"] is None for x in ola)},
        "S3": {"posibles": len([x for x in ve.verificar(edt) if x["tipo"] == "posible"])},
    }
    return {"duras": res, "blandas": blandas, "ok": all(m["ok"] for m in res.values())}


def texto(t, detalle=False):
    L = ["| Meta | Resultado | Detalle |", "| :-- | :-- | :-- |"]
    for k, m in t["duras"].items():
        L.append(f"| {k} {m['nombre']} | {'cumple' if m['ok'] else 'NO cumple'} | {m['detalle']} |")
        if detalle and m["infractores"]:
            L.append(f"| | | {', '.join(map(str, m['infractores'][:20]))} |")
    b = t["blandas"]
    L += ["", f"S1 cuentas {b['S1']['cuentas']} ({b['S1']['cuentas_software']} de software); paquetes de software proyectados {b['S1']['paquetes_software_proyectados']}; paquetes de la ola 1 {b['S1']['paquetes_ola_1']}",
          f"S2 cuentas sin horas {b['S2']['cuentas_sin_horas']}; paquetes de la ola 1 sin horas {b['S2']['paquetes_ola_sin_horas']}",
          f"S3 posibles duplicados o varios entregables {b['S3']['posibles']}", "",
          "Metas duras: " + ("todas cumplen" if t["ok"] else "faltan " + ", ".join(k for k, m in t["duras"].items() if not m["ok"]))]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--edt", default=str(gm.EDT))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--detalle", action="store_true")
    a = ap.parse_args(argv)
    t = tablero(a.edt)
    print(json.dumps(t, ensure_ascii=False, indent=1) if a.json else texto(t, a.detalle))
    return 0 if t["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
