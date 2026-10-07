---
drive_id: "github:openai/math@adc7f12/reasoning_traces/ordinary-two-point-correlations.pdf"
title: "OpenAI math — Reasoning summary: Ordinary two-point correlations of multiplicative functions"
slug: "openai-math-trace-ordinary-two-point-correlations"
category: "theorie-mathematik"
tier: "T2-theory"
index_date: "2026-10-06"
fetched: "2026-10-07"
---

Ordinarytwo-pointcorrelations 1
Summarized chain of thought (Ordinary two-point correlations of
| multiplicative | functions) |     |     |
| -------------- | ---------- | --- | --- |
OpenAI
Part I considers ordinary two-point correlations of bounded multiplicative functions under uniform
non-pretentiousness. PartIIconsidersaﬀineLiouvillecorrelations,withthestrongerquantitativetarget
of a logarithmic-power saving at every scale. Both arguments use weighted divisor graphs, but the
quantitativetargetrequiresadditionalcontrolofthelossesateachstage.
| Part I: Qualitative | corrected | Elliott correlations |     |
| ------------------- | --------- | -------------------- | --- |
Originalprompt(excerpts)
Let \(\mathbb N=\{1,2,\ldots\}\) and \(\mathbb D=\{z\in\mathbb C:|z|\le 1\}\). A function
| \(f:\mathbb | N\to\mathbb | D\) is multiplicative | if  |
| ----------- | ----------- | --------------------- | --- |
\[
| f(mn)=f(m)f(n)\qquad |     | ((m,n)=1). |     |
| -------------------- | --- | ---------- | --- |
\]
For a Dirichlet character \(\chi\), \(t\in\mathbb R\), and \(N\ge 2\), write
\[
| D(f,\chi | n^{it};N)^2 |     |     |
| -------- | ----------- | --- | --- |
=
| \sum_{p\le | N}  |     |     |
| ---------- | --- | --- | --- |
\frac{1-\operatorname{Re}\bigl(f(p)\overline{\chi(p)p^{it}}\bigr)}{p},
\]
where the sum is over primes \(p\), \(p^{it}=e^{it\log p}\), and \(D\) denotes the nonnegative
| square root. |     |     |     |
| ------------ | --- | --- | --- |
Say that \(f\) is uniformly non-pretentious if, for every fixed Dirichlet character \(\chi\),
\[
| \inf_{|t|\le         | N}D(f,\chi | n^{it};N)\to\infty |     |
| -------------------- | ---------- | ------------------ | --- |
| \qquad (N\to\infty). |            |                    |     |
\]
Conjecture / Open Problem: Binary corrected Elliott conjecture for ordinary averages.
Let \(f_1,f_2:\mathbb N\to\mathbb D\) be multiplicative functions. Suppose that at least one of
\(f_1,f_2\) is uniformly non-pretentious. Then for every fixed pair of distinct shifts
| \(h_1,h_2\in\mathbb |     | Z_{\ge 0}\), |     |
| ------------------- | --- | ------------ | --- |
\[
| \frac1N\sum_{n=1}^N  |     | f_1(n+h_1)f_2(n+h_2)=o(1) |     |
| -------------------- | --- | ------------------------- | --- |
| \qquad (N\to\infty). |     |                           |     |
\]
1 From the single-scale obstruction to weighted divisor graphs
Reading Klurman, Mangerel, and Teräväinen [6], the assistant matched the prompt’s uniform hypoth-
esis to Tao–Teräväinen’s cancellation outside exceptional scales [12]. It distinguished both that conclu-
sion and Tao’s logarithmically averaged theorem [13] from ordinary convergence at every scale. The
Liouvillespecializationalreadycontainedordinarytwo-pointChowla.

Ordinarytwo-pointcorrelations 2
Attempts to build counterexamples through prime phases encountered dense compatibility con-
straints. Proof proposals instead extracted prime divisors and encoded neighboring correlations in
arithmetic graphs. Their central diﬀiculty was removing sparse divisibility conditions without chang-
ing the scale. Comparable-size primes supplied insuﬀicient reciprocal mass; broader dilations mixed
differentscales. TheassistantexaminedTao’sentropydecrementargument[13],whoseindependence
estimate selects an unspecified scale, and compared its graph proposals with the prime-divisibility
expansionmethodofHelfgottandRadziwiłł[4].
The assistant next explored positive kernels combining a real scale with congruence information in fi-
nite adeles. Smoothing the real coordinate appeared promising, but the assistant found that restoring
thefinitecoordinatepreventeditfrominferringtherequiredcontinuity. Itconsideredtheequilibrium-
state classifications of Laca–Raeburn and Laca–Neshveyev [7, 8], but identified a missing tracial prop-
ertycloselyrelatedtothedesiredcancellation. Neshveyev’sadelicergodicitytheorem[10]suggesteda
dilation-invariant formulation; the assistant found that infinite measure blocked the simple invariant-
probability argument and that normality remained an extra assumption. It considered the mixing-
subalgebra framework of Cameron, Fang, and Mukherjee [2], while observing that normal mixing re-
sultsdidnotclassifythesingularkernelsitneeded. ItalsoinspectedTao–Teräväinen’squantitativecor-
relationtheorem[14]: thepermittedshiftsandmoduliweretoosmallforitsproposeddilationwindow.
Helfgott’s work on homogeneous polynomial parity and root numbers [5] suggested another direc-
tion. TheassistanttriedapolynomialsubstitutionpreservingLiouvillesigns,butitssparseimageleftit
withoutapositive-densityargument.
Returning to graphs, the attempt used Pilatte’s Improved bounds for the two-point logarithmic Chowla
conjecture as a model for centered divisibility operators [11]. Weighting squarefree divisors by 𝐴𝜔(𝑑)
produced the broad degree (1 + 𝐴)𝜔 𝑆 (𝑛), where 𝜔 counts prime factors from a selected set. With
𝑆
𝛽 = (1+𝐴)−1,centeringat𝛽2/𝑝appearedtoreduceexpansionlossesenoughfortheshortexponential-
sum estimates of Matomäki, Radziwiłł, and Tao [9] to help. It studied Pilatte’s fourth-moment uncen-
teringargumentandTao–Teräväinen’sextensionsofthedecouplingestimate[11,14]asmodelsforthis
step. Theassistantthenreturnedtotheestimatesneededforthisparameterchoice. Localizingdivisor
productstonarrowintervalsrequireduniformconcentrationalonglonggraphwalks;repeatedprimes
could retain too much dependence. It proposed smooth cutoffs and triangular divisibility constraints,
whilecontinuingtoaskhownonconsecutiveoccurrencesofaprimecouldsupplyenoughindependent
constraints. These localization and dependence questions guided the next stage of its weighted-graph
argument.
2 Preserving cancellation while auditing the divisor graph
The corrected Elliott attempt developed and then audited a weighted graph intended to prove ordi-
nary two-point cancellation for multiplicative functions of modulus at most one under the corrected
nonpretentiousnesshypothesis. TheassistantusedPilatte’sworkonlogarithmicChowlaformodelsof
triangulardivisibilityconstraints,prohibitedpaths,andcombinatorialsieves,theninvestigatedhowto
adaptthemtotheweightedgraph[11]. Theconditionalsievewasbasedonthecombinatorialsieveof
HelfgottandRadziwiłł[4].
Squarefree composite steps were restricted to a narrow interval near a scale 𝐻. Normalizing prime-
productweightsbyvertexdegreeschangedthecenteringrequiredtocancelprimesappearingonjustone
traceedge. Freshprimevariableswereintendedtoyieldareciprocallogarithmic-scalesavingperstep,
whiledivisor-countcutoffscompensatedstepslackingsuchvariables. Repeatedvertices,disconnected
primeoccurrences,andbranchingpathscomplicatedthiscalculation.

Ordinarytwo-pointcorrelations 3
VERBATIMEXCERPT
Singleton cancellation requires n residue for singleton primes approximate independent uniform when
no Y failure, even conditioned on repeated prime hits etc. Need upper bound for deviation.
Theassistantidentifiedafailureinitsreturn-edgeargument: boundingareturnfactorpointwiseandre-
movingitbeforesignedintegrationcoulddestroythecancellationneededelsewhere. Therepairretained
returnfactorsduringprimewiseintegration. Afurtherrevisionseparatedheavilyweighted,uncentered
coreprimes𝐶fromcenteredmarks𝑍,using
𝐷(𝑛) = 𝛽−𝜔 𝐶 (𝑛)2𝜔 𝑍 (𝑛), 𝛽 = (1+𝐴)−1.
Here𝜔 (𝑛)countsprimedivisorsfrom𝑆;markswerecenteredat1/(4𝑝),andcutoffsdependedonlyon
𝑆
coreprimes. Conditionalsieveexpansionsandtreedecompositionswereproposedtocontroldamaged
singletoncancellations,butexpandingthesievecoulditselfrestoreprohibitedpaths.
For the uncentering step, it examined Pilatte’s fourth Fourier moment estimate and its sieve input
fromFriedlanderandIwaniec’sOperadeCribro,thenproposedarough-numberanalogue[11,3].
The assistant then checked the parameters and the short exponential-sum theorem of Matomäki,
Radziwiłł,andTaoasaninputtoremovingthecenteringterms[9]. Theircorrectednonpretentiousness
condition requires the minimum pretentious distance over characters of bounded modulus and twists
|𝑡| ≤ 𝑋 to diverge for every fixed modulus bound. Excluding each fixed twist separately is insuﬀicient.
The assistant clarified this premise and organized the candidate proof around further checks of sieve
independence,traceenumeration,andtheproposedspectralestimate. Inrevisitingearlierapproaches,
the assistant retained Tao and Teräväinen’s almost-all-scales cancellation, presented as Theorem A by
Klurman,Mangerel,andTeräväinen,asabenchmarkthatstillallowedexceptionalscales[12,6]. Italso
recalledthequantitativecorrelationtheoremofTaoandTeräväinen: itsuniformpolylogarithmicrange
ofshiftsandmoduliwastooshortfortherationalconfigurationstheassistanthadconsidered[14].
3 A two-band graph and the corrected-Elliott conclusion
The corrected-Elliott attempt ends by refining its contradiction argument for a persistent ordinary cor-
relationofmultiplicativefunctionsofmodulusatmostone,withatleastoneuniformlynonpretentious.
The assistant continued its graph construction, sieve truncation, and uncentering argument from the
preceding sections. The refinement assigns distinct roles to two prime bands. Heavily weighted core
primespayfornarrowmultiplierintervalsandreturnstepsinclosedwalks;centerprimessupplysigned
cancellationthroughfactors1 −1/(4𝑝).
𝑝∣𝑛
A simplification replaces layered core bands by one narrow upper band. First visits in each closed
walk form a rooted tree. Connected prime-label subtrees receive weights whose sum is intended to
cancel the background normalization. Fresh core primes supply interval savings, while exceptional
residuecoincidencesrequireseparatecounting. Theargumentrepeatedlytestsrepeatededges,missing
centerfactors,shareddivisors,andinteractionsamongcutoffpenalties.
The assistant found no fatal contradiction in these tests, but continued to question how to preserve
singleton cancellation while conditioning on forbidden paths. The proposed repair uses truncated
inclusion–exclusion and triangular divisibility constraints, with factorial denominators retained when
summingunorderedprimeassignments.
The assistant used Pilatte’s Improved bounds for the two-point logarithmic Chowla conjecture [11] as a
model for high-trace estimates, prohibited progressions, and triangular constraints controlling the
combinatorial-sieveremainder. ForuncenteringitusedTheorem1.7ofMatomäki,Radziwiłł,andTao’s
An averaged form of Chowla’s conjecture [9], checking that finite-prime cutoff twists preserve the needed

Ordinarytwo-pointcorrelations 4
nonpretentiousness as the averaging scale tends to infinity. It combined this short-exponential-sum
input with rough-number sieve and fourth-moment bounds, taking the averaging limit before the
prime parameter grows. In the closing derivation it replaced an appeal to an upper-bound sieve by
truncated inclusion–exclusion estimates for one and two rough integers. The assistant concluded
that suﬀiciently small centered-graph and uncentering bounds would contradict the lower bound
transferredfromapersistentcorrelation.
The claimed cancellation depends on the conditional-integration, exceptional-pattern enumeration,
triangular-extraction, and short-interval estimates proposed along this route. In particular, the condi-
tionalsingleton-cancellationandsieve-remainderboundsareessentialtotheconclusion.
Part II: Quantitative aﬀine Chowla correlations
Originalprompt(excerpts)
Let λ(n)=(−1)^Ω(n), where Ω counts prime factors with multiplicity. Prove that an absolute c>0
exists such that, for every fixed pair of affine forms L_j(n)=a_jn+b_j with positive integers a_j,
nonnegative integers b_j, and a₁b₂−a₂b₁≠0,
|Σ_{n≤X}λ(L₁(n))λ(L₂(n))|≪_{a₁,a₂,b₁,b₂}X/(log X)^c
for all X≥3. The sum is unweighted and the estimate must hold at every scale.
4 A quantitative aﬀine Chowla attempt
Pilatte’s logarithmic Chowla work [11] suggested using many prime families. Pilatte attributed the
combinatorialsievetoHelfgottandRadziwiłł[4]. Theassistantexaminedrepeatedprimecoordinates
incompositestepsandthecomparisonbetweenfiniteintervalsandindependentresidues:
VERBATIMEXCERPT
Need exact cancellation singleton and nonnegative support of low-rank. Finite CRT prevents mixing
over P for cutoffs.
Here CRT means the Chinese remainder theorem. The combined residue modulus could exceed the
interval length. The assistant explored Braverman’s bounded-independence theorem for Boolean cir-
cuits [1] as a possible way to transfer independent-residue calculations to finite intervals. Applying it
wouldrequireasuitablecircuitencodingofthedeletionpredicatesandcontroloftheavailabledegree
ofindependence.
Atthecombinatorialturningpoint,theassistantsoughtcompatibledeletionwitnessesforeveryprime
labeloccurringonlyonce:
VERBATIMEXCERPT
Mixed difference property stronger than pairwise changes: if total mixed difference nonzero, expand
product over *all* potential witness exclusion booleans. Then at least one intersection of
witnesses in SAME hybrid covers ALL singleton labels; otherwise expansion cancels per term. hybrid
deterministic choice finite, no counting huge.
The proposed common-residue witness cover would supply triangular divisibility constraints, while
compressedcompositewalksneededanewlow-rankforestencoding. Theassistantcontinuedtoseeka
uniformencodingcostforrepeatedandomittedprimelabels.

Ordinarytwo-pointcorrelations 5
In examining Pilatte’s fourth-moment argument, the assistant encountered its classical sieve input
fromFriedlanderandIwaniec’sOperadeCribro[3]anditselementarymean-valueestimateattributedto
Tenenbaum [17]. Removing the centering terms prompted a proposed fourth Fourier moment bound
for rough-number weights and examination of short-interval Liouville estimates of Matomäki, Radzi-
wiłł, and Tao [9]. Cutoffs and deletion errors still threatened the saving. The assistant carried witness
compatibility, finite-interval transfer, and the combined parameter losses forward as estimates it still
neededtocontrol.
5 Closing the quantitative aﬀine Chowla argument
Theconstructionreducedaﬀineformstoafixed-shiftcorrelationrestrictedtoaresidueclass. Itcombined
products of primes from separated ranges with weighted squarefree padding and narrow logarithmic
intervals. A proposed nonbacktracking matrix prohibited consecutive repetition of the entire tuple of
centered primes. Its trace expansion separated configurations with many mean terms, high constraint
rank, or many singleton prime labels. The singleton case adapted Pilatte’s prohibited-sequence and
triangular-systemideas[11],usingjointlypresentwitnessesandtriangularcongruenceelimination;the
remainingpatternswereencodedasforests. Prime-countingestimatesinfixedresidueclasses,checked
againstTao’snotes[15],controlledtheprimesuppliesandpaddingdistribution.
For the finite-average comparison with independent residues, the assistant checked Braverman’s
bounded-independence theorem [1]. For removing the centering terms, it checked corrections to the
Matomäki–Radziwiłł–Tao short exponential-sum input [9]. It combined these inputs with proposed
fourth-moment estimates, a padding cutoff, and a spectral passage from the nonbacktracking matrix
to the centered adjacency sum. The literature check also consulted Tao’s discussion of his paper with
Teräväinen, Quantitative correlations and some problems on prime factors of consecutive integers [14, 16],
whichdistinguishedlogarithmicaveragingandalmost-all-scaleconclusionsfromtheall-scaletarget.
With𝛿 = 1/200,𝐿 = (log𝑋)1/𝐴 and𝐽 = ⌊𝛿log𝐿/(6𝑊)⌋,theassistantconcludedthatsuﬀicientlylarge
absoluteconstants𝐴,𝑊 madethenormalizedfixed-shiftcorrelation
𝐹(𝑋) = 𝑋−1 ∑ 1 𝜆(𝑛)𝜆(𝑛+ℎ)
𝑛≡𝑏 (mod𝑙)
𝑛≤𝑋
decaylike𝑒−𝐽. Here𝜂 = 𝑒−𝐽,𝐾 = 𝑒4𝐽,andℎ,𝑙arethefixedshiftandmodulus:
VERBATIMEXCERPT
With \(J,\eta,K\) as above the right side is \(O_{h,l,W}(e^{-J})\). Thus the desired exponent for
\(F\) can be \(c=\delta/(6WA)>0\), with no discarded scales.
Finally, the assistant returned to the aﬀine forms using 𝑙 = 𝑎 𝑎 , 𝑏 = min(𝑎 𝑏 ,𝑎 𝑏 ), and ℎ =
1 2 2 1 1 2
|𝑎 𝑏 −𝑎 𝑏 |. This reduction would give the all-scale aﬀine bound with an absolute positive exponent,
1 2 2 1
provided the proposed simultaneous-witness elimination, forest-counting, finite-residue comparison,
andspectral-transferboundsholdwiththestateduniformlosses.
References
[1] Mark Braverman. Polylogarithmic independence fools 𝐴𝐶0 circuits. Journal of the ACM 57(5) (2010),
28:1–28:10.https://doi.org/10.1145/1754399.1754401.

Ordinarytwo-pointcorrelations 6
[2] JanCameron,JunshengFang,andKunalMukherjee.MixingsubalgebrasoffinitevonNeumannalge-
bras.NewYorkJournalofMathematics19(2013),343–366.https://nyjm.albany.edu/j/2013/19-1
7.html.
[3] John Friedlander and Henryk Iwaniec. Opera de Cribro. American Mathematical Society, Collo-
quiumPublications57(2010).https://bookstore.ams.org/coll-57.
[4] Harald Andrés Helfgott and Maksym Radziwiłł. Expansion, divisibility and parity. arXiv preprint
arXiv:2103.06853v2(2021).https://arxiv.org/abs/2103.06853v2.
[5] Harald Andrés Helfgott. Root numbers and the parity problem. Ph.D. thesis, Princeton University
(2003).arXiv:math/0305435.https://arxiv.org/abs/math/0305435.
[6] Oleksiy Klurman, Alexander P. Mangerel, and Joni Teräväinen. On Elliott’s conjecture and applica-
tions. Proceedings of the London Mathematical Society 133(3) (2026), e70205. Preprint version:
arXiv:2304.05344v2(2023).https://doi.org/10.1112/plms.70205.
[7] MarceloLacaandIainRaeburn.PhasetransitionontheToeplitzalgebraoftheaﬀinesemigroupoverthe
naturalnumbers.AdvancesinMathematics225(2)(2010),643–688.https://doi.org/10.1016/j.ai
m.2010.03.007.
[8] Marcelo Laca and Sergey Neshveyev. Type III equilibrium states of the Toeplitz algebra of the aﬀine
1
semigroup over the natural numbers. Journal of Functional Analysis 261(1) (2011), 169–187. https:
//doi.org/10.1016/j.jfa.2011.03.009.
[9] Kaisa Matomäki, Maksym Radziwiłł, and Terence Tao. An averaged form of Chowla’s conjecture. Al-
gebra & Number Theory 9(9) (2015), 2167–2196. Corrected version: arXiv:1503.05121v3 (2022),
https://arxiv.org/abs/1503.05121v3.https://doi.org/10.2140/ant.2015.9.2167.
[10] SergeyNeshveyev.ErgodicityoftheactionofthepositiverationalsonthegroupoffiniteadelesandtheBost-
Connesphasetransitiontheorem.ProceedingsoftheAmericanMathematicalSociety130(10)(2002),
2999–3003.https://doi.org/10.1090/S0002-9939-02-06449-3.
[11] Cédric Pilatte. Improved bounds for the two-point logarithmic Chowla conjecture. Journal of the
American Mathematical Society (2026). Published online 10 September 2026. Cited version:
arXiv:2310.19357v3,https://arxiv.org/abs/2310.19357v3.https://doi.org/10.1090/jams/1084.
[12] Terence Tao and Joni Teräväinen. The structure of correlations of multiplicative functions at almost all
scales,withapplicationstotheChowlaandElliottconjectures.Algebra&NumberTheory13(9)(2019),
2103–2150.https://doi.org/10.2140/ant.2019.13.2103.
[13] TerenceTao.ThelogarithmicallyaveragedChowlaandElliottconjecturesfortwo-pointcorrelations.Forum
ofMathematics,Pi4(2016),e8.https://doi.org/10.1017/fmp.2016.6.
[14] Terence Tao and Joni Teräväinen. Quantitative correlations and some problems on prime factors of con-
secutiveintegers.arXivpreprintarXiv:2512.01739v2(2026).Firstversion2025.https://arxiv.org/
abs/2512.01739v2.
[15] Terence Tao. 254A, Notes 2: Complex-analytic multiplicative number theory. Lecture notes on What’s
new(2014).9December2014.https://terrytao.wordpress.com/2014/12/09/254a-notes-2-compl
ex-analytic-multiplicative-number-theory/.
[16] Terence Tao. Quantitative correlations and some problems on prime factors of consecutive integers. Blog
post on What’s new (2025). 1 December 2025; discussion of the joint paper with Joni Teräväinen.
https://terrytao.wordpress.com/2025/12/01/quantitative-correlations-and-some-problems-o
n-prime-factors-of-consecutive-integers/.

Ordinarytwo-pointcorrelations 7
[17] GéraldTenenbaum.Introductiontoanalyticandprobabilisticnumbertheory.AmericanMathematical
Society,GraduateStudiesinMathematics163(2015).Thirdedition;translatedbyPatrickD.F.Ion.
https://www.ams.org/books/gsm/163/.
