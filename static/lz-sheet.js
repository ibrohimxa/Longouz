/* LongoUZ v229 — test oynasidagi YAGONA panel tizimi (formulalar, kalkulyator, shikoyat, savollar ro'yxati).
   - Bir vaqtda faqat BITTA panel ochiq: boshqasini bossangiz, oldingisi darhol yopiladi.
   - Telefonda (<=760px) panel sarlavha ostidan ekranning pastigacha TO'LIQ ochiladi;
     tepadagi tutqichni (yoki sarlavhani) pastga sursangiz — yarim ekranga kichrayadi,
     yana pastga sursangiz — yopiladi; tepaga sursangiz — yana to'liq ekran.
   - Yarim holatda savol tepada ko'rinib turadi, pastki "Oldingi / Keyingi" paneli ham bosiladi.
   - Kompyuterda o'ng tomondan chiqadigan panel (surish shart emas).
   Ishlatish: LZSheet.register("calc", el, { button, onOpen, onClose, half: false }); LZSheet.open("calc"). */
(function () {
  "use strict";
  var sheets = {};
  var current = null;
  var mq = window.matchMedia ? window.matchMedia("(max-width: 760px)") : { matches: false, addEventListener: function () {} };
  var root = document.documentElement;

  function isPhone() { return !!mq.matches; }

  function syncMetrics() {
    var hdr = document.querySelector(".quiz-header") || document.querySelector(".site-header");
    var nav = document.querySelector(".quiz-nav-row");
    var h = hdr ? Math.round(hdr.getBoundingClientRect().height) : 56;
    root.style.setProperty("--lz-hdr", Math.max(h, 0) + "px");
    var nb = 0;
    if (nav && isPhone()) {
      var cs = window.getComputedStyle(nav);
      if (cs.position === "fixed" && cs.display !== "none") nb = Math.round(nav.getBoundingClientRect().height);
    }
    root.style.setProperty("--lz-navbar", nb + "px");
  }

  function setBody() {
    var s = current ? sheets[current] : null;
    document.body.classList.toggle("lz-sheet-open", !!s);
    document.body.classList.toggle("lz-sheet-half", !!(s && s.el.classList.contains("is-half")));
    document.body.classList.toggle("lz-sheet-full", !!(s && !s.el.classList.contains("is-half")));
  }

  function markBtn(s, on) {
    (s.buttons || []).forEach(function (b) {
      if (!b) return;
      b.classList.toggle("is-active", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  function open(name, opts) {
    var s = sheets[name];
    if (!s) return;
    opts = opts || {};
    Object.keys(sheets).forEach(function (n) { if (n !== name) close(n, true); });
    syncMetrics();
    var wantHalf = isPhone() && (opts.half != null ? !!opts.half : !!s.half);
    s.el.style.transform = "";
    s.el.classList.toggle("is-half", wantHalf);
    s.el.classList.add("is-open");
    s.el.setAttribute("aria-hidden", "false");
    if ("inert" in s.el) s.el.inert = false;
    current = name;
    markBtn(s, true);
    setBody();
    if (s.onOpen) { try { s.onOpen(); } catch (e) {} }
  }

  function close(name, silent) {
    var s = sheets[name];
    if (!s || !s.el.classList.contains("is-open")) return;
    s.el.classList.remove("is-open", "is-half", "is-dragging");
    s.el.style.transform = "";
    s.el.setAttribute("aria-hidden", "true");
    if ("inert" in s.el) s.el.inert = true;
    markBtn(s, false);
    if (current === name) current = null;
    setBody();
    if (s.onClose) { try { s.onClose(); } catch (e) {} }
  }

  function toggle(name, opts) {
    if (current === name) close(name); else open(name, opts);
  }

  function setHalf(name, half) {
    var s = sheets[name];
    if (!s || !s.el.classList.contains("is-open")) return;
    s.el.classList.toggle("is-half", !!half && isPhone());
    setBody();
  }

  function wireDrag(name, el) {
    var grab = el.querySelector(".lz-sheet-grab");
    if (!grab) return;
    var dragging = false, startY = 0, base = 0, prevY = 0, prevT = 0, lastY = 0, lastT = 0, H = 1, pid = null;

    grab.addEventListener("pointerdown", function (e) {
      if (!isPhone() || !el.classList.contains("is-open")) return;
      if (e.target.closest("button, input, select, textarea, a")) return;
      dragging = true; pid = e.pointerId;
      H = Math.max(1, el.offsetHeight);
      base = 0;
      startY = prevY = lastY = e.clientY;
      prevT = lastT = performance.now();
      el.classList.add("is-dragging");
      try { grab.setPointerCapture(e.pointerId); } catch (err) {}
      e.preventDefault();
    });
    grab.addEventListener("pointermove", function (e) {
      if (!dragging || e.pointerId !== pid) return;
      prevY = lastY; prevT = lastT; lastY = e.clientY; lastT = performance.now();
      var dy = e.clientY - startY;
      var y = base + dy;
      if (y < 0) y = y / 4;                  // tepaga ortiqcha tortilsa — "rezina" effekti
      el.style.transform = "translateY(" + y + "px)";
    });
    function end(e) {
      if (!dragging || (e && e.pointerId !== pid)) return;
      dragging = false;
      el.classList.remove("is-dragging");
      var dy = lastY - startY;
      var dt = Math.max(1, lastT - prevT);
      var v = (lastY - prevY) / dt;          // px/ms (musbat — pastga)
      var wasHalf = el.classList.contains("is-half");
      el.style.transform = "";
      var frac = dy / H;
      var target;
      if (Math.abs(dy) < 6 && Math.abs(v) < 0.2) { target = wasHalf ? "full" : "stay"; }  // tutqichga bosish: yarim <-> to'liq
      else if (v > 0.9) target = wasHalf ? "close" : (frac > 0.45 ? "close" : "half");
      else if (v < -0.9) target = "full";
      else if (wasHalf) target = frac > 0.35 ? "close" : frac < -0.15 ? "full" : "half";
      else target = frac > 0.7 ? "close" : frac > 0.22 ? "half" : "full";
      if (target === "close") close(name);
      else if (target === "half") setHalf(name, true);
      else if (target === "full") setHalf(name, false);
    }
    grab.addEventListener("pointerup", end);
    grab.addEventListener("pointercancel", end);
    grab.addEventListener("lostpointercapture", function () { if (dragging) end({ pointerId: pid }); });
  }

  function register(name, el, o) {
    o = o || {};
    if (!el) return;
    var btns = [].concat(o.button || [], o.buttons || []).filter(Boolean);
    sheets[name] = { el: el, buttons: btns, onOpen: o.onOpen, onClose: o.onClose, half: !!o.half };
    el.classList.add("lz-sheet");
    el.setAttribute("aria-hidden", "true");
    if ("inert" in el) el.inert = true;
    btns.forEach(function (b) {
      b.addEventListener("click", function (e) { e.preventDefault(); toggle(name); });
    });
    Array.prototype.forEach.call(el.querySelectorAll("[data-sheet-close]"), function (b) {
      b.addEventListener("click", function () { close(name); });
    });
    Array.prototype.forEach.call(el.querySelectorAll("[data-sheet-size]"), function (b) {
      b.addEventListener("click", function () { setHalf(name, !el.classList.contains("is-half")); });
    });
    wireDrag(name, el);
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && current) close(current);
  });
  window.addEventListener("resize", function () {
    syncMetrics();
    if (!isPhone() && current) { var s = sheets[current]; if (s) { s.el.classList.remove("is-half"); setBody(); } }
  });
  if (mq.addEventListener) mq.addEventListener("change", syncMetrics);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", syncMetrics); else syncMetrics();

  window.LZSheet = {
    register: register, open: open, close: close, toggle: toggle, setHalf: setHalf,
    isOpen: function (name) { return name ? current === name : !!current; },
    current: function () { return current; },
    closeAll: function () { if (current) close(current); },
    sync: syncMetrics, isPhone: isPhone
  };
})();
