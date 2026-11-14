# six operations

url: https://ncatlab.org/nlab/show/six+operations
last_revised: 2026-09-30
---

#### Geometry
+--{: .hide}
[[!include higher geometry - contents]]

\tableofcontents

## Idea

### General

What is known as _(Grothendieck's) six operations_ is a formalization of structure that 

* assigns to every [[morphism]] $f$ of suitable [[spaces]] a ([[derived direct image|derived]])[[direct image]]/([[derived inverse image|derived]])[[inverse image]] [[adjunction]] $(f^\ast \dashv f_*)$;

* assigns to every [[separated morphism]] a [[direct image with compact support]]/[[Verdier duality|Verdier dual]] [[adjunction]] $(f_! \dashv f^!)$.

These are _four operations_ and together with

* a [[closed monoidal category|closed]] [[symmetric monoidal category|symmetric monoidal]] [[tensor product]]/[[internal hom]] [[adjunction]] $((-)\otimes X \dashv [X,-])$ 

form _six operations_. 

(All this is usually interpreted as [[derived functors]]/[[(infinity,1)-functors]] so that for instance in the usual application to [[derived categories]] of [[abelian sheaves]] the last two operations are really [[Tor]] and [[Ext]].) 

With a list of compatibility conditions between these (for instance ([Cisinski-D&#233;glise 09, p. x](#CisinskiDeglise09)) this is a structure of _Grothendieck's six operations_.

These consistency conditions include the following:

1. The adjunctions are functorial, hence form [[2-functors]] $f \mapsto f_*$, $f \mapsto f_!$:

1. There is a [[natural transformation]]  $f_! \to f_*$ which is a [[natural equivalence]] when $f$ is a [[proper map]]. 

1. [[Beck-Chevalley condition]] (base change formulas): given a ([[homotopy pullback|homotopy]]) [[pullback]] [[diagram]]

   $$
     \array{
       && Q_1 \underset{X}{\times} Q_2
       \\
       & {}^{\mathllap{p_1}}\swarrow && \searrow^{\mathrlap{p_2}}
       \\
       Q_1 && && Q_2
       \\
       & {}_{\mathllap{f}}\searrow && \swarrow_{\mathrlap{g}}
       \\
       && X
     }
   $$

   such that $f$ is a [[separated morphism]], then there are [[natural equivalences]]

   $$
     g^\ast \circ f_! \simeq (p_2)_! \circ (p_1)^\ast
   $$

   $$
     f^! \circ g_\ast \simeq (p_1)_\ast\circ (p_2)^!
     \,. 
   $$

1. ...

([Cisinski-D&#233;glise 09, p. x](#CisinskiDeglise09))

Morover one imposes a formalization of [[Verdier duality]] with [[dualizing object]]...

([Cisinski-D&#233;glise 09, p. xi](#CisinskiDeglise09))

### Specializations

Often specializations of the general concept play a role:

* [[Wirthmüller context]]: $f^! \simeq f^\ast$ and $f^\ast$ is a strong [[closed monoidal functor]] (hence the [[projection formula]] for $f_!$ holds);

  * [[transfer context]]: in addition the [[projection formula]] for $f_\ast$ holds;

* [[Verdier-Grothendieck context]]: the "projection formula" $Y \otimes f_! X \simeq f_!(f^\ast Y \otimes X)$ holds naturally in $X,Y$:

* [[Grothendieck context]]: $f_! \simeq f_\ast$ and the projection formula holds $Y \otimes f_! X \simeq f_!(f^\ast Y \otimes X)$.

## Mann's approach

Mann ([Mann 22](#Mann22)) has developed an abstract framework for a six-functor formalism that combines the approaches of Liu-Zheng and Gaitsgory-Rozenblyum and applies it to [[rigid analytic geometry]], in particular in combination with [[condensed mathematics]] and [[almost mathematics]] to construct an [[(infinity,1)-category|$\infty$-category]] of derived solid $\mathcal{O}_{X}^{+}/\pi$ almost modules (see also [Scholze22](#Scholze22)).

\begin{definition}
Let $C$ be an $\infty$-category admitting finite limits and let $E$ be a class of morphisms stable under pullback and composition, and including all isomorphisms. The symmetric monoidal $\infty$-category of correspondences $\mathrm{Corr}(C,E)$ has as its objects the objects in $C$, and has as its morphisms the correspondences in $C$, i.e. for objects $X$ and $Y$ of $C$ a morphism from $X$ to $Y$ is given by an object $W$ of $C$ together with maps

  $$
    \array{
      && W
      \\
      & \mathllap{^f}\swarrow && \searrow\mathrlap{^g}
      \\
      X &&&& Y
    }
  $$

where $g\in E$. The symmetric monoidal structure comes from the one on $C$. 
\end{definition}

\begin{definition}
Let $\mathrm{Cat}_{\infty}$ be the $\infty$-category of $\infty$-categories. A *3-functor formalism* is a lax symmetric monoidal functor
$$\mathcal{D}:\mathrm{Corr}(C,E)\to \mathrm{Cat}_{\infty}$$
\end{definition}

The above definition formalizes three of the functors in the 6-functor formalism. The derived tensor product comes from the lax symmetric monoidal structure, $f^{*}$ comes from the image of the correspondence $Y\xleftarrow{f}X=X$, and $f_{!}$ comes from the image of the correspondence $X=X\xrightarrow{f}Y$.

\begin{definition}
A *6-functor formalism* is a 3-functor formalism for which $-\otimes A$, $f^{*}$, and $f_{!}$ admit right adjoints.
\end{definition}

## Properties

### Relation to motivic homotopy theory

The [[initial object]] in the [[(infinity,2)-category]] of functors to [[stable (infinity,1)-categories]] which satisfy the _six  operations_ formalism (and a bit more, such that [[motivic homotopy theory|A1-homotopy invariance]]) is _[[stable motivic homotopy theory]]_. See there for more.

## Related concepts

* [[Grothendieck duality]], [[Verdier duality]]

[[!include twisted generalized cohomology in linear homotopy type theory -- table]]

## References

General abstract discussion:

* [[Halvard Fausk]], [[Po Hu]], [[Peter May]],  *Isomorphisms between left and right adjoints*, Theory and Applications of Categories, **11** 4 (2003) 107-131 &lbrack;[tac:11-04](http://www.tac.mta.ca/tac/volumes/11/4/11-04abs.html), [pdf](http://www.tac.mta.ca/tac/volumes/11/4/11-04.pdf)&rbrack;

* [[Roy Joshua]], _Grothendieck-Verdier duality in enriched symmetric monoidal $t$-categories_ ([[JoshuaDuality.pdf:file]])

* [[Paul Balmer]], [[Ivo Dell'Ambrogio]], [[Beren Sanders]], *Grothendieck-Neeman duality and the Wirthm&#252;ller isomorphism*, Compositio Math. **152** (2016) 1740-1776 &lbrack;[arXiv:1501.01999](http://arxiv.org/abs/1501.01999), [doi:10.1112/S0010437X1600

[... 正文截断于 6000 字符 ...]
