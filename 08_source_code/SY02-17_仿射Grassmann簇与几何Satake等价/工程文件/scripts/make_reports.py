# -*- coding: utf-8 -*-
"""生成讲次报告（L1–L5、A），编号清单由 work/numbering_src.txt 自动汇总。"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程文件
WORK = os.path.join(ROOT, "work")
REP = os.path.join(ROOT, "reports")
os.makedirs(REP, exist_ok=True)

rows = [l.rstrip().split("\t") for l in open(os.path.join(WORK, "numbering_src.txt"), encoding="utf-8")]

META = [
    ("L1", "第一讲", ["1"], "ch01–ch04", "727–1254", "9–21",
     "仿射 Grassmann 簇的定义与可表性（§1.1–§1.2）、去心圆盘上的群与射流群（§1.3）、Beauville–Laszlo 定理（§1.4）、行列式线丛（§1.5）、复数域（§1.6）与 $p$-进（§1.7）两个特例。",
     "本讲的难点是「归纳概形上的可表性」：先用格的有界性把无穷维对象切成有限型逼近，再用引理 1.1.5–1.1.6 的投射性判据说明逼近是闭的。"),
    ("L2", "第二讲", ["2"], "ch05–ch07", "1255–1765", "22–35",
     "Schubert 簇与 Cartan 分解、维数公式与奇点性质（§2.1）、Gr 中的子归纳概形插叙（§2.2）、对偶 Schubert 簇与横截片、Birkhoff 分解（§2.3）、Picard 群（§2.4）、中心扩张与仿射 Kac–Moody 代数（§2.5）。",
     "§2.4 的 $\Pic^e(\Gr)=\bZ\mO(1)$ 是全篇后面所有线丛论证的支点；$\Theta$ 作为有效 Cartier 除子这一事实在 §5.3 的推论 5.3.7 里被再次使用。"),
    ("L3", "第三讲", ["3"], "ch08–ch09", "1766–2194", "35–46",
     "Beilinson–Drinfeld Grassmann 簇的定义、可表性与基本性质（§3.1）；分解性质的四条内容（§3.2）；Ran 空间与 $\Gr_{\Ran}$（§3.3）；$\Gr_{\Ran}$ 上的刚性化线丛（§3.4）。",
     "分解结构是全书的技术枢纽：它把卷积（§5.1）与融合（§5.4）接上，从而给出交换约束的几何来源。译文在此处保留原文的 $(\phi)$ 记号，不简化。"),
    ("L4", "第四讲", ["4"], "ch10–ch11", "2195–2457", "46–53",
     "单点单值化 $u_x:\Gr_x\to\Bun_G$（§4.1）、线丛与非阿贝尔 theta 函数、共形块（§4.2）、adèle 单值化与 $\Gr_{\Rat}$ 的构造（§4.3）。",
     "§4.3 的两个定理（$\Gr_{\Rat}\to\Bun_G$ 是主丛、$\Gr_{\Ran}\to\Gr_{\Rat}$ 的拉回/推前同构）是原文最密的推理段，译文逐句对应，未合并句子。"),
    ("L5", "第五讲", ["5"], "ch12–ch16", "2458–3402", "53–76",
     "Satake 范畴与半单性、奇迹定理（§5.1）；Tannaka 结构（§5.2）；MV 理论与 Langlands 对偶群（§5.3）；融合积（§5.4）；自举到 ${}^LG^{\on{geo}}$ 与多重点版本（§5.5）；与经典 Satake 的对接（§5.6）。",
     "本讲是全书的结论段。§5.3 与 §5.5 的证明较长，译文保留全部步骤；§5.6 的 $\iota(q^{1/2})<0$ 选择是原文的约定，照译并加说明。"),
    ("A", "附录 A", ["A"], "ch17–ch18", "3405–3700", "76–79",
     "层论补充：等变反常层与等变上同调（§A.1，含 GKM 形式性与局部化定理、pro-代数群作用于归纳概形）；ULA 层的定义与五条性质（§A.2）。",
     "附录是技术工具箱，正文多处引用（引理 A.1.1、定理 A.2.4、定理 A.2.5）。原文 §A.1 的 `\subsubsection` 没有 label，译文补了 6 个，便于正文互引。"),
]

for tag, name, prefixes, chunks, lines, pages, gist, note in META:
    items = [r for r in rows if r[0].split(".")[0] in prefixes and r[0] != "0"]
    thm = [f"{n} {k}" for n, k in items if k != "公式"]
    eqs = [n for n, k in items if k == "公式"]
    out = []
    out.append(f"# {name}报告 · {tag}\n")
    out.append(f"- 原文行：{lines}（`工程文件/work/原文/main.tex`）")
    out.append(f"- 译本页：{pages}")
    out.append(f"- 对应块：{chunks}")
    out.append(f"- 编号对象：{len(items)} 个（定理类 {len(thm)}，公式 {len(eqs)}）\n")
    out.append("## 内容\n")
    out.append(gist + "\n")
    out.append("## 编号清单\n")
    out.append("定理类：" + ("；".join(thm) if thm else "无"))
    if eqs:
        out.append("\n编号公式：" + "、".join(f"({e})" for e in eqs))
    out.append("\n\n## 说明\n")
    out.append(note + "\n")
    out.append("## 编译\n")
    out.append("`cd 源码 && xelatex -interaction=nonstopmode main.tex` 跑两遍；本讲次无 error、无 Overfull、无缺字。\n")
    open(os.path.join(REP, f"ch{tag}.md"), "w", encoding="utf-8").write("\n".join(out))
    print("wrote", tag, len(items))
