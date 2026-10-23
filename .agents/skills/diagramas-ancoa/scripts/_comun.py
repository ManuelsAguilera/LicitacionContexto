"""Utilidades compartidas: carga del catálogo y de la especificación del diagrama."""
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CATALOGO = json.loads((RAIZ / "catalogo.json").read_text(encoding="utf-8"))

NOMBRES_COLOR = {
    "#5B6770": "gris",
    "#9E9E9E": "gris claro",
    "#B08A2E": "ocre",
    "#C77700": "ámbar",
    "#1F7A8C": "azul verdoso",
    "#C62828": "roja",
    "#333333": "negra",
    "#C2185B": "magenta",
}
NOMBRES_TRAZO = {"solid": "continua", "dashed": "discontinua", "dotted": "punteada", "dashdot": "punto y raya", "longdash": "de trazo largo"}


def cargar_spec(ruta):
    try:
        return json.loads(pathlib.Path(ruta).read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR: la especificación no es JSON válido: {e}")


def estilo_de(spec):
    return CATALOGO["estilos"].get(spec.get("estilo", ""))


def frente_de_nodo(nodo, grupos_por_id):
    """Frente efectivo de un nodo: el propio o el heredado de su grupo (y ancestros)."""
    if nodo.get("frente"):
        return nodo["frente"]
    gid = nodo.get("grupo")
    while gid:
        g = grupos_por_id.get(gid)
        if not g:
            return None
        if g.get("frente"):
            return g["frente"]
        gid = g.get("padre")
    return None


def grupo_raiz(gid, grupos_por_id):
    while gid and grupos_por_id.get(gid, {}).get("padre"):
        gid = grupos_por_id[gid]["padre"]
    return gid


def leyenda(spec):
    """Entradas de leyenda generadas SOLO a partir de lo que el diagrama usa."""
    est = CATALOGO["estados_nodo"]
    sem = CATALOGO["semanticas_enlace"]
    usados_estado = []
    for n in spec.get("nodos", []):
        e = n.get("estado", "objetivo")
        if e != "objetivo" and e not in usados_estado:
            usados_estado.append(e)
    usados_sem = []
    for a in spec.get("enlaces", []):
        s = a.get("semantica")
        if s not in usados_sem:
            usados_sem.append(s)
    lineas = []
    for s in usados_sem:
        d = sem[s]
        lineas.append(("sem:" + s, f"línea {NOMBRES_TRAZO[d['estilo']]} {NOMBRES_COLOR.get(d['color'], '')}".strip() + f": {d['descripcion']}"))
    for e in usados_estado:
        d = est[e]
        if e == "convivencia":
            txt = "caja gris discontinua: " + d["descripcion"]
        elif e == "por_acreditar":
            txt = "caja ámbar discontinua: " + d["descripcion"]
        elif e == "condicionado":
            txt = "asterisco (*): " + d["descripcion"]
        else:
            txt = "rótulo «(propuesto)»: " + d["descripcion"]
        lineas.append(("est:" + e, txt))
    return lineas
