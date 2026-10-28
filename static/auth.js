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
