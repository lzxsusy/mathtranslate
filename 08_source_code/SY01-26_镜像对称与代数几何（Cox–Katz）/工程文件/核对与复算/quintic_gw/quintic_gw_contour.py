#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""五次三维簇的有理曲线计数——复平面围道积分版（与 quintic_gw.py 互为独立实现）。

思路与 quintic_gw.py 相同（都用 Cox--Katz §5.6.4 式 (5.72) 的闭式），但：

  * 用 mpmath 做 50 位精度浮点，而不是有理数精确算术；
  * 不展开 Y(q) 的幂级数，而是沿 |q| = r 的圆周采样，用
        c_d = [q^d] Y(q) = (1/2πi) ∮ Y(q) q^{-(d+1)} dq
                       ≈ (1/M) Σ_{k=0}^{M-1} Y(q_k) / q_k^d ,   q_k = r·e^{2πik/M}
    数值提取系数（离散傅里叶）；
  * 镜像映射 q = -z·e^{G(z)} 的逆，用牛顿迭代对每个采样点单独求 z(q)，
    不做级数反演。

两条完全不同的代码路径给出同一串整数，这才是"复算通过"的证据。

依赖：mpmath（`pip install mpmath`；若用 Anaconda/Sage 自带则无需安装）。
用法：
    python quintic_gw_contour.py                 # 默认 r=1e-4, M=128, dps=50
    python quintic_gw_contour.py --r 2e-4 --M 256 --dps 60
"""

import argparse
import sys
import time
from math import factorial

try:
    import mpmath as mp
except ImportError:
    sys.exit("需要 mpmath：pip install mpmath")

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


class Quintic:
    """五次三维簇镜像的周期 y0、G 与 Yukawa 耦合 Y(z)。"""

    def __init__(self, nmax=600, dps=50):
        mp.mp.dps = dps
        self.nmax = nmax
        # a_n = (5n)!/(n!)^5，用 mpf 存
        self.a = [mp.mpf(factorial(5 * n)) / mp.mpf(factorial(n)) ** 5
                  for n in range(nmax)]
        # 谐波数 H_m
        self.H = [mp.mpf(0)] * (5 * nmax + 1)
        s = mp.mpf(0)
        for m in range(1, 5 * nmax + 1):
            s += mp.mpf(1) / m
            self.H[m] = s

    # ---- 周期与全纯函数 G ----
    def y0(self, z):
        s = mp.mpf(0)
        for n in range(self.nmax):
            t = self.a[n] * z ** n
            if n % 2:
                t = -t
            s += t
            if n > 20 and abs(t) < abs(s) * mp.mpf(10) ** (-mp.mp.dps - 5):
                break
        return s

    def G(self, z):
        """y1/y0 - log(-z) 的全纯部分。"""
        num = mp.mpf(0)
        for n in range(1, self.nmax):
            t = self.a[n] * (self.H[5 * n] - self.H[n]) * 5 * z ** n
            if n % 2:
                t = -t
            num += t
            if n > 20 and abs(t) < abs(num) * mp.mpf(10) ** (-mp.mp.dps - 5):
                break
        return num / self.y0(z)

    def Gp(self, z):
        """G'(z)，用中心差分到精度的平方根阶。"""
        h = abs(z) * mp.mpf(10) ** (-mp.mp.dps // 3)
        return (self.G(z + h) - self.G(z - h)) / (2 * h)

    def q_of_z(self, z):
        return -z * mp.e ** self.G(z)

    def Y_of_z(self, z):
        y0 = self.y0(z)
        w = 1 + z * self.Gp(z)
        return 5 / ((1 + 5 ** 5 * z) * y0 ** 2 * w ** 3)

    # ---- 牛顿法：给定 q 求 z（q = -z e^{G(z)}）----
    def z_of_q(self, q, iters=60):
        z = -q
        for _ in range(iters):
            f = -z * mp.e ** self.G(z) - q
            fp = -mp.e ** self.G(z) * (1 + z * self.Gp(z))
            dz = f / fp
            z -= dz
            if abs(dz) < abs(z) * mp.mpf(10) ** (-mp.mp.dps + 8):
                break
        return z


def coefficients(qc, r, M, dmax):
    """c_d = (1/M) Σ_k Y(q_k) q_k^{-d}，q_k = r ω^k。"""
    w = mp.e ** (2j * mp.pi / M)
    vals = []
    for k in range(M):
        q = r * (w ** k)
        z = qc.z_of_q(q)
        vals.append(qc.Y_of_z(z))
    c = {}
    for d in range(1, dmax + 1):
        s = mp.mpc(0)                     # 必须是 mpmath 复数，否则退化成 float64
        for k in range(M):
            q = r * (w ** k)
            s += vals[k] / q ** d
        c[d] = (s / M).real
    return c


def main(argv=None):
    ap = argparse.ArgumentParser(description="五次三维簇 n_d 的围道积分复算")
    ap.add_argument("--r", type=float, default=1e-4, help="采样圆半径（默认 1e-4）")
    ap.add_argument("--M", type=int, default=128, help="采样点数（默认 128）")
    ap.add_argument("--dps", type=int, default=50, help="十进制精度（默认 50）")
    ap.add_argument("--to", type=int, default=10, help="算到 n_TO")
    args = ap.parse_args(argv)

    t0 = time.time()
    qc = Quintic(dps=args.dps)
    r = mp.mpf(args.r)
    dmax = args.to

    # 先自检：z → q → z 的牛顿迭代是否回到原点
    z_test = mp.mpf("0.00001")
    q_test = qc.q_of_z(z_test)
    z_back = qc.z_of_q(q_test)
    print("=" * 78)
    print("五次三维簇 n_d —— 复平面围道积分（独立于有理数级数版）")
    print("=" * 78)
    print(f"精度 dps={args.dps}，采样圆 r={mp.nstr(r, 3)}，点数 M={args.M}")
    print(f"镜像映射自检：z={mp.nstr(z_test, 8)} → q → z'={mp.nstr(z_back, 8)}"
          f"（相对误差 {mp.nstr(abs(z_back - z_test) / abs(z_test), 3)}）")
    print()

    c = coefficients(qc, r, args.M, dmax + 4)
    n = {}
    ok = True
    print("  d |            n_d（围道积分）           |           文献值            | 一致")
    print("----+--------------------------------------+-----------------------------+-----")
    for d in range(1, dmax + 1):
        acc = mp.mpf(0)
        for e in range(1, d):
            if d % e == 0:
                acc += n[e] * e ** 3
        nd = (c[d] - acc) / d ** 3
        iv = int(mp.nint(nd))
        n[d] = iv
        ref = LITERATURE.get(d)
        if ref is None:
            print(f"{d:3d} | {iv:>36} | —                           |  —")
        else:
            good = (iv == ref) and abs(nd - iv) < mp.mpf("0.5")
            ok &= good
            print(f"{d:3d} | {iv:>36} | {ref:>27} | {'OK' if good else 'NG'}")
    print()
    print(f"用时 {time.time() - t0:.2f} s")
    print("*** 全部一致 ***" if ok else "*** 有不一致，请检查 ***")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
