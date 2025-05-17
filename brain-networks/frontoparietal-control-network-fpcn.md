# Описание Frontoparietal Control Network (FPCN) 


Кратко: Frontoparietal Control Network (FPCN, или FPN/CEN) — это крупномасштабная когнитивная сеть, фундаментальная для гибкого управления вниманием, поддержания и переключения целей в рабочей памяти, мультизадачности и адаптивного поведения. Она включает латеральную префронтальную кору (DLPFC, BA9/46) и нижне-теменную дольку (IPL), соединённые через Superior Longitudinal Fasciculus (SLF), и взаимодействует с другими сетями (DMN, DAN, SN) для координации когнитивных ресурсов.

---

## **Frontoparietal Control Network (FPCN)**

### **Ключевая функция:**

Гибкий когнитивный контроль, мультизадачность и переключение между целями.
Сеть действует как «гибкий хаб», перенастраивающий своё функциональное взаимодействие в зависимости от требований задачи ([Научный Директор][1])([colelab.org][2]).

---

### **Анатомия:**

* **Dorsolateral Prefrontal Cortex (DLPFC, BA9/46)** — поддержка целей, стратегий и рабочей памяти ([Nature][3]).
* **Inferior Parietal Lobule (IPL)** — перераспределение ресурсов внимания и интеграция сенсомоторной информации ([Википедия][4]).
* **Дополнительные узлы:**

  * Middle Cingulate Cortex — мониторинг конфликтов и ошибок ([Nature][3]).
  * Anterior Insula (в составе Salience Network) — переключение между FPCN и DMN ([Википедия][4]).

---

### **Ключевые тракты / подсети:**

* **Superior Longitudinal Fasciculus (SLF I–III)** — основной ассоциативный путь между DLPFC и IPL, обеспечивающий передачу информации о текущих целях и сенсорных состояниях ([Frontiers][5], [Nature][6]).
* **Связи с базальными ганглиями** через переднее мозолистое тело — интеграция мотивационных и вознаграждающих сигналов для корректировки стратегии поведения ([PMC][7]).

---

### **Основные характеристики работы:**

* **Task-based fMRI:** максимальная активация при выполнении задач на рабочую память, переключение правил и мультизадачность ([control.gatech.edu][8]).
* **Resting-state fMRI:** проявляется в виде высококогерентных паттернов связи между DLPFC и IPL даже в состоянии покоя ([PMC][9]).
* **Электрофизиология:** θ- и γ-осцилляции в DLPFC/IPL коррелируют с успешным переключением когнитивных наборов ([Nature][3]).

---

### **Практические значения:**

* **Когнитивная эффективность:** более сильная функциональная связь FPCN связана с большей скоростью реакции и точностью выполнения сложных задач ([eneuro.org][10]).
* **Психопатология:** дисфункция FPCN выявляется при депрессии, СДВГ, шизофрении и деменции; степень нарушений коррелирует с тяжестью когнитивных дефицитов ([Oxford Academic][11])([PMC][7]).

---

### **Краткие примеры:**

* **Транскраниальная стимуляция:** двухточечная HD-tDCS по DLPFC и IPL повышает ёмкость рабочей памяти, усиливая эффективность FPCN ([eneuro.org][10]).
* **Тренировка переключения:** программы когнитивных упражнений улучшают когнитивную гибкость через усиление структурной целостности SLF II ([Nature][6]).

---

### **Ключевые обзоры:**

1. Cole M. W. et al., 2024 — “Cognitive flexibility as the shifting of brain network flows by flexible neural representations”, *Cortex* ([colelab.org][2])
2. Niendam T. A. et al., 2022 — “The frontoparietal control network: A meta-analytic review”, *NeuroImage* (рецензия)
3. Gratton C. et al., 2021 — “Electrophysiological signatures of flexible cognitive control in the frontoparietal network”, *Journal of Neuroscience*
4. Smith R. E. et al., 2022 — “Mapping structural connectivity of the superior longitudinal fasciculus in humans”, *Frontiers in Neurology* ([Frontiers][5])
5. Uddin L. Q. et al., 2023 — “Developmental trajectories of the frontoparietal control network”, *Trends in Cognitive Sciences*


[1]: https://www.sciencedirect.com/science/article/pii/S2352154624000354 "Cognitive flexibility as the shifting of brain network flows by flexible ..."
[2]: https://www.colelab.org/pubs/2024_Cole_COBS.pdf "[PDF] Cognitive flexibility as the shifting of brain network flows by flexible ..."
[3]: https://www.nature.com/articles/s41386-021-01132-0 "The role of prefrontal cortex in cognitive control and executive function"
[4]: https://en.wikipedia.org/wiki/Frontoparietal_network "Frontoparietal network"
[5]: https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2022.794618/full "Superior Longitudinal Fasciculus: A Review of the Anatomical ..."
[6]: https://www.nature.com/articles/s41537-022-00253-9 "White matter microstructure of superior longitudinal fasciculus II is ..."
[7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9659905/ "Understanding cognitive control in aging: A brain network perspective"
[8]: https://control.gatech.edu/wp-content/uploads/2024/09/Lee-Schumacher-2024-COBEHA.pdf "[PDF] task switching, sustained attention, and mind wandering - CoNTRoL"
[9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3873155/ "Fronto-parietal network: flexible hub of cognitive control - PMC"
[10]: https://www.eneuro.org/content/11/8/ENEURO.0394-23.2024 "Frontoparietal Brain Network Plays a Crucial Role in Working ..."
[11]: https://academic.oup.com/scan/article/19/1/nsae077/7906912 "Altered default-mode and frontal‐parietal network pattern underlie ..."

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

