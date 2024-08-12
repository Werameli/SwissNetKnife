import os
import cmd
import requests
import subprocess
import time

import lib.ascii as art
import lib.color as color

subprocess.call(["clear"])

if os.getenv("LOADED") == "True":
    pass
else:
    print("Illegal Launch! Can't launch script without loader")
    print("Launch loader.py to proceed with script launching!")
    exit(120)

art.borderstripe()

art.menuart()

art.borderstripe()

print("\nCollection of scripts for various network tasks")
print(f"Release: Ver. Alpha 1.1\nRemember to run 'pkgman check' every week!\n")

class SNK_Shell(cmd.Cmd):
    intro = f"SwissNetKnife Shell\n(C) TeamSNK. All rights reserved\n"
    prompt = "SNK@localhost $>"

    def do_help(self, arg):
        print("TIP: To choose option from list just type 'run yournumber'")
        print("")
        print("Available commands:")
        print("list - show ASCII-based list of all SNK's scripts")
        print("run - run desired script")
        print("pkgman - SNK's Package Manager")
        print("clear - clear terminal")
        print("restart - restart script")
        print("quit - quit SNK")

    def do_quit(self, arg):
        exit(0)

    def do_pkgman(self, arg):
        match arg:
            case "check":
                versionfile = open(".version", "r")
                version = versionfile.read()
                versionfile.close()
                repoversion = requests.get("https://raw.githubusercontent.com/Werameli/SwissNetKnife/master/.version").text

                print(color.yellow)
                print(f"Your version is {version}")
                print(f"Latest version on repo is {repoversion}")
                if version != repoversion:
                    print("\nYou need to update!")
                    print(f"Your version {version} needs to be updated to {repoversion}")
                    print(f"Run 'pkgman update' to initialize update process")
                    print(color.green)
                else:
                    print(color.green)
                    print("You're up to date!\n")

            case "update":
                updaterequest = input("Do you wish to start update process? (y/n) ")
                if updaterequest.lower() == "y":
                    os.environ['LOADED'] = str(False)
                    subprocess.Popen(["python3", "updater.py"])
                    exit(0)
                else:
                    pass

            case _:
                print("Available commands:")
                print("check - check is there's a newer version of a script")
                print("update - start update process if there's a newer version of a script")
                print("(UNRELEASED) install - install various plugins")

    def do_restart(self, arg):
        print("Restarting...")
        time.sleep(2)
        os.environ['LOADED'] = str(False)
        subprocess.Popen(["python3", "loader.py"])
        exit(0)

    def do_clear(self, arg):
        subprocess.call(["clear"])

    def do_list(self, arg):
        art.scriptlist()

    def default(self, arg):
        print(f"{color.red}Unknown command. Type 'help' for a list of available commands")
        print(color.green)

if __name__ == '__main__':
    try:
        SNK_Shell().cmdloop()
    except KeyboardInterrupt:
        exit(0)
