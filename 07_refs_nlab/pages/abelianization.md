# abelianization

url: https://ncatlab.org/nlab/show/abelianization
last_revised: 2026-01-21
---

### Context
#### Category theory
+-- {: .hide}
[[!include category theory - contents]]

* table of contents

## Idea

Abelianisation is the process of [[free functor|freely]] making an [[algebraic structure]] 'abelian'. There are several notions of abelianizations for various algebraic structures, notably there is the abelianization of [[non-abelian groups]] to [[abelian groups]].

There are also Freyd's abelianization functor from any additive category to an abelian category with some universal property and, as a special case, [[Verdier's abelianization functor]] from a [[triangulated category]] to an [[abelian category]] with yet another universal property; this is treated in a separate entry.  

## For groups

### Definition

+-- {: .num_defn }
###### Definition

For $G$ a [[group]], its **abelianization** $G^{ab} \in $ [[Grp]] is the [[quotient]] of $G$ by its [[commutator subgroup]]:

$$
  G^{ab} \coloneqq G/[G,G]
  \,,
$$

Hence abelianization is the _[[free construction]]_ of an abelian group from a group.

### Examples

#### Homotopy groups

+-- {: .num_example }
###### Example

Given a [[pointed space|pointed]] [[connected topological space]] $(X,a)$, its first [[singular homology|singular]] [[homology group]] with coefficients in the [[integers]] is the abelianisation of its [[fundamental group]]:
$$ H_1(X,\mathbb{Z}) \cong \pi_1(X,a)^{ab} .$$
This is a [[natural isomorphism]] filling the following diagram of [[functors]]:
$$ \array {
   Top_{\geq 1}^{*/} & \overset{\pi_1}\longrightarrow & Grp \\
   \llap{U}\downarrow & & \downarrow\rlap{ab} \\
   Top & \underset{H_1({-},\mathbb{Z})}\longrightarrow & Ab Grp
} $$
(where $U$ [[forgetful functor|forgets]] the point).

This example can also be done starting with an arbitrary pointed topological space and letting $U$ take the [[connected component]] of the point.  Of course, this example really lives in [[∞ Grpd]] and so we could start with a (pointed, maybe connected) [[simplicial set]], [[Kan complex]], etc.
