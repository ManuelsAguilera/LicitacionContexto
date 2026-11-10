#!/usr/bin/env bash
# Valida, renderiza y exporta las figuras: ./construir.sh [ID ...]
set -u
AQUI="$(cd "$(dirname "$0")" && pwd)"
SK="$AQUI/../../../../.agents/skills/diagramas-ancoa"
python3 "$AQUI/generar_laminas.py" "$@" >/dev/null
mkdir -p "$AQUI/salida"
for j in "$AQUI"/especificaciones/*.json; do
  b=$(basename "$j" .json); k=${b%%_*}
  if [ $# -gt 0 ] && ! printf '%s\n' "$@" | grep -qx "$k"; then continue; fi
  if ! out=$(cd "$SK" && python3 scripts/validar.py "$j" 2>&1); then echo "== $b"; echo "$out" | grep -E "ERROR|AVISO"; continue; fi
  echo "$out" | grep -E "AVISO" | sed "s/^/$b: /"
  (cd "$SK" && python3 scripts/render_fisico.py "$j" "$AQUI/salida/$b" >/dev/null 2>&1) || { echo "render falla $b"; continue; }
  (cd "$AQUI/salida" && timeout 120 drawio -x -f png --scale 1.3 -b 16 -o "$b.png" "$b.drawio" --no-sandbox >/dev/null 2>&1) || echo "png falla $b"
  echo "ok $b"
done
