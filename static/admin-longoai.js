/* v243: Admin — LongoAI sahifasi: suhbat (formulalar/chizmalar bilan), vosita bosqichlari, tasdiq kartalari, avtomatik ish sozlamalari, ishlar jurnali. */
(function () {
  "use strict";
  var P = (window.LONGOAI || {}).prefix || "/neo";
  var $ = function (id) { return document.getElementById(id); };
  var chat = $("la-chat"), text = $("la-text"), sendBtn = $("la-send");
  var STORE = "lz_longoai_chat_v1";
  var hist = [];
  try { hist = JSON.parse(localStorage.getItem(STORE) || "[]").slice(-30); } catch (e) { hist = []; }

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function save() { try { localStorage.setItem(STORE, JSON.stringify(hist.slice(-30))); } catch (e) {} }
  function api(path, body, method) {
    return fetch(P + path, {
      method: method || (body ? "POST" : "GET"), credentials: "same-origin",
      headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" },
      body: body ? JSON.stringify(body) : undefined
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok) throw new Error(j.detail || ("Xato " + r.status)); return j; });
    });
  }
  var scroll = function () { chat.scrollTop = chat.scrollHeight; };
  function hideEmpty() { var e = $("la-empty"); if (e) e.hidden = true; }

  function addUser(t) {
    hideEmpty();
    var d = document.createElement("div"); d.className = "la-msg la-u"; d.textContent = t; chat.appendChild(d); scroll();
  }
  function addAi(t, steps, meta) {
    hideEmpty();
    var wrap = document.createElement("div"); wrap.className = "la-msg la-a";
    var av = document.createElement("div"); av.className = "la-av"; wrap.appendChild(av);
    var body = document.createElement("div"); body.className = "la-body";
    if (steps && steps.length) {
      var st = document.createElement("div"); st.className = "la-steps";
      st.innerHTML = steps.map(function (s) {
        return '<span class="la-step' + (s.ok === false ? " bad" : "") + '" title="' + esc(JSON.stringify(s.args || {})) + '">' + esc(s.label || s.tool) + (s.ms ? " · " + (s.ms / 1000).toFixed(1) + "s" : "") + "</span>";
      }).join("");
      body.appendChild(st);
    }
    var txt = document.createElement("div"); txt.className = "la-text";
    if (window.LongoRender) window.LongoRender.render(txt, t); else txt.textContent = t;
    body.appendChild(txt);
    if (meta) { var m = document.createElement("small"); m.className = "la-meta"; m.textContent = meta; body.appendChild(m); }
    wrap.appendChild(body);
    chat.appendChild(wrap); scroll();
    return wrap;
  }

  // ---------------------------------------------------------------- tasdiq kartalari
  var TYPE = { update_question: "Savolni tuzatish", delete_question: "Savolni o'chirish", create_questions: "Yangi savollar", support_reply: "Xabarga javob" };
  function actionCard(a) {
    var d = document.createElement("div"); d.className = "la-act la-act-" + a.type;
    var p = a.payload || {}, inner = "";
    if (a.type === "update_question") {
      var f = p.fields || {};
      inner = '<div class="la-act-q">Savol <a href="' + P + "/questions/" + esc(p.id) + '/edit" target="_blank">#' + esc(p.id) + "</a></div>";
      Object.keys(f).forEach(function (k) {
        var v = f[k];
        if (k === "options" && Array.isArray(v)) v = v.map(function (o, i) { return "ABCD"[i] + ") " + o; }).join("\n");
        if (k === "correct_index") v = "ABCD"[v] || v;
        inner += '<div class="la-f"><span>' + esc({ question: "Savol matni", options: "Variantlar", correct_index: "To'g'ri javob", explanation: "Izoh", topic: "Mavzu", difficulty: "Qiyinlik", is_active: "Faol", accept: "Qabul qilinadigan javoblar", min_plan: "Tarif" }[k] || k) + '</span><div class="la-fv" data-k="' + esc(k) + '"></div></div>';
        d._vals = d._vals || {}; d._vals[k] = Array.isArray(v) ? v.join(", ") : String(v);
      });
    } else if (a.type === "delete_question") {
      inner = '<div class="la-act-q">Savol <a href="' + P + "/questions/" + esc(p.id) + '/edit" target="_blank">#' + esc(p.id) + "</a> o'chiriladi</div>";
    } else if (a.type === "create_questions") {
      var qs = p.questions || [];
      inner = '<div class="la-act-q">' + esc(p.subject) + " / " + esc(p.mode) + " — " + esc(p.topic) + ": " + qs.length + " ta savol</div><ol class=\"la-newq\">" +
        qs.slice(0, 12).map(function (q) { return "<li data-q></li>"; }).join("") + "</ol>";
    } else if (a.type === "support_reply") {
      inner = '<div class="la-act-q">Xabar <a href="' + P + "/messages/" + esc(p.id) + '" target="_blank">#' + esc(p.id) + '</a> ga javob</div><div class="la-fv" data-k="text"></div>';
      d._vals = { text: p.text || "" };
    }
    d.innerHTML = '<div class="la-act-top"><span class="la-act-type">' + esc(TYPE[a.type] || a.type) + "</span><span class=\"la-act-why\"></span></div>" + inner +
      '<div class="la-act-btns"><button type="button" class="btn-primary admin-btn-sm ok">Qo\'llash</button><button type="button" class="la-ghost no">Rad etish</button><span class="la-act-note"></span></div>';
    d.querySelector(".la-act-why").textContent = a.reason || "";
    Object.keys(d._vals || {}).forEach(function (k) {
      var el = d.querySelector('.la-fv[data-k="' + k + '"]');
      if (el) { if (window.LongoRender && /\$|\\\(|```/.test(d._vals[k])) window.LongoRender.render(el, d._vals[k]); else el.textContent = d._vals[k]; }
    });
    if (a.type === "create_questions") {
      var lis = d.querySelectorAll("li[data-q]");
      (p.questions || []).slice(0, 12).forEach(function (q, i) {
        var opts = (q.options || []).map(function (o, j) { return (j === q.correct_index ? "✓ " : "") + "ABCD"[j] + ") " + o; }).join("   ");
        var src = (q.question || "") + (opts ? "\n" + opts : "") + (q.accept ? "\nJavob: " + q.accept.join(", ") : "");
        if (window.LongoRender) window.LongoRender.render(lis[i], src); else lis[i].textContent = src;
      });
    }
    d.querySelector(".no").onclick = function () { d.classList.add("gone"); setTimeout(function () { d.remove(); syncActions(); }, 250); };
    d.querySelector(".ok").onclick = function () { apply(a, d); };
    d._action = a;
    return d;
  }
  function apply(a, d) {
    var b = d.querySelector(".ok"), note = d.querySelector(".la-act-note");
    b.disabled = true; note.textContent = "Bajarilmoqda…";
    return api("/api/studio/assistant/apply", { action: a }).then(function (j) {
      d.classList.add("done"); note.textContent = "Bajarildi ✓" + (j.regrade && j.regrade.users ? " — " + j.regrade.users + " o'quvchi natijasi yangilandi" : "");
      d.querySelector(".no").hidden = true;
    }).catch(function (e) { b.disabled = false; note.textContent = e.message; d.classList.add("err"); });
  }
  function syncActions() { $("la-actions").hidden = !$("la-actions-list").children.length; }
  $("la-apply-all").onclick = function () {
    var cards = [].slice.call($("la-actions-list").children).filter(function (c) { return !c.classList.contains("done"); });
    (function next(i) { if (i >= cards.length) return; apply(cards[i]._action, cards[i]).then(function () { next(i + 1); }); })(0);
  };

  // ---------------------------------------------------------------- aqlli aylantirish
  // v246: foydalanuvchi tepaga chiqib o'qiyotgan bo'lsa — majburan pastga tushirilmaydi; «Pastga» tugmasi chiqadi
  var stick = true;
  var downBtn = document.createElement("button");
  downBtn.type = "button"; downBtn.className = "la-down"; downBtn.hidden = true; downBtn.setAttribute("aria-label", "Pastga");
  downBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12l7 7 7-7"/></svg>';
  chat.parentNode.insertBefore(downBtn, chat.nextSibling);
  downBtn.onclick = function () { stick = true; chat.scrollTop = chat.scrollHeight; downBtn.hidden = true; };
  chat.addEventListener("scroll", function () {
    var near = chat.scrollHeight - chat.scrollTop - chat.clientHeight < 60;
    stick = near; if (near) downBtn.hidden = true;
  }, { passive: true });
  scroll = function () { if (stick) chat.scrollTop = chat.scrollHeight; else downBtn.hidden = false; };

  // javob matnini bosqichma-bosqich (yozayotgandek) chiqarish
  function typeOut(el, full, done) {
    var words = full.split(/(\s+)/), i = 0, last = 0;
    var per = Math.max(2, Math.round(words.length / 90));   // uzun javob ~3-5 soniyada tugaydi
    function tick() {
      i = Math.min(words.length, i + per);
      var now = Date.now();
      if (now - last > 70 || i >= words.length) {
        last = now;
        var part = words.slice(0, i).join("");
        if (window.LongoRender) window.LongoRender.render(el, part, { streaming: i < words.length }); else el.textContent = part;
        scroll();
      }
      if (i < words.length) setTimeout(tick, 18); else if (done) done();
    }
    tick();
  }

  // ---------------------------------------------------------------- yuborish
  var busy = false;
  function fmtSec(ms) { return (ms / 1000).toFixed(1).replace(".", ",") + " s"; }
  function send(t) {
    t = (t || "").trim(); if (!t || busy) return;
    busy = true; sendBtn.disabled = true; stick = true;
    addUser(t); hist.push({ role: "user", text: t }); save();
    text.value = ""; grow();
    var t0 = Date.now();
    var thinking = window.LongoThink ? window.LongoThink.row("LongoAI o'ylamoqda", { size: "", rotate: false }) : document.createElement("div");
    var holder = document.createElement("div"); holder.className = "la-thinking";
    var live = document.createElement("div"); live.className = "la-steps la-steps-live";
    holder.appendChild(thinking); holder.appendChild(live); chat.appendChild(holder); scroll();
    var clock = setInterval(function () { if (thinking.setStep) thinking.setStep("Ishlamoqda · " + fmtSec(Date.now() - t0)); }, 200);
    function finish(j) {
      clearInterval(clock); holder.remove();
      var wrap = addAi("", j.steps || [], null);
      var body = wrap.querySelector(".la-text");
      typeOut(body, j.reply || "Tayyor.", function () {
        var m = document.createElement("small"); m.className = "la-meta";
        m.textContent = "Ishladi: " + fmtSec(j.ms || (Date.now() - t0)) + ((j.steps || []).length ? " · " + j.steps.length + " ta amal" : "") + (j.model ? " · " + j.model : "");
        body.parentNode.appendChild(m);
        hist.push({ role: "assistant", text: j.reply || "" }); save();
        (j.actions || []).forEach(function (a) { $("la-actions-list").appendChild(actionCard(a)); });
        syncActions();
        busy = false; sendBtn.disabled = false; scroll();
      });
    }
    function fail(msg) { clearInterval(clock); holder.remove(); addAi("Xatolik: " + msg + ". Bir daqiqadan so'ng qayta urinib ko'ring."); busy = false; sendBtn.disabled = false; }
    fetch(P + "/api/longoai/stream", {
      method: "POST", credentials: "same-origin",
      headers: { "Content-Type": "application/json", "X-Requested-With": "fetch", "Accept": "text/event-stream" },
      body: JSON.stringify({ messages: hist.slice(-14) })
    }).then(function (r) {
      if (!r.ok || !r.body) throw new Error("Xato " + r.status);
      var reader = r.body.getReader(), dec = new TextDecoder(), buf = "", got = false;
      function pump() {
        return reader.read().then(function (x) {
          if (x.done) { if (!got) fail("javob kelmadi"); return; }
          buf += dec.decode(x.value, { stream: true });
          var k;
          while ((k = buf.indexOf("\n\n")) >= 0) {
            var block = buf.slice(0, k); buf = buf.slice(k + 2);
            var line = block.split("\n").filter(function (l) { return l.indexOf("data:") === 0; }).map(function (l) { return l.slice(5).trim(); }).join("");
            if (!line) continue;
            var ev; try { ev = JSON.parse(line); } catch (e) { continue; }
            if (ev.step) {
              var st = ev.step;
              if (st.start) { var sp = document.createElement("span"); sp.className = "la-step run"; sp.textContent = st.label || st.tool; live.appendChild(sp); }
              else { var lastRun = live.querySelector(".la-step.run"); if (lastRun) { lastRun.classList.remove("run"); if (st.ok === false) lastRun.classList.add("bad"); lastRun.textContent += " · " + fmtSec(st.ms || 0); } }
              scroll();
            } else if (ev.done) { got = true; finish(ev.done); return; }
            else if (ev.error) { got = true; fail(ev.error); return; }
          }
          return pump();
        });
      }
      return pump();
    }).catch(function (e) { fail(e.message); });
  }
  function grow() { text.style.height = "auto"; text.style.height = Math.min(180, text.scrollHeight) + "px"; }
  text.addEventListener("input", grow);
  text.addEventListener("keydown", function (e) { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(text.value); } });
  $("la-form").addEventListener("submit", function (e) { e.preventDefault(); send(text.value); });
  text.addEventListener("focus", function () { setTimeout(function () { stick = true; scroll(); }, 300); });
  $("la-sugg").addEventListener("click", function (e) { var b = e.target.closest("button"); if (b) send(b.textContent); });
  $("la-clear").onclick = function () {
    hist = []; save();
    [].slice.call(chat.querySelectorAll(".la-msg")).forEach(function (m) { m.remove(); });
    $("la-actions-list").innerHTML = ""; syncActions();
    var e = $("la-empty"); if (e) e.hidden = false;
  };
  // avvalgi suhbatni tiklash
  hist.forEach(function (m) { if (m.role === "user") addUser(m.text); else addAi(m.text); });

  // ---------------------------------------------------------------- sozlamalar
  document.querySelectorAll("[data-cfg]").forEach(function (cb) {
    cb.addEventListener("change", function () {
      var body = {}; body[cb.dataset.cfg] = cb.checked;
      $("la-cfg-note").textContent = "Saqlanmoqda…";
      api("/api/agent/settings", body).then(function () { $("la-cfg-note").textContent = "Saqlandi ✓"; setTimeout(function () { $("la-cfg-note").textContent = ""; }, 1800); })
        .catch(function (e) { $("la-cfg-note").textContent = e.message; cb.checked = !cb.checked; });
    });
  });

  // ---------------------------------------------------------------- ishlar jurnali
  var ST = { pending: "navbatda", running: "bajarilmoqda", done: "hal qilindi", admin: "sizga qoldirildi", error: "xato" };
  var KIND = { report: "Shikoyat", support: "Yordam xabari" };
  function loadJobs() {
    api("/api/agent/jobs?limit=30").then(function (d) {
      $("la-pending").textContent = (d.counts && d.counts.pending) || 0;
      var box = $("la-jobs");
      if (!d.items.length) { box.innerHTML = '<p class="la-note">Hali ish yo\'q. O\'quvchi shikoyat yoki yordam xabari yuborsa, shu yerda ko\'rinadi.</p>'; return; }
      box.innerHTML = d.items.map(function (j) {
        var link = j.kind === "report" ? P + "/reports" : P + "/messages/" + j.ref;
        return '<div class="la-job s-' + esc(j.status) + '"><div class="la-job-top"><a href="' + link + '">' + esc(KIND[j.kind] || j.kind) + " #" + esc(j.ref) + '</a><span class="la-job-st">' + esc(ST[j.status] || j.status) + "</span></div>" +
          (j.result ? '<p>' + esc(j.result).slice(0, 260) + "</p>" : "") + '<small>' + esc(j.created) + (j.steps && j.steps.length ? " · " + j.steps.map(function (s) { return esc(s.label); }).join(" → ") : "") + "</small></div>";
      }).join("");
    }).catch(function () {});
  }
  $("la-run").onclick = function () {
    var b = $("la-run"); b.disabled = true; b.textContent = "Bajarilmoqda…";
    api("/api/agent/run", {}).then(function (d) { b.textContent = d.done.length ? d.done.length + " ta bajarildi" : "Navbat bo'sh"; loadJobs(); })
      .catch(function (e) { b.textContent = e.message; }).then(function () { setTimeout(function () { b.disabled = false; b.textContent = "Hozir bajarish"; }, 2500); });
  };
  loadJobs(); setInterval(function () { if (!document.hidden) loadJobs(); }, 20000);
})();
