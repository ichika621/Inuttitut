# -*- coding: utf-8 -*-
"""English edition of the explanatory text in a2_bank.py (unit titles, can-do statements,
grammar points, item notes). The Inuttitut examples themselves are shared — only the
explanations are translated here."""

KIND_EN = {"P": "printed in the course handouts", "T": "course paradigm table", "R": "built from course forms + rules", "W": "web source"}
KIND_SHORT_EN = {"P": "Course: text", "T": "Course: table", "R": "Course rules", "W": "Web"}

UNIT_EN = {
    "u1": {"title": "Ilitannamek! — Greetings",
           "cando": "Greet people, ask how they are and answer; say yes and no.",
           "grammar": [
               ("Learn these as set phrases", "Ilitannamek! (hello, to someone you haven't seen for a while) and Atsunai! (goodbye) are fixed expressions. Kanuiven? (how are you?) is the verb Kanui- plus the 2nd-person singular question ending -ven?."),
               ("'I'm fine' is a negative form", "Kanuingilanga uses the negative ending -ngilanga (1st person singular): literally 'I'm not (unwell)'."),
               ("'And you?'", "Iffilittauk? turns the question back to the other person (-littauk = 'what about…')."),
           ]},
    "u2": {"title": "Nanimiunguven? — Introductions",
           "cando": "Introduce people, ask where someone is from and answer.",
           "grammar": [
               ("Introducing: Una …", "Una ('this one / this person') + a name or noun = 'This is …'. Una ilannâga Hulda. (This is my friend Hulda.)"),
               ("Origin: place + -miuk + -u- + ending", "-miuk = 'person from', -u- = 'to be'. Nain → Nainimiunguvunga (I'm from Nain). As a question, end in -ven?: Nanimiunguven? (Where are you from?)."),
               ("Third person", "Swap the ending for -juk / -jong? to talk about someone else: Anânait nanimiungujong? (Where is your mother from?)"),
           ]},
    "u3": {"title": "Pisuvunga — Verbs and persons",
           "cando": "Say 'I / you / he or she is doing …', and tell two people (dual) from three or more (plural).",
           "grammar": [
               ("Verb = root + person ending", "Drop the root's final k and add the ending: pisuk- (walk) → pisuvunga (I'm walking)."),
               ("Person endings (course handouts I8, I11)", "1st person: -vunga (I) / -vuguk (we two) / -vugut (we, 3+). 2nd person: -vutit / -vutik / -vusi. 3rd person: -juk / -jok / -jut."),
               ("No pronoun needed", "The ending already says who is doing it, so the verb alone means 'I walk', 'you walk', etc."),
           ]},
    "u4": {"title": "Tuttuk pisujuk — Nouns: one, two, many",
           "cando": "Use singular, dual (two) and plural (three or more) nouns, and make the verb agree.",
           "grammar": [
               ("Noun number (course handouts I2, II1)", "Singular -Ø (nutagak); dual lengthens the final vowel, -V (nutagâk); plural -it (nutagait)."),
               ("Subject–verb agreement", "The subject noun takes no ending; the verb ending matches its number: Tuttuk pisujuk / Tuttok pisujok / Tuttuit pisujut."),
           ]},
    "u5": {"title": "Sunamik takuven? — Questions and negation",
           "cando": "Ask yes/no questions and 'what?', 'how many?', 'where to?' questions, and answer in the negative.",
           "grammar": [
               ("Question endings (course handouts I8, I11)", "1st person: -vingâ? / -vinong? / -vitâ?; 2nd person: -ven? / -viteng? / -vise?; 3rd person: -jong? / -joung? / -jon?"),
               ("Negative endings", "Use -ngila- / -ngitu- instead of -vu- / -ju-: -ngilanga / -ngilatit / -ngituk (dual and plural forms are in the table). In conversation the 3rd person also appears as -ngilak (Anugingilak)."),
               ("Question words", "Sunamik …? (what), Katsinik …? (how many), Namut …? (where to), Nautaima …? (where). A noun asked about takes -mik / -nik."),
           ]},
    "u6": {"title": "PaniKavunga — Family and possession",
           "cando": "Talk about family and belongings with 'my / your / her', and say 'I have …' and how many.",
           "grammar": [
               ("Possessive endings (course handouts I8, I11)", "My: -ga (one) / -Vkka (two) / -kka (three or more). Your: -it / -Vkkik / -tit. His/her: -nga / -Vgik / -ngit."),
               ("'To have' = noun + -Ka-", "PaniKavunga. (I have a daughter.) Put the number first with -mik / -nik: Atautsimik / Maggonik / Pingasunnik paniKavunga."),
               ("'Of' = -up", "The owner takes -up and the thing owned takes -nga: Marinaup umianga (Marina's boat). Two owners: -V; three or more: -it (annâk Kimminga / annait Kimminga)."),
           ]},
    "u7": {"title": "Kâfittugumaven? — Food and wanting",
           "cando": "Offer food and drink, say what you want, and say what you ate or have to eat.",
           "grammar": [
               ("Noun + -tu- = eat / drink it", "kâfi (coffee) → kâfittu- (drink coffee); tuttuvinik (caribou meat) → tuttuvinittu-."),
               ("-guma- = want to", "It goes between the root and the person ending: kâfittugumavunga (I'd like some coffee)."),
               ("-gasua- (try to) and -giaKa- (have to)", "Puijivinittugasuaven? (Will you try seal meat?) / Suli ullâsiutittugiaKavutit. (You still have to eat breakfast.)"),
               ("-lu = too / and", "Attached to the following word: Immumillu? (Milk, too?)"),
           ]},
    "u8": {"title": "SuliaKalâttuk — Time and tense",
           "cando": "Talk about yesterday, earlier today, later today and tomorrow with the right tense; tell the time.",
           "grammar": [
               ("Tense suffixes (course handout I9)", "-lauk- (before today), -kKau- (earlier today), -tainnak- (just now), -lik- (right now), -giasi- (about to), -niak- (later today), -langa- (later today, Hebron dialect), -lâk- (tomorrow or later)."),
               ("After a suffix ending in k", "1st person -vunga becomes -Kunga and 3rd person -juk becomes -ttuk / -tuk: pisulaukKunga / pisulauttuk."),
               ("Telling the time", "Clock times use the German-origin numbers (ainsik, suvait, tarait …). 'It is … o'clock' = number + -vuk. 'At half past ten' = senaliak affami."),
           ]},
    "u9": {"title": "Namut appaliven? — Places and travel",
           "cando": "Say where to, where from, where, and by what means; talk about trips you made or will make.",
           "grammar": [
               ("Place endings (course handout II1)", "-mi (in / at), -mut (to), -mit (from), -kkut (through / by means of), -tigut (across), -tut (like). For two: -Vni / -Vnut / -Vnit; for three or more: -ni / -nut / -nit."),
               ("Place + -lia- = go to", "Hopedaliliavunga. (I'm going to Hopedale.) Nainiliavuguk. (We two are going to Nain.)"),
               ("-giattu- = go somewhere to do", "Hebronimut sinigiattuvunga. (I'm going to Hebron to sleep.)"),
           ]},
    "u10": {"title": "SilakKivâ? — Weather and a morning conversation",
            "cando": "Ask about and describe the weather, use 'if …', and give commands.",
            "grammar": [
                ("Weather is a verb", "Anugivâ? (Is it windy?) / Anugingilak. (It isn't windy.) Weather verbs are used in the 3rd person."),
                ("'If …' = -ppat", "The 3rd-person singular 'if' ending when the subject differs from the main clause: Anugippat nangianiakKunga. (If it's windy, I'll be afraid.)"),
                ("Commands (course handouts I8, I11)", "To one person -git / -ligit / -laugit (written -get / -liget / -lauget in I11), to two -gittek …, to three or more -gitsi …: Tupaliget! (Wake up!)"),
            ]},
    "u11": {"title": "Atuatsisonguvunga — Can, may, must, try",
            "cando": "Say what you can do, are allowed to do, have to do, and are trying to do.",
            "grammar": [
                ("Verb-to-verb suffixes (course handouts I9, I11)", "-songu- (can), -gunna- (may / be allowed), -giaKa- (have to), -giattu- (go to do), -gasua- (try to), -titsi- (make someone do), -jutsau- (should be), -galâ- (a little), -kasâ- (almost), -gajak- (could), -galuak- (although), -Kattak- (habitually), -guma- (want to)."),
                ("Objects: -mik / -nik", "One thing takes -mik, two -Vnik, three or more -nik: Kanimajunnik paitsiKauvutit. (You took care of sick people.)"),
            ]},
    "u12": {"title": "Takuvagit — 'I see you': transitive endings",
            "cando": "Say 'I … you', 'you … me', 'she … him' in a single word.",
            "grammar": [
                ("Transitive endings (course handout II3)", "One ending marks both who does it and to whom. With takuk- (see): takuvagit (I → you), takuvamma (you → me), takujaga (I → him/her), takujait (you → him/her), takujanga (he/she → him/her), takuvânga (he/she → me), takuvâtit (he/she → you)."),
                ("Transitive questions (II3)", "takuvammâ? (do you see me?), takujân? (do you see him/her?), takujagâ? (do I see him/her?)"),
            ]},
}

NOTE_EN = {
    "辞書の語釈: Greeting of old friends; nice to see you again!": "Dictionary gloss: 'Greeting of old friends; nice to see you again!'",
    "否定語尾 -ngilanga の形": "Uses the negative ending -ngilanga.",
    "練習テストの問いへの答え。根拠: anânak + 所有語尾 -ga(I8・I11の表)、Nainimiunguvunga(I2)の語尾を3人称 -juk(I11の表)に替えた形":
        "Answer to a Practice Test question. Basis: anânak + possessive -ga (tables in I8, I11); Nainimiunguvunga (I2) with the 3rd-person ending -juk (I11 table).",
    "授業資料の手書きメモにある文。根拠: pisuvunga(I2の表)、mânna = now(辞書)": "From a handwritten note on the handout. Basis: pisuvunga (I2 table); mânna = 'now' (dictionary).",
    "練習テストの問いへの答え。根拠: sitamannik(I8)、ullugiannik(PT)、takuvunga(II3の表)": "Answer to a Practice Test question. Basis: sitamannik (I8), ullugiannik (Practice Test), takuvunga (II3 table).",
    "練習テストの問題 'Aunâ__? Am I bleeding?' に 1人称疑問語尾 -vingâ?(I11)を入れた形": "Practice Test item 'Aunâ__? Am I bleeding?' completed with the 1st-person question ending -vingâ? (I11).",
    "練習テストの問題 'kamennik pisi__?' に 3人称疑問語尾 -jong?(I11)を入れた形": "Practice Test item 'kamennik pisi__?' completed with the 3rd-person question ending -jong? (I11).",
    "練習テストの問題 'Konga__?' に 2人称複数の疑問語尾 -vise?(I11)を入れた形": "Practice Test item 'Konga__?' completed with the 2nd-person plural question ending -vise? (I11).",
    "根拠: 疑問詞 nautaima...?(I11)、niaKuk + 2人称所有 -it(I11の表。illuk → illuit と同じ規則)": "Basis: question word nautaima…? (I11); niaKuk + 2nd-person possessive -it (I11 table; same rule as illuk → illuit).",
    "根拠: niaKuk + 1人称所有 -ga(I11の表。illuk → illuga と同じ規則)": "Basis: niaKuk + 1st-person possessive -ga (I11 table; same rule as illuk → illuga).",
    "根拠: Maggonik paniKavunga(I8)の panik を Kimmik(II1)に替えた形": "Basis: Maggonik paniKavunga (I8) with panik replaced by Kimmik (II1).",
    "練習テストの問題 'Kimmi__ (my dogs)' に -kka(I8の表)を入れた形": "Practice Test item 'Kimmi__ (my dogs)' completed with -kka (I8 table).",
    "練習テストの問題 'tingijo__ (your planes)' に -tit(I8の表。panik → panitit と同じ規則)を入れた形": "Practice Test item 'tingijo__ (your planes)' completed with -tit (I8 table; same rule as panik → panitit).",
    "練習テストの問題 'pitsi__ (my pitsik)' に -ga を入れた形。pitsik = dried fish(辞書)": "Practice Test item 'pitsi__ (my pitsik)' completed with -ga. pitsik = dried fish (dictionary).",
    "練習テストの問題 'magga__ (his dishes)' に -ngit を入れた形": "Practice Test item 'magga__ (his dishes)' completed with -ngit.",
    "練習テストの問題 'aninni__ (her life)' に -nga を入れた形": "Practice Test item 'aninni__ (her life)' completed with -nga.",
    "練習テストの問いへの答え。根拠: 問いと同じ語幹に1人称 -vunga(I11の表)": "Answer to a Practice Test question. Basis: the same stem as the question with 1st-person -vunga (I11 table).",
    "練習テストの問題 'Ullâsiutittu__niattuk (Johnny will have to eat breakfast)' に -giaKa-(I9)を入れた形": "Practice Test item 'Ullâsiutittu__niattuk (Johnny will have to eat breakfast)' completed with -giaKa- (I9).",
    "練習テストの問題 'Ippasak tuttuvinittulauk__?' の答え。-lauk- の後の2人称疑問は -Ken?(Tusâlanga L3 の sulaukKen? と同じ形)": "Answer to Practice Test item 'Ippasak tuttuvinittulauk__?'. After -lauk- the 2nd-person question ending is -Ken? (same as sulaukKen? in Tusâlanga lesson 3).",
    "根拠: tarait(3、II8の数詞表)+ -vuk(〜時です。Tusâlanga 'Telling Time' の ainsivuk・suvaivuk と同じ作り方)": "Basis: tarait (3, number list in II8) + -vuk ('it is … o'clock'; formed like ainsivuk / suvaivuk in Tusâlanga 'Telling Time').",
    "練習テストの英文 'I (just) arrived from Nain.' の訳。根拠: Nainimut(I9)の -mut を -mit(II1)に替え、TikitainnaKunga(I9)": "Translation of the Practice Test sentence 'I (just) arrived from Nain.' Basis: Nainimut (I9) with -mut changed to -mit (II1), plus TikitainnaKunga (I9).",
    "niugguk = visit another settlement(辞書)": "niugguk = visit another settlement (dictionary).",
    "nangiak = afraid of falling(辞書)": "nangiak = afraid of falling (dictionary).",
    "練習テストの問題 'Atuagammik alla__juk (She wants to write a novel)' に -guma-(I9)を入れた形": "Practice Test item 'Atuagammik alla__juk (She wants to write a novel)' completed with -guma- (I9).",
    "練習テストの英文の訳。根拠: tusâk-(I11の動詞リスト)、目的語 -mik(II1)、3人称複数 -jut(I11)、ilinniatitsijik = teacher(辞書。I9の Ilinniatitsijuk から)":
        "Translation of a Practice Test sentence. Basis: tusâk- (I11 verb list), object -mik (II1), 3rd-person plural -jut (I11), ilinniatitsijik = teacher (dictionary; cf. Ilinniatitsijuk in I9).",
    "napâttuk = tree(辞書)。-ni = 3つ以上の場所「〜で」": "napâttuk = tree (dictionary). -ni = 'in / at' with three or more.",
    "suangak = scold(辞書)、-jau- = 〜される": "suangak = scold (dictionary); -jau- = passive ('be …-ed').",
    "授業資料 I11 の語彙一覧。意味は辞書で確認": "From the vocabulary list in handout I11; meanings checked in the dictionary.",
}

VOCAB_NOTE_JA = "授業資料 I11 の語彙一覧。意味は辞書で確認"
