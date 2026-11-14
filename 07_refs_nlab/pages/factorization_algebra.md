# factorization algebra

url: https://ncatlab.org/nlab/show/factorization+algebra
last_revised: 2026-08-16
---

#### Higher algebra
+--{: .hide}
[[!include higher algebra - contents]]

\tableofcontents

## Idea

A _factorization algebra_ is an [[algebra over an operad]] where the [[operad]] in question is like the [[little disk operad]], but with each disk embedded into a given [[manifold]] $X$.

This way a factorization algebra is an assignment of a [[chain complex]] $V_D$ to each [[ball]] $D \subset X$ embedded in $X$, and for each collection of non-intersecting embedded balls $D_1 , \cdots, D_n \subset D \subset X$ sitting inside a bigger embedded ball $D$ in $X$ a morphism

$$
  V_{D_1} \otimes V_{D_2} \otimes \cdots \otimes V_{D_n} \to V_{D}
$$

such that composition of such operations is suitably respected.

In Euclidean ([[Wick rotation|Wick rotated]]) [[field theory]] factorization algebras serve to axiomatize the [[operator product expansion]].

## Definition

### Prefactorization algebra

+-- {: .num_defn}
###### Definition

For $X$ a [[topological space]] write $Fact_X$ be the colored [[operad]] in [[Set]] whose

* [[object]]s are the [[connected]] [[open subset]]s of $X$;

* the [[hom-set]] $Fact_X(\{U_i\}_i, V)$ is the singleton precisely if the
  $U_i$ are all in $V$ and are pairwise disjoint and is the [[empty set]] otherwise.

This specifies composition uniquely. 

These definitions appear in [Costello & Gwilliam](#CostelloGwilliam).

### Factorization algebras

+-- {: .num_defn #FactorizingCover}
###### Definition

For $X$ a [[topological space]] and $U \subset X$ an [[open subset]], an [[open cover]] $\{U_i \hookrightarrow U\}_{i \in I}$ is called a **factorizing cover** if for every [[finite set]] of points $\{x_1, \cdots, x_k\} \subset U$ there is a finite subset $\{U_{i_j}\}_{j \in J \subset I} $ of pairwise disjoint open subsets such that each point is contained in their union.

+-- {: .num_defn}
###### Notation

For a factorizing cover $\{U_i \to U\}_{i \in I}$ write $P I$ for the set of finite subsets $\alpha \subset I$ such that for $j,j' \in \alpha$ we have $U_j \cap U_{j'} = \emptyset$. 

Given a [prefactorization algebra](#PrefactorizationAlgebra) $\mathcal{F}$ and $\alpha \in P I$ write 

$$
  \mathcal{F}(\alpha) := \otimes_{j \in \alpha}  \mathcal{F}(U_j)
$$

and for $\alpha_1, \cdots, \alpha_k \in P I$ write

$$
  \mathcal{F}(\alpha_1, \cdots, \alpha_k) = 
    \bigotimes_{(j_1, \cdots, j_k) \in \alpha_1 \times \cdots \times \alpha_k}
    \mathcal{F}(U_{j_1} \cap \cdots \cap U_{j_k})
  \,.
$$

For each $1 \leq i \leq k$ there is a canonical morphism

$$  
  p_i : \mathcal{F}(\alpha_1,\cdots, \alpha_k)
  \to 
   \mathcal{F}(\alpha_1, \cdots, \alpha_{i-1}, \alpha_{i+1}, \cdots, \alpha_k)
  \,.
$$

These definitions appear [here](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.382.8322&rep=rep1&type=pdf).

See also at _[[cosheaf]]_.

### Homotopy factorization algebras

Let now $(C,\otimes)$ specifically be a [[category of chain complexes]].

+-- {: .num_defn}
###### Definition

A  [prefactorization algebra]{#PrefactorizationAlgebra} $\mathcal{F} : Fact_X \to End(X)$ is a **homotopy factorization algebra** if for all factorizing covers $\{U_i \to U \subset X\}_{i \in I}$ the canonical morpshim

$$
  \bigoplus_{k \geq 0} \bigoplus_{\alpha_1, \cdots, \alpha_k \in P I}
   \mathcal{F}(\alpha_1, \cdots, \alpha_k)[k-1]
   \to 
  \mathcal{F}(U)
$$

is a [[quasi-isomorphism]], where the [[differential]] on the left is defined by (...).

These definitions appear [here](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.382.8322&rep=rep1&type=pdf).

## Examples

* [[beta-gamma system]]

## Related concepts

Factorization algebras have some similarity with 

* [[Hochschild homology]];

* [[blob homology]], [[factorization homology]], [[topological chiral homology]];

* [[local net]]s in [[AQFT]].

* [[chiral algebra]], [[vertex operator algebra]]

* [[nonabelian Poincaré duality]]
  

[[!include Isbell duality - table]]

## References

* {#CostelloGwilliam} [[Kevin Costello]], [[Owen Gwilliam]]: *Factorization algebras in quantum field theory* &lbrack;[[CostelloGwilliam-FactorizationAlgebras.pdf:file]]&rbrack;

The notion of factorization algebra may be regarded as a slight variation on the concept _[[chiral algebra]]_ originally introduced in

* [[Alexander Beilinson]], [[Vladimir Drinfeld]]:  _[[Chiral Algebras]]_.

A definition formulated genuinely in  [[Higher Algebra]] appears in section 4.1 _Topological Chiral Homology_ of

* [[Jacob Lurie]], _[[On the Classification of Topological Field Theories]]_

This discusses how locally constant factorization algebras obtained from [[En-algebras]] induce [[extended quantum field theory|extended]] [[FQFTs]].

A fairly comprehensive account of factorization algebras as a formalization of [[perturbation theory|perturbative]] [[quantum field theory]] (see at _[[factorization algebra of observables]]_) is in 

* [[Kevin Costello]], [[Owen Gwilliam]], _[[Factorization algebras in perturbative quantum field theory]]_ 

* [[Owen Gwilliam]], _Factorization algebras and free field theories_ PhD thesis ([[GwilliamThesis.pdf:file]])

* [[Owen Gwilliam]], [[Kasia Rejzner]], _Comparing nets and factorization algebras of observables: the free scalar field_, [arxiv:1711.06674](https://arxiv.org/abs/1711.06674)

and the beginnings of

* {#Costello11} [[Kevin Costello]], *Notes on supersymmetric and holomorphic field theories in dimension 2 and 4*, talk at *[Geometric and Algebraic Structures in Mathematics](https://www.math.stonybrook.edu/dennisfest/)*, Stony Brook (2011) &lbrack;[arXiv:1111.4234](https://arxiv.org/abs/1111.4234)&rbrack;

* [[Kevin Costello]], [[Claudia Scheimbauer]], _Lectures on mathematical aspects of (twisted) supersymmetric gauge theories_, pp. 57-88 in: *Mathematical aspects of QFTs*, Springer (2015)

Lecture notes:

* [[Kevin Costello]] (with [[Owen Gwilliam]]), _Factorization algebras in perturbative quantum field theory_ in [[Oberwolfach Workshop, June 2009 -- Strings, Fields, Topology|Strings, Field, Topology]]

[... 正文截断于 6000 字符 ...]
