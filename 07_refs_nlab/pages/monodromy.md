# monodromy

url: https://ncatlab.org/nlab/show/monodromy
last_revised: 2026-11-09
---

#### Homotopy theory
+--{: .hide}
[[!include homotopy - contents]]

Hence this defines a "[[permutation representation|permutation]] [[groupoid representation]]" of $\Pi_1(X)$.

+-- {: .num_prop}
###### Proposition

Given a [[homomorphism]] between two [[covering spaces]] $E_i \overset{p_i}{\to} X$, hence a [[continuous function]] $f \colon E_1 \to E_2$ which respects [[fibers]] in that the [[diagram]]

$$
  \array{
    E_1 && \overset{f}{\longrightarrow} && E_2
    \\
    & {}_{\mathllap{p_1}}\searrow && \swarrow_{\mathrlap{p_2}}
    \\
    && X
  }
$$

[[commuting diagram|commutes]], then the component functions

$$
  f\vert_{\{x\}} \;\colon\; p_1^{-1}(\{x\}) \longrightarrow p_2^{-1}(\{x\})
$$

are compatible with the monodromy $Fib_{E}$ (def. \ref{CoveringSpaceMonodromy}) along any [[path]] $\gamma$ between points $x$ and $y$ from def. \ref{CoveringSpaceMonodromy} in that the following [[diagrams]] of [[sets]] [[commuting diagram|commute]]

$$
  \array{
     p_1^{-1}(x) &\overset{f\vert_{\{x\}}}{\longrightarrow}& p_2^{-1}(x)
     \\
     {}^{\mathllap{Fib_{E_1}([\gamma])}}\downarrow
       &&
     \downarrow^{\mathrlap{ Fib_{E_2}([\gamma]) }}
     \\
     p_1^{-1}(y) &\underset{f\vert_{\{y\}}}{\longrightarrow}& p_2^{-1}(y)
  }
  \,.
$$

This means that $f$ induces a [[natural transformation]] between the monodromy functors of $E_1$ and $E_2$, respectively, and hence that constructing monodromy is itself a functor from the [[category]] of [[covering spaces]] of $X$ to that of [[permutation representations]] of the [[fundamental groupoid]] of $X$:

$$
  Fib
   \;\colon\;
  Cov(X)
    \longrightarrow
  Set^{\Pi_1(X)}
  \,.
$$

### Properties

+-- {: .num_remark}
###### Remark
**([[fundamental theorem of covering spaces]])**

The [[reconstruction of covering spaces from monodromy]] is an [[inverse functor]] to the monodromy functor. The resulting [[equivalence of categories]]

$$
  Cov(X)
    \underoverset
      {\underset{Fib}{\longrightarrow}}
      {\overset{Rec}{\longleftarrow}}
      {}
  Set^{\Pi_1(X)}
$$

between the [[category of covering spaces]] and the [[permutation representation|permutation]] [[groupoid representations]] of the [[fundamental groupoid]] is known as the _[[fundamental theorem of covering spaces]]_.

+-- {: .proof}
###### Proof

By the uniqueness of the path-lifting ([this lemma](covering+space#CoveringSpacePathLifting)) and the very definition of the [[monodromy]] functor.

+-- {: .proof}
###### Proof

By example \ref{CoveringSpaceFundamentalGroupoid}.
