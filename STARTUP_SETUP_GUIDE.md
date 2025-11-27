# Windows 11 Startup Setup Guide for Reset Volume Script

## Task Scheduler Method (Recommended for Windows 11 Security Compliance)

**Why Task Scheduler instead of Startup Folder?**
- More secure and compliant with Windows 11 security policies
- Better suited for environments where computers are infrequently restarted
- Runs at user logon and workstation unlock events
- More reliable and easier to manage

### Prerequisites
1. **Python 3.8+** installed on the system
2. **Required Python packages** (Windows only):
    These should be installed automatically by the bat file if absent.
   ```cmd
   pip install pycaw comtypes
   ```
3. **nircmd utility** (required for fallback and volume control):
   - Download nircmd from: https://www.nirsoft.net/utils/nircmd.html
   - Extract to: `C:\Utils\nircmd\` (recommended location)
   - Add `C:\Utils\nircmd\` to your system PATH environment variable

### Setup Steps
1. **Edit the batch file** to point to your script location:
   - Open `reset_volume_startup.bat` in a text editor (like Notepad)
   - Find the line that looks like: `cd /d "C:\path\to\your\script\folder"`
   - Replace `C:\path\to\your\script\folder` with the actual path where you saved the Python script
   - Example: `cd /d "C:\Users\YourName\Documents\reset_volume"`
   - Save the file

2. **Create a Task Scheduler task**:
   - Press `Win + R` and type: `taskschd.msc`
   - Press Enter to open Task Scheduler
   - In the right panel, click "Create Task..."
   - **General tab**:
     - Name: "Reset Volume on Logon"
     - Check "Run only when user is logged on"
     - Check "Run with highest privileges" (if needed for volume control)
     - Check "Hidden" (optional)
   - **Triggers tab**:
     - Click "New..."
     - Begin the task: "At log on"
     - Specific user: Select your user account
     - Check "Enabled"
     - Click "OK"
   - **Actions tab**:
     - Click "New..."
     - Action: "Start a program"
     - Program/script: Browse to your `reset_volume_startup.bat` file
     - Start in: Set to the directory containing your script (e.g., `C:\Users\YourName\Documents\reset_volume`)
     - Click "OK"
   - **Conditions tab** (optional but recommended):
     - Uncheck "Start the task only if the computer is on AC power" (if applicable)
   - Click "OK" to save the task

3. **That's it!** The script will run automatically when you log in or unlock your workstation

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
cd C:\path\to\your\actual\script\folder
reset_volume_startup.bat
```
*Replace `C:\path\to\your\actual\script\folder` with your real script location*

**Test the Python script directly:**
```cmd
cd C:\path\to\your\actual\script\folder
python reset_volume.py
```
*Replace `C:\path\to\your\actual\script\folder` with your real script location*

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
- Extract the `nircmd.exe` file to a folder like `C:\Utils\nircmd\`
- **Add nircmd to your system PATH** (required for the script to find it):
  1. Press `Win + X` and select "System" (or right-click "This PC" → Properties)
  2. Click "Advanced system settings" on the right side
  3. In the System Properties window, click "Environment Variables"
  4. Under "System variables" (bottom section), find and select "Path"
  5. Click "Edit..."
  6. In the Edit Environment Variable window, click "New"
  7. Type the full path to your nircmd folder: `C:\Utils\nircmd\`
  8. Click "OK" to close all windows
  9. **Important**: Restart your computer for PATH changes to take effect
- **Test that nircmd works**: Open Command Prompt and type `nircmd` - you should see the help text

**If the script doesn't run at logon/unlock:**
- Open Task Scheduler (`taskschd.msc`) and verify the task exists and is enabled
- Right-click the task and select "Run" to test it manually
- Check the task's History tab for any error messages
- Test the batch file manually first
- Check that Python and dependencies are properly installed

### Task Scheduler Access
- **Quick access**: Press `Win + R`, type `taskschd.msc`
- **Alternative**: Search for "Task Scheduler" in Windows search
- **Library location**: Task Scheduler Library → Your created tasks appear here
