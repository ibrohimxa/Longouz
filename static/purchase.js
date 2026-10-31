/* Tarif sotib olish oynasi: ochish/yopish va karta vizualini jonlantirish.
   Ma'lumotlar hech qayerga yuborilmaydi (karta maydonlarida name yo'q). */
(function () {
  "use strict";
  var overlay = document.getElementById("pm-overlay");
  if (!overlay) return;
  var $ = function (id) { return document.getElementById(id); };
  var planInput = $("pm-plan-input");

  function setText(id, v) { var el = $(id); if (el) el.textContent = v; }

  function open(plan, name, price) {
    planInput.value = plan;
    var g = $("pm-google");
    if (g) g.setAttribute("href", "/auth/google/login?next=" + encodeURIComponent("/upgrade?plan=" + plan + "&auto=1"));
    setText("pm-plan-name", name);
    setText("pm-plan-price", price);
    overlay.hidden = false;
    document.body.style.overflow = "hidden"; document.body.classList.add("pm-open");
    if (window.lgTurnstileRender) window.lgTurnstileRender();
    setTimeout(function () { var f = overlay.querySelector("input:not([type=hidden])"); if (f && window.innerWidth > 860) f.focus({ preventScroll: true }); }, 60);
  }
  function close() { overlay.hidden = true; document.body.style.overflow = ""; document.body.classList.remove("pm-open"); }

  window.pmOpen = function (btn) {
    open(btn.dataset.plan, btn.dataset.planName, btn.dataset.activePrice || btn.dataset.monthlyPrice);
  };
  document.querySelectorAll(".checkout-open-btn").forEach(function (b) {
    b.addEventListener("click", function () { window.pmOpen(b); });
  });
  $("pm-close").addEventListener("click", close);
  overlay.addEventListener("mousedown", function (e) { if (e.target === overlay) close(); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !overlay.hidden) close(); });

  var num = $("pm-cnum"), nm = $("pm-name"), exp = $("pm-cexp"), cvv = $("pm-ccvv");
  var face = $("pm-card-face");

  function detect(d) {
    if (d.indexOf("8600") === 0) return ["uzcard", "UzCard"];
    if (d.indexOf("9860") === 0) return ["humo", "HUMO"];
    if (d.charAt(0) === "4") return ["visa", "VISA"];
    if (/^5[1-5]/.test(d) || /^2(22[1-9]|2[3-9]\d|[3-6]\d\d|7[01]\d|720)/.test(d)) return ["mastercard", "Mastercard"];
    return null;
  }
  function drawNumber(d) {
    var box = $("pm-card-num"), pad = (d + "################").slice(0, 16), html = "";
    for (var i = 0; i < 4; i++) {
      var g = pad.substr(i * 4, 4).replace(/#/g, "•");
      html += "<i>" + g + "</i>";
    }
    box.innerHTML = html;
  }
  num.addEventListener("input", function () {
    var d = num.value.replace(/\D/g, "").slice(0, 16);
    num.value = d.replace(/(.{4})/g, "$1 ").trim();
    drawNumber(d);
    var t = detect(d);
    if (t) { face.dataset.cardType = t[0]; setText("pm-card-brand", t[1]); }
  });
  nm.addEventListener("input", function () { setText("pm-card-name", nm.value.trim() ? nm.value.toUpperCase() : "TO'LIQ ISM"); });
  if (nm.value.trim()) setText("pm-card-name", nm.value.toUpperCase());
  exp.addEventListener("input", function () {
    var d = exp.value.replace(/\D/g, "").slice(0, 4);
    if (d.length >= 3) d = d.slice(0, 2) + "/" + d.slice(2);
    exp.value = d;
    setText("pm-card-exp", d || "00/YY");
  });
  cvv.addEventListener("input", function () { cvv.value = cvv.value.replace(/\D/g, "").slice(0, 3); });

  var form = $("pm-form");
  form.addEventListener("submit", function (e) {
    var p1 = $("pm-pass"), p2 = $("pm-pass2");
    if (p1 && p2 && p1.value !== p2.value) {
      e.preventDefault(); e.stopImmediatePropagation();
      p2.setCustomValidity("Parollar bir xil emas"); p2.reportValidity();
      p2.addEventListener("input", function () { p2.setCustomValidity(""); }, { once: true });
    }
  }, true);
})();

/* v231: tarif oynasida email — hisob bor bo'lsa ogohlantiramiz (parol to'g'ri bo'lsa shu hisobga tarif qo'shiladi). */
(function () {
  var inp = document.getElementById("pm-email"), hint = document.getElementById("pm-email-hint");
  if (!inp || !hint) return;
  var last = "", t = null;
  function check() {
    var v = (inp.value || "").trim().toLowerCase();
    if (v === last) return; last = v;
    if (v.indexOf("@") < 1) { hint.hidden = true; return; }
    fetch("/api/auth/email-check?email=" + encodeURIComponent(v)).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d || !d.valid) { hint.hidden = !d; if (d) { hint.textContent = "Email to'liq emas (masalan: ism@gmail.com)"; hint.style.color = "#f5b84a"; } return; }
      if (d.suggest) { hint.textContent = d.suggest + " ni nazarda tutdingizmi?"; hint.style.color = "#f5b84a"; hint.hidden = false; return; }
      if (d.exists) { hint.textContent = "Bu email bilan hisob bor — o'sha hisob parolini kiriting, tarif shu hisobga qo'shiladi."; hint.style.color = "#f5b84a"; hint.hidden = false; }
      else if (d.exists === false) { hint.textContent = "✓ Yangi hisob ochiladi"; hint.style.color = "#2fd39b"; hint.hidden = false; }
    }).catch(function () {});
  }
  inp.addEventListener("blur", check);
  inp.addEventListener("input", function () { clearTimeout(t); t = setTimeout(check, 700); });
})();
