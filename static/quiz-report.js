// LongoUZ — test paytida "Shikoyat qilish": o'ng tarafdan ochiladigan oyna.
// Joriy savol serverda attempt_token + indeks bo'yicha topiladi (to'g'ri javob brauzerga chiqmaydi).
(function () {
  "use strict";
  var $ = function (id) { return document.getElementById(id); };
  var openBtn = $("qr-open"), panel = $("qr-panel"), back = $("qr-backdrop"), send = $("qr-send");
  if (!openBtn || !panel) return;
  var details = $("qr-details"), msg = $("qr-msg"), sending = false;

  function setMsg(t, err) { msg.textContent = t || ""; msg.className = "qr-msg" + (err ? " err" : t ? " ok" : ""); }
  function open() {
    var st = window.LZQuizState; if (!st || !st.ready()) return;
    var q = st.question();
    $("qr-qno").textContent = (st.index() + 1) + " / " + st.total() + "-savol";
    var t = (q && q.question) || ""; $("qr-qtext").textContent = t.length > 260 ? t.slice(0, 260) + "…" : t;
    setMsg(""); send.disabled = false;
    back.hidden = false; panel.hidden = false;
    requestAnimationFrame(function () { panel.classList.add("open"); back.classList.add("open"); });
    setTimeout(function () { details.focus(); }, 250);
  }
  function close() {
    panel.classList.remove("open"); back.classList.remove("open");
    setTimeout(function () { panel.hidden = true; back.hidden = true; }, 220);
  }
  openBtn.addEventListener("click", open);
  $("qr-close").addEventListener("click", close);
  $("qr-cancel").addEventListener("click", close);
  back.addEventListener("click", close);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) close(); });
  details.addEventListener("input", function () { $("qr-n").textContent = details.value.length; });

  send.addEventListener("click", function () {
    if (sending) return;
    var st = window.LZQuizState; if (!st || !st.ready()) { setMsg("Test yakunlangan.", true); return; }
    var cat = (document.querySelector('input[name="qr-cat"]:checked') || {}).value || "other";
    var text = details.value.trim();
    if (cat === "other" && text.length < 5) { setMsg("Iltimos, kamchilikni qisqacha yozing.", true); details.focus(); return; }
    sending = true; send.disabled = true; setMsg("Yuborilmoqda...");
    fetch("/api/question-report", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ attempt_token: st.token, index: st.index(), category: cat, details: text }),
    }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) { if (!r.ok) throw new Error(d.detail || "Yuborib bo'lmadi."); return d; }); })
      .then(function (d) {
        setMsg(d.message || "Yuborildi.");
        details.value = ""; $("qr-n").textContent = "0";
        setTimeout(close, 1400);
      })
      .catch(function (e) { setMsg(e.message, true); send.disabled = false; })
      .then(function () { sending = false; });
  });

  document.addEventListener("lz-quiz-ready", function () { openBtn.hidden = false; });
  document.addEventListener("lz-quiz-finished", function () { openBtn.hidden = true; if (!panel.hidden) close(); });
})();
