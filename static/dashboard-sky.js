// ============================================================================
// LongoUZ — dashboard hero: kunduzgi rejimda quyosh tog' orqasidan asta chiqadi,
// osmon rangi va quyosh o'rni foydalanuvchi mahalliy soatiga qarab o'zgaradi.
// Tema almashganda: oy tog' ortiga tushadi va quyosh asta ko'tariladi (yoki teskarisi).
// Test uchun: sahifa manzilining oxiriga ?hour=13.5 qo'shing.
// ============================================================================
(function () {
  "use strict";
  var hero = document.querySelector(".dash-hero");
  var svg = document.querySelector(".dash-hero-art");
  if (!hero || !svg) return;

  var sun = svg.querySelector("#hs-sun"), moon = svg.querySelector("#hs-moon");
  var horizon = svg.querySelector("#hs-horizon"), stars = svg.querySelector("#hs-stars"), glowC = svg.querySelector("#hs-glowc");
  var gradIds = ["hs-sky", "hs-far", "hs-mid", "hs-main"];
  var grads = gradIds.map(function (id) { return svg.querySelector("#" + id); });
  var REDUCED = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  var NIGHT = {
    sky: ["#070d24", "#1b1b4d", "#6b3a74", "#f4a24a"], far: ["#3a3f86", "#1b1f52"], mid: ["#2b3175", "#12163f"],
    main: ["#49529f", "#262c6b", "#0f1238"], hero: ["#0d1b4f", "#14286b", "#1b3a8f"]
  };
  var KEYS = [
    [4.5, ["#0b1233", "#24305f", "#3b3f7a"], 0], [5.5, ["#33468f", "#c46a86", "#ffb27a"], 0.25],
    [7, ["#3f8fe0", "#8fcbff", "#ffe2b0"], 0.7], [10, ["#2f95f2", "#78c3ff", "#dff3ff"], 1],
    [14, ["#2a8cf0", "#6fbdff", "#d9f0ff"], 1], [16.5, ["#3d7fe0", "#8fb4f0", "#ffe0b0"], 0.85],
    [18.3, ["#4a5cc0", "#ff9468", "#ffd08a"], 0.45], [19.4, ["#1b2a6b", "#7a4a8a", "#f4a24a"], 0.1],
    [20.5, ["#070d24", "#1b1b4d", "#3a2a5c"], 0]
  ];
  var WARM = "#ffb58a";
  var SUN_HIDE = 300, MOON_UP = 74, MOON_HIDE = 250;

  function hex(c) { return [1, 3, 5].map(function (i) { return parseInt(c.substr(i, 2), 16); }); }
  function mix(a, b, t) {
    var A = hex(a), B = hex(b);
    return "#" + A.map(function (v, i) { return ("0" + Math.round(v + (B[i] - v) * t).toString(16)).slice(-2); }).join("");
  }
  function lerpKey(h) {
    if (h <= KEYS[0][0]) return { c: KEYS[0][1], d: KEYS[0][2] };
    for (var i = 0; i < KEYS.length - 1; i++) {
      var a = KEYS[i], b = KEYS[i + 1];
      if (h >= a[0] && h <= b[0]) {
        var t = (h - a[0]) / (b[0] - a[0]);
        return { c: a[1].map(function (col, k) { return mix(col, b[1][k], t); }), d: a[2] + (b[2] - a[2]) * t };
      }
    }
    var l = KEYS[KEYS.length - 1];
    return { c: l[1], d: l[2] };
  }
  function nowHour() {
    var m = /[?&]hour=([\d.]+)/.exec(location.search);
    if (m) return parseFloat(m[1]);
    var d = new Date();
    return d.getHours() + d.getMinutes() / 60;
  }
  function sunPos(h) {
    var f = Math.min(1, Math.max(0, (h - 6) / 13.5));
    return { x: 135 + f * 450, y: 215 - 176 * Math.sin(Math.PI * f) };
  }

  // holat: ranglar (14 ta) + raqamlar
  function stateFor(light) {
    var h = nowHour(), cols, n;
    if (!light) {
      cols = NIGHT.sky.concat(NIGHT.far, NIGHT.mid, NIGHT.main, NIGHT.hero);
      n = { stars: 1, glow: 1, sunX: 360, sunY: SUN_HIDE, sunO: 0, moonY: MOON_UP, moonO: 1 };
      return { cols: cols, n: n };
    }
    var k = lerpKey(h), d = k.d, dh = k.c;
    var lt = 0.18 + (1 - d) * 0.25;
    var tint = function (c, t) { return mix(c, dh[2], t); };
    cols = [dh[0], dh[1], mix(dh[1], dh[2], .5), dh[2],
      tint(mix("#8fb0e8", "#3a3f86", 1 - d), lt), tint(mix("#6f93d4", "#1b1f52", 1 - d), lt),
      tint(mix("#6a8fd8", "#2b3175", 1 - d), lt), tint(mix("#456ab5", "#12163f", 1 - d), lt),
      mix("#7fa3e6", "#49529f", 1 - d), mix("#4f74c6", "#262c6b", 1 - d), mix("#2f4a99", "#0f1238", 1 - d),
      mix(dh[0], "#0d1b4f", .15), mix(dh[0], dh[1], .6), dh[1]];
    var pos = sunPos(h), night = h < 5 || h > 20.3;
    n = {
      stars: Math.max(0, 0.9 - d * 1.6), glow: 0.15, sunX: pos.x, sunY: night ? SUN_HIDE : pos.y, sunO: night ? 0 : 1,
      moonY: d > 0.45 ? MOON_HIDE : MOON_UP, moonO: d > 0.45 ? 0 : 1
    };
    return { cols: cols, n: n, day: !night && d > 0.3 };
  }

  function setStops(grad, arr) {
    if (!grad) return;
    var st = grad.querySelectorAll("stop");
    arr.forEach(function (c, i) { if (st[i]) st[i].setAttribute("stop-color", c); });
  }
  function render(cols, n, light) {
    setStops(grads[0], cols.slice(0, 4)); setStops(grads[1], cols.slice(4, 6));
    setStops(grads[2], cols.slice(6, 8)); setStops(grads[3], cols.slice(8, 11));
    if (stars) stars.style.opacity = String(n.stars);
    if (glowC) glowC.style.opacity = String(n.glow);
    if (sun) { sun.setAttribute("transform", "translate(" + n.sunX.toFixed(1) + " " + n.sunY.toFixed(1) + ")"); sun.style.display = n.sunO > 0.01 ? "" : "none"; sun.style.opacity = String(n.sunO); }
    if (moon) { moon.setAttribute("transform", "translate(118 " + n.moonY.toFixed(1) + ")"); moon.style.display = n.moonO > 0.01 ? "" : "none"; moon.style.opacity = String(n.moonO); }
    if (horizon) {
      var low = Math.min(1, Math.max(0, (n.sunY - 105) / 110)) * Math.min(1, Math.max(0, n.sunO));
      horizon.setAttribute("transform", "translate(" + n.sunX.toFixed(1) + " " + Math.min(n.sunY, 214).toFixed(1) + ")");
      horizon.style.opacity = light ? String(low.toFixed(3)) : "0";
    }
    hero.classList.toggle("is-day", !!light);
  }

  var current = null, raf = 0;
  function lerpState(a, b, t) {
    var cols = a.cols.map(function (c, i) {
      var v = mix(c, b.cols[i], t);
      return i < 4 ? mix(v, WARM, Math.sin(Math.PI * t) * 0.28) : v;
    });
    var n = {};
    Object.keys(a.n).forEach(function (k) { n[k] = a.n[k] + (b.n[k] - a.n[k]) * t; });
    return { cols: cols, n: n };
  }
  function go(light, animate) {
    cancelAnimationFrame(raf);
    var target = stateFor(light);
    if (!animate || REDUCED || !current) { current = target; render(target.cols, target.n, light); if (!light) hero.style.removeProperty("--hero-bg"); return; }
    var from = current, t0 = null, dur = 1250;
    // quyosh/oy yo'li: avval bittasi tushadi, keyin ikkinchisi ko'tariladi
    var start = JSON.parse(JSON.stringify(from));
    function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min(1, (ts - t0) / dur), e = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      var s = lerpState(start, target, e);
      var down = Math.min(1, p / 0.5), up = Math.max(0, (p - 0.4) / 0.6);
      var ease = function (x) { return 1 - Math.pow(1 - x, 3); };
      if (light) {
        s.n.moonY = start.n.moonY + (MOON_HIDE - start.n.moonY) * ease(down); s.n.moonO = 1 - Math.max(0, (down - .7) / .3) * (start.n.moonO ? 1 : 0);
        s.n.sunY = SUN_HIDE + (target.n.sunY - SUN_HIDE) * ease(up); s.n.sunO = target.n.sunO ? Math.min(1, up * 4) : 0; s.n.sunX = target.n.sunX;
      } else {
        s.n.sunY = start.n.sunY + (SUN_HIDE - start.n.sunY) * ease(down); s.n.sunO = start.n.sunO ? 1 - Math.max(0, (down - .75) / .25) : 0; s.n.sunX = start.n.sunX;
        s.n.moonY = MOON_HIDE + (MOON_UP - MOON_HIDE) * ease(up); s.n.moonO = Math.min(1, up * 4);
      }
      render(s.cols, s.n, light && p > 0.35);
      if (p < 1) raf = requestAnimationFrame(step);
      else { current = target; render(target.cols, target.n, light); if (!light) hero.style.removeProperty("--hero-bg"); }
    }
    raf = requestAnimationFrame(step);
  }

  function isLight() { return document.documentElement.getAttribute("data-theme") === "light"; }
  go(isLight(), false);
  if (isLight()) { // sahifa ochilganda quyosh tog' ortidan asta ko'tariladi
    var land = stateFor(true);
    current = stateFor(false); current.n.moonY = MOON_HIDE; current.n.moonO = 0; current.n.stars = 0;
    var tmp = JSON.parse(JSON.stringify(land)); tmp.n.sunY = SUN_HIDE; tmp.n.sunO = 0;
    render(tmp.cols, tmp.n, true); current = tmp; go(true, true);
  }
  // Tugma bosilganda: avval quyosh/oy almashuvi boshlanadi, butun ekran (tog', fon, kartalar)
  // ~0.5 s dan keyin asta-sekin qorong'ilashadi yoki yorishadi.
  var skipObserver = false;
  document.addEventListener("click", function (e) {
    var t = e.target.closest && e.target.closest(".theme-toggle");
    if (!t || REDUCED) return;
    e.preventDefault(); e.stopImmediatePropagation();
    var next = isLight() ? "dark" : "light", root = document.documentElement;
    root.classList.add("theme-anim");
    go(next === "light", true);
    setTimeout(function () {
      skipObserver = true;
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("longouz_theme", next); } catch (err) { /* ignore */ }
      setTimeout(function () { skipObserver = false; }, 0);
    }, 480);
    setTimeout(function () { root.classList.remove("theme-anim"); }, 2300);
  }, true);
  new MutationObserver(function () { if (!skipObserver) go(isLight(), true); }).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
  setInterval(function () { if (!raf || true) { var t = stateFor(isLight()); current = t; render(t.cols, t.n, isLight()); if (!isLight()) hero.style.removeProperty("--hero-bg"); } }, 60000);
})();
