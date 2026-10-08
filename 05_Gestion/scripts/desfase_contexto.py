#!/usr/bin/env python3
"""Detecta en el contexto vigente del sd-03 códigos y términos que las decisiones ya descartaron.

Solo informa. Lee los .md de 80_Artefactos/sd-03_contexto/ (sin historico/). Uso:
    python3 05_Gestion/scripts/desfase_contexto.py [--todo]
--todo incluye los archivos de consulta (auditoria_decisiones.md, insumos_3.3_3.4.md).
"""
import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CARPETA = RAIZ / "80_Artefactos" / "sd-03_contexto"
# Archivos que conservan códigos antiguos a propósito (tabla de equivalencias o consulta).
EXENTOS = {"divisiones_negocio_servicios_sd-03.md"}
CONSULTA = {"auditoria_decisiones.md", "insumos_3.3_3.4.md"}
PATRONES = [
    (r"\b(R-0[1-9]|F-0[1-3])\b", "código de servicio antiguo (usar R:M-01, F:C-01, etc.)"),
    (r"capacidad de absorci", "criterio descartado (capacidad de absorción)"),
    (r"se consultará al mandante|período de consultas|periodo de consultas", "el período de consultas ya cerró (validar al inicio del proyecto)"),
    (r"\b226 RF\b|\b76 RNF\b|\b311\b", "recuento antiguo del catálogo (vigente 308: 227 RF, 72 RNF, 9 OP)"),
    (r"cinco años de historial|historial de precios de 5 años|5 años de historial", "historial de precios vigente: tres años"),
    (r"\bplataforma común\b", "nombre antiguo (usar base tecnológica)"),
]

# Líneas que mencionan lo descartado precisamente para decir que ya no rige.
EXPLICA = re.compile(r"antiguo|obsoleto|cerr[oó]|reemplaz|partieron|superad|descart|ya no|antes", re.I)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--todo", action="store_true", help="incluir archivos de consulta")
    args = ap.parse_args()
    total = 0
    for p in sorted(CARPETA.glob("*.md")):
        if p.name in EXENTOS or (p.name in CONSULTA and not args.todo):
            continue
        for n, linea in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if linea.startswith(">") or EXPLICA.search(linea):
                continue
            for pat, msg in PATRONES:
                if re.search(pat, linea):
                    total += 1
                    print(f"{p.name}:{n}: {msg}")
    print(f"{total} hallazgo(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
