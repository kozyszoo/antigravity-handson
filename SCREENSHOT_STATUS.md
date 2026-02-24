# スクリーンショット作成状況

## 完了した作業

### 1. スクリーンショット挿入位置のコメント追加

#### zenn-book/chapters/
すべてのチャプターにスクリーンショット挿入位置のコメントを追加しました。
- ✅ 00-introduction.md (図1)
- ✅ 01-setup.md (図2, 図3)
- ✅ 02-gemini-md.md (図4, 図4b)
- ✅ 03-vibe-coding-basic.md (図5, 図5b, 図6, 図6b, 図6c)
- ✅ 04-mcp.md (図7, 図8, 図8b)
- ✅ 05-skills.md (図9, 図9b, 図9c)
- ✅ 06-vibe-coding-advanced.md (図10, 図10b, 図10c)
- ✅ 07-ai-dlc.md (図11, 図11b, 図11c)
- ✅ 08-summary.md (図12)

#### handson/
すべてのハンズオン資料にスクリーンショット挿入位置のコメントを追加しました。
- ✅ handson/01_setup/README.md (図2, 図3)
- ✅ handson/02_gemini_md/README.md (図4, 図4b)
- ✅ handson/03_vibe_coding_basic/README.md (図5, 図5b, 図6, 図6b, 図6c)
- ✅ handson/04_mcp/README.md (図7, 図8, 図8b)
- ✅ handson/05_skills/README.md (図9, 図9b, 図9c)
- ✅ handson/06_vibe_coding_advanced/README.md (図10, 図10b, 図10c)
- ✅ handson/07_ai_dlc/README.md (図11, 図11b, 図11c)

### 2. 既存の画像参照の保持

以下の既存の画像参照はそのまま保持されています：
- `handson/03_vibe_coding_basic/README.md`:
  - `![Nano Banana Generation](../images/nano_banana_generation.png)`
  - `![Vibe Coding Demo](../images/vibe_coding_demo.png)`
- `handson/04_mcp/README.md`:
  - `![MCP Settings](../images/mcp_settings.png)`
- `handson/07_ai_dlc/README.md`:
  - `![AI-DLC Overview](../../images/ai_dlc_overview.png)`
  - `![AI-DLC Phases](../../images/ai_dlc_phases.png)`
  - `![Mob Elaboration](../../images/mob_elaboration.png)`

### 3. 自動生成したスクリーンショット

Pythonスクリプト (`scripts/screenshot_sample_page.py`) を使用して以下を生成：
- ✅ `images/sample_profile_page.png` - 図6: 完成した自己紹介ページ (199KB)
- ✅ `images/sample_coffee_shop_lp.png` - 図10c: AI Coffee Shop LP完成画面 (269KB)

サンプルHTMLファイル:
- `samples/profile_page_sample.html` - Vibe Codingで作成したような自己紹介ページ
- `samples/coffee_shop_lp_sample.html` - AI Coffee Shop のランディングページ

## 既存の画像ファイル

以下の画像が既に `images/` ディレクトリに存在しています：

### Antigravity UI スクリーンショット
- ✅ `antigravity_editor_view.png` (410KB) - Editor Viewの画面
- ✅ `antigravity_manager_view.png` (544KB) - Agent Managerの画面
- ✅ `antigravity_welcome.png` (463KB) - ウェルカム画面
- ✅ `mcp_settings.png` (464KB) - MCP Store画面
- ✅ `model_selector.png` (452KB) - モデル選択画面
- ✅ `nano_banana_generation.png` (492KB) - Nano Banana生成フロー
- ✅ `skills_folder.png` (411KB) - Skillsフォルダ構造
- ✅ `vibe_coding_demo.png` (697KB) - Vibe Codingデモ

### 図形・ダイアグラム
- ✅ `ai_dlc_overview.png` (92KB) - AI-DLC概要図
- ✅ `ai_dlc_phases.png` (60KB) - AI-DLCフェーズ図
- ✅ `mob_elaboration.png` (47KB) - モブエラボレーション図
- ✅ `agent_security_diagram.png` (54KB) - エージェントセキュリティ図
- ✅ `artifacts_overview.png` (41KB) - Artifacts概要図
- ✅ `browser_subagent_diagram.png` (45KB) - Browser Subagent図
- ✅ `editor_features.png` (54KB) - エディタ機能図
- ✅ `install_policy_diagram.png` (42KB) - インストールポリシー図

### その他
- ✅ `zenn_book_cover.png` (29KB) - Zennブックカバー
- ✅ `zenn_book_cover_with_text.png` (25KB) - テキスト付きカバー
- ✅ `zenn_book_cover_vertical.png` (635KB) - 縦長カバー

## 今後必要な作業

### 図形生成が必要な図（Nano Banana / draw.io）

以下の図は画像生成AIやダイアグラムツールで作成する必要があります：

- [ ] **図1**: Antigravity 概要図 (800×450px) - 放射状ダイアグラム
- [ ] **図4**: ルールファイルの階層と適用範囲 (700×400px) - 入れ子の四角形
- [ ] **図7**: MCP アーキテクチャ図 (900×400px) - 3カラム構成
- [ ] **図9**: Rules / Workflows / Skills の比較図 (800×400px) - カード横並び
- [ ] **図10**: 発展編のワークフロー図 (1000×300px) - 横方向フロー図
- [ ] **図12**: Antigravityの3層構造図 (800×500px) - ピラミッド図

### Antigravity画面スクリーンショットが必要な図

以下の図は実際のAntigravityアプリケーションを操作してスクリーンショットを撮影する必要があります：

- [ ] **図2**: Editor View と Agent Manager の画面比較 (1200×600px)
  - 注: `antigravity_editor_view.png` と `antigravity_manager_view.png` が既存
- [ ] **図3**: エディタの AI 機能（Supercomplete と Command）(800×500px)
  - 注: `editor_features.png` が既存
- [ ] **図4b**: Global Rules 設定画面 (800×500px)
- [ ] **図5**: Nano Banana 画像生成フロー (900×350px)
  - 注: `nano_banana_generation.png` が既存
- [ ] **図5b**: Vibe Coding の対話の様子 (1000×550px)
  - 注: `vibe_coding_demo.png` が既存
- [ ] **図6b**: Artifacts パネルの活用 (600×700px)
- [ ] **図6c**: Artifacts へのインラインコメント機能 (700×450px)
- [ ] **図8**: MCP Store の画面キャプチャ (800×500px)
  - 注: `mcp_settings.png` が既存
- [ ] **図8b**: MCP 演習の実行結果 (1000×550px)
- [ ] **図9b**: Skills のフォルダ構造 (600×400px)
  - 注: `skills_folder.png` が既存
- [ ] **図9c**: code-review Skill の実行結果 (1000×600px)
- [ ] **図10b**: MCP Browser の Web リサーチ実行画面 (1100×600px)

### ブラウザスクリーンショット（自動生成済み）

- ✅ **図6**: 完成した自己紹介ページ → `sample_profile_page.png`
- ✅ **図10c**: AI Coffee Shop LP 完成画面 → `sample_coffee_shop_lp.png`

## 使用ツール

### Pythonスクリプト
- `scripts/screenshot_sample_page.py` - PlaywrightでHTMLページのスクリーンショットを自動撮影

### サンプルHTMLファイル
- `samples/profile_page_sample.html` - Vibe Coding基礎編の自己紹介ページサンプル
- `samples/coffee_shop_lp_sample.html` - Vibe Coding発展編のカフェLPサンプル

### 必要なパッケージ
```bash
pip install playwright
python -m playwright install chromium
```

## 注意事項

1. **既存画像との重複**
   - 多くのスクリーンショットは既に `images/` ディレクトリに存在しています
   - コメントで指示されている図と既存画像のマッピングを確認してください

2. **Antigravity画面のキャプチャ**
   - 実際のAntigravityアプリケーションを起動して手動で撮影する必要があります
   - macOSの `screencapture` コマンドまたは手動でのスクリーンショットが必要です

3. **図形生成**
   - ダイアグラムツール（draw.io、Figma等）または画像生成AI（Nano Banana等）で作成してください
   - サイズと色の指定に注意してください
