/* Pixel art for the snow village — every tile, sprite and portrait is drawn in code
   (original art, no external images). TILE = 16px; the game scales the canvas up
   with image-rendering: pixelated. */
(function () {
  "use strict";
  var T = 16;
  var C = {
    snow: "#eef3f8", snow2: "#e1e9f2", snowS: "#c9d6e4", spark: "#ffffff",
    path: "#d8cfc2", path2: "#c6baa9", pathS: "#b2a593",
    sea: "#2c5675", sea2: "#3b6c90", seaL: "#7fb0d0", ice: "#a9cde4", iceS: "#86b1cf",
    wood: "#7a4e2d", woodD: "#5a3720", woodL: "#946240",
    roof: "#3a4a66", roofD: "#2b3850", roofSnow: "#f6f9fc",
    win: "#f2b547", winL: "#ffd982", door: "#4a2e1c",
    tree: "#2f5b4a", treeD: "#21443a", treeSnow: "#e8f0f6", trunk: "#5b3a24",
    rock: "#7c8794", rockD: "#5d6775", rockL: "#a3acb8",
    fire: "#f28c28", fireL: "#ffd15c", fireD: "#c4521a", ember: "#7a3b1a",
    tent: "#c9a46a", tentD: "#9c7a45",
    strip: "#c3ccd6", stripL: "#f0d36b",
    mtn: "#8ea3bb", mtnD: "#6f849e",
    navy: "#1e2a44", plane: "#d9534f", planeL: "#f4f4f4", planeD: "#9e2f2c",
    stall: "#a4683c", awning: "#d06a3a", awning2: "#f3e6cf"
  };

  function cv(w, h) { var c = document.createElement("canvas"); c.width = w; c.height = h; var x = c.getContext("2d"); x.imageSmoothingEnabled = false; return [c, x]; }
  function px(x, c, X, Y, w, h) { x.fillStyle = c; x.fillRect(X, Y, w || 1, h || 1); }
  function rng(seed) { var s = seed % 2147483647; if (s <= 0) s += 2147483646; return function () { s = s * 16807 % 2147483647; return (s - 1) / 2147483646; }; }

  function snowBase(x, seed) {
    px(x, C.snow, 0, 0, T, T);
    var r = rng(seed);
    for (var i = 0; i < 6; i++) px(x, C.snow2, (r() * T) | 0, (r() * T) | 0, 2, 1);
    for (var j = 0; j < 2; j++) px(x, C.spark, (r() * T) | 0, (r() * T) | 0);
  }

  var tiles = {};
  function make(name, fn, frames) {
    frames = frames || 1;
    tiles[name] = [];
    for (var f = 0; f < frames; f++) { var a = cv(T, T); fn(a[1], f); tiles[name].push(a[0]); }
  }

  make("snow", function (x) { snowBase(x, 7); });
  make("snow2", function (x) { snowBase(x, 91); px(x, C.snowS, 3, 11, 4, 1); px(x, C.snowS, 10, 4, 3, 1); });
  make("path", function (x) {
    px(x, C.path, 0, 0, T, T);
    var r = rng(33);
    for (var i = 0; i < 10; i++) px(x, C.path2, (r() * T) | 0, (r() * T) | 0, 2, 1);
    for (var j = 0; j < 4; j++) px(x, C.pathS, (r() * T) | 0, (r() * T) | 0);
  });
  make("sea", function (x, f) {
    px(x, C.sea, 0, 0, T, T);
    for (var i = 0; i < 3; i++) { var y = (i * 5 + f * 2) % T; px(x, C.sea2, (i * 6 + f) % 12, y, 5, 1); }
    px(x, C.seaL, (3 + f * 4) % 14, (9 + f) % T, 2, 1);
  }, 4);
  make("ice", function (x) { px(x, C.ice, 0, 0, T, T); px(x, C.iceS, 2, 5, 6, 1); px(x, C.iceS, 9, 11, 5, 1); px(x, "#ffffff", 4, 3, 2, 1); });
  make("dock", function (x) {
    px(x, C.wood, 0, 0, T, T);
    for (var i = 0; i < 4; i++) { px(x, C.woodD, 0, i * 4 + 3, T, 1); px(x, C.woodL, 0, i * 4, T, 1); }
    px(x, C.woodD, 3, 1, 1, 1); px(x, C.woodD, 12, 9, 1, 1);
  });
  make("strip", function (x) { px(x, C.strip, 0, 0, T, T); px(x, "#b6c0cb", 0, 0, T, 1); px(x, "#b6c0cb", 0, 15, T, 1); });
  make("stripMark", function (x) { px(x, C.strip, 0, 0, T, T); px(x, C.stripL, 3, 7, 10, 2); });
  make("roof", function (x) {
    px(x, C.roof, 0, 0, T, T);
    for (var i = 0; i < 4; i++) px(x, C.roofD, 0, i * 4 + 3, T, 1);
    px(x, C.roofSnow, 0, 0, T, 5); px(x, C.roofSnow, 2, 5, 5, 1); px(x, C.roofSnow, 10, 5, 4, 2);
  });
  make("chimney", function (x) {
    px(x, C.roof, 0, 0, T, T); px(x, C.roofSnow, 0, 0, T, 5);
    px(x, C.rockD, 5, 1, 6, 9); px(x, C.rock, 6, 2, 4, 7); px(x, C.roofSnow, 5, 0, 6, 2);
  });
  make("wall", function (x) {
    px(x, C.wood, 0, 0, T, T);
    for (var i = 0; i < 4; i++) px(x, C.woodD, 0, i * 4 + 3, T, 1);
    px(x, C.woodL, 0, 0, T, 1);
  });
  make("window", function (x) {
    px(x, C.wood, 0, 0, T, T);
    for (var i = 0; i < 4; i++) px(x, C.woodD, 0, i * 4 + 3, T, 1);
    px(x, C.woodD, 3, 3, 10, 9); px(x, C.win, 4, 4, 8, 7); px(x, C.winL, 5, 5, 3, 2); px(x, C.woodD, 7, 4, 1, 7); px(x, C.woodD, 4, 7, 8, 1);
    px(x, C.roofSnow, 3, 12, 10, 1);
  });
  make("door", function (x) {
    px(x, C.wood, 0, 0, T, T); px(x, C.door, 3, 2, 10, 14); px(x, C.woodD, 3, 2, 10, 1); px(x, C.winL, 10, 9, 1, 2);
  });
  make("tree", function (x) {
    snowBase(x, 5);
    px(x, C.trunk, 7, 12, 2, 4);
    var rows = [[7, 1, 2], [6, 3, 4], [5, 5, 6], [4, 7, 8], [3, 9, 10], [2, 10, 12]];
    rows.forEach(function (r) { px(x, C.tree, r[0], r[1], T - 2 * r[0], 2); });
    px(x, C.treeD, 9, 6, 4, 6); px(x, C.treeSnow, 6, 3, 3, 1); px(x, C.treeSnow, 4, 7, 4, 1); px(x, C.treeSnow, 9, 9, 4, 1); px(x, C.treeSnow, 3, 11, 3, 1);
  });
  make("rock", function (x) {
    snowBase(x, 13);
    px(x, C.rockD, 2, 7, 12, 7); px(x, C.rock, 3, 6, 10, 6); px(x, C.rockL, 4, 7, 4, 2); px(x, C.snow, 4, 5, 7, 2);
  });
  make("fence", function (x) {
    snowBase(x, 21);
    px(x, C.woodD, 1, 5, 2, 10); px(x, C.woodD, 13, 5, 2, 10); px(x, C.wood, 0, 7, T, 2); px(x, C.wood, 0, 11, T, 2); px(x, C.roofSnow, 0, 6, T, 1);
  });
  make("drift", function (x) {
    snowBase(x, 41);
    px(x, C.snowS, 0, 8, T, 8); px(x, "#dbe5ef", 1, 6, 14, 4); px(x, "#ffffff", 2, 5, 10, 2); px(x, C.snowS, 4, 12, 9, 1);
  });
  make("sign", function (x) {
    snowBase(x, 3);
    px(x, C.woodD, 7, 8, 2, 8); px(x, C.woodD, 2, 2, 12, 7); px(x, C.woodL, 3, 3, 10, 5); px(x, C.woodD, 5, 5, 6, 1); px(x, C.roofSnow, 2, 1, 12, 1);
  });
  make("stall", function (x) {
    px(x, C.stall, 0, 6, T, 10); px(x, C.woodD, 0, 6, T, 1); px(x, C.woodD, 0, 15, T, 1);
    for (var i = 0; i < 4; i++) { px(x, i % 2 ? C.awning : C.awning2, i * 4, 0, 4, 5); }
    px(x, "#8b5a2b", 2, 8, 3, 3); px(x, "#e8d9b8", 7, 8, 3, 3); px(x, "#6f8f5b", 11, 8, 3, 3);
  });
  make("fire", function (x, f) {
    snowBase(x, 17);
    px(x, C.rockD, 2, 12, 12, 3); px(x, C.rock, 3, 12, 3, 2); px(x, C.rock, 10, 12, 3, 2);
    px(x, C.ember, 5, 11, 6, 2);
    var h = [6, 8, 7][f % 3];
    px(x, C.fireD, 5, 13 - h, 6, h - 1); px(x, C.fire, 6, 14 - h, 4, h - 2); px(x, C.fireL, 7, 15 - h + (f % 2), 2, h - 4);
  }, 3);
  make("tent", function (x) {
    snowBase(x, 23);
    for (var i = 0; i < 8; i++) px(x, i < 4 ? C.tentD : C.tent, 8 - i, 3 + i * 1.5 | 0, i * 2, 2);
    px(x, C.tent, 1, 13, 14, 2); px(x, C.ember, 7, 9, 2, 6);
  });
  make("mtn", function (x) {
    px(x, C.mtn, 0, 0, T, T);
    px(x, C.mtnD, 0, 10, T, 6); px(x, "#ffffff", 4, 0, 8, 3); px(x, "#dfe8f1", 2, 3, 12, 3);
  });
  make("boat", function (x) {
    px(x, C.sea, 0, 0, T, T);
    px(x, "#c84b31", 1, 7, 14, 4); px(x, "#7d2a1c", 2, 11, 12, 2); px(x, "#f6efe2", 3, 6, 10, 1); px(x, C.woodD, 7, 1, 1, 6);
  });
  make("plane", function (x) {
    px(x, C.strip, 0, 0, T, T);
    px(x, C.planeL, 1, 6, 14, 4); px(x, C.plane, 1, 8, 14, 2); px(x, C.planeD, 0, 2, 16, 2); px(x, "#5b7fa3", 10, 6, 3, 2); px(x, C.navy, 7, 11, 2, 2);
  });
  make("doghouse", function (x) {
    snowBase(x, 51);
    px(x, C.woodD, 2, 6, 12, 9); px(x, C.wood, 3, 7, 10, 8); px(x, C.door, 6, 10, 4, 5); px(x, C.roofSnow, 1, 4, 14, 3);
  });

  /* ---------------- characters (16x16, 4 directions × 2 walk frames) ---------------- */
  var PEOPLE = {
    player:   { parka: "#3d6fb6", parkaD: "#2a4f86", trim: "#efe7da", skin: "#d9a37e", hair: "#2b2320", pants: "#33384a", boots: "#6b4a2f" },
    anansiak: { parka: "#8a3f5f", parkaD: "#672c46", trim: "#f2ece2", skin: "#c99572", hair: "#b9b6b2", pants: "#3a3340", boots: "#5c3e27", hat: "#d9c2a3" },
    hulda:    { parka: "#3d8a6b", parkaD: "#2b6650", trim: "#efe7da", skin: "#d7a17a", hair: "#2c1f1b", pants: "#2f3448", boots: "#6b4a2f" },
    tami:     { parka: "#9a6b2e", parkaD: "#73501f", trim: "#ece2d0", skin: "#c99472", hair: "#241b18", pants: "#3a3b45", boots: "#4e3420", apron: "#e9e3d6" },
    rita:     { parka: "#c4632f", parkaD: "#984a21", trim: "#f0e8dc", skin: "#d4a07b", hair: "#3a2a22", pants: "#2f3448", boots: "#6b4a2f", vest: "#f2c43d" },
    makusi:   { parka: "#5c4ea8", parkaD: "#43398a", trim: "#efe7da", skin: "#dba982", hair: "#221a17", pants: "#2c3142", boots: "#6b4a2f", bag: "#d0882f" }
  };

  function drawPerson(x, p, dir, fr) {
    var bob = fr ? 1 : 0;
    // boots & legs
    var l = fr ? 1 : 0;
    px(x, p.pants, 5, 11, 2, 3 - l); px(x, p.pants, 9, 11, 2, 2 + l);
    px(x, p.boots, 5, 14 - l, 3, 2); px(x, p.boots, 8, 13 + l, 3, 2);
    // body
    px(x, p.parka, 4, 6 + bob, 8, 6); px(x, p.parkaD, 4, 11 + bob, 8, 1);
    if (p.apron && dir === 0) px(x, p.apron, 6, 8 + bob, 4, 4);
    if (p.vest) { px(x, p.vest, 4, 7 + bob, 2, 4); px(x, p.vest, 10, 7 + bob, 2, 4); }
    if (p.bag && dir !== 0) px(x, p.bag, dir === 3 ? 10 : 3, 7 + bob, 3, 4);
    // arms
    px(x, p.parkaD, 3, 7 + bob, 1, 4); px(x, p.parkaD, 12, 7 + bob, 1, 4);
    // hood + face
    px(x, p.trim, 4, 1 + bob, 8, 6); px(x, p.parka, 5, 0 + bob, 6, 2);
    if (dir === 1) { // up (back)
      px(x, p.parka, 5, 2 + bob, 6, 4);
    } else {
      px(x, p.skin, 5, 2 + bob, 6, 4); px(x, p.hair, 5, 2 + bob, 6, 1);
      if (p.hat) px(x, p.hat, 5, 1 + bob, 6, 1);
      if (dir === 0) { px(x, C.navy, 6, 4 + bob); px(x, C.navy, 9, 4 + bob); }
      if (dir === 2) { px(x, C.navy, 6, 4 + bob); px(x, p.trim, 4, 2 + bob, 1, 4); }
      if (dir === 3) { px(x, C.navy, 9, 4 + bob); px(x, p.trim, 11, 2 + bob, 1, 4); }
    }
  }
  var sprites = {};
  Object.keys(PEOPLE).forEach(function (k) {
    sprites[k] = [];
    for (var d = 0; d < 4; d++) {
      sprites[k][d] = [];
      for (var f = 0; f < 2; f++) { var a = cv(T, T); drawPerson(a[1], PEOPLE[k], d, f); sprites[k][d].push(a[0]); }
    }
  });
  // dog
  sprites.dog = [0, 1].map(function (f) {
    var a = cv(T, T), x = a[1];
    px(x, "#4b4038", 3, 7, 10, 5); px(x, "#efe7da", 5, 9, 6, 3); px(x, "#4b4038", 11, 4 + f, 4, 4); px(x, "#efe7da", 12, 6 + f, 2, 2);
    px(x, C.navy, 13, 5 + f); px(x, "#4b4038", 1, 5 - f, 2, 4); px(x, "#4b4038", 4, 12, 2, 3); px(x, "#4b4038", 10, 12, 2, 3);
    return a[0];
  });

  /* ---------------- portraits (48x48) ---------------- */
  function portrait(key, face) {
    var p = PEOPLE[key], a = cv(48, 48), x = a[1];
    px(x, "#253552", 0, 0, 48, 48); px(x, "#2e4266", 0, 30, 48, 18);
    // shoulders
    px(x, p.parka, 6, 34, 36, 14); px(x, p.parkaD, 6, 44, 36, 4);
    if (p.vest) { px(x, p.vest, 9, 36, 7, 12); px(x, p.vest, 32, 36, 7, 12); }
    if (p.apron) px(x, p.apron, 17, 38, 14, 10);
    // hood fur
    px(x, p.trim, 9, 4, 30, 30); px(x, p.parka, 12, 2, 24, 4);
    for (var i = 0; i < 8; i++) px(x, "#d8cfc0", 9 + i * 4, 4 + (i % 2) * 2, 2, 2);
    // face
    px(x, p.skin, 14, 10, 20, 22); px(x, p.skin, 16, 31, 16, 2);
    px(x, p.hair, 14, 9, 20, 5); px(x, p.hair, 14, 13, 3, 5); px(x, p.hair, 31, 13, 3, 5);
    if (p.hat) { px(x, p.hat, 13, 6, 22, 5); px(x, "#b8a084", 13, 10, 22, 1); }
    if (key === "anansiak") { px(x, "#a39c95", 14, 9, 20, 4); px(x, "#7a6a5c", 17, 25, 1, 1); }
    // eyes
    var ey = 18;
    if (face === "surprised") { px(x, C.navy, 18, ey - 1, 3, 4); px(x, C.navy, 27, ey - 1, 3, 4); }
    else if (face === "happy") { px(x, C.navy, 18, ey + 1, 3, 1); px(x, C.navy, 17, ey + 2, 1, 1); px(x, C.navy, 21, ey + 2, 1, 1); px(x, C.navy, 27, ey + 1, 3, 1); px(x, C.navy, 26, ey + 2, 1, 1); px(x, C.navy, 30, ey + 2, 1, 1); }
    else { px(x, C.navy, 18, ey, 3, 3); px(x, C.navy, 27, ey, 3, 3); px(x, "#ffffff", 19, ey, 1, 1); px(x, "#ffffff", 28, ey, 1, 1); }
    if (face === "puzzled") { px(x, C.navy, 17, ey - 3, 4, 1); px(x, C.navy, 27, ey - 2, 4, 1); }
    // cheeks
    px(x, "#e48f7a", 16, 23, 3, 2); px(x, "#e48f7a", 29, 23, 3, 2);
    // mouth
    if (face === "happy") { px(x, "#8e3b33", 21, 26, 6, 1); px(x, "#8e3b33", 20, 25, 1, 1); px(x, "#8e3b33", 27, 25, 1, 1); px(x, "#f2f2f2", 22, 26, 4, 1); }
    else if (face === "surprised") { px(x, "#8e3b33", 22, 25, 4, 3); }
    else if (face === "puzzled") { px(x, "#8e3b33", 21, 27, 3, 1); px(x, "#8e3b33", 24, 26, 3, 1); }
    else px(x, "#8e3b33", 21, 26, 6, 1);
    if (key === "makusi") { px(x, p.bag, 36, 36, 8, 10); }
    return a[0];
  }
  var portraits = {};
  ["anansiak", "hulda", "tami", "rita", "makusi", "player"].forEach(function (k) {
    portraits[k] = {};
    ["normal", "happy", "surprised", "puzzled"].forEach(function (f) { portraits[k][f] = portrait(k, f).toDataURL(); });
  });

  /* ---------------- small illustrations for dialogue ---------------- */
  function illus(kind) {
    var a = cv(96, 48), x = a[1];
    px(x, "#1b2945", 0, 0, 96, 48);
    if (kind === "stars4") {
      [[14, 10], [38, 20], [62, 8], [80, 26]].forEach(function (s) {
        px(x, "#ffe9a3", s[0], s[1] - 3, 1, 7); px(x, "#ffe9a3", s[0] - 3, s[1], 7, 1); px(x, "#fff7d6", s[0] - 1, s[1] - 1, 3, 3);
      });
      px(x, "#2c3d5e", 0, 38, 96, 10); px(x, "#eef3f8", 0, 44, 96, 4);
    } else if (kind === "sunny") {
      px(x, "#7fb7e3", 0, 0, 96, 48); px(x, "#ffd65c", 70, 6, 14, 14); px(x, "#fff2b3", 73, 9, 8, 8); px(x, "#eef3f8", 0, 36, 96, 12); px(x, "#ffffff", 10, 10, 18, 4);
    } else if (kind === "clock1030") {
      px(x, "#eef3f8", 0, 0, 96, 48); px(x, "#ffffff", 30, 2, 36, 44); px(x, C.navy, 30, 2, 36, 1); px(x, C.navy, 30, 45, 36, 1); px(x, C.navy, 30, 2, 1, 44); px(x, C.navy, 65, 2, 1, 44);
      px(x, C.navy, 47, 24, 2, 18); px(x, C.navy, 39, 18, 9, 2); px(x, C.navy, 37, 16, 2, 2);
    } else if (kind === "dogs2") {
      px(x, "#eef3f8", 0, 0, 96, 48); x.drawImage(sprites.dog[0], 20, 20, 32, 32); x.drawImage(sprites.dog[1], 52, 20, 32, 32);
    }
    return a[0].toDataURL();
  }

  window.ART = { T: T, C: C, tiles: tiles, sprites: sprites, portraits: portraits, illus: illus };
})();
