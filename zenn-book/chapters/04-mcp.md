---
title: "Step 4: MCP（Model Context Protocol）接続"
---

## このステップのゴール

MCP を使って、エージェントを外部ツールやデータソースにつなぐ方法を学びましょう。

## MCP とは

MCP（Model Context Protocol）は、AIエージェントと外部システムを安全に接続するためのオープン標準です。MCP を使うと、エージェントができることが大幅に広がります。

たとえば、ブラウザを操作して Web リサーチをしたり、GitHub の Issue を作成したり、データベースに直接クエリを投げたりできるようになります。

:::message
公式ドキュメントはこちら: https://antigravity.google/docs/mcp
:::

<!-- TODO: 図7 - MCP のアーキテクチャ図（エージェント ↔ MCPサーバー ↔ 外部サービス）を挿入 -->

## MCP の3つの柱

| 機能 | 説明 | 例 |
|:---|:---|:---|
| **Context Resources** | AI がリアルタイムデータを読み取る | SQL スキーマ、ビルドログ |
| **Custom Tools** | AI がアクションを実行する | GitHub Issue 作成、Notion 検索 |
| **MCP Store** | GUI で MCP を追加・管理できる | ワンクリックで有効化 |

Google Search、GitHub、Slack、Jira、PostgreSQL、Notion など多数のサービスに対応しています。

## ハンズオン: MCP を設定しよう

### Step 1: MCP Store を開く

Agent パネルの右上にある三点メニュー（`...`）から **MCP Store** を選択します。

MCP Store は GUI で MCP サーバーの追加・管理ができるビルトイン機能です。

<!-- TODO: 図8 - MCP Store の画面キャプチャを挿入 -->

### Step 2: 利用可能な MCP を確認する

MCP Store を開くと、以下のようなサーバーが一覧表示されます。

| MCP サーバー | 用途 | 設定方法 |
|:---|:---|:---|
| `filesystem` | ローカルファイルの読み書き | デフォルト有効 |
| `chrome-devtools` | Chrome ブラウザ操作・DevTools | MCP Store から追加 |
| `playwright` | ブラウザ自動化・テスト | MCP Store から追加 |
| `context7` | 最新ライブラリドキュメント参照 | MCP Store から追加 |
| `serena` | 大規模コードベース解析 | MCP Store から追加 |
| `postgres` | PostgreSQL 接続 | MCP Store から追加 |
| `github` | GitHub API 連携 | MCP Store から追加 |

### Step 3: MCP サーバーを追加する

**MCP Store から追加する場合（推奨）**: 使いたいサーバーを選んで Install ボタンを押すだけです。

**手動で設定する場合**: 設定ファイルに直接書くこともできます。

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-playwright"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp"]
    }
  }
}
```

## やってみよう: MCP を使ったリサーチ

MCP（Browser）を有効にした状態で、以下を試してみましょう。

### Web 検索

```
Google で「Antigravity IDE 2026」を検索して、
トップ3件の記事タイトルを教えて。
```

エージェントが Browser MCP を使って Google 検索を実行し、結果を報告してくれます。

### ドキュメント参照

```
Context7 MCP を使って、React の useEffect フックの
最新の使い方を調べて教えて。
```

context7 MCP が最新のドキュメントからコード例を取得し、日本語で解説してくれます。

## おすすめ MCP 構成

| MCP | 主な用途 | おすすめ度 |
|:---|:---|:---:|
| **playwright** | E2E テスト、Web スクレイピング | ⭐⭐⭐ |
| **context7** | 最新ライブラリドキュメント参照 | ⭐⭐⭐ |
| **chrome-devtools** | ブラウザ開発者ツール操作 | ⭐⭐ |
| **serena** | 大規模コードベース解析 | ⭐⭐ |
| **github** | PR 作成、Issue 管理 | ⭐⭐ |

## セキュリティ上の注意

:::message alert
MCP は強力な権限を持ちます。信頼できるサーバーだけを有効にしてください。API キーは環境変数で管理し、設定ファイルへの直書きは避けましょう。ネットワークアクセスが必要な MCP はファイアウォール設定も確認してください。
:::
