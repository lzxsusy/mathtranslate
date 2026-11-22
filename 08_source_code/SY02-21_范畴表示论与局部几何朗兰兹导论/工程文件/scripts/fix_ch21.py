import io
p = 'chunks/ch21.tex'
s = io.open(p, encoding='utf-8').read()

a = '「重数自由 ↔ 自同态代数交换」\n对应之下。'
b = '「重数自由」与「自同态代数交换」的通常对应之下。'
assert a in s, 'A missing'
s = s.replace(a, b)

old = r"""\begin{align*} \QCoh( \widetilde{\sN}^\wedge / \cG  \underset {\cfg / \cG}
\times
\widetilde{\sN}^\wedge / \cG)
& \simeq \QCoh(\widetilde{\sN}^\wedge / \cG)  \underset {\QCoh(\sN^\wedge / \cG)}
\otimes  \QCoh(\widetilde{\sN}^\wedge / \cG ) \\ & \simeq \Dmod(\mathring{I}
\backslash LG / \mathring{I}, \psi, \on{s}) \underset {\Dmod(\mathring{I},
\psi, \on{s} \backslash LG / \mathring{I}, \psi, \on{s})} \otimes
\Dmod(\mathring{I}, \psi, \on{s} \backslash LG / \mathring{I}).  \end{align*}"""
new = r"""{\small
\begin{align*} &\QCoh( \widetilde{\sN}^\wedge / \cG  \underset {\cfg / \cG}
\times
\widetilde{\sN}^\wedge / \cG) \\
&\qquad \simeq \QCoh(\widetilde{\sN}^\wedge / \cG)  \underset {\QCoh(\sN^\wedge / \cG)}
\otimes  \QCoh(\widetilde{\sN}^\wedge / \cG ) \\ &\qquad \simeq \Dmod(\mathring{I}
\backslash LG / \mathring{I}, \psi, \on{s}) \underset {\Dmod(\mathring{I},
\psi, \on{s} \backslash LG / \mathring{I}, \psi, \on{s})} \otimes
\Dmod(\mathring{I}, \psi, \on{s} \backslash LG / \mathring{I}).  \end{align*}}"""
assert old in s, 'B missing'
s = s.replace(old, new)
io.open(p, 'w', encoding='utf-8').write(s)
print('ok')
