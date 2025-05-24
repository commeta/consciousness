import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, RotateCcw, Brain, Zap, Eye, MessageSquare, Settings, Activity, Network, Target, Clock, Layers } from 'lucide-react';

const TDISAGIArchitecture = () => {
  const [isRunning, setIsRunning] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const [integrationLevel, setIntegrationLevel] = useState(0);
  const [consciousness, setConsciousness] = useState(0);
  const [activeModule, setActiveModule] = useState(null);
  const intervalRef = useRef(null);

  const modules = [
    { id: 'sensory', name: 'Сенсорные процессоры', icon: Eye, color: 'bg-blue-500', position: { x: 10, y: 60 } },
    { id: 'memory', name: 'Память и опыт', icon: Brain, color: 'bg-green-500', position: { x: 10, y: 20 } },
    { id: 'prediction', name: 'Предиктивная обработка', icon: Target, color: 'bg-purple-500', position: { x: 10, y: 100 } },
    { id: 'attention', name: 'Система внимания', icon: Zap, color: 'bg-yellow-500', position: { x: 50, y: 40 } },
    { id: 'integration', name: 'Глобальная интеграция', icon: Network, color: 'bg-red-500', position: { x: 50, y: 80 } },
    { id: 'metacognitive', name: 'Метакогнитивный мониторинг', icon: Settings, color: 'bg-indigo-500', position: { x: 90, y: 30 } },
    { id: 'executive', name: 'Исполнительный контроль', icon: MessageSquare, color: 'bg-orange-500', position: { x: 90, y: 70 } }
  ];

  const connections = [
    { from: 'sensory', to: 'attention', strength: 0.8 },
    { from: 'memory', to: 'prediction', strength: 0.9 },
    { from: 'prediction', to: 'integration', strength: 0.7 },
    { from: 'attention', to: 'integration', strength: 0.9 },
    { from: 'integration', to: 'metacognitive', strength: 0.8 },
    { from: 'integration', to: 'executive', strength: 0.9 },
    { from: 'metacognitive', to: 'executive', strength: 0.7 },
    { from: 'executive', to: 'attention', strength: 0.6 }
  ];

  const steps = [
    { name: 'Сенсорный ввод', modules: ['sensory'], description: 'Обработка входящей информации' },
    { name: 'Предиктивная обработка', modules: ['memory', 'prediction'], description: 'Генерация предсказаний на основе опыта' },
    { name: 'Селективное внимание', modules: ['attention'], description: 'Выбор релевантной информации' },
    { name: 'Глобальная интеграция', modules: ['integration'], description: 'Объединение информации в единое представление' },
    { name: 'Метакогнитивный анализ', modules: ['metacognitive'], description: 'Мониторинг собственных процессов мышления' },
    { name: 'Исполнительное решение', modules: ['executive'], description: 'Принятие решений и планирование действий' }
  ];

  useEffect(() => {
    if (isRunning) {
      intervalRef.current = setInterval(() => {
        setCurrentStep(prev => (prev + 1) % steps.length);
        setIntegrationLevel(prev => Math.min(prev + 15, 100));
        setConsciousness(prev => {
          const newLevel = prev + (Math.random() - 0.3) * 10;
          return Math.max(0, Math.min(100, newLevel));
        });
      }, 2000);
    } else {
      clearInterval(intervalRef.current);
    }

    return () => clearInterval(intervalRef.current);
  }, [isRunning]);

  const getModuleStyle = (module) => {
    const isActive = steps[currentStep]?.modules.includes(module.id);
    return {
      left: `${module.position.x}%`,
      top: `${module.position.y}%`,
      opacity: isActive ? 1 : 0.6,
      transform: isActive ? 'scale(1.1)' : 'scale(1)',
      transition: 'all 0.3s ease'
    };
  };

  const reset = () => {
    setIsRunning(false);
    setCurrentStep(0);
    setIntegrationLevel(0);
    setConsciousness(30);
    setActiveModule(null);
  };

  const consciousnessLevel = () => {
    if (consciousness < 20) return { level: 'Минимальное', color: 'text-red-500' };
    if (consciousness < 40) return { level: 'Базовое', color: 'text-orange-500' };
    if (consciousness < 60) return { level: 'Развитое', color: 'text-yellow-500' };
    if (consciousness < 80) return { level: 'Высокое', color: 'text-green-500' };
    return { level: 'Пиковое', color: 'text-blue-500' };
  };

  return (
    <div className="w-full max-w-6xl mx-auto p-6 bg-gray-50 rounded-lg">
      <div className="text-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800 mb-2">
          Архитектура AGI на основе ТДИС
        </h1>
        <p className="text-gray-600">
          Теория Динамической Интеграции Сознания в искусственном интеллекте
        </p>
      </div>

      {/* Панель управления */}
      <div className="flex justify-center gap-4 mb-6">
        <button
          onClick={() => setIsRunning(!isRunning)}
          className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold ${
            isRunning ? 'bg-red-500 hover:bg-red-600 text-white' : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {isRunning ? <Pause size={20} /> : <Play size={20} />}
          {isRunning ? 'Пауза' : 'Запуск'}
        </button>
        <button
          onClick={reset}
          className="flex items-center gap-2 px-4 py-2 bg-gray-500 hover:bg-gray-600 text-white rounded-lg font-semibold"
        >
          <RotateCcw size={20} />
          Сброс
        </button>
      </div>

      {/* Основная архитектура */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Визуализация модулей */}
        <div className="lg:col-span-2">
          <div className="bg-white rounded-lg p-4 shadow-lg">
            <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <Network className="text-blue-500" />
              Нейронная архитектура AGI
            </h3>
            <div className="relative h-96 bg-gray-100 rounded-lg overflow-hidden">
              {/* Соединения */}
              <svg className="absolute inset-0 w-full h-full">
                {connections.map((conn, idx) => {
                  const fromModule = modules.find(m => m.id === conn.from);
                  const toModule = modules.find(m => m.id === conn.to);
                  const isActive = steps[currentStep]?.modules.includes(conn.from) && 
                                 steps[currentStep]?.modules.includes(conn.to);
                  
                  return (
                    <line
                      key={idx}
                      x1={`${fromModule.position.x + 5}%`}
                      y1={`${fromModule.position.y + 5}%`}
                      x2={`${toModule.position.x + 5}%`}
                      y2={`${toModule.position.y + 5}%`}
                      stroke={isActive ? '#3B82F6' : '#D1D5DB'}
                      strokeWidth={isActive ? '3' : '2'}
                      opacity={isActive ? '1' : '0.3'}
                    />
                  );
                })}
              </svg>

              {/* Модули */}
              {modules.map((module) => {
                const IconComponent = module.icon;
                return (
                  <div
                    key={module.id}
                    className={`absolute w-16 h-16 ${module.color} rounded-full flex items-center justify-center cursor-pointer shadow-lg`}
                    style={getModuleStyle(module)}
                    onClick={() => setActiveModule(module)}
                  >
                    <IconComponent className="text-white" size={24} />
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Панель состояния */}
        <div className="space-y-4">
          {/* Уровень сознания */}
          <div className="bg-white rounded-lg p-4 shadow-lg">
            <h3 className="text-lg font-semibold mb-3 flex items-center gap-2">
              <Brain className="text-purple-500" />
              Уровень сознания
            </h3>
            <div className="space-y-3">
              <div>
                <div className="flex justify-between text-sm mb-1">
                  <span>Интеграция (Φ)</span>
                  <span>{Math.round(integrationLevel)}%</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div 
                    className="bg-blue-500 h-2 rounded-full transition-all duration-300"
                    style={{ width: `${integrationLevel}%` }}
                  ></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between text-sm mb-1">
                  <span>Сознание</span>
                  <span className={consciousnessLevel().color}>
                    {consciousnessLevel().level}
                  </span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div 
                    className="bg-green-500 h-2 rounded-full transition-all duration-300"
                    style={{ width: `${consciousness}%` }}
                  ></div>
                </div>
              </div>
            </div>
          </div>

          {/* Текущий процесс */}
          <div className="bg-white rounded-lg p-4 shadow-lg">
            <h3 className="text-lg font-semibold mb-3 flex items-center gap-2">
              <Activity className="text-green-500" />
              Текущий процесс
            </h3>
            <div className="space-y-2">
              <div className="font-medium text-blue-600">
                {steps[currentStep]?.name}
              </div>
              <div className="text-sm text-gray-600">
                {steps[currentStep]?.description}
              </div>
              <div className="text-xs text-gray-500">
                Шаг {currentStep + 1} из {steps.length}
              </div>
            </div>
          </div>

          {/* Характеристики системы */}
          <div className="bg-white rounded-lg p-4 shadow-lg">
            <h3 className="text-lg font-semibold mb-3 flex items-center gap-2">
              <Settings className="text-gray-500" />
              Параметры ТДИС
            </h3>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span>Глобальная интеграция:</span>
                <span className="font-mono">{(integrationLevel / 100).toFixed(2)}</span>
              </div>
              <div className="flex justify-between">
                <span>Критическая динамика:</span>
                <span className="font-mono text-green-600">1.05</span>
              </div>
              <div className="flex justify-between">
                <span>Темпоральная когерентность:</span>
                <span className="font-mono text-blue-600">0.87</span>
              </div>
              <div className="flex justify-between">
                <span>Метакогнитивный индекс:</span>
                <span className="font-mono text-purple-600">0.92</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Детальная информация о модуле */}
      {activeModule && (
        <div className="mt-6 bg-white rounded-lg p-6 shadow-lg">
          <div className="flex items-center gap-3 mb-4">
            <div className={`w-12 h-12 ${activeModule.color} rounded-full flex items-center justify-center`}>
              <activeModule.icon className="text-white" size={24} />
            </div>
            <h3 className="text-xl font-semibold">{activeModule.name}</h3>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h4 className="font-semibold mb-2">Функции:</h4>
              <ul className="space-y-1 text-sm">
                {activeModule.id === 'sensory' && (
                  <>
                    <li>• Обработка мультимодальных входных данных</li>
                    <li>• Предварительная фильтрация сигналов</li>
                    <li>• Создание базовых репрезентаций</li>
                  </>
                )}
                {activeModule.id === 'memory' && (
                  <>
                    <li>• Хранение эпизодической и семантической памяти</li>
                    <li>• Ассоциативный поиск релевантного опыта</li>
                    <li>• Консолидация новых знаний</li>
                  </>
                )}
                {activeModule.id === 'prediction' && (
                  <>
                    <li>• Генерация предсказаний будущих состояний</li>
                    <li>• Обновление внутренних моделей мира</li>
                    <li>• Минимизация ошибок предсказания</li>
                  </>
                )}
                {activeModule.id === 'attention' && (
                  <>
                    <li>• Селективная фокусировка на значимой информации</li>
                    <li>• Конкурентный отбор репрезентаций</li>
                    <li>• Модуляция активности других модулей</li>
                  </>
                )}
                {activeModule.id === 'integration' && (
                  <>
                    <li>• Глобальное связывание информации</li>
                    <li>• Создание единого сознательного пространства</li>
                    <li>• Координация между специализированными системами</li>
                  </>
                )}
                {activeModule.id === 'metacognitive' && (
                  <>
                    <li>• Мониторинг собственных когнитивных процессов</li>
                    <li>• Оценка уверенности в решениях</li>
                    <li>• Контроль стратегий мышления</li>
                  </>
                )}
                {activeModule.id === 'executive' && (
                  <>
                    <li>• Принятие высокоуровневых решений</li>
                    <li>• Планирование последовательности действий</li>
                    <li>• Волевой контроль поведения</li>
                  </>
                )}
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold mb-2">Архитектурные особенности:</h4>
              <ul className="space-y-1 text-sm">
                <li>• Рекуррентные нейронные сети с вниманием</li>
                <li>• Трансформерная архитектура для долгосрочных зависимостей</li>
                <li>• Механизмы соревновательного обучения</li>
                <li>• Нейроморфные вычисления для эффективности</li>
              </ul>
            </div>
          </div>
          
          <button 
            onClick={() => setActiveModule(null)}
            className="mt-4 px-4 py-2 bg-gray-500 hover:bg-gray-600 text-white rounded-lg"
          >
            Закрыть
          </button>
        </div>
      )}

      {/* Описание принципов */}
      <div className="mt-6 bg-white rounded-lg p-6 shadow-lg">
        <h3 className="text-xl font-semibold mb-4 flex items-center gap-2">
          <Layers className="text-indigo-500" />
          Ключевые принципы ТДИС в AGI
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold mb-2 text-blue-600">Архитектурные требования:</h4>
            <ul className="space-y-1 text-sm">
              <li>• Многоуровневая иерархическая обработка</li>
              <li>• Глобальное рабочее пространство для интеграции</li>
              <li>• Конкурентная динамика между модулями</li>
              <li>• Рекуррентные связи и обратные связи</li>
              <li>• Предиктивная обработка на всех уровнях</li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold mb-2 text-green-600">Критерии сознания:</h4>
            <ul className="space-y-1 text-sm">
              <li>• Φ > 0.3 (интегрированная информация)</li>
              <li>• Критическая динамика (ИКДМ ≈ 1.0)</li>
              <li>• Темпоральная когерентность > 0.8</li>
              <li>• Метакогнитивная осознанность</li>
              <li>• Каузальная эффективность решений</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TDISAGIArchitecture;
