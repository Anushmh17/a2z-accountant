#!/usr/bin/env python3
"""
Footer Update Script - Batch update HTML files with new footer content
Updates the <div class="btSiteFooter"> section in multiple HTML files
"""

import re
import os
from pathlib import Path

# List of HTML files to update
HTML_FILES = [
    'about.html',
    'contact.html',
    'article.html',
    'blog.html',
    'getquote.html',
    'annual-accounts.html',
    'business-consultancy.html',
    'book-keeping.html',
    'management-accounts.html',
    'online-accounting.html',
    'payroll-services.html',
    'personal-tax.html',
    'tax-services.html',
    'construction.html',
    'clinics-surgeries.html',
    'care-homes.html',
    'hospitality-leisure.html',
    'Landlords.html',
    'Manufacturing.html',
    'retails.html'
]

def read_master_footer(footer_file='master_footer.txt'):
    """Read the new footer content from master_footer.txt"""
    try:
        with open(footer_file, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✓ Successfully read master footer from {footer_file}")
        return content
    except FileNotFoundError:
        print(f"✗ Error: {footer_file} not found!")
        return None
    except Exception as e:
        print(f"✗ Error reading {footer_file}: {e}")
        return None

def update_footer_in_file(file_path, new_footer):
    """Replace the footer section in an HTML file"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create regex pattern to match the entire btSiteFooter section
        # Matches from <div class="btSiteFooter"> to </div><!-- /btSiteFooter -->
        pattern = r'<div class="btSiteFooter">.*?</div><!-- /btSiteFooter -->'
        
        # Check if pattern exists
        if not re.search(pattern, content, re.DOTALL):
            return False, "Footer pattern not found in file"
        
        # Replace the footer section
        updated_content = re.sub(pattern, new_footer.strip(), content, flags=re.DOTALL)
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True, "Success"
    
    except Exception as e:
        return False, str(e)

def main():
    """Main function to update all HTML files"""
    print("=" * 70)
    print("FOOTER UPDATE SCRIPT - Batch Processing")
    print("=" * 70)
    print()
    
    # Read the master footer content
    new_footer = read_master_footer()
    if not new_footer:
        print("\n✗ Failed to read master footer. Exiting.")
        return
    
    print()
    print("-" * 70)
    print("Processing HTML Files...")
    print("-" * 70)
    
    # Track results
    successful_updates = []
    failed_updates = []
    
    # Update each file
    for html_file in HTML_FILES:
        file_path = Path(html_file)
        
        if not file_path.exists():
            print(f"⚠ {html_file:30s} - File not found, skipping")
            failed_updates.append((html_file, "File not found"))
            continue
        
        success, message = update_footer_in_file(file_path, new_footer)
        
        if success:
            print(f"✓ {html_file:30s} - Updated successfully")
            successful_updates.append(html_file)
        else:
            print(f"✗ {html_file:30s} - Failed: {message}")
            failed_updates.append((html_file, message))
    
    # Print summary
    print()
    print("=" * 70)
    print("SUMMARY REPORT")
    print("=" * 70)
    print(f"\nTotal files to update: {len(HTML_FILES)}")
    print(f"Successfully updated:   {len(successful_updates)}")
    print(f"Failed:                 {len(failed_updates)}")
    
    if successful_updates:
        print(f"\n✓ Successfully Updated ({len(successful_updates)} files):")
        for file in successful_updates:
            print(f"  - {file}")
    
    if failed_updates:
        print(f"\n✗ Failed Updates ({len(failed_updates)} files):")
        for file, reason in failed_updates:
            print(f"  - {file}: {reason}")
    
    print()
    if len(successful_updates) == len(HTML_FILES):
        print("🎉 All files updated successfully!")
    elif len(successful_updates) > 0:
        print("⚠ Partial success - some files were updated, but others failed.")
    else:
        print("✗ No files were updated.")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
