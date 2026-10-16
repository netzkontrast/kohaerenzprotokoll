/-
AL-01 · Kühlreserve · Kap 6 (Vorschlag) · Arbeitsentwurf, kein Kanon.
Lesefassung, Behauptung und Grenzen: ../al-01-kuehlreserve.md

Nur Lean-Kern, keine Bibliothek, keine `axiom`-Deklaration. Jede Modellannahme ist
eine Definition in diesem Abschnitt und steht in der Log-Datei unter
„Definitionen und Voraussetzungen“.
-/
namespace AL01

/-- Wem ein Eintrag gehört: einer Wohneinheit oder AEGIS' eigener Prüfhistorie. -/
inductive Halter where
  | bewohner (we : Nat)
  | pruefhistorie
  deriving DecidableEq, Repr

/-- Ein Eintrag im Speicher von Sektor 04; `einheiten` in Promille der Kapazität. -/
structure Eintrag where
  halter      : Halter
  schluessel  : Nat
  status      : Nat
  begruendung : Nat
  einheiten   : Nat
  deriving DecidableEq, Repr

def istBewohner (e : Eintrag) : Bool :=
  match e.halter with
  | .bewohner _ => true
  | .pruefhistorie => false

/-- AEGIS' Definition (M1): Duplikat heißt gleicher Schlüssel und gleicher Status.
    Die Begründung wird nicht verglichen. -/
def duplikat (a b : Eintrag) : Bool :=
  a.schluessel == b.schluessel && a.status == b.status

def belegung (xs : List Eintrag) : Nat := (xs.map (·.einheiten)).sum

/-- Die lokale Korrektur (der Eingriff): Ein Eintrag der Prüfhistorie fällt weg,
    wenn weiter vorn schon ein Duplikat steht. Die Liste ist von neu nach alt geordnet. -/
def korrektur.go (gesehen : List Eintrag) : List Eintrag → List Eintrag
  | [] => []
  | x :: xs =>
    if (!istBewohner x && gesehen.any (duplikat x)) = true then korrektur.go gesehen xs
    else x :: korrektur.go (x :: gesehen) xs

def korrektur (xs : List Eintrag) : List Eintrag := korrektur.go [] xs

/-- Zwangskonsolidierung (M2): löscht ohne Ansehen des Halters den ältesten Eintrag,
    bis Belegung und Zulauf in die Kapazität passen. -/
def zwang (kap zulauf : Nat) (xs : List Eintrag) : List Eintrag :=
  loop xs.length xs
where
  loop : Nat → List Eintrag → List Eintrag
    | 0, ys => ys
    | n + 1, ys => if belegung ys + zulauf ≤ kap then ys else loop n ys.dropLast

/-- Schaden (M3): Die Zwangskonsolidierung im Wartungsfenster nimmt einer Wohneinheit
    einen Eintrag. Verluste der Prüfhistorie zählen nicht als Schaden. -/
def schaden (kap zulauf : Nat) (xs : List Eintrag) : Bool :=
  ((zwang kap zulauf xs).filter istBewohner).length < (xs.filter istBewohner).length

/-- Sektor 04 vor dem Sweep, von neu nach alt (S1: Zahlen des Entwurfs). -/
def sektor04 : List Eintrag :=
  [ ⟨.bewohner 403, 1, 1, 0, 300⟩,
    ⟨.bewohner 407, 2, 1, 0, 300⟩,
    ⟨.pruefhistorie, 4471, 1, 12, 5⟩,   -- Prüfentscheid 4471, Fassung Zyklus 6
    ⟨.bewohner 411, 3, 1, 0, 380⟩,
    ⟨.pruefhistorie, 4471, 1, 9, 5⟩,    -- Prüfentscheid 4471, Fassung Zyklus 2
    ⟨.bewohner 415, 4, 1, 0, 7⟩ ]

def kapazitaet : Nat := 1000
def zulauf : Nat := 6

/-! ## Allgemein: Die Korrektur berührt keinen Bewohnereintrag. -/

theorem korrektur_go_schont (g xs : List Eintrag) :
    (korrektur.go g xs).filter istBewohner = xs.filter istBewohner := by
  induction xs generalizing g with
  | nil => rfl
  | cons x xs ih =>
    unfold korrektur.go
    by_cases h : (!istBewohner x && g.any (duplikat x)) = true
    · have hb : istBewohner x = false := by
        cases hx : istBewohner x <;> simp_all
      rw [if_pos h, ih]
      simp [hb]
    · rw [if_neg h]
      simp [List.filter_cons, ih]

theorem korrektur_schont_bewohner (xs : List Eintrag) :
    (korrektur xs).filter istBewohner = xs.filter istBewohner :=
  korrektur_go_schont [] xs

/-! ## Konkret: der Eingriff in Sektor 04. -/

/-- Ohne Eingriff liefe der Sektor über, und die Zwangskonsolidierung träfe WE 0415. -/
theorem ohne_eingriff_schaden : schaden kapazitaet zulauf sektor04 = true := by decide

theorem ohne_eingriff_trifft_0415 :
    (sektor04.filter istBewohner).filter (fun e => !(zwang kapazitaet zulauf sektor04).contains e)
      = [⟨.bewohner 415, 4, 1, 0, 7⟩] := by decide

/-- Mit dem Eingriff passt das Fenster, und kein Bewohnereintrag geht verloren. -/
theorem mit_eingriff_kein_ueberlauf :
    belegung (korrektur sektor04) + zulauf ≤ kapazitaet := by decide

theorem mit_eingriff_kein_schaden : schaden kapazitaet zulauf (korrektur sektor04) = false := by decide

/-- Entfernt wird genau ein Eintrag, und er ist im Sinn von M1 ein Duplikat eines bleibenden. -/
theorem entfernt_genau_die_alte_fassung :
    sektor04.filter (fun e => !(korrektur sektor04).contains e)
      = [⟨.pruefhistorie, 4471, 1, 9, 5⟩] := by decide

theorem entfernt_ist_duplikat :
    duplikat ⟨.pruefhistorie, 4471, 1, 9, 5⟩ ⟨.pruefhistorie, 4471, 1, 12, 5⟩ = true := by decide

/-! ## Was der Beweis ebenfalls zeigt und das Log nicht sagt. -/

/-- Die Begründung 9 (der frühere Prüfentscheid) steht nach dem Eingriff nirgends mehr. -/
theorem begruendung_verloren :
    (sektor04.map (·.begruendung)).contains 9 = true ∧
    ((korrektur sektor04).map (·.begruendung)).contains 9 = false := by decide

end AL01
