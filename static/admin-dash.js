(function () {
  "use strict";
  var host = document.getElementById("ad-chart"), raw = document.getElementById("ad-data");
  if (!host || !raw) return;
  var d; try { d = JSON.parse(raw.textContent); } catch (e) { return; }
  function draw() {
    var W = Math.max(280, host.clientWidth || 640), H = 210, L = 28, B = 24, T = 10, n = d.days.length;
    var max = Math.max(4, Math.max.apply(null, d.quizzes.concat(d.signups)));
    var step = (W - L) / n, bw = Math.max(3, Math.min(14, step / 2 - 2)), ph = H - B - T;
    var svg = '<svg viewBox="0 0 ' + W + " " + H + '">';
    for (var g = 0; g <= 4; g++) { var y = T + ph - (ph * g) / 4; svg += '<line class="grid" x1="' + L + '" x2="' + W + '" y1="' + y + '" y2="' + y + '"/><text class="tx" x="' + (L - 5) + '" y="' + (y + 3) + '" text-anchor="end">' + Math.round((max * g) / 4) + "</text>"; }
    d.days.forEach(function (day, i) {
      var cx = L + step * i + step / 2, ha = (d.quizzes[i] / max) * ph, hb = (d.signups[i] / max) * ph;
      svg += '<rect class="bar-a" x="' + (cx - bw - 1) + '" y="' + (T + ph - ha) + '" width="' + bw + '" height="' + ha + '" rx="2"><title>' + day + ": " + d.quizzes[i] + " test</title></rect>";
      svg += '<rect class="bar-b" x="' + (cx + 1) + '" y="' + (T + ph - hb) + '" width="' + bw + '" height="' + hb + '" rx="2"><title>' + day + ": " + d.signups[i] + " yangi</title></rect>";
      if (i % Math.ceil(n / 7) === 0 || i === n - 1) svg += '<text class="tx" x="' + cx + '" y="' + (H - 7) + '" text-anchor="middle">' + day + "</text>";
    });
    host.innerHTML = svg + "</svg>";
  }
  draw();
  var t; window.addEventListener("resize", function () { clearTimeout(t); t = setTimeout(draw, 150); });
})();
