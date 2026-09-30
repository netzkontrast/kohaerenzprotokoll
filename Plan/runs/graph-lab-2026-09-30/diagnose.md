# Diagnosis — why a case misses a page, on the stated graph

A miss is one of three, and only one of them is a weight: **no seed** (the question names no page's surface, so nothing walks), **unreachable** (no path along the walked relation types from any seed to the page: no weights can bring it), or **outranked** (reached, and eight other terms rank above it).

| case | gold | hit | no seed | unreachable | outranked | (page: hops, rank among terms) |
|---|---|---|---|---|---|---|
| conflict:C1 | 1 | 1 | | 0 | 0 |  |
| conflict:C10 | 2 | 0 | 2 | | | the question names no page's surface |
| conflict:C11 | 5 | 3 | | 0 | 2 | oblivion: 2, 19; silas: 2, 14 |
| conflict:C12 | 1 | 1 | | 0 | 0 |  |
| conflict:C13 | 1 | 1 | | 0 | 0 |  |
| conflict:C14 | 1 | 1 | | 0 | 0 |  |
| conflict:C15 | 4 | 3 | | 0 | 1 | lia: 1, 9 |
| conflict:C2 | 1 | 1 | | 0 | 0 |  |
| conflict:C3 | 2 | 2 | | 0 | 0 |  |
| conflict:C4 | 9 | 4 | | 0 | 5 | blinder-fleck: 1, 20; cerberus: 1, 9; kairos: 1, 14; logos: 1, 11; sophia: 1, 15 |
| conflict:C5 | 5 | 2 | | 0 | 3 | kairos: 1, 13; realitaetsebenen: 1, 40; sophia: 1, 15 |
| conflict:C6 | 7 | 3 | | 0 | 4 | cerberus: 1, 11; kairos: 1, 15; logos: 1, 13; sophia: 1, 17 |
| conflict:C7 | 1 | 1 | | 0 | 0 |  |
| conflict:C8 | 1 | 1 | | 0 | 0 |  |
| conflict:C9 | 2 | 2 | | 0 | 0 |  |
| question:Q1 | 11 | 2 | | 0 | 9 | cerberus: 1, 13; grenzfeste: 1, 33; kairos: 1, 21; konstrukt-stadt: 1, 19; logos: 1, 17; mnemosyne: 1, 10; moeglichkeits-garten: 1, 15; resonanz-landschaft: 1, 44; sophia: 1, 23 |
| question:Q2 | 7 | 0 | 7 | | | the question names no page's surface |
| question:Q3 | 8 | 2 | | 0 | 6 | did: 1, 26; grenzfeste: 1, 29; konstrukt-stadt: 1, 11; moeglichkeits-garten: 1, 10; realitaetsebenen: 1, 50; resonanz-landschaft: 1, 36 |
| question:Q4 | 5 | 3 | | 0 | 2 | grenzfeste: 1, 45; personas: 2, 86 |
| question:Q5 | 7 | 3 | | 0 | 4 | cerberus: 1, 12; kairos: 1, 16; logos: 1, 14; sophia: 1, 17 |
| question:Q6 | 6 | 5 | | 0 | 1 | verschraenkungs-insel: 1, 22 |
| question:Q7 | 2 | 2 | | 0 | 0 |  |
| question:Q8 | 4 | 3 | | 0 | 1 | algorithmische-melancholie: 1, 38 |
| question:Q9 | 3 | 3 | | 0 | 0 |  |

**96 gold pages over 24 cases:** 49 hit, 38 outranked, 0 unreachable, 9 no seed.

Weights can move the *outranked*; the *unreachable* and *no seed* need a relation or a surface the graph does not have — which is what an alias list, a co-occurrence relation or a contract that extracts term relations would add.
