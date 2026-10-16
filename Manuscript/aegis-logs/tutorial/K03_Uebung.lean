/- Übungsdatei, erzeugt aus K03.lean von `python3 scripts/aegis_logs.py exercises` — nicht von Hand ändern.
   Ersetze jedes `sorry` durch einen Beweis; die Lösungen stehen am Ende von K03.lean. -/
/-
Lean-Tutorial · Lektion 3 · Kap 3 „Der fehlende Schritt“ · Übungsmaterial, kein Kanon.
Begleittext: lektion-3-der-fehlende-schritt.md · Übungen: K03_Uebung.lean

Was hier gelernt wird: Rekursion, Beweis durch Induktion, `simp` und `omega`,
ein allgemeiner Satz und seine Anwendung auf einen Fall, und was `sorry`
und `#print axioms` über eine Lücke sagen.
Die Zahlen kommen aus Entwurf J und Kap 2 A: 210 Schritte, dann 209; 0,73 m.
-/
namespace K03

/-! ## 1. Zweimal zählen: im Fuß und im Kopf

„Ich zähle jeden Schritt zweimal, einmal im Fuß und einmal im Kopf, und wenn
die beiden Zahlen nicht gleichzeitig ankommen, fange ich den Schritt noch einmal an.“ -/

/-- Ein Schritt, in Zentimetern. -/
abbrev Schritt := Nat

/-- Der Fuß zählt Schritt für Schritt. -/
def fuss : List Schritt → Nat
  | []      => 0
  | _ :: xs => fuss xs + 1

/-- Der Kopf nimmt die Länge der Liste. -/
def kopf (xs : List Schritt) : Nat := xs.length

/-- Die beiden Zählungen stimmen immer überein, in jedem Korridor. Beweis durch Induktion:
    für den leeren Weg, und vom Weg `xs` auf den Weg mit einem Schritt mehr. -/
theorem fuss_gleich_kopf (xs : List Schritt) : fuss xs = kopf xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp [fuss, kopf, ih]

/-! ## 2. Was ein fehlendes Stück Korridor mit der Zählung macht -/

/-- Wie viele ganze Schritte ein Weg hat. -/
def schritte (laenge schrittlaenge : Nat) : Nat := laenge / schrittlaenge

/-- Allgemein: Fehlt einem Weg aus `n` ganzen Schritten genau eine Schrittlänge,
    dann zählt man genau einen Schritt weniger. -/
theorem ein_stueck_ein_schritt (n s : Nat) (hs : 0 < s) :
    schritte (n * s - s) s = n - 1 := by
  unfold schritte
  rw [← Nat.sub_one_mul]
  exact Nat.mul_div_cancel _ hs

/-- Der Fall aus Kap 1: Delta-7, Abschnitt 2 verliert 0,73 m, und Kaels Schritt ist 73 cm.
    Von der Bank bis zur Tür: 210 Schritte, danach 209. -/
theorem zweihundertneun : schritte (210 * 73 - 73) 73 = 209 :=
  ein_stueck_ein_schritt 210 73 (by decide)

/-! ## 3. Der Abgleich löscht den Beleg (A Story Requirements: Learning)

„Jeder erfolgreiche Abgleich entfernt einen Beleg des fehlenden Schritts.“ -/

/-- Eine Abweichung zwischen Register und Messung, Stelle für Stelle. -/
def abweichungen : List Nat → List Nat → Nat
  | r :: rs, m :: ms => (if r = m then 0 else 1) + abweichungen rs ms
  | _, _ => 0

/-- Der Abgleich der Stadt: Das Register wird durch die Messung ersetzt. -/
def abgleich (_register messung : List Nat) : List Nat := messung

/-- Nach dem Abgleich gibt es keine Abweichung mehr — für jedes Register und jede Messung. -/
theorem nach_abgleich_kein_beleg (register messung : List Nat) :
    abweichungen (abgleich register messung) messung = 0 := by
  unfold abgleich
  induction messung with
  | nil => rfl
  | cons m ms ih => simp [abweichungen, ih]

/-- Vorher gab es einen: das Register von Kap 1 gegen Kaels Messung in Kap 3. -/
theorem vorher_ein_beleg : abweichungen [210, 312] [209, 312] = 1 := by decide

/-- Was bleibt, liegt außerhalb des Registers: Kaels Messung, die er nicht einträgt. -/
structure Notiz where
  schritte : Nat
  eingetragen : Bool

def kaels_messung : Notiz := ⟨209, false⟩

theorem nur_er_weiss : kaels_messung.eingetragen = false ∧ kaels_messung.schritte ≠ 210 := by decide

/-! ## Übungen — ersetze jedes `sorry` durch einen Beweis -/

/-- Übung 3.1 · Zwei Wege hintereinander: Der Fuß zählt so viel wie beide Wege zusammen.
    Tipp: Induktion über `xs`, dann `simp [fuss, ih]` und `omega`. -/
theorem fuss_append (xs ys : List Schritt) : fuss (xs ++ ys) = fuss xs + fuss ys := by
  sorry

/-- Übung 3.2 · Von der Bank bis zur Konsole sind es 312 Schritte, „und heute sind es dreihundertzwölf“.
    Tipp: `decide`. -/
theorem konsole_unveraendert : schritte (312 * 73) 73 = 312 := by
  sorry

/-- Übung 3.3 · Fehlen zwei Schrittlängen, fehlen zwei Schritte. Tipp: wie `ein_stueck_ein_schritt`,
    mit `Nat.sub_sub`, `Nat.two_mul` und `Nat.sub_mul`. -/
theorem zwei_stuecke (n s : Nat) (hs : 0 < s) :
    schritte (n * s - s - s) s = n - 2 := by
  sorry

end K03
