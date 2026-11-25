# -*- coding: utf-8 -*-
"""追加 v1.1 校订的登记行（疑点清单.tsv / typos.txt），带幂等检查。"""
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = os.path.join(ROOT, "工程文件", "work")

DOUBT = [
    ("原文 1004（§1.3 例 1.3.12）",
     r"$(\Gr_G)_{\on{red}}=\pi_0(G)=\bZ$",
     "笔误",
     "$\\pi_0(G)$ 与上下文不符",
     "核对 $G=\\bG_m$ 时 $\\pi_0(G)=1$，同句前文已说 $\\pi_0(\\Gr_G)\\cong\\bZ$",
     "按文意译作 $\\pi_0(\\Gr_G)$，并加译注（译5）说明原文写法",
     "原文 1003--1004 行；逻辑自洽",
     "已解"),
    ("原文 3347（§5.6）",
     r"$(\mA_1)_y\otimes(A_2)_{y^{-1}x}$",
     "笔误",
     "第二个因子漏 \\m",
     "与同式左侧 $\\mA_1$ 对照",
     "改为 $(\\mA_2)$，登记 typos.txt",
     "原文同式自证",
     "已解"),
    ("ch21 参考文献 22 条",
     "会议年 / 丛书名 / eprint",
     "体例",
     "出版年与会议年是否混用",
     "check_bib.py 逐条比对原文 amsrefs 字段",
     "22 条按出版年与丛书重写，硬问题 0",
     "work/bib_report.txt",
     "已解"),
]

TYPO = ("3347: (A_2) || "
        r"$$(\mA_1\tilde\boxtimes\mA_2)_{(y,y^{-1}x)}\cong (\mA_1)_y\otimes(A_2)_{y^{-1}x}$$ "
        "第二个因子漏 \\m，应作 (\\mA_2)；无歧义，直接补正，不加注")


def append_tsv():
    path = os.path.join(WORK, "疑点清单.tsv")
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    add = []
    for row in DOUBT:
        if row[0] in text:
            continue
        add.append("\t".join(row))
    if add:
        if not text.endswith("\n"):
            text += "\n"
        text += "\n".join(add) + "\n"
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print("疑点清单：追加 %d 行" % len(add))


def append_typos():
    path = os.path.join(WORK, "typos.txt")
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    if "3347:" in text:
        print("typos.txt：已存在，跳过")
        return
    if not text.endswith("\n"):
        text += "\n"
    text += TYPO + "\n"
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("typos.txt：追加 1 行")


if __name__ == "__main__":
    append_tsv()
    append_typos()
