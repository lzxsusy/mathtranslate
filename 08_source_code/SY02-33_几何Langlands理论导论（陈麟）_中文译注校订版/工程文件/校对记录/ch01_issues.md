# ch01（导论）审读：问题清单

范围：`src/chapters/ch01.tex` 全 312 行（原 PDF p5–p11）。行号按当前文件；该文件在审读期间被另一进程插入 4 处 `transnote`（+21 行），若你手上的副本没有这些块，行号会小于此处。
逐句对照 `work/en/ch01_en.txt`，公式按 p005–p011 的整页 PNG 复核（θ_K、Thm 1.1.1、Cor 1.1.2、Def 1.1.3、Lemma 1.1.4、Thm 1.1.5、两张双栏表、Conj 1.3.1 的 L_G^{-1} 方向、Conj 1.4.1 的五行与 8 条 Hom 公式、Conj 1.5.1 的五行）。

结论：P1 0 条；P2 4 条（212、213、216、223 行：1 条误译、1 条断句、2 条术语）。未发现整句漏译/增译，未发现公式符号、上下标、箭头方向或定理编号错误。

## ch01.tex:212（原 PDF p9）
- 原文：Over C, its points are $G(K_v)$-valued points.
- 原译：在 $\mathbb C$ 上，它的点是 $G(K_v)$ 中的点。
- 类型：误译
- 改法：在 $\mathbb C$ 上，它的点是取值于 $G(K_v)$ 的点。
- 理由：原文是“取值为 $G(K_v)$ 的点”（即 $\mathrm{LG}(\mathbb C)=G(K_v)$），“$G(K_v)$ 中的点”把“取值”说成“属于”，丢掉了 -valued。

## ch01.tex:213（原 PDF p9）
- 原文：Define LG-Mod to be the (∞,2)-category of DG categories acted on by the monoidal DG category DMod(LG), with convolution monoidal structure.
- 原译：定义 $LG\text{-}\mathrm{Mod}$ 为被幺半 DG⟨空行⟩范畴 $\DMod(LG)$ 作用的 DG 范畴所构成的 $(\infty,2)$-范畴，其中幺半结构由卷积给出。
- 类型：逻辑
- 改法：删去第 213 行的空行，使“被幺半 DG”与下行的“范畴 $\DMod(LG)$ 作用的”连成同一段。
- 理由：空行让 LaTeX 在句子中途另起一段（第 212 行以“被幺半 DG”结尾，第 214 行以“范畴”开头），定义句被断成两段，是全章唯一一处（脚本扫描确认）。

## ch01.tex:216（原 PDF p9）
- 原文：the moduli ind-stack of $G$-torsors on $X$ of infinite level equipped with a trivialization on the formal neighborhood $D_v$ of $v$.
- 原译：具有无限层结构的 $X$ 上 $G$ 挠子模 ind-叠，后者配备在 $v$ 的形式邻域 $D_v$ 上的平凡化。
- 类型：术语
- 改法：具有无限级结构的 $X$ 上 $G$ 挠子模 ind-叠，后者配备在 $v$ 的形式邻域 $D_v$ 上的平凡化。
- 理由：level 应作“级”（level structure 即“级结构”），译作“层”与本书 sheaf 的“层”同字撞车；同一页第 223 行又把 critical level 译作“临界水平”，同一个 level 出现两种译法。

## ch01.tex:223（原 PDF p9）
- 原文：obtained by taking right $LN$-invariants against a generic character $\chi$, where $N$ is the unipotent radical of a Borel subgroup $B$.
- 原译：它通过相对于一般位置特征标 $\chi$ 取右 $LN$ 不变量而得到，其中 $N$ 是 Borel 子群 $B$ 的幺幂根基。
- 类型：术语
- 改法：它通过相对于一般特征标 $\chi$ 取右 $LN$ 不变量而得到，其中 $N$ 是 Borel 子群 $B$ 的幺幂根基。
- 理由：generic character 在表示论中的固定译法是“一般特征标”（非退化特征标），“一般位置”是几何用语（general position），照字面译会让读者以为说的是“处于一般位置的特征标”。
