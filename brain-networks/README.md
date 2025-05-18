# Нейросети мозга

```mermaid
graph TD
    TPN[TPN] --> DLPFC[DLPFC]
    TPN --> ACC[ACC]
    TPN --> PPC[PPC]

    DMN[DMN] --> mPFC[mPFC]
    DMN --> PCC_Precuneus[PCC/Precuneus]
    DMN --> Medial_Temporal_Lobes[Medial Temporal Lobes]

    MD[MD] --> DLPFC
    MD --> Insula[Insula]
    MD --> PPC

    SN[SN] --> Anterior_Insula[Anterior Insula]
    SN --> ACC

    CEN[CEN] --> DLPFC
    CEN --> PPC

    DAN[DAN] --> SPL[SPL]
    DAN --> FEF[FEF]

    VAN[VAN] --> TPJ[TPJ]
    VAN --> Ventrolateral_PFC[Ventrolateral PFC]

    Visual_Network[Visual Network] --> V1[V1]
    Visual_Network --> V2[V2]
    Visual_Network --> V3[V3]
    Visual_Network --> V4[V4]
    Visual_Network --> V5[V5]

    SMN[SMN] --> Motor_Cortex[Motor Cortex]
    SMN --> Somatosensory_Cortex[Somatosensory Cortex]

    Limbic_Network[Limbic Network] --> Amygdala[Amygdala]
    Limbic_Network --> Hippocampus[Hippocampus]
    Limbic_Network --> OFC[OFC]

    Language_Network[Language Network] --> Brocas_Area[Broca’s Area]
    Language_Network --> Wernickes_Area[Wernicke’s Area]
    Language_Network --> Arcuate_Fasciculus[Arcuate Fasciculus]

    Auditory_Network[Auditory Network] --> Heschls_Gyrus[Heschl’s Gyrus]
    Auditory_Network --> STG[Superior Temporal Gyrus]

    Cerebellar_Network[Cerebellar Network] --> Anterior_Lobules[Anterior Lobules]
    Cerebellar_Network --> Posterior_Lobules[Posterior Lobules]

    Basal_Ganglia_Network[Basal Ganglia Network] --> Caudate[Caudate Nucleus]
    Basal_Ganglia_Network --> Pallidum[Pallidum]
    Basal_Ganglia_Network --> Subthalamic_Nucleus[Subthalamic Nucleus]

    FPCN[Frontoparietal Control Network] --> Lateral_PFC[Lateral PFC]
    FPCN --> IPL[Inferior Parietal Lobule]

    Temporal_Parietal_Network[Temporal-Parietal Network] --> TPJ
    Temporal_Parietal_Network --> Middle_Temporal_Gyrus[Middle Temporal Gyrus]

    Posterior_Multimodal_Network[Posterior Multimodal Network] --> Posterior_Parietal_Cortex[Posterior Parietal Cortex]
    Posterior_Multimodal_Network --> Parieto_Occipital[Parieto-occipital Junction]

    Cingulo_Opercular_Network[Cingulo-Opercular Network] --> ACC
    Cingulo_Opercular_Network --> Anterior_Insula

    Orbitofrontal_Network[Orbitofrontal Network] --> OFC
    Orbitofrontal_Network --> NAcc[Nucleus Accumbens]

    Frontopolar_Network[Frontopolar Network] --> Frontopolar_Cortex[BA10]

    Reward_Network[Reward Network] --> Ventral_Striatum[Ventral Striatum]
    Reward_Network --> vmPFC[Ventromedial PFC]
    Reward_Network --> OFC

    MTL_Memory_Network[MTL Memory Network] --> Hippocampus
    MTL_Memory_Network --> Entorhinal_Cortex[Entorhinal Cortex]
    MTL_Memory_Network --> Parahippocampal_Cortex[Parahippocampal Cortex]

    Parieto_Occipital_Network[Parieto-Occipital Network] --> Posterior_Parietal_Lobe[Posterior Parietal Lobe]
    Parieto_Occipital_Network --> Dorsal_Occipital_Cortex[Dorsal Occipital Cortex]

    Mirror_Neuron_System[Mirror Neuron System] --> Premotor_Cortex[Premotor Cortex]
    Mirror_Neuron_System --> Inferior_Parietal_Lobule[Inferior Parietal Lobule]

    Reading_Network["Reading (Visual Word‑Form) Network"] --> Ventral_Occipito_Temporal[Ventral Occipito‑Temporal Cortex]

    Affective_Network[Affective Network] --> Amygdala
    Affective_Network --> vmPFC
    Affective_Network --> Insula

    Cerebro_Cerebellar_Cognitive_Network[Cerebro‑Cerebellar Cognitive Network] --> Cerebellum
    Cerebro_Cerebellar_Cognitive_Network --> Frontal_Cortex[Frontal Cortex]

    Fronto_Striatal_Network[Fronto‑Striatal Network] --> DLPFC
    Fronto_Striatal_Network --> Caudate

    Right_FPCN[Right-Hemisphere FPCN] --> Right_Lateral_PFC[Right Lateral PFC]
    Right_FPCN --> Right_IPL[Right IPL]

    Ventral_Stream["Ventral Stream (“What” Pathway)"] --> V4
    Ventral_Stream --> Ventral_Temporal_Cortex[Ventral Temporal Cortex]

    Dorsal_Stream["Dorsal Stream (“Where/How” Pathway)"] --> V3A
    Dorsal_Stream --> Superior_Parietal_Lobule

    Anterior_Temporal_Network[Anterior Temporal Network] --> Anterior_Temporal_Lobe[Anterior Temporal Lobe]

    Parietal_Memory_Network[Parietal Memory Retrieval Network] --> Mid_Parietal_Cortex[Mid-Parietal Cortex]
    Parietal_Memory_Network --> PCC

    CAN[Central Autonomic Network] --> Anterior_Insula
    CAN --> mPFC
    CAN --> NTS[Nucleus of the Solitary Tract]
    CAN --> Hypothalamus
    CAN --> Amygdala

    Thalamo_Cortical_Network[Thalamo‑Cortical Network] --> Thalamus
    Thalamo_Cortical_Network --> Cortex

    Interoceptive_Network[Interoceptive Network] --> Posterior_Insula
    Interoceptive_Network --> Somatosensory_Cortex
    Interoceptive_Network --> Cingulate_Cortex

    Pain_Matrix[Pain Matrix] --> Insula
    Pain_Matrix --> ACC
    Pain_Matrix --> Somatosensory_Cortex
    Pain_Matrix --> Thalamus

    Vestibular_Network[Vestibular Network] --> Brainstem_Vestibular_Nuclei
    Vestibular_Network --> Parietal_Vestibular_Cortex
    Vestibular_Network --> Temporo_Parietal_Cortex

    Olfactory_Network[Olfactory Network] --> Olfactory_Bulb
    Olfactory_Network --> Piriform_Cortex
    Olfactory_Network --> OFC

    Gustatory_Network[Gustatory Network] --> Anterior_Insula
    Gustatory_Network --> Inferior_Frontal_Operculum
    Gustatory_Network --> Anterior_Temporal_Cortex

    RAS[Reticular Activating System] --> Brainstem_RF[Brainstem Reticular Formation]
    RAS --> Cortex

    Hippocampal_Neocortical_Memory_Network[Hippocampal‑Neocortical Memory Network] --> Hippocampus
    Hippocampal_Neocortical_Memory_Network --> Entorhinal_Cortex
    Hippocampal_Neocortical_Memory_Network --> PCC
    Hippocampal_Neocortical_Memory_Network --> mPFC

    Precuneus_PPC_Network[Precuneus‑Posterior Parietal Network] --> Precuneus
    Precuneus_PPC_Network --> Posterior_Parietal_Cortex

    Fronto_Limbic_Network[Fronto‑Limbic Network] --> mPFC
    Fronto_Limbic_Network --> OFC
    Fronto_Limbic_Network --> Amygdala

    Sensorimotor_Integration_Network --> Premotor_Cortex
    Sensorimotor_Integration_Network --> SMA
    Sensorimotor_Integration_Network --> Parietal_Cortex

    Auditory_Motor_Network --> STG
    Auditory_Motor_Network --> Brocas_Area
    Auditory_Motor_Network --> SMA

    Subcortical_Arousal_Network --> Brainstem
    Subcortical_Arousal_Network --> Thalamus
    Subcortical_Arousal_Network --> Basal_Nucleus_Meynert

    Cerebellar_Prefrontal_Loop --> Prefrontal_Cortex
    Cerebellar_Prefrontal_Loop --> Posterior_Cerebellum
```


> Мозг человека представляет собой сложный ансамбль функционально взаимосвязанных сетей, каждая из которых отвечает за определённые аспекты восприятия, движения, когнитивного контроля и эмоциональной регуляции. От базовых сенсомоторных и зрительных контуров до высокоуровневых систем управления вниманием и памяти — эти сети обеспечивают координацию нейронной активности, позволяя эффективно обрабатывать внешние стимулы и внутренние потребности. В представленном списке систем выделены 50 ключевых сетей, характеризующихся специфическими областями включения и функциональными ролями, что служит основой для дальнейшего изучения их взаимодействий и значимости в контексте нормального функционирования и патологий.


---


## **1. Task-Positive Network (TPN)**

Подробнее: [Task-Positive Network (TPN)](/brain-networks/task-positive-network-tpn.md)

**Ключевая функция:**
Активируется при целенаправленной работе и решении задач, требующих когнитивного контроля. ([PMC][1])

**Анатомия:**

* Dorsolateral Prefrontal Cortex (DLPFC) — высшие исполнительные функции;
* Anterior Cingulate Cortex (ACC) — мониторинг конфликтов и ошибок;
* Posterior Parietal Cortex (PPC) — пространственное и селективное внимание. ([PMC][1])

**Ключевые тракты / подсети:**

* Фронто-париетальная сеть (соединение DLPFC ↔ PPC через superior longitudinal fasciculus);
* Цингуло-оперкулярный пучок (ACC ↔ оперкулярная кора);
* Фронто-стритальные пути (DLPFC ↔ базальные ганглии).

**Ключевые обзоры:**

* Silton & Miller, 2017 — “Distinct Roles for the Anterior Cingulate and Dorsolateral Prefrontal…” (PMC) ([PMC][1])
* Dosenbach et al., 2007 — “A Dual-Network Architecture of Top-Down Control” (Trends in Cognitive Sciences).

---

## **2. Default Mode Network (DMN)**

Подробнее: [Default Mode Network (DMN)](/brain-networks/default-mode-network-dmn.md)

**Ключевая функция:**
Активна в покое, саморефлексии и «дневном мечтании». ([ScienceDirect][2])

**Анатомия:**

* Medial Prefrontal Cortex (mPFC) — саморефлексия;
* Posterior Cingulate Cortex / Precuneus (PCC) — интеграция внутренних состояний;
* Медиальные височные доли (включая hippocampus) — память и воображение. ([ScienceDirect][2], [Nature][3])

**Ключевые тракты / подсети:**

* Цингуло-париетальный тракт (соединение PCC ↔ mPFC);
* Медиальный продольный фаший (hippocampus ↔ mPFC).

**Ключевые обзоры:**

* Buckner & DiNicola, 2019 — “Twenty years of the default mode network: A review and synthesis” (Neuron) ([ScienceDirect][2])
* Murphy et al., 2020 — “Functional parcellation of the default mode network” (Scientific Reports) ([Nature][3])

---

## **3. Multiple-Demand Network (MD)**

Подробнее: [Multiple-Demand Network (MD)](/brain-networks/multiple-demand-network-md.md) 

**Ключевая функция:**
Гибкая сеть для решения разнообразных когнитивных задач, универсальный «операционный слой». ([Nature][4])

**Анатомия:**

* DLPFC — планирование и контроль;
* Insula — интеграция межочаговой информации;
* PPC — перераспределение ресурсов внимания. ([Nature][4])

**Ключевые тракты / подсети:**

* Фронто-париетальные пути;
* Цингуло-оперкулярный компонент MD;
* Короткие ассоциативные пучки insula ↔ PFC.

**Ключевые обзоры:**

* Assem et al., 2024 — “A multi-demand operating system underlying diverse cognitive tasks” (Nature Communications) ([Nature][4])
* Duncan, 2010 — “The multiple-demand system of the primate brain” (Trends in Cognitive Sciences).

---

## **4. Salience Network (SN)**

Подробнее: [Salience Network (SN)](/brain-networks/salience-network-sn.md)

**Ключевая функция:**
Выделяет значимые стимулы и переключает между режимами покоя (DMN) и задач (TPN/CEN). ([PMC][5])

**Анатомия:**

* Anterior Insula — обнаружение интероцептивных сигналов;
* ACC — интеграция эмоциональных и когнитивных данных. ([The Journal of Neuroscience][6])

**Ключевые тракты / подсети:**

* Цингулярный фаший;
* Фронто-оперкулярные волокна (insular ↔ inferior frontal gyrus).

**Ключевые обзоры:**

* Seeley et al., 2007 — “Saliency, switching, attention and control…” (PMC) ([PMC][5])
* Uddin, 2015 — “Salience Network: A Neural System for Perceiving and…” (Journal of Neuroscience) ([The Journal of Neuroscience][6])

---

## **5. Central Executive Network (CEN)**

Подробнее: [Central Executive Network (CEN)](/brain-networks/central-executive-network-cen.md)

**Ключевая функция:**
Управление рабочей памятью и принятием решений. ([ScienceDirect][7])

**Анатомия:**

* DLPFC — обновление рабочей памяти;
* PPC — селективное внимание и интеграция информации. ([PMC][8])

**Ключевые тракты / подсети:**

* Фронто-париетальные ассоциативные пути;
* Связи с basal ganglia через corona radiata.

**Ключевые обзоры:**

* Niendam et al., 2012 — “Meta-analytic evidence for a superordinate cognitive control network” (American Journal of Psychiatry)
* Engelmann et al., 2012 — “White matter integrity of central executive network correlates with…” (PMC) ([PMC][8])

---

## **6. Dorsal Attention Network (DAN)**

Подробнее: [Dorsal Attention Network (DAN)](/brain-networks/dorsal-attention-network-dan.md)

**Ключевая функция:**
Произвольное (топ-даун) удержание и ориентация внимания. ([ScienceDirect][9])

**Анатомия:**

* Superior Parietal Lobule (SPL) — пространственная ориентация;
* Frontal Eye Fields (FEF) — направленность взгляда и внимания. ([PMC][10])

**Ключевые тракты / подсети:**

* Фронто-париетальные ассоциативные: FEF ↔ SPL;
* Связи с visual cortex через магнитный фаший.

**Ключевые обзоры:**

* Corbetta & Shulman, 2002 — “Control of goal-directed and stimulus-driven attention in the brain” (Nature Reviews Neuroscience)
* Brett et al., 2021 — “Role of the dorsal attention network in distracter suppression…” (PMC) ([PMC][10])

---

## **7. Ventral Attention Network (VAN)**

Подробнее: [Ventral Attention Network (VAN)](/brain-networks/ventral-attention-network-van.md)

**Ключевая функция:**
Автоматическое переключение внимания на неожиданные и важные стимулы. ([ScienceDirect][11])

**Анатомия:**

* Temporoparietal Junction (TPJ) — обнаружение «вневременных» сигналов;
* Ventrolateral Prefrontal Cortex (VLPFC) — инициирование переключения внимания. ([PubMed][12])

**Ключевые тракты / подсети:**

* Arcuate fasciculus (TPJ ↔ VLPFC);
* Inferior fronto-occipital fasciculus (VLPFC ↔ occipital regions).

**Ключевые обзоры:**

* Corbetta & Shulman, 2008 — “Reorienting attention” (Neuron)
* Tang et al., 2019 — “Ventral attention-network effective connectivity predicts…” (PMC) ([PubMed][12])

---

## **8. Visual Network**

Подробнее: [Visual Network](/brain-networks/visual-network.md)

**Ключевая функция:**
Обработка и интеграция зрительной информации (от первичной до ассоциативных областей). ([PMC][13])

**Анатомия:**

* V1 (Primary Visual Cortex) — первичная обработка контуров и контраста;
* V2–V5 (Extrastriate Areas) — движение, форма, цвет;
* Латеральная теменная кора — зрительно-пространственные преобразования. ([ScienceDirect][14])

**Ключевые тракты / подсети:**

* Оптический луч (optic radiation);
* Фасцикулизация V1 ↔ V5 через межкортикальные связи.

**Ключевые обзоры:**

* Felleman & Van Essen, 1991 — “Distributed hierarchical processing in the primate cerebral cortex” (Cerebral Cortex)
* Rela et al., 2024 — “The Connection from Cortical Area V1 to V5…” (PMC) ([PMC][13])

---

## **9. Somato-Motor Network (SMN)**

Подробнее: [Somato-Motor Network (SMN)](/brain-networks/somato-motor-network-smn.md)

**Ключевая функция:**
Сенсомоторная интеграция и контроль движений. ([PMC][15])

**Анатомия:**

* Primary Motor Cortex (M1) — исполнение движений;
* Primary Somatosensory Cortex (S1) — обратная сенсорная информация;
* Supplementary Motor Area (SMA) — планирование сложных движений. ([Nature][16])

**Ключевые тракты / подсети:**

* Corona radiata (M1 ↔ спинной мозг);
* Thalamocortical fibers (таламус ↔ моторная кора).

**Ключевые обзоры:**

* Biswal et al., 1995 — “Functional connectivity in the motor cortex of resting human brain” (Magnetic Resonance in Medicine)
* Dosenbach et al., 2023 — “A somato-cognitive action network alternates with effector regions…” (Nature) ([Nature][16])

---

## **10. Limbic Network**

Подробнее: [Limbic Network](/brain-networks/limbic-network.md)

**Ключевая функция:**
Регуляция эмоций, мотивации и памяти. ([ScienceDirect][17])

**Анатомия:**

* Amygdala — эмоциональная обработка и страх;
* Hippocampus — формирование и консолидация памяти;
* Orbitofrontal Cortex (OFC) — оценка вознаграждений и принятие решений. ([NCBI][18])

**Ключевые тракты / подсети:**

* Fornix (hippocampus ↔ mammillary bodies);
* Uncinate fasciculus (OFC ↔ медиальные височные доли).

**Ключевые обзоры:**

* MacLean, 1952 — “The Triune Brain in Evolution” (Plenum Press)
* Catani et al., 2013 — “A revised limbic system model for memory, emotion and behaviour” (Neuroscience & Biobehavioral Reviews) ([ScienceDirect][17])



---



## **11. Language Network (LN)**

Подробнее: [Language Network (LN)](/brain-networks/language-network-ln.md)

**Ключевая функция:**
Восприятие, анализ и производство языка, от фонологической обработки до синтаксиса и семантики ([PMC][19], [aimspress.com][20]).

**Анатомия:**

* Broca’s area (левый BA44/45) — продукция речи;
* Wernicke’s area (левый posterior STG/MTG) — понимание речи;
* Arcuate fasciculus — магистральный тракт «вперед-назад». ([PMC][19])

**Ключевые тракты / подсети:**

* Тракт Аркуат (аркуатный пучок Broca ↔ Wernicke);
* Прямой лингвистический путь (через нижнюю продольную извилину);
* Короткие ассоциативные связи вокруг латеральной борозды Sylvian.

**Ключевые обзоры:**

* Price C.J., 2010 — “The anatomy of language: a review of 100 fMRI studies published in 2009”, Ann. N. Y. Acad. Sci. ([PMC][19])
* Friederici A.D., 2011 — “The brain basis of language processing: from structure to function”, Physiol. Rev. ([aimspress.com][20])

---

## **12. Auditory Network (AN)**

Подробнее: [Auditory Network (AN)](/brain-networks/auditory-network-an.md)

**Ключевая функция:**
Обработка и кодирование звуковых стимулов от примитивных характеристик до распознавания речи и музыки ([aimspress.com][20], [Europe PMC][21]).

**Анатомия:**

* Heschl’s gyrus (первичная слуховая кора) — анализ частоты и интенсивности;
* Superior Temporal Gyrus (ассоциативная слуховая кора) — распознавание фонем и звуковых объектов. ([Europe PMC][21])

**Ключевые тракты / подсети:**

* Дорсальный слуховой тракт (MGB ↔ A1);
* Вентральный слуховой путь (A1 ↔ STG/MTG);
* Связи с фронтальным речевым ядром (через минутные пучки).

**Ключевые обзоры:**

* Rauschecker J.P. & Scott S.K., 2009 — “Maps and streams in the auditory cortex: nonhuman primates illuminate human speech processing”, Nat. Neurosci. ([aimspress.com][20])
* Hickok G. & Poeppel D., 2007 — “The cortical organization of speech processing”, Nat. Rev. Neurosci. ([Europe PMC][21])

---

## **13. Cerebellar Network (CBN)**

Подробнее: [Cerebellar Network (CBN)](/brain-networks/cerebellar-network-cbn.md)

**Ключевая функция:**
Координация моторики и участие в когнитивных и эмоциональных процессах через предсказательные внутренние модели ([PubMed][22]).

**Анатомия:**

* Anterior lobules (I–V) — соматомоторные функции;
* Posterior lobules (VI–VIII) — когнитивные и эмоциональные связи;
* Crus I/II — рабочая память и язык. ([PubMed][22])

**Ключевые тракты / подсети:**

* Мозжечково-таламические пути (через dentate nucleus ↔ thalamus ↔ PFC);
* Мозжечково-мостовые фибры (cerebral cortex ↔ pons ↔ cerebellum);
* Мозжечково-спинальные тракты (для моторных выходов).

**Ключевые обзоры:**

* Buckner R.L. et al., 2011 — “The organization of the human cerebellum estimated by intrinsic functional connectivity”, J. Neurophysiol. ([PubMed][22])
* Buckner R.L., 2013 — “The cerebellum and cognitive function: 25 years of insight from anatomy and neuroimaging”, Neuron ([Википедия][23])

---

## **14. Basal Ganglia Network (BGN)**

Подробнее: [Basal Ganglia Network, (BGN)](/brain-networks/basal-ganglia-network-bgn.md)

**Ключевая функция:**
Регуляция мотивации, выбор действий и процедурного обучения через множество параллельных петель ([PubMed][24]).

**Анатомия:**

* Caudate nucleus — когнитивные петли;
* Putamen — моторные петли;
* Substantia nigra / STN — модуляция дофамином. ([PubMed][24])

**Ключевые тракты / подсети:**

* Nigrostriatal pathway (SNc ↔ striatum);
* Pallidothalamic fibers (GPi ↔ thalamus ↔ cortex);
* Striato-pallidal «прямая» и «непрямая» цепи.

**Ключевые обзоры:**

* Di Martino A. et al., 2008 — “Functional connectivity of human striatum: a resting state fMRI study”, Cereb. Cortex ([PubMed][24])
* Haber S.N. & Knutson B., 2010 — “The reward circuit: linking primate anatomy and human imaging”, Neuropsychopharmacology

---

## **15. Frontoparietal Control Network (FPCN)**

Подробнее: [Frontoparietal Control Network (FPCN)](/brain-networks/frontoparietal-control-network-fpcn.md)

**Ключевая функция:**
Гибкий когнитивный контроль, мультизадачность и переключение между целями ([Nature][25]).

**Анатомия:**

* Lateral PFC (BA9/46) — поддержка целей и стратегий;
* Inferior Parietal Lobule (IPL) — перераспределение ресурсов внимания. ([PubMed][26])

**Ключевые тракты / подсети:**

* Фронто-париетальные ассоциативные пути (через superior longitudinal fasciculus);
* Связи с basal ganglia для интеграции мотивации.

**Ключевые обзоры:**

* Cole M.W. et al., 2013 — “Multi-task connectivity reveals flexible hubs for adaptive task control”, Nat. Neurosci.
* Vincent J.L. et al., 2008 — “Evidence for a frontoparietal control system revealed by intrinsic functional connectivity”., J. Neurophysiol.

---

## **16. Temporal-Parietal Network (TPN)**

Подробнее: [Temporal-Parietal Network (TPN)](/brain-networks/temporal-parietal-network-tpn.md)

**Ключевая функция:**
Социальное познание (Theory of Mind), эмпатия и языковое взаимодействие ([ScienceDirect][27], [PMC][28]).

**Анатомия:**

* Temporo-Parietal Junction (TPJ) — распознавание чужих намерений;
* Middle Temporal Gyrus (MTG) — контекстуальное понимание. ([PMC][28])

**Ключевые тракты / подсети:**

* Связи TPJ ↔ mPFC через аркуатные и цингуло-париетальные волокна;
* Связи с лимбической системой (через uncinate fasciculus).

**Ключевые обзоры:**

* Schurz M. et al., 2014 — “Fractionating theory of mind: a meta-analysis of functional brain imaging studies”, Neurosci. Biobehav. Rev. ([ScienceDirect][27])
* Carter R.M. & Huettel S.A., 2013 — “A nexus model of the temporal–parietal junction”, Trends Cogn. Sci. ([Википедия][29])

---

## **17. Posterior Multimodal Network (PMN)**

Подробнее: [Posterior Multimodal Network (PMN)](/brain-networks/posterior-multimodal-network-pmn.md)

**Ключевая функция:**
Интеграция зрительных, слуховых и сомато-сенсорных данных для формирования целостного восприятия ([PubMed][26]).

**Анатомия:**

* Posterior Parietal Cortex (PPC) — мультисенсорная интеграция;
* Temporo-Occipital Junction — связывает визуальные и аудиальные входы. ([PubMed][26])

**Ключевые тракты / подсети:**

* Superior longitudinal fasciculus III (PPC ↔ temporal cortex);
* Inferior fronto-occipital fasciculus (occipital ↔ frontal regions).

**Ключевые обзоры:**

* Braga R.M. & Buckner R.L., 2017 — “Parallel interdigitated distributed networks within the individual estimated by intrinsic functional connectivity”, Neuron ([PubMed][26])
* Margulies D. S. et al., 2016 — “Situating the default-mode network along a principal gradient of macroscale cortical organization”, PNAS

---

## **18. Cingulo-Opercular Network (CON)**

Подробнее: [Cingulo-Opercular Network (CON)](/brain-networks/cingulo-opercular-network-con.md)

**Ключевая функция:**
Поддержание тонуса внимания и устойчивый контроль, мониторинг ошибок ([PubMed][30]).

**Анатомия:**

* Dorsal ACC — мониторинг конфликтов;
* Anterior Insula / Frontal Operculum — переключение и поддержание установок;
* Thalamus — глобальная интеграция. ([PubMed][30])

**Ключевые тракты / подсети:**

* Цингуло-оперкулярные волокна (dACC ↔ aI/fO);
* Связи с dorsolateral PFC для совместной работы с FPCN.

**Ключевые обзоры:**

* Dosenbach N.U.F. et al., 2008 — “A dual-networks architecture of top-down control”, Trends Cogn. Sci.
* Sadaghiani S. & D’Esposito M., 2014 — “Functional characterization of the cingulo-opercular network in the maintenance of tonic alertness”, Cereb. Cortex ([PubMed][30])

---

## **19. Orbitofrontal Network (OFN)**

Подробнее: [Orbitofrontal Network (OFN)](/brain-networks/orbitofrontal-network-ofn.md)

**Ключевая функция:**
Оценка вознаграждений/не-вознаграждений и эмоциональное принятие решений ([PMC][31], [PubMed][32]).

**Анатомия:**

* Medial OFC — представление позитивной ценности;
* Lateral OFC — кодирование наказаний и non-reward;
* Nucleus accumbens — интеграция дофаминовых сигналов. ([PubMed][32])

**Ключевые тракты / подсети:**

* Uncinate fasciculus (OFC ↔ medial temporal lobe);
* Ventral amygdalofugal pathway (amygdala ↔ OFC);
* Corticostriatalные проекции (OFC ↔ ventral striatum).

**Ключевые обзоры:**

* Rolls E.T., 2019 — “The orbitofrontal cortex: reward, emotion and depression”, Brain Commun. ([PMC][31], [PubMed][32])
* Rushworth M.F. et al., 2012 — “Valuation and decision making in frontal cortex”, Nat. Neurosci.

---

## **20. Frontopolar Network (FPN)**

Подробнее: [Frontopolar Network (FPN)](/brain-networks/frontopolar-network-fpn.md)

**Ключевая функция:**
Метакогниция, стратегическое планирование и интеграция нескольких целей ([PMC][33], [ResearchGate][34]).

**Анатомия:**

* Rostral PFC (BA10) — «ведущий шлюз» между stimulus-oriented и stimulus-independent процессами;
* Связи с dorsolateral PFC и DMN для координации сложных задач. ([PMC][33])

**Ключевые тракты / подсети:**

* Extreme capsule (BA10 ↔ STS);
* Uncinate fasciculus (BA10 ↔ temporal pole);
* Cingulum bundle (BA10 ↔ PCC/mPFC).

**Ключевые обзоры:**

* Burgess P.W. et al., 2005 — “The gateway hypothesis of rostral prefrontal cortex (area 10) function”, Trends Cogn. Sci. ([ResearchGate][35])
* Gilbert S.J. et al., 2005 — “Involvement of rostral prefrontal cortex in selection between stimulus-oriented and stimulus-independent thought”, Eur. J. Neurosci. ([ResearchGate][34])




---



## **21. Reward Network (RN)**

Подробнее: [Reward Network (RN)](/brain-networks/reward-network-rn.md)

**Ключевая функция:**
Оценка вознаграждения и мотивация через взаимодействие вентрального стрiatума и префронтальной коры ([PMC][36], [PMC][37]).

**Анатомия:**

* Nucleus Accumbens (VS) — кодирование ожидаемой ценности;
* Ventromedial PFC (vmPFC) — интеграция контекста и ценности;
* Orbitofrontal Cortex (OFC) — сравнение вариантов вознаграждения ([PMC][37]).

**Ключевые тракты / подсети:**

* Mesolimbic pathway (VTA ↔ NAcc);
* vmPFC ↔ NAcc через мост и переднюю часть капсулы;
* OFC ↔ ventral striatum через uncinate fasciculus.

**Ключевые обзоры:**

* Di Martino A. et al., 2008 — “Functional connectivity of human striatum: a resting state fMRI study”, Cereb. Cortex.
* Zhang W. et al., 2022 — “Reduced nucleus accumbens functional connectivity in reward circuits in MDD”, Transl. Psychiatry ([Nature][38]).

---

## **22. Medial Temporal Lobe Memory Network (MTL)**

Подробнее: [Medial Temporal Lobe Memory Network (MTL)](/brain-networks/medial-temporal-lobe-memory-network-mtl.md)

**Ключевая функция:**
Формирование и извлечение эпизодической (декларативной) памяти ([PubMed][39]).

**Анатомия:**

* Hippocampus (CA1–CA3, DG, Subiculum) — консолидирует новые воспоминания;
* Entorhinal Cortex — вход и выход информации в гиппокамп;
* Parahippocampal and Perirhinal Cortices — промежуточная обработка ассоциативных связей ([PubMed][40]).

**Ключевые тракты / подсети:**

* Fornix (hippocampus ↔ mammillary bodies);
* Entorhinal-hippocampal projections (perforant path);
* Cingulum bundle (MTL ↔ PCC/mPFC).

**Ключевые обзоры:**

* Squire L.R. & Wixted J.T., 2011 — “The cognitive neuroscience of human memory since H.M.”, Annu. Rev. Neurosci.
* Eichenbaum H., 2000 — “A cortical-hippocampal memory network”, Trends Cogn. Sci. ([PubMed][39], [PubMed][40]).

---

## **23. Parieto-Occipital Network (PON)**

Подробнее: [Parieto-Occipital Network (PON)](/brain-networks/parieto-occipital-network-pon.md)

**Ключевая функция:**
Интеграция визуально-пространственной информации для навигации и ориентации ([PMC][41], [Nature][42]).

**Анатомия:**

* Posterior Parietal Cortex (PPC, особенно SPL/IPS) — пространственное представление;
* Dorsal Occipital Cortex (cuneus, V3A) — анализ давних и локальных элементов сцены.

**Ключевые траты / подсети:**

* Superior longitudinal fasciculus II–III (occipital ↔ PPC);
* Optic radiations (LGN ↔ V1 ↔ dorsal stream).

**Ключевые обзоры:**

* Rauschecker J.P. & Scott S.K., 2009 — “Maps and streams in the auditory cortex…” (для сравнения путей), Nat. Neurosci.
* Vesia M. & Crawford J.D., 2012 — “Specialization of reach function in human posterior parietal cortex”, Exp. Brain Res. ([PMC][41], [Nature][42]).

---

## **24. Semantic/Language Comprehension Network (SCN)**

Подробнее: [Semantic/Language Comprehension Network (SCN)](/brain-networks/semanticlanguage-comprehension-network-scn.md)

**Ключевая функция:**
Семантическая обработка и интеграция смыслового контента языка ([The Journal of Neuroscience][43], [Nature][44]).

**Анатомия:**

* Inferior Frontal Gyrus (BA45/47) — семантический контроль;
* Middle/Inferior Temporal Gyri (MTG/ITG) — лексическое хранение;
* Angular Gyrus (AG) — мультисенсорная семантическая интеграция.

**Ключевые траты / подсети:**

* Arcuate fasciculus (в основном косой сегмент);
* Inferior fronto-occipital fasciculus (ITG ↔ OFC).

**Ключевые обзоры:**

* Lambon Ralph M.A. et al., 2017 — “The neural and computational bases of semantic cognition”, Nat. Rev. Neurosci.
* Price C.J., 2012 — “A review and synthesis of the first 20 лет of PET and fMRI studies of heard speech, spoken language and reading”, Neuroimage ([Nature][44], [The Journal of Neuroscience][43]).

---

## **25. Mentalizing (Theory-of-Mind) Network (MN)**

Подробнее: [Mentalizing (Theory-of-Mind) Network (MN)](/brain-networks/mentalizing-theory-of-mind-network-mn.md)

**Ключевая функция:**
Понимание и предсказание ментальных состояний других людей ([PMC][45], [ScienceDirect][46]).

**Анатомия:**

* Medial PFC — отражение собственных и чужих намерений;
* Temporo-Parietal Junction (TPJ) — различение сам/друг;
* Precuneus/PCC — интеграция рефлексивной информации.

**Ключевые траты / подсети:**

* Cingulum bundle (mPFC ↔ PCC/TPJ);
* Arcuate and longitudinal fasciculi (TPJ ↔ frontal regions).

**Ключевые обзоры:**

* Frith C.D. & Frith U., 2006 — “The neural basis of mentalizing”, Neuron.
* Schurz M. et al., 2014 — “Fractionating theory of mind: a meta-analysis…”, Neurosci. Biobehav. Rev. ([PMC][45], [ScienceDirect][46]).

---

## **26. Mirror Neuron System (MNS)**

**Ключевая функция:**
Имитация действий и понимание намерений через «зеркальную» активность премоторной и теменной коры ([PMC][47], [Nature][48]).

**Анатомия:**

* Premotor Cortex (BA6) — моторная репрезентация;
* Inferior Parietal Lobule (IPL, особенно area PF) — интеграция сенсомоторных сигналов.

**Ключевые траты / подсети:**

* Superior longitudinal fasciculus (premotor ↔ IPL);
* Arcuate fasciculus (IPL ↔ Broca’s area).

**Ключевые обзоры:**

* Rizzolatti G. & Sinigaglia C., 2010 — “The functional role of the parieto-frontal mirror circuit: interpretations and misinterpretations”, Nat. Rev. Neurosci.
* Gazzola V. & Keysers C., 2009 — “The observation and execution of actions share motor and somatosensory voxels in all tested subjects: single-subject analyses of unsmoothed fMRI data”, Cereb. Cortex ([PMC][47], [Nature][48]).

---

## **27. Reading (Visual Word-Form) Network (VWFA)**

**Ключевая функция:**
Визуальное распознавание и категоризация буквенных форм ([ScienceDirect][49], [eneuro.org][50]).

**Анатомия:**

* Visual Word-Form Area (VWFA) в левом окципитально-височном переходе;
* Lateral Occipital Cortex — предварительная обработка объектов;
* Posterior Fusiform Gyrus — интеграция глифов.

**Ключевые траты / подсети:**

* Inferior longitudinal fasciculus (occipital ↔ temporal);
* Vertical occipital fasciculus (VWFA ↔ dorsal stream).

**Ключевые обзоры:**

* Dehaene S. & Cohen L., 2011 — “The unique role of the visual word form area in reading”, Trends Cogn. Sci.
* Lerma-Usabiaga G. et al., 2018 — “Converging evidence for functional and structural segregation within the left ventral occipitotemporal cortex in reading”, PNAS ([ScienceDirect][49], [eneuro.org][50]).

---

## **28. Affective Network (ANet)**

**Ключевая функция:**
Обработка эмоциональной информации и регуляция настроения ([PMC][51], [PubMed][52]).

**Анатомия:**

* Amygdala — обнаружение эмоциональной значимости;
* Ventromedial PFC (vmPFC) — регуляция эмоциональных реакций;
* Insula — межоцептивная осведомлённость.

**Ключевые траты / подсети:**

* Uncinate fasciculus (vmPFC ↔ amygdala);
* Amygdalofugal pathway (amygdala ↔ basal forebrain).

**Ключевые обзоры:**

* Pessoa L., 2010 — “Emotion and cognition and the amygdala: from ‘what is it?’ to ‘what’s to be done?’”, Neuropsychologia.
* Etkin A. et al., 2011 — “Emotional processing in anterior cingulate and medial prefrontal cortex”, Trends Cogn. Sci. ([PMC][51], [PubMed][52]).

---

## **29. Cerebro-Cerebellar Cognitive Network (CCCN)**

**Ключевая функция:**
Участие мозжечка в когнитивном обучении и прогнозировании через петли с корой ([Nature][53], [PMC][54]).

**Анатомия:**

* Cerebellar Crus I/II — рабочая память и язык;
* Anterior Lobules (I–V) — моторные функции;
* Dentate Nucleus — главный выход мозжечка.

**Ключевые траты / подсети:**

* Cortico-pontine-cerebellar fibers (PFC ↔ pons ↔ cerebellum);
* Dentato-thalamic tract (dentate ↔ thalamus ↔ cortex).

**Ключевые обзоры:**

* Buckner R.L. et al., 2011 — “The organization of the human cerebellum estimated by intrinsic functional connectivity”, J. Neurophysiol.
* Ito M., 2008 — “Control of mental activities by internal models in the cerebellum”, Nat. Rev. Neurosci. ([Nature][53], [PMC][54]).

---

## **30. Fronto-Striatal Network (FSN)**

**Ключевая функция:**
Исполнительные функции и контроль импульсов через взаимодействие DLPFC и хвостатого ядра ([Nature][55], [PMC][36]).

**Анатомия:**

* Dorsolateral PFC (BA9/46) — рабочая память и когнитивный контроль;
* Caudate Nucleus — планирование действий и оценка стимулов.

**Ключевые траты / подсети:**

* Frontal–striatal fibers (через anterior limb of internal capsule);
* Corticostriatal loops (прямая и непрямая цепи DLPFC ↔ caudate ↔ GPi/SNr).

**Ключевые обзоры:**

* Haber S.N. & Knutson B., 2010 — “The reward circuit: linking primate anatomy and human imaging”, Neuropsychopharmacology.
* Robbins T.W. & Robbins B.J., 2012 — “Cognitive control and frontostriatal circuits in Parkinson’s disease”, Trends Cogn. Sci. ([Nature][55], [PMC][36]).


---

## 31. **Right-Hemisphere Frontoparietal Control Network (RH-FPCN)**

**Ключевая функция:**
Обеспечивает гибкое управление вниманием и целенаправленное поведение через взаимодействие с другими когнитивными сетями ([PMC][56]).

**Анатомия:**

* Латеральная префронтальная кора (LPFC)
* Медиальная префронтальная/передняя поясная кора (ACC)
* Нижняя теменная долька (IPL) ([PMC][56])

**Ключевые тракты / подсети:**

* Пучок верхней продольной связки (SLF II/III), особенно справа ([Academic Oxford][57])
* Взаимодействие с сенсомоторной и дефолтной сетями через гибкие «хабы» (flexible hubs) ([PMC][58])

**Ключевые обзоры:**

* Vincent & Snyder, 2010 — обзор флексибельных «хабов» в FPCN, *Trends in Cognitive Sciences* ([PMC][58])
* Cole et al., 2013 — концепция «гибких хабов» и их роль в когнитивном контроле, *Nature Reviews Neuroscience* ([PMC][56])

---

## 32. **Ventral Stream (“What” Pathway) (VSP)**

**Ключевая функция:**
Распознавание форм, объектов и лиц в условиях сложного визуального окружения ([PubMed][59]).

**Анатомия:**

* Первичная зрительная кора (V1) → V2 → V4
* Вентральная височная кора (Ventral Temporal Cortex, VTC) ([PubMed][60])

**Ключевые тракты / подсети:**

* Нижний продольный пучок (inferior longitudinal fasciculus)
* Связи с периринальной и энторинальной областями

**Ключевые обзоры:**

* Ungerleider & Haxby, 1994 — «‘What’ and ‘Where’ in the human brain», *Current Opinion in Neurobiology* ([Википедия][61])
* Grill-Spector & Weiner, 2014 — обзор макро- и микроанатомии VTC, *Nature Reviews Neuroscience* ([PubMed][60])

---

## 33. **Dorsal Stream (“Where/How” Pathway) (DSP)**

**Ключевая функция:**
Пространственная локализация, зрительно-моторная координация и управление движениями рук и глаз ([PubMed][59]).

**Анатомия:**

* V1 → V2 → V3A → зона средней височной коры MT/V5
* Верхняя теменная долька (SPL) ([PubMed][59])

**Ключевые тракты / подсети:**

* Пучок верхней продольной связки (SLF I/II)
* Интерконнекции с премоторными областями

**Ключевые обзоры:**

* Goodale & Milner, 1992 — основополагающая работа по разделению потоков, *Behavioral and Brain Sciences* ([PubMed][59])
* Rizzolatti & Matelli, 2003 — Аннотация двух подсистем в дорсальном потоке, *Neuroscience* ([Википедия][61])

---

## 34. **Anterior Temporal Network (ATN)**

**Ключевая функция:**
Обработка социальной и эмоциональной семантики, представление знаний о людях и объектах ([PMC][62]).

**Анатомия:**

* Передние отделы височной доли (антериальные височные поля)
* Мозговая миндалина (amygdala) и периринальная кора ([PMC][63])

**Ключевые тракты / подсети:**

* Uncinate fasciculus (связь с орбитофронтальной корой)
* Связи с лобными семантическими хабами

**Ключевые обзоры:**

* Olson et al., 2007 — роль AT в семантике и социальной когниции, *Current Opinion in Neurobiology* ([PMC][62])
* Patterson et al., 2007 — концепция «семантического хаба» в AT, *Trends in Cognitive Sciences* ([PMC][63])

---

## 35. **Parietal Memory Retrieval Network (PMN)**

**Ключевая функция:**
Извлечение эпизодической и семантической памяти, рализация воспоминаний и ориентация внимания на воспоминания ([PubMed][64]).

**Анатомия:**

* Средняя теменная долька (angular gyrus)
* Задняя поясная кора (posterior cingulate cortex) ([PubMed][64])

**Ключевые тракты / подсети:**

* Поясной пучок (cingulum bundle)
* Связь с медиальной префронтальной корой и гиппокампом

**Ключевые обзоры:**

* Wagner et al., 2005 — обзор корреляций PMN при вспоминании, *Nature Reviews Neuroscience* ([PubMed][64])
* Gilmore et al., 2015 — мульти-методный анализ PMN, *NeuroImage* ([ScienceDirect][65])

---

## 36. **Central Autonomic Network (CAN)**

**Ключевая функция:**
Регуляция вегетативных и гомеостатических функций через интеграцию висцеральных сигналов ([PubMed][66]).

**Анатомия:**

* Передняя островковая кора (anterior insula)
* Медиальная препефронтальная кора
* Ядро одиночного пути (NTS), гипоталамус, миндалина ([PubMed][66])

**Ключевые тракты / подсети:**

* Вагусные афферентные пути
* Связи с продолговатым мозгом и мозжечком

**Ключевые обзоры:**

* Benarroch, 1993 — анатомия и функции CAN, *Neurology* ([PubMed][66])
* Thayer & Lane, 2000 — нейрофизиологическая модель CAN и психофизиология, *Psychophysiology* ([ScienceDirect][67])

---

## 37. **Thalamo-Cortical Network (TCN)**

**Ключевая функция:**
Синхронизация корковых ритмов и эффективная передача сенсорной информации через таламус ([PubMed][68]).

**Анатомия:**

* Множество ядер таламуса (ретикулярное, вентральное постеролатеральное, медиальное ядро и др.)
* Связные корковые области: сенсорные, моторные и ассоциативные зоны ([PMC][69])

**Ключевые тракты / подсети:**

* Таламокортикальные лучи (thalamic radiations)
* Ретикулярная формация и таламический ретикулярный пучок

**Ключевые обзоры:**

* Sherman, 2016 — «Thalamus plays a central role in ongoing cortical functioning», *Nature Neuroscience* ([PubMed][68])
* Halassa & Sherman, 2019 — схемы таламокортикальных мотиваций, *Nature Reviews Neuroscience* ([PMC][69])

---

## 38. **Interoceptive Network (IN)**

**Ключевая функция:**
Восприятие внутренних состояний тела (сердцебиение, дыхание) и их интеграция в субъективные ощущения ([Nature][70]).

**Анатомия:**

* Задняя островковая кора (posterior insula)
* Сомато­сенсорная кора (S1)
* Поясная кора (ACC) ([PubMed][71])

**Ключевые тракты / подсети:**

* Спиноталамический тракт (передний и латеральный каналы)
* Связи между островком и баллаторными центрами

**Ключевые обзоры:**

* Craig, 2002 — сенсация внутреннего тела и роль островка, *Nature Reviews Neuroscience* ([Nature][70])
* Critchley et al., 2004 — нейровизуализация интероцептивных процессов, *Brain* ([PubMed][71])

---

## 39. **Pain Matrix (Nociceptive Network)**

**Ключевая функция:**
Обработка болевых сигналов, интеграция ноцицептивной информации и реакции на угрозы телу ([PMC][72]).

**Анатомия:**

* Островок (insula)
* Передняя поясная кора (ACC)
* Соматосенсорные зоны (S1/S2)
* Таламус ([PMC][72])

**Ключевые тракты / подсети:**

* Спиноталамический тракт
* Мезолимбическая система (минутая связь с миндалиной и PFC)

**Ключевые обзоры:**

* Apkarian et al., 2005 — «The pain matrix», *Nature Reviews Neuroscience* ([ScienceDirect][73])
* Wager et al., 2013 — нейровизуализация болевой реакции и сильное выделение в «матрице боли», *Journal of Neuroscience* ([PMC][72])

---

## 40. **Vestibular Network (VN)**

**Ключевая функция:**
Восприятие положения и движения головы, поддержание равновесия и ориентирование в пространстве ([PubMed][74]).

**Анатомия:**

* Вестибулярные ядра ствола мозга (vestibular nuclei)
* Теменно-височная область (parieto-insular vestibular cortex, PIVC)
* Височно-теменная зона (TPJ) ([PubMed][75])

**Ключевые тракты / подсети:**

* Вестибуло-таламические пути
* Связи с мозжечком и вестибулярным ядром

**Ключевые обзоры:**

* Lopez & Blanke, 2011 — обзор кортикальных областей вестибулярной системы, *Nature Reviews Neuroscience* ([PubMed][75])
* zu Eulenburg et al., 2012 — мета-анализ PIVC, *Cerebral Cortex* ([PubMed][74])


---



## 41. **Olfactory Network (ON)**

**Ключевая функция:**
Обработка обонятельной информации от первичной детекции до сложной перцепции запахов ([PMC][76]).

**Анатомия:**

* **Обонятельная луковица:** первичная проекция обонятельных рецепторов ([MIT Press Direct][77])
* **Переопорикальная кора (piriform cortex):** формирование «обонятельных образов» ([PMC][76])
* **Орбитофронтальная кора (OFC):** интеграция с оценкой запаховых качеств и эмоциональными реакциями ([MIT Press Direct][77])

**Ключевые тракты / подсети:**

* Моносинаптические проекции от луковицы в периринальную и энторинальную кору
* Связи OFC с лимбическими структурами (миндалина, гиппокамп)

**Ключевые обзоры:**

* Stenwall et al., 2025 — «The Bulb, the Brain and the Being», *Frontiers in Neuroanatomy* ([PMC][78])
* Elliott & Gottfried, 2021 — «Structural and functional connectomics of the olfactory system», *NeuroImage* ([ScienceDirect][79])

---

## 42. **Gustatory Network (GN)**

**Ключевая функция:**
Восприятие и дискриминация вкусовых качеств на разных уровнях обработки ([ScienceDirect][80]).

**Анатомия:**

* **Передняя островковая кора (aIns):** первичная вкусовая кора ([ScienceDirect][80])
* **Инсула (Insula):** интеграция вкусовой и висцеральной информации ([PMC][81])
* **Нижняя передняя височная кора (ventral anterior temporal):** семантическая ассоциация вкуса ([PNAS][82])

**Ключевые тракты / подсети:**

* Афферентные пути от NTS через таламус к островке
* Связи островка с OFC и системой вознаграждения

**Ключевые обзоры:**

* Small, 2010 — «The anterior insula in taste and attention», *Journal of Neuroscience* ([PMC][81])
* Veldhuizen et al., 2011 — «The anterior insular cortex represents breaches of taste identity», *Journal of Neuroscience* ([PMC][83])

---

## 43. **Reticular Activating System (RAS)**

**Ключевая функция:**
Поддержание бодрствования и регуляция переходов «сон – бодрствование» через модуляцию корковой возбудимости ([ScienceDirect][84]).

**Анатомия:**

* **Ретикулярная формация (RF) ствола мозга:** центральный узел arousal ([ScienceDirect][85])
* **Ядра моста и средней полоски (parabrachial):** проекции в дальные корковые области ([PMC][86])

**Ключевые тракты / подсети:**

* Восходящие проекции ARAS через таламус и гипоталамус
* Химические модуляторные пути (норадренергические LC, серотонинергические Raphe)

**Ключевые обзоры:**

* Jones, 2004 — «Reticular Activating System: consciousness and arousal», *Brain Research Reviews* ([ScienceDirect][84])
* Edlow et al., 2012 — «Neuroanatomic connectivity of the human ascending arousal system», *Journal of Comparative Neurology* ([PMC][86])

---

## 44. **Hippocampal-Neocortical Memory Network (HNMN)**

**Ключевая функция:**
Консолидация долгосрочной памяти путём постепенного перераспределения информации из гиппокампа в неокортекс ([PMC][87]).

**Анатомия:**

* **Гиппокамп (CA fields, DG):** кодирование и реконсолидация эпизодических воспоминаний ([PubMed][88])
* **Энторинальная кора:** интерфейс между гиппокампом и корой ([PubMed][88])
* **Медиальная PFC и PCC:** участники поздних этапов системной консолидации ([PMC][87])

**Ключевые тракты / подсети:**

* Перфорантный путь (entorhinal → DG → CA3)
* Цингулум (cingulum) для связи с PCC и мPFC

**Ключевые обзоры:**

* Eichenbaum, 2017 — «Memory consolidation and hippocampal–neocortical interactions», *Trends in Cognitive Sciences* ([PMC][87])
* Squire & Alvarez, 1995 — «Retrograde amnesia and memory consolidation», *Science* ([PubMed][88])

---

## 45. **Precuneus-Posterior Parietal Network (PPN)**

**Ключевая функция:**
Интеграция сенсорной, пространственной и саморефлексивной информации в рамках «заднего пояса» ([PubMed][89]).

**Анатомия:**

* **Прецентральная область (precuneus):** мультифункциональный хаб ([Academic Oxford][90])
* **Задняя теменная кора (posterior parietal cortex, PPC):** пространственная обработка и внимание ([PubMed][89])

**Ключевые тракты / подсети:**

* Связи с медиальной PFC
* Интеграция с дорсальным зрительным потоком через SLF

**Ключевые обзоры:**

* Cavanna & Trimble, 2006 — «The precuneus: functional anatomy and behavioural correlates», *Brain* ([PubMed][89], [Academic Oxford][90])
* Utevsky et al., 2014 — «Precuneus as central hub of default network», *Journal of Neuroscience* ([ResearchGate][91])

---

## 46. **Fronto-Limbic Network (FLN)**

**Ключевая функция:**
Регуляция эмоций и принятие решений путём топ-даун модуляции лимбических реакций ([ScienceDirect][92]).

**Анатомия:**

* **Медиальная PFC (mPFC):** когнитивная регуляция эмоций ([PMC][93])
* **Орбитофронтальная кора (OFC):** оценка вознаграждения и риска ([PMC][94])
* **Миндалина (amygdala):** генерация аффективных реакций ([PMC][94])

**Ключевые тракты / подсети:**

* Uncinate fasciculus (OFC ↔ amygdala)
* Цингулум (mPFC ↔ PCC)

**Ключевые обзоры:**

* Ochsner & Gross, 2005 — «The cognitive control of emotion», *Trends in Cognitive Sciences* ([ScienceDirect][92])
* Phillips et al., 2008 — «Affective neuroscience of emotion regulation», *Nature Reviews Neuroscience* ([PMC][94])

---

## 47. **Sensorimotor Integration Network (SMIN)**

**Ключевая функция:**
Интеграция проприоцептивной и моторной информации для точного управления движением ([ScienceDirect][95]).

**Анатомия:**

* **Премоторная кора (PMC):** планирование движений ([ScienceDirect][95])
* **Supplementary Motor Area (SMA):** инициирование последовательных движений ([PMC][96])
* **Теменная долька (parietal cortex):** сенсорная обратная связь ([ScienceDirect][95])

**Ключевые тракты / подсети:**

* Спиноталамические и таламокортикальные пути
* Связи PMC–SMA через переднюю капсулу

**Ключевые обзоры:**

* Grafton, 2010 — «Sensorimotor integration in the central nervous system», *Current Opinion in Neurobiology* ([ScienceDirect][95])
* Capaday et al., 2022 — «Selective sensorimotor integration in M1», *Journal of Physiology* ([PMC][96])

---

## 48. **Auditory-Motor Network (AMN)**

**Ключевая функция:**
Координация акустической обработки и моторной реализации речи ([PMC][97]).

**Анатомия:**

* **Задняя часть верхней височной извилины (pSTG):** анализ слуховых образов ([PMC][97])
* **Broca’s area (IFG):** планирование артикуляции ([PMC][97])
* **SMA:** инициирование речевого моторного паттерна ([PMC][98])

**Ключевые тракты / подсети:**

* Дорсальный «речевой» путь (arcuate fasciculus)
* Контактные связки с церебеллом и стволом

**Ключевые обзоры:**

* Hickok & Poeppel, 2007 — «The cortical organization of speech processing», *Nature Reviews Neuroscience* ([PMC][97])
* Tourville & Guenther, 2011 — «Sensorimotor integration in speech production», *Speech Communication* ([PMC][98])

---

## 49. **Subcortical Arousal Network (SAN)**

**Ключевая функция:**
Модуляция уровня корковой активности через подкорковые ядерно-химические системы ([PMC][99]).

**Анатомия:**

* **Таламус:** главный «релеер» афферентных сигналов ([Nature][100])
* **Базальное ядро Майнерва (nucleus basalis of Meynert):** холинергическая модуляция ([PMC][101])
* **Ствол мозга (LC, Raphe):** норадренергическая и серотонинергическая проекции ([PMC][99])

**Ключевые тракты / подсети:**

* Проекции BF → кортикальные слои I–II
* Thalamocortical radiations

**Ключевые обзоры:**

* Tehovnik & Sommer, 2013 — «Shared subcortical arousal systems», *Brain Research* ([PMC][99])
* Lustberg et al., 2017 — «Cortical arousal events and basal forebrain activity», *Nature Communications* ([Nature][100])

---

## 50. **Cerebellar-Prefrontal Loop (CPL)**

**Ключевая функция:**
Участие мозжечка в исполнительных функциях и когнитивном контроле через обратные петли с PFC ([ScienceDirect][102]).

**Анатомия:**

* **Задние мозжечковые доли (Crus I/II):** подключение к ассоциативным областям PFC ([ScienceDirect][102])
* **Dorsolateral PFC (dlPFC):** топ-даун когнитивный контроль ([ScienceDirect][103])

**Ключевые тракты / подсети:**

* Мозжечково-таламический тракт (dentate → thalamus → PFC)
* Таламокортикальные и кортикозависимые петли

**Ключевые обзоры:**

* Buckner, 2013 — «The Cerebellum and Cognitive Function: 25 Years of Insight», *Neuron* ([ScienceDirect][102])
* Sokolov et al., 2017 — «Cerebellar loops with prefrontal cortex in executive control», *Trends in Cognitive Sciences* ([PMC][104])


[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5939207/ "Distinct Roles for the Anterior Cingulate and Dorsolateral Prefrontal ..."
[2]: https://www.sciencedirect.com/science/article/pii/S0896627323003082 "20 years of the default mode network: A review and synthesis"
[3]: https://www.nature.com/articles/s41598-020-72317-8 "Functional parcellation of the default mode network - Nature"
[4]: https://www.nature.com/articles/s41467-024-46511-5 "A multi-demand operating system underlying diverse cognitive tasks"
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2899886/ "Saliency, switching, attention and control: a network model of insula ..."
[6]: https://www.jneurosci.org/content/39/50/9878 "The Salience Network: A Neural System for Perceiving and ..."
[7]: https://www.sciencedirect.com/topics/psychology/central-executive-network "Central Executive Network - an overview | ScienceDirect Topics"
[8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6867136/ "White matter integrity of central executive network correlates with ..."
[9]: https://www.sciencedirect.com/topics/medicine-and-dentistry/dorsal-attention-network "Dorsal Attention Network - an overview | ScienceDirect Topics"
[10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6882310/ "Role of the dorsal attention network in distracter suppression based ..."
[11]: https://www.sciencedirect.com/topics/medicine-and-dentistry/ventral-attention-network "Ventral Attention Network - an overview | ScienceDirect Topics"
[12]: https://pubmed.ncbi.nlm.nih.gov/30978625/ "Ventral attention-network effective connectivity predicts individual ..."
[13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6793364/ "The Connection from Cortical Area V1 to V5: A Light and Electron ..."
[14]: https://www.sciencedirect.com/science/article/pii/S235215462400010X "Cortico-cortical paired-associative stimulation to investigate the ..."
[15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10462217/ "Somatomotor-Visual Resting State Functional Connectivity ..."
[16]: https://www.nature.com/articles/s41586-023-05964-2 "A somato-cognitive action network alternates with effector regions in ..."
[17]: https://www.sciencedirect.com/science/article/abs/pii/S0149763413001711 "A revised limbic system model for memory, emotion and behaviour"
[18]: https://www.ncbi.nlm.nih.gov/books/NBK538491/ "Neuroanatomy, Limbic System - StatPearls - NCBI Bookshelf"

[19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3398395/ "A review and synthesis of the first 20 years of PET and fMRI studies ..."
[20]: https://www.aimspress.com/article/doi/10.3934/Neuroscience.2021001?viewType=HTML "a systematic review of fMRI studies in the past two decades"
[21]: https://europepmc.org/article/med/23146876/ "The language network. - Abstract - Europe PMC"
[22]: https://pubmed.ncbi.nlm.nih.gov/21795627/ "The organization of the human cerebellum estimated by intrinsic ..."
[23]: https://en.wikipedia.org/wiki/Randy_Buckner "Randy Buckner"
[24]: https://pubmed.ncbi.nlm.nih.gov/18400794/ "Functional connectivity of human striatum: a resting state FMRI study"
[25]: https://www.nature.com/articles/nrn.2017.104 "Individual arrangements | Nature Reviews Neuroscience"
[26]: https://pubmed.ncbi.nlm.nih.gov/28728026/ "Parallel Interdigitated Distributed Networks within the Individual ..."
[27]: https://www.sciencedirect.com/science/article/pii/S0149763414000128 "Fractionating theory of mind: A meta-analysis of functional brain ..."
[28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6866486/ "The role of the right temporo–parietal junction in social decision ..."
[29]: https://en.wikipedia.org/wiki/Social_cognitive_neuroscience "Social cognitive neuroscience"
[30]: https://pubmed.ncbi.nlm.nih.gov/24770711/ "Functional Characterization of the Cingulo-Opercular Network in the ..."
[31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7749795/ "The orbitofrontal cortex: reward, emotion and depression - PMC"
[32]: https://pubmed.ncbi.nlm.nih.gov/33364600/ "The orbitofrontal cortex: reward, emotion and depression - PubMed"
[33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2430004/ "Function and localization within rostral prefrontal cortex (area 10)"
[34]: https://www.researchgate.net/publication/316227003_Rostral_prefrontal_cortex_Brodmann_area_10_metacognition_in_the_brain "(PDF) Rostral prefrontal cortex (Brodmann area 10) - ResearchGate"
[35]: https://www.researchgate.net/publication/313703365_The_gateway_hypothesis_of_rostral_prefrontal_cortex_area_10_function "(PDF) The gateway hypothesis of rostral prefrontal cortex (area 10 ..."

[36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2796919/ "Reward Networks in the Brain as Captured by Connectivity Measures"
[37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6218647/ "The Functional Connectivity Between the Nucleus Accumbens and ..."
[38]: https://www.nature.com/articles/s41398-022-01995-x "Reduced nucleus accumbens functional connectivity in reward ..."
[39]: https://pubmed.ncbi.nlm.nih.gov/15217334/ "The medial temporal lobe - PubMed"
[40]: https://pubmed.ncbi.nlm.nih.gov/1896849/ "The medial temporal lobe memory system - PubMed"
[41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3388718/ "A new neural framework for visuospatial processing - PMC"
[42]: https://www.nature.com/articles/s41598-023-38554-3 "Occipital and parietal cortex participate in a cortical network ... - Nature"
[43]: https://www.jneurosci.org/content/43/17/3144 "Semantic Representations during Language Comprehension Are ..."
[44]: https://www.nature.com/articles/s41586-024-07643-2 "Semantic encoding during language comprehension at single-cell ..."
[45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7137721/ "The mentalizing network and theory of mind mediate adjustment ..."
[46]: https://www.sciencedirect.com/science/article/abs/pii/S0028393220301469 "Theory of mind network activity is associated with metaethical ..."
[47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5810456/ "From Neurons to Social Beings: Short Review of the Mirror Neuron ..."
[48]: https://www.nature.com/articles/nrn2024 "The mirror neuron system and the consequences of its dysfunction"
[49]: https://www.sciencedirect.com/science/article/pii/S2589004224027081 "Demystifying visual word form area visual and nonvisual response ..."
[50]: https://www.eneuro.org/content/11/7/ENEURO.0228-24.2024 "Reading Reshapes Stimulus Selectivity in the Visual Word Form Area"
[51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5862740/ "The multifaceted role of ventromedial prefrontal cortex in emotion ..."
[52]: https://pubmed.ncbi.nlm.nih.gov/30877420/ "The Role of the Amygdala and the Ventromedial Prefrontal Cortex in ..."
[53]: https://www.nature.com/articles/s41467-022-35658-8 "Cerebro-cerebellar networks facilitate learning through feedback ..."
[54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10416251/ "The cerebellum and cognitive neural networks - PubMed Central"
[55]: https://www.nature.com/articles/s41386-021-01132-0 "The role of prefrontal cortex in cognitive control and executive function"

[56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2604839/ "Evidence for a Frontoparietal Control System Revealed by Intrinsic ..."
[57]: https://academic.oup.com/braincomms/article/4/2/fcac080/6555238 "Right fronto-parietal networks mediate the neurocognitive benefits of ..."
[58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6136121/ "The frontoparietal network: function, electrophysiology, and ..."
[59]: https://pubmed.ncbi.nlm.nih.gov/16226590/ "Dual routes to action: contributions of the dorsal and ventral streams ..."
[60]: https://pubmed.ncbi.nlm.nih.gov/24962370/ "The functional architecture of the ventral temporal cortex and its role ..."
[61]: https://en.wikipedia.org/wiki/Two-streams_hypothesis "Two-streams hypothesis - Wikipedia"
[62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3575728/ "Social cognition and the anterior temporal lobes - PubMed Central"
[63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2791360/ "The anterior temporal lobes and the functional architecture of ..."
[64]: https://pubmed.ncbi.nlm.nih.gov/18343462/ "Memory retrieval and the parietal cortex: a review of evidence from a ..."
[65]: https://www.sciencedirect.com/science/article/abs/pii/S1364661315001552 "Review A parietal memory network revealed by multiple MRI methods"
[66]: https://pubmed.ncbi.nlm.nih.gov/8412366/ "The central autonomic network: functional organization, dysfunction ..."
[67]: https://www.sciencedirect.com/science/article/abs/pii/S0025619612622721 "The Central Autonomic Network: Functional Organization ..."
[68]: https://pubmed.ncbi.nlm.nih.gov/27021938/ "Thalamus plays a central role in ongoing cortical functioning - PubMed"
[69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6886702/ "Thalamo-cortical circuit motifs: a general framework - PubMed Central"
[70]: https://www.nature.com/articles/nn1176 "Neural systems supporting interoceptive awareness - Nature"
[71]: https://pubmed.ncbi.nlm.nih.gov/14730305/ "Neural systems supporting interoceptive awareness - PubMed"
[72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6869957/ "Separating brain processing of pain fromthat of stimulus intensity"
[73]: https://www.sciencedirect.com/science/article/abs/pii/S0301008210001759 "The pain matrix reloaded: A salience detection system for the body"
[74]: https://pubmed.ncbi.nlm.nih.gov/21223979/ "The thalamocortical vestibular system in animals and humans"
[75]: https://pubmed.ncbi.nlm.nih.gov/22516007/ "The human vestibular cortex revealed by coordinate ... - PubMed"

[76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8078209/ "Validation of Olfactory Network Based on Brain Structural ..."
[77]: https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00571/128869/The-human-olfactory-amygdala-anatomical "Anatomical connections between the olfactory bulb and amygdala ..."
[78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12025486/ "The Bulb, the Brain and the Being: New Insights into Olfactory ..."
[79]: https://www.sciencedirect.com/science/article/pii/S1353802024012422 "Structural and functional connectomics of the olfactory system in ..."
[80]: https://www.sciencedirect.com/science/article/abs/pii/S027826261530004X "Functions of the anterior insula in taste, autonomic, and related ..."
[81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3221736/ "The Anterior Insular Cortex Represents Breaches of Taste Identity ..."
[82]: https://www.pnas.org/doi/10.1073/pnas.2010932118 "Viewing images of foods evokes taste quality-specific activity ... - PNAS"
[83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6621713/ "A Dynamic Cortical Network Encodes Violations of Expectancy ..."
[84]: https://www.sciencedirect.com/topics/veterinary-science-and-veterinary-medicine/reticular-activating-system "Reticular Activating System - an overview | ScienceDirect Topics"
[85]: https://www.sciencedirect.com/topics/neuroscience/reticular-activating-system "Reticular Activating System - an overview | ScienceDirect Topics"
[86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3387430/ "Neuroanatomic Connectivity of the Human Ascending Arousal ..."
[87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4526749/ "Memory Consolidation - PMC"
[88]: https://pubmed.ncbi.nlm.nih.gov/25770921/ "A central node in a large-scale brain network for memory - PubMed"
[89]: https://pubmed.ncbi.nlm.nih.gov/16399806/ "The precuneus: a review of its functional anatomy and behavioural ..."
[90]: https://academic.oup.com/brain/article/129/3/564/390904 "The precuneus: a review of its functional anatomy and behavioural ..."
[91]: https://www.researchgate.net/publication/7371646_Cavanna_AE_Trimble_MR_The_precuneus_a_review_of_its_functional_anatomy_and_behavioural_correlates_Brain_J_Neurol_129Pt_3_564-583 "Cavanna AE, Trimble MR. The precuneus: a review of its functional ..."
[92]: https://www.sciencedirect.com/science/article/abs/pii/S1364661305000902 "The cognitive control of emotion - ScienceDirect.com"
[93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4133790/ "Functional imaging studies of emotion regulation: A synthetic review ..."
[94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2566753/ "Amygdala–frontal connectivity during emotion regulation - PMC"
[95]: https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/sensorimotor-integration "Sensorimotor Integration - an overview | ScienceDirect Topics"
[96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9305922/ "Sensorimotor integration within the primary motor cortex by selective ..."
[97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3468690/ "The cortical organization of speech processing: Feedback control ..."
[98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4733636/ "Perception drives production across sensory modalities: A network ..."
[99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11429725/ "Shared subcortical arousal systems across sensory modalities ..."
[100]: https://www.nature.com/articles/s41467-017-02815-3 "Subcortical evidence for a contribution of arousal to fMRI studies of ..."
[101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6500474/ "Basal Forebrain Subcortical Projections - PMC - PubMed Central"
[102]: https://www.sciencedirect.com/science/article/pii/S0896627313009963 "The Cerebellum and Cognitive Function: 25 Years of Insight from ..."
[103]: https://www.sciencedirect.com/science/article/abs/pii/S0928425713000223 "Prefrontal cortex and neural mechanisms of executive function"
[104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7786249/ "A New Insight on the Role of the Cerebellum for Executive Functions ..."


---



Оглавление:

- [ЭИРО framework](/README.md)
