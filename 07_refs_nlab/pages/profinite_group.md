# profinite group

url: https://ncatlab.org/nlab/show/profinite+group
last_revised: 2025-07-01
---

#### Group Theory
+-- {: .hide}
[[!include group theory - contents]]

Equivalently:

+-- {: .num_defn}
###### Definition

A _profinite group_ is an [[internalization|internal]] [[group]] object in the [[category]] of [[profinite sets]].

### Inverse limit form

+-- {: .num_defn}
###### Definition

A   __profinite group__ is an [[inverse limit]] of a system of finite groups.

The finite groups are considered as compact [[discrete groups|discrete]] [[topological groups]] and so the inverse limit, as a closed subspace of the compact space that is the product of all those finite groups has the _inverse limit topology_, hence is, as is said above, a compact Hausdorff, totally disconnected group.

Historically a motivating example was:

+-- {: .num_example}
###### Example

The absolute [[Galois group]] of a [[number field]] is profinite.

+-- {: .num_example}
###### Example

In [[SGA1]], Grothendieck defined the [[algebraic fundamental group]] of a [[scheme]] as a profinite group.  (This is linked with his work on [[pro-representable functor|pro-representable functors]].)

## Properties

* The category of profinite groups has nice 'exactness' properties. The [[projective limit]] of a system of profinite groups is an [[exact functor]], unlike its behaviour on groups themselves. To extend this behaviour beyond (pro)finite groups sometimes pro-[[localic groups]] have been used; see [[progroup]].

* [[profinite completion of a group|Profinite completions]] have been extended from groups to homotopy types for the analysis of finitary properties of the homotopy type. Various constructions in algebraic geometry lead  naturally to [[profinite homotopy type|profinite homotopy types]].

* Subclasses of profinite groups are extensively studied.  For instance, if $p$ is a prime number, a pro-$p$ group is a pro-object in the category of $p$-groups.

* Pro-p analytic groups have been introduced as an analogue of Lie groups, with certain rings of formal power series replacing differentiable functions.

## Analogues of the group algebra construction

If $G$ is a profinite or pro-p group, the best replacement for the group algebra of $G$  in this context will be  a [[pseudocompact ring|pseudocompact algebra]].  This is the completed group algebra defined as the inverse limit of the ordinary group algebras $k[G/U]$ as $U$ varies through the open normal subgroups of $G$. Here the coefficient ring $k$ will be chosen itself to be a [[pseudocompact ring]]. As finite rings are pseudocompact, one of the most appropriate choices will be a $k = \mathbb{Z}_p$, the field of $p$ elements; (see the book by Dixon et al, below).

## Related concepts

* [[finite group]], [[finitely generated group]]

* [[pro-object]]

* [[profinite completion of a group]]

* [[profinite set]]

* [[profinite space]]

* [[pro-etale site]]

* [[compact Hausdorff rings are profinite]] 

## References

Introductory lectures include

* [[Hendrik Lenstra]], _Profinite groups_ ([pdf](http://websites.math.leidenuniv.nl/algebra/Lenstra-Profinite.pdf))
 {#Lenstra}

A survey is given in

* Alexander Lubowsky, _Book review_, BAMS 38(4), pp. 475-479, ([pdf](https://www.ams.org/journals/bull/2001-38-04/S0273-0979-01-00914-4/))

A fairly recent textbook is

* L. Ribes and P. Zalesskii, 2000, _Profinite groups_, volume 40 of Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge, Springer-Verlag, 
Berlin. 

For the connections with, amongst other things, Galois theory from a categorical viewpoint:

* [[Francis Borceux]], [[George Janelidze]], _[[Galois Theories]]_, Cambridge Studies in Advanced Mathematics __72__, Cambridge University Press, 2001.

For the corresponding 'analytic theory' see:

* J. Dixon, M. du Sautoy, A. Mann and D. Segal, _Analytic pro-p groups_, volume 61 of Cambridge Studies in Advanced Mathematics, 
Cambridge Univ. Press 1999. 

A standard starting point for the study of the homological properties of the completed group algebra of a profinite group is 

* A. Brumer, _Pseudocompact algebras, profinite groups and class formations_,  J. Algebra __4__ (1966) 442-470, [MR202790](http://www.ams.org/mathscinet-getitem?mr=202790), <a href="http://dx.doi.org/10.1016/0021-8693(66)90034-2">doi</a>
