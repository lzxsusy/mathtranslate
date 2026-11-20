# 五次三维簇有理曲线计数：可复现实验包

> 项目：SY01-26《镜像对称与代数几何》（Cox–Katz）中译校订版
> 对应正文：第 2 章瞬子展开、§5.6.4 例 5.6.4（归一化 Yukawa 耦合，式 (5.72)）
> 目的：让读者**自己动手**把书里那串数字算出来，从而直观确认"镜像对称算对了"。

书里（第 2 章 p.29 附近、§5.6.4 例 5.6.4）给出了五次三维簇前 10 个瞬子数

| d | n_d |
|---|---|
| 1 | 2 875 |
| 2 | 609 250 |
| 3 | 317 206 375 |
| 4 | 242 467 530 000 |
| 5 | 229 305 888 887 625 |
| 6 | 248 249 742 118 022 000 |
| 7 | 295 091 050 570 845 659 250 |
| 8 | 375 632 160 937 476 603 550 000 |
| 9 | 503 840 510 416 985 243 645 106 250 |
| 10 | 704 288 164 978 454 686 113 488 249 750 |

这些数最早由 Candelas–de la Ossa–Green–Parkes（1991）用镜像对称算出，
n₁、n₂ 有 19 世纪的 Schubert、Katz 的独立几何论证，n₃ 由 Ellingsrud–Strømme 验证。
本目录的两个程序只用书里写下的公式，**不抄任何现成数值**，逐项算出上表。

## 一、怎么跑

需要 Python 3.8+。程序一是纯标准库，程序二需要 `mpmath`。

```bash
python quintic_gw.py                 # 精确算术版，约 0.01 秒
python quintic_gw_contour.py         # 围道积分版，约 40 秒（需 mpmath）
python quintic_gw.py --to 20         # 想看更多：算到 n_20
```

Windows 下若控制台中文乱码，先 `chcp 65001` 或设 `PYTHONIOENCODING=utf-8`。

输出见同目录 `out_exact.txt`、`out_contour.txt`（本机 2026-11-21 实跑结果）。

## 二、程序做的数学

书 §5.6.4 的闭式（式 (5.72)）：

```
y0(z) = Σ_{n≥0} (5n)!/(n!)^5 (-1)^n z^n
y1(z) = y0(z) log(-z) + 5 Σ_{n≥1} (5n)!/(n!)^5 (H_{5n} - H_n) (-1)^n z^n
q     = exp(y1/y0)                         ← 镜像映射
Y(z)  = 5 / [ (1 + 5^5 z) y0(z)^2 ((q/z)(dz/dq))^3 ]
```

其中 `H_m = 1 + 1/2 + ... + 1/m`。令 `G := y1/y0 - log(-z)`（全纯，`G(0)=0`），
则 `q = -z e^G`，且

```
(q/z)(dz/dq) = 1/(1 + z G'(z))
Y(z) = 5 / [ (1 + 5^5 z) y0(z)^2 (1 + z G'(z))^3 ]
```

第 2 章的瞬子展开是

```
Y(q) = 5 + Σ_{d≥1} n_d d^3 q^d/(1 - q^d)
```

于是 `c_d := [q^d](Y-5) = Σ_{e|d} n_e e^3`，逐 d 反解

```
n_d = d^{-3} ( c_d - Σ_{e|d, e<d} n_e e^3 ).
```

## 三、两个程序为什么算"两条独立路径"

|  | `quintic_gw.py` | `quintic_gw_contour.py` |
|---|---|---|
| 算术 | 有理数 `Fraction`，零误差 | 60 位浮点（mpmath） |
| 求 z(q) | **Lagrange 反演闭式**：`z = Σ (1/n)[z^{n-1}](-e^{-G})^n q^n` | 每个采样点做**牛顿迭代** |
| 取 c_d | 把 Y(z) 复合进级数再读系数 | 沿 `|q|=r` 圆周采样做**离散傅里叶/围道积分** |
| 时间 | ~0.01 s | ~40 s |
| 依赖 | 无 | `mpmath` |

两条路径在实现上没有任何共享代码，结果逐位相同 —— 这比"我自己写一遍、自己信自己"要硬。
仓库里还有第三条路径 `工程文件/工作流/scripts/verify_quintic_frobenius.py`
（逐项复演算，写法更原始），三者结论一致。

## 四、找过哪些现成程序（2026-11-21 检索）

公开可跑的**成熟软件包**其实很少，找到的多是论文附带的脚本或硬编码数值：

- A. Gathmann 的 habilitation（Kaiserslautern）：附带 **Maple** 脚本，用
  `N1 := Phi(FI((5*H2)^6))` 之类手算 GW/相对 GW 不变量，
  <https://agag-gathmann.math.rptu.de/pub/habil.pdf>（代码在文末附录）。
- J. Straat 的 Utrecht 硕士论文：文中提到用 `quintic.py` 算到 d=5，
  并列出 N₀(d) 与 n₀(d) 对照表，<https://utrecht-theses-test.atmire.com/bitstream/handle/20.500.12932/49915/thesis_JesseStraat.pdf>。
- `SuperInstance/lau-mirror-symmetry`（Rust）：`quintic_genus_zero(d)` 只在代码里
  硬编码了 2875、609250 等前几项，不是真算，<https://github.com/SuperInstance/lau-mirror-symmetry>。
- 各类讲义里的公式（CdGP 1991 原始做法、Frobenius 方法）：
  <https://arxiv.org/abs/2610.14189> 给出了用 Γ 函数写出的周期级数通式。

没有找到维护良好、可直接 `pip install` 的"五次三维簇 GW 不变量"包，
所以这里按书里的公式重写，并用两条独立路径互证。若你克隆了本仓库，
直接跑上面两条命令即可复现。

## 五、机器与复现记录

- 环境：Windows 11 + Python 3.13（mpmath 1.3.0）
- 2026-11-21 实跑：`out_exact.txt`（0.01 s，全部 OK）、`out_contour.txt`（43 s，全部 OK）
- 与书第 2 章表格核对：N₁ = 2875、N₂ = 4 876 875、N₃ = 8 564 575 000 均一致
  （N_d = Σ_{e|d} n_e e³）。

**一句话结论**：书里印的那十个数，用书里的公式、在普通笔记本上、
不到一分钟就能重算出来，而且两条互不相关的算法给出完全相同的整数。
