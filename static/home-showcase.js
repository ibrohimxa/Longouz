// ============================================================================
// LongoUZ — bosh sahifa "jonli reklama" laptopi.
// Sahnalar saytning HAQIQIY ekranlaridan (dashboard, test, AI repetitor,
// formulalar/Mendeleyev jadvali) olingan rasmlardan iborat; ustida kursor,
// bosish, sahifa almashinuvi va ovoz to'lqinlari animatsiyasi o'ynaydi.
// Rasmlar /static/ad/ ichida (kunduz va tun uchun alohida), kursor nuqtalari
// /static/ad/targets.json'da. Sahna o'lchami 1280x800 (16:10).
// 4 ta sahna ketma-ket aylanadi; prefers-reduced-motion bo'lsa avtomatik emas.
// ============================================================================
(function () {
  "use strict";

  var W = 1280, H = 800;
  var REDUCED = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var TARGETS = null;

  function theme() { return document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark"; }
  function img(name) { return "/static/ad/" + name + "_" + theme() + ".webp"; }
  function ctr(r, dx, dy) { return [r[0] + r[2] / 2 + (dx || 0), r[1] + r[3] / 2 + (dy || 0)]; }

  var CURSOR_SVG = '<svg viewBox="0 0 24 24" width="44" height="44"><path d="M4 2l16 9-7 2-3 7z" fill="#111" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/></svg>';

  // ---- sahna ta'riflari: {ms, layers:[{src, steps:[[t, opacity, tx, scale]]}], cursor:[[t,x,y,click]], wave} ----
  function sceneTest(T) {
    var q = T.quiz, d = T.dash;
    var a = ctr(d.tests), o2 = ctr(q.opt2, 60, 0), nx = ctr(q.next);
    return {
      ms: 10500, label: "Test yechish",
      layers: [
        { src: img("dash"), steps: [[0, 1, 0, 1], [3500, 1, 0, 1], [4000, 1, 0, 1.0]] },
        { src: img("quiz"), steps: [[0, 0, 0, 1.03], [3400, 0, 0, 1.03], [3900, 1, 0, 1]] },
        { src: img("quiz_sel"), steps: [[0, 0, 0, 1], [5300, 0, 0, 1], [5500, 1, 0, 1], [7500, 1, 0, 1], [8100, 0, -60, 1]] },
        { src: img("quiz2"), steps: [[0, 0, 60, 1], [7500, 0, 60, 1], [8100, 1, 0, 1]] }
      ],
      cursor: [[0, 980, 640], [900, 900, 600], [1900, a[0], a[1], 1], [3500, a[0] + 60, a[1] + 40], [4700, o2[0], o2[1], 1], [6600, nx[0], nx[1], 1], [9200, nx[0] + 80, nx[1] + 90]],
      end: 10400
    };
  }
  function sceneRep(T) {
    var d = T.dash, r = T.rep;
    var a = ctr(d.rep);
    return {
      ms: 11500, label: "AI repetitor",
      layers: [
        { src: img("dash"), steps: [[0, 1, 0, 1]] },
        { src: img("rep"), steps: [[0, 0, 0, 1.03], [2300, 0, 0, 1.03], [2800, 1, 0, 1]] },
        { src: img("rep_listen"), steps: [[0, 0, 0, 1], [6800, 0, 0, 1], [7200, 1, 0, 1]] }
      ],
      cursor: [[0, 1000, 700], [800, 800, 620], [1800, a[0], a[1], 1], [3200, a[0] + 620, a[1] + 380], [10600, a[0] + 640, a[1] + 360]],
      wave: { rect: r.wave, from: 3000, listenFrom: 7000, to: 11300 },
      end: 11400
    };
  }
  function sceneChem(T) {
    var q = T.quiz, c = T.chem;
    var f = ctr(q.formulas), mg = ctr(c.mg);
    return {
      ms: 10000, label: "Kimyo",
      layers: [
        { src: img("quiz"), steps: [[0, 1, 0, 1], [2100, 1, 0, 1], [2800, 1, -40, 0.985]] },
        { src: img("chem_sheet"), steps: [[0, 0, 90, 1], [2100, 0, 90, 1], [2800, 1, 0, 1]] },
        { src: img("chem_pick"), steps: [[0, 0, 0, 1], [5000, 0, 0, 1], [5400, 1, 0, 1]] }
      ],
      cursor: [[0, 900, 520], [900, 1000, 300], [1900, f[0], f[1], 1], [3200, f[0] - 200, f[1] + 160], [4700, mg[0], mg[1], 1], [7500, mg[0] + 150, mg[1] + 200], [9500, mg[0] + 160, mg[1] + 210]],
      end: 9900
    };
  }
  function scenePhys(T) {
    var q = T.phys;
    var f = ctr(q.formulas), s = ctr(q.search);
    return {
      ms: 9500, label: "Fizika",
      layers: [
        { src: img("phys_quiz"), steps: [[0, 1, 0, 1], [2100, 1, 0, 1], [2800, 1, -40, 0.985]] },
        { src: img("phys_sheet"), steps: [[0, 0, 90, 1], [2100, 0, 90, 1], [2800, 1, 0, 1]] },
        { src: img("phys_pick"), steps: [[0, 0, 0, 1], [4500, 0, 0, 1], [4800, 1, 0, 1]] }
      ],
      cursor: [[0, 900, 500], [900, 1000, 300], [1900, f[0], f[1], 1], [3300, s[0] + 120, s[1] + 40], [4300, s[0], s[1], 1], [8500, s[0] + 200, s[1] + 260], [9300, s[0] + 210, s[1] + 270]],
      end: 9400
    };
  }
  var BUILDERS = [sceneTest, sceneRep, sceneChem, scenePhys];
  var LABELS = ["Test yechish", "AI repetitor", "Kimyo", "Fizika"];

  function frames(steps, total, kind) {
    return steps.map(function (s) {
      var o = Math.min(1, s[0] / total);
      return { offset: o, opacity: s[1], transform: "translateX(" + s[2] + "px) scale(" + s[3] + ")" };
    });
  }

  function Stage(root) {
    this.root = root;
    this.scr = root.querySelector("[data-scr]");
    this.tabs = root.querySelector("[data-tabs]");
    this.idx = 0;
    this.timer = null;
    this.paused = false;
    this.anims = [];
    var self = this;
    this.inner = document.createElement("div");
    this.inner.className = "scr-inner";
    this.scr.appendChild(this.inner);
    if (this.tabs) {
      this.tabs.innerHTML = LABELS.map(function (l, i) {
        return '<button type="button" class="stab" data-i="' + i + '"><span>' + (i + 1) + ". " + l + "</span><i></i></button>";
      }).join("");
      this.tabs.addEventListener("click", function (e) {
        var b = e.target.closest(".stab");
        if (b) self.show(+b.getAttribute("data-i"));
      });
    }
    this.fit();
    if (window.ResizeObserver) new ResizeObserver(function () { self.fit(); }).observe(this.scr);
    root.addEventListener("mouseenter", function () { self.paused = true; root.classList.add("paused"); self.setPlay(false); });
    root.addEventListener("mouseleave", function () { self.paused = false; root.classList.remove("paused"); self.setPlay(true); self.schedule(); });
    document.addEventListener("visibilitychange", function () { if (document.hidden) clearTimeout(self.timer); else self.schedule(); });
    new MutationObserver(function () { self.show(self.idx); }).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
    this.show(0);
  }
  Stage.prototype.fit = function () {
    var w = this.scr.clientWidth || W;
    this.inner.style.transform = "scale(" + (w / W) + ")";
  };
  Stage.prototype.setPlay = function (on) {
    this.anims.forEach(function (a) { try { if (on) a.play(); else a.pause(); } catch (e) { /* eski brauzer */ } });
  };
  Stage.prototype.clear = function () {
    this.anims.forEach(function (a) { try { a.cancel(); } catch (e) { /* yo'q */ } });
    this.anims = [];
    this.inner.innerHTML = "";
  };
  Stage.prototype.show = function (i) {
    var self = this;
    clearTimeout(this.timer);
    this.idx = (i + BUILDERS.length) % BUILDERS.length;
    if (!TARGETS) return;
    var sc = BUILDERS[this.idx](TARGETS[theme()]);
    this.clear();
    var total = sc.ms;
    sc.layers.forEach(function (L, k) {
      var im = document.createElement("img");
      im.className = "ad-layer";
      im.alt = "";
      im.decoding = "async";
      im.src = L.src;
      im.style.zIndex = String(k + 1);
      self.inner.appendChild(im);
      if (im.animate) self.anims.push(im.animate(frames(L.steps, total), { duration: total, fill: "forwards", easing: "ease-in-out" }));
      else im.style.opacity = L.steps[0][1];
    });
    // ovoz to'lqinlari (AI repetitor)
    if (sc.wave) this.addWave(sc, total);
    // kursor
    var cur = document.createElement("div");
    cur.className = "ad-cursor";
    cur.innerHTML = CURSOR_SVG;
    cur.style.zIndex = "50";
    this.inner.appendChild(cur);
    if (cur.animate) {
      var kf = [], clicks = [];
      sc.cursor.forEach(function (p, n) {
        var o = Math.min(1, p[0] / total);
        kf.push({ offset: o, opacity: n === 0 ? 0 : 1, transform: "translate(" + p[1] + "px," + p[2] + "px) scale(1)" });
        if (p[3]) {
          clicks.push(p);
          kf.push({ offset: Math.min(1, (p[0] + 160) / total), opacity: 1, transform: "translate(" + p[1] + "px," + p[2] + "px) scale(.78)" });
          kf.push({ offset: Math.min(1, (p[0] + 330) / total), opacity: 1, transform: "translate(" + p[1] + "px," + p[2] + "px) scale(1)" });
        }
      });
      var last = sc.cursor[sc.cursor.length - 1];
      kf.push({ offset: Math.min(1, sc.end / total), opacity: 0, transform: "translate(" + last[1] + "px," + last[2] + "px) scale(1)" });
      kf.sort(function (a, b) { return a.offset - b.offset; });
      this.anims.push(cur.animate(kf, { duration: total, fill: "forwards", easing: "ease-in-out" }));
      clicks.forEach(function (p) {
        var rp = document.createElement("div");
        rp.className = "ad-ripple";
        rp.style.left = p[1] + "px"; rp.style.top = p[2] + "px"; rp.style.zIndex = "49";
        self.inner.appendChild(rp);
        var o1 = Math.min(1, p[0] / total), o2 = Math.min(1, (p[0] + 700) / total);
        self.anims.push(rp.animate([{ offset: 0, opacity: 0, transform: "translate(-50%,-50%) scale(.2)" }, { offset: o1, opacity: 0, transform: "translate(-50%,-50%) scale(.2)" },
          { offset: Math.min(1, o1 + 0.0001), opacity: .75, transform: "translate(-50%,-50%) scale(.2)" }, { offset: o2, opacity: 0, transform: "translate(-50%,-50%) scale(2.2)" }, { offset: 1, opacity: 0, transform: "translate(-50%,-50%) scale(2.2)" }],
          { duration: total, fill: "forwards" }));
      });
    }
    if (this.tabs) {
      Array.prototype.forEach.call(this.tabs.children, function (b, k) {
        b.classList.toggle("active", k === self.idx);
        var bar = b.querySelector("i");
        bar.style.animation = "none";
        void bar.offsetWidth;
        bar.style.animation = k === self.idx && !REDUCED ? "stabfill " + total + "ms linear forwards" : "none";
      });
    }
    this.total = total;
    this.schedule();
  };
  Stage.prototype.addWave = function (sc, total) {
    var r = sc.wave.rect, n = 19, box = document.createElement("div");
    box.className = "ad-wave";
    // rasmdagi to'lqin joyi: markazda, kengroq qilib chizamiz
    var cx = r[0] + r[2] / 2, cy = r[1] + r[3] / 2, w = Math.max(r[2], 260) * 1.35, h = 110;
    box.style.cssText = "left:" + (cx - w / 2) + "px;top:" + (cy - h / 2) + "px;width:" + w + "px;height:" + h + "px;z-index:20";
    var bars = "";
    for (var i = 0; i < n; i++) {
      var d = (i * 97) % 600, dur = 420 + ((i * 53) % 380), mid = 1 - Math.abs(i - (n - 1) / 2) / (n / 1.6);
      bars += '<i style="--d:-' + d + 'ms;--t:' + dur + 'ms;--m:' + mid.toFixed(2) + '"></i>';
    }
    box.innerHTML = '<div class="ad-wave-env">' + bars + "</div>";
    this.inner.appendChild(box);
    var o = function (t) { return Math.min(1, t / total); };
    this.anims.push(box.animate([
      { offset: 0, opacity: 0 }, { offset: o(sc.wave.from - 10), opacity: 0 }, { offset: o(sc.wave.from + 350), opacity: 1 },
      { offset: o(sc.wave.to), opacity: 1 }, { offset: 1, opacity: 1 }
    ], { duration: total, fill: "forwards" }));
    // gapirish bosqichlari: AI gapiradi (katta, tez) -> foydalanuvchi (kichik, yashil)
    var env = box.querySelector(".ad-wave-env");
    this.anims.push(env.animate([
      { offset: 0, transform: "scaleY(.25)" },
      { offset: o(sc.wave.from + 900), transform: "scaleY(1)" }, { offset: o(sc.wave.from + 1700), transform: "scaleY(.35)" },
      { offset: o(sc.wave.from + 2500), transform: "scaleY(.95)" }, { offset: o(sc.wave.listenFrom - 300), transform: "scaleY(.3)" },
      { offset: o(sc.wave.listenFrom + 500), transform: "scaleY(.55)" }, { offset: o(sc.wave.listenFrom + 1500), transform: "scaleY(1)" },
      { offset: o(sc.wave.listenFrom + 2300), transform: "scaleY(.4)" }, { offset: o(sc.wave.listenFrom + 3000), transform: "scaleY(.9)" },
      { offset: 1, transform: "scaleY(.3)" }
    ], { duration: total, fill: "forwards", easing: "ease-in-out" }));
    this.anims.push(box.animate([
      { offset: 0, filter: "hue-rotate(0deg)" }, { offset: o(sc.wave.listenFrom), filter: "hue-rotate(0deg)" },
      { offset: o(sc.wave.listenFrom + 300), filter: "hue-rotate(-70deg)" }, { offset: 1, filter: "hue-rotate(-70deg)" }
    ], { duration: total, fill: "forwards" }));
  };
  Stage.prototype.schedule = function () {
    var self = this;
    clearTimeout(this.timer);
    if (REDUCED || this.paused || document.hidden || !this.total) return;
    this.timer = setTimeout(function () { self.show(self.idx + 1); }, this.total + 150);
  };

  function boot() {
    var roots = document.querySelectorAll("[data-stage]");
    var stages = [];
    function start() {
      roots.forEach(function (root) {
        if (root.closest("#demo-modal")) return; // demo oynasi ochilganda quriladi
        stages.push(new Stage(root));
      });
      wireDemo();
    }
    fetch("/static/ad/targets.json").then(function (r) { return r.json(); }).then(function (j) { TARGETS = j; start(); })
      .catch(function () { /* rasmlar yo'q bo'lsa — laptop bo'sh qoladi */ });
  }

  function wireDemo() {
    var openBtn = document.getElementById("demo-open");
    var modal = document.getElementById("demo-modal");
    if (!openBtn || !modal) return;
    var big = null;
    function close() { modal.hidden = true; document.body.style.overflow = ""; if (big) { clearTimeout(big.timer); big.clear(); } }
    openBtn.addEventListener("click", function () {
      modal.hidden = false;
      document.body.style.overflow = "hidden";
      if (!big) big = new Stage(modal.querySelector("[data-stage]"));
      else { big.fit(); big.show(0); }
    });
    modal.addEventListener("click", function (e) { if (e.target === modal || e.target.closest("[data-demo-close]")) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !modal.hidden) close(); });
  }

  boot();
})();
