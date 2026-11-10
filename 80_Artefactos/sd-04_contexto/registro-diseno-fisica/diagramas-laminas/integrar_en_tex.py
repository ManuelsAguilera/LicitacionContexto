"""Reemplaza las figuras físicas del SD-04 por las láminas nuevas y renumera las figuras.
Uso (desde la raíz): python3 .../integrar_en_tex.py   — imprime la correspondencia antigua → nueva."""
import json, os, re, shutil, subprocess
RAIZ = os.getcwd()
AQUI = os.path.dirname(os.path.abspath(__file__))
TEX = "02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex"
FIG = "02_Propuesta/latex_final/figuras"
ADJ = "04_Adjuntos/diagramas"
# hash de la figura antigua → (clave nueva o None si se fusiona, título nuevo, clave destino si se fusiona)
PLAN = [
    ("f44f4f31ae2b", "A_topologia-general", "Arquitectura física: sitios, conexiones y regiones"),
    ("fb4f17cc7840", "D1_tienda-red-servidores", "Tienda tipo: red, servidores y equipos"),
    ("0c9d8da5748c", "D2_tienda-energia-espacio", "Tienda tipo: energía y espacio"),
    ("10c2ea3cb93b", "B1_red-chile-central", "Red y entrada de Azure Chile Central por frente, incluida la red de X-01"),
    ("d0650bf21604", None, "B1_red-chile-central"),
    ("ead70a0335fe", "E1_entrega-ambientes", "Canal de entrega y ambientes por frente"),
    ("c73b0fee0dfa", None, "E1_entrega-ambientes"),
    ("8766211b5707", "F4_puntos-falla", "Puntos de falla de los sitios y de la nube, con su contingencia"),
    ("35dda40b1bff", None, "F4_puntos-falla"),
    ("1688f39f837c", "B2_computo-chile-central", "Clústeres de AKS y máquinas de apoyo de Chile Central por frente"),
    ("6e5ec0282f43", "B3_datos-chile-central", "Bases PostgreSQL, mensajería, almacenamiento y respaldo de Chile Central por frente"),
    ("0dde5557a631", None, "B3_datos-chile-central"),
    ("69716b9c4e43", "B4_seguridad-operacion", "Identidad, seguridad, observabilidad y entrega de Chile Central por frente"),
    ("0b9e54f2ffe9", "D3_dc01-casa-matriz", "DC-01, casa matriz, con Retail y la filial emisora separados"),
    ("eb854151a942", "D4_centros-distribucion", "Centros de distribución CD-01 y CD-02"),
    ("56b9be1eff1b", "C1_brazil-red-entrada", "Brazil South: red y entrada de recuperación por frente"),
    ("9c0f119a62a5", "C3_conmutacion", "Conmutación a Brazil South: orden de arranque de las siete etapas"),
]
INSERTAR_TRAS = {"C1_brazil-red-entrada": ("C2_brazil-computo-datos", "Brazil South: cómputo y datos en espera por frente")}

s = open(TEX, encoding="utf-8").read()
BLOQUE = r"(?:\\clearpage\n)?\\begin\{center\}\n\s*\\includegraphics\[([^\]]*)\]\{figuras/recepcion-20261025/%s\.png\}\n\\end\{center\}\n\nFigura (4\.\d+): ([^\n]*?)\. Fuente: ([^\n]*)\n(?:\\clearpage\n)?"
fusion = {}   # número antiguo → clave destino
clave_num = {}  # clave → número antiguo de su bloque
for h, clave, titulo in PLAN:
    m = re.search(BLOQUE % h, s)
    assert m, h
    opts, num, _, fuente = m.groups()
    if clave is None:
        fusion[num] = titulo
        s = s[:m.start()] + s[m.end():]
        continue
    clave_num[clave] = num
    nuevo = f"\\begin{{center}}\n  \\includegraphics[{opts}]{{figuras/@@{clave}@@.png}}\n\\end{{center}}\n\nFigura {num}: {titulo}. Fuente: {fuente}\n"
    if clave in INSERTAR_TRAS:
        c2, t2 = INSERTAR_TRAS[clave]
        nuevo += f"\n\\begin{{center}}\n  \\includegraphics[{opts}]{{figuras/@@{c2}@@.png}}\n\\end{{center}}\n\nFigura 4.99: {t2}. Fuente: {fuente}\n"
        clave_num[c2] = "4.99"
    s = s[:m.start()] + nuevo + s[m.end():]
# renumerar por orden de aparición
orden = re.findall(r"^Figura (4\.\d+):", s, re.M)
assert len(orden) == len(set(orden)), orden
mapa = {old: f"4.{i+1}" for i, old in enumerate(orden)}
num_de_clave = {c: mapa[n] for c, n in clave_num.items()}
for old, dest in fusion.items():
    mapa[old] = num_de_clave[dest]
def sub(m):
    return m.group(1) + " " + re.sub(r"4\.\d+", lambda x: mapa.get(x.group(0), x.group(0)), m.group(2))
s = re.sub(r"(Figuras?) (4\.\d+(?:(?:, | y | a )4\.\d+)*)", sub, s)
s = s.replace(f"Figuras {num_de_clave['C1_brazil-red-entrada']} y {num_de_clave['C3_conmutacion']}",
              f"Figuras {num_de_clave['C1_brazil-red-entrada']} a {num_de_clave['C3_conmutacion']}")
# nombres de archivo definitivos y copias
for clave, n in num_de_clave.items():
    nn = n.split(".")[1]
    nombre = f"diag-04-{int(nn):02d}_{clave.split('_', 1)[1]}"
    s = s.replace(f"@@{clave}@@", nombre)
    src = os.path.join(AQUI, "salida", clave)
    shutil.copy(src + ".png", os.path.join(FIG, nombre + ".png"))
    for ext in (".png", ".drawio"):
        shutil.copy(src + ext, os.path.join(ADJ, nombre + ext))
    shutil.copy(os.path.join(AQUI, "especificaciones", clave + ".json"), os.path.join(ADJ, nombre + ".json"))
    subprocess.run(["drawio", "-x", "-f", "pdf", "-o", os.path.join(ADJ, nombre + ".pdf"), src + ".drawio", "--no-sandbox"],
                   capture_output=True, timeout=180)
    print(clave, "→ Figura", n, nombre)
open(TEX, "w", encoding="utf-8").write(s)
json.dump({"antigua_a_nueva": {k: v for k, v in mapa.items() if k != "4.99"}, "clave_a_figura": num_de_clave},
          open(os.path.join(AQUI, "correspondencia-figuras.json"), "w"), ensure_ascii=False, indent=1)
print({k: v for k, v in sorted(mapa.items(), key=lambda x: float(x[0]))})
