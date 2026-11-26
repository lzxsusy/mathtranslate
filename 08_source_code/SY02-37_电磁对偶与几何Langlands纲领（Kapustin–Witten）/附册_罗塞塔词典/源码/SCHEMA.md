# 罗塞塔词典：写作规范（SCHEMA）

## 这是什么

KW06（Kapustin–Witten《电磁对偶与几何 Langlands 纲领》）把两套语言焊在一起：**物理侧**是 4 维 $\mathcal N=4$ 超对称杨–米尔斯、超对称扭化、A/B 膜、线算子；**数学侧**是 Hitchin 模空间、超凯勒几何、D-模、Hecke 特征层、几何 Langlands 对应。

本词典的用途是**导航**：给出两侧术语的逐条对照，每条都要能回答四个问题——

1. 这个对象在数学上是怎么**定义**的？标准**例子**是什么？
2. 它在物理上是怎么**定义**（登场）的？对应的物理**例子**是什么？
3. 两侧**为什么能对上**？映射的规则是什么？
4. **直觉**是什么？按字面理解会犯什么**错**？

读者设定：懂一点代数几何或一点量子场论、但没读过 KW06 的人；以及读过 KW06 想查某一条对应的人。

## 词条模板（照抄这个结构）

```latex
\begin{word}{电磁对偶}{electric--magnetic duality}{elec-mag-dual}{§1 p.3；§2.1 p.9--11}
\mathdef{…（自足的定义：对象是什么、由什么数据组成、等价关系是什么、关键不变量）…}
\mathex{…（一个具体例子，写清群/空间/维数/参数）…}
\physdef{…（在 4d $\mathcal N=4$ SYM 里它是什么：哪个场、哪个参数、哪个对称性）…}
\physex{…（一个具体例子：$G=SU(2)$、$\tau=i$、某质量/某电荷）…}
\bridge{…（对应规则：谁映到谁，用 \S2 的哪些式/参数说明）…}
\intuit{…（一句话直觉 + 一句为什么这直觉靠得住）…}
\pitfall{…（最常见的误解，以及错在哪）…}
\end{word}
```

硬性要求：

- **每个词条 250–520 个汉字**（不算公式）。四个区块缺一不可；宁可短，不可空。
- **数学侧定义必须自足**：读者不需要翻别处就能知道对象由什么数据组成。涉及记号先给一句解释。
- **例子必须具体**：写「$G=SU(2)$、$C=\mathbb P^1$、$g=0$」这种可算的例子，不写「例如某个群」。
- **对应**一栏要写清映射规则（谁 ↦ 谁）与自由参数（如 $\tau$、$\Psi$、$t$ 怎么映），并给出原文位置。
- **直觉**一栏允许类比，但要说清类比的边界；**易错**一栏必须是「按字面理解会推出错误结论」的那种，不写译名之争。
- 每个词条末尾的第四参数是**原文锚点**：节号 + 印刷页码（用译本 PDF 页减 1 也行，但要标明是印刷页）。
- 正文段落不超过 5 行；不要在词条里放 `table`/`figure`；不要整段引用解经本。
- 数学一律 `$...$`，中文全角标点；英文术语首次出现写成「中文（English）」形式，但词条标题已给英文，正文不必重复。
- 禁止 Unicode 数学符号（`−` `×` `≤` `∈` 之类），一律 LaTeX 命令。

## 质量标尺（范例，可直接模仿语气与密度）

```latex
\begin{word}{电磁对偶}{electric--magnetic duality}{elec-mag-dual}{§1 p.3；§2.1 p.9--11}
\mathdef{设 $G$ 是紧单连通单群，$\mathfrak g$ 为其 Lie 代数。电磁对偶在数学上最干净的表述是：取 Langlands 对偶群 ${}^LG$（其根 datum 由 $G$ 的根 datum 对偶化得到：根与余根互换、单根系与单余根系互换），则 $G$ 的规范理论在参数 $\tau$ 处的行为与 ${}^LG$ 在 $-1/\tau$ 处的行为相同。这里 $\tau=\theta/2\pi+4\pi i/g^2$ 是复耦合，取值于上半平面；对偶映射是 $\tau\mapsto-1/\tau$，它在 $SL(2,\mathbb Z)$ 里生成 $S$ 变换。}
\mathex{$G=SU(2)$ 时 ${}^LG=SO(3)$；$G=SO(3)$ 时 ${}^LG=SU(2)$。更一般地，$G=SU(N)$ 自对偶（${}^LSU(N)=SU(N)/\mathbb Z_N$ 与 $SU(N)$ 有相同 Lie 代数），$G=Spin(2n)$ 与 $SO(2n)$ 互换。注意 $G$ 与 ${}^LG$ 的中心互为对偶：$\pi_1(G)\cong Z({}^LG)$。}
\physdef{在 4d $\mathcal N=4$ 超对称杨–米尔斯中，电磁对偶是 Montonen–Olive 对偶：同一理论在耦合 $\tau$ 与 $-1/\tau$ 下的两套描述等价，磁单极子与规范粒子互换角色，Wilson 线与 't Hooft 线互换。它把 $\mathcal N=4$ 的 $S$-对偶从「弱–强耦合对偶」提升为**精确的量子对称性**（在有超对称的前提下）。}
\physex{$G=SU(2)$、$\theta=0$ 时 $\tau=4\pi i/g^2$，$-1/\tau=ig^2/4\pi$：强耦合（$g\gg1$）的 $SU(2)$ 理论等价于弱耦合（$g'\ll1$）的 $SO(3)$ 理论。$\theta=\pi$ 时 $\tau$ 落在 $S$ 变换的不动点附近，理论自对偶。}
\bridge{物理侧的对偶群就是数学侧的 ${}^LG$（\S2.1）；$\tau\mapsto-1/\tau$ 是 $S$ 变换，与 $\tau\mapsto\tau+1$ 的 $T$ 变换一起生成 $SL(2,\mathbb Z)$ 的模变换。KW06 的全部几何都建立在这条对应上：$S$-对偶把 A-膜与 B-膜互换，从而把 Hitchin 模空间的辛结构一侧翻译成复结构一侧（\S3--\S5）。}
\intuit{电磁对偶不是「两种理论碰巧一样」，而是同一个理论被两种互补的变量描述：电变量（$A_\mu$、Wilson 线）与磁变量（对偶规范场、't Hooft 线）。直觉上像傅里叶变换：位置与动量互换，但物理不变。靠得住的原因是 $\mathcal N=4$ 的超共形对称性排除了大部分量子修正，使经典对偶成为精确对偶。}
\pitfall{不要把电磁对偶与 T-对偶混为一谈：后者是紧化半径 $R\leftrightarrow 1/R$ 的对偶，作用在弦/规范理论的紧化上；也不要把 $G$ 与 ${}^LG$ 当成同构——它们只在 $G$ 自对偶（如 $SU(N)$、$E_8$）时相同，一般情形 $\pi_1$ 与中心互换，恰好是 KW06 里 't Hooft 通量取值于 $\pi_1(G)$ 而 Wilson 线取值于 $Z({}^LG)$ 的根源。}
\end{word}
```

## 五条轨道与词条分配

以 `REF-TERMS.tsv`（111 条，列：group/en/zh/definition/first/pitfall）为底稿，按组分配：

| 轨道 | 文件 | 覆盖组 | 条数 |
|---|---|---|---|
| T1 对偶、群论、耦合 | `entries/t1-duality.tex` | A 组 14 条 | 14 |
| T2 超对称、扭化、拓扑场论 | `entries/t2-twist.tex` | B 组 14 条 | 14 |
| T3 Hitchin、超凯勒、可积 | `entries/t3-hitchin.tex` | C 组 15 条 | 15 |
| T4 广义复几何、sigma 模型、膜 | `entries/t4-branes.tex` | D 组 18 条 | 18 |
| T5 线算子、特征膜、Hecke | `entries/t5-operators.tex` | E 组 13 + F 组 8 条 | 21 |
| T6 Langlands、D-模、几何背景 | `entries/t6-langlands.tex` | G 组 21 条 | 21 |

每组开头写：

```latex
\track{T1\quad 对偶、群论与耦合常数}{本轨道 14 条：电磁对偶是全书的地基，先把「群怎么对偶、耦合怎么变换、通量取值于谁」三件事钉死。}
```

末尾可加一段「本轨道小结」（3–5 句，说清这一族概念如何串起来），不强制。

## 自检

```bash
cd C:\Users\admin\Downloads\KW06_work\rosetta
python tools/check_track.py entries/t1-duality.tex
```

报告 `errors=0` 才能交。检查项：词条环境配对、四区块是否齐全、禁用命令、Unicode 数学符号、中文比例。

## 参考材料（只读，不许抄整段）

- `REF-TERMS.tsv`：111 条术语的一句话定义、首现位置、易混点（**你的词条要在此基础上展开成四区块**）。
- `../brief/GLOSSARY.tsv`：111 条中英对照与定义。
- `../brief/SPEC.md`：固定译法表（术语必须与译本一致）。
- `../brief/reading/witten2008.txt`（Witten 2008 短综述，13 页）、`../brief/reading/frenkel2009.txt`（Frenkel 2009 综述，32 页）：**必读**，对应关系与直觉多来自这两篇。
- `../交付/翻译源码/zh/*.tex`：KW06 中译本，用 `grep` 找术语在中译本里的具体语境与页码锚点。
- `../../Desktop/数译发布/gitee_shuyi/05_seminar_witten/seminars/SEM-0604151/manuscript/sections/20_layer1_phys.tex`、`21_layer1_geom.tex`：解经本的物理层与几何层，可核对对应关系（**参考其判断，不得整段搬运**）。
