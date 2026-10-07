---
drive_id: "github:openai/math@adc7f12/reasoning_traces/symmetric-and-general-mahler-conjectures.pdf"
title: "OpenAI math — Reasoning summary: Symmetric and general Mahler conjectures"
slug: "openai-math-trace-symmetric-and-general-mahler-conjectures"
category: "theorie-mathematik"
tier: "T2-theory"
index_date: "2026-10-06"
fetched: "2026-10-07"
---

GeometricMahlerconjectures 1
| Summarized |     | chain |     | of thought |     | (Symmetric | and general | Mahler |
| ---------- | --- | ----- | --- | ---------- | --- | ---------- | ----------- | ------ |
conjectures)
OpenAI
These three attempts address complementary parts of the Mahler problem. Part I concerns the sharp
symmetriclowerbound. PartIItakesthatboundasasuppliedpremiseandseekstheHannerequality
classification;itssuppliedpremiseandcandidatereasoningarenotidentifiedwiththeparticularproof
in Part I. Part III develops a separate general-body argument for the simplex bound and its equality
cases, rather than deriving it from the symmetric attempts. The three parts retain separate arguments
andhypotheses.
| Part I: The | symmetric |     | lower | bound |     |     |     |     |
| ----------- | --------- | --- | ----- | ----- | --- | --- | --- | --- |
Originalprompt(excerpts)
# Problem
For an integer $n\ge4$, let $K\subset\mathbb R^n$ be a compact convex set with nonempty interior,
| with $K=-K$ | and | $0$ | in its | interior. | Define | its polar by |     |     |
| ----------- | --- | --- | ------ | --------- | ------ | ------------ | --- | --- |
$$
K^\circ=\{y\in\mathbb R^n:\langle x,y\rangle\le1\text{ for every }x\in K\},
| \qquad | \langle | x,y\rangle=\sum_{i=1}^n |     |     | x_i | y_i. |     |     |
| ------ | ------- | ----------------------- | --- | --- | --- | ---- | --- | --- |
$$
Writing $\operatorname{vol}_n$ for $n$-dimensional Lebesgue volume, is it true that
$$
\operatorname{vol}_n(K)\operatorname{vol}_n(K^\circ)\ge\frac{4^n}{n!}
$$
| for every  | $n\ge4$ | and  | every   | such      | $K$? |       |     |     |
| ---------- | ------- | ---- | ------- | --------- | ---- | ----- | --- | --- |
| 1 Boundary |         | laws | and the | symmetric |      | bound |     |     |
The symmetric attempt begins by recalling the three-dimensional result of Iriyeh–Shibata, Meyer’s un-
conditional argument, and the lower bounds of Bourgain–Milman, Kuperberg, and Nazarov [36, 46,
15, 39, 49]. It tries section induction, face flags, equal-measure cone partitions, entropy, and tensoriza-
tion, but finds no sharp constant along these routes. In the polytope approach, it invokes Stanley’s
lowerboundfortheℎ-vectorofcentrallysymmetricsimplicialpolytopes,butstillneedsaboundforthe
associated volume fractions [62]. It revisits Kuperberg’s neck construction and Berndtsson’s complex-
integralproof,examinesNazarov’sBergman-kernelapproach,andconsidersKlartag’srelationbetween
isotropicconstantsandMahlervolumes[39,9,49,38].
Lundin’s extremal-function formula and the Baran metric lead it toward planar boundary laws and
| complexifiedslabs[44,5,6]. |     |     |     | Itchooses |     |     |     |     |
| -------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- |
𝜁𝑘
8
|     |     |     |     |     | 𝑓(𝜁) | = ∑ | ,   |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- |
|     |     |     |     |     |      | 𝜋2  | 𝑘2  |     |
𝑘≥1,𝑘odd
whoseboundaryrealpartisatrianglewave,henceuniformlydistributedon[−1,1]. Foreachrowbasis
ofaslabpresentationof𝐾,itdefinesafeasibilityprobability𝑃 usingindependentboundaryvalues.
𝐼

GeometricMahlerconjectures 2
It uses powers of the inverse conformal map, positivity of the complex Hessian of a logarithmic po-
tential, Stokes’ theorem, and a homogeneous flux calculation to derive ∑ 𝑃 ≥ 1. For the opposite
𝐼 𝐼
𝐾∘, 𝑛!|𝐾||𝐾∘|/4𝑛.
inequality, it associates feasible bases with disjoint simplices in obtaining ∑ 𝑃 ≤ It
𝐼 𝐼
repeatedly checks normalization, genericity, boundary ties, and Hanner examples, then presents the
argumentwithapproximationfromslabpolytopestoarbitrarysymmetricbodies.
| Part II: | Equality | and | Hanner |     | polytopes |     |     |     |
| -------- | -------- | --- | ------ | --- | --------- | --- | --- | --- |
Originalprompt(excerpts)
| # Symmetric |     | Mahler–Hanner: |     | remaining | equality |     | classification |     |
| ----------- | --- | -------------- | --- | --------- | -------- | --- | -------------- | --- |
Let \(|\cdot|\) denote Lebesgue measure in \(\mathbb{R}^n\), and let \(\langle\cdot,\cdot\rangle\)
be the standard inner product. A convex body in \(\mathbb{R}^n\) is a compact convex set with
| nonempty | interior. |     | Write |     |     |     |     |     |
| -------- | --------- | --- | ----- | --- | --- | --- | --- | --- |
\[
\mathcal K_0^n=\{K\subset\mathbb{R}^n: K\text{ is a convex body and }K=-K\}.
\]
| For \(K\in\mathcal |     |     | K_0^n\), | define | its polar | body | by  |     |
| ------------------ | --- | --- | -------- | ------ | --------- | ---- | --- | --- |
\[
K^\circ=\{y\in\mathbb{R}^n:\langle x,y\rangle\le 1\text{ for all }x\in K\},
\]
| and its | volume | product |     | by  |     |     |     |     |
| ------- | ------ | ------- | --- | --- | --- | --- | --- | --- |
\[
P(K)=|K|\,|K^\circ|.
\]
For convex bodies \(K\subset E\) and \(L\subset F\) in finite-dimensional real vector spaces,
| define | their | \(\ell_\infty\)- |     | and | \(\ell_1\)-sums |     | in \(E\oplus | F\) by |
| ------ | ----- | ---------------- | --- | --- | --------------- | --- | ------------ | ------ |
\[
| K\oplus_\infty |     | L=K\times |     | L,  |     |     |     |     |
| -------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
\qquad
K\oplus_1 L=\operatorname{conv}\bigl((K\times\{0\})\cup(\{0\}\times L)\bigr).
\]
The class of Hanner polytopes is the smallest class of origin-symmetric convex polytopes containing
all origin-symmetric line segments and closed under \(\oplus_\infty\) and \(\oplus_1\).
Open problem: For every integer n >= 4 and every origin-symmetric convex body K in \(\mathcal
| K_0^n\), | prove | or  | disprove | that |     |     |     |     |
| -------- | ----- | --- | -------- | ---- | --- | --- | --- | --- |
\[
P(K)=\frac{4^n}{n!}
\quad\Longleftrightarrow\quad
K\text{ is linearly equivalent to an }n\text{-dimensional Hanner polytope}.
\]
A negative answer must give a mathematically valid counterexample to this equivalence. A positive
| answer   | must     | establish | it  | in every | dimension | n   | >= 4. |     |
| -------- | -------- | --------- | --- | -------- | --------- | --- | ----- | --- |
| 2 A lens | argument |           | for | Hanner   | equality  |     |       |     |
Theattempttakesapreviouslysuppliedsharpsymmetriclowerboundasapremiseandreconstructsan
earliercandidateargumentfortheequalitycase. Thatargumentincludesalensconstructionandroutes
fromitsequalityconditionstothethree-ballintersectionproperty.
ItfirstchecksthatpolarityinterchangesthetwoHannersumsandthateithersumindimensions𝑘,𝑙

GeometricMahlerconjectures 3
𝑘+𝑙
hasvolumeproduct𝑃(𝐴)𝑃(𝐵)/( ). InductionfromsegmentsthereforegivestheHannerdirection.
𝑘
Fortheconverse,theassistantstudiestheanalyticmap
8 (−1)𝑗𝑧2𝑗+1
𝐹(𝑧) = ∑ .
𝜋2 (2𝑗+1)2
𝑗≥0
ItchecksconvexityofitsinnerimagecurvesthroughthepositivityofRe(1+𝑧𝐹″/𝐹′). Thelimitingbound-
ary has branches ±𝜆(𝑡)+𝑖𝑡, with uniform height under uniform phase and 𝜆″(𝑡) = −sec(𝜋𝑡/2). For
spanning real rows it forms a sum 𝑆(𝑟) of basis-feasibility probabilities. Splitting a smoothed complex
Hessiandeterminantintominorscontainingaconstantrowandthoseomittingit,itderivesmonotonic-
ity: thelattertermsdecreasewith𝑟,integrationbypartsmakestotalcutoff-massdifferencestendtozero,
and the former terms converge to feasibility probabilities. It checks extra-row ties through a rank-two
phasemapandusesdominatedconvergenceatthecircleandlensendpoints.
Theassistantobtainsthecirclevalue𝑆(0+) = 1byrandomizingsquaredradiiexponentially,integrat-
ingcomplexGaussians, andapplyingCauchy–Binet. It also considersa deterministicexplanation, but
findsphasechoicesforwhichtwobasesarefeasiblesimultaneously:
VERBATIMEXCERPT
Then some phase none to balance. Thus no deterministic. Laplace solution concise.
Atthelensendpoint,theassistantboundsthetotalvolumeofthedisjointfeasiblesimplicesbythevol-
ume of the polar body. Integrating over the original body yields the symmetric lower bound 𝑃(𝐾) ≥
4𝑛/𝑛!. Itthenexaminestheequalityconditions.
For an equality body the assistant lifts to 𝐾 ⊕ [−1,1], whose polar is 𝑄×[−1,1], where 𝑄 = 𝐾∘. It
1
usesinscribedproductapproximationsandvanishingintegratedmissingvolumetoextractcost-optimal
representations with minimum total mass. The asymptotic 𝜆(1 − 𝜂) = (2/𝜋)𝜂log(1/𝜂) + 𝑂(𝜂) turns
thosecostsintoaﬀineexpressions. Comparingtworepresentationsandseparatingtheircompactconvex
aggregate set yields, in its reconstruction, a metric median for any three points in the norm with unit
ball 𝑄. Moving such a median toward a center whose ball misses it gives a common point of three
pairwise-intersectingballs.
The earlier candidate argument also discusses a facial route using Lima’s intersection characteriza-
tion[43]; theassistantchoosesthemedianrouteandchecksthereal, finite-dimensionalhypothesesof
Hansen–Lima’sstructuretheorem, particularlyCorollary7.4[35]. Itconcludesthat𝑄isaniteratedℓ -
1
andℓ -sumofsegmentsandappliespolaritytoconcludethestatedclassificationfor𝐾.
∞
Part III: General convex bodies
Originalprompt(excerpts)
# Problem
For an integer $n\ge2$, a convex body $K\subset\mathbb R^n$ is a compact convex set with nonempty
interior $\operatorname{int}K$. Write $|A|$ for the $n$-dimensional Lebesgue volume of a measurable
set $A\subset\mathbb R^n$ and $\langle x,y\rangle=\sum_{j=1}^n x_jy_j$ for the Euclidean inner
product.
For $z\in\operatorname{int}K$, define
$$

GeometricMahlerconjectures 4
(K-z)^\circ=\{y\in\mathbb R^n:\langle y,x-z\rangle\le1\text{ for every }x\in K\},
\qquad
P(K)=\inf_{z\in\operatorname{int}K}|K|\,|(K-z)^\circ|.
$$
The infimum is attained at a unique interior point, called the Santaló point. A simplex is the
convex hull of $n+1$ points $v_0,\ldots,v_n\in\mathbb R^n$ for which $v_1-v_0,\ldots,v_n-v_0$ are
linearly independent.
Resolve the conjecture that, for every integer $n\ge2$ and every convex body $K\subset\mathbb R^n$,
$$
P(K)\ge\frac{(n+1)^{n+1}}{(n!)^2},
$$
with equality if and only if $K$ is a simplex. The quantifier includes arbitrary convex bodies; no
central symmetry, smoothness, or polytope assumption is imposed.
3 Conic reformulation and the first failed reductions
Theassistantfirstconsideredwhethertensorpowerscouldturnanasymptoticallysharpboundintothe
simplexconstant,comparingthispossibilitywithKuperberg’ssymmetriclowerbound[39]. Ithomog-
enizedthebodyintoaconeofdimension𝑑 = 𝑛+1,andrewrotethetargetas
𝜒 (𝑣)𝜒 (𝑢) ≥ 1, 𝜒 (𝑣) = ∫ 𝑒−⟨𝑣,𝑥⟩𝑑𝑥, ⟨𝑢,𝑣⟩ = 𝑑.
𝐶 𝐶∗ 𝐶
𝐶
Theorthantsuppliedtheequalitymodel. Klartag’slogarithmicLaplaceformulation[38]ledittocovari-
ancerestrictionsatprojectiveminima. Itthennoticedthatsmoothbodiescouldhaveinteriorprojective
minima,defeatingitshoped-foruniversaltraceestimate.
Triangulations expressed the two integrals through determinants of slack matrices. Matching oppo-
site face flags gave equality for the orthant. The assistant then found that fine approximations to a
smoothedsimplexcouldmakethematchedsumsmall: long,nearlyflatprimalpiecescorrespondedto
tinydualpieces. Atransportbuiltfromexponentialquantilesencounteredanotherobstruction. Redun-
dantgeneratorschangedtheauxiliaryCauchy–Schwarzboundwithoutchangingthecone. Theassistant
abandonedthisestimateandexaminedcomplementarysubspaces,Galetransforms,andazonoidcom-
parison. Althoughthezonoidtheorem[55]suggestedaroutethroughprojectionsofcubes,itsproposed
determinantcomparisonlosttoomuchonroundcones. Italsoconsideredthereflection-symmetrythe-
oremofBartheandFradelizi[7],butobservedthatpermutationsofmultidimensionalblockswerenot
hyperplanereflections.
Induction over tangent cones produced a sum of ratios between the body’s volume and truncated
tangent-conevolumes. Inthesimple-polytopecase,theassistantrecognizeditsreformulation:
VERBATIMEXCERPT
So tangent inequality for simple B exactly Mahler. Any B can approximate simple. Not progress
unless geometry helps.
ItnextcomparedthedeficitsindirectandreverseBrascamp–Liebinequalities,developingBarthe’strans-
portargument[8]intodeterminantandheat-flowformulas. Separateboundsonthetwointegralsdid
not give it the required bound on their product. Dirichlet representations likewise concentrated too
stronglyatthecenterofroundsections.
The assistant returned to a maximal-simplex position, recalling local minimality at the simplex [37],
and placed the cone above the positive orthant. It tried to connect the resulting lower sets with the
entropy identity for anti-blocking corners [22]. Saint-Raymond’s inequality and Meyer’s coordinate-
induction method [59, 46] then suggested repeated-coordinate lifts of a convex corner. The primal

GeometricMahlerconjectures 5
weightedintegralapproachedthedesiredconeintegral,butthedualweightsconcentratedatonepoint
of the exposed face. The assistant ended by asking whether varying the replication proportions could
recoverthewholedualsection.
4 Localization losses and stationary incidence measures
Theassistantcontinuedtryingtotransferanti-blockinginequalitiestotheconictarget𝜒 (𝑣)𝜒 (𝑢) ≥ 1.
𝐶 𝐶∗
Repeatingnearlyradialcoordinatesledittoincompatiblescales: broadprimalfluctuationssampledthe
tangentcone,whilethedualintegralconcentratednearonepointofitssection𝐵. Aftercomputingthe
twoasymptotics,itwrote:
VERBATIMEXCERPT
Need |B| factor, not obtained.
It also tested translated corners, power transformations, and permutation chambers. Consulting
Artstein-Avidan, Sadovsky, and Sanyal’s treatment of anti-blocking bodies relative to cones, it found
definitions and decompositions but no direct bound for its proposed reduction [1]. Tensor amplifi-
cation was another possibility: a suﬀiciently strong volume comparison could magnify a deficit until
it contradicted a reverse Santaló bound. The assistant found determinant losses in its column-slicing
estimateandquestionedwhethertensoringpreservedtherequiredcenters,whilekeepingKuperberg’s
boundasapossiblecomparison[39].
NextitusedtheprojectivecovarianceconditionsassociatedwithKlartag’sapproach[38]. Normaliz-
ingonecovariancetotheidentityplacedtwoconesectionsinsideaunitball. Theassistantinvestigated
whetheranexponentialmarginalatacontactpointwouldforcearayfactorandpermitinduction. First
variations then led it to propose vertex–facet incidence measures with facet centroids as conditional
means, cross-moment identities, and a stochastic matrix with eigenvalues 1,−1/𝑛,0. It found that its
determinantestimatelosttoomuchtoreachthetarget.
Section–projection induction brought a different obstruction: simplex sections chosen by a natural
partition could have the wrong Santaló center. The assistant insteadconsidered unequal orthant parti-
tions and tracked their section and projection weights. It also developed an entropy projection onto a
subsetoftheprobabilitysimplex,thennoticedthatprojectingexteriorpointsontoboundaryfacesmade
theproposedchangeofvariablesdegenerate.
ReadingChen,Li,Xi,andXu’sshadow-flowargumentanditsuseofMeyer–Reisnerpolar-volumecon-
vexity[19,47],theassistanttriedtoextendthecountofadmissiblevertexspeeds. Higher-dimensional
incidencecounts,includingthe24-cell,ledittoreconsideruniversaleliminationbydeformation:
VERBATIMEXCERPT
Need lower bound for rigid cases, not classification.
Itreturnedtostationaryincidencemeasures,interpretingthemthroughrandomfacettriangulations
andrandomchoicesofanapex. Theseconstructionssuppliedfurthercovarianceanddeterminantiden-
tities. Itthentriedtoextendvertex–facettransporttocompletedualfaceflagsandnoticedthatartificial
facesintroducedbytriangulationhadnocorrespondingdualfaces.
5 Barycentric coupling and the covariance gap
Theassistantrewrotetheface-flagestimateasavolumefactortimestheaﬀinityoftwoflagdistributions.
Itobservedthatvertex–facetstationaritydidnotspecifytransitionsthroughintermediatefaces. Return-
ingtothecovariancecomparisonassociatedwithKlartag’sprojectivevariations[38],itset𝑧 = 𝑥⋅𝑦 for

GeometricMahlerconjectures 6
independent cone-boundary points and 𝑟 = 𝑞(𝑥) ⋅ 𝑝(𝑦) for their normalized normals. Boundary inte-
grationgave𝔼[𝑟𝑧] = 1/𝑛; the desiredestimatewas𝔼[𝑧2] ≤ 1/𝑛. Abarycentricconstructionproduced
another variable with the law of 𝑟 and conditional mean 𝑧, but the assistant rejected a deduction from
scalarconvexorderalone:
VERBATIMEXCERPT
So no scalar alone. Need coupling constraints relating r and r' and z conditional facets.
It then proposed replacing vertices by small clusters and separating two convex sets of incidence mea-
surestoobtainone couplingsatisfyingbothbarycentricrequirements. Itexplicitlydistinguishedunre-
stricted minimization from minimization with a fixed vertex count, and worked through approximate-
contactconstraints,limitingderivatives,andmeasurableselectionforacontinuumextension.
With that coupling assumed, the assistant examined reversible incidence walks, added-vertex mo-
mentbounds,andconditionaldeterminant–entropyestimatesobtainedfromBarthe’sreverseBrascamp–
Liebinequality[8]. Itfoundlossesforroundedfacets. Meyer–Reisnershadowsystems[47]motivated
attempts to flatten vertices, replace bodies by pyramids, or use perspective sections; the assistant kept
encountering changes in facet structure or constants below its target. A proposed common-random-
vector factorization failed its regular-simplex test. Tangent degenerations led to reciprocal slack mo-
ments,whiletheassistantnotedthatJensen’sinequalityhadtheoppositedirectionfromtheestimateit
wanted.
Further tests used regular polygons, the Birkhoff polytope, the 24-cell, and sections of positive-
semidefinite cones. The assistant combined the zero-curvature condition for minimizers [56] with its
proposed coupling to investigate supporting faces of positive dimension. It also considered pruning
long vertices using Paouris’s concentration bound [51], and using local simplex stability [37] to
separate geometries near the simplex. Tensor amplification invoked the exponential lower bound
of Bourgain–Milman [15]. Symmetric suspensions and difference bodies brought in Kuperberg’s
linking-integral bound and Rogers–Shephard’s inequality [39, 57]; the assistant calculated that the
suspension comparison still lost an exponential factor on the simplex. It considered reflection-group
lifts [7] and revisited the anti-blocking arguments of Saint-Raymond and Meyer [59, 46], tracking the
opposingconcentrationeffectsofcoordinatereplication.
The incidence coupling next yielded an oblique projection on functions of contact pairs: its kernel
was 𝑛𝑞⋅𝑝′, and the complementary stochastic kernel was 1−𝑞⋅𝑝′. The assistant identified a relation
betweenasimplexprojectionandasimplexsection. ItexploredaconnectionwithBall’sreverseisoperi-
metric argument [2], then tried Dirichlet barycenters with concentration invariant under replication.
The concentration giving the uniform simplex was too large for the ball model. Finally, it expressed
the covariance comparison through conditional-expectation operators and a Hilbert–Schmidt inequal-
ity,observingthattheremaininginnerproducthadnosignsuppliedbytheprecedingidentities.
6 Symmetric lifts and the negative contact graph
Theassistantexpressedtheincidencecouplingthroughaconditional-expectationoperator𝑆andanon-
negativeslackkernel𝐿. Itobtained𝐾 = 𝑆𝐿𝑆,withzerodiagonalandprescribedeigenvaluesfor𝐿𝑆,then
testedthedesiredHilbert–Schmidtcomparison. Forapermutationcoupling,itfoundthatthecompar-
ison required an additional symmetry. Nonlinear weighted-centroid maps had derivative −𝑛𝐶 ; their
𝑌
compositionsuggestedextrafixedpoints,buttheassistantcouldnotconnectthosepointstoadecrease
involumeproduct. Italsodevelopedaseparationargumentforsimultaneousbarycentrictransporton
contactpairsandrevisitedtheprojectivecovarianceconditionfromKlartag’swork[38].
Thenextcalculationssoughttoamplifycone-volumeboundsthroughtensorpowersandsymmetric

GeometricMahlerconjectures 7
lifts. TheassistantrevisitedreverseBrascamp–Liebtransport,anti-blockingcorners,andshadowvaria-
tions[8,59,46,1,47,19]. ItexaminedKuperberg’spositiveandnegativecontactgraphsandbottleneck
construction[39, 40]. Forasymmetricbodies, thenegativegraphentered 𝐾 ×(−𝐾∘), andfittingit into
𝐾×𝐾∘ introducedsignorvolumelosses. Orderintervals,differencebodies,andpermutation-invariant
liftsweretestedagainstthesimplex. Inconsideringreflectionsymmetries[7],itfoundthatpermutations
ofwholevectorblocksdidnotprovidethescalarreflectionsitwanted.
Zonoids offered another route through their volume-product inequality; the assistant recalled
Gordon–Meyer–Reisner’s proof while remaining uncertain about its method [31]. The assistant
identified a natural zonoid with a normalized projection body, but noticed that Zhang’s reverse
Petty inequality gave the opposite direction from the estimate it needed [67]. It realized arbitrary
polyhedralconesastangentconesatzonotopeverticesandvariedgeneratorsprojectivelywhilekeeping
denominatorsfixed. Theattemptedinductionthenreturnedtotheoriginalconeproblem:
VERBATIMEXCERPT
Realize proving global minima for projective zonoid by reducing to boundary leads tangent arbitrary
unknown, no induction.
Theassistantnextpairedthepositivesubgradientgraphof𝑔 = 𝑝2/2withaflatnegativegraphover
𝐾
𝐾∩(−𝐾∘). Itcalculatedequalityinthenormalizedregular-simplexmodel,butdidnotestablishageneral
comparison.
Thisledittoseekaconvex,degree-twocontrolpotentialsatisfying
ℎ (−∇𝜓(𝑥)) = 𝑝 (𝑥),
𝐾 𝐾
sothatthenegativegradientgraphwouldlieintherequiredpolarproduct.
VERBATIMEXCERPT
This is promising universal negative conical graph with no shrinking, unlike Kuperberg.
Itexaminedoptimal-control,subgradient,Legendre-duality,andHamiltoniandescriptionsofthisequa-
tion,andsoughtalowerboundforthejointhroughmixedHessiandeterminants. AcomplexGaussian
contouridentitysuggestedretainingoscillatorycancellationinsteadofdiscardingit. Thereasoningthen
turnedtothespecialcase𝐾 = −𝐾∘ andtoself-dualcones.
7 Negative-contact tests and stochastic entropy methods
Theassistanttestedacovariancetraceboundforcenterednegativelyself-polarbodies, againstthepro-
jectivecovarianceconditionsinKlartag’sapproach[38]. Itssphericalexpansiongaveapositivesecond-
orderchangefordegree-threeharmonics. Itthereforerejecteditsexpectedsign,whileleavingrealization
ofthesmoothcenteredperturbationsasafurtherquestion.
Returning to Kuperberg’s linking-integral approach [39], it studied the eikonal potential 𝜓, with
ℎ (−∇𝜓) = 𝑝 , and a mixed-Hessian integral intended to bound the volume product. A Gaussian
𝐾 𝐾
changeofvariablesleftadeterminantintegralthatitfoundtoosmallforasimplexandpotentiallyzero
for symmetric polytopes. Expanding 𝜓 near the ball suggested evenness through third order. It then
derived a polygonal compatibility condition that it thought would fail generically, and sought an ex-
plicitpolygontotestit. ChangingthecomplexcontourcorrectedtheGaussianweightbutalsochanged
the determinant statistic; its simplex calculation gave an exponential gap between the two statistics. It
alsocomparedthegraph-volumelosswithaRogers–Shepharddifference-bodyestimateinthesimplex
case[57].

GeometricMahlerconjectures 8
Theassistantnextconsultedtransport–entropyformulationsofinverseSantalóinequalities[32,26]and
rederivedatargetinvolvingdifferentialentropiesandmaximalscorecorrelation. Fordensitiespropor-
tionalto𝑒−𝑉 and𝑒−𝑊,itsought
ℎ(𝑋)+ℎ(𝑌)+sup𝔼 [∇𝑉(𝑋)⋅∇𝑊(𝑌)] ≥ 3𝑑.
𝜋
𝜋
One-dimensional slicing introduced an infimum over profiles whose integral it could not control
sharply. Gaussianobservationsproducedscoremartingaleswithincrementmatrices𝐼 −𝑡Cov(𝑋 ∣ 𝑍 ).
𝑡
Reparametrizing their paths appeared to give a constant larger than the target, until it noticed an
endpointproblem:
VERBATIMEXCERPT
That would even stronger than Mahler (contradiction extremal). Issue endpoints r∞ random unequal,
can't align log scales pathwise causally. Explore.
Its matrix version likewise exhausted one eigendirection before accounting for the full entropy end-
point.
Afterconsideringentropictransport,theassistantreturnedtocoordinatecouplings.
Opposite triangular transports canceled the unwanted terms for Gaussian laws, but left cross terms
of uncontrolled sign for general densities. It revisited Barthe’s transport proof of reverse Brascamp–
Lieb[8],findingthattheseparatedirectandreverseestimatesstilldidnotcomparetherequiredproduct.
Further stochastic calculations used conditional entropy, covariance, and third moments in a Bellman
candidate. Allowingadaptiveobservationspeedsandeithersignofinnovationcorrelationledittothe
scalarfeasibilitycondition|1−𝐺 𝐺 | ≥ 𝐷 𝐷 whenbothsquaredquantities𝐷2,𝐷2 werenonnegative.
𝑋 𝑌 𝑋 𝑌 𝑋 𝑌
8 Gaussian regularization and failed tensor amplification
The assistant found that its scalar stochastic-localization controls did not settle the terminal compari-
son: conditioninganexponentiallawreducedentropy,keepingtheproposedstoppingratioaboveone.
Replacingconditionalentropybythemaximumentropyatthecurrentmeanrepairedthescalarexpres-
sion,butradialobservationspreservedtheproblematicratioandleftangularinformationunresolved. It
consideredPoissonobservationsandentropymonotonicityonupperconvexsets,usingBerwald’smo-
mentinequalityandquestioningwhetherCaffarelli’scontractionprinciplegavetheneededdirectionof
comparison[12,17].
ItthenintroducedthecenteredGaussianbarrier
𝐹 (𝑎) = maxlog∫ exp(−𝑎⋅𝑥− 1 (𝑥−𝑚)𝑇𝑄(𝑥−𝑚)) 𝑑𝑥.
𝑄 𝑚 𝐶 2
The optimizing center was the posterior mean. Differentiation gave an inflated covariance Hessian,
(Σ−1 −𝑄)−1, suggesting that an integrated covariance comparison might replace the sharp slicing es-
timate associated with Klartag’s approach [38]. Unrestricted minimization let the scales escape; fixed
metrics also made the balanced orthant a maximum along some opposing coordinate variations. The
assistant therefore optimized over mutually inverse metrics. A strengthened Poincaré calculation gave
itacovariancecorrectionandaderivationofgeodesicconcavity. Itusedthisconcavitytoarguethatthe
optimizedprofiletensorizedforconeproducts.
DifferentiatingthroughthemetricoptimumintroducedaninverseHessiancorrectioninvolvingthird
andfourthmoments. Half-linecomputationsmatchedthedesiredorthantprofile:

GeometricMahlerconjectures 9
VERBATIMEXCERPT
Exact equality E=p/r all scalar (due scaling invariance).
The assistant sought a corresponding matrix or trace estimate, developed an inductive boundary-
degeneration argument, and explored Ehrhard’s inequality [24]. It found that the resulting bounds
and repeated Bochner estimates were too weak, particularly when covariance was small. It connected
themissingestimatetosharpthird-momentboundsandcontinuedtestingpossiblescalarextremizers.
Returning to amplification, it observed that direct cone products preserved the normalized deficit.
Projective tensor cones offered a different construction, but ellipsoid estimates based on reverse
Brascamp–Lieb [8] did not control the injective dual with the required constants. The assistant then
reconsidered symmetry and zonoid comparisons [39, 7, 55], noting that permutations of multidimen-
sionalblockswerenothyperplanereflections. Itrevisitedentropyandanti-blockinglifts[22,1,59,46].
Repeated coordinate constraints could retain a fixed neighborhood and so failed to force the desired
amplification. Localizing coordinate induction near a vertex, meanwhile, lost the matching dual
projections;theassistantlookedforadditionalcoordinatesthatwouldpreservethem.
9 Tensor circuits and configuration bodies
The assistant applied simplicial matrices along tensor-array coordinates, obtaining determinant sums
with the desired repeated volume factors. It then found that convexifying the circuit outputs allowed
adaptive conditional distributions whose volume lost the intended amplification. Arbitrary diagonal
weights also broke positivity between paired primal and dual circuits. This prevented its proposed
applicationoftheBourgain–Milmanboundtothecircuitsets[15].
Itnextsoughtastationarydistributionforpositiveslack-matrixdynamics,hopingtocomparebranch
entropywithlogarithmicdeterminants. Theassistantidentifiedthemissingabsolutecontinuityassump-
tion:
VERBATIMEXCERPT
Need avoid circularity (ac impossible if α<1).
Unnecessarysubdivisionofasimplexalreadymadeitsproposedstationary-lawargumentfailatequal-
ity. Tensor arrays gave independent inputs to individual fibers and bounded scalar moments, but the
assistant could not infer a lower bound on joint entropy. It considered entropy-power estimates for
convexmeasures[13],whileobservingthatmixturesafteracircuitlayerneednotremainlog-concave.
Thenextconstructionfixedthesumofconepoints:
𝑆 = {(𝑥 ,…,𝑥 ) ∈ 𝐶𝑚 ∶ ∑ 𝑥 = 𝑚𝑢}.
𝑚 1 𝑚 𝑖 𝑖
After translation to the zero-sum subspace, the assistant described its polar as a projection of a trun-
catedproductofdualcones. ItusedtheRogers–Shephardprojection–sectioninequality[58]tobound
the projection loss polynomially in 𝑚, with the cone dimension fixed. Decomposing the points among
generatingraysexpressed𝑆 asaunionofMinkowskisumsofalignedsimplices. Optimizingoverthis
𝑚
finite-dimensionalfamilyledittoseekanasymptoticMahlerestimateforthosesums.
The assistant compared generator-length variations with Reisner’s zonoid argument and Meyer–
Reisner shadow systems [55, 47]. Entropy optimization showed why independent exponential
lifts were too concentrated for diffuse generators; correlated lifts were needed. Direct and reverse
Brascamp–Liebcomparisons[8]againlefttheproductoftheirtwofactorsuncontrolled. Returningtoa
functionalshadowformulation,itrecognizedthesamerestrictiononmovingvertices:

GeometricMahlerconjectures 10
VERBATIMEXCERPT
To move a vertex maintaining existing facets, need shadow admissibility across nonsimplicial facets
as in Mahler. Fat obstruction dimension d≥5. Functional formulation not escaping.
Binary splitting produced centrally symmetric fibers, prompting comparisons with Kuperberg’s
boundandSaint-Raymond’sunconditionalinequality[39,59];theassistantfoundthatitspairedfibers
were not polars. A subsequent basis-entropy formulation related facet densities to basis-inclusion
probabilities. ItconsideredrandomboxsectionsandVaaler’scube-sectiontheorem[65],butnotedthe
differencebetweencentralsectionsandthesectionsthroughavertexarisinghere. Finally, exponential
tilts of Cartesian powers gave it the covariance condition (𝑛 + 1)(𝑛 + 2)Cov Cov ⪰ 𝐼 at the
𝐾 𝐾∘
corresponding formal minimum; it observed that the improvement over its earlier condition became
smallinhighdimension.
10 Exponential face decompositions and complex analysis
Theassistantdecomposedanexponentialconelawbysubtractingtheminimumnormalizedslack. The
minimumhadanexponentialdistributionindependentoftheboundaryresidual:
VERBATIMEXCERPT
Exactly memoryless along v! Because all s_i v=1 and D+t v. Great.
Itfirstcoupledthefacetlabeltoatriangulation,thenchoseafullapextriangulationseparatelyforeachla-
beltoremoveinformationloss. Lower-dimensionalinductionreduceditsentropycomparisontobound-
ingaverageprojectionlossesbytheentropyofthefacetprobabilities. Itrecognizedthatthiscomparison
returned to the original Mahler inequality. Conditional facet hazards gave a reversible graph identity;
threshold variations suggested bounds on vertex degrees, but it noticed that changing triangulations
produced upward kinks. Deleting a vertex instead related the degree to the volume of the removed
corner.
The assistant next represented points by exponentially filtered trajectories of a Markov chain on
vertices. The simplex produced the uniform law. Covariance calculations supported a conditional-
barycenter identity, but higher moments introduced resolvents for which it could not justify that
identity. Centroid bounds gave transition rates at least one along every edge. It also tried Lawrence’s
vertex-volume formula, where it encountered cancellation between signed terms [41]. Revisiting the
shadow-flow arguments of Chen, Li, Xi, and Xu and Meyer–Reisner, it returned to the diﬀiculty of
deformingnonsimpleminimizers[19,47].
TurningtoNazarov’scomplex-analyticapproach[49],theassistantproposed
𝐽 (𝑣) = ∫ 𝑒−(𝑝+1)𝑣⋅𝑥𝜒 (𝑥)−𝑝𝑑𝑥.
𝑝 𝐶∗
𝐶
An orthant-sharp upper bound for these moments would recover the desired inequality as 𝑝 → ∞. It
testedconvolutionandderivativearguments;asquare-conecalculationgaveanegativethirdderivative,
contradicting its proposed higher-derivative positivity. In the inverse-polar moment calculation, it ap-
pliedBerwald’snormalized-momentcomparisontoaconcavegeometricmean,butfoundthattreating
dualcellsseparatelylosttheirsharedconstraint[12]. FouriersectionsandVaaler’scube-sectioninequal-
ityledittoseekasharperdependenceonthegeneratingdirections[65].
The assistant then tried Hardy-space functions built from facet denominators and found excessive
concentrationforroundcones. Herglotzrepresentationsledittoacomplexmomentbody𝐵 (𝑢),retain-
𝐶
ingsimultaneousdecompositionsof𝑢intoconevectors. UsingthemultidimensionalSuitacomparison

GeometricMahlerconjectures 11
asastartingpoint[50],itsoughtthetwobounds
𝜒 (𝑢)2|𝐵 (𝑢)| ≥ 𝜋𝑑, |𝐵 (𝑢)| ≤ 𝜋𝑑𝜒 (𝑣)2.
𝐶∗ 𝐶 𝐶 𝐶
Its comparisons revisited Kuperberg’s bound, Reisner’s zonoids, Barthe–Fradelizi symmetries,
Saint-Raymond’s inequality, and Barthe’s reverse Brascamp–Lieb theorem [39, 55, 7, 59, 8], along-
side Klartag’s covariance formulation [38]. Higher-rank moment bodies reduced to determinant
optimization,promptingtheassistant’sassessment:
VERBATIMEXCERPT
Mahler target becomes compare χ products to m_B/m ratios (taut).
ItnextconsideredLaplaceoperatorsandGurvits’scapacityinequalities[34]. Returningtoslackmatri-
ces,itobservedthatpermanentestimatesdidnotdirectlycontrolthesigneddeterminantsinthevolume
formulas.
11 Complex transport and weighted zonotope bounds
The assistant sought an upper volume bound for the complex moment body 𝐵(𝐶,𝑢) = {∑ 𝑥 ℎ ∶ 𝑥 ∈
𝑗 𝑗 𝑗 𝑗
𝐶, ∑ 𝑥 = 𝑢, |ℎ | ≤ 1}. It compared this problem with Gurvits’s capacity inequalities, higher-order
𝑗 𝑗 𝑗
difference bodies, and Barthe’s transport proof of reverse Brascamp–Lieb [34, 60, 8]. On a simplicial
piece, transporting each disk to a positive quadrant gave the desired Jacobian estimate; the assistant
couldnotmaketheimagesfromdifferentbasesdisjointorcontroltheregionswhereseveralbasestied.
Holomorphicdiskmapsreproducedthescalarcalculation,buttheirfirstderivativealonelostaconstant
andaglobalchoiceofholomorphicliftsremainedmissing.
It next adapted the Kuperberg–Berndtsson contour argument [39, 9] to the complementarity graph
Γ = {(𝑥,𝑦) ∈ 𝐶×𝐶∗ ∶ 𝑥⋅𝑦 = 0}. Pairing this graph with a positive linear graph gave an orthant-exact
lowerboundinvolvinganintersectionconeanddeterminantsondualfaces. Summingtwocomplemen-
taritygraphskeptbothoutputsintheirconesbutintroducedmultiplicity. Theassistanttriedrank-one
penaltiesanddifferentcomplexphases,findingthatdiscardingtheoscillatorytermsstilllosttheorthant
constant.
In parallel, it considered Vaaler’s section theorem [65] and a toric formulation: one cone integral
became the volume of a Reinhardt domain, while the other became a fraction of integrable monomi-
als. It compared this formulation with the multiplicity–log-canonical-threshold inequality and strong
openness[25,33]. Itrejectedunrestrictedsubadditivitybysplittingasimplexintopieces, thenconsid-
eredrestrictedsubdivisions,polynomialmaps,andBergmantraces. AprojectedCauchy-to-exponential
transportalsofaileditsproposedpointwiseJacobiantest,firstneartheaxisforsymmetricexamplesand
thenalongatwo-leveldirectionofasquarecone.
The assistant formed an overlap kernel with Cauchy marginals in dual-cone directions. Its nega-
tive logarithm 𝑓 was even and convex. It compared the homogeneous case with Schoenberg’s positive-
definitenesscriterionandthezonoidvolume-productbound[61,55],butobservedthatinfinitedivisibil-
ityofthisparticularkernelwouldforceorderintervalstobezonoids. AfterconsideringBergman-kernel
subharmonicity[10],ittestedholomorphiccontractionofLaplacemeanmapsonasquareconeandcon-
cluded:
VERBATIMEXCERPT
Thus no holomorphic contraction on any bounded fixed domain in general. Need exploit station
(global volume vary body). Hess alone not enough.

GeometricMahlerconjectures 12
For a polyhedral cone 𝐷 = 𝐶∗ = {𝑦 ∶ 𝑎 ⋅ 𝑦 ≥ 0}, it then expressed 𝑓∗ through the zonotopes 𝑍 =
𝑖 𝑐
∑ [−𝑐 𝑎 ,𝑐 𝑎 ], where 𝑐 ≥ 0 and ∑ 𝑐 𝑎 = 𝑢. The cost assigned to each coeﬀicient vector came from
𝑖 𝑖 𝑖 𝑖 𝑖 𝑖 𝑖 𝑖 𝑖
maximizing an exponentially weighted section over translated inequalities. With 𝐽 =
2−𝑑∫𝑒−𝑓∗
, the
assistant sought 1/𝜒 (𝑢) ≤ 𝐽 ≤ 𝜒 (𝑣). It noticed that arbitrary unions of the zonotopes could encode
𝐷 𝐶
bipyramidsoverarbitrarysymmetricbodies:
VERBATIMEXCERPT
So pure union Mahler as hard as symmetric general!
It therefore retained the section-derived costs. Its Lorentz-cone asymptotics gave (𝐽/𝜒 (𝑣))1/𝑑 ∼ 𝑒/4
𝐶
and (𝐽𝜒 (𝑢))1/𝑑 ∼ 𝜋/2. For the upper estimate it finally wrote an entropy identity for the density
𝐷
proportionalto𝑒−𝑓∗(2𝑤−𝑢)on[0,𝑢]
,reducingthedesiredinequalitytoalowerboundof𝑑(1−log2)on
𝐶
thesumofitsmeancostanditsrelativeentropyagainsttheconeexponentiallaw.
12 Facet hazards, eikonal flow, and phase losses
The assistant sought an induction for the overlap potential of an exponential cone law. On a facet hy-
perplane it obtained 𝑐 (𝑠)𝑒−𝑓(𝑠) = 𝑐 (0)𝑒−𝑓 𝑖 (𝑠), identifying the hazard-weighted restriction with a lower-
𝑖 𝑖
dimensional overlap potential. It compared this with Meyer’s divergence argument and the zonoid
case [46, 55]. Kinks supplied intervals of subgradients and polar-fiber volume, but the resulting esti-
mate required averages of squared hazards at tilted optimizers. The assistant could not obtain these
averagesfromoffsetvariations: theproposedstationarityconditionconcernedalargerfamilythanthe
originalconeproblem. Italsoconsideredreciprocalsection–projectionestimatesinspiredbyVaaler[65].
Returningtotheeikonalpotential𝜓,with𝑔 = 𝑝2/2,theassistantcorrecteditscomparisonofjoins. If
𝐾
𝐸 denotesanintegratedmixed-Hessiancoeﬀicient,theordinaryjoinuses∑ 𝐸 ,whereastheconiccon-
𝑘 𝑘 𝑘
𝑛
structionweightscoeﬀicientsby1/( ). Simplexandballcalculationsdistinguishedthetwoexpressions.
𝑘
It pursued Kuperberg’s contour construction and Berndtsson’s complex-integral formulation [39, 9],
seeking compensation between the contour’s 𝜓-weight, the desired 𝑔-weight, and oscillatory cancella-
tion. It also used a Golden–Thompson heat-trace bound to reduce another proposed volume estimate
tocontrollingaground-stateenergy[29,63].
CayleycoordinatesconvertedthegradientgraphintoahomogeneousfieldwithHessianeigenvalues
in[−1,1]. Gaussiandeterminantintegralsrepresentedtheprimalandpolarvolumes. Scalingthisfield
toward zero gave a local second-variation estimate; the assistant found that nearly singular directions
preventeditsextensiontotheendpoints. ItexaminedBrascamp–Liebvariancebounds[16]andrecalled
Klartag’scovarianceconditions[38]. Forthesimplex,itexpressedthefieldbyprojectingcoordinatewise
absolutevaluesontothezero-sumhyperplane,exposingthecompetitionbetweenradialexpansionand
collapsingdeterminants.
Theassistantnextdifferentiatedalongtheeikonalcharacteristicfield. ItobtainedRiccati-typeidenti-
tiesfor𝐷2𝜓,relatingradialgrowth,divergence,andweightedcurvature. Aproposedcontourdeforma-
tionthenreproducedthesamegraphunderanewparametrization. Simplexasymptoticsledittoinsist
onrecoveringthecancellationlostbytakingabsolutevalues.
An elliptic Hamiltonian gave a quarter-turn map from the vertical plane to the horizontal plane
through Legendre duality. The assistant found that the accompanying action and billiard-length
estimatesfellbelowitstargetscale. Forself-dualconesittriedorthogonaldecompositions,butiteration
required additional structure on faces; a proposed Moreau-map multiplicity bound failed for an odd-
polygon cone. Its volume comparisons using Rogers–Shephard, Ball’s reverse isoperimetric inequality,
and Barthe’s reverse Brascamp–Lieb inequality retained losses it could not remove [57, 2, 8]. It also
revisited anti-blocking and Bergman-kernel routes through Saint-Raymond and the multidimensional
Suitainequality[59,50].

GeometricMahlerconjectures 13
Finally,rarelargescalarmatricescontradictedanunrestrictedreverseCauchy–Schwarzinequalityfor
averagedmixeddeterminants:
VERBATIMEXCERPT
Fails! Hess homogeneous distributions may not allow scalar mass jump. Geometric path prevents.
The assistant retained the possibility of a geometrically constrained version and turned to a face-pair
formula: orthogonaltangentspacesofpolarfacesmadetheircontributionstothevolumeof(𝜆𝐼+𝜕𝑔)(𝐾)
explicit.
13 Transport moments and a weaker constant
After considering Kuperberg’s contour argument and Saint-Raymond’s unconditional result, the as-
sistant expanded the eikonal potential around a quadratic gauge [39, 59]. For the odd perturbation
ℎ = 𝑟2cos(3𝜃), it obtained a nonzero fifth-order odd term and used subsolutions, supersolutions, and
characteristicdecaytocomparetheexpansionwiththecontrolvalue. Itthereforerejecteditsproposed
evenness of the potential. In the anti-polar case, it applied a moment estimate attributed to Berwald,
with a binomial factor, but found that its high-moment bound lost the constant scale it needed [12].
It then reconsidered transport–entropy approaches [32], seeking a replacement for the degenerating
eikonalHessian.
The replacement was uniform Brenier transport from 𝐾 to −𝑄, where 𝑄 = 𝐾∘. Its constant Jacobian
ledtheassistanttowrite:
VERBATIMEXCERPT
Great! We can choose **any monotone map \(T\) K→−Q**, not eikonal, no homogeneity.
Combiningthisnegativegraphwiththepositivegradientgraph,itderivedcapsonmixed-Hessianmo-
𝑛 2
ments. It then selected a balanced linear position with |𝐾| = |𝑄| = 𝑝𝜅 , writing 𝑐 ≤ poly(𝑛)( ) . Ball
𝑛 𝑘 𝑘
inclusiongaveonlythescale𝑝1/𝑛 ≥ 1/2. For𝐾 = −𝑄,italsousedRogers–Shephardontheinclusionof
its positive-gradient image in 𝐾 −𝐾 tobound that image’s volume [57]. A uniform-direction gradient
argument also failed its simplex test: the assistant found that the volume depended on rare directions
missedbythatcoupling.
Weighted angular integration produced recurrences for negative support moments. The assistant
foundthatnonnegativekernelscouldnotpropagatetherecurrencethroughthelowerhalfoftheexpo-
nent range. Projection estimates, spherical neighborhoods, and exponential kernels then led it back to
curvaturemoments. Withℎ = ℎ , 𝐵 = ∇2ℎ+ℎ𝐼, andnormalizedelementarysymmetricfunctions𝜎̄ ,
𝑄 ℎ 𝑆 𝑘
itwrote
𝑤𝑛−𝑘+1
𝑛
𝑍 = 𝔼ℎ𝑘−𝑛𝜎̄ (𝐵 ), 𝑍 ≥ 𝑘 , 𝑍 ≤ poly(𝑛)( )𝑝,
𝑘 𝑘 ℎ 𝑘 𝑤𝑛−𝑘 𝑘 𝑘
𝑘+1
where 𝑤 denotes the corresponding normalized intrinsic volume. Telescoping the middle ratios, it
𝑘
concluded that 𝑝1/𝑛 ≥ 𝑒−1/2 + 𝑜(1), and checked the coeﬀicient normalization, metric selection, and
transport regularity. It compared this with its target √𝑒/(2𝜋), identifying an accumulated logarithmic
gapofabout0.081𝑛2.
A conic calculation with shifted Gaussian face integrals returned the same constant. The assistant
soughtthemissingcontributioninHölderslack,butfoundthatabstractcurvature-measurerecurrences
allowedsharplyconcentratedmovingdistributions. Itintroducedjointprimal–dualfacemeasuresand

GeometricMahlerconjectures 14
tracked the support gradients lost when passing to adjacent faces. Signed perpendicular heights pre-
vented an immediate positive coupling of complete face chains. Finally, it used the angular partition
generatedby𝜆𝑌+𝑋,forpairedpolar-facepoints𝑌,𝑋. Itshypotheticalzero-slackprofilesuppliedtoo
littleangularvolume. Itcontinuedbyexpressingtheangularintegralthroughjointnegativemoments
of|𝑌|2 and|𝑋|2,lookingforsimultaneouslower-tailcontributions.
14 Centered orthoschemes and the remaining general-case obstruction
Theassistantcomparedangularsaddleconstraintswiththeregular-simplexprofile,thensoughtasharp
estimateforindividualorthoschemes. Fordecreasingsquaredface-footlengths𝐴 ,itwrotetheirGaus-
𝑖
sianconeintegralas
⎛ 1 ⎞
𝐼(𝐴) = ∫ exp⎜ ⎜− ∑𝐴 𝑟 𝑟 ⎟ ⎟ 𝑑𝑟.
𝑟≥0 2 max(𝑖,𝑗) 𝑖 𝑗
𝑖 ⎝ 𝑖,𝑗 ⎠
ItappliedPrékopa’smarginallog-concavitytheoreminlogarithmiccoordinates[54]. At𝐴 = (𝑛−𝑖)/(𝑖+
𝑖
1),Gaussianorderstatisticsrepresentedthelogarithmicderivativesthroughorderedbetadistributions.
MonotonicityofthetwoGaussianmean-excessfunctionssuppliedthedesiredderivativeordering:
VERBATIMEXCERPT
Thus H decreasing. Nice. Beta stoch increasing. g monotonic all n exact! Let's note.
The assistant concluded that the resulting flag estimate could be summed for perfectly centered poly-
topes. It then identified two obstacles to its intended application: general flags carry signs, and the
metric furnishing the transport bounds need not makethe facefeet lie inside their faces. A calibration
using adjacent-face recurrences led it to incompatible equations on overlapping simplex regions. Re-
placingfacefeetbynearestpointsrestoredpositivesubdivisionsbutintroducedzerotransitionheights
andmismatchedflagweights.
The next approach used Gaussian Moreau projection paths. Integrating projections along shifted
Gaussian lines produced convex transport maps into the two cones, in the spirit of Barthe’s transport
proof [8]. A determinant comparison reduced the proposed estimate to a scalar rank-profile inequal-
ity. It explored arbitrary translations, convexified cost profiles, and signed walks through face sub-
spaces. Thesewalksretainedpositivequadraticenergyformulas,butthinangularregionsdefeatedthe
proposed local comparison. Gaussian distance profiles and the Wills functional provided further con-
straints;theassistantfoundthattheresultingestimatesstilllostthesharpconstant. Italsorevisitedthe
Kuperberg bound and Berndtsson’s complex-integral approach while comparing Gaussian regulariza-
tionandconiccontourconstructions[39,9].
Thenextconstructiontransportedexponentialmeasuresdirectly. Writing𝛼 = 𝜒 (𝑣)𝜒 (𝑢),𝑀 = 𝐷𝑇,
𝐶 𝐷
andΔ = 𝑢⋅𝑇−𝑣⋅𝑡,theassistantderivedthecandidateaveragedbound
𝔼[𝑍 (𝑝)𝑒(1/2−𝑝)Δ] ≤ √𝛼.
𝑀
Since𝔼Δ = 0,itsoughtsimultaneousboundsfromtypicalproductsoftransportHessians. Itproposed
aligningtheresultingaxesbyachangeconfinedtoasubspaceofsmalldimension,whilerecordingthe
needtocontrolintegrability,uniformityin𝑝,andtheeffectonfacedeterminants. Atiltedface-balance
identitythengavetheexpectedprojectedenergyinthealignedposition. Theassistantstillneedednested
facedistributionsandcontrolofrarecontributionstotheangularintegrals.
Finallyitvariedaweightedcurvaturefunctional. Atahypotheticalminimizer,itinterpreteditssigned
first-variationmeasurethroughamartingalecouplingbetweenincidentfaces:

GeometricMahlerconjectures 15
VERBATIMEXCERPT
So station imposes mass strictly flows from negative faces F to positive cofaces H!
Fromthisproposedstationarityconditionitinferredconditionalboundsonvertexnormsandfacetdis-
tances,thenbegantranslatingthesignedfacemassesintoconicnotation.
15 Slicing profiles and the missing sharp constant
The assistant tried to use stationarity to balance the face coeﬀicients of an amplified cone. Minimizing
their geometric mean appeared to force the signed first-variation masses to vanish rank by rank. It
then checked the proposed lower bound against the ball and changed the objective back to the largest
normalizedcoeﬀicient.
VERBATIMEXCERPT
Ball violates desired geometric mean inequality!
Itnextexpressedexterior-powercoeﬀicientsthroughcomplementaryprojectionsofprimal–dualcon-
tactpairs. Forafiber𝑄 ,itssupportfunctionℎ(𝑠,𝑏)gavethetangentintercept
𝑏
𝜏(𝑠,𝑏) = ℎ(𝑠,𝑏)−𝑏⋅∇ ℎ(𝑠,𝑏).
𝑏
Theassistantinterpretedthisinterceptthroughalinearprogram,thenenlargedtheslicingsubspaceto
obtainintegralsinvolvingHessianminors. CenteringeachfiberatitsSantalópointsuggestedaconcave
scalarprofile𝑊,withalowerestimateinvolving(𝑊 −𝑏⋅∇𝑊)−𝑘. Rogers–Shephardprojection–section
bounds and Berwald’s inequality entered the comparison with fiber volumes [58, 12]. A radial profile
flat near the origin and proportional to −𝑟log𝑟 farther out obstructed the proposed entropy-scale con-
stant. Combining the weaker estimate with projection bounds did not yield the sought contradiction.
One-coordinaterecursionsalsolostfactors,andmixedderivativesobstructedtransferringthescalarcal-
culationtogeneralfibers.
Theassistantreturnedtoadirectionalcriterionoftheform𝑓 (0)𝑒 (𝑣) ≤ 1/𝑒,pairingacentralmarginal
𝑣 𝜈
density with a positive-part moment of a polar normal measure. It examined covariance restrictions
associated with Klartag’s approach and a dimension-independent lower rate supplied by Bourgain–
Milman [38, 15]. Meyer-style hyperplane partitions led it back to weighted versions of the same di-
rectionalcriterion,whileZhang’sreverseprojectioninequalityleftadimension-dependentloss[46,67].
Cutsthroughproductconesdidnotstrengthenasinglecut. Addingpointsfromcomplementaryaﬀine
slices to contact pairs then produced a directional upper bound for an exterior coeﬀicient; inserting
lower-dimensionalvolume-productestimatesagainlostabinomialfactor.
Forprismatoids, theassistantwrotethefibersas(1−𝑞)𝐴+𝑞𝐵andcomparedtheirmixed-volumedis-
tributionwithabinomiallaw. Homotheticsummandsgavethedesiredscale,whereascomplementary
lower-dimensional summands concentrated the distribution and lost a square-root factor. It sought
compensation for this loss in the volume product of 𝐿 = 𝐶 + 𝐷, considering mixed subdivisions and
variationsofthesummands. LookingatReisner’szonoidmethod,Meyer–Reisnershadowsystems,and
Saint-Raymond’santiblockinginequality,itmadefurtherattemptstoreducesumsofalignedsimplices;
it also revisited reverse Brascamp–Lieb comparisons [55, 47, 59, 8]. The assistant also revisited Kuper-
berg’ssymmetricboundandBarthe–Fradelizi’sreflection-symmetrymethod,askingwhetherrepeated
nonsymmetric factors could acquire enough symmetry without losing the volume-product informa-
tion [39, 7]. Finally, slicing a cone along an extreme ray produced an ordinary convex body with a
distinguished vertex; the assistant recognized the resulting inequality as the original Mahler problem

GeometricMahlerconjectures 16
inthatdescription.
16 Flags, Gale densities, and degenerating decompositions
The assistant tried to combine tensor induction with projection estimates, but found that conditioning
produced truncated exponentials or nonlinear gauges outside the proposed induction class. Addinga
Euclideanballthroughasupport-functioninterpolationrecoveredthemixed-volumeconstraintitwas
trying to strengthen. Its comparisons used Kuperberg’s bound and Klartag’s covariance framework,
whileaprojection–sectioncalculationusedtheRogers–Shephardinequality[39,38,58].
For a simple polytope, it expressed the volume product through the relative entropies of incident
facet-slack coordinates against independent exponentials. It explored a reversible walk on the vertices
andtheLawrencevolumeformula,thenusedfaceflagstoassemblesimplices[41]. Alowerboundthat
retainedonlyflagsanchoredatthesamevertexfailedonregularpolygonswithincreasinglymanysides.
Returningtoacommondecompositionofthewholebody,itfoundanomittedinversevertexprobability.
With𝜋 proportionaltothedeterminantassociatedwithvertex𝑖,therevisedidentityhadtheform
𝑖
𝑛!|𝐾||𝐾∘| = ∑𝜋−1𝔼 ∏ℓ (𝑦 ).
𝑖 𝜎 𝐹 𝑗 𝑆 𝑗
𝑖 𝑗
The corresponding Jensen estimate contained twice the entropy of 𝜋. The assistant then noticed that
verticescouldcoalescewhiletheirdeterminantweightsstayedpositive: vanishingflagslacksdrovethe
logarithmic estimate downward. It retained an exact face recurrence with relative-entropy corrections
andlookedforaboundthatwouldaccommodatethisdegeneration.
The next approach differentiated the volume polynomial with respect to facet offsets, invoking the
Hodge–Riemann framework for simple polytopes [64]. Under an additional nonnegativity condition
on repeated edge coeﬀicients, the assistant derived that every two-dimensional face was a triangle or
parallelogram. It then propagated the local edge structure to describe an aﬀine product of simplices
and checked its factored volume product. It identified signed repeated coeﬀicients as the obstacle to
applyingthisargumentgenerally.
Gale duality recast a slack fiber using the density of a projected Dirichlet distribution and a sum of
determinantsoverfeasiblebases. Theassistantconsideredcomplementarysimplexprojections,reverse
Brascamp–Liebestimates,centroid-sectionbounds,andVaaler’ssectioninequality[8,27,65]. Itfound
that separately bounding the density and determinant sum lost their dependence on the same config-
uration. A wall-crossing calculation then led it to conclude that the weighted determinant sum was
maximalattheweightedcenter. Deletingonecoordinateandintegratingallslicesturnedtheinduction
intoareciprocal-sectionintegralrequiringafactortendingto𝑒. Alongachosenlineofcenters,theassis-
tantrecoveredthatfactorinthenear-maximal-asymmetryregime;forsmallerasymmetryitrecordeda
deficitandreturnedtocovarianceandstationarityconditions.
17 Stationary hazards and a translation instability
TheassistantreturnedtoitssimultaneousboundarycouplingatahypotheticalglobalMahlerminimizer.
It sought deformations whose costs were aﬀine on both primal and dual faces, but dense incidence
patterns and projectively unique polytopes obstructed the proposed shadow motions. It revisited the
shadow-systemargumentsofMeyer–ReisnerandChen–Li–Xi–Xuinthisconnection[47,19]. Facethaz-
ardsofexponentialconemeasuresthenproducedareversiblegraphwithaprescribeddrift. Filteringits
stationaryprocessrecoveredauniformDirichletlawforasimplex;theassistantstillneededanentropy
estimateforgeneralcones.

GeometricMahlerconjectures 17
It next expressed slicing induction through integrals of reciprocal polar section masses. Primal and
dualfiberendpointssharedaprojectedvariable,allowingittocomparetheirLaplacetransforms. When
onlyonefacetcoeﬀicientwaspositive,awidthvariable𝑊 satisfied𝔼𝑊 = 1/𝑝and𝔼𝑊2 = 2/𝑝,forcing
𝑝 ≥ 1/2. It could not guarantee such directions. Testing positive-semidefinite cones, it found large
inflationbetweenthenormalmeasureandtheuniformsectionmeasure:
VERBATIMEXCERPT
Thus direct criterion fails globally for PSD cones!
It therefore sought volume-product gains outside this central-density criterion, returning to Kuper-
berg’ssymmetricestimate,Reisner’szonoidargument,hyperplanesymmetries,andanti-blockinginduc-
tion[39,55,7,59,46]. ItsprojectionandconfigurationcomparisonsusedRogers–Shephardprojection–
section bounds [58]. In recalling its graph-volume argument, it also invoked their difference-body
bound through the inclusion 𝑆 ⊂ 𝐾 − 𝐾 [57]. Its covariance normalization followed the isotropic-
constantapproach[38]. ApplyingreverseBrascamp–Liebtonormalizedrayframesgaveadeterminant
lowerboundwhosemissingfactorithopedtorecoverfromthecoupling[8].
Theassistantthenstudiedthestrongerfunctionalobjective
𝑒−𝑑𝑑!|𝐿|𝑍(𝐿∘), 𝑍(𝑄) = inf∫ 𝑒𝑧⋅𝑦𝑑𝑦.
𝑧 𝑄
Facetconditioningsuggesteddimensioninduction,withconditionalhazardsconstrainingarescalingof
the projected generators. The assistant tracked local simplex determinants and graph rates, but nons-
moothchangesoftriangulationcontinuedtoblocktheproposedsecond-variationargument.
Translating 𝐿 preserved its volume and isolated 𝑍. Writing 𝑄 = 𝐿∘, it used the projective change
𝑦 ↦ 𝑦/(1−𝑡𝑥⋅𝑦). Atan interior stationary translation it obtained 𝑧 = 0; minimizing over the tilt then
gave
𝑑2 ∣
log𝑍((𝐿−𝑡𝑥)∘)∣ = −(𝑑+2)𝑥TΣ 𝑥.
𝑑𝑡2 ∣
∣𝑡=0
𝑌
VERBATIMEXCERPT
Thus stationary translation is **strict local maximum**!
Itfirstexploredwhetherthenormalized-momentlog-concavityattributedtoBerwaldextendedjointly
to dilation and moment power, to control the drift between weights [12]. For a boundary chord, it
rewrote the second derivative as a residual quadratic moment. Joint log-concavity of lifted integrals
weightedby(±𝑥⋅𝑦−𝑡)2 ledittothemoregeneralinequality𝑔″ ≤ (𝑔′)2,where𝑔 = log𝑍. Itconcluded
+
that1/𝑍wasconvexalongtranslationsandpursuedstrictnessatstationarypointsthroughareflected-
gammacomparison. Itthentriedtoextendthisargumenttoshadowdeformationsandtocomparethat
convexitywiththechangesofprimalvolumeacrosstriangulationboundaries.
18 Scalar Gaussian progress and the matrix obstruction
The assistant continued the Meyer–Reisner translation approach [47] by moving every nonzero vertex
of a pyramid. It initially expected the resulting Hessian equality to restrict the cone, then recognized
thatthemotionwasalreadyalineartransformation:

GeometricMahlerconjectures 18
VERBATIMEXCERPT
Right translation of all vertices equivalent GL! Thus Hess equality automatically for pyramid all
x.
Moving the distinguished origin onto the base instead gave a lower-dimensional functional product.
The assistant calculated a square-root dimensional loss and found that a ball did not supply the com-
pensatingdecreaseitwanted. Italsoderivedapolynomialcomparisonbetweenthevalueattheoriginal
vertexandatthecentroid,butitsattemptstocombinethiswithKuperberg’ssymmetricboundretained
anexponentialloss[39].
TheGaussianroutebalancedprimalanddualcovariancesbyoptimizingametric. Theassistantused
Brascamp–LiebandBochnerestimatesformetricconcavity,consideredEhrhard’sinequality,andrevis-
ited Barthe’s direct/reverse comparison [24, 8]. Optimizing the metric added positive terms involving
thirdmomentstothetiltHessian;fixingacommonmetricallowedanisotropicescapeevenfororthants.
Quadratic penalties restored bounded minimization but weakened the spectral estimate. Recalled en-
tropyargumentsalsousedBerwald’smomentinequalityandtransport–entropyformulationsofinverse
Santalóinequalities[12,32,26].
The assistant then concentrated on a centered random variable 𝑊 with density proportional to
𝑒−𝑥2/2−𝜙(𝑥),
where 𝜙 is convex and 𝑊 has variance 𝑠. It compared this law with two Gaussian tails
joined at a kink, matching its first three moments. It assembled sign-change arguments, differential
barriersforahalf-lineGaussianparameter,andpolynomialcoeﬀicientestimatesintoanargumentfor
1+𝐵−1
Var(𝑊2)+ 𝑠 (𝔼𝑊3)2 ≤ 2𝑠, 𝐵 = 𝑚2−𝑠,
1−𝑠 𝑠 𝑠
where𝑚 isthemeanofahalf-lineGaussianlawwithvariance𝑠. Itdescribedthisasaproofofthescalar
𝑠
estimate,thentriedtoextenditthroughsuccessiveone-dimensionalGaussiansmoothings.
EarlieroptimizedslicesintroducedadditionalmixedHessianterms,andfixedgenericsubspacesagain
admittedanisotropicescape. TheassistantconnectedtheremainingcovarianceproblemwithKlartag’s
conicformulation[38]andreturnedtosectionarguments,includingMeyer’smethod[46]. Adimension
reductionstilllostafactoroforder√𝑑:
VERBATIMEXCERPT
Can't ignore .5log d per step.
Itnextrejecteditsproposedsingle-conematrixmomentbound: theradialcomponentalreadyexhausted
the allowance, while an asymmetric tangential component could remain. The subsequent calculations
soughtcancellationbetweentheprimalanddualthird-momenttensors,Gaussianboundarystationarity,
andpossibleJordan-algebrastructurewhentheprojectiveHessianwasdegenerate.
19 Activation transport and polar proximal maps
The assistantreturned toGaussian regularization and the isotropic-constant approach associated with
Klartag [38]. Rank-one elimination led back to a one-dimensional functional Mahler inequality, but
exchanging a supremum and an integral introduced a loss from varying conditional maximizers. It
revisitedthetransport–entropyformulation[32,26]andtriedaveragingdirectionsacrossindependent
copies. ItsGaussianapproximationproducedacriterioninvolvingdirectionalFisherinformationtimes
variance;steepapproximationstoexponentiallawsdefeatedthatcriterion.

GeometricMahlerconjectures 19
VERBATIMEXCERPT
For sharply truncated Exp, Fisher huge. CLT route fails.
Randomperturbationsofreplicatedtiltsremovedafirst-ordermetricresponse,buttheassistantfound
thatthesameperturbationsloweredtheobjectiveatorthantequalityandthereforerequiredconfinement
orboundarycontrol.
Itnextorganizedshiftedconeprojectionsbyexpectedactive-facedimension. ALegendretransforma-
tion of their cost profiles converted the desired estimate into an integral comparison with the orthant.
The assistant calibrated a heat-flow trajectory to that reference, then found that its adjoint weighting
measure was not even, whereas complementary terminal projections paired opposite shifts. A cosine
seed density formally removed an asymmetry but introduced bounded-support requirements. It also
obtainedaGaussianprojectionboundfromapositivetightframeandaskedhowsuchaframecouldbe
suppliedinthedualcone𝐷. Narrowcircularconesobstructedthatrepresentation;theassistantargued
that simultaneous positive tight frames on both polar sides would force orthant structure. Reflected
Brownianmotionsuggestedanotherconstructionthroughboundarylocaltimes, butsingulardistribu-
tionsanddependencebetweenstoppingclockspreventedthedesiredentropyestimate.
Returningtomoments,theassistantexpandedthejointobjectivetofourthorderatcovarianceequality.
Cubic perturbations of a ball then led it to reject a universal covariance-product upper bound without
additionalshapeconditions. ItconsideredCaffarelli’scontractiontheorem[17]forcontrollingthethird-
moment tensor, and an algebra built from that tensor, but could not obtain positivity of the relevant
multiplication operator. It also recalled local minimality at the simplex [37] while considering shape
variationsoftheprojectionprofiles.
Thefinalbranchusedpolarproximalmaps,writing
𝑦 = Π 𝐺, 𝑥 = 𝐺−𝑦 = prox (𝐺).
𝜏 𝜏𝐾∘ 𝜏 𝜏 𝜏𝑝
𝐾
ForafixedGaussianvector,theassistantrelatedthedilationparametertothegaugeoftheresidualand
interpreted the same residual as projection onto a dilation of 𝐾. Adaptive matching of the two gauge
costs yielded an entropy expression for the distribution of logarithmic scales. It investigated whether
changesofmetric,determinantestimates,andstrictnessingaugesubadditivitycouldcontrolbroadscale
distributions. Itaskedwhethertheresultinghomogeneousgaugewasconvex.
20 Centered kernels and a sharpness gap
TheassistanttranslatedtheGaussianinputtomaketheprimalproximalimagehavemeanzero. Writing
𝑃foritsJacobian,𝐵 = 𝔼𝑃,𝑡 = tr𝐵/𝑛,and𝑝 = 𝔼⟨𝑥,𝑦⟩/𝑛,itderived𝑑𝑡/𝑑𝑠 = 𝑝evenwiththemovingcenter.
Gaussianchaosestimatesgave
1
𝐶 = 𝐵−Cov(𝑥), 𝐵(𝐼−𝐵) ⪯ 𝐶 ⪯ 𝐵(𝐼−𝐵),
2
and it interpreted small 𝑝 as proximity to complementary linear projections. It then corrected its treat-
mentofconvexenvelopes: averagingslopescouldincreasethelogarithmicslopeintegralneededforthe
entropybound.
TheassistantconsideredextendingBorell’sGaussiannoise-stabilityinequalitythroughthesemigroup
approachofMosselandNeeman[14,48]. ItquestionedwhethernoncommutingHessiansadmittedthe
scalar comparison, testing Clifford and Jordan examples and the restrictions imposed by symmetry of
thirdderivatives. ItalsoconsideredGaussiancomparisonandregularellipsoidpositions[30,52].

GeometricMahlerconjectures 20
Across-scalecalculationinsteadledittothekernels
1 𝑢 𝑑𝑣
𝑚(𝑡,𝑢) = min(𝑡,𝑢)−𝑡𝑢, 𝑘(𝑡,𝑢) = √𝑝(𝑡)𝑝(𝑢)exp(− ∣∫ ∣).
2 𝑡 𝑝(𝑣)
Assuming𝐵 = 𝑡𝐼,itusedsecond-orderGaussianPoincaréestimatestoobtain𝑚 ≤ 2𝑘 againstnonnega-
𝑡
tiveweights. Itidentified𝑘withtheGreenkernelof−𝑑2/𝑑𝑡2+𝑉,where𝑉 = (1−𝑝′2+2𝑝𝑝″)/(4𝑝2). For
theorthantprofile,𝐼(𝑡) = 𝜙(Φ−1(𝑡))satisfied−𝐼″ = 1/𝐼,givingequalityintheassociatedHardyinequal-
ity. The assistantthencalculated the entropyvariationand foundthat itsweightwasnotproportional
to𝐼2:
VERBATIMEXCERPT
Ratio varies ~.5 tails >.386 center. Not stationary ⇒ Hardy alone insufficient even close to orth
if V redistribution.
ItpursuedhigherGaussianchaoses,approximatenestingofHessianprojections,antipodalcomparisons,
andmetricchangesintendedtoremovethelinearGaussiancomponent.
TheassistantnexttriedtoexploittheexponentiallawasthesumoftwosquaredGaussians. Integrat-
ingone-sidedproximalpathsandpairingoppositeGaussianinputsreproducedtheorthant’squadratic
map. Forgeneralmaps,itencounteredachange-of-variablesobstruction:
VERBATIMEXCERPT
General can have singularities and many preimages (non-gradient in r).
It investigated complex quadratic forms and self-dual cone order intervals. It revisited its use of the
Rogers–Shepharddifference-bodybound[57]. Inrevisitingtheseroutes,itrecalledKuperberg’slinking
construction,Klartag’scovarianceapproach,reflectionandzonoidinequalities,reverseBrascamp–Lieb,
andZhang’sprojectioninequality[39,38,7,55,8,67];italsoreturnedtocontractiontransport,Gaussian
tubeconcavity,andpolynomial-degreeformulas[17,24,11]. Finally,itrewrotethecalculationdirectly
for cone projections with means 𝑀,𝑁, obtaining 𝑑𝑡 = (𝑁 ⋅𝑑𝑀 −𝑀 ⋅𝑑𝑁)/𝑑, and explored paths with
nonconstantmeandirectionstoadjustthecross-kernelandentropycosts.
21 Entropy concavity, convexification, and fixed tests
The assistant rewrote the Gaussian projection slope entropy using 𝑔 = 𝐴′, ℎ = −𝐵′, and 𝑟 = 𝑔/ℎ. The
Wronskianidentitymade𝑄(𝑡,𝑣) = 𝑔(min(𝑡,𝑣))ℎ(max(𝑡,𝑣))doublystochastic. Arelative-entropyvari-
ational formula then expressed 𝐽 = ∫log(𝑔ℎ) as a concave functional of log𝑟, with an orthant tangent
involvingaweightthatchangedsign. Ittriedharmonic-meanestimatesfortheaveragedprojectionHes-
sian, but the sign change prevented the proposed direct comparison. Convexifying the costs created
anotherobstruction:
VERBATIMEXCERPT
But total Q mass slack may offset? J_env≥J_raw usually, cannot assume.
Theassistantnextconvexifiedtheplanarcurve𝐵(𝐴),mixingcomplementaryprojectionmapsatchord
endpoints. It obtained a modified Wronskian density 0 < 𝑤 ≤ 1, monotone virtual slopes, and a dual
NeumannGreenoperator−𝜕(𝑉−1)𝜕+𝑤. AssumingafullHardyinequalityfor𝑉,itderivedacompar-
isonreducingtheentropyexpressionto𝑤 = 1. Itpursuedmetricbalancingthroughtruncatedpositive

GeometricMahlerconjectures 21
eigenfunction tests and rank-dependent bounds on the costs, while retaining questions about continu-
ity,singularmeasures,andendpointlimits. Apositive-framecomparisonusingreverseBrascamp–Lieb
gaveaone-sidedpotentialbound,whoseentropyvariationagainchangedsign[8].
UndertheHardyassumption,itsorthanttangentestimatestillleftapositivegap. Theassistantthere-
fore studied near equality: an integrated Hessian close to a linear Gaussian matrix, nearly nested pro-
jections, and a contact kernel that separated into a product off the diagonal. Wick expansions and a
quadratictestgavedifferentcoeﬀicientsforvarianceheterogeneity,whichithopedtoturnintoaquanti-
tativecontradiction. Itconsideredlocalminimalityatthesimplex[37],butnotedthedimensiondepen-
dence of the required neighborhood. It also revisited scalar noise stability, Gaussian tube inequalities,
andthelossinasymmetric-suspensioncomparison[14,24,39].
Tomaketheperturbationmoreexplicit,theassistantreplacedthepotential-dependenteigenfunction
bythefixedGaussianprofile𝐼(𝑡) = 𝜙(Φ−1(𝑡)). With𝑇 = 1−ℒ ,𝛿 = 𝐼2𝑉−1,𝑢 = 𝑇−1𝛿,and𝜂 = 𝑧𝑢−𝑢′,
𝐺
itsbalancedtestgavethequadraticcondition2𝔼𝛿+𝔼𝜂2 ≤ 0. Polynomialtestssuggestedawaytocontrol
anisotropy,butitstillneededboundedtestsandtailestimates. Theassistantthennoticedthatthissingle
fixedtestdidnotprovidethefullHardyspectralgapusedintheconvexificationcomparison. Itexplored
hybridtestscombiningthefixedprofilewithapositiveeigenfunction,includinghowtheirmixedterms
andbalancingconditionswouldchange.
22 Resolvent cancellation and mismatched Gaussian paths
The assistant decomposed an integrated Hessian as a linear Gaussian matrix plus higher Gaussian
chaoses. Itusedeigenvalue-pairmeasurestocomparematrixDirichletenergywithascalarSteinform,
thensoughttocancelfirst-orderresidualsthroughanauxiliaryprimitivewhosederivativewasasquared
test derivative. It found that the proposed test class could fail to remain regular for induced measures
with atoms, and returned to smooth Gaussian-reference tests. A direct spectral-layer calculation then
canceledseveralnesting-errorterms.
Theassistantnextconsideredmultiplyingahypotheticalcounterexamplebymanyorthantfactors. It
expected the nonorthant contribution to become a small perturbation, making squared displacement
terms negligible to first order. Rewriting this calculation directly on the original cone produced
proposed identities relating contact, nesting, and Gaussian-chaos errors. The assistant still needed
a dimension-independent bound for the spectral trace error. Commuting Gaussian-mixture models
exposed variance heterogeneity; noncommuting matrices added divided-difference errors. It tried
logarithmically oscillating tests, complementary squared derivatives, and separate estimates for even
and odd Gaussian degrees. It also found that some additional compatibility identities merely restated
relationsalreadyavailable.
In these comparisons, the assistant reused the projective covariance restrictions associated with
Klartag’s conic approach, revisited Borell’s scalar noise-stability comparison, and recalled why
Kuperberg’ssymmetricboundalreadyexceededthenonsymmetricasymptoticconstant[38,14,39]. It
returned to its earlier Gaussian projection and heat-calibration calculations rather than obtaining the
remainingtraceestimate.
Asign-changingentropyweightpromptedadifferentpathconstruction. Theassistanttriedsplicing
aprimal-centeredpathtoadual-centeredpath;atthecentraljunction,however,itsFenchelcalculation
producedtheoppositeboundarysignfromtheoneitwanted:
VERBATIMEXCERPT
Boundary ≥0 UNFAVORABLE!
ForastraightalignedpathitderivedanexpressioninvolvingexpectedJacobiantraceminuslongitudinal

GeometricMahlerconjectures 22
curvature, weighted by an odd function. It found that extreme horizontal stretching and compression
could both make the expression unfavorable. Reversing the splice gave a favorable central boundary
term, but the assistant still sought control of the negative Gaussian projection energies. It considered
positivetightframesandreverseBrascamp–Liebboundsaspossiblecompensationforapoordualpro-
file[8].
Finally,theassistantseparatedthetwocenteredpathsaltogether,prescribingprimalanddualmeans
independentlyanddrivingtheirprojectionsbyoppositeGaussianinputs. Itnoticedthattheircross-cost
boundnowusedtheunperturbedorthantkernel:
VERBATIMEXCERPT
This is huge: cross-cost kernel is *exactly orth reference*, not perturbed.
ItbegancombiningthiscontactboundwithHessiancross-productstoseektheintegratedrankcompar-
isonrequiredbyitsentropyestimate.
23 Stitched kernels and a failed Gamma interpolation
The assistant joined a primal-centered Gaussian projection path below zero to a dual-centered path
above zero. It found that ordered contact products retained the form 𝐴(𝑧)𝐵(𝑣) for 𝑧 ≤ 𝑣, even when
the path jumped at the junction. Fixing 𝐴 on one half and 𝐵 on the other eliminated the quadratic
perturbationofthiskernel. Writing𝐽(𝑧)forthesumofthetwoscalarbarrierdifferencesonthenegative
half-line,itexpressedtheprimarydeficitas
0
𝑆 = −2𝐽(0)−4∫ 𝑧𝐽(𝑧)𝑑𝑧.
−∞
The entropy expression used a different weight. The assistant obtained a favorable junction term from
the Fenchel gap, but still needed to control a trace defect associated with unequal Gaussian variances.
Adding the decaying homogeneous solution (𝐴 /𝜑)2 preserved the bulk differential identity; its even
0
extension introduced a cusp and a single-layer term that the assistant could not bound by the existing
deficit. Italsoexploredstaggeredswitchesthroughincreasingsubspaces.
The assistant then revisited Gale densities, orthant sections and projections, and direct and reverse
Brascamp–Lieb comparisons, including Barthe’s transport argument [16, 8]. Its recalled alternatives
includedKlartag’scovariancecondition,Kuperberg’ssymmetricbound,zonoidvolumeproducts,and
shadow-system convexity [38, 39, 55, 47]. It also considered Vaaler-type section estimates, centroid-
density estimates and log-concavity, while identifying losses in the resulting density bounds [65, 27,
54]. Separatedirectandreverseinequalitiesboundedtheirintegralsinoppositedirections;theassistant
soughtacomparisonoftheirdeficitsinstead.
CenteredGammapotentialssuggestedsuchaninterpolation. Fornormalizedrays𝑞 ,positiveweights
𝑖
𝑝 summingto𝑑,anddualcones𝐶,𝐷,itdefined
𝑖
𝑃 (𝑥) = ∏(𝑞 ⋅𝑥)𝑝 𝑖, 𝑃 (𝑦) = sup ∏𝑠 𝑝 𝑖,
𝐷 𝑖 𝐶 𝑖
𝑖 𝑦=∑ 𝑖 𝑝 𝑖 𝑞 𝑖 𝑠 𝑖 𝑖
withpositive𝑠 . ItdividedtheproductofthecorrespondingweightedexponentialintegralsbyΓ(𝑎+1)2𝑑,
𝑖
callingtheresult𝑅(𝑎),andaskedwhetheritdecreasedtoitsGaussianlimit. Laplaceexpansions,Gamma
Stein identities, and variations of the weights produced further conditions to check; the assistant also
consideredBall’scube-slicingboundasapossibledensityestimate[3]. Rare-tailcomparisonsforextra
rays then suggested that 𝑅(𝑎) could fall below one for arbitrary balanced bases, including choices the

GeometricMahlerconjectures 23
assistanthadhopedtojustifybydeterminantoptimization. Itthereforeredirectedtheargumenttoward
smallpositivepowersandoptimizedweights.
Splitting a ray could produce a negative direct-integral variation of order |𝑡|1+𝑎𝑝 𝑖; the assistant com-
pared this with dual gains governed by masses outside adjacent facets. It still needed control of the
optimizingweightsandofexistencewhenthenumberofraysincreased.
VERBATIMEXCERPT
If m unrestricted, existence may nonpoly.
24 Canonical barriers and aﬀine-sphere volume targets
The assistant first paired Gamma potentials through a stochastic channel on normalized cone rays.
Relative-entropy contraction ordered the potentials, but the two partition functions still used different
Gibbs measures. Gale coordinates then expressed the volume product through feasible bases and
projected slack volumes. The assistant explored centroid-section estimates, complementary projec-
tions, and random shifted constraints, drawing on Fradelizi’s section bound and Rogers–Shephard
comparisons; it found that independent thresholds could discard too much determinant mass for
round bodies [27, 58]. Regular upper hulls gave an exact slope-density identity, which the assistant
recognized as another form of its separable gradient map. It also revisited stationary covariance
constraintsfromKlartag’sapproachandreverseBrascamp–Liebestimates[38,8].
The cubic term in the Gamma expansion suggested replacing a chosen logarithmic barrier by the
canonicalpotential𝐹,with
𝐹(𝑡𝑦) = 𝐹(𝑦)−𝑑log𝑡, det𝐷2𝐹 = 𝑒2𝐹.
Using the Cheng–Yau aﬀine-sphere framework, the assistant sought the stronger comparison 𝜒 (𝑥) ≥
𝐶
𝑒𝐹 𝐶∗(𝑥), where 𝜒 isthe cone Laplaceintegral[20]. Foracone over 𝐾 ⊂ ℝ𝑛, with 𝑑 = 𝑛+1, itrewrote
𝐶
thisasamaximum-heightboundforthepositiveconcavesolution
𝑛!|𝐾|
det(−𝐷2𝑢) = 𝑢−𝑛−2, 𝑢| = 0, ‖𝑢‖𝑛+1 ≤ .
𝜕𝐾 ∞ (𝑛+1)(𝑛+1)/2
Theassistantcheckedsimplexequalityandballslack,thentriedtoevolvethevolumesofthelevelsetsof
𝑢. Itsproposeddifferentialinequalityrequiredtheirnormalspeedtobeasupportfunction;examining
simplexgradientsoverturnedthatrequirement.
VERBATIMEXCERPT
Thus p is *far* from support precisely near simplex, ODE fails drastically, can't bootstrap.
It next integrated the Hessian along a cone ray, 𝐵(𝑦,𝑎) = ∫ ∞ 𝐷2𝐹(𝑦 + 𝑡𝑎)𝑑𝑡, obtaining a chart that
0
becomescoordinatewiselogarithmsontheorthant. InvokingCalabi’snonpositive-Ricciestimate,itde-
riveddeterminantandtracecomparisons,thensketchedacubic-tensorcalculationusingcompleteness
and an Omori–Yau maximum principle [18, 66]. In normalized horizontal coordinates it obtained a
convexfunction𝑓 satisfying
|∇𝑓|2
det𝐷2𝑓 ≥ 𝑒−𝑓, Δ𝑓 + ≤ 𝑛.
𝑑
Theremainingtargetwasalowerboundforthevolumeof∇𝑓(ℝ𝑛). Theassistantrelatedthetwodeficits
througharadialdifferentialidentityandconsideredwhetheranearlyvanishingdeficitforcedsimplex
structure. Gaussianentropytrialsretainedanexponentialloss. MarginalizationtrialsusedPrékopaand
Brascamp–Lieb estimates; the assistant also returned to Bergman-kernel and Kuperberg comparisons
whilelookingforadifferentintegralargument[54,16,50,39]. Finally,ellipsoidalfibersovertheaﬀine-
spheregraphledtoweightedGammaintegralsandaproposedmonotonicityquestion.

GeometricMahlerconjectures 24
25 Canonical comparisons tested beyond the orthant
Theassistantpursuedtheorthant-calibratedinequality
𝜒 (𝑎) = ∫ 𝑒−𝑎⋅𝑦−(𝜈−1)𝐹(𝑦)𝑑𝑦 ≥ Γ(𝜈)𝑑
𝜈
𝐶
for a normalized canonical potential. It compared angular integration by parts with the required
trigamma variance, using Brascamp–Lieb estimates and considering Berwald moment normalization;
its first gradient-moment test left a gap [16, 12]. A translated-barrier vector field reproduced the
orthant identities, suggesting a pointwise divergence bound. The pointwise divergence bound
remainedunproved;theassistantturnedtoweightedorcumulativeaveragesofitsdeficit.
A beta-convolution route paired complementary points and introduced an even potential whose or-
thantmodelwas∑ logcosh𝑠 . ForthepairedaveragedHessian,theassistantusedadeterminantcom-
𝑖 𝑖
parison it had derived assuming Calabi’s nonpositive-Ricci bound [18]. Lorentz-cone calculations re-
versed the proposed trace inequality, while Gaussian trial measures left a nonzero gap even for the
orthant. The assistant considered Vaaler’s cube-section bound, revisited Kuperberg’s graph construc-
tion, and explored diffusion and integrated-Hessian coordinates as alternative ways to compare the
integrals[65,39].
Next it sought an exponential-to-Gaussian quantile map built from positive mixtures of translated
Hessians. The local second variation had the desired sign under the same Calabi curvature bound.
Theglobaltransportcomparisonremainedunresolved,andtheassistantconsideredradialcorrections,
determinantmixtures,andanOnofri-typeenergycomparison.
Laguerretestsledtoatwo-pointHessiantarget,
tr(𝑀(𝑝)−1𝑀(𝑞)) ≤ 𝑝𝑇𝑀(𝑞)𝑝.
The assistant derived a gamma comparison that would follow from this bound. Maximum-principle
calculations gave signs the assistant could not use. Linearizing the orthant potential then produced
mixed signs for some proposed deformation modes; it treated their realization by actual cones as a
furtherquestion.
Theassistantshiftedtowardaverageddeficitsandcomplementarypairs,whilealsorevisitingshadow-
systemconvexity,reverseBrascamp–Liebtransport,andSuita-typekernelestimates[47,8,50]. Gamma-
ratio calculations suggested positive integral corrections despite the changing pointwise signs. For a
symmetric pair it proposed summing the two trace deficits. It continued by asking how the paired
inequalitywouldenterthebeta-convolutionargument.
26 Toric residues and random supporting planes
Theassistantexaminedasymmetrizedbarriercomparisonandnoticedthatboundarytermsprevented
its proposed specialization to uniform density. It returned to Calabi’s nonpositive-Ricci bound in its
trace comparison, but recognized that the Laplacian control did not supply the directional convexity
it wanted [18]. It then represented a rational cone by height-one lattice rays, writing 𝑁 = 𝜒 (𝑣) and
𝐶
seeking 𝑁𝜒 (𝑢) ≥ 1 when 𝑢 ⋅ 𝑣 = 𝑑. The multiplicity–log-canonical-threshold inequality suggested
𝐷
a toric analogue, but it found obstructions to finite smooth covers and to applying local multiplicity
estimatesonresolutioncharts[25].
Adeterminantpolynomialledtozonotopeandrandom-simplexcomparisons. Theassistantrejected
aproposedreciprocal-volumeboundaftercheckingitsdimensionalscaleforaball. Itnextusedpolyno-
mial degree and toric residues to formulate a suﬀicient norm–residue estimate [11]. One-dimensional
examples exposed cancellation and conditioning problems. Replacing the signed trace by geometric

GeometricMahlerconjectures 25
means of inverse Jacobians led to entropy criteria; a linear exponential-map criterion then failed for
crosspolytopes. Its related comparisonsrevisitedreverseBrascamp–Lieb, antiblocking, central-section,
andreverse-isoperimetricbounds[8,59,65,2].
The assistant assigned independent exponential heights to vertices and sampled a cell of the lower
regulartriangulationbyitsvolume. Withrays𝑟 = (𝑝 ,1)andratessatisfying∑ 𝛼 = 𝑑and∑ 𝛼 𝑝 = 0,
𝑖 𝑖 𝑖 𝑖 𝑖 𝑖 𝑖
itset𝑀 = ∑ 𝛼 𝑟 𝑟T. Itcalculated
𝑖 𝑖 𝑖 𝑖
det𝑀
Pr(sampledsupportingplaneisnonnegativeon𝑃) = 𝜒 (𝑢),
𝑁 𝐷
so its target became a lower bound of det𝑀/𝑁2 for this probability. Sparse rates returned it to the
originalpolarintegral. AneventusingthefirstPoissonarrivalsyieldedonlyaslabestimate;comparing
that slab with a difference body and Kuperberg’s bound retained a loss [57, 39]. For random upper
constraintsitalsoobtained𝔼|𝑄(𝑏)| = 𝜒 (𝑢),butrecognizedthatthesesectionspassedthroughacorner,
𝐷
preventingadirectuseofcentralcube-sectionbounds.
TheassistantrecalledBanaszczyk’sEuclideantransferenceboundsandGaussianmethod[4]. Itslat-
ticeargumentsuggestedanothersuﬀicientasymptoticconstant,whichitquestionedthroughsimultane-
ouspackingandsimplexexamples. ItexaminedHilbertseries,toricwallrelations,andradialvariations,
while recalling the covariance and shadow-flow approaches [38, 19]. The crosspolytope obstructed its
hopethatradialstationaritywouldforceasimplex:
VERBATIMEXCERPT
If global min proof must compare all stationary including Hanner.
Italsorevisitedvolumelocalization,polynomial-capacitybounds,andBergman-kernelcomparisons[41,
34,50]. Finally,itdecomposedtherandomsection’snormalconesbyupperandloweractiveconstraints.
Thelower-dimensionaltermsenteredwiththeoppositesignfromtheoneitneededforinduction. Pair-
ingprimal and dualrandomboxesproducedcovariancedeterminants; its spherical calculationcontra-
dicted the proposed guaranteed existence of a mutually maximizing pair with only upper constraints
active.
27 Random optimization and Gaussian replacement formulas
The assistant represented a random linear program on a dual cone by independent exponential
constraint heights. Conditional on an optimizer stratum with 𝑘 active upper constraints, it derived a
gamma law for the optimum and a uniform law on the corresponding normalized face. Rescaling the
heights made the survival event a Minkowski sum of a simplex section with the positive orthant. Its
survival polynomial then had normalized mixed-volume coeﬀicients; the highest coeﬀicient measured
the probability that the optimizer avoided the cone boundary. Complementary section–projection
comparisons using Rogers–Shephard and moment comparisons using Berwald lost the constants the
assistantneeded[58,12].
ItnextcombinedreverseBrascamp–Liebestimateswithacontactcouplinghavingzeromeansandpre-
scribedcross-covariance[8]. Atestusingtwoidenticallyorientedsimplicessatisfiedthesemomentcon-
ditionswhileomittingverticesoftheactualpolar. Theomittedpolarverticesshowedwhythesemoment
conditions alone were insuﬀicient. It examined an associated positive transition matrix, anti-blocking
bodies, andthe convexhullofcontact pairs, comparingthese constructionswithSaint-Raymond’svol-
umeinequalityandKuperberg’slinking-integralapproach[59,39]. Surface-normalcovariancesandav-
eragedHessianssuggestedanotherinterpolation;projectionestimatesagainleftadimension-dependent
loss. ItsreturntoGaussianprojectionsalsorecalledthecovarianceconditionassociatedwithKlartag’s
isotropic-constantapproach[38].

GeometricMahlerconjectures 26
FortheseGaussianspectralcomparisons,𝑑denotesascalarprofileindependentoftheconedimension.
WithstandardGaussiandensity𝜙anddistributionfunction𝑝,write
𝑋 = 𝑝/𝜙, 𝑌 = (1−𝑝)/𝜙, 𝑓 = −(1−𝑝)−log𝑝, 𝑗 = −𝑝−log(1−𝑝).
Theprofileis
𝑑(𝑥) = (1+𝑥𝑋(𝑥))2𝑓(𝑥)+(1−𝑥𝑌(𝑥))2𝑗(𝑥).
ForalinearGaussiansymmetricmatrix𝐿,theremainingspectraltermwas
Δ = 𝔼𝜏𝜓(𝐿)−𝔼𝜓(𝐺), 𝜓″ = 𝑁𝑑,
𝜓
withstandardGaussianscalar𝐺,normalizedtrace𝜏,andGaussiannumberoperator𝑁 = 𝑥𝜕 −𝜕2. The
𝑥 𝑥
assistant explored bounded diagnostic functions, changes of metric, and exact centering of the projec-
tionpath. Inacommutingmodel,exactcenteringappearedtoforceequalvariances. Itthennoticedthat
small matrix errors could contribute coherently across coordinates, so this argument did not immedi-
atelygivethedesiredquantitativebound.
Gaussiandoublingsuggestedexpressingthespectraldiscrepancythroughtwoindependentreplace-
ments. Averaging over variance splits removed the oscillations of a fixed split and gave an auxiliary
profile
𝜑″ = (𝑁 +4)(𝑑−1/2).
∗
In the commuting case, the assistant obtained quadratic Fourier expressions in mean characteristic-
function discrepancies. In comparing noncommuting sums with spectral-overlap averages, the assis-
tantinvokedGolden–Thompsonforrealexponentialsandhyperboliccosines,thenexploredanalogous
tracecomparisonsforitsprofile[29,63]. Italsoinferredasquare-roottracecomparisonfromGolden–
ThompsonthroughaLaplaceintegralandconsideredcombiningitwithalowerKhintchineestimate[29,
63]. Theassistantreturnedtotheexactlayerandcontactidentities,checkedtheiralgebra,andpursued
aDuhamelexpansioninwhichtracesymmetrycanceledafirst-ordercommutatorterm. Itstillneeded
anestimatetyingtheremainingcommutatortermstoitsnonnegativedefects.
28 Commuting evidence and Hessian structure
The assistant pursued a dimension-independent bound for the Gaussian spectral discrepancy, writing
𝐿 = ∑ 𝐺 𝑀 and𝑆 = ∑ 𝑀2. ItcomparedscalarandmatrixOrnstein–Uhlenbeckoperatorsthroughthe
𝑖 𝑖 𝑖 𝑖 𝑖
defect
𝑑̃ = (1+𝑁 )−1(𝑁 ℎ(𝐿)−𝑁 ℎ(𝐿)).
ℎ 𝐺 𝑧 𝐺
It hoped that this defect, together with the Dirichlet gap 𝐽 , would control variance heterogeneity and
ℎ
noncommutativity. Revisiting its own earlier calculations, it considered quadratic maps from pairs of
Gaussians,tailconstraints,andalternativemetricbalances. Arotating-projectorexampleledittoreject
a trace-norm reconstruction bound for arbitrary projection layers and to seek additional control from
conecontactpositivity.
Perturbingthecross-covarianceoftwoGaussianinputs,theassistantderivedaquadratic-testinequal-
ityinwhicharesidualsquarecancelled. Itthenencounteredunboundedtestfunctions, therestriction
to positive covariance decrements, and diﬀiculties controlling matrix errors. It proposed allocating di-
agnostics across dyadic variance scales, but observed that compressing away high-variance directions
couldreintroducelargederivativeerrors. Inthecommutingcase,itconsideredatwo-componentprofile
involvinghyperbolicfunctions.
The assistant next tried to change the balancing condition so that the remaining even discrepancy
woulddisappear. ItsHermitecalculationproducedapositiveadjointcompatibilitycondition,whichit

GeometricMahlerconjectures 27
tookasanobstructiontoamonotonereplacement. Afurtherproposaltooffsetthemeanbyanonlinear
scalar balance failed its own test at extreme scalings. It also derived a resolvent identity expressing a
noncommutativecomparisonerrorasaproductofcommutators,thenfoundthatspectralcancellations
obstructed the desired localization estimate. Revisiting Golden–Thompson, the assistant compared a
square-root matrix trace with a spectral-overlap average, but cautioned against assuming the desired
deterministicsign[29,63]. Hermitetriangularitysuggestedformulasquadraticinlower-chaosleakage;
theassistantfoundthatpositivefactorizationsintroducedpolynomialtailsincompatiblewithbounded
diagnostics.
Returning to the full symmetry of the coeﬀicient tensor, the assistant noticed that the comparison
field in 𝑑 was a Hessian. It therefore used the failure of ∇ℎ(𝐿) to be fully symmetric as an additional
ℎ
contributiontotheDirichletdefect.
It then investigated calibrating 𝑆, diagonalizing an independent Gaussian reference matrix, and fac-
toringaclassicaltwo-variablecomparisonkernel. Itcontinuedtoidentifyanisotropicvariance,transfer
toactualprojectionlayers,andglobalestimatesasobstaclestoitsproposedbound.
29 Parity estimates and the limits of path averaging
The assistant tried angular averaging to factor the Gaussian trace discrepancy into squares of mean
discrepancies. Hermite–Laguerreexpansionssuggestedpositivemomentkernels,butitsTaylorexpan-
sion gave signs incompatible with complete monotonicity of the required scalar profile. It therefore
considered signed representations and approximate profiles. Recalling its reverse Brascamp–Lieb and
aﬀine-sphereroutes,itagainfoundmissingcomparisonsbetweentheprimalanddualquantities[8,18].
It next tried bounded non-Gaussian inputs so that linear diagnostics would remain bounded. For a
cosinedensity,itobtainedaconstantproductofthetwoscalarhazards. Itthennoticedthatthecentered
primal mean reached a finite endpoint while the dual hazard diverged, potentially making the dual
entropycostinfinite. Logisticinputsgavecomplementaryderivativematrices,butthecostcomparison
remainedunresolvedinitscalculation.
ReturningtoGaussianinputs,itsplitthehigher-chaosremainderintoevenandoddparts. Theeven
partbeganatdegreetwoandtheoddpartatdegreethree;theassistantusedthesedifferentdegreesto
assign separate quadratic estimates. It retained more of the companion diagnostic’s square instead of
replacingeverythingbyaconstantbound. Variance-dependentSteinequationsandthresholddecompo-
sitionsthentargetedtheremainingmatrixerrors. OnethresholdCauchy–Schwarzestimatedeveloped
alogarithmicallydivergenttail.
Hessiansymmetrysuppliedanotherterm: theassistantcompareddivideddifferencesalongthethree
edgesdeterminedbyasymmetricthird-ordertensor. Itrecognizedadditionallocalcontrolfromthepart
ofadiagnosticthatwasnotitselfaHessian:
VERBATIMEXCERPT
Thus Codazzi doubles J locally!
In comparing matrix and commuting Gaussian laws, it considered Golden–Thompson and Lieb trace
inequalities,thenexploredanaveragedcommutator-momentestimatenearidentitycovariance[29,63,
42]. Star-shaped matrix examples obstructed its proposed extension to heterogeneous covariance; its
attempteduseofLieb’sconcavityforskewinformationlikewiseleftascalingproblem.
Theassistantfinallyrevisitedpathsthatswitchedfromprimalcenteringtodualcenteringatacutoff.
Itderivedthecutoffboundarytermsandaskedwhetheraveragingthecutoffcouldremovethetrouble-
someprofile. Matchingthecoeﬀicientsofbothbarriersforcedtheiraveragedprofilebacktotheoriginal
one:

GeometricMahlerconjectures 28
VERBATIMEXCERPT
So smooth profiles no help;
It then expressed the Fenchel gap as a squared mismatch of centered projections plus a nonnegative
contactterm. FromanidenticallyzerogapitrecoveredtheGaussianrankprofile. Forsmallgaps,how-
ever,itnoticedthatscalarbarrierperturbationscouldchangetheentropyexpressionatfirstorderwhile
changing the gap only quadratically. It turned to the vector mean constraints and independently cen-
teredprimalanddualmapsforadditionalcontrol.
30 Variance rigidity, large spectral rows, and smoothing
The assistant compared independently centered primal and dual projection paths, then tried a deter-
ministicshiftwithacommonmeanresidual. Cancellingitsintegralinacommutingmodelforcedunit
spectralvariances,butitstillneededacalibrationrealizingthatcancellation. Anisotropicallyscaledor-
thantsdefeatedtheproposedentropytangent. Acontactidentityrelatingmeanranktocovariancesug-
gested another route: exact reflection parity would force the Gaussian profile. Its quantitative version
encountered a positive adjoint compatibility condition, while scale-dependent Fourier tests recreated
theunboundedtriangular-kernelobstruction.
Theassistantnextaskedwhetherhigh-variancerowsofaGaussianmatrixcouldretainadefiniteag-
gregatefractionoftheirvarianceinthediagonalof𝔼|𝐿|. Star-shapedexamplesruledouttheindividual-
rowestimate. ItconsiderednoncommutativeKhintchineduality[45],thengroupedvariancesbydyadic
scaleandchargedinteractionswithlargerrowsthroughtheirrank.
Positive-partspectraltestsofferedasecondapproach,usingthePowers–StørmerinequalityandDou-
glas factorization [53, 23]. The assistant estimated the constants needed by its entropy argument and
foundthatasmallpositiveuniversalboundwouldnotsuﬀice.
ItreturnedtoGaussianregularizationofconeLaplaceintegrals. Optimizingprimalanddualmetrics
matchedposteriorcovariances,buttheresultingHessiancontainedthird-momentcorrections. Reexam-
iningitsearlierscalartruncated-Gaussianargument,itdistinguishedthatcalculationfromthemultidi-
mensionalbounditstillsought. TherecalledapproachesusedEhrhard’sinequalityandBrascamp–Lieb
estimates[24,16],CaffarellicontractionandBorellnoisestability[17,14],andBerwald’smomentcom-
parison[12];theassistantcontinuedtoencountertensororconditional-centeringobstructions.
Its review also returned to Klartag’s covariance framework [38], canonical Cheng–Yau barriers and
Calabi curvature estimates [20, 18], and reverse Brascamp–Lieb bounds [8]. Kuperberg’s symmetric
boundandSaint-Raymond’sinequalityremainedpossibleinputstolifts[39,59],buttheassistantnoted
thatfixedexponentiallossespreventeditsproposedtransferfrombeingsharpatthesimplex.
Moreaudecompositionexpressedtheproductintegralthroughtranslatedprimal–dualintersections.
The assistant checked that replacing each intersection by the fixed cone intersection was exact for the
orthant, then found that this replacement could discard needed slack for other models. A proposed
covariancemonotonicitymetamoreexplicitobstruction. For
2𝑎+𝜆
𝐶 = {(𝑧 ,𝑧 ,𝑥) ∶ 𝑧 ,𝑧 ≥ 0, 0 ≤ 𝑥 ≤ 𝑧 +𝑧 }, 𝜒 (𝑎,𝑎,𝜆) = ,
1 2 1 2 1 2 𝐶 𝑎2(𝑎+𝜆)2
itdifferentiatedtwicein𝑎andthenin𝜆. Thevarianceof𝑧 +𝑧 increasedwhen𝜆wassuﬀicientlylarge,
1 2
anditrejectedtheuniversalcurvatureprinciple:

GeometricMahlerconjectures 29
VERBATIMEXCERPT
Thus T_v not PSD globally.
The assistant then proposed realizing smoothing by higher-dimensional cone lifts, hoping to turn
covarianceimprovementintoamplificationofahypotheticaldeficit.
31 Canonical entropy and the failure of scalar induction
The assistant first reconsidered perturbations of product cones, then compared maximal entropy on a
conewithitscanonicalpotential𝐹,normalizedbydet𝐷2𝐹 = 𝑒2𝐹. Itsintendedsuﬀicientinequalitywas
𝐻 (𝑦)+𝐹(𝑦) ≥ 𝑑. It relied on Cheng–Yau completeness and a Calabi curvature calculation, and used
0
Brascamp–LiebvarianceestimatestoorganizeGaussianregularizationatfixedmeanintoapositivetrace
term,anegativesquare,andvariancedeficits[20,18,16]. Completingthesquarestillleftaggregatecon-
trolofthirdmomentsunresolved. Covariancecapsmadethecovarianceisotropicwheneverydirection
wasactive;inactivedirectionsandmixedprecisiontermsremainedobstacles.
Itthencalibratedaspectralpenaltyagainstthehalf-lineentropyprofile. Testingoff-diagonalprecision
matricesonanorthantreversedthedesiredcomparison:
VERBATIMEXCERPT
Thus J negative near non-diagonal orthant! Not valid for all Q.
The assistant next pursued one-dimensional slices. Retaining the variation of the maximizing eigen-
vectorinaBochnercalculationledittoannounceatwo-functionalbound. Itusedthistorestrictrecip-
rocal endpoint distances and attempted to compare interval entropy with half-line entropy, leaving an
elementaryhyperbolicinequalityandadampingargumenttoprove. PartialLegendreeliminationthen
exposedafailureofdimensionalinduction: anobliquefirstsliceofanorthantgivesastrictsurplus,al-
thoughthetotalorthantentropyisexact,sotheremainingfactormustfallbelowtheproposedinductive
target.
VERBATIMEXCERPT
So iterative scalar ≥e false.
Furthercovariance-capcalculationscontrolledradialthirdmomentsbutlefttransversecontributions
unresolved. The assistant explored approximate simultaneous diagonalization of the canonical cubic
tensor, including a reformulation in terms of completely positive maps, to relate these contributions
tocurvature. ItalsorevisitedreverseBrascamp–Liebestimates,hyperplane-symmetryarguments,and
Saint-Raymond’santiblockinginequalityfromitsearliercalculations,withoutfindingthemissingcom-
parison [8, 7, 59]. A gradient-coordinate approach led it back to moment-measure equations [21]. Its
proposed containment by a spectrahedron defined by the cubic tensor failed on centrally symmetric
nonsphericalsections.
The final sustained pivot used the symmetric order interval 𝐾 = {𝑧 ∶ 𝑎±𝑧 ∈ 𝐶} and a beta-integral
comparison, with the orthant as the equality model. The assistant considered whether Kuperberg’s
symmetricvolume-productboundcouldhandlesuﬀicientlyroundcases[39]. Symmetryremovedodd
posterior moments, but determinant control alone admitted radial constructions below the intended
constant. Splitting the averaged chord Hessian into two halves then gave the assistant a trace bound:
afternormalizing𝐷2𝐹(𝑎) = 𝐼,itobtainedtr𝑃 ≤ 𝑑fortheinverseaveragedHessian𝑃. Itendedbytrying
tocombinethistraceboundwithdeterminantslackandfinite-parameterbetaestimates.

GeometricMahlerconjectures 30
32 Beta convolution and failed positivity certificates
Theassistantcontinuedthecanonical-potentialroute,invokingCheng–Yaucompleteness,Calabi’sRicci
estimateandanOmori–Yaumaximumprinciple[20,18,66]. With𝐹(𝑎) = 0and𝐹″(𝑎) = 𝐼,itsought
𝐼 (𝑎) = ∫ 𝑒−2(𝜈−1)𝑈(𝑧)𝑑𝑧 ≥ 𝐵(1/2,𝜈)𝑑, 𝑈(𝑧) = 1 (𝐹(𝑎+𝑧)+𝐹(𝑎−𝑧)).
𝜈 2
𝑎±𝑧∈𝐶
It calculated that the corresponding convolution inequality would give 𝑅2 ≥ 𝑅 ; a saddle-point limit
𝜈 2𝜈
would then give the desired cone bound. In its gradient coordinates, an inverse averaged Hessian 𝑃
produced the correction 𝜃 = logdet𝑃 + 2𝑈. Splitting the chord into halves expressed this correction
throughthreenonnegativeterms.
Ithopedsmallslackwouldpermitapproximationbycommutingmatricesandtheorthant’sproduct
density, but still needed quantitative control. Optimized Gaussian trial laws did not reach the orthant
constantat𝜈 = 1. Aproposedpointwisebounddemandedafourth-derivativeinequalitytheassistant
couldnotjustify. Vinberg-coneboundaryasymptoticsalsoledittorejectaGaussian-quantilecertificate
for some exponents. Revisiting reverse Brascamp–Lieb and Saint-Raymond arguments did not supply
itsmissingcomparison[8,59];ordinaryBrascamp–Liebcovariancecontrolgaveaweakerconvolution-
Hessianestimateevenontheorthant[16].
Integration by parts next yielded an ordinary differential equation with an extra term whose sign
wouldcontrol𝔼(2𝑈). Formalperturbationsoftheorthantproducednegativefirstvariations. Integrat-
ing against a positive Green weight still left adverse boundary examples. It changed the determinant
weight:
VERBATIMEXCERPT
w=0.5 may fix both:
The half-weight represented Riemannian volume for the averaged Hessian. Subsequent spectral de-
compositionsisolatedpositivelogarithmicterms,whiletheirexpectedvaluesremainedtobecontrolled.
Theassistantalsowithdrewaderivativeestimateaftertestingthedilationdirection:
VERBATIMEXCERPT
Oops B_gamma HS bound impossible unless θ gradient zero:
It then used stationarity in the center to derive endpoint moment constraints, revisiting the covari-
anceviewpointassociatedwithKlartag[38]. APoissonequationrepresentedtheconvolutionHessian
through transport energy. Determinant concavity led back to an entropy expression with the opposite
variationaldirectionfromtheoneneeded.
Attheuniform-densityendpoint,theassistant’sgradient-coveringargumentlikewisegaveanupper
bound. Kuperberg’s estimate left the same constant gap in its difference-body calculation [39]. It fi-
nallyturnedtovaryingtheconeitselfandwrotethetransformedMonge–Ampèreequationforshadow
deformations,askingwhichcomparisondirectionthefiberinterpolationwouldprovide.
33 Amplification and almost-pyramidal reduction
The assistant first tried a partial Legendre transform of a shadow deformation, but the resulting de-
terminant comparison did not give the interpolation inequality it needed. It then sought to amplify a
hypothetical Mahler deficit through products and canonical-potential truncations. An explicit barrier

GeometricMahlerconjectures 31
gave a determinant estimate with a polynomial loss; the assistant noticed that the induced concentra-
tionboundbecameeasiertosatisfywhenthecharacteristicvolumewassmall. Dualtruncation,viewed
as primal expansion, led it back to the same direction of comparison. A collective concave constraint
on a product cone gave a proposed multiplier involving a Chernoff bound and a weighted Minkowski
volume. RadialintegrationexpressedthatmultiplierthroughpolarMinkowskisums,andtheassistant
recognizedtheoriginalMahlerminimizationinsidetheproposedamplification.
It next reconsidered random simplex determinants and stationary boundary couplings. Indepen-
dent sampling lost the probability of selecting distinct simplex vertices, while squared determinants
brought it back to covariance estimates. Its comparisons recalled Klartag’s isotropic-constant frame-
work, reverse Brascamp–Lieb and reverse-isoperimetric bounds, Kuperberg’s symmetric estimate, and
centroid-sectionestimates[38,8,2,39,27]. Italsorevisitedshadowsystemsandthethree-dimensional
argument[47,19]. Whileseekingadeformationbeyondtheavailablestationarityidentities,itrecalled
curvaturerestrictionsonlocalminimizers[56].
Forabodyclosetoapyramid,theassistantchoseoppositeextremalpointswithasymmetryparameter
𝑠 ≤ 𝑛. A perspective change of the section height produced sublevel bodies 𝐿 = {𝑓 ≤ 𝑥} and 𝑀 =
𝑥 𝑦
{𝑓∗ ≤ 𝑦} in dimension 𝑛 − 1. It derived weighted formulas for both volumes and isolated a prefactor
minimizedat𝑠 = 𝑛. Applyingthelower-dimensionalMahlerbenchmarkleftaproductofexpectations:
primalmasssampledsmallheights, whereasthedualintegralsampledmuchlargerones. Mixturesof
directionalthresholdsdefeateditsfirstscalarcomparison,soitsoughtcompensationfromthegeometry
ofthelevelbodiesandtheircenters.
Withsymmetricallyrescaledheights𝑔,ℎand𝑟 = 𝑛/𝑠−1,theassistantobtainedanenvelopeestimate
that avoided its earlier tail-divergence objection. It then revisited the scaling Hessian condition in the
exponentiallimitandderived
Var(𝑔)+Var(ℎ) ≥ 2𝑟.
VERBATIMEXCERPT
This kills mixed small-threshold model (both variances O(r²)!);
It compared this constraint with information-content variance bounds [28], but rare large heights and
theheightsofcontactingboundarypointsstillescapedthecontrolitsought. Itpursuedsize-weighted
contactcouplingsandclipping variationswithoutobtainingthe proposednear-pyramidinduction. Fi-
nally,itturnedtothenonnegativekernel𝑇(𝑝,𝑞) = 1−𝑝⋅𝑞: itsspectrumsuggestedacomparisonbetween
nearlyEuclideancomponentsandcomponentsresemblingjoins,whilereverseBrascamp–Liebstillleft
acovariancedeterminanttorecover.
34 Random heights and unused entropy slack
The assistant returned to contact geometry and rejected a fixed-sign rule for products of primal and
dualsimplexdeterminants: afour-by-fournonnegativeslackmatrixwithzerodiagonalcouldhavethe
opposite determinant sign. It found that taking absolute values discarded cancellations needed at the
simplex. RevisitingdirectandreverseBrascamp–Liebtransport,itsoughtextradeterminantgainfrom
nonorthogonalframes,butfoundneitheritsGaussianconstructionnoritsinballestimatecontrolledthe
intermediatecovarianceregime[16,8]. Italsoreconsideredtheshadow-flowobstruction,Kuperberg’s
linkingconstruction,andRogers–Shephardcomparisons[19,39,57].
Triangulating a cone led it to an entropy formulation. A basis had probability proportional to its
absolutedeterminant,anditsinclusionprobabilitiessuppliedratesforindependentexponentialheights.
Integrating the height residuals related the probability of a lower supporting plane being nonnegative
tothedualLaplaceintegral. Fortheresultingrandomlinearprogram,itwrote:

GeometricMahlerconjectures 32
VERBATIMEXCERPT
Conditional on "good", density \(y\sim Exp_D(u)\) independent of x!
Theassistantstillneededaprobabilityestimatefortheweightedtriangulation, ratherthanasumover
all bases. It connected the construction to a zonotope and its normal cones, hoping to use the zonoid
volume-productinequality,butsuspectedthatitsproposedlocalcomparisonmerelyrestatedtheorigi-
naldiﬀiculty[55].
ItnextsoughtamatrixextensionofBorell’sGaussiannoise-stabilitycomparison[14]. ProjectionHes-
sians and their rank-one jumps across polyhedral walls offered additional structure. Scalar rearrange-
mentgavedirectionalmeanbounds,buttheassistantfoundthatapositivedecompositionoftheidentity
using directions from both cones would already impose simplicial structure. It also recalled local sim-
plexminimality,whilenotingthedimensiondependenceofthatapproach[37].
TheassistantthenauditeditsearlierHardy–entropyargument: convexificationofthecostcurve,met-
ricbalancing,GaussianPoincaréestimates,endpointintegrability,andsmoothingofthetransportmaps.
Anonzeroentropycorrectionremained.
ReturningtoKlartag’sprojectivecovariancecondition[38], itlookedforunusedrelativeentropybe-
tween its transport laws and tilted cone laws. Unequal coordinate rates might create a useful mean
discrepancy. Splitting exponentials into independent gamma variables preserved the orthant distribu-
tion,butconditioningontheirproportionsproducedJacobianswhosepositivityandinjectivityitcould
notcontrol.
Finally,cumulativepositivematricesgaveitaproposedlogarithmic-determinantcomparisonwithout
simultaneousdiagonalization. Itsreactionwas:
VERBATIMEXCERPT
exact rearrangement! Orth equality when support pure threshold simultaneously; no dephasing. Nice.
Itdevelopedcompactmetricperturbationsandpositivespectraltailjumps,usingconditionalGaussian
averaging to estimate their entropy gain. Its remaining tasks included controlling finite perturbations,
intermediatevariances,tailconstants,andtheequalitycase.
35 Anisotropic inputs and quadratic layer control
TheassistantreturnedtoitsearlierscalarHardyandmatrix-diagnosticcalculations,seekingtheentropy
gain that those estimates had left missing. It examined constant and varying projection metrics, with
the mean of each projected Gaussian still constrained to a prescribed ray. A constant metric gave a
matrixdiagnosticequaltotheidentityintheorthantmodel. Theassistantsoughtauniformboundfor
itsresponse,especiallyonsmallsubspaceswithlargecovarianceeigenvalues.
For a varying metric, it found that an odd coeﬀicient would cancel the reflected covariance term of
theidealspectral-thresholdfamily,includingnoncommutingthresholds. Transferringthatcancellation
totheactualprojectionsledtoinversespectral-distanceweights:
VERBATIMEXCERPT
Log divergence near z=λ_i.
Ittriedsubtractingthresholdvalues,integratingmatrixprimitivesatcolumn-dependentcutoffs,andus-
ingnonnestingandcommutatorestimates. Theassistantcouldnotobtaintheneededuniformestimate
fromthesereformulations.

GeometricMahlerconjectures 33
It then reconsidered polynomial diagnostics, alternative input distributions, and its earlier doubling
argumentfortheGaussianmatrixseries. Polynomialderivativesintroducedweightederrorsbeyondthe
availabledeficit;smoothingchangedtheorthantequalitycalculation. Theassistantalsorevisitedcone-
contactinequalitiesatindividualpairsofthresholds,hopingtheirsignswoulddistinguishmixturesof
differentvariances. Itrepeatedlyencounteredtransfererrorsproportionaltothesquarerootofadeficit.
AchangetotheGaussianinputcovarianceproducedanewfirst-variationcalculation. Forcovariance
𝐼+𝐸,itexpressedthevariationusingonlythemeanprojectionHessian𝐻 ,with𝑗 = 𝐴/Φ:
𝑧
1
𝜏𝐸[ 𝐼−∫𝑗(𝑧)𝑗′(𝑧)(𝐼−𝐻 )𝑑𝑧].
2 𝑧
The assistant regarded this as a simpler moment diagnostic, but its attempts to control a finite pertur-
bationencounteredconcentratedresponsesandtailterms. Matchingtheprojectionmetrictotheinput
transformation left diagonal orthant projections unchanged, which prompted it to seek estimates that
retainedthisexactcancellation.
Ratherthancontinuecomparingtwochangingprojectionpaths,theassistantrebuiltthecomplemen-
taryidentitiesatananisotropiccovarianceΣ = 𝐼+𝑇. Itseparatedtheweightedtracedefiningthemean-
rank measure from the ordinary trace used in the spectral-layer estimates. When it allowed 𝜏Σ ≠ 1, it
noticedthatitsformulasneededadditionalcenteringconstantsandcorrectedthem. Positivecovariance
directionscouldbetestedthroughconecontact;negativedirectionsstillrequiredanupperestimatefor
aquadraticlayererror.
For that error, the assistant subtracted a positive kernel within each side of a spectral threshold. It
foundthattheremainingkerneldecayedinthetails:
VERBATIMEXCERPT
Thus no divergence for **quadratic** unlike saturated.
Itthenproposedcontrollingtheremainderbythesquarerootofthemisalignmentdeficittimesacom-
mutatornorm,andcomparingthatcostwiththeremainingentropyestimates. Itcontinuedworkingout
thisboundanditsconstants.
36 Riccati cancellation and explicit Gaussian profiles
Theassistantcontinuedtheadaptive-covarianceapproach,writingtheintegratedprojectionstatisticas
𝐴 = 𝐿 + 𝑅 and the covariance as 𝐼 + 𝑇. It checked that the trace identities survived insertion of the
covariance,butfoundthattheweightedJensendefectcouldhaveeithersign. Anevencompanionand
boundedoscillatingdiagnosticsweremeanttocontrolendpointerrorswithoutconsumingtheavailable
layerestimates.
AnegativescalarSteinprofileledtheassistanttochoose𝑇 throughamatrixRiccatiequation,
𝜆𝑇2+sym(𝑇𝐶) = −𝐷.
It derived a cancellation of the leading variance discrepancy and sought to use the resulting quadratic
penalties to absorb the remaining terms. Moving the main quadratic layer calculation from 𝐿 to the
fullstatistic𝐴letitchargeanerrortononnestinginsteadofusingonlythesmallerprojection-mismatch
allowance. It also retained the weighted residual term long enough to cancel part of the covariance
correction.
Theassistantnextexaminedthescalaridentitiesunderlyingtheconicformulation. WiththeGaussian
ratios𝑋,𝑌 andlogarithmicfunctions𝑓,𝑗definedabove,thecompanionprofilesare
𝑔 = 1 (1−𝑋2𝑓 −𝑌2𝑗), 𝑣 = log(𝑋𝑌).
2

GeometricMahlerconjectures 34
FortheGaussiannumberoperator𝑁,itrecovered(𝑁 +2)𝑔 = 𝑑togetherwith
2𝑔′ = 2𝑧𝑑−𝑑′−𝑣′.
The assistant used this identity to express the resolvent profiles directly through Gaussian densities,
distribution functions, and logarithms. In particular, it obtained 𝑟 = −𝑑 −𝑔″, expressing the Riccati
0
profileinexplicitfunctions.
Its equality discussion depended on strict residual estimates: it reasoned that equality would force
𝑇 = 0, commuting coeﬀicient matrices, and vanishing projection mismatch. A coordinatewise cone
projectionwouldthenidentifyanorthantandhenceasimplex. Italsorevisitedsmoothingandboundary
termsforarbitrarycones.
Next,apointwiseweightedCauchyestimatecombinedthesame-sideandopposite-sidelayerintegrals
intoacoeﬀicientinvolvinglog2+1/4. Theuniformscalarboundsremainedtobeestablished.
It explored small-interval derivative estimates, hyperbolic coordinates for the rotating diagnostics,
andtailboundsfromMills-ratiointegrals. Thediﬀicultywastocontrolintermediateintervalsandcan-
cellationinthetails. Theassistantthensoughtanalyticestimatesforthoseremainingterms.
37 Scalar estimates and renewed algebraic scrutiny
TheassistantpursueduniformGaussian-profileinequalitiesinthecoordinate𝑥 = 3.6sinh𝑡. Itusedthe
profiles K = 𝑑 − 2𝑔 and C = −𝑑 + 6.5𝑔″, also written 𝐾,𝐶, and combined their Mills-ratio formulas
withcomplex-stripestimatesandanalyticinterpolationbounds. Theproposeddivisionseparatedshort
endpointintervals,acompactregion,andtails. Peanokernelsimprovedtheshort-intervalestimates;for
thecompactregion,theassistantretainedcorrelationsbetweenprofilesinsteadofaddingtheirseparate
maxima. Italsocorrecteditsinterpolationplantoaccountforthefactthatthetwocoordinatecurvatures
couldattaintheirmaximaatdifferentpoints.
Itthenrederivedthecone-projectionandentropyidentitiesbeforecontinuingthescalarestimates. In
thisaudititidentifiedthepositivecovariance-contacttermastheexpectedinnerproductoftheappro-
priately ordered primal and dual projections, correcting a description in its own earlier reasoning. It
checked the matrix Stein calculation’s endpoint ordering: the outer eigenvalue supplies the endpoint
value of 𝐶, while the shared eigenvalue supplies the endpoint of the squared probe difference. This
ordering determined the sign in the asymmetric endpoint term. It also revisited the Riccati equation,
commutatorestimates,andtheproposeddeductionoforthantrigidityfromequality.
For the scalar estimates, the assistant studied zero-free complex strips, Gaussian-tail bounds, and
interpolationerrors. Itretainedcorrelatedprofileestimates,whichwereneededtocontroltheendpoint
termsuniformly.
Theassistantassembledthescalarestimatesandaddedtailboundstotheargument.
38 A conditional proof chain and its remaining obligations
TheassistantdevelopedthesegmentestimatelinkingaveragesofthescalarprofilesK,Candarotating
diagnostic𝑢 = (𝜋,𝑞)tothevarianceof𝑢. Here
𝑏 = .602, 𝑐 = .365, 𝑘 = √𝑏−𝑐, 𝑟 = .22, 𝑞(𝑥) = 𝑘−√𝑏−𝑟2−𝑑(𝑥).
In the coordinate 𝑥 = 3.6sinh𝑡, the circular component is 𝜋(𝑡) = 𝑟(cos(4.6𝑡),sin(4.6𝑡)). It separated
shortintervals,analytictails,andacompactregion,seekinguniformcontrolofsecondderivativesand
endpointerrors.

GeometricMahlerconjectures 35
TheassistantreconstructedtheconereductionandtheGaussianargument. Fortheconeover𝐾 −𝑧,
indimension𝑚 = 𝑛+1,itcalculated
(𝑛!)2|𝐾||(𝐾−𝑧)∘|
𝜒 (𝑉)𝜒 (𝑈) = .
𝐶 𝐷 𝑚𝑚
ItsoughtalowerboundofonebyintegratingbiasedcomplementaryprojectionsagainstGaussianhaz-
ardweights. Itreplaceddirectdifferentiationofthefullintegralsbytruncationfollowedbysmoothing,
thenworkedthroughthelog-Jacobiansurplusandtheentropycosts. Itsproposedsurpluscontributed
𝑁/8, where 𝑁 integrated the nonnegative kernel measuring failure of the projection derivatives to be
nested.
The subsequent reconstruction kept the covariance Σ = 𝐼 + 𝑇, the change of metric, and the pro-
jection bias separate. The assistant used a simultaneous fixed-point argument to seek zero mean for
theintegratedderivativefieldandamatrixRiccatiequationfor𝑇. Itrederivedthecovariance, contact,
andlayeridentities,checkedtheorientationofmatrixindices,andsplittheresidualintoevenandodd
Gaussiandegrees. Geometricsubtractiononthetwosidesofaspectralthresholdproducedtheconstant
2log2−1/3;anotherintegralgavelog2+1/4. Theseestimateswereintendedtopayforcommutators
andleavethesegmentvarianceavailableforthefinalcomparison.
The assistant assembled a draft in which the Riccati identity supplied a quadratic penalty of at least
1.94𝜏𝑇2,againstastatederrorallowanceof1.8𝜏𝑇2. Itarguedthatequalitywouldforcethecoeﬀicient
matrices of the linear Gaussian field to commute and the projection mismatch to vanish, making the
coneprojectioncoordinatewiseanditsimageanorthant. Itthencalculatedthesimplexvolumeproduct
directly.
39 Recovering variance in the scalar estimates
Fortransformedendpoints𝑚−ℎ,𝑚+ℎ,with𝑥 = 3.6sinh𝑡,theassistantusedphysicalaveragingwith
densityproportionaltocosh𝑡. Itscircle𝜋(𝑡) = .22(cos(4.6𝑡),sin(4.6𝑡))providedvarianceagainstwhich
it charged the chord error of 𝐾, endpoint differences, and squared discrepancies involving 𝐶,𝑞. Sepa-
rate estimates lost correlations between derivative and curvature profiles. It tried joint rearrangement,
Hölderbounds,andpiecewisesecantmajorantsforsquaredaverages.
Theassistantthenreturnedtovarianceomittedfromitssuﬀicientinequality:
VERBATIMEXCERPT
Maybe improve variance term by using discarded q variance.
Itset𝑞 = (𝑞 −𝑞 )/2,𝑒 = 𝑞̄−(𝑞 +𝑞 )/2,and𝑉 = 𝑞2−𝑞2̄ ,obtaining
𝑑 + − 𝑞 + − 𝑞
𝑏 = 𝑉 +𝑒2+𝑞2, 𝑏 = −2𝑞 𝑒 .
𝑎 𝑞 𝑞 𝑑 𝑑 𝑑 𝑞
It observed that the endpoint penalty left a subtraction of 𝑉 , while expanding the residual squares
𝑞
consumedonlypartofthatsubtractionunderitsproposedbounds. FromaLipschitzboundon𝑞anda
lowerboundontheaveragingdensity,itderivedacubiclowerestimateforvarianceintermsofendpoint
displacement. Italsoexaminedtheextracircularvarianceproportionalto𝐵2sech 2 𝑚. Thesegainsledit
ℎ
backtowardsimplerseparateprofileestimates.
The assistant next sought concentration bounds of the form ∫ 𝐴 ≤ 2𝐻(𝛼 − 𝛽𝐻) for |𝐸| = 2𝐻. It
𝐸
reducedthemtoexcessintegrals∫(𝐴−𝑧) ,andusedlayer-cakeintegrationtoboundweightedaverages.
+
Forlargerintervalsandintervalscrossingzero,itexpressedaveragesthroughweightedprimitivesand
compared the endpoint correction with a one-variable function. It continued choosing thresholds and
estimatingchorderrors,approximatemonotonicitytolerances,andtheremainingcorrectionsneededto
establishuniformbounds.

GeometricMahlerconjectures 36
40 Bernstein positivity and the conditional cone reduction
Theassistantsoughtscalarboundsthroughconcentrationestimates,primitivebounds,andpolynomial
inequalities. Formiddlewidths.16 ≤ ℎ ≤ .54,itretainedthevarianceof𝑞,obtaining
𝑉 𝑞 (ℎcothℎ−ℎ)𝑧3 |𝑞 + −𝑞 − |
≥ , 𝑧 = .
ℎ2 3⋅.193 2ℎ
Itusedthiscubicgaintoabsorbendpointpenalties,thenmultipliedtheremainingdeficitsby(sinhℎ/ℎ)2
to remove hyperbolic denominators. Taylor bounds reduced the remaining estimates to positivity of
polynomials of degrees 30 and 32. It handled larger widths through concentration, monotonicity, and
sign-dependentangularbounds. Therequiredpositivityoftheresultingpolynomialsremainedpartof
thescalarestimate.
Itthenrereaditsgeometricargumentfromthebeginning. With𝑚 = 𝑛+1,thecone𝐶overatranslated
bodyanditspositivedual𝐷reducedtheproposedboundto
𝜒 (𝑉)𝜒 (𝑈) ≥ 1, 𝑈 ∈ int𝐶, 𝑉 ∈ int𝐷, 𝑈⋅𝑉 = 𝑚.
𝐶 𝐷
TheassistantcheckedbiasedGaussianprojectionsrealizingprescribedmeans, theirtailestimates,and
a Brouwer argument choosing coordinates and a covariance perturbation. It corrected wording that
appeared to give 𝑝𝑟 the same total mass as ℎ′(𝑧)𝑑𝑧: the former was asserted to be integrable with all
1
moments,whilethelatterhadmass𝑠 .
0
The audit followed the entropy estimate through truncated, smoothed projection maps, positive Ja-
cobians, and Gaussian covariance identities. The assistant rederived the decomposition 𝐴 = 𝐿 + 𝑅,
separated the even and odd parts of 𝑅, and checked how weighted Cauchy–Schwarz estimates and a
matrix Riccati relation paid for the terms involving matrices that did not commute. The argument re-
mained conditional on the scalar inequalities; the assistant continued checking signs, constants, and
equalitydeductions.
For equality, the assistant reasoned that diagonal support of the endpoint measure would force the
coeﬀicientsof𝐿tocommute,whilevanishinglayererrorwouldmaketheprojectionderivativediagonal.
Itexplicitlyidentifiedthenextstep:
VERBATIMEXCERPT
Need argument all j≠i simultaneously yields dependence only i, continuity extends full slices.
Itusedmollificationandvanishingcrossderivativestoobtaincoordinatewisedependence,thenaprod-
uct cone, an orthant, and a simplex section. Finally, it returned to complex-strip interpolation, profile
derivatives,andthetailexpansion.
41 Following the error estimates from tails to middle widths
Theassistantcontinuedcheckingthescalarestimatesforitsproposedprojection-fieldargument. With
𝜉 = 𝑥−2 and𝐷 = 𝑥𝜕 ,itdifferentiatedLaplaceintegralsthroughorderfourandusedbinomialconvolu-
𝑥
tiontotrackproductsofderivativebounds. ItcheckedtheresultingestimatesforK,𝑑,andC,including
thesquarerootdefining𝑞. Forthepositive-partintegralbeyond64,itusedK(𝑥) ≤ 𝑥−2log𝑥.
Under 𝑥 = 3.6sinh𝑡, uniform physical-length averages acquire a cosh𝑡 weight. The assistant inte-
grated the circular component explicitly, obtaining a lower bound 𝑓∗ for its variance, and derived a
0
positivechordkernelfortheaveragingerror. Forhalf-widthℎ ≤ .16,itboundedthejointcurvatureand
endpointcostby.54𝑢 ,where𝑢 = 𝑟2𝑤2ℎ2/3;itsremainingallowancewasapproximately.555109𝑢 . It
0 0 0

GeometricMahlerconjectures 37
thencheckedthreetailconfigurations,usingpositive-partintegrals,narrowprofileranges,andconvex-
itytoleaveaboundedmiddleregion.
Forthatregion,theassistantusedthresholdintegralstoboundconcentrationandintegratedpiecewise
linearprofilestoestimateweightedprimitives. Almost-monotonicityestimatescontrolledendpointdis-
crepancies. Retainingthescalarvariance𝑉 ,ratherthandroppingit,gave
𝑞
𝑣 𝑧3 |𝑞 −𝑞 |
𝑉 /ℎ2 ≥ ℎ , 𝑧 = + − , 𝑣 = ℎcothℎ−ℎ.
𝑞 3⋅.193 2ℎ ℎ
It reduced the excess cost to a cubic maximization and reported 𝑅/ℎ2 ≤ .027. Hyperbolic and trigono-
metric expansions then produced deficit polynomials of degrees 32 and 30; it reduced their positivity
on[.16,.54]toBernstein-coeﬀicientinequalities. Forlargerwidthsitseparatedsignsoftheangularterm
andcheckedtheroundederrorboundsindividually.
42 Checking transport, noncommutation, and equality
The assistant continued checking the scalar estimates and the cone argument. It bounded Gaussian
tails,differentiatedtheprofiles𝑑,𝑔,K,C,𝑞,andexaminedthepositivityneededbeforetakingthesquare
rootin 𝑞. Concentrationestimatesand polynomialbounds wereused toorganizetheremaining scalar
inequalities.
Itthenrederivedtheconenormalization: with𝑚 = 𝑛+1,positivedualconesand𝑈⋅𝑉 = 𝑚,thetarget
became 𝜒 (𝑉)𝜒 (𝑈) ≥ 1. For the biased Gaussian projection field it checked coercivity, positivity of
𝐶 𝐷
the smoothed Hessian, tail convergence, and continuity under changes of coordinates. The covariance
choiceΣ = 𝐼+𝑇usedamatrixsquarerootandafixed-pointargument;theassistantexplicitlyexpanded
thequadraticrelationwithoutassumingthatitsmatricescommute.
Truncation and Gaussian smoothing gave the maps whose Jacobians entered its entropy calculation.
Ittrackedthedeterminantfactors,changeofvariables,conditionalaveraging,andintegration-by-parts
terms. The orthant served as a check: its projection layers became spectral thresholds, the residual
vanished,andtheproposedentropyidentitiesmatchedthereferencecase.
The assistant also rederived the Gaussian covariance identities through Hermite expansions, intro-
duced positive measures on layers and spectral pairs, and checked the commutator estimates used to
absorbnoncommutingerrors. Itsequalityargumentmadethecoeﬀicientmatricescommute,thenmade
theprojectionderivativediagonalinafixedbasis. Vanishingweakcrossderivativesledittoacoordinate
productcone,henceanorthantandasimplexsection.
Inrevisitingpriorwork,itdistinguisheditsconenormalizationfromthecovarianceandHessianideas
ithadexaminedinKlartag’swork[38]. Itreturnedtocomplex-stripnonvanishing,Cauchyinterpolation,
andGaussian-tailexpansionsinthescalarestimates.
43 Scalar positivity and the scope of the cone reformulation
The assistant audited the scalar estimates by separating short segments, tails, and middle widths. It
checked the circle averages, the weighted trapezoid kernel, concentration bounds, and errors in the
weighted primitives. In the middle range it retained the variance of 𝑞: a bound on |𝑞|̇, together with
a lower bound on the averaging density, gave a cubic lower bound for that variance in terms of end-
pointdisplacement. Afteraccountingfortheresidualsquares,itreducedtheremaininginequalitiesto
positivityoftwopolynomials,forwhichtheBernsteinbasisgivesasuﬀicientcriterion:

GeometricMahlerconjectures 38
VERBATIMEXCERPT
if \(T(l+d u)=\sum c_i u^i\), then representation \(\sum_{r=0}^n b_r \binom nr u^r(1-u)^{n-r}\),
| \(b_r=\sum_{i≤r}\binom |     | ri/\binom |     | ni c_i\). | all \(b_r>0\) |     | ensures. |     |     |     |
| ---------------------- | --- | --------- | --- | --------- | ------------- | --- | -------- | --- | --- | --- |
Thegeometricauditalsoquestionedwhethertheconestatementhadinadvertentlystrengthenedthe
| originalproblem. | Theassistantconcluded: |     |     |     |     |     |     |     |     |     |
| ---------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
VERBATIMEXCERPT
Cone Laplace inequality exactly equivalent for hyperplane sections, not all log-concave.
With 𝑚 = 𝑛+1, it checked that the cone over 𝐾 −𝑧 , evaluated at 𝑈 = (0,𝑚) and 𝑉 = (0,1), gives
0
(𝑛!)2/𝑚𝑚.
the Laplace-product factor It revisited arbitrary nonsmooth cones through Lipschitz projec-
tionmapsandGaussiansmoothing,rederivedthecovarianceidentities,andcheckedthatsquaringthe
matrix-square-rootupdateyieldsthesymmetrizedRiccatiequationwithoutacommutationassumption.
TheassistantbegananotherderivationofthebiasconstructionandBrouwernormalization,reachingthe
inward-pointingestimatesforeigenvaluesofthecoordinate-changematrix.
| 44 The orthant | model |     | and directional |     | Gaussian |     | tails |     |     |     |
| -------------- | ----- | --- | --------------- | --- | -------- | --- | ----- | --- | --- | --- |
Theassistantcontinuedcheckingtheproposedconenormalization,beginningwithaninward-pointing
estimate for the matrix parameter. It used this estimate in a Brouwer argument to impose both mean
balance and covariance feedback. It then rederived the entropy comparison: integrated projection
derivativessuppliedJacobians,alogarithmicdeterminantcalculationsuppliedasurplus,andGaussian
smoothing and truncation preceded change of variables. Decomposing the centered layer field as
𝐴 = 𝐿 + 𝑅, it checked the Gaussian covariance identities, parity bounds, and commutator estimates
intended to control the residual and the noncommuting covariance correction. Its equality argument
proceededfromvanishinglayererrorstocommutinglinearcoeﬀicients, coordinatethresholds, andan
orthantafteralineartransformation.
ℝ𝑚,
The orthant became an explicit consistency check and then an illustration in the draft. For 𝐶 =
+
| all-ones𝑈,andcovariancecorrection𝑇 |     |         |     | = 0,theassistantobtained |        |     |     |       |         |     |
| ---------------------------------- | --- | ------- | --- | ------------------------ | ------ | --- | --- | ----- | ------- | --- |
|                                    |     | 𝜉 = 𝑧𝑈, |     | 𝑃 = diag(1               |        | ),  | 𝐴   | = 𝐿 = | diag(−𝐺 | ).  |
|                                    |     | 𝑧       |     | 𝑧                        | {−𝐺≤𝑧} |     |     |       |         | 𝑖   |
𝑖
Integrationofthetransportweightsgavecoordinates−log𝑝(−𝐺 )and−log𝑝(𝐺 ),where𝑝isthestan-
|     |     |     |     |     |     |     |     | 𝑖   |     | 𝑖   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dardGaussiandistributionfunction. Itemphasizedthatgeneralprojectionlayerswerenotassumedto
formanestedfamilyofprojections.
Thetailestimatesrequiredifferentargumentsatthetwoends. For𝑠 ≥ 0,theassistantwrote
|     |     |     |     |     | ∞   |     |     | 𝜙(𝑠) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
𝑢𝑒−𝑠𝑢−𝑢2/2𝑑𝑢
|     |     |     | 𝑎(−𝑠) | = 𝜙(𝑠)∫ |     |     | ≍   |     | .   |     |
| --- | --- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- |
(1+𝑠)2
0
This controlled the negative tail of 𝑃 and 𝑋 . At the positive end it instead used the bias deep inside
|     |     |     |     | 𝑧   | 𝑧   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theconetocontrol𝐼−𝑃 𝑧 and𝑌 𝑧 . Thevanishingstatementconcernsconvergenceas𝑧 → −∞.
| 45 Separability, | variance |     | recovery, |     | and profile |     | growth |     |     |     |
| ---------------- | -------- | --- | --------- | --- | ----------- | --- | ------ | --- | --- | --- |
The assistant reexamined its proposed general Mahler argument from the cone reduction through the
scalarestimates.

GeometricMahlerconjectures 39
It checked the biased Gaussian projection construction, the simultaneous choice of coordinates and
covariance,andtheentropysurplusinvolvingtracesof𝑃 (𝐼−𝑃 ). RecomputingGaussianintegrationby
𝑥 𝑧
partsandthedecomposition𝐴 = 𝐿+𝑅,itfollowedthecovarianceidentities,parityestimates,andlayer
errors through the noncommuting matrix terms. It checked that the matrix square-root update solved
thesymmetrizedRiccatiequationandthattheresultingcommutatorcostsmatchedthescalarendpoint
inequality.
Forequality,theassistantreasonedthatvanishingoff-diagonalspectraldefectforcesthecoeﬀicientsof
𝐿tocommute. Vanishinglayerdefectwouldthenmaketheprojectionderivativediagonalinafixedbasis
almosteverywhere. Itexpandedthefinalgeometricstep: Lipschitznessandvanishingcrossderivatives
makeeachcomponentofΠ dependonlyonitscorrespondingcoordinate,soitsimage𝐶 isaproduct.
𝐶
Solidity and pointedness restrict the coordinate factors to half-lines; undoing the transformation and
slicingtheconewouldgiveasimplex.
Thescalaraudittrackedinterpolationerrors,weightedprimitives,andseparateerrorboundsforshort
intervalsandtails. Intheboundedmiddlerangeitretained𝑉 = 𝑞2−𝑞2̄ . Alowerboundontheaveraging
𝑞
densityandaLipschitzboundfor𝑞gave
𝑣 𝑧3 |𝑞 −𝑞 |
𝑉 /ℎ2 ≥ ℎ , 𝑧 = + − , 𝑣 = ℎcothℎ−ℎ.
𝑞 3⋅.193 2ℎ ℎ
Theassistantcheckedhowthiscubicgainpaidfortheendpoint-errorterms,thenreducedtheremaining
polynomialinequalitiestoBernstein-coeﬀicientinequalities. Forlargerwidthsitrevisitedangularsigns
androundederrorbounds.
Italsoreplacedaverbalallocationofvariancewithanexplicitresidualinequality.
Alaterrereadingfoundanoverbroadgrowthstatement:
VERBATIMEXCERPT
Potential ambiguity: \(X=p/\phi\) grows like \(e^{x²/2}\), not polynomial.
Theassistantrevisedthestatementtonamethetestprofileswhosederivativeshavepolynomialgrowth,
excludingthetemporaryratios𝑋,𝑌. Italsoclarifiedthecone’spositiveheights,fixed-coordinatematrix
expectations, and aﬀine invariance, then continued checking signs, convergence, and equality deduc-
tionsintheassembledcandidateargument.
46 Reexamining the entropy bound and its matrix dependencies
The assistant returned to its general Mahler candidate, reconstructing the cone normalization, the en-
tropyinequality,andthescalarestimates. Fortheconeover𝐾 −𝑧 ,itspositivedual𝐷,and𝑚 = 𝑛+1,
0
itcheckedthattheverticalchoices𝑈 = (0,𝑚),𝑉 = (0,1)give
(𝑛!)2
𝜒 (𝑉)𝜒 (𝑈) = |𝐾||(𝐾−𝑧 )∘|.
𝐶 𝐷 𝑚𝑚 0
ItrederivedtheexistenceandtailsofthebiasedGaussianprojectionfield,thenthesimultaneouschoice
ofcoordinatesandcovarianceΣ = 𝐼 +𝑇. Inparticular,itcheckedthatsquaringthematrixsquare-root
relation produced the intended quadratic equation without assuming that its coeﬀicients commute. It
alsoreconstructedthelog-Jacobiansurplusandthesmoothingargumentfortheentropytransport.
Theassistantnexttrackedthediagonaljumpinthemixedderivativeof𝑎(min(𝑥,𝑧))𝐵(max(𝑥,𝑧)),the
Gaussian resolvent identity, and the signs and factors in the quadratic identities. Spectral thresholds
supplied a positive layer measure even though the projection derivatives were not assumed nested. It

GeometricMahlerconjectures 40
checkedtheHermite-degreeestimates,completedsquares,andcommutatorboundsusedtoabsorbthe
residual terms. Following its candidate’s equality argument, it reasoned that vanishing losses would
force commuting coeﬀicient matrices and coordinatewise projection, hence an orthant cone and a sim-
plexsection.
It then expanded the argument for log-determinant integrability and clarified the Gaussian spectral
formdomainandendpointorientation. Inparticular,itclarifiedthattheclippedproductinthebound
for𝐵 wasconvexasafunctionofonevaryingargument,withtheotherquantityfixed.
1
47 Cone normalization and matrix cancellation
Theassistantcontinuedauditingitsgeneral-caseargumentthroughtheconeinequality
𝜒 (𝑉)𝜒 (𝑈) ≥ 1, ⟨𝑈,𝑉⟩ = 𝑚 = 𝑛+1.
𝐶 𝐷
Itrederivedthebiased-projectionidentities,thenormalizationbyalineartransformationandGaussian
covarianceΣ = 𝐼+𝑇,andtheentropycomparison. Particularchecksconcernednoncommutingmatrices,
determinantlimits,convergenceofthelayerintegrals,anddifferentiationforarbitrarynonsmoothcones.
Theassistantrepeatedlytestedwhetherasign,normalization,orinterchangeofintegralshadbeenlost;
itsorthantmodelsuppliedacaseinwhichtheproposedinequalitiesshouldbecomeequalities.
Writingtheintegratedprojectionfieldas𝐴 = 𝐿+𝑅,itcheckedtheseparationintoGaussiandegrees,
the contact terms, and the two spectral estimates controlling commutators. Direct integration repro-
duced the constants 2log2 − 1/3 and log2 + 1/4. Gaussian integration by parts on the linear field 𝐿,
together with the quadratic equation for 𝑇, was then used to cancel the covariance term and leave the
proposedscalarsegmentinequality. Theassistantfollowedtheequalityargumentfromvanishinglosses
tocommutingcoeﬀicientmatrices,diagonalprojectionderivatives,andanorthantaftertransformation:
VERBATIMEXCERPT
Equality from negative losses doesn't require proving uniqueness of fixed point Q,T; for any one,
if product=1 then all inequalities saturate, support yields transformed cone orthant.
48 Explicit projection maps and scalar dependencies
Theassistantexpandedtheanalyticstepsofitsgeneral-caseargument. Itwrotethesmoothedmapsex-
plicitlyasintegralsofbiasedconeprojections,with𝑍 = Σ1/2𝐺andΣ = 𝐼+𝑇. Itusedstrictmonotonicity
forinjectivity,thenchangeofvariablesandJensen’sinequalityfortheentropyestimate. Itscheckssep-
aratedconvergenceof thelinear costsfrommonotoneconvergenceof thepositiveJacobian factorsand
examinedintegrabilityofthelimitinglogarithmicdeterminants.
Forcovariancefeedbackitrevisitedthedeterministicmatrixequation
𝜆𝑇2+C∘𝑇+K = 0, 𝐵∘𝐸 = (𝐵𝐸+𝐸𝐵)/2.
Itemphasizedthatexpandingthesquareandcomparingpositivesquarerootsdidnotrequiresimulta-
neousdiagonalization:
VERBATIMEXCERPT
None of these matrices need commute; update uses completing square with sym product, and
square-root comparisons are in Loewner order.

GeometricMahlerconjectures 41
ItthenrederivedGaussiancovarianceidentities,Hermiteestimates,spectralthresholdcomparisons,and
thecancellationoftheterminvolving𝜆tr(S𝑇2). Itcheckedthepointwiseidentity𝐹 = 𝑑+|𝑢|2 = 𝑐+2𝑘𝑞
whiledistinguishingitfromamultiplicativerulefortheOrnstein–Uhlenbeckoperator.
Initsequalityargument, strictnessofthescalarsegmentinequalityforcedthespectralpairmeasure
onto the diagonal, hence commutation of the linear Gaussian coeﬀicients. Vanishing layer error then
made the cone projection coordinatewise. The assistant concluded that the transformed cone was an
orthant and its bounded section a simplex. It also checked the normalization on a two-dimensional
simplex,obtainingvolumeproduct27/4.
ThesubsequentreviewreturnedtoscalarestimatesforGaussiantailsandexpansionsin𝑥−2. Interme-
diatesegmentsrequiredthevarianceoftheauxiliaryprofile𝑞,alowerboundfromendpointseparation,
andpositivityofBernsteincoeﬀicients.
49 The general-body conclusion
Theassistantendsthegeneral-caseattemptbycheckingthefixed-pointnormalization,Gaussiancovari-
anceidentities,entropyJacobians,andnoncommutingtraceproducts. Itemphasizesthatthecoeﬀicients
ofthelinearGaussianmatrixfieldaredeterministicexpectations,althoughchosenjointlywiththecovari-
ance correction. It checks orthant and simplicial-cone cases, then follows vanishing layer and spectral
errors to an orthant and a simplex. It adds details about Gaussian smoothing, boundary integrability,
andtheHermitecovarianceformula. Itsproposedconclusionremainsdependentontheuniformscalar
inequalitiesusedintheentropycomparison.
References
[1] Shiri Artstein-Avidan, Shay Sadovsky, and Raman Sanyal. Geometric Inequalities for Anti-Blocking
Bodies. Communications in Contemporary Mathematics 25(3) (2023), 2150113. https://doi.org/
10.1142/s0219199721501133.
[2] Keith Ball. Volume ratios and a reverse isoperimetric inequality. Journal of the London Mathematical
Society(2)44(2)(1991),351–359.https://doi.org/10.1112/jlms/s2-44.2.351.
[3] Keith Ball. Cube slicing in ℝ𝑛. Proceedings of the American Mathematical Society 97(3) (1986),
465–473.https://doi.org/10.1090/s0002-9939-1986-0840631-0.
[4] WojciechBanaszczyk.Newboundsinsometransferencetheoremsinthegeometryofnumbers.Mathema-
tischeAnnalen296(1)(1993),625–635.https://doi.org/10.1007/bf01445125.
[5] MirosławBaran.Siciak’sextremalfunctionofconvexsetsinℂ𝑁.AnnalesPoloniciMathematici48(3)
(1988),275–280.https://doi.org/10.4064/ap-48-3-275-280.
[6] MirosławBaran.ComplexequilibriummeasureandBernsteintypetheoremsforcompactsetsinℝ𝑛.Pro-
ceedings of the American Mathematical Society 123(2) (1995), 485–494. https://doi.org/10.109
0/S0002-9939-1995-1219719-6.
[7] FranckBartheandMatthieuFradelizi.Thevolumeproductofconvexbodieswithmanyhyperplanesym-
metries. American Journal of Mathematics 135(2) (2013), 311–347. https://doi.org/10.1353/ajm.
2013.0018.
[8] Franck Barthe. On a reverse form of the Brascamp–Lieb inequality. Inventiones Mathematicae 134(2)
(1998),335–361.https://doi.org/10.1007/s002220050267.

GeometricMahlerconjectures 42
[9] BoBerndtsson.ComplexintegralsandKuperberg’sproofoftheBourgain–Milmantheorem.Advancesin
Mathematics388(2021),107927.https://doi.org/10.1016/j.aim.2021.107927.
[10] Bo Berndtsson. Subharmonicity properties of the Bergman kernel and some other functions associated to
pseudoconvexdomains.Annalesdel’InstitutFourier56(6)(2006),1633–1662.https://doi.org/10.5
802/aif.2223.
[11] DavidNaumovichBernshtein.Thenumberofrootsofasystemofequations.FunctionalAnalysisand
ItsApplications9(3)(1975),183–185.https://doi.org/10.1007/bf01075595.
[12] LudwigBerwald.VerallgemeinerungeinesMittelwertsatzesvonJ.FavardfürpositivekonkaveFunktionen.
ActaMathematica79(1947),17–37.https://doi.org/10.1007/bf02404692.
[13] Sergey Bobkov and Mokshay Madiman. Reverse Brunn–Minkowski and reverse entropy power in-
equalities for convex measures. Journal of Functional Analysis 262(7) (2012), 3309–3339. https:
//doi.org/10.1016/j.jfa.2012.01.011.
[14] Christer Borell. Geometric bounds on the Ornstein–Uhlenbeck velocity process. Zeitschrift für
Wahrscheinlichkeitstheorie und Verwandte Gebiete 70(1) (1985), 1–13. https://doi.org/10.1
007/bf00532234.
[15] Jean Bourgain and Vitali D. Milman. New volume ratio properties for convex symmetric bodies in ℝ𝑛.
InventionesMathematicae88(2)(1987),319–340.https://doi.org/10.1007/BF01388911.
[16] HermJanBrascampandElliottH.Lieb.OnextensionsoftheBrunn–MinkowskiandPrékopa–Leindler
theorems,includinginequalitiesforlogconcavefunctions,andwithanapplicationtothediffusionequation.
JournalofFunctionalAnalysis22(4)(1976),366–389.https://doi.org/10.1016/0022-1236(76)900
04-5.
[17] LuisA.Caffarelli.MonotonicitypropertiesofoptimaltransportationandtheFKGandrelatedinequalities.
CommunicationsinMathematicalPhysics214(3)(2000),547–563.https://doi.org/10.1007/s002
200000257.
[18] Eugenio Calabi. Complete aﬀine hyperspheres. I. In Symposia Mathematica, vol. X, Academic Press
(1972),19–38.
[19] ShibingChen,YuanyuanLi,DongmengXi,andZhe-FengXu.TheMahlerConjectureinThreeDimen-
sions.Preprint,arXiv:2605.09334v3(2026).https://arxiv.org/abs/2605.09334v3.
[20] Shiu-YuenChengandShing-TungYau.Completeaﬀinehypersurfaces.PartI.Thecompletenessofaﬀine
metrics. Communications on Pure and Applied Mathematics 39(6) (1986), 839–866. https://doi.
org/10.1002/cpa.3160390606.
[21] Dario Cordero-Erausquin and Bo’az Klartag. Moment measures. Journal of Functional Analysis
268(12)(2015),3834–3866.https://doi.org/10.1016/j.jfa.2015.04.001.
[22] Imre Csiszár, János Körner, László Lovász, Katalin Marton, and Gábor Simonyi. Entropy splitting
forantiblockingcornersandperfectgraphs.Combinatorica10(1)(1990),27–40.https://doi.org/10.1
007/bf02122693.
[23] Ronald G. Douglas. On majorization, factorization, and range inclusion of operators on Hilbert space.
Proceedingsof the American Mathematical Society 17(2)(1966), 413–415. https://doi.org/10.1
090/s0002-9939-1966-0203464-1.

GeometricMahlerconjectures 43
[24] Antoine Ehrhard. Symétrisation dans l’espace de Gauss. Mathematica Scandinavica 53 (1983), 281–
301.https://doi.org/10.7146/math.scand.a-12035.
[25] Tommaso de Fernex, Lawrence Ein, and Mircea Mustaţă. Multiplicities and log canonical threshold.
JournalofAlgebraicGeometry13(3)(2004),603–615.https://doi.org/10.1090/s1056-3911-04-0
0346-7.
[26] MatthieuFradelizi,NathaëlGozlan,ShaySadovsky,andSimonZugmeyer.Transport-entropyforms
of direct and converse Blaschke–Santaló inequalities. Preprint, arXiv:2307.04393v1 (2023). https://ar
xiv.org/abs/2307.04393v1.
[27] Matthieu Fradelizi. Sections of convex bodies through their centroid. Archiv der Mathematik 69(6)
(1997),515–522.https://doi.org/10.1007/s000130050154.
[28] MatthieuFradelizi,MokshayMadiman,andLiyaoWang.OptimalConcentrationofInformationCon-
tentForLog-ConcaveDensities.InHighDimensionalProbabilityVII,ProgressinProbability,vol.71,
Birkhäuser(2016),45–60.https://doi.org/10.1007/978-3-319-40519-3_3.
[29] Sidney Golden. Lower Bounds for the Helmholtz Function. Physical Review 137(4B) (1965), B1127–
B1128.https://doi.org/10.1103/physrev.137.b1127.
[30] Yehoram Gordon. On Milman's inequality and random subspaces which escape through a mesh in ℝ𝑛.
In Geometric Aspects of Functional Analysis, Lecture Notes in Mathematics, vol. 1317, Springer
(1988),84–106.https://doi.org/10.1007/BFb0081737.
[31] YehoramGordon,MathieuMeyer,andShlomoReisner.Zonoidswithminimalvolume-product—anew
proof.ProceedingsoftheAmericanMathematicalSociety104(1)(1988),273–276.https://doi.or
g/10.1090/S0002-9939-1988-0958082-9.
[32] NathaëlGozlan.ThedeficitintheGaussianlog-SobolevinequalityandinverseSantaloinequalities.Inter-
nationalMathematicsResearchNotices2022(17)(2022),12940–12983.https://doi.org/10.1093/
imrn/rnab087.
[33] Qi'an Guan and Xiangyu Zhou. Strong openness conjecture and related problems for plurisubharmonic
functions.Preprint,arXiv:1401.7158(2014).https://arxiv.org/abs/1401.7158.
[34] LeonidGurvits.VanderWaerden/Schrijver–Valiantlikeconjecturesandstable(akahyperbolic)homoge-
neous polynomials: one theorem for all. The Electronic Journal of Combinatorics 15(1) (2008), R66.
https://doi.org/10.37236/790.
[35] AllanB.HansenandÅsvaldLima.ThestructureoffinitedimensionalBanachspaceswiththe3.2.inter-
sectionproperty.ActaMathematica146(1981),1–23.https://doi.org/10.1007/BF02392457.
[36] Hiroshi Iriyeh and Masataka Shibata. Symmetric Mahler’s conjecture for the volume product in the 3-
dimensionalcase.DukeMathematicalJournal169(6)(2020),1077–1134.https://doi.org/10.1215/
00127094-2019-0072.
[37] Jaegil Kim and Shlomo Reisner. Local minimality of the volume-product at the simplex. Mathematika
57(1)(2011),121–134.https://doi.org/10.1112/S0025579310001555.
[38] Bo’azKlartag.IsotropicconstantsandMahlervolumes.AdvancesinMathematics330(2018),74–108.
https://doi.org/10.1016/j.aim.2018.03.009.
[39] Greg Kuperberg. From the Mahler conjecture to Gauss linking integrals. Geometric and Functional
Analysis18(3)(2008),870–892.https://doi.org/10.1007/s00039-008-0669-4.

GeometricMahlerconjectures 44
[40] GregKuperberg.Thebottleneckconjecture.Geometry&Topology3(1)(1999),119–135.https://do
i.org/10.2140/gt.1999.3.119.
[41] JimLawrence.Polytopevolumecomputation.MathematicsofComputation57(195)(1991),259–271.
https://doi.org/10.1090/S0025-5718-1991-1079024-2.
[42] Elliott H. Lieb. Convex trace functions and the Wigner–Yanase–Dyson conjecture. Advances in Mathe-
matics11(3)(1973),267–288.https://doi.org/10.1016/0001-8708(73)90011-X.
[43] ÅsvaldLima.Intersectionpropertiesofballsinspacesofcompactoperators.Annalesdel’InstitutFourier
28(3)(1978),35–65.https://doi.org/10.5802/aif.700.
[44] Magnus Lundin. The extremal PSH for the complement of convex, symmetric subsets of ℝ𝑁. Michigan
MathematicalJournal32(2)(1985),197–201.https://doi.org/10.1307/mmj/1029003186.
[45] Françoise Lust-Piquard and Gilles Pisier. Non commutative Khintchine and Paley inequalities. Arkiv
förMatematik29(1–2)(1991),241–260.https://doi.org/10.1007/bf02384340.
[46] MathieuMeyer.Unecaractérisationvolumiquedecertainsespacesnormésdedimensionfinie.IsraelJour-
nalofMathematics55(3)(1986),317–326.https://doi.org/10.1007/BF02765029.
[47] MathieuMeyerandShlomoReisner.Shadowsystemsandvolumesofpolarconvexbodies.Mathematika
53(1)(2006),129–148.https://doi.org/10.1112/S0025579300000061.
[48] ElchananMosselandJoeNeeman.RobustoptimalityofGaussiannoisestability.JournaloftheEuro-
peanMathematicalSociety17(2)(2015),433–482.https://doi.org/10.4171/jems/507.
[49] Fedor Nazarov. The Hörmander proof of the Bourgain–Milman theorem. In Geometric Aspects of
Functional Analysis, Lecture Notes in Mathematics, vol. 2050, Springer (2012), 335–343. https:
//doi.org/10.1007/978-3-642-29849-3_20.
[50] ZbigniewBłockiandWłodzimierzZwonek.EstimatesfortheBergmankernelandthemultidimensional
Suitaconjecture.NewYorkJournalofMathematics 21 (2015), 151–161. https://nyjm.albany.edu/
j/2015/21-6.html.
[51] Grigoris Paouris. Concentration of mass on convex bodies. Geometric and Functional Analysis 16(5)
(2006),1021–1049.https://doi.org/10.1007/s00039-006-0584-5.
[52] Gilles Pisier. The Volume of Convex Bodies and Banach Space Geometry. Cambridge Tracts in Mathe-
matics,vol.94.CambridgeUniversityPress,1989.https://doi.org/10.1017/CBO9780511662454.
[53] Robert T. Powers and Erling Størmer. Free states of the canonical anticommutation relations. Commu-
nicationsinMathematicalPhysics16(1)(1970),1–33.https://doi.org/10.1007/bf01645492.
[54] AndrásPrékopa.Onlogarithmicconcavemeasuresandfunctions.ActaScientiarumMathematicarum
(Szeged)34(1973),335–343.https://acta.bibl.u-szeged.hu/14411/.
[55] Shlomo Reisner. Zonoids with minimal volume-product. Mathematische Zeitschrift 192(3) (1986),
339–346.https://doi.org/10.1007/BF01164009.
[56] ShlomoReisner,CarstenSchütt,andElisabethM.Werner.Mahler’sconjectureandcurvature.Interna-
tionalMathematicsResearchNotices2012(1)(2012),1–16.https://doi.org/10.1093/imrn/rnr003.
[57] Claude Ambrose Rogers and Geoffrey Colin Shephard. The difference body of a convex body. Archiv
derMathematik8(3)(1957),220–233.https://doi.org/10.1007/bf01899997.

GeometricMahlerconjectures 45
[58] ClaudeAmbroseRogersandGeoffreyColinShephard.Convexbodiesassociatedwithagivenconvex
body.JournaloftheLondonMathematicalSociety(1)33(3)(1958),270–281.https://doi.org/10
.1112/jlms/s1-33.3.270.
[59] Jean Saint-Raymond. Sur le volume des corps convexes symétriques. In Séminaire d’initiation à
l’analyse,20eannée,1980–1981,PublicationsMathématiquesdel’UniversitéPierreetMarieCurie,
vol.46,UniversitéParisVI(1981).Exposéno.11,25pp.
[60] Rolf Schneider. Eine Verallgemeinerung des Differenzenkörpers. Monatshefte für Mathematik 74(3)
(1970),258–272.https://doi.org/10.1007/bf01303445.
[61] Isaac Jacob Schoenberg. Metric spaces and positive definite functions. Transactions of the American
MathematicalSociety44(3)(1938),522–536.https://doi.org/10.1090/S0002-9947-1938-1501980
-0.
[62] Richard P. Stanley. On the Number of Faces of Centrally-Symmetric Simplicial Polytopes. Graphs and
Combinatorics3(1)(1987),55–66.https://doi.org/10.1007/bf01788529.
[63] Colin J. Thompson. Inequality with Applications in Statistical Mechanics. Journal of Mathematical
Physics6(11)(1965),1812–1813.https://doi.org/10.1063/1.1704727.
[64] Vladlen Timorin. An analogue of the Hodge–Riemann relations for simple convex polytopes. Russian
MathematicalSurveys54(2)(1999),381–426.https://doi.org/10.1070/rm1999v054n02abeh000134.
[65] JeffreyD.Vaaler.Ageometricinequalitywithapplicationstolinearforms.PacificJournalofMathematics
83(2)(1979),543–553.https://doi.org/10.2140/pjm.1979.83.543.
[66] Shing-Tung Yau. Harmonic functions on complete Riemannian manifolds. Communications on Pure
andAppliedMathematics28(2)(1975),201–228.https://doi.org/10.1002/cpa.3160280203.
[67] GaoyongZhang.Restrictedchordprojectionandaﬀineinequalities.GeometriaeDedicata39(2)(1991),
213–222.https://doi.org/10.1007/bf00182294.
