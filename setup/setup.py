import os
import time

print("Starting installation of required packages...")

os.system('pip3 install sys')
os.system('pip3 install urllib3')
os.system('pip3 install importlib')
os.system('pip3 install requests')

print("Installation complete!")
print("Exiting in 5 seconds...")
time.sleep(5)