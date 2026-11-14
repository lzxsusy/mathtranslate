# polarization

url: https://ncatlab.org/nlab/show/polarization
last_revised: 2026-01-25
---

### Context
#### Geometric quantization
+-- {: .hide}
[[!include geometric quantization - contents]]

* table of contents

## Idea

For a [[symplectic manifold]] $(X, \omega)$ regarded as the [[phase space]] of a [[physical system]], a choice of _polarization_ is, locally, a choice of decomposition of the [[coordinates]] on $X$ into "[[canonical coordinates]]" and "[[canonical momenta]]".

The archetypical example is that where $X = T^* \Sigma$ is the [[cotangent bundle]] of a [[manifold]] $\Sigma$. In this case the canonical [[canonical coordinates]] are those parameterizing $\Sigma$ itself, while the canonical [[canonical momenta]] are coordinates on each [[fiber]] of the cotangent bundle.

But for general symplectic manifolds there is no such canonical choice of coordinates and momenta. Moreover, in general there is not even a global notion of canonical momenta. Instead, a choice of (real) polarization is a [[foliation]] of phase space by [[Lagrangian submanifolds]] and then

* the "[[canonical coordinates]]" are coordinates on the corresponding [[leaf space]] (parameterizing the leaves);

* the "[[canonical momenta]]" are coordinates along each [[leaf]]. If there is no _typical leaf_ then this is not a globally defined notion, only the polarization itself is.

Locally this is a choice of [[coordinate patch]] $\phi : \mathbb{R}^{2n} \to X$ such that the [[symplectic form]] takes the form

$$
  \phi^* \omega = \sum_{i = 1}^n \mathbf{d} q^i \wedge \mathbf{d}p_i
$$

where the $\{q^i : \mathbb{R}^{2n} \simeq \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}\}$ are the canonical coordinates on the first $\mathbb{R}^n$-factor of the [[Cartesian space]] $\mathbb{R}^{2n}$, and where $\{p_o : \mathbb{R}^{2n} \simeq \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}\}$ are canonical coordinates  on the second $\mathbb{R}^n$-factor.

## Definition

The traditional notion of polarization applies to a [[symplectic manifold]].

* [Of a symplectic manifold](#OfASymplecticManifold)

Symplectic manifold are the lowest step in a tower of notions in [[higher symplectic geometry]] which proceeds with [[n-plectic geometry]] for all $n$ and manifolds refined to [[smooth infinity-groupoids]]. The next simplest cases in this tower are [[symplectic Lie n-algebroids]], which for $n=1$ are [[Poisson Lie algebroids]] and for $n = 2$ are [[Courant Lie 2-algebroids]]:

* [Of a Poisson Lie algebroid](#OfAPoissonLieAlgebroid)

* [Of a Courant Lie 2-algebroid](#OfACourantLie2Algebroid)

* [Of a symplectic Lie n-algebroid](#OfASymplecticLienAlgebroid)

### Of a symplectic manifold
 {#OfASymplecticManifold}

Let $(X, \omega)$ be a [[symplectic manifold]]. 

+-- {: .num_defn #ByLagrangianFoliation}
###### Definition

A **real polarization** of $(X, \omega)$ is a [[foliation]] by [[Lagrangian submanifolds]]. 

For instance ([Bates-Weinstein, def. 7.4](#BatesWeinstein))

### Of a Poisson Lie algebroid
 {#OfAPoissonLieAlgebroid}

A [[Poisson Lie algebroid]] $\mathfrak{P}$ is a [[symplectic Lie n-algebroid]] for $n = 1$. Regarding its [[Chevalley-Eilenberg algebra]] as the algebra of functions on a [[dg-manifold]], that dg-manifold carries a graded [[symplectic form]] $\omega$. One can then say

+-- {: .num_defn #ForPoissonLieAlgebroidyByLagrangianFoliation}
###### Definition

A dg-[[Lagrangian submanifold]] of $(\mathfrak{P}, \omega)$ is also called a **$\Lambda$-structure**. ([&#352;evera, section 4](#Severa)).

Hence we might say **real polarization** of $(\mathfrak{P}, \omega)$ is a foliation by dg-Lagrangian submanifolds.

([&#352;evera, section 4](#Severa))

+-- {: .num_remark}
###### Remark

The dg-Lagrangian submanifolds also correspond to [[branes]] in the [[Poisson sigma-model]] (see there) on $(\mathfrak{P}, \omega)$. 

+-- {: .num_prop}
###### Proposition

The dg-Lagrangian submanifolds of a Courant Lie 2-algebroid $(\mathfrak{C}, \omega)$ correspond to [[Dirac structures]] on $(\mathfrak{C}, \omega)$.
