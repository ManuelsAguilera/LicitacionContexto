"""Extensiones de _drawio para las vistas físicas con frontera de alcance (FEP01, diap. 93).

Tres colores fijos: lo que provee el proponente, lo que es del Cliente y lo que es de terceros.
"""

import base64

from _drawio import FONT, TEXT, _esc

SCOPE = {
    "oss": ("#0078D4", "#EEF5FC", "Only Simple Solutions"),
    "cliente": ("#2E7D32", "#EEF7EF", "Cliente"),
    "tercero": ("#C55A11", "#FDF1E7", "Terceros"),
}


def czone(d, x, y, w, h, label, scope, dashed=False, fill=True, align="center", font=None, bold=True):
    """Recuadro coloreado según la frontera de alcance."""
    stroke, bg, _ = SCOPE[scope]
    fs = font or d.zone_font
    style = (f"rounded=1;arcSize=3;whiteSpace=wrap;html=1;verticalAlign=top;align={align};spacingTop=4;"
             f"spacingLeft=10;fontFamily={FONT};fontSize={fs};fontStyle={1 if bold else 0};fontColor={TEXT};"
             f"strokeColor={stroke};strokeWidth=2;fillColor={bg if fill else '#FFFFFF'};")
    if dashed:
        style += "dashed=1;dashPattern=8 4;"
    cid = d._id("z")
    d.cells.append(f'<mxCell id="{cid}" value="{_esc(label)}" style="{style}" vertex="1" parent="1">'
                   f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    d.rects[cid] = (x, y, w, h)
    return cid


def ring(d, x, y, w, h, label):
    """Anillo de red (zona de segmentación): borde gris punteado, sin relleno."""
    style = (f"rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;align=center;spacingTop=4;"
             f"fontFamily={FONT};fontSize={d.zone_font - 2};fontStyle=1;fontColor=#505050;"
             f"strokeColor=#8A8A8A;strokeWidth=1.5;dashed=1;dashPattern=4 3;fillColor=none;")
    cid = d._id("z")
    d.cells.append(f'<mxCell id="{cid}" value="{_esc(label)}" style="{style}" vertex="1" parent="1">'
                   f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    d.rects[cid] = (x, y, w, h)
    return cid


def legend(d, x, y, w, extra=()):
    """Leyenda obligatoria: colores de alcance y tipos de línea."""
    d.text(x, y, w, 34, "Leyenda", size=d.font + 2, bold=True, align="left")
    yy = y + 44
    for key in ("oss", "cliente", "tercero"):
        stroke, bg, txt = SCOPE[key]
        cid = d._id("z")
        d.cells.append(f'<mxCell id="{cid}" value="" style="rounded=1;html=1;strokeColor={stroke};strokeWidth=2;fillColor={bg};" '
                       f'vertex="1" parent="1"><mxGeometry x="{x}" y="{yy}" width="46" height="30" as="geometry"/></mxCell>')
        d.text(x + 58, yy - 6, w - 58, 44, txt, size=d.font - 2, align="left")
        yy += 44
    for (dash, color, width, txt) in extra:
        st = f"endArrow=block;endFill=1;html=1;strokeColor={color};strokeWidth={width};"
        if dash == "dashed":
            st += "dashed=1;dashPattern=6 4;"
        elif dash == "dotted":
            st += "dashed=1;dashPattern=1 3;"
        cid = d._id("e")
        d.cells.append(f'<mxCell id="{cid}" style="{st}" edge="1" parent="1"><mxGeometry relative="1" as="geometry">'
                       f'<mxPoint x="{x}" y="{yy + 15}" as="sourcePoint"/><mxPoint x="{x + 46}" y="{yy + 15}" as="targetPoint"/>'
                       f'</mxGeometry></mxCell>')
        d.text(x + 58, yy - 6, w - 58, 44, txt, size=d.font - 2, align="left")
        yy += 44
    return yy


# ---------- vistas lógicas: cajas sin marcas, con nombres de negocio ----------
LOGIC = {
    "oss": ("#0078D4", "#EAF3FC"),       # lo que construye el proponente
    "cliente": ("#2E7D32", "#EAF6EC"),   # sistemas y personas del Cliente
    "tercero": ("#C55A11", "#FDEFE3"),   # terceros externos
    "neutro": ("#6B7A89", "#F4F6F8"),    # transversal
}


def box(d, x, y, w, h, title, lines=(), scope="oss", dashed=False, tsize=None, lsize=None, valign="top", icon=None, icon_pos="top"):
    """Caja con título en negrita y líneas de detalle. Devuelve el id del rectángulo (para aristas)."""
    stroke, bg = LOGIC[scope]
    ts = tsize or d.zone_font
    ls = lsize or d.font
    style = (f"rounded=1;arcSize=6;whiteSpace=wrap;html=1;strokeColor={stroke};strokeWidth=2;fillColor={bg};"
             + ("dashed=1;dashPattern=8 4;" if dashed else ""))
    cid = d._id("b")
    d.cells.append(f'<mxCell id="{cid}" value="" style="{style}" vertex="1" parent="1">'
                   f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    d.rects[cid] = (x, y, w, h)
    off = 0
    if icon and icon_pos == "top":
        pic(d, x + w / 2 - 26, y + 8, icon, 52, stroke)
        off = 60
    elif icon:
        pic(d, x + 12, y + h / 2 - 22, icon, 44, stroke)
    th = ts * 1.5 * (title.count("\n") + 1) + 14
    d.text(x + 8, y + 6 + off, w - 16, th, title, size=ts, bold=True, align="center")
    if lines:
        d.text(x + 10, y + 6 + off + th, w - 20, h - th - off - 12, "\n".join(lines), size=ls, align="center")
    return cid


def container(d, x, y, w, h, title, scope="oss"):
    """Contenedor de agrupación (frente o capa): borde y título, sin relleno."""
    stroke, _ = LOGIC[scope]
    style = (f"rounded=1;arcSize=3;whiteSpace=wrap;html=1;verticalAlign=top;align=left;spacingTop=4;spacingLeft=12;"
             f"fontFamily={FONT};fontSize={d.zone_font};fontStyle=1;fontColor={TEXT};strokeColor={stroke};strokeWidth=2.5;"
             f"fillColor=none;")
    cid = d._id("k")
    d.cells.append(f'<mxCell id="{cid}" value="{_esc(title)}" style="{style}" vertex="1" parent="1">'
                   f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    d.rects[cid] = (x, y, w, h)
    return cid


def header(d, x, y, w, n, title, icon=None):
    """Encabezado de columna de capa, numerado como en RT-02.01."""
    if icon:
        pic(d, x + w / 2 - 28, y - 62, icon, 56)
    d.text(x, y, w, 70, f"{n}  {title}" if n else title, size=d.zone_font, bold=True, align="center", color="#1F3A5F")
    d.cells.append(f'<mxCell id="{d._id("l")}" style="endArrow=none;html=1;strokeColor=#1F3A5F;strokeWidth=3;" edge="1" parent="1">'
                   f'<mxGeometry relative="1" as="geometry"><mxPoint x="{x}" y="{y + 72}" as="sourcePoint"/>'
                   f'<mxPoint x="{x + w}" y="{y + 72}" as="targetPoint"/></mxGeometry></mxCell>')


# ---------- íconos genéricos para las vistas lógicas (sin marcas ni productos) ----------
_ICONS = {
    "person": '<circle cx="24" cy="15" r="7"/><path d="M9 42c0-9 7-15 15-15s15 6 15 15"/>',
    "users": '<circle cx="17" cy="16" r="6"/><path d="M5 40c0-7 5-12 12-12s12 5 12 12"/><circle cx="34" cy="18" r="5"/><path d="M33 29c6 0 10 4 10 10"/>',
    "monitor": '<rect x="6" y="8" width="36" height="24" rx="2"/><path d="M18 40h12M24 32v8"/>',
    "mobile": '<rect x="14" y="5" width="20" height="38" rx="4"/><path d="M21 38h6"/>',
    "globe": '<circle cx="24" cy="24" r="17"/><path d="M7 24h34M24 7c-8 9-8 25 0 34M24 7c8 9 8 25 0 34"/>',
    "gateway": '<path d="M8 42V20a16 16 0 0 1 32 0v22M4 42h40"/><path d="M16 32h16M27 26l6 6-6 6"/>',
    "services": '<rect x="6" y="6" width="15" height="15" rx="2"/><rect x="27" y="6" width="15" height="15" rx="2"/><rect x="6" y="27" width="15" height="15" rx="2"/><rect x="27" y="27" width="15" height="15" rx="2"/>',
    "database": '<ellipse cx="24" cy="12" rx="15" ry="6"/><path d="M9 12v24c0 3 7 6 15 6s15-3 15-6V12M9 24c0 3 7 6 15 6s15-3 15-6"/>',
    "exchange": '<path d="M8 16h30M30 8l8 8-8 8M40 32H10M18 24l-8 8 8 8"/>',
    "shield": '<path d="M24 5l15 6v11c0 11-7 18-15 21C16 40 9 33 9 22V11z"/><path d="M17 24l5 5 9-10"/>',
    "pulse": '<circle cx="24" cy="24" r="18"/><path d="M8 26h9l4-10 6 18 4-8h9"/>',
    "cart": '<path d="M5 8h7l5 22h20l4-16H14"/><circle cx="19" cy="38" r="3"/><circle cx="34" cy="38" r="3"/>',
    "package": '<path d="M24 5l17 8v20l-17 10L7 33V13z"/><path d="M7 13l17 8 17-8M24 21v22"/>',
    "card": '<rect x="5" y="11" width="38" height="26" rx="3"/><path d="M5 19h38M12 30h10"/>',
    "building": '<rect x="9" y="6" width="22" height="36"/><path d="M31 20h8v22H31M15 14h4M15 22h4M15 30h4M15 38h4"/>',
    "server": '<rect x="7" y="8" width="34" height="12" rx="2"/><rect x="26" y="28" width="15" height="12" rx="2" opacity="0"/><rect x="7" y="26" width="34" height="12" rx="2"/><path d="M13 14h2M13 32h2"/>',
    "truck": '<rect x="4" y="14" width="26" height="20"/><path d="M30 20h9l5 7v7H30"/><circle cx="14" cy="37" r="4"/><circle cx="37" cy="37" r="4"/>',
}


def pic(d, x, y, name, size=52, color="#1F3A5F"):
    """Ícono genérico de línea, incrustado como imagen vectorial."""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48" fill="none" stroke="{color}" '
           f'stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{_ICONS[name]}</svg>')
    b64 = base64.b64encode(svg.encode()).decode()
    cid = d._id("i")
    d.cells.append(f'<mxCell id="{cid}" value="" style="shape=image;aspect=fixed;image=data:image/svg+xml,{b64};" vertex="1" parent="1">'
                   f'<mxGeometry x="{x}" y="{y}" width="{size}" height="{size}" as="geometry"/></mxCell>')
    return cid
