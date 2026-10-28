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
