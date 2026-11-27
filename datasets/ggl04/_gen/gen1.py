# -*- coding: utf-8 -*-
"""生成 ggl04 概念卡（前四张）。"""
import json, os
OUT = os.path.join(os.path.dirname(__file__), "..", "cards", "concepts")

cards = []

cards.append({
 "id": "ggl04/concept/brane-quantization",
 "type": "concept",
 "title": "膜量子化：把辛流形量子化成 A-模型的弦空间",
 "aliases": ["brane quantization", "膜量子化构造"],
 "track": "D",
 "summary": "量子化 $(M,\\omega)$ 可由复化 $Y$ 的 A-模型实现：Hilbert 空间取 $(B_{cc},B')$ 弦空间，$\\omega$ 藏在 $B_{cc}$ 的曲率里。",
 "question": "为什么量子化 $(M,\\omega)$ 可以换成复化 $Y$ 上两个 A-膜之间的弦空间？",
 "definition": {
  "text": "取辛流形 $(M,\\omega)$ 的复化 $Y$，配上全纯辛形式 $\\Omega=\\omega_J+i\\omega_K$，并把 A-模型的辛形式取为 $\\omega_Y=\\omega_K$。在 $Y$ 中放两个 A-膜：支撑整个 $Y$、曲率 $F=\\omega_J$ 的秩 1 余各向同性膜 $B_{cc}$，以及支撑在 $M$ 上、带平坦线丛 $L'$ 的秩 1 Lagrange 膜 $B'$。则 $(M,\\omega)$ 的量子化被定义为弦空间 $H=\\{(B_{cc},B')\\text{ strings}\\}$，而非交换代数 $A=\\{(B_{cc},B_{cc})\\text{ strings}\\}$ 自然作用在 $H$ 上。$\\omega$ 完全编码在 $B_{cc}$ 的曲率中，$B'$ 的不同选择则给出 $A$ 的不同模。",
  "notation": "$Y$ 复化，$\\Omega$ 全纯辛形式，$\\omega_J=\\mathrm{Re}\\,\\Omega$，$\\omega_K=\\mathrm{Im}\\,\\Omega$，$B_{cc}$ 典范余各向同性膜，$B'$ 秩 1 Lagrange 膜，$A$ 非交换代数，$M$ 为 $B'$ 的支撑。"
 },
 "key_points": [
  "两个膜分工明确：$B_{cc}$ 把复结构装进曲率 $F=\\omega_J$，于是 $I=\\omega_Y^{-1}F$ 满足 $I^2=-1$；$B'$ 只提供支撑 $M$ 与平坦线丛 $L'$。",
  "被量子化的是 $(M,\\omega_J)$ 而不是 $Y$。额外条件是 $\\omega_J|_M$ 非退化；若 $\\omega_J|_M=0$（$\\ell$ 水平），得到的是 $D$-模而不是量子化（§3.9）。",
  "弦空间起初只是向量空间：作为向量空间它等于 $B$-模型上同调 $\\oplus_i H^i(M,K^{1/2}\\otimes N)$；Hilbert 结构要由反全纯对合 $\\tau$ 另外给出（§2.4）。",
  "代数 $A$ 不依赖 $B'$：同一个 $A$ 作用在所有 $(B_{cc},B)$ 弦空间上。这正是本文与几何量子化最不同的一点，§4 用它把不同实形式的 Chern–Simons 理论放在同一框架里。",
  "A-模型不变量与超 Kähler 极化无关，所以当 $B'$ 是 $(A,B,A)$ 型时，这套量子化与 Kähler 极化下的几何量子化一致（§2.3、§3.9）。"
 ],
 "formulas": [
  "$\\Omega=\\omega_J+i\\omega_K,\\qquad \\omega_Y=\\omega_K$",
  "$I=\\omega_Y^{-1}F,\\quad F=\\omega_J\\;\\Longrightarrow\\; I=\\omega_K^{-1}\\omega_J,\\quad I^2=-1$",
  "$[O_f,O_g]=-i\\hbar\\,O_{\\{f,g\\}_{\\Omega}}$"
 ],
 "theorems": [
  {
   "name": "量子化的弦空间表述",
   "statement": "设 $B'$ 是支撑在 $M\\subset Y$ 上的秩 1 Lagrange A-膜且 $\\omega_J|_M$ 非退化，则 $(B_{cc},B')$ 弦空间 $H$ 给出 $(M,\\omega_J)$ 的一个量子化：$A$ 作用在 $H$ 上，且当 $B'$ 为 $(A,B,A)$ 型时 $H$ 与 Kähler 极化量子化的空间一致。",
   "proof": {
    "status": "sketch",
    "steps": [
     {"no": 1, "text": "$B_{cc}$ 端的费米子边界条件是 $\\psi_+=J\\psi_-$（因 $F=\\omega_J$ 时 $(g-F)^{-1}(g+F)=J$），$B'$ 端是 $\\psi_+=R\\psi_-$，$R$ 在 $TM$ 上为 $+1$、在法丛上为 $-1$。", "why": "两端边界条件相容才有无歧义的开弦谱，这是把 $(B_{cc},B')$ 弦与 $M$ 上的量子化联系起来的出发点。"},
     {"no": 2, "text": "在超 Kähler 极化下 $B'$ 是 $(A,B,A)$ 型，于是 A-模型弦空间等于 $B$-模型的上同调，可用 $\\bar\\partial$ 上同调算成 $\\oplus_i H^i(M,K^{1/2}\\otimes N)$。", "why": "这一步把拓扑弦空间具体化成一个可计算的向量空间，并说明它与几何量子化的全纯截面空间相符。"},
     {"no": 3, "text": "把 $M$ 上的 $\\omega_J$ 与线丛 $N\\otimes K^{1/2}$ 对照，即得 Kähler 极化量子化；$B_{cc}$ 的曲率给出 $\\omega$，故 $\\omega$ 只出现在 $B_{cc}$ 一侧。", "why": "这是「$\\omega$ 编码在 $B_{cc}$ 里」的准确含义，也是整套构造能反过来当定义用的原因。"}
    ],
    "gap_note": "第 3 步的「一致」在原文中是逐例验证（§3.2–§3.4、§3.9），没有一般性定理；非超 Kähler 极化下的 Hilbert 结构原文只给出 $\\tau$ 的构造，不保证正定。"
   },
   "source": "A p.19 §2.3"
  }
 ],
 "pitfalls": [
  "不要把 $H$ 说成 $Y$ 的量子化：$Y$ 只是辅助的复化，真正被量子化的是 $M$ 上的 $\\omega_J$。",
  "不要漏掉 $\\omega_J|_M$ 非退化：$\\omega_J$ 在 $M$ 上为零的膜（$\\ell$ 水平）给出 $D$-模，不是量子化。",
  "不要以为 $H$ 天生带正定内积：$\\tau$ 在 $M$ 上不恒等时内积只是非退化而不定，正定性等价于 $M$ 落在 $\\tau$ 的固定点集里。"
 ],
 "related": ["ggl04/concept/canonical-coisotropic-brane", "ggl04/concept/half-form-shift", "ggl04/deriv/periods-to-su2-irrep"],
 "sources": [
  {"text": "A", "section": "2.3. Lagrangian Brane And Quantization", "pages": [19, 19], "anchor": "A p.19 §2.3", "quote": "the symplectic manifold that we will quantize"},
  {"text": "A", "section": "2.1. The A-Model And The Canonical Coisotropic Brane", "pages": [15, 15], "anchor": "A p.15 §2.1", "quote": "This is a rather special condition, but there is a simple way to obey it"},
  {"text": "A", "section": "2.1", "pages": [14, 14], "anchor": "A p.14 §2.1", "quote": "we are interested in a rank 1 coisotropic A-brane whose support is simply"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "A 为主（§1–§2 的构造与条件）；「与 Kähler 极化一致」的适用范围按 §3.9 的逐例讨论写，未推广成定理。最没把握的是 $B'$ 为 $(A,B,A)$ 型时 $H$ 与几何量子化在非紧 $M$ 上的一致性。"
})

cards.append({
 "id": "ggl04/concept/canonical-coisotropic-brane",
 "type": "concept",
 "title": "典范余各向同性膜 $B_{cc}$ 的曲率条件",
 "aliases": ["Bcc brane", "rank 1 coisotropic A-brane"],
 "track": "B",
 "summary": "空间填充的秩 1 余各向同性膜要求 $(\\omega_Y^{-1}F)^2=-1$；取 $F=\\omega_J$ 即得 $B_{cc}$，其边界算子代数 $A$ 是 $\\Omega$ 的形变量子化。",
 "question": "为什么 $F=\\omega_J$ 能给出一个可用的余各向同性膜，它的边界算子代数是什么？",
 "definition": {
  "text": "A-模型取辛形式 $\\omega_Y=\\omega_K$。秩 1 空间填充 A-膜的陈–Paton 曲率 $F$ 必须使 $I=\\omega_Y^{-1}F$ 满足 $I^2=-1$（此时 $I$ 自动可积）。取 $F=\\omega_J$ 时 $I=\\omega_K^{-1}\\omega_J$，正是使 $\\Omega$ 为 $(2,0)$ 型的复结构；任何曲率为 $\\omega_J$ 的酉线丛 $L$ 都给出这样的膜，称为典范余各向同性膜 $B_{cc}$。$B_{cc}$ 的边界算子 $f(X)$ 保持拓扑超对称当且仅当 $f$ 关于 $I$ 全纯，故 $(B_{cc},B_{cc})$ 弦的代数 $A$ 是 $Y$ 上全纯函数环被 $\\Omega$ 的 Poisson 括号形变后的非交换环。",
  "notation": "$\\omega_Y=\\omega_K$ 为 A-模型辛形式，$F$ 为 $B_{cc}$ 的陈–Paton 曲率，$I=\\omega_Y^{-1}F$，$A$ 为 $(B_{cc},B_{cc})$ 弦代数。"
 },
 "key_points": [
  "余各向同性条件只有一个：$(\\omega_Y^{-1}F)^2=-1$。它等价于 $I$ 是可积复结构；$F=\\omega_J$ 是最方便的取法，因为此时 $\\Omega$ 关于 $I$ 为 $(2,0)$ 型。",
  "边界算子判据：$f(X)$ 保持不变当且仅当 $f$ 关于 $I$ 全纯；全部边界可观测量的加性结构是 $H^{0,\\star}_{\\bar\\partial}(Y)$，ghost number 0 部分就是全纯函数。",
  "乘法不是点乘：全纯函数环被 $\\Omega$ 的 Poisson 括号形变为非交换环 $A$，即形变量子化；半经典极限是 $[O_f,O_g]=-i\\hbar\\,O_{\\{f,g\\}}$。",
  "高秩情形：$Y$ 为 $G_{\\mathbb C}$ 的余伴随轨道时 $A=U(\\mathfrak g_{\\mathbb C})/I$，$I$ 由 Casimir 算子减去形变常数 $c'_i$ 生成（§3.10）。",
  "沿 $M$ 选取 $I$ 不受拓扑阻碍，因为 $Sp(2n)_{\\mathbb C}/Sp(2n)$ 可缩；这也是 $B_{cc}$ 能与任意 Lagrange 膜配对的几何原因。"
 ],
 "formulas": [
  "$I=\\omega_Y^{-1}F,\\qquad I^2=-1$",
  "$F=\\omega_J\\;\\Longrightarrow\\; I=\\omega_K^{-1}\\omega_J$",
  "$H^{0,\\star}_{\\bar\\partial}(Y)\\ \\text{的 ghost number }0\\ \\text{部分}=\\text{Hol}(Y),\\qquad \\text{乘法被 }\\Omega\\text{ 的 Poisson 括号形变}$",
  "$A=U(\\mathfrak g_{\\mathbb C})/I,\\qquad I=\\langle O_i-c'_i\\rangle_{i=1}^{r}$"
 ],
 "theorems": [
  {
   "name": "$B_{cc}$ 的存在性与唯一性（超 Kähler 极化下）",
   "statement": "给定复辛流形 $(Y,\\Omega)$ 与酉线丛 $L$（曲率 $\\mathrm{Re}\\,\\Omega$），$A$-模型中存在唯一的空间填充秩 1 余各向同性膜 $B_{cc}$，其曲率为 $\\omega_J=\\mathrm{Re}\\,\\Omega$。",
   "proof": {
    "status": "complete",
    "steps": [
     {"no": 1, "text": "由 $\\Omega=\\omega_J+i\\omega_K$ 与 $I^t\\omega_J=-\\omega_K$、$I^t\\omega_K=\\omega_J$ 可验证 $\\omega_K^{-1}\\omega_J=I$，而 $I^2=-1$。", "why": "$I$ 是给定的复结构，这一步把「取 $F=\\omega_J$」与「$I$ 由 $F$ 反解」对上。"},
     {"no": 2, "text": "于是 $I=\\omega_Y^{-1}F$ 满足余各向同性条件，且 $I$ 可积，故 $(Y,F)$ 定义了一个秩 1 空间填充 A-膜。", "why": "满足条件即存在；线丛 $L$ 的曲率固定为 $F$，故除 $L$ 的同构类外无其它选择。"}
    ],
    "gap_note": ""
   },
   "source": "A p.15 §2.1"
  }
 ],
 "pitfalls": [
  "不要把 $A$ 的乘法当成全纯函数的点乘：$A$ 是形变量子化，只有 $\\hbar\\to0$ 时才退化为交换环。",
  "不要混淆三个复结构：$I$ 由 $F$ 定义（$B_{cc}$ 的全纯方向），$K$ 是 A-模型用的近复结构，$J=KI$ 是使 $\\omega_J$ 为 $(1,1)$ 型的那个。",
  "不要以为任何 $F$ 都行：$(\\omega_Y^{-1}F)^2=-1$ 是硬条件；$F=0$（Lagrange 膜）与 $F=\\omega_J$（$B_{cc}$）是两个极端，中间没有连续族。"
 ],
 "related": ["ggl04/concept/brane-quantization", "ggl04/concept/half-form-shift", "ggl04/concept/cs-quantization"],
 "sources": [
  {"text": "A", "section": "2.1", "pages": [15, 15], "anchor": "A p.15 §2.1", "quote": "We call this A-brane the canonical coisotropic brane and denote"},
  {"text": "A", "section": "2.2. Space of (Bcc, Bcc) Strings", "pages": [17, 17], "anchor": "A p.17 §2.2", "quote": "this ring is deformed to a noncommutative ring that we call A"},
  {"text": "A", "section": "3.10. Groups Of Higher Rank", "pages": [63, 63], "anchor": "A p.63 §3.10", "quote": "The algebra A of (Bcc, Bcc) strings in that case is U(gC)/I"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "A 为主；「唯一性」仅指线丛同构类（原文在 §4 也只用这个意义）。最没把握的是 $I$ 可积性一句：原文说 one can show，未给证明，本卡按引用处理。"
})

cards.append({
 "id": "ggl04/concept/half-form-shift",
 "type": "concept",
 "title": "半形式移位：弦空间里的 $K^{1/2}$",
 "aliases": ["half-form shift", "K^{1/2} anomaly"],
 "track": "D",
 "summary": "零模作用量里的线丛要从 $L\\otimes(L')^{-1}$ 改为 $L\\otimes(L')^{-1}\\otimes K^{1/2}$；这一步使 $S^2$ 上恰好得到 $n$ 维表示。",
 "question": "为什么 $(B_{cc},B')$ 弦空间的线丛必须再乘一个 $K^{1/2}$，它改变了什么？",
 "definition": {
  "text": "沿开弦零模的作用量是 $\\int B_\\mu\\,dx^\\mu/d\\tau\\,d\\tau$，其中 $B$ 是线丛 $N=L\\otimes(L')^{-1}$ 上的联络。但 $N$ 一般不是真正的线丛：把世界面费米子绕常值映照量子化时，真空态构成一个只在「线丛」意义下存在的丛 $W\\to M$，且 $W\\cong K^{1/2}$。因此正确的线丛是 $\\hat N=L\\otimes(L')^{-1}\\otimes K^{1/2}$，而弦空间作为向量空间是 $H=\\oplus_{i=0}^{\\dim_{\\mathbb C}M}H^i(M,K^{1/2}\\otimes N)$。",
  "notation": "$N=L\\otimes(L')^{-1}$，$K$ 为 $M$ 的典范丛，$K^{1/2}$ 为半形式（严格说是 $\\mathrm{Spin}^c$ 结构），$\\hat N$ 为移位后的线丛。"
 },
 "key_points": [
  "移位的来源不是约定而是反常：费米子 Fock 真空丛 $W$ 只在「线丛」意义下良定义，$W\\cong K^{1/2}$ 由基态量子数决定。",
  "在 K-理论意义下 $B'$ 的陈–Paton 结构其实是 $M$ 上平坦的 $\\mathrm{Spin}^c$ 结构，$L'$ 只是它的近似；$K^{1/2}$ 与它合并后才给出真正的线丛 $\\hat N$。",
  "$S^2$ 检验：$M=S^2$、$\\omega_J$ 的面积参数为 $2\\pi n$、$L=\\mathcal O(n)$，而 $K^{1/2}=\\mathcal O(-1)$，故 $H^0(S^2,\\mathcal O(n-1))$ 的维数是 $n$，正是 $SU(2)$ 的 $n$ 维不可约表示（$j=(n-1)/2$）。",
  "若辛流形没有平坦 $\\mathrm{Spin}^c$ 结构（例如 $SO(p,q)$ 的最小轨道，$p+q$ 奇且 $p,q\\ge4$），这套做法就无法定义 $B'$，也就不能这样量子化。",
  "$K^{1/2}$ 同时解释了 $J^2=(n^2-1)/4$ 而不是 $n(n+2)/4$：维数少 1 正是半形式的效应。"
 ],
 "formulas": [
  "$\\hat N=L\\otimes(L')^{-1}\\otimes K^{1/2}$",
  "$H=\\bigoplus_{i=0}^{\\dim_{\\mathbb C}M}H^i(M,K^{1/2}\\otimes N)$",
  "$\\dim H^0(S^2,\\mathcal O(n)\\otimes K^{1/2})=\\dim H^0(S^2,\\mathcal O(n-1))=n$"
 ],
 "theorems": [
  {
   "name": "$S^2$ 上的维数检验",
   "statement": "取 $M=S^2\\subset Y$ 为 $(A,B,A)$ 型 Lagrange 膜，$\\int_{S^2}\\omega_J/2\\pi=n>0$，则 $\\dim H=n$，$H$ 是不可约 $SU(2)$ 表示，$j=(n-1)/2$，$J^2=(n^2-1)/4$。",
   "proof": {
    "status": "complete",
    "steps": [
     {"no": 1, "text": "$M$ 单连通，故 $L'$ 平凡、$N=L$；$\\omega_J$ 的整性给出 $L=\\mathcal O(n)$（$n=\\int_M c_1(L)$）。", "why": "把几何数据换成全纯线丛的度数，才能用 Riemann–Roch 数维数。"},
     {"no": 2, "text": "$K_{S^2}=\\mathcal O(-2)$，故 $K^{1/2}=\\mathcal O(-1)$，于是 $K^{1/2}\\otimes N=\\mathcal O(n-1)$，$\\dim H^0=n$。", "why": "半形式把 $n+1$ 降到 $n$；若忘了 $K^{1/2}$ 会得到 $n+1$ 维，与 (3.21) 的 $J_z$ 谱不符。"},
     {"no": 3, "text": "$n$ 维不可约 $SU(2)$ 表示的 $j=(n-1)/2$，故 $J^2=j(j+1)=(n^2-1)/4$，与 (3.7) 在 $\\mu=n$ 时一致。", "why": "这是原文用 (3.19) 定出 (3.7) 中常数 $-1/4$ 的那一步。"}
    ],
    "gap_note": ""
   },
   "source": "A p.35 §3.2"
  }
 ],
 "pitfalls": [
  "不要把 $K^{1/2}$ 当成可以随手去掉的因子：去掉它 $S^2$ 上会得到 $n+1$ 维表示，与 $J_z$ 谱 (3.21) 直接矛盾。",
  "不要以为 $L'$ 一定是线丛：它其实是平坦 $\\mathrm{Spin}^c$ 结构，只有加上 $K^{1/2}$ 才是线丛；在 $b_1(M)=1$ 时单值性 $\\delta$ 的整数化也要用这个结构来定。",
  "不要把 $K^{1/2}$ 与规范场的反常混淆：这里的移位来自世界面费米子真空丛的族反常，不是四维手征反常。"
 ],
 "related": ["ggl04/concept/brane-quantization", "ggl04/deriv/periods-to-su2-irrep", "ggl04/concept/cs-quantization"],
 "sources": [
  {"text": "A", "section": "2.3", "pages": [22, 22], "anchor": "A p.22 eq (2.15)", "quote": "The description (2.15) of H has an important limitation"},
  {"text": "A", "section": "2.3. General Shift By K1/2", "pages": [25, 25], "anchor": "A p.25 §2.3", "quote": "W is isomorphic to K1/2 (and is not quite well-deﬁned as a line bundle"},
  {"text": "A", "section": "3.2. SU(2)", "pages": [35, 35], "anchor": "A p.35 §3.2", "quote": "Quantization of M with n units of ﬂux gives a Hilbert space H of dimension n"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "A 为主；$S^2$ 维数检验是本卡按 (2.15) 与 $K^{1/2}=\\mathcal O(-1)$ 重算的（原文只说 dimension $n$，未展开半形式那一步），归为 B。最没把握的是 $\\mathrm{Spin}^c$ 结构与 $K^{1/2}$ 的精确对应。"
})

cards.append({
 "id": "ggl04/concept/unitarity-by-tau",
 "type": "concept",
 "title": "反全纯对合 $\\tau$ 与内积的符号",
 "aliases": ["hermitian structure from tau", "tau-involution"],
 "track": "D",
 "summary": "反全纯对合 $\\tau$ 与 CPT 算子 $\\Theta$ 合成反线性映射 $\\Theta\\tau$，给出非退化但不一定正定的内积；正定性等价于 $M$ 落在固定点集里。",
 "question": "$\\tau$ 怎样给弦空间一个 hermitian 内积，什么时候它是正定的？",
 "definition": {
  "text": "设 $\\tau:Y\\to Y$ 是满足 $\\tau^2=1$、$\\tau^*\\omega_K=-\\omega_K$ 的对合。若 $\\tau$ 保持 $B_{cc}$ 的曲率（$\\tau^*\\omega_J=\\omega_J$）并保持 $B'$ 的支撑 $M$，则 $\\Theta\\tau$（$\\Theta$ 为 CPT 反线性算子）把 A-模型送到自身，于是 $H$ 上得到内积 $\\langle\\psi,\\psi'\\rangle=(\\Theta\\tau\\psi,\\psi')$。该内积非退化，但正定当且仅当 $\\tau$ 在 $M$ 上恒等，即 $M$ 是 $\\tau$ 固定点集的一个分支。",
  "notation": "$\\tau$ 反全纯对合，$\\Theta$ 为 CPT 反线性算子，$(\\ ,\\ )$ 为圆盘两点函数给出的配对，$\\langle\\ ,\\ \\rangle$ 为 $H$ 上的 hermitian 形式。"
 },
 "key_points": [
  "三条代数条件合起来等价于「$\\tau$ 是 $(Y,I,\\Omega)$ 的反全纯对合且提升到线丛 $L,L'$」：$\\tau^*\\omega_J=\\omega_J$、$\\tau^*\\omega_K=-\\omega_K$、$\\tau^*\\Omega=\\Omega$。",
  "固定点集每个分支都是中维的，而 Lagrange 的 $M$ 也是中维的，所以 $M$ 可以恰好是一个分支；反过来若 $M$ 是固定点分支，则它自动是 Lagrange 的且 $\\omega_J|_M$ 非退化。",
  "经典极限 $\\langle\\psi,\\psi\\rangle\\approx\\int_M\\psi(\\tau x)\\psi(x)$ 说明：$\\tau$ 若在 $M$ 上非平凡，被积函数不恒非负，范数只能是不定的。",
  "符号结构可计算：在 $J_z$ 本征基下 $h\\psi_s=c(-1)^s\\psi_s$，故范数随 $s$ 交替；偶维表示（$s$ 半整）要求 $c$ 为纯虚，$c=\\pm i$ 之间没有自然选择。",
  "同一表示可以同时有 $SU(2)$-不变与 $SL(2,\\mathbb R)$-不变的内积，因为两者是 $SL(2,\\mathbb C)$ 的 inner real forms：$\\langle\\langle\\psi_1,\\psi_2\\rangle\\rangle=\\langle h\\psi_1,\\psi_2\\rangle$，$h$ 把 $(J_x,J_y,J_z)$ 送到 $(-J_x,-J_y,J_z)$。"
 ],
 "formulas": [
  "$\\tau^*\\omega_J=\\omega_J,\\qquad \\tau^*\\omega_K=-\\omega_K,\\qquad \\tau^*\\Omega=\\Omega$",
  "$\\langle\\psi,\\psi'\\rangle=(\\Theta\\tau\\psi,\\psi')$",
  "$(\\psi_n,\\psi_n)(\\psi_{n+1},\\psi_{n+1})=\\dfrac{|(\\psi_{n+1},J_+\\psi_n)|^2}{(s+n)(s+n+1)-J^2}$",
  "$h\\psi_s=c(-1)^s\\psi_s$"
 ],
 "theorems": [
  {
   "name": "内积的符号变化判据",
   "statement": "设 $J_z$ 的本征值为 $s+n$（$n\\in\\mathbb Z$）且 $a_nb_n<0$，则 $(s+n)(s+n+1)>J^2$ 对所有 $n$ 成立；当 $(s+n)(s+n+1)-J^2<0$ 时相邻两个范数 $\\langle\\psi_n,\\psi_n\\rangle$ 与 $\\langle\\psi_{n+1},\\psi_{n+1}\\rangle$ 反号。",
   "proof": {
    "status": "complete",
    "steps": [
     {"no": 1, "text": "由 (3.38)，$a_nb_n=J^2-(s+n)(s+n+1)$；幺正性给 $a_nb_n<0$，故 $(s+n)(s+n+1)>J^2$。", "why": "这把「幺正」翻译成对 $J^2$ 的不等式，是后面所有范数符号判断的入口。"},
     {"no": 2, "text": "由 (3.42)，$a_nb_n=-|(\\psi_{n+1},J_+\\psi_n)|^2/((\\psi_{n+1},\\psi_{n+1})(\\psi_n,\\psi_n))$；与第 1 步联立即得 $\\langle\\psi_n,\\psi_n\\rangle\\langle\\psi_{n+1},\\psi_{n+1}\\rangle=|(\\psi_{n+1},J_+\\psi_n)|^2/((s+n)(s+n+1)-J^2)$。", "why": "这是原文 (3.44) 的正确形式；原文印成乘积，见 errata E2。"},
     {"no": 3, "text": "分母为负时乘积为负，故两相邻范数反号；$s=0$ 时若 $J^2>n(n+1)$ 的整数 $n$ 共有 $2n_0+2$ 个，符号改变偶数次，但中间 $n_0+1$ 个态的范数为负。", "why": "由此得到互补系列（$-1/4<J^2<0$）正定、$J^2>-1/4$ 出现负范态的结论。"}
    ],
    "gap_note": ""
   },
   "source": "A p.43 eq (3.42)"
  }
 ],
 "pitfalls": [
  "不要以为非退化就等于正定：$\\tau$ 在 $M$ 上不恒等时内积只是不定，这在物理上对应「范数可正可负」的态，不是 Hilbert 空间。",
  "不要把 $\\tau$ 与 $\\tilde\\tau$ 混为一谈：$\\tilde\\tau=h\\tau$ 是另一个对合，用它可以得到 $SL(2,\\mathbb R)$-不变而非 $SU(2)$-不变的内积，两者相差一个 $h$。",
  "不要照抄原文 (3.44) 的乘积形式：按 (3.38) 与 (3.42) 联立应是除法（errata E2），照抄会在 $S^1$ 模型里给出 $((n+1/2)^2+\\nu^2)^2\\ne1$。"
 ],
 "related": ["ggl04/concept/brane-quantization", "ggl04/deriv/casimir-from-curve", "ggl04/concept/harish-chandra-curve"],
 "sources": [
  {"text": "A", "section": "2.4. Unitarity", "pages": [26, 26], "anchor": "A p.26 eq (2.18)", "quote": "So Θτ = τΘ is an antilinear map from the A-model to itself"},
  {"text": "A", "section": "2.4. Unitarity", "pages": [27, 27], "anchor": "A p.27 §2.4", "quote": "The hermitian inner product is not necessarily positive deﬁnite"},
  {"text": "A", "section": "3.5. Hermitian Structure", "pages": [55, 55], "anchor": "A p.55 eq (3.64)", "quote": "Thus the states have alternating positive and negative norms"}
 ],
 "rights": "rewritten",
 "status": "draft",
 "provenance_note": "A 为主；(3.44) 按 errata E2 订正后用。最没把握的是 $c=\\pm i$ 的选择：原文说依赖固定点的选取，本卡只记「无自然选择」，不指定哪个。",
 "corrections": [{"id": "E2", "note": "原文 p.44 式 (3.44) 作 $(\\psi_n,\\psi_n)(\\psi_{n+1},\\psi_{n+1})=(n(n+1)-J^2)|(\\psi_{n+1},J_+\\psi_n)|^2$；由 (3.38) 与 (3.42) 联立应为除以 $(s+n)(s+n+1)-J^2$（$s=0$ 时分母为 $n(n+1)-J^2$）。见 errata E2。"}]
})

for c in cards:
    with open(os.path.join(OUT, c["id"].split("/")[-1] + ".json"), "w", encoding="utf-8") as f:
        json.dump(c, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", c["id"])
