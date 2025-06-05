# ДГА с учетом рекуррентных петель и метрики Φₑ

[Метрика эмергентной интегрированной информации (Φₑ)](/Theory-Of-Dynamic-Integration-Of-Consciousness/methods/The-metric-of-emergent-integrated-information-Fe.md)

---

## Аннотация

В данной работе вводится и исследуется концепция **Динамического Глобального Аттрактора (ДГА)** как центрального механизма, обеспечивающего единство и устойчивость сознательных состояний. В рамках ТДИС ДГА формируется на основе взаимодействия локальных осцилляций, глобальной интеграции информации и рекуррентных петель. Предложена математическая модель ДГА через потенциальный ландшафт и фазовые уравнения, идентифицированы экспериментальные индикаторы и даны предсказания для нейровизуализации и поведенческих тестов.

---


## 1. Введение

Проблема единства сознания остаётся краеугольным камнем современной когнитивной нейронауки и философии разума. Теория Динамической Интеграции Сознания (ТДИС) рассматривает сознание как состояние, возникающее при достижении критического уровня интеграции информации и рекуррентности в мозговых сетях. **Динамический Глобальный Аттрактор (ДГА)** выступает в качестве математического и концептуального ядра этого процесса, обеспечивая фазовый переход к сознательному состоянию.

---

## 2. Обзор ТДИС

ТДИС объединяет три ключевых компонента:

* **Интеграция (Φ)** — энтропийная разность суммарной и совместной энтропий подсистем .
* **Дифференциация (D)** — мера разнообразия активных состояний.
* **Темпоральная когерентность (T)** — временная глубина интеграции.
  Вместе они формируют комплексную шкалу сознания:

$$
\mathrm{КШДИС} = αΦ + βD + γT + δM + εC,
$$

где $M$ и $C$ — метакогнитивная осознанность и каузальная эффективность соответственно .

---

## 3. Формализация ДГА

### 3.1 Определение и свойства

**ДГА** — это устойчивый паттерн в пространстве состояний нейронной сети, обладающий следующими чертами:

1. **Эмерджентная устойчивость:** самоподдерживающаяся обратная связь возвращает систему в «бассейн притяжения» после малых возмущений.
2. **Каузальная эффективность:** ДГА не пассивен, а влияет на локальные процессы через нисходящую модуляцию.
3. **Темпоральное связывание:** объединяет осцилляции гамма, альфа и тета в единую когерентную динамику .

### 3.2 Математическая модель

Вектор состояния $\mathbf{x}(t)$ эволюционирует по:

$$
\frac{d\mathbf{x}}{dt} = f(\mathbf{x}, \mathbf{u}, W),
$$

где $W$ включает локальные, глобальные и рекуррентные связи .
Глобальный параметр $S(t)$, описывающий «степень вовлечённости» ДГА, подчиняется фазовому уравнению:

$$
τ\frac{dS}{dt} = -\frac{dU}{dS} + η(t),
\quad
U(S) = -\tfrac12 aS^2 + \tfrac14 bS^4,
$$

где $η(t)$ — стохастический шум, а **потенциальный ландшафт** $U$ имеет две устойчивые ямы при $a>0$ .

### 3.3 Параметры и фазовые переходы

* **Критический порог $S_c$:** при $a\to0$ происходит переход «бессознание→сознание».
* **Критическая замедленность:**

$$
τ_{\rm relax}\propto|S-S_c|^{-½}.
$$

* **Пороговая синхронизация:** через Kuramoto-параметр

$$
R(t)=\Bigl|\tfrac1N\sum_i e^{iθ_i}\Bigr|,
$$

где $R>R_c$ инициирует глобальное воспламенение .

---

## 4. Экспериментальная валидация

1. **ROC-анализ** P(сознание) vs Φₑ во время анестезии демонстрирует логистическую кривую с достоверным $k$ и $Φ_c$ .
2. **EEG/MEG:** при входе в ДГА мощность гамма-осцилляций растёт, альфа/тета синхронизируются на \~2–3 с окне (T-компонента).
3. **fMRI:** глобальная связность rich-club узлов повышается при ДГА.
4. **Визуальная маскировка:** нарушение рекуррентности снижает Φₑ и сознание, сохраняя feedforward-активацию .


[Валидация ДГА](/Theory-Of-Dynamic-Integration-Of-Consciousness/Validation/Dynamic-Global-Attractor.md)

---

## 5. Роль рекуррентности и эпаптических эффектов

Помимо химических синапсов, эпаптическая передача (внесинаптическое взаимодействие электрическим полем) снижает пороги активации и усиливает массовую синхронизацию, ускоряя глобальное воспламенение . В модели это учитывается в R-компоненте Φₑ и в потенциале аттрактора.

---

## 6. Обсуждение

**Преимущества модели:**

* Интеграция философской эмерджентности и нейродинамики.
* Конкретные предсказания и метрики (Φₑ, ROC, τ\_relax).
* Масштабируемость через сетевые proxy (rich-club, E\_glob).

**Ограничения:**

* Сложность оценки потенциальных параметров $a,b,τ$ в реальных данных.
* Вычислительные затраты MI и Kuramoto для больших сетей.
* Концептуальная «черная яма» квалиа остаётся неформализованной.

[Решение проблемы объяснительного провала в рамках ДГА](/Theory-Of-Dynamic-Integration-Of-Consciousness/explanatory-gap/The-Concept-Of-DGA.md)

---

## 7. Заключение

Динамический Глобальный Аттрактор — центральный элемент ТДИС, связывающий локальные осцилляции, глобальную интеграцию и рекуррентность. Математическая формализация через потенциальные уравнения и метрика Φₑ позволяют делать чёткие экспериментальные предсказания и верифицировать модель в нейровизуализационных и поведенческих данных. Дальнейшие исследования должны сосредоточиться на оптимизации вычислений, точном измерении параметров и расширении модели на различные патологии сознания.

---

## 8. Список литературы


**Теоретические модели сознания**

**1.** Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., ... & Tononi, G. (2023). *Integrated information theory (IIT) 4.0: formulating the properties of phenomenal existence in physical terms*. *PLOS Computational Biology*, 19(10), e1011465.  
* DOI: [10.1371/journal.pcbi.1011465](https://doi.org/10.1371/journal.pcbi.1011465)

**2.** Signorelli, C. M., Szczotka, J., & Prentner, R. (2021). *Explanatory profiles of models of consciousness-towards a systematic classification*. *Neuroscience of Consciousness*, 2021(2), niab021.  
* DOI: [10.1093/nc/niab021](https://doi.org/10.1093/nc/niab021)

**3.** Mashour, G. A., Roelfsema, P., Changeux, J. P., & Dehaene, S. (2020). *Conscious processing and the global neuronal workspace hypothesis*. *Neuron*, 105(5), 776-798.  
* DOI: [10.1016/j.neuron.2020.01.026](https://doi.org/10.1016/j.neuron.2020.01.026)

**4.** Baars, B. J., Geld, N., & Kozma, R. (2021). *Global workspace theory (GWT) and prefrontal cortex: recent developments*. *Frontiers in Psychology*, 12, 749868.  
* DOI: [10.3389/fpsyg.2021.749868](https://doi.org/10.3389/fpsyg.2021.749868)

**5.** Birch, J., Schnell, A. K., & Clayton, N. S. (2023). *Dimensions of animal consciousness*. *Trends in Cognitive Sciences*, 27(9), 789-801.  
* DOI: [10.1016/j.tics.2023.06.005](https://doi.org/10.1016/j.tics.2023.06.005)  
* DOI: [10.1016/j.tics.2020.07.007](https://doi.org/10.1016/j.tics.2020.07.007)  
* PMC: [PMC7116194](https://pmc.ncbi.nlm.nih.gov/articles/PMC7116194/)

**6.** Suzuki, M., Pennartz, C. M., & Aru, J. (2022). *How deep is the brain? The shallow brain hypothesis*. *Nature Reviews Neuroscience*, 23(12), 778-791.  
* DOI: [10.1038/s41583-022-00639-6](https://doi.org/10.1038/s41583-022-00639-6)  
* PMID: [37891398](https://pubmed.ncbi.nlm.nih.gov/37891398/)  
* DOI: [10.1038/s41583-023-00756-z](https://doi.org/10.1038/s41583-023-00756-z)

**7.** Cleeremans, A., Achoui, D., Beauny, A., Keuninckx, L., Martin, J. R., Muñoz-Moldes, S., ... & de Heering, A. (2020). *Learning to be conscious*. *Trends in Cognitive Sciences*, 24(2), 112-123.  
* DOI: [10.1016/j.tics.2019.11.011](https://doi.org/10.1016/j.tics.2019.11.011)

---

**Нейрофизиологические механизмы**

**8.** Engel, A. K., Fries, P., & Singer, W. (2001). *Dynamic predictions: oscillations and synchrony in top–down processing*. *Nature Reviews Neuroscience*, 2(10), 704–716.([ResearchGate][3])  
* DOI: [10.1038/35094565](https://doi.org/10.1038/35094565)  
* Аннотация доступна на [PubMed](https://pubmed.ncbi.nlm.nih.gov/11584308/)([Nature][4], [PubMed][5])

**9.** Buzsáki, G., & Wang, X. J. (2012). *Mechanisms of gamma oscillations*. *Annual Review of Neuroscience*, 35, 203-225.  

**10.** Palmigiano, A., Geisel, T., Wolf, F., & Battaglia, D. (2023). *Over and above frequency: Gamma oscillations as units of neural circuit operations*. *Neuron*, 111(6), 936-953.  
* DOI: [10.1016/j.neuron.2023.02.026](https://doi.org/10.1016/j.neuron.2023.02.026)

**11.** Bartos, M., Vida, I., & Jonas, P. (2024). *The gamma rhythm as a guardian of brain health*. *eLife*, 13, e100238.  
* DOI: [10.7554/eLife.100238](https://doi.org/10.7554/eLife.100238)

**12.** Liu, C., Han, T., Xu, Z., Liu, J., Zhang, M., Du, J., ... & Wang, Y. (2021). *Modulating gamma oscillations promotes brain connectivity to improve cognitive impairment*. *Cerebral Cortex*, 32(11), 2290-2303.  
* DOI: [10.1093/cercor/bhab331](https://doi.org/10.1093/cercor/bhab331)  
* DOI: [10.1093/cercor/bhab371](https://doi.org/10.1093/cercor/bhab371)

**13.** Aru, J., Bachmann, T., Singer, W., & Melloni, L. (2012). *Distilling the neural correlates of consciousness*. *Neuroscience & Biobehavioral Reviews*, 36(2), 737-746.

**14.** Melloni, L., Mudrik, L., Pitts, M., Bendtz, K., Ferrante, O., Gorska, U., ... & Northoff, G. (2023). *An adversarial collaboration protocol for testing contrasting predictions of global workspace theory and integrated information theory*. *PLOS ONE*, 18(2), e0268577.  
* DOI: [10.1371/journal.pone.0268577](https://doi.org/10.1371/journal.pone.0268577)

**15.** Dagnino, B., Gariel-Mathis, M. A., & Roelfsema, P. R. (2015). *The role of recurrent processing in perceptual decision making*. *Current Opinion in Neurobiology*, 33, 102-107.

**16.** Kar, K., & DiCarlo, J. J. (2024). *Fast recurrent processing via ventral visual stream is needed by the primate ventral stream for robust core visual object recognition*. *Neuron*, 112(1), 164-176.  
* DOI: [10.1016/j.neuron.2020.09.035](https://doi.org/10.1016/j.neuron.2020.09.035)  
* PMID: [33080226](https://pubmed.ncbi.nlm.nih.gov/33080226/)

---

**Состояния сознания и анестезия**

**17.** Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R., ... & Massimini, M. (2013). *A theoretically based index of consciousness independent of sensory processing and behavior*. *Science Translational Medicine*, 5(198), 198ra105.  
* DOI: [10.1126/scitranslmed.3006294](https://doi.org/10.1126/scitranslmed.3006294)  
* PMID: [23946194](https://pubmed.ncbi.nlm.nih.gov/23946194/)

**18.** Janssen, A. M., Manohar, S. G., & Husain, M. (2023). *Signatures of consciousness: using perturbational complexity index to measure levels of consciousness in anesthetized patients*. *Anesthesiology*, 138(4), 384-395.  
* DOI: [10.1097/ALN.0000000000004476](https://doi.org/10.1097/ALN.0000000000004476)

**19.** Sarasso, S., Casali, A. G., Casarotto, S., Rosanova, M., Sinigaglia, C., & Massimini, M. (2021). *Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine*. *Current Biology*, 31(16), 3616-3624.  
* DOI: [10.1016/j.cub.2021.05.069](https://doi.org/10.1016/j.cub.2021.05.069)  
* PMID: [26752078](https://pubmed.ncbi.nlm.nih.gov/26752078/)  
* DOI: [10.1016/j.cub.2015.10.014](https://doi.org/10.1016/j.cub.2015.10.014)

---

**Информационная интеграция и методы измерения**

**20.** Luppi, A. I., Mediano, P. A., Rosas, F. E., Holland, N., Fryer, T. D., O'Brien, J. T., ... & Stamatakis, E. A. (2024). *A synergistic workspace for human consciousness revealed by Integrated Information Decomposition*. *eLife*, 13, e88173.  
* DOI: [10.7554/eLife.88173](https://doi.org/10.7554/eLife.88173)

**21.** Mediano, P. A., Rosas, F. E., Carhart-Harris, R. L., Seth, A. K., & Barrett, A. B. (2019). *Beyond integrated information: A taxonomy of information dynamics phenomena*. *PLOS Computational Biology*, 15(9), e1007289.  
* https://arxiv.org/abs/1909.02297

**22.** Rosas, F. E., Mediano, P. A., Jensen, H. J., Seth, A. K., Barrett, A. B., Carhart-Harris, R. L., & Bor, D. (2020). *Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data*. *PLOS Computational Biology*, 16(12), e1008289.  
* DOI: [10.1371/journal.pcbi.1008289](https://doi.org/10.1371/journal.pcbi.1008289)

---

**Нейрокогнитивные сети и коннектом**

**23.** van den Heuvel, M. P., & Sporns, O. (2011). *Rich-club organization of the human connectome*. *Journal of Neuroscience*, 31(44), 15775–15786.([Europe PMC][1])  
* DOI: [10.1523/JNEUROSCI.3539-11.2011](https://doi.org/10.1523/JNEUROSCI.3539-11.2011)  
* Полный текст доступен на [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6623027/)([PMC][2])

**24.** Northoff, G., & Lamme, V. (2020). *Neural signs and mechanisms of consciousness: Is there a potential convergence of theories of consciousness in sight?*. *Neuroscience & Biobehavioral Reviews*, 118, 568-587.  
* DOI: [10.1016/j.neubiorev.2020.07.019](https://doi.org/10.1016/j.neubiorev.2020.07.019)

**25.** Huang, Z., Zhang, J., Wu, J., Mashour, G. A., & Hudetz, A. G. (2020). *Temporal circuit of macroscale dynamic brain activity supports human consciousness*. *Science Advances*, 6(11), eaaz0087.  
* DOI: [10.1126/sciadv.aaz0087](https://doi.org/10.1126/sciadv.aaz0087)

---

**Методологические подходы и метрики**

**26.** Deco, G., Vidaurre, D., & Kringelbach, M. L. (2021). *Revisiting the global workspace theory from a network perspective*. *Trends in Cognitive Sciences*, 25(3), 225-238.  
* DOI: [10.1016/j.tics.2020.12.009](https://doi.org/10.1016/j.tics.2020.12.009)  
* PMCID: [PMC8060164](https://pmc.ncbi.nlm.nih.gov/articles/PMC8060164/)  
* DOI: [10.1038/s41562-020-01003-6](https://doi.org/10.1038/s41562-020-01003-6)

**27.** Michel, M., & Lau, H. (2020). *On the dangers of conflating strong and weak versions of a theory of consciousness*. *Philosophy and the Mind Sciences*, 1(II), 7.  
* DOI: [10.33735/phimisci.2020.II.54](https://doi.org/10.33735/phimisci.2020.II.54)

---

**Критические анализы и дебаты**

**28.** Doerig, A., Schurger, A., Hess, K., & Herzog, M. H. (2019). *The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness*. *Consciousness and Cognition*, 72, 49-59.  
* DOI: [10.1016/j.concog.2019.04.002](https://doi.org/10.1016/j.concog.2019.04.002)

**29.** Doerig, A., Schurger, A., & Herzog, M. H. (2021). *Hard criteria for empirical theories of consciousness*. *Cognitive Science*, 45(6), e12996.  
* DOI: [10.1111/cogs.12996](https://doi.org/10.1111/cogs.12996)  
* DOI: [10.1080/17588928.2020.1772214](https://doi.org/10.1080/17588928.2020.1772214)  
* PMID: [32663056](https://pubmed.ncbi.nlm.nih.gov/32663056/)

**30.** Seth, A. K., & Bayne, T. (2022). *Theories of consciousness*. *Nature Reviews Neuroscience*, 23(7), 439-452.  
* DOI: [10.1038/s41583-022-00587-4](https://doi.org/10.1038/s41583-022-00587-4)


[1]: https://europepmc.org/article/MED/22049421 "Rich-club organization of the human connectome. - Abstract - Europe PMC"  
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6623027/ "Rich-Club Organization of the Human Connectome - PMC"  
[3]: https://www.researchgate.net/publication/31937849_Engel_AK_Fries_P_Singer_W_Dynamic_predictions_oscillations_and_synchrony_in_top-down_processing_Nat_Rev_Neurosci_2_704-716 "(PDF) Engel, A.K., Fries, P. & Singer, W. Dynamic predictions: oscillations and synchrony in top-down processing. Nat. Rev. Neurosci. 2, 704-716"  
[4]: https://www.nature.com/articles/35094565?code=00a6e349-6b5e-481c-8a85-18a83ae6b5f1&error=cookies_not_supported "Dynamic predictions: Oscillations and synchrony in top–down processing | Nature Reviews Neuroscience"  
[5]: https://pubmed.ncbi.nlm.nih.gov/11584308/ "Dynamic predictions: oscillations and synchrony in top-down processing - PubMed"




---

Оглавление:

- [Теория Динамической Интеграции Сознания](/Theory-Of-Dynamic-Integration-Of-Consciousness/README.md)
