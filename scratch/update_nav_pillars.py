import os
import re

patterns = [
    # Desktop nav pattern for Global Initiatives
    (re.compile(r'<li style="animation-delay: 0\.3s" class="reveal-up has-dropdown">\s*<a href="#">Global Initiatives <span class="material-symbols-outlined".*?</span></a>\s*<div class="nav-dropdown nav-panel">.*?</li>', re.DOTALL),
     '''<li style="animation-delay: 0.3s" class="reveal-up has-dropdown">
                                    <a href="#">Global Initiatives <span class="material-symbols-outlined"
                                            style="font-size: 16px; vertical-align: text-bottom;">expand_more</span></a>
                                    <div class="nav-dropdown">
                                        <a href="https://gcc.icai.org/">GCC Initiatives</a>
                                        <a href="global-udaan.html">Global Udaan</a>
                                        <div class="has-nested">
                                            <a href="index.html#pillar-board">The 5 Pillars</a>
                                            <div class="nested-dropdown">
                                                <a href="index.html#pillar-board" onclick="if(window.selectPillar) selectPillar(1)">01 Trade Policy & Institutional Engagement</a>
                                                <a href="index.html#pillar-board" onclick="if(window.selectPillar) selectPillar(2)">02 Global Services & Professional Mobility</a>
                                                <a href="index.html#pillar-board" onclick="if(window.selectPillar) selectPillar(3)">03 Strategic Partnerships & Collaborations</a>
                                                <a href="index.html#pillar-board" onclick="if(window.selectPillar) selectPillar(4)">04 GCC & Emerging Global Ecosystems</a>
                                                <a href="index.html#pillar-board" onclick="if(window.selectPillar) selectPillar(5)">05 Capacity Building Programs</a>
                                            </div>
                                        </div>
                                    </div>
                                </li>'''),
    # Mobile nav pattern
    (re.compile(r'<li class="mobile-has-dropdown">\s*<a href="#"\s+onclick="event\.preventDefault\(\); this\.nextElementSibling\.classList\.toggle\(\'active\'\);">Global\s+Initiatives.*?</ul>\s*</li>', re.DOTALL),
     '''<li class="mobile-has-dropdown">
                    <a href="#"
                        onclick="event.preventDefault(); this.nextElementSibling.classList.toggle('active');">Global
                        Initiatives <span class="material-symbols-outlined">expand_more</span></a>
                    <ul class="mobile-sub-menu">
                        <li><a href="https://gcc.icai.org/" onclick="toggleMobileMenu()">GCC Initiatives</a></li>
                        <li><a href="global-udaan.html" onclick="toggleMobileMenu()">Global Udaan</a></li>
                        <li class="mobile-has-dropdown">
                            <a href="#" style="padding-left: 30px !important; font-size: 0.9em !important;"
                                onclick="event.preventDefault(); this.nextElementSibling.classList.toggle('active');">The 5 Pillars <span class="material-symbols-outlined">expand_more</span></a>
                            <ul class="mobile-sub-menu">
                                <li><a href="index.html#pillar-board" onclick="toggleMobileMenu(); if(window.selectPillar) selectPillar(1)">01 Trade Policy</a></li>
                                <li><a href="index.html#pillar-board" onclick="toggleMobileMenu(); if(window.selectPillar) selectPillar(2)">02 Professional Mobility</a></li>
                                <li><a href="index.html#pillar-board" onclick="toggleMobileMenu(); if(window.selectPillar) selectPillar(3)">03 Strategic Partnerships</a></li>
                                <li><a href="index.html#pillar-board" onclick="toggleMobileMenu(); if(window.selectPillar) selectPillar(4)">04 GCC Ecosystems</a></li>
                                <li><a href="index.html#pillar-board" onclick="toggleMobileMenu(); if(window.selectPillar) selectPillar(5)">05 Capacity Building</a></li>
                            </ul>
                        </li>
                    </ul>
                </li>''')
]

for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'index.html':
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            try:
                with open(filename, 'r', encoding='latin-1') as f:
                    content = f.read()
            except:
                continue
        
        new_content = content
        for p, r in patterns:
            new_content = p.sub(r, new_content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
