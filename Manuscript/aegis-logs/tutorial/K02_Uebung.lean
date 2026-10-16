/- Übungsdatei, erzeugt aus K02.lean von `python3 scripts/aegis_logs.py exercises` — nicht von Hand ändern.
   Ersetze jedes `sorry` durch einen Beweis; die Lösungen stehen am Ende von K02.lean. -/
/-
Lean-Tutorial · Lektion 2 · Kap 2 „Die Rolle hält“ · Übungsmaterial, kein Kanon.
Begleittext: lektion-2-die-rolle-haelt.md · Übungen: K02_Uebung.lean

Was hier gelernt wird: Aussagen (`Prop`), `∧`, `∨`, `¬`, `→`, `∃` mit seinem Zeugen,
die Taktiken `intro`, `exact`, `constructor`, `cases`, und Idempotenz.
Die Zahlen kommen aus Kap 2, Entwurf A (Manuscript/kap-02/entwurf-a-die-rolle-haelt.md).
-/
namespace K02

/-! ## 1. Die Frist (A Catalyst: Threat) -/

/-- „Elf Tage. … zweihundertvierundsechzig Stunden.“ -/
theorem frist_in_stunden : 11 * 24 = 264 := rfl

/-- Am Abend steht auf der Wand: „FRIST: 10 TAGE 12 STUNDEN“. Ein Arbeitstag ist vergangen. -/
theorem frist_am_abend : 11 * 24 - 12 = 10 * 24 + 12 := rfl

/-! ## 2. Der offene Posten der Kollegin (A-OS Concern: Conceptualizing)

Die Kollegin an der Konsole rechts notiert drei Abweichungen und sagt:
„Er schließt, wenn ich eine Ursache habe, die ich prüfen kann.“
In Lean ist eine Ursache, die man prüfen kann, ein Beweis. -/

inductive Abweichung where
  | ankunft      -- 07:43 statt 07:31: die zwölf Minuten
  | rueckfrage   -- 11:04: Rückfrage auf die eigene Wohneinheit
  | ausgang      -- 16:31: vor der Null gegangen
  deriving DecidableEq, Repr

/-- Was Kael als Ursache anbieten könnte. -/
inductive Ursache where
  | wartungsplan   -- „Die Wartung.“
  | linkeHand      -- „Meine Hand hat eine Rückfrage gestellt, die ich nicht stellen wollte.“
  | altFrau        -- die Bank, 16:40
  deriving DecidableEq, Repr

/-- Welche Abweichung eine Ursache erklärt. Das ist das Modell, nicht die Welt. -/
def erklaert : Ursache → Abweichung → Bool
  | .wartungsplan, .rueckfrage => true
  | .linkeHand,    .rueckfrage => true
  | .altFrau,      .ausgang    => true
  | _,             _           => false

/-- Wen eine Ursache belastet, wenn sie geprüft wird. -/
def belastet : Ursache → String
  | .wartungsplan => "H. Tamm, Freigabe Wartungsplan Sektor 04"
  | .linkeHand    => "Kael"
  | .altFrau      => "Kael"

/-- Der Posten schließt, wenn jede Abweichung eine Ursache hat. -/
def schliesst (us : List Ursache) : Prop :=
  ∀ a : Abweichung, ∃ u, u ∈ us ∧ erklaert u a = true

/-! ## 3. `∃` braucht einen Zeugen -/

/-- Für die Rückfrage gibt es eine Ursache: Der Zeuge ist der Wartungsplan. -/
theorem rueckfrage_hat_ursache : ∃ u, erklaert u .rueckfrage = true :=
  ⟨.wartungsplan, rfl⟩

/-- Der Zeuge, den Kael wählt, belastet einen anderen. -/
theorem zeuge_belastet_tamm : belastet .wartungsplan ≠ "Kael" := by decide

/-- „Die Wartung erklärt eine Zeile. Sie erklärt nicht, wo Sie gestern Morgen waren.“ -/
theorem wartung_schliesst_nicht : ¬ schliesst [.wartungsplan] := by
  intro h                                   -- angenommen, der Posten schlösse
  obtain ⟨u, hu, he⟩ := h .ankunft           -- dann gäbe es eine Ursache für die Ankunft
  simp at hu                                -- die einzige angebotene ist der Wartungsplan
  subst hu
  simp [erklaert] at he                     -- und der erklärt die Ankunft nicht

/-- Für die zwölf Minuten gibt es im Modell überhaupt keine Ursache. -/
theorem zwoelf_minuten_ohne_zeugen : ∀ u, erklaert u .ankunft = false := by
  intro u
  cases u <;> rfl

/-- Darum schließt kein Angebot den Posten, auch das ehrlichste nicht. -/
theorem nichts_schliesst (us : List Ursache) : ¬ schliesst us := by
  intro h
  obtain ⟨u, _, he⟩ := h .ankunft
  rw [zwoelf_minuten_ohne_zeugen u] at he
  exact Bool.false_ne_true he

/-! ## 4. 251: „Ein Ausgleich, der zurückkommt, ist kein Ausgleich.“ -/

/-- Die neunte Stelle hinter dem Komma der Messreihe 251. -/
structure Stelle where
  ziffer : Nat
  deriving DecidableEq, Repr

def korrigiere (_ : Stelle) : Stelle := ⟨4⟩       -- Kael macht die Drei zur Vier
def nacht (_ : Stelle) : Stelle := ⟨3⟩            -- am Morgen steht wieder eine Drei

/-- Ein Ausgleich ist idempotent: zweimal korrigiert ist einmal korrigiert. -/
theorem korrigiere_idempotent (s : Stelle) : korrigiere (korrigiere s) = korrigiere s := rfl

/-- Aber die Nacht macht ihn ungeschehen: Die Korrektur hält nicht über das Fenster. -/
theorem fehler_der_wartet : nacht (korrigiere ⟨3⟩) ≠ korrigiere ⟨3⟩ := by decide

/-! ## 5. Zwei Belege, die sich widersprechen — als Daten, nicht als P und ¬P -/

/-- Wer was über die Bank sagt, in 10¹⁸ Bit. -/
structure Beleg where
  quelle : String
  bit    : Nat

def register  : Beleg := ⟨"Liste Kap 1: SITZBANK", 31⟩
def inventar  : Beleg := ⟨"Inventar Delta-7: ANHAFTENDES OHNE EINTRAG", 28⟩

/-- „Neun Zehntel davon waren nicht die Bank.“ Mehr als 9/10 des Registerwerts war Anhaftendes. -/
theorem neun_zehntel : 9 * register.bit < 10 * inventar.bit ∧ inventar.bit < register.bit := by decide

/-! ## Übungen — ersetze jedes `sorry` durch einen Beweis -/

/-- Übung 2.1 · Die wahre Ursache gibt es auch — aber ihr Zeuge belastet Kael selbst.
    Tipp: ein anonymer Konstruktor `⟨Zeuge, Beweis, Beweis⟩`. -/
theorem hand_erklaert_rueckfrage : ∃ u, erklaert u .rueckfrage = true ∧ belastet u = "Kael" := by
  sorry

/-- Übung 2.2 · Für den vorzeitigen Ausgang um 16:31 gibt es eine Ursache. Welche? -/
theorem ausgang_hat_ursache : ∃ u, erklaert u .ausgang = true := by
  sorry

/-- Übung 2.3 · Reine Logik: Aus „p und q“ folgt „q und p“. Tipp: `constructor`, dann `exact h.2` und `exact h.1`. -/
theorem und_tauschen (p q : Prop) (h : p ∧ q) : q ∧ p := by
  sorry

/-- Übung 2.4 · Auch die ehrliche Auskunft — die Hand und die alte Frau — schließt den Posten nicht.
    Tipp: Ein allgemeiner Satz weiter oben erledigt das in einem Schritt. -/
theorem ehrlich_schliesst_auch_nicht : ¬ schliesst [.linkeHand, .altFrau] := by
  sorry

end K02
