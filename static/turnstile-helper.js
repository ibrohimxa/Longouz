/* Cloudflare Turnstile — chidamli (explicit) render.
   - Vidjet yashirin oynada (karta/checkout) bo'lsa ham, oyna ochilganda chiziladi.
   - api.js kech yuklansa/bloklansa: har 400ms urinadi; 15s ichida token chiqmasa "Qayta urinish" tugmasi.
   - Vidjet xato bersa (domen ruxsatsiz, tarmoq, kengaytma bloklagan): forma "cf-unavailable=1" bilan
     yuboriladi, server foydalanuvchini bloklamaydi (rate-limit ostida). */
(function () {
  "use strict";
  var widgets = new WeakMap();
  var TIMEOUT_MS = 15000;

  function ensureFlag(form) {
    var f = form.querySelector('input[name="cf-unavailable"]');
    if (!f) { f = document.createElement("input"); f.type = "hidden"; f.name = "cf-unavailable"; f.value = ""; form.appendChild(f); }
    return f;
  }
  function setStatus(form, msg, retry) {
    var st = form && form.querySelector("[data-turnstile-status]");
    if (!st) return;
    st.textContent = msg || "";
    var old = st.parentNode.querySelector(".au-cf-retry");
    if (old) old.remove();
    if (retry) {
      var b = document.createElement("button");
      b.type = "button"; b.className = "au-cf-retry"; b.textContent = "Qayta urinish";
      b.onclick = function () { resetSlot(retry); };
      st.parentNode.appendChild(b);
    }
  }
  function resetSlot(slot) {
    var form = slot.closest("form");
    var id = widgets.get(slot);
    if (form) { ensureFlag(form).value = ""; setStatus(form, ""); }
    try { if (id !== undefined) window.turnstile.reset(id); } catch (e) {}
    arm(slot);
  }
  function arm(slot) {
    clearTimeout(slot._cfTimer);
    slot._cfTimer = setTimeout(function () {
      var form = slot.closest("form");
      var inp = form && form.querySelector('input[name="cf-turnstile-response"]');
      if (form && (!inp || !inp.value)) {
        ensureFlag(form).value = "1";
        setStatus(form, "Tekshiruv uzoq davom etdi. Davom etishingiz mumkin yoki qayta urinib ko'ring.", slot);
      }
    }, TIMEOUT_MS);
  }

  function renderSlot(slot) {
    if (!window.turnstile || widgets.has(slot)) return;
    var form = slot.closest("form");
    if (form) ensureFlag(form);
    if (!slot.style.minHeight) slot.style.minHeight = "65px";
    try {
      var id = window.turnstile.render(slot, {
        sitekey: slot.getAttribute("data-sitekey"),
        theme: "auto",
        size: "flexible",
        appearance: "always",
        retry: "auto",
        "retry-interval": 4000,
        "refresh-expired": "auto",
        callback: function () {
          clearTimeout(slot._cfTimer);
          if (form) { ensureFlag(form).value = ""; setStatus(form, ""); }
        },
        "expired-callback": function () { try { window.turnstile.reset(id); } catch (e) {} arm(slot); },
        "timeout-callback": function () { try { window.turnstile.reset(id); } catch (e) {} },
        "error-callback": function () {
          if (form) {
            ensureFlag(form).value = "1";
            setStatus(form, "Tekshiruv vidjeti yuklanmadi. Davom etishingiz mumkin yoki qayta urinib ko'ring.", slot);
          }
          return true;
        },
      });
      widgets.set(slot, id);
      arm(slot);
    } catch (e) { /* keyingi urinishda */ }
  }

  function renderAll() { document.querySelectorAll(".turnstile-slot").forEach(renderSlot); }
  window.lgTurnstileReady = renderAll;
  window.lgTurnstileRender = renderAll;

  // api.js hali yuklanmagan bo'lsa ham, yuklanishi bilan chizish (onload kechiksa/ishlamasa)
  var tries = 0;
  var poll = setInterval(function () {
    renderAll();
    if (++tries > 75) clearInterval(poll);
  }, 400);

  document.addEventListener("submit", function (e) {
    var form = e.target;
    var slot = form.querySelector && form.querySelector(".turnstile-slot");
    if (!slot) return;
    var input = form.querySelector('input[name="cf-turnstile-response"]');
    var flag = form.querySelector('input[name="cf-unavailable"]');
    if ((!input || !input.value) && !(flag && flag.value === "1")) {
      e.preventDefault();
      setStatus(form, "Iltimos, \"Men robot emasman\" tekshiruvini kuting (bir necha soniya).");
      renderAll();
    }
  }, true);

  var mo = new MutationObserver(renderAll);
  document.addEventListener("DOMContentLoaded", function () {
    mo.observe(document.body, { attributes: true, subtree: true, attributeFilter: ["hidden", "class", "style"] });
    renderAll();
  });
})();
