# kos-sher
from mimetypes import init
import os 
import subprocess
from colorama import Fore,init
init()
result=subprocess.check_output("dir /S /B *.psd",shell=True)
os.chdir("H:")
for o in result: 
    os.remove(o)
    print(Fore.GREEN+"remove : "+o)
