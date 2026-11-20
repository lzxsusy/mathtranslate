---
id: MS-08
zh: 扇与多胞形
en: fan and polytope
aliases: [扇, 多胞形, 法扇, 极多胞形, fan, polytope, normal fan, polar polytope]
layer: L0
prereqs: []
sources:
  - "A 级：Cox–Katz 1999, p.54–59（PDF p.54–59，印刷 p.31–36）§3.1、§3.2.1–3.2.2；p.69–70（印刷 p.46–47）§3.5 定义 3.5.3–命题 3.5.5；p.72–74 例 3.7.1–3.7.3"
  - "A 级：Batyrev 1994, J. Alg. Geom. 3 (1994) 493–535（书内 [Batyrev4]）§1–2（定理号待核，见 §11）"
  - "B 级：Fulton, Introduction to Toric Varieties, Princeton Univ. Press 1993, §1.4、§3.4、§5.3（页码待核）"
  - "B 级：nLab 条目 polytope、fan、toric variety（索引页）"
status: draft
review:
  drafter: agent-219
  reviewer: lead
  blindtest: pending
glossary_refs: ["SY01-24 术语表 扇 fan（p.65）", "SY01-24 术语表 多胞体 polytope（p.73）", "SY01-24 术语表 法扇 normal fan（p.76）", "SY01-24 术语表 尖锥 pointed cone（p.61）", "SY01-24 术语表 反身多胞体（p.81）", "SY01-25 04-术语卡 §9.2 扇区 sector"]
symbols_refs: ["$M$", "$N=\\operatorname{Hom}(M,\\mathbb Z)$", "$N_{\\mathbb R}$", "$\\Sigma$", "$\\Sigma(1)$", "$\\Delta$", "$\\Delta^\\circ$", "$v_\\rho$", "$D_\\rho$", "$l(k\\Delta)$", "$l^*(k\\Delta)$"]
updated: 2026-11-20
---

# MS-08 扇与多胞形

## 1. 一句话

用多胞形的面在对偶空间搭出扇，把多胞形翻译成环面簇。

## 2. 为什么需要它

- **给多胞形环一个几何意义。** §3.2.2 用 $S_\Delta$ 定义 $\mathbb P_\Delta=\operatorname{Proj}(S_\Delta)$（p.57），但只有把 $\Delta$ 的面做成法扇 $\Sigma_\Delta$，才能认出 $\mathbb P_\Delta=X(\Sigma_\Delta)$ 是环面簇（引理 3.2.1，p.57–58）。否则 $S_\Delta$ 只是一个分次环，谈不上轨道、除子与奇点。
- **镜像对称的第一层字典。** §3.5 的 Batyrev 自反多胞形（p.69–70）与第 4 章的镜像族构造（p.76 起）都以「$\Delta$ 与 $\Delta^\circ$ 的极对偶对 ⟹ 环面簇对」为骨架；没有扇与极多胞形，$\Delta$ 只是格点凸包，说不出它的镜像伙伴是谁，也说不出 $X^\circ$ 为何是 Fano。
- **把格点计数变成上同调维数。** 式 (3.6) 的 $l(k\Delta)$、$l^*(k\Delta)$（p.59）在镜像对称多处出现；式 (3.7) 又把它们等同于 $H^0(\mathbb P,\mathcal O_\mathbb P(kD_\Delta))$，这是第 4 章 Picard–Fuchs 与 Hodge 数反射的计算入口。没有「除子—多胞形—扇」三角对应，这些数只是组合量。

## 3. 定义（全假设）

**3.1 格与对偶空间（p.54）。** 固定自由 Abel 群 $M\simeq\mathbb Z^n$，令 $N=\operatorname{Hom}(M,\mathbb Z)\simeq\mathbb Z^n$、$N_\mathbb R=N\otimes_\mathbb Z\mathbb R$、$M_\mathbb R=M\otimes_\mathbb Z\mathbb R$，配对 $\langle\cdot,\cdot\rangle:M\times N\to\mathbb Z$ 双线性延拓到 $\mathbb R$。以下所有锥都在 $N_\mathbb R$，所有多胞形都在 $M_\mathbb R$——两个空间互为对偶，**不可混同**。

**3.2 有理多面锥与强凸（p.54）。** 给定 $u_1,\dots,u_s\in N$，$\sigma=\{\sum\lambda_iu_i:\lambda_i\ge0\}$ 称有理多面锥。若 $\sigma\cap(-\sigma)=\{0\}$ 称**强凸**（= pointed）。$\dim\sigma$ 为 $\sigma$ 张成的子空间维数，对偶锥 $\check\sigma=\{m\in M_\mathbb R:\langle m,v\rangle\ge0\ \forall v\in\sigma\}$。

**3.3 面（p.54–55）。** 对 $u\in M_\mathbb R$，使 $\langle u,\cdot\rangle$ 在 $\sigma$ 上取最小值的子集 $\tau=\{v\in\sigma:\langle u,v\rangle=\min_{\sigma}\langle u,\cdot\rangle\}$ 称 $\sigma$ 的面（书中等价写法：$\tau=\{v\in\sigma:\langle m,v\rangle=0\}$，$m\in M\cap\check\sigma$）。面仍是有理多面锥，面的面是面。余维数为 1 的面称**刻面**。

**3.4 扇（p.55，全书的中心定义）。** $N_\mathbb R$ 中的**扇** $\Sigma$ 是有限个强凸有理多面锥组成的非空集合，满足：(i) $\sigma\in\Sigma$ ⟹ $\sigma$ 的所有面属于 $\Sigma$；(ii) $\sigma,\tau\in\Sigma$ ⟹ $\sigma\cap\tau$ 是两者各自的面（允许 $\{0\}$）。支集 $|\Sigma|=\bigcup_{\sigma\in\Sigma}\sigma$；$\Sigma(d)=\{d\text{ 维锥}\}$；$\Sigma(1)$ 的元素称**射线** $\rho$，$v_\rho$ 为半群 $\rho\cap N$ 的唯一格生成元，于是 $\sigma=\sum_{\rho\subset\sigma}\mathbb R_{\ge0}v_\rho$。$|\Sigma|=N_\mathbb R$ 时称**完备**。

**3.5 多胞形（p.56）。** 有限点集 $m_1,\dots,m_s\in M_\mathbb R$ 的凸包称**多胞形** $\Delta=\operatorname{Conv}(m_1,\dots,m_s)$；顶点全在 $M$ 中时称**整多胞形**；$\dim\Delta$ 为差 $m_i-m_j$ 张成的维数。$\Delta$ 的面 = 某个线性函数在 $\Delta$ 上取最小值的子集，余维 1 的面称**刻面**。本卡后文默认 $\dim\Delta=n$、$0\in\operatorname{Int}\Delta$（极对偶所需）。

**3.6 法扇（p.57）。** 设 $F\subsetneq\Delta$ 为非空面。令 $\check\sigma_F=\{\lambda(m-m'):m\in\Delta,\ m'\in F,\ \lambda\ge0\}\subset M_\mathbb R$，其对偶 $\sigma_F=\check\sigma_F^{\vee}\subset N_\mathbb R$。则 $\Sigma_\Delta=\{\sigma_F:F\text{ 为 }\Delta\text{ 的非空面}\}$ 是 $N_\mathbb R$ 中的**完备扇**，称 $\Delta$ 的**法扇**。

**3.7 极多胞形（p.57）。** $\Delta^\circ=\{v\in N_\mathbb R:\langle m,v\rangle\ge-1,\ \forall m\in\Delta\}$。**若 $0\in\operatorname{Int}\Delta$ 且 $\dim\Delta=n$**，则 $\Delta^\circ$ 是有界多胞形、$0\in\operatorname{Int}\Delta^\circ$、$(\Delta^\circ)^\circ=\Delta$，且面维数反转：$\Delta$ 的 $i$ 维面 $F$ ↔ $\Delta^\circ$ 的 $(n-1-i)$ 维面 $F^\circ$，特征为 $m'\in F,\ v\in F^\circ$ ⟹ $\langle m',v\rangle=-1$。

**3.8 本书用法。** Cox–Katz 在 p.54–57 用的是标准定义：多胞形只指有界凸包，无界情形在 §3.2 不出现；「强凸」即他书所称 pointed cone，与 SY01-24 的「尖锥」同义（§8 冲突 C3），中译本未设「多面体」术语，故不区分「多面体 / 多胞形」（§8 冲突 C1）。另注意本书的「扇」与 SY01-25 的「扇区（sector）」同字不同义（§8 冲突 C6）。

## 4. 最小例子（能算出）

**4.1 $\mathbb P^2$ 的反典范多胞形与它的法扇（书内例 3.7.1，p.72）。**

1. **格。** $N=M=\mathbb Z^2$，$\langle m,v\rangle=m_1v_1+m_2v_2$。
2. **扇。** 取三条射线 $v_1=(1,0)$、$v_2=(0,1)$、$v_0=(-1,-1)$，$\Sigma$ 含 $0$、三条射线与三个二维锥 $\operatorname{cone}(v_0,v_1)$ 等。$|\Sigma|=\mathbb R^2$ 且每个二维锥的生成元可补成 $\mathbb Z^2$ 的基，故 $\Sigma$ 完备、光滑，$X(\Sigma)=\mathbb P^2$。
3. **设 $D=-K_{\mathbb P^2}=D_{v_1}+D_{v_2}+D_{v_0}$**（式 (3.3) 中 $a_\rho=1$）。由 $\Delta_D=\{m:\langle m,v_\rho\rangle\ge-a_\rho\}$ 得三个半空间：$m_1\ge-1$（$v_1$）、$m_2\ge-1$（$v_2$）、$-m_1-m_2\ge-1$ 即 $m_1+m_2\le1$（$v_0$）。
4. **顶点。** 三式两两取等：$(m_1,m_2)=(-1,-1)$、$(2,-1)$、$(-1,2)$。故 $\Delta=\operatorname{Conv}\{(-1,-1),(2,-1),(-1,2)\}$，三张刻面对应三条射线（与 p.56「丰沛时刻面 ↔ $\Sigma(1)$」一致）。
5. **数格点。** 面积 $=\frac12|\det((3,0),(0,3))|=\frac92$；边界格点数 $B=3+3+3=9$；Pick 公式给内点 $I=\frac92-\frac92+1=1$（正是原点）。故 $l(\Delta)=I+B=10$、$l^*(\Delta)=I=1$。又 $2\Delta$：令 $a=m_1+2,\ b=m_2+2$，则 $a,b\ge0$、$a+b\le6$，故 $l(2\Delta)=\binom82=28$；而 $\operatorname{Int}(2\Delta)\cap M=\Delta\cap M$ 在此成立的原因是 $\Delta$ 自反（各刻面到原点的格高恰为 1：$\operatorname{Int}(k\Delta)\cap M=(k-1)\Delta\cap M$ 只对这类多胞形成立，一般整多胞形如 $\operatorname{Conv}\{(-1,0),(0,-1),(2,2)\}$ 不成立），故 $l^*(2\Delta)=10$。
6. **极多胞形。** $\Delta$ 的三张刻面由上述不等式取等给出，其对偶的顶点就是三个法向量：$\Delta^\circ=\operatorname{Conv}\{(1,0),(0,1),(-1,-1)\}$（如刻面 $F_1=\{m_1=-1\}$ 对应的顶点为 $(1,0)=F_1^\circ$）。它是标准单形，$l(\Delta^\circ)=4$、$l^*(\Delta^\circ)=1$；逐条代入得 $(\Delta^\circ)^\circ=\Delta$。
7. **法扇就是第 2 步的扇。** 引理 3.2.1：$\sigma_{F_1}=\mathbb R_{\ge0}(1,0)$、$\sigma_{F_2}=\mathbb R_{\ge0}(0,1)$、$\sigma_{F_0}=\mathbb R_{\ge0}(-1,-1)$，二维锥由相邻刻面给出。故 $\mathbb P_\Delta=X(\Sigma_\Delta)=\mathbb P^2$。
8. **自反性校验（定义 3.5.3，p.69）。** 三张刻面分别落在 $\langle m,(1,0)\rangle=-1$、$\langle m,(0,1)\rangle=-1$、$\langle m,(-1,-1)\rangle=-1$ 上且 $v_\Gamma\in N$；(ii) $\operatorname{Int}(\Delta)\cap M=\{(0,0)\}$。故 $\Delta$ 自反，$\Delta^\circ$ 也自反（引理 3.5.4），$\mathbb P_\Delta=\mathbb P^2$ 是 Fano（命题 3.5.5）。

**4.2 书中升级版：立方体与八面体（例 3.7.3，p.74）。** $\Delta=[-1,1]^3\subset M_\mathbb R=\mathbb R^3$：$l(\Delta)=3^3=27$、$l^*(\Delta)=1$（只有原点）；$\Delta^\circ=\operatorname{Conv}\{\pm e_1,\pm e_2,\pm e_3\}$（八面体）：$l(\Delta^\circ)=7$、$l^*(\Delta^\circ)=1$。$\Delta$ 的法扇是 $N_\mathbb R$ 的 8 个卦限，$\mathbb P_\Delta=\mathbb P^1\times\mathbb P^1\times\mathbb P^1$、$\mathcal O(1)=-K_X$；$\operatorname{vol}(\Delta)=8$，由 $(-K)^n=n!\operatorname{vol}(\Delta)$（p.76，引 [Fulton3] §5.3）得 $(-K_X)^3=48$；对偶侧 $\operatorname{vol}(\Delta^\circ)=\frac43$，故 $(-K_{X^\circ})^3=6\cdot\frac43=8$。两个数差 6 倍，正说明「自反对」不是对称对象。

## 5. 关键性质（3–6 条，带出处）

| # | 性质 | 出处（书页/文献） | 备注 |
|---|---|---|---|
| 1 | 法扇 = 由 $\Delta^\circ$ 各真面上的锥组成的扇；故 $\mathbb P_\Delta=X(\Sigma_\Delta)$ | p.57–58，引理 3.2.1（引 [Batyrev4]）| 多胞形→环面簇的桥，证明只用 $0\in\operatorname{Int}\Delta$ |
| 2 | $\Delta$ 的非空面 ↔ $\Sigma_\Delta$ 的锥（含反序），刻面 ↔ 射线；等价地 $T_N$-轨道闭包 ↔ $\Delta^\circ$ 的真面 | p.57–58；p.56 丰沛情形 | $\Delta$ 的组合结构即 $X(\Sigma_\Delta)$ 的轨道分层 |
| 3 | $D$ 由整体截面生成 ⟺ $\Delta_D=\operatorname{Conv}\{m_\sigma:\sigma\in\Sigma(n)\}$；$D$ 丰沛 ⟺ 这些 $m_\sigma$ 两两不同且为顶点；两情形 $\Delta_D$ 皆整 | p.56 式 (3.3) 之后（引 [Danilov][Fulton3][Oda]）| 反向即「由 $\Delta$ 造法扇」 |
| 4 | $H^0(X,\mathcal O(D))\simeq\bigoplus_{m\in\Delta_D\cap M}\mathbb C\chi^m$；更一般 $(S_\Delta)_k\simeq L(k\Delta)\simeq H^0(\mathbb P,\mathcal O_\mathbb P(kD_\Delta))$ | 式 (3.4) p.57；式 (3.7) p.59 | 故 $l(k\Delta)$ 是上同调维数 |
| 5 | 面维数反转 $\dim F^\circ=n-1-\dim F$、$(\Delta^\circ)^\circ=\Delta$；$\phi_\Delta(v)=\min_{m\in\Delta}\langle m,v\rangle$ 严格上凸 ⟹ $D_\Delta$ 丰沛、$\Delta_{D_\Delta}=\Delta$ | p.57–58（引 [Batyrev4][Oda]）| 缺 $0\in\operatorname{Int}\Delta$ 时 $(\Delta^\circ)^\circ=\Delta$ 失效（§7 第 2 条）|
| 6 | $\Delta$ 自反 ⟺ $\Delta^\circ$ 自反 ⟺ $\mathbb P_\Delta$ Fano 且 $\Delta$ 是反典范除子多胞形 | 引理 3.5.4、命题 3.5.5，p.69–70 | 自反 = 两张多胞形都整的「恰好」条件（§7 第 4 条）|

## 6. 推导流程（D1…Dn）

- **D1（输入）**：$n$ 维整多胞形 $\Delta\subset M_\mathbb R$，$0\in\operatorname{Int}\Delta$，$M\simeq\mathbb Z^n$。依据：p.56。
- **D2（造锥）**：对每个非空面 $F$ 取 $\check\sigma_F=\mathbb R_{\ge0}(\Delta-F)$ 的对偶 $\sigma_F\subset N_\mathbb R$。依据：p.57（:139–146）。
- **D3（验证扇公理）**：$\sigma_F$ 是强凸有理多面锥；$F'\subset F$ ⟹ $\sigma_{F'}\supset\sigma_F$ 且为其面；$\sigma_F\cap\sigma_{F'}=\sigma_{F\cap F'}$（$F\cap F'=\varnothing$ 时取 $\{0\}$）。依据：p.57 引 [Batyrev4]；标准多面体论（B 级 [Fulton3] §1.4 待核）。
- **D4（引理 3.2.1 的识别）**：证 $\sigma_F=\mathbb R_{\ge0}F^\circ$。要点：$v\in\sigma_F$ ⟺ $\forall m\in\Delta,m'\in F$ 有 $\langle m,v\rangle\ge\langle m',v\rangle$；$v\ne0$ 时 $\langle m',v\rangle<0$（否则 $-v$ 与 $0\in\operatorname{Int}\Delta$ 矛盾）；取 $m'$ 在 $F$ 的相对内部并归一化 $v=\lambda v'$，得 $\langle m,v'\rangle\ge-1$，即 $v'\in\Delta^\circ\cap F^\circ$。依据：p.57（:159–165）。
- **D5（得环面簇）**：$\mathbb P_\Delta=\operatorname{Proj}(S_\Delta)$ 与 $X(\Sigma_\Delta)$ 一致：$\Sigma_\Delta$ 完备（p.57），且面 $F$ 给出环满射 $\pi_F:S_\Delta\to S_F$、闭浸入 $\mathbb P_F\hookrightarrow\mathbb P_\Delta$（p.58）。依据：p.57–58（引 [Batyrev4]）。
- **D6（接除子与截面）**：$\phi_\Delta(v)=\min_{m\in\Delta}\langle m,v\rangle$ 是 $D_\Delta$ 的严格上凸支撑函数，$\Delta_{D_\Delta}=\Delta$、$\mathcal O(D_\Delta)\simeq\mathcal O(1)$；式 (3.4) 给整体截面。依据：p.58、式 (3.4) p.57。
- **D7（加自反条件）**：要求每张刻面在 $\langle m,v_\Gamma\rangle=-1$ 上、$v_\Gamma\in N$，且 $\operatorname{Int}\Delta\cap M=\{0\}$；此时 $\Delta^\circ$ 也整、$D_\Delta=-K$ 丰沛，得到第 4 章 Batyrev 镜像族的输入。依据：定义 3.5.3、引理 3.5.4、命题 3.5.5（p.69–70）。

## 7. 常见误解与反例（≥2）

1. **误解：扇的锥与多胞形的面在同一个空间里，法扇就是「把多胞形的面锥摆出来」。** 错：$\Delta\subset M_\mathbb R$、$\Sigma_\Delta\subset N_\mathbb R$，中间隔一次对偶（p.54、p.57）。1 维反例：$\Delta=[-1,1]\subset M_\mathbb R=\mathbb R$ 时 $\Delta^\circ=[-1,1]\subset N_\mathbb R$，法扇为 $\{\{0\},\mathbb R_{\ge0},\mathbb R_{\le0}\}$，$X(\Sigma)=\mathbb P^1$；把扇画进 $M_\mathbb R$ 会得到不对偶的图形。
2. **误解：任何整多胞形 $\Delta$ 的极多胞形 $\Delta^\circ$ 都是有界多胞形。** 错：3.7 的定义需要 $0\in\operatorname{Int}\Delta$（p.57）；无界时它只是 $N_\mathbb R$ 中的多面体。反例：$\mathbb P^2$ 上丰沛除子 $D_0$ 的多胞形 $\Delta_{D_0}=\operatorname{Conv}\{(0,0),(1,0),(0,1)\}$（例 3.7.1），$0$ 是顶点，$\Delta_{D_0}^\circ=\{v:v_1\ge-1,\ v_2\ge-1\}$ 无界，且 $(\cdot)^\circ$ 对不回来。
3. **误解：$\Delta$ 与 $\Delta^\circ$ 对称，格点数、体积应当相近。** 错：极对偶只保证面维数反转与 $(\Delta^\circ)^\circ=\Delta$。例 3.7.3（p.74）：立方体 $l=27$、八面体 $l=7$，体积 $8$ 对 $\frac43$；同页还强调 $X^\circ$ 的锥连单纯都不是。
4. **误解：$\Delta$ 整 ⟹ $\Delta^\circ$ 整。** 错：p.58 明说「极多胞形未必是整的」。反例：$\Delta=2\Delta_0=\operatorname{Conv}\{(-2,-2),(4,-2),(-2,4)\}$（整、$0$ 在内点），三张刻面到原点的格距离都是 2，故 $\Delta^\circ=\frac12\operatorname{Conv}\{(1,0),(0,1),(-1,-1)\}$，顶点 $(\frac12,0),(0,\frac12),(-\frac12,-\frac12)\notin N$。距离全为 1 正是定义 3.5.3 的 (i)。

## 8. 在文献中的坐标

| 文献 | 位置 | 它在那里干什么 |
|---|---|---|
| Cox–Katz 1999（中译本）| p.54–56（印刷 p.31–33）§3.1 | 格/锥/强凸/面/扇/支集/完备/射线 $v_\rho$、式 (3.1) $\operatorname{div}\chi^m=\sum_\rho\langle m,v_\rho\rangle D_\rho$、丰沛的上凸判据 |
| Cox–Katz 1999 | p.56–59（印刷 p.33–36）§3.2.1–3.2.2 | 多胞形/整/刻面、式 (3.3) $\Delta_D$、式 (3.4) 截面、法扇、极多胞形、引理 3.2.1、式 (3.5)–(3.7) 与 $l,l^*$ |
| Cox–Katz 1999 | p.69–70（印刷 p.46–47）§3.5 | 定义 3.5.3 自反、引理 3.5.4（自反对偶）、命题 3.5.5（自反 ⟺ Fano）、引理 3.5.6 |
| Cox–Katz 1999 | p.72–74 例 3.7.1–3.7.3 | 本卡 §4 两算例的来源；例 3.7.3 明写 $X$ 光滑而 $X^\circ$ 奇点严重 |
| SY01-24（Siebert 讲义中译本）| 第 4 章 定义 4.7、例 4.10（p.65–66）；定义 4.12–4.14、命题 4.12（p.73–76）| 扇与法扇的平行定义。**冲突：** 本书 p.54「强凸」= SY01-24 p.61「尖锥」（同 pointed cone）（C3）。**冲突：** SY01-24 用「多胞体」且限定有界（p.73），本书用「多胞形」（C1，_冲突表 T5 已裁：多胞形）。**冲突：** SY01-24 称余维 1 面为「侧面」（p.73），本书称「刻面」（p.56）（C4）。**冲突：** SY01-24 定义 4.14 取 $\Xi^\circ=\{\langle u,v\rangle\le1\}$、命题 4.12 法扇取 $-\sigma_{\Xi'}$，本书取 $\langle m,v\rangle\ge-1$、$\sigma_F$ 不加负号，二者整体差 $v\mapsto-v$（C5；SY01-24 注 4.11 自称这是约定选择）|
| SY01-24 | 第 5 章 定义 5.1（p.81）| 「反身多胞体」= 本书定义 3.5.3「自反多胞形」，两条件逐条相同。**冲突：** 译名「反身多胞体」vs 本书「自反多胞形」（C2，_冲突表 T6 已裁：自反多胞形）|
| SY01-25 资料卡 | 04-术语文献勘误.md §9.2（扇区 sector）| 无 fan/polytope 条目（缺口）；唯一接口是「扇区」——**冲突：** SY01-25 的扇区指按同伦类/边界分层分解茎的子集，与本书 §3.1 的扇无关，只共享一个汉字（C6，同形字）|
| Batyrev 1994（书内 [Batyrev4]）| J. Alg. Geom. 3 (1994) 493–535，§1–2（定理号待核）| 多胞形环、法扇、极对偶，以及用自反多胞形构造 CY 超曲面的镜像对；本书 p.57 引它证 $\mathbb P_\Delta=X(\Sigma_\Delta)$ |
| Fulton 1993（B 级）| Introduction to Toric Varieties, §1.4、§3.4、§5.3（页码待核）| 扇—多胞形—除子字典的标准教材版；本书式 (3.4) 与 $(-K)^n=n!\operatorname{vol}$ 都引它 |

注：书内页码一律为 PDF 物理页（=$\backslash$SourcePage$\{N\}$，印刷页 $+23$）；外部文献用原书页码。

## 9. 前置与后继

- 前置：无（L0 起点）。可选背景：MS-07 环面簇（$X_\sigma=\operatorname{Spec}\mathbb C[M\cap\check\sigma]$ 的粘合与轨道—锥对应，p.54–55）——本卡只用到「扇 ⟹ 环面簇」这一结论。
- 后继：MS-07（环面簇，以本卡的扇为输入）；MS-09（自反多胞形，由 §3.7 与 §5 第 6 条直接升级）；MS-23（nef 分拆与 Batyrev 构造，第 4 章 p.76 起）；MS-03（五次三维簇，作为 $\Delta$ 与 $\mathbb P_\Delta$ 的实例）；MS-06（Picard–Fuchs，式 (3.6)/(3.7) 的 $l(k\Delta)$ 进入周期计算）。
- 术语协调：本卡一律用「扇、多胞形、自反多胞形、刻面、强凸」，与 _冲突表 T5/T6 的裁定一致；「极多胞形」沿用本书字号。

## 10. 形式化接口（Lean 可 sorry）

```lean
import Mathlib.Data.Real.Basic
import Mathlib.Data.Set.Basic
import Mathlib.Data.Finset.Basic

/-- 格对 $(M,N)$：$M\simeq\mathbb Z^n$，$N=\operatorname{Hom}(M,\mathbb Z)$，$\langle m,v\rangle\in\mathbb Z$ 及其 $\mathbb R$-延拓（Cox–Katz p.54）。 -/
structure LatticePair where
  n : ℕ
  pairing : (Fin n → ℤ) → (Fin n → ℤ) → ℤ
  pairingR : (Fin n → ℤ) → (Fin n → ℝ) → ℝ

/-- 有理多面锥：由格点 $\mathbb R_{\ge0}$-组合生成；强凸（pointed）即 $\sigma\cap(-\sigma)=\{0\}$（p.54）。 -/
structure Cone (P : LatticePair) where
  carrier : Set (Fin P.n → ℝ)
  gens : Finset (Fin P.n → ℤ)
  is_strongly_convex : ∀ v, v ∈ carrier → -v ∈ carrier → v = 0

/-- 面关系（p.54）：$\tau$ 是 $\sigma$ 的面。 -/
def IsFace (P : LatticePair) (τ σ : Cone P) : Prop := by sorry

/-- 扇（p.55）：有限强凸有理多面锥的非空集，闭于取面，交为公共面。 -/
structure Fan (P : LatticePair) where
  cones : Finset (Cone P)
  nonempty : cones.Nonempty
  face_closed : ∀ σ ∈ cones, ∀ τ : Cone P, IsFace P τ σ → τ ∈ cones
  pairwise_face : ∀ σ ∈ cones, ∀ τ ∈ cones,
    ∃ F : Cone P, IsFace P F σ ∧ IsFace P F τ

/-- 多胞形 = 有限点集的凸包（p.56）；本书只讨论满维情形。 -/
structure Polytope (P : LatticePair) where
  pts : Finset (Fin P.n → ℤ)
  nonempty : pts.Nonempty
  full_dim : True

/-- 内点集（占位；正文 p.56 用 $\operatorname{Int}\Delta$）。 -/
def interiorOf (P : LatticePair) (Δ : Polytope P) : Set (Fin P.n → ℝ) := by sorry

/-- 极多胞形（p.57）：$\Delta^\circ=\{v:\langle m,v\rangle\ge-1,\ \forall m\in\Delta\}$。 -/
def polar (P : LatticePair) (Δ : Polytope P) : Set (Fin P.n → ℝ) :=
  {v | ∀ m ∈ Δ.pts, P.pairingR m v ≥ -1}

/-- 引理 3.2.1（p.57）：$\Delta^\circ$ 各真面上的锥组成的扇 = $\Delta$ 的法扇，
    需 $0\in\operatorname{Int}\Delta$；有界性与内点性留作假设。 -/
theorem normalFan_eq_polar_face_fan (P : LatticePair) (Δ : Polytope P)
    (h0 : (0 : Fin P.n → ℝ) ∈ interiorOf P Δ) : True := by sorry

/-- 自反（定义 3.5.3，p.69）：刻面在 $\langle m,v_\Gamma\rangle=-1$ 上且 $\operatorname{Int}\Delta\cap M=\{0\}$。 -/
def IsReflexive (P : LatticePair) (Δ : Polytope P) : Prop := by sorry

/-- 「$\Delta$ 给出 Fano 环面簇且是反典范多胞形」（命题 3.5.5，p.69）。 -/
def IsFanoPolar (P : LatticePair) (Δ : Polytope P) : Prop := by sorry

theorem reflexive_iff_fano (P : LatticePair) (Δ : Polytope P) :
    IsReflexive P Δ ↔ IsFanoPolar P Δ := by sorry
```

## 11. 待核清单

- [ ] **冲突 C1（§8 第 5 行）**：SY01-24 术语表与定义 4.13（p.73）把 polytope 译作「多胞体」并强调有界，本书 §3.2.1（p.56）译作「多胞形」。_冲突表 T5 已裁「多胞形」，正文沿用；此处仅登记（涉及 MS-09）。
- [ ] **冲突 C2（§8 第 6 行）**：SY01-24 第 5 章定义 5.1（p.81）「反身多胞体」vs 本书定义 3.5.3（p.69）「自反多胞形」，条件相同、译名不同；_冲突表 T6 已裁「自反多胞形」（涉及 MS-09）。
- [ ] **冲突 C3（§8 第 5 行）**：本书 p.54「强凸」vs SY01-24 p.61「尖锥」（同 pointed cone）。待裁，建议编号 T7；涉及 MS-07、MS-09。
- [ ] **冲突 C4（§8 第 5 行）**：本书 p.56「刻面」vs SY01-24 p.73「侧面」（同 codimension-1 face）。待裁，建议编号 T8；涉及 MS-09。
- [ ] **冲突 C5（§8 第 5 行）**：极多胞形的约定与命名——本书 $\Delta^\circ=\{\langle m,v\rangle\ge-1\}$、法扇取 $\sigma_F$；SY01-24 定义 4.14 取 $\Xi^\circ=\{\langle u,v\rangle\le1\}$、命题 4.12 取 $-\sigma_{\Xi'}$，整体差 $v\mapsto-v$（其注 4.11 自陈）。术语上本书「极多胞形」vs SY01-24「对偶（极）多面体」。待裁，建议编号 T9；涉及 MS-09。
- [ ] **冲突 C6（§8 第 7 行）**：SY01-25 04-术语卡 §9.2「扇区 sector」与本书「扇 fan」同形字不同义，勿混；是否入 _冲突表 待定，建议编号 T10。
- [ ] Batyrev 1994 定理号待核：本书 p.57 引 [Batyrev4] 证 $\mathbb P_\Delta=X(\Sigma_\Delta)$，本卡按书内转述陈述，未核原文编号（A 级降为「待核」）。
- [ ] 式 (3.6) 的 $l^*(k\Delta)$ 措辞待核：书中「不在 $k\Delta$ 的任何刻面上」应理解为 $\operatorname{Int}(k\Delta)\cap M$（OCR 断句可能致歧义）；§4 按内点计。
- [ ] p.58「极多胞形未必是整的」书中未给例；§7 第 4 条的 $2\Delta_0$ 例子为本卡自算，[Fulton3] §3.4 页码待补（B 级）。
- [ ] 「多面体」术语缺口（不算冲突）：本书在 $0\notin\operatorname{Int}\Delta$ 时出现无界对象却未命名，SY01-24 定义 4.12 明确区分多面体/多胞体；本卡 §3.8 只描述、不引入新译名。
- [ ] §4.2 的 $(-K_{X^\circ})^3=8$ 为自算（$\operatorname{vol}(\Delta^\circ)=\frac43$，公式见 p.76 引 [Fulton3] §5.3）；书 p.74 只作定性对比，数值待复核。
- [ ] §10 形式化只到签名层（多处 `by sorry`；`interiorOf`/`IsReflexive`/`IsFanoPolar` 为占位定义）；Mathlib 有无 toric variety / fan 的现成 API 待核。
- **核验（2026-11-20）**：本卡经 `_核验记录.md` 核验，修正 1 处（详见该文件 ✗ 清单与证据链接）；其余待核条目保留。
