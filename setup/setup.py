import os
import time

packages = ["sys", "urllib3", "importlib", "requests"]

def install_packages():
    try:
        for package in packages:
            os.system(f"pip install {package}")
            print("Installation complete!")
            print("Exiting in 5 seconds...")
            time.sleep(5)
            exit(0)
    except Exception as e:
        print(f"Failed to install required packages due to {e}")


if __name__ == "__main__":
    print("Starting installation of required packages...")
    install_packages()