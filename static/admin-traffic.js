/* v243: Admin — tashriflar va testlar paneli (voronka + 14/30 kunlik grafik). */
(function () {
  "use strict";
  var root = document.getElementById("lz-traffic");
  if (!root) return;
  var SER = [
    { k: "visits", n: "Tashriflar", c: "#3dff7b" },
    { k: "visitors", n: "Odamlar", c: "#0bd855" },
    { k: "quiz_start", n: "Test boshlandi", c: "#c6ff3d" },
    { k: "quiz_finish", n: "Test tugadi", c: "#00e0a4" },
    { k: "signup", n: "Ro'yxatdan o'tdi", c: "#9dffbf" },
    { k: "ai_ask", n: "AI savollar", c: "#5effc0" }
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
    document.getElementById("lz-tr-legend").innerHTML = SER.map(function (s) {
      return '<button type="button" data-k="' + s.k + '" class="' + (off[s.k] ? "off" : "") + '"><i style="background:' + s.c + '"></i>' + esc(s.n) + "</button>";
    }).join("");
  }

  function draw() {
    if (!data) return;
    var host = document.getElementById("lz-tr-chart"), S = data.series, n = S.length;
    var W = Math.max(300, host.clientWidth || 700), H = 240, L = 34, R = 18, B = 26, T = 12, ph = H - B - T, step = (W - L - R) / Math.max(1, n - 1);
    var vis = SER.filter(function (s) { return !off[s.k]; });
    var max = 4;
    vis.forEach(function (s) { S.forEach(function (d) { max = Math.max(max, d[s.k] || 0); }); });
    max = Math.ceil(max * 1.1);
    var svg = '<svg viewBox="0 0 ' + W + " " + H + '" preserveAspectRatio="none">';
    for (var g = 0; g <= 4; g++) {
      var y = T + ph - (ph * g) / 4;
      svg += '<line class="grid" x1="' + L + '" x2="' + (W - R) + '" y1="' + y + '" y2="' + y + '"/><text class="tx" x="' + (L - 6) + '" y="' + (y + 3) + '" text-anchor="end">' + fmt((max * g) / 4) + "</text>";
    }
    vis.forEach(function (s) {
      var pts = S.map(function (d, i) { return [L + step * i, T + ph - ((d[s.k] || 0) / max) * ph]; });
      var line = pts.map(function (p, i) { return (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1); }).join(" ");
      svg += '<path d="' + line + " L" + pts[n - 1][0] + " " + (T + ph) + " L" + L + " " + (T + ph) + 'Z" fill="' + s.c + '" opacity=".07"/>';
      svg += '<path d="' + line + '" fill="none" stroke="' + s.c + '" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>';
      pts.forEach(function (p, i) { svg += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="3" fill="' + s.c + '"><title>' + esc(S[i].day + " — " + s.n + ": " + (S[i][s.k] || 0)) + "</title></circle>"; });
    });
    S.forEach(function (d, i) {
      if (i % Math.ceil(n / 8) === 0 || i === n - 1) svg += '<text class="tx" x="' + (L + step * i) + '" y="' + (H - 8) + '" text-anchor="middle">' + d.day + "</text>";
    });
    host.innerHTML = svg + "</svg>";
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
