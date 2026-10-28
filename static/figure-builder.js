// LongoUZ admin — chizma yasovchi: Dekart koordinatalari, geometrik shakllar, rasm, SVG. Jonli ko'rinish bilan.
(function (global) {
  "use strict";
  var KINDS = {
    pt: ["Nuqta", [["x", "x", "n"], ["y", "y", "n"], ["l", "Nomi", "t"]]],
    line: ["Kesma / chiziq", [["x1", "x₁", "n"], ["y1", "y₁", "n"], ["x2", "x₂", "n"], ["y2", "y₂", "n"], ["l", "Nomi", "t"], ["dash", "Punktir", "b"], ["arrow", "Strelka", "b"], ["ext", "Cheksiz davom", "b"]]],
    circle: ["Aylana / doira", [["cx", "Markaz x", "n"], ["cy", "Markaz y", "n"], ["r", "Radius", "n"], ["l", "Nomi", "t"], ["fill", "To'ldirilgan", "b"], ["dash", "Punktir", "b"]]],
    arc: ["Yoy (burchak)", [["cx", "Markaz x", "n"], ["cy", "Markaz y", "n"], ["r", "Radius", "n"], ["a1", "Boshi °", "n"], ["a2", "Oxiri °", "n"], ["l", "Yozuv", "t"]]],
    poly: ["Ko'pburchak", [["pts", "Uchlar (x,y; x,y; …)", "p"], ["names", "Uch nomlari (A,B,C)", "nm"], ["fill", "To'ldirilgan", "b"], ["closed", "Yopiq", "b"]]],
    fn: ["Funksiya grafigi", [["f", "y = f(x), masalan x^2-2 yoki sin(x)", "t"]]],
    text: ["Yozuv", [["x", "x", "n"], ["y", "y", "n"], ["t", "Matn", "t"]]],
  };
  var PRESETS = {
    uchburchak: ["Uchburchak", { pts: [[0, 0], [6, 0], [2, 4]], names: ["A", "B", "C"] }],
    togri: ["To'g'ri burchakli △", { pts: [[0, 0], [6, 0], [0, 4]], names: ["A", "B", "C"] }],
    tortburchak: ["To'rtburchak", { pts: [[0, 0], [6, 0], [6, 4], [0, 4]], names: ["A", "B", "C", "D"] }],
    kvadrat: ["Kvadrat", { pts: [[0, 0], [4, 0], [4, 4], [0, 4]], names: ["A", "B", "C", "D"] }],
    trapetsiya: ["Trapetsiya", { pts: [[0, 0], [7, 0], [5, 4], [2, 4]], names: ["A", "B", "C", "D"] }],
    parallelogramm: ["Parallelogramm", { pts: [[0, 0], [6, 0], [8, 4], [2, 4]], names: ["A", "B", "C", "D"] }],
    romb: ["Romb", { pts: [[0, 3], [4, 0], [8, 3], [4, 6]], names: ["A", "B", "C", "D"] }],
  };

  function h(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function ptsToText(p) { return (p || []).map(function (q) { return q[0] + "," + q[1]; }).join("; "); }
  function textToPts(t) {
    return String(t).split(/;|\n/).map(function (s) { var m = s.split(","); return [parseFloat(m[0]), parseFloat(m[1])]; })
      .filter(function (q) { return isFinite(q[0]) && isFinite(q[1]); });
  }
  function emptyPlane(geom) { return { type: "plane", xmin: geom ? -1 : -6, xmax: geom ? 9 : 6, ymin: geom ? -1 : -6, ymax: geom ? 7 : 6, axes: !geom, grid: !geom, equal: true, items: [] }; }

  function mount(host, opts) {
    opts = opts || {};
    var spec = opts.value || null;
    var onChange = opts.onChange || function () {};
    var uploadUrl = opts.uploadUrl;
    var root = h("div", "fb");
    host.innerHTML = ""; host.appendChild(root);

    var typeSel = h("select"); typeSel.setAttribute("aria-label", "Chizma turi");
    [["", "Chizma yo'q"], ["plane", "Koordinata tekisligi (Dekart)"], ["geom", "Geometrik shakl"], ["image", "Rasm yuklash"], ["svg", "SVG kod"]].forEach(function (o) {
      var op = h("option", null, o[1]); op.value = o[0]; typeSel.appendChild(op);
    });
    var body = h("div", "fb-body"), prev = h("div", "fb-prev");
    root.append(typeSel, body, prev);

    function kindOf(s) { return !s ? "" : s.type === "plane" ? (s.axes ? "plane" : "geom") : s.type; }
    function emit() { render(); onChange(spec); }

    function render() {
      prev.innerHTML = "";
      if (!spec) return;
      if (spec.type === "svg") {
        var img = new Image(); img.className = "lzf-img"; img.alt = "SVG";
        img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(spec.svg || "<svg xmlns='http://www.w3.org/2000/svg'/>");
        prev.appendChild(img);
      } else prev.appendChild(global.LZFigure.render(spec));
    }

    function numInput(obj, key, step) {
      var i = h("input"); i.type = "number"; i.step = step || "any"; i.value = obj[key] != null ? obj[key] : 0;
      i.addEventListener("input", function () { var v = parseFloat(i.value); if (isFinite(v)) { obj[key] = v; emit(); } });
      return i;
    }

    function buildPlane() {
      body.innerHTML = "";
      var rng = h("div", "fb-range");
      [["xmin", "x min"], ["xmax", "x max"], ["ymin", "y min"], ["ymax", "y max"]].forEach(function (f) {
        var l = h("label", "afield", f[1]); l.appendChild(numInput(spec, f[0])); rng.appendChild(l);
      });
      body.appendChild(rng);
      var flags = h("div", "fb-flags");
      [["axes", "O'qlar"], ["grid", "To'r (setka)"]].forEach(function (f) {
        var l = h("label", "fb-check"); var c = h("input"); c.type = "checkbox"; c.checked = !!spec[f[0]];
        c.addEventListener("change", function () { spec[f[0]] = c.checked; emit(); });
        l.append(c, document.createTextNode(" " + f[1])); flags.appendChild(l);
      });
      body.appendChild(flags);

      var list = h("div", "fb-items"); body.appendChild(list);
      function drawItems() {
        list.innerHTML = "";
        spec.items.forEach(function (it, idx) {
          var def = KINDS[it.k]; if (!def) return;
          var row = h("div", "fb-item");
          row.appendChild(h("b", null, def[0]));
          var fields = h("div", "fb-fields");
          def[1].forEach(function (f) {
            var key = f[0], lab = h("label", f[2] === "b" ? "fb-check" : "afield");
            if (f[2] === "b") {
              var c = h("input"); c.type = "checkbox"; c.checked = key === "closed" ? it.closed !== false : !!it[key];
              c.addEventListener("change", function () { it[key] = c.checked; emit(); }); lab.append(c, document.createTextNode(" " + f[1]));
            } else {
              lab.appendChild(document.createTextNode(f[1]));
              var inp;
              if (f[2] === "n") inp = numInput(it, key);
              else {
                inp = h("input"); inp.type = "text"; inp.maxLength = 120;
                inp.value = f[2] === "p" ? ptsToText(it.pts) : f[2] === "nm" ? (it.names || []).join(",") : (it[key] || "");
                inp.addEventListener("input", function () {
                  if (f[2] === "p") it.pts = textToPts(inp.value);
                  else if (f[2] === "nm") it.names = inp.value.split(",").map(function (s) { return s.trim(); });
                  else it[key] = inp.value;
                  emit();
                });
              }
              lab.appendChild(inp);
            }
            fields.appendChild(lab);
          });
          row.appendChild(fields);
          var del = h("button", "abtn danger", "×"); del.type = "button"; del.title = "Olib tashlash";
          del.addEventListener("click", function () { spec.items.splice(idx, 1); drawItems(); emit(); });
          row.appendChild(del); list.appendChild(row);
        });
      }
      drawItems();

      var add = h("div", "fb-add");
      add.appendChild(h("span", "ahint", "Element qo'shish:"));
      Object.keys(KINDS).forEach(function (k) {
        var b = h("button", "abtn", "+ " + KINDS[k][0]); b.type = "button";
        b.addEventListener("click", function () {
          var base = { k: k };
          if (k === "pt") Object.assign(base, { x: 1, y: 1, l: "A" });
          if (k === "line") Object.assign(base, { x1: 0, y1: 0, x2: 3, y2: 3, l: "" });
          if (k === "circle") Object.assign(base, { cx: 0, cy: 0, r: 2 });
          if (k === "arc") Object.assign(base, { cx: 0, cy: 0, r: 1, a1: 0, a2: 60, l: "α" });
          if (k === "poly") Object.assign(base, { pts: [[0, 0], [3, 0], [0, 3]], names: ["A", "B", "C"], closed: true });
          if (k === "fn") Object.assign(base, { f: "x^2-2" });
          if (k === "text") Object.assign(base, { x: 1, y: 1, t: "Yozuv" });
          spec.items.push(base); drawItems(); emit();
        });
        add.appendChild(b);
      });
      body.appendChild(add);
      var pre = h("div", "fb-add");
      pre.appendChild(h("span", "ahint", "Tayyor shakllar:"));
      Object.keys(PRESETS).forEach(function (k) {
        var b = h("button", "abtn", PRESETS[k][0]); b.type = "button";
        b.addEventListener("click", function () {
          spec.items.push({ k: "poly", pts: PRESETS[k][1].pts.map(function (p) { return p.slice(); }), names: PRESETS[k][1].names.slice(), closed: true });
          drawItems(); emit();
        });
        pre.appendChild(b);
      });
      body.appendChild(pre);
    }

    function buildImage() {
      body.innerHTML = "";
      var f = h("input"); f.type = "file"; f.accept = "image/png,image/jpeg,image/webp,image/gif,image/svg+xml";
      var st = h("p", "ahint", spec && spec.src ? "Rasm yuklangan. Almashtirish uchun yangi fayl tanlang." : "PNG, JPG, WEBP, GIF yoki SVG (8 MB gacha).");
      f.addEventListener("change", function () {
        if (!f.files[0]) return;
        var fd = new FormData(); fd.append("file", f.files[0]); st.textContent = "Yuklanmoqda…";
        fetch(uploadUrl, { method: "POST", body: fd, credentials: "same-origin", headers: { "X-Requested-With": "fetch" } })
          .then(function (r) { return r.json().then(function (d) { if (!r.ok) throw new Error(d.detail || "Xatolik"); return d; }); })
          .then(function (d) { spec = d.figure; st.textContent = "Yuklandi."; emit(); })
          .catch(function (e) { st.textContent = "Xato: " + e.message; });
      });
      body.append(f, st);
    }
    function buildSvg() {
      body.innerHTML = "";
      var t = h("textarea"); t.rows = 6; t.placeholder = '<svg viewBox="0 0 200 120">…</svg>'; t.value = (spec && spec.svg) || "";
      t.addEventListener("input", function () { spec = { type: "svg", svg: t.value }; emit(); });
      body.append(t, h("p", "ahint", "Xavfsizlik uchun skriptlar va tashqi havolalar saqlashda avtomatik olib tashlanadi."));
    }

    typeSel.addEventListener("change", function () {
      var k = typeSel.value;
      if (!k) spec = null;
      else if (k === "plane") spec = emptyPlane(false);
      else if (k === "geom") spec = emptyPlane(true);
      else if (k === "image") spec = { type: "image", src: "", alt: "" };
      else spec = { type: "svg", svg: "" };
      build(); render(); onChange(spec);
    });
    function build() {
      var k = kindOf(spec);
      typeSel.value = k;
      if (k === "plane" || k === "geom") buildPlane(); else if (k === "image") buildImage(); else if (k === "svg") buildSvg(); else body.innerHTML = "";
    }
    build(); render();
    return {
      get: function () { if (spec && spec.type === "image" && !spec.src) return null; return spec; },
      set: function (v) { spec = v ? JSON.parse(JSON.stringify(v)) : null; build(); render(); },
    };
  }
  global.LZFigBuilder = { mount: mount };
})(window);
