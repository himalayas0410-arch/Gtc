import os
import re

patterns = [
    # Desktop version (matches multi-line or single line)
    re.compile(r'<a href="images/delegates\.pdf" target="_blank">ICAI Delegation visit to Gift\s+City - IFSCA</a>', re.DOTALL),
    # Mobile version (matches multi-line or single line)
    re.compile(r'<li>\s*<a href="images/delegates\.pdf" target="_blank" onclick="toggleMobileMenu\(\)">ICAI Delegation\s+visit to Gift City - IFSCA</a>\s*</li>', re.DOTALL),
    # Another variant seen in grep
    re.compile(r'<a href="images/delegates\.pdf" target="_blank">ICAI Delegation visit to Gift City - IFSCA</a>', re.DOTALL),
    # Quick links variant (Premium Dashboard Style)
    re.compile(r'<div class="col-lg-4 col-md-6">\s*<a href="images/delegates\.pdf" target="_blank" class="ql-bar-item ql-blue">.*?</a>\s*</div>', re.DOTALL),
    # Another variant of the same
    re.compile(r'<a href="images/delegates\.pdf" target="_blank" class="ql-bar-item ql-blue">.*?</a>', re.DOTALL)
]

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(filename, 'r', encoding='latin-1') as f:
                    content = f.read()
            except:
                print(f"Skipping {filename} due to encoding error")
                continue
        
        new_content = content
        for p in patterns:
            new_content = p.sub('', new_content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")

