// LongoUZ dashboard: halqalar, tarix grafigi, reyting tablari, Ctrl/⌘+K qidiruv
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function animateRing(el) {
    var target = Math.max(0, Math.min(100, parseFloat(el.getAttribute("data-ring")) || 0));
    if (el.classList.contains("dash-ring")) el.classList.add(target >= 70 ? "good" : target >= 40 ? "mid" : "low");
    if (reduce) { el.style.setProperty("--p", target); return; }
    var start = null, dur = 1200;
    function step(ts) {
      if (start === null) start = ts;
      var t = Math.min(1, (ts - start) / dur), e = 1 - Math.pow(1 - t, 3);
      el.style.setProperty("--p", (target * e).toFixed(1));
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var ringEls = document.querySelectorAll("[data-ring]");
  if ("IntersectionObserver" in window) {
    var seen = new WeakSet();
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting && !seen.has(e.target)) { seen.add(e.target); animateRing(e.target); } }); }, { threshold: 0.35 });
    ringEls.forEach(function (r) { io.observe(r); });
  } else { ringEls.forEach(animateRing); }
  document.querySelectorAll(".dash-ring-item").forEach(function (it) {
    it.addEventListener("mouseenter", function () { var r = it.querySelector("[data-ring]"); if (r) animateRing(r); });
  });

  document.querySelectorAll("[data-count]").forEach(function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10) || 0, suffix = el.getAttribute("data-suffix") || "";
    if (reduce || !target) return;
    var start = null;
    function step(ts) {
      if (start === null) start = ts;
      var t = Math.min(1, (ts - start) / 900);
      el.textContent = Math.round(target * (1 - Math.pow(1 - t, 3))) + suffix;
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });

  // ---- Natijalar tarixi (SVG chiziq grafigi, davr tanlash, oxirgi nuqtada bubble) ----
  var host = document.getElementById("dash-history");
  var raw = document.getElementById("dash-data");
  var period = document.getElementById("dash-period");
  var all = [];
  try { all = raw ? (JSON.parse(raw.textContent) || []) : []; } catch (e) { all = []; }

  function drawHistory() {
    if (!host) return;
    var days = period ? parseInt(period.value, 10) : 0, data = all;
    if (days > 0) {
      var cut = new Date(Date.now() - days * 86400000).toISOString().slice(0, 10);
      data = all.filter(function (d) { return (d.iso || "9999") >= cut; });
    }
    if (!data.length) { host.innerHTML = '<p class="dash-empty">' + (all.length ? "Bu davrda test yechilmagan." : "Hali test yechilmagan — birinchi testdan keyin grafik shu yerda paydo bo'ladi.") + "</p>"; return; }
    var W = Math.max(260, host.clientWidth || 640), H = 210, L = 30, R = 16, T = 30, B = 28;
    var n = data.length, pw = W - L - R, ph = H - T - B;
    var X = function (i) { return L + (n === 1 ? pw / 2 : (pw * i) / (n - 1)); };
    var Y = function (v) { return T + ph - (ph * v) / 100; };
    var pts = data.map(function (d, i) { return [X(i), Y(d.percent)]; });
    var path = pts.map(function (p, i) { return (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1); }).join(" ");
    var len = 0; for (var i = 1; i < pts.length; i++) len += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
    var svg = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="Natijalar tarixi grafigi"><defs><linearGradient id="dz-grad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2fbf83" stop-opacity=".5"/><stop offset="1" stop-color="#2fbf83" stop-opacity="0"/></linearGradient></defs>';
    [0, 25, 50, 75, 100].forEach(function (g) {
      svg += '<line class="grid-line" x1="' + L + '" x2="' + (W - R) + '" y1="' + Y(g) + '" y2="' + Y(g) + '"/><text class="axis-text" x="' + (L - 6) + '" y="' + (Y(g) + 4) + '" text-anchor="end">' + g + "</text>";
    });
    if (n > 1) svg += '<path class="area" d="' + path + " L" + pts[n - 1][0] + " " + Y(0) + " L" + pts[0][0] + " " + Y(0) + ' Z"/>';
    svg += '<path class="line" style="--len:' + Math.ceil(len + 4) + '" d="' + (n === 1 ? "M" + (pts[0][0] - 1) + " " + pts[0][1] + " L" + (pts[0][0] + 1) + " " + pts[0][1] : path) + '"/>';
    pts.forEach(function (p, i) {
      var d = data[i], title = d.topic + " — " + d.percent + "% (" + d.date + ")";
      svg += '<circle class="dot" data-i="' + i + '" cx="' + p[0] + '" cy="' + p[1] + '" r="' + (i === n - 1 ? 6 : 4.5) + '"><title>' + title.replace(/[<&]/g, "") + "</title></circle>";
      if (n <= 8 || i % Math.ceil(n / 8) === 0 || i === n - 1) svg += '<text class="axis-text" x="' + p[0] + '" y="' + (H - 8) + '" text-anchor="middle">' + d.date + "</text>";
    });
    host.innerHTML = svg + "</svg>";
    var bubble = document.createElement("div"); bubble.className = "dash-bubble"; host.appendChild(bubble);
    function showBubble(i) {
      var d = data[i], prev = i > 0 ? data[i - 1].percent : null, diff = prev === null ? null : d.percent - prev;
      bubble.className = "dash-bubble" + (diff !== null && diff < 0 ? " down" : "");
      bubble.innerHTML = d.percent + "%" + (diff !== null && diff !== 0 ? "<small>(" + (diff > 0 ? "+" : "") + diff + ")</small>" : "");
      var box = host.querySelector("svg").getBoundingClientRect(), hb = host.getBoundingClientRect();
      bubble.style.left = (box.left - hb.left + (pts[i][0] / W) * box.width) + "px";
      bubble.style.top = (box.top - hb.top + (pts[i][1] / H) * box.height) + "px";
    }
    showBubble(n - 1);
    host.querySelectorAll(".dot").forEach(function (c) {
      var go = function () { showBubble(parseInt(c.getAttribute("data-i"), 10)); };
      c.addEventListener("mouseenter", go); c.addEventListener("click", go);
    });
  }
  drawHistory();
  if (period) period.addEventListener("change", drawHistory);
  window.addEventListener("resize", function () { clearTimeout(drawHistory._t); drawHistory._t = setTimeout(drawHistory, 150); });

  // ---- Maqsad (serverda saqlanadi: profil bilan bir xil) ----
  var gc = document.getElementById("goal-card");
  if (gc) {
    var avgNow = parseInt(gc.getAttribute("data-avg"), 10) || 0, target = parseInt(gc.getAttribute("data-target"), 10) || 90;
    var paint = function () {
      document.getElementById("goal-target").textContent = target; document.getElementById("goal-target2").textContent = target;
      var left = Math.max(0, target - avgNow);
      document.getElementById("goal-left").textContent = left ? "Yana " + left + "% sari harakat!" : "Maqsadga erishdingiz!";
      document.getElementById("goal-fill").style.setProperty("--w", Math.min(100, Math.round(avgNow * 100 / target)) + "%");
    };
    paint();
    document.getElementById("goal-edit").addEventListener("click", function () {
      var v = parseInt(window.prompt("Maqsadli o'rtacha natija (10–100 %):", String(target)), 10);
      if (!(v >= 10 && v <= 100)) return;
      fetch("/api/profile/update", { method: "POST", headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" }, body: JSON.stringify({ target_percent: v }) })
        .then(function (r) { if (r.ok) { target = v; paint(); } });
    });
  }

  // ---- Reyting tablari ----
  var tabs = document.querySelectorAll(".dash-tabs button");
  tabs.forEach(function (b) {
    b.addEventListener("click", function () {
      tabs.forEach(function (x) { x.classList.toggle("active", x === b); });
      document.querySelectorAll("[data-board-list]").forEach(function (l) { l.hidden = l.getAttribute("data-board-list") !== b.getAttribute("data-board"); });
    });
  });

  // ---- Ctrl/⌘ + K qidiruv ----
  var pal = document.getElementById("dash-palette"), inp = document.getElementById("dash-palette-input"), list = document.getElementById("dash-palette-list");
  var items = [
    ["Bosh sahifa", "/dashboard"], ["Test boshlash", "/quiz"], ["Mavzular bo'yicha mashq", "/quiz"], ["AI repetitor", "/repetitor"],
    ["Reyting", "#leaderboard"], ["Balans", "/balance"], ["Profil va sertifikatlar", "/profile"], ["Pro'ga o'tish", "/upgrade"], ["Yordam", "/support"],
  ];
  var sel = 0;
  function render() {
    var q = (inp.value || "").toLowerCase().trim();
    var shown = items.filter(function (it) { return !q || it[0].toLowerCase().indexOf(q) !== -1; });
    sel = Math.min(sel, Math.max(0, shown.length - 1));
    list.innerHTML = shown.map(function (it, i) { return '<li class="' + (i === sel ? "sel" : "") + '"><a href="' + it[1] + '">' + it[0] + "</a></li>"; }).join("") || '<li><a>Hech narsa topilmadi</a></li>';
  }
  function open() { pal.hidden = false; inp.value = ""; sel = 0; render(); setTimeout(function () { inp.focus(); }, 10); }
  function close() { pal.hidden = true; }
  if (pal && inp) {
    document.getElementById("dash-search-btn").addEventListener("click", open);
    pal.addEventListener("click", function (e) { if (e.target === pal) close(); });
    inp.addEventListener("input", function () { sel = 0; render(); });
    inp.addEventListener("keydown", function (e) {
      var n = list.querySelectorAll("li").length;
      if (e.key === "ArrowDown") { sel = (sel + 1) % n; render(); e.preventDefault(); }
      else if (e.key === "ArrowUp") { sel = (sel - 1 + n) % n; render(); e.preventDefault(); }
      else if (e.key === "Enter") { var a = list.querySelector("li.sel a"); if (a && a.getAttribute("href")) { close(); location.href = a.getAttribute("href"); } }
    });
    document.addEventListener("keydown", function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); pal.hidden ? open() : close(); }
      else if (e.key === "Escape" && !pal.hidden) close();
    });
  }
})();
