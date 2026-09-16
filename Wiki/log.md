# Wiki log

[Up](index.md)

Append-only record of every operation on the research wiki. One line per
operation, grammar from `schema/conventions.yaml`:

```
## [YYYY-MM-DD] <op> | <title> | skill=<command or program> | sha256=<hash when a page was written>
```

Ops: `ingest`, `promote`, `understand`, `question`, `clarify`, `tetraframe`,
`query`, `lint`, `health`, `claim`. Read the tail with
`grep "^## \[" Wiki/log.md | tail -20`. Never rewrite a line; a correction is a
new line.

## [2026-09-16] health | wiki skeleton rendered, zero pages | skill=scripts/render_wiki_views.py

## [2026-09-16] health | navigation and page-boundary contract audited | skill=scripts/render_wiki_views.py

## [2026-09-16] health | context routing and maintenance skill audited | skill=wiki-maintenance
## [2026-09-16] ingest | AEGIS | skill=/research-ingest | sha256=0249e053b6909aeeaed684a926622e25331bf58340648a50669d1edc292149b5

## [2026-09-16] ingest | Die 13 Alter (System Kael) | skill=/research-ingest | sha256=b2b92bc06a01045c6d6e58f47b6823474a4d44f1208a341f3d747da0645c115f

## [2026-09-16] ingest | Die Guardians | skill=/research-ingest | sha256=564d9794999ef938d2542af36991faeee144cd932b1c0cfb3f03e260f8f21d90

## [2026-09-16] ingest | Juna/V | skill=/research-ingest | sha256=692058f5cccf0c34c1f23d68dab2653931cd53a2109b2b6ffc9f10a5e77ca835

## [2026-09-16] ingest | Kael / System Kael | skill=/research-ingest | sha256=ef25287fc852d3dff3fc4790bf331d6a4b32bb2061bb472b155b3e36308f3ec2

## [2026-09-16] ingest | Kiko | skill=/research-ingest | sha256=9aa6388ec241c8966cce78e34926705a5b515bbbf5b8086d4eba86ea78a77a00

## [2026-09-16] ingest | Lex | skill=/research-ingest | sha256=d55fa7787d0ae13d2eaf5d0a806ffedf12b7cc9be85e05025c5d7d5845242341

## [2026-09-16] ingest | Nyx | skill=/research-ingest | sha256=4d138eedf2ec12e7f861dc75e17a00825846be7b06360b8bd6f6dc4e157a1613

## [2026-09-16] ingest | Manager-Anteile & unzuverlässige Erzählung | skill=/research-ingest | sha256=01aaba4acae0e3eaa589755c9c497126a29a1bba55f2b6468d84c21bf42eaaeb

## [2026-09-16] ingest | Witness-Funktion | skill=/research-ingest | sha256=575b01282e513ae0dc0825f652961102080d320bdf1f6783ff4b79cdc5407650

## [2026-09-16] ingest | Genesis-Krise | skill=/research-ingest | sha256=8b143b5806450eb7d22413db673b737a2e6e8314b3f286d6518e581d5bc67c2e

## [2026-09-16] ingest | Risse als dialetheische Wahrheiten | skill=/research-ingest | sha256=1e48feed335ba0e4fa4420e50f3a946fa06fb01c89f508940509dfdcfa76ee70

## [2026-09-16] ingest | Telefon-Stille | skill=/research-ingest | sha256=4a973b44e0522322cefec3f83faed224b901f4efc569106c42ab3f9312fed369

## [2026-09-16] ingest | 39-Kapitel-Matrix | skill=/research-ingest | sha256=24d475669413c1f0efcb9fec12657d45329d817f395aa3d57a5b127c393336da

## [2026-09-16] ingest | Atemporalität / nicht-lineare Erzählzeit | skill=/research-ingest | sha256=3cb6d47c986d05fd4a5bbc23ee71c9ccd844bb7dcaa06215a9fd68e5c8168368

## [2026-09-16] ingest | Funktionale Multiplizität | skill=/research-ingest | sha256=68afff670f27a406f235bd936735e5dffa47ec8c17246d39dac46be76398d4f1

## [2026-09-16] ingest | Hard Canon Protokoll (Konsolidierung) | skill=/research-ingest | sha256=1ec284a4fbac067b7b04a84134194343b2306df031cd9e0866cba8760caa0beb

## [2026-09-16] ingest | Hard Sci-Fi als Computational Constraint | skill=/research-ingest | sha256=7868fec785b1cb8cd98a0dde3bed34805753201c3a1f56aeed0fd5bbda634f3e

## [2026-09-16] ingest | Paradoxon X | skill=/research-ingest | sha256=6662215b22c0ca3cd4aead7b9b335a46fd9b91aabb8812770b3023e0cb159a84

## [2026-09-16] ingest | Per-Chapter Dual POV | skill=/research-ingest | sha256=43aa53545826d3eacf5aa55fe99e8717f4ef081d7bbbb212875d878bcc5923b9

## [2026-09-16] ingest | Call to Wholeness | skill=/research-ingest | sha256=fe0cc641115215b00de1769019a87f2fbc29e363c641b32a0315909041e300d4

## [2026-09-16] ingest | Dual-Storyform | skill=/research-ingest | sha256=06784a7404d138d86a800a6e89cc1dee698d8ddf4c88ab1ccc6ef7cc52532da8

## [2026-09-16] ingest | Ouroboros-Klammer | skill=/research-ingest | sha256=5a815fe4e2e96c18bbc130af7a9eeba37d8578b5fc5aa5b41aef3f4c09e969e3

## [2026-09-16] ingest | Victory Through Wholeness | skill=/research-ingest | sha256=92b2b75d7679f3b9f592023fb0b1d2c55b51144f7766b9438365429cc9a14be9

## [2026-09-16] ingest | Living Gödel-Satz & die 6 Paraiyas | skill=/research-ingest | sha256=51c6131cf19c0d0e086bcbd21edac3772432393d8e1fd08fe9ec55cfa9825544

## [2026-09-16] ingest | Algorithmische Melancholie | skill=/research-ingest | sha256=0e7b155f61b53094f42ba20e3805309753a95b4f09fbc16d8d10b5cf147a12b0

## [2026-09-16] ingest | ANP/EP-Struktur | skill=/research-ingest | sha256=b6a4d7c94d3aa284d1a51d0921bc9242d86353a4b43dcc5d6ffd0419dada21a0

## [2026-09-16] ingest | Autopoiesis | skill=/research-ingest | sha256=036dab2c415fb24b8941bd425d972e272c9576f7a99cb72c0a0a3539a1344038

## [2026-09-16] ingest | Dialetheismus & Paraconsistent Logic | skill=/research-ingest | sha256=9234b233b4b5de655376dce383bf5724485fd1167edba918a2e0f28df87e97ff

## [2026-09-16] ingest | Dual-Kernel-Theorie (K0/K1) | skill=/research-ingest | sha256=0c7dd9ee0cec2059c21047c4967cb7d5e63f68f8220b006a71e413bbcc162927

## [2026-09-16] ingest | Gnosis vs. Episteme | skill=/research-ingest | sha256=fecff60d41c591eee10fa5e3cdd6dfae12fdc8a8113e739f11011878a449fb34

## [2026-09-16] ingest | Internal Family Systems (IFS) Modell | skill=/research-ingest | sha256=9c53fd5889a3eb644592e12e22b2f7d1d62ffea9ed459e1a66549f6b099efed9

## [2026-09-16] ingest | Moonshine-Link | skill=/research-ingest | sha256=991ebbf6623cb4ffee4b7ae57236386e7e46157ae240f77bbecf60d976fddda2

## [2026-09-16] ingest | Mutual Information als Liebe | skill=/research-ingest | sha256=469ba606aef018272181b06f3fd10cc25a05dc52a9729515c8f2e60b211ae246

## [2026-09-16] ingest | Reader as Substrate | skill=/research-ingest | sha256=0adf07a57700c6b589433cd18ccf9ad5d363edcfac0347736117440b6831bd76

## [2026-09-16] ingest | TSDP – Theorie der strukturellen Dissoziation | skill=/research-ingest | sha256=346854d6c8883e8fe13a7378f4374d1d6c45e97f305aa7133e0b7a193a1a9e25

## [2026-09-16] ingest | Kohärenz- vs. Korrespondenztheorie der Wahrheit | skill=/research-ingest | sha256=cc0741260893916a3ccc0357ac2e69b3f7dcffcdc1cc4fcdfb26962831e8cc8d

## [2026-09-16] ingest | Externe Ebene: Köln 2026 | skill=/research-ingest | sha256=1a4bdee8cc2277fac6ffd8d0bfe4cf8772a42bc8e559be25733c3fec67cf095d

## [2026-09-16] ingest | Die Kernwelten (KW1–KW4) | skill=/research-ingest | sha256=3f354f5d6931d3bcb20a8138c7fcce36c651d6590db6b4383b1f49a13d23f129

## [2026-09-16] ingest | Potentialmeer / Nichts-Rauschen | skill=/research-ingest | sha256=6ab2314dfae8f831dcc64f01d0bd667de67fb0289d34c56054f9bfffb15dcf51

## [2026-09-16] ingest | The Foundation / Strange Attractor | skill=/research-ingest | sha256=bb11a13534856c206dcb0e158c241d3ae57dc398a5c1790679c4e65343a755e6

## [2026-09-16] ingest | Konsolidierung des Hard Canon Protokolls | skill=/research-ingest | sha256=17ca45afa62ba742e18188de08431ccbdeac20d2f9a82e46a650869e6e0b2a9e

## [2026-09-16] ingest | Reader's Report: A Critical Assessment of "Kohärenz Protokoll" | skill=/research-ingest | sha256=4f6cdb110d3de94ce210becfe23508bea1176193276ebd408fb2afe3b942076a

## [2026-09-16] ingest | Report: Reorienting the Central Conflict as a "Call to Wholeness" | skill=/research-ingest | sha256=65ac7b33394dc58738e15b9e5ffba8d109b62ddab4feecad78b8a7942f771399

## [2026-09-16] ingest | Technical Audit & Research Mandate: The Kohärenz-Protokoll Framework | skill=/research-ingest | sha256=91b135899b28f51d51c20514f2a59cd46b4a7812d7d7797bd707e3431b18cb01
