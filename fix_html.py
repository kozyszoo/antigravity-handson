import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make it white-based theme
html = html.replace('''        :root {
            --bg: #1e1e1e;
            --bg-sidebar: #252526;
            --bg-card: #2d2d2d;
            --bg-code: #1e1e1e;
            --text: #d4d4d4;
            --text-muted: #9cdcfe;
            --primary: #569cd6;
            --secondary: #4ec9b0;
            --border: #404040;
            --warning: #ce9178;
        }''', '''        :root {
            --bg: #ffffff;
            --bg-sidebar: #f7f7f8;
            --bg-card: #ffffff;
            --bg-code: #f6f8fa;
            --text: #333333;
            --text-muted: #666666;
            --primary: #10a37f;
            --secondary: #0077ff;
            --border: #e5e5e5;
            --warning: #ff9900;
        }''')

# Replace Antigravity to OpenAI Codex
html = html.replace('Google Antigravity', 'OpenAI Codex')
html = html.replace('Antigravity', 'Codex')

# Also replace some other parts
html = html.replace('Dual View', 'Ask / Code モード')
html = html.replace('Agent Manager', 'Codex Sidebar')
html = html.replace('Nano Banana', 'DALL-E') # Since nano banana was swapped out

with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
