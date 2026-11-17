---
id: glc/concept/top-hecke-relation
type: concept
track: E
---

# 延拓到 $\operatorname{Bun}_n$ 与最高次 Hecke 关系

> $\operatorname{Aut}_E$ 中间延拓到各次数分支，用最高次关系（$M\mapsto M(-x)$ 降 $n$ 次）拼得 $\operatorname{Aut}_E\in D(\operatorname{Bun}_n)$。

**问题**：为什么最高次 Hecke 关系能给出次数分支之间的**唯一**延拓，而第一 Hecke 关系又能从良好开子叠传播到整个延拓层？

## 定义

令 $j_d:C_n\cap\operatorname{Bun}_n^d\hookrightarrow\operatorname{Bun}_n^d$ 为次数 $d$ 分支中的良好开子叠。构造首先通过中间延拓扩展下降层：$\operatorname{Aut}_E^d:=j_{d,!*}(\operatorname{Aut}_E|_{C_n\cap\operatorname{Bun}_n^d})$；在洁净范围内，它与 $j_{d,!}$ 和 $j_{d,*}$ 给出同一对象。然后，最高次 Hecke 关系给出次数分支之间的唯一延拓，因为 $M\mapsto M(-x)$ 使次数减少 $n$。$\operatorname{Hecke}_n^1$ 与最高次 Hecke 对应之间的相容性，将第一 Hecke 关系从良好开子叠传播到延拓层。于是得到以 $E$ 为特征值的 Hecke 特征层 $\operatorname{Aut}_E\in D(\operatorname{Bun}_n)$。特别地，采用第 2 章的 Hecke 对应约定，$(t_x^{d+n})^*\operatorname{Aut}_E^d\simeq\det(E_x)\otimes\operatorname{Aut}_E^{d+n}$，其中 $t_x^{d+n}:\operatorname{Bun}_n^{d+n}\to\operatorname{Bun}_n^d$ 为同构、$M\mapsto M(-x)$；等价地，对 $\tau_x^d:\operatorname{Bun}_n^d\to\operatorname{Bun}_n^{d+n}$、$M\mapsto M(x)$，有 $(\tau_x^d)^*\operatorname{Aut}_E^{d+n}\simeq\det(E_x)^{-1}\otimes\operatorname{Aut}_E^d$。

*记号*：$j_{d,!*}$ 是中间延拓；$\operatorname{Bun}_n^d$ 是次数 $d$ 分支；$t_x^{d+n}$ 与 $\tau_x^d$ 是互逆的次数平移同构（$M\mapsto M(-x)$ 与 $M\mapsto M(x)$）；$\det(E_x)$ 是 $E$ 在 $x$ 处的纤维的行列式（一维），故为扭转因子。

## 要点

- 两步走：先在每个次数分支内作中间延拓 $j_{d,!*}$，再在分支之间用最高次 Hecke 关系拼接；顺序不能反。
- 洁净范围内 $j_{!*}=j_!=j_*$，所以中间延拓在良好开子叠附近不损失信息。
- 跨分支的唯一性来自 $M\mapsto M(-x)$ 把次数降 $n$：最高次关系把相邻（差 $n$）分支的关系钉死，故延拓唯一。
- 第一 Hecke 关系靠『$\operatorname{Hecke}_n^1$ 与最高次 Hecke 对应相容』从良好开子叠传播；这条相容性是传播的唯一通道。
- 关系式中的扭转是 $\det(E_x)$：来自 $E$ 在 $x$ 处纤维的行列式，与 $M\mapsto M(-x)$ 的平移方向配套。
- 两条式子互为逆：$(t_x^{d+n})^*$ 与 $(\tau_x^d)^*$ 方向相反，扭转因子也取逆 $\det(E_x)^{-1}$。

## 关键公式

- $j_d:C_n\cap\operatorname{Bun}_n^d\hookrightarrow\operatorname{Bun}_n^d$
- $\operatorname{Aut}_E^d:=j_{d,!*}(\operatorname{Aut}_E|_{C_n\cap\operatorname{Bun}_n^d})$
- $(t_x^{d+n})^*\operatorname{Aut}_E^d\simeq\det(E_x)\otimes\operatorname{Aut}_E^{d+n}$
- $(\tau_x^d)^*\operatorname{Aut}_E^{d+n}\simeq\det(E_x)^{-1}\otimes\operatorname{Aut}_E^d$
- $t_x^{d+n}:\operatorname{Bun}_n^{d+n}\to\operatorname{Bun}_n^d,\quad M\mapsto M(-x);\qquad\tau_x^d=(t_x^{d+n})^{-1}$

## 定理与证明

### $\operatorname{Aut}_E$ 的延拓与最高次 Hecke 关系（要点（有缺口））

中间延拓 $\operatorname{Aut}_E^d:=j_{d,!*}(\operatorname{Aut}_E|_{C_n\cap\operatorname{Bun}_n^d})$ 经最高次 Hecke 关系唯一地跨分支拼接为 $\operatorname{Aut}_E\in D(\operatorname{Bun}_n)$；它是以 $E$ 为特征值的 Hecke 特征层，并满足 $(t_x^{d+n})^*\operatorname{Aut}_E^d\simeq\det(E_x)\otimes\operatorname{Aut}_E^{d+n}$，等价地 $(\tau_x^d)^*\operatorname{Aut}_E^{d+n}\simeq\det(E_x)^{-1}\otimes\operatorname{Aut}_E^d$。

1. 在次数 $d$ 分支内取中间延拓 $\operatorname{Aut}_E^d:=j_{d,!*}(\operatorname{Aut}_E|_{C_n\cap\operatorname{Bun}_n^d})$；洁净范围内它与 $j_{d,!}$、$j_{d,*}$ 一致。  
   *为什么*：中间延拓是唯一使层在开子叠上不变、且在补集上尽可能小的延拓，故是分支内的自然选择。
2. 最高次 Hecke 关系给出分支之间的唯一延拓：$M\mapsto M(-x)$ 使次数减少 $n$，故最高次关系已把差 $n$ 的相邻分支钉死。  
   *为什么*：若两个跨分支延拓都满足最高次关系，则它们相差一个沿 $t_x^{d+n}$ 平移不变的因子；该因子又被 $d=0$ 附近的归一化与 $t_x^{n}$ 的生成性排除，故唯一。
3. $\operatorname{Hecke}_n^1$ 与最高次 Hecke 对应之间的相容性，把第一 Hecke 关系从良好开子叠传播到延拓层。  
   *为什么*：第一 Hecke 关系在 $C_n\cap\operatorname{Bun}_n^d$ 上已知（§8.5 命题 8.5.1），要把它搬到补集，只能借两条对应（$\operatorname{Hecke}_n^1$ 与最高次）的相容性。
4. 于是得到以 $E$ 为特征值的 Hecke 特征层 $\operatorname{Aut}_E\in D(\operatorname{Bun}_n)$；按第 2 章的 Hecke 对应约定写成两个分支间的同构 $(\tau_x^d)^*\operatorname{Aut}_E^{d+n}\simeq\det(E_x)^{-1}\otimes\operatorname{Aut}_E^d$，其逆形式为 $(t_x^{d+n})^*\operatorname{Aut}_E^d\simeq\det(E_x)\otimes\operatorname{Aut}_E^{d+n}$。  
   *为什么*：$\tau_x^d$ 与 $t_x^{d+n}$ 互逆，扭转因子 $\det(E_x)$ 随之取逆，两式等价。

> 缺口：讲义只用一段话给出延拓路径（中间延拓 + 最高次 Hecke 关系 + 相容性传播），未展开唯一性细节，也未逐字推导 $\det(E_x)$ 扭转；Hecke 关系式标明『采用第 2 章的 Hecke 对应约定』，其约定在 §2。

*出处*：§8.6 / 原书 p.47


## 易错点

- $j_{d,!*}$ 是中间延拓而不是 $j_{d,!}$ 或 $j_{d,*}$ 的简写：只有在洁净范围内三者才相同，一般情形必须保留 $!*$。
- 跨分支的唯一性用的是**最高次** Hecke 关系（差 $n$ 的分支），不是第一 Hecke 关系；不要把两者弄反。
- $t_x^{d+n}$ 的方向是 $\operatorname{Bun}_n^{d+n}\to\operatorname{Bun}_n^d$、$M\mapsto M(-x)$（降次），$\tau_x^d$ 反过来升次；写错方向会让 $\det(E_x)$ 的指数也跟着错。
- $\det(E_x)$ 与 $\det(E_x)^{-1}$ 分别在两条等价式子中，不能同时写成同一个方向。

## 出处

- 陈麟《Introduction to Geometric Langlands Theory》（2023 秋清华讲义，2025-08-08 修订，85 页），§8.6 延拓到整个 $\operatorname{Bun}_n$ 及尖点性，p.47（PDF p.47），`源码/chapters/ch08.tex:118-121（延拓）；112-115（Hecke 关系式）`

## 核验

状态：`source-only`（2026-11-18）
- nLab：https://ncatlab.org/nlab/show/Hecke+correspondence — $Hck$ 参数化带 modification 的束对、$\pi_1,\pi_2$ 两投影，且「The objects preserved by such a transform up to a tensor multiple are called Hecke eigensheaves.」支持卡里最高次 Hecke 关系 $(t_x^{d+n})^*\operatorname{Aut}_E^d\simeq\det(E_x)\otimes\operatorname{Aut}_E^{d+n}$ 的「张量倍」语义；页面不含 $\det(E_x)$ 的具体扭转与 $t_x/\tau_x$ 的方向。
- JAMS：https://www.ams.org/journals/jams/2002-15-02/S0894-0347-01-00388-5/S0894-0347-01-00388-5.pdf — $\operatorname{Aut}_E$ 是 $\mathrm{Bun}_n$ 上每个分支不可约的反常层、且是 Hecke 特征层——支持卡里把 $\operatorname{Aut}_E$ 延拓到整个 $\mathrm{Bun}_n$ 并保持 Hecke 关系；片段不含最高次关系式的证明。

## 关联

- `glc/concept/aut-e-cuspidal`
- `glc/concept/hecke-laumon-to-hecke`
- `glc/concept/aut-e-whittaker-laumon`
