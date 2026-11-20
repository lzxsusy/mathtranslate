# -*- coding: utf-8 -*-
import io, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '源码'))

def edit(path, pairs):
    s = io.open(path, encoding='utf-8').read()
    for old, new in pairs:
        assert old in s, (path, old[:40])
        s = s.replace(old, new, 1)
    io.open(path, 'w', encoding='utf-8').write(s)

H1 = r'\subsection{环簇情形：加上 $w_V$}'
H1n = r'\subsection{\texorpdfstring{环簇情形：加上 $w_V$}{环簇情形：加上 w\_V}}'
H2 = r'\subsection{加 $w_V$ 之后：不卷绕的版本}'
H2n = r'\subsection{\texorpdfstring{加 $w_V$ 之后：不卷绕的版本}{加 w\_V 之后：不卷绕的版本}}'
H3 = r'\subsection{函子 $U$、$\cap$、$\mu$ 与 $S$}'
H3n = r'\subsection{\texorpdfstring{函子 $U$、$\cap$、$\mu$ 与 $S$}{函子 U、cap、mu 与 S}}'
H4 = r'\subsection{$A_{\mathrm{model}}$ 数据、B 侧解释与 $F$ 的对象}'
H4n = r'\subsection{\texorpdfstring{$A_{\mathrm{model}}$ 数据、B 侧解释与 $F$ 的对象}{A-model 数据、B 侧解释与 F 的对象}}'
H5 = r'\subsection{$\mu^2$ 的传播}'
H5n = r'\subsection{\texorpdfstring{$\mu^2$ 的传播}{mu\^2 的传播}}'

N1 = ('% [Tutor Note: 易错] 加上 $w_V$ 之后，"卷绕"的方向变了：紧化引入的单项式使部分拉格朗日沿纤维方向被推向无穷，'
      '而 $w_0$ 与 $w_V$ 中出现的单项式只在小范围内变动。若把两者一并卷绕，得到的范畴会失去 $\\db\\Coh(H)$ 的有限性。'
      '来源：原书第 2 页与第 3 页的对照。')
N2 = ('% [Tutor Note: 直觉] 单项式容许性说的是：$L$ 在无穷远处只沿少数"许可方向"伸展，从而 $\\arg z^\\nu$ 在这些方向上局部常值。'
      '这是把非紧的 $Y$ 上"卷绕"这个概念变得可数的唯一办法——许可的单项式越少，可卷绕的方向越少，$\\hom$ 越像有限维。'
      '来源：原书第 3 页对象定义三条。')
N3 = ('% [Tutor Note: 易错] $U$ 与 $\\cap$ 只是一对伴随函子，并不是互逆等价：$U$ 把 $F$ 中的拉格朗日沿 U 形弧平行移动，搬到 $Y$ 中；'
      '$\\cap$ 则取 $L$ 在无穷远处的"端点"。正因如此才有非平凡的正合三角 $\\mu^{-1}\\xrightarrow{S}\\id\\to\\cap U$，而不是等号。'
      '来源：原书第 6 页函子表与正合三角。')
N4 = ('% [Tutor Note: 易错] 光滑化参数是 $T^A$ 而不是 $T^{A/2}$，但半粘合的两式右端都是 $T^{A/2}$：一条 $\\PP^1$ 的面积为 $A$，'
      '而它在每个结点处只贡献一半。写错这个指数，$p_1p_2p_3=1$ 就不再成立。来源：原书第 13 页 $yy\'=T^A$ 与 $xy\'=T^{A/2}$ 两式。')
N5 = ('% [Tutor Note: 点拨] 传播的重数就是幂级数展开的系数，而不是 $1$：一条带在顶点处分叉成若干支，每支各得一个系数，'
      '乘起来才是这条带的权重。这也解释了为什么传播规则完全由"图卡数据"决定，与面积无关。来源：原书第 17 页两个重数公式。')

edit('ch1_talk1.tex', [
    (H1, N1 + '\n' + H1n),
    (r'\subsection{单项式容许与 wrapped Fukaya 范畴}', N2 + '\n' + r'\subsection{单项式容许与 wrapped Fukaya 范畴}'),
])
edit('ch2_talk2.tex', [
    (H2, H2n),
    (H3, N3 + '\n' + H3n),
])
edit('ch3_talk3.tex', [
    (H4, N4 + '\n' + H4n),
    (H5, N5 + '\n' + H5n),
])
print('done')
