
import ctypes

# reference for API calls
user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")  # this will handle our error messages

hWnd = None  # creates message box of the owner, if the parameter = NULL then box has no owner
lpText = "Hello World"  # this is the message that is displayed in the window's API
lpCaption = "I am the Title King"  # the title of the message box
uType = 0x00000001  # this determines the behavior of the message box, could be a parameters or group of parameters

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

error = k_handle.GetLastError()
if error != 0:
    print(f"Error Code: {error}")
    exit(1)

if response == 1:
    print("User clicked OK!")
elif response == 2:
    print("User clicked Cancel")
    
