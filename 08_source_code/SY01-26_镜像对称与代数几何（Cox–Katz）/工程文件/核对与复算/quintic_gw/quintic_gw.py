#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""五次三维簇的有理曲线计数（Gromov--Witten 不变量 n_d）——纯标准库、精确算术。

这个程序只做一件事：把 Cox--Katz《Mirror Symmetry and Algebraic Geometry》
§5.6.4 例 5.6.4（中译本式 (5.72)，标签 eq:quintic-normalized-yukawa）写下的
镜像对称闭式，逐项算成整数，再和书上第 2 章表格（以及文献值）逐项比对。

数学依据
--------
五次三维簇的镜像映射与归一化 Yukawa 耦合：

    y0(z) = Σ_{n≥0} (5n)!/(n!)^5 · (-1)^n z^n ,
    y1(z) = y0(z)·log(-z) + 5 Σ_{n≥1} (5n)!/(n!)^5 · (H_{5n}-H_n) · (-1)^n z^n ,
    q     = exp(y1/y0)              （镜像映射，q 是 A 模型一侧的坐标）
    Y(z)  = 5 / [ (1+5^5 z) · y0(z)^2 · ((q/z)(dz/dq))^3 ] ,

写 T := y1/y0 - log(-z) = G(z)（全纯，G(0)=0），则 q = -z·e^{G(z)}，于是

    (q/z)(dz/dq) = 1/(1 + z G'(z)) ,
    Y(z) = 5 / [ (1+5^5 z) · y0(z)^2 · (1+z G'(z))^3 ] .

A 模型一侧的瞬子展开（第 2 章）给出

    Y(q) = 5 + Σ_{d≥1} n_d · d^3 · q^d/(1-q^d) ,

所以若 c_d := [q^d](Y-5)，则

    c_d = Σ_{e|d} n_e e^3   ⟹   n_d = d^{-3} · ( c_d - Σ_{e|d, e<d} n_e e^3 ) .

算法
----
1. 在 z 处做截断幂级数（有理数 Fraction，无浮点误差）；
2. 用 *Lagrange 反演公式* 把 q = -z·e^{G(z)} 反解成 z = Σ_n (1/n)[z^{n-1}](-e^{-G})^n q^n
   （不是逐项递推，而是闭式系数，便于与其它实现交叉核对）；
3. 代入得 Y(q)，提取 c_d，逐 d 反解 n_d；
4. 与书表 / 文献值逐项比对，打印 OK/NG。

用法
----
    python quintic_gw.py            # 算到 n_10
    python quintic_gw.py --to 20    # 算到 n_20（纯有理数，稍慢）

不需要任何第三方库。与同目录 quintic_gw_contour.py（复平面围道积分、mpmath）
互为独立实现：两者共用数学公式，但反解镜像映射与取 q 系数的方式完全不同。
"""

from fractions import Fraction as F
from math import factorial, gcd
import argparse
import sys
import time

# ----------------------------------------------------------------------------
# 极简幂级数工具（截断到 z^N，系数为 Fraction）
# ----------------------------------------------------------------------------
ZERO = F(0)
ONE = F(1)


def zeros(N):
    return [ZERO] * N


def const(N, c):
    v = zeros(N)
    v[0] = F(c)
    return v


def z_var(N):
    v = zeros(N)
    v[1] = ONE
    return v


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def scale(a, c):
    return [x * c for x in a]


def mul(a, b):
    N = len(a)
    out = zeros(N)
    for i, ai in enumerate(a):
        if ai:
            lim = N - i
            for j in range(lim):
                if b[j]:
                    out[i + j] += ai * b[j]
    return out


def inv(a):
    N = len(a)
    assert a[0] != 0, "常数项为零，不可逆"
    out = zeros(N)
    out[0] = ONE / a[0]
    for n in range(1, N):
        s = ZERO
        for k in range(1, n + 1):
            s += a[k] * out[n - k]
        out[n] = -s / a[0]
    return out


def div(a, b):
    return mul(a, inv(b))


def deriv(a):
    N = len(a)
    out = zeros(N)
    for i in range(1, N):
        out[i - 1] = F(i) * a[i]
    return out


def exp_series(a):
    """exp(a)，要求 a[0] = 0。"""
    N = len(a)
    out = zeros(N)
    out[0] = ONE
    for n in range(1, N):
        s = ZERO
        for k in range(1, n + 1):
            s += F(k) * a[k] * out[n - k]
        out[n] = s / n
    return out


def compose(f, g):
    """f(g(z))，g[0] = 0。"""
    N = len(f)
    out = zeros(N)
    p = const(N, 1)          # g^0
    for k in range(N):
        if f[k]:
            out = add(out, scale(p, f[k]))
        p = mul(p, g)
    return out


def power(a, k):
    """a^k（k ≥ 0 整数）。"""
    N = len(a)
    out = const(N, 1)
    base = a
    while k:
        if k & 1:
            out = mul(out, base)
        base = mul(base, base)
        k >>= 1
    return out


# ----------------------------------------------------------------------------
# 五次三维簇的数据
# ----------------------------------------------------------------------------
def harmonic_table(M):
    """H_m = 1 + 1/2 + ... + 1/m，m ≤ M。"""
    H = [ZERO] * (M + 1)
    for m in range(1, M + 1):
        H[m] = H[m - 1] + F(1, m)
    return H


def quintic_periods(N):
    """返回 y0(z) 与 G(z) = y1/y0 - log(-z)。"""
    H = harmonic_table(5 * N)
    a = [F(factorial(5 * n), factorial(n) ** 5) for n in range(N)]     # (5n)!/(n!)^5
    y0 = [(-1) ** n * a[n] for n in range(N)]
    # 5·Σ_{j=n+1}^{5n} 1/j = 5 (H_{5n} - H_n)
    S = [5 * (H[5 * n] - H[n]) for n in range(N)]
    y1_holo = [(-1) ** n * a[n] * S[n] for n in range(N)]
    G = div(y1_holo, y0)
    return y0, G


def lagrange_inverse(Phi, N):
    """z = q·Φ(z) 的复合逆：z(q) = Σ_{n≥1} (1/n)[z^{n-1}] Φ(z)^n q^n。"""
    out = zeros(N)
    p = const(N, 1)           # Φ^0
    for n in range(1, N):
        p = mul(p, Phi)       # Φ^n
        out[n] = p[n - 1] / n
    return out


def yukawa_series(N):
    """返回 Y(z) 的有理系数截断级数。"""
    y0, G = quintic_periods(N)
    one_plus = const(N, 1)
    one_plus[1] = F(5 ** 5)                       # 1 + 5^5 z
    one_plus_zG = add(const(N, 1), mul(z_var(N), deriv(G)))   # 1 + z G'(z)
    den = mul(mul(one_plus, power(y0, 2)), power(one_plus_zG, 3))
    return div(const(N, 5), den)


def instanton_numbers(N):
    """返回 c_d 与 n_d（d < N）。"""
    Y = yukawa_series(N)
    # q = -z e^G  ⟹  z = q·Φ(z),  Φ = -e^{-G}
    _, G = quintic_periods(N)
    Phi = scale(exp_series(scale(G, -1)), -1)
    z_of_q = lagrange_inverse(Phi, N)
    Yq = compose(Y, z_of_q)
    c = list(Yq)
    c[0] -= 5                                     # Y - 5
    n = [ZERO] * N
    for d in range(1, N):
        acc = ZERO
        for e in range(1, d):
            if d % e == 0:
                acc += n[e] * e ** 3
        n[d] = (c[d] - acc) / d ** 3
    return c, n


# ----------------------------------------------------------------------------
# 与文献 / 书表比对
# ----------------------------------------------------------------------------
LITERATURE = {
    1: 2875,
    2: 609250,
    3: 317206375,
    4: 242467530000,
    5: 229305888887625,
    6: 248249742118022000,
    7: 295091050570845659250,
    8: 375632160937476603550000,
    9: 503840510416985243645106250,
    10: 704288164978454686113488249750,
}

# 书第 2 章表格（Cox--Katz 中译本）给出的 GW 不变量 N_d = Σ_{e|d} n_e e^3 前几项
BOOK_GW = {1: 2875, 2: 4876875 // 1, 3: 8564575000}


def main(argv=None):
    ap = argparse.ArgumentParser(description="五次三维簇有理曲线计数（精确算术）")
    ap.add_argument("--to", type=int, default=10, help="算到 n_TO（默认 10）")
    args = ap.parse_args(argv)

    dmax = args.to
    N = dmax + 1 + 12           # 多算 12 阶，保证反解 n_d 的系数足够精确
    t0 = time.time()
    c, n = instanton_numbers(N)
    dt = time.time() - t0

    print("=" * 78)
    print("五次三维簇：Gromov--Witten 不变量 n_d（Cox--Katz §5.6.4 (5.72)）")
    print("=" * 78)
    print(f"截断阶数 N = {N}，全程有理数精确算术，用时 {dt:.2f} s")
    print()
    print("  d |            n_d（本程序）            |           文献值            | 一致")
    print("----+--------------------------------------+-----------------------------+-----")
    ok = True
    for d in range(1, dmax + 1):
        val = n[d]
        if val.denominator != 1:
            print(f"{d:3d} | {str(val):>36} | (非整数?)                    |  NG")
            ok = False
            continue
        iv = val.numerator
        ref = LITERATURE.get(d)
        if ref is None:
            print(f"{d:3d} | {iv:>36} | —                           |  —")
        else:
            good = (iv == ref)
            ok &= good
            print(f"{d:3d} | {iv:>36} | {ref:>27} | {'OK' if good else 'NG'}")
    print()
    print("书表核对（N_d = Σ_{e|d} n_e e^3）：")
    for d, expect in BOOK_GW.items():
        got = sum(n[e] * e ** 3 for e in range(1, d + 1) if d % e == 0)
        print(f"  N_{d} = {got}  （书表 {expect}）{'OK' if got == expect else 'NG'}")
        ok &= (got == expect)
    print()
    print("*** 全部一致 ***" if ok else "*** 有不一致，请检查 ***")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
