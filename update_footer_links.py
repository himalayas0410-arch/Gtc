import os
import re

# The new link provided by the user
new_link = "https://docs.google.com/forms/d/e/1FAIpQLSdHkFQqMV6Mnt3ZXMu47Hw8XIR6fu59ZP5wSWu5MsYAXgiuLg/viewform"

# Target text to find in the anchor tag
target_text = "Member Opportunities"

# Regex pattern explanation:
# 1. (<a[^>]*href=)          -> Group 1: Matches the start of the tag up to href=
# 2. "[^"]*"                 -> Matches the existing href value in double quotes
# 3. ([^>]*>\s*Member Opportunities\s*(?:<span[^>]*>.*?</span>\s*)?</a>)
#                            -> Group 2: Matches the rest of the attributes, the closing >, 
#                               the text "Member Opportunities" (with optional whitespace),
#                               an optional <span> (like the one in video-player.html),
#                               and the closing </a> tag.
pattern = re.compile(r'(<a[^>]*href=)"[^"]*"([^>]*>\s*' + re.escape(target_text) + r'\s*(?:<span[^>]*>.*?</span>\s*)?</a>)', re.IGNORECASE | re.DOTALL)

updated_count = 0

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        file_path = os.path.join('.', filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace using the pattern
            new_content = pattern.sub(rf'\1"{new_link}"\2', content)
            
            if content != new_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Successfully updated: {filename}")
                updated_count += 1
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"\nTotal files updated: {updated_count}")
