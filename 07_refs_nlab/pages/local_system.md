# local system

url: https://ncatlab.org/nlab/show/local+system
last_revised: 2025-04-10
---

#### Algebraic topology
+--{: .hide}
[[!include algebraic topology - contents]]

* table of contents

## Idea

A _local system_  -- which is short for _local system of [[coefficients]] for [[cohomology]]_ -- is a system of coefficients for [[twisted cohomology]].

Often this is presented or taken to be presented by a [[locally constant sheaf]]. Then cohomology with coefficients in a local system is the corresponding [[sheaf cohomology]].

More generally, we say a _local system_ is a [[locally constant stack]], ... and eventually a [[locally constant ∞-stack]].

Under suitable conditions (if we have [[Galois theory]]) local systems on $X$ correspond to [[functor]]s out of the [[fundamental groupoid]] of $X$, or more generally to [[(∞,1)-functor]]s out of the [[fundamental ∞-groupoid]]. These in turn are equivalently [[flat connections]] (this relation is known as the _[[Riemann-Hilbert correspondence]]_) or generally [[flat ∞-connections]].

## Definitions

A notion of [[cohomology]] exists intrinsically within any [[(∞,1)-topos]]. We discuss local systems first in this generality and then look at special cases, such as local systems as ordinary [[sheaves]].

### General 

For $\mathbf{H}$ an [[(∞,1)-sheaf (∞,1)-topos]], write

$$
  (LConst \dashv \Gamma)
  : 
  \mathbf{H}
   \stackrel{\overset{LConst}{\leftarrow}}{\underset{\Gamma}{\to}}
  \infty Grpd
$$

for the [[terminal object|terminal]] [[(∞,1)-geometric morphism]], where $\Gamma$ is the [[global section]] [[(∞,1)-functor]] and $LConst$ the [[constant ∞-stack]]-functor.

Write $\mathcal{S} := core(Fin \infty Grpd) \in $ [[∞Grpd]] for the [[core]] [[∞-groupoid]] of the [[(∞,1)-category]] of finite $\infty$-groupoids. (We can drop the finiteness condition by making use of a higher [[universe]].) This is canonically a [[pointed object]] $* \to \mathcal{S}$, with points the terminal groupoid.

+-- {: .num_defn}
###### Definition

For $X \in \mathbf{H}$ an [[object]], a **local system** or _[[locally constant ∞-stack]]_ on $X$ is a morphism

$$
  \tilde \nabla \colon X \longrightarrow LConst \mathcal{S}
$$

in $\mathbf{H}$ or equivalently the object in the [[over-(∞,1)-topos]]

$$
  (P \to X) \in \mathbf{H}/X
$$

that is classified by $\tilde \nabla$ under the [[(∞,1)-Grothendieck construction]]

$$
  \array{
    P &\to& LConst \mathcal{Z}
    \\
    \downarrow && \downarrow
    \\
    X &\stackrel{\tilde \nabla}{\to}&  LConst \mathcal{S}
  }
$$

In other words, local systems are [[locally constant ∞-stacks]] or equivalently their classifying [[cocycles]] for [[cohomology with constant coefficients]].

+-- {: .num_defn}
###### Definition

Given a local system $\tilde \nabla : X \to LConst \mathcal{S}$, the cohomology of $X$ with this **local system of coefficients** is 
the intrinsic [[cohomology]] of the [[over-(∞,1)-topos]] $\mathbf{H}/X$:

  $$
    H(X,\tilde \nabla)
    :=
    \mathbf{H}_{/X}(X, P_{\tilde \nabla})
    \,,
  $$

where $P_{\tilde\nabla}$ is the [[homotopy fiber]] of $\tilde \nabla$.

### Sheaf-theoretic case

Local systems can also be considered in abelian contexts. One finds the following version of a local system

+-- {: .num_defn}
###### Definition

A **linear local system** is a [[locally constant sheaf]] on a [[topological space]] $X$ (or manifold, analytic manifold, or algebraic variety) whose stalk is a finite-dimensional [[vector space]]. 

## Related concepts

* [[flat vector bundle]], [[Gauss-Manin connection]]

* [[infinity-local system]]

* [[inner local system]]

* [[simplicial local system]]: within Sullivan's (1977) theory of _Infinitesimal computations in topology_, he refers to 'local systems' several times. This seems to be simplicial in nature. [[simplicial local system|This]] entry explores some of the uses of that notion based on Halperin's lecture notes on minimal models

  * D. Sullivan, _Infinitesimal computations in topology_ ([pdf](http://archive.numdam.org/ARCHIVE/PMIHES/PMIHES_1977__47_/PMIHES_1977__47__269_0/PMIHES_1977__47__269_0.pdf))

* [[twisted cohomology]], [[local coefficient bundle]], [[twisted infinity-bundle]]

## References

An early version of the definition of local system appears in

* [[Norman Steenrod]]: _Homology with local coefficients_, Annals 44 (1943) pp. 610 - 627,

This is before the formal notion of [[sheaf]] was published by [[Jean Leray]].  (Wikipedia's entry on [Sheaf theory](http://en.wikipedia.org/wiki/Sheaf_%28mathematics%29#History) is interesting for its historical perspective on this.)

A definition  appears as an exercise in 

* {#Spanier66} [[Edwin Spanier]], _Algebraic topology_, McGraw Hill (1966), Springer (1982) &lbrack;[doi:10.1007/978-1-4684-9322-1](https://link.springer.com/book/10.1007/978-1-4684-9322-1)&rbrack;

> _A local system on a space $X$ is a [[covariant functor]] from the [[fundamental groupoid]] of $X$ to some [[category]]._ &lbrack;p. 58&rbrack;

Then the first major account with discussion of the relation to [[twisted de Rham cohomology]]:

* {#Deligne70} [[Pierre Deligne]], *Equations différentielles à points singuliers réguliers*, Lecture Notes  Math. **163**, Springer (1970) &lbrack;[publications.ias:355](https://publications.ias.edu/node/355)&rbrack;

Making explicit that instead of the [[fundamental group]] one may use the [[fundamental groupoid]] of the base space:

* [[George W. Whitehead]], p. 257 in: *Elements of Homotopy Theory*, Springer (1978) &lbrack;[doi:10.1007/978-1-4612-6318-0](https://link.springer.com/book/10.1007/978-1-4612-6318-0)&rbrack;

Textbook accounts:

* {#Voisin02} [[Claire Voisin]] (translated by [[Leila Schneps]]), Section I 9.2.1 of: _[[Hodge theory and Complex algebraic geometry]] I_, Cambridge Stud. in Adv. Math. __76, 77__, 2002/3 ([doi:10.1017/CBO9780511615344](https://doi.org/10.1017/CBO9780511615344))

* [[Alexandru Dimca]], Section 2.5 of: *Sheaves in Topology*, Universitext, Springer (2004) $[$[doi:10.1007/978-3-642-18868-8](https://doi.org/10.1007/978-3-642-18868-8)$]$

* [[Tamás Szamuely]], sect

[... 正文截断于 6000 字符 ...]
