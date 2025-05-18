# Описание Cerebro-Cerebellar Cognitive Network (CCCN) 

**CCCN** представляет собой функционально значимую сеть, объединяющую ассоциативные зоны коры (префронтальная, париетальная, височная) с неомозжечком (в первую очередь лобулус Crus I/II и ядро dentate) через два основных пути (cortico-pontine-cerebellar и dentato-thalamic). Она участвует в когнитивном обучении, прогнозировании, рабочей памяти и языковых задачах, а её дисфункция связана с когнитивными нарушениями при Alzheimer’s disease, шизофрении и когнитивной дисфункции в раннем старении ([Frontiers][1], [Nature][2]).

---

## **Cerebro-Cerebellar Cognitive Network (CCCN)**

### **Ключевая функция:**

Сеть обеспечивает **когнитивное обучение и прогнозирование** путём передачи предсказаний из неомозжечка в кору, что ускоряет обучение и уменьшает ошибки при сложных задачах ([Nature][2]).
Кроме того, CCCN вовлечена в **регуляцию рабочей памяти и языковой активности** посредством петлей с префронтальной корой ([Frontiers][1], [Frontiers][3]).

---

### **Анатомия:**

* **Cerebellar Crus I/II** — участвуют в рабочей памяти, языковых и исполнительных функциях; крупные зоны когнитивных петлей ([Frontiers][1], [Frontiers][3]).
* **Anterior Lobules (I–V)** — традиционно описываются как моторные, но также вовлечены в подготовительные когнитивные процессы в задачах с моторной компонентой ([ScienceDirect][4]).
* **Dentate Nucleus** — главный выход мозжечка, отправляет предсказания и сигналы обратной связи в таламус и кору ([Frontiers][3]).

---

### **Ключевые тракты / подсети:**

* **Cortico-pontine-cerebellar fibers (PFC ↔ pons ↔ cerebellum):** основной афферентный путь, реконструированный на высоком разрешении in vivo, демонстрирует ламеллярную организацию соединений от префронтальной коры к мозжечку ([Nature][5]).
* **Dentato-thalamic tract (dentate ↔ thalamus ↔ cortex):** эферентный путь, передающий предсказания мозжечка обратно в ассоциативные зоны коры; подробно описан в обзоре «The cerebellar connectome» ([ScienceDirect][4]).

---

### **Основные характеристики работы:**

* **Resting-state fMRI:** CCCN входит в число ассоциативных resting-state сетей, активируясь в состоянии покоя рядом с ECN (Executive Control Network) и DMN ([Frontiers][1]).
* **Task-based fMRI:** при задачах на **рабочую память** (N-back, Sternberg) наблюдается синхронная активность Crus I/II и DLPFC ([ScienceDirect][6]).
* **Языковые парадигмы:** при семантических и синтаксических задачах активируется связь правого Crus I/II с Broca’s area ([PMC][7]).
* **Прогнозирование:** модель ccRNN демонстрирует, что мозжечок предоставляет временные предсказания коре для улучшения обучения как в моторных, так и в когнитивных задачах ([arXiv][8]).

---

### **Практические значения:**

* **Корреляция с поведением:** сила FC в CCCN предсказывает **скорость реакций** и **точность** в задачах на рабочую память ([ScienceDirect][6]).
* **Психопатология:**

  * **Alzheimer’s disease & MCI:** снижения FC между Crus II и париетальной корой коррелируют с ухудшением когнитивных результатов ([Frontiers][9]).
  * **Шизофрения:** дисфункция cerebro-cerebellar WM связей (MCP) ассоциируется с дефицитом исполнительных функций ([Nature][10]).
  * **Субъективный когнитивный спад (SCD):** повышенная нестабильность мозговых состояний включает ухудшенную связь CCCN ([ScienceDirect][11]).
  * **Употребление алкоголя (AUD):** изменения динамики FC в CCCN объясняют развитие и поддержание расстройств в исполнительных функциях ([Scholars @ UT Health San Antonio][12]).

---

### **Краткие примеры:**

* **Визуомоторное обучение:** reward-зависимые сигналы в неомозжечке улучшают усвоение ассоциаций «стимул-действие» ([Nature][13]).
* **Социальное познание в шизофрении:** нарушения связи Crus I/II с темпоро-париетальными областями связаны с дефицитом теории разума ([Nature][10]).

---

### **Ключевые обзоры:**

1. **Gao et al. (2023).** The cerebellum and cognitive neural networks — Frontiers in Human Neuroscience. [Читать](https://www.frontiersin.org/articles/10.3389/fnhum.2023.1197459/full) ([Frontiers][3])
2. **Guell et al. (2021).** Functional Connectivity of the Cognitive Cerebellum — Frontiers in Systems Neuroscience. [Читать](https://www.frontiersin.org/articles/10.3389/fnsys.2021.642225/full) ([Frontiers][1])
3. **Chadwick et al. (2022).** Cerebro-cerebellar networks facilitate learning through feedback predictions — Nature Communications. [Читать](https://www.nature.com/articles/s41467-022-35658-8) ([Nature][2])
4. **Wu et al. (2023).** Cognitive-Affective Functions of the Cerebellum — Journal of Neuroscience. [Читать](https://www.jneurosci.org/content/43/45/7554) ([Journal of Neuroscience][14])
5. **Zhao et al. (2025).** Multiscale gradients of corticopontine structural connectivity — Scientific Reports. [Читать](https://www.nature.com/articles/s41598-025-00886-7) ([Nature][5])



[1]: https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2021.642225/full "Functional Connectivity of the Cognitive Cerebellum - Frontiers"
[2]: https://www.nature.com/articles/s41467-022-35658-8 "Cerebro-cerebellar networks facilitate learning through feedback ..."
[3]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2023.1197459/full "The cerebellum and cognitive neural networks - Frontiers"
[4]: https://www.sciencedirect.com/science/article/pii/S0166432825000439 "The cerebellar connectome - ScienceDirect.com"
[5]: https://www.nature.com/articles/s41598-025-00886-7 "Multiscale gradients of corticopontine structural connectivity - Nature"
[6]: https://www.sciencedirect.com/science/article/abs/pii/S0166432821004745 "The resting-state cerebro-cerebellar function connectivity and ..."
[7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10006158/ "The language-related cerebro-cerebellar pathway in humans"
[8]: https://arxiv.org/abs/2110.11501 "Cortico-cerebellar networks as decoupling neural interfaces"
[9]: https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.645171/full "Differences Changes in Cerebellar Functional Connectivity Between ..."
[10]: https://www.nature.com/articles/s41537-021-00193-w "Intrinsic cerebellar functional connectivity of social cognition and ..."
[11]: https://www.sciencedirect.com/science/article/pii/S105381192400466X "Unstable functional brain states and reduced cerebro-cerebellar ..."
[12]: https://scholars.uthscsa.edu/en/publications/altered-cerebro-cerebellar-dynamic-functional-connectivity-in-alc "Altered Cerebro-Cerebellar Dynamic Functional Connectivity in ..."
[13]: https://www.nature.com/articles/s41467-024-46281-0 "A cerebro-cerebellar network for learning visuomotor associations"
[14]: https://www.jneurosci.org/content/43/45/7554 "Cognitive-Affective Functions of the Cerebellum"


---


## **Подробные технические характеристики сети CCCN**

Ниже представлены ключевые технические параметры при исследовании Cerebro-Cerebellar Cognitive Network (CCCN), включая определение узлов, сбор и предобработку данных, методы оценки связности и графовые метрики.

---

### **1. Парцелляция и определение узлов**

* **Мозжечок**  
  Используется **SUIT-atlas** для анатомической парцелляции мозжечка с разрешением \~1 mm³, включающим лобулы I–X и глубокие ядра (Dentate, Interposed, Fastigial) ([diedrichsenlab.org][15]).
* **Функциональные зоны мозжечка**  
  Парцелляция по **Buckner et al. (2011)**: 7- и 17-сетевые схемы функциональных зон неомозжечка, основанные на корреляции с 7/17 корковыми сетями Yeo et al. ([diedrichsenlab.org][16]).
* **Кора**  
  **Schaefer 2018 atlas** (n=400 ROI, 7-сеточная аннотация); каждый ROI аннотирован принадлежностью к одной из сетей (например, ECN, DMN) ([nilearn.github.io][17]).

---

### **2. Параметры сбора данных fMRI**

* **Протокол сканирования:**

  * TR: 0.8–2 с; TE: \~30 мс;
  * Пространственное разрешение: 2–3 мм³ (исходные данные resting-state ≥10 мин) ([Frontiers][18]).
* **Нормализация:**

  * Нелинейная регистрация в MNI-пространство (FNIRT);
  * Дополнительная нормализация мозжечка через SUIT DARTEL для повышения точности локализации ([diedrichsenlab.org][15]).

---

### **3. Предобработка данных**

* **Коррекция движений и slice timing:** стандартные алгоритмы SPM/CONN ([Википедия][19]).
* **Регрессия шумов:** удаление сигналов от белого вещества, ЦСЖ и параметров движения;
* **Фильтрация:** полосовой фильтр 0.01–0.1 Hz для выделения низкочастотных флуктуаций ([Frontiers][18]).

---

### **4. Оценка функциональной связности**

* **Пирсоновская корреляция:** вычисление попарных корреляций BOLD-сигналов между ROI, затем Fisher z-преобразование для нормализации распределения ([Википедия][19]).
* **Thresholding:**

  * Глобальная плотность сетки 10–20 % (с сохранением экономики связей);
  * Альтернативно z>0.2 для жёсткого порога ([Frontiers][20]).

---

### **5. Динамическая функциональная связность**

* **Метод «скользящего окна»:** окна длиной 60 с (\~30–75 сканов), шаг 1 TR, перекрытие 50 % ([Википедия][21]).
* **Анализ:** извлечение метрик изменчивости FC (variance, dwell time) для выявления «динамических состояний» CCCN.

---

### **6. Графовые метрики**

* **Основные показатели:**

  * **Степень узла (degree):** число связей каждого узла.
  * **Коэффициент кластеризации (clustering coefficient):** вероятность, что соседи узла связаны между собой.
  * **Характеристическая длина пути (path length):** среднее минимальное число рёбер между узлами.
  * **Глобальная и локальная эффективность (global/local efficiency):** обратная path length и локальная связность соответственно ([PMC][22]).
* **Small-worldness (σ):** отношение кластеризации к случайному графу при сохранении короткой path length; σ>1 свидетельствует о «small-world» архитектуре ([arXiv][23]).
* **Модулярность (Q):** выявление сообществ методом Louvain/Infomap;
* **Дополнительные метрики:** participation coefficient, betweenness centrality для оценки «узлов-мостов» между подсетями ([Frontiers][20]).

---

### **7. Статистический анализ и проверка гипотез**

* **Мульти-субъектный GLM:** групповые сравнения метрик FC/графовых показателей в CONN Toolbox с мультивариантным GLM и likelihood-ratio тестом ([Википедия][19]).
* **Коррекция множественных сравнений:** FDR p<0.05 или непараметрические кластерные методы.

---

*Раздел позволяет стандартизировать технический подход к изучению CCCN, обеспечивая воспроизводимость и сравнимость результатов между исследованиями.*

[15]: https://www.diedrichsenlab.org/imaging/suit.htm "SUIT - A spatially unbiased atlas for the cerebellum and brainstem"
[16]: https://www.diedrichsenlab.org/imaging/atlasPackage.htm "SUIT - Cerebellar Atlas Collection - Diedrichsen lab"
[17]: https://nilearn.github.io/dev/modules/description/schaefer_2018.html "Schaefer 2018 atlas - Nilearn"
[18]: https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2021.642225/full "Functional Connectivity of the Cognitive Cerebellum - Frontiers"
[19]: https://en.wikipedia.org/wiki/CONN_%28functional_connectivity_toolbox%29 "CONN (functional connectivity toolbox)"
[20]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2019.00585/full "Application of Graph Theory for Identifying Connectivity Patterns in ..."
[21]: https://en.wikipedia.org/wiki/Dynamic_functional_connectivity "Dynamic functional connectivity"
[22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11223677/ "Cerebello-Basal Ganglia Networks and Cortical Network Global ..."
[23]: https://arxiv.org/abs/1608.05665 "Small-World Brain Networks Revisited"


---


Оглавление:

- [ЭИРО framework](/README.md)
- [Нейросети мозга](/brain-networks/README.md)
