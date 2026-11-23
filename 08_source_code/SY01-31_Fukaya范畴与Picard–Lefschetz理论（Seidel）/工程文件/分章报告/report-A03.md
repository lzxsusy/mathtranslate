# A03 校对报告（§4 幂等元，§5 扭转，原书印刷页 56–87）

## 一、范围与工作量

分配文件与印刷页范围（印刷页 = 文件内 `\SourcePage{n}` 的 n − 8，见第四节）：

| 文件 | 内容 | 印刷页 | 行数（改后） |
| --- | --- | --- | --- |
| `src/chapters/section-4.tex` | §4 Idempotents：4a 背景、4b 幂等元与 $A_\infty$ 模、4c 分裂闭 $A_\infty$ 范畴 | 55–62 | 210 |
| `src/chapters/section-5.tex` | §5 Twisting：5a 抽象运算、5b Yoneda 模的扭转、5c 判定拟表示对象、5d 函子性 | 63–69 | 269 |
| `src/chapters/section-5-eh.tex` | 5e 扭转的复合、5f 扭曲复形、5g 伴随扭转、5h 球面对象 | 70–75 | 176 |
| `src/chapters/section-5-in.tex` | 5i 例外集、5j 变异、5k Koszul 对偶集、5l Beilinson 型谱序列、5m 有向 $A_\infty$ 范畴、5n 有向子范畴 | 76–84 | 246 |
| `src/chapters/section-5-op.tex` | 5o 再论 Koszul 对偶集、5p 含幺 $A_\infty$ 模 | 85–87 | 78 |

工作方式：先用 `work\en\pages\p056.txt`–`p087.txt` 与 `work\en\bundles\A03.txt` 逐段对读英文原文，对每个公式、交换图、正负号、函子方向逐项核对中文；确认有问题的才改，其余只作记录。共完成：

- **译文修订 1 处**（见第二节）；
- **译者注 17 条**（见第三节），其中 B 级（实际打开 nLab 页面核对）6 条、A 级（原书后文/经典文献）9 条、C 级（上下文推断）2 条；
- 存疑未改 3 项、原书可疑处/笔误 9 项（第四、五节）。

五个文件均通过 `work\tools\check.ps1`，输出 `OK`。

## 二、译文修订表

| # | 文件:行 | 原文 | 改文 | 理由 |
| --- | --- | --- | --- | --- |
| 1 | `src/chapters/section-4.tex:19` | 对任意 $A$，都有一个**自然的**分裂闭包构造 | 对任意 $A$，都有一个**平凡的**分裂闭包构造 | 英文 p55 为 "there is a **tautological** construction of a split-closure"。tautological 指"照定义写出即可、无需论证"，不是"自然"；且"自然"在范畴论中是专门术语（natural transformation），此处误用会造成实质性歧义。注 A03-01 已就地说明该构造的分量形式。 |

其余各段经逐式核对未发现确凿误译，特此记录核对过的重点：§4 的像与直和分解、(4.1)、$PA$ 的分量定义、引理 4.1 的补全论证、(4.2) 与 $\wp^d\in\hom^{1-d}$、Hochschild 复形、抽象像 $\mathcal Z$ 与 (4.3) 中的 $+(−1)^{|b|}\frac{b(q)-b(-q)}{2q}$、引理 4.4 的滤过与 $\partial^{-r,s}$、引理 4.5、$\Pi\A$、引理 4.7/4.8、(4.4)；§5 的 (5.1)(5.2)(5.4)(5.6)(5.7)(5.8)、引理 5.3/5.4/5.6 及 $s$ 映射的两个分量与 $\triangle$、5e 的 (5.12)(5.13) 与推论 5.7/5.8、(5.15)(5.16)、(5.19)(5.20)、球面对象的两条件与引理 5.11 的谱序列论证、(5.21)(5.22)、例外集定义与引理 5.13 的 Postnikov 梯形、变异的三类变换与辫关系、5k 的 (5.25)(5.26)、5l 的 (5.27)–(5.29)、5m 的 (5.30)–(5.32)、5n 的引理 5.20–5.23 与 (5.33)(5.34)、5o 的 (5.35)(5.36)、5p 的推论 5.26/5.27。

## 三、译者注表

| # | 文件:行 | 原书页 | 主题 | 来源级别 |
| --- | --- | --- | --- | --- |
| A03-01 | `src/chapters/section-4.tex:19` | 55 | Karoubi 完备化的分量构造与泛性质 | B（nLab "Karoubi envelope"） |
| A03-02 | `src/chapters/section-4.tex:25` | 56 | 三角结构在幂等完备化上的稳定性 | B（nLab "Karoubi envelope"；Seidel §4a） |
| A03-03 | `src/chapters/section-4.tex:42` | 56 | 同伦幂等元即 $\K\to\A$ 的非含幺 $A_\infty$ 函子 | B（nLab "A-infinity-category"） |
| A03-04 | `src/chapters/section-4.tex:162` | 60 | 分裂生成与 §5 中扭转、分裂闭包的对应 | A（Seidel §5e） |
| A03-05 | `src/chapters/section-5.tex:72` | 64 | 扭转三角 (5.4) 即两对象扭曲复形 | B（nLab "twisted complex"） |
| A03-06 | `src/chapters/section-5.tex:95` | 65 | 为何取反向映射：几何数据给出 $Y_2\to T_{Y_0}Y_1$ 的显式代表 | C（上下文推断） |
| A03-07 | `src/chapters/section-5.tex:262` | 69 | $d=1$ 已给出 $H^0$ 中同构的理由 | A（Seidel §5d） |
| A03-08 | `src/chapters/section-5-eh.tex:7` | 70 | 正合三角分裂 $\Leftrightarrow$ 中段复合为零 | B（nLab "triangulated category"；笔记 3.18） |
| A03-09 | `src/chapters/section-5-eh.tex:43` | 71 | 把映射锥显式写成扭曲复形 | B（nLab "twisted complex"） |
| A03-10 | `src/chapters/section-5-eh.tex:104` | 73 | 球面对象术语与 $S^n$ 的上同调环 | C（上下文推断） |
| A03-11 | `src/chapters/section-5-eh.tex:132` | 74 | $E_1$ 页三项、微分一满一单与维数计数 | A（Seidel §5h） |
| A03-12 | `src/chapters/section-5-in.tex:15` | 76 | 例外对象与例外集（Bondal） | B（nLab "exceptional collection"） |
| A03-13 | `src/chapters/section-5-in.tex:59` | 78 | $\Z^m\rtimes\operatorname{Br}_m$ 的作用与辫关系 | B（nLab "exceptional collection"） |
| A03-14 | `src/chapters/section-5-in.tex:108` | 79 | 对偶基描述的复合与 (5.29) 的 Koszul 符号 | A（Seidel §5k–5l） |
| A03-15 | `src/chapters/section-5-in.tex:133` | 80 | Beilinson 型谱序列与 Atiyah–Hirzebruch 谱序列 | A（Seidel §5l 与笔记 5.18） |
| A03-16 | `src/chapters/section-5-op.tex:35` | 85 | 简单模与 Koszul 对偶集的 Yoneda 模 | A（Seidel §5o、§5p） |
| A03-17 | `src/chapters/section-5-op.tex:78` | 87 | 有向性假设对保持 $\hom$ 有限维的作用 | A（Seidel §5p 与推论 2.14） |

说明：C 级两条（A03-06、A03-10）在注文末尾按 brief 要求写明了"译者按（上下文推断，无外部依据）"。nLab 的 "spherical object" 页面已实际打开核对，但它是同伦论意义（模型范畴中的球面对象），与 Seidel 在三角范畴中定义的球面对象不是同一概念，故 A03-10 未引用该页，改用上下文推断。

## 四、存疑未改

1. **$\Y^!$ 与 $\Y^\sharp$ 的记号**。英文 §5k 记（右）Koszl 对偶集为 $Y^\sharp_{m+1-k}$（OCR 中 ♯ 常显示为空白，但 5o 段 "the $A_\infty$-module $Y^\sharp_{m+1-k}$" 可辨）；中文全篇统一写作 $\Y^!_{m+1-k}$。中文内部自洽，数学内容无误，故未改动，但建议全书统一核对一次（若他章按 ♯ 书写，读者会觉得是两支记号）。
2. **(5.17)/(5.18) 中 $Y_0$、$Y_1$ 的次序**。英文 p71 印作 $Y=\bigoplus_{i\in I}S^{-|b_i|+1}Y_1\oplus Y_0$，随后又说 "$\ast$ is the index for the added row and column corresponding to the $Y_0$ summand"；但 (5.18) 给出 $a^{ji}=(-1)^{\sigma_i+1}\beta^{ji}e_{Y_0}$（$i,j\in I$），即 $I$ 指标项之间用 $e_{Y_0}$ 作恒等。中文写作 $\bigoplus_{i\in I}S^{-|b^i|+1}Y_0\oplus Y_1$、$\ast$ 对应 $Y_1$ 直和项，与 (5.18) 自洽，也与 $T_{Y_0}Y_1=\Cone(\hom(Y_0,Y_1)\otimes Y_0\to Y_1)$ 的形状一致。判定英文三处自相矛盾、中文自洽，故中文保持不动。原书原页图像无法取得（见第 3 项），未能目验。
3. **《原书页图》无法取得**。`work\pages` 仅有 11 张 PNG（p003、p004、p008、p009、p011、p012、p013、p020、p021、p090、p096、p104），其中不含 §4–§5 的任何页；`work\tools\render_page.py` 硬编码的源 PDF（`C:\Users\admin\xwechat_files\…\Seidel, Fukaya categories and Picard-Lefschetz theory(1).pdf`）已不存在，工作区内也无该书 PDF，故所有公式只能依据 `work\en\pages` 的文本层判断。凡涉及符号排布（如 (5.17) 的直和次序、(5.22) 的 0/1 互换）的疑问，均以数学自洽性为准，未做图像核实。
4. **页码标注体系**。文件内的 `\SourcePage{n}` 记的是 PDF 页序号，印刷页 = n − 8（例 `section-4.tex` 的 `\SourcePage{64}` 处实为印刷页 56）。本报告与 17 条注的第一参数一律写印刷页，与 lead 的更正一致；但 `\SourcePage` 标记本身保持原样未改（属不可改对象），全书若有按 `\SourcePage` 直接生成的页边注，需另行统一。

## 五、原书可疑处/笔误（英文侧，中文均已正确，未改中文）

1. p58 引理 4.4：英文作 "$\bold{Hom}(Z)(X_0)$"，应为 "$H(Z)(X_0)$"（中文作 $H(Z)$）。
2. p59 末段："Yoneda $A_\infty$-modules $Y$ associated to objects of $Y$"，后一个 $Y$ 应为 $A$。
3. p61 第 59–67 行：$\mu^2(k,r)=\wp^1$ 与 $\mu^2(k,r)-\mu^1(h)=e_Z$ 两行都印作 $k;r$。按 $\mu^2(b,a)=b\circ a$、$r:Y\to Z$、$k:Z\to Y$，第二行只能是 $\mu^2(r,k)-h=e_Z$（中文正确，勿改）。
4. p71 (5.17)：见第四节第 2 项（$Y_0/Y_1$ 次序三处矛盾）。
5. p74–75 (5.22)：长正合列与替换复形中 $Y_0$、$Y_1$ 的 0/1 两处互换，英文与自身不符（中文正确）。
6. p78 第 47–49 行：$X=Y_l$ 的计算中写成 $0\cong\Hom(X_1,\ldots)$，应为 $X_{l-1}$（中文正确）。
7. p81 (5.31)：印作 $V^1,\ldots,V^d$ 与 $\bigoplus_{i=1}^d$，按上下文应为 $m$（中文作 $m$）。
8. p83 第 33 行："$zU=\mathscr L_k zX$"，应为 $zY$（中文作 $\widetilde Y$）。
9. p83 第 5 行："$D(A^{\to})$ is equivalent to $H^0(A^{\to})$"，应为 $H^0(A)$（中文正确）。

## 六、通读小结（约 520 字）

§4 是全书的"缝合层"：它先把"像""分裂闭""分裂生成"这三个几何上直观、代数上需要造机器的概念摆出来，再从同伦幂等元出发造出幂等元的像，最后证明 $\Pi(\Tw\A)$ 就是 $\A$ 的分裂闭包。译文对这条主线的把握是准的：$PA$ 的分量定义、引理 4.1 用补全交换图把三角结构搬到直和项上、引理 4.7 的唯一性、以及笔记 4.10 用 $\Tw^-\A$ 给出的替代构造，都译得干净。唯一明显的误译是开篇把 tautological 译成"自然的"——这个词在范畴论里有固定含义，读者容易误以为那里有一个自然变换。§5 篇幅长、技术密度高，从抽象扭转 $T_YM$ 一路铺到 Koszul 对偶集、Beilinson 型谱序列、有向 $A_\infty$ 范畴与变异作用，中文在符号层面几乎逐字对得上：扭转三角 (5.4) 的第三个对象、$s$ 映射的两个分量与 $\triangle$ 的取值、(5.19) 的 $\mu^1_{C^\vee}$ 公式、(5.22) 的长正合列、(5.29) 的 Koszul 符号，经核对均无误。凡译文与英文有出入处，查下来多是英文 OCR 自身的问题（$X_{l-1}$ 写成 $X_1$、$V^d$ 应为 $V^m$、$H^0(A)$ 写成 $H^0(A^{\to})$、$Y_0/Y_1$ 次序），中文反而更自洽，这说明译者在这一段是读懂后重写的，而不是逐字搬运。可改进之处集中在"跳步"：5c 为何取反向映射、5d 的 $d=1$ 已给出同构、5h 的 $E_2=0$ 维数计数、5l 与拓扑谱序列的类比，原文都只一句带过，本次补的注即针对这些。另需提醒全书统稿者：$\Y^!$ 与 $\Y^\sharp$ 的记号、以及 `\SourcePage` 与印刷页相差 8 页这两件事，最好在合并全书时一并统一。
