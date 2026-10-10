# -*- coding: utf-8 -*-
"""
Inuttitut(ラブラドール方言)A2 例文バンク — 提出用ドキュメントとゲームの唯一の元データ。

種類 (kind):
  P  授業資料に印刷された文・語句をそのまま転記
  T  授業資料の活用表に印刷された語形をそのまま転記
  R  授業資料に印刷された語形と規則だけで組み立てた文(練習テストの答えなど)。根拠を note に明記
  W  ネット上のラブラドール方言資料。出典 URL を明記
"""

SRC = {
    "I1":  "INUTTITUT I, Katimanik #1 (2025-09-09)",
    "I2":  "INUTTITUT I, Katimanik #2 (2025-09-11)",
    "I3":  "INUTTITUT I, Katimanik #3 (2025-09-16)",
    "I8":  "INUTTITUT I, Katimanik #8 (2025-10-07)",
    "I9":  "INUTTITUT I, Katimanik #9 (2025-10-09)",
    "I10": "INUTTITUT I, Numarait (2025-10-16)",
    "I11": "INUTTITUT I, Katimanik #11 (2025-10-21)",
    "II1": "INUTTITUT II, Katimanik #1 (2025-10-28)",
    "II3": "INUTTITUT II, Katimanik #3 (2025-11-04)",
    "II8": "INUTTITUT II, Katimanik #8 (2025-11-20)",
    "PT":  "Practice Test (2025-11-13)",
    "NG":  "Nunatsiavut Government, Language resources — https://nunatsiavut.com/language-resources/",
    "TU2": "Tusâlanga (Nunatsiavummiutut), Lesson 2 — https://nunatsiavut.tusaalanga.ca/lesson/2",
    "TU3": "Tusâlanga (Nunatsiavummiutut), Lesson 3 — https://nunatsiavut.tusaalanga.ca/lesson/3",
    "TU4": "Tusâlanga (Nunatsiavummiutut), Lesson 4 — https://nunatsiavut.tusaalanga.ca/lesson/4",
    "TU5": "Tusâlanga (Nunatsiavummiutut), Lesson 5 — https://nunatsiavut.tusaalanga.ca/lesson/5",
    "TUT": "Tusâlanga (Nunatsiavummiutut), Grammar 41 'Telling Time' — https://nunatsiavut.tusaalanga.ca/node/1115",
    "TUP": "Tusâlanga (Nunatsiavummiutut), Grammar 29 'Possessions & Relations' — https://nunatsiavut.tusaalanga.ca/node/1110",
    "DIC": "Labrador Virtual Museum, English-Inuttut Dictionary — https://www.labradorvirtualmuseum.ca/english-inuttut.htm",
}

KIND_JA = {"P": "授業資料の原文", "T": "授業資料の活用表", "R": "授業資料の形と規則から作成", "W": "ネット資料"}


def s(kind, inu, en, ja, src, note=""):
    return {"kind": kind, "inu": inu, "en": en, "ja": ja, "src": src, "note": note}


UNITS = []

# ---------------------------------------------------------------- U1
UNITS.append({
    "id": "u1", "cefr": "A1.1", "title": "Ilitannamek! — あいさつ", "en": "Greetings",
    "cando": "あいさつをして、相手の調子をたずね、答えられる。はい・いいえで答えられる。",
    "grammar": [
        ("決まった表現として覚える", "Ilitannamek!(やあ!)・Atsunai!(さようなら)は、そのまま覚える定型表現。Kanuiven?(元気?)は動詞 Kanui- に2人称単数の疑問語尾 -ven? がついた形。"),
        ("「元気です」は否定形", "Kanuingilanga は否定語尾 -ngilanga(1人称単数)の形。「悪くない=元気です」という言い方になる。"),
        ("「あなたは?」", "Iffilittauk? で「あなたは?」と聞き返す(-littauk = 話題を相手に移す)。"),
    ],
    "sentences": [
        s("P", "Ilitannamek!", "Hello! (to someone you haven't seen for a while)", "やあ!(久しぶりに会った人へのあいさつ)", "I2", "辞書の語釈: Greeting of old friends; nice to see you again!"),
        s("P", "Kanuiven?", "How are you?", "元気?", "I2"),
        s("P", "Kanuingilanga.", "I'm fine.", "元気です。", "I2", "否定語尾 -ngilanga の形"),
        s("P", "Iffilittauk?", "And you?", "あなたは?", "I2"),
        s("P", "Â.", "Yes.", "はい。", "I9"),
        s("P", "Auka.", "No.", "いいえ。", "I1"),
        s("P", "Ate! Atsunai, Rita.", "OK! Goodbye, Rita.", "じゃあね!さようなら、Rita。", "I2"),
        s("P", "Atsunai!", "Goodbye!", "さようなら!", "I2"),
        s("W", "Ullâkut.", "Good morning.", "おはよう。", "NG"),
        s("W", "Ullusiakkut.", "Good day.", "こんにちは。", "NG"),
        s("W", "Nakummek.", "Thank you.", "ありがとう。", "NG"),
        s("W", "Ilâli.", "Welcome.", "ようこそ。", "NG"),
        s("W", "Kanuivâ?", "How is he/she?", "彼/彼女は元気?", "NG"),
    ],
})

# ---------------------------------------------------------------- U2
UNITS.append({
    "id": "u2", "cefr": "A1.1", "title": "Nanimiunguven? — 自己紹介と出身", "en": "Introductions",
    "cando": "人を紹介し、出身地をたずね、答えられる。",
    "grammar": [
        ("紹介する: Una ~", "Una(これ/この人)+ 名前・名詞 で「こちらは〜です」。Una ilannâga Hulda.(こちらは私の友達のHulda)"),
        ("出身: 地名 + -miuk + -u- + 語尾", "-miuk は「〜の人」、-u- は「〜である」。Nain → Nainimiunguvunga(私はNain出身です)。疑問は語尾を -ven? にして Nanimiunguven?(どこ出身?)。"),
        ("3人称", "語尾を -juk / -jong? に替えると「彼/彼女は」。Anânait nanimiungujong?(あなたのお母さんはどこの出身?)"),
    ],
    "sentences": [
        s("P", "Una ilannâga Hulda.", "This is my friend Hulda.", "こちらは私の友達のHuldaです。", "I2"),
        s("P", "Hulda, una Rita.", "Hulda, this is Rita.", "Hulda、こちらはRitaです。", "I2"),
        s("P", "Nanimiunguven?", "Where are you from?", "どこの出身ですか?", "I2"),
        s("P", "Nainimiunguvunga.", "I'm from Nain.", "私はNainの出身です。", "I2"),
        s("P", "Makkovimmiunguvunga.", "I'm from Makkovik.", "私はMakkovikの出身です。", "I2"),
        s("P", "Anânait nanimiungujong?", "Where is your mother from?", "あなたのお母さんはどこの出身ですか?", "PT"),
        s("R", "Anânaga Nainimiungujuk.", "My mother is from Nain.", "私の母はNainの出身です。", "PT",
          "練習テストの問いへの答え。根拠: anânak + 所有語尾 -ga(I8・I11の表)、Nainimiunguvunga(I2)の語尾を3人称 -juk(I11の表)に替えた形"),
        s("W", "Kinauven?", "Who are you? / What's your name?", "あなたは誰?(お名前は?)", "TU2"),
    ],
})

# ---------------------------------------------------------------- U3
UNITS.append({
    "id": "u3", "cefr": "A1.1", "title": "Pisuvunga — 動詞と人称", "en": "Verbs and persons",
    "cando": "「私は/あなたは/彼は〜している」を言い分けられる。2人(双数)と3人以上(複数)を区別できる。",
    "grammar": [
        ("動詞 = 語根 + 人称語尾", "語根の最後の k を落として語尾をつける: pisuk-(歩く)→ pisuvunga(私は歩いている)。"),
        ("人称語尾(授業資料 I8・I11 の表)", "1人称: -vunga(私)/ -vuguk(私たち2人)/ -vugut(私たち3人以上)。2人称: -vutit / -vutik / -vusi。3人称: -juk / -jok / -jut。"),
        ("代名詞は普通いらない", "語尾が人称を示すので、「私は」「あなたは」は動詞だけで表せる。"),
    ],
    "sentences": [
        s("T", "Pisuvunga.", "I'm walking.", "私は歩いている。", "I2"),
        s("T", "Pisuvutit.", "You're walking.", "あなたは歩いている。", "I2"),
        s("T", "Pisujuk.", "He/she is walking.", "彼/彼女は歩いている。", "I2"),
        s("T", "Pisuvuguk.", "We two are walking.", "私たち2人は歩いている。", "I9"),
        s("T", "Pisuvutik.", "You two are walking.", "あなたたち2人は歩いている。", "I9"),
        s("T", "Pisujok.", "They two are walking.", "彼ら2人は歩いている。", "I9"),
        s("T", "Pisuvugut.", "We (3+) are walking.", "私たち(3人以上)は歩いている。", "I9"),
        s("T", "Pisuvusi.", "You (3+) are walking.", "あなたたち(3人以上)は歩いている。", "I9"),
        s("T", "Pisujut.", "They (3+) are walking.", "彼ら(3人以上)は歩いている。", "I9"),
        s("T", "Ilinniavunga.", "I'm learning.", "私は学んでいる。", "I2"),
        s("T", "SuliaKavutit.", "You're working.", "あなたは働いている。", "I2"),
        s("T", "uKâlajuk.", "He/she is speaking.", "彼/彼女は話している。", "I2"),
        s("T", "Itsivavunga.", "I'm sitting.", "私は座っている。", "I2"),
        s("P", "Inuttitut Laurie ilinniajuk.", "Laurie is learning Inuttitut.", "LaurieはInuttitutを学んでいる。", "II1"),
        s("R", "Mânna pisuvunga.", "I'm walking now.", "今、私は歩いている。", "I2",
          "授業資料の手書きメモにある文。根拠: pisuvunga(I2の表)、mânna = now(辞書)"),
    ],
})

# ---------------------------------------------------------------- U4
UNITS.append({
    "id": "u4", "cefr": "A1.2", "title": "Tuttuk pisujuk — 名詞と数", "en": "Nouns: one, two, many",
    "cando": "名詞の単数・双数(2つ)・複数(3つ以上)を使い分け、主語と動詞の数を合わせられる。",
    "grammar": [
        ("名詞の数(授業資料 I2・II1)", "単数 -Ø(nutagak)、双数は語末の母音を長くする -V(nutagâk)、複数 -it(nutagait)。"),
        ("主語と動詞の一致", "主語の名詞は語尾なしのまま。動詞の語尾を名詞の数に合わせる: Tuttuk pisujuk / Tuttok pisujok / Tuttuit pisujut。"),
    ],
    "sentences": [
        s("P", "Nutagak Kiajuk.", "The baby is crying.", "赤ちゃんが泣いている。", "II1"),
        s("P", "Nutagâk Kiajok.", "The two babies are crying.", "赤ちゃん2人が泣いている。", "II1"),
        s("P", "Nutagait Kiajut.", "The babies (3+) are crying.", "赤ちゃんたち(3人以上)が泣いている。", "II1"),
        s("P", "Tuttuk pisujuk.", "The caribou is walking.", "カリブーが歩いている。", "II1"),
        s("P", "Tuttok pisujok.", "The two caribou are walking.", "カリブー2頭が歩いている。", "II1"),
        s("P", "Tuttuit pisujut.", "The caribou (3+) are walking.", "カリブーたち(3頭以上)が歩いている。", "II1"),
        s("T", "annak — annâk — annait", "woman — two women — women (3+)", "女性 — 2人の女性 — 女性たち", "I2"),
        s("T", "angutik — angutek — angutet", "man — two men — men (3+)", "男性 — 2人の男性 — 男性たち", "I2"),
        s("T", "inuk — inok — inuit", "person — two people — people (3+)", "人 — 2人 — 人々", "I2"),
        s("T", "illuk — illok — illuit", "house — two houses — houses (3+)", "家 — 2軒 — 家々", "I2"),
        s("T", "nanuk — nanok — nanuit", "polar bear — two — (3+)", "シロクマ — 2頭 — 3頭以上", "I2"),
        s("T", "tingijok — tingijok — tingijot", "plane — two planes — planes (3+)", "飛行機 — 2機 — 3機以上", "I2"),
    ],
})

# ---------------------------------------------------------------- U5
UNITS.append({
    "id": "u5", "cefr": "A1.2", "title": "Sunamik takuven? — 質問と否定", "en": "Questions and negation",
    "cando": "はい/いいえの質問と「何?」「いくつ?」「どこへ?」の質問をし、否定で答えられる。",
    "grammar": [
        ("疑問語尾(授業資料 I8・I11)", "1人称: -vingâ? / -vinong? / -vitâ?、2人称: -ven? / -viteng? / -vise?、3人称: -jong? / -joung? / -jon?"),
        ("否定語尾", "-vu- / -ju- の代わりに -ngila- / -ngitu-: -ngilanga / -ngilatit / -ngituk(以下、双数・複数も表あり)。会話では3人称に -ngilak の形も出る(Anugingilak)。"),
        ("疑問詞", "Sunamik ...?(何を)、Katsinik ...?(いくつの)、Namut ...?(どこへ)、Nautaima ...?(どこ)。疑問詞をつけた名詞は -mik / -nik をとる。"),
    ],
    "sentences": [
        s("T", "Pisungilanga.", "I'm not walking.", "私は歩いていない。", "I9"),
        s("T", "Pisungilatit.", "You're not walking.", "あなたは歩いていない。", "I9"),
        s("T", "Pisungituk.", "He/she isn't walking.", "彼/彼女は歩いていない。", "I9"),
        s("T", "Takuven?", "Do you see (it)?", "(それが)見える?", "II3"),
        s("T", "Takujong?", "Does he/she see (it)?", "彼/彼女は見える?", "II3"),
        s("T", "Takuvise?", "Do you (3+) see (it)?", "あなたたち(3人以上)は見える?", "II3"),
        s("P", "Sunamik takuven?", "What do you see?", "何が見えますか?", "II1"),
        s("P", "Katsinik ullugiannik takuven?", "How many stars do you see?", "星がいくつ見えますか?", "PT"),
        s("R", "Sitamannik ullugiannik takuvunga.", "I see four stars.", "星が4つ見えます。", "PT",
          "練習テストの問いへの答え。根拠: sitamannik(I8)、ullugiannik(PT)、takuvunga(II3の表)"),
        s("R", "Aunâvingâ?", "Am I bleeding?", "私、血が出てる?", "PT", "練習テストの問題 'Aunâ__? Am I bleeding?' に 1人称疑問語尾 -vingâ?(I11)を入れた形"),
        s("R", "Kamennik pisijong?", "Is she buying boots?", "彼女はブーツを買っているの?", "PT", "練習テストの問題 'kamennik pisi__?' に 3人称疑問語尾 -jong?(I11)を入れた形"),
        s("R", "Kongavise?", "Are you (3+) angry?", "あなたたち(3人以上)は怒っているの?", "PT", "練習テストの問題 'Konga__?' に 2人称複数の疑問語尾 -vise?(I11)を入れた形"),
        s("P", "Namut appaliven?", "Where are you running to?", "どこへ走って行くの?", "II1"),
        s("R", "Nautaima niaKuit?", "Where is your head?", "あなたの頭はどこ?", "I11",
          "根拠: 疑問詞 nautaima...?(I11)、niaKuk + 2人称所有 -it(I11の表。illuk → illuit と同じ規則)"),
        s("R", "NiaKuga.", "(This is) my head.", "私の頭(です)。", "I11", "根拠: niaKuk + 1人称所有 -ga(I11の表。illuk → illuga と同じ規則)"),
    ],
})

# ---------------------------------------------------------------- U6
UNITS.append({
    "id": "u6", "cefr": "A1.2", "title": "PaniKavunga — 家族と持ち物", "en": "Family and possession",
    "cando": "家族や持ち物について「私の/あなたの/彼女の」を使って話し、「〜がいる/ある」「いくつ」を言える。",
    "grammar": [
        ("所有語尾(授業資料 I8・I11)", "私の: -ga(1つ)/ -Vkka(2つ)/ -kka(3つ以上)。あなたの: -it / -Vkkik / -tit。彼/彼女の: -nga / -Vgik / -ngit。"),
        ("「〜を持つ・〜がいる」= 名詞 + -Ka-", "PaniKavunga.(娘がいます)。数は -mik / -nik をつけて前に置く: Atautsimik / Maggonik / Pingasunnik paniKavunga。"),
        ("「〜の」= -up", "持ち主に -up、持ち物に -nga: Marinaup umianga(Marinaの船)。持ち主が2人なら -V、3人以上なら -it(annâk Kimminga / annait Kimminga)。"),
    ],
    "sentences": [
        s("T", "paniga — panet — paninga", "my daughter — your daughter — her daughter", "私の娘 — あなたの娘 — 彼女の娘", "I8"),
        s("T", "panikka — panitit — paningit", "my / your / her daughters (3+)", "私の/あなたの/彼女の娘たち(3人以上)", "I8"),
        s("T", "illuga — illuit — illunga", "my house — your house — her house", "私の家 — あなたの家 — 彼女の家", "I8"),
        s("T", "umiaga — umiat — umianga", "my boat — your boat — her boat", "私の船 — あなたの船 — 彼女の船", "I8"),
        s("T", "nunaga — nunait — nunanga", "my land — your land — her/his land", "私の土地 — あなたの土地 — 彼女/彼の土地", "I2"),
        s("P", "PaniKavunga.", "I have a daughter.", "私には娘がいます。", "I8"),
        s("P", "Atautsimik paniKavunga.", "I have one daughter.", "私には娘が1人います。", "I8"),
        s("P", "Maggonik paniKavunga.", "I have two daughters.", "私には娘が2人います。", "I8"),
        s("P", "Pingasunnik paniKavunga.", "I have three daughters.", "私には娘が3人います。", "I8"),
        s("P", "Katsinik KimmiKaven?", "How many dogs do you have?", "犬を何匹飼っていますか?", "II1"),
        s("R", "Maggonik KimmiKavunga.", "I have two dogs.", "犬を2匹飼っています。", "I8", "根拠: Maggonik paniKavunga(I8)の panik を Kimmik(II1)に替えた形"),
        s("P", "Marinaup umianga", "Marina's boat", "Marinaの船", "II1"),
        s("P", "annaup Kimminga", "the woman's dog", "その女性の犬", "II1"),
        s("P", "annâk Kimminga", "the two women's dog", "2人の女性の犬", "II1"),
        s("P", "annait Kimminga", "the women's (3+) dog", "女性たちの犬", "II1"),
        s("R", "Kimmikka", "my dogs (3+)", "私の犬たち", "PT", "練習テストの問題 'Kimmi__ (my dogs)' に -kka(I8の表)を入れた形"),
        s("R", "tingijotit", "your planes (3+)", "あなたの飛行機(3機以上)", "PT", "練習テストの問題 'tingijo__ (your planes)' に -tit(I8の表。panik → panitit と同じ規則)を入れた形"),
        s("R", "pitsiga", "my dried fish", "私の干し魚", "PT", "練習テストの問題 'pitsi__ (my pitsik)' に -ga を入れた形。pitsik = dried fish(辞書)"),
        s("R", "maggangit", "his dishes", "彼の皿(3枚以上)", "PT", "練習テストの問題 'magga__ (his dishes)' に -ngit を入れた形"),
        s("R", "aninninga", "her life", "彼女の命", "PT", "練習テストの問題 'aninni__ (her life)' に -nga を入れた形"),
    ],
    "vocab": [
        ("aippak", "spouse, partner", "配偶者"), ("anânak", "mother", "母"), ("atâtak", "father", "父"),
        ("panik", "daughter", "娘"), ("innik", "son", "息子"), ("sugusik", "child", "子ども"),
        ("nutagak", "baby", "赤ちゃん"), ("angajuk", "older sibling (same sex)", "同性の年上のきょうだい"),
        ("nukak", "younger sibling (same sex)", "同性の年下のきょうだい"), ("najak", "sister (of a boy)", "(男性から見た)姉妹"),
        ("anik", "brother (of a girl)", "(女性から見た)兄弟"), ("anânsiak", "grandmother (mother's side)", "母方の祖母"),
        ("ânak", "grandmother (father's side)", "父方の祖母"), ("atâtsiak", "grandfather", "祖父"),
        ("ingutak", "grandchild", "孫"), ("ilannâk", "friend", "友達"),
    ],
})

# ---------------------------------------------------------------- U7
UNITS.append({
    "id": "u7", "cefr": "A2.1", "title": "Kâfittugumaven? — 食べ物と「〜したい」", "en": "Food and wanting",
    "cando": "飲み物や食べ物をすすめ、ほしいものを言える。食べた・食べなければならないを言える。",
    "grammar": [
        ("名詞 + -tu- = 〜を食べる/飲む", "kâfi(コーヒー)→ kâfittu-(コーヒーを飲む)、tuttuvinik(カリブー肉)→ tuttuvinittu-。"),
        ("-guma- = 〜したい", "語根と人称語尾の間に入れる: kâfittugumavunga(コーヒーが飲みたい)。"),
        ("-gasua-(〜しようとする)と -giaKa-(〜しなければならない)", "Puijivinittugasuaven?(アザラシ肉を食べてみる?)、Suli ullâsiutittugiaKavutit.(まだ朝ごはんを食べなきゃ)"),
        ("-lu = 〜も", "後ろの語につく: Immumillu?(ミルクも?)"),
    ],
    "sentences": [
        s("P", "KâfiKavâ?", "Is there any coffee?", "コーヒーある?", "I3"),
        s("P", "Â, kâfittugumaven?", "Yes — would you like some coffee?", "ええ、コーヒー飲みたい?", "I3"),
        s("P", "Â, kâfittugumavunga.", "Yes, I'd like some coffee.", "ええ、コーヒーが飲みたい。", "I3"),
        s("P", "Immumillu?", "Milk, too?", "ミルクも?", "I3"),
        s("P", "Â, immumik, sukarammilu.", "Yes, milk — and sugar, too.", "ええ、ミルクと、砂糖も。", "I3"),
        s("P", "Imikuluttugumavunga.", "I'd like a little water.", "お水を少し飲みたい。", "I3"),
        s("P", "UllâsiutittuKauven?", "Did you have breakfast (earlier today)?", "(今日)朝ごはんは食べた?", "PT"),
        s("R", "UllâsiutittuKauvunga.", "I had breakfast (earlier today).", "(今日)朝ごはんを食べました。", "PT", "練習テストの問いへの答え。根拠: 問いと同じ語幹に1人称 -vunga(I11の表)"),
        s("P", "Tuttuvinimmik nigikKauvunga.", "I ate caribou meat (earlier today).", "(今日)カリブーの肉を食べた。", "II1"),
        s("P", "Tuttugasuajuk.", "He/she is trying to eat caribou.", "彼/彼女はカリブーを食べようとしている。", "I9"),
        s("P", "Puijivinittugasuaven?", "Will you try some seal meat?", "アザラシの肉を食べてみる?", "I9"),
        s("P", "Suli ullâsiutittugiaKavutit.", "You still have to eat breakfast.", "まだ朝ごはんを食べなきゃいけないよ。", "I9"),
        s("R", "UllâsiutittugiaKaniattuk.", "He/she will have to eat breakfast (later today).", "彼/彼女は(このあと)朝ごはんを食べなければならない。", "PT",
          "練習テストの問題 'Ullâsiutittu__niattuk (Johnny will have to eat breakfast)' に -giaKa-(I9)を入れた形"),
        s("R", "Ippasak tuttuvinittulaukKen?", "Did you have caribou yesterday?", "昨日カリブーを食べた?", "PT",
          "練習テストの問題 'Ippasak tuttuvinittulauk__?' の答え。-lauk- の後の2人称疑問は -Ken?(Tusâlanga L3 の sulaukKen? と同じ形)"),
        s("W", "Tetugumaven?", "Would you like some tea?", "お茶はいかが?", "TU5"),
        s("W", "Â, tetugumavunga.", "Yes, I'd like some tea.", "ええ、お茶をください。", "TU5"),
        s("W", "ImmutuKattaven?", "Do you take milk?", "(いつも)ミルクを入れる?", "TU5"),
    ],
})

# ---------------------------------------------------------------- U8
UNITS.append({
    "id": "u8", "cefr": "A2.1", "title": "SuliaKalâttuk — 時と時制", "en": "Time and tense",
    "cando": "昨日・今日・あとで・明日のできごとを、時制を使い分けて言える。時刻を言える。",
    "grammar": [
        ("時制の接尾辞(授業資料 I9 の表)", "-lauk-(今日より前)、-kKau-(今日の早いうち)、-tainnak-(たった今)、-lik-(まさに今)、-giasi-(〜しかけている)、-niak-(今日このあと)、-langa-(今日このあと、Hebron方言)、-lâk-(明日以降)。"),
        ("k で終わる接尾辞のあと", "1人称 -vunga → -Kunga、3人称 -juk → -ttuk / -tuk になる: pisulaukKunga / pisulauttuk。"),
        ("時刻", "時刻にはドイツ語由来の数詞(ainsik, suvait, tarait ...)を使う。「〜時です」は数詞 + -vuk。「10時半に」= senaliak affami。"),
    ],
    "sentences": [
        s("T", "PisulaukKunga.", "I walked (before today).", "(昨日以前に)歩いた。", "I9"),
        s("T", "PisukKauvunga.", "I walked (earlier today).", "(今日のうちに)歩いた。", "I9"),
        s("T", "PisutainnaKunga.", "I just walked.", "たった今歩いてきた。", "I9"),
        s("T", "PisulikKunga.", "I'm walking right now.", "まさに今歩いている。", "I9"),
        s("T", "Pisugiasivunga.", "I'm about to walk.", "歩き出すところだ。", "I9"),
        s("T", "PisuniakKunga.", "I'll walk (later today).", "(今日このあと)歩く。", "I9"),
        s("T", "PisulâkKunga.", "I'll walk (tomorrow or later).", "(明日以降)歩く。", "I9"),
        s("T", "Pisulaungilanga.", "I didn't walk (before today).", "(昨日以前に)歩かなかった。", "I9"),
        s("T", "Pisulângilanga.", "I won't walk (tomorrow or later).", "(明日以降)歩かない。", "I9"),
        s("P", "SuliaKalauttuk.", "He/she worked (before today).", "彼/彼女は(昨日以前に)働いた。", "I9"),
        s("P", "SuliaKakKaujuk.", "He/she worked (earlier today).", "彼/彼女は(今日のうちに)働いた。", "I9"),
        s("P", "SuliaKalittuk.", "He/she is working right now.", "彼/彼女はまさに今働いている。", "I9"),
        s("P", "SuliaKaniattuk.", "He/she will work (later today).", "彼/彼女は(今日このあと)働く。", "I9"),
        s("P", "SuliaKalâttuk.", "He/she will work (tomorrow or later).", "彼/彼女は(明日以降)働く。", "I9"),
        s("P", "TikitainnaKunga.", "I just arrived.", "たった今着いた。", "I9"),
        s("P", "Tutsiagiasijuk.", "He/she is about to sing.", "彼/彼女は歌い出すところだ。", "I9"),
        s("P", "Pisulangajuk.", "He/she will walk (later today) — Hebron dialect.", "彼/彼女は(今日このあと)歩く(Hebron方言)。", "I9"),
        s("P", "Ullâmi Tracey tupakKaujuk.", "Tracey woke up this morning.", "Traceyは今朝起きた。", "II1"),
        s("P", "Tuttonik siagu Sabina takuniattuk.", "Sabina will see two caribou later.", "Sabinaはあとでカリブーを2頭見るだろう。", "II1"),
        s("P", "Tingijok senaliak affami tikiniattuk.", "The plane will arrive at half past ten.", "飛行機は10時半に着く。", "I9"),
        s("R", "Taraivuk.", "It's three o'clock.", "3時です。", "II8",
          "根拠: tarait(3、II8の数詞表)+ -vuk(〜時です。Tusâlanga 'Telling Time' の ainsivuk・suvaivuk と同じ作り方)"),
        s("T", "ainsik, suvait, tarait, fiarat, fimfit, sâtsit", "1, 2, 3, 4, 5, 6 (clock numbers)", "1, 2, 3, 4, 5, 6(時刻の数詞)", "II8"),
        s("T", "sepat, âttat, nainat, senat, ailfat, suvailfat", "7, 8, 9, 10, 11, 12 (clock numbers)", "7, 8, 9, 10, 11, 12(時刻の数詞)", "II8"),
        s("T", "atautsik, maggok, pingasut, sitamat, tallimat", "1, 2, 3, 4, 5", "1, 2, 3, 4, 5", "I10"),
    ],
})

# ---------------------------------------------------------------- U9
UNITS.append({
    "id": "u9", "cefr": "A2.1", "title": "Namut appaliven? — 場所と移動", "en": "Places and travel",
    "cando": "どこへ・どこから・どこで・何で(交通手段)を言い、移動の予定や経験を話せる。",
    "grammar": [
        ("場所の格語尾(授業資料 II1)", "-mi(〜で/に)、-mut(〜へ)、-mit(〜から)、-kkut(〜を通って/〜で〔手段〕)、-tigut(〜を横切って)、-tut(〜のように)。2つなら -Vni / -Vnut / -Vnit、3つ以上なら -ni / -nut / -nit。"),
        ("場所 + -lia- = 〜へ行く", "Hopedaliliavunga.(Hopedaleへ行く)、Nainiliavuguk.(私たち2人はNainへ行く)"),
        ("-giattu- = 〜しに行く", "Hebronimut sinigiattuvunga.(Hebronへ寝に行く)"),
    ],
    "sentences": [
        s("P", "Hopedaliliavunga.", "I'm going to Hopedale.", "私はHopedaleへ行きます。", "I2"),
        s("P", "Nainiliavuguk.", "We two are going to Nain.", "私たち2人はNainへ行きます。", "I2"),
        s("P", "Hebronimut sinigiattuvunga.", "I'm going to Hebron to sleep.", "Hebronへ寝に行きます。", "II1"),
        s("P", "Illumut itsivagiattulauttuk.", "He/she went into the house to sit down.", "彼/彼女は家へ座りに行った。", "II1"),
        s("P", "Rita illonut pisulauttuk.", "Rita walked to the two houses.", "Ritaは2軒の家へ歩いて行った。", "II1"),
        s("P", "Illunut pisulauttut.", "They walked to the houses.", "彼らは家々へ歩いて行った。", "II1"),
        s("P", "Marina tupimmit pisutainnatuk.", "Marina has just walked over from the tent.", "Marinaはたった今テントから歩いてきた。", "II1"),
        s("P", "Umiannit tikitainnaKunga.", "I've just arrived from the boats.", "たった今、船から着いた。", "II1"),
        s("R", "Nainimit tikitainnaKunga.", "I've just arrived from Nain.", "たった今Nainから着いた。", "PT",
          "練習テストの英文 'I (just) arrived from Nain.' の訳。根拠: Nainimut(I9)の -mut を -mit(II1)に替え、TikitainnaKunga(I9)"),
        s("P", "Nunakkut pisulaukKugut.", "We walked over land.", "私たちは陸を歩いて行った。", "II1"),
        s("P", "Nunakkut Hulda tikilauttuk ippasak.", "Hulda arrived by land yesterday.", "Huldaは昨日、陸路で着いた。", "II1"),
        s("P", "Andrea tingijokkut aullaniattuk.", "Andrea will leave by plane (later today).", "Andreaは(今日このあと)飛行機で出発する。", "II1"),
        s("P", "Tracey Kimutsikut Kainiattuk.", "Tracey will come by dog team (later today).", "Traceyは(今日このあと)犬ぞりで来る。", "II1"),
        s("P", "Nunatigut pisugajakKusi.", "You (3+) could walk across the land.", "あなたたちは陸を歩いて渡れる。", "II1"),
        s("P", "Boris nanuttut pisuKattajuk.", "Boris (always) walks like a polar bear.", "Borisはいつもシロクマのように歩く。", "II1"),
        s("P", "Tuttutut appaliget!", "Run like a caribou!", "カリブーのように走れ!", "II1"),
        s("P", "Selma illumi itsivajuk.", "Selma is sitting in the house.", "Selmaは家で座っている。", "II1"),
        s("P", "Ullumi Makusi niugguniattuk Nainimut.", "Today Makusi will travel to Nain.", "今日、MakusiはNainへ出かける。", "I9", "niugguk = visit another settlement(辞書)"),
        s("P", "Tingijok aullagiasijuk.", "The plane is about to leave.", "飛行機が出発しそうだ。", "I2"),
        s("P", "Kailiget!", "Come!", "おいで!", "I2"),
    ],
})

# ---------------------------------------------------------------- U10
UNITS.append({
    "id": "u10", "cefr": "A2.1", "title": "SilakKivâ? — 天気と朝の会話", "en": "Weather and a morning conversation",
    "cando": "天気をたずねて答え、「もし〜なら」を使って気持ちや予定を言える。命令の形を使える。",
    "grammar": [
        ("天気は動詞で言う", "Anugivâ?(風は吹いてる?)・Anugingilak.(風はない)のように、天気を表す動詞を3人称で使う。"),
        ("「もし〜なら」-ppat", "主語が主節と違うときの条件の語尾(3人称単数): Anugippat nangianiakKunga.(風が吹いたら、私は怖くなる)"),
        ("命令(授業資料 I8・I11)", "1人に -git / -ligit / -laugit(I11 では -get / -liget / -lauget と表記)、2人に -gittek …、3人以上に -gitsi …: Tupaliget!(起きなさい)"),
    ],
    "sentences": [
        s("P", "Makusi, tupaliget!", "Makusi, wake up!", "Makusi、起きなさい!", "I9"),
        s("P", "Â. SilakKivâ?", "OK. Is it nice outside?", "うん。天気はいい?", "I9"),
        s("P", "Â, silakKisuak.", "Yes, it's beautiful weather.", "ええ、とてもいい天気よ。", "I9"),
        s("P", "Anugivâ?", "Is it windy?", "風は吹いてる?", "I9"),
        s("P", "Anugippat nangianiakKunga.", "If it's windy, I'll be afraid.", "風が吹いていたら、怖くなりそう。", "I9", "nangiak = afraid of falling(辞書)"),
        s("P", "Anugingilak.", "It isn't windy.", "風はないわ。", "I9"),
        s("P", "Makiliget!", "Get up!", "起き上がりなさい!", "I9"),
        s("P", "Makusi makijuk.", "Makusi gets up.", "Makusiは起き上がる。", "I9"),
        s("P", "Rita ammalu Mary silakKisuammi tânisijok.", "Rita and Mary are dancing in the beautiful weather.", "RitaとMaryはいい天気の中で踊っている。", "II1"),
        s("T", "Tupagit! / Tupaligit! / Tupalaugit!", "Wake up! (to one person)", "起きて!(1人に)", "I8"),
        s("T", "Tupagittek! / Tupaligittek! / Tupalaugittek!", "Wake up! (to two people)", "起きて!(2人に)", "I8"),
        s("T", "Tupagitsi! / Tupaligitsi! / Tupalaugitsi!", "Wake up! (to three or more)", "起きて!(3人以上に)", "I8"),
        s("W", "Ullusiangujuk.", "It is a beautiful day.", "いい日だ。", "NG"),
        s("W", "Kannivâ?", "Is it snowing?", "雪が降っている?", "TU4"),
        s("W", "Annak mitsujuk.", "The woman is sewing.", "女性が縫い物をしている。", "NG"),
    ],
})

# ---------------------------------------------------------------- U11
UNITS.append({
    "id": "u11", "cefr": "A2.2", "title": "Atuatsisonguvunga — できる・してよい・しなければ", "en": "Can, may, must, try",
    "cando": "できること・許されていること・しなければならないこと・しようとしていることを言える。",
    "grammar": [
        ("動詞 → 動詞の接尾辞(授業資料 I9・I11)", "-songu-(できる)、-gunna-(してよい)、-giaKa-(しなければならない)、-giattu-(しに行く)、-gasua-(しようとする)、-titsi-(させる)、-jutsau-(されるべき)、-galâ-(ちょっと)、-kasâ-(しかける)、-gajak-(できるかも)、-galuak-(〜のに)、-Kattak-(いつも)、-guma-(したい)。"),
        ("目的語 -mik / -nik", "「〜を」には -mik(1つ)・-Vnik(2つ)・-nik(3つ以上): Kanimajunnik paitsiKauvutit.(あなたは病人たちの世話をした)"),
    ],
    "sentences": [
        s("P", "Atuatsisonguvunga.", "I can read.", "私は読める。", "I9"),
        s("P", "Atuatsigunnavunga.", "I'm allowed to read.", "私は読んでもいい。", "I9"),
        s("P", "Tikigunnajuk.", "He/she may arrive.", "彼/彼女は来てもいい。", "I9"),
        s("P", "Pisugunnangittuk.", "He/she isn't allowed to walk.", "彼/彼女は歩いてはいけない。", "I9"),
        s("P", "UtigiaKajuk.", "He/she has to go back.", "彼/彼女は戻らなければならない。", "I9"),
        s("P", "SuliaKagiattujuk.", "He/she is going to work.", "彼/彼女は働きに行く。", "I9"),
        s("P", "Inuttut ilinniagasuavugut.", "We are trying to learn Inuttut.", "私たちはInuttutを学ぼうとしている。", "I9"),
        s("P", "Takutitsijuk.", "He/she shows (it).", "彼/彼女は見せる。", "I9"),
        s("P", "Ilinniatitsijuk.", "He/she teaches.", "彼/彼女は教える。", "I9"),
        s("P", "Salumajutsaujuk.", "It should be clean.", "きれいにしておくべきだ。", "I9"),
        s("P", "Ukâlagalâjuk.", "He/she talks a little.", "彼/彼女はちょっと話す。", "I9"),
        s("P", "PuigukasâkKaujuk.", "He/she almost forgot (earlier today).", "彼/彼女は(今日)忘れかけた。", "I9"),
        s("P", "SanagajakKunga.", "I could make it.", "私はそれを作れるかもしれない。", "I9"),
        s("P", "PisugiaKagaluattuk.", "Even though he/she has to walk…", "彼/彼女は歩かなければならないのに…", "I9"),
        s("P", "AllaKattatuk.", "He/she writes regularly.", "彼/彼女はよく書く。", "I9"),
        s("P", "Aullagumalauttuk.", "He/she wanted to leave.", "彼/彼女は出発したがっていた。", "I9"),
        s("P", "Kanimajunnik paitsiKauvutit.", "You took care of sick people (earlier today).", "あなたは(今日)病人たちの世話をした。", "II1"),
        s("P", "Sinijunnik tupatsiKauvunga.", "I woke up the sleeping people (earlier today).", "私は(今日)寝ている人たちを起こした。", "II1"),
        s("P", "Tracey omajonnik tusâkKaujuk.", "Tracey listened to two animals (earlier today).", "Traceyは(今日)2匹の動物の声を聞いた。", "II1"),
        s("P", "Katajummik takukKauvunga.", "I saw something falling (earlier today).", "(今日)何かが落ちるのを見た。", "II1"),
        s("R", "Atuagammik allagumajuk.", "She wants to write a book.", "彼女は本を書きたがっている。", "PT", "練習テストの問題 'Atuagammik alla__juk (She wants to write a novel)' に -guma-(I9)を入れた形"),
        s("R", "Ilinniatitsijimik tusâjut.", "They are listening to the teacher.", "彼らは先生の話を聞いている。", "PT",
          "練習テストの英文の訳。根拠: tusâk-(I11の動詞リスト)、目的語 -mik(II1)、3人称複数 -jut(I11)、ilinniatitsijik = teacher(辞書。I9の Ilinniatitsijuk から)"),
    ],
})

# ---------------------------------------------------------------- U12
UNITS.append({
    "id": "u12", "cefr": "A2.2", "title": "Takuvagit — 「あなたを」「私を」", "en": "I see you: transitive endings",
    "cando": "「私があなたを」「あなたが私を」のように、主語と目的語を1語で言い分けられる。",
    "grammar": [
        ("他動詞の語尾(授業資料 II3 の表)", "1つの語尾が「誰が」と「誰を」を同時に表す。takuk-(見る)の例: takuvagit(私があなたを)、takuvamma(あなたが私を)、takujaga(私が彼/彼女を)、takujait(あなたが彼/彼女を)、takujanga(彼/彼女が彼/彼女を)、takuvânga(彼/彼女が私を)、takuvâtit(彼/彼女があなたを)。"),
        ("他動詞の疑問(II3 の表)", "takuvammâ?(あなたは私が見える?)、takujân?(あなたは彼/彼女が見える?)、takujagâ?(私は彼/彼女が見える?)"),
    ],
    "sentences": [
        s("T", "Takuvagit.", "I see you.", "私はあなたが見える。", "II3"),
        s("T", "Takuvamma.", "You see me.", "あなたは私が見える。", "II3"),
        s("T", "Takujaga.", "I see him/her.", "私は彼/彼女が見える。", "II3"),
        s("T", "Takujait.", "You see him/her.", "あなたは彼/彼女が見える。", "II3"),
        s("T", "Takujanga.", "He/she sees him/her.", "彼/彼女は彼/彼女が見える。", "II3"),
        s("T", "Takuvânga.", "He/she sees me.", "彼/彼女は私が見える。", "II3"),
        s("T", "Takuvâtit.", "He/she sees you.", "彼/彼女はあなたが見える。", "II3"),
        s("T", "Takujavut.", "We (3+) see him/her.", "私たちは彼/彼女が見える。", "II3"),
        s("T", "Takuvammâ?", "Do you see me?", "私が見える?", "II3"),
        s("T", "Takujân?", "Do you see him/her?", "彼/彼女が見える?", "II3"),
        s("P", "Illumit takukKaujaga.", "I saw him/her from the house (earlier today).", "(今日)家から彼/彼女を見た。", "II1"),
        s("P", "Napâttuni naffaKaujaka.", "I found them in the trees (earlier today).", "(今日)木々の中で彼らを見つけた。", "II1", "napâttuk = tree(辞書)。-ni = 3つ以上の場所「〜で」"),
        s("P", "SuliaKatimmut Hulda suangajaukKaujuk.", "Hulda was scolded by her co-worker (earlier today).", "Huldaは(今日)同僚に叱られた。", "II1", "suangak = scold(辞書)、-jau- = 〜される"),
    ],
})


def all_items():
    for u in UNITS:
        for i, x in enumerate(u["sentences"]):
            x = dict(x)
            x["id"] = f"{u['id']}-{i+1:02d}"
            x["unit"] = u["id"]
            yield x


if __name__ == "__main__":
    import collections
    c = collections.Counter(x["kind"] for x in all_items())
    print(len(UNITS), "units;", sum(c.values()), "items;", dict(c))
