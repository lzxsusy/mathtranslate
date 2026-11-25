# STYLE_GUIDE —— SY02-36《约化群的 Kloosterman 层》

> 本工程的排版与译法细则。与 `04_playbook/01_数学文献翻译纪律.md` 一致；冲突时以纪律为准。

## 一、总体

1. **逐句译，不合并、不拆分段落**。原文一段 = 译文一段；原文一句话跨两段（排版断行）时按语义合成一段。
2. **不增不删**。原文的「由 [19, Cor 1.2] 可知」照译成「由 [19, 推论 1.2] 可知」，不展开证明；需要展开的写进 `\zhnote{}`。
3. **编号照原文**：Theorem 1–4 用 `\begin{mainthm}[1]`…（全局编号）；引理/命题/推论/定义/注/猜想/断言用 `lemma/proposition/corollary/definition/remark/conjecture/claim` 环境，与 `equation` 共用按节计数器。公式编号 `\begin{equation}` 自动给出 `(节.序)`。
4. **作者名、文献编号 `[n]`、节号、页码** 一律不动。

## 二、术语

- 只取 `工程文件/work/glossary.tsv`；新术语先入表再入正文，收工前并入 `TERMS.tsv`。
- 固定译法：Hecke 特征层、局部系统、反常层、模叠、大胞腔、主幂幺元、Swan 导子、野惯性群、驯惯性群、Coxeter 元、拟极小表示、伴随表示、标准表示、拟分裂、钉住。
- **不译**（保留拉丁）：Kloosterman、Satake、Kummer、Artin–Schreier、Iwahori、parahoric、Hecke、Grassmannian（写「仿射 Grassmannian」）、Langlands、Tannakian、Bruhat–Tits、Birkhoff–Grothendieck。
- 群记号：$G$ 为原文的约化群，$\mathbb G$ 为 $\mathbb P^1$ 上的群概形，$\check G$ 为 Langlands 对偶群，$^L G=\check G\rtimes\langle\sigma\rangle$ 为 $L$-群。

## 三、数学排版

- 文档类 `ctexart`，`fandol` 字体；`\linespread{1.22}`；A4，边距 2.5cm。
- 交换图用 `tikz-cd`；表用 `booktabs`（表 1、表 2 用 `tabularx` + `\small`）。
- 记号宏统一在 `preamble.tex` 定义：`\Bun`、`\Gr`、`\Loc`、`\Rep`、`\Perv`、`\IC`、`\AS`、`\Kum`、`\Swan`、`\cO`、`\cF`、`\fu`（$\mathfrak g$ 等）、`\check G` 手写。
- 公式里的 `\mathrm{}` 保持原文字形：$\mathrm{Bun}_G$、$\mathrm{Gr}_{G,\mu}$、$\mathrm{Hk}_V$、$\mathrm{Kl}_{\check G}(\varphi)$。
- 上下标中文字（如「上同调」）不放公式内，用 `\text{}` 或移出公式。

## 四、译注

- 命令：`\zhnote{…}`（行内，转脚注式），每条必须以 `[来源：…]` 或 `[译者按：…]` 结尾。
- 三类必加：(a) 原文省略的群概形/层级细节；(b) 引用跳步的落点；(c) 记号冲突。
- 全篇目标 8–15 条。**不写**「这句话的意思是……」式的复述，只写读者自己推不出来的信息。
- 范例句式：「这里 $j_{!}=j_{*}$ 就是原文所说的 clean（见 [BBD, 5.1]）。[来源：原文引理 2.3 与 [BBD] §5.1]」

## 五、标点与格式

- 中文之间用全角标点（，。；：）；数学公式前后不加空格；公式内标点用半角。
- 破折号用 `——`；引号用「」；书名用《》。
- 不出现 TODO、待补、待核、XXX、???。
- 每块译完 `xelatex` 两遍，收工前三遍。

## 六、页面对账

- 译本页码与原文页码不必一致，但每块开头用 `\routenote{p.XX–p.YY}` 标注对应的原文页范围，便于回查。
- 参考文献按原文顺序 `\bibitem`，编号 `[1]`–`[36]` 与正文引用一致。
