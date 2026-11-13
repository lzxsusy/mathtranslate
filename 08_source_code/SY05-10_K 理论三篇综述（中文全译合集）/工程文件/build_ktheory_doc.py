# -*- coding: utf-8 -*-
"""Build the Chinese K-theory / string theory reading dossier (.docx)."""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT

DOCX_PATH = r"<本地路径>"

INK = "1A1A1A"
NAVY = "1F3864"
BLUE = "2E5496"
LINK = "1F5FA8"
GRAY = "666666"
LIGHT = "F4F6FA"
HEAD_BG = "1F3864"

TAG_COLORS = {
    "必读": "C00000",
    "核心": "2E5496",
    "专题": "A0522D",
    "进阶": "7F6000",
    "背景": "666666",
}

DOC = None


# ----------------------------------------------------------------------------
# low level helpers
# ----------------------------------------------------------------------------
def rgb(h):
    return RGBColor.from_string(h)


def clean_theme_fonts(rPr):
    rf = rPr.find(qn("w:rFonts"))
    if rf is None:
        return
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rf.get(qn(attr)) is not None:
            del rf.attrib[qn(attr)]


def set_rfonts(rPr, ascii_font, ea_font):
    clean_theme_fonts(rPr)
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.insert(0, rFonts)
    rFonts.set(qn("w:ascii"), ascii_font)
    rFonts.set(qn("w:hAnsi"), ascii_font)
    rFonts.set(qn("w:eastAsia"), ea_font)


def fmt_run(run, size=10.5, bold=False, italic=False, color=INK,
            ascii_font="Times New Roman", ea_font="宋体"):
    run.font.name = ascii_font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = rgb(color)
    set_rfonts(run._element.get_or_add_rPr(), ascii_font, ea_font)


def add_hyperlink(paragraph, url, text, size=9, color=LINK, bold=False,
                  ea_font="宋体"):
    part = paragraph.part
    r_id = part.relate_to(url, RT.HYPERLINK, is_external=True)
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("r:id"), r_id)
    r = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Times New Roman")
    rFonts.set(qn("w:hAnsi"), "Times New Roman")
    rFonts.set(qn("w:eastAsia"), ea_font)
    rPr.append(rFonts)
    if bold:
        rPr.append(OxmlElement("w:b"))
    c = OxmlElement("w:color")
    c.set(qn("w:val"), color)
    rPr.append(c)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int(size * 2)))
    rPr.append(sz)
    szcs = OxmlElement("w:szCs")
    szcs.set(qn("w:val"), str(int(size * 2)))
    rPr.append(szcs)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    r.append(rPr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    r.append(t)
    hl.append(r)
    paragraph._p.append(hl)


def add_segments(p, segments, size=10.5):
    for seg in segments:
        if isinstance(seg, str):
            text, fmt = seg, {}
        else:
            text, fmt = seg
        s = fmt.get("size", size)
        if fmt.get("link"):
            add_hyperlink(p, fmt["link"], text, size=s,
                          color=fmt.get("color", LINK),
                          bold=fmt.get("bold", False))
        else:
            r = p.add_run(text)
            fmt_run(r, size=s, bold=fmt.get("bold", False),
                    italic=fmt.get("italic", False),
                    color=fmt.get("color", INK),
                    ascii_font=fmt.get("ascii_font", "Times New Roman"),
                    ea_font=fmt.get("ea_font", "宋体"))


def add_rule(p, color=NAVY, size=8):
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.insert_element_before(
        pBdr, "w:shd", "w:tabs", "w:suppressAutoHyphens", "w:kinsoku",
        "w:wordWrap", "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE",
        "w:autoSpaceDN", "w:bidi", "w:adjustRightInd", "w:snapToGrid",
        "w:spacing", "w:ind", "w:contextualSpacing", "w:mirrorIndents",
        "w:suppressOverlap", "w:jc", "w:textDirection", "w:textAlignment",
        "w:textboxTightWrap", "w:outlineLvl", "w:divId", "w:cnfStyle",
        "w:rPr", "w:sectPr", "w:pPrChange")


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def set_table_borders(table, color="BFC7D5", sz=4):
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:" + edge)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(sz))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblPr.insert_element_before(
        borders, "w:shd", "w:tblLayout", "w:tblCellMar", "w:tblLook",
        "w:tblCaption", "w:tblDescription")


def set_cell_margins(table, top=50, bottom=50, left=80, right=80):
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblCellMar")):
        tblPr.remove(old)
    mar = OxmlElement("w:tblCellMar")
    for side, val in (("top", top), ("left", left),
                      ("bottom", bottom), ("right", right)):
        el = OxmlElement("w:" + side)
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.insert_element_before(
        mar, "w:tblLook", "w:tblCaption", "w:tblDescription")


def prevent_split(row):
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn("w:cantSplit")) is None:
        cs = OxmlElement("w:cantSplit")
        trPr.insert_element_before(cs, "w:trHeight", "w:tblHeader",
                                   "w:tblCellSpacing", "w:jc", "w:hidden")


def make_table(headers, rows, widths, font_size=9):
    table = DOC.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)
    set_cell_margins(table)

    for i, col in enumerate(table.columns):
        col.width = Cm(widths[i])
    hdr = table.rows[0]
    trPr = hdr._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader")
    th.set(qn("w:val"), "true")
    trPr.append(th)
    prevent_split(hdr)
    for i, text in enumerate(headers):
        cell = hdr.cells[i]
        cell.width = Cm(widths[i])
        shade(cell, HEAD_BG)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.1
        r = p.add_run(text)
        fmt_run(r, size=font_size, bold=True, color="FFFFFF",
                ea_font="微软雅黑")

    for ri, row in enumerate(rows):
        cells = table.add_row().cells
        prevent_split(table.rows[-1])
        for i, val in enumerate(row):
            cell = cells[i]
            cell.width = Cm(widths[i])
            if ri % 2 == 1:
                shade(cell, LIGHT)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            if isinstance(val, str):
                r = p.add_run(val)
                fmt_run(r, size=font_size)
            else:
                add_segments(p, val, size=font_size)
    return table


def spacer(pts=4):
    p = DOC.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(pts)
    return p


# ----------------------------------------------------------------------------
# document setup
# ----------------------------------------------------------------------------
def setup():
    sec = DOC.sections[0]
    sec.page_width = Cm(21)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(2.2)
    sec.bottom_margin = Cm(2.0)
    sec.left_margin = Cm(2.2)
    sec.right_margin = Cm(2.2)
    sec.header_distance = Cm(1.2)
    sec.footer_distance = Cm(1.0)
    sec.different_first_page_header_footer = True

    normal = DOC.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(10.5)
    normal.font.color.rgb = rgb(INK)
    set_rfonts(normal.element.get_or_add_rPr(),
               "Times New Roman", "宋体")
    pf = normal.paragraph_format
    pf.line_spacing = 1.32
    pf.space_after = Pt(6)
    pf.space_before = Pt(0)

    heading_specs = [
        ("Heading 1", 16, NAVY, 18, 8),
        ("Heading 2", 13, BLUE, 12, 6),
        ("Heading 3", 11.5, NAVY, 10, 4),
    ]
    for name, size, color, before, after in heading_specs:
        st = DOC.styles[name]
        st.font.name = "Times New Roman"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = rgb(color)
        set_rfonts(st.element.get_or_add_rPr(),
                   "Times New Roman", "微软雅黑")
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(after)
        st.paragraph_format.keep_with_next = True
        st.paragraph_format.line_spacing = 1.2

    # footer page number (not on cover)
    footer = sec.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run("— ")
    fmt_run(r, size=8, color=GRAY)
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), " PAGE ")
    fr = OxmlElement("w:r")
    frPr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts")
    rf.set(qn("w:ascii"), "Times New Roman")
    rf.set(qn("w:hAnsi"), "Times New Roman")
    frPr.append(rf)
    fsz = OxmlElement("w:sz")
    fsz.set(qn("w:val"), "16")
    frPr.append(fsz)
    fr.append(frPr)
    ft = OxmlElement("w:t")
    ft.text = "1"
    fr.append(ft)
    fld.append(fr)
    fp._p.append(fld)
    r = fp.add_run(" —")
    fmt_run(r, size=8, color=GRAY)


# ----------------------------------------------------------------------------
# text helpers
# ----------------------------------------------------------------------------
def body(segments, indent=True, size=10.5, after=6):
    p = DOC.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(after)
    pf.line_spacing = 1.32
    if indent:
        pf.first_line_indent = Cm(0.74)
    add_segments(p, segments, size=size)
    return p


def bullet(segments, size=10.5, after=3):
    p = DOC.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(0.9)
    pf.first_line_indent = Cm(-0.45)
    pf.space_after = Pt(after)
    pf.line_spacing = 1.28
    add_segments(p, [("• ", {"color": BLUE, "bold": True})] + segments, size=size)
    return p


def note(segments, size=9.5, after=6):
    p = DOC.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(after)
    pf.line_spacing = 1.25
    pf.left_indent = Cm(0.2)
    add_segments(p, segments, size=size)
    return p


# ----------------------------------------------------------------------------
# cover + contents
# ----------------------------------------------------------------------------
def cover():
    p = DOC.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(130)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run("弦论中的 K-理论")
    fmt_run(r, size=30, bold=True, color=NAVY,
            ascii_font="Georgia", ea_font="微软雅黑")

    p = DOC.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(10)
    add_rule(p)

    p = DOC.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run("D-膜、Ramond–Ramond 荷与快子凝聚")
    fmt_run(r, size=16, bold=True, color=BLUE, ea_font="微软雅黑")

    p = DOC.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(26)
    r = p.add_run("—— 专题综述选读 ——")
    fmt_run(r, size=12, color=GRAY, ea_font="微软雅黑")

    p = DOC.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.left_indent = Cm(2.2)
    p.paragraph_format.right_indent = Cm(2.2)
    p.paragraph_format.line_spacing = 1.45
    p.paragraph_format.space_after = Pt(0)
    add_segments(p, [(
        "本专题以“K-理论如何刻画 D-膜荷与快子凝聚”为主线，选入 Witten、Moore、"
        "Olsen–Szabo 的三篇核心综述，以及奠基论文、快子凝聚关键文献与讲义共二十六篇。"
        "所有条目均在 arXiv 逐一核验，并给出三条阅读路线。",
        {"size": 10, "color": GRAY})], size=10)

    p = DOC.add_paragraph()
    p.paragraph_format.space_before = Pt(150)
    p.paragraph_format.space_after = Pt(2)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("编制：DSH 文献整理　·　2026 年 11 月")
    fmt_run(r, size=10, color=GRAY)
    p = DOC.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("文献来源：arXiv.org　·　条目核验日期：2026-11-06")
    fmt_run(r, size=9, color=GRAY)

    DOC.add_page_break()


def contents():
    p = DOC.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run("目　录")
    fmt_run(r, size=20, bold=True, color=NAVY, ea_font="微软雅黑")
    add_rule(p, color="BFC7D5", size=6)

    items = [
        ("一、导言：为什么用 K-理论看弦论", 0),
        ("二、问题地图：五个核心问题", 0),
        ("三、三篇核心综述", 0),
        ("四、分主题文献导读", 0),
        ("4.1　D-膜荷的 K-理论：三篇奠基论文", 1),
        ("4.2　从荷到场、从物理到数学", 1),
        ("4.3　快子凝聚与 Sen 猜想", 1),
        ("4.4　讲义与背景", 1),
        ("五、Sen 猜想专页", 0),
        ("六、阅读路线", 0),
        ("七、名词速查", 0),
        ("八、arXiv 链接总表", 0),
        ("九、核验说明", 0),
    ]
    for text, level in items:
        p = DOC.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.6 + 0.9 * level)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        fmt_run(r, size=11 if level == 0 else 10,
                bold=(level == 0),
                color=INK if level == 0 else GRAY,
                ea_font="微软雅黑")
    DOC.add_page_break()


# ----------------------------------------------------------------------------
# section 1 - introduction
# ----------------------------------------------------------------------------
def sec1():
    DOC.add_heading("一、导言：为什么用 K-理论看弦论", level=1)
    body([
        "1997–1998 年间，弦论对 D-膜荷的拓扑理解发生了一次跃迁。Minasian 与 Moore 指出，"
        "D-膜携带的 Ramond–Ramond（RR）荷不能只用普通上同调刻画，Chan–Paton 丛的拓扑才是关键；"
        "Witten 随后系统论证：稳定 D-膜荷取值于时空的 K-理论。Horava 则给出构造性证明——"
        "IIA 型理论中所有超对称 D-膜都可由 16 个不稳定 D9-膜上的快子凝聚得到，"
        "相应的荷由 K^{-1}(X) 分类。",
    ])
    body([
        "物理上的原因并不神秘。考虑时空 X 上的一对 D9–反 D9 膜，分别带有 Chan–Paton 丛 E 和 F。"
        "若同时产生（或湮灭）一对带相同丛 G 的 D9–反 D9 膜，物理上不改变任何可观测的荷，"
        "于是在 K-理论中作等价 (E,F) ~ (E⊕G, F⊕G)；等价类构成的群就是 K(X)。"
        "快子凝聚正是实现这一等价关系的动力学过程：brane–antibrane 对上的快子场凝聚，使这对膜消失。",
    ])
    body([
        "由此得到的分类是：IIB 型理论中 D-膜荷取值于 K^0(X)，IIA 型理论中取值于 K^1(X)，"
        "type I 型理论中取值于实 K-理论 KO(X)。RR 场则比荷再移一个 Bott 度："
        "IIB 的 RR 场由 K^1(X) 分类，IIA 的 RR 场由 K^0(X) 分类。"
        "当背景存在非平凡的 NS–NS 三形式 H-流时，普通 K-理论要被扭曲 K-理论取代。",
    ])
    body([
        "这套语言解释了普通上同调看不到的现象：type I 理论中稳定的非 BPS D0-膜、"
        "上同调非平凡却会衰变的 D-膜，以及整体世界面反常的抵消（Freed–Witten 反常），"
        "都只有在 K-理论框架中才自然。",
    ])
    body([
        "而把这些拓扑陈述变成物理动力学核心的，是 Sen 关于快子凝聚的猜想：brane–antibrane 系统的"
        "快子势在极小处，负能量密度恰好抵消两膜张力之和，系统达到零能量并恢复超对称；"
        "非 BPS D-膜上则恰好抵消单膜张力。由快子扭结（kink）解可以得到降维关系"
        "（descent relations），低维 D-膜被理解为高维 brane–antibrane 对上的拓扑孤子。"
        "1999–2006 年间，开弦场论的能级截断计算与 Schnabl 的解析解先后验证并证明了这一猜想。",
    ])
    body([
        "K-理论视角还自然延伸到非交换几何：B-场使时空函数代数非交换，K-理论可以直接推广到"
        "算子代数，而 K-同调与 Kasparov 的 KK-理论给出了更一般的家。Moore 的讲义正是从边界 CFT "
        "的 RG 流、整体反常与 D-膜瞬子出发，论证“物理上为什么必须是 K-理论”；Witten 的综述则用"
        "二十页把电荷、场、非交换推广与大 N 开弦场论串成一条线。",
    ])
    body([
        "本专题的选文原则：只收三类材料——(i) 综述与讲义；(ii) 奠定分类的原始论文；"
        "(iii) 快子凝聚与 Sen 猜想的关键原始论文与证明。全部条目均给出 arXiv 编号并已核验，"
        "按主题分成四组，并在最后给出三条阅读路线。",
    ])


# ----------------------------------------------------------------------------
# section 2 - problem map
# ----------------------------------------------------------------------------
def sec2():
    DOC.add_heading("二、问题地图：五个核心问题", level=1)
    body([
        "K-理论进入弦论不是单一结果，而是一组彼此咬合的问题。下表把五个核心问题、"
        "对应的 K-理论语言与代表文献放在一起，方便先建立坐标系。",
    ])
    headers = ["#", "问题", "K-理论语言", "关键文献"]
    rows = [
        ["1", "稳定 D-膜荷如何分类？",
         "IIB: K^0(X)；IIA: K^1(X)；type I: KO(X)",
         "Minasian–Moore 1997；Witten 1998；Horava 1998"],
        ["2", "存在 H-流（B-场）时如何分类？",
         "扭曲 K-理论 K_H(X)",
         "Kapustin 1999；Freed–Witten 1999；Evslin 2006"],
        ["3", "物理上为什么必须是 K-理论？",
         "边界 CFT 间的 RG 流、整体反常、D-膜瞬子",
         "Moore 2003；Szabo 2002（K-同调）"],
        ["4", "非交换/矩阵背景下如何定义荷？",
         "算子代数 K-理论、KK-理论",
         "Harvey 2001；Szabo 2008"],
        ["5", "快子凝聚如何实现 K-理论等价？",
         "brane–antibrane 湮灭、开弦场论",
         "Sen 1998；Sen–Zwiebach 2000；Schnabl 2006；Sen 2005"],
        ["6", "非 BPS、orientifold 情形？",
         "KO、KR、扭曲（等变）K-理论",
         "Schwarz 1999；Witten 1998；Braun–Stefanski 2002"],
    ]
    make_table(headers, rows, [0.8, 4.7, 5.2, 5.9], font_size=8.8)
    spacer(2)
    note([
        ("读法提示：", {"bold": True, "color": BLUE, "size": 9}),
        ("第 1 行是主线；第 2、3 行说明 K-理论为什么比上同调更“对”；第 5 行是把拓扑等价变成"
         "物理过程的动力学机制；第 6 行是边界情形。", {"size": 9, "color": GRAY}),
    ])


# ----------------------------------------------------------------------------
# section 3 - three core reviews
# ----------------------------------------------------------------------------
CORE_REVIEWS = [
    dict(
        label="★1", title="Overview of K-Theory Applied To Strings",
        authors="Edward Witten",
        arxiv="hep-th/0007175",
        venue="Int. J. Mod. Phys. A16 (2001) 693–706 · 20 页 · Strings 2000 报告",
        tag="必读",
        body=("最短的权威入口。从 A(X) 模的语言定义 K(X)，把 D-膜荷、膜–反膜对的产生/湮灭与"
              "K-理论等价 (E,F)~(E⊕G,F⊕G) 讲清楚；随后讨论 RR 场的 K^1 分类、非交换代数推广，"
              "以及用无穷多个 D9-膜经快子凝聚约化到有限组态、从而重新思考 N=∞ 开弦场论。"
              "若只读一篇，读这篇。"),
    ),
    dict(
        label="★2", title="K-Theory from a Physical Perspective",
        authors="Gregory Moore",
        arxiv="hep-th/0304018",
        venue="expository 讲义（会议文集，arXiv 无 journal_ref）· 43 页",
        tag="必读",
        body=("从物理第一原理出发的 K-理论讲义：把边界 CFT 之间的重整化群流、整体反常抵消与"
              "D-膜瞬子结合起来，说明 K-理论分类不是从数学借来的，而是物理一致性逼出来的；"
              "并以 SU(N) 的扭曲 K-理论为例演示。更短的 10 页速览版见 Moore, "
              "“Some Comments on Branes, G-flux, and K-theory”（hep-th/0012007）。"),
    ),
    dict(
        label="★3", title="Constructing D-Branes from K-Theory",
        authors="Kasper Olsen, Richard J. Szabo",
        arxiv="hep-th/9907140",
        venue="Adv. Theor. Math. Phys. 3 (1999) 889–1025 · 112 页",
        tag="必读",
        body=("一篇 112 页的文献级综述：前半是自足的拓扑 K-理论数学导引，后半把 D-膜实现为"
              "快子孤子，系统复现 BPS 与非 BPS 谱、推导 D-膜荷的显式公式、把各种对偶实现为"
              "K-群同构。数学背景强的读者可从这篇入门；物理读者可把它当参考手册。"),
    ),
]


def lit_entry(entry):
    p = DOC.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    add_segments(p, [
        (entry["label"] + "　", {"bold": True, "color": BLUE, "size": 10}),
        (entry["title"], {"bold": True, "color": NAVY, "size": 11.5,
                          "ea_font": "微软雅黑"}),
    ])
    p = DOC.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    add_segments(p, [
        (entry["authors"] + "　·　", {"color": GRAY, "size": 9}),
        ("arXiv:" + entry["arxiv"],
         {"link": "https://arxiv.org/abs/" + entry["arxiv"], "size": 9}),
        ("　·　" + entry["venue"] + "　", {"color": GRAY, "size": 9}),
        ("[" + entry["tag"] + "]",
         {"color": TAG_COLORS[entry["tag"]], "size": 9, "bold": True}),
    ])
    p = DOC.add_paragraph()
    p.paragraph_format.space_after = Pt(9)
    p.paragraph_format.line_spacing = 1.3
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_segments(p, [(entry["body"], {"size": 10.5})])


def sec3():
    DOC.add_heading("三、三篇核心综述", level=1)
    body([
        "如果时间有限，先读下面三篇。它们分别回答三个问题：K-理论如何分类荷与场（Witten）、"
        "物理上为什么是 K-理论（Moore）、如何系统地从 K-理论构造 D-膜（Olsen–Szabo）。",
    ])
    note([
        ("一个必要的澄清：", {"bold": True, "color": "C00000", "size": 9.5}),
        ("Witten 与 Moore 各有短篇 overview，但两人都没有写长篇教科书式综述；真正系统的大部头"
         "是 Olsen–Szabo。另外，Witten 的 “D-Branes And K-Theory”（hep-th/9810188）与 "
         "Minasian–Moore（hep-th/9710230）是原始研究论文，不是综述——它们放在下一节。",
         {"size": 9.5, "color": GRAY}),
    ])
    for entry in CORE_REVIEWS:
        lit_entry(entry)


# ----------------------------------------------------------------------------
# section 4 - thematic entries
# ----------------------------------------------------------------------------
GROUP_A = [
    dict(label="A1", title="K-theory and Ramond-Ramond Charge",
         authors="Ruben Minasian, Gregory Moore", arxiv="hep-th/9710230",
         venue="JHEP 9711:002 · 8 页 · 原始研究", tag="核心",
         body=("最早把 RR 荷与 Chan–Paton 丛的拓扑联系起来的工作之一：证明拓扑非平凡的法丛会"
               "诱导 RR 荷，并指出 D-膜荷应理解为 K-理论类。篇幅很短，是这条研究线的起点。")),
    dict(label="A2", title="D-Branes And K-Theory",
         authors="Edward Witten", arxiv="hep-th/9810188",
         venue="JHEP 9812:019 · 44 页 · 奠基原始研究", tag="核心",
         body=("奠基论文：利用关于稳定非超对称 D-膜态的论证，提出 D-膜荷取值于时空 K-理论；"
               "IIB 对应 K^0、IIA 对应 K^1、type I 对应 KO，并由此预言 type I 的零膜与 -1-膜等"
               "新对象。分类的“宪法”。")),
    dict(label="A3", title="Type IIA D-Branes, K-Theory, and Matrix Theory",
         authors="Petr Horava", arxiv="hep-th/9812135",
         venue="Adv. Theor. Math. Phys. 2 (1999) 1373–1404 · 32 页 · 原始研究", tag="核心",
         body=("构造性证明：IIA 型理论中所有超对称 D-膜都可由 16 个不稳定 D9-膜上的快子孤子得到，"
               "从而 D-膜荷由 K^{-1}(X) 分类；同时把矩阵理论的动力学与 16 个 D9-膜世界体上的"
               "U(16) 规范场联系起来。")),
]

GROUP_B = [
    dict(label="B1", title="Self-Duality, Ramond-Ramond Fields, and K-Theory",
         authors="Gregory Moore, Edward Witten", arxiv="hep-th/9912279",
         venue="JHEP 0005:032 · 35 页 · 原始研究", tag="进阶",
         body=("把 RR 场（不止电荷）也纳入 K-理论：IIB 的 RR 场由 K^1 分类、IIA 由 K^0 分类；"
               "并证明自对偶性要求对 RR p-形式的 Dirac 量子化公式作出曲率、低维膜荷与 D-膜"
               "世界体费米子反常的修正——这些修正无法用普通上同调自然表达。")),
    dict(label="B2", title="D-Branes, Tachyons and K-Homology",
         authors="Richard J. Szabo", arxiv="hep-th/0209210",
         venue="Mod. Phys. Lett. A17 (2002) 2297–2316 · 18 页", tag="进阶",
         body=("K-同调视角的短综述：强调 D-膜荷的（同调式）分类在拓扑上更自然，并解释"
               "K-同调类与 D-膜之间的物理对应。适合在读完 Witten 1998 后换一个数学视角。")),
    dict(label="B3", title="D-branes and Bivariant K-Theory",
         authors="Richard J. Szabo", arxiv="0809.3029",
         venue="讲义（World Scientific, 2008）· 45 页",
         tag="进阶",
         body=("用几何 K-同调与 Kasparov KK-理论系统处理 D-膜荷：非交换空间上的分类、"
               "用对应与 KK-等价刻画开弦 T-对偶、非交换 Riemann 面与常 H-流背景，"
               "并涉及 Poincaré 对偶、K-定向、特征类与 Riemann–Roch。数学味最重的一篇。")),
    dict(label="B4", title="What Does(n't) K-Theory Classify?",
         authors="Jarah Evslin", arxiv="hep-th/0610328",
         venue="Modave 暑期学校讲义 · 91 页", tag="进阶",
         body=("标题就是问题：K-理论到底分类了什么？作者逐一审视各类 K-理论分类猜想——"
               "基于 Sen 猜想的版本、基于 Freed–Witten 反常的版本——并指出它们在 RR 场自对偶"
               "与 IIB 的 S-对偶下的困难。想理解“K-理论分类的适用边界”，这篇最清醒。")),
    dict(label="B5", title="D-branes in a Topologically Nontrivial B-Field",
         authors="Anton Kapustin", arxiv="hep-th/9909089",
         venue="Adv. Theor. Math. Phys. 4 (2000) 127–154 · 24 页", tag="进阶",
         body=("从世界面整体反常出发，说明当 B-场拓扑非平凡时 D-膜荷取值于扭曲 K-理论"
               "（Witten 的猜想）；并论证 D-膜上的规范场其实是某个非交换代数模上的联络。"
               "扭曲 K-理论方向的源头文献之一。")),
    dict(label="B6", title="Anomalies in String Theory with D-Branes",
         authors="Daniel S. Freed, Edward Witten", arxiv="hep-th/9907189",
         venue="Asian J. Math. 3 (1999) 819 · 39 页 · 原始研究", tag="进阶",
         body=("证明整体反常抵消给出 D-膜拓扑的限制，正是这一限制使得 D-膜荷的 K-理论解释成为"
               "可能。Freed–Witten 反常的原始文献，理解“为什么必须是 K-理论”的必读材料。")),
]

GROUP_C = [
    dict(label="C1", title="Tachyon Condensation on the Brane Antibrane System",
         authors="Ashoke Sen", arxiv="hep-th/9805170",
         venue="JHEP 9808:012 · 6 页 · 原始研究", tag="专题",
         body=("Sen 猜想的原始表述：brane–antibrane 对存在快子模；论证在快子势的经典极小处，"
               "负能量密度恰好抵消膜与反膜张力之和，给出零能量组态并恢复时空超对称。"
               "全文只有 6 页，却是整个方向的起点。")),
    dict(label="C2", title="Universality of the Tachyon Potential",
         authors="Ashoke Sen", arxiv="hep-th/9911116",
         venue="JHEP 9912:027 · 21 页 · 原始研究", tag="专题",
         body=("用开弦场论论证快子势的普适性：在任意边界 CFT 背景下，D-膜–反 D-膜系统"
               "（以及非 BPS D-膜）的快子势具有相同形式；若某背景中极小处能量为零，则任何背景"
               "都为零。这把 Sen 猜想从特例提升为普适陈述。")),
    dict(label="C3", title="Tachyon Condensation in String Field Theory",
         authors="Ashoke Sen, Barton Zwiebach", arxiv="hep-th/9912249",
         venue="JHEP 0003:002 · 13 页 · 原始研究", tag="专题",
         body=("在 Witten 立方开弦场论中做能级截断：只保留快子时，势极小处抵消约 70% 的 D-膜"
               "张力；保留到快子以上四个质量能级时抵消约 99%。这是 Sen 猜想最早的定量证据，"
               "也是“能级截断”方法的范本。")),
    dict(label="C4", title="Analytic Solution for Tachyon Condensation in Open String Field Theory",
         authors="Martin Schnabl", arxiv="hep-th/0511286",
         venue="Adv. Theor. Math. Phys. 10 (2006) 433–501 · 60 页 · 原始研究", tag="专题",
         body=("构造立方开弦场论的精确解析解，描述非微扰快子真空；通过计算微扰真空与非微扰真空"
               "的能量差，解析地证明 Sen 第一猜想。开弦场论非微扰物理的里程碑，也是理解快子凝聚"
               "严格含义的必读。")),
    dict(label="C5", title="D-Branes, Tachyons, and String Field Theory",
         authors="Washington Taylor, Barton Zwiebach", arxiv="hep-th/0311017",
         venue="TASI 2001 讲义 · 103 页", tag="核心",
         body=("最佳自足入门：从 Yang–Mills 低能描述讲到 Witten 立方开弦场论，用 CFT 与"
               "overlap 积分完整搭建形式体系，逐条陈述 Sen 三猜想及其证据，最后讨论 VSFT 与"
               "star-代数投影算符。更短的 52 页版本见 Taylor, hep-th/0301094。")),
    dict(label="C6", title="Tachyon Dynamics in Open String Theory",
         authors="Ashoke Sen", arxiv="hep-th/0410103",
         venue="Int. J. Mod. Phys. A20 (2005) 5513–5656 · 169 页 · 综述", tag="核心",
         body=("快子动力学最完整的综述：二维 CFT、开弦场论、边界弦场论、非交换孤子、"
               "快子有效作用量（DBI 型）、衰变 D-膜产生的闭弦背景，以及由此提出的开弦完备性"
               "猜想。可当工具书长期查阅。")),
    dict(label="C7", title="Non-BPS States and Branes in String Theory",
         authors="Ashoke Sen", arxiv="hep-th/9904207",
         venue="APCTP 冬季学校讲义 · 53 页", tag="专题",
         body=("非 BPS 态与膜的综述：IIA/IIB 中不稳定非 BPS D-膜的构造、orbifold/orientifold 上"
               "的稳定非 BPS 膜、用高维 brane–antibrane 对上的快子孤子描述 BPS 与非 BPS 膜，"
               "以及 D-膜–orientifold 系统的谱。降维关系（descent relations）的详细讨论在这里。")),
    dict(label="C8", title="String Field Theory: A Review",
         authors="Ashoke Sen, Barton Zwiebach", arxiv="2405.19421",
         venue="Handbook of Quantum Gravity · 172 页 · 最新综述", tag="进阶",
         body=("2024 年的 SFT 大综述，覆盖 A∞/L∞ 代数、模空间与 picture changing、BV 量子化，"
               "以及非微扰应用（快子凝聚、经典解）。若想了解 Sen 猜想与开弦场论在当代的完整"
               "图景，从这篇的 tachyon condensation 章节入手。")),
]

GROUP_D = [
    dict(label="D1", title="TASI Lectures on Non-BPS D-Brane Systems",
         authors="John H. Schwarz", arxiv="hep-th/9908144",
         venue="TASI-99 / Cargèse-99 讲义 · 39 页", tag="背景",
         body=("从 D-膜基础讲到非 BPS 系统，重点讨论 K-理论对 D-膜荷的分类（尤其 type I 与"
               "T-对偶的 type I'），并指出 K-理论预言的 type I D7/D8-膜存在的问题。"
               "适合作为非 BPS 方向的入门。")),
    dict(label="D2", title="Komaba Lectures on Noncommutative Solitons and D-Branes",
         authors="Jeffrey A. Harvey", arxiv="hep-th/0102076",
         venue="Komaba 2000 讲义 · 43 页", tag="背景",
         body=("从量子力学与非交换几何讲到非交换场论中的孤子，再把 D-膜实现为快子场的非交换"
               "孤子，最后简要介绍用算子代数 K-理论分类 D-膜荷。连接非交换几何与 K-理论的桥梁。")),
    dict(label="D3", title="Recent Progress in Superstring Theory",
         authors="John H. Schwarz", arxiv="hep-th/0007130",
         venue="会议报告 · 13 页", tag="背景",
         body=("一篇很短的综述报告，把 K-理论分类、快子凝聚、非交换场论三个主题串在一起。"
               "适合在正式读长文前快速建立全局印象。")),
    dict(label="D4", title="D-Brane Primer",
         authors="Clifford V. Johnson", arxiv="hep-th/0007170",
         venue="D-膜系统讲义 · 222 页", tag="背景",
         body=("222 页的 D-膜系统讲义：从经典点粒子、弦的量子化讲到 D-膜、超引力、弦对偶与"
               "AdS/CFT 等应用。不专门讲 K-理论，但作为前置背景非常完整，可当 D-膜百科。")),
    dict(label="D5", title="TASI Lectures on D-Branes",
         authors="Joseph Polchinski", arxiv="hep-th/9611050",
         venue="TASI-96 讲义 · 63 页", tag="背景",
         body=("TASI 的 D-膜经典讲义：D-膜的定义、超对称、与弦对偶及黑洞的联系。"
               "读 K-理论文献前最好的热身，篇幅适中。")),
    dict(label="D6", title="D-branes, Categories and N=1 Supersymmetry",
         authors="Michael R. Douglas", arxiv="hep-th/0011017",
         venue="J. Math. Phys. 42 (2001) 2818–2843 · 41 页", tag="背景",
         body=("邻近方向的延伸：B-模型 D-膜由 Calabi–Yau 上相干层的导出范畴描述，配合 "
               "Pi-稳定性判据给出 BPS 膜的判据。属于“读完 K-理论之后”的自然下一步——"
               "从 K-理论走向导出范畴。")),
]


def group_title(text):
    p = DOC.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    fmt_run(r, size=11, bold=True, color=BLUE, ea_font="微软雅黑")
    add_rule(p, color="D6DCE5", size=4)


def sec4():
    DOC.add_heading("四、分主题文献导读", level=1)
    body([
        "以下按主题分组。每条的“标签”只是相对重要性，不代表难度；"
        "“原始研究”表示该条不是综述，但它在这条研究线中绕不开。",
    ])

    DOC.add_heading("4.1　D-膜荷的 K-理论：三篇奠基论文", level=2)
    body([
        "按时间顺序读最顺：先看 Minasian–Moore 的物理观察，再看 Witten 的系统分类，"
        "最后看 Horava 的构造性证明。三篇都是原始研究，篇幅不长但信息密度高。",
    ])
    for e in GROUP_A:
        lit_entry(e)

    DOC.add_heading("4.2　从荷到场、从物理到数学", level=2)
    body([
        "这一组处理“荷之外还有什么”以及“数学上用什么语言”：把 RR 场也纳入 K-理论"
        "（Moore–Witten）、用 K-同调与 KK-理论重述分类（Szabo 两篇）、批判性审视分类猜想"
        "的边界（Evslin），以及扭曲 K-理论的两篇源头（Kapustin；Freed–Witten）。",
    ])
    for e in GROUP_B:
        lit_entry(e)

    gap = DOC.add_paragraph()
    gap.paragraph_format.space_before = Pt(4)
    gap.paragraph_format.space_after = Pt(8)
    gap.paragraph_format.line_spacing = 1.3
    add_segments(gap, [
        ("缺口提示：", {"bold": True, "color": "C00000", "size": 9.5}),
        ("扭曲 K-理论（H-流背景）与 orientifold 目前都没有面向物理读者的专门长综述。"
         "扭曲 K-理论的入口是上面的源头论文，加上两篇数学综述——Atiyah–Segal, "
         "“Twisted K-theory”（", {"size": 9.5, "color": GRAY}),
        ("math/0407054", {"link": "https://arxiv.org/abs/math/0407054", "size": 9.5}),
        ("）与 Karoubi, “Twisted K-theory, old and new”（", {"size": 9.5, "color": GRAY}),
        ("math/0701789", {"link": "https://arxiv.org/abs/math/0701789", "size": 9.5}),
        ("）；orbifold 情形可看 Kriz–Pando Zayas–Quiroz 的系统讨论（", {"size": 9.5, "color": GRAY}),
        ("hep-th/0703122", {"link": "https://arxiv.org/abs/hep-th/0703122", "size": 9.5}),
        ("）。本文按“源头论文 + 数学综述”处理，不把它们标成物理综述。",
         {"size": 9.5, "color": GRAY}),
    ])

    DOC.add_heading("4.3　快子凝聚与 Sen 猜想", level=2)
    body([
        "这是本专题的第二个核心。建议顺序：先读 Sen 1998 的原始猜想，再看普适性论证与数值检验，"
        "然后读 Taylor–Zwiebach 的讲义把形式体系补齐，最后读 Schnabl 的解析证明和 Sen 的大综述。",
    ])
    for e in GROUP_C:
        lit_entry(e)

    DOC.add_heading("4.4　讲义与背景", level=2)
    body([
        "讲义与背景材料：适合补基础或换角度。Schwarz 的 TASI 讲义覆盖非 BPS 与 type I；"
        "Harvey 的讲义连接非交换几何；Johnson 与 Polchinski 的 D-膜讲义是通用背景；"
        "Douglas 的论文指向导出范畴这一邻近方向。",
    ])
    for e in GROUP_D:
        lit_entry(e)


# ----------------------------------------------------------------------------
# section 5 - Sen conjecture page
# ----------------------------------------------------------------------------
def sec5():
    DOC.add_heading("五、Sen 猜想专页", level=1)
    DOC.add_heading("5.1　猜想说什么", level=2)
    body([
        "Sen 的猜想通常表述为三条（以玻色弦或 II 型理论中的不稳定 D-膜系统为背景）：",
    ])
    bullet([
        ("(S1) 势极小抵消张力：", {"bold": True, "color": NAVY}),
        ("在 Dp–反 Dp 系统上，快子势 V(T) 的极小值满足 V_min + 2T_p = 0；在单个非 BPS "
         "D-膜上满足 V_min + T_p = 0。因此在极小处能量密度为零，系统恢复超对称"
         "（对 brane–antibrane 而言）或到达闭弦真空（对非 BPS 膜而言）。", {}),
    ])
    bullet([
        ("(S2) 降维关系（descent relations）：", {"bold": True, "color": NAVY}),
        ("D(p-2)-膜可以实现为 Dp–反 Dp 对上快子场的扭结/涡旋解；更一般地，低维 D-膜是"
         "快子凝聚的拓扑孤子，其张力与高维膜张力之比由已知公式给出。", {}),
    ])
    bullet([
        ("(S3) 非 BPS D-膜的完全衰变：", {"bold": True, "color": NAVY}),
        ("非 BPS D-膜上的快子凝聚最终衰变到没有 D-膜的真空（快子真空），"
         "能量以闭弦辐射形式释放。", {}),
    ])

    DOC.add_heading("5.2　为什么它是 K-理论分类的动力学基础", level=2)
    body([
        "K-理论把 D-膜荷定义为 brane–antibrane 对的等价类，等价关系 (E,F) ~ (E⊕G, F⊕G) "
        "的物理实现，就是带丛 G 的膜–反膜对的产生与湮灭。Sen 猜想保证这一过程在能量上是"
        "自洽的：势极小处能量恰为零，因此膜–反膜对可以“无代价”地消失，K-理论等价不是"
        "形式游戏。降维关系进一步说明，为什么只靠 D9–反 D9 对就能生成所有 D-膜荷——"
        "低维膜正是快子凝聚的孤子。",
    ])
    body([
        "反过来，K-理论分类的边界（例如存在 H-流、S-对偶、自对偶 RR 场时哪些荷被分类）"
        "也正是检验 Sen 猜想适用范围的物理问题，Evslin 的综述对此有系统讨论。",
    ])

    DOC.add_heading("5.3　检验与证明的里程碑", level=2)
    headers = ["年份", "工作", "结果/意义"]
    rows = [
        ["1998", "Sen, hep-th/9805170", "提出 brane–antibrane 快子势极小处能量抵消猜想（S1）"],
        ["1999", "Sen, hep-th/9911116", "论证快子势的普适性，与边界 CFT 无关"],
        ["1999–2000", "Sen–Zwiebach, hep-th/9912249", "立方开弦场论能级截断：70% → 99% 张力抵消"],
        ["2003", "Taylor–Zwiebach, hep-th/0311017", "TASI 讲义系统陈述 Sen 三猜想及其证据"],
        ["2005", "Sen, hep-th/0410103", "169 页综述整理快子动力学与开弦完备性猜想"],
        ["2006", "Schnabl, hep-th/0511286", "解析构造快子真空，证明 Sen 第一猜想"],
        ["2024", "Sen–Zwiebach, 2405.19421", "172 页 SFT 综述，给出当代完整图景"],
    ]
    make_table(headers, rows, [2.0, 5.4, 9.2], font_size=8.8)
    spacer(2)

    DOC.add_heading("5.4　仍未完结的问题", level=2)
    bullet([("时间依赖的快子凝聚与闭弦产生，其定量描述仍不完整；", {})])
    bullet([("闭弦快子凝聚的物理意义，以及它与开弦图景的统一；", {})])
    bullet([("H-流、非交换、orientifold 背景下 K-理论分类的完整形式与 S-对偶相容性"
             "（Evslin 2006 指出若干分类提案的困难）；", {})])
    bullet([("开弦场论非微扰定义的严格性，以及 Witten 2000 提出的大 N 极限问题。", {})])


# ----------------------------------------------------------------------------
# section 6 - reading routes
# ----------------------------------------------------------------------------
def sec6():
    DOC.add_heading("六、阅读路线", level=1)
    body([
        "不同背景的读者可以走不同路线。括号内是粗略时间估计，按每天 2–3 小时计。",
    ])

    DOC.add_heading("路线 A　物理人快线（约 1–2 周）", level=2)
    steps = [
        ("Witten 2000（1–2 小时）：", "先建立 K-理论分类的全景。"),
        ("Witten 1998 第 1–4 节（半天）：", "看分类如何被论证出来。"),
        ("Moore 2003（1–2 天）：", "理解物理上为什么必须是 K-理论。"),
        ("Sen 1998（1 小时）：", "快子凝聚猜想的原始陈述。"),
        ("Sen–Zwiebach 2000（2–3 小时）：", "看数值证据如何给出。"),
        ("Taylor–Zwiebach 2003（2–3 天，选读）：", "把开弦场论的形式体系补齐。"),
        ("Schnabl 2006（1–2 天，先读引言与结论）：", "解析证明的核心思路。"),
        ("Sen 2005 综述：", "当作参考书，按需查阅具体章节。"),
    ]
    for i, (a, b) in enumerate(steps, 1):
        bullet([(f"{i}. ", {"bold": True, "color": BLUE}),
                (a, {"bold": True}), (b, {})])

    DOC.add_heading("路线 B　数学人路线（约 1 周）", level=2)
    steps = [
        ("Olsen–Szabo 1999 第 2–4 节：", "拓扑 K-理论的数学基础。"),
        ("Szabo 2002：", "K-同调的短综述。"),
        ("Szabo 2008：", "KK-理论与非交换推广。"),
        ("Moore 2003 + Witten 1998：", "补物理动机与分类陈述。"),
    ]
    for i, (a, b) in enumerate(steps, 1):
        bullet([(f"{i}. ", {"bold": True, "color": BLUE}),
                (a, {"bold": True}), (b, {})])

    DOC.add_heading("路线 C　只关心快子凝聚（约 1 周）", level=2)
    steps = [
        ("Sen 2005 综述第 1–3 节：", "先看全局图景。"),
        ("Sen 1999 APCTP 讲义：", "非 BPS 与降维关系。"),
        ("Sen 1998 + Sen 1999 普适性：", "猜想本身。"),
        ("Sen–Zwiebach 2000：", "定量检验。"),
        ("Taylor–Zwiebach 2003：", "把前面串成完整体系。"),
        ("Schnabl 2006：", "解析证明。"),
        ("Sen–Zwiebach 2024（选读）：", "当代视角与后续发展。"),
    ]
    for i, (a, b) in enumerate(steps, 1):
        bullet([(f"{i}. ", {"bold": True, "color": BLUE}),
                (a, {"bold": True}), (b, {})])

    DOC.add_heading("路线 D　只有一个晚上", level=2)
    body([
        "Witten 2000 全文 + Moore 2003 引言 + Sen 2005 综述引言。足以在第二天和别人讨论"
        "“K-理论为什么能分类 D-膜荷”以及“Sen 猜想在说什么”。",
    ])


# ----------------------------------------------------------------------------
# section 7 - glossary
# ----------------------------------------------------------------------------
def sec7():
    DOC.add_heading("七、名词速查", level=1)
    headers = ["术语", "一句话解释"]
    rows = [
        ["K^0(X)", "复向量丛的 Grothendieck 群；IIB 型 D-膜荷的取值群。"],
        ["K^1(X)", "与 K^0 相差一个 Bott 周期；IIA 型 D-膜荷的取值群。"],
        ["KO(X)", "实 K-理论；type I 型理论中 D-膜荷的取值群。"],
        ["KR(X)", "带对合的实 K-理论；orientifold 背景中使用。"],
        ["扭曲 K-理论 K_H(X)", "H-流（B-场）非平凡时替代普通 K-理论的分类群。"],
        ["K-同调", "K-理论的对偶同调理论；D-膜作为“同调式”对象更自然。"],
        ["KK-理论", "Kasparov 的双变 K-理论；统一 K-理论与 K-同调，并推广到非交换代数。"],
        ["RR 荷", "D-膜携带的 Ramond–Ramond 荷；由 K-理论类刻画。"],
        ["Chan–Paton 丛", "D-膜世界体上的规范丛；其 K-理论类决定 D-膜荷。"],
        ["brane–antibrane 对", "D-膜与反 D-膜组成的系统，带快子模，可湮灭。"],
        ["快子凝聚", "快子场获得期望值、系统衰变到更低能量组态的过程。"],
        ["Sen 猜想", "快子势极小处能量恰好抵消膜张力（S1），并有降维关系等推论。"],
        ["能级截断", "在开弦场论中按质量能级截断求数值解的方法。"],
        ["立方开弦场论", "Witten 1986 年提出的开弦场论；Sen 猜想的解析证明在此框架完成。"],
        ["BSFT", "边界弦场论（boundary string field theory），给出快子势的精确形式。"],
        ["Freed–Witten 反常", "D-膜世界体整体反常；其抵消条件与 K-理论分类密切相关。"],
    ]
    make_table(headers, rows, [4.6, 12.0], font_size=8.8)
    spacer(2)


# ----------------------------------------------------------------------------
# section 8 - full arXiv list
# ----------------------------------------------------------------------------
ARXIV_LIST = [
    ("hep-th/0007175", "Witten, Overview of K-Theory Applied To Strings (2000)"),
    ("hep-th/0304018", "Moore, K-Theory from a Physical Perspective (2003)"),
    ("hep-th/9907140", "Olsen & Szabo, Constructing D-Branes from K-Theory (1999)"),
    ("hep-th/9710230", "Minasian & Moore, K-theory and Ramond-Ramond Charge (1997)"),
    ("hep-th/9810188", "Witten, D-Branes And K-Theory (1998)"),
    ("hep-th/9812135", "Horava, Type IIA D-Branes, K-Theory, and Matrix Theory (1998)"),
    ("hep-th/9912279", "Moore & Witten, Self-Duality, RR Fields, and K-Theory (1999)"),
    ("hep-th/0209210", "Szabo, D-Branes, Tachyons and K-Homology (2002)"),
    ("0809.3029", "Szabo, D-branes and Bivariant K-Theory (2008)"),
    ("hep-th/0610328", "Evslin, What Does(n't) K-Theory Classify? (2006)"),
    ("hep-th/9909089", "Kapustin, D-branes in a Topologically Nontrivial B-Field (1999)"),
    ("hep-th/9907189", "Freed & Witten, Anomalies in String Theory with D-Branes (1999)"),
    ("hep-th/9805170", "Sen, Tachyon Condensation on the Brane Antibrane System (1998)"),
    ("hep-th/9911116", "Sen, Universality of the Tachyon Potential (1999)"),
    ("hep-th/9912249", "Sen & Zwiebach, Tachyon Condensation in String Field Theory (1999)"),
    ("hep-th/0511286", "Schnabl, Analytic Solution for Tachyon Condensation in Open SFT (2005)"),
    ("hep-th/0311017", "Taylor & Zwiebach, D-Branes, Tachyons, and String Field Theory (2003)"),
    ("hep-th/0410103", "Sen, Tachyon Dynamics in Open String Theory (2004)"),
    ("hep-th/9904207", "Sen, Non-BPS States and Branes in String Theory (1999)"),
    ("2405.19421", "Sen & Zwiebach, String Field Theory: A Review (2024)"),
    ("hep-th/9908144", "Schwarz, TASI Lectures on Non-BPS D-Brane Systems (1999)"),
    ("hep-th/0102076", "Harvey, Komaba Lectures on Noncommutative Solitons and D-Branes (2001)"),
    ("hep-th/0007130", "Schwarz, Recent Progress in Superstring Theory (2000)"),
    ("hep-th/0007170", "Johnson, D-Brane Primer (2000)"),
    ("hep-th/9611050", "Polchinski, TASI Lectures on D-Branes (1996)"),
    ("hep-th/0011017", "Douglas, D-branes, Categories and N=1 Supersymmetry (2000)"),
]


def sec8():
    DOC.add_heading("八、arXiv 链接总表", level=1)
    body([
        "以下按文中出现顺序汇总，方便复制与检索。点击“arXiv”列可打开 abs 页面。",
    ])
    headers = ["#", "arXiv 编号", "标题（简）", "链接"]
    rows = []
    for i, (aid, title) in enumerate(ARXIV_LIST, 1):
        rows.append([
            str(i),
            aid,
            title,
            [("arXiv", {"link": "https://arxiv.org/abs/" + aid})],
        ])
    make_table(headers, rows, [0.9, 3.2, 9.3, 3.2], font_size=8.6)
    spacer(2)


# ----------------------------------------------------------------------------
# section 9 - verification notes
# ----------------------------------------------------------------------------
def sec9():
    DOC.add_heading("九、核验说明", level=1)
    body([
        "本文档所有 arXiv 编号、标题、作者与期刊信息，均于 2026 年 11 月 6 日通过 arXiv API"
        "（export.arxiv.org/api/query）逐条核验；期刊卷页以 arXiv 元数据为准，"
        "预印本与讲义条目未标注期刊。读者可把任意编号输入 arXiv 搜索框，或直接点击文中链接。",
    ])
    bullet([
        ("度数约定：", {"bold": True}),
        ("K-理论分类的度数在不同文献间可能相差一个 Bott 平移。本文采用 Witten 2000 的约定："
         "IIB 的 D-膜荷在 K^0、RR 场在 K^1；IIA 的 D-膜荷在 K^1、RR 场在 K^0。", {}),
    ])
    bullet([
        ("综述与原始研究的区分：", {"bold": True}),
        ("Witten 的 K-理论综述是 hep-th/0007175，Moore 的是 hep-th/0304018（另有 10 页速览版"
         " hep-th/0012007）；hep-th/9810188 与 hep-th/9710230 是奠基性原始论文，"
         "不是综述。本文已按此标注。", {}),
    ])
    bullet([
        ("覆盖缺口：", {"bold": True}),
        ("扭曲 K-理论与 orientifold 没有面向物理读者的专门长综述；本文以源头论文、"
         "数学综述与短报告作为入口（见 4.2 末段），并明确说明这一点。", {}),
    ])
    bullet([
        ("严格性边界：", {"bold": True}),
        ("Sen 猜想的解析证明主要针对玻色弦与 II 型理论中的不稳定 D-膜系统；"
         "闭弦快子、时间依赖过程与一般 H-流背景仍属前沿。", {}),
    ])


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------
def main():
    global DOC
    DOC = Document()
    cp = DOC.core_properties
    cp.title = "弦论中的 K-理论：D-膜、RR 荷与快子凝聚——专题综述选读"
    cp.author = "DSH 文献整理"
    cp.subject = "K-theory in string theory: reading dossier"
    cp.keywords = ("K-theory; D-branes; Ramond-Ramond charge; "
                   "tachyon condensation; Sen conjecture; arXiv")

    setup()
    cover()
    contents()
    sec1()
    sec2()
    sec3()
    sec4()
    sec5()
    sec6()
    sec7()
    sec8()
    sec9()

    DOC.save(DOCX_PATH)
    print("saved:", DOCX_PATH)
    print("size_bytes:", os.path.getsize(DOCX_PATH))

    # reopen and verify
    d2 = Document(DOCX_PATH)
    print("paragraphs:", len(d2.paragraphs))
    print("tables:", len(d2.tables))
    xml = d2.element.xml
    print("hyperlinks:", xml.count("w:hyperlink"))
    txt = "\n".join(p.text for p in d2.paragraphs)
    for k in ("弦论中的 K-理论", "Sen 猜想", "hep-th/9810188", "Olsen–Szabo"):
        print("contains", repr(k), ":", k in txt)


if __name__ == "__main__":
    main()
