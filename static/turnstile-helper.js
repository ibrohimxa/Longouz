/* Cloudflare Turnstile — ishonchli yuklash va chizish (v217).
   - api.js ni o'zi yuklaydi (sahifada bo'lmasa), takroran yuklamaydi (ikki marta yuklash vidjetni "aylantirib" qo'yardi);
   - vidjet yashirin oynada (karta/checkout) bo'lsa ham, oyna ochilganda chiziladi;
   - "Tekshirilmoqda…" holati va aniq xato kodi ko'rsatiladi (110200 = domen Cloudflare'da qo'shilmagan);
   - 9 soniyada token kelmasa yoki xato chiqsa — ZAXIRA YO'L: forma baribir yuboriladi (server IP bo'yicha qattiq cheklov qo'llaydi),
     shunda foydalanuvchi hech qachon "aylanib" qolgan vidjet ortida qulflanib qolmaydi;
   - tekshiruv tugagach, kutib turgan yuborish avtomatik davom etadi. */
(function () {
  "use strict";
  var widgets = new WeakMap();
  var loadTries = 0;
  var FALLBACK_MS = 9000;
  var API = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=lgTurnstileReady";

  var ERR_TEXT = {
    "110200": "Bu domen Cloudflare Turnstile'da ruxsat etilmagan (admin: Cloudflare → Turnstile → Hostname ro'yxatiga shu domenni qo'shing).",
    "110100": "Turnstile site key noto'g'ri.", "110110": "Turnstile site key noto'g'ri.",
    "300030": "Brauzer tekshiruvdan o'tolmadi.", "600010": "Tekshiruv vaqti tugadi."
  };

  function isVisible(el) { return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length); }
  function statusOf(slot) { var f = slot.closest("form"); return f ? f.querySelector("[data-turnstile-status]") : null; }
  function say(slot, txt, ok) {
    var st = statusOf(slot); if (!st) return;
    st.textContent = txt || ""; st.style.color = ok ? "#10b981" : "";
  }
  function tokenOf(form) {
    var i = form.querySelector('input[name="cf-turnstile-response"]');
    return i && i.value ? i.value : "";
  }
  function fallbackInput(form) {
    var i = form.querySelector('input[name="cf-turnstile-fallback"]');
    if (!i) { i = document.createElement("input"); i.type = "hidden"; i.name = "cf-turnstile-fallback"; form.appendChild(i); }
    return i;
  }
  // v229: vidjet ishlamasa (masalan domen Cloudflare'da hali qo'shilmagan bo'lsa) foydalanuvchiga
  // qo'rqituvchi "Unable to connect" oynasi va admin uchun yozilgan matn KO'RSATILMAYDI — vidjet
  // butunlay yashiriladi, forma odatdagidek yuboriladi (server IP bo'yicha cheklovni qo'llaydi).
  // Sabab faqat brauzer konsolida yoziladi (admin uchun).
  function hideWidget(slot, why) {
    var box = slot.closest(".au-cf") || slot.parentNode;
    if (box) box.style.display = "none";
    var f = slot.closest("form");
    var note = f ? f.querySelector(".au-cfnote") : null;
    if (note) note.style.display = "none";
    if (why) { try { console.warn("[Turnstile] " + why); } catch (e) {} }
  }
  function enableFallback(slot, why) {
    var form = slot.closest("form"); if (!form || tokenOf(form)) return;
    if (fallbackInput(form).value === "1") return;
    fallbackInput(form).value = "1";
    say(slot, "");
    hideWidget(slot, why);
    if (form.__lgPending) { form.__lgPending = false; submitAgain(form); }
  }
  function submitAgain(form) {
    try { if (form.requestSubmit) form.requestSubmit(); else form.submit(); } catch (e) { form.submit(); }
  }

  function ensureApi() {
    if (window.turnstile) return;
    var existing = document.querySelector('script[src*="challenges.cloudflare.com/turnstile"]');
    if (existing) return;                                   // sahifaning o'z <script> i bor — ikkinchisini QO'SHMAYMIZ
    if (loadTries >= 3) return;
    loadTries++;
    var s = document.createElement("script");
    s.src = API; s.async = true;
    s.onerror = function () {
      if (s.parentNode) s.parentNode.removeChild(s);
      document.querySelectorAll(".turnstile-slot").forEach(function (sl) {
        say(sl, loadTries >= 3 ? "Cloudflare tekshiruvi yuklanmadi (tarmoq yoki reklama-bloker)." : "Tekshiruv yuklanmoqda…");
        if (loadTries >= 3) enableFallback(sl);
      });
      setTimeout(ensureApi, 1500 * loadTries);
    };
    document.head.appendChild(s);
  }

  function renderSlot(slot) {
    if (widgets.has(slot) || !isVisible(slot)) return;
    if (!window.turnstile || !window.turnstile.render) { say(slot, "Tekshiruv yuklanmoqda…"); ensureApi(); armTimer(slot); return; }
    var id;
    try {
      id = window.turnstile.render(slot, {
        sitekey: slot.getAttribute("data-sitekey"),
        theme: "auto",
        "refresh-expired": "auto",
        retry: "auto",
        "retry-interval": 4000,
        callback: function () {
          say(slot, "✓ Tekshiruv o'tdi", true); setTimeout(function () { say(slot, ""); }, 1800);
          var f = slot.closest("form"); if (f && f.__lgPending) { f.__lgPending = false; submitAgain(f); }
        },
        "expired-callback": function () { try { window.turnstile.reset(id); } catch (e) {} },
        "timeout-callback": function () { try { window.turnstile.reset(id); } catch (e) {} },
        "error-callback": function (code) {
          enableFallback(slot, ERR_TEXT[String(code)] || ("Tekshiruv vidjeti xato berdi" + (code ? " (" + code + ")" : "") + "."));
          return false;
        }
      });
      widgets.set(slot, id);
      say(slot, "Tekshirilmoqda…");
      armTimer(slot);
    } catch (e) { setTimeout(renderAll, 800); }
  }

  function armTimer(slot) {
    if (slot.__lgTimer) return;
    slot.__lgTimer = setTimeout(function () {
      var f = slot.closest("form");
      if (f && !tokenOf(f)) enableFallback(slot, "Cloudflare tekshiruvi javob bermadi.");
    }, FALLBACK_MS);
  }

  function renderAll() {
    var slots = document.querySelectorAll(".turnstile-slot");
    if (!slots.length) return;
    slots.forEach(renderSlot);
  }

  window.lgTurnstileFailed = function () {          // sahifadagi api.js yuklanmadi (bloker/tarmoq) — darhol zaxira yo'l
    document.querySelectorAll(".turnstile-slot").forEach(function (sl) { say(sl, "Cloudflare tekshiruvi yuklanmadi."); enableFallback(sl); });
  };
  window.lgTurnstileReady = renderAll;
  window.lgTurnstileRender = renderAll;

  document.addEventListener("submit", function (e) {
    var form = e.target;
    var slot = form.querySelector && form.querySelector(".turnstile-slot");
    if (!slot) return;
    if (tokenOf(form)) return;
    if (fallbackInput(form).value === "1") return;           // zaxira yo'l yoqilgan — yuboramiz
    e.preventDefault();
    form.__lgPending = true;                                 // token kelishi bilan o'zi yuboriladi
    say(slot, "Cloudflare tekshiruvi tugashini kutyapmiz (bir necha soniya)…");
    armTimer(slot);
    renderAll();
  }, true);

  function boot() {
    renderAll();
    var n = 0;
    var iv = setInterval(function () {
      n++; renderAll();
      var pending = Array.prototype.some.call(document.querySelectorAll(".turnstile-slot"), function (s) { return !widgets.has(s) && isVisible(s); });
      if (!pending || n > 40) clearInterval(iv);
    }, 750);
    if (document.body) new MutationObserver(renderAll).observe(document.body, { attributes: true, subtree: true, attributeFilter: ["hidden", "class", "style"] });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
