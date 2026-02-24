---
title: "Step 5: Agent Skills の作成"
---

## 目標
カスタム Skill を作り、エージェントに新しい能力を追加しましょう。

---

## Agent Skills とは

Skills は、特定のタスクを実行する手順をパッケージ化してエージェントに教える機能です。

簡単に言うと、**「AIに新しい『技能』を教える機能」**です。「コードレビューのやり方」「テストの作り方」など、担当者が持つ知識をマニュアル化して、AIが同じ品質で作業できるようになります。[agentskills.io](https://agentskills.io) のオープン標準に基づいています。

<!--
  [図9: Rules / Workflows / Skills の比較図]
  【図形生成プロンプト】
  Rules / Workflows / Skills の3つの機能を比較したカード横並び図。
  3枚のカードを横に並べて表示する:

  カード 1（淡紫 / Rules）:
    - アイコン: 歌車アイコン（「常に守るルール」のイメージ）
    - 見出し: 「Rules」
    - 説明: 「常に有効。設定しておけば動く」
    - 例: 「コーディング規約」「応答言語」
    - 発動方法: 「Always On / @ファイル名」

  カード 2（淡青 / Workflows）:
    - アイコン: フローチャートアイコン（「手順の自動実行」のイメージ）
    - 見出し: 「Workflows」
    - 説明: 「コマンドで呼び出す」
    - 例: 「/hello」「/deploy」
    - 発動方法: 「/ワークフロー名」

  カード 3（淡緑 / Skills）:
    - アイコン: 脳アイコン（「専門能力の追加」のイメージ）
    - 見出し: 「Skills」
    - 説明: 「専門知識を追加」
    - 例: 「@code-review」「@generate-test」
    - 発動方法: 「@スキル名 / AI が自動判断」

  背景: 白 (#ffffff)。カード内は各色で屈れる。サイズ: 800×400px。
-->

> 公式ドキュメント: https://antigravity.google/docs/skills

### Skills の構造

Skills は `SKILL.md` ファイルを含むフォルダとして定義します。

```
.agent/skills/<skill-name>/
└── SKILL.md          # スキルの定義（必須）
```

### Skills の配置場所

| レベル | パス | 適用範囲 |
|:---|:---|:---|
| **ワークスペース** | `<root>/.agent/skills/<name>/` | そのプロジェクトのみ |
| **グローバル** | `~/.gemini/antigravity/skills/<name>/` | すべてのプロジェクト |

### SKILL.md のフォーマット

ファイルの先頭に `---` で囲まれた設定ブロック（YAML frontmatterと呼びます）を書き、その下に Markdown で手順を書きます。

```markdown
---
name: my-skill
description: 特定のタスクを支援するスキル
---

# スキルの説明

## 実行手順
1. ステップ 1
2. ステップ 2
...
```

### Skills のベストプラクティス（公式推奨）

- 一つの責任に絞ります
- 名前と説明を明確にして、AI が使いどころを判断できるようにします
- 手順は具体的に書きましょう

---

## ハンズオン: オリジナル Skill を作ろう

### Step 1: ディレクトリ構造を確認

このフォルダにはサンプル Skill が入っています。

<!--
  [図9b: Skills のフォルダ構造]
  【スクリーンショット指示】
  Antigravity のファイルツリー（サイドバー）で、
  `.agent/skills/` 以下のフォルダ構造が表示されているキャプチャ。

  ファイルツリーの内容:
    .agent/
    └── skills/
        ├── code-review/
        │   └── SKILL.md    ← 長形ハイライトされている
        └── marp-presentation/
            └── SKILL.md

  追加要素:
    - SKILL.md ファイルにマウスオーバー時のツールチップが表示されている
      「コードレビュー用 Skill — SKILL.md」
    - 矢印と注釈（#4ecca3）で「SKILL.md が Skill の定義ファイル」と示す
  サイズ: 600×400px。縁取り付き。
-->

```
.agent/
└── skills/
    ├── code-review/
    │   └── SKILL.md      # コードレビュー用 Skill
    └── marp-presentation/
        └── SKILL.md      # Marp プレゼン作成 Skill
```

### Step 2: code-review Skill の中身を確認

`.agent/skills/code-review/SKILL.md` を開いて読んでみましょう。

```markdown
---
name: code-review
description: コードの品質レビューを行う
---

# コードレビュー Skill

## 概要
指定されたコードファイルに対して、品質レビューを実施します。

## 実行手順

1. **ファイル読み込み**: 対象ファイルを読み込む
2. **セキュリティチェック**: 
   - SQLインジェクション脆弱性
   - XSS脆弱性
   - ハードコードされた認証情報
3. **コード品質チェック**:
   - 変数名の適切さ
   - 関数の長さ（50行以下推奨）
   - コメントの有無
4. **改善提案**: 問題点と修正案をリスト形式で出力

## 出力フォーマット

### ✅ 良い点
- ...

### ⚠️ 要改善
- 問題: ...
- 修正案: ...

### 🔒 セキュリティ懸念
- ...
```

### Step 3: Skill を呼び出す

Antigravity のチャットで以下のように入力してください。

```
@code-review で sample.js をレビューして
```

または:

```
code-review Skill を使って、sample.js を確認して
```

---

## やってみよう: サンプルコードをレビュー

このフォルダの `sample.js` に対して Skill を実行してみましょう。

```
sample.js を code-review Skill でレビューして
```

確認すること:
- セキュリティ問題が指摘されるか
- 改善提案が具体的か
- 出力フォーマットが SKILL.md の定義通りか

<!--
  [図9c: code-review Skill の実行結果]
  【スクリーンショット指示】
  Agent Manager で code-review Skill を実行した結果画面のキャプチャ。

  左側（チャット）:
    - ユーザー入力: "sample.js を code-review Skill でレビューして"
    - AI 応答: 「@code-review Skill を使用して sample.js を確認します...」
      から始まり、下にレビュー結果（SKILL.md の出力フォーマット通り）が表示されている
        ✅ 良い点: ...
        ⚠️ 要改善: ...
        🔒 セキュリティ憸念: ...

  右側（Artifacts）:
    - レビュー結果をマークダウン形式でまとめた Walkthrough が表示されている

  矢印と注釈で「@skill名 で呼び出せる」ことを示す。
  サイズ: 1000×600px。縁取り付き。
-->

---

## 応用: 自分の Skill を作ってみよう

### 演習: generate-test Skill を作成

以下の手順で新しい Skill を作ってみましょう。

1. フォルダを作成します: `.agent/skills/generate-test/`
2. `SKILL.md` を作成します

```markdown
---
name: generate-test
description: 関数に対するユニットテストを自動生成する
---

# テスト自動生成 Skill

## 概要
指定された関数のユニットテストを自動生成します。

## 実行手順
1. 対象の関数を読み込む
2. 関数のインターフェース（引数・戻り値）を分析
3. 以下のテストケースを生成:
   - 正常系テスト（期待通りの入出力）
   - 異常系テスト（エラーケース）
   - 境界値テスト（最小値・最大値・空値）
4. テストフレームワークに適したコードを出力

## 出力フォーマット
- テストファイル名: `<元のファイル名>.test.js`
- テストフレームワーク: Jest（指定がなければ）
```

3. 呼び出してみましょう:
```
@generate-test で sample.js のテストを作って
```

### その他の Skill アイデア

| Skill 名 | 用途 |
|:---|:---|
| `translate-code` | コードのコメントを英語と日本語で相互翻訳 |
| `explain-code` | 初心者向けにコードを解説 |
| `optimize-performance` | パフォーマンス改善点を指摘 |
| `create-docs` | README やドキュメントを自動生成 |

---

## Skills / Rules / Workflows の比較

| 機能 | 目的 | 発動方法 |
|:---|:---|:---|
| **Rules** | エージェントの振る舞いを制御する | 自動、または `@ファイル名` |
| **Workflows** | 定型タスクを自動化する | `/ワークフロー名` |
| **Skills** | 専門的な能力を追加する | `@スキル名`、または AI が自動判断 |

---

**次へ進む → [06_vibe_coding_advanced](../06_vibe_coding_advanced/README.md)**
