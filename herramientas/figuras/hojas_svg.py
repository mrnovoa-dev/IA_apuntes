"""Hojas visuales en HTML + SVG en línea para la teoría (Git y agentes).

Se inspiran en la idea de las infografías que circulan por redes (fichas, comparaciones lado a lado,
flujos numerados, diagramas de ramas), pero con el estilo propio de la web: los colores salen de las
variables CSS (--ink, --pen, --marker, --c-ml...), así que funcionan en modo claro y oscuro.

Uso:  python3 herramientas/figuras/hojas_svg.py
Reescribe lo que haya entre <!-- hoja:NOMBRE --> y <!-- /hoja:NOMBRE --> en la teoría.
Importante (gfm): ningún bloque puede llevar líneas en blanco dentro.
"""
import math
from html import escape
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TEORIA = RAIZ / "descargas" / "Teoria_Fundamental_Conceptos_UD2.md"


# ---------- piezas de SVG ----------
def flechas(pref):
    """Puntas de flecha (una por color) con id único por figura."""
    out = []
    for nombre in ("pen", "vuelta", "ml", "tinta", "rojo"):
        out.append(f'<marker id="{pref}-{nombre}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" '
                   f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="sv-punta-{nombre}"/></marker>')
    return "<defs>" + "".join(out) + "</defs>"


def caja(x, y, w, h, titulo, sub=None, cls="sv-caja"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{cls}"/>'
    cx = x + w / 2
    if sub:
        s += f'<text x="{cx}" y="{y + h / 2 - 3}" class="sv-tit" text-anchor="middle">{escape(titulo)}</text>'
        s += f'<text x="{cx}" y="{y + h / 2 + 14}" class="sv-sub" text-anchor="middle">{escape(sub)}</text>'
    else:
        s += f'<text x="{cx}" y="{y + h / 2 + 5}" class="sv-tit" text-anchor="middle">{escape(titulo)}</text>'
    return s


def linea(d, pref, color="pen", cls=None, punta=True):
    c = cls or f"sv-l-{color}"
    m = f' marker-end="url(#{pref}-{color})"' if punta else ""
    return f'<path d="{d}" class="{c}"{m}/>'


def texto(x, y, t, cls="sv-ord", ancla="middle", rot=None):
    r = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{ancla}"{r}>{escape(t)}</text>'


def nodo(x, y, letra, cls="sv-n-main", txt="sv-n-txt"):
    return f'<circle cx="{x}" cy="{y}" r="11" class="{cls}"/><text x="{x}" y="{y + 4}" class="{txt}" text-anchor="middle">{escape(letra)}</text>'


def svg(pref, vb, titulo, desc, cuerpo, cls=""):
    return (f'<svg class="sv {cls}" viewBox="{vb}" role="img" aria-labelledby="{pref}-t {pref}-d">'
            f'<title id="{pref}-t">{escape(titulo)}</title><desc id="{pref}-d">{escape(desc)}</desc>'
            f'{flechas(pref)}{cuerpo}</svg>')


# ---------- Git: las cuatro zonas ----------
ZONAS_DESC = ("git add lleva los cambios de la carpeta de trabajo a la preparación; git commit, de la preparación al "
              "repositorio local; git push, del repositorio local a GitHub. De vuelta: git fetch descarga de GitHub al "
              "repositorio local, git pull descarga y une hasta la carpeta, y git restore --staged saca un archivo de la preparación.")


def zonas_h():
    p = "zh"
    b = ""
    xs = [10, 210, 410, 610]
    nombres = [("Carpeta de trabajo", "lo que editas"), ("Preparación", "lo que irá en la foto"),
               ("Repositorio local", "los commits"), ("GitHub (origin)", "la copia compartida")]
    for x, (t, s) in zip(xs, nombres):
        b += caja(x, 70, 140, 70, t, s, "sv-caja sv-caja-nube" if x == 610 else "sv-caja")
    # llaves
    b += '<path d="M10,52 V42 H550 V52" class="sv-llave"/><path d="M610,52 V42 H750 V52" class="sv-llave"/>'
    b += texto(280, 33, "En tu ordenador", "sv-zona") + texto(680, 33, "En internet", "sv-zona")
    # adelante
    for (a, z, ord_) in [(150, 210, "add"), (350, 410, "commit"), (550, 610, "push")]:
        b += texto((a + z) / 2, 89, ord_) + linea(f"M{a + 4},97 H{z - 4}", p)
    # atrás
    b += linea("M606,121 H554", p, "vuelta") + texto(580, 162, "fetch", "sv-ord sv-ord-vuelta")
    b += linea("M280,144 V172 H115 V146", p, "vuelta") + texto(198, 189, "restore --staged", "sv-ord sv-ord-vuelta")
    b += linea("M680,144 V222 H45 V146", p, "vuelta") + texto(362, 240, "pull = fetch + merge", "sv-ord sv-ord-vuelta")
    return svg(p, "0 0 760 252", "Las cuatro zonas de Git", ZONAS_DESC, b, "sv-h")


def zonas_v():
    p = "zv"
    b = texto(90, 38, "En tu ordenador", "sv-zona", "start") + texto(90, 428, "En internet", "sv-zona", "start")
    ys = [50, 170, 290, 440]
    nombres = [("Carpeta de trabajo", "lo que editas"), ("Preparación", "lo que irá en la foto"),
               ("Repositorio local", "los commits"), ("GitHub (origin)", "la copia compartida")]
    for y, (t, s) in zip(ys, nombres):
        b += caja(90, y, 180, 64, t, s, "sv-caja sv-caja-nube" if y == 440 else "sv-caja")
    for (a, z, ord_) in [(114, 170, "add"), (234, 290, "commit"), (354, 440, "push")]:
        b += linea(f"M215,{a + 4} V{z - 4}", p) + texto(226, (a + z) / 2 + 5, ord_, "sv-ord", "start")
    b += linea("M150,436 V358", p, "vuelta") + texto(142, 402, "fetch", "sv-ord sv-ord-vuelta", "end")
    b += linea("M88,202 H62 V96 H86", p, "vuelta") + texto(54, 150, "restore --staged", "sv-ord sv-ord-vuelta", rot=-90)
    b += linea("M88,472 H28 V68 H86", p, "vuelta") + texto(20, 270, "pull = fetch + merge", "sv-ord sv-ord-vuelta", rot=-90)
    return svg(p, "0 0 360 512", "Las cuatro zonas de Git", ZONAS_DESC, b, "sv-v")


# ---------- Git: unir ramas ----------
def merge_svg():
    p = "gm"
    b = linea("M25,95 H260", p, cls="sv-r-main", punta=False)
    b += linea("M80,95 C95,40 105,40 120,40 H195 C230,40 245,70 258,90", p, cls="sv-r-rama", punta=False)
    for x, l in [(25, "A"), (80, "B"), (150, "C")]:
        b += nodo(x, 95, l)
    for x, l in [(120, "D"), (195, "E")]:
        b += nodo(x, 40, l, "sv-n-rama")
    b += nodo(260, 95, "M", "sv-n-union", "sv-n-txt-ink")
    b += texto(25, 124, "main", "sv-et", "start") + texto(157, 20, "rama", "sv-et sv-et-rama")
    b += texto(290, 124, "commit de unión (2 padres)", "sv-et", "end")
    return svg(p, "0 0 300 132", "git merge",
               "La rama con los commits D y E se une a main, que tenía el commit C, con un commit de unión M que tiene dos padres.", b)


def rebase_svg():
    p = "gr"
    b = linea("M80,95 C95,40 105,40 120,40 H185", p, cls="sv-r-tenue", punta=False)
    b += nodo(120, 40, "D", "sv-n-tenue", "sv-n-txt-tenue") + nodo(185, 40, "E", "sv-n-tenue", "sv-n-txt-tenue")
    b += texto(152, 20, "D y E de antes: se descartan", "sv-et sv-et-tenue")
    b += linea("M25,95 H140", p, cls="sv-r-main", punta=False) + linea("M140,95 H260", p, cls="sv-r-rama", punta=False)
    for x, l in [(25, "A"), (80, "B"), (140, "C")]:
        b += nodo(x, 95, l)
    b += nodo(200, 95, "D′", "sv-n-nuevo", "sv-n-txt-ml") + nodo(260, 95, "E′", "sv-n-nuevo", "sv-n-txt-ml")
    b += texto(25, 124, "main", "sv-et", "start") + texto(290, 124, "D′ y E′: commits nuevos", "sv-et sv-et-rama", "end")
    return svg(p, "0 0 300 132", "git rebase",
               "Los commits D y E se vuelven a aplicar encima de C como D prima y E prima: historia en línea recta, pero con commits nuevos.", b)


def cherry_svg():
    p = "gc"
    b = linea("M25,95 H230", p, cls="sv-r-main", punta=False)
    b += linea("M85,95 C100,40 110,40 130,40 H250", p, cls="sv-r-rama", punta=False)
    for x, l in [(25, "A"), (85, "B"), (150, "C")]:
        b += nodo(x, 95, l)
    for x, l in [(130, "P"), (190, "X"), (250, "Q")]:
        b += nodo(x, 40, l, "sv-n-rama")
    b += linea("M196,52 C205,72 212,78 222,86", p, "ml", "sv-l-copia")
    b += nodo(230, 95, "X′", "sv-n-nuevo", "sv-n-txt-ml")
    b += texto(25, 124, "main", "sv-et", "start") + texto(250, 20, "otra rama", "sv-et sv-et-rama")
    b += texto(290, 124, "X′: copia de X, con otro código", "sv-et", "end")
    return svg(p, "0 0 300 132", "git cherry-pick",
               "Solo el commit X de otra rama se copia a main como X prima, sin traer P ni Q.", b)


# ---------- Agentes: agente frente a sistema agéntico ----------
AG_DESC = ("Un agente recibe una petición; el modelo usa una herramienta, observa el resultado y repite hasta responder. "
           "Un sistema agéntico parte de un objetivo, hace un plan, reparte el trabajo entre agentes (buscar, analizar, "
           "redactar), un revisor comprueba el resultado y, si no cumple, se rehace el plan; si cumple, entrega el resultado.")


def agentes_h():
    p = "ah"
    b = texto(10, 26, "Un agente: una tarea", "sv-zona", "start")
    b += caja(10, 48, 120, 46, "Petición") + caja(190, 48, 120, 46, "Modelo", cls="sv-caja sv-caja-ml")
    b += caja(400, 48, 130, 46, "Herramienta") + caja(620, 48, 130, 46, "Respuesta", cls="sv-caja sv-caja-ok")
    b += linea("M134,71 H186", p)
    b += linea("M314,62 H396", p) + texto(355, 55, "usa", "sv-et")
    b += linea("M396,82 H314", p, "vuelta") + texto(355, 100, "observa", "sv-et")
    b += linea("M250,98 V126 H685 V98", p) + texto(468, 120, "cuando termina", "sv-et")
    b += texto(10, 164, "Un sistema agéntico: un objetivo", "sv-zona", "start")
    b += caja(10, 214, 110, 46, "Objetivo") + caja(160, 214, 100, 46, "Plan", cls="sv-caja sv-caja-ml")
    for i, t in enumerate(["Buscar datos", "Analizar", "Redactar"]):
        y = 186 + i * 40
        b += caja(310, y, 130, 32, t, cls="sv-caja sv-caja-ml")
        b += linea(f"M264,237 L306,{y + 16}", p, "ml")
        b += linea(f"M444,{y + 16} L486,237", p, "ml")
    b += caja(490, 214, 110, 46, "Revisión") + caja(650, 214, 100, 46, "Resultado", cls="sv-caja sv-caja-ok")
    b += linea("M604,237 H646", p) + texto(625, 230, "✓", "sv-et sv-et-ok")
    b += linea("M545,210 V176 H210 V210", p, "rojo") + texto(380, 171, "✗ no cumple: rehacer el plan", "sv-et sv-et-no")
    b += linea("M124,237 H156", p)
    return svg(p, "0 0 760 312", "Agente frente a sistema agéntico", AG_DESC, b, "sv-h")


def agentes_v():
    p = "av"
    b = texto(20, 24, "Un agente: una tarea", "sv-zona", "start")
    b += caja(20, 40, 150, 44, "Petición") + caja(20, 120, 150, 44, "Modelo", cls="sv-caja sv-caja-ml")
    b += caja(210, 120, 130, 44, "Herramienta") + caja(20, 210, 150, 44, "Respuesta", cls="sv-caja sv-caja-ok")
    b += linea("M95,88 V116", p)
    b += linea("M174,132 H206", p) + texto(190, 114, "usa", "sv-et")
    b += linea("M206,154 H174", p, "vuelta") + texto(190, 180, "observa", "sv-et")
    b += linea("M95,168 V206", p) + texto(104, 192, "termina", "sv-et", "start")
    b += texto(20, 296, "Un sistema agéntico: un objetivo", "sv-zona", "start")
    b += caja(20, 312, 150, 42, "Objetivo") + caja(20, 380, 150, 42, "Plan", cls="sv-caja sv-caja-ml")
    b += linea("M95,358 V376", p)
    for i, t in enumerate(["Buscar", "Analizar", "Redactar"]):
        x = 10 + i * 112
        b += caja(x, 450, 100, 36, t, cls="sv-caja sv-caja-ml")
        b += linea(f"M95,426 L{x + 50},446", p, "ml")
        b += linea(f"M{x + 50},490 L95,514", p, "ml")
    b += caja(20, 518, 150, 42, "Revisión") + caja(20, 600, 150, 42, "Resultado", cls="sv-caja sv-caja-ok")
    b += linea("M95,564 V596", p) + texto(104, 585, "✓ cumple", "sv-et sv-et-ok", "start")
    b += linea("M174,539 H348 V401 H174", p, "rojo") + texto(340, 470, "✗ rehacer", "sv-et sv-et-no", rot=-90)
    return svg(p, "0 0 360 652", "Agente frente a sistema agéntico", AG_DESC, b, "sv-v")


# ---------- Agentes: formas de comunicación ----------
def patron(pref, tipo):
    b = ""
    if tipo == "secuencial":
        xs = [25, 75, 125, 175]
        for a, z in zip(xs, xs[1:]):
            b += linea(f"M{a + 12},45 H{z - 13}", pref, "ml")
        for x in xs:
            b += f'<circle cx="{x}" cy="45" r="11" class="sv-n-rama"/>'
    elif tipo == "paralelo":
        for y in (15, 45, 75):
            b += linea(f"M32,45 L86,{y}", pref, "ml") + linea(f"M112,{y} L166,45", pref, "ml")
            b += f'<circle cx="100" cy="{y}" r="11" class="sv-n-rama"/>'
        b += f'<circle cx="20" cy="45" r="11" class="sv-n-main"/><circle cx="180" cy="45" r="11" class="sv-n-main"/>'
    elif tipo == "jerarquica":
        for x in (40, 100, 160):
            b += linea(f"M100,27 L{x},62", pref, "ml") + f'<circle cx="{x}" cy="75" r="11" class="sv-n-rama"/>'
        b += '<circle cx="100" cy="15" r="11" class="sv-n-union"/>'
    else:
        pts = [(100, 15), (40, 75), (160, 75)]
        for (x1, y1), (x2, y2) in [(pts[0], pts[1]), (pts[1], pts[2]), (pts[2], pts[0])]:
            b += linea(f"M{x1 + (x2 - x1) * .2},{y1 + (y2 - y1) * .2} L{x1 + (x2 - x1) * .8},{y1 + (y2 - y1) * .8}", pref, "ml")
        for x, y in pts:
            b += f'<circle cx="{x}" cy="{y}" r="11" class="sv-n-rama"/>'
        b += texto(100, 58, "≤ N rondas", "sv-et")
    desc = {"secuencial": "Cuatro agentes en fila: cada uno pasa su resultado al siguiente.",
            "paralelo": "Un reparto inicial a tres agentes que trabajan a la vez y una unión final.",
            "jerarquica": "Un orquestador arriba que reparte el trabajo a tres agentes.",
            "colaborativa": "Tres agentes que se pasan información entre ellos, con un número máximo de rondas."}[tipo]
    return svg(pref, "0 0 200 90", tipo, desc, b, "sv-mini")


# ---------- hojas HTML ----------
def cmd(t):
    return f'<code class="cmd">{escape(t)}</code>'


def hoja_git():
    vocab = [("Repositorio", "la carpeta del proyecto con toda su historia (en <code>.git/</code>)"),
             ("Commit", "una foto de <b>todo</b> el proyecto en un momento, con mensaje, fecha y autoría"),
             ("Rama", "una línea de trabajo aparte; en realidad, un puntero a un commit"),
             ("HEAD", "dónde estás ahora; normalmente, la rama actual"),
             ("origin", "el nombre por defecto del repositorio remoto"),
             ("Clone", "copia de un repositorio remoto en tu ordenador"),
             ("Fork", "copia <b>en GitHub</b>, a tu nombre, del repositorio de otra persona"),
             ("Pull request", "propuesta para unir tus cambios, que otra persona revisa"),
             (".gitignore", "lista de archivos sin seguimiento que Git no debe mirar"),
             ("Stash", "un cajón para apartar cambios a medias"),
             ("Etiqueta (tag)", "un nombre fijo para una versión: <code>v1.0</code>")]
    deshacer = [("ok", "✓ se recupera", "git restore --staged a.py", "saca el archivo de la preparación; el cambio sigue"),
                ("ok", "✓ se recupera", "git stash -u", "aparta el trabajo a medias; vuelve con <code>git stash pop</code>"),
                ("ok", "✓ se recupera", "git reset --soft HEAD~1", "deshace el último commit; los cambios quedan preparados"),
                ("ok", "✓ se recupera", "git revert 851e20f", "commit nuevo que anula otro: lo único para lo ya subido"),
                ("medio", "⚠ a medias", "git reset --hard HEAD~1", "el commit vuelve con <code>git reflog</code>; lo no guardado, no"),
                ("no", "✗ sin vuelta atrás", "git restore a.py", "tira los cambios que no estaban en ningún commit"),
                ("no", "✗ sin vuelta atrás", "git clean -fd", "borra archivos y carpetas sin seguimiento; antes, <code>git clean -n</code>")]
    flujo = [("Partir de lo último", ["git switch main", "git pull"]),
             ("Una rama para la tarea", ["git switch -c arreglo/media"]),
             ("Cambiar y mirar qué cambió", ["git status", "git diff"]),
             ("Preparar, revisar y guardar", ["git add notas.py", "git diff --staged", 'git commit -m "Evita dividir entre cero"']),
             ("Subir la rama", ["git push -u origin arreglo/media"]),
             ("En GitHub: abrir la pull request", []),
             ("Tras unirla, ordenar", ["git switch main", "git pull", "git branch -d arreglo/media"])]
    h = ['<section class="hoja" aria-labelledby="hoja-git-t">',
         '<p class="hoja-titulo" id="hoja-git-t">Git en una hoja</p>',
         '<p class="hoja-nota">Un resumen para repasar o imprimir. Abajo está todo explicado con ejemplos.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Las cuatro zonas y las órdenes que mueven los cambios</h5>',
         zonas_h(), zonas_v(),
         f'<p class="ficha-pie">{cmd("git clone URL")} hace la primera copia: trae el repositorio de GitHub y llena las tres zonas de tu ordenador.</p></div>',
         '<div class="ficha"><h5>Git no es GitHub</h5><div class="vs">',
         '<div><b>Git</b><ul><li>Un programa que guarda versiones</li><li>Funciona en tu ordenador, sin internet</li>'
         '<li>Software libre (licencia GPL)</li><li>Commits, ramas, historial</li></ul></div>',
         '<div><b>GitHub</b><ul><li>Una web que guarda copias de repositorios Git</li><li>En internet</li>'
         '<li>De una empresa (Microsoft, desde 2018)</li><li><i>Pull requests</i>, <i>issues</i>, Actions, Pages</li></ul></div>',
         '</div><p class="ficha-pie">Hay alternativas a GitHub con el mismo Git: GitLab o Codeberg.</p></div>',
         '<div class="ficha"><h5>Vocabulario mínimo</h5><dl class="vocab">',
         "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in vocab), '</dl></div>',
         '<div class="ficha ancha"><h5>Unir ramas: tres formas</h5><div class="ramas">',
         f'<figure>{merge_svg()}<figcaption>{cmd("git merge rama")} junta las dos historias con un commit de unión.</figcaption></figure>',
         f'<figure>{rebase_svg()}<figcaption>{cmd("git rebase main")} rehace tus commits encima de main: historia recta, commits nuevos. Solo en ramas que nadie más usa.</figcaption></figure>',
         f'<figure>{cherry_svg()}<figcaption>{cmd("git cherry-pick X")} copia un solo commit de otra rama.</figcaption></figure>',
         '</div></div>',
         '<div class="ficha"><h5>Deshacer: ¿hay vuelta atrás?</h5><ul class="semaforo">',
         "".join(f'<li class="{c}">{cmd(o)}<span class="marca">{m}</span><span class="que">{q}</span></li>' for c, m, o, q in deshacer),
         '</ul></div>',
         '<div class="ficha"><h5>Una tarea en equipo, de principio a fin</h5><ol class="flujo">',
         "".join(f'<li><span class="paso">{escape(t)}</span>{"".join(cmd(c) for c in cs)}</li>' for t, cs in flujo),
         '</ol></div>',
         '</div></section>']
    return "\n".join(h)


def hoja_agentes():
    patrones = [("secuencial", "Secuencial", "Cada agente pasa su resultado al siguiente.", "un error al principio llega hasta el final."),
                ("paralelo", "En paralelo", "Varios a la vez sobre partes independientes; luego se juntan.", "resultados que se contradicen al unirlos."),
                ("jerarquica", "Jerárquica", "Un orquestador reparte, vigila y junta.", "si entiende mal el objetivo, todo sale mal."),
                ("colaborativa", "Colaborativa", "Se pasan información y debaten hasta ponerse de acuerdo.", "conversaciones sin fin: hace falta un máximo de rondas.")]
    h = ['<section class="hoja" aria-labelledby="hoja-ag-t">',
         '<p class="hoja-titulo" id="hoja-ag-t">Agentes en una hoja</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Un agente hace una tarea; un sistema agéntico persigue un objetivo</h5>',
         agentes_h(), agentes_v(),
         '<p class="ficha-pie">La diferencia no es el modelo, sino <b>quién decide los pasos</b> y cuántos hay. La flecha roja es lo que lo hace fiable: si nadie revisa, nadie rehace.</p></div>',
         '<div class="ficha ancha"><h5>Cómo se comunican varios agentes</h5><div class="patrones">',
         "".join(f'<figure>{patron("ap" + k[:3], k)}<figcaption><b>{t}.</b> {d} <span class="riesgo">Riesgo: {r}</span></figcaption></figure>'
                 for k, t, d, r in patrones),
         '</div></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Pandas ----------
def tabla(x, y, cab, filas, anchos, alto=26, clases=None, pref=""):
    """Tabla pequeña: cabecera + filas; clases[i] colorea la fila i (o celda si es lista)."""
    s = ""
    cx = x
    for c, w in zip(cab, anchos):
        s += f'<rect x="{cx}" y="{y}" width="{w}" height="{alto}" class="sv-t-cab"/>'
        s += f'<text x="{cx + w / 2}" y="{y + alto / 2 + 4}" class="sv-t-txt sv-t-txtcab" text-anchor="middle">{escape(c)}</text>'
        cx += w
    for i, fila in enumerate(filas):
        cx = x
        yy = y + alto * (i + 1)
        for j, (v, w) in enumerate(zip(fila, anchos)):
            k = (clases or [None] * len(filas))[i]
            if isinstance(k, list):
                k = k[j]
            s += f'<rect x="{cx}" y="{yy}" width="{w}" height="{alto}" class="sv-t-celda {k or ""}"/>'
            s += f'<text x="{cx + w / 2}" y="{yy + alto / 2 + 4}" class="sv-t-txt" text-anchor="middle">{escape(str(v))}</text>'
            cx += w
    return s


GB_DESC = ("La tabla de notas se separa en dos grupos, A y B; a cada grupo se le aplica la media; los resultados "
           "se juntan en una tabla nueva con una fila por grupo: A 7,0 y B 6,5.")
NOTAS = [("A", "8"), ("A", "6"), ("B", "5"), ("A", "7"), ("B", "8")]


def groupby_h():
    p = "pgh"
    cls = ["sv-g-a" if g == "A" else "sv-g-b" for g, _ in NOTAS]
    b = texto(185, 16, "1 · Separar", "sv-zona") + texto(400, 16, "2 · Aplicar", "sv-zona") + texto(585, 16, "3 · Juntar", "sv-zona")
    b += tabla(10, 40, ["grupo", "nota"], NOTAS, [60, 60], clases=cls)
    b += tabla(240, 24, ["grupo", "nota"], [r for r in NOTAS if r[0] == "A"], [60, 60], clases=["sv-g-a"] * 3)
    b += tabla(240, 146, ["grupo", "nota"], [r for r in NOTAS if r[0] == "B"], [60, 60], clases=["sv-g-b"] * 2)
    b += linea("M134,110 L236,80", p) + linea("M134,150 L236,186", p)
    b += linea("M364,89 H436", p) + texto(400, 81, "mean()", "sv-ord")
    b += linea("M364,198 H436", p) + texto(400, 190, "mean()", "sv-ord")
    b += caja(440, 66, 110, 46, "A → 7,0", cls="sv-caja sv-g-a")
    b += caja(440, 175, 110, 46, "B → 6,5", cls="sv-caja sv-g-b")
    b += linea("M554,89 L606,130", p) + linea("M554,198 L606,152", p)
    b += tabla(610, 104, ["grupo", "nota"], [("A", "7,0"), ("B", "6,5")], [60, 60], clases=["sv-g-a", "sv-g-b"])
    return svg(p, "0 0 740 236", "groupby: separar, aplicar y juntar", GB_DESC, b, "sv-h")


def groupby_v():
    p = "pgv"
    cls = ["sv-g-a" if g == "A" else "sv-g-b" for g, _ in NOTAS]
    b = texto(10, 22, "1 · Separar", "sv-zona", "start")
    b += tabla(120, 30, ["grupo", "nota"], NOTAS, [60, 60], clases=cls)
    b += linea("M150,190 L95,226", p) + linea("M210,190 L265,226", p)
    b += tabla(30, 230, ["grupo", "nota"], [r for r in NOTAS if r[0] == "A"], [60, 60], clases=["sv-g-a"] * 3)
    b += tabla(210, 230, ["grupo", "nota"], [r for r in NOTAS if r[0] == "B"], [60, 60], clases=["sv-g-b"] * 2)
    b += texto(180, 360, "2 · Aplicar mean()", "sv-zona")
    b += linea("M90,338 V372", p) + linea("M270,312 V372", p)
    b += caja(30, 376, 120, 42, "A → 7,0", cls="sv-caja sv-g-a") + caja(210, 376, 120, 42, "B → 6,5", cls="sv-caja sv-g-b")
    b += texto(180, 446, "3 · Juntar", "sv-zona")
    b += linea("M90,422 L160,460", p) + linea("M270,422 L200,460", p)
    b += tabla(120, 464, ["grupo", "nota"], [("A", "7,0"), ("B", "6,5")], [60, 60], clases=["sv-g-a", "sv-g-b"])
    return svg(p, "0 0 360 548", "groupby: separar, aplicar y juntar", GB_DESC, b, "sv-v")


MP_DESC = ("Tabla ancha con una columna por materia (alumno, mates, física) y tabla larga con una fila por alumno y "
           "materia (alumno, materia, nota). melt pasa de la ancha a la larga; pivot, de la larga a la ancha.")
ANCHA = [("Uxía", "8", "7"), ("Brais", "6", "9")]
LARGA = [("Uxía", "mates", "8"), ("Uxía", "física", "7"), ("Brais", "mates", "6"), ("Brais", "física", "9")]
CL_ANCHA = [[None, "sv-g-a", "sv-g-b"]] * 2
CL_LARGA = [[None, "sv-g-a", "sv-g-a"], [None, "sv-g-b", "sv-g-b"]] * 2


def meltpivot_h():
    p = "pmh"
    b = texto(130, 30, "Ancha: una columna por materia", "sv-zona")
    b += tabla(10, 46, ["alumno", "mates", "física"], ANCHA, [80, 80, 80], clases=CL_ANCHA)
    b += texto(598, 18, "Larga: una fila por dato", "sv-zona")
    b += tabla(470, 28, ["alumno", "materia", "nota"], LARGA, [85, 85, 85], clases=CL_LARGA)
    b += linea("M264,72 H462", p) + texto(363, 64, "melt", "sv-ord")
    b += linea("M462,112 H264", p, "vuelta") + texto(363, 132, "pivot", "sv-ord sv-ord-vuelta")
    return svg(p, "0 0 740 166", "melt y pivot", MP_DESC, b, "sv-h")


def meltpivot_v():
    p = "pmv"
    b = texto(180, 20, "Ancha: una columna por materia", "sv-zona")
    b += tabla(60, 30, ["alumno", "mates", "física"], ANCHA, [80, 80, 80], clases=CL_ANCHA)
    b += linea("M150,112 V176", p) + texto(140, 150, "melt", "sv-ord", "end")
    b += linea("M210,176 V112", p, "vuelta") + texto(220, 150, "pivot", "sv-ord sv-ord-vuelta", "start")
    b += texto(180, 196, "Larga: una fila por dato", "sv-zona")
    b += tabla(52, 206, ["alumno", "materia", "nota"], LARGA, [85, 85, 85], clases=CL_LARGA)
    return svg(p, "0 0 360 340", "melt y pivot", MP_DESC, b, "sv-v")


TEMP = {"original": [11, None, None, 14, 15, None, 13], "ffill": [11, 11, 11, 14, 15, 15, 13],
        "bfill": [11, 14, 14, 14, 15, 13, 13], "interpolate": [11, 12, 13, 14, 15, 14, 13]}


def huecos_svg(metodo):
    p = "ph" + metodo[:3]
    xs = [22 + 32 * i for i in range(7)]
    y = lambda v: 100 - (v - 10) * 14
    vals = TEMP[metodo]
    b = '<path d="M10,108 H226" class="sv-llave"/>'
    b += "".join(texto(x, 124, f"{8 + i}h", "sv-et") for i, x in enumerate(xs))
    pts = " ".join(f"{x},{y(v)}" for x, v in zip(xs, vals))
    b += f'<polyline points="{pts}" class="sv-l-tenue"/>'
    for x, v, o in zip(xs, vals, TEMP["original"]):
        if o is None:
            b += f'<circle cx="{x}" cy="{y(v)}" r="6" class="sv-n-nuevo"/>'
        else:
            b += f'<circle cx="{x}" cy="{y(v)}" r="5" class="sv-n-main"/>'
    desc = f"Temperaturas de 8 a 14 h con huecos a las 9, 10 y 13 h rellenados con {metodo}: " + ", ".join(str(v) for v in vals) + "."
    return svg(p, "0 0 236 132", metodo, desc, b, "sv-tab")


LOC_FILAS = [("0", "Uxía", "8"), ("1", "Brais", "6"), ("2", "Noa", "7"), ("3", "Iago", "5")]


def loc_svg(tipo):
    p = "pl" + tipo
    marca = {"loc": {1, 2}, "iloc": {1}}[tipo]
    cls = [["sv-t-idx"] + (["sv-g-sel"] * 2 if i in marca else [None, None]) for i in range(4)]
    b = tabla(20, 10, ["", "alumno", "nota"], LOC_FILAS, [40, 80, 60], clases=cls)
    desc = {"loc": "df.loc[1:2] selecciona las filas con etiqueta 1 y 2: el final se incluye.",
            "iloc": "df.iloc[1:2] selecciona solo la fila en la posición 1: el final no se incluye."}[tipo]
    return svg(p, "0 0 220 142", f"df.{tipo}[1:2]", desc, b, "sv-tab")


def hoja_pandas():
    guardar = [("no", "✗ no cambia df", "df.dropna()", "devuelve una tabla nueva y la tira si no la guardas"),
               ("ok", "✓ cambia df", "df = df.dropna()", "guarda el resultado en la misma variable"),
               ("ok", "✓ cambia df", 'df["total"] = df["a"] + df["b"]', "crear o cambiar una columna entera"),
               ("ok", "✓ cambia df", 'df.loc[df["nota"] < 5, "estado"] = "suspenso"', "cambiar solo algunas filas"),
               ("no", "✗ no cambia df", 'df[df["nota"] < 5]["estado"] = "suspenso"', "asignación encadenada: en pandas 3 no hace nada")]
    merge_filas = [("inner", ["2", "3"], "solo las claves que están en las dos"),
                   ("left", ["1", "2", "3"], "todas las de la izquierda; la 1 sin pareja queda con NaN"),
                   ("right", ["2", "3", "4"], "todas las de la derecha"),
                   ("outer", ["1", "2", "3", "4"], "todas; NaN donde falta pareja")]
    def chip(k):
        c = "izq" if k == "1" else "der" if k == "4" else "ambas"
        return f'<span class="clave {c}">{k}</span>'
    h = ['<section class="hoja" aria-labelledby="hoja-pd-t">',
         '<p class="hoja-titulo" id="hoja-pd-t">Pandas en una hoja</p>',
         '<p class="hoja-nota">Las operaciones que más cuesta imaginar, dibujadas. Abajo, cada una con su código.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>groupby: separar, aplicar y juntar</h5>', groupby_h(), groupby_v(),
         f'<p class="ficha-pie">{cmd("df.groupby(\"grupo\")[\"nota\"].mean()")} Con <code>.agg()</code> sale una fila por grupo; con <code>.transform()</code>, una por fila original.</p></div>',
         '<div class="ficha ancha"><h5>Ancha o larga: melt y pivot</h5>', meltpivot_h(), meltpivot_v(),
         f'<p class="ficha-pie">{cmd("df.melt(id_vars=\"alumno\", var_name=\"materia\", value_name=\"nota\")")} {cmd("larga.pivot(index=\"alumno\", columns=\"materia\", values=\"nota\")")} Los gráficos de Seaborn y <code>groupby</code> suelen querer la larga; para leer, la ancha.</p></div>',
         '<div class="ficha"><h5>merge: qué filas quedan</h5>',
         '<p class="ficha-pie" style="margin-block:0 8px">Claves a la izquierda: <span class="clave izq">1</span><span class="clave ambas">2</span><span class="clave ambas">3</span> · a la derecha: <span class="clave ambas">2</span><span class="clave ambas">3</span><span class="clave der">4</span></p>',
         '<dl class="vocab">', "".join(f'<dt><code>how="{h_}"</code></dt><dd>{"".join(chip(k) for k in ks)}<br><small>{q}</small></dd>' for h_, ks, q in merge_filas),
         '</dl></div>',
         '<div class="ficha"><h5>loc incluye el final; iloc, no</h5><div class="ramas">',
         f'<figure>{loc_svg("loc")}<figcaption>{cmd("df.loc[1:2]")} etiquetas 1 y 2</figcaption></figure>',
         f'<figure>{loc_svg("iloc")}<figcaption>{cmd("df.iloc[1:2]")} solo la posición 1</figcaption></figure>',
         '</div><p class="ficha-pie">Con el índice por defecto parecen iguales, pero no lo son. Para un solo valor: <code>df.at[1, "nota"]</code>.</p></div>',
         '<div class="ficha ancha"><h5>Rellenar huecos en datos ordenados</h5><div class="ramas">',
         f'<figure>{huecos_svg("ffill")}<figcaption>{cmd("ffill()")} repite el último valor. Solo usa el pasado.</figcaption></figure>',
         f'<figure>{huecos_svg("bfill")}<figcaption>{cmd("bfill()")} copia el siguiente: usa el futuro.</figcaption></figure>',
         f'<figure>{huecos_svg("interpolate")}<figcaption>{cmd("interpolate()")} línea recta entre vecinos: también necesita el siguiente.</figcaption></figure>',
         '</div><p class="ficha-pie">Puntos llenos: datos medidos. Huecos: valores inventados por el método.</p></div>',
         '<div class="ficha ancha"><h5>¿Se guarda el cambio?</h5><ul class="semaforo">',
         "".join(f'<li class="{c}">{cmd(o)}<span class="marca">{m}</span><span class="que">{q}</span></li>' for c, m, o, q in guardar),
         '</ul></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- LLM: del prompt a la respuesta ----------
LLM_DESC = ("La pregunta se trocea en tokens, cada token se convierte en un vector (tabla de embeddings más posición), "
            "pasa por N bloques de atención y red feed-forward, sale una puntuación (logit) por cada token posible, "
            "softmax con temperatura las convierte en probabilidades, se elige un token con muestreo y top-p, "
            "y el token nuevo se añade al texto y se repite.")
LLM_PASOS = [("Pregunta", "«…devolver un libro?»", "sv-caja"), ("Tokens", "trozos → números", "sv-caja"),
             ("Vectores", "tabla + posición", "sv-caja"), ("Bloques × N", "atención → FFN", "sv-caja sv-caja-ml"),
             ("Logits", "puntuación por token", "sv-caja"), ("Probabilidades", "softmax + temperatura", "sv-caja"),
             ("Elegir", "muestreo, top-p", "sv-caja"), ("Token nuevo", "«15»", "sv-caja sv-caja-ok")]


def llm_h():
    p = "lh"
    b = ""
    for i, (tt, s, c) in enumerate(LLM_PASOS[:4]):
        b += caja(10 + 190 * i, 40, 150, 58, tt, s, c)
    for i, (tt, s, c) in enumerate(LLM_PASOS[4:]):
        b += caja(580 - 190 * i, 190, 150, 58, tt, s, c)
    for i in range(3):
        b += linea(f"M{164 + 190 * i},69 H{196 + 190 * i}", p)
        b += linea(f"M{576 - 190 * i},219 H{544 - 190 * i}", p)
    b += linea("M655,102 V186", p)
    b += linea("M85,186 V150 H275 V102", p, "vuelta") + texto(180, 142, "se añade y se repite", "sv-et")
    b += texto(655, 30, "una vez por capa", "sv-et sv-et-rama")
    return svg(p, "0 0 740 256", "Del prompt a la respuesta", LLM_DESC, b, "sv-h")


def llm_v():
    p = "lv"
    b = ""
    for i, (tt, s, c) in enumerate(LLM_PASOS):
        b += caja(50, 16 + 80 * i, 200, 56, tt, s, c)
        if i < 7:
            b += linea(f"M150,{76 + 80 * i} V{92 + 80 * i}", p)
    b += linea("M48,604 H24 V124 H46", p, "vuelta") + texto(16, 370, "se añade y se repite", "sv-et", rot=-90)
    return svg(p, "0 0 262 680", "Del prompt a la respuesta", LLM_DESC, b, "sv-v")


TEMPS = {0.5: [86.7, 11.7, 1.6], 1.0: [66.5, 24.5, 9.0], 2.0: [50.6, 30.7, 18.6]}


def temp_svg(tt):
    p = "lt" + str(tt).replace(".", "")
    b = '<path d="M14,120 H222" class="sv-llave"/>'
    for i, (c, v) in enumerate(zip(["15", "30", "7"], TEMPS[tt])):
        x = 34 + 64 * i
        h = v * 0.95
        b += f'<rect x="{x}" y="{120 - h}" width="44" height="{h}" rx="3" class="{"sv-barra-1" if i == 0 else "sv-barra"}"/>'
        b += texto(x + 22, 114 - h, f"{v:.1f} %".replace(".", ","), "sv-et")
        b += texto(x + 22, 138, c, "sv-ord")
    desc = f"Con temperatura {tt}: 15 tiene {TEMPS[tt][0]} %, 30 tiene {TEMPS[tt][1]} % y 7 tiene {TEMPS[tt][2]} %."
    return svg(p, "0 0 236 146", f"Temperatura {tt}", desc, b, "sv-tab")


def kv_svg():
    p = "lk"
    b = texto(10, 16, "Prefill: toda la pregunta a la vez", "sv-zona", "start")
    b += '<rect x="6" y="24" width="112" height="26" rx="4" class="sv-llave"/>'
    for j in range(6):
        b += f'<rect x="{10 + 18 * j}" y="29" width="14" height="16" rx="2" class="sv-kv"/>'
    b += texto(128, 42, "6 filas de K y V", "sv-et", "start")
    b += texto(10, 80, "Decode: un token por paso", "sv-zona", "start")
    for i in range(4):
        y = 92 + 28 * i
        for j in range(6 + i):
            b += f'<rect x="{10 + 18 * j}" y="{y}" width="14" height="16" rx="2" class="sv-kv"/>'
        x = 10 + 18 * (6 + i)
        b += f'<rect x="{x}" y="{y}" width="14" height="16" rx="2" class="sv-kv-nuevo"/>'
        b += texto(x + 24, y + 13, f"paso {i + 1}: +1 fila", "sv-et", "start")
    b += texto(10, 214, "Azul: en la caché · naranja: token nuevo", "sv-et", "start")
    return svg(p, "0 0 300 222", "Caché KV", "En el prefill se calculan a la vez las K y V de los 6 tokens de la pregunta. En cada paso del decode solo se calcula la fila del token nuevo y se añade a la caché, que crece de 6 a 10 filas.", b, "sv-kvfig")


def hoja_llm():
    fases = [("Preentrenamiento", "predecir el siguiente token en billones de tokens de texto", "pesos cambian"),
             ("Ajuste supervisado (SFT)", "ejemplos de pregunta → buena respuesta", "pesos cambian"),
             ("Preferencias (RLHF, DPO)", "entre dos respuestas, cuál es mejor", "pesos cambian"),
             ("Uso (inferencia)", "responde a tu conversación", "pesos fijos")]
    confundir = [("Parámetros", "los pesos que se aprenden al entrenar"),
                 ("Ajustes de generación", "temperatura, top-p, longitud: los eliges al usarlo"),
                 ("Ventana de contexto", "lo que el modelo ve en esta respuesta; no es memoria permanente"),
                 ("Caché KV", "reutiliza cálculos dentro de una respuesta"),
                 ("Caché de respuestas", "guarda respuestas enteras; la monta la aplicación"),
                 ("Probabilidad", "lo frecuente en los textos de entrenamiento, no lo verdadero")]
    h = ['<section class="hoja" aria-labelledby="hoja-llm-t">',
         '<p class="hoja-titulo" id="hoja-llm-t">Un LLM en una hoja</p>',
         '<p class="hoja-nota">Del <i>prompt</i> a la respuesta, con el ejemplo «¿Cantos días teño para devolver un libro?». Los detalles, en la sección 10.10.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Del <i>prompt</i> a la respuesta, token a token</h5>', llm_h(), llm_v(),
         '<p class="ficha-pie">El modelo nunca escribe la respuesta de golpe: da la vuelta al circuito una vez por cada token.</p></div>',
         '<div class="ficha ancha"><h5>Logits → probabilidades: lo que cambia la temperatura</h5><div class="ramas">',
         "".join(f'<figure>{temp_svg(tt)}<figcaption>Temperatura {str(tt).replace(".", ",")}{" (más previsible)" if tt < 1 else " (más variada)" if tt > 1 else ""}</figcaption></figure>' for tt in TEMPS),
         '</div><p class="ficha-pie">Logits 2, 1 y 0 para «15», «30» y «7». La temperatura cambia lo aleatorio de la elección, no lo verdadero de la respuesta.</p></div>',
         '<div class="ficha"><h5>De texto a asistente</h5><ol class="flujo">',
         "".join(f'<li><span class="paso">{escape(tt)}</span>{escape(d)} <span class="pesos{" fijos" if "fijos" in pz else ""}">{pz}</span></li>' for tt, d, pz in fases),
         '</ol></div>',
         f'<div class="ficha"><h5>Prefill, decode y caché KV</h5>{kv_svg()}<p class="ficha-pie">Sin caché, cada paso recalcularía K y V de todo el texto. El resultado es el mismo; el trabajo, no.</p></div>',
         '<div class="ficha ancha"><h5>No confundir</h5><dl class="vocab">',
         "".join(f"<dt>{tt}</dt><dd>{d}</dd>" for tt, d in confundir), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Modelos pequeños (SLM) ----------
def memoria_svg():
    p = "sm"
    datos = [("32 bits", 32), ("16 bits", 16), ("8 bits", 8), ("4 bits", 4)]
    esc = 5.2                                   # px por GB
    base = 196
    b = f'<path d="M40,{base} H460" class="sv-llave"/>'
    for i, (et, gb) in enumerate(datos):
        x = 70 + 100 * i
        h = gb * esc
        b += f'<rect x="{x}" y="{base - h}" width="56" height="{h}" rx="3" class="{"sv-barra-1" if gb <= 8 else "sv-barra"}"/>'
        b += texto(x + 28, base - h - 6, f"{gb} GB", "sv-et")
        b += texto(x + 28, base + 18, et, "sv-ord")
    y8 = base - 8 * esc
    b += f'<path d="M40,{y8} H468" class="sv-l-rojo"/>' + texto(474, y8 - 4, "8 GB de RAM:", "sv-et sv-et-no", "start")
    b += texto(474, y8 + 12, "portátil sencillo", "sv-et sv-et-no", "start")
    return svg(p, "0 0 590 222", "Memoria de un modelo de 8000 millones de parámetros", MEM_DESC, b, "sv-memoria sv-h")


MEM_DESC = ("Solo los pesos: 32 GB con 32 bits, 16 GB con 16 bits, 8 GB con 8 bits y 4 GB con 4 bits. "
            "Solo la versión de 4 bits deja sitio en un portátil de 8 GB.")


def memoria_v():
    p = "smv"
    esc, base = 4.6, 176
    b = f'<path d="M10,{base} H290" class="sv-llave"/>'
    for i, (et, gb) in enumerate([("32 bits", 32), ("16 bits", 16), ("8 bits", 8), ("4 bits", 4)]):
        x = 22 + 70 * i
        h = gb * esc
        b += f'<rect x="{x}" y="{base - h}" width="46" height="{h}" rx="3" class="{"sv-barra-1" if gb <= 8 else "sv-barra"}"/>'
        b += texto(x + 23, base - h - 6, f"{gb} GB", "sv-et")
        b += texto(x + 23, base + 18, et, "sv-ord")
    y8 = base - 8 * esc
    b += f'<path d="M10,{y8} H290" class="sv-l-rojo"/>'
    b += texto(150, 218, "Línea roja: 8 GB de RAM (portátil sencillo)", "sv-et sv-et-no")
    return svg(p, "0 0 300 228", "Memoria de un modelo de 8000 millones de parámetros", MEM_DESC, b, "sv-v")


def encoger_svg(tipo):
    p = "se" + tipo[:3]
    if tipo == "destilar":
        b = '<circle cx="50" cy="55" r="38" class="sv-n-rama"/>' + texto(50, 59, "profesor", "sv-n-txt")
        b += '<circle cx="166" cy="55" r="27" class="sv-n-main"/>' + texto(166, 59, "alumno", "sv-n-txt")
        b += linea("M92,55 H134", p, "ml") + texto(113, 46, "imita", "sv-et")
        desc = "Un modelo grande, el profesor, enseña a uno pequeño, el alumno, que aprende a imitar sus respuestas."
    elif tipo == "cuantizar":
        b = texto(100, 34, "0,02137  −0,00841  0,01502", "sv-ord")
        b += linea("M100,44 V64", p)
        b += texto(100, 86, "13   −5   9", "sv-ord sv-ord-vuelta") + texto(100, 104, "× escala 0,00164", "sv-et")
        desc = "Tres pesos decimales se guardan como enteros pequeños, 13, menos 5 y 9, multiplicados por una escala común."
    else:
        xs1, xs2 = [30, 30, 30], [170, 170, 170]
        ys = [20, 55, 90]
        b = ""
        quitar = {(0, 2), (1, 0), (2, 1), (2, 2)}
        for i, y1 in enumerate(ys):
            for j, y2 in enumerate(ys):
                cls = "sv-r-tenue" if (i, j) in quitar else "sv-r-main"
                b += f'<path d="M36,{y1} L164,{y2}" class="{cls}"/>'
        for y in ys:
            b += f'<circle cx="30" cy="{y}" r="8" class="sv-n-main"/><circle cx="170" cy="{y}" r="8" class="sv-n-main"/>'
        desc = "Una red con nueve conexiones de las que se quitan cuatro, las que menos aportan."
    return svg(p, "0 0 200 112", tipo, desc, b, "sv-tab")


def hoja_slm():
    h = ['<section class="hoja" aria-labelledby="hoja-slm-t">',
         '<p class="hoja-titulo" id="hoja-slm-t">Modelos pequeños en una hoja</p>',
         '<div class="hoja-grid">',
         f'<div class="ficha ancha"><h5>Cuánto ocupa un modelo de 8000 millones de parámetros</h5>{memoria_svg()}{memoria_v()}'
         '<p class="ficha-pie">Solo los pesos; el contexto ocupa más. Con 4 bits cabe en un portátil; con 16, no.</p></div>',
         '<div class="ficha ancha"><h5>Tres formas de encoger un modelo</h5><div class="ramas">',
         f'<figure>{encoger_svg("destilar")}<figcaption><b>Destilar.</b> Un modelo pequeño aprende a imitar a uno grande.</figcaption></figure>',
         f'<figure>{encoger_svg("cuantizar")}<figcaption><b>Cuantizar.</b> Cada peso, con menos bits.</figcaption></figure>',
         f'<figure>{encoger_svg("podar")}<figcaption><b>Podar.</b> Quitar las conexiones que menos aportan.</figcaption></figure>',
         '</div></div>',
         '<div class="ficha"><h5>¿En tu ordenador o en la nube?</h5><div class="vs">',
         '<div><b>Modelo local</b><ul><li>Las preguntas no salen del centro</li><li>Gratis después de descargarlo</li><li>Funciona sin internet</li><li>Sabe menos y alucina más</li></ul></div>',
         '<div><b>Servicio en la nube</b><ul><li>Más capaz y rápido</li><li>Cuenta y edad mínima (18 en las API)</li><li>Se paga por token</li><li>Los datos salen a otra empresa</li></ul></div>',
         '</div></div>',
         '<div class="ficha"><h5>Probarlo en clase</h5><ol class="flujo">',
         '<li><span class="paso">Elegir un modelo de 1000 a 4000 millones</span>y leer su licencia</li>',
         f'<li><span class="paso">Instalar Ollama o LM Studio</span>lo hace antes el profesor</li>',
         f'<li><span class="paso">Ejecutarlo</span>{cmd("ollama run llama3.2:3b")}</li>',
         '<li><span class="paso">Ponerlo a prueba</span>preguntas del centro, en gallego, y anotar los errores</li>',
         '</ol></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Trocear para RAG (usa las mismas funciones que el ejemplo de la teoría) ----------
import re as _re
NORMAS = ("Os préstamos duran quince días. Pódense renovar unha vez.\n\n"
          "Quen devolva tarde un libro non poderá levar outro durante unha semana. "
          "Os dicionarios só se consultan na sala.\n\n"
          "A biblioteca abre no recreo e pola tarde, de 16:00 a 18:00.")


def _fijo(t, n=60):
    return [t[i:i + n] for i in range(0, len(t), n)]


def _frases(t, maximo=110):
    fr = _re.split(r"(?<=[.!?])\s+", t.replace("\n", " "))
    out, act = [], ""
    for f in fr:
        if act and len(act) + 1 + len(f) > maximo:
            out.append(act); act = f
        else:
            act = f"{act} {f}".strip()
    return out + [act]


def _recursivo(t, maximo=110, seps=(r"\n\n", r"(?<=[.!?]) ", " ")):
    if len(t) <= maximo or not seps:
        return [t.strip()]
    out = []
    for parte in _re.split(seps[0], t):
        out += _recursivo(parte, maximo, seps[1:])
    return [x for x in out if x]


def hoja_trocear():
    filas = []
    for nombre, f, nota in [("Fijo, 60 caracteres", _fijo, "parte «Quen», «unha» y «biblioteca»"),
                            ("Por frases, hasta 110", _frases, "frases enteras, pero junta dos de párrafos distintos"),
                            ("Recursivo, hasta 110", _recursivo, "respeta los párrafos; si no caben, corta por frases")]:
        tr = f(NORMAS)
        spans = "".join(f'<span class="trozo t{i % 3}"><b>{i + 1}</b>{escape(x.replace(chr(10), " ⏎ "))}</span>' for i, x in enumerate(tr))
        filas.append(f'<div class="trozos-fila"><p class="trozos-nombre"><b>{nombre}</b> · {len(tr)} trozos · {nota}</p><p class="trozos">{spans}</p></div>')
    h = ['<section class="hoja" aria-labelledby="hoja-tro-t">',
         '<p class="hoja-titulo" id="hoja-tro-t">El mismo texto, troceado de tres formas</p>',
         '<div class="hoja-grid"><div class="ficha ancha">', "".join(filas),
         '<p class="ficha-pie">Cada color es un trozo; ⏎ marca un salto de párrafo. Es la salida real del código de abajo.</p></div></div></section>']
    return "\n".join(h)


# ---------- Librerías de gráficos ----------
TAMANOS = [("Altair (HTML)", 2.2), ("Plotly con cdn", 8.4), ("Pygal (SVG)", 18.7), ("Matplotlib SVG", 24.6),
           ("Seaborn PNG", 45.4), ("Matplotlib PNG", 50.9), ("Plotly completo", 4711.2)]


def tamanos_svg():
    import math
    p = "gt"
    b = ""
    for i, (et, kb) in enumerate(TAMANOS):
        y = 14 + 30 * i
        w = 34 * math.log10(kb * 10)               # escala logarítmica: 0,1 KB → 0
        b += texto(124, y + 15, et, "sv-et", "end")
        b += f'<rect x="132" y="{y + 2}" width="{w:.1f}" height="18" rx="3" class="{"sv-barra-mala" if kb > 1000 else "sv-barra"}"/>'
        etiqueta = f"{kb:,.1f} KB".replace(",", " ").replace(".", ",") if kb < 1000 else "4,7 MB"
        b += texto(138 + w, y + 15, etiqueta, "sv-et", "start")
    b += texto(132, 232, "Escala logarítmica: cada marca es 10 veces más", "sv-et", "start")
    desc = "Lo que ocupa el mismo gráfico de barras: " + ", ".join(f"{e} {k} KB" for e, k in TAMANOS) + "."
    return svg(p, "0 0 370 240", "Cuánto ocupa el mismo gráfico", desc, b, "sv-tam")


def vector_svg():
    p = "gv"
    b = '<circle cx="62" cy="58" r="40" class="sv-vec"/>' + texto(62, 122, "SVG: nítido", "sv-et")
    pts = []
    for yy in range(8, 108, 10):                     # cuadrícula centrada en (198, 58)
        for xx in range(148, 248, 10):
            d = ((xx + 5 - 198) ** 2 + (yy + 5 - 58) ** 2) ** 0.5
            if 34 <= d <= 46:
                pts.append(f'<rect x="{xx}" y="{yy}" width="10" height="10" class="sv-pix"/>')
    b += "".join(pts) + texto(198, 122, "PNG: píxeles", "sv-et")
    return svg(p, "0 0 260 130", "Vectorial frente a mapa de bits",
               "El mismo círculo ampliado: en SVG el borde sigue siendo una línea limpia; en PNG se ven los cuadraditos de los píxeles.", b, "sv-tab")


def hoja_graficos():
    donde = [("En papel o en PDF", "Matplotlib (y Seaborn para gráficos estadísticos). PNG con <code>dpi=300</code> o, mejor, PDF o SVG"),
             ("Explorando datos en un cuaderno", "Seaborn para ir rápido; Plotly si necesitas zoom o ver cada punto"),
             ("En una web, con zoom y valores", "Plotly o Altair; Bokeh es otra opción"),
             ("En una web sencilla, sin JavaScript grande", "Un SVG: Pygal (con valores al pasar el ratón) o el SVG de Matplotlib"),
             ("Una aplicación con controles", "Streamlit o Dash, que dibujan con estas mismas librerías")]
    internet = [("ok", "✓ no", "PNG, PDF y SVG de Matplotlib", "todo va dentro del archivo"),
                ("medio", "⚠ en parte", "SVG de Pygal", "se ve sin internet, pero los valores al pasar el ratón cargan un script de kozea.github.io; con <code>js=[]</code> no lo pide"),
                ("ok", "✓ no", "Plotly con write_html()", "lleva dentro todo plotly.js: 4,7 MB"),
                ("no", "✗ sí", "Plotly con include_plotlyjs=\"cdn\"", "pesa 8 KB, pero descarga plotly.js de cdn.plot.ly al abrirlo"),
                ("no", "✗ sí", "HTML de Altair", "descarga Vega de cdn.jsdelivr.net al abrirlo")]
    h = ['<section class="hoja" aria-labelledby="hoja-gr-t">',
         '<p class="hoja-titulo" id="hoja-gr-t">Gráficos en una hoja</p>',
         '<p class="hoja-nota">La pregunta no es qué librería es mejor, sino dónde se va a ver el gráfico.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>¿Dónde se va a ver?</h5><dl class="vocab">',
         "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in donde), '</dl></div>',
         f'<div class="ficha"><h5>Cuánto ocupa el mismo gráfico</h5>{tamanos_svg()}<p class="ficha-pie">Medido con el código de abajo: Matplotlib 3.11, Plotly 7.1, Altair 6.3 y Pygal 3.1.</p></div>',
         f'<div class="ficha"><h5>Vectorial o mapa de bits</h5>{vector_svg()}<p class="ficha-pie"><b>SVG</b> y <b>PDF</b> guardan formas: se amplían sin perder nitidez y el texto se puede buscar. <b>PNG</b> guarda píxeles: va bien para fotos y mapas de calor con muchos puntos.</p></div>',
         '<div class="ficha ancha"><h5>¿Necesita internet al abrirlo?</h5><ul class="semaforo">',
         "".join(f'<li class="{c}"><code class="cmd">{escape(o)}</code><span class="marca">{m}</span><span class="que">{q}</span></li>' for c, m, o, q in internet),
         '</ul><p class="ficha-pie">Cargar un script de otro servidor también le dice a ese servidor quién abre la página: en una web del centro, mejor que todo vaya dentro.</p></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Python: ejecución, colecciones, concurrencia y herramientas ----------
EJ_PASOS = [("notas.py", "tu código"), ("Compilador", "lo traduce"), ("Bytecode", ".pyc en __pycache__"),
            ("Máquina virtual", "lo ejecuta"), ("Salida", "lo que ves")]
EJ_DESC = ("El archivo notas.py pasa por el compilador, que lo traduce a bytecode (archivos .pyc en la carpeta __pycache__); "
           "la máquina virtual de Python ejecuta ese bytecode y produce la salida. Compilador y máquina virtual forman el intérprete, CPython.")


def ejecucion_h():
    p = "pyh"
    b = '<path d="M155,30 V22 H585 V30" class="sv-llave"/>' + texto(370, 15, "el intérprete (CPython)", "sv-zona")
    for i, (tt, s) in enumerate(EJ_PASOS):
        cls = "sv-caja sv-caja-ok" if i == 4 else ("sv-caja sv-caja-ml" if i in (1, 3) else "sv-caja")
        b += caja(10 + 150 * i, 40, 125, 56, tt, s, cls)
        if i < 4:
            b += linea(f"M{139 + 150 * i},68 H{156 + 150 * i}", p)
    b += texto(370, 126, "Sí se compila, pero a bytecode y no a código máquina: por eso no sale un .exe", "sv-et")
    return svg(p, "0 0 745 136", "Cómo se ejecuta un programa de Python", EJ_DESC, b, "sv-h")


def ejecucion_v():
    p = "pyv"
    b = ""
    for i, (tt, s) in enumerate(EJ_PASOS):
        cls = "sv-caja sv-caja-ok" if i == 4 else ("sv-caja sv-caja-ml" if i in (1, 3) else "sv-caja")
        b += caja(40, 12 + 72 * i, 200, 52, tt, s, cls)
        if i < 4:
            b += linea(f"M140,{68 + 72 * i} V{80 + 72 * i}", p)
    b += '<path d="M248,84 H262 V280 H248" class="sv-llave"/>' + texto(274, 182, "intérprete", "sv-zona", rot=90)
    b += texto(140, 384, "Se compila a bytecode, no a código máquina", "sv-et")
    return svg(p, "0 0 290 394", "Cómo se ejecuta un programa de Python", EJ_DESC, b, "sv-v")


def concurrencia_svg(tipo):
    p = "pc" + tipo[:3]
    b = ""
    x0 = 66
    if tipo == "hilos":
        carriles = ["hilo 1", "hilo 2", "hilo 3"]
        tramos = [[("c", 0, 20), ("e", 20, 80), ("c", 80, 100)],
                  [("c", 20, 40), ("e", 40, 110), ("c", 110, 130)],
                  [("c", 40, 60), ("e", 60, 130), ("c", 130, 150)]]
    elif tipo == "procesos":
        carriles = ["núcleo 1", "núcleo 2", "núcleo 3"]
        tramos = [[("c", 0, 150)], [("c", 0, 150)], [("c", 0, 150)]]
    else:
        carriles = ["1 hilo"]
        tramos = [[("a", 0, 20), ("b", 20, 40), ("c3", 40, 60), ("a", 80, 100), ("b", 100, 120), ("c3", 120, 140)]]
    for i, (nom, tr) in enumerate(zip(carriles, tramos)):
        y = 14 + 30 * i
        b += texto(x0 - 6, y + 13, nom, "sv-et", "end")
        b += f'<path d="M{x0},{y + 9} H{x0 + 156}" class="sv-llave"/>'
        for k, a, z in tr:
            cls = {"c": "sv-cpu", "e": "sv-espera", "a": "sv-ta", "b": "sv-tb", "c3": "sv-tc"}[k]
            if k == "e":
                b += f'<path d="M{x0 + a},{y + 9} H{x0 + z}" class="{cls}"/>'
            else:
                b += f'<rect x="{x0 + a}" y="{y}" width="{z - a}" height="18" rx="2" class="{cls}"/>'
    if tipo == "asyncio":
        for k, letra in enumerate("ABCABC"):
            b += texto(x0 + 10 + 20 * k + (20 if k > 2 else 0), 27, letra, "sv-n-txt")
        b += texto(x0 + 70, 52, "← await: espera →", "sv-et")
    b += f'<path d="M{x0},104 H{x0 + 156}" class="sv-llave"/>' + texto(x0 + 156, 118, "tiempo →", "sv-et", "end")
    desc = {"hilos": "Tres hilos de un mismo proceso: calculan por turnos, nunca dos a la vez, y esperan a la red al mismo tiempo.",
            "procesos": "Tres procesos en tres núcleos calculando a la vez durante todo el tiempo.",
            "asyncio": "Un solo hilo que alterna las tareas A, B y C; cada una cede el turno con await mientras espera."}[tipo]
    return svg(p, "0 0 230 124", tipo, desc, b, "sv-tab")


def hoja_python():
    colecciones = [("Lista", "[1, 2, 2]", "✓", "✓", "✓", "por posición"),
                   ("Tupla", "(1, 2, 2)", "✓", "✗", "✓", "por posición"),
                   ("Conjunto", "{1, 2}", "✗", "✓", "✗", "no: se recorre o se pregunta «in»"),
                   ("Diccionario", '{"a": 1}', "✓ desde 3.7", "✓", "claves no", "por clave")]
    filas = "".join(f"<tr><th>{n}</th><td><code>{escape(e)}</code></td><td>{o}</td><td>{m}</td><td>{d}</td><td>{a}</td></tr>"
                    for n, e, o, m, d, a in colecciones)
    herramientas = [("Crear el proyecto", ["uv init proyecto"]), ("Añadir librerías", ["uv add requests"]),
                    ("Revisar y dar formato", ["ruff check --fix", "ruff format"]),
                    ("Comprobar tipos", ["mypy ."]), ("Probar", ["uv run pytest"]),
                    ("Guardar la versión", ['git commit -m "…"'])]
    h = ['<section class="hoja" aria-labelledby="hoja-py-t">',
         '<p class="hoja-titulo" id="hoja-py-t">Python en una hoja</p>',
         '<p class="hoja-nota">Cuatro ideas que muchas chuletas cuentan mal. Versión actual: Python 3.15 (octubre de 2026).</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Cómo se ejecuta tu programa</h5>', ejecucion_h(), ejecucion_v(),
         '<p class="ficha-pie">«Interpretado, sin compilación» es falso: CPython compila a bytecode y lo guarda en <code>__pycache__</code> para no repetirlo.</p></div>',
         f'<div class="ficha ancha"><h5>Las cuatro colecciones</h5><div class="tabla-ficha"><table><thead><tr><th></th><th>Ejemplo</th><th>Ordenada</th><th>Modificable</th><th>Duplicados</th><th>Acceso</th></tr></thead><tbody>{filas}</tbody></table></div>'
         '<p class="ficha-pie">Los diccionarios <b>sí</b> conservan el orden de inserción desde Python 3.7; muchas tablas todavía dicen que no.</p></div>',
         '<div class="ficha ancha"><h5>Tres formas de hacer varias cosas a la vez</h5><div class="ramas">',
         f'<figure>{concurrencia_svg("hilos")}<figcaption><b>Hilos</b> (<code>threading</code>). Se turnan para calcular (el GIL) y esperan a la vez: descargas, ficheros, red.</figcaption></figure>',
         f'<figure>{concurrencia_svg("procesos")}<figcaption><b>Procesos</b> (<code>multiprocessing</code>). Un núcleo cada uno, calculan de verdad a la vez: cálculos pesados.</figcaption></figure>',
         f'<figure>{concurrencia_svg("asyncio")}<figcaption><b><code>asyncio</code></b>. Un solo hilo; cada tarea cede el turno con <code>await</code> mientras espera: miles de conexiones.</figcaption></figure>',
         '</div><p class="ficha-pie">Bloque azul: calcular. Línea discontinua: esperar (red, disco).</p></div>',
         '<div class="ficha ancha"><h5>Las herramientas de un proyecto, en orden</h5><ol class="flujo">',
         "".join(f'<li><span class="paso">{escape(a)}</span>{"".join(cmd(c) for c in cs)}</li>' for a, cs in herramientas),
         '</ol></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Redes neuronales ----------
NEU_DESC = ("Tres entradas (1, 2 y 3) se multiplican por sus pesos (0,2, 0,4 y 0,2) y se suman con el sesgo 0: "
            "z = 1,6. La sigmoide convierte z en la salida 0,832.")


def neurona_h():
    p = "nh"
    b = ""
    for i, (v, w) in enumerate([("1,0", "0,2"), ("2,0", "0,4"), ("3,0", "0,2")]):
        y = 40 + 55 * i
        b += texto(14, y + 4, v, "sv-et", "start") + nodo(62, y, f"x{i + 1}")
        b += linea(f"M75,{y} L{300},{95 + (i - 1) * 14}", p, "tinta")
        yl = y + (95 + (i - 1) * 14 - y) * (150 - 75) / (300 - 75)
        b += texto(150, yl - 7, f"w{i + 1} = {w}", "sv-ord")
    b += texto(334, 18, "sesgo b = 0", "sv-et") + linea("M334,24 V55", p, "tinta")
    b += '<circle cx="334" cy="95" r="34" class="sv-caja"/>' + texto(334, 104, "Σ", "sv-tit")
    b += texto(334, 150, "z = 1·0,2 + 2·0,4 + 3·0,2 + 0", "sv-et") + texto(334, 168, "= 1,6", "sv-ord")
    b += linea("M370,95 H426", p) + caja(430, 66, 130, 58, "Activación", "sigmoide f(z)")
    b += linea("M562,95 H596", p) + caja(600, 66, 130, 58, "Salida", "ŷ = f(1,6) = 0,832", "sv-caja sv-caja-ok")
    return svg(p, "0 0 740 180", "Una neurona por dentro", NEU_DESC, b, "sv-h")


def neurona_v():
    p = "nv"
    b = ""
    for i, (v, w) in enumerate([("1,0", "0,2"), ("2,0", "0,4"), ("3,0", "0,2")]):
        x = 60 + 90 * i
        b += texto(x, 16, v, "sv-et") + nodo(x, 36, f"x{i + 1}")
        b += linea(f"M{x},49 L{150 + (i - 1) * 16},{140}", p, "tinta")
        b += [texto(88, 96, f"w1={w}", "sv-ord", "end"), texto(158, 72, f"w2={w}", "sv-ord", "start"),
              texto(212, 96, f"w3={w}", "sv-ord", "start")][i]
    b += '<circle cx="150" cy="172" r="30" class="sv-caja"/>' + texto(150, 181, "Σ", "sv-tit")
    b += linea("M262,172 H184", p, "tinta") + texto(262, 162, "b = 0", "sv-et", "end")
    b += texto(150, 222, "z = 0,2 + 0,8 + 0,6 + 0 = 1,6", "sv-et")
    b += linea("M150,230 V254", p) + caja(70, 258, 160, 56, "Activación", "sigmoide f(z)")
    b += linea("M150,316 V340", p) + caja(70, 344, 160, 56, "Salida", "ŷ = 0,832", "sv-caja sv-caja-ok")
    return svg(p, "0 0 300 410", "Una neurona por dentro", NEU_DESC, b, "sv-v")


BUCLE_DESC = ("Cada iteración repite cuatro pasos con un lote de datos: hacia delante se calcula la predicción, "
              "la pérdida mide el error, hacia atrás se calcula el gradiente de cada peso y se actualizan los pesos. "
              "Después se vuelve a empezar con el lote siguiente.")


def bucle_svg():
    p = "nb"
    b = caja(10, 14, 156, 60, "1 · Hacia delante", "predicción ŷ")
    b += caja(194, 14, 156, 60, "2 · Pérdida", "cuánto se equivoca")
    b += caja(194, 166, 156, 60, "3 · Hacia atrás", "gradiente de cada peso", "sv-caja sv-caja-ml")
    b += caja(10, 166, 156, 60, "4 · Actualizar", "w ← w − η · gradiente", "sv-caja sv-caja-ok")
    b += linea("M168,44 H190", p) + linea("M272,76 V162", p) + linea("M192,196 H170", p) + linea("M88,164 V78", p, "vuelta")
    b += texto(180, 114, "una vuelta", "sv-et") + texto(180, 130, "por lote", "sv-et")
    return svg(p, "0 0 360 236", "El bucle de entrenamiento", BUCLE_DESC, b, "sv-bucle")


def _curva(f, x0, x1, y0, y1, n=81, ancho=200, alto=120, m=14):
    pts = []
    for k in range(n):
        x = x0 + (x1 - x0) * k / (n - 1)
        y = f(x)
        px = m + (ancho - 2 * m) * (x - x0) / (x1 - x0)
        py = alto - m - (alto - 2 * m) * (y - y0) / (y1 - y0)
        pts.append(f"{px:.1f},{py:.1f}")
    return "M" + " L".join(pts)


ACTIVACIONES = [
    ("sigmoide", lambda z: 1 / (1 + math.exp(-z)), -0.2, 1.2, "salida entre 0 y 1", "Última capa en clasificación binaria"),
    ("tanh", math.tanh, -1.2, 1.2, "salida entre −1 y 1", "Centrada en 0; RNN y redes antiguas"),
    ("ReLU", lambda z: max(0.0, z), -1.2, 4.2, "0 si z < 0; z si no", "Capas ocultas: la más usada"),
    ("Leaky ReLU", lambda z: z if z > 0 else 0.1 * z, -1.2, 4.2, "pendiente pequeña si z < 0", "Evita neuronas «muertas»"),
]


def activacion_svg(i):
    nombre, f, y0, y1, rango, _ = ACTIVACIONES[i]
    p = f"na{i}"
    m, W, H = 14, 200, 120
    ycero = H - m - (H - 2 * m) * (0 - y0) / (y1 - y0)
    b = f'<path d="M{m},{ycero:.1f} H{W - m} M{W / 2},{m} V{H - m}" class="sv-llave"/>'
    for nivel in ((1,) if i == 0 else (1, -1) if i == 1 else ()):
        if True:
            yy = H - m - (H - 2 * m) * (nivel - y0) / (y1 - y0)
            b += f'<path d="M{m},{yy:.1f} H{W - m}" class="sv-r-tenue"/>' + texto(W - m, yy - 4, str(nivel).replace("-", "−"), "sv-et", "end")
    b += f'<path d="{_curva(f, -4, 4, y0, y1)}" class="sv-l-pen"/>'
    desc = f"Gráfica de {nombre} entre z = −4 y z = 4: {rango}."
    return svg(p, f"0 0 {W} {H}", nombre, desc, b, "sv-mini")


def tasa_svg(eta):
    p = "nt" + str(eta).replace(".", "")
    m, W, H = 14, 200, 120
    w, ws = 0.0, [0.0]
    for _ in range(20):
        w = w - eta * 2 * (w - 3)
        ws.append(w)
    y0, y1 = -4, 10
    def py(v):
        return H - m - (H - 2 * m) * (v - y0) / (y1 - y0)
    fuera = next((k for k, v in enumerate(ws) if not y0 <= v <= y1), None)
    vis = ws if fuera is None else ws[:fuera + 1]
    pts = " L".join(f"{m + (W - 2 * m) * k / 20:.1f},{py(v):.1f}" for k, v in enumerate(vis))
    b = f'<clipPath id="{p}-c"><rect x="{m}" y="{m}" width="{W - 2 * m}" height="{H - 2 * m}"/></clipPath>'
    b += f'<path d="M{m},{py(0):.1f} H{W - m}" class="sv-llave"/>'
    b += f'<path d="M{m},{py(3):.1f} H{W - m}" class="sv-r-tenue"/>' + texto(W - m, py(3) - 4, "mínimo: w = 3", "sv-et", "end")
    b += f'<path d="M{pts}" class="sv-l-pen" clip-path="url(#{p}-c)"/>'
    if fuera is not None:
        b += texto(m + (W - 2 * m) * fuera / 20 + 8, m + 14, f"paso {fuera}: w ≈ {ws[fuera]:.1f}, se sale".replace(".", ","), "sv-et sv-et-no", "start")
    b += texto(m, H - 1, "pasos 0 → 20", "sv-et", "start")
    desc = f"Valor de w en 20 pasos de descenso de gradiente sobre (w − 3)² con η = {eta}: termina en {ws[-1]:.2f}."
    return svg(p, f"0 0 {W} {H + 4}", f"Tasa de aprendizaje {eta}", desc, b, "sv-mini")


def hoja_redes():
    salidas = [("Regresión (un número)", "ninguna (lineal)", "MSE o MAE"),
               ("Sí / no", "sigmoide", "entropía cruzada binaria"),
               ("Una clase entre varias", "softmax", "entropía cruzada categórica"),
               ("Varias etiquetas a la vez", "una sigmoide por etiqueta", "entropía cruzada binaria")]
    filas = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in salidas)
    contra = [("Más datos", "lo que mejor funciona, si se puede"),
              ("L2", "castiga los pesos grandes: los encoge todos"),
              ("L1", "castiga cualquier peso: deja muchos en 0"),
              ("Dropout", "apaga neuronas al azar, solo al entrenar"),
              ("Parada temprana", "para cuando la validación deja de mejorar")]
    confundir = [("Época", "una pasada por todos los datos de entrenamiento"),
                 ("Lote", "los ejemplos de un paso: 1000 datos en lotes de 32 son 32 lotes, el último de 8"),
                 ("Iteración", "un paso de actualización, uno por lote"),
                 ("Parámetro", "lo que aprende la red: pesos y sesgos"),
                 ("Hiperparámetro", "lo que eliges tú: η, capas, tamaño de lote, épocas"),
                 ("Validación", "datos para decidir mientras entrenas"),
                 ("Prueba", "datos que solo se miran al final"),
                 ("Pérdida", "lo que se minimiza (BCE, MSE…)"),
                 ("Métrica", "lo que se informa (exactitud, F1…)")]
    h = ['<section class="hoja" aria-labelledby="hoja-nn-t">',
         '<p class="hoja-titulo" id="hoja-nn-t">Una red neuronal en una hoja</p>',
         '<p class="hoja-nota">Las piezas, cómo aprende y cómo se controla. Todos los números salen del código de esta sección.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Una neurona por dentro</h5>', neurona_h(), neurona_v(),
         '<p class="ficha-pie">Multiplicar, sumar y activar. Una red son muchas neuronas así, en capas.</p></div>',
         f'<div class="ficha"><h5>El bucle de entrenamiento</h5>{bucle_svg()}<p class="ficha-pie">La propagación hacia delante no cambia ningún peso: solo el paso 4 lo hace.</p></div>',
         f'<div class="ficha"><h5>¿Qué salida y qué pérdida?</h5><div class="tabla-ficha"><table><thead><tr><th>Problema</th><th>Última capa</th><th>Pérdida</th></tr></thead><tbody>{filas}</tbody></table></div>'
         '<p class="ficha-pie">En las capas ocultas, casi siempre ReLU.</p></div>',
         '<div class="ficha ancha"><h5>Funciones de activación</h5><div class="ramas cuatro">',
         "".join(f'<figure>{activacion_svg(i)}<figcaption><b>{n}</b>: {r}. {u}.</figcaption></figure>' for i, (n, _f, _a, _b, r, u) in enumerate(ACTIVACIONES)),
         '</div></div>',
         '<div class="ficha ancha"><h5>La tasa de aprendizaje η</h5><div class="ramas">',
         f'<figure>{tasa_svg(0.01)}<figcaption><b>η = 0,01</b>. Demasiado pequeña: en 20 pasos ni se acerca.</figcaption></figure>',
         f'<figure>{tasa_svg(0.1)}<figcaption><b>η = 0,1</b>. Adecuada: llega al mínimo sin pasarse.</figcaption></figure>',
         f'<figure>{tasa_svg(1.1)}<figcaption><b>η = 1,1</b>. Demasiado grande: cada paso se pasa más y diverge.</figcaption></figure>',
         '</div><p class="ficha-pie">Minimizando (w − 3)² desde w = 0. La línea discontinua es el mínimo.</p></div>',
         '<div class="ficha"><h5>Contra el sobreajuste</h5><dl class="vocab">',
         "".join(f"<dt>{a}</dt><dd>{d}</dd>" for a, d in contra), '</dl></div>',
         '<div class="ficha"><h5>No confundir</h5><dl class="vocab">',
         "".join(f"<dt>{a}</dt><dd>{d}</dd>" for a, d in confundir), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Algoritmos clásicos ----------
def _cambio_tabla(cantidad, monedas):
    INF = float("inf")
    mejor = [0] + [INF] * cantidad
    ultima = [0] * (cantidad + 1)
    for x in range(1, cantidad + 1):
        for m in monedas:
            if m <= x and mejor[x - m] + 1 < mejor[x]:
                mejor[x], ultima[x] = mejor[x - m] + 1, m
    return mejor, ultima


def _voraz(cantidad, monedas):
    usadas = []
    for m in sorted(monedas, reverse=True):
        while cantidad >= m:
            usadas.append(m)
            cantidad -= m
    return usadas


def pila_cola_svg():
    p = "pc"
    b = texto(80, 18, "Pila (LIFO)", "sv-tit")
    for i, t in enumerate(["abrir", "escribir", "borrar"]):
        y = 150 - 36 * i
        b += f'<rect x="30" y="{y}" width="100" height="30" rx="6" class="sv-caja{" sv-caja-ok" if i == 2 else ""}"/>' + texto(80, y + 20, t, "sv-sub")
    b += f'<path d="M30,{186} H130" class="sv-llave"/>'
    b += linea("M160,92 V62 H112", p, "tinta") + texto(165, 98, "entra", "sv-et", "start")
    b += linea("M112,46 H180 V28", p, "rojo") + texto(186, 32, "sale el último", "sv-et sv-et-no", "start")
    b += texto(530, 18, "Cola (FIFO)", "sv-tit")
    for i, t in enumerate(["Uxía", "Brais", "Noa"]):
        x = 430 + 80 * i
        b += f'<rect x="{x}" y="96" width="70" height="34" rx="6" class="sv-caja{" sv-caja-ok" if i == 0 else ""}"/>' + texto(x + 35, 118, t, "sv-sub")
    b += linea("M700,113 H674", p, "tinta") + texto(700, 150, "entra al final", "sv-et", "end")
    b += linea("M428,113 H384", p, "rojo") + texto(384, 150, "sale el primero", "sv-et sv-et-no", "start")
    desc = ("Pila: se apilan abrir, escribir y borrar; lo último que entra, borrar, es lo primero que sale. "
            "Cola: Uxía, Brais y Noa esperan; entra gente por el final y sale primero Uxía, que llegó antes.")
    return svg(p, "0 0 740 196", "Pila y cola", desc, b, "sv-h")


def pila_cola_v():
    p = "pcv"
    b = texto(110, 18, "Pila (LIFO)", "sv-tit")
    for i, t in enumerate(["abrir", "escribir", "borrar"]):
        y = 150 - 36 * i
        b += f'<rect x="60" y="{y}" width="110" height="30" rx="6" class="sv-caja{" sv-caja-ok" if i == 2 else ""}"/>' + texto(115, y + 20, t, "sv-sub")
    b += linea("M215,92 V62 H174", p, "tinta") + texto(220, 98, "entra", "sv-et", "start")
    b += linea("M174,46 H235 V30", p, "rojo") + texto(242, 34, "sale el último", "sv-et sv-et-no", "start")
    b += texto(150, 222, "Cola (FIFO)", "sv-tit")
    for i, t in enumerate(["Uxía", "Brais", "Noa"]):
        x = 60 + 80 * i
        b += f'<rect x="{x}" y="240" width="70" height="34" rx="6" class="sv-caja{" sv-caja-ok" if i == 0 else ""}"/>' + texto(x + 35, 262, t, "sv-sub")
    b += linea("M326,257 H304", p, "tinta") + texto(300, 296, "entra al final", "sv-et", "end")
    b += linea("M58,257 H20", p, "rojo") + texto(14, 296, "sale el primero", "sv-et sv-et-no", "start")
    desc = ("Pila: lo último que entra, borrar, es lo primero que sale. "
            "Cola: entra gente por el final y sale primero Uxía, que llegó antes.")
    return svg(p, "0 0 340 306", "Pila y cola", desc, b, "sv-v")


def hoja_algoritmos():
    cantidad, monedas = 11, [1, 5, 6, 9]
    mejor, ultima = _cambio_tabla(cantidad, monedas)
    voraz = _voraz(cantidad, monedas)
    usadas, x = [], cantidad
    while x:
        usadas.append(ultima[x]); x -= ultima[x]
    celdas = "".join(
        f'<div{" class=\"fin\"" if i == cantidad else ""}><small>{i} €</small><b>{v}</b>'
        f'<small>{"—" if i == 0 else "+" + str(ultima[i])}</small></div>' for i, v in enumerate(mejor))
    nums, obj = [12, 7, 30, 3, 18], 25
    vistos, filas = {}, []
    for i, n in enumerate(nums):
        busca = obj - n
        esta = busca in vistos
        filas.append(f"<tr><td>{i}</td><td>{n}</td><td>{busca}</td><td>{'✓ en ' + str(vistos[busca]) if esta else '✗'}</td>"
                     f"<td>{'' if esta else f'{n}→{i}'}</td></tr>")
        if esta:
            break
        vistos[n] = i
    costes = [("x in lista", "recorre la lista: más datos, más tiempo"),
              ("x in conjunto o dict", "salta directo: casi igual con 10 que con 10 millones"),
              ("lista.append / pop()", "rápido: trabaja por el final"),
              ("lista.pop(0)", "lento: mueve todos los demás"),
              ("deque.popleft()", "rápido: hecho para colas"),
              ("sorted(lista)", "más que recorrerla una vez, menos que comparar todas las parejas")]
    h = ['<section class="hoja" aria-labelledby="hoja-alg-t">',
         '<p class="hoja-titulo" id="hoja-alg-t">Algoritmos clásicos en una hoja</p>',
         '<p class="hoja-nota">Tres problemas de entrevista y la estructura de datos que los resuelve. Todo calculado con el código de esta sección.</p>',
         '<div class="hoja-grid">',
         f'<div class="ficha ancha"><h5>Cambio de {cantidad} € con monedas de {", ".join(map(str, monedas))}</h5>',
         '<ul class="semaforo">',
         f'<li class="no"><b>Voraz</b><span class="marca">✗ {len(voraz)} monedas</span><span class="que">siempre la más grande que quepa: {" + ".join(map(str, voraz))}</span></li>',
         f'<li><b>Programación dinámica</b><span class="marca">✓ {mejor[cantidad]} monedas</span><span class="que">apunta el mejor resultado para cada cantidad: {" + ".join(map(str, sorted(usadas)))}</span></li>',
         '</ul>',
         f'<p class="ficha-pie">La tabla <code>mejor</code>: cuántas monedas hacen falta como mínimo para cada cantidad, y la última moneda que se añadió.</p><div class="celdas">{celdas}</div>',
         '<p class="ficha-pie">Para 11: la última moneda es 6, y 11 − 6 = 5 se hace con una moneda de 5. Con euros (1, 2, 5, 10…) la voraz sí acierta siempre.</p></div>',
         f'<div class="ficha"><h5>Dos que suman {obj}</h5><div class="tabla-ficha"><table><thead><tr><th>i</th><th>n</th><th>Falta</th><th>¿Está?</th><th>Anoto</th></tr></thead><tbody>{"".join(filas)}</tbody></table></div>',
         f'<p class="ficha-pie">Una sola pasada: el diccionario recuerda lo que ya vi. Probar todas las parejas, con 5000 números, son 12,5 millones de sumas.</p></div>',
         '<div class="ficha"><h5>¿Qué tarda y qué no?</h5><dl class="vocab">', "".join(f"<dt><code>{a}</code></dt><dd>{d}</dd>" for a, d in costes), '</dl></div>',
         f'<div class="ficha ancha"><h5>Pila y cola</h5>{pila_cola_svg()}{pila_cola_v()}<p class="ficha-pie">Pila: <code>append</code> y <code>pop()</code> de una lista (deshacer, llamadas a funciones). Cola: <code>deque</code> con <code>append</code> y <code>popleft()</code> (turnos, recorrido en anchura).</p></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Estadística inferencial ----------
def _medias_svg(n, semilla=1):
    import numpy as np
    rng = np.random.default_rng(semilla)
    espera = rng.exponential(scale=10, size=200_000)
    medias = rng.choice(espera, size=(20_000, n)).mean(axis=1)
    cuentas, bordes = np.histogram(medias, bins=24, range=(0, 40))
    W, H, m = 200, 120, 14
    ancho = (W - 2 * m) / len(cuentas)
    alto_max = cuentas.max()
    b = f'<path d="M{m},{H - m} H{W - m}" class="sv-llave"/>'
    for i, c in enumerate(cuentas):
        h = (H - 2 * m - 10) * c / alto_max
        if h > 0.5:
            b += f'<rect x="{m + i * ancho + 0.5:.1f}" y="{H - m - h:.1f}" width="{ancho - 1:.1f}" height="{h:.1f}" class="sv-barra"/>'
    x10 = m + (W - 2 * m) * 10 / 40
    b += f'<path d="M{x10:.1f},{m} V{H - m}" class="sv-r-tenue"/>' + texto(x10 + 4, m + 8, "media real 10", "sv-et", "start")
    b += texto(m, H - 1, "0", "sv-et", "start") + texto(W - m, H - 1, "40 min", "sv-et", "end")
    desc = (f"Histograma de 20 000 medias de muestras de {n} esperas del autobús. "
            f"Desviación de las medias: {medias.std():.1f} minutos.")
    return svg(f"tcl{n}", f"0 0 {W} {H}", f"Medias de muestras de tamaño {n}", desc, b, "sv-mini"), medias.std()


def _intervalos_svg():
    import numpy as np
    from math import sqrt
    rng = np.random.default_rng(11)
    W, H, m = 360, 250, 16
    mu, filas, fallos = 60, 20, 0
    b = ""
    x = lambda v: m + (W - 2 * m) * (v - 40) / 40
    b += f'<path d="M{x(mu):.1f},{m - 4} V{H - 22}" class="sv-llave"/>' + texto(x(mu), H - 6, "media real: 60 min", "sv-et")
    for i in range(filas):
        muestra = rng.gamma(shape=4, scale=15, size=40)
        c = muestra.mean()
        e = 2.023 * muestra.std(ddof=1) / sqrt(40)
        y = m + i * 10.5
        acierta = c - e <= mu <= c + e
        fallos += not acierta
        cls = "sv-l-pen" if acierta else "sv-l-rojo"
        b += f'<path d="M{x(c - e):.1f},{y:.1f} H{x(c + e):.1f}" class="{cls}"/>'
        b += f'<circle cx="{x(c):.1f}" cy="{y:.1f}" r="2.5" class="sv-n-main"/>'
        if not acierta:
            b += texto(x(c - e) - 6, y + 4, "✗ no la contiene", "sv-et sv-et-no", "end")
    desc = (f"Veinte intervalos de confianza del 95 % calculados con veinte muestras distintas de 40 alumnos. "
            f"{filas - fallos} contienen la media real de 60 minutos y {fallos} no.")
    return svg("tic", f"0 0 {W} {H}", "Veinte intervalos del 95 %", desc, b, "sv-ic"), fallos


def hoja_inferencia():
    figs = [(_medias_svg(n), n) for n in (1, 5, 30)]
    ic, fallos = _intervalos_svg()
    escalas = [("Nominal", "solo nombres: concello, color favorito. Se cuentan (moda)"),
               ("Ordinal", "tienen orden: insuficiente < bien < notable. Mediana, pero no restar"),
               ("Intervalo", "restar tiene sentido, pero el 0 no es «nada»: 20 ºC no es el doble de 10 ºC"),
               ("Razón", "cero real: minutos, alturas, euros. 40 min sí es el doble de 20")]
    sesgos = [("Selección", "la muestra no se parece a la población: encuesta solo al alumnado de la biblioteca"),
              ("No respuesta", "contestan sobre todo los más interesados o los más enfadados"),
              ("Supervivencia", "solo ves los casos que llegaron al final: los negocios que no cerraron"),
              ("Voluntarios", "quien se apunta a un estudio ya es distinto de quien no")]
    h = ['<section class="hoja" aria-labelledby="hoja-inf-t">',
         '<p class="hoja-titulo" id="hoja-inf-t">De la muestra a la población en una hoja</p>',
         '<p class="hoja-nota">Una muestra pequeña dice algo de toda la población, pero con un margen de error. Todo simulado con el código de esta sección.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Teorema central del límite: las medias se vuelven normales</h5><div class="ramas">',
         "".join(f'<figure>{svgm}<figcaption><b>Muestras de {n}</b>: las medias varían {d:.1f} min'
                 f'{" (es la población: muy asimétrica)" if n == 1 else ""}.</figcaption></figure>' for (svgm, d), n in figs),
         '</div><p class="ficha-pie">Esperas del autobús de 10 minutos de media. Con muestras de 30, las medias forman una campana estrecha alrededor de 10, aunque la población no sea normal.</p></div>',
         f'<div class="ficha"><h5>¿Qué significa «95 %»?</h5>{ic}<p class="ficha-pie">Cada línea es el intervalo de una muestra distinta. A la larga, unos 95 de cada 100 contienen la media real; aquí fallan {fallos} de 20. Para una muestra concreta no se sabe si acertó.</p></div>',
         '<div class="ficha"><h5>Sesgos al recoger datos</h5><dl class="vocab">', "".join(f"<dt>{a}</dt><dd>{d}</dd>" for a, d in sesgos), '</dl></div>',
         '<div class="ficha ancha"><h5>Dos formas de equivocarse</h5><ul class="semaforo">'
         '<li class="no"><b>No hay efecto, y digo que sí</b><span class="marca">✗ tipo I</span><span class="que">falso positivo: pasa un 5 % de las veces (α)</span></li>'
         '<li class="no"><b>Hay efecto, y digo «no hay pruebas»</b><span class="marca">✗ tipo II</span><span class="que">falso negativo: frecuente con muestras pequeñas</span></li>'
         '<li><b>Hay efecto, y lo detecto</b><span class="marca">✓ potencia</span><span class="que">se busca que sea al menos del 80 %</span></li>'
         '<li><b>No hay efecto, y no lo afirmo</b><span class="marca">✓ acierto</span><span class="que">«no significativo» no demuestra que no haya efecto</span></li>'
         '</ul><p class="ficha-pie">Con una diferencia real de media desviación, 12 alumnos por grupo la detectan solo 1 de cada 5 veces; 64, unas 4 de cada 5.</p></div>',
         '<div class="ficha ancha"><h5>Escalas de medida</h5><dl class="vocab">', "".join(f"<dt>{a}</dt><dd>{d}</dd>" for a, d in escalas), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Visión artificial: el recorrido completo ----------
VIS_DESC = ("Entrenamiento, una vez: fotos con etiqueta, preparar y aumentar, red base más cabeza, "
            "comparar con la etiqueta y ajustar los pesos, en bucle. Uso, con cada foto nueva: la misma "
            "preparación sin aumento, la red ya entrenada da una salida y una persona decide.")


def vision_h():
    p = "vh"
    b = texto(10, 18, "ENTRENAR · una vez, con fotos etiquetadas", "sv-zona", "start")
    xs = [10, 158, 306, 454, 602]
    filas1 = [("Fotos + etiquetas", "«coche», cajas…"), ("Preparar", "tamaño, 0–1, + aumento"),
              ("Red base + cabeza", "extrae rasgos → tarea"), ("Pérdida", "¿cuánto falla?"),
              ("Ajustar pesos", "retropropagación")]
    for i, (t, sub) in enumerate(filas1):
        cls = "sv-caja sv-caja-ml" if i == 2 else "sv-caja"
        b += caja(xs[i], 28, 128, 56, t, sub, cls)
        if i:
            b += linea(f"M{xs[i] - 18},56 H{xs[i] - 4}", p)
    b += linea("M666,88 V104 H400 V88", p, "vuelta") + texto(533, 118, "en bucle, por lotes y épocas", "sv-et")
    b += texto(10, 150, "USAR · con cada foto nueva", "sv-zona", "start")
    filas2 = [("Foto nueva", "nunca vista"), ("Preparar igual", "sin aumento"),
              ("Red entrenada", "pesos fijos"), ("Salida", "clases, cajas, máscaras"),
              ("Decidir", "una persona revisa")]
    for i, (t, sub) in enumerate(filas2):
        cls = "sv-caja sv-caja-ml" if i == 2 else ("sv-caja sv-caja-ok" if i == 4 else "sv-caja")
        b += caja(xs[i], 160, 128, 56, t, sub, cls)
        if i:
            b += linea(f"M{xs[i] - 18},188 H{xs[i] - 4}", p)
    b += linea("M340,88 V156", p, "tinta") + texto(332, 132, "los pesos aprendidos", "sv-et", "end")
    return svg(p, "0 0 740 226", "El recorrido de un sistema de visión", VIS_DESC, b, "sv-h")


def vision_v():
    p = "vv"
    b = texto(10, 16, "ENTRENAR · una vez", "sv-zona", "start")
    pasos1 = [("Fotos + etiquetas", "«coche», cajas…"), ("Preparar", "tamaño, 0–1, + aumento"),
              ("Red base + cabeza", "rasgos → tarea"), ("Pérdida", "¿cuánto falla?"), ("Ajustar pesos", "retropropagación")]
    y = 24
    for i, (t, sub) in enumerate(pasos1):
        b += caja(40, y, 200, 50, t, sub, "sv-caja sv-caja-ml" if i == 2 else "sv-caja")
        if i < 4:
            b += linea(f"M140,{y + 52} V{y + 62}", p)
        y += 64
    b += linea("M242,{0} H262 V{1} H244".format(24 + 4 * 64 + 25, 24 + 2 * 64 + 25), p, "vuelta") + texto(270, 24 + 3 * 64 + 30, "bucle", "sv-et", "start")
    y0 = 24 + 5 * 64 + 16
    b += texto(10, y0, "USAR · cada foto nueva", "sv-zona", "start")
    pasos2 = [("Foto nueva", "nunca vista"), ("Preparar igual", "sin aumento"), ("Red entrenada", "pesos fijos"),
              ("Salida", "clases, cajas, máscaras"), ("Decidir", "una persona revisa")]
    y = y0 + 8
    for i, (t, sub) in enumerate(pasos2):
        cls = "sv-caja sv-caja-ml" if i == 2 else ("sv-caja sv-caja-ok" if i == 4 else "sv-caja")
        b += caja(40, y, 200, 50, t, sub, cls)
        if i < 4:
            b += linea(f"M140,{y + 52} V{y + 62}", p)
        y += 64
    return svg(p, f"0 0 300 {y + 4}", "El recorrido de un sistema de visión", VIS_DESC, b, "sv-v")


def _rejilla_svg(nombre, matriz, titulo, desc):
    filas, cols = len(matriz), len(matriz[0])
    t = 20
    b = ""
    for f in range(filas):
        for c in range(cols):
            v = matriz[f][c]
            cls = "sv-barra" if v else "sv-llave"
            b += f'<rect x="{2 + c * t}" y="{2 + f * t}" width="{t - 2}" height="{t - 2}" rx="2" class="{cls}"/>'
            if v and nombre == "vi":
                b += texto(2 + c * t + (t - 2) / 2, 2 + f * t + 14, str(v), "sv-et", "middle")
    return svg(nombre, f"0 0 {cols * t + 4} {filas * t + 4}", titulo, desc, b, "sv-mini")


def hoja_vision():
    import numpy as np
    from scipy import ndimage
    sem = np.zeros((8, 12), dtype=int)
    sem[1:4, 1:5] = 1
    sem[4:7, 7:11] = 1
    inst, n = ndimage.label(sem)
    semantica = _rejilla_svg("vs", sem.tolist(), "Segmentación semántica",
                             "Rejilla de 8 por 12 píxeles: todos los píxeles de coche tienen la misma clase, sin distinguir cuántos coches hay.")
    instancias = _rejilla_svg("vi", inst.tolist(), "Segmentación de instancias",
                              f"La misma rejilla con cada coche numerado aparte: {n} coches, el 1 y el 2.")
    tareas = [("Clasificar", "una etiqueta para toda la foto: «hay un coche» (0,90)"),
              ("Detectar", "una caja, una clase y una puntuación por objeto"),
              ("Segmentación semántica", "una clase para cada píxel: «coche», «calzada», «cielo»"),
              ("Segmentación de instancias", "una máscara para cada objeto: coche 1, coche 2"),
              ("Postura", "puntos clave del cuerpo: hombros, codos, rodillas")]
    confundir = [("Aumento de datos", "girar, recortar, cambiar el brillo: solo al entrenar"),
                 ("Normalizar", "igual al entrenar y al usar, con los valores del entrenamiento"),
                 ("Entrenar", "cambia los pesos; necesita etiquetas"),
                 ("Usar (inferencia)", "los pesos no cambian; la foto nueva no enseña nada al modelo"),
                 ("Puntuación 0,90", "lo seguro que está el modelo, no la probabilidad de acertar"),
                 ("RGB o BGR", "OpenCV guarda los colores al revés que casi todas las demás librerías")]
    h = ['<section class="hoja" aria-labelledby="hoja-vis-t">',
         '<p class="hoja-titulo" id="hoja-vis-t">La visión artificial en una hoja</p>',
         '<p class="hoja-nota">De los píxeles a una decisión: qué pasa al entrenar, qué pasa al usar el modelo y qué tareas se pueden hacer con la misma red.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Entrenar una vez, usar muchas</h5>', vision_h(), vision_v(),
         '<p class="ficha-pie">Lo que pasa del entrenamiento al uso son los <b>pesos</b>. La preparación de las fotos tiene que ser la misma en los dos, salvo el aumento de datos.</p></div>',
         '<div class="ficha"><h5>Una red base, varias cabezas</h5><dl class="vocab">',
         "".join(f"<dt>{a}</dt><dd>{d}</dd>" for a, d in tareas),
         '</dl><p class="ficha-pie">La red base (<i>backbone</i>) saca los rasgos de la imagen; cada tarea solo cambia la última parte (la <b>cabeza</b>). YOLO tiene versiones para cajas, máscaras, clases y postura.</p></div>',
         f'<div class="ficha"><h5>¿Cuántos coches hay?</h5><div class="ramas"><figure>{semantica}<figcaption><b>Semántica</b>: 24 píxeles de «coche».</figcaption></figure>'
         f'<figure>{instancias}<figcaption><b>Instancias</b>: {n} coches, numerados 1 y 2, cada uno con su máscara.</figcaption></figure></div>'
         '<p class="ficha-pie">Con la semántica no se pueden contar los coches si se tocan; con instancias, sí.</p></div>',
         '<div class="ficha ancha"><h5>No confundir</h5><dl class="vocab">',
         "".join(f"<dt>{a}</dt><dd>{d}</dd>" for a, d in confundir), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- EDA: doce pasos en orden ----------
EDA_FASES = [("Arreglar", ["1 Mirar: tamaño y tipos", "2 Fechas a fecha", "3 Quitar repetidos", "4 Contar huecos", "5 Limpiar texto"]),
             ("Describir", ["6 Mínimo y máximo", "7 Distribución", "8 Atípicos: uno a uno"]),
             ("Comparar", ["9 Categorías y tamaños", "10 Grupos", "11 Relaciones", "12 Tendencia"])]
EDA_ORDEN = ["los repetidos, antes de contar huecos", "el texto limpio, antes de agrupar", "las fechas, antes de la tendencia"]
EDA_DESC = ("Doce pasos en tres fases. Arreglar: mirar, fechas, repetidos, huecos y texto. Describir: mínimo y máximo, "
            "distribución y atípicos. Comparar: categorías, grupos, relaciones y tendencia. El orden importa: "
            + "; ".join(EDA_ORDEN) + ".")


def eda_h():
    p = "eh"
    b = ""
    xs = [10, 262, 514]
    for k, (fase, pasos) in enumerate(EDA_FASES):
        x = xs[k]
        b += texto(x, 16, fase.upper(), "sv-zona", "start")
        for i, paso in enumerate(pasos):
            cls = "sv-caja sv-caja-ok" if (k, i) in [(0, 2), (0, 4), (0, 1)] else "sv-caja"
            b += caja(x, 26 + i * 42, 216, 34, paso, None, cls)
        if k < 2:
            b += linea(f"M{x + 220},{26 + 17} H{xs[k + 1] - 6}", p)
    b += texto(262, 186, "El orden importa:", "sv-zona", "start")
    for j, t in enumerate(EDA_ORDEN):
        b += texto(262, 204 + j * 16, f"• {t}", "sv-et", "start")
    return svg(p, "0 0 740 240", "Un EDA en doce pasos", EDA_DESC, b, "sv-h")


def eda_v():
    p = "ev"
    b = ""
    y = 4
    for k, (fase, pasos) in enumerate(EDA_FASES):
        b += texto(10, y + 12, fase.upper(), "sv-zona", "start")
        y += 20
        for i, paso in enumerate(pasos):
            cls = "sv-caja sv-caja-ok" if (k, i) in [(0, 2), (0, 4), (0, 1)] else "sv-caja"
            b += caja(20, y, 260, 32, paso, None, cls)
            y += 38
        y += 6
    b += texto(10, y + 12, "El orden importa:", "sv-zona", "start")
    y += 18
    for t in EDA_ORDEN:
        b += texto(10, y + 12, f"• {t}", "sv-et", "start")
        y += 18
    return svg(p, f"0 0 300 {y + 4}", "Un EDA en doce pasos", EDA_DESC, b, "sv-v")


def hoja_eda():
    sql_sucio = [("MIN(fecha) con fechas «dd-mm-aaaa»", "compara letra a letra: «02-02» sale antes que «30-01»"),
                 ("COUNT(*) − COUNT(valoracion)", "cuenta bien los huecos, pero también los de las filas repetidas"),
                 ("GROUP BY edificio", "«B» y «B » son dos grupos: seis edificios en vez de tres"),
                 ("strftime('%W', fecha)", "solo entiende «aaaa-mm-dd»: NULL en todas las filas, sin avisar")]
    raros = [("no", "✗ error", "espera de −4 min", "imposible: se quita y se dice cuántos"),
             ("medio", "⚠ real", "encargo de 60 €", "atípico pero cierto: se separa y se informa"),
             ("ok", "✓ normal", "bocadillo de 5,71 €", "fuera del bigote, pero un pedido corriente")]
    contar = [("Media o mediana", "con datos asimétricos, el pedido típico es la mediana"),
              ("Cada media, con su n", "una media de 3 pedidos no pesa como una de 300"),
              ("Huecos", "el % se calcula después de quitar repetidos"),
              ("Correlación", "dice que van juntas, no cuál causa cuál"),
              ("Semana incompleta", "la primera y la última pueden tener menos días: comparar por día")]
    h = ['<section class="hoja" aria-labelledby="hoja-eda-t">',
         '<p class="hoja-titulo" id="hoja-eda-t">Un EDA en una hoja</p>',
         '<p class="hoja-nota">Doce pasos antes de cualquier gráfico bonito. En verde, los que cambian el resultado de los demás si se hacen tarde.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Doce pasos, en este orden</h5>', eda_h(), eda_v(),
         '<p class="ficha-pie">Cuenta las filas antes y después de cada limpieza y apúntalo: es lo primero que preguntará quien lea el informe.</p></div>',
         '<div class="ficha"><h5>SQL sobre la tabla sin limpiar</h5><ul class="semaforo">',
         "".join(f'<li class="no"><code>{escape(a)}</code><span class="marca">✗</span><span class="que">{escape(d)}</span></li>' for a, d in sql_sucio),
         '</ul><p class="ficha-pie">La limpieza se repite en la consulta: <code>TRIM</code>, <code>UPPER</code>, fechas a formato ISO y <code>COUNT(DISTINCT id)</code>.</p></div>',
         '<div class="ficha"><h5>¿Atípico o error?</h5><ul class="semaforo">',
         "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in raros),
         '</ul><p class="ficha-pie">La regla del rango intercuartílico solo marca; la decisión es tuya, valor a valor.</p></div>',
         '<div class="ficha ancha"><h5>Qué contar al final</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in contar), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Agentes en producción ----------
PRO_BUCLE = ["Percibir", "Planificar", "Actuar", "Observar", "Revisar"]
PRO_SALIDAS = [("Objetivo cumplido", "y comprobado"), ("Límite de pasos", "p. ej., 10"),
               ("Presupuesto", "tokens, euros, tiempo"), ("Fallo repetido", "misma llamada dos veces"),
               ("Hace falta una persona", "acción con efectos o duda")]
PRO_DESC = ("Bucle del agente: percibir, planificar, actuar, observar y revisar, y vuelta a empezar. "
            "Cinco salidas escritas en el código: objetivo cumplido y comprobado, límite de pasos, presupuesto, "
            "fallo repetido y hace falta una persona.")


def produccion_h():
    p = "ph"
    b = texto(10, 16, "EL BUCLE", "sv-zona", "start")
    pos = [(190, 168), (50, 168), (10, 90), (120, 28), (230, 90)]   # Revisar a la derecha, junto a las salidas
    for (x, y), t in zip(pos, PRO_BUCLE):
        b += caja(x, y, 120, 34, t, None, "sv-caja sv-caja-ml" if t == "Revisar" else "sv-caja")
    b += linea("M240,45 C280,50 290,70 290,86", p)
    b += linea("M290,124 C290,150 280,165 270,168", p)
    b += linea("M190,185 H174", p)
    b += linea("M50,170 C40,150 70,130 70,128", p)
    b += linea("M70,90 C70,60 100,48 116,46", p)
    b += texto(400, 16, "CINCO SALIDAS, EN EL CÓDIGO", "sv-zona", "start")
    for i, (t, sub) in enumerate(PRO_SALIDAS):
        cls = "sv-caja sv-caja-ok" if i == 0 else "sv-caja"
        b += caja(400, 26 + i * 40, 330, 34, f"{t}: {sub}", None, cls)
    b += linea("M352,106 H394", p, "rojo")
    return svg(p, "0 0 740 228", "El bucle de un agente y sus cinco salidas", PRO_DESC, b, "sv-h")


def produccion_v():
    p = "pv"
    b = texto(10, 14, "EL BUCLE", "sv-zona", "start")
    y = 22
    for i, t in enumerate(PRO_BUCLE):
        b += caja(40, y, 180, 30, t, None, "sv-caja sv-caja-ml" if t == "Revisar" else "sv-caja")
        if i < 4:
            b += linea(f"M130,{y + 31} V{y + 38}", p)
        y += 40
    b += linea(f"M222,{y - 25} H250 V37 H224", p, "vuelta") + texto(256, 110, "repite", "sv-et", "start")
    y += 10
    b += texto(10, y, "CINCO SALIDAS", "sv-zona", "start")
    y += 8
    for i, (t, sub) in enumerate(PRO_SALIDAS):
        b += caja(10, y, 290, 42, t, sub, "sv-caja sv-caja-ok" if i == 0 else "sv-caja")
        y += 48
    return svg(p, f"0 0 310 {y + 2}", "El bucle de un agente y sus cinco salidas", PRO_DESC, b, "sv-v")


def enchufes_svg():
    p = "pe"
    b = caja(150, 36, 110, 40, "Agente", None, "sv-caja sv-caja-ml")
    b += caja(4, 10, 120, 34, "Calendario", None) + caja(4, 68, 120, 34, "Base de datos", None)
    b += caja(286, 10, 120, 34, "Agente B", None) + caja(286, 68, 120, 34, "Agente C", None)
    b += linea("M148,50 H128", p) + linea("M148,64 L128,82", p)
    b += linea("M262,50 H282", p) + linea("M262,64 L282,82", p)
    b += texto(64, 124, "MCP: herramientas y datos", "sv-et", "middle")
    b += texto(346, 124, "A2A: otros agentes", "sv-et", "middle")
    return svg(p, "0 0 410 132", "MCP y A2A", "El agente usa MCP para conectarse a herramientas y datos, como un calendario o una base de datos, y A2A para encargar tareas a otros agentes.", b)


def hoja_produccion():
    autonomia = [("ok", "✓ solo", "Leer datos, buscar, resumir", "sin efectos fuera: el agente lo hace y lo registra"),
                 ("medio", "⚠ en seco", "Preparar un borrador o un cambio", "lo propone; una persona o una prueba lo revisa"),
                 ("no", "✗ aprobación", "Enviar, pagar, borrar, publicar", "una persona dice «sí» antes, viendo qué y con qué datos")]
    memoria = [("De trabajo", "lo de esta tarea: objetivo, plan, últimos resultados"),
               ("Episódica", "qué pasó en tareas anteriores"),
               ("Semántica", "datos y preferencias que se mantienen"),
               ("Procedimental", "cómo se hacen las cosas: instrucciones versionadas")]
    confundir = [("Idempotente", "repetir la llamada no repite el efecto (clave por intención)"),
                 ("Coste", "crece más que los pasos: cada llamada relee todo lo anterior"),
                 ("«Ya está»", "lo dice el modelo; lo confirma una comprobación"),
                 ("Juicio del modelo", "no es una barrera de seguridad: los límites, en el código"),
                 ("Más agentes", "más coste, más espera y más formas de fallar: solo si se mide que ayudan")]
    h = ['<section class="hoja" aria-labelledby="hoja-pro-t">',
         '<p class="hoja-titulo" id="hoja-pro-t">Un agente que se pueda dejar trabajando</p>',
         '<p class="hoja-nota">El bucle es la parte fácil. Lo que hace fiable a un agente son sus salidas, sus permisos y lo que recuerda.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>El bucle y cuándo parar</h5>', produccion_h(), produccion_v(),
         '<p class="ficha-pie">La primera salida es la única buena, y solo si una comprobación objetiva (una prueba, un esquema, el dato real) lo confirma.</p></div>',
         '<div class="ficha"><h5>¿Cuánta autonomía?</h5><ul class="semaforo">',
         "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in autonomia),
         '</ul><p class="ficha-pie">La autonomía se decide acción por acción, no para todo el producto.</p></div>',
         '<div class="ficha"><h5>Cuatro memorias</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in memoria),
         '</dl><p class="ficha-pie">Solo se guarda lo comprobado, y la persona puede ver y borrar lo suyo.</p></div>',
         f'<div class="ficha"><h5>Dos enchufes</h5>{enchufes_svg()}<p class="ficha-pie">Un servidor MCP o un agente ajeno es código de terceros: solo de confianza y con los permisos justos.</p></div>',
         '<div class="ficha"><h5>No confundir</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in confundir), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Ciberseguridad ----------
CIB_TRES = [("Codificar", "Base64, UTF-8", "lo deshace cualquiera", "sv-caja"),
            ("Resumir (hash)", "SHA-256, scrypt", "no se puede deshacer", "sv-caja sv-caja-ml"),
            ("Cifrar", "AES, Fernet", "solo con la clave", "sv-caja sv-caja-ok")]
CIB_DESC = ("Un mismo mensaje se puede codificar, resumir o cifrar. Codificar, con Base64 o UTF-8, lo deshace cualquiera y no protege nada. "
            "Resumir, con SHA-256 o scrypt, no se puede deshacer y sirve para comprobar integridad y guardar contraseñas. "
            "Cifrar, con AES o Fernet, solo lo deshace quien tiene la clave y protege la confidencialidad.")


def ciber_h():
    p = "ch"
    b = caja(10, 76, 120, 40, "Mensaje", None, "sv-caja")
    for i, (t, ej, deshacer, cls) in enumerate(CIB_TRES):
        y = 10 + i * 64
        b += linea(f"M132,96 C160,96 160,{y + 22} 190,{y + 22}", p)
        b += caja(196, y, 200, 46, t, ej, cls)
        b += linea(f"M398,{y + 23} H426", p, punta=False, cls="sv-l-pen")
        b += texto(434, y + 28, deshacer, "sv-et", "start")
    return svg(p, "0 0 640 200", "Codificar, resumir y cifrar", CIB_DESC, b, "sv-h")


def ciber_v():
    p = "cv"
    b = caja(10, 6, 150, 34, "Mensaje", None, "sv-caja")
    y, medios = 56, []
    for t, ej, deshacer, cls in CIB_TRES:
        b += caja(50, y, 250, 46, t, ej, cls)
        b += texto(175, y + 62, deshacer, "sv-et", "middle")
        medios.append(y + 23)
        y += 82
    b += linea(f"M30,41 V{medios[-1]}", p, punta=False, cls="sv-l-pen")
    for m in medios:
        b += linea(f"M30,{m} H46", p)
    return svg(p, f"0 0 310 {y - 10}", "Codificar, resumir y cifrar", CIB_DESC, b, "sv-v")


def hoja_ciberseguridad():
    donde = [("ok", "✓ sí", "Lo mío", "mi equipo, mis archivos, una máquina virtual o una web montada en local"),
             ("medio", "⚠ con normas", "Plataformas de práctica y CTF", "solo contra lo que ofrecen y dentro de sus reglas"),
             ("no", "✗ no", "Lo ajeno sin permiso escrito", "red y web del centro, aula virtual, wifi de otros: delito (art. 197 bis CP)")]
    claves = [("no", "✗", "Texto plano o cifrado", "si roban la base de datos (o la clave), salen todas"),
              ("no", "✗", "MD5, SHA-1, SHA-256 a secas", "millones de intentos por segundo y sin sal"),
              ("ok", "✓", "Argon2id, scrypt, bcrypt", "lentos a propósito y con sal aleatoria de secrets")]
    confundir = [("Base64", "no es cifrado: se lee con una línea de Python"),
                 ("Sal", "no es secreta: se guarda junto al resumen; su trabajo es que dos claves iguales no se parezcan"),
                 ("MD5", "vale para ver si una copia salió mal, no para defenderse de nadie"),
                 ("OSINT", "que algo esté publicado no permite juntarlo en el perfil de una persona"),
                 ("Herramienta", "la misma sirve para defender o atacar: lo que cambia es el permiso")]
    sem = lambda filas: "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in filas)
    h = ['<section class="hoja" aria-labelledby="hoja-cib-t">',
         '<p class="hoja-titulo" id="hoja-cib-t">Ciberseguridad en una hoja</p>',
         '<p class="hoja-nota">Primero, dónde se puede practicar. Después, las tres operaciones que más se confunden y cómo guardar una contraseña.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha"><h5>¿Dónde puedo probar?</h5><ul class="semaforo">', sem(donde),
         '</ul><p class="ficha-pie">¿Problema de seguridad? INCIBE, en el 017, gratis y confidencial.</p></div>',
         '<div class="ficha"><h5>Guardar contraseñas</h5><ul class="semaforo">', sem(claves),
         '</ul><p class="ficha-pie">Comparar con <code>hmac.compare_digest</code>, nunca con <code>==</code>.</p></div>',
         '<div class="ficha ancha"><h5>Tres cosas distintas</h5>', ciber_h(), ciber_v(),
         '<p class="ficha-pie">Codificar no protege; resumir protege la integridad; cifrar, la confidencialidad.</p></div>',
         '<div class="ficha ancha"><h5>No confundir</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in confundir), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Aprendizaje automático: qué es ----------
ML_DESC = ("Programación tradicional: una persona escribe las reglas; el programa recibe datos y devuelve respuestas. "
           "Aprendizaje automático: se dan datos con sus respuestas, un algoritmo de aprendizaje obtiene el modelo, "
           "que hace de reglas, y el modelo da predicciones para datos nuevos.")


def ml_h():
    p = "mh"
    b = texto(10, 16, "PROGRAMACIÓN TRADICIONAL", "sv-zona", "start")
    b += caja(10, 26, 150, 34, "Datos", None) + caja(10, 70, 150, 34, "Reglas (persona)", None, "sv-caja sv-caja-ml")
    b += linea("M162,43 C185,43 185,62 204,62", p) + linea("M162,87 C185,87 185,66 204,66", p)
    b += caja(208, 46, 140, 36, "Programa", None) + linea("M350,64 H384", p)
    b += caja(388, 46, 150, 36, "Respuestas", None)
    b += texto(10, 140, "APRENDIZAJE AUTOMÁTICO", "sv-zona", "start")
    b += caja(10, 150, 150, 34, "Datos", None) + caja(10, 194, 150, 34, "Respuestas", None, "sv-caja sv-caja-ml")
    b += linea("M162,167 C185,167 185,186 204,186", p) + linea("M162,211 C185,211 185,190 204,190", p)
    b += caja(208, 170, 140, 36, "Aprendizaje", None) + linea("M350,188 H384", p)
    b += caja(388, 170, 150, 36, "Modelo («reglas»)", None, "sv-caja sv-caja-ok")
    b += linea("M463,208 V236", p) + caja(388, 240, 150, 40, "Predicción", "para datos nuevos")
    b += texto(560, 194, "se entrena una vez;", "sv-et", "start") + texto(560, 212, "después solo se usa", "sv-et", "start")
    return svg(p, "0 0 720 290", "Programación tradicional frente a aprendizaje automático", ML_DESC, b, "sv-h")


def ml_v():
    p = "mv"
    b = texto(10, 16, "TRADICIONAL", "sv-zona", "start")
    b += caja(10, 24, 140, 32, "Datos", None) + caja(160, 24, 140, 32, "Reglas (persona)", None, "sv-caja sv-caja-ml")
    b += linea("M80,58 V72", p) + linea("M230,58 V72", p)
    b += caja(10, 76, 290, 32, "Programa", None) + linea("M155,110 V122", p)
    b += caja(10, 126, 290, 32, "Respuestas", None)
    b += texto(10, 190, "APRENDIZAJE AUTOMÁTICO", "sv-zona", "start")
    b += caja(10, 198, 140, 32, "Datos", None) + caja(160, 198, 140, 32, "Respuestas", None, "sv-caja sv-caja-ml")
    b += linea("M80,232 V246", p) + linea("M230,232 V246", p)
    b += caja(10, 250, 290, 32, "Aprendizaje", None) + linea("M155,284 V296", p)
    b += caja(10, 300, 290, 32, "Modelo («reglas»)", None, "sv-caja sv-caja-ok") + linea("M155,334 V346", p)
    b += caja(10, 350, 290, 42, "Predicción", "para datos nuevos")
    return svg(p, "0 0 310 400", "Programación tradicional frente a aprendizaje automático", ML_DESC, b, "sv-v")


def hoja_ml():
    hace_falta = [("no", "✗ no", "Regla clara y fija", "IVA, nóminas, calculadora, horario: se programa y se comprueba"),
                  ("medio", "⚠ quizá", "Regla sencilla con pocos datos", "5 ejemplos de horas y aprobados: un umbral lo hace igual de bien"),
                  ("ok", "✓ sí", "Nadie sabe escribir la regla", "reconocer letras o voz, filtrar spam: muchos ejemplos y una medida de acierto")]
    formas = [("Supervisado", "cada ejemplo con su respuesta: precio, spam o no"),
              ("No supervisado", "sin respuestas: grupos, resumen, cosas raras"),
              ("Semisupervisado", "pocas respuestas y muchos datos sin ellas"),
              ("Autosupervisado", "la respuesta sale del propio dato: la palabra que falta (así se preentrenan los LLM)"),
              ("Por refuerzo", "prueba, recibe premios o castigos, mejora su estrategia")]
    confundir = [("Algoritmo y modelo", "la receta (regresión lineal) y lo que sale de aplicarla a unos datos (sus coeficientes)"),
                 ("«Aprende solo»", "aprende mientras se entrena; publicado, no cambia hasta que alguien lo reentrena"),
                 ("Acertar con lo visto", "no prueba nada: se mide con datos que el modelo no vio"),
                 ("IA, ML y DL", "el DL es parte del ML y el ML de la IA, pero hay IA que no aprende: búsqueda, reglas"),
                 ("Más datos", "ayudan si son buenos y representan bien a quien se va a usar el modelo")]
    sem = lambda filas: "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in filas)
    dl = lambda filas: "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in filas)
    h = ['<section class="hoja" aria-labelledby="hoja-ml-t">',
         '<p class="hoja-titulo" id="hoja-ml-t">El aprendizaje automático en una hoja</p>',
         '<p class="hoja-nota">Qué cambia frente a programar, cuándo merece la pena y cinco formas de aprender según qué datos haya.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Escribir las reglas o sacarlas de ejemplos</h5>', ml_h(), ml_v(),
         '<p class="ficha-pie">El modelo hace el papel de las reglas, pero nadie las ha escrito: hay que comprobar que funcionan con casos nuevos.</p></div>',
         '<div class="ficha"><h5>¿Hace falta aprendizaje automático?</h5><ul class="semaforo">', sem(hace_falta),
         '</ul><p class="ficha-pie">Primero la regla más sencilla; el modelo tiene que mejorarla con datos nuevos.</p></div>',
         '<div class="ficha"><h5>Cinco formas de aprender</h5><dl class="vocab">', dl(formas), '</dl></div>',
         '<div class="ficha ancha"><h5>No confundir</h5><dl class="vocab">', dl(confundir), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Evaluar bien: entrenamiento, validación y prueba ----------
EV_DESC = ("Los datos se separan primero en entrenamiento, validación y prueba. Con el de entrenamiento se ajustan la "
           "preparación (escalado, imputación) y el modelo. Con el de validación se eligen hiperparámetros y cuándo parar. "
           "La prueba se usa una sola vez, al final, con el modelo ya elegido.")


def ev_h():
    p = "eh2"
    b = caja(10, 82, 120, 46, "Datos", "filas + etiqueta")
    b += linea("M132,105 H156", p)
    b += caja(160, 82, 120, 46, "Separar", "antes de nada", "sv-caja sv-caja-ml")
    b += linea("M282,105 C300,105 300,34 318,34", p) + linea("M282,105 H318", p) + linea("M282,105 C300,105 300,176 318,176", p)
    b += caja(322, 10, 190, 48, "Entrenamiento · 60 %", "ajusta preparación y modelo")
    b += caja(322, 82, 190, 48, "Validación · 20 %", "elige ajustes y cuándo parar")
    b += caja(322, 152, 190, 48, "Prueba · 20 %", "no se toca hasta el final", "sv-caja sv-caja-ok")
    b += linea("M514,106 C540,106 540,170 566,172", p)
    b += linea("M514,176 H566", p)
    b += caja(570, 152, 150, 48, "Evaluación final", "una sola vez", "sv-caja sv-caja-ok")
    b += texto(552, 124, "modelo elegido", "sv-et", "start")
    return svg(p, "0 0 730 210", "Entrenamiento, validación y prueba", EV_DESC, b, "sv-h")


def ev_v():
    p = "ev2"
    b = caja(55, 6, 200, 40, "Datos", None)
    b += linea("M155,48 V60", p)
    b += caja(55, 64, 200, 40, "Separar antes de nada", None, "sv-caja sv-caja-ml")
    b += linea("M155,106 V118", p)
    y = 122
    for t, sub, cls in [("Entrenamiento · 60 %", "ajusta preparación y modelo", "sv-caja"),
                        ("Validación · 20 %", "elige ajustes y cuándo parar", "sv-caja"),
                        ("Prueba · 20 %", "no se toca hasta el final", "sv-caja sv-caja-ok")]:
        b += caja(10, y, 290, 46, t, sub, cls)
        y += 56
    b += linea(f"M155,{y - 8} V{y + 4}", p)
    b += caja(55, y + 8, 200, 46, "Evaluación final", "una sola vez", "sv-caja sv-caja-ok")
    return svg(p, f"0 0 310 {y + 62}", "Entrenamiento, validación y prueba", EV_DESC, b, "sv-v")


def hoja_evaluacion():
    fugas = [("no", "✗", "Escalar o rellenar huecos con todos los datos", "la media ya «ha visto» la prueba"),
             ("no", "✗", "Elegir el modelo mirando la prueba", "la prueba deja de medir datos nuevos"),
             ("no", "✗", "Mezclar al azar fechas pasadas y futuras", "se entrena con el futuro"),
             ("ok", "✓", "Pipeline ajustado solo con entrenamiento", "la prueba se transforma con lo aprendido")]
    medir = [("Línea base", "compara con un modelo que no mira los datos (la clase más frecuente)"),
             ("Exactitud", "engaña con clases desequilibradas: mira precisión, exhaustividad, F1"),
             ("Validación al 100 %", "es sospechosa: con pocos datos, la prueba suele salir peor"),
             ("Pocos datos", "mejor validación cruzada que una sola separación")]
    sem = "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in fugas)
    h = ['<section class="hoja" aria-labelledby="hoja-ev-t">',
         '<p class="hoja-titulo" id="hoja-ev-t">Evaluar bien, en una hoja</p>',
         '<p class="hoja-nota">Un modelo puede parecer muy bueno porque se ha evaluado mal. Tres conjuntos, tres trabajos, y las fugas más frecuentes.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Tres conjuntos, tres trabajos</h5>', ev_h(), ev_v(),
         '<p class="ficha-pie">Los porcentajes son orientativos. Con <code>validation_split</code> o con validación cruzada, la validación sale del propio entrenamiento.</p></div>',
         '<div class="ficha"><h5>¿Hay fuga de datos?</h5><ul class="semaforo">', sem, '</ul></div>',
         '<div class="ficha"><h5>Antes de fiarte del número</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in medir), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Un agente por dentro ----------
AD_DESC = ("El orquestador recibe el objetivo y dirige el bucle. Construye el contexto (estado, memoria y documentos de RAG) "
           "y se lo da al LLM, que propone el siguiente paso en JSON. Antes de ejecutar, se valida el esquema y los permisos; "
           "después se ejecuta la herramienta y su observación vuelve al orquestador, que actualiza el estado y decide si seguir.")


def ad_h():
    p = "adh"
    b = caja(10, 100, 120, 46, "Objetivo", "y límites")
    b += linea("M132,123 H176", p)
    b += caja(180, 100, 150, 46, "Orquestador", "bucle, estado, paradas", "sv-caja sv-caja-ml")
    b += caja(180, 10, 150, 46, "LLM", "propone el paso")
    b += linea("M228,98 V60", p) + linea("M282,58 V96", p)
    b += texto(222, 82, "contexto", "sv-et", "end") + texto(288, 82, "JSON", "sv-et", "start")
    b += caja(180, 196, 150, 46, "Contexto", "estado, memoria, RAG")
    b += linea("M255,148 V192", p)
    b += linea("M332,123 H376", p)
    b += caja(380, 100, 140, 46, "Validar", "esquema y permisos", "sv-caja sv-caja-ok")
    b += linea("M522,123 H566", p)
    b += caja(570, 100, 150, 46, "Herramienta", "API, datos, código")
    b += linea("M645,148 V176 H310 V152", p, cls="sv-l-vuelta")
    b += texto(480, 192, "observación (resultado o error)", "sv-et", "middle")
    return svg(p, "0 0 730 250", "Un agente por dentro", AD_DESC, b, "sv-h")


def ad_v():
    p = "adv"
    b = caja(100, 6, 150, 36, "Objetivo", None)
    b += linea("M175,44 V56", p)
    b += caja(75, 60, 200, 44, "Orquestador", "bucle, estado, paradas", "sv-caja sv-caja-ml")
    b += linea("M140,106 V124", p) + linea("M210,124 V108", p)
    b += caja(34, 128, 144, 44, "Contexto", "estado, memoria, RAG")
    b += caja(184, 128, 136, 44, "LLM", "propone en JSON")
    b += linea("M252,174 V190", p)
    b += caja(75, 194, 200, 44, "Validar", "esquema y permisos", "sv-caja sv-caja-ok")
    b += linea("M175,240 V252", p)
    b += caja(75, 256, 200, 44, "Herramienta", "API, datos, código")
    b += linea("M73,278 H18 V82 H71", p, cls="sv-l-vuelta")
    b += texto(10, 200, "observación", "sv-et", "middle").replace("<text", '<text transform="rotate(-90 10 200)"', 1)
    return svg(p, "0 0 330 310", "Un agente por dentro", AD_DESC, b, "sv-v")


def hoja_agentedentro():
    decide = [("ok", "✓", "Proponer la herramienta y sus argumentos", "es su trabajo: sale en JSON"),
              ("medio", "⚠", "Los argumentos", "se validan contra el esquema antes de usarlos"),
              ("no", "✗", "Permisos, borrar, pagar, enviar", "lo decide el programa, y una persona si no se puede deshacer"),
              ("no", "✗", "Cuándo parar del todo", "límites de pasos, tiempo y coste fijados en el código")]
    confundir = [("Contexto", "lo que el modelo ve en este paso; se rehace cada vez"),
                 ("Estado", "el registro de la tarea: objetivo, pasos hechos, resultados; dura toda la tarea"),
                 ("Memoria", "lo que se guarda entre conversaciones: preferencias, casos pasados"),
                 ("RAG", "documentos externos que se buscan para responder; no son recuerdos del agente"),
                 ("«Aprende»", "recordar no es aprender: los pesos del modelo no cambian")]
    tipos = [("Reactivo", "regla con lo que percibe ahora: el termostato"),
             ("Reactivo con modelo", "recuerda algo del mundo: qué casillas ya limpió"),
             ("Por objetivos", "busca cualquier camino que llegue a la meta"),
             ("Por utilidad", "compara caminos con una puntuación: tiempo, coste, riesgo"),
             ("Que aprende", "mejora con la experiencia cambiando su modelo")]
    sem = "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in decide)
    dl = lambda f: "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in f)
    h = ['<section class="hoja" aria-labelledby="hoja-ad-t">',
         '<p class="hoja-titulo" id="hoja-ad-t">Un agente por dentro</p>',
         '<p class="hoja-nota">Quién hace qué en cada vuelta del bucle, qué decide el modelo y qué no, y cuatro palabras que se confunden.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Una vuelta del bucle</h5>', ad_h(), ad_v(),
         '<p class="ficha-pie">El modelo propone; el programa valida, ejecuta y decide cuándo parar.</p></div>',
         '<div class="ficha"><h5>¿Lo decide el modelo?</h5><ul class="semaforo">', sem, '</ul></div>',
         '<div class="ficha"><h5>Tipos clásicos de agente</h5><dl class="vocab">', dl(tipos), '</dl></div>',
         '<div class="ficha ancha"><h5>No confundir</h5><dl class="vocab">', dl(confundir), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Tres perfiles: agentes, IA generativa y ciencia de datos ----------
RUTAS = [
    ("Ingeniería de agentes", "Que la IA actúe: usa herramientas, decide pasos y se controla", [
        ("Python", "teoria.html#11-qué-es-un-programa", "ok"),
        ("Cómo funciona un LLM", "teoria.html#148-ia-generativa-y-modelos-de-lenguaje-llm", "ok"),
        ("Instrucciones (prompting)", "ud4-lenguaje.html#8-modelos-de-lenguaje", "ok"),
        ("Llamada a herramientas", "teoria.html#la-llamada-a-herramientas-por-dentro-y-la-ingeniería-del-contexto", "ok"),
        ("Un marco: LangChain, LangGraph…", "teoria.html#patrones-de-agentes-planificar-repartir-el-trabajo-y-revisar", "medio"),
        ("RAG y bases vectoriales", "teoria.html#rag-mejorado-trozos-con-solapamiento-reordenación-y-bases-vectoriales", "ok"),
        ("Varios agentes", "teoria.html#patrones-de-agentes-planificar-repartir-el-trabajo-y-revisar", "ok"),
        ("Una API (FastAPI, Flask)", "teoria.html#http-y-api-rest", "ok"),
        ("Docker", "teoria.html#docker-y-github-actions-el-mínimo-que-funciona", "medio"),
        ("Evaluar y vigilar el agente", "teoria.html#fiabilidad-de-un-agente-reintentos-alternativas-y-evaluar-el-recorrido", "ok"),
        ("Publicarlo", "teoria.html#un-agente-que-se-pueda-dejar-trabajando-cuándo-parar-memoria-herramientas-y-fallos-típicos", "medio")]),
    ("Ingeniería de IA generativa", "Construir con modelos que generan texto o imágenes, y adaptarlos", [
        ("Python", "teoria.html#11-qué-es-un-programa", "ok"),
        ("Cómo funciona un LLM", "ud4-lenguaje.html#1010-el-transformer-por-dentro", "ok"),
        ("Instrucciones (prompting)", "ud4-lenguaje.html#8-modelos-de-lenguaje", "ok"),
        ("Embeddings", "ud4-lenguaje.html#4-del-texto-al-vector", "ok"),
        ("Bases vectoriales y RAG", "teoria.html#rag-paso-a-paso", "ok"),
        ("PyTorch", "teoria.html#pytorch-paso-a-paso-de-los-tensores-a-guardar-el-modelo", "medio"),
        ("Hugging Face y Transformers", "ud4-lenguaje.html#109-transformers-bert-y-gpt", "medio"),
        ("Ajuste fino (LoRA, PEFT)", "ud4-lenguaje.html#1010-el-transformer-por-dentro", "medio"),
        ("Evaluar un LLM", "teoria.html#evaluar-una-aplicación-con-llm", "ok"),
        ("Una API y Docker", "teoria.html#docker-y-github-actions-el-mínimo-que-funciona", "medio"),
        ("Publicar en la nube", "teoria.html#137-del-notebook-a-la-app-desplegar-un-modelo", "medio")]),
    ("Ciencia de datos", "Sacar conclusiones de los datos y predecir con modelos", [
        ("Python", "teoria.html#11-qué-es-un-programa", "ok"),
        ("NumPy", "teoria.html#71-numpy-computación-numérica", "ok"),
        ("Pandas", "teoria.html#73-pandas-a-fondo", "ok"),
        ("SQL", "datos.html#24-resumir-con-sql-cte-case-y-funciones-de-ventana", "ok"),
        ("Limpieza y análisis exploratorio", "datos.html#25-un-eda-completo-en-orden-python-y-sql-a-la-vez", "ok"),
        ("Estadística y probabilidad", "teoria.html#610-probabilidad-y-distribuciones-frecuentes", "ok"),
        ("Gráficos: Matplotlib y Seaborn", "datos.html#22-elegir-el-gráfico-por-la-pregunta", "ok"),
        ("Preparar variables", "datos.html#32-transformar-agrupar-codificar-y-escalar", "ok"),
        ("scikit-learn y sus algoritmos", "algoritmos.html", "ok"),
        ("Entrenar, evaluar y ajustar", "ud5-ml.html#6-sobreajuste-validación-cruzada-e-hiperparámetros", "ok"),
        ("Publicar el modelo", "teoria.html#137-del-notebook-a-la-app-desplegar-un-modelo", "ok")]),
]


def hoja_rutas():
    marca = {"ok": ("✓", "explicado en la web"), "medio": ("en parte", "explicado en parte")}
    fichas = []
    for titulo, que, pasos in RUTAS:
        items = "".join(
            f'<li class="{c}"><a href="{escape(u)}">{escape(t)}</a>'
            f'<span class="marca" title="{marca[c][1]}" aria-label="{marca[c][1]}">{marca[c][0]}</span></li>'
            for t, u, c in pasos)
        fichas.append(f'<div class="ficha"><h5>{escape(titulo)}</h5><p class="ficha-pie">{escape(que)}</p>'
                      f'<ol class="pasos">{items}</ol></div>')
    comun = [("Git y GitHub", "los tres guardan y comparten su trabajo con Git"),
             ("Pruebas", "comprobar con código que todo sigue funcionando"),
             ("Matemáticas", "álgebra, probabilidad y cálculo, por debajo de todo (14.21)"),
             ("Ética y datos", "privacidad, sesgos y el Reglamento de IA")]
    h = ['<section class="hoja" aria-labelledby="hoja-rut-t">',
         '<p class="hoja-titulo" id="hoja-rut-t">Tres perfiles, tres caminos</p>',
         '<p class="hoja-nota">Un orden posible para cada perfil. Cada paso enlaza a donde se explica en esta web: ✓ explicado; «en parte» y número hueco, solo en parte.</p>',
         '<div class="hoja-grid tres">', *fichas,
         '<div class="ficha ancha"><h5>Lo que necesitan los tres, aunque no salga en las infografías</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in comun), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Resolver problemas ----------
def res_flujo():
    p = "rsf"
    pasos = [("1 Entender", "qué entra, qué sale, límites"), ("2 Ejemplos a mano", "también vacío, uno, repetidos"),
             ("3 Fuerza bruta", "correcta aunque sea lenta"), ("4 ¿Qué se repite?", "ahí está la mejora"),
             ("5 Estructura y técnica", "diccionario, ventana, montículo…")]
    b = ""
    for i, (t, sub) in enumerate(pasos):
        y = 4 + i * 56
        cls = "sv-caja sv-caja-ok" if i == 2 else ("sv-caja sv-caja-ml" if i == 4 else "sv-caja")
        b += caja(40, y, 200, 40, t, sub, cls)
        if i < 4:
            b += linea(f"M140,{y + 41} V{y + 54}", p)
    b += caja(40, 284, 200, 40, "6 Probar", "comparar con la fuerza bruta", "sv-caja")
    b += linea("M140,269 V282", p)
    b += linea("M242,304 C292,304 292,136 244,136", p, cls="sv-l-vuelta")
    b += texto(272, 224, "oráculo", "sv-sub", "middle")
    desc = ("Seis pasos: entender el problema, hacer ejemplos a mano, escribir la fuerza bruta, buscar qué trabajo se repite, "
            "elegir estructura y técnica, y probar la versión rápida comparándola con la fuerza bruta, que sirve de oráculo.")
    return svg(p, "0 0 300 330", "Cómo atacar un problema", desc, b, "sv-tab")


def hoja_resolver():
    def seg(pasos):
        t = pasos / 1e7
        if t < 1:
            return f"{t:.1f} s".replace(".", ",")
        return f"{t:.0f} s" if t < 90 else f"{t / 60:.0f} min"
    import math
    casos = [("O(n)", "n = 10⁶", 1e6), ("O(n log n)", "n = 10⁶", 1e6 * math.log2(1e6)),
             ("O(n²)", "n = 3000", 9e6), ("O(n²)", "n = 10⁵", 1e10), ("O(2ⁿ)", "n = 30", 2 ** 30)]
    def marca(pasos):
        t = pasos / 1e7
        return ("ok", "✓") if t < 1 else (("medio", "⚠") if t < 60 else ("no", "✗"))
    sem = "".join(f'<li class="{marca(x)[0]}"><b>{escape(o)} con {escape(n)}</b><span class="marca">{marca(x)[1]}</span>'
                  f'<span class="que">unos {escape(seg(x))} en Python puro</span></li>' for o, n, x in casos)
    pistas = [("¿Ya lo he visto?", "diccionario o conjunto"), ("Lista ordenada", "búsqueda binaria, dos punteros"),
              ("Sumas de tramos", "sumas acumuladas, ventana"), ("Los k mejores", "montículo (heapq)"),
              ("Qué va antes", "orden topológico (graphlib)"), ("¿Están conectados?", "Union-Find, BFS"),
              ("Subproblemas repetidos", "programación dinámica, @cache")]
    h = ['<section class="hoja" aria-labelledby="hoja-res-t">',
         '<p class="hoja-titulo" id="hoja-res-t">Resolver problemas en una hoja</p>',
         '<p class="hoja-nota">Un método, una cuenta rápida de tiempos y las pistas que llevan a cada técnica.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha"><h5>Cómo atacar un problema</h5>', res_flujo(),
         '<p class="ficha-pie">La fuerza bruta no se tira: comprueba la versión rápida.</p></div>',
         '<div class="ficha"><h5>¿Cabe en un segundo?</h5><ul class="semaforo">', sem, '</ul>',
         '<p class="ficha-pie">Cuenta: unos 10⁷ pasos sencillos por segundo en un bucle de Python. Lo que va en C es mucho más rápido: <code>sorted()</code> ordena 10⁶ datos en 0,26 s.</p></div>',
         '<div class="ficha ancha"><h5>Si el problema dice… piensa en…</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in pistas), '</dl></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Un script de automatización seguro ----------
def scr_flujo():
    p = "scf"
    b = caja(60, 4, 180, 38, "1 Leer argumentos", "argparse: si faltan, código 2")
    b += linea("M150,44 V58", p)
    b += caja(60, 60, 180, 38, "2 Leer configuración", "si falta algo, parar: código 1")
    b += linea("M150,100 V114", p)
    b += caja(60, 116, 180, 38, "3 Planificar", "decidir sin tocar nada", "sv-caja sv-caja-ok")
    b += linea("M150,156 V170", p)
    b += caja(60, 172, 180, 38, "4 Comprobar el plan", "¿conflictos? no se hace nada")
    b += linea("M120,212 C120,226 70,226 70,238", p) + linea("M180,212 C180,226 230,226 230,238", p)
    b += caja(8, 242, 124, 38, "Mostrar el plan", "sin --aplicar", "sv-caja sv-caja-ok")
    b += caja(168, 242, 124, 38, "Hacer los cambios", "con --aplicar", "sv-caja sv-caja-ml")
    b += linea("M70,282 C70,296 130,296 140,304", p) + linea("M230,282 C230,296 170,296 160,304", p)
    b += caja(60, 306, 180, 30, "5 Código de salida: 0", None)
    desc = ("Un script seguro lee los argumentos (si faltan, termina con código 2), lee la configuración (si falta algo, "
            "termina con código 1), planifica sin tocar nada y comprueba el plan. Sin --aplicar solo muestra el plan; "
            "con --aplicar hace los cambios. Si todo va bien, termina con código 0.")
    return svg(p, "0 0 300 340", "El recorrido de un script seguro", desc, b, "sv-tab")


def hoja_script():
    codigos = [("0", "todo bien: la integración continua sigue"),
               ("1", "error: faltaba algo, un conflicto, un fallo al trabajar"),
               ("2", "uso incorrecto: argumentos que faltan o no valen (argparse)"),
               ("echo $?", "en la terminal, el código del último programa")]
    git = [("ok", "✓", "requirements.txt y .env.example", "sí se suben: dicen qué hace falta"),
           ("no", "✗", ".env", "nunca: lleva las claves de verdad"),
           ("no", "✗", ".venv/", "nunca: se rehace con pip install -r")]
    errores = [("no", "✗", "Cambiar primero y mirar después", "planificar, comprobar y luego actuar"),
               ("no", "✗", "Imprimir la clave para comprobarla", "mejor su longitud, o «cargada»"),
               ("medio", "⚠", "import logging y nada más", "sin basicConfig no se ven los INFO"),
               ("medio", "⚠", "pip install sin versiones", "mañana se instala otra versión"),
               ("ok", "✓", "La prueba como lo normal", "--aplicar para el cambio real")]
    li = lambda xs: "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in xs)
    h = ['<section class="hoja" aria-labelledby="hoja-scr-t">',
         '<p class="hoja-titulo" id="hoja-scr-t">Un script que no rompe nada</p>',
         '<p class="hoja-nota">Cinco pasos, tres códigos de salida y qué se sube a GitHub.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha"><h5>El recorrido</h5>', scr_flujo(),
         '<p class="ficha-pie">Si algo falla antes del paso 5, no se ha cambiado nada.</p></div>',
         '<div class="ficha"><h5>Códigos de salida</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in codigos), '</dl>',
         '<h5>¿Se sube a GitHub?</h5><ul class="semaforo">', li(git), '</ul></div>',
         '<div class="ficha ancha"><h5>Errores frecuentes</h5><ul class="semaforo">', li(errores), '</ul></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Llamar a herramientas ----------
def her_protocolo():
    p = "hep"
    A, B = 62, 238
    b = caja(12, 6, 100, 30, "Tu programa", None) + caja(188, 6, 100, 30, "Modelo", None)
    b += linea(f"M{A},38 V292", p, punta=False, cls="sv-l-tenue") + linea(f"M{B},38 V292", p, punta=False, cls="sv-l-tenue")
    pasos = [(60, A, B, "pen", "1 mensajes + herramientas", None),
             (106, B, A, "ml", "2 tool_use 01 y 02", "stop_reason: tool_use"),
             (204, A, B, "pen", "4 UN mensaje: result 01, 02", "el que falla, con is_error"),
             (262, B, A, "ml", "5 respuesta final", "max_tokens = cortada")]
    for y, x0, x1, color, et, sub in pasos:
        b += linea(f"M{x0},{y} H{x1 + (-6 if x1 > x0 else 6)}", p, color=color)
        b += texto(150, y - 7, et, "sv-et", "middle")
        if sub:
            b += texto(150, y + 16, sub, "sv-sub", "middle")
    b += caja(14, 138, 96, 44, "3 ejecuta", "cada petición", "sv-caja sv-caja-ok")
    desc = ("Tu programa envía los mensajes y las herramientas. El modelo se para y pide dos herramientas, cada una con su id. "
            "Tu programa las ejecuta y contesta con un solo mensaje que lleva los dos resultados; el que falla va marcado con is_error. "
            "El modelo da la respuesta final; si se para por max_tokens, la respuesta está cortada.")
    return svg(p, "0 0 300 300", "El protocolo de la llamada a herramientas", desc, b, "sv-tab")


def her_triada():
    p = "het"
    b = caja(90, 6, 120, 44, "Datos privados", "notas, correo")
    b += caja(4, 140, 128, 44, "Texto de fuera", "webs, correos")
    b += caja(168, 140, 128, 44, "Enviar fuera", "correo, URL")
    b += linea("M120,52 L72,138", p, punta=False, cls="sv-l-rojo")
    b += linea("M180,52 L228,138", p, punta=False, cls="sv-l-rojo")
    b += linea("M134,162 H166", p, punta=False, cls="sv-l-rojo")
    b += texto(150, 104, "las tres juntas:", "sv-et", "middle")
    b += texto(150, 120, "fuga de datos", "sv-et-no", "middle")
    b += texto(150, 208, "Defensa: quitar una de las tres", "sv-et", "middle")
    desc = ("Un agente con acceso a datos privados, contacto con texto de fuera y una forma de enviar hacia fuera puede "
            "filtrar datos. La defensa es quitarle una de las tres cosas.")
    return svg(p, "0 0 300 216", "La tríada letal", desc, b, "sv-tab")


def her_passk():
    p = "hek"
    b = ""
    datos = [(1, 0.9, 0.9), (3, 0.999, 0.729), (8, 1.0, 0.43)]
    for i, (k, arroba, todas) in enumerate(datos):
        x = 30 + i * 92
        for j, (v, cls) in enumerate([(arroba, "sv-barra"), (todas, "sv-barra-mala")]):
            h = round(v * 110)
            b += f'<rect x="{x + j * 30}" y="{130 - h}" width="26" height="{h}" rx="3" class="{cls}"/>'
            b += texto(x + j * 30 + 13, 124 - h, f"{v:.2f}".replace(".", ","), "sv-et", "middle")
        b += texto(x + 28, 148, f"k = {k}", "sv-et", "middle")
    b += f'<rect x="20" y="162" width="12" height="12" rx="2" class="sv-barra"/>' + texto(38, 172, "pass@k: alguno bien", "sv-et", "start")
    b += f'<rect x="168" y="162" width="12" height="12" rx="2" class="sv-barra-mala"/>' + texto(186, 172, "pass^k: todos bien", "sv-et", "start")
    desc = ("Un agente que acierta el 90 % de las veces. Con 1 intento, las dos medidas valen 0,90. Con 3, pass@k vale 1,00 "
            "y pass^k 0,73. Con 8, pass@k vale 1,00 y pass^k solo 0,43.")
    return svg(p, "0 0 300 182", "pass@k frente a pass^k", desc, b, "sv-tab")


def hoja_herramientas():
    ctx = [("Limpiar", "los resultados viejos pasan a ser una nota corta"),
           ("Compactar", "cerca del límite, resumir y seguir desde el resumen"),
           ("Notas", "el agente apunta su avance en un archivo"),
           ("Aislar", "un subagente busca en su propio contexto y devuelve un resumen"),
           ("Justo a tiempo", "rutas y nombres al principio; el detalle, cuando haga falta (Agent Skills)")]
    errores = [("no", "✗", "Atender solo el primer tool_use", "cada petición necesita su resultado: si no, error 400"),
               ("no", "✗", "Dar por terminada una respuesta con max_tokens", "está cortada"),
               ("medio", "⚠", "Devolver el error como texto normal", "mejor con is_error, para que cambie de plan"),
               ("medio", "⚠", "Más contexto, mejor respuesta", "el contexto largo se «pudre»"),
               ("ok", "✓", "Romper una pata de la tríada", "más seguro que cualquier filtro")]
    sem = "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in errores)
    h = ['<section class="hoja" aria-labelledby="hoja-her-t">',
         '<p class="hoja-titulo" id="hoja-her-t">Llamar a herramientas sin romper nada</p>',
         '<p class="hoja-nota">El protocolo, el contexto, la seguridad y cómo medir si el agente es fiable.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha"><h5>El protocolo</h5>', her_protocolo(),
         '<p class="ficha-pie">El modelo solo pide; ejecuta tu programa.</p></div>',
         '<div class="ficha"><h5>La tríada letal</h5>', her_triada(),
         '<p class="ficha-pie">Una búsqueda web ya envía datos: van en la dirección.</p></div>',
         '<div class="ficha ancha"><h5>Ingeniería del contexto</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in ctx), '</dl></div>',
         '<div class="ficha"><h5>¿Fiable o a veces acierta?</h5>', her_passk(),
         '<p class="ficha-pie">Agente que acierta 9 de cada 10 veces.</p></div>',
         '<div class="ficha"><h5>Errores frecuentes</h5><ul class="semaforo">', sem, '</ul></div>',
         '</div></section>']
    return "\n".join(h)


# ---------- Matemáticas de la IA ----------
def mat_autovectores():
    p = "mae"
    o = (150, 150)
    esc = 40
    def pt(x, y):
        return o[0] + x * esc, o[1] - y * esc
    b = linea(f"M{o[0]-130},{o[1]} H{o[0]+130}", p, punta=False, cls="sv-llave")
    b += linea(f"M{o[0]},{o[1]+70} V{o[1]-140}", p, punta=False, cls="sv-llave")
    for (x0, y0), (x1, y1), color, et, pos in [((1, 1), (3, 3), "pen", "×3", (3.05, 3.2)),
                                             ((1, -1), (1, -1), "ml", "×1", (1.15, -1.25)),
                                             ((1, 0), (2, 1), "rojo", "gira", (2.1, 0.75))]:
        ax, ay = pt(x0, y0)
        bx, by = pt(x1, y1)
        b += f'<circle cx="{ax}" cy="{ay}" r="5" class="sv-llave"/>'
        b += linea(f"M{o[0]},{o[1]} L{bx},{by}", p, color=color)
        tx, ty = pt(*pos)
        b += texto(tx, ty, et, "sv-et", "start")
    b += texto(150, 245, "○ vector antes; flecha: después de aplicar M", "sv-et", "middle")
    desc = ("La matriz M estira la dirección (1, 1) tres veces y deja igual la dirección (1, −1): son sus autovectores, "
            "con autovalores 3 y 1. La dirección (1, 0) pasa a (2, 1): cambia de dirección, así que no es autovector.")
    return svg(p, "0 0 300 255", "Autovectores", desc, b, "sv-tab")


def mat_bayes():
    p = "mab"
    b = caja(90, 6, 120, 36, "1000 personas", None)
    b += linea("M120,44 C120,60 60,60 60,74", p) + linea("M180,44 C180,60 240,60 240,74", p)
    b += caja(10, 78, 100, 44, "10 enfermas", "1 %")
    b += caja(190, 78, 100, 44, "990 sanas", "99 %")
    b += linea("M60,124 V146", p) + linea("M240,124 V146", p)
    b += caja(10, 150, 100, 44, "≈ 10 positivos", "99 % de 10", "sv-caja sv-caja-ok")
    b += caja(190, 150, 100, 44, "≈ 50 positivos", "5 % de 990: falsos", "sv-caja sv-caja-ml")
    b += texto(150, 222, "De 60 positivos, solo 10 enfermos:", "sv-et", "middle")
    b += texto(150, 240, "P(enfermo | positivo) ≈ 1 de 6 (0,17)", "sv-et", "middle")
    desc = ("De 1000 personas, 10 están enfermas y 990 sanas. Casi las 10 enfermas dan positivo, pero también "
            "unas 50 sanas (el 5 %). De unos 60 positivos, solo 10 están enfermos: alrededor de 1 de cada 6.")
    return svg(p, "0 0 300 250", "Bayes con 1000 personas", desc, b, "sv-tab")


def hoja_matematicas():
    mapa = [("Álgebra lineal", "datos como matrices, capas X·W + b, embeddings y coseno, PCA y SVD"),
            ("Cálculo", "derivadas y gradiente para entrenar; regla de la cadena = retropropagación"),
            ("Probabilidad", "salidas como probabilidades, Bayes, Naive Bayes, incertidumbre"),
            ("Estadística", "describir datos, evaluar modelos, intervalos, pruebas A/B"),
            ("Información", "entropía en los árboles, entropía cruzada como pérdida, KL, selección de variables")]
    errores = [("no", "✗", "Divergencia KL como distancia", "no es simétrica: D(p‖q) ≠ D(q‖p)"),
               ("no", "✗", "Positivo en una prueba = enfermo", "depende de lo frecuente que sea (tasa base)"),
               ("medio", "⚠", "Curtosis de la normal", "3, o 0 si es «en exceso» (SciPy, Pandas)"),
               ("medio", "⚠", "Con n ≥ 30, prueba z", "sin la desviación de la población, siempre t"),
               ("ok", "✓", "Comprobar una cuenta con código", "dos chuletas de estas traen ejemplos mal calculados")]
    sem = "".join(f'<li class="{c}"><b>{escape(o)}</b><span class="marca">{m}</span><span class="que">{escape(q)}</span></li>' for c, m, o, q in errores)
    h = ['<section class="hoja" aria-labelledby="hoja-mat-t">',
         '<p class="hoja-titulo" id="hoja-mat-t">Las matemáticas de la IA, en una hoja</p>',
         '<p class="hoja-nota">Cinco ramas, para qué sirve cada una y dos ideas que se entienden mejor dibujadas.</p>',
         '<div class="hoja-grid">',
         '<div class="ficha ancha"><h5>Qué matemática hay detrás de qué</h5><dl class="vocab">',
         "".join(f"<dt>{escape(a)}</dt><dd>{escape(d)}</dd>" for a, d in mapa), '</dl></div>',
         '<div class="ficha"><h5>Autovectores: direcciones que no giran</h5>', mat_autovectores(),
         '<p class="ficha-pie">PCA busca estas direcciones en la matriz de covarianza de los datos.</p></div>',
         '<div class="ficha"><h5>Bayes con 1000 personas</h5>', mat_bayes(),
         '<p class="ficha-pie">Prueba con 99 % de aciertos en enfermos y 5 % de falsos positivos; enfermedad del 1 %.</p></div>',
         '<div class="ficha ancha"><h5>Errores frecuentes</h5><ul class="semaforo">', sem, '</ul></div>',
         '</div></section>']
    return "\n".join(h)


def insertar(texto_md, nombre, bloque):
    a, z = f"<!-- hoja:{nombre} -->", f"<!-- /hoja:{nombre} -->"
    assert texto_md.count(a) == 1 and texto_md.count(z) == 1, nombre
    assert "\n\n" not in bloque, "sin líneas en blanco dentro del bloque (gfm)"
    i, j = texto_md.index(a) + len(a), texto_md.index(z)
    return texto_md[:i] + "\n" + bloque + "\n" + texto_md[j:]


if __name__ == "__main__":
    t = TEORIA.read_text(encoding="utf-8")
    t = insertar(t, "git", hoja_git())
    t = insertar(t, "agentes", hoja_agentes())
    t = insertar(t, "pandas", hoja_pandas())
    t = insertar(t, "slm", hoja_slm())
    t = insertar(t, "trocear", hoja_trocear())
    t = insertar(t, "graficos", hoja_graficos())
    t = insertar(t, "python", hoja_python())
    t = insertar(t, "redes", hoja_redes())
    t = insertar(t, "algoritmos", hoja_algoritmos())
    t = insertar(t, "inferencia", hoja_inferencia())
    t = insertar(t, "produccion", hoja_produccion())
    t = insertar(t, "ciberseguridad", hoja_ciberseguridad())
    t = insertar(t, "agentedentro", hoja_agentedentro())
    t = insertar(t, "matematicas", hoja_matematicas())
    t = insertar(t, "herramientas", hoja_herramientas())
    t = insertar(t, "script", hoja_script())
    t = insertar(t, "resolver", hoja_resolver())
    TEORIA.write_text(t, encoding="utf-8")
    UD4 = RAIZ / "contenidos" / "ud4-lenguaje.md"
    if UD4.exists():
        u = UD4.read_text(encoding="utf-8")
        UD4.write_text(insertar(u, "llm", hoja_llm()), encoding="utf-8")
    DATOS = RAIZ / "contenidos" / "datos.md"
    if DATOS.exists():
        u = DATOS.read_text(encoding="utf-8")
        DATOS.write_text(insertar(u, "eda", hoja_eda()), encoding="utf-8")
    UD3 = RAIZ / "contenidos" / "ud3-vision.md"
    if UD3.exists():
        u = UD3.read_text(encoding="utf-8")
        UD3.write_text(insertar(u, "vision", hoja_vision()), encoding="utf-8")
    UD5 = RAIZ / "contenidos" / "ud5-ml.md"
    if UD5.exists():
        u = UD5.read_text(encoding="utf-8")
        UD5.write_text(insertar(u, "evaluacion", hoja_evaluacion()), encoding="utf-8")
    UD1 = RAIZ / "contenidos" / "ud1.md"
    if UD1.exists():
        u = UD1.read_text(encoding="utf-8")
        UD1.write_text(insertar(u, "ml", hoja_ml()), encoding="utf-8")
    ITI = RAIZ / "contenidos" / "itinerario.md"
    if ITI.exists():
        u = ITI.read_text(encoding="utf-8")
        ITI.write_text(insertar(u, "rutas", hoja_rutas()), encoding="utf-8")
    print("hojas insertadas")
