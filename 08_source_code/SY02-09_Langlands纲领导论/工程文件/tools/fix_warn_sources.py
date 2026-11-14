# -*- coding: utf-8 -*-
"""Batch 3: 修掉第二批来源抽查的 4 条 WARN（Lead 终审）。"""
import io, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(BASE, '..', 'src', 'chapters')

def rw(name, pairs):
    p = os.path.join(CH, name)
    s = io.open(p, encoding='utf-8').read()
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            print('!! %s: count=%d for %r' % (name, n, old[:60]))
            sys.exit(1)
        s = s.replace(old, new)
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    print('ok', name, len(pairs))

# 1+2: L7 —— 词源句页面 0 命中改掉；Tate 模注改引 Silverman ATAEC（A 级）
rw('lecture07.tex', [
    ('\\znote{「椭圆曲线」这个名字来自计算椭圆弧长时出现的椭圆积分，曲线本身与椭圆无关。特征 $2$、$3$ 时不能化成书中这种短的 Weierstrass 形式',
     '\\znote{「椭圆曲线」指亏格为 $1$ 的射影代数曲线，并指定一个有理点 $O$ 作为基点；下面的 Weierstrass 形式是它在特征不为 $2$、$3$ 时的仿射写法。特征 $2$、$3$ 时不能化成书中这种短的 Weierstrass 形式'),
    ('即曲线非奇异。[来源：nLab "elliptic curve"，\\url{https://ncatlab.org/nlab/show/elliptic+curve}（Last revised 2025-05-11；2026-11-14 访问）。]}',
     '即曲线非奇异。[来源：J. H. Silverman, \\textit{The arithmetic of elliptic curves}, 2nd ed., GTM 106, 第 III 章（本讲参考文献 [S]）；并见 nLab "elliptic curve"，\\url{https://ncatlab.org/nlab/show/elliptic+curve}（Last revised 2025-05-11；2026-11-14 访问）。]}'),
    ('Tate 猜想（Faltings 1983 对 Abel 簇证明）断言：两个 Abel 簇之间的同源，恰由它们 Tate 模上 Galois 表示之间的同构给出，可见这个构造不会丢掉几何信息。[来源：nLab "Tate module"，\\url{https://ncatlab.org/nlab/show/Tate+module}（Last revised 2014-09-16；2026-11-14 访问）。]}',
     'Tate 猜想（Faltings 1983 对 Abel 簇证明）断言：两个 Abel 簇之间的同源，恰由它们 Tate 模上 Galois 表示之间的同构给出，可见这个构造不会丢掉几何信息。[来源：J. H. Silverman, \\textit{The arithmetic of elliptic curves}, 2nd ed., GTM 106, 第 III 章与第 VII 章（本讲参考文献 [S]）。]}'),
])

# 3: L19 —— 带状球函数改引 Satake 1963（本讲 [S]）
rw('lecture19.tex', [
    ('[来源：nLab "spherical function"，\\url{https://ncatlab.org/nlab/show/spherical+function}（Last revised 2024-08-07；2026-11-14 访问）。]}',
     "[来源：I. Satake, \\textit{Theory of spherical functions on reductive algebraic groups over $p$-adic fields}, Publ. Math. IHÉS 18 (1963) 5--69，第 1--2 节（本讲参考文献 [S]）。]}"),
])

# 4: L23 —— 删掉超出书目的 \S2.2
rw('lecture23.tex', [
    ('[来源：Juteau--Mautner--Williamson, \\textit{Parity sheaves}, \\S2.2（本讲参考文献）。]}',
     '[来源：Juteau--Mautner--Williamson, \\textit{Parity sheaves}, J. Amer. Math. Soc. 27 (2014) 1169--1212（本讲参考文献）。]}'),
])
print('done')
