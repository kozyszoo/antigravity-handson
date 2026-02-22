# Hands-on 01: 環境セットアップ

## 目標
Google Antigravity を起動して、ワークスペースの基本設定まで済ませましょう。

---

## システム要件

| OS | 要件 |
|:---|:---|
| **macOS** | バージョン 12 (Monterey) 以上 ※ Apple Silicon のみ。X86 は非対応です |
| **Windows** | Windows 10 (64-bit) 以上 |
| **Linux** | glibc >= 2.28, glibcxx >= 3.4.25（Ubuntu 20, Debian 10, Fedora 36, RHEL 8 等） |

> 公式ドキュメント: https://antigravity.google/docs/get-started

---

## チェックリスト

### 1. Antigravity のインストール確認
- Antigravity アプリケーションがインストールされている
- Google アカウントでログイン済み
- アプリが最新版になっている（Restart to Update が出ていたら再起動してください）

### 2. 初期設定（日本語化・拡張機能）

1. **日本語化**:
   - 左側アイコンバーの「Extensions」をクリック
   - 「Japanese Language Pack for Visual Studio Code」を検索してインストール
   - 再起動して日本語化を確認

2. **ブラウザ拡張機能**:
   - Google Chrome に「Antigravity Browser Extension」を追加
   - これにより AI がブラウザを操作してテストできるようになります

### 3. ワークスペースの作成
```bash
# このハンズオンフォルダをワークスペースとして開きます
# Antigravity > File > Open Folder で以下を選択:
# /path/to/antigravity_handson/handson
```

### 3. 基本画面の確認

Antigravity には 2つのメインView があります。

#### Editor View（エディタ画面）
ファイルツリーとエディタが並ぶ、VS Code ベースの画面です。

- Editor View が表示される（左がファイルツリー、中央がエディタ）
- チャットパネルが開く（右サイドバー）

#### Agent Manager（エージェント管理画面）
AIエージェントとのやりとりに特化した画面です。

- Agent Manager に切り替えできる

#### View切り替えショートカット

| 操作 | ショートカット |
|:---|:---|
| Editor → Agent Manager | `Cmd + E` |
| Agent Manager → Editor | `Cmd + E` |

`Cmd + E` で Editor と Agent Manager を行き来できます。

### 4. モデル選択の確認

Antigravity では複数の AI モデルを切り替えて使えます。

#### 推論モデル（Reasoning Model）
メインのコーディングや対話に使うモデルです。右下のモデルセレクターで切り替えられます。

| モデル | 特徴 |
|:---|:---|
| **Gemini 3 Pro** (High/Low) | Google の最新モデル。高性能 |
| **Gemini 3 Flash** | 高速レスポンス |
| **Claude Sonnet 4.5** | Anthropic 製。Standard / Thinking モード |
| **Claude Opus 4.5** | Anthropic 製。高精度（Thinking モード） |
| **GPT-OSS** | OpenAI 互換 |

- `Gemini 3 Pro` が選択できる
- 他のモデルにも切り替えられる

#### バックグラウンドモデル（固定・自動選択）

| モデル | 役割 |
|:---|:---|
| **Nano Banana Pro** | 画像生成、UIモックアップ、アーキテクチャ図 |
| **Gemini 2.5 Pro UI Checkpoint** | Browser Subagent（ブラウザ操作） |
| **Gemini 2.5 Flash** | チェックポイント、コンテキスト要約 |
| **Gemini 2.5 Flash Lite** | コードベースのセマンティック検索 |

Nano Banana は画像生成専用のモデルです。Step 3 で使います。

---

## やってみよう

Antigravity のチャットで試してみましょう。

```
こんにちは！今日の日付と曜日を教えて。
```

今日の日付と曜日が日本語で返ってくれば成功です。

---

## エディタの AI 機能を体験

Antigravity のエディタには、VS Code をベースにした AI ネイティブ機能が載っています。

### Tab（コード補完）
コードを書いている途中で `Tab` キーを押すと、AI が続きを提案してくれます。

| 機能 | 説明 |
|:---|:---|
| **Supercomplete** | 複数行のコード提案。`Tab` で採用 |
| **Tab-to-Jump** | 次の編集箇所を予測してジャンプ |
| **Tab-to-Import** | 不足している import を自動検出・追加 |

### Command（コマンド）
`Cmd + I` で Command パレットを開き、自然言語で指示できます。

```
例: 「この関数にエラーハンドリングを追加して」
例: 「ポート3000を使っているプロセスを見つけて終了して」（ターミナル内）
```

---

## トラブルシューティング

| 問題 | 解決策 |
|:---|:---|
| ログインできない | VPN を切断してみる / ブラウザのキャッシュクリア |
| モデルが選択できない | Rate Limit に達した可能性があります。しばらく待つか別モデルに切り替えてください |
| チャットが応答しない | ネットワーク接続を確認 / Antigravity を再起動 |
| X86 Mac で起動しない | Apple Silicon (M1 以降) のみ対応です |

---

**次へ進む → [02_gemini_md](../02_gemini_md/README.md)**
