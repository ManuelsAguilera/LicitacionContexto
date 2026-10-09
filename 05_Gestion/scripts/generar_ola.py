#!/usr/bin/env python3
"""Primera ola de paquetes de trabajo (planificación gradual de PMBOK 6): las cuentas de control activas en los meses 1 a 3 se bajan
a paquetes de trabajo de 8 a 80 horas y de un mes como máximo (regla 8/80 y período de reporte mensual, FEP02 diap. 56).

Cuatro grupos de cuentas (cada una en uno solo):
  A. software que empieza en la ola: un paquete de **especificación** por caso de uso (el análisis, 10 % de sus horas del UCP; ver
     `repartir_horas_paquetes.py`). El diseño, la construcción y las pruebas entran en las olas siguientes.
  B. trabajo continuo (ventana de más de 12 meses): un paquete por mes de la ola (por ejemplo, el informe de avance de enero).
  C. cuentas que terminan dentro de la ola: se separan en las partes que su propio nombre enumera (tabla PARTES); si nombran una sola, un paquete.
  D. cuentas que empiezan en la ola y siguen después: su primera entrega, con las partes que el nombre enumera cuando las hay.
Las horas de B, C y D no se inventan: salen de una planilla de tres valores (`21_planilla_ola_1.md`, que este script genera vacía). Escribe
`21_ola_1_paquetes_trabajo.md`.

    python3 05_Gestion/scripts/generar_ola.py [PLANILLA.md ...] [--salida RUTA] [--planilla RUTA]

Código de salida 0 si todo paquete con horas cumple 8 a 80 h y un mes, y 1 si alguno incumple. Los paquetes sin horas se informan como pendientes.
"""

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comparar_metodos as cm  # noqa: E402
import estimacion_ucp as calc  # noqa: E402
import generar_cronograma as gc  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402
import verificar_casos_uso as vcu  # noqa: E402

SALIDA = gm.DIR / "21_ola_1_paquetes_trabajo.md"
PLANILLA = gm.DIR / "21_planilla_ola_1.md"
OLA = (1, 3)
MIN_H, MAX_H = 8, 80
FASES = [("Análisis", 0.10), ("Diseño", 0.20), ("Construcción", 0.40), ("Pruebas", 0.15)]  # la sobrecarga (15 %) va a las cuentas de gestión

# Partes que el propio nombre de la cuenta enumera (propuesta; el equipo las valida). Una cuenta que no figura y es del grupo C tiene un paquete.
PARTES = {
    "1.1.1": ["Plan de gestión del ámbito", "Plan de gestión del cronograma", "Plan de gestión de los costos", "Plan de gestión de la calidad",
              "Plan de gestión de los riesgos", "Plan de gestión de las comunicaciones", "Plan de gestión de los interesados", "Plan de gestión de las adquisiciones"],
    "1.1.2": ["Estructura de descomposición del trabajo", "Diccionario de paquetes con entregable, criterio de aceptación y responsable"],
    "1.1.6": ["Calendario de ventanas de congelamiento y de eventos anuales", "Declaración de impacto por evento"],
    "1.1.13": ["Línea base de costos", "Presupuesto del proyecto"],
    "1.2.1": ["Mapa de las 14 interfaces punto a punto existentes", "Inventario de las 9 plataformas", "Inventario de los 6 proveedores y sus dependencias"],
    "1.2.3": ["Levantamiento de procesos", "Catálogo de reglas de negocio", "Volumetría declarada"],
    "1.14.6": ["Plan de Reversibilidad", "Especificación de la exportación en formatos abiertos"],
    "1.14.10": ["Protocolo de aceptación de entregas", "Protocolo de aceptación del producto final"],
    "1.7.1": ["Plan de migración", "Estrategia de corte y de retorno", "Inventario de datos históricos a migrar"],
    "1.8.1": ["Plan de seguridad", "Matriz de controles", "Modelo de amenazas"],
    "1.8.7": ["Registro de actividades de tratamiento de datos personales", "Matriz de cumplimiento normativo"],
    "1.9.2": ["Estándares de codificación", "Lista de revisión por pares", "Puertas de calidad"],
    "1.3.1": ["Documento de arquitectura", "Catálogo de decisiones de arquitectura"],
}


def grupo(p):
    v = p["ventana"]
    if p["metodo"] == "UCP":
        return "A"
    if v[1] - v[0] + 1 > 12:
        return "B"
    return "C" if v[1] <= OLA[1] else "D"


def horas_por_caso():
    paquetes, _ = gm.cargar()
    _, total, _ = cm.horas_ucp_por_paquete()
    e = vcu.leer_casos(vcu.DIR)[0]
    pesos = {c["codigo"]: calc.clasificar_caso(int(c["trans"]))[1] for c in e}
    uucw = sum(pesos.values())
    return {c["codigo"]: {"nombre": c["nombre"], "trans": int(c["trans"]), "horas": total * pesos[c["codigo"]] / uucw} for c in e}


def construir(planillas=()):
    paquetes, h = gm.cargar()
    if h:
        raise SystemExit("\n".join(h))
    items = [p for p in gc.asignar(paquetes) if p["ventana"] and p["ventana"][0] <= OLA[1]]
    casos = horas_por_caso()
    medias = {}
    ests = [cm.leer_planilla(p)[0] for p in planillas]
    for c in {c for f in ests for c in f}:
        v = [cm.media_pert(f[c]) for f in ests if f.get(c)]
        if v:
            medias[c] = sum(v) / len(v)
    out = []
    for p in items:
        g, v = grupo(p), p["ventana"]
        cod = p["codigo"]
        if g == "A":
            for i, cid in enumerate(p["casos"]):
                c = casos[cid]
                out.append({"codigo": f"{cod}.{i + 1}", "nombre": f"Especificación del caso de uso «{c['nombre']}» ({cid})", "cuenta": cod, "grupo": g,
                            "mes": OLA[0] + i % (OLA[1] - OLA[0] + 1), "horas": c["horas"] * FASES[0][1], "fuente": "UCP (análisis, 10 %)"})
        elif g == "B":
            for m in range(OLA[0], OLA[1] + 1):
                out.append({"codigo": f"{cod}.{m}", "nombre": f"{p['nombre']}, {gc.calendario(m)}", "cuenta": cod, "grupo": g, "mes": m, "horas": medias.get(f"{cod}.{m}"),
                            "fuente": "tres valores" if f"{cod}.{m}" in medias else "por estimar"})
        else:
            partes = PARTES.get(cod) or [p["nombre"] if g == "C" else f"Primera entrega de: {p['nombre']}"]
            for i, nombre in enumerate(partes):
                mes = v[0] + (i % (min(v[1], OLA[1]) - v[0] + 1)) if g == "C" else v[0]
                out.append({"codigo": f"{cod}.{i + 1}", "nombre": nombre, "cuenta": cod, "grupo": g, "mes": mes, "horas": medias.get(f"{cod}.{i + 1}"),
                            "fuente": "tres valores" if f"{cod}.{i + 1}" in medias else "por estimar"})
    return out, items, casos


def incumple(x):
    return x["horas"] is not None and not (MIN_H <= x["horas"] <= MAX_H)


def proyeccion(casos):
    """Paquetes de trabajo del software en todo el proyecto según la regla por fase y transacción."""
    filas = []
    for fase, pct in FASES:
        n, mayor = 0, 0.0
        for c in casos.values():
            hh = c["horas"] * pct
            partes = 1 if hh <= MAX_H else max(c["trans"], math.ceil(hh / MAX_H))
            n += partes
            mayor = max(mayor, hh / partes)
        filas.append((fase, n, mayor))
    return filas


def texto(paquetes, cuentas, casos):
    h = cm.h
    L = ["# Primera ola de paquetes de trabajo (meses 1 a 3)", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_ola.py`; no editar a mano. Fecha: 2026-10-08. Estado: **propuesta**, pendiente del visto bueno del equipo. "
         "Aplica la planificación gradual de PMBOK 6 aprobada por el usuario: las cuentas de control de `14_edt_corregida.md` activas en los meses 1 a 3 (enero a marzo de 2027) se bajan a paquetes de trabajo de **8 a 80 horas y de un mes como máximo** "
         "(FEP02, diapositiva 56; período de reporte mensual por RT-19.06). Los códigos de los paquetes tienen un nivel más que los de las cuentas; es una excepción a los cuatro niveles de la guía, porque el paquete de trabajo es el nivel inferior de la EDT. "
         "Las horas de los paquetes que no son de software no se inventan: esperan la planilla de tres valores (`21_planilla_ola_1.md`).", "",
         "## 1. Resumen", "",
         "| Grupo | Qué es | Cuentas | Paquetes | Con horas |", "| :-- | :-- | --: | --: | --: |"]
    nombres = {"A": "Software que empieza: especificación de cada caso de uso", "B": "Trabajo continuo: un paquete por mes",
               "C": "Cuentas que terminan dentro de la ola, separadas en sus partes", "D": "Cuentas que siguen después: su primera entrega"}
    for g in "ABCD":
        pk = [x for x in paquetes if x["grupo"] == g]
        L.append(f"| {g} | {nombres[g]} | {len({x['cuenta'] for x in pk})} | {len(pk)} | {sum(x['horas'] is not None for x in pk)} |")
    L.append(f"| **Total** | | **{len(cuentas)}** | **{len(paquetes)}** | **{sum(x['horas'] is not None for x in paquetes)}** |")
    con = [x for x in paquetes if x["horas"] is not None]
    mal = [x for x in paquetes if incumple(x)]
    L += ["", f"Paquetes con horas: {len(con)} de {len(paquetes)}. Entre 8 y 80 h: {len(con) - len(mal)}. Fuera de rango: **{len(mal)}**." +
          (" " + ", ".join(x["codigo"] for x in mal) + "." if mal else ""),
          "Cada paquete tiene un solo mes por construcción. Los de software salen del UCP; el resto queda «por estimar» y se verifica al llenar la planilla.", "",
          "## 2. Paquetes de trabajo", ""]
    for g in "ABCD":
        L += [f"### Grupo {g}. {nombres[g]}", "", "| Código | Paquete de trabajo | Cuenta | Mes | Horas | Fuente |", "| :-- | :-- | :-- | :-- | --: | :-- |"]
        for x in paquetes:
            if x["grupo"] == g:
                L.append(f"| {x['codigo']} | {x['nombre']} | {x['cuenta']} | {x['mes']} ({gc.calendario(x['mes'])}) | {h(x['horas']) if x['horas'] is not None else 'por estimar'} | {x['fuente']} |")
        L.append("")
    L += ["## 3. Regla de descomposición del software para las olas siguientes", "",
          "Cada caso de uso se baja en su ola a un paquete de trabajo por fase: análisis (10 %), diseño (20 %), construcción (40 %) y pruebas (15 %). La sobrecarga (15 %) va a las cuentas de gestión. "
          "Si una fase de un caso pasa de 80 h, se parte por transacción (o en partes iguales de hasta 80 h si el caso tiene menos transacciones que partes). Con los 127 casos:", "",
          "| Fase | Paquetes en todo el proyecto | Horas del mayor |", "| :-- | --: | --: |"]
    pr = proyeccion(casos)
    for fase, n, mayor in pr:
        L.append(f"| {fase} | {n} | {h(mayor)} |")
    L.append(f"| **Total** | **{sum(n for _, n, _ in pr)}** | |")
    L += ["", "No son 700 paquetes a la vez: en cada ola se baja solo lo que se ejecuta en ella. La ola 1 tiene los análisis de la Etapa 1 y de la cartera; el diseño y la construcción de la Etapa 1 entran en las olas de los meses 4 en adelante, y los casos de la Etapa 2 en las de los meses 13 en adelante.", "",
          "## 4. Qué falta", "",
          "1. La planilla de tres valores de los paquetes de los grupos B, C y D (`21_planilla_ola_1.md`): dos estimadores, sin consultar el UCP.",
          "2. La validación del equipo de las partes de los grupos C y D, que salen del nombre de cada cuenta.",
          "3. Si se aprueban las cuentas nuevas de `22_coherencia_edt_sd03.md`, las que empiecen en los meses 1 a 3 entran a esta ola.", ""]
    return "\n".join(L)


def plantilla(paquetes):
    L = ["# Planilla de tres valores de la primera ola", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_ola.py`. Plantilla **vacía**. Cada estimador la copia a un archivo propio, llena sus horas (optimista ≤ probable ≤ pesimista, entre 8 y 80 h por paquete) "
         "sin consultar el UCP, y se pasa a `python3 05_Gestion/scripts/generar_ola.py ARCHIVO1.md ARCHIVO2.md`.", "",
         "| Código | Paquete de trabajo | Mes | Unidad | Optimista (h) | Probable (h) | Pesimista (h) |", "| :-- | :-- | :-- | :-- | --: | --: | --: |"]
    for x in paquetes:
        if x["horas"] is None and x["fuente"] == "por estimar":
            L.append(f"| {x['codigo']} | {x['nombre']} | {x['mes']} | 1 mes | | | |")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("planillas", nargs="*")
    ap.add_argument("--salida", default=str(SALIDA))
    ap.add_argument("--planilla", default=str(PLANILLA))
    a = ap.parse_args(argv)
    paquetes, cuentas, casos = construir(a.planillas)
    Path(a.salida).write_text(texto(paquetes, cuentas, casos), encoding="utf-8")
    if not a.planillas:
        Path(a.planilla).write_text(plantilla(paquetes), encoding="utf-8")
    mal = [x for x in paquetes if incumple(x)]
    print(f"{len(cuentas)} cuentas, {len(paquetes)} paquetes, {sum(x['horas'] is not None for x in paquetes)} con horas, {len(mal)} fuera de 8–80 h")
    return 1 if mal else 0


if __name__ == "__main__":
    sys.exit(main())
