import urllib.request
import re

capsule_url = "https://capsule-render.vercel.app/api?type=waving&color=0:1b5e20,100:81c784&height=250&section=header"
typing_url = "https://readme-typing-svg.demolab.com?font=Great+Vibes&weight=400&size=85&duration=1&pause=100000&color=FFFFFF&center=true&vCenter=true&repeat=false&width=1000&height=250&lines=Piyush+Yenorkar"

req1 = urllib.request.Request(capsule_url, headers={'User-Agent': 'Mozilla/5.0'})
capsule_svg = urllib.request.urlopen(req1).read().decode('utf-8')

req2 = urllib.request.Request(typing_url, headers={'User-Agent': 'Mozilla/5.0'})
typing_svg = urllib.request.urlopen(req2).read().decode('utf-8')

# Extract all <style> blocks from typing_svg
styles = re.findall(r'<style>.*?</style>', typing_svg, re.DOTALL)
style_block = "\n".join(styles)

# Extract the inner SVG elements from typing_svg (excluding <svg> and </svg> tags)
inner_typing = re.sub(r'</?svg[^>]*>', '', typing_svg)

# Find the closing </svg> tag in capsule_svg and insert the typing elements before it
# Shift heading down by 30 pixels
combined_svg = capsule_svg.replace('</svg>', f'\n{style_block}\n<g transform="translate(0, 30)">\n{inner_typing}\n</g>\n</svg>')

with open('c:/Users/piyus/Downloads/piyushyenorkar-github/assets/header_combined.svg', 'w', encoding='utf-8') as f:
    f.write(combined_svg)
print("Combined SVG updated successfully!")
