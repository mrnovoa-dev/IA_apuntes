#!/usr/bin/env bash
# Regenera todas las páginas (necesita pandoc y python3 con cryptography).
# Pide la contraseña de las soluciones, o léela de IA_SOL_PASS.
set -e
cd "$(dirname "$0")"
python3 build.py
