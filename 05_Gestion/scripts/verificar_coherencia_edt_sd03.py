#!/usr/bin/env python3
"""Coherencia hacia atrás de la EDT con el subdocumento 3 (`sd-03.tex` y sus anexos).

Comprueba, sin criterio humano, que la EDT corregida (`14_edt_corregida.md`) no contradice al sd-03:
etapa de cada servicio frente a la Tabla 3.1, cantidades de la Tabla 3.4 frente al Anexo B, los 227 RF y las 9 obligaciones en alguna cuenta,
los 28 resultados del Anexo D trazables a una cuenta, y los compromisos del sd-03 (piloto, corte de enlace, compuertas, planes alternativos…)
que deben tener un entregable en la EDT. Los compromisos se buscan por palabras clave en los nombres y el origen de las cuentas. Escribe
`22_coherencia_edt_sd03.md`.

    python3 05_Gestion/scripts/verificar_coherencia_edt_sd03.py [--edt RUTA] [--salida RUTA]

Código de salida 0 si no hay incoherencias y 1 si las hay.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_cronograma as gc  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402
import verificar_casos_uso as vcu  # noqa: E402

RAIZ = vcu.RAIZ
SD03 = RAIZ / "02_Propuesta" / "latex_final" / "sd-03.tex"
SALIDA = gm.DIR / "22_coherencia_edt_sd03.md"
NODO_BASE = "Base tecnológica"

# Compromisos del sd-03 que exigen un entregable en la EDT.
# (id, sección del sd-03, compromiso, expresión que debe aparecer, ventana que fija el sd-03 o None, gravedad, cuenta propuesta si falta)
COMPROMISOS = [
    ("K1", "3.2.2", "Un nuevo punto de venta capaz de operar sin conexión en las 22 tiendas es parte de la Etapa 1 (y componente de la Tabla 3.1)",
     r"punto de venta|\bPOS\b", None, "A", "Punto de venta nuevo con operación sin conexión para las 22 tiendas"),
    ("K2", "3.3.1 y 3.4.5", "El punto de venta de 2014 se sustituye tienda por tienda tras acreditar la operación sin conexión y el retorno",
     r"2014", None, "A", "Sustitución del punto de venta de 2014 tienda por tienda y su retiro"),
    ("K3", "3.2.3", "Piloto del punto de venta en tres tiendas",
     r"piloto", (6, 7), "A", "Piloto del punto de venta en tres tiendas con corte de enlace de 24 horas"),
    ("K4", "3.2.3 y 3.4.5", "Corte de enlace provocado de 24 horas en una tienda del piloto, en los meses 6 y 7, fuera de los congelamientos, con retorno ensayado",
     r"corte de enlace|enlace provocado", (6, 7), "A", "Informe de la prueba del corte de enlace de 24 horas"),
    ("K5", "3.4.5", "Modalidad de contingencia tributaria aprobada y probada antes de comprometer la operación sin enlace",
     r"contingencia", None, "M", "Modalidad de contingencia tributaria aprobada y probada con el ERP/DTE"),
    ("K6", "3.2.3", "El proponente propone los criterios del cupo preaprobado y la filial emisora los fija antes de la prueba",
     r"cupo preaprobado|criterios del cupo", None, "M", "Propuesta de criterios del cupo preaprobado para la filial emisora"),
    ("K7", "3.2.3", "Compuerta de cada tramo de la cartera, cerrada por la Contraparte Técnica y la filial emisora",
     r"compuerta", None, "A", "Actas de compuerta por tramo de la cartera"),
    ("K8", "3.2.3", "Plan de comunicación a los clientes en la migración de la cartera",
     r"comunicaci[oó]n a (los )?clientes|comunicaci[oó]n con (los )?clientes|plan de comunicaci[oó]n", None, "A", "Plan de comunicación a los clientes de la cartera por tramo"),
    ("K9", "3.2.3", "Plan alternativo para cada una de las dos condiciones del adelanto del negocio financiero (crédito con corte de enlace y convivencia con la plataforma de 2011)",
     r"planes? alternativos?|alternativa de continuidad", None, "A", "Planes alternativos de las dos condiciones del adelanto del negocio financiero"),
    ("K10", "3.3.1", "Evaluación de comercio electrónico y fidelización con las pruebas de la primera etapa, y decisión de conservar, remediar o sustituir cada plataforma antes de su ola",
     r"evaluaci[oó]n.*(comercio electr|fideliz)|comercio electr.*evaluaci", None, "M", "Informe de evaluación de comercio electrónico y fidelización"),
    ("K11", "3.4.6", "Pruebas de tareas del punto de venta con cajeros nuevos y experimentados antes del despliegue",
     r"usabilidad|cajeros", None, "M", "Informe de pruebas de tareas del punto de venta con cajeros"),
    ("K12", "3.4.6", "Pruebas de comprensión de precios, entrega e información crediticia con clientes y titulares",
     r"comprensi[oó]n", None, "B", "Informe de pruebas de comprensión con clientes y titulares"),
    ("K13", "3.3.1", "Nueve plataformas: la novena (planillas y listas impresas) deja de ser registro oficial; el levantamiento documenta las catorce interfaces",
     r"14 interfaces", None, "B", "Mapa de las 14 interfaces"),
    ("K14", "3.2.2", "Retiro de la plataforma de crédito de 2011 en octubre de 2028 (mes 22)",
     r"2011.*fuera de servicio|fuera de servicio.*2011", (22, 22), "B", "Plataforma de originación y cobranza de 2011 fuera de servicio"),
    ("K15", "3.2.2", "La recuperación ante desastres se prueba dos veces al año en operación",
     r"recuperaci[oó]n ante desastres", None, "B", "Pruebas periódicas de recuperación ante desastres"),
    ("K16", "3.4.1", "Pruebas en preproducción a 1,5 veces el peak declarado y estrés hasta el punto de quiebre",
     r"carga, estr[eé]s|desempe[ñn]o", None, "B", "Pruebas de carga, estrés y resiliencia"),
]

SERVICIOS_SD03 = {  # Tabla 3.1 y 3.2.2
    "Servicio de oferta comercial": "1", "Servicio de existencias": "1", "Servicio de ventas": "1", "Servicio de originación de crédito": "1",
    "Servicio de evidencia financiera": "1", "Servicio de control de cruces": "1", "Servicio de cartera de crédito": "1 y 2",
    "Servicio de abastecimiento": "2", "Servicio de pedidos": "2", "Servicio de comisiones": "2", "Servicio de marketplace": "2",
    "Servicio de posventa": "2", "Servicio de clientes Retail": "2", NODO_BASE: "1",
}


def tabla_31(sd03=SD03):
    """{componente: etapa} desde la Tabla 3.1 de `sd-03.tex` (filas `Componente & Prueba & Etapa \\\\`)."""
    out = {}
    for linea in Path(sd03).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(Servicio de [^&]+|Base tecnológica[^&]*|Punto de venta[^&]*)&[^&]*&\s*([12](?: y 2)?)\s*\\\\\s*$", linea)
        if m:
            out[m.group(1).strip()] = m.group(2)
    return out


def tabla_34(sd03=SD03):
    """Filas de la Tabla 3.4: {etiqueta: (RF, RNF, OP)}."""
    out = {}
    for linea in Path(sd03).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(Etapa 1|Etapas 1 y 2 \(cartera por tramos\)|Etapa 2) & (\d+) & (\d+) & (\d+) \\\\", linea)
        if m:
            out[m.group(1)] = tuple(int(m.group(i)) for i in (2, 3, 4))
    return out


def anexo_b_por_etapa():
    f, nf = {}, {}
    for linea in vcu.ANEXO_B.read_text(encoding="utf-8").splitlines():
        c = vcu.celdas(linea) if linea.startswith("|") else []
        if len(c) >= 5 and re.fullmatch(r"RF-\d+", c[0]):
            f[c[4]] = f.get(c[4], 0) + 1
        elif len(c) >= 5 and re.fullmatch(r"RNF-\d+", c[0]):
            nf[c[0]] = c[4] if len(c) > 4 else ""
    return f, nf


def comprobar(edt=gm.EDT, directorio=vcu.DIR, sd03=SD03):
    paquetes, h_mapa = gm.cargar(edt, directorio)
    items = gc.asignar(paquetes)
    res = {"mecanicas": [], "compromisos": [], "hallazgos": list(h_mapa)}
    M = res["mecanicas"]
    # 1. etapas de los servicios frente a la Tabla 3.1
    t31 = tabla_31(sd03)
    por_nodo = {}
    for p in paquetes:
        if p["metodo"] == "UCP":
            por_nodo.setdefault(p["nodo"], set()).add(p["etapa"])
    mal = [f"{n}: EDT {sorted(e)} y sd-03 {SERVICIOS_SD03.get(n)}" for n, e in por_nodo.items()
           if e != {SERVICIOS_SD03.get(n)}]
    contra_tabla = [f"{n}: sd-03 {t31[n]} y esperado {SERVICIOS_SD03[n]}" for n in SERVICIOS_SD03 if n in t31 and t31[n] != SERVICIOS_SD03[n]]
    M.append(("La etapa de cada servicio coincide con la Tabla 3.1 (13 servicios y la base tecnológica)",
              not mal and not contra_tabla and len(por_nodo) == 14, f"{len(por_nodo)} nodos revisados" + ("" if not (mal or contra_tabla) else ": " + "; ".join(mal + contra_tabla))))
    # 2. Tabla 3.4 frente al Anexo B
    t34, (rf_et, _) = tabla_34(sd03), anexo_b_por_etapa()
    esperado = {"Etapa 1": rf_et.get("1", 0), "Etapas 1 y 2 (cartera por tramos)": rf_et.get("1 y 2", 0), "Etapa 2": rf_et.get("2", 0)}
    obtenido = {k: t34[k][0] for k in esperado if k in t34}
    M.append(("La Tabla 3.4 (RF por etapa) coincide con el Anexo B", obtenido == esperado, f"Tabla 3.4 {obtenido}; Anexo B {esperado}"))
    # 3. RF por etapa de cada cuenta
    et_rf = {}
    for linea in vcu.ANEXO_B.read_text(encoding="utf-8").splitlines():
        c = vcu.celdas(linea) if linea.startswith("|") else []
        if len(c) >= 5 and re.fullmatch(r"RF-\d+", c[0]):
            et_rf[c[0]] = c[4]
    malas = [p["codigo"] for p in paquetes if p["metodo"] == "UCP" and {et_rf[r] for r in p["rf"] if r in et_rf} not in ({p["etapa"]}, {"1 y 2"} if p["etapa"] == "1 y 2" else set())
             and not (p["etapa"] == "1 y 2" and {et_rf[r] for r in p["rf"] if r in et_rf} <= {"1", "2", "1 y 2"})]
    M.append(("La etapa de cada cuenta de software coincide con la etapa de sus RF en el Anexo B", not malas, "todas coinciden" if not malas else ", ".join(malas)))
    # 4. los 227 RF en alguna cuenta (ya lo comprueba gm.cargar)
    M.append(("Los 227 RF del Anexo B están en alguna cuenta de control", not [x for x in h_mapa if "RF sin paquete" in x], f"{len(et_rf)} RF"))
    # 5. las 9 obligaciones
    ops = set()
    for p in paquetes:
        for a, b in re.findall(r"OP-(\d+)\s+a\s+OP-(\d+)", p["origen"]):
            ops.update(range(int(a), int(b) + 1))
        ops.update(int(x) for x in re.findall(r"OP-(\d+)", re.sub(r"OP-\d+\s+a\s+OP-\d+", "", p["origen"])))
    faltan = sorted(set(range(1, 10)) - ops)
    M.append(("Las 9 obligaciones del proponente (OP-01 a OP-09) están en alguna cuenta", not faltan, "todas" if not faltan else "faltan OP-" + ", OP-".join(f"{x:02d}" for x in faltan)))
    # 6. los 28 resultados del Anexo D
    tr = vcu.trazabilidad(directorio) or {}
    caso2 = {c: p["codigo"] for p in paquetes for c in p["casos"]}
    sin = [n for n in range(1, 29) if not {caso2[c] for c in tr.get(n, []) if c in caso2}]
    M.append(("Los 28 resultados del Anexo D se rastrean a una cuenta de control", not sin, "todos" if not sin else "sin cuenta: " + ", ".join(map(str, sin))))
    # 7. nada excluido como trabajo propio
    malos = [p["codigo"] for p in paquetes if re.search(vcu.VERBOS_EXCLUIDOS, p["nombre"], re.I)]
    M.append(("Ninguna cuenta implementa algo excluido en el Anexo A (verbos de la prueba P3.4)", not malos, "ninguna" if not malos else ", ".join(malos)))
    # 8. compromisos
    texto = {p["codigo"]: (p["nombre"] + " " + p["origen"]) for p in paquetes}
    ventanas = {p["codigo"]: p["ventana"] for p in items}
    for cid, sec, comp, rx, ventana, grav, propuesta in COMPROMISOS:
        hit = [c for c, t in texto.items() if re.search(rx, t, re.I)]
        ok = bool(hit)
        nota = ""
        if ok and ventana:
            fuera = [c for c in hit if ventanas.get(c) and not (ventana[0] <= ventanas[c][0] and ventanas[c][1] <= ventana[1])]
            if fuera:
                ok, nota = False, f"está en {', '.join(fuera)} pero con una ventana que no cae en los meses {ventana[0]} a {ventana[1]} que fija el sd-03"
        res["compromisos"].append({"id": cid, "seccion": sec, "compromiso": comp, "cuentas": hit, "ok": ok, "nota": nota, "gravedad": grav,
                                   "propuesta": propuesta, "ventana": ventana})
    return res


def hallazgos(res):
    return [f"{m[0]}: {m[2]}" for m in res["mecanicas"] if not m[1]] + \
           [f"{c['id']} ({c['seccion']}): {c['compromiso']}" for c in res["compromisos"] if not c["ok"]]


def texto(res):
    L = ["# Coherencia hacia atrás de la EDT con el subdocumento 3", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/verificar_coherencia_edt_sd03.py`; no editar a mano. Fecha: 2026-10-08. "
         "Compara la EDT corregida (`14_edt_corregida.md`) con `sd-03.tex` y sus anexos. «Coherencia hacia atrás» significa que lo que la EDT promete debe poder trazarse a lo que el sd-03 ya dice, y lo que el sd-03 ya compromete debe tener un entregable en la EDT. "
         "Los compromisos se buscan por palabras clave en el nombre y el origen de las cuentas: es una comprobación mecánica, no sustituye la lectura del equipo.", "",
         "## 1. Comprobaciones mecánicas", "", "| Comprobación | Resultado | Detalle |", "| :-- | :-- | :-- |"]
    for nombre, ok, det in res["mecanicas"]:
        L.append(f"| {nombre} | {'cumple' if ok else '**NO cumple**'} | {det} |")
    L += ["", "## 2. Compromisos del sd-03 frente a la EDT", "",
          "| N.º | Sección del sd-03 | Compromiso | Gravedad | Estado | Cuenta de la EDT |", "| :-- | :-- | :-- | :-- | :-- | :-- |"]
    for c in res["compromisos"]:
        estado = "cubierto" if c["ok"] else ("**sin entregable**" if not c["cuentas"] else "**ventana incoherente**")
        cuentas = ", ".join(c["cuentas"][:4]) if c["cuentas"] else "—"
        L.append(f"| {c['id']} | {c['seccion']} | {c['compromiso']} | {c['gravedad']} | {estado} | {cuentas} |")
    falt = [c for c in res["compromisos"] if not c["ok"]]
    L += ["", f"Compromisos sin cubrir: **{len(falt)}** de {len(res['compromisos'])}. Gravedad A es lo que el sd-03 afirma de forma explícita como parte de la Etapa 1 o de sus condiciones; M, lo que el sd-03 pide para una prueba; B, lo que está cubierto de forma implícita.", "",
          "## 3. Cuentas que se proponen agregar o corregir", ""]
    if falt:
        L += ["| N.º | Cuenta propuesta | Ventana que fija el sd-03 | Rama sugerida |", "| :-- | :-- | :-- | :-- |"]
        rama = {"K1": "1.5 (nodo de ventas)", "K2": "1.7 (retiro de plataformas)", "K3": "1.11", "K4": "1.9", "K5": "1.5 (nodo de ventas)", "K6": "1.5 (nodo de originación de crédito)",
                "K7": "1.7", "K8": "1.7 o 1.13", "K9": "1.1", "K10": "1.2", "K11": "1.9", "K12": "1.9"}
        for c in falt:
            v = f"meses {c['ventana'][0]} a {c['ventana'][1]}" if c["ventana"] else "—"
            L.append(f"| {c['id']} | {c['propuesta']} | {v} | {rama.get(c['id'], '—')} |")
        L += [""]
    else:
        L += ["Ninguna: la EDT cubre todos los compromisos revisados.", ""]
    L += ["## 4. Qué no revisa", "",
          "- No lee la prosa del sd-03 buscando promesas nuevas; solo los compromisos de la lista (K1 a K16).",
          "- No valida que el contenido de una cuenta sea suficiente para cumplir el compromiso, solo que exista un entregable con ese tema.",
          "- Las cifras del Anexo D y las ventanas de los hitos obligatorios se comprueban en `04_trazabilidad_resultados.md` y `17_cronograma_edt.md`.", ""]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--edt", default=str(gm.EDT))
    ap.add_argument("--salida", default=str(SALIDA))
    a = ap.parse_args(argv)
    res = comprobar(a.edt)
    Path(a.salida).write_text(texto(res), encoding="utf-8")
    h = hallazgos(res)
    for x in h:
        print(x)
    print(f"{len(h)} incoherencia(s)")
    return 1 if h else 0


if __name__ == "__main__":
    sys.exit(main())
