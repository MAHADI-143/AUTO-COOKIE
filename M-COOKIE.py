import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from cokies import print
 
        print()
 
 
 
elif bit == "32bit":
 
        from DM32 import menu
 
 
        menu()
 
