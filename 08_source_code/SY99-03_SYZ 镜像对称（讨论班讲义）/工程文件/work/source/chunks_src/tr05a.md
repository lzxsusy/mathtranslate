# 源片段 tr05a（底本：Focus-focus Singularities and Almost Toric Fibrations）

<<B155 p>>
Outline: We will start with Lagrangian fibrations with singularities. Generically there'll be only non-degenerate singularities, which have good classification results. Focus-focus singularities form a special type of non-degenerate ones, which have semi-global invariants and monodromy, and have nodal integral affine structures. Similar to toric varieties, with possible toric singularities, we get almost toric fibrations, whose total space is reconstructible from the base.

<<B156 env>>
[ENV] **Definition.** Let $\vec{H}\colon (M^{2n},\omega)$ be a completely integrable Hamiltonian system. A _singular point_ $x\in M$ is _non-degenerate_ if the quadratic parts of degenerate Hamiltonians at $x$ form a Cartan subalgebra under Poisson bracket.

<<B157 li>>
- When $x$ is a fixed point, $\mathrm{rk}\ \vec{H}=0$, the Cartan subalgebra is the total Lie algebra $$Q=\{\text{all quadratic }H\text{ on }(\mathbb{R}^{2n},\omega)\};$$

<<B158 li>>
- When $0<\mathrm{rk}\ \vec{H}=m < n$, assume that $dH_1\wedge\dotsb\wedge dH_m (x)\neq 0$, then we can quotient the system by $\mathbb{R}^m$-action to get a reduced system where we go back to ①.

<<B159 p>>
The _Cartan subalgebra_ is a maximal nilpotent and self-normalizing subalgebra of $C^{\infty} (M,\mathbb{R})$, and if we write $\{q_1,\dotsb, q_k\}$ to be the quadratic part of the Hamiltonian functions $\{H_1,\dotsb, H_k\}$, then they should be

<<B160 li>>
- Poisson-commute.

<<B161 li>>
- Each $q_i$ is diagonalizable over $\mathbb{C}$.

<<B162 li>>
- Maximal.

<<B163 p>>
The corresponding linear Hamiltonian matrices $A_1,\dotsb, A_k$, where $A_i=\begin{pmatrix}0&I\\-I&0\end{pmatrix}\mathrm{Hess}\ H_i$, and their generic linear combinations over $\mathbb{R}$, $c_1A_1+\dotsb+c_kA_k$, have $k_e$ pairs of purely imaginary eigenvalues, $k_h$ real eigenvalues and $k_f$ quadruples of others. We call this singularity has _Williamson type_ $(k_e, k_f, k_h)$. ($k_e+k_f+k_h=n-m=k$)

<<B164 table>>
|  | Component type | Linear model |
| $k_e$ | elliptic | $H=x^2+y^2$ |
| $k_h$ | hyperbolic | $H=xy$ |
| $k_f$ | focus-focus | $\left\{\begin{array}{l}H_1=x_1y_2-x_2y_1\\H_2=x_1y_1+x_2y_2\end{array}\right.$ |

<<B165 p>>
Toric singularities are all of elliptic type.


<<B166 h3>>
## Standard focus-focus singularity.

<<B167 p>>
We can rewrite the linear model for focus-focus singularities as follows: regard $(\mathbb{R}^4,\omega)$ as a complex vector space $\mathbb{C}^2$ where $\omega =dp\wedge d\bar{p}+dq\wedge d\bar{q}$, then we can write $H=-\bar{p}q$. The corresponding Hamiltonian flow can then be described as$$\left\{\begin{array}{l}\phi_{H_1}^t (p,q)=(e^tp,e^{-t}q)\\\pi_{H_2}^t (p,q)=(e^{it}p,e^{it}q)\end{array}\right.$$Orbits of $H_1$ is then the origin $\{0\}$, the $\vert p\vert$-plane, the $\vert q\vert$-plane, and all the preimages of the hyperbolic trajectories depicted in the following picture, under the map $(\vert p\vert, \vert q\vert)$. Orbits of $H_1$.

<<B168 env>>
[ENV] **Definition.** A map $\pi\colon (M^4,\omega)\to B^2$ has a _focus-focus singularity_ at $x$ if there exists local Darboux chart at $x$ that resembles the FF system.

<<B169 env>>
[ENV] **Proposition.** The singular fiber of a Lagrangian fibration with only one singularity of focus-focus type is homeomorphic to a once-pinched torus.

<<B170 prf>>
[PRF] **Proof.** We have $\pi^{-1} (b)=\{x\}\cup\Omega_1\cup\dotsb\cup\Omega_k$ as Hamiltonian orbits, where $\Omega_i$ has dimension $2$, so the only possibilities for each $\Omega_i$ are $\mathbb{R}^2$, $\mathbb{R}\times\mathbb{S}^1$ or $\mathbb{T}^2$. As $\pi^{-1} (b)$ is compact and connected, $\mathbb{T}^2$ is not possible, so either $\Omega_i\cong\mathbb{R}^2$ or $\Omega_i\cong\mathbb{R}\times\mathbb{S}^1$. Let $\Omega_p$ be the orbit of the $\vert p\vert$-plane and $\Omega_q$ be the orbit of the $\vert q\vert$-plane, then from the local chart it's clear that $\Omega_p,\Omega_q\cong\mathbb{R}\times\mathbb{S}^1$. These are the only orbits entering the focus-focus chart, so we must have $\pi^{-1} (b)=\Omega_p\cup\{x\}\cup\Omega_q$. As $\overline{\Omega_p\cup\{x\}\cup\Omega_q}$ is compact, we must have $\Omega_p=\Omega_q$, and therefore $\pi^{-1} (b)$ is homeomorphic to a once-pinched torus.

<<B171 env>>
[ENV] **Theorem.** The action map $\tilde{B}\to\mathbb{R}^2$ has the form$$\left(\frac{1}{2\pi}(S(b)+b_2\theta -b_1 (\ln r-1)),b_2\right)$$where $b=b_1+ib_2=re^{i\theta}$ is a local coordinate on $B$ and $S(b)$ is some smooth function.

<<B172 p>>
For fixed $b$, set $\sigma_1(b)=(-\bar{b},1)$ and $\sigma_2 (b)=(-1,b)$ be two smooth points in the singular fiber of the FF system, lying on the $\vert p\vert$- and $\vert q\vert$-planes, resp.. Let $\vec{T}$ be the time for the Hamiltonian flow from $\sigma_1$ to $\sigma_2$, then $T=(T_1,T_2)$ where $T_1(b)=\ln (b)$ and $T_2 (b)=\arg b$. We write them as $S_1 (b)$ and $S_2 (b)$. Now let $\sigma_1, \sigma_2$ be two given Lagrangian sections avoiding the singular point, then we can compute that $\displaystyle\frac{\partial S_1}{\partial b_2}=\frac{\partial S_2}{\partial b_1}$, and hence there exists a globally defined function $S\colon B\to\mathbb{R}$ such that $\partial_1 S=S_1$ and $\partial_2 S=S_2$. Therefore we can compute out the action map from periods.

<<B173 p>>
In fact, germs of such function $(S)_{\infty}$ near the nodal singularity classifies the FF neighbourhood [[Ngoc03]], and any such $S$ can be realized as a Hamiltonian system, so that we can obtain a manifold $X_S$ and a Hamiltonian system $X_S\xrightarrow{\vec{H}}\mathbb{R}^2$ from $\partial_1 S$ and $\partial_2 S$.

<<B174 env>>
[ENV] **Theorem[[Sym03]].** Given two action functions $S_1$ and $S_2$ of the FF system, there exists a symplectomorphism $X_{S_0}\to X_{S_1}$ thta restricts to a fibered one outside of a neighbourhood of a singular fiber.
