# 三个复结构 I、J、K

- **id**：`gw06/concept/complex-structures-ijk`
- **类型**：concept
- **位置**：§3.2
- **问题**：同一个 M_H 在 I、J、K 三个复结构下分别是什么？为什么复结构与辛形式只依赖部分参数？

> 超 Kähler 流形自带三个复结构，分别把 M_H 读成抛物希格斯丛、抛物局部系统与第三种对象，并给出参数依赖的精确陈述。

## 定义

$\mathcal M_H$ 是超 Kähler 流形，故带有三个复结构 $I,J,K$，满足 $I^2=J^2=K^2=IJK=-1$，以及相应的 Kähler 形式 $\omega_I,\omega_J,\omega_K$；三个全纯辛形式为 $\Omega_I=\omega_J+i\omega_K$、$\Omega_J=\omega_K+i\omega_I$、$\Omega_K=\omega_I+i\omega_J$。函数 $\nu_I=\mu_J+i\mu_K$ 在复结构 $I$ 下全纯，于是 $\nu_I^{-1}(0)/\mathcal G_{p,\mathbb C}$ 是一个 GIT 商，即 $\mathcal M_H$ 在复结构 $I$ 下的全纯描述：稳定抛物希格斯丛 $(E,\varphi)$ 的模空间，其中 $\varphi$ 在 $p$ 处有单极点、留数共轭于 $\sigma\,dz/z$。换成 $J$ 得到稳定抛物局部系统的模空间，其单值性被要求共轭于 $U=\exp(-2\pi(\alpha-i\gamma))$；换成 $K$ 得到第三种描述。物理上这三个复结构对应二维σ模型的三个拓扑扭曲。

**记号**：$I,J,K$：三个复结构、$\omega_I,\omega_J,\omega_K$：三个 Kähler 形式、$\Omega_I=\omega_J+i\omega_K$：全纯辛形式、$\nu_I=\mu_J+i\mu_K$：复结构 $I$ 下的全纯矩映射

## 关键点

- $\nu_I$ 全纯是整套推理的支点：它的零点集是复子簇，才能把辛商按 Kempf–Ness 换成 GIT 商；若 $\nu_I$ 只是两个实方程，这一步不成立。
- 复结构 $I$ 与全纯辛形式 $\Omega_I$ 关于 $\beta+i\gamma$ 全纯地变化、与 $\alpha$ 无关；对 $J$ 是 $\gamma+i\alpha$ 且与 $\beta$ 无关；对 $K$ 是 $\alpha+i\beta$ 且与 $\gamma$ 无关。
- $[\omega_I]$ 只依赖 $\alpha$，$[\omega_J],[\omega_K]$ 在无奇点时为零、有奇点时分别由 $\beta,\gamma$ 控制。
- $SO(3)$ 旋转 $\hat I=pI+qJ+rK$（$p^2+q^2+r^2=1$）同时旋转 $\omega$ 与 $(\alpha,\beta,\gamma)$ 后论证仍成立，由此得到 $\partial x_i/\partial y_j=0\ (i\neq j)$，即上同调类对参数的线性性。
- $I$ 下的稳定性条件依赖 $\alpha$，$J$ 下的依赖 $\beta$；对通有的 $\sigma$ 两者都与相应参数无关，跨墙现象被超 Kähler 结构回避。

## 公式

```latex
\nu_I=\mu_J+i\mu_K
```
```latex
\Omega_I=\omega_J+i\omega_K
```
```latex
U=\exp\left(-2\pi(\alpha-i\gamma)\right)
```
```latex
\hat I=pI+qJ+rK,\qquad p^2+q^2+r^2=1
```

## 定理

**Kempf–Ness：辛商等于 GIT 商**：若 $\nu_I$ 在 $I$ 下全纯、$\mathcal W$ 是带 $\mathcal G_p$ 线性作用的仿射空间，则辛商 $\nu_I^{-1}(0)/\! /\! /\mathcal G_p$ 与 GIT 商 $\nu_I^{-1}(0)/\mathcal G_{p,\mathbb C}$ 一致。

证明：sketch（§3.2，式 (3.5) 之前的讨论）

1. $\nu_I^{-1}(0)$ 是复子簇。 —— $\nu_I$ 全纯，其零点集为复解析子集。
2. 在复子簇上把实矩映射 $\mu_I$ 置零并对 $\mathcal G_p$ 作辛商。 —— 这是辛商的定义，$\nu_I$ 与 $\mu_I$ 同时为零即超 Kähler 商。
3. 由 Kempf–Ness 定理，该辛商等于复化群的 GIT 商。 —— 仿射空间上线性作用的 GIT 商恰由矩映射零集的轨道构成。

## 常见错误

- 把 $I$ 图像与 $J$ 图像说成「两个不同的模空间」，进而把稳定性依赖的参数搞反（$I$ 依赖 $\alpha$，$J$ 依赖 $\beta$）。
- 把 $U=\exp(-2\pi(\alpha-i\gamma))$ 写成 $\exp(-2\pi(\alpha+i\gamma))$，等于把 $\gamma$ 换成 $-\gamma$，与 $\Omega_J$ 依赖 $\gamma+i\alpha$ 的结论不再互相印证。
- 以为 $[\omega_J],[\omega_K]$ 恒为零：这只在无奇点（$\beta=\gamma=0$）时成立，有分歧时它们非零且正是面算符的物理效应。

## 批注

### 易错预警：三个 Ω 的指标不对齐

指标不对齐是本节最常见的错误：$\Omega_I$ 依赖 $\beta+i\gamma$，$\Omega_J$ 依赖 $\gamma+i\alpha$，$\Omega_K$ 依赖 $\alpha+i\beta$——下标 $I$ 配的是「另外两个」参数，不是 $\alpha$。抄写时若按「$I$ 配 $\alpha$」的直觉写，三个全纯辛形式会整体错位。

### 含糊点拨：「等于」是双全纯等同

「$\mathcal M_H$ 在复结构 $I$ 下等于抛物希格斯丛模空间」这句话里的相等是双全纯等同，不是集合相等：同一个点既是希钦方程的解，又在 $I$ 下被读成 $(E,\varphi)$。作者用「暂时记作 $\tilde{\mathcal M}_H$」来避免混淆，读者应把 $\tilde{\mathcal M}_H$ 理解为「$\mathcal M_H$ 换一套复坐标后的样子」。

### 背景直觉：三个复结构 = 三个拓扑扭曲

三个复结构对应二维σ模型的三个拓扑扭曲：$I$ 扭曲给出 B-模型（希格斯丛），$J$ 扭曲给出 A-模型（局部系统），$K$ 扭曲给出第三种。几何朗兰兹纲领的陈述「$\mathcal M_H(G)$ 的 B-模型 = $\mathcal M_H({}^LG)$ 的 A-模型」正是建立在 $I$ 与 $J$ 的这套对应之上。

## 出处

- Gukov–Witten 2006（hep-th/0612073v2）中译校订本 §3.2；印刷页 [35, 39] / PDF 页 [36, 40]；锚点 `08_source_code/SY02-06_规范理论、分歧与几何朗兰兹纲领/源码/sections/s03a-quotient.tex:141-305`
- 复观点与 $SO(3)$ 论证见 PDF 第 36–40 页。

---

权利：`rewritten`；核验：`source-only`（2026-11-20）。
