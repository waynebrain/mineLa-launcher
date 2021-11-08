import minecraft_launcher_lib as mc
import subprocess
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

def runMC():
    ver = input("Enter the minecraft version to run")
    username =  input("Enter a username you want to use: ")
    import uuid
    uuid = uuid.uuid4().hex
    options = {
        "username": username,
        "uuid" : uuid,
        "token": ""
            }
    mccmd = mc.command.get_minecraft_command(ver , mcdir , options)
    subprocess.call(mccmd)

if __name__ == '__main__':
    if action == "install":

        installMC()
    elif action == "run":
        runMC()

