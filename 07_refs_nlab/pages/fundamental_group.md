# fundamental group

url: https://ncatlab.org/nlab/show/fundamental+group
last_revised: 2025-09-04
---

### Context
#### Homotopy theory
+-- {: .hide}
[[!include homotopy - contents]]

* table of contents

## Idea 

The _fundamental group_ $\pi_1(X,x)$ of a [[pointed object|pointed]] [[topological space]] $(X,x)$ is the group of based [[homotopy classes]] of [[loops]] at $x$, with multiplication defined by concatenation (following one path by another).  

This is also called _the first [[homotopy group]]_ of $X$.

The notion of _fundamental group_ $\pi_1(X,x)$ generalises in one direction to the [[fundamental groupoid]] $\Pi_1(X)$, or in another direction to the [[homotopy groups]] $\pi_n(X,a)$ for $n \in \mathbb{N}$. Both of this is contained within the [[fundamental ∞-groupoid]] $\Pi(X)$.

## Definition

+-- {: .num_defn}
###### Definition

For $X$ a [[topological space]] and $x : * \to X$ a [[point]]. A [[loop space|loop]] in $X$ based at $x$ is a [[continuous function]]

$$
  \gamma : \Delta^1  \to X
$$

from the topological 1-[[simplex]], such that $\gamma(0) = \gamma(1) = x$.

A _based [[homotopy]]_ between two loops is a [[homotopy]] 

$$
  \array{
    \Delta^1
    \\
    \downarrow^{\mathrlap{(id,\delta_0)}} & \searrow^{\mathrlap{f}}
    \\
    \Delta^1 \times \Delta^1 &\stackrel{\eta}{\to}& X
    \\
    \uparrow^{\mathrlap{(id,\delta_1)}} & \nearrow_{\mathrlap{g}}
    \\
    \Delta^1
  }
$$

such that $\eta(0,-) = \eta(1,-) = x$.

+-- {: .proof}
###### Proof

This is directly checked. It is also a special case of the general discussion at _[[homotopy]]_. 

+-- {: .num_prop #GroupStructure}
###### Proposition

Concatenation of loops respects based homotopy classes
where it becomes an [[associativity|associative]], [[unital]]
binary pairing with [[inverses]], hence the product in a [[group]].

+-- {: .num_defn}
###### Definition

For $X$ a topological space and $x \in X$ a point, the set of based homotopy equivalence classes of based loops in $X$ equipped with the group structure from prop. \ref{GroupStructure} is the **fundamental group** or **first [[homotopy group]]** of $(X,x)$, denoted

$$
  \pi_1(X,x) \in Grp
  \,.
$$

+-- {: .num_defn #EMSpace}
###### Definition

Conversely, a topological space whose only non-trivial [[homotopy group]] is the fundamental group is called an [[Eilenberg-MacLane space]] denoted $K(\pi_1(X), 1)$.

+-- {: .proof}
###### Proof

For $x_0, x_1 \in X$ any two basepoints, there is by assumption a path connecting them, hence a [[continuous function]]

$$
  p : \Delta^1 \to X
$$

such that $p(0) = x_0$ and $p(1) = x_1$. 

Write $\bar p \coloneqq (p(1-(-)))$ for the same path with the orientation reversed. Then for $\gamma_0$ any loop based at $x_0$, the concatenation 
$ [ p \cdot (\gamma_0 \cdot \bar p) ]$, def. \ref{Concatenation} yield a loop based at $x_1$ (obtained from $[\gamma_0]$ by [[conjugation]] with $[p]$).

It is immediate to check that this induces an [[isomorphism]]

$$
  Ad_{[p]} : \pi_1(X,x_0) \to \pi_1(X,x_1)
  \,.
$$

+-- {: .num_prop}
###### Proposition

It is, however, a functor on [[pointed object|pointed topological spaces]]:
$\pi_1(-) :$ [[Top]] ${}^{*/} \to$ [[Grp]].

+-- {: .proof}
###### Proof

Let 

$$
  \gamma \;\colon\; [0,1] \longrightarrow \mathbb{R}^n
$$

be [[loop]] at $x$, hence a [[continuous function]] with $\gamma(0) = x$ and $\gamma(1) = x$. Using the [[real vector space]] structure on $\mathbb{R}^n$, we may define the function

$$
  \array{
    [0,1] \times [0,1] &\overset{\eta}{\longrightarrow}& \mathbb{R}^n
    \\
    (t,s) &\mapsto& x + s (\gamma(t) - x)
  }
  \,.
$$

This is a [[continuous function]], since it is the composite of the continuous function $(id_{[0,1]} \times \gamma) \;\colon\; (t,s) \mapsto (\gamma(t),s)$ (which is continuous as the [[product topological space|product]] of two continuous functions) and the function $(v,s) \mapsto x + s ( v - x )$ (which is continuous since [[polynomials are continuous]]).

Moreover, by construction we have

$$
  \eta(-,1) = \gamma(-)
   \phantom{AAAA}
  \eta(-,0) = const_x
  \,.
$$

Therefore this is a [[homotopy]] from $\gamma$ to the constant loop at $x$.

+-- {: .num_example}
###### Example

The [[fundamental group of the circle is the integers]]: 

$$
  \pi_1(S^1) \simeq \mathbb{Z}
  \,.
$$

+-- {: .num_example}
###### Example

By definition \ref{EMSpace}, the fundamental group of any [[Eilenberg-MacLane space]] $K(G,1)$ is $G$: $\pi_1(K(G,1)) = G$.
