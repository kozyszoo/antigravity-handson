# Google Antigravity 解説 & ハンズオンガイド

本資料は、次世代AIエージェント統合開発環境「Google Antigravity」の基礎から実践的な活用方法までを、1.5〜2時間程度で習得するためのガイドです。

## ⏱️ 所要時間・全体像
- **所要時間**: 1.5 - 2時間
- **ゴール**: Google Antigravityの基本機能を理解し、Vibe Coding（AIとの直感的な協働）を通じてWebアプリケーションを作成・デプロイする体験をする。

## 📂 ハンズオン資料

| No | フォルダ | 内容 | 所要時間 |
|:---:|:---|:---|:---:|
| 01 | [01_setup](./handson/01_setup/README.md) | 環境セットアップ | 15分 |
| 02 | [02_gemini_md](./handson/02_gemini_md/README.md) | GEMINI.md 設定 | 15分 |
| 03 | [03_mcp](./handson/03_mcp/README.md) | MCP 接続 | 20分 |
| 04 | [04_skills](./handson/04_skills/README.md) | Agent Skills 作成 | 20分 |
| 05 | [05_vibe_coding](./handson/05_vibe_coding/README.md) | Vibe Coding デモ | 30分 |

---

## 1. What is Google Antigravity? (Google Antigravityとは)

**Google Antigravity** は、2025年11月18日にGoogleが発表した、「AIエージェントファースト」の統合開発環境（IDE）です。従来の「コード補完」ツール（Copilot等）とは一線を画し、AIエージェントが開発者のパートナーとして自律的にタスクを計画・実行・検証するアーキテクチャを採用しています。

### 主な特徴
- **Agent-First Architecture**: AIが単なるツールではなく、タスクを実行する主体として振る舞います。
- **Dual View System**: コードを書く「Editor View」と、エージェントを指揮する「Manager View」の2つの視点を提供。
- **Artifacts**: エージェントの作業結果（タスクリスト、計画書、画像、ブラウザ操作ログ）を成果物として可視化・保存。
- **Multi-Model Support**: Gemini 3 Proをはじめ、Claude、そして画像生成特化の **Nano Banana** など、適材適所でモデルを使い分け可能。

## 2. Introduction to Google Antigravity (導入)

Antigravityの哲学は「重力（＝開発の面倒な作業）からの解放」です。環境構築、ボイラープレートの記述、単調なリファクタリング、ドキュメント作成...これらをAIエージェントに任せることで、開発者は「何を創るか（What）」に集中できます（これが **Vibe Coding** の真髄です）。

---

## 3. How to install (インストール方法)

1.  **公式サイトへのアクセス**: [build.google.com/antigravity](https://build.google.com/antigravity) (架空のURL) へアクセス。
2.  **ダウンロード**: OS（macOS, Windows, Linux）に合わせたインストーラーをダウンロード。
3.  **インストール & ログイン**: アプリケーションを起動し、Googleアカウントでログインします。

## 4. Pricing Plans (料金プラン)

| プラン | 価格 | 内容 |
| :--- | :--- | :--- |
| **Free / Individual** | 無料 | Gemini 3 Pro (Rate Limitあり), Nano Banana (月50枚), ローカルMCP接続 |
| **Pro** | $19/月 | Gemini 3 Pro (優先アクセス), Claude Sonnet 4.5, Nano Banana (無制限), クラウドMCP |
| **Team / Enterprise** | お問い合わせ | チーム共有Artifacts, Enterpriseセキュリティ, カスタムモデル |

※ 開発者は基本的に **Freeプラン** でも十分な機能を利用可能です。

---

## 5. How to use Google Antigravity (基本的な使い方)

### Manager View (司令塔)
- **チャットインターフェース**: 自然言語でタスクを依頼。「〇〇の機能を作って」「このバグを直して」
- **エージェント管理**: 複数のエージェント（Coder, Designer, Researcher）が並行して動く様子を監視。

### Editor View (作業場)
- **VS Code互換**: 慣れ親しんだエージェント統合型エディタ。
- **インライン編集**: `Cmd+K` (または `Ctrl+K`) でコード上の即時修正を依頼。

---

## 6. Select model tips (モデル選択のヒント)

タスクに応じて最適なモデルを選択することが、Antigravity活用の鍵です。

| モデル名 | 得意なタスク | 選択推奨シーン |
| :--- | :--- | :--- |
| **Gemini 3 Pro** | **総合力・論理的思考** | メインの開発、複雑なロジック実装、全体設計 |
| **Claude Sonnet 4.5** | **文脈理解・自然な文章** | ドキュメント作成、要件定義、微妙なニュアンスの理解 |
| **Nano Banana (Gemini 2.5 Image)** | **画像生成・UIデザイン** | アイコン作成、OGP画像、LPのヒーローイメージ生成 |
| **Gemini 2.5 Computer Use** | **ブラウザ操作** | Web検索、E2Eテスト、Webサイトからの情報収集 |

---

## 7. GEMINI.md / AGENTS.md (設定ファイルについて)

Antigravityのエージェントは、プロジェクトごとのルールに従います。これを定義するのが設定ファイルです。

### GEMINI.md (または AI_INSTRUCTIONS.md)
プロジェクトルートやサブフォルダに配置することで、エージェントに「このプロジェクトの文脈」や「守るべきルール」を教えます。

**おすすめ設定項目 example:**
- **プロジェクト概要**: 何を作るプロジェクトか。
- **技術スタック**: React, TailwindCSS, TypeScriptなど。
- **コーディング規約**: ファイル命名規則、ディレクトリ構成ルール。
- **振る舞い**: "日本語で回答して" "コードブロックのみ出力して" など。

**Hands-on:** 作業フォルダに `AI_INSTRUCTIONS.md` を作成し、「常に日本語で応答すること」「コードには必ずコメントを入れること」を記述してみましょう。

---

## 8. Connect to MCP (MCPの接続)

**MCP (Model Context Protocol)** は、AIエージェントを外部ツールやデータ（GitHub, Google Drive, Slack, ローカルDBなど）に接続するための標準規格です。

### 設定方法
1.  Antigravityの設定画面 > `MCP Servers` へ移動。
2.  接続したいサーバー（例: `filesystem`, `postgres`, `github`）を選択。
3.  必要なAPIキーなどを入力して有効化。

**おすすめMCP:**
- **Browser (Puppeteer/Playwright)**: ブラウザ操作用。Webリサーチやテストに必須。
- **Filesystem**: ローカルファイルの読み書き（デフォルトで有効）。
- **PostgreSQL**: DBの中身を直接参照しながらSQLを書かせる場合に便利。

---

## 9. Agent Skills (エージェントスキル)

**Skills** は、エージェントに特定の「能力」や「手順」をパッケージとして追加する機能です。`.agent/skills` ディレクトリで管理します。

### Skillsの作り方
1.  `.agent/skills/<skill-name>/` フォルダを作成。
2.  `SKILL.md` にYAMLヘッダーとMarkdownで手順を記述。

**Hands-on Example (`.agent/skills/review-code/SKILL.md`):**
```markdown
---
name: code-review
description: コードの品質レビューを行う
---
# コードレビュー手順
1. 指定されたファイルを読み込む
2. セキュリティ脆弱性がないか確認する
3. 変数名が適切かチェックする
...
```
これを作っておくと、「@code-review して」と頼むだけで定義された手順を実行してくれます。

---

## 10. Agent Manager & Multi Agent Workflow

**Agent Manager** は、複数のエージェントを指揮し、複雑なタスクを並列処理します。

### 活用例
- **Workflow**: 「新機能開発」という指示に対し、
    1. **Planner Agent**: 要件定義とタスク分解
    2. **Coder Agent**: コード実装
    3. **Designer Agent (Nano Banana)**: UIパーツ作成
    4. **Reviewer Agent**: コードレビュー
    これらを連携して自動実行させることができます。

---

## 11. Nano Banana Integration (活用ガイド)

**Nano Banana** (Gemini 2.5 Image) は、Antigravityに深く統合された画像生成/編集モデルです。デザイン素材をエンジニアが即座に用意できる点が革新的です。

### 使い方
- チャットで「このヘッダーに合う背景画像を生成して（Nano Banana）」と依頼。
- 生成された画像は直接 `public/images/` などの指定フォルダに保存・配置されます。
- **Hands-on**: 後述のデモで、Webサイトのメインビジュアルを生成します。

---

## 12. 🚀 Vibe Coding Demo with Google Antigravity

ここからは実際にAntigravityを使って、簡単なLP（ランディングページ）を作成します。

### Step 1: プロジェクト作成
Antigravityにて:
> 「Vite + Reactで、モダンで美しい『AI Coffee Shop』のランディングページを作って。TailwindCSSを使って。」

(Antigravityが `npx create-vite...` などを実行し、雛形を作成)

### Step 2: キャッチコピーと構成（Gemini 3 Pro）
> 「未来的で落ち着くコーヒーショップのキャッチコピーと、LPのセクション構成を考えて（Gemini 3 Pro）」

### Step 3: ビジュアル生成（Nano Banana）
> 「『近未来的なカフェの店内、ネオンライトと植物が調和している、4K、リアル』な画像を生成して。ファイル名は `hero-bg.webp` で `public` フォルダに保存して。（Nano Banana）」

### Step 4: 実装 & プレビュー
> 「生成した画像を背景に使って、Heroセクションを実装して。文字は白で読みやすく、グラスモーフィズムなデザインで。」

### Step 5: デプロイ（Vercel etc.）
> 「これで完成。ビルドしてデプロイの準備をして。」

---

**さあ、はじめましょう！ Antigravityで、重力から解放された開発体験を。**
