# Описание Medial Temporal Lobe Memory Network (MTL) 


MTL-сеть обеспечивает формирование, консолидацию и извлечение эпизодической (декларативной) памяти, включая интеграцию «что», «где» и «когда» информации. В её состав входят гиппокамп (CA1–CA3, DG, subiculum), энторинальная кора, парагиппокампальная и периринальная коры, которые связаны между собой белыми трактами (fornix, perforant path, cingulum bundle). Сеть активно участвует как в состоянии покоя (resting-state), так и в разнообразных задачах памяти и навигации, а её дисфункция ассоциируется с эпилепсией, шизофренией, болезнью Альцгеймера и др. ([PMC][1], [Nature][2])

## **Medial Temporal Lobe Memory Network (MTL)**

### **Ключевая функция:**

Ведущая роль в формировании, консолидации и извлечении эпизодической (декларативной) памяти, включая интеграцию пространственно-временной структуры событий ([PMC][1], [Nature][2]).

### **Анатомия:**

* **Hippocampus (CA1–CA3, Dentate Gyrus, Subiculum)** — критически необходим для кодирования и консолидации новых воспоминаний ([PMC][1]).
* **Entorhinal Cortex (EC)** — главный интерфейс между неокортексом и гиппокампом, обеспечивает входно-выходные потоки информации; латеральная EC вовлечена в сети внимания, медиальная — в память ([PMC][1], [Википедия][3]).
* **Parahippocampal и Perirhinal Cortices** — осуществляют промежуточную обработку ассоциативных связей и участвуют в кодировании контекстуальной информации ([PMC][1], [Википедия][4]).

### **Ключевые тракты / подсети:**

* **Fornix** — основной тракт, связывающий гиппокамп с мамиллярными телами и базальными ядрами; микроструктурная целостность коррелирует с точностью воспоминаний о последовательности событий ([PMC][5], [Википедия][6]).
* **Perforant Path** — проекции из энторинальной коры в зубчатую извилину (DG), ключевой путь передачи кортикальной информации в гиппокамп ([Википедия][7]).
* **Cingulum Bundle** — соединяет MTL с задней поясной корой (PCC) и медиальной префронтальной корой (mPFC), участвуя в сетях по умолчанию и контроле внимания ([PMC][1]).

### **Основные характеристики работы:**

* **Resting-state fMRI**: MTL участвует в нескольких больших сетях — default mode, dorsal attention, salience, визуальной и соматомоторной сетях ([PMC][1]).
* **Task-based fMRI**: активация при задачах распознавания, восстановления контекста, навигации и рабочих задачах памяти; субъективное качество воспроизведения контекста связано с динамикой взаимодействия между Precuneus и MTL ([Nature][8]).
* **Нейронные записи**: человеческие нейроны гиппокампа и энторинальной коры кодируют временную структуру опыта, формируя долговременные предсказательные представления ([Nature][2]).

### **Практические значения:**

* **Корреляции с поведенческими показателями**: увеличенная сложность микроструктуры форникса предсказывает более высокую точность и скорость реакций в задачах воспоминания последовательностей ([PMC][5]).
* **Клинические аспекты**:

  * **Temporal Lobe Epilepsy**: дисфункция MTL связана с антероградной амнезией и ухудшением эпизодической памяти ([PMC][1]).
  * **Болезнь Альцгеймера**: раннее поражение энторинальной и парагиппокампальной кор приводит к дефициту декларативной памяти ([PMC][1]).
  * **Шизофрения и СДВГ**: нарушения функциональной связности MTL ассоциируются с когнитивными дефектами и симптомами диссоциативного характера ([PMC][1]).

### **Краткие примеры:**

* **Работа в состоянии покоя**: data-driven ICA выявила четыре подсети MTL, каждая из которых коактивируется с уникальными крупномасштабными сетями мозга ([PMC][1]).
* **Нейронная кодировка времени**: при последовательном предъявлении образов нейроны гиппокампа и энторинальной коры постепенно отражают вероятностную структуру последовательности ([Nature][2]).
* **Генеративная модель памяти**: интеграция гиппокампальных и неокортикальных реплик при консолидации объясняет выстраивание уникальных и предсказуемых элементов воспоминаний ([Nature][9]).

### **Ключевые обзоры:**

1. Janssen N. et al., 2022 — «Medial temporal lobe contributions to resting-state networks» (Hum. Brain Mapp.) ([PMC][1])
2. Foudil S.-A. & Macaluso E., 2024 — «The influence of the precuneus on the medial temporal cortex...» (Sci. Rep.) ([Nature][8])
3. Tacikowski P. et al., 2024 — «Human hippocampal and entorhinal neurons encode the temporal structure of experience» (Nature) ([Nature][2])
4. Wu J. et al., 2023 — «A generative model of memory construction and consolidation» (Nat. Hum. Behav.) ([Nature][9])
5. Limotai C. et al., 2024 — «Long-term memory plasticity in a decade-long connectivity study» (Nat. Commun.) ([Nature][10])
6. Sun M. & Zheng Y., 2022 — «Entorhinal–DG/CA3 pathway supports memory precision» (eLife) ([eLife][11])

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8930967/ "Medial temporal lobe contributions to resting-state networks - PMC"
[2]: https://www.nature.com/articles/s41586-024-07973-1 "Human hippocampal and entorhinal neurons encode the temporal ..."
[3]: https://en.wikipedia.org/wiki/Entorhinal_cortex "Entorhinal cortex"
[4]: https://en.wikipedia.org/wiki/Parahippocampal_gyrus "Parahippocampal gyrus"
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10336598/ "A role for the fornix in temporal sequence memory - PMC"
[6]: https://en.wikipedia.org/wiki/Fornix_%28neuroanatomy%29 "Fornix (neuroanatomy)"
[7]: https://en.wikipedia.org/wiki/Mossy_fiber_%28hippocampus%29 "Mossy fiber (hippocampus)"
[8]: https://www.nature.com/articles/s41598-024-58298-y "The influence of the precuneus on the medial temporal cortex ..."
[9]: https://www.nature.com/articles/s41562-023-01799-z "A generative model of memory construction and consolidation - Nature"
[10]: https://www.nature.com/articles/s41467-024-55704-x "Long-term memory plasticity in a decade-long connectivity study ..."
[11]: https://elifesciences.org/articles/83365 "The entorhinal-DG/CA3 pathway in the medial temporal lobe retains ..."

---


## **Подробные технические характеристики сети**

### **1. Общая топология**

* **Число узлов (N):** в графе MTL-сети обычно выделяют 6–8 регионов: субполя гиппокампа (CA1–CA3, DG, Subiculum), энторинальную, периринальную и парагиппокампальную кору ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC5764800/)).
* **Число ребер (E):** при пороге корреляции r > 0.2 формируется 15–20 функциональных связей между узлами ([direct.mit.edu](https://direct.mit.edu/netn/article/8/2/377/119098/On-null-models-for-temporal-small-worldness-in)).

### **2. Ключевые графовые метрики**

* **Кластерный коэффициент (C):** 0.45–0.60, указывая на высокую локальную связность и устойчивость к локальным повреждениям ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC3037777/)).
* **Средняя длина пути (L):** 1.8–2.1 шага между любыми двумя узлами, что обеспечивает быструю интеграцию информации ([academic.oup.com](https://academic.oup.com/cercor/article/24/6/1529/296228)).
* **Small-worldness (σ):** σ = (C/C\_random)/(L/L\_random) ≈ 2.3–2.7 (>1, подтверждает «маломирную» архитектуру) ([onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/full/10.1002/brx2.70025)).
* **Глобальная эффективность (E\_glob):** \~0.65, отражает способность сети к интеграции информации на всем уровне ([epilepsybehavior.com](https://www.epilepsybehavior.com/article/S1525-5050%2813%2900617-3/fulltext)).
* **Локальная эффективность (E\_loc):** \~0.72, демонстрируя высокую устойчивость при удалении отдельных узлов ([epilepsybehavior.com](https://www.epilepsybehavior.com/article/S1525-5050%2813%2900617-3/fulltext)).
* **Модульность (Q):** \~0.35–0.40, свидетельствует о чётком разделении на функциональные модули внутри MTL-сети ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634911/)).
* **Eigenvector Centrality (EC):** наивысшая в гиппокампе (≈0.32), указывая на ключевую роль этого узла в глобальной организации сети ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634911/)).
* **Betweenness Centrality (BC):** среднее значение BC ≈0.15, отражает роль узлов-посредников в маршрутизации информации ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC10634911/)).
* **Rich-Club Coefficient (φ):** φ(k)>1 при k>3, что указывает на наличие «богатой» клювифицированной структуры узлов-«хабов» ([sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0149763416307849)).

### **3. Источники данных и методы анализа**

* **Модальности:** rs-fMRI для функциональной связности; DTI для структурных трактов (fornix, perforant path, cingulum) ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC5764800/), [nature.com](https://www.nature.com/articles/s41597-020-0364-3)).
* **Порог бинаризации:** корреляции r > 0.2–0.3 для создания бинарных графов ([direct.mit.edu](https://direct.mit.edu/netn/article/8/2/377/119098/On-null-models-for-temporal-small-worldness-in)).
* **Атлас и сегментация:** AAL-атлас для кориальных регионов, FreeSurfer для субполя гиппокампа ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC5764800/)).
* **Графовый анализ:** инструменты Brain Connectivity Toolbox и NetworkX для вычисления метрик ([epilepsybehavior.com](https://www.epilepsybehavior.com/article/S1525-5050%2813%2900617-3/fulltext)).

### **4. Временные характеристики**

* **Динамическая функциональная связность:** окна длительностью 30–60 с со скольжением 1–2 с для отслеживания изменений топологии во времени ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0960982219301599)).
* **Частотные диапазоны:** тета- (4–8 Гц) и гамма-диапазоны (30–80 Гц) для фазовой синхронизации и кодирования последовательности событий ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0960982219301599)).

### **5. Вычислительные ресурсы**

* **Оборудование:** кластеры HPC или многопроцессорные станции с 64+ ГБ ОЗУ.
* **Время вычислений:** \~2–4 часа на одну сессию rs-fMRI (200 временных точек) при расчёте всех метрик.

> Данная секция позволяет исследователям быстро ознакомиться с точными параметрами построения и анализа MTL-сети, что облегчает воспроизводимость и сопоставимость результатов.




---


Оглавление:

- [ЭИРО framework](/README.md)
- [Нейросети мозга](/brain-networks/README.md)



