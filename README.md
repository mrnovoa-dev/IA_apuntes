# IA · Apuntes

Web de apuntes de **Inteligencia Artificial con Python** para *Tecnoloxías Intelixentes* (1º Bachillerato, curso 2026-27).

| Página | Contenido |
|--------|-----------|
| `index.html` | Portada: acceso a todo el material, unidades del curso y descargas |
| `teoria.html` | Teoría fundamental de la UD2 (secciones 0–15, con los conceptos de IA de la UD1) con índice navegable |
| `mapa.html` | Mapa visual: conceptos, 43 librerías filtrables, chuletas y autoevaluación |
| `descargas/` | Teoría en `.odt` (editable) y en Markdown (fuente) |

## Publicar con GitHub Pages

*Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save.*
La web quedará en `https://mrnovoa-dev.github.io/IA_apuntes/`.

## Actualizar la teoría

1. Edita `descargas/Teoria_Fundamental_Conceptos_UD2.md`.
2. Ejecuta `./build.sh` (necesita [pandoc](https://pandoc.org/)) para regenerar `teoria.html`.
3. Para el `.odt`: `pandoc descargas/Teoria_Fundamental_Conceptos_UD2.md -o descargas/Teoria_Fundamental_Conceptos_UD2.odt`.

Los ejemplos de código usan Python 3.10+. Algunos necesitan conexión a Internet (datasets de Seaborn, APIs) o instalar librerías con `pip`.
