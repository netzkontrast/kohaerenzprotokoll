# Animatic des Erklärvideos

*Gebaut 2026-10-10 aus `../skript.md` und dem Design in `../README.md`. Ein Animatic ist eine Rohfassung zum Anschauen: die
endgültigen Bilder und Zeiten, aber Piper statt ElevenLabs und weder Musik noch Geräusche. Nichts hat den Container verlassen.*

In diesem Ordner liegt alles, was das Animatic aus Text macht. Das MP4 selbst liegt nie in git.

| Datei | was |
|---|---|
| `narration.py` | liest die Zeilen mit `> ` aus `skript.md` und lässt Piper (`de_DE-thorsten-high`) jeden Satz einzeln sprechen. `[Pause]` ergibt 0,6 s Stille, `[lange Pause]` 1,4 s. Schreibt eine WAV je Szene und `timings.json`. |
| `timings.json` | Start und Ende jedes Satzes je Szene, gemessen an Pipers Ausgabe: 66 Sätze in den Szenen 2–8, die Untertitel bekommen; 9 Szenen, 269,2 s Sprache |
| `build.py` | schreibt `index.html`: eine Komposition, neun zeitgesteuerte Abschnitte, eine pausierte GSAP-Timeline. Jede Einblendung sitzt auf dem Start des Satzes, den sie zeigt, also können Bild und Stimme nicht auseinanderlaufen. |
| `style.css` | das Design in CSS: Papier `#F4F4F0`, Tinte `#111111`, Rot `#E61919` nur für Widersprüche; Linien 2–4 px für Video |
| `DESIGN.md`, `BRIEF.md`, `STORYBOARD.md` | was HyperFrames' Ablauf `general-video` vor dem HTML verlangt |

## Neu bauen

```bash
bash scripts/install.sh hyperframes openmontage
cd .openmontage/projects && DO_NOT_TRACK=1 hyperframes init erklaervideo --example blank --resolution landscape --non-interactive
cd erklaervideo && npm install -s @fontsource/archivo@5 @fontsource/archivo-black@5 @fontsource/jetbrains-mono@5 gsap@3.14.2
mkdir -p assets/fonts assets/vendor assets/vo tools && cp node_modules/gsap/dist/gsap.min.js assets/vendor/
cp node_modules/@fontsource/archivo/files/archivo-latin-{400,600,700}-normal.woff2 \
   node_modules/@fontsource/archivo-black/files/archivo-black-latin-400-normal.woff2 \
   node_modules/@fontsource/jetbrains-mono/files/jetbrains-mono-latin-{400,500}-normal.woff2 assets/fonts/
cp ../../../Plan/runs/video/erklaervideo-2026-10-08/animatic/{build.py,style.css,narration.py} tools/
cd ../.. && PATH=$PWD/.venv/bin:$PATH .venv/bin/python -I projects/erklaervideo/tools/narration.py \
   ../Plan/runs/video/erklaervideo-2026-10-08/skript.md projects/erklaervideo/assets/vo de_DE-thorsten-high.onnx
cd projects/erklaervideo && python3 tools/build.py && DO_NOT_TRACK=1 hyperframes check && DO_NOT_TRACK=1 hyperframes render
```

## Gemessen

- Sprache: 269,2 s. Bild: 273,2 s, also 4:33. Szene 1 hält danach 1 s, Szene 9 hält 3 s für den Titel.
- `hyperframes check`: 0 Fehler. 12 Lint-Warnungen bleiben stehen; alle empfehlen Unterkompositionen statt einer Datei. Runtime,
  Layout (9 Stichproben) und Bewegung haben keinen Befund, Kontrast 40 von 40 Textprüfungen nach WCAG AA.
- **Eine Datei statt neun Unterkompositionen.** Wie eine Unterkomposition relative Pfade auflöst (Schriften, Ton), ist nicht
  dokumentiert, und jede müsste ihre `@font-face` selbst tragen. Eine Datei vermeidet beides.
- Aus dem Katalog geprüft und als Technik übernommen: `grain-overlay` (Papierkorn), `typewriter` (Fortschritt als CSS-Variable,
  `steps()`), `strikethrough-replace` (Strich mit `scaleX`). Schriften und GSAP liegen lokal, beim Rendern gibt es keinen
  Netzabruf.
- Eine Prüfrunde mit Kontaktbogen fand sechs Fehler in Szene 5–9, darunter die Platten im Bewegungsmoment: Sie schoben sich
  übereinander statt 40 px voreinander stehen zu bleiben. Alle sechs wurden in einem Durchgang behoben und mit einer
  Bestätigungsrunde geprüft. Die Laufzeitprüfung fand danach noch eine fehlende Kante zu C6.

## Was die Endfassung noch braucht

1. Stimme von ElevenLabs (Entscheidung 029), sobald `ELEVENLABS_API_KEY` gesetzt ist. `narration.py` bekommt dafür eine zweite
   Quelle, `build.py` bleibt, weil es nur `timings.json` liest.
2. Musik und die zwei Geräusche nach `../README.md`, gemischt mit `hyperframes-audio`.
3. Die Länge: Piper spricht etwa 129 Wörter pro Minute, das ergibt 4:33 statt 5:00. Eine ruhigere Stimme oder längere Pausen in
   `skript.md` schließen die Lücke. Am Text muss dafür nichts geändert werden.
