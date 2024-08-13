import json
import time
def readrepo():
    with open('../repolist.json', 'r') as file:
        data = json.load(file)

    for repo in data['repositories']:
        print(f"Name: {repo['name']}\n URL: {repo['url']}\n Description: {repo['description']}\n")
        time.sleep(0.5)

def ifrepoexists():
    with open('../repolist.json', 'r') as file:
        data = json.load(file)

    if 'repositories' in data and data['repositories']:
        return True
    else:
        return False