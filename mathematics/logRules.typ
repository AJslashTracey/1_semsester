#import "../../templates/lecture.typ": lecture

#show: lecture.with(
  course: "Mathematics",
  title: "Log Rules",
  author: "Juri Stoffers",
  term: "1. Semester",
  date: datetime.today().display("[year]-[month]-[day]"),
)

#let logb(base, x) = $ log_(#base)(#x) $


= Logarithm Rules

== Basics


$ log_(a)(a) = 1 => a^0 = 1 $

$ log_(a)(a^x) = x => a^1 = a $

$ a^(log_(a)(x)) = x $

== Produkt Regel

$ log_(a)(x y) = log_(a)(x) + log_(a)(y) $

== Quotientenregel

$ log_(a)(x/y) = log_(a)(x)-log_(a)(y) $


== Potentregel

$ log_(a)(x^r) = r dot log_(a)(x) $

$ logb(2, 8^3) = 3 logb(2, 8) = 9 $


== Basiswechsel
$ logb(a, x) = logb(b, x) / logb(b, a) $
$ logb(a, x) = ln(x)/ln(a) $

$ logb(a, x) = logb(10, x) / logb(10, a) $



== Wichtige Identität

$ logb(a, b) = 1 / logb(b, a) $

$ logb(a, b) = 1/logb(b, a) $

$ logb(a, b) = ln(b)/ln(a) $



Typische Fehler

$ logb(a, x+y) $
