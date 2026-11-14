#!/usr/bin/env python3
"""translate_kit 自测：合成一个最小工程，把闸门与检查的两条路径都走通。

为什么要这个文件：`check` / `gate` 全是"报错容易、放行难"的工具——
只验证失败路径，等于不知道通过路径是否存在。所以这里做两件事：
  1. 造一个**应当通过**的工程，断言 exit=0（否则新流程根本开不了工）；
  2. 逐个埋红旗，断言 check 六类问题全部被抓到（否则规矩是纸面规矩）。

用法：
    python 04_playbook/tools/selftest_kit.py        # 全绿打印 PASS，退出码 0
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(HERE, "translate_kit.py")
PY = sys.executable

# Windows 控制台默认 GBK，PASS/✗ 之类字符会直接抛 UnicodeEncodeError
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

fails = []


def run(*argv):
    r = subprocess.run([PY, KIT, *argv], capture_output=True, text=True, encoding="utf-8")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def expect(cond, label, detail=""):
    if cond:
        print(f"  PASS  {label}")
    else:
        print(f"  FAIL  {label}")
        if detail:
            print("        " + detail.replace("\n", "\n        ")[:1200])
        fails.append(label)


def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


# ---------------------------------------------------------------- 造工程
PAGE1 = """Lecture 1. Introduction

Definition 1.1. A ringed space is a pair (X, O_X) ...

Theorem 1.2 (Main estimate). Let f be a smooth function on a compact manifold M.
Then there exists C > 0 such that sup |f| <= C.

Proof. The argument proceeds in two steps. First ...

Lemma 1.3. Every open cover admits a subordinate partition of unity.
"""

PAGE2 = """Lecture 2. Consequences

Proposition 2.1. Under the assumptions of Theorem 1.2, the constant C depends
only on the dimension.

Corollary 2.2. The estimate is stable under small perturbations.

Remark 2.3. The compactness hypothesis cannot be removed.
"""


def build(root):
    work = os.path.join(root, "工程文件", "work")
    w(os.path.join(work, "pages", "p001.txt"), PAGE1)
    w(os.path.join(work, "pages", "p002.txt"), PAGE2)
    w(os.path.join(work, "pages.json"), json.dumps([{"page": 1}, {"page": 2}], ensure_ascii=False))
    w(os.path.join(work, "fulltext.txt"), PAGE1 + "\n" + PAGE2)
    w(os.path.join(work, "chunks.json"), json.dumps(
        [{"id": "ch01", "from": 1, "to": 2, "chars": 900, "tokens": 3000}], ensure_ascii=False))

    w(os.path.join(work, "glossary.tsv"),
      "# 术语表（英文\\t中文\\t备注）\nringed space\t环空间\t\npartition of unity\t单位分解\t\n"
      "compactness\t紧性\t\n")

    w(os.path.join(work, "definitions.tsv"),
      "术语英文\t术语中文\t首次出现\t定义要点\t采用来源\t依据等级\t状态\n"
      "ringed space\t环空间\tp.001\t局部环化空间\tStacks 01HA\tA\t已定\n"
      "partition of unity\t单位分解\tp.001\t从属于覆盖的连续函数族\tWarner, Foundations\tA\t已定\n"
      "compact manifold\t紧流形\tp.001\t紧的拓扑流形\tMilnor, Topology from the DG Viewpoint\tA\t已定\n"
      "smooth function\t光滑函数\tp.001\tC^infty 实值函数\t同上\tB\t已定\n"
      "subordinate cover\t从属覆盖\tp.001\t与给定覆盖细化关系\tWarner, Foundations\tA\t已定\n")

    w(os.path.join(work, "通读笔记.md"),
      "# 通读笔记\n\n## 主旨\n这两讲讲环空间上的主估计：先给出紧流形上的一致界，再说明常数只依赖维数。\n\n"
      "## 论证路线\n第一步用单位分解把整体估计化成局部估计，第二步对局部块求和并控制交叠重数。\n\n"
      "## 体裁\n讲义体，定理-证明交替，无习题，符号沿用 Warner 的记法。\n\n"
      "## 阅读顺序\n1.1 定义 → 1.2 主估计 → 1.3 单位分解 → 2.1 常数依赖 → 2.2 稳定性 → 2.3 反例说明。\n"
      "\n## 疑点\n2.3 说紧性「无法去掉」却没给反例，需查文献确认是断言还是定理。\n\n"
      "## 术语与记号\nringed space 译「环空间」，partition of unity 译「单位分解」，"
      "subordinate 用「从属」不用「从属的」。"
      r"$\mathcal{O}_X$ 记结构层，$\sup$ 保持正体，全篇用 $\le$ 不用 $\leq$。" "\n\n"
      "## 风险\n2.2 的「稳定」一词原文未量化，译文若加「一致」会超出原文，"
      "应先查证再决定是否加译注。\n")

    w(os.path.join(work, "疑点清单.tsv"),
      "位置\t原文表述\t类型\t初步猜测\t查证动作\t结论\t依据\t状态\t归因\t下一步\n"
      "p.002\tcannot be removed\t数学缺口\t可能需要反例\t查 Milnor 例 3.2\t"
      "原文指去掉紧性后估计失效\tMilnor p.42\t已核\t数学缺口\t写进译注并给 p.42\n")

    return work


GOOD_TEX = r"""\section{引言}

\begin{definition}[环空间]\label{def:ringed}
环空间是一对 $(X,\mathcal{O}_X)$。
\end{definition}

\begin{theorem}[主估计]\label{thm:main}
设 $f$ 是紧流形 $M$ 上的光滑函数，则存在常数 $C>0$ 使 $\sup|f|\le C$。
\end{theorem}

\begin{proof}
论证分两步。首先由定义~\ref{def:ringed} 与单位分解化为局部估计\zhnote{单位分解的构造见
Warner 第 4 章。 [来源：Warner, \emph{Foundations}, p.31]}。
\end{proof}

\routenote{此处改用单位分解而非直接积分，是为了避开边界项估计（原文 p.002）。}

\begin{lemma}\label{lem:pou}
每个开覆盖都有从属的单位分解。
\end{lemma}

\begin{proposition}\label{prop:const}
在定理~\ref{thm:main} 的假设下，常数 $C$ 只依赖维数。
\end{proposition}

\begin{corollary}\label{cor:stable}
该估计在小扰动下稳定。
\end{corollary}

\begin{remark}\label{rem:comp}
紧性假设不能去掉。
\end{remark}
"""

BAD_TEX = r"""\section{坏样例}

\begin{theorem}\label{thm:bad}
参考知乎上的一个证明,结果如下:可以去掉紧性。
\end{theorem}

\zhnote{这一步显然成立，不需要解释。}

见~\ref{thm:nowhere}。

\routenote{这里换了个路线。}

TODO 补图。
"""


def fill_contract(path):
    txt = open(path, encoding="utf-8").read()
    txt = re.sub(r"⟨待填[^⟩]*⟩", "已填内容", txt)
    txt = txt.replace("- 状态: 未填", "- 状态: 已审")
    txt = re.sub(r"- 审阅: .*", "- 审阅: Lead 2026-11-14", txt)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)


def main():
    tmp = tempfile.mkdtemp(prefix="kit_selftest_")
    root = os.path.join(tmp, "proj")
    try:
        work = build(root)
        chunks = os.path.join(root, "源码", "chunks")
        w(os.path.join(chunks, "ch01.tex"), GOOD_TEX)

        print("[1] 未立契约、未通读时，gate 必须拦")
        code, out = run("gate", root)
        expect(code == 1 and "契" in out, "gate 拦下未立契约的工程", out)

        print("[2] contract 生成 + 未填校验")
        code, out = run("contract", root)
        expect(code == 0 and os.path.exists(os.path.join(work, "contracts", "ch01.md")),
               "contract 生成契约卡", out)
        code, out = run("contract", root, "--check")
        expect(code == 1 and "未填" in out, "contract --check 拦下未填的卡", out)

        print("[3] 填完并签字后，contract --check 放行")
        fill_contract(os.path.join(work, "contracts", "ch01.md"))
        code, out = run("contract", root, "--check")
        expect(code == 0, "contract --check 放行已审的卡", out)

        print("[4] 通读笔记早于落笔，gate 通过路径存在")
        now = time.time()
        os.utime(os.path.join(work, "通读笔记.md"), (now - 3600, now - 3600))
        os.utime(os.path.join(chunks, "ch01.tex"), (now, now))
        code, out = run("gate", root)
        expect(code == 0 and "通过" in out, "gate 全绿路径通过", out)

        print("[5] 通读晚于落笔，gate 必须拦（纪律 §1.0.4）")
        os.utime(os.path.join(work, "通读笔记.md"), (now + 60, now + 60))
        code, out = run("gate", root)
        expect(code == 1 and "晚于" in out, "gate 拦下先写后读", out)
        os.utime(os.path.join(work, "通读笔记.md"), (now - 3600, now - 3600))

        print("[6] 疑点未解不清零，gate 必须拦")
        doubt = os.path.join(work, "疑点清单.tsv")
        good_doubt = open(doubt, encoding="utf-8").read()
        w(doubt, good_doubt + "p.003\t另一处\t记号\t不确定\t查书\t—\t—\t未解\t工程\t待查\n")
        code, out = run("gate", root)
        expect(code == 1 and "未解" in out, "gate 拦下未解疑点", out)
        w(doubt, good_doubt)

        print("[7] 干净译文 check 必须放行")
        code, out = run("check", root)
        expect(code == 0, "check 对干净译文放行", out)

        print("[8] 六类红旗全部能被 check 抓到")
        w(os.path.join(chunks, "ch02.tex"), BAD_TEX)
        code, out = run("check", root)
        for label, needle in (
            ("黑名单", "[黑名单]"),
            ("译注无来源", "[译注无来源]"),
            ("悬空引用", "[悬空引用]"),
            ("半角标点", "[标点]"),
            ("残留标记", "[残留]"),
            ("路线注缺页码", "[路线注]"),
        ):
            expect(needle in out, f"check 抓到{label}", out)
        expect(code == 1, "check 有问题时退出码为 1", out)

        print()
        if fails:
            print(f"FAILED {len(fails)} 项")
            return 1
        print("全部通过 ✅（gate 通过/拒绝两条路径 + check 六类红旗）")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
