# 余切丛 $T^*X$ 的典范辛形式（$X=\mathbb{R}^2$）

> `geoq/example/cotangent-bundle-symplectic` · 轨道 A · 相空间的辛几何 · 状态 draft

> **这张卡练什么**：$\lambda=\sum_ip_i\,dq^i$ 在换底流形坐标时怎样变换，$\omega$ 又为什么纹丝不动？

## 一句话

在 $T^*\mathbb{R}^2$ 上具体写出 $\lambda=\sum p_idq^i$ 与 $\omega=d\lambda$，检验非退化，并用一次非线性换元验证 $\lambda$ 与 $\omega$ 都不依赖坐标。

## 设定

取 $X=\mathbb{R}^2$，坐标 $q^1,q^2$，余切丛 $T^*X\cong\mathbb{R}^4$ 的纤维坐标记为 $p_1,p_2$。刘维尔形式 $\lambda=p_1dq^1+p_2dq^2$，辛形式 $\omega=d\lambda=dp_1\wedge dq^1+dp_2\wedge dq^2$。另取 $X$ 上的非线性坐标 $q'^1=q^1$、$q'^2=q^2+(q^1)^2$。

## 计算

**第 1 步**：算 $\omega$ 在坐标基上的取值：$\omega(\partial_{p_i},\partial_{q^j})=\delta_{ij}$，而 $\omega(\partial_{p_i},\partial_{p_j})=\omega(\partial_{q^i},\partial_{q^j})=0$。

> 为什么：$\omega$ 是常系数 $2$-形式，只需在 $2n$ 个基向量上取一次值就能确定整个矩阵。

**第 2 步**：非退化检验：把基按 $(\partial_{p_1},\partial_{p_2},\partial_{q^1},\partial_{q^2})$ 排列，配对矩阵中非零的只有 $p_i$ 与 $q^i$ 之间的 $1$，矩阵可逆（行列式为 $1$），故 $\omega$ 非退化；又 $\omega=d\lambda$ 自动闭，于是 $(T^*X,\omega)$ 是辛流形。

> 为什么：非退化在坐标下就是矩阵可逆，闭性则是 $d^2=0$；两条公理一次验证完毕。

**第 3 步**：换坐标：由 $q^1=q'^1$、$q^2=q'^2-(q'^1)^2$ 得 $\partial q^1/\partial q'^1=1$、$\partial q^1/\partial q'^2=0$、$\partial q^2/\partial q'^1=-2q'^1$、$\partial q^2/\partial q'^2=1$，故 $p'_1=p_1-2q^1p_2$、$p'_2=p_2$。

> 为什么：纤维坐标是余切向量，按 $p'_i=\sum_jp_j\,\partial q^j/\partial q'^i$ 变换，这正是链式法则的转置。

**第 4 步**：验证 $\lambda$ 不变：$p'_1dq'^1+p'_2dq'^2=(p_1-2q^1p_2)dq^1+p_2(dq^2+2q^1dq^1)=p_1dq^1+p_2dq^2$，交叉项 $-2q^1p_2dq^1$ 与 $+2q^1p_2dq^1$ 相消。

> 为什么：换元的雅可比项恰好互相抵消，说明 $\lambda$ 是整体对象而非坐标产物。

**第 5 步**：验证 $\omega$ 不变：$dp'_1=dp_1-2p_2dq^1-2q^1dp_2$，故 $dp'_1\wedge dq'^1=dp_1\wedge dq^1-2q^1dp_2\wedge dq^1$（$dq^1\wedge dq^1=0$）；又 $dp'_2\wedge dq'^2=dp_2\wedge dq^2+2q^1dp_2\wedge dq^1$。两式相加，$\pm2q^1dp_2\wedge dq^1$ 相消，得 $\omega=dp_1\wedge dq^1+dp_2\wedge dq^2$。

> 为什么：这一步是第 4 步的外微分版本：交叉项成对抵消，$\omega$ 的坐标表达式因此与坐标选取无关。

## 结果

$\lambda=\sum_ip_i\,dq^i$ 与 $\omega=\sum_idp_i\wedge dq^i$ 在非线性换元 $q'^2=q^2+(q^1)^2$ 下都保持形式不变，$\omega$ 非退化且闭，$T^*\mathbb{R}^2$ 因此是辛流形；体积形式为 $\omega^2/2!=dp_1\wedge dq^1\wedge dp_2\wedge dq^2$。

## 复核

取一点 $q^1=2$、$p_1=3$、$p_2=5$。旧坐标下 $\lambda(\partial_{q^1})=p_1=3$；新坐标下 $p'_1=3-2\cdot2\cdot5=-17$、$p'_2=5$，而 $dq'^1(\partial_{q^1})=1$、$dq'^2(\partial_{q^1})=2q^1=4$，故 $\lambda(\partial_{q^1})=p'_1\cdot1+p'_2\cdot4=-17+20=3$，与旧值一致。

## 易错点

- $p'_1=p_1-2q^1p_2$ 说明纤维坐标会随底流形坐标混合；若误以为 $p_i$ 是 $X$ 上的函数而令 $p'_1=p_1$，$\lambda$ 立刻不再是整体对象。
- 换元后 $\omega$ 的表达式不变，但这不意味着 $\omega$ 的系数在任意坐标下都相等：这里不变是因为 $\omega$ 常系数且换元是辛同胚；一般换元下 $\omega$ 的系数会变。

## 用到哪些概念

- [余切丛的典范辛结构与刘维尔形式](../concepts/cotangent-bundle.md)
- [辛流形（symplectic manifold）](../concepts/symplectic-manifold.md)

## 相关卡

- [恰当拉格朗日 $L_{df}$ 与相函数（$f=q^1q^2$）](../examples/exact-lagrangian-phase-function.md)

## 出处

- §5.1.4 例 5.1.24：余切丛的典范辛结构，p.261（PDF p.262），源码 `ch05a.tex:691-703`
