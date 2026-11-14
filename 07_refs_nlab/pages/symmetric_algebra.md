# symmetric algebra

url: https://ncatlab.org/nlab/show/symmetric+algebra
last_revised: 2025-10-31
---

#### Algebra
+--{: .hide}
[[!include algebra - contents]]
#### Monoidal categories
+--{: .hide}
[[!include monoidal categories - contents]]

## Properties

+-- {: .num_prop #CochainCohomologyOfSymmetricAlgebraOnCochainComplex}
###### Proposition

Let the ambient [[category]] be the [[category of cochain complexes]] over a [[ground field]] of [[characteristic zero]], regarded as a [[symmetric monoidal category]] via the [[tensor product of chain complexes]] and consider the [[differential graded-commutative algebra]] $Sym(V^\bullet,d)$ free on a cochain complex $(V^\bullet,d)$ from example \ref{SymmetricAlgebraInCoChainComplexes}. 

Then the [[cochain cohomology]] (of the [[forgetful functor|underlying]] cochain complex) of $Sym(V^\bullet,d)$ is the graded symmetric algebra on the [[cochain cohomology]] of $(V^\bullet,d)$:

$$
  H^\bullet\left( 
    Sym\left(V^\bullet,d\right)
  \right)
  \;\simeq\;
  Sym\left( H^\bullet(V^\bullet,d) \right)
  \,.
$$

Symmetric powers in a symmetric monoidal $\mathbb{Q}^{+}$-linear category  are characterized among the countable families of objects as forming a special connected graded quasi-bialgebra (reference to come). 

## Related concepts

* [[Grassmann algebra]]

* [[symmetric algebra spectrum]]

* [[symmetric ring]]

* [[symmetric power]]

## References

* [[Bourbaki]], _Alg&#232;bre_, chap. III, &#167; 6.

* [[Stacks Project]], [Tag 00DM](http://stacks.math.columbia.edu/tag/00DM).

* {#Gallier11} [[Jean Gallier]], *Tensor Algebras, Symmetric Algebras and Exterior Algebras* &lbrack;[pdf](https://www.cis.upenn.edu/~cis6100/diffgeom7.pdf)&rbrack;, section 22 in: *Notes on Differential Geometry and Lie Groups* (2011)

* {#Gallier20} [[Jean Gallier]], [[Jocelyn Quaintance]], *Tensor Algebras and Symmetric Algebras*, Ch 2 in: *Differential Geometry and Lie Groups -- A second course*, Geometry and Computing **13**, Springer (2020) &lbrack;[doi:10.1007/978-3-030-46047-1](https://doi.org/10.1007/978-3-030-46047-1), [webpage](https://www.cis.upenn.edu/~jean/gbooks/manif.html), [pdf](https://www.seas.upenn.edu/~jean/diffgeom-spr-II.pdf)&rbrack;

On the [[symmetric algebra spectrum]] of the [[sphere spectrum]], and its structure as a [[Hopf ring spectrum]]:

* [[Neil Strickland]], [[Paul Turner]], _Rational Morava $E$-theory and $D S^0$_, Topology **36** 1 (1997) 137-151 ([pdf](http://hopf.math.purdue.edu/Strickland-PTurner/rme.pdf))

Further on symmetric powers in [[homotopical algebra|homotopical]]/[[higher algebra]]:

* {#GorchinskiyGuletskii16} [[Sergey Gorchinskiy]], [[Vladimir Guletskii]], *Symmetric powers in abstract homotopy categories*, Adv. Math., **292** (2016) 707-754 &lbrack;[arXiv:0907.0730](https://arxiv.org/abs/0907.0730), [doi:10.1016/j.aim.2016.01.011](https://doi.org/10.1016/j.aim.2016.01.011)&rbrack;

Discussion via [[string diagrams]]:

* {#Vienney23} [[Jean-Baptiste Vienney]], *String diagrams for symmetric powers I: In symmetric monoidal $\mathbb{Q}_{\geq 0}$-linear categories* &lbrack;[arXiv:2308.02094](https://arxiv.org/abs/2308.02094)&rbrack;
