#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""五次三维簇：按 Cox--Katz §5.6.4 例 5.6.4（式 eq:quintic-normalized-yukawa）
机械复算 Gromov--Witten 不变量 n_d（genus 0）。

书中公式（中译本 p.133）：
       Y = 5 / [ (1 + 5^5 z) · y0(z)^2 ] · ( (q/z)(dz/dq) )^3,
其中
       y0(z) = Σ_{n≥0} (5n)!/(n!)^5 · (-1)^n z^n,
       y1(z) = y0(z) log(-z) + 5 Σ_{n≥1} (5n)!/(n!)^5 [Σ_{j=n+1}^{5n} 1/j] (-1)^n z^n,
       q = exp(y1/y0)   （镜像映射，q 是 A 模型一侧的坐标）。

由于 q = e^T,  T = y1/y0 = log(-z) + G(z)，故
       (q/z)(dz/dq) = 1 / (z T'(z)) = 1 / (1 + z G'(z)),
       Y(z) = 5 / [ (1 + 5^5 z) · y0(z)^2 · (1 + z G'(z))^3 ]。
再把 z 换成 q（级数反演），并展开
       Y(q) = 5 + Σ_{d≥1} n_d · d^3 q^d/(1 - q^d),
用 n_d = d^{-3}[ c_d - Σ_{e|d, e<d} n_e e^3 ]（c_d = [q^d](Y-5)）反解。

全程有理数精确算术；不需要任何第三方库。
"""
from fractions import Fraction as F
from math import factorial

N = 24                      # 计算到 q^23
KMAX = 10                   # 与文献比对到 n_10


# ---------------- z 的幂级数 ----------------
def zs():                    return [F(0)] * N
def z1():
    v = zs(); v[0] = F(1); return v
def add(a, b):               return [x + y for x, y in zip(a, b)]
def sub(a, b):               return [x - y for x, y in zip(a, b)]
def mul(a, b):
    out = zs()
    for i, x in enumerate(a):
        if x:
            for j in range(N - i):
                if b[j]:
                    out[i + j] += x * b[j]
    return out
def sc(a, c):                return [x * c for x in a]
def inv(a):
    assert a[0] != 0
    out = zs(); out[0] = 1 / a[0]
    for n in range(1, N):
        s = sum(a[k] * out[n - k] for k in range(1, n + 1))
        out[n] = -s / a[0]
    return out
def div(a, b):               return mul(a, inv(b))
def deriv(a):                return [F(i) * a[i] for i in range(1, N)] + [F(0)]
def exp(a):
    assert a[0] == 0
    out = zs(); out[0] = F(1)
    for n in range(1, N):
        s = sum(F(k) * a[k] * out[n - k] for k in range(1, n + 1))
        out[n] = s / n
    return out
def compose(f, g):           # f(g), g[0] = 0
    out = zs()
    p = z1()
    for k in range(N):
        if f[k]:
            out = add(out, sc(p, f[k]))
        p = mul(p, g)
        if all(x == 0 for x in p):
            break
    return out
def revert(f):               # f 的复合逆，f[0]=0, f[1]≠0
    assert f[0] == 0 and f[1] != 0
    g = zs(); g[1] = 1 / f[1]
    for n in range(2, N):
        # 解 [z^n] f(g) = 0
        c = compose(f, g)[n]
        g[n] = -c / f[1]
    return g


# ---------------- 五次簇的数据 ----------------
# a_n = (5n)!/(n!)^5
A = [F(factorial(5 * n), factorial(n) ** 5) for n in range(N)]
# H_m = 1 + 1/2 + ... + 1/m
H = [F(0)] * (5 * N + 1)
for m in range(1, 5 * N + 1):
    H[m] = H[m - 1] + F(1, m)

y0 = [A[n] * (-1) ** n for n in range(N)]                      # y0(z)
S = [5 * (H[5 * n] - H[n]) for n in range(N)]                  # 5·Σ_{j=n+1}^{5n} 1/j
G = div([A[n] * (-1) ** n * S[n] for n in range(N)], y0)        # G = y1/y0 - log(-z)

print("y0 前 4 项:", [str(y0[i]) for i in range(4)])
print("G  前 3 项:", [str(G[i]) for i in range(3)])

# q = -z·exp(G)
zvar = zs(); zvar[1] = F(1)
q = mul(sc(zvar, F(-1)), exp(G))
print("q(z) 前 4 项:", [str(q[i]) for i in range(4)])

# Y(z) = 5 / [ (1+5^5 z) y0^2 (1 + z G')^3 ]
one_plus = zs()
one_plus[0] = F(1)
one_plus[1] = F(5 ** 5)          # 1 + 5^5 z
zGp = add(z1(), mul(zvar, deriv(G)))                                    # 1 + z G'
den = mul(mul(one_plus, mul(y0, y0)), mul(mul(zGp, zGp), zGp))
Yz = div(sc(z1(), F(5)), den)

# 把 z 换成 q：z = revert(q)
zinvq = revert(q)
Yq = compose(Yz, zinvq)
print("Y(q) 前 6 项:", [str(Yq[i]) for i in range(6)])

# ---------------- 反解 n_d ----------------
c = list(Yq)
c[0] -= 5
n = [F(0)] * N
for m in range(1, N):
    acc = sum(n[e] * e ** 3 for e in range(1, m) if m % e == 0)
    n[m] = (c[m] - acc) / m ** 3

known = {
    1: 2875, 2: 609250, 3: 317206375, 4: 242467530000,
    5: 229305888887625, 6: 248249742118022000,
    7: 295091050570845659250, 8: 375632160937476603550000,
    9: 503840510416985243645106250, 10: 704288164978454686113488249750,
}
print("\n  d |            n_d（本机复算）            |              文献值               | 一致")
ok = True
for d in range(1, KMAX + 1):
    good = (n[d] == known[d]); ok &= good
    print(f"{d:3d} | {str(n[d]):>36} | {known[d]:>33d} | {'OK' if good else 'NG'}")
print("\n*** ALL MATCH ***" if ok else "\n*** MISMATCH ***")

print("\nY(q) - 5 的 q 系数（前 6 个）:")
for i in range(1, 7):
    print(f"  q^{i}: {c[i]}")
