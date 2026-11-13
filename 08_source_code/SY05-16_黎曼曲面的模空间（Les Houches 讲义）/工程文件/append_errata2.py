# -*- coding: utf-8 -*-
"""append_errata2.py — 第三批 ERRATA 登记（Block G/I 上报）"""
EF = r"<本地路径>"
err = """

## 六、第三批上报（Block G / Block I）

| # | 页码 | 位置 | 原文写法 | 正确写法 | 判断依据 |
|---|---|---|---|---|---|
| 26 | p.31–32 | §3.2 首段 | "…but should involve specific combinations **ψ-classes**." | "specific combinations **of** ψ-classes" | combinations 后须接 of（脱漏介词） |
| 27 | p.38 | (4.1) 集合条件第二行 | "with $n$ labelled geodesics boundaries" | "with $n$ labelled **geodesic** boundaries" | 名词作定语用单数 |
| 28 | p.39 | Figure 15 图注 | "$\\alpha_p$ **intersect** $<本地路径> and itself respectively" | "$\\alpha_p$ **intersects** …" | 主谓一致（单数主语） |
| 29 | p.42 | 正文 | "remodelling"（英式）与文献 [BKMP09] 标题 "Remodeling"（美式）不一致 | — | 拼写变体，非笔误；批注说明 |
"""
open(EF, "a", encoding="utf-8", newline="\n").write(err)
print("errata batch 3 appended")
