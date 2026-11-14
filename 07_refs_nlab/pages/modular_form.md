# modular form

url: https://ncatlab.org/nlab/show/modular+form
last_revised: 2025-03-13
---

#### Elliptic cohomology
+-- {: .hide}
[[!include elliptic cohomology -- contents]]

* table of contents

## Idea

A _modular form_  is a [[holomorphic function]] on the [[upper half-plane]] that satisfies certain transformation property under the [[action]] of the [[modular group]]. Abstractly this transformation property makes the function a [[section]] of a certain [[line bundle]] on the [[quotient]] of the [[upper half plane]] that makes it the [[moduli stack of elliptic curves]] (over the [[complex numbers]]) or more generally a [[modular curve]].

Modular forms are also often called _classical [[automorphic forms]]_, see [below](). As automorphic forms, they are related to Galois representations as part of the [[Langlands program]].

Modular forms appear as the [[coefficient]] ring of the [[Witten genus]] on manifolds with rational [[string structure]]. For manifolds with actual [[string structure]] this refines to [[topological modular forms]], which are the [[homotopy groups]] of the [[spectrum]] [[tmf]].

## Definition

### In components

+-- {: .num_defn}
###### Definition

An **(integral) [[modular form]]** of weight $w$ is a [[holomorphic function]] on the [[upper half-plane]]

$$
  f : (\mathbb{R}^2)_+ \hookrightarrow \mathbb{C}
$$

(complex numbers with strictly positive imaginary part) 

such that

1. if $A = \left( \array{a & b \\ c& d}\right) \in SL_2(\mathbb{Z})$ acting by $A : \tau \mapsto = \frac{a \tau + b }{c \tau + d}$ we have
 
   $$
     f(A(\tau)) = (c \tau + d)^w f(\tau)
   $$

   (notice that for $A = \left( \array{1 & 1 \\ 0& 1}\right)$ then  $f(\tau + 1) = f(\tau)$)

1. $f$ has at worst a pole at $\{0\}$ (for _weak_ modular forms this condition is relaxed)

   it follows that $f = f(q)$ with $q = e^{2 \pi i \tau}$ is a meromorphic funtion on the open disk.

1. **integrality** $\tilde f(q) = \sum_{k = -N}^\infty a_k \cdot q^k$ then $a_k \in \mathbb{Z}$
