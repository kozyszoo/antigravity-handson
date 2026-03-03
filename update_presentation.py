import re

with open('presentation.md', 'r') as f:
    orig = f.read()

# We will just append the image slides at the very end of the presentation.md if we can't decide, BUT we'll try to insert them into sections.
# Even better, let's insert the profile slide after "本日のアジェンダ"
profile_slide = """
---

<!-- _class: bg-dark -->

# <span class="ms ms-lg c-lav" style="display:inline-flex; align-items:center; justify-content:center;">👤</span> 自己紹介

<div class="cols">
<div>
<div class="card card-lav">
<strong>山岡 滉治（kozzy）</strong><br>
<small>@kozzy0919</small>
</div>
<div class="card card-blue" style="margin-top: 10px;">
<strong>🏢 データ・AI企画推進 / Developer Relations</strong><br>
<small>インフラ/サーバーエンジニアを経て、現在は生成AI活用の企画・推進を担当。</small>
</div>
</div>
<div>
<div class="card card-green">
<strong>🌟 主要な実績</strong>
<ul>
<li>GitHub Copilot導入で全社利用率60%達成</li>
<li>社内生成AIコミュニティを2,000名規模に成長</li>
</ul>
</div>
<div class="card card-orange" style="margin-top: 10px;">
<strong>📝 その他の活動</strong>
<ul>
<li>『開発系エンジニアのためのGit/GitHub絵とき入門』(2025/3)</li>
<li>プログラミングスクール講師</li>
</ul>
</div>
</div>
</div>
"""

orig = orig.replace('---\n\n<!-- _class: bg-pink -->\n\n# <span class="ms', profile_slide + '\n---\n\n<!-- _class: bg-pink -->\n\n# <span class="ms')

# Extract images from slides.md
with open('slides.md', 'r') as f:
    slides_md = f.read()

img_matches = re.findall(r"<img src='\./(slides/.*?.png)'.*?>", slides_md)

# We will add all image slides to an appendix for now, OR we can append them.
# The user wants "presentation.md に slide.md の内容を導入して".
# What if the user really meant to just take ALL slides from slides.md, convert them to Marp, and replace the content?
# Let's write the image slides to a string
img_slides = ""
for img in img_matches:
    img_slides += f"""
---

<div style="display: flex; justify-content: center; align-items: center; width: 100%; height: 100%;">
  <img src="./{img}" style="max-height: 85%; max-width: 85%; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 8px;" />
</div>
"""

with open('presentation.md', 'w') as f:
    f.write(orig + "\n\n<!-- _class: lead -->\n\n# Appendix: スライド画像\n" + img_slides)

