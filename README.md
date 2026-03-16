# 🚀 OpenAI Codex ハンズオン

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

OpenAI が提供するクラウドベース AI コーディングエージェント「**Codex**」と、ターミナルで動作する「**Codex CLI**」の基礎から実践的な活用方法までを、1.5〜2時間程度で習得するためのハンズオン資料です。

## 📚 目次

- [概要](#概要)
- [クイックスタート](#クイックスタート)
- [ハンズオン構成](#ハンズオン構成)
- [前提条件](#前提条件)
- [セットアップ](#セットアップ)
- [使い方](#使い方)
- [トラブルシューティング](#トラブルシューティング)
- [貢献](#貢献)
- [ライセンス](#ライセンス)

## 🎯 概要

**OpenAI Codex** は、2025年5月に OpenAI がリリースしたクラウドベースの AI ソフトウェアエンジニアリングエージェントです。ChatGPT 内から利用でき、GitHub リポジトリと連携して自律的にコーディングタスクを実行します。

### 2つのインターフェース

- 🌐 **Codex（Web版）**: ChatGPT 内の Codex タブから利用。GitHub リポジトリを接続し、クラウドサンドボックス上でコード生成・バグ修正・PR作成を自動実行
- 💻 **Codex CLI**: ターミナルで動作するオープンソースのコーディングエージェント。ローカル環境でファイルを読み書きし、対話的にコード生成・修正を実行

### 主な特徴

- 🤖 **自律的タスク実行**: コード生成、バグ修正、テスト実行、PR 作成まで自動化
- 🔒 **セキュアなサンドボックス**: 隔離されたクラウドコンテナ内で実行（Web版）
- 🔌 **GitHub 連携**: リポジトリを直接操作し、PR やコードレビューを生成
- 📋 **Ask / Code モード**: 質問特化モードとコード実行モードを使い分け
- 🖥️ **Codex CLI**: ローカル環境で動作する軽量なターミナルエージェント

### 学習目標

このハンズオンを通じて、以下のスキルを習得できます:

- ✅ Codex（Web版）の基本操作と GitHub 連携
- ✅ Codex CLI のインストールと活用
- ✅ Ask モード / Code モードの使い分け
- ✅ 自然言語によるコード生成（Vibe Coding）
- ✅ PR 作成やコードレビューの自動化

## ⚡ クイックスタート

```bash
# 1. リポジトリをクローン
git clone https://github.com/YOUR_USERNAME/codex_handson.git
cd codex_handson

# 2. ハンズオン資料を開く
open docs/index.html

# 3. ハンズオンを開始
# docs/index.html から順番に進めてください
```

## 📂 リポジトリ構成

```
codex_handson/
├── docs/                      # ドキュメント・プレゼンテーション資料
│   ├── index.html            # ハンズオンWebページ
│   ├── live-coding-script.md # ライブコーディング台本
│   └── img/                  # 画像・図表
│       ├── fig1.png
│       ├── fig2.png
│       ├── slide-*.png       # スライド画像
│       └── ...
├── LICENSE
└── README.md
```

## 📚 コンテンツ構成

### 🕐 当日のタイムライン

| 時間 | セクション | 内容 |
|:---|:---|:---|
| 19:00〜19:15 | **イントロ** | Vibe Codingとは？AI コーディングエージェントの進化 |
| 19:15〜19:30 | **Codex の特徴** | Web版 / CLI / GitHub連携 / Ask・Codeモード |
| 19:30〜20:00 | **Step 1** | 環境構築 + Codex CLI セットアップ（30分） |
| 20:00〜20:20 | **Step 2** | Vibe Coding 基礎編（自己紹介ページ作成） |
| 20:20〜20:40 | **Step 3** | Codex Web版で GitHub 連携 + PR 自動作成 |
| 20:40〜21:00 | **Step 4** | Vibe Coding 発展編（AI Coffee Shop LP） |
| 21:00〜21:10 | **Step 5** | まとめ：AI-DLCとハッカソン戦略 |

### 🎯 学習フロー

```
【Step 1】基礎の確立（19:30〜20:00）
  Codex CLI インストール → 基本操作を体験
      ↓
【Step 2】Vibe Coding を最速体験（20:00〜20:20）
  Codex CLI で自己紹介ページ作成
      ↓
【Step 3】Web版で GitHub 連携（20:20〜20:40）
  Codex Web版 → リポジトリ接続 → PR 自動作成
      ↓
【Step 4】総合演習（20:40〜21:00）
  AI Coffee Shop LP（リサーチ→実装→デプロイ準備）
      ↓
【Step 5】実践知識（21:00〜21:10）
  AI-DLC × ハッカソン最強戦略
```

## 🔧 前提条件

### 必須

- **OpenAI アカウント**: ChatGPT Plus / Pro / Team / Enterprise のいずれかのプラン
- **GitHub アカウント**: Codex Web版との連携に必要
- **Node.js**: v22 以上（Codex CLI のインストールに必要）
- **インターネット接続**: OpenAI API との通信に必要

### 推奨

- **Git**: バージョン管理
- **VS Code / Cursor**: コード編集（Codex CLI と併用する場合）
- **OpenAI API キー**: Codex CLI で使用

## 🛠️ セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/YOUR_USERNAME/codex_handson.git
cd codex_handson
```

### 2. Codex CLI のインストール

```bash
# npm でグローバルインストール
npm install -g @openai/codex

# インストール確認
codex --version
```

### 3. OpenAI API キーの設定

```bash
# 環境変数に API キーを設定
export OPENAI_API_KEY="sk-..."
```

### 4. Codex Web版の利用開始

1. [ChatGPT](https://chatgpt.com) にログイン
2. 左サイドバーの「Codex」をクリック
3. GitHub アカウントを接続し、リポジトリへのアクセスを許可
4. Ask モードまたは Code モードを選択してタスクを開始

## 📖 使い方

### ハンズオンの進め方

1. **Webページを開く**: `docs/index.html` をブラウザで開く
2. **順番に進める**: Step 1から順番に進めることを推奨
3. **実際に手を動かす**: コードを書いて、動かして、理解を深める
4. **質問・疑問をメモ**: 後で調べたり、コミュニティで質問

### Codex CLI の基本操作

```bash
# 対話モードで起動
codex

# 直接指示を渡す
codex "このプロジェクトの構造を説明して"

# ファイルを指定して修正
codex "index.html にナビゲーションバーを追加して"
```

### Codex Web版の基本操作

1. **Ask モード**: リポジトリの読み取り専用クローンで質問に回答（ブレインストーミング、コード監査に最適）
2. **Code モード**: コード実行・テスト・修正が可能な完全な開発環境（バグ修正、新機能実装に最適）

## 🎓 学習リソース

### 公式ドキュメント

- [OpenAI Codex 公式ページ](https://openai.com/index/introducing-codex/)
- [Codex CLI GitHub リポジトリ](https://github.com/openai/codex)
- [OpenAI API ドキュメント](https://platform.openai.com/docs)
- [ChatGPT](https://chatgpt.com)

### コミュニティ

- **OpenAI Community Forum**: [community.openai.com](https://community.openai.com)
- **GitHub Discussions**: Codex CLI リポジトリの Discussions
- **Stack Overflow**: `#openai-codex` タグ

### チュートリアル

- [Qiita #OpenAI](https://qiita.com/tags/openai)
- [Zenn #OpenAI](https://zenn.dev/topics/openai)

## 🐛 トラブルシューティング

### よくある問題

#### 1. Codex CLI がインストールできない

**症状**: `npm install -g @openai/codex` でエラー

**解決策**:
```bash
# Node.js のバージョンを確認（v22以上が必要）
node --version

# npm キャッシュをクリア
npm cache clean --force

# 再インストール
npm install -g @openai/codex
```

#### 2. API キーが認識されない

**症状**: `Error: Missing API key` が表示される

**解決策**:
```bash
# 環境変数が正しく設定されているか確認
echo $OPENAI_API_KEY

# .bashrc や .zshrc に永続化
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.zshrc
source ~/.zshrc
```

#### 3. Codex Web版で GitHub 連携できない

**症状**: リポジトリが表示されない

**解決策**:
1. GitHub アカウントが正しく接続されているか確認
2. リポジトリへのアクセス権限を再設定
3. プライベートリポジトリの場合は明示的にアクセスを許可
4. ChatGPT を再ログイン

### サポート

問題が解決しない場合:

1. **GitHub Issues**: バグ報告・機能要望
2. **OpenAI Community Forum**: コミュニティサポート
3. **OpenAI Help Center**: [help.openai.com](https://help.openai.com)

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
