import os
import cmd
import requests
import subprocess
import time

from lib import color as color, ascii as art, pluginManager as plugman, globalplaceholders as gph

class SNK_Shell(cmd.Cmd):
    intro = f"SwissNetKnife Shell\n(C) Werameli (TeamSNK). All rights reserved\n"
    prompt = "SNK@localhost $>"

    def do_help(self, arg):
        print("TIP: To choose option from list just type 'run yournumber'")
        print("")
        print("Available commands:")
        print("list - show ASCII-based list of all SNK's scripts")
        print("run - run desired script")
        print("pkgman - SNK's Package Manager")
        print("plugman - SNK's Plugin Manager")
        print("clear - clear terminal")
        print("restart - restart script")
        print("quit - quit SNK")

    @staticmethod
    def do_quit(arg):
        exit(0)

    @staticmethod
    def do_pkgman(arg):
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
                print("update - start update process if there's a newer version of a script\n")

    def do_plugman(self, arg):
        global result
        match arg:
            case "install":
                if plugman.ifrepoexists():
                    print("Reading repolist...")
                    plugman.readrepo()
                    pkg = input("Enter package name: ")
                    pkgsearch = plugman.searchinrepo(pkg)
                    if pkgsearch:
                        for result in pkgsearch:
                            print(f"\nFile found in repository: {result['repo_name']}")
                    install = input("\nProceed with installation? [Y/N] ")
                    if install.lower() == "y":
                        plugman.installation(result['file_url'])
                    else:
                        print("Installation aborted!")
                else:
                    print("Repolist is empty! Consider adding repositories via 'plugman repoadd'")
            # case "unload":
            #     user_input = input("Enter the name of the plugin to unload (or 'all' to unload all): ")
            #     plugman.unloader(user_input)
            case "list":
                plugman.loaded_list()
            case "repoadd":
                reponame = input("Insert repository name: ")
                repourl = input("Insert repository url:")
                plugman.add_repository(reponame, repourl)
            case _:
                print("Available commands:")
                print("install - install various plugins")
                print("(UNFINISHED) unload - unload plugin(s)")
                print("list - shows a list of all loaded plugins")
                print("repoadd - add plugins repositories to the repolist\n")


    @staticmethod
    def do_restart(arg):
        print("Restarting...")
        time.sleep(2)
        os.environ['LOADED'] = str(False)
        subprocess.Popen(["python3", "loader.py"])
        exit(0)

    @staticmethod
    def do_clear(arg):
        subprocess.call(["clear"])

    @staticmethod
    def do_list(arg):
        art.scriptlist()

    def default(self, arg):
        print(f"{color.red}Unknown command. Type 'help' for a list of available commands")
        print(color.green)


if __name__ == '__main__':
    subprocess.call(["clear"])

    if os.getenv("LOADED") == "True":
        pass
    else:
        print("Illegal Launch! Can't launch script without loader")
        print("Launch loader.py to proceed with script launching!")
        exit(120)

    print("Initializing plugins...")
    time.sleep(2)
    plugman.initialization()
    subprocess.call(["clear"])

    art.borderstripe()

    art.menuart()

    art.borderstripe()

    print("\nCollection of scripts for various network tasks")
    print(f"Release: Ver. {gph.version}\nRemember to run 'pkgman check' every week!\n")
    SNK_Shell().cmdloop()