#!/usr/bin/env python3
"""Autoprueba del harness: los ejemplos válidos deben pasar y cada caso de pruebas/ debe fallar con su código.

Uso:  python3 scripts/probar_harness.py
"""
import pathlib
import subprocess
import sys

from _comun import RAIZ, cargar_spec
from validar import validar

ok = True
for p in sorted((RAIZ / "ejemplos").glob("*.json")):
    e, _ = validar(cargar_spec(p))
    print(("✓" if not e else "✗"), "válido   ", p.name, "" if not e else e)
    ok &= not e

for p in sorted((RAIZ / "pruebas").glob("E*.json")):
    esperado = p.name.split("_")[0]
    e, _ = validar(cargar_spec(p))
    acierto = any(x.startswith(esperado) for x in e)
    print(("✓" if acierto else "✗"), "rechazado", p.name, f"→ {esperado}" if acierto else f"esperaba {esperado}, obtuvo {e}")
    ok &= acierto

for p in sorted((RAIZ / "pruebas").glob("P_*")):
    r = subprocess.run([sys.executable, str(RAIZ / "scripts" / "lint.py"), str(p)], capture_output=True, text=True)
    print(("✓" if r.returncode == 1 else "✗"), "rechazado", p.name, "(lint)")
    ok &= r.returncode == 1

print("\nTODO EN ORDEN" if ok else "\nHAY FALLAS")
sys.exit(0 if ok else 1)
