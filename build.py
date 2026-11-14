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
    ("contenidos/itinerario.md", "itinerario.html", "itinerario"),
    ("contenidos/algoritmos.md", "algoritmos.html", "algoritmos"),
    ("descargas/Teoria_Fundamental_Conceptos_UD2.md", "teoria.html", "teoria"),
]

SOL = re.compile(r'<details class="sol">\s*<summary>(.*?)</summary>.*?</details>', re.S)


# --- Unidad de cada sección (teoría y ejercicios son comunes a todo el curso) ---
UNIDADES = {
    "UD1": "ud1.html",
    "UD2": "asignatura.html#las-cinco-unidades",   # la UD2 no tiene página propia
    "UD3": "ud3-vision.html",
    "UD4": "ud4-lenguaje.html",
    "UD5": "ud5-ml.html",
    "Todas": "asignatura.html#las-cinco-unidades",
}
# Teoría: por número de sección (h2) o de apartado (h3, solo si cambia respecto a su sección)
UD_TEORIA = {
    "0": ["UD1"], "1": ["UD2"], "2": ["UD2"], "3": ["UD2"], "4": ["UD2"], "5": ["UD2"],
    "6": ["UD2"], "7": ["UD2"], "8": ["UD2"], "9": ["UD2"], "10": ["UD5"],
    "11": ["UD2", "UD5"], "12": ["UD2", "UD3", "UD5"], "13": ["UD2", "UD5"], "14": ["Todas"],
    "12.1": ["UD2"], "12.2": ["UD3", "UD5"], "12.3": ["UD2", "UD5"], "12.4": ["UD2"],
    "13.7": ["UD5"], "13.8": ["UD5"],
    "14.1": ["UD1"], "14.2": ["UD1"], "14.3": ["UD2"], "14.4": ["UD5"], "14.5": ["UD2"],
    "14.6": ["UD2"], "14.7": ["UD3", "UD5"], "14.8": ["UD4"], "14.9": ["UD2"],
    "14.10": ["UD2"], "14.11": ["UD2"], "14.12": ["UD1", "UD2"], "14.13": ["UD2"],
    "14.14": ["UD2"], "14.17": ["UD1", "UD2"], "14.18": ["UD2"], "14.19": ["UD2", "UD4", "UD5"],
}
# Ejercicios: por letra de bloque
UD_EJERCICIOS = {
    "A": ["UD2"], "B": ["UD2"], "C": ["UD2"], "D": ["UD2"], "E": ["UD2", "UD5"], "F": ["UD2"],
    "G": ["UD2"], "H": ["UD4"], "I": ["UD2"], "J": ["UD2"], "K": ["UD2"], "L": ["UD3", "UD5"], "M": ["UD2"], "N": ["UD1", "UD2"], "O": ["UD3", "UD5"], "P": ["UD2"], "Q": ["UD2", "UD3", "UD5"], "R": ["UD5"], "S": ["UD2"], "T": ["UD3", "UD5"], "U": ["UD2", "UD4", "UD5"],
    "prompt": ["UD2"],
}
CABECERA = re.compile(r'<(h[23])\s+id="([^"]+)">(.*?)</\1>', re.S)


def clave_teoria(nivel, texto):
    t = texto.replace("🔟", "10")
    t = re.sub(r"(\d)\ufe0f\u20e3", r"\1", t)
    m = re.match(r"\s*(\d+(?:\.\d+)?)", t)
    if not m:
        return None
    return m.group(1) if (nivel == "h2" or "." in m.group(1)) else None


def clave_ejercicios(nivel, texto):
    if nivel != "h2":
        return None
    m = re.match(r"\s*Bloque ([A-Z])\s", texto)
    if m:
        return m.group(1)
    return "prompt" if "prompt" in texto else None


def etiquetas(uds):
    enlaces = "".join(f'<a class="ud-tag" data-ud="{u}" href="{UNIDADES[u]}" title="{'Todas las unidades' if u == 'Todas' else 'Ir a la ' + u}">{u}</a>' for u in uds)
    return f'<span class="ud-tags">{enlaces}</span>'


def marcar_unidades(html, nav):
    if nav == "teoria":
        tabla, clave = UD_TEORIA, clave_teoria
    elif nav == "ejercicios":
        tabla, clave = UD_EJERCICIOS, clave_ejercicios
    else:
        return html
    marcadas = {}

    def cabecera(m):
        nivel, ident, texto = m.groups()
        k = clave(nivel, re.sub(r"<[^>]+>", "", texto))
        if k is None or k not in tabla:
            return m.group(0)
        marcadas[ident] = tabla[k]
        return f'<{nivel} id="{ident}">{texto}{etiquetas(tabla[k])}</{nivel}>'

    html = CABECERA.sub(cabecera, html)
    for ident, uds in marcadas.items():
        patron = re.compile(r'(<a\s+href="#' + re.escape(ident) + r'"\s+id="toc-[^"]*">.*?</a>)', re.S)
        html = patron.sub(lambda m: m.group(1) + etiquetas(uds), html, count=1)
    return html


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


# Menú principal: una sola definición para todas las páginas (plantilla, index.html y mapa.html).
# Cada entrada: (texto, enlace, clave de página) o (grupo, [(texto, descripción, enlace, clave), ...]).
MENU = [
    ("Inicio", "./", "index"),
    ("Unidades", [
        ("La asignatura", "Programación, criterios y evaluación", "asignatura.html", "asignatura"),
        ("UD1 · Conceptos de IA", "Qué es la IA, búsqueda, agentes, ética", "ud1.html", "ud1"),
        ("UD2 · Python y datos", "En la teoría y los ejercicios del curso", "teoria.html#1️⃣-fundamentos-de-programación", None),
        ("UD3 · Visión artificial", "Imágenes, CNN, YOLO, OCR", "ud3-vision.html", "ud3-vision"),
        ("UD4 · Lenguaje", "PLN, embeddings, Transformers", "ud4-lenguaje.html", "ud4-lenguaje"),
        ("UD5 · Aprendizaje automático", "Modelos, métricas, validación, ética", "ud5-ml.html", "ud5-ml"),
    ]),
    ("Teoría", "teoria.html", "teoria"),
    ("Ejercicios", "ejercicios.html", "ejercicios"),
    ("Guías", [
        ("Itinerario IA con Python", "De Python a experto en IA en seis etapas", "itinerario.html", "itinerario"),
        ("Análisis de datos", "De los datos al modelo", "datos.html", "datos"),
        ("Algoritmos de IA", "Catálogo: qué hace cada uno y cuándo usarlo", "algoritmos.html", "algoritmos"),
        ("Mapa de librerías", "Guía visual de Python para IA", "mapa.html", "mapa"),
    ]),
    ("Recursos", [
        ("Apps y juegos", "Proyectos con rúbrica", "apps.html", "apps"),
        ("Chuletas", "Infografías de las librerías", "chuletas.html", "chuletas"),
        ("El libro", "J. F. Puentes, capítulo a capítulo", "libro.html", "libro"),
    ]),
]


def menu_html(actual):
    """HTML del menú con la página actual marcada (aria-current) y su grupo resaltado."""
    def cur(clave):
        return ' aria-current="page"' if clave == actual else ""
    li = []
    for entrada in MENU:
        if isinstance(entrada[1], str):
            texto, enlace, clave = entrada
            li.append(f'<li><a href="{enlace}"{cur(clave)}>{texto}</a></li>')
            continue
        grupo, items = entrada
        ident = "menu-" + grupo.lower()
        clase = "menu-grupo actual" if any(c == actual for *_, c in items) else "menu-grupo"
        sub = "".join(f'<li><a href="{e}"{cur(c)}>{t}<small>{d}</small></a></li>' for t, d, e, c in items)
        li.append(f'<li class="{clase}"><button type="button" class="menu-grupo-boton" aria-expanded="false" '
                  f'aria-controls="{ident}">{grupo}</button><ul class="menu-sub" id="{ident}">{sub}</ul></li>')
    return ('<nav class="menu" aria-label="Principal">'
            '<button type="button" class="menu-boton" aria-expanded="false" aria-controls="menu-lista">'
            '<span class="menu-boton-ico" aria-hidden="true">☰</span>Menú</button>'
            '<ul class="menu-lista" id="menu-lista">' + "".join(li) + '</ul></nav>')


MARCA_MENU = re.compile(r"<!-- menu -->.*?<!-- /menu -->", re.S)


def actualizar_menus_estaticos():
    """index.html y mapa.html no salen de pandoc: se les reescribe el menú entre las marcas."""
    for archivo, clave in [("index.html", "index"), ("mapa.html", "mapa")]:
        ruta = RAIZ / archivo
        texto = ruta.read_text(encoding="utf-8")
        nuevo = MARCA_MENU.sub(lambda m: "<!-- menu -->" + menu_html(clave) + "<!-- /menu -->", texto)
        if nuevo != texto:
            ruta.write_text(nuevo, encoding="utf-8")


def main():
    faltan = [f for f, _, _ in PAGINAS if not (RAIZ / f).exists()]
    if faltan:
        sys.exit("Faltan fuentes: " + ", ".join(faltan) + "\n(las de contenidos/ están en el Proyecto de Claude, no en GitHub)")
    password = os.environ.get("IA_SOL_PASS") or getpass.getpass("Contraseña de las soluciones: ")
    for fuente, salida, nav in PAGINAS:
        extra = ["--metadata", "title=Teoría",
                 "--metadata", "description=Teoría de todo el curso de Tecnoloxías Intelixentes, de la UD1 a la UD5: conceptos de IA, Python, NumPy, Pandas, visualización, ETL, ML, Big Data, librerías, apps, redes neuronales e IA generativa."] if nav == "teoria" else []
        html = subprocess.run(
            ["pandoc", fuente, "-f", "gfm+yaml_metadata_block", "-t", "html5", "-s",
             "--template", str(PLANTILLA), "--toc", "--toc-depth=3",
             "--highlight-style=pygments", "-V", f"menu={menu_html(nav)}", *extra],
            cwd=RAIZ, check=True, capture_output=True, text=True).stdout
        html = marcar_unidades(html, nav)
        html, sal, n = cifrar_soluciones(html, password)
        if n:
            html = html.replace('<article class="content">',
                                f'<article class="content" data-salt="{sal}" data-iter="{ITERACIONES}">', 1)
        (RAIZ / salida).write_text(html, encoding="utf-8")
        print(f"{salida:<20} {n:>3} soluciones cifradas")
    actualizar_menus_estaticos()


if __name__ == "__main__":
    main()
