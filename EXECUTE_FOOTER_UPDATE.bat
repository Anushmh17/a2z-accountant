@echo off
REM Footer Update Batch File
REM This script will execute the Python footer update script

cd /d "c:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z"

echo.
echo ========================================
echo HTML Footer Update Utility
echo ========================================
echo.
echo Starting footer update process...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python or add it to your system PATH
    pause
    exit /b 1
)

REM Run the Python script
python RUN_FOOTER_UPDATE.py

REM Check if successful
if errorlevel 0 (
    echo.
    echo ========================================
    echo Footer update process completed!
    echo ========================================
    echo.
) else (
    echo.
    echo ERROR: Footer update process failed
    echo.
)

pause
