# ring of adeles

url: https://ncatlab.org/nlab/show/ring+of+adeles
last_revised: 2025-07-01
---

#### Algebra
+--{: .hide}
[[!include higher algebra - contents]]

This definition has various equivalent reformulations which are often useful.

+-- {: .num_remark #ProfiniteIntegersAsProductOverpAdics}
###### Remark

By [this proposition](profinite+completion+of+the+integers#AsProductOverAlsoPAdicIntegers) we have that the [[profinite completion of the integers]] is equivalently the [[product]] of all [[p-adic integers]] as $p$ ranges over all [[prime numbers]] 

$$
  \hat \mathbb{Z} \simeq \underset{p\;prime}{\prod} \mathbb{Z}_p
$$ 

Using this in def. \ref{RingOfAdeles} says that the ring of integral adeles is the product

$$
  \mathbb{A}_{\mathbb{Z}} 
    \simeq 
   \mathbb{R} \times
  \underset{p\;prime}{\prod} \mathbb{Z}_p
  \,.
$$

+-- {: .proof}
###### Proof

By remark \ref{ProfiniteIntegersAsProductOverpAdics} the 
[[tensor product]] to be computed is equivalently

$$
  \mathbb{A}_{\mathbb{Q}}
  \simeq
  \mathbb{Q}\otimes_{\mathbb{Z}}
   \left(
     \mathbb{R} \times
    \underset{p \; prime}{\prod} \mathbb{Z}_p
   \right)
  \,.
$$

Now notice that a [[natural number]] $n$ is a [[group of units|unit]] in $\mathbb{Z}_p$ if $p$ is not a [[prime factor]] of $n$. 
Therefore for $(a_p) \in \underset{p}{\prod} \mathbb{Z}_p$ and $\frac{c}{d} \in \mathbb{Q}$, then for each of the [[finite number]] of [[prime factors]] $p$ of $d$ the tensor product
element $\frac{c}{d} \otimes_{\mathbb{Z}} a_p \in \mathbb{Q}_p$ contains a non-vanishing negative power of $p$ and is hence not in $\mathbb{Z}_p$, whereas for all $p$ that do not appear as prime factors in $d$ it is.

+-- {: .num_prop} 
###### Proposition 
$\mathbb{A}_\mathbb{Q}$ is a [[locally compact space|locally compact]] [[Hausdorff space|Hausdorff]] commutative ring. In particular, it is complete with respect to its [[uniform space]] structure. 

If one omits the factor of $\mathbb{R} = \mathbb{Q}_\infty$, then one speaks of the _ring of finite adeles_.

$$
  \mathbb{A}_{\mathbb{Q}}^f \coloneqq \underset{p \; prime}{\prod^\prime} \mathbb{Q}_p
  \,.
$$

All of this generalizes to any [[number field]] $k$. 

### For a number field
 {#ForAnyNumberField}

Let 

* $k$ be a [[number field]];

* $\mathcal{O} = \mathcal{O}_k$ the [[ring of integers|ring of]] [[algebraic integers]] in $k$: 

* $P$ be its [[set]] of [[places]] (equivalence classes of [[absolute values]] on $\mathcal{O}$); 

* $S\subset P$ be the set of [[archimedean valuation|archimedean]] places;

* $k_v$ the [[formal completion]] of $k$ at $v\in P$. 

Notice that

* for $v \in S$ then $k_v$ is isomorphic to one of the [[local fields]] $\mathbb{R}$ or $\mathbb{C}$;

* for $v \notin S$ then $k_v$ is a [[local field]] with an open compact subring $\mathcal{O}_v$ consisting of elements of [[norm]] $1$ or less. 

+-- {: .num_defn} 
###### Definition 

For $k$ a [[number field]], the ring of _integral adeles_ $\mathbb{A}_{\mathcal{O}}$ is the [[product]] of the [[profinite completion]] $\widehat{\mathcal{O}}$ with all the archimedean completions, 

$$
  \mathbb{A}_\mathcal{O} 
   \coloneqq 
  \widehat{\mathcal{O}} \times \prod_{v \in S} k_v 
  \,,
$$ 

and the _ring of adeles_ over $k$ is the [[tensor product]] $\mathbb{A}_k \coloneqq k \otimes_\mathcal{O} \mathbb{A}_\mathcal{O}$. 

+-- {: .num_defn }
###### Definition

The [[group of units]] of the ring of adeles $\mathbb{A}_k$ is called the group of [[ideles]], denoted $\mathbb{I}_k$.

Reviews includes ([Mathew 10](#Mathew10)). 

In the function field case, where $k$ is a finite extension of $\mathbb{F}_p(T)$, the analogous ring of integers $\mathcal{O}(k)$ is the [[integral closure]] in $k$ of the subring $\mathbb{F}_p[T] \hookrightarrow \mathbb{F}_p(T)$. And analogously, the ring of integer adeles $\mathbb{A}_{\mathcal{O}(k)}$ may be defined to be the product of all the completions of $\mathcal{O}(k)$ over all the places of $k$. This is a compact ring. The restricted direct product above map may then, in parallel with the number field case described above, be described as a tensor product 

$$\mathbb{A}_k = k \otimes_{\mathcal{O}(k)} \mathbb{A}_{\mathcal{O}(k)}$$ 

where the right side is again interpreted as a colimit in the category of topological rings of a diagram consisting of compact topological rings and open inclusions between them. 

## Properties

### Basic results 

+-- {: .num_prop} 
###### Proposition 
Under the natural inclusion $i: k \to \mathbb{A}_k$, the subspace topology on $k$ is discrete, and the quotient topology on $\mathbb{A}_k/k$ is compact. 

+-- {: .num_prop} 
###### Proposition 
The additive group $\mathbb{A}_k$ is [[Pontrjagin duality|Pontrjagin self-dual]] in the sense that the map $\phi: \mathbb{A}_k \to \mathbb{A}_k^\wedge$ induced from the pairing $\langle-, -\rangle$ is an isomorphism onto the character group. 

### Function field analogy
 {#FunctionFieldAnalogy}

Via the [[function field analogy]] one may understand any [[number field]] or [[function field]] $F$ as being the [[rational functions]] on an [[arithmetic curve]] $\Sigma$. Under this identification the  ring of adeles $\mathbb{A}_F$ of $F$ has the interpretation of being the ring of functions on all punctured [[formal disks]] around all points of $\Sigma$, such that only finitely many of them do not extend to the given point. ([Frenkel 05, section 3.2](#Frenkel05)). This is most manifest in terms of def. \ref{AsRestrictedProduct} above.

This means for instance that the [[general linear group]] $GL_n(\mathbb{A}_F)$ with [[coefficients]] in the ring of adeles has the interpretation as being the [[Cech cohomology|Cech cocycles]] for [[algebraic vector bundles]] of [[rank]] $n$ on an [[algebraic curve]] with respect to any [[cover]] of that curve by the complement of a finite number of points together with the [[formal disks]] around these points. (Notice that for $n = 1$ then $GL_1(\mathbb{A}_F)$ is the [[group of ideles]]). This is part of a standard construction of the [[moduli stack of bundles]] on algebraic curves, see at _[Moduli spa

[... 正文截断于 6000 字符 ...]
