# 校对报告 rev-c：第 7、8、10 讲（Heuer）

校对范围：`源码/chapters/lecture07.tex`（p.055–061）、`lecture08.tex`（p.062–069）、`lecture10.tex`（p.079–087）。对照：`工程文件/work/pages/pNNN.txt`、`工程文件/work/glossary.tsv`、`工程文件/STYLE_GUIDE.md`、`资料卡/errata.tsv`。仅出报告，未改动任何 .tex。

## lecture07.tex（第 7 讲，p.055–061）

[严重] lecture07.tex:45 | char K 的条件译反，与底本相反 | 「（当 $\operatorname{char}K\notin\{2,3\}$ 时需要更多项，参见 [Del75]）」 | 「（若 $\operatorname{char}K\not\in\{2,3\}$ 即为此式；否则需要更多项，参见 [Del75]）」——底本 p055 作 "if char K ∉ {2,3}, otherwise more terms are required"

[中等] lecture07.tex:185 | 丢掉双陪集分解，等式不成立 | `X_K:=\GL_2(\Q)\backslash(...)=\Gamma(N)\backslash\HH^\pm` | 右端补 $\coprod$：`=\coprod_{[g]}\ \Gamma(N)\backslash\HH^\pm`（底本 p057 此处为 $\coprod$，提取文本作 "a"）

[中等] lecture07.tex:229 | 环境空间写错：Legendre 族割自 $\mathbb{P}^2_U$，非 $\Pone_U$ | 「从 $\Pone_U\to U$ 中割出」 | 「从 $\mathbb{P}^2_U$ 到 $U$ 中割出」（底本 p058："cut out of P²_U → U"；工程无 `\Ptwo` 宏，须直写 `\mathbb{P}^2_U`）

[中等] lecture07.tex:303 | 底本 (2) 的下标自相矛盾，译文照抄且未注 | `P_{\Gamma(N)\cap\Gamma_0(p^n)}` 可表为 `X_{\Gamma_1(N)\cap\Gamma_0(p^n)}` | 保住原样，另加 `\znoteplain` 说明「底本此处的表示概形记作 $X_{\Gamma_1(N)\cap\Gamma_0(p^n)}$，与模问题 $P_{\Gamma(N)\cap\Gamma_0(p^n)}$ 的下标不一致，疑为 $\Gamma(N)$ 之误」（体例 §2.5 要求原文笔误须在译注说明）

[中等] lecture07.tex:329 | 硬译成病句，箭头含义不明 | 「通过在 $\A^1\to\Pone$ 中取正规化」 | 「把 $\A^1$ 嵌入 $\Pone$，再取 $X$ 在 $\Pone$ 中的正规化」

[中等] lecture07.tex:122 | 译注把收敛原因说错 | 「为使级数在 $w=0$ 附近收敛，…标准定义是 $1/(z-w)^2-1/w^2$」 | 「为使和式在 $|w|\to\infty$ 时收敛（减去 $1/w^2$ 消去主项），…」

[轻微] lecture07.tex:247 | 作者脚注被当成译者按（渲染成【译者按】） | `\znoteplain{原文脚注（11）：我们隐含地用了…}` | 改用正体 `\footnote{（原注 11）…}`，与【译注】/【译者按】区分

[轻微] lecture07.tex:250 | 病句 | 「从 $\C$ 过渡到一般 $\Q$-概形 $S$ 上椭圆曲线的模」 | 「把底数域从 $\C$ 换成一般的 $\Q$-概形 $S$：考虑 $S$ 上椭圆曲线的模」

[轻微] lecture07.tex:333 | 「有限除子」易读成「有限的除子」 | 「把 $X^*$ 想成 $X$ 添上一个有限除子」 | 「把 $X^*$ 想成 $X$ 再添上一个由有限多个点构成的除子」

## lecture08.tex（第 8 讲，p.062–069）

[中等] lecture08.tex:403,405,407,411,415,418 | 上标丢负号：应为 $E^{(p^{-1})}$，现作 $E^{(p-1)}$（字面是 $(p-1)$ 次 Frobenius 扭转，另是一物） | `V\colon E\to E^{(p-1)}`；`E^{(p-1)}:=E\times_{\F_p,F^{-1}}\F_p` | 六处统一改为 $E^{(p^{-1})}$；底本提取丢了上标，按「沿 Frobenius 的逆作基变换」重建（体例 §2 第 5 条）

[中等] lecture08.tex:56 | 作者脚注 14 整条丢失，正文用【译者按】顶替，属漏译+注型错 | `\znoteplain{原文此处有脚注 14，但底本的提取文本中没有该脚注的正文，暂付阙如…}` | 依 p062 书页补回脚注 14 正文，在原位置用 `\footnote`；确实无法取得则把这条工程说明移入 `work/reports/lecture08.md`，正文不留

[轻微] lecture08.tex:353 | 病句（缺谓语） | 「其中 $D\subseteq E[p]$ 秩为 $p$」 | 「其中 $D\subseteq E[p]$ 是秩为 $p$ 的子群」

[轻微] lecture08.tex:89 | 同句「光滑」重复 | 「为光滑函数…构成的光滑 $\GL_2(\Af)$-表示」 | 「为光滑函数…构成的 $\GL_2(\Af)$-表示」

[轻微] lecture08.tex:47 | 译注把作用说成「改变 $T_E$ 这个格」，措辞不确 | 「$\GL_2(\Af)$ 中 $p$-进方向的分量会改变 $T_E$ 这个格」 | 「$\GL_2(\Af)$ 的一般元素不保持 $T_E$，只在 $VE=T_E\otimes_\Z\Q$ 上有作用」

[轻微] lecture08.tex:42 | 「⇒」直译成箭头，中文不顺 | 「我们需要 $\GL_2(\Af)$-作用 $\Rightarrow$ 要在准同源的意义下处理椭圆曲线」 | 「于是需要 $\GL_2(\Af)$-作用，因而要在准同源的意义下考虑椭圆曲线」

## lecture10.tex（第 10 讲，p.079–087）

[中等] lecture10.tex:11 | 定理 10.1 的「在 $N$ 外非分歧」与 errata E20 及数学事实都不符（该表示一般在 $\ell$ 处分歧，而同句只保证 $p\nmid N\ell$ 处无分歧） | 「它在 $N$ 外非分歧，且对一切 $p\nmid N\ell$」 | 「它在 $N\ell$ 外非分歧，且对一切 $p\nmid N\ell$」——按 `资料卡/errata.tsv` E20

[中等] lecture10.tex:261 | 用等号写「$\rho_f$ 已在 $F_f$ 上定义」；$\sigma$ 复合后取值已变，只有同构类相等 | 「有 $\rho_f=\sigma\circ\rho_f$」 | 「有 $\rho_f\cong\sigma\circ\rho_f$」（并在译注或括号说明即「$\rho_f$ 与自己的 $\sigma$-共轭同构」）

[中等] lecture10.tex:317 | 「由下一引理」指代错：下一引理（10.14）讲 $\abs{G_\ell}$ 有界，与「零点落在 $\OO_K$ 中」无关；真正依据是后文扩大 $K$，故正文与本行译注自相矛盾 | 「由下一引理，可以假设它们全在 $\OO_K$ 中」 | 「由于 $K$ 已扩大为含所有 $\le A$ 次单位根（见后文），可以假设它们全在 $\OO_K$ 中」；或在译注开头点明「原文 by the next lemma 指代有误」

[中等] lecture10.tex:356 | 硬译，「施加 $\mathrm{Map}$，再由 $G$ 得到」读不出数学步骤 | 「对上述短正合列施加 $\mathrm{Map}$，再由 $G$ 得到非交换群上同调的长正合列」 | 「对上述短正合列逐项取 $\mathrm{Map}$，再取 $G$-不变元（即 $G$ 上同调），得非交换群上同调的长正合列」

[轻微] lecture10.tex:367 | $K\cap\overline{\Z}_\ell=\OO_{K,(\lambda)}$ 严格说只成立包含号（左端是各 $\lambda'\mid\ell$ 处整数环之交），且与 errata E24 的订正措辞不一致 | 「最后，$K\cap\overline{\Z}_\ell=\OO_{K,(\lambda)}$」 | 「最后，$\OO_{K,(\lambda)}$ 即 $K$ 中 $\lambda$-整元素之环（即 $K\cap\Z_\ell$ 在 $\lambda$ 处的整数环）」——照 E24

[轻微] lecture10.tex:215 | 病句：把公式当介词宾语 | 「$\p$ 为 $K$ 中位于 $p\nmid N$ 之上的位」 | 「$\p$ 是 $K$ 的一个位，其下方是有理素数 $p\nmid N$」

[轻微] lecture10.tex:307 | 硬译 | 「现在把上一节应用于 $p$ 由变动中的 $\ell\in L$ 扮演的情形」 | 「下面把上一节的结论用到 $p$ 取遍 $L$ 中素数的情形」

[轻微] lecture10.tex:391 | 「推论」在中文数学里专指 corollary，此处原文是 Consequence | 「\textbf{推论}：若 $F,G\in Y$ 且 $F\equiv G\pmod\lambda$，则 $F=G$」 | 「\textbf{由此可知}：…」

[轻微] lecture10.tex:231 | 形容词「局部自由」直接作谓语 | 「由于 $\Spec(\mathbb{T}_{\OO_K})\to\Spec(\OO_K)$ 局部自由」 | 「由于 $\Spec(\mathbb{T}_{\OO_K})\to\Spec(\OO_K)$ 是局部自由的（有限平坦）态射」

[轻微] lecture10.tex:324 | 冒号后缺谓语 | 「这就变成纯群论问题：对 $\GL_2(\F_\ell)$ 的子群分类」 | 「这就化为纯群论问题：即对 $\GL_2(\F_\ell)$ 的子群分类」

[轻微] lecture10.tex:114 | 译注括注不精确：超奇异时 $E[p]$ 是 $\alpha_p$ 的自扩张 | 「即 $E[p]$ 为 $\alpha_p$ 的扩张之处」 | 「即 $E[p]$ 为 $\alpha_p$ 的自扩张（$0\to\alpha_p\to E[p]\to\alpha_p\to0$）之处」

[轻微] lecture10.tex:387 | 定义 10.17 的 $Y$ 挂着 $\OO_{K,(\lambda)}$，而 405 行要对无穷多个 $\lambda$ 用同一个 $Y$；宜点明 $L$ 已排除 $\le A$ 的素数，故这些单位根对一切 $\lambda$ 都是整的 | 「其中 $\alpha,\beta\in\OO_{K,(\lambda)}$ 是阶 $\le A$ 的单位根。这是有限集」 | 「其中 $\alpha,\beta$ 取遍 $K$ 中阶 $\le A$ 的单位根（它们对一切 $\ell\in L$ 处的 $\lambda$ 都是 $\lambda$-整的），这是有限集」

[轻微] lecture10.tex:59,96 | 标签「回忆」未加粗，与「上次」「要点」「注」不一致（体例 §2.2：标签统一加粗） | 「\item 回忆：我们曾把…」 | 「\item \textbf{回忆}：我们曾把…」

[轻微] lecture10.tex:205,225,336,407 | 证明标签后的标点不统一（`\quad` / `。` / 直接接正文） | 「\noindent\textbf{证明}。」 | 统一作 `\noindent\textbf{证明}\quad`

[轻微] lecture10.tex:451 | 图末译注是重排说明，「原图为扫描排版…宜与原书对照」属工程话，按体例 §5 应移出正文 | `\znoteplain{原第 87 页是一张示意图…宜与原书对照。}` | 删去末句，或整条移入 `work/reports/lecture10.md`，正文只留「原图为示意图，此处按七框重排为两行四列交换图」

[轻微] lecture10.tex:149,182,266,349 | 译注里改掉的原文笔误（$\frac{4}{B_k}$、$X^2-a_\ell X+\varepsilon(\ell)$ 漏 $\ell^{k-1}$、$\phi(g)\phi(g)^{-1}$ 残缺）都未登记到 `资料卡/errata.tsv`（E20–E24 未含），与工程 errata 脱节 | 译注内「原文作 X，此处按 Y 译」 | 按 errata 格式补入 `资料卡/errata.tsv`（不动 glossary.tsv）

核对无误、不列为问题（备查）：编号 10.1–10.18 与底本逐一对应；页标记 9 条（p079–087）齐全且位置正确；p079–087 逐页比对未见漏译，Serre 猜想仍作猜想、Khare–Wintenberger（2008）另述为已证结果，没有「以猜想充定理」。$4/B_k\to 2k/B_k$ 的订正正确（$k=4$ 校验得 $240$）；$E_{p-1}\equiv1\equiv\mathrm{Ha}\pmod p$、Brauer–Nesbitt 用法、Deligne–Serre 提升链（10.9–10.18）均与底本一致；E21–E24 已在译注落实。术语「超奇异的/普通的」「Hasse 不变量」「q-展开」与 glossary 一致，底本此处只称 Dirichlet character，未牵涉「旁特征」；另发现 glossary.tsv 第 104、107 行重复登记 Hasse invariant（全表唯一重复键），按冻结规则只报不改。

## 总体评价

第 10 讲是三讲中质量最高的一讲：编号、页标记、条目层级、errata 落实与译注均到位，未见漏译，本讲问题集中在 4 处「表述不严谨／硬译」上。第 7、8 讲的问题则明显更重：第 45 行把 char K 条件译反、第 185 行丢掉 $\coprod$、第 229 行把 $\mathbb{P}^2$ 写成 $\mathbb{P}^1$ 属实义错误，第 8 讲的六处 $E^{(p-1)}$ 与整条缺失的脚注 14 则会被读者理解成另一个对象或直接丢信息，三讲合计 12 处严重/中等项（1 严重 + 11 中等）必须在定稿前改掉。其余为病句、注型与体例细节，可按上面给出的现成改法批量处理，术语层面无需动 glossary。

定稿意见：**不建议现在定稿**；改完上述 12 处严重/中等项、并对第 7、8 讲做一次复读后，可定稿。
