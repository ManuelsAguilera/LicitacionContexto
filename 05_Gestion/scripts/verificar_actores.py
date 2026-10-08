#!/usr/bin/env python3
"""Pruebas del maestro de actores (puerta G2a del plan de estimación).

Solo informa. Comprueba que el maestro `80_Artefactos/maestro_actores.md` cubre los grupos de
interés del sd-02, que nombra los roles y sistemas que aparecen en el sd-03 y que cada actor
pertenece a un grupo. También avisa cuando el sd-02 y el sd-03 usan nombres distintos para el
mismo actor.

    python3 05_Gestion/scripts/verificar_actores.py [--maestro RUTA] [--sd02 RUTA] [--sd03 RUTA]

Código de salida 0 si no hay hallazgos y 1 si los hay.
"""

import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
MAESTRO = RAIZ / "80_Artefactos" / "maestro_actores.md"
SD02 = RAIZ / "02_Propuesta" / "latex_final" / "sd-02.tex"
SD03 = RAIZ / "02_Propuesta" / "latex_final" / "sd-03.tex"

# Roles y sistemas que el sd-03 menciona y el maestro debe nombrar (P2a.2). Cada entrada es
# (patrón en el sd-03, texto que debe aparecer en el maestro).
VOCABULARIO = [
    (r"ERP/DTE", "ERP/DTE"),
    (r"\bWMS\b", "WMS"),
    (r"transportistas", "Transportistas"),
    (r"\bMarketing\b", "Marketing"),
    (r"vendedores de marketplace", "marketplace"),
    (r"Prevención de pérdidas", "Prevención de pérdidas"),
    (r"jefaturas de tienda", "Jefatura de tienda"),
    (r"cajeros?", "Cajero"),
    (r"repositores externos", "Repositor externo"),
    (r"titulares", "Titular de tarjeta"),
    (r"organismos fiscalizadores", "Autoridades fiscalizadoras"),
    (r"remuneraciones", "remuneraciones"),
    (r"fidelización", "fidelización"),
    (r"Concepción", "Concepción"),
]
# Pares de nombres distintos para el mismo actor (P2a.3): (nombre en un documento, nombre en el otro).
SINONIMOS = [(r"Contralor[íi]a", r"(?:Emisor y|[áa]rea de|Jef[ao] de) Cumplimiento", "Contraloría", "Cumplimiento")]  # nombre del rol, no la palabra común


def grupos_sd02(texto):
    """Primera columna de la Tabla 2.5 del sd-02 (Grupos de interés según influencia e interés)."""
    m = re.search(r"Tabla 2\.5[^\n]*\n(.*?)\\end\{longtable\}", texto, re.S)
    if not m:
        return []
    out = []
    for linea in m.group(1).splitlines():
        if "&" in linea and linea.rstrip().endswith("\\\\") and "Influencia" not in linea:
            primera = linea.split("&")[0].strip()
            if primera and not primera.startswith("\\") and primera != "Grupo":
                out.append(primera)
    return out


def tabla_markdown(texto, titulo):
    """Filas (listas de celdas) de la primera tabla que sigue al encabezado `titulo`."""
    i = texto.find(titulo)
    if i < 0:
        return []
    filas = []
    for linea in texto[i:].splitlines()[1:]:
        if linea.startswith("|"):
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if not set("".join(celdas)) <= set(":- "):
                filas.append(celdas)
        elif filas:
            break
    return filas[1:] if filas else []


def grupos_cubiertos(maestro, grupos):
    """P2a.1. Cada grupo del sd-02 aparece en la sección 2 del maestro."""
    filas = tabla_markdown(maestro, "## 2. Grupos de interés")
    nombres = {f[1].lower() for f in filas if len(f) > 1}
    return [f"P2a.1 el grupo «{g}» del sd-02 no está en el maestro" for g in grupos if g.lower() not in nombres]


def vocabulario_ausente(sd03, maestro):
    """P2a.2. Roles y sistemas que el sd-03 menciona y el maestro no nombra."""
    out = []
    for patron, termino in VOCABULARIO:
        if re.search(patron, sd03, re.I) and termino.lower() not in maestro.lower():
            out.append(f"P2a.2 el sd-03 menciona «{termino}» y el maestro no lo nombra")
    return out


def sinonimos_en_uso(sd02, sd03):
    """P2a.3. Un documento usa un nombre de rol y el otro usa un sinónimo. Los patrones son de rol
    (por ejemplo «Emisor y Cumplimiento») para no confundirlos con la palabra común «cumplimiento»."""
    out = []
    for a, b, nombre_a, nombre_b in SINONIMOS:
        en_02_a, en_02_b = bool(re.search(a, sd02)), bool(re.search(b, sd02))
        en_03_a, en_03_b = bool(re.search(a, sd03)), bool(re.search(b, sd03))
        if (en_02_a and not en_02_b and en_03_b and not en_03_a) or (en_03_a and not en_03_b and en_02_b and not en_02_a):
            out.append(f"P2a.3 el sd-02 y el sd-03 usan nombres distintos para el mismo actor: «{nombre_a}» y «{nombre_b}»")
    return out


def actores_sin_grupo(maestro):
    """P2a.4. Cada actor humano debe estar asignado a un grupo de interés (G-nn)."""
    filas = tabla_markdown(maestro, "### 3.1 Personas")
    out = []
    for f in filas:
        if len(f) >= 3 and not re.search(r"\bG-0\d\b", f[2]):
            out.append(f"P2a.4 el actor {f[0]} ({f[1]}) no está asignado a un grupo de interés")
    return out


def verificar(maestro=MAESTRO, sd02=SD02, sd03=SD03):
    m = Path(maestro).read_text(encoding="utf-8")
    t02 = Path(sd02).read_text(encoding="utf-8")
    t03 = Path(sd03).read_text(encoding="utf-8")
    h = []
    h += grupos_cubiertos(m, grupos_sd02(t02))
    h += vocabulario_ausente(t03, m)
    h += sinonimos_en_uso(t02, t03)
    h += actores_sin_grupo(m)
    return h


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--maestro", default=str(MAESTRO))
    ap.add_argument("--sd02", default=str(SD02))
    ap.add_argument("--sd03", default=str(SD03))
    args = ap.parse_args(argv)
    hallazgos = verificar(args.maestro, args.sd02, args.sd03)
    for h in hallazgos:
        print(h)
    print(f"{len(hallazgos)} hallazgo(s)")
    return 1 if hallazgos else 0


if __name__ == "__main__":
    sys.exit(main())
