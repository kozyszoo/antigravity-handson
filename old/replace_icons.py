#!/usr/bin/env python3
"""
Material Symbols spanタグを色付きSVG画像に置き換えるスクリプト
色クラス（c-blue等）に応じて適切な色フォルダの画像を参照
"""
import re

def replace_icons_with_colored_images(content):
    """
    Replace Material Symbols span tags with colored SVG image references.
    
    Pattern: <span class="ms [classes including c-COLOR]">icon_name</span>
    Replace with: <img src="icons/COLOR/icon_name.svg" width="XX" style="...">
    """
    
    # カラーマッピング
    color_map = {
        'c-blue': 'blue',
        'c-pink': 'pink',
        'c-green': 'green',
        'c-orange': 'orange',
        'c-lav': 'lav',
    }
    
    def get_size_from_class(class_str):
        """Determine icon size based on CSS class"""
        if 'ms-hero' in class_str:
            return '96'
        elif 'ms-xl' in class_str:
            return '64'
        elif 'ms-lg' in class_str:
            return '50'
        else:
            return '38'
    
    def get_color_from_class(class_str):
        """Determine color folder from CSS class"""
        for color_class, color_folder in color_map.items():
            if color_class in class_str:
                return color_folder
        return 'black'  # デフォルト色
    
    # Pattern to match: <span class="ms [...]">icon_name</span>
    pattern = r'<span class="(ms[^"]*?)">([^<]+)</span>'
    
    def replacer(match):
        css_class = match.group(1)
        icon_name = match.group(2)
        size = get_size_from_class(css_class)
        color = get_color_from_class(css_class)
        
        # Return HTML img tag with colored icon
        return f'<img src="icons/{color}/{icon_name}.svg" width="{size}" style="vertical-align: -0.2em; margin-right: 6px;">'
    
    return re.sub(pattern, replacer, content)

def main():
    input_file = 'presentation.md'
    output_file = 'presentation_colored_icons.md'
    
    print(f"📖 Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🎨 Replacing icon spans with colored images...")
    new_content = replace_icons_with_colored_images(content)
    
    print(f"💾 Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # Count replacements
    original_count = len(re.findall(r'<span class="ms[^"]*?">[^<]+</span>', content))
    
    print(f"\n✅ Conversion complete!")
    print(f"   Replaced {original_count} icon spans with colored image references")
    print(f"   Output file: {output_file}")
    print(f"\n次のステップ:")
    print(f"   1. mv {output_file} presentation.md")
    print(f"   2. marp presentation.md --pptx --allow-local-files -o presentation.pptx")

if __name__ == '__main__':
    main()
