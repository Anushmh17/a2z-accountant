FOOTER UPDATE INSTRUCTIONS
==========================

PURPOSE:
This script updates the footer content in 19 HTML files using the master footer 
from master_footer.txt.

FILES CREATED:
✓ update_footers.py - Main script to update all 19 HTML files
✓ verify_ready.py - Verification script to check if all files are present
✓ This README file

WHAT THE SCRIPT DOES:
1. Reads the new footer content from: master_footer.txt
2. For each of the 19 HTML files, finds the entire btSiteFooter section
3. Replaces everything from <div class="btSiteFooter"> to </div><!-- /btSiteFooter -->
4. Saves the updated file
5. Reports success/failure for each file
6. Provides a summary at the end

HTML FILES TO BE UPDATED (19 total):
- about.html
- contact.html
- article.html
- blog.html
- getquote.html
- annual-accounts.html
- business-consultancy.html
- book-keeping.html
- management-accounts.html
- online-accounting.html
- payroll-services.html
- personal-tax.html
- tax-services.html
- construction.html
- clinics-surgeries.html
- care-homes.html
- hospitality-leisure.html
- Landlords.html
- Manufacturing.html
- retails.html

HOW TO RUN:

Option 1: Using the batch file (Easiest)
-----------------------------------------
1. Navigate to: c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z
2. Double-click: run_footer_update.bat
3. The script will run and show results

Option 2: Using Command Prompt
------------------------------
1. Open Command Prompt (Start → cmd)
2. Navigate to: c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z
   Command: cd /d "c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z"
3. Run: python update_footers.py
4. Watch for the results

Option 3: Using Python IDE
--------------------------
1. Open your Python IDE (PyCharm, VS Code, etc.)
2. Open the file: update_footers.py
3. Run the script
4. View the output in the console

VERIFICATION (Optional):
-----------------------
Before running the main script, you can verify all files are present:
  python verify_ready.py

EXPECTED OUTPUT:
---------------
When successful, you'll see:
✓ about.html: Successfully updated
✓ contact.html: Successfully updated
... (one line for each of the 19 files)

SUMMARY
Total files: 19
Successfully updated: 19
Failed: 0

WHAT TO DO IF SOMETHING GOES WRONG:
-----------------------------------
1. Check that master_footer.txt exists and is not empty
2. Make sure all HTML files are in the same directory
3. Try running verify_ready.py to check file presence
4. Check that Python is properly installed
5. Try running from Command Prompt to see detailed error messages

SAFETY:
------
✓ The script creates backups by not deleting the original files until after verification
✓ The script only updates files that have the btSiteFooter section
✓ Each file is processed independently - if one fails, others continue
✓ You can run the script multiple times safely

CONTACT:
--------
If you need to revert changes, you may have git history:
  git status              # Check current state
  git diff <filename>     # See what changed
  git checkout <filename> # Revert a specific file

CREATED: 2024
LOCATION: c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z
