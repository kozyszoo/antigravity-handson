---
name: marp-presentation
description: Marp形式でパステルカラーのプレゼンテーションを作成する
---

# Marp Presentation Creator

Marp形式で美しいパステルカラーのプレゼンテーションスライドを作成するスキルです。

## 使用シーン

- 学生向けプレゼンテーション資料の作成
- Markdown形式でのスライド作成
- パステルカラー調のモダンなデザインが必要な場合
- Material Symbolsアイコンを使用したビジュアル重視のスライド

## 前提条件

- Marp CLIがインストールされていること (`npm install -g @marp-team/marp-cli`)
- Google Fonts (Noto Sans JP, JetBrains Mono) が利用可能であること
- Material Symbols Outlined が利用可能であること

## 基本構成

### 1. ファイル構造

```
presentation.md      # Marpスライドのソース
presentation.pptx    # 生成されたPowerPointファイル
presentation.pdf     # 生成されたPDFファイル (オプション)
```

### 2. Marpテーマ設定

**MarpマークダウンのYAMLフロントマター:**

```yaml
---
marp: true
theme: default
paginate: true
style: |
  /* カラーパレット（パステル調） */
  /* Blue: #a8d8ea, Pink: #f6c6ea, Green: #c1e6c0, Orange: #ffe0ac, Lavender: #d5c6e0 */
```

### 3. カラーパレット（パステル調）

| 色 | カラーコード | 用途 |
|:---|:---|:---|
| **Blue** | `#a8d8ea` / `#6daad8` | メイン、技術 |
| **Pink** | `#f6c6ea` / `#e08ac0` | 課題、警告 |
| **Green** | `#c1e6c0` / `#6bb86a` | 成功、実装 |
| **Orange** | `#ffe0ac` / `#e0a050` | 注意、ヒント |
| **Lavender** | `#d5c6e0` / `#9b82b5` | 概念、まとめ |

### 4. Material Symbolsアイコン

**アイコンサイズクラス:**

```css
.ms          { font-size: 38px; }  /* 基本サイズ */
.ms-lg       { font-size: 50px; }  /* 大きめ */
.ms-xl       { font-size: 64px; }  /* 特大 */
.ms-hero     { font-size: 96px; }  /* ヒーロー表示 */
```

**アイコンカラークラス:**

```css
.c-blue      { color: #6daad8; }
.c-pink      { color: #e08ac0; }
.c-green     { color: #6bb86a; }
.c-orange    { color: #e0a050; }
.c-lav       { color: #9b82b5; }
```

**使用例:**

```html
<span class="ms ms-lg c-blue">rocket_launch</span>
<span class="ms ms-hero c-lav">favorite</span>
```

## デザインガイドライン

### 1. スライド背景

**フラットカラーを使用**（グラデーションは避ける）:

```css
section           { background: #faf5ff; }
section.lead      { background: #e8ddf4; }
section.bg-blue   { background: #e0f0fa; }
section.bg-pink   { background: #fdeef6; }
section.bg-green  { background: #eaf6ea; }
section.bg-orange { background: #fdf4e8; }
section.bg-lav    { background: #efe8f6; }
```

### 2. タイポグラフィ

```css
/* 基本設定 */
section {
  font-family: 'Noto Sans JP', sans-serif;
  font-size: 24px;
  line-height: 1.6;
  padding: 40px 60px;
}

/* 見出し */
h1 { font-size: 38px; font-weight: 900; }
h2 { font-size: 27px; font-weight: 700; }
h3 { font-size: 20px; font-weight: 700; }
```

### 3. カードUI

```css
.card {
  border-radius: 12px;
  padding: 14px 18px;
  margin: 4px 0;
  box-shadow: 0 3px 12px rgba(90,70,120,0.06);
}

.card-blue   { background: rgba(168,216,234,0.28); border: 2px solid #a8d8ea; }
.card-pink   { background: rgba(246,198,234,0.28); border: 2px solid #f6c6ea; }
.card-green  { background: rgba(193,230,192,0.28); border: 2px solid #c1e6c0; }
.card-orange { background: rgba(255,224,172,0.28); border: 2px solid #ffe0ac; }
.card-lav    { background: rgba(213,198,224,0.28); border: 2px solid #d5c6e0; }
```

### 4. レイアウトユーティリティ

```css
/* カラムレイアウト */
.cols   { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.cols-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; }

/* テキスト揃え */
.center { text-align: center; }

/* フレックスレイアウト */
.gap { display: flex; flex-wrap: wrap; gap: 10px; }
```

## スライド内に収める調整

### 要素が収まらない場合のチェックリスト

1. **padding/marginの削減**
   ```css
   /* カード */
   padding: 14px 18px → padding: 10px 16px
   margin: 4px 0 → margin: 6px 0
   
   /* 見出し */
   margin-bottom: 8px → margin-bottom: 4px
   ```

2. **フォントサイズの縮小**
   ```css
   font-size: 24px → font-size: 22px
   ```

3. **テーブルの圧縮**
   ```css
   th { padding: 8px 14px; font-size: 18px; }
   td { padding: 7px 14px; font-size: 17px; }
   ```

4. **コードブロックの簡潔化**
   - 空行を削除
   - コメントを短縮
   - 複数行を1行にまとめる

5. **カラム間隔の調整**
   ```css
   gap: 24px → gap: 16px
   gap: 18px → gap: 12px
   ```

### HTMLブロック内での太字

**注意**: HTMLブロック内では `**太字**` が効かないため、`<strong>` を使用する:

```html
<!-- ❌ 効かない -->
<div>**Manager View** が受け取る</div>

<!-- ✅ 正しい -->
<div><strong>Manager View</strong> が受け取る</div>
```

## PPTXへの変換

### 基本変換

```bash
marp presentation.md --pptx -o presentation.pptx
```

### 編集可能なPPTXとして変換

```bash
marp presentation.md --pptx --pptx-editable -o presentation.pptx
```

**`--pptx-editable` のメリット:**
- テキストボックスや図形が個別に編集可能
- PowerPointでより細かい調整ができる

**注意点:**
- 実験的機能のため、完全な再現性は保証されない
- LibreOffice経由で変換されるため、若干のスタイル変更が発生する可能性がある

### PDFへの変換

```bash
marp presentation.md --pdf -o presentation.pdf
```

## ベストプラクティス

### 1. ファイル構成

```markdown
---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400&display=swap');
  
  /* ここにCSSを記述 */
---

<!-- _class: lead -->
# タイトル

---

<!-- _class: bg-blue -->
# コンテンツスライド
```

### 2. アイコンの効果的な使用

- 見出しには必ずアイコンを付ける
- `.ms-lg` 以上を使用して視認性を確保
- カラークラスで統一感を出す

### 3. カードUIの活用

重要な情報やセクションをカードで囲むことで視覚的に分離:

```html
<div class="card card-blue">
<h3><span class="ms c-blue">lightbulb</span> ポイント</h3>
<p>ここに重要な情報を記載</p>
</div>
```

### 4. レスポンシブなレイアウト

複数列レイアウトには `.cols` や `.cols-3` を使用:

```html
<div class="cols">
  <div class="card card-blue">左カラム</div>
  <div class="card card-pink">右カラム</div>
</div>
```

## トラブルシューティング

### 問題: スライドがはみ出る

**解決策:**
1. カード・ボックスの `padding` を `10px 16px` に削減
2. `margin` を `6px 0` または `4px 0` に削減
3. h3 の `margin-bottom` を `4px` に設定
4. テキストを簡潔にする

### 問題: アイコンが小さすぎる

**解決策:**
1. `.ms` のデフォルトサイズを `38px` に設定
2. 見出しには `.ms-lg` (50px) 以上を使用
3. ヒーローセクションには `.ms-hero` (96px) を使用

### 問題: 太字が効かない

**解決策:**
HTMLブロック内では `<strong>` タグを使用する。

### 問題: フォントが表示されない（PPTX）

**解決策:**
- 編集環境にGoogle Fontsをインストール
- または、PowerPoint上でフォントを手動で調整

## まとめ

このスキルを使用することで:
- ✅ パステルカラーの美しいプレゼンテーションを作成
- ✅ Material Symbolsで視覚的に魅力的なスライドを実現
- ✅ Markdownで効率的に編集
- ✅ PPTX/PDFに簡単に変換

**参考コマンド一覧:**

```bash
# プレビュー
marp -s presentation.md

# PDF生成
marp presentation.md --pdf -o presentation.pptx

# PPTX生成（基本）
marp presentation.md --pptx -o presentation.pptx

# PPTX生成（編集可能）
marp presentation.md --pptx --pptx-editable -o presentation.pptx
```
