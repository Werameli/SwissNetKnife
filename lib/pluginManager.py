import json
import time
import requests
import os
def readrepo():
    with open('repolist.json', 'r') as file:
        data = json.load(file)

    for repo in data['repositories']:
        print(f"\nName: {repo['name']}\nURL: {repo['url']}\n")
        time.sleep(0.5)

def ifrepoexists():
    with open('repolist.json', 'r') as file:
        data = json.load(file)

    if 'repositories' in data and data['repositories']:
        return True
    else:
        return False


def searchinrepo(filename):
    with open('repolist.json', 'r') as file:
        data = json.load(file)

    found_files = []

    for repo in data['repositories']:
        repo_name = repo['url'].replace("https://github.com/", "")
        api_url = f"https://api.github.com/repos/{repo_name}/contents"

        response = requests.get(api_url)

        if response.status_code == 200:
            files = response.json()

            for file_info in files:
                if file_info['type'] == 'file' and file_info['name'] == filename:
                    found_files.append({
                        'repo_name': repo_name,
                        'file_url': file_info['download_url']
                    })
        else:
            print(f"Failed to access {repo_name}: {response.status_code}")

    return found_files


def installation(file_url, destination_folder = "plugins"):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    file_name = os.path.basename(file_url)

    response = requests.get(file_url, allow_redirects=True)

    if response.status_code == 200:
        file_path = os.path.join(destination_folder, file_name)

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"\nDownloaded {file_name} to {destination_folder}")
    else:
        print(f"\nFailed to download {file_name}: {response.status_code}")