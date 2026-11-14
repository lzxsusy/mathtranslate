# vector bundle

url: https://ncatlab.org/nlab/show/vector+bundle
last_revised: 2025-10-21
---

#### Bundles
+-- {: .hide}
[[!include bundles - contents]]

# Vector bundles
* table of contents

## Idea

Given some context of [[geometry]], then a _vector bundle_ is a collection of [[vector spaces]] that varies in a geometric way over a given base [[space]] $X$: over each [[generalized element|element]] $x \in X$ there is a [[vector space]] $V_x$, called the _[[fiber]]_ over $x$, and as $x$ varies in $X$, the fibers vary along in a geometric way. One also says that vector bundles are _[[fiber bundles]]_ whose fiber carries [[vector space]]-structure. Hence the theory of vector bundles is _parameterized_ [[linear algebra]]. The vector bundles over a fixed base $X$ form a category [[Vect(X)|$VectBund_X$]], and as the base space is allowed to vary these fit into a global category [[VectBund]]. 

For example

* in [[topology]] a _[[topological vector bundle]]_ is a collection of [[vector spaces]] which "vary continuously" over a [[topological space]] $X$,

* in [[differential geometry]] a _[[differentiable vector bundle]]_ is a collection of vector space which "varies differentiably" over a [[differentiable manifold]], 

* in [[algebraic geometry]] an _[[algebraic vector bundle]]_ is a collection of vector spaces which vary algebraically over a [[scheme]].

and so on.

One requires that "locally", on small enough patches of the base space $X$, the variation of the fibers is constant up to isomorphism (one says the vector bundle is "locally trivial"), but the key point of vector bundles is that there may be non-trivial structure in how the collection of vector spaces "globally glues together".

For example if $X = S^1$ is the [[circle]] regarded as a [[topological space]] in the standard way, and if we consider [[real vector spaces]], then there are up to [[isomorphism]] two different $\mathbb{R}$-vector bundles over $S^1$ whose [[fibers]] look like the 1-dimensional real vector space $\mathbb{R}$ itself, namely 

1. the [[cylinder]] 

   <img src="https://ncatlab.org/nlab/files/cylinder.jpg" width="190">

1. the [[Möbius strip]]: 

   <img src="https://ncatlab.org/nlab/files/moebiusstrip.jpg" width="200">

(In these pictures each vertical interval is to be thought of as a stand-in for a copy of the [[real line]] $\mathbb{R}$.)

Clearly for the cylinder nothing special happens to the fibers as one moves around the circle (one says this is a _trivial vector bundle_) while the M&#246;bius strip is "locally trivial" but globally has a twist: as one moves once around the circle the original fiber comes back identified with its reflection at the origin.

<div style="float:right;margin:0 10px 10px 0;">
<img src="https://ncatlab.org/nlab/files/TangentSpaceToSphere.png" width="250"> 
<blockquote>
  graphics grabbed from <a href="Hatcher">Hatcher</a>
</blockquote>
</div>

An important class of examples of vector bundles are [[tangent bundles]] of [[differentiable manifolds]] $X$. Here the [[vector space]] at each point of $X$ is the [[tangent space]] of that point, the space of all [[tangent vectors]] based at that point. The graphics on the right shows one of the tangent space of the [[2-sphere]].

Dually, given an [[embedding of differentiable manifolds]] into a [[Euclidean space]], then the [[normal vectors]] to the tangent bundle span a vector bundle called the _[[normal bundle]]_ of the embedding.

All the usual operations on [[finite dimensional vector spaces]] in [[linear algebra]] generalize to vector bundles by applying them [[fiber]]-wise. For instance there is [[direct sum of vector bundles]] and the [[tensor product of vector bundles]] over the same base space.

To the extent that the base [[space]] $X$ is encoded in its [[algebra of functions]] (tautologically in [[algebraic geometry]] or via [[Gelfand duality]] in [[topology]]), the [[Serre-Swan theorem]] asserts that vector bundles over $X$ are equivalently encoded in the [[projective modules]] over these algebras constituted by their [[sections]].

Vector bundles have various applications and uses:

1. their [[Grothendieck group]] under [[direct sum of vector bundles]] yields [[topological K-theory]], an interesting [[generalized (Eilenberg-Steenrod) cohomology theory]];

1. a [[reduction of the structure group]] of vector bundles encodes actual [[geometry]] on the base space; when applied to [[tangent bundles]] such _[[G-structures]]_ on vector bundles encode for instance [[orthogonal structure]], [[Riemannian geometry]], [[complex geometry]], [[symplectic geometry]], [[conformal geometry]] etc. (in general: [[Cartan geometry]]); when applied to [[normal bundles]] these [[G-structures]] give rise, via [[Thom's theorem]], to [[Thom spectra]] and [[cobordism theory]];

1. equipping differentiable vector bundles with [[connection on a vector bundle]] is the basis for [[Chern-Weil theory]] and for the application of vector bundles in [[physics]], where they model [[gauge fields]] and [[instanton sectors]]; see also at _[[fiber bundles in physics]]_.

## Definition

### Standard

See at _[[topological vector bundle]]_

### Sheaf-theoretic version

Vector bundles can also be defined via [[sheaf and topos theory|sheaf theory]], which permits easy transport to general [[Grothendieck toposes]]. Let $Sh(X)$ be the [[category]] of ([[set]]-valued) [[sheaf|sheaves]] on $X$. The sheaf of continuous local sections of the product projection 

$$X \times \mathbb{R} \to X$$ 

forms a [[local ring]] object $R$; when interpreted in the [[internal logic]] of $Sh(X)$, it is the Dedekind [[real numbers object]]. Then, according to a [[Serre-Swan theorem|theorem of Richard Swan]], in its sheaf-theoretic incarnation a vector bundle is the same thing as a [[projective module|projective R-module]]. 

* A theorem of Kaplansky states "every [[projective module]] over a [[local ring]] is [[free module|free]]". When interpreted in [[sheaf semantics]] ([[Kripke-Joyal semantics]]), the [[existential quantifier]] implicit in "free" is interpreted _locally_, so we

[... 正文截断于 6000 字符 ...]
