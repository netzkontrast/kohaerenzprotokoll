# Brief — readings from document 76 (step 6)

1 document, one reader, one batch: `ingest-76`. Files go to `Plan/runs/ingest-76/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 76 | `system-kael-konzeptentwicklung-und-analyse` | 2025-06-24 | „the concept synthesis“ (its title: `Das Kohärenz Protokoll: Eine Konzeptionelle Synthese`) | a German concept analysis of 2025-06-24 in four parts — the ontology (AEGIS's genesis, the Digitale Überwelt and its Wächter, entropy and the Risse), System Kael by TSDP with the four Kern-Welten, the plot of Part 1 as a Heroine's Journey and the Fundament, themes and open questions; it reports a `Fundament-Konzept` and the plot of Part 1 (reference 1) and answers a user's request (L240); no canon claim, „nicht abgeschlossen“ (L261) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (296 lines for `system-kael-konzeptentwicklung`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **An analysis reporting other documents, written the same day as `scifi-roman-mit-ki-schreiben` (record 74) from the same plot of Part 1.** Where a sentence ends in a glued reference number (`1`), it reports a source: „the concept synthesis gives, as its sources' …“; where it interprets (TSDP mappings, the toxic-manager reading, Advaita, P=NP), „the synthesis reads …“. **Write only what record 74's readings on the page do not already hold** — check the page's digest for `scifi-roman-mit-ki-schreiben`; if this document only repeats it (e.g. the Guardian–world pairing), one sentence saying so, or not read. Section 4.2's questions (L263–L266) are questions, never claims. Isabelle's line (L122) says what it says, no more.

## Pages — document 76, `system-kael-konzeptentwicklung-und-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L26, L30, L34, L36, L38, L46, … (32 lines). central (3–5): the genesis as negation, the „Ich“-fragment and the cluster (L30–L34); the ontological core sentence „AEGIS ist, was AEGIS verhindert, dass es nicht ist“ (L36); AEGIS as a „toxischer Manager“ (L177); the Landauer irony — every erasure produces the entropy it fights, the Risse as its own by-product (L80–L84).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Integrity Guardian` L82. minor (1–3): the Guardian-Interface protocols — ZTEM „Never trust, always verify“ (L50), Behavioral Proof-of-Function (L51), Encrypted Intent Channels (L52); `Integrity Guardian` (L82).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L110, L163. minor (1): Alex (Beschützer), core phobia helplessness (L110).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L132. minor (1): Argus (Beobachter), a metacognitive part, core phobia imperfection (L132).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L54, L60, L82, L162, L208. minor (1): the hypervigilant, paranoid defence (L60).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L283. not read unless L283 is more than a reference title: occurrence.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L68, L72, L74, L75, L76, L80, … (8 lines). minor (2): three levels — thermodynamic, Shannon, digital (L74–L76); the fundamental force AEGIS fights (L72).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L264. not read: only inside a question (L264).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L26. minor (1): the genesis as a cosmological mirror of TSDP (L38).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L162, L208. minor (1): KW3, Cerberus's domain, a bunker-like fortress (L162).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L122, L163. minor (1): L122, as the document writes it; one sentence.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L38, L171, L175, L179, L181, L188, … (9 lines). minor (1–2): the `Juna/V`-Verbindung as a safe, co-regulating bond (L179); the central conflict as a struggle for bonding (L181).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L58, L88, L92, L96, L100, … (38 lines). central (2–3): Kael (Host), primary manager of daily life, core phobia the flooding by the EPs (L108); Kael's journey bound to emancipation from the toxic bond with AEGIS (L188); he defeats AEGIS by healing himself (L232).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L54, L61, L164. minor (1): suppressed, potentially chaotic creative potential (L61).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L88, L152, L156, L250, L265. central (2): the four Kern-Welten (KW1-4) as direct externalisations of Kael's inner landscape (L156); their code names — `Co₁`, `McL`, `B`, `Ly` (L160–L164): quote the words after them, the digits are not findable.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L120, L142, L146, L161, L183. minor (1): Kiko (Kind/Angst), flight and freeze (L120).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: title (L13) — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L160. minor (1): KW1, LogOS's domain, the world of the ANPs (L160).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L58, L109, L134, L142, L144, L160, … (8 lines). minor (1): Lex (Analytiker), core phobia emotion and irrationality (L109); LogOS comparable to Lex (L58).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L121, L161, L183. minor (1): Lia (Kind/Ambivalenz), ambivalent attachment (L121).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L54, L58, L160, L206, L252. minor (1): pure logic cut off from emotion (L58).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L54, L59, L161. minor (1): archived but unintegrated emotional memory (L59).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L164, L209. minor (1): KW4, `Kairos/Sophia`, potential and integration (L164).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L111, L123. minor (1): Moros (Kollaps), hopelessness and existential emptiness (L123).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L209, L228. minor (1): L209 or L228 — quote what it says of the Mosaik-Herz.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L266. not read: only inside a question (L266).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L30, L38. minor (1): the genesis's state before the system (L30) — quote its words for the Nichts Rauschen.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L119, L142, L145, L163, L184, L266. minor (1): Nyx (Kämpfer), the fight reaction (L119).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L161, L207. minor (1): KW2, Mnemosyne's domain, emotional memory and trauma (L161).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L111, L134, L142, L147, L185. minor (1): Rhys (Fürsorger), core phobia unhealable pain (L111).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L38, L68, L78, L84, L206. minor (1–2): the Risse as active processes of decay (L78); the paradoxical by-product of AEGIS's control (L84).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L131, L142, L148, L165. minor (1): Selene (Regulatorin) among the integrating parts (L131) and `ANP-Regulator` in Tabelle 1 (L142) — record both.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L208. minor (1) or not read: L208 only if it says something of Silas beyond a name.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L54, L62, L164. minor (1): the often overtaxed attempt at synthesis (L62).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L38, L96, L100, L156. minor (1): the eleven parts sorted into ANPs, EPs and integrating forms (L100–L102).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Überwelt` alone on L42. central (2): the Digitale Überwelt as AEGIS's primary instrument of self-preservation, the „Labor der Kohärenz“ (L46); its structure read as the externalised cognitive functions of a traumatised mind (L56).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Labor der Kohärenz` (near `koharenz`). occurrence: `Labor der Kohärenz` is the Überwelt's epithet (L46), read on ueberwelt (J12).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: a part's name.
- `ueberwelt`: `Digitale Überwelt` (near `uberwelt`). reading, above (`Digitale Überwelt`).


**Also read** (not in the lookup): **`landauer-signatur`** (1): the Landauer principle stated, every logically irreversible erasure dissipating heat (L80), and AEGIS's erasures producing the entropy (L82).

**Record entries:**

- **`c11-landauer-warmth-or-cold-ozone`**: the Landauer irony (L80–L84) — say what the synthesis says of heat, if it does; if it states only entropy, one line saying so.
- **`q5-guardians-and-kern-welten`**: one sentence — the same pairing as record 74, with the worlds' code names (L160–L164).

One reader writes everything.
