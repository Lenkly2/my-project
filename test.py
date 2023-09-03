import os
  
shutdown = input("хто ви?")
  
if shutdown == 'лох':
    exit()
else:
    os.system("shutdown /s /t 1")