// "Saqlandi" bildirishnomasi (yashil galochka) — admin sahifalarida umumiy.
(function (global) {
  "use strict";
  var el, timer;
  function ensure() {
    if (el) return el;
    el = document.createElement("div"); el.className = "saved-toast"; el.setAttribute("role", "status"); el.setAttribute("aria-live", "polite");
    el.innerHTML = '<span class="tick"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="msg"></span>';
    document.body.appendChild(el); return el;
  }
  function show(msg, err, ms) {
    var t = ensure(); t.classList.remove("show"); void t.offsetWidth;
    t.classList.toggle("err", !!err);
    t.querySelector(".tick").innerHTML = err ? '<svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" stroke-linecap="round"/></svg>' : '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    t.querySelector(".msg").textContent = msg; t.classList.add("show");
    clearTimeout(timer); timer = setTimeout(function () { t.classList.remove("show"); }, ms || (err ? 6000 : 3200));
  }
  global.LZToast = { ok: function (m, ms) { show(m, false, ms); }, err: function (m, ms) { show(m, true, ms); } };
})(window);
