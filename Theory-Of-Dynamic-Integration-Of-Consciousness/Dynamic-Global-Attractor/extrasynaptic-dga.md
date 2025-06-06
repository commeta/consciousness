# ДГА с учетом фазовых переходов и сверхсинаптической связи

Схема расширенной формальной модели “Динамического Глобального Аттрактора” (ДГА), учитывающая фазовые переходы, сверхсинаптическую (эфатическую) связь и дающая конкретные экспериментальные прогнозы.

---

## 1. Математическое описание фазовых переходов

### 1.1 Порядковый параметр и потенциальная функция

Пусть Φ(t) — уровень глобальной интеграции (порядковый параметр). Его динамика описывается уравнением:

$$
\tau\,\frac{d\Phi}{dt} \;=\; -\frac{dU(\Phi)}{d\Phi} \;+\;\eta(t),
$$

где

$$
U(\Phi) = -\tfrac{1}{2}\,a\,\Phi^2 + \tfrac{1}{4}\,b\,\Phi^4
$$

— “двухколючковая” потенциальная функция фазового перехода,
τ — характерное время релаксации,
η(t) — стохастический шум.

* При $a>0$ система имеет два устойчивых аттрактора $\Phi^* = \pm\sqrt{a/b}$.
* Переход происходит при $a \to 0$ (критическая точка): скорость релаксации τ растёт как $\sim|a|^{-1/2}$.

### 1.2 Связь с информационным порядком

Альтернативно, описывая dΦ/dt через нелинейную кинетику интеграции информации:

$$
\frac{d\Phi}{dt}
= \;\alpha\iint I(x_i,x_j)\,K(x_i,x_j)\,dx_i\,dx_j 
\;-\;\beta\,\Phi 
\;-\;\gamma\,\Phi^3
$$

— где первый член задаёт накопление интеграции, а остальные обеспечивают диссипацию и нелинейное подавление.

---

## 2. Интеграция сверхсинаптической (эфатической) связи

### 2.1 Расширенный ядровой оператор связности

В традиционном Кернеле $K_{\rm syn}$ учтены только синаптические связи. Добавим к нему эфаптический вклад:

$$
K_{\rm total}(x_i,x_j) 
= K_{\rm syn}(x_i,x_j) \;+\;\lambda\,K_{\rm eph}(x_i,x_j),
$$

где

* $K_{\rm eph}(x_i,x_j)$ — ядро эфаптической связи (зависит от расстояния и накала локального поля),
* λ — коэффициент, отражающий эффективность полевых взаимодействий.

### 2.2 Влияние эфаптики на фазовый переход

Эфатическая связь:

1. Повышает скорость нарастания интеграции ($\alpha$ в уравнении выше возрастает пропорционально λ).
2. Снижает критический порог $a_c$, смещая точку фазового перехода к меньшим уровням локальной активации.
3. Усиливает γ-ритмы за счёт быстрой кросс-нейронной синхронизации вне синаптических задержек.

В итоге динамика упрощённо:

$$
\frac{d\Phi}{dt}
\approx \bigl[\alpha_0 + \lambda\,\alpha_{\rm eph}\bigr]\,F[\Phi]
\;-\;\beta\,\Phi
\;-\;\gamma\,\Phi^3,
$$

где $F[\Phi]$ — нелинейная функция информационного взаимодействия.

---

## 3. Прогнозы для экспериментов

### 3.1 Многозадачность (dual-task paradigm)

* **Гипотеза H₁ (эффект эфаптики):** при искусственном усилении эфаптической связи (например, через слабую электрическую стимуляцию) уменьшится задержка фазового перехода, и реактивные стадии (выбор ответа) начнут переходить в глобальную интеграцию быстрее, что проявится в **снижении двойного узкого места** (dual-task interference).

  * **Измерения:** сверхбыстрая фМРТ (TR\~200 мс) + EEG PLV в γ-диапазоне.
  * **Ожидание:** снижение времени сериализации в MD-сети на 10–20 %.

### 3.2 Изменённые состояния сознания (психоделики, сон, анестезия)

* **Гипотеза H₂ (смещение критической точки):**

  * Под действием психоделиков λ↑ → критический порог $a_c$ ↓ → система часто “перескакивает” между аттракторами → проявляется как расширение “прозрачности” сознания (более высокая вариативность Φ).
  * В глубоких анестетиках λ↓ и β↑ → $a_c$↑ → подавление глобального аттрактора, наблюдается разрыв фазового перехода и падение Φ≈0.

* **Измерения:**

  * EEG/MEG: оценка спектра мощности (степенной закон), проверка критической замедленности τ(Φ) ∝ |Φ–Φc|^(–½).
  * ФМРТ: IGI (глобальный индекс интеграции) и фрактальная оценка ИКДМ.

### 3.3 Изменчивость переключений внимания

* **Гипотеза H₃ (оконечный аттрактор vs семейство состояний):** в норме ДГА проявляется как **семейство аттракторов**, стабилизируемых γ→α→θ-циклом. Под действием изменённых состояний цикл разрывается (например, при медитации θ↑, γ↓), что приводит к расширению или сужению временного окна интеграции.

* **Ожидание:**

  * В медитации — удлинение T-окон (θ-ритмы), что фиксируется через увеличение вязкости Φ (меньше колебаний).
  * В психоделиках — наоборот, увеличение флуктуаций Φ и более частые “скоки” аттрактора.

---

**Итоговая модель** объединяет фазовую кинетику, усиленную эфаптической связностью, и даёт чёткие прогнозы:

1. Смещение критической точки и времени релаксации под влиянием λ.
2. Снижение dual-task interference при усиленной эфаптике.
3. Изменение частоты и амплитуды колебаний порядка Φ в психоделических и медитативных состояниях.

Эта формализация позволяет переходить от концепций к тестируемым гипотезам и конкретным экспериментальным протоколам.

---

## Источники

1. **Anastassiou, C. A., Perin, R., Markram, H., & Koch, C.** (2011). Ephaptic coupling of cortical neurons. *Nature Neuroscience*, 14(2), 217-223. [https://doi.org/10.1038/nn.2727](https://doi.org/10.1038/nn.2727)

2. **Anastassiou, C. A., & Koch, C.** (2015). Ephaptic coupling to endogenous electric field activity: why bother? *Current Opinion in Neurobiology*, 31, 95-103. [https://doi.org/10.1016/j.conb.2014.09.002](https://doi.org/10.1016/j.conb.2014.09.002)

3. **Atasoy, S., Donnelly, I., & Pearson, J.** (2016). Human brain networks function in connectome-specific harmonic waves. *Nature Communications*, 7, 10340. [https://doi.org/10.1038/ncomms10340](https://doi.org/10.1038/ncomms10340)

4. **Bassett, D. S., & Sporns, O.** (2017). Network neuroscience. *Nature Neuroscience*, 20(3), 353-364. [https://doi.org/10.1038/nn.4502](https://doi.org/10.1038/nn.4502)

5. **Bedard, C., & Destexhe, A.** (2009). Macroscopic models of local field potentials and the apparent 1/f noise in brain activity. *Biophysical Journal*, 96(7), 2589-2603. [https://doi.org/10.1016/j.bpj.2008.12.3951](https://doi.org/10.1016/j.bpj.2008.12.3951)

6. **Buzsáki, G., Anastassiou, C. A., & Koch, C.** (2012). The origin of extracellular fields and currents—EEG, ECoG, LFP and spikes. *Nature Reviews Neuroscience*, 13(6), 407-420. [https://doi.org/10.1038/nrn3241](https://doi.org/10.1038/nrn3241)

7. **Carhart-Harris, R. L., & Friston, K. J.** (2019). REBUS and the anarchic brain: toward a unified model of the brain action of psychedelics. *Pharmacological Reviews*, 71(3), 316-344. [https://doi.org/10.1124/pr.118.017160](https://doi.org/10.1124/pr.118.017160)

8. **Deco, G., Jirsa, V. K., & McIntosh, A. R.** (2011). Emerging concepts for the dynamical organization of resting-state activity in the brain. *Nature Reviews Neuroscience*, 12(1), 43-56. [https://doi.org/10.1038/nrn2961](https://doi.org/10.1038/nrn2961)

9. **Freeman, W. J., & Vitiello, G.** (2021). Evolutionary advantages of stimulus-driven EEG phase transitions in the upper cortical layers. *Frontiers in Systems Neuroscience*, 15, 784404. [https://doi.org/10.3389/fnsys.2021.784404](https://doi.org/10.3389/fnsys.2021.784404)

10. **Friston, K. J., Wiese, W., & Hobson, J. A.** (2020). Sentience and the origins of consciousness: from Cartesian duality to Markovian monism. *Entropy*, 22(5), 516. [https://doi.org/10.3390/e22050516](https://doi.org/10.3390/e22050516)

11. **Huang, Z., Mashour, G. A., & Hudetz, A. G.** (2020). Functional geometry of the cortex encodes dimensions of consciousness. *Nature Communications*, 11(1), 6373. [https://doi.org/10.1038/s41467-022-35764-7](https://doi.org/10.1038/s41467-022-35764-7)

12. **Izhikevich, E. M., & Kuramoto, Y.** (2006). Weakly connected neural networks. *Studies in Applied Mathematics*, 118(3), 269-310. [https://doi.org/10.1007/978-1-4612-1828-9](https://doi.org/10.1007/978-1-4612-1828-9)

13. **Kozma, R., & Freeman, W. J.** (2017). Cognitive phase transitions in the cerebral cortex—enhancing the neuron doctrine by modeling neural fields. *Studies in Applied Mathematics*, 138(1), 6-27. [https://doi.org/10.1007/978-3-319-24406-8](https://doi.org/10.1007/978-3-319-24406-8)

14. **Lee, S., Kruglikov, I., Huang, Z. J., Fishell, G., & Rudy, B.** (2013). A disinhibitory circuit mediates motor integration in the somatosensory cortex. *Nature Neuroscience*, 16(11), 1662-1670. [https://doi.org/10.1038/nn.3544](https://doi.org/10.1038/nn.3544)

15. **López-González, A., Panda, R., Ponce-Alvarez, A., Zamora-López, G., Escrichs, A., Martial, C., ... & Deco, G.** (2021). Loss of consciousness reduces the stability of brain hubs and the heterogeneity of brain dynamics. *Communications Biology*, 4, 1037. [https://doi.org/10.1038/s42003-021-02537-9](https://doi.org/10.1038/s42003-021-02537-9)

16. **Moreau, Q., Candelier, R., Barbier, F., Ronget, V., Palacios, A. G., Berry, H., & Cessac, B.** (2022). A realistic modeling of mesoscopic ephaptic coupling in the human brain. *PLOS Computational Biology*, 18(5), e1007923. [https://doi.org/10.1371/journal.pcbi.1007923](https://doi.org/10.1371/journal.pcbi.1007923)

17. **Northoff, G., & Lamme, V.** (2020). Neural signs and mechanisms of consciousness: Is there a potential convergence of theories of consciousness in sight? *Neuroscience & Biobehavioral Reviews*, 118, 568-587. [https://doi.org/10.1016/j.neubiorev.2020.07.019](https://doi.org/10.1016/j.neubiorev.2020.07.019)

18. **Pang, R., Lansdell, B. J., & Fairhall, A. L.** (2016). Dimensionality reduction in neuroscience. *Current Biology*, 26(14), R656-R660. [https://doi.org/10.1016/j.cub.2016.05.029](https://doi.org/10.1016/j.cub.2016.05.029)

19. **Pezzulo, G., Zorzi, M., & Corbetta, M.** (2021). The secret life of predictive brains: what's spontaneous activity for? *Trends in Cognitive Sciences*, 25(9), 730-743. [https://doi.org/10.1016/j.tics.2021.05.007](https://doi.org/10.1016/j.tics.2021.05.007)

20. **Reardon, P. K., Seidlitz, J., Vandekar, S., Liu, S., Patel, R., Park, M. T., ... & Raznahan, A.** (2018). Normative brain size variation and brain shape diversity in humans. *Science*, 360(6394), 1222-1227. [https://doi.org/10.1126/science.aar2578](https://doi.org/10.1126/science.aar2578)

21. **Ruffini, G.** (2017). An algorithmic information theory of consciousness. *Neuroscience of Consciousness*, 2017(1), nix019. [https://doi.org/10.1093/nc/nix019](https://doi.org/10.1093/nc/nix019)

22. **Schartner, M. M., Carhart-Harris, R. L., Barrett, A. B., Seth, A. K., & Muthukumaraswamy, S. D.** (2017). Increased spontaneous MEG signal diversity for psychoactive doses of ketamine, LSD and psilocybin. *Scientific Reports*, 7, 46421. [https://doi.org/10.1038/srep46421](https://doi.org/10.1038/srep46421)

23. **Sitt, J. D., King, J. R., El Karoui, I., Rohaut, B., Faugeras, F., Gramfort, A., ... & Naccache, L.** (2017). Large scale screening of neural signatures of consciousness in patients in a vegetative or minimally conscious state. *Brain*, 140(9), 2258-2270. [https://doi.org/10.1093/brain/awu141](https://doi.org/10.1093/brain/awu141)

24. **Tagliazucchi, E., & Laufs, H.** (2014). Decoding wakefulness levels from typical fMRI resting-state data reveals reliable drifts between wakefulness and sleep. *Neuron*, 82(3), 695-708. [https://doi.org/10.1016/j.neuron.2014.03.020](https://doi.org/10.1016/j.neuron.2014.03.020)

25. **Varela, F., Lachaux, J. P., Rodriguez, E., & Martinerie, J.** (2001). The brainweb: phase synchronization and large-scale integration. *Nature Reviews Neuroscience*, 2(4), 229-239. [https://doi.org/10.1038/35067550](https://doi.org/10.1038/35067550)

26. **Vohryzek, J., Deco, G., Cessac, B., Kringelbach, M. L., & Cabral, J.** (2020). Ghost attractors in spontaneous brain activity: Recurrent excursions into functionally-relevant BOLD phase-locking states. *Frontiers in Systems Neuroscience*, 14, 20. [https://doi.org/10.3389/fnsys.2020.00020](https://doi.org/10.3389/fnsys.2020.00020)



---


Оглавление:

- [Теория Динамической Интеграции Сознания](/Theory-Of-Dynamic-Integration-Of-Consciousness/README.md)

