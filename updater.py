import os.path
import urllib.request
import subprocess
import requests
import shutil
import time
import zipfile
from lib import color

updated = False

def update_check():
    versionfile = open(".version", "r")
    version = versionfile.read()
    versionfile.close()
    repoversion = requests.get("https://raw.githubusercontent.com/Werameli/SwissNetKnife/master/.version").text

    if version != repoversion:
        print(color.yellow)
        print("\nIt looks like we found an update!")
        print(f"Your version {version} needs to be updated to {repoversion}")
        return True
    else:
        print(color.green)
        print("You're up to date! Closing the script...")
        print("NOTE: You need to run loader.py manually!")
        exit(0)


def update():
    print(color.green)
    print("Starting update process...")
    if not os.path.isdir(f"{os.getcwd()}/tmp"):
        os.mkdir(f"{os.getcwd()}/tmp")
    else:
        pass
    time.sleep(2)

    print("Retrieving update files...")
    try:
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Werameli/SwissNetKnife/master/SNK.py",
                                   f"{os.getcwd()}/tmp/SNK.py")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Werameli/SwissNetKnife/master/lib.zip",
                                   f"{os.getcwd()}/tmp/lib.zip")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Werameli/SwissNetKnife/master/.version",
                                   f"{os.getcwd()}/tmp/.version")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/Werameli/SwissNetKnife/master/loader.py",
                                   f"{os.getcwd()}/tmp/loader.py")
    except urllib.request.HTTPError:
        print(color.red)
        print("Fatal error occured while downloading update!")
        print("Please, try again later!")
        exit(0)



    print("Updating files...")
    try:
        os.remove(f"{os.getcwd()}/SNK.py")
        shutil.rmtree(f"{os.getcwd()}/lib")
        os.remove(f"{os.getcwd()}/.version")
        os.remove(f"{os.getcwd()}/loader.py")

        with zipfile.ZipFile(f"{os.getcwd()}/tmp/lib.zip", 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
            zip_ref.close()
        shutil.move(f"{os.getcwd()}/tmp/SNK.py", f"{os.getcwd()}")
        shutil.move(f"{os.getcwd()}/tmp/.version", f"{os.getcwd()}")
        shutil.move(f"{os.getcwd()}/tmp/loader.py", f"{os.getcwd()}")
    except shutil.Error or zipfile.BadZipFile as error:
        print(color.red)
        print(error)
        print("Fatal error occured while updating files!")
        print("Please, contact our developer team to solve the issue!")
        exit(0)

    shutil.rmtree(f"{os.getcwd()}/tmp")
    print(color.green)
    print("Update successful! Closing the script...")
    print("NOTE: You need to run loader.py manually!")
    exit()


subprocess.call(["clear"])
print(f"{color.green}SNK Updater Ver. Alpha 1.1\n(C) Werameli (TeamSNK). All rights reserved")
time.sleep(1)

if __name__ == "__main__":
    if update_check():
        update()