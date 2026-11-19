# part4（§6–§7）校订问题清单

校订对象：`源码/part4_zh.tex`（§6 行列式线丛、§7 计算赫克本征值；原文印刷 p.59–79）。
对照底本：`原文/EN_part4.txt`。校订日期：2026-11-19。

## 一、已改正问题（共 1 处，P2）

| 序号 | 位置(file:line) | 类型 | 原文 | 原译 | 改为 | 依据 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 源码/part4_zh.tex:28 | 误译 | "an isomorphism that can be defined in a universal way and which therefore also gives an isomorphism in families."（`原文/EN_part4.txt:76-78`） | 「……符号 $\cong$ 指可以用一种普适方式定义、因而也能给出族之间同构的同构.」 | 「……符号 $\cong$ 指可以用一种普适方式定义、因而也能在族中给出的同构.」 | "in families" 指在族中逐点同时给出（族的层面），不是在两个族之间比较；原译「族之间」与「同构的同构」均失准。 |

## 二、译注清单（12 条，已实际查证来源）

| 序号 | 位置 | 主题 | 来源 |
| --- | --- | --- | --- |
| 1 | :13 | 行列式线丛与二维手征费米子：截面、Quillen 度量、theta 函数、Pfaffian 平方根 | Quillen 1985（文献 [41]）；nLab "determinant line bundle" |
| 2 | :21–22 | 式 (6.2) 右端是复线而非数；分式记号；Deligne 行列式—上同调配对 | Deligne 1987（文献 [40]）；nLab 同上 |
| 3 | :126 | 万有线丛变换 W→W⊗R 与 gerbe 的 d 次幂扭曲、2-cocycle | 原文 §6.2–§6.3；[KW] §7；nLab "gerbe" |
| 4 | :140 | 自旋结构 = K 的平方根（theta characteristic）；平凡化非典范 | 原文 §6.3、§6.5 脚注；nLab "determinant line bundle" |
| 5 | :140 | Z_n gerbe 的 band、障碍类于 H^2、离散扭转 | [KW] §7；原文 §6.3；nLab "gerbe" |
| 6 | :144 | B 场 2-形式势、B→B+F 大规范变换、H=dB、周期量子化 | 原文 §6.3；[KW] §7；nLab "gerbe (in differential geometry)" |
| 7 | :169 | Quillen 曲率 → (6.24) 线性组合 → (6.25) 辛形式 → 庞加莱线丛 | 原文 §6.4；Quillen 1985（文献 [41]） |
| 8 | :184 | 希钦纤维自对偶：谱覆盖下 $U(N)$ 的纤维（选定 $K^{1/2}$ 后）即 $\Jac(D)$，经 §6.4 配对与谱覆盖翻译 | 原文 §6.5；Hitchin 1987（文献 [13]） |
| 9 | :194 | 式 (6.28) det H*(C,E) 只依赖 det E；线子丛正合列与秩归纳 | 原文 §6.5 |
| 10 | :207 | U(1) 中心与基本群为 Z，电荷与 c_1 无界；对比单非阿贝尔的 Z_N | 原文 §7、§7.1.2、§2.6.6 |
| 11 | :269 | F=2πdω、∫_C F=2πd、φ_0=2πy·d 的归一化验算 → 磁荷 d 的膜 | 原文 §7.1.2；[KW] 式 (3.29) |
| 12 | :329 | 权和 k+rN=Δ；^LG=SU(N) 时 Δ∈N·Z，故无需 U(1) 多重态 | 原文 §7.2.2 |

来源级别：A 级为原文所引原始文献（Deligne 1987、Quillen 1985、Hitchin 1987、[KW]）；B 级 nLab 两页均经 `web_fetch` 实际打开（HTTP 200）并与原文/ A 级交叉后写入；无仅凭 B 级者。nLab 访问日期 2026-11-19。

## 三、已核对范围

- 已核对 §6–§6.1，共 10 段（§6 引言 2 段、§6.1 8 段）。
- 已核对 §6.2–§6.3，共 12 段（§6.2 7 段、§6.3 5 段）。
- 已核对 §6.4–§6.5，共 16 段（§6.4 8 段、§6.5 8 段）。
- 已核对 §7–§7.1.1，共 15 段（§7 引言 2 段、§7.1 无正文、§7.1.1 13 段）。
- 已核对 §7.1.2，共 8 段。
- 已核对 §7.2.1，共 8 段。
- 已核对 §7.2.2，共 5 段。

合计 74 个正文自然段，逐段与 `原文/EN_part4.txt` 对照；式 (6.1)–(6.29)、(7.1)–(7.15) 共 44 式逐式核对符号、上下标、归一化因子与编号；交叉引用 20 处（含 §2.1、§2.6.5、§2.6.6、§3、§3.2、§3.3.1、§4、§4.2、图 1、式 (3.2)(4.6)(4.15)(4.16)(4.30)(5.3) 与脚注 11、1）逐条以 `源码/main.aux` 与原文节号核过，未发现指错；限定词与逻辑连接词（only/just/merely/simply/precisely/if and only if/exactly/necessarily 等）抽查 48 处，全部保真；simple/semisimple 的译法 14 处逐一核对，无错。

## 四、存疑未改

1. **trivial / trivialized 的用词核对**（:154）。英文主句为 "suppose that these flat gerbes are trivial"（`原文/EN_part4.txt:321`，在页末断行；`原文/EN_layout.txt:3365` 同），下句方为 "So G or G′ can be trivialized, but not canonically"（`原文/EN_part4.txt:339`）。两词分工明确：trivial 指 gerbe 本身平凡，trivialize 指「取了扭曲线丛、把它平凡化」。中译「是平凡的」与「都可以平凡化」分别对应，忠实原文，**不改**。核对记录：校订中一度疑原文为 trivialized 并改成「可被平凡化」，经查 PDF 版式（该词后即断页，下页接 "(as flat gerbes, not just topologically)"）确认主句为 trivial，已回退。
2. **原文疑误：$D\otimes \Pic_c(D)$**（:118）。对应 `原文/EN_part4.txt:218-219` "such a universal line bundle is a line bundle W → D ⊗ Pic_c(D)"。万有线丛是族 $D\times\Pic_c(D)$ 上的丛，符号应为乘积 $\times$；中译为忠实照译，按「不改公式符号、不动译者的原文笔误处理」只登记，建议原文校次统一。
3. **原文疑误：$\W=C\times \mathrm{Jac}(C)$**（:238）。对应 `原文/EN_part4.txt:618` "once a universal bundle W = C × Jac(C) is picked"。万有丛应为投影 $\W\to C\times \mathrm{Jac}(C)$（其纤维为 Jac(C)），原文用等号应系笔误；中译照译，未改。
4. **原文疑误：gerbe 基空间不一致**（:140）。`原文/EN_part4.txt:286-290` 先说 "a gerbe over the moduli space M(^LG,C) of ^LG bundles"，但其平凡化开集取 "U ⊂ MH(^LG,C)"，同段末又改为 "defines a Z_n gerbe over MH(^LG,C)"。中译忠实保留这一混用（\M 与 \MH 交替），未改；作者脚注已声明把 \M 换成 \MH 不改变结论，故不影响理解。
5. **符号排版不一致：${\cal G}'$**（:154 末句）。对应 `原文/EN_part4.txt:345` "…universal family of flat trivializations of G (or G′)." 中译作「给出 ${\eG}$（或 ${\cal G}'$）……」，与全文 $\eG'$ 的字形不一致，疑为录入疏漏。因施工细则禁止改动公式符号，只登记未改。
6. **记号复用**：§6.2 的 $\RR$（$\Pic_c(D)$ 上的一维向量空间/线丛）与 §6.3 第二个例子中的 $\mathcal R\to\Pic_c(C)$ 同属「线丛」角色但字形不同，读者易混；系原文记号复用，未改。
