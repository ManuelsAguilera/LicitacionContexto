#!/usr/bin/env python3
"""Genera diag-08-01_rbs y diag-08-02_matriz-exposicion (SVG, y PDF/PNG con Inkscape si existe).
Lee la Tabla 1 de 80_Artefactos/sd-08_contexto/calificacion.md. Uso: python diag-08-00_generar.py"""
import re, shutil, subprocess, sys
from pathlib import Path
from xml.sax.saxutils import escape as esc

AQUI = Path(__file__).resolve().parent
FUENTE = AQUI.parents[1] / "80_Artefactos/sd-08_contexto/calificacion.md"
FONT = "Arial, Helvetica, sans-serif"
ZONAS = ["Crítica", "Alta", "Media", "Baja"]
# relleno, trazo, texto; luminosidad distinta (oscuro a claro) para escala de grises
COL = {"Crítica": ("#7a1f1f", "#4a0f0f", "#ffffff"), "Alta": ("#d9822b", "#8a4f10", "#000000"),
       "Media": ("#f2d98a", "#9a8440", "#000000"), "Baja": ("#e8eee8", "#8a9a8a", "#000000")}
NIV_P = ["Muy baja", "Baja", "Media", "Alta", "Muy alta"]
NIV_I = ["Muy bajo", "Bajo", "Medio", "Alto", "Muy alto"]
RAMAS = [("TEC", "Técnicos"), ("ORG", "Organizacionales"), ("PRO", "De proyecto"),
         ("SEG", "De seguridad"), ("OPE", "De operación")]
ESPERADO_RAMA = {"TEC": 8, "ORG": 5, "PRO": 16, "SEG": 3, "OPE": 5}
ESPERADO_ZONA = {"Crítica": 3, "Alta": 11, "Media": 21, "Baja": 2}

def leer():
    txt = FUENTE.read_text(encoding="utf-8").split("## Tabla 2")[0]
    out = []
    for l in txt.splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if re.fullmatch(r"R-\d\d", c[0]):
            out.append(dict(id=c[0], rbs=c[1], p=int(c[3]), i=int(c[5]), zona=c[9]))
    return out

def zona(p, i):
    v = [0.05, .20, .40, .60, .85][p-1] * [0.05, .10, .20, .40, .80][i-1]
    v = round(v, 4)
    return "Crítica" if v >= .40 else "Alta" if v >= .20 else "Media" if v >= .08 else "Baja"

def t(x, y, s, size=12, anchor="middle", weight="normal", fill="#000"):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" fill="{fill}">{esc(s)}</text>')

def chip(x, y, w, h, rid, z):
    f, s, tx = COL[z]
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{f}" stroke="{s}"/>' +
            t(x+w/2, y+h/2+4, rid, 11, fill=tx, weight="bold"))

def leyenda(x, y):
    o = []
    for k, z in enumerate(ZONAS):
        f, s, _ = COL[z]
        o.append(f'<rect x="{x+k*120}" y="{y}" width="18" height="14" fill="{f}" stroke="{s}"/>')
        o.append(t(x+k*120+24, y+12, z, 12, "start"))
    return o

def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect width="{w}" height="{h}" fill="#fff"/>' + "".join(body) + "</svg>")

def rbs(R):
    W, cols, cw, ch, gap = 940, 8, 60, 24, 6
    xs = 250
    o = []
    y = 70
    root = (20, 0, 150, 50)
    filas = []
    for cod, nom in RAMAS:
        ids = [r for r in R if r["rbs"] == cod]
        n = (len(ids) + cols - 1) // cols
        hh = max(60, n * (ch+gap) + 14)
        filas.append((cod, nom, ids, y, hh)); y += hh + 14
    H = y + 50
    cy = (filas[0][3] + filas[-1][3] + filas[-1][4]) / 2
    o.append(f'<rect x="20" y="{cy-30}" width="150" height="60" rx="6" fill="#1f3a5f" stroke="#10243d"/>')
    o.append(t(95, cy-3, "Riesgos del", 13, fill="#fff", weight="bold"))
    o.append(t(95, cy+14, "proyecto (37)", 13, fill="#fff", weight="bold"))
    o.append(t(W/2, 30, "Estructura de desglose de riesgos (RBS) del proyecto", 16, weight="bold"))
    for cod, nom, ids, y0, hh in filas:
        my = y0 + hh/2
        o.append(f'<path d="M170 {cy} H190 V{my} H205" fill="none" stroke="#555" stroke-width="1.5"/>')
        o.append(f'<rect x="205" y="{my-26}" width="150" height="52" rx="6" fill="#dfe7f2" stroke="#1f3a5f"/>')
        o.append(t(280, my-4, nom, 13, weight="bold"))
        o.append(t(280, my+14, f"{cod} · {len(ids)} riesgos", 12))
        o.append(f'<path d="M355 {my} H375" stroke="#555" stroke-width="1.5"/>')
        o.append(f'<rect x="375" y="{y0}" width="{cols*(cw+gap)+8}" height="{hh}" rx="6" fill="#fafafa" stroke="#bbb"/>')
        for k, r in enumerate(ids):
            o.append(chip(383 + (k % cols)*(cw+gap), y0 + 8 + (k//cols)*(ch+gap), cw, ch, r["id"], r["zona"]))
    o += leyenda(375, H-30)
    o.append(t(20, H-18, "Color de cada ID: zona de exposición.", 11, "start"))
    return svg(W, H, o), H

def matriz(R):
    cx0, cy0, cw, chh = 150, 70, 140, 96
    W, H = cx0 + 5*cw + 30, cy0 + 5*chh + 120
    o = [t(W/2, 28, "Matriz de exposición P × I de los 37 riesgos", 16, weight="bold")]
    for pi in range(5, 0, -1):
        for ii in range(1, 6):
            x, y = cx0 + (ii-1)*cw, cy0 + (5-pi)*chh
            z = zona(pi, ii); f, s, tx = COL[z]
            o.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{chh}" fill="{f}" stroke="#fff" stroke-width="2"/>')
            o.append(t(x+cw-5, y+13, z, 9, "end", fill=tx))
            ids = [r["id"] for r in R if r["p"] == pi and r["i"] == ii]
            per = 4
            for k in range(0, len(ids), per):
                o.append(t(x+cw/2, y+38+(k//per)*16, " ".join(ids[k:k+per]), 11, fill=tx, weight="bold"))
    for pi in range(1, 6):
        o.append(t(cx0-8, cy0+(5-pi)*chh+chh/2+4, NIV_P[pi-1], 12, "end"))
    for ii in range(1, 6):
        o.append(t(cx0+(ii-1)*cw+cw/2, cy0+5*chh+18, NIV_I[ii-1], 12))
    o.append(f'<text transform="translate(22,{cy0+2.5*chh}) rotate(-90)" font-family="{FONT}" font-size="13" text-anchor="middle" font-weight="bold">Probabilidad (P)</text>')
    o.append(t(cx0+2.5*cw, cy0+5*chh+40, "Impacto (I)", 13, weight="bold"))
    o += leyenda(cx0, cy0+5*chh+62)
    o.append(t(cx0, cy0+5*chh+100, "Zona según P × I: crítica ≥ 0,40; alta ≥ 0,20; media ≥ 0,08; baja < 0,08.", 11, "start"))
    return svg(W, H, o), H

def main():
    R = leer()
    assert len(R) == 37, len(R)
    for r in R:
        assert zona(r["p"], r["i"]) == r["zona"], r
    for c, n in ESPERADO_RAMA.items():
        assert sum(r["rbs"] == c for r in R) == n, c
    for z, n in ESPERADO_ZONA.items():
        assert sum(r["zona"] == z for r in R) == n, z
    for nombre, (s, _) in {"diag-08-01_rbs": rbs(R), "diag-08-02_matriz-exposicion": matriz(R)}.items():
        ids = re.findall(r"R-\d\d", s)
        assert sorted(ids) == sorted(r["id"] for r in R), (nombre, len(ids), set(r["id"] for r in R)-set(ids))
        p = AQUI / f"{nombre}.svg"; p.write_text(s, encoding="utf-8")
        ink = shutil.which("inkscape")
        if ink:
            subprocess.run([ink, str(p), "-o", str(p.with_suffix(".pdf"))], check=True, capture_output=True)
            subprocess.run([ink, str(p), "-o", str(p.with_suffix(".png")), "-d", "200"], check=True, capture_output=True)
        print("ok", nombre)
main()
