# 页标落点修正（task：tr07 版式审计 A/B/C 三类）

- 执行者：tr01　依据：`reports/audit_layout.md` §1.1–§1.3 + Lead 的裁定与边界（我负责 ch01a / ch01b / ch01c / ch02a / ch02c / ch03b；ch04a、ch04b 交给 tr03）
- 规则：一页内容一个页标；页首若为节/小节标题，标记在该标题之前；证明或公式跨页时，标记落在该页第一段文字或第一个公式之前。
- 页标编号规则复核：全部 16 块逐块跑脚本，**0 处重复、0 处跳号**（N 均等于 PDF 页 − 1）。

## A 类：落点偏后 → 上移（5 处，本批全部完成）

| # | 文件:行（新） | 页标 | 移到哪里 | 依据（原书页首行，页图） |
|---|---|---|---|---|
| 1 | `ch01a.tex:747`（原 781） | p.26 | `\subsection{量子粒子的希尔伯特空间}`（L748）之前 | `p027.png` 首行「1.5.1 Hilbert Space of Quantum Particle」 |
| 2 | `ch01a.tex:801`（原 805） | p.27 | 「这里 $\hat H$ 是哈密顿算子…」（L802）之前 | `p028.png` 首行「Here Ĥ is the Hamiltonian operator, which is a self-adjoint operator…」 |
| 3 | `ch02c.tex:544`（原 546） | p.147 | 「其中 $\mathcal O$ 是 $\mathcal E$ 上适当的函数…」（L545）之前 | `p148.png` 首行「where O is some appropriate function on E and is called an observable」 |
| 4 | `ch02c.tex:607`（原 612） | p.148 | 「比较可知，逆矩阵 $Q^{-1}$ 的类比物是」（L608）之前 | `p149.png` 首行「the analogue of the inverse matrix Q⁻¹ is」 |
| 5 | `ch03b.tex:79`（原 81） | p.181 | 「这里 $a\star b$ 称为符号 $a$ 与 $b$ 的 Moyal 乘积」（L80）之前 | `p182.png` 首行「Here a⋆b is called the Moyal product of symbols a and b」 |

> 第 2、3、4、5 条都落在段落中段（原书在该句中翻页），标记紧贴该句，未增删空行，段落结构不变。

## B 类：冗余重复页标 → 删除（3 处，本批全部完成）

| # | 文件:行（旧） | 页标 | 同页正确页首标记 | 复核依据 |
|---|---|---|---|---|
| 6 | `ch01a.tex:539` | p.21 | `ch01a.tex:482`「量子情形下，上述两种情形的叠加」 | p.21 页首确为该句（p022.png 中 1.4 与 1.4.1 标题都在页中部）；539 位于 `\subsection{交换子与不确定性}` 之后，属同页中部补标 |
| 7 | `ch01a.tex:742` | p.25 | `ch01a.tex:696`「显然正则交换关系成立」 | p.25 页首为 `It is clear that the canonical commutation relation holds` |
| 8 | `ch02a.tex:882` | p.95 | `ch02a.tex:834` `\subsection{配分函数}` | **重要订正**：§2.5 标题与引言在 p.95 页末（`p096.png` 可见「2.5 Asymptotic Method」在该页底部），p.96 页首是「2.5.1 Laplace's Method」（`p097.png`）。故 887 行的 p.96 标记位置正确，882 那条是 p.95 的重复标记，**应删而不是改成 p.96**（我一度按报告改号，核页图后已改回删除） |

删标后各块页标数：ch01a 21→19（= 原书 p.11–29，19 页 ✓）、ch02a 29→28（= p.80–107，28 页 ✓）。

## C 类：页标落在节标题之后 → 上移到标题之前（2 处，本批全部完成；另 2 处与 B 类重叠已随删标解决）

| # | 文件:行（新） | 页标 | 移到哪里 | 依据 |
|---|---|---|---|---|
| 9 | `ch01b.tex:783`（原 785） | p.45 | `\subsection{散射态}`（L784）之前 | `p046.png` 首行「1.8.3 Scattering States」 |
| 10 | `ch01c.tex:51`（原 52） | p.49 | `\subsection{波包散射}`（L52）之前 | `p050.png` 首行「1.9.1 Wave Packet Scattering」 |

> `ch01b` 的行号与审计报告（782）差 3 行，原因是 Lead 在 L38 附近补了 §1.5 的 takeaway；我只动了这一条标记，未碰其他内容。

## 未由我处理（Lead 已转 tr03）

ch04a：`662`(p.204)、`108`(p.195)、`1108`、`1176`、`1427`；ch04b：`234`(p.225)、`388`(p.228)、`933`(p.237)。我开工前收到 Lead 的边界修正，未改动这两块（其页标数现为 ch04a 29、ch04b 19，均已无重复）。

## 自检

- 页标扫描（16 块全覆盖）：`ch01a 19 / ch01b 18 / ch01c 32 / ch02a 28 / ch02b 30 / ch02c 23 / ch03a 18 / ch03b 13 / ch04a 29 / ch04b 19 / ch04c 8 / ch05a 22 / ch05b 25 / ch06a 16 / ch06b 21 / ch99_back 4`，**重复 0、跳号 0**。
- 6 个改动块逐一重编译：

```
ch01a  LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch01a.pdf
ch01b  LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch01b.pdf
ch01c  LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch01c.pdf
ch02a  LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch02a.pdf
ch02c  LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch02c.pdf
ch03b  LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0   DRAFT PDF -> work\tmp_ch03b.pdf
```

- `tools/crosscheck.py` 六块全部「OK 结构与编号一致」，合计 0 块有问题：
  ch01a 原节=21 译节=21 页标=19 陈述=13；ch01b 11/11/18/4；ch01c 22/22/32/10；ch02a 20/21/28/7（§2.5 跨块，预期差 1）；ch02c 6/6/23/19；ch03b 10/10/13/18。
- 改动仅涉及以 `%` 开头的注释行，未改任何正文、公式、图与结构；`ch03a`、`ch04a`、`ch04b`、`ch06a`、`ch06b` 未动。
