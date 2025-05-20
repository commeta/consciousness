# Описание Ventral Attention Network (VAN) 

**Краткий обзор основных положений:**
VAN включает ключевые узлы — правый темпоротопариетальный узел (TPJ) и вентролатеральную префронтальную кору (VLPFC), связанные дугообразным и иненним лобно-затылочным пучками. Сеть активируется в «oddball»-парадигмах и задачах перенаправления внимания, хорошо выявляется в resting-state и task-based fMRI. Функциональная сила связи VAN коррелирует с реактивностью и точностью выполнения задач, а её дисфункция отмечается при депрессии, шизофрении, ОКР и СДВГ; изменения связности VAN рассматриваются как потенциальные биомаркеры эффективности психофармакотерапии.

---

## **Ключевая функция:**

Автоматическое переключение внимания на неожиданные и важные внешние стимулы, действующее как «механизм аварийной переориентации» при встрече с девиантными событиями ([ScienceDirect][1], [ScienceDirect][2]).

---

## **Анатомия:**

* **Temporoparietal Junction (TPJ)**
  Обнаруживает внезапные и значимые сенсорные события, служит узлом «перехвата» внимания при появлении неожиданных стимулов ([ScienceDirect][1], [Википедия][3]).
* **Ventrolateral Prefrontal Cortex (VLPFC)**
  Инициирует акт перенаправления внимания и взаимодействует с моторными и сенсорными областями для реализации переключения ([ScienceDirect][1], [Википедия][3]).

---

## **Ключевые тракты / подсети:**

* **Arcuate fasciculus** (TPJ ↔ VLPFC)
  Основной белый пучок, обеспечивающий быструю связь между задними паритетальными и вентролатеральными фронтальными областями для синхронного реагирования ([PMC][4]).
* **Inferior fronto-occipital fasciculus (IFOF)** (VLPFC ↔ затылочные регионы)
  Длинный фронто-затылочный тракт, обеспечивающий обмен визуальной информацией и контрольным сигналам между зрительными и исполнительными областями ([Oxford Academic][5]).

---

## **Основные характеристики работы:**

* **Парадигмы активации:**

  * *Oddball* и *cueing*-задачи с девиантными стимулами демонстрируют надёжную активацию VAN при восприятии редких событий ([PMC][6]).
  * *Resting-state fMRI* выявляет сильную внутри-сетевую связность VAN, сопоставимую с другими крупными сетями внимания ([PMC][7]).
* **Нейрофизиологические механизмы:**
  MEG-исследования в *Posner*-задаче показывают временные профили переориентации внимания, где VAN выступает в роли «аварийного выключателя» текущей задачи ([PMC][6]).
* **Динамическое взаимодействие с DAN:**
  Последние модели подчёркивают гибкое переключение между топ-down (DAN) и bottom-up (VAN) модулями в зависимости от требований задачи ([PubMed][8], [Cell][9]).

---

## **Практические значения:**

* **Корреляция с поведением:**
  Укреплённая внутри-сетевая связность VAN ассоциируется с более быстрым временем реакции и повышенной точностью в задачах перенаправления внимания ([PubMed][8]).
* **Психопатология:**

  * *Большое депрессивное расстройство (MDD):* сниженная связность в precuneus/VAN ассоциируется с тяжестью симптомов ([Frontiers][10]).
  * *Шизофрения:* уменьшенная внутри-сетевая связность VAN наблюдается у пациентов, коррелируя с когнитивными дефицитами ([PubMed][11]).
  * *Обсессивно-компульсивное расстройство (ОКР):* мета-анализ выявил вовлечение VAN на ранних стадиях болезни ([Nature][12]).
  * *СДВГ:* межсетевые нарушения между DMN и VAN у детей с ADHD коррелируют с клиническими проявлениями гиперактивности и невнимательности ([Nature][13]).
* **Биомаркеры лечения:**
  Связность стриатума с VAN рассматривается как предиктор ответа на антипсихотическую терапию в шизофрении ([PubMed][14]).

---

## **Краткие примеры:**

* **MDD:** в исследовании 2022 г. обнаружено снижение функциональной связности VAN в прецунеусе у пациентов с MDD по сравнению с контролем ([Frontiers][10]).
* **Шизофрения:** анализ resting-state сетей показал значимое ослабление внутри-сети VAN у пациентов с шизофренией (p < 0.01) ([PubMed][11]).

---


## Таблица: Подсети Ventral Attention Network (VAN)

| Имя подсети                | Анатомические регионы                        | Atlas            | Структурный тракт                              | Функциональная роль                                              | Пересечения с сетями | Источник                                                                                                                                                                                            |
| -------------------------- | -------------------------------------------- | ---------------- | ---------------------------------------------- | ---------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Posterior VAN Subnetwork   | TPJ (IPL, pSTS)                              | AAL              | Arcuate fasciculus                             | Обнаружение неожиданных и значимых сигналов                      | SN                   | Corbetta & Shulman, 2008 (Neuron) ([Wikipedia](https://en.wikipedia.org/wiki/Ventrolateral_prefrontal_cortex))                                                                                      | 
| Anterior VAN Subnetwork    | VLPFC (BA44, BA45, BA47)                     | Brodmann’s areas | Arcuate fasciculus                             | Инициирование перераспределения внимания                         | CEN                  | Corbetta & Shulman, 2008 (Neuron) ([Wikipedia](https://en.wikipedia.org/wiki/Ventrolateral_prefrontal_cortex))                                                                                      | 
| Occipital-VLPFC Subnetwork | V1/V2 (occipital) ↔ VLPFC                    | HCP MMP1.0       | Inferior fronto-occipital fasciculus (IFOF)    | Передача визуальной информации для перераспределения внимания    | Vis                  | Tang et al., 2019 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/30978625/))                                                                                                                             | 
| SLF III-Based Subnetwork   | IPL (supramarginal gyrus) ↔ pars opercularis | Desikan–Killiany | Superior longitudinal fasciculus III (SLF III) | Поверхностное горизонтальное соединение для сдвига внимания      | Lang                 | Rodríguez-Fornells et al., 2019 ([ResearchGate](https://www.researchgate.net/publication/342434232_The_ventral_attention_network_the_mirror_of_the_language_network_in_the_right_brain_hemisphere)) | 
| Right-Lateralized VAN      | rTPJ (IPL + pSTS) & rVLPFC                   | Yeo 7            | —                                              | «Радар» правого полушария: реактивное перераспределение внимания | SN, CEN              | Quicktome Guide, 2022 ([Quicktome](https://quicktome.o8t.com/guide/network/ventral-attention-network))                                                                                              | 
| Left-Lateralized VAN       | lTPJ (IPL + pSTS) & lVLPFC                   | Yeo 7            | —                                              | Менее выраженная левая реактивная перераориентация               | CEN                  | Corbetta & Shulman, 2008 (Neuron) ([Wikipedia](https://en.wikipedia.org/wiki/Ventrolateral_prefrontal_cortex))                                                                                      |
| PFm Subnetwork             | PFm (angular & supramarginal gyri)           | HCP MMP1.0       | Arcuate/SLF                                    | Перераспределение внимания, языковая обработка, рабочая память   | Lang, CEN            | Quicktome Guide, 2022 ([Quicktome](https://quicktome.o8t.com/guide/network/ventral-attention-network))                                                                                              |
| PGi Subnetwork             | PGi (inferior parietal lobule)               | HCP MMP1.0       | —                                              | Переключение внимания, обработка лиц, восприятие речи            | SN                   | Quicktome Guide, 2022 ([Quicktome](https://quicktome.o8t.com/guide/network/ventral-attention-network))                                                                                              | 
| VAN-A Subnetwork           | VLPFC, anterior insula, dACC                 | Yeo 17           | —                                              | Обнаружение и фильтрация значимых стимулов                       | SN, CEN              | Schaefer et al., 2018 ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10132286/))                                                                                                                   |
| VAN-B Subnetwork           | TPJ, IPL, pSTS                               | Yeo 17           | —                                              | Перераспределение внимания на внешние стимулы                    | SN                   | Schaefer et al., 2018 ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10132286/))                                                                                                                   | 
| vlPFC Node                 | Area 47/12 (ventrolateral prefrontal cortex) | Brodmann’s areas | —                                              | Оценка значимости стимулов, интеграция информации                | SN, CEN              | Trambaiolli et al., 2022 ([eLife](https://elifesciences.org/articles/76334))                                                                                                                        | 

---


## **Ключевые обзоры:**

1. **Pozzi et al., 2023** — Обзор нейрофизиологических механизмов и динамического взаимодействия DAN/VAN ([PubMed][8]).
2. **Santarnecchi et al., 2024** — Тренды в механизмах внимания: физически активированные режимы контроля (Trends Cogn. Sci.) ([Cell][15]).
3. **Jaramillo et al., 2024** — Общие и уникальные нейронные механизмы внимания across model species (Trends Cogn. Sci.) ([Cell][9]).


[1]: https://www.sciencedirect.com/topics/medicine-and-dentistry/ventral-attention-network "Ventral Attention Network - an overview | ScienceDirect Topics"
[2]: https://www.sciencedirect.com/topics/immunology-and-microbiology/ventral-attention-network "Ventral Attention Network - an overview | ScienceDirect Topics"
[3]: https://en.wikipedia.org/wiki/Salience_network "Salience network"
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7495290/ "The ventral attention network: the mirror of the language network in ..."
[5]: https://academic.oup.com/brain/article/148/5/1507/8009026 "inferior fronto-occipital fasciculus: bridging phylogeny, ontogeny and ..."
[6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7978122/ "New insights on the ventral attention network: Active suppression ..."
[7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3918493/ "Resting State Functional Connectivity of the Ventral Attention ..."
[8]: https://pubmed.ncbi.nlm.nih.gov/37841074/ "Neuroimaging evidence supporting a dual-network architecture for ..."
[9]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613%2824%2900005-6 "Common and distinct neural mechanisms of attention - Cell Press"
[10]: https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.925253/full "Decreased Connectivity in Precuneus of the Ventral Attentional ..."
[11]: https://pubmed.ncbi.nlm.nih.gov/38077180/ "Functional Connectivity Alterations of Within and Between Networks ..."
[12]: https://www.nature.com/articles/s41593-023-01404-6 "Regional, circuit and network heterogeneity of brain abnormalities in ..."
[13]: https://www.nature.com/articles/s41398-020-0740-y "Shared and distinct resting functional connectivity in children and ..."
[14]: https://pubmed.ncbi.nlm.nih.gov/37797435/ "fMRI connectivity as a biomarker of antipsychotic treatment response"
[15]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613%2824%2900313-9?rss=yes "Physically activated modes of attentional control - Cell Press"


---


## Подробные технические характеристики

В этом разделе собраны основные методические детали и параметры анализа Ventral Attention Network (VAN) при различных нейровизуализирующих и аналитических подходах.

### Пространственные и временные разрешения

* **fMRI**:

  * *Пространственное разрешение*: типично 2–3 мм³ воксель (EPI-последовательности) ([PMC][16]).
  * *Временное разрешение*: TR ≈ 1.5–2.5 с, что определяет частоту выборки BOLD-сигнала ([PMC][16]).
* **MEG/EEG**:

  * *Временное разрешение*: миллисекунды (≥ 1 кГц дискретизации) для отслеживания быстрых осцилляций VAN ([PMC][17]).
  * *Пространственная локализация*: на уровне сантиметров с помощью source-localization алгоритмов (beamforming, MNE) ([Frontiers][18]).

### Метрики функциональной и эффективной связности

* **Функциональная связность (FC)**:

  * *Корреляционный анализ (Pearson r)* между средними временными рядами TPJ и VLPFC в resting-state fMRI ([PMC][19]).
  * *Seed-based analysis* (TPJ ↔ VLPFC), ICA и dual-regression для выделения VAN как отдельного компонента ([ScienceDirect][20]).
* **Эффективная связность (EC)**:

  * *Dynamic Causal Modeling (DCM)*: стохастическое DCM для оценки направленных влияний VLPFC → TPJ и обратно ([PubMed][21]).
  * *Granger Causality (GC)*: оценка направленных связей на основе предсказуемости временных рядов в MEG/fMRI (DAN → VAN, VAN → DAN) ([Journal of Neuroscience][22], [ScienceDirect][23]).

### Графовые характеристики

* **Модулярность (Modularity)**:

  * Оценка разделения VAN как «модуля» внутри широких мозговых сетей с помощью Louvain-алгоритма (γ = 1.0) ([PMC][24]).
* **Центральность (Betweenness, Participation Coefficient)**:

  * Важность узлов TPJ и VLPFC в передаче сигналов измеряется через betweenness centrality и participation coefficient ([PLOS][25]).
* **Динамические граф-метрики**:

  * Скользящее окно (SLiding Window) с длиной 30–60 с и шагом 1 TR для изучения варьabilности модульной структуры VAN ([ScienceDirect][26]).

### Спектральные особенности

* **Диапазоны частот**:

  * θ-диапазон (4–7 Гц): ассоциируется с инициированием переориентации ([PMC][17]).
  * β-диапазон (13–30 Гц): коррелирует с поддержанием нового фокуса внимания после переориентации ([PMC][17]).
* **Методы анализа**:

  * *Wavelet Transform* и multitaper спектральная оценка для извлечения мощности и синхронности между TPJ и VLPFC ([PMC][17]).
  * *Phase-locking value (PLV)* для измерения фазовой синхронизации в MEG/EEG данных ([BioRxiv][27]).

### Структурная организация (Diffusion MRI)

* **Тракто­графия**:

  * *Белые пучки*: Arcuate fasciculus и Inferior fronto-occipital fasciculus (IFOF) реконструируются методом probabilistic tractography (FSL probtrackx) ([PMC][19]).
* **Микроструктурные метрики**:

  * *Fractional Anisotropy (FA)* и *Mean Diffusivity (MD)* в трактах Arcuate fasciculus и IFOF коррелируют с функциональной связностью VAN ([PMC][19]).

---

*Этот раздел обобщает ключевые технические характеристики методов исследования VAN, позволяя стандартизировать протоколы и улучшить воспроизводимость результатов.*

[16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3918493/ "Resting State Functional Connectivity of the Ventral Attention ..."
[17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5895484/ "Oscillatory dynamics in the dorsal and ventral attention networks ..."
[18]: https://www.frontiersin.org/articles/10.3389/fnhum.2022.895034/full "Ventral Attention Network Correlates With High Traits of Emotion ..."
[19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10389834/ "Higher Functional Connectivity of Ventral Attention and Visual ..."
[20]: https://www.sciencedirect.com/topics/medicine-and-dentistry/ventral-attention-network "Ventral Attention Network - an overview | ScienceDirect Topics"
[21]: https://pubmed.ncbi.nlm.nih.gov/30978625/ "Ventral attention-network effective connectivity predicts individual ..."
[22]: https://www.jneurosci.org/content/32/4/1284 "Causal Interactions in Attention Networks Predict Behavioral ..."
[23]: https://www.sciencedirect.com/science/article/pii/S0959438812001845 "Analysing connectivity with Granger causality and dynamic causal ..."
[24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5512538/ "Functional Modular Architecture Underlying Attentional Control in ..."
[25]: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0242985 "Between-module functional connectivity of the salient ventral ... - PLOS"
[26]: https://www.sciencedirect.com/science/article/pii/S1053811924002337 "Evolving brain network dynamics in early childhood: Insights from ..."
[27]: https://www.biorxiv.org/content/10.1101/782649v1 "New insights on the ventral attention network: Inhibition and ..."

---


Оглавление:

- [ЭИРО framework](/README.md)
- [Нейросети мозга](/brain-networks/README.md)

