/* LongoUZ — tugmalar atrofida suvdek aylanuvchi chegara */
(function () {
  var SEL = ".btn,.btn-primary,.btn-secondary,.btn-outline,.btn-ghost,.nav-cta,.au-submit,.dash-btn,.hm-pbtn,.f215-btn,.lz-primary,.lz-ghost,.pm-submit,.plan-btn,.hero-cta,.cta-primary,.checkout-open-btn,#quiz-next-btn,.quiz-next,.au-google,.au-social a,.au-social button";
  function add(el) {
    if (el.__lzr || el.querySelector(":scope > .lz-ring")) return;
    var r = el.getBoundingClientRect(); if (r.width && (r.width < 60 || r.height < 28)) return;
    el.__lzr = 1;
    if (getComputedStyle(el).position === "static") el.style.position = "relative";
    var s = document.createElement("span"); s.className = "lz-ring"; s.setAttribute("aria-hidden", "true"); el.appendChild(s);
  }
  function scan(root) { (root || document).querySelectorAll(SEL).forEach(add); }
  function init() { scan(); new MutationObserver(function (m) { m.forEach(function (x) { x.addedNodes.forEach(function (n) { if (n.nodeType === 1) { if (n.matches && n.matches(SEL)) add(n); scan(n); } }); }); }).observe(document.body, { childList: true, subtree: true }); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
