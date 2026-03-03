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

# 2. Marpをインストール（プレゼンテーション資料を表示する場合）
npm install -g @marp-team/marp-cli

# 3. プレゼンテーション資料を表示
open presentation.html
# または
marp -s presentation.md

# 4. ハンズオンを開始
# handson/01_setup/README.md から順番に進めてください
```

## 📂 ハンズオン構成

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

### 📚 ハンズオン資料

| No | フォルダ | 内容 | 時間帯 | 難易度 |
|:---:|:---|:---|:---:|:---:|
| **01** | [Step 1-1: 環境セットアップ](./handson/01_1_setup/README.md) | 環境構築・基本画面確認 | 19:30〜 | ⭐ |
| **02** | [Step 1-2: GEMINI.md 設定](./handson/01_2_gemini_md/README.md) | GEMINI.md 設定 | 19:45〜 | ⭐⭐ |
| **03** | [Step 2: Vibe Coding 基礎編](./handson/02_vibe_coding_basic/README.md) | 🎨 **自己紹介ページ + Nano Banana** | 20:00〜 | ⭐⭐ |
| **04** | [Step 3-1: MCP 接続](./handson/03_1_mcp/README.md) | MCP接続・Browser Subagent | 20:20〜 | ⭐⭐ |
| **05** | [Step 3-2: Agent Skills 作成](./handson/03_2_skills/README.md) | Agent Skills 作成 | 20:30〜 | ⭐⭐⭐ |
| **06** | [Step 4: Vibe Coding 発展編](./handson/04_vibe_coding_advanced/README.md) | 🚀 **AI Coffee Shop LP 構築** | 20:40〜 | ⭐⭐⭐ |
| **07** | [Step 5: AI-DLC戦略](./handson/05_ai_dlc/README.md) | 🏅 **ハッカソン攻略：AI-DLC** | 21:00〜 | ⭐⭐⭐ |

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



## 📊 プレゼンテーション資料

登壇用のMarpプレゼンテーション資料が含まれています。

### ファイル

- `presentation.md` - Marpソースファイル
- `presentation.html` - HTML版（推奨）
- `presentation.pdf` - PDF版

### 表示方法

#### HTML版（推奨）

```bash
# ブラウザで開く
open presentation.html

# または、ライブサーバーで表示
marp -s presentation.md
# http://localhost:8080 にアクセス
```

**操作方法**:
- `→` または `Space`: 次のスライド
- `←`: 前のスライド
- `F`: フルスクリーンモード
- `Esc`: フルスクリーン解除

#### PDF版

```bash
open presentation.pdf
```

### プレゼンテーションの編集

```bash
# presentation.md を編集後、再生成
marp presentation.md -o presentation.html --html
marp presentation.md -o presentation.pdf --html --allow-local-files
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

- **Marp CLI**: プレゼンテーション資料の表示・編集
  ```bash
  npm install -g @marp-team/marp-cli
  ```

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

1. **順番に進める**: `01_setup` から順番に進めることを推奨
2. **各フォルダのREADME.mdを読む**: 詳細な手順が記載されています
3. **実際に手を動かす**: コードを書いて、動かして、理解を深める
4. **質問・疑問をメモ**: 後で調べたり、コミュニティで質問

### 各ハンズオンの概要

#### 01. 環境セットアップ

Antigravityの基本操作を学びます。

```bash
cd handson/01_setup
# README.mdの手順に従って進める
```

**学習内容**:
- Antigravityのインストール
- プロジェクトの作成
- Manager ViewとEditor Viewの使い分け

#### 02. GEMINI.md 設定

プロジェクト固有のルールをAIに教えます。

```bash
cd handson/02_gemini_md
# README.mdの手順に従って進める
```

**学習内容**:
- GEMINI.mdの役割
- プロジェクト設定の記述方法
- コーディング規約の定義

#### 03. Vibe Coding 基礎編

MCP/Skillsなしで、シンプルなVibe Codingを体験します。

```bash
cd handson/03_vibe_coding_basic
# README.mdの手順に従って進める
```

**学習内容**:
- 自然言語でのWebページ作成
- Nano Bananaでの画像生成
- デザインカスタマイズ

#### 04. MCP 接続

外部ツールとの連携を学びます。

```bash
cd handson/04_mcp
# README.mdの手順に従って進める
```

**学習内容**:
- MCPの概念とMCP Store
- ブラウザMCPの接続
- Context7によるドキュメント参照

#### 05. Agent Skills 作成

エージェントに新しい能力を追加します。

```bash
cd handson/05_skills
# README.mdの手順に従って進める
```

**学習内容**:
- Skillsの仕組み（agentskills.io 標準）
- SKILL.mdの作成
- Rules / Workflows / Skills の使い分け

#### 06. Vibe Coding 発展編

MCP + Skills を活用した本格的なVibe Codingを実践します。

```bash
cd handson/06_vibe_coding_advanced
# README.mdの手順に従って進める
```

**学習内容**:
- MCPを使ったWebリサーチ
- 複数のNano Banana画像の統合
- 高速プロトタイピング

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

## 👥 作成者

- **Your Name** - [@your_twitter](https://twitter.com/your_twitter)

## 🙏 謝辞

- Google Antigravityチーム
- コミュニティの皆様
- このハンズオンに貢献してくださった方々

## 📞 お問い合わせ

- **Twitter**: [@your_twitter](https://twitter.com/your_twitter)
- **Email**: your.email@example.com
- **GitHub**: [Issues](https://github.com/YOUR_USERNAME/antigravity_handson/issues)

---

<div align="center">

**🚀 Google Antigravityで、重力から解放された開発体験を！**

[公式サイト](https://antigravity.google) | [ドキュメント](https://antigravity.google/docs/get-started) | [コミュニティ](https://discord.gg/antigravity)

</div>
