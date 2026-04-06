# HTML Footer Update - Complete Solution

## Overview
This solution provides automated footer updates for 19 HTML files in the A2Z project. All files will have their `<div class="btSiteFooter">` sections replaced with the new footer content from `master_footer.txt`.

## Files to be Updated (19 Total)
1. about.html
2. contact.html
3. article.html
4. blog.html
5. getquote.html
6. annual-accounts.html
7. business-consultancy.html
8. book-keeping.html
9. management-accounts.html
10. online-accounting.html
11. payroll-services.html
12. personal-tax.html
13. tax-services.html
14. construction.html
15. clinics-surgeries.html
16. care-homes.html
17. hospitality-leisure.html
18. Landlords.html
19. Manufacturing.html
20. retails.html

## How to Run

### Option 1: Double-Click Batch File (EASIEST - Windows Only)
1. Navigate to: `c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z`
2. Double-click: `EXECUTE_FOOTER_UPDATE.bat`
3. Wait for completion and review the results

### Option 2: Command Prompt (Windows)
```cmd
cd c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z
EXECUTE_FOOTER_UPDATE.bat
```

### Option 3: Python Direct (All Platforms)
```bash
cd c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z
python RUN_FOOTER_UPDATE.py
```

### Option 4: Using Python 3 (If Python named as python3)
```bash
cd c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z
python3 RUN_FOOTER_UPDATE.py
```

## What the Script Does

1. **Reads** the new footer from `master_footer.txt` (345 lines of HTML)
2. **Processes** each of the 19 HTML files
3. **Finds** the footer section: `<div class="btSiteFooter">` to `</div><!-- /btSiteFooter -->`
4. **Replaces** the entire footer with the new content
5. **Reports** results showing:
   - ✓ Successfully updated files
   - ✗ Failed updates (if any)
   - Total count of updates

## New Footer Features

The new footer includes:
- ✓ 6-column responsive layout (col-md-6, col-sm-12, col-xs-12)
- ✓ Quick Links section (Home, About, Blog, Get Quote, Contact, Article)
- ✓ Services section (8 service links)
- ✓ Sectors section (7 industry links)
- ✓ Ilford Office contact information
- ✓ Middlesex Office contact information
- ✓ Mobile navigation menu (hidden on desktop)
- ✓ Copyright section with 2-column layout on desktop, centered on mobile
- ✓ Professional styling with gold and black theme

## Footer Structure

### Desktop Layout (Visible on md+ screens)
- 6 columns: About Us | Quick Links | Services | Sectors | Ilford | Middlesex

### Mobile Layout (Visible on xs-sm screens)
- Full-width stacked layout
- Centered navigation menu
- Centered copyright text

## Requirements

- **Python 3.6+** (Usually pre-installed on most systems)
- **Read/Write access** to the HTML files
- **master_footer.txt** file (must exist in the same directory)

## Verification

After running the script, verify that the footer was updated correctly by:

1. Opening one of the updated HTML files in a browser
2. Scrolling to the footer
3. Checking that it displays:
   - Two office locations (Ilford & Middlesex)
   - Quick links, Services, and Sectors sections
   - Copyright information at the bottom
   - Proper responsive layout on mobile

## Troubleshooting

### "Python not found" Error
- Ensure Python 3 is installed: https://www.python.org
- Add Python to your system PATH
- Try using `python3` instead of `python`

### "master_footer.txt not found" Error
- Ensure `master_footer.txt` exists in the same directory as the script
- Check the file name spelling (case-sensitive on some systems)

### Script Runs but "Footer pattern not found"
- The HTML file structure may have changed
- Check if the file contains `<div class="btSiteFooter">` tag
- Manually update the file if needed

### File Access Denied
- Close the file if open in editor
- Check file permissions
- Run command prompt as Administrator (if on Windows)

## Script Details

**Script Files:**
- `RUN_FOOTER_UPDATE.py` - Main Python script (recommended)
- `EXECUTE_FOOTER_UPDATE.bat` - Batch wrapper for Windows
- `master_footer.txt` - New footer HTML content

**How it Works:**
1. Uses regex to find footer pattern: `<div class="btSiteFooter">.*?</div><!-- /btSiteFooter -->`
2. Replaces matched content with new footer
3. Preserves all HTML before and after the footer
4. Writes updated content back to the file

## Safety & Backup

**Before running:**
- The script is safe and non-destructive
- It only modifies the footer section
- Rest of the HTML remains untouched
- Consider making a backup of your project folder

**If needed to revert:**
- Use Git to restore: `git checkout <filename>`
- Or manually restore from backup

## Support

If you encounter issues:
1. Check the error message in the console output
2. Verify all files exist and are readable
3. Ensure Python is properly installed
4. Check file permissions
5. Try running as Administrator

## Success Criteria

The update is successful when:
✓ All 19 files show "Updated successfully"
✓ No "Failed" entries in the report
✓ Total count shows 19 successful updates
✓ Footer displays correctly in browsers
✓ Responsive layout works on mobile devices

---

**Last Updated:** 2024
**Version:** 1.0
**Status:** Ready to Run
