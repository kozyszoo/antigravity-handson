import re

with open('slides.md', 'r') as f:
    content = f.read()

slides = content.split('\n---\n')
for i, slide in enumerate(slides):
    if '<img src' in slide:
        imgs = re.findall(r"<img src='\./slides/(.*?)'.*?>", slide)
        if imgs:
            print(f"Slide {i}: Image(s) {imgs}")
    elif 'kozzy' in slide.lower():
        print(f"Slide {i}: Profile Text")
    else:
        # just print title
        title = re.search(r'#(.*)', slide)
        if title:
            print(f"Slide {i}: {title.group(1).strip()}")
        else:
            print(f"Slide {i}: No Title")
