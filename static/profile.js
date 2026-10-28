(function () {
  "use strict";
  function post(url, data) {
    return fetch(url, { method: "POST", headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, data: j }; }); });
  }
  function say(id, text, err) { var m = document.getElementById(id); if (!m) return; m.textContent = text; m.classList.toggle("is-err", !!err); if (!err) setTimeout(function () { m.textContent = ""; }, 3000); }
  function detail(res, fallback) { var d = res.data && res.data.detail; return typeof d === "string" ? d : fallback; }

  var pickedColor = null;
  document.querySelectorAll(".pf-color").forEach(function (b) {
    b.addEventListener("click", function () {
      pickedColor = b.getAttribute("data-color");
      document.querySelectorAll(".pf-color").forEach(function (x) { x.classList.toggle("is-on", x === b); x.setAttribute("aria-checked", String(x === b)); });
      document.getElementById("pf-avatar").style.background = pickedColor;
      post("/api/profile/update", { avatar_color: pickedColor }).then(function (r) { say("pf-msg-profile", r.ok ? "Rang saqlandi" : detail(r, "Xato"), !r.ok); });
    });
  });

  var fp = document.getElementById("pf-form-profile");
  if (fp) fp.addEventListener("submit", function (e) {
    e.preventDefault();
    post("/api/profile/update", { first_name: fp.first_name.value.trim() }).then(function (r) {
      say("pf-msg-profile", r.ok ? "Saqlandi" : detail(r, "Xato"), !r.ok);
      if (r.ok) setTimeout(function () { location.reload(); }, 600);
    });
  });

  var fg = document.getElementById("pf-form-goals");
  if (fg) {
    var gv = document.getElementById("pf-goal-val"), tv = document.getElementById("pf-target-val");
    fg.daily_goal.addEventListener("input", function () { gv.textContent = fg.daily_goal.value; });
    fg.target_percent.addEventListener("input", function () { tv.textContent = fg.target_percent.value; });
    fg.addEventListener("submit", function (e) {
      e.preventDefault();
      post("/api/profile/update", { daily_goal: +fg.daily_goal.value, target_percent: +fg.target_percent.value })
        .then(function (r) { say("pf-msg-goals", r.ok ? "Saqlandi" : detail(r, "Xato"), !r.ok); });
    });
  }

  var fw = document.getElementById("pf-form-pass");
  if (fw) fw.addEventListener("submit", function (e) {
    e.preventDefault();
    if (fw.new_password.value !== fw.repeat.value) { say("pf-msg-pass", "Yangi parollar bir xil emas", true); return; }
    post("/api/profile/password", { current_password: fw.current_password.value, new_password: fw.new_password.value }).then(function (r) {
      say("pf-msg-pass", r.ok ? "Parol almashtirildi" : detail(r, "Parol noto'g'ri yoki juda qisqa"), !r.ok);
      if (r.ok) fw.reset();
    });
  });

  var fd = document.getElementById("pf-form-delete");
  if (fd) fd.addEventListener("submit", function (e) {
    e.preventDefault();
    post("/api/profile/delete", { password: fd.password.value, confirm: fd.confirm.value.trim() }).then(function (r) {
      if (r.ok) { location.href = "/"; } else { say("pf-msg-danger", detail(r, "Xato"), true); }
    });
  });

  document.querySelectorAll("[data-set-theme]").forEach(function (b) {
    b.addEventListener("click", function () {
      var th = b.getAttribute("data-set-theme");
      document.documentElement.setAttribute("data-theme", th);
      try { localStorage.setItem("longouz_theme", th); } catch (e) { /* ixtiyoriy */ }
    });
  });
})();
