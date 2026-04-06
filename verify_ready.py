#!/usr/bin/env python3
"""
Quick verification script to check footer update readiness
"""

import os

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

print("=" * 70)
print("FOOTER UPDATE READINESS CHECK")
print("=" * 70)
print()

# Check footer source
if os.path.exists(FOOTER_SOURCE):
    footer_size = os.path.getsize(FOOTER_SOURCE)
    print(f"✓ Master footer found: {footer_size} bytes")
else:
    print(f"✗ Master footer NOT found at: {FOOTER_SOURCE}")
    exit(1)

print()
print("Checking HTML files:")
print("-" * 70)

all_exist = True
for html_file in HTML_FILES:
    filepath = os.path.join(WORKING_DIR, html_file)
    if os.path.exists(filepath):
        print(f"  ✓ {html_file}")
    else:
        print(f"  ✗ {html_file} - NOT FOUND")
        all_exist = False

print()
print("=" * 70)
if all_exist:
    print("✓ All files are ready for footer update")
    print()
    print("To update footers, run: python update_footers.py")
else:
    print("✗ Some files are missing")
print("=" * 70)
