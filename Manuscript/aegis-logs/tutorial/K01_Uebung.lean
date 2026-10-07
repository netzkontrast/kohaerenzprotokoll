/- Übungsdatei, erzeugt aus K01.lean von `python3 scripts/aegis_logs.py exercises` — nicht von Hand ändern.
   Ersetze jedes `sorry` durch einen Beweis; die Lösungen stehen am Ende von K01.lean. -/
/-
Lean-Tutorial · Lektion 1 · Kap 1 „Vorkühlung“ · Übungsmaterial, kein Kanon.
Begleittext: lektion-1-vorkuehlung.md · Übungen: K01_Uebung.lean

Was hier gelernt wird: Typen und Strukturen, `Option`, `def`, `#eval`,
Listen und `match`, die ersten Beweise mit `rfl` und `decide`, und `≠`.
Die Zahlen kommen aus Entwurf J (Manuscript/kap-01/entwurf-j-rueckfrage.md).
-/
namespace K01

/-! ## 1. Eine Zeile auf Kaels Konsole -/

/-- Was eine Zeile ist. Der Anschluss hat keinen: `DATENTYP —`. -/
inductive Datentyp where
  | messreihe | sitzbank | lied | korridor
  deriving DecidableEq, Repr

/-- Eine Zeile der Zuweisung. Umfang in Bit; ein fehlender Datentyp ist `none`. -/
structure Zeile where
  name      : String
  bit       : Nat
  datentyp  : Option Datentyp
  deriving Repr

def messreihe : Zeile := ⟨"DOPPELT ABGELEGTE MESSREIHE", 210000000000, some .messreihe⟩
def anschluss : Zeile := ⟨"ANSCHLUSS OHNE PLANEINTRAG · WE 0418", 220000000000000000000000000000, none⟩
def bank      : Zeile := ⟨"SITZBANK · DELTA-7 · ABSCHNITT 3", 31000000000000000000, some .sitzbank⟩

#eval anschluss.datentyp          -- none: Lean zeigt die Lücke, wie die Konsole „—“ zeigt

/-- Der erste Beweis: Der Anschluss hat keinen Datentyp. `rfl` heißt: Lean rechnet nach und es stimmt. -/
theorem anschluss_ohne_typ : anschluss.datentyp = none := rfl

/-! ## 2. Kael rechnet (A-MC Unique Ability: Thought) -/

/-- „Ich teile die Zahl meiner Zeile durch die Zahl der Bank. Es kommen sieben Milliarden heraus.“ -/
def baenke : Nat := anschluss.bit / bank.bit

#eval baenke                      -- 7096774193

theorem sieben_milliarden : 7000000000 ≤ baenke ∧ baenke < 8000000000 := by decide

/-! ## 3. Der Tag als Liste von Ereignissen -/

/-- Was Kael an der Konsole tut. -/
inductive Ereignis where
  | bestaetigen (n : Nat)   -- n Zeilen bestätigt, die Zuweisung sinkt um n
  | rueckfrage              -- die linke Hand: nichts wird bestätigt
  | verlassen               -- 16:31, die Schicht endet vorzeitig
  deriving Repr

/-- Wie ein Ereignis die Zuweisung ändert. `match` unterscheidet die Fälle. -/
def schritt (zuweisung : Nat) : Ereignis → Nat
  | .bestaetigen n => zuweisung - n
  | .rueckfrage    => zuweisung
  | .verlassen     => zuweisung

/-- Der ganze Tag: von links nach rechts gefaltet. -/
def tag (start : Nat) (es : List Ereignis) : Nat := es.foldl schritt start

/-- Kap 1 nach Entwurf J: 388 am Morgen, 201 um elf, die Rückfrage, 37 um 16:31. -/
def kap1 : List Ereignis :=
  [.bestaetigen 187, .rueckfrage, .bestaetigen 164, .verlassen]

#eval tag 388 kap1                -- 37

/-! ## 4. Das Ziel und warum es verfehlt wird -/

/-- Kaels Want als Aussage: Der Tag ist richtig, wenn die Zuweisung auf null steht. -/
abbrev richtig (start : Nat) (es : List Ereignis) : Prop := tag start es = 0

/-- Die Wendung von Kap 1, bewiesen: Der Tag ist nicht richtig. -/
theorem kap1_nicht_richtig : ¬ richtig 388 kap1 := by decide

/-- Und warum: Bis 16:31 fehlen genau die 37 Zeilen, die er nicht mehr bestätigt hat. -/
theorem es_fehlen_37 : tag 388 (kap1 ++ [.bestaetigen 37]) = 0 := by decide

/-- Die Rückfrage allein ändert keine Zahl: Sie ist kein Fortschritt in der Zuweisung. -/
theorem rueckfrage_aendert_nichts (z : Nat) : schritt z .rueckfrage = z := rfl

/-! ## 5. Die Abwärme: Bit und Joule (Landauer)

Die Stadt rechnet jede Löschung in Wärme um. Bei 21 °C kostet ein Bit
etwa 2,8149 × 10⁻²¹ J. Wir rechnen in Einheiten von 10⁻²⁵ J, damit alles
eine natürliche Zahl bleibt. -/

def landauer (bit : Nat) : Nat := bit * 28149   -- in 10⁻²⁵ J

/-- Die Messreihe: „0,00000000059 Joule“ heißt 5,9 × 10⁻¹⁰ J = 5 900 000 000 000 000 Einheiten. -/
theorem messreihe_joule :
    5900000000000000 ≤ landauer messreihe.bit ∧ landauer messreihe.bit < 6000000000000000 := by decide

/-! ## Übungen — ersetze jedes `sorry` durch einen Beweis -/

/-- Übung 1.1 · Die Bank hat einen Datentyp, anders als der Anschluss. Tipp: `decide`. -/
theorem bank_hat_typ : bank.datentyp ≠ none := by
  sorry

/-- Übung 1.2 · „sechshundertachtzehn Millionen Joule“: Die Abwärme des Anschlusses liegt zwischen
    6,1 × 10⁸ und 6,2 × 10⁸ J, in Einheiten von 10⁻²⁵ J. Tipp: wie `messreihe_joule`. -/
theorem anschluss_joule :
    6100000000000000000000000000000000 ≤ landauer anschluss.bit ∧
    landauer anschluss.bit < 6200000000000000000000000000000000 := by
  sorry

/-- Übung 1.3 · Zwei Rückfragen hintereinander ändern die Zuweisung nicht. Tipp: `rfl`, Lean rechnet `tag` aus. -/
theorem zwei_rueckfragen (z : Nat) : tag z [.rueckfrage, .rueckfrage] = z := by
  sorry

/-- Übung 1.4 · Ohne die linke Hand und ohne den Weg zur Bank wäre der Tag richtig gewesen:
    187 Zeilen bis elf, 201 danach. Tipp: `decide`. -/
theorem ohne_hand_richtig : richtig 388 [.bestaetigen 187, .bestaetigen 201] := by
  sorry

end K01
