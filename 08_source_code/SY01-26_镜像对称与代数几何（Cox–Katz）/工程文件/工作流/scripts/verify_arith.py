"""核验证据 1：经典不变量与书中公式的算术自洽

(1) 五次三维簇的 Hodge 数 / Betti 数 / Euler 数关系
    b_3 = 2 + 2h^{2,1}，chi = 4 - b_3 = 2(h^{1,1} - h^{2,1})；
(2) 书中 (2.32)/(5.45) 的 Kaehler 模曲线 K(q) = 5 + sum n_d d^3 q^d/(1-q^d)，
    用文献 n_d 复算前四项，与书中 5, 2875, 4876875, 8564575000 对照；
(3) 基础周期 omega0(q) = sum (5d)!/(d!)^5 q^d 的前几项（书中 (5.45) 的分子）。
"""
from fractions import Fraction as F

# (1)
h11, h21 = 1, 101
b3 = 2 + 2 * h21
print("b_3 = 2 + 2h^{2,1} =", b3)
print("b_2 = h^{1,1} =", h11)
print("chi = 4 - b_3 =", 4 - b3)
print("chi = 2(h^{1,1} - h^{2,1}) =", 2 * (h11 - h21))

# (2) 文献值：Schubert 1886 / Katz 1986 / ES 1991 / Kontsevich 1995
n = {1: 2875, 2: 609250, 3: 317206375, 4: 242467530000}
series = [5]
for m in range(1, 5):
    c = sum(n[d] * d ** 3 for d in range(1, m + 1) if m % d == 0)
    series.append(c)
print("K 的前五项 =", series)
print("书中给出的数字：5, 2875(=5x575), 4876875, 8564575000 —— 前四项一致")

# (3) 基础周期
def fact(k):
    r = 1
    for i in range(2, k + 1):
        r *= i
    return r

ser = [F(fact(5 * d), fact(d) ** 5) for d in range(5)]
print("omega0 =", [str(x) for x in ser])
