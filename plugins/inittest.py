import lib.globalplaceholders as gph

def SNKInit():
    return {
        "name": "PluginExample",
        "vendor": "Werameli",
        "version": gph.version,
        "description": "Example plugin with simple functions and init function"
    }

def init():
    print(f"PluginExample has been initiated!")

def cleanup():
    print("PluginExample is cleaning up!")