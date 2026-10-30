/* LongoUZ — test oynasidagi yordamchi vositalar:
   1) "Shikoyat" tugmasi + o'ng yon panel (savol bo'yicha xato/kamchilik yuborish — admin panelga tushadi);
   2) Fanga mos KALKULYATOR (matematika, fizika, kimyo, biologiya) — formula kiritish, tenglama yechish, fanga xos asboblar;
   3) Ochiq (yozma) javob inputi uchun fanga xos BELGILAR klaviaturasi (tarix va tillar fanlarida chiqmaydi). */
(function () {
  "use strict";
  var body = document.body;
  var subject = body.dataset.subject || "";
  var token = body.dataset.attemptToken || "";
  var CALC_SUBJECTS = { math: 1, physics: 1, chemistry: 1, biology: 1 };
  var C = window.LZCalc;

  function el(tag, cls, html) { var n = document.createElement(tag); if (cls) n.className = cls; if (html != null) n.innerHTML = html; return n; }
  function esc(t) { var d = document.createElement("div"); d.textContent = String(t == null ? "" : t); return d.innerHTML; }
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  var Q = function () { return window.LZQuiz || null; };

  // =================================================================== BIRGA OCHILADIGAN YON PANELLAR
  function closeOthers(except) {
    $$(".lz-drawer.is-open").forEach(function (d) { if (d !== except) setDrawer(d, false); });
    var fs = document.getElementById("formula-sheet-overlay");
    if (fs && fs.classList.contains("is-open")) { var t = document.getElementById("formula-sheet-toggle"); if (t) t.click(); }
  }
  function setDrawer(d, open) {
    d.classList.toggle("is-open", open);
    d.setAttribute("aria-hidden", open ? "false" : "true");
    if (open) closeOthers(d);
  }

  // =================================================================== 1) SHIKOYAT
  var CATS = [
    ["wrong_answer", "To'g'ri javob noto'g'ri belgilangan"], ["no_correct", "To'g'ri javob variantlar orasida yo'q"],
    ["question_text", "Savol matnida xato yoki tushunarsiz"], ["options", "Variantlar noto'g'ri yoki takrorlangan"],
    ["figure", "Chizma / rasm xato yoki ko'rinmayapti"], ["topic", "Savol bu fan/mavzuga tegishli emas"],
    ["explanation", "Izoh (yechim) noto'g'ri"], ["typo", "Imlo / yozuv xatosi"], ["duplicate", "Savol takrorlanyapti"], ["other", "Boshqa"]
  ];
  var reportBtn, reportDrawer;
  function buildReport() {
    reportBtn = el("button", "lz-tool-btn lz-report-btn", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg><span>Shikoyat</span>');
    reportBtn.type = "button"; reportBtn.title = "Shu savol bo'yicha shikoyat qilish";
    reportDrawer = el("aside", "lz-drawer lz-report");
    reportDrawer.setAttribute("aria-hidden", "true");
    reportDrawer.innerHTML =
      '<div class="lz-drawer-card"><div class="lz-drawer-head"><h3>Savol bo\'yicha shikoyat</h3><button type="button" class="lz-x" aria-label="Yopish">&times;</button></div>' +
      '<div class="lz-drawer-scroll"><div id="lzr-form">' +
      '<p class="lz-muted" id="lzr-ctx"></p>' +
      '<div class="lz-qprev" id="lzr-q"></div>' +
      '<label class="lz-lab">Nima xato?</label><div class="lz-cats" id="lzr-cats">' +
      CATS.map(function (c, i) { return '<label class="lz-cat"><input type="radio" name="lzr-cat" value="' + c[0] + '"' + (i === 0 ? " checked" : "") + "><span>" + c[1] + "</span></label>"; }).join("") +
      '</div><label class="lz-lab" for="lzr-msg">Batafsil yozing <small>(masalan: qaysi javob to\'g\'ri deb o\'ylaysiz, nima uchun)</small></label>' +
      '<textarea id="lzr-msg" rows="5" maxlength="1500" placeholder="Kamchilik haqida qisqa yozing…"></textarea>' +
      '<p class="lz-err" id="lzr-err" hidden></p>' +
      '<button type="button" class="lz-primary" id="lzr-send">Yuborish</button>' +
      '<p class="lz-muted">Shikoyat adminlarga yuboriladi va savol tekshirib tuzatiladi. Test vaqti to\'xtamaydi.</p></div>' +
      '<div id="lzr-done" hidden><div class="lz-done-ico">✓</div><h4>Rahmat!</h4><p>Shikoyatingiz yuborildi. Savolni tekshirib, kerak bo\'lsa tuzatamiz.</p><button type="button" class="lz-secondary" id="lzr-close2">Testga qaytish</button></div>' +
      "</div></div>";
    document.body.appendChild(reportDrawer);
    reportBtn.addEventListener("click", function () { var open = !reportDrawer.classList.contains("is-open"); if (open) fillReportCtx(); setDrawer(reportDrawer, open); if (open) setTimeout(function () { var t = $("#lzr-msg"); if (t) t.focus(); }, 250); });
    $(".lz-x", reportDrawer).addEventListener("click", function () { setDrawer(reportDrawer, false); });
    $("#lzr-close2").addEventListener("click", function () { setDrawer(reportDrawer, false); });
    $("#lzr-send").addEventListener("click", sendReport);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") $$(".lz-drawer.is-open").forEach(function (d) { setDrawer(d, false); }); });
    window.addEventListener("lz:question", function () { if (reportDrawer.classList.contains("is-open")) fillReportCtx(); });
  }
  function fillReportCtx() {
    var st = Q(); if (!st) return;
    var q = st.question; if (!q) return;
    $("#lzr-ctx").textContent = (st.index + 1) + "-savol";
    $("#lzr-q").textContent = q.question.length > 260 ? q.question.slice(0, 260) + "…" : q.question;
    $("#lzr-form").hidden = false; $("#lzr-done").hidden = true; $("#lzr-err").hidden = true;
    $("#lzr-msg").value = ""; var first = $('input[name="lzr-cat"]', reportDrawer); if (first) first.checked = true;
    $("#lzr-send").disabled = false; $("#lzr-send").textContent = "Yuborish";
  }
  function sendReport() {
    var st = Q(); if (!st || !st.question) return;
    var cat = ($('input[name="lzr-cat"]:checked', reportDrawer) || {}).value || "other";
    var msg = $("#lzr-msg").value.trim(), err = $("#lzr-err");
    if (cat === "other" && !msg) { err.textContent = "Iltimos, nima xato ekanini yozing."; err.hidden = false; return; }
    var a = st.answer, sel = "";
    if (typeof a === "number" && st.question.options) sel = ("ABCD"[a] || a) + ") " + st.question.options[a]; else if (typeof a === "string") sel = a;
    var btn = $("#lzr-send"); btn.disabled = true; btn.textContent = "Yuborilmoqda…";
    fetch("/api/report-question", {
      method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ attempt_token: token, index: st.index, category: cat, message: msg, selected: sel })
    }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok) throw new Error(j.detail || "Yuborib bo'lmadi"); return j; }); })
      .then(function () { $("#lzr-form").hidden = true; $("#lzr-done").hidden = false; reportBtn.classList.add("is-sent"); setTimeout(function () { reportBtn.classList.remove("is-sent"); }, 2500); })
      .catch(function (e) { err.textContent = e.message; err.hidden = false; btn.disabled = false; btn.textContent = "Yuborish"; });
  }

  // =================================================================== 2) KALKULYATOR
  var calc, calcBtn, calcState, calcDeg = true, school = true, lastResult = "";
  function buildCalc() {
    if (!CALC_SUBJECTS[subject] || !C) return;
    calcState = C.newState(true);
    calcBtn = el("button", "lz-tool-btn lz-calc-btn", '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M8 6h8M8 11h2m4 0h2M8 15h2m4 0h2M8 19h2m4 0h2"/></svg><span>Kalkulyator</span>');
    calcBtn.type = "button"; calcBtn.title = "Fanga mos kalkulyator";
    calc = el("div", "lzc"); calc.hidden = true;
    var tabs = [["calc", "Hisob"]].concat(subjectTabs());
    calc.innerHTML =
      '<div class="lzc-head" id="lzc-drag"><b>Kalkulyator</b><span class="lzc-sub">' + ({ math: "Matematika", physics: "Fizika", chemistry: "Kimyo", biology: "Biologiya" }[subject]) + '</span>' +
      '<button type="button" class="lzc-mini" id="lzc-deg" title="Burchak birligi">DEG</button><button type="button" class="lz-x" id="lzc-close" aria-label="Yopish">&times;</button></div>' +
      '<div class="lzc-tabs">' + tabs.map(function (t, i) { return '<button type="button" data-tab="' + t[0] + '"' + (i === 0 ? ' class="on"' : "") + ">" + t[1] + "</button>"; }).join("") + "</div>" +
      '<div class="lzc-body"><div class="lzc-pane" data-pane="calc">' + calcPaneHtml() + "</div>" +
      tabs.slice(1).map(function (t) { return '<div class="lzc-pane" data-pane="' + t[0] + '" hidden></div>'; }).join("") + "</div>";
    document.body.appendChild(calc);
    calcBtn.addEventListener("click", function () { calc.hidden = !calc.hidden; document.body.classList.toggle("lz-tool-open", !calc.hidden); calcBtn.classList.toggle("is-active", !calc.hidden); if (!calc.hidden) { var i = $("#lzc-in"); if (i && window.innerWidth > 700) i.focus(); } });
    $("#lzc-close").addEventListener("click", function () { calc.hidden = true; document.body.classList.remove("lz-tool-open"); calcBtn.classList.remove("is-active"); });
    $("#lzc-deg").addEventListener("click", function () { calcDeg = !calcDeg; calcState.deg = calcDeg; this.textContent = calcDeg ? "DEG" : "RAD"; runCalc(); });
    $$(".lzc-tabs button", calc).forEach(function (b) {
      b.addEventListener("click", function () {
        $$(".lzc-tabs button", calc).forEach(function (x) { x.classList.toggle("on", x === b); });
        $$(".lzc-pane", calc).forEach(function (p) { p.hidden = p.dataset.pane !== b.dataset.tab; });
        var pane = $('.lzc-pane[data-pane="' + b.dataset.tab + '"]', calc);
        if (pane && !pane.dataset.built) { pane.dataset.built = "1"; buildTool(b.dataset.tab, pane); }
      });
    });
    wireCalcPane();
    makeDraggable(calc, $("#lzc-drag"));
  }
  function subjectTabs() {
    if (subject === "math") return [["formula", "Formulalar"], ["eq", "Tenglama"], ["comb", "Kombinatorika"], ["pct", "Foiz"]];
    if (subject === "physics") return [["formula", "Formulalar"], ["const", "Doimiylar"], ["units", "Birliklar"]];
    if (subject === "chemistry") return [["molar", "Molyar massa"], ["balance", "Tenglashtirish"], ["formula", "Formulalar"]];
    if (subject === "biology") return [["gen", "DNK / RNK"], ["chargaff", "Chargaff"], ["hw", "Hardy–Weinberg"], ["mendel", "Mendel"]];
    return [];
  }
  var KEYS = [
    ["sin(", "cos(", "tan(", "π", "e"], ["asin(", "acos(", "atan(", "^2", "√("], ["(", ")", "^", "!", "%"],
    ["7", "8", "9", "/", "⌫"], ["4", "5", "6", "*", "C"], ["1", "2", "3", "-", "ln("], ["0", ".", "x", "+", "log("]
  ];
  var KEYLABEL = { "^2": "x²", "√(": "√", "^": "xʸ", "/": "÷", "*": "×", "-": "−", "!": "n!", "⌫": "⌫" };
  function calcPaneHtml() {
    var keys = KEYS.map(function (row) { return row.map(function (k) { var cls = /^\d$|^\.$/.test(k) ? "num" : (k === "C" || k === "⌫") ? "clr" : /^[\/*\-+]$/.test(k) ? "op" : ""; return '<button type="button" class="' + cls + '" data-k="' + esc(k) + '">' + esc(KEYLABEL[k] || k) + "</button>"; }).join(""); }).join("");
    var consts = subject === "physics" || subject === "chemistry" ? '<select id="lzc-const" class="lzc-sel"><option value="">+ doimiy</option>' + C.CONST_INFO.map(function (c) { return '<option value="' + c[0] + '">' + c[0] + " — " + c[1] + " (" + c[2] + ")</option>"; }).join("") + "</select>" : "";
    return '<input id="lzc-in" class="lzc-in" type="text" autocomplete="off" spellcheck="false" placeholder="Ifoda yoki formula: 2+3*4, sin(30), x^2-5x+6=0">' +
      '<div class="lzc-out" id="lzc-out">&nbsp;</div>' +
      '<div class="lzc-row"><button type="button" class="lzc-mini" id="lzc-ans">Ans</button><button type="button" class="lzc-mini" id="lzc-e10">×10ⁿ</button>' + consts + '<button type="button" class="lzc-mini" id="lzc-copy" hidden>Javobga →</button></div>' +
      '<div class="lzc-keys">' + keys + '<button type="button" class="eq" id="lzc-exe">=</button></div>' +
      '<div class="lzc-hist" id="lzc-hist"></div>' +
      '<p class="lzc-help">Formula kiriting: <code>a=3; b=4; sqrt(a^2+b^2)</code> yoki tenglama: <code>2x+3=11</code>. Funksiya argumentlari: <code>log(8;2)</code>.</p>';
  }
  function insertAt(inp, text) {
    var s = inp.selectionStart == null ? inp.value.length : inp.selectionStart, e = inp.selectionEnd == null ? s : inp.selectionEnd;
    inp.setRangeText(text, s, e, "end");
    inp.dispatchEvent(new Event("input", { bubbles: true }));
  }
  function runCalc(commit) {
    var inp = $("#lzc-in"), out = $("#lzc-out"); if (!inp) return;
    var st = commit ? calcState : { vars: Object.assign({}, calcState.vars), deg: calcDeg, ans: calcState.ans };
    calcState.deg = calcDeg; st.deg = calcDeg;
    var r = C.run(inp.value, st);
    out.className = "lzc-out" + (r.kind === "error" ? " err" : "");
    if (r.kind === "empty") { out.innerHTML = "&nbsp;"; $("#lzc-copy").hidden = true; return; }
    if (r.kind === "error" && !commit) { out.textContent = "…"; out.className = "lzc-out"; return; }
    out.textContent = r.text;
    lastResult = r.plain || ""; $("#lzc-copy").hidden = !lastResult || !currentOpenInput();
    if (commit && r.kind !== "error") {
      var h = $("#lzc-hist"), item = el("button", "lzc-h", "<span>" + esc(inp.value) + "</span><b>" + esc(r.text) + "</b>");
      item.type = "button"; item.addEventListener("click", function () { inp.value = item.firstChild.textContent; runCalc(); inp.focus(); });
      h.insertBefore(item, h.firstChild); while (h.children.length > 8) h.removeChild(h.lastChild);
    }
  }
  function currentOpenInput() { return document.querySelector(".quiz-open-answer input"); }
  function wireCalcPane() {
    var inp = $("#lzc-in");
    inp.addEventListener("input", function () { runCalc(false); });
    inp.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); runCalc(true); } });
    $$(".lzc-keys button[data-k]", calc).forEach(function (b) {
      b.addEventListener("mousedown", function (e) { e.preventDefault(); });
      b.addEventListener("click", function () {
        var k = b.dataset.k;
        if (k === "C") { inp.value = ""; runCalc(); } else if (k === "⌫") { var s = inp.selectionStart; if (s > 0 && inp.selectionEnd === s) { inp.setRangeText("", s - 1, s, "end"); inp.dispatchEvent(new Event("input")); } else { inp.setRangeText("", inp.selectionStart, inp.selectionEnd, "end"); inp.dispatchEvent(new Event("input")); } } else insertAt(inp, k);
        inp.focus();
      });
    });
    $("#lzc-exe").addEventListener("click", function () { runCalc(true); inp.focus(); });
    $("#lzc-ans").addEventListener("click", function () { insertAt(inp, "ans"); inp.focus(); });
    $("#lzc-e10").addEventListener("click", function () { insertAt(inp, "*10^"); inp.focus(); });
    var cs = $("#lzc-const"); if (cs) cs.addEventListener("change", function () { if (cs.value) insertAt(inp, cs.value); cs.value = ""; inp.focus(); });
    $("#lzc-copy").addEventListener("click", function () { var oi = currentOpenInput(); if (oi && lastResult) { oi.value = lastResult.replace(".", oi.dataset.decimal === "," ? "," : "."); oi.dispatchEvent(new Event("input", { bubbles: true })); oi.focus(); } });
  }
  function makeDraggable(box, handle) {
    var sx, sy, ox, oy, drag = false;
    handle.addEventListener("pointerdown", function (e) {
      if (e.target.closest("button") || window.innerWidth <= 700) return;
      drag = true; sx = e.clientX; sy = e.clientY; var r = box.getBoundingClientRect(); ox = r.left; oy = r.top; handle.setPointerCapture(e.pointerId); e.preventDefault();
    });
    handle.addEventListener("pointermove", function (e) { if (!drag) return; box.style.left = Math.max(0, Math.min(window.innerWidth - 80, ox + e.clientX - sx)) + "px"; box.style.top = Math.max(0, Math.min(window.innerHeight - 60, oy + e.clientY - sy)) + "px"; box.style.right = "auto"; box.style.bottom = "auto"; });
    handle.addEventListener("pointerup", function () { drag = false; });
  }

  // ---------------------------------------------------------------- mini-formalar
  function fieldHtml(id, label, val, ph) { return '<label class="lzc-f"><span>' + label + '</span><input type="text" data-f="' + id + '" value="' + esc(val == null ? "" : val) + '" placeholder="' + esc(ph || "") + '" autocomplete="off"></label>'; }
  function num(pane, id) {
    var i = $('[data-f="' + id + '"]', pane); if (!i) return NaN; var v = i.value.trim(); if (!v) return NaN;
    var r = C.run(v, { vars: {}, deg: true, ans: 0 }); return r.kind === "value" ? r.value : NaN;
  }
  function f(x) { return C.fmt(x); }
  function toolShell(pane, title, fieldsHtml, computeFn, hint) {
    pane.innerHTML = '<div class="lzc-tool"><p class="lzc-help">' + (hint || "") + "</p>" + fieldsHtml + '<button type="button" class="lz-primary lzc-go">Hisoblash</button><div class="lzc-res"></div></div>';
    var res = $(".lzc-res", pane);
    function go() { try { var h = computeFn(pane); res.className = "lzc-res"; res.innerHTML = h; } catch (e) { res.className = "lzc-res err"; res.textContent = e.message; } }
    $(".lzc-go", pane).addEventListener("click", go);
    pane.addEventListener("keydown", function (e) { if (e.key === "Enter" && e.target.tagName === "INPUT") { e.preventDefault(); go(); } });
  }
  function rowsHtml(rows) { return rows.map(function (r) { return '<div class="lzc-r"><span>' + r[0] + "</span><b>" + r[1] + "</b></div>"; }).join(""); }

  function buildTool(tab, pane) {
    if (tab === "formula") return buildFormulaSolver(pane);
    if (tab === "const") {
      pane.innerHTML = '<div class="lzc-tool"><p class="lzc-help">Bosing — hisoblash maydoniga qo\'shiladi.</p>' + C.CONST_INFO.map(function (c) { return '<button type="button" class="lzc-const" data-c="' + c[0] + '"><b>' + c[0] + "</b><span>" + c[1] + "</span><em>" + c[2] + "</em></button>"; }).join("") + "</div>";
      $$(".lzc-const", pane).forEach(function (b) { b.addEventListener("click", function () { switchTab("calc"); var i = $("#lzc-in"); insertAt(i, b.dataset.c); i.focus(); }); });
      return;
    }
    if (tab === "units") return buildUnits(pane);
    if (tab === "eq") return buildEq(pane);
    if (tab === "comb") return toolShell(pane, "", fieldHtml2([["n", "n", "10"], ["k", "k", "3"]]), function (p) {
      var n = num(p, "n"), k = num(p, "k"); if (isNaN(n) || isNaN(k)) throw new Error("n va k ni kiriting");
      return rowsHtml([["n!", f(C.fact(n))], ["A(n,k) — o'rinlashtirish", f(C.npr(n, k))], ["C(n,k) — guruhlash", f(C.ncr(n, k))], ["Pₙ = n!", f(C.fact(n))], ["Takrorli o'rinlashtirish nᵏ", f(Math.pow(n, k))]]);
    }, "Kombinatorika: n va k.");
    if (tab === "pct") return toolShell(pane, "", fieldHtml2([["A", "A son", "250"], ["p", "p %", "12"], ["B", "B son (A necha % B dan?)", "1000"]]), function (p) {
      var A = num(p, "A"), pp = num(p, "p"), B = num(p, "B"); var rows = [];
      if (!isNaN(A) && !isNaN(pp)) rows.push([pp + "% of " + A, f(A * pp / 100)], ["A + p%", f(A * (1 + pp / 100))], ["A − p%", f(A * (1 - pp / 100))], ["A soni p% bo'lsa, butun", f(A * 100 / pp)]);
      if (!isNaN(A) && !isNaN(B)) rows.push(["A soni B ning", f(A / B * 100) + " %"]);
      if (!rows.length) throw new Error("A va p (yoki A va B) ni kiriting"); return rowsHtml(rows);
    }, "Foiz hisoblari.");
    if (tab === "molar") return buildMolar(pane);
    if (tab === "balance") return buildBalance(pane);
    if (tab === "gen") return buildGen(pane);
    if (tab === "chargaff") return toolShell(pane, "", fieldHtml2([["A", "A (adenin) %", "20"], ["G", "G (guanin) % (ixtiyoriy)", ""]]), function (p) {
      var a = num(p, "A"), g = num(p, "G"); if (isNaN(a) && isNaN(g)) throw new Error("A yoki G ning foizini kiriting");
      if (isNaN(g)) g = 50 - a; if (isNaN(a)) a = 50 - g;
      return rowsHtml([["A = T", f(a) + " %"], ["G = C", f(g) + " %"], ["A+T", f(2 * a) + " %"], ["G+C", f(2 * g) + " %"], ["Tekshiruv A+G", f(a + g) + " % (=50)"]]);
    }, "Chargaff qoidasi: A = T, G = C, A+G = 50%.");
    if (tab === "hw") return toolShell(pane, "", fieldHtml2([["q2", "q² (retsessiv fenotip ulushi, 0–1)", "0.04"], ["N", "Populyatsiya soni (ixtiyoriy)", "1000"]]), function (p) {
      var q2 = num(p, "q2"), N = num(p, "N"); if (isNaN(q2) || q2 < 0 || q2 > 1) throw new Error("q² 0 dan 1 gacha bo'lsin");
      var q = Math.sqrt(q2), pp = 1 - q, rows = [["q (retsessiv allel)", f(q)], ["p (dominant allel)", f(pp)], ["AA = p²", f(pp * pp)], ["Aa = 2pq", f(2 * pp * q)], ["aa = q²", f(q2)]];
      if (!isNaN(N)) rows.push(["Geterozigotalar soni", f(2 * pp * q * N)]); return rowsHtml(rows);
    }, "Hardy–Weinberg: p + q = 1; p² + 2pq + q² = 1.");
    if (tab === "mendel") return toolShell(pane, "", fieldHtml2([["n", "Geterozigota juft genlar soni (n)", "2"]]), function (p) {
      var n = num(p, "n"); if (isNaN(n) || n < 1 || n > 20) throw new Error("n = 1…20");
      return rowsHtml([["Gameta turlari 2ⁿ", f(Math.pow(2, n))], ["F₂ fenotip sinflari 2ⁿ (to'liq dominantlik)", f(Math.pow(2, n))], ["F₂ genotip sinflari 3ⁿ", f(Math.pow(3, n))], ["F₂ zigota kombinatsiyalari 4ⁿ", f(Math.pow(4, n))], ["Butunlay dominant fenotip ulushi (3/4)ⁿ", f(Math.pow(0.75, n))], ["Butunlay retsessiv ulushi (1/4)ⁿ", f(Math.pow(0.25, n))]]);
    }, "Mendel qonunlari (n juft mustaqil gen, to'liq dominantlik).");
  }
  function fieldHtml2(arr) { return arr.map(function (a) { return fieldHtml(a[0], a[1], a[2]); }).join(""); }
  function switchTab(name) { var b = $('.lzc-tabs button[data-tab="' + name + '"]', calc); if (b) b.click(); }

  function buildEq(pane) {
    pane.innerHTML = '<div class="lzc-tool"><b>Kvadrat tenglama ax²+bx+c=0</b>' + fieldHtml2([["a", "a", "1"], ["b", "b", "-5"], ["c", "c", "6"]]) + '<button type="button" class="lz-primary" data-go="q">Yechish</button><div class="lzc-res" id="lzc-r1"></div>' +
      '<hr><b>Ikki noma\'lumli tizim</b><p class="lzc-help">a₁x + b₁y = c₁,  a₂x + b₂y = c₂</p><div class="lzc-g6">' + fieldHtml2([["a1", "a₁", "2"], ["b1", "b₁", "1"], ["c1", "c₁", "5"], ["a2", "a₂", "1"], ["b2", "b₂", "-1"], ["c2", "c₂", "1"]]) +
      '</div><button type="button" class="lz-primary" data-go="s">Yechish</button><div class="lzc-res" id="lzc-r2"></div></div>';
    $('[data-go="q"]', pane).addEventListener("click", function () {
      var a = num(pane, "a"), b = num(pane, "b"), c = num(pane, "c"), r = $("#lzc-r1"); r.className = "lzc-res";
      if ([a, b, c].some(isNaN) || a === 0) { r.className = "lzc-res err"; r.textContent = "a ≠ 0 bo'lgan a, b, c kiriting"; return; }
      var D = b * b - 4 * a * c, rows = [["D = b²−4ac", f(D)]];
      if (D > 0) rows.push(["x₁", f((-b - Math.sqrt(D)) / (2 * a))], ["x₂", f((-b + Math.sqrt(D)) / (2 * a))]);
      else if (D === 0) rows.push(["x", f(-b / (2 * a))]); else rows.push(["Haqiqiy ildiz yo'q", "D < 0"]);
      rows.push(["Uchi (x₀; y₀)", "(" + f(-b / (2 * a)) + "; " + f(c - b * b / (4 * a)) + ")"], ["x₁+x₂ = −b/a", f(-b / a)], ["x₁·x₂ = c/a", f(c / a)]); r.innerHTML = rowsHtml(rows);
    });
    $('[data-go="s"]', pane).addEventListener("click", function () {
      var v = ["a1", "b1", "c1", "a2", "b2", "c2"].map(function (k) { return num(pane, k); }), r = $("#lzc-r2"); r.className = "lzc-res";
      if (v.some(isNaN)) { r.className = "lzc-res err"; r.textContent = "Barcha koeffitsiyentlarni kiriting"; return; }
      var D = v[0] * v[4] - v[3] * v[1];
      if (D === 0) { r.textContent = (v[2] * v[4] - v[5] * v[1] === 0) ? "Cheksiz ko'p yechim" : "Yechim yo'q"; return; }
      r.innerHTML = rowsHtml([["x", f((v[2] * v[4] - v[5] * v[1]) / D)], ["y", f((v[0] * v[5] - v[3] * v[2]) / D)]]);
    });
  }

  function buildFormulaSolver(pane) {
    var list = C.FORMULAS[subject] || [];
    pane.innerHTML = '<div class="lzc-tool"><input type="search" class="lzc-in" id="lzs-search" placeholder="Formulani qidiring…"><select id="lzs-pick" class="lzc-sel" size="1">' +
      list.map(function (x, i) { return '<option value="' + i + '">' + esc(x[0]) + " — " + esc(x[1]) + "</option>"; }).join("") + '</select><div id="lzs-box"></div></div>';
    var pick = $("#lzs-pick", pane), box = $("#lzs-box", pane);
    function render() {
      var fm = list[parseInt(pick.value, 10)]; if (!fm) return;
      var vars = Object.keys(fm[2]), unk = vars[0];
      box.innerHTML = '<p class="lzc-eq">' + esc(fm[1]) + '</p><label class="lzc-f"><span>Topish kerak:</span><select id="lzs-unk" class="lzc-sel">' + vars.map(function (v) { return '<option value="' + v + '">' + esc(v) + " — " + esc(fm[2][v]) + "</option>"; }).join("") + "</select></label>" +
        vars.map(function (v) { return fieldHtml(v, esc(v) + " — " + esc(fm[2][v]), ""); }).join("") + '<button type="button" class="lz-primary" id="lzs-go">Hisoblash</button><div class="lzc-res" id="lzs-res"></div>';
      var unkSel = $("#lzs-unk", box);
      function sync() { $$("[data-f]", box).forEach(function (i) { var isU = i.dataset.f === unkSel.value; i.disabled = isU; i.parentNode.classList.toggle("dim", isU); if (isU) i.value = ""; }); }
      unkSel.addEventListener("change", sync); sync();
      $("#lzs-go", box).addEventListener("click", function () {
        var res = $("#lzs-res", box), known = {}, miss = [];
        vars.forEach(function (v) { if (v === unkSel.value) return; var x = num(box, v); if (isNaN(x)) miss.push(v); else known[v] = x; });
        res.className = "lzc-res";
        if (miss.length) { res.className = "lzc-res err"; res.textContent = "Kiriting: " + miss.join(", "); return; }
        try {
          var roots = C.solveFormula(fm[1], known, unkSel.value);
          if (!roots.length) { res.className = "lzc-res err"; res.textContent = "Yechim topilmadi (qiymatlarni tekshiring)"; return; }
          var pos = roots.filter(function (r) { return r >= 0; }); var show = pos.length ? pos : roots;
          res.innerHTML = rowsHtml(show.map(function (r) { return [unkSel.value, f(r)]; })) + '<button type="button" class="lzc-mini" id="lzs-use">Hisobga →</button>';
          $("#lzs-use", box).addEventListener("click", function () { switchTab("calc"); var i = $("#lzc-in"); i.value = C.plain(show[0]); runCalc(); });
        } catch (e) { res.className = "lzc-res err"; res.textContent = e.message; }
      });
    }
    pick.addEventListener("change", render);
    $("#lzs-search", pane).addEventListener("input", function () {
      var q = this.value.toLowerCase(), first = -1;
      $$("option", pick).forEach(function (o, i) { var show = !q || o.textContent.toLowerCase().indexOf(q) >= 0; o.hidden = !show; if (show && first < 0) first = i; });
      if (first >= 0) { pick.selectedIndex = first; render(); }
    });
    render();
  }

  var UNITS = {
    "Uzunlik": { m: 1, km: 1000, sm: 0.01, mm: 0.001, mkm: 1e-6, nm: 1e-9, mil: 1609.344 },
    "Massa": { kg: 1, g: 0.001, mg: 1e-6, t: 1000, "mkg": 1e-9 },
    "Vaqt": { s: 1, min: 60, soat: 3600, sutka: 86400, ms: 1e-3 },
    "Tezlik": { "m/s": 1, "km/soat": 1 / 3.6, "sm/s": 0.01 },
    "Bosim": { Pa: 1, kPa: 1000, MPa: 1e6, atm: 101325, "mm sim.ust": 133.322, bar: 1e5 },
    "Energiya": { J: 1, kJ: 1000, kal: 4.1868, kkal: 4186.8, eV: 1.602e-19, "kW·soat": 3.6e6 },
    "Quvvat": { W: 1, kW: 1000, MW: 1e6, "ot kuchi": 735.5 },
    "Hajm": { "m³": 1, "l": 1e-3, "ml": 1e-6, "sm³": 1e-6 },
    "Harorat": { "°C": "C", K: "K", "°F": "F" }
  };
  function buildUnits(pane) {
    pane.innerHTML = '<div class="lzc-tool"><label class="lzc-f"><span>Kattalik</span><select id="lzu-cat" class="lzc-sel">' + Object.keys(UNITS).map(function (k) { return "<option>" + k + "</option>"; }).join("") + "</select></label>" +
      '<div class="lzc-g3"><input type="text" id="lzu-v" class="lzc-in" value="1"><select id="lzu-a" class="lzc-sel"></select><select id="lzu-b" class="lzc-sel"></select></div><div class="lzc-res" id="lzu-r"></div></div>';
    var cat = $("#lzu-cat", pane), a = $("#lzu-a", pane), b = $("#lzu-b", pane), v = $("#lzu-v", pane), r = $("#lzu-r", pane);
    function fill() { var u = Object.keys(UNITS[cat.value]); a.innerHTML = u.map(function (x) { return "<option>" + x + "</option>"; }).join(""); b.innerHTML = a.innerHTML; b.selectedIndex = Math.min(1, u.length - 1); calcU(); }
    function calcU() {
      var x = C.run(v.value, { vars: {}, deg: true, ans: 0 }); if (x.kind !== "value") { r.textContent = ""; return; }
      var t = UNITS[cat.value], out;
      if (cat.value === "Harorat") { var k = a.value === "°C" ? x.value + 273.15 : a.value === "°F" ? (x.value - 32) * 5 / 9 + 273.15 : x.value; out = b.value === "°C" ? k - 273.15 : b.value === "°F" ? (k - 273.15) * 9 / 5 + 32 : k; }
      else out = x.value * t[a.value] / t[b.value];
      r.innerHTML = rowsHtml([[C.fmt(x.value) + " " + a.value + " =", f(out) + " " + b.value]]);
    }
    [cat].forEach(function (s) { s.addEventListener("change", fill); }); [a, b, v].forEach(function (s) { s.addEventListener("input", calcU); s.addEventListener("change", calcU); }); fill();
  }

  function buildMolar(pane) {
    pane.innerHTML = '<div class="lzc-tool"><input type="text" id="lzm-in" class="lzc-in" value="H2SO4" placeholder="Formula: Ca(OH)2, CuSO4·5H2O" autocomplete="off" spellcheck="false">' +
      '<label class="lzc-chk"><input type="checkbox" id="lzm-school" ' + (school ? "checked" : "") + '> Maktab massalari (Cl=35,5; Cu=64; yaxlitlangan)</label><div class="lzc-res" id="lzm-r"></div>' +
      '<hr><b>Modda miqdori hisobi</b><p class="lzc-help">M ni yuqoridan oling; massa, mol yoki hajm (n.sh.) dan birini kiriting.</p>' + fieldHtml2([["M", "M (g/mol)", ""], ["m", "m (g)", ""], ["n", "n (mol)", ""], ["V", "V (l, n.sh.)", ""], ["N", "N (zarracha)", ""]]) +
      '<button type="button" class="lz-primary" id="lzm-go">Hisoblash</button><div class="lzc-res" id="lzm-r2"></div></div>';
    var inp = $("#lzm-in", pane), r = $("#lzm-r", pane), chk = $("#lzm-school", pane);
    function calcM() {
      school = chk.checked;
      try {
        var m = C.molarMass(inp.value, school); r.className = "lzc-res";
        r.innerHTML = rowsHtml([["Mr / M", "<span class=\"lzc-big\">" + f(m.M) + "</span> g/mol"]].concat(m.rows.map(function (x) { return [x.sym + " × " + x.n + " (" + f(x.am) + ")", f(x.part) + " · " + f(Math.round(x.pct * 100) / 100) + " %"]; }))) + '<button type="button" class="lzc-mini" id="lzm-use">M ni qo\'yish</button>';
        $("#lzm-use", pane).addEventListener("click", function () { $('[data-f="M"]', pane).value = C.plain(m.M); });
      } catch (e) { r.className = "lzc-res err"; r.textContent = e.message; }
    }
    inp.addEventListener("input", calcM); chk.addEventListener("change", calcM); calcM();
    $("#lzm-go", pane).addEventListener("click", function () {
      var M = num(pane, "M"), m = num(pane, "m"), n = num(pane, "n"), V = num(pane, "V"), N = num(pane, "N"), r2 = $("#lzm-r2", pane);
      if (isNaN(n)) { if (!isNaN(m) && !isNaN(M)) n = m / M; else if (!isNaN(V)) n = V / 22.4; else if (!isNaN(N)) n = N / 6.02e23; }
      if (isNaN(n)) { r2.className = "lzc-res err"; r2.textContent = "m va M, yoki V, yoki N, yoki n ni kiriting"; return; }
      var rows = [["n", f(n) + " mol"], ["V (n.sh.)", f(n * 22.4) + " l"], ["N", f(n * 6.02e23)]]; if (!isNaN(M)) rows.push(["m", f(n * M) + " g"]); r2.className = "lzc-res"; r2.innerHTML = rowsHtml(rows);
    });
  }
  function buildBalance(pane) {
    pane.innerHTML = '<div class="lzc-tool"><p class="lzc-help">Reaksiyani koeffitsiyentsiz yozing (oksidlanish-qaytarilish ham, ionsiz).</p><input type="text" id="lzb-in" class="lzc-in" value="Fe + O2 -> Fe2O3" spellcheck="false" autocomplete="off"><button type="button" class="lz-primary" id="lzb-go">Tenglashtirish</button><div class="lzc-res" id="lzb-r"></div></div>';
    function go() { var r = $("#lzb-r", pane); try { r.className = "lzc-res"; r.innerHTML = '<div class="lzc-big">' + esc(C.balance($("#lzb-in", pane).value)) + "</div>"; } catch (e) { r.className = "lzc-res err"; r.textContent = e.message; } }
    $("#lzb-go", pane).addEventListener("click", go); $("#lzb-in", pane).addEventListener("keydown", function (e) { if (e.key === "Enter") go(); }); go();
  }
  function buildGen(pane) {
    pane.innerHTML = '<div class="lzc-tool"><p class="lzc-help">Matritsa (kodlovchi bo\'lmagan) DNK zanjirini kiriting (A, T, G, C).</p><input type="text" id="lzg-in" class="lzc-in" value="TACGGATTCACT" spellcheck="false" autocomplete="off"><div class="lzc-res" id="lzg-r"></div></div>';
    var i = $("#lzg-in", pane), r = $("#lzg-r", pane);
    function go() {
      var s = i.value.toUpperCase().replace(/[^ATGC]/g, ""); if (!s) { r.textContent = ""; return; }
      var m = C.transcribe(s), prot = C.translate(m);
      r.innerHTML = rowsHtml([["Komplementar DNK", esc(C.dnaComplement(s))], ["iRNK (transkripsiya)", esc(m)], ["Kodonlar", prot.map(function (x) { return x.codon; }).join(" ") || "—"], ["Aminokislotalar", prot.map(function (x) { return x.name; }).join(" – ") || "—"],
        ["Nukleotidlar soni", String(s.length)], ["DNK uzunligi (0,34 nm × n)", f(s.length * 0.34) + " nm"], ["Molekulyar massa (≈345 × n)", f(s.length * 345)]]);
    }
    i.addEventListener("input", go); go();
  }

  // =================================================================== 3) OCHIQ JAVOB UCHUN BELGILAR KLAVIATURASI
  var PADS = {
    math: [["x²", "²"], ["x³", "³"], ["xⁿ", "^"], ["√", "√("], ["∛", "∛("], ["π", "π"], ["a/b", "/"], ["±", "±"], ["×", "×"], ["÷", "÷"], ["·", "·"], ["(", "("], [")", ")"], ["≤", "≤"], ["≥", "≥"], ["≠", "≠"], ["∞", "∞"], ["°", "°"], ["%", "%"], ["−", "−"], ["{ }", "{}"], ["∪", "∪"], ["∩", "∩"], ["∈", "∈"], ["10ⁿ", "·10^"]],
    physics: [["10⁻", "·10⁻"], ["10ⁿ", "·10^"], ["⁻", "⁻"], ["²", "²"], ["³", "³"], ["⁴", "⁴"], ["⁵", "⁵"], ["⁶", "⁶"], ["⁹", "⁹"], ["×", "×"], ["÷", "÷"], ["√", "√("], ["π", "π"], ["°", "°"], ["Ω", "Ω"], ["μ", "μ"], ["λ", "λ"], ["ρ", "ρ"], ["Δ", "Δ"], ["α", "α"], ["β", "β"],
      ["m/s", " m/s"], ["m/s²", " m/s²"], ["N", " N"], ["J", " J"], ["W", " W"], ["Pa", " Pa"], ["Hz", " Hz"], ["V", " V"], ["A", " A"], ["C", " C"], ["K", " K"], ["kg", " kg"], ["m", " m"], ["s", " s"], ["Ω", " Ω"], ["F", " F"], ["T", " T"], ["Wb", " Wb"], ["eV", " eV"]],
    chemistry: [["₂", "₂"], ["₃", "₃"], ["₄", "₄"], ["₅", "₅"], ["₆", "₆"], ["₇", "₇"], ["₁₂", "₁₂"], ["⁺", "⁺"], ["⁻", "⁻"], ["²⁺", "²⁺"], ["³⁺", "³⁺"], ["²⁻", "²⁻"], ["→", " → "], ["⇌", " ⇌ "], ["↑", "↑"], ["↓", "↓"], ["Δ", "Δ"], ["°C", "°C"], ["·", "·"], ["(", "("], [")", ")"], ["+", " + "],
      ["H", "H"], ["C", "C"], ["N", "N"], ["O", "O"], ["Na", "Na"], ["Mg", "Mg"], ["Al", "Al"], ["S", "S"], ["Cl", "Cl"], ["K", "K"], ["Ca", "Ca"], ["Fe", "Fe"], ["Cu", "Cu"], ["Zn", "Zn"], ["mol", " mol"], ["g", " g"], ["l", " l"], ["%", "%"]],
    biology: [["×", " × "], ["→", " → "], ["♀", "♀"], ["♂", "♂"], ["A", "A"], ["a", "a"], ["B", "B"], ["b", "b"], ["D", "D"], ["d", "d"], ["AA", "AA"], ["Aa", "Aa"], ["aa", "aa"], [":", ":"], ["/", "/"], ["%", "%"], ["½", "½"], ["¼", "¼"], ["¾", "¾"], ["°C", "°C"], ["μm", " μm"], ["nm", " nm"], ["ATF", "ATF"], ["2n", "2n"], ["n", "n"]]
  };
  function decorateOpenInput(wrap, inp) {
    var pad = PADS[subject]; if (!pad) return;
    var bar = el("div", "lz-pad"), toggle = el("button", "lz-pad-toggle", "∑ Belgilar"); toggle.type = "button";
    var keys = el("div", "lz-pad-keys");
    pad.forEach(function (k) {
      var b = el("button", "", esc(k[0])); b.type = "button"; b.title = k[1].trim();
      b.addEventListener("mousedown", function (e) { e.preventDefault(); });
      b.addEventListener("click", function () { insertAt(inp, k[1]); inp.focus(); });
      keys.appendChild(b);
    });
    var open = false; try { open = localStorage.getItem("lz_pad_open") !== "0"; } catch (e) {}
    keys.hidden = !open; toggle.classList.toggle("on", open);
    toggle.addEventListener("click", function () { keys.hidden = !keys.hidden; toggle.classList.toggle("on", !keys.hidden); try { localStorage.setItem("lz_pad_open", keys.hidden ? "0" : "1"); } catch (e) {} });
    var bs = el("button", "lz-pad-bs", "⌫"); bs.type = "button"; bs.title = "O'chirish";
    bs.addEventListener("mousedown", function (e) { e.preventDefault(); });
    bs.addEventListener("click", function () { var s = inp.selectionStart; if (inp.selectionEnd !== s) { inp.setRangeText("", s, inp.selectionEnd, "end"); } else if (s > 0) { inp.setRangeText("", s - 1, s, "end"); } inp.dispatchEvent(new Event("input", { bubbles: true })); inp.focus(); });
    var head = el("div", "lz-pad-head"); head.append(toggle, bs); bar.append(head, keys); wrap.appendChild(bar);
  }
  window.LZTools = { decorateOpenInput: decorateOpenInput };

  // =================================================================== ISHGA TUSHIRISH
  function mount() {
    buildReport(); buildCalc();
    var timer = document.getElementById("quiz-timer");
    var host = timer && timer.parentNode;
    var anchor = document.getElementById("formula-sheet-toggle") || timer;
    [calcBtn, reportBtn].forEach(function (b) { if (!b) return; if (host && anchor && anchor.parentNode === host) host.insertBefore(b, anchor); else if (host) host.appendChild(b); else document.body.appendChild(b); });
    // test boshlanmaguncha (savollar yuklanmaguncha) tugmalar o'chiq
    reportBtn.disabled = true; reportBtn.title = "Savollar yuklangach ishlaydi";
    window.addEventListener("lz:ready", function () { reportBtn.disabled = false; reportBtn.title = "Shu savol bo'yicha shikoyat qilish"; });
    window.addEventListener("lz:finished", function () { [calcBtn, reportBtn].forEach(function (b) { if (b) b.hidden = true; }); if (calc) calc.hidden = true; if (reportDrawer) setDrawer(reportDrawer, false); });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount); else mount();
})();
