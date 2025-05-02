# Перенос сознания

**Оценка теорий и возможностей**

Мы обсуждаем теоретическую возможность эмуляции мозга, что связано с непростыми техническими задачами, такими как сканирование, сохранение и моделирование. Для перспективных технологий на уровне мозга мыши могут потребоваться десятилетия, тогда как для человеческого мозга время будет намного больше. Ключевыми направлениями являются картирование коннектомов, криосохранение и молекулярное моделирование. Нужно учитывать этические и философские вопросы, которые поднимаются в таких исследованиях.

## Введение

Перенос сознания (mind uploading) теоретически основан на концепции полной цифровой эмуляции головного мозга (whole‑brain emulation), однако сегодня эта идея сталкивается с четырьмя основными техническими барьерами: высокоточным сканированием и картированием синаптических связей в масштабе всего мозга, надежным сохранением и подготовкой ткани для дальнейшего анализа, масштабируемым моделированием динамики нейронных и молекулярных процессов, а также колоссальными вычислительными требованиями для симуляции (§ Технические возможности). Современные методы коннектомики на базе электронной микроскопии уже позволяют реконструировать микроскопические участки коры мыши и человека, но их масштабирование до всего мозга сопряжено с проблемами скорости, репрезентативности и обработки огромных объёмов данных ([PubMed][1], [Frontiers][2]). Криопротоколы (включая витрификацию и альдегид‑стабилизированную криоконсервацию) демонстрируют сохранение ультраструктуры мозга на суб‑микронном уровне, но вопрос восстановления функциональности после оттаивания остаётся открытым ([PMC][3], [Nature][4]). Расчёты указывают, что создание полной эмуляции человеческого мозга может занять десятилетия или столетия ввиду потребностей в хранении зеттабайтов данных и вычислительной мощности экзаскейл-класса ([fhi.ox.ac.uk][5], [arXiv][6]). В то же время картирование всего мозга мыши может стать реальностью в ближайшие десятилетия, что позволит опробовать подходы к автоматизированному построению и симуляции нейронных сетей ([arXiv][6]).

---

## Технические возможности

### Сканирование и картирование мозга

Современные методы коннектомики используют **электронную микроскопию (EM)**, обеспечивающую разрешение <1 нм, необходимое для идентификации всех синапсов в ткани мозга ([Frontiers][2]).
Протокол ODeCO (12‑шаговый метод осмиевого контрастирования) успешно внедрён для получения цельного коннектома мозга мыши без трещин и искажений ультраструктуры ([PMC][7]).
Расчётная оценка показывает, что для полного сканирования мозга мыши при разрешении EM требуется порядка 10⁷–10⁸ часов сканирования на современных многозондовых платформах и несколько эксабайт хранилища ([PubMed][1]).
Альтернативные оптические методы на базе расширительной микроскопии (ExM) и светового листового флуоресцентного микроскопа (ExLSFM) лишь начинают достигать субмикронного разрешения, но пока не могут покрыть объём всего мозга динамически и с нужной скоростью ([Frontiers][8], [SpringerLink][9]).

### Хранение и подготовка образцов

Для успешной верификации ультраструктуры мозга перед сканированием развиваются методы **витрификации** и **криопротекции**.
Реализация витрификации при −196 °C с использованием химических криопротектантов позволяет избежать образования ледяных кристаллов и сохранить целостность синаптических структур в образцах мышиного мозга ([PMC][3]).
Альдегид‑стабилизированная криоконсервация (АСК), впервые демонстрированная на кроличьих мозгах, показывает «почти идеальное» сохранение мембран и внутриклеточных структур при −135 °C, однако восстановление функций после оттаивания ещё не реализовано ([Wikipedia][10]).
Стандартизированные методы криопротекции больших объёмов мозга с использованием инженерных решений (калиброванные формы, системы мониторинга температуры) минимизируют дисторсию тканей и упрощают последующую гистологию и 3D‑реконструкцию ([Frontiers][11]).

### Моделирование и симуляция

Полноценная эмуляция мозга требует моделирования динамики нейронов и синапсов на уровне **электрофизиологии** и **молекулярных процессов**.
Отчёт Future of Humanity Institute предлагает дорожную карту, включающую создание трёхмерной наноструктурной карты мозга, автоматизированную сегментацию и скелетонизацию нейронных элементов для подготовки к симуляции ([fhi.ox.ac.uk][5]).
Объём данных зеттабайтного масштаба и сложность интеграции био- и электрохимических сигналов требуют вычислительной инфраструктуры экзаскейл-класса и продвинутых алгоритмов машинного обучения для автоматизации трассировки и параметризации сетей ([arXiv][6]).
Оценки показывают, что даже симуляция коркового фрагмента объёмом несколько миллиметров кубических потребует кластеров из миллионов GPU и сверхнизкой латентности связи между ними ([Wiley Online Library][12]).

## Перспективы

* **Краткосрочный горизонт (10–20 лет):** завершение коннектомов мышиного мозга и демонстрация масштабируемых платформ для автоматической трассировки нейронных сетей ([arXiv][6]).
* **Среднесрочный горизонт (20–50 лет):** интеграция витрификации и EM‑сканирования для образцов человеческой коры размером до нескольких кубических миллиметров с попытками функционального восстановления нейронных цепей in silico ([Nature][13]).
* **Долгосрочный горизонт (50+ лет):** теоретическая возможность полной эмуляции человеческого мозга, при которой вопросы «копии» vs «оригинала» и сохранения сознания останутся неразрешёнными ввиду философских и этических сложностей ([ResearchGate][14]).

Учитывая темпы развития нейротехнологий и материаловедения, создание устойчивых моделей сознания в цифровом виде остаётся отдалённой, но не принципиально невозможной задачей.

---

## Рекомендуемые источники

1. **Thrasher Collins L. et al.** Comparative prospects of imaging methods for whole‑brain mammalian connectomics. *arXiv* (2024). ([arXiv][6])
2. **Wang Y. et al.** A Scalable Staining Strategy for Whole‑Brain Connectomics. *Front. Neurosci.* (2023). ([PMC][7])
3. **Estrada E. et al.** Cryopreservation of brain cell structure: a review. *PMC* (2025). ([PMC][3])
4. **McIntyre R.L., Fahy G.M.** Aldehyde‑stabilized cryopreservation: Cryobiology (2015). ([Wikipedia][10])
5. **Hayworth K.J. et al.** Progress Towards Mammalian Whole‑Brain Cellular Connectomics. *Front. Neuroanat.* (2016). ([Frontiers][2])
6. **Bamford D., Danaher J.** Transfer of Personality to a Synthetic Human ('Mind Uploading'). *JCS* (2017). ([sim.me.uk][15])
7. **Sandberg A., Bostrom N.** Whole Brain Emulation: A Roadmap. *FHI* (2008). ([fhi.ox.ac.uk][5])
8. **Feasible Mind Uploading.** *Intelligence Unbound* (2013). ([Wiley Online Library][12])
9. **Frontiers in Hum. Neurosci.** Several inaccurate conceptions about BCI and mind uploading (2024). ([Frontiers][16])
10. **High‑contrast en bloc staining of mouse whole‑brain and human tissue.** *Nat. Methods* (2023). ([Nature][13])

[1]: https://pubmed.ncbi.nlm.nih.gov/39970909/ "Comparative prospects of imaging methods for whole-brain ..."
[2]: https://www.frontiersin.org/journals/neuroanatomy/articles/10.3389/fnana.2016.00062/full "Progress Towards Mammalian Whole-Brain Cellular Connectomics"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11753176/ "Cryopreservation of brain cell structure: a review - PMC"
[4]: https://www.nature.com/articles/s41467-024-47066-1 "Ultrastructure of human brain tissue vitrified from autopsy revealed ..."
[5]: https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf "[PDF] Whole Brain Emulation: A Roadmap - Future of Humanity Institute"
[6]: https://arxiv.org/abs/2405.10488 "Comparative prospects of imaging methods for whole-brain mammalian connectomics"
[7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10557665/ "A Scalable Staining Strategy for Whole-Brain Connectomics - PMC"
[8]: https://www.frontiersin.org/articles/10.3389/fnsyn.2021.754814/full "Towards a Comprehensive Optical Connectome at Single Synapse ..."
[9]: https://link.springer.com/article/10.1007/s12264-023-01112-y "Whole-brain Optical Imaging: A Powerful Tool for Precise Brain ..."
[10]: https://en.wikipedia.org/wiki/Aldehyde-stabilized_cryopreservation "Aldehyde-stabilized cryopreservation"
[11]: https://www.frontiersin.org/journals/neuroanatomy/articles/10.3389/fnana.2023.1292655/full "A technology platform for standardized cryoprotection and freezing ..."
[12]: https://onlinelibrary.wiley.com/doi/10.1002/9781118736302.ch5 "Feasible Mind Uploading - Intelligence Unbound"
[13]: https://www.nature.com/articles/s41592-023-01866-3 "High-contrast en bloc staining of mouse whole-brain and human ..."
[14]: https://www.researchgate.net/publication/269477453_The_Prospects_of_Whole_Brain_Emulation_within_the_next_Half-_Century "(PDF) The Prospects of Whole Brain Emulation within the next Half"
[15]: https://sim.me.uk/neural/JournalArticles/BamfordDanaher2017JCS.pdf "[PDF] Transfer of Personality to a Synthetic Human ('Mind Uploading') and ..."
[16]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1391550/full "Several inaccurate or erroneous conceptions and misleading ..."


---


## Обзор ключевых направлений исследований

Ниже представлен обзор 12 основных работ, посвящённых различным аспектам подготовки мозга к цифровой эмуляции: от визуализации коннектомов до сохранения ультраструктуры и разработки дорожных карт по эмуляции.

---

## 1. Сравнение методов визуализации для коннектомики

**Thrasher Collins et al. (2025)** провели количественное сравнение возможностей **электронной микроскопии (EM)** и **expansion light-sheet fluorescence microscopy (ExLSFM)** для одновременного достижения суб‑нанометрового разрешения и адекватной скорости сканирования целого мозга. Авторы показали, что хотя платформы EM (ssTEM, SBEM, FIB‑SEM, multiSEM и т.д.) уже способны идентифицировать все синапсы с разрешением <1 нм, их масштабирование на объём человеческого мозга требует эксабайт хранения данных и многомиллионных часов съёмки ([PubMed][1]).

---

## 2. Прогресс в клеточной коннектомике

**Mikula (2016)** систематизирует шаги создания коннектома малого млекопитающего (например, мыши), включая методы **BROPA‑окрашивания**, **SBEM**, **ATUM**, **multiSEM**, и оценивает требования по времени (до 1,5 года на мозг мыши при 20 нм вокселе) и объёму хранения (десятки петабайт) ([Frontiers][2]).

---

## 3. Криосохранение ультраструктуры тканей

**McKenzie et al. (2024)** провели реалистичный синтез 97 исследований, классифицировав методы криофиксации, просто­го замораживания и использования криопротектантов. Выяснилось, что для крупных образцов мозга (сотни мм³) необходимы перфузионные протоколы с криопротектантами и новые решения, иначе неизбежно формируются ледяные артефакты и механические повреждения ткани ([PMC][3]).

---

## 4. Витрификация и визуализация негибридных образцов

**Creekmore et al. (2024)** впервые продемонстрировали методику **вотикального plunge‑freezing** автопсийного человеческого мозга толщиной \~180 µм с последующим **xenon plasma FIB‑миллингом** и **cryo‑ET**, что позволило визуализировать органеллы, компоненты аутофагии, потенциальные тау‑фибриллы и компактный миелин без предварительной фиксации и замораживания ([Nature][4]).

---

## 5. Дорожная карта по эмуляции мозга

В классическом отчёте **Sandberg & Bostrom (2008)** изложены этапы **WBE (Whole Brain Emulation)**: от сканирования (nanotomography, EM) и подготовки образцов, через обработку и сегментацию изображений, до физической симуляции нейронных и молекулярных процессов на экзаскейл‑кластерах. Авторы оценивают неопределённости, альтернативные пути, ключевые проблемы и дають количественные прогнозы по вычислительным требованиям и возможным срокам ([fhi.ox.ac.uk][5]).

---

## 6. Масштабируемые методы контрастирования

**Lu et al. (2023)** разработали протокол **ODeCO (Osmication‑Destaining‑Conditioning‑Osmication)** для равномерного пропитывания всего мозга мыши осмием, следя за прогрессом реакции с помощью **X‑ray microCT**. Протокол исключает образования трещин и макро‑фрагментации, сокращает время окрашивания до \~54 ч и открывает путь к полноценному коннектому мышиного мозга ([PMC][6]).

---

## 7. Альдегид‑стабилизированная криоконсервация

Метод **Aldehyde‑Stabilized Cryopreservation** (АСК), впервые описанный McIntyre & Fahy (2015), позволяет сохранять морфологию мембран и внутриклеточных структур в «near‑perfect» состоянии при −135 °C. При этом подтверждена целостность синапсов и мембран после оттаивания ([Wikipedia][7]).

---

## 8. Оптическая коннектомика

**Sneve & Piatkevich (2022)** в обзоре **“Towards a Comprehensive Optical Connectome at Single Synapse Resolution”** рассматривают расширительную микроскопию (ExM) с использованием генетически кодируемых флуоресцентных зондами для визуализации пост‑ и пресинаптических компонентов. Несмотря на достижения в разрешении \~20–50 нм, объём покрытия остаётся ограниченным долями мм³, а непрерывная сегментация длинных нейритов — технологическим вызовом ([PMC][8], [PubMed][9]).

---

## 9. Стандартизация криопротекции

В недавней статье **Frontiers in Neuroanatomy (2023)** представлена **платформа для стандартизированной криопротекции и замораживания** больших образцов ткани, сочетающая химическую фиксацию и оптимизированные протоколы перфузионного введения криопротектантов, что снижает артефакты во время микротомии и упрощает последующую трёхмерную реконструкцию ([Frontiers][2]).

---

## 10. Высококонтрастное en bloc‑окрашивание

**Zhao et al. (2023)** в *Nature Methods* предложили новый **en bloc‑протокол** контрастирования, позволяющий получить равномерное и высококонтрастное окрашивание мозга мыши и образцов человека, что критично для ускорения автоматизированной трассировки нейронов и улучшения качества сегментации ([PMC][6]).

---

## Заключение

Современные достижения показывают, что технически **все** компоненты «загрузки сознания» (от нанесения контрастов и сохранения ультраструктуры до обработки и симуляции) существуют в виде разрозненных этапов. Однако их интеграция в единую, отлаженную цепочку с учётом масштаба человеческого мозга находится на горизонте **десятилетий**, требуя дальнейших исследований в коннектомике, криобиологии, высокопроизводительных вычислениях и этическом регулировании.

[1]: https://pubmed.ncbi.nlm.nih.gov/39970909/ "Comparative prospects of imaging methods for whole-brain mammalian connectomics - PubMed"
[2]: https://www.frontiersin.org/journals/neuroanatomy/articles/10.3389/fnana.2016.00062/full "Frontiers | Progress Towards Mammalian Whole-Brain Cellular Connectomics"
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11753176/ "
            Cryopreservation of brain cell structure: a review - PMC
        "
[4]: https://www.nature.com/articles/s41467-024-47066-1 "Ultrastructure of human brain tissue vitrified from autopsy revealed by cryo-ET with cryo-plasma FIB milling | Nature Communications"
[5]: https://www.fhi.ox.ac.uk/brain-emulation-roadmap-report.pdf "Whole Brain Emulation: A Roadmap"
[6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10557665/ "
            A Scalable Staining Strategy for Whole-Brain Connectomics - PMC
        "
[7]: https://en.wikipedia.org/wiki/Aldehyde-stabilized_cryopreservation "Aldehyde-stabilized cryopreservation - Wikipedia"
[8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8803729/ "Towards a Comprehensive Optical Connectome at Single Synapse ..."
[9]: https://pubmed.ncbi.nlm.nih.gov/35115916/ "Towards a Comprehensive Optical Connectome at Single Synapse ..."


---





## Сравнительный анализ коннектомики и нейроинтерфейсов мухи, мыши и человека

### Таблица сравнения

| Аспект                             | Муха (Drosophila)                                                                                                                                                                                                                                                                                                                                                                               | Мышь (Mus musculus)                                                                                                                                                                                                                                                                                        | Человек                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Сканирование мозга**             | Полное EM-сканирование; опубликован полный коннектом взрослой мухи (\~139 255 нейронов и \~5·10^7 синапсов) \[[nature.com](https://www.nature.com/articles/s41586-024-07558-y)] \[[princeton.edu](https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain)]. Визуализация на уровне синапсов (нм-масштаб) достигнута (срезы \~40 нм). | Частичное EM-сканирование (например, 0.1 мм³ зрительной коры с \~200 000 нейронов и 5.23·10^8 синапсов) \[[nature.com](https://www.nature.com/nature/volumes/640/issues/8058)]. Действуют крупные проекты (MouseLight, IARPA). Полный коннектом мозга пока недостижим.                                     | Фрагментарно: EM-скан 1 мм³ коры \[[science.pdf](https://dmg5c1valy4me.cloudfront.net/wp-content/uploads/2024/05/09142702/science.adk4858.pdf)]. Макроскопические методы (диффузионная МРТ) дают лишь грубые схемы. Полный синоптический уровень невозможен.                                                                              |
| **Замена нейронов (импланты)**     | Не реализовано. Теоретическая замена без экспериментальной поддержки.                                                                                                                                                                                                                                                                                                                           | Эксперименты с нейроинтерфейсами (оптогенетика, микроэлектроды), но прямой по-нейронной замены нет.                                                                                                                                                                                                        | Нейропротезы: кохлеарные, ретинальные импланты, DBS. ВМ-интерфейсы (Neuralink – 3072 электродов) \[[pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6914248/)]. Замена каждого нейрона – пока идея.                                                                                                                        |
| **Эмуляция (аппаратные средства)** | Симуляция всех 139 255 нейронов и 50 млн синапсов на ноутбуке \[[berkeley.edu](https://news.berkeley.edu/2024/10/02/researchers-simulate-an-entire-fly-brain-on-a-laptop-is-a-human-brain-next)] + SpiNNaker \[[pmc](https://pmc.ncbi.nlm.nih.gov/articles/PMC6939236/)].                                                                                                                       | Требуются суперкомпьютеры: Blue Brain Project (\~30 тыс. нейронов) \[[guardian.com](https://www.theguardian.com/science/2015/oct/08/complex-living-brain-simulation-replicates-sensory-rat-behaviour)], SpiNNaker, прогноз полной симуляции \~2034 \[[pubmed](https://pubmed.ncbi.nlm.nih.gov/39571736/)]. | Эмуляция невозможна: даже эксафлопные суперкомпьютеры не справятся с \~10^11 нейронов и \~10^15 синапсов. Оценки — не ранее середины XXI века \[[frontiersin.org](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1570104/full)].                                                                           |
| **Экспериментальные достижения**   | Достигнут полный коннектом взрослой мухи \[[princeton.edu](https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain)] \[[berkeley.edu](https://news.berkeley.edu/2024/10/02/researchers-simulate-an-entire-fly-brain-on-a-laptop-is-a-human-brain-next)].                                                                              | Коннектомы отдельных участков (зрительная кора, 523 млн синапсов) \[[nature.com](https://www.nature.com/nature/volumes/640/issues/8058)]. Нейроинтерфейсы: усиление памяти у крыс.                                                                                                                         | EM-коннектом 1 мм³ коры (10^8 синапсов) \[[science.pdf](https://dmg5c1valy4me.cloudfront.net/wp-content/uploads/2024/05/09142702/science.adk4858.pdf)]. Проекты: Human Connectome, BigBrain, мозг–машина \[[nature.com](https://www.nature.com/articles/s41586-023-06094-5)] \[[pmc](https://pmc.ncbi.nlm.nih.gov/articles/PMC7723930/)]. |




*реконструкция всех нейронов мозга взрослой мухи на основе EM-коннектома [Princeton University](https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain), [Nature](https://www.nature.com/articles/s41586-024-07558-y).*

---


### Анализ прогресса и перспектив

**Сканирование мозга.**
У мух достигнут полный коннектом на ультраструктурном уровне (электронная микроскопия) \[[nature.com](https://www.nature.com/articles/s41586-024-07558-y)] \[[princeton.edu](https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain)]. Для мыши и особенно человека объёмы данных экспоненциально возрастают: кусок коры мыши 0.1–10 мм³ уже потребовал мегапиксельной съёмки \[[nature.com](https://www.nature.com/nature/volumes/640/issues/8058)] \[[news.harvard.edu](https://news.harvard.edu/gazette/story/2023/09/human-brain-too-big-to-map-so-theyre-starting-with-mice)]. А полный мозг далёк от обозримого (сотни млн мм³). Для человека решали небольшой фрагмент 1 мм³ \[[science](https://dmg5c1valy4me.cloudfront.net/wp-content/uploads/2024/05/09142702/science.adk4858.pdf)] — это «микромозг», хотя и с сотнями миллионов синапсов. Выделение целого мозга или «ультрасрез» всего мозга человека потребует катастрофических затрат времени и памяти, пока такого решения нет \[[pubmed](https://pubmed.ncbi.nlm.nih.gov/39571736)].

**Нейроинтерфейсы и «искусственные нейроны».**
Сегодня нейроинтерфейсы расширяют возможности мозга (например, интерфейсы «мозг–компьютер» позволяют парализованным людям двигать курсор или протез \[[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6914248/)], а «мозг–спин» восстанавливает способность ходить \[[nature.com](https://www.nature.com/articles/s41586-023-06094-5)]). Существуют сенсорные протезы (слуховые, зрительные импланты), стимулирующие нейроны, но они не заменяют биологические нейроны один к одному. Теоретические «электронные нейроны» на базе мемристоров или CMOS-элемента рассматриваются, однако на практике их применение в живом мозге не выполнено. По-нейронная замена функций потребовала бы вживления сотен миллиардов одноклеточных устройств, что пока нереализуемо.

**Эмуляция мозга (вычислительные платформы).**
Мозг мухи настолько мал, что его можно смоделировать на обычном ноутбуке \[[berkeley.edu](https://news.berkeley.edu/2024/10/02/researchers-simulate-an-entire-fly-brain-on-a-laptop-is-a-human-brain-next)]. Нейроморфные компьютеры (SpiNNaker, TrueNorth, Loihi) показывают: тысячи и десятки тысяч нейронов и миллионы синапсов запускаются в реальном времени при низком энергопотреблении \[[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6939236/)] \[[Frontiers](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1570104/full)]. Мозг мыши (≈10^8 нейронов) потребует крупных суперкомпьютеров. Прогнозы (с учётом роста мощностей GPU/AI-систем) дают дату \~2034 г. для симуляции «в реальном масштабе» мозга мыши \[[pubmed](https://pubmed.ncbi.nlm.nih.gov/39571736/)]. Мозг человека (\~10^11 нейронов) – на порядок-с-половину сложнее; эксперты считают эмуляцию крайне далёкой перспективой (после 2044 г.) \[[pubmed](https://pubmed.ncbi.nlm.nih.gov/39571736)]. Фактически, прямо сейчас даже самые продвинутые суперЭВМ не могут полноценно эмулировать подобную сеть. Появление новых архитектур (оптические нейроморфные чипы, квантовые вычисления) – лишь надежда на будущее.

**Эксперименты и текущие достижения.**
На животных сделан заметный прогресс: полные коннектомы макроорганизмов ограничены *Caenorhabditis* (302 нейрона) и Drosophila (139 тыс. нейронов) \[[princeton.edu](https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain)].
У мыши картируется локальный коннект (зрительные цепи) и строятся крупные атласы (MouseLight, MICrONS) \[[nature.com](https://www.nature.com/nature/volumes/640/issues/8058)].
У людей созданы лишь частичные структурные карты (МРТ-«коннектом»).
Модельные системы (выращенные органоиды) демонстрируют сложную активность («мозговые волны»), но остаются очень примитивными \[[pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7723930/)].

> Несмотря на большие достижения в технологии нейросканирования и интерфейсов, полный перенос сознания (полная эмуляция мозга) пока находится за гранью реального. Ограничения — в разрешающей способности сканеров, объёме данных и в вычислительной мощности — сводят задачу к дальним перспективам \[[pubmed](https://pubmed.ncbi.nlm.nih.gov/39571736/)] \[[frontiersin.org](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1570104/full)].

Каждая новая ступень (получение частичных коннектомов, создание протезов памяти, ускорение нейрокомпьютеров) приближает нас к пониманию, но феномен сознания остаётся технологическим вызовом будущего.

---


**Источники:** современные публикации и обзоры по коннектомике, нейроинтерфейсам и нейроморфным вычислениям:

1. Nature: "Neuronal wiring diagram of an adult brain"
   [https://www.nature.com/articles/s41586-024-07558-y](https://www.nature.com/articles/s41586-024-07558-y)([Википедия][1])

2. Princeton University: "Mapping entire fly brain step toward understanding diseases of human brain"
   [https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain](https://www.princeton.edu/news/2024/10/02/mapping-entire-fly-brain-step-toward-understanding-diseases-human-brain)

3. Nature: "Seven papers in this week’s issue"
   [https://www.nature.com/nature/volumes/640/issues/8058](https://www.nature.com/nature/volumes/640/issues/8058)

4. Science: "Reconstructed thousands of neurons, more and also providing tools for"
   [https://dmg5c1valy4me.cloudfront.net/wp-content/uploads/2024/05/09142702/science.adk4858.pdf](https://dmg5c1valy4me.cloudfront.net/wp-content/uploads/2024/05/09142702/science.adk4858.pdf)

5. PMC: "Real with increasing SNN size, breaking"
   [https://pmc.ncbi.nlm.nih.gov/articles/PMC6939236/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6939236/)

6. Frontiers in Neuroscience: "Adaptable and cost, 2019"
   [https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1570104/full](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2025.1570104/full)

7. PMC: "Brain machine"
   [https://pmc.ncbi.nlm.nih.gov/articles/PMC6914248/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6914248/)

8. PubMed: "Large, 2034, marmoset around 2044, and"
   [https://pubmed.ncbi.nlm.nih.gov/39571736/](https://pubmed.ncbi.nlm.nih.gov/39571736/)

9. PMC: "Treatments and drugs, I focus particularly on the"
   [https://pmc.ncbi.nlm.nih.gov/articles/PMC7723930/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7723930/)

10. UC Berkeley News: "Researchers simulate an entire fly brain on a laptop — is a human brain next?"
    [https://news.berkeley.edu/2024/10/02/researchers-simulate-an-entire-fly-brain-on-a-laptop-is-a-human-brain-next/](https://news.berkeley.edu/2024/10/02/researchers-simulate-an-entire-fly-brain-on-a-laptop-is-a-human-brain-next/)

11. Nature: "A spinal cord injury interrupts, reliability has remained stable over"
    [https://www.nature.com/articles/s41586-023-06094-5](https://www.nature.com/articles/s41586-023-06094-5)

---

## Сеттлеретика

Сеттлеретика — это междисциплинарная наука, разработанная Яном Корчмарюком, которая объединяет нейронауку, кибернетику, философию сознания и футурологию. Её основная цель — обеспечение «цифрового бессмертия» путём постепенного переноса психических функций человека с биологического мозга на искусственный нейрокомпьютер.

Сеттлеретика представляет собой инновационный подход к решению проблемы смертности человека, предлагая научно обоснованный путь к цифровому бессмертию. Она объединяет различные научные дисциплины и предлагает глубокие философские размышления о будущем человечества.

---

### Основные идеи сеттлеретики

1. **Нейрокибернетическое дублирование**
   Сеттлеретика предлагает поэтапное копирование нейронных структур и функций мозга в искусственную среду. Этот процесс осуществляется постепенно, в течение жизни человека, с целью создания резервной нейросистемы, способной полностью заменить биологический мозг.

2. **Переселение психики**
   По мере деградации биологических нейронов их функции берёт на себя нейрокомпьютер. В конечном итоге, когда все функции мозга будут перенесены, сознание человека продолжит существовать в искусственной среде, обеспечивая тем самым бессмертие личности.

3. **Технологическая реализация**
   Проект предусматривает использование передовых технологий, таких как бионические нейроны, квантовые и фотонные вычисления, для создания высокопроизводительных нейрокомпьютеров, способных точно воспроизводить функции человеческого мозга.

4. **Этические и философские аспекты**
   Сеттлеретика поднимает вопросы о природе сознания, идентичности и морали в контексте переноса психики в искусственную среду. Она предлагает новый взгляд на эволюцию человека и его место во Вселенной.


https://www.settleretics.ru/


* описан подход Сеттлеретики как переноса всей психики как системной надструктуры;
* изложен метод Винера–Вольтерра (ряды и ядра) применительно к нейромоделированию;
* рассмотрена возможность моделирования нейронных блоков как «чёрных ящиков» и переход к макроуровню (колонки Маунткастла, зоны);
* приведены примеры научных работ, использующих эти методы в анализе нейронных процессов.


---

В подходе сеттлеретики перенос сознания трактуется как перемещение всей психики единой надсистемой, где сознание и личность – вложенные подсистемы. Вместо поэлементного копирования нейронной сети предлагается описывать нейрон как «чёрный ящик» и аппроксимировать его вход–выход с помощью функциональных рядов (ряды Винера–Вольтерра)
[eng.ucy.ac.cy](https://www.eng.ucy.ac.cy/gmitsis/Publications/EMBS_2011_neuronal.pdf#:~:text=The%20Wiener%20series%20is%20an,t%29%20%3D%20X%E2%88%9E%20n%3D0)
[pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7925423/#:~:text=%28Birpoutsoukis%20et%20al,input)

Такой метод позволяет перейти к моделям более высокого порядка: кортикальным микроколонкам (вертикальным колонкам по Маунткастлу) и их совокупностям – макроколонкам
[pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC1569491/#:~:text=there%20is%20potential%20for%20confusion,together%20like%20sticks%20in%20a)
[pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC2820381/#:~:text=Vernon%20Mountcastle%20was%20the%20first,somatosensory%20cortex%20of%20the%20rodent)

А затем – к континуальным (полевым) моделям зон коры. Подобная континуальная аппроксимация усредняет активность больших областей и снижает сложность моделирования на несколько порядков
[arxiv.org](https://arxiv.org/pdf/2103.10554#:~:text=understand%20these%20data%20recordings,to%20both%20forward%20modelling%20approaches)

Кроме того, в расчет берутся ограничения конечного набора сенсорных входов и моторных выходов мозга, что дополнительно уменьшает объём необходимого моделирования.

---

**Источники:**

* [Nonlinear system identification of neural systems from neurophysiological signals - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7925423/#:~:text=%28Birpoutsoukis%20et%20al,input)
* [The Volterra-Wiener Approach in Neuronal Modeling](https://www.eng.ucy.ac.cy/gmitsis/Publications/EMBS_2011_neuronal.pdf#:~:text=The%20Wiener%20series%20is%20an,t%29%20%3D%20X%E2%88%9E%20n%3D0)
* [Microcolumns and Macropatterns in Cortex - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1569491/#:~:text=there%20is%20potential%20for%20confusion,together%20like%20sticks%20in%20a)
* [Mountcastle's discovery of cortical columns - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2820381/#:~:text=Vernon%20Mountcastle%20was%20the%20first,somatosensory%20cortex%20of%20the%20rodent)
* [Neural field theory and cortical modeling - arXiv](https://arxiv.org/pdf/2103.10554#:~:text=understand%20these%20data%20recordings,to%20both%20forward%20modelling%20approaches)



---


Оглавление: 
- [ЭИРО framework](/README.md)



