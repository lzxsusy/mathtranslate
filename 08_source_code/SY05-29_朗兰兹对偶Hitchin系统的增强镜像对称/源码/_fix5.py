# -*- coding: utf-8 -*-
import io

P5 = "\\origpage{2235}下面这些考察的原初动机，是要找到一种办法来检验 \\cite{baraglia-schaposnik,garcia-prada-etal,hitchin-characteristic} 所提出的 $(B,A,A)$ 型与 $(B,B,B)$ 型膜的猜想镜像对。迄今为止唯一的检验——常常就在这些文献中完成——是检查所提议的镜像对相对于 Hitchin 映射是否确实互为 Fourier--Mukai 对偶。而这种检验只能在 Hitchin 底上的\\emph{一般}点处进行。我们希望看到更多整体性的检验，特别是那些能在 Hitchin 映射的 $0$-纤维，即整体幂零锥上验证镜像对称提议的检验。\n\n"

fn = "ch3_enhanced.tex"
s = io.open(fn, encoding="utf-8").read()
anchor = "\\label{enhanced}\n\n\n"
if anchor not in s:
    print("no anchor, trying single blank")
    anchor = "\\label{enhanced}\n\n"
assert anchor in s, "anchor missing"
s = s.replace(anchor, "\\label{enhanced}\n\n" + P5, 1)
io.open(fn, "w", encoding="utf-8", newline="\n").write(s)
print("inserted P5")
