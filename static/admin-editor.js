// LongoUZ admin — mavzu tahrirlagichi: savol matni, ko'rinishi, test oynasi, saqlash hisoblagichi.
(function () {
  "use strict";
  var P = JSON.parse(document.getElementById("editor-data").textContent);
  var $ = function (id) { return document.getElementById(id); };
  var STYLE_DEFAULTS = { fs: 1.25, fw: 600, lh: 1.4, mt: 0, mb: 20, pd: 30, og: 10, ox: 0, oy: 0, al: "left", col: "" };
  var STYLE_FIELDS = [
    ["fs", "Matn o'lchami", 0.9, 2.6, 0.05, "rem"], ["fw", "Qalinligi", 400, 800, 100, ""], ["lh", "Qator balandligi", 1.1, 2.2, 0.05, ""],
    ["mt", "Tepadan masofa", 0, 80, 2, "px"], ["mb", "Pastdan masofa (variantlargacha)", 0, 80, 2, "px"],
    ["pd", "Karta ichki masofasi", 8, 56, 2, "px"], ["og", "Variantlar orasidagi masofa", 4, 32, 1, "px"],
    ["ox", "Chapga / o'ngga surish", -120, 120, 2, "px"], ["oy", "Tepaga / pastga surish", -60, 120, 2, "px"],
  ];
  var LAYOUT_DEFAULTS = { timer: "show", timerPos: "right", timerSize: 1.1, header: "show", progress: "show", cardW: 720, nav: "between" };

  var counter = 0;
  function snap(it) {
    var st = {}; Object.keys(it.style || {}).sort().forEach(function (k) { st[k] = it.style[k]; });
    return JSON.stringify([it.question, it.options, it.correct_index, it.explanation, it.is_active, st, it.figure || {}]);
  }
  var items = P.questions.map(function (q) {
    var it = { key: "q" + q.id, id: q.id, question: q.question, options: q.options.slice(0, 4), correct_index: q.correct_index,
      explanation: q.explanation || "", is_active: q.is_active, style: Object.assign({}, q.style || {}), figure: q.figure && (q.figure.q || (q.figure.o || []).some(Boolean)) ? JSON.parse(JSON.stringify(q.figure)) : null, deleted: false };
    while (it.options.length < 4) it.options.push("");
    it.orig = snap(it); return it;
  });
  var layout = Object.assign({}, P.layout || {});
  var origLayout = JSON.stringify(sortObj(layout));
  function sortObj(o) { var r = {}; Object.keys(o).sort().forEach(function (k) { r[k] = o[k]; }); return r; }

  var cur = Math.min(Math.max((P.start || 1) - 1, 0), Math.max(items.length - 1, 0));
  var editing = false, activeTab = "text";

  function isDirty(it) { return it.deleted ? it.id != null : (it.id == null || snap(it) !== it.orig); }
  function dirtyCount() { return items.filter(isDirty).length; }
  function layoutDirty() { return JSON.stringify(sortObj(layout)) !== origLayout; }
  function visible() { return items.filter(function (i) { return !i.deleted; }); }

  // ---------- Namuna (preview) ----------
  function renderPreview() {
    var it = items[cur], pv = $("epreview");
    $("pv-mode").textContent = P.mode_name; $("pv-subject").textContent = P.subject_name;
    $("pv-timer").textContent = String(P.time_limit_minutes).padStart(2, "0") + ":00";
    $("ebar-sub").textContent = P.subject_name + " · " + P.mode_name;
    var box = $("pv-options"); box.innerHTML = ""; window.LZFigure.fillQuestion($("pv-qfig"), null);
    if (!it) { $("pv-question").textContent = "Bu mavzuda savol yo'q. «Tahrirlash» → «+ Yangi savol qo'shish»."; $("pv-label").textContent = ""; $("pv-fill").style.width = "0"; window.LZQuizStyle.applyLayout(pv, layout); return; }
    var qEl = $("pv-question");
    if (document.activeElement !== qEl) qEl.textContent = it.question || (editing ? "" : "(savol matni bo'sh)");
    qEl.contentEditable = editing ? "plaintext-only" : "false";
    qEl.classList.toggle("inline-edit", editing);
    window.LZFigure.fillQuestion($("pv-qfig"), it.figure);
    it.options.forEach(function (o, i) {
      var b = document.createElement("div"); b.setAttribute("role", "button"); b.tabIndex = 0;
      b.className = "quiz-option" + (i === it.correct_index && editing ? " is-correct-mark" : "");
      var key = document.createElement("span"); key.className = "quiz-option-key"; key.textContent = "ABCD"[i];
      var lab = document.createElement("span"); lab.className = "quiz-option-text"; lab.textContent = o || (editing ? "" : "(bo'sh variant)");
      var fg = window.LZFigure.optionFigure(it.figure, i);
      if (editing) {
        lab.contentEditable = "plaintext-only"; lab.classList.add("inline-edit"); lab.dataset.ph = "variant";
        lab.addEventListener("input", function () { items[cur].options[i] = lab.textContent; touch(true, true); });
        lab.addEventListener("keydown", function (e) { if (e.key === "Enter") e.preventDefault(); });
      }
      if (fg) { var bx = document.createElement("span"); bx.className = "quiz-option-body"; bx.append(lab, fg); b.append(key, bx); } else b.append(key, lab);
      b.addEventListener("click", function (e) {
        if (editing && e.target === lab) return;
        Array.prototype.forEach.call(box.children, function (c) { c.classList.remove("selected"); }); b.classList.add("selected");
        if (editing) { items[cur].correct_index = i; touch(); }
      });
      box.appendChild(b);
    });
    $("pv-label").textContent = (cur + 1) + " / " + items.length + " savol";
    $("pv-fill").style.width = ((cur + 1) / items.length * 100) + "%";
    pv.classList.toggle("is-deleted", it.deleted);
    window.LZQuizStyle.applyLayout(pv, layout);
    window.LZQuizStyle.applyQuestion(pv, it.style);
  }

  // ---------- Navigator ----------
  function renderNav() {
    $("nav-cur").textContent = items.length ? cur + 1 : 0; $("nav-total").textContent = items.length;
    $("nav-prev").disabled = cur <= 0; $("nav-next").disabled = cur >= items.length - 1;
    var wrap = $("nav-chips"); wrap.innerHTML = "";
    items.forEach(function (it, i) {
      var b = document.createElement("button"); b.type = "button"; b.textContent = i + 1;
      b.className = "echip" + (i === cur ? " current" : "") + (it.deleted ? " deleted" : isDirty(it) ? (it.id == null ? " fresh" : " changed") : "") + (!it.is_active && !it.deleted ? " off" : "");
      b.title = it.deleted ? "O'chiriladi" : it.id == null ? "Yangi savol" : isDirty(it) ? "O'zgartirilgan" : it.is_active ? "O'zgarmagan" : "Yashirin";
      b.addEventListener("click", function () { go(i); });
      wrap.appendChild(b);
    });
    var c = wrap.querySelector(".current"); if (c && c.scrollIntoView) c.scrollIntoView({ block: "nearest", inline: "center" });
  }
  function go(i) { if (i < 0 || i >= items.length) return; cur = i; renderAll(); }

  // ---------- Matn paneli ----------
  function renderTextPane() {
    var it = items[cur], box = $("f-options");
    var has = !!it;
    $("f-question").disabled = !has; $("f-expl").disabled = !has; $("f-active").disabled = !has; $("btn-del").disabled = !has;
    if (!has) { $("f-question").value = ""; $("f-expl").value = ""; box.innerHTML = ""; return; }
    if (document.activeElement !== $("f-question")) $("f-question").value = it.question;
    if (document.activeElement !== $("f-expl")) $("f-expl").value = it.explanation;
    $("f-active").checked = it.is_active;
    $("btn-del").textContent = it.deleted ? "O'chirishni bekor qilish" : "O'chirish";
    if (box.children.length !== 4 || box.dataset.key !== it.key) {
      box.dataset.key = it.key; box.innerHTML = "";
      for (var i = 0; i < 4; i++) {
        (function (i) {
          var row = document.createElement("div"); row.className = "eopt";
          var r = document.createElement("input"); r.type = "radio"; r.name = "f-correct"; r.value = i; r.setAttribute("aria-label", "To'g'ri javob: " + "ABCD"[i]);
          var t = document.createElement("input"); t.type = "text"; t.placeholder = "ABCD"[i] + " variant"; t.maxLength = 700;
          r.addEventListener("change", function () { items[cur].correct_index = i; touch(); });
          t.addEventListener("input", function () { items[cur].options[i] = t.value; touch(); });
          row.appendChild(r); row.appendChild(t); box.appendChild(row);
        })(i);
      }
    }
    Array.prototype.forEach.call(box.children, function (row, i) {
      row.children[0].checked = it.correct_index === i;
      if (document.activeElement !== row.children[1]) row.children[1].value = it.options[i];
    });
  }

  // ---------- Ko'rinish va oyna boshqaruvlari ----------
  function mkRange(host, f, getVal, setVal) {
    var wrap = document.createElement("label"); wrap.className = "erange";
    var head = document.createElement("span"); head.innerHTML = "<b>" + f[1] + "</b><output></output>";
    var inp = document.createElement("input"); inp.type = "range"; inp.min = f[2]; inp.max = f[3]; inp.step = f[4];
    var out = head.querySelector("output");
    function sync() { var v = getVal(); inp.value = v; out.textContent = v + f[5]; }
    inp.addEventListener("input", function () { setVal(parseFloat(inp.value)); out.textContent = inp.value + f[5]; });
    wrap.appendChild(head); wrap.appendChild(inp); host.appendChild(wrap); wrap._sync = sync; return wrap;
  }
  function mkSeg(host, label, options, getVal, setVal) {
    var wrap = document.createElement("div"); wrap.className = "eseg-row";
    wrap.innerHTML = "<b>" + label + "</b>";
    var seg = document.createElement("div"); seg.className = "ebar-seg";
    options.forEach(function (o) {
      var b = document.createElement("button"); b.type = "button"; b.textContent = o[1]; b.dataset.v = o[0];
      b.addEventListener("click", function () { setVal(o[0]); sync(); }); seg.appendChild(b);
    });
    function sync() { Array.prototype.forEach.call(seg.children, function (b) { b.classList.toggle("active", b.dataset.v === String(getVal())); }); }
    wrap.appendChild(seg); host.appendChild(wrap); wrap._sync = sync; return wrap;
  }
  var lookCtl = [], winCtl = [];
  function buildLook() {
    var host = $("look-controls"); host.innerHTML = "";
    STYLE_FIELDS.forEach(function (f) {
      lookCtl.push(mkRange(host, f,
        function () { var v = items[cur] && items[cur].style[f[0]]; return v != null ? v : STYLE_DEFAULTS[f[0]]; },
        function (v) { if (!items[cur]) return; items[cur].style[f[0]] = v; touch(true); }));
    });
    lookCtl.push(mkSeg(host, "Matn joylashuvi", [["left", "Chap"], ["center", "Markaz"], ["right", "O'ng"]],
      function () { return (items[cur] && items[cur].style.al) || "left"; },
      function (v) { if (items[cur]) { items[cur].style.al = v; touch(true); } }));
    var cw = document.createElement("label"); cw.className = "erange"; cw.innerHTML = "<span><b>Matn rangi</b></span>";
    var ci = document.createElement("input"); ci.type = "color"; ci.value = "#e6edf3";
    ci.addEventListener("input", function () { if (items[cur]) { items[cur].style.col = ci.value; touch(true); } });
    cw.appendChild(ci); host.appendChild(cw); cw._sync = function () { ci.value = (items[cur] && items[cur].style.col) || "#e6edf3"; }; lookCtl.push(cw);
  }
  function buildWin() {
    var host = $("win-controls"); host.innerHTML = "";
    var L = function (k) { return layout[k] != null ? layout[k] : LAYOUT_DEFAULTS[k]; };
    var S = function (k) { return function (v) { layout[k] = v; touch(true); }; };
    winCtl.push(mkSeg(host, "Soat (taymer)", [["show", "Ko'rinsin"], ["hide", "Yashirilsin"]], function () { return L("timer"); }, S("timer")));
    winCtl.push(mkSeg(host, "Soat joylashuvi", [["left", "Chap"], ["center", "Markaz"], ["right", "O'ng"]], function () { return L("timerPos"); }, S("timerPos")));
    winCtl.push(mkRange(host, ["timerSize", "Soat o'lchami", 0.8, 2.4, 0.1, "rem"], function () { return L("timerSize"); }, S("timerSize")));
    winCtl.push(mkSeg(host, "Sarlavha (rejim / fan nomi)", [["show", "Ko'rinsin"], ["hide", "Yashirilsin"]], function () { return L("header"); }, S("header")));
    winCtl.push(mkSeg(host, "Progress chizig'i", [["show", "Ko'rinsin"], ["hide", "Yashirilsin"]], function () { return L("progress"); }, S("progress")));
    winCtl.push(mkRange(host, ["cardW", "Savol oynasi kengligi", 480, 960, 10, "px"], function () { return L("cardW"); }, S("cardW")));
    winCtl.push(mkSeg(host, "«Oldingi / Keyingi» tugmalari", [["between", "Chetlarda"], ["center", "Markazda"], ["right", "O'ngda"]], function () { return L("nav"); }, S("nav")));
  }
  function syncControls() { lookCtl.concat(winCtl).forEach(function (c) { c._sync(); }); }

  // ---------- Chizma paneli ----------
  var figQ = null, figO = [], figLoading = false, figKey = null;
  function figDoc() {
    var o = figO.map(function (b) { return b.get(); }), q = figQ.get();
    return q || o.some(Boolean) ? { q: q, o: o, w: parseInt($("fe-w").value, 10) || 100 } : null;
  }
  function onFig() {
    if (figLoading || !items[cur]) return;
    items[cur].figure = figDoc(); touch();
  }
  function buildFigPane() {
    var up = P.prefix + "/api/figure/upload";
    figQ = LZFigBuilder.mount($("fe-q"), { uploadUrl: up, onChange: onFig });
    var host = $("fe-o");
    for (var i = 0; i < 4; i++) {
      var d = document.createElement("details"); d.className = "fe-opt"; var sm = document.createElement("summary"); sm.textContent = "ABCD"[i] + " variant chizmasi";
      var inner = document.createElement("div"); d.append(sm, inner); host.appendChild(d);
      figO.push(LZFigBuilder.mount(inner, { uploadUrl: up, onChange: onFig }));
    }
    $("fe-w").addEventListener("input", function () { $("fe-wv").textContent = this.value; onFig(); });
  }
  function syncFigPane() {
    var it = items[cur]; if (!it || figKey === it.key) return;
    figKey = it.key; figLoading = true;
    var f = it.figure || {};
    figQ.set(f.q || null); figO.forEach(function (b, i) { b.set((f.o || [])[i] || null); });
    $("fe-w").value = f.w || 100; $("fe-wv").textContent = f.w || 100;
    figLoading = false;
  }

  // ---------- Umumiy ----------
  function touch(noText, keepPreview) {
    if (!keepPreview) renderPreview();
    renderNav(); renderCounter();
    if (keepPreview && document.activeElement && document.activeElement.classList.contains("inline-edit")) renderTextPane();
  }
  function renderCounter() {
    var n = dirtyCount(), ld = layoutDirty();
    $("ecount").textContent = n; $("ecount").classList.toggle("on", n > 0);
    $("btn-save").disabled = !(n > 0 || ld);
    $("btn-save").title = ld && n === 0 ? "Test oynasi sozlamalari o'zgargan" : n + " ta savol o'zgartirilgan" + (ld ? " + oyna sozlamalari" : "");
    $("btn-revert").hidden = !(n > 0 || ld);
    var nums = []; items.forEach(function (it, i) { if (isDirty(it)) nums.push("№" + (i + 1) + (it.deleted ? " (o'chiriladi)" : it.id == null ? " (yangi)" : "")); });
    var ch = $("echanged"); ch.hidden = !nums.length && !ld;
    ch.innerHTML = ""; var b = document.createElement("b"); b.textContent = nums.length + " ta savol o'zgartirilgan"; ch.appendChild(b);
    if (nums.length) ch.appendChild(document.createTextNode(": " + nums.join(", ")));
    if (ld) ch.appendChild(document.createTextNode(nums.length ? " · test oynasi sozlamalari ham" : " test oynasi sozlamalari o'zgargan"));
  }
  function renderAll() { renderPreview(); renderNav(); renderTextPane(); syncFigPane(); syncControls(); renderCounter(); }

  function setEditing(on) {
    editing = on;
    $("mode-edit").classList.toggle("active", on); $("mode-view").classList.toggle("active", !on);
    $("epanel").hidden = !on;
    document.querySelector(".egrid").classList.toggle("is-editing", on);
    $("pv-hint").textContent = on ? "Namuna o'zgarishlaringizni darhol ko'rsatadi. To'g'ri javob yashil belgi bilan ko'rsatiladi." : "Ko'rish rejimi: savol o'quvchiga qanday ko'rinishini tekshiring. O'zgartirish uchun yuqoridagi «Tahrirlash»ni bosing.";
    renderPreview();
  }

  var toastTimer;
  function toast(msg, kind) {
    var t = $("etoast"); t.hidden = false; t.className = "etoast " + (kind || ""); t.textContent = msg;
    clearTimeout(toastTimer); if (kind !== "err") toastTimer = setTimeout(function () { t.hidden = true; }, 4000);
  }

  // ---------- Hodisalar ----------
  $("mode-view").addEventListener("click", function () { setEditing(false); });
  $("mode-edit").addEventListener("click", function () { setEditing(true); });
  $("nav-prev").addEventListener("click", function () { go(cur - 1); });
  $("nav-next").addEventListener("click", function () { go(cur + 1); });
  $("nav-jump").addEventListener("change", function () { var n = parseInt(this.value, 10); if (n >= 1 && n <= items.length) go(n - 1); this.value = ""; });
  document.querySelectorAll(".etabs button").forEach(function (b) {
    b.addEventListener("click", function () {
      activeTab = b.dataset.tab;
      document.querySelectorAll(".etabs button").forEach(function (x) { x.classList.toggle("active", x === b); });
      document.querySelectorAll(".epane").forEach(function (p) { p.hidden = p.dataset.pane !== activeTab; });
    });
  });
  $("pv-question").addEventListener("input", function () { if (items[cur] && editing) { items[cur].question = this.textContent; touch(true, true); } });
  $("pv-question").addEventListener("keydown", function (e) { if (e.key === "Enter" && !e.shiftKey) e.preventDefault(); });
  $("f-question").addEventListener("input", function () { if (items[cur]) { items[cur].question = this.value; touch(); } });
  $("f-expl").addEventListener("input", function () { if (items[cur]) { items[cur].explanation = this.value; touch(); } });
  $("f-active").addEventListener("change", function () { if (items[cur]) { items[cur].is_active = this.checked; touch(); } });
  $("btn-add").addEventListener("click", function () {
    items.push({ key: "n" + (++counter), id: null, question: "", options: ["", "", "", ""], correct_index: 0, explanation: "", is_active: true, style: {}, figure: null, deleted: false, orig: null });
    cur = items.length - 1; renderAll(); $("f-question").focus();
  });
  $("btn-del").addEventListener("click", function () {
    var it = items[cur]; if (!it) return;
    if (it.id == null) { items.splice(cur, 1); cur = Math.max(0, Math.min(cur, items.length - 1)); renderAll(); return; }
    it.deleted = !it.deleted; renderAll();
    if (it.deleted) toast("Savol «Saqlash» bosilganda bazadan butunlay o'chiriladi.", "warn");
  });
  $("look-reset").addEventListener("click", function () { if (items[cur]) { items[cur].style = {}; renderAll(); } });
  $("look-all").addEventListener("click", function () {
    var src = items[cur]; if (!src) return;
    if (!confirm("Shu savolning ko'rinishi mavzudagi barcha savolga qo'llansinmi?")) return;
    items.forEach(function (i) { if (!i.deleted) i.style = Object.assign({}, src.style); }); renderAll();
  });
  $("win-reset").addEventListener("click", function () { layout = {}; renderAll(); });
  $("btn-revert").addEventListener("click", function () {
    if (!confirm("Barcha saqlanmagan o'zgarishlar bekor qilinsinmi?")) return;
    location.href = location.pathname + location.search.replace(/&start=\d+/, "") + "&start=" + (cur + 1);
  });

  $("btn-save").addEventListener("click", save);
  function save() {
    if ($("btn-save").disabled) return;
    var changes = [], deletes = [];
    items.forEach(function (it, i) {
      if (it.deleted) { if (it.id != null) deletes.push(it.id); return; }
      if (!isDirty(it)) return;
      changes.push({ key: it.key, id: it.id, label: "№" + (i + 1), question: it.question, options: it.options, correct_index: it.correct_index,
        explanation: it.explanation, is_active: it.is_active, style: it.style, figure: it.figure });
    });
    var btn = $("btn-save"); btn.disabled = true; btn.firstChild.textContent = "Saqlanmoqda… ";
    fetch(P.prefix + "/api/topic/save", {
      method: "POST", credentials: "same-origin",
      headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
      body: JSON.stringify({ subject: P.subject, mode: P.mode, topic: P.topic, changes: changes, deletes: deletes, layout: layout }),
    }).then(function (r) { return r.json().then(function (d) { if (!r.ok) throw new Error(d.detail || "Xatolik"); return d; }); })
      .then(function (d) {
        var failed = {}; (d.failed_keys || []).forEach(function (k) { failed[k] = 1; });
        items = items.filter(function (it) { return !(it.deleted && it.id != null); });
        items.forEach(function (it) {
          if (it.key in failed) return;
          if (d.id_map && d.id_map[it.key]) { it.id = d.id_map[it.key]; }
          if (it.id != null) it.orig = snap(it);
        });
        origLayout = JSON.stringify(sortObj(layout));
        cur = Math.min(cur, Math.max(items.length - 1, 0));
        btn.firstChild.textContent = "Saqlash ";
        renderAll();
        if (d.errors && d.errors.length) toast("Qisman saqlandi. Xatolar: " + d.errors.join("; "), "err");
        else { toast("Saqlandi: " + d.saved + " tahrir, " + d.created + " yangi, " + d.deleted + " o'chirildi. Sayt yangilandi.", "ok"); }
        if (!(d.errors && d.errors.length)) window.LZToast.ok("Saved ✓ — o'zgarishlar saytga qo'llandi");
      })
      .catch(function (e) { btn.firstChild.textContent = "Saqlash "; renderCounter(); toast("Saqlab bo'lmadi: " + e.message, "err"); window.LZToast.err("Saqlab bo'lmadi: " + e.message); });
  }

  document.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "s") { e.preventDefault(); save(); return; }
    var tag = (e.target.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea" || tag === "select") return;
    if (e.key === "ArrowLeft") go(cur - 1); else if (e.key === "ArrowRight") go(cur + 1);
  });
  window.addEventListener("beforeunload", function (e) { if (dirtyCount() > 0 || layoutDirty()) { e.preventDefault(); e.returnValue = ""; } });

  buildFigPane(); buildLook(); buildWin(); renderAll(); setEditing(false);
})();
