# derived category

url: https://ncatlab.org/nlab/show/derived+category
last_revised: 2026-06-30
---

#### Homological algebra
+--{: .hide}
[[!include homological algebra - contents]]

\tableofcontents

## Idea

The _derived (infinity,1)-category_ or _derived category_ of an [[abelian category]] $\mathcal{A}$ is the setting for [[homological algebra]] in $\mathcal{A}$: the [[(infinity,1)-categorical localization]] of the [[category of chain complexes]] in $\mathcal{A}$ at the class of [[quasi-isomorphisms]]. The derived category is a fundamental example of a [[stable (infinity,1)-category]]. In the case that $\mathcal{A} \simeq$ [[Mod|$R Mod$]] (cf. the [[Freyd-Mitchell embedding theorem]]), the [[stable Dold-Kan correspondence]] says that the derived $\infty$-category of $\mathcal{A}$ is equivalently the [[stable (infinity,1)-category of spectra|stable $\infty$-category of]] [[Eilenberg-MacLane spectrum|$H R$]]-[[module spectra]].

The derived $\infty$-category is presented by various [[dg-model structures]] on the [[category of chain complexes]], as described at [[model structures on chain complexes]]. As such it has also a natural incarnation as a [[pretriangulated dg-category]], which might be called the _derived dg-category_.

Like any [[stable (infinity,1)-category]], the [[homotopy category of an (infinity,1)-category|homotopy category]] of the derived (infinity,1)-category admits a canonical [[triangulated category]] structure. Often in the literature, the term _derived category_ refers to the [[homotopy category of an (infinity,1)-category|homotopy category]], viewed only as a [[triangulated category]]. The loss of information can often be problematic, but for many purposes is not important.

In what follows, we will describe only the homotopy category. See [[(infinity,1)-category of chain complexes]] for the full [[(infinity,1)-category]].

Associated to $\mathcal{A}$ is

* the [[category of chain complexes]] $Ch_\bullet(\mathcal{A})$ in $\mathcal{A}$ which is naturally a [[homotopical category]];

* the "[[homotopy category of chain complexes]]" $K(\mathcal{A})$;

* the [[stable ∞-category]] $K_\infty(\mathcal{A})$ of [[chain complexes]] in $\mathcal{A}$.

The  _derived category_ $D(\mathcal{A}$ of $\mathcal{A}$ is equivalently

* the [[homotopy category|1-categorical homotopy category]] of $Ch_\bullet(\mathcal{A})$ with respect to the [[quasi-isomorphisms]];

* the [[homotopy category of an (infinity,1)-category|(∞,1)-categorical homotopy category]] of $K_\infty(\mathcal{A})$.

In either case, this means that under the canonical [[localization]] functor

$$
  Q : Ch_\bullet(\mathcal{A}) \to D(\mathcal{A})
$$

the [[quasi-isomorphisms]] of [[chain complexes]] become true [[isomorphisms]]
and that $D(\mathcal{A})$ is [[universal property|universal]] with respect to this property.

Hence the derived category is an approximation to the full [[simplicial localization]] of $K(\mathcal{A})$. It is or can be equipped with several further [[properties]] and [[structure]] that give a more accurate approximation. Notably every derived category is a _[[triangulated category]]_, which is a way of remembering the [[suspension]] and de-suspension operations on its objects -- the [[suspension of chain complexes]] -- hence its "[[stable (infinity,1)-category|stability]]".

## History

Derived categories were introduced by [[Jean-Louis Verdier]] in his thesis under the supervision of [[Alexandre Grothendieck]].  It was originally used to extend [[Serre duality]] to a relative context.  See [[Robin Hartshorne|Hartshorne]]'s lecture notes "Residues and duality".

## Definition 

Let $\mathcal{A}$ be an [[abelian category]] and $K(\mathcal{A})$ its 
[[category of chain complexes]] modulo [[chain homotopy]] (the "[[homotopy category of chain complexes]]"). 

Equip $K(\mathcal{A})$ with the structure of a [[homotopical category]]
by declaring the [[weak equivalences]] to be the
**quasi-isomorphisms**: those morphisms
$f : V \to W$
which induce [[isomorphisms]] in [[homology]], 
$H(f) : H(V) \stackrel{\simeq}{\to} H(W)$. 

+-- {: .num_defn}
###### Definition

The **derived category** $D(\mathcal{A})$ is the [[homotopy category]] of
$K(\mathcal{A})$ with respect to these weak equivalences.

+-- {: .num_prop}
###### Proposition

A [[chain map]] $f_\bullet : V_\bullet \to W_\bullet$ is a 
[[quasi-isomorphism]] precisely there exists a [[distinguished triangle]] in $K(\mathcal{A})$ of the form

$$
  V \stackrel{f}{\to} W \to cone(f)
$$

with the [[mapping cone]] $cone(f) \in N(\mathcal{C})$.

This perspective is discussed in ([Kashiwara-Schapira, section 13](#KashiwaraSchapira)) and ([Schapira, section 6.2, 72](#Schapira)).

### In terms of injective and projective resolutions
 {#InTermsOfResolutions}

In the case that the underlying [[abelian category]] $\mathcal{A}$ has [enough injectives](injective%20object#EnoughInjectives) or [enough projectives](projective%20object#EnoughInjectives), the [[hom sets]] in the derived category may equivalently be obtained as [[homotopy]]-classes of [[chain maps]] from [[projective resolutions]] to [[injective resolutions]] of chain complexes. 

In view of the existence of the injective and projective [[model structure on chain complexes]] this is a special case of the general fact that [[homotopy categories]] of [[model categories]] may be obtained by forming homotopy classes of maps in the model category from  [[cofibrant resolutions]] to [[fibrant resolutions]]. For more details on the model-category point of view, see e.g. Appendix C of [Toën, Vaquié](#TV2007). But here we spell out an direct discussion of this fact for chain complexes.

+-- {: .num_defn}
###### Definition

Write $K^+(\mathcal{I}_{\mathcal{A}}) \hookrightarrow K^+(\mathcal{A})$
for the [[full subcategory]] of the [[homotopy category of chain complexes]] bounded above on those that are degreewise [[injective objects]].

Dually, let $K^-(\mathcal{P}_{\mathcal{A}}) \hookrightarrow K^-(\mathcal{A})$
for the [[full subcategory]] of the [[homotopy category of chain complexes]] bounded below on those tha

[... 正文截断于 6000 字符 ...]
