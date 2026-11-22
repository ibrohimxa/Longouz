/* v246: Moklar — mavzular ro'yxati, ochiladigan savollar, qidiruv, saralash, «Saqlandi» bildirishnomasi. */
(function () {
  "use strict";
  var M = window.MOKLAR || {}, list = document.getElementById("mk-list");
  if (!list) return;
  var cache = {};
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function editUrl(topic, n) {
    return M.prefix + "/topics/edit?subject=" + encodeURIComponent(M.subject) + "&mode=" + encodeURIComponent(M.mode) +
      "&topic=" + encodeURIComponent(topic) + "&src=moklar" + (n ? "&start=" + n : "");
  }
  var DIFF = { 1: ["Oson", "d1"], 2: ["O'rta", "d2"], 3: ["Qiyin", "d3"] }, PLAN = { 1: "Pro", 2: "Ultra" };

  function renderQs(li, items) {
    var body = li.querySelector(".mk-body"), topic = li.dataset.topic;
    if (!items.length) { body.innerHTML = '<p class="mk-none">Savol yo\'q. <a href="' + editUrl(topic) + '">Tahrirlashda qo\'shish</a></p>'; return; }
    body.innerHTML = '<div class="mk-qtools"><span>' + items.length + ' ta savol</span><label><input type="checkbox" class="mk-ans" checked> To\'g\'ri javoblar</label></div>' +
      '<ol class="mk-qs">' + items.map(function (q) {
        var d = DIFF[q.diff] || ["—", "d0"];
        var opts = q.type === "open" ? '<div class="mk-open">Ochiq savol · javob: <b>' + esc((q.opts || []).join(" / ")) + "</b></div>" :
          '<ol class="mk-opts" type="A">' + (q.opts || []).map(function (o, i) { return '<li class="' + (i === q.ci ? "ok" : "") + '">' + esc(o) + "</li>"; }).join("") + "</ol>";
        return '<li class="mk-q' + (q.active ? "" : " off") + '" data-search="' + esc((q.q + " " + (q.opts || []).join(" ")).toLowerCase()) + '">' +
          '<div class="mk-qhead"><span class="mk-qn">' + q.n + '</span><div class="mk-qtext">' + esc(q.q) + "</div>" +
          '<a class="mk-qedit" href="' + editUrl(topic, q.n) + '" title="Shu savoldan tahrirlash">Tahrirlash</a></div>' + opts +
          '<div class="mk-tags"><span class="' + d[1] + '">' + d[0] + "</span>" + (q.fig ? "<span>Chizmali</span>" : "") +
          (PLAN[q.plan] ? "<span>" + PLAN[q.plan] + "</span>" : "") + (q.active ? "" : '<span class="hid">Yashirin</span>') + "<span>ID " + q.id + "</span></div>" +
          (q.expl ? '<details class="mk-expl"><summary>Izoh</summary><p>' + esc(q.expl) + "</p></details>" : "") + "</li>";
      }).join("") + "</ol>";
    body.querySelector(".mk-ans").addEventListener("change", function () { body.classList.toggle("hide-ans", !this.checked); });
  }

  function open(li, on) {
    var body = li.querySelector(".mk-body"), btn = li.querySelector(".mk-toggle");
    if (on === undefined) on = body.hidden;
    body.hidden = !on; li.classList.toggle("open", on); btn.setAttribute("aria-expanded", on ? "true" : "false");
    li.querySelector(".mk-btn.view").textContent = on ? "Yopish" : "Ko'rish";
    if (!on) return;
    var key = li.dataset.topic;
    if (cache[key]) { renderQs(li, cache[key]); return; }
    body.innerHTML = '<p class="mk-loading"><i></i>Savollar yuklanmoqda…</p>';
    fetch(M.prefix + "/api/moklar/questions?subject=" + encodeURIComponent(M.subject) + "&mode=" + encodeURIComponent(M.mode) + "&topic=" + encodeURIComponent(key), { credentials: "same-origin" })
      .then(function (r) { return r.json(); }).then(function (d) { cache[key] = d.items || []; renderQs(li, cache[key]); filter(); })
      .catch(function () { body.innerHTML = '<p class="mk-none">Yuklab bo\'lmadi. Qayta urinib ko\'ring.</p>'; });
  }
  list.addEventListener("click", function (e) {
    var li = e.target.closest(".mk-topic"); if (!li) return;
    if (e.target.closest(".mk-toggle") || e.target.closest(".mk-btn.view")) open(li);
  });

  // qidiruv: mavzu nomi va (ochilgan bo'lsa) savol matni bo'yicha
  var q = document.getElementById("mk-q");
  function filter() {
    var v = (q.value || "").trim().toLowerCase();
    list.querySelectorAll(".mk-topic").forEach(function (li) {
      var hitName = !v || li.dataset.topic.toLowerCase().indexOf(v) >= 0, hitQ = false;
      li.querySelectorAll(".mk-q").forEach(function (x) { var h = !v || x.dataset.search.indexOf(v) >= 0; x.hidden = !(h || hitName); if (h && v) hitQ = true; });
      li.hidden = !(hitName || hitQ);
    });
  }
  q.addEventListener("input", filter);

  // saralash
  var sortSel = document.getElementById("mk-sort");
  sortSel.addEventListener("change", function () {
    var arr = Array.prototype.slice.call(list.querySelectorAll(".mk-topic")), v = this.value;
    arr.sort(function (a, b) {
      if (v === "name") return a.dataset.topic.localeCompare(b.dataset.topic);
      if (v === "most") return b.dataset.total - a.dataset.total;
      if (v === "least") return a.dataset.total - b.dataset.total;
      if (v === "new") return b.dataset.last - a.dataset.last;
      return a.dataset.i - b.dataset.i;
    });
    arr.forEach(function (li, i) { li.querySelector(".mk-n").textContent = i + 1; list.appendChild(li); });
  });

  // tahrirlashdan qaytganda: mavzu ochiladi va «Saqlandi» bildirishnomasi chiqadi
  if (M.open) {
    var target = Array.prototype.find.call(list.querySelectorAll(".mk-topic"), function (li) { return li.dataset.topic === M.open; });
    if (target) { open(target, true); target.classList.add("flash"); setTimeout(function () { target.scrollIntoView({ behavior: "smooth", block: "start" }); }, 80); }
  }
  if (M.saved !== "" && M.saved != null) {
    var t = document.getElementById("mk-toast"), n = parseInt(M.saved, 10) || 0;
    t.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg><span><b>O\'zgarishlar saqlandi</b>' +
      (n ? n + " ta o'zgarish saytga chop etildi" : "Saytdagi holat yangilandi") + "</span>";
    t.hidden = false; requestAnimationFrame(function () { t.classList.add("in"); });
    setTimeout(function () { t.classList.remove("in"); setTimeout(function () { t.hidden = true; }, 400); }, 4200);
    try { history.replaceState(null, "", location.pathname + "?subject=" + encodeURIComponent(M.subject) + "&mode=" + encodeURIComponent(M.mode)); } catch (e) {}
  }
})();
