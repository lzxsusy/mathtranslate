# p-adic number

url: https://ncatlab.org/nlab/show/p-adic+number
last_revised: 2024-08-06
---

#### Algebra
+--{: .hide}
[[!include higher algebra - contents]]

# $p$-adic numbers
* table of contents

## Idea

For $p$ any [[prime number]], the _$p$-adic [[numbers]]_ (or _$p$-adic rational numbers_, for emphasis) form a [[field]] $\mathbb{Q}_p$ that [[complete field|completes]] the field of [[rational numbers]] with respect to a [[metric]], called the $p$-adic metric. As such they are analogous to [[real numbers]]. A crucial difference is that the reals form an [[archimedean field]], while the $p$-adic numbers form a [[non-archimedean field]].

Fields of $p$-adic numbers play a role in non-archimedean [[analytic geometry]] that is analogous to the role of the [[real numbers]]/[[Cartesian spaces]] in ordinary [[differential geometry]]. 

Moreover, as such they serve as an approximation technique in [[arithmetic geometry]] over [[prime fields]] $\mathbb{F}_p$ (see e.g. [Lubicz](#Lubicz)).

There have long been speculations (see the references [below](#ReferencesApplications)) that this must mean that $p$-adic numbers also play a central role in the description of [[physics]], see _[[p-adic physics]]_.

## Definition

We first recall the definition and construction of the [[p-adic integers]]

* [Recollection of the p-adic integers](#RecollectionOfPAdicIntegers)

and then consider

* [The p-adic numbers proper](#PAdicNumbersProper)

### Recollection of the $p$-adic integers
 {#RecollectionOfPAdicIntegers}

Let $\mathbf{Z}$ be the [[ring]] of [[integers]] and for every $q\neq 0$, $q\mathbf{Z}$ its ideal consisting of all integer multiples of $q$, and $\mathbf{Z}/q\mathbf{Z}$ the corresponding [[quotient]], the ring of residues mod $q$.

Let now $p\in \mathbf{Z}_+$ be a [[prime number]]. Then for any two positive integers $n\geq m$ there is an inclusion $p^n \mathbf{Z}\subset p^m\mathbf{Z}$ which induces the canonical homomorphism of quotients $\phi_{n,m}:\mathbf{Z}/p^n\mathbf{Z}\to \mathbf{Z}/p^m\mathbf{Z}$. These homomorphisms for all pairs $n\geq m$ form a family closed under composition, and in fact a category, which is in fact a poset, and moreover a directed system of (commutative unital) rings. The __ring of [[p-adic integers]]__ $\mathbf{Z}_p$ is the (inverse) [[limit]] of this directed system (in the [[category]] [[Ring]] of [[rings]]).

Regarding that the rings in the system are finite, it is clear that the underlying set of $\mathbf{Z}_p$ has a natural topology as a [[profinite space|profinite]] ([[Stone space|Stone]]) space and it is in particular a [[compact space|compact]] [[Hausdorff topological space|Hausdorff topological ring]]. More concretely, $\mathbf{Z}_p$ is the closed (hence compact) subspace of the cartesian product $\prod_{n} \mathbf{Z}/p^n\mathbf{Z}$ of discrete topological spaces $\mathbf{Z}/p^n\mathbf{Z}$ (which is by the [[Tihonov theorem]] compact Hausdorff) consisting of [[thread]]s, i.e. sequences of the form $x = (...,x_n,...,x_2,x_1)$ with $x_n\in p^n\mathbf{Z}$ and satisfying $\phi_{n,m}(x_n) = x_m$.

The kernel of the projection $pr_n: \mathbf{Z}_p\to\mathbf{Z}/p^n\mathbf{Z}$, $x\mapsto x_n$ to the $n$-th component (which is the corresponding projection of the limiting cone) is $p^n\mathbf{Z}_p\subset\mathbf{Z}_p$, i.e. the sequence

$$
0 \longrightarrow \mathbf{Z}_p\stackrel{p^n}\longrightarrow \mathbf{Z}_p\longrightarrow \mathbf{Z}/p^n\mathbf{Z} \longrightarrow 0
$$

is an [[exact sequence]] of [[abelian groups]], hence also $\mathbf{Z}_p/p^n\mathbf{Z}_p\cong \mathbf{Z}/p^n\mathbf{Z}$.

An element $u$ in $\mathbf{Z}_p$ is invertible (and called a $p$-adic unit) iff $u$ is not divisible by $p$. 

Let $U\subset\mathbf{Z}_p$ be the group of all invertible elements in $\mathbf{Z}_p$. Then _every element $x\in \mathbf{Z}_p$ can be uniquely written as $s= u p^n$ with $n\geq 0$ and $u\in U$_. The correspondence $x\mapsto n$ defines a [[discrete valuation]] $v_p:\mathbf{Z}_p\to \mathbf{Z}\cup\{\infty\}$ called the  [[p-adic valuation]] and $n$ is said to be the $p$-adic valuation of $x$. Of course, $v_p(0)=\infty$ as required by the axioms of valuation. The [[norm]] induced by the valuation is (up to equivalence) given by ${|x|}_p = p^{-v_p(x)}$, and this in turn induces a metric 

$$
d(x,y) = {|x-y|}_p,
$$

making the ring $\mathbf{Z}_p$ a [[complete metric space]] and in fact a completion of $\mathbf{Z}$, in that $d$ is a complete [[metric]], and $\mathbf{Z}$ is dense in it. 

Concretely, a $p$-adic integer $x$ may be written as a base-$p$ expansion 

$$x = \sum_{n \geq 0} a_n p^n$$ 

with $a_n \in \{0, 1, \ldots, p-1\}$. Addition and multiplication are performed with [[carrying]] as in ordinary base-$p$ arithmetic, carried infinitely far to the left if $x$ is written as $\ldots a_n a_{n-1} \ldots a_1 a_0$. 

#### As an endomorphism ring 

Algebraically, the ring of $p$-adic integers is isomorphic to the endomorphism ring $\hom(\mathbf{Z}(p^\infty), \mathbf{Z}(p^\infty))$ where $\mathbf{Z}(p^\infty)$ is the [[Pruefer group|Prüfer group]] $\mathbf{Z}(p^\infty) \coloneqq \mathbb{Z}[1/p]/\mathbb{Z}$. In particular, $\mathbf{Z}(p^\infty)$ is tautologically a $\mathbf{Z}_p$-module. 

Relatedly, the additive group of $p$-adic integers is [[Pontrjagin duality|Pontrjagin dual]] to $\mathbf{Z}(p^\infty)$. Observe that $\mathbf{Z}(p^\infty)$ embeds in $S^1$ as the set of all [[root of unity|roots of unity]] of order $p^n$, and that every character $\chi: \mathbf{Z}(p^\infty) \to S^1$ factors through this embedding $\mathbf{Z}(p^\infty) \hookrightarrow S^1$. 

### The $p$-adic numbers proper
 {#PAdicNumbersProper}

The __field of $p$-adic numbers__ $\mathbf{Q}_p$ is the [[field of fractions]] of the [[p-adic integers]] $\mathbf{Z}_p$. The $p$-adic valuation $v_p$ extends to a discrete valuation, also denoted $v_p$ on $\mathbf{Q}_p$. Indeed, it is still true for all $x\in \mathbf{Q}_p$ that they can be uniquely written in the form $p^n u$ where $u\in U$ (the same group $U$ as before), but now one needs to allow $n\in \mathbf{Z}$. One defines the metric on $\mathbf{Q}_

[... 正文截断于 6000 字符 ...]
