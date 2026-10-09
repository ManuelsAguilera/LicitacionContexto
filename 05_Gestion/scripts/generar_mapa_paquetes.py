#!/usr/bin/env python3
"""Mapa de paquetes de la EDT a servicios, casos de uso, RF, etapa y método (paso 8c del plan de estimación).

Lee `14_edt_corregida.md` (paquetes con `{casos: ...; etapa: ...}`) y el modelo de casos, comprueba que cada uno de los casos
de uso está en un solo paquete y que el servicio del nodo coincide con el de sus casos, calcula el UUCW y los RF de cada paquete
y escribe `15_mapa_paquetes_ucp.md`.

    python3 05_Gestion/scripts/generar_mapa_paquetes.py [--edt RUTA] [--salida RUTA] [--solo-verificar]

Código de salida 0 si el mapa es coherente y 1 si hay hallazgos.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import estimacion_ucp as calc  # noqa: E402
import verificar_casos_uso as vcu  # noqa: E402
import verificar_edt as ve  # noqa: E402

DIR = vcu.DIR
EDT = DIR / "14_edt_corregida.md"
SALIDA = DIR / "15_mapa_paquetes_ucp.md"
PREFIJO_POR_NODO = {
    "Servicio de oferta comercial": "OF", "Servicio de abastecimiento": "AB", "Servicio de existencias": "EX",
    "Servicio de pedidos": "PE", "Servicio de ventas": "VE", "Servicio de comisiones": "CM", "Servicio de marketplace": "MK",
    "Servicio de posventa": "PV", "Servicio de clientes Retail": "CL", "Servicio de originación de crédito": "OR",
    "Servicio de cartera de crédito": "CA", "Servicio de evidencia financiera": "EV", "Servicio de control de cruces": "CC",
    "Base tecnológica": "BT",
}
ETAPA_SERVICIO = {"OF": "1", "EX": "1", "VE": "1", "OR": "1", "EV": "1", "CC": "1", "BT": "1", "CA": "1 y 2",
                  "AB": "2", "PE": "2", "CM": "2", "MK": "2", "PV": "2", "CL": "2"}


def cargar(edt=EDT, directorio=DIR, anexo_b=vcu.ANEXO_B):
    """Devuelve (paquetes, hallazgos). Cada paquete: codigo, nombre, nodo, prefijo, casos, rf, uucw, etapa, metodo, origen."""
    ramas, paquetes = ve.leer(edt)
    casos, _ = vcu.leer_casos(directorio)
    por_codigo = {c["codigo"]: c for c in casos}
    rf_servicio = vcu.catalogo_rf(anexo_b)
    h, salida, vistos = [], [], {}
    for r in ramas:
        nodo_de = {}
        for nd in r.get("nodos", []):
            for p in nd["paquetes"]:
                nodo_de[p["codigo"]] = nd
        for p in r["paquetes"]:
            a = p["atributos"]
            nd = nodo_de.get(p["codigo"])
            ids = [x.strip() for x in a.get("casos", "").split(",") if x.strip()]
            item = {"codigo": p["codigo"], "nombre": p["nombre"], "rama": r["codigo"], "nodo": nd["titulo"] if nd else "",
                    "casos": ids, "etapa": a.get("etapa", ""), "origen": a.get("origen", ""), "nivel": a.get("nivel", ""),
                    "metodo": "UCP" if ids else "tres valores", "rf": set(), "uucw": 0, "prefijo": ""}
            prefijos = set()
            for cid in ids:
                if cid not in por_codigo:
                    h.append(f"{p['codigo']} cita {cid}, que no existe en el modelo de casos")
                    continue
                if cid in vistos:
                    h.append(f"{cid} está en {vistos[cid]} y en {p['codigo']}")
                vistos[cid] = p["codigo"]
                c = por_codigo[cid]
                prefijos.add(cid.split("-")[1])
                item["rf"] |= vcu.expandir(c["origen"])
                item["uucw"] += calc.clasificar_caso(int(c["trans"]))[1]
            if len(prefijos) > 1:
                h.append(f"{p['codigo']} mezcla casos de varios servicios: {', '.join(sorted(prefijos))}")
            if prefijos:
                item["prefijo"] = next(iter(prefijos))
                if nd is None:
                    h.append(f"{p['codigo']} tiene casos de uso fuera de un nodo de servicio")
                elif PREFIJO_POR_NODO.get(nd["titulo"]) != item["prefijo"]:
                    h.append(f"{p['codigo']} está en el nodo «{nd['titulo']}» pero sus casos son de {item['prefijo']}")
                esperado = ETAPA_SERVICIO[item["prefijo"]]
                if item["etapa"] != esperado:
                    h.append(f"{p['codigo']}: la etapa «{item['etapa']}» no coincide con la del servicio ({esperado})")
            elif nd is not None and p["atributos"].get("ucp") != "no":
                h.append(f"{p['codigo']} está en un nodo de servicio y no tiene casos")
            salida.append(item)
    faltan = sorted(set(por_codigo) - set(vistos))
    if faltan:
        h.append("casos sin paquete: " + ", ".join(faltan))
    # todos los RF de los servicios deben quedar en algún paquete
    cubiertos = set().union(*(p["rf"] for p in salida)) if salida else set()
    sin_rf = sorted(set(rf_servicio) - cubiertos)
    if sin_rf:
        h.append(f"{len(sin_rf)} RF sin paquete: " + ", ".join(sin_rf[:10]) + ("…" if len(sin_rf) > 10 else ""))
    return salida, h


def rango_rf(rf):
    """Resume un conjunto de RF como `RF-001 a RF-004, RF-009`."""
    nums = sorted(int(x[3:]) for x in rf)
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(f"RF-{nums[i]:03d}" if i == j else (f"RF-{nums[i]:03d}, RF-{nums[j]:03d}" if j == i + 1 else f"RF-{nums[i]:03d} a RF-{nums[j]:03d}"))
        i = j + 1
    return ", ".join(out)


def informe(paquetes):
    ucp = [p for p in paquetes if p["metodo"] == "UCP"]
    L = ["# Mapa de paquetes de la EDT a servicios, casos de uso y método (paso 8c)", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_mapa_paquetes.py` a partir de `14_edt_corregida.md`; no editar a mano. "
         "Fecha: 2026-10-08. Cada fila es un paquete. «UCP» significa que sus horas salen del modelo de casos de uso; «tres valores» significa que las estima el equipo "
         "(`12_plantilla_tres_valores.md`). El UUCW es el peso de sus casos (5 por caso simple y 10 por caso medio).", "",
         f"{len(paquetes)} paquetes: {len(ucp)} cubiertos por el UCP ({sum(len(p['casos']) for p in ucp)} casos, UUCW {sum(p['uucw'] for p in ucp)}) "
         f"y {len(paquetes) - len(ucp)} para tres valores.", "",
         "## 1. Paquetes cubiertos por el UCP", "",
         "| Paquete | Nombre | Servicio | Casos | RF | UUCW | Etapa |", "| :-- | :-- | :-- | :-- | :-- | --: | :-- |"]
    for p in ucp:
        L.append(f"| {p['codigo']} | {p['nombre']} | {p['nodo']} | {', '.join(c for c in p['casos'])} | {rango_rf(p['rf']) or '—'} | {p['uucw']} | {p['etapa']} |")
    L += ["", "## 2. Paquetes para tres valores", "", "| Paquete | Nombre | Etapa | Origen o frontera |", "| :-- | :-- | :-- | :-- |"]
    for p in paquetes:
        if p["metodo"] != "UCP":
            L.append(f"| {p['codigo']} | {p['nombre']} | {p['etapa']} | {p['origen'] or '—'} |")
    L += ["", "## 3. UUCW por servicio", "", "| Servicio | Paquetes | Casos | UUCW |", "| :-- | --: | --: | --: |"]
    por = {}
    for p in ucp:
        d = por.setdefault(p["nodo"], [0, 0, 0])
        d[0] += 1
        d[1] += len(p["casos"])
        d[2] += p["uucw"]
    for nodo, (a, b, c) in por.items():
        L.append(f"| {nodo} | {a} | {b} | {c} |")
    L.append(f"| **Total** | **{sum(v[0] for v in por.values())}** | **{sum(v[1] for v in por.values())}** | **{sum(v[2] for v in por.values())}** |")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--edt", default=str(EDT))
    ap.add_argument("--salida", default=str(SALIDA))
    ap.add_argument("--solo-verificar", action="store_true")
    a = ap.parse_args(argv)
    paquetes, h = cargar(a.edt)
    for x in h:
        print(x)
    if not a.solo_verificar and not h:
        Path(a.salida).write_text(informe(paquetes), encoding="utf-8")
        print("escrito en", a.salida)
    print(f"{len(h)} hallazgo(s)")
    return 1 if h else 0


if __name__ == "__main__":
    sys.exit(main())
