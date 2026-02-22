---
title: "Step 1: 環境セットアップ"
---

## このステップのゴール

Google Antigravity をインストールし、ワークスペースを開いて、基本的な画面構成を把握するところまで進めます。

## システム要件

| OS | 要件 |
|:---|:---|
| **macOS** | バージョン 12 (Monterey) 以上。Apple Silicon のみ対応です（X86 は非対応） |
| **Windows** | Windows 10 (64-bit) 以上 |
| **Linux** | glibc >= 2.28, glibcxx >= 3.4.25（Ubuntu 20, Debian 10, Fedora 36, RHEL 8 等） |

:::message
公式ドキュメントはこちら: https://antigravity.google/docs/get-started
:::

## インストール

1. [公式サイト](https://antigravity.google)にアクセスします
2. お使いの OS に合ったインストーラーをダウンロードします
3. インストーラーを実行します
4. 起動したら Google アカウントでログインします

「Restart to Update」の表示が出ていたら、再起動して最新版にしてください。

## 初期設定（日本語化・拡張機能）

### 1. 日本語化

初期状態は英語です。使いやすくするために日本語化しましょう。

1. 画面左側の「Extensions（拡張機能）」アイコンをクリック
2. 「Japanese Language Pack for Visual Studio Code」を検索してインストール
3. 再起動を促されるので再起動します

### 2. ブラウザ拡張機能の導入

AI が作成したアプリの動作確認を自動で行えるようにするため、ブラウザ拡張機能を入れます。

1. Google Chrome に「Antigravity Browser Extension」を追加します
2. これにより、AI がブラウザを操作してテスト（Walkthrough）できるようになります

## ワークスペースを開く

Antigravity で `File > Open Folder` を選び、ハンズオン用のフォルダを開きます。

```
/path/to/antigravity_handson/handson
```

## 2つのメインView

Antigravity には大きく分けて 2つの画面があります。

<!-- TODO: 図2 - Editor View と Agent Manager の画面キャプチャを挿入 -->

### Editor View（エディタ画面）

ファイルツリーとエディタが並ぶ、VS Code ベースの画面です。コードを書いたり、ファイルを編集したりする作業場として使います。右サイドバーにはチャットパネルがあり、ここからもAIに指示を出せます。

### Agent Manager（エージェント管理画面）

AIエージェントとの対話に特化した画面です。自然言語でタスクを依頼し、エージェントの作業状況をリアルタイムで追いかけられます。生成された成果物（Artifacts）もここで確認します。

`Cmd + E` で Editor View と Agent Manager を切り替えられます。

## モデル選択

Antigravity では複数の AI モデルを切り替えて使えます。

### 推論モデル（手動で選択）

右下のモデルセレクターから切り替えます。

| モデル | 特徴 |
|:---|:---|
| **Gemini 3 Pro** (High/Low) | Google の最新モデル。総合力が高い |
| **Gemini 3 Flash** | 高速レスポンス。軽めのタスク向き |
| **Claude Sonnet 4.5** | Anthropic 製。Standard と Thinking モードあり |
| **Claude Opus 4.5** | Anthropic 製。高精度な推論 |
| **GPT-OSS** | OpenAI 互換 |

### バックグラウンドモデル（自動選択）

以下のモデルは用途に応じて自動的に使い分けられます。ユーザーが選択する必要はありません。

| モデル | 役割 |
|:---|:---|
| **Nano Banana Pro** | 画像生成、UIモックアップ |
| **Gemini 2.5 Pro UI Checkpoint** | ブラウザ操作 |
| **Gemini 2.5 Flash** | チェックポイント、コンテキスト要約 |
| **Gemini 2.5 Flash Lite** | コードベースのセマンティック検索 |

Nano Banana は画像生成専用のモデルです。Step 3 で実際に使ってみます。

## やってみよう

ここまでの設定が済んだら、チャットで軽く動作確認しましょう。

```
こんにちは！今日の日付と曜日を教えて。
```

日本語で日付と曜日が返ってくれば成功です。

## エディタの AI 機能

Editor View にはいくつかの AI 支援機能が組み込まれています。

| 機能 | 操作 | 説明 |
|:---|:---|:---|
| **Supercomplete** | `Tab` | 複数行のコード提案を採用 |
| **Tab-to-Jump** | `Tab` | 次の編集箇所を予測してジャンプ |
| **Tab-to-Import** | `Tab` | 不足している import を自動検出・追加 |
| **Command** | `Cmd + I` | 自然言語でコード変更を指示 |

特に Command（`Cmd + I`）はよく使います。「この関数にエラーハンドリングを追加して」のように、選択したコードに対して自然言語で指示を出せます。

<!-- TODO: 図3 - Supercomplete / Command の動作イメージを挿入 -->

## トラブルシューティング

| 問題 | 対処法 |
|:---|:---|
| ログインできない | VPN を切断してみる。ブラウザのキャッシュもクリアする |
| モデルが選択できない | Rate Limit の可能性があります。しばらく待つか別モデルに切り替えてください |
| チャットが応答しない | ネットワーク接続を確認し、Antigravity を再起動してください |
| X86 Mac で起動しない | Apple Silicon (M1 以降) のみ対応です |
