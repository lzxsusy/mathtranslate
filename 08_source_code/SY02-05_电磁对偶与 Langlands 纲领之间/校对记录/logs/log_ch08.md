# log_ch08 —《谱分解 2.0：Tannakian 重构》对照校订

- 章：第 8 章《谱分解 2.0：Tannakian 重构》，原 PDF pp.95–114（`en/ch08_en.txt` 1022 行；`pages/p-095.png`…`p-114.png`）
- 正文：`src/chapters/ch08.tex`（原 941 行 → 改后 942 行）
- 方法：英文逐段读、逐段在中文里找对应句；编号公式 (8.1)–(8.155) 全部对照页面图逐一核符号（编号两侧完全一致，用作对齐锚点）。
- 结论：段落级无整段漏译、无增译，小节顺序与 155 个编号公式（154 个 `\tag` + (8.4) 由 `\diageq` 生成）全部一一对应；发现 P1 2 处、P2 3 项（6 处）、P3 改动 2 处、P3 记录 8 条、新增注释 1 条、GAP 0 处。

## 1. P1（意义层面，已改）

1. `src/chapters/ch08.tex:406`（原文 p.103）
   - 原文：`took G = A to be an abelian variety, i.e. an abelian, connected, projective algebraic group`
   - 原译：`为Abel 簇，即紧连通射影代数群`
   - 判定：`abelian` 在此是「交换的」（Abel 簇＝交换、连通、射影代数群），原译换成「紧」，丢掉「交换」这一限定词。
   - 改为：`为Abel 簇，即交换的、连通的、射影代数群`
   - 依据：p.103 页面图印刷原文；Abel 簇的标准定义（交换性为定义的一部分）。

2. `src/chapters/ch08.tex:866`（原文 p.113）
   - 原文：`since a D-module is a quasi-coherent sheaf which is equivariant for Ĵac`（页面图上 Jac 带帽，即形式群 $\widehat{\mathrm{Jac}}$）
   - 原译：`且对$d\mathrm{Jac}$等变`
   - 判定：帽子被转写成字母 `d`，所指对象由「形式群」变成无意义的 `dJac`；与 (8.89) $G_{dR}=G/\widehat G$ 的形式群记号也不一致。
   - 改为：`且对$\widehat{\mathrm{Jac}}$等变`
   - 依据：p.113 页面图逐字核对（已放大裁剪确认）。

## 2. P2（一致性/记号，已改）

3. monodromy 译名：`单值化` → `单值性`，共 4 处（改后行号）
   - 231：`只要把局部系统送到它的单值性`
   - 679：`对平坦向量丛可以附着以单值性`
   - 719：`它对应于单值性为$\mu$的秩一局部系统`
   - 796：`即单值性`
   - 依据：`src/appendix_glossary.tex` 用「单值性」；ch04/ch05/ch16 亦用「单值性」；「单值化」在中文数学语境里另指 uniformization，易混。

4. `src/chapters/ch08.tex:723`（(8.120) 第二行）
   - 原文（p.110 图）：$\{L_\mu\}\ \longleftrightarrow\ \{O_\mu\}$
   - 原译：两集合之间无符号（`& &`）
   - 判定：印刷图有双向箭头，表示两类小对象在该等价下相匹配；缺箭头使公式只剩并列。
   - 改为：`\{L_\mu\} & \longleftrightarrow & \{O_\mu\}.`

5. `src/chapters/ch08.tex:932`（(8.155) 下排）
   - 原文（p.114 图）：下排 $\mathcal D_{\mathrm{Jac}}$-mod 与 $\QC(\mathrm{Conn}^\flat_1)$ 之间**无**符号
   - 原译：多加了一个 `& \simeq &`
   - 判定：形变各有两条路径、尚未知是否等价，原图刻意不写等价号；多写 $\simeq$ 等于凭空断言。
   - 改为：删去该位置的 `\simeq`，恢复空列。

## 3. P3 改动（已改，均不改变数学）

6. `src/chapters/ch08.tex:53`：`实际上是幺半函子` → `实际上是对称幺半函子`（原文 *symmetric monoidal functor*）。
7. `src/chapters/ch08.tex:414`：`我们现在就把$\QC$写成拟凝聚层的导出范畴` → `我们就用$\QC$来记拟凝聚层的导出范畴`（原文 *we will just write* QC *for*…，原译方向反了但可懂）。

## 4. 新增注释（1 条）

8. `src/chapters/ch08.tex:789`（(8.132) 之后）：原文 “For λ ∈ C^×” 与下文（$t\partial$ 以 $\lambda$ 作用、$M_\lambda\simeq M_{\lambda+n}$、只依赖 $\mu=\exp\lambda$）矛盾，$\lambda$ 应为 $t\partial$ 的特征值即 $\lambda\in\C$。按「照译＋加注」处理，正文不动，注中标 `[译者按（无外部依据）：由上下文内部一致性判定。]`。

## 5. P3 记录（未改，供 lead 参考）

9. 原书 p.106 本身重复一句：`This allows us to add some "spice" (de Rham)…from section 3.6. Now we can add some spice to all of our favorite examples of Cartier duality.` 译本 `ch08.tex:553` 只译一次（删重复句，合理）。
10. `ch08.tex:303`：原文 “then we get: The upshot is that we get an equivalence of sheaves” 本身重复「we get」，译本照译成「那么得到：结论是我们得到层的等价」，读起来拗口（保留原样）。
11. 原书 p.108 右侧橙色批注 `transition`（`src/figures/inline/p108_d1.png`）译本未加脚注说明；p.97 同类批注 `cite` 译本有脚注（`ch08.tex:96`）。
12. §8.3 标题：原文 “Betti vs. de Rham”，译本作「Betti 与 de Rham 的过渡」（把旁注 transition 的意思并入标题；`ch08.tex:654`）。
13. (8.101)(8.102)：印刷原文为 $(\partial x-x\partial=1)$（下标从简），译本规范化成 $\partial_x x-x\partial_x=1$；数学等价，保留译本写法。
14. p.113 “self-duality of the Hitchin integral system” 译本作「Hitchin 系统」（与 sectionkey 一致，未加“积分”）。
15. Abel 簇/Abel 群（本章）与 ch06「阿贝尔」音译不统一，属全书层面，未动。
16. 橙色批注 p.104 引文：图上是 “Starting here, Loc denotes…”，`ch08.tex:470` 脚注引作 “From here on”；语义相同。

## 6. GAP

（无）本章所疑处均能由页面图、上下文或已有资料确定；无 `% [GAP:` 条目。

## 7. 已知点核对（任务说明 §6）

- (8.106) `ch08.tex:633`：与 p.107 印刷一致；既有注解释原文「$\mathcal D_{\bA^1}$-mod $=\{L\varphi\}$」的记法松散及 “for $\bA_{\bA^1}$” 笔误，照译加注，无需改动。
- (8.109) `ch08.tex:649`：p.108 印刷为 $A_{dR}=\bigl(\mathrm{Jac}/\widehat{\bA^1}\bigr)$（含大括号），译本一致；既有注说明形式群应为 $(\widehat{\bA^1})^g$。
- (8.152) `ch08.tex:916`：p.113 印刷两行（$h=0$: $\mathcal O(T^*X)=\C[x_i,\xi_i]$；$h=1$: $\mathcal D_X=\C\langle x_i,\partial_{x_i}\rangle/(\partial_{x_i}x_i-x_i\partial_{x_i}=\delta_{ij}\hbar)$），译本一致；既有注指出 $\delta_{ij}$ 指标不自洽。
- `\diageq{8.4}`：编号 8.4 正确（`\tag` 由 `src/preamble.tex:85-86` 生成）。**但**所用图 `src/figures/inline/p095_d1.png` 左右被裁：图上只剩 “N —≅→ N⊗M —≅→ M” 与下方 id 弧箭头，首尾的 $M\otimes$ 与 $\otimes N$ 被切掉，字面读成 $N\cong N\otimes M\cong M$。图文件我无权改，见 §9 待裁定。

## 8. §7 自检

- `\begin` 191 个 = `\end` 191 个（脚本核对，无环境不配对）。
- 逐行 `$` 奇偶检查：无异常行（已排除 `%` 注释行与 `\$`）。
- `\label`：`ch:08`、`sec:8.1`–`sec:8.4` 共 5 个，无重复；本章无 `\ref`/`\eqref`。
- 交叉引用核对：2.1 节式 (2.1)（80）、3.6 节（291、398）、7.4 节（353）、3.2 与 3.4 节（395）、8.2.4 节（454）、第 7 章（462、476）、例 19/例 37、注 36、定理 4、注 32–44、例 32–40 均在文中且编号与原文一致（`srcex`/`srcrmk`/`srcthm` 硬编码源编号）。
- 改动处已重读上下文，语句通顺；新增注 `% [Tutor Note: … ]` 闭合，全章 `[Tutor Note:` 10 条、`[GAP:` 0 条。
- log 各「改为」字符串均可在 tex 中 grep 到（已核）。

## 9. 存疑待裁定（跨章 / 无权处理）

- **p095_d1.png 裁切缺陷**（P2 图文）：(8.4) 交换图左右缺项，见 §7。需重新从 p.95 裁图（图目录属公共资产，未动）；或改用 LaTeX 重排（本章对 p102_d1、p104_d2、p113_d1 已有先例）。
- **skyscraper 译名跨章不一致**（P2）：本章用「天穹层」（`ch08.tex:701` sectionkey、719、738 sectionkey、775、795、805、846），`src/appendix_notes.tex:482` 亦作「天穹层」；而 ch06/ch10/ch11/ch15/ch16 用「摩天楼层/摩天大楼层」。sectionkey 与附录均不在我可改范围，须全书统一。
- §8.3 标题「Betti 与 de Rham 的过渡」（见 §5 第 12 条）：若 lead 要求严格对应 “Betti vs. de Rham”，可改为「Betti 对 de Rham」。
