---
title: "はじめに ― このブックの読み方"
---

## Google Antigravityとは

Google Antigravity は、2025年11月に Google が発表した AI エージェント統合開発環境（IDE）です。VS Code をベースにしつつ、AIエージェントが開発の中心にいる、という設計思想で作られています。

従来の AI コーディング支援ツール（GitHub Copilot や Cursor など）は、コードの補完や編集提案が主な役割でした。Antigravity はそこから一歩踏み込んで、AIがタスクの計画・実行・検証まで自律的に行います。開発者が自然言語で「何を作りたいか」を伝えれば、AI がコード生成、ブラウザ操作、画像生成、コードレビューなどを一貫して処理してくれます。

これを **Vibe Coding** と呼びます。

<!-- TODO: 図1 - Antigravityの概要図を挿入 -->

## このブックの対象読者

- Antigravity をこれから触ってみたい人
- AI を使った開発に興味があるエンジニア
- ハンズオン形式で手を動かしながら学びたい人

プログラミングの基本的な知識（HTML / CSS / JavaScript が読める程度）があれば、問題なく進められます。

## ブックの構成

全6ステップのハンズオン構成です。前半でできるだけ早く Vibe Coding を体験し、後半で拡張機能を学んでいく流れになっています。

| ステップ | 内容 | 所要時間 |
|:---:|:---|:---:|
| 1 | 環境セットアップ | 15分 |
| 2 | GEMINI.md 設定 | 15分 |
| 3 | Vibe Coding 基礎編 | 20分 |
| 4 | MCP 接続 | 20分 |
| 5 | Agent Skills 作成 | 20分 |
| 6 | Vibe Coding 発展編 | 30分 |

合計で約2時間です。

前半の 3ステップ（約50分）で基本的な操作と Vibe Coding の感覚をつかみ、後半の 3ステップ（約70分）で MCP や Skills による拡張を学びます。

## ハンズオン用リポジトリ

本書のハンズオン資料はGitHubリポジトリとして公開しています。手を動かしながら進める場合は、cloneしてお使いください。

```bash
git clone https://github.com/YOUR_USERNAME/antigravity_handson.git
cd antigravity_handson
```

Antigravity で `File > Open Folder` からこのフォルダを開けば、すぐにハンズオンを始められます。
