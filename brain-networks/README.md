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



Оглавление:

- [ЭИРО framework](/README.md)
