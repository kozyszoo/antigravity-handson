# 🚀 Google Antigravity ハンズオン

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Marp](https://img.shields.io/badge/Made%20with-Marp-orange)](https://marp.app/)

次世代AIエージェント統合開発環境「**Google Antigravity**」の基礎から実践的な活用方法までを、1.5〜2時間程度で習得するためのハンズオン資料です。

## 📚 目次

- [概要](#概要)
- [クイックスタート](#クイックスタート)
- [ハンズオン構成](#ハンズオン構成)
- [プレゼンテーション資料](#プレゼンテーション資料)
- [前提条件](#前提条件)
- [セットアップ](#セットアップ)
- [使い方](#使い方)
- [トラブルシューティング](#トラブルシューティング)
- [貢献](#貢献)
- [ライセンス](#ライセンス)

## 🎯 概要

**Google Antigravity**は、2025年11月18日にGoogleが発表した「AIエージェントファースト」の統合開発環境（IDE）です。

### 主な特徴

- 🤖 **Agent-First Architecture**: AIが自律的にタスクを計画・実行・検証
- 👁️ **Dual View System**: Manager ViewとEditor Viewの2つの視点
- 🎨 **Nano Banana統合**: AI画像生成でデザイン素材を即座に作成
- 🔌 **MCP対応**: 外部ツールとの柔軟な連携
- 🧠 **Multi-Model Support**: Gemini、Claude、Nano Bananaを適材適所で使い分け

### 学習目標

このハンズオンを通じて、以下のスキルを習得できます:

- ✅ Antigravityの基本操作
- ✅ GEMINI.mdによるプロジェクト設定
- ✅ MCPサーバーの接続と活用
- ✅ Agent Skillsの作成
- ✅ Vibe Codingによる高速開発

## ⚡ クイックスタート

```bash
# 1. リポジトリをクローン
git clone https://github.com/YOUR_USERNAME/antigravity_handson.git
cd antigravity_handson

# 2. ハンズオン資料を開く
open docs/index.html

# 3. ハンズオンを開始
# docs/index.html または zenn-book/chapters/ から順番に進めてください
```

## 📂 リポジトリ構成

```
antigravity_handson/
├── .agent/                    # AIエージェント設定
│   └── agents/               # カスタムエージェント定義
│       ├── copy-designer.md
│       ├── code-researcher.md
│       ├── insight-analyst.md
│       └── ...
├── .claude/                   # Claude設定
│   ├── settings.local.json   # ローカル設定
│   └── skills/               # プロジェクト固有のスキル
│       ├── database/
│       ├── git-workflow/
│       ├── ui-verify/
│       └── ...
├── docs/                      # ドキュメント・プレゼンテーション資料
│   ├── index.html            # ハンズオンWebページ
│   ├── live-coding-script.md # ライブコーディング台本
│   └── img/                  # 画像・図表
│       ├── fig1.png
│       ├── fig2.png
│       ├── slide-*.png       # スライド画像
│       └── ...
├── zenn-book/                 # Zenn本コンテンツ
│   ├── chapters/             # 各章のMarkdown
│   │   ├── 00-introduction.md
│   │   ├── 01-1-setup.md
│   │   ├── 01-2-gemini-md.md
│   │   ├── 02-vibe-coding-basic.md
│   │   ├── 03-1-mcp.md
│   │   ├── 03-2-skills.md
│   │   ├── 04-vibe-coding-advanced.md
│   │   ├── 05-ai-dlc.md
│   │   └── 08-summary.md
│   ├── figures/              # 図表（Draw.io形式）
│   │   ├── fig-01-antigravity-overview.drawio
│   │   ├── fig-02-dual-view.drawio
│   │   └── ...
│   ├── figure-creation-prompts.md  # 図表作成プロンプト
│   └── figure-prompts.yaml         # 図表生成設定
├── LICENSE
└── README.md
```

## 📚 コンテンツ構成

### 🕐 当日のタイムライン（2026.03.07）

| 時間 | セクション | 内容 |
|:---|:---|:---|
| 19:00〜19:15 | **イントロ** | Vibe Codingとは？開発のパラダイムシフト |
| 19:15〜19:30 | **Antigravityの核心技術** | Agent-First / Dual View / Multi-Model |
| 19:30〜20:00 | **Step 1** | 環境構築 + GEMINI.md設定（30分） |
| 20:00〜20:20 | **Step 2** | Vibe Coding 基礎編（自己紹介ページ + Nano Banana） |
| 20:20〜20:40 | **Step 3** | MCP接続 + Browser Subagent & Skills |
| 20:40〜21:00 | **Step 4** | Vibe Coding 発展編（AI Coffee Shop LP） |
| 21:00〜21:10 | **Step 5** | まとめ：AI-DLCとハッカソン戦略 |

### 📖 Zenn本チャプター

| No | ファイル | 内容 | 時間帯 | 難易度 |
|:---:|:---|:---|:---:|:---:|
| **00** | [はじめに](./zenn-book/chapters/00-introduction.md) | 本書の目的と対象読者 | - | - |
| **01-1** | [環境セットアップ](./zenn-book/chapters/01-1-setup.md) | 環境構築・基本画面確認 | 19:30〜 | ⭐ |
| **01-2** | [GEMINI.md 設定](./zenn-book/chapters/01-2-gemini-md.md) | GEMINI.md 設定 | 19:45〜 | ⭐⭐ |
| **02** | [Vibe Coding 基礎編](./zenn-book/chapters/02-vibe-coding-basic.md) | 🎨 **自己紹介ページ + Nano Banana** | 20:00〜 | ⭐⭐ |
| **03-1** | [MCP 接続](./zenn-book/chapters/03-1-mcp.md) | MCP接続・Browser Subagent | 20:20〜 | ⭐⭐ |
| **03-2** | [Agent Skills 作成](./zenn-book/chapters/03-2-skills.md) | Agent Skills 作成 | 20:30〜 | ⭐⭐⭐ |
| **04** | [Vibe Coding 発展編](./zenn-book/chapters/04-vibe-coding-advanced.md) | 🚀 **AI Coffee Shop LP 構築** | 20:40〜 | ⭐⭐⭐ |
| **05** | [AI-DLC戦略](./zenn-book/chapters/05-ai-dlc.md) | 🏅 **ハッカソン攻略：AI-DLC** | 21:00〜 | ⭐⭐⭐ |
| **06** | [活用Tips集](./zenn-book/chapters/06-tips.md) | 実践的な活用方法とリソース | - | ⭐⭐ |
| **08** | [まとめ](./zenn-book/chapters/08-summary.md) | 本書のまとめと次のステップ | - | - |

**合計所要時間**: 約100分（ハンズオン部分のみ）

### 🎯 学習フロー

```
【Step 1】基礎の確立（19:30〜20:00）
  環境セットアップ → GEMINI.md設定
      ↓
【Step 2】Vibe Coding を最速体験（20:00〜20:20）
  自己紹介ページ作成 + Nano Banana 画像生成
      ↓
【Step 3】エージェントを拡張（20:20〜20:40）
  MCP接続 → Browser Subagent → Agent Skills
      ↓
【Step 4】総合演習（20:40〜21:00）
  AI Coffee Shop LP（リサーチ→実装→デプロイ準備）
      ↓
【Step 5】実践知識（21:00〜21:10）
  AI-DLC × ハッカソン最強戦略
```

### なぜこの順番？

- **Step 2 で早期にVibe Codingを体験** → モチベーション維持
- **Step 3 で機能を拡張** → できることが増える
- **Step 4 で総合演習** → 学んだ機能を組み合わせる
- **Step 5 で実践参考** → ハッカソンで即使える戦略を知る



## 📊 ハンズオン資料

### Webページ版（推奨）

ハンズオンの詳細な手順とスライドがWebページ形式で提供されています。

```bash
# ブラウザで開く
open docs/index.html
```

**含まれる内容**:
- ハンズオンの全手順（Step 1〜5）
- スライド画像による視覚的な説明
- ライブコーディングのデモ手順

### Zenn本版

各章が独立したMarkdownファイルとして `zenn-book/chapters/` に格納されています。

```bash
# 各章を読む
cat zenn-book/chapters/01-1-setup.md
cat zenn-book/chapters/02-vibe-coding-basic.md
# ...
```

### ライブコーディング台本

イベント登壇時のライブコーディング用台本です。

```bash
cat docs/live-coding-script.md
```



## 🔧 前提条件

### 必須

- **Google Antigravity**: [公式サイト](https://antigravity.google)からインストール
- **Googleアカウント**: Antigravityへのログインに必要
- **インターネット接続**: AIモデルとの通信に必要

### 推奨

- **Node.js**: v18以上（Vibe Codingデモで使用）
- **Git**: バージョン管理
- **Visual Studio Code**: コード編集（Antigravity以外で確認する場合）

### オプション

- **任意のWebブラウザ**: ハンズオン資料（docs/index.html）の閲覧用

## 🛠️ セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/YOUR_USERNAME/antigravity_handson.git
cd antigravity_handson
```

### 2. Antigravityのインストール

1. [公式サイト](https://antigravity.google)にアクセス
2. お使いのOS（macOS / Windows / Linux）に合わせたインストーラーをダウンロード
3. インストーラーを実行
4. Antigravityを起動し、Googleアカウントでログイン

### 3. プロジェクトを開く

Antigravityで、クローンしたディレクトリを開きます:

```
File > Open Folder > antigravity_handson を選択
```

### 4. GEMINI.mdの確認

プロジェクトルートに `.agent/GEMINI.md` が自動的に認識されます。

## 📖 使い方

### ハンズオンの進め方

1. **Webページを開く**: `docs/index.html` をブラウザで開く
2. **順番に進める**: Step 1から順番に進めることを推奨
3. **Zenn本も参照**: `zenn-book/chapters/` に詳細な解説あり
4. **実際に手を動かす**: コードを書いて、動かして、理解を深める
5. **質問・疑問をメモ**: 後で調べたり、コミュニティで質問

### 各ステップの概要

#### Step 1-1: 環境セットアップ

Antigravityの基本操作を学びます。

```bash
# Zenn本チャプターを参照
cat zenn-book/chapters/01-1-setup.md
```

**学習内容**:
- Antigravityのインストール
- プロジェクトの作成
- Manager ViewとEditor Viewの使い分け

#### Step 1-2: GEMINI.md 設定

プロジェクト固有のルールをAIに教えます。

```bash
cat zenn-book/chapters/01-2-gemini-md.md
```

**学習内容**:
- GEMINI.mdの役割
- プロジェクト設定の記述方法
- コーディング規約の定義

#### Step 2: Vibe Coding 基礎編

MCP/Skillsなしで、シンプルなVibe Codingを体験します。

```bash
cat zenn-book/chapters/02-vibe-coding-basic.md
```

**学習内容**:
- 自然言語でのWebページ作成
- Nano Bananaでの画像生成
- デザインカスタマイズ

#### Step 3-1: MCP 接続

外部ツールとの連携を学びます。

```bash
cat zenn-book/chapters/03-1-mcp.md
```

**学習内容**:
- MCPの概念とMCP Store
- ブラウザMCPの接続
- Context7によるドキュメント参照

#### Step 3-2: Agent Skills 作成

エージェントに新しい能力を追加します。

```bash
cat zenn-book/chapters/03-2-skills.md
```

**学習内容**:
- Skillsの仕組み（agentskills.io 標準）
- SKILL.mdの作成
- Rules / Workflows / Skills の使い分け

#### Step 4: Vibe Coding 発展編

MCP + Skills を活用した本格的なVibe Codingを実践します。

```bash
cat zenn-book/chapters/04-vibe-coding-advanced.md
```

**学習内容**:
- MCPを使ったWebリサーチ
- 複数のNano Banana画像の統合
- 高速プロトタイピング

#### Step 5: AI-DLC戦略

ハッカソン攻略のための実践的な戦略を学びます。

```bash
cat zenn-book/chapters/05-ai-dlc.md
```

**学習内容**:
- AI-DLCサイクルの理解
- ハッカソンでの時間配分
- チーム開発での活用方法

## 🎓 学習リソース

### 公式ドキュメント

- [Antigravity公式サイト](https://antigravity.google)
- [公式ドキュメント](https://antigravity.google/docs/get-started)
- [MCP ドキュメント](https://antigravity.google/docs/mcp)
- [Skills ドキュメント](https://antigravity.google/docs/skills)

### コミュニティ

- **Discord**: Antigravity Developers
- **GitHub Discussions**: 質問・議論
- **Stack Overflow**: `#google-antigravity` タグ

### チュートリアル

- [YouTube公式チャンネル](https://youtube.com/@antigravity)
- [Qiita #Antigravity](https://qiita.com/tags/antigravity)
- [Zenn #Antigravity](https://zenn.dev/topics/antigravity)

## 🐛 トラブルシューティング

### よくある問題

#### 1. Antigravityが起動しない

**症状**: アプリケーションが起動しない、またはクラッシュする

**解決策**:
```bash
# macOSの場合
# アプリケーションを完全に終了
killall Antigravity

# 設定をリセット
rm -rf ~/Library/Application\ Support/Antigravity

# 再起動
open -a Antigravity
```

#### 2. AIモデルが応答しない

**症状**: チャットで質問しても応答がない

**解決策**:
1. インターネット接続を確認
2. Googleアカウントでログインしているか確認
3. 料金プランの制限を確認（Freeプランはレート制限あり）
4. Antigravityを再起動

#### 3. MCPサーバーに接続できない

**症状**: MCP設定で「接続失敗」エラー

**解決策**:
1. MCPサーバーが起動しているか確認
2. ポート番号が正しいか確認
3. ファイアウォール設定を確認
4. 設定ファイル（`.antigravity/mcp.json`）を確認

#### 4. Nano Bananaで画像が生成されない

**症状**: 画像生成のリクエストがエラーになる

**解決策**:
1. 料金プランを確認（Freeプランは月50枚まで）
2. プロンプトが適切か確認（具体的な指示が必要）
3. 生成履歴を確認（Manager View > Artifacts）

### ログの確認

```bash
# Antigravityのログを確認
# macOS
tail -f ~/Library/Logs/Antigravity/main.log

# Windows
type %APPDATA%\Antigravity\logs\main.log

# Linux
tail -f ~/.config/Antigravity/logs/main.log
```

### サポート

問題が解決しない場合:

1. **GitHub Issues**: バグ報告・機能要望
2. **Discord**: リアルタイムサポート
3. **公式サポート**: support@antigravity.google.com

## 🤝 貢献

このハンズオン資料への貢献を歓迎します！

### 貢献方法

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

### 貢献ガイドライン

- **日本語で記述**: すべてのドキュメントは日本語で
- **コードにコメント**: 説明的なコメントを追加
- **テスト**: 変更が既存の機能を壊していないか確認
- **スタイル**: 既存のコードスタイルに従う

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。
