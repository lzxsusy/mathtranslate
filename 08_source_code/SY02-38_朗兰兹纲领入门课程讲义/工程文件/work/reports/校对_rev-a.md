# SY02-38 第 2–4 讲译稿校对报告（rev-a）

范围：lecture02.tex（335 行，p003–p010）、lecture03.tex（641 行，p011–p023）、lecture04.tex（467 行，p024–p032）。逐页与 `工程文件/work/pages/pNNN.txt` 对照；底本笔误按 `疑点清单.tsv` 判。计 2 严重、18 中等、10 轻微。未改动任何 .tex。

## 一、lecture02.tex

- **[中等] lecture02.tex:6, 331** | unipotent radical 译作「单根」，与 glossary「幺幂根基」硬冲突，「对其单根取商」易误读为单根理想（全书另作「幂幺根」，见四） | `单根（unipotent radical）`；`而 $P$ 对其单根取商所得为其 Levi 商 $M$` | `幺幂根基（unipotent radical）`；`$P$ 就其幺幂根基取商所得为其 Levi 商 $M$`
- **[中等] lecture02.tex:6** | 硬译，介词结构断裂，读者断不出「基变换」到「代数闭包」的关系 | `若其基变换 $G_{\bar k}$ 到 $k$ 的代数闭包上不包含同构于加法群 $\mathbb{G}_a$ 的闭正规子群` | `若 $G$ 在其代数闭包上的基变换 $G_{\bar k}$ 不含同构于加法群 $\mathbb{G}_a$ 的闭正规子群`
- **[中等] lecture02.tex:178** | 定理 2.3 定语套叠，主语被割裂 | `每个 Galois 群 $\Gal(F/\Q)$ 为 abelian 的有限 Galois 扩张 $F/\Q$ 都包含在 $\Q(\mu_\infty)$ 中` | `每个使 $\Gal(F/\Q)$ 为 abelian 的有限 Galois 扩张 $F/\Q$ 都包含在 $\Q(\mu_\infty)$ 中`
- **[中等] lecture02.tex:215** | profinite 未按中文惯例处理，夹生 | `都是某个实流形的 profinite 覆盖` | `都是某个实流形的射有限（profinite）覆盖`
- **[中等] lecture02.tex:290** | $U(n)$ 应为 $U(2)$：此处 $G(\R)=\GL_2(\C)$，极大紧子群是 $U(2)$（$\dim A_G\backslash\GL_2(\C)/U(2)=3=\dim H^3$）；底本作 $U(n)$，清单未登记 | `可取 $K_\infty\cong U(n)$（酉群）` | `可取 $K_\infty\cong U(2)$（酉群）`，并加译注「原文作 $U(n)$」
- **[中等] lecture02.tex:304** | 实指数破坏酉性：$\chi=|\det|^s$ 要使 $\chi\otimes\pi$ 在 $A_G=\R_{>0}$ 上平凡，须 $\mathrm{Re}(s)=0$ | `$g\mapsto|\det(g)|^s$（某个 $s\in\R_{>0}$）` | `$g\mapsto|\det(g)|^s$（某个 $s\in i\R$）`，加译注说明原文作 $\R_{>0}$
- **[中等] lecture02.tex:325** | 与定理 2.5 自相矛盾：$m$ 是重数函数，$\mu$ 才是测度；本句写「测度 $m$」却用 $\mu(\pi)>0$（底本同误） | `满足 $\mu(\pi)>0$ 的点 $\pi\in\widehat{G(\A)}$ 对 $\widehat{G(\A)}$ 上的测度 $m$ 而言是「离散」的` | `…对 $\widehat{G(\A)}$ 上的测度 $\mu$ 而言是「离散」的`，加译注「原文作 $m$」
- **[中等] lecture02.tex:331** | proper 未译，术语缺中文外壳 | `$G/P$ 是 $\Spec(\Q)$ 上的 proper 概形` | `$G/P$ 是 $\Spec(\Q)$ 上的本征（proper）概形`
- **[轻微] lecture02.tex:68, 86, 311** | 「等类集」非中文数学用语，三处同 | `不可约酉 $G(\A)$-表示的等类集` | `…的同构类`
- **[轻微] lecture02.tex:121 对 127** | 同一记号两种写法，宽帽位置不一 | `\widehat{\bigoplus_{n\in\Z}}\C\chi_n` / `\widehat{\bigoplus}_{n\in\Z}\C\chi_n` | 统一为 `\widehat{\bigoplus}_{n\in\Z}\C\chi_n`（下标在帽外，同原书），并同步 182、321
- **[轻微] lecture02.tex:216** | 页标记前多一空行，违「前后不留空行」 | 空行 + `% ===== PDF p.008 =====` | 删该空行

## 二、lecture03.tex

- **[严重] lecture03.tex:567** | 与紧邻的 563 式互逆：由 $|\widetilde\phi_f|^2=|f(gi)|^2|\operatorname{Im}(g(i))|^k$ 与 $\widetilde\phi_f=|\det|^{k/2}(ci+d)^{-k}f$ 反解得 $|\det(g)|^{1/2}|ci+d|^{-1}=|\operatorname{Im}(g(i))|^{1/2}$；取 $g=\mathrm{diag}(a,d)$ 即验出倒置。底本 p022 写反，且下文「两边在 $K_\infty$、上三角、对角矩阵下不变」只对正确式成立 | `|\det(g)|^{-1/2}|ci+d|\overset{?}{=}|\operatorname{Im}(g(i))|^{1/2}` | `|\det(g)|^{1/2}|ci+d|^{-1}=|\operatorname{Im}(g(i))|^{1/2}`，译注「原文作 …，此处按 … 译」，并登记疑点清单
- **[中等] lecture03.tex:236** | 底本「after pullback to Z/H」与同页公式 $Z\times F\cong(Z\times^HF)\times_{Z/H}Z$ 矛盾（应为 $Z$），译文径改未注 | `即纤维丛 $Z\times^HF$ 拉回到 $Z$ 之后典范地平凡化` | 译文保留，补译注「原文作拉回到 $Z/H$，此处按 $Z$ 译」
- **[中等] lecture03.tex:445** | 底本 p020「modular forms of level k」显系 weight 之误，译文径改为「权 $k$」未注，违 §5 行 72 | `即权 $k$ 的模形式` | 保留现译，补译注「原文作 level $k$」
- **[中等] lecture03.tex:559** | 底本此处用 $|\phi_f(g)|^2$，译文统一为 $|\widetilde\phi_f|^2$（与 563 一致，改得合理但未注） | `$|\widetilde\phi_f(g)|^2$` | 保留，并在译注中一并说明记号统一
- **[轻微] lecture03.tex:586–588** | 「$y=\log(|q|)$」与 $q=e^{2\pi iz}$ 不符（$y=-\log|q|/(2\pi)$），系数也应为 $(2\pi)^{-k}$；底本同误，不影响收敛 | `因为 $y=\log(|q|)$` | 补半句「（按 $q=e^{2\pi iz}$，严格说 $y=-\frac{1}{2\pi}\log|q|$）」
- **[轻微] lecture03.tex:188** | 底本是形容词 weakly modular，译成名词「弱模形式」后与定义 3.1 的「权 $k$ 模形式」并列，读者会当成两类对象 | `$\Gamma$ 的弱模形式` | 首次出现写「弱模的（weakly modular）」，或统一「弱模形式」并加一句说明
- **[轻微] lecture03.tex:169, 440** | 页标记前多一空行 | 空行 + 页标记 | 删
- **[轻微] lecture03.tex:324** | 交叉引用为纯文本，`\label{lem:3.2}` 建而未用（全文无一处 `\hyperref`） | `注意引理 3.2 蕴涵` | `注意\hyperref[lem:3.2]{引理 3.2} 蕴涵`

## 三、lecture04.tex

- **[严重] lecture04.tex:289–293** | 正文排出的分解式不成立：逐项相加得 $\frac12(-1,\,3i;\,-i,\,1)\ne Y$（$i(i\,1;0\,0)=(-1,i;0,0)$）。清单 p.28 决议是「按 $Y=\frac12(0\,0;i\,1)+\frac i2(i\,1;0\,0)$ 改写并加注」，译稿改成保留原式＋译注，正文仍留一个假等式 | `Y=\frac12 I+\frac1{2i}\begin{pmatrix}0&-1\\1&0\end{pmatrix}+i\begin{pmatrix}i&1\\0&0\end{pmatrix}` | 按清单改作 `Y=\frac12\begin{pmatrix}0&0\\i&1\end{pmatrix}+\frac i2\begin{pmatrix}i&1\\0&0\end{pmatrix}`，译注缩为一两句
- **[中等] lecture04.tex:131–135** | 主语错位病句：求导的主体、作用的对象都悬空 | `Lie 代数 $\g:=\mathfrak{gl}_2(\R)\cong\mathrm{Mat}_{2,2}(\R)$ 经右平移对 $\GL_2(\R)$ 的作用求导，而作用在 $C^\infty(\GL_2(\R))$ 上` | `Lie 代数 $\g:=\mathfrak{gl}_2(\R)\cong\mathrm{Mat}_{2,2}(\R)$：把 $\GL_2(\R)$ 的右平移作用求导，就得到它在 $C^\infty(\GL_2(\R))$ 上的作用`
- **[中等] lecture04.tex:221** | 译注公式多一个「(x)」，且 $\phi_f$ 是二元函数 | `$\widetilde\phi_f=|\det|^{k/2}_{\mathrm{ad\acute e lique}}\phi_f(x)$` | `$\widetilde\phi_f=|\det|^{k/2}_{\mathrm{ad\acute e lique}}\phi_f$`
- **[中等] lecture04.tex:108** | 底本 p025「such that $|\det|^{-k/2}$ lies in the image of $\Phi$」漏宾语，译文补成 $|\det|^{-k/2}\phi$ 而未注 | `使得 $|\det|^{-k/2}\phi$ 落在 $\Phi$ 的像中` | 保留，补译注「原文句漏 $\phi$」
- **[中等] lecture04.tex:394** | 底本 p030「$\phi(g,g_\infty z)=z^{-k}\phi(g,g_\infty z)$」右端重出 $z$（原文笔误，否则为恒等式），译文径改未注 | `$\phi(g,g_\infty z)=z^{-k}\phi(g,g_\infty)$` | 保留，补译注「原文右端作 $\phi(g,g_\infty z)$」
- **[轻微] lecture04.tex:293** | 译注给出的逐项和在 $(1,2)$ 项有误（应 $3i/2$，非 $i/2$）；但「把 $+\frac1{2i}$ 改为 $-\frac1{2i}$ 才一致」这个修正结论正确 | `按右边逐项相加得到的是 $\frac12\begin{pmatrix}-1&i\\-i&1\end{pmatrix}$` | 改为 `…得到 $\frac12\begin{pmatrix}-1&3i\\-i&1\end{pmatrix}$，即 $(1,2)$ 与 $(2,1)$ 两项都不对`
- **[轻微] lecture04.tex:123, 174, 295** | 页标记前多一空行（均在 `\end{itemize}` 之后） | 空行 + 页标记 | 删

## 四、跨讲系统性问题

- **[中等] 三讲全部译注的来源格式** | §5 要求 `\znote` 给外部来源（nLab/Stacks 级），只引原文者用 `\znoteplain`；现状是两种都不对：lecture02.tex:88,146,203,205,264 的 `\znoteplain` 只写「原文脚注：…」不给页号；lecture03.tex:82,340,355,357,401,592,630 与 lecture04.tex:135,221,293,358,403,430 的 `\znote` 一律以「[来源：原文第 X 页]」收尾 | 现在写法：`\znoteplain{原文脚注：…}`；`…[来源：原文第 12 页与 \texttt{[Tho, Theorem 1]}]` | 建议：纯原文出处改成 `\znoteplain{…（原文脚注，p.NNN）}`；确有外部依据的补 nLab 链接与访问日期
- **[中等] 底本笔误被静改未注** | 违 §5 行 72「不要在正文里偷偷改掉而不作声」：lecture03.tex:236（$Z/H\to Z$）、445（level $k\to$ 权 $k$）、lecture04.tex:394（$\phi(g,g_\infty z)\to\phi(g,g_\infty)$）、108（补 $\phi$） | 现在写法：译文已按正确式排印，无任何提示 | 建议：正文保留，各处补一句「原文作 X，此处按 Y 译」；并在疑点清单补登 567、290、304、325 四条
- **[中等] unipotent radical 一名三译** | glossary 冻结「幺幂根基」，但全书无人使用：lecture02.tex:6,331 作「单根」，lecture04.tex:430、lecture05.tex:13、lecture11.tex:53、lecture12.tex:31 作「幂幺根」 | 现在写法：`单根`；`把 $\phi$ 沿幂幺根 $N$ 积分` | 建议：报 glossary 维护者定夺后全书统一；「单根」必须改（与 simple root 撞车）
- **[轻微] 结构与编号** | 页标记齐全且与 pNNN 一一对应（8+13+9=30 条），编号（定义 2.1、定理 2.2–2.5、定义 3.1、引理 3.2、定义 3.3）与底本一致，环境配对无误；但 `\label` 一律未配 `\hyperref`，另有 lecture02.tex:216、lecture03.tex:169,440、lecture04.tex:123,174,295 处页标记前多余空行 | 现在写法：`\phantomsection\label{def:2.1}` 后无任何 `\ref` | 建议：按体例改交叉引用为 `\hyperref[...]{定义 2.1}`，删多余空行

## 总体评价

三讲整体忠实底本：页标记、编号、环境与术语骨架都对，没有整句漏译或增译，真正的硬伤只有两处，且都出在底本自身的公式上。第 3 讲 567 式的倒数错必须改（它使紧接的论证不成立），第 4 讲 $Y$ 的分解式应按清单决议改写而不是「保留假等式＋说明」，其余底本笔误（$U(n)$、$s\in\R_{>0}$、测度 $m$、level $k$）宜统一按「加注不径改」处理。体例上最该收口的是译注来源格式与静改未注，这两项机械、量大、不影响理解但直接影响定稿观感。

**建议：小修后定稿**——先处理 2 处严重与 4 处底本笔误的译注，再统一译注来源格式。
