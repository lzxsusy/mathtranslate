# 源片段 tr01a（底本：Introduction）

<<B012 p>>
In this talk I aim to provide a brief overview of SYZ mirror symmetry proposal from a more mathematical point of view. Recall that the _Homological Mirror Symmetry_ proposal of Kontsevich [[Kon94]] states that there are pairs of (not necessarily smooth) varieties $(X,\omega ,J)$ and $(\check{X},\check{\omega},\check{J})$ such that $$ D^{\pi}\mathcal{Fuk} (X,\omega)\simeq D^b\operatorname{Coh} (\check{X},\check{J})\quad\text{and}\quad D^b\operatorname{Coh} (X,J)\simeq D^{\pi}\mathcal{Fuk} (\check{X},\check{\omega}), $$where $\mathcal{Fuk} (X,\omega)$ is a version of the "Fukaya category" for the symplectic variety $(X,\omega)$ and $D^b\operatorname{Coh} (X,J)$ is the bounded derived category of coherent sheaves on the complex variety $(X,J)$, whenever they're well-defined. On the algebraic (which we call _B-model_) side, there's a famous theorem of Bondal and Orlov [[BO01]] stating that we can re-construct a smooth projective variety $X$ from its derived category of coherent sheaves $D^b\operatorname{Coh} (X)$.

<<B013 env>>
[ENV] **Theorem(Bondal-Orlov).** Let $X$ be a smooth projective variety and $Y$ an algebraic variety such that either the canonical sheaf $K_X$ or the anti-canonical sheaf $-K_X$ is ample, then for any equivalence of derived categories$$D^b\operatorname{Coh} (X)\xrightarrow[\cong]{f} D^b\operatorname{Coh} (Y),$$there exists an isomorphism of schemes $\varphi\colon X\xrightarrow{\cong} Y$ such that $D^b(\varphi_{\ast})=f$.

<<B014 prf>>
[PRF] **Sketch of Proof.** As will be important for the SYZ picture, let's briefly explain the idea of proof of this theorem. Firstly, assume that $X$ and $Y$ are both projective with coordinate algebras $B_X=\bigoplus_{i=0}^{\infty} H^i (X,\mathcal{O}_X(i))$ and $B_Y=\bigoplus_{i=0}^{\infty} H^i (Y,\mathcal{O}_Y (i))$, then any graded isomorphism $B_X\cong B_Y$ will induce an isomorphism of the corresponding varieties $X\cong Y$. As we have known that $X$ is projective with ample canonical or anti-canonical divisor $\pm K_X$, it suffices to find from the isomorphism of derived categories $D^b\operatorname{Coh} (X)\xrightarrow{f}\mathcal{D}$ the image of $\mathcal{O}_X(1)$, or equivalently $\pm K_X$, and show that it's represented by an ample divisor in $Y$. To achieve this, we need a non-commutative notion of "ample divisor" in order to sort out the corresponding object in the abstract derived category $\mathcal{D}$. In an abstract triangulated category $\mathcal{D}$ together with a _Serre functor_, i.e. an automorphism $S_{\mathcal{D}}\colon\mathcal{D}\to\mathcal{D}$ such that $\operatorname{Hom}_{\mathcal{D}} (A,B)\cong\operatorname{Hom}_{\mathcal{D}} (B,SA)^{\ast}$ for any $A,B\in\mathcal{D}$, we can define _point objects_ as follows: an object $P$ is a point object of codimension $s$, if

<<B015 li>>
- $S_{\mathcal{D}} (P)\simeq P[s]$,

<<B016 li>>
- $\operatorname{Hom}^{\leq 0} (P,P)=0$,

<<B017 li>>
- $\operatorname{Hom}^0 (P,P)=k(P)$,

<<B018 p>>
where $k(P)$ is an extension field of $k$. It's clear that skyscraper sheaves in $X$ are naturally point objects in $D^b\operatorname{Coh} (X)\simeq\mathcal{D}$, and vice versa any point objects in $D^b\operatorname{Coh} (X)$ are shifts of skyscraper sheaves on $X$. As this is a purely categorical notion, isomorphism classes of point objects in $\mathcal{D}$ are in one-to-one correspondence with isomorphism classes of point objects in $D^b\operatorname{Coh} (X)$. The above argument only provides identifications between the set of closed points of varieties $X$ and $Y$, and we need to identify the corresponding topologies as well as the scheme structure. The essential ingredient for the topology (and for the ultimate isomorphism) is a categorical notion of _line bundles_, or in algebro-geometric language _invertible sheaves_. An object of $\mathcal{D}$ is called _invertible_ if for any point object $P\in\mathcal{D}$, we can find $s\in\mathbb{Z}$ such that

<<B019 li>>
- $\operatorname{Hom}^s (L,P)=k(P)$,

<<B020 li>>
- $\operatorname{Hom}^i (L,P)=0$, for $i\neq s$.

<<B021 p>>
Such objects can also be shown to be isomorphic to a line bundle up to shift, if $\mathcal{D}$ comes from the derived category of a variety. Now fix a line bundle $L_0$ of $X$, and consider point objects $P$ such that $\operatorname{Hom} (L_0, P)=k(P)$. These would be the unshifted skyscraper sheaves of $Y$, and for any pairs of invertible sheaves $L_1, L_2$ with a morphism $\alpha\colon L_1\to L_2$, the induced morphism $$\Hom (L_2,P)\xrightarrow{\alpha_P^{\ast}}\Hom (L_1, P)$$defines a set of point objects $U_{\alpha} =\{P\vert\alpha_P^{\ast}\neq 0\}$. As $X$ is projective, such $U_{\alpha}$ forms a basis of the Zariski topology of $X$ as $\alpha$ runs over all invertible objects $L_1, L_2$ such that $\Hom^0 (L_i, P)=k(P)$. As for any algebraic variety, such open sets always form a basis of the corresponding Zariski topology [[ND20]], this actually shows that $X$ and $Y$ are homeomorphic as topological spaces. The remaining task is to determine the canonical/anticanonical sheaf and show that the variety $Y$ is also Fano/general type. For the fixed invertible sheaf $L_0$, we can consider the line bundle $L_i=S^i L_0 [-ni]$, then $L_i$s are also line bundles in $X$ (and also in $Y$), the algebra $\bigoplus_{i=0}^{\infty}\Hom (L_0, L_i)$ is then the endomorphism algebra of the canonical sheaf on $X$, and also on $Y$. Now as $\omega_X$ is either ample or anti-ample, open sets $\{U_{\alpha}\}$ for $\alpha\in\Hom (L_i, L_j)$ for all $i,j$ suffices to form a basis of the Zariski topology, and this is an if-and-only-if condition, so that the corresponding canonical sheaf $\omega_Y$ should also be ample and anti-ample. Now the first paragraph makes sense and we get an isomorphism $X\cong Y$.

<<B022 p>>
Based on the resconstruction theorem, we can roughly "re-construct" an algebraic variety from its derived category of coherent sheaves, assuming it's Fano or general type. Let's ignore the condition and use it as a heuristic. Now we have a source of category coming from symplectic geometry: for each symplectic manifold $(X,\omega)$ we can propose an $A_{\infty}$-category $\mathcal{Fuk} (X,\omega)$ which, if the mirror exists, is supposed to be an $A_{\infty}$-enhancement of the derived category of coherent sheaves of some algebraic variety $\check{X}$, and in particular we should be able to re-construct $X$ from the category $\mathcal{Fuk} (X,\omega)$. Assuming $\check{X}$ is separated, from [[ND20]] it suffices for us to determine the point objects and the invertible objects.

<<B023 p>>
Let $p\in\check{X}$ be a smooth closed point of the algebraic variety $(\check{X},\check{J})$, and let $\mathcal{O}_p$ be the structure sheaf of the closed point $p$. Then we can directly compute that
