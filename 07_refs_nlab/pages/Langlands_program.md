# Langlands program

url: https://ncatlab.org/nlab/show/Langlands+program
last_revised: 2024-03-28
---

#### Langlands correspondence
+--{: .hide}
[[!include Langlands correspondence -- contents]]

* table of contents

## Idea
 {#Idea}

What is called the _Langlands correspondence_ in [[number theory]] ([Langlands 67](#Langlands67)) is first of all a [[conjecture|conjectural]] correspondence (a [[bijection]] subject to various conditions) between 

1. $n$-[[dimensional]] complex [[linear representations]] of the [[Galois group]] $Gal(\bar F/F)$ of a given [[number field]] $F$, and

1. certain [[representations]] -- called _[[automorphic representations]]_ -- of the $n$-dimensional [[general linear group]] $GL_n(\mathbb{A}_F)$ with [[coefficients]] in the [[ring of adeles]] of $F$, arising within the representations given by [[functions]] on the [[double coset space]] $GL_n(F) \backslash GL_n(\mathbb{A}_F)/GL_n(\mathcal{O})$ (where $\mathcal{O} = \prod_v \mathcal{O}_p$ is the [[ring of integers]] of all [[formal completions]] of $F$).

This is motivated from the abelian case ($n=1$), which is fully understood: For $n = 1$ then an $n$-dimensional representation of the [[Galois group]] factors through $GL_1$ and hence through an [[abelian group]]. Therefore, by [[adjunction]], it is equivalently a representation of the [[abelianization]] of the Galois group. The [[Kronecker-Weber theorem]] says that for $F = \mathbb{Q}$, then the abelianized Galois group is the [[idele class group]] $GL_1(\mathbb{Q}) \backslash GL_1(\mathbb{A})$, and hence 1-dimensional representations of the Galois group are equivalently representations of this. Moreover, one finds that for any [[prime number]] $p$, then those representations which are "unramified at $p$" are invariant under the subring of [[p-adic integers]], hence are representations of the double quotient group $GL_1(\mathbb{Q}) \backslash GL_1(\mathbb{A})/GL_1(\mathbb{Z}_p)$. More generally, the [[Artin reciprocity law]] says that for any [[number field]] $K$ there is an [[isomorphism]] between $GL_1(K) \backslash GL_1(\mathbb{A}_K)/GL_1(\mathcal{O}_K)$ and the [[abelianization]] of the [[Galois group]] $Gal(\bar K/K)$.

$\,$

Moreover:

{#Conjecture1} **Conjecture 1** To each such [[automorphic representation]] $\pi$ is associated an [[L-function]] -- the _[[automorphic L-function]]_ $L_\pi$ -- and in generalization of [[Artin reciprocity]] the conjecture of Langlands is that the [[Artin L-function]] $L_\sigma$ associated with the given [[Galois representation]] $\sigma$ is equal to this: $L_\sigma = L_\pi$ ([Gelbart 84, conjecture 1 (page 27 (204))](#Gelbart84)).

$\,$

More generally, analogous statements are supposed to hold for general [[reductive algebraic groups]] $G$ other than $GL_n$. Here now an [[L-function]] is assigned to data which in addition to the [[Galois representation]] consists of a [[linear representation]] ${}^L G \longrightarrow GL_n$ of the [[Langlands dual group]] of $G$. 

First of all:

{#Conjecture2} **Conjecture 2** This more general L-function is conjectured to indeed behave like a decent L-function in that it has meromorphic [[analytic continuation]] to the [[complex plane]] and satisfies the "[[functional equation]]"-invariance under sending its parameter $s$ to $1-s$ ([Gelbart 84, conjecture 2' (page 29 (205))](#Gelbart84)).

Second:

{#Conjecture3} **Conjecture 3** This construction is supposed to behave well with respect to an analytic [[homomorphism]] ${}^L G \to {}^L G^{'}$ in that when changing the representation of ${}^L G^{'}$ by precomposition with this homomorphism one may find an accompanying change of Galois representation/automorphic representation from $G$ to $G^{'}$ such that the associated L-function remains invariant under these joint changes. This statement is what [[Robert Langlands]] calls _functoriality_ ([Gelbart 84, conjecture 3 (page 31 (207))](#Gelbart84))

In fact this last conjecture implies the previous two ([Gelbart 84, (page 32 (208))](#Gelbart84)).

$\,$

Various versions and refinements of this conjecture have since been considered, for some perspective see ([Taylor 02](#Taylor02), [Langlands 14](#Langlands14), [Harris 14](#Harris14)). On the one hand the "localization" of the program to [[local fields]] leads to the conjecture of _[[local Langlands correspondences]]_ ([Gelbart 84, (page 34 (210))](#Gelbart84)). On the other hand, the interpretation of the above story dually in [[arithmetic geometry]] in view of the [[function field analogy]] motivates the conjectural _[[geometric Langlands correspondence]]_, based on the following [[analogy]]:

* the [[Galois group]] is essentially the [[fundamental group]] of an [[algebraic curve]];

* hence a [[representation]] of it is a [[principal bundle|principal]]/[[vector bundle]] with [[flat connection]] on this curve;

* while that curious double quotient $GL_n(F) \backslash GL_n(\mathbb{A}_F)/GL_n(\mathcal{O}_F)$ is, in view of the [[Weil uniformization theorem]], analogous to the canonical [[Cech cohomology|Cech]]-realization of the [[moduli stack of bundles]] (see there for details) on that curve.

[[!include Langlands analogies -- table]]

From this [[arithmetic geometry]] point of view the Langlands conjecture seems to speak of a correspondence that sends [[Dirac distributions]] on the [[moduli space of flat connections]] over an [[algebraic curve]] to certain "automorphic" functions on the [[moduli stack of bundles]] on the same curve. This suggests that the Langlands correspondence should be understood as a nonabelian version of a [[Fourier-Mukai transform|Fourier-Mukai]]-type [[integral transform]]. This version of the conjecture is known as the _[[geometric Langlands correspondence]]_. See there for more details.

## Related concepts

* [[local Langlands correspondence]]

* [[automorphic form]]

* [[Galois representation]]

* [[Shimura variety]]

* [[modularity theorem]]

* [[Langlands functoriality]]

* [[relative Langlands program]]

## References
 {#References}

The original [[conjecture]] is due to 

* {#Langlands67} [[Robert Langlan

[... 正文截断于 6000 字符 ...]
