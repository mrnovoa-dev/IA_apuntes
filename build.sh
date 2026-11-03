#!/usr/bin/env bash
# Regenera teoria.html a partir del Markdown (requiere pandoc >= 2.x)
set -e
cd "$(dirname "$0")"
pandoc descargas/Teoria_Fundamental_Conceptos_UD2.md -f gfm -t html5 -s \
  --template assets/plantilla_teoria.html --toc --toc-depth=3 \
  --highlight-style=pygments --metadata title="Teoría UD2" -o teoria.html
echo "teoria.html generado"
