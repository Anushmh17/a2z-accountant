#!/usr/bin/env python3
"""
Batch update footers in 19 HTML files to use the new 6-column layout from index.html
"""

import os
import sys

os.chdir(r'C:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z')

files_to_update = [
    "about.html", "contact.html", "article.html", "blog.html", "getquote.html",
    "annual-accounts.html", "business-consultancy.html", "book-keeping.html", 
    "management-accounts.html", "online-accounting.html", "payroll-services.html", 
    "personal-tax.html", "tax-services.html",
    "construction.html", "clinics-surgeries.html", "care-homes.html", 
    "hospitality-leisure.html", "Landlords.html", "Manufacturing.html", "retails.html"
]

# Read the new footer from index.html (lines 2570-2914)
print("Reading new footer from index.html...")
with open("index.html", 'r', encoding='utf-8') as f:
    index_lines = f.readlines()

# Extract lines 2570-2914 (Python uses 0-based indexing, so 2569-2913)
new_footer_lines = index_lines[2569:2914]
new_footer = ''.join(new_footer_lines)

# Remove the closing </main> if it's at the beginning of the footer (it's on line 2911)
if '</main>' in new_footer:
    new_footer = new_footer.replace('</main>\n', '')

print(f"✓ New footer extracted ({len(new_footer)} characters)")
print(f"Updating {len(files_to_update)} HTML files...\n")

success_count = 0
failed_files = []

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        failed_files.append(filename)
        continue
    
    try:
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the footer section
        footer_start = content.find('<div class="btSiteFooter">')
        if footer_start == -1:
            print(f"❌ No footer found in: {filename}")
            failed_files.append(filename)
            continue
        
        # Find the closing tag
        footer_end = content.find('</div><!-- /btSiteFooter -->', footer_start)
        if footer_end == -1:
            print(f"❌ No footer closing tag found in: {filename}")
            failed_files.append(filename)
            continue
        
        # Include the closing comment in the footer
        footer_end += len('</div><!-- /btSiteFooter -->')
        
        # Create the new content
        # The footer should include both opening and closing tags
        new_complete_footer = '<div class="btSiteFooter">\n' + new_footer.rstrip() + '\n    </div><!-- /btSiteFooter -->'
        
        new_content = content[:footer_start] + new_complete_footer + content[footer_end:]
        
        # Write the file back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated: {filename}")
        success_count += 1
        
    except Exception as e:
        print(f"❌ Error updating {filename}: {str(e)}")
        failed_files.append(filename)

print("\n" + "="*50)
print(f"RESULTS: {success_count}/{len(files_to_update)} files updated successfully")
if failed_files:
    print(f"\n⚠️  Failed files ({len(failed_files)}):")
    for f in failed_files:
        print(f"   - {f}")
else:
    print("\n✅ ALL FILES UPDATED SUCCESSFULLY!")

print("\nVerifying updates in 3 random files...")
import random
test_files = [f for f in files_to_update if f in [fn for fn in os.listdir('.') if fn.endswith('.html')]]
if test_files:
    sample_files = random.sample(test_files[:success_count], min(3, success_count))
    for test_file in sample_files:
        with open(test_file, 'r', encoding='utf-8') as f:
            test_content = f.read()
        
        # Check for key features
        checks = {
            '6-column layout': 'col-md-6 col-sm-12 col-xs-12' in test_content,
            'About Us column': 'About Us' in test_content and 'Expert Accountants' in test_content,
            'Quick Links': 'Quick Links' in test_content and 'Main Pages' in test_content,
            'Services column': 'Services' in test_content and 'What We Offer' in test_content,
            'Sectors column': 'Sectors' in test_content and 'Industries We Serve' in test_content,
            'Mobile nav menu': 'bt_bb_hidden_sm bt_bb_hidden_md bt_bb_hidden_lg bt_bb_hidden_xl' in test_content,
            'Copyright section': 'bt_bb_section69a677468936d' in test_content,
            'Normal spacing': 'bt_bb_top_spacing_normal' in test_content or 'bt_bb_bottom_spacing_none' in test_content
        }
        
        print(f"\n{test_file}:")
        all_passed = True
        for check_name, check_result in checks.items():
            status = "✅" if check_result else "❌"
            print(f"  {status} {check_name}")
            if not check_result:
                all_passed = False
        
        if all_passed:
            print(f"  ✨ All checks passed!")
