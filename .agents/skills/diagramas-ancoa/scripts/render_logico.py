#!/usr/bin/env python3
"""Renderiza una especificación de estilo lógico (L1–L6) con la biblioteca diagrams + Graphviz.

Uso:  python3 scripts/render_logico.py ejemplos/mi_diagrama.json salida/mi_diagrama
Genera salida/mi_diagrama.png y .svg, más salida/mi_diagrama.leyenda.txt con el pie de figura.
La especificación se valida antes; si no cumple el catálogo, no se dibuja nada.
"""
import importlib
import pathlib
import sys

from diagrams import Cluster, Diagram, Edge, Node
from diagrams.custom import Custom

from _comun import CATALOGO, RAIZ, cargar_spec, frente_de_nodo, leyenda
from validar import validar

FUENTE = "Helvetica"
GRIS_TEXTO = "#333333"


def clase_icono(ruta):
    mod, cls = ruta.rsplit(".", 1)
    return getattr(importlib.import_module(mod), cls)


def rotulo(n, paso_por_nodo=None):
    est = CATALOGO["estados_nodo"].get(n.get("estado", "objetivo"), {})
    txt = n["etiqueta"] + est.get("sufijo", "")
    if n.get("codigo") and n["codigo"] not in txt:
        txt += "\n" + n["codigo"]
    return txt


def crear_nodo(n, gpid):
    tipo = n["tipo"]
    estado = n.get("estado", "objetivo")
    frente = frente_de_nodo(n, gpid) or "transversal"
    paleta = CATALOGO["frentes"][frente]
    defn = CATALOGO["tipos_nodo_logicos"][tipo]
    label = rotulo(n)

    # Componentes de convivencia o por acreditar se dibujan siempre como caja discontinua (Fig. 4.1–4.9)
    if estado in ("convivencia", "por_acreditar") or "forma" in defn:
        e = CATALOGO["estados_nodo"][estado]
        forma = defn.get("forma", "box")
        estilo = "rounded,filled" if forma == "box" else "filled"
        if e["trazo"] == "dashed":
            estilo += ",dashed"
        return Node(
            label,
            shape=forma,
            style=estilo,
            fillcolor=e["relleno"] or paleta["caja"],
            color=e["borde"] or paleta["borde"],
            fontcolor="#7A4A00" if estado == "por_acreditar" else GRIS_TEXTO,
            fontname=FUENTE,
            fontsize="11",
            fixedsize="false",
            width="1.6",
            height="0.6",
            margin="0.15,0.08",
            labelloc="c",
            imagescale="false",
        )
    icono = defn["icono"]
    if icono.startswith("assets/"):
        alto = "0.75" if tipo == "servicio" else "1.0"
        return Custom(label, str(RAIZ / icono), fontname=FUENTE, fontsize="11", fontcolor=GRIS_TEXTO,
                      width="1.0", height=alto)
    return clase_icono(icono)(label, fontname=FUENTE, fontsize="11", fontcolor=GRIS_TEXTO)


def renderizar(spec, salida):
    if spec.get('composicion') == 'bandas_horizontales':
        if any(n.get('id') == 'datos_credito' for n in spec.get('nodos',[])):
            from render_compacto_20261022 import renderizar as render_compacto
            return render_compacto(spec, salida)
        if any(n.get('id') in ('security_summary','mlflow_pg','blackbox_r') for n in spec.get('nodos',[])):
            from render_revision_registros import renderizar as render_revision
            return render_revision(spec, salida)
        if any(n.get('id') == 'common_admin' for n in spec.get('nodos',[])):
            from render_horizontal_capa4 import renderizar as render_capa4
            return render_capa4(spec, salida)
        from render_bandas_horizontales import renderizar as render_horizontal
        return render_horizontal(spec, salida)
    if spec.get('composicion') == 'columnas_legibles':
        from render_capas_legibles import renderizar as render_legible
        return render_legible(spec, salida)
    if spec.get('composicion') == 'columnas_decisiones':
        from render_decisiones_20261022 import renderizar as render_decisiones
        return render_decisiones(spec, salida)
    if spec.get('composicion') == 'columnas_organizadas':
        from render_capas_organizadas import renderizar as organizadas
        return organizadas(spec,salida)
    if spec.get('composicion') == 'columnas_referencia':
        from render_capas_referencia import renderizar as render_capas
        return render_capas(spec, salida)
    estilo = CATALOGO["estilos"][spec["estilo"]]
    grupos = spec.get("grupos", [])
    gpid = {g["id"]: g for g in grupos}
    creados = {}

    entradas = leyenda(spec)
    encabezado = spec.get("encabezado") or f"Ancoa · {spec['titulo']}"
    textos = [t for _, t in entradas]
    linea_leyenda = "\n".join("  ·  ".join(textos[i:i + 2]) for i in range(0, len(textos), 2))
    etiqueta_grafo = encabezado + ("\n" + linea_leyenda if linea_leyenda else "")

    graph_attr = {
        "rankdir": estilo["direccion"],
        "label": etiqueta_grafo,
        "labelloc": "t",
        "fontname": FUENTE,
        "fontsize": "13",
        "fontcolor": GRIS_TEXTO,
        "bgcolor": "white",
        "pad": "0.4",
        "nodesep": "0.55",
        "ranksep": "0.75",
        "splines": "spline",
        "compound": "true",
    }

    def dibujar_grupo(gid):
        g = gpid[gid]
        frente = frente_de_nodo({"grupo": gid}, gpid) or "transversal"
        pal = CATALOGO["frentes"][frente]
        attrs = {
            "bgcolor": pal["relleno"],
            "pencolor": pal["borde"],
            "style": "rounded",
            "fontname": FUENTE,
            "fontsize": "13",
            "fontcolor": GRIS_TEXTO,
            "labeljust": "l",
            "margin": "16",
        }
        with Cluster(g.get("etiqueta", ""), graph_attr=attrs):
            for hijo in grupos:
                if hijo.get("padre") == gid:
                    dibujar_grupo(hijo["id"])
            for n in spec["nodos"]:
                if n.get("grupo") == gid:
                    creados[n["id"]] = crear_nodo(n, gpid)

    salida = pathlib.Path(salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    with Diagram(
        "",
        filename=str(salida),
        outformat=["png", "svg"],
        show=False,
        direction=estilo["direccion"],
        graph_attr=graph_attr,
        edge_attr={"fontname": FUENTE, "fontsize": "10", "fontcolor": "#4A4A4A", "arrowsize": "0.7"},
    ):
        for n in spec["nodos"]:
            if not n.get("grupo"):
                creados[n["id"]] = crear_nodo(n, gpid)
        for g in grupos:
            if not g.get("padre"):
                dibujar_grupo(g["id"])
        for a in spec.get("enlaces", []):
            s = CATALOGO["semanticas_enlace"][a["semantica"]]
            label = a.get("etiqueta", "")
            if a.get("paso"):
                label = f"{a['paso']}. {label}".strip()
            creados[a["de"]] >> Edge(
                label=label,
                color=s["color"],
                style=s["estilo"],
                penwidth=str(s["grosor"]),
            ) >> creados[a["a"]]

    pie = f"Figura {spec.get('figura', '4.N')}: {spec['titulo']}\nFuente: {spec['fuente']}\n"
    (salida.parent / (salida.name + ".leyenda.txt")).write_text(
        pie + "Leyenda:\n" + "\n".join("- " + t for _, t in entradas) + "\n", encoding="utf-8")
    return salida


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    spec = cargar_spec(sys.argv[1])
    errores, avisos = validar(spec)
    if errores:
        print("\n".join("ERROR   " + e for e in errores))
        sys.exit("✗ No se renderiza: la especificación no cumple el catálogo.")
    if CATALOGO["estilos"][spec["estilo"]]["familia"] != "logica":
        sys.exit(f"✗ {spec['estilo']} es un estilo físico: use scripts/render_fisico.py")
    for a in avisos:
        print("AVISO   " + a)
    out = renderizar(spec, sys.argv[2])
    print(f"✓ {out}.png, {out}.svg y {out}.leyenda.txt")


if __name__ == "__main__":
    main()
