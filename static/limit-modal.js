// ============================================================================
// LongoUZ — qayta ishlatiladigan "AI limiti tugadi" bloklovchi modal.
// owl-chat.js'dagi bilan bir xil CSS klasslaridan foydalanadi (style.css).
// Chat vidjeti bo'lmagan sahifalarda (masalan IELTS Speaking/Writing mashq
// ekranlari) 402 javobini shu funksiya orqali ko'rsatamiz — faqat
// "Pro/Ultra'ga o'tish" yoki "Bekor qilish" bosilgandagina yopiladi.
// ============================================================================

window.showLimitModal = function (data) {
  const overlay = document.createElement("div");
  overlay.className = "owl-limit-modal-overlay";
  overlay.innerHTML = `
    <div class="owl-limit-modal-card">
      <p class="owl-limit-title">AI suhbat limiti tugadi</p>
      <p class="owl-limit-sub">${data.message || `${data.used}/${data.limit} ta savol ishlatildi.`}</p>
      <div class="owl-limit-actions">
        <a href="/#plans" class="btn-primary">Pro/Ultra'ga o'tish</a>
        <button type="button" class="btn-secondary owl-limit-dismiss">Bekor qilish</button>
      </div>
    </div>
  `;
  document.body.appendChild(overlay);
  overlay.querySelector(".owl-limit-dismiss").addEventListener("click", () => overlay.remove());
};
