/* v243: LongoUZ funksiya grafigi chizgich — window.LZGraph (LZCalc dvigatelidan foydalanadi, eval yo'q).
   LZGraph.parseSpec("y = x^2 - 4\ny = 2x+1\nx: -5..5") -> {fns, xmin, xmax, ymin, ymax}
   LZGraph.draw(el, spec, {interactive:true}) -> SVG grafik: o'qlar, panjara, egri chiziqlar, nollar va kesishish nuqtalari. */
(function () {
  "use strict";
  var COLORS = ["#1def6a", "#c6ff3d", "#00e0a4", "#9dffbf", "#0bd855", "#5effc0"];
  var NS = "http://www.w3.org/2000/svg";

  function loadCalc(cb) {
    if (window.LZCalc) return cb();
    var s = document.querySelector('script[data-lzcalc]');
    if (!s) {
      s = document.createElement("script");
      s.src = "/static/calc-engine.js?v=246"; s.setAttribute("data-lzcalc", "1");
      document.head.appendChild(s);
    }
    s.addEventListener("load", function () { cb(); });
  }

  function parseSpec(src) {
    var spec = { fns: [], xmin: -6, xmax: 6, ymin: null, ymax: null, points: [] };
    String(src || "").split(/\n|;(?![^()]*\))/).forEach(function (line) {
      var l = line.trim();
      if (!l) return;
      var m = l.match(/^x\s*[:∈]\s*\[?\s*(-?[\d.]+)\s*(?:\.\.|,|;|…)\s*(-?[\d.]+)\s*\]?$/i);
      if (m) { spec.xmin = +m[1]; spec.xmax = +m[2]; return; }
      m = l.match(/^y\s*[:∈]\s*\[?\s*(-?[\d.]+)\s*(?:\.\.|,|;|…)\s*(-?[\d.]+)\s*\]?$/i);
      if (m) { spec.ymin = +m[1]; spec.ymax = +m[2]; return; }
      m = l.match(/^(?:nuqta|point|p)\s*[:=]?\s*\(?\s*(-?[\d.]+)\s*[,;]\s*(-?[\d.]+)\s*\)?\s*(.*)$/i);
      if (m) { spec.points.push({ x: +m[1], y: +m[2], label: m[3] || "" }); return; }
      var expr = l.replace(/^(?:y|[a-z]\s*\(\s*x\s*\))\s*=\s*/i, "");
      if (/x/i.test(expr) || /^[-+\d.\s*/^()]+$/.test(expr)) spec.fns.push({ src: l, expr: expr });
    });
    if (!(spec.xmax > spec.xmin)) { spec.xmin = -6; spec.xmax = 6; }
    return spec;
  }

  function compile(expr) {
    var C = window.LZCalc;
    var ast = C.parse(C.normalize(expr));
    return function (x) {
      try { var v = C.evalAst(ast, { vars: { x: x }, deg: false, ans: 0 }); return typeof v === "number" ? v : NaN; } catch (e) { return NaN; }
    };
  }

  function niceStep(span, target) {
    var raw = span / target, p = Math.pow(10, Math.floor(Math.log10(raw))), n = raw / p;
    return (n < 1.5 ? 1 : n < 3 ? 2 : n < 7 ? 5 : 10) * p;
  }
  function fmtN(v) { var r = Math.round(v * 1000) / 1000; return String(r).replace(".", ","); }

  function draw(host, spec, opts) {
    opts = opts || {};
    if (!window.LZCalc) { host.textContent = "Grafik yuklanmoqda…"; return loadCalc(function () { draw(host, spec, opts); }); }
    if (typeof spec === "string") spec = parseSpec(spec);
    var W = opts.width || 340, H = opts.height || 240, pad = 26;
    var fns = [];
    spec.fns.forEach(function (f, i) { try { fns.push({ f: compile(f.expr), src: f.src, c: COLORS[i % COLORS.length] }); } catch (e) { /* noto'g'ri ifoda */ } });
    if (!fns.length) { host.textContent = "Grafik uchun funksiya topilmadi."; return; }
    var xmin = spec.xmin, xmax = spec.xmax, N = 360, samples = [];
    fns.forEach(function (F) {
      var arr = [];
      for (var i = 0; i <= N; i++) { var x = xmin + (xmax - xmin) * i / N; arr.push([x, F.f(x)]); }
      samples.push(arr);
    });
    var ymin = spec.ymin, ymax = spec.ymax;
    if (ymin == null || ymax == null) {
      var ys = [];
      samples.forEach(function (a) { a.forEach(function (p) { if (isFinite(p[1])) ys.push(p[1]); }); });
      ys.sort(function (a, b) { return a - b; });
      var lo = ys.length ? ys[Math.floor(ys.length * 0.03)] : -5, hi = ys.length ? ys[Math.ceil(ys.length * 0.97) - 1] : 5;
      lo = Math.min(lo, 0); hi = Math.max(hi, 0);
      if (hi - lo < 1e-9) { hi += 1; lo -= 1; }
      var m = (hi - lo) * 0.12; ymin = lo - m; ymax = hi + m;
    }
    function X(x) { return pad + (x - xmin) / (xmax - xmin) * (W - 2 * pad); }
    function Y(y) { return H - pad - (y - ymin) / (ymax - ymin) * (H - 2 * pad); }
    var svg = document.createElementNS(NS, "svg");
    svg.setAttribute("viewBox", "0 0 " + W + " " + H);
    svg.setAttribute("class", "lzg-svg");
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", "Grafik: " + fns.map(function (F) { return F.src; }).join(", "));
    var out = "";
    var sx = niceStep(xmax - xmin, 8), sy = niceStep(ymax - ymin, 6);
    for (var gx = Math.ceil(xmin / sx) * sx; gx <= xmax + 1e-9; gx += sx) {
      out += '<line class="lzg-grid" x1="' + X(gx) + '" x2="' + X(gx) + '" y1="' + pad + '" y2="' + (H - pad) + '"/>';
      if (Math.abs(gx) > 1e-9) out += '<text class="lzg-tick" x="' + X(gx) + '" y="' + Math.min(H - pad + 12, Math.max(pad + 10, Y(0) + 12)) + '" text-anchor="middle">' + fmtN(gx) + "</text>";
    }
    for (var gy = Math.ceil(ymin / sy) * sy; gy <= ymax + 1e-9; gy += sy) {
      out += '<line class="lzg-grid" y1="' + Y(gy) + '" y2="' + Y(gy) + '" x1="' + pad + '" x2="' + (W - pad) + '"/>';
      if (Math.abs(gy) > 1e-9) out += '<text class="lzg-tick" y="' + (Y(gy) + 3) + '" x="' + Math.min(W - pad - 2, Math.max(pad + 2, X(0) - 4)) + '" text-anchor="end">' + fmtN(gy) + "</text>";
    }
    if (ymin < 0 && ymax > 0) out += '<line class="lzg-axis" x1="' + pad + '" x2="' + (W - pad + 6) + '" y1="' + Y(0) + '" y2="' + Y(0) + '" marker-end="url(#lzgA)"/><text class="lzg-lab" x="' + (W - pad + 4) + '" y="' + (Y(0) - 6) + '">x</text>';
    if (xmin < 0 && xmax > 0) out += '<line class="lzg-axis" y1="' + (H - pad) + '" y2="' + (pad - 6) + '" x1="' + X(0) + '" x2="' + X(0) + '" marker-end="url(#lzgA)"/><text class="lzg-lab" x="' + (X(0) + 6) + '" y="' + (pad - 2) + '">y</text>';
    if (xmin < 0 && xmax > 0 && ymin < 0 && ymax > 0) out += '<text class="lzg-tick" x="' + (X(0) - 4) + '" y="' + (Y(0) + 12) + '" text-anchor="end">0</text>';
    var marks = "";
    samples.forEach(function (arr, k) {
      var d = "", pen = false, prev = null;
      arr.forEach(function (p) {
        var ok = isFinite(p[1]) && p[1] > ymin - (ymax - ymin) * 3 && p[1] < ymax + (ymax - ymin) * 3;
        if (ok && prev && Math.abs(p[1] - prev[1]) > (ymax - ymin) * 1.5) ok = false;  // uzilish (masalan 1/x)
        if (ok) { d += (pen ? "L" : "M") + X(p[0]).toFixed(1) + " " + Y(Math.max(ymin - (ymax - ymin), Math.min(ymax + (ymax - ymin), p[1]))).toFixed(1); pen = true; }
        else pen = false;
        prev = isFinite(p[1]) ? p : null;
      });
      out += '<path class="lzg-fn" d="' + d + '" stroke="' + fns[k].c + '"/>';
      // nollar (y=0)
      for (var i = 1; i < arr.length; i++) {
        var a = arr[i - 1], b = arr[i];
        if (isFinite(a[1]) && isFinite(b[1]) && (a[1] === 0 || a[1] * b[1] < 0) && Math.abs(a[1] - b[1]) < (ymax - ymin)) {
          var x0 = a[1] === 0 ? a[0] : a[0] - a[1] * (b[0] - a[0]) / (b[1] - a[1]);
          marks += '<circle class="lzg-pt" cx="' + X(x0) + '" cy="' + Y(0) + '" r="3.5" fill="' + fns[k].c + '"><title>(' + fmtN(x0) + "; 0)</title></circle>";
        }
      }
    });
    (spec.points || []).forEach(function (p) {
      marks += '<circle class="lzg-pt" cx="' + X(p.x) + '" cy="' + Y(p.y) + '" r="4" fill="#c6ff3d"/><text class="lzg-lab" x="' + (X(p.x) + 6) + '" y="' + (Y(p.y) - 6) + '">' + (p.label ? p.label.replace(/[<>&]/g, "") + " " : "") + "(" + fmtN(p.x) + "; " + fmtN(p.y) + ")</text>";
    });
    svg.innerHTML = '<defs><marker id="lzgA" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L8 4L0 8z" fill="currentColor"/></marker></defs>' + out + marks +
      '<line class="lzg-cross" y1="' + pad + '" y2="' + (H - pad) + '" x1="-9" x2="-9"/><g class="lzg-tip" visibility="hidden"><rect rx="5" height="18"/><text y="13"></text></g>';
    host.innerHTML = "";
    host.classList.add("lzg");
    host.appendChild(svg);
    var leg = document.createElement("div");
    leg.className = "lzg-legend";
    leg.innerHTML = fns.map(function (F) { return '<span><i style="background:' + F.c + '"></i>' + F.src.replace(/[<>&]/g, "") + "</span>"; }).join("");
    host.appendChild(leg);
    if (opts.interactive === false) return;
    var cross = svg.querySelector(".lzg-cross"), tip = svg.querySelector(".lzg-tip"), tt = tip.querySelector("text"), tr = tip.querySelector("rect");
    function move(ev) {
      var r = svg.getBoundingClientRect(), cx = ((ev.touches ? ev.touches[0].clientX : ev.clientX) - r.left) / r.width * W;
      if (cx < pad || cx > W - pad) { tip.setAttribute("visibility", "hidden"); return; }
      var x = xmin + (cx - pad) / (W - 2 * pad) * (xmax - xmin), y = fns[0].f(x);
      cross.setAttribute("x1", cx); cross.setAttribute("x2", cx);
      tt.textContent = "x=" + fmtN(x) + "  y=" + (isFinite(y) ? fmtN(y) : "—");
      var tw = tt.textContent.length * 6.4 + 10, tx = Math.min(W - tw - 2, cx + 6);
      tr.setAttribute("x", tx); tr.setAttribute("width", tw); tt.setAttribute("x", tx + 5);
      tip.setAttribute("transform", "translate(0," + (pad - 4) + ")");
      tip.setAttribute("visibility", "visible");
    }
    svg.addEventListener("mousemove", move);
    svg.addEventListener("touchmove", move, { passive: true });
    svg.addEventListener("mouseleave", function () { tip.setAttribute("visibility", "hidden"); cross.setAttribute("x1", -9); cross.setAttribute("x2", -9); });
  }

  window.LZGraph = { parseSpec: parseSpec, draw: draw, load: loadCalc };
})();
