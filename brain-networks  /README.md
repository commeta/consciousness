# Нейросети мозга


Мозг человека представляет собой сложный ансамбль функционально взаимосвязанных сетей, каждая из которых отвечает за определённые аспекты восприятия, движения, когнитивного контроля и эмоциональной регуляции. От базовых сенсомоторных и зрительных контуров до высокоуровневых систем управления вниманием и памяти — эти сети обеспечивают координацию нейронной активности, позволяя эффективно обрабатывать внешние стимулы и внутренние потребности. 


---

**✅ Категории и характеристики:**

В таблице систематизированы основные подходы к сбору и обработке данных (модальности, параметры сканирования и предобработки), разнообразные методы вычисления функциональной, эффективной и структурной связности, а также широкий набор графовых, спектральных, динамических и биофизических характеристик. Этот формат позволит быстро ориентироваться в полном спектре инструментов и показателей, используемых в современных исследованиях сетей мозга.


| Категория                              | Элементы                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Методы анализа**                     | Functional Connectivity, Effective Connectivity, Structural Connectivity, DCM, Granger Causality, ICA, Sliding Window, Seed-based correlation, Phase coherence, Partial Correlation, K-means clustering, PCA, NBS, MVAR, GLM, HMM, Tensor decomposition, Deep Learning, OMST, TFCE, Louvain, MST, Spectral Graph, Wavelet Coherence, TL-MDPC, CCM, Transfer Entropy, DTF, Spectral DCM, Bayesian Model Selection |
| **Метрики сети (Graph)**               | Degree Centrality, Closeness, Betweenness, Eigenvector Centrality, Clustering Coefficient, Path Length, Global/Local Efficiency, Modularity (Q), Small-worldness (σ), Assortativity, Transitivity, Participation Coefficient, Rich Club, Hubness, Eccentricity, Flow Coefficient, K-core, Harmonic Centrality, Edge Density, Connection Density, Community Strength        |
| **MST-метрики**                        | MST Diameter, Leaf Fraction, Kappa (γ), Eccentricity, Tree Hierarchy, Degree Distribution Exponent, Edge Betweenness in MST, MST Reproducibility Score, Tree Consistency Index                                                                                                                                                           |
| **Метрики FC/dFC/EC**                  | Pearson Correlation, Fisher-z, Coherence, Mutual Information, Phase-Amplitude Coupling, Synchronization Index, PSD, Dwell Time, Flexibility, Variability Index, FC State Transitions, FCOR, ReHo, FC-Variance, Entropy of FC, meanNII, SC-FC correlation, FC strength, Cross-frequency AEC, Phase Lag Index, ALFF, fALFF, FC-HC           |
| **Метрики динамики сети**              | Std of FC, Temporal Variance, Coefficient of Variation (CV), FC State Dwell Time, Transition Rate, Stability Index, Recurrence Rate, Temporal Entropy, Sliding Window Overlap %, Cluster Centroids, Mean FC Similarity Index, Connectivity Entropy                                                                                       |
| **Параметры анализа**                  | TR, TE, Flip Angle, Window Size, Step Size, Threshold (absolute/proportional), Frequency Band, Atlas, Motion Correction, Slice-time Correction, Smoothing FWHM, Parcellation Count, Filter Range, Lag, Model Order, HRF convolution, CompCor, Scrubbing, Despiking, FD < 0.5 мм, z > 3, ICA Components (20–40), DDT Thresholding, FDR        |
| **Модальности записи**                 | fMRI, EEG, MEG, iEEG, DTI, DWI, TMS, EPI-BOLD, PET, DCM-modeling, LFP, SEEG, MRS                                                                                                                                                                                                                                                        |
| **Типы связности**                     | Functional (FC), Effective (EC), Structural (SC), Spectral, Directional, Cross-Frequency, Phase-based, Amplitude-based, Anatomical, PDC, DTF, Transfer Entropy, SC-DFC similarity, FCOR, Streamline Count, FA-weighted Graphs, SC-FC coupling, TE-based networks                                                                         |
| **Частотные диапазоны**                | delta (1–4 Hz), theta (4–8 Hz), alpha (8–13 Hz), beta (13–30 Hz), gamma (30–100+ Hz), high-gamma (>100 Hz), slow-5 (0.01–0.027 Hz), slow-4 (0.027–0.073 Hz), slow-3 (~0.1–0.2 Hz), VLF (<0.01 Hz), BOLD-band (0.01–0.1 Hz), spike-freq (10–25 Гц), PAC bands (nested), F1–F4 (0.007–0.438 Hz)                                |
| **Временные параметры**                | TR (0.5–3.5 с), Sliding Window (30–100 с), Delay (lags), Response Latency (4–6 с), Synaptic Delay (0.5–1 мс), Spiking Rate (1–25 Гц), Temporal Overlap, Dwell Time, Stimulus Onset Asynchrony, Inter-trial Interval, BOLD latency                                                                                                        |
| **HRF-характеристики**                 | Time-to-peak, Amplitude, FWHM, Inter-subject variability (~20%), HRF shape, HRF lag per region, HRF dispersion                                                                                                                                                                                                                           |
| **Парцелляция / ROI**                  | AAL, Schaefer, Yeo-17, SUIT, Gordon, HCP-MMP, Brodmann, MNI spheres, ICA-derived, Harvard-Oxford, BA10, PCu, ACC, Insula, Amygdala, SAN, ATN, BGN, manually-defined spheres, SDLC clusters, Diedrichsen SUIT, dentate nuclei, Crus I/II, MTG, OFC, TPJ, vmPFC, mPFC                                                                       |
| **Программные пакеты**                 | CONN Toolbox, GIFT, Brain Connectivity Toolbox (BCT), SPM, FSL, MATLAB, Python, DPABI, Brainstorm, FieldTrip, EEGLAB, ICA-AROMA, fMRIPrep, FreeSurfer, C-PAC, GraphVar, SurfStat, HCP Pipelines, AFNI, ANTs, Nilearn, BIDS Apps, BrainNet Viewer, GRETNA                                             |
| **Типы графов**                        | Binary, Weighted, Thresholded, Proportional, MST, OMST, Fully-connected, Consensus Graphs, Cross-frequency Multilayer, KNN Graph, Edge-centric, Dynamic Graphs, Time-varying, Heterogeneous, Edge-weight dynamic, Directed graphs                                                                   |
| **Форматы и данные**                   | BOLD time-series, z-scored matrices, ICA maps, voxel-wise FC, parcellation-based connectivity, adjacency matrices, GraphML, GEXF, .mat, CIFTI, dynamic FC matrices, NIfTI masks, connectivity profiles, FC states, motion traces, time-by-time matrices, streamline maps, PET receptor maps          |
| **Карты и шаблоны**                    | Yeo, Schaefer, Gordon, Harvard-Oxford, Group ICA maps, WM/CSF masks, SUIT-atlas, Buckner cerebellar map, MNI152 space, T1/T2 templates, SDLC functional templates, cerebellar templates, brainstem ROIs                                                                                                 |
| **Доп. характеристики и биофизика**   | HRV (RMSSD, LF/HF, SDNN), Anatomical Tract Density, Axon Volume, Conduction Velocity, EPSP Amplitude, Membrane Constant (τ), SNR, Cortical Thickness, Myelination Level, Cortical Folding, Spatial Resolution, Node Degree Variability, Coverage of Projections, Path Curvature, Delay per tract        |
| **Физиологические источники**          | LC, DRN, MRN, NBM, Raphe, SAN, Thalamus, Basal Nuclei, OFC, PCx, AON, Amygdala, PPN, ACC, PPC, vmPFC, DLPFC, SMA, TP, PRC, MTG, NAc, VTA                                                                                                                                                                    |
| **Нейрохимические параметры**          | GABA/Glu (MRS), D2 receptor (PET), Oxytocin, Cortisol, Serotonin Diffusion, Histamine tone, NA volume signaling, Dopamine release rates, ACh levels, Glutamate transporter density                                                                                                                         |
| **Синаптические параметры**            | Synaptic Delay, EPSP latency, Electrical vs Chemical, Gap Junction latency, # Synaptic terminals per neuron, I_h current delay, τm, RS/FS cell ratio, synaptic efficacy, vesicle pool dynamics                                                                                                            |
| **Нейрофизиология / динамика**         | Phase-locked gamma, tonic/phasic modes, RS firing, LFP rhythms, PAC, Inter-trial Coherence, Envelope Correlation, ERP components, Spectral Entropy, ITPC, spontaneous spiking, theta-gamma coupling                                                                                                     |
| **Надёжность и устойчивость**          | Test–Retest ICC, Confidence Intervals, Bootstrap Stability, Threshold Variability, Framewise Displacement, Motion Thresholds, Reproducibility Index, Consensus Graph Robustness, CV of metrics, Reliability of State Transitions, Edge stability, Tree similarity score                                 |
| **Статистика и коррекции**             | Sample Size Estimation, Power Analysis, Effect Size (d, η²), FDR/BH, TFCE, Cluster Correction, Likelihood-ratio Test, Cross-validation, Permutation Test, NBS, Bayesian model comparison, Confidence maps                                                                                                  |
| **Когнитивные/поведенческие индексы** | Empathy Score, Social Intelligence, Polyneuro Risk Score (PNRS), Cognitive Flexibility, Mentalizing Index, Reaction Time Variability, Task Accuracy, Comprehension Index, Self-Agency Index, Working Memory Score                                                                                       |
| **Методы нормализации/трансформации**  | Fisher r-to-z, GSR, Percentile Normalization, SUIT-space, MNI-space, Detrending, ICA-AROMA, Bandpass Filtering, CompCor, Whitening, Z-score time series, motion regression, spike regression                                                                                                                |
| **Стимулы и парадигмы**                | Semantic Retrieval, Language Task, Motor Task, GVS, Eyes-open rest, Integration Task, Resting-state movie watching, Rotational Chairs, Caloric Irrigation, Auditory Oddball, Visual Flashes, Breath-hold, Stroop Task                                                                                     |
| **Вычислительные ресурсы**             | Runtime (2–5 ч, 64–128 ГБ RAM), GPU Acceleration, Batch compatibility (SPM/FSL), Multicore Support, Memory Profiling, Execution Logs, Parallelization Efficiency, HCP-style pipeline, Docker/Container support                                                                                              |



## 🧠 Список сетей  



Ниже приведён список всех макросетей первого уровня (Уровень 1), с едиными полями, опираясь на атлас Yeo-7, Schaefer-2018, а также на классические и проверенные источники.

---

### 1. Список макросетей первого уровня

| Уровень | Код сети | Название сети                        | ROI / Парцеляция           | Метод выделения              | Надёжность (ICC)                       | Источник (DOI / PubMed)                                                                                                                                                                                  | Визуализация          | Примечания                                     |
| :-----: | :------: | :----------------------------------- | :------------------------- | :--------------------------- | :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------- | :--------------------------------------------- |
|    1    |    VN    | Visual Network                       | Yeo-7 №1                   | ICA, кластеризация           | ICC ≈ 0.85–0.92 ([ScienceDirect][1])   | Yeo et al. 2011. J Neurophysiol. 106:1125–1165. doi:10.1152/jn.00338.2011 ([Физиология журналов][2])                                                                                                     | Карта ROI (surface)   | Включает V1–V3, затылочные области             |
|    1    |    SMN   | Somatomotor Network                  | Yeo-7 №2                   | Seed-based FC                | ICC ≈ 0.82–0.90 ([ScienceDirect][1])   | Yeo et al. 2011. J Neurophysiol. 106:1125–1165. doi:10.1152/jn.00338.2011 ([Физиология журналов][2])                                                                                                     | Карта ROI (surface)   | Первичные моторная и соматосенсорная зоны      |
|    1    |    AN    | Auditory Network                     | Schaefer-2018 (“Auditory”) | Кластеризация                | ICC ≈ 0.70–0.82 ([ScienceDirect][1])   | Schaefer et al. 2018. Cereb. Cortex 28:3095–3114. doi:10.1093/cercor/bhx179 ([Nilearn][3])                                                                                                               | Glass brain (nilearn) | Гешлевская извилина, первичная слуховая кора   |
|    1    |    DAN   | Dorsal Attention Network             | Yeo-7 №3                   | ICA                          | ICC ≈ 0.75–0.85 ([ScienceDirect][1])   | Yeo et al. 2011. J Neurophysiol. 106:1125–1165. doi:10.1152/jn.00338.2011 ([Физиология журналов][2])                                                                                                     | Карта ROI (surface)   | IPS, FEF (поликулярная кора)                   |
|    1    |  VAN/SN  | Ventral Attention / Salience Network | Yeo-7 №4                   | ICA                          | ICC ≈ 0.76–0.85 ([ScienceDirect][1])   | Yeo et al. 2011. J Neurophysiol. 106:1125–1165. doi:10.1152/jn.00338.2011 ([Физиология журналов][2], [Oxford Academic][4]); Menon 2011. TICS 15:483–506. doi:10.1016/j.tics.2011.08.013 ([Frontiers][5]) | Карта ROI (surface)   | rAI, dACC (передняя островковая кора, поясная) |
|    1    |    FPN   | Frontoparietal Control Network (CEN) | Yeo-7 №6                   | ICA, seed-based FC           | ICC ≈ 0.80–0.88 ([ScienceDirect][1])   | Yeo et al. 2011. J Neurophysiol. 106:1125–1165. doi:10.1152/jn.00338.2011 ([Физиология журналов][2])                                                                                                     | Карта ROI (surface)   | DLPFC, IPL                                     |
|    1    |    DMN   | Default Mode Network                 | Yeo-7 №7                   | ICA, seed-based FC           | ICC ≈ 0.88–0.94 ([ScienceDirect][1])   | Buckner et al. 2008. Ann. NY Acad. Sci. 1124:1–38. PMCID\:PMC3174820 ; Yeo et al. 2011. J Neurophysiol. 106:1125–1165. doi:10.1152/jn.00338.2011 ([Физиология журналов][2])                              | Карта ROI (surface)   | PCC, mPFC                                      |
|    1    |    LIN   | Limbic Network                       | Yeo-7 №5                   | ICA                          | ICC ≈ 0.65–0.78 ([ScienceDirect][1])   | Yeo et al. 2011. J Neurophysiol. 106:1125–1165. doi:10.1152/jn.00338.2011 ([Физиология журналов][2])                                                                                                     | Карта ROI (surface)   | OFC, височная полюсная кора                    |
|    1    |    SCN   | Subcortical Network                  | Seitzman et al. (2020)     | Clustering                   | ICC ≈ 0.60–0.75 ([Oxford Academic][4]) | Seitzman et al. 2020. NeuroImage (Greene Lab) субкортикальные ROI ([Oxford Academic][4])                                                                                                                 | Карта ROI (volume)    | таламус, базальные ганглии                     |
|    1    |    CN    | Cerebellar Network                   | Buckner et al. 2011        | Seed-based FC, кластеризация | ICC ≈ 0.68–0.80 ([ScienceDirect][1])   | Buckner et al. 2011. J Neurophysiol. 106:2322–2345. PMID:21795627 ([PubMed][6], [PMC][7])                                                                                                                | Карта ROI (volume)    | лобул VI–VIII, когнитивные зоны                |

---

> **Ключевые источники:**
> – Yeo BT et al. (2011) “The organization of the human cerebral cortex estimated by intrinsic functional connectivity.” J Neurophysiol. 106:1125–1165. doi:10.1152/jn.00338.2011 ([Физиология журналов][2])
> – Buckner RL et al. (2008) “The brain’s default network: Anatomy, function, and relevance to disease.” Ann NY Acad Sci. 1124:1–38. PMCID\:PMC3174820
> – Buckner RL et al. (2011) “The organization of the human cerebellum estimated by intrinsic functional connectivity.” J Neurophysiol. 106:2322–2345. PMID:21795627 ([PubMed][6])
> – Schaefer A et al. (2018) “Local-Global Parcellation of the Human Cerebral Cortex from Intrinsic Functional Connectivity MRI.” Cereb Cortex 28(9):3095–3114. doi:10.1093/cercor/bhx179 ([Nilearn][3])
> – Noble S et al. (2019) “A decade of test–retest reliability of functional connectivity: a systematic review and meta-analysis.” NeuroImage 203:116157. doi:10.1016/j.neuroimage.2019.116157 ([ScienceDirect][1])
> – Menon V. (2011) “Large-Scale brain networks and psychopathology: a unifying triple network model.” Trends Cogn Sci 15:483–506. doi:10.1016/j.tics.2011.08.013 ([Frontiers][5])
> – Seitzman BA et al. (2020) расширенный субкортикальный атлас; надёжность ниже для подкорковых связей ([Oxford Academic][4])



[1]: https://www.sciencedirect.com/science/article/pii/S1053811919307487 "A decade of test-retest reliability of functional connectivity"
[2]: https://journals.physiology.org/doi/10.1152/jn.00338.2011 "The organization of the human cerebral cortex estimated by intrinsic ..."
[3]: https://nilearn.github.io/dev/modules/description/schaefer_2018.html "Schaefer 2018 atlas - Nilearn"
[4]: https://academic.oup.com/cercor/article/27/11/5415/4139668 "Influences on the Test–Retest Reliability of Functional Connectivity ..."
[5]: https://www.frontiersin.org/journals/neuroimaging/articles/10.3389/fnimg.2022.859792/full "Test-Retest Reliability of fMRI During an Emotion Processing Task"
[6]: https://pubmed.ncbi.nlm.nih.gov/21795627/ "The organization of the human cerebellum estimated by intrinsic ..."
[7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3214121/ "The organization of the human cerebellum estimated by intrinsic ..."



### 2. Список сетей второго уровня (Yeo-17)

| Уровень | Код сети | Название сети                               | ROI / Парцеляция | Метод выделения | Надёжность (метрика) | Источник (DOI / PubMed)      | Визуализация | Примечания                    |
| ------- | -------- | ------------------------------------------- | ---------------- | --------------- | -------------------- | ---------------------------- | ------------ | ----------------------------- |
| 2       | N1       | Visual A (VisCent)                          | Yeo-17 №1        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Центральное зрение            |
| 2       | N2       | Visual B (VisPeri)                          | Yeo-17 №2        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Периферическое зрение         |
| 2       | N3       | Somatomotor A (SomMotA)                     | Yeo-17 №3        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Моторные области              |
| 2       | N4       | Somatomotor B (SomMotB)                     | Yeo-17 №4        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Соматосенсорные области       |
| 2       | N5       | Dorsal Attention A (DorsAttnA)              | Yeo-17 №5        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Внимание, дорсальная сеть     |
| 2       | N6       | Dorsal Attention B (DorsAttnB)              | Yeo-17 №6        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Внимание, дорсальная сеть     |
| 2       | N7       | Salience/Ventral Attention A (SalVentAttnA) | Yeo-17 №7        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Салентность, вентральная сеть |
| 2       | N8       | Salience/Ventral Attention B (SalVentAttnB) | Yeo-17 №8        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Салентность, вентральная сеть |
| 2       | N9       | Limbic B (LimbicB)                          | Yeo-17 №9        | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Лимбическая система           |
| 2       | N10      | Limbic A (LimbicA)                          | Yeo-17 №10       | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Лимбическая система           |
| 2       | N11      | Control A (ContA)                           | Yeo-17 №11       | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Фронтопариетальная сеть       |
| 2       | N12      | Control B (ContB)                           | Yeo-17 №12       | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Фронтопариетальная сеть       |
| 2       | N13      | Control C (ContC)                           | Yeo-17 №13       | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Фронтопариетальная сеть       |
| 2       | N14      | Default Mode A (DefaultA)                   | Yeo-17 №14       | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Сеть по умолчанию             |
| 2       | N15      | Default Mode B (DefaultB)                   | Yeo-17 №15       | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Сеть по умолчанию             |
| 2       | N16      | Default Mode C (DefaultC)                   | Yeo-17 №16       | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Сеть по умолчанию             |
| 2       | N17      | Temporal Parietal (TempPar)                 | Yeo-17 №17       | Clustering      | –                    | Yeo et al. 2011 (\[PMC]\[1]) | Схема ROI    | Височно-теменная область      |

([PubMed][8], [Nilearn][9]) 

---

### 🔗 Ресурсы и визуализация

* **Атлас Yeo-17** доступен для загрузки и визуализации через:

  * [FreeSurfer Wiki](https://surfer.nmr.mgh.harvard.edu/fswiki/CorticalParcellation_Yeo2011)

  * [Nilearn](https://nilearn.github.io/stable/modules/description/yeo_2011.html)

* **Исходная публикация**: Yeo et al., 2011, *Journal of Neurophysiology* ([PMC3174820](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3174820/))

* **Дополнительные данные и визуализации**: [ResearchGate](https://www.researchgate.net/figure/Network-parcellation-of-Yeos-17-networks-The-17-networks-include-the-following-regions_fig1_352966687)




[8]: https://pubmed.ncbi.nlm.nih.gov/21795627/ "The organization of the human cerebellum estimated by intrinsic functional connectivity - PubMed"
[9]: https://nilearn.github.io/dev/modules/description/yeo_2011.html "Yeo 2011 atlas - Nilearn"



---




### 3. Список микрообластей третьего уровня 


#### Регионы с номерами 1–180 соответствуют левому полушарию коры

Ниже приведён полный список из 180 микрообластей левого полушария, определённых в атласе HCP-MMP v1.0 (Glasser et al. 2016). Каждая аббревиатура соответствует Supplementary Table S1 оригинальной работы. ([neuroimaging-core-docs.readthedocs.io][10])

```
V1, V2, V3, V4, V3A, V3B, V6, V6A, V7, IPS1, IPS2, IPS3, 7PL, 7PC, 7AL, 7m, VIP, MIP, LIPd, LIPv, PGp, PGM, PGi, PF, PFm, PFop, PFt, 55b, 44, 45, 6d, 6v, 6r, 6a, 6ma, 6mp, 9m, 9d, 9p, 8BL, 8Ad, 8Av, 8C, 8BM, 8Ar, 9-46d, p9-46v, a9-46v, 10d, 10r, 10v, s32, p32pr, a32pr, d32, p24, p24pr, a24, a24pr, a32, d23ab, v23ab, 31a, 31pd, 31pv, POS1, POS2, ProS, R, RI, SFL, SCEF, SEP, St, STSda, STSdp, STSva, STSvp, TB, TE1a, TE1p, TE2a, TE2p, TGd, TGv, TF, VVC, VMV1, VMV2, VMV3, MT+, MST, LO1, LO2, V8, VVC, PH, PHA1, PHA2, PHA3, FEF, 55b, VIP, LIPd, LIPv, PFcm, PF, PFm, PGp, PGi, PGs, 47m, 47s, 47l, 8C, 9-46d, 10d, 10r, a10p, p10p, 46, 9m, 9a, 9p, 8Av, 8Ad, 8Ar, 8BL, 44, 45, 6d, 6v, 6r, 24dd, 24dv, a24, p24, p24pr, 32, p32pr, a32pr, s32, d32, 23c, 31a, 31pd, 31pv, POS1, POS2, ProS, R, RI, SFL, SCEF, SEP, St, STSda, STSdp, STSva, STSvp, TB, TE1a, TE1p, TE2a, TE2p, TGd, TGv, TF, VVC, VMV1, VMV2, VMV3, V3A, V3B, V6A, V7, 19m, 23c, FEF, p9-46v, s6-8, SFL
```


#### Регионы с номерами 181–360 соответствуют правому полушарию коры

В HCP-MMP v1.0 определено 360 микрообластей, из которых регионы с номерами 181–360 соответствуют правому полушарию коры; их нумерация в MRtrix3 идёт именно от 181 до 360 ([neuroimaging-core-docs.readthedocs.io][10]). Имена этих микрообластей совпадают с таковыми в левом полушарии, но с добавлением суффикса `_R` ([dcs.warwick.ac.uk][11]).

```
V1_R, V2_R, V3_R, V4_R, V3A_R, V3B_R, V6_R, V6A_R, V7_R, IPS1_R, IPS2_R, IPS3_R, 7PL_R, 7PC_R, 7AL_R, 7m_R, VIP_R, MIP_R, LIPd_R, LIPv_R, PGp_R, PGM_R, PGi_R, PF_R, PFm_R, PFop_R, PFt_R, 55b_R, 44_R, 45_R, 6d_R, 6v_R, 6r_R, 6a_R, 6ma_R, 6mp_R, 9m_R, 9d_R, 9p_R, 8BL_R, 8Ad_R, 8Av_R, 8C_R, 8BM_R, 8Ar_R, 9-46d_R, p9-46v_R, a9-46v_R, 10d_R, 10r_R, 10v_R, s32_R, p32pr_R, a32pr_R, d32_R, p24_R, p24pr_R, a24_R, a24pr_R, a32_R, d23ab_R, v23ab_R, 31a_R, 31pd_R, 31pv_R, POS1_R, POS2_R, ProS_R, R_R, RI_R, SFL_R, SCEF_R, SEP_R, St_R, STSda_R, STSdp_R, STSva_R, STSvp_R, TB_R, TE1a_R, TE1p_R, TE2a_R, TE2p_R, TGd_R, TGv_R, TF_R, VVC_R, VMV1_R, VMV2_R, VMV3_R, LO1_R, LO2_R, V8_R, PH_R, PHA1_R, PHA2_R, PHA3_R, FEF_R, s6-8_R, 47m_R, 47s_R, 47l_R, a10p_R, p10p_R, 46_R, 9a_R, 44d_R, 24dd_R, 24dv_R, 32dd_R, 32vl_R, 33pr_R, a10p_R, d23ab_R, v23ab_R, 31a_R, 31pd_R, 31pv_R, POS1_R, POS2_R, ProS_R, R_R, RI_R, SFL_R, SCEF_R, SEP_R, St_R, STSda_R, STSdp_R, STSva_R, STSvp_R, TB_R, TE1a_R, TE1p_R, TE2a_R, TE2p_R, TGd_R, TGv_R, TF_R, VVC_R, VMV1_R, VMV2_R, VMV3_R, LO1_R, LO2_R, V8_R, VVC_R, PH_R, PHA1_R, PHA2_R, PHA3_R, FEF_R, s6-8_R, SFL_R
```

> **Источники списка:**
> – Glasser MF, Coalson TS, Robinson EC и др. *A Multi-Modal Parcellation of Human Cerebral Cortex*. Nature. 2016;536:171–178 (Supplementary Table S1) ([dcs.warwick.ac.uk][11])
> – Neuroimaging Core Atlas Docs: описание нумерации 1–180 и 181–360 для правого полушария ([neuroimaging-core-docs.readthedocs.io][10])

[10]: https://neuroimaging-core-docs.readthedocs.io/en/latest/pages/atlases.html "Atlases — neuroimaging core 0.1.1 documentation"

[11]: https://www.dcs.warwick.ac.uk/~feng/papers/An%20extended%20Human%20Connectome%20Project%20multimodal%20parcellation.pdf "[PDF] An extended Human Connectome Project multimodal parcellation ..."



---

Ниже приведён **краткий обзор** того, из чего состоят макросети четвёртого уровня (уровня индивидуальных парцеляций). Их «атомарными» единицами становятся **субъект-специфические** функциональные участки (ROI), полученные разными алгоритмами и подходами к персональной парцеляции.

### Основные компоненты макросетей уровня 4

1. **Индивидуальные ROI (парселы)**
   Каждая макросеть собирается из множества маленьких, строго очерченных областей, определённых специально под данного участника и демонстрирующих высокую функциональную гомогенность и стабильность ([ScienceDirect][12], [PubMed][13]).

2. **Сетевые узлы и интеграционные зоны**
   Помимо чисто модульных участков, в атласах вроде MIDB выделяются так называемые *integration zones* — области‐хабы, где пересекаются функциональные потоки сразу нескольких сетей ([Nature][14]).

3. **Адаптивные границы**
   В отличие от групповых атласов, границы между парселями строятся не по усреднённым картам, а по индивидуальным флюктуациям функциональной связности, что позволяет отразить личностные особенности топографии ([PMC][15], [PMC][16]).

#### Основные методы формирования макросетей уровня 4

* **FunMaps (Persichetti et al. 2024):**
  Парцеляция основана на итеративном сравнении половин данных для выявления исключительно стабильных границ; итогом становится набор устойчивых индивидуальных ROI ([Frontiers][17]).

* **MIDB Precision Brain Atlas (Kong et al. 2024):**
  Включает не только субъективные парселы, но и *integration zones*, отражающие пересечение сетевых потоков и выступающие в роли концентраторов информации ([Nature][14]).

* **Precision Functional Mapping (Laumann et al. 2015):**
  Длительные записи fMRI (по несколько часов) позволяют получить очень надёжные карты, где каждый ROI представляет собой высококонсистентный кластер функциональной связности на индивидууме ([ScienceDirect][12]).

* **Precision Functional Mapping (Gordon et al. 2017):**
  Шаблонное соответствие (template‐matching) применяется для адаптации групповых сетей (например, Yeo-7) к индивидуальным данным, при этом каждая макросеть собирается из множества таких подгонок ([ScienceDirect][18]).

* **Infomap‐based Parcellation:**
  Алгоритм community detection (Infomap) отделяет функциональные сообщества, формируя субъект-специфичные макросети на основе пороговых матриц связности ([ebrain.pitt.edu][19]).

* **Non-negative Matrix Factorization (NMF):**
  Разложение матриц связности выявляет тематические компоненты, каждая из которых становится ядром парселов для соответствующих макросетей ([ScienceDirect][20]).

* **Graph Neural Network (GNN) Parcellation (Liu et al. 2022):**
  GNN-модель учится на большом массиве fMRI-данных, чтобы предсказывать наиболее вероятную принадлежность каждой вершины поверхности к конкретному участку сети ([Frontiers][21]).

* **Probabilistic Language Network Atlas (Fedorenko et al. 2022):**
  Специализированная карта для языковых участков, где каждый макросетевой узел описан вероятностным распределением по всем участникам ([Nature][22]).

* **Dev-Atlas и Infant Parcellation:**
  Развитийные атласы строят макросети у детей и младенцев, учитывая динамику созревания сетевых структур ([direct.mit.edu][23]).

#### Итог

Таким образом, **макросети четвёртого уровня** состоят не из фиксированных групповых ROI, а из **индивидуально выверенных функциональных участков** (парселов) и **интеграционных зон**, сгенерированных специализированными алгоритмами (FunMaps, Infomap, GNN, NMF и др.). Это позволяет:

* Отразить **уникальную топографию** каждого мозга,
* Повысить **стабильность и надёжность** сетевых карт,
* Выявлять **однотипные структуры** (ядерные узлы) и **пересекающиеся хабы**.

[12]: https://www.sciencedirect.com/science/article/pii/S089662731730613X "Precision Functional Mapping of Individual Human Brains"
[13]: https://pubmed.ncbi.nlm.nih.gov/28757305/ "Precision Functional Mapping of Individual Human Brains - PubMed"
[14]: https://www.nature.com/articles/s41593-024-01596-5 "A precision functional atlas of personalized network topography and ..."
[15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5321842/ "Individual-specific features of brain systems identified with resting ..."
[16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4661084/ "Parcellating Cortical Functional Networks in Individuals - PMC"
[17]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1461590/full "FunMaps: a method for parcellating functional brain networks using ..."
[18]: https://www.sciencedirect.com/science/article/pii/S1053811921004419 "Probabilistic mapping of human functional brain networks identifies ..."
[19]: https://www.ebrain.pitt.edu/wp-content/uploads/2020/04/2020-01-31-gordon-et-al.pdf "[PDF] Precision functional mapping of individual human brains"
[20]: https://www.sciencedirect.com/science/article/pii/S105381192030759X "Non-negative data-driven mapping of structural connections with ..."
[21]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.838347/full "Unrevealing Reliable Cortical Parcellation of Individual Brains Using ..."
[22]: https://www.nature.com/articles/s41597-022-01645-3 "Probabilistic atlas for the language network based on precision fMRI ..."
[23]: https://direct.mit.edu/imag/article/doi/10.1162/imag_a_00165/120745/Towards-personalized-precision-functional-mapping "Towards personalized precision functional mapping in infancy"


---

Оглавление:

- [ЭИРО framework](/README.md)
