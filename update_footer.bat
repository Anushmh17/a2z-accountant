@echo off
REM Update footer in all HTML files
cd /d "C:\xampp\htdocs\Webbuilders Projects\A2Z\A2Z"

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing...
    exit /b 1
)

REM Run the Python script
python update_footer.py
pause
