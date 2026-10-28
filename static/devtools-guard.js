// ============================================================================
// LongoUZ — DevTools/kod ko'rish himoyasi.
//
// MUHIM, HALOL IZOH: bu himoya faqat ODDIY foydalanuvchini to'xtatadi —
// F12, o'ng tugma menyusi va asosiy klaviatura kombinatsiyalarini bloklaydi.
// Professional dasturchi/hacker DevTools'ni boshqa yo'llar bilan (masalan
// brauzer menyusi orqali, yoki brauzerni --auto-open-devtools bilan ishga
// tushirib) baribir ocha oladi — bu HECH QANDAY brauzer sayti uchun 100%
// oldini olib bo'lmaydigan narsa. Haqiqiy himoya — SERVER TOMONIDA: maxfiy
// mantiq/kalitlar hech qachon frontendga chiqarilmasligi kerak (buni
// main.py/database.py'dagi anti-tamper tizimi allaqachon ta'minlaydi —
// to'g'ri javoblar brauzerga umuman yuborilmaydi). Shu skript esa faqat
// "ko'chada o'tkinchi" darajasidagi qiziquvchanlikning oldini oladi.
// ============================================================================
(function () {
  // O'ng tugma (kontekst) menyusini o'chirish
  document.addEventListener("contextmenu", function (e) {
    e.preventDefault();
  });

  document.addEventListener("keydown", function (e) {
    // F12
    if (e.key === "F12") {
      e.preventDefault();
      return false;
    }
    // Ctrl+Shift+I / Ctrl+Shift+J / Ctrl+Shift+C (DevTools, Console, Inspect)
    if (e.ctrlKey && e.shiftKey && ["I", "i", "J", "j", "C", "c"].includes(e.key)) {
      e.preventDefault();
      return false;
    }
    // Ctrl+U (View Source)
    if (e.ctrlKey && (e.key === "U" || e.key === "u")) {
      e.preventDefault();
      return false;
    }
  });

  // DevTools ochiq bo'lishini oyna o'lchami farqi orqali aniqlashga urinish
  // (faqat "ajratilgan" DevTools panellari uchun ishlaydi, konsolni
  // alohida oynada ochish yoki mobil rejimda buni chetlab o'tish mumkin —
  // shuning uchun bu FAQAT qo'shimcha, hal qiluvchi emas).
  const threshold = 160;
  let devtoolsWarned = false;
  setInterval(function () {
    const widthDiff = window.outerWidth - window.innerWidth;
    const heightDiff = window.outerHeight - window.innerHeight;
    if ((widthDiff > threshold || heightDiff > threshold) && !devtoolsWarned) {
      devtoolsWarned = true;
      console.log("%cTo'xtating!", "color:red;font-size:40px;font-weight:bold;");
      console.log(
        "%cBu brauzer funksiyasi dasturchilar uchun. Bu yerga biror kod " +
          "joylashtirish yoki 'buyruq' bajarishni birov sizdan so'rasa, bu " +
          "firibgarlik bo'lishi mumkin.",
        "font-size:16px;",
      );
    }
    if (widthDiff <= threshold && heightDiff <= threshold) {
      devtoolsWarned = false;
    }
  }, 1000);
})();
