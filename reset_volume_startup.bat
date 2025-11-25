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

REM Run the Python script
echo Running reset_volume.py...
python reset_volume.py

REM Optional: Uncomment the next line if you want to see the output window briefly
REM timeout /t 3 /nobreak >nul
