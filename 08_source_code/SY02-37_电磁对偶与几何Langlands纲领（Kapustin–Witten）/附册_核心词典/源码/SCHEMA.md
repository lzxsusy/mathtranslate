# 核心词典写作规范（nLab 严格度）

本册是《数学↔物理 罗塞塔石碑：核心词典》。它与详册（`rosetta/`，107 条查阅型词条）分工不同：
**详册是「查」，本册是「立」**——只取十余个最核心的组件，每个都按百科词条（nLab）的严格度写：
先给精确定义，再给可核对的陈述（定理/猜想/物理推导），再给可手算的例子，最后交代出处与真伪状态。

## 一、词条骨架（必须照此顺序）

```latex
\begin{centry}{中文名}{English Name}{label}
\oneline{一句话说清它是什么、为什么在词典里。}

\begin{definition}[名称]
……精确定义。对象、范畴、方程、参数都要给全。
\end{definition}

\begin{theorem}[名称]
……陈述，含全部假设（群是否单连通、亏格、是否分歧、光滑性等）。
\end{theorem}
\begin{proof}
……证明要点 3–6 行：先说用了什么定理，再说关键一步。
\end{proof}

\physside{物理侧翻译：这个数学对象在 4d $\mathcal N=4$ 理论/2d sigma 模型里具体是什么，
作用在哪个参数或算子上，对应规则写成「数学 $X$ $\leftrightarrow$ 物理 $Y$」。}

\begin{example}[可手算的例子]
低维/低秩的显式例子：$SU(2)$、$g=2$、$\mathbb{P}^1$、$T^2$ 等，给出数或公式。
\end{example}

\statusline{逐条标：哪部分是定理（谁证）、哪部分是猜想、哪部分只是物理推导（KW06 哪节 argued）。
引用格式：KW06 §x.y p.N；Witten 2008 arXiv:0802.0999 §k；Frenkel 2009 arXiv:0906.2747 §k；
原始文献作者年份。**不许编造文献。**}

\dictionaryrow{指向本册其他词条（\ref{core:xxx}）与详册对应词条（`rosetta/entries/...`）。}
\end{centry}
```

## 二、硬性要求

1. **真伪状态**：凡是 KW06 只做物理推导、数学上尚未证明的（例如 §11 的翻译器、§12 的提升），
   **必须**在 `\statusline` 里写明 argued，并说明缺哪一步。
2. **定义自足**：读者只读这一条也能懂；不要在定义里用未定义的记号（首次出现给定义）。
3. **例子可验算**：给具体群、具体亏格、具体维数，最好带上「由公式算出 = 某个数」。
4. **数学保真**：公式用 AMS 环境；不写 Unicode 数学符号；中文全角标点；人名保留原文拼写。
5. **nLab 式交叉引用**：每条结尾至少 2 个 `\ref{core:...}`。
6. 单条 700–1200 汉字（不含公式），比详册的 250–520 汉字更厚。
7. 禁 `\usepackage`/`\newcommand`/`\input`/`table`/`figure`；`centry` 内只用标准 AMS 环境与本导言提供的宏。
8. 编译自检：在 `core/` 目录用
   `export PATH="/c/Users/admin/AppData/Local/Programs/MiKTeX/miktex/bin/x64:$PATH"`，然后
   `xelatex -interaction=nonstopmode chk_<your>.tex`（自己写 `\input{preamble}` 的 wrapper），
   要求 `grep -c '^!' chk_<your>.log` 为 0。

## 三、示范词条（照这个密度与口气写）

```latex
\begin{centry}{电磁对偶}{Electric-Magnetic Duality}{em-duality}
\oneline{四维 $\mathcal N=4$ 超对称杨–米尔斯理论在强耦合与弱耦合之间的精确等价，
它把规范群换成 Langlands 对偶群、把复耦合换成其倒数——整篇 KW06 的起点。}

\begin{definition}[Montonen–Olive 对偶]
设 $G$ 为紧单连通单李群，$\mathfrak g=\mathrm{Lie}(G)$，规范理论有复耦合
\[
\tau=\frac{\theta}{2\pi}+\frac{4\pi i}{g^{2}}\in\mathbb H .
\]
称 $(G,\tau)$ 与 $({}^{L}G,\tau')$ 电磁对偶，若两者的量子理论等价，且
\[
\tau'=-\frac{1}{n_{\mathfrak g}\,\tau},\qquad
n_{\mathfrak g}=\begin{cases}1,&G\ \text{单连通且单边（simply-laced）},\\ 2,3,&\text{否则（按边数）}.\end{cases}
\]
等价的内容包括：规范群整体结构、以及 $(\text{电},\text{磁})=(e,m)$ 荷在 $SL(2,\mathbb Z)$ 下的线性变换。
\end{definition}

\begin{theorem}[单边情形的自对偶点]
若 $G$ 单边、$\theta=0$，则 $\tau=4\pi i/g^{2}$，$S:\tau\mapsto-1/\tau$ 的不动点满足 $g^{2}=4\pi$；
此时理论自对偶，$W$ 玻色子质量 $gv$ 与磁单极子质量 $4\pi v/g$（$=m_W\cdot|\tau|=m_W\cdot4\pi/g^{2}$）在该点相等。
\end{theorem}
\begin{proof}
直接把 $\tau=4\pi i/g^{2}$ 代入 $S$ 变换，解 $g^{2}=4\pi$；质量公式见 KW06 式 (2.3)–(2.5) 的 BPS 公式
$m=|ae+a_{D}m|$，在 $a=v$、$a_{D}=\tau v$ 时给出上述两式。
\end{proof}

\physside{在 4d $\mathcal N=4$ 理论里，$S$-对偶就是「强弱对偶」：它同时作用在三样东西上——
复耦合 $\tau\mapsto-1/(n_{\mathfrak g}\tau)$、规范群 $G\mapsto{}^{L}G$、以及线算子的电荷格
$(e,m)\mapsto(-m,e)$。KW06 §2 只用它作用在 $(\tau,G)$ 上的这一面，因此后文把它当作
「把 $G$-理论送到 ${}^{L}G$-理论」的精确对称性来用。}

\begin{example}[$G=SU(2)$，$\theta=0$]
$g^{2}=4\pi\approx12.57$ 时理论自对偶。若 $v$ 为 Higgs 真空期望值，则
$m_{W}=gv$，$m_{\text{单极子}}=4\pi v/g$；自对偶点两者都等于 $\sqrt{4\pi}\,v$。
\end{example}

\statusline{作为量子场论陈述：Montonen–Olive 1977 提出，Sen 1994 由弦论给出强证据，至今
不是数学定理；但它在 $\mathcal N=4$ 中的**作用在参数上**的形式（$\tau$ 的模变换、$G\to{}^{L}G$）
是 KW06 全文的前提（KW06 §2.2 p.11；Witten 2008 §2）。本册把它列为「词典的入口」。}

\dictionaryrow{它把规范群送到 Langlands 对偶群（\ref{core:lg}）；它作用在 $\tau$ 上又诱导
扭化参数 $\Psi$ 的变换（\ref{core:gl-twist}）；几何 Langlands 的物理化身见 \ref{core:gl}。}
\end{centry}
```

## 四、分工

| 文件 | 词条 |
|---|---|
| `c1-duality.tex` | 电磁对偶；Langlands 对偶群；拓扑扭化与 $\Psi$；Hitchin 模空间与超凯勒结构；Hitchin 纤维化与可积系统 |
| `c2-branes.tex` | A/B 模型与膜的类型；B-膜＝相干层；A-膜＝Lagrange 膜；线算子（Wilson/'t Hooft）；特征膜 |
| `c3-langlands.tex` | Hecke 算子与特征层；单极子模空间＝Hecke 修正空间；D-模与平坦联络；几何 Langlands 对应；翻译器 $B_{cc}$ |

## 五、可引材料

- `C:\Users\admin\Downloads\KW06_work\brief\reading\witten2008.txt`（13 页综述，**必读**）
- `C:\Users\admin\Downloads\KW06_work\brief\reading\frenkel2009.txt`（32 页综述，**必读**，含 Weil 三栏石碑原文）
- `C:\Users\admin\Downloads\KW06_work\zh\*.tex`（KW06 中译本 36 片）与 `skel\`、`kw06_pages\`（原文逐页文本，印刷页 = p 号 − 1）
- `rosetta\entries\*.tex`（详册 107 条，可查定义与例子，但本册要更严格、更短、更聚焦）
- `rosetta\SCHEMA.md`、`brief\GLOSSARY.tsv`（术语统一用「余各向同性」「特征膜」「典范参数」等）
