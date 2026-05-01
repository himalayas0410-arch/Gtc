import os
import re

def sync_all():
    base_dir = r"c:\Users\HIMANSHU\Desktop\papa website\New folder\Gtccopy"
    index_path = os.path.join(base_dir, "index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # 1. Extract Master Nav Block (Header + Mobile Overlay)
    # Starts at <div class="header home-header"> and ends at the end of the mobile overlay
    nav_match = re.search(r'(<div class="header home-header">.*?<div class="mobile-overlay" id="mobileOverlay">.*?<nav class="mobile-nav">.*?</nav>\s*</div>)', index_content, re.DOTALL)
    if not nav_match:
        print("Could not find master nav block")
        return
    master_nav = nav_match.group(1)

    # 2. Extract Master Footer
    footer_match = re.search(r'(<footer class="footer-dark py-5".*?</footer>)', index_content, re.DOTALL)
    if not footer_match:
        print("Could not find master footer")
        return
    master_footer = footer_match.group(1)

    html_files = [f for f in os.listdir(base_dir) if f.endswith(".html") and f != "index.html" and f != "sync_nav.py"]

    for filename in html_files:
        file_path = os.path.join(base_dir, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire Nav Block (Header + Overlay)
        # We look for <div class="header" and replace everything until the end of the mobile-overlay
        # This will clean up any nested headers from previous runs
        content = re.sub(r'<div class="header.*?<div class="mobile-overlay".*?</nav>\s*</div>', master_nav, content, flags=re.DOTALL, count=1)
        
        # Replace Footer
        content = re.sub(r'<footer.*?</footer>', master_footer, content, flags=re.DOTALL, count=1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Synced {filename}")

if __name__ == "__main__":
    sync_all()
