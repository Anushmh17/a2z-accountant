#!/usr/bin/env python3
import os
import sys

# Set working directory
os.chdir(r'C:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z')

files_to_update = [
    "about.html", "contact.html", "article.html", "blog.html", "getquote.html",
    "annual-accounts.html", "business-consultancy.html", "book-keeping.html", 
    "management-accounts.html", "online-accounting.html", "payroll-services.html", 
    "personal-tax.html", "tax-services.html",
    "construction.html", "clinics-surgeries.html", "care-homes.html", 
    "hospitality-leisure.html", "Landlords.html", "Manufacturing.html", "retails.html"
]

# Read the new footer from index.html
with open("index.html", 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract footer from index.html
footer_start = index_content.find('<div class="btSiteFooter">')
if footer_start == -1:
    print("ERROR: Could not find footer in index.html")
    sys.exit(1)

# Find the matching closing </div> by counting
div_count = 1
pos = footer_start + len('<div class="btSiteFooter">')
footer_end = -1

while pos < len(index_content) and div_count > 0:
    next_open = index_content.find('<div', pos)
    next_close = index_content.find('</div>', pos)
    
    if next_close == -1:
        break
    if next_open == -1 or next_close < next_open:
        div_count -= 1
        if div_count == 0:
            footer_end = next_close + 6
            break
        pos = next_close + 6
    else:
        div_count += 1
        pos = next_open + 4

if footer_end == -1:
    print("ERROR: Could not find closing footer tag")
    sys.exit(1)

new_footer = index_content[footer_start:footer_end]
print(f"New footer length: {len(new_footer)} characters")
print(f"Updating {len(files_to_update)} HTML files...\n")

success_count = 0
failed_files = []

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"❌ File not found: {filename}")
        failed_files.append(filename)
        continue
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the footer section
        footer_start = content.find('<div class="btSiteFooter">')
        if footer_start == -1:
            print(f"❌ No footer found in: {filename}")
            failed_files.append(filename)
            continue
        
        # Find matching closing </div> for btSiteFooter
        div_count = 1
        pos = footer_start + len('<div class="btSiteFooter">')
        footer_end = -1
        
        while pos < len(content) and div_count > 0:
            next_open = content.find('<div', pos)
            next_close = content.find('</div>', pos)
            
            if next_close == -1:
                break
            if next_open == -1 or next_close < next_open:
                div_count -= 1
                if div_count == 0:
                    footer_end = next_close + 6
                    break
                pos = next_close + 6
            else:
                div_count += 1
                pos = next_open + 4
        
        if footer_end == -1:
            print(f"❌ Could not find closing footer tag in: {filename}")
            failed_files.append(filename)
            continue
        
        # Replace the old footer with the new one
        new_content = content[:footer_start] + new_footer + content[footer_end:]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated: {filename}")
        success_count += 1
        
    except Exception as e:
        print(f"❌ Error updating {filename}: {str(e)}")
        failed_files.append(filename)

print("\n" + "="*40)
print(f"Updated: {success_count} files")
if failed_files:
    print(f"Failed: {len(failed_files)} files")
    print(f"Failed files: {', '.join(failed_files)}")
else:
    print("All files updated successfully!")
