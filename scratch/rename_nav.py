import os
import re

def rename_nav_items():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Define the renames
    renames = [
        (re.compile(r'About the Directorate', re.IGNORECASE), 'About the Committee'),
        (re.compile(r'Member of the group', re.IGNORECASE), 'Member of the Committee'),
        (re.compile(r'Member of the Group', re.IGNORECASE), 'Member of the Committee') # Just in case
    ]
    
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for pattern, replacement in renames:
            new_content = pattern.sub(replacement, new_content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")

if __name__ == "__main__":
    rename_nav_items()
