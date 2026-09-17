
= Lesson 1 Linear Algebra
== What is a span
$bold("Span")$ is a set of vectors with which you can create any vector on that plane written as $ => c_1 dot arrow(v) + c_2 dot arrow(w) $


==Shared list
Shared list of real numbers
$ RR^2 = vec(x, y) $ $ RR^1 = RR $ $ RR^3 = vec(x, y, z) $

== Linear combination or not?
$ v_1 = vec(1, 0) v_2= vec(0, 1) b = vec(3, 4) $

Is $arrow(b)$ a linear combination of $arrow(v_1) "and" arrow(v_2)$? To solve:
$ a vec(1, 0) + b vec(0, 1) = vec(3, 4) $
$=> a = 3, b = 4$

Orthognality and the Pythagoran Theme
$ norm(arrow(v) - arrow(w))^2 = norm(v)^2 + norm(w)^2 space "if" space space arrow(v) perp arrow(w) $

== Cauchy schwarz inequality
$ abs(arrow(v) dot arrow(w)) <= norm(arrow(v)) dot norm(arrow(w)) $

$ abs(arrow(v) dot arrow(w)) = norm(arrow(v)) dot norm(arrow(w)) cos(theta) $
$ arrow cos(theta) <= 0 $

$arrow$ Dotproduct of two vectors is never larger in magnitude than the product of two vector lenghts
