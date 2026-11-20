from fractions import Fraction as F
from math import factorial

N = 10  # number of q-terms


def harmonic(n):
    return sum(F(1, k) for k in range(1, n + 1))


a = [F(factorial(5 * d), factorial(d) ** 5) for d in range(N)]
S = [5 * (harmonic(5 * d) - harmonic(d)) for d in range(N)]

w0 = a[:]                                # omega0 = sum a_d q^d
sig = [a[d] * S[d] for d in range(N)]    # sigma  = sum a_d S_d q^d


def mul(p, q, n=N):
    r = [F(0)] * n
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            if i + j < n and x and y:
                r[i + j] += x * y
    return r


def inv(p, n=N):
    r = [F(0)] * n
    r[0] = 1 / p[0]
    for k in range(1, n):
        s = F(0)
        for i in range(1, k + 1):
            s += p[i] * r[k - i]
        r[k] = -s * r[0]
    return r


w0inv = inv(w0)
Treg = mul(sig, w0inv)                   # T = log q + Treg(q)

# D = q d/dq T = 1 + q d/dq Treg
D = [F(1)] + [k * Treg[k] for k in range(1, N)]

Dinv = inv(D)
D3inv = mul(mul(Dinv, Dinv, N), Dinv, N)
K = [5 * x for x in D3inv]

print("D   =", [str(x) for x in D[:5]])
print("5/D^3 =", [str(x) for x in K[:6]])
print("expect K = 5 + 2875 q + 4876875 q^2 + ...")

# mirror map: Q = q exp(Treg) ; invert to q(Q) = Q + c2 Q^2 + ...
def exp_series(p, n=N):
    r = [F(0)] * n
    r[0] = F(1)
    for k in range(1, n):
        s = F(0)
        for i in range(1, k + 1):
            s += i * p[i] * r[k - i]
        r[k] = s / k
    return r

E = exp_series(Treg)
QQ = mul([F(0)] + [F(1)] + [F(0)] * (N - 2), E)   # Q(q) = q exp(Treg)
qinv = inv(QQ)
print("q(Q) =", [str(x) for x in qinv[:5]])
