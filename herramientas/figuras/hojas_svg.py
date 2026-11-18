"""Hojas visuales en HTML + SVG en línea para la teoría (Git y agentes).

Se inspiran en la idea de las infografías que circulan por redes (fichas, comparaciones lado a lado,
flujos numerados, diagramas de ramas), pero con el estilo propio de la web: los colores salen de las
variables CSS (--ink, --pen, --marker, --c-ml...), así que funcionan en modo claro y oscuro.

Uso:  python3 herramientas/figuras/hojas_svg.py
Reescribe lo que haya entre <!-- hoja:NOMBRE --> y <!-- /hoja:NOMBRE --> en la teoría.
Importante (gfm): ningún bloque puede llevar líneas en blanco dentro.
"""
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
    TEORIA.write_text(t, encoding="utf-8")
    UD4 = RAIZ / "contenidos" / "ud4-lenguaje.md"
    if UD4.exists():
        u = UD4.read_text(encoding="utf-8")
        UD4.write_text(insertar(u, "llm", hoja_llm()), encoding="utf-8")
    print("hojas insertadas")
