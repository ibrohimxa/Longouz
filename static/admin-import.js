(function () {
  "use strict";
  // --- Fayl tanlash / tashlash ---
  var zone = document.getElementById("drop-zone"), input = document.getElementById("imp-file"), list = document.getElementById("drop-list");
  function fmt(n) { return n > 1048576 ? (n / 1048576).toFixed(1) + " MB" : Math.max(1, Math.round(n / 1024)) + " KB"; }
  function renderList() {
    if (!list || !input) return;
    list.innerHTML = "";
    Array.prototype.forEach.call(input.files, function (f) {
      var li = document.createElement("li");
      li.textContent = f.name + " — " + fmt(f.size);
      list.appendChild(li);
    });
    zone.classList.toggle("has-files", input.files.length > 0);
  }
  if (zone && input) {
    input.addEventListener("change", renderList);
    ["dragenter", "dragover"].forEach(function (ev) { zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.add("drag"); }); });
    ["dragleave", "drop"].forEach(function (ev) { zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.remove("drag"); }); });
    zone.addEventListener("drop", function (e) {
      if (e.dataTransfer && e.dataTransfer.files.length) { input.files = e.dataTransfer.files; renderList(); }
    });
  }
  var form = document.getElementById("imp-form"), btn = document.getElementById("imp-submit");
  if (form && btn) form.addEventListener("submit", function () { btn.disabled = true; btn.textContent = "Fayllar o'qilmoqda…"; });

  // --- Ko'rib chiqish: filtr, qidiruv, hisoblagich ---
  var cards = Array.prototype.slice.call(document.querySelectorAll(".import-card"));
  if (!cards.length) return;
  var current = "all", q = "";
  function apply() {
    cards.forEach(function (c) {
      var okKind = current === "all" || c.getAttribute("data-kind") === current;
      var okText = !q || c.getAttribute("data-text").indexOf(q) !== -1;
      c.style.display = okKind && okText ? "" : "none";
    });
  }
  var filter = document.getElementById("imp-filter");
  filter.addEventListener("click", function (e) {
    var b = e.target.closest("[data-f]");
    if (!b) return;
    current = b.getAttribute("data-f");
    Array.prototype.forEach.call(filter.querySelectorAll("[data-f]"), function (x) { x.classList.toggle("active", x === b); });
    apply();
  });
  document.getElementById("imp-search").addEventListener("input", function (e) { q = e.target.value.trim().toLowerCase(); apply(); });
  var boxes = Array.prototype.slice.call(document.querySelectorAll(".inc-box"));
  var counter = document.getElementById("sel-count");
  function count() { counter.textContent = boxes.filter(function (b) { return b.checked; }).length; }
  boxes.forEach(function (b) { b.addEventListener("change", count); });
  document.getElementById("chk-all-new").addEventListener("change", function (e) {
    boxes.forEach(function (b) { if (b.getAttribute("data-kind") === "new") b.checked = e.target.checked; });
    count();
  });
  count();
  // --- Takrorlar hisobotini CSV ---
  var csvBtn = document.getElementById("dup-csv");
  if (csvBtn) csvBtn.addEventListener("click", function () {
    var rows = Array.prototype.map.call(document.querySelectorAll("#dup-table tr"), function (tr) {
      return Array.prototype.map.call(tr.children, function (td) { return '"' + td.textContent.replace(/\s+/g, " ").trim().replace(/"/g, '""') + '"'; }).join(",");
    });
    var blob = new Blob(["﻿" + rows.join("\n")], { type: "text/csv;charset=utf-8" });
    var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = "takrorlar_hisoboti.csv"; a.click();
  });
})();
