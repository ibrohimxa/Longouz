// ============================================================================
// LongoUZ — mavzu (dark/light) boshqaruvi
// Bu skript sahifa <head>'ida, boshqa hamma narsadan OLDIN yuklanadi —
// shu bilan "flash of wrong theme" (noto'g'ri rang bir lahza ko'rinishi) oldi olinadi.
// ============================================================================

(function () {
  var saved = localStorage.getItem("longouz_theme");
  var theme = saved || "dark"; // standart holat — dark mode
  document.documentElement.setAttribute("data-theme", theme);
})();

/* Savollar bazasi serverda hali to'liq yuklanmagan bo'lsa (Vercel birinchi joylashdan keyin), shuni sahifa
   orqali tugaguncha davom ettiradi. Tugagach bir marta eslab qoladi va boshqa so'ramaydi. */
(function () {
  try {
    if (localStorage.getItem("lz_seed_v229") === "1") return;
  } catch (e) {}
  if (!window.fetch || /^\/(neo|static)/.test(location.pathname)) return;
  var tries = 0;
  function step() {
    tries++;
    fetch("/api/seed-step", { credentials: "same-origin" }).then(function (r) { return r.json(); }).then(function (j) {
      if (j && j.done) { try { localStorage.setItem("lz_seed_v229", "1"); } catch (e) {} return; }
      if (tries < 40) setTimeout(step, (j && j.busy) ? 4000 : 800);
    }).catch(function () { if (tries < 40) setTimeout(step, 5000); });
  }
  window.addEventListener("load", function () { setTimeout(step, 1200); });
})();
