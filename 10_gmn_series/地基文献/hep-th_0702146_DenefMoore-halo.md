# Denef–Moore：分裂态、halo 与多中心束缚态 (2007)

| 项 | 内容 |
|---|---|
| 文献 | F. Denef, G. W. Moore, *Split states, entropy enigmas, holes and halos* |
| arXiv | [hep-th/0702146](https://arxiv.org/abs/hep-th/0702146)（v2, 2007-06-18） |
| 页数 | 152 |
| 本地 | `00_原文/基础文献/04_DenefMoore与多中心解/hep-th_0702146_DenefMoore-halo.pdf` |

## 1. 它解决什么

紧 CY 上 D-brane 的 BPS 简并到底怎么算？本文用引力侧的多中心黑洞图像给出**因子化公式**：一个 BPS 态可以「分裂」成若干中心，各中心之间由 attractor flow tree 组织；于是 BPS 希尔伯特空间按流树因子化，DT 不变量与 D6–D2–D0 的 BPS 指标因此可以逐级约化。副产品：OSV 猜想的精化版本、以及「熵谜题」——大体积下双中心解的熵按 Λ³ 增长，竟可能超过同电荷单中心黑洞的 Λ²·S(Γ)，说明小 g_top 下 OSV 会失效。

## 2. 核心构造 / 定理（给式号或页码）

- §3.2.2（p.33）attractor flow trees：多中心 BPS 解存在的判据（各中心电荷与位置的相容性）。
- **§3.2.3（p.35）**「Attractor flow trees and the Hilbert space of quantum BPS states」：本篇最核心的一节——量子 BPS 态的希尔伯特空间按流树**张量因子化**，每个节点贡献一个单中心态，于是指标 = 各节点指标之积。这就是「split state」的精确含义。
- §3.5（p.41）「The Entropy Enigma」给出熵比较；§1.2（p.8）老实列出「完整证明还缺什么」（swing states、cutoff 依赖），这一段是读 GMN1 §7 之前最该看的。
- §1（p.3）的 outline 与 §2 的「D4–D2–D0 配分函数的 fareytail 展开」是技术主体，与 GMN 主线关系较远。

## 3. GMN1–3 里哪一步用到它

- **GMN1 §7（p.49，A proof of the wall-crossing formula）**：GMN1 的物理证明就是「BPS 态在墙两侧重排、但希尔伯特空间整体不变」——这个「重排即因子化」的机制正是本文 §3.2.3 的结论。GMN1 §7 里说的「分裂态」（split states）一词直接取自本文标题。
- **GMN3 §3**「Hilbert spaces, halos, and wall-crossing」把本文的 halo 图像搬到 framed BPS 态上：一个 framed 态外面套一圈 halo（围绕的 BPS 粒子），halo 的 Fock 空间给出穿墙变换的显式算符。
- GMN2 §2.3 在讲 Ω(γ) 的物理意义时，也用「多中心束缚态」作为穿墙的直观图像。

## 4. 读它的前置知识

Denef 的两篇前作（本库第 15、16 条）——多中心 BPS 解与 flow 方程；4d N=2 超引力的 BPS 解与 attractor 机制；CY 的 Gopakumar–Vafa/DT 不变量。152 页里只需 §1.1 + §3.2.3 约 20 页。
