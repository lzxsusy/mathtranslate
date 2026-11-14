# Fourier-Mukai transform

url: https://ncatlab.org/nlab/show/Fourier-Mukai+transform
last_revised: 2025-10-21
---

#### Higher linear algebra
+-- {: .hide}
[[!include homotopy - contents]]
#### Cohomology
+--{: .hide}
[[!include cohomology - contents]]

See [Orlov 2003, 3.2.1](#OrlovSurvey) for a proof.  

+-- {: .num_remark}
###### Remark

Though theorem \ref{OrlovTheorem} is stated there for $F$ admitting a [[right adjoint]], it follows from [Bondal-van den Bergh 2002](#BondalBergh2002) that every [[triangulated functor|triangulated]] [[fully faithful functor]] admits a [[right adjoint]] automatically (see e.g. [Huybrechts 08, p. 6](#Huybrechts08)).

## Enhancements

For any [[quasicompact quasiseparated morphism|quasi-compact quasi-separated]] $k$-schemes $X$ and $Y$ there is a canonical equivalence of [[stable (∞,1)-categories]]

\[
\mathrm{Func}^L(D(X), D(Y)) \simeq D(X \times Y).
\]

## Related concepts

* [[triangulated categories of sheaves]]

* [[Grothendieck duality]]

## References

### General

The original article:

* {#Mukai81} [[Shigeru Mukai]]: _Duality between $D(X)$ and $D(\hat X)$ with its application to Picard sheaves_, Nagoya Mathematical Journal **81** (1981) 153-175 &lbrack;[doi:10.1017/S002776300001922X](https://doi.org/10.1017/S002776300001922X)&rbrack;

Further discussion:

* {#BondalBergh2002} [[Alexei Bondal]], [[Michel van den Bergh]].  _Generators and representability of functors in commutative and noncommutative geometry_, 2002, [arXiv](http://arxiv.org/abs/math/0204218)

* {#OrlovSurvey} [[Dmitri Orlov]], _Derived categories of coherent sheaves and equivalences between them_, Russian Math. Surveys, 58 (2003), 3, 89-172, [translation](http://www.mi.ras.ru/~orlov/papers/Uspekhi2003.pdf).

*  Lutz Hille, Michel van den Bergh, _Fourier-Mukai transforms_ ([arXiv:0402043](http://arxiv.org/abs/math/0402043))
 

* {#Huybrechts08} [[Daniel Huybrechts]], _Fourier-Mukai transforms_ (2008) &lbrack;[pdf](http://www.math.uni-bonn.de/people/huybrech/Garda2.pdf), [[Huybrechts-FourierMukai.pdf:file]]&rbrack;

* Claudio Bartocci, [[Ugo Bruzzo]], Daniel Hernandez Ruiperez: *Fourier-Mukai and Nahm transforms in geometry and mathematical physics*, Progress in Mathematics **276**, Birkhäuser (2009) &lbrack;[doi:10.1007/b11801](https://doi.org/10.1007/b11801)&rbrack;

* {#RVdB2015} Alice Rizzardo, [[Michel Van den Bergh]], _An example of a non-Fourier-Mukai functor between derived categories of coherent sheaves_ 
([arXiv:1410.4039](http://arxiv.org/abs/1410.4039))

* {#Belmans} [[Pieter Belmans]], section 2.2 of _Grothendieck duality: lecture 3_, 2014 ([[BelmansDuality.pdf:file]])

Banerjee and Hudson have defined Fourier-Mukai functors analogously on [[algebraic cobordism]].

* Anandam Banerjee, Thomas Hudson, _Fourier-Mukai transformation on algebraic cobordism_, [pdf](https://sites.google.com/site/anandamb/research/fourier-mukai.pdf?attredirects=0).

Discussion of [[internal homs]] of [[dg-categories]] in terms of refined Fourier-Mukai transforms is in

* [[Bertrand Toën]], _The homotopy theory of dg-categories and derived Morita theory_, Invent. Math. 167 (2007), 615&#8211;667

* Alberto Canonaco, Paolo Stellari, _Internal Homs via extensions of dg functors_ ([arXiv:1312.5619](http://arxiv.org/abs/1312.5619))

Discussion in the context of [[geometric Langlands duality]] is in 

* {#Frenkel05} [[Edward Frenkel]], _Lectures on the Langlands Program and Conformal Field Theory_ ([arXiv:hep-th/0512172](http://arxiv.org/abs/hep-th/0512172))

For a discussion of Fourier-Mukai transforms in the setting of $(\infty,1)$-enhancements, see

* {#BenZviNadlerPreygel13} [[David Ben-Zvi]], [[David Nadler]], Anatoly Preygel.  _Integral transforms for coherent sheaves_,  [arXiv:1312.7164](http://arxiv.org/abs/1312.7164)

### For T-duality
 {#ReferencesForTDuality}

Discussion of the effect of [[T-duality]] on [[RR-field]] [[flux densities]] (in [[ordinary cohomology]] or in [[topological K-theory]]) as a Fourier-Mukai-like transform goes back to:

* [[Kentaro Hori]], [[Yaron Oz]], Section 3.1 of: *F-Theory, T-Duality on K3 Surfaces and $N=2$ Supersymmetric Gauge Theories in Four Dimensions*, Nucl. Phys. B **501** (1997) 97-108 &lbrack;[arXiv:hep-th/9702173](https://arxiv.org/abs/hep-th/9702173), <a href="https://doi.org/10.1016/S0550-3213(97)00361-1">doi:10.1016/S0550-3213(97)00361-1</a>&rbrack;

* [[Kentaro Hori]]: (1.1) and pp. 13 of: *D-branes, T-duality, and Index Theory*, Adv. Theor. Math. Phys. **3** 2 (1999) 281-342 &lbrack;[arXiv:hep-th/9902102](https://arxiv.org/abs/hep-th/9902102), [doi:10.4310/ATMP.1999.v3.n2.a5](https://dx.doi.org/10.4310/ATMP.1999.v3.n2.a5),  journal:[pdf](https://www.intlpress.com/site/pub/files/_fulltext/journals/atmp/1999/0003/0002/ATMP-1999-0003-0002-a005.pdf)&rbrack;
  > (whence "Hori's formula")

with explicit formulation in the context if [[topological T-duality]]:

* {#BouwknegtEvslinMathai04} [[Peter Bouwknegt]], [[Jarah Evslin]], [[Varghese Mathai]], (1.9) in: _T-Duality: Topology Change from H-flux_, Commun. Math. Phys. **249** (2004) 383-415 &lbrack;[hep-th/0306062](http://arxiv.org/abs/hep-th/0306062), [doi:10.1007/s00220-004-1115-6](https://doi.org/10.1007/s00220-004-1115-6)&rbrack; 

Survery and Review:

* Martin Ruderer, *Fourier-Mukai Transforms from T-Duality*, PhD thesis, Regensburg (2015)  &lbrack;[urn:nbn:de:bvb:355-epub-314033](https://nbn-resolving.org//urn:nbn:de:bvb:355-epub-314033), [pdf](https://epub.uni-regensburg.de/31403/6/final.pdf)&rbrack;

* Bjorn Andreas, Daniel Hernandez Ruiperez: *Fourier Mukai Transforms and Applications to String Theory*, Rev. R. Acad. Cienc. Exactas Fis. Nat. Ser. A Mat **99** 1 (2005) 29-77 &lbrack;[arXiv:math/0412328](https://arxiv.org/abs/math/0412328), [spire:667425](https://inspirehep.net/literature/667425), journal: [pdf](https://mat.usal.es/ruiperez/Site/Papers_files/4_ANDREAS.PDF)&rbrack;

For [[non-abelian T-duality]]:

* Eva Gevorgyan, [[Gor Sarkissian]]: *Defects, Non-abelian T-duality, and the Fourier-Mukai transform of the Ramond-Ramond fields*,  J. High Energ. Phys. **2014** 35 (2014) \[<a href="https://doi

[... 正文截断于 6000 字符 ...]
