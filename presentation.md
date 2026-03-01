---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap');
  

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

<span class="ms ms-hero c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m187-551 106 45q18-36 38.5-71t43.5-67l-79-16-109 109Zm154 81 133 133q57-26 107-59t81-64q81-81 119-166t41-192q-107 3-192 41T464-658q-31 31-64 81t-59 107Zm209-145.5q0-29.5 20-49.5t49.5-20q29.5 0 49.5 20t20 49.5q0 29.5-20 49.5t-49.5 20q-29.5 0-49.5-20t-20-49.5Zm5 432.5 109-109-16-79q-32 23-67 43.5T510-289l45 106Zm326-694q9 136-34 248T705-418l-2 2-2 2 22 110q3 15-1.5 29T706-250L535-78l-85-198-170-170-198-85 172-171q11-11 25-15.5t29-1.5l110 22q1-1 2-1.5t2-1.5q99-99 211-142.5T881-877ZM149-325q35-35 85.5-35.5T320-326q35 35 34.5 85.5T319-155q-26 26-80.5 43T75-80q15-109 31.5-164t42.5-81Zm42 43q-14 15-25 47t-19 82q50-8 82-19t47-25q19-17 19.5-42.5T278-284q-19-18-44.5-17.5T191-282Z"/></svg></span>

# Google Antigravity
## ハンズオン 2026.03.07

<br>

<div class="card card-lav" style="display:inline-block; padding: 10px 32px;">
<strong>Vibe Coding で重力から解放されよう</strong>
</div>

<br>

**山岡 滉治（kozzy）**
GitHub Copilot 導入実績 / フルスタックエンジニア

</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M180-80q-24 0-42-18t-18-42v-620q0-24 18-42t42-18h65v-60h65v60h340v-60h65v60h65q24 0 42 18t18 42v620q0 24-18 42t-42 18H180Zm0-60h600v-430H180v430Zm0-490h600v-130H180v130Zm0 0v-130 130Z"/></svg></span> 本日のアジェンダ

<div class="cols">
<div>

<div class="card card-blue" style="margin-bottom:10px;">
<span class="step-badge step-blue">19:00</span> <strong>イントロ</strong><br>
<small>Vibe Codingとは？パラダイムシフト</small>
</div>

<div class="card card-blue" style="margin-bottom:10px;">
<span class="step-badge step-blue">19:15</span> <strong>Antigravityの核心技術</strong><br>
<small>Agent-First / Dual View / Multi-Model</small>
</div>

<div class="card card-green" style="margin-bottom:10px;">
<span class="step-badge step-green">19:30</span> <strong>Step 1-2: 環境構築</strong><br>
<small>インストール + GEMINI.md 設定</small>
</div>

<div class="card card-green">
<span class="step-badge step-green">20:00</span> <strong>Step 3: Vibe Coding 基礎</strong><br>
<small>自己紹介ページ + Nano Banana</small>
</div>

</div>
<div>

<div class="card card-orange" style="margin-bottom:10px;">
<span class="step-badge step-orange">20:20</span> <strong>Step 4-5: エージェント拡張</strong><br>
<small>MCP 接続 + Agent Skills</small>
</div>

<div class="card card-orange" style="margin-bottom:10px;">
<span class="step-badge step-orange">20:40</span> <strong>Step 6: Vibe Coding 発展</strong><br>
<small>AI Coffee Shop LP 構築</small>
</div>

<div class="card card-lav">
<span class="step-badge step-lav">21:00</span> <strong>Step 7: まとめ</strong><br>
<small>AI-DLC × ハッカソン最強戦略</small>
</div>

</div>
</div>

---

<!-- _class: bg-pink -->

# <span class="ms ms-lg c-pink" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M324-111.5Q251-143 197-197t-85.5-127Q80-397 80-480t31.5-156Q143-709 197-763t127-85.5Q397-880 480-880t156 31.5Q709-817 763-763t85.5 127Q880-563 880-480t-31.5 156Q817-251 763-197t-127 85.5Q563-80 480-80t-156-31.5ZM437-141v-82q-35 0-59-26t-24-61v-44L149-559q-5 20-7 39.5t-2 39.5q0 130 84.5 227T437-141Zm294-108q44-48 66.5-107.5T820-480q0-106-58-192.5T607-799v18q0 35-24 61t-59 26h-87v87q0 17-13.5 28T393-568h-83v88h258q17 0 28 13t11 30v127h43q29 0 51 17t30 44Z"/></svg></span> 開発の「重力」から解放される

<div class="cols">
<div>

### 😩 今までの開発

<div class="card card-pink">

- 環境構築に **半日** 消える
- ドキュメント作成で **時間切れ**
- 定型コードを **手で書き続ける**
- テスト・レビューが **後回し**

</div>

<div class="card card-pink" style="margin-top:10px;">
<strong>「作りたいもの」より「作業」に追われる</strong>
</div>

</div>
<div>

### 🚀 Antigravity の世界

<div class="card card-green">

- AIが **自律的にタスクを計画・実行**
- 自然言語で **意図を伝えるだけ**
- デザイン・実装・テストを **AI が担う**
- 人間は **判断と創造** に集中

</div>

<div class="card card-green" style="margin-top:10px;">
<strong>「What（何を作るか）」に集中できる</strong>
</div>

</div>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M240-80v-172q-57-52-88.5-121.5T120-520q0-150 105-255t255-105q125 0 221.5 73.5T827-615l55 218q4 14-5 25.5T853-360h-93v140q0 24.75-17.62 42.37Q724.75-160 700-160H600v80h-60v-140h160v-200h114l-45-180q-24-97-105-158.5T480-820q-125 0-212.5 86.5T180-522.46q0 64.42 26.32 122.39Q232.65-342.09 281-297l19 18v199h-60Zm257-370Zm-48 76h60l3-44q12-2 22.47-8.46Q544.94-432.92 553-441l42 14 28-48-30-24q5-14 5-29t-5-29l30-24-28-48-42 14q-8.33-7.69-19.17-13.85Q523-635 512-638l-3-44h-60l-3 44q-11 3-21.83 9.15Q413.33-622.69 405-615l-42-14-28 48 30 24q-5 14-5 29t5 29l-30 24 28 48 42-14q8.06 8.08 18.53 14.54Q434-420 446-418l3 44Zm-19.5-104.38q-20.5-20.38-20.5-49.5t20.38-49.62q20.38-20.5 49.5-20.5t49.62 20.38q20.5 20.38 20.5 49.5t-20.38 49.62q-20.38 20.5-49.5 20.5t-49.62-20.38Z"/></svg></span> Vibe Coding とは？

<div class="center" style="margin-bottom: 16px;">
<div class="card card-blue" style="display:inline-block; padding: 12px 32px;">
<strong>「自然言語の対話だけで、コードからデザインまで完結させる開発スタイル」</strong>
</div>
</div>

<div class="cols-3">

<div class="card card-blue">
<div class="center">
<span class="ms ms-lg c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M240-399h313v-60H240v60Zm0-130h480v-60H240v60Zm0-130h480v-60H240v60ZM80-80v-740q0-24 18-42t42-18h680q24 0 42 18t18 42v520q0 24-18 42t-42 18H240L80-80Zm134-220h606v-520H140v600l74-80Zm-74 0v-520 520Z"/></svg></span><br>
<strong>伝える</strong><br>
<small>日本語で「こういうの作って」と言うだけ</small>
</div>
</div>

<div class="card card-lav">
<div class="center">
<span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M147-376q-45 0-76-31.21T40-483q0-44.58 31.21-75.79Q102.42-590 147-590v-123q0-24 18-42t42-18h166q0-45 31-76t76-31q45 0 76 31.21T587-773h166q24 0 42 18t18 42v123q45 0 76 31.21T920-483q0 44.58-31.21 75.79Q857.58-376 813-376v196q0 24-18 42t-42 18H207q-24 0-42-18t-18-42v-196Zm224.5-111.74q11.5-11.73 11.5-28.5 0-16.76-11.74-28.26-11.73-11.5-28.5-11.5-16.76 0-28.26 11.74-11.5 11.73-11.5 28.5 0 16.76 11.74 28.26 11.73 11.5 28.5 11.5 16.76 0 28.26-11.74Zm274 0q11.5-11.73 11.5-28.5 0-16.76-11.74-28.26-11.73-11.5-28.5-11.5-16.76 0-28.26 11.74-11.5 11.73-11.5 28.5 0 16.76 11.74 28.26 11.73 11.5 28.5 11.5 16.76 0 28.26-11.74ZM312-285h336v-60H312v60ZM207-180h546v-533H207v533Zm273-267Z"/></svg></span><br>
<strong>AIが実行</strong><br>
<small>計画・コーディング・画像生成まで</small>
</div>
</div>

<div class="card card-green">
<div class="center">
<span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m421-298 283-283-46-45-237 237-120-120-45 45 165 166Zm59 218q-82 0-155-31.5t-127.5-86Q143-252 111.5-325T80-480q0-83 31.5-156t86-127Q252-817 325-848.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 82-31.5 155T763-197.5q-54 54.5-127 86T480-80Zm0-60q142 0 241-99.5T820-480q0-142-99-241t-241-99q-141 0-240.5 99T140-480q0 141 99.5 240.5T480-140Zm0-340Z"/></svg></span><br>
<strong>確認・修正</strong><br>
<small>気に入らなければ「もっと〇〇にして」</small>
</div>
</div>

</div>

<br>

> <span class="ms ms-sm c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m887-567-23-50-50-23 50-23 23-50 23 50 50 23-50 23-23 50ZM760-742l-35-74-74-35 74-35 35-74 35 74 74 35-74 35-35 74ZM302.5-103.5Q279-127 279-161h162q0 34-23.5 57.5T360-80q-34 0-57.5-23.5ZM198-223v-60h324v60H198Zm5-121q-66-43-104.5-107.5T60-597q0-122 89-211t211-89q122 0 211 89t89 211q0 81-38 145.5T517-344H203Zm22-60h271q48-32 76-83t28-110q0-99-70.5-169.5T360-837q-99 0-169.5 70.5T120-597q0 59 28 110t77 83Zm135 0Z"/></svg></span> バイブス（感覚・雰囲気）を伝えるだけで、プロダクトが形になる

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M153-73q-33-33-33-81t33.25-81q33.25-33 80.75-33 14 0 24.5 2.5T280-258l85-106q-19-23-29-52.5t-5-61.5l-121-41q-15 25-39.5 39T114-466q-47.5 0-80.75-33.25T0-580q0-47.5 33.25-80.75T114-694q47.5 0 80.75 33.25T228-580v4l122 42q18-32 43.5-49t56.5-24v-129q-39-11-61.5-43T366-846q0-47.5 33-80.75T480-960q48 0 81 33.25T594-846q0 35-23 67t-61 43v129q31 7 57 24t44 49l121-42v-4q0-47.5 33.25-80.75T846-694q47.5 0 80.75 33T960-580q0 48-33.25 81T846-466q-32 0-57-14t-39-39l-121 41q5 32-4.5 61.5T595-364l85 106q11-5 21.5-7.5t24.06-2.5Q774-268 807-235t33 81q0 48-33 81t-81 33q-48 0-81-33.25T612-154q0-20 5.5-36t15.5-31l-85-106q-32.13 17-68.56 17Q443-310 411-327l-84 107q10 15 15.5 30.5T348-154q0 47.5-33 80.75T234-40q-48 0-81-33Zm-38.96-453q22.96 0 38.46-15.54 15.5-15.53 15.5-38.5 0-22.96-15.54-38.46-15.53-15.5-38.5-15.5Q91-634 75.5-618.46 60-602.93 60-579.96 60-557 75.54-541.5q15.53 15.5 38.5 15.5ZM272.5-115.54q15.5-15.53 15.5-38.5 0-22.96-15.54-38.46-15.53-15.5-38.5-15.5-22.96 0-38.46 15.54-15.5 15.53-15.5 38.5 0 22.96 15.54 38.46 15.53 15.5 38.5 15.5 22.96 0 38.46-15.54Zm246-692q15.5-15.53 15.5-38.5 0-22.96-15.54-38.46-15.53-15.5-38.5-15.5-22.96 0-38.46 15.54-15.5 15.53-15.5 38.5 0 22.96 15.54 38.46 15.53 15.5 38.5 15.5 22.96 0 38.46-15.54ZM480.5-370q37.5 0 63.5-26.5t26-64q0-37.5-26.1-63.5T480-550q-37 0-63.5 26.1T390-460q0 37 26.5 63.5t64 26.5Zm284 254.46q15.5-15.53 15.5-38.5 0-22.96-15.54-38.46-15.53-15.5-38.5-15.5-22.96 0-38.46 15.54-15.5 15.53-15.5 38.5 0 22.96 15.54 38.46 15.53 15.5 38.5 15.5 22.96 0 38.46-15.54Zm120-426q15.5-15.53 15.5-38.5 0-22.96-15.54-38.46-15.53-15.5-38.5-15.5-22.96 0-38.46 15.54-15.5 15.53-15.5 38.5 0 22.96 15.54 38.46 15.53 15.5 38.5 15.5 22.96 0 38.46-15.54ZM480-846ZM114-580Zm366 120Zm366-120ZM234-154Zm492 0Z"/></svg></span> Antigravityの核心：3つの革新

<div class="cols-3">

<div class="card card-blue">
<div class="center">
<span class="ms ms-xl c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M0-240v-53q0-38.57 41.5-62.78Q83-380 150.38-380q12.16 0 23.39.5t22.23 2.15q-8 17.35-12 35.17-4 17.81-4 37.18v65H0Zm240 0v-65q0-32 17.5-58.5T307-410q32-20 76.5-30t96.5-10q53 0 97.5 10t76.5 30q32 20 49 46.5t17 58.5v65H240Zm540 0v-65q0-19.86-3.5-37.43T765-377.27q11-1.73 22.17-2.23 11.17-.5 22.83-.5 67.5 0 108.75 23.77T960-293v53H780Zm-480-60h360v-6q0-37-50.5-60.5T480-390q-79 0-129.5 23.5T300-305v5ZM149.57-410q-28.57 0-49.07-20.56Q80-451.13 80-480q0-29 20.56-49.5Q121.13-550 150-550q29 0 49.5 20.5t20.5 49.93q0 28.57-20.5 49.07T149.57-410Zm660 0q-28.57 0-49.07-20.56Q740-451.13 740-480q0-29 20.56-49.5Q781.13-550 810-550q29 0 49.5 20.5t20.5 49.93q0 28.57-20.5 49.07T809.57-410ZM480-480q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-600q0 50-34.5 85T480-480Zm.35-60Q506-540 523-557.35t17-43Q540-626 522.85-643t-42.5-17q-25.35 0-42.85 17.15t-17.5 42.5q0 25.35 17.35 42.85t43 17.5ZM480-300Zm0-300Z"/></svg></span>
<h3>① Agent-First</h3>
</div>
<small>AIが単なる補完ツールではなく<strong>自律的なパートナー</strong>として計画・実行・検証する</small>
</div>

<div class="card card-orange">
<div class="center">
<span class="ms ms-xl c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M120-260v-440q0-24.75 17.63-42.38Q155.25-760 180-760h600q24.75 0 42.38 17.62Q840-724.75 840-700v440q0 24.75-17.62 42.37Q804.75-200 780-200H180q-24.75 0-42.37-17.63Q120-235.25 120-260Zm270-250h390v-190H390v190Zm229 250h161v-190H619v190Zm-229 0h162v-190H390v190Zm-210 0h150v-440H180v440Z"/></svg></span>
<h3>② Dual View</h3>
</div>
<small><strong>Editor View</strong>（作業場）と<strong>Agent Manager</strong>（司令塔）を <code>Cmd+E</code> で切り替え</small>
</div>

<div class="card card-lav">
<div class="center">
<span class="ms ms-xl c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M206-206q-41-48-63.5-107.5T120-440q0-150 105-254.5T480-799q10 0 20.5.5T519-797l-81-81 42-42 160 160-160 160-43-43 92-92q-11-2-26-3t-23-1q-125 0-212.5 87T180-440q0 51 17 102t52 89l-43 43Zm236-4q0-21-15-43t-32.5-45Q377-321 362-346.5T347-400q0-55 39-94t94-39q55 0 94 39t39 94q0 28-15 53.5T565.5-298Q548-275 533-253t-15 43h-76Zm-2 90v-50h80v50h-80Zm314-86-42-42q30-36 49-85t19-107q0-66-27.5-125.5T670-670l44-44q58 50 92 120.5T840-440q0 67-22.5 126.5T754-206Z"/></svg></span>
<h3>③ Multi-Model</h3>
</div>
<small>Gemini 3・Claude 4.5・Nano Bananaなど<strong>タスクに最適なモデルを自動選択</strong></small>
</div>

</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M120-260v-440q0-24.75 17.63-42.38Q155.25-760 180-760h600q24.75 0 42.38 17.62Q840-724.75 840-700v440q0 24.75-17.62 42.37Q804.75-200 780-200H180q-24.75 0-42.37-17.63Q120-235.25 120-260Zm270-250h390v-190H390v190Zm229 250h161v-190H619v190Zm-229 0h162v-190H390v190Zm-210 0h150v-440H180v440Z"/></svg></span> Dual View System

<div class="cols">
<div>

### Editor View（作業場）

<div class="card card-orange">

- VS Code ベースのエディタ
- ファイルツリー + コードエディタ
- チャットパネル（右サイドバー）
- `Tab` → AI補完（Supercomplete）
- `Cmd + I` → インライン指示

</div>

</div>
<div>

### Agent Manager（司令塔）

<div class="card card-lav">

- AIとの対話に特化した画面
- **Artifacts（成果物）** パネル
  - 実装計画書
  - タスクリスト
  - コード差分
- Inbox で複数会話を並行管理

</div>

</div>
</div>

<br>

<div class="card card-orange" style="text-align:center;">
<span class="ms ms-sm c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M140-200q-24 0-42-18.5T80-260v-440q0-24 18-42t42-18h680q24 0 42 18t18 42v440q0 23-18 41.5T820-200H140Zm0-60h680v-440H140v440Zm160-65h360v-60H300v60Zm-97-125h60v-60h-60v60Zm124 0h60v-60h-60v60Zm123 0h60v-60h-60v60Zm124 0h60v-60h-60v60Zm123 0h60v-60h-60v60ZM203-575h60v-60h-60v60Zm124 0h60v-60h-60v60Zm123 0h60v-60h-60v60Zm124 0h60v-60h-60v60Zm123 0h60v-60h-60v60ZM140-260v-440 440Z"/></svg></span> <code>Cmd + E</code> で Editor ⇔ Agent Manager を即切り替え
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M206-206q-41-48-63.5-107.5T120-440q0-150 105-254.5T480-799q10 0 20.5.5T519-797l-81-81 42-42 160 160-160 160-43-43 92-92q-11-2-26-3t-23-1q-125 0-212.5 87T180-440q0 51 17 102t52 89l-43 43Zm236-4q0-21-15-43t-32.5-45Q377-321 362-346.5T347-400q0-55 39-94t94-39q55 0 94 39t39 94q0 28-15 53.5T565.5-298Q548-275 533-253t-15 43h-76Zm-2 90v-50h80v50h-80Zm314-86-42-42q30-36 49-85t19-107q0-66-27.5-125.5T670-670l44-44q58 50 92 120.5T840-440q0 67-22.5 126.5T754-206Z"/></svg></span> Multi-Model Support

<div class="cols">
<div>

### 推論モデル（選択可能）

<div class="card card-green">

| モデル | 特徴 |
|:---|:---|
| **Gemini 3 Pro** | Google最新・高性能 |
| **Gemini 3 Flash** | 高速レスポンス |
| **Claude Sonnet 4.5** | Thinking モード |
| **Claude Opus 4.5** | 高精度 |

</div>

</div>
<div>

### バックグラウンドモデル（自動）

<div class="card card-blue">

| モデル | 役割 |
|:---|:---|
| **Nano Banana Pro** | 🎨 画像生成・UIモックアップ |
| **Gemini 2.5 Pro UI** | 🌐 Browser Subagent |
| **Gemini 2.5 Flash** | 📋 要約・チェックポイント |

</div>

</div>
</div>

---

<!-- _class: lead -->

<div class="center">

<div class="time-badge">19:30〜20:00</div>

<span class="ms ms-hero c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M705-128 447-388q-23 8-46 13t-47 5q-97.08 0-165.04-67.67Q121-505.33 121-602q0-31 8.16-60.39T152-718l145 145 92-86-149-149q25.91-15.16 54.96-23.58Q324-840 354-840q99.17 0 168.58 69.42Q592-701.17 592-602q0 24-5 47t-13 46l259 258q11 10.96 11 26.48T833-198l-76 70q-10.7 11-25.85 11Q716-117 705-128Zm28-57 40-40-273-273q16-21 24-49.5t8-54.5q0-75-55.5-127T350-782l102 104q9 9 8.5 21.5T451-635L318-510q-9.27 8-21.64 8-12.36 0-20.36-8l-98-97q3 77 54.67 127T354-430q25 0 53-8t49-24l277 277ZM476-484Z"/></svg></span>

# Step 1-2
## 環境構築 + GEMINI.md 設定

</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M480-313 287-506l43-43 120 120v-371h60v371l120-120 43 43-193 193ZM220-160q-24 0-42-18t-18-42v-143h60v143h520v-143h60v143q0 24-18 42t-42 18H220Z"/></svg></span> Step 1: 環境セットアップ

<div class="cols">
<div>

### チェックリスト

<div class="card card-green">

- ✅ Antigravity インストール済み
- ✅ Google アカウントでログイン
- ✅ 最新版に更新済み
- ✅ `File > Open Folder` でこのフォルダを開く

</div>

<div class="card card-blue" style="margin-top:10px;">
<span class="ms ms-sm c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M323-111.5Q250-143 196-197t-85-127.5Q80-398 80-482t31-156.5Q142-711 196-765t127-84.5Q396-880 480-880t157 30.5Q710-819 764-765t85 126.5Q880-566 880-482t-31 157.5Q818-251 764-197t-127 85.5Q564-80 480-80t-157-31.5ZM480-138q35-36 58.5-82.5T577-331H384q14 60 37.5 108t58.5 85Zm-85-12q-25-38-43-82t-30-99H172q38 71 88 111.5T395-150Zm171-1q72-23 129.5-69T788-331H639q-13 54-30.5 98T566-151ZM152-391h159q-3-27-3.5-48.5T307-482q0-25 1-44.5t4-43.5H152q-7 24-9.5 43t-2.5 45q0 26 2.5 46.5T152-391Zm221 0h215q4-31 5-50.5t1-40.5q0-20-1-38.5t-5-49.5H373q-4 31-5 49.5t-1 38.5q0 21 1 40.5t5 50.5Zm275 0h160q7-24 9.5-44.5T820-482q0-26-2.5-45t-9.5-43H649q3 35 4 53.5t1 34.5q0 22-1.5 41.5T648-391Zm-10-239h150q-33-69-90.5-115T565-810q25 37 42.5 80T638-630Zm-254 0h194q-11-53-37-102.5T480-820q-32 27-54 71t-42 119Zm-212 0h151q11-54 28-96.5t43-82.5q-75 19-131 64t-91 115Z"/></svg></span> <strong>日本語化</strong><br>
<small>Extensions →「Japanese Language Pack」をインストール</small>
</div>

</div>
<div>

### セキュリティポリシー設定

<div class="card card-orange">

| モード | 説明 |
|:---|:---|
| **Off** | 手動で許可（最安全） |
| **Auto** | AIが判断（推奨） |
| **Turbo** | 常に自動実行 |

</div>

<div class="card card-orange" style="margin-top:10px;">
<span class="ms ms-sm c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m388-80-20-126q-19-7-40-19t-37-25l-118 54-93-164 108-79q-2-9-2.5-20.5T185-480q0-9 .5-20.5T188-521L80-600l93-164 118 54q16-13 37-25t40-18l20-127h184l20 126q19 7 40.5 18.5T669-710l118-54 93 164-108 77q2 10 2.5 21.5t.5 21.5q0 10-.5 21t-2.5 21l108 78-93 164-118-54q-16 13-36.5 25.5T592-206L572-80H388Zm48-60h88l14-112q33-8 62.5-25t53.5-41l106 46 40-72-94-69q4-17 6.5-33.5T715-480q0-17-2-33.5t-7-33.5l94-69-40-72-106 46q-23-26-52-43.5T538-708l-14-112h-88l-14 112q-34 7-63.5 24T306-642l-106-46-40 72 94 69q-4 17-6.5 33.5T245-480q0 17 2.5 33.5T254-413l-94 69 40 72 106-46q24 24 53.5 41t62.5 25l14 112Zm44-210q54 0 92-38t38-92q0-54-38-92t-92-38q-54 0-92 38t-38 92q0 54 38 92t92 38Zm0-130Z"/></svg></span> <code>Settings > Advanced > Terminal</code> で設定
</div>

</div>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M140-200q-24 0-42-18.5T80-260v-440q0-24 18-42t42-18h680q24 0 42 18t18 42v440q0 23-18 41.5T820-200H140Zm0-60h680v-440H140v440Zm160-65h360v-60H300v60Zm-97-125h60v-60h-60v60Zm124 0h60v-60h-60v60Zm123 0h60v-60h-60v60Zm124 0h60v-60h-60v60Zm123 0h60v-60h-60v60ZM203-575h60v-60h-60v60Zm124 0h60v-60h-60v60Zm123 0h60v-60h-60v60Zm124 0h60v-60h-60v60Zm123 0h60v-60h-60v60ZM140-260v-440 440Z"/></svg></span> エディタのAI機能

<div class="cols">
<div>

### Tab（Supercomplete）

<div class="card card-blue">

複数行のコードをAIが先読みして提案。
押すと採用！

```
// 書きかけのコードで Tab を押す
function fetchUser(id) {
  // ↑ ここで Tab → AIが続きを書いてくれる
}
```

</div>

</div>
<div>

### Cmd + I（Command）

<div class="card card-lav">

自然言語でインライン指示ができる！

```
「この関数にエラーハンドリングを追加して」

「ポート3000を使っているプロセスを終了して」
```

</div>

<div class="card card-orange" style="margin-top:10px;">
<small><span class="ms ms-sm c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m887-567-23-50-50-23 50-23 23-50 23 50 50 23-50 23-23 50ZM760-742l-35-74-74-35 74-35 35-74 35 74 74 35-74 35-35 74ZM302.5-103.5Q279-127 279-161h162q0 34-23.5 57.5T360-80q-34 0-57.5-23.5ZM198-223v-60h324v60H198Zm5-121q-66-43-104.5-107.5T60-597q0-122 89-211t211-89q122 0 211 89t89 211q0 81-38 145.5T517-344H203Zm22-60h271q48-32 76-83t28-110q0-99-70.5-169.5T360-837q-99 0-169.5 70.5T120-597q0 59 28 110t77 83Zm135 0Z"/></svg></span> 日本語でOK！コードを選択してから <code>Cmd+I</code></small>
</div>

</div>
</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M319-250h322v-60H319v60Zm0-170h322v-60H319v60ZM220-80q-24 0-42-18t-18-42v-680q0-24 18-42t42-18h361l219 219v521q0 24-18 42t-42 18H220Zm331-554v-186H220v680h520v-494H551ZM220-820v186-186 680-680Z"/></svg></span> Step 2: GEMINI.md 設定

<div class="cols">
<div>

### GEMINI.md とは？

<div class="card card-lav">

AIへの**「取扱説明書」**

- 「日本語で答えて」
- 「コードにコメントを入れて」
- 「変数名はcamelCase」

毎回言わなくても **自動で従ってくれる**！

</div>

</div>
<div>

### プロジェクトルートのGEMINI.md

```markdown
# プロジェクト設定

## 基本ルール
- 常に日本語で応答
- コードにコメントを入れる

## 技術スタック
- HTML / CSS / JavaScript

## コーディング規約
- 変数名: camelCase
- ファイル名: kebab-case
```

</div>
</div>

<div class="card card-lav" style="margin-top:8px;">
<span class="ms ms-sm c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M422.5-103.5Q399-127 399-161h162q0 34-23.5 57.5T480-80q-34 0-57.5-23.5ZM318-223v-60h324v60H318Zm5-121q-66-43-104.5-107.5T180-597q0-122 89-211t211-89q122 0 211 89t89 211q0 81-38 145.5T637-344H323Zm22-60h271q48-32 76-83t28-110q0-99-70.5-169.5T480-837q-99 0-169.5 70.5T240-597q0 59 28 110t77 83Zm135 0Z"/></svg></span> <strong>試してみよう：</strong> チャットで <code>「Hello World」を表示するHTMLファイルを作成して</code>
</div>

---

<!-- _class: lead -->

<div class="center">

<div class="time-badge">20:00〜20:20</div>

<span class="ms ms-hero c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M320-242 80-482l242-242 43 43-199 199 197 197-43 43Zm318 2-43-43 199-199-197-197 43-43 240 240-242 242Z"/></svg></span>

# Step 3
## Vibe Coding 基礎編
### 🎨 自己紹介ページ + Nano Banana

</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M372-523q-42-42-42-108t42-108q42-42 108-42t108 42q42 42 42 108t-42 108q-42 42-108 42t-108-42ZM160-160v-94q0-38 19-65t49-41q67-30 128.5-45T480-420q62 0 123 15.5T731-360q31 14 50 41t19 65v94H160Zm60-60h520v-34q0-16-9.5-30.5T707-306q-64-31-117-42.5T480-360q-57 0-111 11.5T252-306q-14 7-23 21.5t-9 30.5v34Zm324.5-346.5Q570-592 570-631t-25.5-64.5Q519-721 480-721t-64.5 25.5Q390-670 390-631t25.5 64.5Q441-541 480-541t64.5-25.5ZM480-631Zm0 411Z"/></svg></span> ワーク1: 自己紹介ページを作ろう

<div class="cols">
<div>

### Part 1: HTML 生成（5分）

<div class="card card-blue">

```
新しいフォルダ「my-first-vibe」を作成して、
その中にシンプルなHTMLファイルを作って。
テーマは「自己紹介ページ」で、
モダンでおしゃれなデザインにして。
```

</div>

### Part 2: デザイン調整（5分）

<div class="card card-green" style="margin-top:8px;">

```
背景色をダークモードに変更して。
アクセントカラーは青緑系（#4ecca3）。
名前の部分にふわっとアニメーションを追加。
```

</div>

</div>
<div>

### Part 3: Nano Banana で画像生成（10分）

<div class="card card-orange">

```
Nano Bananaで、プロフィール用のアバター画像を生成。
- スタイル: アニメ風またはイラスト風
- 背景: シンプルなグラデーション
ファイル名は「avatar.png」で保存して。
```

</div>

<div class="card card-orange" style="margin-top:8px;">

```
生成したavatar.pngを自己紹介ページの
プロフィール欄に円形で配置して。
```

</div>

</div>
</div>

---

<!-- _class: bg-blue -->

# <span class="ms ms-lg c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m887-567-23-50-50-23 50-23 23-50 23 50 50 23-50 23-23 50ZM760-742l-35-74-74-35 74-35 35-74 35 74 74 35-74 35-35 74ZM302.5-103.5Q279-127 279-161h162q0 34-23.5 57.5T360-80q-34 0-57.5-23.5ZM198-223v-60h324v60H198Zm5-121q-66-43-104.5-107.5T60-597q0-122 89-211t211-89q122 0 211 89t89 211q0 81-38 145.5T517-344H203Zm22-60h271q48-32 76-83t28-110q0-99-70.5-169.5T360-837q-99 0-169.5 70.5T120-597q0 59 28 110t77 83Zm135 0Z"/></svg></span> Vibe Coding のコツ

<div class="cols-3">

<div class="card card-blue">
<div class="center"><span class="ms ms-lg c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M468-240q-96-5-162-74t-66-166q0-100 70-170t170-70q97 0 166 66t74 163l-63-20q-11-64-60-106.5T480-660q-75 0-127.5 52.5T300-480q0 67 42.5 116.5T449-303l19 63Zm48 158q-9 1-18 1.5t-18 .5q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 9-.5 18t-1.5 18l-58-18v-18q0-142-99-241t-241-99q-142 0-241 99t-99 241q0 142 99 241t241 99h18l18 58Zm305 22L650-231 600-80 480-480l400 120-151 50 171 171-79 79Z"/></svg></span></div>
<h3>具体的に伝える</h3>
<small>
❌ 「かっこいいページを作って」<br><br>
✅ 「ダークモード、青緑アクセント、グラスモーフィズムのカードデザイン」
</small>
</div>

<div class="card card-green">
<div class="center"><span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M250-250h157v-133h103v-133h103v-134h97v-60H553v133H450v133H347v134h-97v60Zm-70 130q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg></span></div>
<h3>段階的に進める</h3>
<small>
❌ 「完璧なポートフォリオを作って」<br><br>
✅ 「まずシンプルな自己紹介を作って」→「次にスキルを追加」
</small>
</div>

<div class="card card-lav">
<div class="center"><span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M259-200v-60h310q70 0 120.5-46.5T740-422q0-69-50.5-115.5T569-584H274l114 114-42 42-186-186 186-186 42 42-114 114h294q95 0 163.5 64T800-422q0 94-68.5 158T568-200H259Z"/></svg></span></div>
<h3>失敗を恐れない</h3>
<small>
「元に戻して」<br>
「別のパターンを3つ提案」<br>
「もっとシンプルに」<br><br>
AIとの対話は**やり取り自由**！
</small>
</div>

</div>

---

<!-- _class: lead -->

<div class="center">

<div class="time-badge">20:20〜20:40</div>

<span class="ms ms-hero c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M356-120H180q-24 0-42-18t-18-42v-176q44-5 75.5-34.5T227-463q0-43-31.5-72.5T120-570v-176q0-24 18-42t42-18h177q11-40 39.5-67t68.5-27q40 0 68.5 27t39.5 67h173q24 0 42 18t18 42v173q40 11 65.5 41.5T897-461q0 40-25.5 67T806-356v176q0 24-18 42t-42 18H570q-5-48-35.5-77.5T463-227q-41 0-71.5 29.5T356-120Zm-176-60h130q25-61 69.89-84t83-23Q501-287 546-264t70 84h130v-235h45q20 0 33-13t13-33q0-20-13-33t-33-13h-45v-239H511v-48q0-20-13-33t-33-13q-20 0-33 13t-13 33v48H180v130q48.15 17.82 77.58 59.69Q287-514.45 287-462.78 287-412 257.5-370T180-310v130Zm285-281Z"/></svg></span>

# Step 4-5
## MCP 接続 + Agent Skills

</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M442-180h76v-82l142-156v-191H300v191l142 155.7v82.3Zm-60 60v-118L240-394v-215q0-24.75 17.63-42.38Q275.25-669 300-669h72l-30 30v-201h60v171h156v-171h60v201l-30-30h72q24.75 0 42.38 17.62Q720-633.75 720-609v215L578-238v118H382Zm98-275Z"/></svg></span> Step 4: MCP とは？

<div class="cols">
<div>

### MCP = AIの「プラグイン」

<div class="card card-orange">

**Model Context Protocol**

AIエージェントと外部システムを
安全に接続するためのオープン標準

<br>

単体では「できなかったこと」が
**拡張機能を追加するだけで可能に！**

</div>

</div>
<div>

### できること

<div class="card card-green">
<span class="ms ms-sm c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M458-81q-79-4-148-37t-120-86.5Q139-258 109.5-329T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q149 0 259 94t135 236h-61q-17-84-71-150t-135-99v18q0 35-24 61t-59 26h-87v87q0 17-13.5 28T393-568h-83v88h110v125h-67L149-559q-5 20-7 39.5t-2 39.5q0 135 91 233t227 106v60Zm392-26L716-241q-21 15-45.5 23t-50.5 8q-71 0-120.5-49.5T450-380q0-71 49.5-120.5T620-550q71 0 120.5 49.5T790-380q0 26-8.5 50.5T759-283l134 133-43 43ZM698-302q32-32 32-78t-32-78q-32-32-78-32t-78 32q-32 32-32 78t32 78q32 32 78 32t78-32Z"/></svg></span> <strong>Browser Subagent</strong><br>
<small>ブラウザを自律操作してWebリサーチ・確認</small>
</div>

<div class="card card-blue" style="margin-top:8px;">
<span class="ms ms-sm c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M319-250h322v-60H319v60Zm0-170h322v-60H319v60ZM220-80q-24 0-42-18t-18-42v-680q0-24 18-42t42-18h361l219 219v521q0 24-18 42t-42 18H220Zm331-554v-186H220v680h520v-494H551ZM220-820v186-186 680-680Z"/></svg></span> <strong>context7</strong><br>
<small>最新ライブラリドキュメントをリアルタイム参照</small>
</div>

<div class="card card-lav" style="margin-top:8px;">
<span class="ms ms-sm c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m379-343 44-44-93-93 92-92-44-44-136 136 137 137Zm202 0 137-137-137-137-44 44 93 93-93 93 44 44ZM180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg></span> <strong>GitHub / Slack / DB</strong><br>
<small>外部サービスをAIが直接操作</small>
</div>

</div>
</div>

---

<!-- _class: bg-orange -->

# <span class="ms ms-lg c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M160-740v-60h642v60H160Zm5 580v-258h-49v-60l44-202h641l44 202v60h-49v258h-60v-258H547v258H165Zm60-60h262v-198H225v198Zm-50-258h611-611Zm0 0h611l-31-142H206l-31 142Z"/></svg></span> MCP の追加方法

<div class="cols">
<div>

### MCP Store（推奨）

<div class="card card-orange">

1. Agent Manager 右上の `...` をクリック
2. **MCP Store** を選択
3. 使いたいサーバーを **Install** するだけ！

<br>

GUIで簡単に追加・管理できる ✅

</div>

</div>
<div>

### 試してみよう！

<div class="card card-green">

```
Browser MCPを使って、
「Antigravity IDE 2026」を検索して、
トップ3件の記事タイトルを教えて。
```

</div>

<div class="card card-blue" style="margin-top:10px;">

```
Context7 MCPを使って、
React の useEffect フックの
最新の使い方を調べて教えて。
```

</div>

</div>
</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M240-80v-172q-57-52-88.5-121.5T120-520q0-150 105-255t255-105q125 0 221.5 73.5T827-615l55 218q4 14-5 25.5T853-360h-93v140q0 24.75-17.62 42.37Q724.75-160 700-160H600v80h-60v-140h160v-200h114l-45-180q-24-97-105-158.5T480-820q-125 0-212.5 86.5T180-522.46q0 64.42 26.32 122.39Q232.65-342.09 281-297l19 18v199h-60Zm257-370Zm-48 76h60l3-44q12-2 22.47-8.46Q544.94-432.92 553-441l42 14 28-48-30-24q5-14 5-29t-5-29l30-24-28-48-42 14q-8.33-7.69-19.17-13.85Q523-635 512-638l-3-44h-60l-3 44q-11 3-21.83 9.15Q413.33-622.69 405-615l-42-14-28 48 30 24q-5 14-5 29t5 29l-30 24 28 48 42-14q8.06 8.08 18.53 14.54Q434-420 446-418l3 44Zm-19.5-104.38q-20.5-20.38-20.5-49.5t20.38-49.62q20.38-20.5 49.5-20.5t49.62 20.38q20.5 20.38 20.5 49.5t-20.38 49.62q-20.38 20.5-49.5 20.5t-49.62-20.38Z"/></svg></span> Step 5: Agent Skills

<div class="cols">
<div>

### Skills = AIへの「技能追加」

<div class="card card-lav">

「コードレビューのやり方」
「テストの作り方」などを
マニュアル化して、
AIが同じ品質で実行できる。

<br>

`.agent/skills/<name>/SKILL.md`
に定義するだけ！

</div>

</div>
<div>

### 試してみよう！

<div class="card card-blue">

```
@code-review で sample.js をレビューして
```

</div>

<div class="card card-lav" style="margin-top:10px;">

**Rules / Workflows / Skills の違い**

| 機能 | 発動方法 |
|:---|:---|
| Rules | 常に自動適用 |
| Workflows | `/ワークフロー名` |
| Skills | `@スキル名` or 自動判断 |

</div>

</div>
</div>

---

<!-- _class: lead -->

<div class="center">

<div class="time-badge">20:40〜21:00</div>

<span class="ms ms-hero c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M442-242q-116 0-199-80t-83-195v-263q0-25 17.5-42.5T220-840h529q54 0 92.5 37t38.5 91q0 60-37 106t-94 46h-25v43q0 115-83 195t-199 80ZM220-620h444v-160H220v160Zm222 318q91 0 156.5-62T664-517v-43H220v43q0 91 65.5 153T442-302Zm282-318h25q33 0 52-28.5t19-63.5q0-29-21-48.5T749-780h-25v160ZM160-120v-60h640v60H160Zm282-440Z"/></svg></span>

# Step 6
## Vibe Coding 発展編
### 🚀 AI Coffee Shop LP 構築

</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M160-120v-60h640v60H160Zm151-140q-63 0-107-43.5T160-410v-430h660q24.75 0 42.38 17.62Q880-804.75 880-780v160q0 24.75-17.62 42.37Q844.75-560 820-560h-96v150q0 63-44 106.5T573-260H311Zm0-60h261.98q36.02 0 63.52-27.5T664-410v-370H220v370q0 35 28 62.5t63 27.5Zm413-300h96v-160h-96v160ZM311-320h-91 444-353Z"/></svg></span> ワーク2: AI Coffee Shop LP

### 全体フロー（20分で本格LPを！）

<div class="cols">
<div>

<div class="card card-blue" style="margin-bottom:8px;">
<span class="step-badge step-blue">① Web リサーチ</span><br>
<small>Browser MCP で競合分析・トレンド調査</small>
</div>

<div class="card card-lav" style="margin-bottom:8px;">
<span class="step-badge step-lav">② 構成決定</span><br>
<small>AI と一緒にキャッチコピー・セクション設計</small>
</div>

<div class="card card-orange" style="margin-bottom:8px;">
<span class="step-badge step-orange">③ 画像生成</span><br>
<small>Nano Banana でヒーロー画像・アイコン生成</small>
</div>

</div>
<div>

<div class="card card-green" style="margin-bottom:8px;">
<span class="step-badge step-green">④ 実装</span><br>
<small>Vite + React + TailwindCSS を AI がセットアップ</small>
</div>

<div class="card card-blue" style="margin-bottom:8px;">
<span class="step-badge step-blue">⑤ 品質チェック</span><br>
<small>@code-review Skill でコードレビュー自動化</small>
</div>

<div class="card card-lav">
<span class="step-badge step-lav">⑥ デプロイ準備</span><br>
<small>Firebase Hosting の設定まで AI にお任せ</small>
</div>

</div>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M796-121 533-384q-30 26-70 40.5T378-329q-108 0-183-75t-75-181q0-106 75-181t182-75q106 0 180.5 75T632-585q0 43-14 83t-42 75l264 262-44 44ZM377-389q81 0 138-57.5T572-585q0-81-57-138.5T377-781q-82 0-139.5 57.5T180-585q0 81 57.5 138.5T377-389Z"/></svg></span> Part 1: Web リサーチ（MCP活用）

<div class="card card-blue">

```
Browser MCPを使って、「おしゃれなカフェ ランディングページ」で検索して、
上位5サイトのデザインの特徴を分析して。

特に以下の点をまとめて：
- 色使い
- レイアウト
- CTAボタンのデザイン
- 画像の使い方
```

</div>

<br>

<div class="cols">
<div class="card card-lav">
<span class="ms ms-sm c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M147-376q-45 0-76-31.21T40-483q0-44.58 31.21-75.79Q102.42-590 147-590v-123q0-24 18-42t42-18h166q0-45 31-76t76-31q45 0 76 31.21T587-773h166q24 0 42 18t18 42v123q45 0 76 31.21T920-483q0 44.58-31.21 75.79Q857.58-376 813-376v196q0 24-18 42t-42 18H207q-24 0-42-18t-18-42v-196Zm224.5-111.74q11.5-11.73 11.5-28.5 0-16.76-11.74-28.26-11.73-11.5-28.5-11.5-16.76 0-28.26 11.74-11.5 11.73-11.5 28.5 0 16.76 11.74 28.26 11.73 11.5 28.5 11.5 16.76 0 28.26-11.74Zm274 0q11.5-11.73 11.5-28.5 0-16.76-11.74-28.26-11.73-11.5-28.5-11.5-16.76 0-28.26 11.74-11.5 11.73-11.5 28.5 0 16.76 11.74 28.26 11.73 11.5 28.5 11.5 16.76 0 28.26-11.74ZM312-285h336v-60H312v60ZM207-180h546v-533H207v533Zm273-267Z"/></svg></span> AIがブラウザを自動操作して検索
</div>
<div class="card card-lav">
<span class="ms ms-sm c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M454-602h345q-28-74-89-130.5T571-810L454-602Zm-93 83 174-299q-12-1-27-1.5t-28-.5q-72 0-132 26t-108 72l121 203ZM150-393h237L217-696q-38 45-57.5 100.5T140-480q0 21 2 44t8 43Zm240 242 120-207H162q28 74 88.5 130.5T390-151Zm90 11q72 0 132.5-26T720-238L600-441 425-142q13 1 27.5 1.5t27.5.5Zm264-124q34-42 55-99t21-117q0-22-2-44.5t-7-43.5H574l170 304ZM480-480Zm0 400q-82 0-155-31.5t-127.5-86Q143-252 111.5-325T80-480q0-83 31.5-155.5t86-127Q252-817 325-848.5T480-880q83 0 155.5 31.5t127 86q54.5 54.5 86 127T880-480q0 82-31.5 155t-86 127.5q-54.5 54.5-127 86T480-80Z"/></svg></span> 各サイトのスクリーンショットを取得
</div>
<div class="card card-lav">
<span class="ms ms-sm c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M284-277h60v-205h-60v205Zm332 0h60v-420h-60v420Zm-166 0h60v-118h-60v118Zm0-205h60v-60h-60v60ZM180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg></span> デザイン特徴をレポート出力
</div>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm56-97h489L578-473 446-302l-93-127-117 152Zm-56 97v-600 600Z"/></svg></span> Part 3: Nano Banana で画像生成

<div class="cols">
<div>

### ヒーロー画像

<div class="card card-green">

```
Nano Banana で、

「近未来的なカフェの店内、
 ネオンブルーとウォームライト、
 観葉植物、4K、フォトリアリスティック」

ファイル名: hero-bg.webp
```

</div>

</div>
<div>

### アイコン3点セット

<div class="card card-blue">

```
以下の3つのアイコンを生成して:
1. コーヒーカップ（AI抽出の象徴）
2. 植物（サステナビリティ）
3. スマホ（モバイルオーダー）

スタイル: ミニマル、線画、白背景
```

</div>

</div>
</div>

---

<!-- _class: bg-green -->

# <span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M473.5-303.5Q517-305 537-336l216-339-335 219q-30 20-32 64t21 67q23 23 66.5 21.5ZM478-799q57 0 119 18.5T716-717l-52 37q-45-30-96.5-44.5T477.98-739q-140.47 0-239.23 100.22Q140-538.57 140-396.02 140-351 152.5-305q12.5 46 35.5 85h579q22-36 35-84t13-94q0-42-12.5-90.5T758-578l39-52q38 56 57 112.5T875-404q2 60-12 113t-41 98q-12 23-25.5 28t-33.5 5H192q-17 0-33.5-8.5T134-193q-26-48-40-97.5T80-396q0-83 31.5-156.5t85.5-128Q251-735 323.68-767T478-799Zm-9 331Z"/></svg></span> 発展編：開発速度の比較

<div class="center" style="margin-bottom:12px;">
<strong>同じ成果物を出す場合の所要時間</strong>
</div>

| 作業 | 従来の開発 | Step 3（基礎） | Step 6（発展） |
|:---|:---:|:---:|:---:|
| リサーチ | 2時間 | — | **10分** |
| デザイン | 4時間 | 20分 | **15分** |
| 実装 | 8時間 | 30分 | **20分** |
| レビュー | 2時間 | — | **5分** |
| **合計** | **16時間** | **50分** | **50分** |

<br>

<div class="card card-green">
<span class="ms ms-sm c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m393-165 279-335H492l36-286-253 366h154l-36 255Zm-73 85 40-280H160l360-520h80l-40 320h240L400-80h-80Zm154-396Z"/></svg></span> MCP + Skills を組み合わせると、<strong>リサーチとレビューが自動化</strong>され、より複雑なプロジェクトにも対応！
</div>

---

<!-- _class: lead -->

<div class="center">

<div class="time-badge">21:00〜21:10</div>

<span class="ms ms-hero c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M298-120v-60h152v-148q-54-11-96-46.5T296-463q-74-8-125-60t-51-125v-44q0-25 17.5-42.5T180-752h104v-88h392v88h104q25 0 42.5 17.5T840-692v44q0 73-51 125t-125 60q-16 53-58 88.5T510-328v148h152v60H298Zm-14-406v-166H180v44q0 45 29.5 78.5T284-526Zm292.5 101q39.5-40 39.5-97v-258H344v258q0 57 39.5 97t96.5 40q57 0 96.5-40ZM676-526q45-10 74.5-43.5T780-648v-44H676v166Zm-196-57Z"/></svg></span>

# Step 7
## AI-DLC × ハッカソン最強戦略

</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M196-331q-20-36-28-72.5t-8-74.5q0-131 94.5-225.5T480-798h43l-80-80 39-39 149 149-149 149-40-40 79-79h-41q-107 0-183.5 76.5T220-478q0 29 5.5 55t13.5 49l-43 43ZM476-40 327-189l149-149 39 39-80 80h45q107 0 183.5-76.5T740-479q0-29-5-55t-15-49l43-43q20 36 28.5 72.5T800-479q0 131-94.5 225.5T480-159h-45l80 80-39 39Z"/></svg></span> AI-DLC とは？

<div class="cols">
<div>

### 従来の AI 支援型開発

<div class="card card-pink">

- **人間が主導**し、AIに指示
- AIは部分的なコーディング補助
- 認識のズレによる手戻りが多い

</div>

</div>
<div>

### AI-DLC（AI-Driven Dev Lifecycle）

<div class="card card-green">

- **AIがワークフローを主導**
- 人間は承認・方向修正に集中
- 要件定義〜デプロイまで AI が担う

</div>

</div>
</div>

<br>

<div class="cols-3">

<div class="card card-blue">
<div class="center"><span class="ms ms-lg c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M422.5-103.5Q399-127 399-161h162q0 34-23.5 57.5T480-80q-34 0-57.5-23.5ZM318-223v-60h324v60H318Zm5-121q-66-43-104.5-107.5T180-597q0-122 89-211t211-89q122 0 211 89t89 211q0 81-38 145.5T637-344H323Zm22-60h271q48-32 76-83t28-110q0-99-70.5-169.5T480-837q-99 0-169.5 70.5T240-597q0 59 28 110t77 83Zm135 0Z"/></svg></span></div>
<strong>① Inception</strong><br>
<small>アイデア → 要件 → 計画</small>
</div>

<div class="card card-orange">
<div class="center"><span class="ms ms-lg c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M705-128 447-388q-23 8-46 13t-47 5q-97.08 0-165.04-67.67Q121-505.33 121-602q0-31 8.16-60.39T152-718l145 145 92-86-149-149q25.91-15.16 54.96-23.58Q324-840 354-840q99.17 0 168.58 69.42Q592-701.17 592-602q0 24-5 47t-13 46l259 258q11 10.96 11 26.48T833-198l-76 70q-10.7 11-25.85 11Q716-117 705-128Zm28-57 40-40-273-273q16-21 24-49.5t8-54.5q0-75-55.5-127T350-782l102 104q9 9 8.5 21.5T451-635L318-510q-9.27 8-21.64 8-12.36 0-20.36-8l-98-97q3 77 54.67 127T354-430q25 0 53-8t49-24l277 277ZM476-484Z"/></svg></span></div>
<strong>② Construction</strong><br>
<small>コード・テスト・デザイン</small>
</div>

<div class="card card-lav">
<div class="center"><span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m187-551 106 45q18-36 38.5-71t43.5-67l-79-16-109 109Zm154 81 133 133q57-26 107-59t81-64q81-81 119-166t41-192q-107 3-192 41T464-658q-31 31-64 81t-59 107Zm209-145.5q0-29.5 20-49.5t49.5-20q29.5 0 49.5 20t20 49.5q0 29.5-20 49.5t-49.5 20q-29.5 0-49.5-20t-20-49.5Zm5 432.5 109-109-16-79q-32 23-67 43.5T510-289l45 106Zm326-694q9 136-34 248T705-418l-2 2-2 2 22 110q3 15-1.5 29T706-250L535-78l-85-198-170-170-198-85 172-171q11-11 25-15.5t29-1.5l110 22q1-1 2-1.5t2-1.5q99-99 211-142.5T881-877ZM149-325q35-35 85.5-35.5T320-326q35 35 34.5 85.5T319-155q-26 26-80.5 43T75-80q15-109 31.5-164t42.5-81Zm42 43q-14 15-25 47t-19 82q50-8 82-19t47-25q19-17 19.5-42.5T278-284q-19-18-44.5-17.5T191-282Z"/></svg></span></div>
<strong>③ Operations</strong><br>
<small>デプロイ・改善サイクル</small>
</div>

</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M0-240v-53q0-38.57 41.5-62.78Q83-380 150.38-380q12.16 0 23.39.5t22.23 2.15q-8 17.35-12 35.17-4 17.81-4 37.18v65H0Zm240 0v-65q0-32 17.5-58.5T307-410q32-20 76.5-30t96.5-10q53 0 97.5 10t76.5 30q32 20 49 46.5t17 58.5v65H240Zm540 0v-65q0-19.86-3.5-37.43T765-377.27q11-1.73 22.17-2.23 11.17-.5 22.83-.5 67.5 0 108.75 23.77T960-293v53H780Zm-480-60h360v-6q0-37-50.5-60.5T480-390q-79 0-129.5 23.5T300-305v5ZM149.57-410q-28.57 0-49.07-20.56Q80-451.13 80-480q0-29 20.56-49.5Q121.13-550 150-550q29 0 49.5 20.5t20.5 49.93q0 28.57-20.5 49.07T149.57-410Zm660 0q-28.57 0-49.07-20.56Q740-451.13 740-480q0-29 20.56-49.5Q781.13-550 810-550q29 0 49.5 20.5t20.5 49.93q0 28.57-20.5 49.07T809.57-410ZM480-480q-50 0-85-35t-35-85q0-51 35-85.5t85-34.5q51 0 85.5 34.5T600-600q0 50-34.5 85T480-480Zm.35-60Q506-540 523-557.35t17-43Q540-626 522.85-643t-42.5-17q-25.35 0-42.85 17.15t-17.5 42.5q0 25.35 17.35 42.85t43 17.5ZM480-300Zm0-300Z"/></svg></span> ハッカソン最強戦略：モブ開発 × AI

<div class="cols">
<div>

### モブエラボレーション

<div class="card card-lav">

ハッカソン**最初の1時間**を全員で！

1. 1人が Antigravity を**画面共有**
2. AIが出した**要件・計画書**を全員で確認
3. 「ここは違う」「これを追加」と**リアルタイム修正**
4. 計画が固まったら「**Proceed**」→ AI がコード生成

</div>

</div>
<div>

### 勝つための3つのルール

<div class="card card-blue" style="margin-bottom:8px;">
<span class="ms ms-sm c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M492-277h60v-406H409v60h83v346ZM180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg></span> <strong>最初にモブエラボレーション</strong><br>
<small>全員でAIの計画を見て合意を取る</small>
</div>

<div class="card card-green" style="margin-bottom:8px;">
<span class="ms ms-sm c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M365-277h230v-60H425v-115h110q24 0 42-18t18-42v-111q0-24-18-42t-42-18H365v60h170v111H425q-24 0-42 18t-18 42v175ZM180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg></span> <strong>コードはAIに任せ、人間は判断に集中</strong><br>
<small>フレームワーク選定・デザイン方針・審査基準</small>
</div>

<div class="card card-orange">
<span class="ms ms-sm c-orange" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M365-277h170q24 0 42-18t18-42v-87q0-27-14.5-42.5T546-482q20 0 34.5-13.5T595-537v-86q0-24-18-42t-42-18H365v60h170v111h-87v60h87v115H365v60ZM180-120q-24 0-42-18t-18-42v-600q0-24 18-42t42-18h600q24 0 42 18t18 42v600q0 24-18 42t-42 18H180Zm0-60h600v-600H180v600Zm0-600v600-600Z"/></svg></span> <strong>デモの見栄えを重視</strong><br>
<small>Nano Banana で画像、Browser Subagent で最終確認</small>
</div>

</div>
</div>

---

<!-- _class: lead -->

<div class="center">

<span class="ms ms-hero c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m80-80 186-520 337 333L80-80Zm101-101 314-112-203-204-111 316Zm376-264-34-34 240-240q32-32 81-32.5t81 31.5l17 17-34 34-19-19q-19-19-44-19.5T800-688L557-445ZM398-600l-34-34 30-30q23-23 21.5-52.5T394-766l-28-28 34-34 26 26q35 35 34.5 87.5T425-627l-27 27Zm81 77-34-34 152-152q19-19 18.5-48.5T596-806l-61-61 34-34 63 63q31 32 32 80.5T633-677L479-523Zm158 159-34-34 47-47q35-35 84-36t84 34l51 51-34 34-52-52q-23-23-48-23t-48 23l-50 50ZM181-181Z"/></svg></span>

# おつかれさまでした！

<br>

<div class="cols-3">

<div class="card card-blue">
<span class="ms ms-lg c-blue" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m421-298 283-283-46-45-237 237-120-120-45 45 165 166Zm59 218q-82 0-155-31.5t-127.5-86Q143-252 111.5-325T80-480q0-83 31.5-156t86-127Q252-817 325-848.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 82-31.5 155T763-197.5q-54 54.5-127 86T480-80Zm0-60q142 0 241-99.5T820-480q0-142-99-241t-241-99q-141 0-240.5 99T140-480q0 141 99.5 240.5T480-140Zm0-340Z"/></svg></span><br>
<strong>Antigravity</strong><br>
<small>基本操作 マスター</small>
</div>

<div class="card card-green">
<span class="ms ms-lg c-green" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m421-298 283-283-46-45-237 237-120-120-45 45 165 166Zm59 218q-82 0-155-31.5t-127.5-86Q143-252 111.5-325T80-480q0-83 31.5-156t86-127Q252-817 325-848.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 82-31.5 155T763-197.5q-54 54.5-127 86T480-80Zm0-60q142 0 241-99.5T820-480q0-142-99-241t-241-99q-141 0-240.5 99T140-480q0 141 99.5 240.5T480-140Zm0-340Z"/></svg></span><br>
<strong>Vibe Coding</strong><br>
<small>基礎〜発展 体験</small>
</div>

<div class="card card-lav">
<span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="m421-298 283-283-46-45-237 237-120-120-45 45 165 166Zm59 218q-82 0-155-31.5t-127.5-86Q143-252 111.5-325T80-480q0-83 31.5-156t86-127Q252-817 325-848.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 82-31.5 155T763-197.5q-54 54.5-127 86T480-80Zm0-60q142 0 241-99.5T820-480q0-142-99-241t-241-99q-141 0-240.5 99T140-480q0 141 99.5 240.5T480-140Zm0-340Z"/></svg></span><br>
<strong>AI-DLC</strong><br>
<small>ハッカソン戦略 理解</small>
</div>

</div>

<br>

<div class="card card-lav" style="display:inline-block; padding: 10px 32px;">
<strong>公式ドキュメント:</strong> <code>https://antigravity.google/docs</code>
</div>

</div>

---

<!-- _class: bg-lav -->

# <span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;"><svg class="ms-svg" fill="currentColor" width="1em" height="1em" xmlns="http://www.w3.org/2000/svg" height="48" viewBox="0 -960 960 960" width="48"><path d="M560-574v-48q33-14 67.5-21t72.5-7q26 0 51 4t49 10v44q-24-9-48.5-13.5T700-610q-38 0-73 9.5T560-574Zm0 220v-49q33-13.5 67.5-20.25T700-430q26 0 51 4t49 10v44q-24-9-48.5-13.5T700-390q-38 0-73 9t-67 27Zm0-110v-48q33-14 67.5-21t72.5-7q26 0 51 4t49 10v44q-24-9-48.5-13.5T700-500q-38 0-73 9.5T560-464ZM248-300q53.57 0 104.28 12.5Q403-275 452-250v-427q-45-30-97.62-46.5Q301.76-740 248-740q-38 0-74.5 9.5T100-707v434q31-14 70.5-20.5T248-300Zm264 50q50-25 98-37.5T712-300q38 0 78.5 6t69.5 16v-429q-34-17-71.82-25-37.82-8-76.18-8-54 0-104.5 16.5T512-677v427Zm-30 90q-51-38-111-58.5T248-239q-36.54 0-71.77 9T106-208q-23.1 11-44.55-3Q40-225 40-251v-463q0-15 7-27.5T68-761q42-20 87.39-29.5 45.4-9.5 92.61-9.5 63 0 122.5 17T482-731q51-35 109.5-52T712-800q46.87 0 91.93 9.5Q849-781 891-761q14 7 21.5 19.5T920-714v463q0 27.89-22.5 42.45Q875-194 853-208q-34-14-69.23-22.5Q748.54-239 712-239q-63 0-121 21t-109 58ZM276-489Z"/></svg></span> 学習リソース

<div class="cols">
<div>

### 公式ドキュメント

<div class="card card-lav">

- [Get Started](https://antigravity.google/docs/get-started)
- [Rules & Workflows](https://antigravity.google/docs/rules-workflows)
- [MCP](https://antigravity.google/docs/mcp)
- [Skills](https://antigravity.google/docs/skills)
- [Tab (Supercomplete)](https://antigravity.google/docs/tab)

</div>

</div>
<div>

### このハンズオン資料

<div class="card card-blue">

各 Step の README.md で詳細な手順と
サンプルプロンプトを確認できます！

```
handson/
├── 01_setup/README.md
├── 02_gemini_md/README.md
├── 03_vibe_coding_basic/README.md
├── 04_mcp/README.md
├── 05_skills/README.md
├── 06_vibe_coding_advanced/README.md
└── 07_ai_dlc/README.md
```

</div>

</div>
</div>
