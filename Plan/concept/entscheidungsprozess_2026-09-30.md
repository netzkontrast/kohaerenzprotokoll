# Entscheidungsblätter: so arbeiten wir sie durch

**Stand 2026-09-30, vereinfacht nach `/simplify`.** Beschlossen ist der Prozess in Entscheidung 016; hier steht er in der Kurzform, darunter die Querprüfung der Blätter W1–W10 und WP (Runde 0). Keine Story-Frage ist dadurch entschieden.

## Der Prozess in drei Schritten

1. **Querprüfen.** Vor einer Runde prüfe ich die Blätter gegeneinander: Abhängigkeitsgraph aus den Köpfen, Verträglichkeit der Empfehlungen je Paar, Abgleich mit deinen entschiedenen Records (C6, C9) und den berichteten Sperren. Bei den Schlüsselfragen der Runde (höchstens fünf) liest je ein Agent das Blatt ohne die Empfehlung und gibt seine eigene Wahl ab. Das misst Stabilität, nicht Wahrheit: Es ist dieselbe Modellfamilie.
2. **Fragen.** `AskUserQuestion`, höchstens vier Fragen je Aufruf, 2–4 Optionen. Die empfohlene steht zuerst, mit der Quelle der Empfehlung im `description`. Jede Option trägt ein `preview`: was sie in den ersten drei Bewegungen ändert, als Ereignis, nicht als Begriff. „Other" ist der Freitext-Weg. Sortiert nach Freischaltung (W7, W6 vor W9, W10).
3. **Aufzeichnen und nachziehen.** Je Runde eine Entscheidungsdatei unter `Plan/decisions/`, im Blatt `status: beantwortet`, im Record, den die Antwort schließt. Danach: welche Blätter ändern ihre Abhängigkeiten, welche Empfehlung fällt weg, was bewegt sich im Treatment. **Nur deine Antwort setzt `beantwortet`.** Was du nicht beantwortest, läuft als `PROVISIONAL` mit `ALT`.

**Der Kopf eines Blatts** hat sechs Felder, weil jedes davon ein Schritt oben benutzt: `id`, `status`, `hängt_ab_von` (Graph), `frage_art` (Triage), `auslöser` (bei Standardwert oder Vertagung), `empfehlung` (Verträglichkeit). Was ein Schritt nicht benutzt oder was sich ableiten lässt, steht nicht drin: Wer von einem Blatt abhängt, folgt aus den `hängt_ab_von` der anderen, Kapitel stehen im Text, und „Empfehlung von der Session" gilt, solange der Status nicht `beantwortet` ist. Ein Prüfskript für Format und Graph schlage ich erst nach Runde 1 vor (P3).

## Welche Fragen in eine Runde gehören

Vier Prüffragen pro Blatt, der Reihe nach. Nur was bei allen vieren besteht, wird gefragt:

1. Nur du? (Geschmack, Absicht, Kanon. Nicht, was ein Pilot misst.)
2. Blockiert es andere Blätter?
3. Ist die Antwort teuer zu ändern?
4. Kann ein Pilot oder Standardwert sie vorerst tragen? Dann nicht jetzt fragen.

**Runde 1, nach dieser Triage:**

| Art | Fragen |
|---|---|
| **Schlüsselfragen** | **K0** Theorie: Rezept, Diagnose, Gerüst? (W1) · **K1** Gegenkraft: Wer oder was will etwas, das Kael verhindert, und wie reagiert es auf seinen Trick? (W2, W6, W10, WP) · **K2** Verlust: Was oder wen verliert Kael zuerst, unwiderruflich? (W5, W9, W10, WP) · **K3** Lesersicht: Was weiß der Leser wann, entsteht ein gespieltes Wir? (W7, W6) · **K4** Raum: eine Stadt oder reist Kael? (W8) |
| **Einmal bestätigen** | das Sperren-Blatt: die 15 berichteten Sperren vom 2026-05-30/31 je bestätigen, ändern, streichen. Es beantwortet W5 und Teile von W6, W7, W9, W14 |
| **Schalter** | Wärme exklusiv Juna · Kaels Name früh · DKT-Wort · Anfangszeile behalten · Kosten physisch oder als Anzeige |
| **Standardwert, Pilot prüft** | W3 Stimme · WP-Types und Signposts · W5 im Detail · W9 Körper/POV · W10 Listenlänge |
| **Vertagt mit Auslöser** | W4 Rahmen, W13, W14, W16 |
| **Erst vorbereiten** | W12 Genesis und W15 Moonshine-Link: von anderen Blättern genannt, ohne eigenes Blatt |
| **Prozess** | A–D im Schreibplan §11 |

## Querprüfung Runde 0

**Abhängigkeiten** (wie oft ein Blatt in den „Abhängigkeiten"-Absätzen der anderen steht): W7 sechsmal, W6 viermal, W2, W9 und W12 je dreimal, W15 zweimal.

**Was sich erst im Vergleich zeigt:**

1. **W5 B widerspricht einer berichteten Sperre,** nicht einem Blatt: Kaltes Ozon gilt dort als Unterdrückung, Wärme als Junas Spur, Landauer-Hitze nur am Vortex (`Plan/runs/plot-2026-09-30/03-constraints.md`, §1.2). Erst deine Antwort auf die Sperre macht W5 beantwortbar.
2. **W2 C und W8 A ziehen nicht am selben Strang.** W2 C funktioniert auch in einer Stadt. W8 empfiehlt die Reise und nimmt damit einen Vorteil von W2 C zurück. Keine Unverträglichkeit.
3. **Vier Empfehlungen vertagen je eine Identität** (W4 Rahmen, W6 Sicht, W9 Junas Herkunft, W10 Besetzung). Zusammen lassen sie dem Treatment keinen Ort und keine Figur. Wer alle annimmt, bekommt die abstrakte Probe von PR 114.
4. **W9 braucht einen Verlust mit Träger, W10 C lässt die Besetzung offen.** K2 löst das auf.
5. **WP** stellt PR 118 auf Alltagsfragen vor Types um, und ich folge dem. Start/Stop und Crucial Element gelten dort als ungeprüfte Hypothesen.

**Drei Korrekturen aus `antwort-pr113`, die ich übernehme:** Das Gutachten war eine Stichprobe (ein Prüfauftrag, kein Urteil über ungelesene Kapitel). Null Treffer für „Story Goal" sind eine Begriffslücke, kein Beweis fehlender Plotfunktion. Ein Gegner mit Willen ist ein Kandidat, keine Notwendigkeit: K1 fragt nach einer Gegenkraft mit Ziel und Reaktion.

## Welche Skills wofür

`continuity-editor` (Abgleich gegen Records, als Logik auf die Blätter), `developmental-editor` und `scene-architecture` (nur als Prüfkriterien), `character-card-builder` (W10; interviewt dich selbst per `AskUserQuestion`), `dramatica-theory`, `dramatica-vocabulary`, `ncp-author` (nur Diagnose, W1 B). Ohne Prosa nicht anwendbar: die Leser-, Lektorats- und Coach-Skills. Jev nicht ohne dein Ja.
