# 源片段 tr05b（底本：Focus-focus Singularities and Almost Toric Fibrations）


<<B175 h3>>
## Monodromy.

<<B176 p>>
Now we work on the opposite direction: given a Lagrangian torus fibration $X^{\circ}\to B\setminus\{b\}$ which induces an integral affine structure on $B\setminus\{b\}$. Can we extend $X^{\circ}$ to a Lagrangian torus fibration on $B$, possibly with singularities, equivalently extending the integral affine structure from $B\setminus\{b\}$ to $B$?

<<B177 env>>
[ENV] **Topological monodromy on torus bundle.** Recall that if $\mathbb{T}^n\to M\xrightarrow{\pi} B$ is a topological torus bundle, then there is an induced fundamental group action $\Phi\colon\pi_1 (B,b)\to\mathcal{M} (\mathbb{T}^n)\to\mathrm{Aut} (H_1 (F_b;\mathbb{R}))\cong GL(n,\mathbb{Z})$, called the _topological monodromy_.

<<B178 env>>
[ENV] **Affine monodromy.** Lagrangian torus fibration over $B$ is equivalent to lattice fibration $\Lambda\to B$, and hence the monodromy action of $\pi_1 (B,b)$ must preserve the lattice $\Lambda_b$. Therefore we have the monodromy action $\Psi_B\colon\pi_1 (B,b)\to\mathrm{Aut} (\Lambda_b)\cong\mathrm{Aff} (n,\mathbb{Z})$ where $\gamma\mapsto\gamma^{\ast} (TB,\Lambda)\cong I\times (\mathbb{R}^n,\mathbb{Z}^n)\big/\left((0,p)\sim (1,\psi_B [\gamma](p))\right)$.

<<B179 env>>
[ENV] **Theorem.** Let $\pi\colon (M,\omega)\to B$ be a Lagrangian torus fibration with topological monodromy matrix $A$, then the corresponding affine monodromy matrix is given by $\left(A^{-1}\right)^T$.

<<B180 env>>
[ENV] **Theorem.** The affine monodromy for symplectic $A_1$-singularity is $\begin{pmatrix}1&1\\0&1\end{pmatrix}$, and $\begin{pmatrix}1&k\\0&1\end{pmatrix}$ for $A_k$.

<<B181 env>>
[ENV] **Nodal integral affine structure.** Consider local charts $U_1=\mathbb{R}^2\setminus\{(x,y)\vert y=0, x\geq 0\}$ and $U_2=(0,\infty)\times (-\varepsilon,\varepsilon)\subseteq\mathbb{R}^2$ with transition map given by $$\phi (x,y)=\left\{\begin{array}{ll} \begin{pmatrix}1&-1\\0&1\end{pmatrix}(x,y),&y>0;\\ (x,y),&y<0. \end{array}\right.$$Then we obtain a topological manifold $B$ homeomorphic to $\mathbb{R}^2$ together with an integral affine structure on $B\setminus\{0\}$.

<<B182 p>>
For $\mathbb{T}^n$ acting hamiltonianly effectively on a symplectic manifold $(M,\omega)$, its moment map $\mu_{\mathbb{T}^n}$ has image a convex polytope. This can be generalized as follows: assume that $M$ is non-compact or with boundary, then we can decompose $\mu$ as $\mu=\Phi\circ\pi$, where $\pi\colon M\to B$ is the orbit space fibration and $\Phi\colon B\to\mathbb{R}^n$ an affine immersion. The work of Symington [[Sym03]] showed that the torus fibration can be encoded in a triple $(B,\mathcal{A},\mathcal{S})$, where $\mathcal{S}$ is a stratification of $B$, called _toric base_, together with some compatibility conditions.

<<B183 env>>
[ENV] **Theorem.** For a toric base of dimension $n$, there exists a unique symplectic manifold $(M,\omega)$ equipped with a unique Lagrangian fibration on it.

<<B184 p>>
Roughly speaking, this can be proven by considering the trivial fibration $(B\times\mathbb{T}^n,\omega)\to B$, taking boundary reductions and finally ending up with a smooth manifold.


<<B185 h3>>
## Almost toric manifolds.

<<B186 p>>
Almost toric manifolds are symplectic manifolds equipped with Lagrangian torus fibrations with only elliptic and focus-focus type singularities. In dimension $4$, such manifolds readily give rise to an almost toric base $(B,\mathcal{A},\mathcal{S})$ together with a discrete set of points $\{b_i\in B^{top}\}$ where locally at each $b_i$ we get a nodal integral affine manifold and each $b\in B\setminus\{b_i\}$ is locally toric.

<<B187 p>>
The inclusions $(B\setminus\{b_i\},\mathcal{A})\to (\mathbb{R}^4,\mathcal{A}_0)$ is NOT an affine immersion, but we can get an affineimmersion by cutting through aneigenvalue. When the base is non-compact or without boundary, the symplectic manifold is uniquely determined, but otherwise uniqueness is no longer true. In this sense, we get classifications of $4$-dimensional almost toric fibrations up to diffeomorphisms. For instance, as discussed in [[LS03]]:

<<B188 table>>
| Base | # nodes | Total space |
| $\mathbb{D}^2$ | $n$ | $\mathbb{C}P^2\#(n+k-3)\overline{\mathbb{C}P^2}$ or $\mathbb{S}^1\times\mathbb{S}^3$, $k=\#\text{vertices}$ |
| $\mathbb{S}^2$ | $24$ | K3 surfaces |
