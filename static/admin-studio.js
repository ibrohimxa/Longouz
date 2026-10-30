(function () {
  "use strict";
  var P = window.STUDIO.prefix;
  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]; }); }
  function api(path, body, isForm) {
    var o = {method: body ? "POST" : "GET", credentials: "same-origin", headers: {"X-Requested-With": "fetch"}};
    if (body) { if (isForm) o.body = body; else { o.headers["Content-Type"] = "application/json"; o.body = JSON.stringify(body); } }
    return fetch(P + path, o).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok) throw new Error(j.detail || ("Xato " + r.status)); return j; });
    });
  }
  // tablar
  var tabs = document.querySelectorAll("#st-tabs button");
  tabs.forEach(function (b) { b.onclick = function () {
    tabs.forEach(function (x) { x.classList.toggle("on", x === b); });
    document.querySelectorAll(".st-pane").forEach(function (p) { p.hidden = p.id !== "p-" + b.dataset.t; });
    if (b.dataset.t === "bank") loadBank(); if (b.dataset.t === "mock") loadMocks();
  }; });

  // ---------- HUJJAT ----------
  var docs = [], items = [], files = [];
  var drop = $("d-drop"), fin = $("d-file");
  drop.ondragover = function (e) { e.preventDefault(); }; drop.ondrop = function (e) { e.preventDefault(); fin.files = e.dataTransfer.files; };
  function status(t) { $("d-status").textContent = t || ""; }
  $("d-go").onclick = function () {
    if (!fin.files.length) { status("Fayl tanlang"); return; }
    var fd = new FormData(), tot = 0; for (var i = 0; i < fin.files.length; i++) { fd.append("file", fin.files[i]); tot += fin.files[i].size; }
    if (tot > 4.3 * 1024 * 1024 && /vercel\.app$/.test(location.hostname)) { status("Vercel 4.5 MB dan katta so'rovni qabul qilmaydi — faylni bo'lib (kichikroq PDF) yuklang yoki lokal ishga tushirib import qiling."); return; }
    files = Array.prototype.slice.call(fin.files);
    status("O'qilmoqda..."); $("d-go").disabled = true;
    api("/api/studio/extract", fd, true).then(function (j) {
      docs = j.docs; items = [];
      var html = "";
      docs.forEach(function (d, i) {
        html += '<div class="st-card"><b>' + esc(d.name) + '</b> <span class="st-badge">' + d.kind + (d.pages ? " · " + d.pages + " bet" : "") + '</span> ' +
          '<span class="st-badge">qoida bo\'yicha: ' + d.n_regex + ' savol</span> ' + (Object.keys(d.figures || {}).length ? '<span class="st-badge">chizma: ' + Object.keys(d.figures).length + '</span>' : "") +
          (d.visual ? ' <span class="st-badge">AI ko\'rish kerak</span>' : "") + (d.warn ? '<div class="st-note">' + esc(d.warn) + '</div>' : "") + '</div>';
        d.regex_items.forEach(function (it) { it._doc = i; items.push(it); });
      });
      $("d-docs").innerHTML = html; $("d-ai").disabled = false; $("d-vis").disabled = false;
      renderItems(); status(items.length + " savol topildi. Natija yomon bo'lsa — 2-qadam (AI).");
    }).catch(function (e) { status(e.message); }).then(function () { $("d-go").disabled = false; });
  };
  $("d-ai").onclick = function () {
    var chunks = []; docs.forEach(function (d, i) { (d.chunks || []).forEach(function (c) { chunks.push({i: i, c: c}); }); });
    if (!chunks.length) { status("Matn bo'laklari yo'q — 'AI ko'rish' dan foydalaning."); return; }
    var out = [], n = 0; $("d-ai").disabled = true;
    (function next() {
      if (n >= chunks.length) { items = out; renderItems(); status("AI: " + out.length + " savol."); $("d-ai").disabled = false; return; }
      status("AI tahlil: " + (n + 1) + "/" + chunks.length);
      api("/api/studio/ai-parse", {text: chunks[n].c, subject: $("d-subject").value, mode: $("d-mode").value, hint: (($("d-topic") && $("d-topic").value.trim()) ? ("Barcha savollar mavzusi: " + $("d-topic").value.trim() + ". ") : "") + $("d-hint").value}).then(function (j) {
        j.items.forEach(function (it) { it.src = docs[chunks[n].i].name; out.push(it); }); n++; next();
      }).catch(function (e) { status(e.message + " (" + (n + 1) + "-bo'lak)"); $("d-ai").disabled = false; if (out.length) { items = out; renderItems(); } });
    })();
  };
  $("d-vis").onclick = function () {
    var fs = files.filter(function (f) { return /\.(pdf|png|jpe?g|webp|gif)$/i.test(f.name); });
    if (!fs.length) { status("PDF/rasm yo'q"); return; }
    var out = items.slice(), k = 0; $("d-vis").disabled = true;
    (function next() {
      if (k >= fs.length) { items = out; renderItems(); status("AI ko'rish tugadi."); $("d-vis").disabled = false; return; }
      status("AI ko'rmoqda: " + fs[k].name); var fd = new FormData(); fd.append("file", fs[k]); fd.append("subject", $("d-subject").value); fd.append("mode", $("d-mode").value);
      api("/api/studio/ai-vision", fd, true).then(function (j) { out = out.concat(j.items); k++; next(); })
        .catch(function (e) { status(e.message); $("d-vis").disabled = false; });
    })();
  };
  function figHtml(f) {
    if (!f || !f.q) return "";
    var q = f.q;
    if (q.type === "svg") return '<div class="fig">' + q.svg + "</div>";
    if (q.data) return '<div class="fig"><img style="width:' + (f.w || 60) + '%" src="data:' + (q.mime || "image/png") + ";base64," + q.data + '"></div>';
    return "";
  }
  function renderItems() {
    var hide = $("d-hide-dup").checked, html = "", shown = 0;
    items.forEach(function (it, i) {
      if (it.sel === undefined) it.sel = !it.dup;
      var _ft = $("d-topic") && $("d-topic").value.trim(); if (_ft && !it._topicSet) { it.topic = _ft; it._topicSet = true; }
      if (hide && it.dup) return; shown++;
      html += '<div class="st-item' + (it.dup ? " dup" : "") + '" data-i="' + i + '"><div class="meta"><label><input type="checkbox" class="sel" ' + (it.sel ? "checked" : "") + '> #' + (it.no || i + 1) + '</label>' +
        '<span class="st-badge">' + it.qtype + '</span>' + (it.solved ? '<span class="st-badge">AI yechdi</span>' : "") + (it.dup ? '<span class="st-badge">takror</span>' : "") +
        (it.figure ? '<span class="st-badge">chizma</span>' : "") + (it.figure_note ? '<span class="st-badge" title="' + esc(it.figure_note) + '">chizma kerak?</span>' : "") +
        '<input type="text" class="topic" style="width:200px" value="' + esc(it.topic || "") + '" placeholder="mavzu">' +
        '<select class="diff">' + [1, 2, 3].map(function (d) { return '<option ' + (it.difficulty === d ? "selected" : "") + ">" + d + "</option>"; }).join("") + '</select>' +
        '<select class="tier"><option value="">tarif: avto</option><option value="0">Free</option><option value="1">Pro</option><option value="2">Ultra</option></select>' +
        (it.figure ? '<label>kenglik <input type="range" class="fw" min="20" max="100" value="' + ((it.figure.w) || 60) + '"></label>' : "") +
        '</div><textarea class="qtext" rows="2">' + esc(it.question) + '</textarea>' + figHtml(it.figure) +
        (it.qtype === "open" ? '<div class="st-note">Qabul qilinadigan javoblar (vergul bilan):</div><input type="text" class="acc" value="' + esc((it.options || []).join(", ")) + '">' :
          '<div class="opts">' + (it.options || []).map(function (o, k) { return '<label><input type="radio" name="c' + i + '" class="ci" value="' + k + '" ' + (it.correct_index === k ? "checked" : "") + '> <input type="text" class="op" value="' + esc(o) + '"></label>'; }).join("") + '</div>') +
        '<textarea class="expl" rows="1" placeholder="izoh">' + esc(it.explanation || "") + '</textarea></div>';
    });
    $("d-list").innerHTML = html; $("d-res").hidden = !items.length;
    $("d-count").textContent = items.length + " savol (" + shown + " ko'rsatilgan)";
  }
  $("d-hide-dup").onchange = function () { sync(); renderItems(); };
  function sync() {
    document.querySelectorAll("#d-list .st-item").forEach(function (el) {
      var it = items[+el.dataset.i]; it.sel = el.querySelector(".sel").checked; it.topic = el.querySelector(".topic").value;
      it.difficulty = +el.querySelector(".diff").value; var t = el.querySelector(".tier").value; it.min_plan = t === "" ? undefined : +t;
      it.question = el.querySelector(".qtext").value; it.explanation = el.querySelector(".expl").value;
      var fw = el.querySelector(".fw"); if (fw && it.figure) it.figure.w = +fw.value;
      var acc = el.querySelector(".acc"); if (acc) it.options = acc.value.split(",").map(function (s) { return s.trim(); }).filter(Boolean);
      else { it.options = Array.prototype.map.call(el.querySelectorAll(".op"), function (o) { return o.value; }); var c = el.querySelector(".ci:checked"); if (c) it.correct_index = +c.value; }
    });
  }
  $("d-list").addEventListener("input", function (e) { if (e.target.classList.contains("fw")) { var el = e.target.closest(".st-item"), img = el.querySelector(".fig img"); if (img) img.style.width = e.target.value + "%"; } });
  $("d-commit").onclick = function () {
    sync(); var sub = $("d-subject").value, groups = {}, total = 0;
    items.filter(function (i) { return i.sel; }).forEach(function (it) { var s = it.subject || sub; if (s === "auto") return; (groups[s] = groups[s] || []).push(it); });
    var skipped = items.filter(function (i) { return i.sel && (i.subject || sub) === "auto"; }).length;
    if (skipped) { status("Fanni tanlang (avtomatik emas) — " + skipped + " savolning fani aniqlanmagan."); return; }
    var keys = Object.keys(groups); if (!keys.length) { status("Hech narsa tanlanmagan."); return; }
    $("d-commit").disabled = true; var done = {added: 0, dup: 0, bad: 0};
    (function next(k) {
      if (k >= keys.length) { status("Qo'shildi: " + done.added + ", takror: " + done.dup + ", yaroqsiz: " + done.bad); $("d-commit").disabled = false; return; }
      var arr = groups[keys[k]], idx = 0;
      (function chunk() {
        if (idx >= arr.length) { next(k + 1); return; }
        api("/api/studio/commit", {subject: keys[k], mode: $("d-mode").value, items: arr.slice(idx, idx + 150), publish: $("d-pub").checked, mock_name: $("d-mock").value, tier: $("d-tier").value})
          .then(function (j) { done.added += j.added; done.dup += j.dup; done.bad += j.bad; idx += 150; status("Yozilmoqda... " + done.added); chunk(); })
          .catch(function (e) { status(e.message); $("d-commit").disabled = false; });
      })();
    })(0);
  };

  // ---------- MOCK ----------
  function loadMocks() {
    api("/api/studio/mocks").then(function (j) {
      $("m-table").innerHTML = "<tr><th>Nomi</th><th>Fan</th><th>Rejim</th><th>Variant</th><th>Savol</th><th>Kirish</th><th>Holat</th><th></th></tr>" +
        j.mocks.map(function (m) { return "<tr><td>" + esc(m.name) + "</td><td>" + esc(m.subject) + "</td><td>" + m.mode + "</td><td>" + m.variant + "</td><td>" + m.total + "</td><td>" + ["Free", "Pro", "Ultra"][m.min_plan] +
          "</td><td>" + (m.active ? "faol" : "o'chiq") + '</td><td><button class="chip" data-t="' + m.id + '" data-a="' + (m.active ? 0 : 1) + '">' + (m.active ? "O'chirib qo'yish" : "Yoqish") + '</button> <button class="chip" data-d="' + m.id + '">O\'chirish</button></td></tr>'; }).join("");
    }).catch(function (e) { $("m-status").textContent = e.message; });
  }
  $("m-table").onclick = function (e) {
    var t = e.target.dataset;
    if (t.t) api("/api/studio/mock/" + t.t + "/toggle", {active: t.a === "1"}).then(loadMocks);
    if (t.d && confirm("Mock o'chirilsinmi?")) api("/api/studio/mock/" + t.d + "/delete", {}).then(loadMocks);
  };
  $("m-go").onclick = function () {
    $("m-status").textContent = "Yaratilmoqda..."; $("m-go").disabled = true;
    api("/api/studio/mock/create", {subject: $("m-subject").value, mode: $("m-mode").value, name: $("m-name").value, variants: +$("m-var").value, min_plan: +$("m-plan").value, time_minutes: +$("m-time").value})
      .then(function (j) { $("m-status").textContent = j.mocks.length + " ta variant yaratildi (" + j.mocks.map(function (m) { return m.total; }).join("/") + " savol)"; loadMocks(); })
      .catch(function (e) { $("m-status").textContent = e.message; }).then(function () { $("m-go").disabled = false; });
  };

  // ---------- BAZA ----------
  function loadBank() {
    api("/api/studio/bank").then(function (j) {
      $("b-table").innerHTML = "<tr><th>Fan</th><th>Rejim</th><th>Jami</th><th>Mavzu</th><th>Free</th><th>Pro (jami)</th><th>Ultra (jami)</th><th>Ochiq</th><th>Moslash</th><th>Chizma</th><th>Nofaol</th></tr>" +
        j.table.map(function (r) { return '<tr class="click" data-s="' + r.subject + '" data-m="' + r.mode + '"><td>' + esc(r.subject_name) + "</td><td>" + r.mode + "</td><td>" + r.total + "</td><td>" + r.topics + "</td><td class='" + (r.free < 50 ? "low" : "") + "'>" + r.free + "</td><td class='" + (r.free + r.pro < 50 ? "low" : "") + "'>" + (r.free + r.pro) + "</td><td>" + r.total + "</td><td>" + r.open + "</td><td>" + r.match + "</td><td>" + r.figures + "</td><td>" + r.inactive + "</td></tr>"; }).join("");
    }).catch(function (e) { $("b-status").textContent = e.message; });
  }
  $("b-refresh").onclick = loadBank;
  $("b-table").onclick = function (e) {
    var tr = e.target.closest("tr.click"); if (!tr) return;
    api("/api/studio/topics?subject=" + tr.dataset.s + "&mode=" + tr.dataset.m).then(function (j) {
      $("b-topics-h").textContent = tr.dataset.s + " / " + tr.dataset.m + " — " + j.topics.length + " mavzu";
      $("b-topics").innerHTML = "<tr><th>Kod</th><th>Sinf</th><th>Mavzu</th><th>Tarif</th><th>Savol</th><th>Free</th><th>Pro (jami)</th><th>Ochiq</th><th>Moslash</th><th>Chizma</th><th></th></tr>" +
        j.topics.map(function (t) { return "<tr><td>" + esc(t.code) + "</td><td>" + t.grade + "</td><td>" + esc(t.topic) + "</td><td>" + t.tier + "</td><td class='" + (t.total < 10 ? "low" : "") + "'>" + t.total + "</td><td>" + t.free_q + "</td><td>" + t.pro_q + "</td><td>" + t.open + "</td><td>" + t.match + "</td><td>" + t.figures + '</td><td><button class="chip gen" data-s="' + tr.dataset.s + '" data-m="' + tr.dataset.m + '" data-t="' + esc(t.topic) + '">AI: +8 savol</button></td></tr>'; }).join("");
    });
  };
  $("b-topics").onclick = function (e) {
    var d = e.target.dataset; if (!d || !d.t || !e.target.classList.contains("gen")) return;
    e.target.disabled = true; e.target.textContent = "…";
    api("/api/studio/ai-generate", {subject: d.s, mode: d.m, topic: d.t, count: 8}).then(function (j) {
      items = j.items; docs = []; $("d-subject").value = d.s; $("d-mode").value = d.m; renderItems();
      document.querySelector('#st-tabs [data-t="doc"]').click(); status("AI " + items.length + " savol yaratdi — tekshirib, bazaga qo'shing.");
    }).catch(function (er) { e.target.textContent = er.message.slice(0, 30); });
  };
  $("b-seed").onclick = function () {
    $("b-seed").disabled = true;
    (function step(n) {
      api("/api/studio/seed", {step: n}).then(function (j) {
        if (j.done) { $("b-status").textContent = "Baza yangilandi."; $("b-seed").disabled = false; loadBank(); return; }
        $("b-status").textContent = "Yuklanmoqda " + (n + 1) + "/" + j.total_steps + " (" + j.subject + "/" + j.mode + ", +" + j.added + ")"; step(n + 1);
      }).catch(function (e) { $("b-status").textContent = e.message; $("b-seed").disabled = false; });
    })(0);
  };

  // ---------- CLAUDE ----------
  var hist = [];
  function addMsg(role, text) { var d = document.createElement("div"); d.className = "st-msg " + (role === "user" ? "u" : "a"); d.textContent = text; $("a-chat").appendChild(d); $("a-chat").scrollTop = 1e6; }
  function send(text) {
    if (!text.trim()) return; addMsg("user", text); hist.push({role: "user", text: text}); $("a-input").value = ""; $("a-send").disabled = true; addMsg("assistant", "…");
    api("/api/studio/assistant", {messages: hist}).then(function (j) {
      $("a-chat").lastChild.textContent = j.reply; hist.push({role: "assistant", text: j.reply});
      (j.actions || []).forEach(showAction);
    }).catch(function (e) { $("a-chat").lastChild.textContent = e.message; }).then(function () { $("a-send").disabled = false; });
  }
  function showAction(a) {
    var d = document.createElement("div"); d.className = "st-act";
    d.innerHTML = "<b>" + esc(a.type) + "</b> — " + esc(a.reason) + "<pre>" + esc(JSON.stringify(a.payload, null, 1)) + '</pre><button class="btn-primary ok">Qo\'llash</button> <button class="btn-secondary no">Rad etish</button> <span class="st-note"></span>';
    d.querySelector(".no").onclick = function () { d.remove(); };
    d.querySelector(".ok").onclick = function () {
      api("/api/studio/assistant/apply", {action: a}).then(function (j) { d.querySelector(".st-note").textContent = "Bajarildi ✓"; d.querySelector(".ok").disabled = true; })
        .catch(function (e) { d.querySelector(".st-note").textContent = e.message; });
    };
    $("a-actions").appendChild(d);
  }
  $("a-send").onclick = function () { send($("a-input").value); };
  $("a-input").onkeydown = function (e) { if (e.key === "Enter") send($("a-input").value); };
  document.querySelectorAll(".chip").forEach(function (c) { if (c.parentNode.classList.contains("st-chips")) c.onclick = function () { send(c.textContent); }; });
})();
