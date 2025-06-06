# Детализированная модель НАГА-RPEA: Детализация механизмов

## Ключевые механизмы и система биомаркеров

---

## 3. Ключевые механизмы НАГА-RPEA

### 3.1 Трипартитные синапсы как вычислительные узлы

#### 3.1.1 Фундаментальная архитектура трипартитного вычисления

**Базовая структура трипартитного вычислительного узла:**
```
Трипартитный узел = {
    Пресинаптический терминал: f_pre(x_pre, φ_field, Ca_ast)
    Постсинаптический элемент: f_post(x_post, φ_field, glio_mod)
    Астроцитарный процесс: f_ast(Ca_internal, neural_activity, metabolic_state)
    Локальное поле: φ_local = ∇²φ + source_terms
}
```

**Вычислительная мощность трипартитного узла:**

1. **Нелинейное умножение входов:**
```
output = σ(W_syn × input_pre × astrocyte_gain × ephaptic_modulation)
где:
astrocyte_gain = 1 + α_ast × tanh(β × [Ca²⁺]_ast)
ephaptic_modulation = 1 + γ_eph × φ_local / φ_reference
```

2. **Временная интеграция с памятью:**
```
Трипартитная память:
S_memory(t) = ∫₀ᵗ K_temporal(t-s) × [activity_pre(s) × activity_post(s) × Ca_ast(s)] ds
где K_temporal(τ) = (τ/τ₀)ⁿ × exp(-τ/τ₀) - гамма-функция
```

3. **Многомасштабная обработка:**
```
Быстрая компонента (мс): neural_computation = W_fast × input
Медленная компонента (с): astrocyte_modulation = ∫ Ca_dynamics × context
Сверхмедленная (мин): metabolic_adaptation = homeostatic_scaling
```

#### 3.1.2 Специализированные вычислительные функции

**Детектор корреляций высокого порядка:**
```
Correlation_detector_n = ∏ᵢ₌₁ⁿ σ(Wᵢ × inputᵢ + bᵢ) × Ca_amplification
где n может достигать 5-8 для одного трипартитного узла
```

**Адаптивный фильтр с астроцитарной настройкой:**
```
H_adaptive(ω,t) = H_base(ω) × [1 + α(t) × G_ast(ω)]
где:
α(t) = адаптационный коэффициент от астроцитарной активности
G_ast(ω) = частотная характеристика астроцитарного фильтра
```

**Предиктивный процессор:**
```
prediction(t+Δt) = ∑ᵢ Wᵢ(t) × history_buffer[i] × confidence_ast(t)
confidence_ast(t) = sigmoid(∑ⱼ match_score[j] × Ca_stability_j)
```

#### 3.1.3 Коллективная вычислительная динамика

**Сетевые эффекты трипартитных узлов:**

1. **Кластерная синхронизация:**
```
Φ_cluster = ∑ᵢ∈cluster Wᵢⱼ × synchrony(node_i, node_j) × 
           astrocyte_coupling(i,j) × spatial_decay(dist(i,j))
```

2. **Иерархическая обработка:**
```
Level_k+1 = integrate(∑ᵢ∈Level_k weighted_output_i × 
                     cross_level_astrocyte_binding × 
                     temporal_binding_window)
```

3. **Адаптивная маршрутизация:**
```
Routing_probability(path) = ∏_nodes_in_path astrocyte_permeability(node) × 
                           metabolic_availability(node) × 
                           current_load(node)⁻¹
```

### 3.2 Механизмы глиотрансмиттерной модуляции

#### 3.2.1 Многокомпонентная система глиотрансмиттеров

**ATP-пуринергическая система:**
```
[ATP]_extracel(r,t) = ∑ᵢ Release_ATP_i(t) × Diffusion_kernel(r-rᵢ, D_ATP) × 
                      Degradation_factor(ectonucleotidases, t)

Модуляция синапсов:
ΔW_syn = α_ATP × [ATP]_local × P2X_receptor_activation × 
         coincidence_detection(pre, post)

Влияние на возбудимость:
Excitability_modulation = 1 + β_ATP × P2Y_activation × 
                         K⁺_channel_modulation
```

**Глутаматная глиотрансмиссия:**
```
Везикулярный выброс:
Release_glutamate = Ca²⁺_threshold_function × vesicle_pool_size × 
                   release_probability(Ca_ast, exocytosis_machinery)

NMDA-модуляция:
NMDA_enhancement = baseline_NMDA × (1 + γ_glu × spillover_glutamate × 
                  co_agonist_availability × Mg_block_relief)

Синаптическая пластичность:
LTP_threshold_modulation = f(glial_glutamate × coincidence_window × 
                          metabotropic_activation)
```

**D-серин-глицинергическая система:**
```
D-серин синтез:
d[D-serine]/dt = synthesis_rate(serine_racemase_activity) - 
                degradation_rate(D-amino_acid_oxidase) - 
                uptake_rate(glial_transporters)

NMDA co-agonist эффект:
NMDA_current = g_NMDA × (V - E_NMDA) × Mg_block × 
               glycine_site_occupancy(D_serine, glycine)
               
Пластичность-зависимая модуляция:
LTP_probability = sigmoid(Ca_influx × D_serine_availability × 
                 temporal_precision × postsynaptic_depolarization)
```

#### 3.2.2 Пространственно-временная динамика глиотрансмиссии

**Диффузионно-деградационная модель:**
```
∂C/∂t = D∇²C - λC + S(r,t) - U(r,t)
где:
C(r,t) - концентрация глиотрансмиттера
D - коэффициент диффузии (зависит от молекулы и среды)
λ - константа деградации
S(r,t) - источники (астроцитарный выброс)
U(r,t) - поглощение (рецепторы, транспортеры)
```

**Критические радиусы действия:**
```
R_critical = √(D/λ) - характерный радиус диффузии

Для разных глиотрансмиттеров:
R_ATP ≈ 20-50 мкм (быстрая деградация)
R_glutamate ≈ 10-30 мкм (активный захват)
R_D-serine ≈ 100-200 мкм (медленная деградация)
```

**Временная динамика модуляции:**
```
Быстрая фаза (100-500 мс): прямая рецепторная активация
Средняя фаза (1-10 с): метаботропные каскады
Медленная фаза (минуты): транскрипционные эффекты
```

#### 3.2.3 Сетевые эффекты глиотрансмиссии

**Глиальные волны и их синаптические эффекты:**
```
Wave_propagation = Ca²⁺_wave_speed × gliotransmitter_release_efficiency × 
                  synaptic_modulation_strength × wave_coherence

Пространственная координация:
Coordination_index = ∑ᵢⱼ cross_correlation(synapse_i_modulation, 
                                         synapse_j_modulation) × 
                    spatial_weight(dist(i,j))
```

**Метапластические эффекты:**
```
Sliding_threshold = baseline_threshold + 
                   ∫₀ᵗ gliotransmitter_history(s) × decay_kernel(t-s) ds

Homeostatic_scaling = target_activity / actual_activity × 
                     glial_scaling_factor × metabolic_constraint
```

### 3.3 Связь метаболических процессов с информационной обработкой

#### 3.3.1 Глюкозо-лактатный челнок как информационный канал

**Энергетическая сигнализация:**
```
Energy_signal(t) = (glucose_uptake(t) - baseline_glucose) / baseline_glucose

Информационное содержание:
I_metabolic = -log₂(P(energy_state)) × uncertainty_reduction_factor

Связь с нейронной активностью:
Neural_activity_prediction = f(lactate_gradient, oxygen_consumption, 
                              ATP/ADP_ratio, metabolic_history)
```

**Астроцитарная метаболическая память:**
```
Metabolic_memory(t) = ∫₀ᵗ energy_demand(s) × forgetting_kernel(t-s) × 
                     adaptation_weight(s) ds

Предиктивная метаболическая подготовка:
Preparatory_metabolism = learned_patterns × circadian_modulation × 
                        cognitive_demand_forecast × stress_indicators
```

#### 3.3.2 ATP как внутриклеточный информационный код

**Энергетические микродомены:**
```
[ATP]_microdomain(r,t) = production_rate(mitochondria, r) - 
                        consumption_rate(neural_processes, r, t) + 
                        diffusion_flux(r) + astrocyte_supply(r,t)

Информационная ёмкость:
Channel_capacity = log₂(1 + SNR_ATP) × bandwidth_metabolic

Кодирование активности:
Activity_encoding = quantize([ATP]_local, resolution_bits) × 
                   temporal_precision × spatial_precision
```

**Митохондриальная сигнализация:**
```
Mitochondrial_signal = Ca²⁺_mitochondrial × membrane_potential_change × 
                      ROS_signaling × protein_synthesis_rate

Информационный поток:
I_mitochondrial→nuclear = transcription_factor_activation × 
                         gene_expression_changes × protein_translation_rate
```

#### 3.3.3 Метаболическая пластичность и обучение

**Энергетическая эффективность синапсов:**
```
Efficiency_synapse = information_transmitted / energy_consumed

Оптимизация:
Optimal_strength = argmax(Efficiency_synapse) subject to:
- metabolic_constraints
- information_fidelity_requirements  
- structural_stability_limits
```

**Метаболически-зависимая долгосрочная потенциация:**
```
LTP_metabolic = LTP_baseline × metabolic_support_factor

где:
metabolic_support_factor = (ATP_availability × protein_synthesis_capacity × 
                          glucose_supply × oxygen_availability) / 
                          energy_demand_baseline

Критерий устойчивости:
LTP_persistence = f(metabolic_stability, protein_turnover_rate, 
                   structural_maintenance_energy)
```

**Циркадная модуляция когнитивных процессов:**
```
Cognitive_performance(t) = baseline_performance × 
                          circadian_metabolic_factor(t) × 
                          sleep_pressure_factor(t) × 
                          nutritional_state_factor(t)

где:
circadian_metabolic_factor(t) = 1 + A × cos(2π(t-φ)/24h + phase_shift)
```

---

## 4. Система биомаркеров НАГА-RPEA

### 4.1 Комплексная метрика оценки сознания

#### 4.1.1 Интегральный индекс ИНАГА-RPEA

**Математически корректная формула:**
```
ИНАГА-RPEA(t) = ∫[t-T to t] W(s) × ∏ᵢ₌₁⁹ [Cᵢ(s)]^αᵢ × Quality_factor(s) ds / ∫[t-T to t] W(s) ds

где:
- T = адаптивное временное окно интеграции
- W(s) = временная весовая функция
- Cᵢ(s) = нормализованные компоненты [0,1]  
- αᵢ = показатели важности, ∑αᵢ = 1
- Quality_factor(s) = коэффициент качества данных
```

**Адаптивные веса компонентов:**
```
Веса αᵢ адаптируются в зависимости от контекста:

α_neural = 0.15 + 0.05 × task_complexity
α_astrocytic = 0.12 + 0.08 × memory_demand  
α_ephaptic = 0.10 + 0.05 × attention_load
α_predictive = 0.18 + 0.07 × uncertainty_level
α_recurrent = 0.13 + 0.02 × narrative_coherence
α_attractor = 0.08 + 0.03 × emotional_stability
α_temporal = 0.12 + 0.04 × temporal_binding_demand
α_metabolic = 0.07 + 0.08 × energy_constraint
α_tripartite = 0.05 + 0.10 × integration_requirement
```

#### 4.1.2 Многомерная структура оценки

**Иерархическая декомпозиция:**
```
ИНАГА-RPEA = Primary_consciousness × Meta_consciousness × 
             Narrative_consciousness × Embodied_consciousness

где каждая компонента:
Primary_consciousness = f(IGI, ECI, ASI, TCI)
Meta_consciousness = f(RRI, PPI, self_model_coherence)
Narrative_consciousness = f(temporal_binding, semantic_integration, autobiographical_continuity)
Embodied_consciousness = f(GAI, MCI, TSI, sensorimotor_integration)
```

**Динамическая калибровка:**
```
Calibration_factor(individual) = normalize_by_baseline(individual) × 
                               age_correction × pathology_correction × 
                               measurement_quality × temporal_stability
```

#### 4.1.3 Статистическая валидация и нормы

**Популяционные нормы:**
```
Здоровые взрослые: ИНАГА-RPEA = 0.72 ± 0.08
Дети (7-12 лет): ИНАГА-RPEA = 0.65 ± 0.12
Пожилые (>65 лет): ИНАГА-RPEA = 0.68 ± 0.10
Сон (REM): ИНАГА-RPEA = 0.45 ± 0.15
Сон (NREM): ИНАГА-RPEA = 0.25 ± 0.10
Общая анестезия: ИНАГА-RPEA = 0.15 ± 0.08
```

**Критические пороги и переходы:**
```
Критический порог сознания: ИНАГА-RPEA_critical = 0.35 ± 0.05
Порог высшего сознания: ИНАГА-RPEA_higher = 0.80 ± 0.03
Порог патологии: ИНАГА-RPEA_pathological < 0.30
```

### 4.2 Специализированные астроцитарные биомаркеры

#### 4.2.1 Кальциевая динамика как биомаркер

**Индекс кальциевой когерентности (ИКК):**
```
ИКК = ∑ᵢ,ⱼ Phase_locking_value(Ca_i(t), Ca_j(t)) × 
      Spatial_weight(dist(i,j)) × Functional_connectivity(i,j)

Нормализация: ИКК ∈ [0,1]
```

**Метрика кальциевых волн (МКВ):**
```
МКВ = Wave_initiation_frequency × Wave_propagation_speed × 
      Wave_spatial_extent × Wave_amplitude_consistency × 
      Wave_direction_coherence

Интерпретация:
МКВ < 0.3: Нарушенная глиальная связность
0.3 ≤ МКВ < 0.7: Нормальная глиальная активность  
МКВ ≥ 0.7: Гипер-активация глиальной сети
```

#### 4.2.2 Глиотрансмиттерные биомаркеры

**Индекс глиотрансмиттерного баланса (ИГТБ):**
```
ИГТБ = weighted_balance([ATP], [Glutamate], [D-serine], [GABA], [Lactate])

где:
weighted_balance = ∑ᵢ wᵢ × ([Transmitter_i] - baseline_i) / baseline_i
веса wᵢ определяются функциональной важностью
```

**Коэффициент астроцитарной реактивности (КАР):**
```
КАР = Response_amplitude / Stimulus_strength × 
      Response_speed × Recovery_completeness × 
      Adaptation_efficiency

Диапазоны:
КАР < 0.4: Гипореактивность (депрессия, астроцитарная дисфункция)
0.4 ≤ КАР ≤ 0.8: Нормальная реактивность
КАР > 0.8: Гипер-реактивность (воспаление, стресс)
```

#### 4.2.3 Метаболические астроцитарные маркеры

**Индекс лактатного челнока (ИЛЧ):**
```
ИЛЧ = (Lactate_production_astrocytes / Glucose_uptake_astrocytes) × 
      (Lactate_uptake_neurons / Neural_activity_level) × 
      Transport_efficiency × Metabolic_coupling_strength
```

**Коэффициент энергетической поддержки (КЭП):**
```
КЭП = Available_energy / Energy_demand × Supply_stability × 
      Efficiency_factor × Reserve_capacity

Критические значения:
КЭП < 0.6: Энергетический дефицит
0.6 ≤ КЭП < 0.9: Адекватная поддержка
КЭП ≥ 0.9: Избыточные резервы
```

### 4.3 Динамические и сетевые биомаркеры

#### 4.3.1 Многомасштабная временная интеграция

**Индекс мультитемпоральной когерентности (ИМТК):**
```
ИМТК = ∫₀^∞ W(τ) × |Coherence(signal(t), signal(t-τ))| × 
       Scale_weight(τ) dτ / ∫₀^∞ W(τ) dτ

где:
- W(τ) = exp(-τ/τ₀) - экспоненциальная весовая функция
- Scale_weight(τ) учитывает важность разных временных масштабов
- Интеграция по всем релевантным временным задержкам
```

**Временные масштабы и их интерпретация:**
```
Миллисекундный (1-10 мс): Синаптическая синхронизация
Сотни мс (100-500 мс): Корковая интеграция  
Секундный (1-10 с): Рабочая память и внимание
Минутный (>1 мин): Долгосрочная память и планирование
```

#### 4.3.2 Сетевые топологические маркеры

**Индекс трипартитной связности (ИТС):**
```
ИТС = (Neural_connectivity × Astrocytic_connectivity × Ephaptic_connectivity)^(1/3) × 
      Cross_network_coupling × Topological_efficiency

Компоненты:
Neural_connectivity = Small_world_index_neural × Clustering_coefficient
Astrocytic_connectivity = Giant_component_size × Path_length_efficiency  
Ephaptic_connectivity = Field_correlation_strength × Spatial_extent
```

**Коэффициент динамической реконфигурации (КДР):**
```
КДР = Network_flexibility × Reconfiguration_speed × 
      Stability_after_change × Adaptation_optimality

где:
Network_flexibility = ∑ᵢ |connections_i(t+1) - connections_i(t)| / total_connections
```

#### 4.3.3 Предиктивные и адаптивные маркеры

**Индекс предиктивной точности НАГА (ИППН):**
```
ИППН = ∑_levels w_level × Prediction_accuracy_level × 
       Confidence_calibration × Uncertainty_quantification

Уровни предсказания:
Уровень 1: Сенсорные предсказания (мс)
Уровень 2: Перцептивные предсказания (100 мс) 
Уровень 3: Когнитивные предсказания (секунды)
Уровень 4: Поведенческие предсказания (минуты)
```

**Коэффициент метапластической адаптации (КМА):**
```
КМА = Learning_rate_adaptation × Forgetting_optimization × 
      Interference_resistance × Transfer_efficiency

Интерпретация:
КМА < 0.4: Ригидность обучения
0.4 ≤ КМА < 0.8: Оптимальная адаптивность
КМА ≥ 0.8: Избыточная пластичность (нестабильность)
```

#### 4.3.4 Интегрированная панель биомаркеров

**Диагностическая панель НАГА-RPEA:**
```
Основные маркеры (всегда измерять):
- ИНАГА-RPEA (общий индекс)
- ИКК (астроцитарная активность)
- ИМТК (временная интеграция)
- ИТС (сетевая связность)

Специализированные маркеры (по показаниям):
- ИГТБ (нейрохимические нарушения)
- КАР (реактивность системы) 
- ИЛЧ (метаболические проблемы)
- ИППН (когнитивные функции)

Исследовательские маркеры:
- КДР (сетевая динамика)
- КМА (пластичность)
- КЭП (энергетика)
```

**Алгоритм интерпретации:**
```
1. Оценить общий уровень сознания (ИНАГА-RPEA)
2. Идентифицировать лимитирующие компоненты (минимальные Cᵢ)
3. Проанализировать специфические нарушения (целевые маркеры)
4. Определить механизмы патологии (паттерн-анализ)
5. Спрогнозировать динамику и ответ на терапию
```

---


## Источники

### Основные теоретические работы
1. Tononi, G. (2008). An information integration theory of consciousness. *BMC Neuroscience*, 9, 1-22.
2. Friston, K. (2010). The free-energy principle: a unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.
3. Chalmers, D. J. (2010). *The Character of Consciousness*. Oxford University Press.
4. Dehaene, S. (2014). *Consciousness and the Brain: Deciphering How the Brain Codes Our Thoughts*. Viking.

### Астроцитарные механизмы и глиотрансмиссия
5. Araque, A., Carmignoto, G., Haydon, P. G., et al. (2014). Gliotransmitters travel in time and space. *Neuron*, 81(4), 728-739.
6. Bazargani, N., & Attwell, D. (2016). Astrocyte calcium signaling: the third wave. *Nature Neuroscience*, 19(2), 182-189.
7. Perea, G., Navarrete, M., & Araque, A. (2009). Tripartite synapses: astrocytes process and control synaptic information. *Trends in Neurosciences*, 32(8), 421-431.
8. Santello, M., Toni, N., & Volterra, A. (2019). Astrocyte function from information processing to cognition and cognitive impairment. *Nature Neuroscience*, 22(2), 154-166.

### Метаболические аспекты
9. Pellerin, L., & Magistretti, P. J. (2012). Sweet sixteen for ANLS. *Journal of Cerebral Blood Flow & Metabolism*, 32(7), 1249-1255.
10. Barros, L. F., & Weber, B. (2018). CrossTalk proposal: an important astrocyte-to-neuron lactate shuttle couples neuronal activity to glucose utilisation in the brain. *The Journal of Physiology*, 596(3), 347-350.
11. Dienel, G. A. (2019). Brain glucose metabolism: integration of energetics with function. *Physiological Reviews*, 99(1), 949-1045.

### Эфаптические взаимодействия
12. Anastassiou, C. A., Perin, R., Markram, H., & Koch, C. (2011). Ephaptic coupling of cortical neurons. *Nature Neuroscience*, 14(2), 217-223.
13. Bokil, H., Laaris, N., Blinder, K., et al. (2001). Ephaptic interactions in the mammalian olfactory system. *Journal of Neuroscience*, 21(20), 7771-7781.
14. Weiss, S. A., & Faber, D. S. (2010). Field effects in the CNS play functional roles. *Frontiers in Neural Circuits*, 4, 15.

### Предиктивное кодирование и байесовский мозг
15. Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*, 36(3), 181-204.
16. Hohwy, J. (2013). *The Predictive Mind: Cognitive Science and Philosophy of Mind*. Oxford University Press.
17. Rao, R. P., & Ballard, D. H. (1999). Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79-87.

### Рекуррентные сети и аттракторы
18. Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 79(8), 2554-2558.
19. Wang, X. J. (2001). Synaptic reverberation underlying mnemonic persistent activity. *Trends in Neurosciences*, 24(8), 455-463.
20. Deco, G., & Hugues, E. (2012). Neural network mechanisms underlying stimulus driven variability reduction. *PLoS Computational Biology*, 8(3), e1002395.

### Интегрированная информация и сложность
21. Oizumi, M., Albantakis, L., & Tononi, G. (2014). From the phenomenology to the mechanisms of consciousness: integrated information theory 3.0. *PLoS Computational Biology*, 10(5), e1003588.
22. Barrett, A. B., & Seth, A. K. (2011). Practical measures of integrated information for time-series data. *PLoS Computational Biology*, 7(1), e1001052.
23. Casali, A. G., Gosseries, O., Rosanova, M., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*, 5(198), 198ra105.

### Темпоральная интеграция и связывание
24. Singer, W. (1999). Neuronal synchrony: a versatile code for the definition of relations? *Neuron*, 24(1), 49-65.
25. Varela, F., Lachaux, J. P., Rodriguez, E., & Martinerie, J. (2001). The brainweb: phase synchronization and large-scale integration. *Nature Reviews Neuroscience*, 2(4), 229-239.
26. Buzsáki, G., & Draguhn, A. (2004). Neuronal oscillations in cortical networks. *Science*, 304(5679), 1926-1929.

### Биомаркеры сознания
27. Laureys, S., & Schiff, N. D. (2012). Coma and consciousness: paradigms (re) framed by neuroimaging. *NeuroImage*, 61(2), 478-491.
28. Sitt, J. D., King, J. R., El Karoui, I., et al. (2017). Large scale screening of neural signatures of consciousness in patients in a vegetative or minimally conscious state. *Brain*, 140(9), 2258-2270.
29. Engemann, D. A., Raimondo, F., King, J. R., et al. (2018). Robust EEG-based cross-site and cross-protocol classification of states of consciousness. *Brain*, 141(11), 3179-3192.

### Методологические аспекты
30. Rubinov, M., & Sporns, O. (2010). Complex network measures of brain connectivity: uses and interpretations. *NeuroImage*, 52(3), 1059-1069.
31. Bullmore, E., & Sporns, O. (2009). Complex brain networks: graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*, 10(3), 186-198.
32. Deco, G., Tononi, G., Boly, M., & Kringelbach, M. L. (2015). Rethinking segregation and integration: contributions of whole-brain modelling. *Nature Reviews Neuroscience*, 16(7), 430-439.


---

Оглавление:


- [Теория Динамической Интеграции Сознания](/Theory-Of-Dynamic-Integration-Of-Consciousness/README.md)

- [Модель НАГА-RPEA: Нейро-Астроцитарный Глобальный Аттрактор с Рекуррентным Предиктивным Кодированием, Эфаптической связью и Астроцитарной Модуляцией](/Theory-Of-Dynamic-Integration-Of-Consciousness/Dynamic-Global-Attractor/NAGA-RPEA.md)

