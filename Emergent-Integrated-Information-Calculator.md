# Калькулятор эмерджентной интегрированной информации (Φₑ) на Python 3

---

## Описание

- Цель: Вычислить значение Φₑ посредством численного интегрирования.

- Методы:

  - Определение функций I₍интеграции₎(t) и R₍рекуррентности₎(t).

  - Использование алгоритма численного интегрирования (например, метода Симпсона).

---

### Реализация на Python 3

[python-fiddle](https://python-fiddle.com/saved/yrfYVLTktpxDd6WiexGF)


```python3
import numpy as np
from scipy.integrate import simps
import matplotlib.pyplot as plt

# Определяем временной интервал
t_start = 0
t_end = 10  # t1 по вашему выбору
num_points = 1000  # Количество точек для дискретизации

t = np.linspace(t_start, t_end, num_points)

# Функция степени интеграции информации I(t)
def I_integration(t):
    # Пример функции, замените на вашу модель
    # Например, экспоненциальное нарастание
    return np.exp(-0.1 * t) * np.sin(t)

# Функция степени рекуррентности R(t)
def R_recurrent(t):
    # Пример функции, замените на вашу модель
    # Например, косинусная функция
    return 1 + 0.5 * np.cos(0.5 * t)

# Вычисляем значения функций
I_values = I_integration(t)
R_values = R_recurrent(t)

# Вычисляем подынтегральную функцию
integrand = I_values * R_values

# Численное интегрирование с помощью метода Симпсона
Phi_e = simps(integrand, t)

print(f"Значение эмерджентной интегрированной информации (Φₑ): {Phi_e}")

# Построение графиков функций
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, I_values, label='I₍интеграции₎(t)', color='blue')
plt.title('Степень интеграции информации I(t)')
plt.xlabel('Время t')
plt.ylabel('I(t)')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, R_values, label='R₍рекуррентности₎(t)', color='green')
plt.title('Степень рекуррентности R(t)')
plt.xlabel('Время t')
plt.ylabel('R(t)')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, integrand, label='I(t) * R(t)', color='red')
plt.title('Подынтегральная функция I(t) * R(t)')
plt.xlabel('Время t')
plt.ylabel('I(t) * R(t)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
```

---

### Объяснение кода

1. Импорт необходимых библиотек:

   - numpy для работы с массивами и численными операциями.

   - scipy.integrate.simps для численного интегрирования методом Симпсона.

   - matplotlib.pyplot для визуализации функций.

2. Установка временного интервала:

   - Время начинается с t_start = 0 и заканчивается в t_end = 10 (вы можете изменить на ваше значение t₁).

   - num_points определяет количество точек для дискретизации временного интервала.

3. Определение функций I_integration(t) и R_recurrent(t):

   - Важно: В данном коде использованы примерные функции. Вам необходимо заменить их на реальные модели, соответствующие вашей системе.

   - I_integration(t): Пример функции экспоненциального затухания с синусоидальной модуляцией.

   - R_recurrent(t): Пример косинусоидальной функции, моделирующей степень рекуррентности.

4. Вычисление значений функций и подынтегральной функции:

   - Вычисляем значения I_values и R_values для каждого момента времени t.

   - Подынтегральная функция integrand получена как произведение I_values на R_values.

5. Численное интегрирование:

   - Используем метод Симпсона (simps) для численного интегрирования подынтегральной функции по времени t.

   - Результат интегрирования сохраняется в переменной Phi_e.

6. Вывод результата:

   - Печатаем значение Φₑ.

7. Визуализация:

   - Строим графики:

     - Степень интеграции информации I(t).

     - Степень рекуррентности R(t).

     - Подынтегральная функция I(t) * R(t).

---

### Пример вывода


`Значение эмерджентной интегрированной информации (Φₑ): 1.98971027488856`


![Графики функций](/Emergent-Integrated-Information-Calculator.png "Графики функций")


---

### Как адаптировать код под ваши нужды

- Измените функции I_integration(t) и R_recurrent(t):
- Вставьте реальные математические модели для ваших функций.

  - Если ваши функции зависят от дополнительных параметров или данных, включите их в определение функций.

- Настройте временной интервал:

  - Измените t_start и t_end в соответствии с интервалом времени, для которого вы хотите провести расчёты.

  - Увеличьте num_points для большей точности интегрирования.

- Выберите метод интегрирования:

  - В данном коде используется метод Симпсона (simps), который хорошо подходит для плавных функций.

  - Вы можете использовать другие методы из scipy.integrate, такие как quad для более точного интегрирования или trapz для метода трапеций.

---

### Дополнительные замечания

- Проверка единиц измерения:

  - Убедитесь, что функции I_integration(t) и R_recurrent(t) имеют совместимые единицы измерения для корректного вычисления произведения и интегрирования.

- Обработка особых случаев:

  - Если функции имеют особенности (например, точки разрыва или сингулярности), рассмотрите возможность разбиения интервала интегрирования или использования специальных методов интегрирования.

- Оптимизация производительности:

  - Для очень больших объёмов данных или сложных функций рассмотрите использование более эффективных алгоритмов или библиотек, поддерживающих параллельные вычисления.

---

### Заключение

Этот калькулятор предоставляет базовую структуру для вычисления эмерджентной интегрированной информации Φₑ. Путём замены примерных функций на реальные модели, вы сможете адаптировать код для анализа конкретных систем в рамках Теории Эмергентной Интеграции и Рекуррентного Отображения (ЭИРО).

Если у вас возникнут вопросы или потребуется помощь в адаптации кода, пожалуйста, не стесняйтесь обращаться!

---

Оглавление: 

- [Полный список алгоритмов для создания Python кода для расчёта представленных формул и теорий](/calc.md)
- [Теория Эмергентной Интеграции и Рекуррентного Отображения](/README.md)
