---
drive_id: "github:openai/math@adc7f12/reasoning_traces/kaplansky-direct-finiteness-characteristic-two.pdf"
title: "OpenAI math — Reasoning summary: Kaplansky's direct-finiteness conjecture in characteristic two"
slug: "openai-math-trace-kaplansky-direct-finiteness-characteristic-two"
category: "theorie-mathematik"
tier: "T2-theory"
index_date: "2026-10-06"
fetched: "2026-10-07"
---

Kaplanskydirectfinitenessincharacteristictwo 1
| Summarized     |     | chain | of  | thought | (Kaplansky |     | Direct Finiteness | in  |
| -------------- | --- | ----- | --- | ------- | ---------- | --- | ----------------- | --- |
| Characteristic |     | Two)  |     |         |            |     |                   |     |
OpenAI
The central algebraic question is whether 𝑎𝑏 = 1 forces 𝑏𝑎 = 1 in every positive-characteristic group
algebra. Part I develops a proposed characteristic-two counterexample. Part II shows how finite-field
witnesses 𝑎𝑏 = 1, 𝑏𝑎 ≠ 1 give an injective, nonsurjective cellular automaton. That conversion assumes
thewitnessesfurnishedbythepreviouscharacteristic-twoargument.
| Part I: Positive-characteristic |     |     |     | direct | finiteness |     |     |     |
| ------------------------------- | --- | --- | --- | ------ | ---------- | --- | --- | --- |
Originalprompt(excerpts)
# Problem
Resolve the following unrestricted positive-characteristic form of Kaplansky's direct-finiteness
| conjecture, | by              | a complete | proof | or a | rigorous | counterexample. |     |     |
| ----------- | --------------- | ---------- | ----- | ---- | -------- | --------------- | --- | --- |
| TARGET      | AND DEFINITIONS |            |       |      |          |                 |     |     |
For every prime p, every field K of characteristic p, every group G, and every a,b in the group
| algebra | K[G],       | prove |      |     |     |     |     |     |
| ------- | ----------- | ----- | ---- | --- | --- | --- | --- | --- |
| ab      | = 1 implies | ba    | = 1. |     |     |     |     |     |
Here K[G] consists of finite formal sums a = sum_g a_g g with a_g in K, with convolution
multiplication induced by the multiplication in G; its identity is the basis element corresponding
to the group identity. Groups with torsion are included. Neither K nor G is assumed finite. It is
enough to establish the assertion for every finitely generated G and then explain the reduction:
the union of the finite supports of a and b generates a subgroup H, and K[H] embeds in K[G].
The target is direct finiteness of group algebras, not the assertion that every group has no zero
divisors or only trivial units. In particular, proving a zero-divisor theorem only for torsion-free
groups does not resolve this task. Stable finiteness asks the analogous identity AB=I implies BA=I
for every finite square matrix size. That stronger conclusion is welcome if proved, but distinguish
it from direct finiteness and justify every claimed equivalence; direct finiteness does not imply
| stable   | finiteness | for | arbitrary | rings. |     |     |     |     |
| -------- | ---------- | --- | --------- | ------ | --- | --- | --- | --- |
| RESEARCH | DIRECTION  |     |           |        |     |     |     |     |
Develop a general argument or an explicit obstruction. Existing proofs for characteristic zero and
for surjunctive groups are useful starting points. Any proof restricted to sofic, residually
finite, amenable, or surjunctive groups must identify its restriction instead of silently extending
it to arbitrary groups. Do not assume all groups satisfy one of those approximation properties. A
theorem about complex operator algebras cannot be transferred to characteristic p without a valid
argument accounting for that change of coefficients. If specializing finitely generated coefficient
rings to finite fields, preserve the equation ab=1 and the nonvanishing of any coefficient
| witnessing | ba-1, | and prove | the | required | specialization |     | exists. |     |
| ---------- | ----- | --------- | --- | -------- | -------------- | --- | ------- | --- |
A useful first milestone is a new class of groups not covered by the known sufficient hypotheses,
or a precise local-to-global criterion whose remaining hypothesis is explicitly isolated. These
| milestones | do  | not replace | the | full quantifiers |     | of the | target. |     |
| ---------- | --- | ----------- | --- | ---------------- | --- | ------ | ------- | --- |
Check explicitly where finite support, the field characteristic, torsion, and any approximation
assumption enter. Verify the argument recovers the elementary finite-group case, where K[G] is a
finite-dimensional K-algebra even when its characteristic divides the group order.

Kaplanskydirectfinitenessincharacteristictwo 2
For a counterexample, specify a prime, a field with an exact representation, a well-defined group,
and two finite sums. Certify the multiplication ab=1 and exhibit a nonzero coefficient or other
rigorous certificate for ba-1. A finitely presented group together with unproved word equalities or
inequalities is not a certificate. One-sided shifts in an unrestricted infinite-dimensional
endomorphism ring or an example in a nongroup monoid algebra do not qualify.
STARTING PRIMARY REFERENCES
1. Tullio Ceccherini-Silberstein, Michel Coornaert, and Xuan Kien Phung, Stable finiteness of
monoid algebras and surjunctivity: https://arxiv.org/abs/2405.18287 ; published version
https://doi.org/10.1016/j.tcs.2025.115228 . Provides a known sufficient surjunctivity hypothesis,
not an all-groups solution.
2. The same authors, First-order model theory and Kaplansky's stable finiteness conjecture for
surjunctive groups: https://ems.press/content/serial-article-files/51166?nt=1 . Gives precise ring
definitions and a model-theoretic proof under surjunctivity. Its historical comments about nonsofic
groups must not be assumed current.
1 From candidate dimensions to characteristic-two sign lifting
The investigation sought direct finiteness, 𝑎𝑏 = 1 ⇒ 𝑏𝑎 = 1, for arbitrary positive-characteristic group
algebras. The assistant used the supplied surjunctivity results to identify a suﬀicient hypothesis for
stable finiteness [12, 13]. It also recorded Elek and Szabó’s sofic-group theorem as a known special
case[19]. Theidempotentdefect𝑞 = 1−𝑏𝑎,with𝑞2 = 𝑞and𝑎𝑞 = 𝑞𝑏 = 0,organizeditssearchbeyond
thathypothesis.
Witt-vectorliftingsuggestedazero-traceidempotent,buttheassistantcouldnotsupplythepositivity
orcontinuationneededtoforcevanishing. Itsentropyapproachrequiredstrictdecreaseonproperlinear
subshifts; nonamenability obstructed naive entropy. It also used the universal left-invertible-element
groupsofDykema,Heister,andJuschenkotoreducetheproblemtofinitecancellationpatterns[17].
Random-prioritypivotdensitiessuggestedanalgebraicdimension,buttheproposedconservationar-
gumentrequireddifferentiatinginfinite-volumequantitiesacrosspossiblephasetransitions. Theassis-
tantdidnotestablishthisstep. Enlargingcoeﬀicientstoaskewgroupringinsteadshiftedthediﬀiculty
toanunresolvedrankcondition.
Spectralamplificationsoughtaforbiddenrationalspectralatomfromrepeateddefectsummands. Its
gainsremainedconditionaloncoeﬀicient,support,denominator,anddeterminantcontrol;theassistant
connectedthisroutewithThom’ssoficeigenvalueandinteger-operatorwork[37,38]andthesoficde-
terminant result discussed by Balci and Skandalis [4]. It still needed an obstruction valid for arbitrary
groups.
Thefinalturnspecializedtocharacteristictwo. Pairingcellswithequalproducts𝑥 𝑦 = 𝑥 𝑦 suggested
𝑖 𝑗 𝑘 𝑙
replacing these relations by 𝑥 𝑦 = 𝑧𝑥 𝑦 , where a central involution 𝑧 would supply minus signs in a
𝑖 𝑗 𝑘 𝑙
complex representation. Success required 𝑧 to survive. Reduced row cycles yielded reduced column
words,whichencouragedtheassistant,butcandidateodd-areasphericaldiagramsdefeatedthesimple
parityjustification. Theircompletiontoafullcancellationpatternremainedunresolved.
VERBATIMEXCERPT
Need show there is always *some* pairing enabling sign lift, or refine by grouping classes size>2
with arbitrary phases. However if equalities exactly 2, no alternative.
Inconsideringwhethercharacteristic-twounitscouldbelifted,itrecalledGardam’snontrivialunitsin
characteristictwoandoverthecomplexnumbers[20,21];itdidnotobtaintheliftingprincipleitwanted.
Theassistantendedbyreformulatingtherowgraphasanimmersionintoagraphwithcolumn-labeled
edges,leavingtherequiredgroup-theoreticcontrolunresolved.

Kaplanskydirectfinitenessincharacteristictwo 3
2 Positivity barriers and asymmetric cancellation
The same attempt moved between proving direct finiteness, 𝑎𝑏 = 1 ⇒ 𝑏𝑎 = 1 in positive-characteristic
group algebras, and constructing a counterexample. Known reductions connected the universal prob-
lem to finite coeﬀicient fields and surjunctivity [12, 13]. In particular, the assistant read the Dykema–
Juschenko reduction equating stable finiteness of 𝐾[𝐺] with direct finiteness of 𝐾[𝐺×𝐻] for every fi-
nite group 𝐻 [18]. It also continued using universal left-invertible-element presentations to encode
characteristic-twocancellations[17].
Random valuations first sought a substitute for positive Hilbert-space geometry. Distinct leading
weightspreventedfinitecancellations,butinfiniteeliminationcouldfailtoconverge,andcoercivitydid
notestablishsurjectivity. Aseparateargumentdevelopedwithinthisattemptamplifiedahypothetical
defect through lamp projections and tensor powers. It proposed integral positive operators with neg-
ative logarithmic determinant, conditional on Lück’s determinant conjecture for the relevant product
groups. Positivityandmomentintegralitydidnotremovethathypothesis.
Manzoor’s work separated the determinant conjecture from co-hyperlinearity for invariant random
subgroups;itdidnotremovethegrouphypothesisintheproposedamplification[28].
Characteristic-two cancellation then suggested comparing right and left quotients of finite supports.
No general parity transfer emerged. A narrower argument observed that collisions under conjugation
occuratisolatedindicesorperiodically. Itproposedthatanidempotent𝑒 satisfying(1−𝑒)𝑡𝑒 = 0fora
groupelement𝑡mustalsosatisfy(1−𝑒)𝑡−1𝑒 = 0.
This obstructed compression by a single group element; extending it to polynomial sums remained
open. Finite-subgroup averages next reduced a possible counterexample to asymmetric double-coset
congruences. Incidence designs promised forward cancellation, but curvature constraints and collaps-
ing presentations blocked the attempted constructions. The assistant still needed to show that an odd
reversedclasssurvivedtheimposedrelations.
Finally, polynomial matrices over the one-sided algebra 𝑘⟨𝑥,𝑦 ∣ 𝑥𝑦 = 1⟩, already considered within
the attempt, seemed to lift forward Laurent identities while preserving a reversed defect. Constant-
intersection restrictions blocked the simplest construction. Split Leavitt families and singular matrices
leftafurtherpossibility,buttheclosingword-countargumentwasunfinished. Thisstageendedwithout
aprooforcounterexample.
3 Coset constructions and the search for positive dimension
Theassistant’ssearchforafailureofdirectfinitenessincharacteristictwograduallygavewaytoattempts
toproveitthroughdimension. Thetargetremainedtheimplication𝐴𝐵 = 1 ⇒ 𝐵𝐴 = 1inagroupalgebra.
Acorrectedrankargumenthandledaspeciallinearconstructionwithsplitrelations,withoutextend-
ing to arbitrary group-algebra elements. The construction search then sought odd-order finite sub-
groups whose nonidentity elements cancel with even multiplicity. Their averaging projectors could
providearectangularfactorization;convertingitintoacounterexamplerequiredfaithfulsubgroupem-
beddings and compatible character projections. Dense identifications threatened collapse, while high-
girthconstructionsexceededtherequiredsizebound.
Recastingthesubgroupidentificationsaslinear-systemsolutiongroupsledtheassistanttoSlofstra’s
embeddingtheoremanditswagon-wheelconstruction[35],asapossiblewaytoretainelementsinvisi-
∗
bletofinite-dimensionalrepresentations. ItalsoconsideredwhetherthemachineryofMIP = RE[25]
couldproducetherequiredcompatiblemeasurements.

Kaplanskydirectfinitenessincharacteristictwo 4
VERBATIMEXCERPT
Cosets give much more flexibility! Any hyperedge set affine copies. Equality δ modp means symmetric
difference of t odd-size cosets leaves singleton.
Translatedsubgroupindicatorsallowedparallelaﬀinepieces,butrealizingtheircancellationwhilekeep-
ing∑ |𝐾 |−1 ≤ 1remainedunresolved. Curvatureestimatesandacharacter-basedintersectionobstruc-
𝑖 𝑖
tionconstrainedparticularconstructionswithoutexcludingallpossibilities.
The positive strategy sought a bounded, strictly monotone dimension invariant under finite-
propagation changes of basis. The assistant had not justified the required conservation identity for
independent random pivot orders. Averaging orders lacked finite normalization, and a quantum
mutual-informationtransportfacedunattainedpivotthresholdsandconditioningproblems.
Before returning to algebraic constructions, the assistant recalled the discussion in Dykema, Heister,
and Juschenko [17] connecting the universal direct-finiteness and stable-finiteness problems, and con-
sideredtransferringamatrixfailuretoascalarfailureoveralargergroup.
Other routes exposed related limitations. A sparse-orthogonality argument required uniformly
bounded supports, whereas the defect-generated families grew. The group-theoretic matrix-
multiplication approach of Cohn and Umans [14] suggested seeking tensor-rank bounds on the
proposed matrix units, but the assistant encountered the absence of a finite ambient volume. Looking
at Manzoor’s work on invariant random subgroups satisfying the determinant conjecture [28] did not
supply a theorem for arbitrary groups. Finite determinant estimates lacked a justified infinite passage.
The later Krylov-space argument suggested an analogy with the information-flow index of Gross,
Nesme, Vogts, and Werner [23]; the assistant sought a corresponding index for its time evolution,
while nonamenable support expansion still prevented the dimension-growth estimate from yielding a
contradiction.
VERBATIMEXCERPT
Formal p-adic solution with support growing not implies finite algebraic solution; complete
filtered ring maybe algebraic power series coordinates with infinite group monomials.
Thuscoeﬀicientliftingalsofailedtopreservetherequiredfinitesupport. Theassistantendedthisstage
withoutacosetcounterexampleorauniversalpositivedimension,leavingitsfinalmodule-localization
proposalsconditional.
4 From modular cancellation to restricted incidence obstructions
The search for 𝑎𝑏 = 1 but 𝑏𝑎 ≠ 1 in a group algebra moved between algebraic constructions and
analytic obstructions. The universal left-invertible-element presentations of Dykema, Heister, and
Juschenko [17] framed the search for finite models of the forward product relations. Laurent-series
completion lacked the flatness needed to preserve an injection; characteristic-two phase lifts required
unprovedglobalconsistency.
The assistant recalled the known sofic and surjunctive cases [19, 12, 13] while asking whether finite
modelsorlogicalcompactnesscouldgobeyondthosehypotheses. Itdidnotobtainsuchanextension.
The attempt’s own subgroup-covering proposal required 𝑡 actual elementary abelian subgroups 𝐾 ,
𝑖
each of odd order 𝑘, with 𝑡 odd and 2 ≤ 𝑡 ≤ 𝑘. Even multiplicity of every nonidentity element would
give
∑𝐾̂ = 1 in𝔽 [𝑁], 𝐾̂ = ∑ 𝑔.
𝑖 2 𝑖
𝑖 𝑔∈𝐾
𝑖
A proposed conversion to a one-sided inverse remained conditional on faithful subgroup realization.

Kaplanskydirectfinitenessincharacteristictwo 5
Meanwhile,therational-eigenvalueroutewasrelatedtoThom’sworkonsoficgroupsandintegraloper-
ators[37]. Tensoramplificationsuggestedadeterminantobstruction,buttheassistantfoundthatinteger
moments allowed small exceptional spectral mass to escape toward large values; the required positiv-
ityprinciplewasmissing. Thesubgroup-coveringsearchalsorecalledArkhipov’sconnectionbetween
graphplanarityandbinarymagicgames[3]. Theassistantaskedwhetheranalogousnoncommutative
flowscouldretainanodd-orderdefect;itdidnotestablishthatextension.
The construction then relaxed complete cancellation to a cylinder set 𝐸 in a probability-preserving
lamp action. Its indicator compressed subgroup sums, with disjoint translates removing uncancelled
terms. Thedesireddensityboundwas𝑡/𝑘 ≤ 𝜇(𝐸). Aninvariant-matchingapproachrecalledLyonsand
Nazarov’sresultforbipartiteCayleygraphsofnonamenablegroups[27]; amatchingprincipleforthe
moregeneralincidencesystemremainedmissing. Associatedactiveblocksformedfinitelinearspaces.
The assistant used the de Bruijn–Erdős finite linear-space bound [11], in its Fisher-type argument, to
forcetheaveragedreciprocal-sizecostaboveoneforanoncollinearblocksurroundedbyleaves:
VERBATIMEXCERPT
Excellent. This kills path/star if neighbors always leaves. If neighbors internal, cost shared;
each line may participate in growing network, maybe use Euler characteristic.
Interacting blocks, odd cycles, and realization of the cylinder remained unresolved. The assistant
ended with this restricted obstruction and no completed construction or proof of unrestricted direct
finiteness.
5 Restricted obstructions and the limits of local information
The assistant investigated the characteristic-two case of direct finiteness through the stronger stable-
finiteness question: whether 𝐴𝐵 = 𝐼 forces 𝐵𝐴 = 𝐼 for square group-algebra matrices. A hypothetical
failuresuppliesthenonzeroidempotent𝑞 = 𝐼−𝐵𝐴.
Inconsideringacompact-shiftformulation,itrecalledSeward’sequal-entropyisomorphismtheorem
for Bernoulli shifts over countably infinite groups, while asking what could distinguish the proposed
product decomposition [33]. The assistant recalled the Andrásfai–Erdős–Sós theorem that a triangle-
freegraphwithminimumdegreegreaterthan2𝑛/5isbipartite[1], andSlofstra’sembeddingtheorem
forfinitelypresentedgroupsinsolutiongroups[35].
Thenextdirectiontreatedasplitcounterexampleasalocalisomorphism𝑋 ≅ 𝑌 ×𝑍, where𝑋,𝑌 are
equal-alphabet full shifts and 𝑍 is nontrivial. A biased independent-input path suggested the entropy
differential 𝑑𝑆 = −⟨𝜙 ,𝑑𝜇 ⟩. The assistant used finite dependence to argue for boundary cancellation
𝑡 𝑡
along that path, then identified unresolved requirements: global path independence, positivity, and
preservationofafinite-rangeGibbsdescriptionwhenretainingonlythecomplementaryfactor.
Information allocation and linear elimination then encountered unbounded propagation. The assis-
tant drew an analogy with the information-flow index of Gross, Nesme, Vogts and Werner for one-
dimensionalquantumcellularautomata,seekingacounterpartonnonamenablegroups[23]. Asharper
circuitproposalused
𝐵 𝑞
𝑊 = ( ),
0 𝐴
whoseinverseandelementary-sheardecompositionfollowfromthesplitrelations. Apparentcompres-
sionofonelogicallayermotivatedanentropy-balanceinvariant. Theassistantconstructedafree-group
controlled-phasegraphstateandconcludedthatitdefeatedthebroaderpremise:

Kaplanskydirectfinitenessincharacteristictwo 6
VERBATIMEXCERPT
So equality of entropy densities for pure finite-depth states is false. Check: C inject from
degree2 to first via boundary operator on free F2, no compact kernel (tree), yes.
VERBATIMEXCERPT
Key EXTRA: in AB case, the entanglement of each S site has Bell *local purification in T*.
Theassistantretainedbounded-neighborhoodBellrecoveryasapossibleextrahypothesis,butdidnot
findaninvariantusingit. Arithmeticliftingfinallyreturnedtothesamelocalitydiﬀiculty: formalcorrec-
tionscouldenlargesupportindefinitely,sotheassistanthadnotobtainedafinite-supportcharacteristic-
zeroinverse.
6 Obstructions to sign lifting and modular corner constructions
The attempt continued seeking direct finiteness: whether 𝑎𝑏 = 1 forces 𝑏𝑎 = 1 in arbitrary positive-
characteristicgroupalgebras. Theassistantretainedsurjunctivityasthesuﬀicienthypothesisinthetwo
startingpapersofCeccherini-Silberstein, CoornaertandPhung[12,13], andrecalledElekandSzabó’s
sofic case [19]. An integral-lift approach associated a divisible module to a hypothetical defect. The
assistantusedashear-and-dilationexampletoarguethatfinitegenerationpermitsunboundedprimary
torsion;themissingconstraintswereprojectivityandasquarepresentation. Decayofinversecoeﬀicients
likewisefailedtolocalizethedefect.
Returning to the universal left-invertible-element presentations of Dykema, Heister and
Juschenko [17], the assistant shifted to lifting characteristic-two cancellation pairs to opposite
signs in characteristic zero. Earlier reasoning within this same attempt supplied the obstruction: odd
sphericaldiagramscancollapsetherequiredcentralinvolution. Itfoundthattensorpairingspreserved
thatobstruction.
Cancelling at the first unsuccessful position in a tensor product appeared cheaper, but the assistant
calculated that correction ranks consumed the entire proposed saving. A compact/discrete duality ar-
gumentthenlackedawell-definedpreservedpairing.
The assistant also revisited its conditional spectral approach, relating a hypothetical modular defect
toanonintegralrationaleigenvalueofanintegralgroup-ringmatrix. Thom’sworkonsoficgroupsand
integeroperatorssuppliedthespectralcomparison[37]; theassistantstillneededadeterminantlower
boundfortheunrestrictedgroupsunderconsideration.
Cycliccancellationpathsretainedonlyconjugacy-classinformation:
VERBATIMEXCERPT
This yields Hattori trace over conjugacy class as expected. Want individual h not sum.
7 Modular decoding meets information at infinity
The positive-characteristic direct-finiteness attempt, seeking 𝑎𝑏 = 1 ⇒ 𝑏𝑎 = 1, moved from small alge-
braic configurations to an information-theoretic obstruction. Characteristic-two calculations with two
copiesof𝑆 ledtheassistanttoexcludeasmallcornerconstructionthroughdouble-cosetanalysisand
3
finiteorvirtuallyabelianreductions. Theydidnotaddressarbitrarygroups.
ItbrieflyconsideredreturningtotheULIEpresentationapproach[17],thenpursuedthespectralroute
associatedwithThom’sworkonsoficgroupsandalgebraiceigenvalues[37]. Theassistantreturnedto

Kaplanskydirectfinitenessincharacteristictwo 7
itsproposedreductiontoanintegergroup-ringmatrix𝑀 = 𝐼 +𝑝𝐶withnormalizedcomplexvonNeu-
mann rank 𝑟 < 1. This suggested a tension: 𝑀𝑋 mod 𝑝 = 𝑋 mod 𝑝 recovers independent input digits
locally, while lowspectralranksuggestslimited information. Tensorpowerspromisedrankat most𝑟𝑗,
whiletheiroperatornormsgrewatmostas𝐾𝑗 forafixed𝐾. TheOrnstein–Weissfree-groupgradientex-
ample[31]defeatedanaiveoutput-onlyargument,andcarrydynamicscouldimportinformationfrom
outside every finite observed region. For the Gaussian channel 𝑌(𝑡) = √𝑡𝑀𝑋 +𝑍, with independent
standard Gaussian noise 𝑍, the assistant compared local digit recovery with a spectral upper bound
involving 1 𝜏log(𝐼 +𝑡𝜎2𝑀𝑀∗), where𝜎2 istheinput-digitvarianceand𝜏 isnormalizedtrace. Itused
2
thefiniteI–MMSEidentity[24]toseekalowerboundfromlocaldecoding,hopingtensoramplification
wouldforceacontradiction:
VERBATIMEXCERPT
This would be a full proof if derivative identity (no lost information to infinity) works.
The infinite-output limit gave an inequality in the wrong direction. A proposed random-order Gaus-
sianpredictionidentitydidnotsolvetheproblem,becauserealpredictorcoeﬀicientsneednotpreserve
modulardecoding.
Reconsidering the attempt’s own tree-code example reversed a suspected entropy-defect sign. The
next approach used systematic encodings 𝑌 = (𝑋 ,𝐸 ), with independent inputs 𝑋 and linear checks
𝑖 𝑖 𝑖 𝑖
𝐸 . Underindependentrandomsitepriorities, theassistantsoughttomatchinputinformationalready
𝑖
revealedbyearliercheckstoinformationnewlycontributedbyotherchecks. Finiteeliminationappeared
promising:
VERBATIMEXCERPT
Since only finitely many rows hit S, descending elimination terminates (ignoring rows zero on S),
regardless chains through others! Excellent.
Butfinitematchingconditionsdidnotyieldaninvariantdensitycomparison,anddecodingthresholds
mightneverbeattained. Smoothscorefunctionsfailedtocapturediscretedigitidentity;thefinallattice-
divisibilityapproachinvokedBombieri–Vaalerboundsonsmallintegerkernelvectorsandtheirgcd-of-
minors refinement [8], but faced uncontrolled boundary growth. The assistant ended with candidate
informationlowerboundswhosepassagefromfinitedecodingtoinvariantaverages,andwhosecontrol
ofexpandingboundaries,ithadnotresolved.
8 Information arriving from infinity
Thecharacteristic-twodirect-finitenessattemptsoughttocontradictanonzerodefect𝐼−𝐵𝐴when𝐴𝐵 = 𝐼.
Areductiondevelopedearlierwithinthissameattemptproposedexcludingintegerfinite-propagation
operators𝑀 ≡ 𝐼 (mod 𝑝) withpositive-dimensionalrealkernel. Independentbase-𝑝 digitsremainex-
actly recoverable from 𝑀𝑋 modulo 𝑝, whereas amplification was intended to make its von Neumann
rank small. The assistant sought a comparison between local recoverability and global information ca-
pacitytocompletethecontradiction.
The assistant tried arithmetic determinants, torus dynamics, and determinantal selections of kernel
coordinates, but found no such comparison. It observed that, on nonamenable groups, finite indepen-
denceneednotexcludeaninfinitesquare-summablekernel,whilelocalmapscanincreasethenumber
ofindependentinformationstreams. ItrecalledSeward’sconnectionbetweenpositiveRokhlinentropy
andtheentropyofBernoullishifts,andworriedthatitsproposedentropyinequalitywouldrequirere-
solvingthatbroaderquestion[34]. TheseobjectionsredirecteditsefforttowardGaussianobservations
andidentitiesrelatinginformationtomean-squareerror.

Kaplanskydirectfinitenessincharacteristictwo 8
VERBATIMEXCERPT
True Brownian with static drift. Thus **reverse** process diffusion with known simple linear
dynamics product across sites, independent! This is huge.
The enthusiasm concerned the independent Brownian bridges obtained by reversing the observations.
Theassistanttriedtoturnthisstructureintoaninformationidentitythrougharepresentationorunique-
nesstheorem,butdidnotestablisheither. Possibleposteriortransitionsandinformationarrivingfrom
arbitrarilydistantcoordinateschallengeditsunrestrictedform. Aspin-flipcalculationsuggestedalow-
signalestimate,buthigher-ordertermsobstructedextension.
TheassistantthenproposedaspatialPoincaréinequality,butrecognizedthatitdidnotgivethecom-
pactnessneededforuniqueness:
VERBATIMEXCERPT
Poincaré alone no compact embedding (infinitely many shifts e_i). q_s weak→0 could carry energy in
changing spatially far modes with bounded gradient, not high temporal frequency.
Finite-coordinateapproximationintroducedcovarianceerrorswhosetotalenergymightsurvivewhile
escaping outward. High-signal disagreement bounds covered only a later regime, leaving the earlier
informationdeficituncontrolled.
Theattemptthenrecastthealgebraiccompressionusingcommutinglocalquantummatrixfactorsand
Bell references. Each logical factor had a fixed outgoing mutual-information bound, but conditioning
couldletonephysicalsiteunlockinformationaboutmanyreferences,defeatingtherequiredincoming
bound. It also considered an information-flow invariant analogous to the one-dimensional index of
Gross,Nesme,Vogts,andWerner,butleftitsextensionacrosstheproposednonamenableinterfaceun-
defined[23]. High-temperatureexpansionsandprojective-unitaryphasessuppliedfurtherspeculative
directions. TheassistantendedwithboththeGaussianuniquenessargumentandthequantumcapacity
argumentunresolved.
9 From Gaussian rank bounds to vertical defect components
The attempt sought to connect arithmetic congruence with analytic rank in the unrestricted positive-
characteristicdirect-finitenessproblem,where𝑎𝑏 = 1shouldimply𝑏𝑎 = 1inagroupalgebra. Itswork-
ingobstructionwasanintegraloperator𝑀 ≡ 𝐼 (mod 𝑝)withdeficientvonNeumannrank,chieflyfor
𝑝 = 2. Tensorpowerswouldamplifythedeficiency. Thisapproachbuiltontheearlierfinite-subgroup
andinteger-flowproposals.
Periodic Gaussian measurements offered a possible bridge: congruence bounds signed Fourier mo-
ments, suggesting nearly independent binary observations. Yet their entropy could not be bounded
directly by real Gaussian capacity, because conditioning on binary observations discards information
retained by real measurements. A subsequent lattice theta estimate seemed less sensitive to the opera-
tor’ssupportdegree:
VERBATIMEXCERPT
Excellent! No support degree! Let's verify Poisson/unimod lattice for coset shift.
The proposed bound controlled finite lattice sums, but the required infinite-volume determinant com-
parisonremainedmissing. WrappedGaussianargumentsencounteredhiddenwindingnumbers;finite-
modulus inverses could send relevant modes to increasing frequencies and supports. The assistant

Kaplanskydirectfinitenessincharacteristictwo 9
foundthatgeneralCameron–MartinandlogarithmicSobolevprinciplesdidnotsupplytheneededcom-
parison.
Afteranalytic-continuationandtorsionproposalsstalled,theattemptturnedtothefixed-supportco-
eﬀicientring
𝐴 = ℤ[𝑎 ,𝑏 ]/(coeﬀicientsof𝑎𝑏−1).
𝑠 𝑡
For 𝑞 = 1 − 𝑏𝑎, it argued that characteristic-zero direct finiteness makes the coeﬀicients of 𝑞 torsion
elementsintheadditivegroupof𝐴. Theirfinitelygeneratedidealsatisfies𝐽2 = 𝐽,soitisgeneratedbyan
idempotent. The proposed conclusion places any defect on an open-and-closed component supported
overfinitelymanyprimes.
Excluding that component remained the missing step. Hensel lifts did not suﬀice because their sup-
portsgrow,whereastheannihilatingintegerbelongstoonefixed-supportscheme. Theassistantthere-
foreretainedtheverticalcomponentastheobstructionitsdeformationandliftingproposalsstillhadto
exclude.
10 Trace, entropy, and boundary barriers to direct finiteness
The search for direct finiteness continued from 𝑎𝑏 = 1 toward excluding the defect 𝑞 = 1−𝑏𝑎 ≠ 0 in
𝔽 [𝐺], especially in characteristic two. The assistant extended constructions developed earlier in the
𝑝
attempt.
The assistant found that coeﬀicient schemes suggested that defects might occupy components con-
finedtopositivecharacteristic;enlargingsupportsdidnotconnectthesecomponentstoordinaryunits.
Integral lifting likewise lost control of support or dimension. A distributional telescoping proposal
sought 𝑥 − 𝑏𝑥𝑎 = 𝑟, where 𝑟 = 𝑞𝑔𝑞 has nonzero coeﬀicient trace 𝜏(𝑟). It rejected this proposal be-
causecyclicityforces𝜏(𝑥−𝑏𝑥𝑎) = 0: compactnessretainedtrace-bearingtailsinsteadofproducingthe
requiredcancellation.
The assistant also reconsidered the ULIE presentations of Dykema, Heister, and Juschenko, asking
whetherthedenseshortrelationsforcedsuﬀicientresidualorgeometricstructuretosettlereversemul-
tiplication[17]. Thisproducednonewcriterion.
Attention shifted to locally split linear encodings of independent physical variables into logical vari-
ables. Ferromagneticbiasesandmasstransportseemedcapableofboundinglogicaldensitybyphysical
density:
VERBATIMEXCERPT
This yields monotonicity and **pressure path inequalities via MTP** maybe enough without
amenability! New promising. Analyze carefully.
Theassistantidentifiedthemissingstepaspassagefromfinite-volumemixed-responsesymmetrytoinfi-
nitevolume. Phasetransitionscouldcarryresponsebeyondfiniteneighborhoods. Pinningfinitelymany
physical coordinates recovered only the ordinary finite-support bound. Local stochastic dynamics did
not repair the gap: the Ornstein–Weiss gradient example [31] showed that proposed entropy currents
neednotdependonlyonendpoints. Localsplittingremainedastronger,unexploitedcondition.
A subsequent lattice approach used an earlier provisional reduction to an integer matrix 𝑀 ≡ 𝐼
(mod 𝑝) with nonzero ℓ2 kernel. Bounded integer solutions must vanish by repeated divisibility. The
assistantinvokedtheBombieri–VaalerformofSiegel’slemmatoboundtheproductofsizesofindepen-
dent integer solutions of finite subsystems [8]. Those short solutions could nevertheless concentrate
neartheboundary;nonamenablegrowthpreventedtheneededinteriorconclusion.

Kaplanskydirectfinitenessincharacteristictwo 10
Finally, finite-subgroupsums andrank-onematrix weightssoughta modularidentity ∑ 𝐾̂𝑊 = 𝐼
𝑖 𝑖 𝑖 𝑚
at low dimension cost. Higher-multiplicity identifications offered coding freedom, while cross terms
imposednewconstraints:
VERBATIMEXCERPT
Offdiag conditions impose additional square density, likely second link counts.
Theassistantendedwithoutestablishingthesubgroupembeddingsortherequiredidentity,leavingthe
trace,entropy,andlatticeapproachesincomplete.
11 Matrix cancellation and punctured aﬀine geometry
Theattemptsoughtacharacteristic-twocounterexampletodirectfinitenessbycombiningmatrixcancel-
lationwithahigh-girthhypergraph. Itsoughtlocalcancellationofrank-onematrixweightswithalarge
nonzeroglobalsum,followedbyagroup-algebraconstruction.
For𝑡verticesanddegree𝐷,rank-onematrices𝑊 shouldsumtozerooneveryhyperedge,whiletheir
𝑣
totalhasrank𝑚largeenoughthat𝑡 ≤ 𝑚(𝐷−1)2. Incidencegirthatleasttwelvewasintendedtosupport
subgroupembeddings. Acorrectedsizeboundworsenedthescalarsizebound;polynomialevaluation
examplesdefeatedaproposedminimum-supportrankinequality,leavingsparselocalconstraintsasthe
∗
central diﬀiculty. A speculative detour invoked MIP = RE while asking about solution-group encod-
ings[25]. Italsoconsidereddesign-matrixrankboundsofBarakandcollaborators,notingthediﬀiculty
of obtaining the needed finite-field bound [5]. Layered basis changes appeared to force short cycles.
Alaterquantum-codereformulationconsideredtheBravyi–Poulin–Terhaltradeoff,buttheassistantre-
gardedgeometriclocalityasunsuitableforthehigh-dimensionalsetting[9].
DescriptionsofGolowichandLin’smultiplication-basedquantumLDPCconstructionandDinur,Liu,
andZhang’saﬀine-linecodesenteredthesearchforlocalpolynomialconstraints[22,15]. Theassistant
later acknowledged their possible inspiration, while continuing to develop the line construction itself.
Thenextproposalremovedholes𝑂from𝐴 = 𝔽𝑛,with𝑞apoweroftwo. Low-degreepolynomialprod-
𝑞
uctssumtozeroonfullaﬀinelines,whereasremovingholescanproduceanonzeroglobalmatrixsum.
Trades replacing radial lines through a hole by parallel lines avoiding it aimed to preserve regularity.
Initialtriangleestimatescontradictedthedimensionsneededforalocal-lemmaargument:
VERBATIMEXCERPT
Need b<a−1 for rare. Generic LLL wanted b>a+4. Conflict!
A punctured-plane tiling offered a revision. For a linear map 𝐽 with no eigenvector over 𝔽 , the line
𝑞
ℓ(𝑥) = 1 was lifted to (𝑥,ℓ(𝐽𝑥)). Independence of 𝑥,𝐽𝑥 for 𝑥 ≠ 0 made these lifted lines partition every
nonzerofiber. SamplingholesfromaNewtoninterpolationinformationsetwouldpreserveindependent
evaluationsafterdeletions. Interpolationpolynomialsthensuggested
∑ 𝑊 = −𝐼 ,
𝑣 |𝑂|
𝑣∈𝐴\𝑂
while retaining local line cancellation. Proposed cycle estimates appeared compatible with the rank
bound.
Theassistantthensetouttheremainingchecks: cycleclassification,probabilisticdependencebounds,
subgroupembeddings,andconversionfromamatrixobstructiontofinitescalargroup-algebrasums. It
proposedattachingadditivegroups𝔽2tovertices,identifyingone-dimensionalsubgroupsalonghyper-
𝑙
edges,andusingnonpositivecurvaturetoestablishembeddings. Subgroupaverageswereintendedto

Kaplanskydirectfinitenessincharacteristictwo 11
produce the matrix factorization, followed by character twists in HNN extensions and a finite-group
matrix corner for the scalar passage. Linnik’s theorem remained a possible dependency for choosing
𝑙+1 divisibleby 𝑞 withinpolynomialbounds [26]. This stageended with the assistantreconstructing
theprobabilistichypotheses.
12 From a characteristic-two construction to a complete draft
Theassistantmovedfromlocalauditstoacompletecandidatecounterexampletodirectfiniteness,the
implication 𝑎𝑏 = 1 ⇒ 𝑏𝑎 = 1 in a group algebra. It reconstructed the proposed characteristic-two
construction from its preceding reasoning and used the supplied surjunctivity results as a consistency
constraint: their stable-finiteness conclusions applied to surjunctive groups, a hypothesis it had not
established for its proposed group [12, 13]. It likewise treated direct finiteness for sofic groups as a
constraintonanyproposedexample[19].
Thegeometricproposalremovedsparseinterpolation points, calledholes, from anaﬀine spaceover
𝔽 , with 𝑞 a power of two. Replacing lines near holes was intended to preserve regular degrees while
𝑞
excluding short incidence cycles. Random subspaces and local-lemma estimates supported this pro-
posed existence argument; Linnik’s theorem controlled the size of a prime ℓ ≡ −1 (mod 𝑞100), giving
𝐷 = ℓ + 1 divisible by 𝑞 [26]. Repeated scrutiny focused on whether repeated polygon labels really
involvedindependentvariables.
For 𝑚 deleted interpolation points, polynomial value columns 𝑥 at the remaining points were in-
𝑣
tendedtosatisfy∑ 𝑥 𝑥T = −𝐼 ,whiletheirGramsumsoneveryretainedlinevanished. Theassistant
𝑣 𝑣 𝑣 𝑚
checked that products of the interpolation polynomials had degree at most 𝑞−2, so their sums along
full aﬀine lines were zero. Finite groups attached to points converted these identities into rectangular
matrices𝑈,𝑇with𝑈𝑇 = 𝐼 . AnearlierrouteappealedtoHaefliger’sdevelopabilitytheoremfornonpos-
𝑚
itivelycurvedcomplexesofgroups,recalledthroughBridson–Haefliger[10];theassistantcheckedlocal
links with girths 6,4,12 and triangle angles 𝜋/3,𝜋/2,𝜋/6. It then replaced this route with a proposed
planarbalanced-diagramargumentusingdegreebounds,longfaces,andEuler’sformulaforthelocal-
group embeddings. With 𝑡 remaining points, the bounds 𝑚 < 𝑡 ≤ 𝑚ℓ2 allowed the proposed packing
ofsubgroupaveragesinto𝑚slotsbycharactertwistsandconjugatinggenerators. Theassistantargued
thatareverseidentitywould,afterapplyingaugmentationintheembeddedbasegroupalgebra,equate
𝐼 withamatrixfactoringthroughdimension𝑚. Anauxiliaryfinite-groupmatrixblockwasintendedto
𝑡
yieldtwoscalargroup-algebraelements. TheassistantrelatedthissteptoDykema–Heister–Juschenko’s
resultthatdirectfinitenessaftertakingproductswitheveryfinitegroupimpliesstablefinitenessofthe
originalgroupalgebra[17].
The assistant investigated possible rank bounds contradicting the polynomial construction and
rechecked the embedding and packing steps. It completed the candidate draft, then returned to the
probabilistic estimates. In particular, it argued that pairwise trivial intersections of direction spaces
separated the cosets for repeated generic polygon labels, and that the resulting small dependency
sums justified the local lemma. It continued scrutinizing this independence argument and the planar
embeddingstep.
In the completed draft, it credited Golowich–Lin’s multiplication-property construction and Dinur–
Liu–Zhang’s prescribed aﬀine-line tests as inspiration for the polynomial pairings, while supplying its
ownproposedgeometricconstruction[22,15].
13 Repeated audits of a characteristic-two candidate
Theassistantrepeatedlychallengeditsownproposedcharacteristic-twocounterexampletodirectfinite-
ness: elements𝑎,𝑏 ∈ 𝐾[𝐺]with𝑎𝑏 = 1but𝑏𝑎 ≠ 1.

Kaplanskydirectfinitenessincharacteristictwo 12
The candidate used a punctured aﬀine space over 𝔽 , with 𝑞 a power of two, covered regularly by
𝑞
fulllineswithincidencegirthatleasttwelve. Polynomialinterpolationattheholesproducedvectors𝑥
𝑣
whoseouterproductssummedtozerooneachsurvivinglineandto−𝐼 globally,where𝑚countedholes.
𝑚
Itcreditedtheaﬀine-linetestsandmultiplicativepairingstoinspirationfromGolowichandLin’swork
on quantum LDPC codes and Dinur, Liu, and Zhang’s codes on high dimensional expanders, without
usingacodingtheoremasadependency[22,15]. Repeatedauditsconcentratedonshort-cyclecounts,
local degree-preserving replacements, and independence of random choices required by the Lovász
locallemma.
The group construction glued copies of 𝔽2 along one-dimensional subgroups. Its proposed embed-
ℓ
dingproofconvertedakilledlocalelementintoabalancedplanargraph. Degreeandfaceboundswere
intendedtocontradictEuler’sformula;theassistantclarifiedthescopeofitsminimalityargument:
VERBATIMEXCERPT
Minimal graph argument doesn't require planar balanced graph remains drawable as word diagram after
contractions; minimal among all graphs satisfying combinatorial balances, not diagrams.
Subgroup averages then yielded rectangular matrices 𝑈,𝑇 with 𝑈𝑇 = 𝐼 . Conjugations and charac-
𝑚
terprojectionswereintendedtogiveasquareone-sidedinverse,whileanembedded-subgroupspecial-
ization would make the reverse identity contradict a rank bound with 𝑡 > 𝑚. Auxiliary matrix units
suppliedtheproposedpassagetoscalargroup-algebraelements. Theassistantrelatedthisenlargement
byafinitegroupfactortoDykema,Heister,andJuschenko’sworkondirectandstablefiniteness[17].
TheassistantusedLinnik’sprimebound[26]tochooseℓ ≡ −1 (mod 𝑞100)withcontrolledsize,keep-
ing⌊log (ℓ+1)⌋boundedas𝑞grew. Attemptstoreplacethisboundwithelementaryprime-divisorargu-
𝑞
ments,largervector-spacespreads,orexplicitMersenneprimesranintodivisibilityorinterpolation-size
obstacles,soitretainedthetheoremasadependency. Theassistantusedcanonicalleastchoicestospec-
ifythefiniteobjectsinitsconstruction.
OnrereadingthetwopapersofCeccherini-Silberstein, Coornaert, andPhung, itretainedsurjunctivity
asthehypothesisfortheirpositivestable-finitenessresults[12,13].
Theassistantendedbyreopeningitsauditoftherandom-variableindependenceinthelineconstruc-
tionandthereductionsintheplanarembeddingargument;ithadnotidentifiedaflawinthesechecks.
14 Stress-testing a characteristic-two counterexample
TheassistantexaminesitsproposedcounterexampletoKaplansky’sdirect-finitenessconjectureagainst
algebraicandgeometricobstructions. Thegoalisfinitegroup-algebrasums𝑎,𝑏with𝑎𝑏 = 1but𝑏𝑎 ≠ 1.
Onrereadingitsdraft,itretainstheattributionofthefinite-factormatrixreductiontoDykema,Heister,
andJuschenko[17],andofthemotivationformultiplicativepolynomialpairingsandprescribedaﬀine-
lineteststoGolowichandLinandtoDinur,Liu,andZhang[22,15]. Thelatterpaperssupplymotivating
themesratherthanatheoremusedinthecandidate’sproof.
Theauditmovesfrompossibleexternalobstructionstotheconstruction’sgeometricandalgebraicjoints.
The assistant checks that the two surjunctivity results assume a surjunctive group or monoid, respec-
tively [13, 12]. Looking at Farrell–Jones theory and CAT(0) groups does not supply an unrestricted
positive-characteristictheoremthatrulesoutthecandidate. Thestable-finitenessdiscussionofBartels,
Lück, and Reich separates characteristic zero from the sofic case [6]; the latter uses Elek and Szabó’s
result [19]. A double-counting check clarifies why characteristic zero cannot support the proposed

Kaplanskydirectfinitenessincharacteristictwo 13
weights: if every vertex has degree 𝐷 and every line sum vanishes, then 𝐷∑ 𝑊 = 0. Here 𝐷 van-
𝑣 𝑣
ishesinthecoeﬀicientfield.
VERBATIMEXCERPT
Our mod2 D divisible q ensures. Thus no lift. Positive characteristic essential.
The assistant also considers whether the eigenvalue restrictions associated with Dodziuk, Linnell,
Mathai,Schick,andYatescouldobstructanintegrallift,butdoesnotestablishtherequiredgroup-class
hypothesis [16]. The geometry uses sparse deleted points, local line replacements preserving other
degrees, and a finite local lemma to exclude short polygons. Conditional independence and witness
countsreceiveparticularscrutiny. Linnik’stheoremsuppliestheprime-distributionboundusedtokeep
theambientdimensionboundedasthefieldgrows[26];proposedelementaryreplacementsencounter
divisibilityorinterpolationdiﬀiculties.
Polynomialweightsareintendedtoproduceanonzeroglobalpairingdespitezerolinesums. Aplanar
Euler-characteristicargumentisthenauditedastheproposedcertificatethatthegluedfinitesubgroups
embed. Averagingprojectionsyieldrectangularmatrices𝑈𝑇 = 𝐼 ; packingthemintosquarematrices
𝑚
wouldmakethereverseidentityimplyadimension-𝑡identityfactoringthroughdimension𝑚 < 𝑡. The
assistantappliesspecializationonlyinsidethesmallergroupalgebra. Finite-groupmatrixunitswould
convertthematrixobstructionintoscalarsums.
Theassistantnextplansfullerjustificationofthegeometriccounts,embeddings,andalgebraicreduc-
tions.
15 Auditing the proposed characteristic-two counterexample
Theassistantscrutinizedwhethergluingfinitegroupspreservedtheirembeddings. Thetargetwasfinite
sums𝑎,𝑏 ∈ 𝐾[𝐺]incharacteristictwowith𝑎𝑏 = 1but𝑏𝑎 ≠ 1.
The assistant reread the supplied primary references and confirmed that their stable-finiteness results
requiredsurjunctivity[12,13].
The assistant credited multiplication properties in Golowich and Lin [22] and prescribed aﬀine-line
testsinDinur,Liu,andZhang[15]asmotivation,withoutinvokingtheircodingtheorems. Theconstruc-
tionusedpolynomialvectors𝑥 onapuncturedaﬀinespaceover𝔽 ,with𝑞 = 2ℎ. Proposedlinetrades
𝑣 𝑞
preservedregularity,whileindependentlychosensubspacesandlocal-lemmaestimatesexcludedshort
incidencecycles. Interpolationwasintendedtogivezeroouter-productsumsoneverylineand
∑𝑥 𝑥T = −𝐼 .
𝑣 𝑣 𝑚
𝑣
Averaging over embedded finite subgroups would then produce a rectangular factorization 𝑈𝑇 = 𝐼 .
𝑚
Conjugating projections into orthogonal slots and finite-group matrix amplification were proposed to
turnthisintothescalarcounterexample;theassistantrelatedtheamplificationtoDykema,Heister,and
Juschenko[17].
Linnik’s theorem [26] remained an explicit dependency for choosing a suitably bounded prime ℓ ≡
−1 (mod 𝑞100); attempted alternatives did not replace it. Possible residual-finiteness and curvature
obstructionsalsoremainedunresolved.
VERBATIMEXCERPT
Could N actually be trivial despite planar argument due to non-planarity of reduction? Need
scrutinize signed wires again. If relators all local and group trivial, s reduces via conjugations
in free group.

Kaplanskydirectfinitenessincharacteristictwo 14
The embedding audit translated a supposedly killed generator into a planar weighted bipartite graph.
Minimalitywasmeanttoforceblackdegreesatleastthree,ordinarywhitedegreesatleasttwo,andall
but possibly one face to have length at least twelve. These estimates would contradict Euler’s formula.
The revisions examined signed reductions, bridges, parallel edges, and neighbor merging, then made
hole-deletion bounds, repeated-label independence, line parametrizations, and interpolation choices
explicit. Writing 𝐵,𝑊,𝐸,𝐹 for black vertices, white vertices, edges, and faces, the assistant obtained
𝐵 ≤ 𝐸/3,𝑊 ≤ 𝐸/2+1/2,and𝐹 ≤ 𝐸/6+1,contradicting𝐵+𝑊 +𝐹 = 𝐸+2.
16 Testing the links in a proposed direct-finiteness counterexample
The recorded attempt repeatedly audited its proposed characteristic-two group-algebra elements satis-
fying 𝑎𝑏 = 1 but 𝑏𝑎 ≠ 1. The aim shifted from reconstructing the entire construction to clarifying its
subgroup embedding and projection packing. The minimization was over finite graphs satisfying the
balanceconditions,ratherthanonlygraphsobtainedbyparticularreductions.
The assistant checked that the positive results of Ceccherini-Silberstein, Coornaert and Phung still
required surjunctivity, under which group algebras over every field are stably finite [12, 13]. Its draft
creditedmultiplicationpropertiesandprescribedaﬀine-linetestsinthecodingpapersofGolowich–Lin
and Dinur–Liu–Zhang as inspiration for the polynomial pairing, without using a coding theorem as a
dependency[22,15].
Thegeometricproposalcombinedaﬀinelines,deletedinterpolationpoints,andrandomlocalreplace-
ments. Linnik’stheoremcontrolledanoddprimeℓ[26],whilealocal-lemmaargumentwasintendedto
ensureincidencegirthatleasttwelve. Polynomialcolumns𝑥 ∈ 𝐾𝑚,forafinitefield𝐾 ofcharacteristic
𝑣
two,weredesignedtosatisfy
∑𝑥 𝑥T = 0, ∑ 𝑥 𝑥T = −𝐼 .
𝑣 𝑣 𝑣 𝑣 𝑚
𝑣∈𝑓 𝑣∈𝑉
Theauditexplainedwhysumminglineidentitiescausednoimmediatecontradiction: theregulardegree
vanishedin𝐾.
Localgroups(ℤ/ℓ)2weregluedalongcyclicsubgroups. Theirproposedinjectivitydependedoncon-
verting a collapsed generator into a planar balanced graph with one exceptional vertex. The assistant
clarifieditsminimizationargumentbyminimizingoverallgraphssatisfyingthebalanceconditions,per-
mittingcontractionsbeyondaparticularwordreduction. Degreeandfaceboundswerethenintended
tocontradictEuler’sformula.
Subgroupaveragesconvertedthepolynomialidentitiesintorectangularmatriceswith𝑈𝑇 = 𝐼 . Char-
𝑚
acterprojectionspackedthemintosquarematrices. Assumingareverseinversewouldforce𝐼 tofactor
𝑡
throughdimension𝑚 < 𝑡,afterapplyingahomomorphismonanembeddedbasealgebra. Afiniteaux-
iliary group supplied the proposed final matrix-to-scalar transfer. The draft related this enlargement
toDykema,HeisterandJuschenko’sresultconnectingdirectfinitenessafterfinite-groupproductswith
stablefiniteness[17].
Theassistantexpandedthealgebraandsharpenedtheplanarargument,thenexaminedthegeometric
existenceargumentandpossibleresidual-finitenessobstructions.
17 Auditing a candidate through algebra and geometry
Theassistantrepeatedlychallengeditsproposedcharacteristic-twocounterexampletodirectfiniteness:
finite sums 𝑎,𝑏 ∈ 𝐾[𝐺] with 𝑎𝑏 = 1 but 𝑏𝑎 ≠ 1. Its aﬀine construction, developed within this attempt,
combined a regular hypergraph of punctured lines, polynomial interpolation, and finite groups glued

Kaplanskydirectfinitenessincharacteristictwo 15
alongcyclicsubgroups. Theintendedidentities
∑𝑥 𝑥T = 0, ∑ 𝑥 𝑥T = −𝐼
𝑣 𝑣 𝑣 𝑣 𝑚
𝑣∈𝑓 𝑣∈𝑉
produceda proposedrectangularfactorization 𝑈𝑇 = 𝐼 ; averagingidempotents, charactertwists, and
𝑚
matrixunitsweremeanttoconvertitintothescalarcounterexample.
With𝑞 = 2ℎ andaprimeℓ ≡ −1 (mod 𝑞100),theassistantusedLinnik’sboundtokeep⌊log (ℓ+1)⌋,
𝑞
andhencetheambientdimension,boundedas𝑞grew[26]. Theauditrecheckedcollisionestimates,local
line exchanges, short polygons, and a planar Euler argument intended to preserve the local subgroup
embeddings. Theassistantfoundthatitsattemptedcontradictionsdidnotproduceproofs. Finiteglobal
dimension and algebraic 𝐾-group information did not automatically provide positivity. Recalling its
examination of Bartels, Lück, and Reich, the assistant noted that their argument used stable finiteness
as a separate hypothesis, with the cited suﬀicient results requiring characteristic zero or soficity [6];
characteristic-zero lifting led to infinite support in a completion; approximate matchings did not give
exactlinepartitions. Anentropyobjectionalsoencounteredjointlyinformativeaverages:
VERBATIMEXCERPT
But collective conditional MI can be greater than sum due synergies (noises cancel via relations).
An optional increase of incidence girth from twelve to fourteen raised possible hyperbolicity and
residual-finitenessconsequences,promptingextrascrutiny. Six-sidedconfigurationsneededfurtheroc-
cupancycontrols,sothisstrengtheningremainedexploratory. Thefinitematrixblockandfinite-support
reductionwereclarified,whilegeometricclassificationremainedunresolved.
Theassistant’sdraftcreditedDykema,Heister,andJuschenkoforthefinite-factorconnectionbetween
directandstablefiniteness[17]. ItalsocreditedGolowichandLin’sworkonproductsofalgebraiccodes
and Dinur, Liu, and Zhang’s work on high-dimensional expander codes with inspiring multiplicative
pairingsandprescribedaﬀine-linetests;ittreatedtheseasinspiration,notcoding-theorytheoremdepen-
dencies[22,15]. ThetwopapersbyCeccherini-Silberstein,Coornaert,andPhungsuppliedthepositive
stable-finitenessresultsunderasurjunctivityhypothesis[12,13].
Wise’sresidual-finitenesstheoremforacute-angledpolygonsoffinitegroupsrequiredatleastfoursides,
so the assistant could not apply it directly to the triangular construction [39]. It ended this stage still
seekingeitherageometricclassificationoracontradiction.
18 Testing the candidate against geometric and algebraic obstructions
Across these consecutive audits, the assistant tried to break its proposed characteristic-two counterex-
ampletodirectfiniteness: finitegroup-algebrasumssatisfying𝑎𝑏 = 1but𝑏𝑎 ≠ 1.
The geometric audit rechecked sparse holes in an aﬀine interpolation set, deletion estimates, and in-
dependenceinalocal-lemmaargumentexcludingshortpolygons. Linereplacementswereintendedto
preserveregulardegreewhileproducingincidencegirthatleasttwelve. Linnik’stheoremremainednec-
essaryforthechosenparameterbalance,keepingtheambientdimensionboundedasthefieldsizegrew;
elementary replacements stalled [26]. A planar balance-diagram argument was supposed to establish
thatlocalfinitegroupssurvivedgluing,usingdegreeboundsandEuler’sformula.
Low-degreepolynomialidentitiesthensuppliedrectangularmatrices𝑈,𝑇 with𝑈𝑇 = 𝐼 . Character
𝑚
projections and conjugating generators were intended to turn this into a square-matrix obstruction: a
reverse inverse would force 𝐼 to have rank at most 𝑚 < 𝑡. Finite-group matrix units would transfer
𝑡

Kaplanskydirectfinitenessincharacteristictwo 16
that obstruction to ordinary group-algebra elements. The assistant credited the finite-factor amplifica-
tion theme to Dykema, Heister and Juschenko [17], and identified Golowich and Lin’s multiplication-
property constructions and Dinur, Liu and Zhang’s prescribed aﬀine-line tests as inspirations for its
polynomialpairing[22,15];itdidnotinvokeacodingtheoremasadependency.
Attention shifted toward structural reasons the candidate might be impossible. The assistant tested
whether Berlai’s criterion for groups with a finitely generated residually finite normal subgroup and
sofic quotient applied, but found no suitable normal subgroup [7]. It also considered Wise’s residual-
finitenessresultforacutepolygonsoffinitegroupswithatleastfoursides,withoutestablishingareduc-
tionofitsgluedconstructiontothatsetting[39]. Itsreviewrecalledtheresiduallyamenableandsofic
suﬀicient classes treated by Ara, O’Meara and Perera and by Elek and Szabó, respectively [2, 19]. The
assistantdistinguishedliftingaprojective-moduleclassfromliftinganactualmodule,andformalidem-
potentcorrectionsfromalgebraicliftswithfinitesupport. Theassistantnotedthatthereviewedstable-
finiteness results assumed surjunctivity [12, 13]. Neither those conditional results nor characteristic-
zeropositivitysettledthecharacteristic-twocaseinitsanalysis. Italsoaskedwhetherthegluedgroup
might be virtually special, sofic, or surjunctive, which would obstruct the proposed counterexample.
Later it recalled Slofstra’s embedding theorem for solution groups and his nonclosure result for quan-
tumcorrelationsasreasonstoquestionwhetherlocalcommutingconstraintsmustadmitfaithfulfinite-
dimensionalrealizations[35,36].
The investigation of the candidate’s compatibilitywith known structuralfiniteness results remained
open.
19 Testing the candidate against finiteness and geometry
Therecordedattemptrepeatedlyreconstructeditsproposedcharacteristic-twocounterexampletodirect
finiteness, the implication 𝑎𝑏 = 1 ⇒ 𝑏𝑎 = 1 in a group algebra. Its own construction used a regular
hypergraph,vectors𝑥 ∈ 𝐾𝑚,andlocalgroupsoforder𝜅 = ℓ2,withℓodd. Theintendedidentitieswere
𝑣
∑𝑥 𝑥T = 𝐼 , ∑𝑥 𝑥T = 0, 𝑚 < 𝑡 < 𝑚𝜅.
𝑣 𝑣 𝑚 𝑣 𝑣
𝑣 𝑣∈𝑓
Subgroupaveragesweresupposedtoyield𝑈𝑇 = 𝐼 ;character-basedpackingandafinite-groupmatrix
𝑚
block would convert this into scalar elements with unequal reverse product. Augmentation supplied
theproposedrankobstruction. Thedraftconnecteditsfinite-groupenlargementtothedirect-to-stable-
finitenessreductionofDykema,Heister,andJuschenko[17]. ItalsoacknowledgedGolowichandLin’s
multiplication-property construction and Dinur, Liu, and Zhang’s prescribed aﬀine-line tests as influ-
encesonitspolynomialpairings,whileusingnocoding-theorytheoremasaproofdependency[22,15].
Thescrutinyshiftedbetweenalgebra,geometry,andcombinatorics. Afinitequotientpreservingevery
localgroupwouldcontradict𝑚 > 𝑡/𝜅,butnonpositivecurvaturedidnotfurnishsuchaquotient. Proper
edgecoloringswereblockedbythepolynomialidentities. Liftingthoseidentitiestocharacteristiczero
also failed: summing over lines multiplies the global pairing by the degree, which vanishes only in
the chosen characteristic. The assistant used Bartels, Lück, and Reich’s discussion of stable finiteness
andprojective-moduleclassestocheckwhetherFarrell–Jonestheorysuppliedthemissingpositivity;it
foundthatthecitedargumentretainedaseparatestable-finitenessassumption[6].
VERBATIMEXCERPT
FJ computes K0 as abelian group with action but not monoid positivity.
Theassistantlaterreturnedtoreconstructingthecandidatefromitsabstractidentities.

Kaplanskydirectfinitenessincharacteristictwo 17
The assistant checked stable-finiteness theorems of Ceccherini-Silberstein, Coornaert, and Phung,
whose conclusions retained a surjunctivity hypothesis [12, 13]. Rechecking planar embedding argu-
ments and local-lemma estimates found no decisive defect; a stronger exclusion of six-step polygons
remainedexploratory. Linnik’stheoremremainedasubstantialdependencyforpolynomiallybounded
primesintherequiredcongruenceclassesafterprime-powerreplacementsfailed[26].
Theassistantretainedthecandidateafterthesechecksandcontinuedtestingstructuralobstructions.
Its proposed exclusion of six-step polygons still required careful counting of repeated labels and
exceptional-line witnesses. In considering whether a stronger girth bound would force a familiar
geometric class, the assistant recalled Ollivier and Wise’s work on cubulating random groups and on
graphical small cancellation with Kazhdan subgroups. It treated these as comparisons and did not
establishthateitherresultappliedtoitsowngroup[29,30].
20 Repeated audits and an unused elementary alternative
The assistant repeatedly tested its proposed characteristic-two counterexample to direct finiteness
againstpossiblecombinatorial,representation-theoretic,andliftingobstructions.
The candidate combined a regular hypergraph of aﬀine lines, polynomial interpolation at removed
points, andglued finite subgroups. On rereading itsconstruction, theassistantretained itsattribution
of the low-degree line tests and multiplicative pairings to themes in the coding work of Golowich and
LinandofDinur,Liu,andZhang[22,15]. If𝑚pointswereremovedand𝑡 > 𝑚remained,interpolation
columnswereintendedtosatisfy
∑𝑥 𝑥T = −𝐼 , ∑𝑥 𝑥T = 0.
𝑣 𝑣 𝑚 𝑣 𝑣
𝑣 𝑣∈𝑓
Theassistantusedtheseidentitiestoruleoutperfectmatchings: theuncoveredverticesmustsupplya
rank-𝑚sumofrank-onematrices,requiringatleast𝑚uncoveredvertices. Initsconstruction,subgroup
averagesyielded𝑈𝑇 = 𝐼 ;compressionandcharacterspecializationwouldmakeareverseidentityim-
𝑚
plytheimpossiblerankinequality𝑡 ≤ 𝑚. Thesubgroup-embeddingargumentwasrecheckedthrough
planardegreeandfaceboundscontradictingEuler’sformula. Theconstructionalsoretaineditsconnec-
tion between a finite auxiliary group and matrix stable finiteness, attributed to Dykema, Heister, and
Juschenko[17];themodel-theoreticreferencerecalledDykemaandJuschenko’sprecisecriterionusing
allfinitedirectfactors[18].
Attempts to recover characteristic-zero positivity failed to preserve either finite support or real trace
equality:
VERBATIMEXCERPT
Trace is predetermined rational by p-adic cyclic calculation and formal terms, maybe real trace
differs even with simultaneous convergence; p-adic equality in infinite rational sums doesn't force
real equality.
The assistant rechecked that the stable-finiteness results it had consulted required surjunctivity [12,
13]. Itschecksoffinitequotients,random-subspaceindependence,shortpolygons,andmatchingheuris-
tics revealed no contradiction. It also revisited its comparison with Wise’s residual-finiteness theorem
foracute-angledpolygonsoffinitegroupswithatleastfoursides,whosescopedidnotcoverthetrian-
gularcomplexesitwasconsidering[39].
AsubsequentdetoursoughttoreplaceLinnik’stheorem[26],whichsuppliedtheoriginalprimepa-
rameters. Chebyshev’s prime-counting bound and a Rankin smooth-number estimate suggested vary-
ing the coeﬀicient characteristic and enlarging the local finite fields. The assistant estimated that the

Kaplanskydirectfinitenessincharacteristictwo 18
probabilisticconstructionmightsurvivetheresultinggrowingdimension,butretainedtheoriginalde-
pendency.
The assistant nevertheless returned to doubts about hidden global constraints, asking whether the
aﬀinegeometryanddegreeforcedshortcyclesthatitsestimateshadmissed. Itbeganextendingthepoly-
gonanalysistolengthsix,butleftthatextensionunfinishedandretainedtheoriginalprime-parameter
construction.
21 Testing the limits of a characteristic-two construction
The assistant repeatedly challenged its proposed failure of direct finiteness, the implication 𝑎𝑏 = 1 ⇒
𝑏𝑎 = 1forgroup-algebraelements.
First,refinedcountsofsix-steppolygonssuggestedstrengtheninganaﬀine-lineincidencegraphfrom
girthtwelvetofourteen. Combinedwithtriangleangles𝜋/7,𝜋/3,𝜋/2,thisraisedthespeculativepossi-
bilityofahyperbolicexample. ThesubsequentreconstructionretainedLinnik’stheorem[26]forchoos-
ing an odd prime ℓ with 𝐷 = ℓ + 1 divisible by a large power of the field order. Random subspaces,
sparseholes,andlocallinereplacementswereintendedtoproducearegularhypergraphwithnoshort
incidence cycles. The assistant continued using low-degree line tests and multiplicative pairings mo-
tivated by Golowich–Lin and Dinur–Liu–Zhang [22, 15], without invoking a coding-theory theorem.
Polynomialinterpolationsuppliedvectors𝑥 ∈ 𝐾𝑚,overcharacteristictwo,satisfying
𝑣
∑𝑥 𝑥T = 0, ∑𝑥 𝑥T = −𝐼 .
𝑣 𝑣 𝑣 𝑣 𝑚
𝑣∈𝑓 𝑣
Subgroup-averaging idempotents were then meant to yield 𝑈𝑇 = 𝐼 . Augmentation would obstruct
𝑚
the reverse identity through a rank comparison; an auxiliary finite-group matrix block would convert
the proposed matrix example into scalar elements, following the finite-factor connection discussed by
Dykema–Heister–Juschenko[17].
The assistant found no contradiction in its tests using finite quotients, coding theory, matchings, and
algebraic 𝐾-theory. It revisited Wise’s residual-finiteness theorem for acute-angled negatively curved
polygons of finite groups with at least four sides [39], but found no application to its triangular con-
struction. Its comparison with Bartels–Lück–Reich [6] distinguished additive projective classes from
positive dimensions: their stable-finiteness inputs had characteristic-zero or sofic hypotheses, so the
assistant did not derive the required conclusion from Farrell–Jones assembly alone. Summing the hy-
peredgeidentitiesalsoexposedwhythesameweightscouldnotsimplybeliftedtocharacteristiczero:
VERBATIMEXCERPT
Thus characteristic-p identity inherently due D=0. p-adic lift must alter supports adding
higher-order terms from nonlocal group elements; trace contradiction possible only if accidentally
still finite.
Rereadingthesurjunctivityresults[12,13],theassistantconfirmedthattheirstable-finitenessconclu-
sionsrequiredsurjunctivityhypotheses. Theremainingauditreturnedtowhetherlocalgroupssurvived
their gluing: planar degree and face-length bounds were compared with Euler’s formula, with partic-
ular attention to bridges and repeated boundaries. The assistant retained the proposal and continued
scrutinizingwhetherthelocalgroupssurvivedthegluing.
22 Repeated scrutiny of the proposed counterexample
Theclosingstagestestedtheassistant’sproposedcharacteristic-twocounterexampletodirectfiniteness:
finitegroup-algebrasumssatisfying𝑎𝑏 = 1but𝑏𝑎 ≠ 1.

Kaplanskydirectfinitenessincharacteristictwo 19
Theconstructioncombinedapuncturedaﬀinespaceover𝔽 ,low-degreeinterpolation,andfinitelocal
𝑞
groups𝐾 ≅ (ℤ/ℓ)2gluedalongcycliclinesubgroups. Primeselectionusedℓ ≡ −1 (mod 𝑞100)andcon-
𝑣
tinuedtodependonLinnik’stheorem[26]. Aproposedplanar-diagramargumentusedincidencegirth
twelve and degree bounds to contradict Euler’s formula, thereby defending the local groups’ embed-
dings. Averagingidempotentsthenenteredrectangularmatriceswith𝑈𝑇 = 𝐼 . Conjugatingelements
𝑚
andcharacterprojectionswereintendedtoproducesquarematriceswhosereverseidentitywouldforce
animpossiblerank-𝑚factorizationof 𝐼 , where𝑡 > 𝑚. Afinitegroup-algebrablockwouldconvertthis
𝑡
matrix obstruction into individual elements. The write-up connected this finite-factor step toDykema,
Heister,andJuschenko’sworkondirectandstablefiniteness[17]. Italsocreditedmultiplicationprop-
erties and prescribed aﬀine-line tests in the coding work of Golowich and Lin and of Dinur, Liu, and
Zhangasmotivationforitspolynomialpairing,whileusingnocodingtheoremasapremise[22,15].
The assistant rechecked the combinatorial probability estimates, interpolation, embeddings, and alge-
braic packing. It examined repeated polygon labels, distinct rectangle witnesses, and the number of
holesleftafterdeletingobstructions. Simpleretractionsavailableforgraphproductsfailedtoapplybe-
causeofthelocallineardependencies;itidentifiednoapplicableresidual-finitenesstheorem. Thecited
stable-finiteness theorems retained their surjunctivity hypothesis [12, 13], so the assistant found that
theydidnotsettletheunrestrictedtarget.
Integer lifts suggested a self-adjoint operator with a nonintegral rational spectral atom −1/2. The
assistantrecalledthealgebraic-eigenvalueworkofDodziuk,Linnell,Mathai,Schick,andYateswhileex-
ploringpossiblespectralobstructions[16]. Itfoundnouniversalexclusionapplicabletoitsconstruction.
Positivity and integral moments did not suﬀice, and the potentially large spectral range frustrated the
suggestedpolynomial-approximationargument. Complexunitaryapproximationlikewisesuppliedno
justifiedtransfertocharacteristictwo.
One correction concerned a speculative extension excluding six-step polygons: tenfold subspace in-
dependencewasinsuﬀicientbeforerepeatedlabelshadbeenestablished,sincetwelvesubspacescould
occur.
VERBATIMEXCERPT
Without direct for all six G, E labels may not repeat! For k≤5 count ≤10. k=6 not covered by
Vandermonde in n=10b.
Increasing the ambient dimension from 10𝑏 to 12𝑏 was proposed, followed by reconsideration of the
counting bounds. In testing this extension, it compared the proposed triangular complex with Wise’s
residual-finitenessresultsfornegativelycurvedpolygonsoffinitegroups[39]andwithhiscubulation
resultsforsmall-cancellationgroups[40]. Itquestionedwhethertherequiredpolygonorwallconditions
held. It also recalled Wise’s work on positive one-relator groups as another possible route, without
establishing applicability [41]. The assistant left its suggested negative-curvature, residual-finiteness,
anddeterminantconsequencesunexploredinitsfinalargument.
Part II: Gottschalk surjunctivity from one-sided inverses
Originalprompt(excerpts)
# Problem
Let G be any group and let A be a nonempty finite set. Write A^G for all functions x:G->A. A
cellular automaton with finite memory is a map tau:A^G->A^G for which there exist a finite subset M
of G and a function phi:A^M->A such that

Kaplanskydirectfinitenessincharacteristictwo 20
| tau(x)(g)=phi((x(gm))_{m |     |     | in M}) |     |     |     |
| ------------------------ | --- | --- | ------ | --- | --- | --- |
for every x in A^G and g in G. The same local function phi is used at every g.
Prove or disprove that every such injective map tau is surjective, for every choice of G,A,M,phi.
Injective means tau(x)=tau(y) implies x=y; surjective means every y in A^G has the form tau(x).
There is no assumption that G is finite, amenable, residually finite, sofic, or finitely presented.
A counterexample must give an allowed group and a finite-memory uniform local rule that is
| injective | but not   | surjective. |      |                    |     |     |
| --------- | --------- | ----------- | ---- | ------------------ | --- | --- |
| 23 From   | one-sided | inverses    | to a | cellular automaton |     |     |
The companion investigation asked whether every injective uniform cellular automaton on a full shift
over a finite alphabet must be surjective. Its starting context distinguished this unrestricted question
frompositiveresultsforsoficgroupsandfromresultsthatalreadyassumedsurjunctivity. Phung’swork
on non-uniform cellular automata supplied that contextual distinction [32]. A previous characteristic-
twoargumentassertedtheexistenceofafinitefield𝐾,agroup𝐺,andfinitesums𝑎,𝑏 ∈ 𝐾[𝐺]with𝑎𝑏 = 1
and 𝑏𝑎 ≠ 1. The assistant took that assertion as its input and sought the actual local rule, rather than
stoppingatthestatementthatthegroupwasnonsurjunctive.
The previous characteristic-two argument also referred to Elek and Szabó’s sofic-group theorem [19],
thegroupandmonoidsurjunctivitytheoremsofCeccherini-Silberstein,Coornaert,andPhung[13,12],
andthefinite-factorreductionofDykema,Heister,andJuschenko[17]. TheprescriptionusedLinnik’s
primebound,citedtherethroughXylouris[42],whilethepolynomialconstructioncreditedGolowich–
LinandDinur–Liu–Zhangasinspiration[22,15]. Thesereferencesenteredthroughthatargument;the
companionconversionretaineditssingleinputoffinite-fieldelementswithunequalone-sidedproducts.
Theconversiontook𝐴 = 𝐾 andassociatedtoeveryfinitesum𝑐 = ∑ 𝑐 𝑢themap
𝑢 𝑢
|     |     |     | 𝑇 (𝑥)(𝑔) | = ∑ 𝑐 𝑥(𝑔𝑢), | 𝑥 ∈ 𝐾𝐺. |     |
| --- | --- | --- | -------- | ------------ | ------- | --- |
|     |     |     | 𝑐        | 𝑢            |         |     |
𝑢∈𝐺
Finite support of 𝑐 makes the sum finite even when 𝑥 is an arbitrary configuration. For 𝜏 = 𝑇 , the
𝑏
memory is 𝑀 = supp(𝑏) and the uniform rule is 𝜙(𝑝) = ∑ 𝑏 𝑝(𝑢). The same coeﬀicients apply at
𝑢∈𝑀 𝑢
| every𝑔,andfinitenessof𝐾 |     | makesthisafinitealphabet. |     |     |     |     |
| ----------------------- | --- | ------------------------- | --- | --- | --- | --- |
Theassistantimmediatelycheckedthesideonwhichmultiplicationappeared:
VERBATIMEXCERPT
Correct order? T_c(x)(g) = ∑ c_m x(gm). (T_a(T_b(x)))(g)= ∑ a_h b_k x(ghk). T_bT_a = T_{ba}. So
yes.
Groupingthefinitedoublesumby𝑢𝑣gives𝑇 ∘𝑇 = 𝑇 . Thus𝑇 ∘𝑇 = 𝑇 = id,and𝑇 isinjective. The
|     |     |     |     | 𝑐 𝑑 𝑐𝑑 | 𝑎 𝑏 1 | 𝑏   |
| --- | --- | --- | --- | ------ | ----- | --- |
assistantcheckedtheorderbecause𝐺neednotbecommutative,andchose𝑏forthedesiredautomaton.
Toobtainnonsurjectivity,theassistantusedthenonzerocoeﬀicientof𝑏𝑎−1. Chooseℎwith(𝑏𝑎) ≠
ℎ
(1) andlet𝑦 = 𝛿 betheconfigurationequalto1 atℎandzeroelsewhere. Everyconfigurationinthe
| ℎ        | ℎ          |     |            | 𝐾            |         |     |
| -------- | ---------- | --- | ---------- | ------------ | ------- | --- |
| imageof𝑇 | isfixedby𝑇 | 𝑇 = | 𝑇 ,whereas |              |         |     |
|          | 𝑏          | 𝑏 𝑎 | 𝑏𝑎         |              |         |     |
|          |            |     | 𝑇 (𝑦)(𝑒)   | = (𝑏𝑎) ≠ (1) | = 𝑦(𝑒). |     |
|          |            |     | 𝑏𝑎         | ℎ            | ℎ       |     |
Consequently this particular 𝑦 has no preimage. The argument uses the full shift, not just finitely sup-
portedinputs;thedeltaconfigurationservesonlyasthewitnessoutsidetheimage.

Kaplanskydirectfinitenessincharacteristictwo 21
The assistant returned repeatedly to the distinction between this implication and an equivalence of
thetwoconjecturaltargets:
VERBATIMEXCERPT
Our use is not identifying equivalence; direct finite failure gives one counterexample, no reverse.
It also considered replacing the witness group by a familiar ambient group, such as Sym(ℕ), through
an embedding of the countable group. It kept the original group and its finite sums instead. The final
write-upspecifiedthecharacteristic-twotheoremanditsprescribedwitnesses,gavethelocalruleabove,
and concluded with the explicit configuration outside its image. The companion argument’s mathe-
maticaldependencyremainedthesuppliedone-sided-inversetheorem;itdidnotreconstructtheaﬀine
incidenceconstructionthatproduced𝑎and𝑏.
References
[1] Béla Andrásfai, Paul Erdős, and Vera T. Sós. On the connection between chromatic number, maximal
clique and minimal degree of a graph. Discrete Mathematics 8(3) (1974), 205–218. https://doi.org/
10.1016/0012-365X(74)90133-2.
[2] PereAra,KevinC.O’Meara,andFrancescPerera.StableFinitenessofGroupRingsinArbitraryChar-
acteristic.AdvancesinMathematics 170(2)(2002), 224–238. https://doi.org/10.1006/aima.2002.
2075.
[3] AlexArkhipov.ExtendingandCharacterizingQuantumMagicGames.arXivpreprintarXiv:1209.3819
(2012).https://arxiv.org/abs/1209.3819.
[4] GülBalciandGeorgesSkandalis.Tracesongroup𝐶∗-algebras,soficgroupsandLück’sconjecture.Expo-
sitionesMathematicae34(4)(2016),353–363.https://doi.org/10.1016/j.exmath.2015.12.008.
[5] BoazBarak,ZeevDvir,AviWigderson,andAmirYehudayoff.RankBoundsforDesignMatriceswith
ApplicationstoCombinatorialGeometryandLocallyCorrectableCodes.Proceedingsofthe43rdAnnual
ACMSymposiumonTheoryofComputing(2011),519–528.https://doi.org/10.1145/1993636.19
93705.
[6] ArthurBartels,WolfgangLück,andHolgerReich.OntheFarrell-JonesConjectureanditsapplications.
JournalofTopology1(1)(2008),57–86.https://doi.org/10.1112/jtopol/jtm008.
[7] Federico Berlai. Groups satisfying Kaplansky’s stable finiteness conjecture. arXiv preprint
arXiv:1501.02893(2015).https://arxiv.org/abs/1501.02893.
[8] EnricoBombieriandJeffreyD.Vaaler.OnSiegel’slemma.InventionesMathematicae73(1983),11–
32.https://doi.org/10.1007/BF01393823.
[9] SergeyBravyi,DavidPoulin,andBarbaraTerhal.Tradeoffsforreliablequantuminformationstoragein
2Dsystems.PhysicalReviewLetters104(5)(2010),050503.https://doi.org/10.1103/PhysRevLett.
104.050503.
[10] Martin R. Bridson and André Haefliger. Metric Spaces of Non-Positive Curvature. Springer,
Grundlehren der mathematischen Wissenschaften 319 (1999). https://doi.org/10.1007/978-3
-662-12494-9.

Kaplanskydirectfinitenessincharacteristictwo 22
[11] NicolaasGovertdeBruijnandPaulErdős.Onacombinatorialproblem.ProceedingsoftheKoninkli-
jke Nederlandse Akademie van Wetenschappen 51(10) (1948), 1277–1279. https://pure.tue.nl/
ws/portalfiles/portal/4300528/597479.pdf.
[12] Tullio Ceccherini-Silberstein, Michel Coornaert, and Xuan Kien Phung. Stable finiteness of monoid
algebras and surjunctivity. Theoretical Computer Science 1042 (2025), 115228. https://doi.org/10
.1016/j.tcs.2025.115228.
[13] TullioCeccherini-Silberstein,MichelCoornaert,andXuanKienPhung.First-ordermodeltheoryand
Kaplansky’sstablefinitenessconjectureforsurjunctivegroups.Groups,Geometry,andDynamics19(2)
(2025),495–503.https://doi.org/10.4171/GGD/885.
[14] HenryCohnandChristopherUmans.Agroup-theoreticapproachtofastmatrixmultiplication.Proceed-
ings of the 44th Annual IEEE Symposium on Foundations of Computer Science (2003), 438–449.
https://doi.org/10.1109/SFCS.2003.1238217.
[15] Irit Dinur, Siqi Liu, and Rachel Yun Zhang. New Codes on High Dimensional Expanders. 40th Com-
putational Complexity Conference (CCC 2025), Leibniz International Proceedings in Informatics
339(2025),27:1–27:42.https://doi.org/10.4230/LIPIcs.CCC.2025.27.
[16] Józef Dodziuk, Peter Linnell, Varghese Mathai, Thomas Schick, and Stuart Yates. Approximating
𝐿2-invariants, and the Atiyah conjecture. Communications on Pure and Applied Mathematics 56(7)
(2003),839–873.https://doi.org/10.1002/cpa.10076.
[17] KenDykema,TimoHeister,andKateJuschenko.FinitelypresentedgroupsrelatedtoKaplansky’sDirect
FinitenessConjecture.ExperimentalMathematics24(3)(2015),326–338.https://doi.org/10.1080/
10586458.2014.993051.
[18] KenDykemaandKateJuschenko.Onstablefinitenessofgrouprings.AlgebraandDiscreteMathemat-
ics19(1)(2015),44–47.https://admjournal.luguniv.edu.ua/index.php/adm/article/view/1174.
[19] Gábor Elek and Endre Szabó. Sofic groups and direct finiteness. Journal of Algebra 280(2) (2004),
426–434.https://doi.org/10.1016/j.jalgebra.2004.06.023.
[20] GilesGardam.Acounterexampletotheunitconjectureforgrouprings.AnnalsofMathematics194(3)
(2021),967–979.https://doi.org/10.4007/annals.2021.194.3.9.
[21] GilesGardam.Non-trivialunitsofcomplexgrouprings.arXivpreprintarXiv:2312.05240(2023).https:
//arxiv.org/abs/2312.05240.
[22] Louis Golowich and Ting-Chun Lin. Quantum LDPC Codes with Transversal Non-Clifford Gates via
Products of Algebraic Codes. Proceedings of the 57th Annual ACM Symposium on Theory of Com-
puting (2025), 689–696. Preprint: arXiv:2410.14662, https://arxiv.org/abs/2410.14662. https:
//doi.org/10.1145/3717823.3718139.
[23] DavidGross,VincentNesme,HolgerVogts,andReinhardF.Werner.Indextheoryofonedimensional
quantumwalksandcellularautomata.CommunicationsinMathematicalPhysics310(2)(2012),419–
454.https://doi.org/10.1007/s00220-012-1423-1.
[24] Dongning Guo, Shlomo Shamai, and Sergio Verdú. Mutual Information and Minimum Mean-square
Error in Gaussian Channels. IEEE Transactions on Information Theory 51(4) (2005), 1261–1282. ht
tps://doi.org/10.1109/tit.2005.844072.
∗
[25] ZhengfengJi,AnandNatarajan,ThomasVidick,JohnWright,andHenryYuen.MIP = RE.arXiv
preprintarXiv:2001.04383(2020).https://arxiv.org/abs/2001.04383.

Kaplanskydirectfinitenessincharacteristictwo 23
[26] YuriVladimirovichLinnik.Ontheleastprimeinanarithmeticprogression.I.Thebasictheorem.Recueil
Mathématique(Nouvellesérie)15(57)(2)(1944),139–178.https://www.mathnet.ru/eng/sm6196.
[27] Russell Lyons and Fedor Nazarov. Perfect Matchings as IID Factors on Non-Amenable Groups. Euro-
peanJournalofCombinatorics32(7)(2011),1115–1125.https://doi.org/10.1016/j.ejc.2011.03.
008.
[28] Aareyan Manzoor. Invariant Random Subgroups, Soficity, and Lück’s determinant conjecture. arXiv
preprintarXiv:2508.15154(2025).https://arxiv.org/abs/2508.15154.
[29] YannOllivierandDanielT.Wise.Cubulatingrandomgroupsatdensitylessthan1/6.Transactionsof
theAmericanMathematicalSociety363(9)(2011),4701–4733.https://doi.org/10.1090/s0002-9
947-2011-05197-4.
[30] YannOllivierandDanielT.Wise.Kazhdangroupswithinfiniteouterautomorphismgroup.Transactions
of the American Mathematical Society 359(5) (2007), 1959–1976. https://doi.org/10.1090/S000
2-9947-06-03941-9.
[31] Donald S. Ornstein and Benjamin Weiss. Entropy and isomorphism theorems for actions of amenable
groups.Journald’AnalyseMathématique48(1)(1987),1–141.https://doi.org/10.1007/bf027903
25.
[32] Xuan Kien Phung. On Gottschalk’s surjunctivity conjecture for non-uniform cellular automata. arXiv
preprintarXiv:2503.23435(2025).https://arxiv.org/abs/2503.23435.
[33] BrandonSeward.Bernoullishiftswithbasesofequalentropyareisomorphic.JournalofModernDynam-
ics18(2022),345–362.https://doi.org/10.3934/jmd.2022011.
[34] BrandonSeward.Krieger’sfinitegeneratortheoremforactionsofcountablegroupsII.JournalofModern
Dynamics15(2019),1–39.https://doi.org/10.3934/jmd.2019012.
[35] WilliamSlofstra.Tsirelson’sproblemandanembeddingtheoremforgroupsarisingfromnon-localgames.
JournaloftheAmericanMathematicalSociety33(1)(2020),1–56.https://doi.org/10.1090/jams
/929.
[36] WilliamSlofstra.Thesetofquantumcorrelationsisnotclosed.ForumofMathematics,Pi7(2019),e1.
https://doi.org/10.1017/fmp.2018.3.
[37] Andreas Thom. Sofic groups and diophantine approximation. Communications on Pure and Applied
Mathematics61(8)(2008),1155–1171.https://doi.org/10.1002/cpa.20217.
[38] Andreas Thom. Integer operators in finite von Neumann algebras. Journal of Topology and Analysis
3(4)(2011),433–450.https://doi.org/10.1142/s1793525311000635.
[39] DanielT.Wise.Theresidualfinitenessofnegativelycurvedpolygonsoffinitegroups.InventionesMath-
ematicae149(3)(2002),579–617.https://doi.org/10.1007/s002220200224.
[40] Daniel T. Wise. Cubulating small cancellation groups. Geometric and Functional Analysis 14(1)
(2004),150–214.https://doi.org/10.1007/s00039-004-0454-y.
[41] Daniel T. Wise. The residual finiteness of positive one-relator groups. Commentarii Mathematici Hel-
vetici76(2)(2001),314–338.https://doi.org/10.1007/pl00000381.
[42] TriantafyllosXylouris.OntheleastprimeinanarithmeticprogressionandestimatesforthezerosofDirich-
let𝐿-functions.ActaArithmetica150(1)(2011),65–91.https://doi.org/10.4064/aa150-1-4.
