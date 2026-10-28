/* LongoUZ — AI repetitor: uzluksiz jonli ovozli suhbat.
   Oqim: salomlashadi -> tinglaydi (SpeechRecognition) -> /api/ask -> /api/tts bilan gapiradi -> yana tinglaydi.
   Mikrofon ishlamasa, matn yozish qatori bor. Ovoz serverda (edge-tts) yaratiladi, bo'lmasa brauzer ovoziga o'tadi. */
(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };
  var root = $("rp-call");
  if (!root) return;

  var el = {
    stage: $("rp-stage"), status: $("rp-status"), live: $("rp-live"), sub: $("rp-sub"),
    start: $("rp-start"), mic: $("rp-mic"), micLabel: $("rp-mic-label"), skip: $("rp-skip"), end: $("rp-end"),
    subject: $("rp-subject"), lang: $("rp-lang"), mode: $("rp-mode"), voice: $("rp-voice"),
    form: $("rp-form"), input: $("rp-input"), transcript: $("rp-transcript"),
    usage: $("rp-usage"), usageFill: $("rp-usage-fill"), wave: root.querySelectorAll(".rp-wave i"),
  };
  var userName = root.getAttribute("data-user") || "do'st";
  var SR = window.SpeechRecognition || window.webkitSpeechRecognition;

  var S = {
    active: false, state: "idle", muted: false, busy: false,
    history: [], rec: null, recRunning: false, silent: 0,
    audio: new Audio(), playToken: 0, ctx: null, analyser: null, raf: 0,
  };

  // ---------- sozlamalar (brauzerda eslab qolinadi) ----------
  function load(key, fallback) { try { return localStorage.getItem("rp_" + key) || fallback; } catch (e) { return fallback; } }
  function save(key, val) { try { localStorage.setItem("rp_" + key, val); } catch (e) { /* ixtiyoriy */ } }
  el.subject.value = load("subject", root.getAttribute("data-subject") || "math");
  if (!el.subject.value) el.subject.value = "math";
  el.lang.value = load("lang", "uz-UZ");
  el.mode.value = load("mode", "chat");
  el.voice.value = load("voice", "male");

  function langCode() { return (el.mode.value === "ielts" ? "en-US" : el.lang.value); }
  function shortLang() { return langCode().split("-")[0]; }

  function applyModeUi() {
    var ielts = el.mode.value === "ielts";
    el.subject.disabled = ielts; el.lang.disabled = ielts;
    if (ielts) { el.subject.value = "english"; el.lang.value = "en-US"; }
    el.sub.textContent = ielts ? "IELTS Speaking — examiner bilan mashq" : "Jonli ovozli suhbat — gapiring, men eshitaman";
  }
  applyModeUi();
  ["subject", "lang", "mode", "voice"].forEach(function (k) {
    el[k].addEventListener("change", function () {
      save(k, el[k].value); applyModeUi();
      if (k !== "voice" && S.active) restartCall();
    });
  });

  // ---------- holat ----------
  var STATUS = {
    idle: "Suhbatni boshlash uchun tugmani bosing", greeting: "Repetitor gapiryapti…", speaking: "Repetitor gapiryapti…",
    listening: "Eshityapman — gapiring", thinking: "O'ylayapman…", paused: "Mikrofon o'chiq — yozing yoki yoqing",
  };
  function setState(st, text) {
    S.state = st; el.stage.setAttribute("data-state", st);
    el.status.textContent = text || STATUS[st] || "";
    var running = S.active;
    el.start.hidden = running; el.mic.hidden = !running; el.end.hidden = !running;
    el.skip.hidden = !(running && (st === "speaking" || st === "greeting"));
    if (st !== "listening") { el.live.hidden = true; el.live.textContent = ""; }
  }

  function addLine(role, text) {
    var d = document.createElement("div");
    d.className = "rp-line rp-" + role;
    var who = document.createElement("b");
    who.textContent = role === "user" ? "Siz" : "Repetitor";
    var p = document.createElement("span");
    p.textContent = text;
    d.appendChild(who); d.appendChild(p);
    el.transcript.appendChild(d);
    el.transcript.scrollTop = el.transcript.scrollHeight;
  }

  // ---------- gapirish (TTS) ----------
  var UZ_HINTS = /\b(va|bu|siz|uchun|bilan|xato|to'g'ri|tuzatish|kerak|yaxshi|juda|lekin|yoki|ham|nima|qanday|keling|mana|xo'sh|ayting|eslab|tavsiya|fikr|baho)\b/i;
  function sentenceLang(sentence) {
    var base = shortLang();
    if (base !== "en") return base;
    return (UZ_HINTS.test(sentence) || /[oOgG]['‘’`ʻ]/.test(sentence)) ? "uz" : "en";
  }

  function splitForTts(text) {
    var sentences = text.replace(/\s+/g, " ").match(/[^.!?…]+[.!?…]*/g) || [text];
    var chunks = [], cur = "", curLang = "";
    sentences.forEach(function (s) {
      s = s.trim(); if (!s) return;
      var l = sentenceLang(s);
      if (cur && (l !== curLang || (cur.length + s.length) > 380)) { chunks.push({ text: cur, lang: curLang }); cur = ""; }
      cur = cur ? cur + " " + s : s; curLang = l;
    });
    if (cur) chunks.push({ text: cur, lang: curLang });
    return chunks;
  }

  function fetchAudio(chunk) {
    return fetch("/api/tts", {
      method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: chunk.text, lang: chunk.lang, voice: el.voice.value }),
    }).then(function (r) { if (!r.ok) throw new Error("tts " + r.status); return r.blob(); })
      .then(function (b) { return URL.createObjectURL(b); });
  }

  function ensureAnalyser() {
    if (S.analyser || !(window.AudioContext || window.webkitAudioContext)) return;
    try {
      S.ctx = new (window.AudioContext || window.webkitAudioContext)();
      var src = S.ctx.createMediaElementSource(S.audio);
      S.analyser = S.ctx.createAnalyser(); S.analyser.fftSize = 64;
      src.connect(S.analyser); S.analyser.connect(S.ctx.destination);
    } catch (e) { S.analyser = null; }
  }
  function animateWave() {
    cancelAnimationFrame(S.raf);
    if (!S.analyser) return;
    var data = new Uint8Array(S.analyser.frequencyBinCount);
    (function tick() {
      if (S.state !== "speaking" && S.state !== "greeting") { el.wave.forEach(function (b) { b.style.transform = ""; }); return; }
      S.analyser.getByteFrequencyData(data);
      el.wave.forEach(function (b, i) {
        var v = data[Math.min(data.length - 1, i + 1)] / 255;
        b.style.transform = "scaleY(" + (0.18 + v * 1.1).toFixed(2) + ")";
      });
      S.raf = requestAnimationFrame(tick);
    })();
  }

  function playUrl(url, token) {
    return new Promise(function (resolve, reject) {
      if (token !== S.playToken) { URL.revokeObjectURL(url); resolve(); return; }
      S.audio.src = url;
      S.audio.onended = function () { URL.revokeObjectURL(url); resolve(); };
      S.audio.onerror = function () { URL.revokeObjectURL(url); reject(new Error("audio")); };
      var pr = S.audio.play();
      if (pr && pr.catch) pr.catch(reject);
      if (S.ctx && S.ctx.state === "suspended") S.ctx.resume();
      animateWave();
    });
  }

  function browserSpeak(text, lang) {
    return new Promise(function (resolve) {
      if (!window.speechSynthesis) { resolve(); return; }
      var u = new SpeechSynthesisUtterance(text);
      u.lang = ({ uz: "uz-UZ", ru: "ru-RU", en: "en-US" })[lang] || "uz-UZ";
      u.onend = u.onerror = function () { resolve(); };
      window.speechSynthesis.speak(u);
    });
  }

  // true — gapirib bo'ldi; "blocked" — brauzer avtomatik ovozga ruxsat bermadi
  async function speak(text) {
    var token = ++S.playToken;
    var chunks = splitForTts(text);
    var next = chunks.length ? fetchAudio(chunks[0]) : null;
    for (var i = 0; i < chunks.length; i++) {
      if (token !== S.playToken) return true;
      var cur = next;
      next = (i + 1 < chunks.length) ? fetchAudio(chunks[i + 1]) : null;
      if (next) next.catch(function () { /* keyin tekshiriladi */ });
      try {
        var url = await cur;
        ensureAnalyser();
        await playUrl(url, token);
      } catch (e) {
        if (e && e.name === "NotAllowedError") return "blocked";
        await browserSpeak(chunks[i].text, chunks[i].lang);
      }
    }
    return true;
  }
  function stopSpeaking() {
    S.playToken++;
    try { S.audio.pause(); } catch (e) { /* e'tiborsiz */ }
    if (window.speechSynthesis) window.speechSynthesis.cancel();
  }

  // ---------- eshitish (STT) ----------
  function stopListening() {
    if (S.rec) { try { S.rec.onend = null; S.rec.abort(); } catch (e) { /* e'tiborsiz */ } }
    S.rec = null; S.recRunning = false;
  }

  function startListening() {
    if (!S.active || S.muted || S.busy) return;
    if (!SR) { setState("paused", "Brauzer ovozli kiritishni qo'llamaydi — pastga yozing"); return; }
    stopListening();
    var rec = new SR();
    rec.lang = langCode(); rec.interimResults = true; rec.continuous = false; rec.maxAlternatives = 1;
    var finalText = "";
    rec.onstart = function () { S.recRunning = true; setState("listening"); };
    rec.onresult = function (ev) {
      var interim = "";
      for (var i = ev.resultIndex; i < ev.results.length; i++) {
        var t = ev.results[i][0].transcript;
        if (ev.results[i].isFinal) finalText += t; else interim += t;
      }
      var show = (finalText + " " + interim).trim();
      if (show) { el.live.hidden = false; el.live.textContent = show; S.silent = 0; }
    };
    rec.onerror = function (ev) {
      if (ev.error === "not-allowed" || ev.error === "service-not-allowed") {
        S.muted = true; syncMic();
        setState("paused", "Mikrofonga ruxsat berilmadi. Brauzer manzil qatoridagi qulf belgisidan ruxsat bering yoki pastga yozing.");
      } else if (ev.error === "network") {
        S.muted = true; syncMic();
        setState("paused", "Ovozni matnga o'girish xizmatiga ulanib bo'lmadi. Pastga yozing yoki internetni tekshiring.");
      }
    };
    rec.onend = function () {
      S.recRunning = false;
      var said = finalText.trim();
      if (said) { onUserSaid(said); return; }
      if (!S.active || S.muted || S.busy) return;
      S.silent++;
      if (S.silent === 4) { setState("listening", "Eshityapman, davom eting…"); }
      if (S.silent >= 8) { S.muted = true; syncMic(); setState("paused", "Uzoq sukut. Davom etish uchun mikrofonni yoqing."); return; }
      setTimeout(startListening, 200);
    };
    S.rec = rec;
    try { rec.start(); } catch (e) { setTimeout(startListening, 400); }
  }

  function syncMic() {
    el.mic.setAttribute("aria-pressed", String(!S.muted));
    el.micLabel.textContent = S.muted ? "Mikrofon o'chiq" : "Mikrofon yoqiq";
    el.mic.classList.toggle("is-off", S.muted);
  }

  // ---------- AI ----------
  function renderUsage(u) {
    if (!u || !u.limit) return;
    el.usage.hidden = false;
    el.usageFill.style.width = Math.min(100, Math.round((u.used / u.limit) * 100)) + "%";
  }

  async function onUserSaid(text) {
    if (S.busy) return;
    S.busy = true; S.silent = 0; stopListening();
    addLine("user", text);
    setState("thinking");
    var reply = "", limited = false;
    try {
      var res = await fetch("/api/ask", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question: text, effort: "normal", source: "repetitor", lang: langCode(),
          subject: el.subject.value, mode: el.mode.value,
          history: S.history.slice(-10),
        }),
      });
      if (res.status === 401) { location.href = "/login"; return; }
      var data = await res.json().catch(function () { return {}; });
      if (res.status === 402 || data.limit_reached) {
        limited = true; reply = data.message || "AI limiti tugadi.";
      } else if (!res.ok) {
        reply = (data && data.detail) ? String(data.detail) : "Server xatosi. Birozdan keyin qayta urinib ko'ring.";
      } else {
        reply = data.answer || "";
        renderUsage(data.usage);
        if (data.provider !== "none") { S.history.push({ role: "user", text: text }, { role: "assistant", text: reply }); }
      }
    } catch (e) {
      reply = "Internet aloqasi uzildi. Qayta urinib ko'ring.";
    }
    S.busy = false;
    if (!reply) { startListening(); return; }
    addLine("assistant", reply);
    if (limited) {
      var a = document.createElement("a"); a.href = "/upgrade"; a.className = "rp-upgrade"; a.textContent = "Tarifni ko'rish";
      el.transcript.appendChild(a);
      setState("paused", "Limit tugadi"); return;
    }
    setState("speaking");
    var r = await speak(reply);
    if (!S.active) return;
    if (r === "blocked") { setState("paused", "Ovoz bloklangan — sahifada bir marta bosing"); return; }
    startListening();
  }

  // ---------- qo'ng'iroq boshqaruvi ----------
  function greeting() {
    var l = shortLang();
    if (el.mode.value === "ielts") {
      return "Hello, " + userName + ". I'm your IELTS speaking examiner today. Let's begin with Part one. Could you tell me a little about yourself? What do you do, work or study?";
    }
    if (l === "ru") return "Здравствуйте, " + userName + "! Я ваш ИИ-репетитор. Какую тему сегодня разберём? Просто скажите.";
    if (l === "en") return "Hello, " + userName + "! I'm your AI tutor. What would you like to practise today? Just say it.";
    return "Assalomu alaykum, " + userName + "! Men sizning AI repetitoringizman. Bugun qaysi mavzuni o'rganamiz? Shunchaki ayting, men eshitaman.";
  }

  async function startCall() {
    if (S.active && S.state !== "idle") return;
    S.active = true; S.muted = false; S.busy = false; S.silent = 0; S.history = [];
    el.transcript.innerHTML = ""; syncMic();
    var g = greeting();
    addLine("assistant", g);
    S.history.push({ role: "assistant", text: g });
    setState("greeting");
    if (!window.isSecureContext && !/^(localhost|127\.0\.0\.1)$/.test(location.hostname)) {
      el.status.textContent = "Mikrofon uchun sahifani HTTPS orqali oching (https://…:6600).";
    }
    var r = await speak(g);
    if (!S.active) return;
    if (r === "blocked") {
      S.active = false; setState("idle", "Brauzer avtomatik ovozni to'sdi — «Suhbatni boshlash» tugmasini bosing");
      return;
    }
    startListening();
  }

  function endCall() {
    S.active = false; S.busy = false; stopListening(); stopSpeaking();
    setState("idle", "Suhbat tugadi. Qayta boshlash uchun tugmani bosing.");
  }
  function restartCall() { endCall(); setTimeout(startCall, 150); }

  el.start.addEventListener("click", function () {
    if (S.ctx && S.ctx.state === "suspended") S.ctx.resume();
    startCall();
  });
  el.end.addEventListener("click", endCall);
  el.skip.addEventListener("click", function () { stopSpeaking(); });
  el.mic.addEventListener("click", function () {
    S.muted = !S.muted; syncMic();
    if (S.muted) { stopListening(); setState("paused"); } else { S.silent = 0; startListening(); }
  });
  el.form.addEventListener("submit", function (e) {
    e.preventDefault();
    var t = el.input.value.trim(); if (!t) return;
    el.input.value = "";
    if (!S.active) { S.active = true; syncMic(); }
    stopSpeaking(); stopListening();
    onUserSaid(t);
  });
  document.addEventListener("visibilitychange", function () {
    if (document.hidden && S.active) { stopListening(); stopSpeaking(); setState("paused", "Sahifa yopiq — qaytganda mikrofonni yoqing"); S.muted = true; syncMic(); }
  });
  window.addEventListener("beforeunload", function () { stopSpeaking(); stopListening(); });

  // limit ko'rsatkichi
  fetch("/api/usage").then(function (r) { return r.ok ? r.json() : null; }).then(renderUsage).catch(function () {});

  // Sahifa ochilishi bilan o'zi boshlaydi; brauzer ovozni to'ssa, tugma qoladi.
  setState("idle");
  setTimeout(startCall, 350);
})();
