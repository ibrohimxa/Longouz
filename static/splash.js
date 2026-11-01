/* LongoUZ — ochilish ekrani (3 soniya, 0→100%) */
(function () {
  try { if (sessionStorage.getItem("lz_splash_done") === "1") return; } catch (e) {}
  var root = document.documentElement;
  var css = ""
    + "#lz-splash{position:fixed;inset:0;z-index:2147483000;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0;background:#041208;overflow:hidden;transition:opacity .45s ease,visibility .45s;font-family:Inter,system-ui,sans-serif}"
    + "#lz-splash.is-out{opacity:0;visibility:hidden}"
    + "#lz-splash .sp-fill{position:absolute;left:0;right:0;bottom:0;height:0;background:linear-gradient(180deg,#27d968 0%,#14a84a 55%,#0d7c37 100%);box-shadow:0 -14px 40px rgba(61,255,126,.45)}"
    + "#lz-splash .sp-fill::before{content:'';position:absolute;left:-10%;right:-10%;top:-18px;height:22px;background:radial-gradient(60% 100% at 50% 100%,#3dff7e 0,#27d968 60%,transparent 62%) 0 0/60px 22px repeat-x;animation:sp-wave 1.4s linear infinite}"
    + "@keyframes sp-wave{to{background-position:60px 0}}"
    + "#lz-splash .sp-box{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;text-align:center}"
    + "#lz-splash .sp-logo{position:relative;width:148px;height:148px;display:grid;place-items:center}"
    + "#lz-splash .sp-logo img{width:96px;height:auto;filter:drop-shadow(0 6px 18px rgba(0,0,0,.35))}"
    + "#lz-splash .sp-logo svg{position:absolute;inset:0;width:100%;height:100%;transform:rotate(-90deg)}"
    + "#lz-splash .sp-track{fill:none;stroke:rgba(255,255,255,.18);stroke-width:4}"
    + "#lz-splash .sp-arc{fill:none;stroke:#b6ffcc;stroke-width:4;stroke-linecap:round;filter:drop-shadow(0 0 6px rgba(120,255,170,.9))}"
    + "#lz-splash .sp-spin{fill:none;stroke:#3dff7e;stroke-width:2.5;stroke-linecap:round;stroke-dasharray:46 380;transform-origin:50% 50%;animation:sp-rot 1.1s linear infinite;opacity:.9}"
    + "@keyframes sp-rot{to{transform:rotate(360deg)}}"
    + "#lz-splash .sp-name{margin:18px 0 0;font-weight:800;font-size:2.1rem;letter-spacing:-.02em;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.35)}"
    + "#lz-splash .sp-name b{color:#b6ffcc}"
    + "#lz-splash .sp-bar{margin-top:22px;width:min(240px,64vw);height:6px;border-radius:99px;background:rgba(255,255,255,.2);overflow:hidden}"
    + "#lz-splash .sp-bar i{display:block;height:100%;width:0;border-radius:99px;background:linear-gradient(90deg,#3dff7e,#e9fff0);box-shadow:0 0 10px rgba(120,255,170,.9)}"
    + "#lz-splash .sp-pct{margin-top:10px;font-weight:700;font-size:1.05rem;letter-spacing:.04em;color:#e9fff0;font-variant-numeric:tabular-nums}"
    + "html.lz-splashing,html.lz-splashing body{overflow:hidden!important}";
  var st = document.createElement("style"); st.textContent = css; root.appendChild(st);
  var R = 70, C = 2 * Math.PI * R;
  var el = document.createElement("div"); el.id = "lz-splash"; el.setAttribute("role", "status"); el.setAttribute("aria-label", "LongoUZ yuklanmoqda");
  el.innerHTML = '<div class="sp-fill"></div><div class="sp-box"><div class="sp-logo">'
    + '<svg viewBox="0 0 148 148" aria-hidden="true"><circle class="sp-track" cx="74" cy="74" r="' + R + '"/>'
    + '<circle class="sp-arc" cx="74" cy="74" r="' + R + '" stroke-dasharray="' + C.toFixed(1) + '" stroke-dashoffset="' + C.toFixed(1) + '"/>'
    + '<circle class="sp-spin" cx="74" cy="74" r="' + (R + 0) + '"/></svg>'
    + '<img src="/static/logo-owl3d-sm.png" alt="" width="96" height="73"></div>'
    + '<p class="sp-name">Longo<b>UZ</b></p><div class="sp-bar"><i></i></div><div class="sp-pct">0%</div></div>';
  root.appendChild(el); root.classList.add("lz-splashing");
  var fill = el.querySelector(".sp-fill"), arc = el.querySelector(".sp-arc"), bar = el.querySelector(".sp-bar i"), pct = el.querySelector(".sp-pct");
  var T = 3000, t0 = null;
  function ease(x) { return x < .5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2; }
  function done() {
    try { sessionStorage.setItem("lz_splash_done", "1"); } catch (e) {}
    el.classList.add("is-out"); root.classList.remove("lz-splashing");
    setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); if (st.parentNode) st.parentNode.removeChild(st); }, 600);
  }
  function tick(ts) {
    if (t0 === null) t0 = ts;
    var p = Math.min(1, (ts - t0) / T), v = Math.round(p * 100), e = ease(p);
    fill.style.height = (e * 100) + "%"; arc.setAttribute("stroke-dashoffset", (C * (1 - p)).toFixed(1));
    bar.style.width = v + "%"; pct.textContent = v + "%";
    if (p < 1) requestAnimationFrame(tick); else setTimeout(done, 120);
  }
  requestAnimationFrame(tick);
  setTimeout(function () { if (document.getElementById("lz-splash")) done(); }, T + 1500); /* himoya */
})();
