# Dramatica — was fertig ist, was fehlt, in welcher Reihenfolge (2026-10-05)

**Auftrag des Autors (2026-10-05):** „what we Need Next f im dramatica“.

**Grundlage:**
- `Plan/storyform/a.json`, `b.json`, `weave.json`, `anteile.json`;
- Entscheidung 025, Schritte 0–39;
- `scripts/dramatica.py`, dessen Prüfungen R1–R8 nur Regeln enthalten, die die Tafel von 1995/1999 selbst trägt.

## Fertig, beide Storyforms

| Ebene | Was steht |
|---|---|
| Throughlines | alle vier, je Klasse, Concern, Issue (mit Gegenpol), Problem, Lösung, Focus, Direction, vier Signposts |
| Dynamik | alle acht: Treiber, Grenze, Ausgang, Urteil, Resolve, Growth, Approach, Stil |
| Plot Story Points | Ziel und alle sieben weiteren (Requirements, Consequence, Forewarnings, Costs, Dividends, Prerequisites, Preconditions) |
| Crucial Element | abgeleitet (im NCP) |
| Figuren | alle Archetypen beider Storyforms besetzt (Schritte 28–31); die Anteile als Ensemble von A |
| Rahmen | Prämisse, Genre, Logline; das Weaving 0–40 mit Routen und Ankern; die Treiber-Ereignisse an den drei Aktübergängen (H11) |
| Szenen | Akt I und Akt II als Szenenlisten (Arbeitsgrundlage); dazu die Ereignis- und Wissenstabelle für Akt I |

## Was fehlt

### 1. Benchmark, vier je Storyform — **erledigt 2026-10-05** (Schritt 40)
- **Was:** Woran sich der Fortschritt einer Throughline messen lässt. Der Benchmark ist ein Type.
- **Wozu:** Das Treatment braucht für jeden Strang eine Messlatte. Für A-MC könnte das sein, wie viele Lücken Kael
  füllen kann, bevor die Ordnung kippt.
- **Prüfbar:** Dass es ein Type ist, ja. Welcher Type, nach Regel, nein, denn die Zuordnung steht nur in der
  lizenzierten DSM. Es bleibt deine Wahl, wie bei den Signposts.

### 2. Unique Ability und Critical Flaw von MC und IC, je Storyform
- **Was:** Die eine Fähigkeit, ohne die die Figur nicht gewinnen kann, und der eine Fehler, der sie aufhält. Beides
  sind Elemente.
- **Wozu:** Die Karten von Kael, Juna und AEGIS bekämpfen sich heute nur über Want und Need. Die Ability gibt Kael ein
  Werkzeug für Kap 13 und den Vortex. Der Flaw gibt AEGIS den Grund, warum es steadfast scheitert.
- **Prüfbar:** nur, dass es ein Element ist. Die Wahl ist deine.

### 3. Catalyst und Inhibitor, je Storyform
- **Was:** Was die Geschichte beschleunigt und was sie bremst. Das sind Variationen.
- **Wozu:** Sie sind das Werkzeug für das Tempo, gerade für Akt II mit seinen drei Zyklen. Ein Kandidat für A ist das
  Wartungsfenster als Catalyst (aus der Ereignistabelle), ein Kandidat für den Inhibitor das Vergessen selbst.

### 4. Die Journeys, drei je Throughline
- **Was:** die Übergänge zwischen den Signposts, 1→2, 2→3, 3→4.
- **Wozu:** Sie sind die Brücke zwischen der Szenenliste und dem Treatment. Für Akt I und II sind sie in den Listen
  implizit, für Akt III und den Vortex fehlen sie.

### 5. Szenenlisten für Akt III (Kap 27–34) und den Vortex (Kap 35–39)
- **Wozu:** Damit stehen alle 41 Bewegungen im selben Raster.
- **Hängt an:**
  - der Übergang 34/35 (H11 steht);
  - Q8, was nach dem Vortex aus AEGIS wird;
  - W12, ob Genesis und Fragmentierungsnacht ein Ereignis sind.

### 6. Progressions und Events
- **Was:** 16 Progressions und 64 Events je Throughline, die Feinstruktur unter den Signposts.
- **Wozu:** Das NCP hat dafür die storybeats `progression` (bis 16) und `event` (bis 64).
- **Wann:** erst mit dem Treatment, Kapitel für Kapitel. Heute zu füllen hieße, Szenen zu erfinden, die noch nicht
  geplant sind.

### 7. Die offenen Weichen, die Dramatica-Werte berühren

| Weiche | was offen ist | betrifft |
|---|---|---|
| W12 | Genesis und Fragmentierungsnacht: ein Ereignis oder zwei | B-MC Signpost 1 (Past), Kap 0, 18, 40 |
| C14 | was das AEGIS-Ich wissen darf | B-MC, Kap 0, 6, 16, 22, 28 |
| Q8 | AEGIS nach dem Vortex | B-Ausgang Failure, Kap 36–40 |
| Q5 | Namen von KW2–KW4, die Guardians | Schauplätze, B-Ensemble |

## Empfohlene Reihenfolge

1. **Benchmarks** (8 Werte). Das ist billig und stark: Das Treatment bekommt seine Messlatten, und es hängt an keiner
   offenen Weiche.
2. **Unique Ability und Critical Flaw** (8 Werte). Sie ergänzen die Karten von Kael, Juna, AEGIS und Kael-in-B.
3. **Catalyst und Inhibitor** (4 Werte), mit dem Wartungsfenster als Kandidat.
4. **W12** vor der Szenenliste für den Vortex, weil Kap 18, 35–40 davon abhängen.
5. **Szenenlisten für Akt III und den Vortex**, mit den Journeys darin.
6. **Das Treatment**, und erst dort Progressions und Events.

**Die Werkzeugseite:** `a.json` und `b.json` können die neuen Felder mit Herkunft tragen. `storyform.py` würde dann
prüfen, ob der Benchmark ein Type ist, ob Unique Ability und Critical Flaw Elemente sind und ob Catalyst und Inhibitor
Variationen sind, und schriebe sie ins NCP. Welche Werte es sind, rechnet es nicht aus. Das bleibt deine Wahl.
