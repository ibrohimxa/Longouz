// LongoUZ bosh sahifa: tog' bloki. Tema almashganda oy tog' ortiga tushadi,
// quyosh tog' orqasidan asta chiqadi (tong -> kun); kunduzdan tunga teskari.
(function () {
  "use strict";
  var sec = document.querySelector(".sky-bg");
  var svg = sec && sec.querySelector("svg");
  if (!svg) return;
  var sun = svg.querySelector("#fm-sun"), moon = svg.querySelector("#fm-moon");
  var stars = svg.querySelector("#fm-stars"), clouds = svg.querySelector("#fm-clouds");
  var REDUCED = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var DARK = { sky1: "#04100f", sky2: "#0d3536", ma1: "#244b63", ma2: "#0c1f2b", mb1: "#17394a", mb2: "#09191f", mc1: "#2a7c78", mc2: "#0b2b2d", mf: "#061214", tree: "#03100e", sun: "#9fffe0", path: "#5dffc4", pole: "#e8fff6", mcL1: "#2a8f88", mcL2: "#0c3436", mcR1: "#10353d", mcR2: "#051519", mist: "#0a2a2c", snow: "#d4eef0" };
  var LIGHT = { sky1: "#8fd3ee", sky2: "#f1fbf4", ma1: "#a9d6e6", ma2: "#dff3f0", mb1: "#7fc4b8", mb2: "#c9ecde", mc1: "#58b3a0", mc2: "#b7e4d3", mf: "#78c79c", tree: "#2f8f6a", sun: "#ffd45e", path: "#ffffff", pole: "#1c5f4b", mcL1: "#8fd6c4", mcL2: "#4fa797", mcR1: "#4a9c8f", mcR2: "#2f7d72", mist: "#e4f7ef", snow: "#ffffff" };
  var WARM = "#ffb58a";
  var SUN_UP = 150, SUN_DOWN = 840, MOON_UP = 140, MOON_DOWN = 840;
  var sunX = 1250, moonX = 330;
  var raf = 0, cur = null;

  function hex(c) { return [1, 3, 5].map(function (i) { return parseInt(c.substr(i, 2), 16); }); }
  function mix(a, b, t) { var A = hex(a), B = hex(b); return "#" + A.map(function (v, i) { return ("0" + Math.round(v + (B[i] - v) * t).toString(16)).slice(-2); }).join(""); }
  function isLight() { return document.documentElement.getAttribute("data-theme") === "light"; }
  function paint(p, from, to) {
    // p: 0 (from) -> 1 (to), 'to' kunduz bo'lsa quyosh ko'tariladi
    var dawn = Math.sin(Math.PI * p) * 0.32;
    Object.keys(DARK).forEach(function (k) {
      var c = mix(from[k], to[k], p);
      if (k === "sky2" || k === "sky1") c = mix(c, WARM, dawn);
      sec.style.setProperty("--" + (k === "pole" ? "flag-pole" : k), c);
    });
  }
  function place(day) { // day: 0..1
    var e = day;
    var sy = SUN_DOWN + (SUN_UP - SUN_DOWN) * e;
    var my = MOON_UP + (MOON_DOWN - MOON_UP) * e;
    sun.setAttribute("transform", "translate(" + sunX + " " + sy.toFixed(1) + ")");
    moon.setAttribute("transform", "translate(" + moonX + " " + my.toFixed(1) + ")");
    stars.style.opacity = String(Math.max(0, 1 - e * 1.5));
    clouds.style.opacity = String(Math.max(0, e * 1.3 - 0.3));
    sun.style.opacity = String(Math.min(1, e * 3));
    moon.style.opacity = String(Math.min(1, (1 - e) * 3));
  }
  function setStatic(light) {
    cur = light ? 1 : 0;
    paint(1, light ? LIGHT : DARK, light ? LIGHT : DARK);
    sec.style.setProperty("--sun", light ? LIGHT.sun : DARK.sun);
    place(cur);
  }
  function animateTo(light, onMid) {
    var target = light ? 1 : 0, start = cur === null ? (light ? 0 : 1) : cur;
    cancelAnimationFrame(raf);
    if (REDUCED || start === target) { if (onMid) onMid(); setStatic(light); return; }
    var from = target ? DARK : LIGHT, to = target ? LIGHT : DARK, t0 = null, dur = 1500;
    function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min(1, (ts - t0) / dur), e = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      if (onMid && p >= 0.4) { var f = onMid; onMid = null; f(); }
      paint(e, from, to);
      // quyosh/oy biroz kechikib harakatlanadi: avval oy tushadi, so'ng quyosh ko'tariladi
      var d = target ? e : 1 - e;
      place(d);
      cur = d;
      if (p < 1) raf = requestAnimationFrame(step); else { if (onMid) { onMid(); onMid = null; } setStatic(light); }
    }
    raf = requestAnimationFrame(step);
  }
  function fitView() {
    var W = window.innerWidth, H = window.innerHeight || 800;
    var vw = Math.min(1600, 900 * W / H), cx = vw >= 1600 ? 800 : Math.max(vw / 2, Math.min(1600 - vw / 2, 1010));
    svg.setAttribute("viewBox", (cx - vw / 2).toFixed(1) + " 0 " + vw.toFixed(1) + " 900");
    var L = cx - vw / 2;
    sunX = moonX = L + vw * (vw < 700 ? 0.72 : 0.47);
    place(cur === null ? 0 : cur);
  }
  window.addEventListener("resize", fitView);
  setStatic(isLight()); fitView();
  var internal = false;
  function flipTheme(next) {
    internal = true;
    document.documentElement.setAttribute("data-theme", next);
    try { localStorage.setItem("longouz_theme", next); } catch (e) {}
    Promise.resolve().then(function () { internal = false; });
  }
  // tugma bosilganda: avval osmon/quyosh/oy harakati boshlanadi, sayt ranglari o'rtasida almashadi
  document.addEventListener("click", function (e) {
    var t = e.target.closest && e.target.closest(".theme-toggle");
    if (!t) return;
    e.stopImmediatePropagation(); e.preventDefault();
    var next = isLight() ? "dark" : "light";
    animateTo(next === "light", function () { flipTheme(next); });
  }, true);
  new MutationObserver(function () { if (!internal) animateTo(isLight()); }).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
})();
