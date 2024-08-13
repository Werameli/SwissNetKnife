import json
import time
import requests
import os
import importlib.util
# import sys
from datetime import datetime

loaded_plugins = {}
# filename = {}

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


def inject_shell_commands(shell_instance, module):
    if hasattr(module, 'ShellIntegrations'):
        shell_integrations_class = getattr(module, 'ShellIntegrations')
        shell_integrations_instance = shell_integrations_class()

        for attr_name in dir(shell_integrations_instance):
            attr = getattr(shell_integrations_instance, attr_name)
            if callable(attr) and hasattr(attr, '_is_shell_command'):
                command_name = attr_name
                setattr(shell_instance.__class__, command_name, attr)


def initialization(shell_instance):
    global loaded_plugins
    plugin_folder = "plugins"
    plugin_files = [f for f in os.listdir(plugin_folder) if f.endswith(".py")]

    if not plugin_files:
        print("No plugin files found in the 'plugins' directory. Skipping...")
    else:
        for filename in plugin_files:
            file_path = os.path.join(plugin_folder, filename)
            module_name = filename[:-3] \

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)

            try:
                spec.loader.exec_module(module)
                print(f"Loaded module: {filename}")
            except Exception as e:
                print(f"Failed to load module: {filename} due to {e}")
                time.sleep(4)
                continue

            if hasattr(module, 'PlugInfo'):
                plug_info_class = getattr(module, 'PlugInfo')
                plug_info_instance = plug_info_class(shell_instance)

                metadata = plug_info_instance.SNKInit()
                plugin_name = metadata.get("name", module_name)
                loaded_plugins[plugin_name] = plug_info_instance

                print(f"Loading plugin: {plugin_name}")

                plug_info_instance.init()

                inject_shell_commands(shell_instance, module)

                print(f"Plugin '{plugin_name}' loaded successfully.")
            else:
                print(f"{filename} does not contain 'PlugInfo' class. Skipping...")
        time.sleep(2)

# def reloader(plugin_name):
#     plugin_folder = "plugins"
#
#     if plugin_name in loaded_plugins:
#         plug_info_instance = loaded_plugins[plugin_name]
#         print(f"Reloading plugin: {plugin_name}")
#
#         plug_info_instance.cleanup()
#
#         module_name = plug_info_instance.__class__.__module__
#         del sys.modules[module_name]
#         del loaded_plugins[plugin_name]
#
#         shell_instance = plug_info_instance.shell_instance
#         file_path = os.path.join(plugin_folder, module_name + ".py")
#
#         spec = importlib.util.spec_from_file_location(module_name, file_path)
#         module = importlib.util.module_from_spec(spec)
#
#         try:
#             spec.loader.exec_module(module)
#             print(f"Reloaded module: {module_name}.py")
#         except Exception as e:
#             print(f"Failed to reload module: {module_name}.py due to {e}")
#             time.sleep(5)
#             return
#
#         if hasattr(module, 'PlugInfo'):
#             plug_info_class = getattr(module, 'PlugInfo')
#             plug_info_instance = plug_info_class(shell_instance)
#
#             metadata = plug_info_instance.get_metadata()
#             plugin_name = metadata.get("name", module_name)
#             loaded_plugins[plugin_name] = plug_info_instance
#
#             print(f"Reloading plugin: {plugin_name}")
#
#             plug_info_instance.init()
#
#             inject_shell_commands(shell_instance, module)
#
#             print(f"Plugin '{plugin_name}' reloaded successfully.")
#         else:
#             print(f"{module_name}.py does not contain 'PlugInfo' class. Skipping...")
#     else:
#         print(f"Plugin '{plugin_name}' is not currently loaded.")
#
# def reload_plugins():
#     global loaded_plugins
#     for plugin_name in list(loaded_plugins.keys()):
#         reloader(plugin_name)

def loaded_list():
    print("\nLoaded plugins:")
    if loaded_plugins:
        for plugin_name in loaded_plugins:
            print(f" - {plugin_name}")
    else:
        print("No plugins were loaded.\n")


def add_repository(reponame, repourl):
    json_file_path = 'repolist.json'

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    else:
        data = {"repositories": []}


    new_repo = {
        "name": reponame,
        "url": repourl,
        "created_at": datetime.now().strftime("%Y-%d-%m")
    }

    data["repositories"].append(new_repo)

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Repository '{reponame}' added successfully!")