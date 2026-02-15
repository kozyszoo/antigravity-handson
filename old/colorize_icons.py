#!/usr/bin/env python3
"""
Material Symbols SVGアイコンに色を付けるスクリプト
icons/ ディレクトリ内のSVGファイルを読み込み、色別フォルダに複製します
"""

import os
import shutil
from pathlib import Path

# カラーマッピング
COLORS = {
    'blue': '#6daad8',
    'pink': '#e08ac0',
    'green': '#6bb86a',
    'orange': '#e0a050',
    'lav': '#9b82b5',
    'black': '#3a3a5c',  # デフォルト
}

def colorize_svg(svg_path, color_hex):
    """SVGファイルの fill 属性を指定色に変更"""
    with open(svg_path, 'r') as f:
        content = f.read()
    
    # <svg> タグに fill 属性を追加
    if '<svg' in content:
        content = content.replace('<svg', f'<svg fill="{color_hex}"', 1)
    
    # <path> タグの fill="..." を置換（もしあれば）
    if 'fill=' in content:
        import re
        content = re.sub(r'fill="[^"]*"', f'fill="{color_hex}"', content)
    
    return content

def main():
    icons_dir = Path('icons')
    
    if not icons_dir.exists():
        print(f"❌ {icons_dir} ディレクトリが見つかりません")
        return
    
    # 色別ディレクトリを作成
    for color_name in COLORS.keys():
        color_dir = icons_dir / color_name
        color_dir.mkdir(exist_ok=True)
    
    # 各SVGファイルを色別に複製
    svg_files = list(icons_dir.glob('*.svg'))
    total_files = len(svg_files)
    
    print(f"🎨 {total_files} 個のアイコンを色別に生成中...\n")
    
    for svg_file in svg_files:
        icon_name = svg_file.name
        
        for color_name, color_hex in COLORS.items():
            # 色付きSVGを生成
            colored_svg = colorize_svg(svg_file, color_hex)
            
            # 色別フォルダに保存
            output_path = icons_dir / color_name / icon_name
            with open(output_path, 'w') as f:
                f.write(colored_svg)
    
    print(f"✅ 色別アイコン生成完了:")
    for color_name in COLORS.keys():
        count = len(list((icons_dir / color_name).glob('*.svg')))
        print(f"   icons/{color_name}/ → {count} files")
    
    print(f"\n使用例:")
    print(f'  <img src="icons/blue/rocket_launch.svg" width="50">')

if __name__ == '__main__':
    main()
