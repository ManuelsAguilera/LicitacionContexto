#!/usr/bin/env python3
"""Horas por paquete y por etapa para el Formulario T-15 (paso 9 del plan de estimación).

Para los paquetes que cubre el UCP, las horas son el total del UCP del escenario del equipo (`calcular_esfuerzo.py`) repartido en
proporción al UUCW de los casos de cada paquete (`15_mapa_paquetes_ucp.md`). Para los demás, las horas salen de las planillas de tres
valores (`12_plantilla_tres_valores.md`) si se entregan, promediando entre estimadores; si no, quedan «por estimar», sin inventar cifras.
Escribe `16_horas_por_paquete.md`. Sin calendario ni personas: la curva por mes y la dotación se hacen aparte.

    python3 05_Gestion/scripts/repartir_horas_paquetes.py [PLANILLA.md ...] [--salida RUTA]

Pruebas de la puerta: P8.1 (la suma de los paquetes de cada nodo y rama es el total de ese nodo y rama) y P8.4 (los totales coinciden con la
memoria de capacidad; queda pendiente porque esa memoria no existe).
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comparar_metodos as cm  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402
import generar_ola as go  # noqa: E402

SALIDA = gm.DIR / "16_horas_por_paquete.md"
NOMBRE_RAMA = {"1.1": "Dirección, gobierno y control del proyecto", "1.2": "Levantamiento y línea base de alcance",
               "1.3": "Arquitectura y diseño", "1.4": "Infraestructura híbrida y plataforma base", "1.5": "Desarrollo de software",
               "1.6": "Integraciones", "1.7": "Migración y saneamiento de datos", "1.8": "Seguridad, identidad y cumplimiento",
               "1.9": "Calidad, pruebas y certificación", "1.10": "Innovaciones", "1.11": "Implantación y despliegue",
               "1.12": "Resultados de las marchas blancas y aceptación por etapa", "1.13": "Gestión del cambio y capacitación",
               "1.14": "Documentación, transferencia y reversibilidad", "1.15": "Operación y soporte"}


def calcular(planillas=()):
    ucp_pk, total, paquetes = cm.horas_ucp_por_paquete()
    medias = {}
    estimadores = [cm.leer_planilla(p)[0] for p in planillas]
    for c in {c for f in estimadores for c in f}:
        v = [cm.media_pert(f[c]) for f in estimadores if f.get(c)]
        if v:
            medias[c] = sum(v) / len(v)
    filas = []
    for p in paquetes:
        if p["metodo"] == "UCP":
            horas, fuente = ucp_pk[p["codigo"]], "UCP"
        elif p["codigo"] in medias:
            horas, fuente = medias[p["codigo"]], "tres valores"
        else:
            horas, fuente = None, "por estimar"
        filas.append({**p, "horas": horas, "fuente": fuente})
    return filas, total


def paquetes_software(filas):
    """Los paquetes de trabajo de software: uno por caso de uso, con código `cuenta.n` y las horas totales del UCP del caso."""
    casos = go.horas_por_caso()
    out = []
    for f in filas:
        if f["fuente"] != "UCP":
            continue
        for i, cid in enumerate(f["casos"], 1):
            c = casos[cid]
            out.append({"codigo": f"{f['codigo']}.{i}", "nombre": f"Componente del caso de uso «{c['nombre']}» ({cid})", "cuenta": f["codigo"],
                        "servicio": f["nodo"], "etapa": f["etapa"], "trans": c["trans"], "horas": c["horas"]})
    return out


def verificar(filas, total):
    """P8.1: la suma de los paquetes de cada rama y del total coincide con lo que se declara."""
    h = []
    suma_ucp = sum(f["horas"] for f in filas if f["fuente"] == "UCP")
    suma_pk = sum(x["horas"] for x in paquetes_software(filas))
    if abs(suma_pk - total) > 1e-6:
        h.append(f"P8.1 los paquetes de software suman {suma_pk:.2f} h y el total del UCP es {total:.2f} h")
    if abs(suma_ucp - total) > 1e-6:
        h.append(f"P8.1 las horas de los paquetes del UCP suman {suma_ucp:.2f} y el total del UCP es {total:.2f}")
    por_rama = {}
    for f in filas:
        por_rama[f["rama"]] = por_rama.get(f["rama"], 0.0) + (f["horas"] or 0.0)
    if abs(sum(por_rama.values()) - sum(f["horas"] or 0.0 for f in filas)) > 1e-6:
        h.append("P8.1 la suma por rama no coincide con la suma por paquete")
    return h


def h_(x):
    return cm.h(x)


def informe(filas, total):
    ucp = [f for f in filas if f["fuente"] == "UCP"]
    estimados = [f for f in filas if f["fuente"] == "tres valores"]
    pend = [f for f in filas if f["fuente"] == "por estimar"]
    suma = sum(f["horas"] for f in filas if f["horas"] is not None)
    L = ["# Horas por paquete y por etapa para el Formulario T-15 (paso 9)", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/repartir_horas_paquetes.py`; no editar a mano. Fecha: 2026-10-08. "
         "Estado: **parcial**. Los paquetes del UCP tienen horas; los demás esperan las planillas de tres valores del equipo (`12_plantilla_tres_valores.md`) y siguen «por estimar». "
         "El calendario por paquete y la curva por mes están en `17_cronograma_edt.md`; la dotación (P8.2) queda aparte.", "",
         "## 1. Resumen", "",
         f"- Paquetes: {len(filas)}. Con horas del UCP: {len(ucp)}. Con tres valores: {len(estimados)}. Por estimar: {len(pend)}.",
         f"- Total del UCP (escenario del equipo, lectura B): {h_(total)} h, repartido en proporción al UUCW de los casos de cada paquete.",
         f"- Horas con valor hoy: {h_(suma)} h.", "",
         "## 2. Por rama", "",
         "| Rama | Paquetes | Con horas | Horas |", "| :-- | --: | --: | --: |"]
    ramas = {}
    for f in filas:
        d = ramas.setdefault(f["rama"], [0, 0, 0.0])
        d[0] += 1
        if f["horas"] is not None:
            d[1] += 1
            d[2] += f["horas"]
    for r in sorted(ramas, key=lambda x: [int(y) for y in x.split(".")]):
        d = ramas[r]
        L.append(f"| {r} {NOMBRE_RAMA.get(r, '')} | {d[0]} | {d[1]} | {h_(d[2]) if d[1] else 'por estimar'} |")
    L.append(f"| **Total** | **{len(filas)}** | **{sum(1 for f in filas if f['horas'] is not None)}** | **{h_(suma)}** |")
    L += ["", "## 3. Por etapa", "",
          "La etapa de los paquetes de software es la de su servicio (sd-03); la cartera de crédito es de las dos etapas y no se reparte entre ellas sin un dato. "
          "Los paquetes que no son de software tienen la etapa «por definir» salvo los que el sd-03 fija. El UAW no tiene paquete propio: sus horas están dentro del reparto proporcional al UUCW. "
          "Por eso las cifras de la Etapa 1 y de la Etapa 2 difieren de las de `10_esfuerzo.md`, que asigna el UAW y toda la cartera de crédito a la Etapa 1.", "",
          "| Etapa | Paquetes | Con horas | Horas |", "| :-- | --: | --: | --: |"]
    etapas = {}
    for f in filas:
        d = etapas.setdefault(f["etapa"], [0, 0, 0.0])
        d[0] += 1
        if f["horas"] is not None:
            d[1] += 1
            d[2] += f["horas"]
    for e in sorted(etapas):
        d = etapas[e]
        L.append(f"| {e} | {d[0]} | {d[1]} | {h_(d[2]) if d[1] else 'por estimar'} |")
    L += ["", "## 4. Por paquete del UCP", "", "| Paquete | Nombre | Servicio | UUCW | Etapa | Horas |", "| :-- | :-- | :-- | --: | :-- | --: |"]
    for f in ucp:
        L.append(f"| {f['codigo']} | {f['nombre']} | {f['nodo']} | {f['uucw']} | {f['etapa']} | {h_(f['horas'])} |")
    sw = paquetes_software(filas)
    L += ["", "## 4b. Paquetes de trabajo de software (uno por caso de uso)", "",
          f"Decisión del usuario del 2026-10-08: el paquete de trabajo de software es el entregable de un caso de uso. Son {len(sw)} paquetes, de {h_(min(x['horas'] for x in sw))} a {h_(max(x['horas'] for x in sw))} h; "
          "ninguno cabe en 80 h y se declara como excepción a la regla 8/80 (cada uno es un subproyecto con su descomposición en actividades, FEP02 diap. 56). "
          "Sus fases son actividades del cronograma de 8 a 80 h (`21_ola_1_paquetes_trabajo.md`, sección 3).", "",
          "| Paquete | Nombre | Cuenta | Etapa | Transacciones | Horas |", "| :-- | :-- | :-- | :-- | --: | --: |"]
    for x in sw:
        L.append(f"| {x['codigo']} | {x['nombre']} | {x['cuenta']} | {x['etapa']} | {x['trans']} | {h_(x['horas'])} |")
    L.append(f"| **Total** | | | | **{sum(x['trans'] for x in sw)}** | **{h_(sum(x['horas'] for x in sw))}** |")
    L += ["", "## 5. Por paquete que el UCP no cubre", "", "| Paquete | Nombre | Etapa | Fuente | Horas |", "| :-- | :-- | :-- | :-- | --: |"]
    for f in filas:
        if f["fuente"] != "UCP":
            L.append(f"| {f['codigo']} | {f['nombre']} | {f['etapa']} | {f['fuente']} | {h_(f['horas']) if f['horas'] is not None else 'por estimar'} |")
    hall = verificar(filas, total)
    L += ["", "## 6. Pruebas de la puerta", "",
          f"- P8.1 (las sumas por paquete, nodo y rama coinciden con el total): {'cumple' if not hall else 'NO cumple: ' + '; '.join(hall)}.",
          "- P8.2 (personas en el pico frente a la dotación): **pendiente**; la dotación es del sd-12, fuera de esta entrega.",
          "- P8.3 (la curva por etapa cuadra con los meses 1 a 12, 13 a 18 y 21 a 56): **cumple para las horas del UCP** (`17_cronograma_edt.md`); la curva completa espera las horas de los demás paquetes.",
          "- P8.4 (los totales coinciden con la memoria de capacidad y esfuerzo de la sección 3.4.1): **pendiente**; esa memoria no existe todavía."]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("planillas", nargs="*")
    ap.add_argument("--salida", default=str(SALIDA))
    a = ap.parse_args(argv)
    filas, total = calcular(a.planillas)
    hall = verificar(filas, total)
    Path(a.salida).write_text(informe(filas, total), encoding="utf-8")
    print("escrito en", a.salida)
    for x in hall:
        print(x)
    return 1 if hall else 0


if __name__ == "__main__":
    sys.exit(main())
