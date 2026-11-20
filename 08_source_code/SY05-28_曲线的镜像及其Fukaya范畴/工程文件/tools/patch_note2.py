# -*- coding: utf-8 -*-
import io, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '源码'))
p = 'app_invitation.tex'
s = io.open(p, encoding='utf-8').read()
anchor = r'\subsection*{第 7 页：例 1，$F^{\mathrm{wr}}\simeq\db$（Abouzaid--Seidel）}'
assert anchor in s
note = ('% [Tutor Note: 易错] 第 6 页与第 7 页的差别只在范畴的选择：紧拉格朗日里 $L_r$ 与 $L_{r\'}$ 不相交时 $\\hom=0$，'
        '所以只能靠 $L_r$ 里的局部系统 $\\xi$ 记录 $z$；换成 wrapped 之后，$L_0$ 可以沿 Reeb 方向卷绕，'
        '于是单个对象 $L_0$ 就承载了整个 $K[x^{\\pm1}]$。两条路线给出同一个 $\\db\\Coh(X^\\vee)$，但后者的生成性是一句话的事。'
        '来源：附录第 6、7、8 页。')
s = s.replace(anchor, anchor + '\n' + note, 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
