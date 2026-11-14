# injective object

url: https://ncatlab.org/nlab/show/injective+object
last_revised: 2025-12-24
---

#### Category theory
+--{: .hide}
[[!include category theory - contents]]

* table of contents

## Definition

There is a very general notion of an _injective object_ in a [[category]] $C$, and then there is a sequence of more concrete notions as $C$ is equipped with more [[stuff, structure, property|structure and property]], in particular for $C$ an [[abelian category]] [[additive and abelian categories|or a relative]] thereof.

The concept of [[resolutions]] by injective objects -- [[injective resolutions]] -- is crucial in the discussion of [[derived functors]] (see [[derived functors in homological algebra]]).

Being injective is a *property* of an object; the corresponding *structure* is called an [[algebraic injective]].

### General definition 

Let $C$ be a [[category]] and $J \subset Mor(C)$ a [[class]] of [[morphisms]] in $C$.  

+-- {: .num_example}
###### Example

Frequently, $J$ is the class of all [[monomorphisms]], or a related class such as the [[regular monomorphisms]].

When $C$ is a [[category of chain complexes]] equipped with the injective [[model structure on chain complexes]], then $J$ is often its class of [[cofibrations]].

\begin{remark}\label{InjectiveObjectsAsInjectiveMorphisms}
If $C$ has a [[terminal object]] $\ast$, then the $J$-injective objects $I$ according to def. \ref{InjectiveObjects} are those for which the unique morphism $I \stackrel{\exists!}{\to} \ast$ is a $J$-[[injective morphism]].
\end{remark}

+-- {: .num_defn #EnoughInjectives}
###### Definition

One says that a category $C$ has **enough injectives** if every object admits a [[monomorphism]] into an injective object.

+-- {: .num_remark}
###### Remark

If $C$ has a [[terminal object]] $*$, then these extensions are equivalently [[lifts]]

$$
  \array{
    X &\longrightarrow& I
    \\
    \mathllap{{}^{j \in J}}
    \big\downarrow 
    & 
    \nearrow_{\mathrlap{\exists}}
    &
    \big\downarrow
    \\
    Z
    &\longrightarrow&
    *
  }
$$

and hence the $J$-injective objects are precisely those that have the [[right lifting property]] against the class $J$.

+-- {: .num_prop #InjectivesCharacterisedBySplitting}
###### Proposition

If $C$ has [[pushouts]] and the pushout of a morphism in $J$ along any other morphism is always an element of $J$, then the $J$-injective objects are precisely the objects $I$ such that every morphism in $J$ with domain $I$ is a [[split monomorphism]].

+-- {: .proof}
###### Proof

By definition of [[abelian category]] every monomorphism $A \hookrightarrow B$ is a [[kernel]], hence a [[pullback]] of the form

$$
  \array{
    A &\to& 0
    \\
    \downarrow && \downarrow
    \\
    B &\to& C
  }
$$

for $0$ the (algebraic) [[zero object]]. By the <a href="http://ncatlab.org/nlab/show/pullback#Pasting">pasting law</a> for pullbacks we find that also the left square in 

$$
  \array{
    0 &\to& A &\to& 0
    \\
    \downarrow && \downarrow && \downarrow
    \\
    0 &\to& B &\to& C
  }
$$

is a pullback, hence $0 \to A \to B$ is exact.

By the [[formal dual]] of [this prop.](projective+module#NProjectiveIFFHomNExact).

### In chain complexes

See [[homotopically injective object]] for a relevant generalization to categories of chain complexes, and its relationship to ordinary injectivity.

## Examples

### Injective modules
 {#InjectiveModules}

Let $R$ be a [[commutative ring]] and  $C = R Mod$ the category of $R$-[[modules]]. We discuss [[injective modules]] over $R$ (see there for more).

The following criterion says that for identifying [[injective modules]] it is sufficient to test the [[right lifting property]] which characterizes injective objects by def. \ref{InjectiveObjects}, only on those [[monomorphisms]] which include an [[ideal]] into the base ring $R$.

+-- {: .num_theorem #BaerTheorem}
###### Proposition 
**([[Baer's criterion]])**

If the [[axiom of choice]] holds, 
then a [[module]] $Q \in R Mod$ is an [[injective module]] precisely if for $I$ any left $R$-[[ideal]] regarded as an $R$-module, any [[homomorphism]] $g : I \to Q$ in $C$ can be extended to all of $R$ along the inclusion $I \hookrightarrow R$.

+-- {: .num_corollary #DirectSumInjectives}
###### Corollary
(Assume that the [[axiom of choice]] holds.) Let $R$ be a [[Noetherian ring]], and let $\{Q_j\}_{j \in J}$ be a collection of [[injective modules]] over $R$. Then the [[direct sum]] $Q = \bigoplus_{j \in J} Q_j$ is also injective. 

+-- {: .num_prop}
###### Proposition

Conversely, $R$ is a [[Noetherian ring]] if [[direct sums]] of injective $R$-[[modules]] are injective. 

This follows for instance using [[Baer's criterion]], prop. \ref{BaerTheorem}.

An explicit proof is spelled out at 
[Planet math -- abelian group is divisible if and only if it is an injective object](https://planetmath.org/abeliangroupisdivisibleifandonlyifitisaninjectiveobject)

+-- {: .num_example}
###### Example

By prop. \ref{InjectiveAbelianGroupIsDivisibleGroup} the following [[abelian groups]] are injective in [[Ab]].

The group of [[rational numbers]] $\mathbb{Q}$ is injective in [[Ab]], as is the additive group of [[real numbers]] $\mathbb{R}$ and generally that underlying any [[field]] of characteristic zero. The additive group underlying any [[vector space]] is injective. The [[quotient]] of any injective group by any other group is injective.

### In toposes 

In any [[topos]], the [[subobject classifier]] $\Omega$ is an injective object, as is any [[powering|power]] of $\Omega$ ([[Mac Lane-Moerdijk]], IV.10). 

Also one can define various notions of *internally* injective objects. These turn out to be equivalent:

+-- {: .num_prop #EquivalenceOfInternalNotionsOfInjectivity}
###### Proposition

In any [[elementary topos]] $\mathcal{E}$ with a [[natural numbers object]], the following statements about an object $I \in \mathcal{E}$ are equivalent.

1. The functor $[-, I] : \mathcal{E}^op \to \mathcal{E}$ maps monomorphisms in $\mathcal{E}$ to epimorphisms.
2. The functor $[-, I] : \mathcal{E}^op \to 

[... 正文截断于 6000 字符 ...]
