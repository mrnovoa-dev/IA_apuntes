# IA · Apuntes

Web de apuntes de **Inteligencia Artificial con Python** para *Tecnoloxías Intelixentes* (1º Bachillerato, curso 2026-27).

| Página | Contenido |
|--------|-----------|
| `index.html` | Portada: acceso a las cinco unidades, ejercicios y descargas |
| `asignatura.html` | La asignatura: objetivos, unidades, criterios, evaluación y metodología (programación 2026/27) |
| `ud1.html` | UD1 · Conceptos clave de la IA: desarrollo, ejemplos y ejercicios |
| `teoria.html` | Teoría de todo el curso (secciones 0–15, de la UD1 a la UD5) con índice navegable y la unidad de cada sección |
| `ejercicios.html` | Ejercicios E1–E99 de todas las unidades (cada bloque indica la suya) con pistas y soluciones, y ejercicios «prompt → código» |
| `ud3-vision.html` | UD3 · Visión artificial |
| `ud4-lenguaje.html` | UD4 · Procesamiento del lenguaje natural |
| `ud5-ml.html` | UD5 · Aprendizaje automático |
| `datos.html` | Itinerario de análisis de datos (UD2 → UD5): adquirir, explorar, limpiar y modelar. Estructura inspirada en el módulo «Análisis de datos (AD)» ([mp5101-ad.vercel.app](https://mp5101-ad.vercel.app/)) |
| `libro.html` | El libro de J. F. Puentes, capítulo a capítulo, con notebooks y banco de prompts |
| `apps.html` | Apps y juegos: diez proyectos de Python (P1–P10) y una revisión crítica (P11), con rúbrica y soluciones cifradas |
| `chuletas.html` | Chuletas visuales (imágenes en `assets/chuletas/`) de Python, NumPy, Pandas, Polars, Matplotlib, scikit-learn, TensorFlow, PyTorch y Terraform (catorce en total, algunas en dos versiones), con notas «Ojo» |
| `itinerario.html` | Itinerario «De Python a experto en IA» en seis etapas (fundamentos, ML y DL, LLM, agentes, evaluación, despliegue): qué aprender, dónde está en la web, qué falta, proyecto y evaluación de cada etapa, y rúbrica del portafolio |
| `mapa.html` | Mapa visual: conceptos, 43 librerías filtrables, chuletas y autoevaluación |
| `descargas/` | Teoría en `.odt` (editable) y en Markdown (fuente) |

Las unidades siguen la programación oficial 2026/27 (UD3 Visión, UD4 Lenguaje) y el libro de J. F. Puentes Calvo, *Tecnologías Inteligentes* (2025, CC BY-NC-ND 4.0). Los textos son propios: el libro se cita por capítulos, no se copia.

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
