# Erklärvideo „Kohärenz Protokoll“: Plan

*Stand 2026-10-08. Der Autor hat ein Erklärvideo von fünf Minuten erbeten und die offenen Fragen delegiert: „Beantworte dir die Fragen selbst“.
Jede Antwort steht unten mit ihrem Grund. Nichts hier ist Kanon, und das Video entscheidet nichts über den Roman.*

Dieser Ordner hält, was eine Produktion an Text erzeugt (Skill `openmontage`, Regel 5): diesen Plan und das Skript mit dem
Szenenplan in `skript.md`. Bild und Ton werden nie committet.

## Die fünf Fragen, selbst beantwortet

| Frage | Antwort | Grund |
|---|---|---|
| **Thema** | Die **Methode** des Projekts: wie aus vielen widersprüchlichen Quellen ein belegter Boden für einen Roman wird | Die Welt des Romans darf nur zeigen, was `Manuscript/kanon.md` hält, und das ist noch zu wenig für fünf Minuten. Die Methode ist vollständig belegbar, und sie ist das, was das Projekt von „KI schreibt einen Roman“ unterscheidet. |
| **Publikum** | Literarisch interessierte Menschen ohne Technikhintergrund: Leserinnen und Leser, Agenturen, Verlage | Daraus folgt der Wortschatz. Das Video sagt „Liste der Begriffe“ statt Zensus, „Konfliktbericht“ statt Reconciliation-Record, „Netz“ statt Graph-Store. |
| **Format** | 16:9, 1920×1080, 25 fps, 5:00 | Fünf Minuten Erklärung schaut man am Desktop oder Fernseher. Hochformat bleibt dem Buch-Teaser. |
| **Stimme** | ElevenLabs für die Endfassung, Piper (`de_DE-thorsten-high`) für das Animatic | Entscheidung 027 hält fest, was an ElevenLabs gehen darf: der Sprechertext, der keine zwölf aufeinanderfolgenden Wörter einer Quelle enthält. |
| **Konzept** | **B mit dem Hook von A**: „Das Leben eines Dokuments“, eröffnet mit „Hier schreibt sie keinen Satz“ | B macht die Methode anfassbar, weil man einem echten Dokument folgt. A gibt ihr die Fallhöhe. C (der Zahlentrichter) veraltet am schnellsten. |

**Das Dokument, dem das Video folgt**, ist `guardians-und-kern-welten-konzept` (2025-04-17). Seine Geschichte ist der ganze
Ablauf an einem Fall: gelesen, auf die Wiki-Seite gebracht, von einem Dokument von 2026 widersprochen, Konflikt C6, vom Autor
entschieden, Zeile C6 in `kanon.md`. Das Dokument von 2026 erklärt sich dabei selbst zur „Source-of-Truth“ und schreibt „bei
Konflikt gewinnt das Neuere“ ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L13]. Das System folgt dem nicht. Dieser Moment trägt das Video.

## Modus und Stilwelt (Skill `impeccable-taste`)

**Modus: Lesen.** Erfolg heißt verstanden haben. Daraus folgt:
- eine Idee pro Szene;
- eine feste Hierarchie: Zahl, Satz, Beleg;
- Untertitel immer an;
- **ein** großer Bewegungsmoment, alles andere tragen Schnitt und Typografie.

**Ist-Zustand.** Die Projekt-App (`scripts/ui.html`, Vercel) ist die bestehende Designentscheidung. Vor dem Bau der ersten Szene
werden ihre Farben und Schriften gelesen. Das Video darf eine eigene Welt haben, weil es einen anderen Zweck hat, aber es darf der
App nicht widersprechen: Eine Konfliktfarbe, die in der App etwas anderes bedeutet, wäre ein Fehler.

**Stilwelt: Industrial Brutalist, Variante Swiss Industrial Print (hell).** Das Projekt besteht aus Dokumenten, Zeilen und
Zitaten, also aus Papier und Tinte. Die übliche KI-Optik (Schwarz, Glas, Leuchten) würde der Kernaussage widersprechen, dass die
Maschine nichts entscheidet.

| Token | Wert | Gebrauch |
|---|---|---|
| `--paper` | `#F4F4F0` | jeder Hintergrund |
| `--ink` | `#111111` | Text, 1-px-Linien |
| `--ink-muted` | `#5A5A55` | Metadaten, Zeilennummern (Kontrast gegen `--paper` über 6:1) |
| `--conflict` | `#E61919` | **nur** wo Quellen sich widersprechen, und nur in großen Flächen oder Linien (unter 4,5:1 auf Papier, deshalb nie für Fließtext) |
| Display | Archivo Black, 160–220 px, Tracking −0.02em | Zahlen, Titel |
| Text | Archivo, 44 px (Untertitel), 56 px (Aussagen) | Sätze |
| Daten | JetBrains Mono, 28–32 px | Belege `slug:Lnn`, Dateinamen, Daten |
| Raster | 12 Spalten, Rand 96 px, Radius 0, keine Verläufe, keine weichen Schatten | alles |

Die Schriften werden lokal eingebettet (`hyperframes-localize-fonts`). Der Proxy dieses Containers kann Google Fonts im
Render-Browser blockieren.

**Bewegung.** Harte Schnitte und lineare Wischblenden, Mono-Text als Schreibmaschine mit 30 Zeichen pro Sekunde. Der einzige große
Moment ist Szene 6: Zwei Zitatplatten gleiten von links und rechts heran (`power4.out`, 1,2 s), bleiben 40 px voreinander stehen,
und dazwischen zieht sich in 0,6 s eine rote Linie. Danach Stille, 0,8 s.

## Ton

- **Stimme:** ruhig, nah, nicht werblich. Das Skript hat 580 Wörter (gezählt 2026-10-08). Bei etwa 125 Wörtern pro Minute und den
  markierten Pausen ergibt das 5:00.
- **Musik:** minimaler Puls um 90 BPM, gedämpftes Klavier über einem tiefen Synthesizer. Unter der Stimme abgesenkt, in Szene 6 für
  2 s ganz weg. Quelle: Suno über den Account des Autors (Prompts vom Skill `suno-lyric-writer`) oder eine Pixabay-Spur
  (`pixabay_music`, ohne Key).
- **Geräusche:** genau zwei. Papierrascheln in Szene 3, ein einzelner Schreibmaschinenanschlag, wenn die rote Linie steht.
- **Pegel:** −14 LUFS integriert, True Peak −1 dBTP. Gemischt mit `hyperframes-audio` oder OpenMontages `audio_mixer`.
- **Untertitel:** satzweise, eingebrannt, Archivo 44 px im unteren sicheren Bereich.

## Produktion

OpenMontage-Pipeline `animated-explainer`, Ausgabe mit HyperFrames aus dem Fork.

| Stufe | Stand | Was |
|---|---|---|
| research | erledigt, hier | Die Quelle ist das Repository selbst: C6, `kanon.md`, die gemessenen Zahlen in `skript.md`. Eine Web-Recherche über andere Erklärvideos entfällt, weil das Thema nur hier existiert. |
| proposal | erledigt, hier | Konzept B mit Hook A, gewählt durch Delegation. Laufzeit: **HyperFrames**. **Remotion abgelehnt**, Grund: „runtime cannot render behind this container's proxy“ (Skill `openmontage`). |
| script | Entwurf | `skript.md` |
| scene_plan | Entwurf | `skript.md`, Spalten „Bild“ und „Layout“ |
| assets | offen | **keine generierten Bilder.** Jedes Dokument wird als typografische Platte aus seinen echten Zeilen gesetzt, lokal und ohne Bildschirmfotos. |
| edit / compose | offen | HyperFrames-Skills `general-video`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-registry` |
| publish | offen | Das MP4 geht an den Autor als Artifact-Asset, nie in git. |

**Kosten.** Piper und HyperFrames kosten nichts. ElevenLabs berechnet nach Zeichen. Der Sprechertext hat rund 3 800 Zeichen (gezählt
2026-10-08). Vor dem Aufruf wird mit `estimate_cost` neu gezählt, und der Preis wird genannt, bevor bezahlt wird.

**Renderzeit.** Gemessen: etwa 3× Echtzeit auf der CPU dieses Containers, also rund 15 Minuten für 5:00.

## Bevor gesprochen wird

1. Die Zahlen in `skript.md` neu messen: `python3 scripts/state.py --prose` prüft ihre Marker.
2. Den Zwölf-Wörter-Test über den Sprechertext laufen lassen (Entscheidung 027). Am 2026-10-08 fand er gegen alle gelandeten
   Dokumente keinen Treffer: `route.shingles` über die Zeilen mit `> ` in `skript.md`, Regieanweisungen entfernt.
3. Ein Animatic mit Piper rendern und dem Autor zeigen. Erst danach geht der Text an ElevenLabs.
