import os
from time import time
import time
from termcolor import colored
from fun.logo import about1, about2, about3, about4, logo, social_media, updateab, aboutupdate, uninstalled, success, can

def zphisher():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && git clone https://github.com/htr-tech/zphisher.git")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd zphisher && bash zphisher.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")
        
    
        
def Red_Hawk():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("apt install php && apt install php-curl && apt install php-xml ")
        os.system("cd $HOME && cd .tools && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd RED_HAWK && php rhawk.php")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")
    
def ngrok():
    print("Hash_Cat")

def MaskPhish():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("apt install php")
        os.system("cd $HOME && cd .tools && git clone https://github.com/jaykali/maskphish")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd maskphish && bash maskphish.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def infect():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("apt install python -y &&  apt install python2 -y && pip install lolcat")
        os.system("cd $HOME && cd .tools && git clone https://github.com/noob-hackers/infect")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd infect && bash infect.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def AndroRat():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("apt install wget && wget && https://raw.githubusercontent.com/MasterDevX/java/master/installjava && bash installjava")
        os.system("cd $HOME && cd .tools && git clone https://github.com/karma9874/AndroRAT.git")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd AndroRAT && pip install -r requirements.txt")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def IPTracker():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        ip=input(colored("Input the Ip:","red"))
        os.system("cd $HOME && cd .tools && git clone https://github.com/lucasfarre/ip-tracker.git")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd ip-tracker")
        os.system("python iptracker.py "+ ip)
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def PyPhisher():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("apt install git python3 php openssh -y")
        os.system("cd $HOME && cd .tools && git clone https://github.com/KasRoudra/PyPhisher")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd PyPhisher && pip3 install -r files/requirements.txt && python3 pyphisher.py")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def kalimux():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat")
        os.system("cd $HOME && cd .tools && git clone https://github.com/noob-hackers/kalimux")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd kalimux && sh kalimux.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def PhoneInfoga():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && git clone https://github.com/sundowndev/PhoneInfoga")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd PhoneInfoga && python3 -m pip install -r requirements.txt && phoneinfoga.py -h")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def T_Bomber():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("apt install python -y  && cd $HOME && cd .tools && git clone https://github.com/TheSpeedX/TBomb.git ")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system(" cd $HOME && cd .tools && cd TBomb && ./TBomb.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def metasploit():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("apt install wget  && wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh ")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("chmod +x metasploit.sh && ./metasploit.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def mrphish():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat  && cd $HOME && cd .tools && git clone https://github.com/noob-hackers/mrphish ")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd mrphish && bash setup && bash mrphish")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def IpHack():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install pyproxify && pip install ua-headers && pip install requests && pip install torpy==1.1.6 && pip install eventlet==0.33.1")
        os.system("wget --no-check-certificate https://raw.githubusercontent.com/mishakorzik/IpHack/main/install.sh")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("bash install.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def tunnel():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("pip install lolcat  && cd $HOME && cd .tools && git clone https://github.com/noob-hackers/tunnel")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd tunnel && bash tunnel.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def Slowloris():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        web=input(colored("example.com:","red"))
        os.system("cd $HOME && cd .tools && git clone https://github.com/gkbrk/slowloris.git")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cd $HOME && cd .tools && cd slowloris")
        os.system("python3 slowloris.py " + web)
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def social_box():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && git clone https://github.com/samsesh/SocialBox-Termux.git")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system(" cd $HOME && cd .tools && cd SocialBox-Termux && chmod +x install-sb.sh")
        os.system("./install-sb.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def osi_ig():
    user=input(colored("Do you want to install it?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && git clone https://github.com/th3unkn0n/osi.ig.git")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system(" cd $HOME && cd .tools && cd osi.ig && pip install -r requirements.txt")
        userid=input(colored("User id without @:","yellow"))
        os.system("python3 main.py -u " + userid)
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def cmatrix():
    user=input(colored("Do you want to cmatrix?(y/n):", "red"))
    if user=="y":
        os.system("apt install cmatrix")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system("cmatrix")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def CamPhisher():
    user=input(colored("Do you want to CamPhisher?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && git clone https://github.com/techchipnet/CamPhish")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system(" cd $HOME && cd .tools && cd CamPhish && bash camphish.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")
def DarkFly():
    user=input(colored("Do you want to Rudrastra(M?(y/n):", "red"))
    if user=="y":
        os.system("apt install python2")
        os.system(" cd $HOME && cd .tools && git clone https://github.com/Ranginang67/DarkFly-Tool")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system(" cd $HOME && cd .tools && cd DarkFly-Tool && python2 install.py")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")

def seeker():
    user=input(colored("Do you want to Seeker?(y/n):", "red"))
    if user=="y":
        os.system(" cd $HOME && cd .tools && git clone https://github.com/thewhiteh4t/seeker.git")
        print(colored(success,"green"))
        time.sleep(0.9)
        os.system(" cd $HOME && cd .tools && cd seeker && chmod +x install.sh && ./install.sh")
    elif user=="n":
        print(colored(can,"green"))
        time.sleep(0.9)
        os.system("clear")
        os.system("python3 CyberD.py")



# fixed no change
def update():
    os.system("cd fun && python3 update.py")
    
def exit():
    print(colored("Thanks","red") + colored(" For","green") + colored(" Using the Tool","blue"))
    os.system("exit")



# Fixed No change
def about():
    os.system("clear")
    print(colored(logo,'blue') + colored(social_media,'red'))
    print(colored(about1,"green",attrs=['reverse', 'blink']) + (colored(about2,"yellow")) + (colored(about3,"red",attrs=['reverse', 'blink'])) + colored(about4,"blue") + (colored(updateab,"blue",attrs=['reverse', 'blink'])) + colored(aboutupdate,"red"))
    what=input(colored("{0}--exit:","yellow"))
    if what=="0":
        os.system("python3 CyberD.py")
    else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        os.system("clear")
        os.system("python3 CyberD.py")
def uninstall():
    os.system("cd $HOME && rm -rf Cyber-D && rm -rf .tools")
    print(colored(uninstalled,"red"))
    time.sleep(0.9)
    os.system("cd $HOME")
def check():
    os.system("cd $HOME && cd .tools && ls")
    time.sleep(2.5)
    os.system("python3 CyberD.py")