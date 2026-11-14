# Tannaka duality

url: https://ncatlab.org/nlab/show/Tannaka+duality
last_revised: 2025-07-28
---

### Context
#### Category theory
+-- {: .hide}
[[!include category theory - contents]]

* table of contents

## Idea

[[Tannaka]] duality or _Tannaka [[reconstruction theorem]]s_ are statements of the form:

if $A$ is a symmetry object (e.g. a [[locally compact topological group]], [[Hopf algebra]]), [[representation|represented]] on objects in a [[category]] $D$, one may _reconstruct_ $A$ from knowledge of the [[endomorphism]]s of the forgetful functor -- the **[[fiber functor]]** --

$$
  F : Rep_D(A) \to D
$$

from the [[category]] $Rep_D(A)$ of [[representation]]s of $A$ on [[object]]s of $D$ that remembers these underlying objects. In a generalization, called mixed Tannakian formalism, not a single [[fiber functor]], but a family of [[fiber functors]] over different bases is needed for a reconstruction. The fiber functor is necessary; for example, in the context of reconstruction of associative algebras, not remembering the underlying vector spaces results in reconstructing two different algebras with equivalent module categories (cf. [[Morita equivalence]]).

There is a general-abstract and a concrete aspect to this. The general abstract one says that an algebra $A$ is reconstructible from the [[fiber functor]] on the category of _all_ its modules. The concrete one says that in nice cases it is reconstructible from the category of _dualizable_ (finite dimensional) modules, even if it is itself not finite dimensional.

More precisely, let $V$ be any [[enriched category theory|enriching category]] (a [[locally small category|locally small]] [[closed monoidal category|closed]] [[symmetric monoidal category]] with all [[limit]]s). Then 

1. for 

   * $A$ a [[monoid]] in $V$;

   * $A Mod$ the $V$-[[enriched category]] of _all_ $A$-[[module]]s in $V$;

   * $F : A Mod \to V$ the [[forgetful functor|forgetful]] _[[fiber functor]]_ ;

   $A$ can be reconstructed as 
   the object of [[enriched functor category|enriched endomorphisms]] of $F$, 
   given by the [[end]]

   $$
     A 
     \simeq
     End(F) := \int_{N \in A Mod} V(F(N), F(N))
     \,.
   $$

   This is just the [[enriched Yoneda lemma]] in a slight disguise.   

1. In good cases, this [[end]] is computed already by restriction to the 
   [[full subcategory]] $A Mod_{dual}$ of [[dual object|dualizable modules]]

   $$
     \cdots \simeq \int_{N \in A Mod_{dual}} V(F(N), F(N))
     \,.
   $$

## Statement

So far the following examples concern the abstract algebraic aspect of Tannaka duality only, which is narrated here as a consequence of the [[enriched Yoneda lemma]] in [[enriched category theory]]. Some of the Tannaka duality theorems involve
subtle harmonic analysis. 

### For $G$-Sets 
  {#ForPermutationRepresentations}

A simple case of Tannaka duality is that of [[G-sets]] of a [[group]], i.e. representations on a [[set]]. In this case, Tannaka duality follows entirely from repeated application of the ordinary [[Yoneda lemma]].

+-- {: .num_theorem}
###### Theorem
**(Tannaka duality for [[G-sets]])**

Let $G$ be a [[group]], write  $G Set$ for the [[category]] of [[G-sets]] and 

$$
  F \colon G Set \longrightarrow Set
$$ 

for the [[forgetful functor]] that sends a [[G-set]] to its underlying [[set]].

Then there is a canonical [[group homomorphism|group-]][[isomorphism]] 

$$
  Aut(F) \;\simeq\; G
  \,.
$$

identifying the [[automorphism group]] of $F$ (the group of invertible [[natural isomorphisms]] from $F$ to itself) with $G$.

+-- {: .proof}
###### Long-winded Proof

We repeat the same proof, but with more notational details on what the entities involved in each step are precisely.
 
Let $\mathbf{B}G$ be the [[delooping]] [[groupoid]] of the [[group]] $G$. Then 

$$
  G Set \;=\; Func(\mathbf{B}G^{op}, Set)
  \,.
$$

The canonical inclusion $i : {*} \to \mathbf{B}G$ induces the [[fiber functor]]

$$
  Func(i,Set) : G Set \to Set
$$

which evaluates a functor $\rho : \mathbf{B}G^{op} \to Set$ on the unique object of $\mathbf{B}G$. By the [[Yoneda lemma]] this is the same as homming out of the functor [[representable functor|represented by]] that unique object

$$
  Func(i,Set) = Hom_{PSh(\mathbf{B}G)}(Y_{\mathbf{B}G} {*}, -)
  \,,
$$

where $Y_{\mathbf{B}G} : \mathbf{B}G \to PSh(\mathbf{B}G)$ is the [[Yoneda embedding]].

But this way we see that $Func(i,Set) : PSh(\mathbf{B}G) \to Set$  is itself a representable functor in the presheaf category $PSh(PSh(\mathbf{B}G)^{op})$

$$
  Func(i,Set) = Y_{\mathbf{PSh(\mathbf{B}G)^{op}}} Y_{\mathbf{B}G} *
  \,.
$$

So applying the [[Yoneda lemma]] twice, we find that

$$
  \begin{aligned}
    Aut_{PSh(PSh(\mathbf{B}G)^{op})} Func(i,Set)
    & =
    Aut_{PSh(PSh(\mathbf{B}G)^{op})} Y_{\mathbf{PSh(\mathbf{B}G)^{op}}} Y_{\mathbf{B}G} *
    \\
    & \simeq
    Aut_{PSh(\mathbf{B}G)^{op}} Y_{\mathbf{B}G} *
    \\
    & \simeq
    Aut_{\mathbf{B}G} *
    \\
    & \simeq G
    \,.
  \end{aligned}
$$

### For $V$-modules
  {#ForVModules}

Let $V$ be a ([[locally small category|locally small]]) [[closed monoidal category|closed]] [[symmetric monoidal category]], so that $V$ is enriched in itself via its [[internal hom]].

Observe that the setup, statement and proof of Tannaka duality for permutation representations given above is the special case for $V = $ [[Set]] of a statement verbatim the same in $V$-[[enriched category theory]], with the ordinary [[functor category]] replaced everywhere by the $V$-[[enriched functor category]]:

Then the $V$-enriched Tannaka duality theorem states that we can reconstruct a monoid $A$ as the monoid of endomorphisms of the forgetful $V$-functor from $A Mod$ to $V$:

+-- {: .num_theorem}
###### Theorem
**(Tannaka duality for $V$-modules over $V$-algebras)**

For $A$ a [[monoid]] in $V$ with [[delooping]] $V$-[[enriched category]] $\mathbf{B}A$, and with 

$$
  A Mod := [\mathbf{B}A,V]
$$

the [[enriched functor category]] that encodes the $V$-[[module]]s of $A$, we have that the $V$-enriched [[endomorphism]] algebra $End(F) := [F,F]$ of the $V$-

[... 正文截断于 6000 字符 ...]
