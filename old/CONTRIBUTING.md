# 貢献ガイドライン

Google Antigravity ハンズオンへの貢献に興味を持っていただき、ありがとうございます！

このドキュメントでは、プロジェクトへの貢献方法について説明します。

## 📋 目次

- [行動規範](#行動規範)
- [貢献の種類](#貢献の種類)
- [開発環境のセットアップ](#開発環境のセットアップ)
- [プルリクエストの流れ](#プルリクエストの流れ)
- [コーディング規約](#コーディング規約)
- [コミットメッセージ](#コミットメッセージ)
- [質問・サポート](#質問サポート)

## 🤝 行動規範

このプロジェクトは、すべての参加者に対して敬意を持って接することを期待しています。

### 期待される行動

- ✅ 他者を尊重する
- ✅ 建設的なフィードバックを提供する
- ✅ 異なる視点や経験を受け入れる
- ✅ コミュニティの利益を優先する

### 許容されない行動

- ❌ ハラスメントや差別的な言動
- ❌ 攻撃的または侮辱的なコメント
- ❌ 個人情報の無断公開
- ❌ その他、プロフェッショナルでない行為

## 🎯 貢献の種類

以下のような貢献を歓迎します:

### 1. バグ報告

バグを見つけた場合は、[Issue](https://github.com/YOUR_USERNAME/antigravity_handson/issues)を作成してください。

**含めるべき情報**:
- バグの詳細な説明
- 再現手順
- 期待される動作
- 実際の動作
- 環境情報（OS、Antigravityバージョンなど）
- スクリーンショット（該当する場合）

### 2. 機能要望

新しい機能のアイデアがある場合も、Issueを作成してください。

**含めるべき情報**:
- 機能の詳細な説明
- ユースケース
- 期待される効果
- 実装案（あれば）

### 3. ドキュメントの改善

- タイポの修正
- 説明の明確化
- 新しいセクションの追加
- 翻訳の改善

### 4. コードの改善

- バグ修正
- 新機能の実装
- パフォーマンス改善
- リファクタリング

### 5. ハンズオン資料の追加

- 新しいハンズオンの作成
- 既存ハンズオンの改善
- サンプルコードの追加

## 🛠️ 開発環境のセットアップ

### 1. リポジトリのフォーク

GitHubでこのリポジトリをフォークします。

### 2. クローン

```bash
git clone https://github.com/YOUR_USERNAME/antigravity_handson.git
cd antigravity_handson
```

### 3. リモートの設定

```bash
# オリジナルのリポジトリをupstreamとして追加
git remote add upstream https://github.com/ORIGINAL_OWNER/antigravity_handson.git

# 確認
git remote -v
```

### 4. 必要なツールのインストール

```bash
# Marp CLI（プレゼンテーション資料の編集に必要）
npm install -g @marp-team/marp-cli

# その他、必要に応じて
```

## 🔄 プルリクエストの流れ

### 1. ブランチの作成

```bash
# 最新のmainブランチを取得
git checkout main
git pull upstream main

# 新しいブランチを作成
git checkout -b feature/your-feature-name
# または
git checkout -b fix/your-bug-fix
```

**ブランチ命名規則**:
- `feature/` - 新機能
- `fix/` - バグ修正
- `docs/` - ドキュメント
- `refactor/` - リファクタリング
- `test/` - テスト追加

### 2. 変更の実装

- コードを書く
- テストを追加（該当する場合）
- ドキュメントを更新

### 3. コミット

```bash
git add .
git commit -m "feat: 新機能の説明"
```

### 4. プッシュ

```bash
git push origin feature/your-feature-name
```

### 5. プルリクエストの作成

1. GitHubでフォークしたリポジトリにアクセス
2. "Compare & pull request"をクリック
3. 変更内容を説明
4. プルリクエストを作成

### プルリクエストのテンプレート

```markdown
## 変更内容

<!-- 何を変更したか、なぜ変更したかを説明 -->

## 関連Issue

<!-- 関連するIssue番号があれば記載 -->
Closes #123

## チェックリスト

- [ ] コードが正しく動作することを確認
- [ ] 適切なコメントを追加
- [ ] ドキュメントを更新
- [ ] テストを追加（該当する場合）
- [ ] コーディング規約に従っている

## スクリーンショット

<!-- 該当する場合、スクリーンショットを追加 -->
```

## 📝 コーディング規約

### 全般

- **言語**: すべてのドキュメントは日本語で記述
- **エンコーディング**: UTF-8
- **改行コード**: LF（Unix形式）
- **インデント**: スペース2つ

### Markdown

- **見出し**: `#` の後にスペースを入れる
- **リスト**: `-` を使用（`*` は使わない）
- **コードブロック**: 言語を指定する

```markdown
# 良い例
```bash
npm install
\```

# 悪い例
\```
npm install
\```
```

### JavaScript/TypeScript

```javascript
// 変数名: camelCase
const myVariable = 'value';

// 関数名: camelCase
function myFunction() {
  // ...
}

// クラス名: PascalCase
class MyClass {
  // ...
}

// 定数: UPPER_SNAKE_CASE
const MAX_COUNT = 100;
```

### ファイル名

- **Markdown**: `kebab-case.md`
- **JavaScript**: `kebab-case.js`
- **TypeScript**: `kebab-case.ts`
- **README**: `README.md`（大文字）

### コメント

```javascript
// 日本語でのコメントを推奨
// 複雑なロジックには必ず説明を追加

/**
 * 関数の説明
 * @param {string} name - パラメータの説明
 * @returns {string} 戻り値の説明
 */
function greet(name) {
  return `こんにちは、${name}さん！`;
}
```

## 💬 コミットメッセージ

[Conventional Commits](https://www.conventionalcommits.org/)に従います。

### 形式

```
<type>: <subject>

<body>

<footer>
```

### Type

- `feat`: 新機能
- `fix`: バグ修正
- `docs`: ドキュメントのみの変更
- `style`: コードの意味に影響しない変更（空白、フォーマットなど）
- `refactor`: バグ修正や機能追加ではないコード変更
- `test`: テストの追加や修正
- `chore`: ビルドプロセスやツールの変更

### 例

```bash
# 新機能
git commit -m "feat: Nano Bananaの使い方セクションを追加"

# バグ修正
git commit -m "fix: プレゼンテーション資料のタイポを修正"

# ドキュメント
git commit -m "docs: READMEのセットアップ手順を更新"

# リファクタリング
git commit -m "refactor: コードレビューの手順を整理"
```

## ❓ 質問・サポート

### 質問がある場合

1. **README.mdを確認**: まず、ドキュメントを確認
2. **既存のIssueを検索**: 同じ質問がないか確認
3. **新しいIssueを作成**: 見つからなければ質問を投稿

### サポートチャンネル

- **GitHub Issues**: バグ報告、機能要望
- **GitHub Discussions**: 一般的な質問、ディスカッション
- **Discord**: リアルタイムサポート

## 🎉 貢献者

このプロジェクトへの貢献者に感謝します！

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## 📄 ライセンス

貢献することで、あなたの貢献がMITライセンスの下でライセンスされることに同意したものとみなされます。

---

**ありがとうございます！あなたの貢献がこのプロジェクトをより良くします！** 🚀
