# Drafting-Brief — gemeinsame Anweisung für alle Kapitel-Drafts

> Gilt für jeden, der Kapitelprosa für *Kohärenz Protokoll* schreibt. Repo-Wurzel: `C:\Users\micha\kohaerenzprotokoll-manuscript\`. Kapitel-Dateien: `Manuscript\works\the-agency-system\works\hard-scifi-cosmic-horror-psychological-thriller\kohärenz-protokoll\chapters\`.

## 1. Pflichtlektüre vor dem Schreiben (vollständig lesen, nicht überfliegen)

1. `Plan\drafting\akt1-plan_2026-09-11.md` — der Szenenplan (für dein Kapitel UND die Nachbarkapitel, damit Anschlüsse stimmen).
2. `Plan\drafting\decision-log_2026-09-11.md` — Draft-Entscheidungen D-01 ff.
3. `chapters\01-erwachen-in-der-konstrukt-stadt.md` — **Stimm-Referenz für Kael** (Neufassung). Zusätzlich `Plan\drafting\sources\CH-01_Erwachen-Zyklus_Draft-v0_5.md` (Autorfassung v0.5) als zweite Stimm-Referenz.
4. `chapters\05-auge-des-sturms.md` — Stimm-Referenz für AEGIS/Log-Format und Fakten, auf die Kap 2–4 zulaufen und aus denen Kap 6 ff. folgen.
5. `Canon\kohaerenz-protokoll_storyform-und-outline_2026-06-10.md` — §0 (Querschnitt-Kanon, Hard-Constraints) und §5 (dein Kapitel). **Normativ bei Konflikt.**
6. `Canon\kohaerenz-protokoll_anteile-profile-sprach-dna_2026-06-10.md` — Sprach-DNA jeder Stimme, die in deinem Kapitel einbricht; §7–§8, §12.
7. `Canon\kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md` — §1.1 (KW1), §2 (Sensorik, Hitze-Polarität), §3.3, §5.3, §10 (R-1 bis R-10 + Self-Review-Checkliste).
8. `Plan\drafting\sources\KP_Plot-Konkretisierung_13-Ideen_F1-Faden_2026-06-10.md` — Teil III (F1-Faden, §0 Vokabular, §5 Kapitel-Beats).

## 2. Stimme Kael (Akt I)

1. Person, Präsens. Nüchtern, beobachtend, konkret. Kurze bis mittellange Sätze; Kommaketten erlaubt, wenn sie Routine tragen (wie in Kap 1). Welt wird positiv beschrieben; Negationsgrammatik nur an Stellen, an denen etwas nicht stimmt. Kael benennt nie sein eigenes Empfinden direkt — Empfinden liegt zwischen den Zeilen, im Körper, in Zahlen. Zähl-Tic. Atem vier/sechs. *Sensor-Rekalibrierung. Standardprotokoll.* als kursiver Selbstbefehl, sparsam. Zeitsprünge als Absatz-Schnitte ohne Kommentar. **Nie „ich erinnere mich nicht".** Metaphernverbot (KW1): keine Bilder aus fremden Welten; wenn Vergleich, dann aus Kaels eigener Welt und konkret. Kein Humor-Zwinkern, keine Ironie des Erzählers.

## 3. Harte Regeln (jede Verletzung ist ein Defekt)

- R-1 Tragische Ironie nie erklären. R-2 Nie sagen, was der Leser denken soll. R-3 Kein „Alter/Anteil/Fragment/DID/System (für Kael)" in Akt I; Stimmenwechsel nur über Syntax + Somatik + Vokabular, **nie Header, nie Sprecher-Tags**. R-4 max. 3 Stimmen-Mikrocues pro Bridge-Szene (Akt I sonst max. 2 pro Szene, Kap 2–5 max. 1 und nur als Artefakt/Somatik). R-5 Kaltes Ozon (AEGIS, scharf, elektrisch) und Wärme (Juna, hautwarm, quellenlos, ab Kap 3) **nie in derselben Szene**. R-6 max. 1 Konzept pro Szene. R-7 max. 1 Genesis-Echo pro Szene. R-8 AEGIS/Direktiven ohne Metapher, Moral, Affekt. R-9 Keine wörtlichen Zitate aus Kap 0. R-10 Juna nie grammatisches Subjekt, nie Name, nie Stimme, nie Körper.
- Keine DKT-Fachbegriffe (Coheron, Erason, Landauer, Kohärenzfeld …) in Akt I. Diegetisches Vokabular: Konsolidierung, Ausgleich, Abweichung, Wartungsfenster, Bestand, Bestandspflege, Restwert, Ausnahme.
- AEGIS erscheint in Akt I nur als VERSALIEN-Direktive auf Flächen/Konsolen; als 3.-Person-Log nur, wo der Plan es vorsieht (Log-Format wie Kap 5, Felder gemäß D-03, **ohne** das Wort „Ich").
- Keine Personen mit Namen außer Doran. Andere Bewohner sind „Einheiten".
- Kein bewusstes Wir vor Kap 9. Kaels Name „Kael" erscheint erstmals in Kap 9 (D-05).
- Tonale Achse: Schmerz und Liebe als derselbe Pulsschlag — in Akt I heißt das: die Liebe ist als Fehlstelle da, der Schmerz als Reibungslosigkeit. Kein Trost, kein Triumph.
- Dissoziation = Amnesie-Terror, nie Crew-Menü. Wenn ein Wechsel verspielt wirkt, ist die Szene falsch.

## 4. Dateiformat

Für jede Kapitel-Datei: YAML-Frontmatter und Template-Kopf (bis einschließlich der Zeile `## Outline …`) **unverändert lassen**, außer:
- `status: "drafted"`
- `pov: "Kael (Hard-A, 1. Person)"` (bzw. was zutrifft)

Dann anhängen:

```
<!-- Draft v0.1 (2026-09-11). Plan: Plan/drafting/akt1-plan_2026-09-11.md · Entscheidungen: D-xx, D-yy -->

---

# Kapitel N — Titel

<Prosa>
```

Szenenwechsel mit einer Zeile `---`. Direktiven fett in VERSALIEN (`**…**`), Logs in einem ```-Codeblock. Kursiv für Kaels Selbstbefehl und den gelockten Silas-Halbsatz.

## 5. Umfang

Zielwert steht im Plan pro Kapitel (±15 %). Nicht auffüllen; lieber eine Szene genauer als eine zusätzliche.

## 6. Nach dem Schreiben

Self-Review-Checkliste (Welt-Sensorik §10.3) für jede Szene durchgehen und korrigieren. Wörter zählen (nur Prosa). Keine anderen Dateien ändern, nicht committen. Im Abschlussbericht: Wortzahl je Kapitel; jede Stelle, an der du vom Plan abgewichen bist oder etwas neu entscheiden musstest (als Vorschlag für das Entscheidungs-Log); jeder Konflikt zwischen Plan und Canon, den du bemerkt hast.
