(function () {
  "use strict";
  var P = document.body.dataset.adminPrefix || "";
  var H = { "x-requested-with": "fetch", "Content-Type": "application/json" };
  var $ = function (id) { return document.getElementById(id); };
  var page = 1;
  function esc(t) { var d = document.createElement("div"); d.textContent = String(t == null ? "" : t); return d.innerHTML; }
  function toast(m, bad) { if (window.LZToast) { bad ? window.LZToast.err(m) : window.LZToast.ok(m); } }
  function api(path, method, body) {
    return fetch(P + path, { method: method || "GET", headers: H, body: body ? JSON.stringify(body) : undefined, credentials: "same-origin" })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok) throw new Error(j.detail || "Xato " + r.status); return j; }); });
  }

  var CAT = { wrong_answer: "Javob xato belgilangan", question_text: "Savol matni", options: "Variantlar", no_correct: "To'g'ri variant yo'q", figure: "Chizma", topic: "Mavzu", explanation: "Izoh", typo: "Imlo", duplicate: "Takror", other: "Boshqa" };
  function stats(d) {
    var c = d.counts || {};
    var items = [["Yangi", c["new"] || 0], ["Tahlil qilingan", c.analyzed || 0], ["Tuzatilgan", c.fixed || 0], ["Rad etilgan", c.dismissed || 0]];
    var cats = Object.keys(d.by_category || {}).sort(function (a, b) { return d.by_category[b] - d.by_category[a]; }).slice(0, 3)
      .map(function (k) { return (CAT[k] || k) + ": " + d.by_category[k]; }).join(", ");
    $("rp-stats").innerHTML = items.map(function (x) { return '<div class="rp-stat"><b>' + x[1] + "</b>" + x[0] + "</div>"; }).join("") +
      (cats ? '<div class="rp-stat"><b style="font-size:.95rem">' + esc(cats) + "</b>Ko'p uchraydigan turlar</div>" : "");
    var nb = $("btn-batch"), n = c["new"] || 0;
    if (nb) { nb.disabled = !n; nb.textContent = n ? "🤖 Yangilarini tahlil qilish (" + Math.min(5, n) + " ta)" : "🤖 Yangi shikoyat yo'q"; }
  }

  function fixForm(r) {
    var f = r.fix; if (!f) return "";
    var opts = (f.options || []).map(function (o, i) { return '<input type="text" data-o="' + i + '" value="' + esc(o) + '">'; }).join("");
    var ci = typeof f.correct_index === "number" ? f.correct_index : 0;
    return '<div class="rp-fix"><b>Taklif etilgan tuzatish (tahrirlash mumkin):</b>' +
      '<textarea data-f="question" rows="3">' + esc(f.question || r.question) + "</textarea>" +
      (opts ? '<div class="grid">' + opts + "</div>" +
        '<label>To\'g\'ri javob: <select data-f="correct_index">' + [0, 1, 2, 3].map(function (i) { return '<option value="' + i + '"' + (i === ci ? " selected" : "") + ">" + "ABCD"[i] + "</option>"; }).join("") + "</select></label>" : "") +
      (f.accept ? '<input type="text" data-f="accept" value="' + esc((f.accept || []).join(" | ")) + '" placeholder="Qabul qilinadigan javoblar (| bilan ajrating)">' : "") +
      '<textarea data-f="explanation" rows="2" placeholder="Izoh">' + esc(f.explanation || "") + "</textarea></div>";
  }

  function card(r) {
    var vcls = r.verdict === "error" ? "err" : r.verdict === "ok" ? "ok" : r.verdict ? "unc" : "";
    var vname = { error: "Xato bor", ok: "Savol to'g'ri", unclear: "Aniq emas" }[r.verdict] || "";
    var opts = (r.options || []).map(function (o, i) {
      return '<div class="' + (i === r.correct_index ? "c" : "") + '">' + "ABCD"[i] + ") " + esc(o) + (i === r.correct_index ? " ✓" : "") + "</div>";
    }).join("");
    var ai = r.verdict ? '<div class="rp-ai"><span class="rp-badge ' + vcls + '">🤖 ' + vname + " · ishonch " + r.confidence + "%</span>" +
      "<pre>" + esc(r.ai_note) + "</pre>" + fixForm(r) + "</div>" : "";
    var open = r.status === "new" || r.status === "analyzed";
    return '<div class="rp-card ' + r.status + '" data-id="' + r.id + '">' +
      '<div class="rp-head"><span class="rp-badge">#' + r.id + "</span><span class=\"rp-badge\">" + esc(r.subject_name) + " · " + esc(r.mode) + "</span>" +
      "<span>" + esc(r.topic) + "</span>" + (r.question_id ? '<span class="rp-badge">savol #' + r.question_id + "</span>" : '<span class="rp-badge">AI savoli</span>') +
      (r.same > 1 ? '<span class="rp-badge err">' + r.same + " ta shikoyat</span>" : "") +
      '<span class="rp-badge">' + esc(r.status_name) + "</span><span>" + esc(r.user) + " · " + esc(r.created) + "</span></div>" +
      '<div class="rp-q">' + esc(r.question) + "</div>" + (opts ? '<div class="rp-opts">' + opts + "</div>" : "") +
      '<div class="rp-msg"><b>' + esc(r.category_name) + "</b>" + (r.message ? "<br>" + esc(r.message) : "") + (r.selected ? "<br><small>Foydalanuvchi tanlagan: " + esc(r.selected) + "</small>" : "") + "</div>" +
      ai + (r.admin_note ? '<div class="st-note">Izoh: ' + esc(r.admin_note) + "</div>" : "") +
      (open ? '<div class="rp-actions">' +
        '<button class="btn-primary admin-btn-sm" data-a="analyze">🤖 ' + (r.verdict ? "Qayta tahlil" : "AI bilan tahlil") + "</button>" +
        (r.fix || r.action === "deactivate" ? '<button class="btn-primary admin-btn-sm" data-a="apply">✅ Tuzatishni qo\'llash</button>' : "") +
        (r.question_id ? '<a class="btn-secondary admin-btn-sm" target="_blank" href="' + P + "/questions/" + r.question_id + '/edit">✏️ Qo\'lda tahrirlash</a>' +
          '<button class="btn-secondary admin-btn-sm" data-a="hide">🙈 Savolni yashirish</button>' : "") +
        '<button class="btn-secondary admin-btn-sm" data-a="dismiss">Rad etish</button></div>' : "") + "</div>";
  }

  function load() {
    $("rp-list").innerHTML = '<p class="st-note">Yuklanmoqda…</p>';
    api("/api/reports?status=" + encodeURIComponent($("f-status").value) + "&subject=" + encodeURIComponent($("f-subject").value) + "&page=" + page).then(function (d) {
      stats(d);
      $("rp-list").innerHTML = d.items.length ? d.items.map(card).join("") : '<p class="st-note">Shikoyat yo\'q 🎉</p>';
      var pages = Math.ceil(d.total / d.per);
      $("rp-pager").innerHTML = pages > 1 ? '<button class="btn-secondary admin-btn-sm" ' + (page <= 1 ? "disabled" : "") + ' data-p="-1">←</button><span>' + page + " / " + pages +
        '</span><button class="btn-secondary admin-btn-sm" ' + (page >= pages ? "disabled" : "") + ' data-p="1">→</button>' : "";
    }).catch(function (e) { $("rp-list").innerHTML = '<div class="form-error">' + esc(e.message) + "</div>"; });
  }

  function collectFix(cardEl) {
    var box = cardEl.querySelector(".rp-fix"); if (!box) return null;
    var fix = {};
    var q = box.querySelector('[data-f="question"]'); if (q) fix.question = q.value.trim();
    var os = box.querySelectorAll("[data-o]"); if (os.length) fix.options = Array.prototype.map.call(os, function (i) { return i.value.trim(); });
    var ci = box.querySelector('[data-f="correct_index"]'); if (ci) fix.correct_index = parseInt(ci.value, 10);
    var ac = box.querySelector('[data-f="accept"]'); if (ac) fix.accept = ac.value.split("|").map(function (s) { return s.trim(); }).filter(Boolean);
    var ex = box.querySelector('[data-f="explanation"]'); if (ex) fix.explanation = ex.value.trim();
    return fix;
  }

  $("rp-list").addEventListener("click", function (e) {
    var b = e.target.closest("button[data-a]"); if (!b) return;
    var el = b.closest(".rp-card"), id = el.dataset.id, a = b.dataset.a;
    b.disabled = true;
    var done = function (msg) { toast(msg); load(); }, fail = function (err) { b.disabled = false; toast(err.message, true); };
    if (a === "analyze") { b.textContent = "Tahlil qilinmoqda…"; api("/api/reports/" + id + "/analyze", "POST").then(function () { done("Tahlil tayyor"); }).catch(fail); }
    else if (a === "apply") { api("/api/reports/" + id + "/apply", "POST", { fix: collectFix(el) }).then(function (r) { done("Tuzatildi (" + r.resolved + " ta shikoyat yopildi)"); }).catch(fail); }
    else if (a === "hide") { if (!confirm("Savolni foydalanuvchilardan yashirasizmi?")) { b.disabled = false; return; } api("/api/reports/" + id + "/hide-question", "POST").then(function () { done("Yashirildi"); }).catch(fail); }
    else if (a === "dismiss") { var note = prompt("Rad etish sababi (ixtiyoriy):") || ""; api("/api/reports/" + id + "/dismiss", "POST", { note: note }).then(function () { done("Rad etildi"); }).catch(fail); }
  });
  $("rp-pager").addEventListener("click", function (e) { var b = e.target.closest("button[data-p]"); if (b) { page += parseInt(b.dataset.p, 10); load(); } });
  $("f-status").addEventListener("change", function () { page = 1; load(); });
  $("f-subject").addEventListener("change", function () { page = 1; load(); });
  $("btn-reload").addEventListener("click", load);
  $("btn-batch").addEventListener("click", function () {
    var b = this; b.disabled = true; $("batch-msg").textContent = "AI tahlil qilmoqda… (1-2 daqiqa olishi mumkin)";
    api("/api/reports/analyze-batch", "POST", { limit: 5, apply: $("cfg-auto-fix").checked }).then(function (r) {
      $("batch-msg").textContent = r.done + " ta tahlil qilindi" + (r.left ? ", yana " + r.left + " ta kutmoqda" : "") + ".";
      b.disabled = false; load();
    }).catch(function (e) { b.disabled = false; $("batch-msg").textContent = e.message; });
  });
  function saveCfg() {
    api("/api/reports/settings", "POST", { auto_analyze: $("cfg-auto-analyze").checked, auto_fix: $("cfg-auto-fix").checked, min_conf: parseInt($("cfg-min-conf").value, 10) || 92 })
      .then(function () { $("cfg-msg").textContent = "Saqlandi ✓"; setTimeout(function () { $("cfg-msg").textContent = ""; }, 1500); }).catch(function (e) { $("cfg-msg").textContent = e.message; });
  }
  ["cfg-auto-analyze", "cfg-auto-fix", "cfg-min-conf"].forEach(function (id) { $(id).addEventListener("change", saveCfg); });
  load();
})();
