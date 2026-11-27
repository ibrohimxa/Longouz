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

/* v267: profil rasmi va shaxsiy ko'rinish */
(function () {
  "use strict";
  function post(url, data) {
    return fetch(url, { method: "POST", headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" }, body: JSON.stringify(data) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, data: j }; }); });
  }
  function say(text, err) {
    var m = document.getElementById("pf-msg-style") || document.getElementById("pf-msg-profile"); if (!m) return;
    m.textContent = text; m.classList.toggle("is-err", !!err); if (!err) setTimeout(function () { m.textContent = ""; }, 2500);
  }
  function sayP(text, err) { var m = document.getElementById("pf-msg-profile"); if (!m) return; m.textContent = text; m.classList.toggle("is-err", !!err); }
  function setAvatars(src) {
    document.querySelectorAll("#pf-avatar, #pf-hero-avatar, .app-header-avatar").forEach(function (el) {
      if (src) { el.innerHTML = '<img src="' + src + '" alt="">'; el.classList.add("has-img"); el.style.background = ""; }
      else { location.reload(); }
    });
  }

  /* rasm: markazdan kvadrat qilib kesib, 256×256 JPEG ga kichraytiramiz */
  var input = document.getElementById("pf-photo-input"), del = document.getElementById("pf-photo-del");
  if (input) input.addEventListener("change", function () {
    var f = input.files && input.files[0]; if (!f) return;
    if (!/^image\//.test(f.type)) { sayP("Rasm formati JPG, PNG, WebP yoki GIF bo'lsin.", true); return; }
    if (f.size > 12 * 1024 * 1024) { sayP("Rasm juda katta (12 MB dan kichik bo'lsin).", true); return; }
    var img = new Image(), fr = new FileReader();   /* CSP: blob: emas, data: ruxsat etilgan */
    img.onload = function () {
      var s = Math.min(img.naturalWidth, img.naturalHeight), sx = (img.naturalWidth - s) / 2, sy = (img.naturalHeight - s) / 2;
      var c = document.createElement("canvas"); c.width = c.height = 256;
      var g = c.getContext("2d"); g.imageSmoothingQuality = "high"; g.drawImage(img, sx, sy, s, s, 0, 0, 256, 256);
      var data = c.toDataURL("image/jpeg", 0.86);
      if (data.length > 150000) data = c.toDataURL("image/jpeg", 0.7);
      sayP("Yuklanmoqda…");
      post("/api/profile/avatar", { image: data }).then(function (r) {
        if (r.ok) { setAvatars(data); sayP("Rasm saqlandi"); if (del) del.hidden = false; }
        else sayP((r.data && r.data.detail) || "Xato", true);
        input.value = "";
      });
    };
    img.onerror = function () { sayP("Rasmni o'qib bo'lmadi.", true); };
    fr.onload = function () { img.src = fr.result; };
    fr.readAsDataURL(f);
  });
  if (del) del.addEventListener("click", function () {
    post("/api/profile/avatar", { image: "" }).then(function (r) { if (r.ok) location.reload(); else sayP("Xato", true); });
  });

  /* sozlamalar */
  var styleTag = document.getElementById("lz-user-style");
  function applyCss(css) {
    if (!styleTag) { styleTag = document.createElement("style"); styleTag.id = "lz-user-style"; document.head.appendChild(styleTag); }
    styleTag.textContent = css || "";
  }
  function save(data, after) {
    post("/api/profile/prefs", data).then(function (r) {
      if (r.ok) { applyCss(r.data.css); say("Saqlandi"); if (after) after(r.data.prefs); }
      else say((r.data && r.data.detail) || "Xato", true);
    });
  }
  document.querySelectorAll("#pf-style [data-pref][data-val]").forEach(function (b) {
    b.addEventListener("click", function () {
      if (b.classList.contains("is-locked")) { location.href = "/plans?plan=" + (b.getAttribute("data-need") || "pro"); return; }
      var key = b.getAttribute("data-pref"), val = b.getAttribute("data-val"), d = {}; d[key] = val;
      save(d, function () {
        document.querySelectorAll('#pf-style [data-pref="' + key + '"]').forEach(function (x) { x.classList.toggle("is-on", x === b); });
        if (key === "frame") {
          document.querySelectorAll("#pf-avatar, #pf-hero-avatar, .app-header-avatar").forEach(function (el) {
            el.className = el.className.replace(/\blz-frame-\w+/g, "").trim() + " lz-frame-" + val;
          });
        }
        if (key === "banner" || key === "badge") setTimeout(function () { location.reload(); }, 350);
      });
    });
  });
  document.querySelectorAll("#pf-style input[type=checkbox][data-pref]").forEach(function (cb) {
    cb.addEventListener("change", function () {
      var key = cb.getAttribute("data-pref"), d = {};
      d[key] = cb.hasAttribute("data-on") ? (cb.checked ? cb.getAttribute("data-on") : cb.getAttribute("data-off")) : cb.checked;
      save(d, function () { if (key === "glow") location.reload(); });
    });
  });
  var bf = document.getElementById("pf-bio-form");
  if (bf) bf.addEventListener("submit", function (e) {
    e.preventDefault();
    save({ bio: bf.bio.value.trim() }, function () { setTimeout(function () { location.reload(); }, 300); });
  });
})();
