---
title: "Step 6: 活用 Tips 集"
---

## 概要

Codex CLI をさらに使いこなすための参考記事・公式リソースをまとめました。ハンズオン後の自習や、チームへの共有にご活用ください。

---

## 📰 活用 Tips

コミュニティや公式ブログから集めた実践的な Tips を紹介します。

### 基本操作編

| Tips | 概要 | 出典 |
|:---|:---|:---|
| **画面は「3分割」で理解する** | 左：Workspace（ファイル置き場）、中：Editor（作業机）、右：AI Chat（頭脳）の3エリア構成。「右のAIに指示して、左の素材を使い、中央で作業させる」と覚えるとシンプル。チャット履歴は右上の「＋」で新規、「時計マーク」で過去ログを参照できる。 | [note.com/kino_11](https://note.com/kino_11/n/n4a7712b47868) |
| **モードは基本「Planning」一択** | Planning Mode ではAIがまず計画を立て、宣言してから作業する。Fast Mode は計画なしで即作業するためミスりやすい。複雑なタスクは急がば回れで Planning を選ぶほうが精度が上がる。モデルは `codex-1` が安定。 | [note.com/kino_11](https://note.com/kino_11/n/n4a7712b47868) |
| **Global Rules に「日本語指示」を書く** | 設定しないとAIが英語で返答することがある。Global Rules に `回答、計画、思考プロセスを全て日本語で行うこと。` の一行を書くだけで日本語対応になる。これが最初にやるべき「憲法」設定。 | [note.com/kino_11](https://note.com/kino_11/n/n4a7712b47868) |
| **Mentions でファイルを「食わせる」** | チャット欄にファイルをドラッグ＆ドロップするか `@ファイル名` で参照することで、AIに正確なコンテキストを与えられる。指示の精度が大きく向上する。 | [note.com/kino_11](https://note.com/kino_11/n/n4a7712b47868) |
| **Auto Execution の使い分け** | 設計を壁打ちしたいときは `Request Review`（AIが毎回確認を求める）、単純作業を任せるときは `Always Proceed`（確認なしで爆速）に切り替える。慣れるまでは Request Review が安全。 | [note.com/kino_11](https://note.com/kino_11/n/n4a7712b47868) |

### 中級テクニック編

| Tips | 概要 | 出典 |
|:---|:---|:---|
| **Artifacts でAIの作業を「見える化」** | タスク実行時に `task.md`（進行状況）・`implementation_plan.md`（実装計画）・`walkthrough.md`（作業ログ）が自動生成される。コードを書く前に計画書が出るため「仕様レビュー」感覚で開発できる。 | [zenn.dev/minedia](https://zenn.dev/minedia/articles/cc718542d8cc73) |
| **Chrome拡張でクロスツール自律操作** | Codex 専用の Chrome 拡張を入れると、AIがブラウザを実際に見て操作できるようになる。ターミナル実行→ブラウザ動作確認まで全自動。UIの実装精度が段違いに向上する。 | [zenn.dev/minedia](https://zenn.dev/minedia/articles/cc718542d8cc73) |
| **スクショに直接コメントで指示する** | 生成されたUIのスクリーンショットや画像に対して、ドラッグ＆ドロップで範囲選択してコメントを入れるだけで修正指示が出せる。「右上のボタンを…」とテキストで説明するストレスから解放される。 | [zenn.dev/minedia](https://zenn.dev/minedia/articles/cc718542d8cc73) |
| **DALL-E Pro で画像を即生成** | UIモックアップ・アーキテクチャ図・Webサイト用の画像アセットなどをAIが生成して直接プロジェクトに配置してくれる。デザイナーを待たずとも高品質な素材が数秒で手に入る。 | [zenn.dev/minedia](https://zenn.dev/minedia/articles/cc718542d8cc73) |

### 上級テクニック編

| Tips | 概要 | 出典 |
|:---|:---|:---|
| **Artifact Review で実行前にモデル切り替え** | Artifact Review Policy を「Request Review」に設定すると、AIが実装計画を提示した段階でレビューできる。ここで**実行前にモデルを切り替えられる**のが最大のメリット。設計フェーズは codex-1、実装フェーズは Low に切り替えると、素早いトライアンドエラーが可能になる。 | [DevelopersIO / G-gen Blog](https://dev.classmethod.jp/articles/google-antigravity-five-tips/) |
| **DevContainer で安全に実行** | OpenAI Codex は DevContainer 対応が組み込み。ホストOSを保護するため、独立した環境内で実行することでリスク軽減できる。`.gitconfig` などの設定ファイルはホストからマウントして引き継ぐ。 | [DevelopersIO / G-gen Blog](https://dev.classmethod.jp/articles/google-antigravity-five-tips/) |
| **Step10 超過時に一時停止させる** | `~/.codex/rules.md` に「Step10超過時に処理を一時停止して、完了内容・状況報告・次アクションを報告すること」と書くことで、根本原因分析を促進し、無限ループを防げる。日本語対応設定も同じファイルに記述できる。 | [DevelopersIO / G-gen Blog](https://dev.classmethod.jp/articles/google-antigravity-five-tips/) |
| **Agent Manager で並列実行** | `Cmd + E` で Agent Manager を開くと、複数エージェントを同時管理できる。**Asynchronous Agents 機能**で複数タスクを並行実行すると、フロントエンド実装とバックエンド構築を同時進行させられる。 | [DevelopersIO / G-gen Blog](https://dev.classmethod.jp/articles/google-antigravity-five-tips/) |
| **無料枠のレート制限に注意** | プレビュー版では無料枠のレート制限が厳しく、数時間で上限に達する可能性がある。制限に達したら**別モデルへ切り替え**（GPT-4.1 は無料で利用可能）、またはエラー発生時は「続きを実装して」と依頼すると再開される。 | [DevelopersIO / G-gen Blog](https://dev.classmethod.jp/articles/google-antigravity-five-tips/) |
| **Review-driven development を活用** | ターミナル実行ポリシーを「Request Review」、変更の適用は「Agent Decides」に設定すると、コマンド実行時に確認を挟みつつ、AIが状況に応じて自動判断できる。要所で人間の確認を挟みながら作業を進められる。 | [DevelopersIO / G-gen Blog](https://dev.classmethod.jp/articles/google-antigravity-five-tips/) |
| **Browser Agent でデバッグ自動化** | Browser Agent 拡張機能をインストールすると、エージェントに「ブラウザで確認するよう指示」するだけで、エラー画面を自動確認・デバッグ情報を収集できる。ターミナル実行→ブラウザ動作確認まで全自動になる。 | [DevelopersIO / G-gen Blog](https://dev.classmethod.jp/articles/google-antigravity-five-tips/) |
| **Planning Mode は9割のケースで使う** | Planning Mode は計画立案→実装の流れで進むため、エラーが出やすいクラウドインフラ構築・複雑な機能実装に最適。Fast Mode は単発の質問やテキスト修正向けで、継続的なタスク実行には不向き。迷ったら Planning を選ぶべし。 | [DevelopersIO / G-gen Blog](https://dev.classmethod.jp/articles/google-antigravity-five-tips/) |

---

## 🔗 公式ドキュメント・リソース

### 公式サイト・ドキュメント

| カテゴリ | 概要 | URL |
|:---|:---|:---|
| **公式サイト** | Codex CLI のダウンロード・プラン・最新情報 | [openai.com](https://openai.com) |
| **公式ドキュメント** | セットアップ・Rules・MCP・Skills・Workflows の詳細リファレンス | [platform.openai.com/docs](https://platform.openai.com/docs) |
| **Rules & Workflows** | GEMINI.md の書き方・Activation Mode・Workflows の設定方法 | [github.com/openai/codex](https://github.com/openai/codex) |
| **MCP（Model Context Protocol）** | 外部ツール連携（ブラウザ・DB・GitHub 等）の接続手順 | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| **Agent Skills** | スキルの作成・配置・呼び出し方法のリファレンス | [github.com/openai/codex](https://github.com/openai/codex) |

### コミュニティ記事

実践的な活用方法や Tips を紹介している記事をまとめました。

- [note.com/kino_11 - Codex CLI 基本操作ガイド](https://note.com/kino_11/n/n4a7712b47868)
- [zenn.dev/minedia - Codex CLI 実践活用法](https://zenn.dev/minedia/articles/cc718542d8cc73)
- [DevelopersIO - OpenAI Codex 5つのTips](https://dev.classmethod.jp/articles/google-antigravity-five-tips/)

---

## 📚 参考リンク

### 学習リソース

- **公式チュートリアル**: [openai.com/tutorials](https://openai.com/tutorials)
- **公式ブログ**: [openai.com/news/](https://openai.com/news/)
- **YouTube公式チャンネル**: [youtube.com/@OpenAI](https://youtube.com/@OpenAI)

### コミュニティ

- **Discord**: Codex Developers Community
- **GitHub Discussions**: 質問・議論フォーラム
- **X (Twitter)**: #Codex ハッシュタグで最新情報をチェック

---

## ✅ まとめ

このチャプターでは、Codex CLI をより効果的に活用するための実践的な Tips と公式リソースを紹介しました。

**次のステップ**:
- 気になる Tips を実際に試してみる
- 公式ドキュメントで詳細を確認する
- コミュニティ記事で実例を学ぶ
- 自分なりの活用方法を見つける

ハンズオンで学んだ基礎に、これらの Tips を組み合わせることで、より高度な AI 駆動開発が可能になります。
