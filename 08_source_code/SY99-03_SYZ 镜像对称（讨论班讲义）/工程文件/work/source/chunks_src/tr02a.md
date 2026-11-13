# 源片段 tr02a（底本：Lagrangian Torus Fibrations）

<<B038 p>>
In this talk we will review some basic geometric facts concerning Lagrangian torus fibrations, particularly regular ones.


<<B039 h3>>
## Regular Lagrangian fibrations.

<<B040 p>>
Our goal of this talk is to establish the following properties of regular Lagrangian fibrations:

<<B041 li>>
- They're locally modelled on completely integrable hamiltonian systems;

<<B042 li>>
- Fibers of regular Lagrangian fibrations are Lagrangian tori;

<<B043 li>>
- Basis of regular Lagrangian fibrations carry integral affine structures.

<<B044 p>>
Let's start with the definition of Lagrangian fibrations.

<<B045 env>>
[ENV] **Definition.** A _stratification_ of a topological space $B$ is a filtration $$ \emptyset =B_{-1}\subseteq B_0\subseteq B_1\subseteq\dotsb\subseteq B_{d+1}\subseteq\dotsb\subseteq B $$where each $B_d$ is a closed subset s.t. $\forall d$, $S_d (B):= B_d\setminus B_{d-1}$ is a smooth manifold of dimension $d$ and $\displaystyle B=\bigcup_{d\geq 0} B_d$. $B$ is _finite dimensional_ if $S_d(B)=\emptyset$ for $d\gg 0$; $B$ is _$n$-dimensional_ if $B$ is finite dimensional and $n$ is the maximal number such that $S_n (B)\neq\emptyset$. In this case, $S_n(B)$ is called the _top stratum_.

<<B046 p>>
Now we are ready to give definitions on Lagrangian fibrations.

<<B047 env>>
[ENV] **Definition.** A _Lagrangian fibration_ is a map $(M^{2n},\omega)\xrightarrow{\pi} B^n$ so that

<<B048 li>>
- $(M^{2n},\omega)$ is a symplectic manifold and $B$ is an $n$-dimensional stratified space;

<<B049 li>>
- $\pi$ is proper and continuous;

<<B050 li>>
- Over the top stratum, $\pi$ is a smooth submersion with connected Lagrangian fibers. Other fibers are connected, stratified with isotropic strata.

<<B051 p>>
Write $B^{reg}:=S_n (B)$ be the top stratum, or _regular locus_ of $\pi$, and $B^{sing}=B\setminus B^{reg}$ the _discriminant locus_ of $\pi$, which has codimension $\geq 1$. By _regular/smooth_ Lagrangian fibration we mean $B=B^{reg}$, i.e. there're no lower-dimensional strata.


<<B052 h3>>
## Integrable hamiltonian systems.

<<B053 p>>
Historically Lagrangian fibrations arose from study of dynamical properties of classical hamiltonian systems. Hamiltonians are smooth functions defined on the phase space serving as an invariant for the system of motions, and the existence of hamiltonian functions allow us to "reduce the degrees of freedom" of the system, meaning that the particle has to move along level hypersurfaces defined by the hamiltonian function. In this section, we will describe systems of hamiltonian functions that allow us to inductively perform degree reduction, and show their connection to Lagrangian fibrations.

<<B054 env>>
[ENV] **Definition.** Let $(M^{2n},\omega)$ be a symplectic manifold. A function $\vec{H}=(H_1,\dotsb, H_k)\colon M\to\mathbb{R}^k$ is an _integrable hamiltonian system_ if

<<B055 li>>
- $H_i$s are _Poisson-commute_, i.e. $\{H_i, H_j\}=0$ for all $i,j$. ($\{H_i,H_j\}=\omega (X_{H_i}, X_{H_j})$)

<<B056 li>>
- $\vec{H}(X)$ contains an open and dense set of regular values in its closure.(i.e. $dH_1,\dotsb, dH_k$ are linearly independent)

<<B057 p>>
We say $\vec{H}$ is _completely integrable_ if $k=n$ and furthermore

<<B058 li>>
- $\vec{H}$ is proper with connected fiber.

<<B059 env>>
[ENV] **Proposition.** Hamiltonian flows of hamiltonian functions $H$ stay inside level sets $H^{-1} (c)$ of $H$.

<<B060 prf>>
[PRF] **Proof.** Let $\gamma(t)$ be the integral curve of $H$, then $\displaystyle\frac{d}{dt} H(\gamma(t))=dH(\dot{\gamma} (t))=dH(X_H(\gamma(t)))=0$.

<<B061 env>>
[ENV] **Proposition.** If $H,G$ are two hamiltonian functions that are Poisson-commute, then their hamiltonian flows commute.

<<B062 prf>>
[PRF] **Proof.** $\left[X_{H_i},X_{H_j}\right]=X_{\{H_i,H_j\}}=0$.

<<B063 p>>
Frobenius theorem immediately tells us that

<<B064 env>>
[ENV] **Corollary.** A completely integrable hamiltonian system $\vec{H}\colon M\to\mathbb{R}^n$ generates an $\mathbb{R}^n$-action on $M$.

<<B065 p>>
Let $c$ be a regular value of $\vec{H}$, then it's immediate from the definition of completely integrable hamiltonian system that $TH^{-1} (c)=\espan\left\{X_{H_1},\dotsb,X_{H_n}\right\}$ and $H^{-1} (c)$ is a Lagrangian orbit of the $\mathbb{R}^n$-action. Now choose a local section $\sigma\colon B\to M$ of $\pi$, where $B\subseteq\vec{H}(M)\subseteq\mathbb{R}^n$ is an open subset of regular values.

<<B066 env>>
[ENV] **Definition.** Given $\vec{H}\colon M\to\mathbb{R}^n$ completely integrable hamiltonian system and $\sigma\colon B\to M$ a local section, a _period lattice_ at $b\in B$ is the subset$$\Lambda_b^H :=\{t\in\mathbb{R}^n\vert \phi_H^t (\sigma (b))=\sigma (b)\}.$$We also define the _period lattice_ to be the $\mathbb{Z}$-local system $\Lambda^H =\{(b,t)\in B\times\mathbb{R}^n\vert t\in\Lambda_b^H\}$. It's called _standard_ if $\Lambda =B\times (2\pi\mathbb{Z})^n$.

<<B067 env>>
[ENV] **Theorem(Little Arnold-Liouville Theorem).** Let $\vec{H}\colon M\to\mathbb{R}^n$ be an integrable hamiltonian system on $M$. Let $\Omega (\sigma (b))$ be the orbit of $\sigma (b)$ under the $\mathbb{R}^n$-action, then $\Omega (\sigma (b))$ is diffeomorphic to $\displaystyle\left(\mathbb{R}^k/\mathbb{Z}^k\right)\times\mathbb{R}^{n-k}$ for some $k$, and it's a torus if $\Omega (\sigma (b))$ is compact.

<<B068 env>>
[ENV] **Exercise.** The Little Arnold-Liouville theorem assumes the existence of a local section $\sigma\colon B\to M$ for the integrable system $\vec{H}$, but we can actually show that such sections always exist locally. For instance, if $x\in M$ is a regular point of $\vec{H}$, then there always exists an open neighbourhood $U$ of $x$ where $\vec{H}(U)=B$ is open in $\mathbb{R}^n$ and a local Lagrangian section $\sigma\colon B\to U$ of $\vec{H}$ with $\sigma (\vec{H} (x))=x$.

<<B069 p>>
Locally near a Lagrangian section $\sigma\colon B\to M$, we can construct a map $\psi\colon B\times\mathbb{R}^n\to M$ by $\psi (b,t)=\phi_H^t (\sigma(b))$, which can be verified to be an immersion and submersion with $\psi^{\ast}\omega =\displaystyle\sum_{i=1}^n db_i\wedge dt_i$. This map is called the _Liouville coordinate_.

<<B070 env>>
[ENV] **Remark.** If $\sigma$ is only a local section, then such construction is still a local diffeomorphism but with $\psi^{\ast}\omega =\sum db_i\wedge dt_i +\beta$ for some closed $2$-form $\beta$. Only when $\sigma$ is Lagrangian we have $\beta=0$.

<<B071 env>>
[ENV] **Theorem(Action-Angle Coordinates).** Given $\vec{H}\colon M\to B\subseteq\mathbb{R}^n$ where $B$ is a disk of dimension $n$ with only regular fibers and a Lagrangian section $\sigma\colon B\to M$, there exists local change of coordinates $\alpha\colon B\to C\subseteq\mathbb{R}^n$ so that the period lattice for $a:=\alpha\circ\vec{H}\colon M\to C\subseteq\mathbb{R}^n$ is standard.

<<B072 prf>>
[PRF] **Proof.** As $B$ is contractible, we can pick a basis for $\Lambda^H$ over $B$ with period $2\pi\tau_1 (b),\dotsb, 2\pi\tau_n (b)$ so that $\Lambda_b^H =2\pi A(b)^T\mathbb{Z}^n$ where $A(b)$ is a diagonal matrix with $\tau_i (b)$ as entries. Now we look for a map $\alpha$ satisfying the partial differential relations $\displaystyle\frac{\partial\alpha_i}{\partial b_j}=A_{ij}$, which is solvable iff $\displaystyle\frac{\partial A_{ij}}{\partial b_k}=\frac{\partial A_{ik}}{\partial b_j}$. Now this can be verified using Liouville coordinates.

<<B073 p>>
We call $a$ the _action coordinate_, and $t$ the _angle coordinate_.

<<B074 env>>
[ENV] **Corollary(Big Arnold-Liouville Theorem).** Let $\vec{H}\colon M\to\mathbb{R}^n$ be completely integrable, then all regular fibers are Lagrangian tori and $M$ is locally symplectomorphic to $B\times\mathbb{T}^n$.

<<B075 p>>
Now we can show the first important property for Lagrangian fibrations:

<<B076 env>>
[ENV] **Proposition.** Regular Lagrangian fibrations are locally modelled on completely integrable hamiltonian systems.

<<B077 prf>>
[PRF] **Proof.** Given an open subset $\phi\colon U_b\to\mathbb{R}^n$ of regular values, we can form the composition $\pi^{-1} (U_b)\xrightarrow{\phi\circ\pi}\mathbb{R}^n$, which can be verified to be a completely integrable hamiltonian system.

<<B078 env>>
[ENV] **Corollary.** Fibers of regular Lagrangian fibrations are tori.

<<B079 p>>
The action-angle coordinates are local, but we can patch them together to glue regular Lagrangian fibrations over contractible spaces into some smooth manifold $B$, which carries a specific rigid structure and we call such manifolds _integral affine manifolds_.

<<B080 env>>
[ENV] **Definition.** An _integral affine transformation_ is a map $T\colon\mathbb{R}^n\to\mathbb{R}^n$ with $T(b)=Ab+c$ for some $A\in GL(n,\mathbb{Z})$ and $c\in\mathbb{R}^n$. An _integral affine structure_ on $B$ consists of an atlas with transition functions being integral affine transformations. We call manifolds admitting an integral affine structure an _integral affine manifold_.

<<B081 env>>
[ENV] **Lemma.** Let $G,H\colon M\to\mathbb{R}^n$ be completely integrable hamiltonian systems and $\psi\colon\mathbb{R}^n$ a diffeomorphism fitting into the commutative diagram

<<B082 quiver>>
[QUIVER] https://q.uiver.app/#q=WzAsMyxbMSwwLCJNIl0sWzAsMSwiXFxtYXRoYmJ7Un1ebiJdLFsyLDEsIlxcbWF0aGJie1J9Xm4iXSxbMCwxLCJHIiwyXSxbMCwyLCJIIl0sWzEsMiwiXFxwc2kiXV0=&embed

<<B083 p>>
then $\psi$ is integral affine.

<<B084 prf>>
[PRF] **Proof.** As we must have $d_b\psi\colon\Lambda_{\psi (b)}^G\to\Lambda_b^H$, for each $b$ $d_b\psi$ is of the form $d_b\psi (\xi)=A(b)\xi +c(b)$ where the matrix $A(b)$ lies in $GL(n,\mathbb{Z})$ and $c(b)\in\mathbb{R}^n$. Since period lattices for $G$ and $H$ are all standard, $d_b\psi$ must be constant, and hence $\psi (b)=Ab+c$.

<<B085 env>>
[ENV] **Corollary.** If $\pi\colon M\to B$ is a regular Lagrangian fibration, then $B$ inherits an integral affine structure.
