#!/usr/bin/env python3
"""Genera las páginas de la web a partir del Markdown.

  python3 build.py            # pide la contraseña de las soluciones
  IA_SOL_PASS=... python3 build.py

Necesita pandoc (>= 2.x) y la librería `cryptography` (pip install cryptography).

Las fuentes con soluciones (`contenidos/*.md`) NO se suben al repositorio
público (están en .gitignore). En la web, cada bloque
<details class="sol">…</details> se cifra con AES-256-GCM y una clave derivada
de la contraseña con PBKDF2-SHA256: el texto de las soluciones no aparece en el
HTML publicado y solo se descifra en el navegador con la contraseña.
"""
import base64
import getpass
import os
import re
import secrets
import subprocess
import sys
from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

RAIZ = Path(__file__).resolve().parent
PLANTILLA = RAIZ / "assets" / "plantilla.html"
ITERACIONES = 250_000

# (fuente, salida, clave de navegación)
PAGINAS = [
    ("contenidos/ud1.md", "ud1.html", "ud1"),
    ("contenidos/ejercicios.md", "ejercicios.html", "ejercicios"),
    ("contenidos/ud3-vision.md", "ud3-vision.html", "ud3-vision"),
    ("contenidos/ud4-lenguaje.md", "ud4-lenguaje.html", "ud4-lenguaje"),
    ("contenidos/ud5-ml.md", "ud5-ml.html", "ud5-ml"),
    ("contenidos/asignatura.md", "asignatura.html", "asignatura"),
    ("contenidos/datos.md", "datos.html", "datos"),
    ("contenidos/libro.md", "libro.html", "libro"),
    ("contenidos/apps.md", "apps.html", "apps"),
    ("contenidos/chuletas.md", "chuletas.html", "chuletas"),
    ("descargas/Teoria_Fundamental_Conceptos_UD2.md", "teoria.html", "teoria"),
]

SOL = re.compile(r'<details class="sol">\s*<summary>(.*?)</summary>.*?</details>', re.S)


def b64(b: bytes) -> str:
    return base64.b64encode(b).decode()


def cifrar_soluciones(html: str, password: str):
    sal = secrets.token_bytes(16)
    clave = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=sal, iterations=ITERACIONES).derive(password.encode())
    aes = AESGCM(clave)
    n = 0

    def sustituir(m):
        nonlocal n
        n += 1
        iv = secrets.token_bytes(12)
        ct = aes.encrypt(iv, m.group(0).encode(), None)
        etiqueta = re.sub(r"<[^>]+>", "", m.group(1)).replace('"', "&quot;")
        return f'<div class="sol-lock" data-label="{etiqueta}" data-iv="{b64(iv)}" data-ct="{b64(ct)}"></div>'

    return SOL.sub(sustituir, html), b64(sal), n


def main():
    faltan = [f for f, _, _ in PAGINAS if not (RAIZ / f).exists()]
    if faltan:
        sys.exit("Faltan fuentes: " + ", ".join(faltan) + "\n(las de contenidos/ están en el Proyecto de Claude, no en GitHub)")
    password = os.environ.get("IA_SOL_PASS") or getpass.getpass("Contraseña de las soluciones: ")
    for fuente, salida, nav in PAGINAS:
        extra = ["--metadata", "title=Teoría UD2",
                 "--metadata", "description=Teoría fundamental de Python para IA (UD2): fundamentos, NumPy, Pandas, visualización, ETL, ML, Big Data, librerías, apps y ampliación."] if nav == "teoria" else []
        html = subprocess.run(
            ["pandoc", fuente, "-f", "gfm+yaml_metadata_block", "-t", "html5", "-s",
             "--template", str(PLANTILLA), "--toc", "--toc-depth=3",
             "--highlight-style=pygments", f"-V", f"cur-{nav}=1", *extra],
            cwd=RAIZ, check=True, capture_output=True, text=True).stdout
        html, sal, n = cifrar_soluciones(html, password)
        if n:
            html = html.replace('<article class="content">',
                                f'<article class="content" data-salt="{sal}" data-iter="{ITERACIONES}">', 1)
        (RAIZ / salida).write_text(html, encoding="utf-8")
        print(f"{salida:<20} {n:>3} soluciones cifradas")


if __name__ == "__main__":
    main()
