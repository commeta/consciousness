# Описание Basal Ganglia Network, BGN) 

В этой сети ключевую роль играют параллельные петли, обеспечивающие регуляцию мотивации, выбор действий и процедурное обучение. Анатомически BGN включает стриатум (хвостатое ядро, putamen), глобус паллидум (GPe/GPi), субстанция нигра и субталамическое ядро, соединённые между собой несколькими важными трактами (nigrostriatal, pallidothalamic, прямой и непрямой путь). Сеть активируется как в состоянии покоя (resting-state fMRI), так и во множестве когнитивных и моторных задач (task-based fMRI). Функциональные изменения BGN отмечаются при болезни Паркинсона, депрессии, СДВГ и шизофрении, коррелируя с клинической симптоматикой и результатами поведенческих тестов.

## **Basal Ganglia Network (BGN)**

### **Ключевая функция:**

BGN отвечает за регуляцию мотивации, выбор действий и процедурное обучение через параллельные «мотивационные», «когнитивные» и «моторные» петли, связывающие кору, стриатум и выводные ядра базальных ганглиев ([Frontiers][1]). Динамическая модель «push-pull» показывает, как изменение баланса возбуждающих и ингибирующих влияний в BGN влияет на моторные симптомы при болезни Паркинсона ([Nature][2]).

### **Анатомия:**

* **Стриатум** (corpus striatum): хвостатое ядро (caudate nucleus) и putamen формируют входные ядра BGN, получающие кортикостриарные возбуждающие проекции ([НЦБИ][3], [Frontiers][4]).
* **Глобус паллидум**: внешняя (GPe) и внутренняя (GPi) сегменты — ключевые выводные ядра BGN, модулирующие кортикальные сигналы через таламус ([Frontiers][4]).
* **Субстанция нигра**: pars compacta (SNc) — источник дофаминергической модуляции BGN; pars reticulata (SNr) — функционирует как выходное ядро, аналогичное GPi ([Frontiers][1]).
* **Субталамическое ядро (STN)** — участвует в непрямом пути, усиливая ингибиторные влияния на GPi через возбуждающие глутаматергические проекции ([Nature][5]).

### **Ключевые тракты / подсети:**

* **Nigrostriatal pathway** (SNc ↔ striatum): дофаминергическая модуляция входных сигналов ([Frontiers][1]).
* **Pallidothalamic fibers** (GPi ↔ thalamus ↔ cortex): основная «выходная» связь BGN с корой через вентральные ядра таламуса ([Frontiers][4]).
* **Прямая петля** (striatum → GPi/SNr → thalamus → cortex): облегчает выполнение выбранных действий ([Nature][5]).
* **Непрямая петля** (striatum → GPe → STN → GPi/SNr → thalamus → cortex): подавляет конкурирующие или нежелательные моторные программы ([Nature][5]).

### **Основные характеристики работы:**

* **Resting-state fMRI:** BGN проявляет устойчивую сетевую корреляцию в покое, снижение которой отмечается при ранних стадиях болезни Паркинсона и когнитивных нарушениях ([Oxford Academic][6]).
* **Task-based fMRI:** активируется при моторных задачах (движение пальца, планирование), когнитивных (рабочая память, обучение) и мотивационных (условное подкрепление) парадигмах ([Frontiers][7]).
* **Парадигмы:** частые подходы – сравнительный анализ активации BGN в состоянии покоя и в ходе задач, моделирование функций прямых и непрямых путей с помощью динамического казуального моделирования (spDCM) ([Frontiers][8]).

### **Практические значения:**

* **Болезнь Паркинсона:** асимметрия функциональной связи BGN коррелирует с тяжестью моторных симптомов, а нормализация связей после глубокой мозговой стимуляции связана с клиническим улучшением ([Научный Директор][9], [Nature][2]).
* **Большое депрессивное расстройство (МДД):** гипо- и гиперконнектность в базоганглио-таламо-кортикальных цепях связана с симптомами депрессии и может служить биомаркерами ответа на лечение ([Nature][10], [PubMed][11]).
* **СДВГ:** нарушения динамики функциональной сети BGN отражаются в изменениях времени пребывания в разных состояниях rs-fMRI, что согласуется с гиперактивностью и дефицитом внимания ([Frontiers][12], [PMC][13]).
* **Шизофрения:** снижение эффективной связи BGN в префронтально-стриальной петле ассоциируется с когнитивными расстройствами и отрицательными симптомами ([Frontiers][8]).

### **Краткие примеры:**

* **PD + DBS:** модель «push-pull» выявила компенсацию через STN-GPi-таламус, объясняя механизм улучшения моторики после стимуляции STN ([Nature][2]).
* **ADHD (дети vs. взрослые):** взрослые пациенты проводят больше времени в состоянии с повышенной коннектностью BGN, что коррелирует с улучшением контроля внимания взрослением ([Frontiers][12]).
* **МДД (7T fMRI):** снижение связи между putamen и superior temporal gyrus у пациентов с депрессией подтверждено на высоком разрешении ([Nature][10]).

### **Ключевые обзоры:**

* Hagen J. et al. Phenomena of hypo- and hyperconnectivity in basal ganglia-thalamo-cortical circuits linked to major depression: a 7T fMRI study. Mol Psychiatry. 2025. ([PubMed][11])
* Martín A. & Knutson B. The reward circuit: linking primate anatomy and human imaging. Neuropsychopharmacology. 2010. [PubMed](https://pmc.ncbi.nlm.nih.gov/articles/PMC3055449/)
* Lanciego JG, Luquin N, Obeso JA. Functional neuroanatomy of the basal ganglia: Cold Spring Harb Perspect Med. 2012. [CSH Perspectives](https://www.ncbi.nlm.nih.gov/books/NBK53216/)
* Push-pull effects of basal ganglia network in Parkinson's disease: Nature NPJ Parkinson’s Disease. 2024. ([Nature][2])
* Basal ganglia for beginners: Frontiers in Systems Neuroscience. 2023. ([Frontiers][1])
* Integrative and network-specific connectivity of the basal ganglia, thalamus and cortex: Trends in Neurosciences. 2019. ([Научный Директор][14])

---

Таким образом, сеть базальных ганглиев является ключевым узлом в регуляции моторных, когнитивных и мотивационных процессов, а её функциональные нарушения — важным механизмом многих неврологических и психиатрических расстройств.

[1]: https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2023.1242929/full "Basal ganglia for beginners: the basic concepts you need to know ..."
[2]: https://www.nature.com/articles/s41531-024-00835-7 "Push-pull effects of basal ganglia network in Parkinson's disease ..."
[3]: https://www.ncbi.nlm.nih.gov/books/NBK537141/ "Neuroanatomy, Basal Ganglia - StatPearls - NCBI Bookshelf"
[4]: https://www.frontiersin.org/journals/neuroanatomy/articles/10.3389/fnana.2021.725731/full "Quantitative Susceptibility Mapping of the Basal Ganglia ... - Frontiers"
[5]: https://www.nature.com/articles/s41586-021-03993-3 "The mouse cortico–basal ganglia–thalamic network | Nature"
[6]: https://academic.oup.com/braincomms/article/5/2/fcad123/7116909 "Basal ganglia functional connectivity network analysis does not ..."
[7]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.526645/full "Dynamic Neural Network Changes Revealed by Voxel-Based ..."
[8]: https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2020.577482/full "Altered Prefrontal–Basal Ganglia Effective Connectivity in Patients ..."
[9]: https://www.sciencedirect.com/science/article/abs/pii/S0006899325001349 "Basal ganglia connectivity and network asymmetry in Parkinson's ..."
[10]: https://www.nature.com/articles/s41380-024-02669-4 "Phenomena of hypo- and hyperconnectivity in basal ganglia ..."
[11]: https://pubmed.ncbi.nlm.nih.gov/39020104/ "and hyperconnectivity in basal ganglia-thalamo-cortical circuits ..."
[12]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2021.697696/full "Differences in Disrupted Dynamic Functional Network Connectivity ..."
[13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11345791/ "Frequency-specific static and dynamic neural activity indices in ..."
[14]: https://www.sciencedirect.com/science/article/pii/S0896627319309754 "Integrative and Network-Specific Connectivity of the Basal Ganglia ..."


---


## **Подробные технические характеристики BGN**

В этом разделе представлены метрики и параметры, которые чаще всего используются при изучении BGN с помощью методов графовой теории, фМРТ и электрофизиологии.

### **1. Парцелляция и узловая структура**

* **Число узлов**: BGN обычно выделяют в рамках парцелляций от 90 до 200 регионов интереса (ROIs), включая хвостатое ядро, putamen, GPe/GPi, SNc/SNr и STN ([PMC][15]).
* **Пространственное разрешение**: при фМРТ-исследованиях классический TR = 2 с, в высокоразрешающих 7 Т сканерах достигают TR ≈ 0.8 с и вокселей \~1.2 мм ([PMC][16]).
* **Подходы к белому веществу**: в DTI-анализе используют до 100 000 детектируемых траекторий для построения матрицы SC (structural connectivity) между узлами BGN ([Научный Директор][17]).

### **2. Топологические (графовые) метрики**

* **Степень (Degree Centrality)**: средний узловой коэффициент степени в BGN составляет 15–20 связей на узел, при этом caudate nucleus и putamen часто выступают «хабами» с DC > 25 ([PMC][18], [Frontiers][19]).
* **Коэффициент кластеризации (Clustering Coefficient, Cp)**: в здоровых испытуемых локальный Cp в узлах BGN лежит в диапазоне 0.35–0.45, что свидетельствует о выраженной модульной структуре ([PMC][20], [Научный Директор][21]).
* **Средний путь (Characteristic Path Length)**: средняя длина путей между узлами BGN ≈ 2.5 ± 0.3 «скачка» по сети, что обеспечивает быструю интеграцию информации ([PMC][20], [ResearchGate][22]).
* **Мировые параметры (Small-worldness, σ)**: σ = (Cp/Cp_rand)/(Lp/Lp_rand) ≈ 1.2–1.4, подтверждая баланс локальной кластеризации и глобальной интеграции ([PMC][20], [PubMed][23]).
* **Модульность (Modularity, Q)**: при оптимальном разбиении Q ≈ 0.3–0.4, BGN делится на 3–4 подсети (мотивационная, когнитивная, моторная) ([PMC][24]).
* **Межузловая центральность (Betweenness Centrality)**: у caudate nucleus и SNr значения BC > 0.15, что указывает на их роль «мостов» между модулями ([Научный Директор][25]).

### **3. Спектральные и электрические характеристики**

* **Полосы частот LFP**: в STN и SNc доминируют бета-колебания (13–30 Гц) и высокочастотные гамма-ритмы (50–90 Гц) ([PMC][26], [PubMed][27]).
* **Спектральная мощность (PSD)**: относительная мощность в полосе бета у пациентов с PD увеличена на 20–30 % по сравнению с контролем ([PMC][28], [PubMed][27]).
* **Кросс-спектральная когерентность**: между putamen и моторной корой Cxy ≈ 0.4–0.6 в бета-диапазоне при движении пальца ([Nature][29], [Научный Директор][30]).

### **4. Временные характеристики**

* **Длительность состояний rs-fMRI**: BGN сохраняет устойчивые состояния коннективности с длительностью \~30–50 с каждое, общая вариабельность \~10 % ([PubMed][31]).
* **Частота обновления (fMRI TR)**: в стандартных протоколах TR = 2 с, при использовании multiband ехо-планарных последовательностей TR может быть уменьшен до 0.8 с для более точного захвата динамики ([PMC][16]).
* **Временные лага-корреляции**: максимальная автокорреляция сигналов BGN при смещении 1–2 TR (\~2–4 с), что отражает медленные колебания < 0.1 Гц ([PMC][24]).

### **5. Параметры эффективной коннективности (DCM)**

* **Моделирование прямого и непрямого путей**: оценки модуляции прямой петли (striatum → GPi → thal) ≈ 0.4–0.6 Hz, непрямой (striatum → GPe → STN) ≈ 0.2–0.4 Hz ([Frontiers][32], [PMC][16]).
* **Контекстная модуляция**: параметр B в spDCM, отвечающий за влияние задания на связь striatum–GPi, среднее значение B ≈ 0.05–0.1, статистически значимо (p < 0.01) ([Frontiers][32], [Frontiers][33]).
* **Направленность связей (Effective Connectivity, EC)**: в PD группе EC прямого пути снижена на 25 % по сравнению с контролем, а непрямого — увеличена на 30 % ([PubMed][34], [Frontiers][33]).

---

Таким образом, BGN характеризуется выраженной модульностью, small-world структурой, яркими бета- и гамма-осцилляциями, а также специфическими параметрами эффективной коннективности, которые меняются при патологии. Эти технические характеристики являются основой для количественного описания работы сети в здоровом и патологическом состояниях.

[15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11287926/ "Analyzing the topological properties of resting-state brain function ..."
[16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8957976/ "Increased Basal Ganglia Modulatory Effective Connectivity ..."
[17]: https://www.sciencedirect.com/science/article/abs/pii/S0306452224003774 "Disrupted white matter structural networks in patients with acute ..."
[18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10844151/ "a resting-state fMRI study - PMC - PubMed Central"
[19]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.582079/full "Alterations in Degree Centrality and Functional Connectivity in ..."
[20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9672501/ "Multiscale entropy and small-world network analysis in rs-fMRI"
[21]: https://www.sciencedirect.com/science/article/pii/S0010945220300307 "A graph theory study of resting-state functional connectivity in ..."
[22]: https://www.researchgate.net/figure/Clustering-coefficient-and-path-length-Explanation-of-the-clustering-coefficient-and_fig2_269466705 "Clustering coefficient and path length. Explanation of the clustering..."
[23]: https://pubmed.ncbi.nlm.nih.gov/39341271/ "Disrupted white matter structural networks in patients with acute ..."
[24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5524274/ "A review on methods in resting state connectivity analysis and ..."
[25]: https://www.sciencedirect.com/science/article/pii/S1059131120303794 "Aberrant basal ganglia-thalamo-cortical network topology in juvenile ..."
[26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5491879/ "Frequency and function in the basal ganglia: the origins of beta and ..."
[27]: https://pubmed.ncbi.nlm.nih.gov/28642341/ "Use of intraoperative local field potential spectral analysis to ..."
[28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4813758/ "Oscillations and the basal ganglia: Motor control and beyond - PMC"
[29]: https://www.nature.com/articles/s42003-022-03665-6 "Basal ganglia-cortical connectivity underlies self-regulation of brain ..."
[30]: https://www.sciencedirect.com/science/article/pii/S1053811922004190 "Contribution of the sensorimotor beta oscillations and the cortico ..."
[31]: https://pubmed.ncbi.nlm.nih.gov/32806881/ "Brain functional network alterations caused by a strong desire to ..."
[32]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1339728/full "Effective connectivity of working memory performance: a DCM study ..."
[33]: https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2022.719089/full "Increased Basal Ganglia Modulatory Effective Connectivity ..."
[34]: https://pubmed.ncbi.nlm.nih.gov/35350633/ "Increased Basal Ganglia Modulatory Effective Connectivity ..."


---


Оглавление:

- [ЭИРО framework](/README.md)
- [Нейросети мозга](/brain-networks/README.md)



