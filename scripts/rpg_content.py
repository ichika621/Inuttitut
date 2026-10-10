# -*- coding: utf-8 -*-
"""
Single source for everything the village RPG says, in English and Japanese:
quests, dialogue scripts, small talk, grammar drills, signs, character names,
the "What is Inuttitut?" page, and a glossary of every other Inuttitut word or
word-part that appears outside the example bank.

RULE: Inuttitut may appear only as
  * a full example from a2_bank.py (say / choose / about examples / drills), or
  * a {{word}} inside English/Japanese text, where word is a bank example or a GLOSSARY key.
validate() enforces this, so the reviewer document (build_a2_doc.py) lists every
Inuttitut string the game can show.
"""
import re

def T(en, ja):
    return {"en": en, "ja": ja}

NPC_NAMES = {
    "anansiak": T("{{Anânsiak}} (Grandma)", "{{anânsiak}}(おばあちゃん)"),
    "hulda": T("{{Hulda}}", "{{Hulda}}"), "tami": T("{{Tâmi}}", "{{Tâmi}}"),
    "rita": T("{{Rita}}", "{{Rita}}"), "makusi": T("{{Makusi}}", "{{Makusi}}"),
}

# ---------------------------------------------------------------- glossary (non-bank Inuttitut)
# kind: word / part (suffix or ending) / name / letter
GLOSSARY = {
    "Inuttitut": ("name", T("the Inuit language of Labrador (also Inuttut, Nunatsiavummiutut)", "ラブラドールのイヌイット語(Inuttut, Nunatsiavummiutut とも)"), "Wikipedia 'Inuttitut'; course handout titles"),
    "Inuttut": ("name", T("another name for Inuttitut (used when speaking)", "Inuttitut の別名(話すときの呼び方)"), "Nunatsiavut Government app notice; course I9"),
    "Nunatsiavummiutut": ("name", T("another name for Inuttitut ('the language of the people of Nunatsiavut')", "Inuttitut の別名"), "Wikipedia 'Inuttitut'; Tusâlanga"),
    "Nunatsiavut": ("name", T("the Labrador Inuit region ('our beautiful land')", "ラブラドール・イヌイットの地域(「私たちの美しい土地」)"), "Nunatsiavut Government language page; course I1"),
    "Anânsiak": ("word", T("grandmother (mother's side) — used as Grandma's name in the game", "母方の祖母(ゲームではおばあちゃんの呼び名)"), "course I11; dictionary"),
    "anânsiak": ("word", T("grandmother (mother's side)", "母方の祖母"), "course I11; dictionary"),
    "Hulda": ("name", T("personal name (from the course dialogues)", "人名(授業の会話より)"), "course I2"),
    "Tâmi": ("name", T("personal name (from the course dialogues)", "人名(授業の会話より)"), "course I2"),
    "Rita": ("name", T("personal name (from the course dialogues)", "人名(授業の会話より)"), "course I2"),
    "Makusi": ("name", T("personal name (from the course dialogues)", "人名(授業の会話より)"), "course I9"),
    "kâfi": ("word", T("coffee", "コーヒー"), "course I3 (kâfittugumavunga); Tusâlanga lesson 5"),
    "pitsik": ("word", T("dried fish", "干し魚"), "Practice Test item 32; dictionary"),
    "ullugiak": ("word", T("star", "星"), "Practice Test item 1 (ullugiannik); dictionary"),
    "Kimmik": ("word", T("dog (Inuit dog)", "犬"), "course II1 (Katsinik KimmiKaven?); dictionary"),
    "ullâsiutik": ("word", T("breakfast (literally 'morning thing')", "朝食(「朝のもの」)"), "course I9, Practice Test; dictionary"),
    "-tu-": ("part", T("eat / drink (noun → verb)", "〜を食べる・飲む(名詞→動詞)"), "course I8, I11 (N→V list)"),
    "-guma-": ("part", T("want to", "〜したい"), "course I8, I9, I11"),
    "-giaKa-": ("part", T("have to", "〜しなければならない"), "course I8, I9, I11"),
    "-niat-": ("part", T("later today (form of -niak- before -tuk)", "今日このあと(-tuk の前の -niak- の形)"), "course I9 (SuliaKaniattuk)"),
    "-vunga": ("part", T("I (statement ending)", "私は(平叙の語尾)"), "course I8, I11"),
    "-tuk": ("part", T("he / she (ending after k-final suffixes)", "彼/彼女は(k で終わる接尾辞の後の語尾)"), "course I9"),
    "ainsik": ("word", T("one (clock numbers, from German 'eins')", "1(時刻の数詞。ドイツ語 eins から)"), "course II8; Wikipedia 'Inuttitut'"),
    "suvait": ("word", T("two (clock numbers, from German 'zwei')", "2(時刻の数詞。ドイツ語 zwei から)"), "course II8; Wikipedia 'Inuttitut'"),
    "tarait": ("word", T("three (clock numbers, from German 'drei')", "3(時刻の数詞。ドイツ語 drei から)"), "course II8; Wikipedia 'Inuttitut'"),
}

# ---------------------------------------------------------------- quests
QUESTS = [
    {"id": "q1", "title": T("Say hello", "あいさつをしよう"),
     "desc": T("Greet three people in the village and remember how to answer.", "村の3人にあいさつしよう。返事のしかたを思い出そう。"),
     "obj": [["greet_anansiak", T("Greet Grandma", "おばあちゃんにあいさつする"), "anansiak"],
             ["greet_hulda", T("Greet {{Hulda}}", "{{Hulda}} にあいさつする"), "hulda"],
             ["greet_tami", T("Greet {{Tâmi}} at the store", "お店の {{Tâmi}} にあいさつする"), "tami"]]},
    {"id": "q2", "title": T("Introductions", "自己紹介"),
     "desc": T("Talk with {{Hulda}} about where you are from, and learn verb and noun forms.", "{{Hulda}} と出身の話をしよう。動詞と名詞の形を教わろう。"),
     "obj": [["hulda_intro", T("Talk with {{Hulda}} about where you're from", "{{Hulda}} と出身について話す"), "hulda"],
             ["lesson:u2", T("Learn 'Introductions' from {{Hulda}}", "{{Hulda}} に「自己紹介」を教わる"), "hulda"],
             ["lesson:u3", T("Learn 'Verbs and persons' from {{Hulda}}", "{{Hulda}} に「動詞と人称」を教わる"), "hulda"],
             ["lesson:u4", T("Learn 'Nouns: one, two, many' from Grandma", "おばあちゃんに「名詞と数」を教わる"), "anansiak"]]},
    {"id": "q3", "title": T("Coffee at the store", "お店でコーヒーを"),
     "desc": T("Order a coffee at the store. Do you remember how many dogs were at Grandma's house?", "お店でコーヒーを頼もう。おばあちゃんの家の犬が何匹いたか、覚えているかな?"),
     "obj": [["tami_coffee", T("Ask {{Tâmi}} for a coffee", "{{Tâmi}} にコーヒーを頼む"), "tami"],
             ["tami_dogs", T("Tell {{Tâmi}} how many dogs you have", "{{Tâmi}} に犬の数を答える"), "tami"],
             ["lesson:u7", T("Learn 'Food and wanting' from {{Tâmi}}", "{{Tâmi}} に「食べ物と〜したい」を教わる"), "tami"],
             ["lesson:u6", T("Learn 'Family and possession' from Grandma", "おばあちゃんに「家族と持ち物」を教わる"), "anansiak"]]},
    {"id": "q4", "title": T("Counting stars", "星をかぞえる"), "unlocks": "east",
     "desc": T("Look at the night sky with {{Hulda}}. Learning to ask questions gets you news from outside the village.", "{{Hulda}} と夜空を見よう。質問のしかたを覚えると、村の外の情報が手に入る。"),
     "obj": [["hulda_stars", T("Talk with {{Hulda}} about the stars", "{{Hulda}} と星の数について話す"), "hulda"],
             ["lesson:u5", T("Learn 'Questions and negation' from {{Hulda}}", "{{Hulda}} に「質問と否定」を教わる"), "hulda"]]},
    {"id": "q5", "title": T("{{Rita}} at the shore", "海辺の {{Rita}}"), "unlocks": "north",
     "desc": T("Talk with {{Rita}} on the east shore (needs Speaking Lv2). Learning places and travel opens the road to the airstrip in the north.", "東の海辺で {{Rita}} と話そう(会話 Lv2 が必要)。場所と移動の言い方を覚えると、北の飛行場へ行ける。"),
     "obj": [["rita_talk", T("Talk with {{Rita}}", "{{Rita}} と話す"), "rita"],
             ["lesson:u9", T("Learn 'Places and travel' from {{Rita}}", "{{Rita}} に「場所と移動」を教わる"), "rita"]]},
    {"id": "q6", "title": T("Plane day", "飛行機の日"),
     "desc": T("At the northern airstrip, talk with {{Makusi}} about the weather and the time (needs Speaking Lv3).", "北の飛行場で {{Makusi}} と天気と時間の話をしよう(会話 Lv3 が必要)。"),
     "obj": [["makusi_weather", T("Talk with {{Makusi}} about the weather", "{{Makusi}} と天気の話をする"), "makusi"],
             ["makusi_time", T("Talk with {{Makusi}} about the plane's time", "{{Makusi}} と飛行機の時間の話をする"), "makusi"],
             ["lesson:u10", T("Learn 'Weather and a morning conversation' from {{Makusi}}", "{{Makusi}} に「天気と朝の会話」を教わる"), "makusi"],
             ["lesson:u8", T("Learn 'Time and tense' from {{Makusi}}", "{{Makusi}} に「時と時制」を教わる"), "makusi"]]},
    {"id": "q7", "title": T("Getting the language back", "ことばを取りもどす"),
     "desc": T("Learn the last A2 lessons from Grandma.", "おばあちゃんに、A2 の仕上げを教わろう。"),
     "obj": [["lesson:u11", T("Learn 'Can, may, must, try' from Grandma", "おばあちゃんに「できる・しなければ」を教わる"), "anansiak"],
             ["lesson:u12", T("Learn 'I see you: transitive endings' from Grandma", "おばあちゃんに「あなたを・私を」を教わる"), "anansiak"]]},
]

TEACH = {"hulda": [["u2", "q2"], ["u3", "q2"], ["u5", "q4"]],
         "anansiak": [["u1", "q1"], ["u4", "q2"], ["u6", "q3"], ["u11", "q7"], ["u12", "q7"]],
         "tami": [["u7", "q3"]], "rita": [["u9", "q5"]], "makusi": [["u10", "q6"], ["u8", "q6"]]}

# ---------------------------------------------------------------- dialogue
def say(inu, who, face=None):
    d = {"say": inu, "who": who}
    if face: d["face"] = face
    return d
def narr(en, ja): return {"narr": T(en, ja)}
def ok(inu, **kw): d = {"t": inu, "ok": 1}; d.update(kw); return d
def no(inu, en, ja): return {"t": inu, "hint": T(en, ja)}
def quiz(en, ja, opts, ans=0, skill="listen"): return {"quiz": T(en, ja), "opts": [T(a, b) for a, b in opts], "ans": ans, "skill": skill}

def greet3(who, first):
    return [
        say(first, who, "happy"),
        narr("They greeted you. Answer them.", "あいさつしてくれた。返事をしよう。"),
        {"choose": [ok(first), no("Atsunai!", "That's goodbye. Answer with the greeting for meeting someone.", "それは別れのあいさつ。会ったときのあいさつを返そう。"),
                    no("Auka.", "That means 'no'. Try answering with the same greeting.", "それは「いいえ」。相手と同じあいさつを返してみよう。")]},
        say("Kanuiven?", who),
        {"choose": [ok("Kanuingilanga."), no("Nakummek.", "That's 'thank you'. You're being asked how you are.", "それは「ありがとう」。調子を聞かれているよ。"),
                    no("Atsunai!", "Not goodbye yet — say 'I'm fine'.", "まだお別れじゃないよ。「元気です」と答えよう。")]},
        narr("Now ask them back.", "今度はこちらから聞き返してみよう。"),
        {"choose": [ok("Iffilittauk?"), no("Ilâli.", "That's 'welcome'. Ask 'and you?'", "それは「ようこそ」。「あなたは?」と聞き返そう。"),
                    no("Auka.", "Try asking 'and you?'", "「あなたは?」と聞き返してみよう。")]},
        say("Kanuingilanga.", who, "happy"),
    ]

SCRIPTS = {
    "intro": [
        narr("A snowy village. I'm standing in front of Grandma's ({{anânsiak}}'s) house.", "雪の村。ぼくはおばあちゃん({{anânsiak}})の家の前に立っていた。"),
        narr("When I was little I spoke this village's language, {{Inuttitut}}… but now I can't remember a thing.", "小さいころは、この村のことば {{Inuttitut}} を話していたはずなのに……今は何も思い出せない。"),
        narr("Talk with the people here and win the words back, little by little. Try talking to Grandma (walk up to her and press Space / Enter / the A button).",
             "村の人と話して、少しずつことばを取りもどそう。おばあちゃんに話しかけてみよう(近づいて Space / Enter / A ボタン)。"),
    ],
    "greet_anansiak": greet3("anansiak", "Ilitannamek!") + [
        narr("The words are slowly coming back. Go and greet the others in the village too ({{Hulda}}, and {{Tâmi}} at the store).", "少しずつ、ことばが戻ってくる気がする。村の人にもあいさつしてみよう({{Hulda}} と、お店の {{Tâmi}})。"),
        {"obj": "greet_anansiak"}],
    "greet_hulda": greet3("hulda", "Ilitannamek!") + [
        narr("{{Hulda}} seems to be a childhood friend — that was the greeting for someone you haven't seen in a long time.", "{{Hulda}} は子どものころの友達らしい。「久しぶり」のあいさつだった。"),
        {"obj": "greet_hulda"}],
    "greet_tami": [
        say("Ullâkut.", "tami", "happy"),
        narr("A morning greeting. Answer the same way.", "朝のあいさつだ。同じように返そう。"),
        {"choose": [ok("Ullâkut."), no("Atsunai!", "That's goodbye.", "それは別れのあいさつ。"),
                    no("Kanuivâ?", "That's 'how is he/she?'. First, greet him back.", "それは「彼/彼女は元気?」。まずはあいさつを返そう。")]},
        say("Kanuiven?", "tami"),
        {"choose": [ok("Kanuingilanga."), no("Auka.", "Say 'I'm fine'.", "「元気です」と答えよう。"), no("Ilâli.", "That's 'welcome'.", "それは「ようこそ」。")]},
        say("Ilâli.", "tami", "happy"),
        narr("He welcomed you to the store.", "「ようこそ」と迎えてくれた。"),
        {"obj": "greet_tami"}],
    "hulda_intro": [
        say("Nanimiunguven?", "hulda"),
        narr("She's asking where you're from. Where do you want to be from? (Your answer will come up again later.)", "出身を聞かれた。きみはどこの出身ということにする?(ここで答えた出身は、あとの会話でも使われる)"),
        {"choose": [ok("Nainimiunguvunga.", set={"home": "Nain"}), ok("Makkovimmiunguvunga.", set={"home": "Makkovik"}),
                    no("Atsunai!", "Say where you're from.", "出身地を答えよう。")]},
        say("Makkovimmiunguvunga.", "hulda", "happy"),
        quiz("Where is Hulda from?", "Hulda の出身は?", [("Makkovik", "Makkovik"), ("Nain", "Nain"), ("Hopedale", "Hopedale")]),
        say("Anânait nanimiungujong?", "hulda"),
        narr("She's asking about your mother, not Grandma. Your mother is from Nain.", "おばあちゃんではなく、お母さんのことを聞かれている。お母さんは Nain の出身だ。"),
        {"choose": [ok("Anânaga Nainimiungujuk."), no("Nanimiunguven?", "Don't ask back — say 'My mother is from Nain'.", "質問を返すのではなく、「私の母は Nain 出身です」と答えよう。"),
                    no("Pisuvunga.", "That means 'I'm walking'.", "それは「私は歩いている」。")]},
        narr("{{Hulda}} offers to teach you introductions and verb forms. (Talk to her again and choose 'Learn'.)", "{{Hulda}} が、自己紹介と動詞の形を教えてくれるという。({{Hulda}} に話しかけて「教わる」を選ぼう)"),
        {"obj": "hulda_intro"}],
    "baby": [
        narr("A baby is crying inside the house.", "家の中から赤ちゃんの泣き声が聞こえる。"),
        say("Nutagak Kiajuk.", "anansiak"),
        quiz("What did Grandma say?", "おばあちゃんは何と言った?", [("The baby is crying.", "赤ちゃんが泣いている"), ("The caribou is walking.", "カリブーが歩いている"), ("There are two dogs.", "犬が2匹いる")]),
        narr("Grandma offers to teach you about nouns and number.", "おばあちゃんが「名詞と数」を教えてくれるという。")],
    "tami_coffee": [
        narr("Ask whether there's any coffee.", "コーヒーがあるか聞いてみよう。"),
        {"choose": [ok("KâfiKavâ?"), no("Kanuivâ?", "That's 'how is he/she?'. Ask whether there's coffee ({{kâfi}}).", "それは「彼/彼女は元気?」。コーヒー({{kâfi}})があるか聞こう。"),
                    no("Anugivâ?", "That's 'is it windy?'.", "それは「風は吹いてる?」。")]},
        say("Â, kâfittugumaven?", "tami", "happy"),
        {"choose": [ok("Â, kâfittugumavunga."), no("Pisungilanga.", "That means 'I'm not walking'.", "それは「私は歩いていない」。"),
                    no("Auka.", "If you want coffee, say 'yes, I'd like some'.", "コーヒーを飲みたいなら「はい、飲みたい」と言おう。")]},
        say("Immumillu?", "tami"),
        {"choose": [ok("Â, immumik, sukarammilu."), no("Imikuluttugumavunga.", "That's 'I'd like a little water'. He's asking about milk.", "それは「お水を少し飲みたい」。ミルクのことを聞かれているよ。"),
                    no("Atsunai!", "Don't leave yet!", "まだ帰らないで。")]},
        narr("{{Tâmi}} makes you a coffee with milk and sugar. Say thank you.", "{{Tâmi}} が、ミルクと砂糖入りのコーヒーを入れてくれた。お礼を言おう。"),
        {"choose": [ok("Nakummek."), no("Ilâli.", "That's 'welcome'. How do you say thank you?", "それは「ようこそ」。お礼の言葉は?"), no("Auka.", "Say thank you.", "お礼を言おう。")]},
        say("Ilâli.", "tami", "happy"),
        {"obj": "tami_coffee"}],
    "tami_dogs": [
        say("Katsinik KimmiKaven?", "tami"),
        narr("He's asking about Grandma's dogs. How many were there?", "おばあちゃんの家の犬のことを聞かれているようだ。何匹いたかな?"),
        {"choose": [ok("Maggonik KimmiKavunga."), no("Pingasunnik paniKavunga.", "That's 'I have three daughters'. Answer with the number of dogs ({{Kimmik}}).", "それは「娘が3人います」。犬({{Kimmik}})の数を答えよう。"),
                    no("Sitamannik ullugiannik takuvunga.", "That's 'I see four stars'.", "それは「星が4つ見えます」。")]},
        narr("{{Tâmi}} laughs and gives you some dried fish ({{pitsik}}) for the dogs.", "{{Tâmi}} は笑って、犬のえさにと干し魚({{pitsik}})を分けてくれた。"),
        {"obj": "tami_dogs"}],
    "hulda_stars": [
        narr("Evening falls. You look up at the sky with {{Hulda}}.", "日が暮れて、{{Hulda}} と空を見上げた。"),
        {"pic": "stars4"},
        say("Katsinik ullugiannik takuven?", "hulda"),
        {"choose": [ok("Sitamannik ullugiannik takuvunga."), no("Maggonik KimmiKavunga.", "That's the number of dogs. Count the stars ({{ullugiak}}).", "それは犬の数。星({{ullugiak}})の数を答えよう。"),
                    no("Kongavise?", "That's 'are you (3+) angry?'.", "それは「あなたたちは怒っているの?」。")]},
        narr("{{Hulda}}: \"There's someone called {{Rita}} on the east shore. She takes her boat to lots of places.\" (She points east.)", "{{Hulda}}:「東の海辺に {{Rita}} という人がいるよ。舟でいろんな村へ行く人。」(身ぶりで東を指さした)"),
        narr("Once {{Hulda}} teaches you how to ask questions, the road east will open.", "質問のしかたを {{Hulda}} に教わったら、東の道が通れるようになる。"),
        {"obj": "hulda_stars"}],
    "rita_talk": [
        say("Ullusiakkut.", "rita", "happy"),
        {"choose": [ok("Ullusiakkut."), no("Atsunai!", "Answer with a greeting for meeting someone.", "会ったときのあいさつを返そう。"), no("Auka.", "Greet her back.", "あいさつを返そう。")]},
        say("Nanimiunguven?", "rita"),
        {"chooseHome": True},
        say("Umiannit tikitainnaKunga.", "rita"),
        quiz("Where has Rita just come from?", "Rita は今どこから来た?", [("From the boats, just now", "船から(たった今)"), ("From a plane, yesterday", "飛行機から(昨日)"), ("From home, tomorrow", "家から(明日)")]),
        say("Nunakkut Hulda tikilauttuk ippasak.", "rita"),
        quiz("When and how did Hulda arrive?", "Hulda はいつ、どうやって着いた?", [("Yesterday, over land", "昨日、陸路で"), ("Today, by plane", "今日、飛行機で"), ("Yesterday, by dog team", "昨日、犬ぞりで")]),
        say("Andrea tingijokkut aullaniattuk.", "rita"),
        quiz("What will Andrea do?", "Andrea はどうする?", [("Leave by plane later today", "今日このあと、飛行機で出発する"), ("Arrived by boat yesterday", "昨日、船で着いた"), ("Walk there tomorrow", "明日、歩いて行く")]),
        narr("So a plane leaves from the northern airstrip today. Learn places and travel from {{Rita}} and the road north will open too.", "北の飛行場から、今日飛行機が出るらしい。{{Rita}} に「場所と移動」を教われば、北の道も通れるようになる。"),
        {"obj": "rita_talk"}],
    "makusi_weather": [
        narr("A boy is looking up at the sky by the airstrip. It seems to be his first time on a plane.", "飛行場で、男の子が空を見上げている。初めての飛行機らしい。"),
        {"pic": "sunny"},
        say("Anugivâ?", "makusi", "puzzled"),
        narr("Look at the sky. No snow is blowing, and the flag isn't moving.", "空を見てみよう。雪も舞っていないし、旗も揺れていない。"),
        {"choose": [ok("Anugingilak."), no("Anugivâ?", "Don't repeat the question — answer it.", "質問をくり返すのではなく、答えよう。"), no("Kailiget!", "That's 'come here!'.", "それは「おいで!」。")]},
        say("Anugippat nangianiakKunga.", "makusi"),
        quiz("What is Makusi worried about?", "Makusi は何が心配?", [("Being scared if it gets windy", "風が吹いたら怖くなること"), ("Snow falling", "雪が降ること"), ("Forgetting breakfast", "朝ごはんを食べ忘れたこと")]),
        narr("Tell him the weather is good, to reassure him.", "天気がいいことを伝えて、安心させよう。"),
        {"choose": [ok("Â, silakKisuak."), no("Anugippat nangianiakKunga.", "That's what Makusi said. Tell him the weather is nice.", "それは Makusi の言ったこと。天気がいいと伝えよう。"),
                    no("Kongavise?", "That's 'are you (3+) angry?'.", "それは「あなたたちは怒っているの?」。")]},
        say("Ullusiangujuk.", "makusi", "happy"),
        {"obj": "makusi_weather"}],
    "makusi_time": [
        {"pic": "clock1030"},
        say("Tingijok senaliak affami tikiniattuk.", "makusi"),
        quiz("What time will the plane arrive?", "飛行機は何時に着く?", [("10:30", "10時半"), ("3:00", "3時"), ("12:00", "12時")]),
        say("Tingijok aullagiasijuk.", "makusi", "surprised"),
        quiz("What did Makusi say?", "Makusi は何と言った?", [("The plane is about to leave", "飛行機が出発しそうだ"), ("The plane has arrived", "飛行機が着いた"), ("The plane isn't coming", "飛行機は来ない")]),
        narr("{{Makusi}} offers to teach you how to talk about weather and time.", "{{Makusi}} が、天気と時間の言い方を教えてくれるという。"),
        {"obj": "makusi_time"}],
    "ending": [
        say("Inuttut ilinniagasuavugut.", "anansiak", "happy"),
        narr("\"We are trying to learn {{Inuttut}},\" Grandma says with a smile.", "「わたしたちは {{Inuttut}} を学ぼうとしているんだよ」——おばあちゃんはそう言って笑った。"),
        say("Takuvagit.", "anansiak", "happy"),
        narr("Greetings, questions, shopping, places, weather, time, 'I see you'. Living in the village, the words came back.", "あいさつ、質問、買い物、場所、天気、時間、「あなたを・私を」。村の暮らしの中で、ことばが戻ってきた。"),
        narr("That's the road to A2. You can keep reviewing at the camp and filling in the word book any time.", "これで A2 までの道のりはひと通り終わり。キャンプでの復習と図鑑の完成は、いつでも続けられる。")],
}

SMALLTALK = {
    "anansiak": [say("Kanuiven?", "anansiak"), {"choose": [ok("Kanuingilanga."), no("Atsunai!", "She's asking how you are.", "調子を聞かれているよ。")]}],
    "hulda": [say("Ilitannamek!", "hulda", "happy"), {"choose": [ok("Ilitannamek!"), no("Auka.", "Greet her back.", "あいさつを返そう。")]}],
    "tami": [say("Â, kâfittugumaven?", "tami", "happy"), {"choose": [ok("Â, kâfittugumavunga."), ok("Auka."), no("Atsunai!", "Say whether you'd like coffee.", "コーヒーを飲むかどうか答えよう。")]}],
    "rita": [say("Ullusiakkut.", "rita", "happy"), {"choose": [ok("Ullusiakkut."), no("Auka.", "Greet her back.", "あいさつを返そう。")]}],
    "makusi": [say("Â, silakKisuak.", "makusi", "happy"), narr("{{Makusi}} looks happily at the sky.", "{{Makusi}} はうれしそうに空を見ている。")],
}

# rita_talk's chooseHome expands to these three options
HOME_OPTIONS = [
    {"t": "Nainimiunguvunga.", "home": "Nain", "hint": T("Earlier you told Hulda you were from Makkovik.", "前に Hulda には Makkovik 出身だと答えたよね。")},
    {"t": "Makkovimmiunguvunga.", "home": "Makkovik", "hint": T("Earlier you told Hulda you were from Nain.", "前に Hulda には Nain 出身だと答えたよね。")},
    {"t": "Atsunai!", "home": None, "hint": T("Say where you're from.", "出身地を答えよう。")},
]

# ---------------------------------------------------------------- grammar drills  "stem|target|rest"
DRILLS = {
    "u3": ["Pisu|vunga|.", "Pisu|vutit|.", "Pisu|juk|.", "Pisu|vuguk|.", "Pisu|vutik|.", "Pisu|jok|.", "Pisu|vugut|.", "Pisu|vusi|.", "Pisu|jut|."],
    "u4": ["Nutagak Kia|juk|.", "Nutagâk Kia|jok|.", "Nutagait Kia|jut|.", "Tuttuk pisu|juk|.", "Tuttok pisu|jok|.", "Tuttuit pisu|jut|."],
    "u5": ["Pisu|ngilanga|.", "Pisu|ngilatit|.", "Pisu|ngituk|.", "Taku|ven|?", "Taku|jong|?", "Taku|vise|?"],
    "u6": ["Kimmi|kka|", "tingijo|tit|", "pitsi|ga|", "magga|ngit|", "aninni|nga|"],
    "u7": ["Â, kâfittu|guma|vunga.", "Tuttu|gasua|juk.", "Suli ullâsiutittu|giaKa|vutit."],
    "u8": ["Pisu|laukKunga|.", "Pisu|kKauvunga|.", "Pisu|tainnaKunga|.", "Pisu|likKunga|.", "Pisu|niakKunga|.", "Pisu|lâkKunga|."],
    "u9": ["Hebroni|mut| sinigiattuvunga.", "Marina tupim|mit| pisutainnatuk.", "Selma illu|mi| itsivajuk.", "Nuna|kkut| pisulaukKugut.", "Boris nanut|tut| pisuKattajuk."],
    "u11": ["Atuatsi|songu|vunga.", "Atuatsi|gunna|vunga.", "Uti|giaKa|juk.", "SuliaKa|giattu|juk.", "Inuttut ilinnia|gasua|vugut."],
    "u12": ["Taku|vagit|.", "Taku|vamma|.", "Taku|jaga|.", "Taku|jait|.", "Taku|janga|.", "Taku|vânga|.", "Taku|vâtit|."],
}

SIGNS = {"21,22": T("Store ({{Tâmi}}'s store)", "お店({{Tâmi}} のお店)"),
         "34,22": T("East → the shore (you can't pass while the snowdrift blocks the way)", "東 → 海辺(雪の吹きだまりでふさがっている時は通れない)"),
         "14,13": T("North → the airstrip", "北 → 飛行場"),
         "38,23": T("The shore. Boats come and go from here.", "海辺。舟が出入りする。"),
         "25,32": T("Camp. Review the words you've met by the campfire.", "キャンプ。たき火で、出会ったことばを復習できる。")}
DOORS = {"5,18": T("Grandma's ({{anânsiak}}'s) house. It's warm inside.", "おばあちゃん({{anânsiak}})の家。中は暖かい。"),
         "19,16": T("{{Hulda}}'s house. The windows are lit.", "{{Hulda}} の家。窓に明かりがともっている。"),
         "29,17": T("A neighbour's house.", "近所の家。"), "6,31": T("A neighbour's house.", "近所の家。"),
         "14,33": T("A neighbour's house.", "近所の家。"), "30,36": T("A neighbour's house.", "近所の家。")}

# ---------------------------------------------------------------- "What is Inuttitut?" page
ABOUT_SOURCES = [
    ("EOA", "Eilís Quinn, 'Inuttitut language revitalization campaign underway in Labrador Inuit region', Eye on the Arctic (Radio Canada International), 1 May 2023",
     "https://www.rcinet.ca/eye-on-the-arctic/2023/05/01/inuttitut-language-revitalization-campaign-underway-in-labrador-inuit-region/"),
    ("WPI", "Wikipedia, 'Inuttitut'", "https://en.wikipedia.org/wiki/Inuttitut"),
    ("WPL", "Wikipedia, 'Inuit languages'", "https://en.wikipedia.org/wiki/Inuit_languages"),
    ("WPK", "Wikipedia, 'Inuktitut'", "https://en.wikipedia.org/wiki/Inuktitut"),
    ("NG", "Nunatsiavut Government, Language resources", "https://nunatsiavut.com/language-resources/"),
    ("TU", "Tusâlanga (Nunatsiavummiutut) — Nunatsiavut Government & Pirurvik Centre", "https://nunatsiavut.tusaalanga.ca/"),
    ("JO", "Alana Johns (1999), 'The Decline of Ergativity in Labrador Inuttut', MIT Occasional Papers in Linguistics 17", "https://ajohns.artsci.utoronto.ca/inuit/alana/publications.html"),
    ("C", "INUTTITUT I / II course handouts (2025)", ""),
]

ABOUT = [
    {"h": T("Who speaks it, and where?", "誰が、どこで話しているの?"),
     "p": [T("{{Inuttitut}} (also called {{Inuttut}} or {{Nunatsiavummiutut}}) is the Inuit language of Labrador, on Canada's Atlantic coast. It is spoken by Labrador Inuit in {{Nunatsiavut}}, the Inuit region of Newfoundland and Labrador. [WPI]",
             "{{Inuttitut}}({{Inuttut}}、{{Nunatsiavummiutut}} とも)は、カナダ大西洋岸・ラブラドールのイヌイット語です。ニューファンドランド・ラブラドール州のイヌイット地域 {{Nunatsiavut}} で、ラブラドール・イヌイットの人々が話しています。[WPI]"),
           T("About 2,560 people live in Nunatsiavut, in five coastal communities — Nain, Hopedale, Makkovik, Postville and Rigolet — and about 4,500 more beneficiaries live elsewhere. [EOA]",
             "Nunatsiavut の人口は約 2,560 人で、海沿いの5つの集落 Nain、Hopedale、Makkovik、Postville、Rigolet に住んでいます。このほか約 4,500 人の受益者(Nunatsiavut の協定上の構成員)が地域の外で暮らしています。[EOA]")]},
    {"h": T("How is the language doing today?", "今、このことばはどんな状況?"),
     "p": [T("Inuttitut is endangered. UNESCO's Atlas of the World's Languages in Danger lists it as 'definitely endangered'. [WPI] In the 2021 Census, only 5.4% of children under 14 and 27.5% of adults aged 65 spoke it — the most endangered Inuit language variety in Canada. [EOA, citing Statistics Canada]",
             "Inuttitut は消滅の危機にあります。ユネスコの『消滅の危機にある世界の言語地図』では「確実に危険(definitely endangered)」に分類されています。[WPI] 2021 年の国勢調査では、14 歳以下の子どもの 5.4%、65 歳の大人の 27.5% しか話しておらず、カナダのイヌイット語の中で最も危機的な状況です。[EOA(カナダ統計局の数字を引用)]"),
           T("Labrador Inuit are bringing it back. The Nunatsiavut Government held a language summit in 2019, adopted a 2021–2026 Language Strategy, ran the first Inuttitut Blitz in 2023, and added an Inuttitut module to the Tusâlanga learning website. [EOA, TU]",
             "ラブラドール・イヌイットの人々は、ことばを取りもどす活動を進めています。Nunatsiavut 政府は 2019 年に言語サミットを開き、2021〜2026 年の言語戦略を定め、2023 年に初の「Inuttitut Blitz」を行い、学習サイト Tusâlanga に Inuttitut のコースを加えました。[EOA, TU]"),
           T("This game is a small study aid. It is not a substitute for learning from speakers.", "このゲームは小さな学習の手助けです。話者から学ぶことの代わりにはなりません。")]},
    {"h": T("What is it related to?", "どんな言語の仲間?"),
     "p": [T("Inuttitut is one dialect of the Inuit language. Inuit dialects form a chain from Alaska across Arctic Canada to Greenland: neighbouring dialects understand each other, and understanding drops with distance. [WPL]",
             "Inuttitut はイヌイット語の方言のひとつです。イヌイット語の方言は、アラスカからカナダ北極圏を通ってグリーンランドまで鎖のようにつながっていて、となり合う方言どうしは通じ合い、離れるほど通じにくくなります。[WPL]"),
           T("In Canada it belongs to the eastern group, with the Inuktitut of Nunavut and Nunavik, but it has its own sound changes, word forms and grammar. [WPI, WPL] That's why this game uses only Labrador sources.",
             "カナダでは東部のグループに属し、Nunavut や Nunavik の Inuktitut の仲間ですが、音の変化・語形・文法に独自の特徴があります。[WPI, WPL] そのため、このゲームはラブラドールの資料だけを使っています。"),
           T("The Inuit languages are closely related to the Yupik languages of Alaska and Siberia, and more distantly to Aleut; together they form the Eskimo–Aleut (Eskaleut) family. [WPL] They are not related to English or French.",
             "イヌイット語は、アラスカやシベリアのユピック諸語ととても近く、アレウト語とはより遠い親戚で、まとめてエスキモー・アレウト語族(Eskaleut)と呼ばれます。[WPL] 英語やフランス語とは系統的なつながりはありません。")]},
    {"h": T("What is it like?", "どんな感じのことば?"),
     "p": [T("Long words built from parts. Every word starts with a root, and suffixes are added one after another. [WPK] One word can say what English needs a whole sentence for:",
             "部品をつないで長い単語を作ります。単語は必ず語根から始まり、そこに接尾辞を次々につけていきます。[WPK] 英語なら1文になる内容を、1語で言えます(日本語の「食べ・させ・たい」のように後ろに足していきますが、名詞まで動詞に変えて、さらに長くつなげます):")],
     "breakdowns": [
         {"word": "Â, kâfittugumavunga.", "parts": ["kâfi", "-tu-", "-guma-", "-vunga"], "src": "C"},
         {"word": "UllâsiutittugiaKaniattuk.", "parts": ["ullâsiutik", "-tu-", "-giaKa-", "-niat-", "-tuk"], "src": "C"}],
     "examples": [
         (T("Endings tell you who — no separate word for 'I' or 'you' is needed:", "語尾が「誰が」を表すので、「私」「あなた」という単語はふつう要りません:"), ["Pisuvunga.", "Pisuvutit.", "Pisujuk."]),
         (T("Two is different from three or more (singular, dual, plural):", "「2つ」と「3つ以上」を区別します(単数・双数・複数):"), ["Nutagak Kiajuk.", "Nutagâk Kiajok.", "Nutagait Kiajut."]),
         (T("One ending can say both who does it and to whom:", "1つの語尾で「誰が」と「誰を」を同時に表せます:"), ["Takuvagit.", "Takuvamma."])],
     "p2": [T("Sounds: there are three vowels, a, i and u, each short or long. In Labrador spelling the long vowels are written â, e and o (e = ii, o = uu). Capital K inside a word is a different sound from k: it is made further back in the throat. [C, WPI]",
              "音: 母音は a・i・u の3つで、それぞれ短い音と長い音があります。ラブラドールの綴りでは長い母音を â・e・o と書きます(e = ii、o = uu)。単語の中の大文字 K は小文字 k とは別の音で、のどのもっと奥で出します。[C, WPI]"),
            T("Writing: Labrador uses a Latin alphabet that goes back to German-speaking Moravian missionaries; a standard writing system was agreed with elders and educators in 1980. Nunavut and Nunavik mostly write Inuktitut in syllabics instead. [WPI, WPL]",
              "文字: ラブラドールでは、ドイツ語を話すモラヴィア派宣教師にさかのぼるラテン文字を使います。1980 年に長老や教育者と共に標準の書き方が決められました。Nunavut や Nunavik では主に音節文字で書きます。[WPI, WPL]"),
            T("Borrowed words: some words came from German through the Moravians — for example the numbers used for telling time, {{ainsik}}, {{suvait}}, {{tarait}} (1, 2, 3). [WPI, C]",
              "借用語: モラヴィア派を通してドイツ語から入った単語もあります。たとえば時刻に使う数 {{ainsik}}、{{suvait}}、{{tarait}}(1、2、3)です。[WPI, C]"),
            T("Grammar note for the curious: like other Inuit varieties, Labrador Inuttut marks the doer of a transitive verb differently from other subjects (ergativity); linguists have studied how this system has changed in Labrador. [JO]",
              "興味のある人へ: ほかのイヌイット語と同じく、他動詞の主語(動作をする人)を自動詞の主語とは違う形で表す「能格性」という性質があり、ラブラドールではその仕組みが変化してきたことが研究されています。[JO]")]},
]


# ---------------------------------------------------------------- validation & export
def all_text_fields(obj):
    if isinstance(obj, dict):
        if set(obj.keys()) == {"en", "ja"}:
            yield obj["en"]; yield obj["ja"]
        else:
            for v in obj.values():
                yield from all_text_fields(v)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from all_text_fields(v)


def validate(bank_inu):
    errs = []
    def need(inu, where):
        if inu not in bank_inu:
            errs.append(f"{where}: not in example bank: {inu}")
    for k, steps in list(SCRIPTS.items()) + [("smalltalk:" + n, s) for n, s in SMALLTALK.items()]:
        for st in steps:
            if "say" in st: need(st["say"], k)
            for c in st.get("choose", []): need(c["t"], k)
    for o in HOME_OPTIONS: need(o["t"], "home options")
    for u, ds in DRILLS.items():
        for d in ds:
            p = d.split("|")
            if len(p) != 3: errs.append(f"bad drill {d}")
            need("".join(p), "drill " + u)
    for sec in ABOUT:
        for b in sec.get("breakdowns", []):
            need(b["word"], "about")
            for part in b["parts"]:
                if part not in GLOSSARY: errs.append(f"about part not in glossary: {part}")
        for _, words in sec.get("examples", []):
            for w in words: need(w, "about")
    texts = list(all_text_fields([QUESTS, SCRIPTS, SMALLTALK, HOME_OPTIONS, SIGNS, DOORS, ABOUT, NPC_NAMES]))
    for t in texts:
        for m in re.findall(r"\{\{(.+?)\}\}", t):
            if m not in GLOSSARY and m not in bank_inu:
                errs.append(f"marked word not in glossary/bank: {m}")
    return errs


def export():
    return {"npcNames": NPC_NAMES, "quests": QUESTS, "teach": TEACH, "scripts": SCRIPTS, "smalltalk": SMALLTALK,
            "homeOptions": HOME_OPTIONS, "drills": DRILLS, "signs": SIGNS, "doors": DOORS,
            "glossary": {k: {"kind": v[0], "mean": v[1], "src": v[2]} for k, v in GLOSSARY.items()},
            "about": ABOUT, "aboutSources": [{"id": a, "text": b, "url": c} for a, b, c in ABOUT_SOURCES]}
