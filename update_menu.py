import os
import re

files = [
    "index.html", "about.html", "members.html", "itec-programs.html", 
    "certificate-courses.html", "reports-publications.html", 
    "partnerships.html", "opportunities.html", "global-presence.html", 
    "events.html", "contact.html"
]

delegation_text = "ICAI Members’ Delegation"

# Desktop regex
desktop_pattern = r'<a href="images/accountax\.jpg" target="_blank">Accountax</a>'
desktop_replacement = '<a href="images/accountax.jpg" target="_blank">ICAI Members’ Delegation</a>\n                                        <a href="images/accountax.jpg" target="_blank">Accountax</a>'

# Mobile regex (standard dropdown)
mobile_pattern_dropdown = r'<li><a href="images/accountax\.jpg" target="_blank" onclick="toggleMobileMenu\(\)">Accountax</a>\s*</li>'
mobile_replacement_dropdown = '<li><a href="images/accountax.jpg" target="_blank" onclick="toggleMobileMenu()">ICAI Members’ Delegation</a></li>\n                        <li><a href="images/accountax.jpg" target="_blank" onclick="toggleMobileMenu()">Accountax</a></li>'

# Mobile regex (flat link - convert to dropdown)
mobile_pattern_flat = r'<li><a href="images/Sponsorship matrix 13-04-2026\.pdf" target="_blank" onclick="toggleMobileMenu\(\)">Member Opportunities</a></li>'
mobile_replacement_flat = '''<li class="mobile-has-dropdown">
                    <a href="#" onclick="event.preventDefault(); this.nextElementSibling.classList.toggle('active');">Member Opportunities <span class="material-symbols-outlined">expand_more</span></a>
                    <ul class="mobile-sub-menu">
                        <li><a href="images/accountax.jpg" target="_blank" onclick="toggleMobileMenu()">ICAI Members’ Delegation</a></li>
                        <li><a href="images/accountax.jpg" target="_blank" onclick="toggleMobileMenu()">Accountax</a></li>
                        <li><a href="images/Sponsorship matrix 13-04-2026.pdf" target="_blank" onclick="toggleMobileMenu()">Sponsorship Matrix</a></li>
                    </ul>
                </li>'''

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        
        # Apply desktop replacement if not already there
        if delegation_text not in content:
             new_content = re.sub(desktop_pattern, desktop_replacement, new_content)
        
        # Apply mobile replacements
        # First try dropdown style
        temp_content = re.sub(mobile_pattern_dropdown, mobile_replacement_dropdown, new_content)
        if temp_content != new_content:
            new_content = temp_content
        else:
            # If no dropdown match, try converting flat link
            new_content = re.sub(mobile_pattern_flat, mobile_replacement_flat, new_content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")
    else:
        print(f"File not found: {filename}")
