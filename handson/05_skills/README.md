# 🛠️ Hands-on 05: Agent Skills の作成

## 目標
カスタム Skill を作成し、エージェントに新しい能力を追加する。

---

## 📖 Agent Skills とは？

**Skills** は、エージェントに**特定のタスクを実行する手順**をパッケージ化して教える機能です。
[agentskills.io](https://agentskills.io) オープン標準に基づいています。

> 📖 公式ドキュメント: https://antigravity.google/docs/skills

### Skills の構造

Skills は **`SKILL.md` ファイルを含むフォルダ** として定義されます。

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

**YAML frontmatter** + **Markdown** の形式で記述します：

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

- **単一の責任** に集中させる
- **明確な名前と説明** を付けて、AI が使い時を判断できるようにする
- **具体的な手順** を記述する

---

## ✅ ハンズオン: オリジナル Skill を作ろう

### Step 1: ディレクトリ構造を確認

このフォルダにはサンプル Skill が含まれています：

```
.agent/
└── skills/
    ├── code-review/
    │   └── SKILL.md      # コードレビュー用 Skill
    └── marp-presentation/
        └── SKILL.md      # Marpプレゼン作成 Skill
```

### Step 2: code-review Skill の中身を確認

`.agent/skills/code-review/SKILL.md` を開いて確認してみましょう：

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

Antigravity のチャットで：

```
@code-review で sample.js をレビューして
```

または：

```
code-review Skill を使って、sample.js を確認して
```

---

## 🎯 やってみよう: サンプルコードをレビュー

このフォルダの `sample.js` に対して Skill を実行してみましょう。

```
sample.js を code-review Skill でレビューして
```

**確認ポイント**:
- [ ] セキュリティ問題が指摘されるか
- [ ] 改善提案が具体的か
- [ ] 出力フォーマットが SKILL.md の定義通りか

---

## 🎨 応用: 自分の Skill を作ってみよう

### 演習: generate-test Skill を作成

以下の手順で新しい Skill を作ってみましょう：

1. フォルダを作成: `.agent/skills/generate-test/`
2. `SKILL.md` を作成

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

3. 呼び出してみる:
```
@generate-test で sample.js のテストを作って
```

### その他の Skill アイデア

| Skill 名 | 用途 |
|:---|:---|
| `translate-code` | コードのコメントを英語/日本語に翻訳 |
| `explain-code` | 初心者向けにコードを解説 |
| `optimize-performance` | パフォーマンス改善点を指摘 |
| `create-docs` | README やドキュメントを自動生成 |

---

## 📌 Skills vs Rules vs Workflows 比較

| 機能 | 目的 | 発動方法 |
|:---|:---|:---|
| **Rules** | エージェントの振る舞いを制御 | 自動 or `@ファイル名` |
| **Workflows** | 定型タスクの自動化 | `/ワークフロー名` |
| **Skills** | 専門的な能力の追加 | `@スキル名` or AI が自動判断 |

---

**次へ進む → [06_vibe_coding_advanced](../06_vibe_coding_advanced/README.md)**
