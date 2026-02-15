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

<img src="icons/lav/rocket_launch.svg" width="96" style="vertical-align: -0.2em; margin-right: 6px;">

# Google Antigravity

## 次世代AIエージェント統合開発環境

重力から解放された開発体験へ

Vibe Codingで創造性を最大化する

---

<!-- _class: bg-blue -->

# <img src="icons/blue/list_alt.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> 本日のアジェンダ

<div class="card card-blue" style="padding:10px 10px;margin:6px 0; padding-bottom:px">
<h3 style="margin-bottom:4px; margin-top:0px;"><img src="icons/blue/flag.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 学習目標</h3>
<strong>Antigravityの魅力を体感し、明日から使えるスキルを身につける</strong>
</div>

| 時間 | 内容 | 詳細 |
|:---:|:---|:---|
| **5分** | <img src="icons/pink/help.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 課題提起 | 従来の開発の問題点 |
| **10分** | <img src="icons/blue/target.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Antigravityとは | 基本概念と革新性 |
| **15分** | <img src="icons/green/build.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 技術詳細 | Architecture / MCP / Skills |
| **20分** | <img src="icons/lav/rocket_launch.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Vibe Coding | 実践デモ |
| **5分** | <img src="icons/orange/auto_awesome.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> まとめ | 次のステップ |
| **15分** | <img src="icons/pink/forum.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Q&A | 質問・ディスカッション |

<p class="sm center" style="margin-top:6px;"><img src="icons/black/schedule.svg" width="14" style="vertical-align: -0.2em; margin-right: 6px;"> 合計約70分</p>

---

<!-- _class: bg-pink -->

# <img src="icons/pink/sentiment_dissatisfied.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> こんな経験ありませんか？

<div class="cols">

<div class="warn">
<h3><img src="icons/pink/warning.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 従来の開発でよくある悩み</h3>
<p>環境構築だけで<strong>半日</strong>が消える。ボイラープレートの記述、単調なリファクタリング、ドキュメント整備、デザイン素材の準備…。本質的な開発に集中できないまま時間だけが過ぎていく。</p>
</div>

<div class="ok">
<h3><img src="icons/green/check_circle.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Antigravityなら</h3>
<p>環境構築もテンプレートも<strong>AIが自動で処理</strong>。リファクタリング、ドキュメント生成、画像生成まですべて自律的に実行。創造的な作業だけに集中できます。</p>
</div>

</div>

<div class="note">
<img src="icons/orange/lightbulb.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 開発時間を<strong>70%削減</strong>し、創造性を最大化するのがAntigravityの目標です。
</div>

---

<!-- _class: bg-lav -->

# <img src="icons/lav/target.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Google Antigravityとは？

> 2025年11月にGoogleが発表した革新的なIDE。従来の「コード補完ツール」から**「自律的AIパートナー」**へのパラダイムシフトを実現しています。

<div class="hl">
<h2><img src="icons/lav/auto_awesome.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 3つの革新ポイント</h2>

<div class="cols">

<div>
<h3><span class="num">1</span> Agent-First Architecture</h3>
<p>AIが単なるツールではなく、タスクの計画・実行・検証までを担う<strong>自律的なパートナー</strong>として機能します。</p>
</div>

<div>
<h3><span class="num">2</span> Dual View System</h3>
<p><strong>Agent Manager</strong>（司令塔）でエージェントを指揮し、<strong>Editor View</strong>（作業場）でコードを書く。<code>Cmd+E</code>で切り替え。</p>
</div>

</div>

<h3><span class="num">3</span> Multi-Model Support</h3>
Gemini 3 Pro/Flash、Claude Sonnet/Opus 4.5、Nano Banana Proなど複数のAIモデルを目的に応じて使い分けられます。

</div>

---

# <img src="icons/blue/compare.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> 従来のAIツールとの違い

| 項目 | GitHub Copilot | Cursor | **Antigravity** |
|:---|:---:|:---:|:---:|
| **役割** | コード補完 | AI編集支援 | **自律エージェント** |
| **タスク実行** | 手動 | 半自動 | **完全自律** |
| **複数モデル** | <img src="icons/pink/close.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> | 一部 | <img src="icons/green/check_circle.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> |
| **ブラウザ操作** | <img src="icons/pink/close.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> | <img src="icons/pink/close.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> | <img src="icons/green/check_circle.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> |
| **画像生成** | <img src="icons/pink/close.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> | <img src="icons/pink/close.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> | <img src="icons/green/check_circle.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> |
| **MCP対応** | <img src="icons/pink/close.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> | 限定的 | <img src="icons/green/check_circle.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> |

---

<!-- _class: bg-green -->

# <img src="icons/green/spa.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Antigravityの哲学

<div class="hl">
<h2><img src="icons/lav/feather.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 「重力からの解放」</h2>

開発者は<strong>「何を創るか（What）」に集中すべき</strong>。環境構築、定型作業、ドキュメント、デザイン素材──これらはすべてAIに任せる。

<div class="gap">
<div class="card card-blue" style="flex:1;text-align:center;"><img src="icons/blue/settings.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 環境構築→AIへ</div>
<div class="card card-pink" style="flex:1;text-align:center;"><img src="icons/pink/repeat.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 定型作業→AIへ</div>
<div class="card card-orange" style="flex:1;text-align:center;"><img src="icons/orange/description.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> ドキュメント→AIへ</div>
<div class="card card-green" style="flex:1;text-align:center;"><img src="icons/green/palette.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> デザイン→AIへ</div>
</div>

<p class="center" style="font-size:24px;font-weight:900;color:#8060a8;margin-top:10px;">これが Vibe Coding の真髄</p>
</div>

---

<!-- _class: bg-blue -->

# <img src="icons/blue/account_tree.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Agent-First Architecture

<div class="card card-lav center" style="padding:10px 16px;">

<strong>開発者</strong> が自然言語で指示
<div class="arrow">↓</div>
<img src="icons/blue/dashboard.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>Manager View</strong> が受け取り、各エージェントへ分配
<div class="arrow">↓</div>
<div class="gap" style="justify-content:center;">
<div class="card card-blue"><img src="icons/blue/fact_check.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Planner</div>
<div class="card card-green"><img src="icons/green/code.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Coder</div>
<div class="card card-pink"><img src="icons/pink/brush.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Designer</div>
<div class="card card-orange"><img src="icons/orange/rate_review.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Reviewer</div>
</div>
<div class="arrow">↓</div>
<img src="icons/lav/inventory_2.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>Artifacts</strong>（成果物）として統合
</div>

---

<!-- _class: bg-lav -->

# <img src="icons/lav/view_sidebar.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Dual View System

<div class="cols">

<div class="card card-lav">
<h3><img src="icons/lav/supervisor_account.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Agent Manager（司令塔）</h3>
<p>チャット形式で自然言語のタスク依頼ができるインターフェース。エージェントの動作をリアルタイムで監視・管理し、Artifacts（成果物）もここで確認できます。</p>
</div>

<div class="card card-blue">
<h3><img src="icons/blue/terminal.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Editor View（作業場）</h3>
<p>VS Code互換のエディタ。<code>Cmd+I</code> でCommand（自然言語で指示）、<code>Tab</code> でSupercomplete（コード補完）。AI機能が組み込まれたエディタです。</p>
</div>

</div>

<div class="note">
<img src="icons/orange/lightbulb.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <code>Cmd+E</code> で Agent Manager ↔ Editor を素早く切り替えできます。
</div>

---

<!-- _class: bg-orange -->

# <img src="icons/orange/model_training.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Multi-Model Support

### 🧠 推論モデル（選択可能）

| モデル | 特徴 |
|:---|:---|
| **Gemini 3 Pro** (High/Low) | Google最新。総合力・論理的思考 |
| **Gemini 3 Flash** | 高速レスポンス |
| **Claude Sonnet 4.5** | 文脈理解・自然な文章 |
| **Claude Opus 4.5** | 高精度（Thinkingモード） |
| **GPT-OSS** | OpenAI互換 |

### 🎨 バックグラウンドモデル（自動選択）

| モデル | 役割 |
|:---|:---|
| **Nano Banana Pro** | 画像生成・UIモックアップ |
| **Gemini 2.5 Pro UI Checkpoint** | Browser Subagent（ブラウザ操作） |
| **Gemini 2.5 Flash** | チェックポイント・コンテキスト要約 |

---

<!-- _class: bg-pink -->

# <img src="icons/orange/image.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Nano Banana（画像生成AI）

<div class="hl">

### <img src="icons/pink/brush.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> エンジニアがデザイン素材を即座に用意

```
「このヘッダーに合う背景画像を生成して（Nano Banana）」
```

<div class="arrow">↓</div>

生成された画像が `public/images/` に自動保存・配置されます。

<div class="gap" style="margin-top:12px;">
<div class="card card-green" style="flex:1;"><img src="icons/green/speed.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> デザイナーを待つ必要なし</div>
<div class="card card-blue" style="flex:1;"><img src="icons/blue/bolt.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> プロトタイプが高速化</div>
<div class="card card-orange" style="flex:1;"><img src="icons/orange/thumb_up.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> イメージ通りの素材を入手</div>
</div>

</div>

---

<!-- _class: bg-green -->

# <img src="icons/green/cable.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> MCP（Model Context Protocol）

> AIエージェントを外部ツールに安全に接続するためのオープン標準です。

<div class="cols">

<div>

### <img src="icons/blue/extension.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 2つの主要機能

<div class="card card-blue"><strong>Context Resources</strong>：AIがリアルタイムデータを読み取り（SQLスキーマ、ビルドログ等）</div>
<div class="card card-green"><strong>Custom Tools</strong>：AIがアクションを実行（GitHub Issue作成、Notion検索等）</div>

</div>

<div>

### <img src="icons/lav/extension.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 接続可能なツール例

<div class="gap">
<div class="card card-blue" style="flex:1;"><img src="icons/blue/language.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>Browser</strong><br>Playwright</div>
<div class="card card-green" style="flex:1;"><img src="icons/green/folder.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>Filesystem</strong></div>
<div class="card card-lav" style="flex:1;"><img src="icons/lav/code.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>GitHub</strong></div>
</div>
<div class="gap">
<div class="card card-orange" style="flex:1;"><img src="icons/orange/storage.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>PostgreSQL</strong></div>
<div class="card card-pink" style="flex:1;"><img src="icons/pink/chat.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>Slack</strong></div>
<div class="card card-blue" style="flex:1;"><img src="icons/blue/cloud.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>Context7</strong></div>
</div>

</div>

</div>

<div class="note">
<img src="icons/orange/lightbulb.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> ビルトインの <strong>MCP Store</strong> でGUIから簡単にサーバーを追加・管理できます。
</div>

---

<!-- _class: bg-lav -->

# <img src="icons/lav/description.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Rules / Workflows / GEMINI.md

<div class="cols">

<div>

### <img src="icons/lav/tune.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Rules（ルール）

エージェントの振る舞いを制御する**持続的な指示**。`GEMINI.md` に記述します。

```markdown
# プロジェクト設定
## 基本ルール
- 常に日本語で応答してください
- コードには必ずコメントを入れてください
## 技術スタック
- React + TypeScript / TailwindCSS / Vite
```

**Activation Mode**: Always On / Manual (`@名前`) / Glob (`src/**/*.ts`)

</div>

<div>

### <img src="icons/blue/repeat.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Workflows（ワークフロー）

繰り返しタスクの自動化。`/名前` で実行します。

```markdown
# .agent/workflows/deploy.md
---
description: デプロイ手順
---
1. テストを実行
2. ビルドを実行
3. デプロイコマンドを実行
```

実行: `/deploy`

</div>

</div>

---

# <img src="icons/blue/psychology.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Agent Skills

<a href="https://agentskills.io">agentskills.io</a> オープン標準に基づく、エージェントに**専門的な能力をパッケージとして追加**する仕組みです。

<div class="cols">

<div class="card card-lav">
<h3><img src="icons/lav/folder_special.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> SKILL.md の構造</h3>

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

<div class="card card-blue">
<h3><img src="icons/blue/folder.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 配置場所</h3>
<p><strong>ワークスペース</strong>:<br><code>.agent/skills/&lt;name&gt;/SKILL.md</code></p>
<p><strong>グローバル</strong>:<br><code>~/.gemini/antigravity/skills/&lt;name&gt;/SKILL.md</code></p>
<p style="margin-top:10px;"><img src="icons/green/check_circle.svg" width="24" style="vertical-align: -0.2em; margin-right: 4px;"> 単一の責任に集中</p>
<p><img src="icons/green/check_circle.svg" width="24" style="vertical-align: -0.2em; margin-right: 4px;"> 明確な名前と説明</p>
</div>

</div>

<p class="center" style="font-size:22px;font-weight:700;color:#8060a8;margin-top:10px;">「@code-review して」と頼むだけで実行されます</p>

---

<!-- _class: bg-orange -->

# <img src="icons/orange/payments.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> 料金プラン

<div class="cols-3">

<div class="card card-green center">
<img src="icons/green/volunteer_activism.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<h3>Free</h3>
<p style="font-size:28px;font-weight:900;color:#6bb86a;">無料</p>
<p class="sm">Gemini 3 Pro（制限あり）<br>Nano Banana（月50枚）<br>ローカルMCP</p>
</div>

<div class="card card-blue center">
<img src="icons/blue/star.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<h3>Pro</h3>
<p style="font-size:28px;font-weight:900;color:#6daad8;">$19/月</p>
<p class="sm">Gemini 3 Pro（優先）<br>Claude Sonnet 4.5<br>Nano Banana（無制限）<br>クラウドMCP</p>
</div>

<div class="card card-lav center">
<img src="icons/lav/business.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<h3>Enterprise</h3>
<p style="font-size:28px;font-weight:900;color:#9b82b5;">要相談</p>
<p class="sm">チーム共有Artifacts<br>Enterpriseセキュリティ<br>カスタムモデル</p>
</div>

</div>

<p class="center" style="margin-top:12px;"><strong>学生でもFreeプランで十分に活用できます</strong></p>

---

<!-- _class: bg-blue -->

# <img src="icons/blue/download.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> インストール方法

<div class="card card-blue">

<p><span class="num">1</span> <strong>公式サイトへアクセス</strong> ― <a href="https://antigravity.google">antigravity.google</a></p>

<p><span class="num">2</span> <strong>ダウンロード</strong> ― macOS / Windows / Linux に対応</p>

<p><span class="num">3</span> <strong>ログイン</strong> ― Googleアカウントでサインインするだけ</p>

</div>

<div class="card card-lav" style="margin-top:10px;">
<h3><img src="icons/lav/devices.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> システム要件</h3>
<p><strong>macOS</strong>: v12 (Monterey)以上 ※Apple Siliconのみ &nbsp;/&nbsp; <strong>Windows</strong>: 10 (64-bit)以上 &nbsp;/&nbsp; <strong>Linux</strong>: glibc >= 2.28</p>
</div>

<p class="center" style="font-size:24px;font-weight:700;color:#5a4d78;margin-top:12px;">
<img src="icons/green/timer.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 5分で開発環境が整います
</p>

---

# <img src="icons/lav/menu_book.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> ハンズオン構成

<div class="note">
<img src="icons/orange/lightbulb.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> <strong>前半</strong>で早めにVibe Codingを体験 → <strong>後半</strong>で拡張機能を学ぶ流れです。
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

<img src="icons/lav/play_circle.svg" width="96" style="vertical-align: -0.2em; margin-right: 6px;">

# 実践！Vibe Coding デモ

## 「AI Coffee Shop」ランディングページを作ってみよう

---

<!-- _class: bg-green -->

# <img src="icons/green/movie.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Vibe Coding デモ ― Step 1

### <img src="icons/green/create_new_folder.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> プロジェクト作成

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

# <img src="icons/blue/movie.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Vibe Coding デモ ― Step 2

### <img src="icons/blue/edit_note.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> キャッチコピーと構成（Gemini 3 Pro）

```
「未来的で落ち着くコーヒーショップのキャッチコピーと、
LPのセクション構成を考えて（Gemini 3 Pro）」
```

<div class="arrow">↓</div>

<div class="card card-blue">
<p><img src="icons/blue/format_quote.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> キャッチコピー：<strong>「未来と伝統が溶け合う、至福の一杯」</strong></p>
<p style="margin-top:8px;"><img src="icons/blue/view_list.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> セクション構成：Hero → Concept → Menu → Access → Contact</p>
</div>

---

<!-- _class: bg-pink -->

# <img src="icons/pink/movie.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Vibe Coding デモ ― Step 3

### <img src="icons/pink/image.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> ビジュアル生成（Nano Banana）

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

# <img src="icons/lav/movie.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Vibe Coding デモ ― Step 4

### <img src="icons/lav/code.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 実装 & プレビュー

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

# <img src="icons/green/movie.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Vibe Coding デモ ― Step 5

### <img src="icons/green/cloud_upload.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> デプロイ準備

```
「これで完成。ビルドしてデプロイの準備をして。」
```

<div class="arrow">↓</div>

<div class="ok">
AIが <code>npm run build</code> を実行し、最適化チェック後、Vercel / Netlify 向けのデプロイコマンドも提示してくれます。
</div>

<p class="center" style="font-size:24px;font-weight:900;color:#3a6a3a;margin-top:12px;">
<img src="icons/green/timer.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> わずか10分で本格的なLPが完成！
</p>

---

<!-- _class: bg-orange -->

# <img src="icons/orange/auto_awesome.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Vibe Codingの魅力

<div class="hl">

<div class="cols">

<div>
<h3><img src="icons/blue/target.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 「What」に集中できる</h3>
<p>「どうやって実装するか」ではなく<strong>「何を創りたいか」</strong>を考える時間が増えます。</p>
</div>

<div>
<h3><img src="icons/green/speed.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 圧倒的な開発速度</h3>
<p>従来 3.5 時間かかっていた作業が<strong>わずか10分</strong>に短縮されます。</p>
</div>

</div>

### <img src="icons/pink/palette.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> デザインとコードの統合

エンジニアが自分でデザイン素材を用意できるため、デザイナーとの待ち時間がなくなります。

</div>

---

<!-- _class: bg-lav -->

# <img src="icons/lav/change_history.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> 開発フローの変化

<div class="cols">

<div class="card card-pink">
<h3><img src="icons/pink/hourglass_top.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 従来の開発フロー</h3>
<p>要件定義 → 設計 → 環境構築 → 実装 → テスト → デバッグ → ドキュメント → デプロイ</p>
<p class="sm" style="color:#8a3060;margin-top:8px;">多くのステップに時間がかかる</p>
</div>

<div class="card card-green">
<h3><img src="icons/green/bolt.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> Antigravityの開発フロー</h3>
<p><span class="num">1</span> 要件定義</p>
<p><span class="num">2</span> AIに指示</p>
<p><span class="num">3</span> 完成！</p>
<p style="font-weight:700;color:#3a6a3a;margin-top:8px;">時間のかかる作業をAIが自律的に処理</p>
</div>

</div>

---

# <img src="icons/lav/summarize.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> Antigravityの強み まとめ

<div class="cols-3">

<div class="card card-blue center">
<img src="icons/blue/smart_toy.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<p style="font-weight:700;margin-top:8px;">自律エージェント</p>
<p class="sm">計画・実行・検証</p>
</div>

<div class="card card-pink center">
<img src="icons/pink/image.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<p style="font-weight:700;margin-top:8px;">画像生成</p>
<p class="sm">Nano Banana</p>
</div>

<div class="card card-green center">
<img src="icons/green/cable.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<p style="font-weight:700;margin-top:8px;">拡張性</p>
<p class="sm">MCP連携</p>
</div>

</div>

<div class="cols-3">

<div class="card card-orange center">
<img src="icons/orange/model_training.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<p style="font-weight:700;margin-top:8px;">マルチモデル</p>
<p class="sm">適材適所</p>
</div>

<div class="card card-lav center">
<img src="icons/lav/tune.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<p style="font-weight:700;margin-top:8px;">カスタマイズ</p>
<p class="sm">GEMINI.md / Skills</p>
</div>

<div class="card card-green center">
<img src="icons/green/savings.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<p style="font-weight:700;margin-top:8px;">無料で始められる</p>
<p class="sm">Freeプラン対応</p>
</div>

</div>

---

<!-- _class: bg-blue -->

# <img src="icons/blue/school.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> 学習リソース

<div class="cols-3">

<div class="card card-blue center">
<img src="icons/blue/article.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<h3>公式ドキュメント</h3>
<p class="sm"><a href="https://antigravity.google/docs">antigravity.google/docs</a></p>
</div>

<div class="card card-lav center">
<img src="icons/lav/groups.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<h3>コミュニティ</h3>
<p class="sm">Discord: Antigravity Developers<br>GitHub: antigravity-examples</p>
</div>

<div class="card card-pink center">
<img src="icons/pink/play_circle.svg" width="64" style="vertical-align: -0.2em; margin-right: 6px;">
<h3>チュートリアル</h3>
<p class="sm">YouTube公式チャンネル<br>Qiita #Antigravity</p>
</div>

</div>

---

<!-- _class: bg-green -->

# <img src="icons/green/rocket_launch.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> 今日から始めよう！

<div class="hl">

<p><span class="num">1</span> <strong>インストール</strong> ― <a href="https://antigravity.google">antigravity.google</a></p>

<p><span class="num">2</span> <strong>ハンズオン実践</strong> ― 本日の資料を参考に6つのステップを体験</p>

<p><span class="num">3</span> <strong>自分のプロジェクトで活用</strong> ― GEMINI.md、Skills、MCPを駆使して開発を加速</p>

</div>

<p class="center" style="font-size:26px;font-weight:900;color:#5a4d78;margin-top:16px;">重力から解放された開発体験を、今すぐ！</p>

---

<!-- _class: lead -->

<img src="icons/lav/favorite.svg" width="96" style="vertical-align: -0.2em; margin-right: 6px;">

# ありがとうございました！

## 質問・ディスカッションタイム

Google Antigravityで、開発の未来を体験しましょう！

---

# <img src="icons/blue/attach_file.svg" width="50" style="vertical-align: -0.2em; margin-right: 6px;"> 補足資料

<div class="cols">

<div class="card card-blue">
<h3><img src="icons/blue/link.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> 参考リンク</h3>
<p>公式サイト：<a href="https://antigravity.google">antigravity.google</a></p>
<p>ドキュメント：<a href="https://antigravity.google/docs">antigravity.google/docs</a></p>
<p>GitHub：<a href="https://github.com/google/antigravity-examples">antigravity-examples</a></p>
</div>

<div class="card card-lav">
<h3><img src="icons/lav/inventory.svg" width="38" style="vertical-align: -0.2em; margin-right: 6px;"> ハンズオン資料</h3>
<p>各ステップの詳細は <code>handson/</code> フォルダを参照してください。</p>
</div>

</div>
