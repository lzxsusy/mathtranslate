# STYLE_GUIDE —— SY02-40《Arkhipov–Bezrukavnikov 等价（Sandvik BunG 讲义）》

> 本工程的排版与译法细则。与 `04_playbook/01_数学文献翻译纪律.md` 一致；冲突时以纪律为准。

## 一、总体

1. **逐句译，不合并、不拆分段落**。原文一段 = 译文一段。
2. **不增不删**。原文的「by [ArBe]」「see Section 2.2 and 10.3 of [AcRi]」照译成「由 [ArBe] 可知」「见 [AcRi] §2.2 与 §10.3」，不展开；需要展开的写进 `yizhu` 环境。
3. **编号照原文**：定理类共用按节计数器，编号形如「节.小节.序号」——§1、§5 无小节，故得 `1.0.1`、`5.0.1`；§2.2 得 `2.2.1`。公式按**全文单一序列**编号 `(1)–(8)`，与原文一致，不按节编号。
4. **脚注照原文**：14 条，顺序不乱，`\footnote{}` 直接嵌在正文对应位置。
5. 作者名、文献编号 `[ArBe]`、节号、页码一律不动。

## 二、术语

- 只取 `工程文件/work/glossary.tsv`；新术语先入表再入正文。
- 固定译法：**中心层**（central sheaf）、**Wakimoto 层**、**附近循环**（nearby cycles）、**反球模**（antispherical module）、**反球 Hecke 范畴**、**反球商**、**Springer 解消**、**倾斜层**（tilting sheaf）、**最高权结构**、**标准层/余标准层**（standard/costandard）、**单值**（monodromy）、**权空间**、**中心仿射 Grassmann 簇**、**仿射旗簇**、**伴随循环**（monodromy 的对数）。
- **不译**（保留拉丁）：Arkhipov–Bezrukavnikov、Wakimoto、Gaitsgory、Bernstein、Mirković、Satake、Tannakian、Iwahori、Whittaker、Hecke、Grassmannian（写「仿射 Grassmann 簇/f簇」）、Langlands、Springer、Bruhat、Artin–Schreier。
- 群与空间记号：$G$ 为原文的约化群（§1–§3 中与 $G^\vee$ 对偶出现），$G^\vee$ 为对偶群，$T^\vee$、$B^\vee$、$U^\vee$、$\mathfrak n^\vee$、$\mathfrak g^\vee$ 随原文；$\widetilde{\mathcal N}$（Springer 解消）、$\widehat{\mathcal N}$、$\widehat{\mathcal N}_X$、$X=\mathrm{Spec}\,\mathcal O(G^\vee/U^\vee)$、$\partial X$ 三个相近记号逐处核对，不改写。

## 三、数学排版

- 文档类 `ctex`（`fontset=windows`）；A4，边距 2.5cm；`\linespread{1.12}`。
- 交换图用 `tikz-cd`（式 (3)、(4)、(7)）；表用 `booktabs`。
- 定理类环境已按「共用计数器 + 小节」定义：`theorem/proposition/lemma/corollary/definition/remark/aside/example`。
- 记号宏统一在 `macros.tex`：`\Coh`、`\Rep`、`\Perv`、`\Fl`、`\Gr`、`\IC`、`\Sat`、`\Zc`（中心函子）、`\PsiC`（附近循环）、`\Wak`（Wakimoto 层 $\mathbb W_\lambda$）、`\AvIW`、`\CAT`（三角范畴）。
- 公式内保持原文字形：$\mathrm{Coh}_{G^\vee}(\widetilde{\mathcal N})$、$\mathcal P_I^{\mathrm{asph}}$、$\mathcal P_{\mathrm{IW}}$、$\mathcal D^b_c(I\backslash \mathrm{Fl}_G)$。

## 四、译注与「本节重点」

- **两套译者所加内容，必须与正文分开**：
  - `\begin{yizhu}[小标题]…\end{yizhu}`：橙框「译注」，编号连续，写原文落点、记号冲突、原文自认的缺口；
  - `\begin{keytakeaways}…\end{keytakeaways}`：蓝框「本节重点」，每节末尾一条，写「这一节在整条链上做了什么」。
- 译注只写读者自己推不出来的信息，**不写**「这句话的意思是……」式的复述。
- 每条译注须有依据：给论文定理号、节号或原文页码。

## 五、标点与格式

- 中文之间用全角标点（，。；：）；公式前后不加空格；公式内标点用半角。
- 破折号用 `——`；引号用「」；书名用《》。
- 不出现 TODO、待补、待核、XXX、???。
- 每节译完 `xelatex` 两遍，收工前跑三遍并以 `0 error` 为准。
