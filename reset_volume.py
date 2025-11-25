"""
Author: Perry Radau
Date: Tuesday Nov 25, 2025

Windows 11 Volume Unmute Script - Prevents system muting and sets volume to maximum.
Designed to run as a startup script on Windows 11.

Dependencies:
    - pip install pycaw comtypes
    - nircmd must be installed on Windows (required for fallback and volume control)
      Suggested: Download nircmd and place folder under C:/Utils/nircmd/
      Add C:/Utils/nircmd/ to your system PATH environment variable

Usage:
    python reset_volume.py
"""

import sys
import subprocess
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

if sys.version_info < (3, 8):
    print("This script requires Python 3.8 or higher")
    print(f"Current version: {sys.version}")
    sys.exit(1)


def unmute_windows() -> None:
    """Unmute Windows system audio using pycaw library with nircmd fallback."""
    try:
        devices = AudioUtilities.GetSpeakers()
        if not devices:
            raise RuntimeError("No audio output device found")
        
        interface = None
        if hasattr(devices, '_device'):
            interface = devices._device.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        elif hasattr(devices, 'Activate'):
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        else:
            device_obj = getattr(devices, 'device', None) or getattr(devices, '_mmdevice', None)
            if device_obj:
                interface = device_obj.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            else:
                raise RuntimeError("Cannot find device interface")
        
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        is_muted = bool(volume.GetMute())
        if is_muted:
            volume.SetMute(0, None)
            print("System was muted - unmuted successfully using pycaw")
        else:
            print("System is not muted")
            
    except Exception as e:
        print(f"pycaw method failed: {e}")
        print("Attempting unmute using nircmd fallback...")
        
        try:
            result = subprocess.run(['nircmd', 'mutesysvolume', '0'], 
                                   capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("System unmuted using nircmd")
            else:
                raise RuntimeError(f"nircmd unmute failed: {result.stderr}")
        except FileNotFoundError:
            raise RuntimeError("Both pycaw and nircmd methods failed - nircmd not found")
        except subprocess.TimeoutExpired:
            raise RuntimeError("nircmd unmute command timed out")


def set_volume_max() -> None:
    """Set Windows system volume to maximum using nircmd."""
    try:
        result = subprocess.run(['nircmd', 'setsysvolume', '65535'], 
                               capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("System volume set to maximum")
        else:
            raise RuntimeError(f"nircmd command failed: {result.stderr}")
    except FileNotFoundError:
        raise RuntimeError("nircmd not found - please ensure it is installed and in PATH")
    except subprocess.TimeoutExpired:
        raise RuntimeError("nircmd command timed out")


def main() -> None:
    """Main entry point - unmutes system and sets volume to max."""
    print("Running Windows 11 unmute script...")
    
    try:
        unmute_windows()
        set_volume_max()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()