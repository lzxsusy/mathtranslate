# monoidal category

url: https://ncatlab.org/nlab/show/monoidal+category
last_revised: 2025-08-14
---

#### Monoidal categories
+--{: .hide}
[[!include monoidal categories - contents]]

* table of contents

## Idea

A **monoidal category** is a [[category]] equipped with some notion of 'tensor product' of its [[objects]].  A good example is the category [[Vect]] of [[vector spaces]], where we can take the [[tensor product of vector spaces|traditional tensor product]], not only of vector spaces, but also of [[linear maps]]: given linear maps $f \colon V \to W$ and $f^\prime \colon V^\prime \to W^\prime$, we get a linear map

$$ f \otimes f^\prime \colon V \otimes V^\prime \to W \otimes W^\prime \,.$$

The same category can often be made into a monoidal category in more than one way.  For example the category [[Set]] can be made into a monoidal category with cartesian [[product]] or [[disjoint union]] (i.e. [[coproduct]]) as the 'tensor product'.   We can also make [[Vect]] into a monoidal category with [[direct sum]] as the 'tensor product' --- this may seem perverse, but it's actually very useful.

For any monoidal category $M$, the operation of tensor product is actually a [[functor]]:

\[
  \label{TensorProductFunctor}
  \otimes \colon  M \times M \longrightarrow M
\]

This functor, which we can think of as a kind of 'multiplication', makes $M$ into a [[vertical categorification|vertically categorified]] version of a [[monoid]].  This explains the term 'monoidal category'. 

A monoidal category can also be considered a one-object [[bicategory]]. See there for more details. 

## Definition
 {#Definition}

### General monoidal categories
 {#DefinitionGeneralMonoidalCategories}

We first give the explicit definition in components (Def. \ref{MonoidalCategory}) and then highlight the succinct abstract idea (Def. \ref{AsPseudomonoidsInCat}) underlying this.

\begin{definition}\label{MonoidalCategory}
**(monoidal category)**
\linebreak
A **monoidal category** is a [[category]] $\mathcal{C}$ equipped with 

1. a [[functor]]

   \[
     \label{TheTensorProductFunctor}
      \otimes 
        \;\colon\; 
      \mathcal{C} \times \mathcal{C}  
       \longrightarrow
      \mathcal{C}
   \]

   out of the [[product category]] of $\mathcal{C}$ with itself, called the **[[tensor product]]**, 

1. an [[object]]

   $$ 
     1 \in \mathcal{C} 
   $$

   called the **[[unit object]]** or **[[tensor unit]]**, 

1. a [[natural isomorphism]] 

   $$
     a 
       \;\colon\; 
     ((-)\otimes (-)) \otimes (-)
       \overset{\simeq}{\longrightarrow}
     (-) \otimes ((-)\otimes(-))
   $$

   with components of the form 

   \[
     \label{AssociatorInAMonoidalCategory}
     a_{x,y,z} : (x \otimes y) \otimes z \to x \otimes (y \otimes z) 
   \]

   called the **[[associator]]**, 

1. a [[natural isomorphism]] 

   \[
     \label{LeftUnitorInAMonoidalCategory}
     \lambda 
       \;\colon\; 
     (1 \otimes (-)) 
       \overset{\simeq}{\longrightarrow}
     (-)
   \]

   with components of the form 

   $$
     \lambda_x \colon 1 \otimes x \to x 
   $$

   called the **[[left unitor]]**, and

1. a [[natural isomorphism]]

   $$
     \rho \;\colon\; (-) \otimes 1 \overset{\simeq}{\longrightarrow} (-)
   $$

   with components of the form 

   $$  
     \rho_x \colon x \otimes 1 \to x 
   $$

    called the **[[right unitor]]**, 

such that the following two kinds of [[commuting diagram|diagrams commute]], for all objects involved:

1. **triangle identity** (not to be confused with the [[triangle identities]] of an [[adjunction]]):

   $$
     \array{
        & (x \otimes 1) \otimes y &\stackrel{a_{x,1,y}}{\longrightarrow} & x \otimes (1 \otimes y)
         \\     
         & {}_{\rho_x \otimes 1_y}\searrow       
         && \swarrow_{1_x \otimes \lambda_y}
         & 
        \\
        &&
        x \otimes y
        &&
     }
   $$

1. {#PentagonIdentity} the **[[pentagon identity]]** (or **pentagon equation**):

   $$
     \array{
       && (w \otimes x) \otimes (y \otimes z)
       \\
       & {}^{\mathllap{\alpha_{w \otimes x, y, z}}}\nearrow
        &&
       \searrow^{\mathrlap{\alpha_{w,x,y \otimes z}}}
       \\
       ((w \otimes x ) \otimes y) \otimes z
        && &&
       w \otimes (x \otimes (y \otimes z))
       \\
       {}^{\mathllap{\alpha_{w,x,y}} \otimes id_z }\downarrow 
        && && 
       \uparrow^{\mathrlap{ id_w \otimes \alpha_{x,y,z} }}
       \\
       (w \otimes (x \otimes y)) \otimes z
         && \underset{\alpha_{w,x \otimes y, z}}{\longrightarrow} &&
       w \otimes ( (x \otimes y) \otimes z )
     }
   $$

\end{definition}

\begin{remark}\label{InViewOfMicrocosmPrinciple}
**(role of the [[microcosm principle]])**
\linebreak
Notice how the very definition of monoidal categories (Def. \ref{MonoidalCategory}) invokes the Cartesian product *of* categories, namely in the definition of the tensor product (eq:TheTensorProductFunctor) *in* a category. But the operation of forming [[product categories]] is itself a (Cartesian) monoidal structure one level higher up in the [[higher category theory]] ladder, namely on the ambient [[2-category]] [[Cat]] of categories, which thereby becomes a [[monoidal 2-category]]. 

The ability to define pseudomonoids in any monoidal 2-category is an [example](microcosm+principle#examples) of the so-called [[microcosm principle]], where the definition of ([[higher structure|higher]]) algebraic [[mathematical structure|structures]] uses and requires analogous  algebraic structure present on the ambient higher category.  
\end{remark}

With this understood, there is a succinct abstract definition of monoidal categories:
\begin{definition}\label{AsPseudomonoidsInCat}
**(as pseudomonoids in $Cat$)**
\linebreak
A monoidal category (Def. \ref{MonoidalCategory}) is equivalently a [[pseudomonoid]] in the [[cartesian monoidal category|cartesian]] [[monoidal 2-category]] [[Cat]] of categories.
\end{definition}

\begin{remark}\label{MakingTheAmbientStructureMorphismsExplicit}
**(making the ambient structure morphisms explicit)**
\linebreak
The equivalent persp

[... 正文截断于 6000 字符 ...]
