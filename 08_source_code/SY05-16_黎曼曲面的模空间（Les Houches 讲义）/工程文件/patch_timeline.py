# -*- coding: utf-8 -*-
"""patch_timeline.py — 用最新边界裁决替换 TIMELINE.md 的「精确接续锚点」一节"""
import io

P = r"<本地路径>"
s = open(P, encoding="utf-8").read()
start = s.index("## 精确接续锚点（防重防漏）")
end = s.index("## 已知细节（防止踩坑）")
new = """## 精确接续锚点（防重防漏）

> ⚠️ **2026-11-03 裁决**：实测发现 §2.2、§2.3、§3.1、§3.2、§3.3 五个小节标题都落在**页面中部**，其前面的公式属于该块的编号区间。因此这五个小节标题**由对应块在正文流里就地写出**，main.tex 不写。各块负责人以收到的修正消息 + 下表为准。
> §2、§2.1、§3、§4、§4.1 五个标题仍由 main.tex 写。

| 边界 | 前块最后一条 | 后块第一条 | 说明 |
|---|---|---|---|
| A→B | (1.2)，p3 末"Funding information"结束 | (2.1) | B 从 p4 "Terminology." 开始；§2 标题 + §2 引言段 + §2.1 标题由 main.tex 写 |
| B→C | (2.16) + p9→p10 的稳定条件段（"…$2g(v)-2+n(v)>0$ for all $v$."） | p10 "The main result about the Deligne–Mumford moduli space is that…" 段（含 **Thm 2.4**、$<本地路径>**(2.17)(2.18)(2.19)**） | **§2.2 标题在 p10 中部，C 就地写出**：插在 "…often called intersection theory." 之后、"Before discussing the cohomology…" 之前 |
| C→D | (2.35)，p15 末 | p16 顶部 "In terms of differential forms…" 段（含 **(2.36)(2.37)(2.38)** + 投影公式） | **§2.3 标题在 p16 中部，D 就地写出**：插在投影公式段之后、"Recall our main goal…" 之前 |
| D→E | (2.61) | (2.62) | 都在 §2.3 内部，无标题 |
| E→F | (2.79) | p27 §3 标题后第一段（Virasoro 约束段，含 **(3.1)(3.2)(3.3)**、TQFT 类比段、Kontsevich–Manin 段） | **§3.1 标题在 p27 中部，F 就地写出**：插在 "…2D TQFTs [Dub96]." 之后、"Fix once and for all…" 之前 |
| F→G | (3.24) | p31 顶部（Example 3.2 余下 bullet，含 **(3.25)**、Novikov 变量段） | **§3.2 标题在 p31 中部，G 就地写出**：插在 "…see [KM94]." 之后、"We have already seen how…" 之前；§3.2 内的 3.2.1/3.2.2/3.2.3 用 `\\subsubsection`（自动编号与原文一致） |
| G→H | (3.48) | p35 顶部（"where $\\delta_m=\\dots$" + **(3.49)**、Exercise 3.3、Teleman 段） | **§3.3 标题在 p35 中部，H 就地写出**：插在 "…Pretty neat!" 之后、"Givental's action provides a recursive construction…" 之前 |
| H→I | (3.60) | (4.1) | §4 与 §4.1 标题由 main.tex 写；**§4.2 标题在 p41 中部，由 I 在 sec4.tex 里就地写出** |

"""
open(P, "w", encoding="utf-8", newline="\n").write(s[:start] + new + s[end:])
print("TIMELINE.md 已更新")
