# Windows 11 Startup Setup Guide for Reset Volume Script

## Simple Batch File Method (Easiest)

### Prerequisites
1. **Python 3.8+** installed on the system
2. **Required Python packages** (Windows only):
   ```cmd
   pip install pycaw comtypes
   ```
3. **nircmd utility** (required for fallback and volume control):
   - Download nircmd from: https://www.nirsoft.net/utils/nircmd.html
   - Extract to: `C:\Utils\nircmd\` (recommended location)
   - Add `C:\Utils\nircmd\` to your system PATH environment variable

### Setup Steps
1. **Copy the batch file** to Windows Startup folder:
   - Press `Win + R` and type: `shell:startup`
   - Press Enter to open the Startup folder
   - Copy `reset_volume_startup.bat` to this folder

2. **That's it!** The script will run automatically when you log in

### How It Works
The batch file (`reset_volume_startup.bat`) automatically:
- Finds your Python installation
- Changes to the correct directory
- Runs the `reset_volume.py` script which:
  - Unmutes the system if it's muted
  - Sets system volume to maximum
  - Uses pycaw as primary method with nircmd as fallback
- Shows helpful error messages if something goes wrong

### Testing
**Test the batch file manually:**
```cmd
cd C:\path\to\your\script\folder
reset_volume_startup.bat
```

**Test the Python script directly:**
```cmd
cd C:\path\to\your\script\folder
python reset_volume.py
```

### Troubleshooting

**If Python is not found:**
- Make sure Python is installed with "Add to PATH" option checked
- Try reinstalling Python from python.org
- The batch file will try multiple ways to find Python automatically

**If dependencies are missing:**
```cmd
pip install pycaw comtypes
```

**If nircmd is not found:**
- Download nircmd from: https://www.nirsoft.net/utils/nircmd.html
- Extract to `C:\Utils\nircmd\` (or another location)
- Add the nircmd folder to your system PATH:
  1. Press `Win + X` and select "System"
  2. Click "Advanced system settings"
  3. Click "Environment Variables"
  4. Under "System variables", find and select "Path", then click "Edit"
  5. Click "New" and add `C:\Utils\nircmd\`
  6. Click "OK" to save changes
- Restart your computer for PATH changes to take effect

**If the script doesn't run at startup:**
- Make sure the batch file is in the correct Startup folder
- Test the batch file manually first
- Check that Python and dependencies are properly installed

### Startup Folder Location
- **Quick access**: Press `Win + R`, type `shell:startup`
- **Full path**: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
