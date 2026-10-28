// LongoUZ admin — "Test qo'shish": bittalab, chizmali, JSON, fayl import.
(function () {
  "use strict";
  var P = JSON.parse(document.getElementById("add-data").textContent);
  var $ = function (id) { return document.getElementById(id); };
  var saved = 0;

  function api(path, body, isForm) {
    var opt = { method: "POST", credentials: "same-origin", headers: { "X-Requested-With": "fetch" } };
    if (isForm) opt.body = body; else { opt.headers["Content-Type"] = "application/json"; opt.body = JSON.stringify(body); }
    return fetch(P.prefix + path, opt).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (d) { if (!r.ok) throw new Error(d.detail || "Xatolik (" + r.status + ")"); return d; });
    });
  }
  function bump(n) { saved += n; $("cnt").textContent = saved; }

  // ---------- Tablar ----------
  var tab = P.tab || "manual";
  function setTab(t) {
    tab = t;
    document.querySelectorAll("#mtabs button").forEach(function (b) { b.classList.toggle("active", b.dataset.tab === t); });
    document.querySelectorAll(".mpane").forEach(function (p) { p.hidden = p.dataset.pane.split(" ").indexOf(t) === -1; });
    document.querySelectorAll(".figsec, .afig").forEach(function (e) { e.hidden = t !== "figure"; });
  }
  document.querySelectorAll("#mtabs button").forEach(function (b) { b.addEventListener("click", function () { setTab(b.dataset.tab); }); });

  // ---------- Savol formasi ----------
  var form = $("qform"), optsBox = $("opts"), optBuilders = [];
  for (var i = 0; i < 4; i++) {
    (function (i) {
      var wrap = document.createElement("div"); wrap.className = "optwrap";
      wrap.innerHTML = '<div class="aopt"><input type="radio" name="correct" value="' + i + '"' + (i === 0 ? " checked" : "") + ' aria-label="To\'g\'ri javob ' + "ABCD"[i] + '"><span class="key">' + "ABCD"[i] + '</span><input type="text" class="o-txt" maxlength="700" placeholder="' + "ABCD"[i] + ' variant"></div><div class="afig" hidden></div>';
      optsBox.appendChild(wrap);
      optBuilders.push(LZFigBuilder.mount(wrap.querySelector(".afig"), { uploadUrl: P.prefix + "/api/figure/upload" }));
    })(i);
  }
  var qFig = LZFigBuilder.mount($("fb-q"), { uploadUrl: P.prefix + "/api/figure/upload" });

  function collect() {
    var fig = null;
    if (tab === "figure") {
      var q = qFig.get(), o = optBuilders.map(function (b) { return b.get(); });
      if (q || o.some(Boolean)) fig = { q: q, o: o, w: parseInt($("fig-w").value, 10) || 100 };
    }
    return {
      subject: P.subject, mode: P.mode, topic: P.topic,
      question: form.question.value.trim(),
      options: Array.prototype.map.call(optsBox.querySelectorAll(".o-txt"), function (t) { return t.value.trim(); }),
      correct_index: parseInt(form.correct.value, 10),
      explanation: form.explanation.value.trim(), is_active: $("publish").checked, figure: fig,
    };
  }
  function resetForm() {
    form.question.value = ""; form.explanation.value = "";
    optsBox.querySelectorAll(".o-txt").forEach(function (t) { t.value = ""; });
    form.correct.value = "0"; form.querySelector("input[name=correct]").checked = true;
    qFig.set(null); optBuilders.forEach(function (b) { b.set(null); }); $("fig-w").value = 100;
    form.question.focus();
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var data = collect(), btn = $("save-q");
    btn.disabled = true;
    api("/api/question/create", data).then(function () {
      bump(1); LZToast.ok("Saqlandi ✓ — savol qo'shildi"); resetForm();
    }).catch(function (err) { LZToast.err(err.message); }).finally(function () { btn.disabled = false; });
  });

  // ---------- JSON ----------
  var EXAMPLE = [
    { question: "2 + 2 nechiga teng?", options: ["3", "4", "5", "6"], correct_index: 1, explanation: "Oddiy qo'shish." },
    {
      question: "Rasmdagi A nuqtaning koordinatalari qanday?", options: ["(2; 3)", "(3; 2)", "(−2; 3)", "(3; −2)"], answer: "A",
      figure: { q: { type: "plane", xmin: -5, xmax: 5, ymin: -5, ymax: 5, axes: true, grid: true, items: [{ k: "pt", x: 2, y: 3, l: "A" }] }, o: [null, null, null, null] },
    },
    {
      question: "ABC uchburchakning yuzini toping.", options: ["6", "12", "10", "8"], correct_index: 0,
      figure: { q: { type: "plane", xmin: -1, xmax: 9, ymin: -1, ymax: 6, axes: false, grid: false, items: [{ k: "poly", pts: [[0, 0], [4, 0], [0, 3]], names: ["A", "B", "C"], fill: true }] } },
    },
  ];
  $("json-ex").textContent = JSON.stringify(EXAMPLE, null, 2);
  $("json-fill").addEventListener("click", function () { $("json-text").value = JSON.stringify(EXAMPLE, null, 2); });
  $("json-file").addEventListener("change", function () {
    var f = this.files[0]; if (!f) return;
    var r = new FileReader(); r.onload = function () { $("json-text").value = String(r.result); }; r.readAsText(f);
  });
  $("json-save").addEventListener("click", function () {
    var text = $("json-text").value.trim(), res = $("json-res"), btn = this;
    if (!text) { LZToast.err("JSON matnini kiriting."); return; }
    btn.disabled = true; res.textContent = "Tekshirilmoqda…";
    api("/api/topic/import-json", { subject: P.subject, mode: P.mode, topic: P.topic, text: text, publish: $("json-pub").checked })
      .then(function (d) {
        bump(d.added);
        res.textContent = "Saqlandi: " + d.added + " ta. Takror: " + d.skipped + ". Xato: " + d.failed + (d.errors.length ? " — " + d.errors.slice(0, 6).join("; ") : "");
        if (d.added) LZToast.ok("Saqlandi ✓ — " + d.added + " ta savol"); else LZToast.err("Hech narsa saqlanmadi.");
      }).catch(function (e) { res.textContent = e.message; LZToast.err(e.message); }).finally(function () { btn.disabled = false; });
  });

  // ---------- Fayl ----------
  var items = [], dz = $("dz"), inp = $("imp-files");
  function upload(files) {
    if (!files.length) return;
    var fd = new FormData(); Array.prototype.forEach.call(files, function (f) { fd.append("file", f); });
    $("imp-status").textContent = "Fayl o'qilmoqda, chizmalar ajratilmoqda…"; $("imp-wrap").hidden = true;
    api("/api/topic/import-file", fd, true).then(function (d) {
      items = d.items.map(function (x) { x.on = true; return x; });
      $("imp-status").textContent = d.items.length + " ta savol topildi" + (d.with_figures ? ", " + d.with_figures + " tasida chizma bor" : "") +
        (d.no_answer ? ". " + d.no_answer + " tasida to'g'ri javob yo'q — belgilang" : "") + (d.warnings.length ? ". " + d.warnings.join(" · ") : "");
      drawList(); $("imp-wrap").hidden = !items.length;
    }).catch(function (e) { $("imp-status").textContent = e.message; LZToast.err(e.message); });
  }
  inp.addEventListener("change", function () { upload(inp.files); });
  ["dragenter", "dragover"].forEach(function (ev) { dz.addEventListener(ev, function (e) { e.preventDefault(); dz.classList.add("over"); }); });
  ["dragleave", "drop"].forEach(function (ev) { dz.addEventListener(ev, function (e) { e.preventDefault(); dz.classList.remove("over"); }); });
  dz.addEventListener("drop", function (e) { upload(e.dataTransfer.files); });
  function drawList() {
    var box = $("imp-list"); box.innerHTML = "";
    items.forEach(function (it, idx) {
      var row = document.createElement("div"); row.className = "pvitem" + (it.on ? "" : " off") + (it.correct_index == null ? " noans" : "");
      var head = document.createElement("label"); head.className = "pvq";
      var c = document.createElement("input"); c.type = "checkbox"; c.checked = it.on;
      c.addEventListener("change", function () { it.on = c.checked; row.classList.toggle("off", !it.on); });
      head.append(c, document.createTextNode(" " + (idx + 1) + ". " + it.question)); row.appendChild(head);
      if (it.figure && it.figure.q) { var f = LZFigure.render(it.figure.q); f.classList.add("pvfig"); row.appendChild(f); }
      var o = document.createElement("div"); o.className = "pvo";
      it.options.forEach(function (t, k) {
        var l = document.createElement("label"); var r = document.createElement("input"); r.type = "radio"; r.name = "pv" + idx; r.checked = it.correct_index === k;
        r.addEventListener("change", function () { it.correct_index = k; row.classList.remove("noans"); });
        var s = document.createElement("span"); s.textContent = "ABCD"[k] + ") " + t;
        l.append(r, s); o.appendChild(l);
      });
      row.appendChild(o); box.appendChild(row);
    });
  }
  $("imp-all").addEventListener("change", function () { var v = this.checked; items.forEach(function (i) { i.on = v; }); drawList(); });
  $("imp-save").addEventListener("click", function () {
    var chosen = items.filter(function (i) { return i.on; });
    var missing = chosen.filter(function (i) { return i.correct_index == null; }).length;
    if (!chosen.length) { LZToast.err("Savol tanlanmagan."); return; }
    if (missing) { LZToast.err(missing + " ta savolda to'g'ri javob belgilanmagan."); return; }
    var btn = this; btn.disabled = true;
    api("/api/topic/import-json", { subject: P.subject, mode: P.mode, topic: P.topic, items: chosen, publish: $("imp-pub").checked })
      .then(function (d) {
        bump(d.added); LZToast.ok("Saqlandi ✓ — " + d.added + " ta savol" + (d.skipped ? " (" + d.skipped + " takror)" : ""));
        $("imp-status").textContent = "Saqlandi: " + d.added + ". Takror: " + d.skipped + ". Xato: " + d.failed + (d.errors.length ? " — " + d.errors.slice(0, 5).join("; ") : "");
        items = []; drawList(); $("imp-wrap").hidden = true; inp.value = "";
      }).catch(function (e) { LZToast.err(e.message); }).finally(function () { btn.disabled = false; });
  });

  setTab(tab);
})();
