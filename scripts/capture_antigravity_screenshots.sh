#!/bin/bash
# Antigravityアプリケーションのスクリーンショット撮影スクリプト
# macOSのscreencaptureコマンドを使用

set -e

IMAGES_DIR="../images"
mkdir -p "$IMAGES_DIR"

echo "======================================"
echo "Antigravity スクリーンショット撮影"
echo "======================================"
echo ""
echo "このスクリプトは、Antigravityアプリケーションの"
echo "スクリーンショットを撮影するためのガイドです。"
echo ""
echo "【重要】撮影前の準備:"
echo "1. Antigravityアプリケーションを起動してください"
echo "2. 撮影したい画面を表示してください"
echo "3. 画面サイズを適切に調整してください"
echo ""

# 撮影する画面のリスト
declare -A SCREENSHOTS=(
    ["antigravity_dual_view.png"]="図2: Editor View と Agent Manager の画面比較 (1200x600px)"
    ["editor_ai_features.png"]="図3: エディタのAI機能（Supercomplete と Command）(800x500px)"
    ["global_rules_settings.png"]="図4b: Global Rules 設定画面 (800x500px)"
    ["nano_banana_flow.png"]="図5: Nano Banana 画像生成フロー (900x350px)"
    ["vibe_coding_dialog.png"]="図5b: Vibe Coding の対話の様子 (1000x550px)"
    ["artifacts_panel.png"]="図6b: Artifacts パネルの活用 (600x700px)"
    ["artifacts_inline_comment.png"]="図6c: Artifacts へのインラインコメント機能 (700x450px)"
    ["mcp_store_screen.png"]="図8: MCP Store の画面キャプチャ (800x500px)"
    ["mcp_execution_result.png"]="図8b: MCP 演習の実行結果 (1000x550px)"
    ["skills_folder_tree.png"]="図9b: Skills のフォルダ構造 (600x400px)"
    ["code_review_result.png"]="図9c: code-review Skill の実行結果 (1000x600px)"
    ["mcp_browser_research.png"]="図10b: MCP Browser の Web リサーチ実行画面 (1100x600px)"
)

echo "撮影が必要なスクリーンショット一覧:"
echo "--------------------------------------"
for filename in "${!SCREENSHOTS[@]}"; do
    description="${SCREENSHOTS[$filename]}"
    if [ -f "$IMAGES_DIR/$filename" ]; then
        echo "✓ [既存] $filename"
        echo "         $description"
    else
        echo "☐ [未撮影] $filename"
        echo "           $description"
    fi
    echo ""
done

echo "======================================"
echo "撮影方法の選択"
echo "======================================"
echo ""
echo "方法1: インタラクティブモード（推奨）"
echo "  - このスクリプトのガイドに従って1枚ずつ撮影"
echo "  - 各画面の準備ができたら撮影を実行"
echo ""
echo "方法2: 手動撮影"
echo "  - macOSの標準機能（Cmd+Shift+4）で撮影"
echo "  - ファイル名を上記リストに合わせてリネーム"
echo "  - images/ディレクトリに配置"
echo ""

read -p "インタラクティブモードで撮影しますか？ (y/n): " choice

if [[ "$choice" != "y" && "$choice" != "Y" ]]; then
    echo ""
    echo "手動撮影を選択しました。"
    echo "上記のファイル名と説明を参考に、スクリーンショットを撮影してください。"
    echo ""
    echo "撮影のヒント:"
    echo "  - Cmd+Shift+4: 範囲選択して撮影"
    echo "  - Cmd+Shift+4 → Space: ウィンドウ全体を撮影"
    echo "  - 撮影後、デスクトップの画像をimages/ディレクトリに移動"
    echo ""
    exit 0
fi

echo ""
echo "======================================"
echo "インタラクティブモード開始"
echo "======================================"
echo ""

# 各スクリーンショットを順番に撮影
for filename in "${!SCREENSHOTS[@]}"; do
    description="${SCREENSHOTS[$filename]}"
    output_path="$IMAGES_DIR/$filename"

    # 既に存在する場合はスキップ
    if [ -f "$output_path" ]; then
        echo "✓ スキップ: $filename (既に存在します)"
        echo ""
        continue
    fi

    echo "--------------------------------------"
    echo "撮影: $filename"
    echo "説明: $description"
    echo "--------------------------------------"
    echo ""
    echo "【準備】"
    echo "1. Antigravityで該当する画面を表示してください"
    echo "2. ウィンドウサイズを適切に調整してください"
    echo "3. 不要な要素を非表示にしてください"
    echo ""
    echo "準備ができたら Enter キーを押してください..."
    read

    echo ""
    echo "5秒後にスクリーンショットを撮影します..."
    echo "撮影範囲を選択してください（カーソルがクロスヘアに変わります）"
    sleep 2
    echo "3..."
    sleep 1
    echo "2..."
    sleep 1
    echo "1..."
    sleep 1

    # screencaptureコマンドで撮影（インタラクティブモード）
    screencapture -i "$output_path"

    if [ -f "$output_path" ]; then
        echo "✓ 撮影完了: $output_path"

        # ファイルサイズを表示
        file_size=$(du -h "$output_path" | cut -f1)
        echo "  ファイルサイズ: $file_size"
    else
        echo "✗ 撮影がキャンセルされました"
    fi
    echo ""

    # 次の撮影に進むか確認
    if [ "${#SCREENSHOTS[@]}" -gt 1 ]; then
        read -p "次のスクリーンショットに進みますか？ (y/n/q=終了): " next
        if [[ "$next" == "q" || "$next" == "Q" ]]; then
            echo "撮影を終了します。"
            break
        fi
        echo ""
    fi
done

echo ""
echo "======================================"
echo "撮影完了"
echo "======================================"
echo ""
echo "撮影されたファイル一覧:"
ls -lh "$IMAGES_DIR"/*.png 2>/dev/null | tail -20 || echo "（ファイルが見つかりません）"
echo ""
echo "次のステップ:"
echo "1. 撮影した画像を確認してください"
echo "2. 必要に応じて画像編集ツールで注釈を追加してください"
echo "3. SCREENSHOT_STATUS.md でチェックリストを更新してください"
echo ""
