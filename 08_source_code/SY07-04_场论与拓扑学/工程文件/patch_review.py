# -*- coding: utf-8 -*-
"""交叉校对落改 patch —— 按 SOP M6：每条替换 exact-match，命中数必须等于预期，否则跳过并打印。"""
import os

ROOT = r"<本地路径>"
CH = os.path.join(ROOT, "src", "chunks")
log = []


def sub(fname, old, new, why, expect=1):
    p = os.path.join(CH, fname)
    t = open(p, encoding="utf-8").read()
    n = t.count(old)
    if n != expect:
        log.append(f"SKIP  {fname}: {why} (命中 {n}, 预期 {expect})")
        return
    open(p, "w", encoding="utf-8").write(t.replace(old, new))
    log.append(f"OK    {fname}: {why}")


# ---------- ch01a（review/ch01a.md M1–M4）----------
OLD_NOTE = r"""% [Tutor Note: 末句的 $H^{2}(LG,\Z)$ 疑为笔误：$LG$ 单连通（本节刚证），故 $H^{2}(LG,\Z)=0$；而式 (1.7) 的 $\omega$ 定义在 $\Lie(LG_{\C})$ 上，这里应为 $H^{2}(LG_{\C},\Z)\cong\Z$。正文照原书，未改。]"""
NEW_NOTE = r"""% [Tutor Note: $LG$ 单连通只保证 $H^{1}(LG,\Z)=0$，$H^{2}$ 一般不为零。事实上 $LG\cong G\times\Omega G$，故 $H^{2}(LG,\Z)\cong H^{2}(G,\Z)\oplus H^{2}(\Omega G,\Z)\cong 0\oplus\Hom(\pi_{3}(G),\Z)\cong\Z$；同理 $H^{2}(LG_{\C},\Z)\cong\Z$。末句把 (1.7) 的 $\omega$ 与其上同调类等同看待（本节已证 $\omega=\omega_{0}+d\beta$，$\omega_{0}$ 的类属于 $H^{2}(LG,\Z)$），并非笔误。]"""
sub("ch01a.tex", OLD_NOTE, NEW_NOTE, "M1 批注纠正（H^2(LG,Z)=Z 不是笔误）")

OLD_M2 = r"""并借助左不变向量场把它与 $\Lie(LG_{\C})$ 等同。对 $\gamma\in LG_{\C}$、$\xi\in T_{\gamma}LG_{\C}$，令"""
NEW_M2 = r"""并借助左不变向量场把它与 $\Lie(LG_{\C})$ 等同。把 $LG_{\C}$ 上的一次微分形式 $\beta$ 定义为：对 $\gamma\in LG_{\C}$、$\xi\in T_{\gamma}LG_{\C}$，令"""
sub("ch01a.tex", OLD_M2, NEW_M2, "M2 补译「beta 是一次微分形式」")

sub("ch01a.tex", r"核心工具是由二维上同调 $H^{2}(L\mathfrak{g},\mathbb{C})\cong\mathbb{C}$",
    r"核心工具是由 2 次上同调 $H^{2}(L\mathfrak{g},\mathbb{C})\cong\mathbb{C}$", "M3 二维→2 次上同调")

sub("ch01a.tex", r"取 $\mathfrak{g}$ 的 Cartan 子代数的一个基 $H$",
    r"取 $\mathfrak{g}$ 的 Cartan 子代数的一个基元 $H$", "M4 一个基→一个基元")

# 可选改 O3（如所周知→众所周知）与 O6（补收束语）
sub("ch01a.tex", r"则如所周知", r"则众所周知", "O3 如所周知→众所周知", expect=1)
sub("ch01a.tex", r"而 $\langle H,H\rangle\ne 0$。以上证明了命题。",
    r"而 $\langle H,H\rangle\ne 0$，由此立即得出该上同调类非平凡。以上证明了命题。", "O6 补「由此立即得出」")

# ---------- ch02a（review/ch02a.md M1）----------
sub("ch02a.tex",
    r"""\begin{proposition}{2.2}
  如图 2.4 所示""",
    r"""\begin{proposition}{2.2}
  （五边形关系式）如图 2.4 所示""", "M1 命题2.2 补标题括注")

print("\n".join(log))
