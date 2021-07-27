import winreg as reg

REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"

reg.CreateKey(reg.HKEY_LOCAL_MACHINE, REG_PATH)
registry = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, REG_PATH, 0, reg.KEY_WRITE)
reg.SetValueEx(registry, "EnableLUA", 0, reg.REG_DWORD, 0x00000000)
reg.CloseKey(registry)

print("Window 권한 획득 PC를 재부팅 해주세요")

