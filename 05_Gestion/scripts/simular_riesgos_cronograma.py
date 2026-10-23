#!/usr/bin/env python3
"""Valor esperado de 14 riesgos y simulación del atraso de hitos por los 13 que pueden precederlos.

Cada riesgo es un evento discreto e independiente. Ocurre con su probabilidad P y, si ocurre, aporta un atraso en
semanas con distribución triangular (mínimo 0,5 x semanas, moda = semanas, máximo 1,5 x semanas) al eslabón de la
ruta crítica (Tabla 7.6 del sd-07) que afecta. Agregación solapada (base) dentro de un eslabón se toma el máximo y entre
eslabones se suma; en serie (cota superior) se suma todo. El mes 22 hereda la cadena de la Etapa 2 y suma la migración. Los datos salen de 80_Artefactos/sd-08_contexto/calificacion.md (Tablas 1 y 2) y son
estimaciones del proponente. Solo biblioteca estándar.

    python3 05_Gestion/scripts/simular_riesgos_cronograma.py [--iteraciones 10000] [--semilla 20261012] [--agregacion solapada|serie]
"""

import argparse
import random

SEMILLA_DEFECTO = 20261012
ITERACIONES_DEFECTO = 10000
HITOS = (16, 21, 22)
NOMBRE_HITO = {16: "Paso a producción Etapa 1 (mes 16)", 21: "Paso a producción Etapa 2 (mes 21)",
               22: "Retiro de la plataforma de 2011 (mes 22)"}

# Eslabones de la ruta crítica (Tabla 7.6 del sd-07) y cadena de eslabones que alimenta cada hito.
ESLABONES = {"LEV": "Levantamiento y línea base (meses 1 a 4)", "ARQ": "Arquitectura y diseño (meses 2 a 4)",
             "PLAT": "Plataforma base y ambientes (meses 3 a 10)", "DES1": "Desarrollo de la Etapa 1 (meses 1 a 12)",
             "CERT1": "Certificación de la Etapa 1 (mes 12)", "MB1": "Marcha blanca de la Etapa 1 (meses 13 a 15)",
             "DES2": "Desarrollo de la Etapa 2 (meses 13 a 18)", "MB2": "Marcha blanca de la Etapa 2 (meses 19 y 20)",
             "MIG": "Migración de cartera y retiro de 2011 (hacia el mes 22)",
             "POST16": "Primer peak posterior al paso a producción (sin hito contractual simulado)"}
CADENAS = {16: ("LEV", "ARQ", "PLAT", "DES1", "CERT1", "MB1"), 21: ("DES2", "MB2"),
           22: ("DES2", "MB2", "MIG")}  # el hito 22 hereda la cadena de la Etapa 2
AGREGACIONES = ("solapada", "serie")

# id: (P inicial, P residual, semanas, horas, eslabón de la ruta crítica que afecta, justificación de la asignación)
RIESGOS = {
    "R-02": (0.60, 0.40, 3, 600, "MB1", "El cruce con el evento anual desplaza la ruta crítica hacia el mes 16."),
    "R-12": (0.60, 0.20, 4, 1280, "MB1", "Los congelamientos de la marcha blanca arrastran el paso a producción del mes 16."),
    "R-13": (0.60, 0.40, 6, 1920, "MIG", "La ventana de migración vence con el retiro de la plataforma de 2011."),
    "R-01": (0.40, 0.20, 4, 960, "MIG", "El tramo difícil migra en la Etapa 2 y se concilia contra el retiro del mes 22."),
    "R-11": (0.40, 0.20, 3, 360, "LEV", "La validación tardía detiene entregables de la ruta crítica de la Etapa 1."),
    "R-16": (0.40, 0.20, 4, 640, "CERT1", "Sin modalidad fiscal aprobada la certificación del mes 12 y el paso del mes 16 se atrasan."),
    "R-18": (0.60, 0.40, 5, 1200, "DES1", "La carga inicial de existencias debe ser confiable al mes 16."),
    "R-20": (0.60, 0.40, 4, 640, "PLAT", "Las olas por tienda de la Etapa 1 dependen del hardware y los enlaces del cliente."),
    "R-23": (0.40, 0.20, 4, 480, "DES1", "La salida de un rol clave a mitad de la Etapa 1 atrasa la ruta crítica."),
    "R-24": (0.60, 0.40, 3, 960, "POST16", "El primer peak ocurre después del paso a producción del mes 16; no retrasa ese hito."),
    "R-25": (0.40, 0.20, 10, 2400, "MIG", "Una falla tras el retiro queda bloqueada por el congelamiento del 1 de noviembre al 7 de enero."),
    "R-33": (0.40, 0.20, 3, 600, "DES2", "La sobreasignación de los meses 13 a 15 atrasa el desarrollo de la Etapa 2."),
    "R-34": (0.60, 0.40, 3, 360, "MB1", "La meta de error de precio se mide en el piloto y la marcha blanca de la Etapa 1."),
    "R-37": (0.40, 0.20, 3, 360, "ARQ", "Las decisiones pendientes aplazan el cierre de arquitectura y el hito del mes 16."),
}


def valor_esperado(riesgos=RIESGOS):
    """Devuelve filas (id, P, semanas, VE semanas, horas, VE horas) y los totales."""
    filas = []
    for rid, (p, _, sem, hor, _, _) in riesgos.items():
        filas.append((rid, p, sem, p * sem, hor, p * hor))
    return filas, sum(f[3] for f in filas), sum(f[5] for f in filas)


def simular(probabilidades, iteraciones=ITERACIONES_DEFECTO, semilla=SEMILLA_DEFECTO, riesgos=RIESGOS,
            agregacion="solapada"):
    """Atrasos por hito (lista de semanas por iteración). `probabilidades` es {id: P}.

    solapada: dentro de un eslabón se toma el máximo atraso (corren en paralelo); entre eslabones se suma.
    serie: se suman todos los atrasos de los eslabones de la cadena (cota superior)."""
    if agregacion not in AGREGACIONES:
        raise ValueError("agregacion debe ser 'solapada' o 'serie'")
    rng = random.Random(semilla)
    resultado = {h: [] for h in HITOS}
    for _ in range(iteraciones):
        por_eslabon = {e: [] for e in ESLABONES}
        for rid, datos in riesgos.items():
            if rng.random() < probabilidades[rid]:
                sem = datos[2]
                por_eslabon[datos[4]].append(rng.triangular(0.5 * sem, 1.5 * sem, sem))
        if agregacion == "solapada":
            tramo = {e: max(v, default=0.0) for e, v in por_eslabon.items()}
        else:
            tramo = {e: sum(v) for e, v in por_eslabon.items()}
        for h in HITOS:
            resultado[h].append(sum(tramo[e] for e in CADENAS[h]))
    return resultado


def percentil(valores, q):
    orden = sorted(valores)
    k = (len(orden) - 1) * q
    i = int(k)
    j = min(i + 1, len(orden) - 1)
    return orden[i] + (orden[j] - orden[i]) * (k - i)


def resumen(atrasos):
    """Media, P50, P80, P90 y probabilidad de atraso mayor que cero por hito."""
    salida = {}
    for h, v in atrasos.items():
        salida[h] = {"media": sum(v) / len(v), "p50": percentil(v, .5), "p80": percentil(v, .8),
                     "p90": percentil(v, .9), "p_atraso": sum(1 for x in v if x > 0) / len(v)}
    return salida


def imprimir(titulo, res):
    print(f"\n{titulo}")
    print("| Hito | Media | P50 | P80 | P90 | P(atraso > 0) |")
    print("| :-- | --: | --: | --: | --: | --: |")
    for h in HITOS:
        r = res[h]
        print(f"| {NOMBRE_HITO[h]} | {r['media']:.1f} | {r['p50']:.1f} | {r['p80']:.1f} | {r['p90']:.1f} | "
              f"{r['p_atraso'] * 100:.0f} % |")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--iteraciones", type=int, default=ITERACIONES_DEFECTO, help="iteraciones Monte Carlo (10000)")
    ap.add_argument("--agregacion", choices=AGREGACIONES, default="solapada",
                    help="solapada (máximo dentro de un eslabón, caso base) o serie (suma, cota superior)")
    ap.add_argument("--semilla", type=int, default=SEMILLA_DEFECTO, help="semilla del generador (%d)" % SEMILLA_DEFECTO)
    a = ap.parse_args()

    filas, tsem, thor = valor_esperado()
    print("Valor esperado antes de la respuesta")
    print("| ID | P | Semanas | VE semanas | Horas | VE horas |")
    print("| :-- | --: | --: | --: | --: | --: |")
    for rid, p, sem, vs, hor, vh in filas:
        print(f"| {rid} | {p:.2f} | {sem} | {vs:.2f} | {hor} | {vh:.0f} |")
    print(f"| Total | | {sum(f[2] for f in filas)} | {tsem:.2f} | {sum(f[4] for f in filas)} | {thor:.0f} |")

    print("\nAsignación de riesgos a eslabones de la ruta crítica")
    for rid, d in RIESGOS.items():
        print(f"{rid} -> {ESLABONES[d[4]]}  ({d[5]})")

    ini = {r: d[0] for r, d in RIESGOS.items()}
    res_ = {r: d[1] for r, d in RIESGOS.items()}
    imprimir(f"Sin respuestas, agregación {a.agregacion} ({a.iteraciones} iteraciones, semilla {a.semilla})",
             resumen(simular(ini, a.iteraciones, a.semilla, agregacion=a.agregacion)))
    imprimir(f"Con respuestas, agregación {a.agregacion} ({a.iteraciones} iteraciones, semilla {a.semilla})",
             resumen(simular(res_, a.iteraciones, a.semilla, agregacion=a.agregacion)))


if __name__ == "__main__":
    main()
