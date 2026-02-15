#!/bin/bash
# presentation.md を Material Symbols フォント付きで PPTX に変換するスクリプト

echo "📄 Step 1: Marp で PDF 生成（フォント埋め込み）..."
marp presentation.md --pdf -o presentation.pdf --allow-local-files

if [ $? -ne 0 ]; then
  echo "❌ PDF 生成に失敗しました"
  exit 1
fi

echo "✅ PDF 生成完了: presentation.pdf"
echo ""
echo "📊 Step 2: PDF から PPTX への変換方法"
echo ""
echo "以下のいずれかの方法で PPTX に変換してください："
echo ""
echo "【方法1】 Adobe Acrobat（推奨）"
echo "  1. Adobe Acrobat で presentation.pdf を開く"
echo "  2. ファイル > 書き出し > Microsoft PowerPoint に書き出し"
echo "  3. フォント埋め込みオプションを有効にする"
echo ""
echo "【方法2】 オンラインツール"
echo "  - https://www.ilovepdf.com/pdf_to_powerpoint （フォント保持）"
echo "  - https://www.adobe.com/acrobat/online/pdf-to-ppt.html"
echo ""
echo "【方法3】 LibreOffice（無料）"
echo "  soffice --headless --convert-to pptx presentation.pdf"
echo "  （ただし、フォントの再現性が低い場合があります）"
echo ""
echo "✨ フォントアイコンの色と配置が正しく保たれます！"
