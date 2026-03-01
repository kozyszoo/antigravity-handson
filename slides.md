---
theme: default
background: https://cover.sli.dev
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Google Antigravity Handson
drawings:
  persist: false
transition: slide-up
title: Google Antigravity Handson
---
---layout: centerclass: text-center---
# Google Antigravity Handson
<div class='text-gray-500 my-4'>次世代AIエージェント統合開発環境に入門しよう</div>
<div class='text-gray-500 my-4'>2026.03.07</div>
<div class='text-gray-500 my-4'>@kozzy0919（Koji Yamaoka）</div>
<div class='text-gray-500 my-4'>📅 2026年3月7日(土) 19:00〜21:00 ｜ 🌐
          オンライン開催</div>


---

# 本日のアジェンダ

<div class="slide-content">


<div class="highlight-purple" style="margin-bottom: 16px;">
<strong>🏁 学習目標</strong><br/>
<strong>Antigravityの魅力を体感し、明日から使えるスキルを身につける</strong>
</div>
<div class="two-col">
<div class="col">
<table>
<tr>
<th>時間</th>
<th>内容</th>
<th>詳細</th>
</tr>
<tr>
<td>5分</td>
<td>課題提起</td>
<td>従来の開発の問題点</td>
</tr>
<tr>
<td>10分</td>
<td>Antigravityとは</td>
<td>基本概念と革新性</td>
</tr>
<tr>
<td>15分</td>
<td>技術詳細</td>
<td>Architecture / MCP / Skills</td>
</tr>
<tr>
<td>20分</td>
<td>Vibe Coding</td>
<td>実践デモ</td>
</tr>
<tr>
<td>5分</td>
<td>まとめ</td>
<td>次のステップ</td>
</tr>
<tr>
<td>15分</td>
<td>Q&amp;A</td>
<td>質問・ディスカッション</td>
</tr>
</table>
</div>
<div class="col">
<div class="highlight-green">
<strong>✅ Antigravityなら</strong><br/><br/>
              環境構築もテンプレートもAIが自動で処理。リファクタリング、ドキュメント生成、画像生成まですべて自律的に実行。創造的な作業だけに集中できます。
            </div>
</div>
</div>
</div>

---

# kozzy (@kozzy0919) | 山岡 滉治（やまおか こうじ）

<div class="slide-content">


<p style="color: #7c6daa; font-weight: 700; margin-bottom: 12px;">データ・AI企画推進 / Developer Relations</p>
<p style="margin-bottom: 16px;">新卒よりBtoBクラウドサービスのインフラ/サーバーエンジニア → Webサービス開発 → 現在はデータ・AI企画推進チームにて<strong style="color:#e67e22;">生成AI活用の企画・推進</strong>を担当</p>
<div style="margin-bottom: 16px;">
<strong>☆ 主要な実績</strong>
<ul class="bullet-list" style="margin-top: 8px;">
<li>GitHub Copilot導入で全社利用率を60%に向上</li>
<li>社内生成AIコミュニティを200名→2,000名以上に成長</li>
<li>生成AI活用の新機能企画・業務改善プロジェクトを推進</li>
</ul>
</div>
<div>
<strong>📝 その他の活動</strong>
<ul class="bullet-list" style="margin-top: 8px;">
<li>🎓 2025年3月 「開発系エンジニアのためのGit/GitHub絵とき入門」出版 (秀和システム)</li>
<li>👨‍🏫 小中学生向けプログラミングスクール講師</li>
</ul>
</div>
</div>

---

# 本日のアジェンダ

<div class="slide-content">


<div class="highlight-purple" style="margin-bottom: 16px;">
<strong>🏁 学習目標</strong><br/>
<strong style="color: #4a3f6b;">Antigravityを使いこなし、ハッカソンで圧倒的な開発速度を実現する</strong>
</div>
<table>
<tr>
<th>時間</th>
<th>内容</th>
<th>詳細</th>
</tr>
<tr>
<td>5分</td>
<td>❓ 課題提起</td>
<td>従来の開発の問題点</td>
</tr>
<tr>
<td>10分</td>
<td>◎ Antigravityとは</td>
<td>基本概念と革新性</td>
</tr>
<tr>
<td>15分</td>
<td>🔧 技術詳細</td>
<td>Architecture / MCP / Skills</td>
</tr>
<tr>
<td>20分</td>
<td>🚀 Vibe Coding</td>
<td>実践デモ</td>
</tr>
<tr>
<td>5分</td>
<td>✨ まとめ</td>
<td>次のステップ</td>
</tr>
<tr>
<td>15分</td>
<td>💬 Q&amp;A</td>
<td>質問・ディスカッション</td>
</tr>
</table>
<p style="text-align: center; color: #888; margin-top: 8px;">⏱ 合計約2時間（19:00〜21:00）</p>
</div>

---

# Antigravityの哲学

<div class="slide-content">


<div class="card" style="margin-bottom: 20px;">
<h3 style="font-size: 1.2em;">「重力からの解放」</h3>
<p style="margin-top: 8px;">開発者は「<strong style="color: #e67e22;">何を創るか（What）</strong>」に集中すべき。環境構築、定型作業、ドキュメント、デザイン素材 ——これらはすべてAIに任せる。</p>
</div>
<div class="flow-row" style="justify-content: center; gap: 12px;">
<div class="flow-item" style="background: #f0e6ff; border: 1px solid #c4b5e3;">⚙️ 環境構築→AIへ</div>
<div class="flow-item" style="background: #fff3e0; border: 1px solid #f39c12;">🔄 定型作業→AIへ</div>
<div class="flow-item" style="background: #e3f2fd; border: 1px solid #3498db;">📄 ドキュメント→AIへ</div>
<div class="flow-item" style="background: #e8f5e9; border: 1px solid #27ae60;">🎨 デザイン→AIへ</div>
</div>
<p style="text-align: center; margin-top: 16px; color: #7c6daa; font-weight: 700;">これが Vibe Coding の真髄</p>
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.006.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.007.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.008.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.009.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.010.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.011.png' class='h-full object-contain' />
</div>

---

# Google Antigravityとは？

<div class="slide-content">


<div class="highlight-purple" style="margin-bottom: 16px;">
          2025年11月発表の革新的なIDE（VS Codeフォーク）。従来の「コード補完」から<strong>「自律的AIパートナー」</strong>へのパラダイムシフトを実現。Gemini 3 Deep Think搭載。
        </div>
<div style="margin-top: 8px;"><strong>✨ 3つの革新ポイント</strong></div>
<div class="card-grid cols-2" style="margin-top: 12px;">
<div class="card">
<h3><span class="badge badge-purple">1</span> Agent-First Architecture</h3>
<p>AIが単なるツールではなく、タスクの計画・実行・検証までを担う<strong style="color:#e67e22;">自律的なパートナー</strong>として機能します。</p>
</div>
<div class="card">
<h3><span class="badge badge-purple">2</span> Dual View System</h3>
<p><strong style="color:#4a3f6b;">Agent Manager</strong>（司令塔）でエージェントを指揮し、<strong style="color:#4a3f6b;">Editor View</strong>（作業場）でコードを書く。<code style="background:#eee;padding:2px 6px;border-radius:4px;">Cmd+E</code> で切り替え。</p>
</div>
</div>
<div class="card" style="margin-top: 12px;">
<h3><span class="badge badge-purple">3</span> Multi-Model Support</h3>
<p>Gemini 3 Pro/Flash、Claude Sonnet/Opus 4.5、Nano Banana Proなど複数のAIモデルを目的に応じて使い分けられます。</p>
</div>
</div>

---

# Agent-First Architecture

<div class="slide-content">

<div style="display: flex; gap: 2px; margin-bottom: 16px;">
<div class="slide-title" style="font-size: 1.2em; margin-bottom: 0;">　　　　　　　　　　　　</div>
<div class="slide-title" style="font-size: 1.5em; margin-bottom: 0;"><span class="icon">💻</span> Dual View
            System</div>
</div>

<div class="two-col">
<div class="col">
<div class="card" style="background: #f4f0fa;">
<p><strong>開発者</strong> が自然言語で指示</p>
<p style="text-align:center; margin: 8px 0;">↓</p>
<p><strong style="color:#7c6daa;">Manager View</strong> が受け取り、各エージェントへ分配</p>
<p style="text-align:center; margin: 8px 0;">↓</p>
<div style="display: flex; gap: 8px; flex-wrap: wrap; justify-content: center;">
<span class="badge" style="background:#e8f5e9; color:#2e7d32;">📋 Planner</span>
<span class="badge" style="background:#e3f2fd; color:#1565c0;">〈〉Coder</span>
<span class="badge" style="background:#fff3e0; color:#e65100;">🎨 Designer</span>
<span class="badge" style="background:#fce4ec; color:#c62828;">📝 Reviewer</span>
</div>
<p style="text-align:center; margin: 8px 0;">↓</p>
<p>📦 <strong>Artifacts</strong>（成果物）として統合</p>
</div>
</div>
<div class="col">
<div class="card" style="background: #ebf5fb;">
<h3>👥 Manager View（司令塔）</h3>
<p>チャット形式で自然言語のタスク依頼ができるインターフェース。エージェントの動作をリアルタイムで監視・管理し、Artifacts（成果物）もここで確認できます。</p>
</div>
<div class="card" style="background: #fff8e1;">
<h3>💻 Editor View（作業場）</h3>
<p>VS Code互換のエディタ。<code style="background:#eee;padding:2px 6px;border-radius:4px;">Cmd+K</code>
                でインライン編集、リアルタイムプレビューに対応。従来の手動開発スタイルとAIを柔軟に使い分けられます。</p>
</div>
</div>
</div>
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.014.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.015.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.016.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.017.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.018.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.019.png' class='h-full object-contain' />
</div>

---

# 開発フローの変化

<div class="slide-content">


<div class="card-grid cols-2" style="flex: 1;">
<div class="compare-box compare-pink">
<h3>⏳ 従来の開発フロー</h3>
<p style="margin-top: 12px; font-weight: 700;">要件定義 → 設計 → 環境構築 → 実装 → テスト → デバッグ → ドキュメント → デプロイ</p>
<p style="margin-top: 8px; color: #888; font-size: 0.85em;">多くのステップに時間がかかる</p>
</div>
<div class="compare-box compare-green">
<h3>⚡ Antigravityの開発フロー</h3>
<div style="margin-top: 12px;">
<p><span class="badge badge-purple">1</span> 要件定義</p>
<p style="margin-top: 8px;"><span class="badge badge-purple">2</span> AIに指示</p>
<p style="margin-top: 8px;"><span class="badge badge-green">3</span> 完成！</p>
</div>
<p style="margin-top: 12px;">時間のかかる作業をAIが自律的に処理</p>
</div>
</div>
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.021.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.022.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.023.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.024.png' class='h-full object-contain' />
</div>


---layout: centerclass: text-center---
# 実践！Vibe Coding デモ
<div class='text-gray-500 my-4'>「AI Coffee Shop」ランディングページを作ってみよう</div>


---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.026.png' class='h-full object-contain' />
</div>

---

# ハンズオン構成

<div class="slide-content">


<div class="highlight-yellow" style="margin-bottom: 16px;">
          💡 <strong>前半</strong>で早めにVibe Codingを体験 → <strong>後半</strong>で拡張機能を学ぶ流れです。
        </div>
<table>
<tr>
<th>No</th>
<th>内容</th>
<th>所要時間</th>
</tr>
<tr>
<td><span class="badge badge-purple">1</span></td>
<td>環境セットアップ</td>
<td>15分</td>
</tr>
<tr>
<td><span class="badge badge-purple">2</span></td>
<td>GEMINI.md（AGENTS.md）設定</td>
<td>15分</td>
</tr>
<tr>
<td><span class="badge badge-orange">3</span></td>
<td><strong style="color:#e67e22;">Vibe Coding 基礎編</strong></td>
<td>20分</td>
</tr>
<tr>
<td><span class="badge badge-purple">4</span></td>
<td>MCP 接続</td>
<td>20分</td>
</tr>
<tr>
<td><span class="badge badge-purple">5</span></td>
<td>Agent Skills 作成</td>
<td>20分</td>
</tr>
<tr>
<td><span class="badge badge-orange">6</span></td>
<td><strong style="color:#e67e22;">Vibe Coding 発展編</strong></td>
<td>30分</td>
</tr>
</table>
<p style="text-align: center; color: #888; margin-top: 8px;">合計：約2時間</p>
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.028.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.029.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.030.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.031.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.032.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.033.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.034.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.035.png' class='h-full object-contain' />
</div>

---

# Step 2: GEMINI.md（AGENTS.md）設定

<div class="slide-content">


<div class="two-col">
<div class="col">
<div><strong>📁 設定ファイルの場所</strong></div>
<table style="font-size: 0.9em;">
<tr>
<th>スコープ</th>
<th>パス</th>
</tr>
<tr>
<td>グローバル</td>
<td>~/.gemini/GEMINI.md</td>
</tr>
<tr>
<td>ワークスペース</td>
<td>.agent/rules/ または GEMINI.md</td>
</tr>
</table>
<div style="margin-top: 12px;"><strong>📂 Rulesを追加する方法</strong></div>
<div class="card" style="font-size: 0.85em; background: #f7f5fb;">
              Editor 右上の [...] &gt; Customizations<br/>&gt; Rules &gt; +Workspace
            </div>
</div>
<div class="col">
<div><strong>📝 設定例</strong></div>
<div class="code-block">
<span class="comment"># プロジェクト設定</span><br/>
<span class="keyword">## 基本ルール</span><br/>
                <span class="string">常に日本語で応答してください</span><br/>
                <span class="string">コードには必ずコメントを入れてください</span><br/>
<span class="keyword">## コーディング規約</span><br/>
                Make sure all code follows PEP 8<br/>
                Always document methods
            </div>
<div class="highlight-yellow">
              💡 ルールはエージェントが毎回参照するシステム指示として機能します。
            </div>
</div>
</div>
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.036.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.037.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.038.png' class='h-full object-contain' />
</div>


---layout: centerclass: text-center---
# 実践！Vibe Coding デモ（発展編）
<div class='text-gray-500 my-4'>Step 6:「AI Coffee Shop」LP構築デモ</div>


---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.040.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.041.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.042.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.043.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.044.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.045.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.046.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.047.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.048.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.049.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.050.png' class='h-full object-contain' />
</div>

---

# 補足資料

<div class="slide-content">


<h3 style="margin-bottom: 12px;">学習リソース</h3>
<div class="card-grid cols-3" style="margin-bottom: 24px;">
<div class="card" style="text-align: center; background: #ebf5fb;">
<div style="font-size: 2em;">📑</div>
<h3>公式ドキュメント</h3>
<p style="font-size: 0.85em; color: #888;">build.google.com/antigravity/docs</p>
</div>
<div class="card" style="text-align: center; background: #ebf5fb;">
<div style="font-size: 2em;">👥</div>
<h3>コミュニティ</h3>
<p style="font-size: 0.85em; color: #888;">Discord: Antigravity Developers<br/>GitHub: antigravity-examples
            </p>
</div>
<div class="card" style="text-align: center; background: #fce4ec;">
<div style="font-size: 2em;">▶</div>
<h3>チュートリアル</h3>
<p style="font-size: 0.85em; color: #888;">YouTube公式チャンネル<br/>Qiita #Antigravity</p>
</div>
</div>
<h3 style="margin-bottom: 12px;">資料</h3>
<div class="card-grid cols-2">
<div class="card" style="background: #f7f5fb;">
<h3>🔗 参考リンク</h3>
<p>公式サイト：build.google.com/antigravity</p>
<p>ドキュメント：build.google.com/antigravity/docs</p>
<p>GitHub：antigravity-examples</p>
</div>
<div class="card" style="background: #fef9e7;">
<h3>📝 ハンズオン資料</h3>
<p>各ステップの詳細は <strong>handson/</strong> フォルダを参照してください。</p>
</div>
</div>
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.052.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.053.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.054.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.055.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.056.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.057.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.058.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.059.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.060.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.061.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.062.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.063.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.064.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.065.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.066.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.067.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.068.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.069.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.070.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.071.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.072.png' class='h-full object-contain' />
</div>

---

<div class='w-full h-full flex justify-center items-center'>
  <img src='./slides/20260307_Antiglavity_Handson.073.png' class='h-full object-contain' />
</div>

<style>
/* CSS copied from original presentation */
.slide-content { display: flex; flex-direction: column; width: 100%; height: 100%; }
.highlight-purple { background: #f4f0fa; border-left: 6px solid #7c6daa; padding: 20px 24px; border-radius: 8px; margin: 20px 0; font-size: 1.05em; line-height: 1.6; }
.highlight-yellow { background: #fef9e7; border-left: 6px solid #f39c12; padding: 20px 24px; border-radius: 8px; margin: 20px 0; font-size: 1.05em; line-height: 1.6; }
.highlight-green { background: #eafaf1; border-left: 6px solid #27ae60; padding: 20px 24px; border-radius: 8px; margin: 20px 0; font-size: 1.05em; line-height: 1.6; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; flex: 1; }
.col { display: flex; flex-direction: column; gap: 16px; }
.card { background: #fff; border-radius: 12px; padding: 24px 30px; border: 1px solid #f0eef5; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05); }
.card h3 { font-size: 1.1em; font-weight: 700; margin-bottom: 12px; color: #382c59; }
.card p { line-height: 1.6; color: #555; }
.badge { display: inline-block; padding: 6px 16px; border-radius: 20px; font-size: 0.85em; font-weight: 700; margin-right: 8px; margin-bottom: 8px; }
.badge-purple { background: #7c6daa; color: #fff; }
.badge-orange { background: #e67e22; color: #fff; }
.badge-green { background: #27ae60; color: #fff; }
table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 20px 0; font-size: 1.05em; border: 1px solid #e0dce8; border-radius: 8px; overflow: hidden; }
th { background: #7c6daa; color: #fff; padding: 14px 20px; text-align: left; font-weight: 700; }
td { padding: 14px 20px; border-bottom: 1px solid #e0dce8; color: #444; }
tr:last-child td { border-bottom: none; }
tr:nth-child(even) td { background: #fbfafc; }
.flow-row { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.flow-item { padding: 12px 24px; border-radius: 8px; font-weight: 600; font-size: 1.05em; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }
.bullet-list { list-style: none; padding: 0; }
.bullet-list li { padding: 8px 0; padding-left: 24px; position: relative; font-size: 1.05em; line-height: 1.6; color: #444; }
.bullet-list li::before { content: "•"; color: #7c6daa; font-size: 1.5em; position: absolute; left: 0; top: 2px; }
.compare-box { border-radius: 12px; padding: 30px 40px; flex: 1; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 4px 12px rgba(0,0,0,0.03); }
.compare-pink { background: #fde8e8; }
.compare-green { background: #e8fde8; }
.code-block { background: #1e1e2e; color: #cdd6f4; border-radius: 12px; padding: 24px 30px; font-family: 'JetBrains Mono', monospace; font-size: 0.9em; line-height: 1.6; overflow-x: auto; box-shadow: inset 0 2px 4px rgba(0,0,0,0.2); }
.code-block .comment { color: #6c7086; }
.code-block .keyword { color: #cba6f7; }
.code-block .string { color: #a6e3a1; }
.card-grid { display: grid; gap: 20px; }
.card-grid.cols-2 { grid-template-columns: repeat(2, 1fr); }
.card-grid.cols-3 { grid-template-columns: repeat(3, 1fr); }
</style>
