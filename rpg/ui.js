/* UI: dialogue runner, NPC menu, lessons & exercises, word book, skills, quests, camp review,
   title / help / about / "What is Inuttitut?" screens, toasts. Bilingual via L10N. */
(function () {
  "use strict";
  var Wd = window.WORLD, LEX = window.LEX, A = window.ART, G = window.G, L = window.L10N;
  var UI = window.UI = {};
  var t = L.t, tx = L.tx, mark = L.mark;
  var $ = function (s) { return document.querySelector(s); };
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), k = a[i]; a[i] = a[j]; a[j] = k; } return a; }
  function item(inu) { return Wd.BY_INU[inu]; }
  function unitOf(id) { for (var i = 0; i < LEX.units.length; i++) if (LEX.units[i].id === id) return LEX.units[i]; return null; }
  function itemsOf(uid) { return LEX.items.filter(function (it) { return it.unit === uid; }); }
  function npcName(id) { var n = Wd.NPCS.filter(function (x) { return x.id === id; })[0]; return n ? n.nameText : ""; }
  function srcLine(it) {
    var s = LEX.src[it.src] || it.src, url = (s.match(/https?:\/\/\S+/) || [""])[0], name = s.split(" — ")[0];
    return "<span class='badge k" + it.kind + "'>" + esc(tx(LEX.kinds[it.kind])) + "</span> " + (url ? "<a href='" + esc(url) + "' target='_blank' rel='noopener'>" + esc(name) + "</a>" : esc(name));
  }
  // meaning of an example in the interface language (Japanese mode can also show English)
  function meanText(it) { return L.lang === "en" || G.state.settings.trans === "en" ? it.en : it.ja; }
  function meaning(it) {
    if (L.lang === "en") return "<span class='en main'>" + esc(it.en) + "</span>";
    var m = G.state.settings.trans;
    return (m !== "en" ? "<span class='ja'>" + esc(it.ja) + "</span>" : "") + (m !== "ja" ? "<span class='en'>" + esc(it.en) + "</span>" : "");
  }
  function playBtn(id) {
    var has = G.hasClip(id, "model");
    return "<button class='px-btn sm play" + (has ? "" : " off") + "' data-play='" + id + "' title='" + esc(has ? t("playModel") : t("noRec")) + "'>♪" + (has ? "" : " " + t("noRecShort")) + "</button>";
  }
  function bindPlay(root) {
    root.querySelectorAll("[data-play]").forEach(function (b) {
      b.onclick = function (e) {
        e.stopPropagation(); b.blur();
        var id = b.getAttribute("data-play");
        if (!G.playClip(id, "model", G.level("listen") >= 2 && G.state.settings.slow ? 0.75 : 1)) UI.toast(t("noAudioToast"));
      };
    });
  }

  /* ------------------------------------------------------------ toast */
  var toastT = 0;
  UI.toast = function (msg) {
    var el = $("#toast"); el.textContent = msg; el.classList.add("on");
    clearTimeout(toastT); toastT = setTimeout(function () { el.classList.remove("on"); }, 3600);
  };

  /* ------------------------------------------------------------ open-state */
  var dlgOpen = false, panelOpen = false, advanceFn = null, lessonLock = false;
  UI.isOpen = function () { return dlgOpen || panelOpen || !$("#title").hidden; };
  UI.advance = function () { if (advanceFn) advanceFn(); };
  UI.closeTop = function () { if (panelOpen && !lessonLock) closePanel(); };

  /* ------------------------------------------------------------ dialogue */
  var D = {};
  function dlgShow(o) {
    $("#dlg").hidden = false; dlgOpen = true;
    var who = o.who ? Wd.NPCS.filter(function (n) { return n.id === o.who; })[0] : null;
    $("#dlg-portrait").innerHTML = who ? "<img alt='' src='" + A.portraits[who.sprite][o.face || "normal"] + "'>" : "";
    $("#dlg-portrait").hidden = !who;
    $("#dlg-name").innerHTML = who ? mark(who.nameText) : "";
    $("#dlg-pic").innerHTML = D.pic ? "<img alt='' src='" + D.pic + "'>" : "";
    var body = "";
    if (o.inu) {
      var it = item(o.inu);
      body += "<div class='inu'>" + esc(o.inu) + "</div><div class='tools'>" + playBtn(it.id) +
        "<button class='px-btn sm' id='dlg-mean'>" + t("meaningBtn") + "</button></div><div class='mean' id='dlg-meantext' hidden>" + meaning(it) + "</div>";
    }
    if (o.narr) body += "<div class='narr'>" + mark(o.narr) + "</div>";
    if (o.hint) body += "<div class='hint'>" + mark(o.hint) + "</div>";
    $("#dlg-body").innerHTML = body;
    var mb = $("#dlg-mean"); if (mb) mb.onclick = function () { var m = $("#dlg-meantext"); m.hidden = !m.hidden; mb.blur(); };
    bindPlay($("#dlg-body"));
    var ch = $("#dlg-choices"); ch.innerHTML = "";
    (o.choices || []).forEach(function (c) {
      var b = document.createElement("button"); b.className = "px-btn choice";
      b.innerHTML = c.inu ? "<b>" + esc(c.label) + "</b>" : (c.html || esc(c.label));
      b.onclick = function () { c.on(b); };
      ch.appendChild(b);
      if (c.inu) { var p = document.createElement("span"); p.innerHTML = playBtn(item(c.label).id); p.className = "choice-play"; ch.appendChild(p); bindPlay(p); }
    });
    $("#dlg-next").hidden = !o.next;
    $("#dlg-next").setAttribute("aria-label", t("next"));
    advanceFn = o.next || null;
  }
  function dlgClose() { $("#dlg").hidden = true; dlgOpen = false; advanceFn = null; D.pic = null; }

  UI.run = function (steps, done, where) {
    var i = 0;
    where = where || t("talkWhere");
    function speaker() { for (var k = i - 2; k >= 0; k--) if (steps[k] && steps[k].who) return steps[k].who; return null; }
    function step() {
      if (i >= steps.length) { dlgClose(); G.save(); G.hud(); if (done) done(); return; }
      var s = steps[i++];
      if (s.pic) { D.pic = A.illus(s.pic); return step(); }
      if (s.obj) { G.objDone(s.obj); return step(); }
      if (s.say) { G.discover(item(s.say).id, where); G.sfx("talk"); return dlgShow({ who: s.who, face: s.face, inu: s.say, next: step }); }
      if (s.narr) return dlgShow({ narr: s.narr, next: step });
      if (s.choose || s.chooseHome) return choose(s, step);
      if (s.quiz) return quiz(s, step);
      step();
    }
    function choose(s, next) {
      var opts = s.choose;
      if (s.chooseHome) {
        var home = G.state.home || "Nain";
        opts = Wd.HOME.map(function (o) { return { t: o.t, ok: o.home && o.home === home ? 1 : 0, hint: o.hint }; });
      }
      opts.forEach(function (o) { G.discover(item(o.t).id, where); });
      var who = speaker();
      function render(hint, face) {
        dlgShow({ who: who, face: face, narr: hint ? null : t("chooseReply"), hint: hint,
          choices: shuffle(opts).map(function (o) {
            return { label: o.t, inu: true, on: function () {
              var id = item(o.t).id;
              if (o.ok) {
                G.sfx("ok"); G.result(id, true, "replied"); G.addXP("speak", 2);
                if (who) G.state.aff[who] = (G.state.aff[who] || 0) + 1;
                if (o.set && o.set.home) G.state.home = o.set.home;
                next();
              } else { G.sfx("ng"); G.result(id, false); render(o.hint || t("thinkAgain"), "puzzled"); }
            } };
          }) });
      }
      render(null, null);
    }
    function quiz(s, next) {
      var order = shuffle(s.opts.map(function (o, k) { return { o: o, k: k }; }));
      function render(hint) {
        dlgShow({ narr: { en: "Q. " + s.quiz.en, ja: "Q. " + s.quiz.ja }, hint: hint, choices: order.map(function (x) {
          return { label: tx(x.o), on: function () {
            if (x.k === s.ans) { G.sfx("ok"); G.addXP(s.skill || "listen", 2); next(); }
            else { G.sfx("ng"); render(t("quizWrong")); }
          } };
        }) });
      }
      render(null);
    }
    step();
  };
  UI.narr = function (lines, done) { UI.run(lines.map(function (l) { return { narr: l }; }), done); };

  /* ------------------------------------------------------------ NPC */
  function pendingConversation(n) {
    var q = G.quest(); if (!q) return null;
    for (var k = 0; k < q.obj.length; k++) {
      var o = q.obj[k];
      if (G.state.flags[o[0]] || o[0].indexOf("lesson:") === 0) continue;
      if (o[2] === n.id) return Wd.SCRIPTS[o[0]] ? o[0] : null;
    }
    return null;
  }
  UI.talk = function (n) {
    var nm = L.plain(n.nameText);
    if (G.level("speak") < n.speak) return UI.narr([t("lockedTalk1", { n: nm }), t("lockedTalk2", { n: nm, l: n.speak })]);
    var key = pendingConversation(n);
    if (key) return UI.run(Wd.SCRIPTS[key], checkEnding, nm);
    npcMenu(n);
  };
  function npcMenu(n) {
    var nm = L.plain(n.nameText);
    var lessons = (Wd.TEACH[n.id] || []).filter(function (x) { return G.qIndex(x[1]) <= G.state.quest; });
    var choices = [{ label: t("talk"), on: function () { UI.run(Wd.SMALL[n.id], null, nm); } }];
    lessons.forEach(function (x) {
      var u = unitOf(x[0]), st = G.state.units[x[0]];
      choices.push({ label: t("learn", { u: tx(u.title) }) + (st.passed ? " ✓" : ""), on: function () {
        dlgClose();
        if (x[0] === "u4" && !G.state.flags.baby_seen) { G.state.flags.baby_seen = true; return UI.run(Wd.SCRIPTS.baby, function () { UI.lesson(x[0], n); }, nm); }
        UI.lesson(x[0], n);
      } });
    });
    choices.push({ label: t("bye"), on: dlgClose });
    dlgShow({ who: n.id, narr: { en: t("whatDo", { n: nm }), ja: t("whatDo", { n: nm }) }, choices: choices });
  }
  function checkEnding() {
    if (G.state.quest >= Wd.QUESTS.length && !G.state.ended) {
      G.state.ended = true; G.save();
      setTimeout(function () { UI.run(Wd.SCRIPTS.ending, function () { UI.notebook("book"); }, npcName("anansiak")); }, 300);
    }
  }

  /* ------------------------------------------------------------ panel */
  function openPanel(html, cls) { var p = $("#panel"); p.className = "panel " + (cls || ""); p.innerHTML = html; p.hidden = false; panelOpen = true; bindPlay(p); return p; }
  function closePanel() { $("#panel").hidden = true; panelOpen = false; lessonLock = false; G.save(); G.hud(); checkEnding(); }
  UI.closePanel = closePanel;

  /* ------------------------------------------------------------ exercises */
  function typable(it) { return it.inu.indexOf(" — ") < 0 && it.inu.indexOf(" / ") < 0 && it.inu.length <= 42; }
  function distract(correct, field, pool, n) {
    var key = function (x) { return field === "mean" ? meanText(x) : x[field]; };
    var seen = {}; seen[key(correct)] = 1;
    var pick = function (src) { return shuffle(src).filter(function (x) { var k = key(x); if (seen[k]) return false; seen[k] = 1; return true; }); };
    var out = pick(pool).slice(0, n);
    if (out.length < n) out = out.concat(pick(LEX.items).slice(0, n - out.length));
    return out;
  }
  function norm(s) {
    s = String(s).trim().replace(/\s+/g, " ").replace(/[.?!,]+$/g, "").replace(/aa/g, "â").replace(/AA/g, "Â");
    if (!s) return s;
    return s[0].toLowerCase() + s.slice(1).replace(/[A-JL-Za-jl-z]/g, function (c) { return c.toLowerCase(); });
  }
  function drillFor(id) { for (var u in Wd.DRILLS) { var d = Wd.DRILLS[u].filter(function (x) { return x.id === id; })[0]; if (d) return { d: d, unit: u }; } return null; }

  function exercise(el, kind, it, done, pool) {
    pool = pool || itemsOf(it.unit);
    var head = "", body = "";
    var skillOf = { meaning: "rw", produce: "speak", type: "rw", drill: "gram", listen: "listen" }[kind];
    var label = { meaning: t("exMeaning"), produce: t("exProduce"), type: t("exType"), drill: t("exDrill"), listen: t("exListen") }[kind];
    var finish = function (ok) {
      G.sfx(ok ? "ok" : "ng");
      G.result(it.id, ok, kind === "type" ? "typed" : kind === "produce" ? "replied" : null);
      if (ok) G.addXP(skillOf, kind === "type" ? 4 : kind === "drill" || kind === "listen" ? 3 : 2);
      var fb = el.querySelector(".fb");
      fb.innerHTML = (ok ? "<b class='ok'>" + t("correct") + "</b>" : "<b class='ng'>" + t("answerIs") + "</b>") + "<div class='inu sm'>" + esc(it.inu) + "</div>" + meaning(it) +
        "<div class='src'>" + srcLine(it) + "</div><button class='px-btn' id='ex-next'>" + t("nextBtn") + "</button>";
      bindPlay(fb);
      el.querySelectorAll(".opt, .typebox button, .typebox input").forEach(function (b) { b.disabled = true; });
      var nb = el.querySelector("#ex-next"); nb.focus(); nb.onclick = function () { done(ok); };
    };
    if (kind === "meaning" || kind === "listen") {
      var opts = shuffle([it].concat(distract(it, kind === "listen" ? "inu" : "mean", pool, 3)));
      head = kind === "listen" ? "<div class='prompt'>" + playBtn(it.id).replace("♪", t("listenBtn")) + "</div>" : "<div class='inu'>" + esc(it.inu) + "</div><div class='tools'>" + playBtn(it.id) + "</div>";
      body = opts.map(function (o) { return "<button class='px-btn opt" + (kind === "listen" ? " inu-opt" : "") + "' data-ok='" + (o.id === it.id ? 1 : 0) + "'>" + esc(kind === "listen" ? o.inu : meanText(o)) + "</button>"; }).join("");
    } else if (kind === "produce") {
      var po = shuffle([it].concat(distract(it, "inu", pool, 3)));
      head = "<div class='prompt'>" + meaning(it) + "</div>";
      body = po.map(function (o) { return "<button class='px-btn opt inu-opt' data-ok='" + (o.id === it.id ? 1 : 0) + "'>" + esc(o.inu) + "</button>"; }).join("");
    } else if (kind === "drill") {
      var df = drillFor(it.id), d = df.d, targets = [];
      Wd.DRILLS[df.unit].forEach(function (x) { if (targets.indexOf(x.target) < 0) targets.push(x.target); });
      var choices = shuffle([d.target].concat(shuffle(targets.filter(function (x) { return x !== d.target; })).slice(0, 3)));
      head = "<div class='prompt'>" + meaning(it) + "</div><div class='inu'>" + esc(d.stem) + "<span class='gap'>＿＿</span>" + esc(d.rest) + "</div>";
      body = choices.map(function (x) { return "<button class='px-btn opt inu-opt' data-ok='" + (x === d.target ? 1 : 0) + "'>-" + esc(x) + "-</button>"; }).join("");
    } else if (kind === "type") {
      head = "<div class='prompt'>" + meaning(it) + "</div><div class='hintline'>" + t("hint") + ": " + esc(it.inu.split(/\s+/).map(function (w) { return w.slice(0, 2) + "…"; }).join(" ")) + "</div>";
      body = "<div class='typebox'><input id='ex-in' autocomplete='off' spellcheck='false' aria-label='" + esc(t("typeLabel")) + "'><div class='keys'>" +
        ["â", "K", "e", "o", "ng"].map(function (k) { return "<button class='px-btn sm' data-k='" + k + "'>" + k + "</button>"; }).join("") +
        "</div><button class='px-btn' id='ex-check'>" + t("check") + "</button><p class='tiny'>" + t("typeHelp") + "</p></div>";
    }
    el.innerHTML = "<div class='ex-kind'>" + label + "</div>" + head + "<div class='opts'>" + body + "</div><div class='fb'></div>";
    bindPlay(el);
    el.querySelectorAll(".opt").forEach(function (b) {
      b.onclick = function () { var ok = b.getAttribute("data-ok") === "1"; b.classList.add(ok ? "right" : "wrong"); if (!ok) el.querySelector(".opt[data-ok='1']").classList.add("right"); finish(ok); };
    });
    if (kind === "type") {
      var inp = el.querySelector("#ex-in"); setTimeout(function () { inp.focus(); }, 30);
      el.querySelectorAll("[data-k]").forEach(function (b) { b.onclick = function () { var k = b.getAttribute("data-k"), s = inp.selectionStart || inp.value.length; inp.value = inp.value.slice(0, s) + k + inp.value.slice(s); inp.focus(); }; });
      var chk = function () { finish(norm(inp.value) === norm(it.inu)); };
      el.querySelector("#ex-check").onclick = chk;
      inp.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.stopPropagation(); chk(); } });
    }
    if (kind === "listen" && G.hasClip(it.id, "model")) setTimeout(function () { G.playClip(it.id, "model"); }, 250);
  }
  function pickKind(it, want) {
    var avail = { meaning: 1, produce: 1, type: typable(it), drill: !!drillFor(it.id), listen: G.hasClip(it.id, "model") };
    return avail[want] ? want : (Math.random() < 0.5 ? "produce" : "meaning");
  }

  /* ------------------------------------------------------------ lessons */
  UI.lesson = function (uid, teacher) {
    var u = unitOf(uid), its = itemsOf(uid), title = tx(u.title);
    lessonLock = true;
    var por = teacher ? "<img class='por' alt='' src='" + A.portraits[teacher.sprite].happy + "'>" : "";
    var box = openPanel("<div class='lesson'></div>", "wide").querySelector(".lesson");
    var where = t("lessonWhere", { u: title });
    function intro() {
      box.innerHTML = "<div class='lhead'>" + por + "<div><div class='cefr'>" + u.cefr + "</div><h2>" + esc(title) + "</h2><p>" + esc(tx(u.cando)) + "</p></div></div>" +
        "<h3>" + t("grammarPoints") + "</h3><ul class='gram'>" + u.grammar.map(function (g) { return "<li><b>" + esc(tx(g.h)) + "</b> " + esc(tx(g.b)) + "</li>"; }).join("") + "</ul>" +
        "<div class='row'><button class='px-btn' id='l-cards'>" + t("studyCards", { n: its.length }) + "</button><button class='px-btn' id='l-prac'>" + t("practice") + "</button><button class='px-btn ghost' id='l-close'>" + t("quit") + "</button></div>";
      box.querySelector("#l-cards").onclick = function () { card(0); };
      box.querySelector("#l-prac").onclick = practice;
      box.querySelector("#l-close").onclick = closePanel;
    }
    function card(i) {
      var it = its[i]; G.discover(it.id, where);
      box.innerHTML = "<div class='cardhead'>" + esc(title) + " — " + (i + 1) + " / " + its.length + "</div>" +
        "<div class='card'><div class='inu'>" + esc(it.inu) + "</div><div class='tools'>" + playBtn(it.id) + "</div>" + meaning(it) +
        (it.note ? "<p class='note'>" + esc(tx(it.note)) + "</p>" : "") + "<div class='src'>" + srcLine(it) + "</div></div>" +
        "<div class='row'><button class='px-btn' id='c-prev'" + (i ? "" : " disabled") + ">" + t("prev") + "</button><button class='px-btn' id='c-next'>" + (i < its.length - 1 ? t("nextCard") : t("toPractice")) + "</button><button class='px-btn ghost' id='c-prac'>" + t("practice") + "</button></div>";
      bindPlay(box);
      box.querySelector("#c-prev").onclick = function () { card(i - 1); };
      box.querySelector("#c-next").onclick = function () { i < its.length - 1 ? card(i + 1) : practice(); };
      box.querySelector("#c-prac").onclick = practice;
    }
    function practice() {
      var picks = shuffle(its).slice(0, Math.min(8, its.length));
      var drills = (Wd.DRILLS[uid] || []).map(function (d) { return Wd.BY_ID[d.id]; });
      var prefs = ["meaning", "produce", "drill", "meaning", "produce", "drill", "type", "listen"];
      var qs = picks.map(function (it, k) {
        var want = prefs[k % prefs.length];
        if (want === "drill" && drills.length) it = drills[(Math.random() * drills.length) | 0];
        return { it: it, kind: pickKind(it, want) };
      });
      var n = 0, score = 0;
      function next() {
        if (n >= qs.length) return result();
        var q = qs[n++];
        box.innerHTML = "<div class='cardhead'>" + esc(title) + " — " + t("practiceN", { i: n, n: qs.length }) + "</div><div class='ex'></div>";
        G.discover(q.it.id, where);
        exercise(box.querySelector(".ex"), q.kind, q.it, function (ok) { if (ok) score++; next(); }, its);
      }
      function result() {
        var pct = Math.round(score / qs.length * 100), pass = pct >= 70, st = G.state.units[uid];
        st.best = Math.max(st.best, pct);
        if (pass && !st.passed) { st.passed = true; G.addXP("gram", 5); }
        if (pass) G.objDone("lesson:" + uid);
        box.innerHTML = "<div class='result'><h2>" + (pass ? t("passed") : t("almost")) + "</h2><p class='big'>" + score + " / " + qs.length + " (" + pct + "%)</p>" +
          "<p>" + (pass ? t("passedMsg") : t("failMsg")) + "</p><div class='row'><button class='px-btn' id='r-again'>" + t("again") + "</button><button class='px-btn' id='r-cards'>" + t("seeCards") + "</button><button class='px-btn ghost' id='r-close'>" + t("close") + "</button></div></div>";
        box.querySelector("#r-again").onclick = practice;
        box.querySelector("#r-cards").onclick = function () { card(0); };
        box.querySelector("#r-close").onclick = closePanel;
        G.save();
      }
      next();
    }
    intro();
  };

  /* ------------------------------------------------------------ camp review */
  UI.camp = function () {
    var now = Date.now();
    var disc = LEX.items.filter(function (it) { return (G.state.items[it.id] || {}).st >= 1; });
    var due = disc.filter(function (it) { return G.state.items[it.id].due <= now; });
    var weak = disc.filter(function (it) { return G.state.items[it.id].ng > G.state.items[it.id].ok; });
    var box = openPanel("<div class='camp'></div>", "wide").querySelector(".camp");
    box.innerHTML = "<h2>" + t("campTitle") + "</h2><p>" + t("campIntro") + "</p>" +
      "<ul class='stats'><li>" + t("campMet") + " <b>" + disc.length + "</b></li><li>" + t("campDue") + " <b>" + due.length + "</b></li><li>" + t("campWeak") + " <b>" + weak.length + "</b></li></ul>" +
      (disc.length ? "<div class='row'><button class='px-btn' id='cp-go'>" + t("campStart") + "</button><button class='px-btn ghost' id='cp-close'>" + t("close") + "</button></div>"
                   : "<p class='hint'>" + t("campNone") + "</p><div class='row'><button class='px-btn ghost' id='cp-close'>" + t("close") + "</button></div>");
    box.querySelector("#cp-close").onclick = closePanel;
    var go = box.querySelector("#cp-go"); if (go) go.onclick = function () { session(disc); };
    function session(list) {
      lessonLock = true;
      var t0 = Date.now(), LIMIT = 5 * 60000;
      var sorted = list.slice().sort(function (a, b) {
        var ra = G.state.items[a.id], rb = G.state.items[b.id];
        return (ra.due <= now ? 0 : 1) - (rb.due <= now ? 0 : 1) || ra.box - rb.box || (rb.ng - rb.ok) - (ra.ng - ra.ok) || Math.random() - 0.5;
      }).slice(0, 8);
      var n = 0, score = 0;
      function next() {
        if (n >= sorted.length || Date.now() - t0 > LIMIT) return end();
        var it = sorted[n++], r = G.state.items[it.id], prefs = [];
        if (G.hasClip(it.id, "model")) prefs.push("listen");
        if (drillFor(it.id)) prefs.push("drill");
        if (typable(it) && (G.level("rw") >= 3 || r.st === 2)) prefs.push("type");
        prefs.push(n % 2 ? "meaning" : "produce");
        var kind = pickKind(it, prefs[(Math.random() * prefs.length) | 0]);
        var mins = Math.max(0, Math.round((LIMIT - (Date.now() - t0)) / 60000));
        box.innerHTML = "<div class='cardhead'>" + t("campHead", { i: n, n: sorted.length, m: mins }) + "</div><div class='ex'></div>";
        exercise(box.querySelector(".ex"), kind, it, function (ok) { if (ok) score++; next(); });
      }
      function end() {
        lessonLock = false;
        var sec = Math.round((Date.now() - t0) / 1000);
        box.innerHTML = "<h2>" + t("campDone") + "</h2><p class='big'>" + score + " / " + n + "</p><p>" + t("campSummary", { m: Math.floor(sec / 60), s: sec % 60 }) + "</p>" +
          "<div class='row'><button class='px-btn' id='cp-again'>" + t("oneMore") + "</button><button class='px-btn ghost' id='cp-close2'>" + t("close") + "</button></div>";
        box.querySelector("#cp-again").onclick = function () { session(disc); };
        box.querySelector("#cp-close2").onclick = closePanel;
        G.save();
      }
      next();
    }
  };

  /* ------------------------------------------------------------ notebook */
  var TREE = {
    speak: [["Talk with Grandma, Hulda and Tâmi", "村の人(おばあちゃん・Hulda・Tâmi)と話せる"], ["Talk with Rita at the shore", "海辺の Rita と話せる"], ["Talk with Makusi at the airstrip", "飛行場の Makusi と話せる"], ["Confident in longer exchanges", "長いやりとりにも自信がつく"], ["Speaking master", "会話マスター"]],
    listen: [["Play speaker recordings with ♪", "♪ でお手本を聞ける(録音がある表現)"], ["Slow playback (settings)", "ゆっくり再生が使える(設定)"], ["More listening questions at the camp", "キャンプで聞き取り問題が増える"], ["Understand conversations quickly", "会話の内容をすぐ理解できる"], ["Listening master", "聞き取りマスター"]],
    rw: [["Read the meaning", "意味を読み取れる"], ["Spelling & sound hints in the word book", "図鑑に「綴りと発音のヒント」が表示される"], ["Writing (typing) questions at the camp", "キャンプで書き取り(入力)問題が出る"], ["Write longer sentences", "長い文も書ける"], ["Reading & writing master", "読み書きマスター"]],
    gram: [["Notice word endings", "語尾の形に気づける"], ["Read the course grammar tables in the notebook", "ノートで「文法表(授業資料)」が読める"], ["More grammar drills at the camp", "キャンプで文法ドリルが増える"], ["Combine endings", "語尾を組み合わせられる"], ["Grammar master", "文法マスター"]]
  };
  function spellHint(inu) {
    var en = L.lang === "en", h = [];
    if (/[âÂ]/.test(inu)) h.push(en ? "â = long a (aa)" : "â = 長い a(aa)");
    if (/e/.test(inu)) h.push(en ? "e = long i (ii)" : "e = 長い i(ii)");
    if (/o/.test(inu)) h.push(en ? "o = long u (uu)" : "o = 長い u(uu)");
    if (/K/.test(inu)) h.push(en ? "K = a k made further back in the throat (uvular), different from k" : "K = のどの奥で出す k(口蓋垂音)。小文字の k とは別の音");
    if (/ng/.test(inu)) h.push(en ? "ng = nasal sound" : "ng = 鼻にかかる音");
    if (/([bcdfghjklmnpqrstvwxyzK])\1/i.test(inu)) h.push(en ? "double consonants are held a little longer" : "同じ子音が2つ続く所は、少しためて長く");
    return h.length ? h.join(" / ") : (en ? "no special spelling" : "特別な綴りはありません");
  }
  UI.notebook = function (tab) {
    tab = tab || "book";
    var tabs = [["book", t("tabBook")], ["skills", t("tabSkills")], ["quests", t("tabQuests")], ["grammar", t("tabGrammar")], ["about", t("tabAbout")]];
    var p = openPanel("<div class='nb'><div class='tabs'>" + tabs.map(function (x) { return "<button class='px-btn tab" + (x[0] === tab ? " on" : "") + "' data-tab='" + x[0] + "'>" + x[1] + "</button>"; }).join("") +
      "<button class='px-btn ghost close' aria-label='" + t("close") + "'>✕</button></div><div class='nb-body'></div></div>", "wide");
    p.querySelectorAll("[data-tab]").forEach(function (b) { b.onclick = function () { UI.notebook(b.getAttribute("data-tab")); }; });
    p.querySelector(".close").onclick = closePanel;
    var body = p.querySelector(".nb-body");
    ({ book: book, skills: skills, quests: quests, grammar: grammar, about: settingsTab })[tab](body);
    bindPlay(body);
  };
  var bookFilter = "all";
  function book(el) {
    var c = G.completion(), now = Date.now();
    var html = "<div class='bookhead'>" + t("bookHead", { d: c.done, t: c.total, p: Math.round(c.done / c.total * 100) }) +
      "<div class='filters'>" + [["all", t("fAll")], ["review", t("fReview")], ["todo", t("fTodo")]].map(function (f) { return "<button class='px-btn sm" + (bookFilter === f[0] ? " on" : "") + "' data-f='" + f[0] + "'>" + f[1] + "</button>"; }).join("") + "</div></div>";
    LEX.units.forEach(function (u) {
      var its = itemsOf(u.id).filter(function (it) {
        var r = G.state.items[it.id] || { st: 0 };
        if (bookFilter === "review") return r.st >= 1 && (r.due <= now || r.ng > r.ok);
        if (bookFilter === "todo") return r.st < 3;
        return true;
      });
      if (!its.length) return;
      html += "<h3>" + esc(tx(u.title)) + " <small>" + u.cefr + "</small></h3><div class='entries'>";
      its.forEach(function (it) {
        var r = G.state.items[it.id] || { st: 0 };
        if (!r.st) { html += "<div class='entry locked'><span class='st s0'>?</span><span class='inu'>" + t("unknown") + "</span><span class='mean'>" + t("notMet") + "</span></div>"; return; }
        html += "<div class='entry'><span class='st s" + r.st + "'>" + (L.lang === "en" ? ["?", "F", "U", "✓"] : ["?", "見", "分", "使"])[r.st] + "</span><div class='eb'><div class='inu'>" + esc(it.inu) + "</div>" + meaning(it) +
          "<div class='src'>" + srcLine(it) + (r.where ? " · " + esc(t("metAt", { w: r.where })) : "") + "</div>" +
          (G.level("rw") >= 2 ? "<div class='spell'>" + esc(t("spelling", { h: spellHint(it.inu) })) + "</div>" : "") +
          (it.note ? "<div class='note'>" + esc(tx(it.note)) + "</div>" : "") +
          "<div class='tools'>" + playBtn(it.id) + "<button class='px-btn sm' data-rec='" + it.id + "|model'>" + t("recModel") + "</button>" +
          "<button class='px-btn sm' data-rec='" + it.id + "|self'>" + t("recSelf") + "</button>" +
          (G.hasClip(it.id, "self") ? "<button class='px-btn sm' data-self='" + it.id + "'>" + t("playSelf") + "</button>" : "") +
          "<span class='state'>" + esc(t("okNg", { st: G.stateLabel(r.st), o: r.ok, n: r.ng })) + "</span></div></div></div>";
      });
      html += "</div>";
    });
    el.innerHTML = html;
    el.querySelectorAll("[data-f]").forEach(function (b) { b.onclick = function () { bookFilter = b.getAttribute("data-f"); UI.notebook("book"); }; });
    el.querySelectorAll("[data-self]").forEach(function (b) { b.onclick = function () { G.playClip(b.getAttribute("data-self"), "self"); }; });
    el.querySelectorAll("[data-rec]").forEach(function (b) {
      b.onclick = function () {
        var pr = b.getAttribute("data-rec").split("|");
        if (b._ctl) { b._ctl.stop(); return; }
        if (pr[1] === "model" && !confirm(t("recConfirm"))) return;
        b._ctl = G.recordClip(pr[0], pr[1], function (st) {
          if (st === "recording") b.textContent = t("stop");
          else if (st === "saved") { b._ctl = null; if (pr[1] === "self") G.addXP("speak", 1); UI.toast(t("recSaved")); UI.notebook("book"); }
          else { b._ctl = null; UI.toast(st === "denied" ? t("recDenied") : st === "unsupported" ? t("recUnsupported") : t("recError")); }
        });
      };
    });
  }
  function skills(el) {
    var li = L.lang === "en" ? 0 : 1;
    el.innerHTML = "<p>" + t("skillsIntro") + "</p><div class='tree'>" + Object.keys(G.SKILLS).map(function (k) {
      var l = G.level(k);
      return "<div class='branch'><h3>" + G.skillName(k) + " <small>Lv" + l + " · " + G.state.xp[k] + " XP</small></h3>" +
        TREE[k].map(function (n, i) { return "<div class='node" + (i < l ? " on" : "") + "'><b>Lv" + (i + 1) + "</b> " + esc(n[li]) + (i >= l ? " <small>(" + G.LEVEL_XP[i] + " XP)</small>" : "") + "</div>"; }).join("") + "</div>";
    }).join("") + "</div>";
  }
  function quests(el) {
    el.innerHTML = Wd.QUESTS.map(function (q, i) {
      var st = i < G.state.quest ? "done" : i === G.state.quest ? "now" : "later";
      return "<div class='quest " + st + "'><h3>" + (st === "done" ? "✓ " : st === "now" ? "▶ " : "· ") + mark(q.title) + "</h3>" +
        (st === "later" ? "<p class='tiny'>" + t("notStarted") + "</p>" : "<p>" + mark(q.desc) + "</p><ul>" + q.obj.map(function (o) { return "<li class='" + (G.state.flags[o[0]] ? "ok" : "") + "'>" + (G.state.flags[o[0]] ? "✓ " : "□ ") + mark(o[1]) + "</li>"; }).join("") + "</ul>") + "</div>";
    }).join("");
  }
  function grammar(el) {
    if (G.level("gram") < 2) { el.innerHTML = "<p class='hint'>" + t("grammarLocked") + "</p>"; return; }
    el.innerHTML = LEX.units.filter(function (u) { return G.unitAvailable(u.id); }).map(function (u) {
      return "<h3>" + esc(tx(u.title)) + " <small>" + u.cefr + "</small></h3><ul class='gram'>" + u.grammar.map(function (g) { return "<li><b>" + esc(tx(g.h)) + "</b> " + esc(tx(g.b)) + "</li>"; }).join("") + "</ul>";
    }).join("") + "<p class='tiny'>" + t("grammarLater") + "</p>";
  }
  function settingsTab(el) {
    var s = G.state.settings;
    el.innerHTML = "<h3>" + t("settings") + "</h3><div class='row wrap'>" +
      "<button class='px-btn sm' id='st-lang'>" + t("langBtn") + "</button>" +
      "<button class='px-btn sm' id='st-sound'>" + t("sound", { v: s.sound ? t("on") : t("off") }) + "</button>" +
      (L.lang === "ja" ? "<button class='px-btn sm' id='st-trans'>" + t("trans", { v: { both: t("transBoth"), ja: t("transJa"), en: t("transEn") }[s.trans] }) + "</button>" : "") +
      "<button class='px-btn sm' id='st-slow'" + (G.level("listen") >= 2 ? "" : " disabled") + ">" + t("slow", { v: s.slow ? t("on") : t("off") }) + (G.level("listen") >= 2 ? "" : t("slowLock")) + "</button>" +
      "<button class='px-btn sm ghost' id='st-reset'>" + t("reset") + "</button></div>" + aboutGameHtml();
    el.querySelector("#st-lang").onclick = function () { L.set(L.lang === "en" ? "ja" : "en"); G.hud(); UI.notebook("about"); };
    el.querySelector("#st-sound").onclick = function () { s.sound = !s.sound; UI.notebook("about"); };
    var tr = el.querySelector("#st-trans"); if (tr) tr.onclick = function () { s.trans = s.trans === "both" ? "ja" : s.trans === "ja" ? "en" : "both"; UI.notebook("about"); };
    el.querySelector("#st-slow").onclick = function () { s.slow = !s.slow; UI.notebook("about"); };
    el.querySelector("#st-reset").onclick = function () { if (confirm(t("resetConfirm"))) { G.reset(); location.reload(); } };
  }
  function aboutGameHtml() {
    var n = { P: 0, T: 0, R: 0, W: 0 }; LEX.items.forEach(function (it) { n[it.kind]++; });
    return t("aboutGameHtml", { n: LEX.items.length, p: n.P, tt: n.T, r: n.R, w: n.W }) +
      "<h3>" + t("sourcesH") + "</h3><ul class='srcs'>" + Object.keys(LEX.src).map(function (k) { var s = LEX.src[k], url = (s.match(/https?:\/\/\S+/) || [""])[0]; return "<li><b>" + k + "</b> " + (url ? esc(s.split(" — ")[0]) + " — <a href='" + esc(url) + "' target='_blank' rel='noopener'>" + esc(url) + "</a>" : esc(s)) + "</li>"; }).join("") + "</ul>" +
      t("audioHtml") + t("cultureHtml");
  }

  /* ------------------------------------------------------------ "What is Inuttitut?" */
  function glossLine(part) { var g = Wd.GLOSSARY[part]; return "<span class='part'><b>" + esc(part) + "</b> " + esc(g ? tx(g.mean) : "") + "</span>"; }
  function exampleRow(inu) { var it = item(inu); return "<div class='exrow'><span class='inu sm'>" + esc(inu) + "</span>" + playBtn(it.id) + "<span class='exmean'>" + esc(meanText(it)) + "</span></div>"; }
  UI.aboutLang = function () {
    var html = "<div class='nb'><div class='tabs'><b>" + t("aboutLang") + "</b><button class='px-btn ghost close' aria-label='" + t("close") + "'>✕</button></div><div class='nb-body about-lang'>" +
      "<p class='tiny'>" + t("aboutLangNote") + "</p>";
    Wd.ABOUT.forEach(function (sec) {
      html += "<h3>" + esc(tx(sec.h)) + "</h3>" + sec.p.map(function (x) { return "<p>" + mark(x) + "</p>"; }).join("");
      (sec.breakdowns || []).forEach(function (b) {
        var it = item(b.word);
        html += "<div class='breakdown'><div><span class='inu'>" + esc(b.word) + "</span> " + playBtn(it.id) + "</div><div class='parts'>" + b.parts.map(glossLine).join("<span class='plus'>+</span>") +
          "</div><div class='exmean'>= " + esc(meanText(it)) + "</div></div>";
      });
      (sec.examples || []).forEach(function (ex) { html += "<p>" + mark(ex[0]) + "</p>" + ex[1].map(exampleRow).join(""); });
      (sec.p2 || []).forEach(function (x) { html += "<p>" + mark(x) + "</p>"; });
    });
    html += "<h3>" + t("aboutLangSources") + "</h3><ul class='srcs'>" + Wd.ABOUT_SRC.map(function (s) {
      return "<li><b>[" + s.id + "]</b> " + esc(s.text) + (s.url ? " — <a href='" + esc(s.url) + "' target='_blank' rel='noopener'>" + esc(s.url) + "</a>" : "") + "</li>";
    }).join("") + "</ul></div></div>";
    var p = openPanel(html, "wide"); p.querySelector(".close").onclick = closePanel;
  };

  /* ------------------------------------------------------------ title / help */
  UI.title = function () {
    var el = $("#title"); el.hidden = false;
    var cont = G.hasSave();
    el.innerHTML = "<div class='tbox'><div class='tlang'><button class='px-btn sm' id='t-lang'>" + t("langBtn") + "</button></div>" +
      "<div class='tsub'>" + t("tagline") + "</div><h1>" + t("gameTitle") + "</h1><div class='tinu'>Ilitannamek!</div>" +
      "<div class='tmenu'>" + (cont ? "<button class='px-btn' id='t-cont'>" + t("cont") + "</button>" : "") + "<button class='px-btn' id='t-new'>" + t("newGame") + "</button>" +
      "<button class='px-btn accent' id='t-lang-about'>" + t("aboutLang") + "</button>" +
      "<button class='px-btn ghost' id='t-help'>" + t("howTo") + "</button><button class='px-btn ghost' id='t-about'>" + t("aboutGame") + "</button></div>" +
      "<p class='tiny'>" + t("titleNote") + "</p></div>";
    $("#t-lang").onclick = function () { L.set(L.lang === "en" ? "ja" : "en"); G.hud(); UI.title(); };
    $("#t-new").onclick = function () {
      if (cont && !confirm(t("confirmNew"))) return;
      G.reset(); el.hidden = true; G.state.introDone = true; G.save(); G.hud();
      UI.run(Wd.SCRIPTS.intro);
    };
    if (cont) $("#t-cont").onclick = function () { G.load(); el.hidden = true; G.hud(); UI.toast(t("welcomeBack")); };
    $("#t-lang-about").onclick = UI.aboutLang;
    $("#t-help").onclick = function () { var p = openPanel("<div class='nb'><div class='tabs'><b>" + t("howTo") + "</b><button class='px-btn ghost close'>✕</button></div><div class='nb-body'>" + t("helpHtml") + "</div></div>", "wide"); p.querySelector(".close").onclick = closePanel; };
    $("#t-about").onclick = function () { var p = openPanel("<div class='nb'><div class='tabs'><b>" + t("aboutGame") + "</b><button class='px-btn ghost close'>✕</button></div><div class='nb-body'>" + aboutGameHtml() + "</div></div>", "wide"); p.querySelector(".close").onclick = closePanel; };
  };

  UI.bind = function () {
    $("#hud-book").onclick = function () { if (!UI.isOpen()) UI.notebook("book"); };
    $("#hud-menu").onclick = function () { if (!UI.isOpen()) UI.notebook("quests"); };
    $("#dlg-next").onclick = function () { UI.advance(); };
  };
})();
