// LongoUZ admin — mavzudagi savollar ro'yxati: bosilganda tugmalar qatori (o'chirish / tahrirlash / nashr-yopiq).
(function () {
  "use strict";
  var P = JSON.parse(document.getElementById("list-data").textContent);
  var $ = function (id) { return document.getElementById(id); };
  var PAGE = 40, page = 1, filter = "all", term = "", openId = null, busy = false;
  var qs = P.questions;

  function post(path, body) {
    return fetch(P.prefix + path, { method: "POST", credentials: "same-origin",
      headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" }, body: JSON.stringify(body || {}) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) { if (!r.ok) throw new Error(d.detail || "Xatolik"); return d; }); });
  }
  function filtered() {
    return qs.filter(function (q) {
      if (filter === "on" && !q.is_active) return false;
      if (filter === "off" && q.is_active) return false;
      return !term || q.question.toLowerCase().indexOf(term) !== -1;
    });
  }
  function stat() {
    var on = qs.filter(function (q) { return q.is_active; }).length;
    $("stat").textContent = qs.length + " savol · " + on + " nashrda · " + (qs.length - on) + " yopiq";
  }
  function btn(text, cls, fn) { var b = document.createElement("button"); b.type = "button"; b.className = "abtn " + cls; b.textContent = text; b.addEventListener("click", fn); return b; }

  function draw() {
    stat();
    var list = filtered(), pages = Math.max(1, Math.ceil(list.length / PAGE));
    page = Math.min(page, pages);
    var box = $("qlist"); box.innerHTML = "";
    if (!list.length) { var e = document.createElement("p"); e.className = "aempty"; e.textContent = qs.length ? "Hech narsa topilmadi." : "Bu mavzuda hali savol yo'q. «+ Test qo'shish» ni bosing."; box.appendChild(e); }
    list.slice((page - 1) * PAGE, page * PAGE).forEach(function (q) {
      var row = document.createElement("div"); row.className = "qrow" + (openId === q.id ? " open" : "");
      var head = document.createElement("button"); head.type = "button"; head.className = "qrow-head"; head.setAttribute("aria-expanded", openId === q.id);
      head.innerHTML = '<span class="qrow-n"></span><span class="qrow-t"></span>' + (q.has_figure ? '<span class="qrow-fig">chizma</span>' : "") + '<span class="qrow-st"></span>';
      head.querySelector(".qrow-n").textContent = q.n; head.querySelector(".qrow-t").textContent = q.question;
      var st = head.querySelector(".qrow-st"); st.textContent = q.is_active ? "Nashrda" : "Yopiq"; st.classList.add(q.is_active ? "on" : "off");
      head.addEventListener("click", function () { openId = openId === q.id ? null : q.id; draw(); });
      var body = document.createElement("div"); body.className = "qrow-body";
      var inner = document.createElement("div"); inner.className = "qrow-in";
      q.options.forEach(function (o, i) { var d = document.createElement("div"); d.textContent = "ABCD"[i] + ") " + o + (i === q.correct_index ? "  ✓" : ""); if (i === q.correct_index) d.className = "corr"; inner.appendChild(d); });
      var btns = document.createElement("div"); btns.className = "qrow-btns";
      btns.appendChild(btn("O'chirish", "danger", function () { del(q); }));
      var edit = document.createElement("a"); edit.className = "abtn"; edit.textContent = "Tahrirlash";
      edit.href = P.prefix + "/topics/edit?subject=" + encodeURIComponent(P.subject) + "&mode=" + encodeURIComponent(P.mode) + "&topic=" + encodeURIComponent(P.topic) + "&start=" + q.n;
      btns.appendChild(edit);
      btns.appendChild(btn(q.is_active ? "Yopiq qilish" : "Nashr qilish (hamma ko'radi)", q.is_active ? "" : "primary", function () { toggle(q); }));
      body.append(inner, btns); row.append(head, body); box.appendChild(row);
    });
    var pg = $("pager"); pg.innerHTML = "";
    if (pages > 1) for (var p = 1; p <= pages; p++) (function (p) {
      var b = btn(String(p), p === page ? "primary" : "", function () { page = p; draw(); window.scrollTo({ top: 0, behavior: "smooth" }); }); pg.appendChild(b);
    })(p);
  }
  function toggle(q) {
    if (busy) return; busy = true;
    post("/api/question/" + q.id + "/active", { active: !q.is_active }).then(function (d) {
      q.is_active = d.active; LZToast.ok(q.is_active ? "Nashr qilindi ✓ — hamma ko'radi" : "Yopiq holatga o'tkazildi ✓"); draw();
    }).catch(function (e) { LZToast.err(e.message); }).finally(function () { busy = false; });
  }
  function del(q) {
    if (!confirm(q.n + "-savol butunlay o'chirilsinmi?")) return;
    post("/api/question/" + q.id + "/delete").then(function () {
      qs = qs.filter(function (x) { return x.id !== q.id; }); qs.forEach(function (x, i) { x.n = i + 1; }); openId = null; LZToast.ok("O'chirildi ✓"); draw();
    }).catch(function (e) { LZToast.err(e.message); });
  }
  $("qsearch").addEventListener("input", function () { term = this.value.trim().toLowerCase(); page = 1; draw(); });
  document.querySelectorAll("#qfilter button").forEach(function (b) {
    b.addEventListener("click", function () { filter = b.dataset.f; page = 1; document.querySelectorAll("#qfilter button").forEach(function (x) { x.classList.toggle("active", x === b); }); draw(); });
  });
  draw();
})();
