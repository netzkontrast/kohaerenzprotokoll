# Claims — every cited sentence beside its line

Fill the last two columns of every row and save the file as `claims.md` beside this one. `python3 scripts/claims.py check <slug>` fails on an empty cell. Read the lines: `python3 scripts/read.py <slug> --from N --to N`, several in one call.

- **who says it** — `document`, or `source: <who>` when the line reports another source;
- **holds?** — `yes`, or `fixed` after you changed the sentence.

| # | where | your sentence, up to its citation | line | its opening words | cues in the line | who says it | holds? |
|---|---|---|---|---|---|---|---|
| 1 | note — 1 · What kind of text this is, and how i <!--claim:34064ddd4104b29e20a795522ad98234e0a96486d02ce5a05d01cb4fdab53e42--> | - **Observed:** the document is organised as numbered parts, among them „Medizinisch-diagnostische Fundierung“ | L29 | ## **II. Medizinisch-diagnostische Fundierung: kPTBS, DIS und Komorbiditäten |  | document | yes |
| 2 | note — 1 · What kind of text this is, and how i <!--claim:bbe919f412bd3c3b52b14917695bd5b3775bbf0d4d0a030a9b07e00a01692eda--> | and „Prozessuale Handlungsempfehlungen“ | L348 | ## **V. Prozessuale Handlungsempfehlungen** |  | document | yes |
| 3 | note — 1 · What kind of text this is, and how i <!--claim:6fe3a0a47e096c8d5fad8ef303562346eaebdb7527583dfaa089c68bd88e19bc--> | ; it ends with a list headed „Referenzen“ | L420 | #### **Referenzen** |  | document | yes |
| 4 | census — Stance, read per passage <!--claim:b5354ceeadc63223c0e6d1de547c3efc284d200059d41afe3ff2aead59be386a--> | The whole document is a legal strategy memo in the register of a report and a plan: it is organised as numbered parts, among them „Medizinisch-diagnostische Fundierung“ | L29 | ## **II. Medizinisch-diagnostische Fundierung: kPTBS, DIS und Komorbiditäten |  | document | yes |
| 5 | census — Stance, read per passage <!--claim:a59fe5b5426d180835eff836793baeaf81b33c1fed8d13ab403149f8c8485367--> | , „Juristische Bewertung des GdB und der Merkzeichen nach VMV und SGB IX“ | L124 | ## **III. Juristische Bewertung des GdB und der |  | document | yes |
| 6 | census — Stance, read per passage <!--claim:bbe919f412bd3c3b52b14917695bd5b3775bbf0d4d0a030a9b07e00a01692eda--> | and „Prozessuale Handlungsempfehlungen“ | L348 | ## **V. Prozessuale Handlungsempfehlungen** |  | document | yes |
