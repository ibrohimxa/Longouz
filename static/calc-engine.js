/* LongoUZ — kalkulyator dvigateli (eval ishlatilmaydi): ifoda tahlilchisi, tenglama yechuvchi, kimyoviy formula,
   fizik doimiylar va formulalar. Brauzerda window.LZCalc, Node'da module.exports sifatida ishlaydi. */
(function (root) {
  "use strict";

  // ------------------------------------------------------------------ doimiylar
  var CONSTS = {
    pi: Math.PI, e: Math.E,
    g: 9.8, g10: 10, c: 3e8, G: 6.67e-11, kC: 9e9, eps0: 8.85e-12, mu0: 4 * Math.PI * 1e-7, h: 6.63e-34, qe: 1.6e-19,
    me: 9.11e-31, mp: 1.67e-27, mn: 1.675e-27, NA: 6.02e23, R: 8.31, kB: 1.38e-23, sigma: 5.67e-8, patm: 101325,
    Vm: 22.4, Rz: 6.4e6, Mz: 6e24, amu: 1.66e-27
  };
  var CONST_INFO = [
    ["g", "Erkin tushish tezlanishi", "9,8 m/s²"], ["g10", "g (yaxlitlangan)", "10 m/s²"], ["c", "Yorug'lik tezligi", "3·10⁸ m/s"],
    ["G", "Gravitatsiya doimiysi", "6,67·10⁻¹¹ N·m²/kg²"], ["kC", "Kulon doimiysi k", "9·10⁹ N·m²/C²"], ["eps0", "Elektr doimiysi ε₀", "8,85·10⁻¹² F/m"],
    ["mu0", "Magnit doimiysi μ₀", "4π·10⁻⁷ H/m"], ["h", "Plank doimiysi", "6,63·10⁻³⁴ J·s"], ["qe", "Elementar zaryad e", "1,6·10⁻¹⁹ C"],
    ["me", "Elektron massasi", "9,11·10⁻³¹ kg"], ["mp", "Proton massasi", "1,67·10⁻²⁷ kg"], ["NA", "Avogadro soni", "6,02·10²³ mol⁻¹"],
    ["R", "Universal gaz doimiysi", "8,31 J/(mol·K)"], ["kB", "Boltsman doimiysi", "1,38·10⁻²³ J/K"], ["sigma", "Stefan–Boltsman", "5,67·10⁻⁸ W/(m²·K⁴)"],
    ["patm", "Normal atmosfera bosimi", "101325 Pa"], ["Vm", "Gazning molyar hajmi (n.sh.)", "22,4 l/mol"], ["Rz", "Yer radiusi", "6,4·10⁶ m"], ["Mz", "Yer massasi", "6·10²⁴ kg"]
  ];

  // ------------------------------------------------------------------ yordamchi
  var SUPMAP = { "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-", "⁺": "+" };
  var SUBMAP = { "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9" };

  function normalize(src) {
    var s = String(src == null ? "" : src);
    s = s.replace(/[×·⋅∙]/g, "*").replace(/÷/g, "/").replace(/[−–—]/g, "-").replace(/√/g, " sqrt ").replace(/∛/g, " cbrt ").replace(/π/g, " pi ").replace(/Δ/g, "D")
      .replace(/ /g, " ").replace(/，/g, ",");
    s = s.replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+/g, function (m) { return "^(" + m.split("").map(function (ch) { return SUPMAP[ch]; }).join("") + ")"; });
    s = s.replace(/[₀₁₂₃₄₅₆₇₈₉]/g, function (ch) { return SUBMAP[ch]; });
    return s;
  }

  function fact(n) {
    if (n < 0 || n !== Math.floor(n)) { if (n > -1) { return gamma(n + 1); } throw new Error("n! faqat n ≥ 0 uchun"); }
    if (n > 170) return Infinity;
    var r = 1; for (var i = 2; i <= n; i++) r *= i; return r;
  }
  function gamma(z) {                     // Lanczos
    var g = 7, c = [0.99999999999980993, 676.5203681218851, -1259.1392167224028, 771.32342877765313, -176.61502916214059, 12.507343278686905, -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
    if (z < 0.5) return Math.PI / (Math.sin(Math.PI * z) * gamma(1 - z));
    z -= 1; var x = c[0]; for (var i = 1; i < g + 2; i++) x += c[i] / (z + i);
    var t = z + g + 0.5; return Math.sqrt(2 * Math.PI) * Math.pow(t, z + 0.5) * Math.exp(-t) * x;
  }
  function gcd(a, b) { a = Math.abs(Math.round(a)); b = Math.abs(Math.round(b)); while (b) { var t = b; b = a % b; a = t; } return a; }
  function ncr(n, k) { if (k < 0 || k > n) return 0; k = Math.min(k, n - k); var r = 1; for (var i = 1; i <= k; i++) r = r * (n - k + i) / i; return Math.round(r); }
  function npr(n, k) { if (k < 0 || k > n) return 0; var r = 1; for (var i = 0; i < k; i++) r *= (n - i); return r; }

  // ------------------------------------------------------------------ tokenizer
  function tokenize(src) {
    var s = normalize(src), i = 0, out = [], parenStack = [];
    function isDigit(c) { return c >= "0" && c <= "9"; }
    function isAlpha(c) { return /[A-Za-z_Ѐ-ӿ]/.test(c); }
    while (i < s.length) {
      var c = s[i];
      if (c === " " || c === "\t" || c === "\n") { i++; continue; }
      if (isDigit(c) || (c === "." && isDigit(s[i + 1] || ""))) {
        var j = i, dec = false;
        while (j < s.length) {
          var d = s[j];
          if (isDigit(d)) { j++; continue; }
          if (d === "." && !dec) { dec = true; j++; continue; }
          if (d === "," && !dec && isDigit(s[j + 1] || "") && !(parenStack.length && parenStack[parenStack.length - 1])) { dec = true; j++; continue; }
          break;
        }
        var e0 = s[j];
        if ((e0 === "e" || e0 === "E") && (isDigit(s[j + 1] || "") || ((s[j + 1] === "-" || s[j + 1] === "+") && isDigit(s[j + 2] || "")))) {
          j += 2; while (isDigit(s[j] || "")) j++;
        }
        out.push({ t: "num", v: parseFloat(s.slice(i, j).replace(",", ".")) });
        i = j; continue;
      }
      if (isAlpha(c)) {
        var k = i; while (k < s.length && (isAlpha(s[k]) || isDigit(s[k]))) k++;
        var name = s.slice(i, k);
        // "sin30", "2pi" ... : raqamdan keyingi harflar alohida; "x2" -> x2 identifikator (foydalanuvchi o'zgaruvchisi)
        out.push({ t: "id", v: name });
        i = k; continue;
      }
      if (c === "(") { var isCall = out.length && out[out.length - 1].t === "id"; parenStack.push(!!isCall); out.push({ t: "(" }); i++; continue; }
      if (c === ")") { parenStack.pop(); out.push({ t: ")" }); i++; continue; }
      if (c === "[") { parenStack.push(false); out.push({ t: "(" }); i++; continue; }
      if (c === "]") { parenStack.pop(); out.push({ t: ")" }); i++; continue; }
      if (c === "," || c === ";") { out.push({ t: "," }); i++; continue; }
      if ("+-*/^!%=°".indexOf(c) >= 0) { out.push({ t: c }); i++; continue; }
      if (c === "<" || c === ">" ) { throw new Error("Tengsizlik qo'llab-quvvatlanmaydi"); }
      if (c === "|") { out.push({ t: "|" }); i++; continue; }
      throw new Error("Noma'lum belgi: " + c);
    }
    return out;
  }

  // ------------------------------------------------------------------ parser -> AST
  function parse(src) {
    var toks = tokenize(src), p = 0;
    function peek() { return toks[p]; }
    function next() { return toks[p++]; }
    function expect(t) { var x = next(); if (!x || x.t !== t) throw new Error("Ifoda noto'g'ri: '" + t + "' kutilgan edi"); return x; }
    function startsPrimary(x) { return x && (x.t === "num" || x.t === "id" || x.t === "(" || x.t === "|"); }

    function expr() {
      var l = term();
      while (peek() && (peek().t === "+" || peek().t === "-")) { var op = next().t; l = { k: "bin", op: op, l: l, r: term() }; }
      return l;
    }
    function term() {
      var l = unary();
      for (;;) {
        var x = peek();
        if (x && (x.t === "*" || x.t === "/")) { next(); l = { k: "bin", op: x.t, l: l, r: unary() }; }
        else if (startsPrimary(x) && !(x.t === "|")) { l = { k: "bin", op: "*", l: l, r: unary() }; }   // yashirin ko'paytirish: 2pi, 3(4+1)
        else break;
      }
      return l;
    }
    function unary() {
      var x = peek();
      if (x && x.t === "-") { next(); return { k: "neg", a: unary() }; }
      if (x && x.t === "+") { next(); return unary(); }
      return power();
    }
    function power() {
      var b = postfix();
      if (peek() && peek().t === "^") { next(); var e = unary(); return { k: "bin", op: "^", l: b, r: e }; }
      return b;
    }
    function postfix() {
      var a = primary();
      for (;;) {
        var x = peek();
        if (x && x.t === "!") { next(); a = { k: "fact", a: a }; }
        else if (x && x.t === "%") { next(); a = { k: "bin", op: "/", l: a, r: { k: "num", v: 100 } }; }
        else if (x && x.t === "°") { next(); a = { k: "deg", a: a }; }
        else break;
      }
      return a;
    }
    function primary() {
      var x = next();
      if (!x) throw new Error("Ifoda tugallanmagan");
      if (x.t === "num") return { k: "num", v: x.v };
      if (x.t === "(") { var e = expr(); expect(")"); return e; }
      if (x.t === "|") { var e2 = expr(); expect("|"); return { k: "call", f: "abs", args: [e2] }; }
      if (x.t === "id") {
        if (peek() && peek().t === "(") {
          next(); var args = [];
          if (peek() && peek().t !== ")") { args.push(expr()); while (peek() && peek().t === ",") { next(); args.push(expr()); } }
          expect(")");
          return { k: "call", f: x.v, args: args };
        }
        // sin 30, sqrt 9 kabi qavssiz yozuv
        if (FUNCS[x.v.toLowerCase()] && startsPrimary(peek()) && peek().t !== "|") { return { k: "call", f: x.v, args: [power()] }; }
        return { k: "var", n: x.v };
      }
      throw new Error("Kutilmagan belgi: " + x.t);
    }
    var ast = expr();
    if (p < toks.length) throw new Error("Ifodaning oxirida ortiqcha belgi bor");
    return ast;
  }

  // ------------------------------------------------------------------ hisoblash
  var FUNCS = {
    sqrt: 1, cbrt: 1, sin: 1, cos: 1, tan: 1, cot: 1, asin: 1, acos: 1, atan: 1, arcsin: 1, arccos: 1, arctan: 1, sinh: 1, cosh: 1, tanh: 1,
    ln: 1, log: 1, lg: 1, log2: 1, exp: 1, abs: 1, floor: 1, ceil: 1, round: 1, fact: 1, gcd: 1, lcm: 1, ncr: 1, npr: 1, max: 1, min: 1,
    hypot: 1, pow: 1, mod: 1, deg: 1, rad: 1, sign: 1, sgn: 1, root: 1, sec: 1, csc: 1
  };

  function evalAst(n, env) {
    switch (n.k) {
      case "num": return n.v;
      case "var": {
        if (Object.prototype.hasOwnProperty.call(env.vars, n.n)) return env.vars[n.n];
        if (Object.prototype.hasOwnProperty.call(CONSTS, n.n)) return CONSTS[n.n];
        var lc = n.n.toLowerCase();
        if (lc === "pi") return Math.PI;
        if (lc === "ans") return env.ans || 0;
        if (env.unknown) { env.unknown.add(n.n); return NaN; }
        throw new Error("Noma'lum o'zgaruvchi: " + n.n);
      }
      case "neg": return -evalAst(n.a, env);
      case "fact": return fact(evalAst(n.a, env));
      case "deg": return env.deg ? evalAst(n.a, env) : evalAst(n.a, env) * Math.PI / 180;
      case "bin": {
        var a = evalAst(n.l, env), b = evalAst(n.r, env);
        switch (n.op) {
          case "+": return a + b; case "-": return a - b; case "*": return a * b;
          case "/": return a / b;
          case "^": return (a < 0 && b !== Math.floor(b)) ? ((1 / b) % 2 !== 0 && Math.abs(1 / b - Math.round(1 / b)) < 1e-12 ? -Math.pow(-a, b) : NaN) : Math.pow(a, b);
        }
        break;
      }
      case "call": {
        var f = n.f.toLowerCase();
        var args = n.args.map(function (x) { return evalAst(x, env); });
        var A = args[0], toR = env.deg ? Math.PI / 180 : 1, fromR = env.deg ? 180 / Math.PI : 1;
        switch (f) {
          case "sqrt": return Math.sqrt(A);
          case "cbrt": return Math.cbrt(A);
          case "root": return args[1] ? (A < 0 && args[1] % 2 === 1 ? -Math.pow(-A, 1 / args[1]) : Math.pow(A, 1 / args[1])) : Math.sqrt(A);
          case "sin": return sinD(A * toR); case "cos": return cosD(A * toR);
          case "tan": return tanD(A * toR); case "cot": return 1 / tanD(A * toR);
          case "sec": return 1 / cosD(A * toR); case "csc": return 1 / sinD(A * toR);
          case "asin": case "arcsin": return Math.asin(A) * fromR;
          case "acos": case "arccos": return Math.acos(A) * fromR;
          case "atan": case "arctan": return Math.atan(A) * fromR;
          case "sinh": return Math.sinh(A); case "cosh": return Math.cosh(A); case "tanh": return Math.tanh(A);
          case "ln": return Math.log(A);
          case "lg": return Math.log10(A);
          case "log": return args.length > 1 ? Math.log(A) / Math.log(args[1]) : Math.log10(A);
          case "log2": return Math.log2(A);
          case "exp": return Math.exp(A);
          case "abs": return Math.abs(A);
          case "floor": return Math.floor(A); case "ceil": return Math.ceil(A);
          case "round": return args.length > 1 ? Math.round(A * Math.pow(10, args[1])) / Math.pow(10, args[1]) : Math.round(A);
          case "fact": return fact(A);
          case "gcd": return args.reduce(function (x, y) { return gcd(x, y); });
          case "lcm": return args.reduce(function (x, y) { return Math.abs(Math.round(x) * Math.round(y)) / (gcd(x, y) || 1); });
          case "ncr": return ncr(A, args[1]); case "npr": return npr(A, args[1]);
          case "max": return Math.max.apply(null, args); case "min": return Math.min.apply(null, args);
          case "hypot": return Math.hypot.apply(null, args);
          case "pow": return Math.pow(A, args[1]);
          case "mod": return ((A % args[1]) + args[1]) % args[1];
          case "deg": return A * 180 / Math.PI; case "rad": return A * Math.PI / 180;
          case "sign": case "sgn": return Math.sign(A);
        }
        throw new Error("Noma'lum funksiya: " + n.f);
      }
    }
    throw new Error("Hisoblab bo'lmadi");
  }
  // 90°, 180° kabi qiymatlarda aniq 0/1 chiqishi uchun
  function sinD(x) { var r = Math.sin(x); return Math.abs(r) < 1e-15 ? 0 : r; }
  function cosD(x) { var r = Math.cos(x); return Math.abs(r) < 1e-15 ? 0 : r; }
  function tanD(x) { var c = Math.cos(x); return Math.abs(c) < 1e-15 ? (Math.sin(x) > 0 ? Infinity : -Infinity) : Math.tan(x); }

  function collectUnknown(ast, env) {
    var set = new Set();
    var e2 = { vars: env.vars, deg: env.deg, ans: env.ans, unknown: set };
    try { evalAst(ast, e2); } catch (err) { /* o'zgaruvchi aniqlash uchun xatolarni e'tiborsiz */ }
    return Array.from(set);
  }

  // ------------------------------------------------------------------ tenglama yechuvchi (son usulida)
  function findRoots(f) {
    var roots = [];
    function add(x) { if (isFinite(x)) { for (var i = 0; i < roots.length; i++) { if (Math.abs(roots[i] - x) <= 1e-7 * Math.max(1, Math.abs(x))) return; } roots.push(x); } }
    function bis(a, b, fa, fb) {
      for (var i = 0; i < 200; i++) { var m = (a + b) / 2, fm = f(m); if (!isFinite(fm)) return null; if (fa * fm <= 0) { b = m; fb = fm; } else { a = m; fa = fm; } if (Math.abs(b - a) < 1e-15 * Math.max(1, Math.abs(a))) break; }
      return (a + b) / 2;
    }
    function scan(pts) {
      var prevX = null, prevF = null, absPrev = null, absPrev2 = null, xs = [], fs = [];
      for (var i = 0; i < pts.length; i++) { xs.push(pts[i]); fs.push(f(pts[i])); }
      for (i = 0; i < xs.length; i++) {
        var fx = fs[i];
        if (!isFinite(fx)) { prevF = null; continue; }
        if (fx === 0) add(xs[i]);
        if (prevF !== null && prevF * fx < 0) {
          var r = bis(xs[i - 1], xs[i], prevF, fx);
          if (r !== null && Math.abs(f(r)) < 1e-6 * Math.max(1, Math.abs(prevF), Math.abs(fx))) add(r);
        }
        prevF = fx;
      }
      // juft karrali ildizlar (parabola uchi): |f| lokal minimumi ≈ 0
      for (i = 1; i < xs.length - 1; i++) {
        var a = Math.abs(fs[i - 1]), b2 = Math.abs(fs[i]), c = Math.abs(fs[i + 1]);
        if (isFinite(a + b2 + c) && b2 <= a && b2 <= c && b2 > 0) {
          var lo = xs[i - 1], hi = xs[i + 1];
          for (var it = 0; it < 120; it++) { var m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3; if (Math.abs(f(m1)) < Math.abs(f(m2))) hi = m2; else lo = m1; }
          var xm = (lo + hi) / 2;
          if (Math.abs(f(xm)) < 1e-9 * Math.max(1, a, c)) add(xm);
        }
      }
    }
    var g1 = []; for (var k = -20000; k <= 20000; k++) g1.push(k * 0.005);          // [-100, 100]
    scan(g1);
    if (!roots.length) {
      var g2 = [];
      for (var e = -9; e <= 12; e += 0.05) { var v = Math.pow(10, e); g2.push(v); g2.push(-v); }
      g2.sort(function (a, b) { return a - b; });
      scan(g2);
    }
    roots = roots.map(function (r) { var rr = Math.round(r); return Math.abs(r - rr) < 1e-9 * Math.max(1, Math.abs(r)) ? rr : r; });
    roots.sort(function (a, b) { return a - b; });
    return roots;
  }

  function solveEquation(lhsAst, rhsAst, name, env) {
    var f = function (x) { var v = Object.assign({}, env.vars); v[name] = x; var e2 = { vars: v, deg: env.deg, ans: env.ans }; try { return evalAst(lhsAst, e2) - evalAst(rhsAst, e2); } catch (er) { return NaN; } };
    return findRoots(f);
  }

  // ------------------------------------------------------------------ formatlash
  function fmt(x, digits) {
    digits = digits || 10;
    if (typeof x !== "number") return String(x);
    if (isNaN(x)) return "aniqlanmagan";
    if (!isFinite(x)) return x > 0 ? "∞" : "−∞";
    if (x === 0) return "0";
    var ax = Math.abs(x);
    if (ax >= 1e12 || ax < 1e-6) {
      var s = x.toExponential(digits - 1).replace(/\.?0+e/, "e");
      var m = s.split("e"), ex = parseInt(m[1], 10);
      return m[0].replace(".", ",") + "·10" + String(ex).replace("-", "⁻").replace(/\d/g, function (d) { return "⁰¹²³⁴⁵⁶⁷⁸⁹"[d]; });
    }
    var r = parseFloat(x.toPrecision(digits));
    return String(r).replace(".", ",");
  }
  function plain(x) { return typeof x === "number" ? (isFinite(x) ? String(parseFloat(x.toPrecision(12))) : "") : String(x); }

  // ------------------------------------------------------------------ yuqori darajali kirish
  /* run(text, state): state = {vars, deg, ans}. Qaytaradi: {text, value, kind, state}. Ko'p operator: ';' emas — bir qatorga bir ifoda,
     lekin "a=3; b=4; a^2+b^2" kabi yozuv ham qabul qilinadi (oxirgi ifoda natija). */
  function run(text, state) {
    state = state || { vars: {}, deg: true, ans: 0 };
    var raw = String(text || "").trim();
    if (!raw) return { text: "", kind: "empty" };
    var parts = splitStatements(raw), last = null;
    for (var i = 0; i < parts.length; i++) {
      var part = parts[i].trim(); if (!part) continue;
      last = runOne(part, state);
      if (last.kind === "error") return last;
    }
    return last || { text: "", kind: "empty" };
  }
  function splitStatements(raw) {
    var depth = 0, cur = "", out = [];
    for (var i = 0; i < raw.length; i++) {
      var c = raw[i];
      if (c === "(" || c === "[") depth++; else if (c === ")" || c === "]") depth--;
      if ((c === ";" || c === "\n") && depth <= 0) { out.push(cur); cur = ""; } else cur += c;
    }
    out.push(cur); return out;
  }
  function runOne(part, state) {
    try {
      var eqs = part.split("=");
      if (eqs.length > 2) throw new Error("Bitta '=' belgisi bo'lsin");
      var env = { vars: state.vars, deg: state.deg, ans: state.ans };
      if (eqs.length === 2) {
        var L = eqs[0].trim(), Rr = eqs[1].trim();
        if (/^[A-Za-z_][A-Za-z_0-9]*$/.test(L) && !CONSTS.hasOwnProperty(L) && L.toLowerCase() !== "ans" && L.toLowerCase() !== "pi") {
          // o'zgaruvchiga qiymat berish, lekin tenglama ham bo'lishi mumkin: "x=5" qiymat, "x=2x+1" tenglama
          var ra = parse(Rr), unk = collectUnknown(ra, env);
          if (!unk.length || (unk.length === 1 && unk[0] === L && false)) {
            var v = evalAst(ra, env); state.vars[L] = v; state.ans = v;
            return { kind: "assign", value: v, text: L + " = " + fmt(v), plain: plain(v) };
          }
        }
        var la = parse(L), rb = parse(Rr);
        var unknowns = Array.from(new Set(collectUnknown(la, env).concat(collectUnknown(rb, env))));
        if (!unknowns.length) {
          var lv = evalAst(la, env), rv = evalAst(rb, env);
          return { kind: "check", text: Math.abs(lv - rv) < 1e-9 * Math.max(1, Math.abs(lv)) ? "To'g'ri tenglik ✓ (" + fmt(lv) + ")" : "Noto'g'ri: " + fmt(lv) + " ≠ " + fmt(rv) };
        }
        if (unknowns.length > 1) throw new Error("Bitta noma'lum bo'lsin (hozir: " + unknowns.join(", ") + ")");
        var name = unknowns[0], roots = solveEquation(la, rb, name, env);
        if (!roots.length) return { kind: "solve", text: name + ": haqiqiy ildiz topilmadi" };
        state.ans = roots[0];
        return { kind: "solve", value: roots[0], roots: roots, text: roots.map(function (r, i) { return name + (roots.length > 1 ? "₍" + (i + 1) + "₎" : "") + " = " + fmt(r); }).join("   "), plain: plain(roots[0]) };
      }
      var ast = parse(part);
      var unk2 = collectUnknown(ast, env);
      if (unk2.length) throw new Error("Noma'lum: " + unk2.join(", ") + " (qiymat bering yoki tenglama yozing: " + unk2[0] + " = ...)");
      var val = evalAst(ast, env);
      state.ans = val;
      return { kind: "value", value: val, text: fmt(val), plain: plain(val) };
    } catch (err) {
      return { kind: "error", text: err.message || String(err) };
    }
  }

  // ------------------------------------------------------------------ KIMYO
  var ATOMS = {
    H: 1.008, He: 4.0026, Li: 6.94, Be: 9.0122, B: 10.81, C: 12.011, N: 14.007, O: 15.999, F: 18.998, Ne: 20.18, Na: 22.99, Mg: 24.305, Al: 26.982, Si: 28.085,
    P: 30.974, S: 32.06, Cl: 35.45, Ar: 39.948, K: 39.098, Ca: 40.078, Sc: 44.956, Ti: 47.867, V: 50.942, Cr: 51.996, Mn: 54.938, Fe: 55.845, Co: 58.933,
    Ni: 58.693, Cu: 63.546, Zn: 65.38, Ga: 69.723, Ge: 72.63, As: 74.922, Se: 78.971, Br: 79.904, Kr: 83.798, Rb: 85.468, Sr: 87.62, Y: 88.906, Zr: 91.224,
    Nb: 92.906, Mo: 95.95, Tc: 98, Ru: 101.07, Rh: 102.91, Pd: 106.42, Ag: 107.87, Cd: 112.41, In: 114.82, Sn: 118.71, Sb: 121.76, Te: 127.6, I: 126.9,
    Xe: 131.29, Cs: 132.91, Ba: 137.33, La: 138.91, Ce: 140.12, Pr: 140.91, Nd: 144.24, Pm: 145, Sm: 150.36, Eu: 151.96, Gd: 157.25, Tb: 158.93, Dy: 162.5,
    Ho: 164.93, Er: 167.26, Tm: 168.93, Yb: 173.05, Lu: 174.97, Hf: 178.49, Ta: 180.95, W: 183.84, Re: 186.21, Os: 190.23, Ir: 192.22, Pt: 195.08,
    Au: 196.97, Hg: 200.59, Tl: 204.38, Pb: 207.2, Bi: 208.98, Po: 209, At: 210, Rn: 222, Fr: 223, Ra: 226, Ac: 227, Th: 232.04, Pa: 231.04, U: 238.03
  };
  // Maktab (DTM) masalalarida ishlatiladigan yaxlitlangan nisbiy atom massalari
  var SCHOOL_EXCEPT = { Cl: 35.5, Cu: 64, Zn: 65, Ba: 137, Hg: 201, Ag: 108, Br: 80, I: 127, Sr: 88, Mn: 55, Cr: 52, Pb: 207, Sn: 119, Sb: 122, Ni: 59, Co: 59 };
  function atomMass(sym, school) {
    var m = ATOMS[sym]; if (m === undefined) throw new Error("Noma'lum element: " + sym);
    if (!school) return m;
    return SCHOOL_EXCEPT[sym] !== undefined ? SCHOOL_EXCEPT[sym] : Math.round(m);
  }
  function parseFormula(f) {
    var s = String(f || "").replace(/[₀₁₂₃₄₅₆₇₈₉]/g, function (c) { return SUBMAP[c]; }).replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]/g, "").replace(/\s+/g, "")
      .replace(/[·•*.]/g, "·").replace(/[{\[]/g, "(").replace(/[}\]]/g, ")");
    s = s.replace(/[+\-]+$/, "");           // zaryad: SO4^2-, Na+
    var pos = 0;
    function parseGroup() {
      var counts = {};
      while (pos < s.length && s[pos] !== ")") {
        var c = s[pos];
        if (c === "(") {
          pos++; var inner = parseGroup(); if (s[pos] !== ")") throw new Error("Qavs yopilmagan"); pos++;
          var n = readNum(1); for (var k in inner) counts[k] = (counts[k] || 0) + inner[k] * n;
        } else if (/[A-Z]/.test(c)) {
          var sym = c; pos++;
          if (pos < s.length && /[a-z]/.test(s[pos])) { sym += s[pos]; pos++; }
          if (ATOMS[sym] === undefined && sym.length === 2) { sym = c; pos--; }     // "Co" vs "CO"
          if (ATOMS[sym] === undefined) throw new Error("Noma'lum element: " + sym);
          var m = readNum(1); counts[sym] = (counts[sym] || 0) + m;
        } else if (c === "·") {
          pos++; var coef = readNum(1); var rest = parseHydrate(); for (var k2 in rest) counts[k2] = (counts[k2] || 0) + rest[k2] * coef;
          return counts;
        } else if (/\d/.test(c) && pos === 0) {   // 2H2O kabi oldidagi koeffitsiyent
          var cf = readNum(1); var tail = parseGroup(); for (var k3 in tail) counts[k3] = (counts[k3] || 0) + tail[k3] * cf; return counts;
        } else throw new Error("Formulada noto'g'ri belgi: " + c);
      }
      return counts;
    }
    function parseHydrate() { var c = parseGroup(); return c; }
    function readNum(def) { var st = pos; while (pos < s.length && /\d/.test(s[pos])) pos++; return pos > st ? parseInt(s.slice(st, pos), 10) : def; }
    var res = parseGroup();
    if (pos < s.length) throw new Error("Formulani o'qib bo'lmadi");
    return res;
  }
  function molarMass(formula, school) {
    var counts = parseFormula(formula), total = 0, rows = [];
    Object.keys(counts).forEach(function (sym) { var am = atomMass(sym, school); total += am * counts[sym]; rows.push({ sym: sym, n: counts[sym], am: am, part: am * counts[sym] }); });
    if (!rows.length) throw new Error("Formula bo'sh");
    rows.forEach(function (r) { r.pct = r.part / total * 100; });
    return { M: total, rows: rows };
  }

  // ------------------------------------------------------------------ FIZIK / UMUMIY FORMULALAR
  /* [nom, tenglama, {o'zgaruvchi: "izoh (birlik)"}] — tenglamada trigonometrik burchaklar GRADUSDA */
  var FORMULAS = {
    physics: [
      ["Tekis harakat: yo'l", "s = v*t", { s: "Yo'l (m)", v: "Tezlik (m/s)", t: "Vaqt (s)" }],
      ["Tezlanish: tezlik", "v = v0 + a*t", { v: "Oxirgi tezlik (m/s)", v0: "Boshlang'ich tezlik (m/s)", a: "Tezlanish (m/s²)", t: "Vaqt (s)" }],
      ["Tekis o'zgaruvchan: yo'l", "s = v0*t + a*t^2/2", { s: "Yo'l (m)", v0: "Boshlang'ich tezlik (m/s)", a: "Tezlanish (m/s²)", t: "Vaqt (s)" }],
      ["Tezlik kvadrati", "v^2 = v0^2 + 2*a*s", { v: "Oxirgi tezlik (m/s)", v0: "Boshlang'ich tezlik (m/s)", a: "Tezlanish (m/s²)", s: "Yo'l (m)" }],
      ["Erkin tushish: balandlik", "h = g*t^2/2", { h: "Balandlik (m)", g: "g (m/s²)", t: "Vaqt (s)" }],
      ["Aylana bo'ylab: markazga intilma tezlanish", "ac = v^2/r", { ac: "Tezlanish (m/s²)", v: "Tezlik (m/s)", r: "Radius (m)" }],
      ["Aylanish davri va chastota", "f = 1/T", { f: "Chastota (Hz)", T: "Davr (s)" }],
      ["Chiziqli va burchak tezlik", "v = w*r", { v: "Chiziqli tezlik (m/s)", w: "Burchak tezlik (rad/s)", r: "Radius (m)" }],
      ["Nyutonning 2-qonuni", "F = m*a", { F: "Kuch (N)", m: "Massa (kg)", a: "Tezlanish (m/s²)" }],
      ["Og'irlik kuchi", "P = m*g", { P: "Og'irlik (N)", m: "Massa (kg)", g: "g (m/s²)" }],
      ["Ishqalanish kuchi", "Fi = mu*N", { Fi: "Ishqalanish kuchi (N)", mu: "Ishqalanish koeffitsiyenti", N: "Reaksiya kuchi (N)" }],
      ["Guk qonuni", "F = k*x", { F: "Kuch (N)", k: "Bikrlik (N/m)", x: "Cho'zilish (m)" }],
      ["Butun olam tortishish", "F = G*m1*m2/r^2", { F: "Kuch (N)", G: "G (6,67e-11)", m1: "m₁ (kg)", m2: "m₂ (kg)", r: "Masofa (m)" }],
      ["Impuls", "p = m*v", { p: "Impuls (kg·m/s)", m: "Massa (kg)", v: "Tezlik (m/s)" }],
      ["Kuch impulsi", "F*t = m*(v - v0)", { F: "Kuch (N)", t: "Vaqt (s)", m: "Massa (kg)", v: "Oxirgi tezlik (m/s)", v0: "Boshlang'ich tezlik (m/s)" }],
      ["Kinetik energiya", "Ek = m*v^2/2", { Ek: "Energiya (J)", m: "Massa (kg)", v: "Tezlik (m/s)" }],
      ["Potensial energiya", "Ep = m*g*h", { Ep: "Energiya (J)", m: "Massa (kg)", g: "g (m/s²)", h: "Balandlik (m)" }],
      ["Prujina energiyasi", "Ep = k*x^2/2", { Ep: "Energiya (J)", k: "Bikrlik (N/m)", x: "Deformatsiya (m)" }],
      ["Mexanik ish", "A = F*s*cos(alpha)", { A: "Ish (J)", F: "Kuch (N)", s: "Ko'chish (m)", alpha: "Burchak (°)" }],
      ["Quvvat", "N = A/t", { N: "Quvvat (W)", A: "Ish (J)", t: "Vaqt (s)" }],
      ["Quvvat: kuch va tezlik", "N = F*v", { N: "Quvvat (W)", F: "Kuch (N)", v: "Tezlik (m/s)" }],
      ["FIK", "eta = Af/Ao*100", { eta: "FIK (%)", Af: "Foydali ish (J)", Ao: "To'liq ish (J)" }],
      ["Bosim", "p = F/S", { p: "Bosim (Pa)", F: "Kuch (N)", S: "Yuza (m²)" }],
      ["Suyuqlik bosimi", "p = rho*g*h", { p: "Bosim (Pa)", rho: "Zichlik (kg/m³)", g: "g (m/s²)", h: "Chuqurlik (m)" }],
      ["Arximed kuchi", "Fa = rho*g*V", { Fa: "Kuch (N)", rho: "Suyuqlik zichligi (kg/m³)", g: "g (m/s²)", V: "Hajm (m³)" }],
      ["Zichlik", "rho = m/V", { rho: "Zichlik (kg/m³)", m: "Massa (kg)", V: "Hajm (m³)" }],
      ["Qizish uchun issiqlik", "Q = c*m*(t2 - t1)", { Q: "Issiqlik (J)", c: "Solishtirma issiqlik sig'imi (J/kg·°C)", m: "Massa (kg)", t2: "Oxirgi t (°C)", t1: "Boshlang'ich t (°C)" }],
      ["Erish issiqligi", "Q = lam*m", { Q: "Issiqlik (J)", lam: "Solishtirma erish issiqligi (J/kg)", m: "Massa (kg)" }],
      ["Yonilg'i issiqligi", "Q = q*m", { Q: "Issiqlik (J)", q: "Yonish issiqligi (J/kg)", m: "Massa (kg)" }],
      ["Mendeleyev–Klapeyron", "p*V = n*R*T", { p: "Bosim (Pa)", V: "Hajm (m³)", n: "Modda miqdori (mol)", R: "R (8,31)", T: "Harorat (K)" }],
      ["Birlashgan gaz qonuni", "p1*V1/T1 = p2*V2/T2", { p1: "p₁", V1: "V₁", T1: "T₁ (K)", p2: "p₂", V2: "V₂", T2: "T₂ (K)" }],
      ["Karno FIK", "eta = (T1 - T2)/T1*100", { eta: "FIK (%)", T1: "Isitkich T (K)", T2: "Sovutkich T (K)" }],
      ["Zaryad va tok", "I = q/t", { I: "Tok (A)", q: "Zaryad (C)", t: "Vaqt (s)" }],
      ["Om qonuni", "U = I*R", { U: "Kuchlanish (V)", I: "Tok (A)", R: "Qarshilik (Ω)" }],
      ["O'tkazgich qarshiligi", "R = rho*l/S", { R: "Qarshilik (Ω)", rho: "Solishtirma qarshilik (Ω·m)", l: "Uzunlik (m)", S: "Kesim yuzasi (m²)" }],
      ["Elektr quvvati", "P = U*I", { P: "Quvvat (W)", U: "Kuchlanish (V)", I: "Tok (A)" }],
      ["Joul–Lens", "Q = I^2*R*t", { Q: "Issiqlik (J)", I: "Tok (A)", R: "Qarshilik (Ω)", t: "Vaqt (s)" }],
      ["To'liq zanjir Om qonuni", "I = E/(R + r)", { I: "Tok (A)", E: "EYuK (V)", R: "Tashqi qarshilik (Ω)", r: "Ichki qarshilik (Ω)" }],
      ["Kulon qonuni", "F = k*q1*q2/r^2", { F: "Kuch (N)", k: "k (9e9)", q1: "q₁ (C)", q2: "q₂ (C)", r: "Masofa (m)" }],
      ["Elektr maydon kuchlanganligi", "E = F/q", { E: "Kuchlanganlik (N/C)", F: "Kuch (N)", q: "Zaryad (C)" }],
      ["Nuqtaviy zaryad maydoni", "E = k*q/r^2", { E: "Kuchlanganlik (N/C)", k: "k (9e9)", q: "Zaryad (C)", r: "Masofa (m)" }],
      ["Kondensator sig'imi", "C = q/U", { C: "Sig'im (F)", q: "Zaryad (C)", U: "Kuchlanish (V)" }],
      ["Kondensator energiyasi", "W = C*U^2/2", { W: "Energiya (J)", C: "Sig'im (F)", U: "Kuchlanish (V)" }],
      ["Amper kuchi", "F = B*I*l*sin(alpha)", { F: "Kuch (N)", B: "Induksiya (T)", I: "Tok (A)", l: "Uzunlik (m)", alpha: "Burchak (°)" }],
      ["Lorens kuchi", "F = q*v*B*sin(alpha)", { F: "Kuch (N)", q: "Zaryad (C)", v: "Tezlik (m/s)", B: "Induksiya (T)", alpha: "Burchak (°)" }],
      ["Induksiya EYuK (harakatdagi o'tkazgich)", "E = B*l*v*sin(alpha)", { E: "EYuK (V)", B: "Induksiya (T)", l: "Uzunlik (m)", v: "Tezlik (m/s)", alpha: "Burchak (°)" }],
      ["Magnit oqimi", "Phi = B*S*cos(alpha)", { Phi: "Oqim (Wb)", B: "Induksiya (T)", S: "Yuza (m²)", alpha: "Burchak (°)" }],
      ["Prujinali mayatnik davri", "T = 2*pi*sqrt(m/k)", { T: "Davr (s)", m: "Massa (kg)", k: "Bikrlik (N/m)" }],
      ["Matematik mayatnik davri", "T = 2*pi*sqrt(l/g)", { T: "Davr (s)", l: "Uzunlik (m)", g: "g (m/s²)" }],
      ["To'lqin uzunligi", "lam = v/f", { lam: "To'lqin uzunligi (m)", v: "Tezlik (m/s)", f: "Chastota (Hz)" }],
      ["Yupqa linza formulasi", "1/F = 1/d + 1/f", { F: "Fokus masofasi (m)", d: "Buyumgacha masofa (m)", f: "Tasvirgacha masofa (m)" }],
      ["Sindirish ko'rsatkichi", "n = c/v", { n: "Sindirish ko'rsatkichi", c: "c (3e8)", v: "Tezlik muhitda (m/s)" }],
      ["Snellius qonuni", "n1*sin(a1) = n2*sin(a2)", { n1: "n₁", a1: "Tushish burchagi (°)", n2: "n₂", a2: "Sinish burchagi (°)" }],
      ["Foton energiyasi", "E = h*f", { E: "Energiya (J)", h: "h (6,63e-34)", f: "Chastota (Hz)" }],
      ["Eynshteyn: massa–energiya", "E = m*c^2", { E: "Energiya (J)", m: "Massa (kg)", c: "c (3e8)" }],
      ["Fotoeffekt (Eynshteyn)", "h*f = A + Ek", { h: "h (6,63e-34)", f: "Chastota (Hz)", A: "Chiqish ishi (J)", Ek: "Kinetik energiya (J)" }],
      ["Radioaktiv yemirilish", "N = N0*2^(-t/T)", { N: "Qolgan yadrolar", N0: "Boshlang'ich yadrolar", t: "Vaqt", T: "Yarim yemirilish davri" }]
    ],
    chemistry: [
      ["Modda miqdori (massa orqali)", "n = m/M", { n: "n (mol)", m: "Massa (g)", M: "Molyar massa (g/mol)" }],
      ["Gaz hajmi (n.sh.)", "V = n*22.4", { V: "Hajm (l)", n: "n (mol)" }],
      ["Zarrachalar soni", "N = n*6.02e23", { N: "Zarrachalar soni", n: "n (mol)" }],
      ["Molyar konsentratsiya", "Cm = n/V", { Cm: "Cₘ (mol/l)", n: "n (mol)", V: "Eritma hajmi (l)" }],
      ["Massa ulushi (%)", "w = m1/m2*100", { w: "w (%)", m1: "Erigan modda massasi (g)", m2: "Eritma massasi (g)" }],
      ["Eritma massasi", "m2 = m1 + mS", { m2: "Eritma massasi (g)", m1: "Erigan modda (g)", mS: "Erituvchi (g)" }],
      ["Zichlik", "rho = m/V", { rho: "Zichlik (g/ml)", m: "Massa (g)", V: "Hajm (ml)" }],
      ["Mendeleyev–Klapeyron (kPa, l)", "p*V = n*8.31*T", { p: "Bosim (kPa)", V: "Hajm (l)", n: "n (mol)", T: "Harorat (K)" }],
      ["Nisbiy zichlik", "D = M1/M2", { D: "Nisbiy zichlik", M1: "Gazning M (g/mol)", M2: "Taqqoslanuvchi gaz M" }],
      ["Unum (amaliy / nazariy)", "eta = mp/mt*100", { eta: "Unum (%)", mp: "Amaliy massa (g)", mt: "Nazariy massa (g)" }],
      ["Suyultirish", "C1*V1 = C2*V2", { C1: "C₁", V1: "V₁", C2: "C₂", V2: "V₂" }],
      ["pH (kuchli kislota)", "pH = -log(H)", { pH: "pH", H: "[H⁺] (mol/l)" }],
      ["pH va pOH", "pH + pOH = 14", { pH: "pH", pOH: "pOH" }],
      ["Reaksiya tezligi (harorat)", "v2 = v1*gamma^((t2 - t1)/10)", { v2: "v₂", v1: "v₁", gamma: "Harorat koeffitsiyenti γ", t2: "t₂ (°C)", t1: "t₁ (°C)" }],
      ["Reaksiya issiqlik effekti", "Q = n*dH", { Q: "Issiqlik (kJ)", n: "n (mol)", dH: "ΔH (kJ/mol)" }]
    ],
    math: [
      ["To'g'ri to'rtburchak yuzi", "S = a*b", { S: "Yuza", a: "Tomon a", b: "Tomon b" }],
      ["Uchburchak yuzi", "S = a*h/2", { S: "Yuza", a: "Asos", h: "Balandlik" }],
      ["Geron: uchburchak yuzi", "S = sqrt(p*(p-a)*(p-b)*(p-c))", { S: "Yuza", p: "Yarim perimetr", a: "a", b: "b", c: "c" }],
      ["Pifagor teoremasi", "c^2 = a^2 + b^2", { c: "Gipotenuza", a: "Katet a", b: "Katet b" }],
      ["Aylana uzunligi", "C = 2*pi*r", { C: "Uzunlik", r: "Radius" }],
      ["Doira yuzi", "S = pi*r^2", { S: "Yuza", r: "Radius" }],
      ["Silindr hajmi", "V = pi*r^2*h", { V: "Hajm", r: "Radius", h: "Balandlik" }],
      ["Konus hajmi", "V = pi*r^2*h/3", { V: "Hajm", r: "Radius", h: "Balandlik" }],
      ["Shar hajmi", "V = 4*pi*r^3/3", { V: "Hajm", r: "Radius" }],
      ["Shar sirti", "S = 4*pi*r^2", { S: "Sirt", r: "Radius" }],
      ["Arifmetik progressiya: n-had", "an = a1 + (n-1)*d", { an: "aₙ", a1: "a₁", n: "n", d: "d" }],
      ["Arifmetik progressiya: yig'indi", "Sn = (2*a1 + (n-1)*d)*n/2", { Sn: "Sₙ", a1: "a₁", n: "n", d: "d" }],
      ["Geometrik progressiya: n-had", "bn = b1*q^(n-1)", { bn: "bₙ", b1: "b₁", q: "q", n: "n" }],
      ["Geometrik progressiya: yig'indi", "Sn = b1*(q^n - 1)/(q - 1)", { Sn: "Sₙ", b1: "b₁", q: "q", n: "n" }],
      ["Murakkab foiz", "S = A*(1 + p/100)^n", { S: "Yakuniy summa", A: "Boshlang'ich", p: "Foiz (%)", n: "Yillar soni" }],
      ["Sinuslar teoremasi", "a/sin(A) = b/sin(B)", { a: "a", A: "A burchak (°)", b: "b", B: "B burchak (°)" }],
      ["Kosinuslar teoremasi", "c^2 = a^2 + b^2 - 2*a*b*cos(C)", { c: "c", a: "a", b: "b", C: "C burchak (°)" }],
      ["Ikki nuqta orasidagi masofa", "d = sqrt((x2-x1)^2 + (y2-y1)^2)", { d: "Masofa", x1: "x₁", y1: "y₁", x2: "x₂", y2: "y₂" }]
    ]
  };

  /* Bitta noma'lumni topish: known = {nom: son}, unknown = nom. Qaytaradi: [ildizlar]. */
  function solveFormula(eq, known, unknown) {
    var sides = eq.split("="), env = { vars: Object.assign({}, known), deg: true, ans: 0 };
    var l = parse(sides[0]), r = parse(sides[1]);
    // to'g'ridan-to'g'ri: "X = ifoda" bo'lsa va X noma'lum
    if (/^\s*[A-Za-z_][A-Za-z_0-9]*\s*$/.test(sides[0]) && sides[0].trim() === unknown) {
      try { var v = evalAst(r, env); if (isFinite(v)) return [v]; } catch (e) { /* son usuliga o'tamiz */ }
    }
    var roots = solveEquation(l, r, unknown, env);
    return roots;
  }


  // ------------------------------------------------------------------ REAKSIYA TENGLAMASINI TENGLASHTIRISH
  function balance(eqText) {
    var s = String(eqText || "").replace(/[₀₁₂₃₄₅₆₇₈₉]/g, function (c) { return SUBMAP[c]; }).replace(/→|⟶|=>|==|=|⇒|->/g, "->");
    var halves = s.split("->");
    if (halves.length !== 2) throw new Error("Tenglamani 'A + B -> C + D' ko'rinishida yozing");
    function species(side) { return side.split("+").map(function (x) { return x.trim().replace(/^\d+\s*(?=[A-Z(])/, ""); }).filter(Boolean); }
    var L = species(halves[0]), R = species(halves[1]);
    if (!L.length || !R.length) throw new Error("Ikkala tomonda ham modda bo'lishi kerak");
    var all = L.concat(R), counts = all.map(function (f) { return parseFormula(f); });
    var els = []; counts.forEach(function (c) { Object.keys(c).forEach(function (e) { if (els.indexOf(e) < 0) els.push(e); }); });
    var n = all.length, rows = els.map(function (e) { return counts.map(function (c, j) { var v = BigInt(c[e] || 0); return j < L.length ? v : -v; }); });
    // Gauss (butun sonlar, kasr: bo'luvchi bilan)
    var m = rows.map(function (r) { return r.map(function (v) { return [v, 1n]; }); });
    function g(a, b) { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) { var t = b; b = a % b; a = t; } return a; }
    function norm(f) { if (f[1] < 0n) f = [-f[0], -f[1]]; var d = g(f[0], f[1]) || 1n; return [f[0] / d, f[1] / d]; }
    function sub(a, b) { return norm([a[0] * b[1] - b[0] * a[1], a[1] * b[1]]); }
    function mul(a, b) { return norm([a[0] * b[0], a[1] * b[1]]); }
    function div(a, b) { return norm([a[0] * b[1], a[1] * b[0]]); }
    var piv = [], r = 0;
    for (var c = 0; c < n && r < m.length; c++) {
      var p = -1; for (var i = r; i < m.length; i++) { if (m[i][c][0] !== 0n) { p = i; break; } }
      if (p < 0) continue;
      var tmp = m[r]; m[r] = m[p]; m[p] = tmp;
      var pv = m[r][c]; m[r] = m[r].map(function (x) { return div(x, pv); });
      for (i = 0; i < m.length; i++) { if (i !== r && m[i][c][0] !== 0n) { var f = m[i][c]; m[i] = m[i].map(function (x, j) { return sub(x, mul(f, m[r][j])); }); } }
      piv.push(c); r++;
    }
    var free = []; for (c = 0; c < n; c++) { if (piv.indexOf(c) < 0) free.push(c); }
    if (free.length !== 1) throw new Error(free.length ? "Tenglamani yagona usulda tenglashtirib bo'lmadi (bir nechta yechim)" : "Bu moddalardan tenglama tuzib bo'lmaydi");
    var fc = free[0], vec = new Array(n).fill(null); vec[fc] = [1n, 1n];
    piv.forEach(function (pc, idx) { vec[pc] = norm([-m[idx][fc][0], m[idx][fc][1]]); });
    var den = 1n; vec.forEach(function (x) { den = den * x[1] / g(den, x[1]); });
    var ints = vec.map(function (x) { return x[0] * (den / x[1]); });
    var gg = ints.reduce(function (a, b) { return g(a, b); }, 0n) || 1n;
    ints = ints.map(function (x) { return x / gg; });
    if (ints.some(function (x) { return x <= 0n; })) { if (ints.every(function (x) { return x <= 0n; })) ints = ints.map(function (x) { return -x; }); else throw new Error("Tenglamani tenglashtirib bo'lmadi (formulalarni tekshiring)"); }
    function side(arr, off) { return arr.map(function (f, j) { var k = ints[off + j]; return (k === 1n ? "" : String(k)) + f; }).join(" + "); }
    return side(L, 0) + " → " + side(R, L.length);
  }

  // ------------------------------------------------------------------ BIOLOGIYA
  var CODON_AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG";
  var CODON_BASES = "UCAG";
  var AA3 = { F: "Fen", L: "Ley", S: "Ser", Y: "Tir", C: "Sis", W: "Trp", P: "Pro", H: "Gis", Q: "Gln", R: "Arg", I: "Ile", M: "Met", T: "Tre", N: "Asn", K: "Lys", V: "Val", A: "Ala", D: "Asp", E: "Glu", G: "Gli", "*": "STOP" };
  function codonAA(c) {
    c = c.toUpperCase().replace(/T/g, "U");
    if (c.length !== 3) return null;
    var i = CODON_BASES.indexOf(c[0]), j = CODON_BASES.indexOf(c[1]), k = CODON_BASES.indexOf(c[2]);
    if (i < 0 || j < 0 || k < 0) return null;
    return CODON_AA[16 * i + 4 * j + k];
  }
  var COMP_DNA = { A: "T", T: "A", G: "C", C: "G" };
  var COMP_RNA = { A: "U", T: "A", G: "C", C: "G", U: "A" };
  function clean(seq) { return String(seq || "").toUpperCase().replace(/[^ATGCU]/g, ""); }
  function dnaComplement(seq) { return clean(seq).replace(/T|A|G|C|U/g, function (b) { return COMP_DNA[b] || b; }); }
  function transcribe(seqTemplate) { return clean(seqTemplate).replace(/T|A|G|C|U/g, function (b) { return COMP_RNA[b] || b; }); }   // matritsa DNK -> iRNK
  function translate(rna) {
    rna = clean(rna).replace(/T/g, "U"); var out = [], start = rna.indexOf("AUG");
    for (var i = start >= 0 ? start : 0; i + 3 <= rna.length; i += 3) { var aa = codonAA(rna.slice(i, i + 3)); out.push({ codon: rna.slice(i, i + 3), aa: aa, name: AA3[aa] || "?" }); if (aa === "*") break; }
    return out;
  }

  var API = {
    CONSTS: CONSTS, CONST_INFO: CONST_INFO, FORMULAS: FORMULAS, ATOMS: ATOMS,
    normalize: normalize, parse: parse, evalAst: evalAst, run: run, fmt: fmt, plain: plain, findRoots: findRoots,
    parseFormula: parseFormula, molarMass: molarMass, atomMass: atomMass, solveFormula: solveFormula,
    balance: balance, codonAA: codonAA, AA3: AA3, dnaComplement: dnaComplement, transcribe: transcribe, translate: translate,
    ncr: ncr, npr: npr, gcd: gcd, fact: fact, newState: function (deg) { return { vars: {}, deg: deg !== false, ans: 0 }; }
  };
  if (typeof module !== "undefined" && module.exports) module.exports = API;
  root.LZCalc = API;
})(typeof window !== "undefined" ? window : globalThis);
