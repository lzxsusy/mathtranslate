"""独立核验：只用五次的 Picard–Fuchs 算子
    L = theta^4 - 5^5 q (theta+1/5)(theta+2/5)(theta+3/5)(theta+4/5)
用 Frobenius 方法取 s=0 处的 0/1/2 阶展开，得到 y0、y0 log q + ...、log^2 解，
再由 Y = theta^2 (y2/y0) 取出 n_d（Y = 1 + sum n_d d^3 q^d/(1-q^d)）。
与 Candelas 等人的 2875, 609250, 317206375, 242467530000 对照。
"""
from fractions import Fraction as F

N = 9          # q 截断阶数
POW5 = 5 ** 5  # 3125


class Tri:
    """s 的 Taylor 展开到二阶：(f(0), f'(0), f''(0))"""

    __slots__ = ("v", "d1", "d2")

    def __init__(self, v, d1=F(0), d2=F(0)):
        self.v, self.d1, self.d2 = F(v), F(d1), F(d2)

    def __add__(self, o):
        o = o if isinstance(o, Tri) else Tri(o)
        return Tri(self.v + o.v, self.d1 + o.d1, self.d2 + o.d2)

    def __mul__(self, o):
        o = o if isinstance(o, Tri) else Tri(o)
        return Tri(self.v * o.v, self.d1 * o.v + self.v * o.d1,
                   self.d2 * o.v + 2 * self.d1 * o.d1 + self.v * o.d2)

    def __truediv__(self, o):
        o = o if isinstance(o, Tri) else Tri(o)
        assert o.v != 0
        iv = 1 / o.v
        i1 = -o.d1 * iv * iv
        i2 = (2 * o.d1 * o.d1 * iv - o.d2 * o.v) * iv ** 3
        inv = Tri(iv, i1, i2)
        return self * inv

    def __pow__(self, k):
        r = Tri(1)
        for _ in range(k):
            r = r * self
        return r


def series_div(num, den, n=N):
    r = [F(0)] * n
    for k in range(n):
        s = num[k]
        for i in range(1, k + 1):
            if i < len(den):
                s -= den[i] * r[k - i]
        r[k] = s / den[0]
    return r


# a_d(s) 的三阶数据
a = [Tri(1)]
for d in range(1, N):
    num = Tri(1)
    for k in range(1, 5):
        num = num * Tri(F(d - 1) + F(k, 5), 1, 0)   # (s + d-1+k/5)
    den = Tri(F(d), 1, 0) ** 4                       # (s+d)^4
    factor = (num / den) * F(POW5)
    a.append(a[-1] * factor)

y0 = [x.v for x in a]
y_top = [x.d1 for x in a]          # d/ds y(s)|0  -> log q 解
y_log2 = [x.d2 / 2 for x in a]     # (1/2) d^2/ds^2 -> (1/2)log^2 解

A = series_div(y_log2, y0)        # rho2/y0
B = series_div(y_top, y0)         # rho1/y0
Y = [F(d * d) * A[d] + 2 * d * B[d] for d in range(N)]
Y[0] += 1

print("y0  :", [str(x) for x in y0[:5]])
print("Y   :", [str(x) for x in Y[:6]])
print("比值 Y[0]:", Y[0])

# 归一化后解出 n_d：Y = Y0 * (1 + sum n_d d^3 q^d/(1-q^d))
c = [x / Y[0] for x in Y]
inst = []
for d in range(1, N):
    s = c[d]
    for k in range(1, d):
        if d % k == 0:
            s -= inst[k - 1] * k ** 3
    inst.append(s / d ** 3)
print("n_d :", [str(x) for x in inst])
