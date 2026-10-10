# -*- coding: utf-8 -*-
"""Build the submission document (Inuttitut A2 例文集) from scripts/a2_bank.py.
Usage: python scripts/build_a2_doc.py [out.docx]   (needs: pip install python-docx)"""
import sys, collections
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import a2_bank as B

doc = Document()
sec = doc.sections[0]
sec.top_margin = sec.bottom_margin = Cm(1.8)
sec.left_margin = sec.right_margin = Cm(1.9)
st = doc.styles["Normal"]
st.font.name = "Calibri"; st.font.size = Pt(10.5)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Yu Gothic")
for name in ("Title", "Heading 1", "Heading 2", "Heading 3"):
    doc.styles[name].element.rPr.rFonts.set(qn("w:eastAsia"), "Yu Gothic")

NAVY = "1F3A5F"; AMBER = (0x9A, 0x5B, 0x13); GREY = (0x55, 0x55, 0x55)
KIND_SHORT = {"P": "授業・原文", "T": "授業・表", "R": "授業の規則", "W": "ネット"}
KIND_FILL = {"P": "E8F0E3", "T": "E3ECF5", "R": "F6EEDC", "W": "F3E3E3"}
SRC_SHORT = {k: v.split(" — ")[0] for k, v in B.SRC.items()}


def shade(cell, hex_):
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hex_)
    cell._tc.get_or_add_tcPr().append(shd)


def p(text="", bold=False, italic=False, size=None, color=None, after=4, align=None):
    para = doc.add_paragraph()
    r = para.add_run(text); r.bold = bold; r.italic = italic
    if size: r.font.size = Pt(size)
    if color: r.font.color.rgb = RGBColor(*color)
    para.paragraph_format.space_after = Pt(after)
    if align: para.alignment = align
    return para


def bullet(text, size=10):
    para = doc.add_paragraph(style="List Bullet")
    r = para.add_run(text); r.font.size = Pt(size)
    para.paragraph_format.space_after = Pt(1)


def table(headers, rows, widths, size=9, fill=NAVY, row_fills=None, italic_cols=()):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = "Table Grid"; t.autofit = False
    for i, (h, w) in enumerate(zip(headers, widths)):
        c = t.rows[0].cells[i]; c.width = Cm(w); c.text = ""
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = RGBColor(255, 255, 255)
        shade(c, fill); c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for i, (v, w) in enumerate(zip(row, widths)):
            cells[i].width = Cm(w); cells[i].text = ""
            r = cells[i].paragraphs[0].add_run(str(v)); r.font.size = Pt(size)
            if i in italic_cols: r.bold = True
            if row_fills and row_fills[ri]: shade(cells[i], row_fills[ri])
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def toc():
    para = doc.add_paragraph(); r = para.add_run()._r
    els = []
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin"); els.append(b)
    ins = OxmlElement("w:instrText"); ins.set(qn("xml:space"), "preserve"); ins.text = 'TOC \\o "1-2" \\h \\z \\u'; els.append(ins)
    sp = OxmlElement("w:fldChar"); sp.set(qn("w:fldCharType"), "separate"); els.append(sp)
    tx = OxmlElement("w:t"); tx.text = "(目次: Word で開いて右クリック →「フィールドの更新」で表示されます)"; els.append(tx)
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end"); els.append(e)
    for el in els: r.append(el)


items = list(B.all_items())
cnt = collections.Counter(x["kind"] for x in items)

# ------------------------------------------------------------ 表紙
doc.add_heading("Inuttitut(ラブラドール方言)A2 学習例文集", level=0)
p("Nunatsiavummiutut / Labrador Inuttitut — A1 から A2 までの段階別例文と文法", italic=True, size=11, color=GREY, after=10)
table(["項目", "内容"], [
    ["対象言語", "Inuttitut(Inuttut、Nunatsiavummiutut)。カナダ・ラブラドール北部 Nunatsiavut のイヌイット語。綴りは1980年標準化のラテン文字表記(â=aa, e=ii, o=uu, K=口蓋垂音)。"],
    ["目標", "CEFR A2(身近な話題について、短い文でやり取りができる)"],
    ["構成", f"12 ユニット・{len(items)} 例文。各ユニットに Can-do、文法のポイント、例文(Inuttitut・英語・日本語・出典)を載せる。"],
    ["例文の出典", f"授業資料の原文 {cnt['P']} / 授業資料の活用表 {cnt['T']} / 授業資料の形と規則から作成 {cnt['R']} / ネット資料 {cnt['W']}"],
    ["主な資料", "INUTTITUT I・II 授業資料(Katimanik #1〜#11、2025-09〜11)、Practice Test(2025-11-13)、Nunatsiavut Government の言語ページ、Tusâlanga(Nunatsiavummiutut 版)、Labrador Virtual Museum English-Inuttut Dictionary"],
], [3.2, 14.2], size=9.5)
doc.add_heading("目次", level=1)
toc()
doc.add_page_break()

# ------------------------------------------------------------ 1. 出典と信頼度
doc.add_heading("1. 出典と信頼度", level=1)
p("この例文集では、授業資料を最も確かな出典とし、その次にラブラドール方言と確認できるネット資料を使った。標準 Inuktitut(Nunavut など)の資料は、語尾の形がラブラドール方言と違うため使っていない(例: 「私は見る」は標準では takujunga、授業資料では takuvunga)。", after=6)
table(["表示", "意味", "確かさ"], [
    ["授業・原文", "授業資料に印刷された文・語句をそのまま転記したもの", "最も確か"],
    ["授業・表", "授業資料の活用表に印刷された語形をそのまま転記したもの", "最も確か"],
    ["授業の規則", "授業資料に印刷された語形と規則(語尾の表)だけで組み立てた文。練習テストの問いへの答えなど。根拠を各ユニットの注に書いた", "確か(規則の当てはめ)"],
    ["ネット", "ネット上のラブラドール方言資料。URL を明記", "公式資料。授業資料と矛盾しないものだけを採用"],
], [3.0, 10.6, 3.8], size=9,
    row_fills=[KIND_FILL["P"], KIND_FILL["T"], KIND_FILL["R"], KIND_FILL["W"]])
p("出典の略号", bold=True, after=2)
table(["略号", "出典"], [[k, v] for k, v in B.SRC.items()], [1.6, 15.8], size=8.5)
p("注: 授業資料の手書きメモ(学習者による訳)は出典として扱っていない。英訳・日本語訳は、授業資料の文法説明、辞書の語釈、接尾辞の意味から作成した。", italic=True, size=9, color=GREY)

# ------------------------------------------------------------ 2. 表記と発音
doc.add_heading("2. 表記と発音(授業資料 I1)", level=1)
table(["項目", "表記", "例"], [
    ["短母音", "a / i / u", "a は father の a、i は feet の ee を短く、u は boot の oo を短く"],
    ["長母音", "â (= aa) / e (= ii) / o (= uu)", "annâk(2人の女性)、angutek(2人の男性)、inok(2人)"],
    ["二重母音", "ai, au, ia, iu, ua, ui", "taima / auka 'no' / niaKuk 'head' / siutik 'ear' / pualuk 'mitten' / puijik 'seal'"],
    ["k と K", "k は英語の k、K は喉の奥で出す音(口蓋垂音)", "kimmik 'heel' と Kimmik 'dog' は別の語"],
    ["ng と二重の ng", "下線つき ng は長い ng", "angutik 'man'、pinnguak / pinguak 'toy'(書き方に揺れがある)"],
    ["子音の組み合わせ", "tl / dl, ts, tj / dj", "atlak (adlak) 'black bear'、Nunatsiavut、utjuk (udjuk) 'square flipper seal'"],
], [3.0, 5.0, 9.4], size=9)

# ------------------------------------------------------------ 3. 道すじ
doc.add_heading("3. A2 までの道すじ", level=1)
p("ユニットは授業の進み方に合わせて並べた。前のユニットの語尾や語を、後のユニットで組み合わせて使う。", after=4)
table(["#", "ユニット", "CEFR", "できるようになること"],
      [[i + 1, u["title"], u["cefr"], u["cando"]] for i, u in enumerate(B.UNITS)],
      [0.8, 5.6, 1.4, 9.6], size=9)
doc.add_page_break()

# ------------------------------------------------------------ 4. ユニット
doc.add_heading("4. ユニット別の例文", level=1)
for ui, u in enumerate(B.UNITS):
    doc.add_heading(f"ユニット {ui + 1}  {u['title']}  ({u['cefr']})", level=2)
    para = doc.add_paragraph(); r = para.add_run("できるようになること: "); r.bold = True
    para.add_run(u["cando"]); para.paragraph_format.space_after = Pt(4)
    p("文法のポイント", bold=True, size=10.5, color=AMBER, after=1)
    for t, body in u["grammar"]:
        para = doc.add_paragraph(style="List Bullet")
        rr = para.add_run(t + ": "); rr.bold = True; rr.font.size = Pt(10)
        r2 = para.add_run(body); r2.font.size = Pt(10)
        para.paragraph_format.space_after = Pt(1)
    p("例文", bold=True, size=10.5, color=AMBER, after=1)
    rows, fills, notes = [], [], []
    for i, x in enumerate(u["sentences"]):
        mark = ""
        if x["note"]:
            notes.append(x["note"]); mark = f" *{len(notes)}"
        rows.append([f"{ui + 1}-{i + 1}", x["inu"], x["en"], x["ja"], f"{KIND_SHORT[x['kind']]}\n{x['src']}{mark}"])
        fills.append(KIND_FILL[x["kind"]])
    table(["No.", "Inuttitut", "English", "日本語", "出典"], rows, [1.1, 4.6, 4.6, 4.6, 2.5], size=8.8, row_fills=fills, italic_cols=(1,))
    if notes:
        for n, t in enumerate(notes, 1):
            p(f"*{n}  {t}", size=8.5, color=GREY, after=1)
    if u.get("vocab"):
        p("このユニットの語彙(授業資料 I11 の Ilait 一覧。意味は辞書で確認)", bold=True, size=10, color=AMBER, after=1)
        table(["Inuttitut", "English", "日本語"], [list(v) for v in u["vocab"]], [4.0, 7.0, 6.4], size=8.8, italic_cols=(0,))

# ------------------------------------------------------------ 5. 文法表
doc.add_page_break()
doc.add_heading("5. 文法表(授業資料より)", level=1)
doc.add_heading("5-1. 自動詞の人称語尾(I8・I11)", level=2)
table(["", "1人称", "2人称", "3人称"], [
    ["単数(1)", "-vunga", "-vutit", "-juk"], ["双数(2)", "-vuguk", "-vutik", "-jok"], ["複数(3+)", "-vugut", "-vusi", "-jut"]], [3.0, 4.8, 4.8, 4.8])
doc.add_heading("5-2. 否定の語尾(I8・I11)", level=2)
table(["", "1人称", "2人称", "3人称"], [
    ["単数", "-ngilanga", "-ngilatit", "-ngituk"], ["双数", "-ngilaguk", "-ngilatik", "-ngitok"], ["複数", "-ngilagut", "-ngilasi", "-ngitut"]], [3.0, 4.8, 4.8, 4.8])
p("会話では3人称単数に -ngilak の形も使われる(I9: Anugingilak.)。", size=9, color=GREY)
doc.add_heading("5-3. 疑問の語尾(I8・I11)", level=2)
table(["", "1人称", "2人称", "3人称"], [
    ["単数", "-vingâ?", "-ven?", "-jong?"], ["双数", "-vinong?", "-viteng?", "-joung?"], ["複数", "-vitâ?", "-vise?", "-jon?"]], [3.0, 4.8, 4.8, 4.8])
doc.add_heading("5-4. 命令(I8。I11 では -get / -liget / -lauget と表記)", level=2)
table(["相手", "語尾", "例"], [
    ["1人", "-git / -ligit / -laugit", "Tupagit! / Tupaligit! / Tupalaugit!"],
    ["2人", "-gittek / -ligittek / -laugittek", "Tupagittek! / Tupaligittek! / Tupalaugittek!"],
    ["3人以上", "-gitsi / -ligitsi / -laugitsi", "Tupagitsi! / Tupaligitsi! / Tupalaugitsi!"]], [2.4, 6.0, 9.0])
doc.add_heading("5-5. 所有の語尾(I8・I11)", level=2)
table(["所有物", "私の", "あなたの", "彼/彼女の"], [
    ["1つ", "-ga", "-it", "-nga"], ["2つ", "-Vkka", "-Vkkik", "-Vgik"], ["3つ以上", "-kka", "-tit", "-ngit"]], [3.0, 4.8, 4.8, 4.8])
table(["名詞", "私の(1/2/3+)", "あなたの(1/2/3+)", "彼女の(1/2/3+)"], [
    ["panik 娘", "paniga / panekka / panikka", "panet / panekkik / panitit", "paninga / panegik / paningit"],
    ["innik 息子", "inniga / inneka / innika", "innet / innekik / innitit", "inninga / innegik / inningit"],
    ["illuk 家", "illuga / illoka / illuka", "illuit / illokik / illutit", "illunga / illogik / illungit"],
    ["Kajak カヤック", "Kajaga / Kajâkka / Kajakka", "Kajait / Kajâkkik / Kajatit", "Kajanga / Kajâgik / Kajangit"],
    ["umiak 船", "umiaga / umiakka / umiakka", "umiat / umiakkik / umiatit", "umianga / umiagik / umiangit"],
], [3.0, 4.8, 4.8, 4.8], size=8.8)
doc.add_heading("5-6. 名詞の格(II1・I11)", level=2)
table(["役割", "単数", "双数", "複数", "意味"], [
    ["主語(pijuk)", "-Ø", "-V", "-it", "〜は/が"], ["目的語(pijak)", "-mik", "-Vnik", "-nik", "〜を"],
    ["所有者", "-up", "-V", "-it", "〜の"], ["方向", "-mut", "-Vnut", "-nut", "〜へ"], ["起点", "-mit", "-Vnit", "-nit", "〜から"],
    ["場所", "-mi", "-Vni", "-ni", "〜で/に"], ["経路・手段", "-kkut", "-Vkkut", "-tigut", "〜を通って/〜で"], ["様態", "-tut", "-Vtut", "-titut", "〜のように"],
], [3.2, 2.6, 2.6, 2.6, 6.4], size=9)
p("V は語根末の母音を二重にすることを表す(授業資料の注記)。", size=9, color=GREY)
doc.add_heading("5-7. 時制(I9。pisuk- 歩く)", level=2)
table(["時制", "接尾辞", "私は", "あなたは", "彼/彼女は", "私は(否定)"], [
    ["今日より前", "-lauk-", "pisulaukKunga", "pisulaukKutit", "pisulauttuk", "pisulaungilanga"],
    ["今日の早いうち", "-kKau-", "pisukKauvunga", "pisukKauvutit", "pisukKaujuk", "pisukKaungilanga"],
    ["たった今", "-tainnak-", "pisutainnaKunga", "pisutainnaKutit", "pisutainnatuk", "pisutainnangilanga"],
    ["現在", "—", "pisuvunga", "pisuvutit", "pisujuk", "pisungilanga"],
    ["まさに今", "-lik- / -lu(k)-", "pisulikKunga", "pisulikKutit", "pisulittuk", "pisulungilanga"],
    ["しかけている", "-giasi-", "pisugiasivunga", "pisugiasivutit", "pisugiasijuk", "pisugiasingngilanga"],
    ["今日このあと", "-niak-", "pisuniakKunga", "pisuniakKutit", "pisuniattuk", "pisuniangilanga"],
    ["今日このあと(Hebron)", "-langa- / -langalu-", "pisulangavunga", "pisulangavutit", "pisulangajuk", "pisulangalungilanga"],
    ["明日以降", "-lâk-", "pisulâkKunga", "pisulâkKutit", "pisulâttuk", "pisulângilanga"],
], [3.0, 2.8, 3.0, 2.9, 2.8, 3.1], size=8.3)
doc.add_heading("5-8. 他動詞 takuk-(見る)(II3)", level=2)
table(["目的語 \\ 主語", "私が", "あなたが", "彼/彼女が"], [
    ["私を", "—", "takuvamma", "takuvânga"],
    ["あなたを", "takuvagit", "—", "takuvâtit"],
    ["彼/彼女を", "takujaga", "takujait", "takujanga"],
], [3.6, 4.6, 4.6, 4.6])
table(["目的語 \\ 主語(疑問)", "私が", "あなたが", "彼/彼女が"], [
    ["私を", "—", "takuvammâ?", "takuvângâ?"],
    ["あなたを", "takuvagen?", "—", "takuvâten?"],
    ["彼/彼女を", "takujagâ?", "takujân?", "takujaung?"],
], [3.6, 4.6, 4.6, 4.6])
doc.add_heading("5-9. 派生接尾辞の一覧(I8・I11)", level=2)
table(["種類", "接尾辞"], [
    ["名詞 → 動詞", "-u-(〜である)、-Ka-(〜を持つ)、-lia-(〜へ行く)、-liu-(〜を作る)、-tu-(〜を食べる/飲む)、-siu-(〜を探す)"],
    ["動詞 → 動詞", "-titsi-(させる)、-guma-(したい)、-songu-(できる)、-giaKa-(しなければならない)、-Kattak-(いつも)、-gunna-(してよい)、-giattu-(しに行く)、-gasua-(しようとする)、-jutsau-(されるべき)、-galâ-(ちょっと)、-kasâ-(しかける)、-gajak-(できるかも)、-galuak-(〜のに)"],
    ["名詞 → 名詞", "-nguak(おもちゃの〜)、-tsiak(よい〜・美しい〜)、-miuk(〜の人)、-vinik(〜の肉)"],
    ["動詞 → 名詞", "-vik(〜する場所)"],
], [3.0, 14.4], size=9)
doc.add_heading("5-10. 数", level=2)
table(["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], [
    ["数(I10)", "atautsik", "maggok", "pingasut", "sitamat", "tallimat", "pingasojuttut", "—", "sitamaujuttut", "—", "tallimaujuttut", "—", "—"],
    ["時刻など(II8)", "ainsik", "suvait", "tarait", "fiarat", "fimfit", "sâtsit", "sepat", "âttat", "nainat", "senat", "ailfat", "suvailfat"],
], [2.2] + [1.27] * 12, size=7.5)
p("— は資料に記載がないもの(I10 の表では 7・9 の欄が空いている。11・12 は I10 に載っていない)。", size=9, color=GREY)

OUT = sys.argv[1] if len(sys.argv) > 1 else "Inuttitut_A2_例文集.docx"
doc.save(OUT)
print("saved", OUT, len(items), "items")
