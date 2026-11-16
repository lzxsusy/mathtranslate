# 三文对读表：B（Kapustin–Witten 2006）× D（Frenkel 2009）× C（Witten 2008）

> M9 收尾 · T91（P2 + 报告人）。用途：把 B 的八单元精读结果、D 的 Bourbaki 综述、C 的压缩版放在同一张表上，
> 标出每一处"对应"的**证据等级**与**是否真的对上**。**本表只做定位与异同标注，不用 D、C 充当 B 的依据。**

## 0. 体例与原则

| 代号 | 文本 | 篇幅 | locator 约定 | 本表角色 |
|---|---|---|---|---|
| **B** | Kapustin–Witten, *Electric–Magnetic Duality And The Geometric Langlands Program*, hep-th/0604151 | §1–§12，印刷 pp.2–222 | **B p.N = 印刷页 N**；逐页文本 `source/text/p{N+1}.txt`（如 B p.3 = `p004.txt`） | 主文；**推导方**（一手构造） |
| **D** | Frenkel, *Gauge Theory and Langlands Duality*, arXiv:0906.2747 | 32 pp | **D p.N = PDF 页 N**；`work/tmp/D/pNN.txt` | 第一导读；**使用方/综述方** |
| **C** | Witten, *Mirror Symmetry, Hitchin's Equations, and Langlands Duality*, arXiv:0802.0999 | 15 pp | **C p.N = PDF 页 N**；`work/tmp/C/pNN.txt` | 第二导读；**回望方**（压缩重述） |

**证据等级原则（贯穿全表）**：B 给出方程与构造（A 级推导）；D 多为 "we therefore expect" / "has not yet been made mathematically rigorous"（C 级期待）；C 多为 "believed" / "few indications"（C 级重述）。
三文之间的"一致"只表示**陈述一致**，不表示**证明成立**；任何一行都不把 D/C 当作 B 结论的支撑。

**关系枚举**：`同一陈述` / `B 更细致` / `D 更一般` / `C 只提一句` / `仅两类有对应` / `互相矛盾（列出）`。
**一致性判断**：(A) 三方同说 / (B) 两方同说、第三方未提 / (C) 只有一方明说、我们判断相通 / (X) 表述不同需澄清。

---

## 1. 对读表（20 行）

| # | 主题 | B（式号/节＋p.N） | D（节＋p.N） | C（节＋p.N） | 关系 | 一致性判断 |
|---|---|---|---|---|---|---|
| 1 | ① GNO 对偶群 ↔ Langlands 对偶群 ^L G | §1 pp.2–3；Table 1（B p.3）：U(N)↔U(N)、SU(N)↔PSU(N)、Sp(n)↔SO(2n+1)、Spin(2n+1)↔Sp(n)/Z₂、G₂↔G₂、E₈↔E₈；B p.3 句 "the GNO dual group is actually the same as the Langlands dual group ^L G" | §1 p.5：根数据 (X_*(T),X^*(T),Δ,Δ∨) 互换给 ^L G 及对偶群表（SL(n)↔PGL(n)、Sp(2n)↔SO(2n+1)、E₈↔E₈）；引言 (0.1) D p.2 为 Montonen–Olive | §2 p.2："Langlands or Goddard–Nuyts–Olive duality"；SU(N)↔PSU(N)、E₈↔E₈ | 同一陈述 | (A) 三方同说；但**论证不同源**：B 由磁荷量子化（Table 1 是断言），D 由根数据互换，C 只点名 |
| 2 | ② 拓扑扭化与 P¹ 族 TFT（第三种 twist） | §3.1 pp.21–22：第三 twist κ:Spin(4)→Spin(6)、Q=uQ_ℓ+vQ_r、P¹ 族 t=v/u、(3.13) p.22：t→((cτ+d)/\|cτ+d\|)t、(3.14) t∼−t；§3.5 (3.52) pp.35–37、(3.54) p.37：S:Ψ→−1/(n_gΨ) | §4 p.13：三种 twist、第三 twist 引 [KW]、Q=uQ_ℓ+vQ_r、P¹ 族、t=v/u 为 "twisting parameter"；S-对偶伴 t 变即 (4.2) p.14 | §2 p.2 末：quantum GL 段引 "Kapustin & Witten (2007), sections 5.2 and 11.3" | B 更细致 | (B) B/D 同说（D 明确言明"这是 [KW] 的第三种 twist"）；C 只一句带过、未列 P¹ 族 |
| 3 | ③ 紧化到 M_H：4d → 2d | §4.1 p.39：M=Σ×C、Hitchin 方程 (4.1)；§3.2 p.25：t=±i ⇒ Y_M(G)=Hom(π₁(M),G_C)；§1 p.4："four-dimensional S-duality acts as two-dimensional mirror symmetry" | §4 p.14：M4=Σ×X，令 X 很小 ⇒ Σ 上 2d TFT、靶 M_H(G)；p.15 同 | §2 pp.2–3：Hitchin 方程 (2.1)、M_H；p.11：2d σ-模型只是 4d 的近似 | 同一陈述 | (A) 三方同说 |
| 4 | ④ S-对偶 ↔ 镜像对称（Ψ 的作用） | §5.3 p.70：(5.35) S=[[0,1/√n_g],[−√n_g,0]] 令 Ψ↦−1/(n_gΨ)、交换 0/∞；S-对偶 ⇒ B(J) on M_H(G) ≅ A(K) on M_H(^L G)，复合 I:φ↦iφ 得 B(J)↔A(J)，Table 2 pp.70–71；§3.5 (3.54) p.37；§11.3 (11.31)–(11.33) pp.201–204 | §4 p.12 (4.1)：τ 变换与 n_g；p.14 (4.2)：t↦(τ/\|τ\|)t；p.15 "After dimensional reduction 4D to 2D, the S-duality … becomes Mirror Symmetry"；§5.2 p.17 | §2 p.2 镜像问题；§3 p.4：mirror B-model M_H(^L G) in J ↔ A-model M_H(G) ω_K；p.5 明说该结论 "was shown in Kapustin & Witten (2007)" | 同一陈述 | (A) 三方同说；**证据等级不同**：B 是推导方，D 用 "expect/believed"，C 是引用重述 |
| 5 | ⑤ Hitchin 纤维化与纤维上的 A/B 膜（SYZ/T-对偶） | §5.2 pp.65–68、§5.5 pp.74–77：Ξ:B→^LB、F≅ĴF̃、p.77 "This is the usual SYZ picture … except that the map Ξ is usually assumed to be trivial"；§4.3 (4.24) p.53 | §5.1 pp.15–16 (5.1)：两 Hitchin 纤维化同底 B、generic 纤维对偶环面、^LF_b 的点 = F_b 上平坦酉线丛；§5.2 pp.16–17：fiberwise T-duality、"S-duality reduces to T-duality" [HMS]、SYZ | §3 pp.3–4：纤维对 Ω_I Lagrangian、对 ω_K special Lagrangian ⇒ SYZ；"Mirror symmetry is believed to arise from T-duality on the fibers of a special Lagrangian fibration"；对偶纤维化 = ^L G 的 Hitchin 纤维化、两底同（Hausel–Thaddeus） | 同一陈述 | (A) 三方同说（C 用 "believed"，但陈述同一） |
| 6 | ⑥ Wilson/'t Hooft 算子与膜 | §6.1 pp.79–81（(6.1)(6.4)）；§6.2 pp.82–84（'t Hooft 按 ^L G 不可约表示 ^L R 分类，p.84 "the classic GNO duality [10], as recently reinterpreted in terms of operators rather than states"；π₁(G)≅center(^L G)）；§6.4 p.95 (6.22) XB=B⊗V eigenbrane、pp.97–101 | §5.3 p.19：三角上的 Wilson/Hecke 函子与 't Hooft 线算子的"2D 影子"（保持 Higgs 场的修改）、S-对偶交换 't Hooft 与 Wilson、诸等价须与函子交换 | §3.1 p.5：Hecke 算子 "one place that one misses something if one attempts to express this subject just in terms of two-dimensional sigma models" | B 更细致 | (B) B/D 同说同一机制；C 只一句提示、未给算子定义与分类 |
| 7 | ⑦ 特征膜与 π₁(C) 局部系统 | §8 pp.117–123：(8.7) U→U⊗E_p(R) p.119；零膜 = 电特征膜 (8.10) p.121；ϑ:π₁(C)→^L G_C、electric eigenbranes ↔ Hom(π₁(C),^L G_C) p.122；§1 p.5 同 | §5.3 pp.17–20：B-膜 = Y(^L G) 上半稳定平坦丛上的 coherent sheaves（即局部系统一侧）；0-膜 O_E ↦ A-膜 (F_b,∇_E) p.20 | 未提（无 eigenbrane/π₁(C) 语言；仅 C p.1 一般地 Y(G,C)=Hom(π₁(C),G_C)） | 仅两类有对应 | (C) 只有 B 明说；D 用"半稳定平坦丛上的 coherent sheaves"表述同一物，**我们判断相通**（D 自己未点 eigenbrane 一词） |
| 8 | ⑧ 't Hooft = Hecke | §9 pp.123–133：(9.5) "the standard Bogomolny equations" 即用来实现 Hecke 变换 p.127、(9.14)(9.15) p.133；§10 pp.148–183：Hecke 修改空间、(10.34) p.178；§1 p.5 明言对应 | §5.3 p.19：范畴层面的 Hecke 函子 = 't Hooft 线算子的 2D 影子（保持 Higgs 场的修改） | §3.1 p.5：geometric Hecke operators "naturally reinterpreted … in terms of the Bogomolny equations of three-dimensional gauge theory"；§6.1 p.12：Hecke 需不稳定丛 | B 更细致 | (A) 三方同说（详略不同：B 给几何构造，D 抽象到函子，C 一句） |
| 9 | ⑨ Bogomolny 方程与 Hecke 修改空间 | §9.1 pp.126–133（(9.5) p.127、(9.14)(9.15) p.133）；§10 pp.148–183，§10 标题即 "The Bogomolny Equations And The Space Of Hecke Modifications"（p.148），扩展 Bogomolny (10.35) p.179 起 | 正文无 "Bogomolny"（仅参考书目 [Wi6] 标题 p.32）；最接近为 §6.2 p.26：BPS 条件 Q·Ψ=0 降维给 Hitchin 方程 (6.3) | §3.1 p.5 一句："in terms of the Bogomolny equations of three-dimensional gauge theory" | 仅两类有对应 | (B) B/C 同说、D 未提（D 只走 Hitchin 版本，不涉 3d Bogomolny） |
| 10 | ⑩ A-膜 ⇒ D-模（c.c. 膜） | §11 pp.184–206：c.c. 膜 (11.1) p.185；自同态 = K_M^{1/2} 上微分算子 pp.187–194；任意 K 型 A-膜 ⇒ D-模 p.196；Ψ-扭化 (11.31)–(11.33) pp.201–204 | §5.3 p.19：(5.4) A↦Hom(A_cc,A)，Hom(A_cc,A_cc)=微分算子层；紧接 "this argument has not yet been made mathematically rigorous" | §3.1 p.5：B-膜真正对偶应是 M(G,C) 上 D-模，桥 = special A-brane（引 KW §11）；§6.1 p.12：D-模须住 Bun_G stack | 同一陈述 | (A) 三方同说（严谨性分歧见第 20 行） |
| 11 | ⑪ 三类膜 (B,B,B)/(B,A,A)/(A,B,A) | §5.6 pp.77–78：四类 (B,B,B)/(B,A,A)/(A,B,A)/(A,A,B)，脚注 24 排除 (B,B,A)、(A,A,A)；§12 pp.207–221：(12.2) p.209 判据、(12.9) p.211、(12.12) p.211、(12.16) p.213、(12.26) p.216、(12.28) p.217、(12.34) p.220；(B,B,B) pp.211–215、(B,A,A) pp.215–217、(A,B,A) pp.217–221；p.221 用 4d 时间反演排除量子修正 | §6.2 pp.25–28：一般边界条件的 S-对偶（"master duality"），未列三类型表 | 未提 | B 更细致 | (C) 只有 B 明说三类型；D 只给一般框架，**我们判断 D 的框架应涵盖之**（D 未逐类验证） |
| 12 | ⑫ 分歧/野分歧（ramified / wild） | 只做 unramified（自陈 B p.5）；§12 的边界条件构造不涉分歧 pp.207–221 | §5.4 pp.20–22：tame 单极点 / wild 高阶极点；[FGa] 用 affine Kac–Moody critical level 推广 BD；Gukov–Witten surface operators（参数 (α,β,γ)）、镜像是 fiberwise T-对偶；§6.1 pp.22–25 内窥 | §4 pp.5–6：tame 参数 (α,β,γ,η)，对偶映射 (α,η)=(^Lη,−^Lα)；§5 pp.7–10：wild（Stokes 矩阵、Boalch、Biquard–Boalch、等单值形变、辫群） | D 更一般 | (B) D/C 同说、B 自陈未涉及（B p.5 明说只处理 unramified） |
| 13 | ⑬ Kac–Moody/CFT 路线 | 自陈缺：B p.5 "we do not shed light on the utility of two-dimensional conformal field theory" | §2 末 p.9：BD 的 oper 构造用 affine Kac–Moody algebras of critical level，"closely related to QFT, but in a seemingly different way"；§5.4 p.21：[FGa] 同框架推广到分歧、与 [GW1] 结论同 | §4 p.7 一句：ramified GL 与 "algebraic geometry and two-dimensional conformal field theory in Frenkel & Gaitsgory (2005)" 类似（C 中唯一实质 CFT 句） | 仅两类有对应 | (B) D/C 同说、B 自陈缺 |
| 14 | ⑭ 几何 Satake / 仿射 Grassmannian | 未涉 Satake；§9.3 pp.145–148：仿射 Grassmannian Gr_G=G_C(X)/G_C(O) 即 (9.34) p.148，但明言 "We will not really use this framework in the present paper" p.145 | 未点名 "Satake"（全文 grep 0 命中）；其 GLC 陈述走 Hecke 特征层/D-模 §2 pp.6–9（几何 Satake 的近邻表述） | 未提 | 仅两类有对应 | (X) 表述不同需澄清：B 的 Gr_G 正是几何 Satake 的群 ind-scheme，但 B 明言不用；D 无 "Satake" 一词，无法逐句对齐 |
| 15 | ⑮ 量子化 / 量子几何 Langlands | §1 p.4：BD 方案 "based on quantization of M_H" [5] + Fourier–Mukai 半经典；§5.1 pp.56–62：q=−t² (5.12) p.62；§5.4 (5.37) p.71：H_{P,α}=∫_C αP(φ) | §4 p.15 脚注 9：其他参数值给 "quantum geometric Langlands correspondence"；§5.3 p.19：A_cc、微分算子层 | §2 p.2：quantum GL 段（引 KW §§5.2, 11.3）；§4 pp.6–7：tame 参数 η 是"classical geometry 中不可见"的量子参数、在 A-模型中 = 复化 Kähler 类的虚部 | B 更细致 | (X) 表述不同需澄清：B 说"量子化 + Fourier–Mukai"，D/C 说"quantum GL / η 参数"，两组语言未逐条对齐 |
| 16 | ⑯ 为什么不等于证明（严格化路线） | §12 pp.207–222：(12.2)–(12.7) pp.209–211 只是"检查清单"；p.216 (12.26) 的差额 [φ₂,φ₃]−F₂₃=0 只写 "Presumably, the extra term arises as a sort of quantum correction"；p.221 用 4d 时间反演严格化 §11 的 K_M^{1/2} 结论 | §3 pp.9–11：(3.1) 把物理等价表述为范畴等价（数学化框架）；§5.3 p.19 "has not yet been made mathematically rigorous"、Nadler–Zaslow 是另一条严格路线；p.20 "may in fact be made into a precise mathematical conjecture"；§6.2 p.28 真实模空间是 DG stacks | §6 pp.10–14：只给 "indications"（p.1 abstract、p.11）；§6.1 p.12 Bun_G stack；p.5 stacks = "a strong clue for an alternative approach that starts in four-dimensional gauge theory" | 同一陈述 | (A) 三方同说"尚未证明"；**严格化路线不同**：D 走范畴等价、B 走 4d 边界条件检验、C 只承认 indications |
| 17 | ⑰ 空间 vs 栈（Bun_G、扭化/gerbe） | §11.2 pp.196–198：A-膜→D-模、U(1) 例 Jac(C) pp.197–200；§6.4 pp.97–101；全文未用 stack/gerbe 语言，但 §11 已出现 K_M^{1/2} 扭化 | §3 p.10：(3.1) 在 Bun_G 上取 D-模；脚注 7：Z₂-gerbe、需 K_X^{1/2}；§5.3 p.19：左 = Y(^L G) 上半稳定丛 coherent sheaves（与 Loc 的 O-模"相近但不同"）；§6.2 p.28 DG stacks | §3.1 p.5：D-模须住 stack Bun_G；§6.1 p.12：Bun_G、Atiyah–Bott（Y=所有联络、W_C=Maps(C,G_C)） | 同一陈述 | (X) 表述不同需澄清：B 的 K_M^{1/2} 扭化膜与 D 脚注 7 的 Z₂-gerbe/K_X^{1/2} 是同一技术障碍的两种语言，三文未互译 |
| 18 | ⑱ 4d 必要性 / 2d 只是近似 | §12.1 pp.207–211：边界条件必须在 4d 定义，(12.2) p.209；§3.2 p.25；§1 p.4 明言 4d 推导 | §6.2 pp.26–27：2d σ-模型只是近似；连续自同构使 Hitchin 图像失效；C^n/C^× 奇点吞掉 P^{n−1} | §6 p.10：曲率是 2-形式、d 维中 2-形式对偶为 (d−2)-形式，只有 d=4 仍是 2-形式；p.11：2d 只是近似、"Any question that involves those singularities should be addressed in the underlying four-dimensional gauge theory" | 同一陈述 | (A) 三方同说 |
| 19 | ⑲ 边界条件与 Nahm 极点 | §10 pp.148–183：§10.1 Boundary Conditions pp.148–155；单极子冒泡/ADHM pp.155–159；扩展 Bogomolny (10.35)(10.36) pp.179–183 | §6.2 p.27：Gaiotto–Witten——非阿贝尔 Neumann 的 S-对偶不是朴素 Dirichlet，而是 σ 在边界有极点、由 sl₂⊂^L g 的 Nahm 方程决定；对应 Arthur SL₂ | 未提 | 仅两类有对应 | (C) 只有 D 明说；B §10 的边界条件框架是同一问题的另一半，**我们判断相通**（B 未写 Nahm 极点） |
| 20 | ⑳ 量子修正/严格性：4d 论证 vs 数学现状 | §12.4 p.221：用 4d 时间反演使 O,O′ 不能配对，"the cohomology of Q … coincides with the classical result"（即 c.c. 膜上的量子修正不改变结论）；p.216 (12.26) 的 "Presumably" | §5.3 p.19：同一 A-膜/D-模一步 "has not yet been made mathematically rigorous"；Nadler–Zaslow 是另一条严格路线 | p.1 abstract "few indications"；p.11 2d 只是近似（C 未直接评 B §12） | 互相矛盾（列出） | (X)：B 称已在 4d 中排除量子修正、D 称该步未严格化、C 只到 indications；**同一技术结论的证据等级三文相反**，需澄清"严格"指哪一步 |

---

## 2. 按主题密度统计

### 2.1 各文本覆盖行数（以 20 行为分母）

| 文本 | 有 locator 的行 | 正面覆盖（给出实质断言） | 仅一句/间接 | 未涉或自陈缺口 | 作为"最细"方 |
|---|---|---|---|---|---|
| **B** | 20 | 18 | 0 | 2（⑫ 未涉分歧、⑬ 自陈 CFT 缺口） | 5（②⑥⑧⑪⑮） |
| **D** | 20 | 19 | 0 | 1（⑨ 正文无 Bogomolny；⑭ 未用 "Satake" 一词但有 §2 Hecke 特征层） | 1（⑫ 更一般） |
| **C** | 16 | 16 | 5（②⑥⑧⑨⑬ 为一句级） | 4（⑦⑪⑭⑲ 完全未涉） | 0 |

> 读法：B 是**唯一在全部 20 个主题上都有 locator 的文本**（其中 2 行是否定/缺口陈述）；D 的覆盖面几乎与 B 等宽但 18 行里多为综述语气；C 只有 16 行有对应、且 5 行仅一句，主要承担"骨架确认"而非"内容展开"。

### 2.2 关系分布

| 关系 | 行数 | 行号 |
|---|---|---|
| 同一陈述 | 8 | ①③④⑤⑩⑯⑰⑱ |
| B 更细致 | 5 | ②⑥⑧⑪⑮ |
| D 更一般 | 1 | ⑫ |
| 仅两类有对应 | 5 | ⑦⑨⑬⑭⑲ |
| 互相矛盾（列出） | 1 | ⑳ |

### 2.3 一致性分布

| 判断 | 行数 | 行号 |
|---|---|---|
| (A) 三方同说 | 8 | ①③④⑤⑧⑩⑯⑱ |
| (B) 两方同说、第三方未提 | 5 | ②⑥⑨⑫⑬ |
| (C) 只有一方明说、我们判断相通 | 3 | ⑦⑪⑲ |
| (X) 表述不同需澄清 | 4 | ⑭⑮⑰⑳ |

---

## 3. 三条"三文互证最硬"

1. **④ S-对偶 ↔ 镜像对称（Ψ 的作用）** —— B p.70 ((5.35)+Table 2)、D pp.14–15 ((4.2)+(5.1))、C pp.2–4（镜像问题 + mirror B-model M_H(^L G) ↔ A-model M_H(G)）。
   三文是**同一个数学对象、同一条参数映射**（Ψ 或 τ 的 S 变换）的三种写法，措辞可逐句对应；C 甚至明说该结论出自 KW。这是全表最硬的一条。
2. **⑤ Hitchin 双纤维化 + 纤维上的 T-对偶（SYZ）** —— B pp.76–77（F≅ĴF̃、Ξ）、D pp.16–17（"S-duality reduces to T-duality"）、C pp.3–4（special Lagrangian 纤维 + 对偶纤维化=^L G 的纤维化 + Hausel–Thaddeus 同底）。
   三文独立给出"两纤维化共用底 B、generic 纤维互为对偶环面"这同一结构，是 B↔C↔D 唯一的"几何级"互证。
3. **③ 紧化到 M_H（4d→2d）** —— B p.39 ((4.1) M=Σ×C)、D p.14（M4=Σ×X、X 小 ⇒ Σ 上 2d TFT）、C pp.2–3 + p.11（Hitchin 方程 (2.1) 与 M_H、2d 只是 4d 近似）。
   三文对"舞台是 M_H"无异议，且都明说 2d 模型是 4d 的派生；这是整张表的**共同地基**。

## 4. 三条"只有 B 说"

1. **§12 三类膜的 4d 边界条件显式构造与判据** —— (12.2)–(12.7) pp.209–211 的分类判据、(12.9) p.211、(12.12) p.211、(12.16) p.213、(12.26) p.216、(12.28) p.217、(12.34) p.220；§5.6 pp.77–78 的四类膜表与脚注 24 的排除项。
   D 只到 §6.2 的"一般边界条件 S-对偶"抽象层面，C 完全不涉；**没有任何第二份文本复述过这些构造**。
2. **§7 的中心与离散 (e,m) 通量、universal bundle 阻碍** —— (7.8)(7.9) p.106（e∈Hom(H¹(W,Z),U(1))、m∈H²(W,Z)、S:H_{e,m}→H_{−m,e}）、(7.12)(7.13) pp.107–108（ζ=ξ(E_ad)）；p.122 的 ϑ:π₁(C)→^L G_C 与 zerobrane。
   D/C 均未处理离散通量（D p.10 脚注只提 Z₂-gerbe 与 K_X^{1/2}，C 无对应）；这是 B 独有的"离散数据"章节。
3. **§3.3–3.4 的消失定理与拉氏量平方和** —— (3.32) p.28、(3.33) p.29 的消失定理（及其加强版）、(3.47)(3.48) p.34 的 I=I₀+I₁+I₂ 平方和。
   D/C 只引用结论（D p.13 用 Ψ、C p.2 引 KW §§5.2/11.3），**都不重做这些恒等式**；B 的技术核心在另两文中没有对应物。
   （备选：§10.2 的单极子冒泡/ADHM 计算，亦为 B 独有。）

## 5. 最意外的一处不一致（第 20 行展开）

- **B §12.4 p.221**：用 4d 时间反演论证 c.c. 膜上的量子修正被排除 —— O 与 O′ 不能配对，"the cohomology of Q … coincides with the classical result"。这是 B 在 §12 唯一一处宣称把 §11 的 K_M^{1/2} 结论**严格化**。
- **D §5.3 p.19**：同一步 A-膜 ↦ Hom(A_cc,A) 被明确标为 "this argument has not yet been made mathematically rigorous"，并另外给出 Nadler–Zaslow 作为严格化路线。
- **C p.1 / p.11**：全文只给 "few indications"；2d σ-模型只是 4d 近似。

即：**同一技术步骤，B 声称已用 4d 论证排除障碍，D 说尚未严格化，C 说只是迹象**。三者不是互相矛盾的事实，而是**证据等级相反**——读的时候不能把 B 的"已排除"当成定论，也不能把 D 的"未严格"当成否定 B 的推导。第 20 行因此标 `互相矛盾（列出）` + `(X)`。

---

## 6. 抽核记录（共 53 处，全部逐行读页或按方程号 grep 命中）

> 方法：`work/tmp/{D,C}/pNN.txt` 与 B 的 `source/text/p{印刷页+1}.txt` 直接读；方程号用精确 grep（如 `\((3\.13)\)`）确认**所在页**。
> 下表 locator 均为**印刷页/PDF 页**，括号内为实际读的文件。

### 6.1 B（26 处）

| # | B locator | 读法 | 核到的原文锚点 |
|---|---|---|---|
| B-01 | B p.3 | 读 p004.txt | Table 1 首行 + "the GNO dual group is actually the same as the Langlands dual group ^L G" |
| B-02 | B p.4 | 读 p005.txt | "four-dimensional S-duality acts as two-dimensional mirror symmetry"；BD "based on quantization of M_H" |
| B-03 | B p.5 | 读 p006.txt | "'t Hooft operators correspond naturally to geometric Hecke operators"；只 unramified；"we do not shed light on … two-dimensional conformal field theory" |
| B-04 | B p.22 | grep→p023.txt:13 | (3.13) t→exp(2iφ(γ))t |
| B-05 | B p.28–29 | 读 p029/p030.txt | (3.32) p.28（Tr F∧F 的分解）、(3.33) p.29（消失定理的被积式） |
| B-06 | B p.34 | grep→p035.txt:65,72 | (3.47)(3.48) 拉氏量平方和 |
| B-07 | B p.37 | 读 p038.txt | (3.54) S:Ψ→−1/(n_gΨ)，句末 "according to (3.13)" |
| B-08 | B p.39 | grep→p040.txt | (4.1) Hitchin 方程 |
| B-09 | B p.46 | 读 p047.txt | (4.11) 矩映射 μ_J |
| B-10 | B p.48 | 读 p049.txt | (4.19) B=−(Re τ)ω_I |
| B-11 | B p.53 | 读 p054.txt | "The Hitchin fibration … is the map π:M_H→B"；(4.24) 为维数恒等式 Σ(2d_i−1)=dim G |
| B-12 | B p.70 | 读 p071.txt | (5.35) S 矩阵、Ψ↦−1/(n_gΨ)、0↔∞；B(J) on M_H(G) ≅ A(K) on M_H(^L G) |
| B-13 | B p.71 | 读 p072.txt | Table 2 存在；(5.37) H_{P,α}=∫αP(φ) |
| B-14 | B p.76 | 读 p077.txt | "Clearly, S-duality establishes an isomorphism between F and JF̃"；Ξ:B→^LB |
| B-15 | B p.77 | 读 p078.txt | "usual SYZ picture … except that the map Ξ is usually assumed to be trivial"；四类膜 |
| B-16 | B p.84 | 读 p085.txt | 't Hooft 按 ^L G 的不可约表示分类 = "the classic GNO duality"；π₁(G)≅center(^L G) |
| B-17 | B p.95 | 读 p096.txt | (6.22) XB=B⊗V = eigenbrane，"… eigensheaf … Beilinson and Drinfeld" |
| B-18 | B p.106 | 读 p107.txt | (7.8) e∈Hom(H¹(W,Z),U(1))、m∈H²(W,Z)；(7.9) S:H_{e,m}→H_{−m,e} |
| B-19 | B p.122 | 读 p123.txt | ϑ:π₁(C)→^L G_C、electric eigenbrane、GL 主 claim、"at least a glimmering" |
| B-20 | B p.127 | 读 p128.txt | (9.5) "the standard Bogomolny equations"；即用来 "implement Hecke transformations" |
| B-21 | B p.148 | 读 p149.txt | §10 标题 "The Bogomolny Equations And The Space Of Hecke Modifications"；§10.1；(9.34) Gr_G=G_C(X)/G_C(O) |
| B-22 | B p.185 | 读 p186.txt | §11.1 "The Canonical Coisotropic A-Brane"；(11.1) (ω⁻¹F)²=−1 |
| B-23 | B p.196 | 读 p197.txt | §11.2 "D-modules Corresponding to A-Branes"；"every A-brane in complex structure K is a module for the sheaf of differential operators on K_M^{1/2}" |
| B-24 | B p.209 | grep→p210.txt:5 | (12.2) 边界条件判据的起点 |
| B-25 | B p.211 / p.213 | grep→p212.txt:17,35；p214.txt:5 | (12.9)、(12.12)、(12.16) |
| B-26 | B p.216 / p.220 / p.221 | 读 p217/p221/p222.txt | (12.26) "(B,A,A)-brane" 与 "[φ₂,φ₃]−F₂₃=0. Presumably … quantum correction"；(12.34) p.220；p.221 "cohomology of Q … coincides with the classical result" |

### 6.2 D（16 处）

| # | D locator | 读法 | 核到的原文锚点 |
|---|---|---|---|
| D-01 | D p.5 | 读 p05.txt | 根数据 (X_*(T),X^*(T),Δ,Δ∨) 互换 → ^L G；对偶群表 SL(n)↔PGL(n)、Sp(2n)↔SO(2n+1)、E₈↔E₈ |
| D-02 | D p.9 | 读 p09.txt | BD 的 oper 构造用 "affine Kac–Moody algebras of critical level"，"closely related to QFT, but in a seemingly different way" |
| D-03 | D p.10 | 读 p10.txt | (3.1) 范畴等价；脚注 7：Z₂-gerbe、需 K_X^{1/2} |
| D-04 | D p.12 | 读 p12.txt | (4.1) (G_c,τ)↔(^L G_c,−1/(n_g τ))；n_g；"[MO] (0.1) 的扩展" |
| D-05 | D p.13 | 读 p13.txt | 三种 twist；第三 twist 引 [KW]；Q=uQ_ℓ+vQ_r；P¹ 族；t=v/u "twisting parameter" |
| D-06 | D p.14 | 读 p14.txt | (4.2) t↦(τ/\|τ\|)t；M4=Σ×X；"S-duality … becomes Mirror Symmetry"；§5 自 p.14 起 |
| D-07 | D p.15 | 读 p15.txt | A-模型靶 M_H(G)+ω_K vs B-模型靶 Y(^L G)+J；脚注 9 "quantum geometric Langlands correspondence" |
| D-08 | D p.16 | 读 p16.txt | (5.1) 两 Hitchin 纤维化同底 B；generic 纤维对偶环面；^LF_b 的点 = F_b 上平坦酉线丛 |
| D-09 | D p.17 | 读 p17.txt | fiberwise T-duality；"S-duality reduces to T-duality" [HMS]；SYZ；§5.2 "Categories of branes" 起 |
| D-10 | D p.18 | 读 p18.txt | (5.2) "we therefore expect … equivalence of (derived) categories of branes"；(5.3) 三角 |
| D-11 | D p.19 | 读 p19.txt | (5.4) A↦Hom(A_cc,A)；"this argument has not yet been made mathematically rigorous"；Nadler–Zaslow；函子与 S-对偶交换 |
| D-12 | D p.20 | 读 p20.txt | 0-膜 O_E↦A-膜 (F_b,∇_E)；Wilson 本征⇒'t Hooft 本征；"may in fact be made into a precise mathematical conjecture" |
| D-13 | D p.21 | 读 p21.txt | tame/wild；[FGa] 用 affine Kac–Moody critical level；Gukov–Witten surface operators (α,β,γ) |
| D-14 | D p.25 | 读 p25.txt | §6.1 内窥（Ngô、π₀(P_b)）；§6.2 "S-duality of more general boundary conditions"；连续自同构群 |
| D-15 | D p.26 | 读 p26.txt | 双 Hitchin 纤维化太 naive；C^n/C^× 吞 P^{n−1}；"master duality"；BPS Q·Ψ=0 → (6.3) Hitchin 方程 |
| D-16 | D p.27 | 读 p27.txt | σ 在边界有极点、Nahm 方程、sl₂⊂^L g；对应 Arthur SL₂ |

### 6.3 C（11 处）

| # | C locator | 读法 | 核到的原文锚点 |
|---|---|---|---|
| C-01 | C p.1 | 读 p01.txt | Y(G,C)=Hom(π₁(C),G_C)；Ω 来自 H¹(C,ad E) 相交配对；脚注 3：ImΩ 上同调平凡、ReΩ 不；abstract "few indications" |
| C-02 | C p.2 | 读 p02.txt | "Langlands or Goddard–Nuyts–Olive duality"；(2.1) Hitchin 方程；quantum GL 段引 "Kapustin & Witten (2007), sections 5.2 and 11.3" |
| C-03 | C p.3 | 读 p03.txt | Ω_I=ω_J+iω_K；J 下 M_H=Y、Ω=iΩ_J、ω=ImΩ=ω_K；J、Ω_J 不依赖 C 复结构 |
| C-04 | C p.4 | 读 p04.txt | "Mirror symmetry is believed to arise from T-duality on the fibers of a special Lagrangian fibration"；对偶纤维化 = ^L G 的纤维化；Hausel–Thaddeus 同底 |
| C-05 | C p.5 | 读 p05.txt | 镜像与 C 复结构无关 "This was shown in Kapustin & Witten (2007)"；§3.1 三 hints；Bogomolny 一句；Bun_G stack "strong clue" |
| C-06 | C p.6 | 读 p06.txt | (4.1) A=αdθ、(4.2) φ=βdr/r−γdθ；M_H(G,C;α,β,γ) 超凯勒；镜像 "not quite" |
| C-07 | C p.7 | 读 p07.txt | tame 对偶 M_H(^L G;^Lα,…)↔M_H(G;α,…)，(α,η)=(^Lη,−^Lα)；CFT 一句（"Frenkel & Gaitsgory (2005)"） |
| C-08 | C p.10 | 读 p10.txt | 4d 必要性：2-形式对偶为 (d−2)-形式，只有 d=4 仍是 2-形式 |
| C-09 | C p.11 | 读 p11.txt | 2d σ-模型在奇点处未良定义；"Any question that involves those singularities should be addressed in the underlying four-dimensional gauge theory" |
| C-10 | C p.12 | 读 p12.txt | §6.1 Stacks：D-模须住 Bun_G（Hecke 需不稳定丛）；Atiyah–Bott 的 Y=所有联络、W_C=Maps(C,G_C) |
| C-11 | C p.13 | 读 p13.txt | 规范群 Maps(Σ,W)=Maps(M,G)、M=Σ×C；Φ:Σ→Bun_G 的 σ-模型 = M 上 4d N=2 SYM |

> 抽核结论：**53 处全部命中**，无一处 locator 落空。其中 3 处修正了单元报告中的页码/式号：B (4.11) 在 p.46（非 p.44–45）、B (9.14)(9.15) 在 p.133（非 pp.140–142）、B (9.34) 在 p.148；另有 1 处核对为"否定命中"：D 正文无 "Bogomolny"、D 全文无 "Satake"（均为 grep 0 命中，已在第 9、14 行如实处理）。

---

## 7. 版本、作者、数据来源

- **版本**：v1（2026-11-17）
- **作者**：P2 + M9（T91 执行人，P2 与报告人职责合体）
- **数据来源**
  - B：工程 `WIT-0604151-EMDGL/source/text/p001.txt`–`p223.txt`（印刷页 N = 文件 p{N+1}.txt）
  - D：`work/tmp/D/p01.txt`–`p32.txt`（locator = D p.N）
  - C：`work/tmp/C/p01.txt`–`p15.txt`（locator = C p.N）
  - 八份定稿报告：`work/rounds/U01/report_v2.md` … `U07/report_v2.md`；**U08 引用 `work/rounds/U08/report_v1.md`**（核对时 report_v2 尚未产出，特此注明——U08 相关两行（⑪、⑳）的 B 侧 locator 已按源页重新抽核，未直接沿用 report_v1 页码）
  - 骨架与路线：`work/reads/00_skeleton_merged.md`（八节骨架）、`05_阅读路线.md`（八单元页段：U01 pp.2–15、U02 pp.16–37、U03 pp.38–55、U04 pp.56–77、U05 pp.78–122、U06 pp.123–147、U07 pp.148–183、U08 pp.184–222）
  - `work/SEED`：**本工作目录下不存在**（已核 `work/` 下仅 STATUS.md、roles.md），故未引用。
- **工具**：`read`（逐页文本）、`grep`（方程号定位）；抽核 53 处，见第 6 节。
