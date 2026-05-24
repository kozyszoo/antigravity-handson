import { useState } from 'react';

type Theme = 'light' | 'dark';

// useState で「現在のテーマ（light / dark）」を管理する
// ボタンクリックでテーマを切り替え、画面の背景色と文字色を変える
export function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>('light');

  const toggleTheme = () => {
    setTheme((prev) => (prev === 'light' ? 'dark' : 'light'));
  };

  const containerStyle: React.CSSProperties = {
    background: theme === 'light' ? '#ffffff' : '#1a1a2e',
    color: theme === 'light' ? '#1a1a2e' : '#e8e8e8',
    padding: '24px',
    borderRadius: '8px',
    transition: 'background 0.2s, color 0.2s',
  };

  return (
    <div style={containerStyle}>
      <h2>現在のテーマ: {theme === 'light' ? '☀️ Light' : '🌙 Dark'}</h2>
      <button onClick={toggleTheme}>
        {theme === 'light' ? 'Dark に切替' : 'Light に切替'}
      </button>
    </div>
  );
}
