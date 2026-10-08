/-
AL-02 · Umverteilung · Kap 13 (Vorschlag) · Arbeitsentwurf, kein Kanon.
Lesefassung, Behauptung und Grenzen: ../al-02-umverteilung.md

Nur Lean-Kern, keine Bibliothek, keine `axiom`-Deklaration.
-/
namespace AL02

/-- Ein Posten einer Wartungslöschung: Wohneinheit und Umfang in Einheiten zu 10¹⁷ Bit. -/
structure Posten where
  we        : Nat
  einheiten : Nat
  deriving DecidableEq, Repr

def summe (p : List Posten) : Nat := (p.map (·.einheiten)).sum

def betroffene (p : List Posten) : List Nat := p.map (·.we)

/-- AEGIS' Zulässigkeit einer Wartungslöschung (M1–M4). -/
structure Zulaessig (soll schwelle gesperrt : Nat) (p : List Posten) : Prop where
  /-- M1: Das Soll des Fensters wird erreicht. -/
  deckt    : soll ≤ summe p
  /-- M2: Keine Wohneinheit verliert in diesem Fenster mehr als die Schwelle. -/
  schwelle : ∀ x ∈ p, x.einheiten ≤ schwelle
  /-- M3: Die Zeile mit offener Rückfrage bleibt unberührt. -/
  schont   : ∀ x ∈ p, x.we ≠ gesperrt
  /-- M4: Jede Wohneinheit steht höchstens einmal im Plan. -/
  einmalig : (betroffene p).Nodup

/-! ## Allgemein: Eine Schwelle je Person erzwingt viele Personen. -/

theorem summe_le (s : Nat) :
    ∀ p : List Posten, (∀ x ∈ p, x.einheiten ≤ s) → summe p ≤ s * p.length
  | [], _ => by simp [summe]
  | x :: xs, h => by
    have hx : x.einheiten ≤ s := h x (by simp)
    have ih := summe_le s xs (fun y hy => h y (by simp [hy]))
    simp only [summe, List.map_cons, List.sum_cons, List.length_cons] at ih ⊢
    rw [Nat.mul_succ]
    omega

/-- Jeder zulässige Plan trifft mindestens soll / schwelle verschiedene Wohneinheiten. -/
theorem mindestens_betroffen {soll s g : Nat} {p : List Posten} (h : Zulaessig soll s g p) :
    soll ≤ s * (betroffene p).length := by
  have := summe_le s p h.schwelle
  simp only [betroffene, List.length_map]
  exact Nat.le_trans h.deckt this

/-! ## Konkret: das Wartungsfenster von Sektor 04. -/

def soll : Nat := 12          -- 1,2 × 10¹⁸ Bit
def schwelle : Nat := 2       -- 2,0 × 10¹⁷ Bit je Wohneinheit
def rueckfrage : Nat := 418   -- WE 0418, Rückfrage offen

/-- Der ursprüngliche Plan: der Posten der Zeile mit Rückfrage. -/
def urspruenglich : List Posten := [⟨418, 12⟩]

/-- Die Umverteilung, die AEGIS vorschlägt. -/
def umverteilung : List Posten :=
  [⟨403, 2⟩, ⟨407, 2⟩, ⟨411, 2⟩, ⟨419, 2⟩, ⟨423, 2⟩, ⟨431, 2⟩]

theorem urspruenglich_unzulaessig : ¬ Zulaessig soll schwelle rueckfrage urspruenglich :=
  fun h => h.schont ⟨418, 12⟩ (by simp [urspruenglich]) rfl

theorem umverteilung_zulaessig : Zulaessig soll schwelle rueckfrage umverteilung :=
  ⟨by decide, by decide, by decide, by decide⟩

/-- Kein zulässiger Plan dieses Fensters trifft weniger als sechs Wohneinheiten. -/
theorem jeder_zulaessige_plan_trifft_sechs (p : List Posten)
    (h : Zulaessig soll schwelle rueckfrage p) : 6 ≤ (betroffene p).length := by
  have := mindestens_betroffen h
  simp only [soll, schwelle] at this
  omega

/-- Vorher eine Wohneinheit, nachher sechs; der Umfang bleibt gleich. -/
theorem preis :
    (betroffene urspruenglich).length = 1 ∧ (betroffene umverteilung).length = 6 ∧
    summe urspruenglich = summe umverteilung := by decide

end AL02
