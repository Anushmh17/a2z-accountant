@echo off
echo ========================================================================
echo          APPLY FIXED FOOTER WITH PROPER ALIGNMENT
echo ========================================================================
echo.
echo This script will apply the corrected footer to all 19 HTML pages.
echo.
echo What's been fixed:
echo   - Proper responsive column widths
echo   - Better desktop spacing
echo   - Centered mobile layout
echo   - Touch-friendly mobile links
echo   - Tablet-optimized 3-column layout
echo.
echo ========================================================================
echo.
pause

python apply_fixed_footer.py

echo.
echo ========================================================================
echo.
echo DONE! Check the output above for results.
echo.
pause
