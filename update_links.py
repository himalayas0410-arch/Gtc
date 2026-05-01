import os

old_link = 'https://www.icai.org/post/cditswto-global-udaan'
new_link = 'global-udaan.html'

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if old_link in content:
                new_content = content.replace(old_link, new_link)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {path}")
