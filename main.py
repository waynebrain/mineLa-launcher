#paid minecraft support coming soon
#beta 0.0.1
import time
import minecraft_launcher_lib as mc
import subprocess
import sys
from colorama import init
from colorama import Fore,Back,Style
init(autoreset=True)
from termcolor import cprint
from mojanglogin import loginintomc
mcdir = mc.utils.get_minecraft_directory()

action = input("Would you like to install or run minecraft: ")



def installMC():
    verinstall = input("Enter minecraft version to install: ")
    #callback mandatory for install
    current_max = 0
    def set_status(status):
        print(status)
    def set_progress(progress):
        if current_max != 0 :
            print("{}/{}".format(progress , current_max))

    def set_max(new_max):
        global current_max
        current_max = new_max

    callback = {
            "setStatus": set_status,
            "setProgress": set_progress,
            "setMax": set_max
    }
    #install minecraft version no optifine or mods supported
    mc.install.install_minecraft_version(verinstall , mcdir , callback=callback)

def runMCcracked():
    print(Fore.RED+Style.BRIGHT+"Enter the minecraft version to run:", end=" ")
    ver = input("")
    #print(Style.RESET_ALL)
    username =  input("Enter a username you want to use: ")
    #huge thanks to @Ezio Auditore on discord for explaining the uuid to me
    import uuid
    uuid = uuid.uuid4().hex
    options = {
        "username": username,
        "uuid" : uuid,
        "token": ""
            }
    mccmd = mc.command.get_minecraft_command(ver , mcdir , options)
    subprocess.call(mccmd)

def runMCpaid():
    #minecraft paid support coming soon
    #userinfo = loginintomc(username , password)
    time.sleep(2)
    fail = "An error ocurred while launching the paid version of minecraft please contact the developer ---> control#6285"
    cprint("{}".format(fail) , "red" , attrs=["bold"])
    time.sleep(1)
    sys.exit(0)
if __name__ == '__main__':
    if action == "install":

        installMC()
    elif action == "run":
        mccheck = input("Are you a cracked or paid player: ").lower()
        if mccheck == "cracked":
            runMCcracked()
        elif mccheck == "paid":
            runMCpaid()
    elif action == "howtocode":
        import webview
        webview.create_window("learn python" , "https://docs.python.org/3/tutorial/")
        webview.start()

