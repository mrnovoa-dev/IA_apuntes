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
    TEORIA.write_text(t, encoding="utf-8")
    print("hojas insertadas")
