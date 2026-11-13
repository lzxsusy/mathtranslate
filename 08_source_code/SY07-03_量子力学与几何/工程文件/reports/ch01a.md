# ch01a 译校报告（Lead 自译样板块）

## 1. 覆盖范围
- chunk：`ch01a` = PDF p.12–30 = **原书 p.11–29**
- 内容：第 1 章「希尔伯特空间形式」章首 + §1.1 状态空间 + §1.2 可观测量 + §1.3 测量 + §1.4 不确定原理 + §1.5 波函数（§1.5.1–§1.5.5）
- 文件：`src/chunks/ch01a.tex`（约 40 KB）
- 块界：文件末句「……本征值 $E$ 自然被理解为该态 $\psi$ 的能量。」为原书 p.29 的完整句；下一块 `ch01b` 从「方程 (*) 称为定态薛定谔方程」起，**不重复该句**。

## 2. 陈述环境编号（全部手工照抄原文）
| 编号 | 名称 | 原书位置 |
|---|---|---|
| Definition 1.1.1 | 希尔伯特空间（Hilbert space） | p.11 |
| Example 1.1.2 | 有限维希尔伯特空间 | p.11 |
| Example 1.1.3 | 平方可和数列空间 $\ell^2$ | p.11 |
| Remark 1.1.4 | 可分性（separability） | p.11 |
| Definition 1.1.5 | 伴随算子（adjoint operator） | p.12 |
| Definition 1.1.6 | 酉算子（unitary operator） | p.12 |
| Remark 1.1.7 | 酉算子与伴随算子的关系 | p.12 |
| Remark 1.3.1 | 玻恩规则的统计含义 | p.18 |

## 3. 公式核对（逐条回页面图像核对，未发现需批注之处）
- 薛定谔方程 $i\hbar\frac{\mathrm d}{\mathrm dt}|\psi(t)\rangle=\hat H|\psi(t)\rangle$、形式解 $|\psi(t)\rangle=\mathrm e^{-\mathrm i\hat Ht/\hbar}|\psi(0)\rangle$（p.13）
- 泊松括号 $\{-,-\}:\mathcal O(M)\times\mathcal O(M)\to\mathcal O(M)$ 与其反对称性、莱布尼茨律、雅可比恒等式（p.13）
- $\{f,g\}=\sum_i\left(\frac{\partial f}{\partial x_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial x_i}\right)$（p.13）
- Born 规则 $P(\lambda_i)=\langle\psi|P_i|\psi\rangle$、$\sum_i P_i=\mathrm{id}$（p.17）
- 双缝振幅叠加 $A=A_1+A_2$、$P=|A_1+A_2|^2\ne P_1+P_2$（p.20）
- 不确定度定义 $(\Delta_\psi O)^2=\langle O^2\rangle_\psi-\langle O\rangle_\psi^2$（p.22）
- 罗伯逊不等式 $(\Delta_\psi A)^2(\Delta_\psi B)^2\ge\frac14|\langle[A,B]\rangle_\psi|^2$ 及其证明（p.22–24）
- 正则对易关系 $[\hat x^k,\hat p_j]=\mathrm i\hbar\delta^k_j$、Heisenberg 关系 $\Delta\hat x^k\Delta\hat p_k\ge\hbar/2$（p.24、p.28）
- 傅里叶变换约定 $(2\pi\hbar)^{-n/2}\int\mathrm d^np\,\mathrm e^{\mathrm ip\cdot x/\hbar}\hat f(p)$（p.27）
- 哈密顿算子 $\hat H=-\frac{\hbar^2}{2m}\nabla^2+V(\mathbf x,t)$、连续性方程 $\partial_t\rho+\nabla\cdot\vec j=0$、概率流 $\vec j=\frac{\hbar}{m}\mathrm{Im}(\bar\Psi\nabla\Psi)$（p.29–30）
  - 说明：原书中间式写作 $\vec j=\frac{\mathrm i\hbar}{2m}[(\nabla\bar\Psi)\Psi-\bar\Psi\nabla\Psi]$，与下一式 $\frac{\hbar}{m}\mathrm{Im}(\bar\Psi\nabla\Psi)$ 一致（括号 $=-2\mathrm i\,\mathrm{Im}(\bar\Psi\nabla\Psi)$），**原书自洽，未加批注**。

## 4. 图
| 图 | 处理 |
|---|---|
| 双缝实验装置（原书 p.20） | TikZ 重绘，标注译中文（源 / 墙（双孔）/ 探测器） |
| 经典图像分布 $P$（原书 p.20） | TikZ 重绘（高斯峰），标注译中文 |
| 量子图像干涉条纹（原书 p.21） | TikZ 重绘（双缝干涉条纹） |
| $f(x)$ 与 $\hat f(p)$ 的宽度关系（原书 p.28） | 裁切 `figures/fig_p029_a.png`（1291×366, 300dpi） |

## 5. 术语处理要点
- operator→算子、eigenvalue→本征值、eigenvector→本征向量、self-adjoint→自伴的、adjoint→伴随算子、unitary→酉、Hermitian inner product→厄米内积、symplectic manifold→辛流形、Poisson bracket→泊松括号、observable→可观测量、expectation→期望、Born rule→玻恩规则、collapse→塌缩、uncertainty→不确定度、commutator→交换子、canonical commutation relation→正则对易关系、probability current→概率流、stationary state→定态、Laplacian→拉普拉斯算子、separable→可分的。
- 首次出现的术语给「中文（English）」，之后只用中文。

## 6. 编译自检
```
powershell -ExecutionPolicy Bypass -File build.ps1 -Chunk ch01a
LOG  file:line=0  fatal=0  missingchar=0  overfull=0  undefref=0
DRAFT PDF -> work\tmp_ch01a.pdf   (11 页)
```
已渲染 `work/preview/draft_*.png` 逐页目检：章标题、`\qmstmt` 加粗陈述头、表格、三张 TikZ 图、裁切图均正常，无溢出。

## 7. 遗留
- 无。
