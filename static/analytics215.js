(function () {
  "use strict";
  const $ = (id) => document.getElementById(id);
  const esc = (t) => { const d = document.createElement("div"); d.textContent = String(t == null ? "" : t); return d.innerHTML; };
  fetch("/api/analytics", { credentials: "same-origin" }).then((r) => r.json()).then(render).catch(() => { $("an-root").innerHTML = "<p class='f215-muted'>Ma'lumotni yuklab bo'lmadi.</p>"; });

  function render(d) {
    const o = d.overview;
    if (!o.attempts) { $("an-empty").hidden = false; $("an-root").hidden = true; return; }
    $("an-stats").innerHTML = [
      [o.attempts, "yechilgan test"], [o.questions, "ishlangan savol"], [o.accuracy + "%", "o'rtacha aniqlik"], [o.this_week, "shu hafta savollar"],
    ].map((x) => `<div class="f215-stat"><b>${x[0]}</b><span>${x[1]}</span></div>`).join("");
    const mx = Math.max(1, ...d.weekly.map((w) => w.total));
    $("an-week").innerHTML = d.weekly.map((w) => `<div class="f215-bar"><small>${w.total ? w.percent + "%" : ""}</small><i style="height:${Math.max(3, w.total / mx * 100)}%"></i><em>${w.day}</em></div>`).join("");
    $("an-week-note").textContent = o.this_week ? `Shu hafta ${o.this_week} ta savol ishladingiz. Ustun balandligi — savollar soni, ustidagi son — aniqlik.` : "Shu hafta hali test yechmadingiz.";
    $("an-subj").innerHTML = d.subjects.map((s) => {
      if (!s.attempts) return `<div class="f215-subj"><span>${esc(s.name)}</span><div class="f215-meter"></div><span class="f215-muted">—</span></div>`;
      const tr = s.trend ? `<small class="${s.trend > 0 ? "f215-up" : "f215-down"}">${s.trend > 0 ? "▲" : "▼"}${Math.abs(s.trend)}</small>` : "";
      return `<div class="f215-subj"><span>${esc(s.name)}</span><div class="f215-meter"><i style="width:${s.percent}%"></i></div><b>${s.percent}% ${tr}</b></div>`;
    }).join("");
    const topicRow = (t) => `<div class="f215-weak"><span>${esc(t.topic)} <small class="f215-muted">· ${esc(t.subject_name)}</small></span><b>${t.percent}%</b></div>`;
    $("an-weak").innerHTML = d.weak.length ? d.weak.map(topicRow).join("") : "<p class='f215-muted'>Mavzu bo'yicha kamida 5 ta savol ishlang — kuchsiz tomonlar shu yerda chiqadi.</p>";
    $("an-strong").innerHTML = d.strong.length ? d.strong.map(topicRow).join("") : "<p class='f215-muted'>Hozircha ma'lumot yetarli emas.</p>";
    // prognoz
    const byCode = {}; d.subjects.forEach((s) => { byCode[s.code] = s; });
    const opts = d.subjects.map((s) => `<option value="${s.code}">${esc(s.name)}</option>`).join("");
    const s1 = $("an-s1"), s2 = $("an-s2"); s1.innerHTML = opts; s2.innerHTML = opts;
    const ranked = d.subjects.filter((s) => d.mandatory.indexOf(s.code) < 0 || true).slice().sort((a, b) => (b.forecast || 0) - (a.forecast || 0));
    const pick = ranked.filter((s) => s.forecast != null).map((s) => s.code);
    s1.value = pick[0] || "physics"; s2.value = pick.find((c) => c !== s1.value) || "chemistry";
    function forecast() {
      const w = d.weights; let total = 0, missing = [];
      const part = (code, n, coef) => { const s = byCode[code]; if (!s || s.forecast == null) { missing.push(s ? s.name : code); return 0; } return s.forecast / 100 * n * coef; };
      d.mandatory.forEach((c) => { total += part(c, w.mandatory.count, w.mandatory.coef); });
      total += part(s1.value, w.spec1.count, w.spec1.coef);
      if (s2.value !== s1.value) total += part(s2.value, w.spec2.count, w.spec2.coef);
      $("an-ball").textContent = total.toFixed(1);
      $("an-fnote").textContent = (s1.value === s2.value ? "Ikki xil ixtisoslik fanini tanlang. " : "") + (missing.length ? "Ma'lumot yo'q (0 deb olindi): " + missing.join(", ") + "." : "Prognoz tegishli fanlardagi so'nggi natijalaringizga asoslangan.");
    }
    s1.addEventListener("change", forecast); s2.addEventListener("change", forecast); forecast();
  }
})();
