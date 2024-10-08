import os.path
import platform
import time
import requests
import subprocess
import updater
import sys
from lib import color, resolution, globalplaceholders as gph

filename = "SNK.py"
libraries = ["ascii.py", "color.py", "resolution.py", "pluginManager.py"]
loaded = False


class rescuemode:
    @staticmethod
    def checkconnection():
        try:
            requests.get("https://google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    @staticmethod
    def terminal():
        print(color.white)
        inputstring = ""
        while inputstring != "exit":
            inputstring = input("rescuemode | $ ")
            match inputstring:
                case "help":
                    print("WARNING: If you haven't got updater.py this script won't help you as it's necessary to it")
                    print(
                        "NOTE: If you missing repolist.json file, just run 'repocreate'. However if you're missing .version file you need to run 'rescue' command")
                    print("AVAILABLE COMMANDS:")
                    print("help - get this page")
                    print("rescue - redownload all necessary files")
                    print("repocreate - create empty repolist.json")
                    print("exit - exit rescue mode")
                case "rescue":
                    updater.update()
                case "repocreate":
                    os.mknod("repolist.json")
                case "exit":
                    exit(0)
                case _:
                    print("Invalid command. Type 'help' for help")


class initScripts:
    @staticmethod
    def syscheck():
        if platform.system() == "Linux":
            pass
        else:
            print("SNK only supports Linux systems!")
            print("Exiting in 5 seconds!")
            exit(0)

        if platform.python_version() < "3.10":
            print("Unsupported Python version!")
            print("Please consider using Python 3.10 or later!")
            print("Exiting in 5 seconds!")
            exit(0)

        time.sleep(0.5)

    @staticmethod
    def rescheck():
        terminalsize = resolution.get_resolution()

        if terminalsize < (150, 30):
            print(f"{color.red}Your terminal size is incorrect!")
            print("Change your terminal size to minimal required size: "
                  "150 columns (Width) and 30 lines (Height) or enter fullscreen mode")
            print("Loading process will continue after you change your terminal size!")
            while terminalsize < (150, 30):
                time.sleep(1)
                terminalsize = resolution.get_resolution()
            print(color.green)
        else:
            time.sleep(0.5)
            pass

    @staticmethod
    def filecheck():
        if os.path.isfile(filename):
            time.sleep(0.5)
            pass
        else:
            print(f"{color.red}Critical error! Script not found!")
            print("Entering rescue mode!")
            if rescuemode.checkconnection():
                rescuemode.terminal()
            else:
                print("No internet connection! Unable to use RescueMode.")
                exit(0)

    @staticmethod
    def libcheck():
        for library in libraries:
            libfolder = os.path.join("lib", library)
            if os.path.isfile(libfolder):
                pass
            else:
                print(f"{color.red}Critical error! Necessary libraries not found!")
                print("Entering rescue mode!")
                rescuemode.terminal()
        time.sleep(0.5)

    @staticmethod
    def adcheck():
        if os.path.isfile(".version") and os.path.isfile("repolist.json"):
            pass
        else:
            print(f"{color.red}Critical error! repolist.json or .version not found!")
            print("Entering rescue mode!")
            rescuemode.terminal()
        time.sleep(1)


if __name__ == "__main__":
    subprocess.call(["clear"])
    print(f"{color.green}SNK Loader Ver. {gph.version}(C) Werameli (TeamSNK). All rights reserved\n")
    time.sleep(1)

    print("Cheking system...")
    initScripts.syscheck()

    print("Checking terminal resolution...")
    initScripts.rescheck()

    print("Checking script file availability...")
    initScripts.filecheck()

    print("Checking libraries integrity...")
    initScripts.libcheck()

    print("Checking additional files integrity")
    initScripts.adcheck()

    print("\n")
    for i in range(5):
        time.sleep(0.1)
        print("\033[1;32;40mLOADING SWISSNETKNIFE...")
    time.sleep(1)
    os.environ['LOADED'] = str(True)
    try:
        if sys.argv[1] == "-d" or "--debug" in sys.argv:
            print(color.red)
            print("WARNING! Debug mode is ENABLED!")
            print(color.green)
            time.sleep(1)
            subprocess.run(["python3", "SNK.py"], check=False)
        else:
            subprocess.run(["python3", "SNK.py"], check=False, stderr=subprocess.DEVNULL)
    except KeyboardInterrupt:
        if sys.argv[1] == "-d" or "--debug" in sys.argv:
            exit(0)
        else:
            subprocess.call(["clear"])
            print("Detected CTRL+C! Exiting...")
            exit(0)
