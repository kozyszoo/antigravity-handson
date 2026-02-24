# Antigravity スクリーンショット撮影ガイド

このガイドでは、Antigravityアプリケーションのスクリーンショットを撮影する手順を説明します。

## 撮影前の準備

### 1. Antigravityの起動
```bash
# Antigravityアプリケーションを起動
open -a Antigravity
```

### 2. 必要なツール
- macOS標準の`screencapture`コマンド
- または、スクリーンショットアプリ（Cmd+Shift+5）

### 3. 推奨設定
- ディスプレイ解像度: 1920x1080以上
- Antigravityのテーマ: ダークモード推奨
- フォントサイズ: 中程度（デフォルト）

---

## 撮影方法

### 方法A: 自動撮影スクリプト（推奨）

```bash
cd scripts
./capture_antigravity_screenshots.sh
```

スクリプトが各スクリーンショットをガイドします。

### 方法B: 手動撮影

#### macOS標準機能を使う
1. `Cmd + Shift + 4`: 範囲を選択して撮影
2. `Cmd + Shift + 4` → `Space`: ウィンドウ全体を撮影
3. 撮影後、デスクトップに保存される画像を`images/`に移動

#### screencaptureコマンドを使う
```bash
# 特定の領域を選択して撮影
screencapture -i images/filename.png

# 5秒後に全画面を撮影
screencapture -T 5 images/filename.png

# 特定のウィンドウを撮影（ウィンドウ選択モード）
screencapture -w images/filename.png
```

---

## 各スクリーンショットの撮影手順

### 図2: Editor View と Agent Manager の画面比較

**ファイル名**: `antigravity_dual_view.png`
**サイズ**: 1200×600px

**手順**:
1. Antigravityで新しいプロジェクトを開く
2. 左側に**Editor View**を表示
   - ファイルツリーを開く
   - 中央にコードエディタを表示
   - 右側にAIチャットパネルを表示
3. `Cmd + E`で**Agent Manager**に切り替え
4. それぞれのスクリーンショットを撮影
5. 画像編集ツールで2枚を左右に並べる
6. 各領域に緑色（#4ecca3）の注釈ラベルを追加

**注釈内容**:
- Editor View: 「ファイルツリー」「エディタ」「AIチャット」
- Agent Manager: 「対話画面」「Artifacts」

---

### 図3: エディタのAI機能（Supercomplete と Command）

**ファイル名**: `editor_ai_features.png`
**サイズ**: 800×500px

**手順**:
1. **上段（Supercomplete）**:
   - Editor Viewでコードを入力中の状態
   - `Tab`キーを押す前のグレーアウトされた補完候補を表示
   - ツールチップ「Tab で採用」を表示
   - スクリーンショットを撮影

2. **下段（Command）**:
   - `Cmd + I`を押してCommandパレットを開く
   - 入力欄に「この関数にエラーハンドリングを追加して」と入力
   - スクリーンショットを撮影

3. 2枚の画像を上下に並べて合成
4. 各部に説明ラベルを追加

---

### 図4b: Global Rules 設定画面

**ファイル名**: `global_rules_settings.png`
**サイズ**: 800×500px

**手順**:
1. Agent Managerを開く
2. 右上の「...」（三点メニュー）をクリック
3. `Customizations` > `Rules` > `Global`を選択
4. GEMINI.mdの編集画面が表示される
5. スクリーンショットを撮影
6. 緑色の矢印で「ここをクリック」の注釈を追加

---

### 図5: Nano Banana 画像生成フロー

**ファイル名**: `nano_banana_flow.png`
**サイズ**: 900×350px

**手順**:
1. **ステップ1（左）**: チャット入力
   - Agent Managerのチャット欄に入力
   - 「Nano Bananaで、プロフィール用のアバター画像を生成して...」
   - 入力直後の状態を撮影

2. **ステップ2（中央）**: 生成中
   - AI応答中のスピナー表示を撮影
   - 「生成中...」のテキストが表示されている状態

3. **ステップ3（右）**: 生成完了
   - 生成された画像のプレビューが表示された状態
   - Artifactsパネルにも画像ファイルが表示

4. 3枚の画像を左→右に並べる
5. 矢印（→）で接続
6. ①②③のラベルを追加

---

### 図5b: Vibe Coding の対話の様子

**ファイル名**: `vibe_coding_dialog.png`
**サイズ**: 1000×550px

**手順**:
1. Agent Managerを開く
2. **左側（チャット）**:
   - ユーザー入力: 「背景色をダークモードに変更して。アクセントカラーは青緑系（#4ecca3）にして。」
   - AI応答: 「承知しました。以下の変更を行います...」

3. **右側（Artifacts）**:
   - Implementation Planが表示されている
   - 変更内容がリスト形式で記載
   - 下部に「Proceed（実行）」ボタン

4. スクリーンショットを撮影
5. 矢印と注釈で「① 指示 → ② 計画書確認 → ③ Proceed で実行」の流れを示す

---

### 図6b: Artifacts パネルの活用

**ファイル名**: `artifacts_panel.png`
**サイズ**: 600×700px

**手順**:
1. Agent ManagerでArtifactsパネルを開く
2. 「Implementation Plan」タブを選択
3. 計画書の内容（Markdown形式）を表示
   - 例: 「## 実装計画\n1. index.htmlの背景色を変更する...」
4. 下部に「Approve（承認）」「Edit（編集）」ボタンを表示
5. 右上のタブ（Code Diff、Walkthroughなど）も見える状態
6. スクリーンショットを撮影
7. 矢印で各タブと承認ボタンの場所を示す注釈を追加

---

### 図6c: Artifacts へのインラインコメント機能

**ファイル名**: `artifacts_inline_comment.png`
**サイズ**: 700×450px

**手順**:
1. Implementation Planの特定行をクリック
2. 行がハイライト（選択状態）される
3. 右横に吹き出し型のコメント入力欄が表示される
   - Googleドキュメント風のUI
4. コメント欄に「エラー時の挙動も追加して」と入力
5. コメント欄下部の「Send（送信）」ボタンを表示
6. スクリーンショットを撮影

---

### 図8: MCP Store の画面キャプチャ

**ファイル名**: `mcp_store_screen.png`
**サイズ**: 800×500px

**手順**:
1. Agent Managerを開く
2. 右上の「...」メニュー → `MCP Store`を選択
3. MCP Store画面が開く
   - 左上に「MCP Store」の見出し
   - 検索バー（上部）
   - カード形式のMCPサーバー一覧（グリッド表示）
     - playwright, context7, github, postgres など
4. インストール済みのものには[Installed]バッジ
5. スクリーンショットを撮影
6. 矢印と注釈（#4ecca3）で「ここからインストール」と記載

---

### 図8b: MCP 演習の実行結果

**ファイル名**: `mcp_execution_result.png`
**サイズ**: 1000×550px

**手順**:
1. Agent Managerで以下を入力・実行:
   ```
   Browser MCPを使って、『Antigravity IDE 2026』を検索して、
   トップ3件の記事タイトルを教えて。
   ```

2. **左側（チャット）**:
   - ユーザー入力が表示
   - AI応答: 「ブラウザを起動して検索中です...」
   - 下に検索結果のサマリーが表示

3. **右側（Artifacts）**:
   - 「Screenshots / Browser Recordings」タブ
   - ブラウザのキャプチャが表示
   - 検索結果TOP3がリスト形式で記載

4. スクリーンショットを撮影
5. 矢印と注釈で「MCPは外部ツールを呼び出す」ことを表現

---

### 図9b: Skills のフォルダ構造

**ファイル名**: `skills_folder_tree.png`
**サイズ**: 600×400px

**手順**:
1. Editor Viewを開く
2. ファイルツリー（サイドバー）で`.agent/skills/`を展開
3. 以下の構造を表示:
   ```
   .agent/
   └── skills/
       ├── code-review/
       │   └── SKILL.md    ← ハイライト
       └── marp-presentation/
           └── SKILL.md
   ```
4. `code-review/SKILL.md`をハイライト
5. マウスオーバー時のツールチップを表示
   - 「コードレビュー用 Skill — SKILL.md」
6. スクリーンショットを撮影
7. 矢印と注釈（#4ecca3）で「SKILL.md が Skill の定義ファイル」と示す

---

### 図9c: code-review Skill の実行結果

**ファイル名**: `code_review_result.png`
**サイズ**: 1000×600px

**手順**:
1. Agent Managerで以下を入力・実行:
   ```
   sample.js を code-review Skill でレビューして
   ```

2. **左側（チャット）**:
   - ユーザー入力が表示
   - AI応答: 「@code-review Skill を使用して sample.js を確認します...」
   - レビュー結果（SKILL.mdの出力フォーマット通り）:
     ```
     ✅ 良い点: ...
     ⚠️ 要改善: ...
     🔒 セキュリティ懸念: ...
     ```

3. **右側（Artifacts）**:
   - レビュー結果をMarkdown形式でまとめたWalkthrough

4. スクリーンショットを撮影
5. 矢印と注釈で「@skill名 で呼び出せる」ことを示す

---

### 図10b: MCP Browser の Web リサーチ実行画面

**ファイル名**: `mcp_browser_research.png`
**サイズ**: 1100×600px

**手順**:
1. Agent Managerで以下を入力・実行:
   ```
   Browser MCPを使って、『おしゃれなカフェ ランディングページ』で検索して、
   上位5サイトのデザインの特徴を分析して。

   特に以下の点をまとめて：
   - 色使い
   - レイアウト
   - CTAボタンのデザイン
   - 画像の使い方
   ```

2. **左側（チャット）**:
   - ユーザー入力が表示
   - AI応答: 「ブラウザを起動して検索中です...」
   - カフェLPのデザイン分析サマリーが表示

3. **右側（Artifacts）**:
   - MCPが取得した各サイトのスクリーンショットサムネイル
   - 下部に「Design Analysis Report」
   - 分析結果が表示

4. スクリーンショットを撮影
5. 矢印と注釈で「ブラウザ操作は AI が行う」ことを表現

---

## 撮影後の処理

### 1. 画像の確認
```bash
# 撮影した画像を確認
open images/
```

### 2. 画像の編集（必要に応じて）
- 注釈の追加（矢印、ラベル、説明テキスト）
- 推奨ツール:
  - Skitch（無料、macOS）
  - Pixelmator Pro（有料）
  - Preview.app（macOS標準）

### 3. ファイルサイズの最適化
```bash
# ImageMagickを使った圧縮（オプション）
brew install imagemagick
mogrify -strip -quality 85 images/*.png
```

### 4. チェックリストの更新
`SCREENSHOT_STATUS.md`を更新して撮影状況を記録

---

## トラブルシューティング

### Q: Antigravityが起動しない
A: Antigravityが正しくインストールされているか確認してください。

### Q: スクリーンショットが大きすぎる
A: 撮影時にウィンドウサイズを調整するか、後から画像編集ツールでリサイズしてください。

### Q: 特定の画面が表示できない
A:
- MCP Storeが表示されない → MCPが有効化されているか確認
- Artifactsパネルが表示されない → 実際にタスクを実行して生成させる
- Skillsフォルダが見えない → `.agent/skills/`ディレクトリを作成

---

## 参考資料

- [macOS screencaptureコマンド](https://ss64.com/osx/screencapture.html)
- [Antigravity公式ドキュメント](https://antigravity.google/docs)
- `figure-creation-prompts.md` - 各図の詳細仕様
