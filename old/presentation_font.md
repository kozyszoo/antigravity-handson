---
marp: true
theme: default
paginate: true
backgroundColor: #faf5ff
color: #3a3a5c
style: |
  /* フォント読み込み: Noto Sans JP / JetBrains Mono / Material Symbols */
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&family=JetBrains+Mono:wght@400;700&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&display=swap');

  /* ========================================
     パステルカラーパレット
     - Blue:     #a8d8ea / #6daad8
     - Pink:     #f6c6ea / #e08ac0
     - Green:    #c1e6c0 / #6bb86a
     - Orange:   #ffe0ac / #e0a050
     - Lavender: #d5c6e0 / #9b82b5
     - Text:     #3a3a5c
     ======================================== */

  /* Material Symbols 基本設定（大きめ表示） */
  .material-symbols-outlined {
    font-family: 'Material Symbols Outlined';
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    font-size: 40px;
    vertical-align: middle;
    margin-right: 6px;
    display: inline-block;
  }
  .ms { font-family: 'Material Symbols Outlined'; font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; font-size: 38px; vertical-align: middle; margin-right: 6px; }
  .ms-lg { font-size: 50px; }
  .ms-xl { font-size: 64px; }
  .ms-hero { font-size: 96px; }
  .c-blue { color: #6daad8; }
  .c-pink { color: #e08ac0; }
  .c-green { color: #6bb86a; }
  .c-orange { color: #e0a050; }
  .c-lav { color: #9b82b5; }

  /* 全スライド共通 */
  section {
    font-family: 'Noto Sans JP', sans-serif;
    background: #faf5ff;
    padding: 40px 60px;
    font-size: 24px;
    line-height: 1.6;
  }

  /* タイトルスライド */
  section.lead {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: #e8ddf4;
  }
  section.lead h1 {
    font-size: 58px;
    font-weight: 900;
    color: #7060a0;
    border: none;
    margin-bottom: 12px;
  }
  section.lead h2 {
    font-size: 30px;
    color: #7a6d90;
    border: none;
    font-weight: 700;
    margin-bottom: 28px;
  }
  section.lead p {
    font-size: 22px;
    color: #9b82b5;
    font-weight: 700;
  }

  /* 背景バリエーションクラス（フラットカラー） */
  section.bg-blue { background: #e0f0fa; }
  section.bg-pink { background: #fdeef6; }
  section.bg-green { background: #eaf6ea; }
  section.bg-orange { background: #fdf4e8; }
  section.bg-lav { background: #efe8f6; }

  /* 見出し */
  h1 {
    font-size: 38px;
    font-weight: 900;
    color: #5a4d78;
    border-bottom: 3px solid #d5c6e0;
    padding-bottom: 8px;
    margin-bottom: 16px;
  }
  h2 {
    font-size: 27px;
    font-weight: 700;
    color: #6a5d88;
    border-bottom: 2px solid #d5c6e0;
    padding-bottom: 6px;
    margin-bottom: 12px;
  }
  h3 {
    font-size: 20px;
    font-weight: 700;
    color: #7a6d90;
    margin-bottom: 8px;
  }

  /* テキスト装飾 */
  strong { color: #8060a8; }
  em { color: #c06888; font-style: normal; font-weight: 700; }
  a { color: #6a90c8; text-decoration: none; border-bottom: 2px solid #a8d8ea; }

  /* コード */
  code {
    background: rgba(168, 216, 234, 0.25);
    padding: 2px 6px;
    border-radius: 6px;
    color: #5070a0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 18px;
  }
  pre {
    background: #2d2640;
    color: #e8e0f0;
    padding: 14px 18px;
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(90, 70, 120, 0.12);
    margin: 10px 0;
  }
  pre code { background: transparent; color: #e8e0f0; font-size: 16px; border: none; }

  /* テーブル */
  table { border-collapse: collapse; width: 100%; margin: 10px 0; border-radius: 10px; overflow: hidden; box-shadow: 0 3px 12px rgba(90,70,120,0.08); }
  th { background: #b8a8d8; color: #fff; padding: 8px 14px; font-weight: 700; font-size: 18px; text-align: center; }
  td { padding: 7px 14px; border-bottom: 1px solid #e8e0f0; background: rgba(255,255,255,0.7); font-size: 17px; }
  tr:last-child td { border-bottom: none; }

  /* 引用 */
  blockquote {
    border-left: 5px solid #c8b8e0;
    padding: 12px 18px;
    background: rgba(213, 198, 224, 0.18);
    border-radius: 10px;
    font-size: 20px;
    color: #6a5d88;
    font-weight: 700;
    margin: 10px 0;
  }

  /* リスト */
  ul, ol { padding-left: 24px; margin: 6px 0; }
  li { margin: 4px 0; }
  li::marker { color: #b0a0c8; }

  /* カラムレイアウト */
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 8px 0; }
  .cols-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin: 8px 0; }

  /* カードパーツ */
  .card { border-radius: 12px; padding: 14px 18px; margin: 4px 0; box-shadow: 0 3px 12px rgba(90,70,120,0.06); }
  .card-blue { background: rgba(168,216,234,0.28); border: 2px solid #a8d8ea; }
  .card-pink { background: rgba(246,198,234,0.28); border: 2px solid #f6c6ea; }
  .card-green { background: rgba(193,230,192,0.28); border: 2px solid #c1e6c0; }
  .card-orange { background: rgba(255,224,172,0.28); border: 2px solid #ffe0ac; }
  .card-lav { background: rgba(213,198,224,0.28); border: 2px solid #d5c6e0; }

  /* ハイライトボックス */
  .hl { background: rgba(213,198,224,0.18); padding: 16px 20px; border-radius: 12px; border: 2px solid #d0c0e4; margin: 8px 0; }

  /* ノート・成功・警告ボックス */
  .note { background: rgba(255,224,172,0.28); border-left: 5px solid #e0a050; padding: 10px 14px; border-radius: 8px; margin: 8px 0; color: #7a5820; font-weight: 700; }
  .ok { background: rgba(193,230,192,0.32); border-left: 5px solid #80c080; padding: 10px 14px; border-radius: 8px; margin: 8px 0; color: #3a6a3a; }
  .warn { background: rgba(246,198,234,0.28); border-left: 5px solid #e090b8; padding: 10px 14px; border-radius: 8px; margin: 8px 0; color: #8a3060; }

  /* ステップ番号バッジ */
  .num { display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 50%; background: #b8a8d8; color: #fff; font-weight: 900; font-size: 18px; margin-right: 8px; flex-shrink: 0; }

  /* 矢印 */
  .arrow { text-align: center; font-size: 22px; color: #b0a0c8; margin: 4px 0; }

  /* ページ番号 */
  section::after { color: #b0a0c8; font-weight: 700; }

  /* テキストユーティリティ */
  .center { text-align: center; }
  .sm { font-size: 14px; color: #9a8aad; }
  .gap { display: flex; flex-wrap: wrap; gap: 10px; margin: 6px 0; }
---



<!-- _class: lead -->

<span class="ms ms-hero c-lav">rocket_launch</span>

# Google Antigravity

## 次世代AIエージェント統合開発環境

重力から解放された開発体験へ

Vibe Codingで創造性を最大化する

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">list_alt</span> 本日のアジェンダ

<div class="card card-blue" style="padding:10px 10px;margin:6px 0; padding-bottom:px">
<h3 style="margin-bottom:4px; margin-top:0px;"><span class="ms c-blue">flag</span> 学習目標</h3>
<strong>Antigravityの魅力を体感し、明日から使えるスキルを身につける</strong>
</div>

| 時間 | 内容 | 詳細 |
|:---:|:---|:---|
| **5分** | <span class="ms c-pink">help</span> 課題提起 | 従来の開発の問題点 |
| **10分** | <span class="ms c-blue">target</span> Antigravityとは | 基本概念と革新性 |
| **15分** | <span class="ms c-green">build</span> 技術詳細 | Architecture / MCP / Skills |
| **20分** | <span class="ms c-lav">rocket_launch</span> Vibe Coding | 実践デモ |
| **5分** | <span class="ms c-orange">auto_awesome</span> まとめ | 次のステップ |
| **15分** | <span class="ms c-pink">forum</span> Q&A | 質問・ディスカッション |

<p class="sm center" style="margin-top:6px;"><span class="ms" style="font-size:14px;">schedule</span> 合計約70分</p>

---

<!-- _class: bg-pink -->

# <span class="ms ms-lg c-pink">sentiment_dissatisfied</span> こんな経験ありませんか？

<div class="cols">

<div class="warn">
<h3><span class="ms c-pink">warning</span> 従来の開発でよくある悩み</h3>
<p>環境構築だけで<strong>半日</strong>が消える。ボイラープレートの記述、単調なリファクタリング、ドキュメント整備、デザイン素材の準備…。本質的な開発に集中できないまま時間だけが過ぎていく。</p>
</div>

<div class="ok">
<h3><span class="ms c-green">check_circle</span> Antigravityなら</h3>
<p>環境構築もテンプレートも<strong>AIが自動で処理</strong>。リファクタリング、ドキュメント生成、画像生成まですべて自律的に実行。創造的な作業だけに集中できます。</p>
</div>

</div>

<div class="note">
<span class="ms c-orange">lightbulb</span> 開発時間を<strong>70%削減</strong>し、創造性を最大化するのがAntigravityの目標です。
</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">target</span> Google Antigravityとは？

> 2025年11月にGoogleが発表した革新的なIDE。従来の「コード補完ツール」から**「自律的AIパートナー」**へのパラダイムシフトを実現しています。

<div class="hl">
<h2><span class="ms c-lav">auto_awesome</span> 3つの革新ポイント</h2>

<div class="cols">

<div>
<h3><span class="num">1</span> Agent-First Architecture</h3>
<p>AIが単なるツールではなく、タスクの計画・実行・検証までを担う<strong>自律的なパートナー</strong>として機能します。</p>
</div>

<div>
<h3><span class="num">2</span> Dual View System</h3>
<p><strong>Manager View</strong>（司令塔）でエージェントを指揮し、<strong>Editor View</strong>（作業場）でコードを書く。</p>
</div>

</div>

<h3><span class="num">3</span> Multi-Model Support</h3>
Gemini 3 Pro、Claude、Nano Bananaなど複数のAIモデルを目的に応じて使い分けられます。

</div>

---

# <span class="ms ms-lg c-blue">compare</span> 従来のAIツールとの違い

| 項目 | GitHub Copilot | Cursor | **Antigravity** |
|:---|:---:|:---:|:---:|
| **役割** | コード補完 | AI編集支援 | **自律エージェント** |
| **タスク実行** | 手動 | 半自動 | **完全自律** |
| **複数モデル** | <span class="ms c-pink">close</span> | 一部 | <span class="ms c-green">check_circle</span> |
| **ブラウザ操作** | <span class="ms c-pink">close</span> | <span class="ms c-pink">close</span> | <span class="ms c-green">check_circle</span> |
| **画像生成** | <span class="ms c-pink">close</span> | <span class="ms c-pink">close</span> | <span class="ms c-green">check_circle</span> |
| **MCP対応** | <span class="ms c-pink">close</span> | 限定的 | <span class="ms c-green">check_circle</span> |

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">spa</span> Antigravityの哲学

<div class="hl">
<h2><span class="ms c-lav">feather</span> 「重力からの解放」</h2>

開発者は<strong>「何を創るか（What）」に集中すべき</strong>。環境構築、定型作業、ドキュメント、デザイン素材──これらはすべてAIに任せる。

<div class="gap">
<div class="card card-blue" style="flex:1;text-align:center;"><span class="ms c-blue">settings</span> 環境構築→AIへ</div>
<div class="card card-pink" style="flex:1;text-align:center;"><span class="ms c-pink">repeat</span> 定型作業→AIへ</div>
<div class="card card-orange" style="flex:1;text-align:center;"><span class="ms c-orange">description</span> ドキュメント→AIへ</div>
<div class="card card-green" style="flex:1;text-align:center;"><span class="ms c-green">palette</span> デザイン→AIへ</div>
</div>

<p class="center" style="font-size:24px;font-weight:900;color:#8060a8;margin-top:10px;">これが Vibe Coding の真髄</p>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">account_tree</span> Agent-First Architecture

<div class="card card-lav center" style="padding:10px 16px;">

<strong>開発者</strong> が自然言語で指示
<div class="arrow">↓</div>
<span class="ms c-blue">dashboard</span> <strong>Manager View</strong> が受け取り、各エージェントへ分配
<div class="arrow">↓</div>
<div class="gap" style="justify-content:center;">
<div class="card card-blue"><span class="ms c-blue">fact_check</span> Planner</div>
<div class="card card-green"><span class="ms c-green">code</span> Coder</div>
<div class="card card-pink"><span class="ms c-pink">brush</span> Designer</div>
<div class="card card-orange"><span class="ms c-orange">rate_review</span> Reviewer</div>
</div>
<div class="arrow">↓</div>
<span class="ms c-lav">inventory_2</span> <strong>Artifacts</strong>（成果物）として統合
</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">view_sidebar</span> Dual View System

<div class="cols">

<div class="card card-lav">
<h3><span class="ms c-lav">supervisor_account</span> Manager View（司令塔）</h3>
<p>チャット形式で自然言語のタスク依頼ができるインターフェース。エージェントの動作をリアルタイムで監視・管理し、Artifacts（成果物）もここで確認できます。</p>
</div>

<div class="card card-blue">
<h3><span class="ms c-blue">terminal</span> Editor View（作業場）</h3>
<p>VS Code互換のエディタ。<code>Cmd+K</code> でインライン編集、リアルタイムプレビューに対応。従来の手動開発スタイルとAIを柔軟に使い分けられます。</p>
</div>

</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange">model_training</span> Multi-Model Support

| モデル | 得意分野 | 使用シーン |
|:---|:---|:---|
| **Gemini 3 Pro** | 総合力・論理的思考 | メイン開発、複雑なロジック |
| **Claude Sonnet 4.5** | 文脈理解・自然な文章 | ドキュメント、要件定義 |
| **Nano Banana** | 画像生成・UIデザイン | アイコン、OGP、ヒーロー画像 |
| **Gemini 2.5 Computer Use** | ブラウザ操作 | Web検索、E2Eテスト |

<p class="center" style="margin-top:12px;"><strong>目的に応じてモデルが自動で選ばれます</strong></p>

---

<!-- _class: bg-pink -->

# <span class="ms ms-lg c-orange">image</span> Nano Banana（画像生成AI）

<div class="hl">

### <span class="ms c-pink">brush</span> エンジニアがデザイン素材を即座に用意

```
「このヘッダーに合う背景画像を生成して（Nano Banana）」
```

<div class="arrow">↓</div>

生成された画像が `public/images/` に自動保存・配置されます。

<div class="gap" style="margin-top:12px;">
<div class="card card-green" style="flex:1;"><span class="ms c-green">speed</span> デザイナーを待つ必要なし</div>
<div class="card card-blue" style="flex:1;"><span class="ms c-blue">bolt</span> プロトタイプが高速化</div>
<div class="card card-orange" style="flex:1;"><span class="ms c-orange">thumb_up</span> イメージ通りの素材を入手</div>
</div>

</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">cable</span> MCP（Model Context Protocol）

> AIエージェントを外部ツールに接続するための標準規格です。

### <span class="ms c-blue">extension</span> 接続可能なツール例

<div class="gap">
<div class="card card-blue" style="flex:1;"><span class="ms c-blue">language</span> <strong>Browser</strong><br>Puppeteer / Playwright</div>
<div class="card card-green" style="flex:1;"><span class="ms c-green">folder</span> <strong>Filesystem</strong><br>ローカルファイル操作</div>
<div class="card card-lav" style="flex:1;"><span class="ms c-lav">code</span> <strong>GitHub</strong><br>リポジトリ操作</div>
</div>
<div class="gap">
<div class="card card-orange" style="flex:1;"><span class="ms c-orange">storage</span> <strong>PostgreSQL</strong><br>DB直接参照</div>
<div class="card card-pink" style="flex:1;"><span class="ms c-pink">chat</span> <strong>Slack</strong><br>通知・連携</div>
<div class="card card-blue" style="flex:1;"><span class="ms c-blue">cloud</span> <strong>Google Drive</strong><br>ドキュメント管理</div>
</div>

<p class="center"><strong>開発環境を自由に拡張できます</strong></p>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">description</span> GEMINI.md（設定ファイル）

プロジェクトルートに配置して、<strong>エージェントにプロジェクトの文脈を教える</strong>役割を持ちます。

```markdown
# プロジェクト設定
## 基本ルール
- 常に日本語で応答してください
- コードには必ずコメントを入れてください
## 技術スタック
- React + TypeScript / TailwindCSS / Vite
## コーディング規約
- 変数名: camelCase / ファイル名: kebab-case
```

<div class="note">
<span class="ms c-orange">lightbulb</span> このファイルを書くだけで、AIがプロジェクトの方針やルールを理解して動いてくれます。
</div>

---

# <span class="ms ms-lg c-blue">psychology</span> Agent Skills

エージェントに特定の<strong>「能力」をパッケージとして追加</strong>できる仕組みです。

<div class="card card-lav">
<h3><span class="ms c-lav">folder_special</span> .agent/skills/code-review/SKILL.md</h3>

```markdown
---
name: code-review
description: コードの品質レビューを行う
---
# コードレビュー手順
1. 指定ファイルを読み込む
2. セキュリティ脆弱性を確認
3. 変数名・パフォーマンスをチェック
```

</div>

<p class="center" style="font-size:22px;font-weight:700;color:#8060a8;margin-top:10px;">「@code-review して」と頼むだけで実行されます</p>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange">payments</span> 料金プラン

<div class="cols-3">

<div class="card card-green center">
<span class="ms ms-xl c-green">volunteer_activism</span>
<h3>Free</h3>
<p style="font-size:28px;font-weight:900;color:#6bb86a;">無料</p>
<p class="sm">Gemini 3 Pro（制限あり）<br>Nano Banana（月50枚）<br>ローカルMCP</p>
</div>

<div class="card card-blue center">
<span class="ms ms-xl c-blue">star</span>
<h3>Pro</h3>
<p style="font-size:28px;font-weight:900;color:#6daad8;">$19/月</p>
<p class="sm">Gemini 3 Pro（優先）<br>Claude Sonnet 4.5<br>Nano Banana（無制限）<br>クラウドMCP</p>
</div>

<div class="card card-lav center">
<span class="ms ms-xl c-lav">business</span>
<h3>Enterprise</h3>
<p style="font-size:28px;font-weight:900;color:#9b82b5;">要相談</p>
<p class="sm">チーム共有Artifacts<br>Enterpriseセキュリティ<br>カスタムモデル</p>
</div>

</div>

<p class="center" style="margin-top:12px;"><strong>学生でもFreeプランで十分に活用できます</strong></p>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">download</span> インストール方法

<div class="card card-blue">

<p><span class="num">1</span> <strong>公式サイトへアクセス</strong> ― <a href="https://build.google.com/antigravity">build.google.com/antigravity</a></p>

<p><span class="num">2</span> <strong>ダウンロード</strong> ― macOS / Windows / Linux に対応</p>

<p><span class="num">3</span> <strong>ログイン</strong> ― Googleアカウントでサインインするだけ</p>

</div>

<p class="center" style="font-size:24px;font-weight:700;color:#5a4d78;margin-top:16px;">
<span class="ms c-green">timer</span> 5分で開発環境が整います
</p>

---

# <span class="ms ms-lg c-lav">menu_book</span> ハンズオン構成

<div class="note">
<span class="ms c-orange">lightbulb</span> <strong>前半</strong>で早めにVibe Codingを体験 → <strong>後半</strong>で拡張機能を学ぶ流れです。
</div>

| No | 内容 | 所要時間 |
|:---:|:---|:---:|
| <span class="num">1</span> | 環境セットアップ | 15分 |
| <span class="num">2</span> | GEMINI.md 設定 | 15分 |
| <span class="num">3</span> | **Vibe Coding 基礎編** | 20分 |
| <span class="num">4</span> | MCP 接続 | 20分 |
| <span class="num">5</span> | Agent Skills 作成 | 20分 |
| <span class="num">6</span> | **Vibe Coding 発展編** | 30分 |

<p class="sm center">合計：約2時間</p>

---

<!-- _class: lead -->

<span class="ms ms-hero c-lav">play_circle</span>

# 実践！Vibe Coding デモ

## 「AI Coffee Shop」ランディングページを作ってみよう

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">movie</span> Vibe Coding デモ ― Step 1

### <span class="ms c-green">create_new_folder</span> プロジェクト作成

```
「Vite + Reactで、モダンで美しい
『AI Coffee Shop』のランディングページを作って。
TailwindCSSを使って。」
```

<div class="arrow">↓</div>

<div class="ok">
Antigravityが自動的に <code>npx create-vite</code> を実行し、TailwindCSSの設定や基本構造を一気に生成します。
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">movie</span> Vibe Coding デモ ― Step 2

### <span class="ms c-blue">edit_note</span> キャッチコピーと構成（Gemini 3 Pro）

```
「未来的で落ち着くコーヒーショップのキャッチコピーと、
LPのセクション構成を考えて（Gemini 3 Pro）」
```

<div class="arrow">↓</div>

<div class="card card-blue">
<p><span class="ms c-blue">format_quote</span> キャッチコピー：<strong>「未来と伝統が溶け合う、至福の一杯」</strong></p>
<p style="margin-top:8px;"><span class="ms c-blue">view_list</span> セクション構成：Hero → Concept → Menu → Access → Contact</p>
</div>

---

<!-- _class: bg-pink -->

# <span class="ms ms-lg c-pink">movie</span> Vibe Coding デモ ― Step 3

### <span class="ms c-pink">image</span> ビジュアル生成（Nano Banana）

```
「『近未来的なカフェの店内、ネオンライトと植物が調和している、
4K、リアル』な画像を生成して。
ファイル名は hero-bg.webp で public フォルダに保存して。
（Nano Banana）」
```

<div class="arrow">↓</div>

<div class="ok">
数秒で高品質な画像が生成され、<strong>プロジェクトに自動配置</strong>されます。
</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">movie</span> Vibe Coding デモ ― Step 4

### <span class="ms c-lav">code</span> 実装 & プレビュー

```
「生成した画像を背景に使って、Heroセクションを実装して。
文字は白で読みやすく、グラスモーフィズムなデザインで。」
```

<div class="arrow">↓</div>

<div class="card card-lav">
AIが背景画像の配置、グラスモーフィズム効果、レスポンシブ対応、アニメーション追加まで一括で実装します。
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">movie</span> Vibe Coding デモ ― Step 5

### <span class="ms c-green">cloud_upload</span> デプロイ準備

```
「これで完成。ビルドしてデプロイの準備をして。」
```

<div class="arrow">↓</div>

<div class="ok">
AIが <code>npm run build</code> を実行し、最適化チェック後、Vercel / Netlify 向けのデプロイコマンドも提示してくれます。
</div>

<p class="center" style="font-size:24px;font-weight:900;color:#3a6a3a;margin-top:12px;">
<span class="ms c-green">timer</span> わずか10分で本格的なLPが完成！
</p>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange">auto_awesome</span> Vibe Codingの魅力

<div class="hl">

<div class="cols">

<div>
<h3><span class="ms c-blue">target</span> 「What」に集中できる</h3>
<p>「どうやって実装するか」ではなく<strong>「何を創りたいか」</strong>を考える時間が増えます。</p>
</div>

<div>
<h3><span class="ms c-green">speed</span> 圧倒的な開発速度</h3>
<p>従来 3.5 時間かかっていた作業が<strong>わずか10分</strong>に短縮されます。</p>
</div>

</div>

### <span class="ms c-pink">palette</span> デザインとコードの統合

エンジニアが自分でデザイン素材を用意できるため、デザイナーとの待ち時間がなくなります。

</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav">change_history</span> 開発フローの変化

<div class="cols">

<div class="card card-pink">
<h3><span class="ms c-pink">hourglass_top</span> 従来の開発フロー</h3>
<p>要件定義 → 設計 → 環境構築 → 実装 → テスト → デバッグ → ドキュメント → デプロイ</p>
<p class="sm" style="color:#8a3060;margin-top:8px;">多くのステップに時間がかかる</p>
</div>

<div class="card card-green">
<h3><span class="ms c-green">bolt</span> Antigravityの開発フロー</h3>
<p><span class="num">1</span> 要件定義</p>
<p><span class="num">2</span> AIに指示</p>
<p><span class="num">3</span> 完成！</p>
<p style="font-weight:700;color:#3a6a3a;margin-top:8px;">時間のかかる作業をAIが自律的に処理</p>
</div>

</div>

---

# <span class="ms ms-lg c-lav">summarize</span> Antigravityの強み まとめ

<div class="cols-3">

<div class="card card-blue center">
<span class="ms ms-xl c-blue">smart_toy</span>
<p style="font-weight:700;margin-top:8px;">自律エージェント</p>
<p class="sm">計画・実行・検証</p>
</div>

<div class="card card-pink center">
<span class="ms ms-xl c-pink">image</span>
<p style="font-weight:700;margin-top:8px;">画像生成</p>
<p class="sm">Nano Banana</p>
</div>

<div class="card card-green center">
<span class="ms ms-xl c-green">cable</span>
<p style="font-weight:700;margin-top:8px;">拡張性</p>
<p class="sm">MCP連携</p>
</div>

</div>

<div class="cols-3">

<div class="card card-orange center">
<span class="ms ms-xl c-orange">model_training</span>
<p style="font-weight:700;margin-top:8px;">マルチモデル</p>
<p class="sm">適材適所</p>
</div>

<div class="card card-lav center">
<span class="ms ms-xl c-lav">tune</span>
<p style="font-weight:700;margin-top:8px;">カスタマイズ</p>
<p class="sm">GEMINI.md / Skills</p>
</div>

<div class="card card-green center">
<span class="ms ms-xl c-green">savings</span>
<p style="font-weight:700;margin-top:8px;">無料で始められる</p>
<p class="sm">Freeプラン対応</p>
</div>

</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue">school</span> 学習リソース

<div class="cols-3">

<div class="card card-blue center">
<span class="ms ms-xl c-blue">article</span>
<h3>公式ドキュメント</h3>
<p class="sm"><a href="https://build.google.com/antigravity/docs">build.google.com/antigravity/docs</a></p>
</div>

<div class="card card-lav center">
<span class="ms ms-xl c-lav">groups</span>
<h3>コミュニティ</h3>
<p class="sm">Discord: Antigravity Developers<br>GitHub: antigravity-examples</p>
</div>

<div class="card card-pink center">
<span class="ms ms-xl c-pink">play_circle</span>
<h3>チュートリアル</h3>
<p class="sm">YouTube公式チャンネル<br>Qiita #Antigravity</p>
</div>

</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green">rocket_launch</span> 今日から始めよう！

<div class="hl">

<p><span class="num">1</span> <strong>インストール</strong> ― <a href="https://build.google.com/antigravity">build.google.com/antigravity</a></p>

<p><span class="num">2</span> <strong>ハンズオン実践</strong> ― 本日の資料を参考に5つのステップを体験</p>

<p><span class="num">3</span> <strong>自分のプロジェクトで活用</strong> ― GEMINI.md、Skills、MCPを駆使して開発を加速</p>

</div>

<p class="center" style="font-size:26px;font-weight:900;color:#5a4d78;margin-top:16px;">重力から解放された開発体験を、今すぐ！</p>

---

<!-- _class: lead -->

<span class="ms ms-hero c-lav">favorite</span>

# ありがとうございました！

## 質問・ディスカッションタイム

Google Antigravityで、開発の未来を体験しましょう！

---

# <span class="ms ms-lg c-blue">attach_file</span> 補足資料

<div class="cols">

<div class="card card-blue">
<h3><span class="ms c-blue">link</span> 参考リンク</h3>
<p>公式サイト：<a href="https://build.google.com/antigravity">build.google.com/antigravity</a></p>
<p>ドキュメント：<a href="https://build.google.com/antigravity/docs">build.google.com/antigravity/docs</a></p>
<p>GitHub：<a href="https://github.com/google/antigravity-examples">antigravity-examples</a></p>
</div>

<div class="card card-lav">
<h3><span class="ms c-lav">inventory</span> ハンズオン資料</h3>
<p>各ステップの詳細は <code>handson/</code> フォルダを参照してください。</p>
</div>

</div>
