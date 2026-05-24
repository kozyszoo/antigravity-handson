import { useState } from 'react';

// シンプルな数値カウンタコンポーネント
// useState で「現在の数値」と「ステップ幅」の2つの状態を管理する
export function Counter() {
  const [count, setCount] = useState<number>(0);
  const [step, setStep] = useState<number>(1);

  const increment = () => setCount((prev) => prev + step);
  const decrement = () => setCount((prev) => prev - step);
  const reset = () => setCount(0);

  return (
    <div className="counter">
      <h2>カウンタ: {count}</h2>

      <label>
        ステップ幅:
        <input
          type="number"
          value={step}
          onChange={(e) => setStep(Number(e.target.value))}
        />
      </label>

      <div className="counter-buttons">
        <button onClick={decrement}>−</button>
        <button onClick={reset}>リセット</button>
        <button onClick={increment}>＋</button>
      </div>
    </div>
  );
}
