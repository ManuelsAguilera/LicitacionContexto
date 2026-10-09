"""Genera la vista física provisional de plataformas y red de Ancoa.

Las ubicaciones se fundamentan en
80_Artefactos/sd-04_contexto/supuestos_plataformas_y_conexiones.md.
La figura no representa el inventario técnico de las 14 interfaces existentes.
"""

from html import escape
from pathlib import Path

HERE = Path(__file__).parent
W, H = 2400, 1430
parts = []


def add(value):
    parts.append(value)


def rect(x, y, width, height, css, radius=16):
    add(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" class="{css}"/>')


def line(path, css="wire"):
    add(f'<path d="{path}" class="{css}"/>')


def label(x, y, value, css="name", anchor="start"):
    add(f'<text x="{x}" y="{y}" class="{css}" text-anchor="{anchor}">{escape(value)}</text>')


def icon(x, y, name, size=50):
    add(f'<use href="#{name}" x="{x}" y="{y}" width="{size}" height="{size}" class="icon"/>')


def card(x, y, width, height, name, symbol, css="site"):
    rect(x, y, width, height, css)
    icon(x + 20, y + (height - 50) / 2, symbol)
    label(x + 86, y + height / 2 + 11, name)


add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">')
add('<title id="title">Ancoa: red y plataformas, modelo físico provisional</title>')
add('<desc id="desc">Plataformas agrupadas por sitio supuesto, con enlaces de acceso, conexión al centro de datos y enlace propuesto a la sala de respaldo. El emplazamiento exacto y los contratos se validan en el proyecto.</desc>')
add('''<defs>
<marker id="arr" markerWidth="11" markerHeight="11" refX="9" refY="5.5" orient="auto"><path d="M0 0L11 5.5L0 11Z" fill="#17806f"/></marker>
<symbol id="shop" viewBox="0 0 64 64"><path d="M9 26h46l-5-13H14L9 26Zm4 0v27h38V26M26 53V35h12v18M9 26c2 8 9 9 12 2 4 7 10 7 13 0 4 7 10 7 13 0 4 7 9 8 13 0"/></symbol>
<symbol id="warehouse" viewBox="0 0 64 64"><path d="M6 26 32 11l26 15v30H6V26Zm8 30V34h36v22M22 34v22m10-22v22m10-22v22"/></symbol>
<symbol id="sheet" viewBox="0 0 64 64"><path d="M14 8h26l10 10v38H14V8Zm26 0v12h10M22 29h20M22 37h20M22 45h14"/></symbol>
<symbol id="hub" viewBox="0 0 64 64"><circle cx="32" cy="32" r="12"/><circle cx="7" cy="10" r="5"/><circle cx="57" cy="10" r="5"/><circle cx="7" cy="54" r="5"/><circle cx="57" cy="54" r="5"/><path d="M23 23 11 13m30 10 12-10M23 41 11 51m30-10 12 10"/></symbol>
<symbol id="rack" viewBox="0 0 64 64"><rect x="12" y="8" width="40" height="14" rx="2"/><rect x="12" y="25" width="40" height="14" rx="2"/><rect x="12" y="42" width="40" height="14" rx="2"/><circle cx="19" cy="15" r="1"/><circle cx="19" cy="32" r="1"/><circle cx="19" cy="49" r="1"/></symbol>
<symbol id="pos" viewBox="0 0 64 64"><rect x="10" y="10" width="44" height="31" rx="3"/><path d="M20 49h24M32 41v8M17 17h30v17H17z"/></symbol>
<symbol id="cart" viewBox="0 0 64 64"><path d="M7 11h8l7 31h29l6-23H18M23 33h30"/><circle cx="28" cy="51" r="3"/><circle cx="47" cy="51" r="3"/></symbol>
<symbol id="credit" viewBox="0 0 64 64"><rect x="6" y="14" width="52" height="36" rx="5"/><path d="M7 25h50M16 39h13"/></symbol>
<symbol id="doc" viewBox="0 0 64 64"><path d="M15 7h26l9 9v41H15V7Zm26 0v11h9M22 29h20M22 38h20M22 47h12"/></symbol>
<symbol id="market" viewBox="0 0 64 64"><path d="M9 24h46l-4-12H13L9 24Zm5 0v29h36V24M23 53V36h18v17M10 24c4 8 9 8 13 0 4 8 10 8 14 0 4 8 9 8 13 0"/></symbol>
<symbol id="star" viewBox="0 0 64 64"><path d="m32 7 7 16 18 2-13 12 4 18-16-9-16 9 4-18L7 25l18-2 7-16Z"/></symbol>
<style>
text{font-family:'DejaVu Sans',Arial,sans-serif;fill:#18334b}.title{font-size:46px;font-weight:700}.subtitle{font-size:32px;fill:#516578}.section{font-size:33px;font-weight:700}.name{font-size:32px;font-weight:650}.muted{font-size:32px;fill:#516578}.domain{font-size:32px;font-weight:700;fill:#39586d}
.white{fill:white;stroke:none}.site{fill:#eef5fb;stroke:#76a4c5;stroke-width:2.4}.app{fill:#fff;stroke:#9db8c7;stroke-width:2.4}.retail{fill:#eff8f5;stroke:#64a697;stroke-width:2.4}.finance{fill:#f4effa;stroke:#aa91c0;stroke-width:2.4}.external{fill:#f5f7f9;stroke:#aabac5;stroke-width:2.4}.datacenter{fill:#f8fafb;stroke:#a7bac7;stroke-width:2.5}.backup{fill:#fff4e7;stroke:#c99c59;stroke-width:2.5}.network{fill:#e8f1f8;stroke:#77a3c4;stroke-width:2.5}
.icon{fill:none;stroke:#326781;stroke-width:3.3;stroke-linecap:round;stroke-linejoin:round}.wire{fill:none;stroke:#417a9d;stroke-width:4.2;stroke-linejoin:round}.wire2{fill:none;stroke:#417a9d;stroke-width:4.2;stroke-linejoin:round}.business{fill:none;stroke:#17806f;stroke-width:4;marker-end:url(#arr)}.provisional{fill:none;stroke:#bd873a;stroke-width:4;stroke-dasharray:13 8}.separator{fill:none;stroke:#d2dce4;stroke-width:2.2}
</style></defs>''')
rect(0, 0, W, H, "white", 0)
label(60, 65, "Red y plataformas · modelo de referencia", "title")
label(60, 110, "Ubicaciones y conexiones provisionales para el levantamiento de Etapa 1", "subtitle")
label(60, 185, "TIENDAS Y CENTROS DE DISTRIBUCIÓN", "section")
label(1990, 185, "EXTERNOS", "section")

# Sitios y componentes locales. Los POS se repiten por agrupación, no por versión.
for x, name in ((60, "Mall ×8"), (425, "Mall ×6"), (790, "Calle ×8")):
    card(x, 210, 340, 94, name, "shop")
    card(x + 18, 326, 304, 72, "POS", "pos", "retail")
card(1125, 210, 420, 94, "CD principal", "warehouse")
card(1157, 326, 356, 72, "WMS", "warehouse", "retail")
card(1570, 210, 390, 94, "CD Concepción", "warehouse")
card(1588, 326, 354, 72, "Planillas", "sheet", "external")
for y, name, symbol in ((210, "Comercio web", "cart"), (325, "Marketplace", "market"), (440, "Fidelización", "star")):
    card(1985, y, 355, 84, name, symbol, "external")
# Intercambio funcional supuesto entre canal propio y marketplace conservado.
line("M2060 294V316", "business")
line("M2255 325V303", "business")

# Conectividad de cada grupo hacia el centro. Dos enlaces solo donde el Caso los acredita.
for x in (230, 595, 960, 1335, 1765):
    line(f"M{x} 398V582")
for x in (223, 1328):
    line(f"M{x} 398V582", "wire2")
for y in (252, 367, 482):
    line(f"M2340 {y}H2365")
line("M2365 252V622")
rect(60, 585, 2310, 86, "network")
icon(92, 603, "hub", 52)
label(170, 641, "Red intersitios / Internet", "name")
label(920, 641, "Enlaces y controles según cada contraparte", "muted")
line("M895 671V775")

# Centro de datos de casa matriz: tres plataformas con responsabilidades propias.
label(60, 745, "CASA MATRIZ", "section")
rect(60, 775, 1660, 424, "datacenter")
icon(92, 802, "rack", 58)
label(170, 842, "Centro de datos principal", "section")
label(120, 922, "RETAIL", "domain")
label(672, 922, "FILIAL EMISORA", "domain")
label(1245, 922, "GESTIÓN", "domain")
card(105, 950, 465, 100, "Sistema central", "rack", "retail")
card(625, 950, 465, 100, "Crédito", "credit", "finance")
card(1145, 950, 465, 100, "ERP / DTE", "doc", "app")
line("M596 900V1110", "separator")
line("M1118 900V1110", "separator")
line("M1090 1000H1136", "business")
label(1114, 1078, "lote", "muted", "middle")
line("M338 1050V1132 M858 1050V1132 M1378 1050V1132 M338 1132H1378")
label(120, 1175, "Red local compartida · separación lógica parcial actual", "muted")

# La sala secundaria es un sitio distinto de la misma comuna, enlazado con el DC primario.
rect(1790, 820, 550, 180, "backup")
icon(1822, 866, "rack", 56)
label(1900, 908, "Sala de respaldo", "name")
label(1900, 952, "Misma comuna", "muted")
line("M1720 890H1785", "provisional")

# Leyenda breve. La matriz de contexto contiene la modalidad de cada flujo.
line("M60 1294H155")
label(175, 1304, "enlace de sitio", "muted")
line("M575 1288H670")
line("M575 1300H670", "wire2")
label(690, 1304, "respaldo acreditado", "muted")
line("M1210 1294H1305", "provisional")
label(1325, 1304, "enlace de respaldo propuesto", "muted")
label(60, 1380, "Ubicaciones y modos de integración: supuestos_plataformas_y_conexiones.md", "muted")
add("</svg>")

(HERE / "diag-04-00_red-actual-plataformas.svg").write_text("\n".join(parts), encoding="utf-8")
