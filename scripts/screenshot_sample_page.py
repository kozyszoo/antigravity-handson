#!/usr/bin/env python3
"""
サンプルHTMLページのスクリーンショットを撮影するスクリプト
Playwrightを使用してブラウザで表示し、スクリーンショットを保存する
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

# プロジェクトのルートディレクトリ
PROJECT_ROOT = Path(__file__).parent.parent
IMAGES_DIR = PROJECT_ROOT / "images"
SAMPLES_DIR = PROJECT_ROOT / "samples"

# 撮影するHTMLファイルと出力画像の設定
SCREENSHOTS = [
    {
        "html_file": SAMPLES_DIR / "profile_page_sample.html",
        "output": IMAGES_DIR / "sample_profile_page.png",
        "viewport": {"width": 1280, "height": 800},
        "description": "図6: 完成した自己紹介ページのサンプル"
    },
    {
        "html_file": SAMPLES_DIR / "coffee_shop_lp_sample.html",
        "output": IMAGES_DIR / "sample_coffee_shop_lp.png",
        "viewport": {"width": 1280, "height": 1000},
        "description": "図10c: AI Coffee Shop LP のサンプル"
    }
]


async def take_screenshot(page, html_file: Path, output: Path, viewport: dict):
    """HTMLファイルを開いてスクリーンショットを撮影"""
    # HTMLファイルを開く
    await page.goto(f"file://{html_file.absolute()}")

    # ページが完全に読み込まれるまで待つ
    await page.wait_for_load_state("networkidle")

    # スクリーンショットを撮影
    await page.screenshot(path=str(output), full_page=False)
    print(f"✓ Saved: {output.name}")


async def main():
    """メイン処理"""
    # imagesディレクトリを作成
    IMAGES_DIR.mkdir(exist_ok=True)

    print("Starting screenshot capture...\n")

    async with async_playwright() as p:
        # ブラウザを起動
        browser = await p.chromium.launch(headless=True)

        for config in SCREENSHOTS:
            html_file = config["html_file"]
            output = config["output"]
            viewport = config["viewport"]
            description = config["description"]

            # HTMLファイルが存在しない場合はスキップ
            if not html_file.exists():
                print(f"⚠ Skipped: {html_file.name} (file not found)")
                continue

            print(f"📸 {description}")
            print(f"   HTML: {html_file.name}")

            # ページを開く
            page = await browser.new_page(viewport=viewport)

            try:
                await take_screenshot(page, html_file, output, viewport)
            except Exception as e:
                print(f"✗ Error: {e}")
            finally:
                await page.close()

            print()

        await browser.close()

    print("Screenshot capture completed!")


if __name__ == "__main__":
    asyncio.run(main())
