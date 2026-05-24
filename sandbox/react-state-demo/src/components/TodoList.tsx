import { useState } from 'react';

// TODO の1件分を表す型
type Todo = {
  id: number;
  text: string;
  done: boolean;
};

// useState で「TODO一覧の配列」と「入力中テキスト」の2つの状態を管理する
export function TodoList() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [draft, setDraft] = useState<string>('');

  const addTodo = () => {
    const text = draft.trim();
    if (text === '') return;

    const newTodo: Todo = {
      id: Date.now(),
      text,
      done: false,
    };
    setTodos((prev) => [...prev, newTodo]);
    setDraft('');
  };

  const toggleTodo = (id: number) => {
    setTodos((prev) =>
      prev.map((todo) =>
        todo.id === id ? { ...todo, done: !todo.done } : todo
      )
    );
  };

  const removeTodo = (id: number) => {
    setTodos((prev) => prev.filter((todo) => todo.id !== id));
  };

  return (
    <div className="todo-list">
      <h2>TODO リスト（残り {todos.filter((t) => !t.done).length} 件）</h2>

      <div className="todo-input">
        <input
          type="text"
          value={draft}
          placeholder="やることを入力"
          onChange={(e) => setDraft(e.target.value)}
        />
        <button onClick={addTodo}>追加</button>
      </div>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id} style={{ textDecoration: todo.done ? 'line-through' : 'none' }}>
            <label>
              <input
                type="checkbox"
                checked={todo.done}
                onChange={() => toggleTodo(todo.id)}
              />
              {todo.text}
            </label>
            <button onClick={() => removeTodo(todo.id)}>削除</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
