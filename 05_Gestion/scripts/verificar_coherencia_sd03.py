#!/usr/bin/env python3
"""Pruebas de coherencia de sd-03.tex (puerta G0 del plan de estimación).

Solo informa. Lee `02_Propuesta/latex_final/sd-03.tex` y los anexos de `04_Adjuntos/tablas/` y
comprueba lo que un revisor humano suele dejar pasar al integrar secciones escritas por distintas
personas. Cada hallazgo lleva el identificador de la prueba (P0.n) del plan.

    python3 05_Gestion/scripts/verificar_coherencia_sd03.py [--tex RUTA] [--anexo-b RUTA]

Código de salida 0 si no hay hallazgos y 1 si los hay.
"""

import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TEX = RAIZ / "02_Propuesta" / "latex_final" / "sd-03.tex"
ANEXO_B = RAIZ / "04_Adjuntos" / "tablas" / "sd-03_s2_anexo-b_catalogo-requerimientos.md"

# Títulos de tabla o figura al comienzo de línea (con o sin llaves o negrita), no menciones dentro del texto.
CAPTION = re.compile(r"^\s*\{?\s*(?:\\textbf\{|\\emph\{|\\textit\{)?\s*(Tabla|Figura)\s+(\d+(?:\.\d+)?)\s*[.:]")
INCLUDE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
NOMBRES_ANTIGUOS = [
    (r"plataforma com[uú]n", "«plataforma común» es el nombre antiguo de la base tecnológica"),
    (r"\b(?:R-0[1-9]|F-0[1-3])\b", "código de servicio antiguo (usar R:M-01, F:C-01, etc.)"),
]
NUMEROS = {"ocho": 8, "nueve": 9, "diez": 10}
NORMA = re.compile(r"(Ley\s+N\.[ºo°]\s*[\d.]+|Circular\s+N\.[ºo°]\s*\d+(?:\s+de\s+la\s+CMF)?)")


def lineas_utiles(texto):
    """Pares (n.º de línea, texto) sin las líneas de comentario de LaTeX."""
    return [(i, l) for i, l in enumerate(texto.splitlines(), 1) if not l.lstrip().startswith("%")]


def seccion(texto, titulo):
    """Texto de una sección sin numerar (`\\section*{titulo}`) hasta la siguiente sección o el final."""
    m = re.search(r"\\section\*\{" + re.escape(titulo) + r"\}", texto)
    if not m:
        return ""
    resto = texto[m.end():]
    fin = re.search(r"\\section\*?\{|\\ossFinalPage|\\end\{document\}", resto)
    return resto[: fin.start()] if fin else resto


def numeracion_duplicada(texto):
    """P0.2. Devuelve hallazgos de tablas o figuras con el mismo número."""
    vistos = {}
    for n, l in lineas_utiles(texto):
        m = CAPTION.match(l)
        if m:
            vistos.setdefault((m.group(1), m.group(2)), []).append(n)
    return [
        f"P0.2 {tipo} {num} aparece como título en las líneas {', '.join(map(str, ls))}"
        for (tipo, num), ls in sorted(vistos.items())
        if len(ls) > 1
    ]


def figuras_faltantes(texto, carpeta):
    """P0.3. Archivos de figura que el .tex referencia y no existen."""
    out = []
    for n, l in lineas_utiles(texto):
        for ruta in INCLUDE.findall(l):
            if not (Path(carpeta) / ruta).exists():
                out.append(f"P0.3 línea {n}: falta el archivo de figura {ruta}")
    return out


def plataformas_inconsistentes(texto):
    """P0.4. El recuento de plataformas actuales debe ser el mismo en todo el texto."""
    hallados = {}
    for n, l in lineas_utiles(texto):
        for m in re.finditer(r"\b(ocho|nueve|diez)\s+(?:plataformas|sistemas)\b", l, re.I):
            hallados.setdefault(NUMEROS[m.group(1).lower()], []).append(n)
    if len({k for k in hallados if k in (8, 9)}) > 1:
        detalle = "; ".join(f"{k} en las líneas {', '.join(map(str, v))}" for k, v in sorted(hallados.items()))
        return [f"P0.4 el recuento de plataformas no coincide ({detalle})"]
    return []


def nombres_antiguos(texto):
    """P0.5. Nombres o códigos descartados."""
    out = []
    for n, l in lineas_utiles(texto):
        for patron, mensaje in NOMBRES_ANTIGUOS:
            if re.search(patron, l, re.I):
                out.append(f"P0.5 línea {n}: {mensaje}")
    return out


def normas_sin_referencia(texto):
    """P0.6. Normas citadas en el cuerpo que no figuran en la lista de Referencias."""
    referencias = seccion(texto, "Referencias")
    cuerpo = texto.replace(referencias, "")
    out = []
    for norma in sorted(set(re.sub(r"\s+", " ", m) for m in NORMA.findall(cuerpo))):
        if norma.startswith("Ley"):
            citada = re.search(r"\d[\d.]*", norma).group(0).rstrip(".") in referencias
        else:
            citada = norma.split()[0] in referencias
        if not citada:
            out.append(f"P0.6 la norma «{norma}» se cita en el texto y no está en Referencias")
    return out


def declaracion_ia_incompleta(texto):
    """P0.7. La declaración de uso de IA debe nombrar todas las secciones numeradas con contenido."""
    declaracion = seccion(texto, "Declaración de uso de IA")
    if not declaracion:
        return ["P0.7 no existe la sección «Declaración de uso de IA»"]
    out = []
    for m in re.finditer(r"\\section\{(3\.\d)\s", texto):
        num = m.group(1)
        inicio = m.end()
        siguiente = re.search(r"\\section\{|\\section\*\{", texto[inicio:])
        cuerpo = texto[inicio : inicio + (siguiente.start() if siguiente else len(texto))]
        sin_comentarios = "\n".join(l for l in cuerpo.splitlines() if not l.lstrip().startswith("%"))
        if len(sin_comentarios.split()) > 50 and num not in declaracion:
            out.append(f"P0.7 la declaración de uso de IA no menciona la sección {num}")
    return out


def totales_anexo_b(ruta):
    """Total, RF, RNF y OP del Anexo B (fila Total de la sección B.1)."""
    texto = Path(ruta).read_text(encoding="utf-8")
    m = re.search(r"\|\s*\*\*Total\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*", texto)
    if not m:
        return None
    rf, rnf, op = map(int, m.groups())
    return {"rf": rf, "rnf": rnf, "op": op, "total": rf + rnf + op}


def conteos_distintos(texto, totales):
    """P0.1. Las cifras del catálogo citadas en el texto coinciden con el Anexo B."""
    if not totales:
        return ["P0.1 no se pudo leer la fila Total del Anexo B"]
    out = []
    for nombre in ("total", "rf", "rnf", "op"):
        valor = totales[nombre]
        if not re.search(rf"\b{valor}\b", texto):
            out.append(f"P0.1 el texto no menciona {valor} ({nombre}) y el Anexo B lo registra")
    return out


def verificar(tex=TEX, anexo_b=ANEXO_B):
    texto = Path(tex).read_text(encoding="utf-8")
    hallazgos = []
    hallazgos += conteos_distintos(texto, totales_anexo_b(anexo_b) if Path(anexo_b).exists() else None)
    hallazgos += numeracion_duplicada(texto)
    hallazgos += figuras_faltantes(texto, Path(tex).parent)
    hallazgos += plataformas_inconsistentes(texto)
    hallazgos += nombres_antiguos(texto)
    hallazgos += normas_sin_referencia(texto)
    hallazgos += declaracion_ia_incompleta(texto)
    return hallazgos


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tex", default=str(TEX))
    ap.add_argument("--anexo-b", default=str(ANEXO_B))
    args = ap.parse_args(argv)
    hallazgos = verificar(args.tex, args.anexo_b)
    for h in hallazgos:
        print(h)
    print(f"{len(hallazgos)} hallazgo(s)")
    return 1 if hallazgos else 0


if __name__ == "__main__":
    sys.exit(main())
