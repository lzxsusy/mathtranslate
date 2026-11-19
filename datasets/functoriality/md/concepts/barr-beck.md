# Barr–Beck 定理

> `functoriality/concept/barr-beck` ｜ track D ｜ draft

**一句话**：Barr–Beck 定理给出伴随 L⊣R 单子性的判据；原文只写两条（BB1 保守、BB2 有余等化子且 L 保持），译者注拆成 BB1–BB3。

**自测**：Barr–Beck 定理为什么需要「保守」与「余等化子」这两类条件，它们分别保证比较函子的哪一半？

## 定义

设 $L\dashv R$ 是伴随对，$T:=RL$ 为相联系的单子，$K:Y\to\Mod T$ 为比较函子。Barr–Beck 定理（原文称 weak tripleability 版本的转述）断言：若 (BB1) $R$ 保守，即反映同构；且 (BB2) $Y$ 具有所有余等化子、$L$ 保持所有余等化子，则 $L\dashv R$ 是单子的，即比较函子 $K$ 是范畴等价。原文只写这两条；译者注指出，把 BB2 拆开就是通常的 BB1/BB2/BB3（保守、具有余等化子、保持余等化子），更精细的版本只要求 $R$-分裂对。本节另举保守函子的例子：$\Grp\to\Set$ 保守，$\Top\to\Set$ 不保守。

记号：$R$：右伴随（遗忘型函子）；$L$：左伴随；$T=RL$：相联系的单子；$K$：比较函子；$\Mod T$：Eilenberg–Moore 范畴。

## 要点

- (BB1) $R$ 保守：$R$ 把同构反射回原范畴，即 $R(f)$ 是同构蕴含 $f$ 是同构。
- (BB2) 原文的写法把两件事压在一起：$Y$ 具有所有余等化子，且 $L$ 保持所有余等化子；拆开就是通常的 BB2（具有余等化子）与 BB3（$L$ 保持余等化子）。
- 有反例说明保守性弱于「$RX\cong RY\Rightarrow X\cong Y$」：同阶有限群之间有双射但未必同构；保守只处理态射。
- 余等化子：对 $f,g:A\rightrightarrows B$，余等化子是 $q:B\to Q$ 使 $q\circ f=q\circ g$ 且对任何这样的 $q'$ 唯一分解；$\Grp$ 中它是商掉 $f(x)g(x)^{-1}$ 生成的正规闭包。
- 定理 5.12 是转述 [Mac71] 习题 VI.7.3 的弱三可表性版本，不是本文证明的定理。

## 公式

$L\dashv R$
$K:Y\to\Mod T$
$f,g:A\rightrightarrows B$
$\Mod T$

## 定理与证明

### 定理 5.12（转述 [Mac71] 习题 VI.7.3 的弱三可表性版本）

设 $L\dashv R$ 为伴随对。若 (BB1) $R$ 保守，且 (BB2) $Y$ 具有所有余等化子、$L$ 保持所有余等化子，则 $L\dashv R$ 是单子的，即比较函子 $K:Y\to\Mod T$ 是范畴等价。原文只写两条条件，译者注把 BB2 拆成 BB2/BB3。

（sketch；来源：原书 p.60–62 §5.7.1（转述 [Mac71] 习题 VI.7.3））

1. 满忠实性：由 (BB1) 与 (BB2) 中的余等化子存在性，可对每个 T-模构造消解，从而比较函子在 Hom 上给出同构。  
   为什么：这是 Beck 单子性定理的标准一半，属于对原文省略证明的补充。
2. 本质满射：需用 $L$ 保持余等化子（BB3）把任一 T-模表为自由 T-模的余等化子，从而落在 $K$ 的本质像中。  
   为什么：这一步说明为何 BB2 不能只理解为「Y 有余等化子」；原文的合并写法正是译者注要拆开之处。

缺口：原文只引述该定理（称其为 weak tripleability）并给出条件，不给证明；以下是标准论证的骨架，细节仍属转述。

## 易错点

- 把 BB1–BB3 说成「原文的三条件」：原文只写两条，(BB2) 合并了「$Y$ 具有所有余等化子」与「$L$ 保持所有余等化子」，拆开才是 BB1/BB2/BB3。
- 把 (BB1) 保守误解为「$RX\cong RY$ 蕴含 $X\cong Y$」：保守只要求反映同构，$\Grp\to\Set$ 保守但同阶群未必同构。
- 把定理 5.12 当本文定理：它是转述 [Mac71] 习题的弱版本，且原文明确说这一形式对普通伴随函子陈述，不是 A∞-函子版本（remark 5.13）。

## 参考与关联

- Abouzaid & Bottman, Functoriality in categorical symplectic geometry (arXiv:2210.11159v1)，§5.7，p.60–62（原书 p.60–62 §5.7）

关联：`functoriality/concept/monad`、`functoriality/concept/eilenberg-moore`、`functoriality/concept/expectation`

来源说明：据中译本 §5.7.1（p.60–62）与译者注转述 [Mac71] 习题 VI.7.3 的弱三可表性版本及保守函子例子。
