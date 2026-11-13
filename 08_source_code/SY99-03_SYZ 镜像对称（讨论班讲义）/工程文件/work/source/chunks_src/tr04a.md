# 源片段 tr04a（底本：SYZ Mirror Symmetry for Toric Fano Varieties）


<<B132 h3>>
## SYZ mirror construction for toric Fano varieties.

<<B133 p>>
With the confirmation of Homological Mirror Symmetry on the other side, we can move forward to the SYZ mirror construction for toric Fano varieties. As explained in the previous section, compactifying $\left(\mathbb{C}^{\ast}\right)^n$ would result in deformation of all the Floer $A_{\infty}$-algebras on Lagrangian tori, and the task in this section is to understand the effect of this $A_{\infty}$-deformation.

<<B134 p>>
The first result is that for toric compactifications, Maslov indices of pseudo-holomorphic disks are well-understood:

<<B135 env>>
[ENV] **Proposition(Cho-Oh '06).** Let $X_{\Sigma}$ be a toric Fano manifold with toric boundary divisor $D=\displaystyle\bigcup_i D_i$ where each $D_i$ are the irreducible components, then for any pseudo-holomorphic disk $u\colon (D^2,\partial D^2)\to (X_{\Sigma},L_b)$ with boundary on a Lagrangian torus $L_b\subseteq\left(\mathbb{C}^{\ast}\right)^n$, its Maslov index is given by $$\mu (u)=2\sum_i (u\cdot D_i),$$where $u\cdot D_i$ is the intersection number of $u$ with the divisor $D_i$.

<<B136 prf>>
[PRF] **Proof.** Note that computation of Maslov indices is a purely topological problem, up to smooth isotopy only the intersection points of the image of $u$ with $D$ would contribute to the Maslov index, and therefore we can consider the simplest model where there is a disk $\mathbb{D}^2\subseteq\mathcal{N}_X\left(\bigcap_{i\in I} D_i\right)$ intersecting with $D_I\colon =\displaystyle\bigcap_{i\in I} D_i$ at the origin of multiplicity $\ell$ and with boundary on the torus bundle over $D_I$. For this local model we know that $D_I$ can be written as $\displaystyle\left\{\prod_{i\in I}z_i=0\right\}$, and we can compute directly (see for example appendix D of [[MS04]]) and verify that the Maslov index of such is $2\ell\vert I\vert$.

<<B137 p>>
In particular, there exists pseudo-holomorphic disks of Maslov index $2$ that contributes to the curvature term $\mathfrak{m}^0$ of the $A_{\infty}$-structure, potentially obstructing Floer cohomologies of Lagrangian tori to be well-defined. To compute this term, we need classifications of these pseudo-holomorphic disks. This is the following main theorem of [[CO06]]:

<<B138 env>>
[ENV] **Theorem(Cho-Oh '06).** Let $\tilde{L}\subseteq\mathbb{C}^N\setminus Z(\Sigma)$ be a fixed orbit of the real $N$-torus $\mathbb{T}^N$. Any holomorphic map $u\colon (\mathbb{D}^2,\partial\mathbb{D}^2)\to (X_{\Sigma},L)$ can be lifted to a holomorphic map $$\tilde{u}\colon (\mathbb{D}^2,\partial\mathbb{D}^2)\to (\mathbb{C}^N\setminus Z(\Sigma),\tilde{L})$$ such that each homogeneous coordinate function $z_1 (\tilde{u}),\dotsb, z_N (\tilde{u})$ is given by a Blaschke product with constant factors, i.e. $$z_i (\tilde{u})=c_i\cdot\prod_{j=1}^{\mu_i}\frac{z-\alpha_{i,j}}{1-\bar{\alpha}_{i,j} z}$$ for $c_i\in\mathbb{C}^{\ast}$, $\mu_i\in\mathbb{Z}_{>0}$ and $\alpha_{i,j}\in\operatorname{Int} (D^2)$. Any two such lifts are related by $\tilde{u}'=t\cdot\tilde{u}$ for some $t\in T(\Sigma)$ a constant element.

<<B139 p>>
In particular, the numbers $\mu_i$ are intersection multiplicities of the pseudo-holomorphic disk $u(\mathbb{D}^2)$ with the toric boundary component $D_i$. Using this classification, we can completely compute contributions of the pseudo-holomorphic disks with arbitrary Maslov indices to $\mathfrak{m}^0$.
