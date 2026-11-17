# K–W 2006 资料卡 · 骨架图

这张图是整套卡的地图：**上面是四维物理，中间是扭化与紧化，下面是二维几何，右下是 Langlands 一侧**。箭头旁标的是「哪一段原文（印刷页）在讲这件事」。概念卡与推导卡就是这条链上的节点与边。

```mermaid
flowchart TD
    subgraph 4d["四维：N=4 SYM"]
        N4["N=4 SYM<br/>场内容、16 超荷<br/>B p.6"] --> TAU["τ = θ/2π + 4πi/g²<br/>B p.8"]
        TAU --> SDUAL["S-对偶 τ→−1/(n_g τ)<br/>G ↔ ^LG<br/>B p.11"]
        SDUAL --> GNO["GNO 对偶群 = ^LG<br/>B p.3"]
    end

    subgraph TW["扭化：一族 4d 拓扑场论"]
        N4 --> TWIST["GL 扭化<br/>B p.17"]
        TWIST --> CP1["CP¹ 参数族 t<br/>Q²=0<br/>B p.22"]
        CP1 --> PSI["典范参数 Ψ<br/>理论与 t 无关，只依赖 Ψ<br/>B p.35"]
    end

    subgraph STAGE["舞台：Riemann 面与 Hitchin 模空间"]
        PSI --> COMP["紧化到 Σ×C<br/>B p.38"]
        COMP --> MH["M_H：超凯勒商<br/>三个复结构 I, J, K<br/>B p.40"]
        MH --> HFIB["Hitchin 纤维化<br/>完全可积<br/>B p.53"]
    end

    subgraph 2D["二维：sigma 模型与膜"]
        MH --> SIGMA["2d 拓扑 sigma 模型<br/>target = M_H<br/>B p.58"]
        SIGMA --> AB["A-模型 / B-模型<br/>B p.61"]
        AB --> MIR["Ψ=∞ 时：S-对偶 = 镜像<br/>B p.70"]
        MIR --> BRANE["A-膜 / B-膜<br/>B p.80"]
    end

    subgraph OPS["线算子与特征膜"]
        BRANE --> WIL["Wilson 算子<br/>B p.79"]
        BRANE --> THT["'t Hooft 算子<br/>B p.81"]
        WIL --> EIG["特征膜 XB ≅ B⊗V<br/>B p.95"]
        THT --> ELE["电特征膜 = 局部系统<br/>π₁(C) → ^LG_C<br/>B p.122"]
    end

    subgraph GL["Langlands 一侧"]
        ELE --> HECKE["Hecke 修改<br/>B p.128"]
        HECKE --> GR["仿射 Grassmannian<br/>B p.145"]
        GR --> BOG["Bogomolny 方程<br/>修改空间 = 解空间<br/>B p.155"]
        HECKE --> EIGS["Hecke 特征层<br/>B p.135"]
        AB --> DMOD["A-膜 ⇒ D-模<br/>c.c. 膜、开弦代数<br/>B p.185"]
        DMOD --> EIGS
    end

    subgraph BACK["回到四维"]
        EIGS --> CHECK["§12 检查表<br/>(B,B,B) / (B,A,A) / (A,B,A)<br/>B p.207"]
        DMOD --> CHECK
    end
```

## 怎么用这张图

- **第一次读**：从上往下走一遍，每个框点开对应的概念卡；框与框之间的箭头，点开对应的推导卡。
- **想补细节**：每张卡末尾都有「出处（印刷页）」，可以回 `B p.N` 那一页逐行对照。
- **想自测**：每张概念卡第一行是「先自测」问题，先不看卡面回答一遍。

## 图与卡、与原文的对应

| 图上节点 | 概念卡 | 原文页 |
|---|---|---|
| 4d 物理块 | `n4-sym-theory` `theta-angle` `s-duality` `gno-dual-group` `langlands-dual-group` | 2–16 |
| 扭化块 | `topological-twist` `topological-qft` `brst-operator` `cohomology` | 16–38 |
| 舞台块 | `riemann-surface` `higgs-bundle` `hitchin-moduli` `hyperkahler-quotient` `hitchin-fibration` | 38–56 |
| 二维块 | `a-model` `b-model` `mirror-symmetry` `a-brane` `b-brane` | 56–78 |
| 算子块 | `wilson-operator` `thooft-operator` `eigenbrane` | 78–123 |
| Langlands 块 | `hecke-operator` `affine-grassmannian` `bogomolny-equation` `d-module` `canonical-coisotropic-brane` | 123–207 |
| 汇合处 | `geometric-langlands` `hecke-eigensheaf` | 2–5, 207–222 |

## 三个最容易搭错的地方

1. **S-对偶 ≠ 只是 $\tau\mapsto-1/\tau$**：它同时换群 $G\leftrightarrow{}^L G$、换电与磁。
2. **$\mathcal M_H$ 的三个复结构不是三个流形**：同一个点集、三套全纯坐标；B-模型与 A-模型只是选了不同复结构。
3. **A-膜 ⇒ D-模不是函子性定理**：原文只对 c.c. A-膜单向构造，措辞是 will show + roughly speaking；这是 §11 的诚实边界。
