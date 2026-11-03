# IA · Apuntes

Web de apuntes de **Inteligencia Artificial con Python** para *Tecnoloxías Intelixentes* (1º Bachillerato, curso 2026-27).

| Página | Contenido |
|--------|-----------|
| `index.html` | Portada: acceso a las cinco unidades, ejercicios y descargas |
| `ud1.html` | UD1 · Conceptos clave de la IA: desarrollo, ejemplos y ejercicios |
| `teoria.html` | UD2 · Teoría de Python para IA (secciones 0–15) con índice navegable |
| `ejercicios.html` | UD2 · Ejercicios E1–E27 con pistas y soluciones, y ejercicios «prompt → código» |
| `ud3-vision.html` | UD3 · Visión artificial |
| `ud4-lenguaje.html` | UD4 · Procesamiento del lenguaje natural |
| `ud5-ml.html` | UD5 · Aprendizaje automático |
| `mapa.html` | Mapa visual: conceptos, 43 librerías filtrables, chuletas y autoevaluación |
| `descargas/` | Teoría UD2 en `.odt` (editable) y en Markdown (fuente) |

Las unidades siguen la programación oficial 2026/27 (UD3 Visión, UD4 Lenguaje) y el libro de J. F. Puentes Calvo, *Tecnologías Inteligentes* (2025, CC BY-NC-ND 4.0). Los textos son propios: el libro se cita por capítulos, no se copia.

## Soluciones con contraseña

Las soluciones de ejercicios y unidades están **cifradas** (AES-256-GCM con clave PBKDF2) dentro del HTML. Se abren en el navegador con la contraseña del profesorado; una vez abierta, se recuerda mientras dure la pestaña.

Las fuentes Markdown con las soluciones en claro (`contenidos/*.md`) **no se suben** a este repositorio público (están en `.gitignore`): se guardan en el Proyecto de Claude «Clases ESO Bachillerato».

## Publicar con GitHub Pages

*Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save.*
La web quedará en `https://mrnovoa-dev.github.io/IA_apuntes/`.

## Regenerar la web

1. Coloca las fuentes en `contenidos/` y edita lo que necesites (la teoría está en `descargas/Teoria_Fundamental_Conceptos_UD2.md`).
2. Ejecuta `./build.sh` (necesita [pandoc](https://pandoc.org/) y `pip install cryptography`). Pide la contraseña con la que se cifran las soluciones.
3. Para el `.odt`: `pandoc descargas/Teoria_Fundamental_Conceptos_UD2.md -o descargas/Teoria_Fundamental_Conceptos_UD2.odt`.

Los ejemplos de código usan Python 3.10+. Algunos necesitan conexión a Internet (datasets de Seaborn, APIs) o instalar librerías con `pip`.
