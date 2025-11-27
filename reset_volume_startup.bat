@echo off
REM Reset Volume Startup Script for Windows 11
REM Author: Perry Radau
REM Date: Tuesday Nov 25, 2025
REM
REM This batch file runs the cross-platform reset_volume.py script at Windows startup.
REM Place this file in the Windows Startup folder.
REM Script location: C:\Users\functional\Documents\python_scripts

REM Change to the script directory
cd /d "C:\Users\functional\Documents\python_scripts"

REM Try to run with python command (both python and python3 now point to Python 3.11)
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Running reset_volume.py with python...
    
    REM Check if dependencies are installed, install if missing
    python -c "import pycaw, comtypes" >nul 2>&1
    if %errorlevel% neq 0 (
        echo Installing missing dependencies...
        python -m pip install pycaw comtypes
    )
    
    python reset_volume.py
    goto :end
)

REM If python command not found, try py launcher
py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Running reset_volume.py with py launcher...
    
    REM Check if dependencies are installed, install if missing
    py -c "import pycaw, comtypes" >nul 2>&1
    if %errorlevel% neq 0 (
        echo Installing missing dependencies...
        py -m pip install pycaw comtypes
    )
    
    py reset_volume.py
    goto :end
)

REM If still not found, show error
echo ERROR: Python not found in PATH
echo Please ensure Python 3.8+ is installed and accessible
echo Required dependencies for Windows: pip install pycaw comtypes
echo Script should be located at: C:\Users\functional\Documents\python_scripts\reset_volume.py
pause

:end
REM Optional: Uncomment the next line if you want to see the output window briefly
REM timeout /t 3 /nobreak >nul





