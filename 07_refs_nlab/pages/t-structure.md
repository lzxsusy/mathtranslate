# t-structure

url: https://ncatlab.org/nlab/show/t-structure
last_revised: 2023-04-20
---

#### Stable Homotopy theory
+--{: .hide}
[[!include stable homotopy theory - contents]]

([BBD 82](#BeilinsonBernsteinDeligne82), [[Higher Algebra|Higher Algebra, remark 1.2.1.12]], [FL16, Ex. 4.1](#FL16) and [FLM19, &#167;3.1](#FLM19))

### Relation to spectral sequences

If the heart (Def. \ref{HeartOfATStructure}) of a t-structure on a [[stable (∞,1)-category]] with [[sequential limits]] is an [[abelian category]], then the [[spectral sequence of a filtered stable homotopy type]] [converges](spectral+sequence#ConvergenceOfSpectralSequences) (see there).

### Relation to normal torsion theories
 {#RelationToNormalTorsionTheories}

In the [[(∞,1)-category theory]], $t$-structures arise as [[torsion theory|torsion/torsionfree]] classes associated with suitable [[orthogonal factorization system|factorization systems]] on [[stable ∞-categories]] $C$.

* In [[stable ∞-category]]-theory, the relevant sub-[[(∞,1)-categories]] are closed under de/suspension simply because they are (co-)[[reflective sub-(∞,1)-categories|reflective]], arising from co/[[reflective factorization systems]] on $C$.

* A _bireflective_ factorization system on a $\infty$-category $C$ consists of a [[orthogonal factorization system|factorization system]] $\mathbb{F}=(E,M)$ where both classes satisfy the [[two-out-of-three]] property.

* A bireflective factorization system $(E,M)$ on a stable $\infty$-category $C$ is called _normal_ if the diagram $S x\to x\to R x$ obtained from the reflection $R\colon C\to M/0$ and the coreflection $S\colon C\to *\!/E$ (where the category $M/\!* =\{A\mid (0\to A)\in M\}$ is obtained as $\Psi(E,M)$ under the adjunction $\Phi \dashv \Psi$ described at *[[reflective factorization system]]* and in [CHK85](#CHK85); see also [FL16, &#167;1.1](#FL16)) is _exact_, meaning that the square in
$$
\begin{array}{cccccc} 
0 &\to& S X &\to& X\\
&& \downarrow&&\downarrow\\
&& 0 &\to& R X\\
&& && \downarrow\\
&& && 0
\end{array}
$$
is a fiber sequence for any object $X$; see [FL16, Def 3.5 and Prop. 3.10](#FL16) for equivalent conditions for normality.

\begin{remark}
[CHK85](#CHK85) established a hierarchy between the three notions of simple, semi-exact and normal factorization system: in the setting of stable $\infty$-category the three notions turn out to be equivalent: see [FL16, Thm 3.11](#FL16).
\end{remark}

\begin{proposition}
\label{CorrespondenceWithNormalTorsionTheories}
There is a bijective correspondence between the class $TS( C )$ of $t$-structures and the class of normal torsion theories on a stable $\infty$-category $C$, induced by the following correspondence:

* On the one side, given a normal, bireflective factorization system $(E,M)$ on $C$ we define the two classes $(C_{\ge0}(\mathbb{F}), C_{\lt 0}(\mathbb{F}))$ of a $t$-structure $\mathfrak{t}(\mathbb{F})$ to be the torsion and torsionfree classes $(*\!/E, M/\!*)$  associated to the factorization $(E,M)$.

* On the other side, given a $t$-structure on $C$ we set
$$E(t)=\{f\in C^{\Delta[1]} \mid \tau_{\lt 0}(f) \;\text{ is an equivalence}\};$$
$$
  M(t)=\{f\in C^{\Delta[1]} \mid \tau_{\geq0}(f) \;\text{ is an equivalence}\}.
$$

\end{proposition}

This is [FL16, Theorem 3.13](#FL16)

\begin{proposition}
There is a natural monotone action of the group $\mathbb{Z}$ of integers on the class $TS( C )$ (now confused with the class $FS_\nu( C )$ of normal torsion theories on $C$) given by the suspension functor: $\mathbb{F}=(E,M)$ goes to $\mathbb{F}[1] = (E[1], M[1])$. 
\end{proposition}

This correspondence leads to study _families_ of $t$-structures $\{\mathbb{F}_i\}_{i\in I}$; more precisely, we are led to study _$\mathbb{Z}$-equivariant_ [[k-ary factorization system|multiple factorization systems]] $J\to TS( C )$.

\begin{proposition}
\label{StableTStructure}
Let $\mathfrak{t} \in TS(C)$ and $\mathbb{F}=(E,M)$ correspond each other under the above bijection (Prop. \ref{CorrespondenceWithNormalTorsionTheories}); then the following conditions are equivalent:

1. $\mathfrak{t}[1]=\mathfrak{t}$, i.e. $C_{\geq 1}= C_{\geq 0}$;

2. $C_{\geq 0}=*\!/E$ is a stable $\infty$-category;

3. the class $E$ is closed under pullback.

\end{proposition}

In each of these cases, we say that $\mathfrak{t}$ or $(E,M)$ is _stable_.

This is [FLM19, Theorem 6.3](#FLM19)

This results allows us to recognize _$t$-structures with stable classes_ precisely as those which are fixed in the natural $\mathbb{Z}$-action on $TS( C )$.

Two "extremal" choices of $\mathbb{Z}$-chains of $t$-structures draw a connection between two apparently separated constructions in the theory of derived categories: _Harder-Narashiman filtrations_ and _semiorthogonal decompositions_ on triangulated categories: we adopt the shorthand $\mathfrak{t}_{1,\dots, n}$ to denote the tuple $\mathfrak{t}_1\preceq \mathfrak{t}_2\preceq\cdots\preceq \mathfrak{t}_n$, each of the $\mathfrak{t}_i$ being a $t$-structure $((C_i)_{\ge 0}, (C_i)_{\lt 0})$ on $C$, and we denote similarly $\mathfrak{t}_\omega$. Then

* In the _stable case_ the tuple $t_{1,\dots, n}$ is endowed with a (monotone) $\mathbb{Z}$-action, and the map $\{0\lt 1\cdots\lt n\}\to TS( C )$ is equivariant with respect to this action; the absence of nontrivial $\mathbb{Z}$-actions on $\{0\lt 1\cdots\lt n\}$ forces each $t_i$ to be stable.
* In the _orbit case_ we consider an _infinite_ family $t_\omega$ of $t$-structures on $C$, obtained as the orbit of a fixed $(E_0, M_0)\in TS( C )$ with respect to the natural $\mathbb{Z}$-action.

### Towers

The HN-filtration induced by a $t$-structure and the factorization induced by a [[semiorthogonal decomposition]] on $C$ both are the byproduct of the _tower_ associated to a tuple $\mathfrak{t}_{1,\dots, n}$:

## Examples
 {#Examples}

The archetypical and historically motivating example (cf. [Gelfand & Manin (1996), IV.4 §1](#GelfandManin96)) is the following:

\begin{example}
\label{TStructureOnDerivedCategoryOfAbelianCategory}
**(canonical t-structure on the [[derived category]] of an [[ab

[... 正文截断于 6000 字符 ...]
