#!/usr/bin/env python3
"""
FIXED Footer Update Script - With Proper Alignment
Applies the corrected footer from index.html to all other HTML files
"""

import os
import re
import sys

print("="*70)
print("    FOOTER UPDATE SCRIPT - WITH ALIGNMENT FIXES")
print("="*70)
print()

# Change to the correct directory
os.chdir(r'C:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z')

# Read index.html and extract the footer content
print("📂 Reading corrected footer from index.html...")
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Find the btSiteFooter div opening
pattern = r'(<div class="btSiteFooter">.*?</div><!-- /btSiteFooter -->)'
match = re.search(pattern, index_content, re.DOTALL)

if not match:
    print("❌ ERROR: Could not find footer in index.html")
    sys.exit(1)

new_footer = match.group(1)
print(f"✅ Footer extracted: {len(new_footer)} characters")
print()

# Verify the new footer has the fixed alignment classes
if 'col-lg-4' in new_footer and 'col-lg-6' in new_footer:
    print("✅ Confirmed: Footer has FIXED responsive classes")
else:
    print("⚠️  WARNING: Footer may not have the latest alignment fixes")
print()

print("📝 Updating HTML files...")
print("-"*70)

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
        print(f"❌ {filename:35s} - FILE NOT FOUND")
        failed.append(filename)
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire btSiteFooter section
        footer_pattern = r'<div class="btSiteFooter">.*?</div><!-- /btSiteFooter -->'
        
        if not re.search(footer_pattern, content, re.DOTALL):
            print(f"❌ {filename:35s} - NO FOOTER SECTION FOUND")
            failed.append(filename)
            continue
        
        new_content = re.sub(footer_pattern, new_footer, content, count=1, flags=re.DOTALL)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {filename:35s} - Updated successfully")
        success += 1
        
    except Exception as e:
        print(f"❌ {filename:35s} - ERROR: {str(e)}")
        failed.append(filename)

print()
print("="*70)
print(f"✅ SUCCESS: {success}/{len(files)} files updated")
if failed:
    print(f"❌ FAILED:  {', '.join(failed)}")
print("="*70)
print()

# Verification
if success > 0:
    print("🔍 Verifying alignment fixes in sample files...")
    print("-"*70)
    
    import random
    sample_files = random.sample([f for f in files if f not in failed], min(3, success))
    
    for sample_file in sample_files:
        with open(sample_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = {
            'Responsive col-lg classes': 'col-lg-4' in content or 'col-lg-6' in content,
            'About Us column (col-xxl-3)': 'col-xxl-3' in content,
            'Quick Links section': 'Quick Links' in content,
            'Services section': 'Services' in content and 'What We Offer' in content,
            'Sectors section': 'Sectors' in content,
            'Mobile menu': 'bt_bb_hidden_sm bt_bb_hidden_md bt_bb_hidden_lg bt_bb_hidden_xl' in content,
        }
        
        print(f"\n📄 {sample_file}:")
        all_passed = True
        for check, result in checks.items():
            status = '✅' if result else '❌'
            print(f"   {status} {check}")
            if not result:
                all_passed = False
        
        if all_passed:
            print(f"   ✅ All alignment checks PASSED")
    
    print()
    print("="*70)

print()
print("📋 NEXT STEPS:")
print()
print("1. Open index.html in your browser")
print("2. Scroll to the footer")
print("3. Resize the browser window to test:")
print("   - Desktop (1200px+): 6 columns")
print("   - Tablet (768-1199px): 2-3 columns")
print("   - Mobile (<768px): 1 column (centered)")
print()
print("4. Verify alignment looks good on all screen sizes")
print()
print("="*70)
print()

input("Press Enter to close...")
