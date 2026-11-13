# 源片段 tr02b（底本：Lagrangian Torus Fibrations）


<<B086 h3>>
## Equivalences.

<<B087 p>>
Lagrangian fibrations are extra structures imposed on a given symplectic manifold $(M,\omega)$, and we want to understand also when two such fibrations are equivalent.

<<B088 env>>
[ENV] **Definition.** Two regular Lagrangian fibrations $\pi\colon M\to B$ and $\pi'\colon M'\to B'$ are _isomorphic_ if there exists a fibered symplectomorphism $\Phi\colon M\to M'$ lying over a diffeomorphism $\phi\colon B\to B'$, i.e. $\Phi$ is a symplectomorphism together with the commutative diagram

<<B089 quiver>>
[QUIVER] https://q.uiver.app/#q=WzAsNCxbMCwwLCJNIl0sWzEsMCwiTSciXSxbMCwxLCJCIl0sWzEsMSwiQiciXSxbMCwxLCJcXFBoaSJdLFswLDIsIlxccGkiLDJdLFsyLDMsIlxccGhpIiwyXSxbMSwzLCJcXHBpJyJdXQ==&embed

<<B090 env>>
[ENV] **Exercise.** It's not hard to show that $\phi$ has to be an isomorphism of integral affine manifolds.

<<B091 p>>
We are ready to prove a "reconstruction theorem" for regular Lagrangian fibrations similar to Theorem [1.1].

<<B092 env>>
[ENV] **Theorem.** Let $M\xrightarrow{\pi} B$, $M'\xrightarrow{\pi'} B$ be two regular Lagrangian fibrations equipped with global Lagrangian sections $\sigma$ and $\sigma'$ respectively. Then there is a unique fibered symplectomorphism $\Phi\colon M\to M'$ such that the diagram

<<B093 quiver>>
[QUIVER] https://q.uiver.app/#q=WzAsMyxbMCwwLCJNIl0sWzEsMSwiQiJdLFsyLDAsIk0nIl0sWzAsMiwiXFxQaGkiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkb3R0ZWQifX19XSxbMCwxLCJcXHBpIiwwLHsiY3VydmUiOi0xfV0sWzIsMSwiXFxwaSciLDIseyJjdXJ2ZSI6MX1dLFsxLDAsIlxcc2lnbWEiLDAseyJjdXJ2ZSI6LTF9XSxbMSwyLCJcXHNpZ21hJyIsMix7ImN1cnZlIjoxfV1d&embed

<<B094 p>>
commutes.

<<B095 prf>>
[PRF] **Proof.** Construct $\Phi$ using Liouville coordinates.

<<B096 p>>
In fact, under these assumptions we can understand the space $M$ explicitly: the integral affine structure on $B$ induces a locally free sheaf of lattices $\Lambda$ in the cotangent bundle $T^{\ast} B$, and we can naturally form the symplectic manifold $T^{\ast} B/\Lambda$ where fibers of the projection $T^{\ast} B/\Lambda\to B$ are Lagrangian tori. Note that $T^{\ast} B/\Lambda\to B$ always has a global Lagrangian section provided by the zero section, and therefore reconstruction theorem [2.20] applies to yield that $M$ is fibered symplectomorphic to $T^{\ast} B/\Lambda$.

<<B097 env>>
[ENV] **Example.** When $M\to B$ does not admit a global Lagrangian section, the reconstruction theorem can fail, and here's an example from [[Eva23]]: consider the symplectic vector space $\mathbb{R}^4$ with coordinates $(t,x,y,z)$ and symplectic structure $dt\wedge dx+dy\wedge dz$. The $\mathbb{Z}^3$-action $(a,b,c)\cdot (t,x,y,z)=(t,x+a,y+b,z+c)$ preserves the symplectic structure, and hence we get a symplectic manifold $\mathbb{R}\times\mathbb{T}^3$ by quotient out this $\mathbb{Z}^3$-action. Now consider a further $\mathbb{Z}$-action on $\mathbb{R}\times\mathbb{T}^3$ by $1\cdot (t,x,y,z)=(t+1,x,y,x+y+z)$, which also preserves the symplectic structure, and we get a symplectic manifold $(K,\omega)$ by quotienting out this $\mathbb{Z}$-action. This is the famous _Kodaira-Thurston manifold_ which is a compact symplectic manifold that does not admit any compatible complex structures (so that it becomes a Kähler manifold). Consider the projection $K\to\mathbb{T}^2$ by $(t,x,y,z)\mapsto (t,y)$. This is a (principal) regular Lagrangian torus fibration, and principal bundles admitting a global section are always trivial, meaning $K\cong\mathbb{T}^4$. However, we can compute that $b_1 (K)=3$ whereas $b_1 (\mathbb{T}^4)=4$, so $K\to\mathbb{T}^2$ does not admit any global Lagrangian sections. On the other hand, we can consider the standard torus $\mathbb{T}^4$ with the symplectic structure $dt\wedge dx+dy\wedge dz$ and the projection $\mathbb{T}^4\to\mathbb{T}^2$ by $(t,x,y,z)\mapsto (t,y)$, which induces the same integral affine structure on $\mathbb{T}^2$ as $K\to\mathbb{T}^2$. This shows that the reconstruction theorem can fail without the existence of global Lagrangian sections.


<<B098 h3>>
## Flux.

<<B099 p>>
Finally, there is a more geometric way of writing down the action-angle coordinates via computing certain period integrals. For given Lagrangian fibration $M\to B$, assume that $M$ is exact, i.e. $\omega =d\lambda$ for some $1$-form $\lambda$, we obtain a locally free sheaf $H_1 (F_b;\mathbb{Z})\to\mathcal{S}\to B$ which becomes trivial after pullback along the universal cover $p\colon\tilde{B}\to B$. Let $c_1,\dotsb, c_n$ be the trivializing sections of the pull-back bundle $p^{\ast}\mathcal{S}$.

<<B100 env>>
[ENV] **Definition.** We define the _flux map_ $I\colon\tilde{B}\to\mathbb{R}^n$ by the formula $$I(\tilde{b})=(I_1 (\tilde{b}),\dotsb, I_n (\tilde{b}))=\left(\frac{1}{2\pi}\int_{c_1 (\tilde{b})}\lambda,\dotsb, \frac{1}{2\pi}\int_{c_n (\tilde{b})}\lambda\right).$$

<<B101 p>>
This definition does not depend on the choice of the primitive $1$-form $\lambda$, as different choices differ by shifting by a constant which is the integral affine transformation, and also not on the choice of the basis $\{c_i\}$ for any choice differs by an element in $GL(n,\mathbb{Z})$, again absorbed into the integral affine structure.

<<B102 env>>
[ENV] **Lemma.** Let $\tilde{U}\xrightarrow{\cong} U$ be open subsets of $\tilde{B}$ and $B$ respectively, then the composition $I\circ\left(p\vert_{\tilde{U}}\right)^{-1}\colon U\to\mathbb{R}^n$ gives action coordinates in $U$.

<<B103 prf>>
[PRF] **Proof.** It suffices to check when $M=U\times\mathbb{T}^n$ with the standard action-angle symplectic structure. Then we can write $\lambda =\sum b_i dt_i$, and $I_i (b)=\displaystyle\frac{1}{2\pi}\int_{c_i} b_idt_i =b_i$ where $c_i$ is the standard basis.

<<B104 p>>
With the flux map $I\colon\tilde{B}\to\mathbb{R}^n$, we naturally obtain an integral affine structure on $\tilde{B}$ by pulling back the standard one on $\mathbb{R}^n$ via $I$. This integral affine structure then descends to $B$ and gives the same integral affine structure on $B$ coming from regular Lagrangian fibrations.
