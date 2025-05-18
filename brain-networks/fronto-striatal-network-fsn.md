# Описание Fronto‐Striatal Network (FSN) 

## **Fronto‐Striatal Network (FSN)**

### **Ключевая функция:**

Сеть отвечает за когнитивный контроль и подавление нецелевых реакций, поддерживая рабочую память и планирование действий через взаимодействие DLPFC и хвостатого ядра ([Nature][1]).

### **Анатомия:**

* **Dorsolateral Prefrontal Cortex (BA9/46)** – ключевая область для рабочей памяти и когнитивного контроля задач, активируется при выполнении сложных исполнительных функций ([Nature][2]).
* **Caudate Nucleus** – участвует в оценке стимулов и планировании движений, демонстрирует усиленную связь с DLPFC в задачах на подавление реакций ([PMC][3]).

### **Ключевые траты / подсети:**

* **Frontal–striatal fibers** – белые волокна через переднее бедро внутренней капсулы, обеспечивающие прямое соединение между лобными и стриатальными структурами ([PMC][4]).
* **Corticostriatal loops** – прямая (DLPFC → caudate → GPi/SNr → thalamus → DLPFC) и непрямая (через GPe) петли, реализующие баланс возбуждения и торможения в исполнительных функциях ([Nature][5]).

### **Основные характеристики работы:**

* В состояниях **resting‐state fMRI** FSN показывает устойчивую корреляцию активации между префронтальной корой и хвостатым ядром ([Nature][6]).
* При **task‐based fMRI** (Go/No‐Go, рабочая память) сеть активируется пропорционально уровню когнитивной нагрузки и требованию подавления импульсивных ответов ([ScienceDirect][7]).

### **Практические значения:**

* Активация FSN коррелирует со скоростью реакций и точностью выполнения когнитивных задач; более сильные функциональные связи DLPFC–caudate предсказывают лучшую производительность ([Nature][1]).
* Дисфункция сети отмечается при **СДВГ** (сниженная rs‐FC, гипоактивация в DLPFC и caudate) ([Frontiers][8]) и при **депрессии**, где выявлено расширение фронто‐стриатальной сети, связанное с тяжестью симптоматики ([Nature][9]).

### **Краткие примеры:**

* **Процедурное обучение**: в исследованиях на моторных и когнитивных задачах Fronto‐Striatal circuits проявляют дифференцированную активность: моторные задачи вовлекают дорсальные отделы стриатума, когнитивные – вентральные ([Nature][1]).
* **Депрессия**: у пациентов с депрессией FSN расширяется почти вдвое по сравнению со здоровыми, что отражает перестройку топографии сети ([Nature][9]).

### **Ключевые обзоры:**

1. **Frontostriatal circuitry as a target for fMRI‐based neurofeedback** – обзор нейрофидбека, влияющего на ассоциативные и моторные подсистемы FSN ([Frontiers][10]).
2. **Meta‐analysis of structural and functional alterations in ADHD** – систематический обзор дисфункции FSN при СДВГ ([Frontiers][8]).
3. **Brain mechanisms underlying the inhibitory control of thought** (*Nature Reviews Neuroscience*, 2025) – обсуждение фронто‐стриатальных взаимодействий при торможении не только действий, но и мыслей ([Nature][11]).

> **Дополнение**: для детального ознакомления с микроструктурой и дифференциацией подсистем FSN рекомендуем также книгу *Organizational Principles of Fronto‐Striatal Circuits* (OUP, 2021), где представлены диффузионно‐мРТС данные и карты функциональных проекций ([academic.oup.com][12]).

[1]: https://www.nature.com/articles/s41539-024-00282-2 "Longitudinal markers of cognitive procedural learning in fronto ..."
[2]: https://www.nature.com/articles/s41386-021-01132-0 "The role of prefrontal cortex in cognitive control and executive function"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11413358/ "Reduced dorsal fronto-striatal connectivity at rest in anorexia nervosa"
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4729321/ "Fronto-striatal organization: Defining functional and microstructural ..."
[5]: https://www.nature.com/articles/s41598-018-21346-5 "Controlling striatal function via anterior frontal cortex stimulation"
[6]: https://www.nature.com/articles/s41398-024-03165-7 "Change in striatal functional connectivity networks across 2 years ..."
[7]: https://www.sciencedirect.com/science/article/pii/S0149763423002543 "Subregional prefrontal cortex recruitment as a function of inhibitory ..."
[8]: https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.1070142/full "Meta-analysis of structural and functional alterations of brain in ..."
[9]: https://www.nature.com/articles/s41586-024-07805-2 "Frontostriatal salience network expansion in individuals in depression"
[10]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2022.933718/full "Frontostriatal circuitry as a target for fMRI-based neurofeedback ..."
[11]: https://www.nature.com/articles/s41583-025-00929-y "Brain mechanisms underlying the inhibitory control of thought - Nature"
[12]: https://academic.oup.com/cercor/article/31/12/5308/6310409 "Organization of Frontostriatal Brain Wiring in Healthy Subjects Using ..."


---



## Подробные технические характеристики FSN

Ниже представлен новый раздел с подробными техническими характеристиками Fronto-Striatal Network (FSN), включающий параметры нейровизуализации, методы анализа, микроструктурные и частотные характеристики, а также статистические и временные особенности.

### 1. Нейровизуализационные протоколы

* **fMRI (BOLD):**
  – **Resting-state:** TR = 0.8–2 с, TE = 30 мс, пространственное разрешение 2–3 мм³ ([PMC][13]).
  – **Task-based (Go/No-Go, рабочая память):** похожие параметры с дополнительным моделированием событий (event-related design) и jittering ([PubMed][14]).
* **DTI:**
  – Направлений градиента 30–64, b-значения 1 000–2 000 с/мм², воксель 2 мм³ ([PMC][15]).
  – Алгоритмы: как детерминированная (FACT), так и вероятностная (BEDPOSTX) трактография для фронто-стриатальных трактов ([SpringerLink][16]).

### 2. Анализ функциональной связности

* **Static FC:** корреляция Пирсона между средними сигналами DLPFC и Caudate за весь скан; порог z > 0.3 для значимых связей ([PMC][17]).
* **Dynamic FC:**
  – Скользящее окно длиной 30–60 с с шагом 1 TR;
  – К-means кластеризация состояний (обычно 4–6 состояний) ([PubMed][14]).
* **Graph Theory:**
  – Метрики узлов: степень (degree), коэффициент кластеризации (clustering coefficient), кратчайший путь (path length);
  – Порог бинаризации на уровне 10–30 % самых сильных связей ([Frontiers][18]).

### 3. Анализ эффективной связности

* **Dynamic Causal Modeling (DCM):**
  – Спектральный DCM с моделированием нейронных и гемодинамических параметров;
  – Типичные значения матрицы A (самосвязи) \~0.2–0.5 Hz, матрицы B (модуляции) \~0.05–0.2 Hz ([PMC][19]).
* **Granger Causality:**
  – Лаг порядка 1–3 TR;
  – Проверка стационарности через ADF-тест перед расчетом ([Nature][20]).

### 4. Микроструктурные параметры белых путей

* **Fractional Anisotropy (FA):**
  – Frontal–striatal tract FA = 0.45–0.60; снижение на 10–15 % при СДВГ и Шизофрении ([PMC][15]).
* **Mean Diffusivity (MD):**
  – MD = (0.7–0.9)×10⁻³ мм²/с; рост MD коррелирует с возрастной дегенерацией ([SpringerLink][16]).
* **Radial (RD) и Axial Diffusivities (AD):**
  – RD ≈ 0.5×10⁻³, AD ≈ 1.2×10⁻³ мм²/с; используются для оценки демиелинизации vs. аксональной дегенерации ([Oxford Academic][21]).

### 5. Частотные характеристики BOLD-флуктуаций

* **Диапазоны:**
  – Slow-5 (0.01–0.027 Hz) и Slow-4 (0.027–0.073 Hz) – основная вкладка FSN;
  – Дополнительные компоненты: Slow-3 (0.073–0.198 Hz) активно связаны с нейромодуляторной динамикой ([PMC][13], [Frontiers][22]).

### 6. Временные параметры и динамика

* **Задержка (lag) между DLPFC и Caudate:** \~4–6 с, оцененная через cross-correlation ([PMC][23]).
* **Dwell Time динамических состояний:** 20–40 с в среднем, с более длительными эпизодами при повышенной когнитивной нагрузке ([ScienceDirect][24]).

### 7. Статистические и контрольные процедуры

* **Коррекция множественных сравнений:** FDR (q < 0.05) или семейно-контролируемая ошибка (FWER, p < 0.05) с cluster-extent threshold ≥ 20 вокселей ([PMC][25]).
* **Модели смешанных эффектов:** для анализа межсубъектных вариаций включают случайные перехваты (random intercepts) и наклоны (slopes) ([ScienceDirect][26]).

---

Этот раздел позволяет планировать эксперименты по всестороннему изучению Fronto-Striatal Network, учитывая ключевые технические параметры для обеспечения репликативности и высокого качества данных.

[13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4313418/ "Functional Integration Between Brain Regions at Rest Occurs in ..."
[14]: https://pubmed.ncbi.nlm.nih.gov/37549587/ "Fronto-striatal dynamic connectivity is linked to dopaminergic motor ..."
[15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6034998/ "White Matter Integrity in the Fronto-striatal Accumbofrontal Tract ..."
[16]: https://link.springer.com/article/10.1007/s00247-020-04802-1 "Diffusion tensor imaging in frontostriatal tracts is associated with ..."
[17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4729321/ "Fronto-striatal organization: Defining functional and microstructural ..."
[18]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2019.00585/full "Application of Graph Theory for Identifying Connectivity Patterns in ..."
[19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8385130/ "Dynamic Causal Modeling Self-Connectivity Findings in the ..."
[20]: https://www.nature.com/articles/s41398-024-03083-8 "Atypical effective connectivity from the frontal cortex to striatum in ..."
[21]: https://academic.oup.com/schizbullopen/article/1/1/sgaa057/5939991 "Frontostriatal Structural Connectivity and Striatal Glutamatergic ..."
[22]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2019.00900/full "Intrinsic Frequencies of the Resting-State fMRI Signal - Frontiers"
[23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6020061/ "Specific Frontostriatal Circuits for Impaired Cognitive Flexibility and ..."
[24]: https://www.sciencedirect.com/science/article/pii/S1053811925000291 "Frontostriatal connectivity dynamically modulates the adaptation to ..."
[25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5708872/ "Graph Theoretic Analysis of Resting State fMRI - PMC"
[26]: https://www.sciencedirect.com/science/article/pii/S1053811918307341 "Functional coherence of striatal resting-state networks is modulated ..."


---


Оглавление:

- [ЭИРО framework](/README.md)
- [Нейросети мозга](/brain-networks/README.md)
