// LongoUZ — savol chizmalari renderi (Dekart koordinatalari, geometrik shakllar, rasm, SVG).
// Spetsifikatsiya formati figures.py da tavsiflangan. Test, natija va admin tahrirlagichda bir xil ishlaydi.
(function (global) {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var COLORS = ["#4A9EFF", "#FFA726", "#2FBF83", "#F85149", "#B388FF", "#26C6DA"];

  function el(name, attrs, parent) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) if (attrs[k] != null) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  function niceStep(range, target) {
    var raw = range / target, p = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10)), f = raw / p;
    return (f < 1.5 ? 1 : f < 3.5 ? 2 : f < 7.5 ? 5 : 10) * p;
  }
  function fmt(n) { return String(Math.round(n * 1000) / 1000).replace("-", "−"); }

  // Xavfsiz ifoda tahlilchisi (eval/Function ishlatilmaydi): + - * / ^, qavslar, x, pi, e, sin cos tan sqrt abs log ln exp asin acos atan
  var FUNCS = { sin: Math.sin, cos: Math.cos, tan: Math.tan, sqrt: Math.sqrt, abs: Math.abs, log: Math.log10, ln: Math.log, exp: Math.exp, asin: Math.asin, acos: Math.acos, atan: Math.atan };
  function compileFn(expr) {
    var src = String(expr).toLowerCase().replace(/\s+/g, ""), pos = 0, tokens = [], m, re = /(\d+\.?\d*|\.\d+)|([a-z]+)|([-+*\/^(),])/g;
    while ((m = re.exec(src)) !== null) tokens.push(m[1] != null ? { n: parseFloat(m[1]) } : m[2] != null ? { id: m[2] } : { op: m[3] });
    if (!tokens.length || tokens.map(function (t) { return t.n != null ? String(t.n) : t.id || t.op; }).join("").length < src.replace(/\./g, "").length - 4) return null;
    function peek() { return tokens[pos]; }
    function isOp(o) { return tokens[pos] && tokens[pos].op === o; }
    function expr_() { var l = term_(); while (isOp("+") || isOp("-")) { var o = tokens[pos++].op, r = term_(); l = bin(o, l, r); } return l; }
    function bin(o, l, r) { return o === "+" ? function (x) { return l(x) + r(x); } : o === "-" ? function (x) { return l(x) - r(x); } : o === "*" ? function (x) { return l(x) * r(x); } : o === "/" ? function (x) { return l(x) / r(x); } : function (x) { return Math.pow(l(x), r(x)); }; }
    function startsFactor() { var t = peek(); return t && (t.n != null || t.id || t.op === "("); }
    function term_() { var l = unary_(); for (;;) { if (isOp("*") || isOp("/")) { var o = tokens[pos++].op, r = unary_(); l = bin(o, l, r); } else if (startsFactor()) { var r2 = unary_(); l = bin("*", l, r2); } else break; } return l; }
    function unary_() { if (isOp("-")) { pos++; var u = unary_(); return function (x) { return -u(x); }; } if (isOp("+")) { pos++; return unary_(); } return pow_(); }
    function pow_() { var b = atom_(); if (isOp("^")) { pos++; var e = unary_(); return bin("^", b, e); } return b; }
    function atom_() {
      var t = tokens[pos++]; if (!t) throw new Error("x");
      if (t.n != null) return function () { return t.n; };
      if (t.op === "(") { var v = expr_(); if (!isOp(")")) throw new Error("x"); pos++; return v; }
      if (t.id === "x") return function (x) { return x; };
      if (t.id === "pi") return function () { return Math.PI; };
      if (t.id === "e") return function () { return Math.E; };
      if (FUNCS[t.id]) { if (!isOp("(")) throw new Error("x"); pos++; var a = expr_(); if (!isOp(")")) throw new Error("x"); pos++; var f = FUNCS[t.id]; return function (x) { return f(a(x)); }; }
      throw new Error("x");
    }
    try { var fn = expr_(); return pos === tokens.length ? fn : null; } catch (e) { return null; }
  }

  function renderPlane(spec) {
    var xmin = spec.xmin, xmax = spec.xmax, ymin = spec.ymin, ymax = spec.ymax;
    var xr = xmax - xmin, yr = ymax - ymin;
    var W = 480, H = Math.max(140, Math.min(560, Math.round(W * yr / xr)));
    var sx = function (x) { return (x - xmin) / xr * W; };
    var sy = function (y) { return H - (y - ymin) / yr * H; };
    var svg = el("svg", { viewBox: "0 0 " + W + " " + H, "class": "lzf-svg", role: "img", preserveAspectRatio: "xMidYMid meet" });
    var defs = el("defs", {}, svg);
    var mk = el("marker", { id: "lzf-arr", markerWidth: 8, markerHeight: 8, refX: 6, refY: 4, orient: "auto" }, defs);
    el("path", { d: "M0,0 L8,4 L0,8 z", fill: "currentColor" }, mk);
    var clipId = "lzf-clip-" + Math.random().toString(36).slice(2, 8);
    var clip = el("clipPath", { id: clipId }, defs);
    el("rect", { x: 0, y: 0, width: W, height: H }, clip);

    if (spec.grid) {
      var gx = niceStep(xr, 10), gy = niceStep(yr, 10 * yr / xr * (W / H) > 3 ? 10 : 8);
      var g = el("g", { "class": "lzf-grid" }, svg);
      for (var x = Math.ceil(xmin / gx) * gx; x <= xmax + 1e-9; x += gx) el("line", { x1: sx(x), y1: 0, x2: sx(x), y2: H }, g);
      for (var y = Math.ceil(ymin / gy) * gy; y <= ymax + 1e-9; y += gy) el("line", { x1: 0, y1: sy(y), x2: W, y2: sy(y) }, g);
    }
    if (spec.axes) {
      var ax = el("g", { "class": "lzf-axes" }, svg);
      var x0 = Math.min(Math.max(0, xmin), xmax), y0 = Math.min(Math.max(0, ymin), ymax);
      el("line", { x1: 0, y1: sy(y0), x2: W - 2, y2: sy(y0), "marker-end": "url(#lzf-arr)" }, ax);
      el("line", { x1: sx(x0), y1: H, x2: sx(x0), y2: 2, "marker-end": "url(#lzf-arr)" }, ax);
      var tx = el("text", { x: W - 6, y: sy(y0) - 6, "class": "lzf-axname", "text-anchor": "end" }, ax); tx.textContent = "x";
      var ty = el("text", { x: sx(x0) + 7, y: 12, "class": "lzf-axname" }, ax); ty.textContent = "y";
      var tg = el("g", { "class": "lzf-ticks" }, svg);
      var stx = niceStep(xr, 8), sty = niceStep(yr, 8);
      for (var a = Math.ceil(xmin / stx) * stx; a <= xmax + 1e-9; a += stx) {
        if (Math.abs(a) < 1e-9) continue;
        el("line", { x1: sx(a), y1: sy(y0) - 3, x2: sx(a), y2: sy(y0) + 3 }, tg);
        var t = el("text", { x: sx(a), y: Math.min(H - 3, sy(y0) + 14), "text-anchor": "middle" }, tg); t.textContent = fmt(a);
      }
      for (var b = Math.ceil(ymin / sty) * sty; b <= ymax + 1e-9; b += sty) {
        if (Math.abs(b) < 1e-9) continue;
        el("line", { x1: sx(x0) - 3, y1: sy(b), x2: sx(x0) + 3, y2: sy(b) }, tg);
        var t2 = el("text", { x: Math.max(14, sx(x0) - 7), y: sy(b) + 4, "text-anchor": "end" }, tg); t2.textContent = fmt(b);
      }
      var o = el("text", { x: sx(x0) - 6, y: sy(y0) + 13, "text-anchor": "end", "class": "lzf-axname" }, tg); o.textContent = "O";
    }

    var body = el("g", { "clip-path": "url(#" + clipId + ")" }, svg);
    var over = el("g", {}, svg);
    var ci = 0;
    function label(text, x, y, color, dx, dy) {
      if (!text) return;
      var t = el("text", { x: sx(x) + (dx == null ? 7 : dx), y: sy(y) + (dy == null ? -7 : dy), "class": "lzf-label", fill: color || null }, over);
      t.textContent = text;
    }
    (spec.items || []).forEach(function (it) {
      var color = it.c || COLORS[ci % COLORS.length], dash = it.dash ? "6 4" : null;
      if (it.k === "fn") {
        var f = compileFn(it.f); if (!f) return;
        var d = "", pen = false, steps = 240, last = null;
        for (var i = 0; i <= steps; i++) {
          var x = xmin + xr * i / steps, y;
          try { y = f(x); } catch (e) { y = NaN; }
          if (!isFinite(y) || Math.abs(y) > yr * 40 || (last != null && Math.abs(y - last) > yr * 3)) { pen = false; last = null; continue; }
          d += (pen ? "L" : "M") + sx(x).toFixed(1) + "," + sy(y).toFixed(1); pen = true; last = y;
        }
        el("path", { d: d, "class": "lzf-stroke", stroke: color, fill: "none" }, body); ci++;
      } else if (it.k === "line") {
        var x1 = it.x1, y1 = it.y1, x2 = it.x2, y2 = it.y2;
        if (it.ext && (x1 !== x2 || y1 !== y2)) {
          var dx = x2 - x1, dy = y2 - y1, n = Math.max(xr, yr) * 4 / Math.hypot(dx, dy);
          x1 -= dx * n; y1 -= dy * n; x2 += dx * n; y2 += dy * n;
        }
        el("line", { x1: sx(x1), y1: sy(y1), x2: sx(x2), y2: sy(y2), "class": "lzf-stroke", stroke: color, "stroke-dasharray": dash, "marker-end": it.arrow ? "url(#lzf-arr)" : null, style: "color:" + color }, body);
        label(it.l, (it.x1 + it.x2) / 2, (it.y1 + it.y2) / 2, color); ci++;
      } else if (it.k === "circle") {
        el("circle", { cx: sx(it.cx), cy: sy(it.cy), r: it.r / xr * W, "class": "lzf-stroke", stroke: color, fill: it.fill ? color : "none", "fill-opacity": it.fill ? 0.18 : null, "stroke-dasharray": dash }, body);
        label(it.l, it.cx + it.r * 0.7, it.cy + it.r * 0.7, color); ci++;
      } else if (it.k === "arc") {
        var rr = it.r / xr * W, a1 = it.a1 * Math.PI / 180, a2 = it.a2 * Math.PI / 180;
        var px1 = sx(it.cx) + rr * Math.cos(a1), py1 = sy(it.cy) - rr * Math.sin(a1);
        var px2 = sx(it.cx) + rr * Math.cos(a2), py2 = sy(it.cy) - rr * Math.sin(a2);
        var large = Math.abs(it.a2 - it.a1) % 360 > 180 ? 1 : 0, sweep = it.a2 > it.a1 ? 0 : 1;
        el("path", { d: "M" + px1 + "," + py1 + " A" + rr + "," + rr + " 0 " + large + " " + sweep + " " + px2 + "," + py2, "class": "lzf-stroke", stroke: color, fill: "none" }, body);
        var mid = (a1 + a2) / 2; label(it.l, it.cx + it.r * 1.25 * Math.cos(mid), it.cy + it.r * 1.25 * Math.sin(mid), color, -4, 4); ci++;
      } else if (it.k === "poly") {
        var pts = it.pts.map(function (p) { return sx(p[0]).toFixed(1) + "," + sy(p[1]).toFixed(1); }).join(" ");
        el(it.closed === false ? "polyline" : "polygon", { points: pts, "class": "lzf-stroke", stroke: color, fill: it.fill ? color : "none", "fill-opacity": it.fill ? 0.18 : null, "stroke-dasharray": dash, "stroke-linejoin": "round" }, body);
        var cx = 0, cy = 0; it.pts.forEach(function (p) { cx += p[0]; cy += p[1]; }); cx /= it.pts.length; cy /= it.pts.length;
        (it.names || []).forEach(function (nm, i) {
          var p = it.pts[i]; if (!p || !nm) return;
          var vx = p[0] - cx, vy = p[1] - cy, len = Math.hypot(vx, vy) || 1;
          var t = el("text", { x: sx(p[0]) + vx / len * 12, y: sy(p[1]) - vy / len * 12 + 4, "class": "lzf-label", "text-anchor": "middle" }, over); t.textContent = nm;
        });
        ci++;
      } else if (it.k === "pt") {
        el("circle", { cx: sx(it.x), cy: sy(it.y), r: 3.6, fill: color, "class": "lzf-pt" }, over);
        label(it.l, it.x, it.y, null); ci++;
      } else if (it.k === "text") {
        var tt = el("text", { x: sx(it.x), y: sy(it.y), "class": "lzf-label", fill: it.c || null }, over); tt.textContent = it.t;
      }
    });
    return svg;
  }

  function render(spec) {
    var wrap = document.createElement("div");
    wrap.className = "lzf";
    if (!spec || typeof spec !== "object") return wrap;
    try {
      if (spec.type === "plane") wrap.appendChild(renderPlane(spec));
      else if (spec.type === "image") {
        var img = document.createElement("img"); img.src = spec.src; img.alt = spec.alt || "Chizma"; img.loading = "lazy"; img.className = "lzf-img"; wrap.appendChild(img);
      } else if (spec.type === "svg") {
        wrap.innerHTML = spec.svg; var s = wrap.querySelector("svg"); if (s) s.setAttribute("class", "lzf-svg");
      }
    } catch (e) { wrap.textContent = ""; }
    return wrap;
  }

  // Savol hujjati bo'yicha: savol chizmasini konteynerga qo'yadi
  function fillQuestion(host, doc) {
    if (!host) return;
    host.innerHTML = "";
    var q = doc && doc.q;
    host.hidden = !q;
    if (q) { var f = render(q); if (doc.w && doc.w < 100) f.style.maxWidth = doc.w + "%"; host.appendChild(f); }
  }
  function optionFigure(doc, idx) { return doc && doc.o && doc.o[idx] ? render(doc.o[idx]) : null; }

  global.LZFigure = { render: render, fillQuestion: fillQuestion, optionFigure: optionFigure, compileFn: compileFn };
})(window);
