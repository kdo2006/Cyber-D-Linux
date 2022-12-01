import os
from time import time
import time
from termcolor import colored

updateing="""
|______________________ Updating________________|
  =============================================
"""
updated="""
|__________________ Updated __________________|
 =============================================
"""
logo= """
   ____      _                    ____  
  / ___|   _| |__   ___ _ __     |  _ \ 
 | |  | | | | '_ \ / _ \ '__|____| | | |
 | |__| |_| | |_) |  __/ | |_____| |_| |
  \____\__, |_.__/ \___|_|       |____/ 
       |___/                     [ ~v1.1] 
                                                                             
 """

social_media= """
 ~ Instagram: https://instagram.com/kdo_shashank
 ~ Whatsapp: https://wa.me/+9779746554757
 ~ Telegram: https://t.me/kdobhai
"""

can="""
|__________installation Cancelled____________|
 =============================================
"""
os.system("clear")
print(colored(logo,"blue") + colored(social_media,"red"))

install=input(colored("Do you want to update Cyber-D (y/n):","yellow"))
if install == "y":
    print(colored(updateing,"green"))
    os.system("apt update -y && apt upgrade -y && apt install python3")
    os.system("cd $HOME && rm -rf Cyber-D")
    os.system("cd $HOME && git clone https://github.com/kdo2006/Cyber-D")
    os.system("cd $HOME/Cyber-D/fun && pip install -r fun/req.txt")
    print(colored(updated,"green"))
    time.sleep(0.5)
    os.system("cd $HOME && cd Cyber-D && python3 CyberD.py")
elif install=="n":
    print(colored(can,"green"))
    time.sleep(0.5)
    os.system("python3 CyberD.py")
else:
    print(colored("[!] Invalid Option, Try Again...","red"))
    time.sleep(0.4)
    os.system("clear")
    os.system("python3 CyberD.py")