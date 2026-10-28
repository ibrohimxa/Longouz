// ============================================================================
// LongoUZ — test paytidagi KALKULYATOR (fanga moslashgan).
//   matematika / fizika / kimyo / biologiya — bor;
//   tarix, ona tili, ingliz va rus tili — YO'Q (u yerda hisob kerak emas).
// Tarkibi:
//   1) Ilmiy kalkulyator — xavfsiz ifoda hisoblagich (eval YO'Q): + − × ÷ ^ ! %, sin/cos/tan,
//      log/ln/sqrt/..., o'zgaruvchilar (m=2 keyin m*9.8), DEG/RAD, oxirgi javob (ans), tarix.
//   2) "Formula" yechuvchi — fan bo'yicha tayyor formulalar: ma'lum qiymatlarni kiriting,
//      bitta bo'sh qoldiring — kalkulyator o'zi topadi (yoki hammasini hisoblaydi).
//   3) Kimyo: molyar massa hisoblagich (H2SO4, Ca(OH)2, CuSO4*5H2O ...).
//   4) Fizika: doimiylar (g, c, h, G, k, N_A, R ...) bir bosishda ifodaga qo'shiladi.
// ============================================================================
(function (root) {
  "use strict";

  // ============================ YADRO: IFODA HISOBLAGICH ============================
  const Core = (function () {
    const CONST = { pi: Math.PI, e: Math.E, tau: 2 * Math.PI };
    const fact = (n) => {
      if (!Number.isInteger(n) || n < 0 || n > 170) throw new Error("Faktorial: 0..170 butun son");
      let r = 1; for (let i = 2; i <= n; i++) r *= i; return r;
    };
    const gcd = (a, b) => { a = Math.abs(a); b = Math.abs(b); while (b) { [a, b] = [b, a % b]; } return a; };
    const nCr = (n, k) => { if (k < 0 || k > n) return 0; k = Math.min(k, n - k); let r = 1; for (let i = 1; i <= k; i++) r = r * (n - k + i) / i; return Math.round(r); };
    const nPr = (n, k) => { if (k < 0 || k > n) return 0; let r = 1; for (let i = 0; i < k; i++) r *= (n - i); return r; };

    function makeFns(angle) {
      const toRad = (x) => (angle === "deg" ? x * Math.PI / 180 : x);
      const fromRad = (x) => (angle === "deg" ? x * 180 / Math.PI : x);
      const cleanTrig = (v) => (Math.abs(v) < 1e-14 ? 0 : v);
      return {
        sin: (x) => cleanTrig(Math.sin(toRad(x))), cos: (x) => cleanTrig(Math.cos(toRad(x))),
        tan: (x) => { const r = toRad(x); if (Math.abs(Math.cos(r)) < 1e-14) throw new Error("tan aniqlanmagan"); return cleanTrig(Math.tan(r)); },
        ctg: (x) => { const t = Math.tan(toRad(x)); if (Math.abs(t) < 1e-14) throw new Error("ctg aniqlanmagan"); return 1 / t; },
        asin: (x) => fromRad(Math.asin(x)), acos: (x) => fromRad(Math.acos(x)), atan: (x) => fromRad(Math.atan(x)),
        sinh: Math.sinh, cosh: Math.cosh, tanh: Math.tanh,
        ln: Math.log, log: Math.log10, lg: Math.log10, log2: Math.log2, exp: Math.exp,
        sqrt: (x) => { if (x < 0) throw new Error("Manfiy sondan ildiz"); return Math.sqrt(x); },
        cbrt: Math.cbrt, abs: Math.abs, floor: Math.floor, ceil: Math.ceil, round: Math.round, sign: Math.sign,
        fact, deg: (x) => x * 180 / Math.PI, rad: (x) => x * Math.PI / 180,
        root: (n, x) => { if (x < 0 && n % 2 === 1) return -Math.pow(-x, 1 / n); if (x < 0) throw new Error("Manfiy sondan juft darajali ildiz"); return Math.pow(x, 1 / n); },
        pow: Math.pow, min: Math.min, max: Math.max, gcd, lcm: (a, b) => Math.abs(a * b) / (gcd(a, b) || 1),
        nCr, nPr, C: nCr, A: nPr, mod: (a, b) => a % b, logb: (b, x) => Math.log(x) / Math.log(b),
      };
    }

    function tokenize(src) {
      let s = String(src).replace(/×|·|⋅/g, "*").replace(/÷|:/g, "/").replace(/[−–—]/g, "-").replace(/π/g, " pi ")
        .replace(/√/g, " sqrt ").replace(/²/g, "^2").replace(/³/g, "^3");
      // O'nlik vergul ("2,5") — faqat funksiya argumentlari (nCr(5,2), max(1,2)) bo'lmasa nuqtaga aylanadi
      const s2 = /[A-Za-z_]\w*\s*\([^)]*,/.test(s) ? s : s.replace(/(\d),(\d)/g, "$1.$2");
      s = s2;
      const out = []; let i = 0;
      while (i < s.length) {
        const ch = s[i];
        if (/\s/.test(ch)) { i++; continue; }
        if (/[0-9.]/.test(ch)) {
          const m = /^(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?/.exec(s.slice(i));
          if (!m) throw new Error("Son noto'g'ri");
          out.push({ t: "num", v: parseFloat(m[0]) }); i += m[0].length; continue;
        }
        if (/[A-Za-z_\u0394\u03b1-\u03c9]/.test(ch)) {
          const m = /^[A-Za-z_\u0394\u03b1-\u03c9][A-Za-z_0-9\u0394\u03b1-\u03c9]*/.exec(s.slice(i));
          out.push({ t: "id", v: m[0] }); i += m[0].length; continue;
        }
        if ("+-*/^()!%,=".includes(ch)) { out.push({ t: "op", v: ch }); i++; continue; }
        throw new Error("Noma'lum belgi: " + ch);
      }
      return out;
    }

    function evaluate(src, vars, angle) {
      vars = vars || {};
      const fns = makeFns(angle || "deg");
      const toks = tokenize(src); let p = 0;
      const peek = () => toks[p]; const next = () => toks[p++];
      const isOp = (v) => peek() && peek().t === "op" && peek().v === v;

      function parseExpr() {
        let v = parseTerm();
        while (isOp("+") || isOp("-")) { const op = next().v; const r = parseTerm(); v = op === "+" ? v + r : v - r; }
        return v;
      }
      function startsOperand() {
        const k = peek(); if (!k) return false;
        return k.t === "num" || k.t === "id" || (k.t === "op" && k.v === "(");
      }
      function parseTerm() {
        let v = parseUnary();
        for (;;) {
          if (isOp("*")) { next(); v *= parseUnary(); }
          else if (isOp("/")) { next(); const d = parseUnary(); if (d === 0) throw new Error("Nolga bo'lish"); v /= d; }
          else if (startsOperand()) { v *= parseUnary(); }          // yashirin ko'paytirish: 2pi, 3(4+1), 2x
          else break;
        }
        return v;
      }
      function parseUnary() {
        if (isOp("-")) { next(); return -parseUnary(); }
        if (isOp("+")) { next(); return parseUnary(); }
        return parsePow();
      }
      function parsePow() {
        let base = parsePostfix();
        if (isOp("^")) { next(); const ex = parseUnary(); return Math.pow(base, ex); }   // o'ngdan chapga
        return base;
      }
      function parsePostfix() {
        let v = parseAtom();
        for (;;) {
          if (isOp("!")) { next(); v = fact(v); }
          else if (isOp("%")) { next(); v = v / 100; }
          else break;
        }
        return v;
      }
      function parseAtom() {
        const k = next();
        if (!k) throw new Error("Ifoda tugallanmagan");
        if (k.t === "num") return k.v;
        if (k.t === "op" && k.v === "(") { const v = parseExpr(); if (!isOp(")")) throw new Error("')' yetishmayapti"); next(); return v; }
        if (k.t === "id") {
          const name = k.v;
          if (isOp("(") && Object.prototype.hasOwnProperty.call(fns, name)) {
            next(); const args = [];
            if (!isOp(")")) { args.push(parseExpr()); while (isOp(",")) { next(); args.push(parseExpr()); } }
            if (!isOp(")")) throw new Error("')' yetishmayapti"); next();
            const r = fns[name](...args); if (typeof r !== "number") throw new Error("Hisoblab bo'lmadi"); return r;
          }
          if (Object.prototype.hasOwnProperty.call(vars, name)) return vars[name];
          if (Object.prototype.hasOwnProperty.call(CONST, name)) return CONST[name];
          if (Object.prototype.hasOwnProperty.call(fns, name)) {          // sin 30 (qavssiz)
            const arg = parseUnary(); return fns[name](arg);
          }
          throw new Error("Noma'lum: " + name);
        }
        throw new Error("Kutilmagan belgi: " + k.v);
      }

      // "x = 5" — o'zgaruvchiga qiymat berish
      if (toks.length >= 3 && toks[0].t === "id" && toks[1].t === "op" && toks[1].v === "=") {
        const name = toks[0].v; p = 2; const val = parseExpr();
        if (p < toks.length) throw new Error("Ortiqcha belgi");
        if (!isFinite(val)) throw new Error("Natija chekli emas");
        return { value: val, assigned: name };
      }
      const val = parseExpr();
      if (p < toks.length) throw new Error("Ortiqcha belgi: " + (peek().v));
      if (!isFinite(val)) throw new Error("Natija chekli emas (nolga bo'lish yoki juda katta son)");
      return { value: val };
    }

    function fmt(n) {
      if (!isFinite(n)) return "—";
      if (n === 0) return "0";
      const a = Math.abs(n);
      if (a >= 1e12 || a < 1e-6) return n.toExponential(6).replace(/\.?0+e/, "e").replace("e+", "e");
      let s = parseFloat(n.toPrecision(12)).toString();
      return s;
    }

    // ---------- Formula yechuvchi ----------
    // f = { name, vars: [[sym, label, unit]], solve: {sym: expr} }  — bitta noma'lumni topadi
    // f = { name, vars: [...], outputs: [[sym, label, expr, unit]] } — kiritilganlardan hammasini hisoblaydi
    function solveFormula(f, values, angle) {
      const known = {}; const empty = [];
      f.vars.forEach(([sym]) => {
        const raw = (values[sym] == null ? "" : String(values[sym])).trim();
        if (raw === "") { empty.push(sym); return; }
        const r = evaluate(raw, {}, angle);
        known[sym] = r.value;
      });
      if (f.outputs) {
        if (empty.length) throw new Error("Hamma maydonni to'ldiring: " + empty.join(", "));
        const res = []; const scope = Object.assign({}, known);
        f.outputs.forEach(([sym, label, expr, unit]) => {
          let v; try { v = evaluate(expr, scope, angle).value; } catch (e) { v = NaN; }
          if (!isFinite(v)) { res.push({ sym, label, text: "yechim yo'q", unit: "" }); return; }
          scope[sym] = v; res.push({ sym, label, value: v, text: fmt(v), unit: unit || "" });
        });
        return res;
      }
      if (empty.length !== 1) throw new Error(empty.length === 0 ? "Bitta qiymatni bo'sh qoldiring — o'sha topiladi." : "Faqat bitta qiymat bo'sh bo'lishi kerak.");
      const target = empty[0]; const expr = f.solve[target];
      if (!expr) throw new Error(target + " ni bu formuladan topib bo'lmaydi");
      const v = evaluate(expr, known, angle).value;
      if (!isFinite(v)) throw new Error("Yechim yo'q (qiymatlarni tekshiring)");
      const meta = f.vars.find((x) => x[0] === target);
      return [{ sym: target, label: meta[1], value: v, text: fmt(v), unit: meta[2] || "" }];
    }

    // ---------- Kimyo: molyar massa ----------
    const AM = { H: 1.008, He: 4.0026, Li: 6.94, Be: 9.0122, B: 10.81, C: 12.011, N: 14.007, O: 15.999, F: 18.998, Ne: 20.18, Na: 22.99, Mg: 24.305, Al: 26.982, Si: 28.085, P: 30.974, S: 32.06, Cl: 35.45, Ar: 39.948, K: 39.098, Ca: 40.078, Sc: 44.956, Ti: 47.867, V: 50.942, Cr: 51.996, Mn: 54.938, Fe: 55.845, Co: 58.933, Ni: 58.693, Cu: 63.546, Zn: 65.38, Ga: 69.723, Ge: 72.63, As: 74.922, Se: 78.971, Br: 79.904, Kr: 83.798, Rb: 85.468, Sr: 87.62, Y: 88.906, Zr: 91.224, Nb: 92.906, Mo: 95.95, Ru: 101.07, Rh: 102.91, Pd: 106.42, Ag: 107.87, Cd: 112.41, In: 114.82, Sn: 118.71, Sb: 121.76, Te: 127.6, I: 126.9, Xe: 131.29, Cs: 132.91, Ba: 137.33, La: 138.91, Ce: 140.12, W: 183.84, Pt: 195.08, Au: 196.97, Hg: 200.59, Tl: 204.38, Pb: 207.2, Bi: 208.98, Rn: 222, Ra: 226, U: 238.03 };
    const SCHOOL = (sym) => { if (sym === "Cl") return 35.5; if (sym === "Cu") return 64; return Math.round(AM[sym]); };

    const srcRef = { s: "" };
    function parseGroupRef() {
      let pos = 0; const s = srcRef.s;
      function readNum() { const m = /^\d+/.exec(s.slice(pos)); if (m) { pos += m[0].length; return parseInt(m[0], 10); } return 1; }
      function group(stopAt) {
        const acc = {};
        while (pos < s.length && s[pos] !== stopAt) {
          const c = s[pos];
          if (c === "(" || c === "[") {
            pos++; const inner = group(c === "(" ? ")" : "]"); if (s[pos] !== (c === "(" ? ")" : "]")) throw new Error("Qavs yopilmagan"); pos++;
            const n = readNum(); for (const k in inner) acc[k] = (acc[k] || 0) + inner[k] * n;
          } else if (/[A-Z]/.test(c)) {
            let sym = c; pos++; while (pos < s.length && /[a-z]/.test(s[pos])) sym += s[pos++];
            if (!(sym in AM)) throw new Error("Noma'lum element: " + sym);
            const n = readNum(); acc[sym] = (acc[sym] || 0) + n;
          } else throw new Error("Formulada noto'g'ri belgi: " + c);
        }
        return acc;
      }
      const r = group(null); if (pos < s.length) throw new Error("Ortiqcha qavs"); return r;
    }
    function molarMassOf(formula) {
      const norm = String(formula).replace(/\s+/g, "").replace(/[·•]/g, "*").replace(/[₀-₉]/g, (c) => String(c.charCodeAt(0) - 8320));
      if (!norm) throw new Error("Formulani kiriting");
      const total = {};
      norm.split("*").forEach((seg) => {
        const m = /^(\d+)([A-Z(\[].*)$/.exec(seg); const mult = m ? parseInt(m[1], 10) : 1;
        srcRef.s = m ? m[2] : seg; const g = parseGroupRef();
        for (const k in g) total[k] = (total[k] || 0) + g[k] * mult;
      });
      let exact = 0, school = 0;
      const rows = Object.keys(total).map((k) => { exact += AM[k] * total[k]; school += SCHOOL(k) * total[k]; return { sym: k, n: total[k], ar: AM[k] }; });
      return { rows, exact, school };
    }

    return { evaluate, fmt, solveFormula, molarMass: molarMassOf, AM };
  })();

  if (typeof module !== "undefined" && module.exports) { module.exports = Core; }
  if (typeof document === "undefined") return;
  root.LZCalcCore = Core;

  // ============================ FORMULALAR (fan bo'yicha) ============================
  const V = (sym, label, unit) => [sym, label, unit || ""];
  const FORMULAS = {
    math: [
      { name: "Kvadrat tenglama  ax²+bx+c=0", vars: [V("a", "a"), V("b", "b"), V("c", "c")], outputs: [["D", "Diskriminant", "b^2-4*a*c"], ["x1", "x₁", "(-b+sqrt(D))/(2*a)"], ["x2", "x₂", "(-b-sqrt(D))/(2*a)"]] },
      { name: "Arifmetik progressiya  aₙ = a₁+(n−1)d", vars: [V("an", "aₙ"), V("a1", "a₁"), V("n", "n"), V("d", "d")], solve: { an: "a1+(n-1)*d", a1: "an-(n-1)*d", n: "(an-a1)/d+1", d: "(an-a1)/(n-1)" } },
      { name: "Arifmetik progressiya yig'indisi  Sₙ", vars: [V("S", "Sₙ"), V("a1", "a₁"), V("d", "d"), V("n", "n")], solve: { S: "n*(2*a1+(n-1)*d)/2" } },
      { name: "Geometrik progressiya  bₙ = b₁·qⁿ⁻¹", vars: [V("bn", "bₙ"), V("b1", "b₁"), V("q", "q"), V("n", "n")], solve: { bn: "b1*q^(n-1)", b1: "bn/q^(n-1)", q: "(bn/b1)^(1/(n-1))", n: "log(bn/b1)/log(q)+1" } },
      { name: "Geometrik progressiya yig'indisi  Sₙ", vars: [V("S", "Sₙ"), V("b1", "b₁"), V("q", "q"), V("n", "n")], solve: { S: "b1*(q^n-1)/(q-1)" } },
      { name: "Foiz  Y = X·p/100", vars: [V("Y", "Y (qism)"), V("X", "X (butun)"), V("p", "p", "%")], solve: { Y: "X*p/100", X: "Y*100/p", p: "Y*100/X" } },
      { name: "Murakkab foiz  S = A(1+p/100)ⁿ", vars: [V("S", "S"), V("A", "A"), V("p", "p", "%"), V("n", "n")], solve: { S: "A*(1+p/100)^n", A: "S/(1+p/100)^n", p: "((S/A)^(1/n)-1)*100", n: "log(S/A)/log(1+p/100)" } },
      { name: "Doira  (r → S, L)", vars: [V("r", "r")], outputs: [["S", "Yuza S", "pi*r^2"], ["L", "Uzunlik L", "2*pi*r"], ["d", "Diametr", "2*r"]] },
      { name: "Uchburchak (Geron formulasi)", vars: [V("a", "a"), V("b", "b"), V("c", "c")], outputs: [["p", "Yarim perimetr p", "(a+b+c)/2"], ["S", "Yuza S", "sqrt(p*(p-a)*(p-b)*(p-c))"], ["P", "Perimetr", "a+b+c"]] },
      { name: "Silindr  (r, h → V, S)", vars: [V("r", "r"), V("h", "h")], outputs: [["V", "Hajm V", "pi*r^2*h"], ["Syon", "Yon sirt", "2*pi*r*h"], ["Sto", "To'la sirt", "2*pi*r*(r+h)"]] },
      { name: "Shar  (R → V, S)", vars: [V("R", "R")], outputs: [["V", "Hajm V", "4/3*pi*R^3"], ["S", "Sirt S", "4*pi*R^2"]] },
      { name: "Konus  (r, h → V, l, S)", vars: [V("r", "r"), V("h", "h")], outputs: [["V", "Hajm V", "pi*r^2*h/3"], ["l", "Yasovchi l", "sqrt(r^2+h^2)"], ["S", "To'la sirt", "pi*r*(r+l)"]] },
      { name: "Kombinatorika  (n, k)", vars: [V("n", "n"), V("k", "k")], outputs: [["P", "Pₙ = n!", "n!"], ["A", "A(n,k) o'rinlashtirish", "nPr(n,k)"], ["C", "C(n,k) guruhlash", "nCr(n,k)"]] },
      { name: "Pifagor  c² = a² + b²", vars: [V("c", "c (gipotenuza)"), V("a", "a"), V("b", "b")], solve: { c: "sqrt(a^2+b^2)", a: "sqrt(c^2-b^2)", b: "sqrt(c^2-a^2)" } },
    ],
    physics: [
      { name: "Tezlik  v = s / t", vars: [V("v", "v", "m/s"), V("s", "s", "m"), V("t", "t", "s")], solve: { v: "s/t", s: "v*t", t: "s/v" } },
      { name: "Tezlanish  a = (v − v₀) / t", vars: [V("a", "a", "m/s²"), V("v", "v", "m/s"), V("v0", "v₀", "m/s"), V("t", "t", "s")], solve: { a: "(v-v0)/t", v: "v0+a*t", v0: "v-a*t", t: "(v-v0)/a" } },
      { name: "Yo'l  s = v₀t + at²/2", vars: [V("s", "s", "m"), V("v0", "v₀", "m/s"), V("a", "a", "m/s²"), V("t", "t", "s")], solve: { s: "v0*t+a*t^2/2", a: "2*(s-v0*t)/t^2", v0: "s/t-a*t/2" } },
      { name: "Nyuton II qonuni  F = m·a", vars: [V("F", "F", "N"), V("m", "m", "kg"), V("a", "a", "m/s²")], solve: { F: "m*a", m: "F/a", a: "F/m" } },
      { name: "Impuls  p = m·v", vars: [V("p", "p", "kg·m/s"), V("m", "m", "kg"), V("v", "v", "m/s")], solve: { p: "m*v", m: "p/v", v: "p/m" } },
      { name: "Ish  A = F·s·cosα", vars: [V("A", "A", "J"), V("F", "F", "N"), V("s", "s", "m"), V("al", "α", "°")], solve: { A: "F*s*cos(al)", F: "A/(s*cos(al))", s: "A/(F*cos(al))" } },
      { name: "Kinetik energiya  E = mv²/2", vars: [V("E", "E", "J"), V("m", "m", "kg"), V("v", "v", "m/s")], solve: { E: "m*v^2/2", m: "2*E/v^2", v: "sqrt(2*E/m)" } },
      { name: "Potensial energiya  E = mgh", vars: [V("E", "E", "J"), V("m", "m", "kg"), V("g", "g", "m/s²"), V("h", "h", "m")], solve: { E: "m*g*h", m: "E/(g*h)", h: "E/(m*g)", g: "E/(m*h)" } },
      { name: "Quvvat  P = A / t", vars: [V("P", "P", "W"), V("A", "A", "J"), V("t", "t", "s")], solve: { P: "A/t", A: "P*t", t: "A/P" } },
      { name: "Bosim  p = F / S", vars: [V("p", "p", "Pa"), V("F", "F", "N"), V("S", "S", "m²")], solve: { p: "F/S", F: "p*S", S: "F/p" } },
      { name: "Zichlik  ρ = m / V", vars: [V("r", "ρ", "kg/m³"), V("m", "m", "kg"), V("V", "V", "m³")], solve: { r: "m/V", m: "r*V", V: "m/r" } },
      { name: "Arximed kuchi  F = ρ·g·V", vars: [V("F", "F", "N"), V("r", "ρ", "kg/m³"), V("g", "g", "m/s²"), V("V", "V", "m³")], solve: { F: "r*g*V", V: "F/(r*g)", r: "F/(g*V)" } },
      { name: "Guk qonuni  F = k·x", vars: [V("F", "F", "N"), V("k", "k", "N/m"), V("x", "x", "m")], solve: { F: "k*x", k: "F/x", x: "F/k" } },
      { name: "Butun olam tortishish  F = G·m₁m₂/r²", vars: [V("F", "F", "N"), V("m1", "m₁", "kg"), V("m2", "m₂", "kg"), V("r", "r", "m")], solve: { F: "6.674e-11*m1*m2/r^2", m1: "F*r^2/(6.674e-11*m2)", r: "sqrt(6.674e-11*m1*m2/F)" } },
      { name: "Matematik mayatnik  T = 2π√(l/g)", vars: [V("T", "T", "s"), V("l", "l", "m"), V("g", "g", "m/s²")], solve: { T: "2*pi*sqrt(l/g)", l: "g*(T/(2*pi))^2", g: "l*(2*pi/T)^2" } },
      { name: "Prujinali mayatnik  T = 2π√(m/k)", vars: [V("T", "T", "s"), V("m", "m", "kg"), V("k", "k", "N/m")], solve: { T: "2*pi*sqrt(m/k)", m: "k*(T/(2*pi))^2", k: "m*(2*pi/T)^2" } },
      { name: "Om qonuni  I = U / R", vars: [V("I", "I", "A"), V("U", "U", "V"), V("R", "R", "Ω")], solve: { I: "U/R", U: "I*R", R: "U/I" } },
      { name: "Elektr quvvati  P = U·I", vars: [V("P", "P", "W"), V("U", "U", "V"), V("I", "I", "A")], solve: { P: "U*I", U: "P/I", I: "P/U" } },
      { name: "Joul–Lens  Q = I²Rt", vars: [V("Q", "Q", "J"), V("I", "I", "A"), V("R", "R", "Ω"), V("t", "t", "s")], solve: { Q: "I^2*R*t", I: "sqrt(Q/(R*t))", R: "Q/(I^2*t)", t: "Q/(I^2*R)" } },
      { name: "Issiqlik miqdori  Q = c·m·ΔT", vars: [V("Q", "Q", "J"), V("c", "c", "J/(kg·K)"), V("m", "m", "kg"), V("dT", "ΔT", "K")], solve: { Q: "c*m*dT", c: "Q/(m*dT)", m: "Q/(c*dT)", dT: "Q/(c*m)" } },
      { name: "Kulon qonuni  F = k·q₁q₂/r²", vars: [V("F", "F", "N"), V("q1", "q₁", "C"), V("q2", "q₂", "C"), V("r", "r", "m")], solve: { F: "8.99e9*q1*q2/r^2", r: "sqrt(8.99e9*q1*q2/F)" } },
      { name: "Ideal gaz  pV = nRT", vars: [V("p", "p", "Pa"), V("V", "V", "m³"), V("n", "n", "mol"), V("T", "T", "K")], solve: { p: "n*8.314*T/V", V: "n*8.314*T/p", n: "p*V/(8.314*T)", T: "p*V/(n*8.314)" } },
      { name: "To'lqin  λ = v / f", vars: [V("l", "λ", "m"), V("v", "v", "m/s"), V("f", "f", "Hz")], solve: { l: "v/f", v: "l*f", f: "v/l" } },
      { name: "Foton energiyasi  E = h·f", vars: [V("E", "E", "J"), V("f", "f", "Hz")], solve: { E: "6.626e-34*f", f: "E/6.626e-34" } },
      { name: "Sindirish ko'rsatkichi  n = c / v", vars: [V("n", "n"), V("v", "v", "m/s")], solve: { n: "3e8/v", v: "3e8/n" } },
    ],
    chemistry: [
      { name: "Modda miqdori  n = m / M", vars: [V("n", "n", "mol"), V("m", "m", "g"), V("M", "M", "g/mol")], solve: { n: "m/M", m: "n*M", M: "m/n" } },
      { name: "Gaz hajmi  n = V / Vₘ  (Vₘ = 22,4 l/mol)", vars: [V("n", "n", "mol"), V("V", "V", "l")], solve: { n: "V/22.4", V: "n*22.4" } },
      { name: "Molyar konsentratsiya  C = n / V", vars: [V("C", "C", "mol/l"), V("n", "n", "mol"), V("V", "V", "l")], solve: { C: "n/V", n: "C*V", V: "n/C" } },
      { name: "Massa ulushi  ω = m(modda)/m(eritma)·100", vars: [V("w", "ω", "%"), V("m1", "m(modda)", "g"), V("m2", "m(eritma)", "g")], solve: { w: "m1/m2*100", m1: "w*m2/100", m2: "m1*100/w" } },
      { name: "Elementning massa ulushi  ω = n·Ar/Mr·100", vars: [V("w", "ω", "%"), V("n", "atomlar soni n"), V("Ar", "Ar"), V("Mr", "Mr")], solve: { w: "n*Ar/Mr*100", Mr: "n*Ar*100/w", Ar: "w*Mr/(100*n)" } },
      { name: "Zarrachalar soni  N = n·Nₐ", vars: [V("N", "N"), V("n", "n", "mol")], solve: { N: "n*6.022e23", n: "N/6.022e23" } },
      { name: "Suyultirish  C₁V₁ = C₂V₂", vars: [V("C1", "C₁"), V("V1", "V₁"), V("C2", "C₂"), V("V2", "V₂")], solve: { C1: "C2*V2/V1", V1: "C2*V2/C1", C2: "C1*V1/V2", V2: "C1*V1/C2" } },
      { name: "pH  (pH = −lg[H⁺])", vars: [V("pH", "pH"), V("c", "[H⁺]", "mol/l")], solve: { pH: "-log(c)", c: "10^(-pH)" } },
      { name: "Ideal gaz  pV = nRT  (kPa, l)", vars: [V("p", "p", "kPa"), V("V", "V", "l"), V("n", "n", "mol"), V("T", "T", "K")], solve: { p: "n*8.314*T/V", V: "n*8.314*T/p", n: "p*V/(8.314*T)", T: "p*V/(n*8.314)" } },
      { name: "Unum (mahsulot chiqishi)  η = m(amaliy)/m(nazariy)·100", vars: [V("eta", "η", "%"), V("mp", "m(amaliy)", "g"), V("mt", "m(nazariy)", "g")], solve: { eta: "mp/mt*100", mp: "eta*mt/100", mt: "mp*100/eta" } },
      { name: "Nisbiy zichlik  D = M₁ / M₂", vars: [V("D", "D"), V("M1", "M₁"), V("M2", "M₂")], solve: { D: "M1/M2", M1: "D*M2", M2: "M1/D" } },
    ],
    biology: [
      { name: "Hardi–Vaynberg  (q → p, p², 2pq, q²)", vars: [V("q", "q (retsessiv allel chastotasi)")], outputs: [["p", "p", "1-q"], ["p2", "p² (AA)", "p^2"], ["pq2", "2pq (Aa)", "2*p*q"], ["q2", "q² (aa)", "q^2"]] },
      { name: "GC-tarkib  (A, T, G, C → %)", vars: [V("A", "A"), V("T", "T"), V("G", "G"), V("C", "C")], outputs: [["gc", "G+C ulushi", "(G+C)/(A+T+G+C)*100", "%"], ["at", "A+T ulushi", "(A+T)/(A+T+G+C)*100", "%"], ["n", "Jami nukleotid", "A+T+G+C"]] },
      { name: "DNK o'lchami  (n nukleotid juftligi)", vars: [V("n", "Nukleotid juftligi soni")], outputs: [["L", "Uzunligi", "n*0.34", "nm"], ["M", "Taxminiy massasi", "n*2*345", "Da"]] },
      { name: "Gametalar / genotiplar  (n juft gen, geterozigota)", vars: [V("n", "n")], outputs: [["g", "Gameta turlari  2ⁿ", "2^n"], ["gen", "Genotiplar  3ⁿ", "3^n"], ["fen", "Fenotiplar  2ⁿ (to'liq dominantlik)", "2^n"], ["zig", "F₂ zigotalar  4ⁿ", "4^n"]] },
      { name: "Foiz  (qism / butun)", vars: [V("w", "Foiz", "%"), V("q", "Qism"), V("b", "Butun")], solve: { w: "q/b*100", q: "w*b/100", b: "q*100/w" } },
      { name: "Energiya (ATF)  jami = soni · 38 / 2", vars: [V("E", "ATF soni"), V("n", "glyukoza molekulalari soni n")], solve: { E: "n*38", n: "E/38" } },
      { name: "Oqsil: aminokislota ↔ nukleotid", vars: [V("aa", "Aminokislotalar soni"), V("nt", "Nukleotidlar (kodlovchi)")], solve: { nt: "aa*3", aa: "nt/3" } },
    ],
  };
  const CONSTANTS = {
    physics: [["g", "9.8", "m/s² (erkin tushish)"], ["g₀", "9.81", "m/s²"], ["c", "3e8", "m/s (yorug'lik)"], ["h", "6.626e-34", "J·s (Plank)"], ["G", "6.674e-11", "N·m²/kg²"], ["k", "8.99e9", "N·m²/C²"], ["e", "1.6e-19", "C (elementar zaryad)"], ["Nₐ", "6.022e23", "1/mol"], ["R", "8.314", "J/(mol·K)"], ["kB", "1.38e-23", "J/K (Boltsman)"], ["mₑ", "9.11e-31", "kg (elektron)"], ["mₚ", "1.67e-27", "kg (proton)"]],
    chemistry: [["Nₐ", "6.022e23", "1/mol"], ["Vₘ", "22.4", "l/mol (n.sh.)"], ["R", "8.314", "J/(mol·K)"], ["F", "96500", "C/mol (Faradey)"]],
    biology: [],
    math: [["π", "pi", ""], ["e", "e", "Eyler soni"]],
  };
  const SUBJECTS_ON = ["math", "physics", "chemistry", "biology"];

  // ================================== UI ==================================
  const body = document.body;
  const subject = body.dataset.subject;
  if (SUBJECTS_ON.indexOf(subject) === -1) return;

  const $ = (sel, el) => (el || document).querySelector(sel);
  const h = (tag, cls, html) => { const x = document.createElement(tag); if (cls) x.className = cls; if (html != null) x.innerHTML = html; return x; };
  const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  const state = { angle: "deg", vars: {}, ans: 0, history: [], tab: "calc" };
  try { const a = localStorage.getItem("lz_calc_angle"); if (a === "rad" || a === "deg") state.angle = a; } catch (e) {}

  const toggleBtn = h("button", "calc-toggle",
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="2" width="14" height="20" rx="2"/><rect x="8" y="5" width="8" height="4" rx="1"/><path d="M8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01M16 17h.01"/></svg><span>Kalkulyator</span>');
  toggleBtn.type = "button"; toggleBtn.title = "Kalkulyator"; toggleBtn.setAttribute("aria-expanded", "false");

  const panel = h("aside", "calc-panel");
  panel.hidden = true; panel.setAttribute("role", "dialog"); panel.setAttribute("aria-label", "Kalkulyator");
  const hasSolver = !!FORMULAS[subject];
  const tabs3 = subject === "chemistry" ? '<button type="button" data-tab="molar">Molyar massa</button>' : "";
  panel.innerHTML =
    '<div class="calc-head"><b>Kalkulyator</b>' +
    '<div class="calc-head-r"><button type="button" class="calc-angle" title="Burchak birligi"></button>' +
    '<button type="button" class="calc-x" aria-label="Yopish">&times;</button></div></div>' +
    '<div class="calc-tabs"><button type="button" data-tab="calc" class="on">Hisoblash</button>' +
    (hasSolver ? '<button type="button" data-tab="solve">Formulalar</button>' : "") + tabs3 + '</div>' +
    '<div class="calc-view" data-view="calc">' +
      '<div class="calc-screen"><input type="text" class="calc-input" inputmode="text" autocomplete="off" spellcheck="false" placeholder="Masalan: 2*pi*5  yoki  m=2" aria-label="Ifoda">' +
      '<div class="calc-result" aria-live="polite">0</div></div>' +
      '<div class="calc-vars" hidden></div>' +
      '<div class="calc-keys"></div>' +
      '<div class="calc-consts"></div>' +
      '<div class="calc-hist"></div>' +
    '</div>' +
    (hasSolver ? '<div class="calc-view" data-view="solve" hidden><select class="calc-formula" aria-label="Formula"></select><div class="calc-form"></div><div class="calc-out" aria-live="polite"></div></div>' : "") +
    (subject === "chemistry" ? '<div class="calc-view" data-view="molar" hidden><input type="text" class="calc-mf" placeholder="Formula: H2SO4, Ca(OH)2, CuSO4*5H2O" autocomplete="off" spellcheck="false"><div class="calc-out calc-mout"></div></div>' : "");

  const input = $(".calc-input", panel), resultEl = $(".calc-result", panel), angleBtn = $(".calc-angle", panel);

  const KEYS = [
    ["sin(", "sin"], ["cos(", "cos"], ["tan(", "tan"], ["ctg(", "ctg"], ["^", "xʸ"],
    ["asin(", "sin⁻¹"], ["acos(", "cos⁻¹"], ["atan(", "tan⁻¹"], ["sqrt(", "√"], ["^2", "x²"],
    ["log(", "lg"], ["ln(", "ln"], ["pi", "π"], ["e", "e"], ["!", "n!"],
    ["(", "("], [")", ")"], ["%", "%"], ["CLR", "C", "k-fn"], ["DEL", "⌫", "k-fn"],
    ["7", "7", "k-n"], ["8", "8", "k-n"], ["9", "9", "k-n"], ["/", "÷", "k-op"], ["root(", "ⁿ√"],
    ["4", "4", "k-n"], ["5", "5", "k-n"], ["6", "6", "k-n"], ["*", "×", "k-op"], ["1/(", "1/x"],
    ["1", "1", "k-n"], ["2", "2", "k-n"], ["3", "3", "k-n"], ["-", "−", "k-op"], ["ans", "Ans"],
    ["0", "0", "k-n"], [".", ".", "k-n"], ["e+", "EXP"], ["+", "+", "k-op"], ["=", "=", "k-eq"],
  ];
  const keysEl = $(".calc-keys", panel);
  KEYS.forEach(([val, label, cls]) => { const b = h("button", "calc-key " + (cls || ""), esc(label)); b.type = "button"; b.dataset.k = val; keysEl.appendChild(b); });

  function updateAngle() { angleBtn.textContent = state.angle === "deg" ? "DEG" : "RAD"; angleBtn.classList.toggle("rad", state.angle === "rad"); }
  updateAngle();

  function insert(text) {
    const s = input.selectionStart == null ? input.value.length : input.selectionStart, e2 = input.selectionEnd == null ? s : input.selectionEnd;
    input.value = input.value.slice(0, s) + text + input.value.slice(e2);
    const pos = s + text.length; input.setSelectionRange(pos, pos); input.focus(); preview();
  }
  function scope() { return Object.assign({}, state.vars, { ans: state.ans }); }
  function preview() {
    const v = input.value.trim();
    if (!v) { resultEl.textContent = state.history.length ? Core.fmt(state.ans) : "0"; resultEl.classList.remove("err"); return; }
    try { const r = Core.evaluate(v, scope(), state.angle); resultEl.textContent = (r.assigned ? r.assigned + " = " : "") + Core.fmt(r.value); resultEl.classList.remove("err"); }
    catch (e) { resultEl.classList.remove("err"); }
  }
  function commit() {
    const v = input.value.trim(); if (!v) return;
    try {
      const r = Core.evaluate(v, scope(), state.angle);
      if (r.assigned) state.vars[r.assigned] = r.value; else state.ans = r.value;
      state.history.unshift({ expr: v, res: Core.fmt(r.value), name: r.assigned || "" });
      state.history = state.history.slice(0, 12);
      resultEl.textContent = (r.assigned ? r.assigned + " = " : "") + Core.fmt(r.value); resultEl.classList.remove("err");
      input.value = ""; renderVars(); renderHist();
    } catch (e) { resultEl.textContent = e.message; resultEl.classList.add("err"); }
  }
  function renderVars() {
    const box = $(".calc-vars", panel), names = Object.keys(state.vars);
    box.hidden = !names.length; box.innerHTML = "";
    names.forEach((n) => { const c = h("button", "calc-chip", esc(n) + " = " + esc(Core.fmt(state.vars[n])) + " <i>&times;</i>"); c.type = "button"; c.dataset.v = n; box.appendChild(c); });
  }
  function renderHist() {
    const box = $(".calc-hist", panel); box.innerHTML = "";
    state.history.forEach((it) => { const row = h("button", "calc-h", '<span>' + esc(it.expr) + '</span><b>' + (it.name ? esc(it.name) + " = " : "= ") + esc(it.res) + '</b>'); row.type = "button"; row.dataset.val = it.res; row.dataset.expr = it.expr; box.appendChild(row); });
  }
  function renderConsts() {
    const box = $(".calc-consts", panel), list = CONSTANTS[subject] || []; box.innerHTML = "";
    if (!list.length) { box.hidden = true; return; }
    list.forEach(([name, val, desc]) => { const b = h("button", "calc-chip c-const", esc(name)); b.type = "button"; b.title = name + " = " + (val === "pi" ? "3.14159…" : val) + (desc ? "  (" + desc + ")" : ""); b.dataset.val = val; box.appendChild(b); });
  }
  renderConsts();

  keysEl.addEventListener("click", (e) => {
    const b = e.target.closest(".calc-key"); if (!b) return; const k = b.dataset.k;
    if (k === "CLR") { input.value = ""; resultEl.classList.remove("err"); resultEl.textContent = "0"; input.focus(); }
    else if (k === "DEL") { const s = input.selectionStart || input.value.length; if (s > 0) { input.value = input.value.slice(0, s - 1) + input.value.slice(s); input.setSelectionRange(s - 1, s - 1); } input.focus(); preview(); }
    else if (k === "=") commit();
    else insert(k);
  });
  input.addEventListener("input", preview);
  input.addEventListener("keydown", (e) => { if (e.key === "Enter") { e.preventDefault(); commit(); } e.stopPropagation(); });
  $(".calc-consts", panel).addEventListener("click", (e) => { const b = e.target.closest(".calc-chip"); if (b) insert(b.dataset.val); });
  $(".calc-vars", panel).addEventListener("click", (e) => { const c = e.target.closest(".calc-chip"); if (!c) return; if (e.target.tagName === "I") { delete state.vars[c.dataset.v]; renderVars(); preview(); } else insert(c.dataset.v); });
  $(".calc-hist", panel).addEventListener("click", (e) => { const r = e.target.closest(".calc-h"); if (r) insert(r.dataset.val); });
  angleBtn.addEventListener("click", () => { state.angle = state.angle === "deg" ? "rad" : "deg"; try { localStorage.setItem("lz_calc_angle", state.angle); } catch (e) {} updateAngle(); preview(); });

  // ---- Tabs ----
  panel.querySelector(".calc-tabs").addEventListener("click", (e) => {
    const b = e.target.closest("button[data-tab]"); if (!b) return;
    state.tab = b.dataset.tab;
    panel.querySelectorAll(".calc-tabs button").forEach((x) => x.classList.toggle("on", x === b));
    panel.querySelectorAll(".calc-view").forEach((v) => { v.hidden = v.dataset.view !== state.tab; });
    angleBtn.style.visibility = state.tab === "molar" ? "hidden" : "visible";
  });

  // ---- Formula yechuvchi ----
  if (hasSolver) {
    const sel = $(".calc-formula", panel), form = $(".calc-form", panel);
    const list = FORMULAS[subject];
    list.forEach((f, i) => { const o = document.createElement("option"); o.value = i; o.textContent = f.name; sel.appendChild(o); });
    const solveOut = panel.querySelector('[data-view="solve"] .calc-out');
    function renderForm() {
      const f = list[+sel.value]; form.innerHTML = ""; solveOut.innerHTML = "";
      f.vars.forEach(([sym, label, unit]) => {
        const row = h("label", "calc-field", '<span>' + esc(label) + (unit ? ' <small>' + esc(unit) + '</small>' : "") + '</span>');
        const inp = h("input"); inp.type = "text"; inp.autocomplete = "off"; inp.spellcheck = false; inp.dataset.sym = sym;
        inp.placeholder = f.outputs ? "kiriting" : "noma'lum — bo'sh qoldiring"; row.appendChild(inp); form.appendChild(row);
      });
      const go = h("button", "calc-go", f.outputs ? "Hisoblash" : "Topish"); go.type = "button"; form.appendChild(go);
    }
    function runSolve() {
      const f = list[+sel.value], vals = {};
      form.querySelectorAll("input").forEach((i) => { vals[i.dataset.sym] = i.value; });
      try {
        const res = Core.solveFormula(f, vals, state.angle);
        solveOut.innerHTML = res.map((r) => '<div class="calc-ans"><span>' + esc(r.label) + '</span><b>' + esc(r.text) + (r.unit ? ' <small>' + esc(r.unit) + '</small>' : "") + '</b></div>').join("");
        solveOut.classList.remove("err");
        if (res.length === 1 && res[0].value != null && !f.outputs) { const t = form.querySelector('input[data-sym="' + res[0].sym + '"]'); if (t) t.placeholder = Core.fmt(res[0].value); }
        if (res[0] && res[0].value != null) state.ans = res[0].value;
      } catch (e) { solveOut.innerHTML = '<div class="calc-err">' + esc(e.message) + "</div>"; }
    }
    sel.addEventListener("change", renderForm);
    form.addEventListener("click", (e) => { if (e.target.classList.contains("calc-go")) runSolve(); });
    form.addEventListener("keydown", (e) => { if (e.key === "Enter") { e.preventDefault(); runSolve(); } e.stopPropagation(); });
    renderForm();
  }

  // ---- Molyar massa (kimyo) ----
  if (subject === "chemistry") {
    const mf = $(".calc-mf", panel), mo = $(".calc-mout", panel);
    function runMolar() {
      const v = mf.value.trim(); if (!v) { mo.innerHTML = ""; return; }
      try {
        const r = Core.molarMass(v);
        const rows = r.rows.map((x) => '<tr><td>' + esc(x.sym) + '</td><td>' + x.n + '</td><td>' + Core.fmt(x.ar) + '</td><td>' + Core.fmt(x.ar * x.n) + '</td></tr>').join("");
        mo.innerHTML = '<table class="calc-tbl"><tr><th>Element</th><th>Soni</th><th>Ar</th><th>Jami</th></tr>' + rows + '</table>' +
          '<div class="calc-ans"><span>Mr (aniq)</span><b>' + Core.fmt(Math.round(r.exact * 1000) / 1000) + '</b></div>' +
          '<div class="calc-ans"><span>Mr (maktab, Cl=35,5)</span><b>' + Core.fmt(r.school) + '</b></div>';
      } catch (e) { mo.innerHTML = '<div class="calc-err">' + esc(e.message) + "</div>"; }
    }
    mf.addEventListener("input", runMolar);
    mf.addEventListener("keydown", (e) => e.stopPropagation());
  }

  // ---- Ochish/yopish ----
  function setOpen(open) {
    panel.hidden = !open; toggleBtn.setAttribute("aria-expanded", open ? "true" : "false"); toggleBtn.classList.toggle("on", open);
    if (open) { positionTop(); setTimeout(() => { if (state.tab === "calc") input.focus(); }, 30); }
  }
  function positionTop() { const hd = document.querySelector(".site-header"); panel.style.top = ((hd ? hd.getBoundingClientRect().bottom : 56) + 8) + "px"; }
  toggleBtn.addEventListener("click", () => setOpen(panel.hidden));
  $(".calc-x", panel).addEventListener("click", () => setOpen(false));
  window.addEventListener("resize", () => { if (!panel.hidden) positionTop(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !panel.hidden) setOpen(false); });

  // Tugma: taymer yonida (shikoyat tugmasidan oldin)
  const timerEl = document.getElementById("quiz-timer");
  if (timerEl && timerEl.parentNode) timerEl.parentNode.insertBefore(toggleBtn, timerEl.nextSibling);
  else document.body.appendChild(toggleBtn);
  document.body.appendChild(panel);
})(typeof window !== "undefined" ? window : globalThis);
