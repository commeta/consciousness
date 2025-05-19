# Описание Sensorimotor Integration Network (SMIN)

**Ключевая функция:**
SMIN отвечает за интеграцию проприоцептивной, тактильной и моторной информации для точного планирования и исполнения движений, обеспечивая связь между восприятием окружающей среды и моторными командами ([Frontiers][1]).

## **Анатомия**

* **Premotor Cortex (PMC):** ключевая зона планирования движений, участвует в подготовке моторных программ и комбинировании зрительных и проприоцептивных сигналов ([MDPI][2]).
* **Supplementary Motor Area (SMA):** обеспечивает инициацию и координацию последовательных движений, особенно при выполнении внутренне запланированных действий ([Википедия][3]).
* **Parietal Cortex (PPC):** задействована в обработке сенсорной обратной связи и трансформации пространственной информации в координаты для моторного исполнения ([MDPI][2]).

## **Ключевые тракты / подсети**

* **Спиноталамические и таламокортикальные пути:** передают проприоцептивную и соматосенсорную информацию из спинного мозга в кору для последующей интеграции ([Frontiers][4]).
* **Ассоциативные связи PMC–SMA через внутреннюю капсулу:** обеспечивают быструю передачу моторных планов и обратных связей между зонами планирования и исполнения ([ScienceDirect][5]).

## **Основные характеристики работы**

* **Задачи с высокой моторной нагрузкой:** сеть активируется при выполнении произвольных движений (например, при нажатии пальцем), отображая готовность моторных областей ([Википедия][3]).
* **Paradigm resting-state vs. task-based fMRI:** в состоянии покоя SMIN демонстрирует выраженную синхронность между сенсомоторными областями, тогда как при выполнении задач усиливается специфическая топографическая активация ([Nature][6]).
* **Роль нейронных осцилляций β-диапазона:** бета-ритмы в сенсомоторной коре связаны с удержанием позы и преддвиженческими процессами, снижаясь перед началом движения ([Frontiers][7]).

## **Практические значения**

* **Корреляция с показателями скорости и точности:** усиленная функциональная связь внутри SMIN обеспечивает более высокую точность выполнения моторных задач и более короткое время реакции ([Frontiers][8]).
* **Связь с психопатологией и неврологией:**

  * При болезни Паркинсона отмечаются нарушения интеграции проприоцепции и моторного исполнения, что приводит к дискоординации движений ([PubMed][9]).
  * У пациентов с хрониче­ской болью (например, при хронической боли в пояснице) изменение сенсомоторного контроля связано с ухудшением моторных навыков и усилением боли ([ScienceDirect][10]).

## **Краткие примеры**

* **Оценка баланса после ЧМТ:** использование Central Sensorimotor Integration (CSMI) теста выявило у пациентов с хроническим легким ТBI дефициты интеграции сенсомоторных сигналов при стоянии ([Frontiers][8]).
* **Имитация движений в реабилитации:** в экспериментах с моторной имитацией показано, что усиление обратных связей в SMIN повышает эффективность восстановления моторных функций после инсульта ([PMC][11]).

## **Ключевые обзоры**

1. **Targeting Sensory and Motor Integration for Recovery of Movement** — Frontiers in Neuroscience (2021). Рассматривает механизмы сенсомоторной интеграции и их роль в обучении движения ([Frontiers][1]).
2. **Emergent Aspects of the Integration of Sensory and Motor Functions** — Brain Sciences (MDPI, 2025). Обзор взаимодействия кортикальных и подкоровых областей в контроле движений ([MDPI][2]).
3. **Sensorimotor Integration and Pain Perception** — Frontiers in Integrative Neuroscience (2022). Анализ путей сенсомоторной интеграции в контексте болевых ощущений ([Frontiers][4]).


[1]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.791824/full "Targeting Sensory and Motor Integration for Recovery of Movement ..."
[2]: https://www.mdpi.com/2076-3425/15/2/162 "Emergent Aspects of the Integration of Sensory and Motor Functions"
[3]: https://en.wikipedia.org/wiki/Sensorimotor_network "Sensorimotor network"
[4]: https://www.frontiersin.org/journals/integrative-neuroscience/articles/10.3389/fnint.2022.931292/full "Sensorimotor Integration and Pain Perception - Frontiers"
[5]: https://www.sciencedirect.com/topics/neuroscience/sensorimotor-integration "Sensorimotor Integration - an overview | ScienceDirect Topics"
[6]: https://www.nature.com/articles/s41467-024-47748-w "Functional connectivity development along the sensorimotor ..."
[7]: https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2021.655886/full "Understanding the Role of Sensorimotor Beta Oscillations - Frontiers"
[8]: https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2022.897454/full "Central sensorimotor integration assessment reveals deficits in ..."
[9]: https://pubmed.ncbi.nlm.nih.gov/38002513/ "Brain Networks Involved in Sensory Perception in Parkinson's Disease"
[10]: https://www.sciencedirect.com/science/article/pii/S0306452224002653 "Sensorimotor Integration in Chronic Low Back Pain - ScienceDirect"
[11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10968555/ "Cortical Sensorimotor Integration as a Neural Origin of Impaired Grip ..."


---


## **Подробные технические характеристики SMIN**

### Методы сбора данных и разрешение

* **fMRI BOLD-параметры:**
  Пространственное разрешение при стандартном сканировании на 3 T составляет \~2–3 мм³, тогда как на высокопольных 7 T достигается субмиллиметровая дискретизация ([PMC][12], [ScienceDirect][13]).
* **Временное разрешение:**
  Время повтора (TR) варьируется от 0.5 до 2 с, с учётом гемодинамического лага (\~3–5 с) ([PMC][12]).

### Предобработка и очистка сигналов

* **FuNP Pipeline:**
  Автоматическая конвейеризация предобработки (коррекция движений, выравнивание, сегментация, нормализация) на базе AFNI, FSL, FreeSurfer и Workbench ([Frontiers][14]).
* **Регрессия артефактов движения и фильтрация:**
  Удаление шума движения и высокочастотных дрейфов, а также применение полосового фильтра 0.01–0.1 Гц для устранения физиологического шума ([PMC][15]).

### Метрики функциональной связности

* **Корреляционный анализ (Pearson):**
  Определение линейной синхронности BOLD-сигналов между ROI ([PMC][15]).
* **Partial correlation & mutual information:**
  Учёт косвенных и нелинейных взаимосвязей между областями.
* **Functional Connectivity Overlap Ratio (FCOR):**
  Метрика перекрытия функциональных сетей, демонстрирующая паттерны дисфункции SMIN в клинических группах ([Oxford Academic][16]).

### Графовые характеристики сети

* **Small-worldness (σ > 1):**
  Баланс локальной кластеризации и глобальной интеграции, характерный для SMIN ([PMC][17], [onlinelibrary.wiley.com][18]).
* **Модулярность (Q ≈ 0.4–0.6):**
  Степень сегрегации сети на функциональные подсети ([PMC][17]).
* **Degree centrality (10–15 ребер/узел):**
  Средняя степень узлов при пороговой корреляции 0.2–0.3 ([medicine.tulane.edu][19]).
* **Глобальная эффективность (Eglob ≈ 0.25–0.35):**
  Интеграция информации через кратчайшие пути в сети ([apertureneuro.org][20]).
* **Локальная эффективность (Eloc ≈ 0.45–0.55):**
  Устойчивость сети к удалению узлов и локальная передача информации ([apertureneuro.org][20]).

### Частотный анализ

* **β-диапазон (13–30 Гц):**
  Ассоциирован с удержанием моторного состояния; мощность β снижается перед движением и восстанавливается после .
* **Альфа-ритм (8–12 Гц):**
  Связан с покоящейся активностью моторных областей; снижение альфа-мощности отражает готовность к действию ([PMC][21]).

### Динамическая функциональная связность

* **Sliding window (30–60 с, шаг 1–2 с):**
  Оценка временных изменений связности SMIN в рамках фиксированного окна ([Frontiers][22]).
* **Spatially constrained ICA (scICA):**
  Пространственно ограниченный ICA для извлечения динамических паттернов активности SMIN на уровне вокселя ([Frontiers][22]).

> **Примечание:** все указанные параметры могут варьироваться в зависимости от конкретных протоколов исследования и аппаратных возможностей оборудования.

[12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3073717/ "Overview of Functional Magnetic Resonance Imaging - PMC"
[13]: https://www.sciencedirect.com/science/article/abs/pii/S0301008221001982 "How pushing the spatiotemporal resolution of fMRI can advance ..."
[14]: https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2019.00005/full "FuNP (Fusion of Neuroimaging Preprocessing) Pipelines: A Fully ..."
[15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12025223/ "Neuroimaging Changes in the Sensorimotor Network and Visual ..."
[16]: https://academic.oup.com/braincomms/article/4/5/fcac214/6672862 "Connectivity impairment of cerebellar and sensorimotor connector ..."
[17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11474538/ "Graph Metrics Reveal Brain Network Topological Property in ..."
[18]: https://onlinelibrary.wiley.com/doi/full/10.1002/brx2.70025 "Small‐world network and neuroscience - Han - 2025 - Brain‐X"
[19]: https://medicine.tulane.edu/sites/default/files/GraphTheoryAPrimertoUnderstandingRestingStatefMRI.pdf "[PDF] Graph Theory: A Primer to Understanding Resting State fMRI"
[20]: https://apertureneuro.org/article/124565 "Development of the whole-brain functional connectome explored via ..."
[21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7775663/ "Sensorimotor Functional Connectivity: A Neurophysiological Factor ..."
[22]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1484954/full "Integrating fMRI spatial network dynamics and EEG spectral power"


---


Оглавление:

- [ЭИРО framework](/README.md)
- [Нейросети мозга](/brain-networks/README.md)

