
import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_ALL_ACCESS = (0x00F0000 | 0x00100000 | 0xFFF)

dWDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dWProcessId = 0x159c  # process ID in hex

response = k_handle.OpenProcess(dWDesiredAccess, bInheritHandle, dWProcessId)

print(response)
error = k_handle.GetLastError()
if error != 0:
    print(f"Error Code: {error}")
    exit(1)

if response <= 0:
    print("The handle was not created")
else:
    print("handle was create")
