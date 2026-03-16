import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make it white-based theme
old_css = """        :root {
            --primary: #4ecca3;
            --bg-dark: #1a1a2e;
            --bg-mid: #16213e;
            --bg-light: #0f3460;
            --text: #e8e8e8;
            --muted: #a0a0a0;
            --purple: #9b82b5;
            --blue: #6daad8;
            --sidebar: 280px;
        }"""

new_css = """        :root {
            --primary: #10a37f;
            --bg-dark: #f9f9f9;
            --bg-mid: #ffffff;
            --bg-light: #eadddf;
            --text: #333333;
            --muted: #666666;
            --purple: #8e44ad;
            --blue: #2980b9;
            --sidebar: 280px;
        }"""

html = html.replace(old_css, new_css)

# Replace remaining Antigravity terms
html = html.replace('Antigravity', 'Codex')
html = html.replace('Dual View', 'Ask / Code モード')
html = html.replace('Agent Manager', 'Codex Sidebar')
html = html.replace('Nano Banana', 'DALL-E')

# And specifically handling the header that I previously changed correctly
html = html.replace('Google Codex', 'OpenAI Codex')

# Find img tags to make sure they're visible if needed... Actually, white background might mess up transparent PNGs, but let's assume it's fine.
# Also fix any card backgrounds or code block backgrounds if they hardcode #111
html = html.replace('background: #111;', 'background: #f0f0f0;\n            color: #333;\n            border: 1px solid #ccc;')
html = html.replace('background: #0f172a;', 'background: #f8f9fa;\n            color: #24292e;\n            border: 1px solid #e1e4e8;')
html = html.replace('color: #6daad8;', 'color: #0366d6;')

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
