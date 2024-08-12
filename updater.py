import urllib.request
import subprocess
import requests
import lib.color as color
import time
import zipfile
import os


def update_check():
    versionfile = open(".version", "r")
    version = versionfile.read()
    versionfile.close()
    repoversion = requests.get("https://pastebin.com/raw/hVGYiDqt").text

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
    time.sleep(2)

    print("Retrieving and updating SNK.py")
    try:
        urllib.request.urlretrieve("https://placeholder.com/repo/public/SNK", "SNK.py")
    except urllib.request.HTTPError:
        print(color.red)
        print("Fatal error occured while downloading update!")
        print("Please, try again later!")
        exit(0)

    print("Retrieving libraries...")
    try:
        urllib.request.urlretrieve("https://placeholder.com/repo/public/lib.zip", "lib.zip")
    except urllib.request.HTTPError:
        print(color.red)
        print("Fatal error occured while downloading update!")
        print("Please, try again later!")
        exit(0)

    print("Updating libraries...")
    try:
        with zipfile.ZipFile("lib.zip", 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
    except zipfile.BadZipFile:
        print(color.red)
        print("Fatal error occured while installing libraries!")
        print("Please, contact our developer team to solve the issue!")
        exit(0)

    return True


subprocess.call(["clear"])
print(f"{color.green}SNK Updater Ver. Alpha 1.0")
time.sleep(1)

if update_check():
    update()

if update():
    print(color.green)
    print("Update successful! Closing the script...")
    print("NOTE: You need to run loader.py manually!")
