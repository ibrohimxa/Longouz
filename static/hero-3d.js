// ============================================================================
// LongoUZ — Bosh sahifa hero bo'limidagi 3D effektlar (faqat CSS transform,
// tashqi kutubxona kerak emas). Bu fayl FAQAT home.html'da ulanadi.
//
//   1) Hero preview kartasi (#hero-tilt-card) sichqoncha pozitsiyasiga
//      qarab uch o'lchamda "egiladi" (tilt) — CSS'dagi --tilt-x/--tilt-y
//      custom propertylari orqali.
//   2) Orbit halqa va simli kublar CSS animatsiyasi bilan avtomatik
//      aylanadi (bu faylga hojat yo'q, faqat style.css'da).
//
// Sezgirlik: faqat "chinakam sichqonchasi bor" qurilmalarda ishga tushadi
// (hover:hover + pointer:fine) va "harakatni kamaytirish" (prefers-reduced-
// motion) yoqilgan bo'lsa — umuman ishga tushmaydi.
// ============================================================================

(function () {
  const card = document.getElementById("hero-tilt-card");
  if (!card) return;

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const hasFinePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  if (prefersReducedMotion || !hasFinePointer) return;

  const wrap = card.closest(".hero-visual") || card;
  const MAX_TILT_DEG = 9; // haddan tashqari "aylanib ketmasligi" uchun chegara

  function handlePointerMove(e) {
    const rect = wrap.getBoundingClientRect();
    const relX = (e.clientX - rect.left) / rect.width;  // 0..1
    const relY = (e.clientY - rect.top) / rect.height;  // 0..1

    // Markazdan chetga chiqqan sari egilish kuchayadi (-1..1 oralig'ida)
    const offsetX = relX * 2 - 1;
    const offsetY = relY * 2 - 1;

    const tiltY = offsetX * MAX_TILT_DEG;   // chapga/o'ngga egilish
    const tiltX = offsetY * -MAX_TILT_DEG;  // yuqoriga/pastga egilish

    card.style.setProperty("--tilt-x", tiltX.toFixed(2) + "deg");
    card.style.setProperty("--tilt-y", tiltY.toFixed(2) + "deg");
  }

  function resetTilt() {
    card.style.setProperty("--tilt-x", "0deg");
    card.style.setProperty("--tilt-y", "0deg");
  }

  wrap.addEventListener("pointermove", handlePointerMove);
  wrap.addEventListener("pointerleave", resetTilt);
})();
