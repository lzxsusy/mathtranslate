# monoidal functor

url: https://ncatlab.org/nlab/show/monoidal+functor
last_revised: 2026-01-26
---

#### Monoidal categories
+--{: .hide}
[[!include monoidal categories - contents]]

+-- {: .num_remark}
###### Remark

In the literature often the term "monoidal functor" refers by default to what in def. \ref{LaxMonoidalFunctor} is called a strong monoidal functor.  With that convention then what def. \ref{LaxMonoidalFunctor} calls a lax monoidal functor is called a  **weak monoidal functor**.  

+-- {: .num_remark}
###### Definition

An __[[oplax monoidal functor]]__ (with various alternative names including **comonoidal**), is a monoidal functor from the [[opposite categories]] $C^{op}$ to $D^{op}$.

## Properties

+-- {: .num_prop #MonoidsToMonoidsByLaxMonoidal}
###### Proposition
**(Lax monoidal functors send [[monoid]]s to monoids)**

If $F : (C,\otimes) \to (D,\otimes)$ is a lax monoidal functor and 

$$
  (A \in C,\;\; \mu_A : A \otimes A \to A, \; i_A : I \to A)
$$

is a [[monoid object]] in $C$, then the object $F(A)$ is naturally equipped with the structure of a monoid in $D$ by setting

$$
  i_{F(A)} : I_D \stackrel{}{\to} F(I_C) \stackrel{F(i_A)}{\to} F(A)
$$

and

$$
  \mu_{F(A)} : 
  F(A) \otimes F(A)
  \stackrel{\nabla_{F(A), F(A)}}{\to} 
  F(A \otimes A)
  \stackrel{F(\mu_A)}{\to}
  F(A)
  \,.
$$

This construction defines a functor

$$
  Mon(f) : Mon(C) \to Mon(D)
$$

between the [[categories of monoids]] in $C$ and $D$, respectively.

### Relation to multicategories

+-- {: .num_remark}
###### Remark

Lax monoidal functors between monoidal categories are in correspondence with [[morphism of multicategories|morphisms]] between their underlying ([[representable multicategories|representable]]) [[multicategories]].

+-- {: .num_remark}
###### Remark

Strict monoidal functors between monoidal categories are in correspondence with morphisms between their underlying colored [[PROs]] that preserve the distinguished isomorphisms $() \xrightarrow{\sim} I$ and  $(A, B) \xrightarrow{\sim} (A \otimes B)$ for all $A, B$.

+-- {: .proof}
###### Proof

The former has an initial object, whereas the latter does not.

+-- {: .proof}
###### Proof

As mentioned at [[monoidal category#the_2category_of_monoidal_categories|monoidal category]], not every skeletal monoidal category is monoidally equivalent to a strict skeletal monoidal category. Therefore the inclusion is not essentially surjective.

+-- {: .proof}
###### Proof

Not every strong monoidal functor between strict monoidal categories is equivalent to a strict one. See for example [this MathOverflow question](https://mathoverflow.net/questions/172815/strictifying-strong-monoidal-functors).

+-- {: .proof}
###### Proof

By the [[coherence theorem for monoidal categories]], every monoidal category is strong monoidally equivalent to a strict one.
