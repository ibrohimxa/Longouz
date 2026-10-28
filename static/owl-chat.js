// ============================================================================
// LongoUZ — pin qilingan "Ask LongoAI" chat mantiqi
// - Login qilingan sahifalarda /api/ask'ga ulanadi
// - Javob kelguncha boyqush kallasi asta aylanib "o'ylaydi"
// - Javob typewriter effektida, birma-bir yoziladi
// - window.LongoUZChat.ask(matn) — boshqa sahifalardan (masalan test
//   natijasi sahifasidan) dasturiy ravishda savol yuborish uchun ochiq API
// ============================================================================

(function () {
  const form = document.getElementById("floating-chat-form");
  const input = document.getElementById("floating-chat-input");
  const messages = document.getElementById("floating-chat-messages");
  const sendBtn = document.getElementById("floating-chat-send");
  const pinButton = document.getElementById("owl-pin-button");
  const chatWidget = document.getElementById("floating-chat-widget");
  const micBtn = document.getElementById("floating-chat-mic");
  const voiceToggleBtn = document.getElementById("floating-chat-voice-toggle");
  const voiceOrb = document.getElementById("owl-voice-orb");
  const orbLabel = document.getElementById("repetitor-orb-label");

  function setOrbLabel(text) {
    if (orbLabel) orbLabel.textContent = text;
  }

  if (!form || !input || !messages) return;

  // Agar sahifada login qilinmagan bo'lsa (bosh sahifa), input disabled qilamiz.
  // MUHIM: session cookie httponly qilib o'rnatiladi (xavfsizlik uchun), shuning
  // uchun uni document.cookie orqali JS'dan o'qib bo'lmaydi — u har doim bo'sh
  // qaytadi va "isLoggedIn" doim false chiqib, login qilingan foydalanuvchiga ham
  // "avval ro'yxatdan o'ting" degan xato ko'rsatilardi. Endi holat server tomondan
  // <body data-logged-in="true|false"> atributi orqali to'g'ri uzatiladi.
  const isLoggedIn = document.body.dataset.loggedIn === "true";
  if (!isLoggedIn) {
    input.disabled = true;
    input.placeholder = "Ro'yxatdan o'tib, savol bering...";
    const empty = document.getElementById("floating-chat-empty");
    if (empty) empty.textContent = "Savol berish uchun avval ro'yxatdan o'ting.";
    return;
  }

  // ==========================================================================
  // OVOZLI KIRISH — to'g'ridan-to'g'ri (jonli) nutq tanish. Ovoz yozib
  // yuborilmaydi: brauzerning Speech Recognition xizmati gapirayotganingizni
  // real vaqtda matnga aylantiradi, jimlik boshlanganda savol avtomatik
  // yuboriladi. /repetitor sahifasida "Jonli suhbat" rejimi: AI javobini
  // aytib bo'lgach, mikrofon o'zi qayta tinglashni boshlaydi.
  // ==========================================================================
  const SpeechRecognitionAPI = window.SpeechRecognition || window.webkitSpeechRecognition;
  const isRepetitorPage = !!voiceOrb && document.body.classList.contains("repetitor-fullpage");
  const langSelect = document.getElementById("repetitor-lang");
  const liveBtn = document.getElementById("repetitor-live-btn");
  const stopSpeakBtn = document.getElementById("repetitor-stop-speak");
  const interimEl = document.getElementById("repetitor-interim");
  let activeRecognition = null;
  let isListening = false;
  let liveMode = false;        // jonli suhbat yoqilganmi
  let busy = false;            // AI o'ylayapti yoki gapiryapti — mikrofon pauza
  let restartTimer = null;

  const STATUS_IDLE = "Savolingizni yozing yoki gapiring";

  function micUnavailableReason() {
    if (!SpeechRecognitionAPI) {
      return "Bu brauzer ovozli kiritishni qo'llamaydi. Chrome, Edge yoki Safari'dan foydalaning — yoki savolni yozing.";
    }
    if (!window.isSecureContext) {
      return "Mikrofon faqat HTTPS yoki localhost orqali ishlaydi. Telefonda ishlatish uchun saytni HTTPS bilan oching (README_ADMIN.md → HTTPS) — hozircha savolni yozishingiz mumkin.";
    }
    return "";
  }

  function noteToUser(text) {
    clearEmptyState();
    let note = document.getElementById("owl-system-note");
    if (!note) {
      note = document.createElement("div");
      note.id = "owl-system-note";
      note.className = "chat-msg chat-system-note";
      messages.appendChild(note);
    }
    note.textContent = text;
    messages.scrollTop = messages.scrollHeight;
  }
  function clearNote() {
    const n = document.getElementById("owl-system-note");
    if (n) n.remove();
  }

  function setInterim(text) {
    if (interimEl) {
      interimEl.textContent = text || "";
      interimEl.hidden = !text;
    }
    input.value = text || "";
  }

  function recognitionLang() {
    if (langSelect && langSelect.value) return langSelect.value;
    const subj = document.body.dataset.subject || "";
    if (subj === "russian") return "ru-RU";
    if (subj === "english") return "en-US";
    return "uz-UZ";
  }

  function updateMicUI() {
    const on = isListening || liveMode;
    if (micBtn) micBtn.classList.toggle("mic-listening", isListening);
    if (liveBtn) {
      liveBtn.classList.toggle("is-live", liveMode);
      liveBtn.setAttribute("aria-pressed", liveMode ? "true" : "false");
      const label = liveBtn.querySelector("span");
      if (label) label.textContent = liveMode ? "Suhbatni tugatish" : "Jonli suhbatni boshlash";
    }
    if (voiceOrb) voiceOrb.classList.toggle("is-listening", isListening);
    if (isListening) setOrbLabel("Tinglayapman... gapiring");
    else if (!busy) setOrbLabel(liveMode ? "Navbat sizda — gapiring" : STATUS_IDLE);
    input.placeholder = isListening ? "Tinglayapman..." : "Savolingizni yozing...";
    void on;
  }

  function stopListening(opts) {
    clearTimeout(restartTimer);
    const rec = activeRecognition;
    activeRecognition = null;
    isListening = false;
    if (rec) {
      rec.onresult = rec.onerror = rec.onend = rec.onstart = null;
      try { rec.abort(); } catch (e) { /* allaqachon to'xtagan */ }
    }
    if (!opts || !opts.keepInterim) setInterim("");
    updateMicUI();
  }

  function startListening() {
    const problem = micUnavailableReason();
    if (problem) { noteToUser(problem); liveMode = false; updateMicUI(); return; }
    if (isListening || busy) return;
    clearNote();

    const rec = new SpeechRecognitionAPI();
    activeRecognition = rec;
    rec.lang = recognitionLang();
    rec.interimResults = true;
    rec.continuous = false;
    rec.maxAlternatives = 1;
    let sent = false;

    rec.onstart = () => { isListening = true; updateMicUI(); };

    rec.onresult = (event) => {
      let transcript = "";
      let isFinal = false;
      for (let i = 0; i < event.results.length; i++) {
        transcript += event.results[i][0].transcript;
        if (event.results[i].isFinal) isFinal = true;
      }
      setInterim(transcript);
      if (isFinal && !sent) {
        const question = transcript.trim();
        if (question) {
          sent = true;
          stopListening();
          sendQuestion(question);
        }
      }
    };

    rec.onerror = (event) => {
      const code = event && event.error;
      if (code === "no-speech" || code === "aborted") return; // onend hal qiladi
      let msg = "Mikrofonda xatolik: " + code;
      if (code === "not-allowed" || code === "service-not-allowed") {
        msg = "Mikrofonga ruxsat berilmagan. Brauzer manzil satridagi qulf belgisidan mikrofonga ruxsat bering va qayta urining.";
      } else if (code === "audio-capture") {
        msg = "Mikrofon topilmadi. Qurilmangizda mikrofon ulanganini tekshiring.";
      } else if (code === "network") {
        msg = "Nutqni tanish xizmatiga ulanib bo'lmadi (internet kerak). Savolni yozib yuborishingiz mumkin.";
      } else if (code === "language-not-supported") {
        msg = "Tanlangan til qo'llanmaydi. Tilni boshqasiga almashtirib ko'ring (masalan Русский yoki English).";
      }
      noteToUser(msg);
      liveMode = false;
      stopListening();
    };

    rec.onend = () => {
      const wasActive = activeRecognition === rec;
      if (!wasActive) return;
      stopListening();
      // Jonli rejimda hech narsa aytilmasa ham (jimlik) qayta tinglaymiz
      if (liveMode && !busy && !sent) restartTimer = setTimeout(startListening, 250);
    };

    try {
      rec.start();
    } catch (e) {
      noteToUser("Mikrofonni ishga tushirib bo'lmadi: " + (e && e.message ? e.message : e));
      liveMode = false;
      stopListening();
    }
  }

  function setBusy(value) {
    busy = value;
    if (busy && isListening) stopListening();
    updateMicUI();
  }

  // AI javobi tugadi (aytib bo'lindi yoki ovoz o'chiq) — jonli rejimda
  // mikrofon qayta ochiladi.
  function maybeAutoListen() {
    setBusy(false);
    if (liveMode) {
      clearTimeout(restartTimer);
      restartTimer = setTimeout(() => { if (liveMode && !busy && !isListening) startListening(); }, 500);
    }
  }

  function toggleLive() {
    const problem = micUnavailableReason();
    if (problem) { noteToUser(problem); return; }
    unlockAudio();
    liveMode = !liveMode;
    if (liveMode) {
      cutSpeech();
      setBusy(false);
      startListening();
    } else {
      cutSpeech();
      stopListening();
      setBusy(false);
    }
    updateMicUI();
  }

  if (liveBtn) liveBtn.addEventListener("click", toggleLive);
  if (stopSpeakBtn) stopSpeakBtn.addEventListener("click", () => { cutSpeech(); maybeAutoListen(); });
  if (langSelect) {
    const saved = localStorage.getItem("longouz_stt_lang");
    if (saved) langSelect.value = saved;
    langSelect.addEventListener("change", () => {
      localStorage.setItem("longouz_stt_lang", langSelect.value);
      if (isListening) { stopListening(); startListening(); }
    });
  }

  if (micBtn) {
    micBtn.addEventListener("click", () => {
      const problem = micUnavailableReason();
      if (problem) { noteToUser(problem); return; }
      unlockAudio();
      if (isListening) { stopListening(); return; }
      if (isRepetitorPage && !liveMode) { toggleLive(); return; }
      startListening();
    });
  }

  // ==========================================================================
  // OVOZLI CHIQISH (Text-to-Speech) — ENDI ASOSAN SERVERDA (edge-tts, tts.py)
  // generatsiya qilinadi — bu HAR BIR foydalanuvchida BIR XIL, sifatli va
  // aniq talaffuzli ovoz beradi (avvalgi holatda brauzer o'zi tanlagan
  // tasodifiy, ko'pincha "tarjimon" kabi eshitiladigan ovozdan foydalanardi).
  // Faqat internet/server muammosi bo'lsa, brauzerning o'z ichki ovoziga
  // (Web Speech API) ZAXIRA sifatida o'tiladi — sayt umuman "soqov"
  // qolib ketmasligi uchun.
  // ==========================================================================
  const VOICE_PREF_KEY = "longouz_voice_enabled";
  const storedVoicePref = localStorage.getItem(VOICE_PREF_KEY);
  // MUHIM: agar foydalanuvchi ilgari hech qanday tanlov qilmagan bo'lsa,
  // bu qiymat sahifaning o'zi belgilagan standart holatdan olinadi (masalan
  // repetitor.html sahifasida <body data-voice-default="on">, chunki bu
  // sahifaning butun maqsadi — OVOZLI suhbat).
  let voiceEnabled = storedVoicePref !== null
    ? storedVoicePref === "1"
    : document.body.dataset.voiceDefault === "on";
  let cachedMaleVoice = null;
  let currentAudio = null;
  // Avtoplay siyosati audio.play()ni rad etsa (foydalanuvchi hali sahifada
  // hech narsa bosmagan bo'lsa), shu yerga saqlanadi — keyingi bosish/tugma
  // hodisasida QAYTA urinib ko'ramiz, "robot" ovoziga sakramasdan (chunki
  // server ovozi aslida TO'LIQ tayyor va ishlagan, faqat brauzer avtomatik
  // ijro etishga ruxsat bermagan edi).
  let pendingAudioRetry = null;
  document.addEventListener("click", retryPendingAudio);
  document.addEventListener("keydown", retryPendingAudio);
  function retryPendingAudio() {
    if (!pendingAudioRetry) return;
    const audio = pendingAudioRetry;
    pendingAudioRetry = null;
    audio.play().catch(() => {});
  }

  function pickMaleVoice() {
    if (cachedMaleVoice) return cachedMaleVoice;
    if (!("speechSynthesis" in window)) return null;

    const voices = window.speechSynthesis.getVoices();
    if (!voices.length) return null;

    // 1) Brauzerda HAQIQIY o'zbekcha ovoz bo'lsa (ba'zi qurilmalarda
    // Google'ning kengaytirilgan ovozlari orasida bo'ladi) — eng yaxshisi,
    // darhol shuni ishlatamiz.
    const uzVoice = voices.find((v) => v.lang && v.lang.toLowerCase().startsWith("uz"));
    if (uzVoice) { cachedMaleVoice = uzVoice; return uzVoice; }

    // 2) MUHIM TUZATISH: ilgari shu yerda turkcha ovoz "o'zbekchaga eng
    // yaqin" deb ataylab tanlanardi -- aynan shu narsa foydalanuvchiga
    // "ovoz turkcha bilan aralashgandek eshitiladi" degan shikoyatga sabab
    // bo'lgan. Endi bu ZAXIRA HOLAT (faqat server TTS -- edge-tts -- ishlamay
    // qolgandagina ishlaydi) turkcha o'rniga tiniqroq, neytral ingliz
    // ovoziga o'tadi.
    const maleNameHints = ["male", "david", "mark", "guy", "daniel"];
    const byHint = voices.find((v) => (
      v.lang && v.lang.toLowerCase().startsWith("en") &&
      maleNameHints.some((h) => v.name.toLowerCase().includes(h))
    ));
    if (byHint) { cachedMaleVoice = byHint; return byHint; }

    const enVoice = voices.find((v) => v.lang && v.lang.toLowerCase().startsWith("en"));
    cachedMaleVoice = enVoice || voices[0];
    return cachedMaleVoice;
  }

  if ("speechSynthesis" in window) {
    // Ba'zi brauzerlarda ovozlar ro'yxati asinxron yuklanadi
    window.speechSynthesis.onvoiceschanged = () => { cachedMaleVoice = null; };
  }

  function speakWithBrowserFallback(text) {
    if (!("speechSynthesis" in window)) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    const voice = pickMaleVoice();
    if (voice) utterance.voice = voice;
    // Sekinlashtirilgan tezlik va pasaytirilgan ton avvalgi "robot"ga
    // o'xshash tovushga sabab bo'lgan asosiy omillardan biri edi — tabiiy
    // gapirish tezligiga yaqinlashtirildi.
    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    utterance.volume = 1;
    if (voiceOrb) {
      utterance.onstart = () => { voiceOrb.classList.add("is-speaking"); setOrbLabel("Gapiryapman..."); showStopSpeak(true); };
      utterance.onend = () => { voiceOrb.classList.remove("is-speaking"); showStopSpeak(false); maybeAutoListen(); };
      utterance.onerror = () => { voiceOrb.classList.remove("is-speaking"); showStopSpeak(false); maybeAutoListen(); };
    } else {
      utterance.onend = () => maybeAutoListen();
      utterance.onerror = () => maybeAutoListen();
    }
    // Qo'riqchi: ba'zi qurilmalarda ovoz umuman boshlanmaydi (ovoz yo'q) —
    // mikrofon abadiy "band" bo'lib qolmasligi uchun.
    let started = false;
    const prevStart = utterance.onstart;
    utterance.onstart = (e) => { started = true; if (prevStart) prevStart(e); };
    setTimeout(() => { if (!started) { window.speechSynthesis.cancel(); showStopSpeak(false); maybeAutoListen(); } }, 3500);
    window.speechSynthesis.speak(utterance);
  }

  // Bitta umumiy <audio> elementi: foydalanuvchi mikrofon/jonli tugmasini
  // bosganda "ochiladi" (unlockAudio), shundan keyin AI javobi avtomatik
  // ijro etilganda brauzer (ayniqsa iOS Safari) to'smaydi.
  const player = new Audio();
  player.preload = "auto";
  let audioUnlocked = false;
  const SILENT_WAV = "data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAABErAAABAAgAZGF0YQAAAAA=";
  function unlockAudio() {
    if (audioUnlocked) return;
    audioUnlocked = true;
    try {
      player.src = SILENT_WAV;
      const p = player.play();
      if (p && p.catch) p.catch(() => {});
    } catch (e) { /* e'tiborsiz */ }
  }

  function showStopSpeak(visible) {
    if (stopSpeakBtn) stopSpeakBtn.hidden = !visible;
  }

  function cutSpeech() {
    pendingAudioRetry = null;
    try { player.pause(); } catch (e) { /* */ }
    if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    if (voiceOrb) voiceOrb.classList.remove("is-speaking");
    showStopSpeak(false);
  }

  async function speak(text) {
    if (!voiceEnabled) { maybeAutoListen(); return; }

    cutSpeech();
    setBusy(true);

    let url;
    try {
      const res = await fetch("/api/tts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      if (!res.ok) throw new Error("tts request failed");
      url = URL.createObjectURL(await res.blob());
    } catch (err) {
      // Server TTS ishlamadi — brauzer ovoziga o'tamiz (sayt "soqov" qolmasin)
      speakWithBrowserFallback(text);
      return;
    }

    player.onplay = () => { if (voiceOrb) voiceOrb.classList.add("is-speaking"); setOrbLabel("Gapiryapman..."); showStopSpeak(true); };
    player.onended = () => {
      if (voiceOrb) voiceOrb.classList.remove("is-speaking");
      showStopSpeak(false);
      URL.revokeObjectURL(url);
      maybeAutoListen();
    };
    player.onerror = () => { showStopSpeak(false); speakWithBrowserFallback(text); };
    player.src = url;
    try {
      await player.play();
    } catch (playErr) {
      // Avtoplay bloklandi — keyingi bosishda qayta uramiz, oraliqda mikrofon bo'sh qolmasin
      pendingAudioRetry = player;
      setBusy(false);
    }
  }

  function updateVoiceToggleUI() {
    if (!voiceToggleBtn) return;
    voiceToggleBtn.classList.toggle("voice-on", voiceEnabled);
    voiceToggleBtn.setAttribute("aria-pressed", voiceEnabled ? "true" : "false");
    voiceToggleBtn.title = voiceEnabled ? "Ovozni o'chirish (gapirish va eshitish)" : "Ovozni yoqish (gapirish va eshitish)";
  }
  updateVoiceToggleUI();
  setOrbLabel(STATUS_IDLE);

  if (voiceToggleBtn) {
    voiceToggleBtn.addEventListener("click", () => {
      voiceEnabled = !voiceEnabled;
      localStorage.setItem(VOICE_PREF_KEY, voiceEnabled ? "1" : "0");
      updateVoiceToggleUI();
      if (!voiceEnabled) {
        cutSpeech();
        maybeAutoListen();
      }
    });
  }

  function clearEmptyState() {
    const empty = document.getElementById("floating-chat-empty");
    if (empty) empty.remove();
  }

  function addUserMessage(text) {
    clearEmptyState();
    const bubble = document.createElement("div");
    bubble.className = "chat-msg chat-msg-user";
    bubble.style.maxWidth = "85%";
    bubble.style.fontSize = "0.85rem";
    bubble.textContent = text;
    messages.appendChild(bubble);
    messages.scrollTop = messages.scrollHeight;
  }

  function showThinking() {
    clearEmptyState();
    const bubble = document.createElement("div");
    bubble.className = "owl-thinking-bubble";
    bubble.id = "owl-thinking-indicator";
    bubble.innerHTML = '<img src="/static/logo-owl.png" alt=""><span>LongoAI o\'ylamoqda...</span>';
    messages.appendChild(bubble);
    messages.scrollTop = messages.scrollHeight;

    if (pinButton) pinButton.classList.add("owl-thinking");
    setOrbLabel("O'ylayapman...");
  }

  function removeThinking() {
    const el = document.getElementById("owl-thinking-indicator");
    if (el) el.remove();
    if (pinButton) pinButton.classList.remove("owl-thinking");
  }

  // Javobni typewriter effektida (birma-bir harf) yozadi, tugagach —
  // ovoz yoqilgan bo'lsa, baland ovozda o'qib beradi.
  function typewriteAnswer(fullText, opts) {
    const bubble = document.createElement("div");
    bubble.className = "chat-msg chat-msg-ai";
    bubble.style.maxWidth = "85%";
    bubble.style.fontSize = "0.85rem";
    messages.appendChild(bubble);

    let i = 0;
    const speed = 14; // ms har harf uchun — tezroq javob berish taassuroti

    function step() {
      if (i < fullText.length) {
        bubble.textContent += fullText[i];
        i++;
        messages.scrollTop = messages.scrollHeight;
        setTimeout(step, speed);
      } else if (opts && opts.silent) {
        maybeAutoListen();
      } else {
        speak(fullText);
      }
    }
    step();
  }

  // Markazlashtirilgan yuborish funksiyasi — forma orqali ham, tashqaridan
  // (masalan "AI'dan so'rash" tugmasi) ham shu orqali yuboriladi.
  const chatHistory = [];
  async function sendQuestion(question) {
    if (!question) return;

    if (isListening) stopListening();
    setInterim("");
    addUserMessage(question);
    sendBtn.disabled = true;
    setBusy(true);
    showThinking();

    try {
      // "source" — serverga qaysi suhbat ekanini aytadi: /repetitor sahifasidagi
      // to'liq AI repetitor ("owl-voice-orb" faqat shu sahifada bor) Claude
      // orqali ishlaydi, boshqa barcha sahifalardagi suzuvchi tezkor chat esa
      // Gemini orqali — ikkalasi ATAYLAB ALOHIDA AI provayderga bog'langan.
      const source = document.getElementById("owl-voice-orb") ? "repetitor" : "widget";
      const res = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question, effort: currentEffort, source,
          history: chatHistory.slice(-10),
          lang: (langSelect && langSelect.value) || "uz-UZ",
        }),
      });

      removeThinking();

      if (res.status === 402) {
        // Kunlik AI limiti tugadi — oddiy javob o'rniga Pro/Ultra taklifini
        // ko'rsatamiz (AI'ga umuman so'rov yuborilmagan, hech narsa
        // sarflanmagan).
        const data = await res.json();
        showLimitReachedCard(data);
        liveMode = false;
        maybeAutoListen();
        return;
      }

      if (res.status === 401) {
        typewriteAnswer("Sessiya tugagan. Iltimos, qayta kiring.", { silent: true });
        return;
      }
      if (!res.ok) {
        typewriteAnswer("Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.", { silent: true });
        return;
      }

      const data = await res.json();
      if (data.provider && data.provider !== "none") {
        chatHistory.push({ role: "user", text: question }, { role: "assistant", text: data.answer });
        if (chatHistory.length > 20) chatHistory.splice(0, chatHistory.length - 20);
      }
      typewriteAnswer(data.answer);
      if (data.usage) updateUsageIndicator(data.usage);
    } catch (err) {
      removeThinking();
      typewriteAnswer("Internet aloqasida muammo bo'ldi. Qayta urinib ko'ring.", { silent: true });
    } finally {
      sendBtn.disabled = false;
    }
  }

  // ==========================================================================
  // "REJIM" (AI javob chuqurligi) — Claude'ning o'z UI'sidagi kabi kompakt
  // pill-tugma + popover. Oddiy/Chuqur o'ylab barcha tariflarda BEPUL va
  // ochiq, Maksimal esa faqat Pro/Ultra'da ishlaydi (bepul tarifda tugma
  // "qulflangan" ko'rinishda turadi, bosilsa qisqa eslatma chiqadi, server
  // ham buni alohida tekshiradi). Tanlov localStorage'da saqlanadi —
  // foydalanuvchi bir marta tanlasa, boshqa sahifalarda ham o'sha daraja
  // qo'llanadi.
  // ==========================================================================
  const EFFORT_PREF_KEY = "longouz_effort_pref";
  const effortRow = document.getElementById("owl-effort-row");
  const modeBtn = document.getElementById("owl-mode-btn");
  const modeBtnLabel = document.getElementById("owl-mode-btn-label");
  const modePopover = document.getElementById("owl-mode-popover");
  const effortButtons = effortRow ? effortRow.querySelectorAll(".owl-effort-btn") : [];
  let currentEffort = localStorage.getItem(EFFORT_PREF_KEY) || "normal";
  let currentPlan = null; // /api/usage javobidan keladi ("free" | "pro" | "ultra")

  function closeModePopover() {
    if (!modePopover || !effortRow) return;
    modePopover.hidden = true;
    effortRow.classList.remove("is-open");
    if (modeBtn) modeBtn.setAttribute("aria-expanded", "false");
  }
  function openModePopover() {
    if (!modePopover || !effortRow) return;
    modePopover.hidden = false;
    effortRow.classList.add("is-open");
    if (modeBtn) modeBtn.setAttribute("aria-expanded", "true");
  }
  if (modeBtn) {
    modeBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      if (modePopover && modePopover.hidden) openModePopover(); else closeModePopover();
    });
    document.addEventListener("click", (e) => {
      if (modePopover && !modePopover.hidden && !effortRow.contains(e.target)) closeModePopover();
    });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeModePopover(); });
  }

  function updateEffortUI() {
    effortButtons.forEach((btn) => {
      const eff = btn.dataset.effort;
      const isActive = eff === currentEffort;
      btn.classList.toggle("is-active", isActive);
      btn.classList.toggle("is-locked", eff === "max" && currentPlan === "free");
      if (isActive && modeBtnLabel) modeBtnLabel.textContent = btn.dataset.label || "Oddiy";
    });
  }

  function showEffortUpsell() {
    if (!modePopover) return;
    let note = modePopover.querySelector(".owl-effort-note");
    if (!note) {
      note = document.createElement("div");
      note.className = "owl-effort-note";
      modePopover.appendChild(note);
    }
    note.textContent = "Maksimal rejim faqat Pro/Ultra tarifida ochiladi.";
    clearTimeout(showEffortUpsell._timer);
    showEffortUpsell._timer = setTimeout(() => { if (note) note.remove(); }, 3500);
  }

  effortButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const eff = btn.dataset.effort;
      if (eff === "max" && currentPlan === "free") {
        showEffortUpsell();
        return;
      }
      currentEffort = eff;
      localStorage.setItem(EFFORT_PREF_KEY, eff);
      updateEffortUI();
      closeModePopover();
    });
  });
  updateEffortUI();

  // ==========================================================================
  // LIMIT KO'RSATKICHI — chat inputi ustidagi progress-bar. /api/usage'dan
  // (sahifa ochilganda) va har bir muvaffaqiyatli /api/ask javobidan keyin
  // yangilanadi — foydalanuvchi limitga necha savol qolganini oldindan ko'radi.
  // ==========================================================================
  const usageIndicator = document.getElementById("owl-usage-indicator");
  const usageBarFill = document.getElementById("owl-usage-bar-fill");
  const usageText = document.getElementById("owl-usage-text");

  function updateUsageIndicator(usage) {
    if (!usageIndicator || !usageBarFill || !usageText) return;
    if (usage.limit === null || usage.limit === undefined) {
      // Ultra — cheksiz: ko'rsatkichni yashiramiz, band qilib turmasin.
      usageIndicator.hidden = true;
      return;
    }
    const percent = usage.limit > 0 ? Math.min(100, Math.round((usage.used / usage.limit) * 100)) : 100;
    usageIndicator.hidden = false;
    usageBarFill.style.width = percent + "%";
    usageBarFill.classList.toggle("is-warning", percent >= 70 && percent < 100);
    usageBarFill.classList.toggle("is-danger", percent >= 100);
    const windowLabel = usage.window_hours ? `so'nggi ${usage.window_hours} soatda` : "";
    usageText.textContent = `${usage.used}/${usage.limit} savol ${windowLabel}`;
  }

  // Sahifa ochilganda joriy holatni bir marta yuklaymiz (hali hech narsa
  // yozmagan bo'lsa ham, foydalanuvchi darhol necha savol qolganini ko'rsin).
  fetch("/api/usage").then((r) => (r.ok ? r.json() : null)).then((data) => {
    if (data) {
      updateUsageIndicator(data);
      currentPlan = data.plan || null;
      // Foydalanuvchi bepul tarifda bo'lib, ilgari "max" tanlagan bo'lsa
      // (masalan Pro'dan chiqib ketgan bo'lsa), avtomatik "Yuqori"ga
      // qaytaramiz — qulflangan darajada qolib ketmasin.
      if (currentPlan === "free" && currentEffort === "max") {
        currentEffort = "high";
        localStorage.setItem(EFFORT_PREF_KEY, "high");
      }
      updateEffortUI();
    }
  }).catch(() => {});

  // ==========================================================================
  // LIMIT TUGAGANDA — TO'LIQ BLOKLOVCHI modal. Faqat "Pro/Ultra'ga o'tish"
  // yoki "Bekor qilish" tugmasi bosilgandagina yopiladi (orqa fonga bosish
  // yoki Esc bilan yopilmaydi) — aniq so'ralganidek: "hech narsa qilolmasin".
  //
  // Ichida JONLI SANOQ bor: sirpanuvchi oyna (3/5 soat) qachon ochilishini
  // soniyama-soniya orqaga sanab ko'rsatadi. Vaqt tugagach modal AVTOMATIK
  // yopiladi va chat qayta yoziladigan holatga o'zi qaytadi — sahifani
  // qo'lda yangilash SHART EMAS ("soatga qarab orqaga ketaveradi, o'zi
  // ochiladi" degan talab shu yerda bajariladi).
  // ==========================================================================
  let limitCountdownTimer = null;

  function formatCountdown(totalSeconds) {
    const h = Math.floor(totalSeconds / 3600);
    const m = Math.floor((totalSeconds % 3600) / 60);
    const s = totalSeconds % 60;
    const pad = (n) => String(n).padStart(2, "0");
    return h > 0 ? `${h}:${pad(m)}:${pad(s)}` : `${m}:${pad(s)}`;
  }

  async function unlockAfterCountdown(overlay) {
    // Vaqt tugagach — mijoz soati bilan serverniki bir oz farq qilishi
    // mumkinligi uchun, faqat lokal taymerga ishonmasdan, serverdan haqiqiy
    // holatni qayta so'raymiz (limit chindan ham ochilganini tasdiqlaymiz).
    try {
      const r = await fetch("/api/usage");
      if (r.ok) {
        const data = await r.json();
        updateUsageIndicator(data);
      }
    } catch (err) { /* internet vaqtincha yo'q bo'lsa ham — modalni baribir yopamiz */ }
    overlay.remove();
  }

  function showLimitReachedCard(data) {
    if (data.usage) updateUsageIndicator(data.usage);
    else updateUsageIndicator({ used: data.used, limit: data.limit, window_hours: data.window_hours });

    const overlay = document.createElement("div");
    overlay.className = "owl-limit-modal-overlay";
    const hasCountdown = typeof data.retry_after_seconds === "number" && data.retry_after_seconds > 0;
    overlay.innerHTML = `
      <div class="owl-limit-modal-card">
        <p class="owl-limit-title">AI suhbat limiti tugadi</p>
        <p class="owl-limit-sub">${data.message || `${data.used}/${data.limit} ta savol ishlatildi.`}</p>
        ${hasCountdown ? `<p class="owl-limit-countdown" aria-live="polite"><span class="owl-limit-countdown-num">${formatCountdown(data.retry_after_seconds)}</span><span class="owl-limit-countdown-label">dan keyin avtomatik ochiladi</span></p>` : ""}
        <div class="owl-limit-actions">
          <a href="/upgrade?plan=pro&amp;auto=1" class="btn-primary">Pro/Ultra'ga o'tish</a>
          <button type="button" class="btn-secondary owl-limit-dismiss">Bekor qilish</button>
        </div>
      </div>
    `;
    document.body.appendChild(overlay);
    overlay.querySelector(".owl-limit-dismiss").addEventListener("click", () => {
      clearInterval(limitCountdownTimer);
      overlay.remove();
    });

    if (hasCountdown) {
      let remaining = data.retry_after_seconds;
      const numEl = overlay.querySelector(".owl-limit-countdown-num");
      clearInterval(limitCountdownTimer);
      limitCountdownTimer = setInterval(() => {
        remaining -= 1;
        if (remaining <= 0) {
          clearInterval(limitCountdownTimer);
          unlockAfterCountdown(overlay);
          return;
        }
        if (numEl) numEl.textContent = formatCountdown(remaining);
      }, 1000);
    }
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const question = input.value.trim();
    if (!question) return;
    input.value = "";
    sendQuestion(question).finally(() => input.focus());
  });

  // ---------- Tashqi (dasturiy) API — boshqa sahifalar shu orqali chatni
  //            ochib, tayyor savol bilan AI'dan so'rashi mumkin ----------
  window.LongoUZChat = {
    ask: function (question) {
      if (chatWidget && !chatWidget.classList.contains("chat-widget-open")) {
        chatWidget.classList.add("chat-widget-open");
      }
      sendQuestion(question);
    },
  };
})();
