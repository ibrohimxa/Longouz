/* v243: LongoAI «o'ylamoqda» animatsiyasi — window.LongoThink.
   LongoThink.el("sm"|"lg") -> faqat animatsiya; LongoThink.row("LongoAI o'ylamoqda") -> animatsiya + yozuv (chat pufakchasi).
   row.setStep("Google'da qidirilmoqda") — joriy ish bosqichini ko'rsatadi. Sahifadagi [data-longo-think] o'zi to'ldiriladi. */
(function () {
  "use strict";
  function ensureCss() {
    if (document.querySelector('link[data-longo-think-css]')) return;
    var l = document.createElement("link");
    l.rel = "stylesheet"; l.href = "/static/longo-think.css?v=245"; l.setAttribute("data-longo-think-css", "1");
    document.head.appendChild(l);
  }
  function el(size) {
    ensureCss();
    var w = document.createElement("span");
    w.className = "lthink" + (size ? " lthink-" + size : "");
    w.setAttribute("aria-hidden", "true");
    w.innerHTML = '<span class="lthink-glow"></span><span class="lthink-orbit"><i class="lthink-d"></i><i class="lthink-d"></i><i class="lthink-d"></i></span><span class="lthink-owl"></span>';
    return w;
  }
  var PHRASES = ["o'ylamoqda", "tekshirmoqda", "hisoblamoqda", "yozmoqda"];
  function row(label, opts) {
    opts = opts || {};
    var r = document.createElement("div");
    r.className = "lthink-row" + (opts.className ? " " + opts.className : "");
    r.setAttribute("role", "status");
    r.setAttribute("aria-live", "polite");
    r.appendChild(el(opts.size || "sm"));
    var t = document.createElement("span");
    t.className = "lthink-text";
    var txt = document.createElement("span");
    var name = label || "LongoAI o'ylamoqda";
    var sp = name.indexOf(" ");
    txt.innerHTML = sp > 0 ? "<b></b>&nbsp;<span></span>" : "<b></b>";
    txt.querySelector("b").textContent = sp > 0 ? name.slice(0, sp) : name;
    if (sp > 0) txt.querySelector("span").textContent = name.slice(sp + 1);
    var dots = document.createElement("span");
    dots.textContent = "…";
    t.appendChild(txt); t.appendChild(dots);
    var box = document.createElement("span");
    box.appendChild(t);
    var step = document.createElement("small");
    step.className = "lthink-step"; step.hidden = true;
    box.appendChild(step);
    r.appendChild(box);
    // uzoq kutishda yozuv o'zgarib turadi (o'ylamoqda -> tekshirmoqda -> yozmoqda)
    var i = 0, timer = null;
    if (opts.rotate !== false && sp > 0) {
      timer = setInterval(function () {
        if (!r.isConnected) { clearInterval(timer); return; }
        i = (i + 1) % PHRASES.length;
        txt.querySelector("span").textContent = PHRASES[i];
      }, 2600);
    }
    r.setStep = function (s) { step.hidden = !s; step.textContent = s || ""; };
    r.stop = function () { if (timer) clearInterval(timer); };
    return r;
  }
  window.LongoThink = { el: el, row: row, css: ensureCss };
  function auto() {
    document.querySelectorAll("[data-longo-think]").forEach(function (n) {
      if (n.dataset.ltDone) return;
      n.dataset.ltDone = "1";
      n.appendChild(n.dataset.longoThink ? row(n.dataset.longoThink) : el(n.dataset.size || ""));
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", auto); else auto();
})();
