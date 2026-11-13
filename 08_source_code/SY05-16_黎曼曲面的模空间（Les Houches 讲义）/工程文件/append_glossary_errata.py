# -*- coding: utf-8 -*-
"""append_glossary_errata.py — 追加术语表条目与 ERRATA 第二批登记"""
GF = r"<本地路径>"
EF = r"<本地路径>"

extra = """string equation\t弦方程\t
dilaton equation\t膨胀子方程\t
multinomial coefficient\t多项系数\t
Morita--Miller--Mumford class\tMorita--Miller--Mumford 类\t
r-spin class\t$r$-旋类（$r$-spin class）\t首见给英文
spin structure\t旋结构（spin structure）\t代数几何惯例；不译"自旋结构"
Verlinde bundle\tVerlinde 丛\t
Hodge integral\tHodge 积分\t
ancestor invariant\t祖先不变量（ancestor invariant）\tCohFT 语境
topological vertex\t拓扑顶点\t
localisation\t局部化\t
"""
with open(GF, "a", encoding="utf-8", newline="\n") as f:
    f.write(extra)

err = """

## 四、补充登记（第二批上报）

| # | 页码 | 位置 | 原文写法 | 正确写法 | 判断依据 |
|---|---|---|---|---|---|
| 20 | p.16 | §2.3 标题后第 2 段 | "we shall always omit the **cap** product since the **cap** product of even-degree cohomology classes is commutative" | 两处均应为 **cup** product | 上同调类之间只有杯积（cap 积是同调与上同调的配对，无"交换性"可言）；同页前文刚说推前 "does not respect the cup product"。与第 1 条 p.10 的 cap/cup 互换是同一处系统性笔误 |
| 21 | p.21 | (2.62) 三行、p.23 (2.74)、p.25 (2.75)(2.77) | 公式末尾的逗号在 PDF 中印在右上角（形如 1/(λ_i+λ_j)′ ,） | 普通逗号 | 疑为源文件遗留的 `\\prime` 或标点抬高；译文排普通逗号，未复制抬高位 |
| 22 | p.22 | "…Bouchard's course [Bou26]!!" | 结尾两个感叹号 | 单个感叹号 | 修辞性冗余，照录并批注 |

## 五、未声明的约定（非笔误，仅批注）

| # | 页码 | 情况 | 处理 |
|---|---|---|---|
| 23 | p.20 | (2.61) 求和项 $(|\\eps|-2)!$ 在 $|\\eps|<2$ 时无定义 | 须把这类项视为零（否则 $n=1$ 算不出 $1/24$）；批注给出 3 组数值核验 |
| 24 | p.22 | 双阶乘只给出 $0!!=1!!=1$，但 (2.67) 的 $k=0$ 项与 (2.73)/(2.78) 的 $d=0$ 项用到 $(-1)!!=1$ | 由 $m!!=m(m-2)!!$ 在 $m=1$ 处即得；批注说明 |
| 25 | p.36 | 脚注 "In the remaining part of this section, we work over $\\C$ rather than $\\Q$." 是原文全文第 4 条脚注 | 译本 footnotes 自动编号与原文不同，批注说明 |
"""
with open(EF, "a", encoding="utf-8", newline="\n") as f:
    f.write(err)
print("appended glossary + errata")
