import os
import re

def update_footers():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    about_pattern = re.compile(r'<p class="footer-text mb-4" style="text-align: justify;">', re.IGNORECASE)
    downloads_pattern = re.compile(r'<li><a href="#">Downloads</a></li>', re.IGNORECASE)
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Remove justify
        new_content = about_pattern.sub('<p class="footer-text mb-4">', content)
        
        # 2. Remove Downloads
        new_content = downloads_pattern.sub('', new_content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")

if __name__ == "__main__":
    update_footers()
