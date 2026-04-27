import os

files = [
    "index.html", "about.html", "members.html", "itec-programs.html", 
    "certificate-courses.html", "reports-publications.html", 
    "partnerships.html", "opportunities.html", "global-presence.html", 
    "events.html", "contact.html"
]

duplicate_line = '<li><a href="images/accountax.jpg" target="_blank" onclick="toggleMobileMenu()">ICAI Members’ Delegation</a></li>'
duplicate_block = duplicate_line + '\n                        ' + duplicate_line

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if duplicate_block in content:
            new_content = content.replace(duplicate_block, duplicate_line)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Sanitized {filename}")
        else:
             # Check for different indentation or whitespace
             pattern = duplicate_line.replace('(', r'\(').replace(')', r'\)')
             # Simpler: just replace two occurrences of the delegation text in a row
             lines = content.split('\n')
             new_lines = []
             last_line = ""
             changed = False
             for line in lines:
                 if duplicate_line.strip() in line and duplicate_line.strip() in last_line:
                     changed = True
                     continue # skip duplicate
                 new_lines.append(line)
                 last_line = line
             
             if changed:
                 with open(filename, 'w', encoding='utf-8') as f:
                     f.write('\n'.join(new_lines))
                 print(f"Sanitized {filename} (line by line)")
             else:
                 print(f"No duplicates in {filename}")
    else:
        print(f"File not found: {filename}")
