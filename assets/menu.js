/* Menú principal (patrón «responsive site navigation»):
   - Sin JavaScript: la lista es un popover nativo que abre el botón «Menú» (popovertarget) y los grupos
     son listas anidadas.
   - Con JavaScript: se mide si la fila cabe. Si cabe, la lista va en línea (sin popover) y cada grupo es
     un popover flotante; si no cabe, la lista es el popover y cada grupo un desplegable con hidden. */
(function () {
  var top = document.querySelector(".top");
  var nav = top && top.querySelector(".menu");
  if (!nav) return;
  var fila = top.querySelector(".in");
  var lista = nav.querySelector(".menu-lista");
  var grupos = Array.prototype.slice.call(nav.querySelectorAll(".menu-grupo"));
  var anchoAnterior = 0, ancho = null;
  var anclaNativa = window.CSS && CSS.supports("position-area", "block-end");

  function prepararGrupo(g, enLinea) {
    var b = g.querySelector(".menu-grupo-boton"), sub = g.querySelector(".menu-sub");
    b.setAttribute("aria-expanded", "false");
    if (enLinea) { sub.setAttribute("popover", "auto"); sub.hidden = false; b.setAttribute("popovertarget", sub.id); }
    else { sub.removeAttribute("popover"); b.removeAttribute("popovertarget"); sub.hidden = true; }
  }
  function aplicar(enLinea) {
    var abierto = lista.matches(":popover-open");
    top.classList.toggle("is-wide", enLinea);
    if (enLinea) lista.removeAttribute("popover");
    else lista.setAttribute("popover", "auto");
    grupos.forEach(function (g) { prepararGrupo(g, enLinea); });
    if (!enLinea && abierto && lista.showPopover) lista.showPopover();
    ancho = enLinea;
  }
  function medir() {
    var w = top.clientWidth;
    if (ancho === false && w <= anchoAnterior) { anchoAnterior = w; return; }   // plegado: solo si crece
    anchoAnterior = w;
    top.classList.add("is-measuring", "is-wide");
    lista.removeAttribute("popover");
    grupos.forEach(function (g) { g.querySelector(".menu-sub").hidden = true; });
    var cabe = fila.scrollWidth <= fila.clientWidth + 1;
    aplicar(cabe);
    requestAnimationFrame(function () { top.classList.remove("is-measuring"); });
  }

  grupos.forEach(function (g) {
    var b = g.querySelector(".menu-grupo-boton"), sub = g.querySelector(".menu-sub");
    b.addEventListener("click", function () {
      if (ancho) return;                                   // en línea lo abre popovertarget
      var abrir = sub.hidden;
      sub.hidden = !abrir; b.setAttribute("aria-expanded", String(abrir));
    });
    sub.addEventListener("toggle", function (e) {
      b.setAttribute("aria-expanded", String(e.newState === "open"));
      if (e.newState === "open" && !anclaNativa) {          // sin anchor positioning: colocar a mano
        var t = b.getBoundingClientRect(), s = sub.getBoundingClientRect();
        var y = t.bottom + 6; if (y + s.height > innerHeight) y = Math.max(0, t.top - s.height - 6);
        sub.style.top = y + "px";
        sub.style.left = Math.min(Math.max(0, t.left), innerWidth - s.width) + "px";
      }
    });
    g.addEventListener("focusout", function (e) {          // al salir con el tabulador se cierra
      if (ancho && e.relatedTarget && !g.contains(e.relatedTarget) && sub.matches(":popover-open")) sub.hidePopover();
    });
  });
  // Al abrir el menú plegado, el grupo de la página actual ya desplegado
  lista.addEventListener("toggle", function (e) {
    if (ancho || e.newState !== "open") return;
    var actual = nav.querySelector(".menu-grupo.actual");
    if (actual) { actual.querySelector(".menu-sub").hidden = false; actual.querySelector(".menu-grupo-boton").setAttribute("aria-expanded", "true"); }
  });

  if (window.ResizeObserver) {
    var ro = new ResizeObserver(function () { medir(); });
    ro.observe(top); ro.observe(lista);
  } else { window.addEventListener("resize", medir); }
  medir();
})();

/* Claro / oscuro: dos estados (seguir al sistema, o el contrario de lo que se ve) */
(function () {
  var meta = document.querySelector('meta[name="color-scheme"]');
  var boton = document.querySelector(".tema");
  if (!meta || !boton) return;
  var sistema = window.matchMedia("(prefers-color-scheme: dark)");
  function visto() { var v = meta.content; return v === "dark" || v === "light" ? v : (sistema.matches ? "dark" : "light"); }
  boton.addEventListener("click", function () {
    var objetivo = visto() === "dark" ? "light" : "dark";
    var sis = sistema.matches ? "dark" : "light";
    try {
      if (objetivo !== sis) localStorage.setItem("color-scheme", objetivo);
      else localStorage.removeItem("color-scheme");
    } catch (e) {}
    meta.content = objetivo !== sis ? objetivo : "light dark";
  });
  window.addEventListener("storage", function (e) {
    if (e.key === "color-scheme") meta.content = e.newValue || "light dark";
  });
})();

/* Figuras: tocar para verlas a tamaño completo */
document.querySelectorAll('main img[src^="assets/img/"]').forEach(function (img) {
  if (img.closest("a")) return;
  var a = document.createElement("a");
  a.href = img.getAttribute("src"); a.target = "_blank"; a.rel = "noopener";
  a.title = "Abrir la figura a tamaño completo";
  img.parentNode.insertBefore(a, img); a.appendChild(img);
});
