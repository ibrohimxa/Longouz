/* v243: Admin — tashriflar va testlar paneli (voronka + 14/30 kunlik grafik). */
(function () {
  "use strict";
  var root = document.getElementById("lz-traffic");
  if (!root) return;
  // v246: aniq ajraladigan ranglar (yashil, ko'k, sariq, binafsha, qizil, havorang)
  var SER = [
    { k: "visits", n: "Tashriflar", c: "#1def6a" },
    { k: "visitors", n: "Odamlar", c: "#2f8cff" },
    { k: "quiz_start", n: "Test boshlandi", c: "#ffb020" },
    { k: "quiz_finish", n: "Test tugadi", c: "#a855f7" },
    { k: "signup", n: "Ro'yxatdan o'tdi", c: "#ff4d6d" },
    { k: "ai_ask", n: "AI savollar", c: "#14d8e8" }
  ];
  var off = {}, data = null, days = 14;
  var fmt = function (n) { return Math.round(n || 0).toLocaleString("ru-RU").replace(/,/g, " "); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };

  function funnel(now) {
    var steps = [
      ["Bugun tashrif", now.today_views], ["Bugun odam", now.today_visitors], ["Test boshlandi", now.tests_started_today],
      ["Test tugadi", now.tests_today], ["Hozir saytda", now.online]
    ];
    var max = Math.max(1, steps[0][1] || 0, steps[1][1] || 0);
    document.getElementById("lz-tr-funnel").innerHTML = steps.map(function (s, i) {
      var w = Math.max(8, Math.round(100 * (s[1] || 0) / max));
      return '<div class="lz-tr-step"><span>' + esc(s[0]) + "</span><b>" + fmt(s[1]) + '</b><i style="--w:' + (i === 4 ? 100 : w) + '%"></i></div>';
    }).join("");
  }

  function legend() {
    var S = (data && data.series) || [];
    document.getElementById("lz-tr-legend").innerHTML = SER.map(function (s) {
      var tot = S.reduce(function (a, d) { return a + (d[s.k] || 0); }, 0);
      return '<button type="button" data-k="' + s.k + '" class="' + (off[s.k] ? "off" : "") + (tot ? "" : " zero") + '" title="' + esc(s.n) + ': davr bo\'yicha jami ' + tot + '"><i style="background:' + s.c + '"></i>' + esc(s.n) + ' <b>' + fmt(tot) + "</b></button>";
    }).join("");
  }

  function draw() {
    if (!data) return;
    var host = document.getElementById("lz-tr-chart"), S = data.series, n = S.length;
    var W = Math.max(300, host.clientWidth || 700), H = 250, L = 34, R = 14, B = 26, T = 14, ph = H - B - T, step = (W - L - R) / Math.max(1, n - 1);
    var vis = SER.filter(function (s) { return !off[s.k]; });
    var max = 4;
    vis.forEach(function (s) { S.forEach(function (d) { max = Math.max(max, d[s.k] || 0); }); });
    max = Math.max(4, Math.ceil(max * 1.12 / 4) * 4);   // butun sonli o'q belgilari
    var X = function (i) { return L + step * i; }, Y = function (v) { return T + ph - (v / max) * ph; };
    var svg = '<svg viewBox="0 0 ' + W + " " + H + '" preserveAspectRatio="none">';
    for (var g = 0; g <= 4; g++) {
      var y = T + ph - (ph * g) / 4;
      svg += '<line class="grid" x1="' + L + '" x2="' + (W - R) + '" y1="' + y + '" y2="' + y + '"/><text class="tx" x="' + (L - 6) + '" y="' + (y + 3) + '" text-anchor="end">' + fmt((max * g) / 4) + "</text>";
    }
    vis.forEach(function (s, si) {
      var pts = S.map(function (d, i) { return [X(i), Y(d[s.k] || 0), d[s.k] || 0]; });
      var line = pts.map(function (p, i) { return (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1); }).join(" ");
      if (si === 0) svg += '<path d="' + line + " L" + pts[n - 1][0] + " " + (T + ph) + " L" + L + " " + (T + ph) + 'Z" fill="' + s.c + '" opacity=".10"/>';
      svg += '<path d="' + line + '" fill="none" stroke="' + s.c + '" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round" opacity=".95"/>';
      pts.forEach(function (p) { if (p[2] > 0) svg += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="3.6" fill="' + s.c + '" stroke="var(--bg-elevated,#0c1a12)" stroke-width="1.5"/>'; });
    });
    S.forEach(function (d, i) {
      if (i % Math.ceil(n / 7) === 0 || i === n - 1) svg += '<text class="tx" x="' + X(i) + '" y="' + (H - 8) + '" text-anchor="' + (i === n - 1 ? "end" : i === 0 ? "start" : "middle") + '">' + d.day + "</text>";
    });
    svg += '<line class="lz-tr-cross" x1="-9" x2="-9" y1="' + T + '" y2="' + (T + ph) + '"/>';
    host.innerHTML = svg + '</svg><div class="lz-tr-tip" hidden></div>';
    var el = host.querySelector("svg"), tip = host.querySelector(".lz-tr-tip"), cross = host.querySelector(".lz-tr-cross");
    function move(ev) {
      var r = el.getBoundingClientRect(), px = ((ev.touches ? ev.touches[0].clientX : ev.clientX) - r.left) / r.width * W;
      var i = Math.max(0, Math.min(n - 1, Math.round((px - L) / step))), d = S[i];
      cross.setAttribute("x1", X(i)); cross.setAttribute("x2", X(i));
      tip.innerHTML = "<b>" + d.day + "</b>" + vis.map(function (s) { return '<span><i style="background:' + s.c + '"></i>' + esc(s.n) + ": <b>" + fmt(d[s.k] || 0) + "</b></span>"; }).join("");
      tip.hidden = false;
      var left = (X(i) / W) * r.width;
      tip.style.left = Math.min(r.width - tip.offsetWidth - 4, Math.max(4, left + 12)) + "px";
    }
    el.addEventListener("mousemove", move); el.addEventListener("touchstart", move, { passive: true }); el.addEventListener("touchmove", move, { passive: true });
    el.addEventListener("mouseleave", function () { tip.hidden = true; cross.setAttribute("x1", -9); cross.setAttribute("x2", -9); });
  }

  function foot() {
    var dv = data.devices || {}, tot = 0, k;
    for (k in dv) tot += dv[k];
    var parts = [];
    for (k in dv) parts.push(esc(k) + " " + (tot ? Math.round(100 * dv[k] / tot) : 0) + "%");
    var now = data.now || {};
    document.getElementById("lz-tr-foot").innerHTML =
      "<span>Qurilmalar (30 kun): <b>" + (parts.join(" · ") || "—") + "</b></span>" +
      "<span>Qaytib kelganlar: <b>" + (data.returning || 0) + "%</b></span>" +
      "<span>Testni oxirigacha yechish: <b>" + (now.finish_rate || 0) + "%</b></span>" +
      "<span>Bugun AI savollar: <b>" + fmt(now.ai_today) + "</b></span>";
  }

  function load() {
    fetch(location.pathname.replace(/\/$/, "") + "/api/traffic?days=" + days, { credentials: "same-origin" })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { if (!d) return; data = d; funnel(d.now || {}); legend(); draw(); foot(); })
      .catch(function () {});
  }

  root.addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b) return;
    if (b.dataset.days) {
      days = +b.dataset.days;
      root.querySelectorAll(".lz-tr-range button").forEach(function (x) { x.classList.toggle("on", x === b); });
      load();
    } else if (b.dataset.k) {
      off[b.dataset.k] = !off[b.dataset.k];
      legend(); draw();
    }
  });
  var t; window.addEventListener("resize", function () { clearTimeout(t); t = setTimeout(draw, 150); });
  load();
  setInterval(function () { if (!document.hidden) load(); }, 30000);
})();
