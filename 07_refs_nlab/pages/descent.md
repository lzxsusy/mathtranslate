# descent

url: https://ncatlab.org/nlab/show/descent
last_revised: 2024-09-12
---

#### Locality and descent
+--{: .hide}
[[!include descent and locality - contents]]

If $S$ is a [[Verdier site]] then every such hypercover $Y \to X$ has a refinement by a hypercover which is cofibrant with respect to the projective global [[model structure on simplicial presheaves]]. We shall from now on make the assumption that the hypercovers $Y \to X$ we discuss are cofibrant in this sense. These are called _split hypercovers_. (This works in many cases that arise in practice, see the discussion after [DHI, def. 9.1](http://hopf.math.purdue.edu//Dugger-Hollander-Isaksen/hypspre.pdf#page=29).)

+-- {: .un_prop}
###### Proposition

The objects of $Sh_{(\infty,1)}(S)$ -- i.e. the fibrant objects with respect to the projective model structure on $[S^{op}, SSet]$ -- are precisely those objects $A$ of $PSh_{(\infty,1)}(S)$ -- i.e. [[Kan complex]]-valued simplicial presheaves -- which
**satisfy descent for all split hypercovers**, i.e. those for which for all split hypercover $f : Y \to X$ in $[S^{op}, SSet]$ we have that
$$
  [S^{op}, SSet](X,A) \stackrel{\simeq}{\to}
  [S^{op}, SSet](Y,A)
$$
is a [[model structure on simplicial sets|weak equivalence of simplicial sets]].

Notice that by the [[co-Yoneda lemma]] every simplicial presheaf $F : S^{op} \to SSet$, which we may regard as a presheaf $F : \Delta^{op}\times S^{op} \to Set$, is isomorphic to the [[weighted limit|weighted colimit]] 

$$
    F \simeq colim^\Delta F_\bullet
$$

which is equivalently the [[end|coend]]

$$
  F \simeq \int^{[n] \in \Delta} \Delta^n \cdot F_n
  \,,
$$ 

where $F_n$ is the Set-valued presheaf of $n$-cells of $F$ regarded as an $SSet$-valued presheaf under the inclusion $Set \hookrightarrow SSet$, and
where the [[SimpSet|SSet]]-weight is the canonical cosimplicial simplicial set $\Delta$, i.e. for all $X \in S$

$$
  F : X \mapsto \int^{[n] \in \Delta} \Delta^n \times F(X)_n
  \,.
$$

In particular therefore for $A$ a [[Kan complex]]-valued presheaf the descent condition reads

$$
  [S^{op}, SSet](X,A) \stackrel{\simeq}{\to}
  [S^{op}, SSet](colim^\Delta Y_\bullet,A)
  \simeq
  lim^\Delta [S^{op}, SSet](Y_\bullet,A)
  \,.
$$

With the shorthand notation introduced above the **descent condition** finally reads, for all global-injective fibrant simplicial presheaves $A$ and hypercovers $U \to X$:

$$
  A(X) \stackrel{\simeq}{\to} lim^\Delta A(Y_\bullet)
  \,.
$$

The right hand here is often denoted $Desc(Y_\bullet \to X, A)$, in which case this reads

$$
  A(X) \stackrel{\simeq}{\to} Desc(Y_\bullet \to X, A)
  \,.
$$

## Descent for strict $\omega$-groupoid valued presheaves 

While simplicial sets are a very convenient model for general reasoning about higher weak categories and [[∞-groupoids]], often concrete computations in particular with $(\infty)$-groupoids are more convenient in the context of more strictified models. 

Notably, by the generalized [[Dold-Kan correspondence]] the [[oriental|$\omega$-nerve]] injects [[crossed complex]]es -- nonabelian generalizations of [[chain complex]]es of abelian groups which are equivalent to [[strict ∞-groupoids]] -- to simplicial sets

$$
  CrsCmplx \stackrel{\simeq}{\to}
  Str \omega Grpd \stackrel{N}{\to}
  SSet
  \,.
$$

Since, for instance, something as simple as an abelian group $A$, regarded as a complex of groups in degree $n$ (hence as an $n$-group), is already a rather involved object to understand under the nerve operation, 

_it is desirable to have a means to control descent for simplicial presheaves which happen to factor through the $\omega$-nerve directly in the context of $Str \omega Cat$._

In his work on descent

* Ross Street, _Categorical and combinatorial aspects of descent theory_, [arXiv:math.CT/0303175](http://arxiv.org/abs/math.CT/0303175)

Ross Street considered presheaves with values in [[strict ∞-categories]]

$$
  A : S^{op} \to Str \omega Cat
$$

and declared the descent $\omega$-category with respect to a simplicial object $Y_\bullet : \Delta^{op} \to S$ to be the [[weighted limit]] in $Str\omega-Cat$-[[enriched category theory]]

$$
  lim^{F \Delta} A(U^\bullet) 
  \,,
$$

where $O := F \Delta : \Delta \to Str \omega Cat$ are the [[orientals]], i.e. the free $\omega$-categories on the simplicial [[simplex|simplices]]

$$
  O = F \circ \Delta
  \,,
$$

where $F : SSet \to Str\omega Cat$ is the [[right adjoint]] to the [[oriental|∞-nerve]] $N : Str \omega Cat \to SSet$.

The two prescriptions 

$$
 \array{
  lim^\Delta N A(U^\bullet) & in SSet
  \\
  \\
  lim^{F \Delta} A(U^\bullet) & in Str \omega Grpd
 }
$$

have a very similar appearance. The following theorem asserts if and when they are actually equivalent.

+-- {: .un_theorem }
###### Theorem (Dominic Verity)

There exists a canonical comparison map

$$
  N(Desc_{Street}(U^\bullet, A))
  :=
  N(lim^{F \Delta} A(U^\bullet))
  \;\;\;\stackrel{\;\;\;\;\;\;\;\;\;}{\hookrightarrow}\;\;\;
  Desc_{simp}(U^\bullet, N \circ A)
  :=
  holim_\bullet N(A(U^\bullet))
  \,.
$$

This is a [[model structure on simplicial sets|weak equivalence]] of [[Kan complex]]es if the cosimplicial simplicial set $N(A(U^\bullet))$ is [[Reedy category|Reedy fibrant]].

## Descent in terms of gluing conditions {#AsGluing}

We unwrap the expression 

$$
  lim^\Delta A(Y_\bullet)
$$

for the descent data for a presheaf $A$ with respect to a (hyper)cover $Y \to X$

This [[weighted limit]] (whether taken in $SSet$- or in $Str \omega Cat$-[[enriched category theory]]) is given by the [[end|coend]]

$$
  lim^W\Delta A(Y_\bullet)
  \simeq
  \int^{[n] \in \Delta} [\Delta^n, A(Y_n)]
  \,.
$$

Unwrapping what this means one finds that an object/vertex of this is a choice of $n$-simplex in each $A(Y_n)$, subject to conditions which say that the boundary of this $n$-simplex must be obtained from pullback of $A$ along the maps $Y_n \to Y_{[n-1]}$ of the $(n-1)$-simplex in $A(Y_{n-1})$

Namely an object in 

$
  lim^W\Delta A(Y_\bullet)
  \simeq
  \int^{[n] \in \Delta} [\Delta^n, A(Y_n)]
$

is a commuting diagram

$$
  \ar

[... 正文截断于 6000 字符 ...]
