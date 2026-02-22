---
title: "まとめと次のステップ"
---

## ハンズオンで学んだこと

全6ステップを通じて、以下の内容を体験しました。

| ステップ | 学んだこと |
|:---:|:---|
| 1 | Antigravity の基本操作、2つの View、モデル選択 |
| 2 | GEMINI.md によるプロジェクトルールの定義、Workflows |
| 3 | 自然言語での HTML 生成、Nano Banana による画像生成 |
| 4 | MCP による外部ツール接続、Web リサーチの自動化 |
| 5 | Agent Skills の作成と呼び出し、Rules / Workflows との使い分け |
| 6 | MCP + Skills を組み合わせた本格的な Vibe Coding |

## Antigravity の全体像

ここまでの内容を振り返ると、Antigravity が提供する仕組みは大きく3層に分かれます。

**基盤**: Editor View と Agent Manager の Dual View、マルチモデル対応
**カスタマイズ**: Rules（GEMINI.md）、Workflows、Agent Skills
**拡張**: MCP による外部ツール接続

<!-- TODO: 図11 - Antigravity の3層構造図を挿入 -->

これらを組み合わせることで「何を作りたいか」を自然言語で伝えるだけで、リサーチから実装、レビュー、デプロイ準備まで一貫して進められるようになります。

## 料金プラン

| プラン | 料金 | 主な内容 |
|:---:|:---:|:---|
| Free | 無料 | Gemini 3 Pro（制限あり）、Nano Banana（月50枚）、ローカル MCP |
| Pro | $19/月 | Gemini 3 Pro（優先）、Claude Sonnet 4.5、Nano Banana（無制限）、クラウド MCP |
| Enterprise | 要相談 | チーム共有 Artifacts、Enterprise セキュリティ、カスタムモデル |

Free プランでも十分に活用できます。

## 次のステップ

### 自分のプロジェクトで使ってみる

まずは既存のプロジェクトに GEMINI.md を置いてみてください。応答言語とコーディング規約を指定するだけでも、エージェントの振る舞いが変わります。

### カスタム Skills を増やす

よく繰り返すタスクがあれば、それを SKILL.md に落とし込んでみましょう。コードレビュー、テスト生成、ドキュメント作成など、自分のワークフローに合った Skills を作ると開発がさらに加速します。

### MCP を拡張する

Slack、GitHub、Jira など、普段使っているツールに MCP で接続すると、エージェントの活動範囲がさらに広がります。

## 参考リンク

- [Antigravity 公式サイト](https://antigravity.google)
- [公式ドキュメント](https://antigravity.google/docs/get-started)
- [MCP ドキュメント](https://antigravity.google/docs/mcp)
- [Skills ドキュメント](https://antigravity.google/docs/skills)
- [MCP プロトコル仕様](https://modelcontextprotocol.io/)
- [Agent Skills 標準](https://agentskills.io)

## ハンズオン用リポジトリ

本書のソースコードとハンズオン資料はGitHubで公開しています。

```bash
git clone https://github.com/YOUR_USERNAME/antigravity_handson.git
```

Issue やプルリクエストも歓迎です。
