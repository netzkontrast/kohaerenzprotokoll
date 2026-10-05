# Kael, Juna und die Anteile gegen Storyform und NCP — und wann, wie und wo sich die Anteile zeigen (2026-10-05)

**Auftrag des Autors (2026-10-05):** „gleiche mit dramatica und ncp ab und denk schon mal drüber nach was wir im Plot
brauchen - wann um wie und wo sich die Alter zeigen“.

**Grundlage:**
- Kaels Karte (`Plan/runs/writing/book/character-card-builder_kael_2026-10-05.md`) und Junas Karte (Kanon, id `Juna`);
- die Vorschläge zu den Anteilen (`character-card-builder_alters_2026-10-05.md`, kurz **AL**) mit der Charakter-Bibel
  (**CB**, `kohaerenz-protokoll-charakter-bibel-2026-05-08-md.md`);
- die Storyforms `Plan/storyform/a.json` und `b.json`, das Weaving `weave.json` und die NCP-3-Datei.

Teil 1 ist eine Prüfung. Teil 2 ist ein **Vorschlag**, über den nichts entschieden ist.

---

## Teil 1 — der Abgleich

### Kael gegen Storyform A (MC)

| Storyform A | Kaels Karte | trägt? |
|---|---|---|
| Problem **Inertia**, das Weitermachen im selben Zustand | Lügen „Solange der Tag richtig ist, bin ich ganz“, „Wenn ich nichts fühle, verliere ich nichts“ (K1) | ja |
| Lösung **Change** | Need: die zehn Jahre tragen, fühlen dürfen, sprechen, wo er schwieg (K2) | ja |
| Focus **Chaos** → Direction **Order** | Want: Ordnung, die Null am Abend. Er sieht Chaos (Lücken, Risse) und antwortet mit Ordnung | ja, genau |
| Concern **Memory**, Issue **Suspicion** | die vergessenen zehn Jahre (F10), Misstrauen gegen die eigenen Lücken | ja |
| Approach **Be-er** | er löst innen, nicht durch äußere Tat (CB:L341) | ja |
| Growth **Stop** | er muss *aufhören* zu vergessen und *aufhören*, alles in Ordnung zu halten | ja |
| Signposts Memory → Subconscious → Preconscious → Conscious | das ist zugleich die Reihenfolge, in der die Anteile hörbar werden (Teil 2) | ja, und trägt Teil 2 |

### Ein Befund: Entscheidung 025, Schritt 13, ist veraltet

Schritt 13 sagt über As Konsequenz („Die Fragmentierungsnacht wiederholt sich“): „a Start story, so it only threatens“.
Seit Schritt 16 ist A aber eine **Stop-Story** (Growth Stop). Damit droht die Konsequenz nicht nur, sie **läuft schon**.
Das generierte NCP sagt das bereits richtig (`storyform.py`: „Stop-Story: die Folgen laufen schon“).

Mit deiner Antwort K4 passt es genau. Die Fragmentierungsnacht hat schon stattgefunden: Die drohende Trennung hat sie
ausgelöst, und die zehn Jahre sind weg. Was droht, ist ihre Wiederholung, wenn Juna wirklich geht. Der Text von Schritt
13 ist entsprechend korrigiert, mit Vermerk.

### Kael gegen Storyform B (IC, Antagonist, Emotion)

- **IC-Problem Disbelief → Faith** (Schritt 19) passt zur Lüge „Wer mir nah ist, wird verletzt“. Er glaubt nicht an die
  eigene Liebe als etwas, das nicht schadet. Faith hieße, ihr zu trauen.
- **Antagonist und Emotion in B** (Uncontrolled, Feeling, Schritt 31): Aus AEGIS' Sicht ist Kael das Gefühl, das sich
  nicht kontrollieren lässt. In A trägt Nyx genau diese Elemente als Emotion-Archetyp. Das ist dieselbe Kraft, von zwei
  Seiten gesehen. Kein Widerspruch: Die Anteile sind Figuren in Kaels Player (Schritt 17).

### Juna gegen Storyform A (IC, steadfast)

Sie trägt **Change** und bleibt standhaft. Ihre Haltung, dass Wandel möglich ist, bleibt, ihr Verhalten reift. Das ist
so im Kanon festgehalten. Ihr Need „sprechen statt schweigen“ und Kaels Need „sprechen, wo er schwieg“ sind dieselbe
Bewegung. Damit hat die Beziehung (A-RS, Ability → Desire: der Kanal als Fähigkeit ist das Problem, Begehren die Lösung)
einen Inhalt: Sie *können* sich ohne Worte verstehen, und genau deshalb sagen sie nichts.

### NCP

- Die Datei kennt **Kael, Juna und alle Archetypen als Players**. `bio`, `visual` und `audio` stehen auf „offen“.
- **Vorschlag:** `storyform.py` liest für die NCP-Biografie die Kanon-Zeilen aus `Manuscript/kanon.md`, für Juna jetzt
  schon. Damit hätte das NCP eine Quelle, statt sie zu kopieren.
  - Das wäre ein Leser von `Manuscript/` außerhalb von Wiki und Sources. Erlaubt ist das, aber neu.
- **Später:** Die Erscheinungen der Anteile aus Teil 2 können **storybeats** mit Scope `progression` oder `event` werden,
  die an den Kapitel-Moments hängen. Das ist erst sinnvoll, wenn du Teil 2 bestätigt hast.

---

## Teil 2 — wann, wie und wo sich die Anteile zeigen (Vorschlag)

### Die Regeln, die es schon gibt

- **Akt I:** Kael weiß nicht, dass er ein System ist. Erst in Kap 13 fällt der Schleier (CB:L349, Weaving: Kap 13 Bridge,
  Vortex-Vorläufer). Bis dahin spürt er die Anteile als „Modi“, „Stimmungs-Drifts“, „Stimmen“, „Systemrauschen“, ohne
  Namen.
- **Plot von A:** Die Vorzeichen sind **Preconscious**, also Durchbrüche der Anteile und Zeitlücken. Vorbedingung ist
  **Present**: nur in Zeitlücken.
- **As OS-Kapitel** (Psychology) sind die Kapitel, in denen das Ensemble der Anteile *handelt*. Die Archetypen der äußeren
  Handlung von A sind Anteile: Selene, Oblivion, Lex, Nyx.

### Wie: drei Kanäle, ohne Namen bis Kap 13

1. **Körper:** die Somatik jedes Anteils aus der Bibel, zum Beispiel Lex' eiskalte Hände, Alex' Kiefer, Rhys' fiebrige
   Hände, Kikos Kleinwerden, Moros' bleierne Glieder.
2. **Satzbau:** Kaels Prosa kippt in die Syntax eines Anteils. Bei Lex wird sie hypotaktisch, bei Nyx stakkato, bei Lia
   brechen die Sätze ab, bei Silas korrigiert sich der Satz als Echo, bei Oblivion löscht er sich.
3. **Spur:** eine Tat, an die Kael sich nicht erinnert, etwa die linke Hand, eine Lücke, ein erledigter Posten, eine
   blutige Knöchelhaut.

### Wann und wo, nach Akten (Kapitel aus dem Weaving)

**Akt I — Signpost Memory. Lücken, kein Name.**

| Kap | Strang | Anteil | wie |
|---|---|---|---|
| 1 | A-MC | **Silas**, **Oblivion** | Die linke Hand drückt RÜCKFRAGE und schützt den Anschluss, das ist Silas als Spur. Der abgebrochene Satz ist ebenfalls Silas (Entwurf G). Die verlorenen Minuten sind Oblivion. |
| 2, 5, 9 | A-OS (Being) | **Lex**, **Alex** | Lex als Kälte in den Händen und Ordnung, die sich verdoppelt; Alex als Körper, der sich wappnet, bevor Kael Gefahr sieht |
| 3 | A-MC | **Kiko** | Die Zeit stockt, Kael findet sich am Boden eines Korridors |
| 8 | A-MC | **Rhys** | ein „Wir“ im Satz; Fürsorge für einen Fremden, die nicht seine ist |
| 12 | A-MC | **Nyx** | Knöchel, die bluten, und eine Wut ohne Erinnerung (CB:L322) |
| 13 | Bridge | **Selene** | Kaels Entscheidung, nicht mehr zu bestätigen (13/14). Der Schleier fällt, die Stimmen bekommen ihre Namen. Selene erscheint zum ersten Mal, „Wenn sie auftaucht, ist es spät“ (CB:L498) |

**Akt II — Signpost Subconscious. Die EPs, die tiefsten Wünsche; drei Spiral-Zyklen.**

| Kap | Anteil | wie und warum |
|---|---|---|
| 14–17 (Z1) | **Kiko**, **Lia** | Die erste Erasure-Welle trifft. Kiko erstarrt, Lia will Juna halten und wegstoßen (die Trennung im Inneren, K3) |
| 18 (Bridge, Genesis) | **Oblivion** | Akt II nach der Bibel: Er sieht erstmals, *was* er löscht (CB:L779). In der Genesis-Rückblende ist das die Fragmentierungsnacht von innen. |
| 19–20 (Z2) | **Argus**, **Lex ↔ Nyx** | Argus bemerkt AEGIS' Fehler als Erster (CB:L502). Lex und Nyx im „maximalen Konflikt“ (CB:L382) |
| 21 (Bridge) | **Silas** | „*Bin ich echt oder nur ein Echo?*“ (CB:L743); die Moonshine-Spur der zehn Jahre |
| 23 | **Rhys ↔ Moros** | Rhys versucht, Moros zu retten, und scheitert. Die Bibel nennt das „zentral in Akt II“ (CB:L705) |
| 24–25 | **Nyx als Isabelle** | Kontrolle über Nähe statt Nähe, als Spur aus den zehn Jahren mit Juna (Akt II: Junas Spuren, Kap 17, 25) |
| 26 (Bridge) | **das Wir**, **Selene** | Die Entscheidung, zu Juna zu gehen (26/27). Selene weiß, wer Juna war (K3) |

**Akt III — Signpost Preconscious. Die Spiegel-Alters, Impulse.**

| Kap | Anteil | wie und warum |
|---|---|---|
| 29 | **Kiko** | die Angst des Kindes, das letzte Aufflammen vor dem Weg |
| 30 | **Alex** | Er schützt den Weg zu Juna, gegen AEGIS' Purge (Kap 28) |
| 31 (Bridge, Spiegel) | **Oblivion** | Er löscht schneller, als Silas empfängt, und es entsteht Landauer-Hitze (CB:L753) |
| 32 (Bridge, Spiegel) | **Silas**, **Juna** | Die erste Begegnung in der Gegenwart. Silas erkennt sie, bevor Kael es tut. Echo trifft auf Ursprung |
| 34 (Bridge) | **Lia** | Kael lässt Juna gehen. Lias „Komm her / Geh weg“ entscheidet sich für „Geh“, und das ist die Lüge „Wer mir nah ist, wird verletzt“ in Tat |

**Vortex — Signpost Conscious. Bewusstsein, Wahl, Wir.**

| Kap | Anteil | wie und warum |
|---|---|---|
| 35 | **Oblivion** | Die Wahl: weiterlöschen oder stehenlassen (CB:L780). Er hört auf, Kaels Amnesie bricht zusammen, und das ist der Pivot Inertia → Change |
| 36 | **Moros**, **Selene** | Moros' „Drachenkampf“ (CB:L710); Selene als Architektin |
| 37 | **Lex** | Der falsche Friede, die Ordnung kehrt zurück, scheinbar |
| 38–39 | **alle**, **Juna** | funktionale Multiplizität (CB:L352), das Wir; Juna in der Zukunft der beiden |

### Was offen ist

- **Wo, als Ort:** Akt I spielt in KW1, der Konstrukt-Stadt (C9, Kanon). Welche Kernwelten die Akte II und III tragen, ist
  Q5 und nicht entschieden. Die Tabellen geben deshalb Kapitel, keine Orte.
- **Wie viele Anteile im Buch** sind, ist W10 und Q3. Der Plan nutzt alle zwölf der Bibel. Ein kleinerer Kreis ließe
  einzelne Zeilen weg.
- **Wer ist die linke Hand?** In Entwurf G schützt sie den Anschluss. Silas ist der Vorschlag. Selene oder Alex wären
  ebenfalls möglich.
