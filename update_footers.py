#!/usr/bin/env python3
"""
Update footer content in 19 HTML files
Reads new footer from master_footer.txt and replaces the btSiteFooter section
"""

import os
import re
from pathlib import Path

# Configuration
WORKING_DIR = r"c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z"
FOOTER_SOURCE = os.path.join(WORKING_DIR, "master_footer.txt")

HTML_FILES = [
    "about.html",
    "contact.html",
    "article.html",
    "blog.html",
    "getquote.html",
    "annual-accounts.html",
    "business-consultancy.html",
    "book-keeping.html",
    "management-accounts.html",
    "online-accounting.html",
    "payroll-services.html",
    "personal-tax.html",
    "tax-services.html",
    "construction.html",
    "clinics-surgeries.html",
    "care-homes.html",
    "hospitality-leisure.html",
    "Landlords.html",
    "Manufacturing.html",
    "retails.html"
]

def read_new_footer():
    """Read the new footer content from master_footer.txt"""
    try:
        with open(FOOTER_SOURCE, 'r', encoding='utf-8') as f:
            footer_content = f.read()
        return footer_content
    except Exception as e:
        print(f"ERROR: Could not read master_footer.txt: {e}")
        return None

def update_file(filepath, new_footer):
    """
    Update a single HTML file with new footer content
    Returns True if successful, False otherwise
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match the entire btSiteFooter div section
        pattern = r'<div class="btSiteFooter">.*?</div><!-- /btSiteFooter -->'
        
        # Check if the pattern exists
        if not re.search(pattern, content, re.DOTALL):
            print(f"  ✗ {os.path.basename(filepath)}: btSiteFooter section not found")
            return False
        
        # Replace the old footer with the new one
        updated_content = re.sub(pattern, new_footer, content, flags=re.DOTALL)
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"  ✓ {os.path.basename(filepath)}: Successfully updated")
        return True
        
    except Exception as e:
        print(f"  ✗ {os.path.basename(filepath)}: Error - {e}")
        return False

def main():
    """Main function to update all HTML files"""
    print("=" * 60)
    print("Footer Update Script")
    print("=" * 60)
    print(f"Working Directory: {WORKING_DIR}")
    print(f"Footer Source: {FOOTER_SOURCE}")
    print()
    
    # Read the new footer
    print("Reading new footer content...")
    new_footer = read_new_footer()
    if new_footer is None:
        print("Failed to read footer. Exiting.")
        return
    
    footer_size = len(new_footer)
    print(f"New footer size: {footer_size} bytes")
    print()
    
    # Process each HTML file
    print("Updating HTML files:")
    print("-" * 60)
    
    successful = 0
    failed = 0
    
    for html_file in HTML_FILES:
        filepath = os.path.join(WORKING_DIR, html_file)
        
        if not os.path.exists(filepath):
            print(f"  ✗ {html_file}: File not found")
            failed += 1
            continue
        
        if update_file(filepath, new_footer):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("-" * 60)
    print()
    print("SUMMARY")
    print("=" * 60)
    print(f"Total files: {len(HTML_FILES)}")
    print(f"Successfully updated: {successful}")
    print(f"Failed: {failed}")
    print("=" * 60)

if __name__ == "__main__":
    main()
