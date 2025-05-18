# Описание Hippocampal-Neocortical Memory Network (HNMN)  

HNMN отвечает за консолидацию эпизодических воспоминаний: постепенный перенос и «перепрошивку» следов памяти из гиппокампа в неокортекс. Эта сеть объединяет быстрый кодирующий потенциал полей CA и зубчатой извилины гиппокампа с медленными, но устойчивыми изменениями в неокортексе (PMC, mPFC, PCC), обеспечивая долговременное хранение информации через синаптическую и системную консолидацию.

## **Ключевая функция:**

Консолидация длиносрочной памяти путём перекачки эпизодической информации из гиппокампа в неокортекс.
Системная консолидация позволяет воспоминаниям со временем стать независимыми от гиппокампа и храниться главным образом в коре головного мозга ([Научные документы][1]). Во сне синхронные колебания в диапазоне δ–σ–θ поддерживают обмен информацией между HC и корой для укрепления синаптических следов ([Cell][2]).

## **Анатомия:**

* **Гиппокамп (CA1–CA3, DG):**
  Отвечает за быстрое кодирование и «реплей» недавно приобретённых воспоминаний. Поля CA3 и DG играют ключевую роль в разделении схожих паттернов (pattern separation) и их последующем объединении ([Nature][3]).
* **Энторинальная кора (EC):**
  Интерфейс между неокортексом и гиппокампом, осуществляющий сбор и передислокацию информации. EC–HC связь представлена как классическая глутаматергическая, а также содержат GABA-эргические проекции ([PMC][4]).
* **Медиальная PFC (mPFC) и задняя поясная кора (PCC):**
  Активируются на поздних стадиях системной консолидации, когда следы памяти уже переносится в ассоциативные области коры. Эти области участвуют в долгосрочном хранении и извлечении контекстуальных воспоминаний ([Nature][5]) и дополнительно поддерживаются во время кодирования естественных событий ([doi.org][6]).

## **Ключевые тракты / подсети:**

* **Перфорантный путь (entorhinal → DG → CA3):**
  Главный путь поступления информации в зубчатую извилину и CA3, служит для initial encoding и последующего replay ([Научные документы][1]).
* **Цингулум (cingulum bundle):**
  Белый тракт, соединяющий гиппокамп и медиа­леные структуры PFC/PCC, обеспечивает bidirectional flow и синхронизацию активности между ними ([Nature][7]).

## **Основные характеристики работы:**

* **Активность при кодировании и извлечении:**
  Во время задач на различение схожих воспоминаний усиливаются θ-колебания (4–5 Гц) в HC–неокортикальных связях, способствуя точному воспроизведению деталей ([doi.org][8]).
* **Resting-state сети:**
  Даже в состоянии покоя межузловые корреляции между HC и PMC/mPFC отражают «предвосхищающее» обеспечение консолидации и предиктивную обработку информации ([Nature][9]).

## **Практические значения:**

* **Корреляция с производительностью:**
  Во время микро-оффлайн интервалов (короткие паузы между сессиями обучения) replay в HC и коре прогнозирует улучшение точности и скорости формирования навыков ([doi.org][10]).
* **Клинические аспекты:**
  — Нарушения синхронизации HC–кортикальных ритмов связаны с амнезией при ранней стадии болезни Альцгеймера. Мягкая стимулация во сне синхронизированно с hippo-δ-ритмом улучшает память распознавания у пациентов с эпилепсией и потенциально может быть применена при Альцгеймере и PTSD ([Nature][7], [WIRED][11]).
  — Нарушения EC–HC связи отмечаются при шизофрении и СДВГ, что приводит к дефицитам в рабочей и автобиографической памяти ([Научные документы][12]).

## **Краткие примеры:**

* **Theta-mediated dynamics:**
  Человеческие внутричерепные записи показали, что фаза 4–5 Гц θ-ритма интегрирует HC и кору при формировании и точном воспроизведении воспоминаний ([Nature][3]).
* **Сон и память:**
  Точная стимуляция во сне, синхронизированная с hippocampo–thalamocortical ритмами, напрямую улучшает консолидированную память на визуальные образы ([Nature][7]).

## **Ключевые обзоры:**

1. **Eichenbaum, 2017** — «Memory consolidation and hippocampal–neocortical interactions», *Trends in Cognitive Sciences*.
2. **Squire & Alvarez, 1995** — «Retrograde amnesia and memory consolidation», *Science*.
3. **Schmidt et al., 2024** — «Coupled sleep rhythms for memory consolidation», *Trends in Cognitive Sciences* ([Cell][2]).
4. **Lee & Frank, 2024** — «Memory consolidation from a reinforcement learning perspective», *Frontiers in Computational Neuroscience* ([Frontiers][13]).

[1]: https://www.sciencedirect.com/topics/psychology/systems-consolidation "Systems Consolidation - an overview | ScienceDirect Topics"
[2]: https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613%2824%2900029-9 "Coupled sleep rhythms for memory consolidation - Cell Press"
[3]: https://www.nature.com/articles/s41467-023-44011-6 "Theta mediated dynamics of human hippocampal-neocortical ..."
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11449717/ "Entorhinal cortex–hippocampal circuit connectivity in health and ..."
[5]: https://www.nature.com/articles/s41593-022-01223-1 "Neocortical synaptic engrams for remote contextual memories - Nature"
[6]: https://doi.org/10.1016/j.neuron.2023.10.010 "Hippocampal-cortical interactions during event boundaries support ..."
[7]: https://www.nature.com/articles/s41593-023-01324-5 "Augmenting hippocampal–prefrontal neuronal synchrony during ..."
[8]: https://doi.org/10.1038/s41467-023-44011-6 "Theta mediated dynamics of human hippocampal-neocortical ..."
[9]: https://www.nature.com/articles/s41467-022-29208-5 "Acquiring new memories in neocortex of hippocampal-lesioned mice"
[10]: https://doi.org/10.1016/j.celrep.2021.109193 "Report Consolidation of human skill linked to waking hippocampo ..."
[11]: https://www.wired.com/story/brain-stimulation-improves-memory-sleep "Gentle Brain Stimulation Can Improve Memory During Sleep"
[12]: https://www.sciencedirect.com/science/article/pii/S0896627323002015 "Review Sleep—A brain-state serving systems memory consolidation"
[13]: https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2024.1538741/full "Memory consolidation from a reinforcement learning perspective"


---


## Подробные технические характеристики сети HNMN

### 1. Временные параметры

* **Задержки проведения (Conduction delays):** варьируются от 0.2 до 10 мс в зависимости от длины аксона и диаметра волокна между гиппокампом и неокортексом ([pnas.org](https://www.pnas.org/doi/10.1073/pnas.192233099)).
* **Синаптические временные постоянные (Synaptic time constants):** для возбуждающих синапсов τ\_τ ≈ 1.7 мс при 35 °C ([jneurosci.org](https://www.jneurosci.org/content/17/20/7606)); для ингибирующих τ\_syn ≈ 5 мс ([biorxiv.org](https://www.biorxiv.org/content/10.1101/864231v1.full-text)); AMPA-рецепторы показывают время деактивации \~1.3 мс и десенситизации \~4.5 мс ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S0896627300803396)).
* **Окно STDP (Spike-Timing Dependent Plasticity):** расширение в пределах \~±20 мс, обеспечивающее укрепление или ослабление синапсов в зависимости от порядка спайков ([en.wikipedia.org](https://en.wikipedia.org/wiki/Spike-timing-dependent_plasticity)).

### 2. Синаптические характеристики

* **Пиковая проводимость (Peak conductance):** типичные значения в модели CA1 — 1–5 нС для AMPA и 0.5–2 нС для NMDA-синапсов ([onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/full/10.1002/hipo.23220)).
* **Коэффициент релизной вероятности:** 0.2–0.5, влияющий на достоверность передачи спайков между HC и неокортексом ([onlinelibrary.wiley.com](https://onlinelibrary.wiley.com/doi/full/10.1002/hipo.23220)).

### 3. Топологические метрики (Graph Metrics)

* **Мера small-worldness (s):** s > 1 указывает на маломировую организацию, способствующую балансу локальной кластеризации и короткому среднему пути ([sciencedirect.com](https://www.sciencedirect.com/science/article/pii/S1053811923003117)).
* **Коэффициент кластеризации (C):** C ≈ 0.3–0.5, значительно выше, чем в эквивалентных случайных графах ([researchgate.net](https://www.researchgate.net/publication/6716200_Small-World_Brain_Networks)).
* **Характеристическая длина пути (L):** L \~ 2–3 шага, обеспечивая быстрое интегрированное взаимодействие между узлами сети ([en.wikipedia.org](https://en.wikipedia.org/wiki/Small-world_network)).
* **Глобальная эффективность (E):** E \~ 0.4–0.6, отражающая способность сети эффективно передавать информацию на макроскопическом уровне ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6674299/)).

### 4. Модулярность и сообщество (Modularity)

* **Индекс модулярности (Q):** Q > 0.3–0.5 свидетельствует о выраженной модульной структуре, где корковые и гиппокампальные узлы образуют устойчивые сообщества ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC2733312/)).
* **Алгоритм детекции сообществ:** чаще всего применяется метод Louvain для оптимизации Q со средней вариативностью < 0.05 при повторных запусках ([en.wikipedia.org](https://en.wikipedia.org/wiki/Louvain_method)).

### 5. Совместимость с fMRI BOLD

* **Корреляция HC–PMC/mPFC:** коэффициенты корреляции r = 0.4–0.7 в состоянии покоя и во время задач на память ([biorxiv.org](https://www.biorxiv.org/content/10.1101/864231v1.full-text), [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9166555/)).
* **Частотные диапазоны BOLD:** основная мощность на 0.01–0.1 Гц, согласованная с δ–θ ритмами гиппокампа ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6674299/)).

*Раздел представляет собой совокупность измеримых параметров и графово-теоретических метрик, описывающих техническую организацию HNMN и её физические ограничения.*



---


Оглавление:

- [ЭИРО framework](/README.md)
- [Нейросети мозга](/brain-networks/README.md)


