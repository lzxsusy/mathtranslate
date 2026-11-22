import io
p = 'chunks/ch22.tex'
s = io.open(p, encoding='utf-8').read()

a = '$p$-adic$$ 理论中一条更早、'
b = '$p$-adic 理论中一条更早、'
assert a in s, 'A'
s = s.replace(a, b)

old = r"""	\begin{align*}
	     \Vect &\simeq  \QCoh( \pt / \cG) \underset {\Hom_{\TwoIC(\LS)}(
	     \QCoh(\pt / \cG), \QCoh(\pt / \cG))} \otimes \Hom_{\TwoIC(\LS)}(
	     \QCoh(\pt /
	     \cG), \QCoh(\pt)) \\ &\simeq
	     \QCoh( \pt / \cG) \underset {\ICn(\pt / \cG \underset \LS \times \pt /
	     \cG)} \otimes \ICn( \pt \underset \LS \times \pt ).
	\end{align*}"""
new = r"""	{\small
	\begin{align*}
	     \Vect &\simeq  \QCoh( \pt / \cG) \\
	     &\quad \underset {\Hom_{\TwoIC(\LS)}(
	     \QCoh(\pt / \cG), \QCoh(\pt / \cG))} \otimes \Hom_{\TwoIC(\LS)}(
	     \QCoh(\pt /
	     \cG), \QCoh(\pt)) \\ &\simeq
	     \QCoh( \pt / \cG) \underset {\ICn(\pt / \cG \underset \LS \times \pt /
	     \cG)} \otimes \ICn( \pt \underset \LS \times \pt ).
	\end{align*}}"""
assert old in s, 'B'
s = s.replace(old, new)
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
