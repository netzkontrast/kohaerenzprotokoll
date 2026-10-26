# Claims — every cited sentence beside its line

Fill the last two columns of every row and save the file as `claims.md` beside this one. `python3 scripts/claims.py check <slug>` fails on an empty cell. Read the lines: `python3 scripts/read.py <slug> --from N --to N`, several in one call.

- **who says it** — `document`, or `source: <who>` when the line reports another source;
- **holds?** — `yes`, or `fixed` after you changed the sentence.

| # | where | your sentence, up to its citation | line | its opening words | cues in the line | who says it | holds? |
|---|---|---|---|---|---|---|---|
| 1 | note — 1 · What kind of text this is, and how i <!--claim:ed4bf465ce9b1b412585063c7e15375770692872eef16159f6aedb32e6fd62c5--> | - It closes with the labels „Status: Abschlussbericht erstellt.“ | L238 | Status: Abschlussbericht erstellt. |  | document | yes |
| 2 | note — 1 · What kind of text this is, and how i <!--claim:4c88c12deebd3fa385a2ca45bfcf6e65ff67b2e2a9b01f1a6ed5ff75f3873d09--> | and „Empfehlung: Sofortige Implementierung des Resonanz-Kodex zur Operationalisierung der Golden Sources.“ | L240 | Empfehlung: Sofortige Implementierung des Resonanz-Kodex zur Operationalisierung der |  | document | yes |
| 3 | note — 1 · What kind of text this is, and how i <!--claim:35b77b0c255c5f0a074fee129572930c68aae76b62a588c85b99d83d489a4931--> | - It heads a proposal „Konzept für das neue Master-Dokument“ | L185 | ### **Konzept für das neue Master-Dokument: "Der Resonanz-Kodex"** |  | document | yes |
| 4 | census — Stance, read per passage <!--claim:7be5c0a0bbe8c9258b4c3100a71974e4b8fd4815d1bf18d054404c856ec9c629--> | It calls itself „eine forensische Tiefenanalyse der Projektarchitektur“ | L15 | Das vorliegende Dossier stellt eine forensische Tiefenanalyse der |  | document | yes |
| 5 | census — Stance, read per passage <!--claim:54144dfe36537b66a8f00b00fc6428b67f793555d3018dcb99ced72ad7df3836--> | „Cluster A: Die Konstitution (Kanon & Ontologie)“ | L141 | ### **Cluster A: Die Konstitution (Kanon & Ontologie)** |  | document | yes |
| 6 | census — Stance, read per passage <!--claim:2c0dc7198cf180a6b5f67b6f54324c16cc9f2a6e694146f1901243f9dd9d9df1--> | ; L181 to L226 a proposal headed „Konzept für das neue Master-Dokument: "Der Resonanz-Kodex"“ | L185 | ### **Konzept für das neue Master-Dokument: "Der Resonanz-Kodex"** |  | document | yes |
| 7 | census — Stance, read per passage <!--claim:ede8102b4da6feddebb2b3059e1f219ff812d19a97bee3bc7b75cfdedfbabd91--> | The close is labelled „Status: Abschlussbericht erstellt.“ | L238 | Status: Abschlussbericht erstellt. |  | document | yes |
| 8 | census — Stance, read per passage <!--claim:4c88c12deebd3fa385a2ca45bfcf6e65ff67b2e2a9b01f1a6ed5ff75f3873d09--> | and „Empfehlung: Sofortige Implementierung des Resonanz-Kodex zur Operationalisierung der Golden Sources.“ | L240 | Empfehlung: Sofortige Implementierung des Resonanz-Kodex zur Operationalisierung der |  | document | yes |
