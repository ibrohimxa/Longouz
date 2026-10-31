/* LongoUZ v229 — sahifadagi [data-news-strip] joyiga eng so'nggi yangiliklarni (rasm bilan) chiqaradi.
   Yangilik bo'lmasa — hech narsa ko'rsatilmaydi (bo'sh blok qolmaydi). */
(function () {
  "use strict";
  var host = document.querySelector("[data-news-strip]");
  if (!host) return;
  function esc(t) { var d = document.createElement("div"); d.textContent = String(t == null ? "" : t); return d.innerHTML; }
  var limit = parseInt(host.getAttribute("data-limit") || "6", 10) || 6;
  fetch("/api/news?limit=" + limit, { credentials: "same-origin" })
    .then(function (r) { return r.ok ? r.json() : { items: [] }; })
    .then(function (d) {
      var items = (d && d.items) || [];
      if (!items.length) { host.hidden = true; return; }
      var title = host.getAttribute("data-title") || "Yangiliklar";
      var wrap = host.getAttribute("data-wrap");
      host.innerHTML = (wrap ? '<div class="' + esc(wrap) + '">' : "") + '<div class="nz-strip-head"><h3>' + esc(title) + '</h3><a href="/news">Barchasi →</a></div><div class="nz-row">' +
        items.map(function (it) {
          var ext = /^https?:/i.test(it.link_url || "");
          return '<article class="nz-card' + ((it.kind === "ad" || it.kind === "promo") ? " nz-ad" : "") + '" data-id="' + it.id + '">' +
            (it.image ? '<div class="nz-img"><img src="' + esc(it.image) + '" alt="" loading="lazy" decoding="async"></div>' : "") +
            '<div class="nz-body"><div class="nz-meta"><span class="nz-tag">' + esc(it.kind_name) + "</span><span>" + esc(it.date) + "</span></div>" +
            (it.title ? "<h4>" + esc(it.title) + "</h4>" : "") + (it.body ? '<p class="nz-text">' + esc(it.body) + "</p>" : "") +
            (it.link_url ? '<a class="nz-link" href="' + esc(it.link_url) + '"' + (ext ? ' target="_blank" rel="noopener"' : "") + ' data-click="' + it.id + '">' + esc(it.link_label || "Batafsil") + " →</a>" : "") +
            "</div></article>";
        }).join("") + "</div>" + (wrap ? "</div>" : "");
      host.hidden = false;
      host.querySelectorAll("[data-click]").forEach(function (a) {
        a.addEventListener("click", function () { try { navigator.sendBeacon("/api/news/" + a.getAttribute("data-click") + "/seen?click=1"); } catch (e) {} });
      });
      // ko'rishlar: karta ekranga chiqqanda bir marta sanaladi
      if ("IntersectionObserver" in window) {
        var seen = {};
        var io = new IntersectionObserver(function (ents) {
          ents.forEach(function (en) {
            var id = en.target.getAttribute("data-id");
            if (en.isIntersecting && id && !seen[id]) { seen[id] = 1; try { navigator.sendBeacon("/api/news/" + id + "/seen"); } catch (e) {} io.unobserve(en.target); }
          });
        }, { threshold: 0.6 });
        host.querySelectorAll(".nz-card").forEach(function (c) { io.observe(c); });
      }
    })
    .catch(function () { host.hidden = true; });
})();
