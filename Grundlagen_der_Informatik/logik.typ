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


= Wahrheitstabelle


