/* LongoUz — sayt tillari: O'zbekcha (lotin), Ўзбекча (кирилл), English, Русский, Türkçe.
   Butun sahifa matnini (dinamik qo'shilganlari ham: bildirishnomalar, test oynasi, xabarlar) tarjima qiladi.
   Admin panelga ulanmaydi. Lug'at: /static/i18n/<til>.js  (window.__LZ_I18N). Lug'atda yo'q matnlar
   serverdagi tarjima xizmatidan (keshlangan) olinadi. translate="no" yoki .notranslate ichidagilar tegilmaydi. */
(function () {
  "use strict";
  var LANGS = [
    { code: "uz", name: "Oʻzbekcha", short: "UZ", flag: "🇺🇿" },
    { code: "uzc", name: "Ўзбекча", short: "ЎЗ", flag: "🇺🇿" },
    { code: "en", name: "English", short: "EN", flag: "🇬🇧" },
    { code: "ru", name: "Русский", short: "RU", flag: "🇷🇺" },
    { code: "tr", name: "Türkçe", short: "TR", flag: "🇹🇷" }
  ];
  function getCookie(n) { var m = document.cookie.match(new RegExp("(?:^|; )" + n + "=([^;]*)")); return m ? decodeURIComponent(m[1]) : ""; }
  var LANG = getCookie("lz_lang") || "uz";
  if (!LANGS.some(function (l) { return l.code === LANG; })) LANG = "uz";
  var root = document.documentElement;
  root.setAttribute("lang", LANG === "uzc" ? "uz-Cyrl" : LANG);
  var DICT = window.__LZ_I18N || {};
  var ACTIVE = LANG !== "uz";

  /* ---------- yordamchi funksiyalar ---------- */
  var APOS = /[‘’ʻʼ`´]/g;
  var NUM = /\d+(?:[.,]\d+)?/g;
  function norm(s) { return s.replace(APOS, "'").replace(/\s+/g, " ").trim(); }
  function keyOf(s) { var nums = []; var k = norm(s).replace(NUM, function (m) { nums.push(m); return "{" + (nums.length - 1) + "}"; }); return { k: k, nums: nums }; }
  function fill(tpl, nums) { return tpl.replace(/\{(\d+)\}/g, function (m, i) { return nums[+i] != null ? nums[+i] : m; }); }

  var UZ_HINT = /(o'|g'|\bva\b|\bbilan\b|\buchun\b|\byoki\b|\bbu\b|\bham\b|\bemas\b|\bkerak\b|\bmumkin\b|\bta\b|sh|ch|lar\b|lari|ning\b|ingiz|imiz|moq|yapti|siz\b|dan\b|\w+ga\b|\w+da\b|\w+ni\b|\bqil|\bbo'l|\bko'r|savol|javob|natija|tarif|fan\b|mavzu|kirish|test|hisob|bepul|kabinet|sertifikat|qayta|tanla|saqla|yuklan|kuting|xato|to'g'ri|'ga\b|\w+(?:gan|ish|lan|lik|chi|dir|miz|ngiz|sini|dagi|moqda|yapmiz)\b)/i;
  var EN_HINT = /\b(the|and|of|you|your|is|are|to|in|for|with|this|that|it|be|on|was|what|how|why|do|does|describe|talk|about)\b/i;
  var MATHY = /[=²³√⁄∫π→≥≤⇒±×÷∞∑]/;
  function looksUz(s) {
    if (!/[A-Za-z]{2}/.test(s)) return false;
    var hits = (s.match(new RegExp(UZ_HINT.source, "gi")) || []).length;
    var en = (s.match(new RegExp(EN_HINT.source, "gi")) || []).length;
    return hits > 0 && hits >= en;
  }

  /* ---------- lotin → kirill ---------- */
  var KEEP = /^(LongoUz|LongoUZ|LongoAI|Longo|Pro|Ultra|Free|PRO|ULTRA|FREE|IELTS|SAT|CEFR|Gemini|Google|GitHub|Vercel|Telegram|Click|Payme|Uzum|UzCard|Humo|Visa|Mastercard|QR|AI|PDF|JSON|Email|email|Gmail|ID|URL|sin|cos|tan|ctg|tg|log|ln|lg|lim|max|min|mod|Ans|A\+|B\+|C\+|OK|Ok|Ctrl|Shift|Alt|Enter|Esc|Streak|Speaking|Writing|Reading|Listening|Band|Task|Part|cue|card|Flexbox|Python|HTML|CSS|LLM|BMBA|UzBMB|UZBMB)$/;
  var MAP = { a: "а", b: "б", d: "д", e: "е", f: "ф", g: "г", h: "ҳ", i: "и", j: "ж", k: "к", l: "л", m: "м", n: "н", o: "о", p: "п", q: "қ", r: "р", s: "с", t: "т", u: "у", v: "в", x: "х", y: "й", z: "з", c: "с", w: "в" };
  function cyrWord(w) {
    if (KEEP.test(w) || /\d/.test(w)) return w;
    if (w.length === 1 && !/^[uUoOeEiIaA]$/.test(w)) return w;          /* x, y, b — o'zgaruvchilar */
    var upAll = w.length > 1 && w === w.toUpperCase() && /[A-Z]/.test(w);
    var s = w, out = "", i = 0, lw = s.toLowerCase();
    while (i < s.length) {
      var ch = s[i], lo = lw[i], two = lw.substr(i, 2), up = ch !== lo, r = null, adv = 1;
      if (two === "o'") { r = "ў"; adv = 2; }
      else if (two === "g'") { r = "ғ"; adv = 2; }
      else if (two === "sh") { r = "ш"; adv = 2; }
      else if (two === "ch") { r = "ч"; adv = 2; }
      else if (two === "ck") { r = "к"; adv = 2; }
      else if (two === "yo") { r = "ё"; adv = 2; }
      else if (two === "yu") { r = "ю"; adv = 2; }
      else if (two === "ya") { r = "я"; adv = 2; }
      else if (two === "ye" && (i === 0 || /[aeiou']/.test(lw[i - 1]))) { r = "е"; adv = 2; }
      else if (lo === "e" && (i === 0 || /[aeiou']/.test(lw[i - 1]))) { r = "э"; }
      else if (lo === "'") { r = (i > 0 && i < s.length - 1) ? "ъ" : "'"; }
      else if (MAP[lo]) { r = MAP[lo]; }
      else { r = ch; }
      if (up || upAll) r = r.toUpperCase();
      out += r; i += adv;
    }
    if (!upAll && w[0] === w[0].toUpperCase() && w[0] !== w[0].toLowerCase()) out = out[0].toUpperCase() + out.slice(1);
    return out;
  }
  function toCyr(s) {
    if (MATHY.test(s) && !looksUz(s)) return s;
    return s.replace(APOS, "'").replace(/[A-Za-z']+(?:'[A-Za-z]+)*/g, function (w) {
      if (/^'+$/.test(w)) return w;
      var lead = w.match(/^'*/)[0], trail = w.match(/'*$/)[0];
      var core = w.slice(lead.length, w.length - trail.length);
      if (/[gGoO]$/.test(core) && trail) { core += "'"; trail = trail.slice(1); }
      return lead + cyrWord(core) + trail;
    });
  }

  /* ---------- tarjima ---------- */
  var CACHE_KEY = "lz_i18n_" + LANG, mem = {};
  try { mem = JSON.parse(localStorage.getItem(CACHE_KEY) || "{}") || {}; } catch (e) { mem = {}; }
  var pending = {}, timer = null, waiters = [];
  function lookup(text) {
    var o = keyOf(text);
    if (!o.k || !/[A-Za-zÀ-ɏ]{2}/.test(o.k)) return null;
    if (LANG === "uzc") {
      if (DICT[o.k] !== undefined || looksUz(o.k)) return toCyr(norm(text));
      return null;
    }
    var hit = DICT[o.k];
    if (hit === undefined) hit = mem[o.k];
    if (hit !== undefined && hit !== null) return fill(hit, o.nums);
    if (looksUz(o.k) && o.k.length < 1800) queue(o.k);
    return null;
  }
  function queue(k) {
    if (pending[k] || mem[k] === null) return;
    pending[k] = 1;
    clearTimeout(timer); timer = setTimeout(flush, 350);
  }
  function flush() {
    var keys = Object.keys(pending).slice(0, 60);
    if (!keys.length) return;
    keys.forEach(function (k) { delete pending[k]; });
    fetch("/api/i18n/translate", { method: "POST", headers: { "Content-Type": "application/json", "X-Requested-With": "fetch" }, body: JSON.stringify({ lang: LANG, items: keys }) })
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (j) {
        var tr = (j && j.items) || {}, got = false;
        keys.forEach(function (k) { if (typeof tr[k] === "string" && tr[k]) { mem[k] = tr[k]; got = true; } });
        try { localStorage.setItem(CACHE_KEY, JSON.stringify(mem).length < 1500000 ? JSON.stringify(mem) : "{}"); } catch (e) { /* to'la */ }
        if (got) walk(document.body);
      }).catch(function () { /* tarmoq yo'q — o'zbekcha qoladi */ });
    if (Object.keys(pending).length) timer = setTimeout(flush, 400);
  }

  var SKIP_TAGS = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEXTAREA: 1, CODE: 1, PRE: 1, svg: 1, math: 1 };
  var done = new WeakMap();
  function skipEl(el) {
    for (var e = el; e && e !== document; e = e.parentElement) {
      if (SKIP_TAGS[e.tagName] || e.isContentEditable) return true;
      if (e.getAttribute && (e.getAttribute("translate") === "no" || (e.classList && (e.classList.contains("notranslate") || e.classList.contains("katex"))))) return true;
    }
    return false;
  }
  function doText(n) {
    var v = n.nodeValue;
    if (!v || !/[A-Za-z]{2}/.test(v)) return;
    if (done.get(n) === v) return;
    if (skipEl(n.parentElement)) return;
    var t = lookup(v);
    if (t != null) {
      var lead = v.match(/^\s*/)[0], trail = v.match(/\s*$/)[0];
      var nv = lead + t + trail;
      done.set(n, nv);
      if (nv !== v) n.nodeValue = nv;
    }
  }
  var ATTRS = ["placeholder", "title", "aria-label", "alt", "data-tip", "data-title"];
  var orig = new WeakMap();
  function doAttrs(el) {
    if (!el.getAttribute || (el.getAttribute("translate") === "no") || skipEl(el.parentElement)) return;
    var o = orig.get(el) || {};
    for (var i = 0; i < ATTRS.length; i++) {
      var a = ATTRS[i], v = el.getAttribute(a);
      if (!v || !/[A-Za-z]{2}/.test(v)) continue;
      if (o[a] && o[a].out === v) continue;
      var t = lookup(v);
      if (t != null) { o[a] = { out: t }; if (t !== v) el.setAttribute(a, t); }
    }
    if (el.tagName === "INPUT" && /^(submit|button)$/i.test(el.type) && el.value) {
      if (!(o.value && o.value.out === el.value)) { var tv = lookup(el.value); if (tv != null) { o.value = { out: tv }; el.value = tv; } }
    }
    orig.set(el, o);
  }
  function walk(rootEl) {
    if (!ACTIVE || !rootEl) return;
    if (rootEl.nodeType === 3) { doText(rootEl); return; }
    if (rootEl.nodeType !== 1) return;
    if (skipEl(rootEl)) return;
    var w = document.createTreeWalker(rootEl, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT, null), n = rootEl;
    doAttrs(rootEl);
    while ((n = w.nextNode())) { if (n.nodeType === 3) doText(n); else doAttrs(n); }
  }
  function translateTitle() { if (!ACTIVE) return; var t = lookup(document.title); if (t) document.title = t; }

  if (ACTIVE) {
    var st = document.createElement("style");
    st.textContent = "html.lz-i18n-wait body{opacity:0!important}html body{transition:opacity .15s}";
    root.appendChild(st); root.classList.add("lz-i18n-wait");
    var reveal = function () { root.classList.remove("lz-i18n-wait"); };
    setTimeout(reveal, 1500);
    var nativeAlert = window.alert, nativeConfirm = window.confirm, nativePrompt = window.prompt;
    window.alert = function (m) { var t = m != null ? lookup(String(m)) : null; return nativeAlert.call(window, t != null ? t : m); };
    window.confirm = function (m) { var t = m != null ? lookup(String(m)) : null; return nativeConfirm.call(window, t != null ? t : m); };
    window.prompt = function (m, d) { var t = m != null ? lookup(String(m)) : null; return nativePrompt.call(window, t != null ? t : m, d); };
    var start = function () {
      translateTitle(); walk(document.head); walk(document.body); reveal();
      new MutationObserver(function (ms) {
        for (var i = 0; i < ms.length; i++) {
          var m = ms[i];
          if (m.type === "characterData") doText(m.target);
          else if (m.type === "attributes") doAttrs(m.target);
          else for (var j = 0; j < m.addedNodes.length; j++) walk(m.addedNodes[j]);
        }
      }).observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ATTRS.concat(["value"]) });
      var tEl = document.querySelector("title");
      if (tEl) new MutationObserver(translateTitle).observe(tEl, { childList: true, characterData: true, subtree: true });
    };
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
  }

  /* ---------- til tanlagich ---------- */
  function setLang(code) {
    document.cookie = "lz_lang=" + code + "; path=/; max-age=31536000; samesite=lax";
    try { localStorage.removeItem("lz_i18n_" + code); } catch (e) { /* */ }
    location.reload();
  }
  window.LZ_LANG = LANG; window.lzT = function (s) { var t = ACTIVE ? lookup(s) : null; return t != null ? t : s; };
  function buildSwitcher() {
    if (document.querySelector(".lz-lang")) return;
    var cur = LANGS.filter(function (l) { return l.code === LANG; })[0];
    var box = document.createElement("div"); box.className = "lz-lang notranslate"; box.setAttribute("translate", "no");
    var btn = document.createElement("button"); btn.type = "button"; btn.className = "lz-lang-btn";
    btn.setAttribute("aria-haspopup", "listbox"); btn.setAttribute("aria-expanded", "false"); btn.setAttribute("aria-label", "Til / Language");
    btn.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3 12h18M12 2.8c2.6 2.6 3.9 5.6 3.9 9.2s-1.3 6.6-3.9 9.2M12 2.8C9.4 5.4 8.1 8.4 8.1 12s1.3 6.6 3.9 9.2" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><b>' + cur.short + '</b><i aria-hidden="true"></i>';
    var list = document.createElement("ul"); list.className = "lz-lang-list"; list.setAttribute("role", "listbox"); list.hidden = true;
    LANGS.forEach(function (l) {
      var li = document.createElement("li"); li.setAttribute("role", "option"); li.setAttribute("aria-selected", String(l.code === LANG)); li.tabIndex = 0;
      li.className = l.code === LANG ? "is-on" : "";
      li.innerHTML = '<span class="lz-lang-code">' + l.short + '</span><span>' + l.name + '</span>';
      li.addEventListener("click", function () { if (l.code !== LANG) setLang(l.code); else close(); });
      li.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); li.click(); } });
      list.appendChild(li);
    });
    function close() { list.hidden = true; btn.setAttribute("aria-expanded", "false"); box.classList.remove("is-open"); }
    btn.addEventListener("click", function (e) { e.stopPropagation(); var o = list.hidden; list.hidden = !o; btn.setAttribute("aria-expanded", String(o)); box.classList.toggle("is-open", o); });
    document.addEventListener("click", function (e) { if (!box.contains(e.target)) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
    box.appendChild(btn); box.appendChild(list);
    var anchor = document.querySelector(".app-header-actions .theme-toggle, .site-header .theme-toggle, .quiz-header .theme-toggle, header .theme-toggle");
    if (anchor) { anchor.parentNode.insertBefore(box, anchor); }
    else { box.classList.add("is-float"); document.body.appendChild(box); }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", buildSwitcher); else buildSwitcher();
})();
