# IA · Apuntes

Web de apuntes de **Inteligencia Artificial con Python** para *Tecnoloxías Intelixentes* (1º Bachillerato, curso 2026-27).

| Página | Contenido |
|--------|-----------|
| `index.html` | Portada: acceso a las cinco unidades, ejercicios y descargas |
| `asignatura.html` | La asignatura: objetivos, unidades, criterios, evaluación y metodología (programación 2026/27) |
| `ud1.html` | UD1 · Conceptos clave de la IA: desarrollo, ejemplos y ejercicios |
| `teoria.html` | Teoría de todo el curso (secciones 0–15, de la UD1 a la UD5) con índice navegable y la unidad de cada sección |
| `ejercicios.html` | Ejercicios E1–E127 de todas las unidades (cada bloque indica la suya) con pistas y soluciones, y ejercicios «prompt → código» |
| `ud3-vision.html` | UD3 · Visión artificial |
| `ud4-lenguaje.html` | UD4 · Procesamiento del lenguaje natural |
| `ud5-ml.html` | UD5 · Aprendizaje automático |
| `datos.html` | Itinerario de análisis de datos (UD2 → UD5): adquirir, explorar, limpiar y modelar. Estructura inspirada en el módulo «Análisis de datos (AD)» ([mp5101-ad.vercel.app](https://mp5101-ad.vercel.app/)) |
| `libro.html` | El libro de J. F. Puentes, capítulo a capítulo, con notebooks y banco de prompts |
| `apps.html` | Apps y juegos: diez proyectos de Python (P1–P10) y una revisión crítica (P11), con rúbrica y soluciones cifradas |
| `chuletas.html` | Chuletas visuales (imágenes en `assets/chuletas/`) de Python, NumPy, Pandas, Polars, Matplotlib, scikit-learn, TensorFlow, PyTorch y Terraform (catorce en total, algunas en dos versiones), con notas «Ojo» |
| `itinerario.html` | Itinerario «De Python a experto en IA» en seis etapas (fundamentos, ML y DL, LLM, agentes, evaluación, despliegue): qué aprender, dónde está en la web, qué falta, proyecto y evaluación de cada etapa, y rúbrica del portafolio |
| `algoritmos.html` | Catálogo de algoritmos de IA por familias (búsqueda, optimización, supervisado, no supervisado, redes, lenguaje, visión, refuerzo) con enlaces a la web, fichas de regresión lineal, KNN, k-means, A* y Q-learning, guía para elegir y ejercicios A1–A3 |
| `assets/menu.css`, `assets/menu.js` | Cabecera y menú principal comunes a todas las páginas (desplegables accesibles con teclado; botón «Menú» en el móvil). El HTML del menú lo genera `build.py` a partir de la lista `MENU`, también en `index.html` y `mapa.html` (entre las marcas `<!-- menu -->`) |
| `assets/img/`, `herramientas/figuras/` | Figuras explicativas propias (PNG). Se generan con `python3 herramientas/figuras/figuras_unidades.py` y `figuras_algoritmos.py` (matplotlib) y los mapas mentales con `mmdc -i herramientas/figuras/X.mmd -o assets/img/mapa_X.png -b white -w 1100`. En las páginas, al tocar una figura se abre a tamaño completo |
| `mapa.html` | Mapa visual: conceptos, 44 librerías filtrables, chuletas y autoevaluación |
| `descargas/` | Teoría en `.odt` (editable) y en Markdown (fuente) |

Las unidades siguen la programación oficial 2026/27 (UD3 Visión, UD4 Lenguaje) y el libro de J. F. Puentes Calvo, *Tecnologías Inteligentes* (2025, CC BY-NC-ND 4.0). Los textos son propios: el libro se cita por capítulos, no se copia.

## Licencia

- **Código** (`build.py`, `herramientas/`, scripts y estilos, y los fragmentos de código de los apuntes): [MIT](LICENSE).
- **Textos y figuras propias**: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es). Se pueden compartir y adaptar citando la autoría, sin fines comerciales y con la misma licencia.
- **No incluidos:** las chuletas de `assets/chuletas/` y demás materiales de terceros, que conservan la licencia de sus autores.

Detalles en [LICENSE-CONTENIDOS.md](LICENSE-CONTENIDOS.md).

Las tipografías de `assets/fonts/` (Archivo, Atkinson Hyperlegible Next y JetBrains Mono) se sirven desde la propia web y tienen licencia SIL Open Font License 1.1 (`assets/fonts/OFL-*.txt`).

## Soluciones con contraseña

Las soluciones de ejercicios y unidades están **cifradas** (AES-256-GCM con clave PBKDF2) dentro del HTML. Se abren en el navegador con la contraseña del profesorado; una vez abierta, se recuerda mientras dure la pestaña.

Las fuentes Markdown con las soluciones en claro (`contenidos/*.md`) **no se suben** a este repositorio público (están en `.gitignore`): se guardan en el Proyecto de Claude «Clases ESO Bachillerato».

## Publicar con GitHub Pages

*Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save.*
La web quedará en `https://mrnovoa-dev.github.io/IA_apuntes/`.

## Regenerar la web

1. Coloca las fuentes en `contenidos/` (incluidas `asignatura.md`, `datos.md` y `libro.md`, sin soluciones) y edita lo que necesites (la teoría está en `descargas/Teoria_Fundamental_Conceptos_UD2.md`).
2. Ejecuta `./build.sh` (necesita [pandoc](https://pandoc.org/) y `pip install cryptography`). Pide la contraseña con la que se cifran las soluciones.
3. Para el `.odt`: `pandoc descargas/Teoria_Fundamental_Conceptos_UD2.md -o descargas/Teoria_Fundamental_Conceptos_UD2.odt`.

Los ejemplos de código usan Python 3.10+. Algunos necesitan conexión a Internet (datasets de Seaborn, APIs) o instalar librerías con `pip`.
