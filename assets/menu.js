/* Menú principal accesible: botones con aria-expanded, Esc para cerrar, clic fuera para cerrar,
   y en móvil un botón «Menú» que abre el panel. Sin JavaScript, el menú se ve completo. */
(function () {
  var nav = document.querySelector(".menu");
  if (!nav) return;
  nav.classList.add("menu-js");
  var boton = nav.querySelector(".menu-boton");
  var grupos = Array.prototype.slice.call(nav.querySelectorAll(".menu-grupo"));
  var movil = window.matchMedia("(max-width: 900px)");

  function abrirGrupo(g, abrir) {
    g.classList.toggle("abierto", abrir);
    g.querySelector(".menu-grupo-boton").setAttribute("aria-expanded", abrir ? "true" : "false");
  }
  function cerrarGrupos(excepto) {
    grupos.forEach(function (g) { if (g !== excepto) abrirGrupo(g, false); });
  }
  function abrirPanel(abrir) {
    nav.classList.toggle("abierto", abrir);
    boton.setAttribute("aria-expanded", abrir ? "true" : "false");
    if (abrir) {                                   // en móvil, el grupo de la página actual ya abierto
      var actual = nav.querySelector(".menu-grupo.actual");
      cerrarGrupos(actual);
      if (actual) abrirGrupo(actual, true);
    } else {
      cerrarGrupos(null);
    }
  }

  grupos.forEach(function (g) {
    var b = g.querySelector(".menu-grupo-boton");
    b.addEventListener("click", function () {
      var abrir = !g.classList.contains("abierto");
      if (!movil.matches) cerrarGrupos(g);
      abrirGrupo(g, abrir);
    });
    g.addEventListener("focusout", function (e) {   // en escritorio, al salir con el tabulador se cierra
      if (!movil.matches && !g.contains(e.relatedTarget)) abrirGrupo(g, false);
    });
  });
  boton.addEventListener("click", function () { abrirPanel(!nav.classList.contains("abierto")); });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var abierto = nav.querySelector(".menu-grupo.abierto");
    if (movil.matches && nav.classList.contains("abierto")) { abrirPanel(false); boton.focus(); }
    else if (abierto) { abrirGrupo(abierto, false); abierto.querySelector(".menu-grupo-boton").focus(); }
  });
  document.addEventListener("click", function (e) {
    if (nav.contains(e.target)) return;
    if (movil.matches) { if (nav.classList.contains("abierto")) abrirPanel(false); }
    else cerrarGrupos(null);
  });
  movil.addEventListener("change", function () { abrirPanel(false); });
})();
