# Riemann-Hilbert correspondence

url: https://ncatlab.org/nlab/show/Riemann-Hilbert+correspondence
last_revised: 2024-08-09
---

## Idea

The most basic form of the Riemann--Hilbert correspondence states that the [[category]] of [[flat connection|flat]] [[vector bundles]] on a suitable [[space]] is equivalent to the category of [[local systems]].

While [[Riemann-Hilbert problem|Hilbert's 21st problem]] has a negative solution, there is a generalized sheaf-theoretical formulation which leads to an equivalence of categories discovered by Mebkhout and a bit later also by [[Kashiwara]].

## Statement

Let $X$ be a smooth algebraic variety over $\mathbb{C}$. Let $D(X^\Zar,\mathcal{D}_{X})$ be the derived category of algebraic [[D-modules]] on $X$ (i.e. quasi-coherent $\mathcal{O}_{X}$-modules with [[flat connection]]), and let $D_{rh}^{b}(X^\Zar,\mathcal{D}_{X})$ be the full subcategory of $D^{b}(X^\Zar,\mathcal{D}_{X})$ consisting of objects whose cohomology sheaves are regular holonomic algebraic D-modules. Let $D(X^{an},\mathbb{C})$ be the derived category of sheaves of $\mathbb{C}$-vector spaces on $X^{an}$, and let $D_{c}^{b}(X^{an},\mathbb{C})$ be the full subcategory of $D^{b}(X^{an},\mathbb{C})$ consisting of objects whose cohomology sheaves are Zariski constructible.

Let $\mathcal{E}$ be an algebraic D-module and let $\mathcal{E}^{\hol}=\mathcal{O}_{X}^{\hol}\otimes_{\mathcal{O}_{X}}\mathcal{E}$. The assignment $\mathcal{E}\to\Omega^{*}(\mathcal{E}^{\mathrm{hol}})$ determines a functor

$$dR: D(X^\Zar,\mathcal{D}_{X})\to D(X^{an},\mathbb{C}).$$

\begin{proposition}(Mebkhout, Kashiwara, Beilinson-Bernstein)

The restriction of the functor $dR$ gives an equivalence of categories

$$D_{rh}^{b}(X^\Zar,\mathcal{D}_{X})\xrightarrow{\sim} D_{c}^{b}(X^{an},\mathbb{C})$$

\end{proposition}

## Use in the geometric Langlands correspondence

The Riemann-Hilbert correspondence allows one to translate the automorphic side of the [[geometric Langlands correspondence]] from the language of [[perverse sheaves]] (which in turn is motivated by functions on $Bun_{G}$, via Grothendieck's functions-to-sheaves dictionary) to the language of [[D-modules]] (see [Frenkel05](#Frenkel05), 3.4 to 3.6).

## p-torsion and p-adic Riemann-Hilbert correspondence

[[Bhargav Bhatt]] and [[Jacob Lurie]] have formulated a version of the Riemann-Hilbert correspondence for finite type schemes over a complete and algebraically closed extension of the [[p-adic numbers]]:

\begin{proposition}([Bhatt21](#Bhatt21), Theorem 5.1)

Let $C$ be a complete and algebraically closed extension of $\mathbb{Q}_{p}$ and let $X$ be of finite type over $\mathcal{O}_{C}$. Then there is a natural exact functor

$$\RH: D_{\cons}^{b}(X_{C},\mathbb{F}_{p})\to D_{\qc}^{b}(X\otimes_{\mathcal{O}_{C}} \mathcal{O}_{C}/p).$$

This functor commutes with proper pushforward, intertwines [[Verdier duality]] and [[Grothendieck duality]] in the almost category, and interacts well with the perverse [[t-structure]].
\end{proposition}

Bhatt and Lurie also have a version with p-adic, instead of p-torsion, coefficients (this time the schemes have to be smooth proper varieties over a finite extension of the p-adic numbers).

\begin{proposition}([Bhatt21](#Bhatt21), Theorem 5.4)

Let $K$ be a finite extension of $\mathbb{Q}_{p}$ and let $X$ be a smooth proper variety over $K$. Then there is a natural exact functor

$$\RH_{\mathcal{D}}: D_{wHT}^{b}(X_{C},\mathbb{Q}_{p})\to DF_{coh}(\mathcal{D}_{X})$$

where $D_{wHT}^{b}(X_{C},\mathbb{Q}_{p})$ is a full subcategory of $D_{cons}^{b}(X_{C},\mathbb{Q}_{p})$ spanned by "weakly Hodge-Tate sheaves" and $DF_{coh}(\mathcal{D}_{X})$ is a suitable derived category of [[D-modules|$\mathcal{D}_{X}$-modules]] equipped with a "good" filtration. This functor commutes with proper pushforward, intertwines [[Verdier duality]] and [[Grothendieck duality]] in the almost category, and interacts well with the perverse [[t-structure]].
\end{proposition}

The construction of Bhatt and Lurie is as follows. Let $K$ be a discretely-valued p-adic field and let $X$ be a smooth projective variety over $K$ with $\mathcal{X}$ its associated rigid analytic space. Let $\mathcal{F}$ be a constructible sheaf over $X$. We say that $\mathcal{F}$ is _weakly de Rham_ if the stalk $\mathcal{F}$ is a weakly de Rham Galois representation. More generally if $\mathcal{F}$ is an object of the derived category $D_{c}^{b}(X,\mathbb{Q}_{p})$ we say that $\mathcal{F}$ is _weakly de Rham_ if its cohomology sheaves are weakly de Rham.

Let $\nu:\mathcal{X}_{proet}\to \mathcal{X}_{et}$ be the projection and let $\mathcal{B}_{dR}$ be the de Rham period sheaf on $\mathcal{X}_{proet}$. If $\mathcal{F}$ is weakly de Rham, we define

$$RH(\mathcal{F}):=R\nu_{*}(\nu^{-1}\mathcal{F}\widehat{\otimes}_{\mathbb{Q}_{p}}\mathcal{B}_{dR}\langle u\rangle)$$ 

[[Lucas Mann]] has also formulated a version of the p-torsion Riemann-Hilbert correspondence for small v-stacks as part of his proof of mod p Poincare duality for [[rigid analytic spaces]]. This version is stated in terms of $\varphi$-modules, which in his context are simultaneously [[solid modules]] and [[almost modules]] over $\mathcal{O}_{X}^{+}/\pi$ together with an action of the Frobenius $\varphi$, and overconvergent etale $\mathbb{F}_{p}$-sheaves (the corresponding derived $\infty$-categories are denoted by $\mathcal{D}_{\square}^{a}(\mathcal{O}_{X}^{+}/\pi)^{\varphi}$ and $\mathcal{D}_{et}(X,\mathbb{F}_{p})^{oc}$ respectively).

\begin{proposition}([Mann22](#Mann22), Theorem 1.2.7, Theorem 3.9.23)

Let $X$ be a small v-stack over $\mathbb{Z}_{p}$ with pseudouniformizer $\pi$ such that $\pi\vert p$. Then the functor

$$-\otimes\mathcal{O}_{X}^{+a}/\pi:\mathcal{D}_{et}(X,\mathbb{F}_{p})^{oc}\to\mathcal{D}_{\square}^{a}(\mathcal{O}_{X}^{+}/\pi)^{\varphi}$$

is fully faithful and induces an equivalence of categories of perfect objects on both sides. 

\end{proposition}

## Related entries

* [[Hilbert's problems]]

* [[flat infinity-connection]]

* [[infinity-local system]]

* [[D-modules]]

## References

* [[Alain Connes]], [[Matilde Marcolli]]

[... 正文截断于 6000 字符 ...]
