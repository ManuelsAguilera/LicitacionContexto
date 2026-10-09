#!/usr/bin/env python3
"""Estructura del diccionario de la EDT por paquete (Formulario T-14, sección 7.1; FEP02, diapositiva 57).

Genera una ficha por paquete de `14_edt_corregida.md` con los doce campos de la clase. Llena solo lo que se puede derivar de los
artefactos del proyecto (casos de uso, RF, resultados del Anexo D, exclusiones del Anexo A, cronograma, horas del UCP) y marca cada
valor como [derivado], [propuesta], [manual] o [por definir]. Nada se inventa: lo que no tiene fuente queda «por definir».
Los valores que escriben las personas van en `19_diccionario_campos_manuales.md` (una fila por código y campo) y ganan sobre los derivados;
así el diccionario se puede regenerar sin perderlos. Escribe `18_diccionario_edt.md`.

    python3 05_Gestion/scripts/generar_diccionario.py [PLANILLA.md ...] [--manual RUTA] [--salida RUTA]

Código de salida 0 si la estructura es coherente (cada paquete con sus doce campos, ajustes con código y campo válidos) y 1 si no.
Que haya campos «por definir» no es un error: se informa en el resumen.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_cronograma as gc  # noqa: E402
import generar_mapa_paquetes as gm  # noqa: E402
import repartir_horas_paquetes as rh  # noqa: E402
import verificar_casos_uso as vcu  # noqa: E402

DIR = gm.DIR
SALIDA = DIR / "18_diccionario_edt.md"
MANUAL = DIR / "19_diccionario_campos_manuales.md"
ANEXO_D = vcu.RAIZ / "04_Adjuntos" / "tablas" / "sd-03_s2_anexo-d_criterios-aceptacion.md"
PD = "por definir"

CAMPOS = [  # (clave, etiqueta de la clase)
    ("descripcion", "Descripción del trabajo"), ("fuera", "Queda fuera"), ("entregable", "Entregable"),
    ("criterio", "Criterio de aceptación"), ("responsable", "Responsable"), ("hitos", "Hitos asociados"),
    ("esfuerzo", "Esfuerzo estimado"), ("costo", "Costo estimado"), ("recursos", "Recursos requeridos"),
    ("supuestos", "Supuestos"), ("referencias", "Referencias"),
]
CLAVES = {c for c, _ in CAMPOS}

RESPONSABLE_POR_RAMA = {  # roles del sd-01 (apartado 1.2); asignación propuesta de este trabajo
    "1.1": "Jefe de Proyecto", "1.2": "Arquitecto de Solución", "1.3": "Arquitecto de Solución",
    "1.4": "Arquitecto de Solución, con apoyo del Líder de Operación", "1.5": "Arquitecto de Solución",
    "1.6": "Arquitecto de Solución, con apoyo del Líder de Datos", "1.7": "Líder de Datos",
    "1.8": "Encargado de Seguridad de la Información", "1.9": "Líder de Calidad",
    "1.10": PD, "1.11": "Líder de Implantación y Gestión del Cambio",
    "1.12": "Líder de Implantación y Gestión del Cambio, con apoyo del Líder de Calidad",
    "1.13": "Líder de Implantación y Gestión del Cambio", "1.14": "Jefe de Proyecto", "1.15": "Líder de Operación",
}
RESPONSABLE_POR_PAQUETE = {
    "1.12.4": "Jefe de Proyecto", "1.12.7": "Jefe de Proyecto", "1.12.8": "Jefe de Proyecto", "1.14.8": "Jefe de Proyecto",
    "1.7.13": "Líder de Implantación y Gestión del Cambio", "1.11.5": "Líder de Implantación y Gestión del Cambio",
    "1.4.17": "Líder de Operación", "1.4.18": "Líder de Operación", "1.14.3": "Jefe de Proyecto, con apoyo del Líder de Operación",
    "1.14.4": "Líder de Operación", "1.14.5": "Líder de Operación", "1.14.6": "Jefe de Proyecto",
}
HITOS_SOFTWARE = {
    "1": "Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16)",
    "2": "Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21)",
    "1 y 2": "Pasos a producción de la Etapa 1 (mes 16) y de la Etapa 2 (mes 21), con la cartera migrada por tramos",
}
TIPOS = [("Plan", "plan"), ("Informe", "informe"), ("Acta", "acta"), ("Registro", "registro"), ("Mapa", "documento"),
         ("Inventario", "documento"), ("Matriz", "documento"), ("Catálogo", "documento"), ("Estudio", "documento"),
         ("Documento", "documento"), ("Documentación", "documento"), ("Especificación", "documento"), ("Modelo", "documento"),
         ("Arquitectura", "documento"), ("Calendario", "documento"), ("Declaración", "documento"), ("Protocolo", "documento"),
         ("Manuales", "documento"), ("Base de conocimiento", "documento"), ("Estándares", "documento"), ("Línea base", "documento"),
         ("Contratos", "documento"), ("Revisión", "informe"), ("Atestación", "informe"), ("Batería", "informe de pruebas"),
         ("Ensayo", "informe de pruebas"), ("Pruebas", "informe de pruebas"), ("Certificación", "acta"),
         ("Entorno", "entorno operando"), ("Ambientes", "entorno operando"), ("Sistema", "sistema operando"), ("Solución", "sistema operando"),
         ("Servicio", "servicio operando"), ("Plataforma", "plataforma operando"), ("Mesa", "servicio operando"), ("Control", "sistema operando")]


def anexo_d_metas():
    out = {}
    for cab, filas in vcu.tablas(ANEXO_D.read_text(encoding="utf-8")):
        if cab[:2] == ["N.º", "Resultado esperado"]:
            for f in filas:
                if f[0].isdigit():
                    out[int(f[0])] = {"resultado": f[1], "meta": f[3]}
    return out


def anexo_a():
    out = {}
    for linea in vcu.ANEXO_A.read_text(encoding="utf-8").splitlines():
        if re.match(r"\|\s*(EXC|SP|RC)-\d+", linea):
            c = vcu.celdas(linea)
            out[c[0]] = c[1]
    return out


def casos_con_supuestos():
    out = {}
    for p in sorted(Path(DIR).glob("03_casos_de_uso_*.md")):
        for cab, filas in vcu.tablas(p.read_text(encoding="utf-8")):
            if cab[:2] == ["Código", "Servicio"] and len(cab) >= 7:
                for f in filas:
                    out[f[0]] = {"nombre": f[2], "actor": f[3], "origen": f[5], "supuestos": f[6], "archivo": p.name}
    return out


def leer_manual(ruta):
    """{(código, clave): valor} desde la tabla `| Código | Campo | Valor | Fuente |` y la lista de hallazgos."""
    out, hall = {}, []
    if not Path(ruta).exists():
        return out, hall
    for cab, filas in vcu.tablas(Path(ruta).read_text(encoding="utf-8")):
        if cab[:3] == ["Código", "Campo", "Valor"]:
            for f in filas:
                if not f[0] or not f[2]:
                    continue
                clave = {e.lower(): c for c, e in CAMPOS}.get(f[1].lower(), f[1].lower())
                out[(f[0], clave)] = (f[2], f[3] if len(f) > 3 else "")
    return out, hall


def meses(a, b):
    return f"el mes {a}" if a == b else f"los meses {a} a {b}"


def tipo_entregable(nombre):
    for ini, tipo in TIPOS:
        if nombre.startswith(ini):
            return tipo
    return None


def construir(planillas=(), manual=MANUAL):
    paquetes, h = gm.cargar()
    if h:
        raise SystemExit("\n".join(h))
    items = gc.asignar(paquetes)
    ventanas = {p["codigo"]: p["ventana"] for p in items}
    filas_h, total = rh.calcular(planillas)
    horas = {f["codigo"]: f for f in filas_h}
    metas, anx_a, casos = anexo_d_metas(), anexo_a(), casos_con_supuestos()
    traza = vcu.trazabilidad(DIR) or {}
    resultados_de = {}
    for n, cs in traza.items():
        for c in cs:
            resultados_de.setdefault(c, set()).add(n)
    rl = leer_manual(manual)[0]
    fichas, hall = [], []
    codigos = {p["codigo"] for p in paquetes}
    for (cod, clave), _ in rl.items():
        if cod not in codigos:
            hall.append(f"ajuste manual: el paquete {cod} no existe")
        if clave not in CLAVES:
            hall.append(f"ajuste manual: el campo «{clave}» no existe (use uno de: {', '.join(e for _, e in CAMPOS)})")
    for p in paquetes:
        cod = p["codigo"]
        vals = {}
        casos_p = [casos[c] | {"codigo": c} for c in p["casos"] if c in casos]
        ventana = ventanas[cod]
        # descripción y entregable
        if casos_p:
            vals["descripcion"] = (f"Análisis, diseño, construcción y pruebas de los casos de uso: " +
                                   "; ".join(f"{c['codigo']} {c['nombre']}" for c in casos_p) + ".", "derivado")
            vals["entregable"] = (f"Componentes de software de «{p['nodo']}» que resuelven esos casos de uso, desplegados y probados.", "derivado")
        else:
            vals["descripcion"] = (PD, "por definir")
            t = tipo_entregable(p["nombre"])
            vals["entregable"] = ((f"Por definir. Tipo probable: {t}; falta concretar el artefacto.", "por definir") if t else (PD, "por definir"))
        # queda fuera
        excl = []
        for c in casos_p:
            for x in re.findall(r"\b(?:EXC|SP|RC)-\d+\b", c["origen"]):
                if x in anx_a and x not in excl:
                    excl.append(x)
        for x in re.findall(r"\b(?:EXC|SP|RC)-\d+\b", p["origen"]):
            if x in anx_a and x not in excl:
                excl.append(x)
        vals["fuera"] = (("; ".join(f"{x}: {anx_a[x]}" for x in excl) + ".", "derivado") if excl else (PD, "por definir"))
        # criterio de aceptación
        res = sorted({n for c in p["casos"] for n in resultados_de.get(c, ())})
        if res:
            vals["criterio"] = ("; ".join(f"Resultado {n} del Anexo D: {metas[n]['meta']}" for n in res if n in metas), "derivado")
        else:
            vals["criterio"] = (PD, "por definir")
        # responsable
        resp = RESPONSABLE_POR_PAQUETE.get(cod) or RESPONSABLE_POR_RAMA.get(p["rama"], PD)
        vals["responsable"] = ((f"{resp}. Acepta la Contraparte Técnica (Art. 18.1).", "propuesta") if resp != PD else (PD, "por definir"))
        # hitos
        if p["metodo"] == "UCP":
            vals["hitos"] = (HITOS_SOFTWARE[p["etapa"]], "derivado")
        elif ventana and ventana[2] == gc.C:
            vals["hitos"] = (f"Ventana de {meses(ventana[0], ventana[1])}, fijada por el contrato ({ventana[3]}).", "derivado")
        else:
            vals["hitos"] = ("Hitos del Formulario E-25: por definir.", "por definir")
        # esfuerzo, costo y recursos
        f = horas[cod]
        if f["fuente"] == "UCP":
            hh = f["horas"]
            vals["esfuerzo"] = (f"{rh.cm.h(hh)} h en total (UCP, escenario del equipo): análisis {rh.cm.h(hh * .10)} h, diseño {rh.cm.h(hh * .20)} h, "
                                f"programación {rh.cm.h(hh * .40)} h, pruebas {rh.cm.h(hh * .15)} h y sobrecarga {rh.cm.h(hh * .15)} h. Por perfil: por estimar (sd-12).", "derivado")
        elif f["fuente"] == "tres valores":
            vals["esfuerzo"] = (f"{rh.cm.h(f['horas'])} h (media de tres valores). Por perfil: por estimar (sd-12).", "derivado")
        else:
            vals["esfuerzo"] = ("Por estimar (planilla de tres valores, Formulario T-15).", "por definir")
        vals["costo"] = ("Por estimar; los montos viven solo en el Sobre Económico.", "por definir")
        vals["recursos"] = ("Por definir con el sd-12.", "por definir")
        # supuestos
        sup = []
        if casos_p:
            for c in casos_p:
                ss = [s.strip() for s in c["supuestos"].split(",") if s.strip()]
                if ss:
                    sup.append(f"{c['codigo']} ({c['archivo']}): {', '.join(ss)}")
        if ventana:
            sup.append(f"Ventana de {meses(ventana[0], ventana[1])} ({ventana[2]}): {ventana[3]}")
        else:
            sup.append("Ventana por definir")
        vals["supuestos"] = ("; ".join(sup) + ".", "derivado")
        # referencias
        ref = []
        if p["rf"]:
            ref.append(gm.rango_rf(p["rf"]))
        if p["casos"]:
            ref.append("casos de uso " + ", ".join(p["casos"]))
        if res:
            ref.append("resultados del Anexo D: " + ", ".join(str(n) for n in res))
        if p["origen"]:
            ref.append(p["origen"])
        vals["referencias"] = (("; ".join(ref) + ".", "derivado") if ref else (PD, "por definir"))
        # ajustes manuales
        for clave in CLAVES:
            if (cod, clave) in rl:
                vals[clave] = (rl[(cod, clave)][0], "manual")
        fichas.append({"paquete": p, "vals": vals, "ventana": ventana})
    return fichas, hall


def resumen(fichas):
    estados = {}
    for f in fichas:
        for clave, (_, e) in f["vals"].items():
            estados.setdefault(clave, {}).setdefault(e, 0)
            estados[clave][e] += 1
    return estados


def texto(fichas, hall=()):
    n = len(fichas)
    L = ["# Diccionario de la EDT por paquete (estructura)", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_diccionario.py` a partir de `14_edt_corregida.md`; no editar a mano. "
         "Los valores que escriben las personas van en `19_diccionario_campos_manuales.md` y se aplican al regenerar. Fecha: 2026-10-08. "
         "Estado: **estructura**. Base: Formulario T-14 y sección 7.1 del Comunicado 10 (entregable, criterio de aceptación y responsable por paquete) y los doce campos de la clase FEP02 (diapositiva 57). "
         "Cada valor lleva su estado: **[derivado]** sale de un artefacto del proyecto, **[propuesta]** lo propone este trabajo y debe validarse, **[manual]** lo escribió una persona y **[por definir]** no tiene fuente todavía.", "",
         "## 1. Estado de llenado", "",
         "| Campo | Derivado | Propuesta | Manual | Por definir |", "| :-- | --: | --: | --: | --: |"]
    est = resumen(fichas)
    for clave, etiqueta in CAMPOS:
        e = est.get(clave, {})
        L.append(f"| {etiqueta} | {e.get('derivado', 0)} | {e.get('propuesta', 0)} | {e.get('manual', 0)} | {e.get('por definir', 0)} |")
    req = ["entregable", "criterio", "responsable"]
    con_valor = sum(1 for f in fichas if all(f["vals"][k][1] != "por definir" for k in req))
    firmes = sum(1 for f in fichas if all(f["vals"][k][1] in ("derivado", "manual") for k in req))
    L += ["", f"Los tres campos que exige el Comunicado 10 (entregable, criterio de aceptación y responsable) tienen valor en {con_valor} de {n} paquetes, "
          f"contando las propuestas, y valor derivado o manual en {firmes}. Una fila «propuesta» todavía no es una decisión del equipo; el responsable es siempre propuesta hasta que el equipo lo valide.", "",
          "## 2. Cómo se completa", "",
          "1. Se escribe cada valor en `19_diccionario_campos_manuales.md` (código del paquete, campo, valor y fuente).",
          "2. Se corre `python3 05_Gestion/scripts/generar_diccionario.py` y el valor aparece como **[manual]**.",
          "3. El criterio de aceptación sale del Anexo B (umbrales) o del Anexo D (metas); si no existe, se deja «por definir».",
          "4. El responsable es siempre un rol. Los roles del proponente son los del sd-01, apartado 1.2; la dotación y la dedicación son del sd-12.", "",
          "## 3. Fichas", ""]
    ramas = {}
    for f in fichas:
        ramas.setdefault(f["paquete"]["rama"], []).append(f)
    for rama in sorted(ramas, key=lambda x: [int(y) for y in x.split(".")]):
        L += [f"### Rama {rama}", ""]
        for f in ramas[rama]:
            p, vals, v = f["paquete"], f["vals"], f["ventana"]
            L += [f"#### {p['codigo']} {p['nombre']}", "",
                  f"- **Rama y servicio:** {rama}" + (f", {p['nodo']}" if p["nodo"] else "") + f". **Etapa:** {p['etapa']}. **Método:** {p['metodo']}.",
                  f"- **Ventana:** " + (f"{meses(v[0], v[1])} ({v[2]})" if v else "por definir")]
            for clave, etiqueta in CAMPOS:
                valor, estado = vals[clave]
                L.append(f"- **{etiqueta}:** {valor} [{estado}]")
            L.append("")
    return "\n".join(L)


PLANTILLA_MANUAL = """# Campos manuales del diccionario de la EDT

Documento de contexto, no es entregable. Aquí se escriben los valores del diccionario que dependen de una persona. `generar_diccionario.py` los lee y gana sobre los derivados. Una fila por código y campo.

Campos válidos: Descripción del trabajo, Queda fuera, Entregable, Criterio de aceptación, Responsable, Hitos asociados, Esfuerzo estimado, Costo estimado, Recursos requeridos, Supuestos y Referencias. El criterio sale del Anexo B o D; si no existe, no se escribe nada y queda «por definir». No se escriben nombres de personas en Responsable: solo roles. Los costos no se escriben aquí: viven en el Sobre Económico.

| Código | Campo | Valor | Fuente |
| :-- | :-- | :-- | :-- |
"""


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("planillas", nargs="*")
    ap.add_argument("--manual", default=str(MANUAL))
    ap.add_argument("--salida", default=str(SALIDA))
    a = ap.parse_args(argv)
    fichas, hall = construir(a.planillas, a.manual)
    for x in hall:
        print(x)
    Path(a.salida).write_text(texto(fichas, hall), encoding="utf-8")
    print("escrito en", a.salida)
    est = resumen(fichas)
    print("; ".join(f"{e}: {sum(d.get(k, 0) for d in est.values())}" for e, k in (("derivado", "derivado"), ("propuesta", "propuesta"), ("manual", "manual"), ("por definir", "por definir"))))
    return 1 if hall else 0


if __name__ == "__main__":
    sys.exit(main())
