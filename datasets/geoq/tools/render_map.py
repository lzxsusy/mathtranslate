#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成几何量子化框架地图：map.svg + map.png。

布局全部写死在 LAYOUT 里，SVG 与 PNG 共用同一套坐标，保证两种格式一致。
用法：python tools/render_map.py [--out DIR]
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

W, H = 1760, 1120

TRACK = {
    "A": {"name": "A 辛几何", "stroke": "#2f6fb0", "fill": "#e9f1fb"},
    "B": {"name": "B 半经典", "stroke": "#b06a2f", "fill": "#fbf1e6"},
    "C": {"name": "C 表示论", "stroke": "#2f8f6a", "fill": "#e7f5ee"},
    "D": {"name": "D 量子化机器", "stroke": "#7a4fa0", "fill": "#f1eaf8"},
    "X": {"name": "出口", "stroke": "#555f6d", "fill": "#f2f4f7"},
}

INK = "#1f2430"
MUTED = "#59616e"
PANEL = "#fcfcfd"
PANEL_BORDER = "#d7dce4"

# key: (label, track, x, y, w, h, font_size)
NODES = {
    # A 面板
    "A6": ("辛流形 (M,ω)\n相空间", "A", 60, 175, 250, 56, 19),
    "A7": ("哈密顿向量场\n与泊松括号", "A", 330, 175, 250, 56, 19),
    "A8": ("余切丛 T*X\n刘维尔形式 θ", "A", 60, 250, 250, 56, 19),
    "A9": ("拉格朗日子流形\n可投影 · 相函数", "A", 330, 250, 250, 56, 19),
    "A10": ("辛同胚\n与哈密顿流", "A", 60, 325, 250, 56, 19),
    "A5": ("马斯洛夫指标\nL(V) 的基本群", "A", 330, 325, 250, 56, 19),
    "A0": ("A1–A4 线性底座：辛向量空间 · Sp(V) · 相容复结构 · L(V)", "A", 60, 400, 520, 50, 17),
    # B 面板
    "B1": ("WKB 解与\n哈密顿–雅可比方程", "B", 680, 175, 360, 56, 19),
    "B2": ("密度、半密度\n与刘维尔测度", "B", 680, 250, 360, 56, 19),
    "B3": ("玻尔–索末菲\n量子化条件", "B", 680, 325, 360, 56, 19),
    "B4": ("马斯洛夫修正\n与 EBK 条件", "B", 680, 400, 360, 56, 19),
    # C 面板
    "C1": ("海森堡李代数 h_V", "C", 1120, 175, 260, 56, 19),
    "C2": ("海森堡群 H_V\n中心扩张", "C", 1410, 175, 290, 56, 19),
    "C3": ("薛定谔表示 T_ℏ", "C", 1120, 250, 260, 56, 19),
    "C4": ("斯通–冯·诺依曼\n定理", "C", 1410, 250, 290, 56, 19),
    "C5": ("Segal–Bargmann / Fock 表示", "C", 1120, 325, 580, 56, 19),
    "C0": ("两个模型由 BKS 核联系（书中只给思路）", "C", 1120, 400, 580, 50, 17),
    # D 面板
    "D1": ("狄拉克量子化原理\nQ1–Q5", "D", 60, 600, 290, 64, 19),
    "D2": ("格罗嫩沃尔德–范霍夫\n不可行定理", "D", 380, 600, 290, 64, 19),
    "D3": ("预量子化线丛 (L,∇)\nF_∇ = −(i/ℏ)ω", "D", 700, 600, 290, 64, 19),
    "D4": ("可量子化条件\n(1/2πℏ)∫ω ∈ Z", "D", 1020, 600, 290, 64, 19),
    "D5": ("极化 P\n实 / 凯勒", "D", 1340, 600, 320, 64, 19),
    "D6": ("量子希尔伯特空间  Γ_P(L ⊗ √K_M)\n（半形式修正）", "D", 700, 710, 520, 64, 19),
    "D7": ("量子算子 Q(f) = iℏ∇_{V_f} + f\n（f 为 P-保持）", "D", 1340, 710, 320, 64, 18),
    # 出口
    "E1": ("谐振子：E_n = (n+½)ℏω", "X", 60, 860, 420, 56, 19),
    "E2": ("S²：可量子化 ⟺ A ∈ (ℏ/2)Z", "X", 510, 860, 420, 56, 19),
    "E3": ("T*X：总可量子化（θ 恰当）", "X", 960, 860, 700, 56, 19),
}

# 面板：x,y,w,h,标题
PANELS = [
    (40, 120, 580, 360, "A · 相空间的辛几何（§5.1）"),
    (650, 120, 420, 360, "B · 几何半经典量子化（§5.2）"),
    (1100, 120, 620, 360, "C · 海森堡群与表示（§5.3）"),
    (40, 550, 1680, 500, "D · 几何量子化机器（§5.4）"),
]

# 面板内连线
EDGES = [
    ("A6", "A7"), ("A6", "A8"), ("A8", "A9"), ("A0", "A5"),
    ("B1", "B2"), ("B2", "B3"), ("B3", "B4"),
    ("C1", "C2"), ("C1", "C3"), ("C2", "C4"), ("C3", "C5"), ("C4", "C5"),
    ("D1", "D2"), ("D2", "D3"), ("D3", "D4"), ("D4", "D5"),
    ("D3", "D6"), ("D5", "D7"), ("D6", "D7"),
]

# 跨面板箭头：((x1,y1),(x2,y2),label)
CROSS = [
    ((330, 480), (330, 550), "辛流形 (M,ω)"),
    ((860, 480), (860, 550), "半密度 + Maslov"),
    ((1400, 480), (1400, 550), "正则对易关系"),
]


def _font(size: int, bold: bool = False):
    from PIL import ImageFont

    cands = [
        os.environ.get("GEOQ_FONT_BOLD" if bold else "GEOQ_FONT", ""),
        r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\msyh.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/System/Library/Fonts/PingFang.ttc",
    ]
    for c in cands:
        if c and Path(c).exists():
            try:
                return ImageFont.truetype(c, size, index=0)
            except OSError:
                continue
    return ImageFont.load_default()


# 微软雅黑缺 ℏ ⊗ ∇ ⟺ 等数学符号，逐字符回退到 Cambria Math 以保证 PNG 不出豆腐块。
MATH_SYMBOLS = set("ℏ⊗∫∇∈√⟺⇔⇒≤≥≠∂∞−×·½²³ⁿ")
_MATH_FONT = None


def _math_font(size: int):
    global _MATH_FONT
    from PIL import ImageFont

    if _MATH_FONT is None:
        for p, idx in [(r"C:\Windows\Fonts\cambria.ttc", 0), (r"C:\Windows\Fonts\seguisym.ttf", 0)]:
            if Path(p).exists():
                try:
                    _MATH_FONT = (p, idx)
                    break
                except OSError:
                    pass
    if _MATH_FONT is None:
        return _font(size)
    return ImageFont.truetype(_MATH_FONT[0], max(size - 1, 8), index=_MATH_FONT[1])


def _run_font(ch: str, size: int, bold: bool):
    return _math_font(size) if ch in MATH_SYMBOLS else _font(size, bold)


def _line_width(text: str, size: int, bold: bool = False) -> float:
    total = 0.0
    for ch in text:
        total += _run_font(ch, size, bold).getlength(ch)
    return total


def _draw_line(d, x, y, text, size, bold=False, fill=INK):
    for ch in text:
        f = _run_font(ch, size, bold)
        d.text((x, y), ch, font=f, fill=fill)
        x += f.getlength(ch)
    return x


def _draw_center(d, cx, y, text, size, bold=False, fill=INK):
    _draw_line(d, cx - _line_width(text, size, bold) / 2, y, text, size, bold, fill)


def _center(box):
    x, y, w, h = box
    return x + w / 2, y + h / 2


def _edge_points(a, b):
    ax, ay, aw, ah = NODES[a][2:6]
    bx, by, bw, bh = NODES[b][2:6]
    acx, acy = ax + aw / 2, ay + ah / 2
    bcx, bcy = bx + bw / 2, by + bh / 2
    if abs(bcx - acx) >= abs(bcy - acy):
        return ((ax + aw, acy), (bx, bcy)) if bcx > acx else ((ax, acy), (bx + bw, bcy))
    return ((acx, ay + ah), (bcx, by)) if bcy > acy else ((acx, ay), (bcx, by + bh))


def _arrowhead(p1, p2, size=11):
    import math

    x1, y1 = p1
    x2, y2 = p2
    ang = math.atan2(y2 - y1, x2 - x1)
    a = ang + math.radians(150)
    b = ang - math.radians(150)
    return [
        (x2, y2),
        (x2 + size * math.cos(a), y2 + size * math.sin(a)),
        (x2 + size * math.cos(b), y2 + size * math.sin(b)),
    ]


def _panel_label(draw, text, x, y, font):
    draw.text((x, y), text, font=font, fill=INK)


def draw_png(path: Path):
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(img)
    f_title = _font(40, True)
    f_sub = _font(19)
    f_head = _font(22, True)
    f_legend = _font(18)
    f_note = _font(16)

    d.text((50, 26), "几何量子化 · 框架地图", font=f_title, fill=INK)
    d.text((52, 82), "李思《量子力学与几何》第 5 章 · 从相空间到量子希尔伯特空间的三条线索与一台机器", font=f_sub, fill=MUTED)

    for (x, y, w, h, title) in PANELS:
        d.rounded_rectangle((x, y, x + w, y + h), radius=14, fill=PANEL, outline=PANEL_BORDER, width=2)
        _draw_line(d, x + 20, y + 14, title, 22, True, INK)

    # 连线（先画线，再画节点，避免压住边框）
    for a, b in EDGES:
        p1, p2 = _edge_points(a, b)
        d.line((p1, p2), fill="#98a2b3", width=2)
        d.polygon(_arrowhead(p1, p2), fill="#98a2b3")
    for p1, p2, label in CROSS:
        d.line((p1, p2), fill="#7d8798", width=3)
        d.polygon(_arrowhead(p1, p2, 13), fill="#7d8798")
        lx = p1[0] + 10
        ly = (p1[1] + p2[1]) / 2 - 9
        d.rectangle((lx - 4, ly - 2, lx + _line_width(label, 16) + 4, ly + 20), fill="#ffffff")
        _draw_line(d, lx, ly, label, 16, False, MUTED)

    for key, (label, track, x, y, w, h, size) in NODES.items():
        c = TRACK[track]
        d.rounded_rectangle((x, y, x + w, y + h), radius=10, fill=c["fill"], outline=c["stroke"], width=2)
        lines = label.split("\n")
        lh = size + 7
        total = lh * len(lines)
        ty = y + (h - total) / 2 + 1
        for line in lines:
            _draw_center(d, x + w / 2, ty, line, size, bold=(key in ("A0", "C0")), fill=INK)
            ty += lh

    # 出口说明
    _draw_line(d, 60, 832, "三个出口例子", 22, True, INK)

    # 缺口框
    d.rounded_rectangle((60, 940, 1680, 1010), radius=10, fill="#fffaf0", outline="#d9b26a", width=2)
    _draw_line(d, 80, 953, "书中只给思路 / 未展开：BKS 核（不同极化之间搬运算子）·  半形式线丛 √K_M 的存在性（metaplectic 结构）", 16, False, "#7a5a1e")

    # 图例
    lx = 60
    for t in ["A", "B", "C", "D", "X"]:
        c = TRACK[t]
        d.rounded_rectangle((lx, 1060, lx + 22, 1082), radius=5, fill=c["fill"], outline=c["stroke"], width=2)
        _draw_line(d, lx + 30, 1060, c["name"], 18, False, INK)
        lx += 30 + _line_width(c["name"], 18) + 34
    _draw_line(d, 1180, 1060, "完整 48 张卡见 taxonomy.md · 本图由 tools/render_map.py 生成", 18, False, MUTED)

    img.save(path)
    return path


def _svg_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def draw_svg(path: Path):
    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    out.append('<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#98a2b3"/></marker>'
               '<marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#7d8798"/></marker></defs>')
    out.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    out.append(f'<text x="50" y="58" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="40" font-weight="700" fill="{INK}">几何量子化 · 框架地图</text>')
    out.append(f'<text x="52" y="100" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="19" fill="{MUTED}">李思《量子力学与几何》第 5 章 · 从相空间到量子希尔伯特空间的三条线索与一台机器</text>')

    for (x, y, w, h, title) in PANELS:
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{PANEL}" stroke="{PANEL_BORDER}" stroke-width="2"/>')
        out.append(f'<text x="{x+20}" y="{y+32}" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="22" font-weight="700" fill="{INK}">{_svg_escape(title)}</text>')

    for a, b in EDGES:
        (x1, y1), (x2, y2) = _edge_points(a, b)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#98a2b3" stroke-width="2" marker-end="url(#arrow)"/>')

    for (x1, y1), (x2, y2), label in CROSS:
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#7d8798" stroke-width="3" marker-end="url(#arrow2)"/>')
        out.append(f'<text x="{x1+10}" y="{(y1+y2)/2+6}" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="16" fill="{MUTED}">{_svg_escape(label)}</text>')

    for key, (label, track, x, y, w, h, size) in NODES.items():
        c = TRACK[track]
        out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c["fill"]}" stroke="{c["stroke"]}" stroke-width="2"/>')
        lines = label.split("\n")
        lh = size + 7
        ty = y + (h - lh * len(lines)) / 2 + size
        weight = ' font-weight="700"' if key in ("A0", "C0") else ""
        out.append(f'<text x="{x + w/2}" y="{ty:.1f}" text-anchor="middle" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="{size}"{weight} fill="{INK}">')
        for i, line in enumerate(lines):
            dy = 0 if i == 0 else lh
            out.append(f'<tspan x="{x + w/2}" dy="{dy}">{_svg_escape(line)}</tspan>')
        out.append('</text>')

    out.append(f'<text x="60" y="855" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="22" font-weight="700" fill="{INK}">三个出口例子</text>')
    out.append(f'<rect x="60" y="940" width="1620" height="70" rx="10" fill="#fffaf0" stroke="#d9b26a" stroke-width="2"/>')
    out.append(f'<text x="80" y="972" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="16" fill="#7a5a1e">书中只给思路 / 未展开：BKS 核（不同极化之间搬运算子）·  半形式线丛 √K_M 的存在性（metaplectic 结构）</text>')

    lx = 60
    for t in ["A", "B", "C", "D", "X"]:
        c = TRACK[t]
        out.append(f'<rect x="{lx}" y="1060" width="22" height="22" rx="5" fill="{c["fill"]}" stroke="{c["stroke"]}" stroke-width="2"/>')
        out.append(f'<text x="{lx+30}" y="1077" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="18" fill="{INK}">{_svg_escape(c["name"])}</text>')
        lx += 30 + len(c["name"]) * 19 + 34
    out.append(f'<text x="1180" y="1077" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="18" fill="{MUTED}">完整 48 张卡见 taxonomy.md · 本图由 tools/render_map.py 生成</text>')
    out.append('</svg>')
    path.write_text("\n".join(out), encoding="utf-8")
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    print(draw_svg(out / "map.svg"))
    print(draw_png(out / "map.png"))


if __name__ == "__main__":
    main()
