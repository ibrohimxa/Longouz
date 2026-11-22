/* v243: LongoAI javoblarini chiroyli ko'rsatish — window.LongoRender.
   * markdown (qalin, kursiv, ro'yxat, sarlavha, kod), * formulalar: $...$, $$...$$, \( \), \[ \] — KaTeX (kerak bo'lganda yuklanadi),
   * ```plot — funksiya grafigi (LZGraph), * ```svg — xavfsiz tozalangan SVG chizma.
   LongoRender.render(el, text, {streaming}) ; LongoRender.toSpeech(text) -> ovoz uchun toza matn. */
(function () {
  "use strict";
  var V = "246";
  var katexState = 0, katexWait = [];
  var texCache = {};

  function loadCss(href, key) {
    if (document.querySelector('link[data-lr="' + key + '"]')) return;
    var l = document.createElement("link"); l.rel = "stylesheet"; l.href = href; l.setAttribute("data-lr", key); document.head.appendChild(l);
  }
  function loadScript(src, key, cb) {
    var s = document.querySelector('script[data-lr="' + key + '"]');
    if (s) { if (s.dataset.ok) cb(); else s.addEventListener("load", cb); return; }
    s = document.createElement("script"); s.src = src; s.async = true; s.setAttribute("data-lr", key);
    s.addEventListener("load", function () { s.dataset.ok = "1"; cb(); });
    s.addEventListener("error", function () { s.dataset.ok = "1"; cb(); });
    document.head.appendChild(s);
  }
  function needKatex(cb) {
    if (window.katex) return cb();
    katexWait.push(cb);
    if (katexState) return;
    katexState = 1;
    loadCss("/static/vendor/katex/katex.min.css?v=" + V, "katex");
    loadScript("/static/vendor/katex/katex.min.js?v=" + V, "katex", function () { var w = katexWait; katexWait = []; w.forEach(function (f) { try { f(); } catch (e) {} }); });
  }
  loadCss("/static/longo-render.css?v=" + V, "lr");

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }

  // ---------------------------------------------------------------- LaTeX -> oddiy matn (KaTeX yuklanguncha / ovoz uchun)
  var SUP = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "-": "⁻", "+": "⁺", "n": "ⁿ" };
  var SUB = { "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉" };
  var SYM = { cdot: "·", times: "×", div: "÷", pm: "±", mp: "∓", le: "≤", leq: "≤", ge: "≥", geq: "≥", neq: "≠", ne: "≠", approx: "≈", infty: "∞",
    pi: "π", alpha: "α", beta: "β", gamma: "γ", delta: "δ", Delta: "Δ", theta: "θ", lambda: "λ", mu: "μ", sigma: "σ", omega: "ω", Omega: "Ω",
    phi: "φ", rho: "ρ", eta: "η", epsilon: "ε", varepsilon: "ε", tau: "τ", circ: "°", degree: "°", to: "→", rightarrow: "→", Rightarrow: "⇒",
    leftrightarrow: "↔", in: "∈", notin: "∉", cup: "∪", cap: "∩", subset: "⊂", emptyset: "∅", angle: "∠", perp: "⊥", parallel: "∥", triangle: "△",
    sum: "∑", int: "∫", partial: "∂", nabla: "∇", forall: "∀", exists: "∃", ldots: "…", cdots: "⋯", quad: " ", qquad: "  ", ",": " ", ";": " ", "!": "" };
  function texToText(t) {
    var s = String(t);
    for (var k = 0; k < 4; k++) {
      s = s.replace(/\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}/g, "($1)/($2)").replace(/\\frac(\d)(\d)/g, "$1/$2")
        .replace(/\\sqrt\s*\[(\d+)\]\s*\{([^{}]*)\}/g, function (m, n, x) { return (n === "3" ? "∛" : n === "4" ? "∜" : n + "√") + "(" + x + ")"; })
        .replace(/\\sqrt\s*\{([^{}]*)\}/g, "√($1)").replace(/\\sqrt\s*(\w)/g, "√$1")
        .replace(/\\(?:mathrm|text|textbf|mathbf|operatorname|mathit)\s*\{([^{}]*)\}/g, "$1").replace(/\\(?:left|right|big|Big)\s*/g, "");
    }
    s = s.replace(/\\([A-Za-z]+|[,;!])/g, function (m, w) { return SYM.hasOwnProperty(w) ? SYM[w] : (/^(sin|cos|tan|cot|log|ln|lg|lim|max|min|arcsin|arccos|arctg|tg|ctg)$/.test(w) ? w : ""); });
    s = s.replace(/\^\{([^{}]*)\}|\^(.)/g, function (m, a, b) { var x = a != null ? a : b; return /^[0-9n+\-]+$/.test(x) ? x.split("").map(function (c) { return SUP[c] || c; }).join("") : "^(" + x + ")"; });
    s = s.replace(/_\{([^{}]*)\}|_(.)/g, function (m, a, b) { var x = a != null ? a : b; return /^[0-9]+$/.test(x) ? x.split("").map(function (c) { return SUB[c] || c; }).join("") : "_" + x; });
    return s.replace(/[{}]/g, "").replace(/\s+/g, " ").trim();
  }
  function texHtml(tex, display) {
    var key = (display ? "D|" : "I|") + tex;
    if (texCache[key]) return texCache[key];
    if (window.katex) {
      try {
        var h = window.katex.renderToString(tex, { displayMode: !!display, throwOnError: false, strict: "ignore", trust: false, output: "html" });
        texCache[key] = h; return h;
      } catch (e) { /* oddiy matnga tushamiz */ }
    }
    return '<span class="lr-tex-fallback">' + esc(texToText(tex)) + "</span>";
  }

  // ---------------------------------------------------------------- SVG tozalash (faqat xavfsiz teglar)
  var OK_TAG = { svg: 1, g: 1, path: 1, line: 1, polyline: 1, polygon: 1, rect: 1, circle: 1, ellipse: 1, text: 1, tspan: 1, defs: 1, marker: 1, title: 1, lineargradient: 1, radialgradient: 1, stop: 1, pattern: 1, clippath: 1, use: 1 };
  var OK_ATTR = /^(viewbox|width|height|x|y|x1|x2|y1|y2|cx|cy|r|rx|ry|d|points|fill|stroke|stroke-width|stroke-dasharray|stroke-linecap|stroke-linejoin|opacity|fill-opacity|stroke-opacity|transform|font-size|font-weight|font-family|font-style|text-anchor|dominant-baseline|dx|dy|id|class|marker-end|marker-start|marker-mid|refx|refy|markerwidth|markerheight|orient|markerunits|offset|stop-color|stop-opacity|gradientunits|x1|preserveaspectratio|clip-path|letter-spacing|href|xmlns|patternunits|fill-rule)$/;
  function sanitizeSvg(src) {
    var m = String(src).match(/<svg[\s\S]*<\/svg>/i);
    if (!m) return null;
    var doc;
    try { doc = new DOMParser().parseFromString(m[0], "image/svg+xml"); } catch (e) { return null; }
    var root = doc.documentElement;
    if (!root || root.nodeName.toLowerCase() !== "svg" || doc.getElementsByTagName("parsererror").length) return null;
    (function walk(n) {
      Array.prototype.slice.call(n.childNodes).forEach(function (c) {
        if (c.nodeType === 1) {
          if (!OK_TAG[c.nodeName.toLowerCase()]) { n.removeChild(c); return; }
          Array.prototype.slice.call(c.attributes).forEach(function (a) {
            var nm = a.name.toLowerCase(), v = a.value;
            var hrefBad = (nm === "href" || nm === "xlink:href") && !/^#[\w-]+$/.test(v);
            if (hrefBad || (!OK_ATTR.test(nm) && nm !== "xlink:href") || /javascript:|url\((?!#)|expression\(/i.test(v)) c.removeAttribute(a.name);
          });
          walk(c);
        } else if (c.nodeType !== 3) n.removeChild(c);
      });
    })(root);
    Array.prototype.slice.call(root.attributes).forEach(function (a) { if (!OK_ATTR.test(a.name.toLowerCase())) root.removeAttribute(a.name); });
    if (!root.getAttribute("viewBox")) {
      var w = parseFloat(root.getAttribute("width")) || 320, h = parseFloat(root.getAttribute("height")) || 220;
      root.setAttribute("viewBox", "0 0 " + w + " " + h);
    }
    root.removeAttribute("width"); root.removeAttribute("height");
    root.setAttribute("class", "lr-svg");
    if (!root.getAttribute("fill")) root.setAttribute("fill", "none");
    return new XMLSerializer().serializeToString(root);
  }

  // ---------------------------------------------------------------- markdown (inline)
  function inline(s) {
    s = esc(s);
    s = s.replace(/`([^`\n]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*\n]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[\s(])\*([^*\n]+)\*(?=[\s).,!?:;]|$)/g, "$1<em>$2</em>")
      .replace(/(^|[\s(])_([^_\n]+)_(?=[\s).,!?:;]|$)/g, "$1<em>$2</em>");
    return s;
  }

  function render(el, text, opts) {
    opts = opts || {};
    var src = String(text || "").replace(/\r/g, "");
    var slots = [], hasMath = false, figs = [];
    function slot(html) { slots.push(html); return "\u0000" + (slots.length - 1) + "\u0000"; }
    // 1) kod bloklari (oqim paytida yopilmagan blok — «chizilmoqda»)
    src = src.replace(/```[ \t]*([\w-]*)[ \t]*\n([\s\S]*?)(```|$)/g, function (m, lang, body, close) {
      lang = (lang || "").toLowerCase();
      if (!close) return slot('<div class="lr-pending">' + (lang === "svg" || lang === "plot" ? "Chizma tayyorlanmoqda…" : "…") + "</div>");
      if (lang === "plot" || lang === "graph" || lang === "grafik") { figs.push({ type: "plot", body: body }); return slot('<div class="lr-fig lr-plot" data-fig="' + (figs.length - 1) + '"></div>'); }
      if (lang === "svg" || /^\s*<svg/i.test(body)) {
        var clean = sanitizeSvg(body);
        return slot(clean ? '<figure class="lr-fig">' + clean + "</figure>" : "");
      }
      return slot('<pre class="lr-pre"><code>' + esc(body.replace(/\n$/, "")) + "</code></pre>");
    });
    // 2) formulalar
    src = src.replace(/\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]/g, function (m, a, b) { hasMath = true; return slot('<div class="lr-math-d">' + texHtml((a || b).trim(), true) + "</div>"); });
    src = src.replace(/\\\(([\s\S]+?)\\\)/g, function (m, a) { hasMath = true; return slot('<span class="lr-math">' + texHtml(a.trim(), false) + "</span>"); });
    src = src.replace(/(^|[^\\$\w])\$([^\s$](?:[^$\n]*?[^\s$])?)\$(?!\d)/g, function (m, pre, a) { hasMath = true; return pre + slot('<span class="lr-math">' + texHtml(a, false) + "</span>"); });
    if (opts.streaming) src = src.replace(/\$\$[^$]*$|(^|[^\\$])\$[^$\n]*$/, function (m, p) { return (p || "") + slot('<span class="lr-pending-i">…</span>'); });
    // 3) bloklar: sarlavha, ro'yxat, xatboshi
    var lines = src.split("\n"), html = "", list = null, para = [];
    function flushPara() { if (para.length) { html += "<p>" + para.map(inline).join("<br>") + "</p>"; para = []; } }
    function flushList() { if (list) { html += "</" + list + ">"; list = null; } }
    lines.forEach(function (ln) {
      var t = ln.trim(), m;
      if (!t) { flushPara(); flushList(); return; }
      if (/^\u0000\d+\u0000$/.test(t) && /lr-(fig|math-d|pre|pending)/.test(slots[+t.slice(1, -1)] || "")) { flushPara(); flushList(); html += t; return; }
      if ((m = t.match(/^(#{1,4})\s+(.*)$/))) { flushPara(); flushList(); html += '<h4 class="lr-h">' + inline(m[2]) + "</h4>"; return; }
      if ((m = t.match(/^[-*•]\s+(.*)$/))) { flushPara(); if (list !== "ul") { flushList(); html += "<ul>"; list = "ul"; } html += "<li>" + inline(m[1]) + "</li>"; return; }
      if ((m = t.match(/^(\d+)[.)]\s+(.*)$/))) { flushPara(); if (list !== "ol") { flushList(); html += '<ol start="' + m[1] + '">'; list = "ol"; } html += "<li>" + inline(m[2]) + "</li>"; return; }
      flushList(); para.push(t);
    });
    flushPara(); flushList();
    html = html.replace(/\u0000(\d+)\u0000/g, function (m, i) { return slots[+i]; });
    el.classList.add("lr");
    el.innerHTML = html;
    // grafiklar
    figs.forEach(function (f, i) {
      var host = el.querySelector('[data-fig="' + i + '"]');
      if (!host) return;
      if (window.LZGraph) window.LZGraph.draw(host, f.body, {});
      else loadScript("/static/lz-graph.js?v=" + V, "lzgraph", function () { if (window.LZGraph) window.LZGraph.draw(host, f.body, {}); });
    });
    if (hasMath && !window.katex) needKatex(function () { if (el.isConnected) render(el, text, opts); });
  }

  function toSpeech(text) {
    var s = String(text || "").replace(/```[\s\S]*?(```|$)/g, " (chizmani ekranda ko'ring) ");
    s = s.replace(/\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)|\$([^$\n]+)\$/g, function (m, a, b, c, d) { return " " + texToText(a || b || c || d) + " "; });
    s = s.replace(/√\(([^)]*)\)/g, "ildiz ostida $1").replace(/√/g, "ildiz ").replace(/²/g, " kvadrat").replace(/³/g, " kub").replace(/π/g, "pi")
      .replace(/≤/g, " kichik yoki teng ").replace(/≥/g, " katta yoki teng ").replace(/≠/g, " teng emas ").replace(/·|×/g, " ko'paytirilgan ").replace(/°/g, " gradus");
    return s.replace(/\*\*|__|`|^#+\s*/gm, "").replace(/^\s*[-*•]\s+/gm, "").replace(/\s+/g, " ").trim();
  }

  window.LongoRender = { render: render, toSpeech: toSpeech, texToText: texToText, sanitizeSvg: sanitizeSvg, preloadMath: function () { needKatex(function () {}); } };
})();
