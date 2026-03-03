# 📁 プロジェクト構造

```
antigravity_handson/
├── 📄 README.md                    # メインドキュメント（このファイルから始めてください）
├── 📄 CONTRIBUTING.md              # 貢献ガイドライン
├── 📄 LICENSE                      # MITライセンス
├── 📄 .gitignore                   # Git除外設定
│
├── 📊 プレゼンテーション資料/
│   ├── presentation.md             # Marpソースファイル
│   ├── presentation.html           # HTML版（推奨）
│   ├── presentation.pdf            # PDF版
│   └── PRESENTATION_README.md      # プレゼンテーション資料の使い方
│
├── 📚 handson/                     # ハンズオン資料（メインコンテンツ）
│   ├── 01_setup/                   # Step 1-1: 環境セットアップ
│   │   └── README.md
│   ├── 02_gemini_md/               # Step 2: GEMINI.md設定
│   │   ├── README.md
│   │   └── examples/
│   ├── 03_mcp/                     # Step 3: MCP接続
│   │   └── README.md
│   ├── 04_skills/                  # Step 4: Agent Skills作成
│   │   ├── README.md
│   │   └── .agent/skills/
│   └── 05_vibe_coding/             # Step 5: Vibe Codingデモ
│       ├── README.md
│       └── demo/
│
└── 📦 old/                         # アーカイブ（参考資料）
    ├── README.md
    └── google_antigravity_handson.md
```

## 🚀 クイックスタート

### 1. プレゼンテーション資料を見る

```bash
# ブラウザで開く
open presentation.html
```

### 2. ハンズオンを始める

```bash
# Step 1から順番に進める
cd handson/01_setup
open README.md
```

### 3. 全体像を理解する

```bash
# メインドキュメントを読む
open README.md
```

## 📖 各ファイルの説明

### ルートディレクトリ

| ファイル | 説明 | 重要度 |
|:---|:---|:---:|
| `README.md` | プロジェクトの概要、セットアップ、使い方 | ⭐⭐⭐ |
| `CONTRIBUTING.md` | 貢献方法、コーディング規約 | ⭐⭐ |
| `LICENSE` | MITライセンス | ⭐ |
| `.gitignore` | Git除外設定 | ⭐ |

### プレゼンテーション資料

| ファイル | 説明 | 用途 |
|:---|:---|:---|
| `presentation.md` | Marpソースファイル | 編集用 |
| `presentation.html` | HTML版 | 表示用（推奨） |
| `presentation.pdf` | PDF版 | 配布用 |
| `PRESENTATION_README.md` | 使い方ガイド | 登壇準備 |

### ハンズオン資料

| ディレクトリ | 内容 | 所要時間 |
|:---|:---|:---:|
| `01_setup/` | Antigravityのインストールと基本操作 | 15分 |
| `02_gemini_md/` | プロジェクト設定とGEMINI.md | 15分 |
| `03_mcp/` | MCPサーバーの接続と活用 | 20分 |
| `04_skills/` | Agent Skillsの作成 | 20分 |
| `05_vibe_coding/` | Vibe Codingの実践デモ | 30分 |

## 🎯 推奨学習フロー

```
1. README.md を読む
   ↓
2. presentation.html でAntigravityの概要を理解
   ↓
3. handson/01_setup から順番に実践
   ↓
4. handson/05_vibe_coding で総合演習
   ↓
5. 自分のプロジェクトで活用！
```

## 📝 ファイルの更新

### プレゼンテーション資料を更新

```bash
# presentation.md を編集後
marp presentation.md -o presentation.html --html
marp presentation.md -o presentation.pdf --html --allow-local-files
```

### ハンズオン資料を追加

```bash
# 新しいハンズオンを作成
mkdir handson/06_new_topic
cd handson/06_new_topic
touch README.md

# README.mdにコンテンツを記述
```

## 🗂️ ディレクトリの役割

### `handson/`
- **目的**: 実践的なハンズオン資料
- **構成**: 各ステップごとにディレクトリを分割
- **形式**: Markdown + サンプルコード

### `old/`
- **目的**: アーカイブ・参考資料
- **内容**: 古いバージョンのドキュメント
- **注意**: 最新情報はルートのREADME.mdを参照

## 🔍 ファイルを探す

### 特定のトピックを探す

```bash
# キーワードで検索
grep -r "Nano Banana" handson/

# ファイル名で検索
find . -name "*mcp*"
```

### 最近更新されたファイル

```bash
# 最近更新されたファイルを表示
ls -lt handson/**/README.md
```

## 📊 統計情報

```bash
# ファイル数
find . -type f -name "*.md" | wc -l

# 総行数
find . -type f -name "*.md" -exec wc -l {} + | tail -1

# 総文字数
find . -type f -name "*.md" -exec wc -c {} + | tail -1
```

## 🎨 カスタマイズ

このプロジェクト構造は、以下のように拡張できます:

### 新しいハンズオンを追加

```bash
mkdir handson/06_advanced_features
cd handson/06_advanced_features
cat > README.md << 'EOF'
# Step 6: Advanced Features

## 概要
...
EOF
```

### 多言語対応

```bash
mkdir i18n
mkdir i18n/en
mkdir i18n/ja

# 各言語のREADMEを作成
cp README.md i18n/ja/README.md
# 英語版を作成
touch i18n/en/README.md
```

## 🔗 関連リンク

- [README.md](../README.md) - メインドキュメント
- [CONTRIBUTING.md](../CONTRIBUTING.md) - 貢献ガイドライン
- [PRESENTATION_README.md](../PRESENTATION_README.md) - プレゼンテーション資料の使い方

---

**このドキュメントは、プロジェクトの構造を理解するためのガイドです。**
**実際のハンズオンは `handson/01_setup/README.md` から始めてください！**
