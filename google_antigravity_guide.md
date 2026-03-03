---
marp: true
theme: default
paginate: true
html: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0');


  /* ===== カラーパレット（パステル調） ===== */
  /* Blue: #a8d8ea / #6daad8, Pink: #f6c6ea / #e08ac0 */
  /* Green: #c1e6c0 / #6bb86a, Orange: #ffe0ac / #e0a050 */
  /* Lavender: #d5c6e0 / #9b82b5 */

  /* ===== ベース ===== */
  section {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 22px;
    line-height: 1.6;
    padding: 40px 60px;
    background: #efe8f6;
    color: #3a2e4a;
  }

  /* ===== 見出し ===== */
  h1 { font-size: 38px; font-weight: 900; color: #4a3560; margin-bottom: 12px; }
  h2 { font-size: 27px; font-weight: 700; color: #5a4575; margin-bottom: 8px; }
  h3 { font-size: 20px; font-weight: 700; color: #6a5580; margin-bottom: 4px; }

  /* ===== 背景バリエーション ===== */
  section.lead      { background: #e3d8f2; }
  section.bg-blue   { background: #efe8f6; }
  section.bg-pink   { background: #efe8f6; }
  section.bg-green  { background: #efe8f6; }
  section.bg-orange { background: #efe8f6; }
  section.bg-lav    { background: #efe8f6; }
  section.bg-dark   { background: #efe8f6; color: #3a2e4a; }
  section.bg-dark h1, section.bg-dark h2, section.bg-dark h3 { color: #4a3560; }

  /* ===== カード ===== */
  .card {
    border-radius: 12px;
    padding: 14px 18px;
    margin: 4px 0;
    box-shadow: 0 3px 12px rgba(90,70,120,0.08);
  }
  .card-blue   { background: rgba(168,216,234,0.28); border: 2px solid #a8d8ea; }
  .card-pink   { background: rgba(246,198,234,0.28); border: 2px solid #f6c6ea; }
  .card-green  { background: rgba(193,230,192,0.28); border: 2px solid #c1e6c0; }
  .card-orange { background: rgba(255,224,172,0.28); border: 2px solid #ffe0ac; }
  .card-lav    { background: rgba(213,198,224,0.28); border: 2px solid #d5c6e0; }

  /* ===== レイアウト ===== */
  .cols   { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .cols-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }
  .center { text-align: center; }
  .gap    { display: flex; flex-wrap: wrap; gap: 10px; }

  /* ===== Material Symbols ===== */
  .ms {
    font-family: 'Material Symbols Outlined';
    font-size: 38px;
    line-height: 1;
    vertical-align: middle;
  }
  .ms-sm   { font-size: 28px; }
  .ms-lg   { font-size: 50px; }
  .ms-xl   { font-size: 64px; }
  .ms-hero { font-size: 96px; }

  /* ===== アイコン色 ===== */
  .c-blue   { color: #6daad8; }
  .c-pink   { color: #e08ac0; }
  .c-green  { color: #6bb86a; }
  .c-orange { color: #e0a050; }
  .c-lav    { color: #9b82b5; }
  .c-white  { color: #ffffff; }

  /* ===== ページ番号 ===== */
  section::after { color: #9b82b5; font-size: 16px; }

  /* ===== タイムバッジ ===== */
  .time-badge {
    display: inline-block;
    background: #9b82b5;
    color: white;
    border-radius: 20px;
    padding: 4px 16px;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 12px;
  }

  /* ===== ステップバッジ ===== */
  .step-badge {
    display: inline-block;
    border-radius: 8px;
    padding: 3px 12px;
    font-size: 16px;
    font-weight: 700;
    margin-right: 8px;
  }
  .step-blue   { background: #6daad8; color: white; }
  .step-green  { background: #6bb86a; color: white; }
  .step-orange { background: #e0a050; color: white; }
  .step-lav    { background: #9b82b5; color: white; }

  /* ===== コードブロック ===== */
  code {
    font-family: 'JetBrains Mono', monospace;
    background: rgba(157,130,181,0.15);
    border-radius: 4px;
    padding: 2px 6px;
    font-size: 0.85em;
  }
  pre code {
    background: none;
    padding: 0;
  }
  pre {
    background: #2d2040;
    color: #e8d8ff;
    border-radius: 10px;
    padding: 14px 18px;
    font-size: 18px;
  }
---

<!-- _class: lead -->

<div class="center">

<div style="font-size: 80px; margin-bottom: 24px;">🚀</div>

<h1 style="font-size: 72px; font-weight: 900; letter-spacing: -1px; margin-bottom: 24px; color: #3a2e4a;">Google Antigravity</h1>

<h2 style="font-size: 30px; color: #5a5a5a; font-weight: 700; margin-bottom: 64px;">次世代AIエージェント統合開発環境<br>完全ガイド</h2>

<div style="font-size: 24px; color: #5a5a5a; font-weight: 700; margin-bottom: 24px;">2026年3月</div>

<div style="display: inline-flex; align-items: center; justify-content: center; background: white; padding: 14px 44px; border-radius: 40px; box-shadow: 0 4px 16px rgba(0,0,0,0.06); font-weight: 700; font-size: 20px; color: #6a5580;">
  <span style="font-size: 24px; margin-right: 8px;">💡</span> 便利な使い方 × 珍しい使い方 <span style="color: #ccc; margin: 0 16px;">|</span> <span style="font-size: 24px; margin-right: 8px;">🎯</span> <span style="color: #72608c;">開発効率を爆上げ</span>
</div>

</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">list</span> 目次

<div class="cols">
<div>

<div class="card card-blue" style="margin-bottom:10px;">
<strong>1️⃣ Google Antigravityとは</strong><br>
<small>基本概念・Cursor/VS Codeとの違い</small>
</div>

<div class="card card-blue" style="margin-bottom:10px;">
<strong>2️⃣ 主要機能</strong><br>
<small>Planning Mode / Browser Agent / MCP</small>
</div>

<div class="card card-green" style="margin-bottom:10px;">
<strong>3️⃣ 便利な使い方</strong><br>
<small>モード使い分け・カスタマイズ・Skills</small>
</div>

</div>
<div>

<div class="card card-orange" style="margin-bottom:10px;">
<strong>4️⃣ 珍しい使い方</strong><br>
<small>MCP統合・GA4分析・GitHub自動化</small>
</div>

<div class="card card-orange" style="margin-bottom:10px;">
<strong>5️⃣ 高度な活用法</strong><br>
<small>複数エージェント・画像生成・Vibe Coding</small>
</div>

<div class="card card-lav">
<strong>6️⃣ 実践プロンプト集</strong><br>
<small>すぐに使える実例</small>
</div>

</div>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">rocket_launch</span> Google Antigravityとは？

<div class="cols">
<div>

<div class="card card-blue">

### 📌 基本情報

- **リリース**: 2025年11月
- **提供**: Google
- **AI**: Gemini 3 Pro（+ Claude、GPT-OSS）
- **ベース**: VS Code互換
- **状況**: パブリックプレビュー（無料）

</div>

<div class="card card-lav" style="margin-top:10px;">

### 💡 コンセプト

**「AIエージェントが主役」**の開発プラットフォーム

従来のコード補完ツールから、<br>**計画→実装→検証を自律実行**する<br>次世代IDEへの進化

</div>

</div>
<div>

<div class="card card-green">

### ⚡ 革新ポイント

- **Weightless Context**<br>
  <small>プロジェクト全体が常にAIからアクセス可能</small>

- **Agent-First Interface**<br>
  <small>AIが計画立案・実装・テストを自律実行</small>

- **Liquid State Sandbox**<br>
  <small>コード・メモリ・DB状態を巻き戻し可能</small>

- **Browser Integration**<br>
  <small>Chromeで動作確認まで自動化</small>

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://qiita.com/nakano_teppei_engineer/items/ad0e80264d851c0dd5dc">Qiita</a> | <a href="https://dad-union.com/google-antigravity-ai-editor">DAD UNION</a> | <a href="https://nobdata.co.jp/report/creative_ai/03/">NOB DATA</a>
</div>

---

<!-- _class: bg-pink -->

# <span class="ms ms-lg c-pink">compare_arrows</span> Cursor・VS Codeとの違い

<div class="cols-3">
<div>

<div class="card card-blue">

### <span class="ms ms-sm c-blue">smart_toy</span> Antigravity

**AI**: Gemini 3（ネイティブ）

**エージェント**: ◎<br>
<small>ブラウザ・ターミナル自動操作</small>

**自律性**: 高<br>
<small>計画→実装→検証まで</small>

**提供**: パブリックプレビュー<br>
<small>（2025年11月〜）</small>

</div>

</div>
<div>

<div class="card card-pink">

### <span class="ms ms-sm c-pink">code</span> Cursor

**AI**: Claude 3.5 / GPT-4

**エージェント**: ○<br>
<small>コード生成特化</small>

**自律性**: 中<br>
<small>提案ベース</small>

**提供**: 一般公開済み<br>
<small>（有料プランあり）</small>

</div>

</div>
<div>

<div class="card card-green">

### <span class="ms ms-sm c-green">developer_mode</span> VS Code

**AI**: 拡張機能による

**エージェント**: △<br>
<small>限定的</small>

**自律性**: 低<br>
<small>補助的</small>

**提供**: オープンソース<br>
<small>（Microsoft提供）</small>

</div>

</div>
</div>

<div class="card card-orange" style="margin-top:16px;">
<strong>🎯 最大の違い</strong>: Antigravityは<strong>ブラウザを実際に開いて動作テストを実行</strong>し、スクリーンショット・動画で検証結果を提出できる点
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://dad-union.com/google-antigravity-ai-editor">DAD UNION</a> | <a href="https://manabinoba.blog/google-antigravity-guide/">学べるブログ</a>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">settings</span> 主要機能（1/3）：Planning vs Fast Mode

<div class="cols">
<div>

<div class="card card-blue">

### <span class="ms ms-sm c-blue">psychology</span> Planning Mode

**推奨**: 90%のタスクで使用

- 実装前に計画（Artifacts）作成
- レビュー後に「Proceed」で実行
- 複雑な実装・インフラ構築に最適

</div>

</div>
<div>

<div class="card card-green">

### <span class="ms ms-sm c-green">bolt</span> Fast Mode

**推奨**: 10%のタスクで使用

- 計画省略して即実行
- 簡単なタスク・単一ファイル修正に最適

⚠️ 複雑なタスクでは原因特定が困難

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://qiita.com/akira_papa_AI/items/0acf2679e4ce9f7fb153">Qiita: 完全攻略ガイド</a> | <a href="https://dev.classmethod.jp/articles/google-antigravity-five-tips/">DevelopersIO</a>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">web</span> 主要機能（2/3）：Browser Agent

<div class="card card-blue">

### 🌐 ブラウザ統合による完全自動デバッグ

エージェントが**人間のようにブラウザを操作**して、動作確認・デバッグを実行

</div>

<div class="cols" style="margin-top:16px;">
<div>

<div class="card card-green">

### 🎬 動作フロー

1. Chrome起動→操作実行
2. ログ・スクリーンショット取得
3. エラー特定→修正→再テスト

</div>

</div>
<div>

<div class="card card-orange">

### 💡 具体例

「保存ボタンを押すと時々落ちる」

**従来**: 手動でブラウザ起動→ログ確認→調査

**Antigravity**: 「エラーが出たから直して」→自動で全工程実行→Artifacts確認

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://blog.g-gen.co.jp/entry/getting-started-with-google-antigravity">G-gen Tech Blog</a> | <a href="https://developers.play.jp/entry/2026/02/16/113000">PLAY DEVELOPERS BLOG</a>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">hub</span> 主要機能（3/3）：MCP統合

<div class="card card-blue">

### 🔌 MCP

外部ツール・データソースとIDEを接続するプロトコル

</div>

<div class="cols" style="margin-top:16px;">
<div>

<div class="card card-green">

### 🛠️ 必須MCP

<span class="step-badge step-blue">Filesystem</span> プロジェクト構造把握
<span class="step-badge step-green">BraveSearch</span> 最新情報取得
<span class="step-badge step-orange">SequentialThinking</span> 論理フロー構築

</div>

</div>
<div>

<div class="card card-pink">

### ⚡ できること

- GitHub連携（Issue→実装→PR自動化）
- GA4分析（Web解析をIDE内で完結）
- GCP統合・Linear連携・Postgres操作

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://note.com/sawahotaru/n/n1b48c673663d">note: GCP開発エージェント</a> | <a href="https://www.jicoo.com/magazine/blog/google-antigravity-mcp-integration">Jicoo</a>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">tips_and_updates</span> 便利な使い方（1/4）：モデルの使い分け

<div class="cols">
<div>

<div class="card card-blue">

### 🎯 利用可能モデル

- **Gemini 3 Pro High**: 深い推論・複雑ロジック
- **Gemini 3 Pro Low**: 低レイテンシ・高速実行
- **Claude Sonnet 4.6**: 思考過程可視化

</div>

</div>
<div>

<div class="card card-green">

### ⚙️ 推奨戦略

- 設計段階 → High（深い推論）
- 実装段階 → Low（高速）
- 複雑ロジック → Claude Sonnet 4.6

💡 設計はHigh、実装はLowに切り替えると効率的

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://dev.classmethod.jp/articles/google-antigravity-five-tips/">DevelopersIO: 5つの活用ポイント</a>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">tune</span> 便利な使い方（2/4）：Customizations

<div class="cols">
<div>

<div class="card card-blue">

### 📝 グローバル指示の設定

`~/.gemini/GEMINI.md` に記述→全セッションで共有

**メリット**: 一貫性確保・手間削減

</div>

<div class="card card-green" style="margin-top:10px;">

### 🔐 セキュリティ設定

Artifact Review: "Request Review"推奨
Terminal: 削除・Git操作は確認必須

</div>

</div>
<div>

<div class="card card-pink">

### 📌 推奨設定例

```markdown
# GEMINI.md
- 思考は英語、出力は日本語
- TypeScript必須
- 機密情報はコミット禁止
```

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://dev.classmethod.jp/articles/google-antigravity-five-tips/">DevelopersIO: 5つの活用ポイント</a>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">auto_awesome</span> 便利な使い方（3/4）：Skills機能

<div class="cols">
<div>

<div class="card card-blue">

### 🎨 Skillsとは

AIエージェントに**再利用可能な手順書**を付与

必要な時だけ知識をロード→コンテキスト汚染を防止

</div>

<div class="card card-green" style="margin-top:10px;">

### 📂 配置場所

プロジェクトルートに `SKILL.md` を配置

</div>

</div>
<div>

<div class="card card-pink">

### 📝 実装例

```markdown
# 原稿作成スキル
1. 資料.txt を読み込む
2. 原稿生成→output.txt保存
3. 画像自動生成
```
**使用**: 「資料.txtで原稿作成」→自動実行

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://forest.watch.impress.co.jp/docs/serial/yaaiwatch/2078823.html">窓の杜: Skills機能</a> | <a href="https://www.kyoukasho.net/entry/Antigravity-tips">AI社長のブログ</a>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">route</span> 便利な使い方（4/4）：Workflow Presets

<div class="cols">
<div>

<div class="card card-blue">

### 🔄 Workflowとは

定型作業を**テンプレート化**（workflow.md）

作業効率化・品質一貫性・ノウハウ共有

</div>

<div class="card card-green" style="margin-top:10px;">

### ⌨️ ショートカット

```
Cmd/Ctrl + E: Editor切替
Cmd/Ctrl + I: インライン編集
Cmd/Ctrl + L: チャット
```

</div>

</div>
<div>

<div class="card card-pink">

### 📌 Workflow例

```markdown
# consulting
1. 分析→提案作成→評価
2. OUTPUT: PDFレポート
```
**使用**: メニュー選択→自動実行

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://www.kyoukasho.net/entry/Antigravity-tips">AI社長のブログ: 20のTIPS</a>
</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange">explore</span> 珍しい使い方（1/4）：GA4分析の自動化

<div class="cols">
<div>

<div class="card card-blue">

### 📊 IDEでWeb解析が完結

**従来**: GA4ブラウザで開く→エクスポート→実装
**文脈切り替え**が非効率

</div>

<div class="card card-green" style="margin-top:10px;">

### 🛠️ セットアップ

1. GCP API有効化
2. サービスアカウント作成
3. mcp.json設定

</div>

</div>
<div>

<div class="card card-pink">

### ⚡ できること

**プロンプト**: 「直帰率が高いページを特定して改善」

**動作**: GA4データ取得→分析→原因特定→改善実装

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://graphbooth.com/posts/2025-11-30-antigravity-mcp-ga4">Graphbooth: GA4統合</a> | <a href="https://www.jicoo.com/magazine/blog/google-antigravity-mcp-integration">Jicoo: MCP統合</a>
</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange">integration_instructions</span> 珍しい使い方（2/4）：GitHub自動化

<div class="cols">
<div>

<div class="card card-blue">

### 🔄 Issue → 実装 → PR を完全自動化

1. 要件定義作成
2. Issue起票
3. 実装計画→実装・コミット
4. PR作成・レビュー

</div>


</div>
<div>

<div class="card card-pink">

### 📝 セットアップ

```bash
# 1. PAT発行 → gh auth login
# 2. mcp_config.json に設定
```

**使用**: 「機能実装してPR作成」→自動実行
**注意**: mcp_config.json を .gitignore に追加

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://zenn.dev/emp_tech_blog/articles/automate-issue-to-pr-with-antigravity-and-mcp">Zenn: GitHub自動化</a>
</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange">sensors</span> 珍しい使い方（3/4）：複数エージェント並列実行

<div class="cols">
<div>

<div class="card card-blue">

### 🎭 Mission Control

**複数タスクを同時進行**

- 待ち時間ゼロ
- 生産性3倍以上
- Inbox機能で一元管理

</div>

</div>
<div>

<div class="card card-pink">

### 💡 実践例

**シナリオ**: レガシーリファクタリング

並列実行:
- A: リファクタリング
- B: ユニットテスト
- C: ドキュメント更新
- D: デプロイスクリプト

**効果**: 開発時間75%削減（8時間→2時間）

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://nobdata.co.jp/report/creative_ai/03/">NOB DATA: 徹底解説</a> | <a href="https://qiita.com/akira_papa_AI/items/0acf2679e4ce9f7fb153">Qiita: 完全攻略ガイド</a>
</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange">palette</span> 珍しい使い方（4/4）：画像生成統合

<div class="cols">
<div>

<div class="card card-blue">

### 🎨 Nano Banana Model

UI開発で**画像アセットも自動生成**

- デザイン指示だけで画像生成
- 対応: PNG/JPG/SVG/WebP

</div>

</div>
<div>

<div class="card card-pink">

### 📝 プロンプト例

「90年代レトロなサイトを作って」

**動作**: CSS実装→画像生成→デプロイ
**結果**: HTML/CSS/JS + 画像10枚が**約3分**で完成

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://hackernoon.com/10-spectacular-use-cases-of-google-antigravity-orchestrating-no-code-ai-agents">HackerNoon: 10 Use-Cases</a>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">science</span> 高度な活用法（1/3）：Vibe Coding

<div class="cols">
<div>

<div class="card card-blue">

### 🎵 Vibe Codingとは

**「雰囲気」だけで開発**

- 従来: How（どう作るか）を指示
- Vibe: What（何を作るか）だけ伝える

**効果**: MVP開発が数週間→**数時間**

</div>

</div>
<div>

<div class="card card-pink">

### 💡 実例

「写真投稿してAIがカロリー計算するアプリを作って」

**動作**: 設計→React+Node実装→API統合→デプロイ
**結果**: プログラミング初心者でも**MVPが数時間で完成**

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://blog.g-gen.co.jp/entry/getting-started-with-google-antigravity">G-gen Tech Blog</a> | <a href="https://developers.play.jp/entry/2026/02/16/113000">PLAY DEVELOPERS BLOG</a>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">psychiatry</span> 高度な活用法（2/3）：ライティングスタイルのクローン化

<div class="cols">
<div>

<div class="card card-blue">

### ✍️ 個人の文体を学習

1. 既存記事を読み込ませる
2. 文体・トーン分析
3. workflow.mdに保存

**メリット**: 一貫性維持・執筆速度向上

</div>

</div>
<div>

<div class="card card-pink">

### 📝 Workflow設定例

```markdown
# personal-writing
- トーン: フレンドリー、専門的
- 構成: 結論先行型
```
**使用**: 「AIツール3000文字で」→自動執筆

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://www.kyoukasho.net/entry/Antigravity-tips">AI社長のブログ: 20のTIPS</a>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">history</span> 高度な活用法（3/3）：Liquid State Sandbox

<div class="cols">
<div>

<div class="card card-blue">

### ⏮️ 時間を巻き戻せる開発環境

**特徴**: コード・メモリ・DB状態を巻き戻し

**Gitとの違い**:
- Git: コードのみ
- Liquid State: コード・メモリ・DB・環境変数すべて

</div>

</div>
<div>

<div class="card card-pink">

### 💡 実践シナリオ

**従来**: git revert + DB手動復元 + 環境変数再設定
**Liquid State**: 「1時間前に戻して」→**全自動復元**

**効果**: デバッグ時間80%削減

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://qiita.com/nakano_teppei_engineer/items/ad0e80264d851c0dd5dc">Qiita: 次世代IDE</a> | <a href="https://nobdata.co.jp/report/creative_ai/03/">NOB DATA</a>
</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">lightbulb</span> 実践プロンプト集（1/2）：基本〜中級

<div class="cols">
<div>

<div class="card card-blue">

### 🎯 基本レベル

「Next.jsでTodoアプリ作成。モダンデザインで動作確認まで」

### ⚙️ ファイル操作

「src/内の未使用import文を削除」
「コンポーネントをTS厳格モードに対応」

</div>

</div>
<div>

<div class="card card-pink">

### 🔍 中級レベル

「コードベース分析してボトルネック特定。改善案3つ提示後、実装」

### 🧪 テスト

「この関数のユニットテストを作成。エッジケースも網羅」

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://dev.classmethod.jp/articles/google-antigravity-five-tips/">DevelopersIO</a> | <a href="https://www.kyoukasho.net/entry/Antigravity-tips">AI社長のブログ</a>
</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">rocket</span> 実践プロンプト集（2/2）：上級

<div class="cols">
<div>

<div class="card card-blue">

### 🚀 GitHub連携

「Issue #123を読み取り要件定義作成。Planning Modeで実装計画→実装→テスト→PR作成→レビュー追加」

</div>

</div>
<div>

<div class="card card-pink">

### 📊 分析 + 実装

「GA4で直帰率高ページ特定→原因分析→改善→A/Bテスト追加」

### 🎨 デザイン

「このデザイン（SS添付）を再現。Nano Bananaで画像も生成」

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://zenn.dev/emp_tech_blog/articles/automate-issue-to-pr-with-antigravity-and-mcp">Zenn: GitHub自動化</a> | <a href="https://graphbooth.com/posts/2025-11-30-antigravity-mcp-ga4">Graphbooth: GA4統合</a>
</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange">security</span> セキュリティのベストプラクティス

<div class="cols-3">
<div>

<div class="card card-blue">

### 🔒 MCP設定

- mcp_config.json / .env を .gitignore に追加
- トークン最小権限・定期ローテーション

</div>

</div>
<div>

<div class="card card-pink">

### ✅ Review Policy

削除/権限変更/外部通信/Git操作は必ずレビュー

</div>

</div>
<div>

<div class="card card-green">

### 📋 Terminal Allowlist

自動OK: ls, cat, grep
確認必須: rm, git push

</div>

</div>
</div>

<div class="card card-lav" style="margin-top:16px;">
<strong>⚠️ 重要</strong>: MCP連携時は、外部システムへのアクセス権限が拡大するため、特に慎重な権限設計が必要
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://manabinoba.blog/google-antigravity-guide/">学べるブログ: セキュリティ設計</a> | <a href="https://note.com/sawahotaru/n/n1b48c673663d">note: MCP設計</a>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">hub</span> エコシステム・コミュニティ

<div class="cols">
<div>

<div class="card card-blue">

### 📚 公式リソース

- 公式サイト: antigravity.google
- Google Codelabs / Developers Blog

</div>

<div class="card card-green" style="margin-top:10px;">

### 🛠️ 拡張機能

Chrome拡張（Browser Agent）、Quota Viewer、Cockpit

</div>

</div>
<div>

<div class="card card-pink">

### 🌐 日本語コミュニティ

- Qiita: 活用事例・TIPS多数
- Zenn: 技術解説記事
- note: 実践レポート

公式Discordコミュニティも活発

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://antigravity.google">公式サイト</a> | <a href="https://qiita.com">Qiita</a> | <a href="https://zenn.dev">Zenn</a> | <a href="https://note.com">note</a>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">compare</span> 競合比較マトリクス

| 機能 | Antigravity | Cursor | VS Code |
|------|-------------|--------|---------|
| **AI Model** | Gemini 3 Pro | Claude/GPT-4 | GPT-4 |
| **Agent** | ◎ 完全自律 | ○ 半自律 | △ 補助 |
| **Browser** | ◎ | × | × |
| **MCP** | ◎ | △ | × |
| **Multi-Agent** | ◎ | × | × |


<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://dad-union.com/google-antigravity-ai-editor">DAD UNION</a> | <a href="https://manabinoba.blog/google-antigravity-guide/">学べるブログ</a>
</div>

---

<!-- _class: bg-pink -->

# <span class="ms ms-lg c-pink">trending_up</span> ロードマップ・今後の展開

<div class="cols">
<div>

<div class="card card-blue">

### 🚀 2026年予定

- Gemini 3.1 Pro対応（2月）
- Enterprise版（春）
- BYOK（夏）
- Team Collaboration（秋）

</div>

<div class="card card-green" style="margin-top:10px;">

### 🔮 将来の可能性

- マルチモーダル強化（音声・動画）
- クラウドネイティブ化
- AIペアプログラミング

</div>

</div>
<div>

<div class="card card-pink">

### 💡 注目トレンド

**エージェント型IDE**: 2025黎明期→2026普及期→2027標準化予測

**開発者の役割**: コーディング→設計・判断へシフト

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/">Google Developers Blog</a>
</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">school</span> 学習リソース・参考文献

<div class="cols">
<div>

<div class="card card-blue">

### 📖 初心者向け

Google Codelabs / G-gen Tech Blog / 窓の杜

</div>

<div class="card card-green" style="margin-top:10px;">

### 🎓 中級者向け

Qiita完全攻略ガイド / DevelopersIO / AI社長のブログ

</div>

</div>
<div>

<div class="card card-pink">

### 🚀 上級者向け

NOB DATA / Graphbooth / Zenn / HackerNoon

</div>

<div class="card card-orange" style="margin-top:10px;">

### 🌐 公式

Google Developers Blog / Gemini Blog

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 上記リンク先が主要な学習リソースです
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">quiz</span> よくある質問（FAQ）

<div class="cols">
<div>

<div class="card card-blue">

**Q1**: CursorやWindsurfとの併用は可能？
**A**: 可能。プロジェクトごとに使い分け

**Q2**: オフラインで使える？
**A**: 不可。インターネット接続必須

**Q3**: 商用利用は可能？
**A**: 可能。利用規約を要確認

</div>

</div>
<div>

<div class="card card-green">

**Q4**: VS Code拡張機能は使える？
**A**: 大部分が互換性あり

**Q5**: エージェントが暴走したら？
**A**: Planning Modeでレビュー必須

**Q6**: プライベートリポジトリも対応？
**A**: 対応。認証情報は安全に管理

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://qiita.com/akira_papa_AI/items/0acf2679e4ce9f7fb153">Qiita: 完全攻略ガイド</a> | <a href="https://dev.classmethod.jp/articles/google-antigravity-five-tips/">DevelopersIO</a>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">emoji_objects</span> 開発効率を最大化する10のコツ

<div class="cols">
<div>

<div class="card card-blue">

1. Planning Modeを基本に（90%推奨）
2. モデル使い分け（設計=High、実装=Low）
3. GEMINI.mdで統一
4. Skillsで再利用
5. MCPで文脈統合

</div>

</div>
<div>

<div class="card card-pink">

6. 複数エージェント活用
7. Browser Agentでデバッグ
8. Artifactsを必ずレビュー
9. ショートカット活用（Cmd/Ctrl+E, I, L）
10. コミュニティで学ぶ

</div>

</div>
</div>

<div style="margin-top:20px; font-size:12px; color:#9b82b5;">
📚 出典: <a href="https://dev.classmethod.jp/articles/google-antigravity-five-tips/">DevelopersIO</a> | <a href="https://www.kyoukasho.net/entry/Antigravity-tips">AI社長のブログ</a> | <a href="https://qiita.com/akira_papa_AI/items/0acf2679e4ce9f7fb153">Qiita</a>
</div>

---

<!-- _class: lead -->

<div class="center">

<div style="font-size: 96px; margin-bottom: 24px;">🚀</div>

<h1 style="font-size: 56px; font-weight: 900; margin-bottom: 32px; color: #3a2e4a;">Google Antigravityで<br>開発の未来を体験しよう</h1>

<div class="cols" style="max-width: 900px; margin: 40px auto;">
<div>

<div class="card card-blue">

### 🎯 今日から始めよう

公式サイトからダウンロード→GEMINI.md設定→Planning Modeで開発開始

</div>

</div>
<div>

<div class="card card-green">

### 🚀 次のステップ

MCP統合→複数エージェント→Browser Agent→コミュニティ参加

</div>

</div>
</div>

<div style="margin-top: 48px; font-size: 20px; color: #6a5580;">
<strong>「コーディング」から「クリエイション」へ</strong><br>
<span style="font-size: 18px; color: #9b82b5;">AIエージェントと共に、開発の新時代を切り拓こう</span>
</div>

</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">link</span> リンク集

<div class="cols">
<div>

<div class="card card-blue">

### 🌐 公式

antigravity.google / Google Developers Blog / Codelabs

</div>

<div class="card card-green" style="margin-top:10px;">

### 📚 日本語記事

Qiita完全攻略 / DevelopersIO / AI社長のブログ

</div>

</div>
<div>

<div class="card card-pink">

### 🔧 実践ガイド

G-gen / Graphbooth / Zenn

</div>

<div class="card card-orange" style="margin-top:10px;">

### 🌍 海外記事

HackerNoon / DEV Community

</div>

</div>
</div>

