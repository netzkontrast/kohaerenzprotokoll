---
drive_id: "github:openai/math@adc7f12/reasoning_traces/spontaneous-magnetization-quantum-heisenberg-ferromagnet.pdf"
title: "OpenAI math — Reasoning summary: Spontaneous magnetization in the quantum Heisenberg ferromagnet"
slug: "openai-math-trace-spontaneous-magnetization-quantum-heisenberg-ferromagnet"
category: "theorie-mathematik"
tier: "T2-theory"
index_date: "2026-10-06"
fetched: "2026-10-07"
---

QuantumHeisenbergferromagnet 1
Summarized chain of thought (Spontaneous magnetization in the
quantum Heisenberg ferromagnet)
OpenAI
Originalprompt(excerpts)
# Problem
For every integer d>=3 and spin S in {1/2,1,3/2,...}, consider the nearest-neighbor isotropic
quantum Heisenberg ferromagnet on Z^d at coupling J=1 and zero external field. At a site use
C^(2S+1) with orthonormal basis e_m, m=-S,-S+1,...,S, and define S^z e_m=m e_m, S^+
e_m=sqrt(S(S+1)-m(m+1)) e_(m+1), with S^+ e_S=0. Put S^-=(S^+)^*, S^x=(S^++S^-)/2 and
S^y=(S^+-S^-)/(2i). The operator S_x^a acts on site x.
For a finite subset Lambda of Z^d, the free-boundary Hamiltonian is
H_Lambda=-sum_{{x,y} subset Lambda: |x-y|_1=1} sum_(a=x,y,z) S_x^a S_y^a,
where each unordered edge is counted once. Let A be the norm completion of the union of all
finite-site matrix algebras, and let tau_t be the infinite-volume time evolution obtained as the
norm limit on local observables of exp(it H_Lambda) A exp(-it H_Lambda) along increasing boxes.
This finite-range interaction defines the limit independently of the exhausting boxes.
A state omega is a positive linear functional on A with omega(1)=1. For finite beta>0, call it an
equilibrium Gibbs state if it satisfies the beta-KMS condition for tau: for all A,B in A there is a
bounded function F_(A,B), continuous on 0<=Im z<=beta and analytic in its interior, with
F_(A,B)(t)=omega(A tau_t(B)) and F_(A,B)(t+i beta)=omega(tau_t(B)A) for real t. Translation
invariance means omega(T_x(A))=omega(A) for every lattice translation T_x.
Prove or refute that for every d and S specified above there is a finite beta_0(d,S)>0 such that
for every finite beta>=beta_0 there exists a translation-invariant beta-KMS state omega with
(omega(S_0^x),omega(S_0^y),omega(S_0^z)) != (0,0,0).
The state may depend on beta,d,S. The target is a zero-field state with spontaneous magnetization
at every sufficiently low positive temperature. It imposes no magnetization requirement on the
rotation-invariant mixture and asserts no pointwise-correlation equivalence. A negative resolution
must give some fixed d,S and arbitrarily large finite beta for which every translation-invariant
equilibrium state has zero magnetization.
1 From comparison attempts to a simultaneous pin test
Thereasoningbeginswithlonginterchangecycles,correlations,fieldderivatives,andmagnetizedevents
ofsubextensivefree-energycost. Seiringer’saccountandthespin-wavefree-energyresultofCorreggi–
Giuliani–Seiringersharpenthediﬀiculty: free-energycontrolalonedoesnotsupplytherequiredorder
parameter [7, 4]. A midpoint-aﬀinity comparison suggests averaging many normalized modifications
instead of paying for one long path. The unpredictable paths of Benjamini–Pemantle–Peres provide a
relatedgeometricidea[2]. NeithercomparisondirectlysuppliesatheoremimplyingHeisenbergorder.

QuantumHeisenbergferromagnet 2
The assistant reconstructs Tóth’s interchange representation [8]. It also recalls Nishimori-type dis-
order comparisons, tentatively compares Elboim–Sly’s high-dimensional unweighted interchange re-
sultwiththeloop-weightedmodelhere,andconsidersthegeneralized-loopframeworksofAizenman–
NachtergaeleandUeltschi[5,1,9]. Complexrotationsandtheclassicaloctopusinequalitylikewisefail
to close its lower-bound argument [6, 3]. Planting paths incurs exponential color costs; current shifts
meetboundedspincapacity;smallmeandefectdensitypermitstrappingwalls. Anaverageconnectivity
identityprovesinsuﬀicient:
VERBATIMEXCERPT
p relation yields self-consistency with arbitrary phase fraction! Can't bootstrap away because
| domain walls | cost etc. |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- |
Deleting labels leads to a conditional one-particle kernel on the remaining slots, called holes. Rank-
onetranspositionssuggestanexterior-poweridentityanddeterminantcancellation. Yetsignedminors
donotdirectlycontrolthepositiveeventthatmanytestsiteslieoninternalcycles.
| Theproposedchangeissymbolic: |     | startwith |        |       |     |
| ---------------------------- | --- | --------- | ------ | ----- | --- |
|                              |     | 𝐹(𝑋,𝑌)    | = 𝔼∏(𝑋 | +𝑌 ). |     |
|                              |     |           | 𝑖      | 𝜋(𝑖)  |     |
𝑖
Identifyinganeliminatedvertex’stwovariablesandextractingtheirlinearcoeﬀicientsplicesthepermu-
tation, contributing two when a cycle closes. The proposed contraction preserves stability and hence
givesnegativedependencefortheinducedoutputset. Thisleadstosparsesimultaneouspintestsand
adownwardinductionoverpinsets. Short-timeleakagemaycontroltherequiredescapecapacity,but
thegeometryanduniformestimatesremaintobesupplied.
| 2 A proposed | proof through | geometry | and heat | leakage |     |
| ------------ | ------------- | -------- | -------- | ------- | --- |
Spin 𝑆 is represented by ℓ = 2𝑆 spin-one-half slots with an on-site symmetric projection. The identity
s ⋅s = 𝑃 /2−𝐼/4givesrate-1/2exchanges;uniformwithin-sitepermutationsimplementtheprojection.
𝑖 𝑗 𝑖𝑗
| Underthepinlawℙ | ,cyclesmissing𝐷haveweighttwo,andℬ |     |     |                 |                      |
| --------------- | --------------------------------- | --- | --- | --------------- | -------------------- |
|                 | 𝐷                                 |     |     | 𝐷 istheirunion. | Boundaryslotsatevery |
| timeform𝐷 .     |                                   |     |     |                 |                      |
0
For old pins 𝐸 and a disjoint same-time test set 𝑇, put 𝑃 = 𝐸 ∪ 𝑇, 𝑚 = |𝑇|. The claimed stability
argumentgives
|     |     | ℙ (𝑇 | ⊆ ℬ ) ≤ | (2𝑟)𝑚, |     |
| --- | --- | ---- | ------- | ------ | --- |
|     |     | 𝐸    | 𝐸       |        |     |
where 𝑟 is the mean fraction of 𝑇 whose next pin is againin 𝑇, under ℙ . Exposing the cyclesmissing
𝑃
𝑃 leavesaholeprocesssubjecttoeveryremainingcyclehitting𝑃. Theexteriorcalculationidentifiesits
next-pinfirstmoment.
|     |     |     | 𝑝𝑚  |     | 𝐿(1+ℎ)𝛼. |
| --- | --- | --- | --- | --- | -------- |
The proposed induction seeks ℙ 𝐸 (𝑇 ⊆ ℬ 𝐸 ) ≤ for tests with growth at most It takes
𝛼 = 1/100,𝜈 = 1/(100𝑑),𝑠 = 𝑝−11/10,𝑅 ≍ 𝑠,and𝛽 ≥ 5𝑠. Markinsertionboundsthe𝑛thfactorialmeasure
by2𝑛timesitsbasevalue. Sparsebranchingwitnessesthencontrollargeblockedcomponents. Atregular
times,localdetoursyieldaNashinequality;thickeningandfillingdistantcomponentspermitsrouting
flowsaroundtheirshells.
𝑈∗𝑓
For the boundary-killed period kernel 𝑈, the hitting function satisfies 𝑓 = 1 on 𝑇 and = 𝑓 off 𝑇,
giving
|     |     | 𝑚(1−𝑟) | ≥ 𝔼 ⟨𝑓,(𝐼−𝑈)𝑓⟩. |     |     |
| --- | --- | ------ | --------------- | --- | --- |
𝑃
Writing𝑓 = 1 +𝑔, theassistantboundsbothearlyforwardandlatereverseleakage. Nashsmoothing
𝑇
controls the propagated test mass; a triangular time average absorbs its overlap with 𝑔 into gradient

QuantumHeisenbergferromagnet 3
dissipation. The residual terms include 𝑅𝛼𝑠−𝑑/2, 𝑅𝑑+𝛼𝑝2𝑑, and 𝑅𝛼/𝑠, all claimed to be 𝑜(𝑝). This closes
theproposedpininduction.
A boundary-up color condition then has surface-order cost, supplies a magnetized spectral tail, and
permitsasmall-fieldselectionfollowedbyatranslation-averagedKMSlimit.
Thenextstepistoexaminetheconstructionmoreclosely,beginningwithconditioningandthesigns
intheexterior-poweridentity.
3 Separating exposure from conditional first moments
The next stage concentrates on whether exposing all cycles missing the pins leaves the correct law on
the remaining slots. For a deterministic initial label set 𝐴 , let 𝐹 require its paths to close and avoid
0 𝐴
0
𝑃,andlet𝐺 requireeverycomplementarycycletohit𝑃. Theirconjunctionidentifiestheexposedset
𝐴
0
uniquely. Theweightedmeasurecanthereforebeexpandedusing
∑1 2#cycles(𝐴 0 )1 .
𝐹 𝐺
𝐴0 𝐴0
𝐴
0
Two clock families separate exchanges involving specified labels from exchanges between holes. The
former determine the exposed trajectories; after those trajectories are fixed, the latter operate on deter-
ministic available intervals. Revealing the specified mappings at the end of the period leaves uniform
completions. Theremaining-cyclecondition𝐺 stillhastobeimposed.
𝐴
0
Before that condition, the layered permutation Π and its mean 𝐾 satisfy the proposed identity
𝑘 𝑘
𝔼⋀ Π = ⋀ 𝐾. Inadeterminantexpansionwitharbitrarymatrix𝑊,cyclesconfinedtononpinvertices
𝑄 give zero. A Schur complement and the terms linear in 𝑊 identify the conditional mean next-pin
kernelas
𝐾 +𝐾 (𝐼−𝐾 )−1𝐾 .
𝑃′𝑃′ 𝑃′𝑄 𝑄𝑄 𝑄𝑃′
Here 𝑃′ retains the test pins and uses finitely many boundary cuts. Positive conditioning probability
supplies invertibility; a closed nonpin class would contradict it, so the finite nonpin block is transient.
Increasing the boundary cuts densely then passes to continuous boundary pinning, with the exposed
datafixed. Thisidentifiesaconditionalfirstmoment,withoutidentifyingthefullpathlaw.
Thecomparisonwalkrefreshesitscomplementaryrandomnessoneachcircuit;itdoesnotrepeatthe
actualconditionedlooptrajectory.
Asecondissueisthedifferencebetweenmassandpointwisecontrol. Forthekilledtransitionoperator
𝐶 , column sums bound mass, but row sums are also needed for 0 ≤ 𝐶 1 ≤ 1. Describing killed
𝑢 𝑢 𝑇
transitionsasaveragesofpartialbijectionssuppliesboth. Irregularanchorsarepaidforindividuallyin
expectation, avoiding a union over the entire test set. The flow estimate is applied at the same time as
theenergyitabsorbs,withoutrequiringall-timeregularity.
Thegeometriccheckalsoidentifiesadetailtomakeexplicit: representativesatasurvivingsitemust
agree across routed edges if their divergences are to cancel. The state construction is checked on both
KMSstripboundaries.
4 Making the routing and stopping rules precise
Theinvestigationtestswhethertheconstructionwouldinadvertentlyprovemorethanintended. Elimi-
natingacycleproducesweighttwo;dividingthatbiasawayneednotpreservestability. Negativedepen-
denceofpin-outputsetsisalsodistinctfrompositiveequilibriumspincorrelations. Aconstantfunction
in a reflecting box and transports that reconcentrate mass provide further tests. Boundary killing and
normlossduringdiffusionareessentialtotheproposedresponses.

QuantumHeisenbergferromagnet 4
Thestoppingruleisclarifiednext. Ignoringinteriorpinsmeansrelaxingthestoppingcriterionofthe
samewalk,whilekeepingtheexposedenvironmentanditslawfixed. Onlythecomplementaryrandom-
ness is refreshed. The expectation in the quadratic-form bound averages over exposed environments,
andallauxiliaryconstantsarefixedbeforechoosingthesmallparameter𝑝.
Fortheflow,onesurvivingslotischosenateverysiteusedbytheroutings. Ashortlocalconnection
transfers the requested source to its representative. Finite preimages alone, however, do not justify ex-
changingsumsinaninfiniteflow. Localizationmustfirstshowthatonly𝐶(1+ℎ)𝑑𝜈 originaledgescan
use a target edge at distance ℎ. This establishes local finiteness before the divergence calculation and
retainsthecombinedenergybound𝐶𝑚𝑅𝛼.
The escape estimate receives the same careful separation of random objects. An actual ℙ picture
𝑃
suppliestheforcedjumps;freshindependentclockssupplyholemotion. Leavingthe𝑅-ballrequires𝑅
chronological spatial marks from these two families. An interval shorter than one period never reuses
anactualmark,evenacrossthetimecut. Countingorderedchoicesgives𝐶𝑅(2𝑠)𝑅/𝑅!,henceexponential
decayfor𝑅 = 𝐶 𝑠. Reversepropagationusesadjointsofkilledpathmatrices,notinversediffusion.
∗
Themagnetizationargumentmakestheconditionalprobabilityabove𝑆/2explicitbeforeapplyingthe
surface-costcomparison.
Thenextchecksreturntothedistinctionbetweentheindependentcompletionlawanditscyclecon-
ditioning,thentohullgeometryanddissipation. Theheatcalculationremainsunderscrutiny.
5 Testing the construction against traps and correlations
The proposed negative dependence is tested against ferromagnetic correlations. The answer distin-
guishestheopenincoming/outputexperimentfromtheclosedspin-colorequilibriumdistribution. The
existingrestrictionisreiterated:
VERBATIMEXCERPT
In particular we do not assume negative dependence under the path exposure.
Conditioning is reconstructed separately for each deterministic 𝐴 branch of finite-jump trajectories.
0
Thedeterminantcalculationistieddirectlytodet(𝐼−𝐵) = ∑ (−1)𝑘tr(⋀ 𝑘 𝐵),withindependentinterval
𝑘
blocks and fixed layer relabelings. Dense-cut passage keeps the exposure fixed, and killing includes
startsatboundarysites. Thesedetailsareintendedtopreventtheconditionalfirstmomentfrombeing
usedasanequalityofpathlaws.
Time-dependent traps raise another question: could forced transports continually return diffused
mass to the source? Permutations cannot restore squared norm already lost to diffusion. For a broad
harmonicplateau,thesame-timeflowestimatechargespersistentoverlaptogradientenergy. Bothend
portionsremainnecessarybecause𝑈 neednotbeself-adjoint.
Theroutingcheckpermitsahullrepresentativetolieinanotherhull. Themapisappliedonce,rather
thanrepeatedlyuntilreachingafixedpoint;divergenceiscomputedfromtheoriginalpreimages. Com-
moncanonicalslotsandalocalsourcecorrectionpreservecancellation. Theoverlapestimatesplitsinto
contributionsneareachcenterandaconvergentdyadictail,using𝑑−2−2𝑑𝜈 > 𝛼.
Finally, let 𝒟 (𝑔 ) be half the sum of squared edge gradients on the surviving-slot graph at time 𝑢.
𝑢 𝑢
2𝑠
Exchanging the order of integration produces the positive term 2∫ 𝑊(𝑢)𝒟 (𝑔 )𝑑𝑢. The triangular
𝑠 𝑢 𝑢
weightssatisfy
2(2𝑠−𝑢) (2𝑠−𝑢)2 2𝑠 𝑤(𝑢)2 4
𝑤(𝑢) = , 𝑊(𝑢) = , ∫ 𝑑𝑢 = .
𝑠2 𝑠2 𝑠 𝑊(𝑢) 𝑠

QuantumHeisenbergferromagnet 5
Young’sinequalitygivestherequired𝐶𝑚𝑅𝛼/𝑠costwithoutatemporallyregularchoiceofflows. After
rechecking the spectral tail and KMS passage, the assistant turns again to global objections that might
escapealocalcalculation.
6 Closing the estimates and selecting the state
The final stage makes the dependence of the conditional law explicit. The marginal distribution of an
exposedhistoryisweightedbytheunconditionedprobabilityof𝐺 . Giventhathistory,theremaining
𝐴
0
picture is the independent completion law conditioned on 𝐺 ; the exterior-power calculation comes
𝐴
0
beforethiscondition. Pintimesaretakenmodulo𝛽,andpositive-durationsitevisitsjustifydetectionby
denseboundarycuts.
Thesparse-witnesscountischeckedateveryradius. Boundedcopyingmultiplicityandboundedcon-
gestioncontrolthelocalNashcomparison. Fortheglobalflow,anamed-endpointconstructionhandles
𝑛+𝑑−1
anedgejoiningtwohulls,andthe( )nonnegativecompositionsatlevel𝑛explainthedecayofthe
𝑑−1
outwardlatticeflow. Onlythepropagationquantitiesbeingaveragedneedthestatedmeasurability.
Theinductionerroriscollectedintoasingleuniformbound,
𝜀(𝑝) = 𝐶[𝑒−𝑐𝑠+𝑅𝛼(𝑠−𝑑/2+𝛿+𝑠−1)] = 𝑜(𝑝), 𝑟 ≤ 𝜀(𝑝),
where 𝛿 = 𝐶𝑅𝑑𝑝2𝑑 + 𝐶𝑒−𝑐𝑅𝜉 , for fixed 𝜉 > 0, bounds the probability of irregularity for one anchor
at a fixed time. Choosing 𝑝 once with 2𝜀(𝑝) ≤ 𝑝 is intended to close the induction and set 𝛽 = 5𝑠.
0
The stability argument also separates the Poisson approximation from the end permutations, whose
convergencetouniformisexplainedthroughapositivecommonuniformpart.
For𝑀 = ∑ 𝑆𝑧,thezero-fieldspectrallawℙ satisfiestheclaimedsurface-costbound
𝑥∈Λ 𝑥 0
1
ℙ (𝑀/|Λ| ≥ 𝑆/2) ≥ exp(−𝐶 |𝜕Λ|).
0 2 𝛽,𝑑,𝑆
Tiltingthislawby𝑒𝛽ℎ𝑀 suppressesmagnetizationbelow𝑆/4atfixedℎ > 0asthevolumegrows. Grow-
ingboxesandfieldsℎ ↓ 0areselecteddiagonally,thenthestatesareaveragedovertranslations. Oneach
fixedKMSstrip,localreal-timeconvergencesuppliesbothboundaryvalues;Gaussiandampingandthe
maximumprinciplegivetheanalyticlimit,extendedbynormapproximation.
Thefinalresponseclaimsatranslation-invariantzero-fieldKMSstatewithpositivemagnetizationat
eachsuﬀicientlylowpositivetemperature;𝑆/4appearsinthefield-selectionestimate.
References
[1] Michael Aizenman and Bruno Nachtergaele. Geometric Aspects of Quantum Spin States. Communi-
cationsinMathematicalPhysics164(1994),17–63.https://doi.org/10.1007/BF02108805.
[2] ItaiBenjamini,RobinPemantle,andYuvalPeres.UnpredictablePathsandPercolation.TheAnnalsof
Probability26(3)(1998),1198–1211.https://doi.org/10.1214/aop/1022855749.
[3] PietroCaputo,ThomasM.Liggett,andThomasRichthammer.ProofofAldous’spectralgapconjecture.
Journal of the American Mathematical Society 23(3) (2010), 831–851. https://doi.org/10.1090/
S0894-0347-10-00659-4.
[4] Michele Correggi, Alessandro Giuliani, and Robert Seiringer. Validity of the Spin-Wave Approxi-
mation for the Free Energy of the Heisenberg Ferromagnet. Communications in Mathematical Physics
339(1)(2015),279–307.https://doi.org/10.1007/s00220-015-2402-0.

QuantumHeisenbergferromagnet 6
[5] Dor Elboim and Allan Sly. Infinite cycles in the interchange process in five dimensions. Preprint,
arXiv:2211.17023(2022;revised2024).https://arxiv.org/abs/2211.17023.
[6] OliverA.McBryanandThomasSpencer.OntheDecayofCorrelationsinSO(n)-symmetricFerromag-
nets.CommunicationsinMathematicalPhysics53(1977),299–302.https://doi.org/10.1007/BF01
609854.
[7] Robert Seiringer. The Heisenberg ferromagnet: a dilute Bose gas in disguise. Workshop contribution
in Mini-Workshop: New Directions in Correlated Quantum Systems, Oberwolfach Report No. 7/2025
(2025),357–358.https://doi.org/10.4171/OWR/2025/7.
[8] BálintTóth.ImprovedLowerBoundontheThermodynamicPressureoftheSpin1/2HeisenbergFerromag-
net.LettersinMathematicalPhysics28(1)(1993),75–84.https://doi.org/10.1007/BF00739568.
[9] Daniel Ueltschi. Random loop representations for quantum spin systems. Journal of Mathematical
Physics54(8)(2013),083301.https://doi.org/10.1063/1.4817865.
