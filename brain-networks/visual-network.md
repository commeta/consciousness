# Описание Visual Network 

Visual Network формирует иерархию от первичных зон V1–V3 до ассоциативных областей в теменной и височной долях, взаимодействуя через оптические лучи и межкортикальные связи. В задаче покоя она проявляет устойчивые функциональные корреляции, а при зрительных экспериментах (дискриминация форм, цветоразличение, движение) активируется в зависимости от парадигмы. Нарушения этой сети выявляются при глаукоме, рассеянном склерозе, депрессии и шизофрении, коррелируя с ухудшением точности и скорости зрительных реакций.

## **Visual Network**

**Ключевая функция:**
Обработка и интеграция зрительной информации от первичной визуальной коры до ассоциативных областей, обеспечивающая восприятие контуров, цвета, движения и пространственную ориентацию ([ScienceDirect][1], [Википедия][2]).

## **Анатомия:**

* **V1 (Primary Visual Cortex):** первичная обработка контуров, ориентации и контраста, ретинотопическая карта ([Nature][3], [Википедия][2]).
* **V2–V4 (Extrastriate Areas):** анализ цветовых характеристик и простых форм ([ScienceDirect][1], [Википедия][2]).
* **V5/MT (Middle Temporal Area):** обработка зрительного движения и скорости ([ScienceDirect][1], [Википедия][2]).
* **Латеральная теменная кора (Lateral Parietal Cortex):** зрительно-пространственные преобразования и интеграция с вестибулярной информацией ([PMC][4]).

## **Ключевые тракты / подсети:**

* **Оптический луч (Optic Radiation):** основной путь от латерального коленчатого тела к V1, ключевой для передачи визуальных сигналов ([PMC][5], [PLOS][6]).
* **Связи V1 ↔ V5/MT:** межкортикальные ассоциации через белое вещество теменно-височных пучков, обеспечивающие интеграцию контраста и движения ([ScienceDirect][7], [SpringerLink][8]).

## **Основные характеристики работы:**

* **Resting-state fMRI:** Visual Network устойчиво проявляется как отдельная компонентная сеть в анализе покоя, демонстрируя высокую корреляцию BOLD-сигнала между V1–V5 и ассоциативными зонами ([ScienceDirect][1], [Frontiers][9]).
* **Task-based fMRI:** сильная активация в задачах визуальной дискриминации контуров, движущихся стимулов и цветоразличения; парадигмы включают ретинотопическое сканирование, адаптацию цветом и анализ сложных сцен ([Nature][3], [Nature][10]).

## **Практические значения:**

* **Когнитивные корреляции:** активность сети предсказывает скорость реакции и точность в визуальных задачах; снижение функциональной связности ассоциируется с замедлением восприятия и ухудшением детекции стимулов ([ScienceDirect][11], [Frontiers][12]).
* **Психопатология:** изменения в Visual Network выявляются при глаукоме (HTG), при которой наблюдается снижение связности V1 и ассоциативных зон ([Frontiers][12], [Frontiers][9]); при депрессии и шизофрении отмечаются дисбалансы между визуальными и высшими когнитивными сетями ([ScienceDirect][11], [Nature][3]).

## **Краткие примеры:**

* **Световые воздействия:** односекундная экспозиция синего света усиливает функциональную связность Visual Network, влияя на настроение и когнитивный контроль ([Nature][3]).
* **Глаукома:** уменьшение связности в V1–V2 коррелирует с тяжестью потери полей зрения у пациентов с HTG ([Frontiers][12]).


## Таблица: Подсети и области Visual Network

| Имя подсети                      | Анатомические регионы                                | Atlas                     | Структурный тракт                             | Функциональная роль                                        | Пересечения с сетями         | Источник                                                                                   |
| -------------------------------- | ---------------------------------------------------- | ------------------------- | --------------------------------------------- | ---------------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------ |
| Primary Visual Cortex Network    | V1 (BA17)                                            | HCP MMP 1.0               | Optic Radiation                               | Первичная обработка контрастов и контуров                  | Visual I (Yeo et al., 2011)  | [Felleman & Van Essen, 1991](https://pubmed.ncbi.nlm.nih.gov/1822724/)                     |
| Secondary Visual Areas Network   | V2–V4 (BA18/19)                                      | HCP MMP 1.0               | U-fibers между V1–V4                          | Обработка формы и цвета                                    | Visual II (Yeo et al., 2011) | [Felleman & Van Essen, 1991](https://pubmed.ncbi.nlm.nih.gov/1822724/)                     |
| Motion-sensitive (MT/V5) Network | V5/MT                                                | Wang MT Probability Atlas | Vertical Occipital Fasciculus (VOF)           | Детекция и оценка движения                                 | Visual II / DAN              | [Wang et al., 2015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4333555/)                 |
| Dorsal Visual Stream Network     | V3a, V7, IPS                                         | HCP MMP 1.0               | Superior Longitudinal Fasciculus (SLF I–III)  | Зрительно-пространственные преобразования                  | DAN                          | [Glasser et al., 2016](https://pubmed.ncbi.nlm.nih.gov/26943602/)                          |
| Ventral Visual Stream Network    | V4, LOC, Fusiform Gyrus                              | HCP MMP 1.0               | Inferior Longitudinal Fasciculus (ILF)        | Распознавание объектов, цвето-форма                        | Visual III                   | [Tanaka, 2003](https://doi.org/10.1093/cercor/13.1.90)                                     |
| Occipital Pole Network           | Cuneus, Lingual Gyrus                                | HCP MMP 1.0               | Vertical Occipital Fasciculus (VOF)           | Централизованная обработка центрального поля зрения        | Visual I                     | [Smith et al., 2009](https://doi.org/10.1016/j.neuroimage.2009.02.025)                     |
| Fusiform Face Complex (FFC)      | Fusiform Gyrus (FG2/FG4)                             | HCP MMP 1.0               | Inferior Longitudinal Fasciculus (ILF)        | Специфическая обработка и распознавание лиц                | Visual III                   | [Kanwisher et al., 1997](https://doi.org/10.1523/JNEUROSCI.17-11-04302.1997)               |
| Visual Medial Network            | Medial occipital cortex                              | HCP MMP 1.0               | MOLT (медиальный окципито-темпоральный тракт) | Обработка базовых визуальных стимулов                      | Visual I                     | [Glasser et al., 2016](https://pubmed.ncbi.nlm.nih.gov/26943602/)                          |
| Visual Lateral Network           | Middle temporal visual area (MT/V5 adj.)             | HCP MMP 1.0               | IFOF (Inferior Fronto-Occipital Fasciculus)   | Обработка сложных (эмоциональных) зрительных стимулов      | Visual III                   | [Pessoa et al., 2002](https://doi.org/10.1073/pnas.172403899)                              |
| Visual Occipital Network         | Задние окципитальные области                         | HCP MMP 1.0               | Внутриокципитальные U-fibers                  | Обработка высокоуровневых зрительных стимулов              | Visual II                    | [Power et al., 2011](https://doi.org/10.1016/j.neuroimage.2011.01.044)                     |
| Visual Periphery Network         | Периферические представительства поля зрения (V1/V2) | HCP MMP 1.0               | VOF / ILF                                     | Обработка периферического зрения                           | Visual I                     | [Kastrup et al., 2008](https://doi.org/10.1016/j.neuroimage.2008.04.242)                   |
| V3 Network                       | V3                                                   | HCP MMP 1.0               | ILF, IFOF, MdLF                               | Интеграция среднеглобального движения и визуальных потоков | Visual II                    | [White et al., 2015](https://doi.org/10.1016/j.neuroimage.2015.04.044)                     |
| V4t Network                      | V4t                                                  | HCP MMP 1.0               | SLF (короткие ветви), VOF                     | Интеграция информации дорсального и вентрального потоков   | Visual II / DAN / VAN        | [Glasser et al., 2016](https://pubmed.ncbi.nlm.nih.gov/26943602/)                          |
| Occipital Face Area (OFA)        | Inferior Occipital Gyrus                             | HCP MMP 1.0               | ILF, короткие U-fibers                        | Начальная обработка лицевых признаков                      | Visual II                    | [Pitcher et al., 2011](https://doi.org/10.1523/JNEUROSCI.5166-10.2011)                     |
| Visual Central Network           | Calcarine sulcus, Cuneus                             | HCP MMP 1.0               | VOF                                           | Специфическая обработка центрального поля зрения           | Visual I                     | [Smith et al., 2009](https://doi.org/10.1016/j.neuroimage.2009.02.025)                     |
| Visual Extrastriate Network      | V2, V3, V4                                           | HCP MMP 1.0               | U-fibers, ILF                                 | Обработка сложных визуальных стимулов                      | Visual II                    | [Rottschy et al., 2007](https://doi.org/10.1016/j.neuroimage.2007.07.050)                  |
| Visual Word Form Area (VWFA)     | Left occipitotemporal cortex (BA37)                  | HCP MMP 1.0               | Inferior Longitudinal Fasciculus (ILF)        | Обработка визуального представления слов                   | Reading Network              | [Dehaene et al., 2002](https://doi.org/10.1097/00001756-200203040-00015)                   |
| Visual Subnetwork A\B            | Общая окципитальная область                          | Yeo 17-network            | Внутриокципитальные U-fibers                  | Обработка основных зрительных стимулов                     | Visual I                     | [Yeo et al., 2011](https://doi.org/10.1016/j.neuroimage.2011.02.003)                       |



## **Ключевые обзоры:**

1. **Resting-State Functional Connectivity** (ScienceDirect, 2010) — обзор методов и сетей, включая Visual Network ([ScienceDirect][1]).
2. **Heuvel & Hulshoff Pol, 2010** — рецензия по таксономии сетей покоя и их эволюционному значению ([Questions and Answers ​in MRI][13]).
3. **Resting-state fMRI of the visual system** (Frontiers in Human Neuroscience, 2022) — современные данные о паттернах при зрительных нейропатиях ([Frontiers][9]).
4. **Functional Alterations in Resting-State Visual Networks** (Frontiers, 2020) — изменения сети при окулоневрологических заболеваниях ([Frontiers][12]).
5. **Probabilistic MRI Tractography of the Optic Radiation** (PLOS One, 2015) — методики картирования оптических лучей и их надежность ([PLOS][6]).

[1]: https://www.sciencedirect.com/topics/neuroscience/resting-state-functional-connectivity "Resting-State Functional Connectivity - ScienceDirect.com"
[2]: https://en.wikipedia.org/wiki/Resting_state_fMRI "Resting state fMRI"
[3]: https://www.nature.com/articles/s41598-022-20668-9 "Functional connectivity of brain networks with three monochromatic ..."
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5524274/ "A review on methods in resting state connectivity analysis and ..."
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3223565/ "Diffusion tensor imaging tractography of the optic radiation for ..."
[6]: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0118948 "Probabilistic MRI Tractography of the Optic Radiation Using ... - PLOS"
[7]: https://www.sciencedirect.com/science/article/abs/pii/S1878875018310842 "Optic Radiation Diffusion Tensor Imaging Tractography"
[8]: https://link.springer.com/article/10.1007/s00701-023-05540-7 "and high-resolution fiber tractography for the delineation of the optic ..."
[9]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2022.943618/full "Resting-state functional MRI of the visual system for characterization ..."
[10]: https://www.nature.com/articles/s41598-021-83246-5 "Brain functional connectivity differs when viewing pictures from ..."
[11]: https://www.sciencedirect.com/science/article/pii/S2213158219301251 "Visual network alterations in brain functional connectivity in chronic ..."
[12]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2020.00330/full "Functional Alterations in Resting-State Visual Networks in High ..."
[13]: https://mriquestions.com/uploads/3/4/5/7/34572113/heuvel_reviewbrainnets1.pdf "[PDF] Exploring the brain network: A review on resting-state fMRI ..."


---


## Подробные технические характеристики

**Краткое резюме:**
Этот раздел охватывает ключевые настройки сбора данных (пространственное и временное разрешение, время эхо), стандартные шаги предобработки (коррекция смещений, нормализация, сглаживание), методы анализа функциональной связности (статические и динамические подходы), применение графовых алгоритмов (центральность, модулярность), частотный анализ BOLD-сигнала и стратегии порогирования матриц связности.

---

### Параметры сбора данных

* **Пространственное разрешение (voxel size):**
  Обычно используют воксели 3 × 3 × 3 мм³, что покрывает всю толщину коры и включает мезоскопические структуры ([Frontiers][14]).
  На высокопольных томографах (7 T) достигают разрешения до 0.5 мм ([PMC][15]).

* **Временное разрешение (TR):**
  Стандартные значения TR составляют 0.72–2 с в зависимости от последовательности (2D-EPI, SMS-EPI, 3D-EPI-CAIPI) ([PMC][16], [ScienceDirect][17]).

* **Время эхо (TE):**
  Обычно TE ≈ 30 мс для оптимизации BOLD-чувствительности в сером веществе ([PMC][18]).

---

### Предобработка данных

* **Коррекция движения и слайс-тайминг:**
  Удаление артефактов смещения головы и выравнивание временных срезов ([PMC][19]).
* **Пространственная нормализация:**
  Регистрация к стандартной мозговой атласу (MNI152) для групповых анализов ([Nature][20]).
* **Сглаживание:**
  Gaussian kernel 4–8 мм FWHM для повышения SNR и учёта межсубъектных различий ([PMC][19]).

---

### Анализ функциональной связности

* **Статическая FC:**
  Расчёт попарного корреляционного коэффициента Пирсона между временными рядами ROI и последующее преобразование в z-оценки через Fisher’s r-to-z ([PMC][21], [PMC][18]).

* **Динамическая FC:**
  Метод скользящего окна (sliding window) длиной 30–60 с с шагом 1–2 с для оценки изменения связности во времени ([PMC][22], [PMC][23]).

---

### Анализ по теории графов

* **Degree Centrality:**
  Количество прямых связей узла; выявляет «хабы» сети ([Cambridge Intelligence][24], [Школа медицины Тулейн][25]).

* **Betweenness Centrality:**
  Доля кратчайших путей, проходящих через узел; отражает его роль в интеграции информации ([Школа медицины Тулейн][25]).

* **Modularity:**
  Степень разбиения сети на кластеры/модули; оценивает функциональную сегрегацию ([Frontiers][26]).

---

### Частотный анализ

* BOLD-сигнал делят на четыре основных частотных диапазона (F1–F4):

  * F1: 0.007–0.052 Hz
  * F2: 0.052–0.106 Hz
  * F3: 0.106–0.206 Hz
  * F4: 0.206–0.438 Hz

  Эти диапазоны сопоставимы с ранее описанными «slow-5» и «slow-4» в resting-state fMRI ([Nature][27], [PMC][28]).

---

### Стратегии порогирования

* **Пропорциональное порогирование:**
  Отбор верхних 10–20 % сильнейших связей для сохранения равной плотности матриц между группами ([ScienceDirect][29], [PMC][21]).

* **Статистическое порогирование (Double Delta Threshold, DDT):**
  Одновременное применение двух статистических порогов для учёта слабых, но значимых связей ([PMC][30]).

---

* Приведённые параметры отражают наиболее распространённые и проверенные практики при изучении Visual Network.

[14]: https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2016.00066/full "fMRI at High Spatial Resolution: Implications for BOLD-Models"
[15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3073717/ "Overview of Functional Magnetic Resonance Imaging - PMC"
[16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6051935/ "Resting-State Functional MRI: Everything That Nonexperts Have ..."
[17]: https://www.sciencedirect.com/science/article/pii/S105381192100776X "Advances in resting state fMRI acquisitions for functional connectomics"
[18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4035703/ "Resting-State fMRI: A Review of Methods and Clinical Applications"
[19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6865661/ "Modular preprocessing pipelines can reintroduce artifacts into fMRI ..."
[20]: https://www.nature.com/articles/s41467-024-48781-5 "Systematic evaluation of fMRI data-processing pipelines for ... - Nature"
[21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5981009/ "Thresholding functional connectomes by means of mixture modeling"
[22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3807588/ "Dynamic functional connectivity: Promise, issues, and interpretations"
[23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7375061/ "Dynamic visual cortical connectivity analysis based on functional ..."
[24]: https://cambridge-intelligence.com/keylines-faqs-social-network-analysis/ "Social Network Analysis: Understanding Centrality Measures"
[25]: https://medicine.tulane.edu/sites/default/files/GraphTheoryAPrimertoUnderstandingRestingStatefMRI.pdf "[PDF] Graph Theory: A Primer to Understanding Resting State fMRI"
[26]: https://www.frontiersin.org/articles/10.3389/fnhum.2015.00386/full "GRETNA: a graph theoretical network analysis toolbox for imaging ..."
[27]: https://www.nature.com/articles/s41598-023-29321-5 "Frequency-specific brain network architecture in resting-state fMRI"
[28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4313418/ "Functional Integration Between Brain Regions at Rest Occurs in ..."
[29]: https://www.sciencedirect.com/science/article/pii/S105381191730109X "Proportional thresholding in resting-state fMRI functional ..."
[30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8415479/ "Thresholding Functional Connectivity Matrices to Recover the ..."


---


Оглавление:

- [ЭИРО framework](/README.md)
- [Нейросети мозга](/brain-networks/README.md)


