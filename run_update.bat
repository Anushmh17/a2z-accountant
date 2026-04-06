@echo off
setlocal enabledelayedexpansion

echo Starting footer update process...
echo.

set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Try running with Node.js first
where node >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Running Node.js script...
    node update_footer.js
    goto :end
)

REM Try running with Python
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Running Python script...
    python update_footer.py
    goto :end
)

REM If neither is available
echo ERROR: Neither Node.js nor Python found in PATH
echo Please install Node.js or Python to run this script
goto :end

:end
echo.
pause
