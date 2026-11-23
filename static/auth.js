/* Kirish / ro'yxatdan o'tish: parol ko'rsatish, bir marta yuborish, xatoni ko'rsatish */
(function () {
  "use strict";
  document.querySelectorAll(".au-eye").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var input = document.getElementById(btn.getAttribute("data-target"));
      if (!input) return;
      var show = input.type === "password";
      input.type = show ? "text" : "password";
      btn.classList.toggle("is-on", show);
      btn.setAttribute("aria-label", show ? "Parolni yashirish" : "Parolni ko'rsatish");
    });
  });
  var form = document.getElementById("auth-form");
  if (!form) return;
  var p1 = document.getElementById("password"), p2 = document.getElementById("password_confirm");
  form.addEventListener("submit", function (e) {
    if (p1 && p2 && p1.value !== p2.value) {
      e.preventDefault(); e.stopImmediatePropagation();
      p2.setCustomValidity("Parollar bir xil emas");
      p2.reportValidity();
      p2.addEventListener("input", function () { p2.setCustomValidity(""); }, { once: true });
    }
  }, true);
  form.addEventListener("submit", function (e) {
    if (e.defaultPrevented) return;
    var b = form.querySelector(".au-submit");
    if (b) { b.classList.add("is-busy"); setTimeout(function () { b.disabled = true; }, 0); }
  });
})();

/* v231: email tekshiruvi — xato yozilgan domen (gmial.com), bunday hisob bor-yo'qligi. */
(function () {
  "use strict";
  var input = document.getElementById("email"), hint = document.getElementById("email-hint");
  if (!input || !hint) return;
  var isLogin = (document.getElementById("auth-form") || {}).getAttribute && document.getElementById("auth-form").getAttribute("action") === "/login";
  var timer = null, last = "";
  function show(html, kind) { hint.innerHTML = html; hint.className = "au-email-hint is-" + kind; hint.hidden = false; }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function check() {
    var v = (input.value || "").trim().toLowerCase();
    if (v === last) return; last = v;
    if (!v || v.indexOf("@") < 1) { hint.hidden = true; return; }
    fetch("/api/auth/email-check?email=" + encodeURIComponent(v), { credentials: "same-origin" })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        if (!d || (input.value || "").trim().toLowerCase() !== v) return;
        if (!d.valid) { show("Email to'liq emas — masalan: <b>ism@gmail.com</b>", "warn"); return; }
        if (d.suggest) {
          show('<b>' + esc(d.suggest) + '</b> ni nazarda tutdingizmi? <button type="button" class="au-hint-fix">Ha, tuzatish</button>', "warn");
          hint.querySelector(".au-hint-fix").onclick = function () { input.value = d.suggest; last = ""; check(); };
          return;
        }
        if (d.exists === null) { hint.hidden = true; return; }
        if (isLogin) {
          if (d.exists) show("✓ Hisob topildi — parolingizni kiriting.", "ok");
          else show('Bu email bilan hisob yo\'q. <a href="/register?email=' + encodeURIComponent(v) + '">Ro\'yxatdan o\'tish →</a>', "warn");
        } else {
          if (d.exists) show('Bu email bilan hisob allaqachon bor. Parolingizni kiritsangiz avtomatik kirasiz yoki <a href="/login?email=' + encodeURIComponent(v) + '">Kirish →</a>', "warn");
          else show("✓ Email bo'sh — yangi hisob ochiladi.", "ok");
        }
      }).catch(function () {});
  }
  input.addEventListener("blur", check);
  input.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(check, 700); });
  if (input.value) setTimeout(check, 300);
})();
