(function () {
  "use strict";
  var A = document.body.dataset.admin || "";
  function post(url, body) {
    return fetch(url, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body || {}) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (d) { if (!r.ok) throw new Error(d.detail || "Xatolik"); return d; }); });
  }
  function collectFix(card) {
    var d = card.querySelector(".rp-fix");
    if (!d) return null;
    var radio = d.querySelector("input[type=radio]:checked");
    return {
      question: d.querySelector(".rp-fix-q").value,
      options: Array.prototype.map.call(d.querySelectorAll(".rp-fix-o"), function (i) { return i.value; }),
      correct_index: radio ? parseInt(radio.value, 10) : 0,
      explanation: d.querySelector(".rp-fix-e").value
    };
  }
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("button[data-act]");
    if (!btn) return;
    var card = btn.closest(".rp-card"), id = card.dataset.id, act = btn.dataset.act;
    if (act === "hide" && !confirm("Savol testlardan yashirilsinmi?")) return;
    if (act === "dismiss" && !confirm("Shikoyat rad etilsinmi?")) return;
    var url = A + "/api/reports/" + id + "/" + act, body = {};
    if (act === "apply") body = { fix: collectFix(card) };
    btn.disabled = true; var old = btn.textContent; if (act === "analyze") btn.textContent = "Tahlil qilinmoqda...";
    post(url, body).then(function () { LZToast.ok("Bajarildi"); setTimeout(function () { location.reload(); }, 500); })
      .catch(function (err) { LZToast.err(err.message); btn.disabled = false; btn.textContent = old; });
  });
  var save = document.getElementById("rp-save"), batch = document.getElementById("rp-batch");
  function cfg() { return { mode: document.getElementById("rp-mode").value, threshold: +document.getElementById("rp-threshold").value || 90, hide_after: +document.getElementById("rp-hide").value || 0 }; }
  if (save) save.addEventListener("click", function () {
    post(A + "/api/reports/settings", cfg()).then(function () { LZToast.ok("Saqlandi"); }).catch(function (x) { LZToast.err(x.message); });
  });
  if (batch) batch.addEventListener("click", function () {
    batch.disabled = true; batch.textContent = "Tahlil qilinmoqda...";
    post(A + "/api/reports/settings", cfg()).then(function () { return post(A + "/api/reports/analyze-batch"); })
      .then(function (d) {
        LZToast.ok("Tahlil: " + d.analyzed + " ta, avto-tuzatildi: " + d.auto_fixed + (d.left ? " · qoldi: " + d.left : ""));
        setTimeout(function () { location.reload(); }, 900);
      }).catch(function (x) { LZToast.err(x.message); batch.disabled = false; batch.textContent = "Yangilarini tahlil qil"; });
  });
})();
