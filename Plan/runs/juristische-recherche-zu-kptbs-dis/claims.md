# Claims — every cited sentence beside its line

Fill the last two columns of every row and save the file as `claims.md` beside this one. `python3 scripts/claims.py check <slug>` fails on an empty cell. Read the lines: `python3 scripts/read.py <slug> --from N --to N`, several in one call.

- **who says it** — `document`, or `source: <who>` when the line reports another source;
- **holds?** — `yes`, or `fixed` after you changed the sentence.

| # | where | your sentence, up to its citation | line | its opening words | cues in the line | who says it | holds? |
|---|---|---|---|---|---|---|---|
| 1 | note — 1 · What kind of text this is, and how i <!--claim:574b73587a50703286ad549b9cd89d98a74205dfea0714b1a8a8f1951e7847de--> | - It is headed „Juristische Analyse der Begutachtung komplexer Traumafolgestörungen im deutschen Sozialrecht“ | L11 | **Juristische Analyse der Begutachtung komplexer Traumafolgestörungen im deutschen |  | document | yes |
| 2 | note — 1 · What kind of text this is, and how i <!--claim:c2132545f638ee01778b1a43218dcd32e1e9ee72def0cf17ce66cb2b2878554e--> | TL;DR (Management Summary / Kernaussagen)“ | L13 | **I. TL;DR (Management Summary / Kernaussagen)** |  | document | yes |
| 3 | census — Stance, read per passage <!--claim:477c8154ee84bd5ec53d923b5f341b31127267da9a1e72d277ef735e40313297--> | The document is a research report on the social-law assessment of real diagnoses; it is headed „Juristische Analyse der Begutachtung komplexer Traumafolgestörungen im deutschen Sozialrecht“ | L11 | **Juristische Analyse der Begutachtung komplexer Traumafolgestörungen im deutschen |  | document | yes |
| 4 | census — Stance, read per passage <!--claim:c2132545f638ee01778b1a43218dcd32e1e9ee72def0cf17ce66cb2b2878554e--> | TL;DR (Management Summary / Kernaussagen)“ | L13 | **I. TL;DR (Management Summary / Kernaussagen)** |  | document | yes |
| 5 | census — Stance, read per passage <!--claim:c91f729f2131ccf9b1d1c80d6028380ba2c30b55c6b8cd1444073cad36efaf02--> | , a discussion of a first research stage, then answers to numbered research questions such as „II.A.1.a Welche allgemeinen Anforderungen stellt die Rechtsprechung“ | L106 | - II.A.1.a Welche allgemeinen Anforderungen stellt die Rechtsprechung |  | document | yes |
| 6 | census — What the extraction ran into <!--claim:1c7407549f0a11e35a91977ab75e653e4fa3b1f046da339e54668c35e290760d--> | The export shows markup artifacts: list-break comments such as „<!-- end list -->“ | L34 | <!-- end list --> |  | document | yes |
| 7 | census — What the extraction ran into <!--claim:f3b185096da89f256e2e32c8ed582c9286d22c64ddf17f2ee4f960ecf260c899--> | , a table whose cells carry escaped asterisks (L50 to L56), glued reference numbers after words (51 in the profile), and source-list entries marked „CAPTCHA, kein Inhalt“ | L558 | - 72 LSG NRW L 13 SB 364/21 |  | document | yes |
| 8 | census — What the extraction ran into <!--claim:468b7178cb0cd18debdccd98a4daa68c968103e223c50c84344588799f544bd4--> | or „Identisch mit“ | L368 | - 72 LSG Nordrhein-Westfalen, Urteil vom 04.10.2023 - |  | document | yes |
