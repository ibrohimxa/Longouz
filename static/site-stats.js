/* v235: kabinetdagi "sayt ko'rsatkichlari" — jonli raqamlar (sanab chiqish), 3D egilish, har 30 soniyada yangilanadi. */
(function () {
  "use strict";
  var root = document.getElementById("lz-site-stats");
  if (!root) return;
  var fmt = function (n) { return Math.round(n).toLocaleString("ru-RU").replace(/,/g, " "); };
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function animate(el, to, suffix) {
    var from = parseFloat(el.getAttribute("data-v")) || 0;
    if (from === to) { el.textContent = fmt(to) + suffix; return; }
    el.setAttribute("data-v", to);
    if (reduce) { el.textContent = fmt(to) + suffix; return; }
    var t0 = performance.now(), dur = from ? 900 : 1400;
    (function step(t) {
      var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(from + (to - from) * e) + suffix;
      if (p < 1) requestAnimationFrame(step);
      else if (from && to > from) { el.parentNode.classList.add("is-bump"); setTimeout(function () { el.parentNode.classList.remove("is-bump"); }, 700); }
    })(t0);
  }

  function load() {
    fetch("/api/site-stats", { credentials: "same-origin" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d) return;
      root.querySelectorAll(".lz-ss-card").forEach(function (c) {
        var k = c.getAttribute("data-k"), num = c.querySelector(".lz-ss-num");
        if (num && d[k] != null) animate(num, Number(d[k]) || 0, c.getAttribute("data-suffix") || "");
      });
      var tv = root.querySelector('[data-sub="today_views"]'); if (tv) tv.textContent = "bugun " + fmt(d.today_views || 0) + " marta";
      var q = root.querySelector('[data-sub="questions"]'); if (q) q.textContent = fmt(d.questions || 0) + "+ savol bazada";
    }).catch(function () {});
  }
  load();
  setInterval(function () { if (!document.hidden) load(); }, 30000);

  // 3D egilish — sichqoncha kartaning qaysi tomonida bo'lsa, o'sha tomonga og'adi
  if (!reduce && window.matchMedia("(hover: hover)").matches) {
    root.querySelectorAll(".lz-ss-card").forEach(function (c) {
      c.addEventListener("mousemove", function (e) {
        var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        c.style.transform = "perspective(700px) rotateX(" + (-y * 14).toFixed(2) + "deg) rotateY(" + (x * 16).toFixed(2) + "deg) translateY(-6px) scale(1.06)";
        c.style.setProperty("--mx", ((x + 0.5) * 100).toFixed(1) + "%"); c.style.setProperty("--my", ((y + 0.5) * 100).toFixed(1) + "%");
      });
      c.addEventListener("mouseleave", function () { c.style.transform = ""; });
    });
  }
})();
