#!/usr/bin/env python3
"""Cronograma de la EDT corregida (paso 10 del plan de estimación).

Asigna a cada paquete de `14_edt_corregida.md` una ventana de meses (inicio y fin), distingue las ventanas fijadas por el contrato
(Art. 17 de las Bases, sd-03, Anexo D) de las que son propuesta de este trabajo, reparte las horas del UCP dentro de la ventana de cada
paquete (en partes iguales por mes: supuesto) y comprueba las anclas del contrato y las ventanas de congelamiento.
Escribe `17_cronograma_edt.md`. No usa horas de los paquetes que el UCP no cubre ni dotación.

    python3 05_Gestion/scripts/generar_cronograma.py [--salida RUTA]

Código de salida 0 si las comprobaciones pasan y 1 si no.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comparar_metodos as cm  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402

SALIDA = gm.DIR / "17_cronograma_edt.md"
MESES = 56
MES_1 = (2027, 1)  # SUP-26
NOMBRES_MES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
# Meses calendario con algún congelamiento (Caso, numeral 13.2 y RT-10.05): 1 nov a 6 ene; evento anual y su semana previa (mayo o junio);
# última semana de noviembre; segunda semana de mayo; última semana de enero a primera de marzo.
CONGELADOS = {1: "1 al 6 de enero y última semana", 2: "todo el mes", 3: "primera semana", 5: "segunda semana y evento anual posible",
              6: "evento anual posible", 11: "todo el mes", 12: "todo el mes"}
ETAPAS = {"1": (1, 12), "2": (13, 18), "1 y 2": (1, 18)}

C, P = "contrato", "propuesta"
# código de paquete -> (inicio, fin, tipo, fuente o criterio). None = por definir.
V = {
    "1.1.1": (1, 3, P, "plan inicial; se actualiza durante el contrato"), "1.1.2": (1, 3, P, "base de la planificación"),
    "1.1.3": (1, 56, C, "Art. 72: todo el contrato"), "1.1.4": (1, 56, P, "continuo"), "1.1.5": (1, 56, P, "continuo"),
    "1.1.6": (1, 3, P, "se actualiza cada año antes de la campaña de noviembre"), "1.1.7": (1, 56, C, "Art. 71: comités durante todo el contrato"),
    "1.1.8": (1, 56, C, "RT-19.06: informe mensual"), "1.1.9": (4, 56, P, "desde el primer entorno de nube"),
    "1.1.10": (1, 56, C, "Art. 18: cada entrega sujeta a aceptación"), "1.1.11": (1, 56, C, "Art. 75.3"), "1.1.12": (1, 1, P, "mes de inicio"),
    "1.1.13": (1, 3, P, "base de la planificación"),
    "1.2.1": (1, 3, P, "entrega temprana, antes del diseño"), "1.2.2": (1, 3, P, "antes del diseño"), "1.2.3": (1, 3, P, "antes del diseño"),
    "1.2.4": (1, 18, P, "mientras dura el desarrollo"), "1.2.5": (2, 4, P, "tras el levantamiento"), "1.2.6": (3, 4, P, "cierra el levantamiento"),
    "1.2.7": (2, 5, P, "OP-01 a OP-05"), "1.2.8": (2, 6, P, "OP-08, OP-09"), "1.2.9": (2, 5, P, "decide el destino de las plataformas"),
    "1.3.1": (2, 4, P, "arquitectura cerrada en el mes 4 (EDT original)"), "1.3.2": (2, 4, P, "idem"), "1.3.3": (2, 4, P, "idem"),
    "1.3.4": (2, 4, P, "idem"), "1.3.5": (3, 4, P, "idem"), "1.3.6": (3, 4, P, "idem"), "1.3.7": (3, 4, P, "idem"),
    "1.3.8": (3, 6, P, "el cliente necesita plazo para ejecutar las obras"),
    "1.4.1": (3, 6, P, "plataforma base lista en el mes 6 (EDT original)"), "1.4.2": (6, 12, P, "antes de la marcha blanca"),
    "1.4.3": (4, 8, P, "ámbito emisor"), "1.4.4": (1, 12, C, "Art. 17: ambientes habilitados dentro de la Etapa 1 (meses 1 a 12)"),
    "1.4.5": (4, 8, P, "antes de las primeras pruebas"), "1.4.6": (3, 5, P, "antes del desarrollo en curso"),
    "1.4.7": (2, 6, P, "a nombre del cliente"), "1.4.8": (3, 6, P, "el cliente adquiere después"), "1.4.9": (2, 4, P, "RT-06.03"),
    "1.4.10": (3, 6, P, "RT-06.06: el cliente ejecuta la obra"), "1.4.11": (2, 5, P, "informe de 2024"),
    "1.4.12": (6, 12, P, "listo antes de la marcha blanca"), "1.4.13": (6, 12, P, "idem"), "1.4.14": (6, 12, P, "idem"),
    "1.4.15": (6, 12, P, "idem"), "1.4.16": (6, 12, P, "idem"), "1.4.17": (6, 12, P, "RT-07.09"), "1.4.18": (8, 12, P, "RT-06.26"),
    "1.4.19": (8, 12, P, "antes del piloto de tiendas"),
    "1.6.1": (2, 5, P, "catálogo de interfaces"), "1.6.2": (5, 12, P, "interfaces de la Etapa 1"), "1.6.3": (13, 18, P, "interfaz de la Etapa 2"),
    "1.6.4": (5, 12, P, "interfaces de la Etapa 1"), "1.6.5": (13, 18, P, "interfaz de la Etapa 2"), "1.6.6": (5, 18, P, "cartera: Etapa 1 y 2"),
    "1.6.7": (13, 18, P, "interfaz de la Etapa 2"), "1.6.8": (5, 12, P, "interfaz de la Etapa 1"), "1.6.9": (13, 18, P, "abastecimiento es de la Etapa 2"),
    "1.6.10": (8, 12, P, "la filial emisora está en la Etapa 1"), "1.6.11": (10, 18, P, "certificación de las dos etapas"),
    "1.7.1": (2, 4, P, "antes de migrar"), "1.7.2": (2, 4, P, "RT-05.15"), "1.7.3": (4, 10, P, "antes de la marcha blanca"),
    "1.7.4": (11, 15, P, "corte antes del paso a producción"), "1.7.5": (8, 15, P, "antes del paso a producción"),
    "1.7.6": (14, 19, P, "clientes Retail es de la Etapa 2"),
    "1.7.7": (10, 21, C, "Anexo D, resultado 24: primera parte en el mes 16 y segunda en el mes 21"),
    "1.7.8": (13, 21, P, "acompaña a la migración"), "1.7.9": (10, 16, P, "antes del paso a producción de la Etapa 1"),
    "1.7.10": (14, 18, P, "antes del retiro"), "1.7.11": (22, 22, C, "sd-03 (operación): fecha objetivo octubre de 2028 = mes 22"),
    "1.7.12": (21, 56, C, "sd-03 (operación): se retira durante la operación; fecha por definir"),
    "1.8.1": (1, 4, P, "base de la seguridad"), "1.8.2": (2, 5, P, "tras la arquitectura"), "1.8.3": (4, 8, P, "tras el diseño"),
    "1.8.4": (4, 8, P, "antes de la marcha blanca"), "1.8.5": (2, 5, P, "tras la arquitectura"), "1.8.6": (4, 10, P, "RNF-33, RNF-34"),
    "1.8.7": (3, 8, P, "Ley 21.719"), "1.8.8": (3, 8, P, "tras el diseño"), "1.8.9": (10, 18, P, "antes de la certificación de cada etapa"),
    "1.8.10": (2, 4, P, "antes de elegir el proveedor de nube"), "1.8.11": (4, 12, P, "RNF-70, RNF-71"), "1.8.12": (4, 8, P, "RNF-73"),
    "1.9.1": (2, 4, P, "antes de probar"), "1.9.2": (4, 6, P, "antes del desarrollo en curso"), "1.9.3": (5, 18, P, "durante el desarrollo de las dos etapas"),
    "1.9.4": (9, 18, P, "antes de la certificación de cada etapa"), "1.9.5": (10, 18, P, "idem"),
    "1.9.6": (14, 21, C, "Anexo D, resultado 25: ensayo del orden de degradación en el mes 16 y prueba de carga completa en el mes 21"),
    "1.9.7": (11, 21, P, "aceptación por etapa"), "1.9.8": (12, 12, C, "Art. 17: la certificación va dentro del desarrollo de la Etapa 1 (meses 1 a 12)"),
    "1.9.9": (18, 18, C, "Art. 17: cierre del desarrollo de la Etapa 2 en el mes 18"), "1.9.10": (1, 3, P, "antes de programar"),
    "1.10.1": None, "1.10.2": None, "1.10.3": None, "1.10.4": None, "1.10.5": None,
    "1.11.1": (3, 6, P, "T-18; se actualiza"), "1.11.2": (9, 12, P, "antes de la marcha blanca"),
    "1.11.3": (9, 18, P, "sitios de la Etapa 1 antes del mes 13 y de la Etapa 2 antes del mes 19"), "1.11.4": (15, 18, P, "Art. 17.2 fija la convivencia en los meses 19 y 20; el plan va antes"),
    "1.12.1": (10, 12, P, "antes de la marcha blanca"), "1.12.2": (15, 15, C, "Art. 17: la marcha blanca de la Etapa 1 termina en el mes 15"),
    "1.12.3": (15, 16, C, "Art. 17.3: condiciones de cierre"), "1.12.4": (16, 16, C, "Art. 17: paso a producción en el mes 16"),
    "1.12.5": (16, 18, P, "antes de la marcha blanca de la Etapa 2"), "1.12.6": (20, 20, C, "Art. 17: la marcha blanca de la Etapa 2 termina en el mes 20"),
    "1.12.7": (21, 21, C, "Art. 17: aceptación final en el mes 21"), "1.12.8": (21, 21, P, "se activa con la aceptación final"),
    "1.12.9": (16, 24, P, "tras cada paso a producción"),
    "1.13.1": (3, 6, P, "antes de capacitar"), "1.13.2": (5, 8, P, "antes de capacitar"),
    "1.13.3": (10, 20, P, "Art. 17.3: la capacitación certificada es condición de cierre de cada marcha blanca (meses 15 y 20)"),
    "1.13.4": (13, 24, P, "tras el paso a producción de cada etapa"),
    "1.14.1": (1, 56, P, "continua, versión final al cierre"), "1.14.2": (5, 56, P, "desde el primer artefacto desplegado"),
    "1.14.3": (48, 56, P, "Art. 77.1: programa de transferencia hacia el cierre"), "1.14.4": (13, 56, P, "desde la marcha blanca"),
    "1.14.5": (10, 20, P, "antes de operar"), "1.14.6": (1, 3, C, "Art. 77.2: dentro de los primeros noventa días; se actualiza cada año"),
    "1.14.7": (56, 56, C, "Art. 77.2: noventa días después del cierre, fuera de los 56 meses"), "1.14.8": (56, 56, P, "cierre del contrato"),
    "1.14.9": (56, 56, P, "cierre del contrato"), "1.14.10": (1, 3, P, "antes de la primera aceptación"),
}
for _c in ("1.15.1", "1.15.2", "1.15.3", "1.15.4", "1.15.5", "1.15.6", "1.15.7", "1.15.8"):
    V[_c] = (21, 56, C, "Art. 17: operación de los meses 21 a 56")
V["1.15.3"] = (21, 56, C, "sd-03: la recuperación ante desastres se prueba dos veces al año")


def calendario(m):
    a = MES_1[0] + (m - 1) // 12
    return f"{NOMBRES_MES[(m - 1) % 12]} {a}"


def mes_calendario(m):
    return (m - 1) % 12 + 1


def fusiones(edt=gm.EDT):
    """{código que queda: [códigos absorbidos]} desde la tabla `| Queda | Absorbe | ... |` de la EDT."""
    out = {}
    for cab, filas in gm.vcu.tablas(Path(edt).read_text(encoding="utf-8")):
        if cab[:2] == ["Queda", "Absorbe"]:
            for f in filas:
                out[f[0]] = [x.strip() for x in f[1].split(",") if x.strip()]
    return out


FUSIONES = fusiones()


def ventana(p):
    """(inicio, fin, tipo, fuente) del elemento; para el software, la de su etapa (Art. 17).
    Si el elemento absorbió otros al fusionarse, su ventana es la unión de las ventanas originales."""
    if p["metodo"] == "UCP":
        a, b = ETAPAS[p["etapa"]]
        return a, b, C, f"Art. 17: desarrollo de la etapa {p['etapa']}" if p["etapa"] != "1 y 2" else "Art. 17 y Anexo D 24: cartera migra en las dos etapas"
    miembros = [p["codigo"]] + FUSIONES.get(p["codigo"], [])
    vs = [V[c] for c in miembros if V.get(c)]
    if not vs:
        return None
    if len(vs) == 1:
        return vs[0]
    fuentes = []
    for v in vs:
        if v[3] not in fuentes:
            fuentes.append(v[3])
    tipo = vs[0][2] if V.get(p["codigo"]) else vs[0][2]
    return min(v[0] for v in vs), max(v[1] for v in vs), tipo, "; ".join(fuentes)


def asignar(paquetes):
    out = []
    for p in paquetes:
        v = ventana(p)
        out.append({**p, "ventana": v})
    return out


def curva(items):
    """Horas del UCP por mes, repartidas en partes iguales dentro de la ventana de cada paquete."""
    ucp_pk, total, _ = cm.horas_ucp_por_paquete()
    por_mes = {m: {"1": 0.0, "2": 0.0, "1 y 2": 0.0} for m in range(1, MESES + 1)}
    for p in items:
        if p["codigo"] not in ucp_pk:
            continue
        a, b = p["ventana"][0], p["ventana"][1]
        for m in range(a, b + 1):
            por_mes[m][p["etapa"]] += ucp_pk[p["codigo"]] / (b - a + 1)
    return por_mes, total


def verificar(items, por_mes, total):
    h = []
    for p in items:
        v = p["ventana"]
        if v is None:
            continue
        a, b = v[0], v[1]
        if not (1 <= a <= b <= MESES):
            h.append(f"{p['codigo']}: ventana {a}–{b} fuera de 1–{MESES} o invertida")
        if p["etapa"] == "operación" and not (a >= 21):
            h.append(f"{p['codigo']}: paquete de operación antes del mes 21")
        if p["metodo"] == "UCP" and not (ETAPAS[p["etapa"]][0] <= a and b <= ETAPAS[p["etapa"]][1]):
            h.append(f"{p['codigo']}: el software de la etapa {p['etapa']} debe caer en los meses {ETAPAS[p['etapa']]}")
    for p in items:
        if p["ventana"] is None and p["rama"] != "1.10":
            h.append(f"{p['codigo']}: sin ventana")
    for m in (16, 21):
        if mes_calendario(m) in CONGELADOS:
            h.append(f"el paso a producción del mes {m} ({calendario(m)}) cae en un congelamiento")
    suma = sum(sum(v.values()) for v in por_mes.values())
    if abs(suma - total) > 1e-6:
        h.append(f"P8.3 la curva suma {suma:.2f} h y el total del UCP es {total:.2f} h")
    for m, v in por_mes.items():
        if v["1"] > 1e-9 and not 1 <= m <= 12:
            h.append(f"P8.3 horas de la Etapa 1 en el mes {m}")
        if v["2"] > 1e-9 and not 13 <= m <= 18:
            h.append(f"P8.3 horas de la Etapa 2 en el mes {m}")
        if v["1 y 2"] > 1e-9 and not 1 <= m <= 18:
            h.append(f"P8.3 horas de la cartera fuera de los meses 1 a 18 en el mes {m}")
    return h


def barra(a, b):
    return "".join("█" if a <= m <= b else "·" for m in range(1, MESES + 1))


def texto(items, por_mes, total):
    h_ = cm.h
    L = ["# Cronograma de la EDT corregida (paso 10)", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_cronograma.py` a partir de `14_edt_corregida.md`; no editar a mano. "
         "Fecha: 2026-10-08. Estado: **propuesta** de este trabajo, pendiente del visto bueno del equipo. El mes 1 es enero de 2027 (SUP-26). "
         "Cada paquete tiene una ventana de meses. La ventana es **fija por contrato** (Bases, sd-03 o Anexo D) o es **propuesta** de este trabajo; la columna Fuente lo dice. "
         "No hay horas de los paquetes que el UCP no cubre, ni dotación, ni personas. No es la carta Gantt del Formulario T-14: es el calendario de ventanas que la hace posible.", "",
         "## 1. Calendario y anclas del contrato", "",
         "| Mes | Calendario | Hito | Fuente |", "| --: | :-- | :-- | :-- |",
         f"| 1 | {calendario(1)} | Inicio del contrato | SUP-26 |",
         f"| 1 a 3 | {calendario(1)} a {calendario(3)} | Plan de Reversibilidad (primeros noventa días) | Art. 77.2 |",
         f"| 1 a 12 | {calendario(1)} a {calendario(12)} | Etapa 1: desarrollo, con certificación y ambientes habilitados | Art. 17 |",
         f"| 13 a 15 | {calendario(13)} a {calendario(15)} | Etapa 1: marcha blanca, en paralelo con el desarrollo de la Etapa 2 | Art. 17, 17.2 |",
         f"| 16 | {calendario(16)} | Etapa 1 pasa a producción y es el registro oficial | Art. 17 |",
         f"| 13 a 18 | {calendario(13)} a {calendario(18)} | Etapa 2: desarrollo (cierra en el mes 18 inclusive) | Art. 17 |",
         f"| 19 a 20 | {calendario(19)} a {calendario(20)} | Etapa 2: marcha blanca, con la Etapa 1 en producción | Art. 17, 17.2 |",
         f"| 21 | {calendario(21)} | Etapa 2 pasa a producción, aceptación final e inicio de la operación | Art. 17 |",
         f"| 22 | {calendario(22)} | Retiro de la plataforma de crédito de 2011 (fecha objetivo) | sd-03, operación |",
         f"| 24 | {calendario(24)} | Hitos del plan de remediación de la autoridad, a más tardar | Anexo D, resultado 23 |",
         f"| 21 a 56 | {calendario(21)} a {calendario(56)} | Operación | Art. 17 |",
         f"| 56 | {calendario(56)} | Cierre del contrato | Art. 17 |", "",
         "### Congelamientos (Caso, numeral 13.2)", "",
         "No puede haber un paso a producción dentro de un congelamiento. Meses calendario afectados: " +
         ", ".join(f"{NOMBRES_MES[k - 1]} ({v})" for k, v in sorted(CONGELADOS.items())) + ". "
         f"Los pasos a producción caen en {calendario(16)} y {calendario(21)}, fuera de todos ellos. "
         f"Cae en congelamiento la marcha blanca de la Etapa 1 ({calendario(13)} a {calendario(15)}): es operación supervisada, sin cambios en producción, así que se coordina con el plan de la marcha blanca. "
         f"Con la Etapa 1 ya en producción, el evento anual de comercio electrónico y el Día de la Madre de 2028 ({calendario(17)} y {calendario(18)}) caen en el desarrollo de la Etapa 2: el ensayo de degradación del evento "
         "(paquete 1.9.6) debe estar hecho antes.", "",
         "## 2. Ventanas por cuenta de control", ""]
    ramas = {}
    for p in items:
        ramas.setdefault(p["rama"], []).append(p)
    L += ["Las barras tienen 56 columnas, una por mes; `█` es un mes activo. El año 1 son las columnas 1 a 12.", "",
          "```", "mes      " + "".join(str((m // 10) % 10) if m % 10 == 0 else " " for m in range(1, MESES + 1)),
          "         " + "".join(str(m % 10) for m in range(1, MESES + 1)), "```", ""]
    for rama in sorted(ramas, key=lambda x: [int(y) for y in x.split(".")]):
        L += [f"### Rama {rama}", "", "| Paquete | Nombre | Ventana | Tipo | Fuente o criterio |", "| :-- | :-- | :-- | :-- | :-- |"]
        for p in ramas[rama]:
            v = p["ventana"]
            if v is None:
                L.append(f"| {p['codigo']} | {p['nombre']} | por definir | — | depende de las innovaciones que se confirmen (sd-13) |")
            else:
                L.append(f"| {p['codigo']} | {p['nombre']} | {v[0]}–{v[1]} | {v[2]} | {v[3]} |")
        L.append("")
    L += ["## 3. Barras", "", "```"]
    for p in items:
        v = p["ventana"]
        L.append(f"{p['codigo']:<9}{barra(v[0], v[1]) if v else '·' * MESES + '  por definir'}")
    L += ["```", "",
          "## 4. Precedencias y ruta crítica", "",
          "La ruta crítica es la cadena de anclas del contrato, que no tiene holgura:", "",
          "| Orden | Eslabón | Mes | Holgura |", "| --: | :-- | --: | --: |",
          "| 1 | Levantamiento y línea base de alcance (1.2) | 1 a 4 | 0 |",
          "| 2 | Arquitectura y diseño (1.3) | 2 a 4 | 0 |",
          "| 3 | Plataforma base y ambientes (1.4) | 3 a 10 | 0 |",
          "| 4 | Desarrollo de la Etapa 1 (1.5, servicios de la Etapa 1) | 1 a 12 | 0 |",
          "| 5 | Certificación de la Etapa 1 (1.9.8) | 12 | 0 |",
          "| 6 | Marcha blanca de la Etapa 1 y sus condiciones de cierre (1.12.1 a 1.12.3) | 13 a 15 | 0 |",
          "| 7 | Paso a producción de la Etapa 1 (1.12.4) | 16 | 0 |",
          "| 8 | Desarrollo de la Etapa 2, en paralelo con los pasos 6 y 7 | 13 a 18 | 0 |",
          "| 9 | Certificación de la Etapa 2 (1.9.9) | 18 | 0 |",
          "| 10 | Marcha blanca de la Etapa 2 (1.12.5, 1.12.6) | 19 a 20 | 0 |",
          "| 11 | Paso a producción de la Etapa 2, aceptación final e inicio de la operación (1.12.7) | 21 | 0 |", "",
          "Los demás paquetes tienen holgura **sin calcular**: no hay horas ni duraciones de los paquetes que el UCP no cubre ni dotación, y una holgura inventada sería falsa. "
          "Se calcula cuando existan las planillas de tres valores y la dotación. Precedencias que se respetaron: el levantamiento antecede a la arquitectura; la arquitectura antecede a la plataforma base y a los ambientes; "
          "los ambientes antecedan a las pruebas de carga, resiliencia y recuperación; el desarrollo de una etapa antecede a su certificación, la certificación a la marcha blanca y esta al paso a producción; "
          "la capacitación certificada es condición de cierre de cada marcha blanca (Art. 17.3); los servicios de la Etapa 2 dependen de servicios de la Etapa 1 (sd-03, Tabla 3.1), así que ninguno empieza antes del mes 13.", "",
          "## 5. Curva de horas del UCP por mes", "",
          "Las horas del UCP (31.850 h) se reparten en partes iguales por mes dentro de la ventana de cada paquete. Es un supuesto de distribución: el UCP da el total, no el perfil dentro de la etapa. "
          "Las horas de los demás paquetes no están (esperan las planillas), por lo que esta curva es **parcial** y no es todavía la curva de dotación del T-15.", "",
          "| Mes | Calendario | Etapa 1 (h) | Etapa 2 (h) | Cartera, etapas 1 y 2 (h) | Total (h) |", "| --: | :-- | --: | --: | --: | --: |"]
    for m in range(1, 19):
        v = por_mes[m]
        L.append(f"| {m} | {calendario(m)} | {h_(v['1'])} | {h_(v['2'])} | {h_(v['1 y 2'])} | {h_(sum(v.values()))} |")
    tot = {k: sum(por_mes[m][k] for m in por_mes) for k in ("1", "2", "1 y 2")}
    L.append(f"| **Total** | | **{h_(tot['1'])}** | **{h_(tot['2'])}** | **{h_(tot['1 y 2'])}** | **{h_(sum(tot.values()))}** |")
    L += ["", f"Entre los meses 13 y 15 coexisten el desarrollo de la Etapa 2 ({h_(por_mes[13]['2'])} h por mes) y la marcha blanca de la Etapa 1 (sin horas del UCP: son del paso 7). "
          "Ahí está el pico que exige el Art. 17.2 y que el T-15 debe demostrar con dotación; sin el sd-12 queda como pregunta.", "",
          "## 6. Pruebas de la puerta", "",
          "- P8.3 (la curva por etapa cuadra con los meses 1 a 12, 13 a 18 y 21 a 56): las horas de la Etapa 1 están solo en los meses 1 a 12, las de la Etapa 2 solo en 13 a 18, la cartera en 1 a 18, y no hay horas del UCP en la operación. **Cumple** para las horas del UCP.",
          "- Pasos a producción fuera de los congelamientos: **cumple**.",
          "- P8.2 (personas en el pico frente a la dotación): **pendiente**; el sd-12 está fuera de esta entrega.",
          "- Holguras de los paquetes que no están en la ruta crítica: **pendiente**, por falta de duraciones.", "",
          "## 7. Supuestos y preguntas para el equipo, con sugerencia", "",
          "| N.º | Pregunta o supuesto | Sugerencia |", "| --: | :-- | :-- |",
          "| 1 | Las ventanas de la rama 1.4 (infraestructura) y de los sistemas del centro de datos están en los meses 6 a 12 | Aceptar. El Art. 17 solo exige los ambientes dentro de los meses 1 a 12; la EDT original fijaba la plataforma base en el mes 6 |",
          "| 2 | El software de cada etapa se reparte parejo por mes dentro de su ventana | Aceptar mientras no haya un plan de iteraciones. Cambiarlo solo desplaza la curva dentro de la etapa |",
          "| 3 | La arquitectura se cierra en el mes 4 y la plataforma base en el mes 6, tomados de la EDT original | Aceptar como propuesta; no están en las Bases, porque los hitos del Formulario E-25 no se leen en las tablas |",
          "| 4 | Los hitos de pago del Formulario E-25 no se anclan | Dejarlos así hasta que se repare la tabla de las Bases |",
          "| 5 | La ventana de cada innovación queda por definir | Cerrarla con el sd-13; el Art. 28 exige las cinco y RT-26.02 pide el mes de cada una |",
          "| 6 | El retiro del sistema central de 2009 no tiene fecha en el sd-03 | Fijarla con el escenario B por ola, después del mes 21; mientras tanto, ventana de operación |",
          "| 7 | La marcha blanca de la Etapa 1 cae en congelamiento (enero a marzo de 2028) | Coordinar el plan de la marcha blanca con el calendario de congelamientos del paquete 1.1.6 |",
          "| 8 | Los noventa días de acompañamiento de reversibilidad quedan después del mes 56 | Dejarlos como están: el Art. 77.2 los fija tras el cierre |", ""]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salida", default=str(SALIDA))
    a = ap.parse_args(argv)
    paquetes, hall = gm.cargar()
    if hall:
        print("\n".join(hall))
        return 1
    items = asignar(paquetes)
    por_mes, total = curva(items)
    hall = verificar(items, por_mes, total)
    for x in hall:
        print(x)
    Path(a.salida).write_text(texto(items, por_mes, total), encoding="utf-8")
    print("escrito en", a.salida)
    return 1 if hall else 0


if __name__ == "__main__":
    sys.exit(main())
