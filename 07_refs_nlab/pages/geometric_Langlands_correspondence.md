# geometric Langlands correspondence

url: https://ncatlab.org/nlab/show/geometric+Langlands+correspondence
last_revised: 2026-04-11
---

#### Langlands correspondence
+--{: .hide}
[[!include Langlands correspondence -- contents]]

\tableofcontents

## Idea
 {#Idea}

The [[conjecture|conjectural]] _geometric Langlands correspondence_ is meant to be an [[analogy|analog]] of the [[number theory|number theoretic]] [[Langlands correspondence]] under the [[function field analogy]], hence with [[number fields]] replaced by [[function fields]] and further replaced by [[rational functions]] on [[complex curves]].  The key to this analogy is the [[Weil uniformization theorem]] which expresses the [[moduli stack of G-principal bundles]] over an [[algebraic curve]] as a [[double coset space]] of various function rings (as discussed at _[Moduli of bundles over curves](moduli+space+of+bundles#OverCurvesAndTheLanglandsCorrespondence)_) of just the kind as they appear in the number-theoretic [[Langlands correspondence]] (for instance in the [[Artin reciprocity law]] and in the definition of [[automorphic representations]]).

[[!include Langlands analogies -- table]]

The original version of the conjectured statement of _geometric Langlands duality_ (going back to [Beilinson-Drinfeld 9x](#BeilinsonDrinfeld9x) and reviewed for instance in [Frenkel 05](#Frenkel05)) asserts that for $G$ a [[reductive group]] and for $\Sigma$ an [[algebraic curve]], then there is an [[equivalence of categories|equivalence]] of [[derived categories]] of, on the one hand, [[D-modules]] on the [[moduli stack of G-principal bundles]] on $\Sigma$, and, on the other hand, [[quasi-coherent sheaves]] on the  ${}^L G$-[[moduli stack of local systems]] on $\Sigma$:

$$
  \mathcal{O}Mod\big(Loc_{{}^L G}(\Sigma)\big)
    \stackrel{\simeq}{\longrightarrow}
  \mathcal{D} Mod\big( Bun_G(\Sigma)\big)
$$

for ${}^L G$ the [[Langlands dual group]]. Moreover, the conjecture asserts that there is canonical such an equivalence which is a [[non-abelian cohomology|non-abelian]] analogue of the [[Fourier-Mukai transform|Fourier-Mukai]] [[integral transform]] and takes [[skyscraper sheaves]] on the left ([[categorification|categorified]] [[Dirac distributions]]) to what are called "[[Hecke eigensheaves]]" on the right.
This equivalence is in turn supposed to be a certain limit of the more general [[quantum geometric Langlands correspondence]] that identifies [[twisted D-modules]] on both sides.

For the [[abelian group|abelian]] case that $G$ is a [[torus]] the above equivalence has indeed been proven, given by a [[Fourier-Mukai transform]]  ([Laumon 85](#Laumon85), [Laumon 96](#Laumon96), [Rothstein 96](#Rothstein96)), see also [below](#AbelianCase).

{#However} However, in general the above version of the conjecture is false. For instance it fails in the case $G = SL_2$ and $\Sigma= \mathbb{P}^1$ ([Lafforgue 09](#Lafforgue09)).

A refined formulation of the conjecture due to [Arinkin & Gaitsgory 12](#ArinkinGaitsgory12), meant to fix this failure, replaces plain quasicoherent sheaves with certain "nilpotent" [[ind-objects]] of quasicoherent sheaves and refines [[derived categories]] to [[stable (∞,1)-categories]], to make the conjecture read

$$
  \bigg(Ind
  \Big(
    \mathcal{O}Mod
    \big(
      Loc_{{}^L G}(\Sigma)
    \big)
  \Big)
  \bigg)_{Nilp_{Glob}}
    \overset{\simeq}{\longrightarrow}
  \mathcal{D} Mod\big( 
    Bun_G(\Sigma)
  \big)
  \,.
$$

([Arinkin & Gaitsgory 12, conjecture 0.1.6](#ArinkinGaitsgory12)).

This form is called the [[categorical geometric Langlands conjecture]]. A proof was given by [Gaitsgory et al. 2025](#GaitsgoryGLCWebpage).

Since [[D-modules]] on [[moduli stacks of G-principal bundles]] play a central role in [[gauge theory|gauge]] [[quantum field theory]] (in particular as [[Hitchin connections]] on bundles of [[conformal blocks]] of $G$-[[Chern-Simons theory]] [[holographic principle|holographically]] dual to the [[WZW model]] [[2d conformal field theory]]) and since the [[Langlands dual group]] also appears in [[electric-magnetic duality]], it has long been suggested ([Atiyah 77](S-duality#Atiyah77)) that geometric Langlands duality has a distinguished meaning also in [[mathematical physics]] in general and in [[string theory]] in particular. One proposal for a realization of the correspondence as an incarnation of [[mirror symmetry]]/[[S-duality]] is due to ([Kapustin & Witten 06](#KapustinWitten06)), which however has not been turned into [[theorems]] yet. Another proposal for realizing the [[local Langlands correspondence|local]] correspondence via another incarnation of [[mirror symmetry]] is due to [Gerasimov, Lebedev & Oblezin 09](#GerasimovLebedevOblezin09).

The geometric Langlands conjecture has been motivated from the [[number theory|number theoretic]] [[Langlands correspondence]] via the [[function field analogy]] and some educated guessing, but there is to date no formalization of this analogy that would allow to regard number-theoretic and the geometric correspondence as two special cases of one "global" [[arithmetic geometry]]/[[global analytic geometry]] statement. Cautioning remarks on the accuracy of the analogy and on the rigour of the mirror-symmetric proposals may be found in ([Langlands 14](#Langlands14)). Some discussion of how to possibly start to go about making the analogy more systematic are at _[[differential cohesion and idelic structure]]_.

[[!include function field analogy -- table]]

## Properties 
 {#Properties}

### Abelian case
 {#AbelianCase}

In the case where $G$ is the [[multiplicative group]], hence where all bundles in question are [[line bundles]], geometric Langlands duality is well understood and is in fact a slight variant of a [[Fourier-Mukai transform]] ([Frenkel 05, section 4.4, 4.5](#Frenkel05)).

### Relation to S-duality
 {#RelationToSDuality}

The [[Kapustin-Witten TQFT]] ([KapustinWitten 2007](#KapustinWitten06)) is supposed to exhibit geometric Langlands duality as a special case of [[S-duality]]. 

See also at _[KK-compactification -- Formalization](http://ncatlab.org/nlab/show/Kaluza-Kl

[... 正文截断于 6000 字符 ...]
