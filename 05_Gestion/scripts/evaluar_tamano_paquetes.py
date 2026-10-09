#!/usr/bin/env python3
"""Evalúa la EDT contra las dos reglas de tamaño de la clase (FEP02, diapositiva 56): 8/80 y período de reporte.

Mide cada elemento de último nivel de `14_edt_corregida.md`: horas (UCP o tres valores si se entregan planillas) y duración de su
ventana en el cronograma. Marca más de 80 h, menos de 8 h, sin horas y duración mayor que el período de reporte (un mes, por el
informe mensual de avance, RT-19.06). Distingue cuentas de control, paquetes de planificación y paquetes de trabajo: las dos reglas
se exigen solo a los paquetes de trabajo, según la planificación gradual de PMBOK 6. Escribe `20_evaluacion_8_80.md`.

    python3 05_Gestion/scripts/evaluar_tamano_paquetes.py [PLANILLA.md ...] [--salida RUTA]

Código de salida 0 si ningún paquete de trabajo incumple las reglas y 1 si alguno las incumple.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_cronograma as gc  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402
import repartir_horas_paquetes as rh  # noqa: E402

SALIDA = gm.DIR / "20_evaluacion_8_80.md"
MIN_H, MAX_H, PERIODO = 8, 80, 1  # horas y meses
TRABAJO = "paquete de trabajo"


def medir(planillas=()):
    """Lista de elementos con horas, duración, nivel y banderas."""
    paquetes, h = gm.cargar()
    if h:
        raise SystemExit("\n".join(h))
    ventanas = {p["codigo"]: p["ventana"] for p in gc.asignar(paquetes)}
    filas, total = rh.calcular(planillas)
    out = []
    for f in filas:
        v = ventanas.get(f["codigo"])
        dur = (v[1] - v[0] + 1) if v else None
        horas = f["horas"]
        nivel = f.get("nivel") or "sin nivel declarado"
        out.append({**f, "duracion": dur, "nivel": nivel,
                    "mas_80": horas is not None and horas > MAX_H, "menos_8": horas is not None and horas < MIN_H,
                    "sin_horas": horas is None, "excede_periodo": dur is not None and dur > PERIODO})
    return out, total


def numeros_base(total):
    e = json.loads((gm.DIR / "07_entrada_calculadora.json").read_text(encoding="utf-8"))
    uucw = sum(5 if n <= 3 else 10 if n <= 7 else 15 for n in e["casos"])
    trans = sum(e["casos"])
    simple = total * 5 / uucw
    return {"total": total, "uucw": uucw, "trans": trans, "simple": simple, "medio": total * 10 / uucw,
            "por_transaccion": total / trans, "programacion_simple": simple * 0.40, "lectura_a_simple": simple * 0.40,
            "min_80": total / MAX_H, "min_44": total / 44}


def incumplen(items):
    return [x for x in items if x["nivel"] == TRABAJO and (x["mas_80"] or x["menos_8"] or x["excede_periodo"] or x["sin_horas"])]


def texto(items, total):
    h = rh.cm.h
    n = numeros_base(total)
    sw = [x for x in items if x["fuente"] == "UCP"]
    dur = [x["duracion"] for x in items if x["duracion"] is not None]
    L = ["# Evaluación de la EDT contra las reglas 8/80 y del período de reporte", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/evaluar_tamano_paquetes.py`; no editar a mano. Fecha: 2026-10-08. "
         "Reglas: FEP02, diapositiva 56 («un paquete de trabajo debe requerir entre 8 y 80 horas» y «debe caber dentro de un período de reporte») y diapositiva 55 "
         "(«demasiadas divisiones disminuyen la productividad de la gestión»). Período de reporte: **un mes**, el del informe mensual de avance (RT-19.06), decisión del usuario del 2026-10-08.", "",
         "## 1. Por qué la EDT no cumple 8/80", "",
         "| Hecho | Valor |", "| :-- | --: |",
         f"| Horas de software del UCP (escenario del equipo, lectura B) | {h(n['total'])} h |",
         f"| Horas de un caso de uso simple / medio | {h(n['simple'])} h / {h(n['medio'])} h |",
         f"| Horas por transacción ({n['trans']} transacciones) | {h(n['por_transaccion'])} h |",
         f"| Programación de un caso simple (40 %, diap. 51) | {h(n['programacion_simple'])} h |",
         f"| Un caso simple con la lectura A (sin el factor ×2,5) | {h(n['lectura_a_simple'])} h |",
         f"| Elementos de software y su rango | {len(sw)}, de {h(min(x['horas'] for x in sw))} a {h(max(x['horas'] for x in sw))} h; {sum(1 for x in sw if x['horas'] <= MAX_H)} con 80 h o menos |",
         f"| Paquetes que harían falta para 8/80 solo en software | {h(n['min_80'])} (a 80 h) a {h(n['min_44'])} (a 44 h, punto medio) |",
         f"| Duración de las ventanas (meses) | {sum(1 for d in dur if d == 1)} de 1; {sum(1 for d in dur if 2 <= d <= 3)} de 2 a 3; {sum(1 for d in dur if 4 <= d <= 12)} de 4 a 12; {sum(1 for d in dur if d > 12)} de más de 12 |", "",
         "Causas, en orden de peso:", "",
         f"1. **La unidad de estimación es más gruesa que la regla.** El UCP mide por caso de uso y el caso más chico pesa {h(n['simple'])} h. Ni siquiera una transacción ({h(n['por_transaccion'])} h) cabe en 80 h. "
         "Con la lectura B, cada caso ya trae su análisis, diseño, pruebas y sobrecarga (factor ×2,5). Incluso con la lectura A, la programación de un caso simple pasa las 80 h.",
         f"2. **Escala.** Son 56 meses y {h(n['total'])} h solo de software; el resto del proyecto todavía no tiene horas (paso 7) y solo suma.",
         "3. **Las reglas que nos pusimos impiden bajar más.** La guía de la EDT prohíbe paquetes por requerimiento, pantalla o persona; el usuario fijó 3 a 8 elementos por servicio; "
         "el rango de 100 a 250 paquetes de la guía es una heurística del equipo, no viene de PMBOK ni de la clase.",
         "4. **Ventanas por etapa, no por período.** El cronograma da al software ventanas de 6 a 12 meses: la regla del período de reporte falla por construcción.",
         "5. **Trabajo continuo como un solo elemento.** Gestión, documentación y operación son trabajo de nivel de esfuerzo de 24 a 56 meses: nunca caben en 80 h ni en un mes si no se cortan por período.",
         "6. **La clase tira en dos direcciones.** La diapositiva 55 advierte contra dividir de más y la 56 pide 8/80. PMBOK 6 lo reconcilia: el último nivel de la EDT puede ser una **cuenta de control**; "
         "lo lejano se deja como **paquete de planificación** y se descompone en **paquetes de trabajo** cuando se acerca (planificación gradual).", "",
         "**Conclusión.** No es un error de conteo. Exigir 8/80 a cada elemento de una EDT de entregables de este tamaño obligaría a tener entre "
         f"{h(n['min_80'])} y {h(n['min_44'])} paquetes solo de software, contra la advertencia de la diapositiva 55. La regla se cumple un nivel más abajo, en los paquetes de trabajo de la ola cercana.", "",
         "## 2. Cumplimiento por rama", "",
         "| Rama | Elementos | Con horas | Más de 80 h | 8 a 80 h | Menos de 8 h | Sin horas | Más de un mes |", "| :-- | --: | --: | --: | --: | --: | --: | --: |"]
    ramas = {}
    for x in items:
        ramas.setdefault(x["rama"], []).append(x)
    for r in sorted(ramas, key=lambda k: [int(y) for y in k.split(".")]):
        g = ramas[r]
        L.append(f"| {r} {rh.NOMBRE_RAMA.get(r, '')} | {len(g)} | {sum(not x['sin_horas'] for x in g)} | {sum(x['mas_80'] for x in g)} | "
                 f"{sum((not x['sin_horas']) and not x['mas_80'] and not x['menos_8'] for x in g)} | {sum(x['menos_8'] for x in g)} | {sum(x['sin_horas'] for x in g)} | {sum(bool(x['excede_periodo']) for x in g)} |")
    L.append(f"| **Total** | **{len(items)}** | **{sum(not x['sin_horas'] for x in items)}** | **{sum(x['mas_80'] for x in items)}** | "
             f"**{sum((not x['sin_horas']) and not x['mas_80'] and not x['menos_8'] for x in items)}** | **{sum(x['menos_8'] for x in items)}** | **{sum(x['sin_horas'] for x in items)}** | **{sum(bool(x['excede_periodo']) for x in items)}** |")
    L += ["", "## 3. Cumplimiento por nivel", "",
          "Las dos reglas se exigen solo a los paquetes de trabajo. Las cuentas de control y los paquetes de planificación pueden ser mayores: se descomponen cuando entran en la ola cercana.", "",
          "| Nivel | Elementos | Incumplen 8/80 o el período |", "| :-- | --: | --: |"]
    niveles = {}
    for x in items:
        niveles.setdefault(x["nivel"], []).append(x)
    for nv, g in sorted(niveles.items()):
        inc = sum(1 for x in g if x["mas_80"] or x["menos_8"] or x["excede_periodo"] or x["sin_horas"])
        L.append(f"| {nv} | {len(g)} | {inc} |")
    malos = incumplen(items)
    L += ["", f"Paquetes de trabajo que incumplen: **{len(malos)}**." + ("" if not malos else " " + ", ".join(x["codigo"] for x in malos) + "."), "",
          "## 4. Decisiones del usuario (2026-10-08)", "",
          "1. Se resuelve con la planificación gradual de PMBOK 6: el último nivel de la EDT son cuentas de control; solo la ola cercana se descompone en paquetes de trabajo de 8 a 80 h y de un mes como máximo; lo lejano queda como paquetes de planificación.",
          "2. Período de reporte mensual (RT-19.06).",
          "3. Las fusiones de la opción A se aplican a nivel de cuentas de control.", "",
          "## 5. Regla de descomposición del software para su ola", "",
          f"Cuando un servicio entra en su ola, cada caso de uso se baja a paquetes de trabajo. Un caso simple ({h(n['simple'])} h) no cabe en 80 h, así que se parte por transacción y fase: "
          f"análisis y diseño ≈ {h(n['por_transaccion'] * 0.30)} h, construcción ≈ {h(n['por_transaccion'] * 0.40)} h y pruebas ≈ {h(n['por_transaccion'] * 0.15)} h por transacción; "
          f"la sobrecarga ({h(n['por_transaccion'] * 0.15)} h por transacción) va a la cuenta de gestión. Son unos {h(n['trans'] * 3)} paquetes en todo el proyecto, pero nunca todos a la vez: solo los de la ola en curso.", ""]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("planillas", nargs="*")
    ap.add_argument("--salida", default=str(SALIDA))
    a = ap.parse_args(argv)
    items, total = medir(a.planillas)
    Path(a.salida).write_text(texto(items, total), encoding="utf-8")
    print("escrito en", a.salida)
    malos = incumplen(items)
    print(f"{len(items)} elementos; {sum(x['mas_80'] for x in items)} con más de 80 h; {len(malos)} paquetes de trabajo que incumplen")
    return 1 if malos else 0


if __name__ == "__main__":
    sys.exit(main())
