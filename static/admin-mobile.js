/* v249: Admin panel — kichik telefonlar. Jadvallar telefonda kartochkalarga aylanadi:
   har bir katak oldida ustun nomi yoziladi, hech bir ustun ekrandan chiqib, yashirinib qolmaydi. */
(function () {
  var mq = window.matchMedia ? window.matchMedia("(max-width: 640px)") : null;
  var SKIP = ".epreview, .la-chat, .la-msg, .lr, .no-card, .quiz-question-card, .lz-tr-chart";
  function headOf(table) {
    var row = table.tHead && table.tHead.rows[0];
    if (!row) {
      var first = table.rows[0];
      if (first && first.cells.length && Array.prototype.every.call(first.cells, function (c) { return c.tagName === "TH"; })) row = first;
    }
    if (!row) return null;
    var out = [];
    Array.prototype.forEach.call(row.cells, function (c) {
      var t = (c.getAttribute("aria-label") || c.textContent || "").replace(/\s+/g, " ").trim();
      for (var i = 0; i < (c.colSpan || 1); i++) out.push(t);
    });
    return { labels: out, row: row };
  }
  function cardify(table) {
    if (table.closest(SKIP)) return;
    var h = headOf(table);
    if (!h || h.labels.length < 3) return;          // 1–2 ustunli jadval telefonga sig'adi
    table.classList.add("lz-cards");
    if (h.row.parentNode && h.row.parentNode.tagName !== "THEAD") h.row.classList.add("lz-head-row");
    Array.prototype.forEach.call(table.rows, function (tr) {
      if (tr === h.row) return;
      var i = 0;
      Array.prototype.forEach.call(tr.cells, function (td) {
        var span = td.colSpan || 1;
        if (span >= h.labels.length || tr.cells.length === 1) { td.classList.add("lz-full"); }
        else if (!td.hasAttribute("data-label")) td.setAttribute("data-label", h.labels[i] || "");
        i += span;
      });
    });
  }
  function run(root) {
    if (mq && !mq.matches) return;
    (root || document).querySelectorAll(".app-content table").forEach(cardify);
  }
  var pending = 0;
  function later() { if (!pending) pending = requestAnimationFrame(function () { pending = 0; run(); }); }
  function init() {
    run();
    var host = document.querySelector(".app-content");
    if (host && window.MutationObserver) new MutationObserver(later).observe(host, { childList: true, subtree: true });
    if (mq && mq.addEventListener) mq.addEventListener("change", function () { run(); });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
