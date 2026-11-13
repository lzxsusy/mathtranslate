# 源片段 tr03a（底本：SYZ Mirror Symmetry for Toric Fano Varieties）

<<B105 p>>
In this talk we will discuss the first type of non-regular singularities of Lagrangian fibrations, which we call _toric singularities_. These are good singularities in that the torus action from the Lagrangian torus fibration extends to the singular fibers, where the stabilization groups are non-trivial. One of the simplest case is the so-called _toric varieties_, where the regular stratum of the base $B$ is $\mathbb{R}^n$, and we will quickly see that the singular stratum form a polyhedral complex partially compactifying $\mathbb{R}^n$.


<<B106 h3>>
## Symplectic toric varieties.

<<B107 p>>
In this section, we will recall the definition of toric varieties, in a symplectic way, in order to keep track of the symplectic(Kähler) structures.

<<B108 env>>
[ENV] **Definition.** A _symplectic toric manifold_ $(M,\omega)$ is a symplectic manifold together with a hamiltonian $\mathbb{T}^n$-action.

<<B109 p>>
A hamiltonian $G$-action on $M$ induces a map of Lie algebras $\rho\colon\mathfrak{g}\to C^{\infty} (M)/\mathbb{R}$, equivalently a map $\mu_G\colon M\to\mathfrak{g}^{\ast}$ up to translation in $\mathfrak{g}^{\ast}$ where $\mu_G(x)(X):=\rho (X)(x)$, called the _moment map_ of $G$. When $G=\mathbb{T}^n$ is a torus, the theorem of Atiyah-Guillemin-Sternberg [[Ati82],[GS82]] states that

<<B110 env>>
[ENV] **Theorem(Atiyah-Guillemin-Sternberg).** The image of $\mu_G\colon M\to\mathfrak{g}^{\ast}$ is a convex polytope.

<<B111 p>>
We call the image of the moment map _the moment polytope_ of the toric symplectic manifold $M$. Let $\Sigma$ be the polytope in $\mathfrak{g}^{\ast}$, it naturally admits a stratification by facets. There is only one top-dimensional facet $\Sigma^{\circ}$ corresponding to values of $\mu_G$ where $T^n$ acts freely transitively on the fiber, which are Lagrangian tori in $M$. Lower dimensional facets correspond to values of $\mu_G$ where $T^n$ acts with stabilizer subgroups of rank equal to the codimension of the corresponding facet. They're naturally isotropic tori obstructing the fibration being regular.

<<B112 env>>
[ENV] Moment polytope for $\mathbb{P}^2$. **Examples.** Let's illustrate how to read off the geometric information of toric varieties from moment polytope via a simple example. Consider the symplectic vector space $\mathbb{C}^3=\mathbb{R}^6$ with the standard symplectic structure, with the standard linear action $T^3\curvearrowright\mathbb{C}^3$ by $(t_1, t_2, t_3).(x,y,z):=(t_1 x,t_2y,t_3z)$. $\mathbb{P}^2$ can be constructed as a _symplectic reduction_ of $\mathbb{R}^6$ by the diagonal torus action $(x,y,z)\mapsto (tx,ty,tz)$, with a choice of regular parameters $\lambda\in (0,\infty)\subseteq\mathfrak{t}=\operatorname{Lie} (\mathbb{T}^1)$. The moment map $\mu_{\mathbb{T}^3}$ can be written explicitly using standard basis as $$ \mu_{\mathbb{T}^3} (x,y,z)=\frac{1}{2} (|x|^2,|y|^2,|z|^2), $$so that using the first two coordinates we can write the induced moment map $\mu_{T}$ on $\mathbb{P}^2$ as $$ \mu_{T} ([x:y:z])=\left(\frac{|x|^2}{2},\frac{|y|^2}{2}\right). $$Clearly the image of $\mu_T$ is the triangle $\{t_1\leq\sqrt{\lambda},\ t_2\leq\sqrt{\lambda},\ t_1+t_2\leq\sqrt{\lambda}\}$ as depicted in figure [1]. The edge $\{t_1=0\}$ in the moment polytope corresponds to the divisor $\{x=0\}\subseteq\mathbb{P}^2$, where we can see that the action of the first circle is trivial. Similarly, the other two edges correspond to two other fixed divisors of $\mathbb{P}^2$. It's also easy to see that fibers over the vertices of the polytope are points, which are fixed points of the torus action.

<<B113 env>>
[ENV] **Remark.** Algebraic geometers are probably more familiar with the _fan description_, where an algebraic $\mathbb{G}_m^n$-action on a variety $X$ gives rise to a union of cones in $\mathbb{R}^n$, where the origin corresponds to the dense torus orbit, rays correspond to divisors, and higher dimensional cones correspond to higher codimensional toric subvarieties. These two pictures are more or less equivalent via the following combinatorial relation: for a given fan $\Sigma$ in $\mathbb{R}^n$, we can consider the polytope $$P=\{x\in\mathbb{R}^n\vert \langle x,v_i\rangle\geq -\lambda_i,\ v_i\text{ are generators of rays in }\Sigma\}$$for chosen vector $(\lambda_i)\in\mathbb{R}^n$. The choice of $(\lambda_i)$ then provides a symplectic structure on the toric variety $X$ that is compatible with the algebraic structure.

<<B114 p>>
Now we proceed to the Fanoness on toric varieties. Recall that a symplectic manifold is _monotone_ or _Fano_ if there exists a positive constant $\tau$ such that $[\omega]=\tau c_1 (X)$, where $c_1 (X)$ is the first Chern class of $X$. As $c_1 (X)$ is integral and algebro-geometrically it's equal to the sum of the representatives of all the toric divisors appearing on the boundary strata, the Fano condition can be read-off combinatorially as the following:

<<B115 env>>
[ENV] **Definition/Proposition(Batyrev).** A toric variety $X$ is Fano if and only if the standardized moment polytope $P$ associated to $X$ is _reflexive_. Let $\Sigma$ be the fan of $X$, and define $$P=\{x\in\mathbb{R}^n\vert \langle x,v_i\rangle\geq -1,\ v_i\text{ are generators of rays in }\Sigma\}$$to be the standardized moment polytope of $X$, then $P$ is _reflexive_ if its _polar dual_$$P^{\circ}=\{y\in\mathbb{R}^n\vert \langle x,y\rangle\geq -1,\ \forall x\in P\}$$is the convex hull of integral vectors.
