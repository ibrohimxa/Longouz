// ============================================================================
// LongoUZ — test yechish sahifasi mantiqi
// - /api/quiz/generate orqali savollarni yuklaydi (DTM yoki Sertifikat rejimi)
// - Taymer: rejimga qarab belgilangan vaqt ichida sanaladi, tugasa avto-topshiradi
// - Har 10 soniyada joriy javoblar /api/quiz/autosave orqali XOTIRAGA (kesh)
//   yoziladi — DB'ga EMAS. Test yakunlanganda BITTA /api/quiz/submit so'rovi
//   bilan bazaga yoziladi (batch write).
// ============================================================================

(function () {
  const body = document.body;
  const subject = body.dataset.subject;
  const level = body.dataset.level;
  const mode = body.dataset.mode || "dtm";
  const topic = body.dataset.topic || null;
  let topicsGroup = null;
  if (body.dataset.topics) {
    try { topicsGroup = JSON.parse(body.dataset.topics); } catch (e) { topicsGroup = null; }
    if (topicsGroup && !topicsGroup.length) topicsGroup = null;
  }
  const missedMode = body.dataset.missedMode === "true";
  const questionCount = parseInt(body.dataset.questionCount, 10) || 10;
  let timeLimitMinutes = parseInt(body.dataset.timeLimitMinutes, 10) || 30;
  const attemptToken = body.dataset.attemptToken;
  const variant = body.dataset.variant || "main";
  const checkpointMode = body.dataset.checkpoint === "true";
  const drillKind = body.dataset.drill || "";
  const blockSpecs = body.dataset.block || "";           // DTM blok mock: "physics,chemistry"
  const adaptiveMode = body.dataset.adaptive === "true"; // AI-adaptiv test
  let adaptiveTotal = questionCount;

  const loadingEl = document.getElementById("quiz-loading");
  const errorEl = document.getElementById("quiz-error");
  const errorTextEl = document.getElementById("quiz-error-text");
  const bodyEl = document.getElementById("quiz-body");
  const resultEl = document.getElementById("quiz-result");

  const progressFill = document.getElementById("quiz-progress-fill");
  const progressLabel = document.getElementById("quiz-progress-label");
  const questionTextEl = document.getElementById("quiz-question-text");
  const optionsEl = document.getElementById("quiz-options");
  const prevBtn = document.getElementById("quiz-prev-btn");
  const nextBtn = document.getElementById("quiz-next-btn");
  const finishBtn = document.getElementById("quiz-finish-btn");
  const timerEl = document.getElementById("quiz-timer");

  let questions = [];
  let currentIndex = 0;
  let answers = {}; // { questionIndex: selectedOptionIndex }
  let remainingSeconds = timeLimitMinutes * 60;
  const paletteEl = document.getElementById("quiz-palette");
  const sectionEl = document.getElementById("quiz-section-label");
  const navBtn = document.getElementById("quiz-nav-btn");
  const navPosEl = document.getElementById("quiz-nav-pos");
  const navCountEl = document.getElementById("lz-nav-count");
  const navSheet = document.getElementById("lz-nav-sheet");
  const navFinishBtn = document.getElementById("lz-nav-finish");
  let timerHandle = null;
  let autosaveHandle = null;
  let startedAt = Date.now();
  let submitted = false;

  // ---------- v229: yuklanish ekrani (boyqush + yashil aylanuvchi halqa) ----------
  const loaderEl = document.getElementById("lz-loader");
  const loaderShownAt = Date.now();
  const Loader = {
    set(title, sub, note) {
      if (!loaderEl) return;
      const t = document.getElementById("lz-loader-title");
      const s = document.getElementById("lz-loader-sub");
      const n = document.getElementById("lz-loader-note");
      if (t) t.textContent = title;
      if (s) s.textContent = sub;
      if (n) n.hidden = !note;
    },
    show(kind) {
      if (!loaderEl) return;
      if (kind === "submit") {
        Loader.set("Natijalar hisoblanmoqda va yuborilmoqda…", "Javoblaringiz tahlil qilinmoqda…", true);
      }
      loaderEl.classList.remove("is-done", "is-hiding");
      loaderEl.hidden = false;
      document.body.classList.add("is-loading");
      Loader.since = Date.now();
    },
    hide(minMs) {
      return new Promise((resolve) => {
        if (!loaderEl) { resolve(); return; }
        const since = Loader.since || loaderShownAt;
        const wait = Math.max(0, (minMs || 0) - (Date.now() - since));
        setTimeout(() => {
          loaderEl.classList.add("is-hiding");
          document.body.classList.remove("is-loading");
          setTimeout(() => { loaderEl.hidden = true; loaderEl.classList.remove("is-hiding"); resolve(); }, 360);
        }, wait);
      });
    },
    done() {
      if (loaderEl) loaderEl.classList.add("is-done");
      return new Promise((r) => setTimeout(r, 620));
    },
  };

  function answeredCount() {
    let n = 0;
    Object.keys(answers).forEach((k) => { const v = answers[k]; if (v !== undefined && v !== "") n++; });
    return n;
  }

  function formatTime(totalSeconds) {
    const m = Math.max(0, Math.floor(totalSeconds / 60));
    const s = Math.max(0, totalSeconds % 60);
    return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
  }

  function startTimer() {
    timerEl.textContent = formatTime(remainingSeconds);
    timerHandle = setInterval(() => {
      remainingSeconds--;
      timerEl.textContent = formatTime(remainingSeconds);
      if (remainingSeconds <= 60) timerEl.classList.add("quiz-timer-warning");
      if (remainingSeconds <= 0) {
        clearInterval(timerHandle);
        finishQuiz(); // vaqt tugadi — avtomatik topshiriladi
      }
    }, 1000);
  }

  // ---------- 10 soniyalik avtosaqlash (faqat xotiraga, DB'ga emas) ----------
  // Qo'shimcha: joriy attempt_token va URL ni localStorage ga yozamiz —
  // foydalanuvchi tasodifan chiqib qayta kirsa, uni shu testga qaytaramiz.
  function _saveAttemptRef() {
    if (!attemptToken) return;
    try {
      localStorage.setItem("lz_active_attempt", JSON.stringify({
        token: attemptToken,
        url: window.location.href,
        ts: Date.now(),
      }));
    } catch (e) { /* xotira to'la bo'lsa e'tiborsiz */ }
  }
  function _clearAttemptRef() {
    try { localStorage.removeItem("lz_active_attempt"); } catch (e) {}
  }

  function startAutosave() {
    _saveAttemptRef(); // Darhol yozib qo'yamiz
    autosaveHandle = setInterval(() => {
      if (submitted) return;
      _saveAttemptRef();
      fetch("/api/quiz/autosave", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          attempt_token: attemptToken,
          answers: answers,
          current_index: currentIndex,
          remaining_seconds: remainingSeconds,
        }),
      }).catch(() => {}); // autosave muvaffaqiyatsiz bo'lsa ham testni to'xtatmaymiz
    }, 10000);
  }

  // Tashqi vositalar (shikoyat, kalkulyator) uchun joriy holat
  Object.defineProperty(window, "LZQuiz", { configurable: true, get() {
    return { index: currentIndex, question: questions[currentIndex] || null, answer: answers[currentIndex], token: attemptToken };
  } });

  let renderedIndex = -1;
  function renderQuestion() {
    const q = questions[currentIndex];
    questionTextEl.textContent = q.question;
    if (renderedIndex !== currentIndex) {
      const card = document.querySelector(".quiz-question-card");
      if (card) { card.classList.remove("qz-swap"); void card.offsetWidth; card.classList.add("qz-swap"); }
      renderedIndex = currentIndex;
    }
    optionsEl.innerHTML = "";
    if (window.LZFigure) window.LZFigure.fillQuestion(document.getElementById("quiz-qfig"), q.figure);
    if (window.LZQuizStyle) window.LZQuizStyle.applyQuestion(document, q.style);
    if (sectionEl) {
      if (q.section) { sectionEl.textContent = q.section; sectionEl.hidden = false; }
      else { sectionEl.hidden = true; }
    }
    renderPalette();
    try { window.dispatchEvent(new CustomEvent("lz:question")); } catch (e) {}

    if (q.type === "open") {
      const wrap = document.createElement("div");
      wrap.className = "quiz-open-answer";
      const lab = document.createElement("label");
      lab.textContent = "Javobingizni yozing (ochiq savol)";
      const inp = document.createElement("input");
      inp.type = "text";
      inp.autocomplete = "off";
      inp.spellcheck = false;
      const _ph = { math: "Masalan: 12 yoki 3/4 yoki √2", physics: "Masalan: 2,5 yoki 3·10⁸", chemistry: "Masalan: 22,4 yoki H₂SO₄", biology: "Masalan: 25 yoki Aa" };
      inp.placeholder = mode === "ielts" ? "TRUE / FALSE / NOT GIVEN yoki 1–2 so'z" : (_ph[subject] || "Masalan: 1370 yoki Amir Temur");
      inp.value = typeof answers[currentIndex] === "string" ? answers[currentIndex] : "";
      inp.addEventListener("input", () => {
        const v = inp.value.trim();
        if (v) answers[currentIndex] = inp.value; else delete answers[currentIndex];
        updatePaletteState();
      });
      inp.addEventListener("keydown", (e) => {
        if (e.key === "Enter") { e.preventDefault(); if (adaptiveMode) { nextBtn.click(); } else if (currentIndex < questions.length - 1) { currentIndex++; renderQuestion(); } }
      });
      const hint = document.createElement("span");
      hint.className = "quiz-open-hint";
      const _hint = { math: "Faqat javobni yozing (son, kasr yoki ifoda). Vergul va nuqta farqi yo'q.", physics: "Sonni yozing; 10ⁿ uchun belgilar tugmalaridan foydalaning. Birlik shart emas.", chemistry: "Son yoki formulani yozing; indeks va zaryad uchun belgilar tugmalari bor.", biology: "Son, genotip yoki atamani qisqa yozing." };
      hint.textContent = mode === "ielts" ? "IELTS: TRUE / FALSE / NOT GIVEN yoki matndagi so'z(lar)ni yozing. Katta-kichik harf farqi yo'q." : (_hint[subject] || "Yil, nom yoki atamani qisqa yozing. Katta-kichik harf va apostrof farqi hisobga olinmaydi.");
      wrap.append(lab, inp, hint);
      optionsEl.appendChild(wrap);
      if (window.LZTools) { try { window.LZTools.decorateOpenInput(wrap, inp); } catch (e) {} }
      // Telefonda klaviatura o'zi ochilib, ekranni yopmasin — faqat kompyuterda avtomatik fokus
      if (!(window.matchMedia && matchMedia("(pointer: coarse)").matches)) setTimeout(() => { try { inp.focus(); } catch (e) {} }, 30);
    }

    (q.type === "open" ? [] : q.options).forEach((optionText, idx) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "quiz-option";
      if (answers[currentIndex] === idx) btn.classList.add("selected");
      const key = document.createElement("span");
      key.className = "quiz-option-key";
      key.textContent = "ABCD"[idx] || String(idx + 1);
      const label = document.createElement("span");
      label.className = "quiz-option-text";
      label.textContent = optionText;
      const optFig = window.LZFigure ? window.LZFigure.optionFigure(q.figure, idx) : null;
      if (optFig) {
        const bodyBox = document.createElement("span");
        bodyBox.className = "quiz-option-body";
        bodyBox.append(label, optFig);
        btn.append(key, bodyBox);
      } else {
        btn.append(key, label);
      }
      btn.addEventListener("click", () => {
        answers[currentIndex] = idx;
        renderQuestion();
      });
      optionsEl.appendChild(btn);
    });

    const shownTotal = adaptiveMode ? adaptiveTotal : questions.length;
    progressFill.style.width = `${((currentIndex + 1) / shownTotal) * 100}%`;
    progressLabel.textContent = `${currentIndex + 1} / ${shownTotal} savol` + (adaptiveMode ? " · AI qiyinlikni moslaydi" : "");
    if (navPosEl) navPosEl.textContent = `${currentIndex + 1} / ${shownTotal}`;

    prevBtn.disabled = currentIndex === 0;
    if (adaptiveMode) prevBtn.style.display = "none";
    const isLast = adaptiveMode ? currentIndex + 1 >= adaptiveTotal : currentIndex === questions.length - 1;
    nextBtn.style.display = isLast ? "none" : "inline-flex";
    finishBtn.style.display = isLast ? "inline-flex" : "none";
    resetFinishConfirm();
    if (!adaptiveMode && window.innerWidth <= 760 && renderedScroll !== currentIndex) {
      renderedScroll = currentIndex;
      const card = document.querySelector(".quiz-question-card");
      if (card && card.getBoundingClientRect().top < 0) window.scrollTo({ top: 0, behavior: "smooth" });
    }
  }
  let renderedScroll = 0;

  // Savollar ro'yxati endi doim ko'rinib turmaydi: pastdagi "1 / 30" tugmasi bosilganda
  // panel ochiladi (raqamni bossangiz — o'sha savolga o'tadi va panel yopiladi).
  function renderPalette() {
    if (!paletteEl) return;
    if (adaptiveMode || questions.length < 2) {
      paletteEl.innerHTML = "";
      if (navBtn) navBtn.classList.add("is-static");
      return;
    }
    if (paletteEl.childElementCount !== questions.length) {
      paletteEl.innerHTML = "";
      questions.forEach((_, i) => {
        const b = document.createElement("button");
        b.type = "button";
        b.textContent = String(i + 1);
        b.setAttribute("aria-label", `${i + 1}-savol`);
        b.addEventListener("click", () => {
          currentIndex = i; renderQuestion();
          if (window.LZSheet) window.LZSheet.close("nav");
        });
        paletteEl.appendChild(b);
      });
    }
    updatePaletteState();
  }

  function updatePaletteState() {
    if (!paletteEl) return;
    Array.from(paletteEl.children).forEach((b, i) => {
      b.classList.toggle("is-answered", answers[i] !== undefined && answers[i] !== "");
      b.classList.toggle("is-current", i === currentIndex);
    });
    if (navCountEl) navCountEl.textContent = `Javob berilgan: ${answeredCount()} / ${questions.length}`;
  }

  // Yakunlash: javobsiz savollar bo'lsa — bir marta ogohlantiramiz (tasodifiy bosishdan himoya)
  let finishArmed = 0;
  function resetFinishConfirm() {
    finishArmed = 0;
    finishBtn.classList.remove("is-armed");
    finishBtn.textContent = "Yakunlash";
    if (navFinishBtn) { navFinishBtn.classList.remove("is-armed"); navFinishBtn.textContent = "Testni yakunlash"; }
  }
  function requestFinish(btn) {
    const total = adaptiveMode ? adaptiveTotal : questions.length;
    const empty = Math.max(0, total - answeredCount());
    if (empty > 0 && !adaptiveMode && Date.now() - finishArmed > 4000) {
      finishArmed = Date.now();
      btn.classList.add("is-armed");
      btn.textContent = `${empty} ta savol javobsiz — yakunlash uchun yana bosing`;
      setTimeout(() => { if (Date.now() - finishArmed >= 3900) resetFinishConfirm(); }, 4000);
      return;
    }
    if (window.LZSheet) window.LZSheet.closeAll();
    finishQuiz();
  }

  if (navSheet && window.LZSheet) {
    window.LZSheet.register("nav", navSheet, { button: navBtn, half: true, onOpen: () => { renderPalette(); resetFinishConfirm(); } });
  }
  if (navFinishBtn) navFinishBtn.addEventListener("click", () => requestFinish(navFinishBtn));

  prevBtn.addEventListener("click", () => {
    if (currentIndex > 0) {
      currentIndex--;
      renderQuestion();
    }
  });

  let adaptiveBusy = false;
  nextBtn.addEventListener("click", () => {
    if (adaptiveMode && currentIndex === questions.length - 1) {
      if (adaptiveBusy) return;
      const a = answers[currentIndex];
      if (a === undefined || a === "") { progressLabel.textContent = "Avval javob tanlang — keyingi savol shunga qarab tanlanadi"; return; }
      adaptiveBusy = true;
      fetch("/api/adaptive/next", {
        method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ attempt_token: attemptToken, index: currentIndex, answer: a }),
      }).then((r) => r.json().then((j) => { if (!r.ok) throw new Error(j.detail || "Keyingi savol yuklanmadi"); return j; }))
        .then((j) => {
          if (j.done) { finishQuiz(); return; }
          questions.push(j.question); currentIndex++; renderQuestion();
        })
        .catch((e) => { progressLabel.textContent = e.message; })
        .finally(() => { adaptiveBusy = false; });
      return;
    }
    if (currentIndex < questions.length - 1) {
      currentIndex++;
      renderQuestion();
    }
  });

  finishBtn.addEventListener("click", () => requestFinish(finishBtn));

  function finishQuiz() {
    if (submitted) return;
    submitted = true;
    try { window.dispatchEvent(new CustomEvent("lz:finished")); } catch (e) {}
    clearInterval(timerHandle);
    clearInterval(autosaveHandle);
    _clearAttemptRef(); // test yakunlandi — active attempt tozalanadi
    if (window.LZSheet) window.LZSheet.closeAll();

    const timeSpentSeconds = Math.round((Date.now() - startedAt) / 1000);

    // XAVFSIZLIK: bu yerda ENDI "necha ta to'g'ri" hisoblanmaydi va
    // serverga yuborilmaydi — faqat foydalanuvchi TANLAGAN variantlar
    // (answers) yuboriladi. Nechta to'g'ri ekanini SERVER o'zi, o'zida
    // saqlangan asl javoblar bilan solishtirib hisoblaydi.
    lastPayload = {
      topic: topic,
      attempt_token: attemptToken,
      answers: answers,
      time_spent_seconds: timeSpentSeconds,
    };
    sendResult();
  }

  // v229: natija yuborilmasa (internet uzilsa) javoblar YO'QOLMAYDI — "Qayta yuborish" tugmasi chiqadi
  let lastPayload = null;
  function sendResult() {
    if (!lastPayload) return;
    Loader.show("submit");
    resultEl.style.display = "none";
    try { localStorage.setItem("lz_pending_submit", JSON.stringify({ p: lastPayload, ts: Date.now() })); } catch (e) {}
    fetch("/api/quiz/submit", {
      method: "POST",
      credentials: "same-origin",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(lastPayload),
    })
      .then(async (res) => {
        if (!res.ok) {
          const err = await res.json().catch(() => ({}));
          const e = new Error(err.detail || "Natijani saqlab bo'lmadi.");
          e.status = res.status;
          throw e;
        }
        return res.json();
      })
      .then(async (data) => {
        try { localStorage.removeItem("lz_pending_submit"); } catch (e) {}
        // Avval yuklanish ekranida "✓" ko'rinadi, so'ng natija oynasi (ball, to'g'ri/xato/javobsiz) ochiladi.
        const wait = Math.max(0, 1100 - (Date.now() - (Loader.since || Date.now())));
        await new Promise((r) => setTimeout(r, wait));
        await Loader.done();
        showCelebration(data);
        await Loader.hide(0);
      })
      .catch(async (err) => {
        // Tarmoq/server xatosi — soxta ball ko'rsatmaymiz, chunki haqiqiy natijani FAQAT server biladi.
        await Loader.hide(400);
        if (err && err.status === 409) {
          try { localStorage.removeItem("lz_pending_submit"); } catch (e) {}
          showSubmitError("Bu test natijasi allaqachon saqlangan bo'lishi mumkin. Kabinetdagi natijalar tarixidan tekshiring.", false);
        } else {
          showSubmitError((err && err.message && err.message !== "Failed to fetch") ? err.message : "Internet aloqasi uzildi. Javoblaringiz saqlanib turibdi — internet tiklangach «Qayta yuborish» tugmasini bosing.", true);
        }
      });
  }

  function showSubmitError(message, canRetry) {
    bodyEl.style.display = "none";
    resultEl.style.display = "block";
    document.getElementById("quiz-result-title").textContent = "Natijani saqlashda xatolik";
    document.getElementById("quiz-result-detail").textContent =
      message || "Internet aloqasida muammo bo'ldi. Qayta urinib ko'ring.";
    const review = document.getElementById("quiz-review-link");
    let retry = document.getElementById("quiz-retry-submit");
    if (canRetry) {
      if (!retry) {
        retry = document.createElement("button");
        retry.type = "button";
        retry.id = "quiz-retry-submit";
        retry.className = "btn-primary";
        retry.textContent = "Qayta yuborish";
        retry.addEventListener("click", sendResult);
        review.parentNode.insertBefore(retry, review);
      }
      retry.style.display = "";
    } else if (retry) {
      retry.style.display = "none";
    }
    review.href = "/dashboard";
    review.textContent = "Kabinetga qaytish";
    review.style.display = canRetry ? "none" : "";
  }

  // ==========================================================================
  // TABRIKLASH OYNASI — kubok + konfetti. Natija foizga qarab 3 darajaga
  // bo'linadi: a'lo (>=85%) — oltin kubok, tez aylanadi, konfetti ko'p;
  // yaxshi (>=60%) — yashil kubok, sekin "nafas oladi", konfetti o'rtacha;
  // past (<60%) — kulrang kubok, harakatsiz, konfetti yo'q (charchatmaslik
  // uchun) — lekin baribir rag'batlantiruvchi matn bilan.
  // ==========================================================================
  function showCelebration(data) {
    bodyEl.style.display = "none";

    const overlay = document.getElementById("quiz-celebrate-overlay");
    const stage = document.getElementById("quiz-trophy-stage");
    const titleEl = document.getElementById("quiz-celebrate-title");
    const detailEl = document.getElementById("quiz-celebrate-detail");
    const confettiField = document.getElementById("quiz-confetti-field");

    const result = data.result || {};
    const correctCount = result.correct;
    const total = result.total;
    const percent = typeof result.percent === "number" ? result.percent : (total ? Math.round((correctCount / total) * 100) : 0);

    let tier = "low";
    if (percent >= 85) tier = "high";
    else if (percent >= 60) tier = "mid";
    stage.className = "quiz-trophy-stage quiz-trophy-" + tier;

    titleEl.textContent = result.label || `${correctCount} / ${total}`;
    // v229: to'g'ri / xato / javobsiz — rangli nuqtalar bilan (aniq raqamlar)
    try {
      const answered = typeof result.answered === "number" ? result.answered : answeredCount();
      const wrong = typeof result.wrong === "number" ? result.wrong : Math.max(0, answered - (correctCount || 0));
      const skipped = typeof result.skipped === "number" ? result.skipped : Math.max(0, (total || 0) - answered);
      const st = document.getElementById("quiz-score-stats");
      if (st && typeof correctCount === "number") {
        document.getElementById("qs-ok").textContent = correctCount;
        document.getElementById("qs-bad").textContent = wrong;
        document.getElementById("qs-skip").textContent = skipped;
        st.hidden = false;
      }
      const kicker = document.getElementById("quiz-celebrate-kicker");
      if (kicker) kicker.textContent = percent >= 85 ? "Ajoyib natija!" : percent >= 60 ? "Yaxshi natija" : "Natija";
    } catch (e) {}
    if (result.mode === "certificate" || result.mode === "cefr") {
      detailEl.textContent = `${correctCount} / ${total} to'g'ri javob (${percent}%) — erishilgan daraja: ${result.band}`;
    } else if (result.mode === "ielts") {
      detailEl.textContent = `${correctCount} / ${total} to'g'ri javob (${percent}%) — taxminiy Band: ${result.band_score}`;
    } else {
      detailEl.textContent = `${correctCount} / ${total} to'g'ri javob (${percent}%)`;
    }

    if (result.official) {
      const extra = result.full_mock ? "" : " (mashq — to'liq imtihon emas, ball 100/93 ga nisbatan hisoblangan)";
      detailEl.textContent = `${correctCount} / ${total} to'g'ri javob (${percent}%) · ${result.label || ""}${extra}`;
    }

    renderBreakdown(document.getElementById("quiz-celebrate-breakdown"), result);

    if (!(data.certificate && data.certificate.verification_id) && result.certificate_note) {
      const lock = document.getElementById("quiz-cert-lock");
      if (lock) { lock.querySelector("p").textContent = result.certificate_note; lock.hidden = false; }
    }
    if (data.certificate && data.certificate.verification_id) {
      const certBox = document.getElementById("quiz-celebrate-cert");
      certBox.style.display = "block";
      document.getElementById("quiz-celebrate-cert-view").href = `/certificate/${data.certificate.verification_id}`;
      document.getElementById("quiz-celebrate-cert-download").href = `/certificate/${data.certificate.verification_id}/pdf`;
    }

    const resultsBtn = document.getElementById("quiz-celebrate-results-btn");
    if (data.quiz_id) {
      resultsBtn.href = `/quiz/${data.quiz_id}/review`;
    } else {
      resultsBtn.style.display = "none";
    }

    if (tier !== "low") spawnConfetti(confettiField, tier === "high" ? 46 : 24);

    overlay.hidden = false;
  }

  function esc(t) { const d = document.createElement("div"); d.textContent = String(t == null ? "" : t); return d.innerHTML; }

  function renderBreakdown(el, result) {
    if (!el) return;
    el.innerHTML = "";
    if (!result || !result.official) return;
    let html = "";
    if (result.full_mock && result.blocks && result.blocks.length) {
      html += "<h4>Bloklar bo'yicha</h4><table>" + result.blocks.map((b) =>
        `<tr><td>${esc(b.name)}</td><td>${b.correct}/${b.total} · ${b.ball}/${b.max}</td></tr>`).join("") + "</table>";
    }
    if (result.by_difficulty && result.by_difficulty.length) {
      html += "<h4>Qiyinlik bo'yicha</h4><table>" + result.by_difficulty.map((d) =>
        `<tr><td>${esc(d.name)}</td><td>${d.correct}/${d.total}</td></tr>`).join("") + "</table>";
    }
    if (result.mode === "certificate" && result.benefit) {
      html += `<div class="result-benefit"><b>Imtiyoz:</b> ${esc(result.benefit)}` +
        (result.mandatory_note ? `<br>${esc(result.mandatory_note)}` : "") + "</div>";
    }
    el.innerHTML = html;
  }

  function spawnConfetti(field, count) {
    const colors = ["#2FBF83", "#FFA726", "#4A9EFF", "#F85149", "#E6EDF3"];
    field.innerHTML = "";
    for (let i = 0; i < count; i++) {
      const piece = document.createElement("span");
      piece.className = "quiz-confetti-piece";
      const fromLeft = i % 2 === 0;
      piece.style.left = fromLeft ? "-2%" : "102%";
      piece.style.top = `${10 + Math.random() * 30}%`;
      piece.style.setProperty("--dx", `${(fromLeft ? 1 : -1) * (220 + Math.random() * 260)}px`);
      piece.style.setProperty("--dy", `${260 + Math.random() * 300}px`);
      piece.style.setProperty("--rot", `${(Math.random() > 0.5 ? 1 : -1) * (360 + Math.random() * 540)}deg`);
      piece.style.background = colors[Math.floor(Math.random() * colors.length)];
      piece.style.animationDelay = `${Math.random() * 0.35}s`;
      field.appendChild(piece);
    }
  }

  // ---------- Savollarni yuklash ----------
  const _genUrl = blockSpecs ? "/api/block/generate" : (adaptiveMode ? "/api/adaptive/start" : "/api/quiz/generate");
  fetch(_genUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: blockSpecs ? JSON.stringify({ specs: blockSpecs.split(","), attempt_token: attemptToken })
      : adaptiveMode ? JSON.stringify({ subject: subject, mode: mode, topic: topic || null, total: questionCount, attempt_token: attemptToken })
      : JSON.stringify({
      subject: subject,
      level: level,
      topic: missedMode || topicsGroup || drillKind ? null : topic,
      topics: topicsGroup,
      count: questionCount,
      mode: mode,
      missed_mode: missedMode,
      attempt_token: attemptToken,
      variant: variant,
      checkpoint: checkpointMode,
      drill: drillKind || "",
      mock_id: parseInt(new URLSearchParams(location.search).get("mock") || "0", 10) || 0,
    }),
  })
    .then(async (res) => {
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || "Test yuklab bo'lmadi.");
      }
      return res.json();
    })
    .then((data) => {
      questions = data.questions || [];
      if (!questions.length) throw new Error("Savollar topilmadi.");
      if (data.adaptive && data.total) adaptiveTotal = data.total;
      if (data.time_limit_minutes) {
        timeLimitMinutes = data.time_limit_minutes;
        remainingSeconds = timeLimitMinutes * 60;
      }

      loadingEl.style.display = "none";
      bodyEl.style.display = "block";
      if (window.LZQuizStyle) window.LZQuizStyle.applyLayout(document, data.layout);
      renderQuestion();
      // Yuklanish ekrani kamida ~0.9 s ko'rinadi (ko'z o'ngida "miltillab" qolmasin), so'ng test ochiladi
      Loader.hide(900).then(() => {
        startTimer();
        try { window.dispatchEvent(new CustomEvent("lz:ready")); } catch (e) {}
        if (window.LZSheet) window.LZSheet.sync();
      });
      startAutosave();
    })
    .catch((err) => {
      loadingEl.style.display = "none";
      Loader.hide(500).then(() => {
        errorEl.style.display = "block";
        errorTextEl.textContent = err.message || "Test hozircha ishlamayapti. Birozdan so'ng qayta urinib ko'ring.";
      });
    });
})();
