# -*- coding: utf-8 -*-
"""校对第一轮：把通读查出的字词/句法缺陷一次性写回 chunks。

每条 = (文件, 原文片段, 新文片段)。要求原文片段在文件中恰好出现一次，否则报错不写。
用法：cd 工程文件/scripts && python fix_text_round1.py
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
CH = os.path.join(ROOT, "源码", "chunks")

FIXES = [
    # ch00 §0.1 「非 阿基米德」多余空格
    ("ch00.tex",
     "（与非 阿基米德 局部域上约化群的调和分析有关）",
     "（与非阿基米德局部域上约化群的调和分析有关）"),
    # ch00 §0.3.2 预层/预叠的（resp.）句式
    ("ch00.tex",
     r"\emph{预层}（prestack 叫\emph{预叠}）是指从 $\Aff_k$ 到集合范畴（相应地，群胚 $2$-范畴）的共变函子（相应地，$2$-函子）。",
     r"\emph{预层}（相应地，\emph{预叠}）是指从 $\Aff_k$ 到集合范畴（相应地，群胚 $2$-范畴）的共变函子（相应地，$2$-函子）。"),
    # ch00 §0.3.6 定冠词直搬
    ("ch00.tex",
     r"以 $\mE^0$ 记\emph{那个}平凡 $\underline G$-主丛。",
     r"以 $\mE^0$ 记平凡 $\underline G$-主丛。"),
    ("ch00.tex",
     r"称之为\emph{那个}\emph{圆盘}与\emph{去心圆盘}，以强调坐标 $t$ 的选定。",
     r"称之为\emph{圆盘}与\emph{去心圆盘}，以强调坐标 $t$ 的选定。"),
    # ch00 §0.4 拉丁名前后缺空格
    ("ch00.tex",
     r"我还要感谢Weizhe Zheng就 \S\ref{ULA sheaf} 的有益讨论，以及 Michael Harris、Jiuzu Hong与 Joel Kamnitzer 的宝贵意见。",
     r"我还要感谢 Weizhe Zheng 就 \S\ref{ULA sheaf} 的有益讨论，以及 Michael Harris、Jiuzu Hong 与 Joel Kamnitzer 的宝贵意见。"),
    # ch00 §0.1 唯一一条译注补来源标记（纪律 §9）
    ("ch00.tex",
     r"\zy{更确切地说，是 Langlands 对 Satake 同构的重新解释。}",
     r"\zy{更确切地说，是 Langlands 对 Satake 同构的重新解释。\textup{［译者按：原文 \S5.6 把 Satake 同构表述为几何 Satake 等价在函子层面的对应；参见 nLab 词条 geometric Satake equivalence（2024-07-22 修订）。］}}"),
    # ch02 例 1.3.x 原文笔误 π₀(G) → π₀(Gr_G)，加译注不改正文
    ("ch02.tex",
     r"事实上 $(\Gr_G)_{\on{red}}=\pi_0(G)=\bZ$。",
     r"事实上 $(\Gr_G)_{\on{red}}=\pi_0(\Gr_G)=\bZ$\zy{［译者按：原文此处写作 $\pi_0(G)$；但 $G=\bG_m$ 时 $\pi_0(G)=1$，且同句前文已说 $\pi_0(\Gr_G)\cong\bZ$，故按文意指 $\pi_0(\Gr_G)$ 译出。原文该处疑为笔误，已记入工程「疑点清单」。］}。"),
    # ch02 §1.3 $\Aut(D)$ 语序
    ("ch02.tex",
     r"以 $\Aut(D)$ 记 $\mO=k[[t]]$ 的自同构群归纳概形。",
     r"以 $\Aut(D)$ 记 $\mO=k[[t]]$ 的自同构所构成的群归纳概形。"),
    # ch12 §5.1 strata 未译
    ("ch12.tex",
     r"且它在每个 strata $\Gr_\la$ 上的限制是常值的",
     r"且它在每个层片 $\Gr_\la$ 上的限制是常值的"),
    # ch12 §5.1 漏「与」
    ("ch12.tex",
     r"Mirkovi\'c--Vilonen 用它证明了卷积映射的半小性，这也命题等价",
     r"Mirkovi\'c--Vilonen 用它证明了卷积映射的半小性，这与命题等价"),
    # ch14 §5.4 语义拧了
    ("ch14.tex",
     r"这一解释显出卷积积更多来自 $X^I$ 对称性的对称性。",
     r"这一解释使卷积积的更多对称性显现出来，它们来自 $X^I$ 的对称性。"),
    # ch16 §5.6 原文笔误 (A_2) 缺 \m，直接改并登记
    ("ch16.tex",
     r"\otimes(A_2)_{y^{-1}x}",
     r"\otimes(\mA_2)_{y^{-1}x}"),
    # ch17 附录 A.1 non-canonical 误作「非同构」
    ("ch17.tex",
     r"有非同构 $\on{H}^*_K(X,\mF)\cong",
     r"有非典范的同构 $\on{H}^*_K(X,\mF)\cong"),
]


def main():
    cache = {}
    for fn, old, new in FIXES:
        if fn not in cache:
            with io.open(os.path.join(CH, fn), encoding="utf-8") as f:
                cache[fn] = f.read()
        n = cache[fn].count(old)
        if n != 1:
            sys.stderr.write("未写入：%s 中片段出现 %d 次：%r\n" % (fn, n, old[:60]))
            return 1
        cache[fn] = cache[fn].replace(old, new)
    for fn, text in cache.items():
        with io.open(os.path.join(CH, fn), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        sys.stdout.write("patched %s\n" % fn)
    sys.stdout.write("done: %d replacements\n" % len(FIXES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
