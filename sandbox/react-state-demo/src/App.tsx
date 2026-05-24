import { Counter } from './components/Counter';
import { TodoList } from './components/TodoList';
import { ThemeToggle } from './components/ThemeToggle';

// 3つの useState サンプルコンポーネントを並べるルートコンポーネント
// serena MCP の解析対象として、useState の使い方が異なる3パターンを揃えている
export function App() {
  return (
    <main style={{ maxWidth: 720, margin: '0 auto', padding: 24 }}>
      <h1>React useState デモ</h1>
      <section style={{ marginBottom: 32 }}>
        <Counter />
      </section>
      <section style={{ marginBottom: 32 }}>
        <TodoList />
      </section>
      <section>
        <ThemeToggle />
      </section>
    </main>
  );
}
