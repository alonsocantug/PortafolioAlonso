/* Mejoras progresivas del portafolio. Sin dependencias. El sitio funciona igual sin este archivo. */
(function () {
  "use strict";
  window.__site = 1;
  var doc = document, root = doc.documentElement;
  var es = (root.lang || "es").indexOf("es") === 0;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* 1. Aparición al hacer scroll */
  var groups = [".work > .project", ".steps > li", ".prose > h2", ".section-head", ".split", ".cv-grid > *", ".timeline > li", ".about-grid > *"];
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    groups.forEach(function (sel) {
      doc.querySelectorAll(sel).forEach(function (el, i) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.95) return;         /* ya visible: no se oculta */
        el.classList.add("reveal");
        el.style.setProperty("--d", Math.min(i, 3) * 90 + "ms");
        io.observe(el);
      });
    });
  }

  /* 2. Barra de progreso de lectura (solo en casos) */
  var prose = doc.querySelector(".prose");
  if (prose) {
    var bar = doc.createElement("div");
    bar.className = "progress"; bar.setAttribute("aria-hidden", "true");
    doc.body.appendChild(bar);
    var ticking = false;
    var update = function () {
      var max = root.scrollHeight - window.innerHeight;
      bar.style.setProperty("--p", max > 0 ? Math.min(1, Math.max(0, window.scrollY / max)).toFixed(4) : 0);
      ticking = false;
    };
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  /* 3. Índice del caso: marca la sección que se está leyendo */
  var links = doc.querySelectorAll(".case-nav a[href^='#']");
  if (links.length && "IntersectionObserver" in window) {
    var byId = {};
    links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) { a.removeAttribute("aria-current"); });
        var a = byId[e.target.id];
        if (a) {
          a.setAttribute("aria-current", "location");
          var ol = a.closest("ol");
          if (ol && ol.scrollWidth > ol.clientWidth) ol.scrollLeft = a.offsetLeft - ol.clientWidth / 3;
        }
      });
    }, { rootMargin: "-15% 0px -75% 0px" });
    Object.keys(byId).forEach(function (id) { var h = doc.getElementById(id); if (h) spy.observe(h); });
  }

  /* 4. Clic para ampliar las imágenes del caso */
  var imgs = doc.querySelectorAll(".prose figure > img");
  if (imgs.length && typeof HTMLDialogElement === "function") {
    var label = es ? "Ampliar" : "Enlarge";
    var dlg = doc.createElement("dialog");
    dlg.className = "lightbox";
    dlg.setAttribute("aria-label", es ? "Imagen ampliada" : "Enlarged image");
    dlg.innerHTML = '<div class="lightbox-inner"><img alt=""></div><button type="button" class="lightbox-close">' + (es ? "Cerrar" : "Close") + "</button>";
    doc.body.appendChild(dlg);
    var big = dlg.querySelector("img");
    var close = dlg.querySelector("button");
    var opener = null;
    imgs.forEach(function (img) {
      var b = doc.createElement("button");
      b.type = "button"; b.className = "zoom"; b.setAttribute("data-label", label);
      b.setAttribute("aria-label", label + ": " + img.alt);
      img.parentNode.insertBefore(b, img); b.appendChild(img);
      b.addEventListener("click", function () {
        opener = b;
        big.src = img.currentSrc || img.src; big.alt = img.alt;
        dlg.showModal();
      });
    });
    var shut = function () { if (dlg.open) dlg.close(); };
    close.addEventListener("click", shut);
    dlg.addEventListener("click", shut);                         /* clic en cualquier parte cierra */
    dlg.addEventListener("close", function () { if (opener) opener.focus(); });
  }
})();
