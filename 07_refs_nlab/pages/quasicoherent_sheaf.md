# quasicoherent sheaf

url: https://ncatlab.org/nlab/show/quasicoherent+sheaf
last_revised: 2026-06-15
---

### Context
#### Topos Theory
+-- {: .hide}
[[!include topos theory - contents]]

We now explain the above statement in detail and thereby prove it.

Let $C = $[[Ring]]${}^{op}$ be the category of (commutative, unital) [[ring]]s.
For $R$ a [[ring]] write $Spec R$ for it regarded as an object of $C$.
Write $Spec f = f^{op} : Spec(S) \to Spec(R)$ for the morphism in $Ring^{op}$ corresponding to the map $f : R \to S$ of commutative rings.

Consider the [[2-category]] of (pre)[[stack]]s on 
$C$. The canonical [[module]] [[bifibration]] $p : Mod \to Ring$ of the category of modules over all rings is the bifibration whose fibered part corresponds to the (pre)stack $QC \in [C^{op},Cat]$ given on objects by 

$$
  QC : Spec R \mapsto R Mod
$$

and on morphisms by

$$
  QC : (Spec S \stackrel{f^{op}}{\to} Spec R) 
         \mapsto 
       (R Mod \stackrel{S\otimes_{f} }{\to} S Mod)
  \,,
$$

where on the right we have the functor that sends any $R$-module $N$ to the 
[[tensor product]] over $S$ with the $R$-$S$-[[bimodule]]
$S = {}_S S_R$ with its canonical left $S$-action and with the right $R$-action induced by the ring homomorphism $f$.

One may think of this as the stack of generalized algebraic vector bundles:

the operation $S \otimes_{f} - : R Mod \to S Mod$ corresponds to the
[[pullback]] of [[bundle]]s along a morphism of the underlying spaces.
(See for instance the discussion of [[monadic descent]] at [[Sweedler coring]] for more on this.)
  
We may [[Kan extension|right Kan extend]] the 2-functor $QC : CRing^{op} \to Cat$ through the [[Yoneda embedding]] $CRing^{op} \hookrightarrow [CRing,Cat]$
to get a definition of $QC$ on arbitrary [[presheaf|presheaves]]. 

$$
  \array{
    CRing^{op} &\stackrel{QC}{\to}& Cat
    \\
    {}^{Y}\downarrow & \nearrow_{\mathrlap{Ran_Y QC}}
    \\
    [CRing,Cat]    
  }
  \,.
$$

Consider $X \in [C^{op},Set]$ any ([[presheaf|pre]])[[sheaf]] on $C$.
This may be the presheaf [[representable functor|represented]]
by a [[scheme]], but for the purposes of the definition of $QC$ it may be much more generally any presheaf.

By the general formula for [[Kan extension]] in terms of a [[weighted limit]] given by an [[end]]
we have

$$
  Ran_Y QC : X \mapsto \int_{R \in Ring} ([Ring,Cat]^{op}(X,Y(R)))^{QC(R)}
$$

which using the [[Yoneda lemma]] is

$$
  \cdots = \int_{R \in CRing} [CRing,Cat](X(R), QC(R))
  \,.
$$

This is the [[end]]-formula for the [[hom-object]] in an [[enriched functor category]]
$[C^{op},Cat]$,
hence this is nothing but the category of (pseudo)[[natural transformation]]s between
the 2-functor $X$ and the 2-functor $QC$.

We write for short

$$
  QC(X) := (Ran_Y QC)(X) := [C^{op},Cat](X,QC)
  \,.
$$

This definition of "generalized vector bundles" on arbitrary presheaves is
entirely analogous to the definition of differential forms on arbitrary
presheaves, that is discussed in some detail for instance in the entry on
[[rational homotopy theory]].

We claim that the category $QC(X)$ is the category of quasicoherent sheaves on
$X$ as defined by other means above, whenever that other definition applies to $X$.

To see this, straightforwardly unwrap the definition: 
an object $N$ in $QC(X) = [C^{op},Cat](X,QC)$
is a [[transfor|pseudonatural transformation]] of 2-functors $N : X \to QC$,
where $X$ is regarded as a 2-functor by the canonical embedding 
$disc : Set \hookrightarrow Cat$ that regards a [[set]] as a [[discrete category]].

The components of $N$ are

* for each $Spec R \in Ring^{op}$ a [[functor]] $N|_{Spec R} : X(R) \to QC(R) = R Mod$:

  this functor picks one $R$-module $N(r) \in R Mod$ for each plot $(r : Spec R \to X) \in X(Spec R)$;
  
* for each morphism $f : Spec A \to Spec B$ 
  a pseudonaturality square

  $$
    \array{
      X(Spec B) 
         &\stackrel{X(f)}{\to}& 
      X(Spec A)
      \\
      {}^{\mathllap{N|_{Spec B}}}\downarrow 
      &{}^{\Gamma(f)}\swArrow_{\simeq}& 
      \downarrow^{\mathrlap{N|_{Spec A}}}
      \\
      B Mod &\underset{- \otimes_{f^*} A}{\to}& A Mod
    }
  $$
  
  in [[Cat]] (these are subject to coherence conditions). This unwraps to the following data:

  * the component functors $N|_{Spec A}$ provide an
    assignment $a \mapsto N(a)$ of modules $N(a)$ to each 
    plot $(a : Spec A \to X) \in X(Spec A)$;

  * these assignments form a presheaf on the [[overcategory]] 
    $Aff/X$ by taking the restriction morphism
    
    $$
      N(f) : N(b) \to N(a)
    $$

    to be that underlying the components of the 
    natural isomorphism in the above diagram

    $$
      N(b)\otimes_{f^*} A \stackrel{\simeq}{\to} N(a)
      \,,
    $$

    i.e. the restriction of this morphism to $(n,1)$.

* for each tuple of composable morphisms 

  $$
    \array{
      && Spec B
      \\
      & {}^f\nearrow && \searrow^g
      \\
      Spec A &&\to&& Spec C
    }
  $$

  a pseudo-naturality prism equation relating, $N(f)$, $N(g)$ and $N(g\circ g)$.  The present author is too lazy to write out the diagram in detail, but it is of precisely the kind described in great detail for instance in the entry on [[group cohomology]]. Under the above identification, this yields the cocycle condition mentioned  in the above definitions.

This way, the transformation $N : X \to QC$ defines 
manifestly a quasicoherent sheaf on $Aff/X$ in the sense of the
definition in the above section [As sheaves on Aff/X](#AsSheaves). Conversely, every quasicoherent sheaf according to that definition gives rise to a transformation $N : X \to QC$ under this prescription.

### As cartesian morphisms of fibrations {#AsFibHoms}

By the equivalence between [[pseudofunctor]]s $Ring \to Cat$
and [[Grothendieck fibration]]s $F \to Ring^{op}$ induced by the
[[Grothendieck construction]], the above may equivalently be
reformulated as follows.

Recall from the discussion at [[Grothendieck fibration]] that the equivalence in question is between the following two [[bicategory|bicategories]]:

* on the one hand the bicategory whose objects are [[pseudo

[... 正文截断于 6000 字符 ...]
