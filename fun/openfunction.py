import os
from termcolor import colored
import time
from fun.logo import success
def zphisherop():
    user=input(colored("Do you have install zphisher?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && cd zphisher && bash zphisher.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("cd $HOME && cd .tools && git clone https://github.com/htr-tech/zphisher.git")
            os.system("cd $HOME && cd .tools && cd zphisher && bash zphisher.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")

    
        
def Red_Hawkop():
    user=input(colored("Do you have install Red Hawk?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && cd RED_HAWK && php rhawk.php")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install php && apt install php-curl && apt install php-xml ")
            os.system("cd $HOME && cd .tools && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd $HOME && cd .tools && cd RED_HAWK && php rhawk.php")
        elif ask=="n":
            os.system("python3 CyberD.py")

    
def ngrokop():
    print("Hash_Cat")

def MaskPhishop():
    user=input(colored("Do you have install MaskPhish?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && cd maskphish && bash maskphish.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install php")
            os.system("cd $HOME && cd .tools && git clone https://github.com/jaykali/maskphish")
            os.system("cd $HOME && cd .tools && cd maskphish && bash maskphish.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def infectop():
    user=input(colored("Do you have install infect?(y/n):", "red"))
    if user=="y":
       os.system("cd $HOME && cd .tools && cd infect && bash infect.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install python -y &&  apt install python2 -y && pip install lolcat")
            os.system("cd $HOME && cd .tools && git clone https://github.com/noob-hackers/infect")
            os.system("cd $HOME && cd .tools && cd infect && bash infect.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def AndroRatop():
    user=input(colored("Do you have install AndroRAT?(y/n):", "red"))
    if user=="y": 
        p=input(colored("port:","yellow"))
        a=input(colored("apk name:","yellow"))
        os.system("cd $HOME && cd .tools && cd AndroRAT &&  python3 androRAT.py -h")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install wget && wget && https://raw.githubusercontent.com/MasterDevX/java/master/installjava && bash installjava")
            os.system("cd $HOME && cd .tools && git clone https://github.com/karma9874/AndroRAT.git")
            os.system("cd $HOME && cd .tools && cd AndroRAT && pip install -r requirements.txt")
        elif ask=="n":
            os.system("python3 CyberD.py")


def IPTrackerop():
    user=input(colored("Do you have install IP Tracker?(y/n):", "red"))
    if user=="y":
        ip=input(colored("Input the Ip:","red"))
        os.system("cd $HOME && cd .tools && cd ip-tracker && python iptracker.py "+ ip)
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            ip=input(colored("Input the Ip:","red"))
            os.system("cd $HOME && cd .tools && git clone https://github.com/lucasfarre/ip-tracker.git")
            os.system("cd $HOME && cd .tools && cd ip-tracker && python iptracker.py "+ ip)
        elif ask=="n":
            os.system("python3 CyberD.py")


def PyPhisherop():
    user=input(colored("Do you have install PyPhisher?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && cd PyPhisher && python3 pyphisher.py")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install git python3 php openssh -y")
            os.system("cd $HOME && cd .tools && git clone https://github.com/KasRoudra/PyPhisher")
            os.system("cd $HOME && cd .tools && cd PyPhisher && pip3 install -r files/requirements.txt && python3 pyphisher.py")
        elif ask=="n":
            os.system("python3 CyberD.py")


def kalimuxop():
    user=input(colored("Do you have install kalimux?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME &&  cd .tools && cd kalimux && sh kalimux.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pip install lolcat")
            os.system("cd $HOME &&  cd .tools && git clone https://github.com/noob-hackers/kalimux")
            os.system("cd $HOME &&  cd .tools && cd kalimux && sh kalimux.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def PhoneInfogaop():
    user=input(colored("Do you have install Phone Infoga?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME &&  cd .tools && cd PhoneInfoga && phoneinfoga.py -h")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("cd $HOME && cd .tools && git clone https://github.com/sundowndev/PhoneInfoga")
            os.system("cd $HOME &&  cd .tools && cd PhoneInfoga && python3 -m pip install -r requirements.txt && phoneinfoga.py -h")
        elif ask=="n":
            os.system("python3 CyberD.py")



def T_Bomberop():
    user=input(colored("Do you have install T-Bomb?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME &&  cd .tools && cd TBomb && ./TBomb.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install python -y  && cd $HOME && cd .tools && git clone https://github.com/TheSpeedX/TBomb.git ")
            os.system("cd $HOME && cd .tools && cd TBomb && ./TBomb.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def metasploitop():
    user=input(colored("Do you have install Metasploit?(y/n):", "red"))
    if user=="y":
        os.system("msfconsole")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install wget  && wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh ")
            os.system("chmod +x metasploit.sh && ./metasploit.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")

def mrphishop():
    user=input(colored("Do you have install mrphish?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && cd mrphish && bash setup && bash mrphish")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
           os.system("pip install lolcat  && cd $HOME && cd .tools && git clone https://github.com/noob-hackers/mrphish ")
           os.system("cd $HOME && cd .tools && cd mrphish && bash setup && bash mrphish")
        elif ask=="n":
            os.system("python3 CyberD.py")


def IpHackop():
    user=input(colored("Do you have install IpHack?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && bash install.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pip install pyproxify && pip install ua-headers && pip install requests && pip install torpy==1.1.6 && pip install eventlet==0.33.1")
            os.system("cd $HOME && cd .tools && wget --no-check-certificate https://raw.githubusercontent.com/mishakorzik/IpHack/main/install.sh")
            os.system("cd $HOME && cd .tools && bash install.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def tunnelop():
    user=input(colored("Do you have install Tunnel?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && cd tunnel && bash tunnel.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("pip install lolcat  && cd $HOME && cd .tools && git clone https://github.com/noob-hackers/tunnel")
            os.system("cd $HOME && cd .tools && cd tunnel && bash tunnel.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


def Slowlorisop():
    user=input(colored("Do you have install Slowlorisop?(y/n):", "red"))
    if user=="y":
        web=input(colored("example.com:","red"))
        os.system("cd $HOME && cd .tools && cd slowloris && python3 slowloris.py " + web)
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            web=input(colored("example.com:","red"))
            os.system("cd $HOME && cd .tools && git clone https://github.com/gkbrk/slowloris.git")
            os.system("cd $HOME && cd .tools && cd slowloris && python3 slowloris.py " + web)
        elif ask=="n":
            os.system("python3 CyberD.py")

def social_boxop():
    user=input(colored("Do you have install Social_box?(y/n):", "red"))
    if user=="y":
        os.system("cd $HOME && cd .tools && cd SocialBox-Termux && chmod +x install-sb.sh")
        os.system("./install-sb.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("cd $HOME && cd .tools && git clone https://github.com/samsesh/SocialBox-Termux.git")
            os.system("cd $HOME && cd .tools && cd SocialBox-Termux && chmod +x install-sb.sh")
            os.system("./install-sb.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")

def osi_igop():
    user=input(colored("Do you have install osi.ig?(y/n):", "red"))
    if user=="y":
        userid=input(colored("User id without @:","yellow"))
        os.system(" cd $HOME && cd .tools && cd osi.ig && pip install -r requirements.txt")
        os.system("python3 main.py -u " + userid)
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("cd $HOME && cd .tools && git clone https://github.com/th3unkn0n/osi.ig.git")
            os.system(" cd $HOME && cd .tools && cd osi.ig && pip install -r requirements.txt")
            userid=input(colored("User id without @:","yellow"))
            os.system("python3 main.py -u " + userid)
        elif ask=="n":
            os.system("python3 CyberD.py")
def cmatrixop():
    user=input(colored("Do you have install Cmatrix?(y/n):", "red"))
    if user=="y":
        os.system("cmatric")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install cmatrix && cmatrix")
        elif ask=="n":
            os.system("python3 CyberD.py")

def CamPhisherop():
    user=input(colored("Do you have install CamPhish?(y/n):", "red"))
    if user=="y":
        os.system(" cd $HOME && cd .tools && cd CamPhish")
        os.system("bash camphish.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system(" cd $HOME && cd .tools && cd CamPhish && bash camphish.sh")
            print(colored(success,"green"))
            time.sleep(0.9)
            os.system(" cd $HOME && cd .tools && cd CamPhish")
            os.system("bash camphish.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")
    
def DarkFlyop():
    user=input(colored("Do you have install DarkFly?(y/n):", "red"))
    if user=="y":
        os.system("DarkFly")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system("apt install python2 && cd $HOME && cd .tools && git clone https://github.com/Ranginang67/DarkFly-Tool")
            print(colored(success,"green"))
            time.sleep(0.9)
            os.system(" cd $HOME && cd .tools && cd DarkFly-Tool && python2 install.py")
        elif ask=="n":
            os.system("python3 CyberD.py")

def seekerop():
    user=input(colored("Do you have install Seeker?(y/n):", "red"))
    if user=="y":
        os.system(" cd $HOME && cd .tools && cd seeker && chmod +x install.sh && ./install.sh")
    elif user=="n":
        ask=input(colored("Do you want to install it:(y/n):","yellow"))
        if ask == "y":
            os.system(" cd $HOME && cd .tools && git clone https://github.com/thewhiteh4t/seeker.git")
            print(colored(success,"green"))
            time.sleep(0.9)
            os.system(" cd $HOME && cd .tools && cd seeker && chmod +x install.sh && ./install.sh")
        elif ask=="n":
            os.system("python3 CyberD.py")


# fixed no change
def exitop():
    print(colored("Thanks","red") + colored(" For","green") + colored(" Using","blue"))
    os.system("python3 CyberD.py")