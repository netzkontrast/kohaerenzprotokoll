# Kritische Durchsicht — Dual-Storyform, Treatment und die Entwürfe zu Kap 1 und 2, 2026-10-06

**Eingaben:** Commit `a05a0658` und dazu der ungespeicherte Arbeitsstand im selben Checkout (`git diff --stat`: Treatment
mit dem 2b-Absatz zu Kap 40, `development.json`, die „Stand 2026-10-06“-Abschnitte mehrerer Weichen). `storyform.py
--check` meldet zur Zeit `overview.md` und das NCP als **STALE**: Gelesen habe ich die Fassung, die im Checkout liegt.
Gelesen: `.agents/skills/storyform/SKILL.md`, `.agents/skills/writing-skills/SKILL.md`, `Manuscript/kanon.md`,
`Plan/storyform/{overview.md,a.json,b.json,weave.json (über die Übersicht),anteile.json (über die Übersicht),clock-b.json}`,
`Plan/decisions/025-dramatica-is-the-recipe.md` (Schritte 0–48), `Manuscript/plot/treatment.md`,
`Manuscript/kap-01/entwurf-j-rueckfrage.md`, `Manuscript/kap-02/entwurf-a-die-rolle-haelt.md`, die vier früheren
Prüfungen, dazu `Plan/runs/storyform-2026-10-02/{engine-rules.md,validation.md}` und die Theorie-Referenzen des
Skills `dramatica-theory` (`00-storyform-validation.md`, `02-characters.md`, `07-storyencoding.md`).

**Vorbehalt:** Ich stamme aus derselben Modellfamilie wie die Sitzungen, die den Plan gebaut haben. Unabhängig ist nur
der Kontext, nicht das Urteil. Alle Befunde sind **Vorschläge**. Nichts hier ist Kanon und nichts ändert einen
beschlossenen Wert. Frühere Prüfungen habe ich nicht wiederholt. Wo ein Befund schon benannt war und am Stand
`a05a0658` noch gilt, steht das dabei, mit einem neuen Aspekt oder gar nicht.

Zeilen sind als `datei:Lnn` aus `nl -ba` oder `rg -n` zitiert. Abkürzungen: `T` = `Manuscript/plot/treatment.md`,
`J` = `Manuscript/kap-01/entwurf-j-rueckfrage.md`, `K2` = `Manuscript/kap-02/entwurf-a-die-rolle-haelt.md`,
`E025` = `Plan/decisions/025-dramatica-is-the-recipe.md`, `OV` = `Plan/storyform/overview.md`, `kanon` =
`Manuscript/kanon.md`.

---

## 1. Was trägt

1. **Die Hard-SF-Rechnung von Kap 1 stimmt, und sie trägt den Plot.** 2,2 × 10²⁹ Bit mal *kT* ln 2 bei 293 K
   ergeben 6,17 × 10⁸ J, im Text 6,18 × 10⁸ J (`J:L74–L75`). Die Messreihe hat 5,9 × 10⁻¹⁰ J (`J:L61`), die
   „sieben Milliarden“ Bänke (`J:L125`) stimmen, und 6,7 × 10⁸ J bringen zwei Tonnen Wasser von 20 °C zum Kochen (`J:L83`).
   Landauer ist hier der Preis einer Handlung und keine Dekoration.
2. **B hat ein sauberes Scharnier.** Bei Steadfast ist das Crucial Element die Lösung Logic. AEGIS trägt sie als
   Reason, Kael trägt den Partner Feeling als Emotion (`OV:L72`). H6–H8 gelten in B ohne Hilfsannahme.
3. **Kap 35 kann die Wende beider Storyforms in einer Geste tragen.** „Kael bestätigt die Löschung nicht mehr …
   Oblivion lässt die widersprüchlichen Erinnerungen stehen“ (`T:L439–L440`). Für A ist das Inertia → Change, für B
   (Kael als IC) Disbelief → Faith: Widersprüchliches stehen lassen, ohne es zu prüfen. Das ist genau „der Host, der
   lernt … zu glauben“ (`Plan/storyform/b.json:L6`). Diese Doppellesung ist der stärkste Beleg für die eine Prämisse.
4. **Die Uhr von A ist räumlich und konkret.** Jede Wende nimmt einen Ort (`Plan/storyform/a.json:L341`), und die vier
   Weltbänder geben ihr eine Geographie (`OV:L82`).
5. **Die RÜCKFRAGE reimt sich über das Buch:** Kap 1, 13 und 35 (E025:L280–L281). Damit hat A's Treiber Decision
   einen Gegenstand.
6. **Juna hat eine eigene Linie, nicht nur Auftritte:** der Ort, gewollt, hergegeben, genommen, geteilt (`T:L537–L538`).
   Das erfüllt die Forderung der Validierung nach einer eigenen IC-Linie
   (`Plan/runs/storyform-2026-10-02/validation.md:L27`).

---

## 2. Strukturelle Befunde zur Dual-Storyform

### S1 — Juna soll im OS „Change“ tragen, ist dort aber 31 Kapitel abwesend · **hoch**

- **Beleg:** `a.json:L114` gibt Juna die OS-Elemente `["Change"]` mit der Begründung „H8“. Die Validierung hakt ab: „✓
  Juna trägt Change“ (`validation.md:L16`). Nach dem Buch sitzt der Player der IC im Overall Story auf dem Paarpartner
  des Crucial Element (`02-characters.md:L1030–L1032`, `07-storyencoding.md:L200`). Schritt 30 verwirft Juna als Sidekick
  mit dem Satz: „she is memory and traces until Kap 32, and an overall-story role needs presence“ (`E025:L163–L165`).
- **Der Widerspruch:** Dieselbe Begründung trifft auch ihr einziges OS-Element. Bis Kap 32 hat Change im OS von A keinen
  Träger, der im Raum handelt. A's OS ist Psychology und spielt sich zwischen den Anteilen und den vier Menschen ab.
- **Folge:** Der OS-Konflikt von A, die Rollenfassade, verhandelt Inertia, aber niemand in der Szene verkörpert Change.
  Das ist die alte Diagnose „niemand im selben Raum will etwas von ihm“, nur eine Ebene tiefer.
- **Offene Frage:** Wer oder was trägt Change im OS, bevor Juna da ist? Zwei Möglichkeiten: ihre Spuren als Gegenstände
  in der Stadt, also eine Handlung über Gegenstände, oder eine Figur, die ihre Funktion stellvertretend trägt (Weiche
  W-F).

### S2 — B ist Steadfast/Failure/Bad, aber das Ende liest sich wie die Erlösung von AEGIS · **hoch**

- **Beleg:** B: steadfast, failure, bad (`OV:L12–L14`). Die Lösung Faith wird „never taken“ (E025:L32–L33, Schritt 7; nach
  der Neuableitung in Schritt 16 steht Faith für Trust). Die generierten Storypoints-Zeilen setzen aber **„B-MC Solution
  Faith“** in Kap 35 und Kap 39 (`T:L446`, `T:L488`). Kap 39: „ein AEGIS im Plural antwortet, im Wir“ (`T:L483`). Kap 40:
  „Das Wir, mit AEGIS im Plural, bezeugt …“, „nicht mehr als Trauma“ (`T:L493–L495`). Der Titel von B heißt „Phönix-Kollaps“.
- **Der Widerspruch:** Ein Phönix, der als Wir wiederkehrt und geheilt bezeugt, ist für den Leser Change und Good. Damit
  wäre das Tragödienargument von B, die Hälfte der Prämisse, zurückgenommen.
- **Offene Frage:** Ist AEGIS-plural **dasselbe Ich**, das gelernt hat (dann widerspricht es Steadfast und Bad), oder ein
  **Nachfolger** ohne die Erinnerung des Monolithen (dann gilt Bad, und das Wir erbt nur)? Siehe Weiche W-E. Unabhängig
  davon sollte „B-MC Solution Faith“ als *nicht ergriffen* erzählt werden. Die Zeile selbst ist generiert. Ändern lässt
  sie sich nur in `development.json`.

### S3 — Auf der Element-Ebene ist Gefühl in B das Problem, die Prämisse nennt Liebe die Ordnung · **mittel**

- **Beleg:** Prämisse „… und Liebe ist die Ordnung, die Vielheit trägt“ (`b.json:L5`). B: OS-Problem Feeling,
  OS-Lösung Logic, RS-Problem Feeling → Logic (`OV:L63–L64`). Kael ist der Antagonist und hält Feeling (`OV:L72`).
  Schritt 0 sagt, B argumentiere „from the other side“ (E025:L67–L69).
- **Spannung:** „Von der anderen Seite“ heißt auf Concern-Ebene: Wer Geschlossenheit sucht, scheitert. Auf der
  Element-Ebene sagt B dagegen wörtlich: Gefühl verursacht die Störung, Logik behebt sie. Mit Failure/Bad liest man das
  leicht als „die Logik reichte nicht“, nicht als „die Liebe trägt“.
- **Offene Frage:** Soll das Treatment B's Feeling als *unkontrolliertes* Gefühl lesen (Nyx, die Ausbrüche) und
  Liebe davon trennen? Dann wäre Liebe in B nicht das Problem, sondern das, was Logic im Wir von Kap 39 *aufnimmt*.
  Oder nimmst du hin, dass B gegen die zweite Hälfte der Prämisse argumentiert? Das muss nicht schlecht sein, es muss
  nur gewollt sein.

### S4 — Die Uhr von B verhält sich wie ein Optionlock · **mittel**

- **Beleg:** „jeder Sweep verbraucht sie“ (`b.json:L309`). `clock-b.json` hat Werte nur in AEGIS-Kapiteln. Der Purge
  verbraucht am meisten (`T:L364`).
- **Problem:** Ein Budget, das *pro Handlung* sinkt, ist eine begrenzte Zahl von Zügen, also ein Optionlock. Würde
  AEGIS nicht sweepen, fiele die Zahl nicht. Ein Timelock braucht Zeit, die auch ohne Handlung abläuft. Die Anlage dafür
  ist schon da: Die Forewarnings sagen, die Wartungsfenster werden dichter (E025:L52), und „Alle paar Wochen ist ein
  Sektor dran“ (`J:L49`).
- **Offene Frage:** Fällt die Reserve auch nach Kalender, mit jedem geplanten Fenster? Das ändert keinen
  Storyform-Wert, nur die Mechanik (Weiche W-D).

### S5 — Wo die Wende von A liegt, verwischen die Storypoints-Zeilen · **mittel**

- **Beleg:** Schritt 27 und 48 legen Inertia → Change in Kap 35 und Kap 34 ausdrücklich auf das alte Muster (E025:L149–L151,
  `OV:L134`). Die Zeilen setzen aber „A-MC Solution Change“ schon in Kap 13, 26 und 34 (`T:L194`, `T:L339`, `T:L432`).
- **Dazu:** Kap 13 endet mit „Die Rückfrage bleibt offen“ (`T:L190`). Das ist derselbe Zustand wie am Ende von Kap 1:
  „RÜCKFRAGE WE 0418 · OFFEN“ (`J:L235`). Kap 35 wiederholt dieselbe Geste nach innen gewendet. Der Reim ist gewollt.
  Weil aber die Zeilen in 13 schon „Solution“ sagen, merkt der Leser den Unterschied zwischen 1, 13 und 35 nicht.
  `development.json` fragt das zu Kap 13 selbst: „Wie ist Kap 1 nur Verschiebung geblieben?“ (`OV:L231`).
- **Offene Frage:** Stammen die Solution-Bezüge in 13, 26 und 34 aus deinen Schritten 45/46 oder aus dem Akt-Rhythmus
  (also aus einem Vorschlag)? Kommen sie aus dem Rhythmus, kann eine Sitzung sie ohne neue Entscheidung zurücknehmen
  (Abschnitt 7).

### S6 — Wer entscheidet an den Aktwenden: Kael oder ein Lager? · **mittel**

- **Beleg:** Schritt 17 legt die Anteile als OS-Figuren in *einen* Player Kael (E025:L86–L90). Die Validierung zählt H9
  dann „je Alter, nicht für den Player Kael“ (`validation.md:L37`). Im Treatment fallen die A-Entscheidungen an den
  Treiberstellen aber als Siege von Lagern: „Die Suche gewinnt“ (`T:L332`), „Die Abwehr gewinnt“ (`T:L425`). Kael selbst
  steht im Lager der Vermeidung (`kanon:L29`). Trotzdem heißt es: „Diesmal ist es ganz seine Wahl“ (`T:L335`).
- **Spannung:** A ist decision-driven und Kael ist MC. Wenn an 26 und 34 ein Lager gewinnt, entscheidet das System und
  nicht die Hauptfigur. Die Prüfung vom 2026-10-06 hat das für Kap 26 und 35 angemerkt
  (`Plan/runs/writing/akt-2-vortex/scene-architecture_2026-10-06.md:L142–L149`). Schritt 48 hat Kap 35 gelöst, für Kap 26
  und 34 ist die Regel offen.
- **Offene Frage:** Ist eine Aktwende-Entscheidung Kaels Tat *gegen* oder *mit* einem Lager, oder ist der Sieg eines
  Lagers selbst die Entscheidung (Weiche W-C)?

### S7 — Die beiden Ensembles fallen aus, und die Elemente bieten eine Übergabe an · **mittel** (schon benannt, neuer Aspekt)

- **Beleg:** Mara erscheint in 2b nur in Kap 7, Dorn nur in Kap 8, die alte Frau in Kap 1 und 10, die Kollegin in Kap 2
  und 5 (`rg -n` über `T`). Ab Kap 14 bleiben alle vier in KW1 zurück (`T:L212`). Sophia, LogOS und Kairos stehen in
  keinem Absatz des Treatments und in keinem Vorschlag von `development.json`: `rg` liefert null Treffer. Benannt in
  `scene-architecture_2026-10-06.md:L57–L65`, offen in W10/W17.
- **Neu:** Die Elemente beider Ensembles sind **paarweise identisch**: Mara und Sophia (Help, Conscience), Dorn und
  Mnemosyne (Hinder, Temptation), die alte Frau und LogOS (Support, Faith), die Kollegin und Kairos (Oppose, Disbelief)
  (`OV:L45`, `OV:L72`). Das Schema enthält damit schon eine Übergabe: Ab KW2 können die Guardians die Funktionen
  übernehmen, die die Menschen in KW1 tragen. Dorns Want hängt an Sektor 04 (`a.json:L176`), und den löscht die Welle in
  Kap 14 (`T:L206`). Sein Faden endet also ohne Szene.
- **Offene Frage:** siehe Weiche W-B.

### S8 — Im Problem-Element sind MC und IC von B gleich · **niedrig**

- **Beleg:** Für AEGIS und Kael gilt in B jeweils Disbelief → Faith (`OV:L61–L62`). Dass die IC über dem MC-Problem
  sitzt, nimmt die Ableitung an (`engine-rules.md:L45`). Kaels IC-Problem hast du aus dem Quad gewählt, als Annahme
  (E025:L99–L105). Kaels Unique Ability ist zugleich seine Lösung Faith (`b.json`, IC).
- **Folge:** MC und IC unterscheiden sich in B auf dieser Ebene nicht. Ihre Gegensätzlichkeit muss allein aus Concern
  und Issue kommen (Future/Openness gegen Subconscious/Dream). Das ist kein Regelverstoß, aber eine dünne Stelle, falls
  du B später gegen eine offizielle Engine prüfst.

---

## 3. Plot- und Treatment-Befunde

### P1 — Kap 11 erinnert, was Kael nicht erinnern kann · **hoch**

- **Beleg:** C7: „Akt I erinnerte Szenen vor dem Anruf (Kap 4, 11)“ (`kanon:L24`). Junas Karte ordnet die Zeit so: „der
  Anruf → zehn Jahre, die Kael vergessen hat → … heute droht eine Trennung“
  (`Plan/runs/writing/book/character-card-builder_juna_2026-10-05.md:L92`). „Er kennt nur das Davor und den Anruf“
  (ebd. `:L57`). Das Treatment zu Kap 11 dagegen: „bis an den Rand der Trennung“, „Sie reißt am Anruf ab“ (`T:L170–L173`).
- **Widerspruch:** Die Trennung droht *nach* den zehn Jahren, und die zehn Jahre sind gelöscht. Kap 11 setzt den Anruf
  und die Trennung gleich. Es zeigt damit einen Rand, der in Akt I nach C7 nicht erinnerbar ist, und nimmt Kap 18 („die
  Nacht von innen“) vorweg.
- **Offene Frage:** Weiche W-G.

### P2 — Wo Juna ist, und was AEGIS ihr antun kann, ist ungeregelt · **hoch**

- **Beleg:** Der Purge „gefährdet Juna“ (`T:L363`, `T:L367`), sie „ist jetzt sichtbar“ (`T:L385`), Begegnung im
  Möglichkeits-Garten (`T:L402`), ihr Ort (`T:L416`). In Kap 17 heißt es „Kael kommt darin nicht vor“ (`T:L245`), die
  Karte sagt dagegen: „die beiden sind inzwischen ein Paar“ (`…juna_2026-10-05.md:L92`). J68 (Ursprungs-Ich oder
  Gegenüber) ist offen (`Plan/weichen/w9-juna.md:L66`), die Regel des Kanals ebenfalls (`Plan/weichen/w15-moonshine-link.md:L81–L93`).
- **Folge:** Ohne Regel bleibt die Gefahr in Kap 28–34 eine Behauptung. Kap 34, „aus dem Schussfeld bringen“, hat dann
  keinen Mechanismus. Wenn die beiden ein Paar sind, ist außerdem offen, wieso er in ihrem weiterlaufenden Leben nicht
  vorkommt (Kap 17).
- **Offene Frage:** Weiche W-A. Sie gibt die Mindestregel und lässt J68 offen.

### P3 — Die Hitzerechnung läuft in Kap 31–35 rückwärts · **hoch**

- **Beleg:** Kap 31: „Oblivion löscht schneller, als Silas empfängt. Die Landauer-Hitze steigt“, „AEGIS'
  Abwärmebudget sinkt“ (`T:L392`, `T:L395`). Kaels inneres Löschen kostet also AEGIS' Reserve. In Kap 35 hört Oblivion
  auf, und **„im selben Moment“** steht das Budget auf 0 % (`T:L442`). Ein Weil steht nirgends.
- **Problem:** Gilt die gemeinsame Währung von Kap 31, dann müsste das Ende von Oblivions Löschen AEGIS *entlasten*.
  Gleichzeitig ist kein Grund. Außerdem gibt es drei Hitzegrößen ohne Umrechnung: ein Abwärmebudget pro Sektor und
  Fenster in Joule (`J:L98`), die Reserve von AEGIS in Prozent (`OV:L177–L179`) und die Landauer-Hitze in Kael (Kap 31).
  Kap 33 ist hard-a und meldet trotzdem „AEGIS' Reserve fällt sichtbar“ (`T:L418`). Für wen ist sie dort sichtbar?
- **Anlage im Text:** Was nicht bestätigt wird, kommt zurück. 251 kehrt wieder (`K2:L83–L88`): „Ein Ausgleich, der
  zurückkommt, ist kein Ausgleich. Er ist ein Fehler, der wartet“ (`K2:L98`). Jedes erneute Löschen kostet erneut. Das
  wäre der kausale Hebel für Kap 35 (Weiche W-D).

### P4 — Das Wartungsfenster und die erste Welle sind ein Ereignis, das zwei Ursachen hat · **mittel**

- **Beleg:** Die Frist ist das nächste Fenster von Sektor 04 (`T:L93–L94`), in `K2:L22` „in 11 Tagen“. Kap 5 zieht es
  vor (`T:L123`). Kap 13: „für die Wartung von Sektor 04 zahlen andere“ (`T:L191`). Kap 14: AEGIS „antwortet“ mit der
  Welle, die Sektor 04 löscht (`T:L206`).
- **Problem:** Ist die Welle das geplante Fenster, dann treibt ein Kalender die Wende von B und keine Handlung von AEGIS
  (H11, B's Hälfte, `OV:L132`). Ist sie AEGIS' Antwort, was wird dann aus dem Fenster? Wie viele Tage Akt I dauert, legt
  bisher nur der Entwurf von Kap 2 fest (M2). Dorns Schwester (S7) und Kaels eigene Wohneinheit WE 0418 in Sektor 04
  (`J:L72`) gehen in Kap 14 ohne eigene Szene unter.

### P5 — Die 734-Spur kommt auf Kaels Seite nirgends an · **mittel**

- **Beleg:** 734 steht nur in AEGIS-Kapiteln: Kap 6 („AEGIS weiß das nicht“, `T:L131–L132`) und Kap 22 („Einen Satz lang
  erkennt AEGIS, was 734 ist“, `T:L294`). Kap 0 erzählt drei Schritte der Genesis (`T:L77`). Q7 lässt offen, was die
  Zahl in Kaels Alltag bezeichnet (`kanon:L33`). Die Entwürfe benutzen WE 0418/0419 und Konsole 4/9, nie 734.
- **Probleme:** (a) Kein Kapitel zeigt, wann Kael oder der Leser erfährt, dass Kael das herausgetrennte Cluster ist.
  (b) AEGIS weiß in Kap 0 von Cluster und Trennungsprotokoll und erkennt in Kap 6 trotzdem nichts. Das trägt nur, wenn
  der Gedächtnisverlust von Kap 0 genau diesen Bezug löscht.
- **Vorschlag:** Der „eigene Logbezug“, den Kap 0 verliert (`T:L71–L72`), ist der Eintrag Genesis → 734. Das kostet
  keine neue Regel, und die Unwissenheit in Kap 6 hat dann eine Ursache.

### P6 — Oblivion „hört auf“ und „wählt zum ersten Mal“ in drei Kapiteln · **mittel**

- **Beleg:** Kap 18 zögert er einmal (`T:L256`). In Kap 31 steht der Einfall „Das Löschen selbst lässt sich wählen“
  (`T:L393`), was schon früher als vorgezogene Lösung benannt wurde. In Kap 35 lässt er stehen (`T:L440`), in Kap 37
  „wählt [er] zum ersten Mal“ (`T:L464`), in Kap 39 „wählt [er] nun“ (`T:L59`).
- **Problem:** Zwischen „aufhören“ (35) und „wählen“ (37) fehlt ein Ereignis, das den Unterschied zeigt. Und Q8 lässt
  AEGIS' Funktion in Kael weiterleben (`kanon:L34`). Dann ist A's Antagonist am Ende der Verwalter des Vergessens.
  Das ist stark, wenn es als Preis erzählt wird. Als Happy End wird es schief.
- **Offene Frage:** Was wählt Oblivion in Kap 37 *gegen* einen Wunsch Kaels? Erst dann ist die Wahl sichtbar.

### P7 — Wiederholungen und Kapitel ohne neuen Zug · **mittel**

- **Der fehlende Schritt:** Er fehlt in J (`J:L109`, `J:L201–L205`), wird in Kap 3 neu gefunden (`T:L104`), und in
  Kap 15 vergisst Kael die Schrittzahl (`T:L222`). Dreimal derselbe Preis (siehe M1).
- **Die Kanal-Kapitel:** 19 (Werkzeug), 21 („Eine Verbindung hält“, `T:L285`), 24 (Filter), 30 („Der Kanal hält“) und
  33 (Schweigen). Solange W15 offen ist, unterscheiden sie sich vor allem durch das Etikett. Erst eine Regel, was
  durchgeht und was es kostet, gibt jedem eine eigene Wendung.
- **Kap 15 und 23** haben defensive Ziele („zurück“, „handlungsfähig bleiben“, `T:L218`, `T:L303`). Für Kap 23 ist das
  benannt, Kap 15 kommt neu dazu. Sein Preis, die Schrittzahl, ist schon verbraucht.

### P8 — Kleine Abfragen · **niedrig**

- Kiko gehört zum Lager der Suche (`kanon:L29`). Kap 29 sagt dagegen „das letzte Aufflammen der Vermeidung“, mit
  wechselndem Pronomen: „Er wird klein“, „statt sie zu übergehen“ (`T:L374–L375`). Das wurde schon benannt und steht am
  Stand `a05a0658` noch so da.
- Die Uhr von A nennt vier verlorene Orte (`a.json:L341`), das Treatment fünf: Kap 27 verliert auch KW3 (`T:L355`). Nach
  dem Weaving liegen Kap 27–28 aber in KW3 (`OV:L113–L114`).

---

## 4. Manuskript-Befunde

### M1 — In den Entwürfen ist der fehlende Schritt eine Löschung der Welt, in Kap 3 eine Lücke Kaels · **hoch**

- **Beleg:** J setzt den Korridor ausdrücklich auf die Löschliste: „KORRIDOR DELTA-7 · ABSCHNITT 2 · 0,73 M“ (`J:L109`).
  K2 bestätigt das: „weil ein Stück von ihm ausgeglichen worden ist, ordnungsgemäß, im Fenster“ (`K2:L100`). Das
  Treatment zu Kap 3 macht dieselben 0,73 m zu Kikos Zeitsprung und zu Kaels Wahl: „Er meldet den fehlenden Schritt
  nicht“ (`T:L104–L105`).
- **Folge:** Steht ein Schritt auf Kaels eigener Konsole verbucht, gibt es nichts zu melden. Die Wahl von Kap 3 und
  Kikos Spur sind damit leer. Die Entwicklung hat aber schon einen besseren Gegenstand: ein von Kael angelegtes
  Messzeichen, an das er sich nicht erinnert (`Plan/storyform/development.json:L134`).

### M2 — Der Entwurf von Kap 2 legt die Frist auf 11 Tage fest · **mittel**

- **Beleg:** „FRIST: NÄCHSTES REGULÄRES FENSTER SEKTOR 04 · IN 11 TAGEN“ (`K2:L22`), „10 TAGE 12 STUNDEN“ (`K2:L176`).
  Offen ist dagegen: „Trägt diese Frist bis Kap 13?“ (`OV:L220`).
- **Folge:** Damit sind die Dauer von Akt I und der Spielraum festgelegt, um den Kap 5 die Frist verkürzt (P4). Das
  kann gut sein, ist aber eine Entscheidung, keine Ausführung.

### M3 — Die Knöchel kommen elf Kapitel vor ihrem Platz · **mittel**

- **Beleg:** J: „Die rechte tut weh, in allen vier Knöcheln“ (`J:L19`, auch `J:L219`). K2: `K2:L28`, `K2:L81`. In
  `anteile.json` steht Nyx' Spur in Kap 12 („Knöchel, die bluten“, `OV:L152`, `T:L182`). Für Kap 1 nennt die Tabelle nur
  Silas und Oblivion (`OV:L146–L147`).
- **Folge:** Entweder wird Kap 12 eine Steigerung (Schmerz ohne Wunde, dann Blut), dann fehlt Nyx in Kap 1 in
  `anteile.json`. Oder die Entwürfe binden eine Spur, die die Arbeitsgrundlage nicht vorsieht.

### M4 — „Abwärmebudget“ heißt in J eine andere Größe als die Uhr von B · **mittel**

- **Beleg:** „ABWÄRMEBUDGET 6,18 × 10⁸ J WIRD UMVERTEILT“ (`J:L98`): eine Größe des Sektors, in Joule, die sich
  umverteilen lässt. Die Uhr von B ist „AEGIS' thermodynamische Reserve“ in Prozent (`b.json:L309`, `OV:L177–L179`).
- **Folge:** Ein Hard-SF-Leser hält beides für dasselbe und rechnet. Siehe P3. Das Wort sollte eine Größe bezeichnen,
  oder die Umrechnung muss im Text stehen.

### M5 — Zwei Archetypen, eine Frage · **niedrig**

- **Beleg:** Die alte Frau fragt „Wie heißen Sie?“ (`J:L189`). Das ist Maras Gewissensfrage „Wie heißt du?“
  (`a.json:L165`, `T:L139`). Ihr Satz „Sie werden sich an mich erinnern“ (`J:L195`) spricht ihren Want aus
  (`a.json:L187`), und das Leserpanel nennt ihn orakelhaft.
- **Folge:** Mara verliert in Kap 7 ihr Erkennungszeichen, und Sidekick und Guardian-Archetyp verschwimmen.

### M6 — Kap 2 setzt eine neue Person und einen zweiten Posten ohne Datentyp · **niedrig**

- **Beleg:** „FREIGABE WARTUNGSPLAN: H. TAMM“ (`K2:L132`): eine benannte Person, die nicht in `a.json` steht. Außerdem
  „ANHAFTENDES OHNE EINTRAG · 1 POSTEN · 2,8 × 10¹⁹ BIT / DATENTYP —“ auf der Bank (`K2:L48–L49`, `K2:L55`), dieselbe
  Signatur wie Kaels Anschluss (`J:L73`) und Kap 0 (`T:L73`).
- **Folge:** Damit ist festgelegt, dass auf der Bank etwas Typloses lag. Für einen solchen Faden gibt es keinen Platz im
  Plan, und er zieht die alte Frau in die Nähe von Junas Spur. Entweder beschließt du das, oder der Faden braucht eine
  Auflösung in Kap 10.

---

## 5. Vorgeschlagene Weichen

Geordnet danach, wie viele Kapitel sie freigeben. Keine davon ist in E025 schon beantwortet.

### W-A — Was AEGIS Juna antun kann (Kap 17, 25, 28, 30, 32–38)

- **Frage:** Über welchen Weg kann AEGIS Juna erreichen, und wo findet die Begegnung in Kap 32 statt?
- **Optionen:**
  1. **Nur über den Kanal.** Juna lebt außerhalb der Stadt. Der Purge trifft die Verbindung und damit sie, über das, was
     der Kanal überträgt. Kap 32 findet an einer Grenze statt, die KW4 öffnet.
     *Folge:* J68 bleibt offen, Kap 34 („sie aus dem Schussfeld bringen“) heißt den Kanal schneiden, und W15 wird
     tragend.
  2. **Sie ist in der Welt.** Der Purge kann sie löschen wie eine Bank. *Folge:* Die Gefahr ist klar, aber J68 wird
     vorentschieden, und Block 4 ist näher.
  3. **Offen lassen.** *Folge:* Kap 28–34 bleiben Behauptungen (P2).
- **Empfehlung:** 1. Das ist die kleinste Regel, die alle betroffenen Kapitel kausal macht. Sie passt zu W15 und ändert
  keinen Storyform-Wert. Sie erklärt auch Kap 17: Ihr Leben läuft ohne ihn weiter, *weil* er aus ihm in die Stadt
  gefallen ist.

### W-B — Wer die Funktionen der Archetypen nach KW1 trägt (Kap 14–34; W17)

- **Frage:** Gehen die Funktionen der vier Menschen in KW2–KW4 an die Guardians mit denselben Elementen über?
- **Optionen:**
  1. **Übergabe nach Element:** Mara an Sophia, Dorn an Mnemosyne, die alte Frau an LogOS, die Kollegin an Kairos.
     *Folge:* Sophia, LogOS und Kairos bekommen endlich Szenen, und A und B spiegeln sich im Personal. Die Guardians
     treten in hard-a-Kapiteln auf, also in Kaels Welt.
  2. **Die Menschen kehren zurück** (in KW4 oder im Vortex). *Folge:* Das bricht die Vorliebe aus Schritt 39 und die
     Kosten der getrennten Welten.
  3. **Stumm lassen.** *Folge:* Für 26 Kapitel fehlen acht Funktionen (S7).
- **Empfehlung:** 1. Die Elementgleichheit (`OV:L45`, `OV:L72`) zeigt, dass der Plan diese Übergabe schon enthält.

### W-C — Wer an den Aktwenden entscheidet (Kap 13, 26, 34)

- **Frage:** Trifft Kael die Wendeentscheidung gegen oder mit einem Lager, oder ist der Sieg eines Lagers selbst die
  Entscheidung?
- **Optionen:**
  1. **Kael entscheidet. Die Lager drücken nur.** In Kap 26 verlässt er die Vermeidung, sein eigenes Lager. In Kap 34
     macht er Lias „Geh“ zu seinem Satz. *Folge:* Der Treiber Decision liegt eindeutig bei der Hauptfigur.
  2. **Das System entscheidet.** Kap 35 ist dann die erste Entscheidung des Hosts. *Folge:* Das ist thematisch stark,
     aber A's Treiber steht dann auf einem Kollektiv.
  3. **Gemischt.** Kap 26 Kael, Kap 34 das Lager. *Folge:* Das ist ehrlich zur Störung, man muss es aber eigens
     markieren.
- **Empfehlung:** 1. Sie macht „ganz seine Wahl“ (`T:L335`) wahr und lässt Kap 34 als *gewählte* Wiederholung lesbar.

### W-D — Die Hitzebuchführung (Kap 1, 2, 28, 31, 33, 35, 38)

- **Frage:** Gibt es eine Hitzewährung oder zwei, und warum steht das Budget gerade in Kap 35 auf null?
- **Optionen:**
  1. **Eine Währung**, mit Kalender und Rückkehr. Die Reserve fällt mit jedem geplanten Fenster (das macht sie zur
     Zeit, S4), und mit jedem Sweep zusätzlich. Was nicht bestätigt ist, kommt zurück wie 251, und erneutes Löschen
     kostet erneut. In Kap 35 lässt Kael Oblivions Löschung unbestätigt. AEGIS' letzter Sweep löscht also gegen etwas,
     das immer wiederkommt, und verbrennt den Rest. *Folge:* Die beiden Wenden von Kap 35 hängen durch ein Weil zusammen.
  2. **Zwei Größen.** Kaels Landauer-Hitze ist seine eigene, AEGIS' Reserve fällt nur durch Sweeps. *Folge:* Kap 31
     kostet AEGIS nichts, und das gleichzeitige Ende in Kap 35 bleibt Zufall.
  3. **Wie jetzt.** *Folge:* P3 bleibt.
- **Empfehlung:** 1. Die Mechanik steht schon in K2:L98. Sie wird zur Regel, und kein Storyform-Wert ändert sich.

### W-E — AEGIS-plural: dasselbe Ich oder ein Nachfolger? (Kap 35, 39, 40)

- **Frage:** Erinnert sich das plurale AEGIS daran, der Monolith gewesen zu sein?
- **Optionen:**
  1. **Nachfolger.** Der Monolith erlischt unversöhnt, und Steadfast/Bad gilt. Das Wir erbt nur die Funktion und nicht
     die Erinnerung. Das ist auch der letzte Preis von „Costs Memory“. *Folge:* Kap 40 bezeugt das Wir und nicht das
     Ich von C14.
  2. **Dasselbe Ich, verwandelt.** *Folge:* B liest sich als Change/Good, und dein Wert für B müsste sich ändern.
  3. **Bewusst unentscheidbar.** *Folge:* Das ist literarisch möglich, aber die Tragödie von B wird schwach.
- **Empfehlung:** 1. Das hält deine beschlossenen Werte und gibt dem Phönix einen echten Tod.

### W-F — Wer Change im OS trägt, bevor Juna da ist (Akt I–II)

- **Frage:** Welche Figur oder welcher Gegenstand trägt Junas OS-Element Change vor Kap 32 (S1)?
- **Optionen:**
  1. **Ihre Spuren als handelnde Dinge:** der Anschluss, der Kanal, ihr Ort. *Folge:* Das ist billig, aber Dinge
     wollen nichts.
  2. **Eine Stellvertreterin:** Die alte Frau trägt zusätzlich Change („kommt wieder, als hätte sie nie gezweifelt“).
     *Folge:* Ein Player trägt dann Change und Faith. Das ist erlaubt und zieht sie näher an Juna (vgl. M6).
  3. **Hinnehmen**, dass das OS von A ohne IC-Gegenpol läuft.
- **Empfehlung:** 2, falls du M6 behalten willst. Sonst 1, mit ausdrücklicher Begründung.

### W-G — Die Zeit der erinnerten Szenen (Kap 4, 11, 18)

- **Frage:** Bleibt Kap 11 vor dem Anruf, wie C7 es sagt, oder zeigt es den Rand der Trennung?
- **Optionen:**
  1. **Kap 11 ist der Anruf selbst** und bricht im Schweigen ab. Der Rand der Trennung gehört Kap 18. *Folge:* C7 und
     Junas Karte halten, und Kap 18 bekommt seinen Inhalt.
  2. **Kap 11 als Riss in die gelöschten Jahre.** *Folge:* Das ist eine Ausnahme von C7, die du festhalten müsstest.
- **Empfehlung:** 1.

### W-H — Der fehlende Schritt (Kap 1, 2, 3, 15)

- **Frage:** Ist der Schritt eine verbuchte Löschung der Welt, wie in J und K2, oder Kaels private Lücke, wie im
  Treatment?
- **Optionen:**
  1. **Eine Löschung der Welt**, wie die Entwürfe sie zeigen. Kap 3 nimmt dann das Messzeichen ohne Erinnerung
     (`development.json:L134`) als private Lücke und Kikos Spur. Kap 15 braucht einen anderen Preis.
  2. **Eine private Lücke.** *Folge:* J und K2 müssen umgeschrieben werden.
- **Empfehlung:** 1. Die Entwürfe tragen die Löschung gut, und das Messzeichen steht schon im Plan.

---

## 6. Was ohne den Autor ableitbar wäre

1. **Herkunft der Solution-Bezüge (S5):** prüfen, ob „A-MC Solution Change“ in Kap 13/26/34 und „B-MC Solution Faith“
   in Kap 35/39 aus Schritt 45/46 stammen oder aus dem Akt-Rhythmus. Bezüge aus dem Rhythmus kann eine Sitzung in
   `development.json` an Schritt 27/48 und Schritt 7 angleichen und dann `storyform.py` laufen lassen.
2. **Kiko in Kap 29 (P8):** Der Kanon geht vor (`kanon:L29`). Den Absatz an das Lager der Suche angleichen, das
   Pronomen vereinheitlichen.
3. **Die Uhr von A gegen das Treatment (P8):** die vier Orte aus `a.json:L341` mit den fünf Verlusten im Treatment
   abgleichen und die Stellen auflisten. Kap 27 gegen das Weltband KW3 prüfen.
4. **Eine Tabelle der Hitzegrößen:** jede Erwähnung von Joule, Prozent, Vorkühlung und Landauer in J, K2, Treatment und
   `clock-b.json`, mit Einheit, Ort und Kapitel. Das ist die Grundlage für W-D und braucht keine Entscheidung.
5. **Eine Wissenstabelle pro Kapitel:** Was wissen Kael, AEGIS und der Leser über 734, die Genesis, Junas Ort und den
   Kanal, vor und nach jedem Kapitel. Das deckt P5 auf und zeigt, wo eine Antwort aus W-A fehlt.
6. **Eine Konkordanz der Spuren in den Entwürfen:** Knöchel, Hände, Minuten, Schritt, Kälte, „Wie heißen“ in J und K2
   gegen `anteile.json`. Daraus werden die Abfragen M1, M3 und M5 als Liste für `continuity-editor`.
7. **Die Zeitleiste von Akt I aus den Entwürfen:** Tag 1 (J), Tag 2 (K2, Frist 11 Tage) und die Frage, wo Kap 3–13 in
   dieser Spanne liegen, als Vorlage für M2 und P4.
8. **`storyform.py` neu laufen lassen:** `--check` meldet `overview.md` und das NCP als STALE. Ein Lauf ohne neue Wahl
   bringt sie auf den Stand des Arbeitsbaums.
