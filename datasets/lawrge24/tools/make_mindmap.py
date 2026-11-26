# -*- coding: utf-8 -*-
"""生成《相对朗兰兹对偶》研读思维导图（PNG）。

数据写在 BRANCHES 里，不依赖网络；字体用本机微软雅黑。
用法：python tools/make_mindmap.py [输出路径]
"""
import re
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 3000, 1810
BG = (250, 249, 246)
INK = (32, 34, 38)
MUTED = (110, 112, 118)
FONT = "C:/Windows/Fonts/msyh.ttc"
FONT_B = "C:/Windows/Fonts/msyhbd.ttc"

BRANCHES = [
    {
        "title": "① 形式化：TQFT 与 A/B 理论",
        "color": (196, 92, 62),
        "items": [
            "TQFT 公理：对称幺半函子 Bord^n → C",
            "配边范畴：对象是 n−1 维闭流形，态射是配边",
            "边界条件 = 理论的对象；配边 = 态射",
            "A-理论 A_G：由 G-丛的模空间给出",
            "B-理论 B_Ĝ：由对偶群局部系给出",
            "Langlands 作为 4d TQFT 的一个边界",
            "算术–拓扑字典：Spec Z 的三维流形类比",
        ],
    },
    {
        "title": "② 局部对偶：球簇与对偶群",
        "color": (58, 110, 165),
        "items": [
            "球 G-簇 X：Borel 子群有稠轨道",
            "对偶群 Ĝ_X：由 X 的着色与不变赋值装配",
            "相对 Cartan 子群 A_X：秩一自由性的载体",
            "小 Weyl 群 W_X：A_X 上的反射群",
            "重数自由：F[X] 的每个不可约分量重数为一",
            "秩一自由：S(X(F))^{G(O)} → H_X^G 是同构",
            "超球簇：Ĝ_X 的结构可显式描述",
        ],
    },
    {
        "title": "③ 整体对偶：周期层与 L-层",
        "color": (74, 124, 89),
        "items": [
            "周期层 P_X = π_! k_{Bun^X_G}：X 的整体周期",
            "L-层 = π_* ω（对偶侧）：对偶侧的谱对象",
            "整体猜想：P_X 与 L-层在 Bun_G 上对偶",
            "Beilinson 投影：从 IndCoh 切到特征层",
            "迹公式：周期积分 = 谱侧求和",
            "Eisenstein / Whittaker：X=G/N 与 X=G/U 的检验",
        ],
    },
    {
        "title": "④ 结构工具箱：Hecke、Satake、谱作用",
        "color": (150, 96, 160),
        "items": [
            "Hecke 范畴 A_G(R)：raviolo 上的卷积",
            "几何 Satake：Shv(Gr) 同构于 Rep(Ĝ)",
            "导出 Satake：IndCoh(Ωĝ/Ĝ)",
            "谱作用：张量_x Rep(Ĝ) 对应 QCoh(Loc_Ĝ Σ)",
            "Koszul 对偶：Loc_Ĝ 与 ĝ*[2]/Ĝ",
            "E3 结构：Hecke 范畴的顶层对称性",
        ],
    },
    {
        "title": "⑤ 例子与检验：可算的东西",
        "color": (176, 132, 44),
        "items": [
            "一维 TQFT：4×4 赋值表与 Frobenius 代数",
            "Tate：zeta 展开为局部积分之积",
            "raviolo：Bun_G = Z 的退化情形",
            "PGL2^l × PGL2^r：树上的模型例",
            "Hitchin–Gaiotto：M=T*X 与对偶侧 M=T*X",
            "奇迹对偶：Ĝ_X 与 G 的对称交换",
        ],
    },
    {
        "title": "⑥ 未决与开放：讲义没说完的",
        "color": (120, 120, 120),
        "items": [
            "shearing 斜框：原文 (11.19) 对 (11.12) 的修正",
            "整体猜想 13.21：只给陈述，不给证明",
            "E3 的来源：几何 Satake 之外的结构解释",
            "讲义自述「极不完整、未校订」，多处标 ?",
            "可计算检验：低秩 G、曲线 P1、X=T*U",
        ],
    },
]


def font(size, bold=False):
    return ImageFont.truetype(FONT_B if bold else FONT, size)


def wrap(draw, text, f, maxw):
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=f) <= maxw:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def seg(draw, pts, color, width):
    draw.line(pts, fill=color, width=width, joint="curve")


def main(out):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    d.text((90, 60), "相对朗兰兹对偶 · 研读思维导图", font=font(54, True), fill=INK)
    d.text((92, 132), "LAWRGE 2024 Notes（73 页 / 15 讲）· 47 张资料卡 · 每条断言锚到原文页",
           font=font(24), fill=MUTED)

    root = (1500, 300)
    rw, rh = 520, 110

    margin_x, gap_x = 80, 40
    panel_w = (W - 2 * margin_x - 2 * gap_x) // 3
    panel_h = 560
    tops = [470, 1150]
    centers = [margin_x + c * (panel_w + gap_x) + panel_w // 2 for c in range(3)]

    # —— 连接线（先画，面板后画，遮住穿过的部分）——
    bus1 = 430
    seg(d, [(root[0], root[1] + rh // 2), (root[0], bus1)], (150, 150, 150), 3)
    seg(d, [(centers[0], bus1), (centers[2], bus1)], (150, 150, 150), 3)
    for cx in centers:
        seg(d, [(cx, bus1), (cx, tops[0])], (150, 150, 150), 3)
    # 第二排：从两列之间的空隙(1020)下到第二条总线
    midx = 1020
    seg(d, [(midx, bus1), (midx, 1100)], (150, 150, 150), 3)
    seg(d, [(centers[0], 1100), (centers[2], 1100)], (150, 150, 150), 3)
    for cx in centers:
        seg(d, [(cx, 1100), (cx, tops[1])], (150, 150, 150), 3)

    d.rounded_rectangle((root[0] - rw // 2, root[1] - rh // 2, root[0] + rw // 2, root[1] + rh // 2),
                        radius=22, fill=(32, 34, 38))
    d.text((root[0], root[1] - 26), "相对朗兰兹对偶", font=font(38, True), fill=(255, 255, 255), anchor="mm")
    d.text((root[0], root[1] + 26), "BZSV · TQFT × 球簇 × 周期层", font=font(20), fill=(235, 235, 235), anchor="mm")

    for i, b in enumerate(BRANCHES):
        col, row = i % 3, i // 3
        x0 = margin_x + col * (panel_w + gap_x)
        y0 = tops[row]
        x1, y1 = x0 + panel_w, y0 + panel_h
        color = b["color"]

        d.rounded_rectangle((x0, y0, x1, y1), radius=26, fill=(255, 255, 255), outline=color, width=3)
        d.rounded_rectangle((x0, y0, x1, y0 + 86), radius=26, fill=color)
        d.rectangle((x0, y0 + 60, x1, y0 + 86), fill=color)
        d.text((x0 + 28, y0 + 43), b["title"], font=font(28, True), fill=(255, 255, 255), anchor="lm")

        ty = y0 + 118
        for it in b["items"]:
            d.ellipse((x0 + 30, ty + 11, x0 + 42, ty + 23), fill=color)
            lines = wrap(d, it, font(21), panel_w - 130)
            for ln in lines:
                d.text((x0 + 56, ty), ln, font=font(21), fill=INK)
                ty += 31
            ty += 16

    d.line((90, H - 72, W - 90, H - 72), fill=(220, 220, 220), width=2)
    d.text((90, H - 52), "生成：datasets/lawrge24/tools/make_mindmap.py · 卡片索引见 index.jsonl · 本图只作结构导航，不替代原文与卡片",
           font=font(18), fill=MUTED)

    img.save(out)
    print("saved", out, img.size)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "05-思维导图.png"
    main(target)
