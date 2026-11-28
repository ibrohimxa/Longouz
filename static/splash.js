/* LongoUZ — ochilish ekrani (0→100%, to'lqin bilan to'ladi).
   v270: butun animatsiya CSS (kompozitor)da ishlaydi — JS band bo'lsa ham to'xtab qolmaydi
   va 3 soniyadan keyin ekran albatta yo'qoladi. */
(function () {
  try { if (sessionStorage.getItem("lz_splash_done") === "1") return; } catch (e) {}
  var root = document.documentElement;
  var T = 2600; /* to'lish vaqti, ms */
  var css = ""
    + "#lz-splash{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;background:#041208;overflow:hidden;font-family:Inter,system-ui,sans-serif;"
    + "animation:sp-out .4s ease " + (T + 150) + "ms forwards}"
    + "@keyframes sp-out{to{opacity:0;visibility:hidden;pointer-events:none}}"
    + "#lz-splash.is-out{opacity:0;visibility:hidden;pointer-events:none;transition:opacity .35s ease,visibility .35s}"
    + "#lz-splash .sp-fill{position:absolute;left:0;right:0;bottom:0;height:calc(100% + 26px);transform:translateY(100%);will-change:transform;"
    + "background:linear-gradient(180deg,#27d968 0,#14a84a 45%,#0d7c37 100%);box-shadow:0 -10px 30px rgba(61,255,126,.45);"
    + "animation:sp-rise " + T + "ms cubic-bezier(.45,0,.55,1) forwards}"
    + "@keyframes sp-rise{to{transform:translateY(0)}}"
    + "#lz-splash .sp-wave{position:absolute;left:0;top:-22px;width:200%;height:24px;will-change:transform;"
    + "background:radial-gradient(60% 100% at 50% 100%,#3dff7e 0,#27d968 60%,transparent 62%) 0 0/60px 24px repeat-x;animation:sp-wave 1.4s linear infinite}"
    + "@keyframes sp-wave{to{transform:translateX(-60px)}}"
    + "#lz-splash .sp-box{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;text-align:center}"
    + "#lz-splash .sp-logo{position:relative;width:148px;height:148px;display:grid;place-items:center}"
    + "#lz-splash .sp-logo img{width:96px;height:auto}"
    + "#lz-splash .sp-logo svg{position:absolute;inset:0;width:100%;height:100%;transform:rotate(-90deg)}"
    + "#lz-splash .sp-track{fill:none;stroke:rgba(255,255,255,.18);stroke-width:4}"
    + "#lz-splash .sp-arc{fill:none;stroke:#b6ffcc;stroke-width:4;stroke-linecap:round;animation:sp-arc " + T + "ms linear forwards}"
    + "#lz-splash .sp-spin{fill:none;stroke:#3dff7e;stroke-width:2.5;stroke-linecap:round;stroke-dasharray:46 380}"
    + "#lz-splash .sp-rot{position:absolute;inset:0;animation:sp-rot 1.1s linear infinite;will-change:transform}"
    + "@keyframes sp-rot{to{transform:rotate(360deg)}}"
    + "#lz-splash .sp-name{margin:18px 0 0;font-weight:800;font-size:2.1rem;letter-spacing:-.02em;color:#fff}"
    + "#lz-splash .sp-name b{color:#3dff7e}"
    + "#lz-splash .sp-bar{margin-top:22px;width:min(240px,64vw);height:6px;border-radius:99px;background:rgba(255,255,255,.2);overflow:hidden}"
    + "#lz-splash .sp-bar i{display:block;height:100%;width:100%;border-radius:99px;background:linear-gradient(90deg,#3dff7e,#e9fff0);transform:scaleX(0);transform-origin:0 50%;will-change:transform;animation:sp-bar " + T + "ms linear forwards}"
    + "@keyframes sp-bar{to{transform:scaleX(1)}}"
    + "#lz-splash .sp-pct{margin-top:10px;font-weight:700;font-size:1.05rem;letter-spacing:.04em;color:#e9fff0;font-variant-numeric:tabular-nums}"
    + "@media (prefers-reduced-motion:reduce){#lz-splash .sp-wave,#lz-splash .sp-rot{animation:none}}"
    + "html.lz-splashing,html.lz-splashing body{overflow:hidden!important}";
  var st = document.createElement("style"); st.id = "lz-splash-css"; st.textContent = css; root.appendChild(st);
  var R = 70, C = (2 * Math.PI * R).toFixed(1);
  st.textContent += "@keyframes sp-arc{from{stroke-dashoffset:" + C + "}to{stroke-dashoffset:0}}";
  var el = document.createElement("div"); el.id = "lz-splash"; el.setAttribute("role", "status"); el.setAttribute("aria-label", "LongoUZ yuklanmoqda");
  el.innerHTML = '<div class="sp-fill"><div class="sp-wave"></div></div><div class="sp-box"><div class="sp-logo">'
    + '<svg viewBox="0 0 148 148" aria-hidden="true"><circle class="sp-track" cx="74" cy="74" r="' + R + '"/>'
    + '<circle class="sp-arc" cx="74" cy="74" r="' + R + '" stroke-dasharray="' + C + '" stroke-dashoffset="' + C + '"/></svg>'
    + '<svg class="sp-rot" viewBox="0 0 148 148" aria-hidden="true"><circle class="sp-spin" cx="74" cy="74" r="' + R + '"/></svg>'
    + '<img src="/static/logo-owl3d-sm.png" alt="" width="96" height="73"></div>'
    + '<p class="sp-name">Longo<b>UZ</b></p><div class="sp-bar"><i></i></div><div class="sp-pct">0%</div></div>';
  root.appendChild(el); root.classList.add("lz-splashing");
  var pct = el.querySelector(".sp-pct"), t0 = Date.now(), finished = false;

  function done() {
    if (finished) return; finished = true;
    try { sessionStorage.setItem("lz_splash_done", "1"); } catch (e) {}
    pct.textContent = "100%";
    el.classList.add("is-out"); root.classList.remove("lz-splashing");
    setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); if (st.parentNode) st.parentNode.removeChild(st); }, 450);
  }
  /* faqat foiz raqami JS bilan — qolgan hammasi CSS'da */
  var iv = setInterval(function () {
    var p = Math.min(1, (Date.now() - t0) / T);
    pct.textContent = Math.round(p * 100) + "%";
    if (p >= 1) { clearInterval(iv); setTimeout(done, 150); }
  }, 50);
  /* himoyalar: vaqt o'tgan bo'lsa (fon/uyqu, sekin telefon) — darhol yopiladi; bosilsa ham yopiladi */
  setTimeout(done, T + 900);
  function late() { if (Date.now() - t0 > T) done(); }
  window.addEventListener("load", function () { setTimeout(late, 200); });
  window.addEventListener("pageshow", late);
  document.addEventListener("visibilitychange", function () { if (!document.hidden) late(); });
  el.addEventListener("pointerdown", done);
})();
