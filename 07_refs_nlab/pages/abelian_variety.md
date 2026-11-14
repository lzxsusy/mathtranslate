# abelian variety

url: https://ncatlab.org/nlab/show/abelian+variety
last_revised: 2026-09-26
---

## Idea

Abelian varieties are higher dimensional analogues of [[elliptic curve]]s (which are included) -- they are [[varieties]] equipped with a structure of an [[abelian group]], hence abelian [[group schemes]], whose multiplication and inverse are regular maps.

## Definition

[Mumford 1970](#Mumford1970) defines an **abelian variety** over an algebraically closed field $k$ to be a [[complete algebraic variety|complete]] [[algebraic group]] over $k$.  Remarkably, any such thing is an _[[abelian group|abelian]]_ algebraic group.  The assumption of connectedness is necessary for that conclusion.

## Automatic abelianness

[Mumford '70](#Mumford1970) gives at least two proofs that every complete algebraic group over an algebraically closed field is automatically abelian.  One of them uses a 'rigidity lemma' which has an interesting category-theoretic interpretation.  We outline this here:

In simple terms, the rigidity lemma says that under certain circumstances "a 2-variable function $f(x,y)$ that is independent of $x$ for one value of $y$ is independent of $x$ for all values of $y$."   

More precisely, in a category with products, say a morphism $f: X \to Y$ is <b>constant</b> if it factors through the unique morphism $X \to 1$.  Say a morphism $f : X \times Y \to Z$ is <b>independent of $X$</b> if it factors through the projection $X \times Y \to Y$.   

Say a <b>point</b> of $Y$ is a morphism $p: 1 \to Y$.  Say a morphism $f: X \times Y \to Z$ is <b>independent of $X$ at some point $p$ of $Y$</b> if $f \circ (1_X \times p) : X \to Z$ is constant.

**Definition.** A category with finite products **obeys the rigidity lemma** if any morphism $f: X \times Y \to Z$ that is independent of $X$ at some point of $Y$ is in fact independent of $X$.

**Theorem 1.** The category of complete algebraic varieties over an algebraically complete field $k$ has finite products and obeys the rigidity lemma.

+-- {: .proof}
######Proof
The hard part, the rigidity lemma, is proved for complete algebraic varieties on page 43 of [Mumford '70](#Mumford1970).  Mumford mentions in a footnote that complete algebraic varieties are automatically irreducible, and he later seems to assume without much explanation that they are connected: these points could use some clarification, at least for amateurs. 

**Corollary 1.** If $C$ is a category with finite products obeying the rigidity lemma, any group object in $C$ is abelian.

+-- {: .proof}
######Proof
If $G$ is a group object in $C$, the inverse map $inv: G \to G$ preserves the identity, so by the above theorem it is a group homomorphism.  This in turn implies that $G$ is abelian.

A consequence of Corollary 2 is that if $Alb : Var_* \to AbVar$ is the left adjoint to $U$, sending any connected pointed projective variety to its Albanese variety, the monad $T = U \circ Alb$ is an [[idempotent monad]].  For more on this see [[Albanese variety]].

## Related concepts

* [[theta function]]

* [[Cartier duality]]

* [[dual abelian group scheme]]

* [[Albanese variety]]

## Literature

* {#Mumford1970} [[David Mumford]]: *Abelian varieties*, Oxford Univ. Press (1970) &lbrack;full: [pdf](https://wstein.org/edu/Fall2003/252/references/mumford-abvar/Mumford-Abelian_Varieties.pdf), Part I: [[Mumford-AbelianVarieties-I.pdf:file]], II: [[Mumford-AbelianVarieties-II.pdf:file]], III: [[Mumford-AbelianVarieties-III.pdf:file]], IV: [[Mumford-AbelianVarieties-IV.pdf:file]]&rbrack;

* [[M. Demazure]], [[P. Gabriel]], _Groupes algebriques_, tome 1 (later volumes never appeared), Mason and Cie, Paris 1970 &#8211; has functor of points point of view; for review see Bull. London Math. Soc. (1980) 12 (6): 476-478, [doi](http://dx.doi.org/10.1112/blms/12.6.476b)

* [[Daniel Huybrechts]], _Fourier-Mukai transforms in algebraic geometry_, Oxford Mathematical Monographs. 2006. 307 pages.

* C. Bartocci, [[Ugo Bruzzo]], D. Hernandez Ruiperez, _Fourier-Mukai and Nahm transforms in geometry and mathematical physics_, Progress in Mathematics 276, Birkhauser 2009.

* J. S. Milne, _Abelian varieties_, course notes &lbrack;[pdf](http://www.jmilne.org/math/CourseNotes/AV.pdf)&rbrack;

* {#Polishchuk03} [[Alexander Polishchuk]], section 17 of: _Abelian varieties, Theta functions and the Fourier transform_, Cambridge Tracts in Mathematics **153**, Cambridge University Press (2003) &lbrack;[doi:10.1017/CBO9780511546532](https://doi.org/10.1017/CBO9780511546532), [review pdf](http://math1.unice.fr/~beauvill/pubs/poli.pdf)&rbrack;

* Goro Shimura, _Abelian varieties with complex multiplication and modular functions_, Princeton Univ. Press 1997.

* [[André Weil]], _Courbes alg&#233;briques et vari&#233;t&#233;s ab&#233;liennes_, Paris: Hermann 1971

In [[E-infinity geometry]]:

* {#LurieI} [[Jacob Lurie]], _Elliptic Cohomology I: Spectral Abelian Varieties_ ([pdf](http://www.math.harvard.edu/~lurie/papers/Elliptic-I.pdf))

Discussion of how the rigidity lemma gives 'automatic abelianness':

* [Two miracles in algebraic geometry](https://golem.ph.utexas.edu/category/2016/08/the_magic_of_algebraic_geometr.html), _The n-Category Caf&eacute_.
