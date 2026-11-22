/* v246: bosh sahifa — jonli raqamlar (sanoqli animatsiya) va «Jonli natijalar» lentasi. */
(function () {
  "use strict";
  var grid = document.getElementById("hm-live-grid");
  if (!grid) return;
  var fmt = function (n) { return Math.round(n).toLocaleString("ru-RU").replace(/,/g, " "); };
  function animate(el, to, suffix) {
    var from = +el.dataset.v || 0, t0 = performance.now(), dur = 1400;
    el.dataset.v = to;
    (function step(t) {
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = fmt(from + (to - from) * e) + (suffix || "");
      if (k < 1) requestAnimationFrame(step);
    })(t0);
  }
  var shown = false;
  function load() {
    fetch("/api/site-stats", { credentials: "same-origin" }).then(function (r) { return r.json(); }).then(function (d) {
      grid.querySelectorAll(".hm-live-card").forEach(function (c) {
        var v = d[c.dataset.k]; if (v == null) return;
        animate(c.querySelector("b"), +v, c.dataset.suffix);
      });
    }).catch(function () {});
  }
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting && !shown) { shown = true; load(); } });
  }, { threshold: 0.2 }) : null;
  if (io) io.observe(grid); else load();
  setInterval(function () { if (shown && !document.hidden) load(); }, 30000);

  // Jonli natijalar lentasi (ism — faqat bosh harf)
  fetch("/api/public/recent-results").then(function (r) { return r.json(); }).then(function (d) {
    var items = (d && d.items) || [];
    if (items.length < 3) return;
    var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
    var html = items.map(function (x) {
      var cls = x.pct >= 80 ? "hi" : x.pct >= 50 ? "mid" : "lo";
      return '<span class="hm-tk ' + cls + '"><b>' + esc(x.name) + "</b> " + esc(x.subject) + " — <em>" + esc(x.score) + "</em></span>";
    }).join("");
    document.getElementById("hm-ticker-run").innerHTML = html + html;
    document.getElementById("hm-ticker").hidden = false;
  }).catch(function () {});
})();
