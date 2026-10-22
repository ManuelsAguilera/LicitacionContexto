#!/usr/bin/env python3
"""Renderiza una especificación de estilo físico (F1–F5) como archivo draw.io con íconos oficiales de Azure.

Uso:  python3 scripts/render_fisico.py ejemplos/mi_diagrama.json salida/mi_diagrama
Genera salida/mi_diagrama.drawio y salida/mi_diagrama.leyenda.txt. Abrir el .drawio en draw.io
(app o diagrams.net) y exportar a PNG/PDF. La especificación se valida antes de dibujar.

Disposición: cada grupo ordena sus hijos (subgrupos primero, luego nodos, en el orden del JSON)
en «fila», «columna» o «rejilla» (con «columnas»). La raíz usa la disposición del estilo.
"""
import html
import pathlib
import sys

from _comun import CATALOGO, cargar_spec, leyenda
from validar import validar

CELDA_W, CELDA_H, ICONO = 120, 92, 44
PAD, CABECERA, SEP = 14, 30, 36
TRAZO_DRAWIO = {"solid": "", "dashed": "dashed=1;", "dotted": "dashed=1;dashPattern=1 3;", "dashdot": "dashed=1;dashPattern=8 3 1 3;", "longdash": "dashed=1;dashPattern=14 5;"}


class Caja:
    def __init__(self, kind, ref, hijos=None):
        self.kind, self.ref, self.hijos = kind, ref, hijos or []
        self.w = self.h = self.x = self.y = 0


def construir_arbol(spec, disp_raiz):
    grupos = spec.get("grupos", [])
    nodos = spec.get("nodos", [])

    def hijos_de(gid):
        hs = [construir(g) for g in grupos if g.get("padre") == gid]
        hs += [Caja("nodo", n) for n in nodos if n.get("grupo") == gid]
        return hs

    def construir(g):
        return Caja("grupo", g, hijos_de(g["id"]))

    raiz = Caja("raiz", {"disposicion": disp_raiz}, [construir(g) for g in grupos if not g.get("padre")]
                + [Caja("nodo", n) for n in nodos if not n.get("grupo")])
    return raiz


def medir(c):
    if c.kind == "nodo":
        c.w, c.h = CELDA_W, CELDA_H
        return
    for h in c.hijos:
        medir(h)
    disp = c.ref.get("disposicion") or ("fila" if all(h.kind == "nodo" for h in c.hijos) and len(c.hijos) <= 4
                                        else "rejilla" if all(h.kind == "nodo" for h in c.hijos) else "columna")
    c.disp = disp
    cab = 0 if c.kind == "raiz" else CABECERA
    pad = 0 if c.kind == "raiz" else PAD
    if not c.hijos:
        c.w, c.h = CELDA_W + 2 * pad, CELDA_H + cab
        return
    if disp == "fila":
        c.w = sum(h.w for h in c.hijos) + SEP * (len(c.hijos) - 1) + 2 * pad
        c.h = max(h.h for h in c.hijos) + cab + 2 * pad
    elif disp == "columna":
        c.w = max(h.w for h in c.hijos) + 2 * pad
        c.h = sum(h.h for h in c.hijos) + SEP * (len(c.hijos) - 1) + cab + 2 * pad
    else:
        cols = int(c.ref.get("columnas") or 3)
        filas = [c.hijos[i:i + cols] for i in range(0, len(c.hijos), cols)]
        cw = max(h.w for h in c.hijos)
        c.filas, c.cw = filas, cw
        c.w = cw * min(cols, len(c.hijos)) + SEP * (min(cols, len(c.hijos)) - 1) + 2 * pad
        c.h = sum(max(h.h for h in f) for f in filas) + SEP * (len(filas) - 1) + cab + 2 * pad


def ubicar(c, x, y):
    c.x, c.y = x, y
    if c.kind == "nodo":
        return
    cab = 0 if c.kind == "raiz" else CABECERA
    pad = 0 if c.kind == "raiz" else PAD
    cx, cy = x + pad, y + cab + pad
    if c.disp == "fila":
        alto = c.h - cab - 2 * pad if c.kind != "raiz" else max((h.h for h in c.hijos), default=0)
        for h in c.hijos:
            # estirar subgrupos al alto de la fila para alinear como en las figuras
            if h.kind == "grupo":
                h.h = alto
            ubicar(h, cx, cy)
            cx += h.w + SEP
    elif c.disp == "columna":
        ancho = c.w - 2 * pad if c.kind != "raiz" else max((h.w for h in c.hijos), default=0)
        for h in c.hijos:
            if h.kind == "grupo":
                h.w = ancho
            ubicar(h, cx, cy)
            cy += h.h + SEP
    else:
        for f in c.filas:
            fx = cx
            for h in f:
                ubicar(h, fx, cy)
                fx += c.cw + SEP
            cy += max(h.h for h in f) + SEP


def recorrer(c):
    yield c
    for h in c.hijos:
        yield from recorrer(h)


def esc(t):
    return html.escape(t, quote=True).replace("\n", "&lt;br&gt;")


def renderizar(spec, salida):
    estilo = CATALOGO["estilos"][spec["estilo"]]
    raiz = construir_arbol(spec, estilo["disposicion_raiz"])
    medir(raiz)
    ubicar(raiz, 20, 20)

    celdas = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']
    pos = {}
    for c in recorrer(raiz):
        if c.kind == "grupo":
            g = c.ref
            d = CATALOGO["grupos_fisicos"][g["tipo"]]
            st = (f"rounded={1 if d['redondeado'] else 0};arcSize=4;whiteSpace=wrap;html=1;fillColor={d['relleno']};"
                  f"strokeColor={d['borde']};{TRAZO_DRAWIO[d['trazo']]}verticalAlign=top;align=left;spacingLeft=8;"
                  f"fontStyle={1 if d['cabecera_negrita'] else 0};fontSize=12;fontColor=#1A1A1A;container=0;")
            celdas.append(f'<mxCell id="g_{g["id"]}" value="{esc(g.get("etiqueta", ""))}" style="{st}" vertex="1" parent="1">'
                          f'<mxGeometry x="{c.x}" y="{c.y}" width="{c.w}" height="{c.h}" as="geometry"/></mxCell>')
    for c in recorrer(raiz):
        if c.kind != "nodo":
            continue
        n = c.ref
        estado = n.get("estado", "objetivo")
        etiqueta = n["etiqueta"] + CATALOGO["estados_nodo"][estado]["sufijo"]
        if estado == "propuesto" and "propuesto" not in etiqueta:
            etiqueta += "\n(propuesto)"
        if estado == "por_acreditar" and "acreditar" not in etiqueta:
            etiqueta += "\n(por acreditar)"
        if n.get("codigo") and n["codigo"] not in etiqueta:
            etiqueta = n["codigo"] + "\n" + etiqueta
        base = CATALOGO["iconos_fisicos"][n["icono"]]
        st = (base + ";verticalLabelPosition=bottom;verticalAlign=top;labelPosition=center;align=center;"
              "fontSize=11;fontColor=#1A1A1A;labelBackgroundColor=#FFFFFF;")
        if estado in ("propuesto", "condicionado", "por_acreditar"):
            st += "opacity=70;"
        ix = c.x + (CELDA_W - ICONO) / 2
        iy = c.y + 6
        pos[n["id"]] = (ix, iy)
        celdas.append(f'<mxCell id="n_{n["id"]}" value="{esc(etiqueta)}" style="{st}" vertex="1" parent="1">'
                      f'<mxGeometry x="{ix}" y="{iy}" width="{ICONO}" height="{ICONO}" as="geometry"/></mxCell>')
        if n.get("insignia") is not None:
            b = CATALOGO["insignia"]
            celdas.append(f'<mxCell id="b_{n["id"]}" value="{n["insignia"]}" style="ellipse;html=1;fillColor={b["relleno"]};'
                          f'strokeColor=none;fontColor={b["texto"]};fontStyle=1;fontSize=11;" vertex="1" parent="1">'
                          f'<mxGeometry x="{ix + ICONO + 4}" y="{iy - 8}" width="{b["diametro"]}" height="{b["diametro"]}" as="geometry"/></mxCell>')

    ids_grupo = {g["id"] for g in spec.get("grupos", [])}
    ref = lambda x: ("g_" if x in ids_grupo else "n_") + x
    aristas = []
    for i, a in enumerate(spec.get("enlaces", [])):
        s = CATALOGO["semanticas_enlace"][a["semantica"]]
        st = (f"edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;endSize=5;"
              f"strokeColor={s['color']};strokeWidth={s['grosor']};{TRAZO_DRAWIO[s['estilo']]}"
              "fontSize=11;fontColor=#1A1A1A;labelBackgroundColor=#FFFFFF;")
        aristas.append(f'<mxCell id="e{i}" value="{esc(a.get("etiqueta", ""))}" style="{st}" edge="1" parent="1" '
                       f'source="{ref(a["de"])}" target="{ref(a["a"])}"><mxGeometry relative="1" as="geometry"/></mxCell>')
    # las líneas van debajo de íconos y rótulos (se insertan justo después de los grupos)
    n_grupos = 2 + len(ids_grupo)
    celdas[n_grupos:n_grupos] = aristas

    # Leyenda dentro de la figura (C4: toda notación se explica), solo con lo usado
    entradas = leyenda(spec)
    ly = raiz.y + raiz.h + 24
    lx = raiz.x
    alto_leyenda = 30 + 22 * max(1, len(entradas))
    ancho_leyenda = 520
    celdas.append(f'<mxCell id="ley" value="Leyenda" style="rounded=0;html=1;fillColor=#FFFFFF;strokeColor=#B0B0B0;'
                  f'verticalAlign=top;align=left;spacingLeft=8;fontStyle=1;fontSize=11;" vertex="1" parent="1">'
                  f'<mxGeometry x="{lx}" y="{ly}" width="{ancho_leyenda}" height="{alto_leyenda}" as="geometry"/></mxCell>')
    sem = CATALOGO["semanticas_enlace"]
    for k, (clave, texto) in enumerate(entradas):
        yy = ly + 30 + 22 * k
        tipo, nombre = clave.split(":", 1)
        if tipo == "sem":
            s = sem[nombre]
            st = (f"html=1;endArrow=block;endFill=1;endSize=5;strokeColor={s['color']};strokeWidth={s['grosor']};"
                  f"{TRAZO_DRAWIO[s['estilo']]}")
            celdas.append(f'<mxCell id="ley_l{k}" value="" style="{st}" edge="1" parent="1"><mxGeometry relative="1" as="geometry">'
                          f'<mxPoint x="{lx + 10}" y="{yy + 8}" as="sourcePoint"/><mxPoint x="{lx + 60}" y="{yy + 8}" as="targetPoint"/>'
                          '</mxGeometry></mxCell>')
        texto_sin_prefijo = texto.split(": ", 1)[1] if tipo == "sem" else texto
        celdas.append(f'<mxCell id="ley_t{k}" value="{esc(texto_sin_prefijo)}" style="text;html=1;align=left;verticalAlign=middle;'
                      f'fontSize=11;" vertex="1" parent="1"><mxGeometry x="{lx + 70}" y="{yy}" width="{ancho_leyenda - 80}" height="16" as="geometry"/></mxCell>')

    xml = ('<mxfile host="diagramas-ancoa" type="device">'
           f'<diagram id="d1" name="Figura {esc(str(spec.get("figura", "4.N")))}">'
           f'<mxGraphModel dx="1200" dy="800" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" '
           f'page="0" pageScale="1" math="0" shadow="0"><root>{"".join(celdas)}</root></mxGraphModel></diagram></mxfile>')
    salida = pathlib.Path(salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    (salida.parent / (salida.name + ".drawio")).write_text(xml, encoding="utf-8")
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
    if CATALOGO["estilos"][spec["estilo"]]["familia"] != "fisica":
        sys.exit(f"✗ {spec['estilo']} es un estilo lógico: use scripts/render_logico.py")
    for a in avisos:
        print("AVISO   " + a)
    out = renderizar(spec, sys.argv[2])
    print(f"✓ {out}.drawio y {out}.leyenda.txt")


if __name__ == "__main__":
    main()
