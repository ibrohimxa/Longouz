// LongoUZ — savol ko'rinishi (admin tahrirlagan) va test oynasi tuzilmasini qo'llash.
// Ham test yechish sahifasida, ham admin tahrirlagich ko'rinishida (preview) ishlatiladi.
(function (global) {
  "use strict";
  function num(v, d) { var n = parseFloat(v); return isFinite(n) ? n : d; }

  function applyQuestion(scope, style) {
    var s = style || {};
    var card = scope.querySelector(".quiz-question-card");
    if (!card) return;
    var title = card.querySelector("h2");
    var opts = card.querySelector(".quiz-options");
    card.style.padding = s.pd != null ? num(s.pd, 24) + "px" : "";
    card.style.transform = (s.ox || s.oy) ? "translate(" + num(s.ox, 0) + "px," + num(s.oy, 0) + "px)" : "";
    if (title) {
      title.style.fontSize = s.fs != null ? num(s.fs, 1.25) + "rem" : "";
      title.style.fontWeight = s.fw != null ? String(Math.round(num(s.fw, 600))) : "";
      title.style.lineHeight = s.lh != null ? String(num(s.lh, 1.4)) : "";
      title.style.textAlign = s.al || "";
      title.style.marginTop = s.mt != null ? num(s.mt, 0) + "px" : "";
      title.style.marginBottom = s.mb != null ? num(s.mb, 20) + "px" : "";
      title.style.color = s.col || "";
    }
    if (opts) {
      opts.style.gap = s.og != null ? num(s.og, 10) + "px" : "";
      Array.prototype.forEach.call(opts.querySelectorAll(".quiz-option"), function (o) {
        o.style.fontSize = s.ofs != null ? num(s.ofs, 1) + "rem" : "";
        o.style.paddingTop = o.style.paddingBottom = s.op != null ? num(s.op, 14) + "px" : "";
      });
    }
    // v246: chizma — o'lchami, joylashuvi va surilishi
    var fig = card.querySelector(".quiz-qfig");
    if (fig) {
      var inner = fig.firstElementChild;
      fig.style.textAlign = s.fal || "";
      fig.style.display = fig.hidden ? "none" : (s.fal ? "block" : "");
      if (inner) {
        inner.style.width = s.fsc != null ? Math.round(num(s.fsc, 100)) + "%" : "";
        inner.style.maxWidth = s.fsc != null && num(s.fsc, 100) > 100 ? "none" : "";
        inner.style.marginLeft = s.fal === "center" || s.fal === "right" ? "auto" : "";
        inner.style.marginRight = s.fal === "center" ? "auto" : "";
      }
      fig.style.transform = (s.fx || s.fy) ? "translate(" + num(s.fx, 0) + "px," + num(s.fy, 0) + "px)" : "";
    }
  }

  function applyLayout(scope, layout) {
    var l = layout || {};
    var header = scope.querySelector(".quiz-header");
    var timer = scope.querySelector(".quiz-timer");
    var main = scope.querySelector(".quiz-main");
    var nav = scope.querySelector(".quiz-nav-row");
    var track = scope.querySelector(".quiz-progress-track");
    var label = scope.querySelector(".quiz-progress-label");
    if (timer) {
      timer.style.display = l.timer === "hide" ? "none" : "";
      timer.style.fontSize = l.timerSize != null ? num(l.timerSize, 1) + "rem" : "";
    }
    if (header) {
      ["left", "center", "right"].forEach(function (p) { header.classList.remove("qs-timer-" + p); });
      if (l.timerPos && l.timerPos !== "right") header.classList.add("qs-timer-" + l.timerPos);
      header.classList.toggle("qs-header-min", l.header === "hide");
    }
    if (track) track.style.display = l.progress === "hide" ? "none" : "";
    if (label) label.style.display = l.progress === "hide" ? "none" : "";
    if (main) main.style.setProperty("--qs-card-w", l.cardW != null ? num(l.cardW, 720) + "px" : "720px");
    if (nav) nav.style.justifyContent = l.nav === "center" ? "center" : l.nav === "right" ? "flex-end" : "";
  }

  global.LZQuizStyle = { applyQuestion: applyQuestion, applyLayout: applyLayout };
})(window);
