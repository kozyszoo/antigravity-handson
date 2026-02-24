# Scripts ディレクトリ

このディレクトリには、Antigravityハンズオン資料のスクリーンショット撮影スクリプトが含まれています。

## スクリプト一覧

### 1. screenshot_sample_page.py

**用途**: ブラウザで表示できるHTMLページのスクリーンショット自動撮影

**対象**:
- サンプル自己紹介ページ (`samples/profile_page_sample.html`)
- AI Coffee Shop LP (`samples/coffee_shop_lp_sample.html`)

**使い方**:
```bash
# Playwrightのインストール（初回のみ）
pip install playwright
python -m playwright install chromium

# スクリプトの実行
python screenshot_sample_page.py
```

**出力**:
- `images/sample_profile_page.png` - 図6: 完成した自己紹介ページ
- `images/sample_coffee_shop_lp.png` - 図10c: AI Coffee Shop LP完成画面

---

### 2. capture_antigravity_screenshots.sh

**用途**: Antigravityアプリケーション自体のスクリーンショット撮影ガイド

**対象**:
- Editor View / Agent Manager の画面
- MCP Store の画面
- Artifacts パネルの画面
- Skills フォルダ構造
- など、Antigravityアプリ内のUI

**使い方**:
```bash
# スクリプトに実行権限を付与（初回のみ）
chmod +x capture_antigravity_screenshots.sh

# インタラクティブモードで撮影
./capture_antigravity_screenshots.sh
```

**インタラクティブモード**:
1. Antigravityアプリを起動
2. スクリプトが撮影する画面を指示
3. 画面を準備して Enter キーを押す
4. screencaptureで範囲を選択して撮影
5. 自動的に images/ ディレクトリに保存

**手動撮影モード**:
- スクリプトで`n`を選択
- 各自で `Cmd+Shift+4` を使って撮影
- ファイル名を規定のものにリネーム
- `images/` ディレクトリに配置

---

## スクリーンショット撮影の全体フロー

### ステップ1: HTMLページのスクリーンショット（自動）

```bash
cd scripts
python screenshot_sample_page.py
```

### ステップ2: Antigravity画面のスクリーンショット（手動）

```bash
cd scripts

# 詳細な撮影手順を確認
open SCREENSHOT_GUIDE.md

# インタラクティブモードで撮影
./capture_antigravity_screenshots.sh
```

### ステップ3: 撮影状況の確認

```bash
# 撮影済みファイルの一覧
ls -lh ../images/*.png

# チェックリストの確認
open ../SCREENSHOT_STATUS.md
```

---

## 必要な環境

### Python環境
- Python 3.7以上
- Playwright（ブラウザ自動化）

```bash
pip install playwright
python -m playwright install chromium
```

### macOS環境
- macOS 10.14以上
- `screencapture`コマンド（標準搭載）

---

## トラブルシューティング

### Q: Playwrightのインストールに失敗する
```bash
# pipのアップグレード
python3 -m pip install --upgrade pip

# 再インストール
pip install playwright
python -m playwright install chromium
```

### Q: screencaptureで撮影できない
```bash
# macOSのスクリーンショット権限を確認
# システム環境設定 > セキュリティとプライバシー > プライバシー > 画面収録
```

### Q: Antigravityアプリが見つからない
```bash
# Antigravityが起動しているか確認
ps aux | grep -i antigravity

# または手動で起動
open -a Antigravity
```

---

## 参考資料

- `SCREENSHOT_GUIDE.md` - 各スクリーンショットの詳細な撮影手順
- `../SCREENSHOT_STATUS.md` - 撮影状況のチェックリスト
- `../zenn-book/figure-creation-prompts.md` - 全図の仕様書
