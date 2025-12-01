'use client';

import { useState } from 'react';
import ChatWidget from '../components/ChatWidget';

export default function MathWebsite() {
  const [calcInput, setCalcInput] = useState('');
  const [calcResult, setCalcResult] = useState('');
  const [selectedFormula, setSelectedFormula] = useState<string | null>(null);

  const handleCalculate = () => {
    try {
      // Simple calculator evaluation (in production, use a proper parser)
      const result = Function(`"use strict"; return (${calcInput})`)();
      setCalcResult(result.toString());
    } catch (error) {
      setCalcResult('Error: Invalid expression');
    }
  };

  const formulas = [
    {
      name: 'Pythagorean Theorem',
      formula: 'a² + b² = c²',
      description: 'For a right triangle with sides a, b, and hypotenuse c'
    },
    {
      name: 'Quadratic Formula',
      formula: 'x = (-b ± √(b² - 4ac)) / 2a',
      description: 'Solutions to ax² + bx + c = 0'
    },
    {
      name: 'Area of Circle',
      formula: 'A = πr²',
      description: 'Area of a circle with radius r'
    },
    {
      name: 'Volume of Sphere',
      formula: 'V = (4/3)πr³',
      description: 'Volume of a sphere with radius r'
    },
    {
      name: 'Euler\'s Identity',
      formula: 'e^(iπ) + 1 = 0',
      description: 'Beautiful relationship between fundamental constants'
    },
    {
      name: 'Sum of Arithmetic Series',
      formula: 'S = n(a₁ + aₙ)/2',
      description: 'Sum of n terms in an arithmetic sequence'
    }
  ];

  const mathFacts = [
    'π (pi) is approximately 3.14159...',
    'The number 0 was invented in India around 500 AD',
    'A googol is 10¹⁰⁰ (1 followed by 100 zeros)',
    'The Fibonacci sequence appears in nature (sunflowers, pinecones)',
    'There are 43,252,003,274,489,856,000 possible Rubik\'s cube combinations',
    'Zero is the only number that cannot be represented in Roman numerals'
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        {/* Header */}
        <header className="text-center mb-12">
          <h1 className="text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 mb-4">
            Math Explorer
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Discover the beauty of mathematics
          </p>
        </header>

        {/* Calculator Section */}
        <section className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 mb-8">
          <h2 className="text-3xl font-semibold mb-6 text-gray-800 dark:text-white">
            Calculator
          </h2>
          <div className="space-y-4">
            <div className="flex gap-2">
              <input
                type="text"
                value={calcInput}
                onChange={(e) => setCalcInput(e.target.value)}
                placeholder="Enter expression (e.g., 2 + 2 * 3)"
                className="flex-1 px-4 py-3 border-2 border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:border-blue-500 dark:bg-gray-700 dark:text-white text-lg"
                onKeyPress={(e) => e.key === 'Enter' && handleCalculate()}
              />
              <button
                onClick={handleCalculate}
                className="px-8 py-3 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-lg font-semibold hover:from-blue-600 hover:to-purple-600 transition-all transform hover:scale-105 shadow-lg"
              >
                Calculate
              </button>
            </div>
            {calcResult && (
              <div className="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg border-2 border-green-200 dark:border-green-800">
                <p className="text-2xl font-bold text-green-700 dark:text-green-400">
                  Result: {calcResult}
                </p>
              </div>
            )}
            <div className="grid grid-cols-4 gap-2 mt-4">
              {['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+'].map((btn) => (
                <button
                  key={btn}
                  onClick={() => {
                    if (btn === '=') {
                      handleCalculate();
                    } else {
                      setCalcInput(prev => prev + btn);
                    }
                  }}
                  className="p-4 bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg font-semibold text-lg transition-colors"
                >
                  {btn}
                </button>
              ))}
            </div>
          </div>
        </section>

        {/* Math Formulas Section */}
        <section className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 mb-8">
          <h2 className="text-3xl font-semibold mb-6 text-gray-800 dark:text-white">
            Famous Math Formulas
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {formulas.map((formula, index) => (
              <div
                key={index}
                onClick={() => setSelectedFormula(selectedFormula === formula.name ? null : formula.name)}
                className={`p-6 rounded-xl border-2 cursor-pointer transition-all transform hover:scale-105 ${
                  selectedFormula === formula.name
                    ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20 shadow-lg'
                    : 'border-gray-200 dark:border-gray-700 hover:border-blue-300 dark:hover:border-blue-700'
                }`}
              >
                <h3 className="text-xl font-bold mb-2 text-gray-800 dark:text-white">
                  {formula.name}
                </h3>
                <p className="text-2xl font-mono mb-2 text-blue-600 dark:text-blue-400">
                  {formula.formula}
                </p>
                {selectedFormula === formula.name && (
                  <p className="text-sm text-gray-600 dark:text-gray-300 mt-2">
                    {formula.description}
                  </p>
                )}
              </div>
            ))}
          </div>
        </section>

        {/* Math Facts Section */}
        <section className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 mb-8">
          <h2 className="text-3xl font-semibold mb-6 text-gray-800 dark:text-white">
            Interesting Math Facts
          </h2>
          <div className="grid md:grid-cols-2 gap-4">
            {mathFacts.map((fact, index) => (
              <div
                key={index}
                className="p-4 bg-gradient-to-r from-purple-50 to-blue-50 dark:from-purple-900/20 dark:to-blue-900/20 rounded-lg border-l-4 border-purple-500"
              >
                <p className="text-gray-700 dark:text-gray-300">{fact}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Visual Math Concepts */}
        <section className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8">
          <h2 className="text-3xl font-semibold mb-6 text-gray-800 dark:text-white">
            Visual Math Concepts
          </h2>
          <div className="grid md:grid-cols-3 gap-6">
            {/* Circle */}
            <div className="text-center p-6 bg-gradient-to-br from-pink-50 to-red-50 dark:from-pink-900/20 dark:to-red-900/20 rounded-xl">
              <div className="w-32 h-32 mx-auto mb-4 rounded-full border-4 border-blue-500 flex items-center justify-center">
                <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">r</span>
              </div>
              <p className="font-semibold text-gray-800 dark:text-white">Circle</p>
              <p className="text-sm text-gray-600 dark:text-gray-400">A = πr²</p>
            </div>

            {/* Square */}
            <div className="text-center p-6 bg-gradient-to-br from-green-50 to-emerald-50 dark:from-green-900/20 dark:to-emerald-900/20 rounded-xl">
              <div className="w-32 h-32 mx-auto mb-4 border-4 border-green-500 flex items-center justify-center">
                <span className="text-2xl font-bold text-green-600 dark:text-green-400">s</span>
              </div>
              <p className="font-semibold text-gray-800 dark:text-white">Square</p>
              <p className="text-sm text-gray-600 dark:text-gray-400">A = s²</p>
            </div>

            {/* Triangle */}
            <div className="text-center p-6 bg-gradient-to-br from-yellow-50 to-orange-50 dark:from-yellow-900/20 dark:to-orange-900/20 rounded-xl">
              <div className="w-32 h-32 mx-auto mb-4">
                <svg viewBox="0 0 100 100" className="w-full h-full">
                  <polygon
                    points="50,10 90,90 10,90"
                    fill="none"
                    stroke="rgb(234, 179, 8)"
                    strokeWidth="4"
                  />
                  <text x="50" y="60" textAnchor="middle" className="text-2xl font-bold fill-yellow-600 dark:fill-yellow-400">
                    h
                  </text>
                </svg>
              </div>
              <p className="font-semibold text-gray-800 dark:text-white">Triangle</p>
              <p className="text-sm text-gray-600 dark:text-gray-400">A = ½bh</p>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="text-center mt-12 text-gray-600 dark:text-gray-400">
          <p>Math Explorer - Where numbers meet beauty</p>
        </footer>
      </div>

      {/* Chat Widget */}
      <ChatWidget />
    </div>
  );
}
