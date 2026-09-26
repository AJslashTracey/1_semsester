= Equation Systems from Matrices

A system of $m$ linear equations in $n$ unknowns can be written compactly as

$ A x = b. $

Here, the coefficient matrix, the vector of unknowns, and the right-hand-side vector are

$
  A = mat(
    a_(1,1), a_(1,2), dots.h, a_(1,n);
    a_(2,1), a_(2,2), dots.h, a_(2,n);
    dots.v, dots.v, dots.down, dots.v;
    a_(m,1), a_(m,2), dots.h, a_(m,n)
  ) in RR^(m times n),
$

$
  x = vec(x_1, x_2, dots.v, x_n) in RR^n
  quad "and" quad
  b = vec(b_1, b_2, dots.v, b_m) in RR^m.
$

== Dimensions

The matrix-vector product is defined because the inner dimensions agree:

$ (m times n)(n times 1) = m times 1. $

Therefore, $A x$ and $b$ are both column vectors in $RR^m$.

== Matrix-vector multiplication

Multiplying $A$ by $x$ forms one dot product for each row of $A$:

$
  A x = vec(
    a_(1,1) x_1 + a_(1,2) x_2 + dots.h + a_(1,n) x_n,
    a_(2,1) x_1 + a_(2,2) x_2 + dots.h + a_(2,n) x_n,
    dots.v,
    a_(m,1) x_1 + a_(m,2) x_2 + dots.h + a_(m,n) x_n
  ).
$

The $i$-th entry of the product is

$ (A x)_i = sum_(j=1)^n a_(i,j) x_j. $

== Equivalent equation system

Thus, the matrix equation $A x = b$ is equivalent to the system

$
  cases(
    a_(1,1) x_1 + a_(1,2) x_2 + dots.h + a_(1,n) x_n = b_1,
    a_(2,1) x_1 + a_(2,2) x_2 + dots.h + a_(2,n) x_n = b_2,
    dots.v,
    a_(m,1) x_1 + a_(m,2) x_2 + dots.h + a_(m,n) x_n = b_m.
  )
$

Each row of $A$ corresponds to one equation, and each column of $A$ corresponds to one unknown.
