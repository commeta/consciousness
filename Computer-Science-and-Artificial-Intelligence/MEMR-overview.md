# MEMR — Обзор мемристоров, вычислений в памяти и нейроморфных систем для LLM/ML

**Полный технический доскональный обзор (рабочая версия v1.0)**
*Обновлено: 12 октября 2025 г.*

**Анонс (кратко)**
Исчерпывающий инженерно-научный обзор по мемристорам, вычислениям в памяти (Compute-in-Memory / AIMC) и нейроморфным платформам в контексте современных задач машинного обучения, включая применение к большим языковым моделям (LLM). Документ объединяет устройство→схема→архитектура→алгоритмы→стек инструментов→производство→безопасность→коммерческие аспекты и содержит практические чек-листы, шаблоны и глоссарий. Этот материал рассчитан на инженеров аппаратного обеспечения, исследователей материалов, архитекторoв систем, ML-инженеров и тех, кто готовит вывод прототипов в производство или валидацию.

**Ключевые особенности документа**

* Полный стек: от физики мемристоров до deployment и TCO-оценок.
* Практические разделы: mapping, calibration, runtime telemetry, CI/CD для AIMC.
* Методики измерений: как честно мерить E/MAC, latency, throughput, endurance и репортить результаты.
* Безопасность и регуляция: threat models, fault injection, требования для BCI/медтеха.
* Шаблоны и артефакты: mapping_table.json, device_preset.json, publication checklist (готовые к использованию).
* Большой расширенный глоссарий и сборник авторитетных источников (до 2025 г.).

**Кому полезно**

* Аппаратным инженерам и разработчикам ASIC/SoC, планирующим AIMC-проекты;
* ML-исследователям, которые хотят переносить слои трансформера на analog-accelerators;
* R&D-командам стартапов и предприятиям, оценивающим FTO и экономику производства;
* Регуляторным и медицинским специалистам, интересующимся BCI и safety-certification.


---


## 1. Введение — цели обзора, границы, критерии оценки

Ниже — развёрнутый, практический вводный раздел для всестороннего обзора мемристорных / нейроморфных технологий в контексте LLM/ML. Цель — однозначно задать, **что** рассматривается, **почему** это важно и **как** мы будем оценивать результаты (метрики и протоколы). Все утверждения опираются на авторитетные обзоры и системные демонстрации (см. цитаты в тексте).

---

### 1.1. Цели и объект обзора (что именно покрываем)

**Основная цель обзора.**
Свести воедино и критически оценить текущее состояние технологий memristor / analog in-memory computing (AIMC) и нейроморфных подходов с фокусом на их применимость к современным задачам ML — в частности к инференсу и обучению больших языковых моделей (LLM), а также к смежным приложениям (edge-LLM, робототехника, BCI, медтех). Обзор должен дать инженер-ориентированные выводы: какие слои модели выгодно переносить на AIMC, какие ограничения остаются, и какие метрики/протоколы нужны для честного сравнения с цифровыми системами. ([Nature][1])

**Границы (scope).**

* *Включено:* устройство → схемотехника → массивы (tiles) → архитектура чипа → toolchain/компилеры → система/развёртывание. Особое внимание — измеримым показателям: energy/MAC, latency, throughput, area, accuracy/quality (task-specific), жизненному циклу (endurance, retention). ([Nature][1])
* *Исключено (за пределами обзора):* глубинная фармакология материалов, коммерческие NDA-конфиденциальные спецификации производителей (если не опубликованы), подробно-юридические аспекты лицензирования (обозревательно — да, но без юрконсультирования).

**Инференс vs training; edge vs datacenter (практическая классификация).**

* *Inference (инференс):* статическая карта весов, большое число VMM/MAС с относительно редкими программированиями → AIMC часто даёт ощутимые выигрыши за счёт близкой к памяти обработке. Иллюстрация: system-demo Ambrogio et al. демонстрирует system-level energy/throughput для инференса на PCM-чипе. ([Nature][2])
* *Training (обучение / on-chip finetune):* требует частых программирований (writes) → вопрос endurance / write-energy критичен; алгоритмы low-write (LoRA/low-rank adapters) и аппаратные методы in-situ обучения находятся в фокусе исследований (Rasch 2024 и др.). ([Nature][3])
* *Edge vs datacenter:* AIMC выигрывает там, где критичны энергия/латентность и/или приватность (edge), но системная периферия (ADC/DAC, interconnect) и amortization (batch size, concurrency) могут сильно влиять на реальную выгоду в дата-центрах — поэтому нужно system-level сравнение (см. секции далее). ([Nature][2])

---

### 1.2. Критерии оценки (метрики — чёткие определения и как измерять)

Ниже — набор **обязательных** метрик, которыми должен оперировать любой честный технический отчёт по AIMC. После каждой метрики — краткое определение и примечание по измерению / отчётности.

1. **Energy per MAC (E_MAC)**

   * **Определение:** суммарная энергия, затраченная системой на одно умножение-аккумуляцию в реальном режиме (включая аналоговое ядро, ADC/DAC, цифровую аккумулацию и межблоковую передачу).
   * **Почему важно:** одиночная оценка «core fJ/MAC» вводит в заблуждение, если не показать decomposition; system-level breakdown обязателен. Практически: измерять E_total для заданного workload и делить на число выполненных MACs, одновременно публикуя деталировку (E_core, E_ADC, E_DAC, E_interconnect, E_program). (Рекомендация основана на системных демонстрациях и обзорах.) ([Nature][2])

2. **Latency (p50/p95/p99) и Throughput**

   * **Определение:** латентность ответа (мс/секунды) и пропускная способность (inferences/sec или tokens/sec) при указанном batch-size и concurrency. Обязательно указывать p95/p99 для приложения с реальными SLA. ([Nature][2])

3. **Area (mm²) и плотность параметров (параметры/мм²)**

   * Показывает аппаратную компактность; важна при сравнении с GPU/TPU (учитывайте packaging/3D-stacking). ([Nature][2])

4. **Accuracy / Quality (task-specific)**

   * Для LLM и NLP: perplexity, BLEU/ROUGE, GLUE / SST-2 / task-specific metrics. Для vision/audio — top-1/top-5, WER для ASR и т.д. Всегда приводить *baseline* (FP32) и *mapped* (после programming+calibration) значения, а также stability (accuracy(t) series). ([Nature][2])

5. **Жизненный цикл устройства: Endurance и Retention**

   * **Endurance:** число program/erase циклов до degradation (например, 50% failure threshold) — критично для on-chip training.
   * **Retention:** время, в течение которого conductance остаётся в допустимом окне (или Arrhenius-экстраполяция). Рекомендуется приводить accelerated tests и методику экстраполяции. Rasch et al. отдельно исследуют, какие device-параметры приемлемы для robust in-memory training. ([Nature][3])

6. **Variability / Drift / Noise**

   * Статистика D2D (device-to-device), C2C (cycle-to-cycle) σ; drift как %-изменение conductance на log-time scale. Эти характеристики напрямую влияют на SNR, требующие replication / calibration / HW-aware training. ([Nature][1])

7. **Program / Verify overhead (latency & energy)**

   * Для training: средняя энергия и время одного обновления веса (program+verify); для fine-tune — суммарное количество программирований на эпоху. Публикации по in-situ training обязаны это репортить. ([Nature][3])

**Как представлять метрики в отчёте (reproducibility rules of thumb):**

* Всегда публикуйте *разложение энергии* (E_core, E_ADC, E_DAC, E_interconnect, E_periphery, E_program).
* Указывайте условия измерения: batch size, concurrency, ambient temperature, supply voltages, ADC ENOB, mapping_table.
* Публикуйте raw traces (power, program/verify logs) и HWA configs (AIHWKit/MemTorch)—чтобы другие могли эмулировать ваш эксперимент. ([IBM Analog Hardware Acceleration Kit][4])

---

### 1.3. Уровни анализа (device → system) — что анализируется на каждом уровне и какие вопросы задавать

Для воспроизводимого и полезного обзора нужно рассматривать всю цепочку — от материала до системы. Ниже — декомпозиция ролей каждого уровня, типичных вопросов и рекомендуемых инструментов/методов анализа.

#### Уровень A. **Устройство (device / material)**

* **Что:** материалный стек (HfOx, TiO₂, GST/PCM, CBRAM, FeFET и др.), селектор, структура ячейки.
* **Вопросы:** endurance, retention, ΔG per pulse, switching physics, BEOL-совместимость.
* **Инструменты:** SPICE / Verilog-A compact models, device characterization benches (IV, pulse sweeps, Arrhenius tests). (Литературная отправная точка — Sebastian et al. обзор по device → system.) ([Nature][1])

#### Уровень B. **Схемотехника (circuit)**

* **Что:** топология ячеек (1T1R vs passive crossbar), селекторы, sense-amps, drivers, low-power ADC/DAC архитектуры.
* **Вопросы:** sneak-path mitigation, shared-ADC amortization, ADC latency/ENOB tradeoffs, IR-drop, thermal effects.
* **Инструменты:** circuit-level SPICE, mixed-signal simulations, prototype silicon measurement (см. Ambrogio 2023). ([Nature][2])

#### Уровень C. **Массив / tile (array)**

* **Что:** физический массив crossbar, per-tile calibration, per-tile telemetry.
* **Вопросы:** mapping of matrices → tiles, per-tile compensation, redundancy, effective yield.
* **Инструменты:** CrossSim / array-level simulators, array calibration procedures; AIHWKit device-presets для эмуляции. ([IBM Analog Hardware Acceleration Kit][4])

#### Уровень D. **Архитектура чипа (chip/system on chip)**

* **Что:** bank/tile organization, on-chip interconnect, 3D stacking, thermal management, runtime policies.
* **Вопросы:** bank scheduling (MoE activations), inter-tile comms cost, system-level E/MAC, area/packaging. IBM/Analog-MoE и Ambrogio демонстрируют system-level trade-offs и real-world измерения. ([IBM Research][5])

#### Уровень E. **Софтстек / toolchain (compiler, mapping, HWA training)**

* **Что:** mapping tools, HWA-trainers (AIHWKit, AIHWKit-Lightning), quantization, LoRA/adapter workflows.
* **Вопросы:** как map'ятся матрицы, каким образом учитывается noise/variability в тренировке, runtime loader/firmware. Рекомендуется использовать AIHWKit/AIHWKit-Lightning для воспроизводимых HWA-экспериментов. ([IBM Analog Hardware Acceleration Kit][4])

#### Уровень F. **Система / deployment (edge / datacenter)**

* **Что:** runtime, telemetry, monitoring, maintenance (refresh, recalibration), TCO (CAPEX/OPEX).
* **Вопросы:** где AIMC действительно экономит (energy/token), какие SLA-гарантии возможны, как выглядят сценарии отказа (failover → digital fallback). System-level reporting обязательно должен включать runtime logs и TCO-модели. ([Nature][2])

---

### Короткая дорожная карта использования введённого фреймворка

1. **При чтении/оценке публикации — проверить:** указаны ли все основные метрики (E_MAC breakdown, latency p95/p99, mapped vs baseline accuracy, endurance/retention protocol), опубликованы ли mapping/cali/HWA config. Если нет — считайте отчёт неполным. ([Nature][2])
2. **При проектировании эксперимента:** начинайте с device-audit (ΔG stats, endurance), затем HWA-retrain (AIHWKit), array-sweep (CrossSim), и только затем system-level prototype / TCO analysis (IBM style). ([Nature][1])

---

### Основные источники, которые лежат в основе этого раздела (must-read)

* A. Sebastian, M. Le Gallo, R. Khaddam-Aljameh, E. Eleftheriou, *Memory devices and applications for in-memory computing*, **Nature Nanotechnology**, 2020 — фундаментальный обзор device→system. ([Nature][1])
* S. Ambrogio et al., *An analog-AI chip for energy-efficient speech recognition and transcription*, **Nature**, 2023 — system-level prototype (PCM, 35M devices) с полным energy/throughput разложением. ([Nature][2])
* M. J. Rasch et al., *Fast and robust analog in-memory deep neural network training*, **Nature Communications**, 2024 — алгоритмические ограничения и требования к device-параметрам для практичного in-memory training. ([Nature][3])
* IBM Analog Hardware Acceleration Kit (AIHWKit) — документация и репозиторий (инструмент для hardware-aware training, mapping и эмуляции). ([IBM Analog Hardware Acceleration Kit][4])
* J. Büchel et al., *Efficient scaling of large language models with Mixture of Experts and 3D analog in-memory computing*, **Nat. Comput. Sci.**, 2025 — roadmap/архитектурные соображения для LLM на 3D-AIMC. ([IBM Research][5])

---


<details>
<summary>Детали</summary>

A) подготовить **краткий шаблон для экспериментального отчёта** (CSV/Markdown) с обязательными полями (E_breakdown, latency_stats, mapping_table, device_preset, program_logs), или
B) сгенерировать **пример HWA-config + mapping_table.json** для типичного transformer-слоя (dense 4096×4096 → tiles 256×256) и показать пример расчёта E_MAC с учётом ADC amortization (включая численные примеры), или

</details>

[1]: https://www.nature.com/articles/s41565-020-0655-z "Memory devices and applications for in-memory computing"
[2]: https://www.nature.com/articles/s41586-023-06337-5 "An analog-AI chip for energy-efficient speech recognition ..."
[3]: https://www.nature.com/articles/s41467-024-51221-z "Fast and robust analog in-memory deep neural network ..."
[4]: https://aihwkit.readthedocs.io/ "IBM Analog Hardware Acceleration Kit's documentation!"
[5]: https://research.ibm.com/publications/efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog-in-memory-computing "Efficient Scaling of Large Language Models with Mixture ..."


---


**2. Исторические основы и теория мемристора** подробно по пунктам 2.1–2.3. Я использовал только авторитетные академические источники (классика + важные обзорные и критические работы до 2024/2025). В тексте — чёткие формулы, технич. пояснения и выводы, которые пригодятся в дальнейшем при сопоставлении с реальными memristive устройствами и их применением в AIMC/нейроморфике.



## 2. Исторические основы и теория мемристора 

### 2.1. Определение и математическая классика (Chua 1971) — формулировка элемента

**Коротко:**	memristor был введён Леоном Чуа как *математически определённый* четвёртый пассивный элемент электрических цепей, дополняющий резистор, конденсатор и индуктор. Идея — в наличии *связи между зарядом (q) и магнитным потоком ( $\varphi$ )*, что в предельном виде приводит к зависимости мгновенного сопротивления от прошедшего через устройство заряда.

**Формула (классическое представление Чуа):**
Чуа ввёл понятие мемристанса (M) через соотношение между напряжением ( $v(t)$ ) и током ( $i(t)$ ) с учётом истории:

$v(t) ;=; M(q(t)); i(t), \qquad q(t)=\int_{-\infty}^{t} i(\tau),d\tau, \qquad M(q) ;=; \frac{d\varphi}{dq}.$

То есть мемристанс (M) — функция от накопленного заряда, и в общем случае напряжение зависит не только от текущего тока, но и от «памяти» заряда (истории). Чуа также показал, что график (i)-(v) идеального мемристора при переменном возбуждении имеет *pinched hysteresis loop* (замкнутую петлю, проходящую через ноль) — это важная «печать» мемристивного поведения в моделях. ([cpmt.org][6])

**Комментарий по идеальности:**
Чуа дал математическое определение — *идеальный* мемристор (его мемристанс зависит исключительно от накопленного заряда). Однако в физике много устройств имеют «память» вследствие внутренних состояний (ионное распределение, фазовые переходы и т.п.), и их поведение часто описывают как *memristive systems* (широкая класс-модель), а не как строгие идеальные мемристоры. См. раздел 2.3. ([ScienceDirect][7])

---

### 2.2. Экспериментальные реализации и «открытие» в нано-системах (Strukov et al., 2008)

**Коротко:**	Струков и соавторы (HP) в 2008 показали, что в наноструктурах с ионно-электронной транспортной физикой (на примере TiO₂) можно наблюдать поведение, которое хорошо описывается зависимостью сопротивления от истории протекшего тока — и интерпретировали это как «реализацию» идеи Чуа в реальном материале. Эта работа стала мощным катализатором бурного роста исследований memristive устройств и их применений (ReRAM/oxide RRAM, CBRAM, PCM и т.д.). ([web.ece.ucsb.edu][8])

**Физический механизм (кратко):**

* В типичной реализации (оксидные структуры) изменение сопротивления связано с миграцией вакансий/ионов (например, кислородных вакансий в TiO₂) и образованием/разрушением проводящих «нитей» (filaments).
* Поскольку распределение дефектов/ионов зависит от предшествующих электрических воздействий (напряжений/токов), итоговое сопротивление «запоминает» историю стимулов. Это даёт нелинейную, гистерезисную I–V-характеристику, часто демонстрирующую «pinched hysteresis loop», похожую на предсказание Чуа, но в общем случае с дополнительными внутренними состояниями и эффективными источниками (см. ниже). ([web.ece.ucsb.edu][8])

**Практическое значение:**
Струков и соавторы продемонстрировали, что мемристивное поведение — не просто математическая абстракция, а естественное следствие электрохимии и ионной кинетики в наноструктурах. Это открытие привело к интенсивной разработке устройств ReRAM/CBRAM/PCM для памяти и для in-memory вычислений. Однако уже в первых последующих дискуссиях стало ясно: «поведение с памятью» далеко не всегда тождественно *идеальному* мемристору Чуа — об этом дальше. ([web.ece.ucsb.edu][8])

---

### 2.3. Дальнейшие дискуссии о терминологии и классификации (когда устройство считать memristor’ом)

После 2008–2013 сформировалось несколько важных потоков работы и критики, которые сейчас определяют терминологию и практику:

**(A) Обобщение: memristive systems / memory materials**
М. Di Ventra и Y. Pershin и др. предложили *широкую классификацию* «memory materials/systems», показав, что многие реальные устройства (RRAM, PCM, MTJ и т.п.) ведут себя как комбинация элементов с памятью (memristors, memcapacitors, meminductors) — то есть нужно работать с общей математикой «memristive systems», где состояние устройства описывается вектором внутренних переменных ( $\mathbf{x}$ ) и уравнениями:

$$\begin{cases} i(t) = G(\mathbf{x},v,t),v(t),[2pt] \dot{\mathbf{x}} = f(\mathbf{x},v,t), \end{cases}$$

а не только (M(q)). Это упростило физическое описание и позволило корректно моделировать реальные устройства с несколькими внутренними степенями свободы. ([ScienceDirect][7])

**(B) Критика «идеальности»: аргументы против тождества реальных устройств идеальному мемристору**
Серьёзные критические работы поставили под сомнение утверждение «всё, что имеет hysteresis — это memristor Чуа»:

* *Valov et al., 2013 (Nature Communications)* показали, что в редокс-основанных (nanoionic) резистивных переключателях присутствуют эффекты «нанобатареек» (локальные электрохимические потенциалы), которые добавляют к модели поведения элементы, не укладывающиеся в простую идею (M(q)); требуется расширение теории memristor-типа для корректного описания таких эффектов. Это важно, потому что электрохимия и поляризация в реальных устройств вносят вклад, который меняет динамику и термодинамические соображения. ([Nature][9])

* *Pershin & Di Ventra (2018/2019)* предложили *экспериментальную проверку* (тест) для выявления **идеального** мемристора (чтобы отличать устройства, чья сопротивляемость зависит *только* от накопленного заряда, от устройств с другими внутренними состояниями). Тест дал чёткую методику: в цепи конденсатор-мемристор при возвращении заряда конденсатора к начальному знаку, идеальный мемристор обязан вернуться в исходное состояние. Это важный инструмент верификации. ([arXiv][10])

* *Kim et al., 2019/2020 (Advanced Electronic Materials / arXiv)* экспериментально применили подобный тест к распространённым resistance-switching ячейкам (Cu-SiO₂, electrochemical metallization cells) и продемонстрировали, что эти физические элементы **не** проходят тест для идеального мемристора — следовательно, они не являются мемристорами в строгом математическом смысле Чуа. Авторы сформулировали и две «impossibility conjectures» о невозможности точного представления реальных switching-устройств как идеальных мемристоров. ([arXiv][11])

**(C) Философско-теоретическая критика: можно ли считать мемристор «четвёртым фундаментальным пассивным элементом»?**

* Работы Vongehr (2015) и Abraham (2018) подробно обсуждали, что «идеальный» мемристор как фундаментальный новый пассивный элемент либо не реализуем (с точки зрения электромагнитной физики, требующей магнитной составляющей), либо его «фундаментальность» проблематична. Abraham 2018 аргументировал, что в электротехнике фундаментальные пассивные элементы — это три, а устройства, демонстрирующие память, должны рассматриваться как сложные много-входные/много-состояные системы, часто с активной компонентой в модели. Эти критические работы важны, потому что они заставляют чётко различать: *математическая дефиниция* (Чуа) vs *практическая классификация физических устройств*. ([Nature][12])

**(D) Итог для практиков (консенсус):**

* Большинство исследователей для практических задач используют **понятие memristive/memristive systems** (обобщённая модель с внутренними переменными) и уходят от строгой идентичности с идеальным Чуа-мемристором. Для приложений (ReRAM, AIMC) гораздо важнее корректно смоделировать реальные физические процессы (ионная кинетика, электрохимия, drift/diffusion, термика) и измерить параметры (endurance, retention, drift, write energy), чем демонстрировать соответствие строгому математическому определению 1971 г. Это не отменяет ценности математической постановки Чуа (она остаётся удобной теоретической опорой), но уточняет её предел применимости. ([ScienceDirect][7])

---

## Заключение раздела 2 — что важно запомнить для дальнейших глав обзора

1. **Чуа (1971)** дал строгое математическое определение идеального мемристора; формула (v = M(q), i) и «pinched hysteresis» — ключевые отличительные признаки в теории. ([cpmt.org][6])
2. **Strukov et al. (2008)** продемонстрировали, что мемристивное поведение естественно возникает в наноструктурах с ионной кинетикой (TiO₂ и т.п.), что породило волну исследований устройств с памятью. ([web.ece.ucsb.edu][8])
3. **Реальность сложнее идеала.** Начиная ~2011–2019 сформировался консенсус: реальные resistive-switching устройства — это *memristive systems* с множеством внутренних состояний, электрохимическими эффектами (nanobatteries), drift/diffusion, и иногда активными элементами в поведении; некоторые эксперименты и теоретические работы (Pershin & Di Ventra, Kim et al., Valov et al.) прямо показывают, что считать все такие устройства «идеальными мемристорами Чуа» некорректно. ([ScienceDirect][7])

**Практическая рекомендация для инженера AIMC / нейроморфика:** при создании моделей и при переносе нейросетевых алгоритмов на memristor-hardware опирайтесь на *конкретные физические модели устройства и измеренные параметры* (program/verify time, variability, write energy, retention, drift), а не на упрощённое математическое представление (M(q)). Совместное (device ↔ circuit ↔ algorithm) моделирование — обязательный путь. ([knowen-production.s3.amazonaws.com][13])

---

## Основные использованные источники (рекомендуется к прочтению)

* **Chua L. O.** *Memristor — The Missing Circuit Element.* IEEE Trans. Circuit Theory (1971). — классическая математическая постановка memristor’а. ([cpmt.org][6])
* **Strukov D.B., Snider G.S., Stewart D.R., Williams R.S.** *The missing memristor found.* Nature (2008). — ключевая экспериментальная демонстрация в наноструктурах (TiO₂). ([web.ece.ucsb.edu][8])
* **Di Ventra M., Pershin Y.V.** *Memory materials: a unifying description.* Materials Today (2011). — обзор-обобщение про memory materials / memristive systems. ([ScienceDirect][7])
* **Valov I. et al.** *Nanobatteries in redox-based resistive switches require extension of memristor theory.* Nature Communications (2013). — важная работа о роли электрохимии («nanobatteries») в real ReRAM. ([Nature][9])
* **Pershin Y.V., Di Ventra M.** *A simple test for ideal memristors.* J. Phys. D / arXiv (2018/2019). — методика проверки «идеального» мемристора. ([arXiv][10])
* **Kim J. et al.** *An experimental proof that resistance-switching memory cells are not memristors.* (arXiv 2019 / AEM 2020) — экспериментальное опровержение тождества многих switching-устройств идеальному мемристору. ([arXiv][11])
* **Vongehr S., Meng X.** *The Missing Memristor has Not been Found.* Sci. Rep. (2015). — критический анализ терминологии и концепции «missing memristor». ([Nature][12])
* **Abraham I.** *The case for rejecting the memristor as a fundamental circuit element.* Sci. Rep. (2018). — философско-техническая критика фундаментальности мемристора. ([Nature][14])
* **Sebastian A. et al.** *Memory devices and applications for in-memory computing.* Nature Nanotechnology (2020). — обзор по применению памяти (ReRAM/PCM и т.д.) в AIMC (релевантен для дальнейших разделов). ([knowen-production.s3.amazonaws.com][13])
* **Aguirre F. et al.** *Hardware implementation of memristor-based artificial neural networks: challenges and opportunities.* Nat. Commun. (2024). — обзор аппаратных реализаций memristive ANNs. ([Nature][15])

---

<details>
<summary>Детали</summary>

* 1. подготовить **короткий (1–2 стр.) технический cheat-sheet**: формулы, тест Pershin/DiVentra, список измеряемых device-параметров и стандартные методы characterization (что мерить и как), или

</details>

[6]: https://www.cpmt.org/scv/meetings/chua.pdf   "Memristor-The Missing Circuit Element"
[7]: https://www.sciencedirect.com/science/article/pii/S1369702111702991   "Review Memory materials: a unifying description"
[8]: https://web.ece.ucsb.edu/~strukov/papers/2008/Nature2008.pdf   "LETTERS - The missing memristor found"
[9]: https://www.nature.com/articles/ncomms2784   "Nanobatteries in redox-based resistive switches require ..."
[10]: https://arxiv.org/pdf/1806.07360   "A simple test for ideal memristors"
[11]: https://arxiv.org/abs/1909.07238   "An experimental proof that resistance-switching memories ..."
[12]: https://www.nature.com/articles/srep11657   "The Missing Memristor has Not been Found"
[13]: https://knowen-production.s3.amazonaws.com/uploads/attachment/file/5270/10.1038_s41565-020-0655-z.pdf   "Memory devices and applications for in-memory computing"
[14]: https://www.nature.com/articles/s41598-018-29394-7   "The case for rejecting the memristor as a fundamental ..."
[15]: https://www.nature.com/articles/s41467-024-45670-9   "Hardware implementation of memristor-based artificial ..."


---


## 3. Классификация и физика мемристивных устройств

Ниже — систематизированное, технически точное и подкреплённое литературой изложение основных классов «устройств с памятью сопротивления» (memristive / NVM), их физических механизмов, типичных параметров и ключевых проблем, релевантных для AIMC / нейроморфных систем и для маппинга ML/LLM. Все важнейшие утверждения сопровождаются современными, хорошо цитируемыми источниками (включая обзоры до 2024–2025 гг.).

---

### 3.0. Краткая карта: какие классы устройств важны для AIMC/нейроморфики

* **Oxide RRAM (filamentary memristors)** — переключение за счёт образования/разрыва проводящих нитей (filaments) в оксидном слое (напр., TiO₂, HfOₓ). Часто рассматриваются как «искусственные синапсы» в crossbar-массивах. ([Nature][16])
* **Phase-Change Memory (PCM)** — информация в кристаллическом/аморфном состоянии chalcogenide-сплавов; хороша для multi-level analog storage и быстро переключается при джоулевом нагреве. ([poplab.stanford.edu][17])
* **CBRAM (Conductive-Bridge RAM / electrochemical metallization)** — формирование/растворение металлических нитей (Ag/Cu) в матрице; низкое напряжение переключения, быстрый отклик. ([MDPI][18])
* **Ferroelectric FET / FeFET / FEFET** — использование устойчивой поляризации ферроэлектрика для NVM; удобны для интеграции с CMOS и быстрых операций. ([ScienceDirect][19])
* **Spintronic MRAM (STT-MRAM / SOT-MRAM)** — хранение в магнитных туннельных структурах; высокая выносливость и очень быстрая запись/чтение. ([Nature][20])
* **2D-материалы и гибриды** — мемристоры на основе двумерных материалов (MoS₂, h-BN и т.д.) — потенциал для экстремальной масштабируемости и новых режимов переключения. ([Nature][21])

---

### 3.1. Oxide RRAM / filamentary memristors

#### 3.1.1. Устройство и структура

Типичная структура — металл/оксид/металл (MIM): верхний электрод / тонкий оксидный слой (TiO₂, HfOₓ, TaOₓ и т.п.) / нижний электрод. Под действием поля в оксиде мигрируют вакансии/ионы (напр. кислородные вакансии), формируя проводящую нить (low-resistance state, LRS). Разрыв нити возвращает устройство в high-resistance state (HRS). ([Nature][16])

#### 3.1.2. Физика переключения

* **Filament formation/rupture:** локальная агрегация дефектов → образование проводящего канала; разрыв — термодинамически обратимый процесс. Механизмы зависят от материала и структуры (валентные изменения, миграция кислорода, тепловая локализация). ([ScienceDirect][22])
* **Нелинейность и гистерезис:** I–V характеристика обычно гистерезисная; при синусоидальном входе наблюдается «pinched hysteresis loop» в идеальных моделях, но реальная форма определяется кинетикой и температурой. ([Nature][16])

#### 3.1.3. Типичные метрики (фактические диапазоны)

(диапазоны зависят от технологии и структуры — приводим типичные, из обзоров/экспериментов):

* **Switch voltage:** ~0.3–3 V (зависит от толщины и состава). ([MDPI][23])
* **Endurance:** от 10³ до >10⁹ циклов при оптимизированных структурах; типично 10⁴–10⁷ в академических образцах, есть устройства с >10⁹ (BEOL) в отдельных работах. ([ResearchGate][24])
* **ON/OFF ratio:** от ~10 до 10⁵ (в зависимости от материалов и геометрии). ([MDPI][23])
* **Switching time:** нс–мкс диапазон (в лабораторных демо). ([PMC][25])

(Источники: обзоры Waser & Aono; Ielmini; эксперименты по HfOₓ/TaOₓ). ([Nature][16])

#### 3.1.4. Преимущества и ограничения для AIMC

* **Преимущества:** компактность, простая структура для crossbar, потенциал для analog-веса (настройка проводимости), совместимость с BEOL-интеграцией. ([Nature][16])
* **Ограничения:** вариабельность, нелинейность программирования, drift (дрейф проводимости), необходимость verify-циклов и высокая энергоёмкость записи при частых обновлениях (важно для on-chip training). Стратегии компенсации — non-ideality-aware training, калибровка, дублирование и ECC. ([ACS Publications][26])

---

### 3.2. Phase-Change Memory (PCM)

#### 3.2.1. Устройство и принцип

PCM использует фазовое состояние chalcogenide-сплавов (чаще Ge₂Sb₂Te₅ — GST): аморфное состояние (выс. сопротивление) ↔ кристаллическое состояние (низ. сопротивление). Переключение достигается локальным джоулевым нагревом (reset — плавление/быстрая закалка → аморф; set — медленное охлаждение/кристаллизация). ([poplab.stanford.edu][17])

#### 3.2.2. Типичные метрики

* **Switch energy:** крупные варианты — ~10–100 pJ (мные структуры), но последние работы показывают возможности ~0.1 pJ с CNT-электродами / узкими вдаваемыми контактами. ([poplab.stanford.edu][27])
* **Switching speed:** суб-нс до нс для оптимизированных структур; crystallization time — ключевой фактор. ([poplab.stanford.edu][17])
* **Endurance:** типично 10⁶–10⁹ циклов для mushroom-структур; есть перспективы для улучшения при наномасштабировании. ([ResearchGate][28])
* **Retention:** хорошие (годы при комнатной температуре) — в силу термодинамической стабильности кристаллической фазы. ([poplab.stanford.edu][17])

#### 3.2.3. PCM как «analog weight» для AIMC

* **Плюсы:** multi-level storage (несколько уровней проводимости), относительно стабильная retention → подход для длительного хранения весов; demonstrated mapping в задачах inferencing. ([poplab.stanford.edu][17])
* **Минусы:** write-energy и тепловая природа переключения усложняют частые обновления (training); drift (изменение сопротивления аморфного состояния со временем) и элементная неоднородность требуют алгоритмической компенсации. ([Cambridge University Press & Assessment][29])

---

### 3.3. CBRAM, Ferroelectric FEFET, Spintronic (STT/SOT) и 2D-материалы

#### 3.3.1. CBRAM (Conductive-Bridge RAM) — механизм и применение

* **Механизм:** электролитическая миграция Ag/Cu → образование или растворение металлического моста (filament) между электродами; переключение часто при низких напряжениях и быстрых временных масштабах. ([MDPI][18])
* **Метрики:** быстрый отклик (порядка десятков нс), ON/OFF ratio высокая, retention и endurance зависят от материалов; есть отчёты о >10⁸ циклов в некоторых вертикально-переключаемых структурах. ([advanced.onlinelibrary.wiley.com][30])
* **Особенности для AIMC:** хороши для low-voltage, fast switching; некоторые реализации демонстрируют и volatile/нейроморфное поведение (полезно для SNN/emulating short-term plasticity). ([MDPI][18])

#### 3.3.2. Ferroelectric FET / FeFET / FEFET

* **Принцип:** поляризация FE-слоя изменяет пороговое напряжение канала MOSFET → неволатильное запоминание «0/1» или multi-level через контролируемую поляризацию. ([ScienceDirect][19])
* **Параметры:** быстрые операции, низкие напряжения, умеренная endurance (зависит от материала FE); recent advances (dual-bit FeFET) улучшают плотность и endurance. ([Nature][31])
* **Для AIMC:** FeFET удобно интегрируется в CMOS-стек и хорошо подходит для интеграции памяти рядом с логикой; однако для analog-весов требуется контролируемое multi-level поведение и устойчивость доменных состояний. ([ScienceDirect][19])

#### 3.3.3. Spintronic MRAM (STT и SOT)

* **Механизм:** туннельный магнитный переход (MTJ), переключение магнитного состояния через spin-transfer torque (STT) или spin-orbit torque (SOT). ([ScienceDirect][32])
* **Параметры:** экстремально высокая endurance (часто >10¹² циклов), быстрое переключение (нс), но ON/OFF ratio и multi-level analog-поведение сложнее (MTJ — бистабильное устройство). ([Nature][20])
* **Для AIMC:** MRAM лучше подходит для цифровых архитектур и как замена SRAM/Flash, но для аналога/веса требует специальных схем (multi-MTJ, stochastic approaches). ([Nature][20])

#### 3.3.4. 2D-материалы и гибридные структуры

* **Идея:** ультратонкие слои (MoS₂, graphene, h-BN) и их гетероструктуры дают новые режимы переключения (контакты, дефекты, фазовые переходы), высокую компактность и потенциал для снижения энергии. ([Nature][21])
* **Состояние:** активные исследования (2020–2024) показывают многообещающие демонстрации, но промышленная зрелость пока ниже, чем у HfOₓ/PCM/CBRAM. ([Nature][21])

---

### 3.4. Общие проблемы и аппаратно-материальные «узкие места» (cross-cutting issues)

1. **Variability & stochasticity.** Все наноструктурные переключатели показывают статистическую вариабельность по проводимости, порогам и временным характеристикам; это ключевая причина необходимости non-ideality-aware training и аппаратной компенсации. ([ACS Publications][33])
2. **Drift (особенно PCM) и retention.** Дрейф аморфных состояний (R(t) меняется со временем) — проблема для точных analog-весов; для PCM характерен drift, требующий коррекции. ([poplab.stanford.edu][17])
3. **Endurance vs precision trade-off.** Увеличение числа программирований снижает ресурс; высокоточные многократные обновления (training) требуют высокой выносливости или гибридного подхода (pretrain off-chip). ([Cambridge University Press & Assessment][29])
4. **Sneak-path, selectors и array-level проблемы.** Для пассивных crossbar-матриц необходимы селекторы и архитектурные приёмы для подавления «sneak paths». ([Nature][16])
5. **Периферия и mixed-signal overhead.** ADC/DAC, sense amps и программирующая периферия съедают существенную часть выигрыша по энергии/плотности; оптимизации по совместному дизайну устройства↔схема критичны. ([Nature][34])

---

### 3.5. Короткая таблица-сводка (какие устройства — за/против для AIMC / LLM-весов)

| Класс                    |                                       Сильные стороны (AIMC) | Ограничения / риски                                 | Источники                    |
| ------------------------ | -----------------------------------------------------------: | --------------------------------------------------- | -------------------------- |
| Oxide RRAM (filamentary) |           Простая MIM структура, BEOL-интегр., analog tuning | Вариабельность, drift, программир. verify-overhead  | ([Nature][16])              |
| PCM                      | Multi-level, стабильная retention, proven for analog weights | Write energy (тепло), drift, endurance пределы      | ([poplab.stanford.edu][17]) |
| CBRAM                    |         Низкие V, быстрый switching, потенциально low-energy | Управление filament dynamics, retention/variability | ([MDPI][18])                |
| FeFET                    |                          Хорошая совместимость с CMOS, low-V | Контроль multi-level, эндюранс не всегда достаточен | ([ScienceDirect][19])       |
| STT/SOT MRAM             |                             Очень высокая endurance, быстрый | Трудно получить плавный analog-вес                  | ([Nature][20])              |
| 2D-materials             |                     Ультра-масштабируемость, новые механизмы | Ранняя стадия, производственная зрелость            | ([Nature][21])              |

---

### 3.6. Практические рекомендации инженеру AIMC / исследователю нейроморфики

1. **Выбирайте устройство по сценарию использования.** Для «чистого» inference (статичные веса) PCM и RRAM подходят хорошо; для частого on-chip learning лучше ориентироваться на CBRAM/оптимизированные RRAM с высокой endurance или гибридные схемы. ([poplab.stanford.edu][17])
2. **Всегда использовать device-aware моделирование.** При переносе сетей в analog-crossbar моделируйте не только идеальные conductance→weight, но и noise, nonlinearity, write stochasticity и периферийные ADC/DAC эффекты (AIHWKit, CrossSim и др. инструменты). ([Nature][34])
3. **Архитектурные mitigations.** Employ tiling, redundancy, weight remapping, error-correction, mixed-precision и периодические калибровки; экспериментально проверить endurance и write-energy для целевого workflow (training vs inference). ([ACS Publications][26])

---

### 3.7. Основные источники (рекомендуется прочесть в первую очередь)

* **Sebastian A., Le Gallo M., Khokhar A. et al.** *Memory devices and applications for in-memory computing.* Nature Nanotechnology, 2020 — обзорный «must-read» по устройствам AIMC. ([Nature][34])
* **Waser R., Aono M.** *Nanoionics-based resistive switching memories.* Nature Materials (обзор классики по RRAM / nanoionics). ([Nature][16])
* **Raoux S., Xiong F., Wuttig M., Pop E.** *Phase change materials and phase change memory.* (PCM review). ([poplab.stanford.edu][17])
* **Ielmini D.** *Resistive switching RRAM (Chemical Reviews / 2024).* (технически глубокий обзор механизмов и характеристик). ([ACS Publications][33])
* **CBRAM reviews (Abbas 2022; recent 2024/2025 papers)** — для electrochemical metallization и neuromorphic-apps. ([MDPI][18])
* **2D-materials memristors (Nirmal 2024; Rehman 2020)** — обзор возможностей 2D-подходов для memristors. ([Nature][21])
* **Standards & characterization:** Lanza M. et al., ACS Nano (2021) — рекомендации по корректной картеризации endurance/retention. ([ACS Publications][26])

---

#### Заключение раздела 3 — основные мысли

* **Нет «универсального» memristor-решения.** Каждый класс устройств даёт уникальный набор trade-offs (энергия, скорость, endurance, точность), и выбор зависит от целевого сценария (inference vs training, edge vs datacenter). ([Nature][34])
* **Ключ к успеху — co-design:** device ↔ circuit ↔ algorithm. Для LLM/AIMC это означает: выбирать устройства, проектировать массивы и периферию с учётом device-level non-idealities и адаптировать алгоритмы (quantization, adapters, mixed-precision, HW-aware training). ([Nature][34])

---

<details>
<summary>Детали</summary>

* подготовить **таблицу-параметров** (CSV) с реальными числами (switch-V, endurance, energy, ON/OFF) для ключевых материалов и работ (с источниками)

</details>

[16]: https://www.nature.com/articles/nmat2023 "Nanoionics-based resistive switching memories"
[17]: https://poplab.stanford.edu/pdfs/Raoux-PCMreview-mrsbull14.pdf "Phase change materials and phase change memory - Eric Pop"
[18]: https://www.mdpi.com/2072-666X/13/5/725 "Conductive Bridge Random Access Memory (CBRAM)"
[19]: https://www.sciencedirect.com/science/article/abs/pii/S0925838824046656 "The working principle, structural design and material ..."
[20]: https://www.nature.com/articles/s44306-024-00044-1 "Recent progress in spin-orbit torque magnetic random- ..."
[21]: https://www.nature.com/articles/s41699-024-00522-4 "Advancements in 2D layered material memristors"
[22]: https://www.sciencedirect.com/science/article/abs/pii/S0167931724000480 "Filament-based memristor switching model"
[23]: https://www.mdpi.com/2079-9292/11/22/3820 "HfO x /Ge RRAM with High ON/OFF Ratio and Good ..."
[24]: https://www.researchgate.net/figure/a-Endurance-cycles-of-HfO-x-based-RRAM-at-different-SET-voltage-and-cell-size-b-with_fig5_340856124 "a Endurance cycles of HfO x -based RRAM at different SET ..."
[25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7466260/ "Advances of RRAM Devices: Resistive Switching ..."
[26]: https://pubs.acs.org/doi/10.1021/acsnano.1c06980 "Standards for the Characterization of Endurance in Resistive ..."
[27]: https://poplab.stanford.edu/pdfs/Stern-SubNsPCMenergyLimits-aem21.pdf "Uncovering Phase Change Memory Energy Limits by Sub ..."
[28]: https://www.researchgate.net/publication/335626453_Phase-change_memory_cycling_endurance "Phase-change memory cycling endurance | Request PDF"
[29]: https://www.cambridge.org/core/journals/mrs-bulletin/article/phasechange-memory-cycling-endurance/4B7019F184081B441D27701A432A42CD "Phase-change memory cycling endurance | MRS Bulletin"
[30]: https://advanced.onlinelibrary.wiley.com/doi/10.1002/aelm.202400650 "Vertical‐Switching Conductive Bridge Random Access ..."
[31]: https://www.nature.com/articles/s44335-025-00030-8 "Dual-Bit FeFET for enhanced storage and endurance"
[32]: https://www.sciencedirect.com/science/article/abs/pii/S0304885322001275 "Comparative analysis of STT and SOT based MRAMs for ..."
[33]: https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00845 "Resistive Switching Random-Access Memory (RRAM)"
[34]: https://www.nature.com/articles/s41565-020-0655-z "Memory devices and applications for in-memory computing"

---

**4. Модели переключения, компакт-модели и SPICE/Verilog-A** подробно, с математикой, архитектурой моделей, практическими рекомендациями по реализации в SPICE/Verilog-A и ссылками на авторитетные, высокоцитируемые источники (включая публикации и обзоры до 2024–2025 гг.).

---

## 4. Модели переключения, компакт-модели и SPICE/Verilog-A 

### Вводное замечание — зачем это нужно

Для проектирования систем AIMC / memristor crossbars требуется одновременно:

* физически корректное устройство-уровневое описание (физика нитей, ионная кинетика, фазовые процессы),
* компактная, численно устойчивая модель для SPICE/Verilog-A, пригодная для circuit-level симуляций и co-design (device→circuit→architecture), и
* модели шума/варьабильности, теплового взаимодействия и ageing, которые влияют на точность AI-приложений.

Ниже по пунктам — полное разбиение.

---

### 4.1. Физические модели: filament formation/rupture, vacancy drift, phase nucleation

#### 4.1.1. Общая кинетика — уравнения переноса и внутренние переменные

Реальные resistive-switching устройства описывают как *системы с внутренними состояниями*. Базовая картина — одна (или несколько) внутренняя переменная (x(t)) (например, длина/ширина «щели»/пробоя (w), концентрация вакансий ( $c(\mathbf{r},t)$ ), фракция кристаллической фазы (f(t)) и т. п.) управляет проводимостью (G(x)). Общая система записывается как:

$$\begin{aligned} i(t) &= G\big(x(t), v(t)\big), v(t) \quad\text{(электрический отклик)},[4pt] \dot{x}(t) &= F\big(x(t), v(t), T(t)\big) \quad\text{(динамика внутренних переменных)}. \end{aligned}$$

Здесь (F) получается из кинетики миграции и/или фазовой кинетики (ниже — детали для главных технологий). Эта формулировка — ядро «memristive systems» подхода. ([Nature][35])

> **Ключевая нагрузочная (load-bearing) идея №1:** В oxide-RRAM основная физика — ионная миграция/образование проводящих нитей (filament), и этим объясняются медленные/исторично-зависимые изменения сопротивления. ([web.ece.ucsb.edu][36])

#### 4.1.2. Filamentary RRAM: модели и примеры уравнений

* **Gap/filament-length (w) models.** Часто управление проводится через переменную (w) — длину/пересечение проводящей нити. Простая (Strukov / linear ion drift) модель:

$$\frac{dw}{dt} = \mu_v \frac{R_{\mathrm{on}}}{D} i(t) \quad \text{(linear ion drift, Strukov model)}$$

и проводимость аппроксимируется как последовательность сопротивлений LRS/HRS, зависящих от (w). Эта модель проста, но не учитывает нелинейности вблизи границ, температурные эффекты и пороговую динамику — поэтому появились «окна» (window functions) и более сложные версии. ([web.ece.ucsb.edu][36])

* **Field- and thermally-driven filament growth.** Более физичные модели (Ielmini и др.) описывают скорость роста/стирания нитей через поле-ускоренную диффузию вакансий и термическую активацию:

$$\dot{c}(\mathbf{r},t) = -\nabla\cdot \mathbf{J},\qquad \mathbf{J} = -D(T),\nabla c + \frac{\mu(E,T)}{q} c E,$$


где (D(T)) — диффузионный коэффициент (термально-активированный), ( $\mu$ ) — подвижность и (E) — локальное поле. Эти модели требуют решения совместно с тепловым уравнением (Joule heating). ([ScienceDirect][37])

* **Kinetic Monte-Carlo (KMC) / atomistic models.** Для понимания статистики формирования нитей применяют KMC, где отдельные ионные/редокс события моделируются стохастически — полезно для исследования разброса и вероятностей формирования (форминг). ([www2.eecs.berkeley.edu][38])

#### 4.1.3. Phase-Change Memory (PCM): nucleation/growth kinetics

PCM опирается на лазер/электронагрев-индуцированный переход между аморфным/кристаллическим состояниями. Математически — KJMA (Kolmogorov–Johnson–Mehl–Avrami) или модели кристаллизации/ампорфизации:

$$\frac{df}{dt} = K(T) \big(1-f\big)^{n} \quad (\text{упрощённо, заработок на nucleation+growth}),$$

где (f) — доля кристаллической фазлы, (K(T)) экспоненциально зависит от температуры (активационная энергия). Для PCM критична точная модель теплового поля и локального времени/температуры (Joule heating), так как переключение — термодинамический процесс. ([poplab.stanford.edu][39])

#### 4.1.4. Stochasticity и нестабильность

По мере уменьшения размеров, отклик становится стохастичным: образование/разрыв нитей — редкое событие на уровне отдельных дефектов → сильная вариабельность между устройствами и по циклам. Это объясняет большие разбросы ON/OFF и необходимость учитывать статистику при моделировании и проектировании систем. ([Nature][40])

---

### 4.2. Компакт-модели для SPICE/Verilog-A — как моделировать нелинейность и шум

Цель компакт-модели: сохранить ключевую физику (поведение I–V, динамика весов, nonlinearity, drift, stochasticity) при приемлемой скорости и устойчивости симуляции. Ниже — классификация и рекомендации.

#### 4.2.1. Классы компакт-моделей

1. **Phenomenological / behavioral models** — Strukov linear-ion drift, Yakopcic model, TEAM/VTEAM (пороговые адаптивные модели). Просты, параметризуются под данные. (VTEAM — широко используемая voltage-threshold адаптация). ([Hajim School of Engineering][41])
2. **Physics-informed compact models** — моделируют концентрацию вакансий, туннельный барьер (Simmons), температуру. Примеры: Simmons-barrier + gap model, Zanotti et al. физически-основанные RRAM compact model (Verilog-A реализация). ([ScienceDirect][42])
3. **Data-driven / hybrid models** — параметрический/нейросетевые (PINN) или data-driven Verilog-A, обученные по измерениям (полезно, когда физика многокомпонентна и трудно полностью моделируется аналитически). ([PMC][43])

#### 4.2.2. Популярные компакт-модели (конкретика)

* **Strukov / linear ion drift model** — простейший memristor-модель, хороша для концептуальной работы, плохо себя ведёт у границ и без «window function». ([web.ece.ucsb.edu][36])
* **Yakopcic model (IEEE EDL 2011)** — расширяет простую модель, включает нелинейные функции и пороги, часто используется в neuromorphic simulations. ([Chris Yakopcic][44])
* **TEAM / VTEAM (Kvatinsky et al.)** — threshold adaptive models (TEAM = current-controlled, VTEAM = voltage-controlled), гибкие и распространённые, удобны для SPICE. ([Hajim School of Engineering][41])
* **Pickett model / Simmons tunneling gap model** — физически правильнее для filamentary RRAM, моделирует tunneling gap и экспоненциальную зависимость тока от gap; точен, но может приводить к численной жёсткости в SPICE. ([OSTI][45])
* **Zanotti et al. (2022) / comprehensive Verilog-A models** — пример хорошо-тестированной, верифицированной семейства compact-моделей, реализованных в Verilog-A и проверенных на разных технологических данных. Рекомендуется как «industrial-grade» база. ([ScienceDirect][42])

#### 4.2.3. Window functions и ограничение состояния

Фактически все простые модели используют «window function» (f(x)) чтобы: (i) предотвратить выход переменной состояния за физические границы; (ii) ввести нелинейность вблизи границ. Примеры: Joglekar, Biolek, Prodromakis, модифицированные версии. Выбор window-function влияет на устойчивость симуляции и на наличие/отсутствие «boundary lock» и аттракторов в динамике. ([arXiv][46])

#### 4.2.4. Моделирование шума и вариабельности

* **Стохастическая часть**: додайте в уравнение ( $\dot{x}$ ) шумовой член ( $\eta(t)$ ) (например, белый/colored noise) или моделируйте скачки событий (KMC-like) для статистики.
* **Параметрическая вариабельность:** при batch-симуляциях используйте распределения параметров (log-normal для ON/OFF, Gauss/Weibull для Vset/Vreset) и Monte-Carlo. Это важно для предсказания отказоустойчивости crossbar-массивов. ([www2.eecs.berkeley.edu][38])

#### 4.2.5. Численные проблемы и «best practices» в Verilog-A / SPICE

* **Избегать жёстких, разрывных функций.** Используйте сглаженные (differentiable) приближения (soft-thresholds, smooth-abs), потому что дискретные переключатели (если есть) вызывают проблемы с сходимостью. (см. T. Wang / Sandia рекомендации). ([tianshiwang.github.io][47])
* **Границы и clamp-функции:** реализуйте window functions, но аккуратно — некоторые «window» приводят к boundary lock; тестируйте на длительных transient-ах. (см. Biolek vs Joglekar обсуждение). ([arXiv][46])
* **Тепловой coupling:** если модель включает Joule heating, решайте температурное уравнение с подходящим time-step management (thermal time constants обычно больше электрических, но могут влиять на switching). ([ScienceDirect][37])
* **Validation на device-data:** извлекайте параметры из измерений (IV, switching time, variability) и используйте data-driven fitting (nonlinear least squares, Bayesian inference). Messaris / Data-driven Verilog-A — полезные примеры. ([eprints.soton.ac.uk][48])

> **Ключевая нагрузочная идея №2:** Практичные и широко применяемые compact-модели для circuit-level симуляций — это VTEAM/TEAM, Yakopcic и физические модели с Simmons-barrier; выбор модели — trade-off точность ↔ скоростная / численная устойчивость. ([Hajim School of Engineering][41])

---

### 4.3. Температурная зависимость, ageing, масштабирование (нанометровые размеры)

#### 4.3.1. Joule heating и мультифизические эффекты

* **Joule heating** (P = i^2 R) локально повышает температуру и влияет ионную подвижность ( $\mu(T)$ ), диффузию (D(T)) и фазовую кинетику (K(T)). Для PCM это основной переключающий механизм; для RRAM локальный нагрев ускоряет миграцию вакансий и формирование нитей. Модели должны решать coupled electro-thermal уравнения:

$$\rho c_p \frac{\partial T}{\partial t} = \nabla\cdot(k\nabla T) + i^2 R(x,T),$$

где (k) — теплопроводность, ( $\rho c_p$ ) — теплоёмкость. Тепловая динамика часто определяет скорость switching и endurance. ([poplab.stanford.edu][39])

#### 4.3.2. Ageing / endurance mechanisms

* **Физические причины деградации:** электромиграция электродов, образование стабильных/неустранимых нитей, накопление побочных реакций, снижение эффективности tunnel gaps. Endurance лимитируется изменениями интерфейсов и электродных слоёв. Экспериментально наблюдаются разные режимы failure (stuck-ON, stuck-OFF). ([Nature][49])

* **Модель ageing:** вводят «дефицит» ресурса (a(t)), который снижается по мере циклов и влияет на параметры (F) (например, уменьшает подвижность ( $\mu$ ) или увеличивает разброс переключения). В симуляциях полезно моделировать degradation law (empirical fit: power-law или exponential в зависимости от механизма). ([Nature][49])

#### 4.3.3. Масштабирование и вариабильность на nm-уровне

* По мере уменьшения размеров усиливается статистическая природа процесса: один дефект/атом может определять switching. Это приводит к сильному росту cycle-to-cycle и device-to-device variation; требуется stochastic modelling (KMC) и robust system-level компенсации (redundancy, retraining, coding). ([Nature][40])

#### 4.3.4. Влияние температурной среды и эксплуатации

* **Retention/Drift:** особенно PCM проявляет drift аморфного состояния — зависимость R(t) ~ R_0 t^ν (ν ~ 0.05–0.2) — что ухудшает точность analog-weights. Для RRAM есть температурная зависимость retention, и многие работы (Palhares 2024 для PCM) исследуют методы компенсации. ([MDPI][50])

> **Ключевая нагрузочная идея №3:** Тепловые и ageing-эффекты (Joule heating, electromigration, drift) критичны — compact-модель без electro-thermal coupling и ageing-law не даст реалистичной оценки endurance/precision для training-heavy workflows. ([poplab.stanford.edu][39])

---

### 4.4. Практическая дорожная карта: как строить SPICE/Verilog-A модель для AIMC

1. **Выбор уровня модели.** Для архитектурных/системных исследований достаточно VTEAM/Yakopcic (быстрые, численно устойчивые). Для device→circuit co-design используйте physics-informed models (Simmons gap + vacancy dynamics) или Zanotti-style Verilog-A модели. ([Hajim School of Engineering][41])

2. **Шаги разработки модели:**

   * собрать IV datasets (set/reset under range of voltages, pulse widths, temperature);
   * подобрать класс модели (VTEAM / Pickett / vacancy-based) и определить state variables;
   * реализовать сглаженные пороговые и window-функции;
   * встроить stochastic term / Monte-Carlo параметризацию;
   * (если нужно) добавить thermal solver (implicit time stepping) или использовать lumped thermal node;
   * верифицировать на measured traces и perform DC/AC/transient + Monte-Carlo. ([eprints.soton.ac.uk][48])

3. **Verilog-A практики:**

   * избегать вызовов, блокирующих симулятор ($abstime in loops etc.); использовать smooth functions; ограничить использование случайных функций в time-critical paths (seeded RNG for repeatability);
   * документировать параметры и диапазоны (units!), снабдить parameter sweep scripts. (см. рекомендации Zanotti 2022, Messaris 2018). ([ScienceDirect][42])

4. **Верификация:** кроме matching IV/RT curves, проверяйте endurance trends, retention drift, temperature sensitivity и crossbar-scale effects (line resistance, sneak paths). Для этого используйте CrossSim / AIHWKit / MNSIM. ([ResearchGate][51])

> **Ключевая нагрузочная идея №4:** Хорошая Verilog-A модель — это компромисс: достаточно физики для предсказуемости (thermal + vacancy kinetics) и достаточно smoothing/regularization для численной устойчивости в SPICE. Zanotti 2022 и Data-driven Verilog-A примеры — лучшие отправные точки. ([ScienceDirect][42])

---

### 4.5. Примеры уравнений / шаблонов (для разработчика)

#### (A) Простая VTEAM-style форма (schematic)

$$\begin{aligned} i &= G(x),v,
\dot{x} &= \begin{cases} f_+(v)\cdot W(x), & v>V_{\mathrm{th}+},
f_-(v)\cdot W(x), & v< -V_{\mathrm{th}-},
0, & |v| < V_{\mathrm{th}} \end{cases} \end{aligned}$$

где (W(x)) — окно (Biolek/Prodromakis), ( $f_\pm(v)$ ) — полиномиальная/экспоненциальная функция управления скоростью. (VTEAM реализация Kvatinsky et al.). ([ece.technion.ac.il][52])

#### (B) Vacancy-based compact template (physics-informed)

$$\begin{aligned}
i &= I_0\exp!\big(-\alpha, d(x)\big), \sinh!\big(\beta v\big) \quad\text{(tunneling + field)},\
\dot{c} &= -\nabla\cdot(-D(T)\nabla c + \mu(E,T),cE) - R_{\mathrm{recomb}}(c,T) .
\end{aligned}$$

Здесь (d(x)) — effective tunneling gap; (I_0, $\alpha$, $\beta$) — fit параметры; second equation обычно редуцируется к ODE для среднего (c(t)) для компакт-модели. ([OSTI][45])

#### (C) Thermal coupling (lumped)

$$C_{\mathrm{th}} \frac{dT}{dt} = i^2 R(x,T) - \frac{T-T_0}{R_{\mathrm{th}}},$$

используйте этот узел как источник для (D(T)), ( $\mu(T)$ ), (K(T)) и т. д. ([poplab.stanford.edu][39])

---

### 4.6. Литература (must-read) — компактный список источников для реализации моделей

1. D. B. Strukov et al., *The missing memristor found*, **Nature** 2008. ([web.ece.ucsb.edu][36])
2. M. Prezioso et al., *Training and operation of an integrated neuromorphic network based on metal-oxide memristors*, **Nature** 2015. (демонстрации crossbar). ([Nature][35])
3. D. Ielmini, *Resistive Switching Random-Access Memory (RRAM)* — обзор/модели (Chem. Rev / IEEE papers). ([ACS Publications][53])
4. S. Raoux, E. Pop et al., *Phase change materials and PCM review* (MRS Bull / review). ([poplab.stanford.edu][39])
5. H. Lv et al., *Atomic view of filament growth* / evolution of conductive filaments, **Sci. Rep.** (2015). — атомные наблюдения filament dynamics. ([Nature][40])
6. S. Kvatinsky et al., *VTEAM: Voltage Threshold Adaptive Memristor model* (TCASII / IEEE brief). — VTEAM model (Verilog-A implementations exist). ([ece.technion.ac.il][52])
7. T. Zanotti et al., *Comprehensive physics-based RRAM compact model (Verilog-A)* (2022). — пример промышленно ориентированного compact-model. ([ScienceDirect][42])
8. M. J. Rasch et al., *Fast and robust analog in-memory deep neural network training*, **Nat. Commun.** 2024 — требования к устройствам и modelling limits (noise, retention, endurance). ([Nature][54])
9. I. Messaris et al., *A Data-Driven Verilog-A ReRAM Model* (2018) — практический пример data-fitting → Verilog-A. ([eprints.soton.ac.uk][48])
10. PINN / physics-informed compact model: Y. Lee et al., *Physics-informed neural network based compact memristor model* (2024). — пример гибридного подхода. ([PMC][43])

(полная расширённая библиография с DOI/полн. метаданными я могу подготовить отдельно, как вы просили ранее.)

---

### 4.7. Короткие выводы и практические рекомендации (quick checklist)

1. **Если ваша цель — архитектурные/системные оценки (быстро):** начните с VTEAM/Yakopcic (быстрые, гибкие, numerically stable). ([ece.technion.ac.il][52])
2. **Если цель — device→circuit co-design или прогноз endurance/retention:** используйте physics-informed vacancy/filament models с thermal coupling и KMC-подсвеченными параметрами; реализуйте в Verilog-A аккуратно, избегая функций с разрывами. ([ScienceDirect][42])
3. **Обязательно:** включите stochastic / Monte-Carlo профиль параметров (Vset/Vreset, ON/OFF, switching time) — это ключ к предсказуемости crossbar-систем. ([Nature][40])
4. **Тестируйте на масштабе:** при переходе от single-device к large crossbar учитывайте line-resistance, sneak-path, ADC/DAC quantization; симулируйте массивы (CrossSim, AIHWKit) и сравнивайте с Verilog-A device-level. ([ResearchGate][51])

---

#### 5 наиболее «нагружающих» (load-bearing) утверждений этого раздела (и их источники)

1. **Filamentary/Oxide RRAM — основная физика: ионная миграция и образование/разрыв нитей; это диктует динамику resistance-switching.** ([web.ece.ucsb.edu][36])
2. **Для circuit-level симуляций используются семейства компакт-моделей (VTEAM, Yakopcic, Pickett/Simmons-gap), причём выбор — компромисс между точностью физики и численной устойчивостью.** ([ece.technion.ac.il][52])
3. **Тепловое coupling (Joule heating) и ageing (electromigration, filament evolution) существенно влияют на switching и endurance — их нужно учитывать в моделях.** ([poplab.stanford.edu][39])
4. **Window functions (Joglekar/Biolek/Prodromakis и модификации) — стандартный приём для ограничения state-variable и получения стабильных симуляций; их выбор влияет на динамику и погрешность.** ([arXiv][46])
5. **Для практических AIMC/LLM задач компакт-модель должна включать stochastic/variability-модель и быть верифицирована не только по IV, но и по endurance/retention/temperature test-sets.** ([ScienceDirect][42])

---

<details>
<summary>Детали</summary>

1. Сгенерировать пример **Verilog-A шаблона** (VTEAM-стиль) с smoothing/window functions и lumped thermal node — готовый к вставке в SPICE;
2. Подготовить **CSV-таблицу параметров** (типичные Vset/Vreset, ON/OFF, endurance, switching energy) для классов RRAM/PCM/CBRAM/FeFET/MRAM с привязкой к конкретным публикациям;

</details>


[35]: https://www.nature.com/articles/nature14441 "Training and operation of an integrated neuromorphic ..."
[36]: https://web.ece.ucsb.edu/~strukov/papers/2008/Nature2008.pdf "LETTERS - The missing memristor found"
[37]: https://www.sciencedirect.com/science/article/pii/S0167931718300157 "Brain-inspired computing with resistive switching memory ..."
[38]: https://www2.eecs.berkeley.edu/Pubs/TechRpts/2013/EECS-2013-38.pdf "Experimental and Simulation Study of Resistive Switches for ..."
[39]: https://poplab.stanford.edu/pdfs/Raoux-PCMreview-mrsbull14.pdf "Phase change materials and phase change memory - Eric Pop"
[40]: https://www.nature.com/articles/srep13311 "Atomic View of Filament Growth in Electrochemical ..."
[41]: https://www.hajim.rochester.edu/ece/sites/friedman/papers/TCASII_15_VTEAM.pdf "VTEAM: A General Model for Voltage-Controlled Memristors"
[42]: https://www.sciencedirect.com/science/article/abs/pii/S0167931722001800 "Comprehensive physics-based RRAM compact model ..."
[43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10892042/ "A Compact Memristor Model Based on Physics-Informed ..."
[44]: https://cyakopcic1.wordpress.com/wp-content/uploads/2014/02/a-memristor-device-model.pdf "A Memristor Device Model"
[45]: https://www.osti.gov/servlets/purl/1469639 "SAND2018-9642J"
[46]: https://arxiv.org/pdf/1811.06649 "Importance of the window function choice for the predictive ..."
[47]: https://tianshiwang.github.io/talks/2016-10-24--Sandia-memristor-v0.pdf "Well-Posed Models of Memristive Devices - Tianshi Wang"
[48]: https://eprints.soton.ac.uk/403644/2/A_Data_Driven_Verilog_A_ReRAM_Model.pdf "A Data-Driven Verilog-A ReRAM Model - ePrints Soton"
[49]: https://www.nature.com/articles/srep07764 "Evolution of conductive filament and its impact on reliability ..."
[50]: https://www.mdpi.com/2079-9268/14/4/50 "Phase Change Memory Drift Compensation in Spiking ..."
[51]: https://www.researchgate.net/publication/5400588_The_Missing_Memristor_Found "The Missing Memristor Found | Request PDF"
[52]: https://ece.technion.ac.il/wp-content/uploads/2021/01/publication_856-1.pdf "VTEAM – A General Model for Voltage Controlled Memristors"
[53]: https://pubs.acs.org/doi/abs/10.1021/acs.chemrev.4c00845 "Resistive Switching Random-Access Memory (RRAM)"
[54]: https://www.nature.com/articles/s41467-024-51221-z "Fast and robust analog in-memory deep neural network ..."

---


**5. Надёжность устройств: endurance, retention, variability, drift** подробно, с формулами, практическими таблицами значений, влиянием на нейросети и набором методов компенсации. Все ключевые утверждения опираются на авторитетную литературу (обзоры и экспериментальные работы до 2024–2025 гг.). В тексте после утверждений стоят ссылки на использованные источники — по ним можно открыть оригиналы.


## 5. Надёжность устройств: endurance, retention, variability, drift

### Краткая вводная (what & why)

Надёжность (reliability) memristive / NVM-устройств — критический фактор для применения в AIMC/нейроморфных системах. Надёжность здесь включает в себя несколько разных, но взаимосвязанных характеристик:

* **Endurance** — число корректных циклов программирование/стереть (write/erase) до отказа;
* **Retention** — способность удерживать состояние (сопротивление/проводимость) во времени;
* **Variability** — распределение параметров между ячейками (device-to-device) и между циклами (cycle-to-cycle);
* **Drift** — эволюция значения сопротивления/проводимости во времени (особенно важно для PCM).

Эти факторы напрямую определяют, насколько хорошо вязанные аппаратные веса соответствуют «софтверным» весам LLM/ML и насколько часто требуется «ремаппинг»/перепрограммирование/калибровка. ([knowen-production.s3.amazonaws.com][55])

---

### 5.1. Endurance и retention — определения и типичные диапазоны

#### 5.1.1. Формальные определения

* **Endurance (cycles to failure):** количество полных SET/RESET циклов, после которых устройство перестаёт корректно переключаться или теряет приемлемое ON/OFF соотношение. В практических исследованиях рекомендуется строить график «resistance vs cycle» с *одной точкой на цикл* и покрывать множество устройств (см. стандарты). ([pubs.acs.org][56])
* **Retention:** время, в течение которого значение сопротивления/проводимости остаётся в установленном допуске (например ±X% от заданного значения) при заданной температуре; для оценки часто использовать ускоренные испытания (elevated-temperature) и экстраполяцию через Arrhenius-подход. ([pubs.acs.org][57])

#### 5.1.2. Типичные диапазоны (литературные данные)

Ниже — ориентировочные диапазоны, собранные по обзорам и экспериментам (важно: разброс большой; значения зависят от материала, структуры, процесса):

* **Oxide RRAM / filamentary:**

  * Endurance: **~10³ — 10⁸** циклов (в академических публикациях часто 10³–10⁶, в некоторых оптимизированных BEOL-реализациях — >10⁸). ([pubs.acs.org][57])
  * Retention: от часов/дней до >10 лет при RT (зависит от устройства и условия ускоренных тестов). ([knowen-production.s3.amazonaws.com][55])

* **Phase-Change Memory (PCM):**

  * Endurance: **~10⁶ — 10⁹** циклов (зависит от cell geometry и материалов). ([pubs.acs.org][58])
  * Retention: хорошие (годы при RT) для кристаллической фазы; аморфное состояние подвержено drift, но retention традиционно «сильная» сторона PCM. ([pubs.acs.org][58])

* **CBRAM (conductive-bridge):**

  * Endurance: **~10⁵ — 10⁸** (в зависимости от реализации и металла). ([advanced.onlinelibrary.wiley.com][59])
  * Retention: зависит от структуры, иногда хуже чем PCM при высоких температурах. ([advanced.onlinelibrary.wiley.com][59])

* **FeFET / MRAM (spintronic):**

  * FeFET: endurance обычно **10⁶–10⁹** (для NVM-FeFET); retention годами. ([ScienceDirect][60])
  * STT/SOT MRAM: **>10¹²** циклов (очень высокая endurance), retention — хорошая, но MRAM — бистабильные, не легко применять как плавно-аналогое резистивное хранилище. ([ResearchGate][61])

*(Источники: обзоры Sebastian et al. 2020, Ielmini 2024, Lanza et al. 2021 — по стандартизации измерений endurance — и другие экспериментальные работы). ([knowen-production.s3.amazonaws.com][55]))*

---

### 5.2. Variability и drift — статистика, модели и влияние на веса нейросетей

#### 5.2.1. Типы вариабельности

* **Device-to-device (D2D)** — постоянные различия параметров между ячейками (R_on/R_off, Vset/Vreset, programming response).
* **Cycle-to-cycle (C2C)** — изменчивость при повторных программированиях одной и той же ячейки.
* **Temporal drift / noise** — коротко- и долгосрочные флуктуации (1/f noise, Random Telegraph Noise), и дрейф (systematic change of resistance with time). ([pubs.acs.org][57])

#### 5.2.2. Математические модели drift / retention

* **Power-law drift (PCM):** часто R(t) описывают формулой

$$R(t) = R(t_0),\Big(\frac{t}{t_0}\Big)^{\nu},$$

где ν — **drift exponent** (обычно 0.01–0.2 в экспериментаов, зависит от материала и состояния). Это выражение широко применяют для PCM и некоторых RRAM-форм. ([MDPI][62])

* **Arrhenius law для retention:** вероятность термальной деградации часто моделируется через экспоненциальную зависимость от температуры:

$$\tau(T) = \tau_0 \exp!\left(\frac{E_a}{k_B T}\right),$$

где (E_a) — энергия активации процесса деградации (используется при экстраполяции retention с повышенной температуры на RT). Такой подход лежит в основе ускоренных тестов retention. ([pubs.acs.org][57])

#### 5.2.3. Влияние вариабельности и drift на нейронные веса и выходы сетей

Рассмотрим простую операцию VMM (вектор·матрица): выход для j-го выхода ( $y_j = \sum_i w_{ij} x_i)$ ). Если веса хранятся как проводимости ( $g_{ij}$ ) и подвержены стохастике (нулевое смещение μ и дисперсия σ²), вклад вариабельности в дисперсию выхода:

[
\operatorname{Var}(y_j) = \sum_i x_i^2 \operatorname{Var}(g_{ij}).
]

Т.е. ошибка из-за шума/вариабельности масштабируется с суммой квадратов входов (для аддитивного шума). Для LLM/трансформеров большие входные значения, большие матрицы и аккумулируемые суммирования означают, что даже небольшая σ в весах может превратиться в заметную ошибку в активации, ухудшая качество (perplexity, BLEU и т.д.). ([ScienceDirect][63])

Кроме того:

* **Систематический drift** приводит к смещению весов (bias) во времени → деградация accuracy без перепрограммирования/калибровки.
* **Cycle-to-cycle stochasticity** ухудшает применимость on-chip gradient-based training (частые перепрограммирования «съедают» endurance и вносят шум в шаги обновления). ([nature.com][64])

---

### 5.3. Методы компенсации (hardware + circuit + algorithmic)

Ниже — перечень практик компенсации, от device-level до алгоритмических, с оценкой применимости для inference и training.

#### A. Device-/circuit-level методы

1. **Program-and-Verify / incremental step pulse programming (ISPP):**

   * Запрограммировать короткими шагами и после каждого шага читать состояние (verify) — повторять до требуемого значения. Уменьшает погрешность установки conductance, но увеличивает time/energy overhead и изнашивает устройство (endurance trade-off). См. систематические исследования и сравнения схем MLC/verify. ([re.public.polimi.it][65])

2. **Closed-loop programming with learned pulse patterns / neural pulse predictors:**

   * Recent works показывают, что ML-модели (NN) можно обучить предсказывать серию программирующих импульсов для достижения заданного ΔG, учитывая текущую conductance (adaptive programming). Это сокращает число verify-итераций и повышает точность. ([arXiv][66])

3. **Differential pairs / multi-device encoding of one weight:**

   * Использование двух (или N) устройств для представления одного веса (G_pos − G_neg) уменьшает влияние систематических смещений и позволяет компенсировать некоторую вариабельность (снижение относительной ошибки). Однако площадь/энергия растут. Это стандартная аппаратная практика в memristive crossbars. ([Semantic Scholar][67])

4. **Redundancy & remapping:**

   * Если ячейка выходит из строя (stuck-on/off), вес можно перераспределить на резервные ячейки; на уровне матрицы — использовать spare rows/cols и dynamic remapping. Поддерживает работоспособность больших массивов, но требует контроллера и логики управления. ([ResearchGate][68])

5. **Periodic refresh / background calibration:**

   * Для устройств с drift/retention (особенно PCM) периодически читать значения и, при необходимости, перепрограммировать (refresh). Частота refresh — компромисс: чем чаще, тем меньше drift, но тем выше energy / меньше endurance. Рекомендуется настраивать на уровне workload (частота inference/updates). ([MDPI][62])

6. **Error-correcting codes (ECC) и analog-aware ECC:**

   * Традиционные цифровые ECC мало применимы к analog weights; однако комбинированные схемы (квантизация + ECC на цифровых представлениях; parity для coarse-grain blocks) и методы коррекции в уровне mapping (см. программные методы) используются. Для analog-weights эффективнее – differential encoding + redundancy. ([pubs.acs.org][56])

#### B. Algorithmic / software-level методы

1. **Hardware-aware training (noise-aware / non-ideality-aware training):**

   * Включение модели устройства (шум, nonlinearity, drift) в тренировочный loop (QAT for analog devices). Это делает сеть устойчивее к некорректностям при инференсе на реальных устройствах. IBM AIHWKit и др. — примеры инструментов; Rasch et al. 2024 демонстрируют, что такие алгоритмы ограничивают требования к device-параметрам и расширяют набор пригодных материалов. ([nature.com][64])

2. **Optimal weight programming strategies / mapping (software → hardware translation):**

   * Автоматизированные алгоритмы (например, Mackin et al. 2022) оптимизируют последовательность программирования, выбор уровней и порядок программирования весов, чтобы минимизировать деградацию accuracy во времени и уменьшить energy/verify burden. Эти стратегии учитывают drift-модели и device-nonlinearity. ([PMC][69])

3. **Low-rank adapters / LoRA / sparse updates:**

   * Для LLM эффективна идея: не обновлять весь набор весов on-device, а обучать/внедрять малые low-rank адаптеры (LoRA), которые можно хранить/обновлять в более надежной памяти или на небольшом числу high-endurance устройств. Это снижает износ массивов при on-device fine-tune. Rasch 2024 и IBM/Analog papers обсуждают преимущества подобных гибридных подходов. ([nature.com][64])

4. **Periodic re-training / calibration loops in software:**

   * Периодическая калибровка bias/scale (пересчёт zero-point) и дополнительный малый fine-tune могут компенсировать drift и накопленные ошибки в весах без полного перепрограммирования. Rasch 2024 предлагает алгоритмы, снижающие требование к «точной» нулевой точке, что уменьшает нагрузку на перепрограммирование. ([nature.com][64])

5. **Ensembling and stochastic averaging:**

   * Использование ансамблей (несколько экземпляров сети/слоев с небольшими различиями) и усреднение выходов снижает влияние случайного шума и повышает robustness, но увеличивает ресурсные затраты. ([PMC][70])

#### C. Системный подход (co-design)

Оптимальная стратегия обычно гибридная: аппарат/периферия (differential pairs, redundancy, program-verify), plus алгоритмы (hardware-aware training, LoRA, mapping optimization), plus системные политики (refresh cadence, spare allocation). Rasch 2024 подробно анализирует ограничивающие device-параметры и делает вывод, какие материалы/архитектуры подходят для *fast & robust* in-memory training. ([nature.com][64])

---

### 5.4. Практические протоколы измерения и отчётности (что обязателенo репортировать)

Чтобы сравнения между публикациями/технологиями были честными и воспроизводимыми, рекомендуется (Lanza et al., ACS Nano 2021):

1. **Endurance testing:** по одной точке на цикл, многодевайсный набор (N ≥ 10), отчёт о медиане и разбросе; ясно указывать условия (pulse width, amplitude, verify scheme). ([pubs.acs.org][56])
2. **Retention testing:** указывать температуру, read-pulse условия, графики R(t) и метод экстраполяции (Arrhenius) если используется. ([pubs.acs.org][57])
3. **Variability statistics:** отчёт μ/σ (или CV), распределение Vset/Vreset, ON/OFF ratio distribution, cycle-to-cycle jitter. ([PMC][71])
4. **Drift exponent / behavior:** для PCM указывать ν (drift exponent) и метод его извлечения; для RRAM — указать наблюдаемые drift/relaxation формулы. ([MDPI][62])
5. **Program energy & latency:** измерить энергию одной программы и среднее время program-and-verify; это важно для оценки viability on-device training. ([re.public.polimi.it][65])

---

### 5.5. Влияние на выбор материалов/архитектур и рекомендации

* **Если цель — infere nce-only (статические веса, редкий апдейт):** PCM и RRAM с хорошей retention подходят (переобучение редко), используют multi-level quantization, компенсацию drift (refresh) по расписанию. ([pubs.acs.org][58])
* **Если цель — on-chip frequent training/fast updates:** требуется высока endurance и low write energy; в текущем ландшафте предпочтительны CBRAM/оптимизированные RRAM или гибридные схемы + algorithmic снижение числа обновлений (LoRA, sparse updates). Rasch 2024 ограничивает выбор материалов для *fast & robust* in-memory training (conductance noise, symmetry, retention, endurance). ([nature.com][64])
* **Для LLM:** практично использовать hybrid flow: pretrain в дата-центре на digital (GPU/TPU) → deploy weights в AIMC для inference + on-device lightweight adapters/LoRA для personalization / fine-tune; это минимизирует write-demand на memristive arrays. ([nature.com][64])

---

### 5.6. Короткая таблица: основные методы компенсации — плюсы/минусы

| Метод                         |                         Плюсы | Минусы / затраты                 | Источники                   |
| ----------------------------- | ----------------------------: | -------------------------------- | --------------------------- |
| Program-and-Verify (ISPP)     |    Высокая точность установки | Время/энергия, износ (endurance) | ([re.public.polimi.it][65]) |
| NN-пульс-предикторы (learned) |      Меньше verify, адаптивно | Требует training контроллера     | ([arXiv][66])               |
| Differential pairs            |           Снижение bias/noise | Удвоение area/energy             | ([Semantic Scholar][67])    |
| Redundancy & remapping        |             Увеличивает yield | Area + control logic             | ([ResearchGate][68])        |
| Periodic refresh              |            Компенсирует drift | Частые writes → endurance/energy | ([MDPI][62])                |
| Hardware-aware training       |  Алгоритмическая устойчивость | Требует accurate device model    | ([nature.com][64])          |
| LoRA / low-rank adapters      | Минимизируют on-device writes | Не покрывают все use-cases       | ([nature.com][64])          |

---

### 5.7. Резюме — ключевые рекомендации

1. **Стандартизируйте измерения.** Следуйте Lanza et al. (ACS Nano 2021) при оценке endurance/retention — это исключит завышенные/неповторимые отчёты. ([pubs.acs.org][56])
2. **Выбирайте технологию по сценарию.** Для LLM-инференса выбирайте стабильные multi-level технологии (PCM/optimized RRAM), для частых обновлений — выше endurance (CBRAM/optimized RRAM) + алгоритмы, уменьшающие write load. ([pubs.acs.org][58])
3. **Комбинируйте аппаратные и алгоритмические подходы.** Program/verify + differential encoding + hardware-aware training + mapping/LoRA — это рабочая комбинация для минимизации деградации accuracy при сохранении выгоды AIMC. ([nature.com][64])
4. **Моделируйте variability и drift в симуляциях.** Любая архитектурная оценка LLM↔AIMC должна включать Monte-Carlo по параметрам устройств и drift-модели (R(t)=R0 t^ν / Arrhenius retention). Инструменты: AIHWKit, CrossSim, MNSIM + device-level compact models. ([ResearchGate][61])

---

### Основные использованные источники (чтобы быстро перейти к ним)

* Sebastian, A.; Le Gallo, M.; Khokhar, A. et al., *Memory devices and applications for in-memory computing*. **Nature Nanotechnology** (2020). ([knowen-production.s3.amazonaws.com][55])
* Lanza, M.; Waser, R.; Ielmini, D. et al., *Standards for the Characterization of Endurance in Resistive Switching Devices*. **ACS Nano** (2021). ([pubs.acs.org][56])
* Ielmini, D., *Resistive Switching Random-Access Memory (RRAM)* — Chem. Rev. / major review (2024). ([pubs.acs.org][57])
* Rasch, M. J.; Carta, F.; et al., *Fast and robust analog in-memory deep neural network training.* **Nature Communications** (2024). — limits in terms of conductance noise, symmetry, retention and endurance; algorithmic mitigation. ([nature.com][64])
* Mackin, C. et al., *Optimised weight programming for analogue memory-based DNNs* (2022) — framework for program/verify and optimal mapping. ([PMC][69])
* Palhares, J.H.Q., *PCM drift compensation in spiking hardware* (2024) — examples of refresh/compensation strategies for PCM. ([MDPI][62])

---

<details>
<summary>Детали</summary>

A) Сформировать **CSV-таблицу** «типичные параметры устройств» (Endurance, Retention @RT, Drift ν, Vset/Vreset, ON/OFF, switching energy) для RRAM/PCM/CBRAM/FeFET/MRAM на основе cited papers;
B) Подготовить **пример тест-протокола** (шаг-за-шагом) для измерения endurance/retention и отчётности (по рекомендациям Lanza 2021);
C) Сгенерировать **краткий Verilog-A / measurement driver pseudocode** для program-and-verify с adaptive pulse scheduling (NN-predictor example).

</details>

[55]: https://knowen-production.s3.amazonaws.com/uploads/attachment/file/5270/10.1038_s41565-020-0655-z.pdf "Memory devices and applications for in-memory computing"
[56]: https://pubs.acs.org/doi/10.1021/acsnano.1c06980 "Standards for the Characterization of Endurance in Resistive ..."
[57]: https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00845 "Resistive Switching Random-Access Memory (RRAM)"
[58]: https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00670 "Phase-Change Memory for In-Memory Computing"
[59]: https://advanced.onlinelibrary.wiley.com/doi/10.1002/aelm.202400905 "Resistance Drift of Phase Change Materials Beyond the ..."
[60]: https://www.sciencedirect.com/science/article/abs/pii/S2352940724001501 "Forming-less flexible memristor crossbar array for ..."
[61]: https://www.researchgate.net/publication/340288631_Memory_devices_and_applications_for_in-memory_computing "Memory devices and applications for in-memory computing"
[62]: https://www.mdpi.com/2079-9268/14/4/50 "Phase Change Memory Drift Compensation in Spiking ..."
[63]: https://www.sciencedirect.com/science/article/pii/S1359028625000130 "Current opinions on memristor-accelerated machine ..."
[64]: https://www.nature.com/articles/s41467-024-51221-z "Fast and robust analog in-memory deep neural network ..."
[65]: https://re.public.polimi.it/retrieve/e0c31c11-b93a-4599-e053-1705fe0aef77/TED_2021_rev_v3_nomarks.pdf "Accurate program/verify schemes of resistive switching ..."
[66]: https://arxiv.org/html/2403.06712v1 "Neural Networks Facilitating Memristor Programming"
[67]: https://www.semanticscholar.org/paper/Memristor-based-neural-networks-with-weight-Wang-Xiong/84efcb2cc2fb367c0bb138fd80eb88eb0e37b16d "[PDF] Memristor-based neural networks with weight ..."
[68]: https://www.researchgate.net/publication/317572455_Rescuing_Memristor-based_Neuromorphic_Design_with_High_Defects "Rescuing Memristor-based Neuromorphic Design with ..."
[69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9247051/ "Optimised weight programming for analogue memory- ..."
[70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10912231/ "Hardware implementation of memristor-based artificial ..."
[71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9980037/ "A review of memristor: material and structure design ..."

---


## 6. Топологии и схемотехника: crossbar, 1T1R, селекторы, sneak-path mitigation 


Ниже — подробный технический разбор популярных топологий для memristor-матриц (passive crossbar vs active 1T1R/1S1R), физики и математики «sneak-path» эффекта, обзор селекторов, схемных и архитектурных приёмов (tiling, hierarchical macros, V/2,V/3 bias-schemes, ADC-sharing) и комментарии по вертикальному (3D) стеку. Для каждого подпункта — конкретные выводы, рекомендации по проектированию и ссылки на авторитетные источники.

---

### 6.0. Короткая карта раздела (чему учимся)

* Что такое passive crossbar, откуда берётся «sneak-path» и почему это ограничивает размер матриц. ([Nature][72])
* Почему 1T1R (или 1S1R) решает sneak-path, какие у этого компромиссы (плотность, BEOL/FEOL интеграция). ([Wiley Online Library][73])
* Какие селекторы существуют (diode, OTS, threshold selectors, self-rectifying cells), плюсы/минусы, как их моделировать. ([SpringerLink][74])
* Архитектурные приёмы: V/2, V/3 biasing, tiling, hierarchical macros, ADC/driver placement, и вертикальный stacking (3D) — влияние на плотность, тепло, производительность. ([ScienceDirect][75])

---

### 6.1. Passive crossbar vs transistor-assisted (1T1R / 1S1R): преимущества и проблемы (sneak paths)

#### 6.1.1. Passive crossbar — принцип и «накладные» эффекты

* **Структура:** двухслойная сетка проводящих строк (WL — word lines) и столбов (BL — bit lines) с двухконтактными мемристорами в пересечениях (MIM). MAC реализуется как суммирование тока на колонке (Kirchhoff). ([Nature][72])
* **Преимущества:** максимум плотности (нет транзистора на ячейку), простота BEOL интеграции, хорошая вертикальная масштабируемость (несколько crossbar-слоёв в BEOL). ([Nature][76])
* **Главная проблема — sneak-path currents:** при попытке прочитать или записать выбранную ячейку ток идёт не только через неё, но и по множеству параллельных путей через соседние ячейки. Это снижает read margin, искажает результирующие суммы и мешает точной установке conductance. Математически — при чтении i_BL (ток столбца) = I_selected + Σ I_sneak, где I_sneak — суммарный ток через все непреднамеренные пути; при увеличении размера N×N и при наличии LRS-ячейок сумма sneak-токов растёт быстро. ([RSC Publishing][77])

**Формула (упрощённая модель):**
Для маленького примера 2×2 (M1 выбранная, остальные M2–M4 возможные «sneak»):

$$I_{BL} ;=; \frac{V}{R_{M1}} ;+; \frac{V}{R_{M2}+R_{path2}} ;+; \frac{V}{R_{M3}+R_{path3}} + \dots$$

где дополнительные слагаемые — токи через «параллельные» ветви; при N ≫ 1 суммарный шумовой вклад может сравняться с сигналом. Практический вывод: пассивный crossbar даёт плотность, но ограничивает масштаб 1R-матриц без селекторов/схемных мер. ([users.cs.utah.edu][78])

#### 6.1.2. 1T1R / transistor-assisted arrays (active crossbar)

* **1T1R (или 1T–1M):** каждая ячейка включает селектор-транзистор (обычно MOSFET) в серии с мемристором → при чтении/записи транзистор открывает только выбранную строку/ячейку, предотвращая sneak-path. Это убирает большую часть побочных токов и существенно расширяет read/write-margin. ([Wiley Online Library][73])
* **Плюсы:** надёжность операций, простая адресация, отсутствие или снижение V/2/V/3 хитростей, упрощённая периферия (меньше необходимости в сложных схемах компенсации). ([Nature][76])
* **Минусы:** площадь на ячейку резко увеличивается (≈ ×5–10 по сравнению с 1R, зависит от технологии транзистора), сложнее масштабировать по плотности; сложность BEOL/FEOL интеграции (если транзистор — в том же слое CMOS). Для 3D-stacking 1T1R также сложнее, но есть подходы с вертикальными транзисторами/monolithic-3D. ([Wiley Online Library][73])

#### 6.1.3. 1S1R (selector + memristor) — компромисс

* **1S1R:** сериация отдельного селектора (S) и памяти (R) на ячейку; селекторы бывают двух типов: (i) диодные (унидирекционные), (ii) threshold/OTS (двухполярные без значимой проводимости при малом напряжении, резкое включение выше Vth). 1S1R восстанавливает большую часть преимуществ 1T1R по подавлению «sneak», при этом селектор обычно меньше транзистора по площади → лучшая плотность. ([SpringerLink][74])
* **Минусы селекторов:** требуется селектор с высокой нелинейностью, большой I_on/I_off и совместимость по току/напряжению с памятью; некоторые селекторы (OTS) обладают ограничением по endurance/variability и добавляют требования к управлению термикой. ([SpringerLink][74])

**Практический вывод:** выбор 1R vs 1S1R vs 1T1R — это trade-off плотности ↔ надёжность/контролируемость. Для крупных, высокоштучных LLM-матриц, где плотность и 3D-stacking критичны, промышленники (и IBM-группа по AIMC) рассматривают 1S1R + aggressive tiling и vertical stacking как компромисс. ([IBM Research][79])

---

### 6.2. Selector-devices и архитектурные методы (tiling, hierarchical macros)

#### 6.2.1. Типы селекторов — обзор

* **Диодные селекторы (1D1R):** простая uni-directional селекция; требует двунаправленной память для bipolar switching или схемы записи/чтения с полярностью управления; диоды обычно CMOS-compatible, но могут ограничивать линейность. ([Wiley Online Library][73])
* **ОВС / OTS — Ovonic Threshold Switch (1S1R):** быстрый threshold-switch (прямая/обратная полярность), используется в PCM/PCM-like crosspoint (Optane стиль). Показывает очень высокую нелинейность (практически открывается при V>Vth). Современные OTS разработки — материалные вариации (Ge-Se-Te и т.д.). Недостаток: управляемость I_on и endurance задачи. ([SpringerLink][74])
* **MIEC/selective-selector (metal-insulator electrochemical):** селекторы с ионной реакцией, часто сочетаются с CBRAM; те же проблемы: соответствие по току, стабильность. ([ACS Publications][80])
* **Self-rectifying memristors / intrinsic nonlinearity:** некоторые мемристоры показывают сильную нелинейность в I–V, что позволяет строить «selectorless» 1R-матрицы (self-rectifying RRAM). Их преимущества — простота; недостатки — ограниченная универсальность и чувствительность к process variations. ([Nature][81])

#### 6.2.2. Критерии выбора селектора

* **High nonlinearity (I(Vth)/I(0))** — чем выше, тем лучше подавление sneak-path.
* **High On-current (I_on) @ Vop** — должен пропускать нужный write/read ток.
* **Low leakage (I_off)** — минимизировать шунтирующие токи при «полувыбранных» состояниях.
* **Thermal robustness & endurance** — селектор и память должны выдерживать циклы и Joule heating при программировании. ([SpringerLink][74])

#### 6.2.3. Архитектурные методы: V/2, V/3, biasing и их trade-offs

* **V/2 и V/3 схемы:** при выбранной ячейке WL=V, BL=0, остальные строки/столбцы получают V/2 (или V/3 вариант), чтобы половинчатые/третичные напряжения не вызывали переключение полувыбранных ячеек. V/2 простая, но создаёт большие полувыбранные напряжения → напряжение влияет на точность write/read и sneak. V/3 снижает полувыбранное напряжение, но требует более сложного драйвера (и увеличивает number of rails). RSC/Frontiers обзоры и симуляции показывают, что V/3 даёт лучшую масштабируемость по размеру по сравнению с V/2, но сложнее реализуется. ([RSC Publishing][77])

* **One-hot / one-WL pulsing, Ground scheme** — альтернативы для некоторых режимов, иногда используемые в SNN/neuromorphic pulsing schemes; trade-off: сложнее по timing. ([ResearchGate][82])

#### 6.2.4. Tiling, hierarchical macros и ADC-sharing

* **Tiling:** практический приём — разбивать большие матрицы на tiles (например 128×128, 256×256) и выполнять VMM по tile’ам, аккумулируя результаты цифрово. Это держит массивы в пределах допустимого read-margin и облегчает локальную калибровку и перекрытие ADC-ресурсов. ([Nature][76])
* **Hierarchical macros:** несколько tiles формируют macro; внутри macro — локальная периферия (ADC, DAC, drivers) для снижения межсоединений и latency. Это даёт баланс плотности и управляемости. ([Nature][76])
* **ADC-sharing:** чтобы экономить область и энергию, один «мощный» ADC может обслуживать несколько колонок по time-multiplexing; trade-off — throughput. Параметры выбора: ADC-ENOB vs budget latency, scheduler. ([Wiley Online Library][73])

#### 6.2.5. Другие схемные хитрости

* **Differential encoding (G+ / G−)** уменьшает влияние offset/half-select errors, но удваивает число ячеек на вес. ([Nature][76])
* **Active-read circuits (sense amps, low-noise amplifiers)** и calibration loops уменьшают влияние line resistance и sneak-currents в практике. ([users.cs.utah.edu][78])

---

### 6.3. Вертикальный stacking (multi-layer crossbars) и влияние на плотность / производство

#### 6.3.1. Что даёт 3D / BEOL stacking

* **Плотность:** вертикальное многослойное размещение crossbar-слоёв (BEOL memristor layers над CMOS) значительно повышает synapse-density на единицу площади пластинки (orders-of-magnitude по сравнению с 2D). Это особенно важно для LLM-scale weight matrices, где нужен огромный объём памяти. ([OpenReview][83])
* **Короткие межслойные interconnects** при 3D уменьшает delay/latency между слоями и может упростить распределение power/ground. ([OpenReview][83])

#### 6.3.2. Трудности и ограничения (thermal, yield, testability)

* **Тепловая проблема:** плотная вертикальная упаковка затрудняет отвод тепла (Joule heating при записи), что усиливает drift и ускоряет ageing; thermal coupling между слоями требует мультифизического дизайна и, возможно, throttling при интенсивных write-сценариях. ([Nature][76])
* **Yield & defectivity:** чем больше слоёв и пересечений, тем важнее встроенные схемы ремонта (spare rows/cols), тестирование и remapping — это противоречит цели максимальной плотности. ([Nature][76])
* **Integration flow:** BEOL-процессы для memristors должны быть совместимы с CMOS thermal budgets; некоторые материалы требуют low-temperature deposition, иначе ухудшаются CMOS-транзисторы. Это ограничивает список «производственно пригодных» материалов. ([Wiley Online Library][73])

#### 6.3.3. Архитектурные выводы (особенности AIMC / LLM)

* **3D + MoE synergy:** при использовании Mixture-of-Experts (MoE) можно хранить разные expert-blocks на разных физически изолированных 3D-bank’ах и активировать только нужный слой/bank → уменьшение energy на inference. IBM/ETH работы 2024–2025 показывают, что MoE + 3D AIMC — практически жизнеспособный путь масштабирования LLM-инференса. ([IBM Research][79])
* **Design guidance:** для больших LLM массивов рекомендуется: (i) 3D stacking с 1S1R (OTS или диод-селектор) для плотности, (ii) агрессивный tiling с локальной ADC/driver периферией, (iii) system-level thermal management и spare allocation для yield. ([Nature][76])

---

### 6.4. Практические рекомендации и чек-лист инженеру

1. **Выберите cell-type по system-requirements:**

   * если критична плотность и 3D stacking — рассматривайте 1S1R с качественным OTS/diode селектором;
   * если критична надёжность/гибкая адресация (training, frequent updates) — 1T1R предпочтительна. ([Nature][76])

2. **Ограничьте tile-size под read-margin:** моделируйте sneak-current и выбирайте tile size (например 128×128…512×512) так, чтобы read-margin в worst-case (много LRS полей) оставался положительным с запасом. Симуляторы: CrossSim/AIHWKit, SPICE + Verilog-A compact models. ([ResearchGate][84])

3. **Смешайте аппаратные и алгоритмические mitigations:** differential encoding + hardware-aware training + program/verify + periodic refresh → наилучшее сочетание в большинстве сценариев AIMC/LLM. ([Nature][76])

4. **Если используете passive 1R, требуйте self-rectifying I–V или очень высокую nonlinearity:** в противном случае sneak-path делает массивы неуправляемыми. Исследуйте self-rectifying RRAM и complementary switching topologies. ([Nature][81])

5. **Планируйте thermal budget и testing/repair:** для 3D stacks заранее проектируйте thermal sensors, controlled write scheduling и spare rows/cols для ремонта дефектов. ([Nature][76])

---

### 6.5. Ключевые источники (must-read для глубокого погружения)

* Prezioso M. et al., *Training and operation of an integrated neuromorphic network based on metal-oxide memristors*, **Nature** 2015 — экспериментальная демонстрация transistor-free crossbar-NN; важна как proof-of-concept для passive arrays. ([Nature][72])
* Shi L. et al., *Research progress on solutions to the sneak path issue in memristor crossbar arrays*, **Nanoscale Adv. / RSC** 2020 — обзор методов борьбы со sneak-path (1T1R, 1S1R, biasing схемы, архитектуры). ([RSC Publishing][77])
* Ielmini D., *Resistive Switching Random-Access Memory (RRAM)* — Chem. Rev. / comprehensive review (2024) — хорош для device→circuit trade-offs. ([ACS Publications][80])
* Aguirre F. et al., *Hardware implementation of memristor-based artificial neural networks: challenges and opportunities*, **Nat. Commun.** 2024 — системный обзор архитектурных проблем crossbar и периферии. ([Nature][76])
* Büchel J., Vasilopoulos A. et al., *Efficient scaling of large language models with Mixture of Experts and 3D analog in-memory computing* (IBM Research / Nat Comput Sci 2025) — про 3D-AIMC и MoE как практический путь масштабирования LLM-инференса. ([IBM Research][79])
* Papers on selectors / OTS (Zhao 2024; recent OTS demonstrations 2024–2025) — обзор и новейшие материал-инженерные решения для селекторов. ([SpringerLink][74])

---

### 6.6. Итог (takeaways)

* **Пассивный 1R-crossbar** даёт максимальную плотность, но **sneak-paths** и line-resistance ограничивают реальный размер матриц без селекторов или хитрых схем; решения: 1S1R (selector) или 1T1R (transistor). ([RSC Publishing][77])
* **Selector-devices (OTS, diode, self-rectifying RRAM)** — ключевой технологический компонент: качество селектора определяет, будет ли 1S1R работать в большой матрице. ([SpringerLink][74])
* **Архитектурные паттерны (tiling, hierarchical macros, ADC-sharing, V/2,V/3)** — необходимы для практической реализации AIMC и масштабирования матриц для LLM. ([Nature][76])
* **3D stacking** — даёт путь к требуемой плотности для LLM, но требует решения thermal/yield/testability вопросов; в сочетании с MoE даёт убедительную экономику. ([OpenReview][83])

---

<details>
<summary>Детали</summary>

* а) сгенерировать **шаблон-модель** sneak-path (SPICE) для оценки read-margin / V/2,V/3 в N×N матрице (с параметризуемыми R_on/R_off и wire-resistance),
* б) подготовить **сравнительную таблицу** (CSV) area/throughput/energy для 1R / 1S1R / 1T1R с опорой на литературу

</details>

[72]: https://www.nature.com/articles/nature14441 "Training and operation of an integrated neuromorphic ..."
[73]: https://onlinelibrary.wiley.com/doi/full/10.1002/aisy.202100017 "Memristive Crossbar Arrays for Storage and Computing ..."
[74]: https://link.springer.com/article/10.1007/s40820-023-01289-x "Chalcogenide Ovonic Threshold Switching Selector"
[75]: https://www.sciencedirect.com/science/article/abs/pii/S0038110115002294 "Numerical study of read scheme in one-selector ..."
[76]: https://www.nature.com/articles/s41467-024-45670-9 "Hardware implementation of memristor-based artificial ..."
[77]: https://pubs.rsc.org/en/content/articlehtml/2020/na/d0na00100g "Research progress on solutions to the sneak path issue in ..."
[78]: https://users.cs.utah.edu/~rajeev/pubs/iccd15m.pdf "Improving Memristor Memory with Sneak Current Sharing"
[79]: https://research.ibm.com/publications/efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog-in-memory-computing "Efficient Scaling of Large Language Models with Mixture ..."
[80]: https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00845 "Resistive Switching Random-Access Memory (RRAM)"
[81]: https://www.nature.com/articles/s41598-019-48932-5 "A Novel Resistive Switching Identification Method through ..."
[82]: https://www.researchgate.net/figure/a-Three-reading-bias-schemes-in-memristor-crossbar-array-ground-V-2-and-V-3-schemes_fig4_321256283 "a) Three reading bias schemes in memristor crossbar array"
[83]: https://openreview.net/pdf?id=J23gohVY9s "3D Analog In-Memory Computing for Efficient Mixture of ..."
[84]: https://www.researchgate.net/publication/391962261_River_Sneak_Path_Aware_READ-based_In-Memory_Computing_for_1T1M_Memristive_Crossbars "Sneak Path Aware READ-based In-Memory Computing for ..."

---

## 7. Периферия и смешанные-сигнальные узкие места (ADC/DAC, sense-amps, драйверы) 


Ниже — технически подробный разбор роли периферии в AIMC/мемристор-матрицах, количественные ориентиры, основные «бутылочные горлышки» и проверенные инженерные приёмы (ADC-sharing, analog accumulation, current-mode sense-amps и т.д.). Все главные утверждения опираются на авторитетные публикации и открытые инструменты (IBM AIHWKit, Ambrogio et al. 2023, Rasch 2024, обзоры 2024–2025 и исследования по ADC-моделированию).

---

### 7.1. Архитектура периферии и её роль (DAC → crossbar → ADC)

#### Что делает периферия в типичной AIMC-системе

1. **Ввод (DAC / driver / pulse engine).** Цифровые входы (активации) преобразуются в аналог (напряжение, ток, длительность импульса, PWM). Типы: бинарные/многоуровневые DAC (capacitive/correlated-cap DACs), резистивные DAC, а также генераторы pulse-width/pulse-amplitude. IBM-чип Ambrogio et al. 2023 использует PWM/pulse-duration для подачи 8-бит входов на строки. ([Nature][85])
2. **MAC в кроссбаре (аналог).** Токи или заряды суммируются по столбцам (Kirchhoff). Это даёт огромный параллелизм: N² весов → N выходов за 1 шаг. ([Nature][85])
3. **Чтение/оцифровка (ADC / sense-amp / ramp → counter).** Аналоговый суммарный ток/заряд нужно преобразовать в цифровое значение (активацию следующего слоя). Варианты: прямые ADC на каждой колонке, shared/pooled ADC, charge → time (ramp / pulse-duration) и даже ADC-free схемы. ([Nature][85])

#### Битность / масштаб (typical choices)

* **Input precision (DAC side):** 4–8 бит для многих AIMC демо; Ambrogio 2023 использует 8-бит входы, но входы часто кодируют в PWM/duration, не в классический DAC. IBM AIHWKit моделирует 4–8 бит в исследованиях hardware-aware training. ([Nature][85])
* **ADC resolution (колонка → цифровой выход):** в практике встречаются 4–8 бит ADC для колонок (trade-off energy↔accuracy). При высокоточном требовании иногда используют 8–10 бит, но energy/area растут резко. См. раздел 7.2 про энергию. ([arXiv][86])

---

### 7.2. Сравнение энергоэффективности: периферия vs «чистый» crossbar

#### Главная эмпирическая правда

* **Аналог-ядро (VMM) само по себе очень энергоэффективно** — параллельные операции в кроссбаре часто дают десятки–сотни× выигрыша по energy/MAC по сравнению с цифровым сопоставлением. Но **периферия может съедать существенную долю выигрыша**: ADCs и DACs часто оказываются «доминирующим» потребителем area и энергии в реальных макрокомпонентах. ([Nature][85])

#### Количественные ориентиры (литература)

* В нескольких работах и симуляциях показано, что **ADCs могут составлять большую долю площади и энергии блока**: в одном анализе ADC-подсистемы ответственны за ~57% площади и до ~86% энергопотребления CIM-макро (зависит от архитектуры и применяемых ADC). Это подчёркивает, почему оптимизация ADC/их числа/битности — ключ. ([ACM Digital Library][87])
* Ambrogio et al. (Nature 2023) демонстрируют альтернативные методы (pulse-width/charge→duration), которые снижают необходимость «тонких» одиночных ADC на каждую колонку, и показывают системную энергоэффективность до 6–12 TOPS/W на реальном кристалле (с учётом периферии). Это пример «правильной» архитектуры периферии (charge integration + ramp/duration → счётчики), которая сильно уменьшает нагрузку на классические ADC. ([Nature][85])
* Модель-статья по ADC (Andrulis et al., 2024, arXiv) даёт инструмент-оценку: число ADC, их разрешение и требуемая пропускная способность прямо определяют архитектурный energy/area trade-off; увеличение число параллельных ADC уменьшает нагрузку на каждый (и при прочих равных может снизить энергию на операцию), но увеличивает площадь. Вывод: оптимизация — многомерна и зависит от throughput target. ([arXiv][86])

#### Следствия для дизайна AIMC / LLM

* **Если ADC-энергия доминирует** → выгодней уменьшать их число или разрешение, использовать ADC-sharing / time-multiplexing, или заменить ADC схемой charge→time (duration) / ramp+comparator + counter (как у Ambrogio), либо искать ADC-less архитектуры. ([Nature][85])
* **Если требуются высокие-битные частые оцифровки** (напр., для transformer attention с staging) — периферия неизбежно займёт значительную часть power/area бюджета; тогда важен co-design (адаптировать NN к низкому ENOB/low-bit partial sums). ([Nature][88])

---

### 7.3. Hardware-tricks: ADC-sharing, analog accumulation, current-mode sense-amps и проч.

Ниже — набор техник, реально используемых/исследуемых, с кратким объяснением, когда и почему они работают.

#### 7.3.1. ADC-sharing и time-multiplexing

* **Идея:** иметь меньше ADC, чем колонок, и обслуживать их по очереди (time-multiplex). Экономия площади/энергии за счёт меньшего числа ADC, но throughput падает и/или требуется более сложный scheduler.
* **Когда применимо:** когда рабочая нагрузка допускает по-колонное time-division (низкая частота обновлений) или когда колонки уже делятся на tiles. Примеры: архитектурные исследования и модели (Andrulis et al., 2024) показывают, что при разумной конфигурации можно найти «sweet spot» по E⋅area. ([arXiv][86])

#### 7.3.2. Analog accumulation / charge-domain accumulation / pulse-duration encoding (PWM → duration)

* **Как работает (пример Ambrogio):** входы кодируют длительностью импульса (PWM); кроссбар суммирует токы в периферийную ёмкость (charge integration). Затем периферия конвертирует заряд в длительность/кол-во импульсов и/или в цифровое значение с помощью счетчика (ramp / comparator + counter), снижая требование к классическому high-precision ADC. Это сильно уменьшает energy/area overhead ADC и даёт высокую параллельность. ([Nature][85])
* **Плюсы:** меньшая потребность в дорогих ADC; гибкость (можно мультиплексировать интеграторы между плитами); хорошая масштабируемость для inference-heavy workloads. ([Nature][85])

#### 7.3.3. Current-mode sense-amps и интеграторные схемы

* **Current-to-voltage / current-to-time преобразователи**: вместо ADC можно сначала конвертировать суммарный ток в временной интервал (time-to-digital) или в заряд на конденсаторе, затем сравнивать/оцифровывать более «дешёвым» способом. Эти интерфейсы (current-mode sense amps, transimpedance amplifiers, integrators) дают выигрыш по энергопотреблению при определённых SNR требованиях. ([arXiv][89])

#### 7.3.4. ADC-less и hybrid подходы

* **ADC-less architectures:** ряд исследований (RIMAC, HCiM и пр.) показывают схемы, где весь или значительная часть oцифровки убраны — используют бинар/тернарные выходы или вычисляют частично в цифровом CiM. Это даёт заметное снижение overhead, но требует co-design ML (quantization-aware / pruning / specially trained nets). ([ACM Digital Library][90])
* **Пример:** Pruning for Improved ADC Efficiency (2024) — модификации обучения, которые делают активность «дружественной» к ADC (sparsity балансированная по колонкам), позволяют уменьшить ADC-энергию до нескольких× без потери точности. ([arXiv][91])

#### 7.3.5. Multi-level / mixed-signal tricks (partial-sum quantization, extreme PSQ)

* **Partial-sum quantization / bit-serial accumulation:** разбивать вход на биты / каналы и выполнять несколько проходов (bit-serial DACs + low-bit ADC). Позволяет уменьшить ADC-битность и/или использовать дешёвые ADC, но увеличивает latency/number of cycles. Исследования показывают выгодность для energy/area в edge-кейсах; trade-offs для LLM — сложнее, но применимы для некоторого набора слоев. ([ACM Digital Library][87])

#### 7.3.6. Low-precision ADC design & choice (SAR / flash / pipeline)

* **SAR ADCs:** часто выбирают для low-to-medium resolution (4–8 бит) — хорошая энергоэффективность на низкой аналитике; подходит многим CIM случаям. Недорогие SARs сейчас достигают fJ–pJ/conv-step в продвинутых работах (в зависимости от процесса и частоты). ([Lab Groups][92])
* **Flash ADCs / parallel ADCs:** быстрые, но энерго-и площадно-дорогие; используются если нужен extremely high throughput при низкой битности.
* **Вывод:** выбор ADC топологии и разрешения — архитектурный демарш-пункт: чем больше ADC/ниже latency — тем выше area/energy; чем меньше ADC/ниже разрешение — тем больше требования к NN-adaptation и HWA training. ([arXiv][86])

---

### Практические рекомендации инженеру (checklist)

1. **Сначала эмпирически смоделируйте (AIHWKit / RAELLA / Modeling ADC tools).** Используйте IBM AIHWKit для быстрых экспериментов hardware-aware: она включает модели ADC/DAC и периферии. ([aihwkit.readthedocs.io][93])
2. **Определите допустимую ENOB и throughput:** если сеть терпит 4–6 бит partial sums → можно использовать дешёвые SARs / shared ADCs; если нужны 8+ бит — учитывайте, что ADC-энергия/площадь вырастет и потребуется архитектурная компенсация (tiling, pipeline). ([arXiv][86])
3. **Исследуйте ADC-sharing + charge→time (PWM/duration) как способ снизить ADC-overhead.** Ambrogio 2023 — хороший HW-референс. ([Nature][85])
4. **Для LLM-attention/transformer, где staging/partial sums важны,** планируйте ADC-budget заранее: иногда удобнее частично оцифровывать внутренние представления (OLP / digital scratch) вместо полного analog-pipeline. ([Nature][85])
5. **Используйте алгоритмические приёмы (pruning targetted to ADC efficiency, quant-aware training)** чтобы «сделать» модель дружественной ADC. Такие co-design подходы дают большие выигрыши. ([arXiv][91])

---

### Быстрый набор «нагружающих» утверждений (load-bearing claims) — и ссылки

1. **ADCs/DACs/периферия часто съедают подавляющую долю area и energy в CIM-блоке — оптимизация периферии критична для реальной выгоды AIMC.** ([ACM Digital Library][87])
2. **Charge-integration / pulse-duration (PWM→duration) и ramp+counter архитектуры (использованные в Ambrogio 2023) — практический способ значительно снизить требование к high-precision ADC.** ([Nature][85])
3. **ADC-sharing и time-multiplexing дают area/energy выигрыш, но trade-off по throughput; существует «sweet-spot», который можно найти моделированием (см. Andrulis et al. 2024).** ([arXiv][86])
4. **ADC-less / hybrid подходы (RIMAC, HCiM и др.) показывают, что при co-design (алгоритм↔железо) можно убрать или снизить роль ADC и сохранить точность.** ([ACM Digital Library][90])
5. **Практичные AIMC-проекты требуют совместного дизайна: device → array → периферия → алгоритмы (HWA training / pruning / quantization) — иначе периферия «съест» весь выигрыш от analog VMM.** ([Nature][88])

---

### Полезные ссылки (для быстрой работы / моделирования)

* IBM AIHWKit — документация и GitHub (моделирование device→system и peripheral effects). ([aihwkit.readthedocs.io][93])
* Ambrogio S. et al., *An analog-AI chip for energy-efficient speech recognition and transcription*, **Nature** 2023 — реальное HW-демо с ramp/duration peripheral. ([Nature][85])
* Andrulis T. et al., *Modeling Analog-Digital-Converter Energy and Area for CiM Accelerator Design* (arXiv 2024) — архитектурное моделирование ADC energy/area. ([arXiv][86])
* ACM/ISCA/architecture papers (Extreme Partial-Sum Quantization) и арки по ADC-less (RIMAC, HCiM) — идеи для ADC-free/low-ADC дизайнов и pruning-driven co-design. ([ACM Digital Library][87])
* Rasch M. J. et al., *Fast and robust analog in-memory deep neural network training* (Nat Commun 2024) — ограничения device/periphery для on-chip training и guidance for device requirements. ([PMC][94])

---

<details>
<summary>Детали</summary>

A) построить простую архитектурную модель (CSV/таблица) с расчётом энергии/площади для выбранных конфигураций: «full ADC per column (8b)» vs «ADC-sharing 1:4 (6b)» vs «charge→duration (ramp+counter)» — с приближенными числами из литературы;
B) сгенерировать SPICE-псевдокод / структурную схему ramp→comparator→counter (как в Ambrogio) и прокомментировать практические параметры (компоненты, time-constants, noise budget);

</details>

[85]: https://www.nature.com/articles/s41586-023-06337-5 "An analog-AI chip for energy-efficient speech recognition and transcription | Nature"
[86]: https://arxiv.org/abs/2404.06553 "Modeling Analog-Digital-Converter Energy and Area for Compute-In-Memory Accelerator Design"
[87]: https://dl.acm.org/doi/10.1145/3528104 "Extreme Partial-Sum Quantization for Analog Computing-In ..."
[88]: https://www.nature.com/articles/s41467-024-45670-9 "Hardware implementation of memristor-based artificial ..."
[89]: https://arxiv.org/pdf/2403.18367 "arXiv:2403.18367v2 [cs.AR] 21 May 2024"
[90]: https://dl.acm.org/doi/10.1145/3566097.3567860 "RIMAC: An Array-Level ADC/DAC-Free ReRAM-Based ..."
[91]: https://arxiv.org/abs/2403.13082 "Pruning for Improved ADC Efficiency in Crossbar-based Analog In-memory Accelerators"
[92]: https://labs.engineering.asu.edu/mixedsignals/wp-content/uploads/sites/58/2023/04/Low-Power_SAR_ADC_Design_Overview_and_Survey_of_State-of-the-Art_Techniques-1.pdf "Low-Power SAR ADC Design: Overview and Survey of State ..."
[93]: https://aihwkit.readthedocs.io/en/latest/analog_ai_hw.html "Analog AI Hardware"
[94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335942/ "Fast and robust analog in-memory deep neural network ..."

---

## 8. Compute-in-Memory / Analog In-Memory Computing (AIMC) — концепции и реализации

Ниже — развёрнутый технический раздел, который покрывает: как и почему в crossbar-матрицах выполняются аналоговые MAC (8.1), какие гибридные/цифровые варианты и 3D-интеграция применяются на практике (8.2), и какие системные парадигмы (edge-inference, MoE для LLM, роботы) наиболее естественно выигрывают от AIMC (8.3). Везде даны ссылки на авторитетные, высоко цитируемые и свежие публикации (2020–2025).

---

### 8.1. Аналоговые MAC в crossbar — принцип работы (Ом, Кирхгоф) и скорость инференса

#### 8.1.1. Физическая / математическая идея (очень кратко)

* **Устройство:** crossbar = сетка пересекающихся строк (word-lines) и столбцов (bit-lines). В каждом пересечении находится элемент памяти с проводимостью ( $g_{ij}$ ).
* **Операция VMM (вектор·матрица):** подаём аналоговые напряжения ( $v_i$ ) на строки; по закону Ома и правилу Кирхгофа суммарный ток в j-том столбце равен:

$$I_j ;=; \sum_i g_{ij}, v_i .$$

Далее ( $I_j$ ) преобразуется периферией в цифровую активацию (ADC / charge→time / comparator+counter). Это физически ветвящаяся параллельная реализация матричного умножения — «все веса участвуют одновременно» → высокая параллельность и потенциально очень высокая пропускная способность. ([knowen-production.s3.amazonaws.com][95])

**Нагружающее утверждение 1:** аналоговый VMM в crossbar выполняет (N) сумм за время одного аналогового шага (параллельно), что даёт фундаментальное преимущество по throughput по сравнению с последовательным цифровым выполнением. ([knowen-production.s3.amazonaws.com][95])

#### 8.1.2. Практика: якоря реализации и ограничения

* **Параллелизм и latency:** latency одного «шагового» VMM≈ время установки напряжений + время интеграции + ADC latency. В реальных системах суммарная латентность на tile — десятки наносекунд → миллисекунды на слои больших LLM при мерцании tile-to-tile коммуникаций. ([Nature][96])
* **Шум / неточности:** физические non-idealities (шум, проводимость-шум, межстрочные сопротивления, нелинейности программирования, drift) превращают операцию в стохастическую аппроксимацию; требуется hardware-aware training / calibration. Это снижает «идеальный» выигрыш, но зачастую выигрыш по energy остаётся существенным. ([Nature][97])

**Нагружающее утверждение 2:** эффективный перенос нейросетей на AIMC требует совместного дизайна: устройство ↔ массив ↔ периферия ↔ алгоритмы (hardware-aware training), иначе шум и non-idealities резко убивают accuracy. ([Nature][97])

#### 8.1.3. Примеры чисел / HW-демонстрации

* **Ambrogio et al., Nature 2023:** реальный analog-AI чип на PCM-массиве (35M устройств, 34 tiles) показал chip-sustained ~12.4 TOPS/W на speech-task — демонстрация практического energy-вклада AIMC при хорошо спроектированной периферии (charge-integration / ramp→counter). Это одна из самых консервативно измеренных HW-демо, показывающая реальную эффективность. ([Nature][96])
* **ALBERT on analog chip (Chen et al., 2025):** демонстрация трансформера ALBERT на PCM-analog-tiles (34 tiles, 14 nm CMOS BEOL) — proof-of-concept Transformer-scale inference на analog-hardware. Это показывает, что масштабировать AIMC на real-world LLM-слои уже возможно (с архитектурными договорённостями). ([Nature][98])

---

### 8.2. Гибридные и цифровые CiM (mixed-signal, TSV/3D stacking)

#### 8.2.1. Почему гибрид? (архитектурная мотивация)

* Полностью аналоговая цепочка редко покрывает все операции NN (layer-norm, softmax, attention-normalization, nonlinearity), поэтому практичные AIMC-чипы обычно **смешанные**: тяжелые VMM в аналоговой памяти, остальное в цифровом ядре/CMOS. Это даёт лучшее соотношение энергоэффективности ↔ универсальность. ([knowen-production.s3.amazonaws.com][95])

#### 8.2.2. 3D / TSV / BEOL stacking — зачем и какие проблемы

* **Преимущества:** BEOL-слои memristors над CMOS-логикой даёт огромную плотность synapse-на-площадь, уменьшает длину межсоединений и даёт возможность вертикальной кластеризации tiles (важно для LLM). ([IBM Research][99])
* **Проблемы:** thermal coupling (Joule heating при записи), yield & repair (спайки/дефекты в большом объёме), процессные ограничения (низкотемпературный BEOL требуется для CMOS-сохранности). Требуется архитектурный контролёр для распределения writes и thermal-throttling. ([IBM Research][100])

**Нагружающее утверждение 3:** 3D NVM-BEOL stacking + mixed-signal peripherals является ключевым инженерным путём для достижения synapse-density, необходимой LLM-масштабам; одновременно это вводит новые thermal/yield требования, которые стали предметом интенсивных исследований (IBM 2025 MoE+3D работы). ([IBM Research][99])

#### 8.2.3. Mixed-signal patterns на уровне системы

* **Local analog compute + local ADC + digital accumulation:** наиболее распространённый паттерн — analog VMM → per-tile ADC → цифров accumulation / partial-sum routing → следующий tile. Это упрощает cross-tile коммуникацию, но ADC-пер-tile/column — большая часть площади/энергии (см. раздел 7). ([Nature][96])
* **Charge-domain / time-to-digital techniques:** как в Ambrogio (charge→duration + counter) — снижение требования к дорогим high-precision ADC; совместимо с mixed-signal 3D стеком. ([Nature][96])

---

### 8.3. Парадигмы использования: edge inference, MoE для LLM, energy-constrained robotics

#### 8.3.1. Edge inference (on-device, privacy / latency)

* **Почему AIMC:** ограниченные энергетические ресурсы и требование low-latency делают AIMC привлекательным для on-device LLM/LLM-inference (частичное/локальное). Analog VMM на BEOL может обеспечить orders-of-magnitude более высокую энергоэффективность по сравнению с GPU при inference-heavy workloads. Практические кейсы: speech, keyword spotting, local NLP tasks. ([Nature][96])

#### 8.3.2. Mixture-of-Experts (MoE) + 3D AIMC для LLM (ключевая идея)

* **Идея MoE:** условная активация (conditional computing): в каждой инстанции inference активируется только небольшой набор «expert» подсетей — существенно уменьшает практическую вычислительную нагрузку на модель с миллиардными параметрами.
* **Почему MoE + 3D-AIMC хорошо сочетаются:**
  *MoE снижает фактическую долю весов, которые нужно активировать для одного inference,* а 3D stacked AIMC даёт плотность хранения для огромного числа experts. Совместная комбинация может радикально снизить inference-cost для LLM. IBM/ Büchel et al. 2025 анализируют и демонстрируют этот путь как практичный для масштабирования LLM-инференса в AIMC. ([IBM Research][99])

**Нагружающее утверждение 4:** сочетание MoE и 3D NVM-AIMC — один из наиболее убедительных путей сделать LLM-уровень параметров энергетически и экономически выполнимым на analog-hardware (показано в IBM 2025). ([IBM Research][99])

#### 8.3.3. Робототехника и энерго-ограниченные системы (real-time control)

* **Требование real-time:** robotics и автономные системы требуют детерминированного low-latency inference и небольшого энергопрофиля; AIMC может дать преимущества в control loops и sensor fusion, особенно если сети компактны или используют SNN/neuromorphic форматы. Однако для safety-critical систем требуется дополнительная валидация надежности/отказоустойчивости. ([knowen-production.s3.amazonaws.com][95])

#### 8.3.4. Практическая стратегия для LLM deployment (рекомендуемая)

1. **Pretrain в цифровом датасентре (GPU/TPU)** → сохранить «основание» модели.
2. **Map inference heavy слои (dense, FFN, experts) на AIMC tiles**; держать attention/softmax/normalization в цифровом домене или реализовать гибридные numeric алгоритмы. (ALBERT 2025 demo — пример). ([Nature][98])
3. **Использовать LoRA / low-rank adapters** для on-device fine-tune (минимизирует число weight-updates на AIMC). ([Nature][97])
4. **MoE + conditional routing** для экономии энергии при хранении огромного числа параметров, активируя только нужные tiles для каждого запроса. ([IBM Research][99])

**Нагружающее утверждение 5:** на практике оптимальная рабочая схема для LLM — гибрид: digital pretrain + analog inference (tiles) + light on-device adapters (LoRA) + MoE для масштабирования; это уже подтверждается демонстрациями на PCM-чипах и архитектурными исследованиями 2024–2025. ([Nature][96])

---

### Заключение раздела 8 — основные выводы и рекомендации

* AIMC даёт фундаментальное аппаратное преимущество для параллельных VMM-операций (экономия движения данных, большая плотность synapse), но **ключ к реальному выигрышу** — грамотный co-design: device ↔ array ↔ периферия ↔ алгоритмы. ([knowen-production.s3.amazonaws.com][95])
* Для LLM практичный путь — **hybrid**: digital pretrain + analog inference + low-write adapters + MoE + 3D stacking; это минимизирует write-нагрузку, решает плотностные требования и делает энергетическую экономику выгодной. ([IBM Research][99])
* Из ключевых публикаций/демо для углубления читателя: Sebastian et al. 2020 (обзор AIMC и устройств), Ambrogio et al. 2023 (analog chip demo), Rasch et al. 2024 (алгоритмы для robust in-memory training), IBM Büchel et al. 2025 (MoE + 3D AIMC roadmap), Chen et al. 2025 (ALBERT на analog chip). ([knowen-production.s3.amazonaws.com][95])

---

<details>
<summary>Детали</summary>

* A) привести **пошаговый рецепт** (mapping recipe) для переноса одного слоя Transformer (Dense + FFN) на AIMC-tile с конкретными числовыми примерами (битность входов, размер tile, число tiles, оценка energy/MAC), или
* B) сгенерировать **сопоставимую таблицу**: GPU vs AIMC (inference & hybrid training) с величинами energy/MAC и latency, опираясь на Ambrogio 2023, Rasch 2024 и IBM 2025 оценки

</details>


[95]: https://knowen-production.s3.amazonaws.com/uploads/attachment/file/5270/10.1038_s41565-020-0655-z.pdf "Memory devices and applications for in-memory computing"
[96]: https://www.nature.com/articles/s41586-023-06337-5 "An analog-AI chip for energy-efficient speech recognition ..."
[97]: https://www.nature.com/articles/s41467-024-51221-z "Fast and robust analog in-memory deep neural network ..."
[98]: https://www.nature.com/articles/s41467-025-63794-4 "Demonstration of transformer-based ALBERT model on a ..."
[99]: https://research.ibm.com/publications/efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog-in-memory-computing "Efficient Scaling of Large Language Models with Mixture ..."
[100]: https://research.ibm.com/people/julian-buchel "Julian Büchel"

---


**9. Нейроморфные принципы и спайковые нейронные сети (SNN)** подробно, с математикой, практическими соображениями по обучению и аппаратной реализации, плюс сравнением основных платформ. Ниже — структурированный технический текст по пунктам 9.1–9.3, с ключевыми выводами и ссылками на авторитетную литературу.

> **Ключевые load-bearing утверждения (цитаты):**
>
> 1. STDP — классическое правило временной пластичности и его нейробиологическое обоснование. ([PubMed][101])
> 2. Сравнение кодировок (rate vs temporal / latency) — их достоинства/недостатки в задачах распознавания и энергоэффективности. ([PMC][102])
> 3. Surrogate-gradient методы сделали возможным прямое градиентное обучение глубоких SNN и сейчас составляют основной практический путь учебы SNN. ([arXiv][103])
> 4. Intel Loihi — программируемый manycore для SNN с on-chip learning и богатой моделью нейрона/пластичности; Loihi/Loihi-2 — основной индустриальный референс. ([Редвуд Центр Нейронаук][104])
> 5. TrueNorth — крупномасштабный аппаратный демонстратор (1M нейронов / 256M синапсов) как proof-of-concept event-driven архитектуры. ([Наука][105])

---

## 9. Нейроморфные принципы и спайковые нейронные сети (SNN)

### 9.1. Кодирование информации: rate code, temporal code, latency code (и смешанные схемы)

#### Что такое кодирование в SNN

SNN оперируют дискретными событиями (спайками). «Кодирование» — способ представления чисел/сигналов через последовательности спайков. Главные схемы:

1. **Rate coding (частотное кодирование).** Информация кодируется средней частотой спайков за окно времени (T). Простая концепция (аналог амплитуды в ANNs): значение (x) ↔ частота ( $f(x)$ ). Преимущества — стабильность против джиттера; недостаток — требуется много времени/спайков для точности → потеря энергоэффективности. ([PMC][102])

2. **Temporal coding / time-to-first-spike / latency coding.** Информация кодируется временем первого спайка или точной временной позицией спайка относительно начала окна. При низкой активности (один-несколько спайков) можно передать больше информации быстрее и с меньшей энергией, но требует высокой точности временных задержек и чувствительности к шуму. ([PMC][102])

3. **Population / rank / phase codes.** Значение кодируется через распределение по популяции нейронов (параллельность) или относительный порядок спайков (rank order). Хороши для робастности и быстрого распознавания при небольшой латентности. ([PMC][102])

4. **Смешанные подходы.** Практические SNN часто используют гибриды: latency (быстрая передача) + небольшие раунды rate для улучшения точности, либо комбинируют кодирование вместе с temporal filters (resonant neurons). ([arXiv][106])

#### Математика (LIF-нейрон и spike encoding)

Часто используют модель LIF (leaky integrate-and-fire):

$$\tau_m \frac{dV(t)}{dt} = - (V(t)-V_{rest}) + R_m I(t),$$

нейрон генерирует спайк, когда ( $V(t)$ ) достигает порога ( $V_{th}$ ), затем происходит reset. Кодирование времени первого спайка (time-to-first-spike) определяется тем, как быстро интегрируется входной ток ( $I(t)$ ) до порога — при большей амплитуде (I) — быстрее достижение ( $V_{th}$ ).

#### Практические соображения при выборе кодировки

* **Energy vs latency trade-off:** temporal/latency коды дают минимальную энергию и малую латентность при условии низкой частоты спайков, но требуют точной синхронизации и устойчивых задержек. Rate-код более робастен, проще обучаем и моделируется, но требует больше spikes/time. ([PMC][102])
* **Совместимость с аппаратурой:** event-driven hardware (TrueNorth, Loihi) естественно поддерживают sparse temporal codes; memristor-based AIMC подходы чаще используют rate-like или pulse-based кодирование (количество/ширина импульсов) для совместимости с analog crossbar. ([Наука][105])

**Вывод:** выбор кода зависит от задачи (реальное-время vs batch), требуемой точности, аппаратной платформы и допустимой сложности обучения/декодирования.

---

### 9.2. Локальные правила обучения: STDP, Hebbian, и современные алгоритмы (e-prop, surrogate gradients и др.)

#### Классические локальные механизмы: Hebb, STDP

* **Hebbian plasticity (классический):** «neurons that fire together, wire together» — корреляция pre/post spike увеличивает вес.
* **STDP (Spike-Timing Dependent Plasticity):** изменение веса ( $\Delta w$ ) зависит от временной разницы ( $\Delta t = t_{\text{post}}-t_{\text{pre}}$ ): если pre перед пост ( ($\Delta t>0$) ) → LTP (усиление), если post перед pre → LTD (ослабление). Форма функции обычно экспоненциальная с временными константами порядка 10–50 ms. STDP — экспериментально подтверждаемое правило (обзор Caporale & Dan). ([PubMed][101])

**Практическая роль STDP:** локальная, биологически правдоподобная и энергонезависимая — отлична для онлайн learning и ассоциативного запоминания, но сама по себе редко достигает качества, сопоставимого с современными градиентными методами для сложных распознавательных задач. Поэтому часто комбинируют STDP с глобальными сигналами (reward-modulated STDP) или используют как механизм initial/unsupervised обучения. ([PubMed][101])

#### Modern training paradigms — от e-prop до surrogate gradients

1. **E-prop (Bellec et al., 2020).** Предлагает biologically-plausible локально вычислимые правила для обучения рекуррентных SNN, приближая производительность BPTT (backprop through time) при онлайн-обучении; идея — комбинировать локальные eligibility traces с глобальным error signal (neuromodulator). E-prop — ключевой алгоритм для on-chip learning на neuromorphic hardware. ([Nature][107])

2. **Surrogate gradients (Neftci et al. 2019; Zenke 2021 и др.).** Тактика: заменить нули производной порога на гладкую «surrogate» функцию при обратном распространении, позволив тем самым применять современный градиентный оптимизатор для SNN (SGD/Adam). Surrogate-gradient методы сделали возможным прямое обучение глубоких SNN и сейчас — основной практический путь обучения SNN в ML-контексте. Эти методы совместимы как с фреймворками (PyTorch), так и с аппаратными эмуляциями. ([arXiv][103])

3. **Conversion methods (ANN→SNN).** Конверсия обученной ANN в SNN (rate-approximation) остаётся практичным способом получить SNN-реализации с качеством, близким к ANN, особенно для vision-задач: учат ANN с ReLU / quantization-aware, затем переводят активации в spike-rates. Плюс — простота; минус — потеря преимуществ temporal coding и latency. ([PMC][108])

4. **Reinforcement / reward-modulated STDP.** Для задач управления и RL используют глобальные reward-signals чтобы модулировать локальные STDP-правила. Это даёт простую, биологически вдохновлённую online learning схему, пригодную для embedded/robotics. ([PubMed][109])

#### Практическая рекомендация по обучению SNN

* Для **сложных распознавательных задач** и глубоких архитектур в настоящее время предпочтительны surrogate-gradient методы или гибриды (surrogate + e-prop), поскольку они дают лучшее качество и контроль над loss-функцией. ([arXiv][103])
* Для **low-power online learning (роботы, BCI)** — e-prop / reward-modulated STDP / eligibility traces — более подходящие, так как требуют локального апдейта и малой коммуникации. ([Nature][107])

---

### 9.3. Платформы SNN: Loihi (Loihi/Loihi-2), TrueNorth, SpiNNaker и другие — сравнение возможностей

Ниже — сравнительная сводка «по-функциям», ключевые сильные и слабые стороны.

#### Intel Loihi / Loihi-2 (Davies et al.)

* **Архитектура:** many-core neuromorphic processor (Loihi: 128 cores? 60 mm² chip; поддерживает программируемые нейроны, dendritic compartments, on-chip learning rules и асинхронную event-driven модель). Loihi-2 расширяет возможности (более гибкие нейронные модели, улучшенная производительность, доступ через Neuromorphic Research Cloud). ([Редвуд Центр Нейронаук][104])
* **Сильные стороны:** программируемые локальные правила, on-chip learning, гибкая поддержка surrogate/e-prop like schemes, хороший инструментальный стек (SDK), ориентирован на онлайн/streaming workloads (sensor fusion, robotics). ([dynamicfieldtheory.org][110])
* **Ограничения:** не предназначен для «тяжёлых» dense LLM-уровней; лучше подходит для sparse, event-driven, real-time задач. ([Intel Download][111])

#### IBM TrueNorth (Merolla et al. 2014)

* **Архитектура:** 1M spiking neurons, 256M synapses — крупномасштабный интегральный пример event-driven нейроморфного чипа с высокой энергоэффективностью для специфических задач. ([Наука][105])
* **Сильные стороны:** доказал масштабируемость event-driven neuromorphic approach; low-power operation for pattern-recognition tasks.
* **Ограничения:** ограниченная гибкость в программируемых learning-rules и нейронных моделях; разработан больше как ASIC для конкретных рабочий нагрузок, чем как general-purpose neuromorphic computer. ([Наука][105])

#### SpiNNaker (University of Manchester)

* **Архитектура:** цифровой manycore (ARM cores) с сетевой коммутацией, ориентирован на реал-тайм симуляцию больших сетей до биологических масштабов; гибкий и программируемый. ([ePrints Soton][112])
* **Сильные стороны:** гибкость в моделях и масштабах (можно моделировать до миллиардов нейронов распределённо); хорошо подходит для исследовательских задач и симуляции.
* **Ограничения:** digital cores → энергопотребление выше, чем у специализированных event-driven ASIC/analog платформ при тех же задачах. ([ePrints Soton][112])

#### Другие платформы

* **BrainScaleS (Heidelberg)** — analog accelerated neuromorphic hardware (fast, but requires calibration).
* **Memristor-based SNN demonstrators** — интеграция memristive synapses + CMOS neurons (исследования 2023–2025 показывают promising energy‐density tradeoffs для SNN). ([MDPI][113])

#### Табличная сводка (кратко)

| Платформа                |                                          Тип | Сильные стороны                                                          | Ограничения                                |
| ------------------------ | -------------------------------------------: | ------------------------------------------------------------------------ | ------------------------------------------ |
| Loihi / Loihi-2          | digital manycore, event-driven, programmable | on-chip learning, flexible neuron models, low energy for event workloads | не для dense LLM layers                    |
| TrueNorth                |                            ASIC event-driven | extreme scale (1M neurons), low power                                    | ограниченная гибкость                      |
| SpiNNaker                |                       digital manycore (ARM) | гибкость, масштабируемость для исследований                              | выше power vs ASIC                         |
| BrainScaleS              |                           analog accelerated | очень высокая скорость (acceleration factor)                             | calibration, analog variability            |
| Memristor SNN prototypes |                        hybrid memristor+CMOS | potential high density & low energy                                      | device variability, integration immaturity |

(подробнее — см. обзоры и survey-papers по Loihi/TrueNorth/SpiNNaker). ([Редвуд Центр Нейронаук][104])

---

### 9.4. Приложения, где SNN дают преимущество

* **Event-based vision (DVS) и sensor fusion:** низкая латентность и нативная обработка событий → большая энергоэффективность и низкая пропускная нагрузка. ([arXiv][106])
* **Robotics / control / real-time inference:** локальное обучение, маленькая задержка, стойкость к шуму; e-prop и reward-modulated STDP — реальные кандидаты для on-device adaptation. ([Nature][107])
* **Low-power Always-on tasks (keyword spotting, anomaly detection):** SNN хорошо подходят для таких задач, где sparse event-driven computation экономит энергию. ([dynamicfieldtheory.org][110])

---

### 9.5. Ограничения, открытые проблемы и направление R&D (2024–2025)

1. **Точность vs эффективность:** SNN пока обычно уступают ANNs в «сырых» метриках качества на больших датасетах; surrogate-gradient методы и ANN→SNN conversion сокращают разрыв, но универсального рецепта нет. ([PMC][108])
2. **Algorithm↔hardware co-design:** требуется развитие алгоритмов (sparse temporal codes, hardware-aware surrogate gradients, e-prop variants) вместе с аппаратурой для реального выигрыша. ([dynamicfieldtheory.org][110])
3. **Интеграция с AIMC / memristors:** memristor-synapse arrays обещают плотность/энергию, но device-variability и on-chip plasticity реализация остаются активной темой исследований (см. memristor-SNN обзоры 2024–2025). ([MDPI][113])
4. **Benchmarking & reproducibility:** нужно больше репликативных HW-демонстраций и standardized benchmarks для SNN (как то делает Loihi community). ([dynamicfieldtheory.org][110])

---

### 9.6. Рекомендуемая библиотека чтения (must-read)

* **Davies M. et al.,** *Loihi: A Neuromorphic Manycore Processor with On-Chip Learning.* IEEE Micro (2018). ([Редвуд Центр Нейронаук][104])
* **Merolla P. A. et al.,** *A million spiking-neuron integrated circuit with a scalable communication network and interface.* Science (2014). ([Наука][105])
* **Painkras E. et al.,** *SpiNNaker: a 1-W 18-core system-on-chip for massively-parallel neural network simulation.* JSSC (2013). ([ePrints Soton][112])
* **Caporale N., Dan Y.,** *Spike-timing-dependent plasticity: a Hebbian learning rule.* Annu. Rev. Neurosci. (2008). ([PubMed][101])
* **Neftci E. O. et al.,** *Surrogate Gradient Learning in Spiking Neural Networks.* arXiv (2019) — practical overview. ([arXiv][103])
* **Bellec G. et al.,** *A solution to the learning dilemma for recurrent networks of spiking neurons (e-prop).* Nat. Commun. (2020). ([Nature][107])
* **Zenke F.,** *The Remarkable Robustness of Surrogate Gradient Learning.* Neural Comput. (2021). ([PubMed][114])
* **Guo Y. et al.,** *Direct learning-based deep spiking neural networks: a review.* (2023) — обзор современных подходов обучения SNN. ([PMC][108])
* **Recent memristor-SNN reviews (2024–2025)** — обсуждают интеграцию memristive synapses и аппаратные SNN-реализации. ([MDPI][113])

---

### 9.7. Короткое практическое резюме / рекомендации

* Для **real-time, low-power, event-driven** задач (DVS, robotics, always-on) — SNN + Loihi-style hardware / memristor hybrid дают реальные преимущества (энергия/латентность). ([arXiv][106])
* Для **сложных perception / large-scale ML** пока чаще выигрывает ANN+quantization/AIHWKit/AIMC pipeline; SNN-подходы быстро улучшаются (surrogate gradients, e-prop), но требуют co-design. ([arXiv][103])
* Для исследования on-chip learning выбирайте платформы с программируемыми plasticity (Loihi), а для large-scale simulation/benchmarking — SpiNNaker / distributed digital platforms. ([Редвуд Центр Нейронаук][104])

---

<details>
<summary>Детали</summary>

* а) привести **практический рецепт** (шаблон) для перевода небольшой трансформер-подобной задачи в SNN-формат (кодирование, архитектура, обучение surrogate-grad),
* б) подготовить **сравнительную таблицу** энергопотребления / latency для типичных SNN-hardware (Loihi, TrueNorth, SpiNNaker, memristor prototypes) на реальных задачах (sensor fusion, keyword spotting) — с источниками

</details>

[101]: https://pubmed.ncbi.nlm.nih.gov/18275283/ "Spike timing-dependent plasticity: a Hebbian learning rule"
[102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7970006/ "Neural Coding in Spiking Neural Networks: A Comparative ..."
[103]: https://arxiv.org/abs/1901.09948 "Surrogate Gradient Learning in Spiking Neural Networks"
[104]: https://redwood.berkeley.edu/wp-content/uploads/2021/08/Davies2018.pdf "Loihi: A Neuromorphic Manycore Processor with On-Chip ..."
[105]: https://www.science.org/doi/10.1126/science.1254642 "A million spiking-neuron integrated circuit with a scalable ..."
[106]: https://arxiv.org/abs/2111.03746 "Efficient Neuromorphic Signal Processing with Loihi 2"
[107]: https://www.nature.com/articles/s41467-020-17236-y "A solution to the learning dilemma for recurrent networks of ..."
[108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10313197/ "Direct learning-based deep spiking neural networks: a review"
[109]: https://pubmed.ncbi.nlm.nih.gov/32681001/ "A solution to the learning dilemma for recurrent networks ..."
[110]: https://dynamicfieldtheory.org/upload/file/1631291311_c647b66b9e48f0a9baff/DavisEtAl2021.pdf "Advancing Neuromorphic Computing With Loihi: A Survey ..."
[111]: https://download.intel.com/newsroom/2021/new-technologies/neuromorphic-computing-loihi-2-brief.pdf "Taking Neuromorphic Computing with Loihi 2 to the Next ..."
[112]: https://eprints.soton.ac.uk/350493/ "SpiNNaker: a 1-W 18-core system-on-chip for massively ..."
[113]: https://www.mdpi.com/2079-4991/15/14/1130 "Memristor-Based Spiking Neuromorphic Systems Toward ..."
[114]: https://pubmed.ncbi.nlm.nih.gov/33513328/ "The Remarkable Robustness of Surrogate Gradient ..."

---

## 10. Мемристор-нейроморфные чипы: прототипы и демонстрации 


Ниже — детальное, технически насыщенное изложение экспериментальных прототипов memristor-нейроморфных чипов (in-situ обучение, приложения, системные демонстрации), с перечислением измеренных метрик, архитектурных деталей, ограничений и уроков для переноса в AIMC / LLM-контекст. Для каждого нагрузочного утверждения приведена ссылка на авторитетную публикацию (Nature / Nature Communications / PMC / IBM и т.д.).

---

### 10.0. Вводная мысль — почему прототипы важны

Экспериментальные демонстрации показывают не только proof-of-concept (что memristor arrays действительно могут хранить и манипулировать весами), но и дают реальные измерения: энергию программирования, скорость инференса, endurance, drift, влияние периферии, требования к калибровке и реальные практические сложности (sneak paths, line resistance, variability). Без этих данных архитектурный и алгоритмический co-design невозможен. ([Nature][115])

---

### 10.1. Prezioso et al., *Nature* 2015 — in-situ обучение в metal-oxide crossbar (single-layer perceptron)

#### Краткое описание эксперимента

Prezioso и соавторы продемонстрировали транзисторно-бесcтруктурный (1R) metal-oxide crossbar, в котором веса нейросети (single-layer perceptron) программировались непосредственно в кроссбаре и обучение выполнялось *in-situ* (coarse-grained delta rule). Авторы показали, что при контролируемой программировке и ограниченной вариабельности устройств можно реализовать корректную классификацию 3×3-пиксельных образов (буквы). ([Nature][115])

#### Технические детали и ключевые результаты

* **Топология:** пассивный crossbar (1R) на metal-oxide memristors, перекрёстки как синапсы; использование протоколов program/verify для установки conductance. ([Nature][115])
* **Обучение:** coarse-grained delta rule, применяемый на аппаратуре (не эмуляция): весовые обновления делались через программирование соответствующих ячеек в кроссбаре. ([Nature][115])
* **Метрики:** успешная классификация простых образцов; критическим оказался контроль variability и program/verify стратегия — без них точность резко ухудшается. ([Nature][115])

#### Выводы / уроки

1. *In-situ training в пассивных crossbar возможен* для простых сетей при условии строгого контроля device variability и программирования. ([Nature][115])
2. Program/verify — необходимый инструмент, но он увеличивает latency и write-energy, что ставит вопрос об endurance при масштабировании на большие модели. ([Nature][115])

---

### 10.2. Gao et al., *Nature Communications* 2022 — memristor-based auditory localization с in-situ training

#### Краткое описание и значение

Gao et al. продемонстрировали систему для звуковой локализации (brain-inspired sound localization), где memristor arrays использовались для аналоговой обработки и где часть обучения (в-situ) выполнялась на аппаратуре. Это один из наиболее зрелых application-level примеров применения memristive AIMC для реальной sensory-task с end-to-end demonstrator. ([Nature][116])

#### Технические детали и ключевые результаты

* **Архитектура:** memristor crossbars (скорее всего oxide/filamentary) для матричных операций в front-end, с периферией для интеграции/оцифровки; дизайн был ориентирован на low-energy реализацию слуховой обработки. ([Nature][116])
* **In-situ training:** авто-адаптация весов в железе с учётом device non-idealities; показано, что с hardware-aware процедурами можно достичь приемлемой точности локализации. ([Nature][116])
* **Энергия/производительность:** авторы подчёркивают энергоэффективность analog подхода для данной real-time задачи по сравнению с цифровыми реализациями (см. данные в статье). ([Nature][116])

#### Выводы / уроки

1. *Сенсорные, real-time приложения* (аудио, DVS vision) — «низко висящий плод» для memristor-AIMC: они требуют меньше точности весов, выигрывают от низкой латентности и sparse/event-driven представлений. ([Nature][116])
2. Демонстрации application-level важны, потому что показывают взаимодействие device-limits (drift, variability) с алгоритмами обучения в реалии. ([Nature][116])

---

### 10.3. Серия демонстраций 2020–2025: PCM / oxide-based чипы (Ambrogio 2023, Rasch 2024, ALBERT 2025 и др.)

#### 10.3.1. Ambrogio et al., *Nature* 2023 — 35M PCM devices, analog-AI chip (speech recognition)

* **Что:** масштабный аналог-AI кристалл с 35 миллионами PCM устройств, 34 tiles, с системной периферией и меж-tile коммуникацией; продемонстрирована реальная рабочая нагрузка (speech recognition) с высокой энергоэффективностью (до ~12.4 TOPS/W chip-sustained). ([Nature][117])
* **Почему важно:** показывает, что PCM-based AIMC может быть интегрирован в крупный банковый чип с межтайловой коммутацией и добиваться реальных системных выигрышей при правильно спроектированной периферии (charge integration, ramp→counter). ([Nature][117])

#### 10.3.2. Rasch et al., *Nature Communications* 2024 — алгоритмы и device-requirements для robust in-memory training

* **Что:** предложены алгоритмические улучшения для in-memory training и подробно исследованы ограничения (conductance noise, symmetry, retention, endurance), которые «сужают» выбор подходящих device-материалов для быстрого и робастного on-chip обучения. ([Nature][118])
* **Почему важно:** соединяет device-физику и алгоритмы, показывая конкретные числовые требования (noise, symmetry и т.п.), которые нужны, чтобы on-chip training был практически осуществим. ([Nature][118])

#### 10.3.3. Chen et al., *Nature Communications* 2025 — ALBERT на 14 nm analog inference chip (демонстрация трансформера)

* **Что:** (2025) демонстрация того, что слоя-за-слоем один слой ALBERT можно маппить на PCM-based analog inference chip, фактически показана совместимость AIMC с Transformer-классом моделей (proof-of-concept для LLM-scale inference на analog hardware). ([Nature][119])
* **Почему важно:** это первый открытый демонстратор трансформера (ALBERT) на реальном analog-chip’е и значимый шаг в направлении применения AIMC к LLM-задачам (хотя масштабы и детали организации меж-tile communication остаются критичными). ([Nature][119])

#### 10.3.4. Другие заметные работы 2020–2025

* **Song et al., Science 2024** — архитектурные/цифровые патчи для получения высокой точности при ограничениях analog memories (circuit+protocol level). ([Наука][120])
* **USC / Joshua Yang и др. (2024)** — схемы для повышения точности analog memories через архитектурные методы. ([USC Viterbi | School of Engineering][121])

#### Выводы / уроки 2020–2025

1. **Trend:** от small proof-of-concept (Prezioso 2015) → к application-level demonstrators (Gao 2022) → масштабным analog-chips (Ambrogio 2023) → Transformer demos (2025). Эти шаги показывают эволюцию: device → tile → system → model. ([Nature][115])
2. **Ключевое препятствие:** периферия, меж-tile communication и thermal/yield при 3D stacking остаются системными bottlenecks; алгоритмические улучшения (Rasch 2024) помогают смягчать device-требования, но не аннулируют их. ([Nature][118])

---

### 10.4. Таблица-сводка: ключевые прототипы (выборочно)

|  Год | Работа / демонстрация      | Технология                  |                       Масштаб / устройство | Ключевые результаты                                                                                          |
| ---: | -------------------------- | --------------------------- | -----------------------------------------: | ------------------------------------------------------------------------------------------------------------ |
| 2015 | Prezioso et al., *Nature*  | Metal-oxide 1R crossbar     | single layer perceptron (in-situ training) | Proof-of-concept in-situ learning; показана роль program/verify & variability. ([Nature][115])                 |
| 2022 | Gao et al., *Nat Commun*   | Oxide memristors (crossbar) |         auditory localization demonstrator | In-situ training for sound localization; energy-efficient sensor application. ([Nature][116])                  |
| 2023 | Ambrogio et al., *Nature*  | PCM arrays (35M devices)    |                    34 tiles analog-AI chip | System demo: speech recognition; up to ~12.4 TOPS/W; demonstrates scale & periphery design. ([Nature][117])    |
| 2024 | Rasch et al., *Nat Commun* | algorithm + device analysis |                                          — | Algos for robust in-memory training; device requirements (noise/symmetry/retention/endurance). ([Nature][118]) |
| 2025 | Chen et al., *Nat Commun*  | PCM analog inference chip   |                ALBERT layer mapped to chip | Proof-of-concept Transformer inference on analog chip (layer-by-layer mapping). ([Nature][119])                |

---

### 10.5. Ограничения, failure-modes и практические проблемы при масштабировании

1. **Variability & stochasticity:** устройство-уровневый разброс (D2D, C2C) требует программной/аппаратной компенсации (calibration, ensembles, HW-aware training). Это — первичная причина, почему многие прототипы используют program/verify и differential encoding. ([Nature][115])
2. **Endurance & write-energy:** массовые on-chip обновления (training) «съедают» ресурс устройств; практичные системы склонны к hybrid flows (off-chip pretrain → on-chip fine-tune / LoRA). ([Nature][118])
3. **Thermal coupling / Joule heating:** особенно для PCM и dense 3D stacks — локальный нагрев влияет на retention и drift, ухудшает yield; требует thermal sensors и throttling. ([Nature][117])
4. **Pериферия & inter-tile communication:** ADC/DAC и межтайловые каналы — значительная доля площади/энергии; эффективные решения (charge→time, ramp+counter, ADC-sharing) уменьшили проблему, но trade-offs сохраняются. ([Nature][117])

---

### 10.6. Рекомендации для разработчика/исследователя (практический чек-лист)

1. **Испытать device-suite в realistic protocol:** IV, endurance, retention, drift (R(t)), switching energy, set/reset distribution; использовать accelerated testing (Arrhenius) для retention. ([ResearchGate][122])
2. **Проектировать program/verify и differential encoding с учётом endurance:** планируйте frequency of writes и spare allocation; если нужны частые обновления — выбирать материалы с высокой endurance (или LoRA-workflow). ([Nature][118])
3. **Симулировать массивы с периферией:** Verilog-A device models → SPICE crossbar → system level (AIHWKit / CrossSim) для оценки real energy/latency. ([Nature][117])
4. **Выбрать target application правильно:** sensory / real-time / edge tasks дают лучшие шансы раннего успеха для memristor-AIMC; LLM-scale inference — достижимо, но требует 3D stacking + MoE + серьёзной архитектурной работы. ([Nature][116])

---

### 10.7. Заключение раздела

Экспериментальные демонстрации (Prezioso 2015 → Gao 2022 → Ambrogio 2023 → Rasch 2024 → Chen 2025 и др.) последовательно выводят memristor-AIMC из лабораторных концептов к системным demonstrator’ам. Они показывают реальную энергоэффективность и параллелизм analog VMM, но одновременно выявляют практические ограничения (variability, endurance, thermal, периферия), которые сегодня решаются комбинацией device-engineering, circuit-tricks и алгоритмического co-design. Для LLM-приложений текущий практически жизнеспособный маршрут — гибрид: цифровое pretrain → analog inference (tiles) + low-write adapters + MoE/3D stacking. ([Nature][115])

---

#### Основные использованные источники (чтобы открыть)

* Prezioso, M. *et al.* Training and operation of an integrated neuromorphic network based on metal-oxide memristors. **Nature** 2015. ([Nature][115])
* Gao, B. *et al.* Memristor-based analogue computing for brain-inspired sound localization with in-situ training. **Nature Communications** 2022. ([Nature][116])
* Ambrogio, S. *et al.* An analog-AI chip for energy-efficient speech recognition and transcription. **Nature** 2023. ([Nature][117])
* Rasch, M. J. *et al.* Fast and robust analog in-memory deep neural network training. **Nature Communications** 2024. ([Nature][118])
* Chen, A. *et al.* Demonstration of transformer-based ALBERT model on a 14 nm analog AI inference chip. **Nature Communications** 2025. ([Nature][119])
* Song, W. *et al.* Programming memristor arrays with arbitrarily high precision (Science, 2024). ([Наука][120])

---

<details>
<summary>Детали</summary>

* A) подготовить **CSV-таблицу** с точными числовыми метриками (energy per write/read/MAC, endurance, ON/OFF, tile size) для перечисленных работ (с DOI и ссылками), или
* B) сгенерировать **однотипный протокол воспроизводимости** (пошаговый) для демонстрации in-situ обучения на memristor crossbar (экспериментальный SOP)

</details>

[115]: https://www.nature.com/articles/nature14441 "Training and operation of an integrated neuromorphic ..."
[116]: https://www.nature.com/articles/s41467-022-29712-8 "Memristor-based analogue computing for brain-inspired ..."
[117]: https://www.nature.com/articles/s41586-023-06337-5 "An analog-AI chip for energy-efficient speech recognition ..."
[118]: https://www.nature.com/articles/s41467-024-51221-z "Fast and robust analog in-memory deep neural network ..."
[119]: https://www.nature.com/articles/s41467-025-63794-4 "Demonstration of transformer-based ALBERT model on a ..."
[120]: https://www.science.org/doi/10.1126/science.adi9405 "Programming memristor arrays with arbitrarily high ..."
[121]: https://viterbischool.usc.edu/news/2024/02/new-chip-design-to-enable-arbitrarily-high-precision-with-analog-memories/ "New Chip Design to Enable Arbitrarily High Precision with ..."
[122]: https://www.researchgate.net/publication/396011478_Demonstration_of_transformer-based_ALBERT_model_on_a_14nm_analog_AI_inference_chip "Demonstration of transformer-based ALBERT model on a ..."

---

## 11. Искусственные нейроны и bio-realistic building blocks 


Ниже — технически детализированное, практическое и документированное изложение по трём подпунктам: (11.1) «искусственные нейроны», соответствующие биологическим параметрам (что именно означают «параметры» и какие числа достижимы), (11.2) применение в bio-hybrid интерфейсах и энерго-чувствительных сенсорах, (11.3) как такие нейроны могут взаимодействовать с memristive «синапсами» и перспективы для BCI / нейропротезов. Все ключевые утверждения сопровождаются ссылками на современную, высокоцитируемую литературу (включая Fu et al., Nature Communications 2025), см. цитаты.

---

### 11.1. «Искусственные нейроны», соответствующие биологическим параметрам — что это значит и как достигнуто (Fu et al. 2025)

#### Что означает «соответствие биологическим параметрам»

Под «параметрическим соответствием» понимают одновременное приближение ключевых характеристик биологических нейронов:

* **амплитуда спайка (action potential)** — порядка десятков–сотен mV (биологические AP ≈70–130 mV);
* **токовые уровни, мембранное сопротивление** — биологические клетки реагируют на токи ≈наноампер (nA) и имеют большие input resistances (10⁷–10⁹ Ω);
* **энергия одного спайка** — порядка 0.3–100 pJ (оценки и диапазоны из физиологии);
* **временные характеристики** — rise/fall times, refractory periods и частотная чувствительность в биологическом диапазоне;
* **чувствительность к химическим модификациям (neuromodulators)** — возможность модуляции работы устройcтва через ионы/молекулы. ([Nature][123])

#### Что продемонстрировано в Fu et al. (Nature Commun. 2025) — конкретные числа

Fu и соавторы показали искусственный «neuron» на базе специально спроектированных memristor/органо-био гибридных слоёв, который:

* переключается при напряжениях **~60 mV** и рабочих токах порядка **~1.7 nA** — значения в биологическом диапазоне. ([Nature][123])
* имеет OFF-сопротивление порядка **~200 MΩ**, сопоставимое с величинами мембранного сопротивления в нейронах. ([Nature][123])
* обеспечивает временные формы и частотную реакцию, близкие к биологическим, и энергетику спайка, совместимую с биологическими уровнями (в литературных диапазонах ≈0.3–100 pJ). ([Nature][123])
* показывает возможность **химической модуляции** (реагирование на внеклеточные ионы/молекулы), что важно для bio-interfacing. ([Nature][123])

> Нагружающее утверждение: достижение рабочей точки ≈60 mV / ≈1–2 nA и высокое OFF-R — ключевой рычаг, позволяющий «подружить» электронику с биологией без масштабной усилительной электроники и без инвазивного воздействия на среду. ([Nature][123])

#### Как это сделано (технически, кратко)

* **Материалы/структура:** авторы используют memristor-структуры с функциональными нанопроводами / органическими компонентами (protein nanowires от Geobacter и т.п.), что снижает пороговые напряжения и увеличивает чувствительность при малых токах. ([Nature][123])
* **Динамика:** физика образования/разрыва нитей и их нестабильность/релаксация используются как аналог интеграции и «пороговой» генерации спайка (IF = integrate-and-fire). ([Nature][123])

---

### 11.2. Применение таких нейронов в bio-hybrid интерфейсах и энерго-чувствительных сенсорных системах

#### Почему соответствие параметрам важно для интерфейсов

* **Без усилителей/конвертеров:** если амплитуда и импеданс искусственного нейрона близки к биологическим, сигнал можно передавать/принимать напрямую (минимум электроники между тканью и вычислителем) → снижение латентности, шумов и энергозатрат, более компактный интерфейс. Fu et al. прямо демонстрируют соединение искусственного нейрона с биоклеткой в реальном времени. ([Nature][123])

#### Технологии, подходящие для bio-hybrid сенсорики

* **Organic electrochemical transistors (OECTs)** и органо-гибридные memristive устройства — они работают при низких напряжениях, биосовместимы и часто демонстрируют neuron-like динамику (в т.ч. single-transistor artificial neurons). Конкретные демо и обзоры OECT-нейронов появились в 2022–2025. ([Nature][124])
* **Protein-nanowire/biomaterial-enhanced memristors** — пример Fu et al. — дают низкие пороги и работают в bio-амплитудном режиме. ([Nature][123])

#### Примеры приложений

* **In situ sensing + preprocessing:** сенсор → artificial neuron (event detection, thresholding/spiking) → memristive synapse → local decision (низкая латентность, low-power). Особенно подходит для всегда-on biosensing, wearable devices, implantable monitors. ([Nature][123])
* **Neuromodulated sensing:** устройство реагирует на ионные концентрации/нейромедиаторы (chemically gated response) — путь к ситуационной адаптации (например, менять чувствительность при воспалении/изменении pH). Fu et al. демонстрируют такое химическое модулирование. ([Nature][123])

---

### 11.3. Взаимодействие искусственных нейронов с memristive синапсами: перспективы для BCI / нейропротезов

#### Физические интерфейсы нейрон ↔ синапс (упрощённая схема)

1. **Биологический нейрон (extracellular electrode)** генерирует EPSC/IPSC (nA, ms).
2. **Искусственный нейрон (bio-amplitude memristor / OECT)** интегрирует входный ток/напряжение; при достижении порога генерирует spike-поток (на напряжениях и токах, совместимых с биологией). ([Nature][123])
3. **Memristive синапс** (на crossbar-tile) преобразует spike в conductance-change (weight) или в аналоговый current для передачи дальше; может реализовывать STDP/учебные правила при нужной программатике импульсов. ([Nature][125])

#### Как реализовать обучение STDP / plasticity на таком стеке

* **Пульс-кодирование:** pre/post spikes формируют перекрывающиеся стимулы на memristor, индуцирующие асимметричные изменения conductance (ΔG от временной разницы) — стандартный аппаратный путь к STDP. Требуются уровни напряжения/тока, согласованные между искусственным нейроном и memristor-синапсом. ([Nature][125])
* **Аддитивные vs метапластичность:** использование контролируемых verify-пассажей и adaptive pulse patterns + software/hardware co-design (ALGORITHMS для компенсирования drift/variability) — см. обзор по memristor-ANN. ([Nature][125])

#### Преимущества для BCI и нейропротезов

* **Латентность и энергия:** прямой bio-amplitude путь сокращает электронику между тканью и вычислителем → меньше delay и энергии, что критично для closed-loop stimulation. ([Nature][123])
* **Local learning / adaptation:** on-device plasticity (memristor-синапсы + local artificial neurons) позволяет адаптироваться к изменениям имплантата/ткани без постоянной связи с облаком. Это важно для долгосрочной стабильности и персонализации. ([ACS Publications][126])

#### Ограничения и риски (технические, клинические)

* **Долговечность / drift / биосовместимость:** memristive материалы и органические компоненты требуют долгосрочной проверки (коррозия, воспаление, деградация, drift conductance). Fu et al. отмечают перспективы, но подчёркивают необходимость тестов на стабильность. ([Nature][123])
* **Шумы / SNR / false-positives:** биологический сигнал слаб и шумен — требуется продуманная схемотехника (фильтрация, адаптивные thresholding, event-detection) и умелая co-design аппаратуры и алгоритмов. ([ACS Publications][126])
* **Безопасность и регулирование:** для имплантов требуется соблюдение медрегуляций (ISO/IEC/medical device standards), электростимуляция должна быть в безопасных диапазонах; разработчики обязаны планировать валидацию и клинические испытания. (обзор интерфейсов и требования см. Rana 2024). ([ACS Publications][126])

---

### Практические рекомендации / дорожная карта для исследователя / инженера

1. **Определите target-интерфейс (extracellular vs intracellular, acute vs chronic)** и подбирайте материалы (OECT / bio-nanowire memristor) в соответствии с требованиями. ([Nature][124])
2. **Стандартные числа для целевой аппаратуры:** ориентируйтесь на пороги <130 mV и токи ~nA, OFF-R ≳10⁸ Ω для прямой совместимости; Fu et al. дают рабочие примеры ≈60 mV / 1.7 nA / 200 MΩ. ([Nature][123])
3. **Совместимая периферия:** предусмотреть adaptive-gain readout и защиту от transients (stimulation artefacts), а также thermal/chemical stability tests. ([Nature][127])
4. **Оптимизировать учёт non-idealities:** моделируйте drift, variation, write-endurance и разрабатывайте program/verify, redundancy, differential encoding, а также hardware-aware learning для компенсации. ([Nature][125])
5. **Планируйте валидацию:** biologically-relevant tests (acute cell coupling, chronic implant animal studies), биосовместимость, и соответствие медицинским стандартам. ([Nature][123])

---

### Ключевые источники (must-read для раздела 11)

* Fu S. et al., *Constructing artificial neurons with functional parameters comprehensively matching biological values*, **Nature Communications** (2025). — демонстрация bio-amplitude memristor-neurons, chemical neuromodulation, cell-device coupling. ([Nature][123])
* Ji J. et al., *Single-transistor organic electrochemical neurons* (Nature Communications, 2025) — OECT-based artificial neurons и их применимость для bio-interfacing. ([Nature][124])
* Yao Y. et al., *An organic electrochemical neuron for a neuromorphic…* (PNAS, 2025) — архитектуры OECN для sensing/biointerfacing. ([PNAS][128])
* Aguirre F. et al., *Hardware implementation of memristor-based artificial neural networks* (Nature Communications review, 2024) — обзор memristor-hardware, применим для понимания синаптической стороны. ([Nature][125])
* Rana D., *Neural vs Neuromorphic Interfaces: Where Are We Standing?* (ACS Chem Rev, 2024) — обзор нейро-гибридных интерфейсов, биосовместимости и translational challenges. ([ACS Publications][126])
* Pawlak W. A. et al., *Neuromorphic algorithms for brain implants: a review* (2025) — алгоритмические требования для BCI/implantable neuromorphic systems. ([PMC][129])
* Hodgkin A. L., Huxley A. F., *A quantitative description of membrane current...* (1952) — классика физиологии, опорная точка для всех биологических параметров. ([PMC][130])

---

### Краткое заключение

* **Технический прорыв Fu et al. (2025)** показал, что параметрическое (амплитуда, ток, энергия, временные константы) приближение искусственных нейронов к биологическим уровням — реальная возможность, что открывает путь к более простым и энерго-эффективным bio-interfacing решениям. ([Nature][123])
* **Практическая интеграция** artificial neurons + memristive synapses обещает мощные, локально обучаемые, low-power нейро-интерфейсы (BCI, нейропротезы, in-sensor neuromorphic preprocessing), но требует системного решения проблем долговечности, биосовместимости и регулирования. ([Nature][125])

---

<details>
<summary>Детали</summary>

* A) подготовить **техническую сводную таблицу** (CSV) с целевыми биологическими числами (AP amplitude, spike energy, input resistance, typical currents) и соотношением к опубликованным характеристикам Fu 2025 + OECT демо;
* B) сгенерировать **схематическую аппликацию** (блок-диаграмма) для BCI: electrode → artificial neuron (memristor/OECT) → memristor crossbar (synapses) → local learning loop + stimulator; с указанием примерных уровней V/I; 

</details>

[123]: https://www.nature.com/articles/s41467-025-63640-7 "Constructing artificial neurons with functional parameters comprehensively matching biological values | Nature Communications"
[124]: https://www.nature.com/articles/s41467-025-59587-4 "Single-transistor organic electrochemical neurons"
[125]: https://www.nature.com/articles/s41467-024-45670-9 "Hardware implementation of memristor-based artificial ..."
[126]: https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00862 "Neural vs Neuromorphic Interfaces: Where Are We Standing?"
[127]: https://www.nature.com/articles/s41528-025-00472-x "A fully-integrated flexible in-sensor computing circuit based ..."
[128]: https://www.pnas.org/doi/10.1073/pnas.2414879122 "An organic electrochemical neuron for a neuromorphic ..."
[129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12021827/ "Neuromorphic algorithms for brain implants: a review - PMC"
[130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1392413/ "A quantitative description of membrane current and its ..."

---

## 12. Training на memristor-платформах: in-situ (on-chip) vs off-chip pretraining 


Ниже — технически детализированный разбор существующих алгоритмов и аппаратных схем обучения на memristor/AIMC-платформах, рабочие паттерны (hybrid / full on-chip), реальные ограничения (endurance, write-energy, latency, retention, variability) и практические рекомендации для попытки обучения больших моделей (включая LLM). Для ключевых утверждений приведены современные, авторитетные источники (Nature / NatCommun / крупные обзоры / инструменты) — см. цитаты.

---

### 12.1 In-situ (on-chip) алгоритмы: STDP, аппаратные варианты градиента, coarse-grained delta rule

#### 12.1.1 Классификация in-situ алгоритмов

1. **Локальные правила (event-driven, unsupervised):** STDP / Hebbian-like обновления, реализуемые пересечением pre/post-пульсов — просты аппаратно и применимы для SNN / локальных задач. (подходит для low-precision sensing/edge).
2. **Coarse-grained delta / perceptron-style in-situ:** исторический пример — Prezioso et al. (2015): in-situ обучение single-layer perceptron прямо в metal-oxide crossbar с использованием program/verify и delta-rule-похожей процедуры. Это реальный proof-of-concept для аппаратного обучения, но масштабируется с трудом на глубокие сети без алгоритмической помощи. ([Nature][131])
3. **Outer-product / coincidence-based updates (stochastic pulse trains):** идея Gokmen & Vlasov (Tiki-Taka family): градиентную outer-product-update вычислять полностью в памяти с помощью генерации стохастических пульсов и их совпадения — параллельно по всей матрице. Это даёт константное по размеру время обновления, но требует специальных свойств устройств или алгоритмических компенсаторов. ([arXiv][132])
4. **Алгоритмы для реальных неидеальностей:** TTv2 (Tiki-Taka v2) и его модификации (c-TTv2, AGAD) — направления, усиливающие устойчивость к асимметрии, смещению симметричной точки (reference) и шуму. Rasch et al. (2024) предложили c-TTv2 и AGAD, которые значительно снижают требования к «идеальности» reference-устройств и расширяют набор пригодных материалов. AGAD, например, вычисляет динамический reference «на лету» (on-the-fly), что снимает потребность в точной предварительной программировке reference-массива. ([PMC][133])

#### 12.1.2 Техническая механика hardware-gradient / in-memory update

* **Outer-product update:** реализуется как параллельное суммирование импульсов, где внешний ток/напряжение кодирует активации и ошибки; совпадения дают ΔG для каждого элемента одновременно (O(1) по времени для матрицы). Это минимизирует цифровую работу, но чувствительно к non-ideal device-response. ([PMC][133])
* **Pulse-engineering и program/verify:** для точного ΔG часто применяют последовательности пульсов (staircase, verify loops). Это уменьшает программировочную ошибку, но увеличивает write-latency и write-energy. Prezioso демонстрировал практическое применение program/verify в 1R crossbar. ([Nature][131])
* **Двойная-матрица / residual approach (Tiki-Taka):** хранение дополнительного массива («residual» или reference) и попеременное обновление основной и вспомогательной матриц, что компенсирует асимметрию и drift. Это добавляет area и дизайн-сложность, но улучшает сходимость. ([arXiv][132])

#### 12.1.3 Примеры и измеренные характеристики (из практики)

* Rasch et al. (2024) оценили алгоритмы c-TTv2 и AGAD: AGAD демонстрирует runtime ≈**62.1 ns** для обновления 512×512 матрицы (оценка для выбранных гиперпараметров) по сравнению с >3000 ns при полном цифровом накоплении градиента — демонстрация огромного теоретического ускорения. Однако это число опирается на допущения о t_single_pulse и архитектуре периферии. ([PMC][133])
* Rasch также подсчитал «пульсы на пример» для разных массивов: устройства для **градиентного аккумулятора** могут получать **0.5–4 pulses** на входной пример, тогда как устройства, которые представляют сами веса, получают примерно **2·10⁻⁴ … 4·10⁻⁴ pulses** на пример (т.е. обновление весов происходит значительно реже). Это подчёркивает, что требования по endurance различны для различных классов массивов. ([PMC][133])

---

### 12.2 Off-chip pretraining → on-chip mapping (практическая рабочая стратегия)

#### 12.2.1 Почему hybrid-workflow — практичный стандарт сегодня

* Полное on-chip BP для больших DNN/LLM требует огромного числа обновлений весов (много write-циклов), высоких требований к симметрии/retention/endurance и большой периферии. Поэтому индустрия и академия приходят к рабочему паттерну: **предобучение (pretrain) off-chip на GPU/TPU → квантизация / hardware-aware fine-tuning → маппинг и частичная on-chip адаптация (LoRA/адаптеры/low-rank) / inference на AIMC**. Этот путь минимизирует число on-chip записей и переводит большую часть write-нагрузки в цифровую среду. ([IBM Analog Hardware Acceleration Kit][134])
* Кроме того, LoRA / Low-rank adapters и другие параметрические методы сокращают число параметров для обновления on-device (orders-of-magnitude меньше, чем full-BP), что делает on-chip fine-tuning реалистичным даже при ограниченной endurance. ([IBM Analog Hardware Acceleration Kit][134])

#### 12.2.2 Конкретный pipeline (рекомендуемая практическая последовательность)

1. **Full pretrain (cloud/GPU/TPU):** получить исходную модель (FP32/FP16).
2. **Hardware-aware offline retraining:** QAT и аппарат-aware noise injection (имитировать conductance noise, drift, nonlinearity) — цель: «перенести» устойчивость к non-idealities в веса. Инструменты: IBM AIHWKit (для эмуляции AIMC) и CrossSim / MNSIM. ([IBM Analog Hardware Acceleration Kit][134])
3. **Pruning / sparsity / LoRA / adapters:** сократить число on-device параметров; подготовить low-rank-адаптеры для on-device fine-tune. ([IBM Analog Hardware Acceleration Kit][134])
4. **Tile mapping & partitioning:** разбить матрицы трансформера (dense/FFN/проекционные слои) между crossbar-тайлами с учётом размерности ADC/DAC и меж-тайловых каналов; учесть битность и схему differential encoding. (см. Ambrogio et al. 2023 по межтайловой коммутации). ([Nature][135])
5. **Final on-chip fine-tune (low-write):** адаптация LoRA/адаптеров, calibration, и/или ограниченная in-situ training (если endurance и write-energy позволяют). Использовать AGAD/c-TTv2/TTv2-family или MP-hybrid в зависимости от device-properties. ([PMC][133])

#### 12.2.3 Инструменты и эмуляторы, необходимые в pipeline

* **AIHWKit (IBM)** — open-source toolkit для эмуляции AIMC, QAT и mapping. ([IBM Analog Hardware Acceleration Kit][134])
* **CrossSim (Sandia)** — crossbar-симулятор; полезен для accuracy/sensitivity analysis на уровне device→array. ([GitHub][136])
* **MNSIM / CIM-SIM / другие** — поведенческие симуляторы для системного анализа (latency, throughput, energy). ([GitHub][137])

---

### 12.3 Ограничения: endurance, write-energy, programming latency — влияние на возможность полного on-chip BP для LLM

#### 12.3.1 Endurance (жизненный цикл записи)

* **Нерaвномерность требований:** как показывает Rasch (2024), разные массивы в архитектуре имеют категорически разные требования: массивы для временного накопления градиента (gradient accumulators) требуют высокой endurance (несколько пульсов на input sample), тогда как массивы, в которых хранятся окончательные веса, обновляются очень редко (≈10⁻⁴–10⁻³ pulses/sample в их симуляциях), т.е. endurance для основных весов может быть значительно ниже, если используются правильные алгоритмы и редкие обновления. Это даёт шанс для гибридного подхода. ([PMC][133])
* **Диапазон endurance по технологиям:** обзоры показывают широкие диапазоны: PCM — от ~10⁶ до >10¹² в зависимости от структуры и материалов; RRAM — варианты с endurance от 10³ до 10¹²; ECRAM / FEFET / MRAM могут иметь лучшие циклы (вплоть до 10¹²) в отдельных отчётах. Следовательно, конкретная feasibility сильно зависит от выбранного device и его реализации. (обзоры: Ielmini 2024 / Boniardi 2024 и др.). ([ACS Publications][138])

#### 12.3.2 Write-energy и программировочная латентность

* **Write-energy (порядки величин):** современные оценки и эксперименты дают диапазон от <<1 pJ (проектные PCM / superlattice с очень коротким pulse) до сотен pJ / nJ в более консервативных реализациях. Например, Wu et al. (2024) проецируют reset-energy ≈**0.15 pJ** при 2 ns pulses для 40 nm superlattice PCM; практические разработки (Ambrogio 2023) используют pulse widths порядка **tens of ns** и энергию на обновление выше, но всё же дающую значительное преимущество над цифровыми write-операциями. ([Nature][139])
* **Programming latency:** pulse-widths в литературе варьируют: от **несколько ns** (новые экспериментальные PCM) до **10s–100s ns** (частые отчёты) и даже µs-уровня в некоторых RRAM/PCM экспериментальных сетапах; общая задержка программирования включает verify-loops и периферийную конвертацию (ADC/DAC), поэтому practical latency на одно обновление может быть существенно больше одного физического p-пульса. Эти параметры напрямую влияют на throughput при on-chip BP. ([tsapps.nist.gov][140])

#### 12.3.3 Implication for full on-chip BP для LLM

1. **Write-count problem:** обучение LLM (полный BP) включает огромное число весовых обновлений (billion-parameter models, миллионы батчей): даже при малой частоте обновлений per-parameter суммарные записи будут огромны → требования к endurance и управлению износа критичны. Rasch показывает, что некоторые алгоритмы значительно уменьшают write-нагрузку (разделение ролей массивов, AGAD), но не устраняют её полностью. ([PMC][133])
2. **Write-energy × throughput:** для on-chip BP требуется одновременно высокая скорость программирования и низкая энергия; многие device-технологии ещё не дают этой комбинации в крупном масштабе (хотя advanced PCM/PCM-superlattices и ECRAM демонстрируют обещающие числа). Ambrogio-chip показывает, что масштабные аналоговые чипы возможны, но их primary цель — inference; full-scale training остаётся трудной задачей. ([Nature][135])
3. **Периферия и digital-overhead:** даже если crossbar делает MVM быстро, gradient accumulation, normalization, BatchNorm/LayerNorm/softmax и другие «utility» операции часто выполняются в цифровой части; это снижает общий выигрыш и увеличивает write-latency/energy при попытке полного on-chip BP. Rasch оценивает, что алгоритмы AGAD/c-TTv2 минимизируют эти эффекты, но цифровые utility-операции остаются. ([PMC][133])

#### 12.3.4 Практический вывод

* **Для LLM-scale моделей сегодня наиболее жизнеспособна схема:** off-chip full pretrain → HW-aware retrain & quantize → on-chip analog inference; для адаптации/персонализации — on-chip low-write fine-tune (LoRA / adapters) или ограниченная in-situ training с AGAD / c-TTv2 на специально выбранных массивах (gradient accumulators из высоко-endurance устройств). Полное on-chip BP для больших LLM требовательно к материалам (выше endurance, низкая write-energy, быстрые p-pulses, стабильный reference) и к архитектуре периферии — и пока остаётся исследовательской целью, но не общепромышленной практикой. ([PMC][133])

---

### 12.4 Практические рекомендации / чек-лист для реализации обучения на memristor-платформе

1. **Провести device-audit:** измерить ΔG per pulse, asymmetry, drift, retention, endurance, write-energy и минимальный pulse-width; сравнить с требованиями алгоритмов (Rasch даёт числовые требования для AGAD/c-TTv2). ([PMC][133])
2. **Выбрать алгоритм под device-свойства:**

   * если devices **асимметричны** → Tiki-Taka/TTv2 family или AGAD;
   * если devices очень симметричны и стабильны → in-memory SGD / direct analog SGD;
   * если endurance ограничена → hybrid MP (grad accumulation digital) + rare analog writes. ([arXiv][132])
3. **Разделить массивы по ролям:** использовать высоко-endurance материалы/структуры для gradient-accumulators и low-retention/high-speed материалы для временных массивов; хранение окончательных весов в low-update режиме. Rasch подчёркивает стратегию «не все массивы равны». ([PMC][133])
4. **Использовать инструменты эмуляции:** AIHWKit, CrossSim, MNSIM — симулировать full pipeline (training+mapping+periphery) до изготовления прототипа. ([IBM Analog Hardware Acceleration Kit][134])
5. **Планировать wear-leveling и fault tolerance:** wear-leveling, spare-allocation, вероятностное кодирование и периодический remapping важны для продления life-time. ([arXiv][141])
6. **Разработать realistic benchmarking:** energy/MAC, end-to-end latency, accuracy (SWeq), write-counts per epoch, estimated lifetime при заданном наборе задач. Сравнивать с GPU/TPU на одном и том же наборе метрик. ([Nature][142])

---

### 12.5 Короткое резюме (takeaways)

* **In-situ training** на memristor-массивах возможен и даёт огромное теоретическое ускорение (orders-of-magnitude) для обновления весов/outer-product, если использовать pulse-coincidence и специализированные алгоритмы (Tiki-Taka, AGAD, c-TTv2). Однако реальные device-non-idealities (asymmetry, drift, variability), периферия и endurance ограничивают практическую применимость в больших масштабах. ([arXiv][132])
* **Hybrid workflow** (off-chip pretrain → hardware-aware retrain → analog inference + low-write on-chip fine-tune) — текущий промышленно-ориентированный путь для LLM/AIMC. ([IBM Analog Hardware Acceleration Kit][134])
* **Ключевые барьеры для full on-chip BP LLM:** endurance (суммарные записи), write-energy и latency (program/verify), а также системная сложность периферии и inter-tile communication. Алгоритмы последних лет (AGAD, c-TTv2) заметно снижают требования, но не устраняют их полностью. ([PMC][133])

---

### 12.6 Основные источники (для чтения и цитирования)

* Prezioso M., *et al.*, **Training and operation of an integrated neuromorphic network based on metal-oxide memristors**, *Nature* 2015. (coarse-grained in-situ delta rule demo). ([Nature][131])
* Rasch M. J., *et al.*, **Fast and robust analog in-memory deep neural network training**, *Nature Communications* 2024 — AGAD, c-TTv2, device-requirements, runtime/energy/endurance analysis. (PMC open access). ([PMC][133])
* Gokmen T., Haensch W., **Tiki-Taka algorithm / TTv2** family — algorithmic approach to overcome device asymmetry (arXiv / Frontiers). ([arXiv][132])
* Ambrogio S., *et al.*, **An analog-AI chip for energy-efficient speech recognition and transcription**, *Nature* 2023 — крупномасштабный PCM analog-chip (35M devices), примеры системных trade-offs. ([Nature][135])
* IBM AIHWKit (docs + GitHub) — toolkit для hardware-aware training / simulation / mapping. ([IBM Analog Hardware Acceleration Kit][134])
* CrossSim (Sandia) и MNSIM (Tsinghua) — симуляторы crossbar / memristor для accuracy/throughput modeling. ([GitHub][136])
* Обзоры device/architectural: Aguirre F. *et al.*, **Hardware implementation of memristor-based ANNs** (NatCommun review 2024); Ielmini D., **RRAM review** (2024) — по физике, endurance и практическим параметрам. ([Nature][142])

---

<details>
<summary>Детали</summary>

A)  **сводную таблицу (CSV)** с числовыми метриками (endurance, typical write-energy, pulse-width, ΔG per pulse, типичные pulse-counts per sample из Rasch) для ключевых device-семейств (PCM, RRAM, ECRAM, FEFET), с источниками;
B)  **пошаговый pipeline** (код/скрипт) для «pretrain → AIHWKit HW-aware retrain → map → CrossSim validation» (включая примеры команд и конфигов);
C)  **сводку-рекомендаций** (1-page) для руководителя проекта, чтобы принять решение: «стоит ли инвестировать в full on-chip training для LLM сейчас» (риски/пороговые требования/ROI).

</details>


[131]: https://www.nature.com/articles/nature14441 "Training and operation of an integrated neuromorphic ..."
[132]: https://arxiv.org/abs/1909.07908 "Algorithm for Training Neural Networks on Resistive Device Arrays"
[133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335942/ "Fast and robust analog in-memory deep neural network training - PMC"
[134]: https://aihwkit.readthedocs.io/ "IBM Analog Hardware Acceleration Kit's documentation!"
[135]: https://www.nature.com/articles/s41586-023-06337-5 "An analog-AI chip for energy-efficient speech recognition ..."
[136]: https://github.com/sandialabs/cross-sim "sandialabs/cross-sim: CrossSim: accuracy simulation of ..."
[137]: https://github.com/thu-nics/MNSIM-2.0 "thu-nics/MNSIM-2.0: A Behavior-Level Modeling ..."
[138]: https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00845 "Resistive Switching Random-Access Memory (RRAM)"
[139]: https://www.nature.com/articles/s41467-023-42792-4 "Novel nanocomposite-superlattices for low energy and ..."
[140]: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957911 "Low-Energy Spiking Neural Network using Ge4Sb6Te7 ..."
[141]: https://arxiv.org/abs/2010.02825 "WoLFRaM: Enhancing Wear-Leveling and Fault Tolerance in Resistive Memories using Programmable Address Decoders"
[142]: https://www.nature.com/articles/s41467-024-45670-9 "Hardware implementation of memristor-based artificial ..."

---


## 13. Алгоритм–железо co-design: non-ideality-aware training, quantization, sparsity, LoRA/LoHA 

Ниже — подробный практический и научно-обоснованный разбор техник co-design для переноса и эксплуатации больших нейросетей (включая трансформеры/LLM) на аналоговых / мемристорных платформах. Для каждого подпункта даю: (1) принцип, (2) почему это важно для AIMC, (3) конкретные методы и hyper-параметры, (4) примеры инструментов/реализаций и литературы.

> Краткое содержание (takeaways):
> *Hardware-aware / non-ideality-aware обучение и адаптация (QAT, noise injection, LoRA-подходы) — обязательный этап для успешного переноса моделей на AIMC;* инструменты типа IBM AIHWKit и AIHWKit-Lightning уже реализуют большинство приёмов. ([IBM Analog Hardware Acceleration Kit][143])

---

### 13.1. Non-ideality-aware training (включение шумовой/вариабельной модели в тренировочный цикл)

#### 13.1.1. Что такое non-ideality-aware (hardware-aware) training

Hardware-aware (HWA) или non-ideality-aware обучение — это включение моделей физических ошибок/ограничений устройства (шум, D2D вариабельность, drift, асимметрия ΔG/пульс, конечная дискретность, ограниченный диапазон conductance и периферийные артифакты ADC/DAC) прямо в цикл обучения (forward/backward) или в процедуру fine-tuning, чтобы сеть «пережила» реальные ошибки на железе. Это может быть: инъекция шума в веса/partial sums, имитация ограничений динамического диапазона, моделирование drift/retention, моделирование ADC quantization и т.д. ([IBM Analog Hardware Acceleration Kit][143])

**Зачем это нужно.** Без HWA-retraining даже хорошо предобученные сети часто теряют точность при маппинге в AIMC из-за систематических смещений и стохастики аппаратуры. HWA-training обычно возвращает «software-equivalent» или близкую точность на target-hardware. ([Nature][144])

#### 13.1.2. Какие non-idealities моделировать (порядок приоритета)

1. **Device noise & D2D variability** (статическая разброска conductance).
2. **ΔG nonlinearity и асимметрия отклика на set/reset (update asymmetry).**
3. **Drift / retention (временная эволюция conductance).**
4. **Finite conductance range & resolution (ON/OFF span, number of distinguishable states).**
5. **ADC/DAC quantization & ENOB, peripheral latency.**
6. **Wire resistance / IR drop / sneak paths (в больших tiles).**
7. **Programming stochasticity (ΔG per pulse distribution) и verify-loops effects.**
   Модель каждого эффекта должна быть статистической (sampling из эмпирических PDF), либо приближённой физической (Verilog-A/behavioral). ([IBM Analog Hardware Acceleration Kit][143])

#### 13.1.3. Как включать моделирование в цикл обучения (практические шаблоны)

* **Training-time noise injection (forward pass).** На каждом батче перед вычислением loss подмешивать к весам/partial-sums шум по эмпирическому распределению: ( $\tilde W = W + \epsilon_W, \ \epsilon_W \sim P_{\rm device}$ ). Это имитирует статическую/динамическую вариабельность. Хорошая практика — anneal амплитуду шума к концу retrain. ([Nature][144])
* **Quantization & ADC model in forward.** Эмуляция ADC (ENOB, non-linearities) и DAC (pulse-width limits) в forward; при backprop применять surrogate-gradients для non-differentiable quantizers. ([IBM Analog Hardware Acceleration Kit][143])
* **Drift/Retention augmentation (temporal augmentation).** Эмулировать drift как multiplicative/logarithmic shift ( $G(t)=G_0 \cdot f(t)$ ) и периодически оценивать стабильность — useful для long-term deploy. ([Nature][144])
* **Device update model in optimizer (update asymmetry).** Включать модель ΔG( pulse, polarity, current state ) в step-функцию: вместо цифрового ( $W \leftarrow W - \eta \nabla W$ ) симулировать эквивалентный набор p-пульсов с ассиметричным ΔG. Это особенно важно для in-situ training/outer-product updates. ([arXiv][145])

#### 13.1.4. Реализации и инструменты

* **IBM AIHWKit** — содержит presets устройств, noise models, analog update optimizers (plain SGD analog outer-product, mixed-precision etc.) и готовые HWA-pipelines. Это основной production-уровнев инструмент. ([IBM Analog Hardware Acceleration Kit][143])
* **AIHWKit-Lightning** — оптимизированный стек для масштабной HWA-тренировки (LLM-scale), интегрирует ускоренные HWA-операции. ([IBM Research][146])
* **Rasch et al. / Le Gallo et al.** — демонстрируют методологии HWA-retraining и числовые эффекты non-idealities на accuracy. ([Nature][147])

#### 13.1.5. Практические hyper-параметры / рецепты

* **Noise schedule:** стартовая σ_noise = 0.5–1.5× empirical device σ, постепенно уменьшать до measured value; batch-wise noise лучше, чем per-step fixed. ([Nature][144])
* **Calibration loop:** после HWA-retrain выполнить tile-level calibration (bias/scale per column), затем ещё короткий fine-tune с малым LR (1e-5…1e-6). ([IBM Analog Hardware Acceleration Kit][143])
* **Surrogate gradients** для non-differentiable mappings (quantizers, pulse discreteness) — используйте smoothed approximations (e.g., straight-through estimator или sigmoid surrogate). ([IBM Analog Hardware Acceleration Kit][143])

---

### 13.2. Quantization-aware training, mixed-precision, stochastic rounding

#### 13.2.1. Роль QAT и mixed-precision в AIMC

Quantization-aware training (QAT) адаптирует модель к малобитным представлениям (DAC/ADC битность, partial-sum precision) и часто используется совместно с HWA-training. Mixed-precision (например, 4–8-bit для analog partial sums, 16-bit for accumulators) — распространённая стратегия для минимизации периферийных затрат при сохранении точности. ([IBM Analog Hardware Acceleration Kit][143])

**Почему важно для AIMC.** Analog arrays обычно «работают» с ограниченной ENOB и частыми low-bit ADC; QAT делает модель устойчивой к этой дискретизации и позволяет уменьшить требования к периферии. ([IBM Analog Hardware Acceleration Kit][143])

#### 13.2.2. Stochastic rounding — зачем и как

* **Идея:** вместо deterministic rounding to nearest, применять вероятностный выбор соседних representable значений с вероятностью, пропорциональной расстоянию. Это предотвращает «stagnation» при малых апдейтах и сохраняет unbiasedness в ожидании. Показано (Gupta et al., 2015), что stochastic rounding позволяет тренировать при очень низкой точности без деградации. ([arXiv][148])
* **Применение в AIMC:** stochastic rounding на уровне ADC/DAC/accumulators и в цифровых частях при mixed-precision accumulation уменьшает bias от малых update и важен при low-precision gradient accumulation. ([PMC][149])

#### 13.2.3. Практические техники QAT для AIMC

1. **Range-and-scale calibration:** выбрать динамический диапазон (clipping) для каждого layer/tile так, чтобы максимальное значение входа использовало доступный conductance-range; часто полезно per-channel scaling. (см. dynamic quantization range control для AIMC). ([lirias.kuleuven.be][150])
2. **Fake-quantization in forward + straight-through or surrogate in backward.** Типичный QAT-шаблон, реализован в AIHWKit. ([IBM Analog Hardware Acceleration Kit][143])
3. **Mixed precision placement:** держать activation/partial sums quantized to low bits (4–6 bits) на analog path; acumulation & layernorm/softmax — в higher precision (16–32 bit) в цифровом домене. Это отражает реальные trade-offs периферии. ([IBM Analog Hardware Acceleration Kit][143])
4. **Use stochastic rounding for accumulators & small updates.** Например, применять stochastic rounding for gradient accumulation to avoid losing tiny but many updates. ([arXiv][148])

#### 13.2.4. Инструменты и реализации

* **AIHWKit** имеет QAT/analog-quantization presets и опционы для stochastic rounding / fake-quant. ([IBM Analog Hardware Acceleration Kit][143])
* **Research papers** по dynamic range control и QAT-flows для AIMC (Laubeuf 2022, Rasch et al.) дают практические рекомендации по выбору битности и clipping ranges. ([lirias.kuleuven.be][150])

---

### 13.3. Low-rank adapters (LoRA) / LoHA и другие техники для эффективной адаптации LLM под AIMC

#### 13.3.1. Идея LoRA / зачем это критично для AIMC

LoRA (Low-Rank Adaptation) — метод параметрической и вычислительно эффективной дообучки: предобученная матрица (W) остаётся фиксированной, а добавляются небольшие low-rank модули ( $\Delta W = A B$ ) (rank r ≪ d), которые обновляются при fine-tuning. LoRA резко уменьшает число параметров, которые нужно хранить/обновлять on-device. Это критично для AIMC, потому что: (a) уменьшает write-count и endurance-нагрузку; (b) даёт возможность держать «meta-weights» на analog array, а LoRA-адаптеры — на дешевом digital/fast SRAM / NVM с высокой endurance. ([arXiv][151])

#### 13.3.2. Hardware-aware LoRA (HWA-LoRA / AHWA-LoRA) — recent advances

* **AHWA-LoRA / HWA-LoRA (Li et al., arXiv Nov 2024)** — в статье предлагается держать pre-trained «meta-weights» в analog (фиксированными) и использовать LoRA-модули для адаптации к hardware-constraints и задачам. Метод даёт почти full-accuracy без полного HWA-retrain и уменьшает потребность в on-chip записях (LoRA веса хранятся в цифровой части или в быстрых SRAM). Это прямо решает практическую потребность: минимизировать on-chip writes и упростить deployment. ([arXiv][152])
* **HaLoRA / HaLoRA (2025)** — расширение, учитывающее hybrid CIM/SM architectures (предлагает хранить LoRA в SRAM и meta-weights в RRAM/PCM), с теоретическими гарантиями по сходимости при шуме и non-idealities. ([arXiv][153])

#### 13.3.3. Практические рекомендации по LoRA-разворачиванию на AIMC

1. **Meta-weights on analog; LoRA on digital (SRAM/NVM):** наиболее надёжная схема: analog хранит базовую модель, LoRA (A, B матрицы, rank r≈4–64 в зависимости от задачи) держится в цифровом быстрое-памяти; во время inference LoRA корректирует выходы цифрово/смесью. Это минимизирует writes и позволяет on-device adaptation через обновление только LoRA. (см. Li et al. 2024). ([arXiv][154])
2. **Rank selection:** empirical rule: r in [4, 64] часто даёт ≈SOTA trade-off accuracy vs params; для сложных NLP-задач r≈16–32 — хорошая стартовая точка. Используйте sweep r and LR. ([arXiv][151])
3. **Learning rates & scale:** LoRA требует обычно большие LR для A и маленькие для B (или наоборот — см. LoRA+). Попробуйте LoRA+ рекомендации (разные LR для A and B) для более быстрой и качественной адаптации. ([arXiv][155])
4. **Hardware-aware LoRA training:** two-stage: (i) mount meta-weights to analog (no changes), (ii) retrain LoRA with HWA simulation (inject device noise / quantization) — это дает LoRA-модули, устойчивые к hardware errors. AHWA-LoRA/Chen-Li showed this works for transformer deployments. ([arXiv][156])

#### 13.3.4. LoHA / другие расширения

* **LoHA (Low-rank Hardware-aware Adapters)** — общий термин для LoRA-вариантов, специально оптимизированных под hardware non-idealities (weight clipping, noise alignment, regularization toward meta-weights). HaLoRA / H4H и другие работы 2024–2025 разрабатывают formal guarantees и realistic deployment recipes. ([arXiv][153])

#### 13.3.5. Примеры и результаты

* **Chen Li et al. (Efficient Deployment of Transformer Models in AIMC, arXiv 2411.17367)**: показали, что HWA-LoRA (meta on analog, LoRA in digital + HWA training) даёт accuracy, сравнимую или лучше, чем классический hardware-aware full retrain при значительно меньших вычислительных затратах и write-нагрузке. ([arXiv][152])

---

### 13.4. Общие практические рекомендации по co-design (checklist)

1. **Всегда начать с HWA-retraining (AIHWKit / AIHWKit-Lightning).** Обязательно включить device-models (noise, update asymmetry, ADC/DAC model). ([IBM Analog Hardware Acceleration Kit][143])
2. **Используйте QAT + stochastic rounding** для защиты от low-bit ADC/DAC и accumulation errors; stochastic rounding особенно полезен при малых апдейтах. ([arXiv][148])
3. **Применяйте LoRA/HWA-LoRA (meta on analog, adapters in digital/SRAM) для LLM-адаптации.** Это уменьшит write-count и упростит валидацию. Проведите rank/scale sweep и HWA-LoRA retrain. ([arXiv][154])
4. **Определяйте на ранней стадии целевую битность ADC/DAC и ENOB;** адаптируйте QAT-range и per-tile scaling (dynamic quantization range control). ([lirias.kuleuven.be][150])
5. **Если требуется on-chip fine-tune (not only inference),** рассматривать Tiki-Taka / TTv2 / AGAD / c-TTv2 алгоритмы для on-device parallel updates; они уменьшают требование к симметрии device updates. Но комбинируйте с LoRA, чтобы снизить общий write-count. ([arXiv][145])
6. **Интегрируйте мониторинг & calibration:** периодические calibration sweeps, per-tile bias/scale, and drift-monitoring routine — встроить в deployment pipeline. ([IBM Analog Hardware Acceleration Kit][143])

---

### 13.5. Типичные ошибки и как их избежать

* **Ошибка:** делать HWA-training «поверхностно» — только одна форма шума.
  **Фикс:** моделируйте полный стек: device ΔG, ADC nonlinearity, wire IR, drift. ([Nature][144])

* **Ошибка:** пытаться полностью обучать LLM on-chip без разделения ролей массивов.
  **Фикс:** hybrid pipeline: pretrain off-chip + LoRA/HWA-LoRA on-device + selective in-situ updates (if necessary) с Tiki-Taka/AGAD. ([arXiv][154])

* **Ошибка:** недооценивать роль периферии (ADC/DAC) — надеяться, что analog core сам даст весь выигрыш.
  **Фикс:** оптимизировать peripheral budget совместно с QAT & low-bit mapping. ([IBM Analog Hardware Acceleration Kit][143])

---

### 13.6. Ключевые источники / «must-read» (чтобы глубже вникнуть)

* IBM AIHWKit docs & tutorials — hardware-aware training, analog update optimizers, QAT presets. ([IBM Analog Hardware Acceleration Kit][143])
* AIHWKit-Lightning (IBM) — scalable hw-aware training toolkit для LLMs (2024). ([IBM Research][146])
* Rasch M. J. et al., *Hardware-aware training for large-scale DNNs / Fast and robust analog in-memory deep neural network training* — исследования по non-ideality-aware training и device requirements. ([Nature][147])
* Gupta S. et al., *Deep Learning with Limited Numerical Precision* — stochastic rounding (ICML 2015) — классика по SR. ([arXiv][148])
* Li C. et al., *Efficient Deployment of Transformer Models in Analog In-Memory Computing Hardware* (arXiv 2411.17367) — HWA-LoRA / AHWA-LoRA идея и репозиторий. ([arXiv][152])
* LoRA original (Hu et al., 2021) и LoRA+ (Hayou et al., 2024) — основы low-rank adaptation и рекомендации по LR для A/B. ([arXiv][151])
* Gokmen & Vlasov — Tiki-Taka algorithm (2019/2020) и последующие TTv2/variants — для on-device analog updates на неидеальных устройствах. ([arXiv][145])

---

### Заключение раздела 13 (сводно)

1. **Co-design — необходимость**, а не опция: алгоритмы (HWA-training, QAT, LoRA) должны учитываться вместе с device/circuit constraints уже на этапе model design. ([IBM Analog Hardware Acceleration Kit][143])
2. **LoRA/HWA-LoRA — практический «мост»** между предобученной цифровой моделью и analog deployment: минимизирует write-count и даёт гибкую on-device адаптацию. ([arXiv][154])
3. **Stochastic rounding + mixed-precision + dynamic range control** — обязательные элементы для контроля bias и сохранения точности при низкой битности периферии. ([arXiv][148])
4. **Инструменты** (AIHWKit / AIHWKit-Lightning / CrossSim / MNSIM) уже доступны и должны использоваться как стандартная часть pipeline для валидации HWA-подходов перед silicon/FPGA prototyping. ([IBM Analog Hardware Acceleration Kit][143])

---

<details>
<summary>Детали</summary>

1.  **пример concrete pipeline** (команды / псевдокод) для HWA-LoRA: pretrain → map → HWA-LoRA retrain (AIHWKit snippets + гиперпараметры для rank/LR); или
2.  **шпаргалку-checklist** (CSV) для инженера: какие non-idealities измерить, какие параметры включать в HWA-training и типичные числовые диапазоны (σ_noise, ADC bits, recommended rank r); 

</details>

[143]: https://aihwkit.readthedocs.io/en/latest/hwa_training.html "Analog Hardware-aware Training"
[144]: https://www.nature.com/articles/s41467-023-40770-4 "Hardware-aware training for large-scale and diverse deep ..."
[145]: https://arxiv.org/pdf/1909.07908 "Algorithm for Training Neural Networks on Resistive ..."
[146]: https://research.ibm.com/publications/aihwkit-lightning-a-scalable-hw-aware-training-toolkit-for-analog-in-memory-computing "AIHWKIT-Lightning: A Scalable HW-Aware Training Toolkit ..."
[147]: https://www.nature.com/articles/s41467-024-51221-z "Fast and robust analog in-memory deep neural network ..."
[148]: https://arxiv.org/abs/1502.02551 "Deep Learning with Limited Numerical Precision"
[149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8905452/ "Stochastic rounding: implementation, error analysis and ..."
[150]: https://lirias.kuleuven.be/retrieve/683787 "Dynamic Quantization Range Control for Analog-in-Memory ..."
[151]: https://arxiv.org/abs/2106.09685 "LoRA: Low-Rank Adaptation of Large Language Models"
[152]: https://arxiv.org/abs/2411.17367v2/ "Efficient Deployment of Transformer Models in Analog In- ..."
[153]: https://arxiv.org/html/2502.19747v1 "HaLoRA: Hardware-aware Low-Rank Adaptation for Large ..."
[154]: https://arxiv.org/html/2411.17367v1 "Efficient Deployment of Transformer Models in Analog In- ..."
[155]: https://arxiv.org/abs/2402.12354 "LoRA+: Efficient Low Rank Adaptation of Large Models"
[156]: https://arxiv.org/abs/2411.17367 "Efficient transformer adaptation for analog in-memory ..."

---


## 14. Mapping Transformers / LLM на AIMC — практическая тактика (развёрнутый раздел)

Ниже — подробный, практический и источниково-подкреплённый «how-to» по переносу трансформеров и LLM-слоёв на analog in-memory computing (AIMC). Раздел охватывает (1) что целесообразно маппить в analog, а что держать в цифровом домене, (2) как сочетать MoE и 3D-AIMC чтобы сократить стоимость инференса, и (3) конкретные кейс-стади (ALBERT / IBM-доказы), а также набор практических рецептов (tile-sizes, bitwidth, partitioning, routing, calibration). Все ключевые утверждения опираются на недавние публикации IBM/Nature/архивы (2023–2025). ([Nature][157])

---

### 14.0. Краткая мотивация и общий принцип

AIMC даёт большую энергоэффективность и плотность для матричных умножений (VMM), но страдает от device-non-idealities, ограниченной точности периферии и меж-тайловых затрат. Поэтому практическая задача «маппинга» — максимизировать долю тяжёлых линейных операций (где выигрышь по energy/MAC и плотности велик) и при этом минимизировать влияние non-idealities и накладных расходов (ADC/DAC, interconnect, thermal). ([Nature][157])

---

### 14.1. Что маппить в analog, а что держать в цифровом домене (рекомендации)

#### 14.1.1. Ядро: **маппить в analog (high priority)**

1. **Dense (fully-connected) слои FFN / большие матричные проекции** — именно здесь AIMC показывает наибольшую выигрышность; FFN обычно содержит ≈60–80% параметров трансформера. Маппинг: каждую линейную проекцию (W · x) → crossbar tiles. ([arXiv][158])
2. **Embedding tables / projection layers** — большие lookup/проекции (особенно для больших vocab) выгодно хранить на AIMC, если tile-планирование и sharding позволяют. Вариант: хранить embedding трансформацию в analog, а индексацию/окончательную агрегацию в digital. ([arXiv][158])
3. **MoE experts’ dense layers** — experts обычно большие FFN-блоки; при MoE многие experts «хранятся, но редко активируются» → отличная кандидатура для 3D-AIMC (см. 14.2). ([IBM Research][159])

#### 14.1.2. Держать в цифровом домене (low priority для analog)

1. **Softmax / attention normalization / layer-norm / RMSNorm / GELU nonlinearity** — эти операторы требуют высокоточной редукции/нормировки и условно нелинейных операций; надежнее и проще исполнять в цифровом блоке (FP16/FP32) или гибридно (частично в analog через lookup/approx). ([Nature][157])
2. **Key/Query routing logic (MoE routing, top-k gating)** — условная логика, sparsity routing, load balancing и routing decisions лучше делать в цифровом контроллере; он формирует адреса/маски для активации нужных tiles/experts. ([IBM Research][159])
3. **Layer-wise normalization, softmax stable accumulation, final logits scaling** — требовательны к точности накопления → держать цифровыми. ([Nature][157])

**Практическое правило:** «Analog for massively parallel dense VMM; digital for precise nonlinearities, control & routing.» ([Nature][157])

---

### 14.2. Mixture-of-Experts (MoE) + 3D AIMC — тактика снижения inference cost

#### 14.2.1. Почему MoE + 3D-AIMC хорошо сочетаются

* **MoE** увеличивает число параметров (до сотен миллиардов), но при inference активирует только небольшое подмножество experts → эффективная conditional compute стратегия.
* **3D BEOL stacking** (вертикальные NVM-слои над CMOS) даёт необходимую synapse-density, чтобы хранить огромное число expert-параметров на небольшой площади. Вместе это позволяет хранить тысячи experts и активировать только те, которые требуются для данного запроса → резкое снижение amortized energy per request. ([IBM Research][159])

#### 14.2.2. Концепция размещения (placement) и routing

1. **Banking / Bank-per-expert:** для каждого expert выделяется bank (или набор слоёв) физически компактно размещённых в 3D-stack; routing/controller активирует bank-ы по требованию. Это минимизирует inter-bank traffic при коротких ветках inference. ([IBM Research][159])
2. **Conditional activation → thermal & power budget:** поскольку несколько experts активируются одновременно (обычно 1–4), проектировщик должен гарантировать, что thermal budget и peak power диспетчеризуются — scheduling/activation throttling и load balancing важны. ([IBM Research][159])
3. **Local partial-sum accumulation:** результат каждого expert → локально оцифровывается (ADC) и суммируется цифрово в downstream — избегать переноса полных аналоговых сигналов далеко по матрице. Это снижает inter-tile analog routing cost. ([Nature][157])

#### 14.2.3. Архитектурные оптимизации IBM (практический набор)

* **Store experts across 3D stacks**, активировать only the selected expert banks → уменьшить активные весы и общий energy per inference. IBM показывает, что при корректном mapping и HWA-training MoE+3D AIMC может сделать LLM-scale inference практичным. ([IBM Research][159])

---

### 14.3. Case study: ALBERT на analog-чипе (what they did, why it matters)

#### 14.3.1. Что продемонстрировано (Chen et al., 2025 / Nature Communications)

* ALBERT (a lite BERT variant) был маппирован на 14 nm analog inference chip с PCM, где ~7.1M уникальных analog weights были запрограммированы в ≈28.3M PCM-устройств (за счёт дифференциального кодирования и репликации) и показана near-iso точность для задач NLP. Это первая «meaningful» демонстрация Transformer-класса на реальном analog-hardware. ([Nature][160])

#### 14.3.2. Как они распределяли слои (коротко)

* **Dense linear layers (FFN, Q/K/V projections)** → на аналог-tiles;
* **Нормировки и softmax** → в цифровом домене;
* **Прецизионная настройка и calibration** → hardware-aware retraining и per-tile calibration;
* **Использовали differential encoding и репликацию** весов для повышения SNR и компенсации device-variability. ([Nature][160])

#### 14.3.3. Главные takeaways от ALBERT-демо

1. **Proof-of-feasibility:** Transformer-слой можно корректно запрограммировать и получить near-iso accuracy при помощи HWA-retraining и системной калибровки. ([Nature][160])
2. **Replication & differential encoding** остаются практическими «must»: уменьшают требование к device-однородности, но увеличивают synapse-count. ([Nature][160])
3. **Inter-tile comms + ADC budget** — ключевые инженерные узкие места: успех зависит не только от crossbar, но и от качественного дизайна периферии и сети между tiles. ([Nature][157])

---

### 14.4. Практические рецепты: tile size, bitwidth, partitioning, routing, calibration

#### 14.4.1. Tile sizing и tiling strategy

* **Типичные tile sizes**: 128×128 … 1024×1024 в литературе; для Transformer-слоёв практичный sweet spot часто ≈256×256 или 512×512 — баланс между read-margin (sneak-paths, IR drop) и computational density. Меньшие tiles упрощают calibration/ADC sharing; большие увеличивают плотность, но усложняют margin. ([Nature][157])

#### 14.4.2. Bitwidth и ADC/ DAC

* **Входы (DAC):** 4–8 бит (в зависимости от HWA-training);
* **ADC на колонку / shared ADC:** типично 4–8 бит ENOB; Ambrogio/AIBM демо использовали charge→time / ramp+counter схемы, чтобы снизить энергопотребление ADC. Для LLM mapping рекомендуется проектировать под 6–8 бит ADC и планировать HWA-QAT. ([Nature][157])

#### 14.4.3. Partial sums, accumulation и dataflow

* **Local ADC → digital partial-sum accumulation → cross-tile reduction.** Нести частичные суммы цифрово между tiles (а не аналогово) — уменьшает sensitivity к wire resistances и drift и упрощает accumulation stability. ([Nature][157])

#### 14.4.4. Calibration & HW-aware retrain

* **Per-tile calibration:** bias/scale и offset для каждой колонны после программирования весов; perform short fine-tune on hardware or HWA simulation. AIHWKit/AIHWKit-Lightning используются для HWA retrain и mapping validation. ([IBM Research][161])

#### 14.4.5. Fault tolerance & replication

* **Differential encoding (G+/G−)** и **replication (N-fold)** для повышения SNR и компенсации variability; trade-off: area↑. Практический выбор: start with 2× differential, ramp to higher replication for sensitive layers. ([Nature][157])

---

### 14.5. Toolchain и валидация (что использовать сейчас)

1. **AIHWKit / AIHWKit-Lightning** — симуляция device→array→system, HWA-training и MoE extensions (Analog-MoE). Необходим минимум для рабочего pipeline. ([aihwkit.readthedocs.io][162])
2. **Analog-MoE (GitHub)** — расширения для MoE workloads с HW-awareness (routing sim, gating overhead). ([GitHub][163])
3. **CrossSim / MNSIM** — для более глубокой SPICE-низы модели crossbar и wire-effects (если нужны device-level симуляции). ([arXiv][158])

---

### 14.6. Возможные архитектурные сценарии (deployment patterns)

1. **Edge / On-device small LLMs:** map most linear layers to AIMC tiles, keep attention control digital; use LoRA for adaptivity. Good for privacy/latency use-cases. ([Nature][157])
2. **Cloud / datacenter hybrid:** MoE + 3D-AIMC banks holding many experts; digital controller routes requests and aggregates outputs → large inference capacity at reduced energy cost. IBM 2025 shows this as promising path. ([IBM Research][159])
3. **Accelerated inference + partial on-chip fine-tune:** pretrain off-chip, HWA-retrain, deploy analog inference + LoRA stored in digital for on-device personalization. This is currently the most pragmatic commercial path. ([arXiv][158])

---

### 14.7. Риски, ограничения и «но» (чему заранее готовиться)

* **Inter-tile communication bottlenecks:** при большом числе tiles меж-тайловые задержки и energy передачи частичных сумм значимы; проектируйте высокопараллельные buses и low-latency routers. ([Nature][157])
* **Thermal / write constraints for 3D stacks:** активирование множества experts создаёт локальные hotspot’ы, требует throttling и thermal-aware scheduling. ([IBM Research][159])
* **Accuracy erosion without HWA retrain:** прямой маппинг без hardware-aware training обычно приводит к заметной потере качества; HWA retrain + calibration — обязательны. ([IBM Research][161])

---

### 14.8. Список ключевых источников (пять наиболее важный для раздела)

1. IBM — *Efficient Scaling of Large Language Models with Mixture of Experts and 3D analog in-memory computing* (Büchel et al., 2025). ([IBM Research][159])
2. Chen et al., *Demonstration of transformer-based ALBERT model on a 14 nm analog AI inference chip* (Nature Commun., 2025) — ALBERT analog demo (case study). ([Nature][160])
3. Ambrogio S. et al., *An analog-AI chip for energy-efficient speech recognition and transcription* (Nature, 2023) — system design, tiles, peripheral strategies. ([Nature][157])
4. Chen Li et al., *Efficient Deployment of Transformer Models in Analog In-Memory Computing Hardware* (arXiv 2411.17367) — mapping strategies and experiments on MobileBERT / transformer layers. ([arXiv][164])
5. AIHWKit / AIHWKit-Lightning (IBM) — toolkit & practical HWA training pipeline for AIMC; includes Analog-MoE extensions. ([aihwkit.readthedocs.io][162])

---

### 14.9. Быстрый чек-лист (engineer’s actionable list)

1. **Выбрать target layers**: map FFN/dense + embeddings; keep softmax/LayerNorm digital. ([Nature][157])
2. **Определить tile size**: start 256×256 or 512×512; simulate sneak-paths and IR. ([Nature][157])
3. **Определить ADC/DAC budget**: aim 6–8 bit ENOB for partial sums; consider charge→time architecture. ([Nature][157])
4. **Plan MoE placement**: bank per expert in 3D stack; routing & thermal budget analysis. ([IBM Research][159])
5. **Run HWA retrain**: AIHWKit-Lightning + Analog-MoE; calibrate per tile and run small on-chip fine-tune. ([IBM Research][161])

---

<details>
<summary>Детали</summary>

* A) **сформировать пример mapping-плана** для одного трансформер-слоя (конкретные tile-размеры, число tiles, оценка ADC-битности и energy/MAC, с расчётом throughput), или
* B) **сгенерировать скрипт-шаблон** (AIHWKit / AIHWKit-Lightning) для hw-aware mapping и HWA-retraining трансформера (псевдо-код + ключевые конфиги)

</details>

[157]: https://www.nature.com/articles/s41586-023-06337-5   "An analog-AI chip for energy-efficient speech recognition ..."
[158]: https://arxiv.org/html/2411.17367v1   "Efficient Deployment of Transformer Models in Analog In- ..."
[159]: https://research.ibm.com/publications/efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog-in-memory-computing   "Efficient Scaling of Large Language Models with Mixture ..."
[160]: https://www.nature.com/articles/s41467-025-63794-4   "Demonstration of transformer-based ALBERT model on a ..."
[161]: https://research.ibm.com/publications/aihwkit-lightning-a-scalable-hw-aware-training-toolkit-for-analog-in-memory-computing   "AIHWKIT-Lightning: A Scalable HW-Aware Training Toolkit ..."
[162]: https://aihwkit.readthedocs.io/   "Welcome to IBM Analog Hardware Acceleration Kit's ..."
[163]: https://github.com/IBM/analog-moe   "IBM/analog-moe: HW-aware training extension to AIHWKIT ..."
[164]: https://arxiv.org/abs/2411.17367v1/   "Efficient Deployment of Transformer Models in Analog In- ..."


---

## 15. Inference vs Training: численные выигрыши, ограничения, реальные измерения 

Ниже — технически насыщенный, источниково-проработанный обзор практических чисел, измерений и причин того, почему **AIMC / memristor-чипы уже сегодня дают заметный выигрыш при инференсе**, тогда как **полноценное on-chip обучение (BP для больших моделей)** остаётся серьёзной исследовательской/инженерной задачей. Всё основано на рецензируемых работах и обзорах 2020–2025 (Sebastian 2020; NeuRRAM / Wan 2022; Ambrogio 2023; Gao 2022; Rasch 2024; AIHWKit и др.). ([knowen-production.s3.amazonaws.com][1])

---


### 15.1. Измеренные выигрыши при инференсе (energy/MAC, throughput) — обзорные цифры и диапазоны

#### 15.1.1. Как интерпретировать TOPS/W → energy per op (MAC)

Практичный перевод:

$$\text{energy per op (J)} = \frac{1}{\text{TOPS/W}} \times 10^{-12}\ \text{J/op}$$

т.е. 1 TOPS/W ≈ **1 pJ / op**; 10 TOPS/W ≈ 0.1 pJ/op = 100 fJ/op. (эта простая инверсия часто используется в статьях для грубой конвертации). ([Nature][166])

#### 15.1.2. Конкретные peer-reviewed измерения (примерные значения)

* **Ambrogio et al., Nature 2023 (PCM analog-AI chip):** до **12.4 TOPS/W** chip-sustained. Переводитcя в ≈**0.081 pJ / MAC** ≈ **81 fJ/MAC** (грубо). Авторы отмечают реальные system-level ограничения (периферия, меж-тайловая коммуникация) и приводят замеры на speech workload. ([Nature][166])
* **NeuRRAM / Wan et al., Nature 2022 (RRAM CIM chip):** представлены измерения эффективности до **~78.4 TOPS/W** для специализированных режимов — ≈**12.8 fJ / MAC** (в специфичных условиях и при определённой битности). Это демонстрирует, что при удачном co-design и малой периферийной оплате можно получить энергию на порядок лучше. ([Nature][167])
* **Gao et al., Nat Commun 2022 (auditory localization demonstrator):** application-level demo показал высокую энергоэффективность для real-time sensing и in-situ training; акцент авторов — энергетическое преимущество в задаче sensor→decision по сравнению с полностью цифровыми цепочками. Конкретные energy/MAC там зависят от экспериментальной конфигурации, но общий вывод — существенное снижение энергии на весь pipeline. ([Nature][168])

#### 15.1.3. Общие диапазоны из обзоров и экспериментов (консервативно)

* **Хорошо спроектированные AIMC макросы / chips (peer-reviewed):** **≈10–100 fJ / MAC** (варианты NeuRRAM, Ambrogio и др. попадают в этот диапазон при разных допущениях по ADC/DAC и bitwidth). ([Nature][167])
* **Исследовательские/прототипные демонстраторы и архитектурные предложения:** от **<10 fJ/MAC** (в экзотических/условных измерениях, сильно зависимых от битности и схемы измерения) до **>1 pJ/MAC** (если считать полную систему с плохой периферией). Разброс большой — главное: выигрыш по инференсу часто — **порядки** по сравнению с GPU-реализациями на уровне MAC, но system-level выигрыш зависит от периферии и communication. ([arXiv][169])

#### 15.1.4. Throughput / latency

* AIMC выполняет VMM практически «за один аналоговый шаг» (параллельно для всех весов в кроссбаре) — это даёт очень высокую пропускную способность на tile-уровне; реальные chip-sustained throughput зависит от ADC latency, inter-tile routing и от того, как быстро можно подавать/считывать входы/partial sums. Ambrogio приводит chip-sustained показатели TOPS/W и throughput на speech task (показывает, что архитектурно-сбалансированный chip может поддерживать сотни TOPS). ([Nature][166])

#### 15.1.5. Что «съедает» выигрыш (варианты, которые уменьшают идеальный gain)

* **ADC/DAC и периферия.** Обзоры указывают, что ADC/DAC и сопутствующая mixed-signal периферия могут составлять заметную долю энергии (в отдельных обзорах — до десятков процентов или более; time-to-digital / ramp→counter схемы часто применяют чтобы снизить это). ([queensu.ca][170])
* **Inter-tile communication и цифровая accumulation** (partial-sums): если много cross-tile обменов → итоговый system-level выигрыш уменьшается. ([Nature][166])

**Вывод 15.1:** по инференсу реальные экспериментальные демонстрации показывают энергию на MAC в диапазоне десятков-сотен фемто-джоулей (~10–100 fJ/MAC) для современных AIMC-чипов; это обычно на порядок-два лучше типичных GPU-реализаций на уровне чистого MAC (но system-level сравнение требует учета периферии и коммутаций). ([Nature][167])

---

### 15.2. Почему training пока выигрывает значительно реже: write-overheads, ADC/DAC, endurance

#### 15.2.1. Ключевые причины ограниченного выигрыша при training

1. **Write-overhead (энергия и латентность записи).**

   * Обучение (BP) требует обновлений весов — это физические записи (program pulses) в NVM. Запись часто дороже по энергии и времени, чем чтение/аналоговый VMM. В некоторых технологиях write-energy ≈ десятки–сотни fJ до pJ/операцию или выше в зависимости от устройства и режима (soft vs hard write). Для частого обновления весов (миллионы батчей) суммарная нагрузка становится огромной. Обзоры и device-статьи (PCM / RRAM) подчеркивают, что write-энергия и endurance — ключевой лимит для on-chip training. ([Nature][171])
2. **Endurance (число циклов записи).**

   * Многие RRAM/PCM реализации имеют конечную endurance (диапазон от 10³ до >10¹² в зависимости от материала/процесса). Для интенсивного тренинга LLM нагрузка на записи может быстро исчерпать ресурс устройств. Rasch et al. (2024) и обзоры уточняют, что для full BP LLM endurance требования очень строги и зависят от выбранного алгоритма и архитектуры (некоторые алгоритмы уменьшают частоту записей, но не устраняют потребность в износостойких решениях). ([PMC][172])
3. **Programming latency и verify-loops.**

   * Прецизионное изменение conductance часто требует последовательности пульсов + verify (program/verify) → увеличивает latency и энергию обновления. Это уменьшает throughput обучения по сравнению с цифровыми вариантами (где апдейт — быстрый цифровой write в SRAM/DRAM). ([PubMed][173])
4. **Периферия для градиентных операций.**

   * Training требует accumulation градиентов, масштабных редукций, поддержания временных буферов градиентов — этo digital-heavy задачи. Даже алгоритмы «in-memory outer-product updates» (Tiki-Taka family) требуют дополнительной периферии и специфических device-свойств; Rasch (2024) и последующие работы разрабатывают AGAD / c-TTv2, которые снижают требования к «идеальным» устройствам, но при этом остаётся условие: hardware & algorithm co-design. ([PMC][172])

#### 15.2.2. Что показывает Rasch et al. 2024 (PMC) — количественные/качественные выводы

* **Rasch et al.** предложили алгоритмы AGAD / c-TTv2 и оценили ограничения: алгоритмы сохраняют быстрый runtime TTv2 и снижают требования по точной нулевой reference, однако **узкие места остаются**: conductance noise, asymmetry, retention и endurance всё ещё ограничивают выбор устройств для full-scale in-memory training. Авторы дают оценку, что с оптимальными алгоритмами можно существенно снизить write-count и runtime, но полная практическая реализация для LLM остаётся требовательной по device-характеристикам. ([PMC][172])

#### 15.2.3. ADC/DAC и периферия — процент системной оплаты

* Обзоры по mixed-signal AIMC отмечают, что **ADC/DAC и периферийная электроника** часто составляют значительную долю площади/энергии (в отдельных архитектурах — до 40–64% общей энергии в макросе). Для обучения эта доля ещё больше, потому что accumulation/verify/measurement требуют дополнительных conversions. Следовательно даже если MAC в crossbar дешев, полная цепочка обучения остаётся энергоёмкой. ([queensu.ca][170])

#### 15.2.4. Пример оценки «потрясающей, но не бесплатной» разницы

* В inference-демо Ambrogio (2023) energy/op ≈80 fJ/MAC; но если каждый вес обновлять часто, write-energy и verify-loops могут поставить суммарное energy/op (для update) в порядок pJ–nJ, быстро нивелируя инференсный выигрыш при попытке полного on-chip BP. Поэтому в индустрии практичным становится разделение: heavy pretrain off-chip, затем analog inference + selective fine-tune. ([Nature][166])

**Вывод 15.2:** training требует частых, энергоёмких и (в настоящее время) относительно медленных записей в NVM; endurance и периферия — главные технические барьеры. Несмотря на алгоритмический прогресс (AGAD/TTv2), full on-chip BP для LLM остаётся проблемой материалов/схем и требует гибридных архитектур и/или новых device-классов с очень высокой endurance и низкой write-energy. ([PMC][172])

---

### 15.3. Практичные гибриды: pretrain digital → analog inference + on-device fine-tune

#### 15.3.1. Почему гибрид — текущий практически рабочий паттерн

Сочетание: **(A)** полное предобучение на GPU/TPU (FP32/FP16); **(B)** hardware-aware retrain / QAT (эмуляция non-idealities в тренировке); **(C)** загрузка весов в analog tiles для inference; **(D)** небольшие on-device адаптации (LoRA / low-rank adapters / tiny fine-tune) — даёт почти все преимущества: энергоэффективный inference и возможность персональной адаптации без интенсивных on-chip записей. AIHWKit и его расширения — основной инструментальный стек для этого pipeline. ([aihwkit.readthedocs.io][174])

#### 15.3.2. Конкретный workflow (практический рецепт)

1. **Pretrain** на цифровой инфраструктуре.
2. **Hardware-aware retrain / quantize (AIHWKit):** inject device noise, quantization, update asymmetry в forward pass; подогнать weight-ranges и clipping. ([aihwkit.readthedocs.io][174])
3. **Map heavy dense layers → AIMC tiles:** FFN и большие матричные проекции; сохранить softmax/LayerNorm/attention-routing в цифровом домене или реализовать их гибридно. ([Nature][166])
4. **Deploy inference:** analog tiles выполняют VMM; per-tile ADC→digital partial-sum accumulation; calibration sweep + small on-chip calibration fine-tune. ([Nature][166])
5. **On-device adaptation (LoRA / LoHA):** хранить адаптеры в цифровой быстродействующей памяти; обновлять их часто; при необходимости — редкие on-chip writes в специально отведённые high-endurance arrays. ([Nature][175])

#### 15.3.3. Инструменты и подтверждающие работы

* **IBM AIHWKit / AIHWKit-Lightning** — симуляция HWA retrain, mapping, QAT. IBM-группа и другие используют этот стек как standard pipeline. ([aihwkit.readthedocs.io][174])
* **Ambrogio 2023 + Chen et al. 2025 (ALBERT analog demo)** — примеры успешного применения hybrid-pipeline: pretrain/off-chip → HWA retrain → analog inference на реальном chip. Эти демо показывают, что такой путь воспроизводим и практичен. ([Nature][166])

#### 15.3.4. Практические числовые ожидания (примерно)

* **Inference energy per token** (оценка зависит от архитектуры, активированных experts и т.д.): для AIMC-mapped больших слоёв — десятки–сотни fJ/MAC; суммарная энергия на токен (включая attention, softmax, KV cache, routing) будет выше, но всё ещё может быть ниже на порядок по сравнению с GPU в хорошо спроектированных системах (см. архитектурные исследования 2024–2025). ([arXiv][176])

**Вывод 15.3:** практический и безопасный путь к реальной выгоде сегодня — hybrid: цифровой pretrain + HWA retrain + analog inference + low-write on-device adapters. Такой pipeline даёт основной энергетический выигрыш инференса и контролирует риски endurance/latency при обучении. ([aihwkit.readthedocs.io][174])

---

### 15.4. Резюме — краткие takeaways для принятия решений

1. **Inference:** AIMC уже демонстрирует реальные измеримые выигрыши (≈10–100 fJ/MAC в peer-reviewed chips), что делает analog-inference привлекательным для edge/real-time/energy-constrained деплоев. ([Nature][167])
2. **Training:** из-за write-energy, latency и endurance полное on-chip BP для LLM остаётся нерешённой инженерной задачей; алгоритмы (AGAD, c-TTv2 / TTv2 family) снижают требования, но не снимают их полностью. ([PMC][172])
3. **Hybrid pipeline (рекомендуется):** pretrain off-chip → HWA retrain + analog inference + LoRA/low-write fine-tune on-device — лучший текущий compromise между эффективностью и практичностью. Используйте AIHWKit / CrossSim / MNSIM в цепочке валидации. ([aihwkit.readthedocs.io][174])

---

#### Основные использованные источники (выделено для быстрой проверки)

* A. Sebastian et al., *Memory devices and applications for in-memory computing*, **Nat. Nanotech.** (2020) — обзор преимуществ/ограничений AIMC. ([knowen-production.s3.amazonaws.com][165])
* S. Ambrogio et al., *An analog-AI chip for energy-efficient speech recognition and transcription*, **Nature** (2023) — 35M PCM devices, до **12.4 TOPS/W** (пример system-level измерения). ([Nature][166])
* W. Wan et al. (NeuRRAM), *A compute-in-memory chip based on RRAM* (Nature 2022) — RRAM-CIM пример с **~78.4 TOPS/W** в specific mode. ([Nature][167])
* M. J. Rasch et al., *Fast and robust analog in-memory deep neural network training*, **Nat. Commun.** / PMC (2024) — алгоритмы AGAD / c-TTv2 и анализ ограничений (endurance, drift, noise). ([PMC][172])
* B. Gao et al., *Memristor-based analogue computing for brain-inspired sound localization with in-situ training*, **Nat. Commun.** (2022) — application-level demo showing energy advantages for sensing tasks. ([Nature][168])
* IBM AIHWKit (docs / GitHub) — toolkit для hardware-aware training / mapping. ([aihwkit.readthedocs.io][174])

---

<details>
<summary>Детали</summary>

* A) **сформировать таблицу (CSV)** с численными метриками energy/MAC и throughput для ключевых peer-reviewed работ (Ambrogio 2023, NeuRRAM 2022, Gao 2022, Rasch 2024) — с явными источниками и конвертацией TOPS/W → fJ/MAC; или
* B) **подготовить короткую презентацию (PDF)** «Inference vs Training on AIMC — executive summary» с ключевыми цифрами и рекомендациями для руководителя, или
* C) **сделать расчёт-пример**: «оценочный energy на token» для маленького трансформера при заданном split (где какая часть на analog) с числовыми допущениями (tile size, ADC bits, MAC counts).

</details>

[165]: https://knowen-production.s3.amazonaws.com/uploads/attachment/file/5270/10.1038_s41565-020-0655-z.pdf   "Memory devices and applications for in-memory computing"
[166]: https://www.nature.com/articles/s41586-023-06337-5   "An analog-AI chip for energy-efficient speech recognition ..."
[167]: https://www.nature.com/articles/s41586-022-04992-8   "A compute-in-memory chip based on resistive random- ..."
[168]: https://www.nature.com/articles/s41467-022-29712-8   "Memristor-based analogue computing for brain-inspired ..."
[169]: https://arxiv.org/html/2306.15552v2   "A Survey on Deep Learning Hardware Accelerators for ..."
[170]: https://www.queensu.ca/physics/shastrilab/sites/shastwww/files/uploaded_files/publications/journals/88_Garg_JSTQE_Dynamic-precision_2023.pdf   "Dynamic Precision Analog Computing for Neural Networks"
[171]: https://www.nature.com/articles/s41467-023-42792-4   "Novel nanocomposite-superlattices for low energy and ..."
[172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335942/   "Fast and robust analog in-memory deep neural network ..."
[173]: https://pubmed.ncbi.nlm.nih.gov/32231270/   "Memory devices and applications for in-memory computing"
[174]: https://aihwkit.readthedocs.io/   "IBM Analog Hardware Acceleration Kit's documentation!"
[175]: https://www.nature.com/articles/s41467-024-51221-z   "Fast and robust analog in-memory deep neural network ..."
[176]: https://www.arxiv.org/pdf/2409.19315v1   "Analog In-Memory Computing Attention Mechanism for Fast and ..."


---


## 16. Точность, шум, drift и методы компенсации 

Ниже — детальная, практическая инструкция по тому, какие ошибки и дрейфы возникают в AIMC/memristor-массивах, как их измерять, как моделировать в тренировке и как компенсировать аппаратно и алгоритмически. Для ключевых утверждений даю ссылки на современные, высокоцитируемые работы и инструменты (AIHWKit, Rasch 2024, Ambrogio 2023, Mackin 2022, recent ensemble/averaging papers и пр.). ([IBM Analog Hardware Acceleration Kit][177])

---

### 16.0. Короткое введение — какие типы ошибок нас интересуют

1. **Статическая вариабельность (D2D/C2C)** — device-to-device spread в начальных conductance/порогах. ([Nature][178])
2. **Циклическая / случайная вариабельность (C2C, cycle-to-cycle)** — ΔG/пульс распределение при повторных программированиях. ([Nature][179])
3. **Шум (read noise, thermal, shot-noise и др.)** — быстрые флуктуации измеряемого тока/напряжения в режиме чтения. ([Nature][180])
4. **Drift (темпоральный дрейф conductance)** — медленная эволюция conductance после программирования (обычно логарифмическая или степенная зависимость времени). ([Nature][181])
5. **Асимметрия апдейта (set vs reset ΔG)** — разные величины и распределения ΔG для позитивных и негативных пульсов. ([PMC][182])
6. **Периферийные non-idealities** — ADC/DAC quantization, limited ENOB, IR-drop по шинам, sneak-paths. ([IBM Analog Hardware Acceleration Kit][177])

Эти non-idealities влияют как на инференс (точность, SNR), так и на обучение (bias, несходимость, wear). Правильная защита требует комбинации трёх слоёв: *измерение → моделирование (в HWA-training) → компенсация (circuit+algorithm)*. ([IBM Analog Hardware Acceleration Kit][183])

---

### 16.1. Hardware-aware training: error injection, ensembles, calibration loops

#### 16.1.1. Что делает hardware-aware training (HWA)

HWA-training включает статистические и поведенные модели non-idealities прямо в forward/backward (или в fine-tuning) — шум в весах/partial sums, квантование ADC/DAC, update asymmetry, drift-augmentation и т.д. Это даёт реальную устойчивость на deployed hardware и часто восстанавливает «software-equivalent (SW_eq)» accuracy после маппинга. Практические инструменты: IBM **AIHWKit / AIHWKit-Lightning** — готовые device-presets и HWA-pipeline. ([IBM Analog Hardware Acceleration Kit][183])

#### 16.1.2. Error injection — базовая методика (практика)

* **Forward pass:** заменяем W → W + ε_W, где ε_W моделируется как смесь статической D2D-шумовой компоненты (sampled once per device) и динамической C2C компоненты (sampled per-update/batch). Часто используют нормальное или лог-нормальное распределение, параметры которого берутся из эмпирики. ([IBM Analog Hardware Acceleration Kit][183])
* **ADC/DAC:** во forward моделируем finite ENOB и nonlinearity (т.е. fake-quant + non-ideal transfer curve). В backward используем surrogate gradients / straight-through. ([PMC][184])
* **Drift augmentation:** периодически (в тренировочной эпохе) применять трансформацию G(t)=G0·f(t) (лог-/пауэр-зависимость), чтобы сеть училась быть устойчивой к медленному дрейфу. Rasch и другие рекомендуют прогрессивную аугментацию drift при fine-tuning. ([PMC][182])

#### 16.1.3. Ensemble / replica strategies (hardware ensembles)

* **Replica averaging / layer ensemble averaging:** маппить одну и ту же логическую матрицу на N физически разных пластов/реплик и усреднять выходы — очень эффективный трюк для уменьшения эффекта D2D и дефектов. Недостаток — рост required device-count и area. Recent experimental/empirical works демонстрируют near-SW_eq восстановление с приемлемым N (см. Yousuf et al. — layer ensemble averaging). ([arXiv][185])
* **Differential pairs + replication:** классическая практика: кодирование весов G = G⁺ − G⁻ и репликация колонки/строки для повышения SNR и компенсации offset. Амброджио и другие используют differential + replication в крупных сборках. ([Nature][186])

#### 16.1.4. Calibration loops (практический SOP)

1. **Initial program + verify:** программируем веса (program/verify staircase) и сохраняем baseline conductance. (Mackin et al. — оптимизация weight programming). ([Nature][181])
2. **Per-tile column/row bias & scale calibration:** измерить per-column gain/offset на calibration vectors и применять цифровое развёртывание (scale + bias) при inference. ([IBM Analog Hardware Acceleration Kit][183])
3. **Short fine-tune:** после первого программирования выполнить короткий HWA-fine-tune на hardware-emulator или реальном чипе (несколько эпох, малый LR) — повышает SW_eq. ([IBM Analog Hardware Acceleration Kit][183])
4. **Periodic refresh / recalibration:** делать scheduled refresh (ре-программирование) для тяжелых слоев по расписанию или по threshold-monitoring (drift > eps). ([Nature][181])

**Пример автоматизированного цикла calibration (псевдокод):**

```
for tile in tiles:
  program_weights(tile, target_G)
  measure_G = read_tile(tile)
  compensate_params = fit_scale_bias(measure_G, target_G)
  store(compensate_params)
perform_short_finetune(hardware/emulator)
schedule_refresh(policy=drift_threshold or time_interval)
```

(см. AIHWKit examples и Mackin 2022). ([IBM Analog Hardware Acceleration Kit][183])

---

### 16.2. Algorithmic defence: replica-averaging, stochastic rounding, retraining/finetune

#### 16.2.1. Replica-averaging и layer ensembles — когда выгодно

* **Когда:** при высокой D2D/defect rate и для inference-critical слоев.
* **Как:** маппировать одну логическую матрицу на M независимых physical instances → усреднять выходы (или majority voting для классификаторов). Yousuf et al. показывают, что при разумном M можно восстановить близкую к SW_acc точность. Trade-off area∝M, energy↑, но robustness↑. ([arXiv][185])

#### 16.2.2. Stochastic rounding — где и почему

* **Идея:** при низкой битности накопления/квантования заменять round-to-nearest на stochastic rounding (SR), чтобы апдейты не усекались и чтобы ошибки округления были unbiased в среднем. Показано (Gupta et al., 2015), что SR позволяет тренировать в низкой разрядности без потери точности; в AIMC SR полезен для цифровых accumulators/quantizers и при низких LR-апдейтах на hardware. ([arXiv][187])

#### 16.2.3. Retraining / periodic finetune

* **Регулярный HWA-finetune:** короткие сеансы finetune (с HWA-noise + drift augmentation) после установки весов на чипе — компенсируют накопившийся drift и non-linearities. Rasch 2024 и AIHWKit рекомендуют такие «maintenance-runs». ([PMC][182])

#### 16.2.4. Additional algorithmic tricks

* **Weight clipping & range control:** ограничение динамического диапазона весов (per-tile scaling) для улучшения SNR при фиксированном conductance range. ([IBM Analog Hardware Acceleration Kit][183])
* **Noise-aware regularization:** L2/L1 c шумовой регуляризацией, DropConnect / quantization noise training. ([Nature][188])
* **Checkpoint + rollback policies:** при агрессивных write-операциях планируйте бинарные / differential checkpoints, чтобы иметь возможность отката в случае деградации. ([Nature][181])

---

### 16.3. Benchmarks — как репортить accuracy/robustness при наличии non-idealities

#### 16.3.1. Обязательные метрики и протоколы (минимум для публикации/отчёта)

1. **Baseline (software) accuracy:** на той же модели и наборе данных, FP32 baseline. (обязателен). ([IBM Analog Hardware Acceleration Kit][183])
2. **Mapped-to-hardware accuracy (immediately after programming):** accuracy после initial program+calibration. Отдельно репортируйте: mean ± std по N runs/replicas. ([Nature][181])
3. **Time-series accuracy (drift curve):** accuracy(t) и weight-drift curves G(t) measured for t in {1 min, 1 h, 1 day, 1 week, ...} или accelerated Arrhenius tests для retention projection. Покажите loss/accuracy vs time и drift statistics (median, 5–95 percentile). ([Nature][181])
4. **Write-counts & endurance budget:** записей per weight per epoch and projected lifetime (e.g., how many inference/fine-tune ops until X% devices exhausted). Rasch et al. подчеркивают необходимость этих показателей. ([PMC][182])
5. **Energy breakdown:** отдельные строки: core analog VMM energy, ADC/DAC energy, periphery (drivers, sense amps), calibration/refresh energy (включая program/verify cost). Не только aggregate TOPS/W — показать decomposition. ([Nature][189])
6. **Variability & noise statistics:** report D2D σ, C2C σ, ΔG per pulse distribution, asymmetry metrics. ([Nature][179])

#### 16.3.2. Рекомендуемый формат отчёта (чтобы сравнение было корректным)

* Таблица: {Work | Device | Tile size | ADC bits | baseline acc | mapped acc (t0) | mapped acc (t1 = 24h) | energy/core | energy/periphery | writes/epoch | projected lifetime}.
* Графики: (a) accuracy vs time, (b) drift distribution (boxplots for G(t)-G0), (c) sensitivity sweep (accuracy vs injected σ_noise), (d) ablation of compensation techniques (no HWA vs HWA vs HWA+ensembles). ([IBM Analog Hardware Acceleration Kit][183])

#### 16.3.3. Репликативные требования к статистике

* **N_runs ≥ 5–10** для оценок mean/std; при публикации device-level claims — желательно ≥30 измерений (или bootstrap CI). Для ускоренных тестов retention/endurance — показать методику accelerated aging и модель реконструкции реального времени (Arrhenius extrapolation). ([Nature][181])

---

### 16.4. Практический чек-лист компенсаций (engineer’s actionable list)

1. **Сделать полный device-audit:** ΔG per pulse, asymmetry, D2D σ, C2C σ, drift law, retention (Arrhenius), endurance. (start here). ([Nature][179])
2. **Включить HWA-training:** error injection (static+dynamic), ADC model, drift augmentation. Использовать AIHWKit presets как базовую модель. ([IBM Analog Hardware Acceleration Kit][183])
3. **Использовать differential encoding + replication** для критичных слоёв (SNR boost). Trade-off: area↑. ([Nature][186])
4. **Реализовать calibration loop и schedule refresh:** program/verify, per-tile bias/scale; short on-chip fine-tune после программирования. ([Nature][181])
5. **Опционально: layer ensemble averaging / replica averaging** для слоёв с высокой чувствительностью — особенно если device yield / variability плохие. ([arXiv][185])
6. **Добавить stochastic rounding** в цифровые накопители/quantizers, чтобы сохранить малые апдейты и уменьшить bias. ([arXiv][187])
7. **Мониторинг и метрики:** измерять accuracy(t), G(t), write_counts, energy breakdown и публиковать их. ([Nature][181])

---

### 16.5. Ключевые источники (must-read, recent)

* **AIHWKit docs / tutorials** — hardware-aware training patterns, fake-quant, device-presets и calibration examples. ([IBM Analog Hardware Acceleration Kit][177])
* **Rasch M. J. et al., *Fast and robust analog in-memory deep neural network training*, Nat. Commun. 2024 (PMC)** — алгоритмы AGAD/c-TTv2, оценка предельных требований conductance noise/retention/endurance. ([PMC][182])
* **Ambrogio S. et al., *An analog-AI chip for energy-efficient speech recognition and transcription*, Nature 2023** — system-level демонстрации, replication/differential encoding и per-tile calibration в крупной системе. ([Nature][186])
* **C. Mackin et al., *Optimised weight programming for analogue memories*, Nat. Commun. 2022** — автоматизация программинга весов и стратегии уменьшения деградации accuracy со временем. ([Nature][181])
* **O. Yousuf et al., *Layer ensemble averaging for improving memristor-based ANN performance* (arXiv / Nat-comm 2024/2025)** — практический алгоритм replica/ensemble averaging для fault tolerance. ([arXiv][185])
* **G. Gulafshan et al., *Realistic behavioral model for ReRAMs capturing non-idealities*, 2025** — продвинутые behavioral-модели, включая drift и cycle variability. ([Nature][179])
* **Survey/review by Aguirre et al., *Hardware implementation of memristor-based ANNs*, Nat. Commun. 2024** — обзор практик, компромиссов и инструментов. ([Nature][178])

---

### Заключение раздела 16 (сводно)

1. **Accuracy vs time — многомерная метрика.** Нельзя ограничиваться single-shot accuracy: обязательны time-series (drift), energy & write-counts. ([Nature][181])
2. **Комбинация методов даёт наилучший результат:** HWA-training + calibration loops + differential encoding/replication + stochastic rounding + (при необходимости) layer-ensembles. ([IBM Analog Hardware Acceleration Kit][183])
3. **Инструменты (AIHWKit, CrossSim) + экспериментальные data → roadmap:** прогоняйте device-audit → симуляции HWA → малый hardware prototype → calibration+short-finetune → longer tests (retention/endurance). ([GitHub][190])

---

<details>
<summary>Детали</summary>

A) **CSV-шаблон** для отчёта (столбцы: device, D2D σ, C2C σ, drift law params, baseline acc, mapped acc(t0), mapped acc(t24h), writes/epoch, energy breakdown) — готово к заполнению;
B) **Псевдокод calibration loop + HWA-training recipe** (конкретные команды AIHWKit + hyper-params) — пригодится для воспроизведения;
C) **Короткий checklist для тестирования drift/endurance** (SOP для lab): какие тесты запускать, какие графики строить, критерии прохода/отказа.

</details>

[177]: https://aihwkit.readthedocs.io/ "IBM Analog Hardware Acceleration Kit's documentation!"
[178]: https://www.nature.com/articles/s41467-024-45670-9 "Hardware implementation of memristor-based artificial ..."
[179]: https://www.nature.com/articles/s43246-025-00807-1 "Realistic behavioral model for ReRAMs capturing non- ..."
[180]: https://www.nature.com/articles/s41586-022-04992-8 "A compute-in-memory chip based on resistive random- ..."
[181]: https://www.nature.com/articles/s41467-022-31405-1 "Optimised weight programming for analogue memory ..."
[182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335942/ "Fast and robust analog in-memory deep neural network ..."
[183]: https://aihwkit.readthedocs.io/en/latest/hwa_training.html "Analog Hardware-aware Training"
[184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12298086/ "Memristor Emulator Circuits: Recent Advances in Design ..."
[185]: https://arxiv.org/abs/2404.15621 "Layer Ensemble Averaging for Improving Memristor-Based Artificial Neural Network Performance"
[186]: https://www.nature.com/articles/s41586-023-06337-5 "An analog-AI chip for energy-efficient speech recognition ..."
[187]: https://arxiv.org/abs/1502.02551 "Deep Learning with Limited Numerical Precision"
[188]: https://www.nature.com/articles/s41467-023-40770-4 "Hardware-aware training for large-scale and diverse deep ..."
[189]: https://www.nature.com/articles/s41467-024-51221-z "Fast and robust analog in-memory deep neural network ..."
[190]: https://github.com/IBM/aihwkit "IBM/aihwkit: IBM Analog Hardware Acceleration Kit"

---

## 17. Симуляторы, инструменты и репозитории (AIHWKit, CrossSim, MNSIM и пр.) 

Ниже — подробный справочник по наиболее важным open / research инструментам для моделирования memristor-/AIMC-систем. Для каждого инструмента даю: уровень моделирования (device → array → architecture → algorithm), ключевые возможности, ограничения, установка/быстрый старт, рекомендуемые сценарии использования и ссылки на репозитории / документацию. Все утверждения основаны на официальных страницах и рецензируемых публикациях (2020–2025). ([GitHub][191])

---

### 17.1. AIHWKit (IBM) — HW-aware training и симуляция non-idealities

#### Что это и для чего

AIHWKit — Python-фреймворк от IBM для hardware-aware (HWA) тренировки нейросетей с эмуляцией device-level non-idealities (noise, update asymmetry, quantization, drift и т.д.). Предназначен главным образом для того, чтобы включать поведение «реального» AIMC-железа прямо в цикл обучения (forward/fine-tune), и содержит device-presets, fake-quant/ADC/DAC модели и API для интеграции с PyTorch. ([GitHub][191])

#### Уровень моделирования

* **Algorithm / training level**: HWA training, fake-quant, noise injection.
* **Array behavior**: базовая модель crossbar-array, differential encoding, per-tile scaling.
  (Не заменяет SPICE-уровень моделирования, но покрывает всё, что нужно для ML-инженера.) ([aihwkit.readthedocs.io][192])

#### Ключевые возможности

* Device-presets (PCM/RRAM etc.), signal-chain models (ADC/DAC), quantization & surrogate gradients.
* Интеграция с PyTorch → легко сделать QAT / HWA fine-tune.
* Документация + примеры на ReadTheDocs; pip-пакет для быстрой установки. ([aihwkit.readthedocs.io][192])

#### Быстрый старт / установка

```bash
pip install aihwkit
## или
conda install -c conda-forge aihwkit
```

Документация, примеры и how-to: AIHWKit ReadTheDocs. ([aihwkit.readthedocs.io][193])

#### Ограничения и когда применять

* Отличен для HWA-retraining, QAT и ранней валидации моделей.
* Не предназначен для детальных circuit/SPICE-исследований или для full system thermal/IR-drop analysis — для этого нужны CrossSim / NeuroSim / SPICE-потоки. ([aihwkit.readthedocs.io][192])

**Источник:** AIHWKit GitHub + Документация. ([GitHub][191])

---

### 17.2. AIHWKit-Lightning / Analog-MoE (IBM) — масштабируемая HWA-тренировка и MoE-поддержка

#### Что это

AIHWKit-Lightning — ускоренная / масштабируемая версия AIHWKit, ориентированная на LLM-scale HWA-training; Analog-MoE — библиотека/ядро для MoE операций с hardware-aware extension. Эти проекты облегчают тренировку больших сетей с учётом аппаратных non-idealities. ([GitHub][194])

#### Когда использовать

* При HWA-тренировке крупных трансформеров и MoE-архитектур, когда нужна высокая производительность на GPU и интеграция HW-noise model в pipeline. ([GitHub][195])

**Источники:** AIHWKit-Lightning repo / IBM публикация по AIHWKit-Lightning; Analog-MoE GitHub. ([GitHub][194])

---

### 17.3. CrossSim (Sandia) — crossbar accuracy / behavior simulator (GPU-accelerated)

#### Что это и для чего

CrossSim — GPU-ускоренный Python-инструмент для точной оценки влияния crossbar-non-idealities на accuracy ML-задач. Фокус — accuracy/co-design: моделирование I–V, IR-drop, wire-resistance, колонковые/строчные модели, ADC/driver effects и их влияние на выходные partial sums и accuracy. Содержит manual, примеры и исполняемый пакет. ([Crossbar Simulator][196])

#### Уровень моделирования

* **Array / crossbar behavior → algorithm accuracy.** Подходит для воспроизведения device→array→accuracy цепочек; GPU-ускорение делает его удобным для sweep'ов параметров. ([Crossbar Simulator][196])

#### Ключевые возможности

* Модели IR-drop, bias rows, negative weight handling (двойной массив), variable-pulse driving, integration→ADC model.
* Примеры: Keras H5 модель → CrossSim input (manual описывает workflow). ([osti.gov][197])

#### Установка / быстрый старт

CrossSim распространяется как пакет с manual; manual содержит pip-инструкции и примеры установки/входных форматов. (См. CrossSim manual; сайт проекта). ([Crossbar Simulator][198])

#### Ограничения

* Не заменяет circuit-level SPICE, но даёт точные оценки влияния crossbar-эффектов на accuracy. Отличен для stage «array → model accuracy». ([Crossbar Simulator][196])

**Источник:** CrossSim site + manual / downloadable package. ([Crossbar Simulator][196])

---

### 17.4. MNSIM / MNSIM-2.0 (Tsinghua) — behavior-level PIM architecture simulator

#### Что это и для чего

MNSIM-2.0 — инструмент уровня «architecture / system» для исследования PIM-архитектур: поддерживает inference accuracy simulation с учётом mixed-precision, non-idealities, hierarchical modeling (tile/array/bank), а также performance/energy estimation для PIM-architectures. Публикация 2020 описывает возможности и валидацию. Репозиторий MNSIM-2.0 доступен на GitHub. ([ACM Digital Library][199])

#### Уровень моделирования

* **Architecture / system level** — позволяет исследовать mapping, dataflow, latency/throughput/energy для PIM архитектур и проводить «design-space exploration». ([nicsefc.ee.tsinghua.edu.cn][200])

#### Ключевые возможности

* Hierarchical modeling (tile → bank → chip), включение device-non-idealities в accuracy estimation, support для mixed-precision. Полезен для early-stage архитектурных решений. ([nicsefc.ee.tsinghua.edu.cn][200])

#### Установка / быстрый старт

* Репозиторий MNSIM-2.0 (GitHub) содержит инструкции, примеры и paper. Подойдёт для академических DSE-экспериментов. ([GitHub][201])

**Источник:** MNSIM-2.0 paper + GitHub. ([ACM Digital Library][199])

---

### 17.5. MemTorch — PyTorch-integrated memristor simulation framework

#### Что это и для чего

MemTorch — open-source фреймворк, напрямую интегрируемый с PyTorch, предназначенный для co-simulation memristive DL (device non-idealities + peripheral). Хорош для исследователей, желающих «подружить» PyTorch-workflow с memristor-моделями. Описание в Neurocomputing / arXiv (2020–2022). ([arXiv][202])

#### Уровень моделирования

* **Algorithm / device co-simulation**: позволяет проводить тренировки/конвертацию моделей, вставляя device-поведение. ([memtorch.readthedocs.io][203])

#### Ключевые возможности

* Набор device-моделей (VTEAM, linear ion drift, Stanford PKU RRAM и т.д.), API для интеграции в PyTorch, tutorial-notebooks. Удобен для reproduction и быстрых экспериментов. ([arXiv][202])

#### Установка / примеры

* GitHub + ReadTheDocs + Colab examples доступны; подходит для ML-инженеров, привыкших к PyTorch. ([GitHub][204])

**Источник:** MemTorch GitHub + статья в Neurocomputing / arXiv. ([ScienceDirect][205])

---

### 17.6. NeuroSim & другие CAD/estimation-фреймворки

#### Что это

NeuroSim — фреймворк для device→circuit→architecture→system level performance/area/power modeling, часто используемый для post-layout validation (требует device / cell parameters) и калибруется под 40nm RRAM макросы. Полезен для подсчёта energy/MAC и area projections. ([Frontiers][206])

#### Когда применять

* Когда нужно получить quantitative power/area/latency оценки и сравнить с ASIC/GPUs на уровне energy/MAC; хорош для feasibility/benchmarking. ([Frontiers][206])

---

### 17.7. Как выбирать инструмент по этапам разработки (рекомендованная pipeline)

1. **Device & compact models (early device-audit):** собрать Verilog-A / measured ΔG per pulse, drift, endurance. (SPICE / Verilog-A tools — внешние).
2. **PyTorch-level emulation & HWA-training:** MemTorch (fast experiments) → AIHWKit (production HWA training / QAT) → AIHWKit-Lightning (LLM-scale). ([memtorch.readthedocs.io][203])
3. **Array/accuracy sweep:** CrossSim (array IR-drop/ADC effects → model accuracy). ([Crossbar Simulator][196])
4. **Architecture / system DSE:** MNSIM / NeuroSim (tile sizing, mapping, energy/latency). ([nicsefc.ee.tsinghua.edu.cn][200])
5. **End-to-end validation:** combine AIHWKit emulation with CrossSim/MNSIM results and small hardware prototype. ([aihwkit.readthedocs.io][192])

---

### 17.8. Практические советы, трюки и «подводные камни»

* **Start small and escalate:** начинайте с MemTorch / AIHWKit на MNIST/CIFAR-scaled примерах; потом делайте CrossSim-sweep; только после этого переходите к MNSIM/NeuroSim DSE. ([arXiv][202])
* **Согласуйте device-models:** используйте одинаковые device-presets между инструментами (например, то же PDF распределения ΔG) — иначе сравнения meaningless. ([aihwkit.readthedocs.io][192])
* **Watch the peripherals:** многие исследователи забывают ADC/DAC; используйте инструменты, которые моделируют периферию (AIHWKit, CrossSim, NeuroSim делают это в разной степени). ([aihwkit.readthedocs.io][192])
* **GPU acceleration:** для CrossSim / AIHWKit-Lightning нужна мощная GPU-инфраструктура при больших sweep'ах / LLM-scale HWA-training. ([Crossbar Simulator][196])

---

### 17.9. Ключевые репозитории и ссылки (откройте их)

* **AIHWKit (IBM) — GitHub / Docs.** ([GitHub][191])
* **AIHWKit-Lightning (IBM) — GitHub / paper.** ([GitHub][194])
* **Analog-MoE (IBM) — GitHub (MoE kernels + HWA extensions).** ([GitHub][195])
* **CrossSim (Sandia) — site + manual + package.** ([Crossbar Simulator][196])
* **MNSIM-2.0 (Tsinghua) — GitHub + paper** (GLSVLSI 2020). ([GitHub][201])
* **MemTorch — GitHub + paper (Neurocomputing / arXiv).** ([GitHub][204])
* **NeuroSim — paper & validation (Frontiers / calibration study).** ([Frontiers][206])

---

### 17.10. Короткая сводка — когда что применять (cheat-sheet)

* **Исследователь device → model (быстро, PyTorch):** MemTorch. ([GitHub][204])
* **HWA-training / deployment pipelines:** AIHWKit → AIHWKit-Lightning (+ Analog-MoE для MoE). ([aihwkit.readthedocs.io][192])
* **Array → accuracy detailed sweep (IR, wire, ADC):** CrossSim. ([Crossbar Simulator][196])
* **Architecture / system DSE (tile, bank, 3D stacking):** MNSIM / NeuroSim. ([nicsefc.ee.tsinghua.edu.cn][200])

---

<details>
<summary>Детали</summary>

* A) подготовить **короткий рабочий пример** (notebook-шаблон) «PyTorch → MemTorch → AIHWKit» с командами установки и простым сет-workflow (код + комментарии), или
* B) сгенерировать **таблицу-сравнение** (CSV/Markdown) всех перечисленных инструментов — уровни моделирования, ключевые возможности, команды установки, GitHub/DOI, и рекомендованный этап пайплайна

</details>

[191]: https://github.com/IBM/aihwkit "IBM/aihwkit: IBM Analog Hardware Acceleration Kit"
[192]: https://aihwkit.readthedocs.io/ "Welcome to IBM Analog Hardware Acceleration Kit's ..."
[193]: https://aihwkit.readthedocs.io/en/latest/install.html "Installation — IBM Analog Hardware Acceleration Kit 1.0.0 ..."
[194]: https://github.com/IBM/aihwkit-lightning "IBM/aihwkit-lightning: Scalable HW-Aware Training ..."
[195]: https://github.com/IBM/analog-moe "IBM/analog-moe: HW-aware training extension to AIHWKIT ..."
[196]: https://cross-sim.sandia.gov/ "CrossSim: Crossbar Simulator - Sandia National Laboratories"
[197]: https://www.osti.gov/servlets/purl/1869509 "CrossSim Inference Manual (v2.0)"
[198]: https://cross-sim.sandia.gov/app/uploads/sites/110/2021/09/crosssim_manual.pdf "ROSS SIM - CrossSim: Crossbar Simulator"
[199]: https://dl.acm.org/doi/10.1145/3386263.3407647 "MNSIM 2.0: A Behavior-Level Modeling Tool for Memristor- ..."
[200]: https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/publications/2020/GLSVLSI20_None.pdf "MNSIM 2.0: A Behavior-Level Modeling Tool for Memristor- ..."
[201]: https://github.com/thu-nics/MNSIM-2.0 "thu-nics/MNSIM-2.0: A Behavior-Level Modeling ..."
[202]: https://arxiv.org/pdf/2004.10971 "An Open-source Simulation Framework for Memristive ..."
[203]: https://memtorch.readthedocs.io/ "MemTorch — MemTorch 1.1.6 documentation"
[204]: https://github.com/coreylammie/MemTorch "coreylammie/MemTorch: A Simulation Framework for ..."
[205]: https://www.sciencedirect.com/science/article/abs/pii/S0925231222002053 "MemTorch: An Open-source Simulation Framework for ..."
[206]: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2021.659060/full "NeuroSim Simulator for Compute-in-Memory Hardware ..."

---

## 18. Аппаратно-программные стеки и toolchain для AIMC-LLM 

Ниже — практический, «инженер-ориентированный» разбор полного toolchain’а для разработки, маппинга, запуска и отладки LLM/Transformer-нагрузок на AIMC (memristor/PCM/RRAM) платформах. Для каждого подпункта: что делать, какие инструменты использовать, какие метрики собирать и какие типичные параметры/конфигурации выбирать.

> Краткая идея: рабочий pipeline состоит из трёх уровней—(1) **model/HWA-training** (PyTorch + AIHWKit/AIHWKit-Lightning), (2) **array/accuracy validation** (CrossSim / device→array sweep), (3) **system/runtime** (MNSIM/NeuroSim + chip firmware / monitor). Каждый уровень имеет свои артефакты (tile maps, calibration tables, telemetry) и обязан поддерживать интерфейс следующему уровню. ([aihwkit.readthedocs.io][207])

---

### 18.1. Mapping / partitioning: compiler support, tiling, routing weights across tiles

#### Задача и критерии

Цель mapping-а — разложить большие матрицы трансформера (проекции Q/K/V, FFN, embedding tables) на физические tiles/crossbar так, чтобы:

* минимизировать меж-тайловую передачу partial-sums;
* удовлетворять ограничениям tile-size (например 256×256 или 512×512), ADC-битности и драйверов;
* обеспечить баланс по нагрузке (температура/энергия) и учесть репликацию/differential encoding для SNR. ([aihwkit.readthedocs.io][207])

#### Инструменты и возможности компилера

* **AIHWKit (mapping API)** — предоставляет primitives для разбиения слоёв на tiles, класс-описания tile (tile_array_class) и параметры маппинга (stride, split, differential encoding). Это позволяет программно описать, как именно матрицы разбиваются и в каком порядке программируются tiles. ([aihwkit.readthedocs.io][208])
* **AIHWKit-Lightning / Analog-MoE extensions** — оптимизированы под LLM/MoE: масштабируемые стратегии маппинга, батч-параллелизм и шаблоны routing для условного актива (MoE). Они включают готовые паттерны partitioning (bank-per-expert, shard по входному/выходному измерению) и ускоренные утилиты для генерации tile-layouts. ([IBM Research][209])

#### Практический workflow для маппинга

1. **Проанализировать слой**: счёт параметров, плотность заполнения (sparsity) и требуемую точность.
2. **Выбрать tile size** (обычно 256–512): для больших FFN — крупные плитки; для критичных слоёв (attention projections) — мелкие, с меньшей репликацией. ([aihwkit.readthedocs.io][207])
3. **Выбрать encoding**: differential (G⁺/G⁻) для слоёв чувствительных к SNR; replication для критичных слоёв. Учесть area-компромисс. ([Nature][210])
4. **Сгенерировать mapping table**: пер-tile метаданные — (tile_id, layer, row_range, col_range, encoding, ADC_bits, verify_policy). Это становится частью firmware и loader’а чипа. ([aihwkit.readthedocs.io][208])
5. **Симулировать в AIHWKit / AIHWKit-Lightning**: hw-aware fine-tune с учётом выбранного map → получить скорректированные веса и per-tile scale/bias. ([IBM Research][209])

#### Типовые параметры, которые нужно зафиксировать в compiler-flow

* tile_size (rows × cols), column ADC ENOB (4–8 bit), input DAC resolution (4–8 bit), differential replication factor (1,2,4), per-tile max_current, verify_policy (open-loop vs program/verify with thresholds). ([aihwkit.readthedocs.io][207])

---

### 18.2. Runtime / monitoring: profiling power, ADC load, weight-program verification

#### Что мониторить в рантайме (обязательно)

* **Power & thermal per bank/tile** (реальное потребление, hot-spot detection).
* **ADC utilization / sample rate / ENOB** (пиковая загрузка, latency при conversion).
* **Driver currents and per-column peak** (чтобы избежать overcurrent/thermal).
* **Weight program stats**: #program pulses per tile, #verify attempts, program latency distribution, programmed G histogram vs target.
* **Accuracy telemetry**: periodic test inferences on validation mini-batches to detect degradation. ([Nature][210])

#### Средства и методы профайлинга

* **On-chip telemetry agents**: microcontrollers/monitor blocks measure current/voltage/temperature per bank and stream logs. Эти данные нужны для динамического throttling (например, MoE activation scheduler). IBM/Analog-MoE designs и Ambrogio-chip используют такие монитор-агенты. ([IBM Research][211])
* **ADC load profiling**: runtime собирает статистику ADC-calls (частота, shared-ADC contention) — помогает корректировать DAC/ADC time-multiplexing и batching, чтобы не превысить latency budget. ([GitHub][212])
* **Weight programming verification (program/verify logs)**: каждый program/verify цикл логируется — распределение ΔG per pulse, число итераций программирования и failures → используется для wear-leveling и обнаружения «плохих» устройств. В прототипах write-verify — стандарт практики. ([Iris Polito][213])

#### Автоматическая реакция рантайма (policy examples)

* **Thermal throttling**: уменьшение происходящих параллельных activations (MoE) при достижении T_threshold. ([IBM Research][211])
* **Adaptive ADC resolution / time-multiplexing**: динамически снижать ENOB или использовать ADC-sharing при пиковых нагрузках для сохранения throughput. ([PMC][214])
* **Program retry policy**: ограничить verify-loops, пометить cell как «degraded» после N-fails и переключиться на резервные реплики. Логи используются для wear-leveling. ([Iris Polito][213])

#### Какие метрики сохранять в runtime log (минимум)

* timestamp, tile_id, op_type (read/write/inference), ADC_calls, ADC_latency, peak_current, tile_temp, program_pulses, verify_count, program_latency, tile_state_version, short_validation_loss. Эти поля формируют audit trail и feed для SRE/ML-ops. ([Nature][210])

---

### 18.3. Debugging analog accelerators: error visualisation, per-tile calibration

#### Основные техники отладки

1. **Per-tile calibration sweep**: программирование calibration vectors (set of orthogonal inputs) и измерение outputs → строятся per-column scale/offset maps. Эти параметры сохраняются в tile-metadata (scale,bias) и применяются в runtime. AIHWKit и CrossSim workflow включают per-tile calibration step. ([aihwkit.readthedocs.io][207])
2. **Error heatmaps / visualisation:** визуализация deviation = measured_output − expected_output по строкам/столбцам → быстро локализует «плохие» ячейки, IR-drop зоны и контроллерные артефакты. CrossSim manual показывает примеры подобных диагностик для inference и объясняет форматы вывода. ([Crossbar Simulator][215])
3. **Program/verify trace debugging:** хранение trace’ов программирования (pulse amplitudes, readback currents) — полезно для root-cause анализа failures (stuck-on/stuck-off, filament anomalies). На этапе bring-up это основной инструмент диагностики. ([Iris Polito][213])

#### Calibration SOP (практический рабочий цикл)

* **Step 0 (preprogram checks):** check tile health (leakage / stuck cells)
* **Step 1 (program nominal weights):** program using write-verify, record per-cell program attempts and final G distribution.
* **Step 2 (calibration vectors):** run N orthogonal inputs, measure outputs, fit per-column gain/offset and residual error matrix.
* **Step 3 (store compensation):** write scale/bias into metadata and upload to runtime.
* **Step 4 (short HWA fine-tune):** optional 1–3 epochs of fine-tune with HWA noise using AIHWKit emulator or on-chip (if endurance allows).
* **Step 5 (monitor):** schedule refreshes / re-calibration based on drift thresholds or elapsed time. ([aihwkit.readthedocs.io][207])

#### Инструменты отладки и визуализации

* **CrossSim’s inference manual & tools** — GPU-ускоренные sweep’ы и visual diagnostics для crossbar effect analysis (IR-drop maps, error histograms). ([Sandia National Laboratories][216])
* **AIHWKit tile state & API** — позволяет сохранять analog_tile_state и загружать calibration params; удобно для интеграции в CI/bring-up scripts. ([aihwkit.readthedocs.io][217])
* **On-chip dashboards** (telemetry viewer) — custom dashboards показывают per-tile health and trending (power/verify rates/temperature). Ambrogio-like systems expose similar telemetry for system operators. ([Nature][210])

---

### 18.4. Рекомендации по интеграции toolchain в CI/CD и MLOps

1. **Версионирование map & tile metadata**: храните map tables, tile firmware и calibration tables в git + artifact registry; при каждом изменении модели создавайте новый mapping-artifact. ([aihwkit.readthedocs.io][207])
2. **Pre-deploy HWA regression**: CI запускает HWA-retrain + CrossSim sweep (coverage of σ_noise/ADC_bits) и сравнивает mapped_acc vs baseline; откат при деградации > ε. ([IBM Research][209])
3. **On-device canary & rolling deploy**: выкатывайте сначала на небольшой набор tiles (canary), мониторьте program/verify stats и drift; только после успешной валидации — roll-out. ([Nature][210])

---

### 18.5. Набор «must-have» артефактов (что должен генерировать toolchain для каждой версии модели)

* mapping_table.json (tile layout + encoding + ADC config).
* per_tile_calibration/{tile_id}.json (scale, bias, last_program_ts, program_stats).
* tile_health_report.csv (D2D failures, stuck cell list, estimated remaining_endurance).
* runtime_policy.yaml (thermal thresholds, program_retry_policy, refresh_schedule).
* HWA-retrain checkpoint + AIHWKit config (device-preset + noise params). ([aihwkit.readthedocs.io][207])

---

### 18.6. Сводка инструментов по этапам (cheat-sheet)

* **Model → HWA training & mapping:** AIHWKit + AIHWKit-Lightning (scale, QAT, mapping API). ([aihwkit.readthedocs.io][207])
* **Array → accuracy sweep & calibration diagnostics:** CrossSim (IR-drop, error maps, inference manual). ([Sandia National Laboratories][216])
* **System runtime / scheduling / telemetry:** custom firmware with on-chip telemetry; reference architectures and policies in IBM Analog-MoE / Ambrogio systems. ([IBM Research][211])
* **Architecture DSE:** MNSIM / NeuroSim for tile/bank/3D stack exploration. ([IBM Research][211])

---

### 18.7. Быстрые рекомендации (engineering rules of thumb)

* **Сначала HWA-retrain, потом map; не наоборот.** HWA-retrain с моделью, эмулирующей выбранный tile/ADC → генерируйте final weights для программирования. ([IBM Research][209])
* **Программируйте веса пакетно и делайте calibration сразу после programming.** Program/verify → calibration vectors → store compensation. ([Iris Polito][213])
* **Логируйте всё:** program traces и telemetry — без этого root-cause анализа failures не будет. ([Nature][210])

---

#### Основные использованные источники (для чтения и быстрой проверки)

* AIHWKit docs (mapping API, tile modules). ([aihwkit.readthedocs.io][208])
* AIHWKit-Lightning (scalable HW-aware toolkit for LLMs / Analog-MoE extensions). ([IBM Research][209])
* CrossSim manuals & site (array accuracy simulation, inference manual, diagnostics). ([Crossbar Simulator][215])
* IBM research: *Efficient Scaling of Large Language Models with Mixture of Experts and 3D analog in-memory computing* (2025). ([IBM Research][211])
* Ambrogio S. et al., *An analog-AI chip for energy-efficient speech recognition and transcription*, **Nature** (2023) — системный пример per-tile programming/replication/telemetry. ([Nature][210])

---

<details>
<summary>Детали</summary>

A) сгенерировать **пример mapping_table.json** и соответствующий per_tile_calibration template (JSON + объяснения полей),
B) подготовить **notebook-шаблон** (PyTorch + AIHWKit) для pipeline «model → HWA-retrain → export mapping_table»,
C) составить **runtime policy.yaml** (thermal thresholds, verify_policy, refresh schedule) под конкретный набор device-параметров (скажите, какие device-параметры считать — или я возьму разумные default’ы из Ambrogio / AIHWKit).

</details>

[207]: https://aihwkit.readthedocs.io/ "IBM Analog Hardware Acceleration Kit's documentation!"
[208]: https://aihwkit.readthedocs.io/en/latest/api/aihwkit.simulator.parameters.mapping.html "aihwkit.simulator.parameters.mapping module"
[209]: https://research.ibm.com/publications/aihwkit-lightning-a-scalable-hw-aware-training-toolkit-for-analog-in-memory-computing "AIHWKIT-Lightning: A Scalable HW-Aware Training Toolkit ..."
[210]: https://www.nature.com/articles/s41586-023-06337-5 "An analog-AI chip for energy-efficient speech recognition ..."
[211]: https://research.ibm.com/publications/efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog-in-memory-computing "Efficient Scaling of Large Language Models with Mixture ..."
[212]: https://github.com/IBM/aihwkit-lightning "IBM/aihwkit-lightning: Scalable HW-Aware Training ..."
[213]: https://iris.polito.it/bitstream/11583/2996345/2/s41467-024-45670-9_compressed.pdf "Hardware implementation of memristor-based artificial neural ..."
[214]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10912231/ "Hardware implementation of memristor-based artificial ..."
[215]: https://cross-sim.sandia.gov/app/uploads/sites/110/2021/09/crosssim_manual.pdf "ROSS SIM - CrossSim: Crossbar Simulator"
[216]: https://www.sandia.gov/app/uploads/sites/110/2022/06/CrossSim_Inference_manual_v2.0.pdf "CrossSim Inference Manual (v2.0)"
[217]: https://aihwkit.readthedocs.io/en/latest/api/aihwkit.simulator.tiles.base.html "aihwkit.simulator.tiles.base module"

---

## 19. Производство, интеграция с CMOS и 3D-stacking, yield и экономика масштаба 

Ниже — детальная, практическая и источниково-подкреплённая стратегия по выводу memristor / AIMC-технологий на производство: от технологических потоков BEOL/monolithic-3D до методов тестирования, оценки выхода годных (yield) и экономических соображений (CAPEX/OPEX, TCO). Я подчёркиваю ключевые инженерные риски и даю конкретные метрики и SOP-рекомендации для команды bring-up / productization.

---

### 19.1. CMOS-integration: process flows (BEOL memristor layers vs monolithic integration)


#### 19.1.1. Два главных подхода интеграции

1. **Back-End-Of-Line (BEOL) integration (NVM на BEOL над CMOS):** стандартный практический маршрут для большинства демонстрационных AIMC-чипов — сначала делают CMOS «front-end» в коммерческом foundry (например, 14 nm), затем добавляют NVM / memristor (PCM, RRAM и др.) в BEOL (последние металлизационные уровни) в специализированных подразделениях (example: IBM Albany NanoTech Center для PCM). BEOL-путь уже продемонстрирован в крупных прототипах (14 nm + PCM на 300-мм). ([Nature][218])
2. **Monolithic 3D (M3D, monolithic vertically stacked integration):** синтез слоёв функциональных устройств (NVM/logic) подряд с тонкоплёночными процессами, без промежуточной сборки пластин; обещает меньшие задержки, плотную вертикальную связь и высокую плотность (low-latency vertical vias), но требует совместимых температурных budget’ов и выдерживания CMOS-условий (high-temp steps ограничены). M3D активно исследуется как путь к масштабированию 3D-AIMC. ([ScienceDirect][219])

> Практическое следствие: для быстрой коммерциализации — BEOL над CMOS-flow; для максимальной плотности и будущих datacenter-bank → monolithic 3D остаётся приоритетной R&D-целью. ([Nature][218])

#### 19.1.2. Типичный BEOL-flow (практический порядок шагов)

1. **Front-end CMOS fabrication** (foundry standard flow, e.g. 14 nm) — logic, periph, drivers, ADC/DAC CMOS ядро.
2. **BEOL metallization up to a process plane** — подготовка верхних металлов с контактными площадками.
3. **Deposition / patterning of memristive stack** (e.g., PCM: bottom electrode, GST layer, top electrode; RRAM: metal/oxide/metal). Требуются точные litho/etch и чистая среда.
4. **Back-end anneal / low-T steps** — температурные ограничения (обычно < ~400 °C) критичны, чтобы не разрушить CMOS. Это ограничивает материалы и процессы.
5. **Via-formation и BEOL interconnect** — подключение memristor arrays к CMOS периферии (drivers, sense amps).
6. **Wafer-level test / singulation / packaging** и последующий wafer-sort. ([Nature][218])

#### 19.1.3. Ограничения материалов и температур

* BEOL-процессы должны укладываться в **low-thermal budget** (обычно ≤400 °C и часто ≪400°C) — это ограничивает выбор фазовых и окисных материалов и требует оптимизированных deposition/anneal шагов; PCM/oxides и специализированные heaters (mushroom cell) — популярный выбор на практике. ([Nature][218])

#### 19.1.4. Почему крупные foundries и 300-mm важны

* Производство AIMC в объёмах требует 300-мм фабрик, проверенной process control и supply-chain для metrology / yield control. Крупные демонстраторы (Ambrogio et al.) уже использовали 300-мм wafer flow с BEOL PCM, что показывает технологическую жизнеспособность BEOL-маршрута для масштабируемых сборок. ([Nature][218])

---

### 19.2. 300-mm fabs, yield, тестовые методики для больших массивов memristor

#### 19.2.1. Основные метрики выхода годных и их значение для AIMC

* **Device yield (per-cell):** доля исправных переключающихся ячеек.
* **Array yield / usable tile yield:** доля tile/array, проходящих acceptance criteria (accuracy/tolerance). Для AIMC-продуктов важен «functional yield» (можно ли достичь требуемой accuracy после calibration/replication), а не только raw device yield.
* **Effective yield (after redundancy и repair):** учитывает spare rows/cols, ECC, replication/differential encoding. ([knowen-production.s3.amazonaws.com][220])

#### 19.2.2. Тестовые методики (wafer→chip→system)

1. **Wafer-level parametric tests (short-flow):** массовые параллельные param tests, characterizing I–V, switching thresholds, initial R_on/R_off, variability statistics — быстрый screening до dicing. (Short-flow методики позволяют экономить время и деньги при ранних этапах NVM тестирования.) ([PDF 솔루션][221])
2. **Array functional tests / programming trials:** program/verify sequences, ΔG per pulse distribution, endurance/retention spot-tests (accelerated). Это даёт статистику программируемости и первого-поколения drift. ([pubs.acs.org][222])
3. **Accelerated aging & Arrhenius tests:** температурно-ускоренные тесты для предсказания retention и жизненного цикла. Важны для projection of deployed lifetime. ([pubs.acs.org][222])
4. **Post-pack system validation:** full-stack end-to-end tests: программирование больших весов, calibration sweep, HWA inference с эталонной моделью (software baseline vs mapped accuracy). Это решающий этап acceptance. ([Nature][223])

#### 19.2.3. Методы повышения effective yield

* **Redundancy (spare rows/cols) + on-chip repair mapping.**
* **Differential encoding + replication:** повышает SNR, но увеличивает area. При проектировании product-level tile-budget нужно заранее включать replication factor. ([Nature][218])
* **Built-in self test (BIST) & factory calibration:** автоматические процедуры для per-tile calibration и bad-cell mapping на этапе производства. ([TU Delft Research Portal][224])
* **Defect-aware mapping & ECC:** адаптивный mapp­ing, который избегает «плохих» ячеек в ключевых местах и применяет ECC к чувствительным слоям. ([knowen-production.s3.amazonaws.com][220])

#### 19.2.4. Математика yield modelling (practical rule)

* Простая модель: если per-cell yield = p, tile содержит N cells, вероятность, что tile без дефектов ≈ p^N — для больших N это быстро падает → практическая стратегия — допустимый percentage дефектов + redundancy/repair + ensemble approach. Поэтому **effective yield** часто моделируют с учётом spare rows/cols и replication, а не raw p^N. (Literature: yield estimation papers и практики ReRAM arrays). ([ResearchGate][225])

---

### 19.3. Экономика: CAPEX/OPEX и сравнение с GPU-центрами (TCO для LLM-инференса)

#### 19.3.1. CAPEX: что дорого при запуске AIMC-линии

* **Fab modifications / BEOL tooling:** интеграция NVM в BEOL/замещение process steps требует инвестиции (или договор с fab-партнёром); если делаете M3D — требуется R&D и process development equipment.
* **Advanced packaging / 3D stacking costs:** TSVs, micro-bumps, thermal interfaces и advanced packaging для 3D stacks серьёзно увеличивают per-wafer/pack cost. ([ScienceDirect][219])

#### 19.3.2. OPEX: где экономия и где расходы

* **Снижение energy bills при инференсе:** AIMC демонстрирует существенную выгоду energy/MAC (peer-reviewed прототипы показывают десятки–сотни fJ/MAC), что прямо влияет на OPEX для inference-heavy workloads. IBM и другие показывают многократные преимущества в энергоэффективности для inference-кейсов. ([Nature][218])
* **Техобслуживание / refresh / replacement:** в OPEX входят периодические refresh-ы, калибровки, возможная замена деградированных tiles — это реальный operational cost для NVM-платформ.

#### 19.3.3. TCO / break-even соображения

* **Переменные, влияющие на break-even:** энергоэкономия на inference (руб/токен), utilisation (загрузка hardware), стоимость интеграции/сбора (CAPEX), стоимость охлаждения (AIMC может снизить cooling CAPEX/OPEX), инженерные расходы на bring-up и поддержание ecosystem.
* **Практическая заметка:** аналитические отчёты и IBM-декларации (prototype claims) указывают на значительное energy-gain; однако реальные TCO-сравнения зависят от utilisation: при низкой загрузке (много простоя) экономика собственных кластеров часто хуже, чем аренда cloud API. Маркет-аналитики подчёркивают, что только при высокой, стабильно загруженной инференс-нагрузке AIMC/специализированные ASICs начинают выигрывать по TCO. ([IDTechEx][226])

#### 19.3.4. Консервативная практическая оценка

* Используйте scenario analysis: (A) conservative: include 2–3× CAPEX uplift vs GPU server for prototype fabs and packaging; (B) optimistic: use foundry BEOL partnerships (outsourced BEOL at specialized integration center) to reduce CAPEX; (C) run break-even token-volume calc (tokens/day × energy_saving_per_token vs CAPEX_diff amortized). IBM и IDTechEx материалы дают входные параметры/диапазоны для energy savings и рыночных прогнозов. ([IBM Research][227])

---

### 19.4. Риски, баттон-апы и mitigation strategies (engineering playbook)

#### Ключевые риски

1. **Yield cliff при масштабировании массивов** — решается redundancy, replica, selective mapping. ([TU Delft Research Portal][224])
2. **Thermal / reliability проблемы 3D stacks** — требуется thermal-aware scheduling и conservative activation policies. ([ScienceDirect][219])
3. **Lack of fab ecosystem / supply chain** — mitigation: partnership with established fabs (BEOL integration centers) и использование проверенных process nodes (e.g., 14 nm demo path). ([Nature][218])

#### Практические меры

* **Design for testability (DfT)**: встроенные BIST, parametric test hooks, built-in calibration vectors; автоматический factory calibration pipeline. ([PDF 솔루션][221])
* **Redundancy + adaptive mapping**: hardware/software co-design для автоматического обхода дефектов. ([knowen-production.s3.amazonaws.com][220])
* **Economic hedges**: staged investment (pilot → small prod → scale), use of foundry BEOL services to reduce CAPEX spike. ([IBM Research][228])

---

### 19.5. Что измерять и репортить при выводе продукта (обязательный минимальный набор метрик)

1. **Per-cell switching statistics:** R_on/R_off, ΔG per pulse distribution, set/reset voltages. ([pubs.acs.org][229])
2. **Tile/array functional yield:** fraction of tiles passing acceptance (functionality after calibration). ([Nature][218])
3. **Endurance & retention projections:** measured cycles to failure, Arrhenius-extrapolated retention times. ([pubs.acs.org][222])
4. **Energy breakdown (core vs ADC/DAC vs periphery):** fJ/MAC numbers and system-level energy/token. ([Nature][218])
5. **TCO projections:** CAPEX, amortized per token costs under different utilisation scenarios. (Include sensitivity analysis.) ([Semiconductor Engineering][230])

---

### 19.6. Ключевые источники (must-read)

* A. Sebastian et al., *Memory devices and applications for in-memory computing*, **Nat. Nanotech.** 2020 — фундаментальный обзор device → system. ([knowen-production.s3.amazonaws.com][220])
* S. Ambrogio et al., *An analog-AI chip for energy-efficient speech recognition and transcription*, **Nature** 2023 — 14 nm front-end + BEOL PCM на 300-мм, system demo и manufacturing комментарии. ([Nature][218])
* F. Aguirre et al., *Hardware implementation of memristor-based artificial neural networks*, **Nat. Commun.** 2024 — обзор device→system, включая вопросы производственного вывода и тестирования. ([Nature][231])
* Y. Fan / Jeon et al., *Monolithic 3D integration reviews* (2024) — современное обсуждение M3D и его trade-offs. ([ScienceDirect][219])
* D. Ielmini et al., *RRAM / resistive memory reviews and testing* (Chem. Rev. / ACS Nano review items) — методы characterisation, endurance/retention standards. ([pubs.acs.org][229])
* IBM Research: *Efficient Scaling of LLMs with Mixture of Experts and 3D analog in-memory computing* (2025) and IBM blog posts — архитектурные и экономические соображения для LLM-scale AIMC. ([IBM Research][228])

---

### 19.7. Краткий actionable checklist для практической команды (bring-up / productization)

1. Выбрать завод-партнёра для BEOL (300-mm facility) или подготовить M3D R&D schedule. (Если нужен быстрый time-to-market — BEOL на proven node.) ([Nature][218])
2. Провести device-audit: ΔG distributions, endurance, retention (accelerated), temperature sensitivity. ([pubs.acs.org][222])
3. Спроектировать redundancy/replication budget заранее (рамки area overhead и target effective yield). ([TU Delft Research Portal][224])
4. Разработать wafer-level short-flow tests и BIST; автоматизировать factory calibration pipeline. ([PDF 솔루션][221])
5. Провести scenario-TCO analysis: energy savings × utilisation vs CAPEX uplift; определить break-even token-volume. ([Semiconductor Engineering][230])

---

#### Заключение

Технология memristor-AIMC уже перешла от «lab curiosity» к prototype-production: BEOL-integrated PCM/RRAM на 300-мм показаны в крупных демонстраторах (см. Ambrogio 2023), а monolithic 3D остаётся перспективной, но более рискованной R&D-дорогой для экстра-высокой плотности. Основные барьеры для масштабного коммерческого развёртывания — **yield, тестирование/производственные методики и экономика (CAPEX vs OPEX)**; их практическое решение требует tight HW/SW co-design, фабричных партнёрств и зрелых test/repair flows. ([Nature][218])

---

<details>
<summary>Детали</summary>

* A) **Production SOP (PDF)**: wafer-level test checklist + sample test vectors + acceptance thresholds (JSON/CSV); или
* B) **TCO-модель-шаблон (spreadsheet)**: вводные: CAPEX, energy_saving_per_token, utilisation → break-even months; заполню realistic defaults на базе Ambrogio/IBM/IDTechEx; 

</details>

[218]: https://www.nature.com/articles/s41586-023-06337-5   "An analog-AI chip for energy-efficient speech recognition ..."
[219]: https://www.sciencedirect.com/science/article/abs/pii/S1359028624000652   "Monolithic 3D integration as a pathway to energy-efficient ..."
[220]: https://knowen-production.s3.amazonaws.com/uploads/attachment/file/5270/10.1038_s41565-020-0655-z.pdf   "Memory devices and applications for in-memory computing"
[221]: https://ko.pdf.com/wp-content/uploads/2020/05/PublishedPaper_2019-IEEE-JEDS_CrossPoint_Memory_Model_Test_PDFS_Brozek.pdf   "Design and Measurement Requirements for Short Flow ..."
[222]: https://pubs.acs.org/doi/10.1021/acsnano.1c06980   "Standards for the Characterization of Endurance in Resistive ..."
[223]: https://www.nature.com/articles/s41467-025-63794-4   "Demonstration of transformer-based ALBERT model on a ..."
[224]: https://research.tudelft.nl/files/123590808/PhD_Dissertation_Moritz_Fieback.pdf   "Testing RRAM and Computation-in-Memory Devices"
[225]: https://www.researchgate.net/publication/343039984_Yield_Estimation_of_a_Memristive_Sensor_Array   "Yield Estimation of a Memristive Sensor Array | Request PDF"
[226]: https://www.idtechex.com/en/research-report/ai-chips-for-data-centers-and-cloud/1095   "AI Chips for Data Centers and Cloud 2025-2035"
[227]: https://research.ibm.com/blog/analog-ai-chip-inference   "An energy-efficient analog chip for AI inference"
[228]: https://research.ibm.com/publications/efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog-in-memory-computing   "Efficient Scaling of Large Language Models with Mixture ..."
[229]: https://pubs.acs.org/doi/10.1021/acs.chemrev.4c00845   "Resistive Switching Random-Access Memory (RRAM)"
[230]: https://semiengineering.com/understanding-the-total-cost-of-ownership-in-hpc-and-ai-systems/   "Understanding The Total Cost Of Ownership In HPC And AI ..."
[231]: https://www.nature.com/articles/s41467-024-45670-9   "Hardware implementation of memristor-based artificial ..."

---

## 20. Бенчмарки, метрики и экспериментальные протоколы 

Ниже — практическое руководство («how-to») по честной, воспроизводимой и сопоставимой валидации AIMC-систем (memristor / analog in-memory). Содержит (1) точные определения измеряемых метрик и методику получения energy/MAC с учётом ADC/DAC-overhead; (2) шаблон репортов (latency/throughput/accuracy + reproducibility checklist); (3) рекомендуемые мини-бенчмарки (vision / audio / text) и протоколы для long-term / accelerated tests. Основные принципы опираются на крупные обзорные и экспериментальные работы по AIMC и на инструменты hw-aware training / simulators (AIHWKit, CrossSim, Ambrogio / NeuRRAM / Rasch и др.). ([knowen-production.s3.amazonaws.com][232])

---

### 20.1. Как корректно измерять energy/MAC и учитывать ADC/DAC overhead

#### 20.1.1. Определения (чётко и однозначно)

1. **MAC** — умножение-аккумулирование (multiply-accumulate) для одного элемента (a·w + partial_sum).
2. **Energy per MAC (E_MAC)** — суммарная энергия, затраченная системой на один MAC в реально исполняемой конфигурации: $E_{MAC} = E_{analog_core_per_MAC} + E_{ADC/DAC_per_MAC} + E_{interconnect_per_MAC} + E_{periphery_per_MAC}$ где каждый член — реально измеряемая составляющая (см. 20.1.3). ([Nature][233])

#### 20.1.2. Почему простое «TOPS/W → fJ/MAC» может вводить в заблуждение

* Простая конверсия 1 TOPS/W ≈ 1 pJ/MAC (обратная величина) даёт грубую оценку, но **она не учитывает**: ADC/DAC энергию, overhead меж-тайловой передачи partial-sums, контроллеры, refresh/program cost и режимы time-multiplexing. При реальном system-level бенчмарке все эти расходы нужно явно детализировать. Ambrogio / NeuRRAM показывают, что system-level цифры зависят от архитектурных trade-offs (replication, ADC-ENOB, tiling). ([Nature][233])

#### 20.1.3. Практическая методика измерения (стандартный протокол)

1. **Разбить систему на слои затрат** и измерять/оценивать каждую отдельно:
   a. *Analog core* — измерять токо-/напряжение на crossbar во время VMM; интегрировать по времени (например, осциллограф + шунт / высокоскоростный ватт-метр).
   b. *ADC/DAC* — измерять энергопотребление ADC и DAC при реальном режиме (битность, sample rate); если ADC shared, учитывать amortized cost per read.
   c. *Interconnect & digital accumulation* — подсчитать energy цифровой передачи partial sums и цифровой accumulation (содержится в SoC-логике).
   d. *Program/verify* (если training/fine-tune) — измерить энергию и время одного program/verify цикла и выразить как energy_per_update. ([GitHub][234])

2. **Как перейти от измерений к E_MAC:**

   * Измерить энергию полного inference/inference-batch (E_total) для заданного workload; посчитать суммарное число MACs выполненных за это время (N_MAC). Тогда: $E_{MAC} = \frac{E_{total}}{N_{MAC}}$
   * Но дополнительно дать детализованный breakdown: E_analog, E_ADC, E_interconnect, E_program (если применимо). Такой breakdown обязателен для корректного сравнения с GPU/TPU. Ambrogio и NeuRRAM демонстрируют важность такой декомпозиции в публикациях. ([Nature][233])

3. **Учёт shared-ADC / time-multiplexing:** если ADC общий и обслуживает несколько колонок, измерьте его *пиковую* и *среднюю* нагрузку; амортизируйте энергию ADC по количеству MACs, обслуженных за период: $E_{ADC/ per_MAC} = \frac{E_{ADC_total_per_cycle}}{N_{MAC_served}}$

4. **Учитывайте conversion overhead при малых батчах / latency-sensitive режимах.** Малые батчи повышают амортизированную долю ADC/DAC в E_MAC, поэтому в отчёте всегда показывайте режимы (batch size, concurrency). ([Nature][233])

#### 20.1.4. Пример численного расчёта (показательный)

* Допущения: chip-sustained measurement E_total = 0.81 J за N_MAC = 10¹³ MAC → E_MAC = 81 fJ/MAC. При этом breakdown: E_analog = 50 fJ, E_ADC = 20 fJ, E_interconnect = 8 fJ, E_periphery = 3 fJ. Такой стиль подачи — предпочитаемый, потому что показывает, откуда берётся выигрыш. (см. Ambrogio 2023 / NeuRRAM 2022 как примеры). ([Nature][233])

---

### 20.2. Репорты: latency, throughput, accuracy (task-specific) и reproducibility checklist

#### 20.2.1. Обязательные метрики для публикации / отчёта (минимум)

1. **Software baseline** — модель и точность в FP32/FP16 (dataset + seed).
2. **Mapped (hw) accuracy** — точность на реальном железе *после* programming + calibration (t₀), и её статистика (mean ± std over N runs).
3. **Energy breakdown:** E_total and decomposition (analog core, ADC, DAC, digital accumulation, program/verify).
4. **Latency / throughput:** latency per inference (p99), throughput (inferences/sec or tokens/sec) при заданной batch size и concurrency. Указывайте и п95/p99 latency.
5. **Write metrics (если training/fine-tune):** writes per weight per epoch, average pulses per update, program latency distribution. Это критично для endurance projections. ([PMC][235])

#### 20.2.2. Расширенная таблица репорта (рекомендуемый формат)

Колонки (пример):
`Work | Device | Chip/Tile config | Tile size | ADC bits | Batch size | Baseline acc | Mapped acc (t0) | Mapped acc (t24h) | E_total (J) | E/MAC (fJ) | E_core | E_ADC | Writes/epoch | Projected_lifetime | Notes`

Такой формат помогает сравнивать работы и видеть trade-offs (accuracy vs energy vs endurance). Ambrogio и Rasch приводят аналогичные breakdowns в своих публикациях. ([Nature][233])

#### 20.2.3. Reproducibility checklist (обязательные артефакты)

Для воспроизводимости и peer review приложите/опубликуйте:

1. **Model code + weights** (FP32 baseline) и seed.
2. **Mapping table** (tile layout, encoding, replication, per-tile scale/bias).
3. **Calibration scripts & raw calibration data** (per-tile measured outputs for calibration vectors).
4. **Raw runtime traces (anonymized)**: power traces, program/verify logs, ADC call logs (в формате csv).
5. **HWA-simulation config** (AIHWKit config file, device-preset JSON), чтобы можно было эмулировать на другом оборудовании. AIHWKit / CrossSim примеры показывают, как снабдить публикацию этими файлами. ([GitHub][234])

#### 20.2.4. Статистика и runs

* Выполнить ≥5 независимых runs для accuracy/energy; лучше ≥10 при высокой вариабельности device. Для retention/drift предъявлять time-series: t ∈ {0, 1h, 24h, 1w, 1m} или Arrhenius-accelerated equivalent с прозрачной эксплойтацией. Rasch и Ambrogio подчеркивают важность time-series отчётов. ([PMC][235])

---

### 20.3. Рекомендуемые datasets / benchmarks для AIMC (vision / audio / text mini-benchsets)

#### 20.3.1. Парадигма выбора benchmark-ов для AIMC

* **Small, well-understood tasks** для быстрой лабораторной итерации (MNIST, CIFAR-10/100, Google Speech Commands). Эти задачи позволяют быстро измерять accuracy vs hardware noise. NeuRRAM и Gao широко использовали их. ([Nature][236])
* **Representative, medium-scale tasks** (TinyImageNet, subset of ImageNet, LibriSpeech/TTS subsets, GLUE tasks/SQuAD/CoLA) для демонстрации real-world behaviour и latency/throughput. Ambrogio/ALBERT-demo использовали speech/NLP tasks as intermediate scale demos. ([Nature][233])
* **Task-specific microbenchmarks for LLM mapping:** small transformer benchmarks (Wikitext-2 LM, LAMBADA small slices, SST-2 / MRPC from GLUE) — useful for comparing mapping strategies, LoRA effects and quantization. (ALBERT analog demo is an example of transformer mapping to analog). ([Nature][233])

#### 20.3.2. Конкретный рекомендованный mini-benchset (быстро воспроизводимый)

**Vision:**

* CIFAR-10 (full) — quick accuracy check.
* TinyImageNet (64×64 subset) — medium complexity.
  **Audio:**
* Google Speech Commands (v2, subset) — classification & latency sensing.
* LibriSpeech test-clean subset (short segments) — simple ASR throughput test.
  **Text / NLP:**
* Wikitext-2 (LM perplexity) — small LM task.
* SST-2 (sentiment) or MRPC (sentence pair) — classification tasks for transformer mapping.
  **Control / sensor:**
* Gao et al. style binaural auditory localization dataset — for in-situ training demos. ([Nature][237])

> Пояснение: такие mini-бенчи дают баланс между воспроизводимостью, скоростью запуска и релевантностью к реальным задачам. Для LLM-скейла требуется отдельный pipeline (см. разделы 14/18), но mini-benchset достаточен для initial claims. ([Nature][233])

#### 20.3.3. Новые инициативы и стандарты

* **AnalogNAS-Bench (2025, preprint)** — первая попытка стандартизировать NAS/benchmarks для AIMC; полезна для исследований в направлении архитектурно-чувствительных метрик. Включайте такие emerging-benchmarks в supplement при доступности. ([arXiv][238])

---

### 20.4. Протоколы long-term / accelerated testing (retention / endurance / drift)

1. **Accelerated retention (Arrhenius) test:** измерять G(t) при повышенных температурах и экстраполировать к эксплуатационным температурам с указанием модели (Arrhenius parameters). Отчёт всегда должен включать методику экстраполяции. ([PMC][235])
2. **Endurance sweep:** program/erase cycling до failure для sample set (Ncells ≫ 1000) — строить survival-curve и median cycles to failure. Указывать write-pulse амплитуды & ширины. ([PMC][235])
3. **Drift & accuracy over time:** periodic inference checks (t0, t1, t24h, t1w, …) с тем же calibration policy; публиковать accuracy(t) и G(t) распределения. ([Nature][233])

---

### 20.5. Практический checklist для лабораторного бенчмарка (шаблон эксперимента)

1. Подготовка: установить AIHWKit/ CrossSim конфиги, baseline model + seed. ([GitHub][234])
2. Device audit: измерить ΔG per pulse, D2D σ, write-energy, minimal pulse widths. ([PMC][235])
3. Program + calibration: program weights → run calibration vectors → store scale/bias. ([Nature][233])
4. Inference run (repeated N times): измерить E_total (power meter + telemetry), latency distributions, accuracy. Сохранить raw traces. ([Nature][233])
5. Reporting: собрать таблицу (см. 20.2.2), опубликовать mapping table + calibration data + HWA config. ([GitHub][234])

---

### 20.6. Ключевые источники (must-read для этого раздела)

* A. Sebastian et al., *Memory devices and applications for in-memory computing*, **Nat. Nanotechnol.** 2020 — обзор device→system и рекомендации по метрикам. ([knowen-production.s3.amazonaws.com][232])
* S. Ambrogio et al., *An analog-AI chip for energy-efficient speech recognition and transcription*, **Nature** 2023 — пример system-level measurement и energy breakdown (chip-sustained TOPS/W). ([Nature][233])
* W. Wan et al. (NeuRRAM), *A compute-in-memory chip based on RRAM*, **Nature** 2022 — набор реальных benchmark-кейсов (vision/audio) и измерения energy/accuracy. ([Nature][236])
* M.J. Rasch et al., *Fast and robust analog in-memory deep neural network training*, **Nat. Commun.** 2024 — методики измерения влияния non-idealities на training и рекомендации по endurance/drift reporting. ([PMC][235])
* IBM AIHWKit docs / tutorials — практики HWA-training, mapping и reproducibility artifacts. ([GitHub][234])
* B. Gao et al., *Memristor-based analogue computing for brain-inspired sound localization with in-situ training*, **Nat. Commun.** 2022 — примеры application-level tests и energy-focused demos. ([Nature][237])

---

### 20.7. Краткие рекомендации — «правила честного сравнения»

1. **Всегда приводите energy-breakdown**, а не только aggregate TOPS/W. Без breakdown сравнение бессмысленно. ([Nature][233])
2. **Сравнивайте «end-to-end» (system) numbers**, включая периферию и interconnect, а не только core MAC-energy. ([Nature][236])
3. **Публикуйте mapping + calibration + raw traces** для воспроизводимости; используйте AIHWKit/ CrossSim конфиги как supplement. ([GitHub][234])
4. **Отдельно считайте эффект batch-size и ADC sharing** — амортизация ADC сильно меняет E_MAC при разных latency-режимах. ([Nature][233])

---

<details>
<summary>Детали</summary>

* A) **сгенерировать шаблон-таблицу (CSV)** для публикации результатов (включит все поля из 20.2.2), либо
* B) **подготовить Jupyter-notebook-шаблон** (PyTorch + AIHWKit + CrossSim skeleton) для запуска reproducible mini-bench (CIFAR-10 + Speech Commands) с автоматическим сбором energy/latency/accuracy и экспортом mapping/cali files, или
* C) **сформировать короткий checklist (PDF)** «How to submit an AIMC benchmark» с mandatory artifacts для рецензирования.

</details>

[232]: https://knowen-production.s3.amazonaws.com/uploads/attachment/file/5270/10.1038_s41565-020-0655-z.pdf "Memory devices and applications for in-memory computing"
[233]: https://www.nature.com/articles/s41586-023-06337-5 "An analog-AI chip for energy-efficient speech recognition ..."
[234]: https://github.com/IBM/aihwkit "IBM/aihwkit: IBM Analog Hardware Acceleration Kit"
[235]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335942/ "Fast and robust analog in-memory deep neural network ..."
[236]: https://www.nature.com/articles/s41586-022-04992-8 "A compute-in-memory chip based on resistive random- ..."
[237]: https://www.nature.com/articles/s41467-022-29712-8 "Memristor-based analogue computing for brain-inspired ..."
[238]: https://arxiv.org/abs/2506.18495 "A NAS Benchmark for Analog In-Memory Computing"

---


## 21. Приложения: edge-LLM, роботы, автономные системы, BCI и медтех 

Ниже — подробный, практический разбор целевых применений AIMC / мемристорных и нейроморфных платформ. Для каждой подсекции даю (1) зачем AIMC здесь полезно, (2) ключевые технические требования и ограничения, (3) примеры демонстраций / публикаций, (4) практические рекомендации и чек-листы для инженера/исследователя. Все важные утверждения опираются на авторитетные рецензируемые источники и официальные руководства. ([Nature][239])

---

### 21.1 Edge inference: privacy, latency, energy constraints — где AIMC выигрывает

#### 21.1.1 Почему AIMC/мемристоры подходят для edge

* **Энергоэффективность при VMM.** Analog-in-memory дает большой выигрыш в энергии/MAС (т.е. fJ–10⁰ fJ/MAC в опубликованных прототипах), что критично для батарейных и low-power edge-устройств. Это позволяет держать LLM-подобные модели в режиме реального времени с низким энергопотреблением и уменьшенной потребностью в удалённой связи. ([Nature][239])
* **Низкая латентность для локального отклика.** Параллельная природа crossbar VMM сокращает время вычисления больших матричных проекций — выгодно для задач с жёсткими требованиями по задержке (интерактивные ассистенты, голосовой контроль на устройстве). ([Nature][239])
* **Конфиденциальность и автономность.** Обработка данных локально снижает риск утечек чувствительных данных и уменьшает зависимость от сетей/облака (важно для персональных и медицинских приложений). ([Nature][239])

#### 21.1.2 Технические требования / ограничения для edge-LLM

* **Какие части модели маппить на analog:** большие dense/FFN-проекции и embedding-таблицы; оставлять softmax/LayerNorm/контроль routing в цифровом домене (см. раздел 14). ([redwood.berkeley.edu][240])
* **ADC/DAC-budget и batch-size:** при низких батчах амортизация ADC ухудшает энергопрофиль — проектировщик должен оптимизировать time-multiplexing и ADC-sharing. ([redwood.berkeley.edu][240])
* **Robustness / calibration:** для edge-deployment обязательны per-tile calibration, HWA-retrain и периодические refresh-политики. ([Nature][239])

#### 21.1.3 Примеры и демонстрации

* Обзор возможностей и ограничений AIMC — Sebastian et al. (2020). Практические прототипы показывают, что при правильной co-design стратегия «pretrain off-chip → HWA-retrain → analog inference + LoRA for on-device adaptation» — наиболее прагматичная. ([Nature][239])

#### 21.1.4 Практический чек-лист для инженера (edge)

1. Оценить рабочую нагрузку: latency budget, средний batch size, p99 latency.
2. Выбрать слои для маппинга: FFN/embeddings → analog; softmax/LayerNorm → digital.
3. Смоделировать energy/ADC amortization для целевых batch size (AIHWKit/CrossSim).
4. Провести HWA-retrain + per-tile calibration; предусмотреть refresh policy. ([Nature][241])

---

### 21.2 Robotic control / автономные системы: real-time adaptation и on-device learning (SNN + memristors)

#### 21.2.1 Почему neuromorphic / AIMC полезны в робототехнике

* **Event-driven, low-latency контроль.** Нейроморфные (SNN) и AIMC подходы естественно поддерживают event-driven вычисления, что экономит энергию и уменьшает задержки в сенсор-актуаторных циклах. ([redwood.berkeley.edu][240])
* **On-device, continuous adaptation.** Для адаптации в реальном времени (онлайн calibration, локальная компенсация ошибок) выгодны локальные, аппаратно-реализуемые правила обучения (STDP, локальные апдейты), особенно когда требуется learning-in-the-loop. ([Nature][241])

#### 21.2.2 Технические требования и архитектурные паттерны

* **Архитектура:** гибрид SNN (Loihi/TrueNorth опыт) для fast control loops + AIMC для dense perception/feature extraction. Loihi-подобные платформы предлагают он-чипные правила обучения и детерминированный low-power SNN-раундтрип. ([redwood.berkeley.edu][240])
* **Timing & determinism:** контрольные задачи требуют жёсткие bound-на задержку и предсказуемости — проектирование должно учитывать worst-case ADC latency и inter-tile delays. ([redwood.berkeley.edu][240])

#### 21.2.3 Демонстрации

* Gao et al. (2022) — memristor-based analog demo для звуковой локализации с in-situ training: пример «brain-inspired» sensor→compute→actuation с низкой энергозатратой и адаптацией на аппаратуре. Это прототип, который показывает feasibility для perception→control pipelines. ([Nature][241])

#### 21.2.4 Практический чек-лист для robotic use-cases

1. Разделить pipeline: критичные control-loops → SNN/neuromorphic cores; perception/FFN → AIMC.
2. Проверить real-time гарантии: ADC-latency, interconnect, worst-case program/verify impact.
3. Протоколы safety: fail-safe цифровой path (fallback), watchdogs и thermal throttling для 3D stacks. ([Nature][241])

---

### 21.3 BCI и медтех / ассистивные устройства: регуляция, демонстраторы и риски

#### 21.3.1. Почему AIMC / искусственные нейроны интересны для BCI и медтех

* **Низкая потребляемая энергия и «bio-compatible» параметры.** Новые «искусственные нейроны», которые по амплитуде, энергии и временным характеристикам ближе к биологическим, открывают путь к bio-hybrid интерфейсам и более эффективным neurorprosthetics. Fu et al. (2025) демонстрируют artificial neurons с параметрами, сопоставимыми с биологией — важный шаг для совместимых интерфейсов. ([Nature][242])
* **Memristor-synapse + neuromorphic decoder** даёт low-power on-chip decoding для BCI (реальное применение: нейро-контроллеры и assistive-устройства). Примеры показывают совместимость memristor-чипов с BCI-декодерами. ([ResearchGate][243])

#### 21.3.2 Регуляторные и клинические требования (must-read)

* **FDA guidance** для имплантируемых BCI-устройств и для device-software: требования к non-clinical тестам, валидации, безопасности и документации (протоколы IDE/PMA). Любой проект BCI/имплантируемого интерфейса должен следовать этим рекомендациям на ранних этапах. ([U.S. Food and Drug Administration][244])
* **Клинические испытания и валидация:** довести device-level reliability (retention/endurance), biocompatibility, электростимуляционные риски; подтвердить эффективность на целевых эндо-пользователях в пилотных исследованиях. PMC-обзоры по BCI дают методологию translational path. ([PMC][245])

#### 21.3.3 Демонстрации / исследования

* Появляются исследования memristor-enabled neuromorphic decoders и adaptive on-chip алгоритмы для BCI (2023–2024 prototyping works). Они демонстрируют feasibility low-power, co-evolutional BCI с memristor-энейблед нейроморфной декодировкой. Однако это всё ещё ранние демонстрации, требующие долгой клинической валидации. ([ResearchGate][243])

#### 21.3.4 Этика, безопасность и риски

* **Privacy & data governance:** нейроданные крайне чувствительны; требуется строгая защита, шифрование канала, локальная обработка и минимизация хранения необработанных сигналов. ([PMC][245])
* **Fail-safe & revertibility:** implantable/assistive systems должны иметь безопасные fallback-механизмы; возможность отключения/отката прошивки без вреда пациенту — обязательна. ([U.S. Food and Drug Administration][244])

#### 21.3.5 Практический путь вывода на рынок (roadmap)

1. **R&D → bench prototyping:** device reliability + in-vitro bio-compatibility tests.
2. **Preclinical:** animal studies, accelerated aging, electrical safety.
3. **Regulatory engagement (early):** pre-sub meetings with FDA / notified bodies, согласование IDE design. ([U.S. Food and Drug Administration][244])
4. **Clinical feasibility trials → pivotal trials → approval.** На пути важны документация, traceability (S/W & H/W), и доказательство безопасной эксплуатации. ([U.S. Food and Drug Administration][244])

---

### 21.4 Общие рекомендации для всех приложений (engineering & programmatic)

1. **Не торопить клиническое применение:** демонстрация energy/latency не равна готовности к медтеху — необходим full regulatory path и долгие испытания. ([U.S. Food and Drug Administration][244])
2. **Hybrid architecture чаще всего оптимальна:** neuromorphic cores (Loihi/TrueNorth style) + memristor AIMC для perception/FFN + цифровой контроллер для safety & routing. ([redwood.berkeley.edu][240])
3. **Раннее взаимодействие с регуляторами:** особенно для BCI и имплантов — планируйте non-clinical/GLP тесты заранее. ([U.S. Food and Drug Administration][244])
4. **Пилотные поля испытаний:** начните с non-critical assistive devices (hearing aids, low-risk wearables) прежде чем переходить к имплантам. ([Nature][241])

---

### 21.5 Ключевые источники (must-read)

* Sebastian A., *Memory devices and applications for in-memory computing*, **Nature Nanotechnology** 2020 — обзор AIMC и приложений. ([Nature][239])
* Gao B. et al., *Memristor-based analogue computing for brain-inspired sound localization with in-situ training*, **Nature Communications** 2022 — demonstrator perception→control с in-situ training. ([Nature][241])
* Fu S. et al., *Constructing artificial neurons with functional parameters comprehensively matching biological values*, **Nature Communications** 2025 — artificial neurons, параметры, bio-hybrid перспективы. ([Nature][242])
* Davies M. et al., *Loihi: A Neuromorphic Manycore Processor with On-Chip Learning*, Intel (Loihi paper) — архитектура SNN с on-chip learning (benchmark для нейроморфных платформ). ([redwood.berkeley.edu][240])
* FDA guidance: *Implanted Brain-Computer Interface (BCI) Devices* — требования по non-clinical testing и регуляторный путь. ([U.S. Food and Drug Administration][244])
* Zhang H. et al., *Brain–computer interfaces: the innovative key to unlocking …* (review, 2024) — обзор translational / ethical аспектов BCI. ([PMC][245])
* Memristor chip-enabled adaptive neuromorphic decoder (2024 prototype) — примеры memristor-enabled BCI-декодеров (research demos). ([ResearchGate][243])

---

<details>
<summary>Детали</summary>

* A) собрать **checklist готовности** (PDF) для edge-LLM или BCI (включая safety/regulatory steps и список измерений), или
* B) подготовить **deployment recipe** (пошаговый pipeline) для робота: «perception on AIMC + neuromorphic control + safety fallback» с примерными конфигурациями и параметрами (tile sizes, ADC bits, expected latencies), или
* C) сгенерировать **список контактов / организаций** и call-to-action для поиска fab-/regulator-partners по подготовке клинических испытаний (список центров, useful links — FDA, major foundries).

</details>

[239]: https://www.nature.com/articles/s41565-020-0655-z "Memory devices and applications for in-memory computing"
[240]: https://redwood.berkeley.edu/wp-content/uploads/2021/08/Davies2018.pdf "Loihi: A Neuromorphic Manycore Processor with On-Chip ..."
[241]: https://www.nature.com/articles/s41467-022-29712-8 "Memristor-based analogue computing for brain-inspired ..."
[242]: https://www.nature.com/articles/s41467-025-63640-7 "Constructing artificial neurons with functional parameters ..."
[243]: https://www.researchgate.net/publication/378734680_Memristor_chip-enabled_adaptive_neuromorphic_decoder_for_co-evolutional_brain-computer_interfaces "(PDF) Memristor chip-enabled adaptive neuromorphic ..."
[244]: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing "Implanted Brain-Computer Interface (BCI) Devices for ..."
[245]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11392146/ "Brain–computer interfaces: the innovative key to unlocking ..."

---

## 22. Безопасность, надёжность, приватность нейроданных и регуляция 

Ниже — практический, исчерпывающий разбор угроз, тестов и практик безопасного развёртывания AIMC / мемристорных и нейроморфных систем в приложениях от edge-LLM до BCI/медтеха. Для каждого подпункта даю (1) какие угрозы/риски, (2) как их тестировать/симулировать, (3) какие инженерные и организационные меры применять, (4) какие регуляторные требования учитывать. Все ключевые утверждения опираются на авторитетные академические/регуляторные источники 2020–2025. ([PMC][246])

---

### 22.1. Fault injection / tampering / aging — возможные атаки и тесты

#### 22.1.1. Какие векторы атак и почему они реальны

* **Fault-injection (на аппаратном уровне):** внешние электрические/пульсовые глитчи, лазерные импульсы, локальные power glitches — могут изменить поведение отдельных ячеек, нейронов или схем управления и привести к деградации/изменению вывода сети (целевые или случайные сбои). Такие атаки продемонстрированы и для SNN/analog-neurons, и для memristor-акселераторов. ([Frontiers][247])
* **Tampering / physical compromise:** захват устройства, считывание/реверс-инжиниринг прошивки, прямой доступ к весам (readout) или к интерфейсам теста (test pads) — позволяет извлечь модель/веса или внедрить malicious firmware. ([MDPI][248])
* **Aging-based and wear attacks:** целенаправленное «переписывание» (intensive writes) определённых областей для ускорения износа (endurance exhaustion) — ведёт к деградации точности и сокращению срока службы массива. Rasch et al. подчёркивают, что endurance и retention — ключевые ограничения для тренировки и эксплуатации. ([PMC][246])
* **Side-channels & information leakage:** энергопотребление, timing, EM-излучение и ADC/DAC-шумы могут служить каналами для извлечения информации о входах/весах/нейроданных. ([MDPI][248])

(Ключевые load-bearing факты: non-idealities в устройствах влияют на устойчивость и endurance; fault injection и лазер-glitch атаки реально демонстрируются в академии.) ([PMC][246])

---

#### 22.1.2. Рекомендуемые тесты и протоколы (lab SOP)

1. **Power-glitch and clock-glitch testing:** стандартные fault-injection методы (glitch amplitude/time) для оценки эффектов на inference и on-chip learning; логировать degradation of accuracy и error modes. (использовать FPGA/board testbench). ([arXiv][249])
2. **Laser fault injection / focused energy:** локальные лазерные удары для провокации переключений/сбоев в отдельных ячейках — выявляет уязвимости к физическому атакующему действию. (применялось в исследованиях SNN/analog). ([Frontiers][247])
3. **Accelerated wear / directed write stress:** искусственно повышать цикл-записи в целевых секторах, чтобы смоделировать атакующее «сгорание» endurance; измерять survival curves и последствия для model accuracy. Rasch и другие рекомендуют явно включать endurance-sweeps в validation. ([PMC][246])
4. **Side-channel profiling:** собирать power/timing/EM-трейсы при разных входах и пытаться реконструировать вход/веса (attack simulations). Оценивайте, нужен ли encryption/obfuscation. ([MDPI][248])
5. **Fault-aware adversary simulations:** проводить software-in-the-loop эмуляции атак (bit-flips, stuck-cells, drift spikes) и запуск HWA-retrain/ensemble методов чтобы оценить resiliency. ([ACM Digital Library][250])

**Метрика риска:** report (a) accuracy drop under targeted fault; (b) number of induced fails to cross accuracy threshold; (c) mean time to degrade under directed write stress. Эти измерения нужны для SLA и для оценки mitigation cost.

---

#### 22.1.3. Техники обнаружения и смягчения на уровне hardware/firmware

* **Redundancy, ECC и replica averaging:** репликация слоёв и корреляционная обработка уменьшает влияние локальных сбоев, а ECC/repair-maps позволяют скрыть «плохие» ячейки. ([MDPI][248])
* **Runtime anomaly detection & attestation:** встроенные агенты мониторят power/verify-rates/temperature и сигнализируют о аномалиях (внезапные spikes в program/verify, unusual drift) — при подозрении выполняют graceful failover. ([PMC][251])
* **Write-rate throttling and wear-leveling:** ограничение частоты записей и балансировка обновлений по массивам уменьшают возможность targeted wear attacks. ([PMC][246])
* **Physical tamper-evidence and secure packaging:** эпоксидные/mesh-экраны, sensors for enclosure opening, secure boot chain с подписью прошивки и attestation keys в secure element. ([MDPI][248])

---

### 22.2. Конфиденциальность нейроданных, медицинская регуляция (FDA/EMA guidance для BCI)

#### 22.2.1. Почему neurodata — особая категория

* Нейроданные часто содержат очень чувствительную информацию (эмоции, намерения, частично состояние здоровья). Публичные опросы показывают высокую чувствительность общественности и требовательность к защите этих данных. Поэтому для BCI- и медицинских приложений приватность и consent-management — первостепенные требования. ([PMC][252])

#### 22.2.2. Регуляторные ориентиры (FDA и пр.)

* **FDA guidance (Implanted BCI Devices, May 2021)** — рекомендует обширные non-clinical testing, биосовместимость, электробезопасность, reliability (endurance/retention), а также клинические study designs и post-market surveillance. Для BCI-продуктов ранняя коммуникация с FDA обязательна. ([U.S. Food and Drug Administration][253])
* **EMA / EU & data protection:** в ЕС нейроданные попадают под GDPR как персональные данные, часто как специальные категории — нужно согласие, минимизация данных, правовые основания обработки и DPIA (Data Protection Impact Assessment). Кроме того, национальные и региональные инициативы по «neurorights» развиваются и требуют наблюдения. ([geneva-academy.ch][254])

(Load-bearing: FDA guidance — обязательный норматив для имплантируемых BCI; GDPR и neurodata privacy literature — важная правовая подоплёка.) ([U.S. Food and Drug Administration][255])

---

#### 22.2.3. Практики защиты приватности и данных (engineering + process)

1. **Минимизация данных & on-device processing:** храните и обрабатывайте сырые нейросигналы локально; передавайте только анонимизированные/агрегированные выводы. Это снижает риск exfiltration. ([arXiv][256])
2. **Encryption in transit and at rest:** использовать authenticated encryption для телеметрии и шифрование модели/весов на устройстве; secure key provisioning (TPM / secure element). ([SSRN][257])
3. **Differential privacy / local DP:** при сборе статистических данных для улучшения моделей применять DP-методы, чтобы снизить риск восстановления личной информации из агрегатов. Для нейроданных DP-применение требует аккуратности из-за маленьких выборок. ([arXiv][256])
4. **Consent, provenance & audit trails:** сохранять защищённые логи с аудитом доступа к нейроданным; обеспечить user consent workflows и механизмы удаления/portability. ([geneva-academy.ch][254])

---

### 22.3. Практики безопасного развёртывания (graceful degradation, failover to digital)

#### 22.3.1. Архитектурные паттерны для «безопасного отказа»

* **Failover to digital path:** при обнаружении hardware anomaly (threshold breach, sudden drift, verify failures) переключать inference/critical control loops на цифровой fallback (FPGA/CPU) с заранее загруженными модельными weight-снэпшотами. Это обязательный паттерн для safety-critical систем (роботы, BCI). ([PMC][251])
* **Graceful degradation modes:** заранее определить экономичные degraded-modes (reduced model capacity, lower batch concurrency, local quantized model) чтобы сохранять core functionality при деградации hardware. ([PMC][251])

#### 22.3.2. Operational practices и SRE / MLOps

* **Continuous runtime monitoring + canary deploys:** выкатывать новые маппинги/прошивки сначала на canary tiles, запускать stress & fault injection tests в production mirror; мониторить drift/accuracy и автоматически откатывать при деградации. ([PMC][251])
* **Scheduled maintenance & refresh windows:** плановые recalibration/programming windows и refresh policy (по времени или по drift-threshold) минимизируют неожиданное ухудшение. ([PMC][246])
* **Incident response & cyber playbook:** иметь SOP для compromised device (isolate, forensic capture, restore from signed backups, notify regulators/patients if applicable). Для медтех-устройств это совпадает с requirements по post-market surveillance. ([U.S. Food and Drug Administration][255])

#### 22.3.3. Технические меры для повышения надёжности и безопасности

* **Authenticated firmware/secure boot:** предотвращает загрузку malicious firmware; публичные ключи и secure element обязаны быть частью устройства. ([MDPI][248])
* **Runtime attestation & measurement:** регулярная cryptographic attestation состояния устройства (checksums, hash of tile metadata, program/verify counters) чтобы обнаруживать постфактум tampering. ([MDPI][248])
* **Anomaly detectors on model outputs:** на верхнем уровне ML-pipeline — простые statistical checks (sanity filters) и ensemble cross-checks, которые могут обнаружить implausible outputs из-за hardware corruption. ([ACM Digital Library][250])

---

### 22.4. Checklist (быстрое руководство для инженера / compliance team)

1. **Перед деплоем:** device audit (endurance/retention/ΔG stats); fault injection baseline; wear projections. ([PMC][246])
2. **Security by design:** secure boot, encrypted storage, key management, tamper-evidence, runtime telemetry. ([MDPI][248])
3. **Privacy by design:** минимизация сырья, on-device processing, DP/aggregation, documented consent and DPIA (для EU). ([PMC][258])
4. **Operational:** canary rollout, continuous monitoring (power/verify/temperature/drift), scheduled refresh, incident playbook. ([PMC][251])
5. **Regulatory:** engage FDA/EMA early for BCI/implantable devices; prepare non-clinical testing per FDA guidance; plan post-market surveillance. ([U.S. Food and Drug Administration][255])

---

### 22.5. Ключевые источники (must-read)

* M. J. Rasch et al., *Fast and robust analog in-memory deep neural network training*, **Nat. Commun.** 2024 — анализ ограничений (noise, symmetry, retention, endurance) и влияние на надежность обучения/эксплуатации. ([PMC][246])
* FDA, *Implanted Brain-Computer Interface (BCI) Devices* guidance (May 2021) — обязательные non-clinical и клинические рекомендации для имплантируемых BCI. ([U.S. Food and Drug Administration][253])
* W. Lillis et al., *Survey of Security Issues in Memristor-Based Machine Learning Systems*, **MDPI** 2024 — обзор угроз, атак и защит для memristor-систем. ([MDPI][248])
* K. Nagarajan et al., *Fault Injection Attacks in Spiking Neural Networks and ...*, **Frontiers (nano)** 2022 — демонстрации лазер/электрических glitch-атак на нейроморфные системы. ([Frontiers][247])
* A. S. Jwa et al., *Addressing privacy risk in neuroscience data*, **PMC review** 2022 — принципы защиты нейроданных, DPIA и правовые вопросы. ([PMC][258])
* C. Lammie et al., *The Inherent Adversarial Robustness of Analog In-Memory Computing*, **Nat. Commun.** / arXiv 2024–2025 — новые результаты по тому, как стохастичность AIMC может давать адверсариальную устойчивость и сопутствующие угрозы/возможности. ([arXiv][259])

---

#### Заключение — что важно помнить

1. **AIMC даёт сильные преимущества по энергоэффективности**, но вводит новые поверхности атак (физические, wear-based и side-channel). Поэтому безопасность и приватность должны быть спроектированы параллельно с HW/SW (secure-by-design + privacy-by-design). ([PMC][246])
2. **Для BCI/медтеха регуляторы (FDA/EMA) требуют раннего взаимодействия** и строгих non-clinical/clinical программ; neurodata требует особой правовой и этической защиты. ([U.S. Food and Drug Administration][255])
3. **Практический набор мер:** тесты fault-injection, wear stress, side-channel analysis; runtime monitoring/attestation; failover to digital; encryption & consent — и всё это должно быть частью product-release checklist. ([Frontiers][247])

---

<details>
<summary>Детали</summary>

* A) сгенерировать **checklist тестов** (CSV/Markdown) для security & reliability (power glitch, laser FI, accelerated wear, side-channel suites) с детальными параметрами (амплитуды, частоты, duration), или
* B) подготовить **incident playbook / SOP** (PDF) «device compromised / tampering detected» с шагами isolate/forensic/rollback/notify (подходит для MLOps и регуляторной документации)

</details>

[246]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335942/ "Fast and robust analog in-memory deep neural network ..."
[247]: https://www.frontiersin.org/journals/nanotechnology/articles/10.3389/fnano.2021.801999/full "Fault Injection Attacks in Spiking Neural Networks and ..."
[248]: https://www.mdpi.com/2674-0729/3/2/9 "Survey of Security Issues in Memristor-Based Machine ..."
[249]: https://arxiv.org/pdf/2302.07655 "Fault Injection in Native Logic-in-Memory Computation on ..."
[250]: https://dl.acm.org/doi/abs/10.1145/3600231 "Adversarial Defense and Device Variation-tolerance in ..."
[251]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10876512/ "Recent Advances in In-Memory Computing"
[252]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10800024/ "U.S. public perceptions of the sensitivity of brain data - PMC"
[253]: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing "Implanted Brain-Computer Interface (BCI) Devices for ..."
[254]: https://www.geneva-academy.ch/joomlatools-files/docman-files/Neurodata%20-%20Navigating%20GDPR%20and%20AI%20Act%20Compliance%20in%20the%20Context%20of%20Neurotechnology.pdf "research brief - neurodata"
[255]: https://www.fda.gov/media/120362/download "Implanted Brain-Computer Interface (BCI) Devices for ..."
[256]: https://arxiv.org/html/2412.11394v1 "Privacy-Preserving Brain-Computer Interfaces"
[257]: https://papers.ssrn.com/sol3/Delivery.cfm/5138265.pdf?abstractid=5138265&mirid=1 "1 Cyber Risks to Next-Gen Brain-Computer Interfaces"
[258]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9444136/ "Addressing privacy risk in neuroscience data - PubMed Central"
[259]: https://arxiv.org/abs/2411.07023 "The Inherent Adversarial Robustness of Analog In-Memory ..."

---


## 23. Патентный и коммерческий ландшафт 

Ниже — практический, подробно проработанный обзор ключевых игроков (корпорации + стартапы), их R&D-направлений, а также рекомендации и конкретные шаги по оценке IP-рисков и freedom-to-operate (FTO). Для важнейших утверждений приведены авторитетные источники 2023–2025 гг.

---



### 23.1. Крупные игроки: кто и над чем работает

#### 23.1.1. IBM — лидер по AIMC/analog-MoE, инструменты и интеграция в LLM-стек

* **Фокус:** масштабирование LLM через 3D NVM-AIMC (analog MoE), toolchain (AIHWKit и производные), system-level integration (per-tile telemetry, mapping, 3D stacking). IBM публикует исследования и практические демонстрации, ориентированные на реальное deployment-поведение и TCO. ([IBM Research][260])
* **Почему важно:** IBM сочетает device→chip→software (AIHWKit, Analog-MoE), поэтому их патентный пул и публикации являются ключевой отправной точкой для FTO и технологического бенчмаркинга. ([IBM Research][260])

#### 23.1.2. Intel — нейроморфика и системные подходы (Loihi, Hala Point)

* **Фокус:** neuromorphic processors (Loihi / Loihi-2), масштабные neuromorphic systems (Hala Point 1.15B-neuron), исследование event-driven SNN и on-chip learning. Intel нацелен на edge/low-power SNN-workloads и ecosystem для приложений. ([Newsroom][261])
* **Почему важно:** Intel собирает сильную патентную базу вокруг архитектур SNN, on-chip learning и интеграции many-core neuromorphic systems — это важно при планировании нейроморфных решений и разработки гибридных (SNN+AIMC) платформ. ([Newsroom][261])

#### 23.1.3. Samsung — MRAM/near-memory и коммерческие инициативы памяти

* **Фокус:** MRAM / near-memory solutions, исследования по интеграции NVM для AI, демонстрации MRAM-based in-memory computing; активные разработки в направлении интеграции память→compute в продуктах памяти и SoC. ([Samsung Новости][262])
* **Почему важно:** Samsung — крупный игрок на уровне foundry/ecosystem и потенциальный поставщик BEOL/packaging решений; их патенты по MRAM и near-memory влияют на производственные варианты. ([Samsung Новости][262])

#### 23.1.4. TSMC — foundry / 3D-stacking / selector & process ecosystem

* **Фокус:** развитие SoIC/3D-IC и экосистемы для 3D stacking, support для RRAM/PCM/selector devices; TSMC — ключевой партнёр для массового производства BEOL / M3D решений. ([tsmc.com][263])
* **Почему важно:** для коммерческого производства AIMC решения критичны foundry-услуги (BEOL integration, 300-mm flows, packaging). Патенты и договоры с foundry напрямую влияют на FTO. ([tsmc.com][263])

---

### 23.2. Стартапы и частные компании — кто делает что (выборка ключевых игроков)

> Ниже — компактные карточки стартапов и малых компаний, релевантных AIMC / memristor / neuromorphic экосистеме. Для каждой — кратко о технологии и о применимости.

#### 23.2.1. Mythic — analog inference (flash-based analog compute)

* **Что:** коммерческая analog-inference компания (аналог-в-памяти на основе flash/analog circuits) — продукт ориентирован на edge inference с высокой энергоэффективностью. ([Mythic][264])

#### 23.2.2. CrossBar (CrossBar Inc.) — ReRAM / secure-processing units

* **Что:** ReRAM developer с патентами на RRAM-cell/arrays и продуктами выступает как поставщик IP/модулей для NVM; релевантен как поставщик ячеек и патентных прав на RRAM-устройства. ([CrossBar][265])

#### 23.2.3. Weebit Nano — ReRAM (embedded RRAM IP)

* **Что:** разработчик ReRAM (RRAM IP, модули для PDK), ориентирован на встроенные (embedded) применения и сотрудничество с foundries / IDM-партнёрами. ([Weebit][266])

#### 23.2.4. MemryX — edge AI accelerators, in-memory ideas

* **Что:** выпускает edge AI ускорители с архитектурой, использующей идеи in-memory/dataflow; больше акцент на коммерческом ускорителе для edge-AI, а не исключительно на memristor device stack; релевантен как пример доступных edge-решений с in-memory компонентами. ([MemryX][267])

#### 23.2.5. BrainChip (Akida) и другие нейроморфные стартапы

* **Что:** BrainChip (Akida) — цифровой event-based neuromorphic процессор для edge; полезен как индустриальный пример нейроморфной коммерциализации (SNN-в-продукт). ([BrainChip][268])

#### 23.2.6. Новые игроки & «аналоговый» стартап-спектр (Sagence и др.)

* **Что:** ряд молодых компаний (Sagence и другие упоминаемые в индустриальных обзорах) разрабатывают инновационные analog-AI и AIMC подходы; ландшафт быстро меняется, поэтому актуальный FTO-список надо обновлять каждые 6–12 мес. ([IEEE Spectrum][269])

**Примечание:** список стартапов выше — иллюстративный, не исчерпывающий; многие лаборатории/университетские spin-outs и IP-портфели (университеты, национальные центры) активно публикуют патенты и технологии (RRAM, PCM, selectors, ferroelectric FEFET и т.д.). Рекомендуется формировать динамический «tracker» патентов/старт-апов в рамках FTO-процесса. ([yolegroup.com][270])

---

### 23.3. IP-риски и freedom-to-operate: практические советы

#### 23.3.1. Основные категории патентного риска в AIMC / memristor экосистеме

1. **Device & materials IP:** патенты на физические stacks (PCM GST stacks, oxide RRAM stacks, selector materials), heater geometries, filament control и т. п. (патенты часто защищают материалы и ключевые processing steps).
2. **Array & circuit IP:** патенты на топологии crossbar, selector-cell arrangements (1T1R/1S1R), sneak-path mitigation, programming schemes (program/verify algorithms).
3. **System & algorithmic IP:** mapping schemes, programming protocols, mixed-signal ADC/DAC architectures и алгоритмический co-design (например, HWA-training methods, hardware-aware quantization).
4. **Packaging & integration IP:** 3D stacking / vertical vias / BEOL integration flows и специфические packaging/thermal solutions.
   (Каждая из этих категорий активно патентуется крупными корпорациями и стартапами — это источник FTO-рисков). ([Samsung Новости][262])

#### 23.3.2. Практический план FTO / IP-due diligence (пошагово)

1. **Scoping (техническая карта):** формализуйте, какие именно элементы вашей реализации — device stack, selector, cell geometry, 1bit/2bit кодирование, differential схемы, ADC-архитектура, mapping/compilers — будут уникальны. Это определит search-queries.
2. **Patent landscape search (outsourced + in-house):**

   * выполнить поиски в Espacenet, USPTO, Google Patents по ключевым словам и патентным семьям (RRAM, PCM, memristor, in-memory computing, crossbar, program/verify).
   * заказать Freedom-to-Operate отчёт у патентных экспертов (патентные адвокаты / патент-аналитики) — включить ключевые страны (US, EU, CN, KR, JP, TW).
3. **Map risk to design:** сопоставить найденные патентные семейства с вашей технической картой; выделить «blocking patents» (патенты, которые непосредственно покрывают вашу критичную технологию).
4. **Mitigation options:** (a) redesign (work-around) — изменить архитектуру, чтобы избежать claims; (b) license — переговоры с держателями IP; (c) cross-license / partnership; (d) defensive publication (формализовать описания, publish to invalidate будущие broad patents).
5. **Contractual & manufacturing checks:** проверить договоры с foundry/3rd party IP providers (подписанные NDA/License), review supplier IP indemnities.
6. **Ongoing monitoring:** ежеквартальные/полугодовые патент-alerts по релевантным классам. ([yolegroup.com][270])

#### 23.3.3. Рекомендации — «practical do’s & don’ts»

* **DO**: вовлекать IP counsel на ранних этапах (прежде чем публично демонстрировать прототипы или подписывать foundry deals).
* **DO**: сохранять техдокументы, lab-logs и даты (for priority / proof-of-invention), если планируете защищать свои разработки.
* **DO**: использовать defensive publication (грамотно сформулированные технические раскрытия), если вы хотите блокировать конкурентные broad claims.
* **DON’T**: считать, что «open research papers» = свободная зона — многие коммерческие патенты покрывают практические шаги и workflow, даже если идеи публикуются в академии. ([yolegroup.com][270])

---

### 23.4. Практический checklist для стартапа / R&D-команды (IP & commercial readiness)

1. **Сделать стартовый patent-landscape** (внутренний) — список 20–50 наиболее релевантных патентных семей и их владельцев.
2. **Сформировать список target-partners** (foundries, packaging, measurement houses) и запросить их IP-terms/indemnities.
3. **Определить «non-negotiables» (core-freedom)** — какие части дизайна вы не готовы менять; для них следует готовить стратегии licensing / partnership.
4. **Зарегистрировать ключевые собственные изобретения** (патентная заявка) и/или сделать defensive publications.
5. **Провести FTO-gap analysis** — если blocking patents есть, рассмотреть cost/benefit переговоров о лицензировании vs redesign. ([IBM Research][260])

---

### 23.5. Ключевые источники и дальнейшее чтение (must-read)

* IBM Research — *Efficient Scaling of LLMs with Mixture of Experts and 3D analog in-memory computing* (IBM Research page / paper). ([IBM Research][260])
* IBM Research blog / Analog AIMC overview (Jan 2025) — system-level позиция IBM по analog-MoE и implications. ([IBM Research][271])
* Intel Research / Loihi & Hala Point announcements — neuromorphic systems & scale (Intel newsroom). ([Newsroom][261])
* Samsung Research — MRAM / near-memory posts and Nature-paper coverage on MRAM in in-memory tasks. ([Samsung Новости][262])
* TSMC research pages — memory ecosystem, 3D IC and SoIC support (foundry readiness for stacking & memory). ([research.tsmc.com][272])
* Mythic, CrossBar, Weebit, MemryX — корпоративные сайты (products / whitepapers) как первичные источники по их коммерческим направлениям. ([Mythic][264])
* Yole / industry analyses (2024–2025) — портрет стартап-ландшафта и инвестиционные тренды в AI-hardware. ([yolegroup.com][270])

---

### 23.6. Заключение — takeaways для команды, которая планирует коммерциализацию

1. **IP-ландшафт плотный и многослоен.** Device → array → circuit → mapping → system — по каждому слою есть активные патентные семьи у больших игроков и стартапов. Планируйте FTO на раннем этапе. ([IBM Research][260])
2. **Партнёрства с foundry и licensing-deals часто критичны** для скорого выхода на 300-mm производство; договорные положения о IP и indemnities — ключевой риск. ([tsmc.com][263])
3. **Гибридные стратегии (design-workarounds + defensive publications + selective licensing)** дают наилучшую практическую дорожную карту: минимизировать юридические риски и одновременно сохранять технологический ритм. ([yolegroup.com][270])

---

<details>
<summary>Детали</summary>

A) **подготовить краткий FTO-план (step-by-step)** с примерными затратами и временем (PDF/Markdown),
B) **сделать таблицу-карточки (CSV)** с ключевыми игроками/стартапами (технология, ключевые продукты, релевантные патентные семьи/ссылки), или
C) **запустить начальный патентный поиск (базовый список патентных семей)** по 5–10 ключевым терминам (вы получите список релевантных патентных публикаций и их владельцев).

</details>

[260]: https://research.ibm.com/publications/efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog-in-memory-computing   "Efficient Scaling of Large Language Models with Mixture ..."
[261]: https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai   "Intel Builds World's Largest Neuromorphic System to ..."
[262]: https://news.samsung.com/global/samsung-demonstrates-the-worlds-first-mram-based-in-memory-computing   "Samsung Demonstrates the World's First MRAM Based In- ..."
[263]: https://www.tsmc.com/english/news-events/blog-article-20240926   "Advancing 3D IC Design for AI Innovation"
[264]: https://mythic.ai/   "Power-efficient analog compute for edge AI - Mythic"
[265]: https://www.crossbar-inc.com/   "CrossBar - Advanced ReRAM Memory Solutions"
[266]: https://www.weebit-nano.com/   "ReRAM Next-Generation Memory Technology | Weebit"
[267]: https://memryx.com/   "Home - MemryX - Our AI chips bring the power of server ..."
[268]: https://brainchip.com/brainchip-to-unveil-akida-neuromorphic-processor-enabled-by-microchips-32-bit-mpu-at-ces-2024/   "BrainChip to Unveil Akida Neuromorphic Processor ..."
[269]: https://spectrum.ieee.org/analog-ai-2669898661   "Analog AI Startup Aims to Lower Gen AI's Power Needs"
[270]: https://www.yolegroup.com/industry-news/these-are-the-10-hottest-ai-hardware-companies-to-follow-in-2025/   "These are the 10 hottest AI hardware companies to follow ..."
[271]: https://research.ibm.com/blog/how-can-analog-in-memory-computing-power-transformer-models   "Analog in-memory computing could power tomorrow's AI ..."
[272]: https://research.tsmc.com/english/research/memory/publish-time-1.html   "Memory"

---

## 24. Открытые проблемы, roadmap и приоритеты исследований 

Ниже — подробный, практический и источниково-подкреплённый обзор **основных открытых проблем** на пути к промышленному внедрению memristor-AIMC и нейроморфных решений для LLM/ML, а также **конкретный roadmap** с приоритетами по уровням (device → circuit → algorithm → system). Везде, где это важно для принятия решений, я даю конкретные метрики, проверяемые гипотезы и предложенные эксперименты. Основные литературные опоры: обзор Sebastian et al. (2020), экспериментальные system-demos Ambrogio et al. (2023) и NeuRRAM (Wan et al., 2022), алгоритмические ограничения и предложения Rasch et al. (2024) и системные roadmaps IBM (AIMC+MoE, 2025). ([Nature][273])

---

### 24.0. Краткая постановка: почему roadmap нужен сейчас

AIMC/memristor-платформы уже демонстрируют впечатляющие fJ-уровни на MAC в лабораторных прототипах, но переход к массовому применению LLM требует скоординированного прогресса по устройствам, периферии, алгоритмам и производству. Без чётко приоритизированного roadmap риск «lab-demo → провал в продакшн» остаётся высоким. ([Nature][274])

---

### 24.1. Device level (endurance, variability, селекторы, материалы)

#### Открытые проблемы

1. **Endurance vs write-energy trade-off.** Многие RRAM/PCM вариации имеют ограниченную endurance (варианты от 10³ до >10¹² циклов в исследованиях), а низкоэнергетичные записи часто сопровождаются худшей retention/variability. Это ключевой барьер для on-chip обучения. ([Nature][273])
2. **Стабильность/дрейф conductance (drift) и cycle-to-cycle variability.** Дрейф (лог-/степенной зависимости) и C2C шум уменьшают SNR и требуют частых recalibration/replication. ([Nature][273])
3. **Selector devices и sneak-path mitigation.** Для плотных passive crossbar-матриц нужен селектор с высокими I-V соотношениями и совместимостью BEOL. Наличие селектора критично для масштабируемости. ([Nature][273])
4. **Materials & BEOL-compatibility.** Материалы (GST / HfOx / TiO₂ / ферроэлектрики) должны быть совместимы с low-T BEOL-flow и иметь воспроизводимые process windows для 300-mm fabs. ([Nature][274])

#### Метрики, которые нужно улучшать / стандартизировать

* **Endurance (cycles to 10% failure)** в реальном write-режиме (реальные pulse amplitudes/widths).
* **Retention (t₁/₂ при 85°C/25°C) и Arrhenius parameters.**
* **ΔG per write (statistic: mean, σ, skew) и asymmetry (set vs reset).**
* **Selector Ion/Ioff / nonlinearity, process yield на wafer.**

#### Приоритетные исследования / эксперименты (device)

* **Мат-инжиниринг селекторов** с low-T deposition и высокой nonlinearity; тест в масштабе 300-mm BEOL-flows.
* **Low-energy write regimes + verify-algorithms**: оптимизация program/verify для минимизации pulse-count при сохранении precision.
* **Quantified endurance under HWA workloads**: прогон real HWA-update workloads (микро-бэтчи, LoRA-паттерны) до деградации. Это даст реальную метрику пригодности для on-chip fine-tune. ([Nature][273])

---

### 24.2. Circuit level (ADC/DAC, periphery, selectors, stacking)

#### Открытые проблемы

1. **ADC/DAC energy & area доминируют при масштабировании.** В системах с большим числом колонок ADC-энерго/площадь могут нивелировать fJ-выигрыш core. Нужны новые low-power ADC-архитектуры и схемы shared-ADC с контролем latency/ENOB. ([arXiv][275])
2. **IR-drop, wire resistance и межтайловая аналоговая коммуникация** ограничивают масштаб — требуется co-design шины, драйверов и зарядо-временных схем. ([PubMed][276])
3. **Thermal management в 3D stacks.** Вертикальное размещение увеличивает плотности, но порождает thermal hotspots, влияющие на retention/variability. ([IBM Research][277])

#### Приоритетные исследования / эксперименты (circuit)

* **ADC архитектуры для CiM:** разработка charge-to-time, ramp/counter, SAR-hybrid ADC с вычислительной поддержкой, оптимизированных по energy/throughput (см. архитектурную модель ADC energy 2024). ([arXiv][275])
* **Analog inter-tile protocols:** low-loss analog signalling (charge-pulse, time-encoded) для уменьшения energy коммуникации (новые публикации 2025 предлагают analog attention circuits). ([Nature][278])
* **Thermal-aware floorplanning & activation scheduling** для 3D stacks: co-design scheduler + thermal sensor network. IBM/Ambrogio-демонстрации указывают на необходимость такого подхода в system level. ([Nature][274])

---

### 24.3. Algorithmic level (hardware-aware training, mapping, low-write updates)

#### Открытые проблемы

1. **Hardware-aware training (HWA) для LLM масштаба.** HWA-техника сейчас работает на small→medium models; для LLM нужны scalable HWA frameworks (AIHWKit-Lightning, Analog-MoE) и методы, сохраняющие convergence и generalization. ([IBM Research][277])
2. **Low-write / endurance-aware learning algorithms.** Алгоритмы, минимизирующие количество write-операций (LoRA, low-rank updates, sparse adapters, update accumulation) — ключ к практичному on-device fine-tune. Rasch et al. анализируют пределы и предлагают direction. ([PMC][279])
3. **Mapping & compiler problems для Transformer/MoE на AIMC.** Разбиение весов, шардирование experts, partial-sum routing, replication — всё это требует оптимальных компилерных стратегий под конкретный hardware footprint. ([IBM Research][277])

#### Приоритетные исследования / эксперименты (algorithm)

* **Масштабируемые HWA-тренировки для трансформеров:** проекты по интеграции AIHWKit-Lightning + distributed HWA retrain для 100M–1B параметров, включить analog-noise, drift augmentation, replica strategies. ([IBM Research][277])
* **Low-write адаптеры:** систематическое исследование LoRA/LoHA/low-rank adapters в AIMC: сравнить энергию/accuracy/ write-count trade-offs и показать practical pipelines. ([PMC][279])
* **Optimal MoE placement algorithms:** work on bank-placement, expert-bank shaping, thermal & power constrained routing and scheduling (validate with MNSIM/CrossSim + small hardware). ([IBM Research][277])

---

### 24.4. System level (integration, yield, manufacture, economics)

#### Открытые проблемы

1. **Yield & repair strategies для больших crossbar массивов.** Per-cell yields приводят к экспоненциальному падению при больших N; нужны adaptive repair, redundancy budgeting и defect-aware mapping. ([Nature][274])
2. **Manufacturing readiness (BEOL, 300-mm)** и supply chain для selectors / materials. Ambrogio-демо показывает возможность, но массовый выпуск требует industrialization. ([Nature][274])
3. **TCO / economic validation для LLM-workloads.** Энергосбережение должно компенсировать CAPEX на fabs/packaging; реальные TCO-модели требуют realistic utilization сценариев. ([IBM Research][277])

#### Приоритетные исследования / действия (system)

* **Pilot fab flows & DfT work:** сотрудничество с foundries на BEOL trials, development of wafer-scale test flows и automated factory calibration pipelines. ([Nature][274])
* **Yield modelling + redundancy study:** quantitative studies, пробные runs с redundancy/repair и economic sensitivity analysis (effect of replication factor on effective yield & area). ([Nature][274])
* **TCO case studies:** open, reproducible TCO models contrasting AIMC datacenter racks vs GPU clusters для specific LLM workloads and utilisation profiles (use IBM / industry inputs). ([IBM Research][277])

---

### 24.5. Метрики успеха: что измерять, чтобы понять прогресс

Для каждого уровня приведите «go/no-go» метрику:

**Device**

* Endurance > 10⁹ cycles at target pulse energy (для realistic on-device fine-tune) — go.
* Drift rate < X% conductance change / decade (определять для целевых retention windows).

**Circuit**

* ADC energy per conversion amortized < 20–40 fJ per MAC-equivalent (в зависимости от bitwidth/throughput). (Модель ADC energy 2024 даёт способ оценки). ([arXiv][275])

**Algorithm**

* HWA-mapped LLM (mini-bench) retains ≥99% of baseline accuracy after mapping + single HWA short fine-tune, with write-count per weight < Y (порог зависит от device endurance). ([PMC][279])

**System**

* Effective TCO break-even within N years under 60–80% utilization для target LLM workload (case study). ([IBM Research][277])

---

### 24.6. Roadmap (конкретные временные горизонты и milestones)

> **Короткосрочно (1–2 года)** — *de-risking & toolchain maturity*

* Развернуть и стандартизировать HWA toolchains (AIHWKit-Lightning, CrossSim integration).
* Device audits: endurance/retention datasets для candidate stacks under HWA workloads.
* Demonstrate robust analog inference on medium-scale transformer (≤100M) with reproducible energy breakdown. ([IBM Research][277])

> **Среднесрочно (3–5 лет)** — *scale pilots & hybrid deployment*

* Pilot BEOL runs in 300-mm foundry; validated assembly of 3D stacks at module level.
* Demonstrations of MoE + 3D AIMC with bank per expert and scheduler showing real throughput/energy gains (IBM-style demos).
* Low-write adapter ecosystems (LoRA/LoHA) standardized для AIMC pipelines. ([IBM Research][277])

> **Долгосрочно (5–10 лет)** — *mass production & on-device training options*

* Mature M3D monolithic flows для very high density AIMC stacks (subject to thermal solutions).
* Device classes and algorithms enabling practical frequent on-device training (or continuous personalization) with acceptable lifetime. ([Nature][274])

---

### 24.7. Ресурсы / организационная структура для исполнения roadmap

* **Мультидисциплинарные «Vertical Integration» команды**: device scientists + circuit designers + ML researchers + system architects + foundry partners + IP/legal.
* **Shared infrastructure:** common datasets (device audit bench), shared AIHWKit/ CrossSim instances, standardized bench protocols для reproducibility. ([Nature][273])

---

### 24.8. Открытые научные вопросы (наиболее «больные»)

1. **Можно ли создать device с endurance ≫10¹² при write-energies в десятки fJ?** (материаловедческий вызов). ([Nature][273])
2. **Какая архитектура ADC/DAC даёт наилучший system-level энерго/latency компромисс при LLM-размерности?** (архитектурно-круглый вопрос; требует co-design и новые ADC-архитектуры). ([arXiv][275])
3. **Насколько далеко можно продвинуть HWA-training для BERT/LLM-scale без значительного роста write-counts?** (алгоритмический вызов: low-write learning). ([PMC][279])

---

### 24.9. Немедленные (first-order) эксперименты, которые дадут максимальную информацию

1. **Endurance vs HWA workload sweep:** запустить realistic HWA-update сценарии (LoRA, small-LR fine-tune) на candidate devices до их деградации → получить practical write-budget. (покрывает device+algorithm). ([PMC][279])
2. **System-level energy decomposition for a mapped transformer:** измерить E_total и breakdown (analog core / ADC / interconnect / periphery) на реальном прототипе или на validated emulation chain (AIHWKit + CrossSim). Это даст честную оценку экономики. ([Nature][274])
3. **MoE bank activation & thermal study:** эмитировать realistic MoE traffic и измерять thermal transients в 3D stack prototype / thermal model; разработать scheduler. ([IBM Research][277])

---

### 24.10. Ключевые ссылки (для быстрого чтения)

* A. Sebastian et al., *Memory devices and applications for in-memory computing*, **Nat. Nanotech.** 2020 (overview device → system). ([Nature][273])
* S. Ambrogio et al., *An analog-AI chip for energy-efficient speech recognition and transcription*, **Nature** 2023 (system prototype, BEOL PCM). ([Nature][274])
* W. Wan et al., *NeuRRAM: RRAM-based compute-in-memory chip*, **Nature** 2022 (array/system co-design). ([PubMed][276])
* M. J. Rasch et al., *Fast and robust analog in-memory deep neural network training*, **Nat. Commun.** 2024 (algorithms & limits for in-memory training). ([PMC][279])
* J. Büchel et al., *Efficient scaling of large language models with Mixture of Experts and 3D analog in-memory computing*, **Nat. Comput. Sci.** 2025 (MoE+3D AIMC roadmap). ([PubMed][280])
* Architecture-level ADC energy model (arXiv 2024) — практическая модель для проектировщиков периферии. ([arXiv][275])

---

### 24.11. Короткое резюме — какие приоритеты ставить в первую очередь

1. **Device audit + endurance under HWA workloads** (highest priority) — без честной оценки endurance on-device training невозможен. ([PMC][279])
2. **ADC/DAC & periphery energy minimization (co-design)** — второе по важности; без этого system-level gains будут съедены периферией. ([arXiv][275])
3. **Scalable HWA training & low-write adaptation algorithms** (LoRA/LoHA / sparse adapters) — приложить усилия по алгоритмам, которые минимизируют write-budget. ([PMC][279])
4. **Pilot BEOL runs and yield/repair strategies** — подготовить промышленный путь к 300-mm production. ([Nature][274])

---

<details>
<summary>Детали</summary>

* A) **сгенерировать краткий 1→3-летний план действий** для вашей команды (Gantt-style) с конкретными экспериментами, ресурсами и критериями go/no-go; или
* B) **подготовить checklist экспериментов** (CSV/Markdown) для device-audit + HWA endurance sweep + system energy breakdown; или
* C) **создать Triage-matrix** (spreadsheet) — сравнение candidate device-stacks по ключевым метрикам (endurance, drift, write-energy, BEOL-compatibility) с рекомендуемыми follow-up experiments.

</details>

[273]: https://www.nature.com/articles/s41565-020-0655-z   "Memory devices and applications for in-memory computing"
[274]: https://www.nature.com/articles/s41586-023-06337-5   "An analog-AI chip for energy-efficient speech recognition ..."
[275]: https://arxiv.org/html/2404.06553v1   "Modeling Analog-Digital-Converter Energy and Area for ..."
[276]: https://pubmed.ncbi.nlm.nih.gov/35978128/   "A compute-in-memory chip based on resistive random- ..."
[277]: https://research.ibm.com/publications/efficient-scaling-of-large-language-models-with-mixture-of-experts-and-3d-analog-in-memory-computing   "Efficient Scaling of Large Language Models with Mixture ..."
[278]: https://www.nature.com/articles/s43588-025-00854-1   "Analog in-memory computing attention mechanism for fast ..."
[279]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335942/   "Fast and robust analog in-memory deep neural network ..."
[280]: https://pubmed.ncbi.nlm.nih.gov/39779828/   "Efficient scaling of large language models with mixture ..."

---

**25. Глоссарий**. Ниже — подробный, единообразный и технически точный набор терминов, охватывающий весь стек (device → circuit → architecture → algorithms → benchmarks → deployment). Каждый термин — краткое определение + зачем он важен для AIMC / LLM-проектов. 

---

## 25. — Глоссарий 

1. **Memristor / memristive device** — двухконтактный элемент, проводимость которого зависит от предшествующей истории токов/напряжений; в практике чаще понимается как «memristive system» (внутренние состояния, drift, стохастика). (важен как физический базис AIMC). 
2. **Memristive system** — обобщённая модель устройства с одним или несколькими внутренними состояниями x(t) и уравнениями i = G(x,v), ˙x = f(x,v). (реалистичнее для RRAM/PCM). 
3. **Chua (идеальный) memristor** — математическая модель (v = M(q)·i), pinched hysteresis loop; теоретический эталон, редко выполняемый в идеале в реальных устройствах. 
4. **Pinched hysteresis loop** — характерная петля I–V идеального мемристора при переменном возбуждении; диагностический признак мемристивности. 

---

### Устройства / материалы

5. **RRAM / Oxide RRAM / OxRAM** — резистивная память на основе оксидов (HfOx, TiO₂ и др.), переключение за счёт формирования/разрыва нитей (filaments). 
6. **Filamentary switching** — локальная агрегация вакансий/ионов → проводящая нить; ключ к fast switching, но источник вариабельности. 
7. **PCM (Phase-Change Memory)** — память на фазовых переходах (кристалл ↔ аморф) в chalcogenide; multi-level storage, но термически-энергетическая природа записи. 
8. **CBRAM (Conductive-Bridge RAM)** — электролитно-металлическое формирование проводящего моста (Ag/Cu); low-V switching и свои особенности reliability. 
9. **FeFET / FEFET (ferroelectric FET)** — транзистор с ферроэлектрическим затвором для non-volatile хранения (высокая совместимость с CMOS). 
10. **STT-MRAM / SOT-MRAM (spintronic)** — магнитная память на MTJ; очень высокая endurance, но обычно бистабильная (цифровая). 
11. **2D-material memristors** — мемристоры на базе двумерных материалов (MoS₂, graphene и т.д.), перспективны для scaling, пока в research-stage. 

---

### Параметры устройств и надёжность

12. **Endurance** — число program/erase циклов до деградации (важно для on-chip training). 
13. **Retention** — временная сохранность заданного conductance; обычно выражается в часах/годах или через Arrhenius-экстраполяцию. 
14. **Drift** — изменение conductance с течением времени (особенно заметно в PCM — R(t) ~ R0·t^ν). 
15. **Variability (D2D / C2C)** — разброс параметров device-to-device и cycle-to-cycle; критичен для точности весов. 
16. **ΔG per write (program granularity)** — средний шаг изменения conductance при одной программной операции (важно для precision). 

---

### Топологии и array-level термины

17. **Crossbar (1R passive)** — матрица word-lines / bit-lines с двухконтактными memristors в узлах; реализует аналоговый VMM через токовую суммаризацию. 
18. **Passive crossbar** — crossbar без селектора/транзистора в каждой ячейке (макс. плотность, большие проблемы с sneak path). 
19. **1T1R (1 transistor + 1 resistive element)** — активная ячейка с транзистором для адресации; уменьшает sneak currents за счёт селекции ячейки. 
20. **1S1R (1 selector + 1 resistive element)** — селектор (diode/OTS/threshold) в серию с memristor; компромисс плотности и управляемости. 
21. **Selector (OTS / diode / self-rectifying / threshold)** — устройство, дающее высокую нелинейность I–V для подавления sneak-path; требования: I_on, I_off, thermal robustness. 
22. **Sneak-path (sneak currents)** — нежелательные параллельные токи в passive crossbar, искажающие считывание и суммирование токов. (формула i_BL = I_sel + Σ I_sneak). 
23. **V/2, V/3 biasing** — схемы частичного смещения (read/write) для снижения полувыбранных напряжений и уменьшения ненамеренного переключения. 
24. **Tiling / hierarchical macros** — разбиение огромных матриц на тайлы/макросы + top-level routing для управления накладными расходами и тестируемости. 

---

### Схемотехника и периферия

25. **ADC (Analog-to-Digital Converter)** — преобразователь аналогового результата суммы в цифровой вид; ENOB / latency / energy — ключевые параметры. 
26. **DAC (Digital-to-Analog Converter)** — формирует аналоговые входы (вольтажные/токовые) для строк или столбов; влияет на latency и energy. 
27. **ENOB (Effective Number Of Bits)** — реальная разрешающая способность ADC с учётом шума/нестабильности; критична для точности VMM. 
28. **Sense-amp / current sense** — схема измерения суммарного тока столбца; архитектурные решения сильно влияют на latency/energy. 
29. **ADC-sharing / ADC amortization** — приём уменьшения числа ADC путём последовательного/параллельного time-multiplexing столбцов для экономии area/energy. 
30. **Driver / write driver** — источник программирующих/читающих импульсов (pulse control), влияет на program latency и energy. 

---

### Моделирование и инструменты

31. **SPICE / Verilog-A compact model** — упрощённые модели устройств, пригодные для circuit-level симуляций (VTEAM, Yakopcic, Pickett, Zanotti и др.). 
32. **VTEAM / TEAM / Yakopcic models** — популярные компакт-модели с пороговыми и адаптивными поведениями для Verilog-A. 
33. **Window function (Joglekar / Biolek / Prodromakis)** — математические окна, ограничивающие internal state x в компакт-моделях и предотвращающие «boundary lock». 
34. **Simmons tunneling / Pickett model** — физически-ориентированные модели, описывающие tunneling through gaps / barrier dependence на расстоянии d(x). 
35. **Thermal lumped node / electro-thermal coupling** — схема для моделирования Joule heating и его влияния на switching/retention. 
36. **KMC (Kinetic Monte-Carlo)** — стохастический метод моделирования ионной/атомной кинетики (filament formation statistics). 

---

### Алгоритмы и co-design

37. **HW-aware training (HWA)** — обучение с учётом non-idealities железа (noise, nonlinearity, quantization, drift) — делается через инъекции шума, calibration-loops, retraining. 
38. **Non-ideality-aware training** — включение моделей device-noise/variability в тренировочный цикл, чтобы сеть была робастной при маппинге на AIMC. 
39. **Quantization-aware training (QAT)** — тренировка с учётом дискретных уровней представления; важна при low-bit ADC/DAC. 
40. **LoRA (Low-Rank Adaptation)** — метод тонкой настройки LLM через низкоранговые адаптеры (сокращает write-budget при on-device finetune). 
41. **LoHA** — аналогичные low-write адаптеры, оптимизированные под hardware constraints (вариация на тему LoRA для AIMC). 
42. **MoE (Mixture-of-Experts)** — архитектурный приём для масштабирования LLM (sparcity): только subset experts активируется → выгодно для tiled AIMC/3D stacking. 

---

### Нейроморфика и SNN

43. **SNN (Spiking Neural Network)** — event-driven нейросети, использующие дискретные спайки; хорошо сочетаются с энергоэффективными event-driven архитектурами. 
44. **STDP (Spike-Timing-Dependent Plasticity)** — локальное правило изменения веса в SNN: зависимость от относительного времени преп/пост-синаптических спайков. 
45. **Loihi / Loihi-2 / TrueNorth / SpiNNaker** — аппаратные платформы для SNN (Intel, IBM/Nervana-style и др.) — используются как reference для neuromorphic benchmarks. 

---

### LLM / ML-специфичные термины и метрики

46. **VMM (Vector-Matrix Multiply)** — ключевая операция в NN/LLM, реализуемая аппаратно как аналоговый MAC в crossbar. 
47. **MAC (Multiply-Accumulate)** — базовая операция, energy/MAC — стандартная метрика для сравнений hardware. 
48. **Perplexity / BLEU / ROUGE / WER** — task-specific quality metrics (NLP/LLM/ASR) — обязательно приводить mapped vs baseline. 

---

### Benchmarks, инструменты, репозитории

49. **AIHWKit (IBM)** — HW-aware training toolkit / emulator для AIMC, содержит device-presets и примеры mapping/QAT. 
50. **CrossSim (Sandia)** — crossbar-scale accuracy simulator / toolchain для оценки array-level effects. 
51. **MNSIM / MNSIM-2.0** — архитектурный симулятор для memristor systems (Tsinghua). 

---

### Производство и интеграция

52. **BEOL (Back-End-Of-Line)** — расположение memristor/selector слоёв над CMOS (важно для совместимости fab flows). 
53. **FEOL (Front-End-Of-Line)** — транзисторная логика, интеграция сложнее при монолитном 3D. 
54. **300 mm flow / wafer yield** — промышленные параметры производства; yield критичен для экономичности AIMC. 
55. **3D stacking / monolithic 3D** — вертикальная интеграция crossbar слоёв для плотности; требует thermal/power/yield решения. 

---

### Надёжность, безопасность, эксплуатация

56. **Program / Verify (P/V) scheme** — итеративный метод программирования conductance: pulse → measure → коррекция; влияет на write-energy и latency. 
57. **Calibration / per-tile calibration** — процедуры измерения и корректировки per-tile scale/bias для компенсации D2D и drift. 
58. **Repair / redundancy / remapping** — методы борьбы с дефектными ячейками (spare rows/cols, remap tables). 
59. **Fault injection / adversarial tampering (hardware attacks)** — test-scenarios для robustness/security; особенно важно для BCI/medtech. 

---

### Экономика и экосистема

60. **TCO (Total Cost of Ownership)** — CAPEX + OPEX model для сравнения AIMC vs GPU/TPU в LLM-инференсе. 
61. **FTO (Freedom-To-Operate) / IP landscape** — патентные риски и основные игроки (IBM, Intel, Samsung, стартапы по memristor/PCM). 

---

Оглавление:

- [ЭИРО framework](/README.md)
