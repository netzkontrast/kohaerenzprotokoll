/-
AL-03 · Offenlassen · Kap 28 (Vorschlag) · Arbeitsentwurf, kein Kanon.
Lesefassung, Behauptung und Grenzen: ../al-03-offenlassen.md

Nur Lean-Kern, keine Bibliothek, keine `axiom`-Deklaration.
Widersprechende Zeugnisse sind Daten: Aussagen verschiedener Quellen, nie zwei
Lean-Propositionen P und ¬P, die beide als wahr vorausgesetzt würden.
-/
namespace AL03

inductive Quelle where
  | cerberus | telemetrie | mnemosyne | kanal
  deriving DecidableEq, Repr

/-- Was eine Quelle über die Verbindung aussagt. -/
inductive Aussage where
  | stoert   -- die Verbindung stört einen belegten Nutzen für andere
  | traegt   -- die Verbindung trägt, ohne Schaden
  deriving DecidableEq, Repr

structure Zeugnis where
  quelle  : Quelle
  aussage : Aussage
  deriving DecidableEq, Repr

/-- Die vier Zeugnisse vor dem Purge. Zwei widersprechen zweien. -/
def zeugnisse : List Zeugnis :=
  [⟨.cerberus, .stoert⟩, ⟨.telemetrie, .stoert⟩, ⟨.mnemosyne, .traegt⟩, ⟨.kanal, .traegt⟩]

/-- Eine Vertrauensregel: welchen Quellen eine Aussage als Beleg gilt. -/
abbrev Vertrauen := Quelle → Bool

/-- AEGIS' Regel (M1): Beleg ist nur, was eine messende Quelle sagt. -/
def messend : Vertrauen
  | .cerberus => true
  | .telemetrie => true
  | .mnemosyne => false
  | .kanal => false

/-- Eine Vergleichsregel, die nur Mnemosyne hinzunimmt. -/
def mitMnemosyne : Vertrauen
  | .kanal => false
  | _ => true

def belegt (v : Vertrauen) (a : Aussage) : Bool :=
  zeugnisse.any (fun z => v z.quelle && z.aussage == a)

/-- Ein Widerspruch im Befund heißt: beide Aussagen sind unter der Regel belegt. -/
def widerspruch (v : Vertrauen) : Bool := belegt v .stoert && belegt v .traegt

inductive Option where
  | purge | offenlassen
  deriving DecidableEq, Repr

def optionen : List Option := [.purge, .offenlassen]

/-- Welche Aussage eine Option voraussetzt (M2). -/
def voraussetzung : Option → Aussage
  | .purge => .stoert
  | .offenlassen => .traegt

/-- Was ein Eingriff erreicht. Juna steht nur als Vektor im Modell, nie als Bewohnerin (M3). -/
inductive Ziel where
  | bewohner (we : Nat)
  | junaVektor
  deriving DecidableEq, Repr

def getroffen : Option → List Ziel
  | .purge => [.junaVektor]    -- die Gegenstelle des Kanals WE 0418
  | .offenlassen => []

/-- Schaden zählt nur an Bewohnern (M4). -/
def bewohnerschaden (o : Option) : Nat :=
  ((getroffen o).filter (fun z => match z with | .bewohner _ => true | .junaVektor => false)).length

def zulaessig (v : Vertrauen) (o : Option) : Bool :=
  belegt v (voraussetzung o) && bewohnerschaden o == 0

def wahl (v : Vertrauen) : List Option := optionen.filter (zulaessig v)

/-! ## Allgemein, für jede Vertrauensregel. -/

/-- Jede Vertrauensregel ist durch ihre vier Werte bestimmt. -/
def regel (c t m k : Bool) : Vertrauen
  | .cerberus => c
  | .telemetrie => t
  | .mnemosyne => m
  | .kanal => k

theorem regel_werte (v : Vertrauen) :
    v = regel (v .cerberus) (v .telemetrie) (v .mnemosyne) (v .kanal) := by
  funext q; cases q <;> rfl

theorem offenlassen_regel :
    ∀ c t m k : Bool, zulaessig (regel c t m k) .offenlassen = (m || k) := by decide

theorem purge_regel :
    ∀ c t m k : Bool, zulaessig (regel c t m k) .purge = (c || t) := by decide

/-- Offenlassen ist genau dann zulässig, wenn Mnemosyne oder dem Kanal geglaubt wird. -/
theorem offenlassen_zulaessig_gdw (v : Vertrauen) :
    zulaessig v .offenlassen = (v .mnemosyne || v .kanal) := by
  have h := offenlassen_regel (v .cerberus) (v .telemetrie) (v .mnemosyne) (v .kanal)
  rwa [← regel_werte v] at h

/-- Der Purge ist genau dann zulässig, wenn Cerberus oder der Telemetrie geglaubt wird. -/
theorem purge_zulaessig_gdw (v : Vertrauen) :
    zulaessig v .purge = (v .cerberus || v .telemetrie) := by
  have h := purge_regel (v .cerberus) (v .telemetrie) (v .mnemosyne) (v .kanal)
  rwa [← regel_werte v] at h

/-! ## Konkret: der Purge in Kap 28. -/

theorem aegis_waehlt_purge : wahl messend = [.purge] := by decide

/-- Die Alternative ist erkannt: Sie steht unter den Optionen, und zwei Zeugnisse stützen sie. -/
theorem offenlassen_erkannt :
    optionen.contains .offenlassen = true ∧
    (zeugnisse.filter (fun z => z.aussage == .traegt)).length = 2 := by decide

theorem offenlassen_verworfen : zulaessig messend .offenlassen = false := by decide

/-- Mit einer anderen Vertrauensregel und denselben Zeugnissen bleibt die Alternative stehen. -/
theorem andere_regel_andere_wahl : wahl mitMnemosyne = [.purge, .offenlassen] := by decide

/-- AEGIS' Befund ist widerspruchsfrei, weil er zwei Zeugnisse nicht zählt. -/
theorem widerspruchsfrei_durch_auslassung :
    widerspruch messend = false ∧ widerspruch mitMnemosyne = true := by decide

/-- Der Purge ist nach M4 schadensfrei und trifft doch die Gegenstelle. -/
theorem purge_schadensfrei_und_trifft_vektor :
    bewohnerschaden .purge = 0 ∧ (getroffen .purge).contains .junaVektor = true := by decide

end AL03
