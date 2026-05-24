# react-state-demo

`serena` MCP の「コードベース解析」デモ用サンプルです。
`useState` の使い方が異なる3つのコンポーネントを意図的に並べています。

## 構成

| コンポーネント | useState で管理する状態 | パターン |
|---|---|---|
| `Counter.tsx` | `count: number`, `step: number` | プリミティブ値（数値）の更新 |
| `TodoList.tsx` | `todos: Todo[]`, `draft: string` | 配列の追加・更新・削除 |
| `ThemeToggle.tsx` | `theme: 'light' \| 'dark'` | リテラル型の切り替え |

## 使い方（Antigravity IDE）

Step 3-1 の手順で `serena` MCP を有効化したあと、Agent Manager で以下のように依頼すると、各ファイルが意味的に解析されます。

```text
serena を使って、このプロジェクト内で useState フックを使っているコンポーネントを全て見つけて、
それぞれどのような状態を管理しているか分析して教えて。
```

## 注意

- このフォルダはあくまで「serena に食わせる解析対象サンプル」です。
- 起動・ビルドは不要なので、`npm install` も行っていません（実行したい場合は Vite 等を別途追加してください）。
