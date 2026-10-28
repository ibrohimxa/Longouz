// ============================================================================
// LongoUZ — login/register sahifasidagi jonli boyqush
// - Email maydoniga yozilganda: bosh pastga qaraydi
// - Parol maydoniga yozilganda: ikkala ko'z yumiladi
// - Ko'z ikonkasi bosilganda (parolni ko'rsatish): bir qanot tushadi,
//   bitta ko'z ochiladi (Telegram uslubidagi maymun animatsiyasiga o'xshab)
// ============================================================================

(function () {
  const head = document.getElementById("auth-owl-head");
  const eyelidLeft = document.getElementById("auth-eyelid-left");
  const eyelidRight = document.getElementById("auth-eyelid-right");
  const wingLeft = document.getElementById("auth-owl-wing-left");
  const wingRight = document.getElementById("auth-owl-wing-right");
  const owlLift = document.getElementById("auth-owl-lift");

  if (!head) return; // bu sahifada boyqush yo'q — chiqamiz

  // ---------- 0. Boyqush BOSHIDA devor ortida yashiringan — Ism yoki
  //              Email maydoniga birinchi marta fokus qilinganda "birdan"
  //              chiqib keladi va SHU sahifada qolgan vaqt davomida ochiq
  //              qoladi (qayta yashirilmaydi). ----------
  function revealOwl() {
    if (owlLift && !owlLift.classList.contains("is-revealed")) {
      owlLift.classList.add("is-revealed");
    }
  }
  const revealTriggers = document.querySelectorAll("#first_name, .auth-email-input");
  revealTriggers.forEach((input) => {
    input.addEventListener("focus", revealOwl, { once: false });
  });

  // Qanotning tinch (pastki) va ko'zni to'liq yopadigan (yuqori) holatlari
  const WING_REST = "translateY(0) rotate(0deg)";
  const WING_COVER_LEFT = "translateY(-58px) rotate(12deg)";
  const WING_COVER_RIGHT = "translateY(-58px) rotate(-12deg)";

  const emailInput = document.querySelector(".auth-email-input");
  const passwordInputs = document.querySelectorAll(".auth-password-input");

  // ---------- 1. Email yozilganda bosh pastga qaraydi ----------
  if (emailInput) {
    emailInput.addEventListener("focus", () => {
      head.style.transform = "rotate(0deg) translateY(6px)";
    });
    emailInput.addEventListener("input", () => {
      // Yozilgan harflar soniga qarab bosh biroz ko'proq egiladi
      const len = Math.min(emailInput.value.length, 14);
      const tilt = 4 + len * 0.4;
      head.style.transform = `rotate(0deg) translateY(${6 + tilt}px)`;
    });
    emailInput.addEventListener("blur", () => {
      head.style.transform = "translateY(0)";
    });
  }

  // ---------- 2. Parol yozilganda: IKKALA qanot yuqoriga ko'tarilib,
  //              ikkala ko'zni TO'LIQ yopadi (real Telegram uslubida) ----------
  function closeEyes() {
    if (eyelidLeft) eyelidLeft.style.transform = "scaleY(1)";
    if (eyelidRight) eyelidRight.style.transform = "scaleY(1)";
    if (wingLeft) wingLeft.style.transform = WING_COVER_LEFT;
    if (wingRight) wingRight.style.transform = WING_COVER_RIGHT;
  }

  function openEyes() {
    if (eyelidLeft) eyelidLeft.style.transform = "scaleY(0)";
    if (eyelidRight) eyelidRight.style.transform = "scaleY(0)";
    if (wingLeft) wingLeft.style.transform = WING_REST;
    if (wingRight) wingRight.style.transform = WING_REST;
  }

  // Faqat bitta ko'zni ochish (ko'z ikonkasi bosilganda) — CHAP ko'z TO'LIQ
  // yopiq qoladi (chap qanot yopib turadi), O'NG ko'z esa TO'LIQ ochiladi.
  // Ikkalasi ham endi "chiziq" emas — to'liq doira (yopiq) yoki to'liq
  // ko'rinadigan qorachiq (ochiq) bo'ladi, hech qachon oraliq holatda
  // qolib ketmaydi.
  function openOneEye() {
    if (eyelidLeft) eyelidLeft.style.transform = "scaleY(1)";  // chap — to'liq yopiq
    if (eyelidRight) eyelidRight.style.transform = "scaleY(0)"; // o'ng — to'liq ochiq
    if (wingLeft) wingLeft.style.transform = WING_COVER_LEFT;
    if (wingRight) wingRight.style.transform = WING_REST;
  }

  passwordInputs.forEach((input) => {
    input.addEventListener("focus", closeEyes);
    input.addEventListener("input", closeEyes);
    input.addEventListener("blur", () => {
      // Agar shu payt "ko'rsatish" tugmasi orqali ochilmagan bo'lsa, yumiq qoladi
      if (input.type === "password") closeEyes();
    });
  });

  // ---------- 3. Parolni ko'rsatish tugmasi ----------
  const toggleButtons = document.querySelectorAll(".password-toggle-btn");
  toggleButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-target");
      const targetInput = document.getElementById(targetId);
      if (!targetInput) return;

      if (targetInput.type === "password") {
        targetInput.type = "text";
        openOneEye();
      } else {
        targetInput.type = "password";
        closeEyes();
      }
    });
  });
})();
