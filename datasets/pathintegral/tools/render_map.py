#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成路径积分框架地图：map.svg + map.png。

布局全部写死在 NODES/PANELS/EDGES 里，SVG 与 PNG 共用同一套坐标。
用法：python tools/render_map.py [--out DIR]
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

W, H = 1760, 1120

TRACK = {
    "A": {"name": "A 基础与时间切片", "stroke": "#2f6fb0", "fill": "#e9f1fb"},
    "B": {"name": "B 高斯与谐振子", "stroke": "#b06a2f", "fill": "#fbf1e6"},
    "C": {"name": "C 渐近与半经典", "stroke": "#2f8f6a", "fill": "#e7f5ee"},
    "D": {"name": "D 格林函数与 WKB", "stroke": "#7a4fa0", "fill": "#f1eaf8"},
    "E": {"name": "E 微扰与代数", "stroke": "#a03f5f", "fill": "#fbeaf0"},
    "X": {"name": "出口", "stroke": "#555f6d", "fill": "#f2f4f7"},
}

INK = "#1f2430"
MUTED = "#59616e"
PANEL = "#fcfcfd"
PANEL_BORDER = "#d7dce4"

# key: (label, track, x, y, w, h, font_size)
NODES = {
    # A 面板
    "A1": ("费曼核 K\n路径积分", "A", 60, 180, 220, 56, 19),
    "A2": ("位置 / 动量表示", "A", 300, 180, 230, 56, 19),
    "A3": ("时间切片\n多重积分", "A", 60, 255, 220, 56, 19),
    "A4": ("路径积分定义\n复合律", "A", 300, 255, 230, 56, 19),
    "A5": ("自由粒子核", "A", 60, 330, 220, 56, 19),
    "A6": ("虚时间 / Wick", "A", 300, 330, 230, 56, 19),
    "A0": ("A 轨：定义与可算的入口", "A", 60, 405, 470, 48, 17),
    # B 面板
    "B1": ("高斯积分\n命题 2.3.1", "B", 600, 180, 200, 56, 19),
    "B2": ("zeta 正则化\ndet A = exp(−ζ′(0))", "B", 820, 180, 200, 56, 17),
    "B3": ("谐振子核\n精确传播子", "B", 600, 265, 200, 56, 19),
    "B4": ("配分函数\nZ = 1/(2sinh(βℏω/2))", "B", 820, 265, 200, 66, 17),
    "B0": ("B 轨：可精确求和的高斯模型", "B", 600, 405, 420, 48, 17),
    # C 面板
    "C1": ("拉普拉斯方法", "C", 1090, 180, 220, 50, 19),
    "C2": ("最速下降", "C", 1330, 180, 150, 50, 19),
    "C3": ("莫尔斯流\n斯托克斯现象", "C", 1500, 180, 200, 50, 18),
    "C4": ("艾里函数\n斯托克斯射线", "C", 1090, 250, 220, 56, 18),
    "C5": ("半经典费曼核\n驻定相位 + Maslov", "C", 1330, 250, 370, 56, 18),
    "C6": ("雅可比场\nVan Vleck 行列式", "C", 1090, 325, 220, 56, 18),
    "C7": ("时间切片行列式", "C", 1330, 325, 370, 56, 18),
    "C0": ("C 轨：ℏ → 0 的渐近机器", "C", 1090, 405, 610, 48, 17),
    # D 面板
    "D1": ("固定能量格林函数\nG(E) = ∫dT exp(iET/ℏ) K", "D", 60, 590, 250, 64, 16),
    "D2": ("半经典格林函数\n鞍点 · 经典旅行时间", "D", 330, 590, 250, 64, 17),
    "D3": ("WKB 波函数\np(x) = √(2m(E−V))", "D", 600, 590, 250, 64, 17),
    "D4": ("量子隧穿\n透射系数", "D", 60, 695, 250, 64, 18),
    "D5": ("连接公式\nAiry 匹配", "D", 330, 695, 250, 64, 18),
    "D0": ("D 轨：从核到谱与隧穿", "D", 600, 695, 250, 64, 17),
    # E 面板
    "E1": ("威克定理\n配对求和", "E", 920, 585, 240, 60, 18),
    "E2": ("费曼图展开\nAut(Γ) 与权重", "E", 1180, 585, 240, 60, 17),
    "E3": ("外尔量子化\nMoyal 乘积", "E", 1440, 585, 260, 60, 18),
    "E4": ("S¹ 关联\nG(θ) 与量子化乘法", "E", 920, 680, 240, 60, 17),
    "E5": ("Hochschild 同调\nHH_p(A) = Ω^p(A)", "E", 1180, 680, 240, 60, 17),
    "E6": ("量子 HKR", "E", 1440, 680, 260, 60, 19),
    # 出口
    "O1": ("谐振子能谱\nE_n = (n+½)ℏω", "X", 60, 835, 410, 60, 18),
    "O2": ("隧穿与连接\n透射系数 · Stokes 跳跃", "X", 500, 835, 430, 60, 17),
    "O3": ("量子化乘法\nMoyal ⋆ · 量子 HKR", "X", 960, 835, 740, 60, 18),
}

# 面板：x,y,w,h,标题
PANELS = [
    (40, 120, 500, 360, "A · 路径积分与时间切片（§2.1–§2.2）"),
    (560, 120, 480, 360, "B · 高斯路径积分与谐振子（§2.3–§2.4）"),
    (1060, 120, 660, 360, "C · 渐近方法与半经典（§2.5–§2.6）"),
    (40, 520, 830, 300, "D · 格林函数、WKB 与隧穿（§2.7）"),
    (900, 520, 820, 300, "E · 微扰展开与代数结构（§2.8）"),
]

# 面板内连线
EDGES = [
    ("A1", "A2"), ("A1", "A3"), ("A3", "A4"), ("A4", "A5"), ("A4", "A6"),
    ("B1", "B2"), ("B1", "B3"), ("B3", "B4"),
    ("C1", "C2"), ("C1", "C3"), ("C1", "C4"), ("C1", "C5"),
    ("C5", "C6"), ("C5", "C7"),
    ("D1", "D2"), ("D2", "D3"), ("D4", "D5"), ("D2", "D5"),
    ("E1", "E2"), ("E2", "E3"), ("E1", "E4"), ("E4", "E5"), ("E5", "E6"),
]

# 跨面板箭头：((x1,y1),(x2,y2),label)
CROSS = []

# 出口箭头
OUT = [
    ("B3", "O1", "能谱"),
    ("D4", "O2", "隧穿"),
    ("E6", "O3", "量子化乘法"),
]


def _font(size: int, bold: bool = False):
    from PIL import ImageFont

    cands = [
        os.environ.get("PI_FONT_BOLD" if bold else "PI_FONT", ""),
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


# 微软雅黑缺 ℏ ∫ ∇ ∈ √ ⇔ 等数学符号，逐字符回退到 Cambria Math，避免 PNG 出现豆腐块。
MATH_SYMBOLS = set("ℏ⊗∫∇∈√⟺⇔⇒≤≥≠∂∞−×·½²³ⁿζΩΓ⋆αβεπθ")
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
    return sum(_run_font(ch, size, bold).getlength(ch) for ch in text)


def _draw_line(d, x, y, text, size, bold=False, fill=INK):
    for ch in text:
        f = _run_font(ch, size, bold)
        d.text((x, y), ch, font=f, fill=fill)
        x += f.getlength(ch)
    return x


def _draw_center(d, cx, y, text, size, bold=False, fill=INK):
    _draw_line(d, cx - _line_width(text, size, bold) / 2, y, text, size, bold, fill)


def _edge_points(a, b, nodes=None):
    nodes = nodes or NODES
    ax, ay, aw, ah = nodes[a][2:6]
    bx, by, bw, bh = nodes[b][2:6]
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


def draw_png(path: Path):
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(img)
    f_title = _font(40, True)
    f_sub = _font(19)
    f_head = _font(22, True)
    f_legend = _font(18)
    f_note = _font(16)

    d.text((50, 26), "路径积分 · 框架地图", font=f_title, fill=INK)
    d.text((52, 82), "李思《量子力学与几何》第 2 章 · 从费曼核到量子 HKR 的三层计算引擎", font=f_sub, fill=MUTED)

    for (x, y, w, h, title) in PANELS:
        d.rounded_rectangle((x, y, x + w, y + h), radius=14, fill=PANEL, outline=PANEL_BORDER, width=2)
        _draw_line(d, x + 20, y + 14, title, 22, True, INK)

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
            _draw_center(d, x + w / 2, ty, line, size, bold=(key in ("A0", "B0", "C0", "D0")), fill=INK)
            ty += lh

    # 出口
    _draw_line(d, 60, 805, "三个出口：从核到谱、隧穿与量子化乘法", 22, True, INK)
    for key, (label, track, x, y, w, h, size) in NODES.items():
        if track != "X":
            continue
        c = TRACK[track]
        d.rounded_rectangle((x, y, x + w, y + h), radius=10, fill=c["fill"], outline=c["stroke"], width=2)
        lines = label.split("\n")
        lh = size + 7
        ty = y + (h - lh * len(lines)) / 2 + 1
        for line in lines:
            _draw_center(d, x + w / 2, ty, line, size, fill=INK)
            ty += lh

    # 缺口框
    d.rounded_rectangle((60, 940, 1700, 1010), radius=10, fill="#fffaf0", outline="#d9b26a", width=2)
    _draw_line(
        d,
        80,
        953,
        "书中只给思路 / 未展开：路径积分测度（无严格定义）· 一般势的连接公式（只做线性势/Airy 模型）· 量子 HKR 的完整证明（定理 2.8.16 只陈述）",
        16,
        False,
        "#7a5a1e",
    )

    # 图例
    lx = 60
    for t in ["A", "B", "C", "D", "E", "X"]:
        c = TRACK[t]
        d.rounded_rectangle((lx, 1060, lx + 22, 1082), radius=5, fill=c["fill"], outline=c["stroke"], width=2)
        _draw_line(d, lx + 30, 1060, c["name"], 18, False, INK)
        lx += 30 + _line_width(c["name"], 18) + 28
    _draw_line(d, 1240, 1060, "完整 50 张卡见 taxonomy.md · render_map.py 生成", 18, False, MUTED)

    img.save(path)
    return path


def _svg_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def draw_svg(path: Path):
    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    out.append(
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#98a2b3"/></marker>'
        '<marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#7d8798"/></marker></defs>'
    )
    out.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    out.append(f'<text x="50" y="58" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="40" font-weight="700" fill="{INK}">路径积分 · 框架地图</text>')
    out.append(f'<text x="52" y="100" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="19" fill="{MUTED}">李思《量子力学与几何》第 2 章 · 从费曼核到量子 HKR 的三层计算引擎</text>')

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
        weight = ' font-weight="700"' if key in ("A0", "B0", "C0", "D0") else ""
        out.append(f'<text x="{x + w/2}" y="{ty:.1f}" text-anchor="middle" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="{size}"{weight} fill="{INK}">')
        for i, line in enumerate(lines):
            dy = 0 if i == 0 else lh
            out.append(f'<tspan x="{x + w/2}" dy="{dy}">{_svg_escape(line)}</tspan>')
        out.append('</text>')

    out.append(f'<text x="60" y="825" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="22" font-weight="700" fill="{INK}">三个出口：从核到谱、隧穿与量子化乘法</text>')
    out.append(f'<rect x="60" y="940" width="1640" height="70" rx="10" fill="#fffaf0" stroke="#d9b26a" stroke-width="2"/>')
    out.append(f'<text x="80" y="972" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="16" fill="#7a5a1e">书中只给思路 / 未展开：路径积分测度（无严格定义）· 一般势的连接公式（只做线性势/Airy 模型）· 量子 HKR 的完整证明（定理 2.8.16 只陈述）</text>')

    lx = 60
    for t in ["A", "B", "C", "D", "E", "X"]:
        c = TRACK[t]
        out.append(f'<rect x="{lx}" y="1060" width="22" height="22" rx="5" fill="{c["fill"]}" stroke="{c["stroke"]}" stroke-width="2"/>')
        out.append(f'<text x="{lx+30}" y="1077" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="18" fill="{INK}">{_svg_escape(c["name"])}</text>')
        lx += 30 + len(c["name"]) * 19 + 28
    out.append(f'<text x="1240" y="1077" font-family="Microsoft YaHei, Noto Sans CJK SC, sans-serif" font-size="18" fill="{MUTED}">完整 50 张卡见 taxonomy.md · render_map.py 生成</text>')
    out.append("</svg>")
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
