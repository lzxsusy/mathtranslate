# etale morphism of schemes

url: https://ncatlab.org/nlab/show/etale+morphism+of+schemes
last_revised: 2026-07-03
---

#### &#201;tale morphisms
+--{: .hide}
[[!include etale morphisms - contents]]

* table of contents

## Idea

The notion of _&#233;tale morphism of schemes_ is the realization of the general notion of [[étale morphism]] for maps between [[schemes]], hence it captures roughly the idea of a map of schemes which is a [[local homeomorphism]]/[[local diffeomorphism]].

A central use of &#233;tale morphisms of schemes is that they appear as [[coverings]] in the [[Grothendieck topology]] of the [[étale site]]. The [[abelian sheaf cohomology]] with respect to these &#233;tale covers of schemes is accordingly called _[[étale cohomology]]_.

## Definition

+-- {: .num_defn #EquivalentConditionsForEtale}
###### Definition

A [[morphism]] of [[schemes]] is an **&#233;tale morphism** if the following equivalent conditions hold:

1. it is

   1. [[smooth morphism of schemes|smooth]] 

   1. [[unramified morphism|unramified]] 

1. it is

   1. [[smooth morphism of schemes|smooth]] 

   1. of [[relative dimension]] $0$. 

1. it is 

   1. [[flat morphism|flat]] 

   1. [[unramified]];

1. it is

   1. [[formally étale morphism of schemes|formally étale]];

   1. [[locally of finite presentation]]

+-- {: .num_remark}
###### Remark

Relaxing the finiteness condition in item 4 of \ref{EquivalentConditionsForEtale} yields the notion of _[[weakly étale morphism]]_.

[[étale morphism of schemes|étale morphism]] $\Rightarrow$ [[pro-étale morphism of schemes|pro-étale morphism]] $\Rightarrow$ [[weakly étale morphism of schemes|weakly étale morphism]] $\Rightarrow$ [[formally étale morphism of schemes|formally étale morphism]]

+-- {: .num_remark}
###### Remark

Most of the pairs of conditions in def. \ref{EquivalentConditionsForEtale} can be read as constraining the fiber of the morphism to be first suitably surjective/[[bundle]]-like ([[smooth morphism of schemes|smooth]], [[flat morphism|flat]]) and second suitably locally injective ([[unramified]]).

Specifically the first condition has an [[infinitesimal object|infinitesimal]] analog: a [[formally étale morphism]] is a [[formally smooth morphism|formally smooth]] and [[formally unramified morphism]]. These notions also have an interpretation in [[synthetic differential geometry]] and there they correspond to the statement that a [[local diffeomorphism]] is a [[submersion]] which is also an [[immersion of smooth manifolds]].

+-- {: .num_remark}
###### Remark

These are sheaf-like properties, which can be formalized in the language of [[Q-categories]] ([[monopresheaf]] and [[epipresheaf]] properties on the $Q$-category of nilpotent thickenings). 

See at _[[differential cohesion]]_ and at _[[infinitesimal shape modality]]_.

(e.g. [Milne, prop. 2.11](#Milne))

+-- {: .proof}
###### Proof

Use that an &#233;tale morphism is a [[formally étale morphism]] with finite fibers, and that $f \colon X \to Y$ is formally &#233;tale precisely if the [[infinitesimal shape modality]] [[unit of a monad|unit]] [[natural transformation|naturality square]]

$$
  \array{
    X &\longrightarrow& \Pi_{inf}(X)
    \\
    \downarrow && \downarrow
    \\
    Y &\longrightarrow& \Pi_{inf}(Y)
  }
$$

is a [[pullback]] square. Then the three properties to be shown are equivalently the [[pasting law]] for pullback diagrams.

+-- {: .num_remark}
###### Remark

This disjointness picture of &#233;tale covers make them suitable for having nontrivial [[cohomology]] in situations where Zariski covers give vanishing cohomology.

This appears for instance as [de Jong, prop. 3.1 i)](#deJong). 

+-- {: .num_remark}
###### Remark

Such &#233;tale morphisms are classified by the classical [[Galois theory]] of field extensions.

This appears for instance as ([Milne, prop. 2.1](#Milne)).

### As locally constant sheaves {#AsLocallyConstantSheaves}

+-- {: .num_prop}
###### Proposition

A [[sheaf]] $F$ on a scheme $X$ corresponds to an &#233;tale morphism $Y \to X$ precisely if there is an [[étale cover]] $\{U_i \to X\}$ such that each restriction

$$
  F|_{U_i} \simeq LConst K_i
$$

is [[isomorphic]] to a [[constant sheaf]] on a [[set]] $K_i$.

+-- {: .num_example #OpenImmersionIsEtale}
###### Example

Every [[open immersion of schemes]] is an &#233;tale morphism of schemes.
In particular a standard open inclusion (a [[cover]] in the [[Zariski topology]]) induced by the [[localization of a commutative ring]]

$$
  Spec(R[S^{-1}]) \longrightarrow Spec(R)
$$

is &#233;tale.

## Related concepts

* [[étale morphism]]

* **&#233;tale morphism of schemes**

  * [[étale site]], [[étale cohomology]]

  * [[étale (∞,1)-site]]

  * [[étale morphism of E-∞ rings]]

## References

The classical references are

* [[Pierre Deligne]] et al., _Cohomologie &#233;tale_ , Lecture Notes in Mathematics, no. 569, Springer-Verlag, 1977.
{#Deligne}

* [[James Milne]], _[[Étale Cohomology]]_, Princeton Mathematical Series __33__, 1980. xiii+323 pp.

Lecture notes include

* [[James Milne]], section 2 of _[[Lectures on Étale Cohomology]]_
 {#Milne}

* [[Aise Johan de Jong]], _&#201;tale cohomology_ ([pdf](http://math.columbia.edu/~pugin/Teaching/Etale_files/EtaleCohomology.pdf))
{#deJong} --- link broken, couldn't find another copy online

The local structure theorems are discussed in 

* Leovigildo Alonso, Ana Jeremias, Marta Perez, _Local structure theorems for smooth maps of formal schemes_ ([arXiv:math/0605115](http://arxiv.org/abs/math/0605115))

Discussion of etale morphisms between [[E-infinity rings]]/[[spectral schemes]] is in 

* [[Jacob Lurie]], section 7.5 of _[[Higher Algebra]]_

and generally in [[E-∞ geometry]] in 

* [[Jacob Lurie]], section 1.2 of _[[Quasi-Coherent Sheaves and
Tannaka Duality Theorems]]_
