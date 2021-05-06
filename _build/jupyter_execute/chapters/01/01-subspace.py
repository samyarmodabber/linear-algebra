# Subspace

In this section we consider the vector space $\left( V,F,+,\cdot  \right)$ while we write $V$.

## Definition
 
**Subspace** 

Let $V$ be a vector space. $W\subseteq V$is called a subspace of $V$if $\left( W,F,+,\cdot  \right)$ be a vector space.

Theorem
Let $V$be a vector space and $W\subseteq V$. $W$ is a subspace of $V$iff the following two conditions hold:
1.	$0\in W$
2.	$\forall a\in F\ \ \forall u,v\in W\ \ \ \ au+v\in W.$

## Theorem

Let $V$be a vector space and $\left\{ {{W}_{i}} \right\}_{i=1}^{\infty }$ be a family of the subspace of $V$ then $\bigcap\limits_{i=1}^{\infty }{{{W}_{i}}}$ ia a subspace of $V$.


## Definition

**Sum**

If ${{S}_{1}},\ {{S}_{2}}$ are two nonempty subset of $V$ then sum of  ${{S}_{1}},\ {{S}_{2}}$ denote by ${{S}_{1}},\ {{S}_{2}}$ and define by

$${{S}_{1}}+{{S}_{2}}=\left\{ {{s}_{1}}+{{s}_{2}}\left| {{s}_{i}}\in {{S}_{1}}\ for\ i=1,2 \right. \right\}$$

**Direct sum**

If ${{W}_{1}},\ {{W}_{2}}$ are two subspace of $V$ then $W$ is called the direct sum of ${{W}_{1}},\ {{W}_{2}}$ and denote $W$ by ${{W}_{1}}\oplus {{W}_{2}}$ if

$$\forall w\in W\ \ \ \exists !\ {{w}_{1}}\in {{W}_{1}},\ {{w}_{2}}\in {{W}_{2}}\ \ \ w={{w}_{1}}+{{w}_{2}}$$

## Theorem
Let ${{W}_{1}},\ {{W}_{2}}$ be subspaces of $V$ then ${{W}_{1}}\oplus {{W}_{2}}$ is a subspace of $V$.

## Theorem
Let ${{W}_{1}},\ {{W}_{2}}$ be subspaces of $\left( V,F,+,\cdot  \right)$ and $W={{W}_{1}}+{{W}_{2}}$then $W={{W}_{1}}\oplus {{W}_{2}}$  iff one of the following two conditions holds:
1.	$\forall {{w}_{1}}\in {{W}_{1}},\ {{w}_{2}}\in {{W}_{2}}\ \ \ {{w}_{1}}+{{w}_{2}}=0\ \Rightarrow {{w}_{1}}={{w}_{2}}=0$
2.	${{W}_{1}}\bigcap {{W}_{2}}=\left\{ 0 \right\}$

## Definition

**Coset**

If $W$ be a subspace of $V$ and $v\in V$ then $\left\{ v \right\}+W$ is called the coset of $W$ containing $v$and denote $v+W$(or simply $\left[ v \right]$).

**Quotient**

The quotient of $V$by a subspace $W$is denote by ${}^{V}/{}_{W}$(read  $V$ mod $W$ or $V$ by $W$) and define by
${}^{V}/{}_{W}=\left\{ \left[ v \right]\left| v\in V \right. \right\}$

## Theorem

Let $V$ be a vector space, $W$be a subspace of $V$and $v,u\in V$, then
1.	$v+W$ be a coset of $V$iff $v\in W$.
2.	$v+W=u+W$ iff $v-u\in W$

### Theorem
The quotient of $V$by a subspace $W$is a vector space with following operators:

$$\forall a\in F\ \ \ \forall \left[ v \right],\ \left[ u \right]\ \in {}^{V}/{}_{W}\ \ \ \ \left[ v \right]+\left[ u \right]=\left[ v+u \right]\ \ \ \ a\left[ v \right]=\left[ av \right]$$