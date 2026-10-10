/* Engine: state + save, learning records (SRS), skills, audio clips, world rendering,
   movement, interaction, minimap, HUD. UI panels live in ui.js. */
(function () {
  "use strict";
  var A = window.ART, Wd = window.WORLD, LEX = window.LEX;
  var T = A.T, VW = 20, VH = 11;
  var SAVE_KEY = "inuttitut-rpg-v1";
  var SKILLS = { listen: 1, speak: 1, rw: 1, gram: 1 };
  var t = function (k, v) { return window.L10N.t(k, v); };
  var LEVEL_XP = [0, 20, 50, 100, 170];
  var BOX_MIN = [0, 3, 20, 120, 720, 2880]; // review intervals in minutes per Leitner box

  var G = window.G = { SKILLS: SKILLS, LEVEL_XP: LEVEL_XP, VW: VW, VH: VH };
  G.skillName = function (k) { return t("skill_" + k); };

  /* ------------------------------------------------------------ state */
  function fresh() {
    var u = {}; LEX.units.forEach(function (x) { u[x.id] = { passed: false, best: 0 }; });
    var aff = {}; Wd.NPCS.forEach(function (n) { aff[n.id] = 0; });
    return { v: 1, home: null, px: 5, py: 19, dir: 0, flags: {}, quest: 0, units: u, items: {},
             xp: { listen: 0, speak: 0, rw: 0, gram: 0 }, aff: aff, introDone: false, ended: false,
             settings: { sound: true, trans: "both" }, savedAt: 0 };
  }
  G.state = fresh();
  G.hasSave = function () { try { return !!localStorage.getItem(SAVE_KEY); } catch (e) { return false; } };
  G.save = function () {
    if (!G.state.introDone) return; // nothing to save before a game has started
    G.state.px = G.player.x; G.state.py = G.player.y; G.state.dir = G.player.dir; G.state.savedAt = Date.now();
    try { localStorage.setItem(SAVE_KEY, JSON.stringify(G.state)); } catch (e) { /* storage unavailable: play continues unsaved */ }
  };
  G.load = function () {
    try {
      var s = JSON.parse(localStorage.getItem(SAVE_KEY));
      if (s && s.v === 1) { var f = fresh(); Object.keys(f).forEach(function (k) { if (s[k] === undefined) s[k] = f[k]; }); G.state = s; }
    } catch (e) { G.state = fresh(); }
    G.player.x = G.state.px; G.player.y = G.state.py; G.player.dir = G.state.dir; G.player.rx = G.player.x; G.player.ry = G.player.y;
  };
  G.reset = function () { try { localStorage.removeItem(SAVE_KEY); } catch (e) {} G.state = fresh(); G.player.x = 5; G.player.y = 19; G.player.rx = 5; G.player.ry = 19; };

  /* ------------------------------------------------------------ learning records */
  function rec(id) { var r = G.state.items[id]; if (!r) r = G.state.items[id] = { st: 0, box: 0, due: 0, ok: 0, ng: 0, typed: 0, replied: 0, where: "" }; return r; }
  G.rec = rec;
  G.discover = function (id, where) { var r = rec(id); if (r.st < 1) { r.st = 1; r.due = Date.now(); if (where) r.where = where; G.hud(); } else if (where && !r.where) r.where = where; };
  G.result = function (id, ok, how) {
    var r = rec(id); if (r.st < 1) r.st = 1;
    if (ok) {
      r.ok++; r.box = Math.min(5, r.box + 1);
      if (how === "typed") r.typed++;
      if (how === "replied") r.replied++;
      if (r.st < 2) r.st = 2;
      if (r.typed >= 1 || r.replied >= 2) r.st = 3;
    } else { r.ng++; r.box = Math.max(0, r.box - 1); }
    r.due = Date.now() + BOX_MIN[r.box] * 60000;
  };
  G.stateLabel = function (st) { return t("st" + (st || 0)); };
  G.completion = function () { var n = 0; LEX.items.forEach(function (it) { if ((G.state.items[it.id] || {}).st === 3) n++; }); return { done: n, total: LEX.items.length }; };

  /* ------------------------------------------------------------ skills */
  G.level = function (k) { var x = G.state.xp[k], l = 0; LEVEL_XP.forEach(function (t) { if (x >= t) l++; }); return l; };
  G.addXP = function (k, n) {
    var before = G.level(k); G.state.xp[k] += n; var after = G.level(k);
    if (after > before) { G.sfx("level"); window.UI && UI.toast(t("levelUp", { s: G.skillName(k), n: after }) + (k === "speak" && after >= 2 ? t("levelUpSpeak") : "")); }
    G.hud();
  };

  /* ------------------------------------------------------------ quests */
  G.quest = function () { return Wd.QUESTS[G.state.quest] || null; };
  G.objDone = function (key) {
    if (G.state.flags[key]) return;
    G.state.flags[key] = true;
    var q = G.quest();
    if (q && q.obj.every(function (o) { return G.state.flags[o[0]]; })) {
      G.sfx("level");
      if (q.unlocks) { G.state.flags["gate:" + q.unlocks] = true; }
      window.UI && UI.toast(t("questDone", { t: L10N.plain(q.title) }) + (q.unlocks === "east" ? t("eastOpen") : q.unlocks === "north" ? t("northOpen") : ""));
      G.state.quest++;
      var nq = G.quest();
      if (nq) setTimeout(function () { UI.toast(t("newQuest", { t: L10N.plain(nq.title) })); }, 1600);
    }
    G.save(); G.hud();
  };
  G.unitAvailable = function (uid) {
    var ok = false;
    Object.keys(Wd.TEACH).forEach(function (npc) { Wd.TEACH[npc].forEach(function (t) { if (t[0] === uid && qIndex(t[1]) <= G.state.quest) ok = true; }); });
    return ok;
  };
  function qIndex(qid) { for (var i = 0; i < Wd.QUESTS.length; i++) if (Wd.QUESTS[i].id === qid) return i; return 99; }
  G.qIndex = qIndex;
  G.nextObjective = function () {
    var q = G.quest(); if (!q) return null;
    for (var i = 0; i < q.obj.length; i++) if (!G.state.flags[q.obj[i][0]]) return q.obj[i];
    return null;
  };

  /* ------------------------------------------------------------ sound effects (no speech is synthesised) */
  var ac = null;
  G.sfx = function (kind) {
    if (!G.state.settings.sound) return;
    try {
      ac = ac || new (window.AudioContext || window.webkitAudioContext)();
      var notes = { ok: [660, 880], ng: [220], talk: [520], level: [523, 659, 784], open: [440, 660] }[kind] || [440];
      notes.forEach(function (f, i) {
        var o = ac.createOscillator(), g = ac.createGain(), t = ac.currentTime + i * 0.09;
        o.type = kind === "ng" ? "triangle" : "square"; o.frequency.value = f;
        g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.05, t + 0.01); g.gain.exponentialRampToValueAtTime(0.0001, t + 0.16);
        o.connect(g); g.connect(ac.destination); o.start(t); o.stop(t + 0.18);
      });
    } catch (e) {}
  };

  /* ------------------------------------------------------------ audio clips (real recordings only)
     Two slots per item: "model" (a speaker's recording) and "self" (the learner's own voice).
     Stored in IndexedDB in this browser. Bundled recordings can be listed in window.AUDIO_FILES. */
  var db = null, clipKeys = {};
  function idb(cb) {
    if (db) return cb(db);
    try {
      var rq = indexedDB.open("inuttitut-rpg-audio", 1);
      rq.onupgradeneeded = function () { rq.result.createObjectStore("clips"); };
      rq.onsuccess = function () { db = rq.result; cb(db); };
      rq.onerror = function () { cb(null); };
    } catch (e) { cb(null); }
  }
  G.audioInit = function (done) {
    idb(function (d) {
      if (!d) return done && done();
      var tx = d.transaction("clips", "readonly").objectStore("clips").getAllKeys();
      tx.onsuccess = function () { tx.result.forEach(function (k) { clipKeys[k] = true; }); done && done(); };
      tx.onerror = function () { done && done(); };
    });
  };
  G.hasClip = function (id, slot) { return !!clipKeys[id + "|" + slot] || (slot === "model" && window.AUDIO_FILES && window.AUDIO_FILES[id]); };
  G.playClip = function (id, slot, rate) {
    var bundled = slot === "model" && window.AUDIO_FILES && window.AUDIO_FILES[id];
    function go(src) { var a = new Audio(src); a.playbackRate = rate || 1; a.play().catch(function () {}); }
    if (clipKeys[id + "|" + slot]) {
      idb(function (d) { if (!d) return; var g = d.transaction("clips", "readonly").objectStore("clips").get(id + "|" + slot); g.onsuccess = function () { if (g.result) go(URL.createObjectURL(g.result)); }; });
      return true;
    }
    if (bundled) { go(bundled); return true; }
    return false;
  };
  G.recordClip = function (id, slot, onState) {
    if (!navigator.mediaDevices || !window.MediaRecorder) { onState("unsupported"); return null; }
    var ctl = { stop: function () {} };
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function (stream) {
      var chunks = [], mr = new MediaRecorder(stream);
      mr.ondataavailable = function (e) { chunks.push(e.data); };
      mr.onstop = function () {
        stream.getTracks().forEach(function (t) { t.stop(); });
        var blob = new Blob(chunks, { type: mr.mimeType || "audio/webm" });
        idb(function (d) { if (!d) return onState("error"); var tx = d.transaction("clips", "readwrite"); tx.objectStore("clips").put(blob, id + "|" + slot); tx.oncomplete = function () { clipKeys[id + "|" + slot] = true; onState("saved"); }; });
      };
      mr.start(); onState("recording");
      ctl.stop = function () { if (mr.state !== "inactive") mr.stop(); };
      setTimeout(ctl.stop, 6000);
    }).catch(function () { onState("denied"); });
    return ctl;
  };
  G.deleteClip = function (id, slot, done) {
    idb(function (d) { if (!d) return; var tx = d.transaction("clips", "readwrite"); tx.objectStore("clips").delete(id + "|" + slot); tx.oncomplete = function () { delete clipKeys[id + "|" + slot]; done && done(); }; });
  };

  /* ------------------------------------------------------------ world */
  var canvas, ctx, mini, mctx;
  G.player = { x: 5, y: 19, rx: 5, ry: 19, dir: 0, moving: false, t0: 0, fx: 5, fy: 19, step: 0 };
  var DIRS = [[0, 1], [0, -1], [-1, 0], [1, 0]]; // down, up, left, right
  G.busy = function () { return window.UI && UI.isOpen(); };

  function gateAt(x, y) { return Wd.gates[x + "," + y]; }
  G.tileAt = function (x, y) {
    if (x < 0 || y < 0 || x >= Wd.W || y >= Wd.H) return "mtn";
    var g = gateAt(x, y); if (g && G.state.flags["gate:" + g]) return "path";
    return Wd.grid[y][x];
  };
  function npcAt(x, y) { for (var i = 0; i < Wd.NPCS.length; i++) { var n = Wd.NPCS[i]; if (n.x === x && n.y === y) return n; } return null; }
  function dogAt(x, y) { for (var i = 0; i < Wd.DOGS.length; i++) if (Wd.DOGS[i].x === x && Wd.DOGS[i].y === y) return Wd.DOGS[i]; return null; }
  function blocked(x, y) { return !!Wd.SOLID[G.tileAt(x, y)] || !!npcAt(x, y) || !!dogAt(x, y); }

  var keys = {}, lastBump = 0;
  G.input = { dir: -1 };
  function tryMove(d) {
    var p = G.player; p.dir = d;
    var nx = p.x + DIRS[d][0], ny = p.y + DIRS[d][1];
    if (blocked(nx, ny)) {
      var g = gateAt(nx, ny);
      if (g && !G.state.flags["gate:" + g] && Date.now() - lastBump > 1500) {
        lastBump = Date.now();
        UI.toast(g === "east" ? t("gateEast") : t("gateNorth"));
      }
      return;
    }
    p.fx = p.x; p.fy = p.y; p.x = nx; p.y = ny; p.moving = true; p.t0 = performance.now(); p.step ^= 1;
  }
  G.interact = function () {
    if (G.busy()) return;
    var p = G.player, fx = p.x + DIRS[p.dir][0], fy = p.y + DIRS[p.dir][1];
    var tl = G.tileAt(fx, fy), n = npcAt(fx, fy);
    if (!n && tl === "stall") n = npcAt(fx + DIRS[p.dir][0], fy + DIRS[p.dir][1]);
    if (n) { faceNpc(n); return UI.talk(n); }
    if (dogAt(fx, fy)) return UI.narr([t("dogs")]);
    var key = fx + "," + fy;
    if (tl === "sign" && Wd.SIGNS[key]) return UI.narr([Wd.SIGNS[key]]);
    if (tl === "door" && Wd.DOORS[key]) return UI.narr([Wd.DOORS[key]]);
    if (tl === "fire") return UI.camp();
    if (tl === "drift") return UI.narr([gateAt(fx, fy) === "east" ? t("driftEast") : t("driftNorth")]);
  };
  function faceNpc(n) { var p = G.player; n.dir = p.x < n.x ? 2 : p.x > n.x ? 3 : p.y < n.y ? 1 : 0; }

  /* ------------------------------------------------------------ particles */
  var flakes = [], smoke = [];
  for (var i = 0; i < 46; i++) flakes.push({ x: Math.random() * VW * T, y: Math.random() * VH * T, s: 0.15 + Math.random() * 0.35, d: Math.random() * 6 });

  /* ------------------------------------------------------------ render */
  var cam = { x: 0, y: 0 };
  function render(now) {
    var p = G.player;
    if (p.moving) {
      var k = Math.min(1, (now - p.t0) / 150);
      p.rx = p.fx + (p.x - p.fx) * k; p.ry = p.fy + (p.y - p.fy) * k;
      if (k >= 1) { p.moving = false; p.rx = p.x; p.ry = p.y; }
    }
    if (!p.moving && !G.busy()) { var d = G.input.dir; if (d >= 0) tryMove(d); }
    cam.x = Math.max(0, Math.min(Wd.W - VW, p.rx - (VW - 1) / 2));
    cam.y = Math.max(0, Math.min(Wd.H - VH, p.ry - (VH - 1) / 2));
    var ox = Math.round(cam.x * T), oy = Math.round(cam.y * T);
    ctx.fillStyle = "#eef3f8"; ctx.fillRect(0, 0, VW * T, VH * T);
    var tf = Math.floor(now / 400);
    var x0 = Math.floor(cam.x), y0 = Math.floor(cam.y);
    for (var y = y0; y <= y0 + VH; y++) for (var x = x0; x <= x0 + VW; x++) {
      var t = G.tileAt(x, y), fr = A.tiles[t] || A.tiles.snow;
      ctx.drawImage(fr[(t === "fire" ? Math.floor(now / 160) : tf) % fr.length], x * T - ox, y * T - oy);
      if (t === "chimney" && Math.random() < 0.03) smoke.push({ x: x * T + 8, y: y * T, a: 1 });
    }
    // dogs
    Wd.DOGS.forEach(function (dg) { ctx.drawImage(A.sprites.dog[Math.floor(now / 500 + dg.x) % 2], dg.x * T - ox, dg.y * T - oy); });
    // characters sorted by y
    var chars = Wd.NPCS.map(function (n) { return { k: n.sprite, x: n.x, y: n.y, d: n.dir, f: 0, n: n }; });
    chars.push({ k: "player", x: p.rx, y: p.ry, d: p.dir, f: p.moving ? p.step : 0 });
    chars.sort(function (a, b) { return a.y - b.y; });
    var target = G.nextObjective();
    chars.forEach(function (c) {
      var sx = Math.round(c.x * T - ox), sy = Math.round(c.y * T - oy);
      ctx.fillStyle = "rgba(60,80,110,.18)"; ctx.fillRect(sx + 3, sy + 14, 10, 2);
      ctx.drawImage(A.sprites[c.k][c.d][c.f], sx, sy);
      if (c.n) {
        var locked = G.level("speak") < c.n.speak;
        var want = target && target[2] === c.n.id;
        if (locked || want) bubble(sx, sy - 9, locked ? "…" : "!", locked ? "#9aa6b5" : "#e9a23b", now);
      }
    });
    // smoke
    smoke.forEach(function (s) { s.y -= 0.18; s.x += Math.sin(s.y / 6) * 0.15; s.a -= 0.006; ctx.fillStyle = "rgba(200,206,214," + Math.max(0, s.a) + ")"; ctx.fillRect(Math.round(s.x - ox), Math.round(s.y - oy), 3, 3); });
    smoke = smoke.filter(function (s) { return s.a > 0; });
    // snow
    ctx.fillStyle = "rgba(255,255,255,.9)";
    flakes.forEach(function (f) { f.y += f.s; f.x += Math.sin((now / 900) + f.d) * 0.12; if (f.y > VH * T) { f.y = -2; f.x = Math.random() * VW * T; } ctx.fillRect(Math.round(f.x), Math.round(f.y), 1, 1); });
    drawMini(now);
    requestAnimationFrame(render);
  }
  function bubble(x, y, ch, col, now) {
    var bob = Math.floor(now / 300) % 2;
    ctx.fillStyle = "#1e2a44"; ctx.fillRect(x + 4, y - bob, 9, 8);
    ctx.fillStyle = "#ffffff"; ctx.fillRect(x + 5, y + 1 - bob, 7, 6); ctx.fillRect(x + 7, y + 8 - bob, 2, 1);
    ctx.fillStyle = col;
    if (ch === "!") { ctx.fillRect(x + 8, y + 2 - bob, 1, 3); ctx.fillRect(x + 8, y + 6 - bob, 1, 1); }
    else { ctx.fillRect(x + 6, y + 5 - bob, 1, 1); ctx.fillRect(x + 8, y + 5 - bob, 1, 1); ctx.fillRect(x + 10, y + 5 - bob, 1, 1); }
  }

  /* ------------------------------------------------------------ minimap */
  var MCOL = { snow: "#eef3f8", snow2: "#eef3f8", path: "#cbbfae", sea: "#3b6c90", ice: "#a9cde4", dock: "#8a5a35", strip: "#b9c3ce", stripMark: "#b9c3ce",
               roof: "#3a4a66", chimney: "#3a4a66", wall: "#7a4e2d", window: "#f2b547", door: "#4a2e1c", tree: "#2f5b4a", rock: "#7c8794", fence: "#7a4e2d",
               drift: "#d9534f", sign: "#7a4e2d", stall: "#d06a3a", fire: "#f28c28", tent: "#c9a46a", mtn: "#8ea3bb", boat: "#c84b31", plane: "#d9534f", doghouse: "#7a4e2d" };
  var miniBase = null;
  function drawMini(now) {
    if (!mctx) return;
    if (!miniBase || miniBase._q !== JSON.stringify(G.state.flags)) {
      miniBase = document.createElement("canvas"); miniBase.width = Wd.W * 2; miniBase.height = Wd.H * 2; miniBase._q = JSON.stringify(G.state.flags);
      var b = miniBase.getContext("2d");
      for (var y = 0; y < Wd.H; y++) for (var x = 0; x < Wd.W; x++) { b.fillStyle = MCOL[G.tileAt(x, y)] || "#eef3f8"; b.fillRect(x * 2, y * 2, 2, 2); }
    }
    mctx.drawImage(miniBase, 0, 0);
    var tgt = G.nextObjective();
    Wd.NPCS.forEach(function (n) {
      var on = tgt && tgt[2] === n.id && Math.floor(now / 400) % 2;
      mctx.fillStyle = on ? "#e9a23b" : "#ffffff"; mctx.fillRect(n.x * 2 - (on ? 1 : 0), n.y * 2 - (on ? 1 : 0), on ? 4 : 2, on ? 4 : 2);
    });
    mctx.fillStyle = "#1e2a44"; mctx.fillRect(Math.round(G.player.rx * 2) - 1, Math.round(G.player.ry * 2) - 1, 4, 4);
    mctx.strokeStyle = "rgba(30,42,68,.6)"; mctx.strokeRect(cam.x * 2 + 0.5, cam.y * 2 + 0.5, VW * 2, VH * 2);
  }

  /* ------------------------------------------------------------ HUD */
  G.hud = function () {
    var q = G.quest(), o = G.nextObjective();
    var qEl = document.getElementById("hud-quest");
    if (qEl) qEl.innerHTML = q ? "<b>" + L10N.mark(q.title) + "</b><span>" + (o ? "▶ " + L10N.mark(o[1]) : "") + "</span>" : "<b>" + t("allDone") + "</b><span>" + t("keepGoing") + "</span>";
    var sEl = document.getElementById("hud-skills");
    if (sEl) sEl.innerHTML = Object.keys(SKILLS).map(function (k) {
      var l = G.level(k), cur = LEVEL_XP[l - 1] || 0, nxt = LEVEL_XP[l] || cur, pct = l >= 5 ? 100 : Math.round((G.state.xp[k] - cur) / (nxt - cur) * 100);
      return "<div class='sk'><i>" + G.skillName(k) + "</i><em>Lv" + l + "</em><s><u style='width:" + pct + "%'></u></s></div>";
    }).join("");
    var c = G.completion(), bEl = document.getElementById("hud-book");
    if (bEl) bEl.textContent = t("bookCount", { d: c.done, t: c.total });
    var mEl = document.getElementById("hud-menu"); if (mEl) mEl.textContent = t("quests");
  };

  /* ------------------------------------------------------------ boot */
  G.boot = function () {
    canvas = document.getElementById("world"); canvas.width = VW * T; canvas.height = VH * T;
    ctx = canvas.getContext("2d"); ctx.imageSmoothingEnabled = false;
    mini = document.getElementById("minimap"); mini.width = Wd.W * 2; mini.height = Wd.H * 2; mctx = mini.getContext("2d");
    var map = { ArrowDown: 0, s: 0, S: 0, ArrowUp: 1, w: 1, W: 1, ArrowLeft: 2, a: 2, A: 2, ArrowRight: 3, d: 3, D: 3 };
    window.addEventListener("keydown", function (e) {
      if (e.target && /INPUT|TEXTAREA/.test(e.target.tagName)) return;
      if (e.target && e.target.tagName === "BUTTON" && (e.key === " " || e.key === "Enter")) return; // let the focused button click natively
      if (map[e.key] !== undefined) {
        keys[e.key] = true; G.input.dir = map[e.key]; e.preventDefault();
        if (!G.busy() && !G.player.moving) tryMove(map[e.key]); // a quick tap still turns/steps
      }
      if (e.key === " " || e.key === "Enter" || e.key === "z" || e.key === "Z") { if (UI.isOpen()) UI.advance(); else G.interact(); e.preventDefault(); }
      if (e.key === "Escape" || e.key === "x" || e.key === "X") UI.closeTop();
      if ((e.key === "n" || e.key === "N") && !UI.isOpen()) UI.notebook("book");
    });
    window.addEventListener("keyup", function (e) {
      if (map[e.key] !== undefined) { delete keys[e.key]; var rest = Object.keys(keys).filter(function (k) { return map[k] !== undefined; }); G.input.dir = rest.length ? map[rest[rest.length - 1]] : -1; }
    });
    // touch d-pad
    document.querySelectorAll("[data-pad]").forEach(function (b) {
      var d = +b.getAttribute("data-pad");
      function on(e) { e.preventDefault(); G.input.dir = d; }
      function off(e) { e.preventDefault(); if (G.input.dir === d) G.input.dir = -1; }
      b.addEventListener("pointerdown", on); b.addEventListener("pointerup", off); b.addEventListener("pointerleave", off); b.addEventListener("pointercancel", off);
    });
    var abtn = document.getElementById("pad-a");
    if (abtn) abtn.addEventListener("click", function () { if (UI.isOpen()) UI.advance(); else G.interact(); });
    // click/tap a neighbouring tile to interact with it
    canvas.addEventListener("click", function (e) {
      if (UI.isOpen()) return;
      var r = canvas.getBoundingClientRect(), tx = Math.floor(cam.x + (e.clientX - r.left) / r.width * VW), ty = Math.floor(cam.y + (e.clientY - r.top) / r.height * VH);
      var p = G.player, dx = tx - p.x, dy = ty - p.y;
      if (Math.abs(dx) + Math.abs(dy) === 1 || (Math.abs(dy) === 2 && dx === 0 && G.tileAt(p.x, p.y + dy / 2) === "stall")) {
        p.dir = dy > 0 ? 0 : dy < 0 ? 1 : dx < 0 ? 2 : 3; G.interact();
      }
    });
    setInterval(function () { if (G.state.introDone) G.save(); }, 15000);
    requestAnimationFrame(render);
    G.hud();
  };
})();
