// ============================================================================
// LongoUZ — kirish animatsiyasi, typewriter, scroll-reveal
// ============================================================================

(function () {

  // ==========================================================================
  // 1. KIRISH ANIMATSIYASI — 2 soniya yashil progress bar, och ko'k fon
  // ==========================================================================
  const introScreen = document.getElementById("intro-screen");

  // v219: 3 soniyalik kirish ekrani sahifani bloklab qo'yardi — endi darhol olib tashlanadi
  if (introScreen) introScreen.remove();
  document.body.classList.remove("intro-active");
  startPageAnimations();

  // ==========================================================================
  // 2. TYPEWRITER EFFEKT — ikki xil gap navbatma-navbat yozilib-o'chiriladi
  // ==========================================================================
  function startTypewriter() {
    const el = document.getElementById("typewriter-text");
    if (!el) return;

    const phrases = [
      "DTM'ga tayyorlan.",
      "IELTS'da yuqori ball ol.",
      "Har kuni bir qadam.",
      "O'zbek tilini mukammal bil.",
      "Matematikani tushun.",
      "Tarixni esda qol.",
    ];

    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let pauseBeforeDelete = false;

    function tick() {
      const current = phrases[phraseIdx];

      if (pauseBeforeDelete) {
        pauseBeforeDelete = false;
        setTimeout(tick, 1400); // 1.4 soniya kutadi
        return;
      }

      if (!isDeleting) {
        // Yozish
        el.textContent = current.slice(0, charIdx + 1);
        charIdx++;
        if (charIdx === current.length) {
          isDeleting = true;
          pauseBeforeDelete = true;
          setTimeout(tick, 20);
        } else {
          setTimeout(tick, 60); // yozish tezligi
        }
      } else {
        // O'chirish
        el.textContent = current.slice(0, charIdx - 1);
        charIdx--;
        if (charIdx === 0) {
          isDeleting = false;
          phraseIdx = (phraseIdx + 1) % phrases.length;
          setTimeout(tick, 400); // keyingi gapdan oldin pauza
        } else {
          setTimeout(tick, 35); // o'chirish tezligi
        }
      }
    }

    setTimeout(tick, 600);
  }

  // ==========================================================================
  // 3. SCROLL-REVEAL
  // ==========================================================================
  function startScrollReveal() {
    const revealEls = document.querySelectorAll("[data-reveal]");
    if (!revealEls.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("reveal-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    revealEls.forEach((el) => observer.observe(el));
  }

  // ==========================================================================
  // 4. FAN TANLASH ACCORDION — fan tanlanganda daraja qismi pastdan chiqadi
  // ==========================================================================
  function initSubjectAccordion() {
    const subjectCards = document.querySelectorAll(".subject-select-card");
    const levelSection = document.getElementById("level-section");

    if (!subjectCards.length || !levelSection) return;

    subjectCards.forEach((card) => {
      card.addEventListener("click", () => {
        // Avval barcha kartalardan active'ni olib tashlash
        subjectCards.forEach((c) => c.classList.remove("selected"));
        card.classList.add("selected");

        // Daraja qismini ko'rsatish (accordion kabi pastdan ochiladi)
        levelSection.classList.add("level-open");
        levelSection.scrollIntoView({ behavior: "smooth", block: "nearest" });
      });
    });
  }

  // ==========================================================================
  // 5. THEME TOGGLE — quyosh/oy tugmasi
  // ==========================================================================
  function initThemeToggle() {
    const toggles = document.querySelectorAll(".theme-toggle");
    if (!toggles.length) return;

    toggles.forEach((btn) => {
      btn.addEventListener("click", () => {
        const current = document.documentElement.getAttribute("data-theme") || "dark";
        const next = current === "dark" ? "light" : "dark";
        const root = document.documentElement;
        root.classList.add("theme-anim");
        setTimeout(() => root.classList.remove("theme-anim"), 1300);
        root.setAttribute("data-theme", next);
        localStorage.setItem("longouz_theme", next);
      });
    });
  }

  // ==========================================================================
  // ==========================================================================
  // 6b. JONLI BOYQUSH (asl PNG + overlay qorachiq) — header, sidebar va
  //     boshqa joylardagi kichik logotiplarda ishlatiladi. SVG chizishga
  //     hojat yo'q, shuning uchun hech qachon "ko'rshapalak"ga o'xshab
  //     qolmaydi — doim ASL logotip ko'rinadi, faqat ko'zi qimirlaydi.
  // ==========================================================================
  function initLivingOwl(containerId, maxOffsetPx) {
    const container = document.getElementById(containerId);
    if (!container) return;
    const leftPupil = container.querySelector("[data-lo-pupil-left]");
    const rightPupil = container.querySelector("[data-lo-pupil-right]");
    if (!leftPupil || !rightPupil) return;

    document.addEventListener("mousemove", (e) => {
      const rect = container.getBoundingClientRect();
      if (rect.width === 0) return;
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;

      const dx = e.clientX - centerX;
      const dy = e.clientY - centerY;
      const distance = Math.hypot(dx, dy) || 1;
      const offset = Math.min(distance / 14, maxOffsetPx);
      const mx = ((dx / distance) * offset).toFixed(1) + "px";
      const my = ((dy / distance) * offset).toFixed(1) + "px";

      container.style.setProperty("--lo-mx", mx);
      container.style.setProperty("--lo-my", my);
    });
  }

  // ==========================================================================
  // 7. PIN QILINGAN BOYQUSH — butun sayt bo'ylab ko'rinadi, bosilganda
  //    chat ochiladi/yopiladi (bosh qimirlamaydi — faqat ko'zi, yuqoriga q.)
  // ==========================================================================
  function initPinnedOwl() {
    const btn = document.getElementById("owl-pin-button");
    if (!btn) return;

    initLivingOwl("owl-pin-living", 5);

    btn.addEventListener("click", () => {
      const chatWidget = document.getElementById("floating-chat-widget");
      if (chatWidget) {
        chatWidget.classList.toggle("chat-widget-open");
        if (chatWidget.classList.contains("chat-widget-open")) {
          const input = chatWidget.querySelector("input");
          if (input && !input.disabled) input.focus();
        }
      }
    });
  }

  function startPageAnimations() {
    startTypewriter();
    startScrollReveal();
    initSubjectAccordion();
    initThemeToggle();
    initPinnedOwl();
    // MUHIM: header-dagi logotipda ko'z-kuzatish ATAYLAB o'chirilgan —
    // faqat pastki pin qilingan boyqushda (initPinnedOwl ichida) qoladi.
    // initLivingOwl("header-owl-living", 3);
  }

})();

// ============================================================================
// MOBIL/PLANSHET: yon panel yuqori panelga aylanadi. Sig'magan bo'limlar
// "3 chiziq" tugmasi ortiga yig'iladi va shu joyida ochiladigan darchada chiqadi.
// ============================================================================
(function () {
  const sidebar = document.querySelector(".app-sidebar");
  if (!sidebar) return;
  const brand = sidebar.querySelector(".sidebar-brand");
  const nav = sidebar.querySelector(".sidebar-nav");
  if (!brand || !nav) return;
  const mq = window.matchMedia("(max-width: 900px)");
  const links = Array.from(nav.querySelectorAll(".sidebar-link"));
  const mqPhone = window.matchMedia("(max-width: 640px)");
  links.forEach((a) => {
    Array.from(a.childNodes).forEach((n) => {
      if (n.nodeType === 3 && n.textContent.trim()) {
        const sp = document.createElement("span"); sp.className = "sb-lbl"; sp.textContent = n.textContent.trim(); a.replaceChild(sp, n);
      }
    });
  });
  const logout = sidebar.querySelector(".sidebar-footer a[href*='logout']");

  const burger = document.createElement("button");
  burger.type = "button"; burger.className = "sidebar-burger"; burger.hidden = true;
  burger.setAttribute("aria-label", "Menyu"); burger.setAttribute("aria-expanded", "false");
  burger.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>';
  sidebar.appendChild(burger);
  const drop = document.createElement("div");
  drop.className = "sb-drop"; drop.setAttribute("role", "menu");
  sidebar.appendChild(drop);

  function setOpen(open) {
    drop.classList.toggle("open", open);
    sidebar.classList.toggle("is-open", open);
    burger.setAttribute("aria-expanded", open ? "true" : "false");
  }
  function fit() {
    drop.innerHTML = ""; setOpen(false);
    links.forEach((a) => a.classList.remove("sb-hidden"));
    if (!mq.matches) { burger.hidden = true; return; }
    burger.hidden = false;
    // Telefonda: bo'limlar pastki panelda, "Yana" tugmasi shu panelning oxirida
    if (mqPhone.matches) { nav.appendChild(burger); } else if (burger.parentNode !== sidebar) { sidebar.appendChild(burger); }
    document.documentElement.classList.toggle("has-bottom-nav", mqPhone.matches);
    const avail = nav.clientWidth - (mqPhone.matches ? burger.offsetWidth + 6 : 0);
    const widths = links.map((a) => a.offsetWidth + 2);
    let used = 0, k = 0;
    const cap = mqPhone.matches ? 4 : links.length;
    while (k < links.length && k < cap && used + widths[k] <= avail) { used += widths[k]; k++; }
    const activeIdx = links.findIndex((a) => a.classList.contains("active"));
    const hidden = new Set();
    for (let i = k; i < links.length; i++) hidden.add(i);
    if (hidden.size && activeIdx >= k && k > 0) { hidden.delete(activeIdx); hidden.add(k - 1); }
    links.forEach((a, i) => { if (hidden.has(i)) a.classList.add("sb-hidden"); });
    links.forEach((a, i) => { if (hidden.has(i)) { const c = a.cloneNode(true); c.classList.remove("sb-hidden"); drop.appendChild(c); } });
    if (logout) { const sep = document.createElement("div"); sep.className = "sb-sep"; drop.appendChild(sep); drop.appendChild(logout.cloneNode(true)); }
    const up = document.createElement("a");
    up.className = "sidebar-link"; up.href = "/upgrade";
    up.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3 6 6 .9-4.5 4.4 1 6.2L12 16.6 6.5 19.5l1-6.2L3 8.9 9 8z"/></svg>Pro tarif';
    drop.appendChild(up);
    if (!hidden.size && !logout) burger.hidden = true;
  }
  burger.addEventListener("click", (e) => { e.stopPropagation(); setOpen(!drop.classList.contains("open")); });
  document.addEventListener("click", (e) => { if (!sidebar.contains(e.target)) setOpen(false); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") setOpen(false); });
  let t = 0;
  window.addEventListener("resize", () => { clearTimeout(t); t = setTimeout(fit, 80); });
  if (mq.addEventListener) { mq.addEventListener("change", fit); mqPhone.addEventListener("change", fit); }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
  fit();
})();
