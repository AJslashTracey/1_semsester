#set page(margin: 2cm)
#set text(size: 11pt)

= Logikoperatoren

#table(
  columns: (auto, 1.5fr, 1.7fr, 2.8fr, 2.4fr),
  inset: 6pt,
  align: (center, left, left, left, left),
  stroke: 0.6pt,
  [*Operator*], [*Name*], [*Schreibweise*], [*Bedeutung*], [*Beispiel*],
  [$not p$], [Negation], [`not p`], [kehrt den Wahrheitswert um], [$not "wahr" = "falsch"$],
  [$p and q$], [Konjunktion], [`p and q`], [wahr, wenn beide wahr sind], [$"wahr" and "falsch" = "falsch"$],
  [$p or q$], [Disjunktion], [`p or q`], [wahr, wenn mindestens einer wahr ist], [$"wahr" or "falsch" = "wahr"$],
  [$p xor q$], [Exklusives Oder], [`p xor q`], [wahr, wenn genau einer wahr ist], [$"wahr" xor "wahr" = "falsch"$],
  [$p => q$],
  [Implikation],
  [`p => q`],
  [falsch nur bei wahrer Voraussetzung und falscher Folgerung],
  [$"wahr" => "falsch" = "falsch"$],

  [$p <=> q$],
  [Äquivalenz],
  [`p <=> q`],
  [wahr, wenn beide denselben Wahrheitswert haben],
  [$"wahr" <=> "wahr" = "wahr"$],

  [$not (p and q)$], [NAND], [`not (p and q)`], [Negation der Konjunktion], [$not ("wahr" and "wahr") = "falsch"$],
  [$not (p or q)$], [NOR], [`not (p or q)`], [Negation der Disjunktion], [$not ("falsch" or "falsch") = "wahr"$],
)


= Gesetze

== Kontraposition

$A => B <=> not B => not A$

Eine Implikation ist logisch äquivalent zu ihrer Kontraposition.

== De Morgansche Gesetze

$not (A and B) <=> not A or not B$

$not (A or B) <=> not A and not B$

Die Negation verteilt sich über die Klammer und vertauscht dabei `and` und `or`.

= Wahrheitstabelle

#table(
  columns: (auto, auto, auto, auto, auto, auto, auto),
  inset: 6pt,
  align: center,
  stroke: 0.6pt,
  [*$A$*], [*$B$*], [*$C$*], [*$A or B$*], [*$not C$*], [*$not (C => A)$*], [*$(A or B) and not (C => A)$*],
  [w], [w], [w], [w], [f], [f], [f],
  [w], [w], [f], [w], [w], [f], [f],
  [w], [f], [w], [w], [f], [f], [f],
  [w], [f], [f], [w], [w], [f], [f],
  [f], [w], [w], [w], [f], [w], [w],
  [f], [w], [f], [w], [w], [f], [f],
  [f], [f], [w], [f], [f], [w], [f],
  [f], [f], [f], [f], [w], [f], [f],
)
