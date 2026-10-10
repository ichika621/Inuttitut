/* World: the map and NPC placement. All text (quests, dialogue, drills, signs, names) comes
   from window.STORY (scripts/rpg_content.py) and all Inuttitut from window.LEX (scripts/a2_bank.py);
   both are generated and checked at build time. This file re-checks the links at load. */
(function () {
  "use strict";
  var LEX = window.LEX, S = window.STORY;
  var BY_INU = {}, BY_ID = {};
  LEX.items.forEach(function (it) { BY_INU[it.inu] = it; BY_ID[it.id] = it; });
  var missing = [];
  function need(inu) { if (!BY_INU[inu]) missing.push(inu); }

  /* ---------------------------------------------------------------- map */
  var W = 60, H = 40;
  var grid = [], gates = {};
  for (var y = 0; y < H; y++) { grid.push([]); for (var x = 0; x < W; x++) grid[y].push(((x * 7 + y * 13) % 11 === 0) ? "snow2" : "snow"); }
  function set(x, y, t) { if (x >= 0 && y >= 0 && x < W && y < H) grid[y][x] = t; }
  function rect(x0, y0, x1, y1, t) { for (var y = y0; y <= y1; y++) for (var x = x0; x <= x1; x++) set(x, y, t); }
  function house(x, y, doorDx) {
    rect(x, y, x + 4, y + 1, "roof"); set(x + 3, y, "chimney");
    ["wall", "window", "wall", "window", "wall"].forEach(function (t, i) { set(x + i, y + 2, t); });
    for (var i = 0; i < 5; i++) set(x + i, y + 3, i === doorDx ? "door" : "wall");
  }
  rect(0, 0, W - 1, 1, "mtn");
  rect(6, 5, 44, 7, "strip"); for (var sx = 8; sx <= 42; sx += 4) set(sx, 6, "stripMark");
  set(30, 4, "plane"); set(31, 4, "plane");
  for (var rx = 0; rx < W; rx++) set(rx, 12, rx % 3 === 0 ? "rock" : "tree");
  [14, 15, 16].forEach(function (gx) { set(gx, 12, "drift"); gates[gx + "," + 12] = "north"; });
  for (var wy = 13; wy < H; wy++) set(36, wy, wy % 4 === 0 ? "rock" : "tree");
  [23, 24, 25].forEach(function (gy) { set(36, gy, "drift"); gates[36 + "," + gy] = "east"; });
  rect(48, 13, W - 1, H - 1, "sea"); for (var iy = 13; iy < H; iy++) set(47, iy, "ice");
  rect(46, 27, 55, 28, "dock"); set(47, 27, "dock"); set(47, 28, "dock");
  set(51, 24, "boat"); set(53, 31, "boat");
  for (var by = 13; by < H; by++) set(0, by, "tree");
  for (var bx = 0; bx < 36; bx++) set(bx, H - 1, "tree");
  rect(5, 19, 5, 21, "path"); rect(5, 21, 33, 21, "path"); rect(33, 21, 33, 24, "path"); rect(33, 24, 46, 24, "path");
  rect(45, 24, 45, 27, "path"); rect(15, 13, 15, 21, "path"); rect(15, 2, 15, 11, "path"); rect(26, 21, 26, 31, "path");
  house(3, 15, 2); house(17, 13, 2); house(27, 14, 2); house(4, 28, 2); house(12, 30, 2); house(29, 33, 1);
  set(9, 18, "doghouse");
  set(22, 20, "stall"); set(23, 20, "stall"); set(24, 20, "stall");
  set(21, 22, "sign"); set(34, 22, "sign"); set(14, 13, "sign"); set(38, 23, "sign"); set(25, 32, "sign");
  set(27, 30, "tent"); set(28, 30, "tent"); set(27, 32, "fire");
  [[2, 24], [3, 33], [10, 25], [19, 27], [21, 35], [31, 26], [35, 37], [8, 36], [16, 37], [24, 37], [34, 30], [2, 14], [11, 14], [33, 14],
   [40, 15], [42, 33], [39, 37], [44, 19], [3, 5], [48, 4], [52, 8], [10, 9], [38, 10]].forEach(function (p) { set(p[0], p[1], "tree"); });
  [[12, 23], [30, 23], [18, 33], [41, 29], [24, 9], [55, 5]].forEach(function (p) { set(p[0], p[1], "rock"); });

  var SOLID = { sea: 1, ice: 1, roof: 1, chimney: 1, wall: 1, window: 1, door: 1, tree: 1, rock: 1, fence: 1, drift: 1, sign: 1, stall: 1, fire: 1, tent: 1, mtn: 1, boat: 1, plane: 1, doghouse: 1 };

  /* ---------------------------------------------------------------- NPCs */
  var NPCS = [
    { id: "anansiak", sprite: "anansiak", x: 6, y: 19, dir: 0, speak: 1 },
    { id: "hulda", sprite: "hulda", x: 18, y: 18, dir: 0, speak: 1 },
    { id: "tami", sprite: "tami", x: 23, y: 19, dir: 0, speak: 1 },
    { id: "rita", sprite: "rita", x: 44, y: 27, dir: 3, speak: 2 },
    { id: "makusi", sprite: "makusi", x: 20, y: 8, dir: 0, speak: 3 }
  ];
  NPCS.forEach(function (n) { n.nameText = S.npcNames[n.id]; });
  var DOGS = [{ x: 9, y: 19 }, { x: 10, y: 19 }];

  /* ---------------------------------------------------------------- re-check links */
  function walk(steps) { steps.forEach(function (s) { if (s.say) need(s.say); (s.choose || []).forEach(function (c) { need(c.t); }); }); }
  Object.keys(S.scripts).forEach(function (k) { walk(S.scripts[k]); });
  Object.keys(S.smalltalk).forEach(function (k) { walk(S.smalltalk[k]); });
  S.homeOptions.forEach(function (o) { need(o.t); });
  var DRILLS = {};
  Object.keys(S.drills).forEach(function (u) {
    DRILLS[u] = S.drills[u].map(function (d) {
      var p = d.split("|"), full = p.join(""); need(full);
      return { stem: p[0], target: p[1], rest: p[2], full: full, id: BY_INU[full] ? BY_INU[full].id : null };
    });
  });
  if (missing.length) throw new Error("Inuttitut text not in the example bank: " + missing.join(" / "));

  window.WORLD = { W: W, H: H, grid: grid, gates: gates, SOLID: SOLID, SIGNS: S.signs, DOORS: S.doors, NPCS: NPCS, DOGS: DOGS,
                   QUESTS: S.quests, TEACH: S.teach, SCRIPTS: S.scripts, SMALL: S.smalltalk, HOME: S.homeOptions, DRILLS: DRILLS,
                   GLOSSARY: S.glossary, ABOUT: S.about, ABOUT_SRC: S.aboutSources, BY_INU: BY_INU, BY_ID: BY_ID };
})();
