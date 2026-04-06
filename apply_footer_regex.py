#!/usr/bin/env python3
"""
Apply new footer from index.html to all other HTML files
"""

import os
import re

os.chdir(r'C:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z')

# Read index.html and extract the footer content
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Find the btSiteFooter div opening
match = re.search(r'(<div class="btSiteFooter">.*?</div><!-- /btSiteFooter -->)', index_content, re.DOTALL)
if not match:
    print("ERROR: Could not find footer in index.html")
    exit(1)

new_footer = match.group(1)

# Clean it up - remove the closing </main> if it exists from index.html
new_footer = re.sub(r'\s*</main>\s*', '\n', new_footer)

print(f"Footer extracted: {len(new_footer)} characters")
print("Updating files...")

files = [
    "about.html", "contact.html", "article.html", "blog.html", "getquote.html",
    "annual-accounts.html", "business-consultancy.html", "book-keeping.html",
    "management-accounts.html", "online-accounting.html", "payroll-services.html",
    "personal-tax.html", "tax-services.html",
    "construction.html", "clinics-surgeries.html", "care-homes.html",
    "hospitality-leisure.html", "Landlords.html", "Manufacturing.html", "retails.html"
]

success = 0
failed = []

for filename in files:
    if not os.path.exists(filename):
        print(f"❌ {filename}: NOT FOUND")
        failed.append(filename)
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire btSiteFooter section
        # Match from <div class="btSiteFooter"> to </div><!-- /btSiteFooter -->
        pattern = r'<div class="btSiteFooter">.*?</div><!-- /btSiteFooter -->'
        
        if not re.search(pattern, content, re.DOTALL):
            print(f"❌ {filename}: NO FOOTER FOUND")
            failed.append(filename)
            continue
        
        new_content = re.sub(pattern, new_footer, content, count=1, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {filename}")
        success += 1
        
    except Exception as e:
        print(f"❌ {filename}: {str(e)}")
        failed.append(filename)

print(f"\n{'='*50}")
print(f"SUCCESS: {success}/{len(files)}")
if failed:
    print(f"FAILED: {', '.join(failed)}")

# Verify
print("\nVerifying 3 sample files...")
import random
for sample_file in random.sample([f for f in files if f not in failed], min(3, len([f for f in files if f not in failed]))):
    with open(sample_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        '6-column layout': 'col-md-6 col-sm-12 col-xs-12' in content,
        'About Us': 'About Us' in content,
        'Quick Links': 'Quick Links' in content,
        'Services': 'Services' in content,
        'Sectors': 'Sectors' in content,
        'Mobile menu': 'bt_bb_hidden_sm bt_bb_hidden_md bt_bb_hidden_lg bt_bb_hidden_xl' in content,
    }
    
    print(f"\n{sample_file}:")
    for check, result in checks.items():
        print(f"  {'✅' if result else '❌'} {check}")
