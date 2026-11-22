import io
p = 'chunks/ch22.tex'
s = io.open(p, encoding='utf-8').read()

old = r"""	{\small
	\begin{align*}
	     \Vect &\simeq  \QCoh( \pt / \cG) \\
	     &\quad \underset {\Hom_{\TwoIC(\LS)}(
	     \QCoh(\pt / \cG), \QCoh(\pt / \cG))} \otimes \Hom_{\TwoIC(\LS)}(
	     \QCoh(\pt /
	     \cG), \QCoh(\pt)) \\ &\simeq
	     \QCoh( \pt / \cG) \underset {\ICn(\pt / \cG \underset \LS \times \pt /
	     \cG)} \otimes \ICn( \pt \underset \LS \times \pt ).
	\end{align*}}"""
new = r"""	{\small
	\begin{align*}
	     \Vect &\simeq  \QCoh( \pt / \cG) \otimes_{\Hom_{\TwoIC(\LS)}(
	     \QCoh(\pt / \cG), \QCoh(\pt / \cG))} \Hom_{\TwoIC(\LS)}(
	     \QCoh(\pt /
	     \cG), \QCoh(\pt)) \\ &\simeq
	     \QCoh( \pt / \cG) \otimes_{\ICn(\pt / \cG \underset \LS \times \pt /
	     \cG)} \ICn( \pt \underset \LS \times \pt ).
	\end{align*}}"""
assert old in s, 'B'
s = s.replace(old, new)
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
